---
title: A virtual sensing approach to enhancing personalized strategies for indoor environmental quality
  and residential energy management
url: https://doi.org/10.1016/j.buildenv.2024.111684
category: consumer-behavior
subcategory: empirical
date: 2024-05
venue: Building and Environment
authors:
- Stylianos Karatzas
- Jorge Merino
- Alena Puchkova
source: openalex-oa
pdf_url: https://www.repository.cam.ac.uk/bitstreams/1ce273a4-d783-4a55-8390-f01e3cf0a0af/download
pages: 13
chars: 70772
fetched_at: '2026-11-08T17:05:11+00:00'
kb_version: 1
---

# A virtual sensing approach to enhancing personalized strategies for indoor environmental quality and residential energy management

Building and Environment 261 (2024) 111684
Available online 27 May 2024
0360-1323/© 2024 The Authors. Published by Elsevier Ltd. This is an open access article under the CC BY license ( http://creativecommons.org/licenses/by/4.0/).
A virtual sensing approach to enhancing personalized strategies for indoor
environmental quality and residential energy management
Stylianos Karatzas a,*, Jorge Merino a, Alena Puchkova a, Christos Mountzouris b,
Grigoris Protopsaltis b, John Gialelis b, Ajith Kumar Parlikad a
a University of Cambridge, Department of Engineering, Institute for Manufacturing, Cambridge, UK
b University of Patras, Department of Electrical Engineering, Patras, Greece
ARTICLE INFO
Keywords:
Energy efficiency
Virtual sensing
Indoor environmental quality (IEQ)
Thermal comfort
Demand side management
Indoor air quality (IAQ)
ABSTRACT
This study presents a consumer-centric approach on Demand-Side Management (DSM) for residential energy
systems, aiming to align cost-efficient energy strategies with the individual’s preferences on operational time-
flexibility for residential electric appliances, thermal comfort, and indoor air quality. The optimization frame-
work innovatively incorporates forecasts of the Indoor Air Quality (IAQ) index and thermal comfort levels using
virtual sensing technology to predict their day-ahead values, which are furtherly integrated as constraints in the
optimization problem. A dual-objective approach is employed, balancing the minimization of electricity costs all
whilst increasing consumer’s satisfaction. The approach underlines the critical role of consumer participation in
DSM and illustrates how the integration of smart home technologies can lead to reductions in energy con-
sumption and cost savings. This paradigm not only promotes consumer engagement in energy management but
also showcases the potential of intelligent home systems to optimize energy usage while maintaining person-
alized comfort standards.
1. Introduction
Currently, the climate targets stated in the Paris Agreement [1] steer
the European Union (EU) towards a transition into a net zero economy
and society by 2050, emphasizing the urgency for increased energy ef-
ficiency. The strategic application of technologies and practices to sys-
tematically reduce energy consumption while preserving services
reliability and performance, is pivotal in diminishing the EU’s carbon
footprint and promoting sustainable growth. In 2021, 40 % of the total
energy demand across the EU was attributable to buildings [2], with
residencies accounting for a significant 67 % of this demand, consti-
tuting 18.6 % of the gross inland energy consumption in the EU [2]. This
substantial portion of energy consumption is primarily driven by the
necessity for maintaining a thermally comfortable indoor environment,
as heating alone accounts for 64.4 % [2] of residencies’ total energy
usage, underscoring the challenge for effective management of resi-
dential heating and cooling systems. In this context, it becomes imper-
ative to pursue a balanced approach that ensures cost-effective
operation of residential flexible power loads, while minimizing the
disruption of the consumers’ daily routine and improving their overall
environmental comfort experience, which can lead to significant im-
provements on health outcomes. In their review study, William J. Fisk
[3] synthesized findings indicating that low indoor temperatures and
inadequate thermal comfort are often associated with negative health
outcomes. Additionally, the review suggests that improvements in in-
door air quality are consistently linked with better respiratory health
outcomes in non-asthma conditions and overall general health.
Demand-Side Management (DSM) has emerged as a pivotal component
of residential energy management systems, fundamental to optimizing
energy consumption, minimizing energy costs, improving energy grid
reliability, and facilitating the integration of renewable energy sources
[4]. DSM plays a pivotal role in enhancing the robustness and resilience
of energy systems, enabling them to adapt to rapid transformations
within the evolving energy landscape. Consequently, they provide sub-
stantial economic and environmental advantages, by fostering syner-
gistic interactions among a diverse array of stakeholders, ranging from
consumers to utility providers. Modern DSM systems are empowered by
big data analytics, artificial intelligence (AI), machine learning (ML),
and Internet of Things (IoT) connectivity [5]. These technologies can
unlock the complex and stochastic behavioral patterns of energy
* Corresponding author.
E-mail addresses: stylianos.karatzas@upatras.gr, sk2095@cam.ac.uk (S. Karatzas).
Contents lists available at ScienceDirect
Building and Environment
journal homepage: www.elsevier.com/locate/buildenv
https://doi.org/10.1016/j.buildenv.2024.111684
Received 1 March 2024; Received in revised form 23 May 2024; Accepted 25 May 2024

Building and Environment 261 (2024) 111684
2
consumers, providing precise insights into their energy usage dynamics
[6]. Highly customized optimization algorithms aligned with in-
dividual’s comfort preferences and energy usage needs mark a trans-
formative shift towards a more personalized, data-oriented, and
technologically sophisticated approach to residential energy manage-
ment systems [7]. Furthermore, the efficacy of modern DSM systems is
rooted on proactive consumer engagement, where end-users are active
participants in the energy marketplace. This engagement is facilitated by
user-friendly interfaces and real-time feedback mechanisms, empower-
ing consumers to make informed decisions regarding their energy usage.
At the core of today’s energy market transformation stand the dy-
namic energy pricing schemes, whose incorporation to smart home
systems promotes the consumer-centrism of the modern energy land-
scape [8]. The implementation of such schemes incentivizes efficient
energy usage by consumers and aligns their energy behavioral patterns
with broader energy conservation and sustainability goals. In addition,
dynamic pricing schemes aim to provide a balanced approach between
the enhancement of consumer’s welfare, the stability, efficiency and
sustainability of the energy grid, as well as the optimization of the
economic outcomes for energy retail companies. In DSM, various pricing
schemes are employed to encourage efficient energy use from consumers
[9]. Time-of-Use (ToU) pricing differentiates the cost of energy based on
the time of day, discouraging use during high-demand periods with
higher rates. Real-Time Pricing (RTP) moves a step further by reflecting
the cost of electricity instantaneously, thus signaling consumers to
adjust usage in response to price fluctuations. Critical Peak Pricing (CPP)
sharpens this approach by imposing even higher rates during critical
peak times, typically forecasted a day ahead, to deter consumption
during system strains. Lastly, Peak Time Rebates (PTR) provide rebates
to consumers who reduce their demand during these peak times,
rewarding efficient energy consumption behavior.
Another cornerstone for DSM is Home Energy Management Systems
(HEMS), which are integral to the residential sector’s energy conserva-
tion efforts, serving as an intermediate node for communication between
households and utility providers [10]. By enabling the real-time transfer
of energy consumption data, HEMS facilitate more informed energy
usage decisions, contribute to the optimization of households’ energy
profiles, and enhance the overall efficiency and reliability of the power
grid. This exchange not only promotes energy-saving practices but also
supports providers in demand forecasting and managing peak loads,
which is critical for maintaining grid stability.
The inherent limitations of physical sensor systems, such as suscep-
tibility to systematic errors, noisy signals, short lifetime, need for peri-
odic maintenance and operational deficiencies, necessitate the evolution
towards more sophisticated sensing methodologies [11]. Virtual sensing
technology emerges as a robust alternative to physical sensing, har-
nessing the power of AI and ML to enable cost-efficient, agile, scalable,
resilient, and non-intrusive data collection [12,13]. These
software-based sensing systems offer a transformative solution within
the IoT domain, facilitating seamless integration of data intelligence
with physical sensing. Specifically, in our context, virtual sensing tech-
nology offers two critical advantages. Firstly, it obviates the need for
users to be burdened with disruptive equipment on their bodies. By
moving away from physical sensor reliance, we ensure a more
user-friendly and non-intrusive experience. Secondly, and perhaps most
crucially, virtual sensing allows for the prediction of sensor values for
the upcoming day. This predictive capability is integral to our optimi-
zation efforts, enabling us to anticipate and prepare for future scenarios,
thereby enhancing overall efficiency and effectiveness.
The key contributions of this paper are:
⁃ The introduction of a consumer-centric approach in DSM, high-
lighting the shift from the legacy utility-centric paradigm of DSM to a
modern, data-driven and consumer-centric one, which emphasizes
the importance of aligning energy management strategies with the
individual’s preferences on operational time-flexibility, thermal
comfort level and indoor air quality status.
⁃ The integration of the air quality index as a regulatory constraint in
the optimization problem of household electric appliances sched-
uling, enhancing indoor air quality control while optimizing energy
consumption.
⁃ Leveraging virtual sensing to integrate a precise assessment of con-
sumer’s thermal comfort level and indoor air quality status, thereby
optimizing the scheduling of the AC and the AP units to align with
individualized comfort and air quality preferences.
Following the introduction, the paper is structured as follows:
⁃ Literature Review: This section provides a review of existing studies
and theoretical frameworks pertinent to optimization of energy
consumption in the residential environment, indoor environmental
quality control in regards to household appliances optimized
scheduling, particularly focusing on Linear Programming. It aims to
identify gaps in current research and set the stage for the method-
ologies introduced in this paper.
⁃ Methods and Tools: The core methodologies and tools used in this
study are segmented into three detailed subsections:
Integer Linear Programming Framework: Explores the theoretical
background and application of the Integer Linear Programming frame-
work used for optimizing indoor environmental conditions, detailing the
mathematical models and operational constraints.
Virtual Sensing Framework for Indoor Thermal Comfort and Tem-
perature: Discusses a specialized framework designed to predict indoor
thermal comfort and temperature, covering the involved algorithms and
integration to the overall framework.
Virtual Sensing Framework for Indoor Air Quality (IAQ) Index: Fo-
cuses on the framework developed for assessing the IAQ index,
describing the sensing technologies, data analysis methods, and pre-
dictive capabilities.
⁃ Results: This section presents the findings from the application of the
described framework, analyzing their effectiveness in real-world
scenarios and their implications for indoor environmental
management.
⁃ Conclusion and Future Work: The paper concludes by summarizing
the key findings and contributions of the research. We also discuss
potential avenues for future research.
2. Literature Review
Academic interest in consumer-centric Demand Side Management
(DSM) is increasing, largely because it effectively encourages partici-
pation in demand response (DR) initiatives and fosters sustainable en-
ergy practices. A crucial element in developing Demand Side
Management (DSM) is optimizing demand. Typically, appliance sched-
uling takes into account time slots, user preferences, and different
consumption profiles to either minimize peak demand (Qayyum., 2015)
or lower energy costs [14]) DSM strategies can be designed using either
heuristic [15] or deterministic algorithms (Soares, 2022). This interest is
driven by the ability of these approaches to align with and adapt to
consumers’ preferences and daily routines. By minimizing disruptions to
regular activities, consumer-centric DSM ensures a seamless integration
into everyday life. The emergence of smart home technologies has
facilitated the practical implementation of personalized Demand Side
Management (DSM) strategies that are evolving into actionable solu-
tions that lead to significant cost savings and enhanced energy
efficiency.
In several studies, an inconvenience factor (IC) has been employed to
quantify and penalize deviations from typical household load schedules,
measuring the level of disruption to consumer’s daily routine. This
S. Karatzas et al.

Building and Environment 261 (2024) 111684
3
factor encapsulates the concept of operational time-flexibility and serves
as a balancing component in traditional load scheduling algorithms,
striking a balance between cost-efficient management of household
loads and minimal intrusiveness in consumer’s lifestyle patterns. Lu
et al. [16] integrated a weighted IC to measure the discomfort experi-
enced by consumers due to time shifts in their regular electricity usage
patterns from demand-response program participation. A lower value
implies a reduced penalty for discomfort, thereby encouraging con-
sumers to shift more load to lower their overall costs. Utilizing a
balanced factor of 0.2 between cost-savings and consumer comfort, the
optimized schedule resulted in a significant 34.71 % reduction in total
energy costs. In the same context, Yahia et al. [17] incorporated an IC in
the objective function to represent the deviation between consumer’s
preferred schedule, acknowledging the potential discomfort associated
with shifting appliance usage. The consumers’ willingness to adjust their
usage is captured by the metric of flexibility ratio with a wider opera-
tional window indicating a higher tolerance for schedule adjustments to
optimize energy costs. This study resulted to substantial electricity cost
savings - approximately 35 % for a small-scale scenario and up to 50 %
for a large-scale case - compared to consumer-defined schedules.
While inconvenience factors (ICs) are important contributors in
balancing cost-efficiency with user comfort, it is crucial to acknowledge
certain limitations. These factors rely significantly on subjective as-
sessments of consumer discomfort, which can vary widely between in-
dividuals. This variability introduces challenges in standardizing
optimal scheduling, potentially leading to less predictable energy
management outcomes. Moreover, the dependency on consumer input
to determine ICs can complicate the implementation process, affecting
the scalability and overall effectiveness of such systems.
Charoen et al. [18] developed a comprehensive day-ahead sched-
uling framework coupled with an intra-day rescheduling system for
flexible household loads, integrating a cost metric for consumer
discomfort arising from operational shifts. The model assigns a priority
value to each flexible load, reflecting its significance to the user; a high
priority value indicates that any shift from the preferred operating time
would result in considerable discomfort, thereby influencing the fairness
of the calculated electricity costs among the community and ensuring
minimal disturbance to the consumer’s routine. However, this approach
does introduce certain challenges, as it necessitates that users manually
set the priority for each load, which can be a tedious process. This
requirement potentially limits the model’s practicality and
user-friendliness, making it less accessible for some consumers who may
find continuous interaction with the system overly demanding.
M. Awais et al. [19] incorporated the peak-to-average ratio as a
critical parameter among electricity costs and consumer comfort with
the aim of maximizing utility for both the consumer and the grid.
Furthermore, a hybrid heuristic optimization framework was designed
to enhance computational efficiency in solving such complex load
scheduling problems, entailing a comparative analysis of two day-ahead
and critical peak pricing models to determine their cost-efficacy for
consumers and stability for grid. However, the method does not allow
consumers to indicate their tolerance for disruption, providing a fixed
solution that lacks customization options. This constraint prevents users
from adapting the system to suit their specific needs and preferences,
which could lead to reduced satisfaction.
D. Setlhaolo [20] used mixed integer non-linear programming to
enable consumers get insights on optimal usage of their loads in regards
to electricity costs and assist with the rescheduling to off peak time
periods. A weighting factor α is introduced to model the flexibility of an
occupant to shift demand-side elements, which is additionally an indi-
cator of the level of inconvenience that the user would be subjected to.
This study achieved a substantial reduction on the cost of electricity and
additionally incorporated financial incentives for the effective applica-
tion of the proposed schedule.
In their study, Ghayour et al. [21]utilized mixed integer linear pro-
gramming (MILP) to transition from previously favored non-linear
approaches, achieving a single, optimal solution under conditions of
uncertainty. This method accounts for the variability in renewable en-
ergy sources and market volatility, and incorporates both heat and
electrical energy supplies, leading to a notable reduction in total energy
costs. However, the adoption of this framework involves substantial
retrofits such as additional boilers and combined heat and power (CHP)
systems. These necessary modifications entail significant investment
and complex installation procedures, which may deter widespread
implementation despite the prospective cost savings.
Furthermore, several studies have incorporated thermal-flexibility
profiles within the optimization strategies, extending the consumer-
centrism in DSM beyond the operational time-flexibility profiles.
These approaches handle cooling and heating systems not merely as
appliances but as integral components that shape the living environ-
ment. E. Shirazi et al. [22] proposed a discomfort index that integrates
both the preferred temperature range, defined as the average between
the upper and lower temperature limits, and the deviation from the
preferred operational time window for household appliances. In A.
Agnetis et al. study [23], the optimization problem is structured to
maximize both consumer’s scheduling and climatic comfort preferences.
Climatic comfort is an index value, representing the consumer’s will-
ingness to maintain the indoor temperature of the household within the
desired lower and upper boundaries. Anvari-Moghaddam et al. [24]
devised a multi-objective optimization framework with distinct objec-
tives for maximizing consumer convenience and thermal comfort.
Consumer’s thermal comfort is evaluated using a time-series, which
integrates lags of indoor temperature data, user-defined temperature
setpoints, and deviations from predefined comfort thresholds. S. Wang
et al. [25] implemented a simplified adaptation of Fanger’s thermal
comfort model for HVAC load scheduling, considering only the indoor
temperature, consumer gender, and a standardized seasonal clothing
insulation value. This simplification aims to align the model with
practical home energy management systems, where day-ahead predic-
tion of all original model parameters is challenging. Lin et al. [26] in-
tegrated several models into a thermal model to study the impact of
occupants’ behaviors on the building energy consumption and an elec-
tric consumption model was developed to simulate the usage pattern
and the electricity input to household electric appliances. Karatzas et al.
[27] developed a context-driven energy management framework
focusing on human factors and business processes hosted in the building,
through the introduction of comfort and business process-related pa-
rameters. The major innovation of the proposed framework is that it
considers the relationship between the major load types with the ac-
tivities in a building, developing a linkage between energy management
and organizational structures. Consequently, valuable knowledge can be
gained on how everyday actions affect energy consumption, as well as
how much users can potentially improve their energy consuming habits.
While these studies offer valuable insights into optimizing household
energy management by balancing load scheduling flexibility with
thermal comfort, they predominantly focus on indoor temperature as the
primary metric of environmental comfort. This approach overlooks the
multifaceted nature of human comfort, which encompasses a wider
range of physiological and psychological factors. The literature, there-
fore, indicates a research gap in developing more comprehensive envi-
ronmental comfort models that integrate additional dimensions,
potentially offering a more nuanced understanding of consumer pref-
erences and behaviors in demand-side management strategies.
3. Methods and material
3.1. Integer linear programming framework
In this section, an Integer Linear Programming (ILP) framework is
introduced (Fig. 1), aimed to minimize the daily energy costs associated
with controllable electricity loads in residential settings while accom-
modating consumer’s preferences regarding scheduling, thermal
S. Karatzas et al.

Building and Environment 261 (2024) 111684
4
comfort and air quality status. The objective of this framework extends
beyond the mere cost-efficient scheduling of controllable electricity
loads; it is also constrained on the preferred operational time window for
each load, while ensuring that thermal comfort and air quality condi-
tions do not violate consumer preferences. The temporal scope T under
examination encompasses a full 24-h cycle, starting from 00:00 to 23:00,
with each hour furtherly divided into I equal time intervals. This gran-
ular approach facilitates a dual purpose; firstly, to incorporate the
patterns of energy demand with a higher degree of precision, which in
turn allows for a more precise scheduling; secondly, to ensure compat-
ibility with different electricity pricing models, specifically those that
operate at a lower temporal resolution than hourly intervals (see Fig. 2).
For the proposed ILP framework, the controllable residential electric
appliances are classified into four (4) principal categories: (i): time-
controllable loads, (ii): phase-controllable loads, (iii): air-conditioning
(AC) unit, and (iv): air-purifier (AP) unit. The time-controllable loads
Fig. 1. Overall architecture.
Fig. 2. Correlation Heatmap for the target variable of clothing insulation.
S. Karatzas et al.

Building and Environment 261 (2024) 111684
5
are distinguished by their operational flexibility, allowing for scheduling
of their function within strategically chosen time windows. Consumer
predefines a set of preferences regarding the earliest start time (EST) and
the latest end time (LET) for each time-controllable load, thus estab-
lishing a well-defined time-schedule that aligns with their daily activ-
ities. Once activated, a time-controllable load requires continuous
operation to complete its cycle efficiently. In this study, the set of
household loads examined comprises the washing machine (WM), the
tumble drier (TD) and the dishwasher (DW). Phase-shiftable loads are
characterized by operation in discrete, non-continuous phases, an
attribute that facilitates strategic interruptions and subsequent re-
sumptions during their operation cycle. Within this category, a nuanced
distinction is drawn between phase-variable and phase-constant loads.
Phase-variable loads are marked by their adaptability in power con-
sumption, which can be dynamically modulated across various levels
during their operational phases, enabling the optimization of energy
usage in response to fluctuating energy demands and varying electricity
tariff rates. Conversely, phase-constant loads are characterized by their
steady power consumption throughout their operational cycle, resulting
in a predictable energy demand profile. Both phase-variable and phase-
constant loads share a common requirement; the necessity for a known
maximum amount of power to ensure their full and efficient operation.
To synchronize phase-shiftable loads with a consumer’s daily routine, it
is essential for the consumer to specify the earliest start time (EST) and
latest end time (LET), mirroring the approach taken with time-shiftable
loads, too. In the proposed ILP problem, the electric vehicle (EV) and the
electric water heater (EWH) stand as the phase-variable and phase-
constant load, respectively. Lastly, the non-controllable and non-
shiftable residential electric loads, such as refrigerator and oven, are
not omitted; they are considered as the aggregated baseline load,
denoted as bt,i.
The electricity tariff πt adheres to the day-ahead pricing model, yet it
is adaptable for a time-of-use model if necessary. The study accounts for
the variability and unpredictability of energy markets by dividing each
hour into It intervals, enabling a more responsive approach to demand-
side management. The objective function (Eq (1)) represents the total
energy costs by quantifying those associated with the time-controllable
loads, the phase-controllable loads, the AC unit, the AP unit and the
baseline load. Two monetary penalty coefficients are integrated in the
objective function. They serve the purpose of integrating the deviations
from consumer’s desired thermal comfort range and minimum air
quality index into the optimization problem, ensuring a balanced
approach between minimizing the daily electricity costs and maintain-
ing the consumer’s preferences. Penalty coefficient ρAC (€/◦C) quantifies
the economic value consumers place on thermal comfort, monetizing
each degree of temperature variance from their selected range. This
calibration of comfort preferences offers a precise financial measure for
temperature regulation in the optimization schema. Similarly, the pen-
alty coefficient ρAP(€/IAQ) corresponds to the financial impact associ-
ated with each incremental unit change in the air quality index from the
consumer’s minimum acceptable level, thereby integrating air quality
standards into the economic framework of household energy
management.
minZ=
∑T
t=1
×
∑I
i=1
πt,i×
(
bt,i+
∑J
j=1
pj,t,i+
∑K
k=1
qk,t,i+
∑L
m=1
ym,t,i+ PAC+ PAP
)
+
∑T
t=1
×
∑I
i=1

ρAC× σtemp+ ρAP× σAQ
)
(1)
Where πt,i is the electricity tariff per timestep, bt,i is the aggregated
baseline consumption, pj,t,i the consumption of time-controllable loads,
qk,t,i the consumption of phase-constant loads, ym,t,i the consumption of
phase-variable loads, PAC and PAP are the power demands of the air-
conditioning and air purifier units respectively, ρAC and ρAP are pen-
alty coefficients, σtemp and σAQ are the deviations of temperature and air
quality index from their desired range.
3.1.1. Time-controllable loads
Each time-controllable load j is governed by an operation cycle of
duration dj, with power demand fj,r during in each operation stage r,
operating within a consumer-defined daily time-window. The binary
decision variable wj,r,t,i indicates the load’s activity status, subjected to
constraints (Eq (2)) - (Eq (9)). Constraints (Eq (2)) and (Eq (3)) dictate
the power usage and operational status within the designated time
window, whereas the constraints (Eq (4)) - (Eq (6)) sequence load op-
erations, ensuring exclusivity and adherence to the schedule. Lastly,
constraints (Eq (7)) - (Eq (9)) ensure that the initiation and duration of a
load’s activity comply with the schedule, while maintaining power de-
mand within established boundaries.
pj,t,i=
∑dj
r=1
fj,r× wj,r,t,i, j= 1,.., J, t= 1, …, T, i= 1,.., It (2)
pj,t,i= 0, j= 1,.., J, t< Tstart,j∨ t> Tend,j, i= 1,..It (3)
∑dj
r=1
wj,r,t,i≤ 1, j= 1,.., J, t∈
{
Tstart,j, Tend,j
}
, i= 1,..It (4)
wj,r+1,t+1,i+1≥ wj,r,t,i, j= 1,.., J, r= 1,.., dj 1, t= Tstart,j,.., Tend 1,j, i
= 1,..It (5)
∑Tend,j
t=Tstart,j
wj,r,t,i= 1, j= 1,.., J, r= 1,.., dj, i= 1,..It (6)
∑It
i=1
wj,1,t,i≥ 1, j= 1,.., J, t= Tstart,j,.., Tend 1,j dj (7)
wj,r,t,i∈{0, 1}, j= 1,.., J, r= 1,.., dj, t= Tstart,j,.., Tend,j, i= 1,.., It (8)
pj,t,i≥ 0, j= 1,.., J, t= 1,.., T, i= 1, …, It (9)
Where pj,t,i is the actual power demand of each time step, fj,r is the
required power demand for each operation stage, wj,r,t,i is the binary
decision variable, dj is the duration of a complete operation cycle, T is
the temporal scope, It is the amount of sub-hour intervals, Tstart,j and
Tend,j are user-defined total time constraints.
3.1.2. Phase-variable loads
Phase-constant loads k maintain a steady power demand Qk,t,i during
each active time-slot, while phase-variable loads m modulate their
power intake Qs m through s distinct stages. The operational protocols for
these loads are meticulously designed to reach a predetermined supply
threshold, reflecting the consumers’ specific state-of-charge (SoC) or
temperature preferences. Constraints (Eq (10)) - (Eq (14)) delineate the
operation of phase-constant loads within a prescribed time frame,
ensuring adherence to consumer-defined energy ceilings. Similarly,
constraints (Eq (15)) - (Eq (20)) orchestrate the dynamic energy con-
sumption of phase-variable loads, achieving the desired operational
states within the consumer-allocated temporal boundaries. Decision
variables uk,t,i and xs m,t,i serve as binary indicators of the active status for
phase-constant and phase-variable loads, respectively, ensuring their
integration within the household’s strategic energy management
schema.
qk,t,i= uk,t,i× Qk,t,i, k= 1,.., K, t= Tstart,k,.., Tend,k, i= 1, …, It (10)
S. Karatzas et al.

Building and Environment 261 (2024) 111684
6
qk,t,i= 0, k= 1,.., K, t< Tstart,k∨ t> Tend,k, i= 1, …, It (11)
qk,t,i≥ 0, k= 1,.., K, t= 1,.., T, i= 1, …, It (12)
∑Tend,k
t=Tstart,k
qk,t,i= Ek, k= 1,.., K, i= 1, …, It (13)
uk,t,i∈{0, 1}, k= 1,.., K, t= Tstart,k,.., Tend,k, i= 1, …, It (14)
ym,t,i=
∑S
s=1
xs m,t,i× Qs m, m= 1,.., M, t= Tstart,m,.., Tend,m, i= 1, …, It (15)
∑S
s=1
xs m,t,i≤ 1, m= 1,.., M, t= Tstart,m,.., Tend,m, i= 1, …, It (16)
∑Tend,m
t=Tstart,m
ym,t,i= Gm, m= 1,.., M, i= 1, …, It (17)
ym,t,i= 0, m= 1,.., M, t< Tstart,m∨ t> Tend,m, i= 1, …, It (18)
xs m,t,i∈{0, 1}, s= 0,.., S, m= 1,.., M, t= Tstart,m,.., Tend,m, i= 1, …, It
(19)
ym,t,i≥ 0, m= 1,.., M, t= 1,.., T, i= 1, …, It (20)
Where qk,t,i is the actual power demand of each time step, uk,t,i is the
decision variable, Qk,t,i is the required power demand for each time slot,
K is the number of phase-constant loads, Tstart,k and Tend,k are optional
user-defined total time constraints and Ek is the total power allocated for
the phase-constant load. As for the phase-variable loads, ym,t,i is the
actual power demand of each time step, xs m,t,i is the decision variable, Qs m
is the required power demand of each step s, M is the number of phase-
variable loads, Tstart,m and Tend,m are optional user-defined total time
constraints.
3.1.3. Air-conditioning and purifier units
The operation of AC and AP units are described by (Eq (21)) and (Eq
(22)), respectively. Their operation is discretized into five (5) levels of
operation, accounting to 0 %, 25 %, 50 %, 75 % and 100 % of their
nominal power.
PAC= ∑4
p=0
0, 25× p× δp,t,i× PAC nom, t= 1,.., T, i= 1, …, It (21)
PAP= ∑4
p=0
0, 25× p× δʹ p,t,i× PAP nom, t= 1,.., T, i= 1, …, It (22)
∑4
p=0
δp,t,i≤ 1, t= 1,.., T, i= 1, …, It (23)
∑4
p=0
δʹ p,t,i≤ 1, t= 1,.., T, i= 1, …, It (24)
Where PAC and PAP are the total power demand of the AC and the air
purifier units respectively, PAC nom and PAP nom correspond to their nominal
power, while δp,t,i and δʹ p,t,i are the binary decision variables.
To ensure that the consumer’s preferences regarding the indoor
thermal comfort and indoor air quality are not violated, additional
constraints are employed, as described by (Eq (25)) - (Eq (29)).
σtemp≥ θin t,i θmax, t= 1,.., T, i= 1, …, It (25)
σtemp≥ θmin θin t,i, t= 1,.., T, i= 1, …, It (26)
σtemp ≥ 0 (27)
σAQ ≥ IAQmin IAQin t,i (28)
σAQ ≥ 0 (29)
Where σtemp is the deviation from the temperature limit θmin or θmax as
calculated by (Eq (31)) and user-defined thermal comfort tolerances, θin t,i
is the current temperature, σAQ is the deviation from the minimum
acceptable indoor air quality index IAQmin and IAQin t,i is the indoor air
quality index at the current timestep.
3.2. Virtual sensing framework for indoor thermal comfort level and
indoor temperature
In this section, we explore the implementation of a virtual sensing
framework aimed at enhancing the prediction and optimization of in-
dividual thermal comfort. The framework’s cornerstone is a virtual
sensor capable of forecasting the Predicted Mean Vote (PMV) and cor-
responding temperature on an hourly, day-ahead basis. This approach
establishes a direct correlation between PMV and temperature,
streamlining the process of integrating user comfort preferences into the
overall optimization problem. The following subsections detail the
design, development, and operational aspects of this virtual sensing
framework.
The thermostatic load of the AC unit functions at four (5) distinct
power levels, corresponding to equal fractions of its nominal power PAC.
The operation of this unit serves the purpose of an optimal balance be-
tween consumer’s requirements for thermal comfort, delineated by
Fanger’s seven-point thermal comfort scale, and cost-efficiency, as ar-
ticulated by the monetary penalty ρAC. Specifically, the Fanger’s scale
spans in the discrete set of values from  3 (cold) to +3 (warm),
reflecting seven (7) discrete comfort states. The thermal comfort model
relies on both environmental factors — indoor air temperature, relative
humidity, air velocity and mean radiant temperature (MRT) — and the
physiological parameters of metabolic rate and clothing insulation.
The metabolic rate quantifies the energy output of an individual,
typically assuming a restful state with adjustments for transient activ-
ities. In this study, the metabolic rate is considered to be equal to 1 met,
indicative of a sedentary state - the typical one for inhabitants within
indoor environments. Instantaneous increases of the metabolic rate from
short-duration indoor activities are excluded as they would not have any
significant effect on the median hourly metabolic rate.
Clothing insulation is a metric of garments’ thermal insulation, with
higher values indicating greater thermal resistance, thus retaining the
body’s thermal sensation in cooler ambient conditions. A random forest
regressor [28] was employed for regression analysis with the aim of
predicting the individual’s clothing insulation, trained and validated on
historical recordings from multiple thermal comfort studies included on
ASHRAE-DB II — refined to 78,909 records after data preprocessing. In
the feature selection step, the key variables for the predictive model
were identified; specifically, indoor air temperature, relative humidity,
mean monthly outdoor temperature, and seasonality resulted as the
significant model’s predictors.
In tuning the Random Forest, a random search cross-validation was
utilized to optimize the number of trees (N_EST) and the maximum
depth of each tree (M_d). The final model configuration included 200
trees with a maximum depth of 20, ensuring a balance between model
complexity and predictive power. We set the number of features
considered by each tree at two (m = 2), enhancing the diversity of the
model’s decision-making process. The model’s prediction for clothing
insulation, ˆy(X), is given by the average output of these trees:
S. Karatzas et al.

Building and Environment 261 (2024) 111684
7
̂y(X)=
∑200
i=1
Ti(X; Θi, m= 2, Md= 20)
/
200 (30)
A linear regression model was developed to estimate the Mean
Radiant Temperature (MRT) as a function of indoor air temperature. The
effectiveness of the model is indicated by a high Pearson’s correlation
coefficient of 0.889, demonstrating a strong positive correlation, and a
coefficient of determination (R2) of 0.791, suggesting that approxi-
mately 79.1 % of the variance in MRT can be explained by variations in
indoor air temperature.
Further analysis revealed a significant correlation between indoor
and outdoor absolute humidity, with a Pearson correlation coefficient of
0.96. This finding suggests a predictive link between outdoor and indoor
humidity levels. The regression model’s slope coefficient of 0.69 in-
dicates that a unit change in outdoor humidity is associated with a 0.69
unit change in indoor humidity, on average. This relationship enables
the use of outdoor humidity data, such as day-ahead forecasts from
weather APIs, to reliably predict indoor humidity conditions.
The relevance of air velocity in the indoor environment was also
evaluated. However, based on the consistent near-zero values recorded
in the ASHRAE-DB II dataset, air velocity was determined to have a
negligible impact on indoor thermal comfort. Consequently, this vari-
able was excluded from the model, simplifying the analysis without
detracting from the model’s precision in predicting thermal comfort
parameters.
Following the above preliminary steps, the Predicted Mean Vote
(PMV) model, a standard for assessing indoor thermal comfort, was
adapted employing a virtual sensing approach to determine the day-
ahead values for the consumer’s thermal comfort. This sensor is
designed to estimate the PMV based solely on the indoor air tempera-
ture. This approach effectively simplifies the PMV model, enabling it to
operate as a function where indoor air temperature is the primary input
(Eq (31)). The advantage of this method lies in its ability to bypass the
need for extensive physical measurements traditionally required to
assess each factor individually.
PMV 1(Tin)= f(Tin, RH(Tin), MRT(Tin), Iclo(Tin, Tout, S), MET= 1, AV= 0)
(31)
To predict the indoor air temperature matrix required for the opti-
mized load scheduling, the determination of three coefficients a, β and γ
is required, as emerges from an analysis of the building’s thermal
characteristics, while the Coefficient of Performance (CoP) quantifies
the efficacy of the AC unit. The parameter a (Eq (32)) is the complement
to β, representing the non-envelope-related thermal behavior of the
system. The parameter β (Eq (33)) is a dimensionless figure indicative of
the envelope’s conductance to the building’s thermal inertia, and
parameter γ (Eq (34)) provides a measure of the system’s responsiveness
weighted by the CoP.
a= 1 β (32)
β= U× A C × Δt (33)
γ= Δt/C× COP (34)
Where A denotes the surface area of the building’s envelope, U repre-
sents the overall heat transfer coefficient, C is the thermal capacity of the
indoor air, and Δt is the time interval for analysis.
θin t = α× θin t 1+ β× θext t + γ× PAC t (35)
Where θin t is the indoor temperature of the current timestep, θin t 1 is the
indoor temperature of the previous timestep, θext t is the external tem-
perature and PAC t is the power demand of the AC unit for the current
timestep.
3.3. Virtual sensing framework for IAQ index
3.3.1. Dataset collection
The capabilities of recurrent neural networks (RNNs) at capturing
significant temporal patterns on time-series were utilized to predict the
day-ahead IAQ index in residential settings with hourly granularity. A
long short-term memory (LSTM) network was developed, focusing on
specific key air pollutants that have a profound impact on indoor air
quality assessments. The data acquisition phase commenced in February
2023, taking place within a residential setting in Athens, Greece. The
process involved systematic collection of indoor environmental data
using the portable smart device of Atmotube Pro. This device monitors
in real-time the air temperature, relative humidity, volatile organic
compounds (VOCs), and particulate matters (PM1, PM2.5 and PM10).
Two sensors are integrated into the Atmotube Pro to capture pollutants;
the SPS30 sensor captures particle matter PM1, PM2.5, PM10 in μg/m3
with a sampling rate of 1 s and specifications presented in Table 1 and
the Sensirion SGPC3 captures total volatile organic compounds (TVOC)
in ppm with an output range of 0–60 ppm, sampling rate of 2 s and
typical accuracy 15 % of the measured value. Zheng et al. have evalu-
ated this device and have reindorsed the accuracy claims from the
manufacturer [29]. From this phase, a comprehensive dataset of
approximately 40,000 samples collected over a one-month period.
To predict the value of the IAQ index, this study primary focuses on
two pollutants; VOCs and PM2.5. VOCs, measured in in parts per million
(ppm), refer to a large group of organic chemicals that can easily
vaporize at room temperature. High concentration levels can cause
various short and long-term health effects, from eye and respiratory
irritation to more severe effects like damage to the liver, kidney, or
central nervous system. PM2.5, measured in milligrams per cubic meter
(mg/m3), refers to fine particulate matter with a diameter of 2.5 μm or
smaller. These particles are small enough to penetrate deep into the
respiratory tract, potentially causing significant health problems.
Furthermore, air temperature and relative humidity were incorporated
into the dataset, providing the contextual environmental conditions for
each measurement. Data communication between the sensed data from
the physical layer and the storage infrastructure on the application layer
was streamlined through an API endpoint, ensuring integration with the
database. In particular, a custom webhook facilitated the asynchronous
parsing and logging of captured measurements, each tied to specific
timestamps, within a PostgreSQL database schema. Access to this data
flow was regulated via an API key, obtained upon request from Atmo-
tube, to authenticate and authorize the exchange of information.
3.3.2. Categorization of IAQ index values
The target variable for the LSTM network is the IAQ index, which is a
metric derived from the values of indoor air pollutants. In the absence of
a universally accepted framework for this index, the standard from the
United States Environmental Protection Agency (US EPA) has been
adopted. This standard delineates an index that spans in a continuous
and non-dimensional range from 0 to 500, categorizing the IAQ into six
(6) levels: good (0 50), moderate (51–100), unhealthy for sensitive
groups (101–150), unhealthy (151–200), very unhealthy (201–300),
and hazardous (300–500) [30].
This classification leverages the concentrations of principal indoor
air pollutants (VOCs, PM2.5) as the critical metrics in IAQ evaluation
due to their considerable health implications [31]. The pollutant with
Table 1
Measurement range and accuracy of particulate matter (PM).
Atmotube Pro Typical Accuracy Output Range
PM1 [0–100 μg/m3] ±5 μg/m3 + 5 % m.v.] 0–1000 μg/m3
PM2.5 [100–1000 μg/m3] ±10 % m.v.
PM10 [0–100 μg/m3] ±25 μg/m3
[100–1000 μg/m3] ±25 % m.v.
S. Karatzas et al.

Building and Environment 261 (2024) 111684
8
the highest concentration dictates the classification level of IAQ, thus
ensuring the index accurately reflects the most critical air quality
concern. The categorization of VOC levels in relation to the IAQ index is
not strictly defined, with a common approach to be presented in Table 2
[32].
The AQI for PM2.5 is well-established, with its categorization pre-
sented in Table 3 [32].
3.3.3. LSTM description
In the data preprocessing phase, the collected data were assigned
into a Pandas dataframe. Pandas is an open-source Python library, which
is extensively utilized in data analysis due to its robust data structures
and advanced capabilities for handling and manipulating datasets. In
the data preprocessing phase, a series of essential data cleaning tasks
were executed on the dataframe to enhance the quality of forecasts.
These tasks involved the removal of records with missing or null values,
a crucial step to maintain data integrity. Additionally, actions performed
to identify and remove outliers that exhibited significant deviations
from the regular pattern of the time-series. Recognizing that irregular
patterns can hold significance in time-series analysis, a hybrid approach
was employed to detect and mitigate outliers. This approach combined
data truncation and winsorization techniques to handle extreme values
effectively. Specifically, values exceeding the 99th percentile for each
feature were systematically replaced with the value at the 99th
percentile. Furthermore, data points for each pollutant that fell outside
the defined EPA standard’s range were removed, ensuring that the
dataset remained within the bounds of regulatory compliance. In all
features included in the dataset, a normalization process was performed
to standardize the values within the range between 0 and 1, removing
any disparities stemming from varying scales between different air
pollutants. To refine the dataset for the study’s analysis, the data fre-
quency adjusted to 1-min intervals. This resampling frequency was
chosen as an optimal balance to achieve high accuracy while capturing
short-term temporal fluctuations.
The LSTM network deployed in this research is configured to analyze
time-series data with hourly granularity, encompassing a comprehen-
sive range of environmental and operational variables. This model is
trained on a dataset including VOC, PM2.5, indoor air temperature,
indoor relative humidity, outdoor air temperature and occupancy status.
Specifically, occupancy status is a binary variable indicating human
presence in the residence, which is a critical determinant for IAQ index
forecasting. Delayed effects were incorporated using lags for the pol-
lutant’s value at the previous hours, and rolling moving average for the
day used to summarize temporal trends. The LSTM network features an
input layer comprising 64 neurons, a figure derived from empirical
optimization to balance computational load with the model’s capacity
for capturing complex temporal relationships. A second layer of 32
neurons employed to distill the model’s acuity in discerning longer-span
temporal dependencies, which is critical for high-fidelity time-series
forecasting. A densely connected output layer with a single neuron was
employed, utilizing a linear activation function apt for continuous target
prediction. This design is pivotal in transducing the sequential patterns
processed by the LSTM into a discrete forecast of IAQ index values. An
advanced regularization strategy was integrated within the network
architecture, utilizing a dropout mechanism set at a rate of 0.2, to
systematically exclude a fraction of the neurons during each training
pass. This serves as a probabilistic approach to mitigate the risk of
overfitting, enhancing the model’s generalization capability. The
training regimen was orchestrated over a span of 100 epochs, with a
mini-batch size of 32 - a heuristic that offers a compromise between the
noise reduction of gradient descent and the generalization benefits of
stochastic methods. Early stopping, a form of regularization, was
meticulously calibrated with a patience parameter of 10 epochs to
preclude overtraining on the validation set. Optimization during back-
propagation was conducted via the Adam algorithm, leveraging its
adaptive moment estimation to dynamically adjust the learning rate,
commencing at a base rate of 0.001. This optimizer is selected for its
robustness in navigating the complex topology of loss landscapes typical
of deep networks. Upon encountering a plateau in validation loss, the
learning rate is attenuated by an order of magnitude to fine-tune
convergence. For the loss computation, the MSE criterion is adopted,
reflecting the average of the squares of the errors or deviations — pre-
cisely, the difference between the predicted and actual values. The
dataset is apportioned into training (70 %), validation (15 %), and
testing (15 %) subsets, aligning with best practices to validate the
model’s extrapolative strength and ensure that it remains an unbiased
estimator of the underlying IAQ dynamics.
In evaluating the predictive performance of the LSTM network for
day-ahead forecasting, the model exhibits a considerable level of accu-
racy. The Root Mean Squared Error (RMSE) stands at an approximate
76.8, indicating a reasonable degree of predictive precision. The Mean
Absolute Error (MAE) was reported at 45, suggesting that on average,
the model’s forecasts are within this margin of the true values for each
class. The Coefficient of Determination, or R2, is calculated to be 0.78,
denoting that the model accounts for 78 % of the variance in the IAQ
index, a robust level of explanatory power for the variability in air
quality. Additionally, the Mean Absolute Percentage Error (MAPE)
hovers around 15 %, providing further confirmation that the model’s
predictions are generally close to the observed values, with an average
percentage error that supports its utility in practical scenarios.
Incorporating the predictive output for the IAQ index into the opti-
mization problem involves the operational impact of the air purifier
unit. This integration process accounts for the immediate past value of
the IAQ index (lag-1), the predicted IAQ index for the current time slot
along with the operational intensity of the air purifier. Specifically, it
considers the proportion of its nominal power at which the air purifier is
functioning. This approach allows for a more dynamic and responsive
adjustment of the air purifier’s operation, directly based on the recent
air quality measurements and the current efficacy of the unit.
IAQin t = αʹ× IAQin t 1+ bʹ× IAQpred t + γʹ× PAP t (36)
Where IAQin t and IAQin t 1 are the indoor quality indexes of the current and
previous timesteps, IAQpred t is the predicted indoor air quality index, PAP t
is the power demand at current timestep.
4. Results
This section presents a comparative analysis of the daily electricity
Table 2
Categorization of VOC levels.
IAQ Levels Category IAQ Index Values TVOC [ppm]
1 Good 0–50 0–0.065
2 Moderate 51–100 0.066–0.22
3 Unhealthy for Sensitive Groups 101–150 0.23–0.66
4 Unhealthy 151–200 0.67–2.2
5 Very Unhealthy 201–300 2.3–5.5
6 Hazardous 301–500 >5.5
Table 3
Categorization of PM2.5
IAQ
Levels
Category IAQ-Index
Values
PM2.5 [μg/m3]
1 Good 0–50 0.0–12.0
2 Moderate 51–100 12.1–35.4
3 Unhealthy for Sensitive
Groups
101–150 35.5–55.4
4 Unhealthy 151–200 55.5–150.4
5 Very Unhealthy 201–300 150.5–250.4
6 Hazardous 301–500 250.5–500
S. Karatzas et al.

Building and Environment 261 (2024) 111684
9
costs for a particular residency as derived from the proposed optimiza-
tion framework for the day-ahead scheduling against the baseline en-
ergy consumption pattern. This analysis underscores the potential
benefits and cost-effectiveness of employing such a personalized day-
ahead scheduling framework in residential settings. The baseline
pattern emerges from the consumer’s habitual use of time-controllable
and phase-controllable loads without the influence of a structured
scheduling framework, reflecting the most frequent operation instances,
as documented through a comprehensive questionnaire survey con-
ducted over the span of a month. The operation of AC and AP units
exhibits a high degree of probabilistic variability throughout a day.
Accurately documenting consumer’s interactions with these units would
necessitate an intrusive level of detail, requiring the consumer to dili-
gently log every instance of activation along with the associated tem-
perature settings and power levels. In response to this challenge, our
approach involves aggregating the total energy consumption of these
units, as determined by the optimization problem. This aggregated
consumption is then allocated throughout the day, aligned with the
consumer’s occupancy status (see Fig. 3).
The pricing structure applied in this comparative analysis accurately
reflects the electricity tariffs for a typical February day in the Greek
energy sector, as depicted in (Fig. 4) and documented by the European
Network of Transmission System Operators for Electricity (ENTSO-E).
For each hour, the median value of all tariffs recorded in February was
calculated and assigned to the respective hour of the day being analyzed.
A statistical examination of these tariffs reveals an average day-ahead
electricity price of €0.161 per kWh, accompanied by a standard devia-
tion of €0.021, which indicates significant hourly price volatility. The
minimum tariff recorded is €0.133 per kWh, likely indicative of lower
demand periods, while the maximum observed tariff is €0.207 per kWh.
This degree of variation in daily electricity tariffs underscores the
considerable opportunity for consumers to enhance economic efficiency
by adopting their energy consumption patterns in response to tariff
changes.
To establish the operational constraints for the AC and AP units, the
consumer specified the acceptable boundary conditions for thermal
comfort and the IAQ index. Specifically, the moderate level was set as
the upper acceptable boundary for the IAQ index, and for thermal
comfort, the range was determined to be between neutral and slightly
cool. A penalty coefficient of 0.2 was applied to the objective function
for both units, facilitating a balance between the cost of electricity and
comfort levels. Furthermore, the vectors with the values for the day-
ahead thermal comfort and indoor IAQ were forecasted to control the
operation of AC and AP units, respectively, as described in Section 3. The
day-ahead vector for thermal comfort was generated using the outdoor
air temperature obtained from an open-access weather API endpoint.
This temperature was then translated into an expected indoor air tem-
perature by incorporating specific building thermal characteristics and
considering the effects of the previous operational cycle of the AC unit,
as described in (Eq (32)) - (Eq (34)). The coefficients α, β, and γ, essential
for the thermal modeling within the residential context (Eq (35)), were
ascertained through a review of field studies in the literature pertaining
to residential energy consumption. C. Antunes et al. [33] incorporated
building thermal characteristics of the residence under study into
equations resulting in the following values; α equaled 0.857, indicating
the proportionality factor for heat gains from external sources; β was set
at 0.143, representing the heat gains from internal sources; and γ was
calculated to be 2.78, reflecting the rate of heat loss to the environment.
Throughout a one-month duration, the Atmotube Pro device systemat-
ically recorded levels of VOCs, PM2.5, indoor air temperature, and
relative humidity. These measurements were collated to establish the
training dataset for the LSTM network, which is intended to produce the
day-ahead IAQ index vector. Occupancy status was also manually
recorded and factored into the training dataset to enhance the predictive
accuracy of the LSTM network.
Furthermore, the consumer requested to define the EST and LET for
each time-controllable and phase-controllable load. The time-
controllable loads were scheduled as follows: the dishwasher (DW)
was to operate between 01:00 and 06:00, the washing machine (WM)
from 02:00 to 09:00, and the tumble dryer (TD) was set between 02:00
and 07:00. The scheduling for the phase-shiftable loads was established
with specific operational windows: the electric vehicle (EV) charging
Fig. 3. Linear regression for the temperature variable.
S. Karatzas et al.

Building and Environment 261 (2024) 111684
10
was to be completed between 01:00 and 08:00, while the electric water
heater (EWH) was to finish its operation cycle between 01:00 and 18:00.
In the typical scheduling for electric appliances, presented in (Fig. 5),
energy consumption peaks tend to be more dispersed throughout the
day, with a pronounced increase in activity during the evening hours
(18:00–23:00). In contrast, during the nocturnal hours from 01:00 to
07:00, there is an absence of appliance activation, thus missing the
potential benefits of lower energy tariffs typically available during these
off-peak hours. Moreover, a substantial gap in appliance use is observed
between 09:00 and 16:00, a period coinciding with the absence of oc-
cupants from the home, which also presents a missed opportunity to
capitalize on lower tariff rates.
The optimal scheduling for electric appliances, as presented in
(Fig. 6), demonstrates a strategic shift in load activation, with notable
peaks in energy usage during times when the electricity price is low (e.
g., 01:00 to 06:00). The overall pattern of appliance usage has been
shifted to take advantage of lower energy prices during off-peak hours.
The total energy cost per time slot is significantly reduced compared to
the typical schedule, especially during high-price periods, suggesting
that the optimization framework has successfully identified and
exploited the times when it is most economical to operate these
appliances.
From the thermal comfort standpoint, the optimally scheduled
operation of the AC unit extends for more hours relative to the baseline
scenario, a calculated approach to fulfill the consumer’s specified
thermal comfort constraints on the optimization problem. The data
suggests that consumers who are amenable to a broader range of tem-
peratures could potentially decrease the usage hours of the AC unit,
thereby realizing additional reductions in energy costs. A clear view of
the AC unit’s operation in relation to the indoor and outdoor tempera-
tures is presented in (Fig. 7). It is noteworthy that the AC unit remains
operational during traditional sleeping hours and engages preemptively
even when the residence is empty. This function is strategic, ensuring
that the residence achieves the desired thermal comfort by the evening
and circumvents the necessity for high-power usage during periods of
peak energy tariffs.
The operation of the air purifier (AP) unit is enhanced in the opti-
mized schedule, adopting a data-informed approach that aligns its
activation with actual periods of detected indoor air pollution, as pre-
sented in (Fig. 8). Unlike the baseline scenario, where the AP unit is
triggered solely during times of human presence—owing to the con-
sumer’s lack of real-time awareness of indoor air quality when away or
unfamiliar with off-peak tariffs—the optimization framework intelli-
gently manages the AP’s operation. It maintains healthy Indoor Air
Quality (IAQ) levels throughout the day, ensuring that the air quality is
not compromised, while also avoiding significant energy expenditure.
This demonstrates the framework’s ability to provide a healthy living
environment in a cost-effective manner.
The analysis revealed that the daily electricity costs incurred through
optimized scheduling amounted to €6.095, while the costs associated
Fig. 4. Day-ahead electricity price with hourly resolution.
Fig. 5. Typical load activation schedule.
S. Karatzas et al.

Building and Environment 261 (2024) 111684
11
with the baseline pattern were €7.46. This delineates a notable cost
reduction of approximately 18.30 % when employing the proposed
optimization scheduling strategy. This strategy respects the consumer’s
preferences on thermal comfort, indoor air quality, and timelines. Pro-
jecting these savings across an entire year, the estimated total electricity
costs for optimized scheduling approximates €2224.68 annually,
compared to €2722.90 for the baseline scenario. This annual projection
emphasizes the considerable financial advantages that can be realized
by adopting such an optimization framework.
Fig. 6. Optimal load activation schedule.
Fig. 7. AC unit operation in relation to the indoor and outdoor temperatures.
Fig. 8. AP unit operation in relation to the AQI index.
S. Karatzas et al.

Building and Environment 261 (2024) 111684
12
5. Conclusions and future work
This study introduces a consumer-centric ILP framework that opti-
mizes daily electricity costs in residential settings. This framework
balances the financial goal of minimizing electricity costs with the
imperative of minimal disruption to the consumer’s daily routine and
lifestyle, aligning with the preferred operational time-window for each
controllable electric load. Crucially, it ensures the sustenance within the
desired comfort levels, meticulously quantified by the metrics of thermal
comfort and the IAQ index. A key novelty of this framework is the
methodical incorporation of the IAQ index as an explicit constraint
within the objective function of the optimization problem. This pivotal
integration catalyzes the efficient operation of the AP unit, adeptly
maintaining healthy indoor air conditions without forfeiting energy ef-
ficiency. Further enhancing the framework’s capability is the scheduling
of thermostatic loads, achieved by embedding Fanger’s thermal comfort
model directly into the optimization algorithm. This approach tran-
scends controls over thermostatic loads driven by temperature or
simplified thermal comfort models, strongly aligning with the con-
sumer’s need for thermally acceptable conditions within indoor envi-
ronments. Both time-controllable and phase-shiftable loads were
examined under the proposed optimization framework, providing a
comprehensive and realistic assessment of a real-world scenario. The
comparative analysis indicates a substantial reduction in daily elec-
tricity costs, achieving a 18.30 % decrease compared to a baseline
scenario.
This study acknowledges certain limitations that could be addressed
in future work:
• The current optimization problem does not take into account the
integration of owned Renewable Energy Sources (RES) assets, such
as solar rooftop panels, which could significantly influence both the
solution of the optimization problem and the overall electricity costs.
Future iterations of the model could benefit from including owned
RES in the optimization algorithm, which would likely alter the en-
ergy consumption patterns and cost calculations, potentially leading
to greater cost savings and promoting the use of sustainable energy
sources.
• The role of EVs in this study is limited to their charging requirements.
However, EVs have the potential to function as energy storage sys-
tems, effectively acting as batteries that can store energy when
electricity costs are low and supply energy back to the home or grid
when costs are high. Incorporating this bidirectional energy flow into
the optimization problem could provide additional flexibility and
efficiency in energy usage, reduce costs further, and assist in
balancing the grid during peak demand times. Integrating this
functionality would require a more complex optimization algorithm
and careful consideration of the EV’s battery health and the resi-
dency’s transportation needs.
• The LSTM network utilized for forecasting IAQ currently considers
only VOCs and PM2.5 as pollutants. A more advanced LSTM model
could be developed to include a wider array of indoor air pollutants,
such as PM1, PM10, and CO2. Additionally, an enhanced model
could integrate data on household activities and the operation of
appliances, providing insights into the correlation between these
variables and pollutant levels. This would enable a more precise
prediction of IAQ, leading to improved scheduling decisions and
potentially healthier indoor environments.
• This study does not address the potential conflicts arising from the
diverse preferences of household members, each with unique life-
style routines. The existing settings may result in interruptions or
inconveniences for some individuals. Future research should
consider implementing a unified inconvenience factor to quantify
disruptions to daily routines, attributable to the scheduling of
household loads within the proposed ILP framework. Additionally,
the development of more adaptable thresholds for desired indoor air
quality and thermal comfort could be explored to better accommo-
date the full spectrum of household preferences.
Funding
This research was funded by the UKRI [Grant Ref: EP/×024075/1]
under the project entitled “TwinBAS: Digital Twins enabled Building
Automation System for comfortable, healthy and energy efficient
buildings”.
CRediT authorship contribution statement
Stylianos Karatzas: Writing – review & editing, Writing – original
draft, Visualization, Validation, Supervision, Resources, Methodology,
Funding acquisition, Formal analysis, Data curation, Conceptualization.
Jorge Merino: Writing – review & editing, Validation, Conceptualiza-
tion. Alena Puchkova: Writing – review & editing, Validation, Formal
analysis. Christos Mountzouris: Visualization, Software, Data curation.
Grigoris Protopsaltis: Validation, Formal analysis, Data curation. John
Gialelis: Writing – review & editing, Supervision. Ajith Kumar Parli-
kad: Supervision, Conceptualization.
Declaration of competing interest
The authors declare that they have no known competing financial
interests or personal relationships that could have appeared to influence
the work reported in this paper.
Data availability
Data will be made available on request.
References
[1] United Nations, Paris agreement, United Nations Framework Convention on
Climate Change (2015). Paris: United Nations.
[2] Eurostat, Energy consumption in households, Retrieved from Eurostat, https://ec.
europa.eu/eurostat/statistics-explained/index.php?title=Energy_consumption_i
n_households, 2024.
[3] J. William, B.C. Fisk, Association of residential energy efficiency retrofits with
indoor environmental quality, comfort, and health: a review of empirical data,
Build. Environ. (2020).
[4] E. Sarker, Progress on the demand side management in smart grid and optimization
approaches, Int. J. Energy Res. (2020).
[5] I. Antonopoulos, Artificial intelligence and machine learning approaches to energy
demand-side response: a systematic review, Renew. Sustain. Energy Rev. (2020).
[6] P.W. Tien, Machine Learning and Deep Learning Methods for Enhancing Building
Energy Efficiency and Indoor Environmental Quality, 2022.
[7] B.S. Patnam, Demand response in consumer-Centric electricity market:
mathematical models and optimization problems, Elec. Power Syst. Res. (2021).
[8] L. Silva-Rodriguez, Short term wholesale electricity market designs: a review of
identified challenges and promising solutions, Renew. Sustain. Energy Rev. (2022).
[9] S. Sharda, Demand side management through load shifting in IoT based HEMS:
overview, challenges and opportunities, Sustain. Cities Soc. (2021).
[10] M. Hussain, Demand side management techniques for home, Energy Management
Systems for Smart Cities. Sustainability (2021).
[11] D. Martin, Virtual sensors, Business & Information Systems Engineering (2021).
[12] R.G. Petr Kadlec, Review of adaptation mechanisms for data-driven soft sensors,
Comput. Chem. Eng. (2011) 1–24.
[13] Z.G. Qingqiang Sun, A survey on deep learning for data-driven soft sensors, IEEE
Trans. Ind. Inf. (2021).
[14] K.N. Qureshi, Trust aware energy management system for smart homes appliances,
Comput. Electr. Eng. 97 (2022).
[15] C.A. Hassan, Smart grid energy optimization and scheduling appliances priority for
residential buildings through meta-heuristic hybrid approaches, Energies 15 (5)
(2022) 1752.
[16] X. Lu, Optimal scheduling of household appliances for smart home energy
management considering demand response, Nat. Hazards (2017).
[17] Z. Yahia, Optimal load scheduling of household appliances considering consumer
preferences: an experimental analysis, Energy (2018).
[18] P. Charoen, User-centric consumption scheduling and fair billing mechanism in
demand-side management, Energies (2019).
[19] M. Awais, An efficient genetic algorithm based demand side management scheme
for smart grid, International Conference on Network-Based Information Systems
(NBIS) (2015).
S. Karatzas et al.

Building and Environment 261 (2024) 111684
13
[20] D. Setlhaolo, Optimal scheduling of household appliances for demand response,
Elec. Power Syst. Res. 116 (2014) 24–28.
[21] T.B. Sepideh Saravani Ghayour, Optimal Scheduling of Electrical and Thermal
Resources and Appliances in a Smart Home under Uncertainty, 2022.
[22] S.J. Elham Shirazi, Cost reduction and peak shaving through domestic load shifting
and DERs, Energy (2017).
[23] A. Agnetis, Load scheduling for household energy consumption optimization, IEEE
Trans. Smart Grid (2013).
[24] A. Anvari-Moghaddam, Optimal smart home energy management considering
energy saving and a comfortable lifestyle, IEEE Trans. Smart Grid (2020).
[25] S. Wang, Coordinated residential energy resource scheduling with human thermal
comfort modelling and renewable uncertainties, IET Gener., Transm. Distrib.
(2019).
[26] Y. Lin, A study on the impact of household occupants’ behavior on energy
consumption using an integrated computer model, Frontiers in Built Environment
1 (2015) 16.
[27] S.K. Karatzas, Business processes and comfort demand for energy flexibility
analysis in buildings, Energies 13 (24) (2020) 6561.
[28] C. Mountzouris, Non-interventional precise TC assessment for enhancing consumer
energy flexibility, in: IEEE 21st International Conference on Industrial Informatics
(INDIN), 2023.
[29] Zheng, Laboratory evaluation of low-cost air quality monitors and single sensors
for monitoring typical indoor emission events in Dutch daycare centers, Environ.
Int. (2022).
[30] M. Mannan, Indoor Air Quality in Buildings: A Comprehensive Review on the
Factors Influencing Air Pollution in Residential and Commercial Structure,
Environmental Science and Engineering, 2021.
[31] F.M. Jesús, Methodology for the study of the envelope airtightness of residential
buildings in Spain: a case study, Energies (2018).
[32] V.V. Tran, Indoor air pollution, related human diseases, and recent trends in the
control and improvement of indoor air quality, Int. J. Environ. Res. Publ. Health
(2020).
[33] V.R. Carlos Henggeler Antunes, A Discussion of Mixed Integer Linear Programming
Models of Thermostatic Loads in Demand Response, 2019.
S. Karatzas et al.
