---
title: 'Politics and Propaganda on Social Media: How Twitter and Meta Moderate State-Linked Information
  Operations'
url: https://arxiv.org/abs/2401.02095
category: social-media
subcategory: empirical
date: 2024-01
venue: ''
authors:
- Nihat Mugurtay
- Umut Duygu
- Onur Varol
source: arxiv
pdf_url: https://arxiv.org/pdf/2401.02095
pages: 34
chars: 90139
fetched_at: '2026-11-08T13:04:58+00:00'
kb_version: 1
---

# Politics and Propaganda on Social Media: How Twitter and Meta Moderate State-Linked Information Operations

Politics and Propaganda on Social Media:
How Twitter and Meta Moderate State-Linked
Information Operations
Nihat Mugurtay1, Umut Duygu2, Onur Varol1,3,*
1Faculty of Engineering and Natural Sciences, Sabanci University
2Sabanci University, Faculty of Arts and Social Sciences, Sabanci University
3Center of Excellence in Data Analytics, Sabanci University
*Corresponding author: onur.varol@sabanciuniv.edu
Abstract
Why do Social Media Corporations (SMCs) engage in state-linked in-
formation operations? Social media can significantly influence the global
political landscape, allowing governments and other political entities to
engage in concerted information operations, shaping or manipulating do-
mestic and foreign political agendas. In response to state-linked political
manipulation tactics on social media, Twitter and Meta carried out take-
down operations against propaganda networks, accusing them of interfer-
ing foreign elections, organizing disinformation campaigns, manipulating
political debates and many other issues. This research investigates the
two SMCs’ policy orientation to explain which factors can affect these
two companies’ reaction against state-linked information operations. We
find that good governance indicators such as democracy are significant el-
ements of SMCs’ country-focus. This article also examines whether Meta
and Twitter’s attention to political regime characteristics is influenced
by international political alignments. This research illuminates recent
trends in SMCs’ take-down operations and illuminating interplay between
geopolitics and domestic regime characteristics.
1
arXiv:2401.02095v1  [cs.SI]  4 Jan 2024

Introduction
Political actors are using social media platform to campaign for themselves and
influence political agendas in their countries or international relations. Online
platforms have become tools for social and political contestation, public opinion,
electoral manipulation, disinformation, inauthentic behavior, smear campaigns,
and various other forms of online political activities [1–9]. A number of interna-
tional and domestic measures have been taken in response to these state-linked
concerted actions. SMCs are requested to provide information about activities
on their platforms and mitigation plans by governments and platform users.
Since 2018, Twitter and Meta have initiated numerous take-down operations
against state-linked coordinated activities across the globe. SMCs had vari-
ous reasons for paying attention to specific networks across different countries:
interference in foreign elections, suppression of political opposition, government-
affiliated fake news and social bot accounts, and propaganda aimed at legitimiz-
ing authoritarian regimes. We examine the premises of Twitter’s and Meta’s
response to state-linked information operations. We explore the politics of social
media take-downs originating in many countries, by first exploring the proposed
logic of social media take-downs and then using a regression analysis to capture
a more delicate analysis of multiple variables, we explore the politics of social
media take-downs.
Social media provides a useful modality of public diplomacy, and govern-
ments prioritize their digital existence as a part of their national priorities [10].
At this point, there emerge a complex and interesting phenomenon regarding two
American SMCs’ response to state-linked information operations. The proce-
dure of taking-down users from specific countries does not merely involve a sim-
ple content moderation, but also involves a very close attention to coordinated
and state-linked propaganda channels that disseminate political disinformation
and government propaganda. Scrutinizing multiple users, groups and companies
from different countries, the two SMCs detect concerted political actions which
are linked to the governments. This action is directly political in the sense that
they focus on government-affiliated entities and decide when, where, and what
to moderate. These state-linked actors can be governments, government-related
social media companies, political parties, military, security branches of govern-
ment, individual politicians, municipalities, military, and paramilitary groups
[11]. Therefore, both Twitter and Meta use their own assessment mechanism,
regardless of countries’ or political regions’ de-jure framework. When it comes
to attempting to take down concerted state-affiliated networks, SMCs have a
certain amount of discretion in selecting when, where, and who to target.
In addition, revenue extraction is also vital for investing in other countries.
Giving the fact that content moderation of these companies can be affected
from their commercial interests [12, 13], conducting state-linked disinformation
take downs against governmental entities and private enterprises might result
in disrupting their relations with these governments. This becomes more salient
with the existence authoritarian challenge across the world, where SMCs estab-
lish local partnerships, helping Meta and Twitter to generate more wealth by
2

locational advantages. Social media giants need to establish good relations with
large economies and populations (users) to extract more revenues. On the other
hand, democratic countries as well are also subject to coordinated inauthentic
activities, which is sometimes initiated by pro-US actors [14]. Therefore, SMCs
also respond to state-linked information operations in the Western Hemisphere,
where their main headquarters and decision-making mechanism are located. In
this sense, two US-based social media giants are taking action on multiple fronts
-in a polarizing geopolitical environment- in response to coordinated-political
and state-linked operations. This multi-faceted political, economic, and inter-
national dynamics create a puzzle to uncover which factors are significant for
take-down policies. For instance, Twitter’s last report on state-linked infor-
mation operations was announced just prior to Elon Musk’s acquisition of the
company turning it into a private entity. During the acquisition topics rele-
vant to platform safety such as social bots and misinformation were raised for
discussion [15, 16]. Couple months later, Musk laid off the team responsible
for investigating misinformation campaigns on the platform. Consequently, our
research covers the period between 2018 and 2022, beginning with the SMCs’
reaction against state-linked information operations and Musk’s acquisition of
Twitter.
We examine the factors that can be associated with the take down of Meta
and Twitter by scrutinizing the states associated with these networks. Domestic
political configuration, international politics, and SMCs’ focus on revenue ex-
traction from these countries can be significant factors of their reaction against
state-linked operations. Therefore, we focus on regime types, countries’ inter-
national political positioning, and their potential for revenue extraction. At
this point, we underline that the two American SMCs’ reaction against state-
linked information operations exist in a complex international environment. Cy-
berspace and information operations exist with the increasing salience geopo-
litical setting [17]. We uncover which factors can explain take-down policies of
these corporations.
Building on this puzzle, the challenges of SMCs’ political action become more
diverse and contentious because these companies deal with political spectrum in
multiple countries. This point is significant to show similarities and differences
between the two social media giants. In our initial analysis, we find significant
parallel and diverging patterns in terms of taking down accounts from specific
countries. In this sense, our research scrutinizes Twitter and Meta’s take downs
in two ways: First, we analyze Twitter and Meta’s take-down operations by
utilizing an exploratory analysis on countries involved in these operations. We
provide a detailed information on why they select specific countries also by
analyzing their general discourse and announcements. As a second step, we
offer different regression models to determine which variables explains the take
downs. We test multiple hypotheses regarding democracy, political stability and
violence, and economic indicators.
3

Background on Information Operations
The actions taken by private SMCs against perilous agents are not a novel
phenomenon, yet their policies towards state-linked information operations are
relatively new. The literature on SMCs’ reaction against inauthentic behavior
and online manipulation are mostly associated with content moderation. This
is primarily related to insulting, harassment, hate speech, harmful or illegal
contents which are also mostly within the scope of countries’ domestic legal
framework [18]. Debates on freedom expression [19], SMCs’ attention for com-
mercial interests [12, 13], or regulating content moderation with constitutional
and democratic values [20, 21] have been significant topics for SMCs. Indeed,
SMCs’ action against governments’ information operations go beyond the issues
of content moderation.
A state-linked propaganda campaign involves strategic efforts to sway the
opinions of targeted groups through a variety of communications tactics with
the purpose of achieving a specific outcome [22–24]. Coordinated inauthentic
behavior on social media encompasses political, social, and psychological di-
mensions [25]. Individuals often persistently adhere to false belief [26, 27] and
political actors tend to take the advantage of this misinformation environment.
Disinformation proliferation has manifested a significant increase, transcending
national boundaries and becoming a more globalized concern [28, 29]. Within
this realm, state-linked propaganda as a political communication tool are getting
more attention [30]. Through the involvement of organized groups, online plat-
forms have become an increasingly important component of public diplomacy.
Disinformation comes into play when misinformation, polarization, fake news or
conspiracy theories are deliberately transformed through intentional interven-
tions by governments, political parties, automated bots, coordinated actions by
citizens, and internet trolls[24, 31–41]. Indeed, particularly bots or concerted
disinformation operations are very useful to disseminate low-credible inauthen-
tic content [42–46]. Social and political turmoils [47] –including electoral pe-
riods–are permissive processes for shaping public discourse via disinformation
[48–50]. In such a disinformation environment, government-run inauthentic so-
cial media campaigns grown in response to the mass political mobilizations, and
often intend to manipulate elections [8, 9, 51–53].
Twitter and Meta can take-down users from different countries based on
inter-state or intra-state factors [54]. These two modes of concerted action by
perilous networks has multiple modalities. Within the context of intra-state
objectives, state-affiliated domestic cyber and information maneuvers are fre-
quently tied to governmental strategies aimed at manipulating narratives to gain
support from domestic audience. However, in the international arena, foreign
governments use disinformation strategies and many online manipulation tactics
to influence geopolitical or foreign domestic processes. Digital sphere can also be
an arena of contestation between countries such as China and the United States
[55], and government-linked inauthentic behavior might target other nations and
foreign elections [29, 56]. In both domestic and international realm, fake news,
trolls, disinformation campaigns, conspiracy theories and coordinated authentic
4

or inauthentic actions are the subject matters of these state-linked information
operations [57–59]. With existence of strong authoritarian countries, the issue of
disinformation becomes more interesting to investigate [60]. In addition, demo-
cratic countries also have become an arena of disinformation contest [14, 61, 62].
This makes state-linked information operations more complex because having
alternative source of information [63] (i.e, social media) is crucial point for
democratic regimes. SMCs react against these political manipulation tactics.
Focusing on which countries more likely to get attention from SMCs is worth-
while endeavor to illuminate similar or varying patterns. Deciding on which
country to focus on against state-linked operations entails a in-house consistent
policy-harmonization. Therefore, we also focus on countries’ political orienta-
tion towards the United States and other great powers. In this sense, we also
search for the factors that might dilute regimes characteristics with geopolitical
orientations. At least, we can suggest that the politics of multinationals’ matter
with the existing polarizing international environment [10, 14, 17, 64–66].
Our research is the first in terms of conducting multi-platform analysis on
state-linked information operations. We inquiry the political moment transcend-
ing a comparison of content moderation policies. By this way, we manifest
the trends in take-down strategies. Detecting take-downs and selection specific
groups in different countries entail a policy-vision that illuminate different trends
for SMCs. In this research, our descriptive and inferential research design un-
cover these trends. Overall, estimating possible premises of SMCs’ state-linked
information operations is a substantial contribution to the literature on SMCs’
policy outlook.
The Politics of Twitter and Meta’s Information
Operations
Twitter began to disclose its actions against state-linked information operations
after 2018. We should also note that SMCs can outsource their counter-action
against state-linked information operations. For instance, Stanford Observa-
tory, the institution Twitter cooperates for take-downs, was mentioned in mul-
tiple Twitter reports explaining the logic of state-linked information operations.
Meta also initially mentioned their partnership with Atlantic Council’s Digital
Forensic Lab (DFRLab) in taking-down state-linked political networks. Initially,
users from a selected number of countries were taken-down for their government-
related coordinated behavior. It is crucial to understand that the motivations
behind these take downs vary across countries, as each government engages in
specific coordinated activities to shape their social and political agenda. Twit-
ter justifies these take-downs based on both domestic and foreign (inter-state)
factors [54]. Domestically, Twitter has taken action against accounts involved in
government propaganda against opposition or ethnic minorities. Internationally,
it cites interference in elections on social media as a primary concern [54]. For
instance, Twitter’s action against Iran-linked information operations primar-
5

KII"
D"JJJI
D"J

"D EC
2DCH

HD
 D BI!
ECD"
JL"
IJED"
"J!KD"
HCD"
PH"#D
EH "
#"A"IJDPA"IJD

PA!IJD
EBEL

2H 2PIJD

D"
A"IJD

IHB
" H"
D B
E ED EB
KD"I"
AH"D
	EDKHI
K"H"JH

 !H"D
 2FJEHEE
BIJ"D
DED
EHD
!"D
	ED 

ED
F"D
DPKB
 HP"B
H DJ"D
 EB"L"
HK
KEH
N"E
 IH
DJHBH"DFKB"
EPC"GK
CEHJ"FKB"EJ!ED E
QJR
LE"H
CHEED
KD
"2B H"
 EID"
!D
KH"JD"
"HHED
ECB"
DPD"
"CM

KH"IJD "EDBELHDCDJ
BBLEH
HK K2
!"B
CEHJ"FKB"EED E
!"B"FF"DI
2H"KHA2
FD
 BHKI
HD
B"" H KHA"DIE
EJR
LE"H
!
GKJEH"BK"D
EKJ!H"
 D
!"BD
J!"EF"
 D"D
ECEHEI
IJ DADP

HG
"H K
EJBD
C"
"CMDED E
PH"#D
EIJ"
 !D"IJD
B2I"
P!FKB"
CD
H"
K
#

CAA
  A  )C
"
B! 
A#
 BBBA
 
! ! 

B#

C!#
E"B
C#
C#E
! C#A
 ! A
AB
"C
#
C
# 
)#
 
 ) 
 EC#A
	'!
 B## 

"C
Figure 1: T ake-down operations statistics and country interaction net-
works for different platforms. Countries listed by the number of take-down
operations held in their country. Discrepancies for Meta (left) and Twitter
(right) can be seen by comparing the ranks and the numbers of operations.
Networks of interactions are also presented between countries (nodes) and oper-
ations (edges from targeting to targeted country). Domestic information oper-
ations represented wth self-loops and some of the isolated nodes corresponds to
these countries. Node colors represents the out-strengths to measure activities
of these countries.
ily focused on accounts who allegedly dealt with the US presidential election.
In some other cases, Twitter closures are associated with domestic or ethnic
issues such as Indonesia’s action against West Papua, the 2017 Catalonia’s in-
dependence referendum. In total Twitter focused on 22 countries around the
globe as shown in the supplementary information (SI:Table-1). In Figure 1, we
mapped out top countries that Twitter and Meta’s take action against state-
linked information operations. For example, Twitter has taken down accounts
from Iran and Russia due to their alleged interference in the international af-
fairs and domestic politics of the United States. Also, it took down accounts
originating in China as they involve in Hong Kong and other regional issues. In
some other cases, Russia’s Internet Research Agency (IRA) conduct operations
in Ghana and Nigeria, where suspended accounts dealt with mostly race and
civil rights [67]. These operations are conducted by opening accounts in many
African countries. Twitter were able to detect some of these accounts that are
working for Russian interests, which are directly affiliated with Russia’s IRA.
Saudi Arabia, Turkey, and Venezuela are other examples for Twitter platform
due to their alleged state-linked information operations. For each platform, we
built networks mapping of all information operations and their respective tar-
get countries through directed edges. In Figure 1(right) illustrates that Twitter
has primarily concentrated on perilous networks originating from Saudi Arabia,
China, Egypt, Iran, UAE, and Russia. Overall, Twitter has taken measures
against perilous networks from 22 different countries, leading to the suspension
6

Subjected to T ake-Down Operation
Mann-Whitney Significant (P<0.05)
V-Dem PolyarchyUNGA Voting (US)PVEFreedom House
a.Meta
HIGH SCORE <--------------------------------> LOW SCORE
b.Twitter
Figure 2: Positions of countries in different measures. Ranking of coun-
tries taken down by Meta (left) and Twitter (right) presented as red bars. Each
row presents different state characteristics scores for years between 2018 and
2021.
of several of these networks. However the network constructed from the infor-
mation operations on Meta suggests Iran and Russia are primary actors and
mainly targeting USA.
When compared to Twitter’s reaction against state-linked information oper-
ations, Meta’s Coordinated Inauthentic Behavior (CIB) policy focus on various
countries in many different regions. In total, we collected information about
taken-down perilous networks from 48 countries by Meta, which is significantly
more than reported numbers for Twitter. The corporation mainly focuses on
concerted users from specific countries claiming they violate the Meta’s misrep-
resentation policy. Different from Twitter, Meta announces both state-linked
inauthentic networks and other coordinated political activities under one har-
monized framework. Coordinated inauthentic activities driven by commercial
interests have also been announced by the Meta. Looking at the content of the
Meta suspensions, we also encounter many government-related (executive, mili-
tary, state-linked companies, municipalities) actions examined by the platform.
Meta -for a while- used a specific take-down policy called, Foreign and Govern-
ment Inauthentic Behavior (FGI), aiming to take-down coordinated activities by
such state-linked information operations. However, FGI does not cover all years
between 2018 and 2022. Therefore, we manually checked each announcement
and document related to CIB and created a full list of Meta’s action against
state-linked information operations. We also discovered that even some accounts
publish mainly non-political content about beauty and physical well-being, the
Meta detected that these pages are in affiliation with Myanmar military [68].
7

The platform suggests that celebrity and beauty pages are useful places to boost
state-affiliated networks’ impact. This operation against Myanmar-linked ac-
counts has been explained by Meta’s emphasis on human rights violations and
oppression in the country. In some other instances, Meta revealed a significant
portion of inauthentic networks from Russia, and detected that a group of peo-
ple disguised themselves as journalists and disseminate content about Ukraine
and Crimea. The platform claims that this suspended network was in relation
with the Russian military. In one example, Meta detected a network affiliated
with Islamic Republic of Iran’s Press TV, the main broadcasting apparatus of
Iran [69]. Meta also pays attention to de-facto or de-jure sub-state entities such
as West Bank and Gaza and Kurdistan Regional Government.
We also have some complex cases, where Meta take downs specific non-state
actors such as Muslim Brotherhood , which is an Islamist organization known
by their influence on various Islamist movements from charitable organizations
to political parties. Accounts originated in Egypt, Turkey, and Morocco have
been taken down by Meta accusing them of committing coordinated informa-
tion campaigns [70]. In a different particular case, Meta closed accounts from
Albania, where a group of Iranians exiled in the country committed coordi-
nated inauthentic behavior [71]. In such complex circumstances, we omitted
such governments as targeted by the two SMCs. It is because Turkey, Mo-
rocco, and Albania governments were not designated as a part of state-linked
information operations by the two SMCs directly. In other words, we coded
these countries as being targeted by Twitter and META, if these two SMCs
find out a state-linked information networks. We curated a complete picture
of Meta’s take-down practice by detecting actual state-linked information op-
erations. This entailed an extra layer of hardness to compile Meta’s data in
detail. In the Western hemisphere, the Meta also carried out its operations
against accounts originated countries like Canada and France. In another ex-
ample, Meta suggested that their teams find a coordinated inauthentic behavior
in relation with the French military. At the first sight, as shown in Table 1 in the
SI, Meta’s operations seem geographically diverse and uncover coordinated and
state-linked accounts based on multiple state entity including military, political
party, municipality, and any other governmental entity.
Due to the fact that oscillating regimes towards authoritarianism can oppress
their domestic media and find alternative ways of manipulating audience [72],
both Meta and Twitter appeals to human rights and some other governance-
related humanitarian emphasis when they announce their suspensions. Second,
Twitter and Meta suspend accounts where they see a foreign intervention in
other countries’ domestic or regional politics. This creates a puzzle regarding
their stance based on these premises because there is an important variation in
their country-focus list as seen in Figure 1. This also puts significant questions
about their state-linked operations since we expect a more harmonized approach
due to the global nature of such coordinated misinformation campaigns.
To describe Meta and Twitter’s practice against state-linked information
operations, we ranked countries based on different political variables. In Fig-
ure 2, we present different metrics to provide a basis for comparison, with red
8

bars signifying ranks of these countries that manifest state-linked information
operations on that particular scale. Each row indicates measures used for com-
parison such as V-Dem Polyarchy, political similarity with the United States,
Political Stability and Absence of Violence (PVE) and Freedom House Index
[73, 74]. V-Dem Polyarchy score relies on a robust understanding of democracy,
which inspired from Robert Dahl’s democratic theory. The measure includes
electoral institutions, free press and media and many other civil liberties such
as right to protest [75]. To quantify statistical significance of separation be-
tween the countries taken down by SMCs and other by using Mann-Whitney
test. This test estimates higher scores if two groups of countries differ in terms
of their ranking of the particular metric. For instance, it is visible that countries
(red bars) clustered around the low score V-Dem’s Polyarchy Index, PVE, and
Freedom House meaning that both Meta and Twitter more likely to focus on
countries with lower democracy and freedom scores. Dark blue rectangles next
to ranking plots indicates significant (P-values lower than 0.01) ranking differ-
ences by 95 percent confidence level, while light blue denotes non-significance.
These scores further reinforce the notion that a country’s regime type, freedom
scores and political stability are more significant differentiation than geopolitical
alignments. As Figure 2 illustrates, generally good governance indicators such
as democracy and political stability emerge as the most distinguishing factors
among when compared to geopolitical stances. However, this initial description
needs a more detailed investigation since we still need to detect which premises
are the most relevant when compared to others. This is why we employed a
regression analysis to capture the politics of Meta and Twitter’s information
operations.
Indeed, such an initial observation lead us to key questions: Why does Twit-
ter and Meta specifically focus on certain countries for account take downs,
alleging disinformation and manipulation? Are these actions due to these na-
tions engaging in more disinformation compared to others, or are they driven by
considerations of human rights, democracy, or geopolitical concerns? Twitter
and Meta’s justifications encompass political disinformation elements, making
it vital to discern which state characteristics factor into these take downs.
Hypotheses and Data
Meta and Twitter -as being American multinational SMCs- are giant commer-
cial enterprises that often have complicated relationship with the authoritarian
governments and different regime types [76, 77]. In different circumstances,
authoritarian countries offer permissive or difficult conditions for multinational
international investments. However, this relationship become more salient due
to increasing importance of social media as an alternative source of informa-
tion. Fake news and online manipulation are shown to be effective weapons to
undermine democratic ideals [78]. Both Twitter and Meta mention governance-
related issues such as democracy, elections, justice, and human rights in their
reports, and we expect from both that authoritarian regimes are on the top
9

of their priorities in global information landscape [61, 62]. State-linked infor-
mation operations are also manipulation tools for diverting both domestic and
foreign attention. China, Iran, and Russia are notable instances of information
operations. Particularly, their online intervention in regional and electoral agen-
das are well pronounced by the SMCs. More authoritarian governments can use
social media as a public diplomacy tool to divert the public’s attention from
their oppression. However, we also have other non-authoritarian countries that
were scrutinized by SMCs. It shows that information operations are not unique
to only autocratic governments. However, we need to have a clear measure if
SMCs focus on authoritarian countries more than democratic governments. In
order to identify possible differences between Meta and Twitter’s emphasis on
authoritarian inclinations, we operationalize different political and governance-
related variables.
H1. Social media platforms are more likely to take actions against state-
linked information operations if they originate in more authoritarian countries.
The geographical variation of state-linked information operations may not
be explained solely by regime oscillations and companies’ reactions against more
authoritarian regimes. However, not all authoritarian countries have the same
level of repressiveness or political instability. From another perspective, there
can be more democratic countries with higher levels of political instability and
violence. In democratic countries with higher political instability, political par-
ties and different segments of state bureaucracy can use disinformation and
other online manipulation tactics to convey their propaganda. These less au-
thoritarian countries can be more open to state-linked information operations
including countries such as Mexico, Nigeria, and Ukraine. Alternatively, we can
expect that non-democratic countries with more stability focus on their peo-
ple’s well-being, while some authoritarian countries use their force to oppress
domestic dissent. The Meta documents clearly the emphasize on human-rights
violations committed by oppressive regimes. These regimes are primarily target
the physical integrity of their own population. Large SMCs may take down
accounts originating in countries with less political stability, reflecting concerns
about domestic violence and other relevant issues. To examine this hypothesis,
we used the “absence of violence” variable from the World Bank’s Good Gov-
ernance Indicators.
H2. Social media platforms carry out take-down actions against users where
political violence and political instability more likely to take place.
In addition to governance indicators, Cyberspace has been an arena of in-
ternational relations [64]. This space creates a policy pressure on the United
States to be more active against state-linked information operations [65]. In
such a geopolitical environment, some countries are following the footsteps of
great powers and express changing levels of similarity in political outcomes
[79]. We note that both Meta and Twitter are multinational corporations. In
10

        
81*$9RWLQJ6LPLODULW\ZLWK&KLQD





81*$9RWLQJ6LPLODULW\ZLWKWKH86
9'HP3RO\DUFK\,QGH[




        
81*$9RWLQJ6LPLODULW\ZLWK&KLQD





81*$9RWLQJ6LPLODULW\ZLWKWKH86
1DWR0HPEHU


Figure 3: UNGA V oting similarities of countries to US and China.
UNGA voting similarity shows negative association between United States and
China. More democratic countries in V-Dem Polyarchy index have similar vot-
ing pattern to US (left) and Nato members also more likely to align with pref-
erences of US (right).
other words, they can establish local partnerships with other parties, outsource
some of their operations to third parties and open branches in multiple geogra-
phies. They can also be affected from host countries’ political conditions [80].
Although they tend to globalize their commercial activities, they are Ameri-
can multinational SMCs, meaning that their headquarters and decision-making
process take place in the United States. Multinational SMCs are not exempt
from their country-of-origin characteristics and are affected by the international
geopolitical agenda of their home countries [81, 82]. Therefore, international
alignments might be an influential factor for SMCs. United Nations General
Assembly (UNGA) voting patterns is a useful tool to test if countries have a
similar mindset or policy-orientation in international affairs. It should be noted
that UNGA Similarity does not directly manifest the strong de-facto or de-jure
political alliances, but it shows how countries are similar to each other in inter-
national politics. It gives a picture of how countries cast their votes similarly
at the international level. We investigate if multinationals carry out their take-
down operations focusing on the countries with less UNGA voting similarity
or not. With this regard, we expect that international political similarity is a
significant factor of take-down policies of MNCs.
H3. Users originating from countries with higher political similarity to the
United States are less likely to have their accounts taken down by Meta and
Twitter.
Foreign policy and geopolitical concerns are becoming more substantial for
multinational companies [66]. Concerns for human rights and democracy exist
11

in such a geopolitical setting [83]. SMCs operate under the pressure of a geopo-
litical and polarized world where authoritarian countries emerge as contending
actors, and social media operations are part of great power politics [17]. In this
sense, we investigate if Twitter and Meta’s reaction against more authoritarian
counties are moderated by these countries’ political similarity with the United
States or China. To address this, we concentrate on a possible conditional effects
illuminating if good governance indicators (democracy and absence of violence)
interact with great powers’ positioning in international issues. We take this
similarity as a reflection of general political like-mindedness in the international
system (not as a reflection of de-jure or de-facto political alliances). Indeed,
these similarity matters because great powers usually manifest a clear diver-
gence from each other. To illustrate, as seen in the Figure 3, if a country has
a high voting similarity with the United States, then this country more likely
to have a low voting similarity with China between 2000 and 2021. Because
UNGA voting patterns show opposite trends for great powers, we are confident
to use UNGA Voting similarity to measure countries like-mindedness in the po-
litical realm. In Biden-Harris National Security Strategy, China is also defined
as “the only competitor” that has a potential to transform the international
political and economic landscape [84]. We also suggest that China is labelled as
the geostrategic rival by the US authorities. It is also visible that NATO mem-
ber countries have relatively higher UNGA voting similarity with the United
States, indicating how UNGA voting similarity reflects a systemic understand-
ing. Therefore, using UNGA voting similarity with China will be appropriate
to see if it follows our findings on the US case.
There is a geopolitical issue here when it comes to democratic backsliding,
authoritarian regimes and multinational corporations. Moreover, Figure 3 (left)
shows that higher V-Dem Polyarchy scores are associated with more political
similarity with the United States. Therefore, UNGA agreement scores can not
only reflect geopolitical orientations but also a partnership of democratic coun-
tries at the international level. Multinational SMCs are not immune to these
global trends since economic blocks, regionalization, and degrading globalization
are substantial challenges. For instance, home countries call some of their high-
tech companies to return back by channeling significant amount of incentives.
In some other examples, geopolitical changes divert capital from rouge states to
more politically like-minded countries. Therefore, as American multinationals,
Meta and Twitter might more openly examine state-linked information opera-
tions in countries that have a low level of political similarity with the United
States. Here, we do not offer a causal link but we expect a negative associ-
ation between SMCs’ take-down operations and UNGA voting similarity with
the United States.
H4. More authoritarian or oppressive countries with higher political sim-
ilarity to the United States are less likely to be scrutinized by Meta and Twitter.
An important indicator of SMC investments is the number of users and
revenue extracted from a country. SMCs’ global outreach is a useful tool to
12

establish local partnerships and extract more revenue. In simpler terms, large
populations are essential for growing markets and they can be the focus of big
SMCs. In similar fashion, we observe a strong correlation between the popu-
lation and the number of social media users (SI. Fig-2). Therefore, population
can be used to assess the global outreach and power of SMCs.
We also suggest that the economic power of countries may act as a deterrent
for SMCs not to interfere with state-linked operations. A social media com-
pany makes its profit globally as a multinational actor investing in variety of
countries across the globe. They form alliances with local partners for a variety
of profit-making purposes. Consequently, wealthier countries become attrac-
tive economic markets due to increasing business, advertising, and their high
demand for technology. For example, focusing on India and Brazil, and other
countries with emerging markets, SMCs specifically tailor their services to the
domestic audience in these regions.
However, users’ marginal economic contribution also appears to be more im-
portant than the revenue opportunities provided by wealthier countries based
on advertisements, marketing, and other commercial activities. In particular,
average revenue per user (ARPU), which is a key indicator of the profitability,
indicates whether or not SMCs will generate a greater amount of revenue from
one additional user. Generally, revenue generation is centered in regions with
high ARPUs. Currently, we are using regional estimates provided by Meta and
Twitter [85]. Taking down state-linked accounts from countries with higher AR-
PUs could be avoided by Meta and Twitter. In contrast, we do not have ARPU
for all countries. Thus, since ARPU is directly related to GDP per capita, we
use that as proxy for ARPU and assumes adding one more user from countries
with a higher GDP per capita will result in greater revenue for SMCs. Taking
down users from such countries can be costly for SMCs.
H5. Twitter and Meta are less likely to focus on countries with larger
populations and higher GDP per capita.
Research Design
To address the hypothesis introduced in the previous session, we use a binary
dependent variable model, and operationalize different logistic regression mod-
els. These models capture factors that are associated with Twitter and Meta’s
take-downs in particular countries. We first used pooled logistic models to ob-
serve between-unit trends in time with clustered standard errors (CSE). Using
CSE at the country level in pooled models overcome the problems associated
with serial correlation and heteroskedasticity. The first equation shows our first
estimation for non-interaction models. The second equation shows an example
of interaction models of good governance indicators and political similarity with
the United States. For more robustness, we also used linear probability models
to demonstrate if our models follow a similar output pattern as seen in tables 2
and 3 in the supplementary material (SI:Table 2 and 3).
13

Our regression model in Table 1 covers the years between 2018 and 2022,
since Twitter reported state-linked operations until 2022. To analyze and illus-
trate the differences between countries, we marked countries as 1 for all years
between 2018 and 2022 if they experienced a take-down operation by Twitter
or Meta during these years. This also touches the point that Meta and Twitter
handled their reaction to state-linked information operations. They follow these
coordinated networks for a long time to see how they operate [69]. Therefore,
scrutinizing a perilous network can take even two or more years. Even this
might be the case, we used also cross-sectional logistic models with robust stan-
dard errors to capture between-unit variance more clearly. In these models, our
continuous predictors are four-year averages between 2018 and 2022.
To test our hypotheses, we curated a dataset from Twitter and Meta’s official
web pages. We find out that not all Meta’s politics-related focus is addressing
state-linked information operations. We checked each announcement to see if
Meta builds a linkage between inauthentic networks and governments. If they
underline these linkages, then we coded this operation as state-linked.
(1)
log
 P(T=1)
1 − P(T=1)

= β0 + β1V-Dem Polyarchy + β2UNGA(w/USA)
+ β3Political Stability + β4GDP per capita(log)
+ β5Population(log) + ϵ
(2)
log
 P(T=1)
1 − P(T=1)

= β0 + β1V-Dem Polyarchy + β2UNGA(w/USA)
+ β3V-Dem Polyarchy × UNGA(w/USA)
+ β4Political Stability + β5GDP Per Capita(log)
+ β6Population(log) + ϵ
To explore state-characteristics, we provide general datasets and their scores
encompassing regime type, freedoms, corruption, and UN-Voting similarity with
the United States. For each model, we used V-Dem Polyarchy Score [75], Po-
litical Stability and Absence of Violence [73], UN-Voting Similarity estimates
[86], Gross Domestic Product (GDP), and Population from World Bank. We
transformed GDP Per Capita and population with their logarithms in base 10.
According to the variance inflation factors (VIF) provided in the supplementary
material (SI:Table-7), we did not find any multicolliniarity between the V-Dem
Polyarchy Index and Political Stability score.
Since, user statistics is another important indicator of SMCs’ market poten-
tial in a country, we have substituted population data with user statistics and
incorporated our regression models, as detailed in supplementary information
(SI:Table-5). Although this approach provide more robustness to our findings,
we want to point that China, Iran, and Russia (the most scrutinized countries)
lacks official user statistics for these platforms. This explains the reasons we
have to rely on population data instead of user statistics.
14

Table 1: Regression Results (Logit Estimates, Pooled Time-Series)
(1) (2) (3) (4) (5) (6) (7) (8) (9) (10)
Meta Twitter Meta Twitter Meta Twitter Meta Twitter Meta Twitter
V-Dem Polyarchy -2.146*** -3.540*** -1.344 -3.631*** -2.316** -3.731** -0.803 1.641 -1.573 -3.108**
(0.72) (1.19) (0.90) (1.33) (1.08) (1.59) (2.33) (3.38) (1.07) (1.57)
PVE -0.409* 0.059 -0.183 0.198 -0.192 0.244 1.637** 1.332**
(0.21) (0.22) (0.28) (0.39) (0.29) (0.42) (0.64) (0.64)
UNGA Voting (w/USA) 0.806 -2.606 4.292 9.322 -0.022 -3.430
(1.88) (2.31) (5.19) (6.90) (1.96) (2.27)
GDP Per Capita (log) 0.216 0.577** 0.257 0.655** 0.335* 0.626**
(0.18) (0.29) (0.19) (0.29) (0.20) (0.30)
Population (log) 0.640*** 0.841*** 0.652*** 0.862*** 0.690*** 0.848***
(0.16) (0.27) (0.16) (0.27) (0.16) (0.27)
V-Dem Polyarchy × UNGA Voting (w/USA) -5.317 -18.908*
(7.22) (10.92)
PVE × UNGA Voting (w/USA) -6.811*** -4.262**
(2.51) (1.80)
Constant 0.030 -0.482 -0.496 -0.419 -12.649*** -18.639*** -14.113*** -22.723*** -14.351*** -19.096***
(0.39) (0.50) (0.49) (0.60) (3.02) (5.09) (3.88) (5.06) (3.30) (5.03)
Number of clusters 168 168 168 168 168 168 168 168 168 168
Number of observations 672 672 672 672 672 672 672 672 672 672
Table 2: Regression Results (Logit Estimates, Crosssection)
(1) (2) (3) (4) (5) (6) (7) (8) (9) (10)
Meta Twitter Meta Twitter Meta Twitter Meta Twitter Meta Twitter
V-Dem Polyarchy -2.271*** -3.601*** -1.368 -3.691*** -2.471** -3.758** -0.796 2.033 -1.700 -3.105*
(0.73) (1.21) (0.92) (1.35) (1.16) (1.66) (2.55) (3.58) (1.15) (1.64)
PVE -0.460** 0.059 -0.195 0.201 -0.206 0.246 1.788** 1.445**
(0.22) (0.22) (0.30) (0.40) (0.30) (0.44) (0.79) (0.69)
UNGA Voting (w/USA) 1.102 -2.625 5.057 10.712 0.321 -3.470
(2.07) (2.53) (6.02) (7.65) (2.20) (2.40)
GDP Per Capita (log) 0.191 0.588* 0.235 0.664** 0.319 0.637**
(0.18) (0.30) (0.20) (0.30) (0.20) (0.31)
Population (log) 0.665*** 0.839*** 0.680*** 0.861*** 0.719*** 0.851***
(0.16) (0.28) (0.16) (0.28) (0.17) (0.28)
V-Dem Polyarchy × UNGA Voting (w/USA) -5.960 -20.669*
(8.21) (11.82)
PVE × UNGA Voting (w/USA) -7.547** -4.658**
(3.26) (1.88)
Constant 0.122 -0.455 -0.473 -0.392 -12.867*** -18.696*** -14.506*** -23.134*** -14.707*** -19.234***
(0.39) (0.51) (0.50) (0.61) (3.10) (5.16) (4.14) (5.13) (3.45) (5.11)
Number of observations 168 168 168 168 168 168 168 168 168 168
Regarding the political economy of multinational SMCs, we also add the
UNGA Voting Patterns for China in the supplementary material (SI:Table-4).
If there is a moderating effect of UNGA Similarity with the United States, then
we should at least observe a moderating effect of political similarity with China
and Russia. This will provide more robustness if we find such a tendency, re-
flecting the existing environment for take-down operations. Indeed, our main
interest here is to show how UNGA Voting Patterns with the United States
change Meta and Twitter’s attention for more authoritarian countries. Our
exploratory analysis and regression output show significant parallel trends be-
tween Twitter and Meta.
Results and Discussion
Our pooled and cross-sectional logit estimates show significant implications to
test hypotheses presented in this work. Table 1 shows the time-series pooled
logit estimates for 2018-2022, while Table 2 is the cross-sectional version of same
models. Since H1 and H2 are related to governance-related issues, models 1-4 in
both regression tables shows the association between governance indicators and
15

-.6
-.4
-.2
0
.2
.4
Effects on Pr(Meta)
0 .1 .2 .3 .4 .5 .6 .7 .8 .9 1
UNGA Voting (w/USA)
Absence of Violence
-1.5
-1
-.5
0
.5
0 .1 .2 .3 .4 .5 .6 .7 .8 .9 1
UNGA Voting (w/USA)
V-Dem Polyarchy
-.4
-.2
0
.2
.4
Effects on Pr(Twitter)
0 .1 .2 .3 .4 .5 .6 .7 .8 .9 1
UNGA Voting (w/USA)
Absence of Violence
-1.5
-1
-.5
0
.5
1
0 .1 .2 .3 .4 .5 .6 .7 .8 .9 1
UNGA Voting (w/USA)
V-Dem Polyarchy
Figure 4: Conditional Effects of Polyarchy and Political Stability on Meta and
Twitter’s Country Focus
SMCs take-downs. We initially assessed whether Twitter and Meta’s take-down
operations focus more on authoritarian countries. The bi-variate regression
model in the first two columns indicates that both are concentrating on less
democratic countries. In simpler terms, the likelihood of SMCs directing their
actions towards countries rises as V-Dem scores decrease. Although Meta and
Twitter may focus on varying numbers of countries, they exhibit a similarity
in addressing accounts originating from less democratic nations. This effect is
more strong and significant for Twitter. Our analysis in Figure 2 also reflects
this finding.
Authoritarian countries vary in repressiveness and political instability. Some
democracies face higher political instability and violence. Political parties and
state bureaucracies in these democracies may use disinformation and online ma-
nipulation for propaganda, making them sensitive to state-linked information
operations. Models 3 and 4 in both tables reveal that Meta primarily focuses
on accounts originating from countries with higher levels of political instabil-
ity. Conversely, Twitter continues to direct its attention towards countries with
more authoritarian tendencies, even after including the political stability vari-
able, as seen in Model 4. After adding other independent variables, we observe
that good-governance indicators protect their effect on SMCs’ take-downs for
columns 5 and 6. On Column 5 and 6 of 2 and 1, we see a significant negative
association between Twitter and META’s take-downs and countries’ democracy
score at 95 percent confidence level.
In summary, the initial six models without interaction terms indicate that
governance indicators, particularly play a significant role in the SMCs’ country
16

focus vis a vis other variables. Based on this, H1 is corroborated for the first
six regression column of Table 2 and 1.
We also put a caution here. Our findings do not suggest that more authori-
tarian countries commit more state-linked information operations. We estimate
our regression models based on what Twitter and META reported. Such oper-
ations are not unique to authoritarian countries. For instance, we see META
also focuses on United States and France if they detect a state-linked network,
meaning that Western democracies also can be focused on by SMCs. If such
take-downs happen, it means that democratic countries are also subjects of
state-linked information campaigns. However, Meta and Twitter’s take-down
policies reflect divergences in investigating Western democracies. For instance,
Twitter never carried-out its take-down operations in relation with any West-
ern Democracies. This puts a question mark regarding the politics of take-down
operations. This brings us the idea behind H3 and H4. We also investigate if
there is an underlying geopolitical logic in these two SMCs’ information opera-
tions. Domestic state regime characteristics may be influenced by the presence
of realpolitik in international affairs.
Multinational companies are powerful actors regarding market information
and their competitiveness in domestic markets, which complicates their rela-
tionship with the sovereign states [87–89]. Since these companies might be af-
fected by international politics, we add UNGA Voting similarity with the United
States. Model 5 and 6 in both Table 2 and 1 manifest non-interaction models
with other independent variables including UNGA Voting (w/USA), Population
(log) and GDP Per Capita (log). These analysis yield no significant relationship
between SMCs’ take-downs and countries’ political similarity with the United
States. In other words, Twitter and Meta take actions for countries regardless
of their political like-mindedness with the US at the international level. This
finding is valid for our all models, which falsifies H3. These finding is important
because these take-down operations also carried out for many reasons including
international reasons such as election intervention, anti-American propaganda.
Indeed, we do not find a significant effect of political like-mindedness with the
United States on the two SMCs’ take-down operations.
Since disinformation landscapes are a complex amalgam of domestic and in-
ternational politics, we used an interaction variable based on good governance
indicators and UNGA Voting similarity with the United States. Models 7-10
reflects this idea focusing on if international political similarity moderates the
effect of good-governance indicators. In these models, we observe that political
similarity with the United States has a moderating effect on good governance in-
dicators, particularly in columns 8, 9 and 10 in both tables. In other words, the
effect of democracy and political stability changes with different levels of UNGA
Voting (w/USA). Since regression coefficients in logistic models are odd-plotting
marginal and conditional effects are useful tool to interpret interaction coeffi-
cients. We plotted conditional effect of good governance indicators’ as seen in
the Figure 4. All four figures show how the effect of good governance indicators
vary for different levels of UNGA Voting Similarity with the US. Subplots on
the top row show that the conditional effect of absence of violence and V-Dem
17

democracy scores on Meta’s take-downs changes for different levels of UNGA
Voting Similarity (w/USA). For Meta, we find that the effect of good gover-
nance indicators are more visible for higher values of political similarity with
the United States. This is valid for both political stability and democracy scores.
For Twitter, the interaction effect is more visible for V-Dem Democracy score
(lower right in Fig.4). But, the same is not valid for absence of violence. This
can also be seen in the different models of regression tables, and this conditional
effect is more pronounced for higher levels of UNGA Voting (w/USA).
It is interesting that although political similarity with the United States is
not significant based on main effects as seen in models 5-6, it has a interaction
effect on good-governance indicators. At this point, we suggest that our models
7-10 corroborates H4. However, we approach this finding with a caution. As
seen in Figure 4, we have also included a histogram of UNGA Voting (w/USA)
to determine if its distribution is skewed. Its distribution, evident in the four
figures, demonstrates a skew towards lower values. Given this, we need to pay
attention in interpreting its effects beyond the 0.6 mark, where the data points
are notably sparse. While corroborating our H4, we do not offer any causality
regarding this moderating effect.
In addition to good governance indicators and international alignments, we
tested whether countries’ economic power and population manifest an associa-
tion between Twitter and Meta’s reaction to information operations. As seen
in H5, we expected that there can be an economic logic for SMCs, prevent-
ing them carrying out their take-down operations. However, it is observed that
users originating in countries with larger populations are more likely to be taken
down by SMCs, a trend consistent across all regression models for both tables.
This important because larger populations imply larger user statistics and rev-
enue extraction (SI:Table-6 and Figure-2). Also, we propose that a higher GDP
Per Capita represents an additional potential for revenue extraction by users.
Contrary to expectations, our analysis did not confirm that SMCs are less in-
clined to take down accounts originating in countries with higher GDP per
capita. As a result, we found no economic rationale underlying the take-down
policies of SMCs. Interestingly, we discovered evidence that Meta conducts
counter-operations even against the United States, which is the country where
it generates the highest revenue [90]. This is the opposite of what we expected.
It illustrates that while scrutinizing state-linked accounts originating in coun-
tries, Meta and Twitter is carrying out their operations against state-linked
coordinated activities regardless of countries’ economic power.
These findings can explain how Meta and Twitter are similar or different
in terms of their response to state-linked information operations in different
countries. While they are more hesitant to different good-governance indica-
tors, political similarity with the US has a moderating effect for both SMCs.
We demonstrated that both Twitter and Meta are responsive to countries’ good
governance indicators such as democracy and political stability, based on pooled
logit and cross-sectional estimations. However, we also underline the importance
of political similarity with great powers at the international level. Therefore,
a demarcation line between authoritarian and democratic countries -regarding
18

SMCs’ response to state-linked information operations- can be misleading. This
is the point that we observe the possible conditional effect of international align-
ments on SMCs’ action against different states.
There is a trend towards authoritarianism globally. However, these author-
itarian inclinations occur in a multi-polar international landscape. Disinfor-
mation and concerted perilous networks can nurture in places when they are
protected by a powerful state apparatus such as military or security entities.
These networks operate in an international landscape, where geopolitical shifts
take place including inter-state and civil-wars. While multinational corpora-
tions seek more revenue globally, they also suffer acute or long-term geopolitical
crises. Countries such as China, Iran, North Korea and Russia ban access to
the two SMCs. The countries are also politically distant from the United States
and other western countries. Thus, we can see how autocratic tendencies meddle
with international alignments. Our study suggests two possible interpretations
regarding the prevalence of state-linked information operations. First, it is con-
ceivable that authoritarian regimes provide a permissive environment for the
proliferation of state-linked information operations, which would explain the
higher frequency of account take-downs by SMCs. Secondly, it is plausible to
consider that SMCs utilize a selective mechanism in their regulatory actions,
focusing not only on the oppressive nature of these operations but also on their
involvement in international affairs, including interference in foreign elections
and domestic politics. Several networks have been targeted for this purpose,
including those linked to China, Iran, and Russia. For instance, Meta, through
116 separate announcements on state-linked operations, identified 38 of them as
foreign interference. Within this 38 foreign operations, Meta reports that United
States was targeted by seven times by other country-linked perilous networks
such as Russia, Iran and China. However, Egypt and the UAE-linked networks
target multiple countries including Iran(7), Turkey(5) and Qatar(5) 1. Based
on Twitter’s 48 released datasets (separate announcements), United States has
been the top country targeted by these state-linked information operations (SI:
Table 8). Qatar, Hong Kong and Turkey are other countries as being targeted by
state-linked perilous networks. That is, when it comes to target of taken-down
networks, we see variations across different SMC platforms. According to Twit-
ter reports and our statistical anaylsis, it pays more attention to domestic-based
actions.
This underscores the complex and dynamic nature of digital geopolitical
landscape, where state-linked information operations are not confined to a single
strategy or target. It highlights the need for ongoing outlook and adaptive
strategies by SMCs to counter these evolving threats and protect the integrity
of global information landscapes. It is important to note, however, we do not
provide any anecdotal or qualitative evidence. Indeed, our findings regarding
conditional effects show how regime characteristics and international political
similarity interact with each other statistically.
All findings above would be challenged or corroborated with with more data
1Number of separate operations in parenthesis
19

coming from SMCs. Each social media or information technology company has
different levels of transparency[91]. Twitter offers user-level metadata, which
allows researchers to analyze take-down operations in a comprehensive man-
ner. User characteristics and tweets inform us about their possible network,
replies, quote tweets and many other user-level traits. However, Meta or Face-
book does not provide open access to this type of information. If an in-depth
individual-level data were available for both platforms, a deeper understand-
ing of the underlying premises guiding their take-down operations would be
possible. In-country and between-country comparisons would be possible and
helpful to understand how they detect these networks. Researchers can extend
their research on SMCs’ take-down policies, which would be an integral part of
transparency in the cyberspace and disinformation landscape.
Conclusion
SMCs operate in a challenging global environment. This includes dealing with
authoritarian regimes in a world with many powerful nations. The shift away
from democracy is and important factor for the spread of misinformation. So-
cial media emerges a key and contested arena for countries to implement their
(dis)information strategies. These efforts often aim to bolster their domestic
and international agendas. Governments can use this to build support locally
or to distort the truth about events to gain international backing, since social
media is a common platform for interaction among individuals, political parties,
and politicians. Based on Meta and Twitter’s reports, this is evident in actions
by countries like Russia, Iran, and China and many other countries, where they
have a capability to influence foreign elections, create fake news, engage in mis-
leading public diplomacy, and spread misinformation. Therefore, it is crucial for
SMCs to develop a coherent approach against these state-linked activities and
to fight misinformation through social media. When SMCs address these issues,
they act in a political environment because the subjects of their take-down op-
erations are state-linked. This is the main difference between these operations
and classical content moderation.
This study provides significant insights into the behavior of SMCs, specifi-
cally for Meta and Twitter. We have found that domestic governance indicators
are important for both SMCs. Our findings indicate that SMCs tend to focus on
countries with lower democracy scores and higher levels of political instability.
This suggests that governance indicators play a crucial role in shaping SMCs’
focus, which aligns with the hypothesis that less democratic nations are more
likely to experience such operations.
However, we also questioned if good governance indicators’ impact is affected
by international political tendencies. In other words, we ask if the impact of
good governance indicators is moderated by UNGA Voting Similarity with the
U.S. Despite the lack of direct evidence between SMCs’ actions and interna-
tional political like-mindedness, it is interesting to note that we find a modest
evidence that the effect of good governance indicators change with different lev-
20

els of like-mindedness with the United States and China. Considering both in-
ternal governance structures and international relations when analyzing SMCs’
operational strategies highlights the multifaceted nature of their responses to
global information manipulation. The politics of Twitter and Meta’s operations
matter in such a geopolitical landscape. We can conclude that authoritarian
challenges occur in a geopolitical landscape which is a reflection of differentiat-
ing geographical orientations in world politics.
Two problems are identified throughout our analysis. First, there is no har-
monized approach across the two social media platforms. Second, the scope
and vision of both SMCs differ significantly when it comes to geographical vari-
ations in their take-down operations. While we observe parallel trends in terms
of their interest in regime characteristics, defining state-linked networks, detect-
ing those networks, and establishing the main premises of their operations to
take down these networks require a more coherent approach. As a part of such
policy-relevant outlooks, transparency concerns are also important. Meta, for
example, does not provide user-level meta data, making further analysis diffi-
cult. More data will enable the use of more fruitful analyses, such as comparisons
within and between countries.
However, we also note that a possible problem for external validity arises
with the existence of other US or China-based social media platforms. YouTube,
TikTok and many other social media environments have a content moderation
policy. Assuming they made their state-linked operations public, we would know
more about the political nature of SMCs’ take-down operations. This would be
more interesting with TikTok, which has been under pressure by US authorities
as a Chinese social media corporation. This could cause a potential bias in terms
of how we evaluate the effectiveness of SMCs’ take-down operations. We need to
consider the possibility that these platforms have different policies, which could
impact our findings. This could lead to different conclusions about the political
nature of SMCs’ take-down operations. Therefore, further studies can change
our findings or generate more robustness. However, a level of transparency is
needed to deal with the problem of SMCs’ reaction to state-linked information
operations.
References
[1] Selman Selim Aky¨ uz. The impact of misinformation and preferences of
news sources on institutional trust perception in the covid-19 process. In
Impact of Infodemic on Organizational Performance , pages 291–310. IGI
Global, 2021.
[2] Samantha Bradshaw and Philip N Howard. The global organization of
social media disinformation campaigns. Journal of International Affairs ,
71(1.5):23–32, 2018.
[3] Prateek Dewan, Shrey Bagroy, and Ponnurangam Kumaraguru. Hiding in
plain sight: The anatomy of malicious pages on facebook. Social Network
21

Based Big Data Analysis and Applications , pages 21–54, 2018.
[4] C ¸ i˘ gdem Bozda˘ g. Bottom-up nationalism and discrimination on social me-
dia: An analysis of the citizenship debate about refugees in turkey. Euro-
pean Journal of Cultural Studies , 23(5):712–730, 2020.
[5] Elif Yolbulan Okan, Ayper Topcu, and Serhat Aky¨ uz. The role of social
media in political marketing: 2014 local elections of turkey. European
Journal of business and Management , 6(22):131–140, 2014.
[6] Elif Yolbulan Okan, Ayper Topcu, and Serhat Aky¨ uz. The role of social
media in political marketing: 2014 local elections of turkey. European
Journal of business and Management , 6(22):131–140, 2014.
[7] Se¸ cil Toros and Emre Toros. Social media use and political participation:
the turkish case. Turkish Studies, 23(3):450–473, 2022.
[8] Panagiotis T Metaxas and Eni Mustafaraj. Social media and the elections.
Science, 338(6106):472–473, 2012.
[9] Ashok Deb, Luca Luceri, Adam Badaway, and Emilio Ferrara. Perils and
challenges of social media and election manipulation analysis: The 2018 us
midterms. In Companion proceedings of the 2019 world wide web confer-
ence, pages 237–247, 2019.
[10] Britney Harris. Diplomacy 2.0: the future of social media in nation brand-
ing. Exchange: The Journal of Public Diplomacy , 4(1):3, 2013.
[11] Bilge Yesil. Social media manipulation in turkey: Actors, tactics, targets.
In The Routledge Companion to Media Disinformation and Populism, pages
386–396. Routledge, 2021.
[12] Sarah T Roberts. Digital detritus:’error’and the logic of opacity in social
media content moderation. First Monday , 2018.
[13] Sarah T Roberts. Commercial content moderation: Digital laborers’ dirty
work. 2016.
[14] S. Frenkel and T. Hsu. Facebook, twitter and others remove pro-u.s. influ-
ence campaign. The New York Times , August 2022.
[15] Onur Varol. Should we agree to disagree about twitter’s bot problem?
Online Social Networks and Media , 37:100263, 2023.
[16] Deana A Rohlinger, Kyle Rose, Sarah Warren, and Stuart Shulman. Does
the musk twitter takeover matter? political influencers, their arguments,
and the quality of information they share. Socius, 9:23780231231152193,
2023.
[17] Todd Helmus. Social media and influence operations technologies: Implica-
22

tions for great power competition. Strategic Assessment 2020: Into a New
Era of Great Power Competition , pages 153–166, 2020.
[18] ´Angel D ´ ıaz and Laura Hecht-Felella. Double standards in social media
content moderation. Brennan Center for Justice at New York Univer-
sity School of Law. https://www. brennancenter. org/our-work/research-
reports/double-standards-socialmedia-content-moderation, 2021.
[19] Dominik B¨ ar, Nicolas Pr¨ ollochs, and Stefan Feuerriegel. New threats
to society from free-speech social media platforms. arXiv preprint
arXiv:2302.01229, 2023.
[20] Kyle Langvardt. Regulating online content moderation. Geo. LJ, 106:1353,
2017.
[21] Onur Varol. Spatiotemporal analysis of censored content on twitter. In
Proceedings of the 8th ACM Conference on Web Science , pages 372–373,
2016.
[22] Edward L Bernays. Manipulating public opinion: The why and the how.
American journal of sociology , 33(6):958–971, 1928.
[23] Garth S Jowett and Victoria O’donnell. Propaganda & persuasion . Sage
publications, 2018.
[24] Daniel Arnaudo, Samantha Bradshaw, Hui Hui Ooi, Kaleigh Schwalbe,
V Zakem, and A Zink. Combating information manipulation: A playbook
for elections and beyond. The International Republican Institute & The
National Democratic Institute & The Stanford Internet Observatory , 2021.
[25] Facebook. Removing bad actors on facebook, Jul 2018.
[26] Jennifer Jerit and Yangzi Zhao. Political misinformation. Annual Review
of Political Science , 23:77–94, 2020.
[27] James H Kuklinski, Paul J Quirk, Jennifer Jerit, David Schwieder, and
Robert F Rich. Misinformation and the currency of democratic citizenship.
The Journal of Politics , 62(3):790–816, 2000.
[28] Samantha Bradshaw and Philip N Howard. The global organization of
social media disinformation campaigns. Journal of International Affairs ,
71(1.5):23–32, 2018.
[29] Samantha Bradshaw and Philip N Howard. The global organization of
social media disinformation campaigns. Journal of International Affairs ,
71(1.5):23–32, 2018.
[30] Samuel C Woolley and Philip N Howard. Political communication, compu-
tational propaganda, and autonomous agents: Introduction. International
journal of Communication , 10, 2016.
23

[31] Kai Shu, Suhang Wang, Dongwon Lee, and Huan Liu. Disinformation,
misinformation, and fake news in social media . Springer, 2020.
[32] Erkan Saka. Siyasi troll¨ uk ¨ orne˘ gi olarak aktroller.Birikim,(322), pages
17–21, 2016.
[33] Turgay Yerlikaya and Seca Toker Aslan. Social media and fake news in the
post-truth era. Insight Turkey, 22(2):177–196, 2020.
[34] Seong Jae Min. Who believes in conspiracy theories? network diversity,
political discussion, and conservative conspiracy theories on social media.
American Politics Research, 49(5):415–427, 2021.
[35] Erkan Saka. Social media in turkey as a space for political battles: Aktrolls
and other politically motivated trolling. Middle East Critique , 27(2):161–
177, 2018.
[36] Kai Shu, Suhang Wang, Dongwon Lee, and Huan Liu. Disinformation,
misinformation, and fake news in social media . Springer, 2020.
[37] Yannis Theocharis, Ana Cardenal, Soyeon Jin, Toril Aalberg, David Nicolas
Hopmann, Jesper Str¨ omb¨ ack, Laia Castro, Frank Esser, Peter Van Aelst,
Claes de Vreese, et al. Does the platform matter? social media and covid-
19 conspiracy theory beliefs in 17 countries. new media & society , page
14614448211045666, 2021.
[38] Matthew Atkinson, Darin DeWitt, Joseph E Uscinski, JC Lucas,
CJ Galdieri, and TS Sisco. Conspiracy theories in the 2016 election. Con-
ventional Wisdom, Parties, and Broken Barriers in the 2016 Election , 163,
2017.
[39] Nir Grinberg, Kenneth Joseph, Lisa Friedland, Briony Swire-Thompson,
and David Lazer. Fake news on twitter during the 2016 us presidential
election. Science, 363(6425):374–378, 2019.
[40] Ergin Bulut and Erdem Y¨ or¨ uk. Mediatized populisms— digital populism:
Trolls and political polarization of twitter in turkey. International Journal
of Communication, 11:25, 2017.
[41] Samantha Bradshaw and Philip Howard. Troops, trolls and troublemakers:
A global inventory of organized social media manipulation. Computational
Propaganda Research Project, 2017.
[42] Onur Varol and Ismail Uluturk. Deception strategies and threats for online
discussions. First Monday , 2018.
[43] Chengcheng Shao, Giovanni Luca Ciampaglia, Onur Varol, Kai-Cheng
Yang, Alessandro Flammini, and Filippo Menczer. The spread of low-
credibility content by social bots. Nature communications, 9(1):1–9, 2018.
24

[44] Emilio Ferrara, Onur Varol, Clayton Davis, Filippo Menczer, and Alessan-
dro Flammini. The rise of social bots. Communications of the ACM ,
59(7):96–104, 2016.
[45] Onur Varol, Emilio Ferrara, Clayton Davis, Filippo Menczer, and Alessan-
dro Flammini. Online human-bot interactions: Detection, estimation, and
characterization. In Proceedings of the international AAAI conference on
web and social media , volume 11, pages 280–289, 2017.
[46] Onur Varol and Ismail Uluturk. Journalists on twitter: self-branding, au-
diences, and involvement of bots. Journal of Computational Social Science,
3(1):83–101, 2020.
[47] Onur Varol, Emilio Ferrara, Christine L Ogan, Filippo Menczer, and
Alessandro Flammini. Evolution of online user behavior during a social
upheaval. In Proceedings of the 2014 ACM conference on Web science ,
pages 81–90, 2014.
[48] Gordon Pennycook and David G Rand. Examining false beliefs about voter
fraud in the wake of the 2020 presidential election. The Harvard Kennedy
School Misinformation Review , 2021.
[49] Max Bader. Disinformation in elections. Security and Human Rights, 29(1-
4):24–35, 2018.
[50] Ashok Deb, Luca Luceri, Adam Badaway, and Emilio Ferrara. Perils and
challenges of social media and election manipulation analysis: The 2018 us
midterms. In Companion proceedings of the 2019 world wide web confer-
ence, pages 237–247, 2019.
[51] Ayla Albayrak and Joe Parkinson. Turkey’s government forms 6,000-
member social media team. The Wall Street Journal , 16, 2013.
[52] E. K. Sozeri. Mapping turkey’s twitter trolls, October 2015.
[53] Duygu Karatas and Erkan Saka. Online political trolling in the context of
post-gezi social media in turkey.International Journal of Digital Television,
8(3):383–401, 2017.
[54] Xinyu Wang, Jiayi Li, Eesha Srivatsavaya, and Sarah Rajtmajer. Evidence
of inter-state coordination amongst state-backed information operations.
Scientific reports, 13(1):7716, 2023.
[55] Maria Repnikova and Keyu Alexander Chen. Asymmetrical discursive com-
petition: China–united states digital diplomacy in africa. International
Communication Gazette, 85(1):15–31, 2023.
[56] Samantha Bradshaw and Philip N Howard. Challenging truth and trust: A
global inventory of organized social media manipulation.The computational
propaganda project, 1:1–26, 2018.
25

[57] Maya Merhi, Sarah Rajtmajer, and Dongwon Lee. Information operations
in turkey: Manufacturing resilience with free twitter accounts. In Pro-
ceedings of the International AAAI Conference on Web and Social Media ,
volume 17, pages 638–649, 2023.
[58] Elif Yolbulan Okan, Ayper Topcu, and Serhat Aky¨ uz. The role of social
media in political marketing: 2014 local elections of turkey. European
Journal of business and Management , 6(22):131–140, 2014.
[59] Se¸ cil Toros and Emre Toros. Social media use and political participation:
the turkish case. Turkish Studies, 23(3):450–473, 2022.
[60] Jessica Brandt. How autocrats manipulate online information: Putin’s and
xi’s playbooks. The Washington Quarterly , 44(3):127–154, 2021.
[61] Jessica Brandt. How democracies can win an information contest without
undercutting their values. Carnegie Endowment, August , 2, 2021.
[62] T. Peel. The coalition’s twitter fraud and deception. Independent Australia,
June 2013.
[63] Robert A Dahl. What political institutions does large-scale democracy
require? Political Science Quarterly , 120(2):187–197, 2005.
[64] Jan-Frederik Kremer and Benedikt M¨ uller. Cyberspace and international
relations: Theory, prospects and challenges . Springer, 2013.
[65] A. Segal. A new u.s. foreign policy for cyberspace, July 2022.
[66] J. Chipman. Why your company needs a foreign policy: Multinationals
must address growing geopolitical volatility. Harvard Business Review ,
September 2016.
[67] Alex Hern and Luke Harding. Russian-led troll network based in west africa
uncovered. The Guardian, Mar 2020.
[68] Facebook. Removing myanmar military officials from facebook, Aug 2018.
[69] Meta. Taking down more coordinated inauthentic behavior, Aug 2018.
[70] Meta. October 2020 coordinated inauthentic behavior report, Nov 2020.
[71] Meta. March 2021 coordinated inauthentic behavior report, Apr 2021.
[72] Berk Esen and Sebnem Gumuscu. Rising competitive authoritarianism in
turkey. Third World Quarterly , 37(9):1581–1606, 2016.
[73] Daniel Kaufmann and Aart Kraay. Worldwide governance indicators, 2023
update. http://www.govindicators.org, 2023. Accessed on 19 October
2023.
26

[74] Freedom House. Freedom in the world. https://freedomhouse.org/
report/freedom-world#Data, 2023. Accessed: [date of access].
[75] Michael Coppedge, John Gerring, Carl Henrik Knutsen, Staffan I. Lind-
berg, Jan Teorell, Lisa Gastaldi, Sandra Grahn, Natalia Natsika, Jose-
fine Pernes, Oskar Ryd´ en, and Johannes von R¨ omer. V-Dem [Country-
Year/Country-Date] Dataset v13. Varieties of Democracy (V-Dem)
Project, 2023.
[76] L Jeremy Clegg, Hinrich Voss, and Janja A Tardios. The autocratic advan-
tage: Internationalization of state-owned multinationals. Journal of World
Business, 53(5):668–681, 2018.
[77] Nathan M Jensen. Democratic governance and multinational corporations:
Political regimes and inflows of foreign direct investment. International
organization, 57(3):587–616, 2003.
[78] Susan Morgan. Fake news, disinformation, manipulation and online tactics
to undermine democracy. Journal of Cyber Policy , 3(1):39–43, 2018.
[79] Erik Voeten, Anton Strezhnev, and Michael Bailey. United Nations General
Assembly Voting Data, 2009.
[80] Matthias Busse and Carsten Hefeker. Political risk, institutions and foreign
direct investment. European journal of political economy , 23(2):397–415,
2007.
[81] Niels G Noorderhaven and Anne-Wil Harzing. The “country-of-origin ef-
fect” in multinational corporations: Sources, mechanisms and moderating
conditions. In Management and International Review: Can Multinationals
Bridge the Gap Between Global and Local? , pages 47–66. Springer, 2003.
[82] Bruce Kogut and Harbir Singh. The effect of national culture on the choice
of entry mode. Journal of international business studies , 19:411–432, 1988.
[83] Joakim Kreutz. Human rights, geostrategy, and eu foreign policy, 1989–
2008. International organization, 69(1):195–217, 2015.
[84] The White House. National security strategy, October 2022.
[85] Facebook users, stats, data & trends. https://datareportal.com/
essential-facebook-stats, 2023. Accessed: [date of access].
[86] Erik Voeten, Anton Strezhnev, and Michael Bailey. United Nations General
Assembly Voting Data. 2009.
[87] Joseph S Nye. Multinational corporations in world politics. Foreign Affairs,
53(1):153–175, 1974.
[88] Hongfei Gu. Data, big tech, and the new concept of sovereignty. Journal
of Chinese Political Science , pages 1–22, 2023.
27

[89] Maxwell Lowe. Social media is blurring the lines of national sovereignty, 4
2021.
[90] Meta. Meta’s adversarial threat report, third quarter 2022, Nov 2022.
[91] Aleksandra Urman and Mykola Makhortykh. How transparent are trans-
parency reports? comparative analysis of transparency reporting across
online platforms. Telecommunications Policy, 47(3):102477, 2023.
28

A Supplamentary Information
Compiling Data for Meta and Twitter’s Take Down Oper-
ations
We compiled our data from Twitter and Meta’s announcements. In each news,
they announced country of origin, targeted countries, modality of operation and
many other information such as domestic and foreign elements. We curated a
dataset for reports between 2018 and 2022. During this time, they targeted
different countries for state-linked operations. Table SI-1 shows all countries
that Meta and Twitter focused on regarding different information operations.
For instance, Russia originated operations identified by Meta and Twitter for
21 and 9 times, respectively for state-linked operations.
Meta carry out its take-down operations against accounts originating in 48
distinct countries. We only coded state-linked operations if Meta clearly empha-
sized any linkage with governments, military, political parties and municipalities.
This provided more insight to compare Meta with Twitter’s take-down opera-
tions, since Twitter -from the beginning- announced state-linked operations.
In the case of Twitter, Russia can set up networks in other countries such as
Ghana and Nigeria. In such cases, we did not coded Ghana and Nigeria as being
targeted by Twitter’s counter operations. 2 We should also note that Twitter
make user-level data public, while Meta does not provide such data. This is
a significant difference between these SMCs. User level data is significant to
understand the inherent mechanism of disinformation networks.
Regarding regression sample, we excluded some countries because of lack
of data. For instance, we cannot retrieve GDP Per Capita data for Eritrea,
South Sudan and Venezuela. Therefore, software automatically omits row with
missing variables.
Table SI-1 shows which countries are focused by Meta and Twitter. We
observe that Meta was more active than Twitter in taking action against state-
linked operations. There are 48 unique countries for Meta and this number is
22 for Twitter.
2https://www.theguardian.com/technology/2020/mar/13/facebook-uncovers-russian-led-troll-network-based-in-west-africa
29

Table SI-1: Country Summary of Meta and Twitter’s Geographic Response
(2018-2021)
Country List
Country Number of Meta-Target Number of Twitter-Target
Russia 21 9
Iran 12 7
Mexico 8 1
Myanmar 8 -
Brazil 4 -
China 4 6
Georgia 4 -
Kyrgyzstan 3 -
Pakistan 3 -
WB/Gaza 2 -
El Salvador 2 -
Peru 2 -
Spain 2 2
Azerbaijan 2 -
Morocco 2 -
Ukraine 2 -
Nigeria 1 1
Nicaragua 1 -
Romania 1 -
Philippines 1 -
Saudi Arabia 1 4
Serbia (Yugoslavia) 1 1
Sudan 1 -
Thailand 1 1
Uganda 1 1
United States 1 -
Moldova 1 -
Algeria 1 -
Malaysia 1 -
KRG 1 -
Azerbeijan 1 -
Bangladesh 1 1
Belarus 1 -
Benin 1 -
Bolivia 1 -
Comoros 1 -
Costa Rica 1 -
Cuba 1 1
DRC 1 -
Ecuador 1 1
Egypt 1 2
Ethiopia 1 -
France 1 -
Ghana - 1
Honduras 1 1
India 1 -
Indonesia 1 1
Israel 1 -
Jordan 1 -
Kazakhstan 1 -
Armenia - 1
Tanzania - 1
Turkey - 1
United Arab Emirates - 1
Venezuela - 4
30

Robustness analysis for regression models
Table SI-2: Regression Results (Linear Probability Modes-Pooled Time Series)
(1) (2) (3) (4) (5) (6) (7) (8) (9) (10)
Meta Twitter Meta Twitter Meta Twitter Meta Twitter Meta Twitter
b/se b/se b/se b/se b/se b/se b/se b/se b/se b/se
V-Dem Polyarchy -0.402*** -0.322*** -0.228 -0.359** -0.327* -0.359** -0.025 0.145 -0.237 -0.327**
(0.13) (0.10) (0.17) (0.14) (0.17) (0.14) (0.39) (0.27) (0.17) (0.14)
PVE -0.080* 0.017 -0.035 0.035 -0.035 0.033 0.206*** 0.120**
(0.04) (0.03) (0.05) (0.04) (0.05) (0.04) (0.07) (0.05)
UNGA Voting (w/USA) 0.050 -0.245* 0.760 0.942 0.037 -0.249
(0.28) (0.15) (0.87) (0.62) (0.23) (0.15)
GDP Per Capita (log) 0.038 0.049** 0.047 0.063*** 0.057** 0.056**
(0.03) (0.02) (0.03) (0.02) (0.03) (0.02)
Population (log) 0.092*** 0.063*** 0.095*** 0.068*** 0.096*** 0.064***
(0.02) (0.02) (0.02) (0.02) (0.02) (0.02)
V-Dem Polyarchy × UNGA Voting (w/USA) -1.064 -1.778**
(1.20) (0.86)
PVE × UNGA Voting (w/USA) -0.873*** -0.312**
(0.18) (0.14)
Constant 0.474*** 0.283*** 0.367*** 0.306*** -1.399*** -1.048*** -1.705*** -1.559*** -1.628*** -1.130***
(0.08) (0.07) (0.10) (0.09) (0.36) (0.28) (0.53) (0.39) (0.36) (0.28)
Number of clusters 168 168 168 168 168 168 168 168 168 168
Number of observations 672 672 672 672 672 672 672 672 672 672
R-squared 0.053 0.065 0.072 0.067 0.197 0.190 0.201 0.212 0.253 0.204
Table SI-3: Regression Results (Linear Probability Modes-Corssection)
(1) (2) (3) (4) (5) (6) (7) (8) (9) (10)
Meta Twitter Meta Twitter Meta Twitter Meta Twitter Meta Twitter
V-Dem Polyarchy -0.372*** -0.303*** -0.179 -0.290* -0.322* -0.288* 0.080 0.347 -0.226 -0.249
(0.13) (0.10) (0.17) (0.15) (0.18) (0.16) (0.44) (0.32) (0.18) (0.16)
PVE -0.086* -0.006 -0.039 0.028 -0.040 0.027 0.215*** 0.133**
(0.04) (0.03) (0.06) (0.04) (0.06) (0.04) (0.07) (0.06)
UNGA Voting (w/USA) -0.023 -0.292 0.909 1.185* -0.030 -0.294
(0.34) (0.18) (1.01) (0.71) (0.26) (0.19)
GDP Per Capita (log) 0.037 0.048* 0.048 0.065** 0.056* 0.056**
(0.03) (0.02) (0.03) (0.03) (0.03) (0.02)
Population (log) 0.091*** 0.074*** 0.095*** 0.079*** 0.097*** 0.076***
(0.02) (0.02) (0.02) (0.02) (0.02) (0.02)
V-Dem Polyarchy × UNGA Voting (w/USA) -1.411 -2.235**
(1.38) (0.99)
PVE × UNGA Voting (w/USA) -0.923*** -0.378**
(0.21) (0.17)
Constant 0.454*** 0.285*** 0.337*** 0.277*** -1.365*** -1.221*** -1.761*** -1.847*** -1.614*** -1.323***
(0.08) (0.07) (0.10) (0.09) (0.37) (0.30) (0.58) (0.43) (0.38) (0.31)
Number of clusters
Number of observations 173 173 172 172 166 166 166 166 166 166
Table SI-4: Regression Results (Logit Estimates, Cross-section, with UNGA
Voting with China)
(1) (2) (3) (4) (5) (6) (7) (8) (9) (10)
Meta Twitter Meta Twitter Meta Twitter Meta Twitter Meta Twitter
b/se b/se b/se b/se b/se b/se b/se b/se b/se b/se
main
V-Dem Polyarchy -2.271*** -3.601*** -1.368 -3.691*** -2.518** -3.561** -7.294 -28.594** -1.764 -2.921*
(0.73) (1.21) (0.92) (1.35) (1.15) (1.76) (8.62) (12.95) (1.14) (1.76)
PVE -0.460** 0.059 -0.184 0.176 -0.181 0.291 -7.722** -5.271***
(0.22) (0.22) (0.29) (0.41) (0.30) (0.43) (3.11) (2.02)
UNGA Voting Similarity with China -1.540 4.027 -5.386 -15.116 -0.350 5.208
(2.50) (3.31) (7.48) (9.29) (2.57) (3.29)
GDP Per Capita (log) 0.185 0.613** 0.217 0.694** 0.285 0.649**
(0.18) (0.31) (0.20) (0.30) (0.19) (0.31)
Population (log) 0.671*** 0.824*** 0.689*** 0.910*** 0.746*** 0.859***
(0.16) (0.28) (0.16) (0.27) (0.17) (0.29)
V-Dem Polyarchy × UNGA Voting Similarity with China 5.735 29.964**
(10.26) (15.15)
PVE × UNGA Voting Similarity with China 9.043** 6.516***
(3.58) (2.40)
Constant 0.122 -0.455 -0.473 -0.392 -11.320*** -22.808*** -8.626 -8.642 -14.481*** -24.842***
(0.39) (0.51) (0.50) (0.61) (4.25) (6.76) (6.09) (8.50) (4.42) (6.54)
Number of clusters
Number of observations 168 168 168 168 168 168 168 168 168 168
31

-2
-1.5
-1
-.5
0
.5
Effects on Pr(META Target)
0 .1 .2 .3 .4 .5 .6 .7 .8 .9 1
UNGA Voting Similarity with China
V-Dem Polyarchy
-.6
-.4
-.2
0
.2
.4
0 .1 .2 .3 .4 .5 .6 .7 .8 .9 1
UNGA Voting Similarity with China
PVE
-1.5
-1
-.5
0
.5
1
Effects on Pr(Twitter Target)
0 .1 .2 .3 .4 .5 .6 .7 .8 .9 1
UNGA Voting Similarity with China
V-Dem Polyarchy
-.4
-.2
0
.2
.4
0 .1 .2 .3 .4 .5 .6 .7 .8 .9 1
UNGA Voting Similarity with China
PVE
Figure SI-1: Conditional Effects of Polyarchy and Political Stability on Meta
and Twitter’s Country Targeting
Table SI-5: Regression Results (Logit Estimates, Cross-section, with User
Statistics)
(1) (2) (3) (4) (5) (6) (7) (8) (9) (10)
Meta Twitter Meta Twitter Meta Twitter Meta Twitter Meta Twitter
b/se b/se b/se b/se b/se b/se b/se b/se b/se b/se
main
V-Dem Polyarchy -2.271*** -3.601*** -1.368 -3.691*** -1.943* -2.916* -2.883 4.142 -1.402 -2.277
(0.73) (1.21) (0.92) (1.35) (1.07) (1.58) (2.39) (4.09) (1.06) (1.56)
PVE -0.460** 0.059 -0.824** -0.503 -0.821** -0.519* 0.768 0.472
(0.22) (0.22) (0.36) (0.31) (0.36) (0.30) (0.72) (0.55)
UNGA Voting (w/USA) 2.547 -0.230 0.445 14.071* 2.256 -1.802
(1.63) (2.13) (4.88) (7.67) (1.90) (2.46)
GDP Per Capita (log) -0.101 0.457 -0.135 0.606* 0.043 0.495
(0.27) (0.30) (0.29) (0.33) (0.28) (0.31)
Facebook Users (%Population) 2.953** 3.077** 2.305
(1.46) (1.52) (1.45)
Twitter Users (% Population) 0.171 -0.194 0.181
(1.49) (1.51) (1.47)
V-Dem Polyarchy × UNGA Voting (w/USA) 3.218 -24.207*
(7.15) (14.48)
PVE × UNGA Voting (w/USA) -5.927** -3.586*
(2.64) (1.93)
Constant 0.122 -0.455 -0.473 -0.392 -1.440 -4.843* -0.636 -9.943** -2.411 -4.894*
(0.39) (0.51) (0.50) (0.61) (1.96) (2.49) (2.72) (3.87) (2.13) (2.54)
Number of observations 168 168 168 168 162 160 162 160 162 160
32

10
15
20
Population (log)
5 10 15 20
Facebook Users (2023, log)
10
15
20
5 10 15 20
Twitter (X) Users (2023, log)
Figure SI-2: User Statistics and Population. On the left, we plotted the cor-
relation between user statistics and population. We captured a strong positive
correlation between user statistics and population.
Table SI-6: Correlation Table
Population Facebook Users’23 Twitter Users’23
Population 1.0000
Facebook Users 2023 0.9126 1.0000
Twitter Users 2023 0.4589 0.6350 1.0000
Table 6 statistically shows the association between user statistics and popula-
tion. For Facebook, the correlation is .91, which is stronger than the association
between Twitter’s. Indeed, statistics with user statistics do not change our es-
timations as seen in Table 5. Since China, Iran and Russia do not have official
user statistics for Facebook and Twitter, we replaced user statistics with pop-
ulation for a more comprehensive sampling. Our models with population and
user statistics manifest similar results, as expected.
Table SI-7: Variance inflation factors
Meta Twitter
PVE 2.707492 2.707492
V-Dem Polyarchy 2.041271 2.041271
GDP Per Capita (log) 2.405718 2.405718
UNGA Voting (w/USA) 2.07146 2.07146
Population(log) 1.329778 1.329778
N 166 166
33

T arget of State-Linked Info-Ops
(Meta)
T arget of State-Linked Info-Ops
(Twitter)
United States(7), Qatar(7), Iran(6),
United Kingdom(5), Yemen(5),
Turkey(5), Morocco(4), Su-
dan(4), Lebanon(4), Egypt(3),
Libya(3), Saudi Arabia(3), Syria(3),
Tunisia(3), Ukraine(3), Jordan(3),
Kazakhstan(2), Bahrain(2), Ger-
many(2), India(2), Indonesia(2),
Israel(2), Spain(2), Hong Kong(2),
Comoros(2), Romania(1), Latvia(1),
Estonia(1), Lithuania(1), Ar-
menia(1), Azerbaijan(1), Geor-
gia(1), Tajikistan(1), Uzbekistan(1),
Moldova(1), Russia(1), Kyrgyzs-
tan(1), Afghanistan(1), Albania(1),
Algeria(1), France(1), Iraq(1), Mex-
ico(1), Pakistan(1), Serbia(1), South
Africa(1), Italy(1), Austria(1),
Nigeria(1), Senegal(1), Togo(1),
Angola(1), China(1), UAE(1), West
Bank and Gaza(1), Somalia(1)
USA (5), Qatar (5), Hong Kong (4),
Turkey (2), Uyghurs (2), Iran (1),
Catalonia (1), Israel (1), Yemen (1),
Spain (1), West Papua (1), Azerbai-
jan (1), NATO (1), EU (1), Central
African Republic (1)
Table SI-8: Targets of State-Linked Information Networks Taken Down by Meta
and Twitter
We have identified that out of 196 operations where Meta took action to
suspend or take down accounts, 116 were associated with state-linked activities.
Within these 116 operations, 38 featured as involving inter-state state-linked in-
formation operations (the remaining networks deal with domestic propaganda).
Similarly, for Twitter, all 47 datasets (as reported in separate announcements)
are connected to state-linked activities. The targets of these state-linked oper-
ations encompass regional, domestic, and inter-state entities. Twitter explicitly
lists the names of countries targeted in the second column of Table 8. This
table provides a comprehensive overview of the countries, as well as regions,
de facto states, and organizations, targeted by these state-linked information
operations.
34
