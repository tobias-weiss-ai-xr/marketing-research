---
title: How to measure consumer's inconsistency in sensory testing?
url: https://arxiv.org/abs/2312.08141
category: consumer-behavior
subcategory: empirical
date: 2023-12
venue: ''
authors:
- László Sipos
- Kolos Csaba Ágoston
- Péter Biró
- Sándor Bozóki
- László Csató
source: arxiv
pdf_url: https://arxiv.org/pdf/2312.08141
pages: 26
chars: 45624
fetched_at: '2026-11-08T13:12:07+00:00'
kb_version: 1
---

# How to measure consumer's inconsistency in sensory testing?

How to measure consumer’s inconsistency in sensory
testing?
L´ aszl´ o Siposa,b,∗, Kolos Csaba ´Agostonc, P´ eter Bir´ ob,c, S´ andor Boz´ okid,c,
L´ aszl´ o Csat´ od,c
a Department of Postharvest, Commercial and Sensory Science, Institute of Food Science
and Technology, Hungarian University of Agriculture and Life Sciences, Budapest,
Hungary
b HUN-REN Institute of Economics, Centre for Economic and Regional Studies
(HUN-REN KRTK), Budapest, Hungary
c Department of Operations Research and Actuarial Sciences, Institute of Operations and
Decision Sciences, Corvinus University of Budapest, Hungary
d HUN-REN Institute for Computer Science and Control (HUN-REN SZTAKI),
Laboratory on Engineering and Management Intelligence, Research Group of Operations
Research and Decision Systems, Budapest, Hungary
Abstract
Standard methods, standard test conditions and the use of good sensory
practices are key elements of sensory testing. However, while compliance
assessment by trained and expert assessors is well developed, few informa-
tion is available on testing consumer consistency. Therefore, we aim to an-
swer the following research questions: What type of metrics can be used
to characterise (in)consistent evaluation? How to rank assessors and at-
tributes’ evaluations based on (in)consistency? Who can be considered an
(in)consistent assessor? What is the difference between consistent and in-
consistent assessors’ evaluations and use of scale? What is the impact of
consistent and inconsistent assessors’ evaluations on the overall liking esti-
mate? The proposed detection of (in)consistency requires evaluations on two
connected scales. We reveal how assessors and attributes can be ranked ac-
cording to the level of inconsistency, as well as how inconsistent assessors
∗ Corresponding author
Email addresses: sipos.laszlo@uni-mate.hu, sipos.laszlo@krtk.hun-ren.hu
(L´ aszl´ o Sipos),kolos.agoston@uni-corvinus.hu (Kolos Csaba ´Agoston),
peter.biro@krtk.hun-ren.hu (P´ eter Bir´ o),bozoki.sandor@sztaki.hun-ren.hu
(S´ andor Boz´ oki),laszlo.csato@sztaki.hun-ren.hu (L´ aszl´ o Csat´ o)
Preprint submitted to Elsevier December 2023
arXiv:2312.08141v1  [stat.AP]  13 Dec 2023

can be identified. The suggested approach is illustrated by data from sen-
sory tests of biscuits enriched with three pollens at different levels. Future
consumer tests are recommended to account for possible inconsistent evalu-
ations.
Keywords: consistency, consumer sensory testing, JAR scale, liking score,
product development
1. Introduction
Consumer testing is used in many areas of sensory research and food
practice. The use of liking/acceptability feedback from target consumers is
wide-ranging and includes comparing competing products, optimising prod-
uct development, determining shelf-life, obtaining the liking of sensory at-
tributes, assessing the impact of a product composition/packaging change on
liking, etc. The main focus is to test whether or not there is a perceived dif-
ference in liking as a result of a treatment/change/modification. Consumer
tests should be conducted with circumspection, taking into account many
factors such as: purpose of the research, type of product, number of prod-
ucts, definition of target population (market product/new product, current
users/potential users, preliminary results, specific segments), test location,
expected accuracy of measurement, test procedure, product presentation plan
for the chosen test procedure, specifications of the hypothesis to be tested
(composition and size of the consumer sample) [12].
In practice, there are a number of available consumer testing methods,
from which the most appropriate method for the research objective should
be chosen. There are two main groups of hedonic tests: 1) acceptability
tests that measure the intensity of pleasure of consumption; and 2) prefer-
ence tests that measure the order of preference of different products (pairwise
comparison test, ranking). Preference tests are relative and do not provide
information on acceptability. In addition to the test method, it is also neces-
sary to decide on the location of the test: central location test (CLT), point
of sale test (PST), home use test (HUT), home panel test (HPT), in-house
test (IHT), which can be characterised by different advantages and disadvan-
tages. The main advantage of tests carried out in a sensory laboratory is that
they are based on good sensory practice and are carried out under controlled
conditions. The advantages and disadvantages of different testing sites have
already been discussed in the literature [16, 12, 3, 10, 19, 22, 24, 33].
2

International standard methods, standard test conditions and the use of
good sensory practices are key elements of sensory testing, too. The charac-
teristics of a sensory expert include demonstrated sensory sensitivity, exten-
sive training and experience, and the ability to provide consistent and repeat-
able evaluations [15]. Compliance assessment by trained and expert assessors
is well developed: measurement of discrimination, agreement, repeatability
[11], consonance [2, 6, 17], scaling usage and scaling effect [5, 25, 29], statisti-
cal methods and software for performance measurement of sensory panelists
and panels [32], workflow of panel performance [23], characteristics of trained
panels [7], panel management [28], panel and panelist performance of Tem-
poral Dominance of Sensations [9, 20, 21, 31], sensory analysis programme
in quality control [13, 22, 26].
In sensory testing, consistency refers on the one hand to a mechanical at-
tribute perceived by mechanical tactile or visual receptors [15]. On the other
hand, the consistency is one of the performance characteristics of a trained
and expert assessor or panel, along with discrimination ability, repeatability
ability, agreement and scale usage, which can be monitored and evaluated
in one session or over time. According to the international standard for
guidelines for the measurement of quantitative descriptive sensory panel per-
formance the consistency of an assessor is inversely related to the standard
deviation of the bias terms (difference between the assessor’s mean for the
sample and the panel mean) calculated from each sample. Using ANOV A
model, both panel consistency (session to session standard deviation with
control sample) and internal consistency (interaction of assessor and session)
can be determined [11]. Internal consistency test based on Cronbach’s alpha
is an accepted method, since it allows identifying attributes better under-
stood by panelists, and it gives a ranking of panelists according to their
consensus with the rest of the panel [27]. Other multivariate methods are
also used to measure the (in)consistency of panels, such as Wilk’s lambda in
MANOV A models [8], or gravity centre and area/perimeter (GCAP) method
[18], and parallel factor analysis (PARAF AC) [30].
The problem of inconsistent consumer response is typically associated
with questionnaire surveys in consumer research. It is a common goal when
designing a questionnaire to filter out inconsistent consumer responses after
the test, so the same questions are often asked in different ways or on different
types of response scales. Obtaining unbiased and consistent study results
depends heavily on the way the survey is administered and distributed to
respondents and how respondents are sampled from the target population [4].
3

While there are many developed measures, indices and statistical methods
for trained and expert sensory assessors, there are no developed statistical
indicators for measuring consumer (in)consistency. The following research
questions have been identified:
1. What type of metrics can be used to characterise (in)consistent evalu-
ation?
2. How to rank assessors and the evaluations of attributes based on
(in)consistency?
3. Who can be considered an (in)consistent assessor?
4. What is the difference between consistent and inconsistent assessors’
evaluation and use of scale?
5. What is the impact of consistent and inconsistent assessors’ evaluations
on the overall liking estimate?
2. Material and Methods
2.1. Biscuit Preparation
Biscuits were prepared according to the AACC-approved method 10–50D
[1]. The control sample contained ingredients included in the standard.
Ground bee pollens were used to substitute 2%, 5%, or 10% of wheat flour
(C control; RS2, RS5, RS10 rapeseed; SF2, SF5, SF10 sunflower; PH2, PH5,
PH10 phacelia).
All ingredients were weighed in a plastic bowl with a precision of two
decimal places, then mixed into a homogenous mass. The dough was sheeted
to a thickness of 7mm. Biscuits with a diameter of 50mm were formed and
baked in an electrically heated rotary oven (Gierre, Milano, Italy) for 10
minutes at 205◦C. The samples were cooled to room temperature and placed
in sealable plastic bags for testing within one hour.
2.2. Consumers’ preference tests
Sensory tests were carried out in a sensory laboratory (Hungarian Uni-
versity of Agriculture and Life Sciences, Institute of Food Science and Tech-
nology, Department of Postharvest, Commercial and Sensory Science) that
meet the standard requirements [16]. The work was conducted in accordance
4

with The Code of Ethics of the World Medical Association (Declaration of
Helsinki). The tests were carried out anonymously and on a voluntary basis.
Participants gave informed consent via the statement “I am aware that my
responses are confidential, and I agree to participate in this experiment”;
an affirmative reply was required to enter the test. They were able to with-
draw from the experiment at any time without giving a reason. The products
tested were safe for consumption. Before the test, participants were informed
that the biscuits contained pollen and gluten, which may cause hypersensi-
tivity reactions in sensitive individuals. The tests were designed and imple-
mented according to the international standard for consumer preference tests
[12]. A total of 100 consumers participated. Inclusion criteria were as follows:
willingness to participate in the experiment, does not have a history of food
allergies or intolerances including sensitivity to beekeeping products. Each
participant evaluated biscuits on two sessions to minimize fatigue. Products
were coded with random, three-digit numbers starting with non-zero. Orders
of biscuit samples were balanced. As a taste neutralizer, mineral water with
a neutral taste was provided for each participant.
Consumers evaluated the different samples on two different scales. Firstly,
the biscuits were evaluated according to their liking, based on the following
10 attributes: darkness, overall odour, sweet odour, margarine odour, overall
taste, sweet taste, margarine taste, hardness, crumbliness, and overall ac-
ceptance. A nine-category monotonic ascending hedonic response scale was
used, where each category was associated with emoticons and descriptive
terms (1 = extremely dislike, 2 = strongly dislike, 3 = moderately dislike,
4 = slightly dislike, 5 = neither like nor dislike, 6 = slightly like, 7 = mod-
erately like, 8 = strongly like, 9 = extremely like). Secondly, the biscuits
were evaluated according to their intensity values, including the following 9
attributes: darkness, overall odour, sweet odour, margarine odour, overall
taste, sweet taste, margarine taste, hardness, crumbliness, on a 5-category
just about right (JAR) scale ( −2 = not enough at all, −1 = not enough, 0
= just about right, 1 = too much, 2 = far too much) [14].
3. Results
This section presents our approach for measuring inconsistency and ap-
plies it to the biscuit dataset. Tables 1 and 2 show the means and standard
deviations of the liking and JAR intensity scores for the 10 different types of
products.
5

Table 1: Descriptive statistics of liking scores
Attribute C RS2 RS5 RS10 SF2 SF5 SF10 PH2 PH5 PH10 All
Colour 6.18 (1.93) 6.36 (1.43) 6.92 (1.69) 6.73 (1.77) 6.81 (1.66) 6.91 (1.56) 6.65 (1.86) 5.81 (1.94) 4.73 (1.95) 4.66 (2.28) 6.18 (1.99)
Global odour 5.87 (1.60) 5.68 (1.85) 5.56 (2.00) 4.65 (2.43) 6.18 (1.51) 6.12 (1.57) 5.81 (2.18) 5.84 (1.65) 5.61 (1.52) 4.38 (1.98) 5.57 (1.93)
Sweet odour 5.58 (1.94) 5.51 (1.90) 5.78 (1.90) 4.59 (2.23) 5.67 (1.65) 5.79 (1.71) 5.46 (1.97) 5.46 (1.78) 5.35 (1.64) 4.20 (1.86) 5.34 (1.92)
Margarine odour 5.38 (1.25) 5.37 (1.61) 5.43 (1.53) 4.52 (1.94) 5.85 (1.42) 5.42 (1.49) 5.49 (1.55) 5.44 (1.54) 5.40 (1.63) 4.46 (1.68) 5.28 (1.63)
Global taste 6.50 (1.76) 5.76 (2.16) 5.82 (1.85) 4.63 (2.58) 6.96 (1.36) 6.89 (1.59) 6.10 (2.16) 6.71 (1.82) 6.63 (1.59) 4.11 (2.42) 6.01 (2.14)
Sweet taste 6.57 (1.58) 6.25 (1.88) 6.38 (1.80) 5.23 (2.40) 6.94 (1.39) 6.78 (1.62) 6.03 (1.91) 6.50 (1.70) 6.60 (1.54) 4.59 (2.35) 6.19 (1.97)
Margarine taste 5.83 (1.83) 5.36 (1.76) 5.35 (1.65) 4.9 (2.04) 6.36 (1.51) 6.16 (1.45) 5.55 (1.87) 6.15 (1.60) 5.72 (1.90) 4.30 (1.88) 5.57 (1.85)
Hardness 4.92 (2.27) 6.02 (2.00) 4.98 (2.25) 4.56 (2.57) 6.62 (2.00) 5.62 (2.21) 4.92 (2.48) 5.58 (2.38) 4.39 (2.38) 3.58 (2.54) 5.12 (2.45)
Crumbleness 5.61 (2.05) 6.26 (1.91) 5.70 (2.02) 5.36 (2.32) 6.39 (1.88) 6.18 (1.97) 5.57 (2.02) 5.60 (2.16) 5.39 (2.07) 4.87 (2.34) 5.69 (2.12)
Global liking 6.29 (1.79) 5.94 (2.21) 5.99 (1.93) 4.69 (2.59) 6.93 (1.63) 6.58 (1.82) 5.80 (2.09) 6.53 (1.71) 5.81 (1.96) 3.83 (2.34) 5.84 (2.20)
Notes: Means are at the top, standard deviations are at the bottom in parenthesis.
C: control.
RS2, RS5, RS10: rapeseed (2%, 5%, 10%).
SF2, SF5, SF10: sunflower (2%, 5%, 10%).
PH2, PH5, PH10: phacelia (2%, 5%, 10%).
6

Table 2: Descriptive statistics of JAR scores
Attribute C RS2 RS5 RS10 SF2 SF5 SF10 PH2 PH5 PH10 All
Colour −0.83 (0.84) −0.69 (0.75) −0.29 (0.48) 0.54 (0.74) −0.21 (0.62) 0.40 (0.55) 0.51 (0.69) −0.13 (0.92) 0.90 (1.05) 1.56 (0.72) 0.18 (1.03)
Global odour −0.74 (0.73) −0.16 (0.94) −0.08 (0.75) 0.80 (1.02) −0.49 (0.81) −0.04 (0.85) 0.18 (1.00) −0.23 (0.81) −0.10 (0.88) 0.80 (1.24) −0.01 (1.03)
Sweet odour −0.86 (0.80) −0.43 (0.89) −0.39 (0.82) −0.11 (1.19) −0.54 (0.74) −0.36 (0.84) −0.60 (0.93) −0.51 (0.90) −0.61 (0.79) −0.86 (1.18) −0.53 (0.94)
Margarine odour −0.59 (0.75) −0.16 (0.90) −0.44 (0.84) −0.18 (1.17) −0.29 (0.69) −0.16 (0.80) −0.37 (0.99) −0.32 (0.85) −0.42 (0.94) −0.48 (1.26) −0.34 (0.94)
Global taste −0.16 (0.80) 0.27 (0.85) 0.18 (0.70) 0.94 (1.04) −0.23 (0.62) 0.17 (0.71) 0.35 (0.95) −0.11 (0.60) 0.05 (0.73) 0.85 (1.27) 0.23 (0.93)
Sweet taste −0.09 (0.81) 0.24 (0.88) 0.23 (0.74) 0.18 (1.22) −0.10 (0.61) −0.06 (0.75) 0.05 (0.97) −0.01 (0.73) −0.25 (0.74) −0.72 (1.21) −0.05 (0.92)
Margarine taste −0.16 (0.92) −0.10 (0.89) −0.14 (0.79) −0.03 (1.11) −0.15 (0.69) −0.08 (0.77) −0.10 (0.93) −0.10 (0.70) −0.19 (0.80) −0.51 (1.13) −0.16 (0.89)
Hardness 0.42 (0.94) −0.15 (0.78) 0.53 (0.76) 1.02 (0.89) 0.01 (0.67) 0.67 (0.73) 0.88 (0.86) 0.53 (0.87) 0.88 (0.87) 1.59 (0.79) 0.64 (0.94)
Crumbleness 0.03 (0.80) −0.06 (0.80) 0.25 (0.81) 0.40 (0.92) 0.21 (0.80) 0.33 (0.80) 0.39 (0.74) 0.28 (0.74) 0.44 (0.91) 0.27 (1.14) 0.25 (0.99)
Notes: Means are at the top, standarda deviations are at the bottom in parenthesis.
C: control.
RS2, RS5, RS10: rapeseed (2%, 5%, 10%).
SF2, SF5, SF10: sunflower (2%, 5%, 10%).
PH2, PH5, PH10: phacelia (2%, 5%, 10%).
Numbers in italics are significantly different from zero at 5%.
7

Table 3: Contingency table of all liking and JAR scores
(a) Numbers of evaluations
Liking JAR score
score −2 −1 0 1 2
1 77 39 37 43 131
2 92 69 69 88 145
3 77 142 112 163 131
4 83 215 240 274 114
5 135 477 829 270 81
6 57 358 625 308 54
7 52 304 824 304 43
8 22 184 943 202 45
9 3 36 432 46 25
(b) Proportional distribution of JAR scores for each liking score
Liking JAR score
score −2 −1 0 1 2
1 23.55% 11.93% 11.31% 13.15% 40.06%
2 19.87% 14.90% 14.90% 19.01% 31.32%
3 12.32% 22.72% 17.92% 26.08% 20.96%
4 08.96% 23.22% 25.92% 29.59% 12.31%
5 07.53% 26.62% 46.26% 15.07% 04.52%
6 04.07% 25.53% 44.58% 21.97% 03.85%
7 03.41% 19.91% 53.96% 19.91% 02.82%
8 01.58% 13.18% 67.55% 14.47% 03.22%
9 00.55% 06.64% 79.70% 08.49% 04.61%
3.1. The relationship between liking and JAR scores
Based on the definitions of the liking and JAR intensity scales, the high-
est liking score (extremely liked, 9) is expected to be associated with the
optimal level of intensity (just about right, 0). Being less strict, a reasonable
assumption for the consistency of evaluations is that a higher liking score
implies a lower absolute JAR intensity score, and vice versa.
Table 3a shows the contingency table of the liking scores and JAR in-
tensity values when all evaluations are considered. The general picture is
8

encouraging: for low liking scores, JAR scores of −2 or +2 are dominant and
vice versa; for high liking scores, JAR score of 0 is dominant. On the other
hand, the lowest possible liking score (1) coincides with an optimal JAR in-
tensity level (JAR score = 0) in 37 cases out of the total 9000. Similarly,
in 28 (25 + 3) cases, the highest liking score (9) comes with a JAR score of
−2 or +2, which indicates suspicious and possible unreliable opinions. These
observations strengthen our idea that the issue of (in)consistency is worth
analyzing deeper.
Table 3b reports the normalized contingency table, where the relative
frequencies sum to 1 in each row. This makes the distributions of JAR
scores for different liking scores comparable. For example, for the JAR value
of −2, the nominal frequencies corresponding to liking scores 1 and 2 is 77-92,
which is explained by the fact that liking 2 was given more frequently. The
normalized values 23.55% and 19.87% show the relation better: a JAR score
of −2 has a higher probability to occur if the liking score is 1 rather than
2. Unsurprisingly, the normalized frequencies are decreasing as a function
of the liking score for the JAR value −2. However, this pattern does not
hold for the JAR value +2 if the liking score is relatively high. Finally, the
normalized frequencies are almost increasing for JAR= 0, except for liking
values 5 and 6.
3.2. Identifying inconsistent evaluations
Given an attribute and a biscuit sample, we consider a pair of evaluations
on liking and JAR scales consistent if a higher liking score is associated with
a smaller absolute JAR score. The Kendall τ correlation coefficient, one
of the widely used rank correlation coefficients, seems to be an appropriate
measure for this relationship. However, the original version of Kendall τ does
not allow for ties, but ties are characteristic in these applications.
The modified versions of Kendall τA, τB and τc allow ties but differ from
each other in the way of handling them. Since the frequency of ties is quite
high due to the narrow JAR scale, and the corresponding contingency table
is non-squared (nine liking scores vs. three absolute JAR intensity scores),
Kendall τC—also known as Stuart τC—seems to be the best option. Its range
is the interval [ −1, +1], where −1 indicates perfect correlation between the
two evaluations, that is, a higher liking score is always paired to a lower JAR
intensity score, and vice versa.
Assume that there are n observations and a pair of values (likingi, JARi)
for each observation (i = 1, . . . , n). Furthermore:
9

– Let nc denote the number of “concordant” pairs ( i, j), for which either
likingi > likingj and |JARi| < |JARj|; or likingi < likingj and |JARi| >
|JARj| hold, where |a| is the absolute value of a;
– Let nd denote the number of “discordant” pairs ( i, j), for which either
likingi > likingj and |JARi| < |JARj|; or likingi < likingj and |JARi| >
|JARj| hold;
– Let m denote the minimum of columns and rows in the crosstable.
The definition of Kendall τC is:
τC = nc − nd
n2(m − 1)/m .
The Kendall τC values have been calculated using the StuartTauC func-
tion in package DescTools in R.
A perfectly consistent assessor, with Kendall τC = −1, may give pairs of
evaluations such as (9,0), (1,−2), (5,+1), where the first coordinate is on the
liking scale and the second one is on the JAR intensity scale. A totally incon-
sistent assessor, with Kendall τC = +1, may give completely contradictory
evaluation-pairs such as (9, −2), (7,+1), (1,0). Random evaluations would
lead to Kendall τC = 0 in expected value. Thus, if Kendall τC is closer to
−1, a higher liking score is more likely to be associated with a lower absolute
JAR value.
Consequently, the Kendall τC coefficient can be used to quantify the level
of inconsistency. The coefficient should be negative for a consistent assessor—
and it can be tested whether Kendall τC is significantly smaller than 0. This
makes it possible to identify assessors whose evaluations seem to be random
(it cannot be rejected that Kendall τC is zero), as well as assessors whose
evaluations are worse than random (Kendall τC coefficient is significantly
positive), which indicates a possible misunderstanding of the task.
Table 4 shows the least and the most inconsistent assessors in our sample.
In particular, Table 4a is the contingency table of the least inconsistent asses-
sor (who has the smallest Kendall τC = −0.73), while Table 4b corresponds
to the least consistent assessor (who has the smallest Kendall τC = 0.08).
Table 4a is visualized in Figure 1. Circle sizes are proportional to the
frequencies of liking-JAR score pairs. The hypothetical perfectly consistent
assessor, who gives (9,0), (1, −2), (1,+2), (5, −1) and (5,+1), would result in
10

Table 4: Contingency tables of the least and the most inconsistent assessors
(a) The least inconsistent assessor (Kendall τC = −0.73)
Liking JAR score
score −2 −1 0 1 2
1 1 1 0 0 11
2 3 1 0 0 3
3 0 0 0 0 1
4 0 2 0 4 3
5 1 4 9 0 3
6 0 0 8 2 0
7 0 1 10 4 0
8 0 0 6 2 0
9 0 0 10 0 0
(b) The most inconsistent assessor (Kendall τC = 0.08)
Liking JAR score
score −2 −1 0 1 2
1 0 0 0 0 2
2 0 0 8 0 0
3 0 1 3 0 0
4 0 0 1 1 2
5 0 0 29 3 0
6 0 0 11 4 0
7 1 1 8 4 0
8 1 0 7 2 0
9 0 1 0 0 0
a > shape. The distribution of circles of the least inconsistent assessor shows
a similar pattern.
Note that the intermediate liking score 5 frequently (29 times) occurs
together with a JAR score of 0, representing an ideal level, in Table 4b. This
phenomenon can be observed not only for the most inconsistent assessor, but
also for many other ones. A possible explanation is a misunderstanding or
misinterpretation of the two scales.
This phenomenon calls attention to a potential drawback of the Kendall
11

liking score
JAR score1 2 3 4 5 6 7 8 9
1
2
0
−1
−2
Figure 1: JAR and liking scores of the least inconsistent assessor (see also Table 4a).
τC rank correlation coefficient: neither concordant, nor disconcordant pairs
can be identified if the liking or JAR values are equal. In an extreme case,
if an assessor has only given JAR values of 0, then τC = 0, independently of
the liking values.
3.3. The consistency of assessors’ evaluations
Consistency can be analysed with respect to both the assessors and the
attributes, which leads to the rankings of assessors as well as attributes ac-
cording to the proposed Kendall tauC. Rank leaders’ pairs of evaluations
satisfy consistency the most frequently and to the highest degree. This way
the definition of consistency can be applied to assessors or attributes.
Figure 2 presents the distribution of Kendall τC coefficients for all asses-
sors. Unsurprisingly, they are typically negative, but some positive values
also occur. At a significance level 5%, 88 assessors have a significantly nega-
tive Kendall τC coefficient, the remaining 12 assessors get the “inconsistent”
label.
12

−1 −0.5 0 0.5 10
5
10
15
20
25
Figure 2: Histogram of Kendall τC values for the 100 assessors
(a) Liking scores
3
4
5
6
7
Inconsistent Consistent
(b) JAR scores
-0.5
-0.25
0
0.25
0.5
Inconsistent Consistent
Figure 3: Comparison of mean scores for the two types of assessors
3.4. The connection between consistency and the use of the scales
In the first step, the mean liking score and mean JAR scores have been
calculated across all samples and attributes that can be seen in Figure 3.
Interestingly, three is no significant difference between the two groups, sta-
tistical tests do not reject a null hypothesis of equal means for consistent and
inconsistent assessors.
13

(a) Liking scores
1.4
1.8
2.2
2.6
3
Inconsistent Consistent
(b) JAR scores
0.5
0.7
0.9
1.1
1.3
Inconsistent Consistent
Figure 4: Comparison of standard deviations for the two types of assessors
In the second step, the standard deviation of liking scores and JAR scores
have been calculated across all samples and attributes that can be seen in
Figure 4. Now, there are significant differences between the two groups, the
consistent assessors generally use both scales with a higher spread than the
inconsistent assessors.
This finding is somewhat surprising because we assumed that inconsistent
assessors would only select a few random values when the standard deviations
of the inconsistent assessors would be higher. Looking at the results, it seems
that the consistent assessors are more confident and, therefore, use the scale
more “intensively”, giving values from a broader range of the scale.
The relationship between the standard deviation of the liking/JAR scores
and Kendall τC coefficient values is worth further analyzing. Figure 5 rein-
forces that for higher standard deviation the KendallτC correlation coefficient
tends to be lower for a higher standard deviation, which makes the assessor
is less inconsistent. The slope of the fitted curve is also negative.
Finally, Figure 6 compares the number of evaluation pairs without ties,
and the Kendall τC coefficients. The inconsistent assessors seem to be less
discriminative in their evaluations, and there is non-negligible connection
between the number of evaluation pairs without ties and Kendall τC even
for the consistent assessors. This provides another evidence that the less
inconsistent assessors use the two scales better, they are more likely to avoid
14

(a) Liking scores
1.5 2 2.5
−0.8
−0.6
−0.4
−0.2
0.0
Standard deviation
Kendall τC
(b) JAR scores
0.4 0.6 0.8 1 1.2
−0.8
−0.6
−0.4
−0.2
0.0
Standard deviation
Figure 5: The relationship
between the standard deviation of scores and Kendall τC coefficients for the assessors
Notes: Blue points represent consistent assessors. Red points represent inconsistent assessors.
The dashed line shows the linear trend, which is y = 0.07062 − 0.22345x (R2 = 0.1825) for Figure 5a and
y = −0.005823 − 0.370524x (R2 = 0.1318) for Figure 5b.
giving the same score for two different products.
3.5. The consistency of evaluations with respect to attributes
Any attribute is only one aspect of the sensory evaluation. As such, it does
not include a direct source of inconsistency. However, once the assessments
are collected from two different scales (nine-category monotonic ascending
liking response scale, five-category just about right (JAR) scale of intensity),
it becomes reasonable to define the level of inconsistency with respect to
a particular attribute. If the same biscuit is evaluated differently by the
two scales (e.g. it gets the highest liking score and the highest/lowest JAR
score), then the assessment, with respect to the given attribute, becomes
controversial.
The Kendall τC coefficients can also be calculated between the rankings
of liking scores and JAR scores (in absolute value) for each attribute across
all assessors and samples, which is presented in Table 5. Furthermore, τC
is plotted as a function of the standard deviations of the scores in Figure 7.
The standard deviations are the smallest and the Kendall τC coefficients
are the highest for margarine odour and margarine taste that the assessors
probably find difficult to evaluate. On the other hand, colour and global
15

800 1,000 1,200 1,400 1,600 1,800 2,000 2,200 2,400 2,600
−0.8
−0.6
−0.4
−0.2
0.0
Number of concordant and disconcordant evaluation pairs
Kendall τC
Figure 6: The relationship between the number of
concordant and disconcordant evaluation pairs and KendallτC coefficients for the assessors
Notes: Blue points represent consistent assessors. Red points represent inconsistent assessors.
The dashed line shows the linear trend, which is y = 0.3459 − 0.0003x (R2 = 0.2861).
Table 5: Kendall τC correlation coefficients for each attribute
Attribute Abbreviation Value of Kendall τC
Colour CL −0.54
Global odour GO −0.35
Sweet odour SO −0.35
Margarine odour MO −0.20
Global taste GT −0.47
Sweet taste ST −0.39
Margarine taste MT −0.29
Hardness HN −0.43
Crumbleness CR −0.31
taste are evaluated less inconsistently as shown by the low value of KendallτC
(Table 5). Again, Figure 7 reveals a (significant) negative correlation between
the standard deviation of scores and Kendall τC coefficients, although the
sample size is small, making the result less reliable.
16

(a) Liking scores
1.6 1.8 2 2.2 2.4
−0.5
−0.4
−0.3
−0.2
CL
GO
SO
MO
GT
ST
MT
HN
CR
Standard deviation
Kendall τC
(b) JAR scores
0.85 0.9 0.95 1
−0.5
−0.4
−0.3
−0.2
CL
GOSO
MO
GT
ST
MT
HN
CR
Standard deviation
Figure 7: The relationship
between the standard deviation of scores and Kendall τC coefficients for the attributes
Notes: Each point represents an attribute.
The dashed line shows the linear trend, which is y = 0.1566 − 0.2632x (R2 = 0.3523) for Figure 7a and
y = 0.4312 − 0.8502x (R2 = 0.2138) Figure 7b.
The abbreviations of the attributes are given in table 5.
3.6. The effect of inconsistent evaluations
Here we focus on the importance of considering the consistency of the
assessors. The relationship between global taste and global liking scores can
be studied by fitting three models. In Figure 8, the first regression is based
on all evaluations (black dotted line), the second only on consistent assessors
(blue dashed line), and the third only on inconsistent assessors (red solid
line). The slope is somewhat steeper for consistent assessors but the blue
and black lines almost coincide since 88% of the assessors are consistent in
our study. However, other sensory tests may lead to substantially different
ratio of consistent and inconsistent assessors, and the aggregated preferences
vary depending on including or excluding the inconsistent group. Therefore
such an analysis is recommended for each consumer sensory test.
Finally, the global liking score can be explained with the nine attributes
of the experiment such that separate models are estimated for consistent and
inconsistent assessors. The regression outputs can be found in the Appendix.
Even though the regression models do not differ to a high extent, some
differences appear as well:
– for consistent assessors, global taste plays a more robust role;
17

Global taste
Global liking
1 2 3 4 5 6 7 8 9
1
2
3
4
5
6
7
8
9
Figure 8: The relationship between global taste and global liking scores
Notes: The ratio of consistent and inconsistent assessors is shown by blue and orange circular sectors.
The three lines shows linear trends, which are y = 1 .21097 + 0.76649x (R2 = 0 .5619) for consistent
assessors (dashed blue); y = 2 .53432 + 0.58105x (R2 = 0 .3428) for inconsistent assessors (solid red);
y = 1.34029 + 0.74841x (R2 = 0.5381) for all assessors (black dotted).
– for consistent assessors, all significant variables have positive coeffi-
cients, but this is not obvious for inconsistent assessors;
– a different set of variables is significant for the two groups;
– the explanatory power is better for consistent assessors (the values of
18

the adjusted R2 are 0.66 and 0.56 for the two groups, respectively).
4. Discussion
The results are discussed separately for each research question. Further-
more, we have some suggestions on how to conduct sensory tests in the
future.
What type of metrics can be used to characterise consistent and inconsistent
evaluation?
To assess (in)consistency, at least two values should exist that can be
compared.
This approach requires the presence of two scales (liking, JAR), whose
pairs of values provide the basis for the comparison. In our case, any as-
sessor evaluated the same attribute in two different ways, first on a nine-
category monotonic ascending hedonic response scale, and on a five-category
just about right (JAR) scale.
How to rank assessors and attributes’ evaluations based on (in)consistency?
The previous approach can be used, either to evaluate the attributes or
to rank the assessors according to their level (in)consistency. The order of
the attributes has a natural interpretation. For example, an inconsistent
attribute may indicate that it is difficult to interpret or perceive by the
consumers. Such an attribute should be specified or omitted from tests of
the given product. In other words, consumer questionnaires need to take the
ability, knowledge, and perception of consumers into account.
Assessors have different perceptual, cognitive, socio-cultural background.
At the same time, the consumer test administered at a given time may be
influenced by the individual’s current health status, motivational state, task
awareness, attention, concentration, hunger, mood, etc. If the inconsistency
on a given trait affects a large number of raters, it indicates problems with
the sensory trait. If it involves a small number of raters, then it is the
individual’s assessment that needs to be examined.
Who can be considered an (in)consistent assessor?
If one has a ranking of assessors by their inconsistency, a simple threshold
can be used to separate the set of assessors whose evaluations are probably
19

unreliable for the given set. A natural choice is labelling an assessor inconsis-
tent if their evaluations are seemingly random (or they have misunderstood
the two scales), i.e., the associated Kendall τC is not significantly negative.
What is the difference between consistent and inconsistent assessors’ evalua-
tion and use of scale?
In our dataset, the mean liking and JAR values of consistent raters and
inconsistent raters do not differ significantly, but they do differ significantly
in their standard deviations. The range of the scale is better used by the
consistent assessors in both liking and JAR assessment. Further studies are
needed to test this conjecture. Scale usage should also be analysed in any
such test because it may be indicative of inconsistent evaluation.
What is the impact of consistent and inconsistent assessors’ evaluations on
the overall liking estimate?
In our study, there is no significant difference between inconsistent and
consistent assessors in the estimation of global liking. However, it is entirely
possible that this effect varies from test to test, and significantly high effects
may be observed for the evaluation of inconsistent assessors. Therefore, the
impact of omitting inconsistent evaluations should be checked after each test.
Recommendations
Using two different scales (e.g. liking and JAR) in sensory testing makes it
possible to identify and measure the inconsistency of assessors. Nonetheless,
it is important to ensure that they fully understand the two scales, which can
be checked, for instance, by presenting two examples with Kendall τC values
close to −1 and 0 (such as in Table 4) and asking which of them is more likely
to be obtained from a past test. Furthermore, in an online questionnaire, the
evaluations can be continuously monitored and the assessor might be warned
if the last score is suspicious, e.g. an almost maximal liking score is followed
by a JAR score of −2 or +2, when the assessor can be asked to review
the most recent score. This technique can help to avoid typos and obvious
mistakes.
Once the evaluations are collected, the process described in Section 3 can
be implemented:
1. Kendall τC coefficients are calculated for all assessors;
20

2. Assessors are called consistent and inconsistent according to whether
the Kendall τC of their evaluations is significantly lower than zero (con-
sistent) or not (inconsistent);
3. The standard sample analysis is carried out for all consistent asses-
sors, as well as for only the consistent assessors, and the results are
compared.
Generally, we think it is better to conclude only on the basis of consistent
evaluations since inconsistent preferences may distort reality.
5. Conclusions
Consumer sensory testing is the basis for determining directions of prod-
uct development in food industry practice. The reliability of consumer
tests resides in the consistency of consumer assessment. In our study, the
consumers evaluated different biscuit samples on two different scales (nine-
category monotonic ascending hedonic response scale, five-category just about
right (JAR) intensity scale), which allowed testing consistency. Using these
pairs of evaluations, Kendall τC values have been calculated to identify incon-
sistent evaluations, which might be considered with a lower weight or fully
excluded from further assessment (e.g. preference mapping, or penalty anal-
ysis, etc.). A ranking of both assessors and attributes can be established,
too. We found that consistent assessors are characterised by the use of a
broader range of the liking scale and JAR scale.
Further research is needed on the roots, factors and circumstances be-
hind inconsistent evaluations: sensory fatigue, misunderstanding of scales,
intentional manipulation, motivation, mental abilities, different perceptual
abilities, product specificity, etc. For all consumer sensory tests having a
similar design, it is advisable to test inconsistency since this is the only way
to tell who has been affected by the inconsistent evaluation, for which sen-
sory attribute and for which sensory question. Furthermore, future consumer
tests are recommended to be adapt a design that makes it possible to identify
inconsistent evaluations.
Acknowledgements
This research was funded by National Research, Development and Innovation
Office, OTKA, contracts number 135700.
21

References
[1] AACC (1980). Approved Method 10-50D: Baking Quality of Cookie Flour.
AACC, Washington, DC, USA.
[2] Aguirre, V. M., Huerta-Pacheco, N. S., and Lopez, M. T. (2017). CONS
an R based graphical interface to perform Consonance Analysis. Food
Quality and Preference, 62:183–189.
[3] Boutrolle, I., Delarue, J., Arranz, D., Rogeaux, M., and K¨ oster, E. P.
(2007). Central location test vs. home use test: Contrasting results de-
pending on product type. Food Quality and Preference, 18(3):490–499.
[4] Brace, I. (2018). Questionnaire Design: How to plan, structure and write
survey material for effective market research . Kogan Page Publishers.
[5] Brockhoff, P. B., Schlich, P., and Skovgaard, I. (2015). Taking individual
scaling differences into account by analyzing profile data with the mixed
assessor model. Food Quality and Preference, 39:156–166.
[6] Dijksterhuis, G. (1995). Assessing panel consonance. Food Quality and
Preference, 6(1):7–14.
[7] Djekic, I., Lorenzo, J. M., Munekata, P. E., Gagaoua, M., and Tomasevic,
I. (2021). Review on characteristics of trained sensory panels in food
science. Journal of Texture Studies , 52(4):501–509.
[8] Fernando, D. R., Samita, S., and Peiris, T. U. S. (2022). Identifying panel
inconsistency in sensory profiles using Multivariate Analysis of Variance
(MANOV A) and follow-up Canonical Variate Analysis (CV A). Tropical
Agricultural Research, 33(1):80–91.
[9] Frascolla, C., Visalli, M., Cardot, H., and Schlich, P. (2023). Indexes of
individual repeatability and product discrimination in TDS and TCATA
and their statistical inference. Food Quality and Preference, 110:104929.
[10] Hasted, A., McEwan, J. A., and Jenner, M. (2023). Controlled prod-
uct testing in the home-implications for sample size. Food Quality and
Preference, 103:104688.
22

[11] ISO 11132 (2021). Sensory Analysis—Methodology—Guidelines for the
measurement of the performance of a quantitative descriptive sensory
panel. ISO, Geneva, Switzerland.
[12] ISO 11136 (2014). Sensory Analysis—Methodology—General guidance
for conducting hedonic tests with consumers in a controlled area . ISO,
Geneva, Switzerland.
[13] ISO 20613 (2019). Sensory Analysis—General guidance for the applica-
tion of sensory analysis in quality control . ISO, Geneva, Switzerland.
[14] ISO 4121 (2003). Sensory Analysis—Guidelines for the use of quantita-
tive response scales. ISO, Geneva, Switzerland.
[15] ISO 5492 (2008). Sensory Analysis—Vocabulary. ISO, Geneva, Switzer-
land.
[16] ISO 8589 (2007). Sensory Analysis—General guidance for the design of
test rooms. ISO, Geneva, Switzerland.
[17] Kermit, M. and Lengard, V. (2005). Assessing the performance of a sen-
sory panel–panellist monitoring and tracking. Journal of Chemometrics:
A Journal of the Chemometrics Society , 19(3):154–161.
[18] Koll´ ar-Hunek, K., Heszberger, J., K´ okai, Z., L´ ang-L´ azi, M., and Papp,
E. (2008). Testing panel consistency with gcap method in food profile anal-
ysis. Journal of Chemometrics: A Journal of the Chemometrics Society ,
22(3-4):218–226.
[19] Lawless, H. T. and Heymann, H. (2010). Sensory Evaluation of Food:
Principles and Practices . Springer, Berlin/Heidelberg, second edition.
[20] Lepage, M., Neville, T., Rytz, A., Schlich, P., Martin, N., and Pineau,
N. (2014). Panel performance for temporal dominance of sensations. Food
Quality and Preference, 38:24–29.
[21] Meyners, M. (2011). Panel and panelist agreement for product compar-
isons in studies of Temporal Dominance of Sensations. Food quality and
Preference, 22(4):365–370.
[22] Munoz, A. M., editor (2013). Sensory Evaluation in Quality Control .
Springer Science & Business Media.
23

[23] Næs, T., Brockhoff, P. B., and Tomic, O. (2011). Statistics for Sensory
and Consumer Science . John Wiley & Sons.
[24] Park, S., Heo, J., Oh, J., Chung, S.-J., and Kwak, H. S. (2023). Con-
sumer testing away from a sensory facility: Application of home-use test
and no-contact home-use test. Food Quality and Preference, 109:104905.
[25] Peltier, C., Visalli, M., and Schlich, P. (2016). Multiplicative decompo-
sition of the scaling effect in the mixed assessor model into a descriptor-
specific and an overall coefficients. Food Quality and Preference, 48:268–
273.
[26] Pineau, N., Chabanet, C., and Schlich, P. (2007). Modeling the evolution
of the performance of a sensory panel: a mixed-model and control chart
approach. Journal of Sensory Studies , 22(2):212–241.
[27] Pinto, F. S. T., Fogliatto, F. S., and Qannari, E. M. (2014). A method
for panelists’ consistency assessment in sensory evaluations based on the
Cronbach’s alpha coefficient. Food Quality and Preference, 32:41–47.
[28] Rogers, L. (2017). Sensory Panel Management: A Practical Handbook
for Recruitment, Training and Performance . Woodhead Publishing.
[29] Romano, R., Brockhoff, P. B., Hersleth, M., Tomic, O., and Næs, T.
(2008). Correcting for different use of the scale and the need for further
analysis of individual differences in sensory analysis. Food Quality and
Preference, 19(2):197–209.
[30] Romano, R., Vestergaard, J. S., Kompany-Zareh, M., and Bredie,
W. L. P. (2011). Monitoring Panel PerformanceWithin and between
Sensory Experiments by Multi-Way Analysis , page 335–342. Springer,
Berlin/Heidelberg.
[31] Schlich, P. (2017). Temporal Dominance of Sensations (tds): A new deal
for temporal sensory analysis. Current Opinion in Food Science, 15:38–42.
[32] Sipos, L., Nyitrai, ´A., Hitka, G., Friedrich, L. F., and K´ okai, Z. (2021).
Sensory panel performance evaluation—Comprehensive review of practical
approaches. Applied Sciences, 11(24):11977.
[33] Stone, H., Bleibaum, R. N., and Thomas, H. A. (2020). Sensory Evalu-
ation Practices. Academic Press.
24

Appendix
Regression output for consistent assessors
Coefficients:
Estimate Std. Error t value Pr(>|t|)
(Intercept) -0.81294 0.21183 -3.838 0.000133 ***
colour 0.06173 0.02364 2.611 0.009184 **
global_odour 0.12827 0.03115 4.118 4.18e-05 ***
sweet_odour 0.04783 0.03091 1.547 0.122189
margarine_odour -0.04080 0.03275 -1.246 0.213218
global_taste 0.48071 0.03096 15.525 < 2e-16 ***
sweet_taste 0.10315 0.03257 3.167 0.001592 **
margarine_taste 0.11238 0.03105 3.619 0.000313 ***
hardness 0.16735 0.02058 8.132 1.45e-15 ***
crumbleness 0.08486 0.02344 3.621 0.000310 ***
---
Signif. codes: 0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
Multiple R-squared: 0.6601, Adjusted R-squared: 0.6565
Regression output for inconsistent assessors
Coefficients:
Estimate Std. Error t value Pr(>|t|)
(Intercept) -0.58162 0.67222 -0.865 0.388800
colour -0.07221 0.07742 -0.933 0.353032
global_odour 0.18447 0.09435 1.955 0.053098 .
sweet_odour 0.16118 0.09816 1.642 0.103442
margarine_odour -0.17723 0.09003 -1.969 0.051517 .
global_taste 0.29717 0.07766 3.827 0.000216 ***
sweet_taste 0.29706 0.08925 3.328 0.001188 **
margarine_taste 0.30966 0.07768 3.986 0.000121 ***
hardness 0.18614 0.06167 3.019 0.003157 **
crumbleness -0.02762 0.06915 -0.399 0.690315
---
Signif. codes: 0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
Multiple R-squared: 0.5972, Adjusted R-squared: 0.5642
25

Regression output for all assessors
Coefficients:
Estimate Std. Error t value Pr(>|t|)
(Intercept) -0.73306 0.20278 -3.615 0.000316 ***
colour 0.04650 0.02272 2.047 0.040955 *
global_odour 0.13847 0.02969 4.664 3.53e-06 ***
sweet_odour 0.06059 0.02963 2.045 0.041162 *
margarine_odour -0.06306 0.03064 -2.058 0.039866 *
global_taste 0.44907 0.02883 15.575 < 2e-16 ***
sweet_taste 0.12280 0.03066 4.006 6.65e-05 ***
margarine_taste 0.14075 0.02864 4.915 1.04e-06 ***
hardness 0.17121 0.01957 8.749 < 2e-16 ***
crumbleness 0.07089 0.02227 3.184 0.001498 **
---
Signif. codes: 0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
Multiple R-squared: 0.6463, Adjusted R-squared: 0.6431
26
