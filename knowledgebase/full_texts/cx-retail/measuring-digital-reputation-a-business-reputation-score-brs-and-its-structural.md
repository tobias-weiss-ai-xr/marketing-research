---
title: 'Measuring digital reputation: a Business Reputation Score (BRS) and its structural and spatial
  drivers'
url: https://doi.org/10.1007/s10660-026-10202-8
category: cx-retail
subcategory: framework
date: 2026-09
venue: Electronic Commerce Research
authors:
- Hubert Wojewoda
- Katarzyna Kopczewska
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1007/s10660-026-10202-8.pdf
pages: 35
chars: 100929
fetched_at: '2026-11-08T18:47:21+00:00'
kb_version: 1
---

# Measuring digital reputation: a Business Reputation Score (BRS) and its structural and spatial drivers

Electronic Commerce Research
https://doi.org/10.1007/s10660-026-10202-8
Extended author information available on the last page of the article
Received: 20 April 2026 / Accepted: 8 September 2026
© The Author(s) 2026
Measuring digital reputation: a Business Reputation Score
(BRS) and its structural and spatial drivers
Hubert Wojewoda1 · Katarzyna Kopczewska1
Abstract
Digital reputation has become a critical asset for place-based service businesses,
where customer experiences are generated in physical locations but communicated
through digital platforms. However, digital reputation is typically measured using
isolated indicators such as average ratings or review volume, overlooking its mul -
tidimensional nature. This paper introduces the Business Reputation Score (BRS),
a composite indicator integrating perceived quality and market recognition into a
theoretically grounded measure of digital reputation. Using the Yelp Open Dataset
and an explainable machine learning framework (XGBoost–SHAP), we examine
how business characteristics, spatial context, and business category jointly shape
business reputation. The results highlight the importance of structural attributes,
neighbourhood quality spillovers, and category-specific effects, while demonstrat -
ing the value of interpretable machine learning for explaining digital reputation.
The findings are based on structured platform data and should be interpreted along -
side other reputation-forming mechanisms, including review content and platform
governance.
Highlights
 ● Proposes the Business Reputation Score (BRS) using star ratings and review
volume.
 ● Conceptualises digital reputation as a latent construct comprising perceived
quality and market recognition.
 ●  Evidences that the digital reputation of physical service businesses is spatially
embedded and depends on spatial spillovers.
 ● Applies XGBoost and SHAP to model and explain digital reputation.
 ● Reveals category-specific patterns in digital reputation formation across service
sectors.
Keywords Business Reputation Score (BRS) · Digital reputation · Online
reviews · Customer engagement · Spatial analysis

1 3
H. Wojewoda, K. Kopczewska
1 Introduction
Digital reputation has become one of the primary currencies of competition in plat -
form economies [1, 2]. Customer reviews, ratings and recommendations increasingly
shape consumer trust, purchasing decisions and firms’ competitive positions [ 3–5],
making digital reputation one of the most valuable intangible assets for any business.
Unlike traditional reputation, which develops gradually through direct interactions
and brand recognition, digital reputation is continuously co-created by customers [6]
and mediated by digital platforms that collect, aggregate, filter and present online
evaluations [ 7, 8]. As platform economies continue to expand, understanding and
measuring digital reputation has become an important challenge for both researchers
and practitioners [9].
Despite the growing literature on online reviews and electronic word-of-mouth
(eWOM), digital reputation remains difficult to measure [ 9]. Existing studies typi -
cally operationalise digital reputation using isolated indicators, including average
ratings, review volume, and textual sentiment, rather than treating reputation as a
multidimensional construct [9–11]. Empirical studies commonly rely on average rat-
ings, review volume, or sentiment extracted from textual reviews as separate proxies
for digital reputation [ 12, 13]. Although each of these measures captures an impor -
tant aspect of customer feedback, none reflects how reputation is actually perceived
in digital marketplaces. Consumers rarely evaluate ratings independently from the
number of reviews supporting them [ 14, 15]. Instead, they simultaneously interpret
customer satisfaction, customer engagement and the collective validation provided
by many reviewers [5, 16].
To address this mismatch, we introduce the Business Reputation Score (BRS), a
composite indicator integrating average customer ratings and review volume into a
single measure of digital reputation. Rather than measuring realised business per -
formance, the BRS captures the observable reputation of businesses as reflected in
customer evaluations on digital platforms [ 2, 7]. Building on this conceptualisation,
next we investigate the determinants of digital reputation by examining complemen-
tary dimensions: business characteristics and spatial context. We argue that digital
reputation is not only platform-mediated but also spatially embedded, since customer
experiences in stationary businesses are generated in physical places where neigh -
bouring businesses, local competition [17] and agglomeration processes [18–20] may
influence customer evaluations.
The empirical analysis uses the Yelp open dataset [1] and combines Extreme Gra-
dient Boosting (XGBoost) [ 21] with SHapley Additive exPlanations (SHAP) [ 22].
This framework allows not only to model complex, non-linear relationships between
business characteristics and digital reputation [23, 24], but also to interpret the rela -
tive importance of individual drivers [ 25], providing transparent and managerially
relevant insights into reputation formation.
This study makes four contributions to the literature. First, it reconceptualises
digital reputation as a multidimensional construct that jointly reflects perceived qual-
ity and market recognition, rather than treating online review metrics as independent
signals [14, 15]. Second, it develops new methodology by introducing the Business
Reputation Score (BRS), a theoretically grounded composite indicator [ 26]. Third,

1 3
Measuring digital reputation: a Business Reputation Score (BRS) and its…
empirically, it uses explainable machine learning to identify the determinants of
digital reputation [21, 22, 25]. Fourth, it contributes substantively by demonstrating
that digital reputation is spatially embedded, extending research on online reviews
beyond firm-level characteristics [1, 2] to include neighbourhood effects and spatial
spillovers [18, 20]. Collectively, these contributions advance the literature on digital
reputation in platform economies [9] by providing a transparent framework for mea-
suring and explaining business reputation using customer-generated data.
The paper is organised as follows. Section 2 develops the theoretical framework
for digital reputation and derives three research hypotheses: that business operational
attributes systematically influence digital reputation as measured by the BRS (H1),
that spatial proximity to high-quality businesses generates reputational spillovers
(H2), and that business category is systematically associated with digital reputation,
with the direction and magnitude of its contribution varying across service contexts
(H3). Section 3 describes the Yelp dataset. Section 4 develops the construction of the
BRS. Section 5 presents the XGBoost–SHAP analytical framework and reports the
empirical findings. Section 6 discusses theoretical and managerial implications, and
Sect. 7 concludes.
2 Literature review
2.1 Digital reputation as a theoretical construct
Reputation has long been recognised as one of the most important intangible assets
of organisations, influencing stakeholder trust, competitive advantage and long-term
organisational performance [ 27, 28]. Traditionally, reputation has been understood
as a collective evaluation formed gradually through repeated interactions between
organisations and their stakeholders [ 2, 7]. Unlike brand image, which can be
actively shaped through communication strategies, reputation emerges over time as
an externally constructed assessment of an organisation’s credibility, reliability and
quality [16, 27]. Although this understanding originated in corporate and strategic
management research, the rapid expansion of digital platforms has fundamentally
transformed both the mechanisms through which reputation is created and the ways
in which it is observed [7–9].
In digital platform economies, reputation is increasingly constructed through dig-
ital interactions among businesses, consumers and platform infrastructures [ 7, 8].
Customer evaluations, recommendations and online discussions continuously update
public perceptions of businesses [ 4, 5], while platform algorithms determine how
these signals are aggregated, prioritised and presented to potential customers [ 1, 29,
30]. Consequently, digital reputation should not be viewed simply as the online
equivalent of traditional corporate reputation. Rather, it represents a distinct construct
that emerges from the dynamic interaction between customer-generated information
and platform-mediated information processing [2, 7]. Reputation is therefore simul-
taneously social, digital and algorithmically mediated [8, 9, 30].
This perspective implies that digital reputation is not directly observable. Similar
to concepts such as competitiveness, resilience or quality of life, reputation represents

1 3
H. Wojewoda, K. Kopczewska
a latent construct that cannot be measured directly but must be inferred from observ-
able manifestations [26, 27, 31]. Individual indicators available on digital platforms,
such as customer ratings [ 1], review activity [ 4, 32], textual opinions [ 33, 34] or
other behavioural signals, should therefore be interpreted as observable expressions
of an underlying construct rather than as the construct itself [ 7, 16]. Distinguishing
between the theoretical concept of digital reputation and its empirical indicators is
essential for developing meaningful measures and avoiding conceptual ambiguity
[9, 15].
Conceptualising digital reputation as a latent construct also highlights its inher -
ently multidimensional nature [ 27, 31]. Reputation does not arise from a single
customer evaluation or a single platform metric. Instead, it reflects the cumulative
outcome of repeated customer experiences, collective judgements and market visibil-
ity [2, 7]. Consumers evaluate businesses by integrating multiple signals that differ in
both informational content and perceived credibility [ 14–16]. Consequently, digital
reputation should be understood as a higher-order construct emerging from several
complementary dimensions rather than as an attribute represented by a single observ-
able metric [9, 26].
Although the literature broadly acknowledges the strategic importance of digital
reputation [1, 30], considerably less attention has been devoted to its conceptualisa -
tion. Existing research predominantly examines the consequences of online reviews
[3, 4, 32] or analyses individual reputation-related indicators [ 15, 24], while rela -
tively few studies explicitly discuss what digital reputation represents as a theoretical
construct and how it should be distinguished from its empirical manifestations [ 9,
26]. This conceptual ambiguity has important implications for measurement. Before
asking how digital reputation should be measured, it is first necessary to establish
what digital reputation actually is [ 31]. The following section therefore examines
the multidimensional nature of digital reputation and identifies the dimensions that
should be considered when developing a theoretically grounded measure.
2.2 Dimensions of digital reputation
Building on the conceptualisation presented in the previous section, we argue that
digital reputation should be understood as a higher-order construct composed of two
complementary dimensions: perceived quality and market recognition [27, 31] (Fig.
1). Together, these dimensions capture not only how positively a business is evalu -
ated [1, 3], but also the extent to which these evaluations become collectively estab-
lished within the marketplace [7, 30]. While conceptually distinct, they jointly shape
consumers’ perceptions of business reputation and therefore should be considered
simultaneously rather than analysed in isolation [15, 26].
The first dimension, perceived quality, reflects customers’ evaluations of prod -
ucts and services based on their consumption experiences. It represents the quali -
tative component of digital reputation, expressing the degree to which a business
consistently meets or exceeds customer expectations [14, 16]. Within the literature on
electronic word-of-mouth, perceived quality has traditionally been operationalised
through customer ratings or similar evaluative measures that summarise post-con -
sumption satisfaction [ 1, 3, 4]. Positive evaluations reduce information asymmetry

1 3
Measuring digital reputation: a Business Reputation Score (BRS) and its…
[27, 28], increase trust [ 5, 7] and strengthen consumers’ willingness to purchase
[16, 35], making perceived quality one of the fundamental building blocks of digital
reputation.
However, high-quality evaluations alone are insufficient to establish a strong
reputation. A business evaluated positively by only a few customers communicates
a substantially weaker market signal than a business receiving consistently posi -
tive evaluations from hundreds or thousands of customers [ 27, 28]. This observa -
tion motivates the second dimension, market recognition, which reflects the extent
to which customer experiences become collectively visible and socially validated
within platform ecosystems [7, 30]. Market recognition captures the public acknowl-
edgement of a business through cumulative customer participation [1, 5]. It is there-
fore associated not with the quality of individual evaluations but with their collective
magnitude and visibility [ 15, 26]. Previous research has shown that larger volumes
of customer feedback increase the credibility, diagnostic value and perceived reliabil-
ity of online information, thereby strengthening consumers’ confidence in observed
evaluations [11, 14, 16].
Importantly, these two dimensions should not be interpreted as substitutes but as
complementary manifestations of digital reputation [26, 31]. High perceived quality
without market recognition may indicate excellent customer experiences that remain
insufficiently visible to influence broader market perceptions [ 27, 30]. Conversely,
high market recognition without favourable evaluations may reflect visibility rather
than positive reputation [29, 36]. Consumers integrate both dimensions when form -
ing judgements about businesses, simultaneously considering how positively a busi-
ness is evaluated and how broadly these evaluations are shared [ 11, 14, 15]. Digital
reputation therefore emerges from the interaction between perceived quality and
market recognition rather than from either dimension alone [9].
Fig. 1 Conceptual model of
digital reputation and its opera-
tionalisation through the Business
Reputation Score (BRS)

1 3
H. Wojewoda, K. Kopczewska
This conceptualisation distinguishes digital reputation from related constructs
frequently discussed in the literature. Customer satisfaction reflects individual
evaluations following consumption [ 23, 24], while customer engagement describes
behavioural interactions with digital platforms [ 5, 35]. Market recognition, in con -
trast, represents an aggregate market-level outcome generated through the accumu -
lation of these individual behaviours [ 7, 15]. Digital reputation is therefore broader
than either customer satisfaction or customer engagement because it captures how
businesses are collectively perceived within the marketplace rather than how indi -
vidual consumers think or behave [9, 30].
Conceptualising digital reputation through the complementary dimensions of
perceived quality and market recognition has important implications for measure -
ment [26, 31]. Existing studies predominantly operationalise reputation using iso -
lated indicators that represent only one of these dimensions, potentially overlooking
the broader construct they seek to explain [ 11, 15]. A theoretically grounded mea -
sure of digital reputation should therefore integrate both dimensions into a coherent
framework [9, 27]. The following section reviews the dominant approaches to mea -
suring digital reputation and demonstrates why existing operationalisations remain
incomplete.
2.3 From dimensions to measurement
Although digital reputation has become one of the central concepts in research on
electronic commerce and online platforms, its empirical operationalisation remains
fragmented [9, 11]. Existing studies typically rely on individual observable indica -
tors, such as average ratings [1, 3], review volume [4, 32], review sentiment [33, 34]
or review helpfulness [14, 15], depending on the specific research question and data
availability. While these indicators provide valuable insights into particular aspects
of customer feedback, each represents only a part of digital reputation rather than the
construct itself [26, 31].
Average customer ratings constitute the most widely used proxy for digital repu -
tation because they directly summarise customers’ evaluations of products and ser -
vices. Numerous studies have demonstrated that higher ratings positively influence
consumer trust, purchasing decisions and business performance [ 3, 4, 1]. However,
ratings alone provide limited information regarding the broader market position of
a business. Two businesses may receive identical average ratings despite substantial
differences in the amount of customer feedback supporting these evaluations [15, 29].
Review volume has therefore emerged as an additional indicator frequently
incorporated into studies of online reputation. Larger numbers of customer reviews
increase the visibility, credibility and perceived reliability of available information
while reducing uncertainty associated with isolated customer opinions [ 11, 14, 16].
Importantly, review volume does not represent customer satisfaction itself but rather
the degree to which customer experiences become collectively recognised within the
marketplace [7, 15]. It therefore reflects a distinct dimension of digital reputation
[26].
More recent research has further expanded the operationalisation of digital rep -
utation by incorporating textual sentiment [ 33, 34], linguistic characteristics [ 37],

1 3
Measuring digital reputation: a Business Reputation Score (BRS) and its…
review helpfulness [14, 15], reviewer credibility [16, 36] and other platform-specific
indicators [8, 24]. These approaches have substantially improved our understanding
of online reviews and consumer behaviour [11]. Nevertheless, they also illustrate the
growing conceptual diversity of digital reputation measurement, with different stud -
ies capturing different manifestations of the same underlying construct [9, 31].
Building on the conceptual framework developed in the previous sections, we
argue that the diversity of existing indicators should not be interpreted as evidence
that digital reputation lacks a coherent structure. Rather, individual indicators repre -
sent different empirical manifestations of the two underlying dimensions identified
earlier: perceived quality and market recognition. Average customer ratings primarily
operationalise perceived quality [ 1, 4], whereas review volume reflects market rec -
ognition [7, 15]. Considered separately, each captures only one dimension of digital
reputation. Considered jointly, however, they provide a theoretically coherent repre-
sentation of the broader construct [9, 26].
While this conceptual framework clarifies how digital reputation can be opera -
tionalised, it also highlights an important distinction between the latent construct and
its empirical representation. Customer experiences originate in physical interactions
between businesses and consumers, yet researchers and prospective customers do
not observe these experiences directly. Instead, they observe a platform-mediated
observable representation created through digital platforms that collect, aggregate,
rank, filter and display customer evaluations [ 7, 30, 38]. Consequently, digital repu-
tation should be understood not simply as the sum of customer opinions but as their
observed representation within a platform ecosystem, shaped jointly by customer
behaviour and platform governance mechanisms [11]. The Business Reputation Score
proposed in this study therefore operationalises this observable, platform-mediated
representation rather than the latent construct itself. This distinction acknowledges
that platform-specific processes—including review moderation, algorithmic ranking,
credibility assessment and the mitigation of review manipulation—may influence
how reputation is represented, even though the underlying customer experiences
remain unchanged [38, 39].
This reasoning motivates the development of the Business Reputation Score
(BRS), proposed as an empirical operationalisation of digital reputation. Rather than
introducing an additional reputation metric, the BRS integrates the two theoretically
grounded dimensions identified in the previous section into a single composite mea-
sure [31]. In doing so, it seeks to bridge the gap between the multidimensional nature
of digital reputation and the predominantly one-dimensional operationalisations
adopted in previous research [11, 15].
2.4 Determinants of digital reputation
Once digital reputation is conceptualised as a multidimensional construct and oper -
ationalised through the Business Reputation Score, the next question concerns its
determinants. Existing research has identified numerous factors influencing online
evaluations, ranging from service quality and business characteristics to platform
design and customer behaviour [ 8, 11, 24]. However, these factors have typically
been examined in isolation and using different operationalisations of reputation [ 9,

1 3
H. Wojewoda, K. Kopczewska
26]. Building on the conceptual framework developed in the previous sections, we
argue that the determinants of digital reputation can be organised into complemen -
tary domains: business-specific characteristics and spatial context, embedded within
a broader layer of platform-mediated mechanisms [7, 30] (Fig. 2).
The first group comprises business-specific characteristics, including operational
attributes, service quality, amenities and organisational features that directly shape
customer experiences [14, 16]. These characteristics influence how customers evalu-
ate businesses and therefore primarily affect the perceived quality dimension of digi-
tal reputation. Previous studies consistently show that factors such as service quality,
convenience, accessibility, price transparency and customer-oriented facilities con -
tribute to more favourable online evaluations and stronger digital reputation [1, 3, 4].
Secondly, although digital reputation is generated and communicated online, cus-
tomer experiences often remain fundamentally place-based. Restaurants, cafés and
other local service businesses operate in physical environments characterised by
spatial location, neighbourhood effects, local competition and agglomeration econo-
mies [18, 20]. Businesses located in attractive commercial districts may benefit from
increased customer flows and reputational spillovers [ 17, 18], whereas businesses
located in peripheral areas may experience lower visibility and weaker market recog-
nition despite comparable service quality [2]. This suggests that digital reputation is
spatially embedded [17, 20].
The third domain concerns digital platform mechanisms. Customer evaluations
are not observed directly by future consumers but are filtered, aggregated and pre -
sented through digital platforms [ 1, 7]. Consequently, reputation is co-created not
only by customers but also by platform architectures that influence review visibility,
ranking algorithms, recommendation systems and information presentation [ 8, 30].
Fig. 2 Design of the research model

1 3
Measuring digital reputation: a Business Reputation Score (BRS) and its…
Platform design therefore affects how digital reputation is formed, interpreted and
amplified within digital marketplaces [ 29, 30]. This perspective has gained increas -
ing attention in recent research on platform governance, review credibility and infor-
mation transparency [9, 11].
Digital platforms do not merely display customer evaluations but actively govern
how they become visible and influential. Through ranking algorithms, recommen -
dation systems, moderation policies and filtering mechanisms, platforms determine
which reviews are emphasised, suppressed or removed, thereby shaping the infor -
mation environment within which consumers form judgements. Consequently, the
reputation observed by users reflects not only customer experiences but also the
platform-specific processes through which user-generated content is organised, fil -
tered and presented [ 38, 40]. This perspective shifts attention from online reviews
as passive information to digital reputation as a platform-mediated representation of
customer experiences.
Platform governance has become increasingly important due to the growing
prevalence of review manipulation in digital marketplaces. Contemporary platforms
face diverse forms of information manipulation, including manipulated, incentivised,
coordinated and AI-generated reviews, which may distort consumers’ perceptions
and undermine trust in online evaluation systems [ 39, 41]. In response, platforms
invest heavily in credibility assessment, review filtering and automated moderation
mechanisms designed to detect suspicious content and preserve the integrity of digi-
tal reputation [ 42, 43]. Beyond improving information quality, these mechanisms
actively shape the reputation ultimately observed by platform users, as they deter -
mine which evaluations remain visible and credible within the platform ecosystem
[38, 40]. Furthermore, manipulated reviews influence not only perceived credibility
but also consumers’ purchasing decisions, reinforcing the importance of platform
governance for maintaining trustworthy reputation systems [44].
The present study does not seek to model these platform governance mechanisms
directly. Instead, it explains digital reputation as represented by structured platform
information, recognising that the Business Reputation Score operationalises the
observable outcome of customer evaluations after platform-level information pro -
cessing has taken place. Consequently, the BRS should be interpreted as a platform-
mediated representation of customer experiences rather than a direct measure of the
latent construct itself. This perspective acknowledges that observed reputation is
jointly shaped by customer behaviour, platform governance and the digital environ -
ment in which evaluations are created, curated and communicated.
Taken together, these three domains indicate that digital reputation emerges
through the interaction of operational, digital and spatial environments [ 7, 20, 30].
While previous research has extensively examined individual determinants, relatively
little attention has been devoted to integrating these perspectives within a common
conceptual framework [ 9, 26]. This framework provides the theoretical foundation
for the empirical analysis presented in the following sections, where the Business
Reputation Score is explained using business characteristics, spatial attributes and
platform-mediated information available through Yelp.

1 3
H. Wojewoda, K. Kopczewska
2.5  Digital reputation in space
The spatial dimension of digital reputation is an important component of the proposed
approach. It draws on agglomeration economics, which holds that firms co-located
in dense urban clusters benefit from knowledge spillovers, shared labour pools, and
heightened consumer traffic [20, 45]. Applied to the online context, geographic prox-
imity may generate reputational spillovers: customers visiting a high-quality cluster
are exposed to elevated service standards and are more likely to leave reviews, rais -
ing the digital visibility of the entire area [10, 17, 18].
Importantly, spatial context may affect both dimensions of digital reputation iden-
tified in this study in distinct ways. Local service environments influence perceived
quality by shaping customer expectations, reference points and competitive bench -
marking - consumers evaluate businesses relative to locally available alternatives
rather than in isolation [2, 17, 46]. At the same time, commercial density and neigh-
bourhood attractiveness affect market recognition, as businesses located in highly
active areas accumulate customer evaluations more rapidly and become more visible
within platform ecosystems [ 18, 20]. Spatial context therefore contributes not only
to how businesses are evaluated but also to how widely these evaluations become
recognised.
Despite these mechanisms, existing research on online reviews has paid relatively
limited attention to the geographical foundations of digital reputation. Most studies
explain reputation using business characteristics or platform-specific variables while
treating location primarily as a control variable rather than as a theoretically moti -
vated determinant [8, 24]. Such approaches overlook the possibility that reputation
itself may display spatial dependence because neighbouring businesses share similar
market conditions and customer environments [ 17, 20]. Integrating spatial charac -
teristics therefore extends existing theories of digital reputation by recognising that
online evaluations are rooted in place-based experiences [9].
2.6 Research hypotheses
Building on the theoretical framework developed in the preceding sections, this study
investigates three complementary domains through which digital reputation - opera-
tionalised as the Business Reputation Score - is shaped.
H1 for business characteristics: The first domain concerns business-specific
operational attributes. Service-dominant logic holds that value is co-created through
interactions between businesses and their customers, and that a firm’s capacity to
facilitate these interactions - through convenience features, accessibility options and
service quality - directly shapes customer experiences [6, 14]. Businesses that invest
in operational attributes signal their readiness to meet customer needs, thereby reduc-
ing perceived service risk and increasing the likelihood of positive evaluations [ 27,
28]. We therefore hypothesise that business operational attributes positively influence
digital reputation as measured by the BRS.
H2 for spatial context: The second domain concerns the geographic environment in
which businesses operate. Agglomeration theory holds that firms co-located in dense
commercial clusters benefit from knowledge spillovers, elevated local standards and

1 3
Measuring digital reputation: a Business Reputation Score (BRS) and its…
increased customer flows [18, 20]. Applied to digital reputation, geographic proxim-
ity to high-quality businesses may generate reputational spillovers that raise the BRS
of neighbouring establishments. We therefore hypothesise that spatial proximity to
high-quality businesses positively influences digital reputation as measured by the
BRS.
H3 for business category: The third domain concerns the moderating role of busi-
ness category. Customer expectations, emotional stakes and review behaviour vary
substantially across service contexts [ 23, 24]. Experiential categories - such as res -
taurants, cafés and entertainment venues - involve high-involvement consumption
experiences where positive outcomes generate enthusiastic reviews and negative
outcomes generate strong criticism. Transactional or high-stakes categories - such
as convenience stores or medical services - involve more routine or anxiety-laden
interactions where review patterns differ. We therefore hypothesise that business cat-
egory moderates the relationship between service attributes and digital reputation,
with experiential categories showing greater sensitivity to the quality of customer
experiences than transactional categories.
3 Data used in empirical analysis of Business Reputation Score and
its determinants
The empirical setting was selected to reflect the theoretical characteristics of digital
reputation developed in Sect. 2. An appropriate setting for studying digital reputation
should simultaneously capture customer evaluations, collective market recognition
and the place-based environments in which customer experiences occur. It should
therefore enable the observation of both dimensions of digital reputation - perceived
quality and market recognition—while providing information on the business and
spatial characteristics proposed in the research framework (Fig. 2).
The Yelp open dataset satisfies these requirements by offering one of the most
comprehensive publicly available sources of information from a digital platform on
local service businesses and customer-generated content. Yelp combines detailed
information on business characteristics, customer ratings, review activity, opera -
tional attributes and precise geographical locations across multiple service catego -
ries, available at https://www.yelp.com/dataset. Rather than representing merely a
source of online reviews, the Yelp ecosystem provides an empirical laboratory for
examining how digital reputation emerges through the interaction between customer
evaluations, platform mechanisms and local market environments (Table 1).
This empirical dataset directly operationalises the theoretical framework devel -
oped in the previous section. Customer ratings represent the perceived quality dimen-
sion of digital reputation, whereas review volume operationalises market recognition.
Business-related and spatial variables, in turn, represent the conceptual domains
proposed in the research framework (Fig. 2). Consequently, the empirical setting
provides a coherent translation of the theoretical model into an empirical design,
enabling the proposed operationalisation of digital reputation to be examined using
observable platform data (Table 2).

1 3
H. Wojewoda, K. Kopczewska
The empirical analysis focuses on place-based service businesses, including res -
taurants, cafés and other establishments whose reputation is formed through direct
customer experiences occurring in physical locations. This context is particularly
appropriate because customer evaluations simultaneously reflect service quality,
business characteristics and neighbourhood conditions. Consequently, digital reputa-
tion can be analysed not only as a platform-mediated phenomenon but also as one
embedded within local commercial environments.
Table 1 Summary of variables from the ‘business.json’ YELP dataset
Variable name Variable description
business_id Unique business identification
name The business’s name
address, city, state, postal
code
Full address of the business, its city, state and postal code
longitude, latitude Longitude and latitude (to 10 decimal places), precise geo-location of
business
stars Star rating, rounded to half-stars
review_count Number of reviews
is_open Dummy variable, 0 for closed, 1 for open
attributes Business attributes: DriveThru (collection of food from the car), BYOB
(bring your own bottle (e.g. of soft drink or alcohol), Wheelchair
Accessible, Dogs Allowed, HasAddress, Business Accepts Bitcoin,
Restaurants Table Service, By Appointment Only (reserved tables),
Corkage (extra fee for own wine), Happy Hour (cheaper during
off-peak hours), Has Hours, Smoking, WiFi, Bike Parking, Business
Parking, Restaurants Reservations, Coat Check, Caters, Restaurants
Delivery, Business Accepts Credit Cards, BYOB Corkage, Alcohol,
HasTV , Restaurants Take Out, Outdoor Seating, Good For Kids,
Restaurants Price Range, Restaurants Attire, Noise Level, Restaurants
Good For Groups, Ambience, Accepts Insurance, Good For Dancing,
Music, Good For Meal, Hair Specializes In, Best Nights, Ages Allowed,
Dietary Restrictions, Restaurants Counter Service, Open24Hours
categories Business categories (e.g. Restaurant, Tattoo Shop, Convenience store)
average_score_proximity,
businesses_in_proximity
Spatial variables characterizing neighbourhoods; illustrates the
BRS of neighbouring business units and number of business in the
neighbourhoods
Table 2 Operationalisation of the theoretical framework
Theoretical domain Theoretical concept Empirical indicator(s) Variables used
Digital reputation Perceived Quality Average customer
evaluation
stars
Market Recognition Customer participation review_count
Business
characteristics
Service attributes Amenities and business
features
WiFi, Alcohol, OutdoorSeat-
ing, RestaurantsPriceRange2,
BusinessParking, …
Accessibility Accessibility features BikeParking, RestaurantsDe-
livery, RestaurantsTakeOut, …
Spatial
environment
Local business
environment
Neighbourhood
characteristics
spatial density, neighbour
quality, competition, …
Platform
environment
Platform-based
information
Context of the analysis Type of platform

1 3
Measuring digital reputation: a Business Reputation Score (BRS) and its…
4 Business Reputation Score: construction and empirical calibration
Building on the theoretical framework and the operationalisation developed in the
previous sections, we now specify the formula for the Business Reputation Score
(BRS) as:
 𝐵𝐵𝐵𝐵𝐵𝐵 𝐵 (𝛼𝛼 ×𝐵𝐵 ) + (𝛽𝛽 × 𝑙𝑙𝑙𝑙𝑙𝑙 (𝐵𝐵 + 𝑙)) (1)
where S is the star rating, R is the number of reviews, log is natural logarithm and α,
β are weights reflecting the relative importance of the star rating and the number of
reviews, respectively.
This BRS metric is simple and efficient because it consists of only the two vari -
ables that matter to most customers and captures the critical aspects of customer
feedback that impact business reputation. The star rating represents perceived qual -
ity, whereas the number of reviews captures market recognition generated through
cumulative customer participation. It integrates both the quantitative aspect of review
counts and the qualitative aspect of star ratings. The inclusion of the logarithm of the
number of reviews accounts for diminishing returns, recognising that an increase
in reviews has a greater impact when the total number of reviews is low, and a less
significant impact as the number of reviews increases. The role of weights (α, β) is to
balance both components and is discussed below.
Composite indicators may be constructed according to two complementary phi -
losophies. One approach derives weights empirically, for example through optimisa-
tion procedures, statistical learning or calibration against external outcomes, with the
primary objective of maximising predictive performance. The alternative approach
assigns weights based on theoretical considerations, aiming to preserve conceptual
interpretability and consistency with the underlying construct [ 26, 31]. Since the
purpose of the Business Reputation Score is not to maximise predictive accuracy
but to operationalise the observable, platform-mediated representation of a theoreti -
cally defined latent construct, we deliberately adopt the latter approach. The selected
weights therefore reflect the conceptual balance between the two dimensions of digi-
tal reputation—perceived quality and market recognition—while the subsequent sen-
sitivity analysis verifies that the resulting ranking remains robust across plausible
alternative specifications. This philosophy is consistent with the broader practice of
constructing composite indicators for latent socio-economic constructs, where theo -
retical interpretability typically takes precedence over predictive optimisation.
As the BRS is a relationship between the number of reviews and the star rating, it
is important to see how the data relates statistically. Figure 3 shows this relationship
for Yelp dataset - it is clear that the extremes - the lowest and highest - occur less
frequently than other ratings. The distribution shows a slightly greater representation
of higher values, but in general the ratings are balanced.
The level of star ratings is known – always between 1 and 5 (on Yelp platform),
while the typical number of online reviews ranges from a few reviews to several thou-
sand. Logarithms make these values much more similar, for example, log(5) = 1.61,
log(10) = 2.30, log(50) = 3.91, log(100) = 4.61, log(500) = 6.21, log(1,000) = 6.91,
log(5,000) = 8.52, log(10,000) = 9.21, log(15,000) = 9.62, log(20,000) = 9.90. For

1 3
H. Wojewoda, K. Kopczewska
these numbers, the logarithm is between approximately 1 and 10, similar to the dou-
bled star rating. This is also visible in Fig. 3, where log(reviews) ranges from 2 to 9
which is approximately two times the range of ratings (from 1 to 5).
The final form of the Business Reputation Score (BRS), as previously presented
in Eq. (1), requires the setting of weights. Their role is not to optimise predictive per-
formance but to ensure that both conceptual dimensions contribute proportionately to
the composite indicator. Therefore, in order to give both components approximately
equal weight in the BRS, one needs to double-weight the ratings – therefore we set
coefficient for star ratings α = 2 and coefficient for log(reviews) β = 1. This gives the
following form for the BRS:
 𝐵𝐵𝐵𝐵𝐵𝐵 𝐵 (2×𝐵𝐵 ) + (1 × 𝑙𝑙𝑙𝑙𝑙𝑙 (𝐵𝐵 + 1)) (2)
The construction of the BRS with the selected weights gives reasonably balanced
results. Approximately half of the input to the BRS comes from the star rating and
half from the number of reviews. BRS in this form ranges from ca. 3.6 for 1 star and 4
reviews (1*2 + log(5) = 2 + 1.61 = 3.61) to ca. 20 for 5 stars and 20,000 reviews (5*2 +
log(20000) = 10 + 9.90 = 19.90). Figure 4 illustrates the values of BRS, depending on
the combination of star rating and number of reviews. Businesses with the same aver-
age star rating will have different BRS values, lower for fewer reviews and higher for
more. Values below 12 indicate a poor reputation, while values above 16 indicate a
well-grounded reputation.
Fig. 3 Understanding the scale of digital assessment - number of log(reviews) by star rating in Yelp
dataset. The graph shows the distribution of star rating on the x-axis and the logarithm of the number
of reviews on y-axis. The highest (5) and lowest (1) ratings are rarely achieved, while other ratings are
more common. It is also visible that log(reviews) ranges from 2 to 9 what is approximately two times
the range of ratings (from 1 to 5)

1 3
Measuring digital reputation: a Business Reputation Score (BRS) and its…
As the weights α and β are the essential elements of the BRS, a sensitivity analysis
was conducted to verify that the substantive findings are not an artefact of this particu-
lar parameterisation. We calculated the rank correlation (Spearman’s ρ) between BRS
computed with α = 2, β = 1 and alternative specifications (α = 1.5, β = 1; α = 2, β = 0.5;
α = 3, β = 1) - it exceeds 0.97 across all Yelp businesses in the sample, confirming
that the ranking of businesses and the direction of the XGBoost feature importances
are stable across plausible weight choices. This robustness analysis suggests that the
substantive conclusions of the study are not driven by a particular weighting speci -
fication but by the underlying relationship between perceived quality and market
recognition. However, weights α = 2, β = 1 should be changed if the ratings scale is
different - for example, if a different platform ranges ratings from 1 to 10. Upscaling
the number of reviews is less important, since log(1,000,000) is 13.81 and this is still
close to the scale used in this case.
The resulting empirical BRS for Yelp with weights α = 2, β = 1 has a minimum
value of 3.79 and a maximum value of 17.71, with most businesses scoring between
10 and 12 (mean = 10.26), as visualised in Fig. 5 (more in Appendix).
5 Determinants of digital reputation—empirical analysis
5.1 The design of the study
The previous section developed the Business Reputation Score (BRS), a composite
indicator that integrates two dimensions of digital reputation: perceived quality, rep-
resented by average ratings, and market recognition, represented by review volume.
It shows that some companies have a higher BRS than others. The open question is
what determines whether a company is well and massively rated online. This chapter
Fig. 4 Simulated Business Repu-
tation Score values for different
combinations of star ratings (y
axis) and number of reviews (x
axis). Graph shows the possible
values of BRS depending on stars
rating (on y-axis) and number of
reviews (on x-axis). The highest
values of BRS (in red, around 20)
require highest star ratings (4.5 or
5) and several thousand reviews

1 3
H. Wojewoda, K. Kopczewska
builds the quantitative model that explains the factors that determine BRS – busi -
nesses features and spatial environment, as shown in Table 2.
We use the spatial machine learning XGBoost model [ 47]. It is a well-known
and widely used gradient boosting algorithm based on decision trees that has gained
popularity due to its high-quality prediction capabilities. It is known for its efficiency
and effectiveness in dealing with a complex and non-linear datasets. Interpretation
of results is possible with XAI (Explainable AI). The whole methodology assumes
careful data preparation, model selection and rigorous validation, to provide insights
that are both actionable and based on empirical evidence.
Feature selection emerges as a critical phase in this methodology, as the number
of features can quickly become excessive with such complex and extensive data. It
is necessary to ensure that only the most relevant variables are included in the final
analysis. Using a combination of XGBoost feature importance scores and statisti -
cal tests, variables are carefully selected from the data to isolate those features that
have the most predictive power. This selection process not only improves the per -
formance of the models, but also ensures that the results are based on statistically
significant data, thereby increasing the credibility and relevance of the conclusions.
Several evaluation metrics are used to determine the effectiveness of the models:
MAE (Mean Absolute Error), R² (Coefficient of Determination), and MAPE (Mean
Absolute Percentage Error). They enable finding a final model that may have limited
variables due to feature selection and works with optimised hyperparameters.
To ensure the reliability of the analysis results, 5-fold cross-validation has been
used, a technique that ensures the robustness of the analysis. By dividing the dataset
into five parts and iteratively using four parts for training and one part for testing, the
risk of over-fitting can be reduced and the metrics provides a more reliable estimate
of how the models are likely to perform on unknown data. Conducting the analysis
in this way ensures that the accuracy of the model is not just a matter of luck. The
analysis was carried out using the Python packages ‘dalex’ and ‘shap’.
Fig. 5 Histogram of Business
Reputation Score (BRS) for Yelp
dataset. This histogram presents
the frequency (on y-axis) of
particular BRS values (on x-axis)
as calculated for the Yelp dataset.
The most frequent are values
around 11 and 12

1 3
Measuring digital reputation: a Business Reputation Score (BRS) and its…
5.2 Empirical model to detect key drivers of digital reputation
Because XGBoost is a tree-based model, it cannot be expressed as equation in addi -
tive form (as is common in econometric models), but as a general functional form:
 𝐵𝐵𝐵𝐵𝐵𝐵 𝐵 𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵 𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵 𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵 𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵  (3)
where business attributes and spatial environment were defined in Tables 1 and 2.
We used MAE, MAPE and R² to assess the quality of the estimation. In the final
model with the selected parameters and features, these metrics are as follows: MAE
= 1.434, R²=0.385, MAPE = 16.4%. With an MAE of 1.434, the model’s predictions
deviate on average by approximately 1.4 BRS units from the actual values. The R²
of 0.385 indicates that the structural features available in the Yelp dataset - business
attributes, spatial context, and category membership - account for roughly 38.5% of
the variance in the BRS. This level of fit is consistent with cross-sectional studies
predicting subjective business performance from observational data [ 2, 23] (more
in Appendix). Non-explained variation may stem from the sentiment and content
quality of individual reviews, seasonal fluctuations in customer traffic, managerial
responsiveness to negative feedback, and idiosyncratic local factors such as recent
media coverage or neighbourhood gentrification. Incorporating textual sentiment
analysis alongside structured attributes [24, 33] represents a promising direction for
improving predictive power in future work.
Figure 6 compares predicted and observed BRS values across the score distribu -
tion. Prediction error is substantially higher in the mid-range (BRS approximately
Fig. 6 Prediction error for optimized model

1 3
H. Wojewoda, K. Kopczewska
9–12) than at the extremes. This pattern is theoretically interpretable: businesses at
the high and low ends of the distribution exhibit consistent, easily detectable attri -
bute profiles - consistently excellent service and high engagement versus persistent
operational failures and minimal engagement - making them reliably predictable
from structured features. Businesses in the middle range, by contrast, are subject to
a greater mix of confounding influences: heterogeneous customer segments, incon -
sistent service delivery, category overlap, and the partial randomness inherent in
individual review decisions [48]. This finding aligns with research showing that con-
sumer ratings for “average” businesses are particularly sensitive to contextual noise
[7]. It underscores the importance of model transparency: rather than treating the
XGBoost output as a definitive prediction, practitioners should use it as a diagnostic
tool that highlights structural drivers of success, with explicit acknowledgement of
its limitations in the middle ground.
Understanding the drivers of quality and prediction performance can be based on
the importance of the XGBoost features. Figure 7 shows the most important variables
in the model - it shows how important each feature is to the predictions. The values
Fig. 7 Feature importance in XGBoost model. The longer the bar of the variable importance, the more
essential that variable is for explaining BRS

1 3
Measuring digital reputation: a Business Reputation Score (BRS) and its…
shown are the ‘gain’ - the improvement in accuracy that each feature brings when
used in the trees of the model [ 21]. During training, XGBoost builds decision trees
that split on the features that most reduce impurity. The importance of each feature
is then measured based on how often it is used in these splits and the magnitude of
its impact on performance. This process produces a list of features ranked by their
contribution to model accuracy.
The feature importance (Fig. 7) shows that the type of dining experience - spe -
cifically service settings such as casual, street and dinner - dominate as the most
influential factors in predicting business success. This suggests that attributes com -
monly associated with the restaurant sector are important to the performance of the
model. This seems logical, as customers today often check reviews before going to
a restaurant and write a review if their experience was either good or bad. In addi -
tion, convenience features such as DriveThru and WiFi availability, as well as acces-
sibility options such as WheelchairAccessible and BikeParking, have a significant
impact on customer satisfaction and reviews [ 5, 14]. The hours_open variable also
appears to be one of the most important, depending on the model. Meal specifics
and price points also play a crucial role, with features such as lunch and various
RestaurantsPriceRange categories indicating their importance. Less influential, but
still notable, are attributes related to dining atmosphere and policies, such as Classy
and NoiseLevel. Importantly, these variables also include the spatial variable created
earlier - average_score_proximity. This means that the scores of competitors or busi-
nesses in the vicinity of a business are relevant in determining its score.
These findings support H1, as structural attributes—particularly those related to
accessibility and convenience—are among the strongest predictors of digital reputa-
tion measured by the BRS. This is consistent with the service-dominant logic premise
that a firm’s capacity to facilitate customer interactions directly shapes how those
interactions are evaluated and recorded on digital platforms.
One can also analyse the differential impact of customer ratings across different
business categories. To investigate these effects, Shapley scores and summary plots
were used (Fig. 8), which provide insight into the contribution of each feature to the
model’s predictions.
This SHAP (Shapley Additive exPlanations) summary plot visualises the impact
of different features on the output of the model, specifically how each feature con -
tributes to the prediction of the business success score. SHAP values provide a way
of interpreting complex models by assigning each feature an importance value for a
particular prediction [22]. Positive SHAP values indicate that the feature contributes
to higher model output, while negative SHAP values indicate lower model output.
The colour coding represents the feature values, with red indicating high feature val-
ues and blue indicating low feature values.
The graph shows how different business categories (binary variables indicating
the presence or absence of certain attributes) influence the model’s predictions. For
example, ‘categories_Fast Food’ has a predominantly negative SHAP value, sug -
gesting that being classified as a fast food restaurant generally contributes negatively
to the business rating. Conversely, ‘categories_Arts & Entertainment’ and ‘catego-
ries_Desserts’ show positive contributions, indicating that these categories are asso-
ciated with higher ratings. It’s interesting to note that ‘categories_Doctors’ shows

1 3
H. Wojewoda, K. Kopczewska
a mix of positive and negative SHAP scores, suggesting that being in the medical
services category can have a variable impact on ratings, likely influenced by other
factors such as service quality and patient experience. Other categories such as ‘cate-
gories_Housing’ and ‘categories_Convenience Stores’ show negative SHAP values,
indicating that these types of businesses are associated with lower ratings.
Categories such as fast food, desserts and arts and entertainment often involve
frequent, casual interactions with customers where the quality of the experience is
immediately apparent and can lead to very positive or negative emotions. On the
other hand, categories such as medical services and convenience stores can be more
variable and negative for a number of reasons. Medical services often involve high
stakes and deeply personal experiences, where negative outcomes or perceived short-
comings can lead to harsh reviews. Convenience stores, while essential, may not
provide memorable experiences, generally leading to fewer reviews.
It was hypothesised that certain business categories are more sensitive to negative
reviews, which affects their overall ratings differently. The SHAP plot supports this
hypothesis by highlighting that some categories consistently contribute to higher rat-
ings (e.g. Arts & Entertainment, Desserts), while others show more mixed or negative
contributions (e.g. Doctors, Convenience Stores). The significant spread in SHAP
scores for some categories suggests that customer reviews have different impacts on
these categories, reflecting different sensitivities and robustness to negative feedback.
5.3 Spatial context of digital reputation
Spatial context constitutes an important dimension of the analysis because place-
based service businesses operate within local commercial environments rather than
in isolation. We therefore examine whether businesses with higher and lower Busi -
Fig. 8 Shapley summary plot after adding categories

1 3
Measuring digital reputation: a Business Reputation Score (BRS) and its…
ness Reputation Scores display visible spatial clustering and whether neighbourhood
characteristics contribute to the predictive explanation of the BRS.
Figure 9 presents the spatial distribution of businesses in Philadelphia, with
colours representing their BRS values. The map indicates that businesses with rela -
tively high BRS values are concentrated particularly in central and commercially
dense parts of the city. Lower-scoring businesses also display spatial concentration,
although they appear more frequently in peripheral and less densely developed loca-
tions. This pattern is consistent with the argument that businesses operating in similar
local environments may be exposed to shared customer flows, competitive conditions
and neighbourhood-level service standards [ 18, 20]. However, the map should be
interpreted as descriptive evidence of spatial patterning rather than as a formal test
of spatial spillovers.
A broadly similar spatial pattern is visible in New Orleans (Fig. 10). Businesses
with higher BRS values are concentrated in central areas, including downtown and
the French Quarter, which are characterised by substantial visitor activity and a dense
local service economy. Lower BRS values occur more frequently in peripheral areas,
although the spatial pattern is not uniform. These distributions suggest that digital
reputation may be associated with the characteristics of the surrounding commercial
environment. Businesses located in active and highly evaluated areas may benefit
from greater customer visibility, more intensive review activity and local competitive
benchmarking, while businesses in less active environments may accumulate reputa-
tion under different market conditions.
Because visual clustering alone does not establish the predictive relevance of spa-
tial context, we complement the maps with drop-out loss variable importance derived
from the XGBoost model (Fig. 11). Drop-out loss measures how much model per -
formance deteriorates when information from a particular variable is removed. It
Fig. 9 Map of Philadelphia with businesses coloured by BRS

1 3
H. Wojewoda, K. Kopczewska
therefore indicates the variable’s contribution to prediction, although it does not by
itself identify a causal effect or the direction of the underlying relationship.
The results show that both spatial variables are among the most relevant predictors
of the BRS. The variable average_score_proximity, representing the average rating of
surrounding businesses, ranks second in drop-out loss importance, with an increase
in model error of approximately 0.149 when excluded. This finding indicates that
information about the quality of neighbouring businesses contributes substantially to
the model’s ability to explain variation in digital reputation. It is consistent with the
possibility that businesses located near highly rated establishments share customer
environments, local expectations and reputational signals [17, 18].
The variable businesses_in_proximity, representing the local density of businesses,
also ranks among the leading predictors, with a drop-out loss of approximately 0.092.
Fig. 11 Drop-out loss variable importance

Fig. 10 Map of New Orleans with businesses coloured by BRS

1 3
Measuring digital reputation: a Business Reputation Score (BRS) and its…
Its importance suggests that the intensity of the surrounding commercial environ -
ment is relevant to digital reputation. Higher business density may reflect greater
customer traffic, stronger competition and more frequent opportunities for compari -
son and review activity [20]. At the same time, the variable importance measure does
not establish whether density increases or decreases the BRS in every context, as
the relationship may be non-linear and heterogeneous across locations and business
categories.
Taken together, the descriptive maps and the model-based importance measures
provide evidence consistent with H2. Businesses do not accumulate digital reputation
independently of their geographic context, and variables describing neighbourhood
quality and local business density materially improve the explanation of the BRS.
These findings support the interpretation of digital reputation as spatially embedded
and are consistent with the presence of neighbourhood-level reputational spillovers.
Nevertheless, the results should be understood as evidence of predictive association
rather than as a causal estimate of the effect of proximity.
6 Discussion
6.1 Theoretical implications
A central conceptual implication of this study is the distinction between digital repu-
tation as a latent construct and the reputation signals observable through a digital
platform. Digital reputation is a platform-mediated representation of customer expe-
riences: ratings and review volumes become visible only after platform-level aggre -
gation, filtering and presentation. The BRS therefore operationalises this observable
representation rather than the latent construct itself. This distinction clarifies both
the analytical value and the interpretive boundaries of platform-derived reputation
measures.
This study contributes to the growing literature on digital reputation by demon -
strating that reputation in platform economies is simultaneously multidimensional,
spatially embedded and algorithmically conditioned. The empirical findings are con-
sistent with the theoretical framework developed in this paper, which conceptualises
digital reputation as a higher-order construct comprising two complementary dimen-
sions: perceived quality and market recognition [27, 31].
The results confirm that business-specific characteristics - including operational
convenience features such as Wi-Fi availability, drive-through access and flexible
opening hours - are among the strongest predictors of digital reputation. This finding
aligns with the service-dominant logic perspective that value is co-created through
interactions between businesses and customers, and that operational attributes that
facilitate these interactions are fundamental determinants of customer experience [6,
14]. The prominence of category membership as a predictor further supports the view
that customer expectations, and therefore the standards against which businesses are
evaluated, vary substantially across service contexts [23, 24].
The spatial findings represent the most substantive theoretical contribution of the
study. The significance of average_score_proximity and businesses_in_proximity as

1 3
H. Wojewoda, K. Kopczewska
predictors of BRS provides empirical support for the argument that digital reputation
is spatially embedded. Businesses do not accumulate reputation independently of
their geographic context: proximity to high-quality businesses raises local standards,
increases customer flows and generates reputational spillovers that benefit neighbour-
ing establishments [17, 18, 20]. This finding extends existing online review research,
which has predominantly treated location as a control variable, by demonstrating
that spatial context constitutes a theoretically meaningful and empirically significant
determinant of digital reputation [8, 9].
The accelerated post-pandemic digitalisation of consumer behaviour has further
intensified these dynamics. Research documents a structural shift in reliance on
peer-generated ratings across service categories following COVID-19, as consumers
increasingly substituted in-person evaluation with platform-mediated reputation sig-
nals [11, 49]. The BRS framework is particularly well-suited to capture this shift, as
it integrates both the qualitative signal of ratings and the social validation embedded
in review volume - the two dimensions most sensitive to changes in digital consumer
engagement.
Finally, the application of XGBoost combined with SHAP values demonstrates
the value of explainable machine learning as an analytical framework for theory
development, not merely prediction. Recent work in hospitality and retail analyt -
ics confirms that gradient-boosted models, when paired with post-hoc explanation
methods, can reveal non-linear driver structures that conventional regression models
obscure [24, 50]. The present study extends this approach by grounding the analyti -
cal framework in a theoretically motivated composite measure rather than individual
performance proxies.
6.2 Platform governance, review manipulation and observed reputation
A central implication of using platform data is that researchers do not observe cus -
tomer experiences or even all submitted evaluations directly. They observe customer-
generated signals after these have been aggregated, filtered, ranked and displayed
through the platform’s information architecture. The BRS should therefore be inter -
preted as a measure of the observable, platform-mediated representation of digital
reputation rather than as a direct measure of the underlying latent construct.
This distinction is particularly important because digital review ecosystems are
exposed to multiple forms of information manipulation. These include incentivised
reviews, coordinated reviewing activity, strategically positive or negative evalu -
ations and, increasingly, AI-generated content [ 39, 41]. Such practices can distort
both components of the BRS. Manipulated evaluations may alter average ratings,
while coordinated or artificial review activity may inflate review volume and create
an exaggerated impression of market recognition. Research also indicates that inau -
thentic reviews can affect perceived credibility and influence purchasing decisions,
making review integrity important not only methodologically but also economically
[43, 44].
Digital platforms respond to these risks through credibility assessment, automated
detection, moderation and review-filtering mechanisms [40, 42]. These interventions
are necessary to maintain trust in online evaluation systems, but they also mean that

1 3
Measuring digital reputation: a Business Reputation Score (BRS) and its…
the data visible to users and researchers are partly the outcome of platform gover -
nance. Platforms determine which evaluations remain visible, which are deprioritised
and which are removed or classified as unreliable. Recent research shows that gover-
nance policies may also influence firms’ incentives to engage in review manipulation,
reinforcing the active role of platforms in shaping observed reputation [38].
For the present study, this has an important interpretive consequence. The Yelp
ratings and review counts used to calculate the BRS represent platform-curated
information rather than an unprocessed record of all customer evaluations. The BRS
therefore captures the reputational signal available within the Yelp ecosystem after
platform-level information processing has taken place. This does not invalidate the
measure, because consumers themselves make decisions on the basis of the same
visible information environment. It does, however, define the boundaries of the con-
struct being measured.
The results should consequently be interpreted as explaining variation in observed
digital reputation within a specific platform architecture. They do not distinguish
between genuine differences in customer experiences and differences arising from
platform moderation, review selection or manipulation intensity. This limitation may
also affect spatial interpretation. For example, highly competitive central districts
may experience greater incentives for strategic reviewing and potentially more inten-
sive filtering, while review manipulation may differ across business categories. If
such mechanisms vary systematically over space, part of the observed neighbour -
hood pattern could reflect differences in platform-mediated information processing
rather than customer experience alone.
Future research could address this issue by comparing BRS values across plat -
forms, incorporating indicators of filtered or non-recommended reviews where
available, and examining whether moderation intensity varies by business category,
location or competitive environment. Cross-platform analysis would be particularly
valuable because it could help separate the underlying reputational characteristics
of businesses from the effects of platform-specific governance and information pre -
sentation. In this sense, platform governance is not merely a technical limitation of
online review data but an integral part of how digital reputation becomes observable.
6.3 Managerial implications
The BRS framework offers several actionable insights for business managers operat-
ing in platform-mediated markets. First, the prominence of operational convenience
attributes - Wi-Fi, drive-through access, parking, extended opening hours - among
the top BRS predictors suggests that investments in service accessibility translate
directly into reputational returns. These attributes shape not only customer satisfac -
tion but also the likelihood that customers will engage in review activity, thereby con-
tributing to both dimensions of digital reputation simultaneously [5, 14]. Second, the
spatial findings imply that location strategy has reputational consequences beyond
foot traffic and visibility. Businesses entering high-quality commercial clusters ben -
efit from positive spillovers, as elevated neighbourhood standards raise consumer
expectations and encourage review activity across the cluster. Conversely, businesses
operating in peripheral or low-quality neighbourhoods may face a structural dis -

1 3
H. Wojewoda, K. Kopczewska
advantage in digital reputation that is difficult to overcome through service quality
improvements alone [ 17, 18]. Managers should therefore consider in their spatial
CRM (Customer Relationship Management) the reputational profile of prospective
locations - not only their demographic or commercial characteristics - when making
location decisions [ 51]. Third, the SHAP-based analysis provides category-specific
insights that aggregate models cannot deliver. The differential sensitivity of business
categories to negative reviews - with experiential categories such as Arts & Entertain-
ment showing greater upside and transactional categories such as convenience stores
showing more limited reputational range - suggests that reputation management strat-
egies should be tailored to category context [24, 30].
6.4 Limitations and future research
This study has several limitations that point to productive directions for future
research. First, the empirical analysis relies on Yelp data from two US cities - Phil -
adelphia and New Orleans - which limits the generalisability of findings to other
geographic and cultural contexts. Platform review behaviour, spatial market struc -
tures and the relative importance of operational attributes may differ substantially
across cities, countries and cultural settings. Replication using data from European
or Asian platforms, where review cultures and competitive dynamics differ, would
strengthen the external validity of the BRS framework [8, 52]. Second, the cross-sec-
tional nature of the dataset precludes causal inference. The BRS captures a snapshot
of digital reputation at a point in time, but the dynamics through which reputation
accumulates, deteriorates and responds to operational changes remain unexplored.
Longitudinal panel data would allow researchers to examine how BRS evolves in
response to changes in business characteristics, neighbourhood composition and
platform filtering policies [ 7, 11]. Third, the BRS operationalises digital reputation
through two dimensions - ratings and review volume - that are directly observable
on the platform. Future work could explore whether incorporating additional sig -
nals, such as sentiment scores derived from review text, response rates or reviewer
credibility indicators, further improves the construct validity of the measure [15, 16,
34]. Finally, the present study focuses on Yelp as a single platform. Platform-specific
features - ranking algorithms, review filtering policies, display formats - influence the
reputation signals that businesses accumulate and that consumers observe. Compara-
tive research across multiple platforms would allow researchers to disentangle the
effects of platform architecture from the underlying reputational dynamics that the
BRS seeks to capture [9, 30].
7 Summary
The first contribution of this study is conceptual. Previous research has frequently
operationalised digital reputation using individual indicators such as average rat -
ings, review volume or textual sentiment. While these measures capture important
aspects of customer-generated information, they represent only partial manifestations
of a broader phenomenon. Building on insights from electronic commerce, online

1 3
Measuring digital reputation: a Business Reputation Score (BRS) and its…
review research and platform studies, this paper conceptualises digital reputation as
a multidimensional construct comprising two complementary dimensions: perceived
quality and market recognition. This conceptual distinction helps explain why busi -
nesses with similar customer ratings may differ substantially in their digital visibil -
ity and market position. Average ratings reflect how positively customers evaluate
a business, whereas review volume reflects the extent to which these evaluations
become socially recognised through cumulative customer participation. We intro -
duce the Business Reputation Score (BRS), an operational measure that integrates
both dimensions. Considering these dimensions jointly provides a richer understand-
ing of digital reputation than treating either indicator in isolation.
The second contribution concerns explanation of digital reputation. We propose
an integrated framework in which digital reputation is shaped by business and spa -
tial characteristics within a platform-mediated information environment. Business
characteristics influence customer experiences and therefore shape perceived qual -
ity. Platform mechanisms condition how customer evaluations are filtered, displayed
and observed, although these mechanisms are not modelled directly in the present
study. Finally, spatial context influences both customer experiences and the broader
commercial environments in which reputation develops. Rather than acting indepen-
dently, these domains reinforce one another. Digital reputation therefore emerges
from the interaction between organisational capabilities, digital platform ecosystems
and place-based market conditions. This integrated perspective extends previous
online review research by connecting literature from electronic commerce, platform
studies and economic geography within a common conceptual framework.
The third contribution is methodological. Most applications of machine learning
in electronic commerce focus primarily on predictive performance. In contrast, the
present study employs explainable machine learning to support theory development.
Combining XGBoost with SHAP enables nonlinear relationships to be identified
while preserving transparent interpretation of the relative contribution of different
determinants. Consequently, explainable machine learning functions not merely as a
predictive technique but as an analytical framework for examining complex theoreti-
cal constructs. This perspective may prove valuable for future research investigating
multidimensional phenomena that cannot be adequately explained using conven -
tional linear modelling approaches.
Empirical analysis using the Yelp dataset confirms all three research hypotheses,
with one partial qualification. H1 is supported: operational attributes - including
Wi-Fi availability, drive-through access and flexible opening hours - consistently
rank among the top BRS predictors in both gain-based and drop-out loss importance
plots, confirming that business characteristics shape digital reputation through their
effect on customer experience [ 6, 14]. H2 is supported: the spatial variable aver-
age_score_proximity ranks second in drop-out loss importance (ΔMAE = + 0.149),
confirming that proximity to high-quality businesses generates meaningful reputa -
tional spillovers [18, 20]. H3 is partially supported: SHAP analysis reveals category-
specific patterns consistent with the hypothesis - experiential categories (Arts &
Entertainment, Desserts) show positive contributions while transactional and high-
stakes categories (Fast Food, Convenience Stores, Doctors) show negative or mixed

1 3
H. Wojewoda, K. Kopczewska
contributions - though the causal mechanism underlying this moderation warrants
further investigation [23, 24].
The findings suggest that digital reputation should therefore not be viewed simply
as an aggregation of online ratings, but as a multidimensional and platform-mediated
representation of place-based customer experiences. This perspective extends exist -
ing research on online reviews by integrating insights from electronic commerce,
platform studies and spatial analysis within a coherent theoretical framework.
Appendix
Data preparation
After the explanatory variable is ready for analysis, it is possible to move on to work
on the other variables in the dataset. To start with, the attributes feature needs to be
changed from JSON format to columns in the dataset. This can be done using several
functions extracting the necessary data and then assigning the values to the appropri-
ate columns accordingly. The same will also be carried out on categories, except that
it was found that there were a lot of different categories (over 2,000), so this part of
the analysis will be carried out separately.
From the other columns in the data, insights can be extracted by changing their
form into a more manageable one for analysis. The hours column, for example, will
be changed to hours_open, which will indicate how many hours a week a particular
business is open. Similarly, the latitude and longitude variables will be replaced by
two spatial variables that are better suited to the needs of this work. The first is busi-
nesses_in_proximity, which represents the number of businesses within a kilometer
radius of a given business. The second is average_score_proximity, which denotes
the average number of stars among businesses within a kilometre radius. These col -
umns will help answer one of the key hypotheses posed in this thesis, that spatial
variables have a significant impact on how a business is perceived in online reviews.
Following these changes, all spatial variables such as address, city and state were
excluded from the dataset. Similarly, business_id and variables used to derive new
features have been removed. Most importantly, both review_count and stars have
been omitted, as they directly measure business performance and could affect the
predictive model if included.
The refined dataset now consists of 111 explanatory variables, adjusted to include
the capture of a wide range of business attributes, such as BusinessAcceptsCredit-
Cards, RestaurantsDelivery and BikeParking. These attributes are crucial as they
have the potential to influence customer decisions and therefore business success.
With almost 120,000 observations, the dataset is robust enough to support extensive
statistical analysis. Such a large amount of data increases the reliability of the predic-
tive models and ensures that the conclusions drawn are statistically valid and reflect
the dynamics of the real world. The results of this analysis are expected to provide
valuable insights into the factors that drive business success.

1 3
Measuring digital reputation: a Business Reputation Score (BRS) and its…
Values of BRS
In order to better understand and check whether the chosen equation and weights
work in the desired way, it is possible to check the top, best and worst companies
according to this indicator and assess whether their positioning is appropriate. As can
be seen in Tables 3 and 4, the results are reasonable. The highest level of the indica-
tor is reached by companies with an almost perfect rating and a very high number
of reviews, and the lowest level is reached by companies with the worst rating and
a low number of reviews. This confirms that the Eq. (2) developed and the weights
chosen are a good reflection of whether a company has been successful online, i.e.
whether it has a high level of positive community engagement. With the confidence
that the explanatory variable is meaningful, one can move on to the next stages of
the analysis.
Modelling
At the beginning of the analysis, using previously prepared data, a default model was
trained to pre-test the results for later comparison. The mean, cross-validated results
are as follows:
 MAE: 1.463 R2: 0.363 MAPE: 16 , 7%
This, then, is the baseline, and any subsequent change or improvement to the
model will be compared to these levels. One can see that for a model without any
optimizations, it still performs quite well for a rather complex problem like predict -
ing the success of a business on the Internet.
The initial step in improving the model should be feature selection, for the cur -
rent dataset has as many as 111 columns, which increases training time and makes it
much more difficult to interpret its performance. Recursive feature elimination with
cross-validation (RFECV from sklearn package) will be used to reduce the number of
variables at the initial stage (Figure 12). With this method, it is possible to determine
Table 3 Top three businesses with the highest Business Reputation Score (BRS)
Name City Review count Stars Business success score (BRS)
Hattie B’s hot chicken - Nashville Nashville 6093 4.5 17.71
Reading terminal market Philadelphia 5721 4.5 17.65
Ruby slipper - New Orleans New Orleans 5193 4.5 17.55
Table 4 Last three businesses with the lowest Business Reputation Score (BRS)
Name City Review count Stars Business success score (BRS)
Absolute luxury Tampa Bay 5 1.0 3.79
Tuchman cleaners Greenwood 5 1.0 3.79
Lincare Clearwater 5 1.0 3.79

1 3
H. Wojewoda, K. Kopczewska
which columns and the number of columns to maximize the model result. It works
by iteratively building models and removing the least important features to find the
optimal number of features that yield the best model performance. Starting with all
available features, it fits a model and uses feature importance scores to eliminate the
least significant feature(s) at each iteration. This process is repeated until all features
have been evaluated
As can be seen in the graph above, the result reaches a maximum at around 50–60
variables and then stagnates. However, according to the algorithm, the most optimal
number would be 97 features. Upon further analysis, this is because the highest score
is, in fact, achieved with this number, but it is only marginally better than the one
obtained with half of them. Therefore, in order to facilitate the interpretation of the
model and to make it more generic, a restriction to the 50 most important variables
according to the algorithm will be applied. For this, a twin algorithm will be used, the
RFE, which allows to select an exact number of explanatory variables.
Having successfully reduced the number of variables, the time has come to opti -
mize the parameters of the XGBoost algorithm so that it is exactly suited to the prob-
lem and dataset posed in this thesis. For this purpose, Random Search will be used.
Unlike grid search, which systematically tests all possible combinations of hyperpa-
rameters, random search selects random combinations from a specified distribution.
This approach is particularly useful when dealing with large hyperparameter spaces
or when some hyperparameters are more influential than others, as it can often find a
good enough solution with significantly fewer iterations.
After drawing 50 different sets of variables and checking the results for each using
cross-validation, the following values proved to be the best set of parameters:
Fig. 12 Test accuracy based on the number of features

1 3
Measuring digital reputation: a Business Reputation Score (BRS) and its…

′𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 ′ ∶ 0.7, ′𝑟𝑟𝑠𝑠𝑟𝑟_𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑙𝑙𝑠𝑠 ′ ∶ 0.1, ′𝑟𝑟𝑠𝑠𝑟𝑟_𝑠𝑠𝑠𝑠𝑠𝑠𝑎𝑠𝑠′ ∶ 0.5,
′𝑛𝑛_𝑠𝑠𝑠𝑠𝑒𝑒𝑒𝑒 𝑠𝑠𝑠𝑠𝑒𝑒𝑒𝑒𝑟𝑟𝑠𝑠 ′ ∶ 550, ′ min _𝑐𝑐𝑎𝑒𝑒𝑠𝑠𝑙𝑙 _𝑤𝑤𝑠𝑠𝑒𝑒𝑟𝑟𝑎𝑒𝑒 ′ ∶ 8, ′ max _𝑙𝑙𝑠𝑠𝑠𝑠𝑒𝑒𝑎 ′ ∶ 8,
′𝑠𝑠𝑠𝑠𝑠𝑠𝑟𝑟𝑛𝑛𝑒𝑒𝑛𝑛𝑟𝑟 _𝑟𝑟𝑠𝑠𝑒𝑒𝑠𝑠 ′ ∶ 0.058, ′𝑟𝑟𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 ′ ∶ 4, ′𝑐𝑐𝑒𝑒𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 _𝑠𝑠𝑏𝑏𝑒𝑒𝑟𝑟𝑠𝑠𝑠𝑠 ′ ∶ 0.5
Internal mechanisms of the model
To better understand how the model handles each variable and uses it for final pre -
diction and to address the famous “black-box” problem of algorithms as complex as
XGBoost – one can use ceteris paribus plots (Fig. 13), which show how a particular
variable influences the model without changing anything else. It is also possible to
take an example prediction process and see how exactly each feature contributed to
the final score. These plots can be seen below.
Ceteris Paribus plots (Figure 13) illustrate the impact of individual features on
business success while keeping other variables constant. The analysis reveals that
moderate operating hours initially boost success scores, but excessive hours reduce
them, likely due to operational inefficiencies. Proximity to other businesses shows
that a moderate competitive environment is beneficial, while high competition satu -
rates the market, decreasing success. The average score of nearby businesses posi -
tively correlates with a business’s success, highlighting the benefits of being in high-
quality neighbourhoods. In contrast, the restaurant price range does not significantly
impact the success score, suggesting that other factors, such as service quality and
ambiance, play a more crucial role in customer perception.
Fig. 13 Ceteris Paribus plots. Source: Own study

1 3
H. Wojewoda, K. Kopczewska
On the other hand, the breakdown plot (Figure 14) illustrates how various features
contribute to the predicted business success score in the model. Starting from an
intercept value of 10.266, the average score proximity negatively impacts the score
by 0.52, indicating the detrimental effect of being near low-rated businesses. Con -
versely, being open for 48 h increases the score by 0.363, highlighting the optimal
point of operational hours. Features like WiFi availability and the number of nearby
businesses have minor negative impacts, decreasing the score by 0.144 and 0.042,
respectively. Having a business that accepts credit cards contributes positively by
0.12, while the absence of features like a car or bike parking lot, and a non-casual set-
ting slightly detracts from the score. The cumulative effect of all other factors results
in a minor reduction of 0.423, leading to a final predicted success score of 9.297.
Discussion of data content
The study uses simple average ratings assessed businesses based solely on their aver-
age star rating. Potentially, it could go deeper into text modelling. While numeric
approach provides a quick snapshot of customer satisfaction, it did not take into
account the quality or sentiment of the reviews, potentially leading to biased insights.
More advanced techniques included sentiment analysis, which used natural lan -
guage processing (NLP) to analyse the tone and sentiment of customer reviews. This
approach provided deeper insights into customer opinions and feelings. By analysing
the language used in reviews, companies can gauge customer satisfaction and iden -
tify specific areas of concern or praise. However, sentiment analysis requires sophis-
ticated algorithms and significant computing resources. The Net Promoter Score
(NPS) is a widely used metric that measures customer loyalty and satisfaction by ask-
ing customers how likely they are to recommend the company to others. Responses
are categorised as promoters, passives and detractors, and the NPS is calculated by
subtracting the percentage of detractors from the percentage of promoters. This met-
ric is useful for understanding overall customer satisfaction and the likelihood of
word-of-mouth. Customer Satisfaction Score (CSAT) measures the percentage of
satisfied customers by asking them to rate their satisfaction with a product or service
Fig. 14 Break down plot for a random business. Source: Own study

1 3
Measuring digital reputation: a Business Reputation Score (BRS) and its…
on a scale (e.g. 1–5). The CSAT score is calculated by taking the percentage of cus -
tomers who rated their satisfaction as high (e.g. 4 or 5). It provides a direct measure
of customer satisfaction, but may not capture the full range of customer experiences.
Some also used social media platforms, which can be a rich source of customer feed-
back. Companies can use sentiment analysis tools to track and analyse positive and
negative comments, reactions and ratings on social media. This approach helps com-
panies understand public perception and identify trends in customer sentiment. The
problem with this approach is that not every customer is interested in, or even uses,
corporate social media in this way.
Funding This research received no external funding.
Data availability The data used in this study are publicly available through the Yelp Open Dataset.
Declarations
Competing interests The authors declare that they have no known competing financial interests or per -
sonal relationships that could have appeared to influence the work reported in this paper.
Open Access   This article is licensed under a Creative Commons Attribution-NonCommercial-
NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution
and reproduction in any medium or format, as long as you give appropriate credit to the original author(s)
and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed
material. You do not have permission under this licence to share adapted material derived from this article
or parts of it. The images or other third party material in this article are included in the article’s Creative
Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in
the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or
exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view
a copy of this licence, visit http://creativecommons.org/licenses/by- nc - n d /4.0/.
References
1. Luca, M. (2016). Reviews, reputation, and revenue: The case of Yelp.com. Harvard business school
NOM unit working paper, 12–016.
2. Moreno, A., & Terwiesch, C. (2014). Doing business with strangers: Reputation in online service
marketplaces. Information Systems Research, 25(4), 865–886.
3. Anderson, M., & Magruder, J. (2012). Learning from the crowd: Regression discontinuity estimates
of the effects of an online review database. The Economic Journal, 122(563), 957–989.
4. Chevalier, J. A., & Mayzlin, D. (2006). The effect of word of mouth on sales: Online book reviews.
Journal of Marketing Research, 43(3), 345–354.
5. Hennig-Thurau, T., Gwinner, K. P., Walsh, G., & Gremler, D. D. (2004). Electronic word-of-mouth
via consumer-opinion platforms: What motivates consumers to articulate themselves on the internet?
Journal of interactive marketing, 18(1), 38–52.
6. Vargo, S. L., & Lusch, R. F. (2008). Service-dominant logic: Continuing the evolution. Journal of the
Academy of Marketing Science, 36, 1–10.
7. Dellarocas, C. (2003). The digitization of word of mouth: Promise and challenges of online feedback
mechanisms. Management Science, 49(10), 1407–1424.
8. Xiang, Z., Du, Q., Ma, Y ., & Fan, W. (2017). A comparative analysis of major online review plat -
forms: Implications for social media analytics in hospitality and tourism. Tourism management, 58,
51–65.

1 3
H. Wojewoda, K. Kopczewska
9. Martinez, L. F. (2025). Navigating the landscape of e-commerce: Thematic clusters, intellectual
turning points, and burst patterns in online reputation management. Electronic Commerce Research,
25(1), 1–38.
10. Marra, A., & D’Isidoro, A. (2025). Combining geographical and semantic proximity to measure
spillovers. The case of Sweden. Spatial Economic Analysis.  h t t    p  s :  /  / d  o i . o  r g  / 1  0 . 1 0 8 0 / 1 7 4 2 1 7 7 2 . 2 0 2 5 .
2 5 8 6 5 5 0
11. Pocchiari, M., Proserpio, D., & Dover, Y . (2025). Online reviews: A literature review and roadmap
for future research. International Journal of Research in Marketing, 42(2), 275–297.
12. Al-Natour, S., & Turetken, O. (2020). A comparative assessment of sentiment analysis and star rat -
ings for consumer reviews. International Journal of Information Management, 54, Article 102132.
13. Karasenko, A., & Baier, D. (2025). Beyond sentiment analysis of online customer reviews: An
approach to automated measurement of technology acceptance from online customer reviews. Jour-
nal of Business Economics, 95(7), 917–955.
14. Filieri, R., McLeay, F., Tsui, B., & Lin, Z. (2018). Consumer perceptions of information helpfulness
and determinants of purchase intention in online consumer reviews of services. Information & man-
agement, 55(8), 956–970.
15. Hong, H., Xu, D., Wang, G. A., & Fan, W. (2017). Understanding the determinants of online review
helpfulness: A meta-analytic investigation. Decision Support Systems, 102, 1–11.
16. Thomas, M. J., Wirtz, B. W., & Weyerer, J. C. (2019). Determinants of online review credibility and
its impact on consumers’ purchase intention. Journal of Electronic Commerce Research, 20(1), 1–20.
17. Matti, J. (2020). Reaching for the stars: Spatial competition and consumer reviews. Atlantic Eco-
nomic Journal, 48(3), 339–353.
18. Glaeser, E. L. (2011). Triumph of the City: How Our Greatest Invention Makes Us Richer, Smarter,
Greener, Healthier, and Happier. Penguin Press.
19. Macdonald, J. L., Dolega, L., & Singleton, A. (2022). An open source delineation and hierarchical
classification of UK retail agglomerations. Scientific Data, 9(1), 541.
20. Rosenthal, S. S., & Strange, W. C. (2004). Evidence on the nature and sources of agglomeration
economies. In J. V . Henderson & J.-F. Thisse (Eds.), Handbook of Regional and Urban Economics
(V ol. V ol. 4, pp. 2119–2171). Elsevier.
21. Chen, T., & Guestrin, C. (2016). XGBoost: A scalable tree boosting system. Proceedings of the 22nd
ACM SIGKDD international conference on knowledge discovery and data mining, 785–794.
22. Lundberg, S. M., & Lee, S. I. (2017). A unified approach to interpreting model predictions. Advances
in Neural Information Processing Systems, 30, 4765–4774.
23. Phillips, P., Zigan, K., Silva, M. M. S., & Schegg, R. (2015). The interactive effects of online reviews
on the determinants of Swiss hotel performance: A neural network analysis. Tourism Management,
50, 130–141.
24. Zhao, Y ., Xu, X., & Wang, M. (2019). Predicting overall customer satisfaction: Big data evidence
from hotel online textual reviews. International Journal of Hospitality Management, 76, 111–121.
25. Ribeiro, M. T., Singh, S., & Guestrin, C. (2016). Why should I trust you? Explaining the predictions
of any classifier. Proceedings of the 22nd ACM SIGKDD international conference on knowledge
discovery and data mining, 1135–1144.
26. De Maeyer, P. (2012). Impact of online consumer reviews on sales and price strategies: A review and
directions for future research. Journal of Product & Brand Management, 21(2), 132–139.
27. Connelly, B. L., Certo, S. T., Ireland, R. D., & Reutzel, C. R. (2011). Signaling theory: A review and
assessment. Journal of Management, 37(1), 39–67.
28. Spence, M. (1973). Job market signaling. The Quarterly Journal of Economics, 87(3), 355–374.
29. Luca, M., & Zervas, G. (2016). Fake it till you make it: Reputation, competition, and Yelp review
fraud. Management Science, 62(12), 3412–3427.
30. Yang, M., Zheng, Z. (E.), & Mookerjee, V . (2021). The race for online reputation: Implications for
platforms, firms, and consumers. Information Systems Research, 32(4), 1262–1280.
31. OECD, European Union/EC-JRC. (2008). Handbook on constructing composite indicators: Method-
ology and user guide. OECD Publishing.
32. Ye, Q., Law, R., & Gu, B. (2009). The impact of online user reviews on hotel room sales. Interna-
tional Journal of Hospitality Management, 28(1), 180–182.
33. Guo, Y ., Barnes, S. J., & Jia, Q. (2017). Mining meaning from online ratings and reviews: Tourist
satisfaction analysis using latent dirichlet allocation. Tourism Management, 59, 467–483.
34. Pang, B., & Lee, L. (2008). Opinion mining and sentiment analysis. Foundations and Trends® in
Information Retrieval, 2(1–2), 1–135.

1 3
Measuring digital reputation: a Business Reputation Score (BRS) and its…
35. Srinivasan, S. S., Anderson, R., & Ponnavolu, K. (2002). Customer loyalty in e-commerce: An explo-
ration of its antecedents and consequences. Journal of Retailing, 78(1), 41–50.
36. Mayzlin, D., Dover, Y ., & Chevalier, J. A. (2014). Promotional reviews: An empirical investigation
of online review manipulation. American Economic Review, 104(8), 2421–2455.
37. Liang, T. P., Li, X., Yang, C. T., & Wang, M. (2015). What in consumer reviews affects the sales of
mobile apps: A multifacet sentiment analysis approach. International Journal of Electronic Com -
merce, 20(2), 236–260.
38. Zhang, W., Zhang, X., Wang, Q., Li, J., & Ma, Z. (2025). Stop it or not? Effect of platform’s gover-
nance on firms’ online review manipulation. Information & Management, 62(7), Article 104200.
39. Xu, Y ., & Xu, X. (2023). Rating deviation and manipulated reviews on the Internet—A multi-method
study. Information & Management, 60(6), Article 103829.
40. Gu, X., Cao, J., & Fang, Y . (2026). Review manipulation and filtering on digital platforms. Informa-
tion Systems Research, 37(2), 927–947.
41. Chernyaeva, O., Lee, O. K. D., & Hong, T. (2025). From fake to AI-generated: Leveraging informa-
tion manipulation theory and explainable AI for robust detection of manipulated reviews. Decision
Support Systems. https://doi.org/10.1016/j.dss.2025.114522
42. Pan, Y ., & Xu, L. (2024). Detecting fake online reviews: An unsupervised detection method with a
novel performance evaluation. International Journal of Electronic Commerce, 28(1), 84–107.
43. Pooja, K., & Upadhyaya, P. (2024). What makes an online review credible? A systematic review of
the literature and future research directions. Management Review Quarterly, 74(2), 627–659.
44. Kumar, R., Mukherjee, S., & Rana, N. P. (2024). Exploring latent characteristics of fake reviews
and their intermediary role in persuading buying decisions. Information Systems Frontiers , 26(3),
1091–1108.
45. Marshall, A. (1920). Principles of economics: An introductory volume (8th ed.). Macmillan.
46. Pacicco, F., Serati, M., & Venegoni, A. (2025). Shaping the local business structure: Drivers of firm
location at the municipal level. Spatial Economic Analysis, 20(3), 484–513.
47. Kopczewska, K. (2022). Spatial machine learning: New opportunities for regional science. The
Annals of Regional Science, 68(3), 713–755.
48. Hu, N., Liu, L., & Zhang, J. J. (2008). Do online reviews affect product sales? The role of reviewer
characteristics and temporal effects. Information Technology and management, 9(3), 201–214.
49. Pantano, E., Pizzi, G., Scarpi, D., & Dennis, C. (2020). Competing during a pandemic? Retailers’ ups
and downs during the COVID-19 outbreak. Journal of Business Research, 116, 209–213.
50. Abdullah, S., Van Cauwenberge, P., Vander Bauwhede, H., & O’Connor, P. (2024). Review ratings,
sentiment in review comments, and restaurant profitability: Firm-level evidence. Cornell Hospitality
Quarterly, 65(3), 378–392.
51. Kostecka, Z., & Kopczewska, K. (2023). Spatial CRM and location strategy: E-commerce solutions
in the furniture industry. Case of IKEA pick-up points in Poland. Electronic Commerce Research and
Applications, 62, Article 101308.
52. Gretzel, U., & Yoo, K. H. (2008). Use and impact of online travel reviews. Information and com -
munication technologies in tourism 2008 (pp. 35–46). Springer.
Publisher’s Note Springer Nature remains neutral with regard to jurisdictional claims in published maps
and institutional affiliations.
Authors and Affiliations
Hubert Wojewoda1 · Katarzyna Kopczewska1
 Katarzyna Kopczewska
kkopczewska@wne.uw.edu.pl
Hubert Wojewoda
hubertwojewoda@wp.pl
1 Faculty of Economic Sciences, University of Warsaw, Warsaw, Poland
