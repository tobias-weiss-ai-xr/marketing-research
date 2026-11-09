---
title: Generative AI Applications in Advertising
url: https://doi.org/10.54097/4tggde31
category: ai-marketing
subcategory: empirical
date: 2026-06
venue: Frontiers in Computing and Intelligent Systems
authors:
- Y Wang
source: openalex-oa
pdf_url: https://drpress.org/ojs/index.php/fcis/article/download/35205/34396
pages: 8
chars: 33014
fetched_at: '2026-11-08T18:12:53+00:00'
kb_version: 1
---

# Generative AI Applications in Advertising

Frontiers in Computing and Intelligent Systems
ISSN: 2832-6024 | V ol. 17, No. 1, 2026

31
Generative	AI	Applications	in	Advertising
Yifei Wang *
College of Arts & Science, New York University, New York City, 10012, USA
* Corresponding author Email: yw7596@nyu.edu

Abstract: This paper aims to investigate th e application of generative ar tificial intelligence (GenAI) models in advertising,
particularly how their use affects the quality of advertising c ontent and consumers' perceptions of AI-generated advertisements
across different industries. In this paper, a curated AI-Generated Advertisement Dataset is used to conduct a content-level analysis,
aiming to examine existing AI-generated advertisements based on their contents. Statistics and correlation analysis are applie d
to assess the quality AI-generated advertisements in four evalu ation categories: Visual Quality, Style Consistency, Semantic
Accuracy, and Creativity. The other, Xiaohongshu dataset, is used for user engagement and sentiment analysis. Two regression
models are applied to the dataset to understand how people react and interact with AI-generated contents. This paper suggests a
necessary improvement for the current development of GenAI mode ls. That is, paying more attention to improving users’
attitudes/perceptions toward AI-generated advertisements, leading to strengthened authenticity and reliability of advertisements.
This suggestion is especially critical for industries where con sumers value these qualities more, to enhance the overall
effectiveness of AI applications  in advertising. This paper add resses the real-world impact of GenAI model’s application in
advertising, offering new marketing lenses on how AI-generated ads can gain more consumers’ attention and trust.
Keywords: Generative Artificial Intelligence; Artificial Intelligence Generated Content; Advertising; Marketing.

1. Introduction
The rapid development of Generative artificial intelligence
(GenAI) marks the beginning of a new era for digital
advertising [1]. Models such as text-to-image and text-to-
video enable brands to generate high-quality visual content
with shorter production times, lower costs, and greater
creative freedom [2]. As a result, an increasing number of
advertising campaigns are in corporating AI-generated
elements [3], ranging from fully synthetic visuals to AI-
assisted creation.
Although many brands have adopted GenAI in advertising,
most lack knowledge of AI capabilities and characteristics,
which affects their understanding of consumer perception of
AI-generated advertisements (ads) [4]. Therefore, it is
important to discuss how to highlight a brand's advantages in
AI-generated ads in a more relevant, precise, and attractive
way [5].
This study aims to analyze AI-generated ads from the
perspectives of content production and public
engagement&sentiment perspectives. First, a dataset of
explicitly disclosed AI-generated ads from a variety of real-
world marketing campaigns is created. The quality of each ad
is assessed through four evaluation dimensions. Second, a
large-scale social media dat aset from the Xiaohongshu
platform is incorporated, including user-generated posts and
comments from different industries (later referred to as
domains) about Artificial Intelligence Generated Content
(AIGC).
This study will address the real-world impacts of GenAI
tools, expanding on prior findings that focused on their
creation capabilities, and provide insights not only for
producing higher-quality AI-generated ads but also, more
importantly, offer new marketing lenses on how AI-generated
ads can gain more consumers’ attention and trust.
2. Literature Review
Xiang et al. introduce the major technological capabilities
and characteristics of genera tive GenAI. Unlike traditional
machine learning models that aim to produce optimal
solutions, GenAI is designed to generate creative outputs
without predefined answers [ 6]. Particularly, two major
functionalities of GenAI are text generation (e.g., copywriting,
translation) and image generation (e.g., image and design
creation, video generation, virtual avatars, 3D model
generation), enabling companies across industries to improve
both innovation and efficiency [6]. However, the accuracy
and quality of AI-generated content remain questionable, a
concern that is especially critical in advertising.
In the paper of Gao et al., how GenAI can be applied in the
advertising context is discussed. AI applications in
advertising often consist of three components: image/video
production, copywriting, and content planning. Together,
these functions provide a more data-driven, tailored
advertising approach, improving efficiency and optimizing
user targeting[4]. In addition, this paper addresses a few
ethical challenges, such as algorithmic bias, privacy concerns,
and lack of transparency, that AI applications in advertising
face [3].
Beyond content generation, AI has profoundly reshaped the
entire advertising process. I n the Chinese market, AI
advertising is built on a data -centric platform that uses
algorithms to support every stage of the advertising workflow.
Second, the process has become more tool-based, reducing
the need for manual labor and enabling large-scale
automation. Third, AI enables real-time synchronization of
advertising activities, reducing the need for complex planning
cycles and enabling dynamic changes based on user behavior.
Finally, AI significantly improves efficiency, allowing for the
creation of large volumes of personalized advertising content.
This is especially important i n rapidly growing markets like
e-commerce, where demand for high-quality, personalized

32
advertising is rising [2].
3. Methodology
3.1. Research Design
This study combines two complementary data sources
because generating a comprehensive dataset capturing both
the visual characteristics of AI-generated ads and consumer
responses is challenging.
The two datasets are the AI-Generated Advertisement
Dataset and the Xiaohongshu AIGC Dataset. These two
datasets generate two distinct but related perspectives,
content-production and user engagement & sentiment, that
could provide a more comprehensive understanding of AI-
generated ads and their impacts on consumers.
3.2. Data Sources
3.2.1. AI-Generated Advertisement Dataset
This dataset consists of ads that are explicitly disclosed or
clearly identifiable as AI-generated. For each ad, information
including brand name, campaign name, year, industry,
platform, region, AI modality, AI function, evidence type, and
quality scores (visual quality, style consistency, semantic
accuracy, creativity) is collected. This dataset is used to
evaluate the visual quality of AI-generated ads.
Given the limited availability of publicly accessible
datasets on AI-generated ads, this dataset is manually curated
from verified sources. Therefore, this dataset is not large-
scale.
3.2.2. Xiaohongshu AIGC Dataset
The second dataset is obtained from Kaggle and contains
user-generated posts and comments related to AIGC on the
Xiaohongshu social platform. This dataset includes post and
comment subsets in specific domains (a total of 12), such as
food and fashion. The subsets include variables such as likes,
comments, shares, and comment content.
This Xiaohongshu dataset is used to analyze public
engagement and sentiment toward AI-generated Ads, which
are two key factors that experts use to evaluate the
effectiveness of advertising campaigns on social media
networks [7]. It provides large-scale evidence of how
engagement and sentiment levels influence ad effectiveness
[8].
3.3. Variable Construction
3.3.1. Content Evaluation Variables
The quality of AI-generated ads is evaluated across four
dimensions. The name and definition of each variable are
explained as follows:
● Visual Quality(VQ): The technical and
aesthetic quality of visual output. This includes
clarity, realism, and rendering quality [9].
● Style Consistency(SC): The degree of visual
consistency among the various elements within an
ad [10].
● Semantic Accuracy(SA): The extent to
which the visual materials accurately reflect the
intended message or concept [11,12].
● Creativity(CR): The originality and novelty
of the ad’s concept and execution [10].
Each variable is measured using a 5-point Likert scale,
where 1 represents “very low quality” and 5 represents “very
high quality” based on the definition of each variable.
3.3.2. Engagement Variables
The posts.csv subsets, such as post-food.csv and post-
fashion.csv, are used in this study to examine consumers’
engagement with AIGC across different domains. The
following variables are analyzed:
● Like Count: Number of likes(the proxy for
evaluating user engagement)
● Comment Count: Number of
comments(interaction score)
● Share Count: Number of shares(interaction
score)
● Collected Count: Number of
collected(interaction score)
3.3.3. Sentiment Variables
The comments.csv subsets are used to study public
sentiment toward AIGC across different domains.
Specifically, each comment’s like counts and sentiment are
studied.
● Like Count: Number of likes for each
comment.
● Sentiment: User’s attitude depicted in each
comment, evaluated as positive or negative.
These variables enable the study to examine how user
responses to AIGC vary across content contexts.
3.4. Content Analysis of AI-Generated
Advertisements
To examine the quality of AI-generated ads, a series of
descriptive and comparative analyses is conducted using the
first dataset.
First, an overall quality score i s calculated as the average
of the four variables for each campaign.  Descriptive
statistics are calculated for the overall quality scores of the
four evaluation dimensions to provide a summary of content
performance.
Second, a correlation analysis (e.g., 𝑐𝑜𝑟𝑟ሺ𝑉𝑄, 𝑆𝐶ሻ,
𝑐𝑜𝑟𝑟ሺ𝑆𝐴, 𝐶𝑅ሻ ) is done to examine the relationships among
these variables.
Finally, conduct cross-group comparisons across
categories such as industries or brand types to identify
structural differences in the production methods of AI-
generated ads.
3.5. Regression Analysis - User Engagement
A regression model is applied to the post subsets of the
Xiaohongshu dataset. Since the engagement variables, such
as like count, are highly skewed, a logarithmic transformation
is applied.
The model is:
𝑙𝑜𝑔ሺ𝐿𝑖𝑘𝑒𝐶𝑜𝑢𝑛𝑡௜ ൅1 ሻ
ൌ𝛽 ଴ ൅𝛽 ଵ𝐶𝑜𝑚𝑚𝑒𝑛𝑡𝐶𝑜𝑢𝑛𝑡௜
൅𝛽 ଶ𝑆ℎ𝑎𝑟𝑒𝐶𝑜𝑢𝑛𝑡௜ ൅𝛽 ଷ𝐶𝑜𝑙𝑙𝑒𝑐𝑡𝑒𝑑𝐶𝑜𝑢𝑛𝑡௜
൅𝛽 ସ𝐷𝑜𝑚𝑎𝑖𝑛௜
LikeCount is the dependent variable, representing user
engagement. CommentCount, ShareCount, and
CollectedCount track user interaction intensity. Domain
represents different AIGC industries (e.g., food, fashion,
cars, ...)
This model helps identify ke y factors associated with
higher engagement and enable s comparisons of engagement

33
patterns across different AIGC domains.
3.6. Regression Analysis - User Sentiment
To examine users’ attitudes toward AIGC across different
domains, comment subsets are used. Each subset includes the
sentiment label, which categorizes attitudes toward AIGC as
positive or negative. A logistic regression model is applied to
these subsets:
𝑃ሺ𝑆𝑒𝑛𝑡𝑖𝑚𝑒𝑛𝑡௜ ൌ𝑘 ሻൌ𝛽଴ ൅𝛽 ଵ𝐷𝑜𝑚𝑎𝑖𝑛௜
Sentiment serves as the dependent variable. Domain is a
categorical variable that represents different application areas,
such as fashion, cars, food, literature, etc.
Specifically, this model can determine how users’ attitudes
vary across different AIGC domains.
3.7. Analytical Framework
This study combines two complementary levels of analysis
in a parallel, comparative approach. Visual quality and user
engagement&sentiment are analyzed separately but
interpreted jointly.
4. Results & Analysis
4.1. Content Analysis of AI-Generated
Advertisements
4.1.1. Descriptive Statistics
Table 1 shows the mean and standard deviation for the four
evaluation dimensions of AI-generated ads.

Table 1. Mean and Standard Deviation for the four evaluation dimensions
 Visual Quality Style Consistency Semantic Accuracy Creativity
Mean μ 4.286 4.810 4.714 4.619
Standard Deviation σ 0.717 0.512 0.902 0.669
Overall, the results indicate that AI-generated ads achieve
relatively high scores in style consistency ( μ=4.810) and
semantic accuracy ( μ=4.714), indicating that generative
models are effective at producing visually coherent content
and conveying the intended messages of the ads. However,
the visual quality score ( μ= 4.286) is the lowest, suggesting
that AI-generated ads still have issues, such as a lack of
realism or poor quality.
Semantic Accuracy shows the greatest variability
(σ=0.902). This implies that the alignment with the intended
message is not always consistent. Visual Quality also shows
relatively high variability ( σ=0.717) ,  m e a n i n g  t h a t  s o m e
brands can produce realistic AI-generated ads, while others
cannot.
Creativity ( μ=4.619; σ0.669 ) shows a moderate-to-high
overall score and considerable variation across ads,
suggesting differences in creativity levels among brands.
Thus, AI-generated ads tend to excel in visual coherence
and semantic precision, but exhibit limitations in visual
quality.
4.1.2. Correlation Analysis
To further investigate the relationship between the four
dimensions, a correlation analysis is conducted.
The following is a pairwise summary table of Pearson
correlation coefficient r and p-values (Table 2) as well as the
correlation matrix (Figure 1) for n = 21.

Table 2. Pairwise Summary Table
Pair r p-value
VQ-SC 0.428 0.053
VQ-SA 0.364 0.104
VQ-CR 0.342 0.129
SC-SA 0.851 0.000
SC-CR 0.654 0.001
SA-CR 0.556 0.009

According to Table 2 and Figure 1, style consistency (SC)
and semantic accuracy (SA) are strongly correlated (r=0.851,
p < 0.01 ), indicating that AI-generated ads with more
coherent visual styles tend to convey clearer, more accurate
intended messages. Style consistency is also strongly
correlated with creativity (CR), r=0.654, p < 0.01, suggesting
that a consistent visual style helps maintain creativity.

Figure 1. Correlation Matrix-AI Ad Quality Scores

A moderate positive relationship is observed between SA
and CR (r=0.556, p<0.01), suggesting that more creative AI
ads can still maintain the accuracy and clarity of the intended
message.
In contrast, visual quality (VQ) has a statistically
insignificant relationship with the other three variables.
Overall, this correlation analysis shows that style
consistency plays a key role in AI ads and is closely related to
both semantic accuracy and crea tivity. In contrast, visual
quality has a relatively minor impact on variations in AI-ads
performance across different industries.
4.1.3. Group Comparison
This paper also compares scores across four evaluation
dimensions across industries (n =21).

Table 3. Means of different industry groups
Industry Group VQ SC SA CR
Fashion 4.600 4.800 4.400 4.800
Food&Drinks 4.430 4.860 5.000 4.710
Other 4.000 4.780 4.670 4.440

As shown in Table 3 and Figure 2, overall, fashion-related
AI ads show a relatively higher quality score for VQ, SC, and

34
CR. However, its SA score is the lowest among the Food &
Drinks and Other industries. In contrast, Food & Drinks-
related AI ads have the highest SA score.

Figure 2. Group Mean Score Comparison

To investigate differences in overall evaluation scores
across industries, a Kruskal-Wallis test is conducted.

Table 4. Kruskal-Wallis Test Results
VQ H = 2.76, p = 0.2518 ns
SC H = 0.12, p = 0.9411 ns
SA H = 1.33, p = 0.5134 ns
CR H = 0.53, p = 0.7667 ns

Table 4 shows no statistically significant differences across
industries for any of the four evaluation dimensions. The p-
values for VQ, SC, SA, and CR all fail to reach the statistical
significance level (p>0.05).
In summary, the overall perfo rmance of AI-generated ads
is relatively similar across industries, with no strong evidence
that any one industry outperforms the others.
4.2. Engagement Analysis
P o s t  s u b s e t s  a r e  u s e d  t o  a n a l y z e  u s e r s ’  e n g a g e m e n t  o n
A I G C .  T o  p e r f o r m  t h e  a n a l y s i s ,  a l l  t h e  p o s t -  C S V  f i l e s  a r e
merged into a single dataframe.
4.2.1. Cross-Domain Comparison

Figure 3. Mean Engagement Metrics Across AIGC Domains

T he  r e s ul t s  s h ow n i n Figure 3 indicate that the Drawing
domain tends to generate the highest engagement, as its mean
likes, collects, and shares are the highest across all domains.
Food, Fashion, and Friction domains also tend to generate
higher engagement levels. The Car and Sport domains tend to
generate relatively lower engagement levels.
This result suggests that consumers may respond
differently to AIGC depending on the domains associated
with it.
4.2.2. Regression Results
Table 5 represents the results of the OLS regression model
examining factors influencing user engagement, measured as
the logarithm of like counts.
Overall, the model can explain different factors’ impact on
user engagement well, with an 𝑅ଶ o f  0.413, suggesting that
approximately 41.3% of the variation in engagement levels
can be explained by the included variables. The model is
statistically significant, with an F-statistic of 73.47 and p<
0.01, indicating a strong overall fit.

OLS Summary:
𝑹𝟐 ൌ 𝟎. 𝟒𝟏𝟑𝟎 𝑨𝒅𝒋. 𝑹𝟐 ൌ 𝟎. 𝟒𝟎𝟕𝟒
𝑭 െ 𝒔𝒕𝒂𝒕𝒊𝒔𝒕𝒊𝒄 ൌ 𝟕𝟑. 𝟒𝟕, 𝒑 ൌ 𝟎. 𝟎𝟎𝟎𝟎
𝑵 ൌ 𝟏, 𝟒𝟕𝟕

35

Table 5. OLS Regression Results
 Coefficient Standard Error t-value p-value Significant
const 2.8796 0.1742 16.5298 0.0000 significant
comment_count 0.0005 0.0001 6.0039 0.0000 significant
share_count 0.0007 0.0001 9.8480 0.0000 significant
collected_count 0.0001 0.0000 8.4201 0.0000 significant
Domain: car 0.3375 0.2062 1.6372 0.1018 Non-sig
Domain: drawing 5.1090 0.3669 13.9231 0.0000 significant
Domain: fashion 1.7911 0.2080 8.6118 0.0000 significant
Domain: fiction 3.8029 0.3987 9.5386 0.0000 significant
Domain: food 0.7434 0.2693 2.7598 0.0059 significant
Domain: food-additional -0.8619 0.3188 -2.7034 0.0069 significant
Domain: food_2 1.7043 0.3759 4.5340 0.0000 significant
Domain: literature 1.2191 0.3297 3.6977 0.0002 significant
Domain: sport 0.3744 0.2605 1.4373 0.1508 non
Domain: sport-additional 1.0250 0.3167 3.2363 0.0012 significant
Domain: technological
development 1.5446 0.3362 4.5946 0.0000 significant
Interaction-Based Variables
The results show that all interaction-based variables have
positive and statistically significant effects on user
engagement level. The 𝛽 value and p-value for each variable
are:
- CommentCount: 𝛽=0.0005, p< 0.01
- ShareCount: 𝛽=0.0007, p< 0.01
- CollectedCount: 𝛽=0.0001, p<0.01
These results indicate that posts with higher interaction
scores tend to receive more likes, suggesting greater user
engagement. Among these three variables, content sharing
plays a critical role in increasing engagement as its 𝛽 i s  t h e
largest.
Domain Effects
Table 5 also shows variation in engagement across each
AIGC domain. Several domains show strong positive and
statistically significant effects on user engagement level
compared to the baseline category:

Drawing: 𝛽=5.109, p<0.01
Friction: 𝛽=3.803, p<0.01
Fashion: 𝛽=1.791, p<0.01
Technological development: 𝛽=1.543, p<0.01
Food: has multiple values, but is generally significant
Literature: 𝛽=1.219, p<0.01

The Drawing and Friction show especially higher levels of
user engagement. A possible implication of this finding is that
users are more likely to engage with visually appealing or
creativity-driven AI-generated content.
However, some domains do not show statistically
significant effects: Car (p=0.102) and Sport (p=0.151).
In addition, the food_additional category has a statistically
significant negative effect (β= -0.862, p< 0.01 ), indicating a
decreasing impact on engagement
In summary, user engagement with AIGC posts is
influenced not only by interaction-based variables but also by
certain domains, with content-sharing variables and visually
appealing domains generating higher user engagement.
4.3. Sentiment Regression Analysis
4.3.1. Descriptive Statistics

Table 6. Descriptive Statistics of Comments’ Like Count by Domain
 Mean Standard Deviation Minimum Maximum source_file
Technology Outlook 2.97 51.91 0.0 2122.0
car 2.69 69.77 0.0 5508.0
drawing 39.01 510.66 0.0 15000.0
fashion 11.87 433.68 0.0 34000.0
fiction 6.29 98.39 0.0 5087.0
food 3.34 42.55 0.0 1958.0
food-additional 2.62 37.68 0.0 1443.0
food_2 39.54 530.26 0.0 22000.0
literature 9.54 156.32 0.0 7966.0
sport 16.70 521.95 0.0 38000.0
sport-additional 0.33 1.62 0.0 18.0
technological development 94.48 1334.56 0.0 28000.0
According to Table 6 , comments related to the
Technological development domain generate the highest
counts of likes. Comments associated with the Drawing
domain also generate higher counts of likes, while comments
related to the Car domain generate relatively lower counts of
likes.

36
The standard deviation for each  domain is relatively high,
suggesting that like counts vary widely across comments.
4.3.2. Cross-Domain Comparison
Figure 4  displays the distribution of sentiment labels
(negative or positive) across domains.
The results show that the Car domain generates the most
negative sentiment labels, while the Technological
Development domain generates the fewest. The Car and Sport
domains also generate a relatively higher number of positive
labels.
These results suggest that consumers’ attitudes toward
AIGC may vary depending on its domains.

Figure 4. Sentiment Distribution Across AIGC Domains

4.3.3. Regression Results
Table 7  demonstrates the relationship between AIGC
domains and user sentiment using a logistic regression model.
The model includes a large sample size ( N=53,779) and is
statistically significant overall. However, the pseudo 𝑅ଶ  o f
0.0164 suggests that the application domain explains only a
small portion of the overall variation in user sentiment. Other
factors can also influence users’ sentiment toward AIGC.
Domain Effects on Sentiment
Several domains, including Food, Fashion, Technological
Development, Car, and Fiction, show significant negative
effects on sentiment (as indicated by negative coefficients and
odds ratios < 1), suggesting a lower likelihood of positive
sentiment towards content in these domains.
In contrast, the domain Sport shows a significant positive
effect, indicating that positive emotions are slightly more
likely to appear in sports-related AIGC content.
Additionally, the Drawing and Literature domains show no
statistically significant effects, indicating that sentiment in
these domains does not differ significantly from the baseline.

Table 7. Logistic Regression Result
 Coefficient Standard Error z-value p-value Odds Ratio Significant
const 0.2114 0.0282 7.5063 0.0000 1.2354 significant
Domain: car -0.2652 0.0347 -7.6430 0.0000 0.7670 si gnificant
Domain: drawing 0.0075 0.0578 0.1293 0.8971 1.0075 Non-si gnificant
Domain: fashion -0.5316 0. 0360 -14.7776 0.0000 0.5877 si gnificant
Domain: fiction -0.2744 0.0374 - 7.3278 0.0000 0.7601 significan t
Domain: food -0.4679 0.0449 -10.4120 0. 0000 0.6263 significant
Domain: food-
additional 0.0238 0.0553 0.4303 0.6670 1.0241 Non-significant
Domain: food_2 -1.0809 0.0475 -22. 7330 0.0000 0.3393 significan t
Domain: literature 0.0341 0. 0401 0.8504 0.3951 1.0347 Non-signi ficant
Domain: sport 0.0940 0.0360 2.6127 0.0090 1.0986 si gnificant
Domain: sport-
additional -0.7383 0.0999 -7.3879 0. 0000 0.4779 significant
Domain:
technological
development
-0.3300 0.0871 -3.7890 0. 0002 0.7189 significant
Overall, public sentiment of  A I G C  i s  s u b j e c t  t o  m o r e
consistent constraints. In most application domains, users are
less likely to stay positive about AIGC.
5. Integrated Discussion: Content
Production vs Public Engagement&
Sentiment
The findings of this study indicate a significant contrast
between the capabilities of gener ative AI in content creation
and consumers’ engagement with and attitudes toward such
content.
From a content-production perspective, AI-generated ads
can perform well in style consistency and semantic accuracy.
Most companies can produce visually consistent ads and
deliver their messages to consumers. However, visual quality
tends to vary. Some brands may own more advanced
generative models capable of producing more realistic,
visually appealing ads. Additionally, there are differences in
the level of creativity among different brands. This might be

37
because some brands might use their own teams to develop
frameworks or write scripts. Moreover , style consistency &
semantic accuracy, and style consistency & creativity, exhibit
a strong positive correlation, suggesting that stylistic
coherence is critical in shaping the overall quality of AI ads.
Additionally, the group comparison results highlight that
brands generate ads with specific design priorities. Some
prioritize aesthetic appeal, while others emphasize clarity and
functionality.
Overall, the analysis of content-production perspectives
indicates that the overall performance is strong.
However, the overall quality score of AI-generated ads
does not guarantee universal consumer satisfaction. The user
engagement analysis shows that only domains associated with
creative or visually appealing content are more likely to make
consumers willing to engage.
The sentiment regression m odel demonstrates distinct
patterns in user attitudes across domains. In fields such as
food, fashion, and technology, users tend to have a negative
attitude towards AI-generated ads, possibly because they
expect these areas to be trustworthy and authentic, and AIGC
might not meet those expectations. Meanwhile, the model
suggests that the domain alone does not decide how people
feel about AIGC. Consumers’ attitudes are influenced by
factors such as how good the content looks, what they like,
what they have experienced w ith AI before, and how much
they trust the AIGC. Therefore, attitudes toward AIGC are
influenced by multiple contexts, rather than determined solely
by domains.
Furthermore, the findings reveal that consumers’ behaviors
might not align exactly with their attitudes. Some domains,
such as Fashion, generate high engagement levels but receive
more negative comments, comparing the two regression
models. This suggests that consumers may feel unsure or
conflicted, yet still engage with AIGC content out of curiosity
or for entertainment.
I n  s u m m a r y ,  w h i l e  g e n e r a t i v e  A I  e x c e l s  a t  p r o d u c i n g
visually satisfying ads, it does not necessarily foster positiv e
attitudes among consumers. This result serves as a reminder
to marketers that future use of GenAI in advertising should
not only improve the quality of visual content, especially
realistic images, but also needs to prioritize consumers’
feelings about and willingness to engage with AI-generated
ads. One potential method to enhance this is to boost AIGC’s
authenticity and credibility.
6. Conclusion
This study builds on existing research on AI in advertising
and provides comprehensive insights into the evaluation of
AIGC and how it is received across different industries.
The content-production analys i s  s h o w s  t h a t  A I - g e n e r a t e d
ads can achieve high style consistency and semantic accuracy,
with a strong correlation among style consistency, semantic
accuracy, and creativity. Thes e findings indicate that
companies can use current GenAI models to produce visually
coherent and compelling advertising content. However,
variations occur across industries due to companies’
intentions and needs.
The consumer engagement&sentiment analysis shows a
relatively conflicted picture of how consumers engage with
AIGC and how they feel about it. While consumers are more
likely to engage with AIGC, par ticularly in domains related
to creative or visually appealing content, their sentiment
toward it remains relatively cautious across many areas.
However, user sentiment is only weakly explained by domain
differences and may also be influenced by other factors, such
as user demographics and prior AIGC experience.
In conclusion, this study reveals a critical problem in the
current development of GenAI models. That is, enhancing
models' technical capabilities does not necessarily guarantee
consumers’ positive attitudes toward AIGC. It is necessary to
pay greater attention to improving the authenticity and
reliability of AIGC, especially in industries where consumers
value these qualities more, to enhance the overall
effectiveness of AI applications in advertising.
7. Limitations & Future Research
Directions
7.1. Limitations
From the perspective of content-production analysis, a
significant limitation is the small sample size (n=21). Such a
small sample size reduces statistical power and may lead to
less reliable results. Moreover, the scores for the four
evaluation dimensions are assessed subjectively, which may
cause measurement bias. The results cannot be generalized
perfectly to the broader population of AI ads.
For the engagement&sentiment analysis, the biggest
limitation is the uneven distribution of observations across
domain subsets, leading to biased estimates and unreliable
comparisons across industries. In particular, subsets with
larger sample sizes may have a disproportionate impact on
results.
Another potential limitation is that the analysis relies solely
on data from the Xiaohongshu platform, and distinct
consumer behaviors, preferences, and demographics that can
also influence engagement and sentiment are not included.
Thus, the results may not represent the entire population of
consumers.
7.2. Future Research Directions
Future studies can explore  more objective evaluation
methods using deep learning and other applications. For
instance, by incorporating a computer vision model alongside
human Likert-scale ratings, the consistency of the
advertisement evaluation would improve.
Furthermore, future research could examine ethical issues
in AI applications in advertising by integrating theoretical
frameworks on consumer trust and AI transparency from prior
studies. For instance, by comparing users’ reactions to content
explicitly labeled as AI-generated versus content without such
labeling, the findings could gain deeper insights into how
transparency influences trust, engagement, and user
sentiment.
References
[1] Li, H. (2019). Special secti on introduction: Artificial
intelligence and advertising. Journal of Advertising , 48(4),
333–337. https://doi.org/10.1080/00913367.2019.1654947.
[2] Qin, X., & Jiang, Z. (2019). The impact of AI on the advertising
process: The Chinese experience. Journal of Advertising, 48(4),
338–346. https://doi.org/10.1080/00913367.2019.1652122.
[3] G a o ,  B . ,  W a n g ,  Y . ,  X i e ,  H . ,  &  H u ,  Y .  ( 2 0 2 3 ) .  A r t i f i c i a l
intelligence in advertising: A dvancements, challenges, and
ethical considerations in target ing, personalization, content
creation, and ad optimization. SAGE Open, 13(4). https://doi.
org/10. 1177/21582440231210759.

38
[4] Beyari, H., & Hashem, T. (2025). The role of artificial
intelligence in personalizing social media marketing strategies
for enhanced customer experience. Behavioral Sciences, 15(5),
700. https://doi.org/10.3390/bs15050700.
[5] Sharakhina, L. V., Ilyina, I., Kaplun, D., Teor, T. R., &
Kulibanova, V. (2023). AI technologies in the analysis of
visual advertising messages. Journal of Marketing Analytics .
https://doi.org/10.1057/s41270-023-00255-1.
[6] Xiang, Y., Wu, Y., Song, J., G ong, Y., & Liang, P. (2024).
Generative AI in industrial revolution: A comprehensive
research on transformations, challenges, and future directions.
Journal of Knowledge Learning and Science Technology, 3(2),
11–20. https://doi.org/10.60087/jklst.vol.3n2.p20.
[7] Raudeliūnienė, J., Davidavičienė, V., Tvaronavičienė, M., &
Jonuška, L. (2018). Evaluation of advertising campaigns on
social media networks. Sustainability, 10(4), 973. https://doi.
org/ 10.3390/su10040973.
[8] Achar, C., So, J., Agrawal, N. , & Duhachek, A. (2016). What
we feel and why we buy. Current Opinion in Psychology , 10,
166–170. https://doi.org/10.1016/j.copsyc.2016.01.009.
[9] Sheng, X., Li, L., Chen, P., Wu, J., Xu, L., Yang, Y., & Li, Y.
(2023). Technical quality-assist ed image aesthetics quality
assessment. In Lecture Notes in Computer Science (pp. 50–62).
https://doi.org/10.1007/978-981-99-8552-4_5.
[10] Zheng, J. (2025). Generative AI-driven visual advertising
creativity generation and style consistency modeling. Advances
in Computer and Communication , 6(5), 262–267. https://doi.
org/ 10.26855/acc.2025.12.001.
[11] Ganmote, D. P., & Bapuso, S. S. (2025). Artificial intelligence
and the future of English semantics. In Global Dimensions of
Multidisciplinary Research (p. 47). https://doi.org/ 10. 25215/
9371837764.07.
[12] Yang, Y., Guo, C., Liu, F., Sun, L., Liu, C., & Sun, Q. (2022).
Semantic communications with artificial intelligence tasks:
Reducing bandwidth requirements and improving artificial
intelligence task performance. IEEE Industrial Electronics
Magazine, 17(3), 4–13. https://doi. org/10. 1109/ mie. 2022.
317433.
