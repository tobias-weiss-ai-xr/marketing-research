---
title: The Effects of Stress and Chatbot Services Usage on Customer Intention for Purchase on E-commerce
  Sites
url: https://doi.org/10.11648/j.ijdst.20241001.11
category: ai-marketing
subcategory: empirical
date: 2024-02
venue: International Journal on Data Science and Technology
authors:
- Abed Matini
- Stanley Lekata
- Boniface Kabaso
source: openalex-oa
pdf_url: https://article.sciencepg.com/pdf/j.ijdst.20241001.11
pages: 10
chars: 27688
fetched_at: '2026-11-08T19:44:10+00:00'
kb_version: 1
---

# The Effects of Stress and Chatbot Services Usage on Customer Intention for Purchase on E-commerce Sites

International Journal on Data Science and Technology
2024, V ol. 10, No. 1, pp. 1-10
https://doi.org/10.11648/j.ijdst.20241001.11

*Corresponding author:
Received: 7 September 2023; Accepted: 9 January 2024; Published: 20 February 2024

Copyright: © The Author(s), 2024. Published by Science Publishing Group. This is an Open Access article, distributed
under the terms of the Creative Commons Attribution 4.0 License (http://creativecommons.org/licenses/by/4.0/), which
permits unrestricted use, distribution and reproduction in any medium, provided the original work is properly cited.

Research Article
The Effects of Stress and Chatbot Services Usage on
Customer Intention for Purchase on E-commerce Sites
Abed Matini, Stanley Lekata, Boniface Kabaso*
Faculty of Information Technology, Cape Peninsula University of Technology, Cape Town, South Africa

Abstract
In the rapidly evolving digital marketplace, customer service has become a critical factor influencing consumer behaviour. With
the advent of Artificial Intelligence (AI), particularly chatbots, customer service companies are increasingly leveraging
technology to enhance user experience. This study explores the relationship between customer emotions, detected during
interactions with e -commerce chatbots, a nd their subsequent purchase intentions. Emotion detection within Human -Computer
Interaction (HCI) is a vital area of research, as specific emotions, such as joy or frustration, can significantly impact mar keting
effectiveness and consumer decision-making. This research aims to understand how emotional responses to chatbot interactions
can predict customer's intention to purchase, thereby offering insights for businesses to optimize their AI-driven customer service
strategies. The study analyzes four divers e datasets – EmotionLines, CARER, GoEmotion, and EmotionPush – to identify
emotion-labelled sentences indicative of purchase intention. Our findings reveal that Neutral and Joyful emotions are
predominant in influencing customers' purchase intentions, highlighting the importance of understanding these emotional states
in e-commerce settings. While Neutral emotion is most influential, Joy consistently plays a significant role in positive customer
engagement. This research underscores the need for e -commerce businesses to focus on emotional intelligence in chatbots,
enhancing customer experience and potentially driving sales. Future research directions include examining real chatbot-customer
interactions to further understand the impact of AI-driven customer service on consumer emotions and behaviours.
Keywords
Artificial Intelligence, Chatbots, Customer Engagement, Customer Service, E -commerce, Purchase Intentions, User Emotions

1. Introduction
Customer service companies have shown significant i n-
terest in integrating Artificial Intelligence (AI) into their
systems. A chatbot is an AI application with the ability to
initiate a conversational session with a human partner, mai n-
tain, and handle a complex and nuanced conversation in na t-
ural language [1]. The primary reason businesses are keen on
chatbots is their potential to reduce customer service costs
and handle multiple users simultaneously [2].
Emotion detection in Human -Computer Interaction (HCI)
has been a subject of research for over two decades [3]. Pre-
vious research indicates that certain emotions, such as anger,
are particularly relevant in marketing. Anger suggests that
the customer is engaged and has an optimistic outlook on the
future, making it more likely to lead to action [4]. Therefore,
understanding emotio ns and their significance in the human
decision-making process can be beneficial for commercial

International Journal on Data Science and Technology http://www.sciencepg.com/journal/ijdst

2
entities, institutions, and organizations.
1.1. Previous Work
Research has been conducted on customer purchase inte n-
tion with chatbots [5, 6]. It has been found  that factors like
security, reliability, an enjoyable chatbot experience, and inti-
macy have a positive impact on encouraging users to engage
in more conversations with chatbots, consequently increasing
purchase intentions. Additionally, experiencing positive emo-
tions through product reviews and personalized advertisements
can also influence purchasing decisions [7, 8].
1.2. Problem Statement
The rapid growth of companies' interest in utilizing cha t-
bots in their customer service departments and the high e x-
pectations placed on chatbots to comprehensively address
customer requests [9] have driven chatbot developers to e n-
hance chatbot performance. Despite the progress made in
improving chatbot efficiency in information detection, ana l-
ysis, and user responses, e motion detection, particularly
stress detection, is lacking in e -commerce chatbots. Impl e-
menting stress detection algorithms can empower chatbots to
discern both explicit and implicit information from users.
The absence of emotion detection in e -commerce c hatbots
may impact user engagement rates.
1.3. Aim and Objectives
The aim of this paper is to detect and classify potential
buyers via automated chatbots to present offers at moments
that would entice them to make a purchase. To achieve this
aim, two main objectives have been established. The first
objective is to identify datasets that have been labe lled with
emotions and pinpoint sentences that express an intention to
purchase. The second objective is to assess the emotions
associated with these sentences to test our hypothesis.
1.4. Hypothesis
1.4.1. Background
Several studies [10, 11] have identified a significant rel a-
tionship between stress and compulsive buying. Since stress
detection algorithms have recently been applied to m i-
croblogs [12, 13], it is reasonable to assume a connection
between stressed users interacting with chatbots and their
intention to make a purchase. Studies by  [4] support this a s-
sumption, suggesting that certain emotions are likely to i n-
fluence the decision-making process.
1.4.2. Null Hypothesis Ho
There is no relationship between user emotion and their
online buying decision-making.
1.4.3. Alternative Hypothesis H1
User emotions play a significant role in online purchasing
decision-making.
2. Method
A quasi-experimental design is a type of experimental d e-
sign that utilizes observational data to address research que s-
tions and causal hypotheses [14]. Quasi -experimental d e-
signs are often employed when it is neither possible nor et h-
ical to randomly assign participants to treatment and control
groups, or when it is impractical to do so. These designs can
be used to investigate both cause-and-effect relationships and
associations. In a cause -and-effect relationship, the ind e-
pendent variable is the cause, and the dependent variable is
the effect. In an association, both variables are correlated, but
there is no causal relationship.
The ideal experimental design for our research would i n-
volve one or more controlled groups of customers to whom
we offer a sale specifically and record their acc eptance or
rejection while observing their emotional state for our r e-
search. Unfortunately, we do not have access to such datasets.
Consequently, we are unable to pretest our dataset. Due to
our limitations, the only viable option for a true experimental
design is to observe whether the purchase occurs in a neutral
or non-neutral emotional state. Therefore, we compare these
neutral and non-neutral emotional states.
The limitation of this study pertains to purchases labe lled
as "Neutral." All four datasets u sed in our research were
compiled from previous studies. In these studies, individuals
responsible for labe lling each sentence with relevant em o-
tions were instructed to select "neutral" emotions when they
could not fully comprehend the emotional content of  the
sentence, when mixed emotions were present, when no pr e-
dominant emotions were discernible, or when emotions were
absent. Thus, a sentence labe lled as "neutral" does not ne c-
essarily mean the sentence itself is neutral; it signifies that
the emotional state of the sentence could not be conclusively
determined. Moreover, we sought datasets resembling cha t-
bot conversations, and these datasets consist mostly of short
sentences, often lacking sufficient context to indicate a pu r-
chase. Consequently, there mig ht be purchases with em o-
tional content in the overall chat session, but such emotions
cannot be attributed to individual sentences.
In our experimental design, we did not randomly select
our datasets and purchase records but used the entire dataset.
3. Procedures
3.1. Data Collection
In our paper, we had four groups of datasets, each extracted
from previous researchers who had made their datasets pu b-
licly available. These datasets met two critical criteria. First,

International Journal on Data Science and Technology http://www.sciencepg.com/journal/ijdst

3
they took the form of chat conversations ge nerated from chat
histories or a series of comments or tweets derived from the
history of social media websites. Second, these datasets had
been annotated with relevant emotions, including joy, sadness,
anger, etc. Furthermore, the detected emotions in the se d a-
tasets were attributed to humans, not another machine or soft-
ware, ensuring the reliability of the emotion detection. During
our literature review process, we identified four datasets that
met these specifications: EmotionLines [15], CARER [16],
GoEmotions [17], and EmotionPush [18].
Table 1. Collected Datasets Description.
# Dataset Brief Description
1 EmotionLines Dialogues extracted from the Friends TV Series are labelled by Basic emotion: Anger, Disgust, Fear, Happiness, Sadness, and Surprise. The dialogue emotions were identified by humans in a survey.
2 CARER Tweets extracted from the tweeter. They are in English Language and their emotions were identified by their authors' given hashtags. Emotions are Anger Anticipation, Disgust, Fear, Joy, Sadness, Surprise, and Trust.
3 GoEmotions The datasets are extracted from Reddit comments based on 27 emotions.
4 EmotionPush Messages are extracted from Facebook Messenger with 7 emotions: Joy, Anticipation, neutral, tired, anger, fear, and sadness

3.2. Filtering Datasets Based on Purchase
Intentions
3.2.1. EmotionLines
In the EmotionLines dataset, we had over 10,800 chat d i-
alogues. Approximately 19 of them indicated an intention to
make a purchase. Out of these 19 sentences, Neutral and
Joyful emotions played the most significant roles, with Jo y-
ful having 8 instances, Neutral with 6, Mad with 4, and
Powerful with 1 showing purchase intentions. Several se n-
tences were identified with other emotions, making it unclear
which precise emotion was associated with the sentence.
However, this did not affect the overall result as the count
remained at zero. The EmotionLines dataset indicated that
Neutral, Joy, and Surprise appeared more frequently.
3.2.2. CARER
The CARER dataset contained over 11,300 tweets, which
had been labe lled with relevant emotions through hashtags
by their authors. Our analysis revealed that 66 sentences e x-
hibited an intention to engage in a transaction. Out of these
66 tweets, Joy played the most significant role with 32 i n-
stances of purchase intentions, followed by Sadness with 15
intentions to buy. Fear was the third with 10 intentions, A n-
ger had 7, and Surprise had only 2. Similar to EmotionLines,
tweets with unknown emotions were labelled as "others," and
again, the count remained at zero.
3.2.3. GoEmotions
GoEmotion had over 211,200 comments from Reddit,
with 318 of these comments indicating an intention to a c-
quire goods or services. Neutral was the predominant em o-
tion in this dataset, with 251 intentions to buy. Joy and A n-
ger were close in results, with Joy at 24 and Anger at 21.
Sadness had 13 intentions, while Fear and Nervousness had 5
and 4 purchase intentions, respectively.
3.2.4. EmotionPush
EmotionPush include d over 10,900 Facebook messages,
with 34 messages showing an intention to obtain a product or
service. Neutral had the most instances, with 31 purchase
intentions, while Joy was a distant second with 3. Other
emotions like Anticipation, Tiredness, Anger, F ear, and
Sadness had zero purchase intentions.
4. Results
4.1. Comparing Results in Four Datasets
Table 1 and Figure 1 illustrate the comparison of users'
neutral and emotional states in our four datasets. In Em o-
tionLines, six purchases occurred when users ' emotions were
neutral, while thirteen purchases occurred when users' em o-
tions were non -neutral, which included Joyful, Mad, Powe r-
ful, and others. In the CARER dataset, 66 purchases took
place in emotional states such as Joy, Sadness, Fear, Anger,
and Sur prise, with no records of neutral emotions. In the
GoEmotion dataset, 251 purchases were associated with
Neutral emotions, while 67 purchases occurred when users
had non -neutral emotions, including Anger, Fear, Joy,
Nervousness, and Sadness. Lastly, in Emo tionPush, 31 pu r-
chases were recorded in a neutral emotional state, with only
3 emotional purchases. In EmotionPush, non -neutral em o-
tions included Joy, Anticipation, Tiredness, Anger, Fear, and
Sadness.

International Journal on Data Science and Technology http://www.sciencepg.com/journal/ijdst

4

Table 2. Neutral and Non-neutral Purchase in our Four Datasets.
Datasets Purchased Neutral Emotion Non-neutral Emotion
EmotionLines Yes 6 13
CARER Yes 0 66
GoEmotions Yes 251 67
EmotionPush Yes 31 3

Figure 1. Comparing Users' Neutral and Emotional State on Purchase Intention.
4.2. Hypothesis Testing
4.2.1. EmotionLines
We rejected the alternative hypothesis since the dataset
indicated that Neutral was among the top two emotions with
an impact on purchase intention. While Joy ranked as the
primary emotion influencing purchase intention, Neutral
came in second, and Mad was  third. Additionally, there were
a total of six instances of neutral emotions, while there were
thirteen instances of non-neutral emotions. Consequently, we
could not accept the alternative hypothesis and had to reject
it. Table 3 displays the percentage o f purchase intentions in
the EmotionLines dataset.
Table 3. EmotionLines vs Purchase Intention by percentage.
Count of Emotion Column Labels
Row Labels No YES Grand Total
Neutral 16.67% 83.33% 100.00%
Non-neutral Emotion 7.69% 92.31% 100.00%
Grand Total 10.53% 89.47% 100.00%
Figure 2 shows our result in a Pivot Chart.

International Journal on Data Science and Technology http://www.sciencepg.com/journal/ijdst

5

Figure 2. EmotionLines vs Purchase Intention PivotChart.
Table 4 illustrates the crosstabulation of Emotion and Purchase Intention in the EmotionLines dataset. It presents the distr i-
bution of purchase intentions among both Neutral and Non-neutral Emotions, represented as percentages.
Table 4. EmotionLines & Purchase Intention Crosstabulation.
Emotion * Purchase intention Crosstabulation

Purchase intention
Total
No Yes
Emotion
Neutral Count 1 5 6
% within Emotion 16.7% 83.3% 100.0%
Non-neutral Emotion
Count 1 12 13
% within Emotion 7.7% 92.3% 100.0%
Total
Count 2 17 19
% within Emotion 10.5% 89.5% 100.0%
Table 5 displays the results of the chi -square test conducted on the EmotionLines dataset. This table provides statistical i n-
formation regarding the association between Emotion and Purchase Intention, assessing the significance of this relationship.
Table 5. EmotionLines Chi-square Tests.
Chi-Square Tests
 Value df Asymptotic Significance (2-sided) Exact Sig. (2-sided) Exact Sig. (1-sided)
Pearson Chi-Square .351a 1 .554
Continuity Correctionb .000 1 1.000
Likelihood Ratio .329 1 .566

International Journal on Data Science and Technology http://www.sciencepg.com/journal/ijdst

6
Chi-Square Tests
 Value df Asymptotic Significance (2-sided) Exact Sig. (2-sided) Exact Sig. (1-sided)
Fisher's Exact Test    1.000 .544
N of Valid Cases 19
a. 2 cells (50.0%) have expected count less than 5. The minimum expected count is.63.
b. Computed only for a 2x2 table
The P-value (0.554) was greater than the level of signif i-
cance (0.05). Consequently, we retained the null hypothesis
and concluded that there was no relationship between emotion
and purchase intention. In other words, emotion did not i n-
fluence purchase intention.
4.2.2. Emotion Lines
We were unable to conduct the Chi -squared test on this
dataset. The significant difference between this dataset and
the other three was the absence of the Neutral label, which
was replaced with "Others," resulting in zero insta nces in our
results. However, Joy had 32 instances, and Sadness had 14.
This dataset indicated 0 for Neutral emotions and 66 for
Non-neutral emotions.
4.2.3. Go Emotion
We rejected the alternative hypothesis since the dataset
revealed that Neutral was the dominant emotion influencing
purchase intention, with a count of 251, compared to Joy with
24 and Anger with 21. Table 8 also displayed 251 instances of
Neutral emotion and 67 instances of non -neutral emotion.
This dataset highlighted that, after Neutral, Joy continued to
play a significant role in purchase intention. This similarity
was observed between this dataset and EmotionLines and
CARER. Table 5 shows purchase intention by percentage o f
Go-Emotion.
Table 6. Go-Emotion vs Purchase Intention by Percentage.
Count of Emotion Column Labels
Row Labels No YES Grand Total
Neutral 29.13% 70.87% 100.00%
Non-neutral Emotion 51.52% 48.48% 100.00%
Grand Total 34.56% 65.44% 100.00%
Figure 3 shows our result in a Pivot Chart

Figure 3. Go-Emotion vs Purchase Intention PivotChart.

International Journal on Data Science and Technology http://www.sciencepg.com/journal/ijdst

7

Table 7 presents the crosstabulation analysis conducted on
the GoEmotion dataset. This table showcases the interplay
between Emotion and Purchase Intention within the dataset,
displaying the distribution of purchase intentions among di f-
ferent emotional states.
Table 7. GoEmotion & Purchase Intention Crosstabulation.
Emotion * Purchase Intention Crosstabulation

Purchase Intention
Total
No Yes
Emotion
Neutral
Count 30 73 103
% within Emotion 29.1% 70.9% 100.0%
Non-neutral Emotion
Count 17 16 33
% within Emotion 51.5% 48.5% 100.0%
Total
Count 47 89 136
% within Emotion 34.6% 65.4% 100.0%
Table 8 showcases the results of the chi -square tests performed on the GoEmotion dataset. This table provides statistical i n-
sights into the relationship between Emotion and Purchase Intention within the dataset, assessing the significance of this a sso-
ciation.
Table 8. Go-Emotion Chi-Square Tests.
Chi-Square Tests
 Value df Asymptotic Significance (2-sided) Exact Sig. (2-sided) Exact Sig. (1-sided)
Pearson Chi-Square 5.539a 1 .019
Continuity Correctionb 4.594 1 .032
Likelihood Ratio 5.358 1 .021
Fisher's Exact Test    .022 .017
N of Valid Cases 136
a. 0 cells (0.0%) have expected count less than 5. The minimum expected count is 11.40.
b. Computed only for a 2x2 table
The P -value (0.19) was greater than  the level of signif i-
cance (0.05). Therefore, we retained the null hypothesis and
concluded that there was no relationship between emotion and
purchase intention. In other words, emotion did not influence
purchase intention.
4.2.4. Emotion Push
We rejected the alternative hypothesis for this dataset,
which indicated that Neutral was the predominant emotion
influencing purchase intention. Neutral had a count of 31,
while the second emotion, Joy, had only 3 instances of
purchase intention. All the other emotions combined
showed zero purchase intentions. Table 8  provide s a
comparison between 31 instances of Neutral Emotion s and
3 of Non-neutral emotions. This dataset also highlighted
the significant role played by Joy in purchase intention.
Table 9 shows purchase intention by the percentage o f
Emotion Push.

International Journal on Data Science and Technology http://www.sciencepg.com/journal/ijdst

8
Table 9. EmotionPush vs Purchase Intention in Percentage.
Count of Emotion Column Labels
Row Labels No Yes Grand Total
Neutral 18.57% 81.25% 100.00%
Non-neutral Emotion 33.33% 66.67% 100.00%
Grand Total 20.00% 80.00% 100.00%
Figure 4 shows our result in a Pivot Chart

Figure 4. Emotion Push vs Purchase Intention Pivot Chart.
Table 10 illustrates the crosstabulation analysis of Emotion and Purchase Intention in the EmotionPush dataset. This table
reveals the distribution of purchase intentions across different emotional states, shedding light on the relationship between these
variables.
Table 10. Purchase Intention & Emotion Crosstabulation.
Purchase intention * Emotion Crosstabulation

Emotion
Total
Neutral Non-neutral Emotion
Purchase intention
No Count 6 1 7
% within Purchase intention 85.7% 14.3% 100.0%
Yes
Count 26 2 28
% within Purchase intention 92.9% 7.1% 100.0%
Total
Count 32 3 35
% within Purchase intention 91.4% 8.6% 100.0%

International Journal on Data Science and Technology http://www.sciencepg.com/journal/ijdst

9
Table 11 presents the results of the chi-square tests conducted on the EmotionPush dataset. This table offers statistical insights
into the relationship between Emotion and Purchase Intention within the dataset, assessing the significance of this relations hip
through statistical analysis.
Table 11. EmotionPush Chi-Square Tests.
Chi-Square Tests
 Value df Asymptotic Significance (2-sided) Exact Sig. (2-sided) Exact Sig. (1-sided)
Pearson Chi-Square .365a 1 .546
Continuity Correctionb .000 1 1.000
Likelihood Ratio .324 1 .569
Fisher's Exact Test    .499 .499
N of Valid Cases 35
a. 2 cells (50.0%) have an expected count of less than 5. The minimum expected count is 60.
b. Computed only for a 2x2 table
The P-value (0.546)  was greater than the level of signif i-
cance (0.05). Consequently, we retained the null hypothesis
and concluded that there was no relationship between emotion
and purchase intention. In other words, emotion did not i n-
fluence purchase intention.
When compar ing all four datasets, it was evident that
although Joy was not the primary emotion influencing pu r-
chase intention, it consistently played a significant role,
particularly after the Neutral emotion. This observation
aligned with our findings from the syste matic literature
review, which emphasized the impact of positive mood on
purchase intention.
5. Conclusion
We had identified four datasets, each from entirely diffe r-
ent sources (EmotionLines, CARER, GoEmotion, and Em o-
tionPush). This diversity allowed us to  test our hypothesis
across a range of sources. We filtered the sentences and
identified those indicating a purchase through observational
methods, utilizing words with precise purchase -related
meanings, as well as sentences with multiple interpretations
that could imply a purchase.
The results of our hypothesis testing led to the rejection
of our alternative hypothesis. The testing revealed that the
Neutral emotion was the primary emotion associated with
purchase intention. Additionally, Joy emerged as the  se-
cond most influential emotion affecting purchase intention.
6. Limitations and Future Directions
We selected four datasets with characteristics rese m-
bling chatbot conversations to test our hypothesis. Ho w-
ever, having access to actual chat histories of c ustomers
with a customer service chatbot would provide valuable
insights into customer interactions with computers and
their emotional dynamics. Since customer service often
deals with complaints and technical queries, many detected
emotions in the chats m ay include anger, frustration, or
disappointment. Nonetheless, handling customer requests
and successfully resolving their issues could potentially
lead to changes in emotional states during the course of the
conversation.
Conflicts of Interest
The authors declare no conflicts of interest.
References
[1] A. Argal, S. Gupta, A. Modi, P. Pandey, S. Shim, and C. Choo,
“Intelligent Travel Chatbot for Predictive Recommendation in
Echo Platform,” pp. 176–183, 2018.
[2] B. R. Ranoliya, N. Raghuwanshi, and S. Singh, “Chatb ot for
university related FAQs,” in 2017 International Conference on
Advances in Computing, Communications and Informatics,
ICACCI 2017, 2017.
https://doi.org/10.1109/ICACCI.2017.8126057
[3] R. Kaiser and K. Oertel, “Emotions in HCI – An Affective
E-Learning System,” Computer (Long. Beach. Calif). , pp.
105–106, 2006.
[4] A. Seyeditabari, U. N. C. Charlotte, and U. N. C. Charlotte,
“Emotion Detection in Text : a Review,” 2018.

International Journal on Data Science and Technology http://www.sciencepg.com/journal/ijdst

10
[5] K. Jiang, M. Qin, and S. Li, “Chatbots in retail: How do they
affect the continued use an d purchase intentions of Chinese
consumers?,” J. Consum. Behav., vol. 21, no. 4, pp. 756 –772,
Jul. 2022, https://doi.org/10.1002/CB.2034
[6] S. Siripipatthanakul, W. Nurittamont, B. Phayaphrom, and S.
Nuanchaona, “Factors affecting consumer’s purchase intention
of chatbot commerce in Thailand,” Int. J. Business, Mark.
Commun., vol. 1, no. 3, pp. 1–13, 2021.
[7] L. Grigorios, S. Magrizos, I. Kostopoulos, D. Drossos, and D.
Santos, “Overt and covert customer data collection in online
personalized advertising: The rol e of user emotions,” J. Bus.
Res., vol. 141, no. March, pp. 308–320, 2022,
https://doi.org/10.1016/j.jbusres.2021.12.025
[8] A. Xu, Z. Liu, Y . Guo, V . Sinha, and R. Akkiraju, “A new
chatbot for customer service on social media,” in Conference
on Human Factors  in Computing Systems - Proceedings,
Association for Computing Machinery, May 2017, pp. 3506 –
3510. https://doi.org/10.1145/3025453.3025496
[9] J. Zamora, “Rise of the Chatbots : Finding a Place for Artificial
Intelligence in India and US,” roceedings 22nd Int. Conf. Intell.
User Interfaces Companion, pp. 109–112, 2017,
https://doi.org/10.1145/3030024.3040201
[10] S. Dawson, P. H. Bloch, and N. M. Ridgway, “Shopping
Motives, Emotional States, and Retail Outcomes,” J. Retail. ,
vol. 66, no. 4, p. 408, 1990, [Online]. Available:
http://search.ebscohost.com/login.aspx?direct=true&db=buh&
AN=4667693&site=ehost-live
[11] A. Saraneva, M. Sääksjärvi, A. Saraneva, and M. Sa, “Young
compulsive buyers and the emotional roller -coaster in
shopping,” 2008, https://doi.org/10.1108/17473610810879657
[12] H. Lin et al., “Psychological stress detection from cross-media
microblog data using Deep Sparse Neural Network,” Proc. -
IEEE Int. Conf. Multimed. Expo , vol. 2014 -Septe, no.
Septmber, pp. 1–6, 2014,
https://doi.org/10.1109/ICME.2014.6890213
[13] R. G. Pillai, M. Thelwall, and C. Orasan, “Detection of Stress
and Relaxation Magnitudes for Tweets,” vol. 2, pp. 1677–1684,
2018.
[14] H. White and S. Sabarwal, “Quasi -Experimental Design and
Methods,” no. 8, 2014.
[15] S. Y . Chen, C. C. Hsu, C. C. Kuo, T. H. K. Huang, and L. W. Ku,
“Emotionlines: An emotion corpus of multi -party
conversations,” Lr. 2018 - 11th Int. Conf. Lang. Resour. Eval.,
pp. 1597–1601, 2019.
[16] E. Saravia, H. C. Toby Liu, Y . H. Huang, J. Wu, and Y . S. Chen,
“Carer: Contextualized affect representa tions for emotion
recognition,” Proc. 2018 Conf. Empir. Methods Nat. Lang.
Process. EMNLP 2018, pp. 3687–3697, 2018,
https://doi.org/10.18653/v1/d18-1404
[17] D. Demszky, D. Movshovitz -Attias, J. Ko, A. Cowen, G.
Nemade, and S. Ravi, “GoEmotions: A Dataset of
Fine-Grained Emotions,” pp. 4040–4054, 2020,
https://doi.org/10.18653/v1/2020.acl-main.372
[18] C. Y . Huang and L. W. Ku, “EmotionPush: Emotion and
Response Time Prediction Towards Human -Like Chatbots,”
2018 IEEE Glob. Commun. Conf. GLOBECOM 2018 - Proc.,
2018, https://doi.org/10.1109/GLOCOM.2018.8647331
