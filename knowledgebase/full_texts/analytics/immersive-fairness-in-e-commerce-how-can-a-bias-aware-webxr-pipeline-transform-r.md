---
title: 'Immersive Fairness in E-Commerce: How Can a Bias-Aware WebXR Pipeline Transform Regional Delivery
  Analytics?'
url: https://doi.org/10.52756/ijeim.2026.v02.i01.004
category: analytics
subcategory: case-study
date: 2026-01
venue: International Journal of Engineering and Information Management
authors:
- Krisha Mehta
source: openalex-oa
pdf_url: https://ijeim.in/index.php/IJEIM/article/download/54/57
pages: 31
chars: 113465
fetched_at: '2026-11-08T17:46:17+00:00'
kb_version: 1
---

# Immersive Fairness in E-Commerce: How Can a Bias-Aware WebXR Pipeline Transform Regional Delivery Analytics?

DOI: 10.52756/ijeim.2026.v02.i01.004 Int. J. Eng. Infor. Manag. Vol. 2, Issue 1: 52-82 (2026-Jan)
International Journal of Engineering and Information Management
Journal homepage: www.ijeim.in
Immersive Fairness in E-Commerce: How Can
a Bias-Aware WebXR Pipeline Transform
Regional Delivery Analytics?
Krisha Mehta
Department of Mathematics, Indian Institute of Technology Kharagpur, Kharagpur, West Bengal 721302, India
Corresponding Author:krishamehta1313.24@kgpian.iitkgp.ac.in
Article Information Abstract
Type of Article:Original
Received:Nov 3, 2025
Accepted:Jan 14, 2026
Published:Jan 15, 2026
Keywords:
Delivery Fairness
E-Commerce Logistics
Immersive Analytics
Responsible AI
WebXR
Cite this article:
Krisha Mehta (2026). Immersive F airness
in E-Commerce: How Can a Bias-A ware
W ebXR Pipeline T ransform Regional
Delivery Analytics?International Journal of
Engineering and Information Management,
2(1), 52-82.
DOI: 10.52756/ijeim.2026.v02.i01.004
E-commerce delivery systems often exhibit regional and socioeconomic
disparities in delays, cancellations, and refunds that are not evident in
aggregate dashboards, especially for intersectional demographic and geographic
cohorts. Existing work primarily emphasises sales and marketing analytics,
leaving delivery fairness underexplored and exposing the shortcomings of
traditional two-dimensional tools in uncovering multidimensional bias across
geography, income, and order attributes.This paper introduces a bias-aware
delivery analytics pipeline that integrates intersectional fairness metrics with
WebXR-based immersive visualisation, using the Brazilian Olist dataset as
a real-world case study. The pipeline fuses relational order, review, and
geolocation data with fairness metrics derived from an extended version of
Fairlearn’s MetricFrame to capture disparities among overlapping groups.
The delivery performance metrics, such as delay and cancellation rates, are
encoded as three-dimensional representations—bar height, colour scales of
equal perceptual difference, and dynamic particle orbitals—in a browser-
native WebXR environment that is accessible from both desktop and VR.
An interactive governance layer equipped with immersive tools enables the
establishment of an audit trail through confidence intervals that can be
interacted with, causal flow overlays, metric snapshots, all of which are designed
to help stakeholders identify when, where, and for whom unfairness has
occurred. The initial results reveal a considerable range of disparities in worst-
performing cohorts, where orders from distant locations and low prices had
delivery times and cancellation rates two to three times longer than those of
central, high-pricedorders. Aplannedcomparativeuserstudywillestimatehow
theWebXRsystemimpactstheaccuracy, time-to-insight, andconfidenceinbias
detection compared to standard dashboards, positioning immersive analytics as
a practical and helpful tool for more equitable, data-driven logistics decisions.
1 Introduction
Machine learning (ML) and data-driven analytics are serving as a backbone to decisions in credit scoring,
hiring, healthcare (Pramanik et al., 2024), criminal justice, safety (Sarkar et al., 2019; Pramanik et al.,
2025), and supply-chain management. While these systems promise efficiency and Scalability, extensive
work has revealed that algorithms might systematically replicate or even exacerbate existing social
inequalities, a phenomenon known as algorithmic bias. Thus, rather than being impartial, models portray
historical data, design choices, and institutional power, which makes fairness a primary concern every
time ML impacts large-scale decisions affecting people’s lives.
Empirical evidence pointing out algorithmic bias in various fields has accumulated over the past
decade. Early studies on targeted advertising, recidivism prediction, and high-stakes risk modelling
ISSN: 3107-5886 (Online)/©2026 International Academic Publishing House (IAPH)
This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/)

Mehta (2026) Int. J. Eng. Infor. Manag. Vol. 2, Issue 1: 52-82 (2026-Jan)
demonstrated that ostensibly data-driven systems were able to disadvantage already marginalised
communities systematically. Influential critics of "weapons of math destruction" further argued that
large-scale, non-transparent models used in hiring, insurance, and education can enlarge structural harms
while remaining difficult to scrutinise. A significant inflexion point came from work on facial analysis that
revealed dramatically higher error rates for darker-skinned women than for lighter-skinned men, providing
striking quantitative evidence of intersectional bias at the intersection of race and gender. Thus, the
focus shifted from single-attribute disparities (e.g., by race or gender) to intersectional fairness, where
overlapping sensitive attributes and small, underrepresented subgroups must be considered. Subsequent
research proposed metrics and statistical estimation techniques for auditing fairness in the context of
sparse data, emphasising that fairness should be treated as a core property of ML systems rather than
an optional post-hoc adjustment.
Furthermore, recent scholarship has also emphasised that fairness frameworks developed in North
American and European settings may not be accurately suitable for the regions characterised by
profound socioeconomic and infrastructural inequalities (Sambasivan et al., 2021). Work grounded in
the Global South shows that fairness notions must be re-imagined in contexts where data is incomplete,
infrastructures are uneven and limited, and histories of marginalisation complex. In such environments,
algorithmic harms frequently manifest as unequal access to services and infrastructure forms a type
of disparity that standard benchmarks may overlook. This perspective is particularly pertinent for
large countries like Brazil, where regional disparities in connectivity, logistics capacity, and income can
influence algorithmic decisions in subtle yet consequential ways (Wells et al., 2021). Here, fairness
transcends simple parity in model outputs; it also encompasses the pathways through which outputs
navigate through physical networks of warehouses, carriers, and roads, ultimately shaping individual
experiences with service quality (Yang et al., 2023).
Despite considerable attention to fairness in areas such as credit scoring, hiring, healthcare, and
criminal justice, logistics and last-mile delivery systems remain comparatively underexamined and have
not received similar scrutiny. Yet delivery performance delays, cancellations, and refunds directly impact
access to goods, participation in digital marketplaces, and consumer trust in e-commerce platforms. In
geographically expansive and diverse regions, optimisation and service-level algorithms may inadvertently
disadvantage remote or lower-income communities, leading to systematically longer delivery times
or elevated cancellation rates for specific groups. Conventional business-intelligence (BI) dashboards
generally operate at aggregate levels, such as national or state averages, which smooth over the extremes
of the distribution where marginalised subgroups are often concentrated. Even recent "AI-powered
BI" tools, while adding automated insights and real- time monitoring largely remains two-dimensional,
offeringlimitedsupportforexploringhigh-dimensional, intersectional, andgeospatialpatternsoffairness.
Consequently, subtle yet persistent disparities in delivery quality can remain hidden inside aggregates
and static visualisations.
The types of bias in regional delivery analytics systems are interrelated but have multiple types of
impact on service equity. Geographic bias is a feedback mechanism where algorithms prioritize affluent,
densely populated regions over rural or low-income neighborhoods, building on previous patterns of
service allocation, which leads to the creation of service disparities. The bias of data collection manifests
itself in the incomplete or unrepresentative data where the bias systematically eliminates some areas,
and the bias in algorithm design is an optimization criterion that targets efficiency measures such as
travel time that are more favourable to well-maintained infrastructure in more affluent regions. Proxy
variable bias occurs when zip codes, credit scores, or access to digital services are used in place of race and
socioeconomic status to allow some kind of digital redlining despite a lack of demographic information.
Lastly, there is temporal bias because of using outdated information that does not represent the present
situation, and behavioral bias because underserved areas produce less data because of low service quality,
which lowers incentives of algorithms to help operations of delivery in under-served regions.
Immersive analytics broadens the scope of data exploration, extending to virtual reality (VR),
augmented reality (AR) and spatial-computing environments, building on a foundation that includes
early room-scale, stereoscopic systems for scientific visualisation (Allam et al., 2022). Contemporary
studies suggest that immersive environments can enhance engagement and help users perceive complex
spatial structures and anomalies, particularly when dealing with inherently geographic or structurally
53

Mehta (2026) Int. J. Eng. Infor. Manag. Vol. 2, Issue 1: 52-82 (2026-Jan)
rich data. However, traditional VR deployments have faced challenges in enterprise settings related to
hardware, complex installation requirements and integration issues.WebXR revolutionises this landscape
by enabling VR and AR experiences to be accessed directly in web browsers through standardised
APIs, making immersive analytics available via URLs while also ensuring alignment with current web
security and integration practices (Batch et al., 2023). As a result, this opens the door to fairness-aware
dashboards in which Intersectional delivery disparities are encoded as three-dimensional structures, such
as bar heights, colour gradients, and flow lines over real geographies, allowing stakeholders to literally
"walk through" regions most affected by unequal service levels.
Motivated by (1) the historical evidence of algorithmic harms across domains, (2) the
underrepresentation of delivery fairness and logistics in fairness research,(3) the limitations of 2D
dashboards for intersectional and spatial analysis and (4) the underutilisation of immersive analytics for
operational and logistic fairness,this paper proposes a Bias-Aware Delivery Fairness pipeline that couples
principled fairness metrics with WebXR-based immersive analytics. Using the Brazilian Olist e-commerce
dataset, the pipeline integrates geospatial and cohort-level information, computes intersectional fairness
metrics using a fairness toolkit, and renders these metrics as interactive 3D encodings in a browser-
native environment. Beyond visualisation, the work introduces an Immersive Governance layer that
facilitates audit trails, scenario comparison, and transparency features addressing long-standing concerns
about accountability in algorithmic systems. Finally, the paper details a controlled user study comparing
immersive WebXR visualisations to conventional BI dashboards for bias-detection tasks. The overarching
objective is to demonstrate that immersive, web-native analytics are not merely cosmetic enhancements,
but rather powerful instruments for revealing and governing fairness within complex, geographically
distributed delivery networks.
The remainder of this paper is structured as follows: Section 2 describes the recent related work
and literature review along with the research gaps and research contributions made by this paper.
Section 3 explains the detail data preprocessing and fairness metrics computation as well as the WebXR
visualization design and visual encodings. Furthermore, it explains proposed governance layer useful for
the policy makers. Section 4 presents preliminary findings from the Olist dataset analysis, details the
theoretical contributions and practical and managerial implications. Finally, Section 5 concludes with
future research scope and directions.
2 Literature Review
In this section, we explore relevant literature across three areas: fairness in e-commerce and logistics
systems, intersectional analysis and contextualised fairness assessment, and visual analytics and
immersive technologies for fairness exploration.
2.1 Fairness in E-commerce and Logistics
An analysis of systematic differences in delivery performance of e-commerce across geographies and
demographics lacks in both research and practice, although e-commerce delivery systems are essential
in determining consumer access to goods and services. While algorithmic fairness has been extensively
researched in fields such as credit scoring and healthcare, less attention has been paid to applying
it in e-commerce and last-mile logistics, despite of its massive impact on consumer trust and market
participation.
Chen et al. (2023) studied the presence of geographical equity in 1-day delivery, revealing that profit-
maximising routing algorithms consistently omit peripheral and low-income areas, leading to disparities
in service coverage. Their investigation highlighted the importance of maintaining a minimum service
availability as their primary objective, showing that ignoring geographical and demographic equity
results in a substantial reduction in long-term utility and sustenance. The authors introduce socially
aware routing models designed to balance profitability with equitable distribution, demonstrating that
marginal variations in efficiency and service can considerably enhance accessibility in underserved areas
. More recently, Chen et al. (2025) examined issues of fairness within supply chains under conditions
54

Mehta (2026) Int. J. Eng. Infor. Manag. Vol. 2, Issue 1: 52-82 (2026-Jan)
of uncertainty, illustrating that logistics decisions governed by platform operators, including warehouse
location and route planning, resulted in spatial and demographic disparities. This analysis highlighted
that decisions regarding logistics design have a direct impact on delivery performance.
The Brazilian Olist dataset, a public e-commerce dataset having 100,000+ orders from 2016-2018,
has been analysed to understand the delivery performance patterns. Multiple studies emphasise strong
correlations between delivery delays and negative customer sentiment, with late deliveries receiving lower
ratings than timely deliveries, emphasising the importance of timely service (Xu et al., 2023). Regional
analysis reveal a considerable variation in delivery times across Brazilian states, with remote and less
urbanised regions experiencing delays that are two to three times greater than those in metropolitan
cities.
2.2 Intersectional Analysis and Contextualised Fairness Assessment
The current studies use standard 2D dashboard and aggregate metrics that can conceal and obscure the
intersectional trends, e.g. the compounded disadvantages of the rural customers placing orders due to
low-value products in particular regions (D’Ignazio & Klein, 2023). The intersectional analysis structure,
which initially pertained to the social science field and fairness studies, can be applied to all types of
operational systems where a number of attributes and characteristics interplay to form a compound
effect.These 2D views complicate the definition of the existence of systematic inequities in vulnerable
marginalisedsubgroupsthatoccurinthetailsofthedistribution(Correll,2019). Insteadofjustlookingat
disparities by individual dimensions(i.e., by region alone or by order value alone), intersectional methods
consider their intersections to expose the cases in which certain cohorts are subjected to greater impacts.
The worst case disparity ratio is a standard measure, which is the ratio between the best and the worst
score of a particular performance measure by subgroups. Having these ratios vary significantly, other
than one, is indicative of the system having significant intersectional disparities, which might not be
felt in aggregate statistics. Statistical structures have been constructed to quantitatively predict such
disparities even where intersectional subgroups are small or less represented in data.
Disaggregated evaluation by arbitrary groupings and metric aggregation Online Libraries or
frameworks like Fairlearn allow flexible APIs. Although they were originally developed to audit ML
models, they can be used on operational measures of delivery times and cancellations across overlapping
cohorts based on geography, level of urbanisation, order value and customer characteristics.
(Sambasivan et al., 2021) has highlighted that analysis frameworks that are made in the West may
not reflect the realities in the areas where there are high levels of socioeconomic and infrastructural
inequity. In the Global South, data is normally incomplete and sparse, infrastructure is varied and social
dynamics are multifaceted. Their work demonstrates that the inequalities tend to be manifested by
infrastructural gaps in terms of unequal access to logistics systems, discrimination in service provision, or
unevenresourcedistributionthatislatentandobscuredwithoutspecificandcontextualisedanalysis.Their
work reveals that inequalities are manifested in countries such as Brazil where vast geographies, unequal
urbanisation, or demographic disparities are the conditions of systematic service discrimination and the
absence of equitability. Such patterns are frequently not identified in the regular analytics which are
usually conducted at a national or state level of aggregation.
2.3 Visual Analytics and Immersive Technologies for Fairness
Exploration
Different types of tools are popular to evaluate the performance and delivery operations, and include
dashboards, heatmaps, and tabular reports. Those platforms have the possibility to summarize the past
data trends and facilitate the high-level performance analysis by means of such indicators as average
delivery time, the overall cancellation rate, and the regional volume. Nevertheless, traditional BI systems
are weak in disclosing the intersectional and multidimensional differences. Even the current AI-driven BI
dashboards that combine machine learning to predictive analytics, streams of real-time data, and natural
language processing, are fundamentally two-dimensional (2D), with no spatial depth or multidimensional
mechanisms of exploratory analysis of the patterns of inequity. This is more limiting to the delivery
55

Mehta (2026) Int. J. Eng. Infor. Manag. Vol. 2, Issue 1: 52-82 (2026-Jan)
fairness analysis in which the geographic, demographic, and transactional variables have a complex and
complex interaction. The traditional 2D layouts can be soon overwhelmed and difficult to understand
especially when the analysts need to factor in (region x urbanisation x order value x product category)
all at the same time.
Cabrera et al. (2019) developed FairVis, an interactive visual analytics system that utilises
coordinated multiple views, parallel coordinates, scatterplots, and matrix visualisations to help
analysts explore performance metrics across different subgroup combinations, thereby enhancing their
understanding of the data. User studies demonstrated that interactive visual tools improve pattern
detection accuracy compared to static tabular summaries.However, even advanced 2D visual analytics
systems struggle when the number of intersecting features increase. In flat layouts, visual clutter and
cognitive load tend to escalate quickly, which constrains the complexity of analyses that practitioners are
able to undertake effectively (Ellis & Dix, 2007). This motivates exploration of spatial, three-dimensional
visualisation approaches that can leverage depth cues and embodied navigation to support more intuitive
exploration of multidimensional data (Skarbez et al., 2019). Carolina Cruz-Neira’s 1992 Cave Automatic
Virtual Environment (CAVE) system was the first to use virtual reality (VR), augmented reality (AR),
and spatial computing to analyse data (Cruz-Neira et al., 1993). The CAVE projects stereo images onto
several walls that are the size of a room, creating a virtual space that one can walk around in. This
is what makes it possible to visualise and analyse spatial data together in scientific computing (Cruz-
Neira et al., 1992).Cruz-Neira also developed CAVELib and VR Juggler, two software frameworks that
enabled the creation of interactive VR applications, which remain important in business and research
today (Bierbaum et al., 2001).
Recent comparative studies assess whether immersive environments provide quantifiable benefits
over 2D interfaces for data analysis tasks. Studies on VR-based data exploration show that immersive
analytics can make users more interesed and help them find new insights, especially with spatial,
network, and structural datasets. The time it takes to complete tasks is about the same as with
2D dashboards. Users report higher satisfaction and subjective understanding when using VR for
complex spatial datasets, such as geographic distribution patterns, network topologies, and multivariate
relationships. However, cognitive load remains a concern for extended sessions, and design factors
including visual encoding choices (colour scales, spatial metaphors), interaction mechanisms (raycasting,
controllers), and performance optimisation (maintaining 60+ FPS) are critical for user comfort and task
effectiveness.Traditional VR platforms such as Unity and Unreal Engine require dedicated installations,
specialised hardware, and complex deployment pipelines, creating significant barriers to enterprise
adoption (Franke & Haehn, 2020).
WebXR has a number of benefits for enterprise analytics deployments. For example, it allows
users to access the data without having to install anything, it works on all devices (including
desktop browsers, mobile devices, and VR headsets), it integrates data in real time using standard
HTTP/WebSocket protocols, and it is open source, which means that security audits can be done using
browser developer tools. These properties make WebXR particularly suitable for operational analytics
in regulated industries where transparency, auditability, and rapid deployment are critical (Butcher
et al., 2021).Recent work demonstrates the feasibility of WebXR for collaborative data exploration and
lightweight scientific visualisation (Brunhart-Lupo et al., 2021), although applications to fairness auditing
in operational systems, such as delivery logistics, remain unexplored (Yang et al., 2023).
Research Gaps: Synthesizing the literature and the aforementioned past work concerning fairness and
intersectional bias reveals three critical gaps that motivate this work:
(i)Delivery Fairness Underexplored: Although there is rich work on e-commerce operations,
customer satisfaction, and retention, very little research directly analyzes delivery fairness as
a first-class objective. Existing studies rarely examine how delivery service quality (delays,
cancellations, reliability) systematically varies across intersecting geographic and demographic
groups, beyond a few early attempts that add simple geographic equity constraints to optimization
models.
(ii)Aggregate Analytics Obscure Disparities: Mainstream BI dashboards and even sophisticated
2D visual analytics rely heavily on aggregate statistics and flat layouts, which makes it difficult to
56

Mehta (2026) Int. J. Eng. Infor. Manag. Vol. 2, Issue 1: 52-82 (2026-Jan)
see intersectional disparities in high-dimensional data. Important patterns that emerge only at the
intersection of region, urbanization level, and customer or order attributes are often smoothed out
or completely hidden in such aggregate 2D views.(Frost, 2024; Solokov, 2025).
(iii)Immersive Analytics Untapped for Operational and logistic Fairness: Immersive analytics
has shown promise for exploring complex spatial data in scientific settings, but it has not yet
been applied to fairness auditing in real operational systems such as e-commerce logistics. In
particular, the governance-aware, browser-native capabilities of WebXR for deploying immersive
fairness visualizations remain largely unexplored and underutilized.
Research Contributions: To address the above mentioned research gaps, this work makes four principal
contributions:
(i)Delivery Fairness Analytics Pipeline: This paper builds a pipeline of analytics that can be
used to reproduce that analytics and combine the Brazilian Olist e-commerce dataset with a robust
set of intersectional fairness measures. The pipeline measures disparities in delivery time, rates
of late delivery, and rates of cancellations in many dimensions such as geographic region, level of
urbanization, andordervaluesegments, whichprovidessystematicmeasurementofdeliveryfairness.
(ii)WebXR-Based SpatialVisualisation:Thearticlepresentsa3DWebXRsetofvisualisationtools
that project the following metrics of a delivery to a geospatial map of Brazil. The differences are
conveyed by the intuitive visual encodings like the height of the bar to signal the delay in delivery,
the color gradient to signal the cancellation rate, the use of particle systems to signal retention
of customers, and animated flows to signal the causal relationship. This three-dimensional design
renders the defects of the region and intersectionality instantly visible and readily navigable.
(iii)Immersive Governance Layer: The work also suggests an immersive governance layer that will
improve the transparency and accountability in the process of analytics. It offers visualization of
user interactions and interactive confidence intervals as well as scenario comparison tools. The
combination of these characteristics makes the fairness metrics readable, traceable, and operational
to promote evidence-based operational and policy decisions in delivery networks.
3 Methodology
Thisapproachisapathwayprocessthatconvertscrudespatialandbusinessinformationintoengagements
in VR/AR, which are decision-ready. It is structured into layers whereby each layer provides a distinct
type of intelligence to the data. The flowchart of the methodology is shown in Fig. 1.
The Foundation Layer (Phase 1) converts raw geospatial data, including latitude and longitude, into
one unified three-dimensional coordinate system, which creates a digital twin environment on which all
the other layers are built. The heart of the system is the Analytical Engine (Phases 2-5) which is the
calculation of fairness metrics to identify bias, regional similarity analysis to group similar areas, causal
inference to identify causation versus correlation, and customer sentiment that is projected to geographic
areas. The Dynamics Layer (Phase 6) is a phase that applies concepts of differential geometry and
uses them to simulate temporal variations, transforming essentially stagnant spatial data into animated
flow fields which are used to visually depict patterns over time. Integration Platform (Phase 7) is the
combination of the three-dimensional environment, analysis, and nimble animations into an interactive
WebXR (VR/AR) interface that allows one to explore and navigate the data intuitively. Application
Layer (Phases 8- 9) will translate the gained analytical knowledge into prescriptive action, including an
ideal selection of the site, and will offer a governance interface that can facilitate collaborative decision-
making and syntactic policy documentation. Lastly, the Validation Layer (Phase 10) works in concert
with deployment and uses standard metrics of evaluation, like NASA-TLX and SUS, to evaluate usability
and to confirm that the system is useful to make informed and fair decisions.
57

Mehta (2026) Int. J. Eng. Infor. Manag. Vol. 2, Issue 1: 52-82 (2026-Jan)
Raw Spatial &
Business Data
Phase 1: Geospatial
Coordinate
Transformation
& 3D Scene
Phase 4: Causal
Inference
(Linear Structural
Models)
Phase 3:
Inter-Regional
Similarity Analysis
Phase 5: Cust.
Experience Sentiment
& Retention
Phase 2: Fairness
Metrics &
Uncertainty
Phase 6: Differential
Geometry &
Flow Animation
Phase 7: Immersive User Experience Architecture
(WebXR / VR / AR)
Phase 8: Prescriptive
Analytics (Site
Selection)
Phase 9: Immersive
Governance Layer
Phase 10: User
Study & Evaluation
(NASA-TLX, SUS,
Performance Metrics)
Decisions &
Policy Making
Foundation Layer
Analytical Engine
Dynamics Layer
Integration Platform
Application Layer
Validation Layer
Iterative Design F eedback
Figure 1:System Architecture and Methodological Pipeline
3.1 Phase 1: Geospatial Coordinate Transformation and 3D Scene
Construction
Cartographic Projection for Immersive Rendering:The transformation from 2D cartographic
representations to stereoscopic 3D immersive environments requires a coordinate transformation
framework that preserves spatial fidelity while adapting to the performance and rendering constraints
inherent in real-time virtual reality systems. Our implementation framework utilizes Three.js (revision
150+) as the WebGL abstraction layer, along with custom projection shaders tailored for geographic
data.
Given the geographical extent of Brazil that spans latitudeϕ∈[−33.75◦,5.27◦]and longitudeλ∈
[−73.99◦,−28.84◦], we introduce a normalized coordinate transformationT:R 2→R 3 that maps the
WGS84 coordinates to a bounded Cartesian space suitable for integration within VR scene graphs. To
align with the conventional Right-Handed coordinate system employed by WebGL where the negative
Z-axis extends into the screen and corresponds northwards, the transformation is formalised in Eq. (1):
58

Mehta (2026) Int. J. Eng. Infor. Manag. Vol. 2, Issue 1: 52-82 (2026-Jan)
Figure 2:Brazil Map and 3D scene Construction
x=α x· λ−λ min λmax−λ min −βx
z=−
(
αz· ϕ−ϕ min ϕmax−ϕ min −βz
)
y=h(m r)
(1)
whereα x,αz are scaling factors (typically 22 units to fit within the VR frustum),βx,βz are centering
offsets, andh(m r)is a height function encoding regional fairness metrics. Normalization ensures that
the entire Brazilian territory occupies a22×22unit plane in world space, preventing depth precision
artifacts in the VR headset’s depth buffer (typically a 24-bit fixed-point integer).
Geodetic Centroid Computation:Regional anchor points are computed as weighted geographic
centroids from the Olist geolocation table. For regionrwithn r ZIP code observations, the centroid
coordinates( ¯λr, ¯ϕr)are calculated according to Eq. (2):
¯λr = 1 Wr nr∑ i=1 wiλi, ¯ϕr = 1 Wr nr∑ i=1 wiϕi, W r = nr∑ i=1 wi (2)
where weightswi denotes the transaction volume in ZIP codei,thereby ensuring that high-activity
zones exert dominating influence in the centroid calculation. This produces a more semantically
meaningfuldefinationofcenterthansimplearithmeticmeans, asitcapturestheactualunderlyingdemand
density.
Geometric instantiation:Each Brazilian state is visualised as a vertical bar using Three.js
BoxGeometryprimitives. The geometry parameters are determined algorithmically to accurately
represent territorial extent as a square prism with spatial fidelity, as described in Eq. (3):
height=κ·m r +ϵ,width=
√
Ar,depth=width (3)
wherem r denotes the normalized fairness metric for regionr,κ= 8is a perceptual scaling constant
empirically determined to maximize discriminability while mitigating occlusion effects,ϵ= 0.5gurantees
zero-metric regions remain visible, andA r is the geographic area of the state. Visual Materials are
assigned using a custom ShaderMaterial implementing a sequential color mappingc: [0,1]→RGB
based on ColorBrewer’s RdYlBu diverging palette augmented with gamma correction (γ= 2.2) ensuring
perceptual linearity.
59

Mehta (2026) Int. J. Eng. Infor. Manag. Vol. 2, Issue 1: 52-82 (2026-Jan)
3.2 Phase 2: Fairness Metric Formulation and Uncertainty
Quantification
Operational Definitions of Logistics Fairness:We adopt a distribution-sensitive fairness framework
in which service quality disparities are quantified through group-wise conditional expectations rather than
aggregate, system-level averages. LetD={(oi,gi,ti,si)}N i=1 denote the order dataset, whereoi represents
orderi,g i∈Gis the customer’s geographic group (Brazilian state),ti∈R + is the realised delivery time
in days, andsi∈{delivered,canceled}is the order status. This formulation allows service quality to be
analysed at the level of protected or policy-relevant groups (e.g., regions), making disparities explicit and
measurable.
Primary Fairness Indicators:Three metrics constitute the core of the fairness assessment
framework; each compares a group-specific quantity to its overall population baseline.
Average Delivery Delay Disparity(∆ delay)as defined in Eq. (4), measures the expected delivery time
for groupgrelative to the national mean.
∆delay(g) =E[t|g]−E[t],whereE[t] = 1 N N∑ i=1 ti (4)
Positive values∆ delay(g)>0indicate that customers in regiongsystematically experience slower
deliveries than the average customer, whereas negative values indicate an advantage in service speed.
Late Order Rate Disparity(∆ late)as formalised in Eq. (5),captures reliability gaps rather than delay
magnitude, flagging deviations from the promised delivery window regardless of how long the eventual
delay is.
∆late(g) =P(t>t est|g)−P(t>t est)(5)
A high∆ late(g)therefore reflects a breach of expectation, which is often more salient to customers
than absolute transit time.
Cancellation Rate Disparity(∆ cancel): The cancellation rate disparity for groupgis defined in Eq. (6).
∆cancel(g) =P(s=canceled|g)−P(s=canceled)(6)
Eq. (6) captures regional differences in order fulfilment failure rates, serving as a proxy for systemic
logistics friction (e.g., stockouts, routing failures, or payment issues). Large positive values indicate that
customers in groupgface a disproportionate risk of orders not being completed.
Collectively, these indicators enable fairness to be assessed along multiple dimensions
mainly—timeliness, reliability, and completion—rather than relying on a single scalar performance
measure.
Statistical Inference and Uncertainty Quantification:The point estimates of the metrics
defined in Eqs. (4)–(6) are subject to sampling variability, particularly for smaller states with limited
transaction counts. To mitigate the risk overinterpreting noise as structure, we associate confidence
intervals to each group-wise estimate. For each metricmin groupg, with sample sizen g, we employ
parametric inference based on the Student’s t-distribution to construct 95% confidence intervals and
this approach remains appropriate for small samples (ng <30) under the assumption of approximate
normality. The resulting confidence interval construction is given in Eq. (7):
CI0.95(mg) = ¯xg±
(
tν,0.975· sg √ng
)
(7)
In Eq. (7),¯xg is the sample mean of the metric for groupg,sg is the sample standard deviation,
tν,0.975 is the critical t-value at the 97.5th percentile withν=ng−1degrees of freedom, ands g/√ng is
the standard error of the mean. The interval width, defined in Eq. (8),
wg = 2tν,0.975· sg √ng (8)
60

Mehta (2026) Int. J. Eng. Infor. Manag. Vol. 2, Issue 1: 52-82 (2026-Jan)
acts as a quantitative measure of epistemic uncertainty.
These intervals propagate directly into the immersive visualisation layer, where they modulate the
opacityα vis of the confidence ring objects surrounding each state according to Eq. (9):
αvis(g) =clamp
( wg
wscale
,α min,α max
)
(9)
Here,w scale is a domain-specific scaling factor that normalises interval widths into the[αmin,α max]
range, and clamp(·)enforcing that opacity remains within perceptually meaningful bounds. In a
deliberate inversion of conventional uncertainty visualisation (where uncertainty is often de-emphasised),
wider intervals yield higher opacity (αvis →0.8), producing a visually solid red warning ring for
uncertain or volatile regions. Conversely, high-confidence estimates render as semi-transparent (αvis→
0.1), reducing visual salience for well-characterised areas. This design choice intentionally draws
analytical attention toward data regimes where fairness assessments are least certain, promoting cautious
interpretation and further investigation prior to acting upon such signals.
3.3 Phase 3: Inter-Regional Similarity Analysis via Feature-Space
Distance
Rationale for Similarity-Based Edge Construction:Conventional geographic adjacency networks
which connect solelu=y bordering states and fail to capture functional similarities among non-contiguous
regions that share common logistics profiles, such as infrastructure limitations, low population density, or
dependence on long-haul routes. For instance, a state in the remote North may face the same operational
challenges as an interior state in the Center-West, despite absence of physical shared border. To uncover
these latent patterns, we construct a feature-space similarity graph where edges encode behavioral or
performance similarity rather than geographic proximity. This formulation enables the identification
of intervention strategies that can be systematically applied to non-adjacent regions exhibiting shared
failure modes.
Feature Vector Construction.Each stategis represented as a normalized feature vectorvg∈R k,
as formalized in Eq. (10):
vg =
[m1(g)−µ 1
σ1
,m2(g)−µ 2
σ2
,..., mk(g)−µ k
σk
]⊤
(10)
The componentsm j(g)correspond to the fairness metrics computed for groupg(average delivery
delay, late order rate, cancellation rate), and(µj,σj)represent the dataset-wide mean and standard
deviation for metricj. This z-score transformation (standardization) ensures that all dimensions
contribute equally to the subsequent distance calculation, regardless of their native scale or units.
Without normalization, a metric measured in days (e.g., delivery delay) would dominate over a metric
expressed as a proportion (e.g., cancellation rate of 0.05), leading to biased similarity assessments.
Similarity Measure and Edge Criterion:The similaritys(g i,gj)between any two states is
computed as the Euclidean distance in the normalized feature space, as shown in Eq. (11):
s(gi,gj) =∥v gi−vgj∥2 =
/radicaltp/radicalvertex/radicalvertex√ k∑
d=1
(
v(d) gi −v (d) gj
)2
(11)
A smaller distances(g i,gj)corresponds to greater similarity in logistics performance. An edge
(gi,gj)is instantiated in the VR scene if and only ifs(gi,gj)< θ, whereθ= 0.2is a strict threshold
empirically tuned through iterative visualization trials to balance network density and interpretability.
Lower thresholds yield sparse networks that highlight only the most statistically identical state pairs,
preventing the visual clutter and occlusion that are common in dense 3D graph layouts. Higher thresholds
would connect nearly all states, obscuring meaningful structure.
61

Mehta (2026) Int. J. Eng. Infor. Manag. Vol. 2, Issue 1: 52-82 (2026-Jan)
Figure 3:Similarity Edges’ Construction
Visual Encoding of Similarity Edges:Edges are rendered as Quadratic Bézier Curves
(THREE.QuadraticBezierCurve3) rather than straight line segments, creating graceful “arcing bridges”
that visually separate similarity links from the planar map geometry below. This curvature prevents
visual confusion between similarity edges and potential flow arcs (which represent delivery routes). The
visual grammar includes:
•Color:Cyan (#00FFFF), chosen to distinguish similarity links from both geographic features
(map base layer) and causal annotations (red/green color-coding).
•Opacity:α edge = 0.3(fixed), ensuring the links act as a subtle contextual layer rather than
occluding primary data such as bar heights or confidence rings. This semi-transparency allows
users to perceive the similarity structure without being overwhelmed.
•Geometry:Arcs with a control point elevated proportionally to the geodesic distance between
nodes, reinforcing the visual “bridge” metaphor and providing a depth cue that aids spatial
perception in stereoscopic VR.
Such visualization allows one to see non-obvious regional clusters. As an example, the system shows
that Espirito Santo (ES), which is a coastal state and Mato Grosso do Sul (MS), an inland state are both
visually connected but are separated by more than 1,500 km and no common geographical boundary.
Further feature analysis confirms that the two regions have statistically equivalent logistics profiles and
similar delivery delays (≈15.3days vs.15.2days) and almost the same rates of late product delivery
(12.0% vs. 11.3%) indicative of shared bottlenecks in operations, specifically with respect to last mile
distribution inefficiency, but not due to simple geographic distance factors. This would be shrouded
in conventional standard adjacency-based network layouts or 2D choropleth charts, thus showing the
analytical utility of feature-space similarity encoding as fairness diagnostics.
3.4 Phase 4: Causal Inference Framework via Linear Structural
Models
LimitationsofCorrelationalFairnessAnalysis:Thepresenceofobservationaldifferencesindelivery
times makes the causal effects and confounding factors confounded to each other (Pearl, 2009; Hernán
& Robins, 2020). The delays can be high in an area because of inherent geography (far distances
to distribution centers), demographics (orders of lower value, which receive slower shipping levels), or
systematic discrimination (deprioritization by carriers). These mechanisms cannot be differentiated by
correlational analysis alone, even when it comes to causal studies (Rubin, 2005). For instance, if remote
regions also tend to place orders during peak seasons with limited carrier capacity, a naive comparison
wouldmisattributedelayentirelytogeographywheninfactseasonality(aconfounder)partiallydrivesthe
observed disparity. Distinguishing these mechanisms requires formal causal identification to isolate the
specific, incremental impact of distance or hub location from confounding variables (Pearl & Mackenzie,
2018).
62

Mehta (2026) Int. J. Eng. Infor. Manag. Vol. 2, Issue 1: 52-82 (2026-Jan)
Figure 4:Causal Effect Visual Encodings
Causal Model Specification:We adopt a Structural Causal Model (SCM) framework implemented
using the DoWhy library. We define a directed acyclic graph (DAG)G= (V,E)where the outcomeY
(delivery delay in days) is influenced by a binary treatmentT(e.g.,T= 1if haversine distance>2000
km, indicating long-haul delivery) and a set of observed confoundersWincluding seasonality (month
of order), carrier quality (historical on-time delivery rate), order value (in BRL), product weight, and
payment method. The Average Treatment Effect (ATE), defined in Eq. (12), is formally given by:
τ=E[Y|do(T= 1)]−E[Y|do(T= 0)](12)
As defined in Eq. (12), thedo(·)operator represents a hypothetical intervention that sets the
treatmentTto a specific value, breaking all incoming edges toTin the causal graph. This quantity
captures the causal effect of the treatment on the outcome, free from confounding.
Identification relies on theBackdoor Criterion, which requires that the setWblocks all spurious
(non-causal) paths betweenTandY. Formally, this assumes conditional ignorability, as expressed in
Eq. (13):
(Y(1),Y(0))⊥T|W(13)
Eq. (13) states that, conditional on the observed confoundersW, treatment assignment is
independent of the potential outcomes. Under this assumption—often referred to as “no unmeasured
confounding”—conditioning onWremoves confounding bias, enabling causal effect estimation from
observational data.
Linear Regression Adjustment Estimator:To estimate the causal effectτ, we employ a Linear
Regression Adjustment estimator (implemented via DoWhy’sbackdoor.linear_regressionmethod).
This approach provides high interpretability and computational efficiency for offline batch processing,
making it well-suited for generating causal estimates across all 27 Brazilian states. The method fits a
linear structural equation to the data, as shown in Eq. (14):
Yi =α+τT i +β⊤Wi +ϵi (14)
Whereτcaptures the isolated causal effect of the treatment (e.g., the additional delay in days
strictly attributable to long-distance delivery, holding all confounders constant). The coefficient vector
βrepresents the effects of the confounding variablesW, controlling for seasonality, carrier quality, order
characteristics, and other factors that jointly influence both treatment assignment and outcome, whileϵi
denotes an error term assumed to be independent and identically distributed with mean zero.
This multi channel visual encoding bridges the gap between abstract regression coefficients and
spatial intuition such that domain analysts (not necessarily trained to interpret the implications of causal
inference) can at a glance discern a difference between structural penalties (as in geography determined
fixed distance penalties) and operational penalties (as in hub efficiency gains) without necessarily having
to interpret the results of complex regression tables in the immersive environment.
Causal Effect Visualization in VR:The computed causal coefficients{τg}for each regiongare
serialized into optimized JSON payloads (mean size: 3.2 KB per state) and streamed to the WebXR client
63

Mehta (2026) Int. J. Eng. Infor. Manag. Vol. 2, Issue 1: 52-82 (2026-Jan)
at runtime. These causal estimates are rendered as floating attribution bubbles anchored 1.2 units above
the corresponding regional bars in the 3D scene, creating a spatial association between the geographic
region and the causal mechanism affecting it. The visual encoding includes:
•Semantic Labeling:Text labels display human-interpretable causal language rather than raw
statistical outputs. For example, a bubble above Roraima (RR) reads “DISTANCE: +8.4d,”
indicating that geographic remoteness causally adds 8.4 days to delivery time after adjusting for
confounders such as seasonality and carrier quality. This semantic translation makes causal logic
accessible to operations managers and logistics planners who may not be familiar with regression
diagnostics.
•Color-Coded Driver Analysis:Positive treatment effects (factors that increase delay) are
rendered in Red, while negative effects (efficiency gains, such as “HUB: -1.3d” for Rio de Janeiro,
indicating that hub proximity causally reduces delay by 1.3 days) are rendered in Green. This color
scheme leverages universal conventions (red for warnings, green for positive signals) to facilitate
rapid visual pattern recognition.
•Font Size Modulation:The font size of each bubble is scaled proportionally to the magnitude of
the causal effect (fontSize= 12 + 2|τg|), such that large causal effects are more visually prominent,
guiding analytical attention toward the most impactful drivers of disparity.
•Transparency Encoding:Bubbles representing estimates that failed refutation tests are
rendered with reduced opacity (α= 0.4vs.α= 1.0for robust estimates), providing a visual
indicator of epistemic uncertainty and encouraging cautious interpretation.
This multi channel visual encoding fills the gap between abstract regression coefficients and spatial
intuition, so that domain analysts (who may not be trained as to how to interpret causal inference) can
immediately see a difference between structural penalties (such as geography determined fixed distance
penalties) and operational penalties (such as hub efficiency gains) without necessarily having to interpret
the results of complex regression tables within the immersive environment.
3.5 Phase 5: Customer Experience Quantification: Sentiment and
Retention Modeling
Multi-Modal Experience Indicators:Beyond operational indicators such as delivery delays and
cancelations, customer experience is additionally captured by sentiment and retention which are latent
variables deduced from review behavior and transaction patterns.
Sentiment Score Derivation:The system utilises precomputed regional sentiment scores
normalized to a continuous scale ¯ψg ∈[0,1]. This normalization transforms the raw 5-star ratings
into a probabilistic satisfaction index, where0.0represents total negativity and1.0represents perfect
satisfaction.
Context-Aware Sentiment Thresholds:To facilitate explainability and visualization, heuristic
thresholds are applied to classify regional sentiment into three discrete emotional states. Rather than
adaptive distribution-based methods, we employ fixed “Satisfaction Tiers” to ensure consistent cross-
region comparison. As formalized in Eq. (15), regional sentiment is discretized into three satisfaction
categories based on the average sentiment score:
Sentiment Category=



Happy if ¯ψg≥0.55,
Neutral if0.45< ¯ψg <0.55,
Unhappy if ¯ψg≤0.45.
(15)
As formalized in Eq. (15), this logic visually isolates regions exceeding the “High Satisfaction”
benchmark (e.g., Minas Gerais at0.56) from those in critical dissatisfaction zones (e.g., Alagoas at
0.37).
64

Mehta (2026) Int. J. Eng. Infor. Manag. Vol. 2, Issue 1: 52-82 (2026-Jan)
Figure 5:Sentiment Visualisation through Emojis
VR Sentiment Visualization:Sentiment categories derived from Eq. (15) are encoded using
billboarded text sprites rendered above region bars. By mapping the emoji glyphs toTHREE.Sprite
objects, the system ensures the text always rotates to face the user’s active camera, maintaining legibility
from any viewing angle within the immersive scene.
Retention Score Formulation:As defined in Eq. (16), customer retention probability is computed
as the proportion of repeat customers within each state. Customer retention probabilityρg is modeled
as the raw Repeat Customer Rate, defined as the proportion of unique customers in a state who have
placed more than one order:
ρg = Count(Customersg with orders≥2) Total Customersg (16)
As defined in Eq. (16), this metric serves as a direct proxy for loyalty, unmediated by complex regression
coefficients.
Figure 6:Retention Score Visualisation through Atomic Orbitals
Orbital Visualization Metaphor:Retention scores computed via Eq. (16) are visualized using
an “Atomic Orbital” analogy, where small geometries (octahedrons) orbit the region bars. To prevent
visual clutter, the system utilizes a tiered discrete encoding rather than a continuous scale. As defined
in Eq. (17), the number of orbitals and their material encodings are determined by discrete loyalty
thresholds:
(norb,Material) =



(3,Gold)ifρ g >0.06,
(2,Silver)ifρ g >0.045,
(1,Bronze)otherwise.
(17)
65

Mehta (2026) Int. J. Eng. Infor. Manag. Vol. 2, Issue 1: 52-82 (2026-Jan)
Orbital Trajectories:As defined in Eq. (18), orbital motion follows a circular parametric trajectory
around each region bar:
porb(t) =
[
xc +rcos(θ), ybar 2 , zc +rsin(θ) ] (18)
The angleθincrements per frame (θt+1 =θ t +ω). The angular velocityωis coupled to the retention
rate (ω= 0.02 + 0.5ρ g), ensuring that high-loyalty regions like Acre (ρ≈9.8%) exhibit faster, more
energetic orbital systems compared to transient markets.
3.6 Phase 6: Differential Geometry and Parametric Animation for
Flow Visualization
Quadratic Bézier Curve Formulation:Straight-line visualizations of customer–seller connections
produce visual clutter and fail to convey flow directionality in 3D space. We adopt quadratic Bézier
curvesB(t) : [0,1]→R 3, defined by three points: the sourceP 0, the destinationP 2, and a single
intermediate control pointP 1. As formalized in Eq. (19), the curve is expressed as a second-order
polynomial interpolation between these points:
B(t) = (1−t) 2P0 + 2(1−t)tP 1 +t 2P2 (19)
This formulation is computationally more efficient than cubic curves for WebXR rendering while
sufficiently capturing the “arching” metaphor of long-distance logistics.
Control Point Calculation:LetP 0 andP 2 be the start and end vectors in local scene coordinates.
The control pointP 1 is computed to create a vertical arc elevation proportional to the route length.
We first calculate the midpointM= P0+P2 2 and the Euclidean distanced=∥P 2−P 0∥. As defined in
Eq. (20), the control point is elevated along the vertical axis as a function of route length:
P1 =M+ (C+κ·d) ˆy(20)
C= 3.0is a base height offset andκ= 0.3is a distance scaling factor. This produces a natural
visual hierarchy: local deliveries appear as shallow arcs, while inter-regional shipments (e.g., São Paulo
to Amazonas) manifest as high-altitude parabolas, allowing users to distinguish flow types based on arc
apogee.
Haversine Distance for Metric Validation:While the visual geometry uses scene units, the
system strictly calculates the reported “Days Saved” metrics using the Haversine formula to ensure
geodesic accuracy. As given in Eq. (21), the great-circle distance between two geographic coordinates is
computed as:
dgeo = 2Rarcsin
(√
sin2
(∆ϕ
2
)
+ cos(ϕ1) cos(ϕ2) sin2
(∆λ
2
))
(21)
R= 6371km denotes the Earth’s radius. This ensures that the “Optimization Correction” feedback
(e.g., “−4.1Days”) is based on real-world kilometers rather than the arbitrary coordinate space of the
3D canvas.
Lagrangian Particle Animation:To visualize flow directionality without the computational cost
of sinusoidal opacity modulation, we utilize a Lagrangian particle system. A set of points is instantiated
along the curve geometry. As defined in Eq. (22), particle positions are advanced along the curve using
a modular linear update rule:
ut+1 = (ut +δ) mod 1(22)
whereδ≈0.005represents the flow speed.
Semantic Color Encoding:Rather than encoding individual delivery status, the particle systems
use color to visually reinforce the causal attribution of each route.
•Red flow(RGB= (1,0.2,0.2)): Used for “Bad” causal drivers, specifically visualizing the long-
distance penalty (τdist) connecting the Southeast to the Northern Frontier.
66

Mehta (2026) Int. J. Eng. Infor. Manag. Vol. 2, Issue 1: 52-82 (2026-Jan)
•Green flow(RGB= (0,1,0.5)): Used for “Good” causal drivers and optimization proposals,
representing high-efficiency routes (e.g., hub effects or proposed K-means centroids).
•Cyan flow(RGB= (0,1,1)): Used for the correlation layer, linking statistically similar regions.
This consistent color grammar ensures that motion (animation) and meaning (causality) are tightly
coupled in the user’s perception.
3.7 Phase 7: Immersive User Experience Architecture
WebXR Session Management:The system initializes virtual reality sessions through the
navigator.xrAPI, requesting animmersive-vrsession type (Group, 2023). The rendering loop is
synchronized with the display’s native refresh rate (generally 72Hz or 90Hz on Meta Quest 2) using the
renderer.xr.setAnimationLoopmethod, which abstracts the low level boilerplate associated with the
native WebXR Device API.
Stereoscopic Rendering Pipeline:Separate view matrices are automatically managed by the
Three.jsWebXRManager. By configuringrenderer.xr.enabled = true, the engine effectively handles
the dual-camera offset and projection matrix updates required for binocular depth perception obviating
the requirement of manual matrix math (Jerald, 2015).
Spatial Metaphor and Scale Decisions:In accordance with the existing immersive analytics
design principles, we adopt a "Giant’s Perspective" where users experience the visualisation as elevated
observers (Willett et al., 2021). The camera is positioned at(0,8,12), yielding a 45-degree downward
view of the map. Vertical bar heights are computed as defined in Eq. (23):
h= max
(
0.2,delaynorm×1.5
)
(23)
This scaling results in a height range of[1.0,4.0]units. This ensures that even small delays remain
visible while preventing the largest bars from occluding the user’s view of the entire dataset (Ware, 2012).
Hybrid Raycasting for Diegetic Interaction:To support both desktop debugging and VR
deployment, the system implements a dual-input strategy (Bowman et al., 2004):
•Desktop:A standard pointer ray is cast from the camera center based on mouse coordinates
usingTHREE.Raycaster.
•VR controller:A ray is cast from the controller’s grip position forward (via
controller.getDirection()).
Intersection tests are performed every frame against the bounding boxes of the bar geometries. To
optimize performance, a shared material state is used: when a bar is intersected, itsemissiveIntensity
is boosted from0.2to1.0, providing immediate visual feedback (“highlight on hover”) without the
overhead of swapping materials (Valentini, 2012).
3D Info Panel Construction:Upon selection, the system avoids relying on HTML DOM overlays
(which are invisible in VR contexts); instead, it instantiates a world-space information group. A512×256
HTML5 canvas is created in memory, and the region’s metadata (Name, Delay, Retention, Sentiment) is
drawn to this canvas using standard 2D context API commands. This canvas is subsequently used as a
texture for aTHREE.Sprite; unlike aPlaneGeometry, which would require explicit manuallookAtlogic,
a sprite automatically billboards to face the active camera, thereby ensuring text legibility irrespective
of the user’s position or head rotation.
Lazy Instantiation:To minimize garbage collection overhead and improve runtime performance,
a singlevrInfoGroupis instantiated at initialization stage and reused throughout the session.
During interaction events, this group is merely toggled (visible = true/false) and repositioned
(position.copy(target)), rather than being destroyed and recreated on a per-frame basis.
67

Mehta (2026) Int. J. Eng. Infor. Manag. Vol. 2, Issue 1: 52-82 (2026-Jan)
3.8 Phase 8: Prescriptive Analytics: Interactive Site Selection via
Localized K-Means
Problem Formulation:Rather than a static global optimization, the system addresses the single
facility location problem in real time: given a user-selected target pointptarget (representing a proposed
site), it identifies the local neighborhood of demand nodesN={c 1,...,c k}and computes the optimal
centroidw∗ that minimizes the weighted Euclidean distance, as defined in Eq. (24):
w∗ =
∑k
i=1vici ∑k
i=1vi
(24)
vi denotes the order volume of regioni. This formulation corresponds to a weighted centroid, allowing
analysts to test hypotheses such as “What if we build a hub here?” dynamically.
Client-Side Heuristic Algorithm:A lightweight, real-time clustering heuristic is implemented
directly within the JavaScript render loop to ensure instant feedback without server round-trips:
•Neighborhood selection:Upon user click (raycast intersection with the map floor), the system
calculates Euclidean distances fromptarget to allnstate centroids.
•Cluster formation:Thek= 5nearest states are selected to form a demand cluster.
•Centroid computation:The recommended facility location is computed as the weighted center
of mass of this cluster using Eq. (24).
Figure 7:"Ghost Warehouse" Facility
Visualizing the Counterfactual:The recommended facility is rendered as a “Ghost Warehouse”
(translucent green box,THREE.BoxGeometry,α= 0.8) positioned at the computed centroid. Green
QuadraticBezierCurve3arcs connect the new facility to the cluster nodes, visually overriding the
existing long-haul connections, while green flow particles traverse these new routes to provide immediate
feedback on the efficiency of the proposed network.
Quantitative Feedback:A floating billboard label is instantiated above the ghost warehouse,
displaying the aggregate impact metric, as defined in Eq. (25):
∆savings = 1 |N| ∑ i∈N ( dcurrent(i)−d new(i) ) (25)
This value represents the mean reduction in delivery distance (or time proxy) across the affected
neighborhood. This text is rendered as a sprite (e.g., “Optimization Correction|−4.1Days”), enabling
68

Mehta (2026) Int. J. Eng. Infor. Manag. Vol. 2, Issue 1: 52-82 (2026-Jan)
immediate quantitative assessment of the intervention’s value relative to the status quo (São Paulo hub
dependence).
Interaction Design:
This module performs with 60+ FPS (as compared to batch optimization processes, where there is
a need to wait to get the results) and operates in parallel. Users may move their cursor all over the
map, and the ghost warehouse and the savings metric that it represents given by the requirements of the
savings metric of Eq. (25). The savings metric can be continuously updated with the movement of the
cursor over the map, which facilitates a quick sensitivity analysis wherein the user can intuitively feel
where the optimal location is by watching the savings metric change as they move the cursor over the
map.
3.9 Phase 9: Proposed Immersive Governance Layer
Though detection is easier through visualization, accountability would be needed in the operational
systems in a bid to make things fair. We suggest an Immersive Governance Layer; a computer component
that is part of the WebXR pipeline that converts the 3D space to an active viewing space that we
can scan to a workspace.(Jerald, 2015). This layer, implemented as a discrete scene graph manager
(GovernanceLayer), provides three critical mechanisms for responsible AI deployment (Wieringa, 2020).
Spatiotemporal Audit Trails:The system uses a persistent 3D audit log in order to overcome the
black box” nature of decision-making. Each critical user interaction, filtering event, policy parameter
change, or hub optimization simulation, is represented as a physical object in the virtual world. The
various types of interactions are coded as different geometries (e.g. cubes in case of an optimization
event, cones in case of a policy shift) and are positioned at the precise spot of the world at which the
choice was made.
A dashedCatmullRomCurve3connects these artifacts chronologically, creating a visible “decision
thread” that allows auditors to physically trace the sequence of actions leading to a specific operational
outcome. Each artifact stores metadata (User ID, Timestamp, Action Values) within itsuserData
property, which can be retrieved via raycasting for retrospective analysis.
Probabilistic Confidence Shells:Standard dashboards often present point estimates as absolute
definitive truths, masking the statistical uncertainty especially inherent in small-sample subpopulations.
The Governance Layer enforces epistemic transparency through confidence shells. Instead of relying on
standard error bars, uncertainty is rendered via three concentricSphereGeometryshells corresponding
to probability density (1σ,2σ,3σ).
The opacity of these shells is inversely mapped to statistical confidence; highly uncertain estimates
(e.g., those derived from sparse rural data) render as opaque red spheres (opacity: 0.9), intentionally
obstructing the analyst’s view and visually forcing the recognition of the data’s limitations prior to
decision making process.
Counterfactual Scenario Comparison:To facilitate evidence-based decision making, the system
supports in-situ A/B scenario comparison (Pearl & Mackenzie, 2018). When a new logistics strategy
is proposed (e.g., Proposed Val), it is rendered concurrently against the baseline val using a dual-glyph
metaphor. The status quo is shown as a wireframe “ghost” box (α= 0.3), whereas the proposed outcome
is illustrated as a solid object (α= 0.8).
A vertical connector line links the two states, supplemented by a floating billboard label explicitly
calculating the delta (e.g., “ 15.2%”). The delta is color-coded (green for improvement, red for regression),
allowing stakeholders to rapidly assess whether a proposed intervention reduces or amplifies the existing
disparities (Barocas et al., 2019).
3.10 Phase 10: Planned User Study & Evaluation
The validation layer of the whole framework is User study and Evaluation. Its main goal is to measure
the performance of the immersive analytics system against the classical two-dimensional (2D) basis
and to detect the possibilities of the iterative improvement of the user experience outlined in Phase 7.
69

Mehta (2026) Int. J. Eng. Infor. Manag. Vol. 2, Issue 1: 52-82 (2026-Jan)
The assessment is based on a mixed-methods methodology which involves a combination of quantitative
measuresofperformanceandqualitativefeedbackofuserstogiveaholisticviewoftheusability, efficiency,
and cognitive impact.
The research design is a within-subject design, whereby the individuals undertake a predetermined set
of decision-making problems, including the optimal location of a new plant with given set constraints, in
two conditions. Condition A (Baseline), the subjects employ traditional 2D visualization resources such
as charts, flat maps and dashboards. Condition B (Immersive) involves the use of the WebXR/VR/AR
environment proposed by the authors. This design allows the direct comparison of performance and
experience of both analytical paradigms and adjusting the individual difference under control.
Three fundamental quantitative measures are used to measure objectively the performance and
usability. Time to Completion (TTC) and Error Rate are used to measure task performance, and
the combination of these two measures can be used to determine whether immersive dimensionality
helps participants to reason spatially more quickly and with fewer errors. A standardized ten-item
questionnaire, called System Usability Scale (SUS), is used to generate the perceived system usability
(Brooke, 1996). Any score that falls above 68 is regarded as above average whilst a score above 80 means
that the user experience is excellent. Moreover, NASA Task Load Index (NASA-TLX) is also applied to
measure perceived workload on six dimensions including Mental Demand, Physical Demand, Temporal
Demand, Performance, Effort and Frustration(Hart & Staveland, 1988).
In addition to a quantitative assessment, qualitative feedback is gathered with the help of semi-
structured interviews and think-aloud protocols (Ericsson & Simon, 1993). These techniques represent
user perceptions of the flow animations that were proposed in Phase 6 and their ability to be interpreted
and interpreted as causal knowledge that had been developed in Phase 4. This feedback can further
explain the cognitive participation of the users in the immersive environment and where there can be an
interactional or conceptual barrier.
The last step is that the process of evaluation creates a continuous feedback loop with Phase 7,
Integration Platform. The intuition based on both quantitative and qualitative findings is used to make
improvements in the design. To give an example, when the NASA-TLX scores are high and it is found
that the Physical Demand is high, the interaction mechanisms like hand gestures, controller inputs, or
navigation techniques can be redesigned to decrease fatigue and an increase in user comfort. By doing
so, not only is the system performance validated but Phase 10 is also a contributor to the gradual
enhancement of the immersive analytics structure.
4 Results And Discussion
This section demonstrates the initial findings and insights obtained in accordance with the pipeline of
immersive analytics used on the Olist dataset outlining the most significant contributions and their
implications. Table 1 provides the full-regional data, which is a compilation of the key logistical,
sentiment, and retention data that formed the basis of the ground truth in training and testing the
whole fairness-conscious pipeline.
4.1 Spatial Heterogeneity and Fairness Metrics
The geographic heterogeneity and variance of service quality across the Brazilian states was drawn out
well using the immersive visualization; this would otherwise be buried in aggregate statistics or 2D
choropleth maps which were plotted correctly in fig 8 and fig 9 and fig 10.
(a) Regional Disparity Patterns:The 3D bar height encoding clearly illustrated a distinctive “South-
North divide” in delivery performance. Southeast and South states (specifically São Paulo, Paraná)
exhibited normalized bar heights that corresponded to average delivery times of 8–12 days (e.g., SP:
¯t= 8.3days), while in contrast Northern frontier states (Roraima, Amapá, Amazonas) depicted bars
3.5 times taller, representing mean delivery times ranging from 26 to 29 days. This noticeable spatial
gradient reflects the well-known disparities in Brazil’s logistics infrastructure network. Additionally, the
70

Mehta (2026) Int. J. Eng. Infor. Manag. Vol. 2, Issue 1: 52-82 (2026-Jan)
(a)2D Representation
 (b)3D Encodings
Figure 8:Customer Review Sentiment vs Geography
(a)2D View (Cancel Density)
 (b)3D View (Color: Rate)
Figure 9:Cancellation rate vs Geography
(a)2D View
 (b)3D Correlation Edges
Figure 10:Inter-Regional Similarity Analysis71

Mehta (2026) Int. J. Eng. Infor. Manag. Vol. 2, Issue 1: 52-82 (2026-Jan)
T able 1:Regional Performance Metrics: Logistics, Sentiment, and Retention.
Region Total Orders Avg Delay (Days) Late Orders (%) Cancel Rate (%) Sentiment Retention (%)
AC 81 20.6 3.7 0.0 0.52 9.9
AL 417 24.0 23.0 0.2 0.38 6.1
AM 149 25.9 4.0 0.0 0.59 5.4
AP 68 26.7 4.4 0.0 0.60 2.9
BA 3,397 18.9 13.6 0.5 0.43 5.9
CE 1,339 20.8 14.7 0.5 0.43 3.5
DF 2,160 12.5 6.9 0.3 0.53 6.1
ES 2,043 15.3 12.0 0.5 0.52 6.2
GO 2,037 15.1 8.0 0.6 0.52 6.6
MA 751 21.1 18.8 0.5 0.38 5.2
MG 11,706 11.5 5.5 0.5 0.57 6.2
MS 726 15.2 11.3 0.3 0.56 5.6
MT 910 17.6 6.6 0.2 0.55 6.8
PA 981 23.3 11.9 0.4 0.42 5.1
PB 537 19.9 10.6 0.4 0.51 6.0
PE 1,663 17.9 10.3 0.3 0.51 5.0
PI 496 19.0 15.3 0.8 0.46 4.8
PR 5,064 11.5 4.9 0.4 0.59 6.2
RJ 12,930 14.9 12.9 0.7 0.44 7.0
RN 487 18.8 10.5 0.0 0.55 4.5
RO 253 18.9 2.8 1.2 0.53 9.5
RR 46 29.0 10.9 2.2 0.30 4.3
RS 5,506 14.8 7.0 0.5 0.57 6.5
SC 3,651 14.5 9.5 0.5 0.54 5.6
SE 350 21.0 14.6 0.3 0.40 5.4
SP 41,964 8.3 5.7 0.8 0.59 6.6
TO 280 17.2 12.5 0.4 0.55 5.0
immersiverepresentationenabledanimmediatevisualperceptualcomprehensionofmagnitudedifferences
that tabular representations would typically require laborious numerical analysis to interpret.
(b) Reliability vs. Speed Trade-offs:
Alongside the absolute delay measures, the red rings of the color of the opacities represented the
defining feature of equitable nature as far as predictability is concerned. Other states like Minas Gerais
(MG) registered moderate delays (¯t= 11.5days), with exceedingly slim confidence (CI width = 0.26
days), displayed as faint and almost invisible rings, which signifies constant service and reliability. On
the other hand, Roraima (RR) showed both very extreme mean delay (¯t= 29.0days) and very large
confidence intervals (CI width = 17.5 days), that were rendered in solid, opaque red rings. This visual
contrast of the translucency and the opaqueness distinguishes between structural delays (which carry
the same distance penalty) and operational volatility and instability (which creates some uncertainty),
a point that has to be made with careful consideration to the customer expectations in volatile areas
where some unpredictability is tolerated and yet there is no ambiguity.
(c) Non-Geographic Similarity Networks:The similarity edges in the feature-space (activated when
s(gi,gj)<0.2) revealed heinous functional similarities and correlations between geographically dispersed
regions. As an example, the coastal state of Espirito Santo (ES) has been graphically connected through
the cyan curves to the inland state of Mato Grosso do Sul (MS), even though a distance between the
two areas is more than 1,500 km. Experimental analysis of features has verified that both areas have
statistically identical logistical characteristics, including similar delivery times (≈15.3days vs.15.2days)
and almost equal levels of late deliveries (12.0%vs.11.3%). These trends represent common bottlenecks
of operation, basically to do with the processing efficiency of the Last Mile, which would otherwise be
invisible and unknown in conventional geographical proximity studies. In this way, similarity graph serves
as a diagnostic overlay, which makes it possible to find policy clusters that can be effectively worked with
by the optimisation strategy in many non-contiguous problem areas.
72

Mehta (2026) Int. J. Eng. Infor. Manag. Vol. 2, Issue 1: 52-82 (2026-Jan)
4.2 Causal Attribution: Distinguishing Correlation from Structural
Drivers
One of the main contributions of this system is the ability to draw a visual difference between observed
disparities. distracting mechanisms established by causal inference, thus, resolving a core. drawback of
Descriptive conventional analytics. The Double Machine Learning to causal estimation, represented as
floating annotation objects on top of regional bars, where there was quantitative attribution of elements
that caused delays in delivery. Table 2 disaggregates the causal analysis of delivery delays to quantify
how individual factors regarding the region and operations (e.g., the volume of orders or the proximity
of hub) had a positive or negative effect on the overall delivery time. The soundness of these causal
assertions is also supported by the soundness. checks in Table 3, in which a placebo treatment refuter
provided a result a near-zero effect ( -0.004 days) with a p-value of 0.86, which validates the fact that
the identified drivers. are not random and meaningless.
T able 2:Causal Inference Findings: Impact of Regional Factors on Delivery Delay.
Source Region Causal Factor Impact (Days) Type Interpretation
São Paulo (SP) Weekend Order+0.1Info Negligible delay
São Paulo (SP) High Order Volume+4.0Info Significant congestion
Rio de Janeiro (RJ) Hub Proximity−1.3GoodReduces delay
Rio de Janeiro (RJ) Weekend Order+0.2Info Slight delay
Minas Gerais (MG) Long Distance+2.5BadIncreases delay
T able 3: Causal Robustness Check.Comparison of the estimated causal effect against a placebo test where the treatment
variable was randomized. The near-zero placebo effect supports the validity of the original estimate.
Test Type Original Estimate New Effect (Placebo) p-value Result
Placebo Treatment Refuter 5.94 days -0.004 days 0.86Pass
Diagram 11 illustrates the assumed causal structure for the Minas Gerais analysis. Arrows represent
directional influence:SeasonalityandCarrier Qualityare modeled as confounders that influence both
the treatment (Long Distance) and the outcome (Delivery Delay).
(a) Congestion vs. Efficiency:In the case of the commercial centre in Sao Paulo (SP)-Brazil, the
causal decomposition has shown a strong Volume Congestion effect:τvolume = +4.0days. This positive
coefficientiscontrarytothesimplistic, naiveassumptionsabouttheeconomiesofscale, rather, itindicates
that very high order density in the metropolitan area is making the processing bottlenecks too large to
compensate by the existing infrastructure benefits. On the contrary, this pattern was not true in the
nearby state of Rio de Janeiro (RJ):τhub =−1.3days. This visual difference highlights the fact that the
bulk of volume is being managed by SP at present with RJ having greater throughput efficiency when
compared to its operational load which indicates that logistic investments should be made to decongest
the SP sorting facilities instead of increasing the RJ capacity.
(b) Case Study of Minas Gerais vs. Coastal Hubs:Comparative visualisation of Minas Gerais
state (MG) inland state and coastal hubs showed causal profiles which were different. This MG causal
annotation depicted a Distance penalty:τdistance = +2.5days, as it highlights the importance of last-mile
geography, which is mountainous and has high populations scattered across rural locations, as the major
cause of latency. Unlike SP where the amount of business is what causes delays (process), delays in
MG are caused by topology (structure). Such visual difference justifies the required policy changes: MG
should obtain the last-mile solutions (local micro-fulfilment and drone delivery pilots), and SP should
receive the high-volume process automation.
73

Mehta (2026) Int. J. Eng. Infor. Manag. Vol. 2, Issue 1: 52-82 (2026-Jan)
Figure 11: Causal Directed Acyclic Graph (DAG)
(c) Validation via Hybrid Arc Encoding:The corroborative evidence of the causal estimates is the
colour-coded delivery route arcs. Particles of long distance flow between the central hubs and the cluster
of Far States (Amazonas, Roraima, Amapa) were displayed as red, which graphically strengthens the
causal hypothesis that distance is the only dominant failure mode of Northern Brazil, in contrast to the
congestion of operations as in the southeast.
4.3 Customer Experience Dimensions: Sentiment and Retention
Theincorporationofemotionbasedonreviewsandtransaction-basedretentionmeasuresofferedahuman-
oriented view and solution to fairness to show that the operational logistics imbalances have no linear
relationship with customer dissatisfaction.
(a) The Sentiment-Delay Dissociation:However, unlike the expected linear negative correlation
between delay of getting the delivery and sentiment, the analysis of the regions showed that there is
more complicated and sophisticated nonlinear association. This in effect implies that, the northern
states, like Amazonas (AM) and Amapa (AP), whose delay was more than the mean (25 days) had
in fact maintained high sentiment levels of 0.59, which are as good as those of the more efficient state
of Parana. This paradox may be explained by the effects of adaptation when the customers in the
underserved areas evolve their expectations and base them on the local standards, not the national ones.
Nevertheless, this tolerance is limited: Roraima (RR) with the maximum delay of 28.9 days, fell to the
minimum sentiment rating in the data (0.30), which can be seen as a point of customer tolerance.
(b) Identifying Actionable Pain Points:The emoji representation has been effective in identifying
particular areas of issues independent of the high-delay areas. The negative sentiment (0.40) was found in
Sergipe (SE) in spite of the lower delays than the northern frontier. An even deeper examination showed
the cause behind that: SE has an excessively high Late Orderrate (14.5%), which is nearly three times as
large as that of efficiency states, such as SP (5.7%). This implies that the penalty imposed by customers
on unreliability (missed deadlines) is higher than consistent delays, and interventions and policies are
shaped to increase the predictability of the operations instead of simply emphasising the speed.
(c) Retention as a Fairness Outcome:The intuitive encoding of customer loyalty was the orbital
74

Mehta (2026) Int. J. Eng. Infor. Manag. Vol. 2, Issue 1: 52-82 (2026-Jan)
visualisation metaphor. Surprisingly, the Gold-orbital states were not the major commercial centers,
but, to some extent, the peripheral areas, such as Acre (AC) and Rondonia (RO), that had the most
significant retention rates of the data (9.8% percent and 9.4% percent, respectively). However, Sao Paulo
(SP) had a comparatively low retention rate of 6.6% even when it has better service. The same graphic
dislocation of the visual image implies, in turn, an implication of Captive Market fairness in that in less
densely populated areas high retention must be as a result of a dearth of retail options and not customer
satisfaction, which practically seals customers into a high-latency logistic system.
4.4 Prescriptive Analytics: Warehouse Optimization and Impact
Simulation
The real-time counterfactual reasoning in immersive environments was feasible due to the developed
integrated K-means recommendation engine.
(a) Interactive Site Selection:The system uses Human-in-the-Loop instead of a stationary global
solution. One can simply click anywhere on the map and an on-demand clustering event will be triggered.
Thealgorithmdynamicallydeterminesthefivenearestdemandnodestothecursorlocationandcomputed
a weighted centroid (Centre of Gravity). When we asked the system to provide a sample interaction to
the Northeast, a hub location near Bahia (BA) was immediately proposed by the system as an alternative
to the long-haul dependency on Sao Paulo to a localised distribution strategy.
(b) Visual Impact Assessment:The Ghost Warehouse rendering-a green box with emanating green
optimisation arcs facilitated instant qualitative evaluation of topology modification in the network. The
visualisation itself, by superimposing these direct, short, green flows on the already existing, long-range
flows, shows intuitively the short-circuing of logistical inefficiency. The resulting floating label is instant
feedback, which calculates a distance-related savings measure-e.g., Optimisation Correction -4.1 Days-
based on the difference between the new centroid and the current SP hub.
(c) Quantitative Validation:According to the simulation, latency will be greatly reduced to the
distant clusters. In the case of the Amazonian cluster, AM, RR, AC and RO, a local hub decreased the
effective weighted distance by over 2,000 km, which translates to a delay decrease of 2.5-3 days of delay
but is purely theoretical. The reduction of variability promising not only faster but more predictable
service implies the fairness of the dimensions of speed and reliability, simultaneously without involving
a complicated tabular interpretation.
4.5 System Performance and User Experience
(a) Computational Efficiency:The architectural choice of using procedural geometry generation in
the client-side JavaScript engine provided with the stability of performance without the obligation to
download heavy assets. The generation of map texture (2048x2048) and 3D meshes (Bars, Rings) during
run-time with HTML5 Canvas API and Three.js primitives maintained the overall size of the payload of
the application at the low level (less than 50 KB). Analysis of frame time values on target hardware based
on WebXR showed a consistent performance that is comfortably under the 11.1ms frame rate needed to
run at 90Hz and act as an anti-motion sickness measure. Particles and simple geometry primitives were
instanced to ensure that the call count was kept down, and scaling was proven.
(b) Interaction Latency:The interaction latency of the Direct Manipulation” metaphor was tolerable
with a selection based on raycasting. Latency is attributed to the dynamic development of Canvas
Textures to the floating information labels (on-demand development, text layout, and upload of the data
to the graphics card on each click). This was good enough to do prototyping, but already gives a clue of
how this can be optimised in subsequent versions: with Texture Atlasing, the glyphs would be generated
in advance, rather than creating a specific texture to use each interaction event.
(c) Perceptual Discriminability:The strategy of visual encoding mentioned above was confirmed
75

Mehta (2026) Int. J. Eng. Infor. Manag. Vol. 2, Issue 1: 52-82 (2026-Jan)
in our post-hoc analysis. Rather than mapping Confidence Intervals to spatial size, this was achieved
with the help of opacity (red rings), this would not create visual clutter and the user would easily notice
the difference between High Risk, which is represented by solid red, and Safe, which is represented by
transparent, without obscuring the primary metric of Delay (bar height). Also, there was the application
of alternative motion channels, -Orbiting for Retention and Pulsing for Uncertainty- that entered the
preattentive processing, and had the ability to view several variable states concurrently without mental
clogging.
4.6 Theoretical Contributions
WebXR delivery analytics pipeline is a paradigm shift in the logistics management of converting the 2D
data to the immersion Digital Twin with fairness and comprehensiveness. The combination of Python-
based causal inference (DoWhy) and optimization algorithms (K-Means) with a spatial interface in
Three.js enables the framework to develop the theoretical knowledge of how immersive settings can be
used to support fairness-aware reasoning. It demonstrates that multidimensional spatial representations
may allow analysts to get past correlation to the causal interpretation, where it is possible to explicitly
distinguish between the operational inefficiency and the geographic or structural constraint by intuitive,
visually based process of causal bubbles. This makes immersive analytics not only an aestheticization
of visualization, but a new epistemic framework of causal reasoning on matters of fairness in complex
socio-technical systems.
(a) Perceptual Integration Theory for Fairness Analytics:The work demonstrates
that stereoscopic 3D environments allow simultaneous representation of a variety of data dimensions
(geography, magnitude, volume, uncertainty, and causalattribution)in anintegralvisual object, lessening
cognitive load than switching attention between 2D displays. This also expands perceptual integration
theory to the realm of equity analytics, demonstrating that pre-attentive pattern recognition of complex
intersectional disparities (e.g., Resilient Clusters”) can be undertaken where the relevant attributes are
spatially co-located as opposed to being spread out across different visualizations.(Willett et al., 2021).
(b) Causal Transparency Framework:The system gives a theoretical platform on how to
separate the correlation and causality in fairness of evaluation through the visualisation of causal effects
of treatment using Structural Causal Models (Pearl, 2009). This realises in an operationalised form
the principles of algorithmic transparency by inspecting and contesting causal attribution mechanisms
(structural inequities versus compositional artifacts) by visual encodings that have spatial reference,
beyond the mere reporting of disparities at a descriptive level (Doshi-Velez et al., 2017).
(c) Perceptually-Grounded High-Dimensional Encoding:The work defines methodological
concepts of the development of multi-attribute immersive visualization that fulfills human perceptual
constraints. It shows that scalable visual designs can be guided by systematic application of
psychophysical models (Stevens, 1957; Ware, 2012) through coding budgets which do not incorporate
information overload whilst providing discriminability across 6 simultaneous dimensions using optimized
color palettes (ColorBrewer RdYlBu with gamma correction by default set to 2.2) and spatial depth clues
and particle movements.
(d) Prescriptive Equity Analytics:The incorporation of the ability to use counterfactual
reasoning into immersive environments fills the theoretical disjunction between efficiency optimization
and equity evaluation. The framework allows one to not just assess the aggregate performance
benefits, but also their distributional impact on subpopulation groups of demographic and geographic
characteristics, and contributes to the discussion of fairness by the relevant stakeholders on whether
algorithmic solutions are in line with the organizational values of fairness or not (Barocas et al., 2019).
(e) Architectural Generalizability and Scalability:The topography of the pipeline (
Foundation→Analytical Engine→Dynamics→Integration→Governance) offers an architecture
domain-independent intersectional fairness analysis of socio-technical systems. Phase 1, geospatial
transformation, accepts any WGS84 coordinates, which allow direct usage outside the Brazilian e-
commerce to urban transportation equity, healthcare service distribution, and financial access disparities.
The templated fairness metric framework (group metric - population baseline, Eq. 4-6) can be applied
to any performance indicator, and computation complexity (O(n)) and analytics based on aggregation
76

Mehta (2026) Int. J. Eng. Infor. Manag. Vol. 2, Issue 1: 52-82 (2026-Jan)
provide scalability to regional pilots (27 Brazilian states, 100,000 orders) to the national ones. This
is in response to the request for fairness frameworks by the context of the global South Sambasivan
et al. (2021) that are incomplete, unevenly distributed in infrastructure terms, and with complicated
socioeconomic processes.
(f) Browser-Native Deployment as Theoretical Innovation:The concept of WebXR
implementation does not follow common beliefs that immersive analytics needs a special hardware and
installation. The work provides a new theoretical framework of democratized immersive analytics that
transcends enterprise adoption barriers that have been reported by Franke & Haehn (2020) by showing
that zero-installation, cross-device compatibility (desktop, mobile, VR headsets), using standardized
web API, can be used to deliver 60+ FPS performance; the work outperforms other engines such as
Unity or Unreal engines. The inverted confidence ring (Eq. 9) design, in which uncertainty is now
graphicallyexaggerated(widerintervals)insteadoftoneddown, isacontentionofparadigmsofvisualizing
uncertainty by making analytical effort focus on those data regimes that need careful interpretation.
4.6.1 Comparative 2D vs. 3D Visualization Analysis
As a measure of the effectiveness of the proposed immersive visualizations, we contrasted the proposed
visualizations with basic 2D analogs in three major dimensions of analysis sentiment analysis, cancellation
metrics, and inter-regional similarity. In conventional 2D representations, the representation itself can
also be misleading due to overlapping clusters of data (Fig. 8a), while using the 3D encoding (Fig. 8b)
results in the use of spatially attached bars with emotive icons on top of them, allowing users to identify
the positive and negative sentiment immediately without losing geographical context.
This accuracy is applied in risk monitoring as demonstrated in Figure 9. The 2D density heatmap
(Fig. 9a) gives only a generalized impression of the cancellation hotspots but the 3D projection (Fig. 9b)
directly looks at the rate of cancellation against bar color i.e. the transition of the color to red and
therefore the high-risk areas become easily identified which could be obscured by a gradient in the 2D
projection.
Finally, Figure 10 addresses the issue of visual occlusion in network analysis. Where the standard
2D view (Fig. 10a) suffers from visual clutter due to intersecting connectivity lines, the 3D construction
(Fig. 10b) lifts these correlation edges into vertical arcs. This method preserves the visibility of the
underlying map while clearly delineating complex relationships between regional nodes, such as the
non-obvious similarity between Espírito Santo (ES) and Mato Grosso do Sul (MS) despite 1,500+ km
separation and no geographic border.
Lastly, Figure 10 deals with the problem of visual congestion in network analysis. In systems where
the conventional 2D representation (Fig. 10a) is afflicted by visual crowding on the basis of overlapping
connectivity lines, the 3D representation (Fig. 10b) elevates such correlation edges of (Fig. 10a) to vertical
arcs.
4.7 Practical and Managerial Implications
Practically, the WebXR delivery analytics pipeline illustrates how immersive and equity-conscious digital
twins can make state-of-the-art analytical reasoning more democratic. The system allows decision-makers
to discover structural disadvantages to remote or underserved areas by encoding delay, volume, sentiment,
and retention into unified 3D objects and interactive What-If” scenario simulation (Phase 8). This has a
direct reduction of bias since it focuses attention not on the raw speed of performance, but on intrinsic
reliability and long term value and it is here that infrastructure investments can be considered in terms
of their efficiency, but also in their distributional fairness.
(a) Operational Strategy and Decision Making:Although the driving application is logistics
fairness, the pipeline architecture is general to other fairness-critical areas where spatial inequality
overlays with service provision such as resource allocation in healthcare (wait time by census tract),
financial inclusion (bank branch access by neighbourhood) (Li & Li, 2023), education opportunity
(school quality measures by district) (Reardon, 2011) and and environmental justice (pollution exposure
by zip code (Morello-Frosch et al., 2002). The geospatial transformation (Phase 1) takes any WGS84
coordinates, so that it can be used outside of Brazilian e-commerce, whereas the templated fairness metric
77

Mehta (2026) Int. J. Eng. Infor. Manag. Vol. 2, Issue 1: 52-82 (2026-Jan)
structure (group metric−population baseline, Eq. 4–6) is adjusted to any performance indicator. The
O(n) computation and analytics based on aggregation guarantee the ability to scale between regional
pilots (27 Brazilian states, 100,000+ orders) and national deployments. In analogy to analysts with
data fatigue, the switch to 3D enriches the processing of intersecting disparities that may be missed on
a two-dimensional display, and it allows more accurate and quicker identification of these disparities,
particularly by computer-aided analysts in a stereoscopic 3D environment. The feature-space similarity
analysis (Phase 3, Eq. 1011) finds non-contiguous areas sharing common operation bottlenecks, like
Espirito Santo and Mato Grosso do Sul that are 1,500+km apart and yet have exactly the same delay
profile, and allows efficiency gains by applying common interventions instead of region-specific ones.
(b) Economic Viability and Technical Infrastructure:The WebXR architecture is a browser
native platform that eliminates the costs on the traditional VR deployment presentations with high
economies of scale. High-fidelity immersive analytics can be deployed by IT and engineering teams
even without costly, tethered workstations (Jerald, 2015) to work (Meta Quest 2, desktop browsers,
mobile devices) and are open source in stack (Three.js, A-Frame) reducing capital spending by several
folds compared to enterprise VR with Unity/Unreal. The system, by decoupling inference (server-side
Python/DoWhy) and rendering (client-side WebGL), allows interactive frame rates of 60+ FPS, and
still helps keep the data integrated in real-time by using HTTP/WebSocket protocols. It is also shown
that current statistical settings (Python, Pandas, scikit-learn) can be easily integrated with WebXR
through the use of data streaming over JSON(McKinney, 2012), enabling teams to maintain existing
analytical pipelines but only modify the visualization front-end. The investment payoff is based on:
(1) better customer retention due to less regional disparity (equity-conscious delivery eliminates churn
in underserved areas), (2) regulatory compliance (preemptive bias audit can help to avoid penalties on
discrimination), and (3) reputational capital (transparent fairness governance helps to build brand trust
in socially conscious markets). The system speeds up the discovering insight by uncovering intersectional
disparities as spatial navigation opposed to combinatorial SQL queries, which saves the expenses of
analyst labor.
(c) Democratization and Communication:Non-technical stakeholders can directly query the
outcomes of analytical tests by manipulatively representing abstract statistical constructs, including
confidenceintervalsandcounterfactualoutcomes, asspatialobjects. Thiseliminatestheneedtohavedata
scientists to act as intermediaries, and operational managers are given the power to make the distinction
between operational failures that can be handled by corrective actions and structural constraints which
are inherent in the nature of the business model. This interpretability through immersion helps to sustain
new requirements of explicable and transparent AI systems (Lipton, 2018). The Immersive Governance
Layer (Phase 9) offers a record of auditable decision-making by generating spatiotemporal interaction
logs and counterfactual scenario comps, and allows policy makers to evaluate proposed interventions (e.g.,
mandating minimum service provision in rural areas) by color-coded visualization (green to improvement,
red to regression) with stakeholders having an easy time communicating with.
(d) Governance, Compliance, and Ethics:In the case of controlled industries, the combined
provenance recording system offers a tangible avenue of compliance and algorithmic responsibility. The
system creates an audit trail by documenting the explored disparities and reviewed counterfactuals, which
can prove that an organization had an organizational duty of care in overseeing algorithmic bias denoting
an accountable action to address the problem of bias in algorithmic decision-making (Doshi-Velez et al.,
2017). It also goes a step further to make fairness metrics and their uncertainty more perceptually salient
than buried in technical documentation, making them more responsible AI practice (Kay et al., 2016;
Correll & Gleicher, 2014). The visualization based on the inverted confidence ring (Eq. 9), in which
broader uncertainty intervals imply increased transparency, makes it impossible to ignore the fact that
algorithms are subject to statistical constraints in their policy-making, which has been a long-standing
issue of accountability in algorithmic systems.
5 Conclusion
The studies reveal that immersive analytics results in high-quality decision making when it comes
to complex, multidimensional and spatially-oriented processes, like optimization of a supply chain.
78

Mehta (2026) Int. J. Eng. Infor. Manag. Vol. 2, Issue 1: 52-82 (2026-Jan)
ExtensivesurveysbyMarriottetal.(2018)anduserstudiesbyCordeiletal.(2017)showthatatraditional
2D dashboard is superior in accurate lookups of values, but immersive WebXR environments are far more
successful in identifying patterns, outliers, and spatial relationships. Embodied cognition Immersive tools
have the benefit of deferring the "cognitive load" needed to mentally imagine the abstract rows in the
spreadsheet as physical logistics by use of physical intuition to navigate through the data. This results
in increased involvement and quicker uncovering of unknown unknowns (surprising interactions) that are
almost always overlooked in flat, tabular reports.
In this work a fairness conscious immersive analytics framework, including causal inference, predictive
modeling, and spatial visualization, is proposed that can be used to authoritatively analyze e-commerce
logistics systems in an equity-oriented manner. Therefore, the study illustrates in real life how immersive
analytics can be used to expand fairness-conscious decision making in the logistics field. This is
done through highly integrated, causally transparent and strongly interactive facilities of exploring
multidimensional disparity data. It questions the fact that the only way of making such information
available and understandable to the stakeholders is to compromise statistical precision. With the ever-
increasing impact of algorithmic systems, regulating the use of resources in the welfare and corporate
sector, methods through which fairness measures can be studied transparently, causally, and dynamically
in optimization pipelines are becoming more important. These approaches are significant to both fairness-
directed optimization and to optimization itself. This work fits the current trends of responsible use of
AI because it employs the framing of immersive analytics both as a cognitive support tool (through the
use of spatial intelligence to identify complex patterns) and as a governance mechanism (constructing
auditable records of equity-based discussions). Necessarily, the representatives of different communities
must be actively involved in the co-design processes, which include the visualization grammar based on
the principles of ethics. The point is not only to make beautiful images, but to make decisions more
productive, and fair, quick and just, and to improve algorithms but be ethically responsible. The need of
the appropriate methodologies of benchmarking and the unified frameworks of the design of immersive
analytics is high. To be able to prove their effectiveness in a rigorous way compared to the traditional
methods of analytic approach, controlled evaluations are needed. Another advantage of our pipeline is
that it is a strong prototype that could be further developed and improved. The current system follows
the decoupled architecture, where the causal inference is done in the batch mode instead of real-time.
Such design restricts users to run precomputed causal scenarios, rather than dynamically retraining
causal models on the inside of the VR setup. Although the option ensures high frame rates and motion
comfort, it limits the ability of the analyst to interactively modify causal graphs. Moreover, such issues
as generalization (the ability to effectively transfer data to immersive platforms), somewhat unlikely
but potentially significant perceptual and cognitive bias, and technical and implementation limitations
can likewise be linked to our suggested pipeline and the field of immersive analytics in general. Future
directions In the future, it is possible to enable online updates of the pipeline with real-time streamlining
data, add more advanced edge ML and LLM-based features (e.g., customer sentiment analysis via natural
language processing, advanced double machine learning constructs with refutation tests, etc.) to optimize
the accuracy of encoding (Ménétrey et al., 2022), federated learning to decentralize fairness monitoring
and to add haptic feedback mechanisms to facilitate multimodal fairness perception. The framework
can also be improved with collaborative multi-user VR setup where multiple decision-makers could be
able to work in the same analytical space at the same time (Fanini & Gosti, 2023). Lastly, longitudinal
empirical validation, controlled evaluation and the incorporation of automated benchmarking tools will
be of paramount importance to scale of immersive analytics and apply it to sophisticated real-world
domains and situations (Hart & Staveland, 1988).
References
Allam, Z., Sharifi, A., Bibri, S. E., Jones, D. S., & Krogstie, J. (2022). The metaverse as a virtual form of smart
cities: Opportunities and challenges for environmental, economic, and social sustainability in urban futures.
Smart Cities,5(3), 771–801. https://doi.org/10.3390/smartcities5030040.
Barocas, S., Hardt, M., & Narayanan, A. (2019).Fairness and Machine Learning. fairmlbook.org.
79

Mehta (2026) Int. J. Eng. Infor. Manag. Vol. 2, Issue 1: 52-82 (2026-Jan)
Batch, A., Shin, S., Liu, J., Butcher, P. W. S., Ritsos, P. D., & Elmqvist, N. (2023). Evaluating view
management for situated visualization in web-based handheld ar.Computer Graphics Forum,42(3), 349–
360. https://doi.org/10.1111/cgf.14835.
Bierbaum, A., Just, C., Hartling, P., Meinert, K., Baker, A., & Cruz-Neira, C. (2001). Vr juggler: a virtual
platform for virtual reality application development. InProceedings IEEE Virtual Reality 2001(pp. 89–96).
https://doi.org/10.1109/VR.2001.913774.
Bowman, D. A., Kruijff, E., LaViola, J. J., & Poupyrev, I. (2004).3D User Interfaces: Theory and Practice.
Boston: Addison-Wesley. ISBN: 0-201-75867-9.
Brooke, J. (1996). Sus: A “quick and dirty” usability scale. In P. W. Jordan, B. Thomas, B. A. Weerdmeester,
& I. L. McClelland (Eds.),Usability Evaluation in Industry(pp. 189–194). London: Taylor & Francis.
Brunhart-Lupo, N., Bush, B., Gruchalla, K., Potter, K., &Smith, S.(2021). Collaborativeexplorationofscientific
datasets using immersive and statistical visualization. InProceedings of the 2021 IEEE VR Workshop on
Immersive Data Analytics (IDA): IEEE. https://www.nrel.gov/docs/fy21osti/79574.pdf.
Butcher, P. W. S., John, N. W., & Ritsos, P. D. (2021). Vria: A web-based framework for creating immersive
analytics experiences.IEEE Transactions on Visualization and Computer Graphics,27(7), 3213–3225.
https://doi.org/10.1109/TVCG.2020.2965109.
Cabrera, Á. A., Epperson, W., Hohman, F., Kahng, M., Morgenstern, J., & Chau, D. H. (2019).
Fairvis: Visual analytics for discovering intersectional bias in machine learning. InProceedings of
the 2019 IEEE Conference on Visual Analytics Science and Technology (VAST)(pp. 46–56).: IEEE.
https://doi.org/10.1109/VAST47406.2019.8986948.
Chen, L., Wang, Y., Zeng, L., Jiang, J., Zhu, X., & Peng, J. (2025). Logistics service decision for e-commerce
supply chain with fairness concern under uncertain environment.International Journal of General Systems,
54(1), 1–36. https://doi.org/10.1080/03081079.2024.2359037.
Chen, X., Wang, T., Thomas, B. W., & Ulmer, M. W. (2023). Same-day delivery with fair customer service.
European Journal of Operational Research,308(2), 738–751. https://doi.org/10.1016/j.ejor.2022.12.009.
Cordeil, M., Cunningham, A., Dwyer, T., Thomas, B. H., & Marriott, K. (2017). imaxes: Immersive
axes as embodied affordances for interactive multivariate data visualization. InProceedings of
the 30th Annual ACM Symposium on User Interface Software and Technology(pp. 71–83).: ACM.
https://doi.org/10.1145/3126594.3126613.
Correll, M. (2019). Ethical dimensions of visualization research. InProceedings of the 2019 CHI Conference on
Human Factors in Computing Systems(pp. 1–13).: ACM. https://doi.org/10.1145/3290605.3300418.
Correll, M. & Gleicher, M. (2014). Error bars considered harmful.IEEE Computer Graphics and Applications,
34(4), 8–15. https://doi.org/10.1109/TVCG.2014.2346298.
Cruz-Neira, C., Sandin, D. J., & DeFanti, T. A. (1993). Surround-screen projection-based virtual reality: the
design and implementation of the cave. InProceedings of the 20th annual conference on Computer graphics
and interactive techniques (SIGGRAPH ’93)(pp. 135–142).: ACM. https://doi.org/10.1145/166117.166134.
Cruz-Neira, C., Sandin, D. J., DeFanti, T. A., Kenyon, R. V., & Hart, J. C. (1992). The cave:
audio visual experience automatic virtual environment.Communications of the ACM,35(6), 64–73.
https://doi.org/10.1145/129888.129892.
D’Ignazio, C. & Klein, L. F. (2023).Data Feminism. MIT Press.
Doshi-Velez, F., Kortz, M., Budish, R., Bavitz, C., Gershman, S., O’Brien, D., & Wood, A. (2017).
Accountability of ai under the law: The role of explanation.arXiv preprint,arXiv:1711.01134.
https://arxiv.org/abs/1711.01134.
Ellis, G. & Dix, A. (2007). A taxonomy of clutter reduction for information visualisation.IEEE Transactions
on Visualization and Computer Graphics,13(6), 1216–1223. https://doi.org/10.1109/TVCG.2007.70535.
Ericsson, K. A. & Simon, H. A. (1993).Protocol Analysis: Verbal Reports as Data. Cambridge, MA: MIT Press,
revised edition.
Fanini, B. & Gosti, G. (2023). A new generation of collaborative immersive analytics on the web.Future Internet,
16(5), 147. https://doi.org/10.3390/fi16050147.
Franke, L. & Haehn, D. (2020). Modern scientific visualizations on the web.Informatics,7(4), 37.
https://doi.org/10.3390/informatics7040037.
Frost, J. (2024). Data aggregation: Strengths & weaknesses of aggregated data.
https://statisticsbyjim.com/basics/data-aggregation-strengths-weaknesses-aggregated-data/.
Group, I. W. W. (2023). Webxr device api specification. W3C Recommendation.
https://www.w3.org/TR/webxr/.
Hart, S. G. & Staveland, L. E. (1988). Development of nasa-tlx (task load index): Results of empirical and
theoretical research. InHuman Mental Workload(pp. 139–183). Elsevier. https://doi.org/10.1016/S0166-
4115(08)62386-9.
80

Mehta (2026) Int. J. Eng. Infor. Manag. Vol. 2, Issue 1: 52-82 (2026-Jan)
Hernán, M. A. & Robins, J. M. (2020).Causal Inference: What If. Boca Raton, FL: Chapman & Hall/CRC.
ISBN: 9780367357969 (Hardcover), 9780367357952 (Paperback), 9780429250909 (eBook).
Jerald, J. (2015).The VR Book: Human-Centered Design for Virtual Reality. Morgan & Claypool Publishers.
ISBN: 978-1627050088.
Kay, M., Heer, J., Hullman, J., Bartram, L., Agrawala, M., Fisher, D., & Gajos, K. Z. (2016).
A case study using visualization interaction logs and insight metrics to understand how analysts
arrive at insights.IEEE Transactions on Visualization and Computer Graphics,22(1), 190–200.
https://doi.org/10.1109/TVCG.2015.2467613.
Li, X. & Li, D. (2023). Digital financial inclusion: Visualizing the academic literature.Research in International
Business and Finance,64, 101862. https://doi.org/10.1016/j.ribaf.2022.101862.
Lipton, Z. C. (2018). The mythos of model interpretability.Queue,16(3), 31–57.
https://doi.org/10.1145/3236386.3241340.
Marriott, K., Schreiber, F., Dwyer, T., Klein, K., Riche, N. H., Itoh, T., Stuerzlinger, W., & Thomas, B. H.
(2018).Immersive Analytics. Springer. https://doi.org/10.1007/978-3-030-01388-2.
McKinney, W. (2012).Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython. O’Reilly
Media. https://www.oreilly.com/library/view/python-for-data/9781449323592.
Ménétrey, J., Pasin, M., Felber, P., & Schiavoni, V. (2022). Webassembly as a common layer for the cloud-edge
continuum. InProceedings of the 2nd Workshop on Flexible Resource and Application Management on the Edge
(FRAME ’22)(pp. 3–8).: Association for Computing Machinery. https://doi.org/10.1145/3526059.3533618.
Morello-Frosch, R., Pastor, M. J., & Sadd, J. (2002). Integrating environmental justice and the precautionary
principle in research and policy-making: The case of ambient air toxics exposures and health risks among
schoolchildren in los angeles.The ANNALS of the American Academy of Political and Social Science,584(1),
47–68. https://doi.org/10.1177/000271620258400104.
Pearl, J. (2009).Causality: Models, Reasoning, and Inference. Cambridge University Press, 2nd edition. ISBN:
978-0521895606.
Pearl, J. & Mackenzie, D. (2018).The Book of Why: The New Science of Cause and Effect. Basic Books. ISBN:
978-0465097614.
Pramanik, A., Sarker, S., Sarkar, S., & Bose, I. (2024). Fgi-cogvit: Fuzzy granule-based interpretable cognitive
vision transformer for early detection of alzheimer’s disease using mri scan images.Information Systems
Frontiers. https://doi.org/10.1007/s10796-024-10541-7.
Pramanik, A., Sarker, S., Sarkar, S., & Pal, S. (2025). Real-time fall detection on roads
using transfer learning-based granulated bi-lstm.Knowledge-Based Systems, 311, 113038.
https://doi.org/10.1016/j.knosys.2025.113038.
Reardon, S. F. (2011). The widening academic achievement gap between the rich and the poor.Educational
Leadership,68(7), 10–16. https://cepa.stanford.edu/content/widening-academic-achievement-gap-between-
rich-and-poor-new-evidence-and-possible-explanations.
Rubin, D. B. (2005). Causal inference using potential outcomes.Journal of the American Statistical Association,
100(469), 322–331. https://doi.org/10.1198/016214504000001880.
Sambasivan, N., Arnesen, E., Hutchinson, B., Doshi, T., & Prabhakaran, V. (2021). Re-imagining algorithmic
fairness in india and beyond. InProceedings of the 2021 ACM Conference on Fairness, Accountability, and
Transparency (FAccT ’21)(pp. 315–328).: ACM. https://doi.org/10.1145/3442188.3445896.
Sarkar, S., Chain, M., Nayak, S., & Maiti, J. (2019). Decision support system for prediction of occupational
accident: A case study from a steel plant. InEmerging Technologies in Data Mining and Information Security,
volume 813 (pp. 787–796). Springer, Singapore. https://doi.org/10.1007/978-981-13-1498-8_69.
Skarbez, R., Polys, N. F., Ogle, J. T., North, C., & Bowman, D. A. (2019). Immersive analytics: Theory and
research agenda.Frontiers in Robotics and AI,6, 82. https://doi.org/10.3389/frobt.2019.00082.
Solokov, A. (2025). Beyond the binary: Improving data visualization for intersectional identities.Nightingale:
Journal of the Data Visualization Society.https://nightingaledvs.com/beyond-the-binary/. Accessed:
2025-12-28.
Stevens, S. S. (1957). On the psychophysical law.Psychological Review,64(3), 153–181.
https://doi.org/10.1037/h0046162.
Valentini, P. P. (2012). Natural interface in augmented reality interactive simulations.Virtual and Physical
Prototyping,7(2), 137–151. https://doi.org/10.1080/17452759.2012.682332.
Ware, C. (2012).Information Visualization: Perception for Design. Boston: Morgan Kaufmann, 3rd edition.
ISBN:978-0-12-381464-7.
Wells, K. J., Attoh, W. K., & Cullen, D. (2021). “just-in-place” labor: Driver organizing
in the uber workplace.Environment and Planning A: Economy and Space,53(2), 315–331.
https://doi.org/10.1177/0308518X20949266.
81

Mehta (2026) Int. J. Eng. Infor. Manag. Vol. 2, Issue 1: 52-82 (2026-Jan)
Wieringa, M. (2020). What to account for when accounting for algorithms: A systematic literature
review on algorithmic accountability. InProceedings of the 2020 Conference on Fairness, Accountability,
and Transparency, FAT* ’20 (pp. 1–18). Barcelona, Spain: Association for Computing Machinery.
https://doi.org/10.1145/3351095.3372833.
Willett, W., Prouzeau, A., Anthes, C., Büschel, W., Dunne, C., Dwyer, T., Grubert, J., Haga, J. H.,
Kirshenbaum, N., Kobayashi, D., Lin, T., Olaosebikan, M., Pointecker, F., Saffo, D., Saquib, N., Schmalstieg,
D., AlbersSzafir, D., Whitlock, M., &Yang, Y.(2021). Grandchallengesinimmersiveanalytics. InProceedings
of the 2021 CHI Conference on Human Factors in Computing Systems, CHI ’21 (pp. 1–17). New York, NY,
USA: Association for Computing Machinery. https://doi.org/10.1145/3411764.3446866.
Xu, Z., Tan, Y., Wang, X., & Li, X. (2023). Data-driven analysis for the operation status of the
e-commerce platform based on olist. InProceedings of the 1st International Conference on Public
Management, Digital Economy and Internet Technology (ICPDI 2022)(pp. 859–867).: SciTePress.
https://doi.org/10.5220/0011836600003607.
Yang, H., Liu, Z., Zhang, Z., Zhuang, C., & Chen, X. (2023). Towards robust fairness-aware recommendation.
InProceedings of the 17th ACM Conference on Recommender Systems (RecSys ’23)(pp. 211–222). Singapore:
Association for Computing Machinery. https://doi.org/10.1145/3604915.3608784.
82
