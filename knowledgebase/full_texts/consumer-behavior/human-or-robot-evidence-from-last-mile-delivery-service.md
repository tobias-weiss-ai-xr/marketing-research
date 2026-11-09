---
title: Human or Robot? Evidence from Last-Mile Delivery Service
url: https://arxiv.org/abs/2509.11562
category: consumer-behavior
subcategory: empirical
date: 2025-09
venue: ''
authors:
- Baorui Li
- Xincheng Ma
- Brian Rongqing Han
- Daizhong Tang
- Lei Fu
source: arxiv
pdf_url: https://arxiv.org/pdf/2509.11562
pages: 36
chars: 58809
fetched_at: '2026-11-08T13:06:57+00:00'
kb_version: 1
---

# Human or Robot? Evidence from Last-Mile Delivery Service

Human or Robot? Evidence from Last-Mile Delivery
Service
Baorui Li1, Xincheng Ma 2, Brian Rongqing Han 3, Daizhong
Tang4, and Lei Fu 5
1The University of Texas at Dallas
2Hong Kong University of Science and Technology
3University of Illinois Urbana-Champaign
4Tongji University
5Alibaba Group Inc.
1
arXiv:2509.11562v1  [econ.GN]  15 Sep 2025

Abstract
As platforms increasingly deploy robots alongside human labor in last-mile logis-
tics, little is known about how contextual features like product attributes, environmen-
tal conditions, and psychological mechanisms shape consumer preference in real-world
settings. To address this gap, this paper conducts an empirical study on consumer
choice between human versus robot service, analyzing 241,517 package-level choices
from Alibaba’s last-mile delivery stations. We identify how product privacy sensitivity,
product value, and environmental complexity affect consumer preference. Our find-
ings reveal that consumers are significantly more likely to choose robot delivery for
privacy-sensitive packages (11.49%) and high-value products (0.97% per 1% increase
in value), but prefer human couriers under adverse weather conditions (1.63%). These
patterns are robust to alternative specifications and controls. These results also under-
score that delivery choices are shaped not only by functional considerations but also
by psychological concerns, highlighting the need for context-aware service design that
aligns strategies with consumer perceptions.
Keywords: last-mile delivery; human-robot service; consumer preference
2

1 Introduction
The rapid advancement of artificial intelligence and automation technologies has led to in-
creasing integration of service robots into traditional offline service environments. Zhou et
al. (2023) reports that autonomous delivery, automated and intelligent assistants are rapidly
entering industries such as retail, logistics and food service, signaling a new era in which hu-
man and robot services coexist. This shift raises a critical yet underexplored question: how
do consumers choose between human and robot services? Understanding not only what con-
sumers choose, but also why is essential for firms seeking to optimize service design, resource
allocation, and consumer experience in such hybrid human-robot systems. However, the
psychological drivers behind consumer preferences and their behavioral consequences have
received limited systematic investigation in both academic research and industry practice.
Prior research has primarily examined human-robot interaction in task execution, focus-
ing on the roles of experts, workers, or consumers in conjunction with AI systems (Fügener et
al., 2021; Lu&Zhang, 2024; Wangetal., 2023; Zhangetal., 2025)aswellashumanresponses
to AI-powered robots relative to traditional human or rule-based service providers (Bai et al.,
2022; Cui et al., 2022; Luo et al., 2019; Xu et al., 2024). However, little is known about
how consumers actively choose between human and robot services in real-world contexts,
and what contextual or psychological factors shape these choices. This gap is particularly
salient in complex offline environments where AI-enabled robots are increasingly deployed,
yet empirical research remains limited (Jeon et al., 2022; Wang et al., 2024).
Our study addresses this gap by analyzing real-world consumer choices in the context of
Alibaba’s last-mile logistics network, Cainiao Station. Leveraging a large-scale proprietary
dataset comprising 241,517 package-level records in Cainiao campus stations at 32 univer-
sities across China, we examine how key contextual features – product privacy sensitivity,
product value and environmental complexity – systematically influence consumer choices.
Building on prior theoretical research, we propose that different contextual factors acti-
vate distinct psychological mechanisms that shape consumer decision-making. Specifically,
3

product privacy sensitivity triggers heightened privacy concerns, leading consumers to prefer
less socially intrusive options such as robots (Awad & Krishnan, 2006; Smith et al., 1996). In
contrast, high-value products can trigger different consumer concerns: some may emphasize
the risk of service failure and prefer human couriers for their discretion and adaptability
(Bauer, 1960; Featherman & Pavlou, 2003; Ma et al., 2025), while others may prioritize
consistency and traceability, favoring robots in structured environments (Wirtz et al., 2018;
Yalcin et al., 2022; You & Robert Jr., 2024). Finally, environmental complexity, such as
bad weather, increases the perceived uncertainty, potentially enhancing reliance on human
service providers who are viewed as better able to exercise adaptive judgment (Mayer et al.,
1995; McKnight et al., 2002).
Based on our analysis of delivery choices, we empirically test our hypotheses and find
that user 1 choices systematically respond to contextual triggers. Privacy-sensitive products
increase the likelihood of robot delivery by 11.49% (p <0.001), consistent with the notion
that consumers seek to avoid social judgment by opting for less intrusive service. For high-
value items, a 1% increase in package value leads to a 0.97% increase in the likelihood of
choosing robot delivery (p <0.001), suggesting that robots are perceived as secure and
traceable in structured environments. In contrast, adverse weather conditions reduce the
likelihood of robot delivery by 1.63% (p <0.001), reflecting users’ greater trust in human
couriers when facing environmental uncertainty.
Furthermore, we identify the heterogeneity in consumer preferences driven by user char-
acteristics, specifically gender and prior usage experience. Female users are significantly
more likely to choose human delivery under adverse weather conditions, with the likelihood
of robot delivery decreasing by an additional 1.38% (p <0.001). By taking the interaction
between main factors, we find that bad weather conditions attenuate the positive effect of
privacy-sensitive packages on robot choice. The likelihood of choosing a robot in adverse
weather for these packages was 6.37%, a significant reduction from the baseline effect of
1The termsuserandconsumerare used interchangeably in this paper.
4

11.49%(p <0.05). Prior delivery experience also plays a pivotal role in shaping current
choices: selecting robot delivery in the previous orders increases the likelihood of repeating
that choice by 24.6% (p <0.001), while prior human delivery reduces it by 49.7% (p <0.001).
We also find evidence of cumulative habit formation: each additional prior robot delivery
increases the likelihood of choosing robot service by 0.07 – 0.19% (p <0.001), and 0.16 –
0.18% (p <0.001) for that of human service. The recalibration effect of cumulative experi-
ence is also uncovered by incorporating the interaction terms. These findings highlight the
dynamic and adaptive nature of consumer decision-making in hybrid human-robot service
systems.
Our study makes several contributions. First, to the best of our knowledge, it is the first
to systematically examine actual consumer choice between human and robot delivery service
in a real-world offline environment. By utilizing large-scale package-level data, we provide
empirical insights into consumer behavior in the emerging phase of human-robot service
coexistence. Second, we advance the theoretical understanding of robot service choice by
showing how contextual factors activate distinct psychological mechanisms, including privacy
concerns, perceived risk, and trust expectations. This framework enriches the literature on
human-robot interaction by identifying the conditions under which automation is preferred
or resisted. Finally, our findings offer actionable implications for platforms designing hybrid
human-robot service systems, emphasizing the need for context-sensitive resource allocation
and service channel management in the evolving landscape of automation.
The remainder of the paper is structured as follows. Section 2 reviews the related lit-
erature; Section 3 develops our main hypotheses; we introduce our empirical setting and
dataset in Section 4 and present the main result in Section 5; Section 6 and Section 7 show
our heterogeneous analysis and robustness checks respectively; finally, Section 8 concludes.
5

2 Literature Review
Our work intersects two main research streams: human-robot services interaction and last-
mile delivery.
2.1 Human-robot Services Interaction
Prior studies have examined both how robot augments the user’s work and how users respond
to AI-enabled robot services. The former highlights robot’s ability to support judgment
across domains such as clinical diagnosis (Yan & Xu, 2021), drug development (Lou & Wu,
2021), financial forecasting (Fu et al., 2021; Lu & Zhang, 2024), and consumer co-creation
(Zhang et al., 2025).
The latter stream of interest focuses on how users evaluate and interact with robots,
emphasizing concerns around trust (Dietvorst et al., 2015; Xu et al., 2024), privacy (Goldfarb
& Tucker, 2011; Holthöwer & Van Doorn, 2023), cost (Castelo et al., 2023) and empathy
(Yalcin et al., 2022). For example, Dietvorst et al. (2015) and You and Robert Jr. (2024)
address that trust-in-robots determines user acceptance of robot service directly. Yalcin
et al. (2022) finds that consumers perceive robot to be less empathetic than human ones
in emotionally charged scenarios. This agrees with the complementary finding of Mende
et al. (2019) that consumers are more willing to be served by humans when consuming
"healthy product" like healthy food due to the experience of high-level social belongingness.
However, the belief that "robots do not judge" becomes a positive driver for consumers to
conversely choose robot service from the perspective of privacy. Holthöwer and Van Doorn
(2023) identifies a key situation where consumers prefer service robots over humans if they
encounter an embarrassing service, showing that consumers feel less judged by a robot when,
for example, purchasing a sensitive product like sexual disease medicine.
Much of this literature has studied digital or simulated chatbots, recommender systems,
or automated work assignment tools, where users passively receive outputs (Cui et al., 2022;
6

Luo et al., 2019; Ma et al., 2025). Relatively little is known about how users make active
choices between robot and human service options. Ma et al. (2025) is closely aligned with
our research focus, showing that customers in luxury service settings have a lower preference
for service robots compared to mainstream settings. This "robot disadvantage" is driven by
the customer’s desire to feel superior to the service provider, a feeling that human interaction
can satisfy but robot interaction cannot. Many of these studies use surveys to understand
consumer psychological processes, but have investigated consumer choice in real-choice set-
tings less. We contribute to this gap by analyzing delivery decisions in a physical hybrid
human-robot service system, where both robot and human services are available.
2.2 Last-mile Delivery
This study also connects to the literature on last-mile delivery contextually by offering em-
pirical insight into how consumers choose between robot and human delivery. Existing work
has primarily focused on optimizing delivery network design and efficiency (Carlsson et al.,
2023; Fatehi & Wagner, 2022; Liu et al., 2021) as well as cost (Qi et al., 2018; Raghavan &
Zhang, 2024).
Empirical studies have highlighted the value of operational innovations such as pickup
stations and human couriers (Amorim et al., 2024; Han, Sun, et al., 2024; Lim et al., 2023;
Lu et al., 2023). For instance, Lu et al. (2023) investigates the value of human delivery in
the last-mile delivery context, indicating that last-mile delivery significantly increases sales
and customer spending on online retail platform. More recent research has begun to examine
robot delivery in field settings. Han, Li, et al. (2024) shows that the introduction of robot
delivery increases order volume relative to self-pickup and may generate greater value than
human couriers. These studies quantify the aggregate benefits of automation but do not
examine consumer-side decisions when both delivery services are simultaneously available.
Table 1 displays how we differentiate our work from prior literature. Using user choice
data, we study the decision-making setting directly. Our analysis links contextual drivers
7

to delivery selections, extending the last-mile literature to account for user agency in hybrid
human-robot service environments. In doing so, we complement existing supply-side and
design-focused work with a demand-side perspective on the adoption and comparative appeal
of robot delivery.
Table 1: Positioning of the current study in last-mile delivery literature
Comparison
(rowvs.col) Self-pickup Human Delivery Robot Delivery
Self-pickup
(intro. of last-mile sta.)
Value of last-mile station
(Han, Sun, et al., 2024) — —
Human Delivery Impact of to-door delivery (Lu et al., 2023) — —
Robot Delivery Effect of robotic delivery (Wu et al., 2023) The current study —
3 Hypothesis Development
The increasing integration of service robots into traditional offline environments raises impor-
tant questions about how consumers make service type choices in human-robot coexistence
settings. Based on prior research in service marketing and technology adoption, we pro-
pose that consumer choice between human and robot services is systematically influenced
by contextual factors that activate different psychological mechanisms. Among these fac-
tors, especially we propose thatproduct privacy sensitivity,product value, andenvironmental
complexityact as key contextual triggers that respectively heighten privacy concerns, risk
perceptions, and trust expectations. These psychological processes, in turn, shape consumer
preferences between human and robot.
3.1 Product Privacy Sensitivity
Privacy concerns are key drivers of consumer behavior in technology-mediated services, es-
pecially when sensitive products are involved (Awad & Krishnan, 2006; Smith et al., 1996).
In last-mile delivery, items like intimate apparel or personal care products may evoke anxiety
8

due to anticipated embarrassment (Argo et al., 2005). Robot service providers offer a dis-
tinct advantage in such contexts: unlike human servers, robots are perceived as lacking social
judgment capabilities and emotional evaluation, thereby serving as "safe" recipients of sensi-
tive information (Mende et al., 2019; Wirtz et al., 2018) and reducing embarrassment when
acquiring sensitive products (Holthöwer & Van Doorn, 2023; Pitardi et al., 2022). This per-
ception reduces the psychological discomfort associated with privacy-sensitive transactions
and may make consumers more willing to opt for robot service.
H1:For privacy-sensitive products, consumers are more likely to choose robot service
over human service.
3.2 Product Value
Consumer’s delivery preferences for high-value products can be influenced by distinct the-
oretical mechanisms. According to classic theories of perceived risk, greater product value
heightens the perceived consequences of service failure, thereby increasing the demand for
human judgment, discretion, and accountability (Bauer, 1960; Featherman & Pavlou, 2003).
From this perspective, human couriers may be viewed as better equipped to handle valu-
able items, particularly in the face of unexpected challenges. Prior studies also find a robot
disadvantage such that consumers see human staff as key to the prestige of luxury, so robot
preference is lower in luxury contexts (Ma et al., 2025). Based on this reasoning, we propose
the following hypothesis:
H2a:For high-value products, consumers are more likely to choose human service over
robot service.
Alternatively, research on service automation suggests that, in highly structured and
monitored environments such as campus logistics systems, robots may be perceived as more
consistent, traceable, and less prone to error. Once trust in an automated system is estab-
lished, it can be preferred for important, high-stakes tasks (You & Robert Jr., 2024). These
attributes can enhance user’s sense of control and security, especially when the stakes are
9

high (Wirtz et al., 2018; Yalcin et al., 2022). This leads to an alternative hypothesis:
H2b:For high-value products, consumers are more likely to choose robot service over
human service.
3.3 Environmental Complexity
Achieving a high level of autonomy requires adaptation to unpredictable and changing envi-
ronments, supporting the rationale that humans are currently more capable in such scenarios
(Beer et al., 2014). In stable settings, consumers may prefer robots for their efficiency and
consistency. However, as unpredictability rises – such as during extreme weather – trust
expectations increase, humans are often viewed as more capable of exercising judgment, em-
pathy, and flexibility (Wirtz et al., 2018), prompting a shift in preference toward human
service providers.
H3:In complex service environments like extreme weather conditions, consumers are
more likely to choose human service over robot service.
In summary, we propose a framework wherein product privacy sensitivity, product value,
and environmental complexity activate distinct psychological processes that systematically
influence consumer preferences. Our empirical study in the last-mile delivery offers a unique
opportunity to test these hypotheses in a real-world human-robot coexistence environment.
4 Empirical Setting and Data
By the end of 2024, Alibaba’s logistics subsidiary, Cainiao Smart Logistics Network, had
deployed thousands of campus-based last-mile distribution facilities, "Cainiao Stations" (see
Appendix A Figure A1), with each university typically hosting one station to enable on-
site package collection. Many stations have incorporated last-mile delivery services via both
human couriers and robot vehicles (see Appendix A Figure A2), where users can choose
preferred delivery services by themselves.
10

Our research context focuses on 32 Cainiao campus stations across China. These are the
subset of campus stations that have included both delivery services during the year of 2024.
After the inbounding of the packages, users can order a specific delivery service through
which packages can be delivered from the station to a selected location. Figure 1 and Figure
2 display the timeline of delivery services and the process of placing order respectively.
Figure 1: Timeline of delivery service
Figure 2: Ordering process of delivery services
Figure 2 illustrates the ordering process for last-mile delivery on Cainiao’s mobile app,
where users choose between paid human and robot delivery options. After a package arrives
at the station, the user selects "Book a delivery", chooses a delivery type, picks a time
window, and confirms the order. This process gives users control over both delivery method
and timing, with price as a key consideration.
11

Wecollectpackage-leveldatafromthese32campusstationsbetweenJanuaryandNovem-
ber 2024. The dataset includes (i) delivery details (delivery type, fee, lead time), (ii) package
attributes (product name, price, inbound time), and (iii) user demographics (gender, birth-
place, device type), along with external variables such as weather, school level, and location.
Out of 7,453,438 total package records, 241,517 involved either robot or human delivery, with
the rest self-picked by users. Among delivered packages, 57% were handled by robots and
43% by human couriers, covering 61,630 unique users.
To test our hypotheses, we operationalize three key variables. First, sensitivity refers
specifically and narrowly to adult/sexual products and contraceptive supplies (e.g., sex toys,
condoms, and lingerie), where privacy concerns are most salient. Second, package value
capturesthelistedpriceofthegoods. Third, weusebadweatherasaproxyforenvironmental
complexity. Specifically, we define a weather condition as "bad" if it meets either of the
following criteria: (1) a temperature warning is issued by the administration (⩾37◦C or⩽
-6 ◦C), or (2) any form of precipitation occurs, including rain and snow.
5 Main Results
5.1 Station-level Evidence
We first construct a station-level panel to track the overall effect of sensitivity. We use the
following OLS model with two-way fixed effect to estimate the station-level effect:
type_ratio st =α+β 1 ·sensitive_ratio st +β 0 ·X st +StationF Es +M onthF Et +ε st (1)
wheretype_ratio st denotes the percentage of robot (human) delivery over total package
number of stationsin montht.X st are control variables.StationF Es andM onthF Et are
station fixed effect and time fixed effect respectively.
Table 2 presents the estimated result based on equation (1). The ratio of sensitive
12

Table 2: Station-level evidence: effect of sensitivity
(1)
ratio_robot
(2)
ratio_human
const 0.0106 (0.0077) 0.0104 (0.0063)
sensitive_ratio 1.1663** (0.5518) 0.3020 (0.4515)
lg(avg_package_value) 3.711e-06 (0.0012) 0.0010 (0.0010)
StationF EYes Yes
T imeF EYes Yes
R2 0.0299 0.0094
Observations 172 172
Note.**p <0.05, ***p <0.01. Standard errors are in parentheses.
packages has an significantly positive effect on the ratio robot delivery. When the ratio of
sensitive packages increases by 1%, number of packages delivered by robot vehicle will then
increase by 1.17%. The impact of package value does not show a significant effect on average
at the station level. Weather effect is absorbed by station and time fixed effects. However,
such significant effect is not observed in human delivery. To further investigate the impact
on user choice behavior, we conduct the package-level analysis in the following section.
5.2 Main Effects
To empirically test the three hypotheses outlined above, we estimate an OLS model us-
ing the full delivery dataset of 241,517 package-level observations. The dependent variable
delivery_typeis a binary indicator equal to 1 if the delivery was completed by a robot and 0
if completed by a human courier. In addition, we incorporate both user fixed effects and time
fixed effects to control for temporal variation in delivery conditions. Formally, our empirical
model specification is as follows:
13

delivery_type ijst =α+β 1 ·is_package_sensitive i +β 2 ·lg(package_value) i
+β3 ·is_bad_weather st +β 0 ·X ijst +T imeF Et +ε ijst (2)
wheredelivery_type ijst isthebinarychoiceofuserjforpackageiinstationsattimet, where
delivery_type ijst equals1forrobotdeliveryand0forhumandelivery.is_package_sensitive i
isalsoabinaryvariablesuchthat1forsensitivepackagesand0otherwise.lg(package_value) i
denotes the log of the value of packageithat userjpaid.is_bad_weather st is another bi-
nary variable that represents the weather of stationsis bad or not at timet.X ijst are
control variables consisting of three types of covariates: delivery information, user demo-
graphic and station-level variables. Following the setup in Amorim et al. (2024), we include
lead_time,lead_time_otheranddelivery_priceto control the delivery-related effective-
ness. To take into account demographic effect, gender (is_f emale), device model (is_ios),
delivery time sensitivity (is_time_sensitive), and place of birth (is_South) are included
as well. Additionally, the station-level characteristics are also considered by incorporating
school type (is_211, "211 universities", China’s equivalent of R1 universities in the US) and
school location (is_school_South).T imeF Et considers the time fixed effect.
Table 3 demonstrates our main result. Following the approach of Chen (2013), we first
estimate the main effects of interest. Column (1) shows direct estimation towards our hy-
potheses. Column (2) to (4) incorporate delivery covariates, demographic characteristics
and station-level characteristics respectively step-by-step. Column (4) presents our final
estimation.
We empirically test the three hypotheses proposed earlier. Consistent with H1, we find
that consumers are significantly more likely to choose robot delivery when the package is
privacy-sensitive. As shown in Table 3, the probability of selecting robot delivery increases
by 11.49% (p <0.001) for sensitive items. This sizable effect validates our proposition that
14

Table 3: Main effects on user-level choice of delivery
Dependent Variable:delivery_type
(1) (2) (3) (4)
const 0.5473*** (0.0034) 0.8596*** (0.0037) 0.8920*** (0.0039) 0.9069*** (0.0040)
is_package_sensitive 0.1392*** (0.0158) 0.1224*** (0.0146) 0.1095*** (0.0146) 0.1149*** (0.0143)
lg(package_value) 0.0059*** (0.0008) 0.0127*** (0.0007) 0.0135*** (0.0007) 0.0097*** (0.0007)
is_bad_weather -0.0135*** (0.0024) -0.0426*** (0.0022) -0.0398*** (0.0022) -0.0163*** (0.0022)
lead_time -0.0241*** (0.0002) -0.0239*** (0.0002) -0.0235*** (0.0002)
lead_time_other 0.0040*** (0.0002) 0.0040*** (0.0002) 0.0038*** (0.0002)
delivery_price -0.1628*** (0.0010) -0.1658*** (0.0010) -0.1489*** (0.0010)
is_f emale -0.0449*** (0.0020) -0.0590*** (0.0019)
is_ios 0.0064*** (0.0019) 0.0047** (0.0018)
is_time_sensitive 0.0040 (0.0025) 0.0020 (0.0024)
is_South -0.0306*** (0.0020) 0.0178*** (0.0021)
is_school_South -0.1140*** (0.0022)
is_211 0.2101*** (0.0026)
T imeF EYes Yes Yes Yes
R2 0.0007 0.1401 0.1435 0.1732
Observations 241,517 241,517 241,517 241,517
Note.*p <0.1, **p <0.05, ***p <0.01. Standard errors are in parentheses.
privacy concerns, particularly the desire to avoid social judgment, drive users toward a less
socially intrusive service type, making robot delivery the preferred option in such contexts.
Regarding H2, our results support the mechanism outlined in H2b. We find that a 1%
increase in package value is associated with a 0.97% increase in the likelihood of choosing
robot delivery (p <0.001). This effect suggests that, consumers view robots as sufficiently
reliable and secure to handle valuable goods, likely due to their perceived consistency and
traceability.
15

Finally, in support of H3, we find that bad weather conditions significantly increase the
preference for human delivery. Specifically, under conditions of extreme temperature or
precipitation, the probability of choosing robot delivery decreases by 1.63% (p <0.001),
implying a corresponding increase in preference for human couriers. This finding aligns with
our hypothesis that environmental complexity heightens trust expectations, prompting users
to rely on humans for their adaptive judgment and contextual flexibility.
Taken together, these empirical results directly address our central research question
regarding how consumers make service type choices in human-robot coexistence settings.
By demonstrating that delivery service choices are systematically influenced by contextual
triggers through psychologically grounded mechanisms, our findings validate the theoretical
framework developed earlier. This evidence highlights the nuanced and situational nature
of consumer decision-making in technology-mediated services. In doing so, we contribute
to a deeper understanding of the transitional phase of human-robot service coexistence and
provide a behavioral foundation for designing more adaptive, context-aware service systems.
6 Heterogeneous Analysis
Building upon our baseline findings, we further investigate how user-level traits moderate
the effects of three drivers on delivery service choices. Specifically, we explore two forms
of heterogeneity: (1) gender differences and (2) the role of user experience, focusing on
behavioral adaptation through repeated interactions with robot and human delivery services.
In addition, we also model user’s habit formation and reactions to price adjustment in this
section.
6.1 Impact of Gender Heterogeneity
To examine gender differences in delivery preferences, we interact the three contextual drivers
with a gender indicator variable (is_f emale). The gender heterogeneous model is as follows.
16

delivery_type ijst =α+β 1 ·is_sensitive i +β 2 ·lg(package_value) i +β 3 ·is_bad_weather st
+γ 1 ·(is_sensitive i ×is_f emalej)
+γ 2 ·(lg(package_value) i ×is_f emalej)
+γ 3 ·(is_bad_weather st ×is_f emalej)
+β 0 ·X ijst +T imeF Et +ε ijst (3)
As shown in Column (1) of Table 4, while all three main effects remain significant and
directionally consistent with our earlier findings, we observe notable gender-based modera-
tion in two contexts. Specifically, the interaction between bad weather and female user is
significantly negative (-0.0138,p< 0.01), indicating that female users are even more likely
than male users to prefer human delivery under adverse environmental conditions. This re-
sult suggests that women may place greater trust in human couriers when facing uncertainty,
aligning with prior literature on gender differences in risk perception and trust preferences.
Conversely, the interactions between gender and the effects of privacy sensitivity and product
value (-0.0032,p< 0.05) are weaker. The latter suggests that female users are slightly less
likely to choose robot delivery as product value increases, potentially reflecting more cau-
tious attitudes toward automation in high-stakes scenarios. We do not find the interaction
effect between gender and package sensitivity. One possible explanation is that we adopt a
very narrow definition of sensitive packages, and both male and female users may experience
social embarrassment when receiving sexual products or contraceptive supplies.
6.2 Interaction Effect of Main Factors
We next examine whether contextual factors jointly influence delivery choice. Rather than
treating three main factors independently, we explore their interaction: for example, a
privacy-sensitive item delivered during rainy day may trigger qualitatively different pref-
17

Table 4: Heterogeneity effect of gender and user historical behavior
Dependent Variable:delivery_type
(1) (2) (3)
const 0.8963*** (0.0053) 0.8347*** (0.0032) 0.8396*** (0.0031)
is_package_sensitive 0.1285*** (0.0173) 0.0635*** (0.0111) 0.0644*** (0.0104)
is_package_sensitive×is_f emale -0.0463 (0.0310)
is_package_sensitive×robot_cumu_num -0.0005 (0.0011)
is_package_sensitive×human_cumu_num -0.0010 (0.0007)
lg(package_value) 0.0116*** (0.0011) 0.0061*** (0.0005) 0.0050*** (0.0005)
lg(package_value)×is_f emale -0.0032** (0.0014)
lg(package_value)×robot_cumu_num -0.0003*** (0.0000)
lg(package_value)×human_cumu_num -0.0000 (0.0000)
is_bad_weather -0.0084*** (0.0031) -0.0159*** (0.0017) -0.0166*** (0.0016)
is_bad_weather×is_f emale -0.0138*** (0.0037)
is_bad_weather×robot_cumu_num 0.0001 (0.0001)
is_bad_weather×human_cumu_num 0.0004*** (0.0001)
lead_time -0.0235*** (0.0002) -0.0102*** (0.0002) -0.0102*** (0.0002)
lead_time_other 0.0038*** (0.0002) 0.0009*** (0.0001) 0.0009*** (0.0001)
delivery_price -0.1489*** (0.0010) -0.0945*** (0.0007) -0.0945*** (0.0007)
is_f emale -0.0403*** (0.0063) -0.0225*** (0.0014) -0.0226*** (0.0014)
is_ios 0.0047** (0.0018) 0.0024* (0.0013) 0.0024* (0.0013)
is_time_sensitive 0.0020 (0.0024) -0.0003 (0.0017) -0.0001 (0.0017)
is_South 0.0178*** (0.0021) 0.0157*** (0.0015) 0.0157*** (0.0015)
is_school_South -0.1142*** (0.0022) -0.0570*** (0.0016) -0.0569*** (0.0016)
is_211 0.2103*** (0.0026) 0.0449*** (0.0020) 0.0449*** (0.0020)
robot_cumu_num 0.0019*** (0.0002) 0.0007*** (0.0001)
human_cumu_num -0.0016*** (0.0000) -0.0018*** (0.0001)
last_choice_robot 0.2456*** (0.0017) 0.2461*** (0.0017)
last_choice_human -0.4967*** (0.0018) -0.4966*** (0.0018)
T imeF EYes Yes Yes
R2 0.1733 0.5756 0.5755
Observations 241,517 241,517 241,517
Note.*p <0.1, **p <0.05, ***p <0.01. Standard errors are in parentheses.
18

Table 5: Interaction effect of main factors
Dependent Variable:delivery_type
(1)
const -0.0962*** (0.0046)
is_package_sensitive×lg_package_value -0.0211 (0.0141)
is_package_sensitive×is_bad_weather 0.0637** (0.0292)
lg_package_value×is_bad_weather -0.0019 (0.0014)
is_package_sensitive 0.1874*** (0.0691)
lg_package_value 0.0105*** (0.0009)
is_bad_weather -0.0090 (0.0062)
lead_time -0.0235*** (0.0002)
lead_time_other 0.0038*** (0.0002)
delivery_price -0.1489*** (0.0010)
is_f emale -0.0590*** (0.0019)
is_ios 0.0047** (0.0018)
is_time_sensitive 0.0020 (0.0024)
is_South 0.0178*** (0.0021)
is_school_South -0.1140*** (0.0022)
is_211 0.2101*** (0.0026)
T imeF EYes
R2 0.1732
Observations 241,517
Note.*p <0.1, **p <0.05, ***p <0.01. Standard errors are in parentheses.
erences than would be predicted by each condition alone. Table 5 shows a significant inter-
action betweenis_package_sensitiveandis_bad_weather(0.0637,p <0.05), indicating
that users tend to choose robot delivery for sensitive packages when the weather is bad.
The main effect estimates show two countervailing forces:is_package_sensitivein-
19

creases the probability of selecting robot, whereasis_bad_weatherdecreases it. However,
bad weather conditions can attenuate the effect of sensitive packages (i.e., coefficient of the
interaction term is smaller than that ofis_package_sensitivealone in main effect esti-
mates). More specifically, while sensitive packages tend to push customers toward robots,
that push is weakened in bad weather. Customers trade off privacy concerns against weather-
related concerns. This pattern is consistent with theories that distinguish social-evaluative
drivers (which favor robots for sensitive consumption) from competence drivers (which fa-
vor humans under uncertainty), which is reflected in Holthöwer and Van Doorn (2023) on
embarrassment reduction and Wirtz et al. (2018) on trust and adaptability.
6.3 Modeling Dynamic Preferences and Habit Formation
To examine whether consumer delivery preferences evolve over time, we extend our baseline
specification to incorporate dynamic behavioral factors such as habit formation, trust accu-
mulation, and contextual recalibration. Specifically, to assess whether repeated experience
with robot or human delivery influences subsequent choices, we augment our model with
dynamic behavioral indicators. These include whether a user’s last choice was handled by a
robot or human (the user is a new customer when both are zero), as well as the cumulative
number of each delivery type. We augment our model as follows.
delivery_type ijst =α+β 1 ·is_package_sensitive i +β 2 ·lg(package_value) i +β 3 ·is_bad_weather st
+δ 1 ·last_choice_robot jt +δ 2 ·last_choice_human jt
+β 4 ·robot_cumu_num jt +β 5 ·human_cumu_num jt
+γ 1 ·(is_sensitive i ×robot(human)_cumu_num jt)
+γ 2 ·(log(package_value) i ×robot(human)_cumu_num jt)
+γ 3 ·(is_bad_weather st ×robot(human)_cumu_num jt)
+β 0 ·X ijst +T imeF Et +ε ijst (4)
20

wherelast_choice_robot(human) jt indicates whether userjchose robot(human) delivery
on their most recent prior transaction.robot(human)_cumu_num jt captures the cumu-
lative number of robot(human) deliveries made by userjup to timet(current order not
included). The interaction coefficientsγ 1 –γ 3 test whether the main effects are moderated
by accumulated robot(human) service experience.
As reported in Columns (2) and (3) of Table 4, behavioral history significantly shapes
current choices. Users are more likely to repeat their previous choice: having selected robot
delivery in the prior transaction increases the likelihood of choosing it again by 24% – 25%
(p< 0.001), while choosing a human service in the previous choice reduces the probability
of selecting a robot in the current round by around 49.7% (p< 0.001). These strong path
dependencies suggest substantial habit formation in delivery service decisions. Further, cu-
mulative experience also plays a role: the coefficient onrobot_cumu_numis positive and
significant (0.0007–0.0019,p< 0.001), while that onhuman_cumu_numis negative and
significant (-0.0018 – -0.0016,p< 0.001), indicating that growing familiarity with a delivery
type reinforces user preference for that type.
Interestingly, as users accumulate more experience with robot delivery, the positive effect
of product value on the likelihood of choosing a robot diminishes (lg(package_value)×
robot_cumu_num: -0.0003,p <0.001). While first-time or infrequent robot users are more
inclined to choose robots for high-value packages – likely due to perceptions of security and
traceability – this sensitivity weakens over time. Experienced users may grow more confident
in robot performance across all product categories, and as a result, no longer anchor their
delivery choice to item value.
On the other hand, more frequent use of human service also softens the drop in robot de-
liverypreferenceunderadverseweatherconditions(is_bad_weather×human_cumu_num:
0.0004,p <0.001). In the baseline, bad weather discourages robot use due to concerns about
mechanical failure or limited adaptability. However, users with higher human delivery ex-
perience are less reactive to such trust concern: they are less likely to switch away from
21

robots when facing environmental uncertainty. One possible interpretation is the relative
trust recalibration: frequent human delivery users may realize the practical limits of human
adaptability or experience inconsistent performance in poor weather, which makes robot
delivery comparatively more acceptable over time.
This dynamic specification enables us to move beyond static heterogeneity and uncover
the trajectory of consumer adaptation in hybrid human-robot service systems.
6.4 Reactions to Dynamic Delivery Pricing
We further investigate the impact of delivery price on user preference, which makes it possible
to estimate the elasticity of the delivery price. During the study period, four stations adjust
their prices for either of the delivery types. Two stations (station 1 and station 2) decreased
price of human service by 1 RMB (from 2 RMB to 1 RMB) and 1 RMB (from 1 RMB to
free) respectively. Two stations (station 3 and station 4) increased price of robot service by
0.6 RMB (from 2.2 RMB to 2.8 RMB) and 1 RMB (from 1.5 RMB to 2.5 RMB) respectively.
Price changing is exogenous to users. We model this price adjustment by a Difference-in-
Difference (DiD) model as follows.
delivery_type ijst =α
+β·af ter_human(robot)_price_change st ×is_human(robot)_price_change s
+γ·X ijst
+U serF Ej +T imeF Et +ε ijst (5)
whereaf ter_human(robot)_price_changest equals 1 if, for stations, periodtfalls after
that station’s price change for the corresponding delivery type (human or robot), and 0
otherwise;is_human(robot)_price_change s equals 1 for stations that ever changed the
corresponding type’s price during the sample window (treated stations), and 0 for stations
that never did (controls). We estimate the specification separately for human-fee changes
22

and robot-fee changes; in each case, the interactionaf ter×isis the DiD term, and its
coefficientβidentifies the average treatment effect on the treated (ATT).
Table 6: DiD Result for Price Changing
Dependent Variable:delivery_type
(1)
Station 1
(2)
Station 2
(3)
Station 3
(4)
Station 4
const 0.5863*** (0.2237) 0.5697** (0.2240) 0.5694** (0.2241) 0.5675** (0.2241)
af ter_human_price_decrease_station1
×is_human_price_decrease_station1
-0.2721***
(0.0116)
af ter_human_price_decrease_station2
×is_human_price_decrease_station2
-0.1974***
(0.0169)
af ter_robot_price_increase_station3
×is_robot_price_increase_station3
-0.0133**
(0.0055)
af ter_robot_price_increase_station4
×is_robot_price_increase_station4
-0.1469***
(0.0374)
control_variables Omitted
U serF EYes Yes Yes Yes
T imeF EYes Yes Yes Yes
R2 0.1387 0.1367 0.1361 0.1361
Note.*p <0.1, **p <0.05, ***p <0.01. Standard errors are in parentheses.
Table 6 shows the ATT observations with keeping others in the control. Either decreasing
the price of human service or increasing the price of robot delivery intuitively makes users
use more human service: ATT of station 1 is -0.2721 (p <0.001), for which the price of
human service decreases from 2 RMB to 1 RMB; ATT of station 2 is -0.1974 (p <0.001),
for which the price of human service decreases from 1 RMB to 0; ATT of station 3 is -0.0133
(p <0.001), for which the price of robot service increases from 2.2 RMB to 2.8 RMB; ATT
of station 4 is -0.1469 (p <0.001), for which the price of robot service increases from 1.5
RMB to 2.5 RMB.
Based on above estimation, we construct a semi-elasticity (SE),semi_elasticity P =
AT TP
∆P ×100%, reflecting user price sensitivity. The semi-elasticity measures the percentage
change in preference of robot per RMB. Although the signs of SEs are the same, the absolute
value are 27.21, 19.74, 2.22 and 14.69, respectively. Users are more price-sensitive for human
23

service than robot service averagely.
7 Robustness Check
7.1 Alternative Choice Models
We implement two different discrete regressions to strengthen our main results. As shown
in Appendix B Table B1, using Logit and Probit regressions does not change our findings
fundamentally, where users tend to have their sensitive or high-value packages to be delivered
by robots and order human delivery service under adverse weather conditions.
7.2 User-level Fixed Effect
We excluded user-level fixed effect in our main result due to the consideration to check the
impact of user traits. In this section, we add user-level fixed effect to further examine the
robustness. Appendix B Table B2 shows that sensitivity and package value remain significant
but not for bad weather. Stations chosen in this study are campus-based and generally far
away from each other. As a result, no packages for the same user were distributed to
different stations at the same day. Because the variableis_bad_weatherdescribes station-
wide bad weather on a day, adding two-way fixed effects will remove the variation that
previously identified the coefficient (i.e., two-way fixed effects soak up the variation since
is_bad_weatheris measured at station-daily level).
This section incorporates two additional robustness checks with more to be added.
8 Conclusion
This paper utilizes 241,517 package-level delivery choices from 32 Cainiao stations to ex-
amine how product privacy sensitivity, product value, and environmental complexity shape
consumer selections between human and robot last-mile delivery. To the best of our knowl-
24

edge, this is the first empirical investigation of consumer decision-making in human-robot
delivery service environments in a real-world setting. By uncovering how contextual factors
and psychological mechanisms jointly shape delivery choices, our study not only contributes
to the understanding of human-robot interaction in operational settings but also paves the
way for future research on hybrid human-robot service system design, user heterogeneity,
and the evolving role of automation in consumer-facing services.
Main empirical findings.Our findings reveal that consumer preferences in hybrid
human-robot service environments are systematically shaped by contextual factors that ac-
tivate distinct psychological mechanisms. Consumers are more likely to choose robot delivery
for privacy-sensitive and high-value products, reflecting a desire to reduce social exposure
and a perception of robots as secure, traceable, and consistent. In contrast, adverse weather
shifts preference toward human couriers, highlighting trust in human adaptability under
uncertainty. In addition, we find that gender moderates these effects: female users are espe-
cially likely to switch to human delivery under bad weather. The interaction estimates show
that bad weather attenuates the positive effect of privacy sensitivity. We also document
pronounced behavioral dynamics: prior robot choice raises the likelihood of repeating robot
delivery, while prior human choice reduces robot selection, and cumulative experience with
a delivery type reinforces continued use (small but significant cumulative effects). These
results demonstrate that delivery choices are driven not only by functional considerations
such as price or speed, but also by deeper psychological concerns of users. Finally, we show
the different price sensitivities of both delivery types respectively through DiD.
Theoretical contribution.These findings advance theory on robot service choice
in three ways. First, they provide empirical evidence to show that consumer adoption of
automation is not determined solely by instrumental trade-offs (price, speed) but also by
context-activated psychological processes: 1) privacy sensitivity prompts an avoidance of
socially evaluative human interaction, elevating the appeal of non-judgmental robots; 2)
25

product value can amplify concerns about loss or accountability and, in monitored campus
settings, can alternatively increase trust in robots’ traceability; 3) environmental complexity
heightens demand for flexibility. Second, the strong path dependence we observe highlights
habit and trust accumulation as central dynamics in hybrid human-robot service adoption,
implying that short-run menu design and early experiences can have long-run effects on
delivery type shares. Third, by analyzing choices in a field setting where users actively se-
lect the service type (rather than responding to hypothetical prompts), we provide practical
evidence connecting lab-level psychological mechanisms to real-world behavior.
Managerialimplications.Forplatformsandoperatorsdesigninghybridhuman-robot
systems, the results point to three actionable principles. 1) Context-aware channel design:
promote robot delivery prominently for privacy-sensitive categories to strengthen perceptions
of security and non-judgment. 2) Dynamic resource allocation and pricing: anticipate shifts
toward human couriers during adverse weather and consider dynamic staffing or surge pricing
to preserve service quality; pay attention to heterogeneous price sensitivities across delivery
types and stations, which supports targeted price experiments. 3) Experience management
to accelerate desirable adoption: because prior choices strongly predict subsequent choices,
targeted trial incentives and immediate post-delivery promotions can accelerate habit for-
mation for the corresponding delivery type.
Limitations and future research.This study is subject to several limitations that
also open avenues for future work. First, the evidence comes from campus Cainiao Stations,
where demographics and operational structures may differ from broader urban or residential
contexts, suggesting the need for replication in diverse settings and with alternative robot
designs. Although we implement alternative specifications, the observational design cannot
fully eliminate concerns about omitted variables. Experimental approaches could more di-
rectly test the underlying mechanisms. Finally, future research could extend our analysis
to capture long-run dynamics, such as how habit formation influences market shares, cost
26

structures, and welfare outcomes as the automation diffuses.
Taken together, our results indicate that consumer choice in hybrid human-robot delivery
systems is systematic, psychologically grounded, and path-dependent. Designing service
channels that are sensitive to privacy, value, and environmental context, and that proactively
shape early user experiences, can improve both user experience and operational performance
as automation continues to scale.
27

References
Amorim, P., DeHoratius, N., Eng-Larsson, F., & Martins, S. (2024). Customer preferences for
delivery service attributes in attended home delivery.Management Science,70(11),
7559–7578. https://doi.org/10.1287/mnsc.2020.01274
Argo, J. J., Dahl, D. W., & Morales, A. C. (2005). Consumer contamination: How consumers
react to products touched by others.Journal of Marketing Research,42(4), 364–373.
https://doi.org/10.1509/jmkg.70.2.08
Awad, N. F., & Krishnan, M. S. (2006). The personalization privacy paradox: An empiri-
cal evaluation of information transparency and the willingness to be profiled online.
Management Information Systems Quarterly,30(1), 13–28. https://doi.org/10.2307/
25148715
Bai, B., Dai, H., Zhang, D. J., Zhang, F., & Hu, H. (2022). The impacts of algorithmic work
assignment on fairness perceptions and productivity: Evidence from field experiments.
Manufacturing & Service Operations Management,24(6), 3060–3078. https://doi.
org/10.1287/msom.2022.1120
Bauer, R. A. (1960). Consumer behavior as risk taking. InDynamic marketing for a changing
world(pp. 389–398). American Marketing Association.
Beer, J. M., Fisk, A. D., & Rogers, W. A. (2014). Toward a framework for levels of robot
autonomy in human-robot interaction.Journal of human-robot interaction,3(2), 74.
https://doi.org/10.5898/JHRI.3.2.Beer
Carlsson, J. G., Liu, S., Salari, N., & Yu, H. (2023). Provably good region partitioning for
on-time last-mile delivery.Operations Research,72(1), 91–109. https://doi.org/10.
1287/opre.2021.0588
Castelo, N., Boegershausen, J., Hildebrand, C., & Henkel, A. P. (2023). Understanding and
improving consumer reactions to service bots.Journal of Consumer Research,50(4),
848–863. https://doi.org/10.1093/jcr/ucad023
28

Chen, M. K. (2013). The effect of language on economic behavior: Evidence from savings
rates, health behaviors, and retirement assets.American Economic Review,103(2),
690–731. https://doi.org/10.1257/aer.103.2.690
Cui, R., Li, M., & Zhang, S. (2022). AI and procurement.Manufacturing & Service Opera-
tions Management,24(2), 691–706. https://doi.org/10.1287/msom.2021.0989
Dietvorst,B.J.,Simmons,J.P.,&Massey,C.(2015).Algorithmaversion:Peopleerroneously
avoid algorithms after seeing them err.Journal of Experimental Psychology: General,
144(1), 114. https://doi.org/10.1037/xge0000033
Fatehi, S., & Wagner, M. R. (2022). Crowdsourcing last-mile deliveries.Manufacturing &
Service Operations Management,24(2), 791–809. https://doi.org/10.1287/msom.
2021.0973
Featherman, M. S., & Pavlou, P. A. (2003). Predicting e-services adoption: A perceived risk
facets perspective.International Journal of Human-Computer Studies,59(4), 451–
474. https://doi.org/10.1016/S1071-5819(03)00111-3
Fu, R., Huang, Y., & Singh, P. V. (2021). Crowds, lending, machine, and bias.Information
Systems Research,32(1), 72–92. https://doi.org/10.1287/isre.2020.0990
Fügener, A., Grahl, J., Gupta, A., & Ketter, W. (2021). Will humans-in-the-loop become
borgs? Merits and pitfalls of working with AI.Management Information Systems
Quarterly,45(3), 1527–1556. https://doi.org/10.25300/MISQ/2021/16553
Goldfarb, A., & Tucker, C. E. (2011). Privacy regulation and online advertising.Management
Science,57(1), 57–71. https://doi.org/10.1287/mnsc.1100.1246
Han, B. R., Li, M., Zhang, Y., & Li, P. (2024). Value of autonomous last-mile delivery:
Evidence from alibaba.Available at SSRN. https://papers.ssrn.com/sol3/papers.
cfm?abstract_id=5047978
Han, B. R., Sun, T., Chu, L. Y., & Wu, L. (2024). Connecting customers and merchants
offline: Experimental evidence from the commercialization of last-mile stations at
29

alibaba.Management Information Systems Quarterly,48(3), 1157–1192. https://doi.
org/10.25300/MISQ/2022/16674
Holthöwer, J., & Van Doorn, J. (2023). Robots do not judge: Service robots can alleviate
embarrassment in service encounters.Journal of the Academy of Marketing Science,
51(4), 767–784. https://doi.org/10.1007/s11747-022-00862-x
Jeon, H. H., Lucarelli, C., Mazarati, J. B., Ngabo, D., & Song, H. (2022). Last-mile delivery
in health care: Drone delivery for blood products in rwanda.Available at SSRN.
https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4214918
Lim, S. F. W., Wang, Q., & Webster, S. (2023). Do it right the first time: Vehicle routing with
home delivery attempt predictors.Production and Operations Management,32(4),
1262–1284. https://doi.org/10.1111/poms.13926
Liu, S., He, L., & Max Shen, Z.-J. (2021). On-time last-mile delivery: Order assignment with
travel-time predictors.Management Science,67(7), 4095–4119. https://doi.org/10.
1287/mnsc.2020.3741
Lou, B., & Wu, L. (2021). AI on drugs: Can artificial intelligence accelerate drug devel-
opment? Evidence from a large-scale examination of bio-pharma firms.Management
Information Systems Quarterly,45(3), 1451–1482. https://doi.org/10.25300/MISQ/
2021/16565
Lu, T., & Zhang, Y. (2024). 1+1>2? Information, humans, and machines [Forthcoming].
Information Systems Research. https://doi.org/10.1287/isre.2023.0305
Lu, Z., Cui, R., Sun, T., & Wu, L. (2023). The value of last-mile delivery in online retail.
Available at SSRN. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4590356
Luo, X., Tong, S., Fang, Z., & Qu, Z. (2019). Frontiers: Machines vs. humans: The impact
of artificial intelligence chatbot disclosure on customer purchases.Marketing Science,
38(6), 937–947. https://doi.org/10.1287/mksc.2019.1192
30

Ma, S., Ge, L., Jia, H., & Wang, Y. (2025). Understanding and mitigating the robot dis-
advantage in luxury services: The role of desire for superiority.Information Systems
Research. https://doi.org/10.1287/isre.2023.0229
Mayer,R.C.,Davis,J.H.,&Schoorman,F.D.(1995).Anintegrativemodeloforganizational
trust.Academy of Management Review,20(3), 709–734. https://doi.org/10.5465/
amr.1995.9508080335
McKnight, D. H., Choudhury, V., & Kacmar, C. (2002). Developing and validating trust
measures for e-commerce: An integrative typology.Information Systems Research,
13(3), 334–359. https://doi.org/10.1287/isre.13.3.334.81
Mende, M., Scott, M. L., van Doorn, J., Grewal, D., & Shanks, I. (2019). Service robots
rising: How humanoid robots influence service experiences and elicit compensatory
consumer responses.Journal of Marketing Research,56(4), 535–556. https://doi.org/
10.1177/0022243718822827
Pitardi, V., Wirtz, J., Paluch, S., & Kunz, W. H. (2022). Service robots, agency and em-
barrassing service encounters.Journal of service management,33(2), 389–414. https:
//doi.org/10.1108/JOSM-12-2020-0435
Qi, W., Li, L., Liu, S., & Shen, Z.-J. M. (2018). Shared mobility for last-mile delivery: De-
sign, operational prescriptions, and environmental impact.Manufacturing & Service
Operations Management,20(4), 737–751. https://doi.org/10.1287/msom.2017.0683
Raghavan, S., & Zhang, R. (2024). The driver-aide problem: Coordinated logistics for last-
mile delivery.Manufacturing & Service Operations Management,26(1), 291–311.
https://doi.org/10.1287/msom.2022.0211
Smith, H. J., Milberg, S. J., & Burke, S. J. (1996). Information privacy: Measuring indi-
viduals’ concerns about organizational practices.Management Information Systems
Quarterly,20(2), 167–196. https://doi.org/10.2307/249477
31

Wang,W.,Liu,X.,Zhang,X.,&Hong,Y.(2023).Knowledgetrap:Humanexpertsdistracted
by details when teaming with AI.Available at SSRN. https://papers.ssrn.com/sol3/
papers.cfm?abstract_id=4395858
Wang, X. S., Zhang, Y., & Zheng, J. (2024). Beyond the value for ai adopters: Analyzing the
impacts of autonomous vehicle testing on traffic conditions in california.Available at
SSRN. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4775378
Wirtz, J., Patterson, P. G., Kunz, W. H., Gruber, T., Lu, V. N., Paluch, S., & Martins, A.
(2018). Brave new world: Service robots in the frontline.Journal of Service Manage-
ment,29(5), 907–931. https://doi.org/10.1108/JOSM-04-2018-0119
Wu, L., Li, P., Han, B. R., Li, M., & Zhang, Y. (2023). Value of autonomous last-mile
delivery: Evidence from alibaba.ICIS 2023 Proceedings. https://aisel.aisnet.org/
icis2023/hti/hti/2
Xu, Y., Dai, H., & Yan, W. (2024). Identity disclosure and anthropomorphism in voice
chatbot design: A field experiment.Management Science. https://doi.org/10.1287/
mnsc.2022.03833
Yalcin, G., Lim, S., Puntoni, S., & van Osselaer, S. M. (2022). Thumbs up or down: Consumer
reactions to decisions by algorithms versus humans.Journal of Marketing Research,
59(4), 696–717. https://doi.org/10.1177/00222437211070016
Yan, A., & Xu, D. (2021). Ai-human hybrid for depression treatment: The moderating
role of social stigma.ICIS 2021 Proceedings. https://aisel.aisnet.org/icis2021/
is_implement/is_implement/8
You, S., & Robert Jr., L. P. (2024). Trusting and working with robots: A relational demogra-
phy theory of preference for robotic over human co-workers.Management Information
Systems Quarterly,48(4), 1297–1330. https://doi.org/10.25300/MISQ/2023/17403
Zhang, M., Han, B., Sun, T., Luo, L., & Golden, J. (2025).Motivating consumer and ai
co-creation(tech. rep.) (Working Paper).
32

Zhou, B., Chen, K., & Zhen, J. (2023).2023 global smart last-mile logistics outlook. Deloitte
Insights. https://www.deloitte.com/cn/en/services/consulting/perspectives/2023-
global-smart-last-mile-logistics-outlook.html
33

Appendix A: Additional Information
Figure A1: Cainiao Station
Figure A2: Cainiao Autonomous Delivery Robot
34

Appendix B: Tables for Robustness Checks
Table B1: Alternative models (Logit & Probit)
Dependent Variable:delivery_type
(1)
Logit
(2)
Probit
const 2.7700*** (0.0263) 2.7700*** (0.0263)
is_package_sensitive 0.5992*** (0.0783) 0.5992*** (0.0783)
lg(package_value) 0.0649*** (0.0036) 0.0649*** (0.0036)
is_bad_weather -0.1314*** (0.0097) -0.1314*** (0.0097)
lead_time -0.1282*** (0.0014) -0.1282*** (0.0014)
lead_time -0.0051*** (0.0007) -0.0051*** (0.0007)
delivery_price -1.1686*** (0.0082) -1.1686*** (0.0082)
is_f emale -0.3071*** (0.0100) -0.3071*** (0.0100)
is_ios 0.0585*** (0.0095) 0.0585*** (0.0095)
is_time_sensitive 0.0233* (0.0125) 0.0233* (0.0125)
is_South 0.1163*** (0.0108) 0.1163*** (0.0108)
is_school_South -0.5664*** (0.0115) -0.5664*** (0.0115)
is_211 1.0690*** (0.0167) 1.0690*** (0.0167)
is_M onday 0.0150 (0.0174) 0.0150 (0.0174)
is_T uesday -0.0294* (0.0176) -0.0294* (0.0176)
is_T hursday 0.0221 (0.0174) 0.0221 (0.0174)
is_F riday 0.0687*** (0.0175) 0.0687*** (0.0175)
is_Saturday 0.0836*** (0.0175) 0.0836*** (0.0175)
is_Sunday 0.1204*** (0.0169) 0.1204*** (0.0169)
P seudo R2 0.1679 0.1679
Observations 241517 241517
Note.*p <0.1, **p <0.05, ***p <0.01. Standard errors are in parentheses.
35

Table B2: Main Result with Two-way Fixed Effect
Dependent Variable:delivery_type
(1)
One-way FE
(2)
Two-way FE
const 0.9069*** (0.0040) 0.4708** (0.2315)
is_package_sensitive 0.1149*** (0.0143) 0.0231** (0.0100)
lg(package_value) 0.0097*** (0.0007) 0.0032*** (0.0005)
is_bad_weather -0.0163*** (0.0022) -0.0014 (0.0016)
lead_time -0.0235*** (0.0002) -0.0065*** (0.0002)
lead_time 0.0038*** (0.0002) -0.0003** (0.0001)
delivery_price -0.1489*** (0.0010) -0.0988*** (0.0009)
is_F emale -0.0590*** (0.0019)
is_ios 0.0047** (0.0018)
is_time_sensitive 0.0020 (0.0024)
is_South 0.0178*** (0.0021)
is_school_South -0.1140*** (0.0022) 0.1379 (0.3361)
is_211 0.2101*** (0.0026) 1.0659*** (0.2059)
U serF ENo Yes
T imeF EYes Yes
R2 0.1732 0.0776
Observations 241517 241517
Note.*p <0.1, **p <0.05, ***p <0.01. Standard errors are in parentheses.
36
