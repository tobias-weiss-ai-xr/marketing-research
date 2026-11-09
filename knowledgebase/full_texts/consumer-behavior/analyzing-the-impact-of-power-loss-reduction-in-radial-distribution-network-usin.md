---
title: Analyzing the impact of power loss reduction in radial distribution network using diverse distributed
  generators by utilizing ZIP load models
url: https://doi.org/10.1038/s41598-026-55639-x
category: consumer-behavior
subcategory: case-study
date: 2026-06
venue: Scientific Reports
authors:
- Gopisetti Manikanta
- Priyanshu Kumar
- Ashish Mani
source: openalex-oa
pdf_url: https://www.nature.com/articles/s41598-026-55639-x_reference.pdf
pages: 33
chars: 90226
fetched_at: '2026-11-08T18:31:49+00:00'
kb_version: 1
---

# Analyzing the impact of power loss reduction in radial distribution network using diverse distributed generators by utilizing ZIP load models

ARTICLE IN PRESS
Article in Press
Analyzing the impact of power loss reduction
in radial distribution network using diverse
distributed generators by utilizing ZIP load
models
Scientific Reports
Received: 23 January 2026
Accepted: 26 May 2026
Cite this article as: Manikanta G.,
Kumar P ., Mani A. et al. Analyzing the
impact of power loss reduction in radial
distribution network using diverse
distributed generators by utilizing ZIP
load models. Sci Rep (2026). https://doi.
org/10.1038/s41598-026-55639-x
Gopisetti Manikanta, Priyanshu Kumar, Ashish Mani, Sujit Kumar, Anubhav Kumar
Pandey, Nandini K. Krishnamurthy & Pulakraj Aryan
We are providing an unedited version of this manuscript to give early access to its
findings. Before final publication, the manuscript will undergo further editing. Please
note there may be errors present which affect the content, and all legal disclaimers
apply.
If this paper is publishing under a Transparent Peer Review model then Peer
Review reports will publish with the final article.
https://doi.org/10.1038/s41598-026-55639-x
© The Author(s) 2026. Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing,
adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source,
provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included
in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative
Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission
directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

Analyzing the Impact of Power Loss Reduction in
Radial Distribution Network using Diverse
Distributed Generators by utilizing ZIP Load
Models
Gopisetti Manikanta1, Priyanshu Kumar1, Ashish Mani3, Sujit Kumar4, Anubhav
Kumar Pandey1,2[0000-0002-0935-3262], Nandini K. Krishnamurthy5[0000-0002-0246-1834],
Pulakraj Aryan6, *
gopisetti-eee@dayanandasagar.edu ; priyanshu-eee@dayanandasagar.edu ; amani@amity.edu ;
k_sujit@blr.amrita.edu ; anubhav-eee@dayanandasagar.edu ; nandini.kk@nitte.edu.in ;
pulakraj.aryan@jaipur.manipal.edu
1Department of Electrical and Electronics Engineering, Dayananda Sagar College of Engineering,
Bengaluru, 560078, Karnataka, India.
2Centre for E-Mobility and Sustainability, Dayananda Sagar College of Engineering, Bengaluru,
Karnataka - 560078, India.
3Amity Innovation & Design Centre, IIC, Amity University, Noida, UP, India.
4Department of Electrical and Electronics Engineering, Amrita School of Engineering, Amrita Vishwa
Vidyapeetham, Bengaluru, Karnataka, India.
5Department of Electrical and Electronics Engineering, NMAM Institute of Technology, Nitte
(Deemed to be University),
Nitte, Karnataka, India.
6Department of Electrical Engineering, School of Engineering, Manipal University Jaipur, Jaipur-
303007, Rajasthan, India.
*Corresponding author: Pulakraj Aryan pulakraj.aryan@jaipur.manipal.edu
Abstract: Distributed generators (DGs) are recent emerging technologies which are executed in
distribution system (DS) to reduce power losses (PLs). However, optimal location and sizing of DG
(OLSDG) remain a challenging combinatorial optimization problem due to its large search space and
load uncertainties. Numerous scholars attempted to effectively handle this optimization problem
characterized by a fixed load model (constant power (CP)), which fails to represent the real-world
consumer behavior. This assumption causes a research gap, as practical DS is mainly dependent on
characteristics of voltage magnitude and ZIP load models better represents this behavior. To overcome
these challenges, this work reports a novel metaheuristic Algorithm inspired by quantum principles
(Multipartite Adaptive Quantum inspired Evolutionary Algorithm (MAQiEA)) to discover the OLSDG.
The originality of the work stands out by using realistic load model (ZIP load model), utilizing
multipartite adaptive variation operator and analyzing the influence of diverse DGs with CP and ZIP
load models. This study investigates two different scenarios to analyze the effect of various DGs on CP
and ZIP load models. In first case, a study was conducted to analyze the influence of diverse DGs with
CP load which are tabulated in the statistical analysis results that demonstrate the efficacy and
soundness of MAQiEA. For performance assessment, proposed algorithm is compared with some well-
known other metaheuristic algorithms. Tabulated results demonstrate that, MAQiEA outperforms other
metaheuristic algorithms in PL reduction. Finally, the approach is suitable in terms of overall
operational framework which is an important investigation in mitigating the PLs.
Keywords: Active & Reactive Power injection; Distributed Generator; Hybrid AC/DC systems;
Optimization Algorithm; Power loss; Renewable Energies
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

NOMENCLATURE
Ip Percentage active current
Iq Percentage reactive current
k1 Total number of DGs for active power injection
k2 Total number of DGs for reactive power injection
P(m) Real power at mth bus
PDG(m) Location of DG corresponding to active power injection at the mth bus
PMax DG Maximum permissible DG capacity for active power injection
PMin DG Minimum permissible DG capacity for active power injection
PLoad Total active power load
PLoss Total losses (active)
P0(m) Initial active power load   at mth bus
Pp Percentage active power
Pq Reactive power in percentage
PFDG DG’s Power fact
Psub Total substation power
Q(m) mth bus reactive power
QDG(m) Location of DG for reactive power injection at  mth bus
QMax DG Maximum allowable size of DG for reactive power injection
QMin DG Minimum allowable size of DG for reactive power injection
Q0(m) Initial reactive power load   at mth bus
R(m) Resistance of the line at mth bus
V(m) Voltage at mth bus
Vi(m) Voltage at mth bus
Vmax(m) Maximum allowable voltage mth bus
Vmin(m) Minimum allowable voltage mth bus
V0(m) Nominal voltage at mth bus
VSI(m
+ 1) Voltage Stability index at m + 1 bus
X(m) Reactance of the line at mth bus
Zp Percentage resistance
Zq Percentage reactance
ABBREVIATION
ALO Ant Lion Optimization Algorithm
AOA Arithmetic Optimization Algorithm
AQiEA Adaptive Quantum inspired Evolutionary Algorithm
CI Constant current
CP Constant power
CWO Carpet Weaver Optimization
CZ Constant impedance
DG Distributed Generator
DS Distribution system
HOA Hippopotamus Optimization Algorithm
MALO Modified Ant Lion Optimization
MAQiEA Multipartite Adaptive Quantum inspired Evolutionary Algorithm
MGWO Modified Grey Wolf Optimization
MRFOA Manta Ray Foraging Optimization Algorithm
OLSDG Optimal Location and Sizing of Distributed Generator
PL Power Loss
PO Puma optimizer
PSO Particle Swarm Optimization
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

QiEA Quantum inspired Evolutionary Algorithm
T&Ds Transmission & Distribution systems
TYPE-I
DG Provides active power injection only
TYPE-II
DG Provides reactive power injection only
TYPE-III
DG Injects active and absorbs reactive power
TYPE-IV
DG Provides both active and reactive power injection
WDG With DG
WHO Wild Horse Optimization Algorithm
WOA Whale Optimization Algorithm
WoDG Without DG
ZIP Load Combination of CP, CI and CZ loads
1. INTRODUCTION
Central power station is used for generating the electric power and sometimes called as
generating station or generating plant also referred as power house. Most of the electric
power generating stations or generating plants burns fossil fuels such as coal-based
generation, natural gas, oil followed by nuclear power to generate electricity. The power
generating stations or central power plants are sited far from the consumers and the power
is being transmitted and distributed through transmission and distribution system (T&Ds).
In general, Distribution systems (DSs) accounts major power losses (PLs) in comparison with
transmission vertical due to high R/X proportion. In DS, reduction of PL is considered as one
of the important problems to be solved in power system network [1]. Several approaches are
employed to reduce the PL i.e., sizing and sitting of capacitors, increasing the size of
conductors, changing the transformer taps followed by location and sizing of distributed
generators (OLSDG) etc.
In present scenario, integration of DG into DSs is considered as one of the alternative
solutions for PL minimization problem. DGs are usually categorized as a small-scale source
of power generation which are positioned closer to the consumer, typically their capacity
ranges from few kW to 100MW [2]. It is considered as an important power generation source,
where electric power delivery is difficult to the consumers. However, DG usage has been
significantly increased due to environmentally friendly technologies & ease of
implementation and in some cases, it is used as power back up storage devices for supplying
the power under peak load conditions. Some of the DG technologies which are commonly
available are modularly structured biomass and wind energy systems, small scale
hydropower and solar photovoltaic systems [3-5]. Therefore, their impacts on DSs operation,
stability and control vary depending on their locations and sizes. DG is strategically located
and operated in the DSs to minimize PL, improvise reliability, load-ability by maintaining
voltage profile to eliminate regular system upgrades.
Several optimization approaches and methodologies have been presented in the literature to
investigate DG allocation in DSs to minimize the PL [6]. Several numerical-based [6,7],
analytical [8-9] and metaheuristic methods [10-17] are used for placing the DG along with
its size, in some methods sizing of DG is alone considered to reduce the search space.
Gradient search [6] & Thevenin’s impedance-based stability index [7] are some methods
which are used for DG allocation. Even though analytical based methods are simple and
convenient to implement but a demerit is a single DG with a relatively large size is placed in
the whole system to minimize the PL [8]. In some analytical approaches multiple DG
allocation is also considered to reduce the PL, these approaches are applied on small bus
systems [9]. Computational burden for large test bus systems is very high which is usually
considered as the main disadvantage.
Metaheuristics based advanced methods are population-based techniques which comes
with ease of execution and computational robustness. In particular, to mitigate the PL in DSs
with DG integration, advanced metaheuristics are utilized as potential solution tactics.
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

Hippopotamus Optimization Algorithm (HOA) [10], Modified Grey Wolf Optimization
(MGWO) algorithm [11], Carpet Weaver Optimization (CWO) [12], Ant Lion Optimization
Algorithm (ALO) [13], Puma optimizer (PO) technique [14], Wild Horse Optimization
Algorithm (WHO) [15], Manta Ray Foraging Optimization Algorithm (MRFOA) [16], Modified
Ant Lion Optimization (MALO) algorithm [17], Arithmetic Optimization Algorithm (AOA) [18]
are few methods which are employed to reduce the PLs. All the methods which are explained
in the literature are used with a primary objective to minimize these losses by OLSDG while
in some methods only sizing of DG is considered to lessen the search space. Also, some
approach only considers either real power injection or reactive power injection followed by
OLSDGs in the system [19, 20].
Based on power delivering capability in relation to their terminal characteristics
different type of DGs are available for the study, e.g. DG with a solitary real power injection
are Type-I DG, DG with a solitary reactive power injection are Type-II DG, DG that involves
the injection of active power and the absorption of reactive power are Type-III DG and DG
which injects both powers are Type-IV DG. But, most of the techniques represented in earlier
research studies have used only Type-I and Type II DG with unity (active power) and zero
power factors (reactive power). Some researchers have implemented diverse types of DGs
to deal with these PLs. Hien and Mithulananthan [21] used Particle Swarm Optimization
(PSO) with different DGs, single DG and two DGs are independently implemented, multiple
DG installations highly mitigate the losses as compared to a single DG unit with a high active
power injection capability. Reddy et al. [22] studied the impact of different DGs with Whale
Optimization Algorithm (WOA) to mitigate the PLs. Similar to above, this study is also
implemented a sole DG with high power injection into the system which induces very little
drop in PL in comparison with multiple DG installations.
Jagtap and Khatod [23] proposed a new method on loss allocation problem with
different DGs. Different load models are utilized to dela with PL with single DG. It is observed
from the reported work that some of the authors solved this important optimization problem
with single DG. Multiple DG implementations are not considered by the researchers which
induces minimum PL reduction. Therefore, an investigation is carried out to reduce the PLs
by taking multiple DGs into consideration. It is also as observed from the reviewed literature
that different types of DGs are used to mitigate PLs, however independent implementation
is only considered. In general, any type of DG can be used in DSs to lower the PLs, depending
on the demand, in some cases all type of DGs are also considered in the system with respect
to their operating constraint. In this study, in addition to independent implementation of
different types of DG, a mixed range of DGs viz., combination of all type of DGs is also
considered to cut short the PLs.
The load at DS is not constant and varies according to season. Given to the preceding
literature, the majority of the authors handled the OLSDG problem using a load model of
constant power (CP). The CP is a fixed load model that does not vary over time and is voltage
independent; nonetheless, the load at DS is mostly determined by the magnitude of the
supply voltage. According to the available literature, certain researchers have addressed this
critical problem using voltage dependent load models [24-28]. Load models are classified
into three types: (CP) load, constant impedance (CZ) load, and constant current (CC) load.
All of the mentioned load’s combinations form a more representative static load model, often
referred as ZIP load model [29–32].
It has been observed from above literature that majority of the work proposed by
researchers have examined the impact of DG with independent implementation of DG with
either active power or reactive power injection into the system, in general based on terminal
characteristics four different types of DGs are considered, very few researchers have
investigated the impact of these different DGs on DS. In addition, the load DS is mainly
dependent on voltage magnitude but several studies examined the optimization problem
(OLSDG) on CP, this creates a research gap, in this study, an investigation has been
performed to study the impact of different DGs on realistic load model (ZIP load model). Two
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

different cases are considered to study the impact of different DGs, in first case, an
investigation has been performed to study the impact of diverse DGs on PL reduction and in
other case, a realistic load model i.e, ZIP load model is considered with six different scenarios
and an investigation has been performed on these scenarios to study the impact on different
DGs. The prime focus of this study is to mitigate power consumption through the adoption of
DG on various ZIP load scenarios.
ZIP load model is mainly used because it reflects more realistic illustration of practical
DS by taking voltage dependent nature of loads. In contrast to the CP load which is
independent of voltage variations, the ZIP model represents the combined effect of CP, CZ
and CC. This enables accurate analysis of system behavior, in DG allocation studies, where
variation in voltage significantly influence the loss and performance of DS.
The OLSDG is plays a crucial role in lowering PL. To handle this significant optimization
problem, which contains both continuous and discrete variables and necessitates a lengthy
search, a Multipartite Adaptive Quantum Inspired Evolutionary Algorithm (MAQiEA)
technique is employed to determine the OLSDG. MAQiEA is an improved version of an
Adaptive Quantum Inspired Evolutionary Algorithm (AQiEA). AQiEA is a sophisticated
evolutionary intelligence technique used to solve a variety of engineering optimization
challenges. Recently, AQiEA [33] has been employed in addressing a wide range of
engineering optimization tasks, including DG allocation problem [34-36], Network
Reconfiguration [37-38], ceramic grinding [39], and the integrated approach involving both
DG and capacitor implementation [40-41]. In MAQiEA, two Q-bits are entangled and
expressed within a quantum system as a superposition of fundamental states, thereby
enhancing the population diversity. Various rotation algorithms are employed to adaptively
drive the population convergence toward the global optimums. Unlike other metaheuristic
algorithms, MAQiEA does not require any parameter tuning operators to prevent premature
convergence or tune parameters to improve convergence rate.
This article address, PL minimization by considering OLSDG on realistic ZIP load model. In
addition, diverse types of DGs are taken in consideration to study the impact with ZIP load
model. Furthermore, MAQiEA which is relatively powerful evolutionary intelligence method
which is inspired from QiEA is used to determine the OLSDG. The major contributions of this
work are summarized below:
●DG allocation (DG location and sizing) plays a main role in PL reduction of DS.
In this study, a novel MAQiEA is proposed to solve this important optimization
problem.
●Unlike previous works, majority of researchers have solved this problem (DG
location and sizing) with CP load model viz., doesn’t alter with time, but the load
at DS mainly depends on the magnitude of voltage, this study considers a realistic
load model using ZIP characteristics which improves the practical accuracy and
relevance.
●A study was undertaken to analyze the impact of diverse DGs based on their
terminal characteristics.
●Two case studies are considered to investigate the impact of different DG under
two distinct load models i.e., CP load model (first case) and ZIP load model
(second case).
●Two IEEE benchmark test bus viz., 33 bus radial DS and 69 bus radial DS are
considered for simulation and validation.
●The efficacy of MAQiEA is validated by comparing it with other metaheuristic
algorithms for both cases, the proposed method shows a notable improvement in
enhancing percentage PL reduction.
The remaining paper is structured in the following way: a realistic load model is
considered in the subsequent section to analyze the effect of different DGs. The mathematical
formulation corresponding to various DG configurations is discussed in Section II, based on
their terminal characteristics and realistic ZIP load models considering all constraints. An
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

improved AQiEA i.e., MAQiEA is employed for solving this important problem, which is
conferred in ‘Section III’. ‘Section IV’ demonstrates the outcomes obtained with different DG
on CP load model followed by the implementation of different DG on realistic ZIP based load
models. Finally, ‘Section V’ consists of concluding remarks and a glimpse of future directions.
2. FORMULATION OF PROBLEM
One benefit of placing a DG in DSs is lessening the PL and enhancement in voltage profile,
which is anticipated as the core objective in present approach. The total PLs produced by
the system is determined by summing the individual branch PL in all line sections.
  F1 = Ploss = {∑Nb m=1( P(m)2 +Q(m)2 V(m)2 ) * R(m)}      (1)
F = Min(F1) (2)
However, integration of DG will increase the voltage profile levels in DSs and enhance
voltage security. Therefore, voltage stability index (VSI) is used to enhance the overall
improvement in voltage profile in the system with and without DG.
{VSI(m + 1)} =
(∑Nb m=1[|V(m)|4 - 4(P(m + 1) * X(m) - Q(m + 1) * R(m))2 - 4(P(m + 1) * R(m) - Q(m + 1) * X(m))|V(m)|2])
    (3)
The stability of each bus in the DSs is identified by VSI, if VSI of each bus exceeds the
minimum limit, the related stability of that bus is better.
A direct load flow method [42] is explored for finding the individual PL at each bus,
total PL, voltage profile improvement and VSI at each bus. The objective function is governed
by the following design constraints:
Operational constraints of DG and capacitor:
 Pmin DG (m) ≤ PDG(m) ≤ Pmax DG (m) (4)
 Qmin DG (m) ≤ QDG(m) ≤ Qmax DG (m) (5)
The total DG power injection will be maintained in acceptable limits. PDG(m) and QDG
(m) are injected active and reactive powers.
Power injection:
  ∑k i=1 PDg,i + PSubstation = PLoad + PLosses (6)
  ∑k1 m=1 PDG(m) + ∑k2 m=1 QDG(m) + Psub ≤ Ploss + Pload (7)
The total power inserted by diverse DGs with substation power must be equivalent or
less than its cumulative load demand and system losses. Where Psub, Ploss, Pload represents
substation power, total PLs followed by systems load demand.
Voltage limit:
The voltage generated at each respective bus in the system is maintained within the
restrictions as per (8).
 Vmin(m) ≤ V(m) ≤ Vmax(m) (8)
2.1 DIFFERENT TYPES OF DGS
DGs are sectionalized into different categories according to their individual terminal
characteristics, generation ratings and technologies. In present work DGs are divided into
four categories depending on their active and reactive power injection and consumption
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

capabilities [21-23]. The real power injected by DG and reactive power injected by capacitors
at a particular bus is in the systems is discussed as follows.
Type I: DG only injects active power into the system with unity power factor (UPF).
In Type I, DG is modelled as active power generation source. Photovoltaic, fuel cells, micro
turbine are some of the examples for this type. The load at mth bus with DG unit is modelled
as:
 P(m) = P(m) - PDG(m) (9)
Type II: DG injects only reactive power into the system with zero power factor (ZPF),
which provides reactive power support. In this case, DG is modeled as reactive power
generation source. Capacitors, synchronous compensators are some of the examples for this
type. The load at mth bus with DG unit is modeled as
 Q(m) = Q(m) - QDG(m) (10)
Type III: DG injects active power and consumes reactive power into the system with
leading power factor between 0 to 1. In this case, DG is modeled as variable reactive power
generation source. Induction generator used in wind farms is one of the examples for this
type. The overall reactive power consumed at mth bus is given as follows:
  QDG(m) = PDG(m) * tan ((PFDG(m)) )  (11)
The load at mth bus with DG unit is modeled as
 P(m) +jQ(m) = (P(m) + jQ(m)) - {PDG(m) - jQDG(m)} (12)
  P(m) +jQ(m) = (P(m) - PDG(m)) +j{Q(m) + QDG(m)} (13)
The real power injection and reactive power consumption at mth bus is given as follows:
 P(m) = P(m) - PDG(m) (14)
 Q(m) = Q(m) + QDG(m) (15)
Type IV: DG injects both real and reactive power into the system with lagging power
factor between 0 to 1. Synchronous generator, co-generation are some of the examples for
this type. The reactive power modeling is same as Type III, the load at mth bus with DG unit
is modeled as:
 P(m) +jQ(m) = (P(m) + jQ(m)) - {PDG(m) +jQDG(m)}} (16)
The injection of both real power and reactive power at mth bus is presented in (17, 18):
 P(m) = P(m) - PDG(m) (17)
 Q(m) = Q(m) - QDG(m) (18)
The real and reactive power injected/consumed by DG at m th bus in a DS is expressed as
follows: PDG +jQDG =
{
PDG                     Type I             unity power factor
 QDG                  Type II             zero power factor
PDG - jQDG       Type III       leading power factor
PDG + jQDG      Type IV       lagging power factor
 (19)
2.2 ZIP LOAD MODELS:
The load composition in DSs has progressively evolved during the last few years. Over the
last few years, household appliances have changed. To illustrate the power–voltage
relationship in this research, a practical load model is utilized to derive a polynomial equation
for voltage magnitude. The goal of this work is to investigate the effect of various DGs on
ZIP load models. ZIP denotes CZ load, CI load, and CP load, respectively. The ZIP coefficients
model's real and reactive powers are expressed as:
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

 P(m) = P0(m) * [Zp[ Vi Vo] 2 + Ip [ Vi Vo] + Pp] (20)
 Q(m) = Q0(m) * [Zq[ Vi Vo] 2 + Iq [ Vi Vo] + Pq] (21)
Where Zp + Ip + Pp = 1 & Zq + Iq + Pq = 1
In conventional approach for power flow studies, CP load model is considered by taking
ZIP coefficients as zero. These ZIP coefficients for the load model are listed in Table I [29].
Table.  IZIP load models for various appliances
Zp Ip Pp Zq Iq Pq
Laptop Charger 0.25 -0.48 1.23 0.14 0.32 0.54
Tungsten Light 0.45 0.66 -0.11 0.21 0.11 0.68
CFL Bulb -0.63 1.66 -0.03 -0.34 1.4 -0.06
Elevator 2.36 -4.15 2.79 11.7 -19.5 8.81
Resistance
Heater 1.19 -0.26 0.07 0.59 0.65 -0.24
Battery Charger 3.51 -3.94 1.43 5.8 -7.3 2.46
3. MULTIPARTITE ADAPTIVE QUANTUM INSPIRED EVOLUTIONARY
ALGORITHM
Optimization is the process of attaining the best possible result under given conditions.
Gradient-based approaches are utilized to solve some engineering optimization challenges.
In some circumstances, gradient-based approaches have failed to address the intricacies of
engineering design problems. Evolutionary algorithms (EAs) are population-based
optimization algorithms that operate on Darwinian principles. Individuals within the
population compete for survival, with the fittest moving on to the following generation. They
are popular because of their simplicity of implementation and are used to solve difficult and
complex optimization challenges. The selection operator normally directs evolution
according to Darwinian principles. The solution for the following iteration is obtained by
recombining the current iteration's results using the crossover operator. The key limitations
of EA are early convergence, sensitivity to parameter selection, stagnation, and slow
convergence. Many efforts have been undertaken to overcome these limits. QiEA is created
by incorporating some quantum computing ideas and concepts, such as Q-bit representation,
entanglement, measurement, and superposition of states, within the framework of EA [43].
Individual representation, population dynamics, and function assessment are all features
shared by other EAs. However, EA suffers from delayed convergence, stagnation in
parameter selection, and premature convergence. QiEA is utilized to overcome these
restrictions and maintain an appropriate balance between the exploration phase and the
exploitation phase. QiEA improves diversity by using a probabilistic model of the search
space and a genotype known as a Q-bit, which is the smallest unit of information [44]. The
quantum state vector | ∝ ￿ represents the weighted sum of a quantum particle for two
potential positions A1 and A2 equals X|A1￿+Y|A2￿, where X|A1￿ and Y|A2￿ are two state
vectors. Q-bit may be represented in binary state of “ A1” or in state “ A2”, or in any
superposition of two.
 |α￿ = X|A1￿ +Y|A2￿ (22)
Where |X|2 and |Y|2 are probability amplitudes of the Q-bit in state |A1￿ and |A2￿.
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

 |X|2 + |Y|2 = 1 (23)
The Q-gate functions as a variation operator to guide individuals in the population to
better solutions. MAQiEA is utilized to determine the placement and sizing of DG to curtail
PLs. The suggested solution makes use of two Q-bit representations, as well as superposition
and entanglement principles. The proposed approach employs two Q-bits: the first Q-bit
stores the fitness values of the solution vectors, while the second Q-bit dynamically adjusts
the rank assigned to the solution vector's objective function [38]. Entanglement is defined as
when two or more Q-bits are entangled with each other, any quantum operation realized on
one of the Q-bits affects the state of the other Q-bits. However, two Q-bits are entangled if
any operation on one of them affects the state of the other Q-bit. A measurement operator
generates a solution string from a Q-bit string as seen in Table II [38-39].
Table.  IICalculated operators on Q bit string
j 1 2 3 4 5 … Np
X2 j 0.79 0.65 0.17 0.56 0.41 … 0.36
Y2 j 0.21 0.35 0.83 0.44 0.59 … 0.64
Nrj 0.82 0.25 0.24 0.12 0.07 … 0.49
Qmj 0.21 0.65 0.83 0.56 0.41 … 0.64
Two Q-bits are said to be entangled when a quantum operation performed on one qubit
instantaneously influences the state of the other.
|￿2k(t)￿=f1(|￿1k(t)￿) (24)
A crossover mechanism based on the adaptive quantum principles, acting as a variation
operator, is discussed in (25):
|￿1k(t + 1)￿=f2(|￿2k(t)￿, |￿2l(t)￿,|￿1k(t)￿,|￿1l(t)￿) (25)
The variation operator focusses the search on a better solution by employing three
rotation strategies (R-I, R-II, and R-III) [39].
Quantum registers are used to hold Q-bits. The fittest and poorest vectors in the second
Q-bit are assigned the values 1 and 0, respectively. The other solution vectors in the second
Q-bit are assigned scaled rankings between 1 and 0. If 'P' denotes the overall population size
and 'X' the number of variables. Figure 1 depicts the quantum register used to reduce PLs
associated with DG integration.
Fig.  1.Chromosome representation of MAQiEA
MAQiEA pseudo code is as follows:
t ← 0
a. Initialize (Quantum_Register (t))
While (!criteria_termination)
{
b. Qm = Operation_Measurement_operator (Quantum_Register (t))
c. f(x)= Compute_ Fitness (Qm(t))
d. QR2(t)= Rank_ Scale (f(x))
e. QR1c= Different_Rotations (Quantum_Register (t), (QR2(t))
f. Selection_ Tourn_ (Quantum_Register (t), f(x))
t ← t+1
}
M11 …… M1X N11 …… N1X
Location of DG with X variables Size of DG with X variables
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

3.1 Description:
a) Assign some initial inputs to quantum register such as No of iterations, Variables and total
Population.
b) A new measured string (Q m) is produced after performing the measurement, lies in the
range of (0 and 1). (Nr), the length of the Qm and Nr are has same length as Q-bit strings.
c) Quantum register (Q m) is mainly implemented to compute the fitness, in terms of PL
reduction in DSs with integration of DG.
d) The main operation of second Q-bit QR 2 dynamically adjusts the rank assigned to the
solution vector's objective function.
e) Different rotation stratagems are utilized for registering the best possible solution.
f) Tournament based selection has been implemented between individuals in the population.
The selection follows based on the Darwinian principle i.e., the appropriate one will only
sustain to the next generation.
4. IEEE BENCHMARK TEST BUS SYSTEMS:
The proposed approach is validated on two benchmark test bus systems, incorporating
independent deployment of multiple DG types. The data for line and load are adapted from
[37]. The initial data required for benchmark test bus systems are listed in Table III. The
single line diagram for both IEEE benchmark test bus systems are shown in Fig 2 & Fig 3.
Many studies have implemented OLSDG optimization problem with either one or three DGs
on IEEE 33 and 69 bus system, in this study three DGs are considered. Increasing the number
of DGs beyond three to either four or five may in turn increase the technical cost and system
complexity. Based on the power injection the penetration level of DG can be increased which
may increase the PLs in the system. The penetration level of DG should be maintained within
the acceptable limits, the penetration level is selected to ensure stability, prevent over load
issues and avoid reverse power flow.
Table.  IIIInitial data for 33 and 69-bus system.
PARTICULAR VALUE (33 bus system) VALUE (69 bus system)
Aggregate Real Power Demand
(MW) 3.715 3.81
Aggregate Reactive Power Demand
(MVAr) 2.3 2.694
Line Voltage (kV) 12.66 12.66
Base (MVA) 100 100
Buses 1 to 33 1 to 69
Sectionalizing switches 1 to 32 1 to 68
Tie line switches 33 to 37 69 to 73
Maximum Allowable Size of DG 1MW & 1MVAr 1MW & 1MVAr
The basic assumptions which are considered before implementing DG into the test bus
systems. All buses in network (except substation node) are considered as candidate location
for DG allocation. In this study, multiple DGs are used to inject the power into the system,
the total load acted on both test bus systems is below 4MW, if the power injected by DG goes
above the load it induces more PLs due to increased penetration level, so the allowable size
of DG is 1MW and 1MVAr with voltages of 0.90p.u & 1.1p.u and tolerance ±10%. Repetitions
of bus numbers for optimal location of DG are not allowed. Results obtained with MAQiEA
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

are also correlated with different methods such as ALO, AOA, MRFO and WHO. The total
number of iteration and population size for all algorithms are 1000 and 50.
Fig.  2.Single line diagram depicting IEEE-33 bus system
5. RESULTS & DISCUSSIONS
Case-A:
The total PLs produced by first test bus system without DG placement, is 202.62 kW and
135.23 kVAr with minimum voltage 0.9132p.u and minimum VSI 0.6944p.u at locations 18
and 19 buses. The total PLs without DG placement in DSs by second test bus system are
224.95 kW and 102.12 kVAr with minimum VSI 0.6825p.u and minimum voltage 0.9092p.u
at locations 65 and 64 buses.
Fig.  3.Single line diagram depicting IEEE-69 bus system
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

5.1 For 33-bus system:
Table IV demonstrates the PLs induced in the first test bus system with diverse DGs. The PLs
are reduced after implementing or injecting power through DG. In this study, different DGs
are considered based on their terminal characteristics. Five diverse cases are discussed to
reduce the loss by injecting power through DGs. In case of Type-I DG, as it introduces active
power in the network only, the PLs are reduced. The incurred PL after injecting power
through Type-I DG for proposed algorithm is 71.69 kW, with optimal location 13, 30 and 24.
However, the losses incurred in the system with other algorithms are 72.14 kW for WHO,
73.32 kW for MRFO, 74.55 kW for AOA and 77.61 kW for ALO. The OLSDG for the above-
mentioned algorithms are different. As compared with other algorithms MAQiEA is injecting
minimal power into the system and in turn produces highest percentage PL reduction.
As Table IV indicates that the losses incurred in the system for Type-II DG is high as
compared with Type-I DG, as Type-II DG injects only reactive power into the system. The
tabulated results clearly indicate that the PLs induced in the system after injecting power
through Type-II DG with proposed algorithm is 132.25 kW. Before implementing DG for this
test bus system, the active PL is 202.62 kW but after injecting power through DG results in
a smaller reduction in losses. The optimal location of DG with MAQiEA is 13, 23 and 29. It is
observed that Type I and Type II DGs injects different powers into the system one injects
active power and other injects reactive power into the system, the optimal location of DGs
for Type-I and Type-II has been changed. The PLs sustained in the system with other methods
such as WHO, MRFO, AOA and ALO are 133.51 kW, 134.82 kW, 136.39 kW and 137.98 kW
respectively.
Table.  IVComparative analysis of power losses with different DGs for 33-bus system
DG Method Location (Bus Number) & Size of DG Ploss ( kW) Qloss ( kVAr) Min Voltage  (p.u.) Min VSI (p.u.)
24 33 13ALO 1 1 1 77.6155 55.8387 0.9742 0.9
10 24 32AOA 1 0.9734 0.9738 74.5584 51.7676 0.9663 0.871
29 24 12MRFO 1 1 1 73.3286 50.246 0.966 0.871
30 12 24WHO 1 0.9010 1 72.1517 49.7124 0.9665 0.8731
13 30 24
Type –I
(MW)
MAQiE
A 0.8125 1 1 71.6982 49.4323 0.9668 0.8736
26 32 25ALO 0.8328 0.7289 0.4608 137.981 93.7074 0.9295 0.7455
23 29 10AOA 0.4301 1 0.4176 135.994 90.6106 0.9347 0.7625
30 24 11MRFO 0.7749 0.8174 0.4351 134.851 90.3027 0.9341 0.7603
24 30 9WHO 0.5682 0.8282 0.6369 133.514 89.2456 0.9357 0.7657
14 24 30
Type –II
(MVAr)
MAQiE
A 0.3548 0.5841 1 132.251 88.4937 0.9384 0.7746
23 10 31ALO 0.9441 0.7107 0.1752 156.919 105.3346 0.9315 0.7530
33 8 24AOA 0.2816 0.9301 0.5267 155.563 104.3698 0.9304 0.7484
32 23 13MRFO 0.3203 1 0.4692 154.853 104.1252 0.9333 0.7588
13 26 24
Type –III
(MW &
MVAr)
WHO 0.3721 1 0.4178 153.569 103.4856 0.9331 0.7580
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

In general, Type-III DG injects active power and absorbs the reactive power. The PLs
obtained in the system after injecting power through Type-III DG with MAQiEA is 152.32 kW.
After implementing Type-III DG, it has been observed that Type-III DG suffers from higher
energy losses in the system as linked with Type-I and Type-II DGs. The PLs incurred in the
system with remaining algorithms are 153.66 kW, 154.67 kW, 155.55 kW, 156.07 kW and
the OLSDG are different.
Table.  VComparative analysis of power losses with Mixed DGs for 33-bus system
Algorit
hm
Type
I
Type
II
Type
III
Type
IV
Ploss
( kW)
Qloss
( kVAr)
Min
Voltage
(p.u.)
Min VSI
(p.u.)
24 31 30 13
ALO 1 1 1 0.650 2 30.3883 22.7262 0.9830 0.9315
31 29 24 12
AOA 1 1 0.719 6 0.910 9 25.5495 19.2922 0.9885 0.9489
24 31 30 8
MRFO 1 1 0.879 3 0.996 9 27.9663 20.8551 0.9733 0.8962
23 32 31 12
WHO 1 1 0.647 2 1 26.6400 21.1456 0.9835 0.9350
31 29 23 11
Mixed
(Combinati
on of all
DGs)
(MW &
MVAr)
MAQiE
A 1 1 0.642 0.935 24.3171 18.2971 0.9854 0.9373
a) Voltage profile of Type-I DG with different
algorithms
b) Voltage profile of Type-II DG with different
algorithms
6 14 24MAQiE
A 0.867 0.3803 0.6116 152.321 102.5451 0.9314 0.7525
10 31 24ALO 0.8483 1 0.6105 26.8205 19.4105 0.9757 0.9052
11 25 31AOA 0.9564 1 0.9408 23.3669 17.5448 0.9826 0.9312
30 12 25MRFO 1 0.8342 0.9438 22.1100 16.6481 0.9802 0.9222
12 30 25WHO 0.9653 1 1 21.5237 16.1932 0.9856 0.9437
24 12 30
Type –IV
(MW &
MVAr)
MAQiE
A 1 0.9643 1 20.4226 15.3349 0.9856 0.9436
0.965
0.970
0.975
0.980
0.985
0.990
0.995
1.000
1.005
1 5 9 13 17 21 25 29 33
ALO AOA
MRFO WHO
Voltage (p.u)
Bus Number
0.925
0.935
0.945
0.955
0.965
0.975
0.985
0.995
1.005
1 5 9 13 17 21 25 29 33
ALO AOA
MRFO WHO
MAQiEA
Voltage (p.u)
Bus Number
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

c) Voltage profile of Type-III DG with different
algorithms
d) Voltage profile of Type-IV DG with different
algorithms
e) Voltage profile of Mixed DG with different
algorithms f) Voltage profile of different DGs with MAQiEA
Fig.  4.Voltage profile with different algorithms for 33-bus system
Type-IV DG injects both real and reactive power into the electrical system. The numerical
results demonstrate that, the losses incurred in the system after injecting power through
Type-IV DG with MAQiEA is 20.42 kW. Type-IV DG injects both active and reactive power
into the system, the losses induced in the system are very less as compared with Type I, Type
II and Type III DGs. It is clear from the analysis, as compared with other types of DGs such
as Type-I, Type-II and Type-III, Type-IV has maximum reduction in PL. The induced PLs after
injecting power through Type-IV DG with WHO, MRFO, AOA and ALO are 21.59 kW, 22.11
kW,23.36 kW and 26.11 kW.
0.925
0.935
0.945
0.955
0.965
0.975
0.985
0.995
1.005
1 5 9 13 17 21 25 29 33
ALO AOA MRFO
WHO MAQiEA
Voltage (p.u)
Bus Number
0.975
0.98
0.985
0.99
0.995
1 5 9 13 17 21 25 29 33
ALO
AOA
MRFO
WHO
MAQiEA
Voltage (p.u)
Bus Number
0.97
0.975
0.98
0.985
0.99
0.995
1
1.005
1.01
1 5 9 13 17 21 25 29 33
ALO AOA
MRFO WHO
Voltage (p.u)
Bus Number
0.92
0.93
0.94
0.95
0.96
0.97
0.98
0.99
1
1.01
1 5 9 13 17 21 25 29 33
Type-1 Type-2 Type-3
Type-4 Mixed
Voltage (p.u)
Bus Number
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

a) VSI of Type-I DG with different algorithms b) VSI of Type-II DG with different algorithms
c) VSI of Type-III DG with different algorithms d) VSI of Type-IV DG with different algorithms
e) VSI of Mixed DG with different algorithms f) VSI of different DGs with MAQiEA
Fig.  5.VSI with different algorithms for 33-bus system
In normal operating conditions, there is possibility that all types of DG are used. In this study,
in addition to above a class of mixed DG is considered which inject only active power, only
reactive power, injects active and absorbs reactive, injects both active and reactive powers
into the system. In mixed DG model, combinations of all four types of DGs are considered.
Table V shows the comparative analysis of power losses with Mixed DGs for first test bus
system. The PLs induced after injecting power through combination of all four types of DGs
with MAQiEA is 24.31 kW. In case of mixed DG model, the optimal location for Type-I DG is
31, Type-II DG is 29, Type-III DG is 23, Type-IV DG is 11. Similarly, from tabulated results
the PLs incurred in the system for other algorithms are 26.64 kW for WHO, 27.96 kW for
MRFO, 25.54 kW for AOA and 30.38 kW for ALO.
0.85
0.87
0.89
0.91
0.93
0.95
0.97
0.99
1.01
1 5 9 13 17 21 25 29 33
ALO AOA
MRFO WHO
MAQiEA
Voltage (p.u)
Bus Number
0.74
0.79
0.84
0.89
0.94
0.99
1.04
1 5 9 13 17 21 25 29 33
ALO AOA
MRFO WHO
MAQiEA
Voltage (p.u)
Bus Number
0.74
0.79
0.84
0.89
0.94
0.99
1.04
1 5 9 13 17 21 25 29 33
ALO AOA
MRFO WHO
MAQiEA
Voltage (p.u)
Bus Number
0.90
0.92
0.94
0.96
0.98
1.00
1.02
1 5 9 13 17 21 25 29 33
ALO AOA
MRFO WHO
MAQiEA
Voltage (p.u)
Bus Number
0.89
0.91
0.93
0.95
0.97
0.99
1.01
1.03
1 5 9 13 17 21 25 29 33
ALO AOA MRFO
WHO MAQiEA
Voltage (p.u)
Bus Number
0.72
0.77
0.82
0.87
0.92
0.97
1.02
1.07
1 5 9 13 17 21 25 29 33
Type-1 Type-2 Type-3
Voltage (p.u)
Bus Number
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

a) Convergence Graph of Type-I DG with
different algorithms
b) Convergence Graph of Type-II DG with
different algorithms
c) Convergence Graph of Type-III DG with
different algorithms
d) Convergence Graph of Type-IV DG with
different algorithms
e) Convergence Graph of Mixed DG with
different algorithms
f) Convergence Graph of different DGs with
MAQiEA
Fig.  6.Convergence Graph with different algorithms for 33-bus system
Implementation of DGs in DS not only helps in minimizing the losses but also improve the
voltage profile. It has been witnessed from tabulated results that improvement of the voltage
profile and VSI after injecting power through DG in the DS. Fig. 4 and Fig. 5 show the overall
enhancement in voltage profile and VSI with different types of DGs. Fig 6 shows the
convergence graph for different DGs with MAQiEA, ALO, AOA, WHOA and MRFO. The
70
75
80
85
90
95
100
20
80
140
200
260
320
380
440
500
560
620
680
740
800
860
920
980
MAQiEA
WHO
MRFO
AOA
ALO
Power Loss ( KW)
Iterations
130
135
140
145
150
155
20
80
140
200
260
320
380
440
500
560
620
680
740
800
860
920
980
MAQiEA
WHO
MRFO
AOA
ALO
Power loss ( KW)
Iterations
151
153
155
157
159
161
20
80
140
200
260
320
380
440
500
560
620
680
740
800
860
920
980
MAQiEA
WHO
MRFO
AOA
ALO
Power loss ( KW)
Iterations
20
22
24
26
28
30
32
34
20
80
140
200
260
320
380
440
500
560
620
680
740
800
860
920
980
MAQiEA
WHO
MRFO
AOA
ALO
Power loss ( KW)
Iterations
23
25
27
29
31
33
35
37
20
80
140
200
260
320
380
440
500
560
620
680
740
800
860
920
980
MAQiEA
WHO
MRFO
AOA
ALO
Power loss ( kW)
Iterations
15
35
55
75
95
115
135
155
175
20
80
140
200
260
320
380
440
500
560
620
680
740
800
860
920
980
DG1 DG2 DG3
DG4 Mixed
Power loss ( kW)
Iteration
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

comparative analysis of PLs with different DGs implementing on different algorithms are
shown in Fig 7.
Fig.  7.Comparative analysis with different algorithms power loss for 33-bus system
5.2 For 69-bus system:
The PL incurred in the system before injecting power with DG is 224.95 kW. Table VI shows
the cumulative analysis of PLs for different DGs with MAQiEA, AOA, ALO, WHO and RFO. It
is evident form tabulated results, that the losses are reduced by injecting power with DG at
a specific bus. It is aware that, Type-I DG normally injects real power into the system, by
injecting power through Type-I DG the losses are abridged from 224.95 kW to 72.69 kW for
MAQiEA, 74.73 kW for WHO, 74.53 kW for MRFO, 76.53 kW for AOA and 83.66 kW for ALO.
It is noted that MAQiEA has maximum reduction in power when correlated with other
algorithms as listed. The optimal site of DG with MAQiEA is 61, 18 and 60 with allowable
capacity 1 MW, 560 kW, and 899 kW respectively.
Table.  VIPower loss comparison under different DG configurations for the 69-bus test system.
DG Method Location (Bus Number) & Size of DG Ploss (kW) Qloss ( kVAr) Min Voltage (p.u.) Min VSI (p.u.)
60 61 57ALO 0.7456 1 0.4199 83.6674 40.4738 0.9701 0.8854
61 62 68AOA 0.7427 0.8366 0.5149 76.5309 37.8643 0.9723 0.8928
61 62 66MRFO 0.9815 0.7523 0.8267 74.5311 36.664 0.9777 0.9139
62 61 69WHO 0.8615 0.9164 0.6586 74.7322 36.8535 0.9789 0.9184
61 18 60
Type –I
(MW)
MAQiE
A 1 0.5604 0.8994 72.9387 36.4036 0.9802 0.9223
66 68 63ALO 0.6648 0.2418 1 150.6494 69.7549 0.9295 0.7451
66 63 60AOA 0.6068 0.5979 0.7196 148.9605 69.1268 0.9318 0.7529
62 66 64MRFO 0.5995 0.6401 0.5544 149.0523 69.1856 0.9322 0.7498
64 61 66WHO 0.2356 1 0.5833 147.2085 68.3021 0.9320 0.7534
62 13 61
Type –II
(MVAr)
MAQiE
A 0.64 0.41 0.6 146.9360 68.3864 0.9310 0.7504
67 69 61ALO 0.272 0.2744 1 166.0637 76.5540 0.9420 0.7866
26 69 61
Type –III
(MW &
MVAr) AOA 0.1467 0.2786 1 165.1790 76.2841 0.9414 0.7847
77.6155
137.9813
156.9194
26.8205
30.3883
74.5584
135.9949
155.5637
23.3669
25.5495
73.3286
134.8517
154.8531
22.1100
27.9663
72.1517
133.5145
153.5692
21.5237
26.6400
71.6982
132.2519 152.3211
20.4226 24.3171
0
50
100
150
200
Type-1 Type-2 Type-3 Type-4 Mixed
ALO AOA MRFO WHO MAQiEA
Power loss ( kW)
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

61 68 69MRFO 0.8965 0.1933 0.2313 166.9442 76.9274 0.9385 0.7748
69 27 61WHO 0.4442 0.1095 1 166.1047 76.5707 0.9421 0.7867
17 61 52MAQiE
A 0.2566 0.9338 0.3565 164.9668 76.1997 0.9403 0.78099
62 64 69ALO 1 0.6831 0.9283 20.3842 13.0311 0.9887 0.9556
62 61 69AOA 0.723 1 0.4096 19.7901 13.3295 0.9787 0.9176
63 60 17MRFO 0.9573 0.9264 0.4833 15.2366 11.8201 0.9927 0.9704
21 61 63WHO 0.457 0.9982 1 13.9717 10.9735 0.9930 0.9716
18 62 61
Type –IV
(MW &
MVAr)
MAQiE
A 0.5162 0.8631 1 12.5558 10.4544 0.9932 0.9724
Type-II DG normally injects reactive power into the system and the losses in the system after
injecting power through Type-II DG is 150.64 kW for ALO, 148.66 kW for AOA, 149.05 kW
for MRFO, 147.21 kW for WHO and 146.93 kW for MAQiEA. The optimal placement and
allowable capacity of Type-II DG with MAQiEA is 62, 13, 61 and 640 kVAr, 410 kVAr and 600
kVAr, respectively.
Table.  VIIPower loss comparison under Mixed DG configurations for the 69-bus test system.
Algorit
hm
Type
I
Type
II
Type
III
Type
IV
Ploss
( kW)
Qloss
( kVAr)
Min
Voltage
(p.u.)
Min VSI
(p.u.)
66 60 61 62
ALO 0.876
3 1
0.744
3
0.746
7
23.4799 14.9596 0.9804 0.9237
68 60 61 62
AOA 0.676
2 1 1 1
25.0191 15.5207 0.9839 0.9372
69 62 60 61
MRFO 0.861
6 1
0.405
8 1
20.4371 13.1494 0.9845 0.9393
61 62 60 17
WHO
1 1 0.488
0.621
7
18.7068 13.2457 0.9811 0.9257
69 61 62 63
Mixed
(Combinati
on of all
DGs)
(MW &
MVAr)
MAQiE
A 0.695 6 1 0.628 7 1 17.2400 12.0361 0.9827 0.9326
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

a) Voltage profile of Type-I DG with different
algorithms
b) Voltage profile of Type-II DG with different
algorithms
c) Voltage profile of Type-III DG with different
algorithms
d) Voltage profile of Type-IV DG with different
algorithms
e) Voltage profile of Mixed DG with different
algorithms
f) Voltage profile of different DG with MAQiEA
Fig.  8.Voltage profile with different algorithms for 69-bus system
The tabulated results indicate that, Type-III DG which injects active power and absorbs the
reactive power is having high PL as compared with other DGs. The cumulative losses induced
in the system after implementing Type-III DG with MAQiEA is 164.58 kW with optimal
0.965
0.970
0.975
0.980
0.985
0.990
0.995
1.000
1.005
1 10 19 28 37 46 55 64
ALO AOA
MRFO WHO
MAQiEA
Voltage (p.u)
Bus Number
0.925
0.935
0.945
0.955
0.965
0.975
0.985
0.995
1.005
1 10 19 28 37 46 55 64
ALO AOA MRFO
WHO MAQiEA
Voltage (p.u)
Bus Number
0.925
0.935
0.945
0.955
0.965
0.975
0.985
0.995
1.005
1 10 19 28 37 46 55 64
ALO AOA
MRFO WHO
MAQiEA
Voltage (p.u)
Bus Number
0.975
0.98
0.985
0.99
0.995
1 10 19 28 37 46 55 64
ALO
AOA
MRFO
WHO
MAQiEA
Voltage (p.u)
Bus Number
0.978
0.983
0.988
0.993
0.998
1.003
1 10 19 28 37 46 55 64
ALO
AOA
MRFO
WHO
MAQiEA
Voltage (p.u)
Bus Number
0.92
0.93
0.94
0.95
0.96
0.97
0.98
0.99
1
1.01
1 10 19 28 37 46 55 64
Type-1 Type-2 Type-3
Type-4 Mixed
Voltage (p.u)
Bus Number
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

location and capacity 17, 61, 52 and 256 kW, 933 kW and 356 kW. The maximum PL reduction
is realized by implementing Type-IV DG. Type-IV DG normally injects both active and reactive
power in the system. After implementing Type-IV DG, PLs induced in the system with
MAQiEA is 12.55 kW. Similarly, in case of mixed DG, the losses induced in the system with
MAQiEA is 17.24 kW. Table VII shows the power loss comparison under Mixed DG
configurations for the 69-bus test system.
a)VSI of Type-I DG with different algorithms b)VSI of Type-II DG with different algorithms
c)VSI of Type-III DG with different algorithms d)VSI of Type-IV DG with different algorithms
e)VSI of Mixed DG with different algorithms f)VSI of different DG with MAQiEA
Fig.  9.VSI for 69-bus system with different algorithms
After implementing DG in DS, voltage profile and VSI are observed to be improved. Fig. 8
and Fig. 9 show the overall enhancement in voltage profile and VSI with different types of
DGs. Fig 10 shows the convergence graph for different DGs with MAQiEA, ALO, AOA, WHOA
0.85
0.87
0.89
0.91
0.93
0.95
0.97
0.99
1.01
1 10 19 28 37 46 55 64
ALO
AOA
MRFO
WHO
MAQiEA
Voltage (p.u)
Bus Number
0.74
0.79
0.84
0.89
0.94
0.99
1.04
1 10 19 28 37 46 55 64
ALO AOA
MRFO WHO
MAQiEA
Voltage (p.u)
Bus Number
0.74
0.79
0.84
0.89
0.94
0.99
1.04
1 10 19 28 37 46 55 64
ALO AOA MRFO
WHO MAQiEA
Voltage (p.u)
Bus Number
0.90
0.92
0.94
0.96
0.98
1.00
1.02
1.04
1 10 19 28 37 46 55 64
ALO AOA
MRFO WHO
MAQiEA
Voltage (p.u)
Bus Number
0.89
0.91
0.93
0.95
0.97
0.99
1.01
1.03
1 10 19 28 37 46 55 64
ALO AOA
MRFO WHO
MAQiEA
Voltage (p.u)
Bus Number
0.72
0.77
0.82
0.87
0.92
0.97
1.02
1 7 13 19 25 31 37 43 49 55 61 67
Type-1 Type-2 Type-3
Type-4 Mixed
Voltage (p.u)
Bus Number
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

and MRFO. The comparative analysis of PLs with different DGs implementing on different
algorithms are depicted in Fig 11. Fig 12 shows the comparative analysis of both test bus
system for MAQiEA with different DGs.
a) Convergence Graph of Type-I DG with
different algorithms
b) Convergence Graph of Type-II DG with
different algorithms
c) Convergence Graph of Type-III DG with
different algorithms
d) Convergence Graph of Type-IV DG with
different algorithms
e) Convergence Graph of Mixed DG with
different algorithms
f) Convergence Graph of different DG with
MAQiEA
Fig.  10.Convergence Graph with different algorithms for 69-bus system
70
75
80
85
90
95
100
105
20
80
140
200
260
320
380
440
500
560
620
680
740
800
860
920
980
MAQiEA WHO
MRFO AOA
ALO
Power loss ( kW)
Iterations
145
147
149
151
153
155
157
159
161
20
80
140
200
260
320
380
440
500
560
620
680
740
800
860
920
980
MAQiEA
WHO
MRFO
AOA
ALO
Power loss ( KW)
Iterations
164
165
166
167
168
169
170
20
80
140
200
260
320
380
440
500
560
620
680
740
800
860
920
980
MAQiEA
WHO
MRFO
AOA
ALO
Power loss ( KW)
Iterations
10
12
14
16
18
20
22
24
20
80
140
200
260
320
380
440
500
560
620
680
740
800
860
920
980
MAQiEA
WHO
MRFO
AOA
ALO
Power loss ( KW)
Iterations
15
20
25
30
35
20
80
140
200
260
320
380
440
500
560
620
680
740
800
860
920
980
MAQiEA WHO
MRFO AOA
ALO
Power loss ( kW)
Iterations
0
20
40
60
80
100
120
140
160
20
80
140
200
260
320
380
440
500
560
620
680
740
800
860
920
980
DG1 DG2 DG3
DG4 Mixed
Power loss ( kW)
Iteration
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

After implementing DG into the Ds, improvement in voltage (voltage profile and VSI) has
been observed. The improvement in voltage at every bus for Type-II and Type-III DG has very
minor change with different algorithms. However, the improvement in voltage for Type-I,
Type-IV and Mixed DGs are varying unevenly for both test bus systems.
Fig.  11.Performance comparison of different optimization algorithms applied to the 69-bus test system
Fig.  12.Comparative analysis with proposed algorithm for both test bus systems
Case-B:
In actual DSs, majority of loads used by consumers are reliant primarily on magnitude of
supply voltage. In this study, a realistic model viz., ZIP based load model is used to test of
different DGs in DSs. Six different ZIP load models are used with diverse DGs following which
six different scenarios are created with these load models. In Scenario-I, laptop charger load
model is used which is defined as load model L1. The cumulative load acted on the system is
L1, for each bus in the system, the load is assumed to be L1. Likewise, the other load models
such as Tungsten light, CFL bulb, Elevator, Resistance Heater, Battery Charger are defined
as load model L2, L3, L4, L5 & L6. The cumulative load acted on the system for varied
scenarios are listed as follows.
Scenario I. Laptop Charger (L1)
Scenario II. Tungsten Light (L2)
Scenario III. CFL Bulb (L3)
Scenario IV. Elevator (L4)
Scenario V. Resistance Heater (L5)
Scenario VI. Battery Charger (L6)
Table.  VIIIReal and reactive power losses with different DGs on ZIP based load models for 33-bus system
83.6674
150.6494
166.0637
20.3842
23.4799
76.5309
148.9605
165.1790
19.7901
25.0191
74.5311
149.0523
166.9442
15.2366
20.4371
74.7322
147.2085
166.1047
13.9717
18.7068
72.9387
146.9360 164.9668
12.5558 17.2400
0
50
100
150
200
Type-1 Type-2 Type-3 Type-4 MixedALO AOA MRFO WHO MAQiEA
Power loss ( kW)
224.9500
202.6200
72.9387
71.6982
146.9360
132.2519
164.9668
152.3211
12.5558
20.4226
0
50
100
150
200
250
69-Bus System 33-Bus System
Base Case
Type-1
Type-2
Type-3
Type-4
Power loss ( kW)
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

Ploss(kW) Qloss(kVAr) Min Volt(p.u) Min VSI (p.u) % ReductionLoa
d Loc Size (MW) WoDG WDG WoDG WDG WoD G WD G WoD G WD G %Ploss %Qloss
DG-I
L1 2 3 2 9 1 2 1.00 00 1.00 00 0.80 69 197.41 81 67.666 5 131.66 16 46.67 14 0.91 41 0.96 79 0.69 74 0.87 77 65.72 43 64.55 20
L2 1 2 2 3 2 9 0.70 15 1.00 00 0.94 48 171.14 15 66.466 1 113.87 13 45.68 72 0.92 12 0.97 00 0.71 92 0.88 53 61.16 31 59.87 82
L3 2 9 1 2 2 3 1.00 00 0.76 92 1.00 00 187.69 28 65.726 0 125.06 58 45.32 63 0.91 66 0.96 94 0.70 49 0.88 31 64.98 22 63.75 80
L4 1 3 2 9 2 3 0.74 10 1.00 00 1.00 00 169.46 43 49.145 4 112.78 82 34.14 60 0.92 06 0.97 36 0.71 74 0.89 85 70.99 95 69.72 56
L5 2 3 2 9 1 2 1.00 00 0.90 00 0.66 71 151.20 45 55.536 1 100.40 17 38.22 01 0.92 61 0.97 28 0.73 47 0.89 56 63.27 08 61.93 28
L6 2 3 1 2 2 9 1.00 00 0.61 49 0.83 01 118.82 49 36.532 9 78.617 0 25.32 98 0.93 49 0.97 85 0.76 30 0.91 67 69.25 48 67.78 07
DG-II
L1 1 2 2 3 2 9 0.38 33 0.60 99 0.99 89 197.41 81 131.54 18 131.66 16 87.99 49 0.91 41 0.93 86 0.69 74 0.77 53 33.36 89 33.16 59
L2 2 9 2 3 1 3 1.00 00 0.55 97 0.33 51 171.14 15 106.43 77 113.87 13 71.01 80 0.92 12 0.94 54 0.71 92 0.79 77 37.80 72 37.63 31
L3 2 3 1 3 2 9 0.58 76 0.32 16 1.00 00 187.69 28 123.91 50 125.06 58 82.84 50 0.91 66 0.94 04 0.70 49 0.78 11 33.97 99 33.75 88
L4 2 3 2 9 1 1 0.43 70 0.77 78 0.34 45 169.46 43 124.06 55 112.78 82 82.76 56 0.92 06 0.93 83 0.71 74 0.77 43 26.78 96 26.61 86
L5 1 1 2 3 2 9 0.39 86 0.53 36 0.84 89 151.20 45 98.441 0 100.40 17 65.48 58 0.92 61 0.94 61 0.73 47 0.80 01 34.89 55 34.77 62
L6 2 3 1 0 2 9 0.44 78 0.33 01 0.64 76 118.82 49 86.453 3 78.617 0 57.30 69 0.93 49 0.95 04 0.76 30 0.81 49 27.24 31 27.10 62
DG-III
L1 2 5 1 3 2 3 0.80 19 0.38 34 0.61 46 197.41 81 146.63 46 131.66 16 98.66 57 0.91 41 0.93 29 0.69 74 0.75 74 25.72 38 25.06 11
L2 2 3 2 5 1 3 0.58 71 0.67 42 0.33 21 171.14 15 133.79 63 113.87 13 89.70 10 0.92 12 0.93 66 0.71 92 0.76 96 21.82 12 21.22 60
L3 2 5 2 3 1 3 0.81 25 0.60 13 0.38 77 187.69 28 140.67 86 125.06 58 94.54 82 0.91 66 0.93 51 0.70 49 0.76 46 25.04 85 24.40 12
L4 1 3 3 0 2 3 0.46 77 0.48 64 0.69 98 169.46 43 116.61 01 112.78 82 78.15 43 0.92 06 0.94 35 0.71 74 0.79 14 31.18 90 30.70 70
L5 2 5 1 3 2 3 0.65 71 0.33 28 0.60 59 151.20 45 115.36 42 100.40 17 77.26 60 0.92 61 0.94 15 0.73 47 0.78 57 23.70 32 23.04 31
L6 1 3 2 3 2 5 0.33 29 0.57 15 0.69 15 118.82 49 83.728 7 78.617 0 56.05 44 0.93 49 0.95 08 0.76 30 0.81 73 29.53 60 28.69 94
DG-IV
L1 2 3 2 9 1 2 1.00 00 1.00 00 0.84 59 197.41 81 19.001 2 131.66 16 14.42 82 0.91 41 0.98 46 0.69 74 0.94 00 90.37 52 89.04 15
L2 2 3 1 2 2 9 1.00 00 0.74 42 1.00 00 171.14 15 18.483 3 113.87 13 13.96 66 0.92 12 0.98 80 0.71 92 0.95 30 89.20 00 87.73 47
L3 2 3 1 2 2 9 1.00 00 0.81 21 1.00 00 187.69 28 18.209 5 125.06 58 13.85 16 0.91 66 0.98 60 0.70 49 0.94 50 90.29 82 88.92 45
L4 1 2 2 3 2 9 0.77 15 1.00 00 1.00 00 169.46 43 13.425 4 112.78 82 10.60 90 0.92 06 0.98 96 0.71 74 0.95 90 92.07 77 90.59 39
L5 1 2 2 9 2 3 0.68 34 1.00 00 1.00 00 151.20 45 14.886 2 100.40 17 11.49 04 0.92 61 0.99 15 0.73 47 0.96 53 90.15 49 88.55 56
L6 2 9 1 2 2 3 0.93 30 0.59 82 0.96 38 118.82 49 9.9327 78.617 0 7.980 3 0.93 49 0.99 36 0.76 30 0.97 19 91.64 09 89.84 92
5.3 33-bus system:
The PLs in the system before executing DG for different ZIP load models are 197.418 kW,
131.66 kVAr for laptop charger load (L-1), 171.142 kW, 113.87 kVAr for Tungsten light load
(L2), 187.69 kW, 125.06 kVAr for CFL bulb load (L3), 169.46 kW, 112.78 kVAr for load
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

Elevator (L4), 151.2 kW, 100.4 kVAr for Resistance Heater (L5) & 118.82 kW, 78.61 kVAr for
load Battery Charger (L6). Tabulated results in Table VIII reveals the PLs for different ZIP
based load models with different DGs. The losses induced in the system after executing active
power injection i.e., Type-I DG for different ZIP load models are 67.66 kW, 46.71 kVAr for
load L1, 66.46 kW, 45.68 kVAr for load L2, 65.72 kW, 45.32 kVAr for load L3, similarly for
load L4, L5 & L6 has PL of 49.14 kW, 55.53 kW, 36.53 kW & 34.14 kVAr, 38.22 kVAr, 25.32
kVAr. The PL induced in the system after injecting reactive power with Type-II DG are 131.54
kW, 87.99 kVAr for load L1, 106.43 kW, 71.02 kVAr for load L2, 123.91 kW, 82.84 kVAr for
load L3, 112.78 kW, 82.76 kVAr for load L4, 98.44 kW, 65.48 kVAr for load L5 & 81.45 kW,
57.30 kVAr for load L6.

(a)  Active power loss on ZIP based load models for
33-bus system
(b) Reactive power loss on ZIP based load models for
33- bus system
(c) VSI on ZIP based load models for 33-bus system
(d) Voltage profile improvement on ZIP based load
models
for 33-bus system
(e) Percentage (active) power loss on ZIP based load
models for
33-bus system
(f)  Percentage (reactive) power loss on ZIP based load
models for
33- bus system
Fig.  13.Power loss & Voltage profile enhancement on different ZIP load models with diverse DGs for 33-
bus system
197.4181
67.6665
131.5418
146.6346
19.0012
171.1415
66.4661
106.4377
133.7963
18.4833
187.6928
65.7260
123.9150
140.6786
18.2095
169.4643
49.1454
124.0655
116.6101
13.4254
151.2045
55.5361
98.4410
115.3642
14.8862
118.8249
36.5329
86.4533
83.7287
9.9327
0
50
100
150
200
250
Base DG-I DG-II DG-III DG-IV
L1
L2
L3
L4
L5
L6
Ploss( kW)
131.6616
46.6714
87.9949
98.6657
14.4282
113.8713
45.6872
71.0180
89.7010
13.9666
125.0658
45.3263
82.8450
94.5482
13.8516
112.7882
34.1460
82.7656
78.1543
10.6090
100.4017
38.2201
65.4858
77.2660
11.4904
78.6170
25.3298
57.3069
56.0544
7.9803
0
20
40
60
80
100
120
140
160
Base DG-I DG-II DG-III DG-IV
L1
L2
L3
L4
L5
L6
Qloss( kVAr)
0.6974
0.8777
0.7753
0.7574
0.9400
0.7192
0.8853
0.7977
0.7696
0.9530
0.7049
0.8831
0.7811
0.7646
0.9450
0.7174
0.8985
0.7743
0.7914
0.9590
0.7347
0.8956
0.8001
0.7857
0.9653
0.7630
0.9167
0.8149
0.8173
0.9719
0.65
0.70
0.75
0.80
0.85
0.90
0.95
1.00
Base DG-I DG-II DG-III DG-IV
L1 L2 L3 L4 L5 L6
Voltage(p.u)
0.9141
0.9679
0.9386
0.9329
0.9846
0.9212
0.9700
0.9454
0.9366
0.9880
0.9166
0.9694
0.9404
0.9351
0.9860
0.9206
0.9736
0.9383
0.9435
0.9896
0.9261
0.9728
0.9461
0.9415
0.9915
0.9349
0.9785
0.9504
0.9508
0.9936
0.00
0.20
0.40
0.60
0.80
1.00
Base DG-I DG-II DG-III DG-IV
L1 L2 L3 L4 L5 L6
Voltage(p.u)
65.7243
33.3689
25.7238
90.3752
61.1631
37.8072
21.8212
89.2000
64.9822
33.9799
25.0485
90.2982
70.9995
26.7896
31.1890
92.0777
63.2708
34.8955
23.7032
90.1549
69.2548
27.2431
29.5360
91.6409
20
40
60
80
100
120
DG-I DG-II DG-III DG-IV
L1 L2 L3 L4 L5 L6
Ploss(%)
64.5520
33.1659
25.0611
89.0415
59.8782
37.6331
21.2260
87.7347
63.7580
33.7588
24.4012
88.9245
69.7256
26.6186
30.7070
90.5939
61.9328
34.7762
23.0431
88.5556
67.7807
27.1062
28.6994
89.8492
20
40
60
80
100
120
DG-I DG-II DG-III DG-IV
L1 L2 L3 L4 L5 L6
Qloss(%)
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

Type-III DG which injects active power and engages the reactive power has high PLs as
linked with other types of DGs. Maximum percentage PL reduction is observed with Type-IV
DG. The overall PL after implementing Type DG on different ZIP load model are 19.01 kW,
18.48 kW, 18.20 kW, 13.42 kW, 14.88 kW & 9.93 kW. The percentage of PL reduction for
load L1 on different DG is as follows 65.72 for Type-I DG, 33.36 for Type-II DG, 25.72 for
Type-III & 90.37 for Type-IV DG.
Table.  IXReal and reactive power losses with different DGs on ZIP based load models for 69-bus system
Ploss(kW) Qloss(kVAr) Min Volt (p.u) Min VSI (p.u) % ReductionLoa
d Location Size (MW) WoDG WDG WoD G WDG WoD G WD G WoD G WD G %Ploss %Qloss
DG-I
L1 6 0 1 7 6 1 0.96 43 0.53 06 0.77 32 216.60 91 65.142 8 98.39 58 33.02 44 0.91 06 0.97 91 0.68 66 0.91 81 69.92 61 66.43 72
L2 6 0 6 1 1 7 0.89 13 0.70 48 0.47 12 181.52 21 65.498 0 83.35 19 33.08 28 0.91 98 0.98 19 0.71 52 0.92 78 63.91 73 60.30 95
L3 6 0 1 6 6 1 1.00 00 0.49 54 0.70 88 203.45 33 63.405 4 92.76 63 32.25 97 0.91 37 0.98 06 0.69 62 0.92 37 68.83 54 65.22 48
L4 1 6 6 1 6 0 0.51 63 0.78 90 0.95 39 183.90 71 45.353 6 84.35 75 24.44 97 0.91 71 0.98 50 0.70 63 0.93 99 75.33 89 71.01 66
L5 6 0 1 6 6 3 1.00 00 0.48 31 0.45 11 157.25 46 53.228 3 72.92 71 27.80 36 0.92 53 0.98 38 0.73 22 0.92 69 66.15 15 61.87 49
L6 1 6 6 3 6 0 0.50 73 0.30 62 1.00 00 119.76 67 33.079 7 56.62 71 18.88 47 0.93 45 0.98 68 0.76 18 0.93 93 72.37 99 66.65 08
DG-II
L1 6 0 1 6 5 4 1.00 00 0.30 18 0.45 72 216.60 91 145.60 79 98.39 58 67.69 26 0.91 06 0.93 05 0.68 66 0.74 89 32.77 85 31.20 38
L2 6 0 6 3 1 1 1.00 00 0.18 71 0.56 10 181.52 21 112.41 19 83.35 19 53.32 99 0.91 98 0.94 13 0.71 52 0.78 30 38.07 26 36.01 84
L3 5 2 6 0 1 6 0.49 62 1.00 00 0.34 53 203.45 33 134.90 98 92.76 63 63.08 57 0.91 37 0.93 31 0.69 62 0.75 72 33.69 00 31.99 50
L4 6 0 6 6 1 6 0.93 09 0.35 07 0.26 65 183.90 71 135.92 26 84.35 75 63.49 32 0.91 71 0.93 39 0.70 63 0.75 99 26.09 17 24.73 32
L5 6 6 1 5 6 0 0.20 13 0.26 79 0.99 89 157.25 46 101.71 99 72.92 71 48.87 20 0.92 53 0.94 27 0.73 22 0.78 87 35.31 52 32.98 51
L6 6 0 1 7 4 8 0.80 24 0.29 37 0.66 52 119.76 67 87.200 4 56.62 71 41.18 85 0.93 45 0.94 79 0.76 18 0.80 54 27.19 14 27.26 37
DG-III
L1 4 8 6 0 1 5 0.37 42 0.99 97 0.33 70 216.60 91 154.71 92 98.39 58 70.65 57 0.91 06 0.94 24 0.68 66 0.78 79 28.57 22 28.19 24
L2 1 8 6 8 6 0 0.21 75 0.18 17 0.81 79 181.52 21 140.02 84 83.35 19 65.35 38 0.91 98 0.94 61 0.71 52 0.80 03 22.85 88 21.59 30
L3 6 0 6 8 1 7 1.00 00 0.17 99 0.22 31 203.45 33 147.50 02 92.76 63 68.58 73 0.91 37 0.94 57 0.69 62 0.79 88 27.50 17 26.06 45
L4 5 0 6 0 1 6 0.37 74 1.00 00 0.21 18 183.90 71 119.65 95 84.35 75 56.62 95 0.91 71 0.94 98 0.70 63 0.81 28 34.93 48 32.86 96
L5 5 0 2 0 6 0 0.44 26 0.20 01 0.76 10 157.25 46 118.00 42 72.92 71 55.89 28 0.92 53 0.95 07 0.73 22 0.81 60 24.95 98 23.35 80
L6 6 0 4 8 1 8 0.78 31 0.48 70 0.28 43 119.76 67 81.787 7 56.62 71 39.10 97 0.93 45 0.95 88 0.76 18 0.84 32 31.71 08 30.93 46
DG-IV
L1 1 7 6 1 6 0 0.56 59 0.88 21 0.97 57 216.60 91 10.741 5 98.39 58 9.461 2 0.91 06 0.99 43 0.68 66 0.97 74 95.04 11 90.38 45
L2 6 1 6 0 1 6 0.69 94 1.00 00 0.52 46 181.52 21 13.019 6 83.35 19 10.37 24 0.91 98 0.99 44 0.71 52 0.97 72 92.82 75 87.55 59
L3 6 1 6 0 1 6 0.81 43 1.00 00 0.56 01 203.45 33 10.896 8 92.76 63 9.487 4 0.91 37 0.99 43 0.69 62 0.97 81 94.64 41 89.77 28
L4 1 6 6 0 6 1 0.54 81 1.00 00 0.71 68 183.90 71 7.3241 84.35 75 7.936 1 0.91 71 0.99 44 0.70 63 0.97 81 96.01 75 90.59 23
L5 1 7 6 0 6 2 0.53 42 1.00 00 0.53 59 157.25 46 10.395 4 72.92 71 9.216 1 0.92 53 0.99 44 0.73 22 0.97 82 93.38 94 87.36 26
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

L6 1 6 6 0 6 3 0.45 57 0.97 79 0.40 89 119.76 67 6.3884 56.62 71 7.288 6 0.93 45 0.99 43 0.76 18 0.97 69 94.66 60 87.12 88
Similarly, the percentage PL reduction for loads L2, L3 & L4 are 61.16, 63.75, 69.72 for
Type-I DG, 37.81, 33.97, 26.78 for Type-II DG, 21.82, 25.04, 31.18 for Type-III DG, 89.2,
90.29, 92.07 for Type-IV DG. Tabulate results shown in Table VIII gives a detailed explanation
on real PL, reactive PL, voltage profile enhancement and VSI on various ZIP based load
models. Fig 13 displays the power loss & voltage profile improvement on 33-bus system with
diverse DGs on six ZIP load models.
5.4 69-Bus System:
The numerical results enlisted in Table IX shows that PLs i.e., real and reactive for different
ZIP based load models. The losses induced in the system without implementing DGs for
different ZIP load models are 216.61 kW, 98.39 kVAr for load L1, 181.52 kW, 83.35 kVAr for
load L2, 203.45 kW, 92.76 kVAr for load L3, 183.91 kW, 84.35 kVAr for load L4, 157.25 kW,
72.92 kVAr for load L5, 119.76 kW, 56.62 kVAr for load L6. OLSDG for Type-I DG for load L1
is 60, 17, 61, 964 kW, 530 kW, 773 kW with PL reduction 65.14 kW, 33.02 kVAr. The OLSDG
for load L2 is 60, 61, 17, 891 kW, 704 kW, 471 kW with PL reduction 65.49 kW, 33.08 kVAr.
Similarly, the optimal location for other load models such as load L3 & L4 is 60, 61, 61 and
the optimal location for load L5 & L6 is 16, 63, 60 with PL reduction of 63.41 kW, 32.25 kVAr
(L3), 45.35 kW, 24.45 kVAr (L4), 53.22 kW, 27.81 kVAr (L5), 33.07 kW, 56.62 kVAr (L6). The
percentage reduction in PL for different ZIP based load models is 69.92, 63.91, 68.83, 75.33,
66.15 and 72.37. Similarly, reactive PL percentage reduction with different ZIP load is 66.43,
60.31, 65.22, 71.02, 61.87, and 66.65 respectively.
(a)  Active power loss on ZIP based load models for
69-bus system
(b) Reactive power loss on ZIP based load models for 69-
bus system
(c) VSI on ZIP based load models for 69-bus system
(d) Improvement in voltage profile on ZIP based load
models for
69-bus system
216.6091
65.1428
145.6079
154.7192
10.7415
181.5221
65.4980
112.4119
140.0284
13.0196
203.4533
63.4054
134.9098
147.5002
10.8968
183.9071
45.3536
135.9226
119.6595
7.3241
157.2546
53.2283
101.7199
118.0042
10.3954
119.7667
33.0797
87.2004
81.7877
6.3884
0
50
100
150
200
250
Base DG-I DG-II DG-III DG-IV
L1
L2
L3
L4
L5
L6
Ploss( kW)
98.3958
33.0244
67.6926
70.6557
9.4612
83.3519
33.0828
53.3299
65.3538
10.3724
92.7663
32.2597
63.0857
68.5873
9.4874
84.3575
24.4497
63.4932
56.6295
7.9361
72.9271
27.8036
48.8720
55.8928
9.2161
56.6271
18.8847
41.1885
39.1097
7.2886
0
20
40
60
80
100
120
Base DG-I DG-II DG-III DG-IV
L1
L2
L3
L4
L5
L6
Qloss( kVAr)
0.6866
0.9181
0.7489
0.7879
0.9774
0.7152
0.9278
0.7830
0.8003
0.9772
0.6962
0.9237
0.7572
0.7988
0.9781
0.7063
0.9399
0.7599
0.8128
0.9781
0.7322
0.9269
0.7887
0.8160
0.9782
0.7618
0.9393
0.8054
0.8432
0.9769
0.65
0.70
0.75
0.80
0.85
0.90
0.95
1.00
1.05
Base DG-I DG-II DG-III DG-IV
L1 L2
L3 L4
L5 L6
Voltage(p.u)
0.9106
0.9791
0.9305
0.9424
0.9943
0.9198
0.9819
0.9413
0.9461
0.9944
0.9137
0.9806
0.9331
0.9457
0.9943
0.9171
0.9850
0.9339
0.9498
0.9944
0.9253
0.9838
0.9427
0.9507
0.9944
0.9345
0.9868
0.9479
0.9588
0.9943
0.00
0.20
0.40
0.60
0.80
1.00
Base DG-I DG-II DG-III DG-IV
L1 L2 L3
L4 L5 L6
Voltage(p.u)
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

(e) Percentage (active) power loss on ZIP based
load models for 69-bus system
(f)  Percentage (reactive) power loss on ZIP based load
models for 69-bus system
Fig.  14.Power loss & Voltage profile improvement on different ZIP based load models with
different DGs for 69-bus system
Type-II DG that inoculates reactive power into the system also lessens the PLs. The power
induced in the system after injecting reactive power into the system are 145.6 kW, 67.69 for
load L1 with optimal location and capacity 60,16, 54, 1MW, 301 kW, 457 kW. Reduction in
PLs load model L2, L3 are 112.41 kW, 53.32 kVAr, 134.91 kW, 63.08 kVAr with optimal
location 60, 63, 11 & 52, 60, 16. Similarly, results for other load models are given in
numerical results. The PL reduction for Type-II DG with different ZIP based load models in
percentage are 32.77, 38.07, 33.69, 26.09, 35.31and 27.19.
It is evident from tabulated results that Type-III DG which injects active power and
absorbs reactive power has relatively high PL as compared other DGs. Moreover, the PLs
induced after executing Type-III DG with different ZIP load models are 154.71 kW, 70.65
kVAr for load L1, 140.02 kW, 65.35 kVAr for load L2, 147.5 kW, 68.58 kVAr for load L3,
119.65 kW, 56.62 kVAr for load L4, 118.01 kW, 55.89 kVAr for load L5, 81.78 kW, 39.11 kVAr
for load L6. The PL reduction for different ZIP load models in percentage is 28.57, 22.85,
27.50, 34.93, 24.95 & 31.71. Similarly, the percentage reduction in reactive PL for different
ZIP based load models is 28.19, 21.59, 26.06, 32.86, 23.35 & 30.93. It is clear from numerical
results that Type-IV DG which injects both active power and reactive power into the system
has minimum PL as compared other DGs.
The PLs incurred in the system after the implementation of Type-IV DG with different
ZIP load models are 10.74 kW, 9.46 kVAr for load L1, 13.01 kW, 10.37 kVAr for load L2,
10.89 kW, 9.48 kVAr for load L3, 7.32 kW, 7.93 kVAr for load L4, 10.39 kW, 9.21 kVAr for
load L5, 6.38 kW, 7.28 kVAr for load L6. The PL reduction for different ZIP based load models
in percentage are 95.04, 92.82, 94.64, 96.07.93, 93.38 & 94.66. Similarly, the percentage
reactive PL reduction for different ZIP load models is 90.38, 87.55, 89.77, 90.59, 87.36 &
87.12. Tabulate results shown in Table IX gives a detailed explanation on real PL, reactive
PL, voltage profile enhancement and VSI on different ZIP based load models with different
DGs. Fig 14 illustrates the PL & voltage profile improvement on 69-bus system with different
DGs on six ZIP load models.
5.5 Discussion
One of the major concern areas is reducing the PLs where many utilities are focusing.
In present scenario, DG is used as one of the alternatives to minimize these losses in DSs.
Inappropriate allocation of DG induces more PLs due to poor voltage regulations. Many
numerical, heuristic and optimization techniques are used to deal with this problem. Many
researchers have explored optimization this problem with different heuristic and
optimization techniques. Most of the authors have considered a single type of DG i.e., either
injecting real power or reactive power to curtail the PLs with appropriate size and position.
Based on power delivering capability with respect to their terminal characteristics different
type of DGs is available for the study. In this paper, an independent implementation for
diverse types of DGs is considered with an objective to further reduce the PLs.
In this study, multiple cases are considered to test the effect of DG on different load
models. Primarily, different types of DGs are used with CP load model to lessen the PLs. To
69.9261
32.7785
28.5722
95.0411
63.9173
38.0726
22.8588
92.8275
68.8354
33.6900
27.5017
94.6441
75.3389
26.0917
34.9348
96.0175
66.1515
35.3152
24.9598
93.3894
72.3799
27.1914
31.7108
94.6660
20
40
60
80
100
120
DG-I DG-II DG-III DG-IV
L1 L2 L3 L4 L5 L6
Ploss(%)
66.4372
31.2038
28.1924
90.3845
60.3095
36.0184
21.5930
87.5559
65.2248
31.9950
26.0645
89.7728
71.0166
24.7332
32.8696
90.5922
61.8749
32.9851
23.3580
87.3625
66.6508
27.2637
30.9346
87.1288
20
40
60
80
100
120
DG-I DG-II DG-III DG-IV
L1 L2 L3 L4 L5 L6
Qloss(%)
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

the best of author knowledge, majority of loads used in DSs relies on magnitude of supply
voltage, but most of the work done to solve the DG optimization with CP load model which
voltage independent. If the OLSDG obtained with CP load are used in practical DSs, which
induces higher PL and deprived voltage regulation. In addition to CP load, another load which
is voltage dependent is considered. Thus, in another case, a realistic load model is utilized
to analyze the consequence of diverse DGs. Six different ZIP based load models are used to
study the DG effect.
Also, two different IEEE benchmark test bus systems are utilized to evaluate the results.
Type-IV DG has maximum PL reduction for both test cases. Whereas, Type-III DG has
minimum percentage reduction in PL as compared with other types of DGs. Maximum PL
reduction in Type-IV is occurring mainly due to active and reactive power injection capability.
In case of Type-III DG, it is absorbing reactive power from the system and injecting only
active power into the network. Mixed DG has maximum reduction in PL as compared with
other types of DG except Type-IV DG. OLSDG not only reduces the PL but also improves the
voltage stability and overall voltage profile of the system. It is observed that Type-IV DG has
maximum improvement in VSI and voltage profile as compared with other DG types. It has
been observed that combination of different types of DGs reduces majority of PLs and
improves VSI.
This work provides a impactful contribution in the field of grid management (power
system) for researchers and practitioners. This study aims to achieve PL reduction via DG
implementation by injecting power (active, reactive and both). This study presents an
investigation involving CP load model and ZIP load model on diverse DGs with their terminal
characteristics. Along with CP load model, inclusion of realistic load or ZIP load model
enables the researchers to know the impact of DG allocation under different load conditions.
In addition, a powerful optimization tool, i.e., a novel MAQiEA is proposed which plays a
central role in solving the combinatorial optimization problem. MAQiEA is the updated
version of AQiEA that incorporate quantum computing concepts such as Q-bits, measurement
operator, superposition, entanglement and rotational strategies which allows enhanced
search ability and faster convergences. Researchers can further extend MAQiEA to address
many engineering optimization problems in the field of power systems.
MAQiEA serves as a robust supporting tool for practitioners as it can handle both variables
such as continuous and discrete, it is suited for practical planning scenarios of DG. Inclusion
of ZIP Load model make the system representation more realistic, ensuring the solution
obtained with proposed algorithm closely reflect real world DSs. By integrating diverse DGs
in DS, DS operators and utility engineers can gain practical advantages. For instance, one
DG injects active power and one category provides reactive power support to the system.
The overall PL reduction and voltage profile improvement is not same on both cases. This
gives an opportunity for the practitioners to fine tune the placement according to location
specific which maximize the performance.
6. CONCLUSIONS
This work is performed to mitigate the losses in DSs with different types of DGs. Majority of
reviewed work has solved this important optimization problem with either active or reactive
power injection. But in actual practice other types of DGs are also available for the study. In
this study, based on active and reactive power delivering capability with respect to their
terminal characteristic’s diverse types of DGs are considered. In addition to above, a realistic
load model is also used to study the effect of DG. The OLSDG is a complex combinatorial
optimization issue with both continuous and discrete factors. The best position and capacity
of DG were determined using a quantum-inspired evolutionary algorithm known as MAQiEA.
Also, two benchmark IEEE bus systems i.e., 33 and 69 are used to test the effectiveness of
MAQiEA. Two different cases are considered to analyze the effect of DG. First case is mainly
implemented to study the effect of different DGs on CP load model which is independent of
voltage. The numerical results reveal, Type-IV DG registers a maximum drop in PL when
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

corelated with other types of DGs, the percentage PL reduction of different DGs on both test
bus systems are 64.62%, 34.73%, 24.33% and 89.92% for 33 bus system and 67.58%,
34.68%, 26.66% and 94.42% for 69 bus system. Maximum PL reduction in Type-IV is
occurring mainly due to active and reactive power injection capability. For CP load model, a
category of mix DGs (87.99% for 33 bus system and 92.34% for 69 bus system) is also used
to further reduce the losses. It is pertinent that mixed DG has maximum reduction in PL and
outperforms the other types of DG except Type-IV. Second case is implemented to observe
the effect of different DGs on a realistic load model. Six different ZIP based load models are
specifically utilized to study the effect of DG. The percentage of rection in PL induced in both
test system after injecting power with different DGs are 61%-73%, 26%-38%, 21%-35% and
89%-96% respectively. The simulated results are also correlated with AOA, ALO, WHO and
MRFO. The computational results demonstrated that MAQiEA have improved performance
than the other algorithms in the available literature. The work is mainly limited to fixed load
conditions and steady state operations, renewable intermittency, load uncertainty and
harmonic impacts are not considered. In the future, this work could be enhanced with
simultaneous implementation of DG and electric vehicles (EV). The integration of charging
stations (EV charging stations) is examined to study the impact of DG on voltage profile
improvement and PL reduction with dynamic load profiles.
DECLARATIONS
FUNDING
No funding was received for conducting this study.
Non-financial interests: None.
Data availability
All data generated or analysed during this study are included in this published article.
Author contributions
G.M., P.K., A.M., S.K.: Conceptualization, Data curation, Methodology, Software, Resources,
Project, Writing- Original draft preparation, and A.K.P., N.K.K. and P.A.: Validation,
Investigation, Writing- Original draft preparation, Writing—Review & Editing,
administration, Supervision, Visualization and Resources.
Conflict of interest
The authors have no conflicts of interest to declare that are relevant to the content
presented in this article.
Ethical approval
Not applicable, since this article does not involve any human or animal participation.
Consent to Participate: Not applicable.
Consent to Publish: Not applicable.
Additional information
Correspondence should be addressed to P.A.
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

REFERENCES
[1] P. Dorji, S. Lachowicz, and O. Bass, “Optimization of size and siting of distributed
generation in unbalanced distribution systems: A literature review,” Electric Power
Systems Research, vol. 249, p. 112039, 2025.
[2] P. Rajakumar, P. M. Balasubramaniam, E. Parimalasundar, K. Suresh, and P. Aravind,
“Optimized placement and sizing of solar photovoltaic distributed generation using
jellyfish search algorithm for enhanced power system performance,” Scientific
Reports, vol. 15, no. 1, p. 20755, 2025.
[3] S. M. Nassar, A. A. Saleh, A. A. Eisa, E. M. Abdallah, and I. A. Nassar, “Optimal
allocation of renewable energy resources in distribution systems using meta-heuristic
algorithms,” Results in Engineering, vol. 25, p. 104276, 2025.
[4] Khunkitti, Sirote, Natsawat Pompern, Suttichai Premrudeepreechacharn, and Apirat
Siritaratiwat. "Optimal placement and capacity of BESS and PV in EV integrated
distribution systems: the tenth feeder of phitsanulok substation case study." Batteries
10, no. 6 (2024): 212.
[5] Khunkitti, Sirote, Krit Wichitkrailat, and Apirat Siritaratiwat. "Optimal locations and
capacities of multiple BESSs in a RES-integrated distribution network: a real-world
case study." Scientific Reports (2026).
[6] N. S. Rau and Y.-H. Wan, “Optimum location of resources in distributed planning,”
IEEE Transactions on Power Systems, vol. 9, no. 4, pp. 2014–2020, 1994.
[7] T. E. Gümüş, S. Emiroglu, and M. A. Yalcin, “Optimal DG allocation and sizing in
distribution systems with Thevenin based impedance stability index,” International
Journal of Electrical Power & Energy Systems, vol. 144, p. 108555, 2023.
[8] N. Acharya, P. Mahat, and N. Mithulananthan, “An analytical approach for DG
allocation in primary distribution network,” International Journal of Electrical Power
& Energy Systems, vol. 28, no. 10, pp. 669–678, 2006.
[9] S. G. Naik, D. K. Khatod, and M. P. Sharma, “Optimal allocation of combined DG and
capacitor for real power loss minimization in distribution networks,” International
Journal of Electrical Power & Energy Systems, vol. 53, pp. 967–973, 2013.
[10]P. Maurya, P. Tiwari, and A. Pratap, “Application of the hippopotamus optimization
algorithm for distribution network reconfiguration with distributed generation
considering different load models for enhancement of power system performance,”
Electrical Engineering, vol. 107, no. 4, pp. 3909–3946, 2025.
[11]N. Bouchikhi et al. , “Optimal distributed generation placement and sizing using
modified grey wolf optimization and ETAP for power system performance
enhancement and protection adaptation,” Scientific Reports, vol. 15, no. 1, p. 13919,
2025.
[12]T. Hamadneh, B. Batiha, and G. M. Gharib, “Enhanced distributed generation
placement using carpet weaver optimization: A comparative metaheuristic approach,”
Large-Scale Systems, vol. 18, p. 22, 2025.
[13]R. Palanisamy and S. K. Muthusamy, “Optimal siting and sizing of multiple distributed
generation units in radial distribution system using ant lion optimization algorithm,”
Journal of Electrical Engineering & Technology, vol. 16, pp. 79–89, 2021.
[14]P. Maurya, P. Tiwari, and A. Pratap, “Puma optimiser technique for efficient
distributed generation planning in electrical distribution network with different load
models,” International Journal of Ambient Energy, vol. 46, no. 1, p. 2478140, 2025.
[15]M. H. Ali et al., “An improved wild horse optimization algorithm for reliability based
optimal DG planning of radial distribution networks,” Energy Reports, vol. 8, pp. 582–
604, 2022.
[16]M. G. Hemeida et al., “Optimal allocation of distributed generators DG based Manta
Ray Foraging Optimization algorithm (MRFO),” Ain Shams Engineering Journal, vol.
12, no. 1, pp. 609–619, 2021.
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

[17]B. P. Nanda, D. P. Mishra, and S. R. Salkuti, “A modified ant lion optimization
algorithm for efficient distributed generation allocation in power distribution
networks,” Electric Power Systems Research, vol. 246, p. 111705, 2025.
[18]J. Montano et al., “Application of the arithmetic optimization algorithm to solve the
optimal power flow problem in direct current networks,” Results in Engineering, vol.
16, p. 100654, 2022.
[19]B. Mahdad, “Optimal integration and coordination of distributed generation and shunt
compensators using improved African vultures optimizer,” Engineering Optimization,
vol. 56, no. 4, pp. 548–585, 2024.
[20]A. Rahiminejad, S. H. Hosseinian, B. Vahidi, and S. Shahrooyan, “Simultaneous
distributed generation placement, capacitor placement, and reconfiguration using a
modified teaching-learning-based optimization algorithm,” Electric Power
Components and Systems, vol. 44, no. 14, pp. 1631–1644, 2016.
[21]N. C. Hien, N. Mithulananthan, and R. C. Bansal, “Location and sizing of distributed
generation units for loadability enhancement in primary feeder,” IEEE Systems
Journal, vol. 7, no. 4, pp. 797–806, 2013.
[22]V. C. Veera Reddy, “Optimal renewable resources placement in distribution networks
by combined power loss index and whale optimization algorithms,” Journal of
Electrical Systems and Information Technology, vol. 5, no. 2, pp. 175–191, 2018.
[23]K. M. Jagtap and D. K. Khatod, “Loss allocation in radial distribution networks with
various distributed generation and load models,” International Journal of Electrical
Power & Energy Systems, vol. 75, pp. 173–186, 2016.
[24]S. Banerjee, D. Das, and C. K. Chanda, “Voltage stability of radial distribution
networks for different types of loads,” International Journal of Power and Energy
Conversion, vol. 5, no. 1, pp. 70–87, 2014.
[25]M. F. N. Khan and T. N. Malik, “Probabilistic generation model for optimal allocation
of PV DG in distribution system with time-varying load models,” Journal of Renewable
and Sustainable Energy, vol. 9, no. 6, 2017.
[26]M. F. N. Khan, T. N. Malik, and I. A. Sajjad, “Impact of time varying load models on
PV DG planning,” Journal of Renewable and Sustainable Energy, vol. 10, no. 3, 2018.
[27]G. Manikanta, A. Mani, H. P. Singh, and D. K. Chaturvedi, “Effect of voltage
dependent load model on placement and sizing of distributed generator in large scale
distribution system,” Majlesi Journal of Electrical Engineering, vol. 14, no. 4, 2020.
[28]Sujatha, B. C., A. Usha, R. S. Geetha, and E. Poornima. "Impact of Various Load
Models for Combined Assignment of DG Source and D-STATCOM Device in the Radial
Distribution System." Distributed Generation & Alternative Energy Journal  (2023):
1149-1176.
[29]M. Kashyap, S. Kansal, and B. P. Singh, “Optimal installation of multiple type DGs
considering constant, ZIP load and load growth,” International Journal of Ambient
Energy, vol. 41, no. 14, pp. 1561–1569, 2020.
[30]A. Bokhari et al. , “Experimental determination of the ZIP coefficients for modern
residential, commercial, and industrial loads,” IEEE Transactions on Power Delivery,
vol. 29, no. 3, pp. 1372–1381, 2013.
[31]K. Polisetti and A. Kumar, “Distribution system nodal prices determination for
realistic ZIP and seasonal loads: An optimal power flow approach,” Procedia
Technology, vol. 25, pp. 702–709, 2016.
[32]Sadeghi, M., and M. Kalantar. "Allocation and sizing of a DG unit considering ZIP load
model." In 2013 Smart Grid Conference (SGC), pp. 252-258. IEEE, 2013.
[33]G. Manikanta, A. Mani, A. Jain, R. Kuppusamy, and Y. Teekaraman, “Implementation
of distributed energy resources along with network reconfiguration for cost-benefit
analysis,” Sustainable Computing: Informatics and Systems, vol. 45, p. 101078, 2025.
[34]G. Manikanta, A. Mani, H. P. Singh, and D. K. Chaturvedi, “Adaptive quantum-inspired
evolutionary algorithm for optimizing power losses by dynamic load allocation on
distributed generators,” Serbian Journal of Electrical Engineering, vol. 16, no. 3, pp.
325–357, 2019.
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

[35]G. Manikanta et al., “The impact of the mixed load model on the placement and sizing
of distributed generation (DG) in a radial distribution network,” in Proc. 2024 Int.
Conf. Social and Sustainable Innovations in Technology and Engineering (SASI-ITE),
pp. 66–71, IEEE, 2024.
[36]G. Manikanta, A. Mani, H. P. Singh, and D. K. Chaturvedi, “Enhancement of
performance indices on realistic load models with distributed generators in radial
distribution network,” Energy Systems, vol. 15, no. 2, pp. 635–671, 2024.
[37]G. Manikanta and A. Mani, “A quantum-inspired evolutionary approach to minimize
the losses in distribution network through feeder reconfiguration under time-varying
load,” Electrical Engineering, pp. 1–24, 2024.
[38]G. Manikanta, A. Mani, H. P. Singh, and D. K. Chaturvedi, “Minimization of power
losses in distribution system with variation in loads using adaptive quantum inspired
evolutionary algorithm,” in Proc. 2018 4th Int. Conf. Computing Communication and
Automation (ICCCA), pp. 1–6, IEEE, 2018.
[39]A. Mani and C. Patvardhan, “An improved model of ceramic grinding process and its
optimization by adaptive quantum inspired evolutionary algorithm,” International
Journal of Simulations: Systems Science and Technology , vol. 11, no. 6, pp. 76–85,
2012.
[40]G. Manikanta, N. K. Kumar, A. Mani, and V. Indragandhi, “Placement and sizing of
distributed generator and capacitor in a radial distribution system considering load
growth,” in Intelligent and Soft Computing Systems for Green Energy, pp. 1–24, 2023.
[41]G. Manikanta, A. Mani, H. P. Singh, and D. K. Chaturvedi, “Simultaneous placement
and sizing of DG and capacitor to minimize the power losses in radial distribution
network,” in Soft Computing: Theories and Applications: Proc. SoCTA 2017, pp. 605–
618, Springer, 2018.
[42]J.-H. Teng, “A direct approach for distribution system load flow solutions,” IEEE
Transactions on Power Delivery, vol. 18, no. 3, pp. 882–887, 2003.
[43]K.-H. Han and J.-H. Kim, “Quantum-inspired evolutionary algorithm for a class of
combinatorial optimization,” IEEE Transactions on Evolutionary Computation, vol. 6,
no. 6, pp. 580–593, 2002.
[44]G. Zhang, “Quantum-inspired evolutionary algorithms: A survey and empirical study,”
Journal of Heuristics, vol. 17, no. 3, pp. 303–351, 2011.
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS
