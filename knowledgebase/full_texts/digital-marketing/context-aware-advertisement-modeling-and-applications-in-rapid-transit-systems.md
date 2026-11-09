---
title: Context-aware Advertisement Modeling and Applications in Rapid Transit Systems
url: https://arxiv.org/abs/2409.09956
category: digital-marketing
subcategory: empirical
date: 2024-09
venue: ''
authors:
- Afzal Ahmed
- Muhammad Raees
source: arxiv
pdf_url: https://arxiv.org/pdf/2409.09956
pages: 16
chars: 32493
fetched_at: '2026-11-08T13:11:28+00:00'
kb_version: 1
---

# Context-aware Advertisement Modeling and Applications in Rapid Transit Systems

Context-aware Advertisement Modeling and
Applications in Rapid Transit Systems
Afzal Ahmeda, Muhammad Raees a
aMirpur University of Science and Technology, Mirpur, AJK, Pakistan
Abstract
In today’s businesses, marketing has been a central trend for growth. Mar-
keting quality is equally important as product quality and relevant metrics.
Quality of Marketing depends on targeting the right person. Technology
adaptations have been slow in many fields but have captured some aspects
of human life to make an impact. For instance, in marketing, recent devel-
opments have provided a significant shift toward data-driven approaches. In
this paper, we present an advertisement model using behavioral and tracking
analysis. We extract users’ behavioral data upholding their privacy principle
and perform data manipulations and pattern mining for effective analysis.
We present a model using the agent-based modeling (ABM) technique, with
the target audience of rapid transit system users to target the right person
for advertisement applications. We also outline the Overview, Design, and
Details concept of ABM.
Keywords: Pattern Mining, Behavioral Clustering, Marketing Applications
1. Introduction
With the growing usage of technological data-driven advancement in orga-
nizational settings, business decision-making needs to be reconsidered. Ma-
chine learning technologies are becoming prevalent in businesses, however,
there are many concerns to make such technologies useful in practical con-
texts [1]. This is especially relevant for offline businesses when deciding about
optimal strategic and operational marketing and advertising [2]. Due to per-
vasive mobile and internet usage in modern society, target advertising is an
effective strategy to convey the appropriate message instead of randomized
spamming, Likewise, with anonymous and consensual data collection, com-
panies can advertise to specific market segments meeting the criteria. These
arXiv:2409.09956v1  [cs.MA]  16 Sep 2024

technologies provide their users with more flexibility concerning when, where,
and how to travel. Understanding the influence of ICTs in our mobile in-
formation society [3, 4] will be essential for updating environmental policies
for our task, and maintaining sustainable mobility and transportation [5].
Moreover, ICTs have provided a wide range of spatio-temporal data sources,
which can be used for geographic knowledge discovery and data mining in
studies on geographic dynamics, such as human travel behavior and mobility
patterns [6, 7].
Although several spatiotemporal datasets (e.g., geo-referenced mobile
phone data) only provide incomplete data with relatively low resolution and
few individual attributes, it is important to determine how much and to
what extent we can extract knowledge from sparse data sources, as well
as dealing with uncertainty in sparse datasets but still the extracted infor-
mation is very helpful in determining the behavior of a person towards a
specific brand. Due to the widespread use of mobile communications, there
have been several studies focusing on acquiring geographical knowledge from
geo-referenced mobile phone data and using that knowledge for different pur-
poses. A social positioning method (SPM) combines both location data and
social attributes of mobile phone users to study the dynamics of urban sys-
tems [6]. For instance, by identifying individual trajectories of mobile phone
users based on tracked location data, we can capture new insights into un-
derstanding the basic law of user trajectories. However social networks are
way more expanded these days and almost everyone is connected through
this network data extraction from social networks can be quite helpful in
determining the behavior of the individual as well as a group of personnel
traveling in a specific area and advertising the brands related to them [8].
Although the point of consideration while advertising is the customer our
proposed method is not only going to help customers but also the companies
advertising their brands to only those relevant to them which decreases the
cost in terms of money and effort exerted while advertising their brands to
those who are not even interested.
When it comes to shopping many factors affect the behavior of the cus-
tomer. We have divided the factors into two main states 1) individual state
and 2) external/environmental state. The first state is the description of in-
dividual activity state focusing on the age group, daily routine, occupation,
emotional state income level, etc. while the second state is a description of
the external factors affecting the individual’s life in which we shall be focusing
on the society, friends circle, and travel patterns, etc [6]. This short article
2

provides a case evaluation of optimizing advertisement strategies to target
relevant customers. The targeted advertising can be customized to market
segments, channels, or geographical areas. For instance, by utilizing non-
pervasive and anonymous tracking through Information and communication
technologies (ICTs), such as mobile phone sensors.
The remainder of the article is organized in the following pattern section
2 is the literature review conducted to provide the summary of the work
already done in fields under discussion section 3 is the proposed methodology
to resolve the problem section 4 is the evaluation results to validate our work
and section 5 contains the conclusion and future research direction.
2. Background
We have reviewed our literature in three main points of view Agent-Based
Modeling(ABM), pattern mining and ML applications, and advertisement
strategies.
2.1. Agent based Modeling
Agent-based modeling is considered to be a powerful simulation model-
ing technique that helped in solving many problems in the last few years,
including applications to real-world business problems [9, 10, 11]. The core
objective of using Agent-Based Modeling is to represent the activities and
processes involved in a collaborative environment [12]. Agents should be
more than just a simple software package or program but it is a bit unclear
where the boundaries lie. This is the demonstration of a general problem
present in AI of defining ‘intelligence’ [3]. According to Anumba et al. [13]
Agents should not only be like that their actions are only the results of
their environment but they should have the capability of taking initiative
following a goal-directed behavior. Agent-based modeling is considered an
approach that is being used in epidemiological literature [8]. Machine learn-
ing techniques are quite useful in implementing the behavior of the agents
[14]. Agent-based models (ABMs), using a complex systems approach, pro-
vide a method for examining dynamic interactions of social and demographic
actors at both micro and macro levels [15, 12].
Haghnevis et al. [16] presented a formal agent-based modeling (ABM)
platform that enables managers to predict and partially control patterns of
behaviors in certain engineered complex adaptive systems (ECASs). The
approach integrates social networks, social science, complex systems, and
3

diffusion theory into a consumer-based optimization and agent-based mod-
eling (ABM) platform [16]. The Agent-based modeling approaches are used
in many fields ranging from economics and social sciences to biology and
diverse engineering areas [9, 17, 11]. Understanding ABMs important as it
should describe a complete model, for instance by standardization. Stan-
dardization supports understanding models and making inferences. When
there are issues in standardization, analyzing the protocol issues is essential
and it makes it easier to understand and write models. A root-cause analysis
can also provide an effective strategy to understand what to build in models
[18].
When the system being modeled is complex, modular decentralized, change-
able, and defined at the time of design, ABM is a well-fitted method of mod-
eling [10]. Some models about optimal control to determine the speed of
transport systems are discussed in the literature [12]. Under the optimal
control approach, research studies are mainly grouped into two categories:
exact solution algorithm and heuristic algorithm [19]. Another framework
[20] for cooperation in intermodal freight transport chains as multi-actor
systems. And when it comes to the domain related to the negotiation of the
agents Rosenschein and Zlotkin [21] distributed this domain into three sub-
domains task orientated domains (TODs), state-orientated domains (SODs),
and worth-orientated domains (WODs), here each subdomain is a general-
ization of the previous one TODs are very simple in these the activity of the
agents is based on the set of assigned tasks it has to accomplish. WODs are
the domains where worth is defined by the agents for each state available.
Here goals can be more flexible and making concessions is also allowed. An
example would be agents in an e-marketing place where the goal for a com-
pany may be to obtain the maximum price for a within period b. The chances
of deadlocks and conflicts a present here too but here the environment is more
bargaining.
2.2. Pattern Mining
Majid et al. [2] stated in their article that the pervasive use of digital
cameras and sharing photos on social networks such as Flicker makes a lot
of geo-tagged photos available on the Web. Based on the geo-tagged photos
and experiences shared over social networks, they got the traveling prefer-
ence of the user and proposed a new method to recommend user new tourism
places relevant to them [2]. According to Yoon et al. [4] it takes time for
the travelers to digest and put together the collected information for use.
4

For instance, many Transit systems issue smart cards to traveling personnel
to pay through it. Companies mine the data of individuals to reduce the
involved complexity in travel patterns and make clusters, thereby, mining
customer data for clustering is studied to better service each segment [22].
For instance, businesses can tailor what to market to a specific group of cus-
tomer based on their existing behavior providing clarity of decision-making
for future scenarios. Studies use various methods for customer segmentation
such as clustering models [22]. Bayesian decision tree can also be used to
extract the boarding changes in boarding volumes between two transactions
conducted consecutively and evaluate this information combined with histor-
ical data of the speed profiles extracted using GPS to get the probability of
the potential stop [23].
Density-based Spatial Clustering of application with noise (DBSCAN)
was used to get the travel pattern of individuals efficiently [23? ]. According
to Chun et al., [24] data mining methods based upon the input from past
data available for the prediction of the short-term movements of the impor-
tant currencies, interest rates, or equities have been studied by the researcher
to build a quantitative trading tool to improve the trading to make it effi-
cient [24]. Banks have huge databases containing the transactions and other
personal details that can be used for predictions but human resources are not
enough for this so a data mining technique is necessary to detect the pattern
of the customer and predict the profile of the customer [23]. Liu et al. [25]
proposed a technique named Mining Data Record (MDR) to mine web page
data they extracted the HTML tags to build the tag tree and trained their
system on different domains like book, travel, and auction, software and jobs
and they also compared the results with other two techniques OMINI and
IPEAD and when it came to prediction OMINI only detected 6 out of 46
pages correctly and IPEAD predicted 14 pages correctly while MDR pre-
dicted 44 correctly. In predicting patterns IPEAD does not work for similar
records but MDR is very good at detecting boundaries [25].
2.3. Advertisement Strategies
According to Chen and Tseng [26] the brand equity for a traveler’s behav-
ior is dependent on the following three points (1) frequent visits to that place,
(2) period spent there during visits, and (3) recommendation frequency of
the destination. In a study Brand equity of a tourist place named Bali was
measured in five measurement variables i.e. (1) knowledge about the brand
(2) image of the brand (3) associations of the brand (4) observed quality of
5

brand and (5) loyalty to that brand. They concluded that maintaining the
equity of the brand can help in getting the loyalty of the visitors, choosing
the right area to be targeted, and advantage over the competitors [27]. Build-
ing on Keller’s brand positioning, brand resonance, and brand value chain
models, A study has been conducted in which impact of the brand manage-
ment process fast-paced advancement in technologies, digital development,
and constraints related to environment and social activities have been dis-
cussed. They concluded their discussion by suggesting that responsiveness
according to user needs, innovation in the products, and responsibility are
crucial attributes in the management of brand equity. They also suggested
that global macro changes demand to concentrate on specified brand equity
for both the purposes to meet the expectations of the consumers evolving
day by day and to be in a competitive state and achieve high performance
in the market [28].
Krush et al. [29] explored the connection available between marketing and
resources of the sales (e.g. capability of sales and dashboards for marketing)
and sensemaking, and the combinational effects on performance of the firm.
Their study explored that the capability of sales and using dashboards for
marketing explicitly contribute to the performance of the firm and it also has
an interactive effect with sensemaking. In addition to this, sensemaking can
affect both growth in the firm and the efficiency of the cost. For marketing
scholars, sensemaking is important as it plays a vital role in the knowledge
capabilities of the firm and makes the firm more successful and sound in
facing changes occurring in the market [22]. These studies confirm how im-
portant it is for sales and marketing operations to integrate. Zhao et al. [6]
discussed the preconditions for the success of the first product launched in
the market and the association to existing resources of the firm, and inves-
tigated the strategy of the positioning of the product that can mediate the
effects of technical resources, marketing resources, and startup expertise of
the founding team on the success of the product. The authors claimed that
the impact of the founding teams with more prior experience is smaller than
the founding teams with less prior startup experience.
3. Context-Aware Advertisement
We used the Agent-Based Modeling (ABM) approach to model our re-
search. In brand management first, we need to identify the agents. Our
agents are as follows users, Brands, travel vehicles, and stations. A user
6

in our system is connected to the stations he/she travels, the user is also
connected to social media where we share our locations our likes and dis-
likes, and express our emotional states 1. When a person goes to any station
he/she will be able to watch ads running on the screen but those ads that are
relevant to them are not a big question mark. People ignore such ads which
are not relevant to them. We discussed three strategies to improve the ads
mechanism to display them on the screen.
Figure 1: Generic Model of Context-aware Ad. Manager.
We propose a model 2 in which we generate a map against the user’s
motion getting location data from the GPS of the smartphones they are us-
ing and mining that data combined with the social media, station location,
brand location, and advertisement screen locations to predict the adds to be
displayed on the screen on the different times and different stations. This
model takes user travel history from mobile phone GPS data logs, persons’
personal information from travel company Metro in our case, and social be-
havior of the person from the links the user has provided while signing up
for the Metro card. All this information is processed by the Density-Based
Spatial Clustering of Applications with Noise (DBSCAN). DBSCAN detects
the patterns and makes clusters of them. These clusters are then further
extracted in two main forms (a) Spatial Clusters: Clusters according to lo-
cation patterns (b) Temporal Clusters: Clusters according to time patterns
followed by the users. Based on these clusters, we divided the ad display
tasks into four preferences.
7

Figure 2: Conceptual Diagram of the Proposed Model.
3.1. Behavioral modeling using ODD model
3.1.1. Overview
Purpose: The purpose of the model is to explore the behavior of the
people traveling across the stations and to find more effective and efficient
ways of the advertisement strategy. Under what conditions the ads shall be
displayed on the station screens? How can the travel patterns combined with
their social media activities of people describe the behavior of the people?
And how it is helpful in advertisements?
Entities, state variables, and scales.Our model consists of a set of
entities, state variables, and scales as described below
• Traveling persons Pi
• Brands B j
• Stations Sk
• Each brand and station is characterized by their location Lk
• Each traveling personnel has two state variables: his check-in location
CIN and check-out location COUT
• There is a global variable of hour of the day Th
8

• The distance D between the stations is not specified as we designed a
generic model
Process overview. The processes in our model are the patterns of the
persons traveling from one station to another station at different times, per-
sons visiting the brands, and persons liking the ads. At each time step person
moves from one station to another while the station and brands observe at
each time step as if some person has visited a specific place.
3.1.2. Design concept
In our model, the basic principle that is addressed is the idea of relevant
advertisements on the screens. The screen is going to adapt a specific type
of ad at the time according to the changes made in the environment by other
agents like the type of persons coming to the station at a specific time. This
adaptive behavior is modeled by simply observing the previous travel history
of the persons using that track. Our model does not include direct interaction
among the traveling personnel. As at a time traveling toward a station in the
peak hours there is a probability that people will be of the same profession.
This probability is going to help in the decision-making of the Density-Based
Spatial Clustering of Application with Noise (DBSCAN) algorithm and will
help make clusters afterward.
Emergence: This idea emerged from the concept of utilizing rapid tran-
sit systems for advertisement. Rapid Transit Systems are one of the most
rushy areas during the whole day. Hence, we can target the most appropriate
audience at these stations.
Observation: In this model we observe the user movement pattern. The
decisions will be made based on user feedback and movement.
Adaptive behavior: If the user provides positive feedback or remains
silent then the ads will continue. Otherwise, more relevant ads will be put
to him.
Sensing: We will sense the motion of the users and the frequency of the
users. Also, we will sense the trend of the users.
Prediction: Prediction will lead to the decision-making. The system
will predict appropriate ad. for specific target.
Interaction: This model will keep the interaction of different stakehold-
ers like a service provider, customer, and broker.
Stochasticity: The movement and task of the users varies. Hence, this
system will deal with such variability.
9

3.1.3. Model Details
Initialization: The distance between the stations was initialized at the
start of the model. The persons initialized at the start of the model were
1000, stations were initialized to 7, and brands were initialized to 10 at
each station. The persons (agents) were initialized according to real-world
information about the type of buildings around the stations at the peak hours
T1, off-peak hours T2, and night times T3 which have almost 3: 2: 1 ratio
respectively.
Input: The brand’s feedback will provide the input data to the system.
Sub models: The adapting behavior of the screens sub-model defines
what exactly is going to be displayed on the screen it only takes the inputs
in the clusters forms and the decision-making is based on the type of times
we decided. This sub-model decides whether to display ads according to the
density of the people at the station or the density of the buildings surrounding
it. The decision of whether to display an ad according to the density of the
people at the station or according to the type of the buildings surrounding
the station is decided by the variable T h which tells the density of the people
at that time of the day at a specific station. Here are some of the preferences
we used.
Ads according to Maximum number of audience:In this technique
probability of the number of users will define the type of ads to be displayed
on the screen of the station. For example, if there are n total personnel
predicted at that time of the day and according to our algorithm let a, b,
and c be the number of personnel related to different professions then the ad
to be displayed is calculated as
highestO(a, b, c) ↔ adToBeDisplayedOnScreen
Ads according to audience ratio:In this technique ads shall be dis-
played in the ratio of the audience predicted at that time of the day. For
example, if there are n personnel on the station and, a and b are the number
of audiences predicted at that time of the day then ads shall be displayed in
the ratio of the audiences available. The screen shall be shared by the ads
according to the ratio of the audiences detected.
P (a/n) > P(b/n) ↔ TOS(a) > TOS(b)
Here P(a/n) is the probability of a while TOS function returns the Time
On Screen value for each ad.
10

Ads According to the nearest Buildings to the station:In this
technique preference is given to the buildings available near the station. A
station is mostly filled by the people working in the areas near to that station
so it would be a good idea that the ads shall be displayed according to the
nearest buildings and the time at which people mostly use the station to go
to those buildings. Let d be the set of buildings and t be the set of time
spans at which the station is filled with the people going to those buildings.
d(i) ∧ t(j) ↔ adToBeDisplayedOnScreen
Where i and j are the indices of the sets a and b and
timeFor(d(i)) = t(j) ↔ i = j
Ads according to Building ratio:In this technique ads shall be dis-
played in the ratio of the building around that station if according to predic-
tion people from the different buildings visit the station at the same time of
the day. Then the ads shall be displayed according to the number of people
predicatively visiting the station and going to that building. Let d be the set
of the building a,b be the number of visitors of that building on the station
then mathematically it can be represented as
(a(d(i)) > b(d(j))) → (TOS(d(i)) > TOS(d(j))) ∴ i ̸= j
Cost Evaluation: We evaluate the cost of ads in two main points (1)
density of the visitors and (1) density of the buildings near by Cost according
to Density of the Visitors. In this case, we calculate the cost of the ads
keeping in mind the density of the users in the office starts and end times.
Let VR be the relevant user view Let C(VR) be the cost of the relevant view
Using these two we can calculate the Total cost of the ad.
TotalCost =
nX
i=1
VR · C(VR)
Where C(VR) can be calculated as
C(VR) = (SingleUserPerSecondViewCost) × (TotalTimeInSeconds)
Cost according to Density of the Nearby Building:In this case
we are going to calculate the cost of the ads being displayed in terms of the
11

building surrounding it as on off days or even office times visitors only visit
a station according to the buildings nearby. For this purpose, we need to
define the station business factor which is the value of the station at that
time of the day. Let, SBR be the Station Business Factor, T be the total
time the ad is being displayed, and PR be the per-second rate of the ad then.
TotalCost = PR × SBF × CA
Here CA is the Ad Cost which can be calculated as
CA = PR × T
4. Scenario
Let’s consider the scenario of the Rawalpindi-Islamabad Metro Bus Sys-
tem in Pakistan. This rapid transport system has a total length of 22 kilome-
ters with 24 stations. An average of 0.1 million passengers per day use this
transport. Normally, passengers traveling regularly use metro cards. Based
on that metro card their daily entering and leaving stations can be recorded.
Suppose, a student of Bahria University Islamabad named Usama has a
residence at 6th-Road Satellite Town Rawalpindi. Often, he enters the 6th-
Road station between 8:30 am to 9:00 am and checkout at Kechahri station
between 8:50 am to 9:20 am. Similarly, Usama enters Kechari station from
5:00 pm to 5:30 pm and leaves at 5:20 pm to 5:50 pm. On weekends and
holidays, Usama visits Saddar and 7th Avenue as well. Depending upon this
information we can send him relevant ads. Let’s say Subway has a branch in
F-8 and Usama moves in that direction from the nearest station Kechahri.
Then, the addition of the Subway will be appropriate for Usama. Similarly,
if Usama provides feedback that the Subway advertisement is not relevant to
him then, other ads. according to his interest should be sent. Also, Cabinet
Computer at 6th Road announces a discount on laptops. So, this ad. should
also be sent to Usama. Now, we have a problem that how these ads. will be
managed by the broker in case of more appropriate ads. for specific users.
For this purpose, our model introduces different schemes. These ads. can
be managed based on either the audience ratio or the cost. The formulas
described in the model can be used to calculate these factors.
12

5. Conclusion
The study has proposed an effective method to improve advertisement
strategy. We used travel data of the persons to identify the patterns and
to get help in decision-making of which ad to be displayed on any screen.
After the evaluation, the results have shown that the travel patterns of the
persons are quite helpful in determining the behavior of the person which in
turn can be used to make decisions about the advertisement strategy for a
specific group of people. We also calculated the cost of the ads to companies
according to the number of audiences available at any time of the day.
References
[1] M. Raees, I. Meijerink, I. Lykourentzou, V.-J. Khan, K. Papangelis,
From explainable to interactive ai: A literature review on current trends
in human-ai interaction, International Journal of Human-Computer
Studies (2024) 103301.
[2] A. Majid, L. Chen, G. Chen, H. T. Mirza, I. Hussain, J. Woodward, A
context-aware personalized travel recommendation system based on geo-
tagged social media data mining, International Journal of Geographical
Information Science 27 (4) (2013) 662–684.
[3] M. Raubal, Cogito ergo mobilis sum: the impact of location-based ser-
vices on our mobile lives, The SAGE handbook of GIS and society (2011)
159–173.
[4] H. Yoon, Y. Zheng, X. Xie, W. Woo, Social itinerary recommendation
from user-generated digital trails, Personal and Ubiquitous Computing
16 (2012) 469–484.
[5] A. de Souza e Silva, Cell phones and places: The use of mobile tech-
nologies in brazil, in: Societies and cities in the age of instant access,
Springer, 2007, pp. 295–310.
[6] Y. L. Zhao, D. Libaers, M. Song, First product success: a mediated
moderating model of resources, founding team startup experience, and
product-positioning strategy, Journal of product innovation manage-
ment 32 (3) (2015) 441–458.
13

[7] Y. Chang, H. Zhao-Cheng, Travel pattern recognition using smart card
data in public transit, International Journal 6 (2016).
[8] A. M. El-Sayed, P. Scarborough, L. Seemann, S. Galea, Social network
analysis and agent-based modeling in social epidemiology, Epidemiologic
Perspectives & Innovations 9 (1) (2012) 1–9.
[9] W. Rand, C. Stummer, Agent-based modeling of new product market
diffusion: an overview of strengths and criticisms, Annals of Operations
Research 305 (1) (2021) 425–447.
[10] T. Novosel, L. Perkovi´ c, M. Ban, H. Keko, T. Pukˇ sec, G. Krajaˇ ci´ c,
N. Dui´ c, Agent based modelling and energy planning–utilization of mat-
sim for transport energy demand modelling, Energy 92 (2015) 466–475.
[11] F. Riaz, S. I. Shah, M. Raees, I. Shafi, A. Iqbal, Lateral pre-crash sens-
ing and avoidance in emotion enabled cognitive agent based vehicle-2-
vehicle communication system, International Journal of Communication
Networks and Information Security 5 (2) (2013) 127.
[12] M. Raees, T. A. Khan, K. Mustafa Abbasi, A. Ahmed, S. Fazilat,
I. Ahmed, Context-aware services using manets for long-distance vehic-
ular systems: A cognitive agent-based model, Scientific Programming
2021 (1) (2021) 8835859.
[13] C. Anumba, Z. Ren, A. Thorpe, O. O. Ugwu, L. Newnham, Negotia-
tion within a multi-agent system for the collaborative design of light
industrial buildings, Advances in Engineering Software 34 (7) (2003)
389–401.
[14] K. Dehghanpour, M. H. Nehrir, J. W. Sheppard, N. C. Kelly, Agent-
based modeling of retail electrical energy markets with demand response,
IEEE Transactions on Smart Grid 9 (4) (2016) 3465–3475.
[15] N. E. Williams, M. L. O’Brien, X. Yao, Using survey data for agent-
based modeling: design and challenges in a model of armed conflict
and population change, Agent-based modelling in population studies:
Concepts, methods, and applications (2017) 159–184.
14

[16] M. Haghnevis, R. G. Askin, D. Armbruster, An agent-based modeling
optimization approach for understanding behavior of engineered com-
plex adaptive systems, Socio-Economic Planning Sciences 56 (2016) 67–
87.
[17] M. Dorigo, M. Birattari, X. Li, M. L´ opez-Ib´ a˜ nez, K. Ohkura, C. Pin-
ciroli, T. St¨ utzle, Swarm Intelligence: 10th International Conference,
ANTS 2016, Brussels, Belgium, September 7-9, 2016, Proceedings, Vol.
9882, Springer, 2016.
[18] M. Raees, Study of software quality improvement through reliability
metrics models and root cause analysis program, International Journal
of Computer Engineering and Information Technology 12 (6) (2020) 42–
47.
[19] X. Yang, X. Li, B. Ning, T. Tang, A survey on energy-efficient train
operation for urban rail transit, IEEE Transactions on Intelligent Trans-
portation Systems 17 (1) (2015) 2–13.
[20] A. Di Febbraro, N. Sacco, M. Saeednia, An agent-based framework for
cooperative planning of intermodal freight transport chains, Transporta-
tion Research Part C: Emerging Technologies 64 (2016) 72–85.
[21] J. S. Rosenschein, G. Zlotkin, Rules of encounter: designing conventions
for automated negotiation among computers, MIT press, 1994.
[22] M. Raees, V.-J. Khan, K. Papangelis, Four challenges for iml designers:
Lessons of an interactive customer segmentation prototype in a global
manufacturing company, in: Extended Abstracts of the 2023 CHI Con-
ference on Human Factors in Computing Systems, 2023, pp. 1–6.
[23] M. Hammawa, Data mining for banking and finance, Oriental J. Com-
put. Sci. Technol 4 (2011) 273–280.
[24] S.-H. Chun, S. H. Kim, Data mining for financial prediction and trad-
ing: application to single and multiple markets, Expert Systems with
Applications 26 (2) (2004) 131–139.
[25] B. Liu, R. Grossman, Y. Zhai, Mining data records in web pages, in:
Proceedings of the ninth ACM SIGKDD international conference on
Knowledge discovery and data mining, 2003, pp. 601–606.
15

[26] C.-F. Chen, W.-S. Tseng, Exploring customer-based airline brand eq-
uity: evidence from taiwan, Transportation journal 49 (1) (2010) 24–34.
[27] I. K. S. Diarta, The influence of bali brand equity on tourists traveling
behavior, E-Journal of Tourism 2 (2) (2015) 96–114.
[28] Z. G¨ urhan-Canli, C. Hayran, G. Sarial-Abi, Customer-based brand eq-
uity in a technologically fast-paced, connected, and constrained environ-
ment, AMS review 6 (2016) 23–32.
[29] M. T. Krush, R. Agnihotri, K. J. Trainor, E. L. Nowlin, Enhancing
organizational sensemaking: An examination of the interactive effects
of sales capabilities and marketing dashboards, Industrial Marketing
Management 42 (5) (2013) 824–835.
16
