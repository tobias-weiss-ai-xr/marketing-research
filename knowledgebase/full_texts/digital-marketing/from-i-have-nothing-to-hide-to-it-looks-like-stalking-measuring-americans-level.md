---
title: 'From "I have nothing to hide" to "It looks like stalking": Measuring Americans'' Level of Comfort
  with Individual Mobility Features Extracted from Location Data'
url: https://arxiv.org/abs/2502.05686
category: digital-marketing
subcategory: empirical
date: 2025-02
venue: ''
authors:
- Naman Awasthi
- Saad Mohammad Abrar
- Daniel Smolyak
- Vanessa Frias-Martinez
source: arxiv
pdf_url: https://arxiv.org/pdf/2502.05686
pages: 33
chars: 112370
fetched_at: '2026-11-08T13:13:20+00:00'
kb_version: 1
---

# From "I have nothing to hide" to "It looks like stalking": Measuring Americans' Level of Comfort with Individual Mobility Features Extracted from Location Data

From "I have nothing to hide" to "It looks like stalking": Measuring Americans’
Level of Comfort with Individual Mobility Features Extracted from Location Data
Naman Awasthi
University Of Maryland, College Park
Saad Abrar
University Of Maryland, College Park
Daniel Smolyak
University Of Maryland, College Park
Vanessa Frias-Martinez
University Of Maryland, College Park
Abstract
Location data collection has become widespread with smart
phones becoming ubiquitous. Smart phone apps often collect
precise location data from users by offering free services,
and then monetize it for advertising and marketing purposes.
While major tech companies only sell aggregate behaviors
for marketing purposes; data aggregators and data brokers
offer access to individual location data. Some data brokers
and aggregators have certain rules in place to preserve pri-
vacy; and the FTC has also started to vigorously regulate
consumer privacy for location data. In this paper, we present
an in-depth exploration of U.S. privacy perceptions with re-
spect to specific location features derivable from data made
available by location data brokers and aggregators. These
results can provide policy implications that could assist orga-
nizations like the FTC in defining clear access rules. Using a
factorial vignette survey, we collected responses from 1,405
participants to evaluate their level of comfort with sharing
different types of location features, including individual trajec-
tory data and visits to points of interest, available for purchase
from data brokers worldwide. Our results show that trajectory-
related features are associated with higher privacy concerns,
that some data broker based obfuscation practices increase
levels of comfort, and that race, ethnicity and education have
an effect on data sharing privacy perceptions.We also model
the privacy perceptions of people as a predictive task with F1
score 0.6.
1 Introduction
Location (GPS) data collection has become widespread with
smart phones becoming ubiquitous. Smart phone apps of-
ten collect precise location data from users by offering free
services like navigating using Maps, tracking fitness goals,
finding relevant and customized search results, social network-
ing and meetups, or location tracking for personal safety in
times of crises, among others. Location data is used by app
developers to understand app usage, improve functionalities
and most importantly, to serve personalized ads and drive
monetization.
Monetization is driven by two distinct approaches. Tech
companies like Google 1, Apple or Meta collect precise lo-
cation data from their users and use the data internally to
improve app functionality while selling aggregate behaviors
(e.g., geographical areas visited) for advertising purposes.
However, an individual’s location data is never shared with or
sold directly to third parties. On the other hand, data aggrega-
tors and data brokers collect, repackage, and sell individual
location data to third-parties, including private organizations
and academic researchers [1, 2, 3, 4]. These data aggregators
either develop their own apps, or create Software Develop-
ment Kits (SDK) that are then shared with app developers
to collect location data from specific apps. Well-known tech
companies have faced lawsuits for location tracking with-
out the user’s consents 2,3. The Federal Trade Commission
(FTC) has also penalized two data brokers in 2024, for selling
location data to advertisers without adequately informing con-
sumers or obtaining their consent [5]. However, while tech
companies never share individual location data with third par-
ties, data brokers do, and this has created several instances
of inappropriate uses including the US Defense department’s
access to prayer app’s location data to monitor Muslim com-
munities [6], local law enforcement agencies tracking racial
justice protesters using location apps [6], and the use of loca-
tion data purchased from data brokers to track gay priests [7]
and people who visit abortion clinics [8].
As a result of these news, some data aggregators and data
brokers have created policies to prevent sensitive information
about individuals being leaked. For example, data aggregator
companies like Cuebiq don’t allow the identification of visits
to healthcare locations on their platforms, or only allow for the
1https://policies.google.com/technologies/location-data?
hl=en-US#how-is-location-information-used-for-ads
2https://www.tzlegal.com/news/37-5-million-settlement-f
acebook-tracking-users-location-without-consent/
3https://www.reuters.com/legal/google-pay-155-million-s
ettlements-over-location-tracking-2023-09-15
1
arXiv:2502.05686v1  [cs.CY]  8 Feb 2025

identification of home locations obsfuscated as census tracts
4. However, although internal policy guidelines are important,
they are solely based on data aggregators’ decisions rather
than on the perceptions of users whose location data is being
monetized. We put forward that true consumer privacy rules
need to come directly from consumer privacy perceptions.
In this paper, we conduct a thorough evaluation of user
levels of comfort with respect to the use of individual location
data - acquired from data aggregators and data brokers - to
identify and characterize personal trips and visits to places.
Studies in the past have used survey approaches to explore
people’s perceptions toward the collection and use of indi-
vidual location data, with a focus on points of interest (POI)
visited [9, 10, 11]. For example, past research has shown that
users feel much more comfortable sharing their work or home
location than their location when they attend a rally or visit
a medical facility [10]. However, points of interest are not
the only feature available. In fact, travel history of millions
of individual devices are available from data aggregators 5.
This location data is useful in deriving trajectory-based fea-
tures such as origin-destination trips (e.g., trips from home to
work) or the use of specific modes of transport (e.g., identify-
ing driving vs. use of public transit vs walks). In this paper, we
extend the state of the art in individual location data privacy
perceptions by evaluating user perceptions with respect to
trajectory-based features extracted from location data as well
as points of interest, and we do so using U.S. representative
surveys.
Obfuscation Techniques. As stated before, data aggrega-
tors have developed approaches to extract trajectory and visit
features from location data and obfuscate details in privacy
respectful ways. For example, instead of computing the ex-
act home location, the location is computed as a census tract
(SafeGraph); [12] or instead of sharing the exact route trajec-
tory, data points are changed to obfuscate movement patterns
towards sensitive locations and home/work location ( e.g.,
Data aggregators like spectus protects trajectories that end
at home by replacing exact home location with the centroid
of the census tract a person’s home is in [13]). In this paper,
we conduct an extensive review of current obfuscation ap-
proaches via published papers to identify the different types
of techniques applied to individual location data acquired
from data brokers; and we evaluate user privacy perceptions
when using obfuscated location data vs. detailed (raw) loca-
tion data. It is important to clarify that we exclusively focus
on obfuscation techniques that directly change the location of
a user as opposed to anonymization mechanisms that attempt
to hide the actual location [14].
Factorial Vignette Approach. Past literature like [11, 15],
has shown that the level of comfort with location data sharing
varies depending on who would be accessing the data and
4https://cuebiq.com/spoi-policy/
5https://datarade.ai/data-categories/mobile-location-dat
a
for what purpose. We follow Nissembaum’s [16] contextual
integrity (CI) framework similar to [11] for creating survey
questions that ask participants to evaluate their level of com-
fort with a specific feature to be used for a certain purpose by
a certain actor. Using a factorial vignette survey approach we
randomly create plausible combinations of actors, purposes
and features to expose survey participants to different ways
in which their location data could be used. Understanding
these nuanced privacy perceptions can support the creation
of policies and rules concerning the types of features that
can be extracted from location data, the types that should be
avoided because they generate low levels of comfort, and the
types of privacy respectful practices that are successful in
increasing users’ level of comfort. The FTC has started to
vigorously regulate consumer privacy providing "bright-line
rules" for companies to clearly understand what can and can-
not be done with location data [17]. This paper is an effort
to illuminate this path, and provide guidelines for potential
future FTC-proposed rules. To sum up, the main contributions
and findings of this paper are:
• A thorough evaluation of user levels of comfort with respect
to the use of trajectory data and Points of Interest taking
into account actors and purposes. Our results show that
people were uncomfortable particularly towards movement
(trajectory-based) features such as frequent travel paths and
were more comfortable with obfuscated home, work, and
walk features. To the best of our knowledge, we are the first
ones to reveal user perceptions with respect to the use of
trajectory data.
• An evaluation of users’ level of comfort with respect to
current data brokers’ practices around the use of privacy
respectful approaches to compute features from location
data. Our results reveal a distinct preference for obfuscation
approaches, especially when applied to detailed trajectory
data. To the best of our knowledge, we are the first ones
to evaluate user perceptions with respect to current data
aggregator practices.
• An analysis of how levels of comfort change with respect to
educational background as well as racial and ethnic groups.
Our analysis shows that there are significant differences
in comfort between the racial groups White, Asian, His-
panic and Black. Additionally, participants with higher
self-reported knowledge of computer science/programming
were associated with higher comfort in sharing location
features.
2 Literature Review
2.1 Location Data Tracking
Location data can be collected using GPS sensors/Bluetooth
beacons on mobile phone devices or smart-watches and using
2

WiFi or IP addresses when surfing the web. Current app de-
velopment toolkits offer the possibility of combining location
data from multiple sensors to get better accuracy: for example,
the Fused location Provider API [18] in Android development
or the CLLocationManager [19] in iOS development. In ad-
dition, there exist several third-party Software development
Kits (SDKs) (e.g., X-Mode, SafeGraph) that help app develop-
ers, tech companies and data brokers and aggregators collect,
visualize and track location data [20].
With data from data brokers and aggregators, many re-
searchers have shown that location data characterizing the
places visited by a person as well as their trajectories can be
useful in a plethora of settings such as modeling the spread-
ing of a pandemic through tracing apps [21], inferring socio-
economic indicators [22, 23], health outcomes [24], urban
development and disaster risk [25, 2], targeted marketing and
advertising [26], understanding migration patterns [27], im-
proving public transit [28], or modeling mobility patterns for
public safety [29].
At the same time, there has been a lot of work focused
on privacy preserving methods for location data. Primault et.
al. [14] extensively outline the techniques for sharing location
data in a privacy preserving manner either via anonymization
or obfuscation approaches. While obfuscation techniques di-
rectly change the location of a user to protect their privacy,
anonymization mechanisms attempt to hide the actual loca-
tion from an attacker. In this paper, we focus on obfuscation
techniques, not on k-anonymization approaches, since obfus-
cation is the most common method used by data brokers, data
aggregators and the researchers and analysts acquiring and
analyzing location data from these companies.
2.2 Privacy Perceptions for Location data
Duckham et. al. [30] define location privacy as "special type
of information privacy which concerns the claim of individ-
uals to determine for themselves when, how, and to what
extent location information about them is communicated to
others". Our research builds on prior work investigating pri-
vacy perceptions around sharing personal location data in
various contexts [11, 9, 15]. Prior research has looked into
the effects of different variables on the willingness of indi-
viduals to share their personal location data including the
role of (1) Actors, defined as individuals accessing the loca-
tion data [11, 15, 10, 31] (2) Purposes, defined as how the
location data is going to be used [11, 32, 10] (3) Time, de-
fined as the duration of the access to location data [11, 32]
(4) Age [9, 33, 34] (5) Privacy attitudes [35, 36], and (6)
Socio-cultural aspects [37, 32, 38, 39].
These works have shown that actors like the FBI, com-
mercial entities, employers and data brokers are negatively
perceived while local government and social media compa-
nies generate more positive perceptions when collecting and
using location data. The duration of the location data collec-
tion as well as the purposes of using location data have also
been associated with varying levels of comfort when sharing
that data. For example, while the identification of sexual ori-
entation or political views are perceived negatively, purposes
related to public health or public safety are perceived more
positively.
There is also research exploring the use of location data
for specific settings such as surveillance [40, 20], location
tracking for advertisements [41], or location tracking for pan-
demic contexts. Surveillance applications have been associ-
ated with some level of comfort in human-centered contexts
like disaster recovery. On the other hand, research during
COVID-19 found strong opposition towards contact tracing
apps [38, 39, 42], with over 50% of the participants in both
studies being unlikely to install such apps due to concerns
around government intrusion.
Finally, prior work has also examined how monetary in-
centives influence participants’ willingness to share their
location data for specialized research studies or market re-
search [43, 44]; and the relationship between personality traits
and privacy perceptions [35, 36]. Participants’ positive per-
ception of the service collecting their data, higher incentives,
agreeableness, conscientiousness, and openness to new ex-
periences were also linked positively to comfort in sharing
location data.
Building on these findings, we extend the state of the art
by (1) evaluating user perceptions with respect to trajectory-
based features extracted from location data, beyond current
analyses focused on visits to points of interest (POI), (2) evalu-
ating user privacy perceptions when using obfuscated location
data vs. detailed (raw) location data, and (3) analyzing the
effect of race, ethnicity and education on privacy perceptions
with respect to trajectory and POI visit location data.
2.3 Predicting Privacy Preferences
Privacy fatigue is an important issue highlighted in research.
This fatigue stems from factors like ubiquitous collection of
personal data, scarcity of alternatives and additional permis-
sion requirements people need to go through [45, 46, 47].
Prediction models have been developed to explore peo-
ple’s perceptions around data collection and sharing like
[48, 49, 50, 51, 26, 11]. In these paper, the authors model
people’s perceptions of comfort in sharing location data as a
multi-class classification or regression problem and model the
perceptions around different actors accessing location data
for different purposes. Eg: [51] models people’s perceptions
in sharing IOT data as a binary classification task (predict-
ing allow/deny); reporting accuracies of 77.6% (0.70 recall)
for a multi-class, 3-point Likert classification task, and 81%
(0.78 recall) for the binary classification. In another study,
researchers created binary classifiers to determine privacy atti-
tudes with regards to data sharing in several contexts including
sharing biological data or personally identifying information
3

(PII) [52]; achieving a mean recall of 0.46 for prediction of
privacy concerns from contextual labels.
In this paper, we explore binary and multi-class approaches,
similarly to prior works.
3 Survey Design
Past work has shown that the level of comfort when sharing
highly private information is influenced by who accesses the
data and for what purpose, as stated by Nissembaum’s con-
textual integrity framework [16]. Hence, we used a factorial
vignette survey approach where each vignette in the survey
was created following the same format: Actor X wants to do
Purpose Y and for that, they need to use Feature Z while
systematically changing actors, features and purposes across
participants to test their relevance. For example, a potential
survey vignette could be "A doctor wants to monitor your
personal wellness. For that purpose they want to access your
detailed walking activity. How comfortable would you feel
with this use of your personal location data?". Levels of com-
fort were measured using a 5-point Likert scale, from Very
Uncomfortable to Very Comfortable. Participants were also
asked to fill out a free-form text box explaining their answer
(see Figs. 6 and 7 in the Appendix for two survey question
examples). Next, we describe location features, actors and
purposes in detail.
Location Features We advance the state of the art in the
evaluation of location data privacy perceptions along two
main fronts. First, we consider features extracted from loca-
tion data that go beyond current analyses focused on visits to
points of interest (POI) such as visiting a hospital or a liquor
store. Specifically, we evaluate trajectory-based features that
are extracted from location data by considering sets of GPS
points that define spatio-temporal datasets characterizing tra-
jectories. For example, we can ask a participant about their
level of comfort with a company using their detailed driving
trips (showing the specific route followed) or their detailed
walking activity.
Second, we evaluate trajectory-based and POI visit features
using two approaches: detailed and obfuscated. While de-
tailed uses all GPS points available, obfuscating approaches
characterize location data using current state-of-the-art data
aggregator practices of obfuscation. For example, an obfus-
cated driving trip would only specify the origin and destina-
tion census tract of the trip instead of the detailed trajectory
with all locations (GPS points) visited in-between. Similarly,
an obfuscated home location would only specify home loca-
tion at the county level instead of the exact location.
Table 1 shows all the features we have used to craft the
survey vignettes. These features can be categorized into six
groups: "Home+Work", "Places Visited", "Transportation",
"Movement", "Walking Activity", and "International Trips".
For each feature in each category, we define both its Detailed
(D) and its Obfuscated (Ob) version. Next to each feature
in the Table, we provide links to papers that compute these
features using location data acquired from data brokers or
aggregators, showing that these are in fact state-of-the-art
features when working with datasets from data aggregators.
While POI features such as home, work and places visited
have already been explored in the literature, comfort percep-
tions for obfuscating approaches for these have not been ex-
plored; nor the other trajectory features in either detailed or
obfuscated forms. Each of these features is presented to the
survey participants via an accompanying visualization. See
the Description column in Table 1 for links to sample visu-
alizations shown to survey participants. More details about
survey design choices, including visualizations, are explained
at the end of this section.
Actors Table 2 shows the list of the nine actors we use
to create the vignette questions. These actors have been
examined in previous studies related to location data pri-
vacy [11, 15] and represent the majority of entity types that
can access an individual’s location information. Our work’s
novel contribution lies in looking at the effect of these actors
on privacy perceptions in conjunction with novel trajectory-
based features while controlling for demographic and educa-
tional data.
Purposes Table 3 lists the ten different purposes we use
when crafting the vignette questions. These purposes are in-
formed by prior work looking into privacy perceptions related
to location data [11, 15], and cover public service purposes
such as understanding where to build a new hospital, public
health purposes such as monitoring population mobility dur-
ing a pandemic, law enforcement such as using location data
to identify criminal activity, as well as economic, commercial
and general purpose such as using location data to show ads
or optimize productivity.
There are combinations of actor, feature and purpose that
do not make sense. For example, a doctor will not be interested
in getting access to mobility patterns at city scale. Hence, we
eliminate implausible combinations from the pool of possible
questions. After this process, a total of 445 valid combinations
of actor, purpose and feature are left and randomly shown to
participants.
We did a qualitative study with 5 respondents recruited
from Craigslist to understand comprehension of vignette ques-
tions asked in the survey. They were asked to answer 10
randomly selected vignette questions and elaborate on their
thought process. All the respondents were able to interact
with the map visualizations, answer our questions about the
contents of the map and did not raise any issues with the
structure of the vignettes.
3.1 Design Choices
Prior work in privacy risk perception studies has shown three
important insights that we build on when creating the survey.
First, [47] showed that abstract scenarios are often perceived
4

Table 1: Location Features and Abbreviations. We cite examples of recent studies where such features are used in the "feature
cluster" column
Feature Cluster Feature Abbreviation Description
Your inferred home location Home location (De-
tailed)
Home location as a point on map (Eg. fig. 10)
Your inferred home location represented
as a census tract
Home location (Obfus-
cated)
Home’s county location (Eg., Fig. 11)
Your inferred work location Work location (De-
tailed)
Work location as a point on map (Eg., Fig. 12)Home + Work [3, 4]
Your inferred work location represented
as a census tract
Work location (Obfus-
cated)
Work’s county location (Eg., Fig. 13)
The places you visit Places you visit (De-
tailed)
Chart indicating types and frequency of places visited.
Includes a map depicting the detailed locations of the
places visited (Eg., Figs. 14, 15)
The types of places you visit Places you visit (Obfus-
cated)
Chart indicating types and frequency of places visited
(Eg., Fig. 15)Places Visited [53, 4, 54]
The geographical area where you spend
most of your time
Area you spent most of
your time (Obfuscated)
Map displaying radius of gyration (Eg., Fig. 16)
The modes of transportation you use,
with what frequency and their corre-
sponding routes
Modes of transportation
(Detailed)
Chart indicating frequency and types of mode of trans-
port used. It also includes a map with lines indicating
detailed routes for each frequent mode of transport (Eg.,
Fig. 17, 18)Transportation [55, 56, 4] The modes of transportation you use and
with what frequency
Modes of transportation
(Obfuscated)
Chart indicating frequency and types of mode of trans-
port used (Eg., fig 18)
Your most frequent trips Most frequent trips (De-
tailed)
Map with frequently taken routes. Routes are detailed
showing start and end locations as well as the in-between
GPS points visited (Eg., Fig. 19)
Your least frequent trips Least frequent trips (De-
tailed)
Map with infrequently taken routes. Routes show start
and end locations as well as all the GPS points visited
(Eg., Fig. 20)
Your most frequent types of trips Most frequent type of
trips (Detailed)
Map with the different frequent trips taken and the in-
ferred trip purpose by type of destination (Eg., Fig. 21)
Your most frequent trips represented by
their origin and destination census tracts
and connected by a line
Most frequent trips be-
tween counties (Obfus-
cated)
Map with frequently taken routes. It protects privacy
by showing the start and end points as counties, and the
frequently taken routes as straight lines between counties
instead of detailed GPS. (Eg., Fig. 22)
Movement [55, 57, 54]
Your most frequent trips represented by
their origin and destination census tracts
and connected by an approximate route
Most frequent trips
between counties
(’Google’) (Obfus-
cated)
Map with frequently taken routes. It protects privacy by
showing the start points, end points as counties, and the
frequently taken routes as suggested by Google Maps,
instead of the actual GPS route. (Eg., Fig. 23)
Your walking activity and the corre-
sponding routes
Frequent walking activ-
ity (Detailed)
Chart indicating frequency and duration of walks. It also
includes a map with detailed GPS trajectories indicating
routes for each frequent walking path (Eg., Fig. 24 and
25)Walking Activity [1, 58, 56, 59] Your walking activity Frequent walking activ-
ity (Ob)
Chart indicating frequency and duration of walks with
no detailed trajectories (Eg., Fig. 25)
The foreign countries you have visited
and the duration of the visit, including
all the locations where you have stayed
International visits (De-
tailed)
Chart indicating frequency,duration and location of inter-
national trips. It includes a map with detailed GPS points
indicating regions visited in the foreign county (Eg., Fig.
26)International Trips [60] The foreign countries you have visited,
and for how long
International visits (Ob) Chart indicating frequency, duration and location of in-
ternational trips. (Eg., Fig. 27)
as being less risky when compared to personal scenarios.
Hence, before starting the survey questions, we ask partici-
pants to situate themselves in the vignettes as if this was their
own personal data. In addition, the questions are phrased in a
way that put the participant at the center of the vignette using
the "you" pronoun (see Appendix C.1 for more details on this
design).
Second, prior work has shown that visualizations can help
better understand privacy risks, and that when privacy-related
questions are asked with visualizations, privacy risk concerns
with data sharing tend to decrease [61]. Hence, each of the
vignette questions in the survey is accompanied by an inter-
active visualization of the location feature, as well as by a
brief explanation of that visualization to make sure that the
user understand the feature extracted from the location data.
Figure 6 in the Appendix shows a visualization for a question
where the feature is detailed trajectory data and transportation
modes. The Appendix shows three other examples of fea-
ture visualizations including detailed features Frequent Trips
(Fig. 19) and visits to points of interest (Fig. 14) as well as
5

Table 2: Actors and the abbreviations. Actors taken from
previous studies like [11, 32, 15]
Actor Abbreviation
An emergency service - like emergency
medical services or fire and rescue services
Emergency services
A federal government agency - like the
FBI or CIA
Federal government agency
A local government agency Local government agency
Your employer Employer
A commercial entity Commercial Entity
Your family Family
Your doctor Doctor
A law enforcement agency - like a city po-
lice department or a county sheriff’s office
Law enforcement agency
Academic researchers Academic researchers
Table 3: Purposes and Abbreviations. Purposes taken from
previous studies like [11, 32, 15]
Purpose Abbreviation
Understand criminal activity by looking into
the relationship between crime, people’s move-
ments and locations visited
Analysis of criminal
activity
Analyze terrorist attacks by looking into peo-
ple’s movements and locations visited
Analysis of terrorist at-
tacks
Monitor how people move (or don’t) to control
the spread of a disease e.g., covid-19
Control spread of dis-
eases
Monitor your personal wellness and physical
activity
Personal wellness
Show you targeted ads or personalized an-
nouncements
Show Ads
Analyze traveling experiences and public tran-
sit services
Analysis of Public tran-
sit services
Understand how people move in a city so as to
inform the design of new walking and cycling
infrastructure
Design new walk-
ing/cycling infrastruc-
ture
Understand your commute to work so as to
optimize work productivity
Optimize work produc-
tivity
Monitor your mobility patterns e.g., the places
you visit or the trips you make
Monitor mobility pat-
terns
Understand how people move so as to iden-
tify optimal locations for hospitals, libraries
or parks
Identify locations for
infrastructure
an obfuscated feature showing frequent trips with synthetic
trajectories generated with Google Maps (Fig. 23).
Third, prior work has shown that having prior technical
knowledge or specific demographic or personality traits might
affect privacy perceptions [11]. Hence, we also ask partici-
pants to fill out questions covering both privacy attitudes as
well as technical knowledge and demographic data. We broke
these questions into two blocks, demographic and general
tech knowledge questions were shown before the vignettes
and the privacy attitudes questionnaire after. This design was
based on user feedback from our qualitative survey evaluation,
as it appeared to provide breaks before and after the more
in-depth vignette questions. Following Martin et. al. [11],
the privacy attitudes questionnaire asked participants to rate
on a 5-Likert scale (from "strongly disagree" to "strongly
agree") their agreement with different privacy attitudes such
as trust in business or in government (see Figs.8 and 9 in
the Appendix for a detailed list of all the questions asked,
and section C.4 for further details on the rationale behind the
privacy questionnaire design).
3.2 Platform
We advertised our online survey on Cint6. Interested partici-
pants clicked on a link on Cint that took them to an institution
webpage where we hosted the survey. We did not use Cint sur-
veys directly because of the elaborate nature of the factorial
vignettes that were randomly sampled and of the custom map
visualizations we created, consistent with the survey question.
Each participant was paid $7 for completing the survey which
consisted of five vignette questions, seven demographic and
computer knowledge questions, 10 privacy attitude questions.
All participants were protected by IRB number 1768475-4 7.
We collected a U.S. representative sample of 1,405 partici-
pants (7,025 vignette questions answered), which produced
an average of 16 answers per vignette, on par with prior work
in privacy perceptions [11, 15].
4 Analytical Approach
As stated in the Introduction, the main objective of this paper
is to analyze user levels of comfort with respect to the use of
individual trajectory and POI visits taking into account the
actors and purposes involved in the data analysis, as well as
the presence (or not) of obfuscating approaches to preserve
privacy. In addition, we are also interested in evaluating how
these perceptions might change with respect the participants’
educational or racial background.
To carry out this analysis, we employ a mixed-effects ordi-
nal logistic regression (clmm in R) due to the ordinal nature
of the Likert responses (5-point Likert scale from ( very un-
comfortable) to (very comfortable)). We follow best practices
for the vignette data analysis using ordinal regressions [62].
We use participant ID (each participant given a random ID)
and vignette (vignette number) as two random effects. The
dependent variable in the mixed effects ordinal regression
is the level of comfort (five categories) and the independent
variables are the variables whose effect we want to evaluate:
actors, purposes, features (separating detailed features from
features computed using obfuscation approaches), education
and race and ethnicity. We also include the answers to the
privacy attitudes, demographic and technical knowledge ques-
tionnaires as control variables in the regression, given that
these have been associated with privacy comfort levels in
prior work ( [11]).
6https://www.cint.com/
7https://osf.io/x2vjk?view_only=e6dd3400991946afa3b265d
f5b1f3132
6

A coefficient analyses of the independent variables will
allow us to identify which variables are statistically significant
and thus have an effect on the level of comfort that users have
with different types of location data being shared. A detailed
description of the ordinal regression proposed is provided
in the Appendix, in section A, where we also show that that
assumptions for the ordinal regression are met (see Table 15
in Appendix).
In addition, we are also interested in evaluating the interac-
tion effects between independent variables. For example, the
ordinal regression might reveal a trajectory feature as having
a significant negative effect on the level of comfort; but we
are also interested in quantifying significant changes in levels
of comfort for that feature across different types of actors or
purposes. To run these analyses, we first transform the 5-point
Likert scale categorical answers into a numerical scale from
-2 to +2, with -2 being very uncomfortable, 0 being a neutral
privacy perception, and +2 being a very comfortable level of
comfort; and then run Kruskal-Wallis (KW) statistical tests
between the pairs of variables whose interactions we want
to evaluate (features and actors in our example); followed
by post-hoc Dunn tests with the Benjamini-Hochberg correc-
tion to identify statistically significant differences in comfort
levels across specific pairs (of features and actors in our ex-
ample). Further details for the KW and post-hoc Dunn tests
are provided in the Appendix, in section B. We do not run
the interaction effects analyses within the ordinal regression
because that would only allow us to explore relationships with
respect to specific regression baselines, instead of across all
feature values.
In the next section, we provide some general statistics about
the survey participants and the general distribution of levels
of comfort across features, actors, and purposes. Next, in the
following sections, we will discuss results for our three main
research questions: 1) RQ1: effect of individual trajectory and
POI visits on user levels of comfort, and their interactions with
actors and purposes, 2) RQ2: effect of obfuscating approaches
on user levels of comfort, and 3) RQ3: effect of educational
background and race and ethnicity on privacy perceptions.
5 Survey Response Analysis
We collected answers from 1,405 participants. Each partic-
ipant spent a mean of 18 min on the survey answering the
5 factorial vignette questions, as well as the demographic,
computer knowledge and privacy attitudes questionnaires.
From the 7,025 vignette questions answered, we removed an-
swers whose required free-form text-box explanations did not
clearly match the user comfort selected on the Likert scale,
including both lack of quality explanations or low quality
text. To achieve that, the answers were manually reviewed
by two researchers who agreed upon its quality. In addition,
we also removed answers with response times lower than 10
sec (given that the average adult reading speed is between
Table 4: U.S. census and survey population distribution across
four major races/ethnicities and education levels.
Education Under
High
School
High school
to Bache-
lors
Bachelors
and above
U.S. Cen-
sus
Race/Eth
White 6.2% 37.4% 24.5% 68.2%
Black 1.2% 7.2% 2.9% 11.3%
Asian 1.2% 2.0% 3.2% 5.7%
Hispanic 3.6% 8.4% 2.9% 14.9%
Census 12.1% 55.0% 33.5%
Education Under
High
school
High school
to Bache-
lors
Bachelors
and above
Survey Pop-
ulation
Race/Eth
White 3.60% 48.80% 21.40% 73.80%
Black 1.00% 8.80% 3.30% 13.10%
Asian 0.20% 2.80% 2.60% 5.60%
Hispanic 0.40% 5.50% 1.70% 7.60%
Survey 5.20% 65.90% 29.00%
100-1200 words/min [63] and the average vignette length is
43 words).
We aim for representative sampling (proportions similar
to U.S. Census from ACS [64]. Survey population and ACS
statistics are in Table 4.
Table 4 shows the demographic characteristics across all
survey participants for education levels as well as racial and
ethnic groups, which are the focus of our analysis. (Please
see Appendix for Age: Table 9 and Gender: Table 10). As
can be seen, the sample is approximately representative of the
U.S. population. The percentages for White and Black groups
are close to ACS estimates, while the values for Asian and
Hispanic are a bit lower. To account for this slight imbalance,
we apply weights to our ordinal regression analysis, giving
more importance to groups that are less represented (further
details are provided in the Appendix A).
Response Analyses. Figure 1 presents the distribution of
participants’ comfort levels for each location feature in our
study. Trajectory features, including detailed most frequent
trips, least frequent trips, most frequent walking trips, and
places visited, were frequently labeled as Uncomfortable or
Very Uncomfortable. In contrast, several obfuscated features
showed considerably higher levels of comfort when compared
to their detailed counterpart including frequent trips, frequent
walking activity, or work location, among others. These num-
bers reveal that efforts to obfuscate individual trajectory and
POI visit features are favorably seen by participants, increas-
ing their comfort with these types of analytical approaches.
Table 14 in the Appendix shows all mean comfort levels per
location feature when levels are transformed into a numeric
variable.
The privacy attitudes questionnaire at the end of the survey
asked participants to rate their agreement with different state-
ments related to trust in business or in government, or the role
7

Figure 1: Percentage of responses per feature type and level
of comfort (ordered left to right: Very uncomfortable, Uncom-
fortable, Neutral, Comfortable, Very comfortable).
of authority, among others. Interestingly, trust in institutions
and a general predisposition towards compliance appear to
increase comfort levels with sharing location data (detailed or
obfuscated), while skepticism towards authority is associated
with reduced willingness to share location information. De-
tailed results can be explored in the Appendix (see Table 11).
These results confirm the importance of adding participant
responses to privacy attitude questionnaires in the regression
model as control variables, since they appear to play a role in
the perception of privacy comfort.
The distribution of comfort levels for each purpose and
for each actor considered in the study confirmed prior work
[11, 65, 21, 15] (see Figure 2 and Table 12 in the Appendix
for detailed results). Participants more frequently responded
with "Very Uncomfortable" or "Uncomfortable" for purposes
related to optimizing work productivity and monitoring mobil-
ity patterns; while purposes with perceived societal benefits,
such as identifying locations for infrastructure development,
designing walking/cycling infrastructure, and analyzing pub-
lic transit services, were more frequently rated ascomfortable
or very comfortable. On the other hand, and also confirming
prior work, participants expressed greater discomfort shar-
ing data with Employers and Federal Government Agencies;
while actors such as Academic Researchers, Family, Emer-
gency Services, and Doctors were rated higher on the comfort
scale (see Figure 3 and Table 13 in the Appendix for further
details).
6 RQ1: Effect of Location Features, Actors
and Purposes on Privacy Perceptions
Table 5 shows the ordinal regression coefficients and odds ra-
tios across actors, purposes and location features. Statistically
significant coefficients reveal features that have a significant
effect on participants’ levels of comfort. The odds ratio in-
dicates the odds of that effect being more or less likely with
respect to the baseline, holding all other variables constant.
First, we analyze the effect of location features (individual
trajectory and POI visit data) on privacy perceptions, and
evaluate interaction effects between location features and
actors or purposes. Next, we describe our main findings for
actors and purposes, confirming significant insights found in
prior work.
6.1 Location Features
Table 5 shows that participants expressed statistically signifi-
cant lower levels of comfort when sharing detailed trajectory
data compared to detailed visits to POIs (regression baseline).
For example, the odds of being comfortable sharing Most Fre-
quent Trips (Detailed) was 0.74 times that of sharing detailed
visits to POIs. In other words, participants were significantly
less comfortable with the use of detailed trajectory data than
with the use of visits to specific types of POIs (restaurants,
libraries, schools, etc). As one participant stated: "There is no
good reason for them to monitor my trips on the regular at
all." (Participant-8a6a).
Participants, on the other hand, demonstrated higher com-
fort levels sharing obfuscated trajectory data compared to de-
tailed visits to POIs. For example, walking (Frequent Walking
Activity) was 1.5 times more likely to be rated as comfort-
able and international trips (International Visits) were 1.44
times more likely to be rated as comfortable than detailed
visits to specific points of interest. Finally, participants were
significantly more comfortable sharing their home and work
locations (obfuscated to the census tract) than sharing detailed
visits to specific POIs, although no significant difference was
observed when home and work locations were not obfuscated
(we discuss this further in RQ2). Interestingly, these results
reflect that if handled appropriately, users are willing to share
some of their trajectory data. As Participant-D303 shared,
"This is general information and I would be interested in this
as well".
Interactions with Actors and Purposes
Table 6 shows a subset of results for the Kruskal-Wallis
(KW) and Dunn tests between the levels of comfort for indi-
vidual trajectory data and POI visit features and the different
types of actors and purposes considered in our study (please
see Table 17 in the Appendix for full details). The results show
two interesting findings. First, the median level of comfort
sharing obfuscated trajectory data decreases depending on the
actor accessing the datwhile for researchers, family, or doctors
8

Table 5: Regression coefficients for Actors, Purposes, Features, Ethnicity and Education. Odds ratio column is the likelihood of
being more comfortable compared to the baseline class. Coefficients are only show for actor, purpose, feature, ethnicity and
education. Other control variables are shown in the Appendix Table 16
Coefficient Odds Ratio Std Err Statistic p-value
Actor (Baseline: Commercial Entity)
Federal government agency -0.249** 0.78 0.11 -2.266 0.023
Law enforcement agency 0.14 1.15 0.11 1.272 0.203
Local government agency 0.105 1.111 0.097 1.081 0.28
Academic researchers 0.539** 1.714 0.087 6.199 0
Emergency services 1.166** 3.209 0.185 6.297 0
Doctor 1.078** 2.939 0.169 6.393 0
Employer -0.626** 0.535 0.149 -4.205 0
Family 1.409** 4.092 0.166 8.493 0
Purpose (Baseline: Show ads)
Analysis of terrorist attacks 0.09 1.094 0.183 0.488 0.626
Analysis of Public transit services -0.047 0.954 0.185 -0.255 0.799
Control spread of diseases 0.138 1.148 0.188 0.731 0.465
Monitor mobility patterns -0.654** 0.52 0.178 -3.666 0
Personal wellness -0.338 0.713 0.212 -1.594 0.111
Analysis of criminal activity -0.075 0.928 0.179 -0.416 0.677
Design new walking/cycling infrastructure 0.583** 1.791 0.195 2.986 0.003
Identify locations for infrastructure 0.296 1.344 0.19 1.56 0.119
Optimize work productivity 0.152 1.164 0.224 0.679 0.497
Feature (Baseline: Places you Visit (Detailed))
International visits (Detailed) -0.061 0.941 0.209 -0.29 0.772
International visits (Obfuscated) 0.369* 1.446 0.21 1.753 0.08
Area you spent most of your time (Obfuscated) 0.012 1.012 0.148 0.081 0.936
Modes of transportation (Obfuscated) 0.192 1.212 0.144 1.327 0.185
Modes of transportation (Detailed) 0.01 1.01 0.149 0.066 0.948
Places you visit (Obfuscated) 0.166 1.181 0.139 1.191 0.234
Home location (Obfuscated) 0.441** 1.554 0.213 2.068 0.039
Home location (Detailed) -0.101 0.904 0.21 -0.48 0.631
Work location (Obfuscated) 0.376** 1.456 0.19 1.973 0.049
Work location (Detailed) -0.2 0.819 0.191 -1.043 0.297
Least frequent trips (Detailed) -0.198 0.82 0.153 -1.292 0.196
Most frequent trips between counties (Obfuscated) 0.168 1.183 0.148 1.134 0.257
Most frequent trips between counties (’Google’) (Obfuscated) 0.23 1.259 0.147 1.562 0.118
Most frequent trips (Detailed) -0.297** 0.743 0.146 -2.039 0.041
Most frequent type of trips (Detailed) -0.063 0.939 0.147 -0.431 0.667
Frequent walking activity (Detailed) -0.191 0.826 0.143 -1.335 0.182
Frequent walking activity (Obfuscated) 0.458** 1.581 0.145 3.166 0.002
Ethnicity/Race (Baseline: White)
Asian -0.017 0.983 0.233 -0.072 0.942
Black 0.221 1.247 0.162 1.361 0.174
Hispanic 0.504** 1.655 0.196 2.574 0.01
Education (Baseline: Highschool to Bachelors)
Bachelors and above -0.206 0.814 0.126 -1.631 0.103
Under Highschool -0.017 0.983 0.227 -0.075 0.94
Significance ** p − value < 0.05, * p − value < 0.1
9

Table 6: Kruskal-Wallis analysis with post-hoc Dunn test
results for a subset of pairs (full analysis in Table 17 in Ap-
pendix). M"i" represents median level of comfort value for
distribution "i". Significance at p-value <0.05)
Feature Actor1 Actor2 M1 M2 M2-M1
Freq
Walks(Ob)
Employer Researchers 0 1 1
Doc 0 1 1
Family 0 1 1
Freq
Walks(Ob)
Fed Researchers 0 1 1
Doc 0 1 1
Family 0 1 1
Freq
Walks(Ob)
Local gov Doc 0 1 1
Feature Purpose1 Purpose2 M1 M2 M2-M1
Visits(Ob) Monitor mo-
bility
Public transit 0 1 1
Infra
(Walk/Cycling)
0 1 1
the median level of comfort is "comfortable" (median=1, p-
value<0.05) for Federal Government agency or Employer ac-
tors the level of comfort is neutral (median=0, p-value<0.05)).
Second, the levels of comfort with respect to visits to POIs
(Places you visit (Ob)) has significantly higher median values
for purposes with social impact such as "Identifying loca-
tions for infrastructure or cycling" (median=1, p-value<0.05)
than for more generic purposes, such as "monitoring mobility
patterns" (median=0, p-value<0.05).
6.2 Actors and Purposes
Our ordinal regression results confirm prior findings for the
effect of actors and purposes on privacy perceptions [11, 15].
Table 5 shows that Federal Government Agencies and Em-
ployers were significantly negatively related to comfort when
accessing location data. In fact, participants had 0.78 and 0.53
times the odds (p<0.01) of rating their level of comfort lower
for these actors than for commercial entities (regression base-
line). On the other hand, Academic Researchers, Emergency
Services, Family members, and Doctors were positively re-
lated to levels of comfort, with participants having 1.7, 3.2, 4
and 2.9 times the odds (p<0.01) of rating their level of comfort
higher for these actors than for commercial entities (baseline).
Moving on to purposes, we observe that purposes with
social impact (e.g., Designing public infrastructure) were per-
ceived more favorably than marketing purposes (regression
baseline), with the odds ratio being 1.79 times higher. On the
other hand, more general purposes (e.g., Monitor mobility pat-
terns) were associated with significantly lower comfort levels
compared to the baseline, i.e. people were approximately half
as likely to be comfortable with sharing data (p-value<0.05).
Interaction Analysis. A Table with the Kruskal-Wallis
and Dunn test results for the interaction between actors and
location features can be found in Table 18 in the Appendix.
We would like to highlight a couple of significant findings.
First, while the effect of the actor being a Doctor is positive on
the level of comfort (as we showed in Table 5), the perception
is more positive when sharing walking activity (obfuscated)
(median level of comfort=1) than other features such as most
frequent type of trips (obfuscated) (median=0, neutral) or
most frequent trips (detailed) (median=-0.5, leaning uncom-
fortable). On the other hand, when the actor is an Employer,
giving access to the most frequent places of visit (obfuscated)
was perceived as more uncomfortable (median=-1, uncom-
fortable) than giving access to walking activity (obfuscated)
(median=0, neutral). Finally, no significant differences were
identified between purposes and location features, pointing
to similar levels of comfort independently of the trajectory or
POI visit feature.
7 RQ2: Effect of Obfuscating Approaches on
Privacy Perceptions
Looking into the Features column in Table 5 we can ob-
serve that some obfuscated trajectory and POI visit features
are associated with statistically significant higher levels of
comfort than detailed features (Places you visit (detailed) as
baseline). Specifically, obfuscated frequent walking activity
as well as obfuscated international trips, obfuscated home
and work locations had 1.58, 1.4, 1.55 and 1.45 times the
odds (p<0.05) of being rated higher in level of comfort than
detailed places visited, pointing to individuals being more
prone to sharing certain types of trajectory and visits data
if protected by obfuscation approaches. Beyond statistical
significance, it is important to highlight that when looking
into mean levels of comfort for each detailed and obfuscated
location feature, all means were higher for obfuscation fea-
tures than for their detailed counterpart e.g., Home (Detailed -
Obfuscated) = 0.055, Modes of Transport (Detailed - Obfus-
cated) = 0.045. In other words, although not significant in the
regression model, obfuscated location features are associated
with more positive levels of comfort towards data sharing.
Table 14 in the Appendix shows all mean levels of comfort
across location features.
Interaction Analysis. We perform KW and post-hoc Dunn
tests between the levels of comfort associated with "Detailed"
location features and "Obfuscated" location features across
types of actors and purposes. Detailed results are shown in the
Appendix Table 19. Here, we discuss two relevant findings.
First, we observe that when the actor accessing the location
feature is a family member (actor=Family), the user level of
comfort increases from neutral to comfortable if the location
feature is obfuscated instead of detailed. Similarly, we found
that obfuscated features improved the privacy level of comfort
when compared to detailed features for certain purposes such
as "control the spread of diseases". This finding aligns with
studies that show privacy preserving location sharing apps
10

during COVID were perceived more positively compared to
detailed location sharing app [38, 42, 39].
8 RQ3: Effect of Race/Ethnicity and Educa-
tion on Privacy Perceptions
8.1 Race and Ethnicity
The results in Table 5 show that Hispanic participants are as-
sociated with statistically significant higher levels of comfort
that White participants (regression baseline), having 1.6 times
the odds (OR=1.6, p<0.01) of rating their level of comfort
with location data higher than White participants. Some of
the free-form text boxes align with these observations. For
example, participants who self-identified as Hispanic said: "I
have nothing to hide so it doesn’t really make a difference to
me." (Participant-050e); and "(In) this particular scenario I
feel very comfortable with my data being accessed & used
for this purpose. Hospital locations are important and their
location within a community can severely impact the quality
of life for that community too." (Participant-2ae1). On the
other hand, no significant difference in level of comfort was
observed between any other racial or ethnic groups.
Interaction analysis. The KW and Dunn statistical tests
between the levels of comfort across race/ethnicity and loca-
tion data types, actor types and purposes revealed interesting
nuanced privacy perceptions. Detailed results can be found
in Tables ?? in the Appendix. Here, we discuss the most
relevant findings. For Hispanic individuals, the levels of com-
fort were the lowest when their location data was used for
marketing purposes i.e. showing ads (median=-1 "uncomfort-
able, p-value<0.05). In contrast, Black participants perceived
marketing purposes as positive (median=1 "comfortable", p-
value< 0.05) when compared to other purposes like analysis
of terrorist attacks (median=0), public transit (median=0), mo-
bility monitoring (median=0).
Nevertheless, no significant differences were observed be-
tween Hispanic ethnicity and actor or feature types; neither
between Black and actors or feature types. This might indi-
cate that, for Hispanic and Black participants, data comfort
revolves around purpose of data access, and not around who
access the data (actor) or the specific type of data accessed
(feature).
On the other hand, for Asian and White respondents there
was a significant change in level of comfort between detailed
and obfuscated features with, for example, "Most frequent
trips (Detailed)" having a lower median comfort (median=0,
p-value<0.05) than "Frequent walking activity (Obfuscated)"
(median=1) for White individuals. In addition, the tests also
showed Asian and White respondents being significantly less
comfortable with the Federal Government, Law enforcement,
Local government (median=0) and Employers (median=-1)
than with Researchers, Family, Doctors or Emergency services
(median=1). White participants were also more comfortable
in sharing data for infrastructure purposes (designing cycling
infrastructure and designing built infrastructure) (median=1,
p-value<0.05) than for all the other purposes (median=0).
Thus, for Asian and White participants we find evidence that
the combinations of actors, purposes and features are respon-
sible for the overall privacy perception.
8.2 Education
We do not observe any statistically significant difference in
comfort levels for different education groups when compared
to participants with education high school to bachelors (base-
line).
Interaction analysis. Kruskal-Wallis and post-hoc Dunn
tests to assess interactions between levels of comfort across
education levels and actors, purposes and location features
revealed some interesting insights (see Table 22 in the Ap-
pendix for full details). Participants with a "Bachelors and
above" felt more comfortable in sharing obfuscated features
(median=1,pval<0.05) compared to detailed (median=0, p-
value<0.05).
Interestingly, no statistical difference between detailed and
obfuscated location data was observed for the other two ed-
ucational groups "High School to Bachelors" and "Under
High School". Participants with a "Bachelors and above" also
showed significantly lower levels of comfort with purposes
related to monitoring mobility (median=0, p-value<0.05) and
with sharing location data with employers (median=-1, p-
value<0.05). These findings indicate that decisions of this
educational group depend on the interaction of the full spec-
trum of actor-purpose-feature (along with privacy attitudes).
Participants with education "High School to Bachelors"
were significantly less comfortable in sharing their location
data with the Federal Government, law enforcement agen-
cies (median=0, p-value<0.05) or employers (median=-1,p-
value<0.05) than with Researchers and Emergency services
(median= 1,pval<0.05). These results reveal that the privacy
perceptions for this educational group are mostly shaped
around actors and purposes, and not types of features or obfus-
cation techniques. Finally, we did not observe any significant
difference between pairs of actors, purposes or features for
participants with "Under High School" education, signaing
that for these participants their decisions might be mostly
shaped by their individual privacy attitudes.
9 Predictive Modeling
This section explores the creation of models that predict levels
of comfort in sharing location data a given a combination of
actor, purpose and location feature. Such models can help
companies evaluate levels of comfort with different types
of location features before they are actually implemented
and deployed in their location intelligence platforms. For
example, a company could be interested in evaluating the level
11

of comfort of a Hispanic person in sharing their movement
data with law enforcement for public safety.
9.1 Model
We frame the prediction task as a classification task with the
classes being the levels of comfort. We explore two types of
models. In Model 1, our objective is to predict the level of
comfort of a given demographic group with a given vignette
(framed as actor, location feature, factor). This model would
allow a company to evaluate the level of comfort with the
use of a location feature associated with a specific population
group. We also evaluate a second modelModel 2, whereby pri-
vacy attitudes from the population of interest are also known,
either because the company knows them, or because they
can run a privacy attitudes survey among their population of
interest.
We consider three different approaches to defining the
classes in the classification task: 1) 5-point Likert scale (as
used in the original survey), 2) 3-point Likert scale ((very)
uncomfortable, neutral and (very)comfortable), and 3) Binary
classification ((very) uncomfortable or neutral vs. (very) com-
fortable). We perform an 80% train 20%test split for training
and model evaluation, and compare the performance of these
machine learning algorithms (suitable for classification tasks):
Random Forest (RF), Gradient Boosting Machines (XGB)
and K-Nearest Neighbours (KNN). To assess model perfor-
mance, we utilize the following metrics: Accuracy, Precision,
Recall, F1-score and Cohen’s Kappa.
9.2 Performance Analysis
Model 1. Table 7 presents the performance metrics for pre-
dicting comfort levels given a tuple of actor, purpose and
feature as well as general demographic information of the
population of interest to the company. We can observe mod-
erate accuracy and F1 scores across models and number of
classes with ranges (0.299-0.695) and (0.279-0.325), respec-
tively. As expected, higher number of classes are associated
with lower accuracy values. Nevertheless, the F1 scores are
the lowest for the binary classification pointing to challenges
in balancing precision and recall, possibly due to class imbal-
ance. The moderate performance across all models suggests
that vignette and demographic information alone may not be
sufficient for highly accurate predictions of comfort levels in
location data sharing. This underscores the complexity of pri-
vacy perceptions and the potential influence of other factors
not captured in demographic data such as privacy attitudes.
Model 2. Here, we examine the predictive performance of
Model 1 enhanced with privacy attitude data from the popu-
lation of interest. As Table 8 shows, adding privacy attitudes
as independent variables in the prediction model consistently
improves prediction performance across all metrics: accuracy,
precision, recall, and Cohen-Kappa; with improvements over
Table 7: Detailed classification report for the three labeling
approaches. Dependent variables: Actor, purpose, feature, de-
mographic attributes Best metric per classification approach
are in bold. XGB: XGBoost, KNN: K-nearest Neighbours,
RF: RandomForest, CK: Cohen Kappa score
Model Class Acc. Prec. Rec. F1 CK
XGB 2 0.695 0.155 0.455 0.232 0.095
KNN 2 0.647 0.219 0.349 0.269 0.052
RF 2 0.658 0.223 0.372 0.279 0.073
XGB 3 0.481 0.587 0.481 0.521 0.118
KNN 3 0.478 0.605 0.478 0.527 0.106
RF 3 0.459 0.530 0.459 0.486 0.096
XGB 5 0.299 0.385 0.299 0.325 0.060
KNN 5 0.287 0.380 0.287 0.318 0.042
RF 5 0.293 0.351 0.293 0.313 0.060
Table 8: Detailed classification report for the three labeling
approaches. Dependent variable: Actor, purpose, feature, de-
mographic attributes, privacy attitudes and trust. Best metric
per classification approach are in bold. XGB: XGBoost, KNN:
K-nearest Neighbours, RF: RandomForest, CK: Cohen Kappa
score
Model Classes Acc. Prec. Rec. F1 CK
XGB 2 0.772 0.522 0.642 0.576 0.422
KNN 2 0.780 0.522 0.665 0.585 0.439
RF 2 0.783 0.549 0.661 0.600 0.452
XGB 3 0.621 0.649 0.621 0.632 0.386
KNN 3 0.593 0.588 0.593 0.589 0.364
RF 3 0.642 0.647 0.642 0.644 0.433
XGB 5 0.476 0.486 0.476 0.478 0.318
KNN 5 0.464 0.462 0.464 0.462 0.314
RF 5 0.517 0.520 0.517 0.517 0.375
50% for 3-point and 5-point Likert scales when compared to
Model 1. Accuracy and F1 score values for Model 2 were in
the ranges (0.517,0.783) and (0.517,0.600), respectively. The
best performing model was the Random Forest which showed
superior performance across all classification settings (binary
and multi-class).
10 Implications for Policy and Practice
Location Features. Our regression analyses demonstrate that
participants have higher levels of comfort in sharing detailed
visits to POIs than detailed trajectory data. However, obfuscat-
ing some of the trajectory variables resulted in higher levels
of comfort even above sharing detailed visits to POIs. Our
analyses also showed that these levels of comfort are also
increased when the actors accessing the data are researchers
or family, or when the purpose is focused on social good.
These findings point to the implementation of more granular
control mechanisms that allow users to specify which types
12

of location features can be derived from the data collected
from them. Since data brokers and data aggregators collect
data from apps via SDKs, they could also allow users to se-
lect, during the app installation and when they are notified
about the location data collection, which one of the six feature
clusters shown in Table 1 they would be comfortable shar-
ing their location data for. Users should also have an opt-out
mechanism for which type of actor and purpose their data can
be used for. While arguing against the purchase of location
data from data brokers by government agencies, legal scholars
and practitioners like Rahbar [66] and Conner 8, have raised
serious concerns about such purchases violating the fourth
amendment.
Obfuscation Approaches. Higher levels of comfort were
clearly observed for some obfuscated location features (both
trajectory and visits to POIs) when compared to detailed visits
to POIs (baseline) in the regression model 5. These levels of
comfort were increased when the actor accessing the data was
a family member. Although not all obfuscated approaches
were significantly associated with higher levels of comfort
in the regression, the mean values were lower. We posit that
maybe there is no need for more granular control over ob-
fuscated vs. detailed features. By default, the features could
be obfuscated, and during the app installation users could
be offered to opt-in to share more detailed features, together
with an explanation of why this would be valuable for ana-
lytical purposes (actor, purpose). In future research, we will
also explore why obfuscation techniques appear to not always
alleviate privacy concerns.
Race, Ethnicity and Education Effects. Our regression
analysis has revealed significant differences in comfort lev-
els for the Hispanic participants when compared to White
participants, with Hispanic participants being more comfort-
able sharing trajectory and visit data. Our interaction analysis
has also shown a complex interplay between cultural fac-
tors, educational experiences, and privacy perceptions while
controlling for privacy attitudes and computer knowledge.
Hispanic and Black participants as well as "High School to
Bachelors" appear to shape their perceptions mostly on the
purpose of the data access, or on who has access to the data
(actor). On the other hand, White participants and participants
with educational level "Bachelors and above" appear to shape
their privacy perceptions around actors, purposes and by the
types of location data being shared. These findings could be
used to pre-populate some of the initial app selections for
types of location data, actors or purposes based, for example,
on the educational background of the person installing the
app, thus reducing the burden of having to select among many
different options from scratch.
8https://www.lawfaremedia.org/article/data-broker-sales
-and-the-fourth-amendment
11 Conclusion
This study contributes to our understanding of the nuanced
nature of privacy perceptions in location data sharing. By
highlighting the importance of the type of location feature
(trajectory or visits to POIs), the presence of an obfuscation
approach, contextual factors such as actors and purpose, at-
titudes and demographic variations, our findings provide a
foundation for more user-centric, feature focused approach
to location privacy. Our results have shown that trajectory-
related features are associated with higher privacy concerns;
that current obfuscation approaches by location data brokers
and aggregators are sometimes successful; and that race, eth-
nicity and education have an effect on privacy perceptions
with Hispanic and High School to Bachelor populations being
associated with higher levels of comfort. As technology con-
tinues to evolve, ongoing research in this area will be crucial
for developing privacy practices and policies that effectively
balance the benefits of location-based services with individual
privacy rights.
12 Ethical considerations
This study was evaluated and approved as a human subject re-
search by the Internal Review Board of the authors’ university.
Prior to starting the survey, participants were provided a link
to the Internal Review Board document detailing: the purpose
of the study, the different procedures, any potential risks or dis-
comforts that could occur during the study, potential benefits
and compensation value and the mechanism of compensa-
tion delivery. We offered an incentive of $7 per participant
to complete our survey. The compensation was disbursed by
Cint. Participants were also provided with an email and phone
number to raise any concerns, or complaints related to the
study. We did not receive any concerns or complains from
the participants and there were no research-related injuries
reported.
The survey data collected was analyzed in an anonymous
way. The names and emails of the participants were separated
from their responses and each participant was assigned a Uni-
versally Unique Identifier (UUID) (which was generated ran-
domly during the survey). Names and emails of participants
were only used to justify incentive expenses (compensation
for participation) to our IRB board. When quoting participant
responses from the free-form text replies in the survey, we
identify each participant using the last 4 characters of their
UUID. None of the Personally Identifiable Information (PII)
will be made available publicly during or after the research is
concluded.
13

13 Compliance with Open science policy
Literature has shown that data visualizations are better at con-
veying detailed information to participants when conducting
perception surveys. To integrate interactive map visualiza-
tions in our survey, we developed a Flask app that we hosted
on a private server during the experiment. Participants were
recruited via Cint and then were taken to our server where the
survey data was collected and consolidated. The Flask app is
connected with a local database which has the questions and
corresponding visualizations that are randomized and shown
to participants. After the data collection, the analysis was
performed using python.
If required, we will be able to share: 1) Hosting: Flask
app code, maria-db database with questions and visualiza-
tions as HTML files; 2) Analysis Python code/R code (re-
gression analysis and Kruskal-Wallis test followed by Dunn
post-hoc test). To enhance the reproducibility and replicability
of our scientific findings, we can also share the anonymized
responses to our survey.
References
[1] Ruth F Hunter, Leandro Garcia, Thiago Herick de Sa,
Belen Zapata-Diomedi, Christopher Millett, James
Woodcock, Alex ’sandy’ Pentland, and Esteban Moro.
Effect of COVID-19 response policies on walking be-
havior in US cities. Nat. Commun., 12(1):3652, June
2021.
[2] Jinpeng Wang and Yujie Hu. Unraveling hurricane ian’s
impact: A multiscale analysis of mobility networks in
florida. Transportation Research Part D: Transport and
Environment, 136:104482, 2024.
[3] Qingqing Chen and Ate Poorthuis. Identifying home
locations in human mobility data: an open-source r
package for comparison and reproducibility. Interna-
tional Journal of Geographical Information Science ,
35(7):1425–1448, 2021.
[4] Katarzyna Siła-Nowicka, Jan Vandrol, Taylor Oshan,
Jed A. Long, Urška Demšar, and A. Stewart Fother-
ingham. Analysis of human mobility patterns from
gps trajectories and contextual information. Interna-
tional Journal of Geographical Information Science ,
30(5):881–906, 2016.
[5] FTC settles unprecedented case against geolocation data
broker — therecord.media. https://therecord.me
dia/ftc-settles-case-geolocation-data-bro
ker-xmode-outlogic. [Accessed 27-08-2024].
[6] Brennan Center. Closing the data broker loophole |
brennan center for justice, Jan 2024.
[7] Sara Morrison. This outed priest’s story is a warning for
everyone about the need for data privacy laws, Jul 2021.
[8] Joseph Cox. Data broker is selling location data of
people who visit abortion clinics, May 2022.
[9] Margarita Gamarra, Inés Meriño Fuentes, Juan Cal-
abria Sarmiento, Omar Gutierrez Acosta, Mauricio Bar-
rios Barrios, Nallig Leal, and Pedro Mario Wight-
man Rojas. Privacy perception in location-based ser-
vices for mobile devices in the university community of
the north coast of colombia. Ingenieria y Universidad,
23(1), Feb 2019.
[10] Sarah Gilbert, Katie Shilton, and Jessica Vitak. When
research is the context: Cross-platform user expecta-
tions for social media data reuse. Big Data & Society,
10(1):20539517231164108, 2023.
[11] Kirsten Martin and Helen Nissenbaum. What is it about
location? Berkeley technology law journal / Boalt Hall
School of Law, University of California, Berkeley , 12
2019.
[12] SafeGraph. Places data curated for accurate geospatial
analytics, 2025.
[13] Device Recurring Areas and Sensitive Locations - Spec-
tus Documentation Portal — docs.spectus.ai. https:
//docs.spectus.ai/Getting%20Started/User_G
uides/Data_Assets/Device_Recurring_Areas
_and_Sensitive_Locations/#how-we-expose-t
he-devices-recurring-areas . [Accessed 05-02-
2025].
[14] Vincent Primault, Antoine Boutet, Sonia Ben Mokhtar,
and Lionel Brunie. The long road to computational loca-
tion privacy: A survey. IEEE Communications Surveys
& Tutorials, 21(3):2772–2793, 2019.
[15] Jessica Vitak, Yuting Liao, Anouk Mols, Daniel Trottier,
Michael Zimmer, Priya C. Kumar, and Jason Pridmore.
When do data collection and use become a matter of
concern? a cross-cultural comparison of u. 2022.
[16] Helen Nissenbaum. Privacy as contextual integrity.
Wash. L. Rev., 79:119, 2004.
[17] FTC’s Khan warns tech industry that agency will strictly
enforce AI data privacy — therecord.media. https:
//therecord.media/ftc-warns-tech-industr
y-ai-data-privacy . [Accessed 27-08-2024].
[18] Fused Location Provider API | Google for Developers
— developers.google.com. https://developers.goo
gle.com/location-context/fused-location-p
rovider. [Accessed 02-09-2024].
14

[19] Cclocationmanager | apple developer documentation.
https://developer.apple.com/documentatio
n/corelocation/cllocationmanager . [Accessed
02-09-2024].
[20] Sara Morrison. The hidden trackers in your phone,
explained, Jul 2020.
[21] Alex Akinbi, Mark Forshaw, and Victoria Blinkhorn.
Contact tracing apps for the covid-19 pandemic: a sys-
tematic literature review of challenges and future di-
rections for neo-liberal societies. Health Information
Science and Systems, 9(1), Apr 2021.
[22] Lingzi Hong, Enrique Frias-Martinez, and Vanessa Frias-
Martinez. Topic models to infer socio-economic maps.
In Proceedings of the AAAI Conference on Artificial
Intelligence, volume 30, 2016.
[23] Yanni Yang, Alex Pentland, and Esteban Moro. Identi-
fying latent activity behaviors and lifestyles using mo-
bility data to describe urban dynamics. EPJ Data Sci.,
12(1):15, May 2023.
[24] Bernardo Garcia-Bulle, Abigail L. Horn, Brooke M.
Bell, Mohsen Bahrami, Burcin Bozkaya, Alex Pentland,
Kayla de la Haye, and Esteban Moro. You are where
you eat: Effect of mobile food environments on fast food
visits. medRxiv, 2022.
[25] Timothy Fraser, Takahiro Yabe, Daniel P. Aldrich, and
Esteban Moro. The great equalizer? mixed effects of so-
cial infrastructure on diverse encounters in cities. Com-
puters, Environment and Urban Systems, 113:102173,
2024.
[26] Christine Bauer and Christine Strauss. Location-based
advertising on mobile devices. Management Review
Quarterly, 66(3):159–194, Jan 2016.
[27] Lingzi Hong, Jiahui Wu, Enrique Frias-Martinez, An-
drés Villarreal, and Vanessa Frias-Martinez. Charac-
terization of internal migrant behavior in the immedi-
ate post-migration period using cell phone traces. In
Proceedings of the tenth international conference on
information and communication technologies and devel-
opment, pages 1–12, 2019.
[28] Xiaolei Ma and Yinhai Wang. Development of a data-
driven platform for transit performance measures using
smart card and gps data. Journal of Transportation
Engineering, 140(12):04014063, 2014.
[29] Jiahui Wu, Saad Mohammad Abrar, Naman Awasthi,
Enrique Frias-Martinez, and Vanessa Frias-Martinez.
Enhancing short-term crime prediction with human mo-
bility flows and deep learning architectures. EPJ data
science, 11(1):53, 2022.
[30] Roland Billen, Elsa Joao, and David Forrest, editors.
Dynamic and mobile GIS . Innovations in GIS. CRC
Press, Boca Raton, FL, November 2006.
[31] Jessica Vitak and Michael Zimmer. Surveillance and
the future of work: exploring employees’ attitudes to-
ward monitoring in a post-covid workplace. J. Comput.
Mediat. Commun., 28, 2023.
[32] A Gorra. An analysis of the relationship between indi-
viduals? perceptions of privacy and mobile phone loca-
tion data - a grounded theory study. April 2007.
[33] Emily Fekete Matthew Haffner, Adam J. Mathews and
G. Allen Finchum. Location-based social media behav-
ior and perception: Views of university students. Geo-
graphical Review, 108(2):203–224, 2018.
[34] Rajarshi Chakraborty, Claire Vishik, and H. Raghav Rao.
Privacy preserving actions of older adults on social me-
dia: Exploring the behavior of opting out of information
sharing. Decision Support Systems, 55(4):948–956, Nov
2013.
[35] Iris Junglas and Christiane Spitzmuller. Personality
traits and privacy perceptions: An empirical study in the
context of location-based services. In2006 International
Conference on Mobile Business, pages 36–36, 2006.
[36] Gaurav Bansal, Fatemeh Mariam Zahedi, and David
Gefen. Do context and personality matter? trust and pri-
vacy concerns in disclosing private information online.
Information & Management, 53(1):1–21, 2016.
[37] Edward Shih-Tse Wang and Ruenn-Lien Lin. Perceived
quality factors of location-based apps on trust, perceived
privacy risk, and continuous usage intention. Behaviour
& Information Technology, 36(1):2–10, 2017.
[38] Baobao Zhang, Sarah Kreps, Nina McMurry, and
R Miles McCain. Americans’ perceptions of privacy
and surveillance in the covid-19 pandemic. Plos one,
15(12):e0242652, 2020.
[39] Athina Ioannou and Iis Tussyadiah. Privacy and surveil-
lance attitudes during health crises: Acceptance of
surveillance and privacy protection behaviours. Tech-
nology in Society, 67:101774, 2021.
[40] Andrew Tzer-Yeu Chen, Morteza Biglari-Abhari, and
Kevin I-Kai Wang. Context is king: Privacy perceptions
of camera-based surveillance. In 2018 15th IEEE In-
ternational Conference on Advanced Video and Signal
Based Surveillance (AVSS), pages 1–6, 2018.
[41] Oliver T. Kurtz, Bernd W. Wirtz, and Paul F. Langer.
An empirical analysis of location-based mobile adver-
tising—determinants, success factors, and moderating
15

effects. Journal of Interactive Marketing, 54(1):69–85,
2021.
[42] Junghwan Kim and Mei-Po Kwan. An examination of
people’s privacy concerns, perceptions of social benefits,
and acceptance of covid-19 mitigation measures that
harness location information: A comparative study of
the us and south korea. ISPRS International Journal of
Geo-Information, 10(1):25, 2021.
[43] Carlos Ochoa Gómez. Willingness to partici-
pate in geolocation-based research. PLOS ONE ,
17(12):e0278416, Dec 2022.
[44] Florian Keusch, Bella Struminskaya, Christopher An-
toun, Mick P Couper, and Frauke Kreuter. Willingness
to Participate in Passive Mobile Data Collection. Public
Opinion Quarterly, 83(S1):210–235, 06 2019.
[45] Michael Benisch, Patrick Gage Kelley, Norman Sadeh,
and Lorrie Faith Cranor. Capturing location-privacy
preferences: quantifying accuracy and user-burden trade-
offs. Personal Ubiquitous Comput., 15(7):679–694, Oc-
tober 2011.
[46] Vanessa Bracamonte, Sebastian Pape, and Sascha Loeb-
ner. “all apps do this”: Comparing privacy concerns
towards privacy tools and non-privacy tools for social
media content. Proceedings on Privacy Enhancing Tech-
nologies, 2022(3):57–78, Jul 2022.
[47] Nina Gerber, Benjamin Reinheimer, and Melanie V olka-
mer. Investigating people’s privacy risk percep-
tion. Proceedings on Privacy Enhancing Technologies,
2019(3):267–288, Jul 2019.
[48] Yuchen Zhao, Juan Ye, and Tristan Henderson. Privacy-
aware location privacy preference recommendations. In
Proceedings of the 11th International Conference on
Mobile and Ubiquitous Systems: Computing, Network-
ing and Services, MOBIQUITOUS ’14, page 120–129,
Brussels, BEL, 2014. ICST (Institute for Computer Sci-
ences, Social-Informatics and Telecommunications En-
gineering).
[49] A. Alshehri and Fayez Alotaibi. Predicting users mo-
bile app privacy preferences. Journal of Computer and
Communications, 2019.
[50] Daniel Smullen, Yuanyuan Feng, Shikun Zhang, and
N. Sadeh. The best of both worlds: Mitigating trade-offs
between accuracy and user burden in capturing mobile
app privacy preferences. Proceedings on Privacy En-
hancing Technologies, 2020:195 – 215, 2020.
[51] Pardis Emami Naeini, Sruti Bhagavatula, Hana Habib,
Martin Degeling, Lujo Bauer, Lorrie Faith Cranor, and
Norman Sadeh. Privacy expectations and preferences
in an IoT world. In Thirteenth Symposium on Usable
Privacy and Security (SOUPS 2017) , pages 399–412,
Santa Clara, CA, July 2017. USENIX Association.
[52] Yaqing Yang, Tony W Li, and Haojian Jin. On the feasi-
bility of predicting users’ privacy concerns using con-
textual labels and personal preferences. In Proceedings
of the CHI Conference on Human Factors in Computing
Systems, CHI ’24, New York, NY , USA, 2024. Associa-
tion for Computing Machinery.
[53] Yanni Yang, Alex Pentland, and Esteban Moro. Identi-
fying latent activity behaviors and lifestyles using mo-
bility data to describe urban dynamics. EPJ Data Sci.,
12(1):15, May 2023.
[54] Natalie Coleman, Chenyue Liu, Yiqing Zhao, and Ali
Mostafavi. Lifestyle pattern analysis unveils recovery
trajectories of communities impacted by disasters. Hu-
manit. Soc. Sci. Commun., 10(1), November 2023.
[55] Thomas Adler, Vince Bernardin, J. Dumont, Leah Flake,
and Hadi Sadrsadat. The promise and limitations of lo-
cational app data for origin-destination analysis: A case
study. Technical Report FHWA-HEP-20-022, United
States. Federal Highway Administration, 10 2017.
[56] I-Ting Chuang, Lee Beattie, and Lei Feng. Analysing
the relationship between proximity to transit stations and
local living patterns: A study of human mobility within
a 15 min walking distance through mobile location data.
Urban Science, 7(4), 2023.
[57] Wenwen Li, Shaohua Wang, Xiaoyi Zhang, Qingren Jia,
and Yuanyuan Tian. Understanding intra-urban human
mobility through an exploratory spatiotemporal analysis
of bike-sharing trajectories. International Journal of
Geographical Information Science, 34(12):2451–2474,
2020.
[58] Jinsoo Kim, Jae Hun Kim, and Gunwoo Lee. Gps data-
based mobility mode inference model using long-term
recurrent convolutional networks. Transportation Re-
search Part C: Emerging Technologies , 135:103523,
2022.
[59] I-Ting Chuang and Qingqing Chen. Urban street
dynamics: Assessing the relationship of sidewalk
width and pedestrian activity in auckland, new zealand,
based on mobile phone data. Urban Studies ,
0(0):00420980241293659, 0.
[60] Cuebiq Marketing Team. Come Back Soon! Measuring
the Effectiveness of Tourism Campaigns with — cue-
biq.com. https://cuebiq.com/come-back-soon-t
ourism/. [Accessed 06-02-2025].
16

[61] Florian M. Farke, David G. Balash, Maximilian Golla,
Markus Dürmuth, and Adam J. Aviv. Are privacy dash-
boards good for end users? evaluating user perceptions
and reactions to google’s my activity. In 30th USENIX
Security Symposium (USENIX Security 21), pages 483–
500. USENIX Association, August 2021.
[62] Thom Baguley, Grace Dunham, and Oonagh Steer. Sta-
tistical modelling of vignette data in psychology.British
Journal of Psychology, 113(4):1143–1163, 2022.
[63] Silvia Primativo, Donatella Spinelli, Pierluigi Zoccolotti,
Maria De Luca, and Marialuisa Martelli. Perceptual and
cognitive factors imposing “speed limits” on reading
rate: A study with the rapid serial visual presentation.
PLoS One, 11(4):e0153786, April 2016.
[64] U.S. Census Bureau. Age and sex. American Com-
munity Survey 5-Year Estimates Subject Tables, Table
S0101, 2022. Available at: https://data.census.go
v/table/ACSST1Y2023.S1501?q=education%20at
tainment.
[65] Noah Apthorpe, Yan Shvartzshnaider, Arunesh Mathur,
Dillon Reisman, and Nick Feamster. Discovering smart
home internet of things privacy norms using contextual
integrity. Proc. ACM Interact. Mob. Wearable Ubiqui-
tous Technol., 2(2), jul 2018.
[66] Dori H Rahbar. How the government’s purchase of
commercial location data violates carpenter and evades
the fourth amendment. Columbia Law Rev., 122(3):713–
754, 2022.
[67] Naresh K Malhotra, Sung S Kim, and James Agarwal.
Internet users’ information privacy concerns (IUIPC):
The construct, the scale, and a causal model. Inf. Syst.
Res., 15(4):336–355, December 2004.
Table 9: Age distribution in the U.S. and in our survey popu-
lation.
Age Census % Survey %
18-24 12% 8%
25-34 18% 22%
35-44 17% 19%
45-54 16% 17%
55-64 17% 19%
65+ 21% 14%
A Ordinal Regression
The survey measures comfort levels using a five-point ordi-
nal scale (very uncomfortable ≤ uncomfortable ≤ neutral
Table 10: Gender distribution for the U.S. Adult population
(age 18 and above) and in our survey population.
Gender U.S. Census Survey
Male 49% 46%
Female 51% 53%
Figure 2: Percentage of responses per actor and level of com-
fort (ordered left to right: Very uncomfortable, Uncomfortable,
Neutral, Comfortable, Very comfortable).
≤ comfortable ≤ very comfortable). Mixed effects Ordinal
regression was chosen over ordinal regression and multi-class
classification to account for the ordered nature of the de-
pendent variable. Ordinal regressions are preferred to linear
regressions because ordinal categories are not necessarily
evenly spaced (e.g., the difference between uncomfortable
and neutral may not equal the difference between neutral and
comfortable).
We used the following formula for the Mixed effects Ordi-
nal regression:
Ans ∼ 1 + Actor + Purpose + Feature+
Ethnicity + Education+
Privacy and Attitude questions+ +
(1|ID) + (1|apf) (1)
Assumption Testing. We test the assumptions for the
mixed effects ordinal regression model: proportionality odds
and multicollinearity using the nominal_test and scale_test
in R. None of the variables have p-value < 0.05 (thus no
significant evidence of non-proportional odds). We also com-
pute Variance Inflation Factor (VIF) and all the variables have
VIF < 2 which indicates no multicollinearity in the regression
setting.
Next, we also check goodness of fit and compare different
ordinal regression settings in Table 15. We find that the model
with best AIC is the one with two random intercepts ID and
vignette (actor-purpose-feature combination). ID is the UUID
17

Table 11: Percentage of responses for each privacy attitude question across levels of comfort.
Privacy Attitudes Comfort Level
Very Un-
comfort-
able
UncomfortableNeutral Comfortable Very Com-
fortable
I trust businesses
S. disagree 37.872 17.872 11.915 14.468 17.872
Disagree 23.62 27.964 19.548 19.91 8.959
Undecided 13.6 21.76 31.893 24.053 8.693
Agree 10.047 14.317 21.193 38.556 15.887
S. Agree 8.73 6.032 8.413 28.095 48.73
Privacy importance
S. disagree 22.857 15.714 7.143 15.714 38.571
Disagree 5 13 23 33 26
Undecided 3.939 6.364 32.424 36.97 20.303
Agree 7.173 16.14 24.522 39.103 13.06
S. Agree 19.218 20.025 20.328 23.733 16.696
Trust in government
S. disagree 32.898 24.408 17.551 17.061 8.082
Disagree 14.579 24.735 24.112 26.168 10.405
Undecided 11.299 15.71 29.124 30.937 12.931
Agree 6.205 13.179 20.872 39.744 20
S. Agree 5.882 6.723 13.277 32.605 41.513
Great that young
people are prepared to
defy authority
S. disagree 16.978 14.044 19.733 24.178 25.067
Disagree 13.048 18.974 22.735 34.644 10.598
Undecided 13.69 20.428 24.599 29.198 12.086
Agree 9.969 18.7 23.034 33.746 14.551
S. Agree 21.504 11.729 17.594 20.902 28.271
Discipline and
follow leader
S. disagree 32.048 18.554 19.036 19.036 11.325
Disagree 15.767 23.313 20.307 29.08 11.534
Undecided 13.023 18.43 29.07 28.314 11.163
Agree 7.795 16.256 23.128 37.026 15.795
S. Agree 9 9.444 14.444 29.889 37.222
Give benefit of doubt
S. disagree 40 17.6 16 11.2 15.2
Disagree 19.744 22.821 18.974 21.026 17.436
Undecided 17.253 17.582 28.352 28.462 8.352
Agree 12.637 19.264 22.969 32.755 12.375
S. Agree 11.756 12.258 17.993 26.953 31.039
18

Table 12: Actor and Comfortableness (Mean)
Actor Answer
Actor: Commercial Entity 0.162
Actor: Federal government agency -0.073
Actor: Law enforcement agency 0.081
Actor: Local government agency 0.189
Actor: Academic researchers 0.387
Actor: Emergency services 0.525
Actor: Doctor 0.256
Actor: Employer -0.424
Actor: Family 0.383
Table 13: Purpose and Comfortableness (Means)
Purpose Answer
Purpose: Analysis of terrorist attacks 0.126
Purpose: Analysis of Public transit services 0.276
Purpose: Control spread of diseases 0.233
Purpose: Monitor mobility patterns -0.022
Purpose: Personal wellness 0.157
Purpose: Show ads 0.185
Purpose: Analysis of criminal activity 0.147
Purpose: Design new walking/cycling in-
frastructure
0.425
Purpose: Identify locations for infrastruc-
ture
0.446
Purpose: Optimize work productivity -0.054
of an individual (as we ask multiple questions to the same
person). Actor-Purpose-Feature (1|apf) models the between
vignette heterogeneity as described in [62]. We analyze this
regression model in the paper.
Weights. We weigh the samples in the mixed effects or-
dinal regression model for representativity of education and
ethnicity. We calculate these weights by dividing % of ex-
pected population by our population e.g.,: 6.2% of adult white
population is educated and has a degree under high school.
Since we have 3.6% participants in that strata, we assign a
weight of 1.72 to each respondent.
B Kruskal Wallis and Dunn posthoc test
The Kruskal-Wallis test, a non-parametric method, is used to
identify statistically significant differences in medians across
multiple independent groups. We use the "survey" package
in R to factor for the random intercepts while calculating
the Kruskal-wallis statistic. While this test determines the
presence of differences, it does not specify which pairs differ.
Therefore, we conduct a post-hoc Dunn test to identify pairs
of groups with statistically significant median differences.
Table 14: Feature and Comfortableness (Means)
Feature Answer
Feature: International visits (Detailed) 0.286
Feature: International visits (Obfuscated) 0.247
Feature: Area you spent most
of your time (Obfuscated) 0.200
Feature: Modes of transportation (Obfus-
cated)
0.220
Feature: Modes of transportation (De-
tailed)
0.175
Feature: Places you visit (Detailed) 0.092
Feature: Places you visit (Obfuscated) 0.224
Feature: Home location (Obfuscated) 0.210
Feature: Home location (Detailed) 0.155
Feature: Work location (Obfuscated) 0.263
Feature: Work location (Detailed) 0.268
Feature: Least frequent trips (Detailed) 0.026
Feature: Most frequent trips between
counties (Obfuscated) 0.129
Feature: Most frequent trips between
counties(’Google’) (Obfuscated) 0.152
Feature: Most frequent trips (Detailed) -0.058
Feature: Most frequent type
of trips (Obfuscated) 0.145
Feature: Frequent walking activity (De-
tailed)
0.054
Feature: Frequent walking activity (Obfus-
cated)
0.356
This combined approach is employed throughout our statisti-
cal analysis to discern perception differences. We do not use
interaction effects in regression settings because in interac-
tions, the significant coefficients indicate odds ratio compared
to only the baseline interaction e.g., actor:education interac-
tions that are significant in the regression setting would only
be significantly higher/lower from the baseline (Commercial
Entity: Highschool to Bachelors). The comparisons for all
actors:education pairs cannot be established with a single re-
gression model. KW with Dunn can do pairwise comparisons
and post hoc corrections to reduce FDR (False Discovery
Rate).
We demonstrate the process using an example. Let us
assume we are interested in understanding significant dif-
ferences in comfort levels across actors and location fea-
tures. Participants were asked about their comfort levels in
sharing location data for different actors and features. Each
actor-feature combination (N=138) represents an independent
group, allowing for comparison using the Kruskal-Wallis test.
The test yielded an F statistic of [316.28] with p-value < 0.05,
indicating significant differences between the medians of
actor-feature pairs. Following the Kruskal-Wallis test, we em-
19

Figure 3: Percentage of responses per purpose and level (or-
dered left to right: Very uncomfortable, Uncomfortable, Neu-
tral, Comfortable, Very comfortable).
Table 15: ANOV A analysis of different models to select the
best model. CLM: Cumulative link model (Ordinal model),
CLMM (cumulative linked mixed model). Best models are
CLMMID and CLMMID_V IG with lowest AIC scores. Signifi-
cance "**" < 0.05
Model Description AIC
CLM a+p+f+privacy and attitudes 20218
CLMMintercept random intercepts only 19332
CLMMnoap f Random Intercept + privacy &
attitudes
18803**
CLMMID a+p+f+privacy and attitudes +
(1|ID)
18589**
CLMMID_V IG a+p+f+privacy and attitudes +
(1|ID)+ (1|apf)
18583**
ployed the Dunn post-hoc test with the Benjamini-Hochberg
(to reduce false discovery rate) correction for multiple compar-
isons. This post-hoc analysis produces an N x N matrix (where
N is the number of actor-feature combinations), with each
cell containing the adjusted p-value for the corresponding
pairwise comparison. For each actor, we tabulate only those
features whose median comfort levels were found to be sta-
tistically significantly different (pvalue < 0.05) by at least
1. By grouping the results by actors and analyzing the differ-
ent features per actor, we can understand how perceptions of
the same actor may vary when accessing different types of
location data. This analytical approach is applied throughout
the paper for various combinations, including actor-purpose,
purpose-feature, education-feature, and privacy-actor pairs,
to provide a comprehensive understanding of the factors in-
fluencing location data sharing comfort levels.
C Survey and User Interface
In this section, we discuss the survey in detail and the different
sections in it. We built a custom survey webpage for better
customization and functionality. Participants were shown ads
for our survey on the Cint portal and they were directed to
our survey page upon clicking on it.
The survey is divided into the following sections:
• Consent and Briefing
• Demographic Information and General Technical Knowl-
edge
• Understanding Level of comfort with location data shar-
ing: Vignettes
• Privacy Attitudes
C.1 Consent and Briefing
Figure 5 is the landing page of our survey. The landing page
opens with a pop-up window (see Figure 4) briefly describing
the objective of the study. The participants are also provided
with a link to the Internal Review Board’s (IRB) document
detailing the project, ethical considerations, data handling
and contact information. All participants are asked for their
name, email, whether they are 18 years or older, consent to
participate and whether they are voluntarily agreeing to par-
ticipate in the survey. If they press the "I do not consent"
button, they are directed away from the website. When the
participant presses on the "submit" button, the pop-up window
disappears and they can read the introduction page (Figure 5)
which details our study, the different sections and the number
of questions, asking participants to think about the data and
visualizations they see as their own. The participant moves to
the next section when they click on the "Next" button.
C.2 Demographic Information and General
Technical Knowledge
After reading the brief and moving to the next page, partici-
pants are asked about their demographic details and general
awareness with different technologies (see Figure 9).
C.3 Understanding Level of comfort with loca-
tion data sharing: Vignettes
There are 5 vignette questions asked to each participant. The
questions are generated randomly from a set of questions and
displayed on the participant’s browser. There are two types
of location features (Detailed vs Obfuscated). Fig. 6 shows
an example of a vignette focused on a detailed feature. In this
example, participants see a chart showing statistics about the
types of transportation inferred from location data as well as
an interactive map with the detailed trajectories for each mode
of transportation together with labels characterizing origin
and destination place. Participants can interact with the map
to understand better all the information being shared. On the
other hand, Figure 7 shows an example of a location feature
20

Figure 4: Popup showing the consent page and Internal Review Board (IRB) document link
Figure 5: The Introduction page
21

computed in a privacy-preserving way. The participant can
see general statistics about their walking activity and assess
their level of comfort by selecting one of the five options.
As can be observed, all vignettes also have a text box for
participants to explain the rationale behind their choice.
C.4 Privacy Attitudes
After completing the 5 vignette questions, participants are re-
quired to fill out the privacy attitudes survey, shown in Figure
8. Studies like [15, 51, 11, 9] have asked privacy and atti-
tude questions which try to understand the person’s general
attitudes towards data sharing and privacy. We include the
questions in Martin et. al. [11] as additional control variables
in our regression to understand how different attitudes relate to
comfort in sharing specific location features. These questions
indirectly measure control, awareness and collection aspects
as studied in Internet Users Information Privacy Concerns
(IUIPC) [67] based studies. As our goals are strictly under-
standing the broader horizon of location features and comfort,
we focus our attention to these questions rather than forming
the hierarchical IUIPC scores. We incorporate responses to
the questions as ordinal variables (see response categories
in 11 ). Table 16 highlights questions which were signifi-
cantly related to comfort levels. We observe similar trends
to [11] in these questions. People with positive attitudes to-
wards government and businesses show higher comfort levels.
While people with higher defiance to authority had inverse
relation with sharing location data. Two interesting findings:
(1) Positive relation between computer science knowledge
and comfort in sharing location data. (2) People who are
more aware of their privacy settings were less comfortable in
sharing location data.
22

Table 16: Additional control variables used in the regression setting which were significant (** pvalue<0.05). L :Linear, C :
Cubic, Q: Quadratic.
Coefficients Odds Ratio Std Err Statistic p val
Privacy.importance.L -1.301** 0.272 0.385 -3.382 0.001
Privacy.importance.Q -0.246 0.782 0.353 -0.697 0.486
Privacy.importance.C 0.141 1.151 0.336 0.42 0.675
Privacy.importance^4 -0.048 0.953 0.285 -0.168 0.867
Trust.in.government.L 1.398** 4.047 0.189 7.386 0
Trust.in.government.Q -0.172 0.842 0.158 -1.087 0.277
Trust.in.government.C 0.134 1.143 0.122 1.105 0.269
Trust.in.government^4 -0.064 0.938 0.109 -0.588 0.557
Great.that.young.people.are.prepared.to.defy.authority.L -0.425** 0.654 0.161 -2.641 0.008
Great.that.young.people.are.prepared.to.defy.authority.Q 0.143 1.154 0.149 0.955 0.339
Great.that.young.people.are.prepared.to.defy.authority.C -0.38** 0.684 0.119 -3.191 0.001
Great.that.young.people.are.prepared.to.defy.authority^4 -0.033 0.968 0.108 -0.304 0.761
Discipline.and.follow.leader.L 0.753** 2.123 0.168 4.493 0
Discipline.and.follow.leader.Q 0.097 1.102 0.15 0.648 0.517
Discipline.and.follow.leader.C 0.26** 1.297 0.119 2.188 0.029
Discipline.and.follow.leader^4 -0.115 0.891 0.108 -1.058 0.29
Give.benefit.of.doubt.L 0.475 1.608 0.288 1.651 0.099
Give.benefit.of.doubt.Q 0.075 1.078 0.253 0.297 0.767
Give.benefit.of.doubt.C 0.433** 1.542 0.201 2.158 0.031
Give.benefit.of.doubt^4 -0.516** 0.597 0.165 -3.131 0.002
Avoid.mobile.apps.due.to.privacy.concern.L -0.783** 0.457 0.136 -5.777 0
Avoid.mobile.apps.due.to.privacy.concern.Q -0.085 0.919 0.097 -0.879 0.379
Uninstalled.app.for.collecting.data.L -0.159 0.853 0.133 -1.192 0.233
Uninstalled.app.for.collecting.data.Q 0.01 1.01 0.096 0.105 0.917
Computer.Science.or.Programming.Experience.L 0.558** 1.747 0.24 2.321 0.02
Computer.Science.or.Programming.Experience.Q 0.058 1.06 0.163 0.355 0.723
Computer.Science.or.Programming.Experience.C 0.042 1.043 0.114 0.367 0.714
Machine.Learning.Experience.L 0.019 1.019 0.289 0.067 0.947
Machine.Learning.Experience.Q 0.057 1.059 0.194 0.296 0.767
Machine.Learning.Experience.C -0.015 0.985 0.134 -0.114 0.909
Statistics.Experience.L 0.05 1.051 0.276 0.18 0.857
Statistics.Experience.Q -0.134 0.875 0.191 -0.7 0.484
Statistics.Experience.C -0.13 0.878 0.127 -1.022 0.307
Frequency.of.use.of.data.collection.tools.like.GMaps..Fitbit.L 0.321 1.379 0.167 1.926 0.054
Frequency.of.use.of.data.collection.tools.like.GMaps..Fitbit.Q 0.212 1.236 0.162 1.305 0.192
Frequency.of.use.of.data.collection.tools.like.GMaps..Fitbit.C -0.079 0.924 0.125 -0.627 0.531
Frequency.of.use.of.data.collection.tools.like.GMaps..Fitbit^4 -0.195 0.823 0.14 -1.393 0.163
Privacy.settings.awareness.L 0.461** 1.586 0.179 2.571 0.01
Privacy.settings.awareness.Q 0.076 1.079 0.156 0.484 0.628
Privacy.settings.awareness.C -0.019 0.981 0.117 -0.166 0.868
Privacy.settings.awareness^4 -0.133 0.875 0.12 -1.104 0.269
I.trust.businessess.L 1.159** 3.187 0.259 4.484 0
I.trust.businessess.Q 0.62** 1.859 0.222 2.791 0.005
I.trust.businessess.C 0.163 1.177 0.153 1.068 0.286
I.trust.businessess^4 0.085 1.089 0.115 0.741 0.459
23

Figure 6: Example of Vignette Question (Actor: Law enforcement agency- like city police department or a county sheriff’s office,
Purpose: Understand criminal activity, Feature: Places you visit). The feature is detailed and shows an interactive map with
information
24

Figure 7: Example of Vignette Question (Actor:Commercial entity, Purpose: Personal wellness and physical activity, Feature:
Walking activity). The feature is obfuscating and only shows general statistics
25

Figure 8: Privacy attitude questions as seen by the survey participants
26

Figure 9: Demographic and technical knowledge questions as seen by the survey participants
27

Table 17: KW with Dunn test to identify significantly dif-
ferent medians when different actors and purposes are in-
volved with the same feature. Median differences are statis-
tically different (pval <0.01) Kruskal-Wallis Chi-sq statis-
tic interaction(feature,actor)= 316.28 pval<0.01; interac-
tion(feature,purpose)= 236.13 pval<0.01;
Feature Actor1 Actor2 M1 M2 M2-M1
Radius(Ob) Employer Researchers -1 1 2
Commercial -1 0 1
911 -1 1 2
Family -1 1 2
Local gov -1 1 2
Radius(Ob) Fed 911 0 1 1
Freq
Walks(Ob)
Employer Researchers 0 1 1
Doc 0 1 1
Family 0 1 1
Freq
Walks(Ob)
Fed Researchers 0 1 1
Doc 0 1 1
Family 0 1 1
Freq
Walks(Ob)
Local gov Doc 0 1 1
Home(D) Commercial Local gov 0 1 1
Fed Local gov -0.5 1 1.5
Least
FreqT(D)
Employer Researchers -1 1 2
Commercial -1 0 1
911 -1 1 2
Transport- Employer Researchers 0 1 1
ation(Ob)
FreqT(D) Employer Researchers -1 0 1
911 -1 1 2
FreqT-
counties(Ob)
Employer Researchers -1 1 2
Commercial -1 0 1
911 -1 1 2
Law EA -1 0 1
Local gov -1 1 2
FreqT-
counties(Ob)
Fed Researchers -0.5 1 1.5
911 -0.5 1 1.5
Local gov -0.5 1 1.5
FreqTypeT(D) Employer Researchers -0.5 1 1.5
Visits(D) Employer Researchers -1 1 2
Commercial -1 0 1
Doc -1 1 2
911 -1 1 2
Visits(Ob) Employer Researchers -1 1 2
Commercial -1 0 1
Family -1 1 2
Law EA -1 0 1
Local gov -1 0 1
Feature Purpose1 Purpose2 M1 M2 M2-M1
Visits(Ob) Monitor mo-
bility
Public transit 0 1 1
Infra
(Walk/Cycling)
0 1 1
Table 18: KW with Dunn test to identify significantly dif-
ferent medians when different features are involved with an
actor. Median differences are statistically different (pvalue
<0.01). Kruskal wallis chi-sq interaction(feature,actor)=
316.28 pval<0.01
Actors Feature1 Feature2 M1 M2 M2-M1
Commercial FreqT(D) Freq Walks(Ob) 0 1 1
Doc Radius(Ob) Freq Walks(Ob) 0 1 1
Least
FreqT(D)
Freq Walks(Ob) 0 1 1
FreqT(D) Freq Walks(Ob) -0.5 1 1.5
FreqTypeT(D) Freq Walks(Ob) 0 1 1
Employer FreqT-
counties(Ob)
Freq Walks(Ob) -1 0 1
Fed FreqT-
counties(Ob)
International(D) -0.5 1 1.5
Local gov Freq Walks(D) Home(D) 0 1 1
Visits(D) Home(D) 0 1 1
Table 19: KW with Dunn test to identify significantly dif-
ferent medians when obfuscated features are used for dif-
ferent actors and purposes. Median differences are statis-
tically different (pval <0.01). Kruskal wallis chi-sq statis-
tic for interaction(actor,privacy) = 192.84 pval<0.01; in-
teraction(purpose,privacy) = 120.06 pval<0.01; interac-
tion(feature,privacy) = 37.26 pval<0.01
Component Feature Feature M1 M2 M1-M2
Family Obfuscated Detailed 1 0 1
Control dis-
eases
Obfuscated Detailed 1 0 1
Table 20: KW with Dunn test to identify significantly dif-
ferent medians for Actors when different ethnicity/race par-
ticipants are involved. Median differences are statistically
different (pvalue <0.01). Kruskal wallis chi-sq statistic for
interaction(actor,ethnicity) = 241.47 pval<0.01
Ethnicity Actor1 Actor2 M1 M2 M2-M1
Asian Employer Family -1 1 2
Fed Family 0 1 1
White Commercial Researchers 0 1 1
911 0 1 1
Employer Researchers -1 1 2
Commercial -1 0 1
Doc -1 0 1
911 -1 1 2
Family -1 0 1
Fed -1 0 1
Law EA -1 0 1
Local gov -1 0 1
Fed Researchers 0 1 1
911 0 1 1
Law EA Researchers 0 1 1
911 0 1 1
Local gov Researchers 0 1 1
911 0 1 1
28

Table 21: KW with Dunn test to identify significantly different
medians for ethnicity/racial group participants when different
purpose, feature and privacy groups are involved. Median dif-
ferences are statistically different (pvalue <0.01). Kruskal wal-
lis chi-sq statistic for interaction(purpose,ethnicity) = 187.67
pval<0.01; interaction(feature,ethnicity) = 132.08 pval<0.01;
interaction(privacy,ethnicity) = 68.63 pval<0.01
Ethnicity Feature1 Feature2 M1 M2 M2-M1
White FreqT(D) Freq Walks(Ob) 0 1 1
Feature Feature M1 M2 M2-M1
Asian Detailed Obfuscated 0 1 1
Purpose1 Purpose2 M1 M2 M2-M1
Asian Monitor mo-
bility
Infra (Buildings) 0 1 1
Black Public transit Ads 0 1 1
Terrorist
attacks
Ads 0 1 1
Monitor mo-
bility
Ads 0 1 1
Hispanic Public transit Infra
(Walk/Cycling)
0 1 1
Infra (Buildings) 0 1 1
Work 0 1 1
Ads Criminal activity -1 1 2
Terrorist attacks -1 1 2
Control diseases -1 1 2
Infra
(Walk/Cycling)
-1 1 2
Infra (Buildings) -1 1 2
Monitor mobil-
ity
-1 1 2
Work -1 1 2
Wellness -1 1 2
White Criminal activ-
ity
Infra
(Walk/Cycling)
0 1 1
Infra (Buildings) 0 1 1
Terrorist
attacks
Infra
(Walk/Cycling)
0 1 1
Infra (Buildings) 0 1 1
Control dis-
eases
Infra (Buildings) 0 1 1
Monitor mo-
bility
Infra
(Walk/Cycling)
0 1 1
Infra (Buildings) 0 1 1
Work Infra
(Walk/Cycling)
0 1 1
Infra (Buildings) 0 1 1
Wellness Infra
(Walk/Cycling)
0 1 1
Infra (Buildings) 0 1 1
Ads Infra (Buildings) 0 1 1
Table 22: Subsample of KW with Dunn test to identify sig-
nificantly different medians for actors, purposes and fea-
tures when different education groups are involved. Me-
dian differences are statistically different (pvalue <0.01).
Kruskal wallis chi-sq statistic for interaction(actor,education)
= 198.53 pval<0.01; interaction(purpose,education) = 121.38
pval<0.01; interaction(feature,education) = 86.08 pval<0.01;
interaction(privacy,education) = 31.44 pval<0.01
Education Actor1 Actor2 M1 M2 M2-M1
Bachelors
and above
Employer Researchers -1 1 2
Commercial -1 0 1
Doc -1 1 2
911 -1 1 2
Family -1 1 2
Fed -1 0 1
Law EA -1 1 2
Local gov -1 1 2
Highschool
to Bachelor
Employer Researchers -1 1 2
Commercial -1 0 1
Doc -1 0 1
911 -1 1 2
Family -1 0 1
Fed -1 0 1
Law EA -1 0 1
Local gov -1 0 1
Fed Researchers 0 1 1
911 0 1 1
Law EA Researchers 0 1 1
911 0 1 1
Local gov Researchers 0 1 1
911 0 1 1
Feature1 Feature2 M1 M2 M2-M1
Bachelors
and above
Least
FreqT(D)
Freq Walks(Ob) 0 1 1
FreqT(D) Freq Walks(Ob) 0 1 1
Highschool
to Bachelor
FreqT(D) Freq Walks(Ob) 0 1 1
Purpose1 Purpose2 M1 M2 M2-M1
Bachelors
and above
Monitor mo-
bility
Public transit 0 1 1
Criminal activity 0 1 1
Control diseases 0 1 1
Infra
(Walk/Cycling)
0 1 1
Infra (Buildings) 0 1 1
Work Infra
(Walk/Cycling)
0 1 1
Infra (Buildings) 0 1 1
Feature Feature M1 M2 M2-M1
Bachelors
and above
Detailed Obfuscated 0 1
29

Figure 10: Snapshot of interactive map with home Feature
(Home(D)) as visible to participants. It shows the exact
home location of the hypothetical data contributor using a pin
marker.
Figure 11: Snapshot of interactive map with home Feature
(Home(Ob)) as visible to participants. It shows the census
tract region the hypothetical data contributor lives in.
Figure 12: Snapshot of interactive map with Work location
feature (Work(D)) as visible to participants. It shows the exact
work location of the hypothetical data contributor using a pin
marker.
Figure 13: Snapshot of interactive map with Work feature
(Work(Ob)) as visible to participants. It shows the census
tract region where the hypothetical data contributor works at.
Figure 14: Snapshot of interactive map with most Places of
Visit (D) feature (Visits(D) as visible to participants. It shows
the specific places the hypothetical data contributor frequently
visits. The types of places are color coded (and consistent be-
tween the map and chart in Fig. 15) and labelled appropriately
Figure 15: Chart with Places of Visit (Ob) feature (Visits(Ob))
as visible to participants. The bar chart shows the different
places of interest our hypothetical data contributor visits and
the number of days such visits happen.
30

Figure 16: Snapshot of interactive map with most Geographi-
cal area you spend most time feature (Radius(Ob) as visible to
participants. The circle describes the region our hypothetical
data contributor stays in. The pin denotes the center of this
region
Figure 17: Snapshot of interactive map with transportation
Feature (Transportation(D)) as visible to participants. The
map displays different modes of transport (driving, walking,
etc) with different colors consistently between the map and
the chart in fig. 18. For our hypothetical data contributor, the
pins denote the start and end points and the line joining the
pins denote the most frequent route taken by that mode of
transport. E.g. Black pins and line segment denote the most
frequent walking trip. The label "Riverfront" indicates the
inferred type of trip
Figure 18: Chart with modes of transportation Feature (Trans-
portation(Ob)) as visible to participants. The bar chart shows
the different modes of transport our hypothetical data contrib-
utor takes and the number of hours spent in each mode.
Figure 19: Snapshot of interactive map with most frequent
trips feature (FreqT (D) as visible to participants. For our
hypothetical data contributor, the pins denote the start and
end points and the line joining the pins denote one of the most
frequent routes. E.g. red pins and line segment denote the
most frequent trip between home and work.
31

Figure 20: Snapshot of interactive map with Least Frequent
trips feature (LeastFreqT(D)) as visible to participants. For
our hypothetical data contributor, the pins denote the start and
end points and the line joining the pins denote one of the least
frequent routes. E.g. red pins and line segment denote the
least frequent trip between home and hospital.
Figure 21: Snapshot of interactive map with Most frequent
type of trips Feature (Freq-TypeT(Ob)) as visible to partici-
pants. For our hypothetical data contributor, the pins denote
the start and end points and the line joining the pins denote
one of types of frequent trips. E.g. First, the most frequent
trips are identified and labelled according to end points. Green
pins and line segment denote a frequent trip to school which
is between "home" and "school" and thus is a type of school
trip.
Figure 22: Snapshot of interactive map with Most frequent
trips represented by their origin and destination census tracts
and connected by a line Feature (FreqT-counties(Ob)) as vis-
ible to participants. We see that the home census tract and
work census tract are joined by a straight green line (most
frequent movement between these census tracts).
Figure 23: Snapshot of interactive map with Most frequent
trips represented by their origin and destination census tract
and connected by a synthetic route extracted from Google
Maps (FreqT-Google(Ob)) as visible to participants. The
home census tract centroid and work census tract centroid
are joined by a segment suggested by Google maps routes
API .
32

Figure 24: Snapshot of interactive map with Your walking
activity and corresponding routes feature (Freq Walks(D)) as
visible to participants. For our hypothetical data contributor,
the pins denote the start and end points and the line joining
the pins denote the most frequent walking path taken. E.g.
Red pins and line segment denote the most frequent walking
trip. The label "park" on both pins indicates the start and end
of the walk was in a park
Figure 25: Snapshot of the chart with Your walking activity
(Freq Walks(Ob)) as visible to participants. Chart indicates
frequency and duration of walks with no detailed trajectories
Figure 26: Snapshot of interactive map with International
visits feature (International(D)) as visible to participants. The
map highlights the different countries visited and the pins
indicate specific locations of visit with the duration of stay
Figure 27: Snapshot of interactive map with International
visits feature (International(P)) as visible to participants. It
specifies only the countries of visit and the duration of visit.
33
