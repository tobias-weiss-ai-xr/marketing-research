---
title: Analysis of Consumer Behavior Through Eye-Tracking Monitoring
url: https://doi.org/10.1007/978-3-031-81962-9_18
category: consumer-behavior
subcategory: measurement
date: 2025-01
venue: Springer proceedings in business and economics
authors:
- Despoina Taskoudi
- Evangelos Kehris
- George Karavasilis
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1007/978-3-031-81962-9_18.pdf
pages: 10
chars: 19315
fetched_at: '2026-11-08T17:54:45+00:00'
kb_version: 1
---

# Analysis of Consumer Behavior Through Eye-Tracking Monitoring

Analysis of Consumer Behavior Through
Eye-Tracking Monitoring
Despoina Taskoudi, Evangelos Kehris, George Karavasilis,
and Vasiliki Vrana
Abstract Eye tracking technology is valuable in consumer behavior research, as
it offers measurements of visual attention, which are crucial for understanding
purchasing decisions. Previous studies suggest that consumers’ gaze plays a critical
role in preference formation. However, inconsistencies in ﬁndings highlight the need
for further investigation. This paper aims to examine gaze behavior, including ﬁxation
duration, gaze transitions, and saccades, in the context of product placement. Using
the Gaze Recorder application, the study reveals that participants initially focus on
the left side of a screen, indicating a preference that marketers can exploit by placing
key products there. Additionally, the right side, where participants end their viewing,
is ideal for high-impact content to leave a lasting impression. The ﬁndings emphasize
the complexity of interpreting visual attention and the necessity of complementary
methods to fully understand consumer behavior and decision-making.
Keyword Consumer behavior · Eye-tracking · Gaze recorder
1 Introduction
Eye tracking is a technique used to identify a user’s visual focus by monitoring the
direction of their gaze [1] and determining where and how they direct their attention
[2]. It also measures the duration of time a user spends looking at something of
interest and tracks their eye movements [ 1], which are often classiﬁed as ﬁxations
and saccades. Fixation happens when a user gazes at and concentrates on a particular
element, showing their interest in certain images or text while navigating a web page.
In contrast, saccades are quick eye movements between ﬁxation points. They indicate
how many ﬁxations occur from the starting point until the user ﬁnds their target. A
large number of saccades suggests a longer search process [ 3].
Eye-tracking technology has been widely used in consumer behavior research due
to its ability to provide objective and precise measurements of visual attention and
D. Taskoudi · E. Kehris · G. Karavasilis · V. V r a n a (B)
International Hellenic University, Thermi, Thessaloniki, Greece
e-mail: vrana@ihu.gr
© The Author(s) 2025
A. Kavoura et al. (eds.), Strategic Innovative Marketing and Tourism, Springer
Proceedings in Business and Economics, https://doi.org/10.1007/978-3-031-81962-9_18
163

164 D. Taskoudi et al.
has numerous implications in terms of understanding consumer purchasing decisions
[4, 5]. Previous studies [ 6, 7] suggest that the consumer’s gaze is actively involved
in preference formation. Goyal, Miyapuram, and Lahiri [ 6] claimed that a consumer
is more likely to purchase the item they spend the most time viewing. This creates a
positive feedback loop between what consumers focus on and what consumers come
to prefer. Numerous studies have also explored various parameters, attributes, and
potential determinants of consumer attention and decision-making [8–10]. However,
the ﬁndings are often inconsistent, highlighting the need for further research [ 10].
The aim of this study is to investigate gaze characteristics (number of ﬁxations,
ﬁxation duration, number of gaze transitions, Saccades) when potential consumers
look at products.
2 Methodology
The experiment is based on a gaze-tracking application which (a) displays two prod-
ucts on the computer screen, one on the left side of the screen and one on the right and
(b) records the participant’s gaze using a webcam as they look at the two products.
Before the experiment, clear instructions were given to each participant. All sessions
were recorded without violating any personal data.
To conduct the experiment, a convenient sample of 50 skilled participants with
extensive computer experience were selected. The sample consists of 25 men and 25
women. The participants were university students aged between 18 and 25 years old.
The products (boxes of cereals) were chosen to have distinctive differences in their
appearance: one product package employed vivid colors and a cartoon ﬁgure while
the other package displayed a photograph of the product against a white background
(Fig. 1).
Fig. 1 A representation of the two product boxes that demonstrates the basic elements and colors

Analysis of Consumer Behavior Through Eye-Tracking Monitoring 165
Once the participant is seated in front of the screen, the camera is adjusted to
focus on their eye, ensuring they are positioned at the correct height and distance.
Detailed explanations about the upcoming procedure are then provided. The approach
leverages the Gaze Recorder application, a tool known for its accuracy and reliability
in capturing eye movement data [ 11]. The Gaze Recorder application is launched
after completing the calibration process. Calibration involves several markers that
the participant must follow with their gaze without moving their head, allowing
the program to automatically adjust to each individual’s characteristics. Once the
calibration is complete, the image of the two products under observation is displayed.
The duration of each session is measured from the moment the image of the two
products appears until the user completes the task, which is recorded with a precision
of 20 ms.
During the experiment, the Gaze Recorder system uses the user’s camera to track
and record their gaze, pinpointing the areas on the screen where their focus is directed.
After the experiment, the system generates both a static image and a dynamic heatmap
(video) to visualize the user’s gaze movements. Additionally, the system enables
the experiment administrator to deﬁne areas of interest on the experimental image,
represented as rectangular regions. Figure 2 illustrates three such areas of interest:
the yellow areas surrounding each box and the green area in the middle, between the
two boxes.
For each area of interest, the system provides the following information: (a) the
dwell time in the area (b) the timestamp of the ﬁrst glance, and (c) the number of
participants who viewed the area.
This allows to capture the total dwell time and the ﬁxation time for both the left
and right areas.
In addition, the experiment administrator also has access to a ﬁle that records
the gaze movements of each participant. Speciﬁcally, the log ﬁle generated by the
program contains a set of tuples (id, t, x, y), where: id is the experiment code, t is
Fig. 2 Encircling the boxes to record the viewing times and the ﬁrst glance

166 D. Taskoudi et al.
the time in milliseconds from the start of the experiment at which the recording was
made x, y are the coordinates of the point where the user’s gaze was focusing at time
t. Based on the recorded data ﬁle, various metrics related to viewing time, ﬁxation
time, and quick movements were calculated for each of the three areas of the image
(left box, central space, right box).
The following metrics were calculated:
• The number of gaze transitions between areas.
• The ﬁrst area the user viewed at the beginning of the experiment.
• The last area the user viewed at the end of the experiment.
• The total ﬁxation time in each of the three areas (i.e. when the gaze was stable,
ha
ving a dwell time greater than 100 ms).
• The total time of rapid gaze movements in each of the three areas, calculated as
the
sum of durations where the gaze moved quickly, with a dwell time of less than
100 ms.
3 Findings
To analyze how users’ gaze traversed the image, graphs were created to depict the
variation in the x-coordinate over time. First, detailed graphs were generated to
capture the precise changes in the x-coordinate. The right area (right box) corresponds
to the upper part of the diagram, the left area to the lower part, and the middle area
to the center (Fig. 3—left). These were followed by graphs highlighting only the
transitions between different areas. Red indicates long-duration gazes, green denotes
medium-duration gazes, and gray represents short-duration gazes (Fig. 3—right).
Figure 4a (left) depicts the ﬁrst area that participants look at. This indicates that
36 out of the 50 participants ﬁrst observe the left side of the screen, while none look
at the center. Figure 4b (right) illustrates the ﬁnal area observed by participants at the
end of the experiment. The majority appear to focus on the right side of the screen
as the session concludes.
One of the most critical parameters examined was the average viewing time of
the two boxes, left and right. Hypothesis H1 is central to the research, as it aims to
elucidate participants’ preferences for the two products.
H1: The average viewing times of the right box and the left box are equal.
As it is evident from Tables 1 and 2 and Fig. 5a, the viewing time of the left box
and the viewing time of the right box are approximately equal. The H1 is accepted.
The Pearson correlation coefﬁcient between the left and right box viewing time
(sec) indicates a rather moderate negative linear relation between the two variables
(Fig. 5b).
The duration of the ﬁrst gaze at an object is a critical indicator of an indi-
vidual’s attention and initial impressions. Given the signiﬁcance of visual attention
in decision-making and behavior, analyzing the differences in ﬁrst gaze duration can

Analysis of Consumer Behavior Through Eye-Tracking Monitoring 167
Fig. 3 Gaze movement from one area to another for user 27
ab first area
40
35
30
25
20
15
10
[-1, -0.14] [-0.14, 0.72]
0
36
14
19
29
2
[0.72, 1.58] [-1, -0.08] [-0.08, 0.84] [0.84, 1.76]
5
0
35
30
25
20
15
10
5
0
last area
Fig. 4 Area of the (a) ﬁrst (b) last look
Table 1 Analysis of viewing time (sec)
Left box viewing time Right box viewing time
Mean 7.7600 8.0522
Median 7.4350 7.7450
Standard Deviation 2.7926 2.6108

168 D. Taskoudi et al.
Table 2 Pair sample
correlations of viewing time N Correlation Sig
Left–right box viewing time 50 -0.562 0.000
Left box viewing time (sec)
Left box viewing time (sec)
05 2
0
5
10
20
15
4 6 8 10 12 14
2 4 6 8 10 12 14
Density
Density
10 15
r = –0.562
20
Left box viewing time (sec)
46 8 1 0 1 2 1 4 1 6
Right box viewing time (sec)
Right box viewing time (sec)
Right box viewing time (sec)
ab
Fig. 5 (a) Box plots of left and right box viewing time in sec. (b) scatter diagram, Pearson
correlation coefﬁcient, and densities of left and right box viewing time (sec)
offer valuable insights into the underlying cognitive processes and preferences of
individuals.
H2: The average duration of the ﬁrst gaze among participants is equal for both
box
es.
The difference between the time of the ﬁrst gaze at the left box and the right box
is statistically signiﬁcant. Therefore, the H2 is rejected. Even though the average
viewing times are similar, the longer initial gaze duration on the right box (H2
rejected) suggests that the right box might have a stronger initial draw.
Table 3 Analysis of ﬁrst gaze
Time of the ﬁrst gaze at the left box Time of the ﬁrst gaze at the right box
Mean 0.7092 1.3716
Median 0.4750 1.0300
Standard deviation 0.6020 1.4344
Table 4 Paired samples t test
t Degrees of freedom pv a l u e
Left–right box viewing time −2.769 49 0.008

Analysis of Consumer Behavior Through Eye-Tracking Monitoring 169
[4135, 6835]
0
2
4
6
8
10
12
14
16 16 16
fix area 1
13
3
2
18
(6835, 9535] (9535, 12235] (12235, 14935](14935, 17635]
0
5
10
15
20
25
30
35 35
fix area 2
34
7
1
40
[250, 1200] (1200, 2150] (2150, 3100] (3100, 4050] (4050, 5000]
0
5
10
15
20
6
20
15
fix area 3
8
1
25
[2752, 5452] (5452, 8152] (8152, 10852] (10852, 13552](13552, 16252]
ab
c
Fig. 6 Fixation time (>100 ms) for the (a) left, (b) middle, and (c) right area
Figure 6 presents the ﬁxation time (>100 ms) in the left, middle, and right area,
respectively. Most participants seem to ﬁx their gaze on the left area for a relatively
constant amount of time.
An independent samples t-test was conducted to investigate the following
hypotheses:
H3: The average ﬁxation time for the boxes on the right and left are equal between
men
and women.
H4: The average time of the ﬁrst view for the boxes on the right and left are equal
between
men and women.
Both hypotheses were supported, indicating that there is no signiﬁcant difference
in average ﬁxation time or average time of the ﬁrst view between men and women
for the boxes on either side.
At the end of the experiment, the number of participants who looked at the left,
center, and right areas was 19, 2, and 29, respectively.
The next hypothesis examined was:
H5: The participants’ gender and the direction of their last view at the end of the
e
xperiment are independent variables.
The results showed that 16 out of 25 men focused their last view on the right area,
while none of the 25 women looked at the center. This suggests that both men and
women tend to focus more on the right area at the end of the experiment, a trend
consistent across the overall sample.

170 D. Taskoudi et al.
[5, 11]
0
2
4
6
8
10
12
14
16
18
20
(11, 17] (17, 23] (23, 29] (29, 35]
1
6
13
18
12
transitions
Fig. 7 The number of gaze transitions from one area to another
The lack of signiﬁcant gender differences in viewing behavior indicates that
consumer designs should cater to all users equally, avoiding assumptions that
different genders have different preferences for visual content or layout.
Finally, differences in the number of gaze transitions made by participants during
the experiment were analyzed. Most participants, speciﬁcally 18 individuals, had
between 12 and 17 gaze transitions, while only one person exhibited more than 30
transitions (Fig. 7).
Finally, the saccades of participants in the left, middle, and right, areas were
recorded. In the middle area, a greater number of rapid movements are observed,
ranging from 0 to 258 (Fig. 8).
4 Conclusions
Eye tracking is a powerful tool in understanding consumer behavior because it
provides direct insights into what catches a consumer’s attention. By tracking where,
for how long, and in what sequence consumers focus on different elements of a visual
display, a deeper understanding can be gained of the factors that drive consumer
preferences and choices. Previous studies have investigated various parameters,
attributes, and determinants of consumer attention and decision-making. However,
the ﬁndings are often inconsistent, underscoring the need for further research to
clarify these relationships. This paper seeks to contribute to this area by exam-
ining gaze behavior in the context of product placement. The analysis of initial gaze
behavior indicates that a signiﬁcant majority of participants ﬁrst focus on the left side
of the screen. This suggests a clear preference for the left area when participants start

Analysis of Consumer Behavior Through Eye-Tracking Monitoring 171
[0, 35]
0
5
10
15
20
25
35
30
40
45 43
3
succ area 1
succ area 3
3
0 10
50
(35, 70] (70, 105] (105, 140] (175, 210](140, 175]
0
5
10
15
20
25
30
35
40
45 46
1 0 2 0 1
50
[0, 18] (18, 36] (36, 54] (54, 72] (72, 90] (90, 108]
a
[0, 86]
0
5
10
15
20
10
16
succ area 2
20
3
1 0
25
(86, 172] (172, 258] (258, 344] (430, 516](344, 430]
b
c
Fig. 8 Saccades of participants in the (a) left, (b) middle, (c) right areas
viewing the image. Marketers can use this insight to position key products in this area
to maximize visibility and engagement from the start. The tendency for participants
to end their viewing on the right side suggests that the ﬁnal area of focus might be
where the most important content should be placed. Given the longer initial gaze
duration on the right side and ﬁnal focus tendency, this area is ideal for content that
needs to make a lasting impression. However, interpreting these results is complex,
as visual attention alone does not fully explain consumer behavior. Questionnaires
can assess consumers’ willingness to purchase and help identify which information
they focus on when making buying decisions. Current research focused on consumer
behavior studied in a laboratory environment. Research has reported discrepancy in
the results between studies performed in the lab and studies conducted in a real
supermarket environment [10]. Future research combining a laboratory setup with a
real shop environment might be useful in drawing more conclusive conclusions.
References
1. Sari JN, Ferdiana R, Santosa PI, Nugroho LE (2015) An eye tracking study: exploration
customer
behavior on web design. In: Proceedings of the International HCI and UX conference
in Indonesia, pp 69–72. https://doi.org/10.1145/2742032.274257
2. Bojko A (2006) Using eye tracking to compare web page designs: a case study. J Usability
Stud
1:112–20
3. Poole A, Ball LJ (2006) Eye tracking in human-computer interaction and usability research:
current
status and future prospects. Encyclopedia of human-computer interaction. Igi-Global
https://doi.org/10.4018/978-1-59140-562-7.ch034

172 D. Taskoudi et al.
4. Khachatryan H, Rihn AL (2014) Eye-tracking methodology and applications in consumer
research.
Electron data Inf source UF/IFAS Ext, pp 1–5
5. Iloka BC, Anukwe GI (2020) Review of eye-tracking: a neuromarketing technique. Neuro-
science
Research Notes 3:29–34. https://doi.org/10.31117/neuroscirn.v3i4.61
6. Goyal S, Miyapuram KP , Lahiri U (2015) Predicting consumer’s behavior using eye tracking
data.
In: 2015 second international conference on soft computing and machine intelligence
(ISCMI), IEEE, pp 126–129. https://doi.org/10.1109/ISCMI.2015.26
7. Shimojo S, Simion C, Shimojo S, Scheier C (2003) Gaze bias both reﬂects and inﬂuences
preferences.
Nat Neurosci 6:1317–1322. https://doi.org//10.1038/nn1150
8. Bigné E, Llinares C, Torrecilla C (2016) Elapsed time on ﬁrst buying triggers brand choices
within
a category: a virtual reality-based study. J Bus Res 69:1423–1427. https://doi.org/10.
1016/j.jbusres.2015.10.119
9. Bialkova S, Grunert KG, Juhl HJ, Wasowicz-Kirylo G, Stysko-Kunkowska M, van Trijp HC
(2014)
Attention mediates the effect of nutrition label information on consumers’ choice.
Evidence from a choice experiment involving eye-tracking. Appetite 76:66–75. https://doi.
org/10.1016/j.appet.2013.11.021
10. Bialkova S, Grunert KG, van Trijp H (2020) From desktop to supermarket shelf: eye-tracking
e
xploration on consumer attention and choice. Food Qual Prefer 81:103839. https://doi.org/10.
1016/j.foodqual.2019.103839
11. Bojko A (2013) Eye tracking the user experience: a practical guide to research. Rosenfeld
Media,
Brooklyn New Y ork
Open Access This chapter is licensed under the terms of the Creative Commons Attribution 4.0
International License ( http://creativecommons.org/licenses/by/4.0/), which permits use, sharing,
adaptation, distribution and reproduction in any medium or format, as long as you give appropriate
credit to the original author(s) and the source, provide a link to the Creative Commons license and
indicate if changes were made.
The images or other third party material in this chapter are included in the chapter’s Creative
Commons license, unless indicated otherwise in a credit line to the material. If material is not
included in the chapter’s Creative Commons license and your intended use is not permitted by
statutory regulation or exceeds the permitted use, you will need to obtain permission directly from
the copyright holder.
