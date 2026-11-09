---
title: 'Bucovina Tourism through the Lens of Artificial Intelligence: Enhancing Regional Sustainability
  by Addressing Tourist Needs'
url: https://doi.org/10.5709/ce.1897-9254.599
category: ai-marketing
subcategory: review
date: 2026-09
venue: Contemporary Economics
authors:
- Angela Albu
- Paul Paşcu
source: openalex-oa
pdf_url: https://doi.org/10.5709/ce.1897-9254.599
pages: 13
chars: 39684
fetched_at: '2026-11-08T20:02:37+00:00'
kb_version: 1
---

# Bucovina Tourism through the Lens of Artificial Intelligence: Enhancing Regional Sustainability by Addressing Tourist Needs

www.ce.vizja.pl
414
This work is licensed under a Creative Commons Attribution 4.0 International License.
This article outlines the potential of artificial intelligence (AI) in enhancing the sustainability of
tourism in the Bucovina region, Romania, by analyzing tourists’ perceptions derived from online
reviews. By employing sentiment analysis and clustering techniques, the research identifies
patterns, segments tourists, and validates hypotheses related to their sentiments, preferences, and
experiences. The analysis incorporates 2,000 reviews collected from platforms such as TripAdvisor,
Booking, and Google Reviews, focusing on post-pandemic tourism trends. The findings indicate
that, although the sentiment expressed in reviews influences overall scores, the correlation is not
statistically significant. Cluster analysis revealed no significant differences in scores across tourist
segments, despite notable variations in sentiments. Tourists engaging in outdoor recreational
activities expressed more positive sentiments than those participating in cultural activities,
although their ratings were similar. Furthermore, thematic analysis using the Latent Dirichlet
Allocation (LDA) method highlighted overlaps between natural and cultural themes, suggesting
an integrated tourist experience in Bucovina. This study provides concrete recommendations for
stakeholders, emphasizing the need for personalized marketing strategies, improved infrastructure,
and the development of integrated tourism offerings that combine cultural heritage with natural
attractions. By leveraging AI-driven insights, our research aims to enhance tourist satisfaction and
promote Bucovina as a sustainable and attractive destination. These conclusions underscore the
transformative potential of AI in regional tourism development and decision-making.
Bucovina Tourism through the Lens of Artificial
Intelligence: Enhancing Regional Sustainability by
Addressing Tourist Needs
ABSTRACT
L83, L86, M31, Z32, C81.
KEY WORDS:
JEL Classification:
Bucovina, tourism data analytics, AI, tourist segmentation, seasonal tourism trends.
Department of Economics, Economic Informatics, and Business Management, University Stefan cel Mare of Suceava, Romania
Correspondence concerning this article should be addressed to:
Paul Paşcu, University Stefan cel Mare of Suceava, Romania.
E-mail: paul.pascu@usm.ro
Angela Albu
  and Paul Paşcu

Primary submission: 13.03.2024   |    Final acceptance: 18.06.2024
1. Introduction
In the last decade, Bucovina, a historic region in
Romania, has become increasingly well-known and vi-
sited by tourists. The area attracts both Romanian and
international visitors who come to explore its medieval
monasteries, part of the UNESCO heritage, as well as
its mountain landscapes and local traditions. Additio-
nally, tourists can attend local fairs and festivals, which
are being organized more frequently, and thus discover
the region’s unique local gastronomy. All of these ele -
ments make Bucovina a unique destination in Eastern
Europe (Paşcaniuc, 2019).
For local tourism service providers, the goal is to
make tourism in the area sustainable while mainta -
ining a high standard of quality so that visitors are de-

www.ce.vizja.pl
415
Bucovina Tourism through the Lens of Artificial Intelligence: Enhancing Regional Sustainability by Addressing Tourist Needs
This work is licensed under a Creative Commons Attribution 4.0 International License.
414
lighted by their experience and encouraged to return
(Wu et al., 2015).
In this context, reviews from tourists who have vi -
sited Bucovina can become extremely important. Opi-
nions posted on tourism platforms such as TripAdvi -
sor, Booking, or Google Reviews provide a clearer
insight into how visitors perceive services and their
overall experience in Bucovina (Bessière, 1998). These
reviews (Mellinas et al., 2016) represent a reliable so -
urce of information, indicating both satisfaction levels
and any issues encountered during their stay.
However, manually analyzing thousands of reviews
is an enormous task. For this reason, we decided to use
natural language processing (NLP), a branch of artifi -
cial intelligence, to efficiently analyze reviews and pro-
cess as much data as possible (McCloskey et al., 2024).
The advantage of using AI techniques is that, in ad-
dition to identifying tourists’ sentiments, we can also
uncover recurring themes within comments posted
on travel platforms (Puh & Bagić Babac, 2023). Such
information would be challenging to extract through
traditional statistical analysis methods.
This study proposes using AI technologies to analy-
ze the reviews of tourists who have visited Bucovina.
Our goal is to better understand the needs and expec -
tations of tourists to create a sustainable framework
for local tourism (Khan, 2020). We hope these findings
will contribute to improving the tourism offer, sup -
porting local tourism initiatives, and providing clear
recommendations to stakeholders involved in develo-
ping tourism in Bucovina.
2. Literature Review
Numerous studies have emphasized the relevance of
online reviews in shaping travel decisions and influ -
encing destination image (Marine-Roig & Clavé, 2015;
Xiang & Gretzel, 2010). User-generated content has
emerged as a powerful form of electronic word-of-mo-
uth (eWOM), often surpassing traditional marketing
in trust and influence (Sigala, 2016). Reviews reflect
not only tourist satisfaction but also unmet expecta -
tions, offering valuable insights for service quality im-
provement (Puh & Bagić Babac, 2023).
Prior research (e.g., Liu, 2012; Hu & Liu, 2004) has
focused on sentiment analysis techniques to measu -
re satisfaction levels, while studies such as Gretzel et
al. (2015) explored the smart tourism paradigm that
incorporates real-time data and AI for strategic deci -
sions. Trust in review authenticity, however, remains a
debated issue, affecting user perception and credibility
(He et al., 2013). The current study builds upon these
foundations, seeking to identify how tourist-generated
data can inform sustainable tourism planning in les -
ser-studied regions like Bucovina.
 3. Research Objectives
To gain a deeper understanding of the differences
in tourist perceptions (Ho et al., 2012) as they emerge
from online reviews analyzed via artificial intelligence
methods, we have formulated several working hypo -
theses (Li et al., 2017). These hypotheses, previously
used for more prominent locations, focus on diffe -
rences in the level of detail offered by each source,
the frequency of specific themes mentioned, and the
extent to which tourist sentiments correlate (or not)
with official statistical data. Our primary objective is to
determine whether online feedback analysis, proces -
sed using AI techniques and the Python programming
environment (Sarkar, 2019) through text analysis (Ag-
garwal & Zhai, 2012), can offer an alternative perspec-
tive or complement official statistical data.
To frame our analysis, we formulated four research
hypotheses grounded in previous studies and aligned
with our goal to understand tourist behavior and sa -
tisfaction patterns through AI-based methods. These
hypotheses address sentiment-score correlation, clu -
ster-based segmentation, activity-type satisfaction
differences, and thematic distinctions within reviews.
Hypothesis 1: There are no significant differences
between review sentiment and scores given by tourists.
We assume that data analyzed through AI techniqu-
es can offer a more detailed view of sentiment inter -
pretation (Liu, 2012), which may influence the given
score. We start from the hypothesis that tourist reviews
reflect unique experiences, which are often highly per-
sonal and tend to capture the specifics of each service
offered. On the other hand, official data focuses more
on general aspects and fails to highlight the detailed
aspects of service quality evaluation.
Hypothesis 2: Significant differences exist between
tourist segments identified through the clustering me-
thod.
Tourists posting online reviews often discuss spe -
cific aspects of local hospitality and their experiences,
while official statistics fail to capture such details. This
is due to the fact that tourism platforms allow tourists
to provide more detailed opinions about their personal
experiences. With this hypothesis, we aim to deter -
mine whether, based on reviews and scores given by
tourists, segments (Hennig et al., 2015) identified thro-
ugh clustering methods (such as K-Means) will show
significant differences in tourist behavior, preferences,
and satisfaction levels.
Hypothesis 3: Tourists who participate in engaging

416
Angela Albu, Paul Paşcu
10.5709/ce.1897-9254.599DOI:
CONTEMPORARY ECONOMICS
Vol. 20 Issue 3 414-4262026
activities are more satisfied than those focused strictly
on cultural experiences.
This hypothesis seeks to determine if positive sen -
timents expressed in online reviews can be correlated
with predominant themes, such as nature-based acti -
vities versus cultural activities, potentially becoming a
predictive factor for tourists returning to Bucovina. We
aim to find out if tourists who express satisfaction in
their reviews are more likely to revisit the area. Confir-
ming this hypothesis based on sentiment analysis could
become a useful tool to predict tourist loyalty to the de-
stination (Xiang et al., 2015).
Hypothesis 4: Reviews mentioning cultural and natu-
ral experiences are divided into distinct themes.
This hypothesis will be tested through theme analy-
sis using LDA (Latent Dirichlet Allocation) (Blei et al.,
2003) within the Python programming environment.
Such interpretations, even if not directly reflected in ag-
gregated statistics, can significantly influence the gene-
ral perception of tourism services (Gretzel et al., 2015).
4. Methodology
Our methodology involved several distinct sta -
ges (Manning et al., 2008), as shown in Figure 1,
including data collection, data preprocessing and
processing, sentiment analysis, clustering (K-Me -
ans), identification of recurring themes present in
review texts, hypothesis validation, and recommen-
dation formulation (Jurafsky & Martin, 2021.
5. Data Collection
Data was collected from three platforms: TripAdvi-
sor, Booking, and Google Reviews, which are popular
among tourists worldwide, including those visiting Bu-
covina (Xiang & Gretzel, 2010). These platforms pro -
vide extensive information about tourist experiences,
including reviews of tourist attractions, accommoda -
tions, gastronomy, other tourist attractions, and infra-
structure (Marine-Roig & Clavé, 2015). We analyzed
reviews posted between January 2022 and December
2023, totaling 2,000 entries. Of these, 43% originated
Figure 1
Research Methodology Flowchart

www.ce.vizja.pl
417
Bucovina Tourism through the Lens of Artificial Intelligence: Enhancing Regional Sustainability by Addressing Tourist Needs
This work is licensed under a Creative Commons Attribution 4.0 International License.
Table 1
Organization of the Collected Data
ID Date Review Score
1 2023.06.10 “I had a wonderful experience at the guesthouse.
Everything was great. ”
5
2 2023.05.21 “The services did not meet expectations, and
everything was a bit expensive. ”
3
3 2023.07.15 “The location is superb, but the cleanliness needs
improvement. The sheets were not changed daily. ”
4
4 2023.08.02 “The food was excellent, but we waited too long. ” 4
5 2023.09.10 “ A dream destination, but the prices are a bit high. ” 4
Table 2
ANOVA Detailed Results
Sentiment Mean Rating N
Positive 3.0018 1659
Neutral 2.8522 176
Negative 2.9878 165
Table 3
Organization of the Collected Data
Source Sum of Squares df Mean Square F Sig.
Between Groups 0.915859 2 0.457929 0.91585 0.400
Within Groups 1997
Total  1999
Figure 2
Number of Reviews vs Average Rating by Sentiment Category

418
Angela Albu, Paul Paşcu
10.5709/ce.1897-9254.599DOI:
CONTEMPORARY ECONOMICS
Vol. 20 Issue 3 414-4262026
from TripAdvisor, 31% from Google Reviews, and 26%
from Booking.com. Since Booking.com often focuses
on accommodation, we applied a relevance filter using
keywords related to tourism attractions, activities, and
gastronomy, ultimately retaining 1,734 reviews consi -
dered pertinent to broader tourism experiences in Bu -
covina (Zhao & Park, 2023).
To ensure the data’s relevance and usability, we chose
to include only reviews written in Romanian and En -
glish. This approach allowed us to avoid any potential
confusion arising from translation or interpretation
issues. Additionally, we decided to exclude reviews with
fewer than five words, as they would not provide suffi -
cient information for effective sentiment analysis (Pang
& Lee, 2008).
These records were organized in a database, as
shown in Table 1, after removing any personally iden -
tifiable information. Each entry was assigned a unique
ID, posting date, review text, and given score. Using this
database was essential to easily apply natural language
processing (NLP) techniques and other AI methods
(Bird et al., 2009). The file format chosen for the data -
base was CSV , as it is user-friendly and allows for effi -
cient data manipulation in programming environments
such as Python.
5.1. Data Preprocessing
The first step in processing the reviews began with
data cleaning, which involved removing semantically
irrelevant words (stop words), such as „and, ” „in, ” and
„is” . Next, we applied a text normalization algorithm,
removing punctuation marks and extra spaces, and per-
forming lemmatization of terms (Buttcher et al., 2010).
Through lemmatization, we reduced words to their
base form; for example, „hiking trip” became „hike. ”
We also used the TF-IDF (Term Frequency-Inverse Do-
cument Frequency) technique to transform the reviews
into vectors (Eisenstein, 2019). This method was neces-
sary to prepare the data for applying machine learning
algorithms, such as K-Means for clustering and LDA
for analyzing and extracting central themes.
5.2. Hypothesis Analysis
Hypothesis 1: The sentiment of reviews significantly
influences the scores given by tourists.
We calculated the mean scores for reviews based on
sentiment using a one-way ANOV A, and the results
are presented in Table 2. The ANOV A results showed
mean scores of 3.00 for positive reviews, 2.85 for neu -
tral reviews, and 2.99 for negative reviews. F = 0.92, p =
.40. These results indicate that there were no significant
differences in mean review scores based on review sen-
timent categories (Tabachnick & Fidell, 2019).
The interpretation of the F-statistic value shows that
it measures the differences between the analyzed gro -
ups (positive, neutral, and negative reviews) compared
to the variation within each group, with a high F-stati -
stic value indicating large differences between groups.
In this case, the F = 0.92 is relatively low, suggesting
that the variations between the average scores of re -
views with different sentiments are not large enough to
indicate significant differences between these groups.
Additionally, the p-value represents the probability
that the observed differences between groups occurred
by chance if the null hypothesis (which assumes no dif-
ferences between groups) is true. Generally, if the p-va-
lue < 0.05, the null hypothesis is rejected, suggesting
that significant differences exist between groups. For
this test, the p-value = 0.40 > 0.05, indicating that we
cannot reject the null hypothesis, as shown in Table 3.
Therefore, there is insufficient evidence to support
that the sentiment of reviews significantly influences
the scores given by tourists.
Based on these results, the ANOV A test conclusion
shows that there are no significant differences between
the average scores given based on the sentiment expres-
sed in reviews (positive, neutral, or negative). Although
there are slight variations between scores, they are not
large enough to be considered statistically significant
(Corder & Foreman, 2014). This suggests that, in the
case of the reviews analyzed, the emotional tone of the
reviews does not significantly influence the numerical
scores given by tourists.
The graph below provides a clearer view of score va-
riability and helps us see if there are significant differen-
ces between sentiment categories. The distributions for
positive and negative reviews are similar, almost identi-
cal, which may be an unexpected result, suggesting that
scores do not always reflect the emotional tone of the
reviews. Neutral reviews have a lower average, indica -
ting that tourists who do not express a clear sentiment
tend to give lower scores.
Figure 2 illustrates the distribution of average ratings
across the three sentiment categories. Although positi-
ve reviews have the highest mean rating (3.00), followed
closely by negative reviews (2.99), and neutral reviews
have the lowest mean rating (2.85), the differences are
small and were not statistically significant ( F = 0.92,
p = .40). Therefore, the figure should be interpreted
as descriptive rather than as evidence of a significant
relationship between review sentiment and rating. For
positive reviews, the average rating is higher than for
neutral or negative reviews, indicating a direct corre -

www.ce.vizja.pl
419
Bucovina Tourism through the Lens of Artificial Intelligence: Enhancing Regional Sustainability by Addressing Tourist Needs
This work is licensed under a Creative Commons Attribution 4.0 International License.
Figure 3
Number of Reviews vs Average Rating by Sentiment Category
Table 4
Top Terms by Cluster
Cluster 0 (frequency) Cluster 1 (frequency) Cluster 2 (frequency)
hiking 257 330
mountains 257
blown 147
away 147
beauty 147
natural 147
landscapes 147 230 149
incredible 147
craftsmanship 147
monasteries 147 325
Bucovina 391
views 366
mountain 279
historical 269
monasteries 267 294
trip 205
monasteries 202
must-visit 149
place 149
nature 149
lovers 149
history 149
enthusiasts 149
impressive 149
serene  149

420
Angela Albu, Paul Paşcu
10.5709/ce.1897-9254.599DOI:
CONTEMPORARY ECONOMICS
Vol. 20 Issue 3 414-4262026
Table 5
ANOVA Summary
Source Sum of Squares df Mean Square F Sig.
Between Groups 0.24483099 2 MS Between 0.244830 0.782860
Within Groups Residual SS n-3 MS Within
Total Total SS n-1
Figure 4
Frequency of Themes Appearing in Comments
Table 6
Outdoor vs Cultural Activities
Activity Type Mean Sentiment Mean Rating
Outdoor 0.451 2.998
Cultural 0.347 2.961

www.ce.vizja.pl
421
Bucovina Tourism through the Lens of Artificial Intelligence: Enhancing Regional Sustainability by Addressing Tourist Needs
This work is licensed under a Creative Commons Attribution 4.0 International License.
lation between positive sentiments and a higher rating.
For negative reviews, the „Average Rating” line shows
that tourists consistently gave lower scores, suggesting
an unsatisfactory experience. For neutral reviews, the
average rating is lower than that of positive reviews but
still higher than that of negative reviews, indicating a
balanced sentiment, reflecting experiences that were
neither exceptionally good nor exceptionally bad.
We also wanted to determine whether there was va -
riability in review sentiment over time or if it remained
constant. To this end, we created a distribution of re -
views by sentiment across time intervals (months) and
applied the chi-square test (Hu & Liu, 2004); the results
are shown in Figure 3.
According to this chart, positive reviews dominated
throughout the analyzed period, suggesting that to -
urists generally had good experiences in Bucovina. In
certain months, such as August 2022 and September
2022, there was a higher number of positive reviews, in-
dicating a period when tourists were more satisfied; this
could be attributed to the fact that these two months are
exceptionally beautiful in Bucovina. Negative reviews
fluctuated slightly from month to month but do not
show a clear trend of increase or decrease. For example,
in February 2022 and March 2023, there was a higher
number of negative reviews. These winter months may
affect infrastructure, with some roads being cleared of
snow later than expected, and some tourists might also
experience thermal discomfort.
In general, the summer months (June-August) show
a slight increase in positive reviews, likely due to the
tourist season when people are on holiday and positive
experiences are more common. During winter mon -
ths (December-February), there appears to be a slight
decrease in the total number of reviews and a relative
increase in negative reviews in some cases, which could
suggest more challenging conditions or other seasonal
dissatisfaction (Griffiths & Steyvers, 2004).
The ANOV A test result, as shown in Table 5, indica-
tes that the F-statistic value is 0.245, with an associated
p-value of 0.783. This suggests that there are no statisti-
cally significant differences between tourist clusters in
Figure 5
Mean Sentiment and Rating for Outdoor vs Cultural Activities

422
Angela Albu, Paul Paşcu
10.5709/ce.1897-9254.599DOI:
CONTEMPORARY ECONOMICS
Vol. 20 Issue 3 414-4262026
Table 7
Topics and Top Terms from Tourist Reviews in Bucovina
Topics Top terms words Frequences
Topic 0 average bit overall absolutely
landmarks worth historical
views trip mountains
"mountains", "trip", "views", "historical", "land -
marks"
151
Topic 1 lovers’ enthusiasts impressi -
ve bucovina views incredible
nature mountains landscapes
monasteries
"monasteries", "mountains", "landscapes", "nature",
"incredible"
805
Topic 2 repetitive felt time exploring
amazing scenic mountains hi-
king suceava monasteries
"monasteries", "hiking", "scenic", "mountains", "su-
ceava"
222
Topic 3 loved significance bucovina
trip views details highlight in-
tricate mountain monasteries
"monasteries", "mountain", "details", "views", "bu-
covina"
333
Topic 4 okay interesting nature peace-
fulness unforgettable combi -
ned countryside beauty buco-
vina monasteries
"monasteries", "peacefulness", "nature", "beauty",
"bucovina"
259
Figure 6
LDA Topic-Term Heatmap: Frequency of Top Terms by Topic

www.ce.vizja.pl
423
Bucovina Tourism through the Lens of Artificial Intelligence: Enhancing Regional Sustainability by Addressing Tourist Needs
This work is licensed under a Creative Commons Attribution 4.0 International License.
terms of the ratings given, as the p-value is much higher
than the conventional significance threshold of 0.05.
In other words, based on the scores provided by to -
urists, the segments identified through clustering do
not appear to exhibit statistically significant differences.
We also used a graphical representation, as shown in
Figure 4, of the frequency of themes that appear across
the three clusters to better identify common elements
and explain them.
Hypothesis 3: Tourists who participate in engaging ac-
tivities are more satisfied than those focused strictly on
cultural experiences.
To test this hypothesis, we categorized reviews ba -
sed on positive or negative sentiments. This allowed us
to see if tourists who participated in engaging (outdo -
or) activities were more satisfied than those who par -
ticipated in cultural activities. The second step was
to determine if the average ratings were significantly
different between the two activity categories: outdoor
(nature) activities versus cultural activities. To do this,
we identified reviews mentioning nature activities and
those mentioning cultural activities and applied senti -
ment analysis to the review text. As the final step, we
compared the results to check for significant differences
between these two groups.
We conducted sentiment analysis, assigning each re-
view a polarity score ranging from -1 (very negative)
to +1 (very positive). The next step was to compare the
average sentiment and rating scores between the two
groups of activities: outdoor and cultural (Ren & Zhao,
2024).
For the expressed sentiment, we obtained a t-stati -
stic value of t=6.87 and a p-value of 8.95e-12 (<0.05),
indicating a significant difference between the senti -
ments of tourists who participate in outdoor activities
and those who participate in cultural activities. For the
rating, with a t-statistic value of 0.52 and a p-value of
0.6 (>0.05), there are no statistically significant diffe -
rences. Thus, we can conclude that tourists who engage
in outdoor activities express significantly more positive
sentiments in their reviews compared to those focusing
on cultural activities; however, based on the given ratin-
gs, the difference is not substantial (see Fig. 5).
The chart illustrates the average sentiment and
average rating for two categories of tourist activities:
outdoor (nature) activities and cultural activities. The
blue bars represent the average sentiment, which ranges
from -1 (very negative) to 1 (very positive), while the
orange bars represent the average rating on an approxi-
mate scale from 1 to 5. Tourists who participated in
outdoor activities expressed significantly more positive
sentiments (0.451) than those who participated in cul -
tural activities (0.347). However, differences in average
ratings are much smaller, with both activity types ha -
ving very similar ratings: 2.998 for outdoor and 2.961
for cultural activities.
Hypothesis 4: Reviews mentioning cultural and na -
tural experiences are divided into distinct themes.
To test this hypothesis, we used LDA, a technique for
extracting hidden themes from a set of texts. We ap -
plied LDA to reviews mentioning cultural and natural
experiences and extracted five main themes (Anderson,
2012).
To clarify how topics were defined and distinguished,
Figure 7
Frequency of Topics Extracted with LDA

424
Angela Albu, Paul Paşcu
10.5709/ce.1897-9254.599DOI:
CONTEMPORARY ECONOMICS
Vol. 20 Issue 3 414-4262026
we created a topic-term heatmap, Figure 6, where hi -
gher frequencies are marked in darker shades. This al -
lows for a quick comparison of the term distributions
across themes.
Although the themes are divided between natural
elements (hiking, landscapes, mountains, nature) and
cultural ones (monasteries, historical, landmarks), the-
re is some overlap between the two categories. Howe -
ver, they seem to reflect two main directions: some the-
mes emphasize Bucovina’s natural aspects, while others
highlight cultural and historical features.
This suggests that cultural and natural experiences
do indeed form distinct themes, but in some cases, they
are combined in tourists’ reviews (Ren & Zhao, 2024).
This chart, Figure 7, shows the distribution of re -
views by theme, providing a clear view of the relevan -
ce of each theme within the dataset. The chart above
indicates the frequency with which various themes
extracted through the LDA technique appear in tourist
reviews (Blei, 2012). We observe that Topic 1 has the
highest frequency, suggesting that the dominant theme
in the analyzed reviews relates to natural and cultural
experiences, with a focus on specific elements such as
“mountains, ” “monasteries, ” and “landscapes. ”
This confirms our hypothesis that tourists visiting
Bucovina frequently express appreciation for the blend
of cultural and natural experiences. In contrast, Topic
0, which has a relatively low frequency, appears to hi -
ghlight a less-discussed theme in the reviews. Such the-
mes might relate to more specific aspects or contextual
particularities, such as nearby historical sites discussed
occasionally in reviews. Additionally, thematic overlap
between natural and cultural elements is present across
multiple topics, indicating that tourist experiences in
Bucovina can be perceived as integrated, combining
cultural traditions with natural heritage.
This distribution helps us conclude that, although
themes can be distinct, they are not completely separate
in tourists’ perceptions, reflecting an interdependence
between the cultural and natural facets of the region
(He et al., 2013).
6. Discussion
The results of this study can enhance tourist expe -
riences in Bucovina, leading us to propose specific re -
commendations for relevant stakeholders (local autho-
rities, tourism operators, local communities, and other
interested parties). These recommendations aim to
contribute to the sustainable development of regional
tourism and create memorable experiences for visitors.
Firstly, we suggest optimizing services based on to -
urist segmentation. This segmentation, grounded in
reviews and sentiment analysis, offers a detailed under-
standing of tourist preferences and behaviors. Stake -
holders should therefore tailor tourism services to each
segment, developing specialized packages that cater to
tourists’ needs, whether they are interested in cultural
activities or nature-based recreation.
Another recommendation targets local authorities,
focusing on improving infrastructure and tourist fa -
cilities. Negative reviews, especially during the winter
months, indicate that infrastructure issues (such as de-
lays in snow removal) impact tourist experiences. Local
authorities and tourism operators should prioritize in-
frastructure enhancements, particularly during adverse
weather conditions, to prevent declines in tourist satis-
faction.
We also propose creating integrated cultural and re-
creational tourism offerings. Thematic analysis revealed
that tourists appreciate experiences that combine cul -
tural and natural elements. Accordingly, stakeholders
could develop packages that blend visits to monasteries
or other cultural landmarks with outdoor activities,
such as mountain hikes. These packages might attract
a broader range of tourists and foster loyalty to the de -
stination.
Furthermore, stakeholders should establish an active
review monitoring system to identify recurring issues
and make real-time adjustments to services. Respon -
ding promptly and positively to tourist feedback could
enhance the destination’s image and increase satisfac -
tion. Seasonal considerations should inform Bucovina’s
promotional efforts, as positive reviews peak during the
summer, when conditions favor outdoor activities.
Although the concept of sustainability is not analy -
zed in a distinct section, our recommendations — such
as the personalization of services, infrastructure enhan-
cement, and integration of cultural and natural expe -
riences — align with sustainable tourism development
principles (Gretzel et al., 2015). Furthermore, by pro -
moting seasonally balanced tourism and encouraging
the integration of local products and services, our fin -
dings support the economic, environmental, and socio-
cultural pillars of sustainability.
Importantly, these insights highlight the potential
of artificial intelligence to uncover nuanced patterns in
tourist feedback, allowing stakeholders to implement
targeted and adaptive strategies. By combining cultural
heritage with natural landscapes in a coherent and da -
ta-driven manner, Bucovina can differentiate itself in a
competitive tourism market.
We argue that such initiatives are not only instru -
mental in improving visitor satisfaction but also in ar -
ticulating a clearer identity for the region. Ultimately,

www.ce.vizja.pl
425
Bucovina Tourism through the Lens of Artificial Intelligence: Enhancing Regional Sustainability by Addressing Tourist Needs
This work is licensed under a Creative Commons Attribution 4.0 International License.
they can contribute to building Bucovina’s brand as an
authentic and integrated tourist destination, one that
balances tradition and innovation while responding
dynamically to visitor expectations (Sigala, 2016).
7. Conclusion
In this study, we aimed to explore and understand the
perceptions of tourists visiting Bucovina from a fresh
perspective, using AI techniques for sentiment analysis
and clustering methods for segmenting tourists. By in-
tegrating analyzed online reviews and official statistical
data, we were able to identify several key conclusions.
Firstly, no significant differences were observed be -
tween the sentiment expressed in reviews and the nu -
merical ratings given by tourists. Although the emotio-
nal tone of reviews slightly influenced scores, statistical
analysis (ANOV A) showed that these variations were
not substantial enough to indicate significant group
differences. This suggests that the emotional tone of
reviews does not directly correlate with the numerical
evaluation of tourism services.
Secondly, clustering analysis (K-Means) showed that
tourists with similar preferences rated tourism expe -
riences in Bucovina uniformly, with no significant dif -
ferences in average scores across groups.
Thirdly, tourists who engaged in outdoor recreatio -
nal activities reported higher satisfaction than those
focusing on cultural experiences. While this distinction
is more apparent in sentiment expressed in reviews,
scores were relatively similar between the two activity
types. Nonetheless, sentiment analysis suggested that
outdoor activities are generally perceived more favora-
bly than cultural ones.
Finally, thematic analysis revealed a partial overlap
between cultural and natural experiences. Using LDA,
we observed that although distinct themes represent
each experience type, many reviews combine elements
of both. This finding highlights the importance of in -
tegrating cultural heritage and natural landscapes into
Bucovina’s tourism offering.
These conclusions demonstrate the potential of sen-
timent analysis and AI-based segmentation for optimi-
zing tourism offerings and developing personalized
marketing strategies that better meet tourists’ needs
and expectations. The findings provide a strong foun -
dation for future recommendations aimed at enhancing
the Bucovina tourism experience and promoting the
region as a top-tier destination.
ReferencesReferences
Aggarwal, C. C., & Zhai, C. (2012). Mining text data.
Springer.
Anderson, C. K. (2012). The impact of social media on
lodging performance. Cornell Hospitality Report,
12(15), 6–11.
Bessière, J. (1998). Local development and heritage:
Traditional food and cuisine as tourist attractions
in rural areas. Sociologia Ruralis, 38 (1), 21–34.
https://doi.org/10.1111/1467-9523.00061
Bird, S., Klein, E., & Loper, E. (2009). Natural language
processing with Python. O’Reilly Media.
Blei, D. M. (2012). Probabilistic topic models. Com-
munications of the ACM, 55(4), 77–84. https://doi.
org/10.1145/2133806.2133826
Blei, D. M., Ng, A. Y ., & Jordan, M. I. (2003). Latent
Dirichlet allocation. Journal of Machine Learning
Research, 3, 993–1022.
Buttcher, S., Clarke, C. L. A., & Cormack, G. V . (2010).
Information retrieval: Implementing and evaluating
search engines. MIT Press.
Corder, G. W ., & Foreman, D. I. (2014). Nonparametric
statistics: A step-by-step approach (2nd ed.). Wiley.
Eisenstein, J. (2019). Introduction to natural language
processing. MIT Press.
Gretzel, U., Sigala, M., Xiang, Z., & Koo, C. (2015).
Smart tourism: Foundations and developments.
Electronic Markets, 25 (3), 179–188. https://doi.
org/10.1007/s12525-015-0196-8
Griffiths, T. L., & Steyvers, M. (2004). Finding scien -
tific topics. Proceedings of the National Academy
of Sciences, 101 (Suppl. 1), 5228–5235. https://doi.
org/10.1073/pnas.0307752101
He, W ., Zha, S., & Li, L. (2013). Social media com -
petitive analysis and text mining: A case study in
the pizza industry. International Journal of Infor -
mation Management, 33 (3), 464–472. https://doi.
org/10.1016/j.ijinfomgt.2013.01.001
Hennig, C., Meila, M., Murtagh, F ., & Rocci, R. (2015).
Handbook of cluster analysis . Chapman and Hall/
CRC. https://doi.org/10.1201/b19706
Ho, C.-I., Lin, M.-H., & Chen, H.-M. (2012). Web users’
behavioral patterns of tourism information search:
From online to offline.  Tourism Management,
33(6), 1468–1482. https://doi.org/10.1016/j.tour -
man.2012.01.016
Hu, M., & Liu, B. (2004). Mining and summarizing

426
Angela Albu, Paul Paşcu
10.5709/ce.1897-9254.599DOI:
CONTEMPORARY ECONOMICS
Vol. 20 Issue 3 414-4262026
customer reviews. Proceedings of the Tenth ACM
SIGKDD International Conference on Knowledge
Discovery and Data Mining , 168–177. https://doi.
org/10.1145/1014052.1014073
Jurafsky, D., & Martin, J. H. (2021). Speech and language
processing (3rd ed.). Pearson.
Khan, A. (2020). Natural language processing for busi-
ness analytics: Practical applications of text analytics
and machine learning. Packt Publishing.
Li, X., Pan, B., Law, R., & Huang, X. (2017). Forecast -
ing tourism demand with composite search in -
dex. Tourism Management, 59, 57–66. https://doi.
org/10.1016/j.tourman.2016.07.005
Liu, B. (2012). Sentiment analysis and opinion mining.
Morgan & Claypool Publishers.
Manning, C. D., Raghavan, P ., & Schütze, H. (2008).
Introduction to information retrieval . Cambridge
University Press.
Marine-Roig, E., & Clavé, S. A. (2015). Tourism ana -
lytics with massive user-generated content: A case
study of Barcelona. Journal of Destination Mar -
keting & Management, 4 (3), 162–172. https://doi.
org/10.1016/j.jdmm.2015.06.004
McCloskey, B. J., LaCasse, P . M., & Cox, B. A. (2024).
Natural language processing analysis of online re -
views for small business: Extracting insight from
small corpora. Annals of Operations Research,
341(1), 295–312. https://doi.org/10.1007/s10479-
023-05816-2
Mellinas, J. P ., María-Dolores, M., & García, J. L. S.
(2016). Effects of the Booking.com scoring sys -
tem. Tourism Management, 57, 80–83. https://doi.
org/10.1016/j.tourman.2016.05.015
Pang, B., & Lee, L. (2008). Opinion mining and sen -
timent analysis. Foundations and Trends in In -
formation Retrieval, 2 (1–2), 1–135. https://doi.
org/10.1561/1500000011
Paşcaniuc, E. (2019). Receptarea curentelor, direcțiilor
şi tendințelor din folcloristica românească în Bu -
covina (II). Analele Bucovinei, XXVI(2), 507–519.
Puh, K., & Bagić Babac, M. (2023). Predicting senti -
ment and rating of tourist reviews using machine
learning. Journal of Hospitality and Tourism In -
sights, 6 (3), 1188–1204. https://doi.org/10.1108/
JHTI-02-2022-0078
Ren, S., & Zhao, X. (2024). Cultural ecosystem ser -
vices in heritage parks: Emotional landscape anal -
ysis using deep learning and social media text.
SSRN Electronic Journal . https://doi.org/10.2139/
ssrn.4966809
Sarkar, D. (2019). Text analytics with Python: A prac -
titioner’s guide to natural language processing (2nd
ed.). Apress.
Sigala, M. (2016). Social media and the co-creation of
tourism experiences. In M. Sotiriadis (Ed.),  The
Handbook of Managing and Marketing Tourism
Experiences (pp. 85–111). Emerald Group Publish-
ing Limited. https://doi.org/10.1108/978-1-78635-
290-320161033
Tabachnick, B. G., & Fidell, L. S. (2019). Using multivar-
iate statistics (7th ed.). Pearson.
Wu, H.-C., Ai, C.-H., Y ang, L. J., & Li, T. (2015). A study
of revisit intentions, customer satisfaction, corpo -
rate image, emotions, and service quality in the hot
spring industry. Journal of China Tourism Research,
11, 371–401. https://doi.org/10.1080/19388160.20
15.1110545
Xiang, Z., & Gretzel, U. (2010). Role of social media in
online travel information search. Tourism Manage-
ment, 31 (2), 179–188. https://doi.org/10.1016/j.
tourman.2009.02.016
Xiang, Z., Schwartz, Z., Gerdes, J. H., & Uysal, M.
(2015). What can big data and text analytics tell
us about hotel guest experience and satisfac -
tion? International Journal of Hospitality Man -
agement, 44 , 120–130. https://doi.org/10.1016/j.
ijhm.2014.10.013
Zhao, Y ., & Park, B. (2023). Exploring thematic in -
fluences on theme park visitors’ satisfaction: An
analysis of online reviews. Journal of Consumer
Behaviour, 23(1), 90–106. https://doi.org/10.1002/
cb.2157
