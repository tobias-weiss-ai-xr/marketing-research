---
title: 'Measuring social media customer engagement with brands based on information entropy: an application
  case of luxury brand'
url: https://doi.org/10.1057/s41262-024-00376-7
category: social-media
subcategory: framework
date: 2025-02
venue: Journal of Brand Management
authors:
- Siwei Xiao
- Xiaoyu Chen
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1057/s41262-024-00376-7.pdf
pages: 19
chars: 79509
fetched_at: '2026-11-08T17:33:39+00:00'
kb_version: 1
---

# Measuring social media customer engagement with brands based on information entropy: an application case of luxury brand

Vol:.(1234567890)
Journal of Brand Management (2025) 32:184–202
https://doi.org/10.1057/s41262-024-00376-7
ORIGINAL ARTICLE
Measuring social media customer engagement with brands based
on information entropy: an application case of luxury brand
Siwei Xiao1  · Xiaoyu Chen2
Revised: 2 December 2024 / Accepted: 5 December 2024 / Published online: 10 February 2025
© The Author(s) 2025
Abstract
Customer engagement (CE) within social media has emerged as a focal point in marketing research due to its significant
impact on brand and firm-related outcomes. However, effective measurement methodologies for CE behaviours remain
underexplored in this context. Building upon the existing concept of CE behaviour proposed by Brodie et al. (J Serv Res
14(3):252–271, 2013), and the CE cycle theory, this paper introduces an operational definition that supports an entropy-based
CE behaviour measurement framework, offering a nuanced reflection of social media dynamics. The proposed measurement
approach, among the initial attempts to integrate the multi-criteria decision-making (MCDM) weighting method into brand
marketing analytics, ensures a reliable and rigorous assessment of CE performance with brands. Additionally, a range of
analytical methods, including regression modelling using dummy variables, sentiment analysis, and hierarchical clustering
algorithm, were synthesized to assist the objective evaluation of brands’ impacts on CE behaviour outcomes. A peer group
of six luxury brands were chosen to analyse their impacts on engagement performance independently. Key findings from this
application demonstrate the approach’s ability to compare the engagement performance of different brands, offering a sig-
nificant tool to differentiate engagement behaviour levels while providing actionable insights for brand marketing initiatives.
Keywords Shannon entropy · Customer engagement behaviour · Customer brand engagement · Social media · Brand
marketing · Luxury brand
Introduction
In the big data era, the enriched data environment, along
with the evolving landscape of relationship marketing, is
driving a rapid escalation in customer engagement (CE)
within virtual environments. Service providers increasingly
depend on social media to uncover the latent value underly-
ing CE behaviours, encompassing both business-related (e.g.
sales revenue, net profits) and brand-related outcomes (e.g.
brand exposure, brand experience, brand attachment) (Basu
et al. 2023; Kim and Ko 2012; Wu et al. 2019; Zhang et al.
2017; Hollebeek et al. 2014). A study by Kumar and Pansari
(2016) highlighted a significant gap in organizational per -
formance attributable to a firm’s level of engagement, which
directly influences its brand equity and financial sustain-
ability. Recognizing the critical role of brand engagement
strategies, the Marketing Science Institute (2022) has once
again prioritized CE as a Tier 1 focus area for the period
from 2022 to 2024. This underscores the growing recogni-
tion of CE’s importance in fostering brand loyalty and driv-
ing business success.
Notably, the emergence of social media platforms
has fostered a more dynamic and communicative digital
environment, facilitating the sharing of brand information
and opinions among customers (McQuarrie et al. 2013;
Wang 2023; Ismagilova et al. 2020). For marketing prac-
titioners, these platforms present opportunities to expand
communication channels with customers while fulfilling
objectives related to customer relationship management
and business promotion (Bai and Yan 2020). In response
to these trends, an increasing number of studies have
focused on how CE on social media impacts brand-related
and customer-related outcomes (Harmeling et al. 2017;
 * Siwei Xiao
 xiaosiwei1006@gmail.com
 Xiaoyu Chen
 reneechen513@gmail.com
1 University of Bristol, Beacon House, Queens Road,
Bristol BS8 1QU, UK
2 University of Birmingham, Birmingham Research Park, 97
Vincent Drive, Birmingham B15 2SQ, UK

185
Measuring social media customer engagement with brands based on information entropy: an…
Schivinski et al. 2016). Additionally, many researchers
(e.g. Basu et al. 2023; Schivinski et al. 2016; van Doorn
et al. 2010) have sought to conceptualize CE behaviours
on social media to illuminate how a brand’s online mar -
keting activities influence CE.
Despite the development of CE antecedents, stud-
ies examining the features of social media content that
enhance CE behaviours remain scarce (Wu et al. 2019),
necessitating more relevant research. Moreover, while
many studies explore the framework for CE behaviours
on social media (Liu et al. 2021; Wu et al. 2019; Brodie
et al. 2013; van Doorn et al. 2010), limited attention has
been given to the exploration of measurable social media
CE behaviours. This gap hinders brand practitioners
from leveraging CE information to assess how efficient
their marketing activities are in engaging customers, and
whether their existing marketing mix is advantageous or
needs adaptations. Accordingly, this study addresses the
following research questions.
RQ1 How to assess the target brand’s CE behaviour
level (score)?
RQ2 How does the target brand’s CE behaviour level
(score) compare with those of peer brands?
RQ3 How do the target brand’s social media market-
ing activities impact CE behaviour outcomes?
In response to RQ1 & RQ2, this study provides an
overview of existing efforts to measure CE behaviours
while proposing an entropy-based CE measurement
framework. This framework is grounded in an operational
definition of CE behaviour based on four premises and
utilizes Shannon entropy (1948) to quantify behaviour
levels. This represents one of the initial attempts to incor -
porate multi-criteria decision-making (MCDM) into the
quantitative exploration of CE in brand marketing.
For RQ3, we employed a fixed-effect model to assess
brand CE performance and the impact of brands’ social
media marketing activities. Our analysis included a total
of 18,964 brand-generated contents (BGCs) on Twitter
from 2017 and 2022, alongside 25,991 customer-gen -
erated content (CGCs), especially focusing on luxury
brands.
The remainder of this paper is organized as follows. In
"Literature review" section reviews CE on social media
and provides an operational conceptualization based
on the CE cycle (Sashi 2012) and Brodie et al. (2013).
In  "Methodology" section details the proposed entropy-
based CE measurement approach and the associated con-
ceptual research framework. In "Results and discussion"
section presents the study results, while "Contributions,
implications and limitations" section discusses key impli-
cations and future research pathways.
Literature review
CE conceptualization
Given the growing number of online users and increasing
attachments to digital tools, CE conceptualization has been
extensively investigated in extensive studies (e.g. Harmel-
ing et al. 2017; Verleye et al. 2014; Brodie et al. 2013,
2011; Hollebeek 2011; van Doorn et al. 2010). Diverse
dimensions have been identified in these studies, but the
CE conceptualization may nonetheless be consolidated
into three major dimensions, namely, behavioural, affec-
tive and cognitive (Lim & Rasul 2022). However, in other
studies, CE has been categorized and interpreted in sig-
nificantly different ways. For example, five dimensions
comprising valence, modality, scope, nature of impact,
and customer goals were emphasized by van Doorn et al.
(2010). Similarly, So et al. (2016) proposed dimensions of
identification, attention, absorption, enthusiasm, and inter -
action. Alternatively, a broader model incorporates CE as
a decision variable that connects and examines antecedents
and consequences, referring to (Dwivedi 2015 ; Verhoef
et al. 2010). To reconcile the varied manifestations of CE,
Lim et al. (2022, p. 441) argued that CE can be approached
from diverse perspectives, but the most important is cap-
turing and explaining the “nature of interaction” exhibited
by customers.
Besides, brand engagement (BE) is often confused with
customer engagement, as the terms are frequently used inter-
changeably by brand practitioners (e.g. Duncan et al. 2019;
Hollebeek 2011). While these concepts overlap, they are
context-dependent. At the firm level, BE refers to the extent
to which stakeholders involve or commit to a known iden-
tity (Duncan et al. 2019). Compared to CE, BE involves a
broader range of stakeholders such as suppliers, employees,
and investors (Paschen and Pitt, 2019). On the other hand,
in the context of marketing initiatives, CE is often high-
lighted for its pivotal role in driving brand equity (Duncan
et al. 2019), with an emphasis on the exchange relation-
ship between customers and brands. In this setting, BE is
linked to other marketing constructs, sometimes being used
interchangeably with CE or referred to as customer brand
engagement, see examples (Wong & Merrilees 2015; Hol-
lebeek 2011). To align with the scope of proposed RQs, this
paper adopts the term CE to encompass all related concep-
tualizations in the subsequent discussion.
CE on social media and CE cycle
In the context of social media, Brodie et al (2013) pro-
posed a working definition that highlights the specific

186 S. Xiao, X. Chen
interactive experiences between key entities (customers
and brands) and emphasizes the context-dependent nature
of online CE, in addition to the traditionally recognized
tripartite dimensions. This working definition not only
facilitates the exploration of CE in a digital environment
but also underscores the pivotal role of CE in relational
exchange (Brodie et al. 2013).
Sashi (2012) attributed the diverse manifestations of
CE to different practitioner perspectives and the evolving
role of CE within the CE cycle, which encompasses sev -
eral intermediate stages: Connection, Interaction, Satisfac-
tion, Retention, Commitment, Advocacy, and Engagement.
Connection serves as the foundational step in establishing
relationships with customers, acting as the prerequisite for
relational exchange. This initial stage hinges on fulfilling
customer needs, whether from a functional or psychologi -
cal perspective. For instance, customers might seek service
advice, develop an emotional bond, or express themselves,
marking the beginning of a relational exchange process with
brands. At this stage, customers are likely to engage in inter-
active activities (e.g. reading, watching, sharing, comment-
ing), signalling a transition to the next stage—Interaction.
Satisfaction, as an intermediate indicator, reflects the
overall level of customer contentment, forming the basis
for progression to the stages of Retention, Commitment, and
Advocacy. The final stage, Engagement, is reached when a
loyal or delighted customer consistently displays both loy -
alty and delight for a brand, indicating the presence of strong
emotional bonds and enduring relational exchange between
customers and brands.
Sashi’s (2012) CE cycle provides insights into the com-
plex relationships among customer-related antecedents
during the engagement process, capturing the dynamic
emotional and behavioural states. Notably, Sashi’s frame-
work (2012) applies to both offline and online marketing
contexts. However, this research is specifically focused on
social media, where BGC is a critical touch point for assess-
ing the depth of relational exchange to a brand. Building on
previous discussions (Brodie et al. 2013; Sashi 2012), we
propose the following operational definition of interactive
CE behaviours on social media:
Customer engagement on social media refers to the inten-
sity of customer participation in relational exchanges with
a focal object on social media platforms. These interactions
are inherently multidimensional and driven by customer
needs, which can be direct or indirect. Direct engagement
occurs at the touch point of brand-generated information,
while indirect engagement can take place elsewhere on
social media, often happening simultaneously.
This definition offers explicit guidance for measuring
CE behaviours on social media, while outlining finite path-
ways that support exploratory research within its frame-
work. To enhance the validity and effectiveness of this
conceptualization, we propose the following premises: (a)
it is set within the context of developed markets; (b) the
targets on social media should ideally be equipped with
the potential of turning into fans for interested brand(s);
(c) brand-generated content should be the primary virtual
touchpoint for marketing practitioners; (d) customers pri-
marily engage in interactive brand activities through three
strategies: liking, sharing, and commenting (Schivinski et al.
2016), which reflect cognitive and emotional CE behaviours.
Particularly, the concept of fans mentioned in premise (b),
aligning with that in Sashi (2012), refers to the relation-
ship ultimately achieved through the CE cycle at the cost of
brands’ efforts in building commitment and emotional bonds
with customers.
Social media marketing activities for luxury brands
The compatibility of luxury brands with mass-media plat-
forms has conventionally been scrutinized due to the neces-
sity of maintaining uniqueness and exclusivity (Heine and
Berghaus 2014; Okonkwo 2009; Quach and Thaichon 2017).
However, as customer interactions increasingly shift to
social media, luxury brands must attentively monitor cus-
tomer responses and sentiments (Barger et al. 2016; Kunz
et al. 2017). Notably, Kim and Ko (2012) identified five key
dimensions of social media marketing efforts in the sector
context of luxury fashion brands: entertainment, interaction,
trendiness, customization, and word-of-mouth (WOM).
Entertainment focuses on luxury brands delivering engag-
ing and enjoyable content through social media. Research
indicated that entertainment is a primary motivator for con-
sumers to create user-generated content (Phelps et al. 2004).
The entertaining nature of content enhances its virality, as
engaging information is more likely to spread quickly across
social media (Dobele et al. 2007; Golan and Zaidner 2008).
Trendiness, as defined by Liu et al. (2021), pertains to the
extent to which luxury brands update their social media
content. About themselves. Studies suggest that trendiness
significantly influences consumer purchasing decisions as
brand-related messages are perceived as a more trustwor -
thy information source compared to traditional marketing
(Dauriz et al. 2014).
Interaction is crucial for luxury brands, facilitating the
sharing of opinions and experiences among users. Hennig-
Thurau et al. (2010) highlight that social media’s partici-
patory nature essentially encourages internal information
exchange and feedback through various formats, includ-
ing text, video, and images. Customization refers to the
tailored information or services luxury brands provide on
social media (Liu et al. 2021), enhancing the value exchange
between firms and customers. This digital strategy not only
reduces CE costs but also improves responsiveness.

187
Measuring social media customer engagement with brands based on information entropy: an…
Lastly, WOM signifies customers’ willingness to recom-
mend and share received information from social media
marketing with others (Liu et al. 2021). For this study, we
observed that the two terms representing the WOM construct
in (Kim and Ko 2012) align with the contribution dimen-
sion of participation strategies identified by (Schivinski et al.
2016). Both can be interpreted through engagement behav -
iours such as forwarding or quoting content, particularly in
the context of social media platforms. Consequently, Kim
and Ko’s WOM dimension is integrated into the framework
of interactive CE behaviour, serving as a dependent variable
for evaluating a brand’s social media marketing activities
(Entertainment, Interaction, Trendiness, Customization).
Approaches to measuring social media CE
behaviours
From the above discussion, CE on social media generally
reflects customers’ participation in brand-related activities
involving single or multiple focal objects. In this context, CE
behaviour is viewed as a response to social media content
or activities initiated by brands, which indicates the brand’s
effectiveness in communication strategies. Although many
existing efforts in exploring CE behaviours (e.g. Bai and
Yan 2020; Shah et al. 2019; Muñoz-Expósito et al 2017;
Guesalaga 2017; Ashley and Tuten 2015), measurement of
CE within the social media context remains limited (Schultz
and Peltier 2013), necessitating an overview of approaches
to measuring CE behaviours.
Overall, existing studies on measuring CE levels on
social media have employed either qualitative or quantitative
approaches. For instance, Ashley and Tuten (2015) utilized
content analysis to investigate how social media content
influences CE, leveraging secondary data from Engage-
mentdb (2009) to assess CE scores. Guesalaga (2016) and
Shah et al. (2019) applied regression models to illustrate
the impact of CE on firm performance and customer satis-
faction, respectively. Notably, when considering interviews,
whether internal (firm) or external (customer), engagement
was framed as the willingness to participate in interactive
experiences on social media, which could be quantified
using a scaled variable. These studies underscore the mul -
tifaceted nature of CE and its implications for both brands
and customers. However, a singular qualitative framework
may lack consistent measurement criteria, limiting the gen-
eralization of findings across different sectors.
The quantitative CE measurement in existing studies
emphasizes a comprehensive, data-driven strategy that uti-
lizes customer-related metrics to derive a final engagement
indicator (e.g. Bai & Yan 2020; Muñoz-Expósito et al 2017).
Essentially, composite measures effectively capture broad
constructs (Dearden et al. 2013), and have been applied in
relevant studies (Liu et al. 2021; Wu et al. 2019) for each
brand within a specified time frame. Muñoz-Expósito et al
(2017) proposed a CE involvement metric in a ratio form,
reflecting progress towards defined goals that facilitate con-
tinuous improvements for target brands on social media
(Peter et al. 2013).
Despite the advantages of providing indicators for CE
management on social media, the composite measure
method faces challenges, leading to significant research
gaps. First, actions of interest are often treated as equal
efforts by users, which weakens the interpretability and con-
sistency concerning marketing objectives. Second, efforts
to capture customers’ affective and cognitive behaviours
remain rare. In response to these difficulties, we propose an
entropy-based CE behaviour measurement framework, as
detailed in  "Methodology" section.
Methodology
Research framework
For this study, a data-centric CE decision support system has
been proposed, as depicted in Fig. 1. In the initial stage, it is
essential to establish the theoretical grounds that align with
the operational definition of CE behaviour outlined in  "CE
conceptualization" section. In the context of the luxury
industry, the EITC (entertainment, interaction, trendiness,
customization) framework was utilized to analyse social
media marketing activities, as demonstrated in  " Social
media marketing activities for luxury brands" section.
Specifically, a proxy method is employed to identify the
dimensions of ‘entertainment’ and ‘trendiness’ by assigning
a value of 0 (not identified) or 1 (identified) based on a pre-
defined set of keywords, as detailed in Table 4B of (Liu et al.
2021). The interaction dimension is qualified as the sum
of one plus the number of hashtags and mentions included
in a tweet, recognizing that each tweet represents a single
opportunity for interaction with customers. Furthermore, in
their examination of CE, Liu et al. (2021) defined customi-
zation as the frequency with which a brand replies to social
media users within a specified timeframe. This study adopts
a similar approach, using the count of brand replies under
each BGC as the measure of customization.
The second stage focuses on constructing an informa-
tive CE behaviour indicator that assesses the engagement
performance of each BGC. This approach facilitates direct
comparisons of BGCs’ engagement performance consist-
ently and objectively, as it avoids the inconvenience stem-
ming from the complexity of brand and customer-related
characteristics.
Subsequently, a fixed-effect model is employed to analyse
the impact of social media marketing activities on CE per -
formance, allowing for the extraction of the brand’s overall

188 S. Xiao, X. Chen
Fig. 1  The conceptual research framework

189
Measuring social media customer engagement with brands based on information entropy: an…
CE performance via introducing dummy variables. This
method effectively captures the degree of behavioural inter-
actions associated with CE. Additionally, the average senti-
ment score of CGCs that reference the same brand serves
as a proxy for customers’ affective engagement. This senti-
ment analysis supports further cluster analysis, providing
valuable insights into engagement marketing strategies for
practitioners.
Data collection and sample
This research selects Twitter as the data source. The reason
for choosing Twitter is that it is one of the most popular and
influential microblogging sites and is receiving increasing
attention from scholars from multiple disciplines (Jin and
Phua 2014). We used Tweepy, a Python library that ena-
bles accessing data through the Twitter API. This library
has been systematically applied to the study of social media
operations, for example, Hasson et al. (2019).
Inspired by Liu et al. (2021), we collected data from six
luxury brands: Armani, Burberry, Chanel, Dior, Gucci, and
Louis Vuitton (LV). This dataset encompasses tweets gath-
ered within a data range from 2017 to 2022, resulting in a
total of 18,964 BGCs from the selected brands. For senti-
ment analysis, we used the same tool to gather 25,991 CGCs
that included hashtags (‘#’) or mentions (‘@’) of the target
brands in August of 2022. Samples of the collected tweets
from both customers and brands are exhibited in Tables  9
and 10 in the Appendix. The following section will outline
the preparation of these unstructured data stages 2 & 3 in
Fig. 1.
Data processing
The tweet data for processing consists of textual contents
and numeric values. We stored the dataset in a DataFrame
format, and utilized Pandas, a Python package, to transform
the unstructured datasets. Unprocessed signs and words in
the texts can negatively impact the screening of keywords.
Consequently, two steps were taken to clean textual tweets
and implement EITC dimensions.
First, a series of NLP procedures, as outlined by Manning
and Schutze (1999), were applied to the collected 18,964
brand-generated and customer-generated tweets. In this
study, we focused particularly on textual variables related to
hashtags, mentions, and tweet texts. Four new columns were
created from the loaded raw data: the hashtag included in the
text, the number of hashtags, the textual format of mention,
and the number of mentions see columns 7–10 in Table 1.
Secondly, we applied a combination of functions to strip
punctuation, convert text to lowercase, and remove users
and website links to obtain cleaned content (column 11 in
Table 1). This cleaning process facilitates easier operations
in the subsequent steps. Note that some texts in Table 1 have
been omitted for conciseness.
Building upon the discussion in Sect.  3.1, we utilized
keyword dictionaries defining the dimensions of both enter-
tainment and trendiness. Specifically, if a tweet contained
any keyword from the dictionary, it was tagged with the
value of 1; otherwise, it received a value of 0 (columns 12
& 13 in Table 1). Additionally, the columns for hashtags and
mentions (columns 7 & 8) assist in verifying the consist -
ency and validity of contents, while the counts of hashtags
and mentions (columns 9 &10) measure the interaction and
customization. The results are presented in columns 14 &15.
Proposed entropy‑based engagement measurement
approach
The public metrics of social media content generated by
luxury brands are represented as discrete integers and follow
a non-uniform distribution. This indicates that the distribu-
tion is non-symmetrical and positively skewed, consistent
with findings from previous social media studies (Weinstein
2017; García-Perdomo et al., 2017; Burnap et al. 2014).
Through exploratory data analysis, we observed a long
tail effect in the number of replies and number of quotes,
with medians of 4 and 3, respectively. In contrast, the maxi-
mum values for these metrics reached 190,335 and 57,746,
highlighting significant disparities and serious skew inherent
in interactive metrics on social media.
Cousineau and Chartier (2010) explored outlier detection
and the influence of various types of outliers on research
objectives, concluding a transformation approach suitable
for data drawn from an unknown but asymmetrical popula-
tion. In this context, the outliers identified in Table 2 cannot
be simply removed from the dataset, as they significantly
contribute to the variance.
According to Cousineau and Chartier (2010), three com-
monly used transformations can help normalize the distri-
bution: log transform, square-root transform, and arcsin
transform. This research tested these three approaches, along
with a general transformation method, and found that the
square-root transformation and the general transformation
produced similar results with equally effective performance.
Consequently, this research adopts a sixth-root transforma-
tion, and the results of the data prepared for entropy calcula-
tion are presented in Table 3.
Next, Shannon entropy is applied to calculate the weight
for each engagement measure (number of retweets, replies,
likes and quotes) to derive the CE score. The process
involves three key steps to obtain the aggregated score for
each observation: (1) standardization of measured values
(Gorgij et al. 2017; Li et al. 2012); (2) Entropy value calcula-
tion (Ej) (Dong te al. 2018) for the j th criterion; (3) weight
calculation (wj) for the jth criterion.

190 S. Xiao, X. Chen
Table 1  Sample of prepared brand-generated observations
Tweet Retweet-count Reply_count Like_count Quote_count Brand Mentioned Hashtags hashtag_
count
Men-
tion_
count
Clean_tweet Enter-
tain-
ment
Trendiness Interaction Cus-
tomiza-
tion
Virginie Viard
has chosen
House ambas-
sador and
…Now
available in
boutiques
#CHANEL
96 7 246 2 Chanel [] [‘#CHANEL’] 1 0 Virginie viard
has chosen
house ambas-
sador and …
smithnow
available in
boutique-
schanel
0 1 2 0
CHANEL Con-
nects, the arts
&p; culture
podcast.@
EmeraldFen-
nell …
70 8 212 1 Chanel ['@Emerald-
Fennell', '@
TheGillian-
Flynn']
['#CHANEL-
Connects',
'#CHANEL']
2 2 Chanel con-
nects the arts
amp culture
podcastem-
eraldfennell
connects
with … now
on chanel-
connects
chanel
0 0 5 2
The Finale
of the
#CHANEL
Fall-Winter
2022/23
Haute Cou-
ture show
by Virginie
Viard. …
149 13 509 10 Chanel [] ['#CHANEL',
'#CHANEL-
HauteCouture']
2 0 The finale of
the chanel
fallwinter
202,223
haute couture
show by
virginie …
black and
silvermore at
chanelhaute-
couture
0 0 3 0
One minute
with
actresses
Carole
Bouquet
and Anna
Mouglalis
talking about
their vision
…https://t.
co/ 9Ynes
b8din
56 16 283 4 Chanel [] ['#CHANE-
LandCinema',
'#CHANELin-
Cannes',
'#CHANEL']
3 0 One minute
with
actresses car-
ole bouquet
and anna …
themchane-
landcinema
chanelin-
cannes
chanel
1 0 4 0

191
Measuring social media customer engagement with brands based on information entropy: an…
Assuming we have J  indicators and I  observations to
evaluate, with the measured value of the i th observation
under the j th indicator denoted as x ij (in this case, J  = 4,
I = 18,964).
Firstly, standardization of measured values. Before
obtaining the standardized value of x ij, the data were nor -
malized through:
Note that x min (j) is the minimum value for the value
and xmin (j) is the maximum value for the value in the j th
indicator, ymax and y min are the constants used to adjust
the lower boundary of the normalized dataset (y max = 1,
ymin = 0.02). Consequently, any value must be lying in the
range of [0.02, 1]. Then, the standardized value can be
calculated as:
The next step is calculating the information value E j for
each indicator:
Following the above equation, the weights of each indica-
tor can be obtained through the following formulation:
Here wj is the final entropy weight for the j  th indicator.
Finally, the customer engagement score for x ij is computed
as follows:
The validation of how Shannon entropy applies to CE
measurement and its results will be discussed in "Results
and discussion" section.
Hausman test and fixed‑effect model
A fixed-effect model was employed to analyse panel data
containing 11, 490 observations that start from 2019 Novem-
ber to 2022 August, alongside seven columns: period, brand,
engagement score, entertainment, interaction, trendiness,
and customization. Next, these observations were aggre-
gated by period, indexed as t = 1, …, T (with T = 34), and by
xij =/parenleft.s1ymax − ymin /parenright.s1 ∗ /parenleft.s2 xij − x(j) min /parenright.s2 ∕ /parenleft.s2 x(j) max − x(j) min /parenright.s2
+ ymin,, j = 1, … , J.
pij = xij∕
n/uni2211.s1
(i=1)
∗ xij, j = 1, … , J.
Ej =− 1∕ ln n ∗
/parenleft.s4 n/uni2211.s1
i=1
∗ pij ln pij
/parenright.s4
, j = 1, … , J.
wj = /parenleft.s11 − Ej /parenright.s1∕
/parenleft.s4 m/uni2211.s1
j=1
∗ /parenleft.s11 − Ej /parenright.s1
/parenright.s4
, j = 1, … , J.
SCustomer Engagement = w1 ∗ number of retweets + w2 ∗ number of replies
+ w3 ∗ number of likes + w4 ∗ number of quotes.
brand, indexed as n = 1,…, N (with N = 6), representing the
six luxury brands. To assess the impact level of each brand
on CE performance, dummy variables were created for the
‘brand’ variable, labelled with the names of the six brands.
As a result, we generated 204 observations (N X T) with 13
columns (seven original columns plus six dummy variables).
Before running the fixed-effect regression, the Hausman
test (Hausman 1978) was conducted to examine the endo-
geneity among the variables. The null hypothesis posits that
there is no endogeneity, which would suggest a random-
effect regression model. In this study, the Hausman test
results for the four dimensions all yielded p values less than
0.001, indicating the fixed-effect model was more appro-
priate for the analysis. The formulation of the fixed-effect
model is presented below:
Note that the β j (j = 1, 2, 3, 4) is the coefficient of each
independent variable, intercept is a constant and unknown
(Engagement)nt = b1 ∗( Entertainment)nt + b2 ∗( Interaction)nt
+ b3 ∗( Trendiness)nt + b4 ∗( Customization)nt
+ (Armani + Burberry + Chanel + Dior + Gucci + LV)
+ intercept + ent
Table 2  The descriptive result of public metrics of brand-generated
tweets
Retweet_count Reply_count Like_count Quote_count
Count 18,964 18,964 18,964 18,964
Mean 543.90 42.87 1990.94 33.47
Std 7025.35 1441.19 21,631.48 585.84
Min 0 0 0 0
25% 28 2 161 1
50% 50 4 359 3
75% 93 9 644 7
max 476,446 190,335 1,194,745 100
Table 3  The statistical result of public metrics of brand-generated
tweets after root transformation
The floating numbers in the table are kept to 4 decimal places
Retweet_count Reply_count Like_count Quote_count
Count 18,964 18,964 18,964 18,964
Mean 1.6822 1.1009 2.0637 1.0521
Std 0.3188 0.4758 0.5084 0.4909
Min 0 0 0 0
25% 1.5167 1.0905 1.8874 1.0000
50% 1.6307 1.1892 2.0863 1.1472
75% 1.7622 1.3160 2.2445 1.2755
max 5.1257 4.5702 5.7499 3.9372

192 S. Xiao, X. Chen
before obtaining the result, and ε nt represents random error
existing among variables.
Results and discussion
Customer engagement measurement results
This section presents the results of the CE score for each
Tweet. Figure 2 illustrates the distribution of CE scores for
the selected luxury brands. Overall, the engagement scores
for most tweets fall within the range of 25 to 40, rarely
exceeding 60. The mean score for the entire population is
29.59 while a median of 31.29. The 75th percentile score is
34.18, and the maximum score recorded is 100. The 25th
percentile is 27.95. This distribution highlights the concen-
tration of CE scores around the lower to mid-range, indicat-
ing that the majority of BGCs’ engagement levels remain
relatively modest.
Additionally, a boxplot was created to illustrate the key
statistic information for each brand, as presented in Fig.  2.
In terms of mean CE scores, Chanel outperformed the other
brands with an average score of 33.83, while Armani and
Burberry lagged with average values of 22.73 and 25.66,
respectively. The standard deviation (STD) further informs
us about the dispersion of the scores, reflecting both varia-
tion and stability. According to Fig. 2, Chanel demonstrates
the highest stability in its engagement scores, whereas Arm-
ani and Burberry exhibit a wider variation, indicating less
consistent performance (Fig. 3).
Comparison of different MCDM weighting methods
Examining the weighting results from the entropy method
reveals the following weights assigned to public meas-
ures: retweet (w 1) = 0.0756, reply (w 2) = 0.3632, like
(w3) = 0.1323, and quote (w 4) = 0.4288. To validate the
effectiveness of the entropy method, a Spearman ranking
correlation analysis was conducted, comparing the rankings
derived from the entropy method with brand value rankings
from the Brandirectory report (2022). The Spearman rank -
ing correlation is notably strong at 0.8286, with a p -value
of 0.0416, indicating a significant and positive correlation
while supporting the reliability of the proposed entropy CE
measurement approach.
Besides, considering the realm of complex decisions
and competing nature among selected weights within the
context of social media, we delved into other novel weight-
ing-based methods. Investigating recent advancements
in objective weighting methods, Criterion Impact Loss
(CILOS), Integrated Determination of Objective CRIteria
Weights (IDOCRIW), and Method Based on the Removal
Effects of Criteria (MEREC) are frequently adopted, as
reviewed by Ayan et al. (2023).
The weighting results obtained from the entropy,
CILOS, IDOCRIW, and MEREC methods are illustrated in
Fig. 4. Additionally, Table  4 provides a descriptive analy -
sis of the corresponding CE scores. The results imply that
the CE scores computed using the entropy method exhibit
a superior discriminatory power, characterized by higher
variation, facilitating a better way of distinguishing differ -
ent levels of engagement behaviours.
While the other weighting methods yield relatively sat-
isfactory score distributions, they inherently lack inter -
pretability within the text of social media engagement.
In contrast, The entropy method assigns to indicators that
display greater variation, providing a clearer understand-
ing of engagement dynamics.
For instance, the CILOS method evaluates importance
based on the relative loss of a criterion, suggesting that
the smaller the loss, the greater the weight assigned to
that criterion (Ayan et al. 2023), which is opposite to the
evaluation principles of Shannon entropy. In the context
of social media, the CILOS method can lead to misinter -
pretations when assessing CE levels of promotional BCGs.
We observed conflicts between the CILOS and entropy
methods particularly in two scenarios:
Fig. 2  Histogram chart for CE
scores by brand using all BGCs

193
Measuring social media customer engagement with brands based on information entropy: an…
Case (a): A sales promotion BGC that exhibited high
numbers of likes and retweets but significantly fewer
replies.
Case (b): An event-style BGC with a larger number
of replies compared to other metrics (few in likes and
retweets)
In case (a), the CILOS commonly assigned higher scores
to the BGC (30.45) based on weights shown in Fig. 4, while
the entropy method evaluated it lower (8.21) due to its rela-
tively low number of replies. Conversely, in case (b), the
entropy method assigned higher scores to the event-style
BGC, which received considerable engagement through
replies at a value of 11.74, while CILOS provided a lower
evaluation (2.89). It is important to mention that these scores
are used to illustrate the assessment gap between the two
weighting methods and a discrepancy that is also present
among other BGCs. This variation underscores the critical
need to select an appropriate weighting method, as it can
significantly influence the evaluation of CE performance
and subsequent marketing strategies informed by these
assessments.
The IDOCRIW method seeks to strike a balance between
the entropy and CILOS methods, positing that a weight
should decrease if its relative loss is higher than that of
other criteria (Zavadskas & Podvezko 2016). Although this
method offers a comprehensive consideration, particularly
in addressing country-wide productivity issues, the strong
interpretability provided by the entropy method suggests that
it is the better choice for analysing social media CE.
Lastly, the MEREC method assigns weights based on the
impact of a criterion when it is removed (Shanmugasundar
et al. 2022). However, it may be less effective in this context,
as all indicators in Table 3 exhibit a sharp range, character-
ized by a J-shaped distribution.
In summary, after comparing the entropy method with
alternative weighting approaches, it has been demonstrated
to be more persuasive, accurately reflecting real-world mar-
keting operations, and exhibiting stronger discriminatory
power. This leads to a more informative and reliable weight-
ing choice for this research.
Impact of brand’s social media marketing
on customer engagement
Among the initial 18,964 tweets, 1,368 were marked as
‘entertainment’ (with 17,596 were marked ‘0’), and 2,391
were marked ‘trendiness’ (with 16,573 were marked ‘0’.
The mean values of interaction and customization are
3.5920 and 0.5491, respectively.
After that, the fixed-effect model discussed in  "Haus-
man test and fixed-effect model" section was applied to
Fig. 3  Boxplot of CE scores by brand using all BGCs

194 S. Xiao, X. Chen
filter the data, resulting in a total of 11,490 observations.
These were grouped to ultimately yield 204 observations.
Additionally, dummy variables were then introduced to
assess the impact of brands themselves on CE behaviour
levels. By employing this approach, intrinsic characteris-
tics, including temporal fluctuations and variations stem-
ming from each brand’s brand-related characteristics such
as marketing strategy, were controlled for. This ensures
a reliable observation of the impacts of the independent
variables. The results of the fixed-effect model are pre-
sented in Table  5.
Considering the evolving nature of luxury brands, we
ran word clouds for two datasets: the full dataset of 18,964
tweets and a top-performance group with an average CE
score greater than 35. The results are illustrated in Fig.  5.
The left group results revealed significant trends with terms
like ‘style’, ‘first class’, and ‘fashion’ frequently appear -
ing. Besides, words associated with entertainment, such as
‘film’ and ‘festival’, were prominent. Other notable terms
that enhance brand identity include brand names, locations,
popular fashion items (e.g. ‘bag’, ‘watch’), and materials
(e.g. ‘leather’).
For the top-performance group, displayed on the right
side of Fig. 5, highlighted a focus on brand image reinforce-
ment in their social media efforts. In addition to common
terms (e.g. ‘collection’, ‘new’, ‘discover’), there was a nota-
ble presence of interaction-related terms: ‘show live’, ‘cel-
ebrate’, and ‘fashion show’.
After updating the dictionaries for entertainment and
trendiness with the newly identified terms, as shown in
Table  6, we re-ran the fixed-effect model. The result in
Table 7 indicated consistent trends with those in Table  5,
along with improvements in model fit.
In Table  7, the R square indicates that this regression
analysis explains 94% of the variation in CE scores attrib-
uted to the independent variables, while only 6% of the vari-
ation remains unexplained, suggesting that the minor varia-
tion results from random error. Examining the coefficients,
we found that the EITC dimensions of brands’ social media
marketing activities significantly impact the CE level, at a
significance level of 0.05. Similarly, the brands themselves
also demonstrated a significant effect on CE, thereby pro-
viding a unique ranking among the brands (Gucci  < Arm-
ani < Burberry < Chanel < LV < Dior), and allowing for fur-
ther benchmarking in the meanwhile (Table 8).
It is important to note that a brand’s coefficient derived
from the fixed-effect approach reflects its relative contribu-
tion to CE behaviours while controlling for other factors. A
negative coefficient does not necessarily imply a negative
impact on social media outcomes; rather, it indicates a lesser
contribution compared to other brands within the model.
In this context, the engagement level by a brand inherently
suggests a measure of efficiency, compared with the peer.
Fig. 4  Weighting results using
ENTROPY, CILOS, IDOCRIW
& MEREC methods
Table 4  Descriptive analysis of CE scores calculated from
ENTROPY, CILOS, IDOCRIW, MEREC weighting methods
The floating numbers in the table are kept to 4 decimal places
ENTROPY CILOS IDOCRIW MEREC
Count 18,964 18,964 18,964 18,964
Mean 29.5896 30.3409 31.3066 31.8325
Std 9.6448 8.0183 7.8800 7.6841
Min 3.1131 2.8930 6.2804 6.7350
25% 27.9472 31.6873 28.6342 28.9433
50% 31.2884 35.2044 32.0448 32.4200
75% 34.1796 37.9605 34.7503 35.1033
max 100 98.1943 97.9503 98.1259

195
Measuring social media customer engagement with brands based on information entropy: an…
Sentiment analysis
To measure the degree of emotional bonds, this research
used the average sentiment performance of a set of CGCs
as a proxy. We applied sentiment analysis to the cleaned
textual content of 25,991 collected customer-generated
tweets, utilizing the Natural Language Toolkit, a Python
library, to effectively capture sentiment changes.
Each tweet’s sentiment score ranges from − 1 to 1. The
analysis revealed that 32.05% (8, 331) of the tweets had
a positive sentiment score, while 4.78% (1, 242) were
categorized as negative. Comparatively, these proportions
differ significantly from those reported by Ibrahim and
Wang (2019a, b), where only 8% of tweets tested positive
and 9% negative. This disparity can be attributed to the
industry difference; while Ibrahim and Wang (2019a, b)
focused on retail sales, this paper targets customer senti-
ments towards luxury brands, leading to distinct senti-
ment results.
Clustering analysis
After deriving the behavioural engagement levels and mean
sentiment performance for each luxury brand, a cluster
analysis was performed to check for clusters that differen-
tiate these brands. The hierarchically structured clustering
approach, which computes Euclidean distances to iden-
tify neighbouring observations, was adopted to facilitate a
straightforward understanding of the clustering process. The
results of the hierarchical cluster analysis are presented in
Fig. 6, with the dendrogram illustrating the inherent group-
ings within the data. Four clusters were identified:
Cluster1 (LV, Chanel): Low affective & High behav -
ioural engagement
Cluster2 (Dior): High affective & High behavioural
engagement
Cluster3 (Gucci, Armani): High affective & Low
behavioural engagement
Cluster4 (Burberry): Low affective & Low behavioural
engagement
Table 5  The result of the fixed-effect model using original dictionar -
ies
Intercept = 302.5354, p value = 0.000
F-statistic = 290
R-squared = 0.928
Dimensions of social media mar-
keting activities
Customer engagement
coefficient p value
Entertainment 16.0075 0.000
Interaction 6.2004 0.000
Trendiness 11.2319 0.002
Customization  − 5.4094 0.002
Armani  − 242.3089 0.000
Burberry  − 224.8024 0.000
Chanel 147.4506 0.013
Dior 673.6616 0.000
Gucci  − 253.7275 0.001
LV 202.2621 0.004
Fig. 5  Word cloud result of all-tweets (left) and top-performance groups (right)

196 S. Xiao, X. Chen
Cluster 1, comprising Chanel and LV, demonstrates
efficiency in fostering behavioural engagement with cus-
tomers while showing less effectiveness in establishing
emotional bonds, as indicated by lower positive sentiment
scores. By the same token, Cluster 2, 3 and 4  highlight
varying levels of luxury brands’ efficiency in cultivating
both behavioural and affective engagement with their
customers.
Discussion
The fixed-effect model results suggest that a luxury brand’s
social media activities aimed at enhancing entertainment,
interaction, trendiness pay off regarding increasing engage-
ment performance of BGCs, aligning with findings by Liu
et al. (2021). Entertainment content is crucial for engaging
customers and motivating their participation in branding
activities, while trendiness ensures customers stay updated
with the latest products, enhancing brand positioning while
engaging customers (Straker and Wrigley 2016). Addition-
ally, interaction is vital for bridging the gap between custom-
ers and luxury brands, offering opportunities for CE despite
their exclusivity. Modern luxury brands (e.g. Tiffany, Burb-
erry) actively engage customers on social media, underscor-
ing the importance of aligning social media marketing with
customer growth strategies (Hughes et al. 2016; Straker and
Wrigley 2016).
Nevertheless, an unexpected finding was that improve-
ments in customization did not contribute to the engagement
performance of BGCs. One plausible explanation for this
is the incomplete detection of customized interaction with
customers, as we only accessed public comments on Twitter.
Table 6  Updated keywords dictionaries to identify dimensions of entertainment and trendiness
A. Entertainment dimension (total 63 words)
amuse, amuses, amused, amusing, amusement, anticipated, anticipation, anticipating, captivate, captivating, captivated, captivation, captivates,
clever, enjoying, enjoyment, enjoyable, compelling, entertain, entertainment, entertaining, feast, festival, festive, film, fun, funny, funnier,
funniest, good time, hilarious, humour, humourous, hysterical, hysterically, interesting, interested, laugh, laughter, laughing, mesmerizing,
mesmerized, pageantry, performance, performer, pleasure, recreation, red carpet, relaxing, relaxation, ridiculously, screaming, theatre, thrill,
thrilling, thrilled, witty, special, fashion show, celebrate, signature
B. Trendiness dimension (total 65 words)
best, catwalk, chic, classy, contemporary, cool, creative, dressy, elegant, elegantly, fabulous, fabulously, famous, fashion, fashionable, first class,
glamour, glamourous, gorgeous, gorgeously, icon, iconic, in vogue, influential, innovative, innovator, innovating, inspiring, inspiration, latest,
leading, leader, luxurious, luxury, modish, modern, newest, on-trend, pioneering, popular, renowned, styles, stylish, supermodel, superstar,
top, trend, trends, trendy, trend-setter, iconic, classic, bold, worn, haute, styled, special, model, colourful, tailoring, bontique, inspired, spirit,
creation
Table 7  The result of the fixed-effect model using updated dictionar -
ies
Intercept = 224.4412, p value = 0.000
F-statistic = 357.3
R-squared = 0.940
Dimensions of social media mar-
keting activities
Customer engagement
coefficient p value
Entertainment 14.8604 0.000
Interaction 5.2266 0.000
Trendiness 15.7664 0.000
Customization  − 3.5713 0.023
Armani  − 210.0108 0.000
Burberry  − 160.0156 0.002
Chanel 95.5087 0.066
Dior 577.4266 0.000
Gucci  − 256.1554 0.000
LV 177.6877 0.001
Table 8  Sentiment analysis
results for six luxury brands
The floating numbers in the table are kept to 4 decimal places
Brand name Armani Burberry Chanel Dior Gucci LV
Count 1325 6086 1322 6017 5204 6037
Mean 0.1374 0.1255 0.1377 0.1670 0.1459 0.1503
Min  − 0.8481  − 0.9100  − 0.8481  − 0.8834  − 0.9552  − 0.9485
25% 0 0 0 0 0 0
50% 0 0 0 0 0 0
75% 0.3400 0 0.3400 0.3612 0 0.2023
max 0.9493 0.9451 0.9493 0.9460 0.8910 0.9300

197
Measuring social media customer engagement with brands based on information entropy: an…
Brands may also directly message customers to provide ser-
vice or event information, as pointed out by Liu et al. (2021).
Furthermore, due to the innate characteristics of the Twitter
platform, many official comments from brands were directed
towards other official accounts rather than engaging custom-
ers, resulting in lower CE scores. Therefore, we encourage
future research to explore luxury brands’ customized com-
munication efforts on other social media platforms.
This study also categorized selected luxury brands based
on a quantitative pathway that measures the relational
exchange between customers and brands – specifically, the
CE level for a brand, and the degree of affective engage-
ment. To convert the clustering analysis results into action-
able marketing guides, we combined the Theory of Engage-
ment Marketing (Harmeling et al. 2017) with the CE matrix
(Sashi 2012).
First, on the premise that most interactions occurring at
the BGC touchpoint are from brand fans, we argue that the
ultimate goal of a CE strategy should be to transform cus-
tomers into fans, alongside customer acquisition. For brands
in Cluster 3 (Gucci, Armani), which demonstrate a high
degree of emotional bond but a lower degree of behavioural
exchange, there is likely a higher proportion of delighted
customers outside the fan group. This indicates that these
customers are developing affective commitment to the
brands, characterized by positive affective communication
and typically positioned in the advocacy stage in the CE
cycle, making them more likely to convert into fans (Sashi
2012). Therefore, we advocate for task-based engagement
initiatives that guide structured marketing actions (e.g. write
a review, refer a customer), mediated by psychology owner-
ship (Harmeling et al. 2017).
In contrast, brands in Cluster 1 (LV, Chanel) exhibit a
high degree of behavioural exchange with customers but
a lower degree of affective commitment. These brands are
likely to have a majority of loyal customers outside the
fan group, primarily driven by calculative commitment in
which switching costs or lack of alternative suppliers creates
lock-in or stickiness (Shashi 2012). Thus, building trust and
establishing long-term customer relationships are essential
for transforming them into fans. Experiential-based engage-
ment initiatives, psychological and emotional connections to
the brand and foster community among customers (Harmel-
ing et al. 2017). Regardless of the form these initiatives take,
the core focus should be on delivering ‘content’ and ‘value’,
with immediate and enduring communication playing an
important role.
Lastly, Dior in Cluster 1 serves as the benchmark for
remaining brands, boasting a significant fan base, whereas
Burberry falls into Cluster 4, implying a relatively larger
group of transactional customers. For Burberry, in addition
to adopting a combination of task-based and experiential
engagement initiatives, overall satisfaction would be a pri-
ority so that customers can be turned into either loyal or
delighted customers, eventually fans (Sashi 2012). For Dior,
engagement can be enhanced by strengthening existing rela-
tional bonds or fostering new cognitive connections. Impor-
tantly, customer acquisition should remain a primary focus,
given its high efficiency in building trust and commitment
with customers.
Fig. 6  Dendrogram of hierarchi-
cal cluster analysis

198 S. Xiao, X. Chen
Contributions, implications and limitations
Theoretical contributions
CE has gained increasing focus within the context of social
media due to its impact on both brand, customer and firm-
related outcomes, while. Despite already advancements in
CE conceptualization and social media-related research,
rare efforts have been made to build a measurable CE
framework that supports marketing efficiency on social
media platforms. This research contributes to relevant
theoretical developments in several ways.
First, while significant work has been done to con -
ceptualize CE (e.g. Hollebeek et al. 2014 ; Brodie et al.
2013; van Doorn et al. 2010), specific attributions of CE
as displayed on social media remain underexplored. This
study builds on Brodie et al’s (2013) definition of CE on
social media and integrates the CE cycle proposed by
(Sashi 2012), emphasizing the role of customer needs in
understanding CE behaviours. We extend this to create an
operational concept of interactive CE behaviour, consider -
ing contexts (social media platforms), setting (developed
market), and interactive customer behaviours that contrib-
ute to defined CE, based on (Schivinski et al. 2016).
Second, this paper reviews existing efforts to measure CE
behaviours on social media (e.g. Bai and Yan 2020; Shah
et al. 2019; Muñoz-Expósito et al 2017; Guesalaga 2017).
Various techniques have been taken to construct qualitative
expressions for CE behaviours. However, inconsistencies in
the criteria across these studies hinder the generalization of
their findings. This study proposes a CE behaviour measure-
ment framework that introduces the MCDM weighting tech-
nique -specifically, Shannon entropy, to assess engagement
performance for each social media message, enabling objec-
tive and consistent comparisons between brands. Notably,
this is the initial attempt to apply MCDM to CE research.
Third, studies examining the features of social media
content that enhance CE behaviours remain scarce (Wu
et al. 2019). Compared with previous studies (Liu et al.
2021; Wu et al. 2019) that mainly focus on communication
styles, this study, in addition, proposes a comprehensive
data-centric CE framework that considers both behavioural
and affective engagement within the social media commu-
nication context. By utilizing the Theory of Engagement
Marketing (Harmeling et al. 2017), we inform appropriate
engagement initiatives that enhance customer interactions.
Practical implications
The proposed entropy-based CE measurement approach
offers valuable managerial insights for brand marketers.
One key advantage is its capability to distinguish the CE
score of numerous BGCs by adopting an objective weight-
ing method. Thereby, this approach enables fair assess-
ment based on information entropy, identifying valuable
brand messages with meaningful score results. The derived
social media engagement measure further supports the
evaluation of target brands’ online marketing activities
through a fixed-effect regression model. If no endogeneity
exists among the desired variables, a random-effect model
can be applied. This novel framework controls for both
external and internal factors, allowing for the benchmark -
ing of different brands’ impact on their CE performance.
As a result, this framework enables brand managers to
more accurately assess their brands’ engagement with cus-
tomers via social media and provides actionable marketing
insights through clustering analysis.
In the context of the luxury brand sector explored in
this paper, the regression findings stressed the necessity of
adopting entertainment, interaction, and trendiness com-
munication styles to enhance brand engagement perfor -
mance through relaxing and engaging customers. Specifi-
cally, marketers can code social media messages that keep
customers informed about the latest products, styles, and
events. Moreover, to enhance entertainment, marketers can
collaborate with celebrities or online influencers to provoke
excitement and build brand cognition (Dauriz et al. 2014).
Next, brand practitioners are encouraged to let customers
join the co-creation of brand content, fostering the connec-
tion among the virtual brand community while cultivating
the psychological ownership of customers. Lastly, although
an unexpected outcome for the customization dimension of
marketing activities, the personalized experience matters in
the process of building emotional bonds with customers,
either online or offline.
Limitations and research pathways
This study acknowledges several limitations that present
key considerations for future studies. A primary concern
stems from studying a brand outside the scope of the dis-
cussed premise (b) (e.g. sports brands), in which case the
non-customer engagement will be mostly captured. In this
case, a different analysis pathway would support non-cus-
tomer engagement. Therefore, a thorough sectoral review
and expert consultations are essential before the CE evalu-
ation, for example, to answer the question of how much
potential your social media audience has to turn into your
customers. Second, the complex nature of social media plat-
forms may hinder us from deriving meaningful findings for
target brands. For instance, various social media channels
are adopted by the same brand (e.g. Facebook, Instagram),
and brand interaction, in the form of direct messages, may

199
Measuring social media customer engagement with brands based on information entropy: an…
lie outside the scope of findings derived via the proposed
research framework.
Third, we encourage future studies to evaluate brands’
social media marketing activities on CE performance using
dimensions beyond those in the EITC framework (Kim and
Ko 2012). For example, the growing importance of story -
telling, which can evoke customers’ emotional and affective
purchasing behaviours (Júnior et al. 2023), highlights the
need to incorporate this for a more comprehensive analysis.
Lastly, in the field of relationship marketing, CE encom-
passes not only the relationships between brands and cus-
tomers, but also the dynamics involving potential, actual cus-
tomers, and society in general (Muñoz-Expósito et al. 2017).
Engagement marketing explains the increasingly influential
role of customers as pseudo-marketers, emphasizing their
participation in co-creating brand value and their critical
impacts on other customers. It is essential to consider cus -
tomer-owned resources in the attributions of CE, advocat -
ing for the identification of social media influencers, who
are engaging in significant self-disclosures on social media
(Bastrygina et al. 2023; Joshi et al. 2023; Koay et al. 2023).
Practically, brand marketers can recognize influencers
through communication functions (e.g. mention, quote) on
social media, contributing to the total engagement score for
a brand over a specified period.
Appendix
See Tables 9, 10.
Table 9  Sample of collected brand-generated tweet data with brand label
Tweet Retweet Reply Like Quote Time Brand
The Giorgio Armani Lexicon: Travels https://t. co/ vXfmB MvwIO 21 6 122 0 2022–08-12T14:47:47.000Z Armani
Eduardo Scarpetta wore #GiorgioArmani to the 52nd Edition of the Gif-
foni Film Festival. https://t. co/ dYBIa bAWO5
13 11 80 1 2022–08-01T06:33:16.000Z Armani
Richard Madden wore #GiorgioArmani to attend the photocall at the
Giffoni Film Festival 2022
@_richardmadden https://t. co/ 0OqZr dnk3p
27 7 166 4 2022–08-01T06:27:33.000Z Armani
… … … … … … …
Tessa Thompson stars on the cover of Harper Bazaar August 2022 Issue
in #GiorgioArmani
@TessaThompson_x https://t. co/ dRwlC 4FM62
38 7 221 0 2022–08-01T06:26:45.000Z Armani
Table 10  Sample of user-generated tweet data (Armani)
The user account column is hidden in this sample for protecting user privacy
Tweet Follower Retweets Favourites Created time Brand
@HeymanHustle @WWERomanReigns @WWEUsos @USA_Network @
WWEonFOX @peacockTV @battistoniroma @Dolcepunta @ItaloFerretti
@armani Why call me I don't want no one to call me
21 0 0 20/08/2022 03:20:17 Armani
Le foto di Richard al #Giffoni22
non sono mai abbastanza
#richardmadden #richardinitalia  #rich_ardmaddenfanitalia20 #giffoni2022
#Giffoni2022 #Italia #armani #giorgioarmani #experienceaward #rich_ard-
maddenfanitalia20
#fanaccount #fanpage https://t. co/ krH48 50ExX
222 2 5 19/08/2022 18:18:37 Armani
… … … …
@HeymanHustle @WWERomanReigns @WWEUsos @USA_Network @
WWEonFOX @peacockTV @battistoniroma @Dolcepunta @ItaloFerretti
@armani You have my attention sir pls continue !
172 0 0 20/08/2022 02:09:53 Armani

200 S. Xiao, X. Chen
Acknowledgements The authors wish to declare that parts of this
submission are based on previous unpublished or assessed works by
Xiaoyu Chen. In particular, we wish to disclose the following works
An Entropy-based engagement measurement approach using natural
language processing-application in social media strategy for luxury
brands, as part of her Master’s thesis.
Declarations
Conflict of interest The authors certify that they have NO affiliations
with or involvement in any organization or entity with any financial in-
terest (such as honoraria; educational grants; participation in speakers’
bureaus; membership, employment, consultancies, stock ownership,
or other equity interest; and expert testimony or patent-licensing ar -
rangements), or non-financial interest (such as personal or professional
relationships, affiliations, knowledge or beliefs) in the subject matter of
materials discussed in this manuscript.
Open Access This article is licensed under a Creative Commons Attri-
bution 4.0 International License, which permits use, sharing, adapta-
tion, distribution and reproduction in any medium or format, as long
as you give appropriate credit to the original author(s) and the source,
provide a link to the Creative Commons licence, and indicate if changes
were made. The images or other third party material in this article are
included in the article’s Creative Commons licence, unless indicated
otherwise in a credit line to the material. If material is not included in
the article’s Creative Commons licence and your intended use is not
permitted by statutory regulation or exceeds the permitted use, you will
need to obtain permission directly from the copyright holder. To view a
copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
References
Ashley, C., and T. Tuten. 2015. Creative strategies in social media
marketing: An exploratory study of branded social content and
consumer engagement. Psychology & Marketing 32 (1): 15–27.
https:// doi. org/ 10. 1002/ mar. 20761.
Ayan, B., S. Abacıoğlu, and M.P. Basilio. 2023. A comprehensive
review of the novel weighting methods for multi-criteria deci-
sion-making. Information 14 (5): 285. https:// doi. org/ 10. 3390/
info1 40502 85.
Bai, L., and X. Yan. 2020. Impact of firm-generated content on firm
performance and consumer engagement: Evidence from social
media in China. Journal of Electronic Commerce Research 21
(1): 56–74.
Barger, V., J.W. Peltier, and D.E. Schultz. 2016. Social media and
consumer engagement: A review and research agenda. Journal
of Research in Interactive Marketing 10 (4): 268–287. https://
doi. org/ 10. 1108/ JRIM- 06- 2016- 0065.
Bastrygina, T., and W.M. Lim. 2023. Foundations of consumer
engagement with social media influencers. International Jour -
nal of Web Based Communities 19 (2/3): 222–242. https:// doi.
org/ 10. 1504/ IJWBC. 2023. 131410.
Basu, R., W.M. Lim, A. Kumar, and S. Kumar. 2023. Marketing ana-
lytics: The bridge between customer psychology and marketing
decision-making. Psychology & Marketing 40 (12): 2588–2611.
https:// doi. org/ 10. 1002/ mar. 21908.
Brandirectory. 2022. The annual report on the most valuable and
strongest luxury & premium brands 2022. https:// brand irect ory.
com/ ranki ngs/ luxury- and- premi um/ 2022.
Brodie, R.J., L.D. Hollebeek, B. Jurić, and A. Ilić. 2011. Customer
engagement. Journal of Service Research 14 (3): 252–271.
https:// doi. org/ 10. 1177/ 10946 70511 411703.
Brodie, R.J., A. Ilic, B. Juric, and L. Hollebeek. 2013. Consumer
engagement in a virtual brand community: An exploratory anal-
ysis. Journal of Business Research 66 (1): 105–114. https:// doi.
org/ 10. 1016/j. jbusr es. 2011. 07. 029.
Burnap, P., M.L. Williams, L. Sloan, O. Rana, W. Housley, A. Edwards,
V. Knight, R. Procter, and A. Voss. 2014. Tweeting the terror:
Modelling the social media reaction to the Woolwich terrorist
attack. Social Network Analysis and Mining 4 (1): 206. https://
doi. org/ 10. 1007/ s13278- 014- 0206-4.
Cousineau, D., and S. Chartier. 2010. Outliers detection and treatment:
A review. International Journal of Psychological Research 3 (1):
58–67. https:// doi. org/ 10. 21500/ 20112 084. 844.
Dauriz, L., N. Remy, and N. Sandri. 2014. Perspectives on retail and
consumers goods, 26–31. USA: McKinsey & Company.
Dearden, K., B. Crookston, H. Madanat, J. West, M. Penny, and S.
Cueto. 2013. What difference can fathers make? Early paternal
absence compromises Peruvian children’s growth. Maternal &
Child Nutrition 9 (1): 143–154. https:// doi. org/ 10. 1111/j. 1740-
8709. 2011. 00347.x.
Dobele, A., A. Lindgreen, M. Beverland, J. Vanhamme, and R. van
Wijk. 2007. Why pass on viral messages? Because they connect
emotionally. Business Horizons 50 (4): 291–304. https:// doi. org/
10. 1016/j. bushor. 2007. 01. 004.
Dong, G., J. Shen, Y. Jia, and F. Sun  2018. Comprehensive evaluation
of water resource security: Case study from Luoyang city, China.
Water 10(8): 1106. https:// doi. org/ 10. 3390/ w1008 1106
Duncan, S.Y., R. Chohan, and J.J. Ferreira. 2019. What makes the dif-
ference? Employee social media brand engagement. Journal of
Business & Industrial Marketing 34 (7): 1459–1467. https:// doi.
org/ 10. 1108/ jbim- 09- 2018- 0279.
Dwivedi, A. 2015. A higher-order model of consumer brand engage-
ment and its impact on loyalty intentions. Journal of Retailing
and Consumer Services 24: 100–109. https:// doi. org/ 10. 1016/j.
jretc onser. 2015. 02. 007.
Engagementdb. (2009). The world’s most valuable brands. Who’s
most engaged? Engagementdb ranking the top 100 global brands.
http:// www. engag ement db. com/ downl oads/ ENGAG EMENT db_
Report_ 2009. pdf.
García-Perdomo, V., R. Salaverría, D.K. Brown, and S. Harlow. 2018.
To share or not to share. Journalism Studies 19 (8): 1180–1201.
https:// doi. org/ 10. 1080/ 14616 70X. 2016. 12658 96.
Golan, G.J., and L. Zaidner. 2008. Creative strategies in viral adver -
tising: An application of Taylor’s six-segment message strategy
wheel. Journal of Computer-Mediated Communication 13 (4):
959–972. https:// doi. org/ 10. 1111/j. 1083- 6101. 2008. 00426.x.
Gorgij, A.D., O. Kisi, A.A. Moghaddam, and A. Taghipour, 2017.
Groundwater quality ranking for drinking purposes, using the
entropy method and the spatial autocorrelation index. Envi-
ronmental Earth Sciences 76(7). https:// doi. org/ 10. 1007/
s12665- 017- 6589-6
Guesalaga, R. 2016. The use of social media in sales: Individual and
organizational antecedents, and the role of customer engagement
in social media. Industrial Marketing Management 54: 71–79.
https:// doi. org/ 10. 1016/j. indma rman. 2015. 12. 002.
Harmeling, C.M., J.W. Moffett, M.J. Arnold, and B.D. Carlson. 2017.
Toward a theory of customer engagement marketing. Journal of
the Academy of Marketing Science 45 (3): 312–335. https:// doi.
org/ 10. 1007/ s11747- 016- 0509-2.
Hasson, S G., J. Piorkowski, and I. McCulloh, 2019. Social media as a
main source of customer feedback. Proceedings of the 2019 IEEE/
ACM International Conference on Advances in Social Networks
Analysis and Mining. https:// doi. org/ 10. 1145/ 33411 61. 33456 42.
Hausman, J.A. 1978. Specification tests in econometrics. Econometrica
46 (6): 1251. https:// doi. org/ 10. 2307/ 19138 27.
Heine, K., and B. Berghaus. 2014. Luxury goes digital: How to tackle
the digital luxury brand–consumer touchpoints. Journal of Global

201
Measuring social media customer engagement with brands based on information entropy: an…
Fashion Marketing 5 (3): 223–234. https:// doi. org/ 10. 1080/ 20932
685. 2014. 907606.
Hennig-Thurau, T., E.C. Malthouse, C. Friege, S. Gensler, L. Lobschat,
A. Rangaswamy, and B. Skiera. 2010. The impact of new media
on customer relationships. Journal of Service Research 13 (3):
311–330. https:// doi. org/ 10. 1177/ 10946 70510 375460.
Hollebeek, L.D. 2011. Demystifying customer brand engagement:
Exploring the loyalty nexus. Journal of Marketing Management
27 (7–8): 785–807. https://  doi. org/ 10. 1080/  02672  57X. 2010.
500132.
Hollebeek, L.D., M.S. Glynn, and R.J. Brodie. 2014. Consumer brand
engagement in social media: Conceptualization, scale develop-
ment and validation. Journal of Interactive Marketing 28 (2):
149–165. https:// doi. org/ 10. 1016/j. intmar. 2013. 12. 002.
Hughes, M.Ü., W.K. Bendoni, and E. Pehlivan. 2016. Storygiving as
a co-creation tool for luxury brands in the age of the internet: A
love story by Tiffany and thousands of lovers. Journal of Product
& Brand Management 25 (4): 357–364. https:// doi. org/ 10. 1108/
JPBM- 09- 2015- 0970.
Ibrahim, N.F., and X. Wang. 2019a. A text analytics approach for
online retailing service improvement: Evidence from Twitter.
Decision Support Systems 121: 37–50. https:// doi. org/ 10. 1016/j.
dss. 2019. 03. 002.
Ibrahim, N.F., and X. Wang. 2019b. Decoding the sentiment dynam -
ics of online retailing customers: Time series analysis of social
media. Computers in Human Behavior 96: 32–45. https:// doi. org/
10. 1016/j. chb. 2019. 02. 004.
Institute, M.S. 2022. MSI announces 2022–24 research priorities.
https:// www. msi. org/ artic le/ msi- annou nces- 2022- 24- resea rch-
prior ities/.
Ismagilova, E., Dwivedi, Y., Rana, N. 2020. Unanticipated Conse-
quences of Interactive Marketing: Systematic literature review
and directions for future research, 91–98. https:// doi. org/ 10. 1007/
978-3- 030- 47595-6_ 12.
Jin, S.A.A., and Phua, J. 2014. Following celebrities’ tweets about
brands: The impact of twitter-based electronic word-of-mouth on
consumers’ source credibility perception, buying intention, and
social identification with celebrities. Journal of Advertising 43(2):
181–195. https:// doi. org/ 10. 1080/ 00913 367. 2013. 827606
Joshi, Y., W.M. Lim, K. Jagani, and S. Kumar. 2023. Social media
influencer marketing: Foundations, trends, and ways forward.
Electronic Commerce Research. https:// doi. org/ 10. 1007/
s10660- 023- 09719-z.
Júnior, J.R.O., R. Limongi, W.M. Lim, J.K. Eastman, and S. Kumar.
2023. A story to sell: The influence of storytelling on consumers’
purchasing behavior. Psychology & Marketing 40 (2): 239–261.
https:// doi. org/ 10. 1002/ mar. 21758.
Kim, A.J., and E. Ko. 2012. Do social media marketing activities
enhance customer equity? An empirical study of luxury fashion
brand. Journal of Business Research 65 (10): 1480–1486. https://
doi. org/ 10. 1016/j. jbusr es. 2011. 10. 014.
Koay, K.Y., W.M. Lim, S. Kaur, K. Soh, and W.C. Poon. 2023. How
and when social media influencers’ intimate self-disclosure fos-
ters purchase intentions: The roles of congruency and parasocial
relationships. Marketing Intelligence & Planning 41 (6): 790–809.
https:// doi. org/ 10. 1108/ MIP- 06- 2023- 0246.
Kumar, V., and A. Pansari. 2016. Competitive advantage through
engagement. Journal of Marketing Research 53 (4): 497–514.
https:// doi. org/ 10. 1509/ jmr. 15. 0044.
Kunz, W., L. Aksoy, Y. Bart, K. Heinonen, S. Kabadayi, F.V. Ordenes,
M. Sigala, D. Diaz, and B. Theodoulidis. 2017. Customer engage-
ment in a big data world. Journal of Services Marketing 31 (2):
161–171. https:// doi. org/ 10. 1108/ JSM- 10- 2016- 0352.
Li, X., X. Wei, and Q. Huang, 2012. Comprehensive entropy weight
observability-controllability risk analysis and its application to
water resource decision-making. Water SA 38(4). https:// doi. org/
10. 4314/ wsa. v38i4. 13
Lim, W.M., S. Kumar, N. Pandey, T. Rasul, and V. Gaur. 2023. From
direct marketing to interactive marketing: A retrospective review
of the Journal of Research in Interactive Marketing. Journal of
Research in Interactive Marketing 17 (2): 232–256. https:// doi.
org/ 10. 1108/ JRIM- 11- 2021- 0276.
Lim, W.M., and T. Rasul. 2022. Customer engagement and social
media: Revisiting the past to inform the future. Journal of Busi-
ness Research 148 (1): 325–342. https:// doi. org/ 10. 1016/j. jbusr
es. 2022. 04. 068.
Lim, W.M., T. Rasul, S. Kumar, and M. Ala. 2021. Past, present, and
future of customer engagement. Journal of Business Research
140 (1): 439–458. https:// doi. org/ 10. 1016/j. jbusr es. 2021. 11. 014.
Liu, X., H. Shin, and A.C. Burns. 2021. Examining the impact of
luxury brand’s social media marketing on customer engagement:
Using big data analytics and natural language processing. Jour -
nal of Business Research 125: 815–826. https:// doi. org/ 10. 1016/j.
jbusr es. 2019. 04. 042.
Manning, D., and H. Schütze. 1999. Foundations of statistical natural
language processing. MIT Press.
McQuarrie, E.F., J. Miller, and B.J. Phillips. 2013. The megaphone
effect: Taste and audience in fashion blogging. Journal of Con -
sumer Research 40 (1): 136–158. https:// doi. org/ 10. 1086/ 669042.
Muñoz-Expósito, M., M.Á. Oviedo-García, and M. Castellanos-Ver -
dugo. 2017. How to measure engagement in Twitter: Advancing
a metric. Internet Research 27 (5): 1122–1148. https:// doi. org/ 10.
1108/ IntR- 06- 2016- 0170.
Okonkwo, U. 2009. Sustaining the luxury brand on the Internet. Jour-
nal of Brand Management 16 (5–6): 302–310. https:// doi. org/ 10.
1057/ bm. 2009.2.
Paschen, J., L. Pitt, and J. Kietzmann. 2019. Guest editorial. Journal of
Business & Industrial Marketing 34 (7): 1401–1402. https:// doi.
org/ 10. 1108/ jbim- 08- 2019- 416.
Peters, K., Y. Chen, A.M. Kaplan, B. Ognibeni, and K. Pauwels. 2013.
Social media metrics—A framework and guidelines for managing
social media. Journal of Interactive Marketing 27 (4): 281–298.
https:// doi. org/ 10. 1016/j. intmar. 2013. 09. 007.
Phelps, J.E., R. Lewis, L. Mobilio, D. Perry, and N. Raman. 2004. Viral
marketing or electronic word-of-mouth advertising: Examining
consumer responses and motivations to pass along email. Journal
of Advertising Research 44 (4): 333–348. https:// doi. org/ 10. 1017/
S0021 84990 40403 71.
Quach, S., and P. Thaichon. 2017. From connoisseur luxury to mass
luxury: Value co-creation and co-destruction in the online envi-
ronment. Journal of Business Research 81: 163–172. https:// doi.
org/ 10. 1016/j. jbusr es. 2017. 06. 015.
Sashi, C.M. 2012. Customer engagement, buyer-seller relationships,
and social media. Management Decision 50 (2): 253–272.
Schivinski, B., G. Christodoulides, and D. Dabrowski. 2016. Meas-
uring consumers’ engagement with brand-related social-media
content. Journal of Advertising Research 56 (1): 64–80. https://
doi. org/ 10. 2501/ JAR- 2016- 004.
Schultz, D.E., and J. Peltier. 2013. Social media’s slippery slope: Chal-
lenges, opportunities and future research directions. Journal of
Research in Interactive Marketing 7 (2): 86–99. https:// doi. org/
10. 1108/ JRIM- 12- 2012- 0054.
Shah, S.A.A., R. Sukmana, B.A. Fianto, M.A. Ahmad, I.U. Usman, and
W.A. Mallah. 2019. Effects of Halal social media and customer
engagement on brand satisfaction of Muslim customer. Journal
of Islamic Marketing 11 (6): 1671–1689. https:// doi. org/ 10. 1108/
JIMA- 06- 2019- 0119.
Shanmugasundar, G., G. Sapkota, R. Čep, and K. Kalita. 2022.
Application of MEREC in multi-criteria selection of optimal

202 S. Xiao, X. Chen
spray-painting robot. Processes 10 (6): 1172. https:// doi. org/ 10.
3390/ pr100 61172.
Shannon, C.E. 1948. A mathematical theory of communication. Bell
System Technical Journal 27 (4): 623–656. https:// doi. org/ 10.
1002/j. 1538- 7305. 1948. tb009 17.x.
So, K.K.F., C. King, B.A. Sparks, and Y. Wang. 2016. The role of
customer engagement in building consumer loyalty to tourism
brands. Journal of Travel Research 55 (1): 64–78. https:// doi. org/
10. 1177/ 00472 87514 541008.
Straker, K., and C. Wrigley. 2016. Emotionally engaging customers
in the digital age: The case study of “Burberry love.” Journal of
Fashion Marketing and Management 20 (3): 276–299. https:// doi.
org/ 10. 1108/ JFMM- 10- 2015- 0077.
van Doorn, J., K.N. Lemon, V. Mittal, S. Nass, D. Pick, P. Pirner, and
P.C. Verhoef. 2010. Customer engagement behavior: Theoretical
foundations and research directions. Journal of Service Research
13 (3): 253–266. https:// doi. org/ 10. 1177/ 10946 70510 375599.
Verhoef, P.C., W.J. Reinartz, and M. Krafft. 2010. Customer engage-
ment as a new perspective in customer management. Journal of
Service Research 13 (3): 247–252. https:// doi. org/ 10. 1177/ 10946
70510 375461.
Verleye, K., P. Gemmel, and D. Rangarajan. 2014. Managing engage-
ment behaviors in a network of customers and stakeholders. Jour-
nal of Service Research 17 (1): 68–84. https:// doi. org/ 10. 1177/
10946 70513 494015.
Wang, C.L. 2023. Interactive Marketing is the New Normal. In The Pal-
grave handbook of interactive marketing, 1–12. Springer Interna-
tional Publishing. https:// doi. org/ 10. 1007/ 978-3- 031- 14961-0_1.
Weinstein, E. 2017. Adolescents’ differential responses to social media
browsing: Exploring causes and consequences for intervention.
Computers in Human Behavior 76: 396–405. https:// doi. org/ 10.
1016/j. chb. 2017. 07. 038.
Wong, H.Y., and B. Merrilees. 2015. An empirical study of the ante-
cedents and consequences of brand engagement. Marketing Intel-
ligence & Planning 33 (4): 575–591. https:// doi. org/ 10. 1108/
mip- 08- 2014- 0145.
Wu, J., J. Chen, H. Chen, W. Dou, and D. Shao. 2019. What to say on
social media and how. Journal of Service Theory and Practice
29 (5/6): 691–707. https:// doi. org/ 10. 1108/ JSTP- 11- 2018- 0243.
Zavadskas, E.K., and V. Podvezko. 2016. Integrated Determination of
Objective Criteria Weights in MCDM. International Journal of
Information Technology & Decision Making  15 (02): 267–283.
https:// doi. org/ 10. 1142/ S0219 62201 65000 36.
Zhang, M., L. Guo, M. Hu, and W. Liu. 2017. Influence of customer
engagement with company social networks on stickiness: Medi-
ating effect of customer value creation. International Journal of
Information Management 37 (3): 229–240. https:// doi. org/ 10.
1016/j. ijinf omgt. 2016. 04. 010.
Publisher's Note Springer Nature remains neutral with regard to
jurisdictional claims in published maps and institutional affiliations.
Siwei Xiao is a graduated postgraduate from University of Bristol,
United Kingdom, majoring in Business Analytics. He obtained double
bachelor’s degrees from Yangzhou University in China (International
Business), and Charles Sturt University in Australia (Business Studies).
His research focuses on performance evaluation using data envelop-
ment analysis (DEA) and optimization algorithm in operations system,
as well as those applied to social media marketing analytics. He is also
interested in topics including statistics, predictive analysis, database
with their tools that are involved in information management.
Xiaoyu Chen is a graduated postgraduate from University of Bir -
mingham, United Kingdom, majoring in International Business. She
obtained her bachelor’s degree from Yangzhou University, China and
Charles Sturt University, Australia. Her interests lie in topics of brand
management, social media marketing and integrated marketing commu-
nication strategy. She is also interested in applying statistical analysis
to real-world problems discussed in corporate management strategy.
