---
title: 'Invited review: Using data from sensors and other precision farming technologies to enhance the
  sustainability of dairy cattle breeding programs'
url: https://doi.org/10.3168/jds.2025-26554
category: brand
subcategory: review
date: 2025-08
venue: Journal of Dairy Science
authors:
- Luiz F. Brito
- B. Heringstad
- Ilka Christine Klaas
source: openalex-oa
pdf_url: https://orbi.uliege.be/bitstream/2268/343643/1/BRITO_SENSOR.pdf
pages: 28
chars: 168557
fetched_at: '2026-11-08T17:43:09+00:00'
kb_version: 1
---

# Invited review: Using data from sensors and other precision farming technologies to enhance the sustainability of dairy cattle breeding programs

10447
ABSTRACT
The increased uptake of sensor technologies and preci-
sion farming tools for the dairy cattle sector is enabling
real-time monitoring of animal health, welfare, and
productivity. These digital advancements provide high-
frequency, objective, and large-scale phenotypic data for
breeding purposes. This review explores the potential
of sensor-derived data to improve genetic and genomic
evaluations in dairy cattle and outlines key challenges,
opportunities, and approaches associated with their im-
plementation. While these data streams have great poten-
tial for genetic evaluations, their integration into national
and international breeding programs remains limited due
to fragmentation across sensor brands, lack of standard-
ization, and challenges related to data accessibility, data
access and portability rights, business interests, and gov-
ernance. A crucial aspect of leveraging digital technolo-
gies in dairy cattle breeding is data harmonization and
integration. We highlight the importance of establishing
standardized data collection and data sharing protocols,
implementing robust quality control and data cleaning
methodologies, as well as defining novel sensor-based
traits and estimating their genetic background. In this
context, we compiled heritability estimates for novel
traits derived from data recorded by sensors and other
technologies in dairy cattle populations. The develop-
ment of phenomics in breeding programs, which involves
integrating multisource data—including sensor-based,
genomic, and management information—will be key to
accelerating genetic progress, especially for traits related
to animal welfare, health, resilience, and efficiency. This
review presents a roadmap for the effective use of sen-
sor-derived data in genetic evaluations, advocating for
centralized data infrastructures, transparent data-sharing
agreements, and the role of different stakeholders from
academia and industry, including organizations such
as the International Committee on Animal Recording
(ICAR) in establishing global standards and guidelines.
By addressing these challenges, dairy breeding programs
can fully harness precision dairy farming technologies
to enhance production and environmental efficiency,
improve animal health and welfare, and drive sustainable
genetic advancements in the dairy cattle sector.
Key words: genomic selection, genetic parameters,
heritability, novel traits, precision livestock farming
INTRODUCTION
Sensor systems and other precision dairy farming
technologies can partially replace human labor, contrib-
ute to improving the quality of life of dairy farmers (Tse
et al., 2017; Lovarelli et al., 2020; Hogan et al., 2022),
enhance labor output and labor cost over time (Liu et al.,
2023), increase reproduction efficiency (Reith and Hoy,
2018), contribute to improving animal health and welfare
Invited review: Using data from sensors and other precision farming
technologies to enhance the sustainability of dairy cattle breeding programs
Luiz F. Brito,1*  Bjørg Heringstad,2  Ilka Christine Klaas,3  Katharina Schodl,4  Victor E. Cabrera,5
Anna Stygar,6  Michael Iwersen,7  Marie J. Haskell,8  Kathrin F. Stock,9  Nicolas Gengler,10
Jeffrey Bewley,11  Miel Hostens,12  Elsa Vasseur,13  and Christa Egger-Danner4
1Department of Animal Sciences, Purdue University, West Lafayette, IN 47907
2Norwegian University of Life Sciences, 1432 Ås, Norway
3DeLaval International AB, 14721 Tumba, Sweden
4ZuchtData EDV–Dienstleistungen GmbH, 1200 Vienna, Austria
5University of Wisconsin–Madison, Madison, WI 53706
6Bioeconomy and Environment, Natural Resources Institute Finland (Luke), 00790 Helsinki, Finland
7Centre for Veterinary Systems Transformation and Sustainability, Clinical Department for Farm Animals and Food System Science,
University of Veterinary Medicine, 1210 Vienna, Austria
8SRUC (Scotland’s Rural College), Edinburgh EH9 3JG, United Kingdom
9IT Solutions for Animal Production (vit), 27283 Verden, Germany
10TERRA Teaching and Research Center, Gembloux Agro-Bio Tech, University of Liège, 5030 Gembloux, Belgium
11Holstein Association USA, Brattleboro, VT 05302
12College of Agriculture and Life Sciences, Cornell University, Ithaca, NY 14853
13McGill University, Ste Anne de Bellevue, H9X 3V9, QC, Canada

J. Dairy Sci. 108:10447–10474
https://doi.org/10.3168/jds.2025-26554
© 2025, The Authors. Published by Elsevier Inc. on behalf of the American Dairy Science Association®.
This is an open access article under the CC BY license (https://creativecommons.org/licenses/by/4.0/).
The list of standard abbreviations for JDS is available at adsa.org/jds-abbreviations-25. Nonstandard abbreviations are available in the Notes.
Received March 3, 2025.
Accepted July 28, 2025.
*Corresponding author: britol@  purdue  .edu

10448
Journal of Dairy Science Vol. 108 No. 10, 2025
(Dawkins, 2021) and productive efficiency (Simitzis et
al., 2021), optimize on-farm management, and increase
the long-term sustainability of dairy farms (Gargiulo et
al., 2018; Kaur et al., 2023). On-farm sensor systems
collect large amounts of data, which are only shared to
a limited extent and with the farmer’s consent outside
the farm (e.g., with milk recording organizations, breed-
ing organizations, milk processors, or other stakehold-
ers along the dairy value chain). Other data frequently
collected on farms include documented treatments with
related diagnoses and hoof-trimming registrations; re-
sults of laboratory tests from biological samples, such
as milk and blood; data from breeding and performance
recording organizations; and data from feed and dairy
processing operations (Steeneveld and Hogeveen, 2015).
Although large amounts of sensor data are being col-
lected on-farm, the data generated is so far not being
fully used across herds, such as in national genetic evalu-
ations, breeding programs, quality assurance programs
by dairy processors, or by other actors along the dairy
value chain. The value of the datasets generated can be
maximized through data integration. Data integration in
precision dairy farming refers to the process of combin-
ing and synchronizing data from multiple sources (e.g.,
sensors, automated systems, and management software)
into a unified platform. Therefore, the main goals of this
review are to (1) discuss the challenges and opportuni-
ties for integrating and leveraging data sets from sensor
systems and other technologies for improving dairy ge-
netic and genomic evaluations; (2) present a roadmap for
the standardization and integration of data from digital
technologies for use in dairy cattle breeding programs;
(3) describe the process of novel trait development;
and (4) provide examples of potentially useful sensor-
derived traits, along with available heritability estimates
when available, for inclusion in breeding programs. This
work is part of a joint initiative between the International
Committee of Animal Recording (ICAR; www .icar .org)
and the International Dairy Federation (IDF
; https:  / / fil
-idf .org) through the ICAR Functional
Traits Working
Group (FTWG) and the IDF Standing Committee of
Animal Health and Welfare in collaboration with interna-
tional experts from academia and industry organizations
(Egger-Danner et al., 2024). The main aim of this initia-
tive is to promote the integrated use of data from sensors
and other precision technologies and derived traits along
the dairy value chain with the goal of improving the sus-
tainability of dairy cattle production.
SENSORS AND OTHER TECHNOLOGIES
USED IN DAIRY FARMS
Recent advancements in sensor systems and other pre-
cision technologies (digital technologies) have enabled
the development of various tools for precision dairy
farming that support farmers and their advisors in moni-
toring the health and welfare, performance, reproductive
status, and environmental efficiency of dairy animals. A
wide range of technologies are commercially available
and have been implemented in dairy farms around the
world to support herd management and animal monitor -
ing (Stygar et al., 2021; Linstädt et al., 2024). In addition
to perform tasks such as milking cows (i.e., by automated
milking systems [AMS], also known as milking robots;
Marino et al., 2021), sensor technologies can be used for
automatically recording various physiological parameters
(Cerri et al., 2021; Tsai et al., 2021), animal behaviors
(Halachmi and Guarino, 2016), performance- and effi-
ciency-related characteristics (e.g., milk production and
composition, milking speed, feed efficiency), physical
attributes (e.g., body condition, BW; Silva et al., 2021),
environmental footprint (e.g., methane emission; Tullo et
al., 2019), and many others. Some technologies are used
for applications at the herd or group level, whereas oth-
ers monitor individual animals. The sources of data for
genetic evaluations are mainly those technologies that
record data on individual animals.
A plethora of equipment is available on the market,
which is usually supported by algorithms and computing
tools to provide summarized and processed information
(Rutten et al., 2013). For instance, accelerometers placed
on or in different parts of the animal’s body (e.g., leg,
neck, ear, reticulorumen, vagina, tail) can recognize
rumination, eating, lying, standing, and other behaviors,
and provide alerts and other information to the dairy
farmers and their possible advisors. Various sensor sys-
tems developed and used in dairy farms have been widely
described in the literature (Schillings et al., 2021; Silva
et al., 2021; Stygar et al., 2021; Hut et al., 2022; Singh et
al., 2022; Džermeikaitė et al., 2023; Linstädt et al., 2024;
Lovarelli et al., 2024).
Sensors and other technologies generate large amounts
of heterogeneous data (high recording frequency com-
bined with measurement over extended periods of time
and in different formats). In many cases, only summa-
rized or aggregated data based on the needs of the users
is made available to the users through proprietary algo-
rithms and web tools. Datasets from different technolo-
gies and technology providers tend to be of incompatible
formats, which make it difficult for dairy producers (and
their advisors or partners) to integrate the data from mul-
tiple sources in comprehensive tools and analyses. These
circumstances may lead to the creation of data silos on
dairy farms, hindering the usefulness of the comple-
mentary datasets for timely decision making. Further -
more, these datasets usually need to be processed using
statistical methods and often require high performance
computers for analyzing them comprehensively. In this
Brito et al.: INVITED REVIEW: SENSOR DATA FOR GENETIC IMPROVEMENT

Journal of Dairy Science Vol. 108 No. 10, 2025
10449
context, modern dairy farms require a data-oriented and
technology literate labor force to take full advantage of
the on-farm sensor technologies and datasets available.
On-farm sensors are used for improving herd man-
agement (Gargiulo et al., 2018; Liu et al., 2023), calv-
ing or estrus detection (Reith and Hoy, 2018; Szenci,
2022; Umaña Sedó et al., 2024), and identification of
cows needing attention or treatment (Džermeikaitė et
al., 2023; Lemmens et al., 2023). In addition, the da-
tasets generated can be used for supplementing genetic
and genomic evaluations. Sensor systems and other
technologies are potentially valuable sources of data for
genetic and genomic evaluations because data are col-
lected automatically, more objectively (higher precision
and less human errors), and continuously (or in high
frequency). Furthermore, as these digital technologies
have been used for many years in various farms, data
may already be available for a large proportion of the
population of cows that is currently included in the ge-
nomic evaluations. The automatically recorded data can
also be helpful for the definition and large-scale pheno-
typing of proxies for traits that are costly to record or
have low measurement frequencies, such as functional
traits (Egger-Danner et al., 2015; Brito et al., 2020).
More accurate phenotypes translate into greater genetic
progress of the target traits and breeding goals (God-
dard et al., 2016; Jones and Wilson, 2022).
ROLE OF PHENOTYPING IN DAIRY CATTLE
BREEDING PROGRAMS
Different sources of data have been used in breeding
programs over time, including data from sensors and
other technologies (e.g., Rojas de Oliveira et al., 2024).
The usefulness of variables recorded by sensor systems
for breeding purposes depends on several factors. De-
rived traits must exhibit sufficient phenotypic variation,
be heritable and repeatable within the target population,
capture the biological mechanisms relevant to the breed-
ing goal of interest or show a genetic correlation with the
target or breeding goal trait, be measured reliably and
frequently over an extended time period (i.e., longitu-
dinal measurements), and be objectively recorded in a
standardized manner. Data collected by several precision
technologies meet many of these criteria, but are not well
documented in the literature.
In addition to measuring the traits of interest (or
auxiliary traits), there is a need for recording environ-
mental (systematic) effects influencing the phenotypic
records to allow appropriate statistical modeling. When
performing genetic and genomic evaluations, fitting as
many as possible significant systematic effects (com-
monly known as “fixed effects”) in the models removes
nongenetic influence on the traits resulting in more ac-
curate breeding values. Examples of systematic effects
include cow parity, age at measurement, contemporary
group (e.g., concatenation of herd, year, and season
of calving), measurement time, sensor type, climatic
variables, and others. Digital technologies can also be
useful for recording variables allowing to derive some
of these systematic effects.
Another important point to emphasize is the value of
having many animals from the same herds with measure-
ments for multiple variables (i.e., various sensor types
on the same animal or close relatives as well as direct
and indirect traits related to the breeding goal). Having
the same animals with phenotypic records for all (or
most) traits facilitate the estimation of phenotypic and
genetic covariances between traits. This is important for
accurate estimation of the genetic correlations among all
measured traits which is needed for the proper design or
refinement of selection indexes.
The effectiveness of dairy cattle breeding programs
depends on large-scale and diverse datasets for multiple
traits measured ideally throughout the life of a dairy
animal or across prolonged periods. This includes rou-
tinely recorded datasets (e.g., records from dairy farmers
through DHIA, veterinarians, claw trimmers; farm man-
agement systems; pedigree and conformation variables
from breed associations), data from sensors and other
precision technologies, multi-omic intermediate data
such as genomics, metabolomics (from biological sam-
ples, such as milk, saliva, and blood), microbiome, tran-
scriptomics (gene expression), epigenomics, proteomics,
lipidomics, and many others. Full integration of these
data into a common platform has a huge potential for
optimization of dairy cattle genetic evaluation and man-
agement purposes. The individual reliability of breeding
values relies, among other factors, on the amount of
phenotypic information available for the animals them-
selves and on genetically related individuals. As digital
technologies enable the collection of more objective data
in higher frequency as compared with traditional data
collection schemes (e.g., test-day records), (genomic- or
pedigree-based) EBV for traits derived from precision
technologies have the potential to be more reliable, and
consequently, greater genetic progress can be obtained
for such traits (Poppe et al., 2019; Pedrosa et al., 2023;
Schodl et al., 2024b).
CHALLENGES IN COLLECTING AND USING DATA
FROM SENSORS AND OTHER TECHNOLOGIES
FOR BREEDING PURPOSES
Despite the great and clear potential of sensor data for
genetic and genomic analyses, several challenges must be
overcome. The main challenges described here in more
details is not an exhaustive list. First, the global market
Brito et al.: INVITED REVIEW: SENSOR DATA FOR GENETIC IMPROVEMENT

10450
Journal of Dairy Science Vol. 108 No. 10, 2025
of digital technologies for the dairy sector is very frag-
mented. Already in 2020, there were 67 different provid-
ers of various sensor technologies, including 37 suppliers
of accelerometer-based technologies and 13 producers of
milking robots (Stygar et al., 2021). The increasing num-
ber of start-ups with focus on precision livestock farming
imply that the overall figures today might be even higher.
Uniform standards exist for some of these technologies,
but only for limited devices and technology-derived
variables. For instance, ICAR has developed standards
and recommendations for testing, approval, and periodic
checking of milk recording devices including milk yield
and composition (ICAR, 2020). However, there are no
guidelines for using records from accelerometer-based
technologies, making it more difficult to use sensor data
from more than one brand in genetic evaluations.
For better use for genetic evaluations, sensors and
other technologies should be tested in more diverse
farming environments (i.e., not only in experimental
farm conditions), across different management systems
(e.g., intensive dairy production, pasture-based systems,
freestall and tiestall housing) and geographical locations
with diverse climatic conditions, in different breeds, and
in animals of different ages and in varied physiological
stages (e.g., lactation stage, reproductive stage). As this
testing is time consuming and costly, collaboration among
academia and manufacturers is essential for improving
the quality assessment of sensor technologies and for
increasing the accessibility of independent validations of
commercially available sensors.
In most cases, comprehensive information on the sen-
sor systems is lacking, which complicates their evaluation
and application for breeding purposes. This challenge is
exacerbated by the wide variety of approaches employed
to address similar problems or collect similar types of
data, leading to inconsistencies in methodologies and
outcomes. For instance, many sensors are available for
measuring activity and rumination time, but they may
use different algorithms, perform different data editing
and quality control, or may capture different information,
and consequently, the phenotypic records obtained may
be quite different even when multiple sensors are used
in the same animals (Mayo et al., 2019). In many cases,
“gold standard” variables or procedures to validate the
sensors are lacking (or the gold standard approach may
be time or cost prohibitive), contributing to unsatisfac-
tory agreement among sensors recording the same type of
information. Some variables are easier to validate (e.g.,
milk yield, milk composition, SCC), whereas others are
more complex such as animal activity across sensors and
alerts based on multiple and different parameters depend-
ing on the sensor brand.
Many data providers exist (e.g., manufacturers of sen-
sor systems, data integration organizations), and often
producers are unsure of which sensor to use, as valida-
tion and comparison among the sensor systems are cur -
rently lacking. This is an important challenge for genetic
evaluations, especially national genetic evaluations that
combine data from multiple farms, as the data from dif-
ferent types of sensor technologies or sensor technolo-
gies targeting the same condition but provided by dif-
ferent brands may represent different traits. Therefore,
several analyses (e.g., estimation of genetic correlations
between traits recorded by different sensor types) must
be performed before merging datasets on a routine basis.
As a first step, it is important to enhance the transparency
of the testing conditions (e.g., farm type, breed, life stage
of the animals) and, subsequently, to clarify the potential
and limitations of each commercial technology for genet-
ic evaluations that are made available in the market. In
the case of wearable sensors, the animal’s body location
where the sensors are attached may influence the data
recorded and must accordingly be indicated. Additional
validation of existing sensor systems is an important re-
search task to be completed.
In general, sensor systems consist of measuring devic-
es, algorithms, and computer applications or interfaces,
which are often proprietary information. Sensor outputs
can be measurements of certain individual conditions, or
outputs based on multiple parameters, given as indexes
or alerts (e.g., for estrus or health issues). As sensor
systems were developed to support farmers in managing
their herds, they have been optimized to provide action-
able information. However, the use of sensor data across
herds and along the dairy value chain (e.g., for genetic
evaluations) will require more information or additional
variables and definitions. There is significant lack of
background information on the data generation proce-
dures and detailed metadata with information on the type
of data recorded, units, and resolution or frequency of the
records (Rutten et al., 2013). In many cases, manufactur -
ers may only provide information on a few variables of
greater interest to the dairy farmers (e.g., estrous alert),
but the data used for generating these alerts could be of
great value for deriving traits for inclusion in genetic
evaluations. Many providers of sensor technology do not
have (or provide) any information about the variables
that are being collected by the sensors (e.g., variable
definition, units, plausible ranges, calculation approach).
This results in data being underused or misused as com-
munication between academia or data analysts working
with the farmers and manufacturers may not always be
straightforward. The publication of data user guides as-
sociated with each digital technology would be of great
value for geneticists and other data analysts. It is worth
noting that manufacturers of sensor systems may be will-
ing to share additional data for research purposes but
may be more restrictive when sharing data publicly or
Brito et al.: INVITED REVIEW: SENSOR DATA FOR GENETIC IMPROVEMENT

Journal of Dairy Science Vol. 108 No. 10, 2025
10451
for other commercial purposes. To promote data sharing
(e.g., for genetic evaluations), clear communication be-
tween stakeholders and development of interinstitutional
guidelines and agreements are of great importance. Or -
ganizations such as ICAR can develop standards and
guidelines to technically facilitate data exchange, thus
creating an environment that facilitates negotiations and
agreements for commercial use between different parties.
Sensors and algorithms are believed to have been
improved over time, which is positive because the data
generated is expected to become more accurate. How-
ever, there tends to be a lack of recording (or sharing)
of important information such as algorithm or sensor
updates that may affect the accuracy of the data being
recorded on individual animals. If not recorded and ac-
counted for in the statistical models, this could result
in artificial differences in the phenotypic measurements
collected over time (i.e., biased phenotypic trends).
When these changes are homogeneous across all
animals in the same contemporary group (animals with
similar conditions; e.g., concatenation of farm, calving
season, and calving year), the lack of updates’ informa-
tion may be less of an issue. However, when farmers
combine animals with older and recent versions of the
equipment in the same contemporary group, the lack of
information on these versions (or updates) could result
in less accurate breeding values. Even if this informa-
tion is shared, geneticists or other data analysts need to
carefully adjust their pipelines for the genetic analyses
to include the changes made by the data providers.
As dairy farms are using many sensors and technolo-
gies, there are consequently different data sources with
multiple data retrieval protocols (e.g., through applica-
tion programming interface, data provider’s website,
farm back-ups). Some additional challenges for retriev-
ing and merging the datasets include (1) datasets are
generated in heterogeneous data formats; (2) sensors
may record data with different frequencies (e.g., every 2
h vs. daily summaries); (3) data sources may use differ -
ent animal identification systems; (4) datasets generated
are in many cases proprietary implying limitations of the
access to the raw datasets (defined here as unprocessed
data as originally recorded by the sensors); (5) the scripts
and pipelines developed may be nontransferable across
data sources; (6) lack or poor internet connectivity in
rural areas, which makes it more difficult to transfer data
from the farms to data processing stations; (7) on-farm
hardware and software may be outdated, making the
herd management and sensor systems unstable and data
extraction more difficult; (8) datasets can be very large
(e.g., video data) and require a lot of computing power
for storage and analyses, which can become expensive
in the long term; and (9) data provider platforms may
only store the data at a lower resolution (e.g., daily sum
or averages instead of per-visit measurements). All these
challenges contribute to increasing data silos within and
between farms and to an underutilization of the informa-
tion contained in these datasets that could be used for
herd management and breeding.
Within different research projects, data integration
platforms have been set up including, for example, the
Purdue Animal Science Data Ecosystem (Boerman et
al., 2025), DairyBrain (Cabrera et al., 2020), and Giga-
cow (Klingström et al., 2022). Within other projects
such as D4Dairy (www  .d4dairy  .com; Egger-Danner et
al. 2022a,b), routine data exchange pipelines have been

elaborated and implemented in the central cattle database
and manufacturers. In collaboration between DHIA,
breeding organizations, and manufactures routine data
exchange pipelines have been or are being established
and integrated data are being made available. Examples
are the Nordic Cattle Database (www  .nordicebv  .info)
and the Central Cattle Database Cooperation between
Germany and Austria (
www .rdv  -gmbh  .net) . The Inter -
national Dairy Data Exchange Network (
www .idden
.org) is also working on simplifying data flow with
one seamless interface connecting dairy stakeholders.

Furthermore, many companies are working on this area,
including Iyotah Solutions (www  .iyotah  .com/  ), Vyla
(www .vyla  .com/  ), Dairy Data Warehouse (dairydata
-
warehouse.com), Join-Data (www  .join  -data  .nl), Dairy
Performance Network (
www .dairyperformancenetwork
.com/  ), AgriGates (https:  / / agrigates  .io/  ), Connecterra
(www .connecterra  .ai/  ), and others.
Once data collected by sensor technologies have been
received, extensive preprocessing and cleaning of the
data are often needed to ensure its usability and reliability

(van der V oort et al., 2021; Schodl et al., 2024b). Limited
data editing and cleaning protocols are available in the
scientific literature. Data scientists may also have access
to different types of data requiring different handling.
Raw data, defined here as unprocessed or minimally pro-
cessed data directly collected by sensors and monitoring
devices before any form of cleaning, filtering, analysis,
or interpretation within the sensor systems will likely
vary much more than summarized or processed data.
The absence of standardized protocols for editing sensor
data undermines the comparability and reliability of the
results generated. Therefore, we encourage the develop-
ment of automated pipelines for data collection, process-
ing, editing, analytics, and data visualization.
Last, but certainly not least, a need exists for continu-
ous dialog between stakeholders along the dairy value
chain from sensor manufacturers to farmers and research-
ers from different organizations to create a common un-
derstanding on the potential and value of sensor data for
genetic evaluation. Such dialog will facilitate the defini-
tion of suitable data sharing models, which ideally, will
Brito et al.: INVITED REVIEW: SENSOR DATA FOR GENETIC IMPROVEMENT

10452
Journal of Dairy Science Vol. 108 No. 10, 2025
increase the benefits for all stakeholders along the dairy
value chain, while strengthening academic and industrial
research and innovation. Addressing all these challeng-
ing topics is essential to enhance the consistency, qual-
ity, and utility of sensor-based systems for genetic and
genomic evaluations as well as for many other purposes.
DATA CLEANING, EDITING,
AND QUALITY ASSURANCE
Considering the growing amount of sensor devices,
applications, data, and computational methods, the need
for comprehensive data cleaning procedures has grown
to ensure data quality, accuracy, and utility. Despite es-
tablished data cleaning protocols in bioinformatics (e.g.,
Chicco et al., 2022) and health informatics (e.g., Van
den Broeck et al., 2005) or for the use in routine genetic
evaluation and tools provided by DHI and breeding orga-
nizations (see ICAR, 2022), comparable guidelines spe-
cific to high-resolution dairy sensor data remain limited.
Based on experiences within the D4Dairy project (https:
/ / d4dairy .com; Egger-Danner et al., 2022a,b) and review
of relevant literature, Schodl et al. (2024b) proposed a

5-step framework for cleaning sensor data, including
 1. Validating the data merging process. Accurate
alignment between animal identifiers and sensor
data is critical. Errors such as nonunique device
by animal combination, broken sensors, and time
zone mismatches must be identified and cor -
rected, if possible. It is recommended to consult
with digital technology companies for informa -
tion on proper alignment, as well as algorithm
learning periods.
 2. Understanding the data. This step involves iden-
tifying the type of data (e.g., raw sensor data or
processed data retrieved from interfaces), its

nature including units and whether it is a single
point measurement or an aggregated value, and
sampling rates. Proper data visualization is rec-
ommended to facilitate detection of patterns, dis-
tributions, or anomalies.
 3. Checking data completeness. Missing data causing
gaps in time series is a common issue and often
caused by sensor malfunctions, low battery, or

poor connectivity. Depending on the subsequent
analyses, missing data may require interpolation,
imputation, or exclusion. Conversely, duplicate
or inconsistent timestamps should be resolved to
maintain data integrity.
 4. Evaluating data plausibility and detecting outliers.
This step may be the most critical one requiring
well-considered decisions by the data user. Outlier

detection may be based on biologically meaningful
ranges, cross-checks using additional information,
if available, statistical thresholds (e.g., ± 3 SD
from the mean), or advanced modeling techniques
such as Dynamic Linear Models incorporating
Kalman filters (e.g., Stygar et al., 2017) or utiliz-
ing the co-dependency of data quality and model
robustness (e.g., Papst et al., 2021). Regarding
the management of outliers, attention should be
paid to avoid removal of genuine outliers that may
provide critical insights.
 5. Addressing technology-related noise. Inconsis-
tencies in the data may be caused by sensor drift,
calibration issues, and hardware or software
updates. Information on updates and handling of

drift and calibration issues by the sensor com-
pany may be helpful but not necessarily easily
available. Indications to look for in the data are
for example the introduction of new variables,
different temporal resolutions, and sudden or
persistent changes in scale.
In addition to these steps summarized by Schodl et al.
(2024b), broader aspects such as the purpose and con-
text of data analyses, as well as their thorough documen-
tation. Data for applications in herd management may
have different requirements than those for breeding. As
an example, if different versions of a software were used
in a certain farm, but all animals from the same con-
temporary group had the same sensor version, the data
would be useful for genetic purposes as geneticists are
interested in differences among animals from the same
group rather than the absolute values. Conversely, alerts
generated by sensors are important for management pur -
poses, but for genetic evaluations, the continuous vari-
able used for generating the alerts (e.g., activity level
to predict estrus events) might be preferred because of
its independence from the quality of would already be
useful even if the system’s algorithm used for generating
the alerts was not highly accurate.
Data cleaning process is both costly and time consum-
ing (Wang and Wang, 2020). However, some savings
can be achieved by broad implementation of automated
procedures. Regarding dairy cows, automatic sensor data
cleaning pipelines have been successfully applied to
improve the accuracy of positioning algorithms (Pastell
et al., 2018), to detect leg problems using load sensors
(Pastell et al., 2008), or even to track mastitis control op-
tions (Rustas et al., 2024). Furthermore, automatic repair
methods exist for non-sensor data, but the authors are not
aware of their application in dairy science (for instance,
filling in missing information on breed or herd number).
Therefore, in the future, more standardized approaches
should be considered and (open source) data cleaning
solutions should be made available.
Brito et al.: INVITED REVIEW: SENSOR DATA FOR GENETIC IMPROVEMENT

Journal of Dairy Science Vol. 108 No. 10, 2025
10453
DERIVING NOVEL TRAITS FROM SENSORS
AND OTHER TECHNOLOGIES
Sensors and other technologies provide an opportunity
for recording such traits in a more frequent and accurate
manner and could, consequently, fasten the rate of ge-
netic progress for these key breeding goals. Ideally, the
derived traits should have sufficient phenotypic varia-
tion, be heritable and repeatable, capture the biological
mechanisms of interest (or be genetically correlated with
the breeding goal trait), be clearly defined and evaluated
in a standard way across the population being jointly
genetically evaluated, and be recorded routinely and in
large-scale at a low cost per data point. First, it is es-
sential to obtain detailed documentation on the record-
ing methods and units of the variables of interest. This
information, which needs to be provided by the manufac-
turers of sensors or technologies, includes how data are
recorded and the handling of missing values (e.g., zeros,
blanks, or other symbols). Accurate documentation en-
sures consistency and reliability in subsequent analyses.
When working with the same variables recorded by
sensors from different brands, it is important to assess
the variance of the variables and not merely correct for
the mean effect by including the brand or company as
a fixed effect. This evaluation ensures comparability
across different sources and informs whether data from
different sensors can be combined effectively. In some
cases, similar types of data may represent different (but
correlated) traits. Once the data are harmonized, traits of
interest should be derived. It is also critical to define the
gold standard measures of the breeding goal of interest to
facilitate comparisons with derived traits.
After the breeding goals and the potential data sources
(with the selection criteria variables) have been clearly
identified (e.g., improved fertility based on variability in
activity level recorded by activity monitors; Heringstad
and Wethal, 2023), statistical models must then be devel-
oped to test systematic effects that influence the trait(s)
of interest. These effects should be incorporated into ge-
netic models to ensure accurate predictions of breeding
values. Understanding the influence of each systematic
effect (e.g., parity, lactation stage, herd, season, diet, re-
productive stage, housing time) on traits can also inform
future management decisions; for instance, assessing the
effect of ambient temperature and humidity on rumina-
tion patterns could guide feeding strategies. Modeling
systematic effects that significantly influence the target
trait is enabled by integrating sensor data into the estab-
lished data infrastructure for dairy cattle. This highlights
the need for data integration as systematic effects are
usually recorded in herd management software and not
directly by the sensors. Finally, variance components and
genetic parameters, including heritability and genetic
correlations among all derived and existing traits, should
be estimated for all derived traits. The accuracy of (G)
EBV and the potential re-ranking of selection candidates
should also be assessed to ensure robust decision mak-
Brito et al.: INVITED REVIEW: SENSOR DATA FOR GENETIC IMPROVEMENT
Table 1. Heritability estimates for automatically recorded indicators of health in dairy cattle populations 1
Trait  Sensor type N Breed h2 Reference
EC  AMS integrated sensor 1,714 Holstein 0.22 ± 0.04 Dechow et al. (2020)
Daily average EC  AMS integrated sensor 8,455 Holstein 0.48 ± 0.10 Lu et al. (2024)
EC at milking session 1  AMS integrated sensor 8,455 Holstein 0.46 ± 0.10 Lu et al. (2024)
EC at milking session 2  AMS integrated sensor 8,455 Holstein 0.47 ± 0.10 Lu et al. (2024)
EC at milking session 3  AMS integrated sensor 8,455 Holstein 0.47 ± 0.10 Lu et al. (2024)
EC  AMS integrated sensor 4,280 Holstein 0.46 ± 0.02 Medeiros et al. (2024)
EC  AMS integrated sensor 4,507 Holstein 0.38 to 0.49 Pedrosa et al. (2023)
EC  AMS integrated sensor 1,899 Holstein 0.38 ± 0.01 Piwczyński et al. (2021)
EC, front left  AMS integrated sensor 922 Holstein 0.46 ± 0.09 Santos et al. (2018)
EC, front right  AMS integrated sensor 922 Holstein 0.44 ± 0.09 Santos et al. (2018)
EC, rear left  AMS integrated sensor 922 Holstein 0.37 ± 0.08 Santos et al. (2018)
EC, rear right  AMS integrated sensor 922 Holstein 0.38 ± 0.09 Santos et al. (2018)
Overall EC  AMS integrated sensor 922 Holstein 0.53 ± 0.09 Santos et al. (2018)
EC  AMS integrated sensor 1,486 Holstein 0.36 ± 0.04 Sitkowska et al. (2024)
EC, mean  AMS integrated sensor 4,714 Norwegian Red 0.35 ± 0.03 Wethal et al. (2020a)
EC, maximum  AMS integrated sensor 4,714 Norwegian Red 0.23 ± 0.02 Wethal et al. (2020a)
Blood in milk  AMS integrated sensor 1,714 Holstein 0.09 ± 0.03 Dechow et al. (2020)
Smoothed milk BHB values (parity 1)  Herd Navigator (BHB) 794 Nordic Red 0.09 ± 0.07 Häggman et al. (2019)
Smoothed milk BHB values (parity 2)  Herd Navigator (BHB) 794 Nordic Red 0.07 ± 0.07 Häggman et al. (2019)
Milk temperature  AMS integrated sensor 1,899 Holstein 0.41 ± 0.01 Piwczyński et al. (2021)
SCS  AMS integrated sensor 1,899 Holstein 0.36 ± 0.01 Piwczyński et al. (2021)
Mastitis susceptibility  AMS integrated sensor 1,791 Holstein 0.07 ± 0.03 Welderufael et al. (2017)
Mastitis recovery  AMS integrated sensor 1,791 Holstein 0.08 ± 0.03 Welderufael et al. (2017)
Log-transformed online cell count  AMS integrated sensor 1,490 Norwegian Red 0.09 ± 0.03 Wethal et al. (2020a)
1AMS = automated milking system; EC = electrical conductivity. Values for h 2 are reported as ± SE or range.

10454
Journal of Dairy Science Vol. 108 No. 10, 2025
ing in breeding programs. When the same variable (e.g.,
rumination time) is recorded by different sensors, before
merging all the data for genetically evaluating the ani-
mals for a single trait, one should assess the genetic cor -
relation between the traits derived from different sensors
and the phenotypic records recorded by different sensors
should only be merged and considered as the same (or
similar) trait when very high (e.g., >0.90) genetic cor -
relations are observed between them. Otherwise, the
records from different sensors should be evaluated as
different and correlated traits in the genetic evaluations.
Additional genomic analyses could be performed to bet-
ter understand the underlying mechanisms influencing
the derived traits such as GWAS and post-GWAS analy-
ses to identify candidate genes and metabolic pathways
associated with the target traits.
In the past few years, various sensor-based traits have
been derived and some of them have already been in-
cluded in corporate or national selection indexes. In the
subsequent sections and in Tables 1, 2, 3, 4, 5, 6, 7, 8, and
9, we describe examples of novel traits that have been de-
rived based on data from sensors and other technologies
along with their heritability estimates (when available)
and respective references. In general, higher heritability
estimates, and accordingly higher accuracies of (G)EBV ,
can be expected for sensor-based traits than for tradition-
ally recorded traits, which relates to the different levels
of phenotyping accuracy and frequency.
Health and Welfare
Several animal welfare and health parameters are cur -
rently collected routinely through technologies for the
primary purpose of on-farm monitoring of animal status.
Body Temperature. Wearable sensors such as rumen
boluses, ear tags, or skin-mounted devices are commonly
used for continuously monitoring body temperature
(Woodward et al., 2024). Body temperature data are
stored on different resolutions (e.g., every 5 or 10 min)
and analyzed to detect deviations from normal tempera-
ture ranges, indicating potential health issues such as
infections or heat stress (Woodward et al., 2024). Body
temperature data enable early detection of diseases, al-
lowing for prompt interventions. In addition, body tem-
perature data are used for monitoring heat stress to adjust
management practices accordingly and also for breeding
for improved heat tolerance, as discussed below. Body
temperature in dairy cattle is heritable (Luo et al., 2021a)
and influenced by key genes (Luo et al., 2021b), sug-
gesting potential for selection. A challenge with body
temperature is that it varies depending on the sensor
location on the animal’s body (Bewley et al., 2008a).
Further research investigating the genetic background of
sensor-based body temperature variability in dairy cattle
is still needed.
Heart and Respiration Rate. Wearable biometric
sensors, such as heart rate monitors and respiratory sen-
sors, collect data continuously (Vakulya et al., 2024).
Fluctuations in heart and respiration rates can indicate
stress, pain, or disease (von Borell et al., 2007). There-
fore, such variables can be used for assessing animal
welfare and stress levels and early detection of respira-
tory or cardiovascular issues. Limited studies are avail-
able on the heritability of heart and respiration rate in
dairy cattle populations. Thus far, sensors for measuring
heart and respiration rates are cumbersome, invasive,
and not suitable for long-term data collection. Cameras
may provide an avenue for automatically recording res-
Brito et al.: INVITED REVIEW: SENSOR DATA FOR GENETIC IMPROVEMENT
Table 2. Heritability (h 2) estimates for cow behavioral traits derived from automated milking systems (milking robots)
Trait N Breed h2 ± SE Reference
Choice consistency score (5–50 DIM, primiparous) 730 Holstein 0.04 ± 0.06 Løvendahl et al. (2016b)
Choice consistency score (5–50 DIM, multiparous) 1,231 Holstein 0.05 ± 0.04 Løvendahl et al. (2016b)
Choice consistency score (51–110 DIM, primiparous) 730 Holstein 0.11 ± 0.08 Løvendahl et al. (2016b)
Choice consistency score (51–110 DIM, multiparous) 1,231 Holstein 0.07 ± 0.05 Løvendahl et al. (2016b)
Choice consistency score (111–215 DIM, primiparous) 730 Holstein 0.14 ± 0.08 Løvendahl et al. (2016b)
Choice consistency score (111–215 DIM, multiparous) 1,231 Holstein 0.07 ± 0.04 Løvendahl et al. (2016b)
Choice consistency score (216–305 DIM, primiparous) 730 Holstein 0.08 ± 0.07 Løvendahl et al. (2016b)
Choice consistency score (216–305 DIM, multiparous) 1,231 Holstein 0.02 ± 0.03 Løvendahl et al. (2016b)
Knock off (binary) 922 Holstein 0.03 ± 0.03 Santos et al. (2018)
Log-transformed handling time 4,883 Norwegian Red 0.07 ± 0.02 Wethal and Heringstad (2019)
Number of kick-offs 4,883 Norwegian Red 0.06 ± 0.01 Wethal and Heringstad (2019)
Number of kick-offs 1,714 Holstein 0.08 ± 0.02 Dechow et al. (2020)
Proportion of milkings with kick-offs 4,883 Norwegian Red 0.13 ± 0.03 Wethal and Heringstad (2019)
Preference consistency score 4,249 Holstein 0.09 ± 0.01 Bérat et al. (2025)
Preference consistency score 2,258 Holstein 0.07 ± 0.02 Løvendahl and Buitenhuis (2022)
Preference consistency score 2,407 Jersey 0.13 ± 0.03 Løvendahl and Buitenhuis (2022)
Temperament 72,683 Norwegian Red 0.05 ± 0.01 Wethal et al. (2020b)
Time profile (profile of the diurnal milking time) 2,258 Holstein 0.11 ± 0.02 Løvendahl and Buitenhuis (2022)
Time profile (profile of the diurnal milking time) 2,407 Jersey 0.04 ± 0.02 Løvendahl and Buitenhuis (2022)

Journal of Dairy Science Vol. 108 No. 10, 2025
10455Brito et al.: INVITED REVIEW: SENSOR DATA FOR GENETIC IMPROVEMENT
Table 3. Heritability (h 2) estimates for sensor-based activity traits measured in Holstein dairy cows
Trait  Sensor type or brand N h2 ± SE Reference
Activity time (min/24 h)  SenseHub (Allflex Livestock Intelligence) collar 453 0.14 ± 0.06 Lemal et al. (2024)
Activity (daily)  Pedometer 635 0.19 ± 0.06 Nascimento et al. (2024)
Activity (weekly)  Pedometer 635 0.23 ± 0.07 Nascimento et al. (2024)
Activity  Electronic activity neck tags (SCR Heatime HR system) 1,171 0.09 ± 0.05 Schöpke and Weigel (2014)
Duration of high activity episode  Electronic activity tags (neckbands) 11,522 0.03 ± 0.01 Ismael et al. (2016)
Eating rate (kg/h)  Automated feeders 842 0.46 ± 0.09 Lin et al. (2013)
Eating time (first parity)  SenseHub dairy sensors (Allflex) 142 0.42 ± 0.09 Atashi et al. (2024)
Eating time (second parity)  SenseHub dairy sensors (Allflex) 243 0.45 ± 0.04 Atashi et al. (2024)
Eating time (first parity)  SenseHub dairy sensor (Allflex) 142 0.42 ± 0.09 Atashi et al. (2024)
Eating time (second parity)  SenseHub dairy sensor (Allflex) 243 0.45 ± 0.04 Atashi et al. (2024)
Eating time (min/24 h)  SenseHub (Allflex) collar 453 0.12 ± 0.05 Lemal et al. (2024)
Interval from calving to first high activity  Electronic activity tags fitted on neckbands 11,522 0.11 ± 0.02 Ismael et al. (2016)
Lying time (daily)  SMARTBOW ear-tag accelerometer 728 0.37 ± 0.07 Nascimento et al. (2024)
Lying time (weekly)  SMARTBOW ear-tag accelerometer 728 0.48 ± 0.09 Nascimento et al. (2024)
Strength of high activity episode  Electronic activity tags (neckbands) 11,522 0.03 Ismael et al. (2016)
Daily sum activity (DIM 7 and 14)  Lely 1,084 0.13 ± 0.09 Schodl et al. (2024a)
Daily SD activity (DIM 7 and 14)  Lely 1,084 0.33 ± 0.14 Schodl et al. (2024a)
Mean daily activity sum over 5–7 and 12–14 DIM  Lely 1,084 0.24 ± 0.07 Schodl et al. (2024a)
Mean daily activity SD over 5–7 and 12–14 DIM  Lely 1,084 0.35 ± 0.09 Schodl et al. (2024a)
Regression slope of activity daily sum over 5–7 and 12–14 DIM  Lely 1,084 0.12 ± 0.03 Schodl et al. (2024a)
Regression slope of daily SD over 5–7 and 12–14 DIM  Lely 1,084 0.18 ± 0.04 Schodl et al. (2024a)
Mean daily activity sum over 150 DIM  Lely 1,084 0.15 ± 0.06 Schodl et al. (2024a)
Mean daily activity SD over 150 DIM  Lely 1,084 0.19 ± 0.07 Schodl et al. (2024a)
Regression slope of daily activity sum over 150 DIM  Lely 1,084 0.22 ± 0.13 Schodl et al. (2024a)
Regression slope of daily activity SD over 150 DIM  Lely 1,084 0.11 ± 0.14 Schodl et al. (2024a)
Mean daily activity sum over 305 DIM  Lely 1,084 0.18 ± 0.05 Schodl et al. (2024a)
Mean daily activity SD over 305 DIM  Lely 1,084 0.18 ± 0.06 Schodl et al. (2024a)
Regression slope of daily activity sum over 305 DIM  Lely 1,084 0.18 ± 0.13 Schodl et al. (2024a)
Regression slope of daily activity SD over 305 DIM  Lely 1,084 0.26 ± 0.17 Schodl et al. (2024a)
Daily activity sum on 7 and 14 DIM  Smaxtec 409 0.18 ± 0.11 Schodl et al. (2024a)
Daily activity SD on 7 and 14 DIM  Smaxtec 409 0.55 ± 0.21 Schodl et al. (2024a)
Mean daily activity sum over 5–7 DIM and 12–14 DIM  Smaxtec 409 0.34 ± 0.11 Schodl et al. (2024a)
Mean daily activity SD over 5–7 DIM and 12–14 DIM  Smaxtec 409 0.47 ± 0.11 Schodl et al. (2024a)
Regression slope of daily activity sum over 5–7 DIM and 12–14 DIM  Smaxtec 409 0.00 ± 0.00 Schodl et al. (2024a)
Regression slope of daily activity SD over 5–7 DIM and 12–14 DIM  Smaxtec 409 0.07 ± 0.03 Schodl et al. (2024a)
Mean daily activity sum over 150 DIM  Smaxtec 409 0.00 ± 0.00 Schodl et al. (2024a)
Mean daily activity SD over 150 DIM  Smaxtec 409 0.00 ± 0.00 Schodl et al. (2024a)
Regression slope of daily activity sum over 150 DIM  Smaxtec 409 0.00 ± 0.00 Schodl et al. (2024a)
Regression slope of daily activity SD over 150 DIM  Smaxtec 409 0.00 ± 0.00 Schodl et al. (2024a)
Mean daily activity sum over 305 DIM  Smaxtec 409 0.00 ± 0.00 Schodl et al. (2024a)
Mean daily activity SD over 305 DIM  Smaxtec 409 0.00 ± 0.00 Schodl et al. (2024a)
Regression slope of daily activity sum over 305 DIM  Smaxtec 409 0.00 ± 0.00 Schodl et al. (2024a)
Regression slope of daily activity SD over 305 DIM  Smaxtec 409 0.00 ± 0.00 Schodl et al. (2024a)
Activity: mean, SD, and median on the day of milk recording (test day)  Lely 1,289 0.09–0.16 (±0.01–0.04) Schodl et al. (2023)
Activity: deviation between mean and SD at test day and 5 and 10 d before  Lely 1,289 0.12–0.19 (±0.01–0.05) Schodl et al. (2023)
Activity: mean, SD, mean SD, and median over 3–305 DIM  Lely 1,289 0.17–0.20 (±0.03) Schodl et al. (2023)
Eating time: mean, SD, and median on the day of milk recording (test day)  Lely 1,289 0.11–0.33 (±0.01–0.06) Schodl et al. (2023)
Eating time: deviation between mean and SD at test day and 5 and 10 d before  Lely 1,289 0.20–0.37 (±0.03–0.07) Schodl et al. (2023)
Eating time: mean, SD, mean SD, and median over 3–305 DIM  Lely 1,289 0.34–0.39 (±0.06–0.07) Schodl et al. (2023)

10456
Journal of Dairy Science Vol. 108 No. 10, 2025
piration rate data but, to our knowledge, it has not yet
been tested in large scale.
Rumen Activity and Reticuloruminal pH. Boluses
equipped with sensors measure parameters such as pH
and temperature in the rumen and reticulum (Denwood et
al., 2018; Mensching et al., 2020). Continuous monitor -
ing helps in assessing digestive health and detecting dis-
orders such as acidosis (Simoni et al., 2023, 2024). This
type of data can be used for managing feeding strategies
to prevent metabolic disorders, for optimizing rumen
health for better feed efficiency, and for breeding pur -
poses. However, heritability estimates for rumen activity
and reticuloruminal pH stability are scarce.
Lameness and Hoof Disorders. Accelerometers, pres-
sure-sensitive walkways, and advanced video analyses
(2- and 3-dimensional [3D]) are employed for assessing
the presence and severity of lameness (Nejati et al., 2023).
For instance, computer vision techniques analyze gait
and posture to identify lameness. Recent advancements
use deep learning models to enhance detection accuracy
(Karoui et al., 2021; Dervić et al., 2024). Such tools have
the potential to enable early identification of lameness,
allowing for timely treatment, improving animal welfare
and reducing economic losses. Lemmens et al. (2023)
showed differences in sensor-based behavior (e.g., eat-
ing time, activity) between cows with different lameness
scores. Lameness has been found to have a heritable com-
ponent, with heritability estimates ranging from low to
moderate (Heringstad et al., 2018; Köck et al., 2019) and
are of highly polygenic nature (Sousa Junior et al., 2024).
This indicates potential for genetic selection to reduce
lameness incidence through genomic selection.
Udder Health. Table 1 presents heritability estimates
for various sensor-derived udder health traits, with heri-
tability estimates ranging from 0.07 to 0.53. Somatic cell
count is a widely used indicator of udder health, with ge-
netic studies showing moderate heritability (0.15–0.32),
suggesting potential for selection to improve mastitis
resistance (Martin et al., 2018; Piwczyński et al., 2021).
Changes in milk electrical conductivity (EC) have also
been proposed as an early indicator of subclinical mas-
titis, as bacterial infections alter the ionic composition
of milk. Studies on Chinese Holstein cows indicate
moderate-to-high heritability of EC (0.46–0.49), but its
genetic correlation with SCC remains limited, suggest-
ing that EC alone is not a fully reliable predictor (Lu et
al., 2024). Other studies have reported heritability esti-
mates for EC traits ranging from 0.22 to 0.53 (Table 1).
Behavioral changes, such as reduced milking speed and
increased milking time, have also been linked to mastitis,
with milking speed exhibiting a genetic correlation of
0.31 with SCC (Piwczyński et al., 2021).
Different studies show that mastitis in dairy cows
results in a change in behavior. The changes in activity
are more unregularly in cows with mastitis (Veissier et
al., 2017) and time of standing is increased (Fogsgaard
et al., 2012). Cows with mastitis have been shown to
have reduced feed intake (Siivonen et al., 2011) and
reduced daily rumination time (Fogsgaard et al., 2015;
Anatanaitis et al., 2022). Studies on genetic correla-
tions between sensor based behavioral traits and udder
health traits are rare, but Moretti et al. (2018) reported
low genetic correlations. In addition to SCC records and
clinical mastitis diagnoses, results of bacteriological milk
analyses provide valuable information regarding udder
health (Suntinger et al., 2022). Although first heritability
analyses showed low heritability, the genetic correlation
with the routinely recorded udder health traits is high.
The use of AMS allows for continuous monitoring
of udder health indicators, including online cell count
(OCC), EC variations, and elevated mastitis risk, pro-
viding valuable data for genetic evaluation and herd
management (Wethal et al., 2020a; Table 1). Wethal et al.
(2020a) assessed the values of maximum and mean EC as
indicators of udder health and suggested OCC to be more
valuable. Given the economic and welfare impacts of
mastitis, incorporating multiple phenotypic and genetic
indicators, including SCC, EC, milking speed, and AMS-
based health markers, could enhance early detection and
genetic selection strategies for improved udder health.
Metabolic Disorders. Wearable biometric sensors,
such as automated health-monitoring systems, continu-
ously collect data on rumination time and physical activ-
ity (Stangaferro et al., 2016). Alterations in patterns of
these parameters can indicate metabolic and digestive
disorders, including displaced abomasum, ketosis, and
indigestion (Rial et al., 2023). Therefore, such variables
can be used for assessing animal health status, early
disease detection, and improving dairy cow management
(Paudyal et al., 2018), even more so when combined with
other available health data (Sturm et al., 2020). Genetic
parameters for sensor-based metabolic disease traits need
to be explored to assess their potential for genetic selec-
tion. Mid-infrared spectroscopy (MIR)-based predictors
for ketosis show potential for screening and preventing
ketosis in dairy herds (Köck et al., 2024). Köck et al.
(2022) estimated heritabilities between 0.16 and 0.30 for
MIR-based predictors (Aceton-MIR, BHB-MIR and Ke-
toMIR) and genetic correlations between 0.60 and 0.73
with BHB measures using a handheld device. Fuerst-
Waltl et al. (2022) analyzed different direct and indirect
traits for ketosis. The genetic correlation between Ke-
toMIR and the veterinarian diagnoses ketosis was >0.90.
Heat Stress. Heat stress in dairy cattle is a major con-
cern as it can result in reduced milk production, impaired
fertility, and increased susceptibility to diseases, leading
to significant economic losses (Polsky and von Keyser -
lingk, 2017). Effective management strategies and genet-
Brito et al.: INVITED REVIEW: SENSOR DATA FOR GENETIC IMPROVEMENT

Journal of Dairy Science Vol. 108 No. 10, 2025
10457Brito et al.: INVITED REVIEW: SENSOR DATA FOR GENETIC IMPROVEMENTTable 4. Heritability estimates for sensor-based rumination time traits in dairy cattle populations
Trait  Sensor type or brand N h2 ± SE Reference
Rumination time (first parity)  SenseHub dairy sensor (Allflex) 142 0.45 ± 0.06 Atashi et al. (2024)
Rumination time (second parity)  SenseHub dairy sensors (Allflex) 243 0.43 ± 0.02 Atashi et al. (2024)
Rumination time (first lactation)  SenseHub dairy sensors (Allflex) 142 0.45 ± 0.06 Atashi et al. (2024)
Rumination time (second parity)  SenseHub dairy sensor (Allflex) 243 0.43 ± 0.02 Atashi et al. (2024)
Rumination time (early)—research herds  Microphone-based rumination monitoring sensor 159 0.14 ± 0.27 Byskov et al. (2017)
Rumination time (late)—research herds  Microphone-based rumination monitoring sensor 159 0.23 ± 0.26 Byskov et al. (2017)
Rumination time (peak)—research herds  Microphone-based rumination monitoring sensor 159 0.44 ± 0.34 Byskov et al. (2017)
Rumination time (total)—research herds  Microphone-based rumination monitoring sensor 159 0.33 ± 0.16 Byskov et al. (2017)
Rumination time (early)—commercial herds  Microphone-based rumination monitoring sensor 10,475 0.29 ± 0.03 Byskov et al. (2017)
Rumination time (peak)—commercial herds  Microphone-based rumination monitoring sensor 10,475 0.28 ± 0.03 Byskov et al. (2017)
Rumination time (mid)—commercial herds  Microphone-based rumination monitoring sensor 10,475 0.32 ± 0.04 Byskov et al. (2017)
Rumination time (late)—commercial herds  Microphone-based rumination monitoring sensor 10,475 0.31 ± 0.04 Byskov et al. (2017)
Rumination time (total)—commercial herds  Microphone-based rumination monitoring sensor 10,475 0.30 ± 0.03 Byskov et al. (2017)
Rumination time  Accelerometer-based neck tag (Lely Qwes HR-LDn) 1,486 0.14 ± 0.04 Sitkowska et al. (2024)
Rumination time  SenseHub collar (Allflex) 453 0.19 ± 0.05 Lemal et al. (2024)
Rumination time  Electronic collar with acoustic sensors (Allflex SCR, Hi Tag) 656
0.45 ± 0.14 Lopes et al. (2024)
Rumination time  Collar with tag (Lely Qwes) 775 0.17 ± 0.06 López-Paredes et al. (2020)
Rumination time (early)  Neck collar with a tag (microphone + 3-axis accelerometer) 710 0.32 Moretti et al. (2018)
Rumination time (mid)  Neck collar with a tag (microphone + 3-axis accelerometer) 710 0.34 Moretti et al. (2018)
Rumination time (late)  Neck collar with a tag (microphone + 3-axis accelerometer) 710 0.35 Moretti et al. (2018)
Rumination Time (weekly)  SMARTBOW ear-tag accelerometer 728
0.25 ± 0.08 Nascimento et al. (2024)
Rumination time (daily) SMARTBOW ear-tag accelerometer 728 0.19 ± 0.06 Nascimento et al. (2024)
Mean, SD and median on the day of milk recording (test day)  Lely 1,289 0.03–0.30 ± 0.01–0.04 Schodl et al. (2023)
Deviation between mean and SD at test day and 5 and 10 d before  Lely 1,289 0.10–0.37 ± 0.01–0.05 Schodl et al. (2023)
Mean, SD, mean SD, and median over 3–305 DIM  Lely 1,289 0.39–0.50 ± 0.06 Schodl et al. (2023)
Mean and SD on day of milk recording (test day)  Lely 834 0.06–0.18 ± 0.03–0.04 Schodl et al. (2022)
Deviation between mean and SD at test day and 5 d before  Lely 834 <0.01–0.04 ± 0.01–0.02 Schodl et al. (2022)
Regression slope of daily mean and SD over 5days before to test day  Lely 834 <0.01–0.04 ± 0.01–0.02 Schodl et al. (2022)
Rumination time  SCR recording system (accelerometer) 77,697 0.32 ± 0.01 to 0.45 ± 0.02 Weller and Ezra (2024)

10458
Journal of Dairy Science Vol. 108 No. 10, 2025
Brito et al.: INVITED REVIEW: SENSOR DATA FOR GENETIC IMPROVEMENT
Table 5. Heritability (h 2) estimates for indicators of fertility derived based on automatically recorded data in dairy cattle populations
Trait  Sensor type N Breed h2 ± SE Reference
Calving to first heat  Herd Navigator (P4) 676 Nordic Red 0.19 ± 0.11 Häggman et al. (2019)
Calving to first heat  Herd Navigator in-line milk progesterone system 2,645 Swedish Red and Holstein 0.18 ± 0.05 Tarekegn et al. (2019)
Commencement of luteal activity  Herd Navigator (P4) 766 Nordic Red 0.24 ± 0.12 Häggman et al. (2019)
Commencement of luteal activity  Herd Navigator in-line milk progesterone system 2,645 Swedish Red and Holstein 0.24 ± 0.04 Tarekegn et al. (2019)
Days from calving to first high activity episode  Electronic activity tag 517 Holstein, Red Dane, Jersey 0.18 ± 0.07 Løvendahl and Chagunda (2009)
Duration of estrus episode  Electronic activity tag 517 Holstein, Red Dane, Jersey 0.05 ± 0.02 Løvendahl and Chagunda (2009)
Estrus period activity variation  SCR Heatime HR system (accelerometer neck tag) 1,070 Holstein 0.11 ± 0.06 Schöpke and W
eigel (2014)
Estrus period average activity  SCR Heatime HR system (accelerometer neck tag) 1,070 Holstein 0.12 ± 0.05 Schöpke and Weigel (2014)
First luteal phase length  Herd Navigator in-line milk progesterone system 2,645 Swedish Red and Holstein 0.08 ± 0.04 Tarekegn et al. (2019)
Interval from calving to first high activity  Automatic milking system (Lely) 8,139 Norwegian Red 0.05 ± 0.01 Heringstad and Wethal (2023)
Interval from commencement of luteal activity to first service  Herd Navigator in-line milk progesterone system 2,645 Swedish Red and Holstein 0.03 ± 0.04 Tarekegn et al. (2019)
Interval from commencement of luteal activity to first service  Herd Navigator in-line milk progesterone system 1,561 Holstein 0.11 ± 0.06 Tenghe et al. (2015)
Length of first interovulatory interval  Herd Navigator in-line milk progesterone system 2,645 Swedish Red and Holstein 0.03 ± 0.04 Tarekegn et al. (2019)
Luteal activity between 25 and 60 DIM  Herd Navigator in-line milk progesterone system 1,561 Holstein 0.06 ± 0.04 Tenghe et al. (2015)
Luteal activity during first 60 DIM  Herd Navigator in-line milk progesterone system 2,645 Swedish Red and Holstein 0.15 ± 0.04 Tarekegn et al. (2019)
MIR-predicted fertility  MIR spectroscopy 4,124 Holstein 0.16 ± 0.03 van den Berg et al. (2021)
Natural log of commencement of luteal activity  Herd Navigator in-line milk progesterone system 1,561 Holstein 0.12 ± 0.05 Tenghe et al. (2015)
Postestrus activity variation  SCR Heatime HR system (accelerometer neck tag) 1,070 Holstein 0.14 ± 0.05 Schöpke and Weigel (2014)
Postestrus average activity  SCR Heatime HR system (accelerometer neck tag) 1,070 Holstein 0.03 ± 0.03 Schöpke and Weigel (2014)
Pre-estrus activity variation  SCR Heatime HR system (accelerometer neck tag) 1,070 Holstein 0.15 ± 0.05 Schöpke and Weigel (2014)
Pre-estrus average activity  SCR Heatime HR system (accelerometer neck tag) 1,070 Holstein 0.05 ± 0.04 Schöpke and Weigel (2014)
Proportion of samples in luteal activity between 25 and 60 DIM  Herd Navigator in-line milk progesterone system 1,561 Holstein 0.12 ± 0.05 Tenghe et al. (2015)
Proportion of samples with luteal activity  Herd Navigator in-line milk progesterone system 2,645 Swedish Red and Holstein 0.13 ± 0.03 Tarekegn et al. (2019)
Regularity of estrus episodes  Electronic activity tag 483 Holstein, Red Dane, Jersey 0.00 ± 0.02 Løvendahl and Chagunda (2009)
Strength of estrus  Electronic activity tag 517 Holstein, Red Dane, Jersey 0.06 ± 0.02 Løvendahl and Chagunda (2009)

Journal of Dairy Science Vol. 108 No. 10, 2025
10459Brito et al.: INVITED REVIEW: SENSOR DATA FOR GENETIC IMPROVEMENT
Table 6. Estimates of heritability (h 2) for traits related to feed intake, feeding behavior, and feed efficiency in dairy cattle populations 1
Trait  Sensor type or brand N Breed  Life stage h2 ± SE Reference
DMI  Feed bins from Biocontrol (weights for roughage intake) 557 Norwegian Red  Lactating cows 0.29 Bakke and Heringstad (2024)
DMI  Electronic feeder (Gallagher) 1,598  to 1,958 Holstein  Lactating cows 0.19 ± 0.04 to
0.36 ± 0.04
Bolormaa et al. (2023)
DMI  Feed bins, feed gates controlled by neck collars  Holstein  Lactating cows 0.32 ± 0.07 to
0.49 ± 0.08
Byskov et al. (2017)
DMI  Automated feed intake system (recorded in AMS) 3,075 Holstein  Lactating cows (P1) 0.32 ± 0.03 Hardie et al. (2017)
DMI  Automated feed intake system (recorded in AMS) 2,667 Holstein  Lactating cows (multiparous) 0.23 ± 0.03 Hardie et al. (2017)
DMI  Electronic feeder 842 Holstein  Dairy heifers (~6 mo) 0.50 ± 0.09 Lin et al. (2013)
DMI  Cattle Feed Intake System (3D cameras) 2,688 Holstein  Lactating cows 0.25 ± 0.02 Manzanilla-Pech et al. (2023)
DMI  Cattle Feed Intake System (3D cameras) 1,378 Jersey  Lactating cows 0.17 ± 0.03 Manzanilla-Pech et al. (2023)
DMI  Cattle Feed Intake System (3D cameras) 1,951 Nordic Red  Lactating cows 0.18 ± 0.02 Manzanilla-Pech et al. (2023)
DMI  Electronic feed recording system 379 Australian dairy
cows
 Lactating cows 0.33 ± 0.13 Richardson et al. (2021)
DMI  Electronic feeding system (RIC system, Insentec) 7,379 Holstein  Lactating cows 0.20–0.37 Stephansen et al. (2023)
RFI  Feed bins, feed gates controlled by neck collars  Holstein  Lactating cows 0.23 ± 0.07 to
0.36 ± 0.08
Byskov et al. (2017)
RFI  Derived from automated feed intake, milk yield, and BW records 2,667  and 3,075
Holstein  Lactating cows 0.13 ± 0.03 and
0.14 ± 0.03
Hardie et al. (2017)
RFI  Electronic feeder (Gallagher) 842 Holstein  Heifers (~6 mo) 0.48 ± 0.09 Lin et al. (2013)
Genetic RFI  Derived from DMI, ECM, and BW data 7,379 Holstein  Lactating cows 0.22–0.34 Stephansen et al. (2023)
Residual energy intake  Derived from AMS records, electronic scale, and n-alkane–based
DMI estimates
1,274 Holstein  Lactating cows 0.08 ± 0.03 Hurley et al. (2017)
Residual energy production  Derived from AMS records, electronic scale, and n-alkane–based
DMI estimates
1,274 Holstein  Lactating cows 0.24 ± 0.05 Hurley et al. (2017)
Net energy intake  Derived from AMS records, electronic scale, and n-alkane–based
DMI estimates
1,274 Holstein  Lactating cows 0.17 ± 0.05 Hurley et al. (2017)
Energy balance  Derived from AMS records, electronic scale, and n-alkane–based
DMI estimates
1,274 Holstein  Lactating cows 0.12 ± 0.04 Hurley et al. (2017)
Duration of each feeder visit  Automated intake recording system 1,328 Holstein  Mid-lactation 0.16 ± 0.03 Cavani et al. (2022)
Duration of each meal  Automated intake recording system 1,328 Holstein  Mid-lactation 0.14 ± 0.02 Cavani et al. (2022)
Energy conversion efficiency  Derived from AMS records, electronic scale, and n-alkane–based
DMI estimates
1,274 Holstein  Lactating cows 0.17 ± 0.05 Hurley et al. (2017)
Feeding duration  Electronic feeder (Gallagher) 842 Holstein  Heifers (~6 mo) 0.45 ± 0.08 Lin et al. (2013)
Feeding interval  AMF 4,572 Holstein  Calves 0.008 ± 0.01 Graham et al. (2024a)
Feeding rate per meal  Automated intake recording system (RIC) 1,328 Holstein  Mid-lactation 0.23 ± 0.03 Cavani et al. (2022)
Feeding rate per visit  Automated intake recording system (RIC) 1,328 Holstein  Mid-lactation 0.11 ± 0.02 Cavani et al. (2022)
Intake per meal  Automated intake recording system (RIC) 1,328 Holstein  Mid-lactation 0.13 ± 0.02 Cavani et al. (2022)
Intake per visit  Automated intake recording system (RIC) 1,328 Holstein  Mid-lactation 0.16 ± 0.03 Cavani et al. (2022)
Number of feeder visits per day  Automated intake recording system (RIC; Hokofarm Group) 1,328 Holstein  Mid-lactation 0.16 ± 0.03 Cavani et al. (2022)
Number of meals per day  Automated intake recording system (RIC) 1,328 Holstein  Mid-lactation 0.09 ± 0.02 Cavani et al. (2022)
Number of meals  Electronic feeder (Gallagher) 842 Holstein  Heifers (~6 mo) 0.40 ± 0.09 Lin et al. (2013)
Per-visit milk consumption  AMF 4,572 Holstein  Calves 0.025 ± 0.01 Graham et al. (2024a)
Average meal size  Electronic feeder (Gallagher) 842 Holstein  Heifers (~6 mo) 0.46 ± 0.09 Lin et al. (2013)
Daily milk consumption  AMF 10,076 Holstein  Calves 0.07 ± 0.01 Graham et al. (2024a)
Daily number of rewarded visits  AMF 10,076 Holstein  Calves 0.03 ± 0.01 Graham et al. (2024a)
Daily sum of drinking duration  AMF 10,076 Holstein  Calves 0.07 ± 0.01 Graham et al. (2024a)
Drinking duration per visit  AMF 4,572 Holstein  Calves 0.02 ± 0.01 Graham et al. (2024a)
Drinking speed  AMF 10,076 Holstein  Calves 0.08 ± 0.01 Graham et al. (2024a)
Total consumption variance  AMF 4,572 Holstein  Calves 0.21 ± 0.02 Graham et al. (2024a)
Total drinking duration variance  AMF 4,572 Holstein  Calves 0.23 ± 0.02 Graham et al. (2024a)
Total duration of feeder visits
per day
 Automated intake recording system (RIC) 1,328 Holstein  Mid-lactation 0.16 ± 0.03 Cavani et al. (2022)
Total number of visits  AMF 10,076 Holstein  Calves 0.05 ± 0.01 Graham et al. (2024a)
13D = 3-dimensional; AMS = automated milking system; AMF = automated milk feeding machine; N = number of cattle; P1 = first parity; RFI = residual feed intake.

10460
Journal of Dairy Science Vol. 108 No. 10, 2025
ic selection for heat tolerance are essential to maintaining
productivity and animal welfare. Several variables can be
measured to assess heat tolerance in dairy cattle, aiding
in genetic selection for improved thermotolerance (Luo
et al., 2021a,b; Hu et al., 2023). Physiological indicators
such as rectal or vaginal temperature, respiration rate,
and sweating rate provide direct measures of an animal’s
ability to dissipate heat. Coat characteristics, including
hair length, coat color, and hair density, influence heat
absorption and retention. Most studies evaluating the
genetic background of heat tolerance in dairy cattle
have focused on variability of performance data (e.g.,
milk yield, fertility) across environmental gradients usu-
ally defined based on data from public weather stations
(Silva Neto et al., 2024; Misztal et al., 2025; Shi et al.,
2025). To our knowledge no estimates of heritability ex-
ist for sensor-derived indicators of heat stress in dairy
cattle. Recent studies have investigated variability in
automatically recorded vaginal temperature in lactating
sows based on random regression models (Wen et al.,
2023) and also derived resilience indicators with moder -
ate heritability estimates (Wen et al., 2024). The same
sensors could be used in dairy cattle studies.
Dairy Cow Behavior
Behavior encompasses a complex set of activities
exhibited by animals in response to various stimuli,
including environmental, social, internal factors, and
human handling. Understanding and quantifying pheno-
typic variability in behavioral traits within dairy cattle
populations is crucial for identifying new traits that can
be incorporated into breeding programs (Pacheco et al.,
2025). As reviewed by Pacheco et al. (2025) and Chang
et al. (2020), dairy cattle exhibit a wide range of behav-
iors throughout their lives, which can be categorized into
several groups. These include, but are not limited to, calf
behavior, feeding and drinking behavior, rumination pat-
terns, estrus expression, reproductive behaviors in both
males and females, responses to milking, interactions
with on-farm technologies, reactions to stressors (such
as heat stress, infectious diseases, nutritional challenges,
and novel objects), maternal behavior, and social interac-
tions. Tables 2, 3, and 4 present heritability estimates for
sensor-based behavioral traits, including activity (Table
3) and rumination traits (Table 4). Heritability estimates
for sensor-based traits tend to be higher than for manu-
ally recorded variables. For instance, using manual ob-
servations of cow behavior across 24 h, Løvendahl and
Munksgaard (2016a) found very low heritabilities for
activity traits (e.g., daily lying time: 0.00 ± 0.10, number
of lying bouts/day: 0.01 ± 0.09; lying bout duration 0.07
± 0.08). However, studies using pedometers or neck col-
lars found higher values (e.g., 0.09 ± 0.05: Schöpke and
Weigel, 2014; 0.23 ± 0.07: Lemal et al., 2024; 0.19 ±
0.06: Nascimento et al., 2024 and see Table 3). This is
likely because the use of sensors allows for continuous
recording for larger numbers of animals across longer
time periods. Interestingly, heritability was higher when
lying was considered over periods longer than a day. This
supports the idea that lying time is elastic and related
to eating time (Løvendahl and Munksgaard, 2016a); to
support high yields, cows must adjust their lying time
within a day to ensure that they have sufficient time to
feed. However, that lying time is an important “need”
that must be fulfilled over the longer term.
Activity. As discussed above, one of the first applica-
tions of sensor technology to dairy farming was the devel-
opment of an activity monitor that detected the rise in ac-
tivity associated with estrus (e.g., Dolecheck et al., 2015).
Wearable collars, ear-tags, or similar accelerometer-based
tools generate data permanently and at relatively low costs
which can be related to welfare and health. The discovery
that activity changes in response to disease and pain led to
the development of systems that predict time of calving,
lameness, and milk fever (Beer et al., 2016; Borchers et
al., 2017; Barraclough et al., 2020).
Feeding and Rumination. Changes in eating, grazing,
and rumination time have also been used to detect poor
health (Simoni et al., 2024). Changes in eating time can
also be used as a measure of heat tolerance (Lemal et al.,
2024). Løvendahl and Munksgaard (2016a) found low to
moderate heritabilities for feeding behavior using manual
observations (daily feeding time: 0.20 ± 0.13, number of
feeding bouts/day: 0.12 ± 0.09; duration of feeding bouts:
0.06 ± 0.09). Estimates of heritability for eating time us-
ing sensors are generally higher (e.g., 0.42 ± 0.09: Atashi
et al., 2024). Estimates for rumination vary somewhat
with the sensor used (between 0.14 to 0.45; see Table 4).
Again, heritability values are typically higher when cal-
culated over a longer time period and not just daily. This
also suggests that the amount of eating and ruminating
within a day may be somewhat flexible, but it is critical
that certain levels are maintained in the longer term.
Personality and Other Behavior Patterns. Underly-
ing traits that affect the expression of behavior, such as
response to milking (milking temperament), have been
shown to have low to moderate heritabilities (e.g., 0.07
± 0.001 Pryce et al., 2000; 0.13 ± 0.01: Sewalem et al.,
2011; see Haskell et al., 2014; Chang et al., 2020; and
Pacheco et al., 2025, for literature reviews). The trait of
“number of kick-offs” is a similar trait measured in AMS.
It also has a low heritability (0.06 ± 0.01; Wethal and
Heringstad, 2019). Many other behavior patterns contrib-
ute to welfare in dairy, such as positive and negative so-
cial interactions in adult cattle and play in calves. Sensor
technology has been used to measure play in calves (e.g.,
Gladden et al., 2020; Vázquez-Diosdado et al., 2024),
Brito et al.: INVITED REVIEW: SENSOR DATA FOR GENETIC IMPROVEMENT

Journal of Dairy Science Vol. 108 No. 10, 2025
10461Brito et al.: INVITED REVIEW: SENSOR DATA FOR GENETIC IMPROVEMENT
Table 7. Heritability estimates for traits related to enteric greenhouse gas emissions by dairy cattle populations
Trait1  Technology type or brand N Breed h2 ± SE Reference
CH4 concentration  Nondispersive infrared methane detector installed in the AMS feed bin 1,501 Holstein 0.11 ± 0.03 López-Paredes et al. (2020)
CH4 concentration, first lactation  Nondispersive infrared CH4 sensor 489 Holstein 0.10–0.28 (±0.05–0.06) Manzanilla-Pech et al. (2022)
CH4 concentration, second lactation  Nondispersive infrared CH4 sensor 368 Holstein 0.13–0.29 (±0.05–0.06) Manzanilla-Pech et al. (2022)
CH4 concentration  Guardian NG infrared gas monitor installed in the feed bin of the AMS 416 Holstein 0.12 ± 0.01 Saborío-Montero et al. (2020)
CH4 concentration (log10(CH4))  Nondispersive infrared sensor in AMS 1,508 Holstein 0.11 ± 0.02 van Engelen et al. (2018)
CH4 concentration (ppm, weekly)  Sniffer 1,800 Holstein 0.32 ± 0.02 van Breukelen et al. (2023)
CH4 concentration (weekly)  Sniffer 4,664 Holstein 0.17 ± 0.04 van Breukelen et al. (2024)
CH4 concentration (ppm, daily)  Sniffer 1,800 Holstein 0.18 ± 0.01 van Breukelen et al. (2023)
CO2 concentration  Nondispersive infrared sensor (SenseAir LPL CH4/CO2, Rise Acreo)
in AMS
1,508 Holstein 0.12 ± 0.02 van Engelen et al. (2018)
CO2 concentration (ppm, daily)  Sniffer 1,800 Holstein 0.20 ± 0.01 van Breukelen et al. (2023)
CO2 concentration (ppm, weekly)  Sniffer 1,800 Holstein 0.32 ± 0.02 van Breukelen et al. (2023)
CH4 conversion factor  Sniffer method integrated in AMS 182 Holstein 0.13 ± 0.13 Uemoto et al. (2024)
CH4 intensity  GreenFeed 265 Holstein 0.21 ± 0.14 Kamalanathan et al. (2023)
CH4 intensity  Noninvasive FTIR analyzer 1,745 Holstein 0.21 ± 0.06 Lassen and Løvendahl (2016)
CH4 intensity  SF6 tracer and daily milk records (MIR) 379 Australian dairy cows 0.33 ± 0.12 Richardson et al. (2021)
CH4 production (g/d)  GreenFeed 1,370 Norwegian Red 0.39 ± Bakke and Heringstad (2024)
CH4 production  Infrared CH4 analyzer in milking robot 184 Holstein 0.12–0.45 Breider et al. (2019)
CH4 production (g/d)  GreenFeed 212 Norwegian Red 0.56 ± 0.20 Heringstad and Bakke (2023)
CH4 production  GreenFeed 330 Holstein 0.16 ± 0.10 Kamalanathan et al. (2023)
CH4 production  Milking robot (FTIR sensor) 339 Holstein 0.24 ± 0.15 Lassen et al. (2016)
CH4 production  GreenFeed 451 Holstein 0.36 ± 0.12 Lopes et al. (2024)
CH4 production  Nondispersive infrared method 1,501 Holstein 0.12 ± 0.04 López-Paredes et al. (2020)
CH4 production, first lactation  Derived from sensor data (Guardian NG; calculated using ECM and
BW)
425 Holstein 0.11–0.49 (±0.07–0.13) Manzanilla-Pech et al. (2022)
CH4 production, second lactation  Derived from sensor data (Guardian NG; calculated using ECM and
BW)
318 Holstein 0.14–0.36 (±0.07–0.13) Manzanilla-Pech et al. (2022)
CH4 production  SF6 tracer method 379 Australian dairy cows 0.16 ± 0.11 Richardson et al. (2021)
CH4 production  GreenFeed 822 Holstein 0.19 ± 0.02 to 0.33 ± 0.04 van Breukelen et al. (2023)
CO2 production (g/d)  GreenFeed 822 Holstein 0.24 ± 0.03 van Breukelen et al. (2023)
CH4 production  FTIR gas analyzer (“sniffer” in AMS) 1,397 Holstein 0.25 ± 0.07 Zetouni et al. (2018)
CH4 production and intensity predicted
from MIR
 Milk mid-infrared spectroscopy (MIR) 231,400  to 336,126 Holstein 0.17 ± 0.01 to 0.25 ± 0.01 Kandel et al. (2017)
CH4 production predicted from MIR  Milk mid-infrared spectroscopy (MIR) 541,565 Holstein 0.23 ± 0.01 Rojas de Oliveira et al. (2024)
CH4 yield  GreenFeed system 287 Holstein 0.27 ± 0.12 Kamalanathan et al. (2023)
CH4 yield  SF6 tracer and electronic feed recording system 379 Australian dairy cows 0.23 ± 0.12 Richardson et al. (2021)
CH4_MILK  Milking robot (FTIR sensor) 339 Holstein 0.26 ± 0.14 Lassen et al. (2016)
CH4_RATIO  Milking robot (FTIR sensor) 339 Holstein 0.09 ± 0.11 Lassen et al. (2016)
CH4/CO2 ratio  Sniffer method integrated in AMS 182 Holstein 0.12 ± 0.14 Uemoto et al. (2024)
CH4/CO2 ratio  Nondispersive infrared sensor (SenseAir LPL CH4/CO2, Rise Acreo)
in AMS
1,508 Holstein 0.03 ± 0.01 Van Engelen et al. (2018)
CH4/CO2 ratio per visit  Sniffer in AMS feed bin 1,746 Holstein 0.01 ± 0.01 van Breukelen et al. (2022)
CH4/CO2 ratio per week  Sniffer in AMS feed bin 1,579 Holstein 0.02 ± 0.01 van Breukelen et al. (2022)
Daily CH4 production  Noninvasive FTIR analyzer 1,745 Holstein 0.21 ± 0.06 Lassen and Løvendahl (2016)
Log-transformed CH4 emissions per visit  Sniffer in AMS feed bin 1,746 Holstein 0.09 ± 0.01 van Breukelen et al. (2022)
Log-transformed CH4 emissions per week  Sniffer in AMS feed bin 1,579 Holstein 0.23 ± 0.03 van Breukelen et al. (2022)
Mean CH4 emissions (ppm) per visit  Sniffer in AMS feed bin 1,746 Holstein 0.13 ± 0.01 van Breukelen et al. (2022)
Mean CH4 emissions (ppm) per week  Sniffer in AMS feed bin 1,579 Holstein 0.32 ± 0.03 van Breukelen et al. (2022)
Median CH4 emissions (ppm) per visit  Sniffer in AMS feed bin 1,746 Holstein 0.13 ± 0.01 van Breukelen et al. (2022)
Median CH4 emissions (ppm) per week  Sniffer in AMS feed bin 1,579 Holstein 0.32 ± 0.03 van Breukelen et al. (2022)
Ratio between CH4 and CO2  Noninvasive FTIR analyzer 3,121 Holstein 0.16 ± 0.04 Lassen and Løvendahl (2016)
1CH4_RATIO = the ratio between CH 4 and CO2 in the breath of the cows; CH4_MILK = grams of CH 4 per liter of milk produced.

10462
Journal of Dairy Science Vol. 108 No. 10, 2025
but heritability has not been estimated. Learning and
behavioral plasticity in cattle has been genetically evalu-
ated using longitudinal docility records (Alvarenga et al.,
2023), but sensors and cameras could be great tools for
deriving cognition and behavioral plasticity traits. The
use of technology to classify and count social interac-
tions has been considered, but further research is needed.
Although the individual behavior patterns appear to have
low heritability, traits do exist that assess overall patterns
of behavior and that are important for animal welfare and
production, which could be monitored via sensor systems
and included in breeding programs.
Animal Resilience
Resilience can be defined based on the ability of
animals to be minimally affected by environmental
disturbances or quickly return to the unperturbed state
(Colditz and Hine, 2016). Dairy cattle are exposed to
multiple stressors throughout their lives, including
thermal stress, injuries and diseases, social stress, and
nutritional stress (Jurkovich et al., 2024). In general,
these stressors negatively affect animal performance
and other traits longitudinally recorded by digital tech-
nologies (e.g., milk yield, feed intake, activity, rumi-
nation time). Therefore, over the past few years, there
has been a great interest in deriving resilience traits
based on longitudinal records in various species. For
instance, several authors have derived resilience based
on variability in milk yield recorded by AMS and parlor
systems (Poppe et al., 2020, 2021; Chen et al., 2023).
These traits are heritable in Holstein cattle populations
with heritability estimates ranging from 0.01 to 0.25
(Poppe et al., 2020, 2021; Chen et al., 2023; Maskal et
al., 2024). Milk losses and variability during environ-
mental perturbations across lactations stages have also
been proposed as resilience indicators and shown to
be genetically correlated with health traits in Holstein
cattle (Wang et al., 2022, 2024). Poppe et al. (2022)
also derived resilience indicators based on daily step
count measured by Nedap Smarttag leg accelerometers
(Nedap, Groenlo, the Netherlands). Heritability esti-
mates were highest for resilience indicators describing
mean step count, from 0.22 for the 2-wk period prepar -
tum to 0.45 for the whole lactation. In dairy calves, Gra-
ham et al. (2024b) derived various resilience indicators
based on variability in milk consumption recorded by
automated milk feeders. The derived resilience indica-
tors quantified the degree and duration of perturbations,
including amplitude, perturbation time, recovery time,
and deviation velocities. Although low, all the derived
calf resilience traits were found to be heritable and
some of them were moderately genetically correlated
with the number of treatments for bovine respiratory
Brito et al.: INVITED REVIEW: SENSOR DATA FOR GENETIC IMPROVEMENT
Table 8. Heritability (h 2) estimates for BW and udder conformation traits derived from automatically recorded data 1
Trait  Sensor type or brand N Breed h2 ± SE Reference
BW  Electronic scale (in AMS) 184 Holstein 0.40–0.67 Breider et al. (2019)
Metabolic BW  Electronic scale (in AMS) 3,075 Holstein 0.51 ± 0.03 Hardie et al. (2017)
Metabolic BW  Electronic scale (in AMS) 2,667 Holstein 0.46 ± 0.03 Hardie et al. (2017)
BW  Cattle Feed Intake System (3D cameras) 2,688 Holstein 0.51 ± 0.04 Manzanilla-Pech et al. (2023)
BW  Cattle Feed Intake System (3D cameras) 1,378 Jersey 0.45 ± 0.04 Manzanilla-Pech et al. (2023)
BW  Cattle Feed Intake System (3D cameras) 1,951 Nordic Red 0.58 ± 0.04 Manzanilla-Pech et al. (2023)
BW  Automated weighing system 7,379 Holstein 0.39–0.52 Stephansen et al. (2023)
Change in BW  Derived from automated weighing system data 7,379 Holstein <0.02 Stephansen et al. (2023)
Weekly average BW, lactation 1  Electronic scale (in AMS) 3,253 Holstein 0.31–0.53 T
ribout et al. (2023)
Weekly average BW, lactation 2  Electronic scale (in AMS) 2,553 Holstein 0.43–0.56 T
ribout et al. (2023)
BW loss from wk 1 to wk 5, lactation 1  Derived from sensor-recorded body weight 3,253 Holstein 0.04 T
ribout et al. (2023)
BW loss from wk 1 to wk 5, lactation 2  Derived from sensor-recorded body weight 2,553 Holstein 0.02 T
ribout et al. (2023)
Udder balance  AMS 4,280 Holstein 0.41 ± 0.02 Medeiros et al. (2024)
Distance front–rear  AMS 4,280 Holstein 0.65 ± 0.02 Medeiros et al. (2024)
Front teat distance  AMS 4,279 Holstein 0.53 ± 0.02 Medeiros et al. (2024)
Rear teat distance  AMS 4,278 Holstein 0.40 ± 0.02 Medeiros et al. (2024)
Udder depth  AMS 4,280 Holstein 0.79 ± 0.01 Medeiros et al. (2024)
Rear teat distance  AMS 12,663 Holstein 0.47 ± 0.02 Poppe et al. (2019)
Front teat distance  AMS 12,663 Holstein 0.60 ± 0.02 Poppe et al. (2019)
Udder depth  AMS 12,663 Holstein 0.69 ± 0.02 Poppe et al. (2019)
Distance front–rear  AMS 12,663 Holstein 0.61 ± 0.02 Poppe et al. (2019)
Udder balance  AMS 12,663 Holstein 0.40 ± 0.02 Poppe et al. (2019)
1AMS = automated milking system.

Journal of Dairy Science Vol. 108 No. 10, 2025
10463
diseases (Graham et al., 2024b). This is an active area
of research and sensors are a great source of data for
deriving such traits.
Fertility and Reproduction Traits
Fertility and reproduction traits are usually lowly heri-
table and highly polygenic (Fleming et al., 2019; Chen
et al., 2022), implying reasonable interest in identifying
novel traits that may be more heritable (Fleming et al.,
2019). Cow activity measurements are widely used in
herd management tools for estrus detection. Therefore,
data from activity sensors can be used to derive novel
traits useful for genetic evaluation of cow fertility, which
reflect the cow’s ability to return to estrus cyclicity and
to show estrus after calving. One example of a trait de-
rived from measures of increased level of activity is the
interval from calving to first high activity (CFHA). Esti-
mated heritability of CFHA range between 0.05 and 0.18
(Løvendahl and Chagunda, 2009; Heringstad and Wethal,
2023; Table 5). Other possibilities could be to define heat
strength from measures of the height and duration of the
increased activity peak. Cow activity data could also be
used to derive traits such as conception rate.
Progesterone in milk is an indicator of cow fertility
and can be used to derive a variety of traits, measuring
different aspects of cow fertility. On-farm technology
such as Herd Navigator (DeLaval Int., Tumba, Sweden),
with in-line systems for automatic sampling and analy-
ses of milk, provides measures of the cow’s estrus and
pregnancy status. Research from Häggman et al. (2019),
Tarekegn et al. (2019), and Tenghe et al. (2015) demon-
strated that information from in-line milk progesterone
measures can be used to define novel fertility traits for
genetic evaluation such as commencement of luteal ac-
tivity, defined as the number of days from calving to the
commencement of luteal activity. Automatic, continuous
recording of cow activity or progesterone in milk may
provide objective and frequent measures of traits related
to different aspects of cow fertility. Traits derived from
such measures would be less affected by herd manage-
ment decisions than traditional fertility traits based on
insemination dates, and these new traits can supplement
or replace current cow fertility traits.
Feed Intake, Feeding Behavior, and Feed Efficiency
Feeding represents one of the largest costs of dairy
cattle production. Therefore, improving feed efficiency
through genomic selection has been a key goal of the
dairy cattle sector over the past few decades. In addi-
tion to feed efficiency traits, feed intake variability and
feeding behavior can be related to health status and other
stressors. For instance, fluctuations in rumination time
and regurgitation frequency can indicate changes in di-
gestion, stress, or disease (Simoni et al., 2023; Hoffmann
et al., 2024). Therefore, such variables can be used for
assessing animal health status, early disease detection,
and improving dairy cow management. Various equip-
ment has been employed for recording feeding related
traits, including 3D cameras and various types of elec-
tronic feeders. Table 6 presents heritability estimates for
various indicators of feed efficiency, feeding behavior,
and feeding intake. Traits such as DMI and residual feed
intake (RFI) are moderately heritable with estimates
ranging from 0.13 to 0.49 (Table 6). It is worth noting
that a cost-effective system based on 3D cameras has
been proposed in Denmark (Cattle Feed Intake System)
with heritability estimates for DMI of 0.25 ± 0.02 in Hol-
stein and 0.17 ± 0.03 in Jersey cattle (Manzanilla-Pech
et al., 2023). Various other feed-related traits have been
derived over time (Table 6), but most dairy breeding pro-
grams have only included feed efficiency traits in their
selection indexes.
Methane Emissions
Breeding is an efficient tool that can be used to re-
duce the environmental footprint of dairy production.
Various methods and sensors for individual measures of
enteric GHG emissions in cattle have been developed,
where “sniffers” installed in AMS feed bins and Green-
Feed systems are most common in genetic studies (Table
7). A common proxy for methane production predicted
from MIR, which has the advantage that it can be used
to generate large amounts of data (Table 7). Heritability
estimates of methane emissions in dairy cows range from
0.10 to 0.39 (Table 7). The substantial genetic variation
for methane emissions illustrates a potential for reducing
methane emissions from dairy cows through breeding.
Body Condition, BW, and Conformation
Body condition and conformation are critical aspects
of dairy cattle management and play a significant role in
many breeding programs. These traits interact with health,
productivity, fertility, and overall welfare of dairy cows
being the reason for issues, but also visible consequences.
The integration of sensor technologies offers new op-
portunities for the accurate and continuous monitoring
of these traits, thereby enhancing genetic evaluations and
breeding decisions. Basic technologies are mostly rely-
ing on 3D Imaging Systems capturing detailed images of
the bodies of cows, allowing for precise measurements of
body condition and conformation traits leading to the pre-
diction of BW. Three-dimensional imaging can be used
to assess body shape, udder depth, teat placement, and
other conformation characteristics. Related technologies
Brito et al.: INVITED REVIEW: SENSOR DATA FOR GENETIC IMPROVEMENT

10464
Journal of Dairy Science Vol. 108 No. 10, 2025
Brito et al.: INVITED REVIEW: SENSOR DATA FOR GENETIC IMPROVEMENT
Table 9. Heritability (h 2) estimates for milking efficiency and milk-related traits derived from automated milking systems (AMS; milking robots) in
dairy cattle populations
Trait N Breed h2 ± SE Reference
Attachment time 1,899 Holstein 0.25 ± 0.007 Piwczyński et al. (2021)
Average flow rate 1,645 Swedish Holstein 0.37 ± 0.06 Carlström et al. (2013)
Average flow rate 1,512 Swedish Holstein 0.40 ± 0.08 Carlström et al. (2013)
Average flow rate 1,447 Swedish Red 0.37 ± 0.07 Carlström et al. (2013)
Average flow rate 1,544 Swedish Red 0.48 ± 0.08 Carlström et al. (2013)
Milk flow rate 1,714 Holstein 0.55 ± 0.14 Dechow et al. (2020)
Milk harvest rate 1,714 Holstein 0.30 ± 0.10 Dechow et al. (2020)
Average milk flow rate 401 Holstein 0.49 ± 0.06 Gäde et al. (2006)
Maximum milk flow rate 401 Holstein 0.55 ± 0.05 Gäde et al. (2006)
Average milk flow rate 4,507 Holstein 0.43 to 0.52 Pedrosa et al. (2023)
Maximum milk flow rate 4,507 Holstein 0.47 to 0.58 Pedrosa et al. (2023)
Flow rate 4,883 Norwegian Red 0.48 ± 0.04 Wethal and Heringstad (2019)
Box time 1,645 Swedish Holstein 0.21 ± 0.05 Carlström et al. (2013)
Box time 1,512 Swedish Holstein 0.24 ± 0.07 Carlström et al. (2013)
Box time 1,447 Swedish Red 0.38 ± 0.06 Carlström et al. (2013)
Box time 1,544 Swedish Red 0.44 ± 0.07 Carlström et al. (2013)
Box time 1,053 Swedish Holstein 0.24 Carlström et al. (2014)
Box time 1,749 Swedish Red 0.45 Carlström et al. (2014)
Box time 2,258 Holstein 0.25 ± 0.05 Løvendahl and Buitenhuis (2022)
Box time 2,407 Jersey 0.27 ± 0.05 Løvendahl and Buitenhuis (2022)
Box time 1,486 Holstein 0.21 ± 0.03 Sitkowska et al. (2024)
Box time 4,883 Norwegian Red 0.27 ± 0.03 Wethal and Heringstad (2019)
Connection time 27,726 Danish Holstein (including Danish Red
Holstein)
0.36 ± 0.02 Stephansen et al. (2018)
Handling time 4,883 Norwegian Red 0.05 ± 0.01 Wethal and Heringstad (2019)
Incomplete milkings 1,714 Holstein 0.03 ± 0.01 Dechow et al. (2020)
Incomplete milkings 4,883 Norwegian Red 0.01 ± 0.005 Wethal and Heringstad (2019)
Leakage 66,743 Norwegian Red 0.04 ± 0.01 Wethal et al. (2020a)
Milk yield 1,713 Holstein 0.25 ± 0.05 Aerts et al. (2021)
305-d mature-equivalent
 milk yield
1,714 Holstein 0.30 ± 0.02 Dechow et al. (2020)
Milk yield (5 to 70 d postpartum) 670 Nordic Red 0.29 ± 0.13 Häggman et al. (2019)
Milk yield 401 Holstein 0.20 ± 0.03 Gäde et al. (2006)
Daily milk yield 953 Holstein 0.14–0.20 Nixon et al. (2009)
Daily milk yield 4,507 Holstein 0.07 to 0.28 Pedrosa et al. (2023)
Daily milking frequency 953 Holstein 0.02–0.08 Nixon et al. (2009)
Milking efficiency 4,506 Holstein 0.45 to 0.56 Pedrosa et al. (2023)
Milking frequency 1,713
Holstein 0.23 ± 0.04 Aerts et al. (2021)
Milking failures 4,511 Holstein 0.02 ± 0.01 Pedrosa et al. (2023)
Milking efficiency 1,486 Holstein 0.35 ± 0.01 Sitkowska et al. (2024)
Milking efficiency 4,883 Norwegian Red 0.22 ± 0.03 Wethal and Heringstad (2019)
Milking frequency 2,258 Holstein 0.22 ± 0.04 Løvendahl and Buitenhuis (2022)
Milking frequency 2,407 Jersey 0.17 ± 0.04 Løvendahl and Buitenhuis (2022)
Milking frequency 1,899 Holstein 0.51 ± 0.01 Piwczyński et al. (2021)
Milking frequency 4,883 Norwegian Red 0.05 ± 0.01 Wethal and Heringstad (2019)
Milking frequency (DIM 0–99 d) 1,216 Not reported (dairy cattle) 0.16 ± 0.04 König et al. (2006)
Milking frequency
 (DIM 100–199 d)
1,112 Not reported (dairy cattle) 0.19 ± 0.05 König et al. (2006)
Milking frequency

 (DIM 200–299 d)
1,004 Not reported (dairy cattle) 0.22 ± 0.05 König et al. (2006)
Test-day milking frequency 543 Holstein 0.14 ± 0.01
Nixon et al. (2009)
Milking interval 1,645 Swedish Holstein 0.26 ± 0.05 Carlström et al. (2013)
Milking interval 1,512 Swedish Holstein 0.17 ± 0.05 Carlström et al. (2013)
Milking interval 1,447 Swedish Red 0.09 ± 0.03 Carlström et al. (2013)
Milking interval 1,544 Swedish Red 0.23 ± 0.05 Carlström et al. (2013)
Milking interval 4,883 Norwegian Red 0.02 ± 0.01 Wethal and Heringstad (2019)
Milking refusals 4,511 Holstein 0.09 ± 0.01 Pedrosa et al. (2023)
Milking speed 1,713 Holstein 0.42 ± 0.07 Aerts et al. (2021)
Milking speed 1,899 Holstein 0.43 ± 0.01 Piwczyński et al. (2021)
Milking speed 1,486 Holstein 0.36 ± 0.05 Sitkowska et al. (2024)
Milking speed 72,487 Norwegian Red 0.22 ± 0.01 Wethal et al. (2020)
Milking time 1,714 Holstein 0.26 ± 0.04 Dechow et al. (2020)
Milking time 401 Holstein 0.38 ± 0.03 Gäde et al. (2006)
Milking time 4,507 Holstein 0.22 to 0.28 Pedrosa et al. (2023)
Milking time 1,899 Holstein 0.31 ± 0.01 Piwczyński et al. (2021)
Continued

Journal of Dairy Science Vol. 108 No. 10, 2025
10465
generation spatial coordinated allow, automatically dur -
ing AMS milking, to acquire udder conformation traits,
which were already considered for use in genetic evalu-
ations in several countries (Poppe et al., 2019; Medeiros
et al., 2024) because of its low costs (i.e., no need to send
an appraiser) and good integration in the development of
AMS systems. Advanced technologies are also automated
BCS systems using cameras and image analysis software
to automatically score body condition with numerous
contributions in the last 20 yr (e.g., Bewley et al., 2008b;
Hernandez-Gotelli et al., 2023). They provide consistent
and objective assessments, reducing the variability asso-
ciated with manual scoring. Moreover, efforts are ongo-
ing to estimate BW, BCS, and type traits in dairy cows
using 3D cameras but also integrating them with manual
body measurements (e.g., Martins et al., 2020). Finally,
indirectly through devices such as accelerometers and
pedometers, one can monitor cow activity and movement
patterns, providing indirect indicators of body condition
and conformation defects as leg health. Changes in activ-
ity levels and movement patterns can signal issues such as
lameness (Nejati et al., 2023) or discomfort then leading
to lower BCS. As shown in Table 8, BW and body confor -
mation traits have moderate to high heritability estimates,
ranging from 0.31 to 0.79 (Table 8).
Milk Production and Milking Efficiency
Automated milking systems facilitate the continuous
monitoring of various traits related to lactation perfor -
mance and animal behavior, providing valuable data for
both management and genetic selection. With the wide
adoption of AMS in dairy farms, such datasets are being
generated in large scale. In addition to milk yield, other
traits related to milking efficiency are of great interest,
including milking speed or flow rate, box time, number of
incomplete milkings, milking interval, milking failures,
and milking refusals. As shown in Table 9, most traits re-
lated to milk yield and milking efficiency have moderate
heritability estimates, indicating that genetic selection for
improved performance in robotic dairy farms is feasible.
DATA ACCESS, OWNERSHIP, STORAGE,
AND INFRASTRUCTURE
Effective genetic evaluations and breeding programs
incorporating data from sensors and other technolo-
gies are based on large-scale datasets. The storage and
management of data for dairy cattle genetic evaluations
require a robust and scalable infrastructure capable of
handling large and multidimensional datasets (Wangen
et al., 2021). As large amounts of data are generated, an
important step is the definition of the variables and data
that should be stored for long-term usage to ensure con-
sistency, relevance, and efficiency in genetic evaluations.
The primary challenges include ensuring data integrity,
security, and accessibility while maintaining computa-
tional efficiency for real-time or near-real-time analyses.
High-throughput storage solutions, such as distributed
databases and cloud-based platforms, are essential to ac-
commodate the continuous influx of genomic and pheno-
typic data from diverse sources. Additionally, standard-
ized data formats and interoperability frameworks are
necessary to facilitate seamless integration and analyses
across research institutions, breeding organizations, and
industry stakeholders. Efficient indexing, redundancy
mechanisms, and scalable computing resources are criti-
cal to optimizing data retrieval and processing for ac-
curate and timely genetic evaluations. However, many
factors must be considered before a structured data flow
system can be incorporated into genetic evaluations. This
includes regulatory considerations such as data access
and portability rights, data access modalities (automatic
and secure data transfer pipelines on site or off site), data
storage (format, resolution), data governance, robust data
security, and ethical considerations. Therefore, a need
exists for clear data sharing agreements, which include
the above-mentioned points for parties involved in data
generation. Stakeholders (with support from regulatory
agencies) should foster trust and develop business mod-
els that are of mutual benefit. Examples of stakeholders
include dairy farmers, DHIA organizations, technology
providers, ICAR, universities, and other research organi-
Brito et al.: INVITED REVIEW: SENSOR DATA FOR GENETIC IMPROVEMENT
Trait N Breed h2 ± SE Reference
Natural logarithm of number of
attachments per teat
27,726 Danish Holstein (including Danish Red
Holstein)
0.26 ± 0.02 Stephansen et al. (2018)
Number of milkings 1,447 to 1,645 Swedish Holstein and Swedish Red 0.02 ± 0.01 to
0.07 ± 0.01
Carlström et al. (2013)
Number of milkings 1,714 Holstein 0.07 ± 0.02 Dechow et al. (2020)
Incomplete milkings 4,883 Norwegian Red 0.14 ± 0.03 Wethal and Heringstad (2019)
Milkings with teat not found 4,883 Norwegian Red 0.12 ± 0.03 Wethal and Heringstad (2019)
Rejected milkings 4,883 Norwegian Red 0.05 ± 0.02 Wethal and Heringstad (2019)
Teat not found 4,883 Norwegian Red 0.002 ± 0.004 Wethal and Heringstad (2019)
Table 9 (Continued). Heritability (h 2) estimates for milking efficiency and milk-related traits derived from automated milking systems (AMS;
milking robots) in dairy cattle populations

10466
Journal of Dairy Science Vol. 108 No. 10, 2025
zations, breeding companies, national genetic evaluation
centers, and others.
In general, dairy producers own and control the use of
data generated in their herds, including genomic infor -
mation, and access to their data is regulated by agree-
ments signed with DHIA service providers, research
organizations, or other institutions. However, getting
access to data sets from on-farm technologies in the first
place usually require agreements between relevant stake-
holders for the specific purpose, good data governance
practices, and efficient computing infrastructure.
The use of sensor-derived data for genetic improvement
introduces critical questions about legal data allocation
(commonly called “data ownership”) and the allocation of
the results of data sharing, intellectual property rights, and
privacy. Although farmers generate and manage these data
streams through on-farm technologies, access and porta -
bility rights become ambiguous when the farmer generates
data, which it does not control factually because they are
“possessed” by the manufacturer. The lack of explicit data

governance frameworks poses risks of data misuse, re -
stricted farmer access, and inequitable value distribution.
Therefore, ensuring that farmers retain appropriate control
over their sensor data while enabling its use for genetic
advancements is essential to fostering trust and maximiz -
ing industry benefits (Barton et al., 2025).
As the role of sensor data in genetic evaluations expands,
the need for standardized policies on data access, sharing,
and monetization becomes increasingly important. Regu-
latory frameworks in Europe, such as the General Data
Protection Regulation for personal data and the upcoming
Data Act as a horizontal regulation for user access to all
Internet of Things data and the Data Governance Act as
data governance regulation, will facilitate data sharing in
the future while preserving privacy of personal data and
trade secrets, and creating trust in data sharing. Without
clear policies, farmers risk losing control over their sen-
sor-derived data, potentially leading to restricted access
to genetic insights derived from their own contributions.
Transparent policies and contracts should define access
and portability rights, provide mechanisms for opt-in or
opt-out participation, and ensure equitable value distribu-
tion among all stakeholders (Majcen, 2022; Barton et al.,
2025). To efficiently integrate new traits into large-scale
breeding programs, several technical and legal problems
need to be resolved, especially when it comes to interop-
erability and data governance.
ROADMAP FOR USING SENSOR DATA
FOR GENETIC EVALUATIONS
For the efficient implementation of routine genetic and
genomic evaluations, collaboration among various stake-
holders and organizations is essential. At the core of this
process is the commitment of dairy farmers, whose ac-
tive participation ensures the availability of sensor data
for downstream analyses, which also allows reliability
checking of the automated data collection. As sensor
technologies become more widespread, dairy farmers
may also seek to monetize their data, potentially making
agreements with research organizations, national genetic
evaluation centers, or even selling their data to private
dairy breeding companies that are developing reference
populations for novel traits. However, the benefit from
reliable genetic and genomic evaluations has sustained
the routine centralized data processing, and it is not yet
clear whether the availability of new data sources such
as sensor technology will, in the long term, lead to split
of data flow and limited data sharing with the established
national evaluation centers.
As datasets are generated, pipelines must be devel-
oped for routine gathering and integration of the sensor
data, with frequent data delivery or real-time data flow
to a central platform. The DHIA organizations play a
crucial role in the routine collection, aggregation, and
analyses of recorded variables. As trusted data handlers
with long-term experience in data management, they
are well positioned to facilitate the integration of sen-
sor data into genetic evaluations. The network of DHIA
organizations and related computation centers provide
the required infrastructure for data governance, enabling
benchmarking and sectoral analyses while maintaining
neutrality across different sensor brands and models.
Their strong connections with governmental and breed-
ing organizations further enhance their capacity to
standardize and validate sensor-derived information.
To maximize the benefits of sensor data integration,
well-documented metadata, and clear guidelines for data
editing, control, and analyses under routine conditions
must be established. Implementing data governance
principles based on fairness and transparency is essen-
tial for building long-term trust among farmers, dairy
sector stakeholders (e.g., DHIA, breeding organizations,
companies, breed associations, national genetic evalua-
tion centers), and research institutions. In this context,
acknowledged international bodies, such as ICAR, must
provide the framework for ensuring interoperability
and consistency across data sources, including guide-
lines and reference standards to promote the effective
use of sensor data in genetic and genomic evaluations.
Standards for data recording and use are developed and
agreed upon by experts and include consensus on how
to better integrate, edit, and use the different types of
automatically recorded data. However, the development
of such standards and guidelines implies reasonable ef-
forts and requires collaboration and agreement between
different stakeholders. Therefore, working groups such
as the ICAR-IDF Sensor Initiative (Egger-Danner et al.,
Brito et al.: INVITED REVIEW: SENSOR DATA FOR GENETIC IMPROVEMENT

Journal of Dairy Science Vol. 108 No. 10, 2025
10467
2024) are valuable to meet these goals. Standards facili-
tate cooperation between stakeholders and result in more
efficient data exchange and use, improved interpretation
and more consistent results (Baldin et al., 2025).
All the integrated data needs to be securely stored in
central databases for performing genetic and genomic
analyses and routine genetic evaluations. For instance,
producers-owned central databases could be essential for
advancing the dairy sector, making neutral benchmarks
available, ensuring autonomy from international provid-
ers, and enabling collective research as well as genetic
progress through reliable comprehensive evaluation
systems. The datasets available can be used for deriving
novel traits for refining selection indexes. Data editing,
processing, and integration should be highly automa-
tized. After the traits of interest are derived, variance
components should be (re)estimated on a regular basis.
Genomic evaluations are then performed, followed by
aggregation of the (G)EBVs in selection indexes, which
are reported to breeding organizations and dairy farmers
as basis for selection and culling decisions at the farm
and population levels.
Finally, the optimal use of sensor data in dairy genetics
requires continuous advancements in education and pro-
fessional training. The next generation of professionals,
including breeders, farm managers, and veterinarians,
must be equipped with the knowledge how to make best
use of the wealth of information becoming regularly
available. Having animal science expertise and strong
data science skills is helpful and may become a prerequi-
site for successful dairy farm management in the future.
Strengthening these capacities will ensure that sensor
data are effectively leveraged for improving genetic
evaluations and overall efficiency of the dairy sector.
CONCLUSIONS
The integration of sensor technologies into dairy cattle
breeding offers a major opportunity to enhance genetic
evaluations and accelerate progress in traits linked to
health, welfare, and sustainability. High-frequency, ob-
jective data from automated systems enable more precise
selection criteria and improved evaluation reliability.
Realizing this potential requires overcoming challenges
in data harmonization, standardization, access, and gov-
ernance. Transparent sharing frameworks, stakeholder
collaboration, and robust quality control are essential.
Global bodies like ICAR and IDF are key to developing
guidelines that ensure interoperability. Success will also
depend on policies that balance data ownership, privacy,
and fair value, along with scalable infrastructure, artifi-
cial intelligence–driven analytics, and professional train-
ing. By addressing these needs and fostering innovation,
the dairy sector can leverage precision livestock farming
to boost productivity, improve welfare, and advance sus-
tainable breeding, transforming dairy herd improvement
into a more efficient, data-driven process worldwide.
NOTES
Luiz Brito received funding from the Agriculture and
Food Research Initiative Competitive Grant number
2022-67021-37022 from the USDA National Institute
of Food and Agriculture (Washington, DC) and support
from the Purdue College of Agriculture and Purdue Ag
Data Services (West Lafayette, IN) for developing the
Purdue Animal Sciences Data Ecosystem (PASDE; Boer -
man et al., 2025). Anna Stygar received financial support
from the European Union’s Horizon Europe Coordina-
tion and Support Action under grant agreement number
101134866 (project Digi4Live). Christa Egger-Danner
acknowledges the COMET-Project D4Dairy (Digitalisa-
tion, Data integration, Detection and Decision support in
Dairying, project number: 872039), which was supported
by the Federal Ministry of Mobility, Innovation, and In-
frastructure (BMINI, Vienna, Austria) and the Federal
Ministry of Economy, Energy, and Tourism (BMWET,
Vienna, Austria) from the Republic of Austria, and the
provinces of Lower Austria and Vienna in the framework
of the Competence Centers for Excellent Technologies
(COMET). The COMET program is handled by the
Austrian Research Promotion Agency (FFG, Vienna,
Austria; grant number 872039). The experiences and
lessons learned from the D4Dairy project were the basis
for Christa Egger-Danner, Chair of the ICAR FTWG, to
initiate the ICAR IDF Sensor Initiative (Egger-Danner et
al., 2024) together with Ilka Klaas of the IDF Standing
Committee on Animal Health and Welfare. The authors
thank all colleagues, scientists, manufacturers, represen-
tatives from ICAR members and working groups, espe-
cially Robert Fourdraine and Steven J. Sievert, and other
stakeholder organizations for many fruitful discussions
and contributions to the work of the ICAR IDF FTWG on
the topic of sensor data use. We also thank Patrick Majcen
for their contribution on the legal aspects of data sharing.
No human or animal subjects were used, so this analysis
did not require approval by an Institutional Animal Care
and Use Committee or Institutional Review Board. The
authors have not stated any conflicts of interest.
Nonstandard abbreviations used: CH4_RATIO = the
ratio between CH 4 and CO 2 in the breath of the cows;
CH4_MILK = grams of CH 4 per liter of milk produced;
3D = 3-dimensional; AMF = automated feeding machine;
AMS = automated milking systems; CFHA = calving to
first high activity; EC = electrical conductivity; FTIR =
Fourier-transform infrared spectroscopy; FTWG = Func-
tional Traits Working Group; ICAR = International Com-
Brito et al.: INVITED REVIEW: SENSOR DATA FOR GENETIC IMPROVEMENT

10468
Journal of Dairy Science Vol. 108 No. 10, 2025
mittee on Animal Recording; IDF = International Dairy
Federation; MIR = mid-infrared spectroscopy; OCC =
online cell count; RFI = residual feed intake.
REFERENCES
Aerts, J., D. Piwczyński, H. Ghiasi, B. Sitkowska, M. Kolenda, and
H. Önder. 2021. Genetic parameters estimation of milking traits in
Polish Holstein-Friesians based on automatic milking system data.
Animals (Basel) 11:1943. https:  / / doi .org/ 10 .3390/  ani11071943.
Alvarenga,
A. B., H. R. Oliveira, S. P. Turner, A. Garcia, K. J. Retallick,
S. P. Miller, and L. F. Brito. 2023. Unraveling the phenotypic and
genomic background of behavioral plasticity and temperament in
North American Angus cattle. Genet. Sel. Evol. 55:3. https:  / / doi .org/
10 .1186/ s12711 -023 -00777  -3.
Antanaitis, R.,
V . Juozaitienė, D. Malašauskienė, M. Televičius, M. Ur -
butis, A. Rutkaukas, and G. Šertvytytė., and w. Baumgartner. 2022.
Identification of changes in rumination behavior registered with an
online sensor system in cows with subclinical mastitis. Vet. Sci.
9:454. https:  / / doi .org/ 10 .3390/  vetsci9090454.
Atashi, H., P. Lemal, M.-N.
Tran, and N. Gengler. 2024. Estimation of
genetic parameters and single-step genome-wide association studies
for eating time and rumination time in Holstein dairy cows. J. Dairy
Sci. 107:3006–3019. https:  / / doi .org/ 10 .3168/  jds .2023  -23790.
Bakke, K., and B. Heringstad. 2024. Genetic correlations between daily
dry matter intake, body weight, and enteric methane in Norwegian

Red. Interbull Bull. 60. Proc. 2024 Interbull Meeting. Accessed Feb.
2, 2025. https:  / / journal  .interbull  .org/ index  .php/ ib/ article/  view/  1934.
Baldin, M.,
J. M. Bewley, V . E. Cabrera, K. Jones, C. Loehr, G. Mazon,
J. D. Perez, M. Utt, and J. Weyers. 2025. Standardization for data
generation and collection in the dairy industry: Addressing chal-
lenges and charting a path forward. Animals (Basel) 15:250. https:  / /
doi .org/ 10 .3390/  ani15020250.
Barraclough, R. A. C., D. J. Shaw
, V . M. Thorup, M. J. Haskell, W. Lee,
and A. I. Macrae. 2020. The behavior of dairy cattle in the transition
period: Effects of blood calcium status. J. Dairy Sci. 103:10604–
10613. https:  / / doi .org/ 10 .3168/  jds .2020 -18238.
Barton, R., J. Burchard, V
. E. Cabrera, D. Cook, W. Cooley, R. Cue, L.
Fadul, J. Mattison, and A. Saha. 2025. Data ownership and privacy
in dairy farming: Insights from U.S. and global perspectives. Ani-
mals (Basel) 15:524. https:  / / doi .org/ 10 .3390/  ani15040524.
Beer, G., M.
Alsaaod, A. Starke, G. Schuepbach-Regula, H. Müller, P.
Kohler, and A. Steiner. 2016. Use of extended characteristics of lo-
comotion and feeding behavior for automated identification of lame
dairy cows. PLoS One 11:e0155796. https:  / / doi .org/ 10 .1371/  journal
.pone  .0155796.
Bérat, H., N. Gengler, J. M. Maskal, J. P
. Boerman, and L. F. Brito. 2025.
Investigating the genetic background of novel behavioral indicators
of robotic milking efficiency in North American Holstein cattle. J.
Dairy Sci. 108:7262–7277. https:  / / doi .org/ 10 .3168/  jds .2024 -25597.
Bewley, J. M., M. E. Einstein, M.
W. Grott, and M. M. Schutz. 2008a.
Comparison of reticular and rectal core body temperatures in lactat-
ing dairy cows. J. Dairy Sci. 91:4661–4672. https:  / / doi .org/ 10 .3168/
jds .2007  -0835.
Bewley, J. M.,
A. M. Peacock, O. Lewis, R. E. Boyce, D. J. Roberts, M.
P. Coffey, S. J. Kenyon, and M. M. Schutz. 2008b. Potential for esti-
mation of body condition scores in dairy cattle from digital images.
J. Dairy Sci. 91:3439–3453. https:  / / doi .org/ 10 .3168/  jds .2007  -0836.
Boerman, J. P., L. F
. Brito, M. E. Montes, J. M. Maskal, J. Doucette, and
K. Kalbaugh. 2025. Technical Note: Data processing techniques to
improve data integration from dairy farms. JDS Commun. 6:339–
344. https:  / / doi .org/ 10 .3168/  jdsc2024  -0723.
Bolormaa, S., M. Haile-Mariam, L. C. Marett, F. Miglior
, C. F. Baes, F.
S. Schenkel, E. E. Connor, C. I. V . Manzanilla-Pech, E. Wall, M. P.
Coffey, M. E. Goddard, I. M. MacLeod, and J. E. Pryce. 2023. Use of
dry-matter intake recorded at multiple time periods during lactation
increases the accuracy of genomic prediction for dry-matter intake
and residual feed intake in dairy cattle. Anim. Prod. Sci. 63:1113–
1125. https:  / / doi .org/ 10 .1071/  AN23022.
Borchers, M. R., Y
. M. Chang, K. L. Proudfoot, B. A. Wadsworth, A.
E. Stone, and J. M. Bewley. 2017. Machine-learning-based calving
prediction from activity, lying, and ruminating behaviors in dairy
cattle. J. Dairy Sci. 100:5664–5674. https:  / / doi .org/ 10 .3168/  jds
.2016 -11526.
Breider
, I. S., E. Wall, and P. C. Garnsworthy. 2019. Short communica-
tion: Heritability of methane production and genetic correlations
with milk yield and body weight in Holstein-Friesian dairy cows. J.
Dairy Sci. 102:7277–7281. https:  / / doi .org/ 10 .3168/  jds .2018  -15909.
Brito, L. F., H. R. Oliveira, B. R. McConn,
A. P. Schinckel, A. Arra-
zola, J. N. Marchant-Forde, and J. S. Johnson. 2020. Large-scale
phenotyping of livestock welfare in commercial production systems:
A new frontier in animal breeding. Front. Genet. 11:793. https:  / / doi
.org/ 10 .3389/  fgene .2020  .00793.
Byskov, M.
V ., A. Fogh, and P. Løvendahl. 2017. Genetic parameters
of rumination time and feed efficiency traits in primiparous Hol-
stein cows under research and commercial conditions. J. Dairy Sci.
100:9635–9642. https:  / / doi .org/ 10 .3168/  jds .2016 -12511.
Cabrera,
V . E., J. A. Barrientos-Blanco, H. Delgado, and L. Fadul-
Pacheco. 2020. Symposium review: Real-time continuous decision
making using big data on dairy farms. J. Dairy Sci. 103:3856–3866.
https:  / / doi .org/ 10 .3168/  jds .2019 -17145.
Carlström, C., G. Pettersson, K. Johansson, E. Strandberg, H. Stålham
-
mar, and J. Philipsson. 2013. Feasibility of using automatic milking
system data from commercial herds for genetic analysis of milk-
ability. J. Dairy Sci. 96:5324–5332. https:  / / doi .org/ 10 .3168/  jds .2012
-6221.
Carlström, C., E. Strandberg, K. Johansson, G. Pettersson, H. Stålham-
mar
, and J. Philipsson. 2014. Genetic evaluation of in-line recorded
milkability from milking parlors and automatic milking systems. J.
Dairy Sci. 97:497–506. https:  / / doi .org/ 10 .3168/  jds .2013  -6948.
Cavani, L., W
. E. Brown, K. L. Parker Gaddis, R. J. Tempelman, M. J.
VandeHaar, H. M. White, F. Peñagaricano, and K. A. Weigel. 2022.
Estimates of genetic parameters for feeding behavior traits and their
associations with feed efficiency in Holstein cows. J. Dairy Sci.
105:7564–7574. https:  / / doi .org/ 10 .3168/  jds .2022 -22066.
Cerri, R. L. A.,
T. A. Burnett, A. M. L. Madureira, B. F. Silper, J. Denis-
Robichaud, S. LeBlanc, R. F. Cooke, and J. L. M. Vasconcelos. 2021.
Symposium review: Linking activity-sensor data and physiology to
improve dairy cow fertility. J. Dairy Sci. 104:1220–1231. https:  / / doi
.org/ 10 .3168/  jds .2019  -17893.
Chang, Y
., L. F. Brito, A. B. Alvarenga, and Y . Wang. 2020. Incorporat-
ing temperament traits in dairy cattle breeding programs: Challenges
and opportunities in the phenomics era. Anim. Front. 10:29–36.
https:  / / doi .org/ 10 .1093/  af/ vfaa006.
Chen, S.-Y ., J. P
. Boerman, L. S. Gloria, V . B. Pedrosa, J. Doucette, and
L. F. Brito. 2023. Genomic-based genetic parameters for resilience
across lactations in North American Holstein cattle based on vari-
ability in daily milk yield records. J. Dairy Sci. 106:4133–4146.
https:  / / doi .org/ 10 .3168/  jds .2022 -22754.
Chen, S. Y
., F. S. Schenkel, A. L. Melo, H. R. Oliveira, V . B. Pedrosa, A.
C. Araujo, M. G. Melka, and L. F. Brito. 2022. Identifying pleiotro-
pic variants and candidate genes for fertility and reproduction traits
in Holstein cattle via association studies based on imputed whole-
genome sequence genotypes. BMC Genomics 23:331. https:  / / doi
.org/ 10 .1186/ s12864  -022 -08555  -z.
Chicco, D., L. Oneto, and E. T
avazzi. 2022. Eleven quick tips for data
cleaning and feature engineering. PLOS Comput. Biol. 18:e1010718.
https:  / / doi .org/ 10 .1371/  journal  .pcbi  .1010718.
Colditz, I. G., and B. C. Hine. 2016. Resilience in farm animals: Biology,

management, breeding and implications for animal welfare. Anim.
Prod. Sci. 56:1961. https:  / / doi .org/ 10 .1071/  AN15297.
Dawkins, M. S. 2021. Does smart farming improve or damage animal
welfare?
Technology and what animals want. Front. Anim. Sci.
2:736536. https:  / / doi .org/ 10 .3389/  fanim  .2021  .736536.
Dechow, C. D., K. S. Sondericker
, A. A. Enab, and L. C. Hardie. 2020.
Genetic, farm, and lactation effects on behavior and performance
of US Holsteins in automated milking systems. J. Dairy Sci.
103:11503–11514. https:  / / doi .org/ 10 .3168/  jds .2020 -18786.
Denwood, M. J., J. L. Kleen, D. B. Jensen, and N. N. Jonsson. 2018.
Describing temporal variation in reticuloruminal pH using continu
-
Brito et al.: INVITED REVIEW: SENSOR DATA FOR GENETIC IMPROVEMENT

Journal of Dairy Science Vol. 108 No. 10, 2025
10469
ous monitoring data. J. Dairy Sci. 101:233–245. https:  / / doi .org/ 10
.3168/  jds .2017  -12828.
Dervić, E.,
C. Matzhold, C. Egger-Danner, F. Steininger, and P. Klimek.
2024. Improving lameness detection in cows: A machine learning
algorithm application. J. Dairy Sci. 107:11550–11562. https:  / / doi
.org/ 10 .3168/  jds .2024 -24730.
Dolecheck, K. A.,
W. J. Silvia, G. Heersche Jr., Y . M. Chang, D. L. Ray,
A. E. Stone, B. A. Wadsworth, and J. M. Bewley. 2015. Behavioral
and physiological changes around estrus events identified using
multiple automated monitoring technologies. J. Dairy Sci. 98:8723–
8731. https:  / / doi .org/ 10 .3168/  jds .2015 -9645.
Džermeikaitė, K.,
D. Bačėninaitė, and R. Antanaitis. 2023. Innovations
in cattle farming: Application of innovative technologies and sensors
in the diagnosis of diseases. Animals (Basel) 13:780. https:  / / doi .org/
10 .3390/  ani13050780.
Egger-Danner
, C., J. B. Cole, J. E. Pryce, N. Gengler, B. Heringstad,
A. Bradley, and K. F. Stock. 2015. Invited review: Overview of
new traits and phenotyping strategies in dairy cattle with a focus
on functional traits. Animal 9:191–207. https:  / / doi .org/ 10 .1017/
S1751731114002614.
Egger
-Danner, C., I. Klaas, L. Brito, K. Schodl, J. M. Bewley, V . Ca-
brera, M. J. Haskell, M. Iwersen, B. Heringstad, K. Stock, A. Stygar,
R. van der Linde, M. Hostens, N. Charfeddine, N. Gengler, and E.
Vasseur. 2024. Improving animal health and welfare by using sensor
data in herd management and dairy cattle breeding—A joint initia-
tive of ICAR and IDF. Pages 56_63 in Proc 11th Eur. Conf. Precis.
Livest. Farming, Bologna, Italy. Organizing Committee of the 11th
European Conference on Precision Livestock Farming (ECPLF),
University of Veterinary Medicine, Vienna, Austria.
Egger-Danner, C., K. Linke, B. Fuerst-Waltl, P. Klimek, O. Saukh, and
T. Wittek. 2022a. D4Dairy: From data integration to decision sup-
port—Lessons learned. In Proc. 73rd Annual Meeting of the Europe-
an Federation of Animal Science. Wageningen Academic Publishers,
Porto, Portugal. https:  / / doi .org/ 10 .3920/  978 -90 -8686  -937 -4.
Egger-Danner
, C., K. Linke, B. Fuerst-Waltl, P. Klimek, O. Saukh, and
T. Wittek. 2022b. D4Dairy—Interdisciplinary network for creating
added value out of different data sources. Pages 497–504 in Pre-
cision Livestock Farming. O. Berckmans, M. Oczak, M. Iwersen,
and K. Wagener, ed. Organizing Committee of the 10th European
Conference on Precision Livestock Farming (ECPLF), University of
Veterinary Medicine, Vienna, Austria
Fleming, A., C. F. Baes, A. A. A. Martin, T. C. S. Chud, F. Malchiodi, L.
F. Brito, and F. Miglior. 2019. Symposium review: The choice and
collection of new relevant phenotypes for fertility selection. J. Dairy
Sci. 102:3722–3734. https:  / / doi .org/ 10 .3168/  jds .2018 -15470.
Fogsgaard, K. K., C. M. Rontved, P. Sorensen, and M. S. Herskin. 2012.

Sickness behavior in dairy cows during Escherichia coli mastitis. J.
Dairy Sci. 95:630–638. https:  / / doi .org/ 10 .3168/  jds .2011 -4350.
Fogsgaard, K. K., T
. W. Bennedsgaard, and M. S. Herskin. 2015. Behav-
ioral changes in freestall-housed dairy cows with naturally occur -
ring clinical mastitis. J. Dairy Sci. 98:1730–1738. https:  / / doi .org/ 10
.3168/  jds .2014  -8347.
Fuerst-Waltl, B., H. Schwarzenbacher
, K. Schodl, M. Suntinger, F.
Steininger, and C. Egger-Danner. 2022. Ketosis and its auxiliary
traits. Page 661 in Book of Abstracts of the 73rd Annual Meeting of
the European Federation of Animal Science. European Federation of
Animal Science. https:  / / doi .org/ 10 .3920/  978 -90 -8686 -937 -4.
Gäde, S., E. Stamer,
W. Junge, and E. Kalm. 2006. Estimates of ge-
netic parameters for milkability from automatic milking. Livest. Sci.
104:135–146. https:  / / doi .org/ 10 .1016/  j .livsci  .2006 .04 .003.
Gargiulo, J. I., C. R. Eastwood, S. C. Garcia, and N.
A. Lyons. 2018.
Dairy farmers with larger herd sizes adopt more precision dairy
technologies. J. Dairy Sci. 101:5466–5473. https:  / / doi .org/ 10 .3168/
jds .2017 -13324.
Gladden, N., E. Cuthbert, K. Ellis, and D. McKeegan. 2020. Use of a
tri-axial accelerometer can reliably detect play behaviour in new
-
born calves. Animals (Basel) 10:1137. https:  / / doi .org/ 10 .3390/
ani10071137.
Goddard, M. E.,
K. E. Kemper, I. M. MacLeod, A. J. Chamberlain, and
B. J. Hayes. 2016. Genetics of complex traits: Prediction of phe-
notype, identification of causal polymorphisms and genetic archi-
tecture. Proc. Biol. Sci. 283:20160569. https:  / / doi .org/ 10 .1098/  rspb
.2016 .0569.
Graham, J. R., M.
E. Montes, V . B. Pedrosa, J. Doucette, M. Taghipoor,
A. C. Araujo, L. S. Gloria, J. P. Boerman, and L. F. Brito. 2024a.
Genetic parameters for calf feeding traits derived from automated
milk feeding machines and number of bovine respiratory dis-
ease treatments in North American Holstein calves. J. Dairy Sci.
107:2175–2193. https:  / / doi .org/ 10 .3168/  jds .2023 -23794.
Graham, J. R., M. T
aghipoor, L. S. Gloria, J. P. Boerman, J. Doucette,
A. O. Rocha, and L. F. Brito. 2024b. Trait development and genetic
parameters of resilience indicators based on variability in milk con-
sumption recorded by automated milk feeders in North American
Holstein calves. J. Dairy Sci. 107:11180–11194. https:  / / doi .org/ 10
.3168/  jds .2024  -25192.
Häggman, J., J. M. Christensen, E. A. Mäntysaari, and J. Juga. 2019.

Genetic parameters for endocrine and traditional fertility traits,
hyperketonemia and milk yield in dairy cattle. Animal 13:248–255.
https:  / / doi .org/ 10 .1017/  S1751731118001386
.
Halachmi, I., and M. Guarino. 2016. Editorial: Precision livestock
farming: A ‘per animal’ approach using advanced monitoring
technologies. Animal 10:1482–1483. https:  / / doi .org/ 10 .1017/
S1751731116001142
.
Hardie, L. C., M. J. VandeHaar, R. J. Tempelman, K. A. Weigel, L. E.
Armentano, G. R. Wiggans, R. F. Veerkamp, Y . de Haas, M. P. Cof-
fey, E. E. Connor, M. D. Hanigan, C. Staples, Z. Wang, J. C. M.
Dekkers, and D. M. Spurlock. 2017. The genetic and biological basis
of feed efficiency in mid-lactation Holstein dairy cows. J. Dairy Sci.
100:9061–9075. https:  / / doi .org/ 10 .3168/  jds .2017 -12604.
Haskell, M. J., G. Simm, and S. P.
Turner. 2014. Genetic selection for
temperament traits in dairy and beef cattle. Front. Genet. 5:368.
https:  / / doi .org/ 10 .3389/  fgene .2014  .00368.
Heringstad, B., and K. Bakke. 2023. Heritability of methane emission in
young
Norwegian Red bulls estimated from GreenFeed measures at
the test station. Interbull Bull. 59:69–73.
Heringstad, B., C. Egger-Danner, N. Charfeddine, J. E. Pryce, K. F.
Stock, J. Kofler, A. M. Sogstad, M. Holzhauer, A. Fiedler, K. Mül-
ler, P. Nielsen, G. Thomas, N. Gengler, G. de Jong, C. Ødegård, F.
Malchiodi, F. Miglior, M. Alsaaod, and J. B. Cole. 2018. Invited
review: Genetics and claw health: Opportunities to enhance claw
health by genetic selection. J. Dairy Sci. 101:4801–4821. https:  / / doi
.org/ 10 .3168/  jds .2017 -13531.
Heringstad, B., and K. B. W
ethal. 2023. Cow activity measurements can
be used to define new fertility traits for use in genetic evaluation.
JDS Commun. 4:99–100. https:  / / doi .org/ 10 .3168/  jdsc .2022 -0251.
Hernandez-Gotelli, C., D. Manríquez, J. Azocar
, A. De Vries, and P. J.
Pinedo. 2023. Factors associated with the time and magnitude of the
nadir body condition score in early lactation and its subsequent ef-
fects on fertility of Holstein cows. J. Anim. Sci. 101:skad119. https:
/ / doi .org/ 10 .1093/  jas/ skad119.
Hof
fmann, G., S. Strutzke, D. Fiske, J. Heinicke, and R. Mylostyvyi.
2024. A new approach to recording rumination behavior in dairy
cows. Sensors (Basel) 24:5521. https:  / / doi .org/ 10 .3390/  s24175521.
Hogan, C., J. Kinsella, B. O’Brien, A. Markey
, and M. Beecher. 2022.
Estimating the effect of different work practices and technologies
on labor efficiency within pasture-based dairy systems. J. Dairy Sci.
105:5109–5123. https:  / / doi .org/ 10 .3168/  jds .2021 -21216.
Hu, L., L. F. Brito, H. Luo, S. Chen, J. S. Johnson,
A. Sammad, G. Guo,
Q. Xu, and Y . Wang. 2023. Differential responses of physiological
parameters, production traits, and blood metabolic profiling between
first- and second-parity Holstein cows in the comparison of spring
versus summer seasons. J. Agric. Food Chem. 71:11902–11920.
https:  / / doi .org/ 10 .1021/  acs .jafc .3c00043.
Hurley,
A. M., N. López-Villalobos, S. McParland, E. Lewis, E. Ken-
nedy, M. O’Donovan, J. L. Burke, and D. P. Berry. 2017. Genetics
of alternative definitions of feed efficiency in grazing lactating dairy
cows. J. Dairy Sci. 100:5501–5514. https:  / / doi .org/ 10 .3168/  jds .2016
-12314.
Hut, P. R., J. Scheurwater, M. Nielen, J. van den Broek, and M. M.

Hostens. 2022. Heat stress in a temperate climate leads to adapted
sensor-based behavioral patterns of dairy cows. J. Dairy Sci.
105:6909–6922. https:  / / doi .org/ 10 .3168/  jds .2021 -21756.
Brito et al.: INVITED REVIEW: SENSOR DATA FOR GENETIC IMPROVEMENT

10470
Journal of Dairy Science Vol. 108 No. 10, 2025
ICAR. 2022. Section 7—Guidelines for health, female fertility, udder
health, claw health traits, lameness and calving traits in bovine.
Accessed Jan. 8, 2025. https:  / / www .icar .org/ Guidelines/  07 -Bovine
-Functional  -Traits  .pdf.
ICAR. 2020. Section
11—Guidelines for testing, approval and checking
of milk recording devices. Accessed Jan. 11, 2025. www  .icar .org/
Guidelines/  11 -Milk  -Recording  -Devices  .pdf.
Ismael, A., E. Strandber
g, B. Berglund, M. Kargo, A. Fogh, and P. Løven-
dahl. 2016. Genotype by environment interaction for activity-based
estrus traits in relation to production level for Danish Holstein. J.
Dairy Sci. 99:9834–9844. https:  / / doi .org/ 10 .3168/  jds .2016  -11446.
Jones, H. E., and P
. B. Wilson. 2022. Progress and opportunities through
use of genomics in animal production. Trends Genet. 38:1228–1252.
https:  / / doi .org/ 10 .1016/  j .tig .2022 .06 .014.
Jurkovich, V
., P. Hejel, and L. Kovács. 2024. A review of the effects of
stress on dairy cattle behaviour. Animals (Basel) 14:2038. https:  / / doi
.org/ 10 .3390/  ani14142038.
Kamalanathan, S., K. Houlahan, F. Miglior
, T. C. S. Chud, D. J. Sey-
mour, D. Hailemariam, G. Plastow, H. R. de Oliveira, C. F. Baes, and
F. S. Schenkel. 2023. Genetic analysis of methane emission traits
in Holstein dairy cattle. Animals (Basel) 13:1308. https:  / / doi .org/ 10
.3390/  ani13081308.
Kandel, P. B., M.-L.
Vanrobays, A. Vanlierde, F. Dehareng, E. Froid-
mont, N. Gengler, and H. Soyeurt. 2017. Genetic parameters of
mid-infrared methane predictions and their relationships with milk
production traits in Holstein cattle. J. Dairy Sci. 100:5578–5591.
https:  / / doi .org/ 10 .3168/  jds .2016 -11954.
Karoui,
Y ., A. A. Boatswain Jacques, A. B. Diallo, E. Shepley, and E.
Vasseur. 2021. A deep learning framework for improving lame-
ness identification in dairy cattle. Proc. AAAI Conf. Artif. Intell.
35:15811–15812. https:  / / doi .org/ 10 .1609/  aaai .v35i18  .17902.
Kaur, U.,
V . M. R. Malacco, H. Bai, T. P. Price, A. Datta, L. Xin, S. Sen,
R. A. Nawrocki, G. Chiu, S. Sundaram, B.-C. Min, K. M. Daniels, R.
R. White, S. S. Donkin, L. F. Brito, and R. M. V oyles. 2023. Invited
review: Integration of technologies and systems for precision animal
agriculture—A case study on precision dairy farming. J. Anim. Sci.
101:skad206. https:  / / doi .org/ 10 .1093/  jas/ skad206.
Klingström, T
., I. Ohlsson, and D. J. de Koning. 2022. The infrastructure
for cattle data at the Swedish University of Agricultural Sciences,
Gigacow. Pages 1808–1811 in Proc. 12th World Congress on Ge-
netics Applied to Livestock Production (WCGALP). Wageningen
Academic Publishers, the Netherlands.
Köck, A., L. M. Dale, A. Werner, M. Mayerhofer, F.-J. Auer, and C.
Egger-Danner. 2024. Ketosis risk derived from mid-infrared pre-
dicted traits and its relationship with herd milk yield, health and
fertility. Front. Anim. Sci. 5:1367210. https:  / / doi .org/ 10 .3389/  fanim
.2024 .1367210.
Köck, A., B. Fuerst-W
altl, J. Kofler, J. Burgstaller, F. Steininger, and C.
Fuerst., C. and C. Egger-Danner. 2019. Short communication: Use
of lameness scoring to genetically improve claw health in Austrian
Fleckvieh, Brown Swiss and Holstein cattle. J. Dairy Sci. 102:1397–
1401. https:  / / doi .org/ 10 .3168/  jds .2018  -15287.
Köck, A., K. Schodl, B. Fuerst-W
altl, H. Schwarzenbacher, L. M. Dale,
A. Werner, M. Mayerhofer, F.-J. Auer, C. Grelet, J. Sölkner, L. Ri-
enesl, N. Gengler, and J. Leblois. J. and C. Egger-Danner. 2022.
New traits predicted from milk-infrared spectra to reduce incidence
of subclinical ketosis. Pages 161–164 in Proc. ICAR Annual Con-
ference (2022), Montreal, QC, Canada. ICAR. https:  / / www .icar
.org/  Docume
nts/  tec
hnical  _serie
s/ ICAR  -Tec
hnical  -Serie
s -no  -26
-Montreal/  26 %20New  %20trait
s %20predicte
d %20from  %20milk
%20mid  -infrared  .pdf.
König, S., F. Köhn, K. Kuwan, H. Simianer
, and M. Gauly. 2006. Use
of repeated measures analysis for evaluation of genetic background
of dairy cattle behavior in automatic milking systems. J. Dairy Sci.
89:3636–3644. https:  / / doi .org/ 10 .3168/  jds .S0022  -0302(06)72403  -1.
Lassen, J., and P. Løvendahl. 2016. Heritability estimates for enteric

methane emissions from Holstein cattle measured using noninvasive
methods. J. Dairy Sci. 99:1959–1967. https:  / / doi .org/ 10 .3168/  jds
.2015 -10012.
Lassen, J., N. A. Poulsen, M. K. Larsen, and
A. J. Buitenhuis. 2016.
Genetic and genomic relationship between methane production
measured in breath and fatty acid content in milk samples from
Danish Holsteins. Anim. Prod. Sci. 56:298. https:  / / doi .org/ 10 .1071/
AN15489.
Lemal, P., M.-N. T
ran, H. Atashi, M. Schroyen, and N. Gengler. 2024.
Adding behavior traits to select for heat tolerance in dairy cattle.
JDS Commun. 5:368–373. https:  / / doi .org/ 10 .3168/  jdsc .2023  -0421.
Lemmens, L., K. Schodl, B. Fuerst-Waltl, H. Schwarzenbacher
, C.
Egger-Danner, K. Linke, M. Suntinger, M. Phelan, M. Mayerhofer,
F. Steininger, F. Papst, L. Maurer, and J. Kofler. 2023. The combined
use of automated milking system and sensor data to improve detec-
tion of mild lameness in dairy cattle. Animals (Basel) 13:1180. https:
/ / doi .org/ 10 .3390/  ani13071180.
Lin, Z., I. Macleod, and J. E. Pryce. 2013. Estimation of genetic param
-
eters for residual feed intake and feeding behavior traits in dairy
heifers. J. Dairy Sci. 96:2654–2656. https:  / / doi .org/ 10 .3168/  jds
.2012  -6134.
Linstädt, J., C. Thöne-Reineke, and R. Merle. 2024.
Animal-based
welfare indicators for dairy cows and their validity and practical-
ity: A systematic review of the existing literature. Front. Vet. Sci.
11:1429097. https:  / / doi .org/ 10 .3389/  fvets  .2024 .1429097.
Liu, N., J. Qi, X. An, and
Y . Wang. 2023. A review on information tech-
nologies applicable to precision dairy farming: Focus on behavior,
health monitoring, and the precise feeding of dairy cows. Agriculture
13:1858. https:  / / doi .org/ 10 .3390/  agriculture13101858.
Lopes, L. S. F., F
. S. Schenkel, K. Houlahan, C. M. Rochus, G. A.
Oliveira Jr., H. R. Oliveira, F. Miglior, L. M. Alcantara, D. Tulpan,
and C. F. Baes. 2024. Estimates of genetic parameters for rumination
time, feed efficiency, and methane production traits in first-lactation
Holstein cows. J. Dairy Sci. 107:4704–4713. https:  / / doi .org/ 10
.3168/  jds .2023 -23751.
López-Paredes, J., I. Goiri, R. Atxaerandio,
A. García-Rodríguez, E.
Ugarte, J. A. Jiménez-Montero, R. Alenda, and O. González-Recio.
2020. Mitigation of greenhouse gases in dairy cattle via genetic se-
lection: 1. Genetic parameters of direct methane using noninvasive
methods and proxies of methane. J. Dairy Sci. 103:7199–7209. https:
/ / doi .org/ 10 .3168/  jds .2019 -17597.
Lovarelli, D., J. Bacenetti, and M. Guarino. 2020. A
 review on dairy
cattle farming: Is precision livestock farming the compromise for
an environmental, economic, and social sustainable production? J.
Clean. Prod. 262:121409. https:  / / doi .org/ 10 .1016/  j .jclepro  .2020
.121409.
Lovarelli, D., M. Bovo, C. Giannone, E. Santolini, P. T
assinari, and M.
Guarino. 2024. Reducing life cycle environmental impacts of milk
production through precision livestock farming. Sustain. Prod. Con-
sum. 51:303–314. https:  / / doi .org/ 10 .1016/  j .spc .2024 .09 .021.
Løvendahl, P., and
A. J. Buitenhuis. 2022. Genetic and phenotypic varia-
tion and consistency in cow preference and circadian use of robotic
milking units. J. Dairy Sci. 105:5283–5295. https:  / / doi .org/ 10 .3168/
jds .2021  -21593.
Løvendahl, P., and M. G. G. Chagunda. 2009. Genetic variation in estrus

activity traits. J. Dairy Sci. 92:4683–4688. https:  / / doi .org/ 10 .3168/
jds .2008  -1736.
Løvendahl, P., and L. Munksgaard. 2016a.
An investigation into genetic
and phenotypic variation in time budgets and yield of dairy cows. J.
Dairy Sci. 99:408–417. https:  / / doi .org/ 10 .3168/  jds .2015  -9838.
Løvendahl, P., L. P
. Sørensen, M. Bjerring, and J. Lassen. 2016b. Ge-
netic variation in choice consistency for cows accessing automatic
milking units. J. Dairy Sci. 99:9857–9863. https:  / / doi .org/ 10 .3168/
jds .2016  -11287.
Lu, X., M. Long, Z. Zhu, H. Zhang, F
. Zhou, Z. Liu, Y . Mao, and Z. Yang.
2024. Comprehensive genetic analysis and predictive evaluation of
milk electrical conductivity for subclinical mastitis in Chinese Hol-
stein cows. BMC Genomics 25:1230. https:  / / doi .org/ 10 .1186/ s12864
-024 -11157 -6.
Luo, H., L. F. Brito, X. Li, G. Su, J. Dou,
W. Xu, X. Yan, H. Zhang,
G. Guo, L. Liu, and Y . Wang. 2021a. Genetic parameters for rectal
temperature, respiration rate, and drooling score in Holstein cattle
and their relationships with various fertility, production, body con-
formation, and health traits. J. Dairy Sci. 104:4390–4403. https:  / / doi
.org/ 10 .3168/  jds .2020  -19192.
Brito et al.: INVITED REVIEW: SENSOR DATA FOR GENETIC IMPROVEMENT

Journal of Dairy Science Vol. 108 No. 10, 2025
10471
Luo, H., X. Li, L. Hu, W. Xu, Q. Chu, A. Liu, G. Guo, L. Liu, L. F. Brito,
and Y . Wang. 2021b. Genomic analyses and biological validation of
candidate genes for rectal temperature as an indicator of heat stress
in Holstein cattle. J. Dairy Sci. 104:4441–4451. https:  / / doi .org/ 10
.3168/  jds .2020  -18725.
Majcen, P. 2022. Data integration in D4Dairy and new opportunities

under the Data-Governance Act and the Data Act. Page 658 in Book
of Abstracts of the 73rd Annual Meeting of the European Federation
of Animal Science. Wageningen Academic Publishers.
Manzanilla-Pech, C. I. V ., G. F. Difford, P. Løvendahl, R. B. Stephansen,
and J. Lassen. 2022. Genetic (co-) variation of methane emissions,
efficiency, and production traits in Danish Holstein cattle along and
across lactations. J. Dairy Sci. 105:9799–9809. https:  / / doi .org/ 10
.3168/  jds .2022  -22121.
Manzanilla-Pech, C. I. V
., R. B. Stephansen, and J. Lassen. 2023. Ge-
netic parameters for feed intake and body weight in dairy cattle us-
ing high-throughput 3-dimensional cameras in Danish commercial
farms. J. Dairy Sci. 106:9006–9015. https:  / / doi .org/ 10 .3168/  jds
.2023  -23405.
Marino, R., F. Petrera, M. Speroni,
T. Rutigliano, A. Galli, and F. Abeni.
2021. Unraveling the relationship between milk yield and quality
at the test day with rumination time recorded by a PLF technology.
Animals (Basel) 11:1583. https:  / / doi .org/ 10 .3390/  ani11061583.
Martin, P
., H. W. Barkema, L. F. Brito, S. G. Narayana, and F. Miglior.
2018. Symposium review: Novel strategies to genetically improve
mastitis resistance in dairy cattle. J. Dairy Sci. 101:2724–2736.
https:  / / doi .org/ 10 .3168/  jds .2017 -13554.
Martins, B. M., A. L. C. Mendes, L. F
. Silva, T. R. Moreira, J. H. C.
Costa, P. P. Rotta, M. L. Chizzotti, and M. I. Marcondes. 2020. Es-
timating body weight, body condition score, and type traits in dairy
cows using three-dimensional cameras and manual body measure-
ments. Livest. Sci. 236:104054. https:  / / doi .org/ 10 .1016/  j .livsci  .2020
.104054.
Maskal, J. M., V . B. Pedrosa, H. Rojas de Oliveira, and L. F
. Brito. 2024.
A comprehensive meta-analysis of genetic parameters for resilience
and productivity indicator traits in Holstein cattle. J. Dairy Sci.
107:3062–3079. https:  / / doi .org/ 10 .3168/  jds .2023 -23668.
Mayo, L. M., W
. J. Silvia, D. L. Ray, B. W. Jones, A. E. Stone, I. C.
Tsai, J. D. Clark, J. M. Bewley, and G. Heersche Jr. 2019. Auto-
mated estrous detection using multiple commercial precision dairy
monitoring technologies in synchronized dairy cows. J. Dairy Sci.
102:2645–2656. https:  / / doi .org/ 10 .3168/  jds .2018 -14738.
Medeiros, G. C., J. B. S. Ferraz, V
. B. Pedrosa, S.-Y . Chen, J. S. Doucette,
J. P. Boerman, and L. F. Brito. 2024. Genetic parameters for udder
conformation traits derived from Cartesian coordinates generated by
robotic milking systems in North American Holstein cattle. J. Dairy
Sci. 107:7038–7051. https:  / / doi .org/ 10 .3168/  jds .2023  -24208.
Mensching, A., K. Bünemann, U. Meyer
, D. von Soosten, J. Hummel, A.
O. Schmitt, A. R. Sharifi, and S. Dänicke. 2020. Modeling reticular
and ventral ruminal pH of lactating dairy cows using ingestion and
rumination behavior. J. Dairy Sci. 103:7260–7275. https:  / / doi .org/ 10
.3168/  jds .2020  -18195.
Misztal, I., L. F. Brito, and D. Lourenco. 2025. Breeding for improved

heat tolerance in dairy cattle: Methods, challenges, and progress.
JDS Commun. 6:464–468. https:  / / doi .org/ 10 .3168/  jdsc .2024  -0651.
Moretti, R., M. P. G. de Rezende, S. Biffani, and R. Bozzi. 2018. Herita
-
bility and genetic correlations between rumination time and produc-
tion traits in Holstein dairy cows during different lactation phases.
J. Anim. Breed. Genet. 135:293–299. https:  / / doi .org/ 10 .111
1/ jbg
.12346.
Nascimento, B. M., L. Cavani, M. J. Caputo, M. N. Marinho, M. R.
Borchers, R. L. W
allace, J. E. Santos, H. M. White, F. Peñagaricano,
and K. A. Weigel. 2024. Genetic relationships between behavioral
traits and feed efficiency traits in lactating Holstein cows. J. Dairy
Sci. 107:8141–8149. https:  / / doi .org/ 10 .3168/  jds .2023  -24526.
Nejati, A.,
A. Bradtmueller, E. Shepley, and E. Vasseur. 2023. Technol-
ogy applications in bovine gait analysis: A scoping review. PLoS
One 18:e0266287. https:  / / doi .org/ 10 .1371/  journal  .pone .0266287.
Nixon, M., J. Bohmanova, J. Jamrozik, L. R. Schaeffer
, K. Hand, and F.
Miglior. 2009. Genetic parameters of milking frequency and milk
production traits in Canadian Holsteins milked by an automated
milking system. J. Dairy Sci. 92:3422–3430. https:  / / doi .org/ 10
.3168/  jds .2008  -1689.
Pacheco, H. A., R. O. Hernandez, S.
Y . Chen, H. W. Neave, J. A. Pempek,
and L. F. Brito. 2025. Invited Review: Phenotyping strategies and
genetic background of dairy cattle behavior in intensive production
systems—From trait definition to genomic selection. J. Dairy Sci.
108:6–32. https:  / / doi .org/ 10 .3168/  jds .2024  -24953.
Papst, F., K. Schodl, and O. Saukh. 2021. Exploring the co-dependency

of IoT data quality and model robustness in precision cattle farming.
Pages 433–438 in Proc. 19th ACM Conference on Embedded Net-
worked Sensor Systems (SenSys ’21). Association for Computing
Machinery.
Pastell, M., L. Frondelius, M. Järvinen, and J. Backman. 2018. Filter -
ing methods to improve the accuracy of indoor positioning data
for dairy cows. Biosyst. Eng. 169:22–31. https:  / / doi .org/ 10 .1016/  j
.biosystemseng  .2018 .01 .008.
Pastell, M., M. Hautala, V
. Poikalainen, J. Praks, I. Veermäe, M. Kujala,
and J. Ahokas. 2008. Automatic observation of cow leg health using
load sensors. Comput. Electron. Agric. 62:48–53. https:  / / doi .org/ 10
.1016/  j .compag  .2007  .09 .003.
Paudyal, S., F. P
. Maunsell, J. T. Richeson, C. A. Risco, D. A. Donovan,
and P. J. Pinedo. 2018. Rumination time and monitoring of health
disorders during early lactation. Animal 12:1484–1492. https:  / / doi
.org/ 10 .1017/  S1751731117002932
.
Pedrosa, V . B., J. P. Boerman, L. S. Gloria, S. Y . Chen, M. E. Montes, J.
S. Doucette, and L. F. Brito. 2023. Genomic-based genetic param-
eters for milkability traits derived from automatic milking systems
in North American Holstein cattle. J. Dairy Sci. 106:2613–2629.
https:  / / doi .org/ 10 .3168/  jds .2022 -22515.
Piwczyński, D.,
B. Sitkowska, and E. Ptak. 2021. Genetic relationship
among somatic cell score and some milking traits in Holstein-
Friesian primiparous cows milked by an automated milking system.
Animal 15:100094. https:  / / doi .org/ 10 .1016/  j .animal  .2020  .100094.
Polsky, L., and M.
A. von Keyserlingk. 2017. Invited review: Effects
of heat stress on dairy cattle welfare. J. Dairy Sci. 100:8645–8657.
https:  / / doi .org/ 10 .3168/  jds .2017 -12651.
Poppe, M., G. Bonekamp, M. L. van Pelt, and H. A. Mulder
. 2021. Ge-
netic analysis of resilience indicators based on milk yield records
in different lactations and at different lactation stages. J. Dairy Sci.
104:1967–1981. https:  / / doi .org/ 10 .3168/  jds .2020 -19245.
Poppe, M., H. A. Mulder
, B. J. Ducro, and G. de Jong. 2019. Genetic
analysis of udder conformation traits derived from automatic milk-
ing system recording in dairy cows. J. Dairy Sci. 102:1386–1396.
https:  / / doi .org/ 10 .3168/  jds .2018 -14838.
Poppe, M., H. A. Mulder
, M. L. van Pelt, E. Mullaart, H. Hogeveen,
and R. F. Veerkamp. 2022. Development of resilience indicator traits
based on daily step count data for dairy cattle breeding. Genet. Sel.
Evol. 54:21. https:  / / doi .org/ 10 .1186/ s12711 -022 -00713  -x.
Poppe, M.,
R. F. Veerkamp, M. L. van Pelt, and H. A. Mulder. 2020.
Exploration of variance, autocorrelation, and skewness of deviations
from lactation curves as resilience indicators for breeding. J. Dairy
Sci. 103:1667–1684. https:  / / doi .org/ 10 .3168/  jds .2019  -17290.
Pryce, J. E., M. P. Cof
fey, and S. Brotherstone. 2000. The genetic rela-
tionship between calving interval, body condition score and linear
type and management traits in registered Holsteins. J. Dairy Sci.
83:2664–2671. https:  / / doi .org/ 10 .3168/  jds .S0022  -0302(00)75160  -5.
Reith, S., and S. Hoy. 2018. Behavioral signs of estrus and the potential

of fully automated systems for detection of estrus in dairy cattle.
Animal 12:398–407. https:  / / doi .org/ 10 .1017/  S1751731117001975
.
Rial, C., A. Laplacette, L. Caixeta, C. Florentino, F. Peña-Mosca, and
J. O. Giordano. 2023. Metabolic-digestive clinical disorders of
lactating dairy cows were associated with alterations of rumination,
physical activity, and lying behavior monitored by an ear-attached
sensor. J. Dairy Sci. 106:9323–9344. https:  / / doi .org/ 10 .3168/  jds
.2022 -23156.
Richardson, C. M., T
. T. T. Nguyen, M. Abdelsayed, P. J. Moate, S. R.
O. Williams, T. C. S. Chud, F. S. Schenkel, M. E. Goddard, I. van
den Berg, B. G. Cocks, L. C. Marett, W. J. Wales, and J. E. Pryce.
2021. Genetic parameters for methane emission traits in Australian
dairy cows. J. Dairy Sci. 104:539–549. https:  / / doi .org/ 10 .3168/  jds
.2020 -18565.
Brito et al.: INVITED REVIEW: SENSOR DATA FOR GENETIC IMPROVEMENT

10472
Journal of Dairy Science Vol. 108 No. 10, 2025
Rojas de Oliveira, H. R., H. Sweett, S. Narayana, A. Fleming, S.
Shadpour, F. Malchiodi, J. Jamrozik, G. Kistemaker, P. Sullivan,
F. Schenkel, and D. Hailemariam. 2024. Development of genomic
evaluation for methane efficiency in Canadian Holsteins. JDS Com-
mun. 5:756–760. https:  / / doi .org/ 10 .3168/  jdsc .2023 -0431.
Rustas, B.
O., Y . Persson, E. Ternman, A. R. Kristensen, A. H. Stygar,
and U. Emanuelson. 2024. The evolutionary operation framework as
a tool for herd-specific control of mastitis in dairy cows. Livest. Sci.
279:105390. https:  / / doi .org/ 10 .1016/  j .livsci  .2023 .105390.
Rutten, C. J., A. G. J.
Velthuis, W. Steeneveld, and H. Hogeveen. 2013.
Invited review: Sensors to support health management on dairy
farms. J. Dairy Sci. 96:1928–1952. https:  / / doi .org/ 10 .3168/  jds .2012
-6107.
Saborío-Montero, A., M. Gutiérrez-Rivas, A. García-Rodríguez, R.
Atx-
aerandio, I. Goiri, E. López de Maturana, J. A. Jiménez-Montero, R.
Alenda, and O. González-Recio. 2020. Structural equation models to
disentangle the biological relationship between microbiota and com-
plex traits: Methane production in dairy cattle as a case of study. J.
Anim. Breed. Genet. 137:36–48. https:  / / doi .org/ 10 .111
1/ jbg .12444.
Santos, L. V
., K. Brügemann, A. Ebinghaus, and S. König. 2018. Genetic
parameters for longitudinal behavior and health indicator traits gen-
erated in automatic milking systems. Arch. Tierzucht 61:161–171.
https:  / / doi .org/ 10 .5194/  aab -61 -161 -2018.
Schillings, J., R. Bennett, and D. C. Rose. 2021. Exploring the potential
of precision livestock farming technologies to help address farm

animal welfare. Front. Anim. Sci. 2:639678. https:  / / doi .org/ 10 .3389/
fanim  .2021 .639678.
Schodl, K., B. Fuerst-Waltl, F
. Steininger, H. Schwarzenbacher, and C.
Egger-Danner. 2024a. Approaches to defining genetic traits from
sensor data and estimation of genetic parameters. Proceedings of the
11th European Conference on Precision Livestock Farming, Bolo-
gna, Italy.
Schodl, K., B. Fuerst-Waltl, F. Steininger, M. Suntinger, H. Schwar -
zenbacher, and D4Dairy Consortium. 2023. Genetic parameters
for potential auxiliary traits for lameness based on data from PLF-
technologies. 74th Annual Meeting of the European Federation of
Animal Science, Lyon, France.
Schodl, K., H. Schwarzenbacher, C. Egger-Danner, F. Steininger, and M.
Suntinger. D4Dairy Consortium, and B. Fuerst-Waltl. 2022. Poten-
tial of sensor-based phenotypes for breeding. 73rd Annual Meeting
of the European Federation of Animal Science, Porto, Portugal.
Schodl, K., A. Stygar, F. Steininger, and C. Egger-Danner. 2024b. Sensor
data cleaning for applications in dairy herd management and breed-
ing. Front. Anim. Sci. 5:1444948. https:  / / doi .org/ 10 .3389/  fanim
.2024  .1444948.
Schöpke, K., and K. A.
Weigel. 2014. Use of accelerometer data for
genetic evaluation in dairy cattle. Interbull Bull. 48:68–72.
Sewalem, A., F. Miglior, and G. J. Kistemaker. 2011. Genetic parameters
of milking temperament and milking speed in Canadian Holsteins. J.
Dairy Sci. 94:512–516. https:  / / doi .org/ 10 .3168/  jds .2010  -3479.
Shi, R., L. F. Brito, S. Li, L. Han, G. Guo,
W. Wen, Q. Yan, S. Chen,
and Y . Wang. 2025. Genomic prediction and validation strategies for
reproductive traits in Holstein cattle across different Chinese regions
and climatic conditions. J. Dairy Sci. 108:707–725. https:  / / doi .org/
10 .3168/  jds .2024  -25121.
Siivonen, J., S. T
aponen, M. Hovinen, M. Pastell, B. Lensinke, S.
Pyörälä, and L. Hänninen. 2011. Impact of acute clinical mastitis
on cow behaviour. Appl. Anim. Behav. Sci. 132:101–106. https:  / / doi
.org/ 10 .1016/  j .applanim  .2011 .04 .005.
Silva, S. R., J. P.
Araujo, C. Guedes, F. Silva, M. Almeida, and J. L. Cer -
queira. 2021. Precision technologies to address dairy cattle welfare:
Focus on lameness, mastitis and body condition. Animals (Basel)
11:2253. https:  / / doi .org/ 10 .3390/  ani11082253.
Silva Neto, J. B., L. F
. Mota, M. Londoño-Gil, P. I. Schmidt, G. R. Ro-
drigues, V . A. Ligori, L. M. Arikawa, C. U. Magnabosco, L. F. Brito,
and F. Baldi. 2024. Genotype-by-environment interactions in beef
and dairy cattle populations: A review of methodologies and per -
spectives on research and applications. Anim. Genet. 55:871–892.
https:  / / doi .org/ 10 .111
1/ age .13483.
Simitzis, P., C.
Tzanidakis, O. Tzamaloukas, and E. Sossidou. 2021.
Contribution of precision livestock farming systems to the improve-
ment of welfare status and productivity of dairy animals. Dairy
3:12–28. https:  / / doi .org/ 10 .3390/  dairy3010002.
Simoni, A.,
A. Hancock, C. Wunderlich, M. Klawitter, T. Breuer, F.
König, K. Weimar, M. Drillich, and M. Iwersen. 2023. Association
between rumination times detected by an ear tag-based accelerom-
eter system and rumen physiology in dairy cows. Animals (Basel)
13:759 https:  / / doi .org/ 10 .3390/  ani13040759.
Simoni, A.,
F. König, K. Weimar, A. Hancock, C. Wunderlich, M.
Klawitter, T. Breuer, M. Drillich, and M. Iwersen. 2024. Evalu-
ation of sensor-based health monitoring in dairy cows: Exploiting
rumination times for health alerts around parturition. J. Dairy Sci.
107:6052–6064. https:  / / doi .org/ 10 .3168/  jds .2023 -24313.
Singh, D., R. Singh, A. Gehlot, S.
V . Akram, N. Priyadarshi, and B.
Twala. 2022. An imperative role of digitalization in monitoring
cattle health for sustainability. Electronics (Basel) 11:2702. https:  /
/ doi .org/ 10 .3390/  electronics11172702
.
Sitkowska, B., H. M. Yüksel, D. Piwczyński, and H. Önder. 2024. Heri-
tability and genetic correlations of rumination time with milk-yield
and milking traits in Holstein-Friesian cows using an automated
milking system. Animal 18:101101. https:  / / doi .org/ 10 .1016/  j .animal
.2024 .101101.
Sousa,
L. P. B. Junior, L. F. B. Pinto, V . A. Cruz, and G. A. Oliveira
Jr., H. R. de Oliveira, T. S. Chud, V . B. Pedrosa, F. Miglior, F. S.
Schenkel, L. F. and Brito. 2024. Genome-wide association and
functional genomic analyses for various hoof health traits in North
American Holstein cattle. J. Dairy Sci. 107:2207–2230. https:  / / doi
.org/ 10 .3168/  jds .2023  -23806.
Stangaferro, M. L., R. W
ijma, L. S. Caixeta, M. A. Al-Abri, and J. O.
Giordano. 2016. Use of rumination and activity monitoring for the
identification of dairy cows with health disorders: Part I. Metabolic
and digestive disorders. J. Dairy Sci. 99:7395–7410. https:  / / doi .org/
10 .3168/  jds .2016  -10907.
Steeneveld, W
., and H. Hogeveen. 2015. Characterization of Dutch
dairy farms using sensor systems for cow management. J. Dairy Sci.
98:709–717. https:  / / doi .org/ 10 .3168/  jds .2014 -8595.
Stephansen, R. S.,
A. Fogh, and E. Norberg. 2018. Genetic parameters
for handling and milking temperament in Danish first-parity Hol-
stein cows. J. Dairy Sci. 101:11033–11039. https:  / / doi .org/ 10 .3168/
jds .2018 -14804.
Stephansen, R. B., P. Martin, C. I.
V . Manzanilla-Pech, B. Gredler-
Grandl, G. Sahana, P. Madsen, K. Weigel, R. J. Tempelman, F. Pe-
ñagaricano, K. Parker Gaddis, and H. M. White. 2023. Novel genetic
parameters for genetic residual feed intake in dairy cattle using time
series data from multiple parities and countries in North America
and Europe. J. Dairy Sci. 106:9078–9094. https:  / / doi .org/ 10 .3168/
jds .2023 -23330.
Sturm, V
., D. Efrosinin, M. Öhlschuster, E. Gusterer, M. Drillich, and M.
Iwersen. 2020. Combination of sensor data and health monitoring for
early detection of subclinical ketosis in dairy cows. Sensors (Basel)
20:1484. https:  / / doi .org/ 10 .3390/  s20051484.
Stygar,
A. H., Y . Gómez, G. V . Berteselli, E. Dalla Costa, E. Canali, J. K.
Niemi, P. Llonch, and M. Pastell. 2021. A systematic review on com-
mercially available and validated sensor technologies for welfare
assessment of dairy cattle. Front. Vet. Sci. 8:634338. https:  / / doi .org/
10 .3389/  fvets  .2021 .634338.
Stygar,
A. H., M. A. Krogh, T. Kristensen, S. Østergaard, and A. R. Kris-
tensen. 2017. Multivariate dynamic linear models for estimating the
effect of experimental interventions in an evolutionary operations
setup in dairy herds. J. Dairy Sci. 100:5758–5773. https:  / / doi .org/ 10
.3168/  jds .2016  -12251.
Suntinger, M., B. Fuerst-W
altl, W. Obritzhauser, C. Firth, A. Köck, and
C. Egger-Danner. 2022. Usability of bacteriological milk analyses
for genetic improvement of udder health in Austrian Fleckvieh
cows. J. Dairy Sci. 105:5167–5177. https:  / / doi .org/ 10 .3168/  jds .2021
-20832.
Szenci, O. 2022. Accuracy to predict the onset of calving in dairy farms
by using dif
ferent precision livestock farming devices. Animals (Ba-
sel) 12:2006. https:  / / doi .org/ 10 .3390/  ani12152006.
Tarekegn, G. M., P
. Gullstrand, E. Strandberg, R. Båge, E. Rius-Vilarra-
sa, J. M. Christensen, and B. Berglund. 2019. Genetic parameters of
endocrine fertility traits based on in-line milk progesterone profiles
Brito et al.: INVITED REVIEW: SENSOR DATA FOR GENETIC IMPROVEMENT

Journal of Dairy Science Vol. 108 No. 10, 2025
10473
in Swedish Red and Holstein dairy cows. J. Dairy Sci. 102:11207–
11216. https:  / / doi .org/ 10 .3168/  jds .2019  -16691.
Tenghe,
A. M. M., A. C. Bouwman, B. Berglund, E. Strandberg, J. Y .
Blom, and R. F. Veerkamp. 2015. Estimating genetic parameters
for fertility in dairy cows from in-line milk progesterone profiles.
J. Dairy Sci. 98:5763–5773. https:  / / doi .org/ 10 .3168/  jds .2014 -8732.
Tribout,
T., S. Minéry, R. Vallée, S. Saille, D. Saunier, P. Martin, V .
Ducrocq, P. Faverdin, and D. Boichard. 2023. Genetic relationships
between weight loss in early lactation and daily milk production
throughout lactation in Holstein cows. J. Dairy Sci. 106:4799–4812.
https:  / / doi .org/ 10 .3168/  jds .2022 -22813.
Tsai, I. C., L. M. Mayo, B.
W. Jones, A. E. Stone, S. A. Janse, and J.
M. Bewley. 2021. Precision dairy monitoring technologies use in
disease detection: Differences in behavioral and physiological
variables measured with precision dairy monitoring technologies
between cows with or without metritis, hyperketonemia, and hypo-
calcemia. Livest. Sci. 244:104334. https:  / / doi .org/ 10 .1016/  j .livsci
.2020  .104334.
Tse, C., H.
W. Barkema, T. J. DeVries, J. Rushen, and E. A. Pajor. 2017.
Effect of transitioning to automatic milking systems on producers’
perceptions of farm management and cow health in the Canadian
dairy industry. J. Dairy Sci. 100:2404–2414. https:  / / doi .org/ 10 .3168/
jds .2016 -11521.
T
ullo, E., A. Finzi, and M. Guarino. 2019. Review: Environmental
impact of livestock farming and precision livestock farming as a
mitigation strategy. Sci. Total Environ. 650:2751–2760. https:  / / doi
.org/ 10 .1016/  j .scitotenv  .2018 .10 .018.
Uemoto, Y
., T. Tomaru, M. Masuda, K. Uchisawa, K. Hashiba, Y . Ni-
shikawa, K. Suzuki, T. Kojima, T. Suzuki, and F. Terada. 2024.
Exploring indicators of genetic selection using the sniffer method
to reduce methane emissions from Holstein cows. Anim. Biosci.
37:173–183. https:  / / doi .org/ 10 .5713/  ab .23 .0120.
Umaña Sedó, S. U., D. L. Renaud, J. Morrison, D. L. Pearl, J. F. Mee,

and C. B. Winder. 2024. Using an automated tail movement sen-
sor device to predict calving time in dairy cows. JDS Commun.
5:317–321. https:  / / doi .org/ 10 .3168/  jdsc .2023  -0445.
Vakulya, G., É. Hajnal, P
. Udvardy, and G. Simon. 2024. In-depth de-
velopment of a versatile rumen bolus sensor for dairy cattle. Sensors
(Basel) 24:6976. https:  / / doi .org/ 10 .3390/  s24216976.
van Breukelen, A. E., M.
A. Aldridge, R. F. Veerkamp, and Y . de Haas.
2022. Genetic parameters for repeatedly recorded enteric methane
concentrations of dairy cows. J. Dairy Sci. 105:4256–4271. https:  / /
doi .org/ 10 .3168/  jds .2021 -21420.
van Breukelen, A. E., M. N.
Aldridge, R. F. Veerkamp, L. Koning, L. B.
Sebek, and Y . de Haas. 2023. Heritability and genetic correlations
between enteric methane production and concentration recorded by
GreenFeed and sniffers on dairy cows. J. Dairy Sci. 106:4121–4132.
https:  / / doi .org/ 10 .3168/  jds .2022 -22735.
van Breukelen, A. E., R. F
. Veerkamp, Y . de Haas, and M. N. Aldridge.
2024. Genetic parameter estimates for methane emission from breath
during lactation and potential inaccuracies in reliabilities assum-
ing a repeatability versus random regression model. J. Dairy Sci.
107:5853–5868. https:  / / doi .org/ 10 .3168/  jds .2024  -24285.
van den Berg, I., P
. N. Ho, M. Haile-Mariam, and J. E. Pryce. 2021. Ge-
netic parameters for mid-infrared spectroscopy–predicted fertility.
JDS Commun. 2:361–365. https:  / / doi .org/ 10 .3168/  jdsc .2021 -0141.
Van den Broeck, J., S.
Argeseanu Cunningham, R. Eeckels, and K.
Herbst. 2005. Data cleaning: Detecting, diagnosing, and editing data
abnormalities. PLoS Med. 2:e267. https:  / / doi .org/ 10 .1371/  journal
.pmed  .0020267.
van der V
oort, M., D. Jensen, C. Kamphuis, I. N. Athanasiadis, A. De
Vries, and H. Hogeveen. 2021. Invited review: Toward a common
language in data-driven mastitis detection research. J. Dairy Sci.
104:10449–10461. https:  / / doi .org/ 10 .3168/  jds .2021  -20311.
van Engelen, S., H. Bovenhuis, P
. P. J. Van der Tol, and M. H. P. W.
Visker. 2018. Genetic background of methane emission by Dutch
Holstein Friesian cows measured with infrared sensors in automatic
milking systems. J. Dairy Sci. 101:2226–2234. https:  / / doi .org/ 10
.3168/  jds .2017  -13441.
Vázquez-Diosdado, J. A., C. Doidge, E.
V . Bushby, F. Occhiuto, and J.
Kaler. 2024. Quantification of play behaviour in calves using au-
tomated ultra-wideband location data and its association with age,
weaning, and health status. Sci. Rep. 14:8872. https:  / / doi .org/ 10
.1038/  s41598  -024 -59142  -z.
Veissier
, I., M.-M. Mialon, and K. Sloth. 2017. Short communication:
Early modification of the circadian organization of cow activity in
relation to disease or estrus. J. Dairy Sci. 100:3969–3974. https:  / / doi
.org/ 10 .3168/  jds .2016  -11853.
von Borell, E., J. Langbein, G. Després, S. Hansen, C. Leterrier
, J.
Marchant, R. Marchant-Forde, M. Minero, E. Mohr, A. Prunier, D.
Valance, and I. Veissier. 2007. Heart rate variability as a measure
of autonomic regulation of cardiac activity for assessing stress and
welfare in farm animals—A review. Physiol. Behav. 92:293–316.
https:  / / doi .org/ 10 .1016/  j .physbeh  .2007 .01 .007.
Wang,
A., L. F. Brito, H. Zhang, R. Shi, L. Zhu, D. Liu, G. Guo, and Y .
Wang. 2022. Exploring milk loss and variability during environmen-
tal perturbations across lactation stages as resilience indicators in
Holstein cattle. Front. Genet. 13:1031557. https:  / / doi .org/ 10 .3389/
fgene .2022 .1031557.
Wang,
A., G. Su, L. F. Brito, H. Zhang, R. Shi, D. Liu, G. Guo, and Y .
Wang. 2024. Investigating the relationship between fluctuations in
daily milk yield as resilience indicators and health traits in Holstein
cattle. J. Dairy Sci. 107:1535–1548. https:  / / doi .org/ 10 .3168/  jds
.2023 -23495.
Wang, X., and C.
Wang. 2020. Time series data cleaning: A survey.
IEEE Access 8:1866–1881. https:  / / doi .org/ 10 .1109/ ACCESS  .2019
.2962152.
Wangen, S.
R., F. Zhang, L. Fadul-Pacheco, T. E. da Silva, and V . E.
Cabrera. 2021. Improving farm decisions: The application of data
engineering techniques to manage data streams from contemporary
dairy operations. Livest. Sci. 250:104602. https:  / / doi .org/ 10 .1016/  j
.livsci  .2021 .104602.
Welderufael, B. G., L. L. G. Janss, D. J. De Koning, L. P
. Sørensen, P.
Løvendahl, and W. F. Fikse. 2017. Bivariate threshold models for
genetic evaluation of susceptibility to and ability to recover from
mastitis in Danish Holstein cows. J. Dairy Sci. 100:4706–4720.
https:  / / doi .org/ 10 .3168/  jds .2016  -11894.
W
eller, J. I., and E. Ezra. 2024. Genetic analysis of rumination time
based on an analysis of 77,697 Israeli dairy cows. J. Dairy Sci.
107:4793–4803. https:  / / doi .org/ 10 .3168/  jds .2023 -24095.
Wen, H., J. S. Johnson, P
. H. Freitas, J. M. Maskal, L. S. Gloria, A.
C. Araujo, V . B. Pedrosa, F. Tiezzi, C. Maltecca, Y . Huang, A. P.
Schinckel, and L. F. Brito. 2023. Longitudinal genomic analyses of
automatically-recorded vaginal temperature in lactating sows under
heat stress conditions based on random regression models. Genet.
Sel. Evol. 55:95. https:  / / doi .org/ 10 .1186/ s12711 -023 -00868  -1.
Wen, H., J. S. Johnson, L. S. Gloria,
A. C. Araujo, J. M. Maskal, S. O.
Hartman, F. E. de Carvalho, A. O. Rocha, Y . Huang, F. Tiezzi, C.
Maltecca, A. P. Schinckel, and L. F. Brito. 2024. Genetic parameters
for novel climatic resilience indicators derived from automatically-
recorded vaginal temperature in lactating sows under heat stress
conditions. Genet. Sel. Evol. 56:44. https:  / / doi .org/ 10 .1186/ s12711
-024 -00908  -4.
Wethal, K. B., and B. Heringstad. 2019. Genetic analyses of novel tem
-
perament and milkability traits in Norwegian Red cattle based on
data from automatic milking systems. J. Dairy Sci. 102:8221–8233.
https:  / / doi .org/ 10 .3168/  jds .2019  -16625.
Wethal, K. B., M. Svendsen, and B. Heringstad. 2020a.
A genetic study
of new udder health indicator traits with data from automatic milk-
ing systems. J. Dairy Sci. 103:7188–7198. https:  / / doi .org/ 10 .3168/
jds .2020  -18343.
Wethal,
K. B., M. Svendsen, and B. Heringstad. 2020b. Are farmer
assessed temperament, milking speed, and leakage genetically the
same traits in automatic milking systems and traditional milking
systems? J. Dairy Sci. 103:3325–3333. https:  / / doi .org/ 10 .3168/  jds
.2019  -17503.
Woodward, S. J. R., J. P
. Edwards, K. J. Verhoek, and J. G. Jago. 2024.
Identifying and predicting heat stress events for grazing dairy cows
using rumen temperature boluses. JDS Commun. 5:431–435. https:  /
/ doi .org/ 10 .3168/  jdsc .2023  -0482.
Zetouni, L., M. Kargo, E. Norber
g, and J. Lassen. 2018. Genetic cor -
relations between methane production and fertility, health, and body
Brito et al.: INVITED REVIEW: SENSOR DATA FOR GENETIC IMPROVEMENT

10474
Journal of Dairy Science Vol. 108 No. 10, 2025
type traits in Danish Holstein cows. J. Dairy Sci. 101:2273–2280.
https:  / / doi .org/ 10 .3168/  jds .2017 -13402.
ORCIDS
Luiz F. Brito,  https:  / / orcid .org/ 0000 -0002  -5819 -0922
Bjørg Heringstad,  https:  / / orcid  .org/ 0000 -0001  -7388  -3893
Ilka Christine Klaas,  https:  / / orcid  .org/ 0000 -0002 -1397  -8505
Katharina Schodl,  https:  / / orcid  .org/ 0000 -0002  -9592  -4040
Victor E. Cabrera,  https:  / / orcid  .org/ 0000 -0003 -1739  -7457
Anna Stygar,  https:  / / orcid  .org/ 0000 -0003  -3112 -2847
Michael Iwersen,  https:  / / orcid  .org/ 0000 -0001  -7893  -6050
Marie J. Haskell,  https:  / / orcid  .org/ 0000 -0001  -9373  -0624
Kathrin F. Stock,  https:  / / orcid  .org/ 0000 -0002  -7642  -8885
Nicolas Gengler,  https:  / / orcid  .org/ 0000 -0002  -5981  -5509
Jeffrey Bewley,  https:  / / orcid  .org/ 0000 -0002  -7347  -2741
Miel Hostens,  https:  / / orcid  .org/ 0000 -0001  -5376  -976X
Elsa Vasseur,  https:  / / orcid  .org/ 0000 -0002  -5087  -6508
Christa Egger-Danner  https:  / / orcid  .org/ 0000 -0002  -8879  -6845
Brito et al.: INVITED REVIEW: SENSOR DATA FOR GENETIC IMPROVEMENT
