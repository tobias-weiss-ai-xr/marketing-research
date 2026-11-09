---
title: 'Data-Driven Analysis of Omnichannel Purchasing Pathways: Age and Gender Effects Across Retail
  Product Categories'
url: https://doi.org/10.30657/pea.2026.32.34
category: cx-retail
subcategory: empirical
date: 2026-06
venue: Production Engineering Archives
authors:
- Emília Madudová
- Tatiana Čorejová
- Margita Majerčáková
source: openalex-oa
pdf_url: https://reference-global.com/download/article/10.30657/pea.2026.32.34.pdf
pages: 14
chars: 79449
fetched_at: '2026-11-08T17:33:44+00:00'
kb_version: 1
---

# Data-Driven Analysis of Omnichannel Purchasing Pathways: Age and Gender Effects Across Retail Product Categories

© 2026 Author(s).  This is an open access article licensed
                          under the Creative Commons Attribution (CC BY)
                          License (https://creativecommons.org/licenses/by/ 4.0/).
 416                                                                      ARCHIWUM INŻYNIERII PRODUKCJI

PRODUCTION ENGINEERING ARCHIVES  2026, 32(3), 416-429

PRODUCTION ENGINEERING ARCHIVES
ISSN 2353-5156  (print)
ISSN 2353-7779  (online)
Exist since 4th quarter 2013
Available online at https://pea-journal.eu

Data-Driven Analysis of Omnichannel Purchasing
Pathways: Age and Gender Effects Across Retail Product
Categories
Emília Madudová1* , Tatiana Čorejová1 , Margita Majerčáková1
1 Žilinská univerzita v Žiline, Univerzitná 8215/1 010 26 Žilina Slovak Republic; emilia.madudova@uniza.sk (EM);
tatiana.corejova@uniza.sk (TČ); margita.majercakova@uniza.sk (MM)
*Correspondence: emilia.madudova@uniza.sk

Article history
Received 30.03.2026
Accepted 01.06.2026
Available online 30.06.2026
 Abstract
The emergence of omnichannel environments has transformed consumer purchasing into a highly
complex, multistage decision-making process, generating nonlinear demand signals that heavily influ-
ence retail logistics, inventory optimization, and production engineering systems. Moving beyond the
binary choice between online and offline commerce, omnichannel purchasing reflects structured path-
ways through which consumers allocate information search and transaction activities across multiple
touchpoints. This paper investigates how age and gender influence these purchasing pathways across
selected product categories using a data-driven analytical framework. The empirical analysis is based
on primary survey data collected from 889 consumers with prior omnichannel purchasing experience.
To identify systematic differences and predictive patterns in purchasing behavior, categorical data
analysis methods are employed, including chi-square tests of independence, association measures, and
multinomial logistic regression (MLR). The results indicate that omnichannel purchasing behavior
varies significantly across age groups, with younger consumers displaying stronger tendencies toward
digitally completed transactions, even when physical stores are involved in the earlier stages of the
purchasing process. Older consumers exhibit greater reliance on in-store purchasing in selected prod-
uct categories, suggesting differences in channel substitution and complementarity. Gender-based var-
iations further shape purchasing pathways, particularly in webrooming and showrooming behaviors,
highlighting the importance of demographic segmentation in channel integration strategies. Additional
heterogeneity was observed in channel interaction patterns across demographic segments, further re-
inforcing the structured nature of omnichannel purchasing pathways. These findings provide insights
into demand allocation across channels and offer implications for the design and evaluation of omni-
channel retail systems within contemporary digital economies.
Keywords
omnichannel purchasing,
consumer pathways,
retail economics,
Demographic heterogeneity.

DOI: 10.30657/pea.2026.32.34

1. Introduction
In the context of contemporary industrial operations, the
seamless integration of digital and physical retail channels has
fundamentally disrupted traditional supply chain management
and production engineering systems  (Aflaki et al., 2020;
Madlenak et al., 2023;  Strenitzerová et al., 2018).  The emer-
gence of omnichannel environments has transformed con-
sumer purchasing into a highly complex multistage decision -
making process. This behavioral shift has profound implica-
tions for retail logistics, inventory optimization, and demand
forecasting frameworks.  From a production engineering and
operations management perspective, omnichannel retailing
represents a massive, decentralized demand -allocation prob-
lem. Consumers dynamically distribute their information
search and transaction activities across multiple intercon-
nected touchpoints, thereby generating nonlinear demand sig-
nals that heavily influence reverse logistics, warehousing ca-
pacity requirements, and last-mile delivery operations.
Although extensive research in industrial engineering has
evaluated the optimization of production processes and static
logistics networks, achieving continuous operational improve-
ment requires a robust, data -driven understanding of the de-
mand-side drivers that initiate these supply chains (Madlenak

EMÍLIA MADUDOVÁ ET AL.. / PRODUCTION ENGINEERING ARCHIVES 2026, 32(3), 416-429

 417                                                                      ARCHIWUM INŻYNIERII PRODUKCJI

et al., 2020). Omnichannel consumer pathways characterized
by behaviors such as webrooming, showrooming, and dy-
namic cross-channel movement are critical. They dictate how
physical inventory must be allocated across regional distribu-
tion centers versus brick -and-mortar storefronts to prevent
costly stockouts and minimize the holding costs.  Therefore,
investigating how demographic heterogeneity, specifically
age and gender cohorts, influences these purchasing pathways
is essential for the systemic design, capacity planning, and op-
erational resilience of modern retail engineering systems.
Previous research has highlighted both the opportunities and
challenges associated with omnichannel strategies. Studies
such as Hole et al. (2019) identified key factors shaping om-
nichannel behavior and emphasized the complexity of inte-
grating multiple cha nnels within retail systems. Similarly,
Maggioni et al. (2020) provide insights into cross-channel pur-
chasing behavior, demonstrating that discrepancies may arise
between retailer strategies, consumer expectations and pur-
chasing plans. Other studies questi on whether omnichannel
strategies are universally beneficial, pointing to potential inef-
ficiencies and coordination challenges across channels (Chen
et al., 2023; Liu et al., 2020 a; Zhao et al., 2020). These find-
ings suggest that omnichannel behavior should be examined
not only as a marketing phenomenon but also as an economi-
cally structured decision-making process.
This study was motivated by the need to better understand
how consumers navigate omnichannel retail environments, as
digital touchpoints create nonlinear demand signals.  This
study addresses this gap by conceptualizing omnichannel pur-
chasing as a structured multistage decision -making pathway
rather than an isolated channel choice. While omnichannel re-
tailing has been widely examined, limited attention has been
paid to how consumers systematically integrate browsing and
transaction activities across online a nd physical channels in
discrete demographic segments.
To date, no study has simultaneously quantified the effect
of both age and gender on discrete omnichannel purchasing
pathways across multiple product categories within a single
unified analytical framework, leaving a critical empirical gap
at the intersection of consumer demographics and retail engi-
neering demand allocation.
Accordingly, this study adopts a data-driven approach to an-
alyzing omnichannel purchasing as an economic decision -
making process. By examining age- and gender-based differ-
ences across multiple product categories, this study provides
empirical evidence relevant to retail logistics and digital com-
merce, enhancing the understanding of how consumer demand
is allocated across decentralized retail systems.
From the perspective of retail economics, omnichannel pur-
chasing can be conceptualized as an allocation problem,
wherein consumers distribute their information searches and
transaction activities across competing and complementary
distribution channels.  Instead of selecting a single channel,
consumers encounter trade -offs related to transaction costs,
information asymmetry, perceived risk, and convenience.
These trade -offs differ across product categories and demo-
graphic groups, resulting in diverse purchas ing pathways in
omnichannel retail systems. Economic research indicates that
channel choice is influenced not only by price considerations
but also by non-monetary costs, such as search effort, time in-
vestment, and uncertainty associated with product evaluation.
Physical retail environments reduce uncertainty for experi-
ence and credence goods by allowing direct inspection,
whereas digital channels often offer lower transaction costs
and greater price transparency. Omnichannel behavior reflects
rational decision-making under heterogeneous constraints, ra-
ther than inconsistent consumer behavior.
Recent studies have emphasized the importance of channel
complementarity, highlighting that online and offline channels
frequently serve different functional roles in the purchasing
process (Gao and Fan, 2021).  Online channels tend to domi-
nate information searches and price comparisons, whereas
physical stores provide experiential validation and risk reduc-
tion. This complementarity challenges traditional substitution-
based views of retail channel competition and supports a more
integrated understanding of omnichannel retailing.
Despite these insights, empirical evidence on how consum-
ers allocate purchasing activities across channels in a struc-
tured manner remains limited, particularly when accounting
for demographic heterogeneity and product -specific charac-
teristics. Many existing studies have focused on isolated chan-
nel preferences or single-stage decisions, leaving a critical re-
search gap in understanding how browsing and purchasing
decisions are combined into coherent purchasing pathways in
omnichannel environments.
2. Literature review
The distinction between consumers and customers in online
shopping is a focal point in contemporary literature. Research
by Shih et al. (2019) and Țoniș-Bucea-Manea et al. (2019) ex-
plored customer perception and behavior, finding that while
online shopping is often perceived as a superior option, secu-
rity concerns remain a significant barrier. Additionally, Țoniș-
Bucea-Manea et al. (2019) emphasized the diverse factors in-
fluencing consumer behavior within the Internet of Things
(IoT) ecosystem. Joshi et al. (2021) evaluate the impact of de-
mographics on customer attitudes, while Zhao et al. (2022)
provide a theoretical framework for understanding behavioral
patterns in virtual storefronts.  Singh and Srivastava (2019)
further demonstrate that consumer engagement in multichan-
nel online retail environments is shaped by both individual
characteristics and channel -specific attributes, with demo-
graphic factors playing a measurable role in determining the
depth and consistency of cross -channel interactions.  Collec-
tively, these studies demonstrate the multidimensional nature
of consumer behavior in digital settings.  However, to effec-
tively support online business operations, research must move
beyond these descriptive insights to address the specific barri-
ers, such as webrooming and showrooming, that hinder wider
omnichannel adoption, particularly among younger demo-
graphic segments.
While contemporary retail research increasingly recognizes
multi-rooming, characterized by a fluid, non-linear oscillation
between multiple digital and physical touchpoints (Moliner &

EMÍLIA MADUDOVÁ ET AL.. / PRODUCTION ENGINEERING ARCHIVES 2026, 32(3), 416-429

ARCHIWUM INŻYNIERII PRODUKCJI                                    418

Tortosa-Edo, 2024) as the global hallmark of omnichannel en-
vironments, the operational optimization of retail engineering
systems requires a more granular decomposition of these jour-
neys. It is insufficient to view omnichannel integration only as
a global, outward phenomenon; rather, the substance of the re-
search must lie in identifying the specific internal structural
pathways that consumers navigate.
For the purposes of this study, 'omnichannel purchasing
pathways' are conceptualized as discrete, sequentially struc-
tured behavioral patterns through which consumers allocate
information search and transaction activities across digital and
physical retail touchpoints within a single purchase episode.
This definition explicitly distinguishes these pathways from
(a) multichannel behavior, which involves parallel but unco-
ordinated channel use, and (b) the broader multi-rooming phe-
nomenon (Moliner & Tortosa -Edo, 2024), which describes
fluid, nonlinear oscillation across all available touchpoints.
Our operationalization focuses specifically on measurable
two-stage sequences webrooming (Online→BM) and show-
rooming (BM→Online) as well as consistent single -channel
paths (Online/Online; BM/BM), enabling precise empirical
quantification of demand allocation patterns. As visually syn-
thesized in our framework, Omnichannel Purchasing Path-
ways' (Figure 1), this approach allows for a precise mapping
of how consumers move thr ough space and time to execute a
transaction. While a general omnichannel view assumes a
seamless 'everything-with-everything' interaction, production
and fulfillment networks require the identification of specific
trajectories to effectively manage inventory allocation and de-
mand forecasting.  By focusing on these isolated pathways,
this study provides the necessary architectural insight into the
discrete behavioral sequences that initiate supply chain opera-
tions, effectively bridging the gap between global  consumer
trends (Moliner & Tortosa -Edo, 2024) and the systemic re-
quirements of modern retail engineering ecosystems.
Recent theoretical advancements emphasize that modern re-
tail must accommodate highly complex, cross -channel free -
riding behaviors, prominently characterized as ' multi -room-
ing ' (Moliner & Tortosa-Edo, 2024). Furthermore, the under-
lying drivers of these behaviors are heavily mediated by inter-
nal reasoning patterns related to consumer value (Zafar et al.,
2023).
Despite these conceptual developments, a critical research
gap remains: the literature lacks a granular , empirical synthe-
sis of how discrete demographic variables (age and gender)
systematically dictate nonlinear purchasing pathways across
distinct product categories.  This study provides a theoretical
contribution by moving beyond descriptive frameworks and
explicitly quantifying how demographic heterogeneity drives
decentralized demand allocation, which is a critical input re-
quired for optimizing modern retail supply chains and produc-
tion engineering networks.
2.1. Omnichannel Adoption Across Generations
Engaging with multiple channels for a single purchase and
transitioning between touchpoints throughout the shopping
process exemplifies omnichannel behavior.  For practitioners
and researchers, it is of considerable interest to investigate the
factors contributing to consumers' channel switching during
their purchasing journey, as this understanding facilitates the
formulation of more effective cross-channel marketing strate-
gies. Furthermore, statistically significant differences in chan-
nel interactions have  been identified across gender cohorts
(Matos et al., 2022).
Despite the potential advantages of omnichannel retailing,
barriers to adoption persist as significant concerns, particu-
larly among younger consumers.  Joshi et al. (2021) explored
the challenges hindering young consumers' engagement in
omnichannel retailing, offering valuable insights for retailers
aiming to target this demographic effectively  while Rukmana
et al. (2019) identified key determinants of omnichannel ser-
vice adoption, finding that perceived usefulness and trust re-
main critical factors influencing consumers' willingness to en-
gage across multiple channels, with notable variation across
demographic groups.  Building on this foundation, the present
study focuses on the behavioral patterns of Generation Y and
Generation Z (Table 1), as these cohorts represent the primary
drivers of digital-physical channel integration in retail.
The study by Beregovskaya et al. (2020) highlights both the
opportunities and challenges of implementing omnichannel
marketing for Generation Z. While these consumers value the
ability to independently choose interaction modes and switch
channels seamlessly, significant barriers remain, including the
lack of standalone online sales channels, slow -loading plat-
forms with cumbersome interfaces, and limited mobile app
functionality
Table 1. Generations Z and Y Definitions (Source: Joshi et al.,
2021)
*Note: Note: The age ranges presented in the 'Age Group in Re-
search' column represent the operational sample brackets used in
this study (data collection 2024-2025) and are defined to capture the
digitally active sub-cohorts of Generations Y and Z most relevant to
omnichannel retail behavior, rather than the full generational birth-
year ranges.
2.2. The role of webrooming and showrooming in om-
nichannel integration
The omnichannel concept involves a cohesive and inte-
grated experience encompassing various touchpoints, includ-
ing brick-and-mortar stores, online shops, and direct market-
ing efforts.  This ecosystem extends to mass communication
platforms (television, radio, print) and digital channels such as
Age
Group
(Birth
Year)
Generation
Age
Group
in Re-
search
Key Characteristics
Born
1997
-
2012
Generation Z
(Centennials,
Zoomers)
18-23
Self-sufficient, multitask-
ing, open to digital ad-
vancements, and valuing
authentic communication.
Born
1981
-
1996
Generation Y
(Millennials) 24 - 42
They are collaborative,
achievement-oriented,
creative, and highly adap-
tive to new technologies.

EMÍLIA MADUDOVÁ ET AL.. / PRODUCTION ENGINEERING ARCHIVES 2026, 32(3), 416-429

 419                                                                      ARCHIWUM INŻYNIERII PRODUKCJI

social media, search engines, comparison websites, and
branded mobile applications (Öztürk & Okumuş, 2018).
While retailers recognize the necessity of adopting omnichan-
nel strategies, empirical data on the extent and effectiveness
of this transformation remain limited, complicating the identi-
fication of key operational enhancements (Acquila-Natale and
Iglesias-Pradas 2021; Iglesias-Pradas et al. 2022).
Establishing a showroom channel requires the strategic
alignment of online and offline operations. Delivering a seam-
less service experience incurs specific effort costs that must be
balanced against the benefits of reducing consumer uncer-
tainty. Research indicates that the optimal decision -making
process for a retailer differs significantly before and after
opening a showroom channel, particularly regarding return
rates and service quality (Liu, 2021; Liu et al., 2020b).
Wieland (2023) suggested that shopping channel selection
is primarily determined by consumers ‘spatial , sociodemo-
graphic, and psychographic traits. Factors such as transaction
costs, including travel time, delivery fees, and information
search effort, significantly influence both store selection and
overall spending. Despite the importance of retail geography,
a notable gap remains in exploring spatial shopping behavior
when consumers are presented with integrated online -offline
options (Wieland 2021).
Based on the established theoretical framework and the need
to examine the complex multistage pathways inherent in om-
nichannel environments, the following formal hypotheses
were developed:
H0a: There is no statistically significant association between
demographic factors (age and gender) and the preferred spatial
choice of purchasing location (online versus physical store)
across the evaluated product segments (groceries, alcohol,
drugstore, cosmetics, books, electronics, clothing, and foot-
wear).
H1a: There is a statistically significant association between
demographic factors (age and gender) and the preferred spatial
choice of purchasing location across the evaluated product
segments.
The evolving technological landscape plays a critical role in
these transitions. Alexander and Kent (2022) examined the
impact of technology on in-store customer experiences, while
Ariannezhad et al. (2021) focused on understanding multi -
channel customer b ehavior. Furthermore, Chang and Chen
(2022) highlighted that Generations Y and Z follow distinct
shopper journeys, requiring targeted demographic strategies.
To critically examine these sequences (e.g., browsing online
and purchasing in-store or examining in-store and purchasing
online), a second set of hypotheses was formulated:
    H0b: There is no statistically significant association be-
tween demographic factors (age and gender) and the sequenc-
ing of the purchase decision -making process (specifically
webrooming, showrooming, or multirooming pathways).
    H1b: There is a statistically significant association be-
tween demographic factors (age and gender) and the sequenc-
ing of the purchase decision-making process.
However, the difference in purchasing amount between the
group of customers who joined online membership and used
offline channels and another customer group that joined of-
fline membership and used online channels was not statisti-
cally significant in Kang et al. (2019). Loupiac et al. (2019)
revealed that direct online experience on a website creates be-
liefs about the physical stores of the same brand. These beliefs,
in turn, influence consumer attitudes towards the store (Kao et
al., 2021). Many luxury bra nds treat their online and offline
experiences as distinct and separate entities. However, in the
era of omnichannel retailing, luxury brands that seek to cir-
cumvent future marketplace challenges should strive to pro-
vide a cohesive shopping experience that  integrates both
online and in -store elements (Burnasheva, 2019). The omni-
channel consumer journey exerts both direct and indirect ef-
fects on electronic satisfaction (eS). Notably, women and
younger consumers reported higher levels of e -satisfaction
(Moliner and Tortosa-Edo, 2024).
Zhang (2023) confirmed the impact of omnichannel integra-
tion on consumer purchasing decisions. This study analyses
the effectiveness of integrated marketing strategies and seam-
less customer experiences. In addition, the study by Kang et
al. (2019) provides  empirical evidence of omnichannel pur-
chasing patterns, influencing health and lifestyle products
across different channels. Compared to consumers who
choose home delivery, those who choose alternative options
are more likely to engage in physical effort b ut are less inter-
ested in closely monitoring informational updates. The re-
quirement for social interaction often discourages consumers
from opting for attended deliveries, thereby making unat-
tended options, such as home delivery and self -collection,
more a ttractive. Additionally, factors such as socio -demo-
graphic characteristics and product value influence consumer
preferences (Sun et al., 2020; Wang et al. 2024). Creating om-
nichannel strategies requires an understanding of how custom-
ers use multiple channels in a multichannel environment (Gas-
parin and Slongo, 2023).
The provision of free Wi -Fi network access in physical
stores is another key element in facilitating channel integra-
tion, especially considering that mobile devices are currently
redefining the in-store experience. In addition to providing an
overview of omnichannel in this field, the research evaluates
the association between age and gender.
3. Materials and Methods
Primary data were collected using a structured quantitative
research design aimed at analyzing omnichannel purchasing
behavior across online and offline retail environments. This
study focused on consumers with prior experience in omni-
channel shopping, allowing for the examination of purchasing
pathways involving multiple touchpoints. Data were collected
between 2024 and 2025, reflecting a contemporary retail con-
text characterized by increasing digital-physical channel inte-
gration. Primary data were gathered using an electronic, self -
administered questionnaire (CAWI method) hosted on the
Google Form platform.  The data collection phase was con-
ducted between 2024 and 2025. To reach the target audience,
the survey was distributed through targeted digital communi-
cation channels, including social media groups and university-

EMÍLIA MADUDOVÁ ET AL.. / PRODUCTION ENGINEERING ARCHIVES 2026, 32(3), 416-429

ARCHIWUM INŻYNIERII PRODUKCJI                                    420

affiliated networks, focusing on individuals with active expe-
rience in online purchasing
A total of 889 valid and eligible responses were included in
the final dataset of this study. The sample size provides a suf-
ficient empirical basis for comparative analyses across demo-
graphic groups and product categories. Respondents were cat-
egorized into four age groups (18-23, 24-29, 30-36, and 37-42
years) and by gender (male and female), enabling the assess-
ment of demographic heterogeneity in purchasing behaviors
and channel allocation preferences . This demographic seg-
ment was selected because of its high engagement with digital
technologies and e -commerce platforms.  The demographic
composition of the sample was informed by official census
data from the Statistical Office of the Slovak Republic, ensur-
ing that the age and gender distribution of respondents broadly
reflects the structure of the target population.
The research instrument was developed based on a multi -
dimensional framework of five key omnichannel identifiers
derived from established marketing literature: 1) Channel In-
terconnectivity; 2) Content Consistency; 3) Process Continu-
ity; 4) Individual Appro ach; and 5) Delivery/Payment Flexi-
bility. The questionnaire consisted of 29 items, including
nominal filter questions, ordinal preference scales, and spe-
cific behavioral scenarios (e.g., BOPAC adoption)
3.1. Research design and data analysis methods
While contemporary omnichannel research frequently em-
ploys variance -based structural equation modeling (PLS -
SEM) to explore latent psychological variables (Ali et al.,
2023), the specific objectives of this study necessitated a dif-
ferent statistical paradigm.  PLS-SEM is optimal for continu-
ous latent constructs; however, the primary variables analyzed
here, specifically the discrete spatial choice of transaction lo-
cation and demographic cohort membership, are nominal and
categorical. Consequently, this study employed a rigorous
non-parametric categorical data analysis framework.
The Pearson Chi -Square Test of Independence, coupled
with standardized residual analysis, is mathematically optimal
for identifying statistically significant structural associations
across discrete demographic cohorts. These categorical meth-
ods effectively map the topological distribution of the pur-
chasing pathways.
To enhance the analytical depth and address the predictive
power of demographic variables, multinomial logistic regres-
sion (MLR) was employed. This method allowed for modeling
the probability of specific consumer behaviors and purchase
motivators based on age cohorts and channel interaction pref-
erences of the consumers.  The model's goodness -of-fit was
evaluated using the Nagelkerke R2 coefficient, and the signif-
icance of individual predictors was determined using Likeli-
hood Ratio Tests.  This advanced techni que complements the
non-parametric analysis by quantifying how structural demo-
graphic factors and digital touchpoint engagement influence
the consumer's decision-making process.
This analytical perspective enables a more nuanced under-
standing of consumer behavior beyond single -channel prefer-
ences and aligns with contemporary research on omnichannel
retailing. Table 2 summarizes the operationalization of the key
constructs, demographic variables, and analytical dimensions.
This design supports the identification of structured omni-
channel purchasing pathways and facilitates systematic com-
parisons across demographic segments of consumers.
Table 2. Primary research design (Source: Authors)
Research problem:
Identification of consumer behavior (Generation Y and Z)
in relation to key consumer journey identifiers through
online and offline touchpoints.
Partial research goal:
Omnichannel Adoption Across Generations
Hypothesis Primary research
H0a: There is no statistically signifi-
cant association between demo-
graphic factors (age and gender) and
the preferred spatial choice of pur-
chasing location (online versus phys-
ical store) across the evaluated prod-
uct segments (groceries, alcohol,
drugstore, cosmetics, books, elec-
tronics, clothing, and footwear).
H1a: There is a statistically signifi-
cant association between demo-
graphic factors (age and gender) and
the preferred spatial choice of pur-
chasing location across the evaluated
product segments.
Age group:
18-23;24-29;30-
36;37-42.
Gender:
Male (M); Female
(F)
Omnichannel decision path-
way
Captured through consumers’
sequential interactions with online
and offline touchpoints, identifying
webrooming, showrooming, and
consistent channel paths.
H0b: There is no statistically signifi-
cant association between demo-
graphic factors (age and gender) and
the sequencing of the purchase deci-
sion-making process (e.g., specific
webrooming, showrooming, or
multi-rooming pathways).
H1b: There is a statistically signifi-
cant association between demo-
graphic factors (age and gender) and
the sequencing of the purchase deci-
sion-making process.
Purchasing spa-
tial choice behavior :
Operationalized as con-
sumers’ preferred trans-
action channel (online
vs. brick -and-mortar)
across eight categories:
1) groceries; 2) alcohol;
3) drugstore; 4) cosmet-
ics; 5) books; 6) elec-
tronics; 7) clothing; and
8) footwear.
Purchasing Pathways Definitions
    a) Webrooming (Online/BM): Browse online and complete
the purchase in a brick-and-mortar store.
    b) Showrooming (BM/Online): Examine the product in a
brick-and-mortar store and complete the purchase online.
    c) Pure Offline (BM/BM): Examine and complete the pur-
chase entirely within a brick-and-mortar environment.
    d) Pure Online (Online / Online): Browse and complete the
purchase entirely through online platforms
* While multirooming  represents the broader behavioral
context, our analysis strictly isolates specific measurable se-
quences, such as webrooming and showrooming, to meet the sys-
temic requirements of retail engineering and inventory optimi-
zation

EMÍLIA MADUDOVÁ ET AL.. / PRODUCTION ENGINEERING ARCHIVES 2026, 32(3), 416-429

 421                                                                      ARCHIWUM INŻYNIERII PRODUKCJI

To complement significance testing, measures of associa-
tion, such as Cramér’s V and the contingency coefficient, were
used to assess the strength of the observed relationships. The
inclusion of effect size measures is particularly important in
large-sample studies (N = 889), where statistical significance
alone may not adequately capture the substantive relevance of
observed associations.
4. Results and discussion
The empirical analysis provides a segmented examination
of omnichannel purchasing behavior across multiple retail
product categories, including cosmetics, books, electronics,
clothing, footwear, groceries, alcohol, and drugstore items.
The drugstore category exhibited strong and consistent de-
mographic differentiation across all age groups, with signifi-
cant deviations in both male and female cohorts. In the cos-
metics sector, notable correlations between age, gender, and
channel preference were identified. Specifically, among re-
spondents aged 18-23, males exhibited a propensity for show-
rooming behavior in the cosmetics category while showing a
negative deviation for pure online purchasing (Appendix 2).
The book segment demonstrated the high est degree of demo-
graphic differentiation, particularly within the 30 -36 and 37 -
42 age groups, respectively.
Within the electronics segment, statistically significant as-
sociations were absent among the oldest cohort (37 -42;
p=.176), whereas younger age groups and the aggregate sam-
ple demonstrated significant associations (Total: p=.006,
V=.119), albeit with a weak overall effect size indicating com-
paratively uniform channel allocation behavior relative to
other product ca tegories. In the alcohol segment, statistically
significant associations were identified across all age groups,
including the youngest cohort (18 -23; p=.002) and the 30 -36
group (p<.001), indicating consistent demographic differenti-
ation in channel preferences for this product category.
Table 3. Categorical Analysis of Spatial Purchasing Behavior Across
Product Segments (N=889) (Source: Authors)
Category / Age Pearson χ2  df p-value Cramér’s V
Groceries

18-23 1.510 1 .219 .095
24-29 14.035 2 .001 .263
30-36 7.603 2 .022 .167
37-42 33.472 2 <.001 .370
Total Groceries 29.265 3 .002 .183
Alcohol

18-23 12.923 2 .002 .277
24-29 9.383 2 .009 .215
30-36 33.676 3 <.001 .351
37-42 30.158 3 <.001 .351
Total Alcohol 10.061 3 .018 .106
Drugstore

18-23 23.289 3 <.001 .372
24-29 28.754 3 <.001 .376
30-36 28.274 3 <.001 .322
37-42 15.479 3 .001 .251
Total Drugstore 68.186 3 <.001 .277
Cosmetics

18-23 17.622 3 <.001 .324
24-29 40.602 3 <.001 .447
30-36 16.476 3 <.001 .246
37-42 37.497 3 <.001 .391
Total Cosmetics 36.037 3 <.001 .201
Books

18-23 1.816 3 .612 .104
24-29 11.978 3 .007 .243
30-36 83.590 3 <.001 .553
37-42 56.199 3 <.001 .479
Total Books 57.488 3 <.001 .254
Electronics

18-23 22.456 3 <.001 .366
24-29 25.189 3 <.001 .352
30-36 48.534 3 <.001 .422
37-42 4.937 3 .176 .142
Total Electronics 12.578 3 .006 .119
Clothing

18-23 44.605 2 <.001 .515
24-29 18.745 3 <.001 .304
30-36 34.688 3 <.001 .356
37-42 12.525 3 .006 .226
Total Clothing 15.813 3 <.001 .130
Footwear

18-23 11.715 3 .008 .264
24-29 15.474 3 <.001 .276
30-36 13.096 3 .004 .219
37-42 23.619 3 <.001 .310
Total Footwear 15.108 3 .002 .130
*Note: "Constant" indicates sub-segments where observed re-
sponses exhibited zero variance, preventing the standard chi -
square calculation.

The degrees of freedom vary across age subgroups within
categories due to structural zeros in the contingency tables,
where certain purchasing pathways were absent for specific
demographic cohorts. These sub-segments are excluded from
the chi-square computation per the 'Constant' condition noted
in Table 3.
At the aggregate level, both cosmetics and electronics
showed statistically significant associations, although the ef-
fect sizes were weaker for electronics.  However, segment-
level analyses revealed moderate to strong effect sizes in spe-
cific age-product combinations, notably within the book seg-
ment for older cohorts, whereas the clothing segment showed
uniform patterns across these groups.

EMÍLIA MADUDOVÁ ET AL.. / PRODUCTION ENGINEERING ARCHIVES 2026, 32(3), 416-429

ARCHIWUM INŻYNIERII PRODUKCJI                                    422

These findings indicate that aggregate -level insignificance
may conceal meaningful within -segment variations in pur-
chasing behavior (see Table 3). While chi-square tests identify
statistically significant associations between demographic
variables and purchasing behavior, effect size measures pro-
vide additional insights into the substantive relevance of these
relationships. Across product categories, the magnitude of the
associations varied considerably by age group, indicating the
heterogeneous strength of demographic effects.
The use of standardized residual analysis (Appendix 1 and
2) provides the necessary granularity to identify which spe-
cific demographic segments drive the aggregate significance
observed in Table 3. This multi -level analytical approach en-
sures that operational decisions in retail engineering are based
on specific behavioral deviations rather than generalized de-
mographic assumptions.
Moderate to strong associations were observed in the book
segment within the selected age cohorts, whereas the drug-
store segment exhibited strong aggregate -level associations,
with high effect sizes across all age groups. In contrast, the
weaker effect sizes in electronics and clothing indicate com-
paratively uniform purchasing behavior across demographic
groups, despite occasional statistical significance. These re-
sults demonstrate that statistical significance alone does not
fully capture the structure of omnichannel purchasing behav-
ior and that effect size patterns are essential for identifying
economically meaningful demographic differences.
In the second stage of the analysis, purchase decision -mak-
ing processes (Appendix 1 and 2; Tables 5 and 6 ) associated
with webrooming and showrooming behaviors were examined
to test hypotheses H0b and H1b. The results reveal distinct age
and gender-based patterns in omnichannel decision pathways.
Younger males (18 -23) exhibited positive deviations toward
showrooming behavior specifically in the alcohol and cosmet-
ics segments, whereas females within the same cohort dis-
played more heterogeneous purchasing pathways. (Appendix
1 and 2). Among respondents aged 30-36, males demonstrated
consistent statistically meaningful deviations favouring
webrooming behavior in categories such as books and cosmet-
ics, while females in this cohort showed significant negative
deviations for the webrooming pathway  (Appendix 2) ; con-
versely, males in this segment demonstrated a significant pos-
itive deviation toward the pure in -store purchasing pathway
(BM/BM). In the oldest cohort (37 -42), gender-specific deci-
sion-making patterns became more pronounced, with females
exhibiting positive deviations toward webrooming and males
toward brick-and-mortar purchases. The results further indi-
cate that webrooming and showrooming behaviors are not
symmetrically distributed across demographic groups. While
both behaviors represent forms of omnichannel integration,
their prevalence systematically differs by age and gender.
Webrooming behavior exhibits a greater demographic con-
centration, particularly among female respondents in younger
and middle-aged cohorts. In contrast, showrooming behavior
appears to be more prevalent among younger male consumers,
suggesting distinct information acquisition and risk mitigation
strategies. This asymmetry indicates that omnichannel inte-
gration should not be treated as a homogeneous construct but
as a set of differentiated behavioral pathways reflecting selec-
tive channel use.
This asymmetry partially contradicts the findings of Matos
et al. (2022), who identified gender-based differences in chan-
nel interaction but did not observe a consistent dominance of
webrooming among female consumers across product catego-
ries. A possible explanation lies in the product mix examined:
the present study includes categories such as cosmetics and
drugstore items, which are traditionally associated with higher
female purchase involvement and where physical inspection
retains experiential value. T his product-demographic interac-
tion may amplify webrooming tendencies among female con-
sumers in ways that are not visible in studies using broader or
less differentiated category sets.
Beyond individual product categories, the results indicate
varying degrees of omnichannel purchasing intensity across
different demographic groups . Certain age -gender combina-
tions exhibit a higher concentration of integrated purchasing
pathways, characterized by frequent transitions between
online and physical touchpoints.
Older consumers (30-42) exhibit the highest concentration
of significant omnichannel deviations, whereas younger co-
horts show selective engagement across fewer channels. Older
consumers tend to integrate these behaviors more selectively,
focusing their omnichannel engagement within specific seg-
ments rather than across their entire purchasing portfolio.
These patterns indicate that the intensity of omnichannel en-
gagement is unevenly distributed across the population, re-
flecting differentiated purchasing strategies  rather than uni-
versal adoption of a single strategy.  The results revealed
statistically significant associations  between demographic
characteristics and omnichannel purchasing behavior across
selected product categories (notably groceries, alcohol, books,
and footwear) and age groups, with additional significant as-
sociations observed in cosmetics, electronics, clothing, and
drugstore categories (Table 3). These findings underscore the
presence of structured demographic heterogeneity in both
channel choice and omnichannel decision-making pathways.
4.1. Predictive analysis of purchase motivators
The multinomial logistic regression (MLR) analysis re-
vealed that age cohorts and channel integration factors signif-
icantly predict consumer purchasing motivators. The models
demonstrated substantial explanatory power, with Nagelkerke
R2 values ranging from 0.501 to 0.513, indicating a strong as-
sociation between demographic structures and behavioral out-
comes (Table 4) . These values are notably high relative to
comparable behavioral studies in omnichannel retailing,
where Nagelkerke R² coefficients typically range between
0.20 and 0.35, suggesting that the combination of demo-
graphic cohort membership and channel integrati on prefer-
ences captures a substantial proportion of the variance in con-
sumer purchase motivators.
Specifically, the model for 'Influence of friends' achieved
the highest predictive accuracy (Nagelkerke R 2 =0.513),
where the age cohort emerged as a critical significant predictor
(p<0.001). Regression coefficients indicate that as consumers

EMÍLIA MADUDOVÁ ET AL.. / PRODUCTION ENGINEERING ARCHIVES 2026, 32(3), 416-429

 423                                                                      ARCHIWUM INŻYNIERII PRODUKCJI

move into older cohorts (24 -36 years), they rely significantly
less on peer consultation compared to the youngest group (18-
23 years), exhibiting a shift toward autonomous decision -
making (Table 4).
Table 4. Multinomial Logistic Regression Analysis of Purchase
Motivators (Source: Authors)
Dependent
Variable:
Motivator

R2
Sig.
Predictors
Pearson
(χ2)
df p-value
Influence
of friends
0.513 Age
cohort
39.740 12 <.001

Online
content
tracking
12.490 4 .014

Social
media
to e-shop
links
17.704 4 .001

Discount
code
search
9.936 4 .042
Product
aesthetics
0.501 Age
cohort
32.411 12 <.001

Social
media
 to e-shop
links
11.558 4 .021

Discount
code
search
18.230 4 .001
Influence
of
influencers
0.508 Age
cohort
28.920 12 .004

Social
media to
 e-shop
links
13.035 4 .011

Furthermore, the likelihood of being motivated by 'Product
aesthetics' (Nagelkerke R2 =0.501) is heavily influenced by the
consumer's demand for seamless channel integration, specifi-
cally the presence of direct social media -to-e-shop links
(p=0.021). These findings mathematically confirm that omni-
channel purchasing pathways are not random c hoices but are
structured by a combination of generational traits and tech-
nical channel capabilities (Table 4)
4.2. Discussion
This study provides empirical evidence that omnichannel
purchasing behavior reflects structured decision-making path-
ways rather than simple substitutions between online and
physical retail channels.  These findings are consistent with
prior research emphasizing that consumer behavior in omni-
channel environments follows a multi -stage decision-making
process rather than a binary channel choice (Pires et al., 2022;
Rodríguez-Torrico et al., 2020a; Rodrígu ez-Torrico et al.,
2020b). Our results extend this unders tanding by quantifying
how specific demand signals  such as the 'Social media  to
e-shop links' identified in the MLR model and illustrated in
the decision sequences of Figure 1 function as critical predic-
tors of these pathways.
This supports the interpretation of omnichannel purchasing
as an allocation mechanism shaped by information costs, per-
ceived risk, and channel accessibility. The predictive analysis
(Table 4) and the residual patterns observed in Appendix 1 and
2 demonstrate that these allocation strategies are not uniform;
for instance, the declining reliance on peer consultation among
older cohorts (Generation Y) correlates with their preference
for in -store transactions in routine segments like groceries.
Consequently, t he findings demonstrate that age and gender
significantly shape how consumers distribute purchasing ac-
tivities across channels, supporting the interpretation of omni-
channel retailing as an economically organized system of
complementary distribution mechanisms that dictate the oper-
ational requirements of modern retail engineering ecosystems.
The regression output further strengthens the observation
that younger consumers (Generation Z) operate in a more so-
cially and digitally integrated ecosystem.  The high predictive
value of 'Social media-to-e-shop links' in the MLR model cor-
relates with the observed webrooming pathways, where digital
information acquisition is the primary driver  of transactions.
In contrast, the declining reliance on external influences
among older cohorts (Generation Y) aligns with their  prefer-
ence for in-store purchasing in routine segments such as gro-
ceries, where experiential validation outweighs digital persua-
sion. These results support the conceptualization of
omnichannel retail not as a replacement for traditional meth-
ods but as a multi -stage allocation process driven by demo-
graphic-specific rationalities.
It is noteworthy, however, that despite their high digital en-
gagement, Generation Z consumers did not exhibit statisti-
cally significant preferences for purely online transaction
completion across most product categories. This finding nu-
ances the prevailing narrative of a uniform digital-first gener-
ation and aligns more closely with Chang and Chen (2022),
who demonstrated that Generation Z follows hybrid shopper
journeys rather than exclusively digital ones. Being digitally
fluent does not mean buying exclus ively online. For Genera-
tion Z, physical stores still serve a clear purpose mainly for
checking products before buying elsewhere.
The high predictive value of 'Social media to -e-shop links'
(p = 0.021) suggests that digital touchpoints act as primary
catalysts for non-linear demand signals. For production engi-
neering systems, this implies that social media engagement
data can serve a s an early -stage proxy for warehousing and
last-mile delivery requirements, bridging the gap between dig-
ital marketing and supply chain synchronization.
From an economic perspective, these findings reinforce the
view that digital and physical channels perform complemen-
tary functions in the consumer decision-making process. Dig-
ital channels primarily reduce search and information costs,
whereas physical retail environments provide experiential ver-
ification and risk mitigation.  Prior studies confirm that con-
sumers with a higher tendency toward omnichannel behavior
process information differently and exhibit distinct response

EMÍLIA MADUDOVÁ ET AL.. / PRODUCTION ENGINEERING ARCHIVES 2026, 32(3), 416-429

ARCHIWUM INŻYNIERII PRODUKCJI                                    424

patterns, indicating that omnichannel integration reflects ra-
tional decision-making under heterogeneous constraints rather
than inconsistent consumer behavior (Tyrväinen & Kar-
jaluoto, 2019).
The findings reveal that individuals aged 24 -29 exhibit
mixed purchasing patterns ; with a tendency toward online
completion in selected categories (e.g., electronics, cosmet-
ics), but not uniformly across all product segments. This trend
indicates that younger consumers perceive digital channels as
offering lower transaction costs and greater convenience at the
point of purchase. Conversely, individuals aged 30-42 demon-
strate a sustained preference for brick -and-mortar stores in
routine product categories such as groceries, reflecting the
continued economic role of physical retail in experiential val-
idation and risk mitigation. In the grocery segment, older con-
sumers (37 -42) showed a tendency toward brick -and-mortar
purchasing, yet this preference did not reach statistical signif-
icance (residual 1.4 < 1.96), indicating a balanced channel al-
location rather than a clear dominance of either channel. T his
observation contrasts with previous studies that suggest a gen-
eralized shift towards online grocery shopping, highlighting
the persistence of product - and context-specific channel allo-
cation strategies.
Older consumers appear to stick with familiar purchasing
habits visiting physical stores even when digital alternatives
are available. This aligns with the concept of status quo bias,
where switching to a new channel carries psychological costs
that outwei gh the perceived convenience. This interpretation
extends the transaction cost framework applied by Wieland
(2023), suggesting that for older cohorts, the perceived costs
of digital adoption  including uncertainty, effort, and loss of
interpersonal interacti on outweigh the convenience benefits
that drive younger consumers toward online completion. Re-
tailers targeting this segment should therefore prioritize seam-
less in-store experiences rather than aggressive digital migra-
tion strategies.
Gender-based differences further contribute to the heteroge-
neity of omnichannel decision-making. The role of perceived
value further elucidates this diversity. Empirical evidence sug-
gests that the effectiveness of channel integration depends on
consumers’ ability to transition seamlessly across touchpoints
and perceive consistency across channels (Rakhmanita et al.,
2023). Consistent with the literature, the results of the present
study indicate that omnichannel purchasing pathways differ
systematically acr oss demographic groups, reflecting varia-
tions in perceived benefits, decision costs, and channel famil-
iarity rather than uniform adoption patterns.
Webrooming behavior appears in selected categories among
younger female consumers, particularly cosmetics, but is not
uniformly dominant across all product segments. Males in the
30-36 age group exhibit a greater tendency toward webroom-
ing or in -store-oriented purchasing strategies.  These patterns
suggest that omnichannel pathways are shaped not only by ac-
cess to digital technologies but also by demographic differ-
ences in information processing, risk perception, and purchas-
ing habits.
The results show that a simple online -offline distinction is
insufficient to capture how consumers actually behave in om-
nichannel environments.
 Instead, purchasing decisions emerge from structured path-
ways in which digital and physical channels perform comple-
mentary roles, depending on demographic characteristics and
product categories. This highlights the importance of channel
complementarity rather than channel substitution in under-
standing contemporary consumer behavior within a multi -
stage economic framework.
From an economic standpoint, the observed purchasing
pathways indicate that consumers actively balance efficiency
and risk when navigating omnichannel retail environments to
maximize their utility.  Younger consumers’ preference for
digitally completed transactions suggests lower perceived
transaction costs and higher confidence in online purchasing
mechanisms, even when physical stores are used for prelimi-
nary information gatherings. This behavior is consistent with
economic models of rational choice under reduced uncertainty
and increased digital literacy.
In contrast, the increased reliance on traditional brick -and-
mortar purchasing among older consumers in specific product
categories can be attributed to the greater perceived benefits
of physical inspection and interpersonal interactions.  These
findings support the interpretation that channel choice is influ-
enced by diverse cost -benefit structures rather than the uni-
form adoption of technology.  Therefore, omnichannel retail
systems should be conceptualized as environments in which
different channels specialize in distinct economic functions.
The presence of webrooming and showrooming behaviors
further illustrates the complementary relationship between
online and offline channels. Previous research has also high-
lighted the importance of digital communication and market-
ing channels in shaping early stage purchasing decisions. Dig-
ital tools influence consumer expectations and information
acquisition, particularly at the beginning of the decision-mak-
ing process, even when the final transactions are completed
offline (Ravindran and Sathyamoorthi, 20 19; Ulker-Demirel,
2019). This aligns with the empirical evidence of this study,
which shows that online channels frequently dominate the in-
formation search phase of omnichannel purchasing pathways.
Rather than signaling inefficiencies or consumer confusion,
these behaviors represent economically rational strategies that
allow consumers to optimize information acquisition and
transaction execution across all channels.  Such strategies re-
duce overall decision-making costs while preserving the flex-
ibility of the purchasing process.
These results add to existing evidence that online and offline
channels work alongside each other rather than competing for
the same customers. From a retail economics perspective, this
implies that investments in digital infrastructure do not dimin-
ish the value of physical retail assets but may enhance their
strategic role within integrated distribution systems.
Compared to existing research, this study contributes to om-
nichannel literature by integrating purchasing locations and
decision-making pathways within a unified analytical frame-
work. By focusing on consumers rather than customers, the
analysis acknowledges that purchasing decisions may involve

EMÍLIA MADUDOVÁ ET AL.. / PRODUCTION ENGINEERING ARCHIVES 2026, 32(3), 416-429

 425                                                                      ARCHIWUM INŻYNIERII PRODUKCJI

transactions made for others or across multiple usage contexts,
offering a broader interpretation of demand allocation in om-
nichannel retail.
This study has several limitations. The exclusion of income-
related variables reflects respondents’ reluctance to disclose
financial information, which may limit direct comparability
with markets characterized by higher -income transparency.
Nevertheless, prior evidence indicates that Slovak consumers
exhibit high sensitivity, suggesting that the observed purchas-
ing patterns remain informative for understanding omnichan-
nel decision-making, which is driven primarily by value con-
siderations rather than income segmentation.
Figure 1 provides a synthesized representation of omnichan-
nel purchasing pathways across age groups and product cate-
gories, supporting the empirical interpretation of omnichannel
behavior as a structured-allocative process. Although consum-
ers aged 24-29 frequently engage with online channels during
the information search phase, their preference for completing
transactions purely online was not statistically significant
across most product categories, suggesting a more complex
and selective pattern of channel integration than a simple dig-
ital-first strategy.
In contrast, older consumers exhibit a stronger reliance on
in-store purchasing pathways in selected categories, notably
groceries, reinforcing the continued economic role of brick -
and-mortar retail environments in omnichannel systems. Gen-
der-based differences are also apparent, with webrooming be-
havior being more prevalent among female consumers in
younger cohorts, while males in middle age groups (30 -42)
exhibited significant negative deviations for showrooming
pathways in categories such as groceries and alcohol.
Overall, Figure 1 visually reinforces the interpretation that
omnichannel integration does not imply the replacement of
physical retail with digital channels.  Instead, online and of-
fline touchpoints operate as complementary elements within
consumer decision -making pathways, consistent with the
study’s broader economic framing of omnichannel retailing
behavior.

Fig. 1. Omnichannel Purchasing Pathways across Age Groups and
Product Categories, incorporating social media to e-shop links as
critical path drivers. (Source: Authors)
These findings are particularly relevant for retail systems
that operate under cost pressures and channel coordination
constraints. The figure presents the dominant purchasing path-
ways (webrooming, showrooming, in -store-, and online pur-
chasing) identified through a standardized residual analysis.
Product categories are displayed on the vertical axis, while age
groups (18-23, 24-29, 30-36, 37-42) separated by gender are
shown on the horizontal axis. Colored markers indicate statis-
tically significant deviations from the expected frequencies,
illustrating demographic heterogeneity in channel selection
and pathway structure within omnichannel purchasing behav-
ior.
These findings partially corroborate and extend the work of
Moliner and Tortosa -Edo (2024), who demonstrated that
women and younger consumers report higher levels of e -sat-
isfaction throughout the omnichannel consumer journey.
Whereas their multi -rooming framework captures the broad,
fluid oscillation between touchpoints, the present study pro-
vides granular empirical evidence that this oscillation is not
random but is structured into distinct, demographically differ-
entiated pathway sequences (webrooming and showrooming),
with specific behavioral asymmetries by age and gender. This
distinction advances the theoretical understanding of multi -
rooming by decomposing it into operationally measurable
sub-pathways relevant for retail engineering and inventory
management.
5. Summary and conclusion
This study establishes that omnichannel purchasing is a
structured economic decision -making process rather than a
random or binary choice between digital and physical chan-
nels. By analyzing data from 889 consumers, the research
demonstrates that these "purchasing pathways" are systemati-
cally dic tated by demographic factors, particularly age and
gender.
Primary and secondary research frame omnichannel behav-
ior as an allocation mechanism where consumers distribute ac-
tivities such as information search, evaluation, and transaction
to optimize information acquisition and reduce uncertainty.
Younger consumers (Generation Z) engage extensively with
digital touchpoints yet demonstrate selective rather than ex-
clusive online purchasing, consistent with hybrid channel
strategies identified in the MLR analysis.
Older consumers (Generation Y) rely more consistently on
physical retail for necessity-based categories, reflecting higher
psychological switching costs and the experiential value of in-
store interaction.
The study identifies that webrooming (browsing online and
buying in -store) and showrooming (examining in -store and
buying online) are not symmetrically distributed; webrooming
is more pronounced among female consumers in younger and
middle-aged cohorts. Showrooming is more prevalent among
younger male consumers, suggesting distinct strategies for in-
formation acquisition and risk management.
Among the oldest cohort (37 -42), gender patterns become
even more distinct, with females favoring webrooming and
males favoring brick-and-mortar transactions

EMÍLIA MADUDOVÁ ET AL.. / PRODUCTION ENGINEERING ARCHIVES 2026, 32(3), 416-429

ARCHIWUM INŻYNIERII PRODUKCJI                                    426

Multinomial logistic regression (MLR) confirms that these
pathways are structured by generational traits and technical
channel capabilities.
 The model for the "Influence of friends" showed the highest
predictive accuracy (R 2=0.513), revealing that as consumers
age, they rely significantly less on peer consultation.
  The motivation of "Product aesthetics" (R 2=0.501) was
heavily influenced by the presence of direct links between so-
cial media and e-shops, highlighting how seamless integration
drives the purchasing journeys of younger digitally integrated
cohorts.
For production and supply chain managers, these behavioral
differences are not just a marketing concern  they directly af-
fect how inventory should be planned and allocated. They gen-
erate nonlinear demand signals that dictate how physical in-
ventory must be allocated across distribution centers versus
storefronts to prevent stockouts and minimize holding costs.
By conceptualizing omnichannel behavior as a structured al-
location process, this study provides the necessary "architec-
tural insight" to optimize modern retail supply chains and ful-
fill systemic requirements for operational resilience.
From a practical standpoint, the demographic -specific pur-
chasing pathways identified in this study carry direct implica-
tions for retail operations and inventory management. Retail-
ers serving female consumers in the 24 -29 and 30 -36 age
cohorts in categories such as cosmetics and drugstore items
should anticipate elevated webrooming demand, meaning that
physical store inventory must be maintained at levels suffi-
cient to capture transactions initiated through digital channels.
Conversely, the showrooming tende ncy observed among
younger male consumers (18 -23) in categories such as elec-
tronics and alcohol suggests that online fulfilment capacity
and competitive pricing transparency are critical conversion
factors for this segment. Furthermore, the predictive signifi-
cance of social media -to-e-shop links ident ified in the MLR
analysis suggests that social media engagement metrics can
serve as leading indicators of short -term demand shifts, ena-
bling more responsive inventory allocation and last -mile de-
livery planning. For production engineering systems operating
under cost and capacity constraints, these findings imply that
demographic segmentation should be integrated not only into
marketing strategy but also into demand forecasting models
and distribution network design. Building the same omnichan-
nel system for all consumer segments is unlikely to work well,
given how differently age and gender groups behave across
product categories.
Overall, this study shows that omnichannel behavior cannot
be adequately captured using a binary online -offline frame-
work. The results of this study provide further empirical sup-
port for conceptualizing omnichannel purchasing as a struc-
tured and economically rational decision-making process. The
observed purchasing pathways are consistent with prior find-
ings, indicating that consumers strategically integrate online
and offline channels to optimize information acquisition, re-
duce uncertainty, and enhance perceived value throughout the
purchasing process (Pires et al., 2022; Rodríguez -Torrico et
al., 2020b).  Omnichannel behavior, rather than indicating a
substitution of channels, represents a complementary distribu-
tion of decision-making activities across retail channels. Pur-
chasing decisions emerge from dynamic, demographic -spe-
cific pathways, where online and physical channels function
as complementary components within the retail system. Treat-
ing omnichannel purchasing as a demand allocation problem
rather than simply a channel choice opens up more useful
ways to study and design retail systems.
5.1. Limitations and future research
This study has several limitations. Although the sample size
of 889 respondents provides a solid empirical basis for cate-
gorical analysis, future research could extend the geographical
scope of this study to enhance its generalizability.  Addition-
ally, the exclusion of income-related variables limits the abil-
ity to assess purchasing behavior from a detailed socioeco-
nomic perspective. Nevertheless, prior evidence indicates that
Slovak consumers exhibit high price sensitivity, suggesting
that the observed purc hasing patterns remain informative for
understanding value-driven omnichannel decision making.
Another limitation of this study relates to its cross-sectional
design, which captures purchasing behavior at a single point
in time. Omnichannel retail environments have evolved rap-
idly in response to technological innovations, platform devel-
opment, and changing consumer expectations.  Consequently,
longitudinal data can provide deeper insights into how pur-
chasing pathways adapt over time and in response to market -
level changes.  These findings also align with previous evi-
dence suggesting that omnichannel co nsumers are not a ho-
mogeneous group and that variations in channel usage reflect
differentiated strategies rather than inconsistent behavior
(Viejo-Fernández 2021).
By confirming that demographic characteristics systemati-
cally shape omnichannel purchasing pathways, this study ex-
tends the existing literature and contributes to a more nuanced
understanding of omnichannel retailing as an allocation pro-
cess embedded withi n contemporary digital economies (Ma-
dudova and Corejova, 2023; Rakhmanita et al., 2023).  Fur-
thermore, reliance on self-reported survey data may introduce
recall bias or subjective interpretation of purchasing behavior.
Future research could complement surv ey-based approaches
with behavioral or transactional data to enhance the measure-
ment accuracy and further validate the observed patterns.
A further limitation concerns the sampling procedure. As
data were collected through social media groups and univer-
sity-affiliated networks, the sample may systematically over -
represent younger, digitally proficient consumers. This re-
cruitment strategy, while effective for reaching the target de-
mographic of Generations Y and Z, may limit the generaliza-
bility of the findings to older consumer segmen ts or
populations with lower levels of digital engagement. Future
research should consider probability-based sampling methods
or complementary data sources to mitigate this potential bias.
Acknowledgements
This paper is written under the project VV-MVP-24-0375 and
VEGA 1/0333/24

EMÍLIA MADUDOVÁ ET AL.. / PRODUCTION ENGINEERING ARCHIVES 2026, 32(3), 416-429

 427                                                                      ARCHIWUM INŻYNIERII PRODUKCJI

Reference
Acquila-Natale, E., Iglesias-Pradas, S., 2021. A matter of value? Predicting
channel preference and multichannel behaviors in retail. Technological
Forecasting and Social Change, 162, 120401. DOI: 10.1016/j.tech-
fore.2020.120401
Aflaki, A., Feldman, P., Swinney, R., 2020. Becoming Strategic: Endogenous
Consumer Time Preferences and Multi -Period Pricing. Operations Re-
search, 68(4): 1116-1131. DOI: 10.1287/opre.2019.1937
Alexander, B., & Kent, A. (2022). Changes in technology-enabled omnichan-
nel customer experiences in -store. Journal of Retailing and Consumer
Services, 65, 102338. DOI: 10.1016/j.jretconser.2020.102338
Ariannezhad, M., Jullien, S., Nauts, P., Fang, M., Schelter, S., de Rijke, M.,
2021. Understanding Multi-Channel Customer Behavior in Retail.  Pro-
ceedings of the 30th ACM International Conference on Information &
Knowledge Management, 2867-2871. DOI: 10.1145/3459637.3482208
Beregovskaya, T.A., Grishaeva, S.A., 2020. Generation Z: Consumer Behav-
ior in Digital Ecosystem.  Vestnik Universiteta, (1), 92 -99. DOI:
10.26425/1816-4277-2020-1-92-99
Burnasheva, R., 2019. The Role of Omnichannel Experience in Luxury Fash-
ion Brands. Journal of Textile Science & Fashion Technology, 2(2). DOI:
10.33552/JTSFT.2019.02.000534
Chang, W. -L., Chen, L. -M., 2022. Analyzing the Omni -Channel Shopper
Journey Configuration of Generations Y and Z. Journal of Organizational
and End User Computing, 33(6), 1-18. DOI: 10.4018/JOEUC.293273
Chen, T.Y., Yeh, T.L., Wu, H.L., Deng, S., 2023. Effect of channel integration
quality on consumer responses within omni -channel retailing. Asia Pa-
cific Journal of Marketing and Logistics, 35(1), 149 -173. DOI:
10.1108/APJML-04-2021-0270
Gao, W., Fan, H., 2021. Omni-Channel Customer Experience (In)Consistency
and Service Success: A Study Based on Polynomial Regression Analysis.
Journal of Theoretical and Applied Electronic Commerce Research,
16(6), 1997-2013. DOI: 10.3390/jtaer16060112
Gasparin, I., Slongo, L.A., 2023. Omnichannel as a Consumer-Based Market-
ing Strategy. Revista de Administração Contemporânea, 27(4).  DOI:
10.1590/1982-7849rac2023220327.en
Hole, Y., Pawar, S., Khedkar, E.B., 2019. Omni Channel Retailing: An Op-
portunity and Challenges in the Indian Market. Journal of Physics: Con-
ference Series, 1362(1), 012121.  DOI: 10.1088/1742 -6596/1362/1/
012121
Iglesias-Pradas, S., Acquila-Natale, E., Del-Río-Carazo, L., 2022. Omnichan-
nel retailing: a tale of three sectors. Economic Research -Ekonomska
Istraživanja, 35(1), 3305-3336. DOI: 10.1080/1331677X.2021.1991825
Joshi, S., Sharma, M., Bisht, P., Singh, S., 2021. Explaining the Factors Influ-
encing Consumer Perception, Adoption Readiness, and Perceived Use-
fulness toward Digital Transactions: Online Retailing Experience of Mil-
lennials in India. Journal of Operations and Strategic Planning, 4(2), 202-
223. DOI: 10.1177/2516600X211052649
Kang, J., Majer, M., Kim, H.-J., 2019. Empirical Study of Omnichannel Pur-
chasing Pattern with Real Customer Data from Health and Lifestyle Com-
pany. Sustainability, 11(24), 7185. DOI: 10.3390/su11247185
Kao, Y.-T., Lin, H. -W., Qiu, D. -Y., 2021. Implementation of Offline Con-
sumer Behavior Tracking. International Journal of Pattern Recognition
and Artificial Intelligence, 35(09), 2150028.  DOI: 10.1142/
S0218001421500282
Liu, J., 2021. Single -online-channel Retailer’s Pricing and Service Decision
in Showroom Omnichannel Retailing. 2021 2nd International Conference
on Computer Science and Management Technology (ICCSMT), 617 -
622. DOI: 10.1109/ICCSMT54525.2021.00121
Liu, L., Feng, L., Xu, B., Deng, W., 2020a. Operation strategies for an omni-
channel supply chain: Who is better off taking on the online channel and
offline service? Electronic Commerce Research and Applications, 39,
100918. DOI: 10.1016/j.elerap.2019.100918
Liu, Z., Lu, L., Qi, X., 2020 b. The showrooming effect on integrated dual
channels. Journal of the Operational Research Society, 71(9), 1347-1356.
DOI: 10.1080/01605682.2019.1605470
Loupiac, P., Goudey, A., 2019. How website browsing impacts expectations
of store features. International Journal of Retail & Distribution Manage-
ment, 48(1), 92-108. DOI: 10.1108/IJRDM-07-2018-0146
Madlenak, R., Chinoracky, R., Stalmasekova, N., Madlenakova, L., 2023. In-
vestigating the Effect of Outdoor Advertising on Consumer Decisions:
An Eye-Tracking and A/B Testing Study of Car Drivers’ Perception. Ap-
plied Sciences, 13(11), 6808. DOI: 10.3390/app13116808
Madlenak, R., Madlenakova, L., 2020. Multi-criteria Evaluation of E -shop
Delivery Methods from the Customer Perspective.  Transport Problems,
15(1), 5-14. DOI: 10.21307/tp-2020-001
Madudova, E., Corejova, T., 2024. The Issue of Measuring Household Con-
sumption Expenditure. Economies, 12(1), 9. DOI: 10.3390/econo-
mies12010009
Maggioni, I., Sands, S.J., Ferraro, C.R., Pallant, J.I., Pallant, J.L., Shedd, L.,
Tojib, D., 2020. Consumer cross -channel behaviour: is it always
planned? International Journal of Retail & Distribution Management,
48(12), 1357-1375. DOI: 10.1108/IJRDM-03-2020-0103
Matos, S., Durão, M., Magano, J., 2022. Omnichannel Shopping Experience:
An Exploratory Study on a Generation Z Sample. Percursos & Ideias, 1-
12. DOI: 10.56123/percursos.2022.n12.1
Moliner, M.A., Tortosa-Edo, V., 2024. Multirooming: generating e-satisfac-
tion throughout omnichannel consumer journey design and online cus-
tomer experience. Journal of Research in Interactive Marketing, 18(3),
349-369. DOI: 10.1108/JRIM-05-2023-0149
Öztürk, S., Okumuş, A., 2018. Chapter 6: The Birth of Omni -Channel Mar-
keting and New Dynamics of Consumers’ Approach to Retail Channels.
Marketing Management in Turkey, 247 -272. Emerald Publishing Lim-
ited, Bingley DOI: 10.1108/978-1-78714-557-320181018
Pires, P.B., Santos, J.D., Brito, P.Q. de, Marques, D.N., 2022. Connecting
Digital Channels to Consumers’ Purchase Decision -Making Process in
Online Stores. Sustainability, 14(21), 14392. DOI: 10.3390/su142114392
Rakhmanita, A., Hurriyati, R., Disman, D., Hendrayati, H., Susilawati, E.,
2023. The driver of purchase intentions in omnichannel retail: Perceived
value examination. Journal of Eastern European and Central Asian Re-
search (JEECAR), 10(4), 650-658. DOI: 10.15549/jeecar.v10i4.1360
Ravindran, K., Sathyamoorthi, V., 2019. Impact of Digital Marketing on Con-
sumer Purchase Decision. International Journal of Innovative Technol-
ogy and Exploring Engineering, 9(2S2), 453 -455. DOI: 10.35940/iji-
tee.B1214.1292S219
Rodríguez-Torrico, P., San -Martín, S., San José Cabezudo, R., 2020 a. The
role of omnichannel tendency in digital information processing. Online
Information Review, 44(7), 1347 -1367. DOI: 10.1108/OIR -08-2019-
0272
Rodríguez-Torrico, P., Trabold Apadula, L., San-Martín, S., San José-Cabe-
zudo,R, 2020b. Have an omnichannel seamless interaction experience!
Dimensions and effect on consumer satisfaction. Journal of Marketing
Management, 36(17 -18), 1731 -1761. DOI: 10.1080/0267257X.
2020.1801798
Rukmana, W., Susyanto, H.A., Murwani, I.A., 2019. The Determinant Factors
of Omnichannel Service Adoption in Jakarta. Asian Journal of Research
in Computer Science, 1-12. DOI: 10.9734/ajrcos/2019/v3i430097
Shih, S.-F., Li, C.-Y., Lin, M.-C., 2019. The Diversified Insurance Marketing
Channels Driven Development of Consumer Behaviour. Proceedings of
the 2019 10th International Conference on E-business, Management and
Economics, 253-258. DOI: 10.1145/3345035.3345040
Singh, S., Srivastava, S., 2019. Engaging consumers in multichannel online
retail environment. Journal of Modelling in Management, 14(1), 49 -76.
DOI: 10.1108/JM2-09-2017-0098
Strenitzerová, M., Gaňa, J., 2018. Customer Satisfaction and Loyalty as a Part
of Customer -Based Corporate Sustainability in the Sector of Mobile
Communications Services. Sustainability, 10(5), 1657. DOI: 10.3390/
su10051657
Sun, Y., Yang, C., Shen, X.-L., Wang, N., 2020. When digitalized customers
meet digitalized services: A digitalized social cognitive perspective of
omnichannel service usage. International Journal of Information Man-
agement, 54, 102200. DOI: 10.1016/j.ijinfomgt.2020.102200
Țoniș-Bucea-Manea, R., Blăjină, O., 2019. Factors Influencing Online Con-
sumer Behavior in the Era of IoT. Materials Science Forum, 957, 81-89.
DOI: 10.4028/www.scientific.net/MSF.957.81
Tyrväinen, O., Karjaluoto, H., 2019. Omnichannel experience: Towards suc-
cessful channel integration in retail. Journal of Customer Behaviour,
18(1), 17-34. DOI: 10.1362/147539219X15633616548498
Ulker-Demirel, E. (2019).  The Features of New Communication Channels
and Digital Marketing, 302 -313. DOI: 10.4018/978 -1-5225-9790-
2.ch026
Viejo-Fernández, N., 2021. Retailers: All Omni-Shoppers Are Not the Same.
DOI: 10.3233/FAIA210226

EMÍLIA MADUDOVÁ ET AL.. / PRODUCTION ENGINEERING ARCHIVES 2026, 32(3), 416-429

ARCHIWUM INŻYNIERII PRODUKCJI                                    428

Wang, X., Wong, Y.D., Shi, W., Yuen, K.F., 2024. An investigation on con-
sumers’ preferences for parcel deliveries: applying consumer logistics in
omni-channel shopping. The International Journal of Logistics Manage-
ment, 35(2), 557-576. DOI: 10.1108/IJLM-07-2022-0288
Wieland, T., 2021. Identifying the Determinants of Store Choice in a Multi -
Channel Environment: A Hurdle Model Approach. Papers in Applied Ge-
ography, 7(4), 343-371. DOI: 10.1080/23754931.2021.1895875
Wieland, T., 2023. A Micro‐Econometric Store Choice Model Incorporating
Multi‐ and Omni‐Channel Shopping: The Case of Furniture Retailing in
Germany. Geographical Analysis, 55(1), 3-30. DOI: 10.1111/gean.12308
Zafar, S., Badghish, S., Yaqub, R. M. S., & Yaqub, M. Z. (2023). The Agency
of Consumer Value and Behavioral Reasoning Patterns in Shaping
Webrooming Behaviors in Omnichannel Retail Environments. Sustaina-
bility, 15(20), 14852. https://doi.org/10.3390/su152014852
Zhang, Z., 2023. Check and Balance Overspending in Average American
Household Consumption. Highlights in Business, Economics and Man-
agement, 7, 1-7. DOI: 10.54097/hbem.v7i.6808
Zhao, W., Deng, N., 2020. Examining the Channel Choice of Experience-Ori-
ented Customers in Omni-Channel Retailing. International Journal of In-
formation Systems in the Service Sector, 12(1), 16 -27. DOI:
10.4018/IJISSS.2020010102
Zhao, Y., Zhao, X., Liu, Y., 2022. Exploring the Impact of Online and Offline
Channel Advantages on Brand Relationship Performance: The Mediating
Role of Consumer Perceived Value. Behavioral Sciences, 13(1), 16. DOI:
10.3390/bs13010016

Appendix 1
Table 5. Standardized Residual Analysis of Purchasing Pathways by Segment, Age, and Gender (Source: Authors)
Category / Age Gender Online/ Online Online / BM ** BM / Online *** BM / BM
Groceries

18-23 Male — 0.8 — -0.3
Female — -0.8 — 0.3
24-29 Male — -1.8 -1.8 0.7
Female — -1.8 -1.8 0.7
30-36 Male -1.9 -0.1 — 0.3
Female 1.9 0.1 — -0.3
37-42 Male -2.7 — -2.7 1.4
Female 2.8 — 2.8 -1.4
Total Male -3.3 1.3 -1.2 0.4
Female 3.4 -1.4 1.2 -0.4

Alcohol

18-23 Male -0.2 — 2.3 0.7
Female 2.0 — -2.5 0.7
24-29 Male 1.0 1.8 -0.7 —
Female -1.0 -1.8 0.7 —
30-36 Male 1.8 -1.1 -3.3 1.0
Female -1.8 1.2 3.4 -1.1
37-42 Male -0.1 1.8 -3.3 0.8
Female 0.1 -1.8 3.4 -0.8
Total Male 0.5 0.5 -2.1 0.3
Female -0.5 -0.5 2.1 -0.4

Drugstore

18-23 Male -0.2 -2.1 -1.9 1.6
Female 0.2 2.3 2.1 -1.7
24-29 Male -0.1 -3.2 -0.1 2.0
Female 0.1 3.3 0.1 -2.0
30-36 Male -3.3 -0.9 -0.1 1.5
Female 3.4 1.0 0.1 -1.5
37-42 Male -1.9 -1.2 -1.2 1.1
Female 2.0 1.2 1.2 -1.1
Total Male -2.8 -3.8 -1.4 3.0
Female 2.9 3.9 1.4 -3.1
*Note: BM = Brick-and-Mortar retail environment. Standardized residuals exceeding ±1.96 (indicate statistically significant deviations from the expected
frequencies at the α=0.05 level.
** Webrooming
*** Showrooming

EMÍLIA MADUDOVÁ ET AL.. / PRODUCTION ENGINEERING ARCHIVES 2026, 32(3), 416-429

 429                                                                      ARCHIWUM INŻYNIERII PRODUKCJI

Appendix 2
Table 6. Standardized Residual Analysis of Purchasing Pathways (Continued) (Source: Authors)
Category / Age Gender Online/ Online Online / BM ** BM / Online *** BM / BM
Cosmetics
18-23 Male -1.3 -1.3 2.1 -0.5
 Female 1.4 1.4 -2.3 0.5
24-29 Male 1.0 -3.6 -0.2 2.3
 Female -1.0 3.8 0.2 -2.4
30-36 Male -0.8 2.4 -1.3 0.3
 Female 0.8 -2.4 1.4 -0.3
37-42 Male -2.8 -1.6 0.6 2.8
 Female 2.8 1.7 -0.6 -2.8
Total Male -2.3 -2.3 0.6 2.5
 Female 2.4 2.4 -0.6 -2.6
Books
18-23 Male 0.0 -0.4 -0.3 0.8
 Female 0.0 0.4 0.3 -0.8
24-29 Male 0.3 -2.0 1.3 -0.2
 Female -0.3 2.0 -1.4 0.2
30-36 Male -3.3 4.4 -0.7 3.1
 Female 3.4 -4.5 0.7 -3.2
37-42 Male -3.0 -1.2 -0.8 4.1
 Female 3.0 1.2 0.8 -4.2
Total Male -3.1 0.9 -0.4 4.1
 Female 3.2 -1.0 0.4 -4.3
Electronic
18-23 Male 1.6 1.1 -1.6 -1.9
 Female -1.8 -1.2 1.8 2.1
24-29 Male 1.0 -2.3 2.3 -0.9
 Female -1.0 2.3 -2.4 0.9
30-36 Male -4.1 1.2 2.4 -0.1
 Female 4.2 -1.2 -2.5 0.1
37-42 Male -1.2 1.0 -0.1 -0.2
 Female 1.2 -1.0 0.1 0.2
Total Male -1.4 0.6 1.6 -1.1
 Female 1.4 -0.6 -1.7 1.1
*Note: BM = Brick-and-Mortar. Standardized residuals exceeding ±1.96   indicate statistically significant deviations at α=0.05.
** Webrooming
*** Showrooming
