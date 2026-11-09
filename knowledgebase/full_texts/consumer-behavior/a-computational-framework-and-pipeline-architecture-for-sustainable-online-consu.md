---
title: A Computational Framework and Pipeline Architecture for Sustainable Online Consumer Behavior
url: https://doi.org/10.38094/jastt62509
category: consumer-behavior
subcategory: framework
date: 2025-11
venue: Journal of Applied Science and Technology Trends
authors:
- Nikita Panwar
- Dasharathraj K Shetty
- Sandeep S Shenoy
source: openalex-oa
pdf_url: https://jastt.org/index.php/jasttpath/article/download/509/115
pages: 19
chars: 110441
fetched_at: '2026-11-08T17:30:06+00:00'
kb_version: 1
---

# A Computational Framework and Pipeline Architecture for Sustainable Online Consumer Behavior

Vol. 06, No. 02, pp. 408 –426 (2025)
ISSN: 2708-0757

JOURNAL OF APPLIED SCIENCE AND TECHNOLOGY TRENDS

www.jastt.org

408

doi: 10.38094/jastt62509

A Computational Framework and Pipeline Architecture for
Sustainable Online Consumer Behavior
Nikita Panwar1 , Dasharathraj K. Shetty2 *, Sandeep S. Shenoy3 , Anusha Pai4
1Department of Humanities and Management, Manipal Institute of Technology, Manipal Academy of Higher Education, Ma nipal,
576104, Karnataka, India, nikita.mitmpl2022@learner.manipal.edu
2Manipal Institute of Technology, Manipal Academy of Higher Education, Manipal, 576104, Karnataka, India ,
raja.shetty@manipal.edu
3Manipal School of Commerce and Economics, Manipal Academy of Higher Education, Manipal, Karnataka, I ndia,
sandeep.shenoy@manipal.edu
4Department of Accommodations operations, Welcomgroup Graduate School of Hotel Administration, Manipal Academy of
Higher Education, Manipal, 576104, Karnataka, India, anusha.pai@manipal.edu

*Correspondence: raja.shetty@manipal.edu
Abstract
This study proposes a design -oriented computational framework and pipeline architecture for e-commerce systems to address the gap
between pro-environmental attitudes and sustainable purchase behaviors. Despite growing availability of green personal care products
(GPCP) on e -commerce platforms, consumer engagement remains limited. Prior studies of ten overlook this niche, focusing instead on
broader green product categories or offline retail contexts. This study also addresses the gap by examining how pro -environmental and
consumption values shape consumer behavior for GPCPs in digital commerce, and  then translates the validated determinants into a
computational design. A quantitative design guided by the Value–Attitude–Behavior framework was employed. Data were collected from
302 consumers who purchased GPCPs online in the past six months. Construct s were measured using validated scales and analyzed
through Partial Least Squares Structural Equation Modelling (PLS -SEM). The empirically significant determinants were then mapped
into a multi-stage pipeline architecture to demonstrate how behavioral fact ors can be operationalized within e -commerce systems. The
findings indicate that emotional value, functional quality value, and perceived environmental knowledge significantly shape p ositive
consumer attitudes toward GPCPs in e-commerce settings. Green purchase attitudes were strongly predictive of purchase intentions (β =
0.781, p < 0.000), which subsequently influenced actual purchase behavior (β = 0.726, p < 0.000). These empirically validated determinants
inform the computational pipeline, where values act as inputs, attitudes and intentions as intermediate system states, and behaviors as
measurable outcomes. Theoretically, this study advances the Value–Attitude–Behavior framework by confirming the distinct and context-
dependent roles of emotional and functional quality values, as well as environmental knowledge, in shaping sustainable consumer attitudes
in digital contexts. Practically, by integrating these behavioral insights into a pipeline design, the study contributes a co mputational
framework that links consumer psychology with system architecture.

Keywords: Pipeline Architecture, Sustainable Online Purchasing,  Green Personal Care Products, s dg12, Consumption Values,
Pro-Environmental Values
Received: September 17th, 2025 / Revised:  November 05th, 2025/ Accepted: November 15th, 2025 / Online: November 21st, 2025
I. INTRODUCTION
Computational systems architected to influence, measure,
and reinforce sustainable choices are beco ming increasingly
important as sustainability challenges intensify. Rising
environmental problems like climate change, resource
depletion, and pollution create both behavioural and design
challenges for digital commerce platforms. This shift has shaped
consumer behaviour, as individuals are more aware of the
environmental impact of their purchasing choices and prefer
eco-friendly alternatives [1]. However, a gap remains between
consumers’ stated environmental attitudes and their actual
purchases [2]. This d iscrepancy is visible across product
categories, including personal care, where eco-friendly products
are growing rapidly, especially in digital marketplaces. E -
commerce systems must reduce this gap by using structured data
flows, layered interfaces, and b ehaviour-informed pipeline
architectures.
While prior studies have extensively examined the role of
personal values in shaping sustainable consumption, much of the
existing literature has focused on offline or general retail
contexts, with limited attentio n paid to product -specific
behaviour within digital environments. This omission is striking
because the sector carries

Panwar et al. / Journal of Applied Science and Technology Trends Vol. 06, No. 02, pp. 408 –426 (2025)

409
distinctive characteristics that set it apart from the broader green
industry [3]. Unlike general green products, personal care items
are applied directly to the body, raising concerns about safety
and ingredient transparency [4]. At the same time, aesthetic and
sensory dimensions (like texture, scent, even packaging appeal)
intersect with ethical considerations, producing a complex
impact of drivers that are not easily reduced to environmental
concern alone. So, the drivers of online green personal care
purchases may differ substantially from other segments, making
focused study on this category necessary. By viewing these
behavioural drivers as inputs and outputs in a computational
pipeline, values can be turned into measurable signals, and
interventions can be organized as modular layers within the
system.
On a practical level, personal care products occupy a
distinctive place in everyday routines. Dodson et al. (2021), for
instance, reported that women typically use a median of 8
personal care items each day, while some incorporate as many
as 30 into their regimen [5]. More recent work suggests that men
are also increasingly demanding the green cosmetics market,
noting a steady rise in demand [6]. These trends show the
importance to study the GPCP purchases, especially on e -
commerce platforms where the absence of physical interaction
introduces unique decision -making constraints [7].
Computational approaches such as pipeline architectures, SEM-
based system design, and algorithmic feedback loops enable the
monitoring of how values shape actual purchase behaviour.
Prior green -consumption models, such as the Theory of
Planned Behaviour (TPB), the Norm Activation Model (NAM),
and the Value –Belief–Norm (VBN) theory, have offered
valuable insights into sustainable consumer choices. These
frameworks explain attitudinal, normative, and value -based
drivers of behaviour. However, they remain largely de scriptive
and are rarely connected to system-level implementation.
In parallel, existing sustainability and e -commerce
architectures have largely concentrated on optimizing technical
or operational dimensions rather than addressing the underlying
drivers o f sustainable consumer behaviour. Recommender -
system architectures have improved prediction through
collaborative filtering, content -based methods, and hybrid
techniques. For instance, sustainability -oriented designs have
introduced digital nudges to promote greener product selection
[8], while others have optimized algorithmic efficiency to
reduce the energy and carbon footprint of recommender training
[9]. Blockchain -based solutions have also been proposed to
ensure traceability and verification of green claims [10]. Yet,
these architectures remain limited to surface-level optimization,
such as recommending greener items, improving transparency,
or lowering technical costs. However, they fail to address the
deeper issue of why consumers often struggle to t ranslate pro-
environmental attitudes into actual purchases.
By contrast, the pipeline proposed in this study is novel in
three key ways. First, it operationalizes the Value –Attitude–
Behavior (VAB) framework by mapping values, attitudes, and
intentions into  modular layers that can guide e -commerce
system design. Second, it focuses only on empirically significant
determinants, making the pipeline more parsimonious and
practically implementable than broader models or architectures
that rely on weak predictors. Third, it is tailored specifically to
GPCPs, a category often overlooked in sustainability research
but uniquely important due to its intimate, health -related, and
emotional dimensions. Together, these contributions distinguish
the proposed pipeline from existing sustainability and e -
commerce architectures and position it as a blueprint for
behaviourally intelligent system design.
The study is guided by two primary objectives:
To empirically examine how consumption and pro -
environmental values shape sustai nable online consumer
behaviour through the Value –Attitude–Behaviour framework,
using SEM analysis.
To propose a computational pipeline architecture that
operationalizes these behavioural determinants into system
components.
To achieve these aims, the structure of the paper is arranged
as follows. Section 2 introduces the theoretical foundation and
formulates research hypotheses. Section 3 details the
methodological approach used to examine proposed
relationships. Section 4 reports the results of the empiri cal
investigation, while Section 5 discusses these findings in
relation to prior studies, outlines limitations, and suggests
directions for future research. Lastly, Section 6 concludes the
study by summarizing its main contributions.
II. THEORETICAL FRAMEWORK AND HYPOTHESES
A. The Pipeline Concept in Digital Consumer Behaviour
In computational system design, a pipeline is a sequence of
stages where inputs are encoded, transformed, and evaluated
into outputs. Each stage performs a specific function, passing its
results forward to the next stage, ensuring both modularity and
transparency in how data and interactions are processed. In the
context of sustainable e -commerce, the pipeline provides a
formal architecture for translating abstract constructs such as
values, attitudes, and intentions into observable digital signals
that can be monitored, modelled, and optimized.
This study first seeks to identify the relationships between
consumer values and green purchasing behavior in e-commerce
platforms, and then to trans late these relationships into a
structured pipeline design. Framing digital commerce as a
pipeline allows behavioral theories to be built into system
design. Values can become encoded inputs, for instance through
sustainability surveys, clickstream metadat a indicating
preference for organic products, or eco -label interactions such
as consumers filtering for “Fair Trade” certifications. Attitudes
are represented as evaluative states, which can be inferred from
engagement patterns (e.g., time spent comparing carbon-neutral
products versus conventional alternatives) or micro -surveys
embedded post -purchase to gauge perceptions of brand
responsibility. Intentions serve as commitment nodes, visible
through low-friction trial actions such as adding an item to a
Wishlist on Amazon, subscribing to a “back -in-stock”
notification, or opting into a free trial of a digital service like
Premium versions. Behaviors then constitute the measurable
outputs, most directly observable in completed purchases, repeat
subscriptions (e.g., auto-replenishment of household items on

Panwar et al. / Journal of Applied Science and Technology Trends Vol. 06, No. 02, pp. 408 –426 (2025)

410
Instacart), or participation in loyalty programs that reflect
sustained commitment.
Beyond behavioral mapping, recent research has also
applied computational and AI -based methods to sustainable
consumption. M achine learning classifiers and clustering
algorithms have been used to predict green purchase
propensities and segment consumers by sustainability
preferences [11, 12]. Computational approaches, including
reinforcement learning (RL) are also being utilized to encourage
sustainable consumption behaviors. In particular, Huynh et al.
(2022) demonstrate how RL can optimize marketing
interventions for sustainable products through personalization
and behavioral modeling, leading to improved adoption
outcomes [13 ]. Natural language processing techniques have
been applied to analyze consumer reviews of eco -friendly
products, revealing insights into sustainability perceptions and
product design optimization [14]. Explainable AI has also been
employed to advance sust ainable growth by enhancing trust,
transparency, and data -driven decision -making in business
contexts [15]. While these approaches demonstrate the technical
feasibility of embedding sustainability into digital commerce
pipelines, they tend to remain isolat ed focusing on prediction,
personalization, or verification in silos. The present study
extends this line of work by embedding such computational
capacities within a Value–Attitude–Behavior framework, where
psychological determinants are mapped directly on to pipeline
stages for systematic implementation.
The pipeline structure also enables modular intervention:
platform designers can insert various nudges at specific stages.
This aligns with dual -process theories of persuasion, which
argue that interventions are most effective when targeted at the
right processing stage - peripheral cues at early stages, central
arguments when attitudes are being formed, and commitment
devices when intentions are being consolidated.
B. Green Consumer Behaviour in the E-Commerce Context
Digital commerce platforms can be conceptualized as
information-processing systems, in which consumer behavior
emerges from data flows, interaction signals, and algorithms. In
this context, understanding green consumer behaviour requires
not only behavioural insights but also system design strategies
that reduce information asymmetries.
Green consumer behaviour is often described as a key driver
in steering markets toward more sustainable practices [ 16].
Within this broader movement, the personal care industry
appears to have significant growth in the range of eco-conscious
alternatives. Consumers seem increasingly drawn to products
framed as safe, ethically produced, and environmentally
responsible
Simultaneously, the rise of digital retail has complicated this
landscape. E -commerce offers convenience, greater variety,
wider accessibility, and efficiency of purchase without physical
constraints. This makes it a primary channel for GPCPs. Yet
these features also introduce a set of difficulties. Sustainable
decision-making may be undermined when buyers cannot
handle items directly or scrutinise packaging in person. As
McLoughlin et al. (202 4) observed, the absence of tactile
inspection limits verification of quality, authenticity, and
ecological claims. By contrast, Traditional retail settings allow
for sensory evaluation and face -to-face consultation, both of
which can reinforce consumer tr ust [ 17]. In digital spaces,
however, assessments are mediated by textual descriptions,
symbolic branding, and the often-uneven authority of third-party
reviews [18]. Designing e-commerce pipelines allows proxies to
be filtered, weighted, and presented to reduce cognitive burden
and support sustainable decision-making.
E-commerce environments are not neutral spaces; they are
shaped by persistent information asymmetry. Consumers
frequently encounter overlapping or even contradictory
sustainability claims, but the means of verifying these claims are
often limited or opaque [1 9]. In such contexts, factors like
perceived value, trust, and a certain level of digital literacy
appear to play an outsized role in guiding green purchasing
behaviour. From a system -design standpoint, these challenges
can be addressed by encoding values, attitudes, and trust -
building mechanisms into digital pipelines that structure
consumer interactions, algorithmic nudges, and feedback loops.
Online platforms, can be harnessed to promote  sustainable
products through curated digital interactions that highlight
ecological benefits or by embedding green values into the
broader shopping experience [20]. Yet digital mediation can also
magnify barriers. The absence of physical cues, coupled with the
sheer volume of information, may foster uncertainty, scepticism,
or decision fatigue. Framing consumer uncertainty in
computational terms allows these frictions to be treated as data-
processing bottlenecks, addressable through system -level
interventions.
C. The Value–Attitude–Behaviour (VAB) Framework
The VAB framework can be treated as a layered processing
model where values act as system inputs, attitudes as
intermediate states, intentions as commitment nodes, and
behaviour as measurable outputs. This makes it naturally suited
for implementation within a digital pipeline architecture. It was
first articulated in the field of psychology and sociology [21]. At
its core, the model suggests that individuals’ underlying values
influence their attitudes, whic h then guide intentions and,
eventually, observable behaviours. Consumer researchers have
found this structure useful, particularly when trying to make
sense of decision -making processes that appear fragmented or
inconsistent at first glance.
In green consumption, the framework is especially useful for
investigating how ecological values and beliefs might translate
into favourable orientations toward sustainable products and
services [22-24]. Attitudes and intentions mediate this gap by
highlighting where interventions may be targeted. When
integrated into a computational architecture, VAB determinants
can be logged as structured signals (clicks, hovers, micro -
surveys), processed as intermediate states (attitudes and
intentions), and linked causally to outc omes (purchases). This
allows both explanatory modelling and real -time adaptive
interventions.
This study adopts the Value –Attitude–Behaviour (VAB)
theory because it aligns more effectively with data -driven
models in digital commerce. Compared with other b ehavioral
theories such as the TPB, NAM, or VBN theory, VAB offers a
more parsimonious and computationally compatible structure

Panwar et al. / Journal of Applied Science and Technology Trends Vol. 06, No. 02, pp. 408 –426 (2025)

411
for digital commerce. Constructs like subjective norms,
perceived control, or moral obligation are valuable in offline
contexts but are challenging to infer from online behavioral data.
By contrast, values and attitudes can be proxied through
measurable signals such as eco -label interactions, product -
quality checks, or engagement with sustainability content. These
online traces reveal consumers’ underlying priorities and can be
systematically captured within the platform. Th is makes the
sequential flow of values → attitudes → intentions → behaviour
particularly well suited for integration into pipeline
architectures, where abstract psychological constructs must be
translated into observable system states.
D. Consumption Values
Consumption values represent the benefits or utilities that
people seek when making consumption decisions. This study
focuses on four consumption values to examine their impact on
e-commerce platforms. These are functional quality value
(FQV), functional price value (FPV), emotional value (EMV)
and social value (SCV).
FPV refers to how consumers judge the value they receive
from the price paid. This shows how cost -effective they find a
product or service. This value strongly affects brand loyalty and
purchase intent, as buyers compare prices with perceived
benefits [25]. High prices are often seen as a main barrier in
green product settings [26, 27]. But consumers may find green
products worth the higher cost if they see additional benefits
related to health, environmental or ethics [28]. For GPCPs, this
trade-off becomes especially significant as these items are
compared to widely available non -green alternatives. H igher
prices may be more acceptable to consumers who value non -
toxic ingredients, ethical sourcing, and skin safety. Also,
perceived price value in online settings might become a decisive
factor because price comparisons are immediate and product
experience is limited. When consumers believe the price aligns
with perceived benefits, they are more likely to complete the
purchase. Therefore:
H1: “Functional Price Value has a significant relationship
with Green Purchase Attitude.”
On the other hand, FQV perta ins to the consumer's
perception of the quality and performance of a product or
service. It encompasses attributes such as reliability, quality, and
effectiveness [2 9]. Functional value is especially critical in
green product consumption because eco-friendly alternatives are
sometimes perceived as less effective than conventional
products [ 30]. For GPCPs, functional quality is even more
essential due to the intimate and health -related nature of their
use. Consumers consider factors like effectiveness, skin
compatibility, and ingredient transparency, all of which strongly
influence trust and satisfaction [4, 31, 32] . In online contexts,
where consumers cannot physically evaluate products -
functional value becomes a decisive factor. Digital shoppers rely
heavily on descriptions, third -party certifications, and user
reviews to assess performance [ 33], making functional quality
perception central to their decision-making. Therefore:
H2: “Functional Quality Value has a significant
relationship with Green Purchase Attitude.”
SCV refers to the benefits a product provides by improving
consumers’ social standing or self-perception within their social
context [30]. In the context of green consumption, it plays a role
when consumers believe that buying eco -friendly prod ucts
signals responsibility, awareness, or prestige [ 34]. For GPCPs,
this signalling effect may be even more significant, as personal
grooming choices such as using organic shampoos or cruelty -
free cosmetics are often associated with ethical self -expression
and visible lifestyle choices. In digital settings, social value
becomes stronger through social media, peer sharing and
influencer support. Consumers may choose GPCPs not just for
personal use, but to earn social approval, match with identity -
based groups, and shape their online image. Therefore:
H3: “Social Value has a significant relationship with Green
Purchase Attitude.”
EMV refers to the affective states that a product can evoke,
feelings such as pride, pleasure, or even a more subdued sense
of satisfaction [35]. In the context of green consumption, this
affective dimension often appears to stem from the alignment
between purchases and ethical or environmental commitments
[36]. In particular, GPCPs seem capable of generating strong
emotional responses. This may be because they intersect with
aspects of self -identity, body image, and modes of self -
expression in ways that utilitarian green products for example,
energy-efficient appliances rarely do [ 37]. In other words,
GPCPs are not simply consumed for their functional properties;
they are entangled with lifestyle aspirations and broader
wellness narratives. In digital retail environments, the affective
pull of these products may be heightened. Influencer marketing,
visual brand storytelling, and other forms of digitally mediated
persuasion can amplify emotional resonance, sometimes
blurring the line between personal expression and commercial
promotion [38]. For these reasons, it seems plausible that EMV
plays a particularly salient role in shaping consu mer responses
to online GPCPs. Therefore,
H4: “Emotional Value has a significant relationship with
Green Purchase Attitude.”
E. Pro-Environmental Values
Pro-environmental values show a consumer’s intent to lower
their environmental impact, protect natural res ources and
support ethical brands. These values often lead to a higher
chance of buying GPCPs. Following earlier studies, this
research uses three key dimensions to measure pro -
environmental values: Environmental Concern (ENC),
perceived environmental know ledge (PEK) and perceived
consumer effectiveness (PCE) [39].
ENC refers to the extent to which a person understands
environmental problems and feels responsible to act against
them. It shows both awareness of environmental damage and
readiness to take step s that reduce harm [ 40]. It is a core
component of pro-environmental values and is strongly linked
to green consumer behaviour [40, 41] . For GPCPs, this concern
can lead consumers to choose items that are cruelty -free,
ethically sourced, or packed in biod egradable materials. Such
choices help them express their environmental values through
daily grooming habits. Even online, where sensory engagement

Panwar et al. / Journal of Applied Science and Technology Trends Vol. 06, No. 02, pp. 408 –426 (2025)

412
is limited, these consumers pay attention to eco -labels,
certifications, and sustainability claims. Therefore:
H5: “Environmental Concern has a significant relationship
with Green Purchase Attitude.”
PEK is the extent to which a consumer believes they know
about environmental issues, sustainable practices, and the
impact of their own consumption. It differs from  actual or
objective knowledge, which is based on factual accuracy.
Perceived knowledge, even if not completely accurate, can
strongly influence attitudes and behaviours toward sustainability
[42]. It plays a foundational role in shaping pro -environmental
attitudes and behaviour. As people who feel more
knowledgeable are more likely to notice green products and
make sustainable choices [ 43]. For GPCPs, this knowledge
helps consumers judge ingredients, understand production
impacts, and interpret sustainabil ity certification. In online
shopping such knowledge becomes critical as physical checks
are not possible. It helps consumers trust credible green claims,
lowers uncertainty and increases their willingness to buy.
Therefore:
H6: “Perceived Environmental Knowledge has a significant
relationship with Green Purchase Attitude.”
PCE refers to an individual’s belief that their personal
actions can help solve environmental problems. It is a critical
factor in understanding consumer behaviour particularly in the
context of sustainability [ 44]. It reflects a sense of individual
responsibility and self -efficacy in driving environmental
change. Prior studies consistently found that individuals with
high PCE are more likely to engage in green behaviours,
including ethic al consumption, waste reduction and green
purchase [ 45]. In online settings, where consumers cannot
physically inspect products or verify the authenticity of green
claims, trust becomes a major barrier. Consumers often rely on
internal beliefs such as PCE,  to justify sustainable purchasing
decisions. This reliance is especially relevant in the context of
GPCPs which involve health -sensitive and ethically charged
factors like ingredient safety, animal testing and
biodegradability. When external cues are limi ted, people who
strongly believe that their purchases matter are more likely to
buy GPCPs online. Therefore:
H7: “Perceived Consumer Effectiveness has a significant
relationship with Green Purchase Attitude.”
The overall system can be conceptualized as a p ipeline in
which encoded values are processed through evaluative nodes
(attitudes), commitment nodes (intentions), and behavioural
outputs (purchases). In this formulation, mediators such as GPA
and GPI serve as intermediate processing layers, enabling bot h
prediction and intervention. Overall, Consumption values focus
on personal benefits like usefulness, emotional satisfaction and
social recognition. Whereas pro -environmental values address
broader ethical concerns of sustainability and responsibility.
Consumers support eco -friendly products in attitude but often
do not purchase them [46]. Connecting these two value domains
is key to reducing the value–action gap. Understanding this link
is important for building effective digital marketing and policy
measures that encourage sustainable consumption. Fig. 1
provides the conceptual model proposed by the study.
Digital marketplaces create challenges such as limited
product tangibility and overwhelming information, which can
affect how values turn into green purchase behaviour (GPB). To
explain this process, the present model uses green purchase
attitude (GPA) and green purchase intention (GPI) as mediators,
in line with theories like the Theory of Planned Behaviour [39].
These mediators help explain how persona l values are
internalized into behavioural motivation and, ultimately, online
purchase actions. Therefore, the following hypotheses were
developed:
H8: “Green Purchase Attitude has a significant relationship
with Green Purchase Intention.”
H9: “Green Purchase Intention has a significant
relationship with Green Purchase Behaviour”.

Fig. 1. Conceptual model (Author)

Panwar et al. / Journal of Applied Science and Technology Trends Vol. 06, No. 02, pp. 408 –426 (2025)

                        413
III. METHODOLOGY
A. Research Design
The study relied on a quantitative design to explore how
consumer values might influence the adoption of GPCPs
through e -commerce channels. Data were gathered using a
structured questionnaire, which provided a relatively
standardized way of capturing consumer responses. For the
analysis, Structural Equation Modelling (SEM) was employed.
This method has been widely recommended when dealing with
complex causal frameworks, particularly those that involve
multiple latent constructs and interrelated pathways [4 8].
Although other techniques were possible, SEM appeared
especially useful here because it allows for simultaneous testing
of measurement and structural relationships.
B. Sampling Strategy and Participants
The sampling process was purposive, reflecting the need to
reach participants with prior experience purchasing GPCPs
online. T o achieve this, screening questions were embedded
within the survey to filter out ineligible respondents. In terms of
sample size, the study drew on the “10-times rule” proposed by
Hair et al. (2014), which suggests a minimum of 200 cases given
the 10 late nt variables and 9 hypothesised paths in the model
[48]. The study also used power analysis to validate sample size
adequacy. Power analysis determines the minimum number of
cases required to detect a specified effect size with a given
statistical power (commonly 0.80) at a significance level of 0.05.
Using G*Power 3.1.9.7, the analysis indicated that a sample of
at least 262 respondents would be sufficient for the structural
model. With 302 valid responses retained, the sample size of this
study comfortably exceeds both the 10-times rule and the power
analysis threshold, ensuring robustness for hypothesis testing. In
terms of geographic distribution, all respondents were based in
India, with both urban (65.23%) and rural (34.76%)
representation across sever al states. Recruitment channels
included emails, professional networks, and social media groups
(e.g., WhatsApp, LinkedIn, Instagram), with an emphasis on
communities likely to include environmentally conscious
consumers. Questionnaire also included screen ing questions
ensuring access to participants who had demonstrable
experience with online GPCP purchases, while also capturing
diversity in socio -demographic characteristics. After data
cleaning procedures such as removing incomplete or
inconsistent respon ses, 302 relevant responses cases were
retained.
C. Instrument Development
The questionnaire was structured into distinct sections,
beginning with demographic information and then moving into
the main research constructs. Demographic items included
gender, a ge, education, and income, providing context for
consumer behaviour. Measures of pro -environmental values
drew on three constructs PCE, ENC, and PEK each represented
by three items adapted from earlier work [49, 50 ] . The decision
to rely on these constru cts reflects their repeated use in prior
sustainability research. In terms of consumption values, the
study adopted four dimensions commonly discussed in
consumer behaviour research: FPV, FQV, EMV, and SCV. Each
was measured with three items, drawing from validated scales
in existing literature [51, 52] . Finally, the behavioural side of
the framework was operationalised through GPA, GPI, and
GPB. These were measured with five items each, adapted from
several studies that have sought to connect attitudinal measures
to actual consumer practices [ 51-56] . Though it does not
necessarily capture the full breadth of “green” value
orientations, slight modifications were made to fit in the context
of study.
D. Validity and Reliability Procedures
To strengthen the credibility of the instrument, a multi-stage
validation process was followed. In the first stage, six scholars
with expertise in marketing and consumer behaviour reviewed
the questionnaire. Their assessment focused on face and content
validity, and several items were revised in response to concerns
about clarity and nuance. This expert review is often treated as
routine, but it arguably provides only a partial safeguard, as
consensus among reviewers does not guarantee conceptual
precision.
A second stage invol ved a pilot test with 50 participants,
which served two purposes: to evaluate the intelligibility of the
items and to flag potential issues in wording or structure.
Although pilots cannot replicate full study conditions, they help
identify ambiguities rese archers may overlook. Finally, a
preliminary SEM analysis was carried out using the pilot data.
This step helped assess the fit of the measurement model and
provided early evidence of reliability and construct validity.
While the pilot results were encouraging, it should be noted that
findings based on such a small sample may not always be stable;
nonetheless, they offered a degree of reassurance before moving
forward with the full-scale survey.
E. Data Analysis
The data were analysed using Structural Equation Modelling
(SEM), a method well-suited for handling complex relationships
between latent constructs. The analysis proceeded in two stages.
First, the measurement model was tested through Confirmatory
Factor Analysis (CFA). Reliability was gauged using
Cronbach’s alpha alongside composite reliability, while
convergent validity was examined through factor loadings and
the average variance extracted (AVE). Discriminant validity
was also checked, with the goal of ensuring that the constructs
were sufficiently distinct from one another.
In the second stage, the structural model was tested to
evaluate the hypothesised paths. Model fit was assessed using
indices commonly cited in SEM research. Path coefficients were
examined for statistical significance and the explained variance
(R²) of the endogenous constructs was reported as an indicator
of predictive strength. This procedure examined how consumer
values shape GPCP adoption in online marketplaces.
IV. RESULTS
A. Descriptive Statistics and Sample Characteristics
Table I  summarizes the demographic profile of the 302
respondents. The sample comprised a slightly higher proportion
of females (55.96%) compared to males (44.03%). A significant
majority resided in urban areas (65.23%), while 34.76% were
from rural locations. In  terms of educational attainment, most
participants held either a postgraduate (48.01%) or graduate

Panwar et al. / Journal of Applied Science and Technology Trends Vol. 06, No. 02, pp. 408 –426 (2025)

414
degree (41.72%). The age distribution skewed towards younger
individuals, with 65.23% aged between 18–27 years and 26.49%
between 28–43 years. Respondents a bove 44 years constituted
less than 10% of the total sample. Regarding annual income, a
majority (56.29%) reported earnings up to ₹2,50,000, while
25.16% earned between ₹2,50,000 –₹5,00,000. Higher income
brackets were less represented.
TABLE I.  DEMOGRAPHIC  CHARACTERISTICS OF THE
RESPONDENTS
Demographic variables Frequency Percent
Gender
Female 169 55.96
Male 133 44.03
Region
Rural 105 34.76
Urban 197 65.23
Qualifications
Secondary 9 2.98
Higher Secondary 11 3.64
Doctoral 11 3.64
Graduate 126 41.72
Postgraduate 145 48.01
Age
18- 27 years 197 65.23
28- 43 years 80 26.49
44- 59 years 18 5.96
60 and above 7 2.31
Annual Income
0 to Rs. 2,50,000 170 56.29
Between Rs. 2,50,000- 5,00,000 76 25.16
Between Rs. 5,00,000- 7,50,000 29 9.6
Between Rs. 7,50,000- 10,00,000 4 1.32
Between Rs. 10,00,000- 12,50,000 5 1.65
Between Rs. 12,50,000- 15,00,000 4 1.32
Above Rs. 15,00,000 14 4.63
Although the survey was broadly distributed across multiple
channels, a purposive sampling strategy was applied, and
respondents without prior experience purchasing GPCPs online
were excluded. As a result, the final sample was predominantly
younger, urban, and more educated a demographic segment that
is also the most active in online green personal care prod uct
consumption.

B. Measurement Model Evaluation
Reliability and validity of the constructs were first assessed
and the results are shown in Tables II and VI. As shown in Table
VI, all constructs exceeded the recommended thresholds for
internal consistency, with Cronbach’s alpha values exceeding
the recommended threshold of 0.70 [ 57]. AVE values for all
constructs were above the 0.50 threshold [ 58], indicating
adequate convergent validity. Factor loadings were above 0.70
for all items except one (PCE2), which  was subsequently
removed to improve construct validity. The constructs show
strong reliability and validity.
To test the potential influence of common method bias,
Harman’s single -factor test was conducted as an initial
diagnostic. The unrotated factor s olution revealed that the first
factor accounted for less than 40% of the total variance, which
is less than the threshold value of 50% [ 59]. Variance Inflation
Factor values were also examined to detect any issues related to
multicollinearity among the in dicators. Its values ranged from
1.00 to 3.81, all below the conservative threshold of 5 [57]. This
means the indicators are free from multicollinearity concerns.

TABLE II.  FORNELL-LARCKER CRITERION
  EMV ENC FPV FQV GPA GPB GPI PCE PEK SCV
EMV 0.884
ENC 0.549 0.843
FPV 0.599 0.333 0.889
FQV 0.695 0.401 0.675 0.862
GPA 0.598 0.436 0.501 0.569 0.903
GPB 0.674 0.558 0.544 0.611 0.591 0.827
GPI 0.701 0.512 0.506 0.564 0.781 0.726 0.866
PCE -0.147 -0.079 -0.352 -0.14 -0.184 -0.261 -0.177 0.909
PEK 0.58 0.587 0.446 0.571 0.532 0.637 0.522 -0.219 0.817
SCV 0.633 0.374 0.649 0.581 0.486 0.543 0.514 -0.427 0.47 0.863
 The Fornell -Larcker criterion was used to e valuate
discriminant validity ( Table II). Based on this criterion, a
construct’s square root of Average Variance Extracted (AVE)
must exceed its largest correlation with any other construct [58].
The diagonal elements represent the square roots of AVE and
the off-diagonal elements represent inter-construct correlations.
As shown in the Table III, all diagonal values exceed the
corresponding off-diagonal correlations in their respective rows
and columns. The findings confirm discriminant validity, as
each construct is conceptually and empirically distinct.

Panwar et al. / Journal of Applied Science and Technology Trends Vol. 06, No. 02, pp. 408 –426 (2025)

415
C. Structural Paths and Hypotheses Tests
The structural model was evaluated using bootstrapping with
5,000 resamples to assess the significance of hyp othesized
relationships. Table III presents the standardized path
coefficients, associated t -statistics, an d p -values. Among the
antecedents of Green Product Attitude (GPA), Functional
Quality Value (FQV) (β = 0.174, t = 2.294, p = 0.022), Perceived
Environmental Knowledge (PEK) (β = 0.177, t = 2.262, p =
0.024), and Emotional Value (EMV) (β = 0.241, t = 2.747,  p =
0.006) has shown a significant influence. Conversely,
Environmental Concern (ENC) (β = 0.079, p = 0.228), Perceived
Consumer Effectiveness (PCE) (β = -0.025, p = 0.618), Social
Value (SCV) (β = 0.047, p = 0.524), and Functional Price Value
(FPV) (β = 0.096, p = 0.232) did not demonstrate significant
effects on GPA. Fig. 2 presents the structural model.
In the outcome model, Green Product Attitude showed a
strong positive effect on Green Purchase Intention (β = 0.781, t
= 25.019, p < 0.001), which in tu rn significantly influenced
Green Purchase Behavior (β = 0.726, t = 23.125, p < 0.001). The
results confirmed the central role of attitude and intention in
purchase outcomes.
TABLE III.  PATH COEFFICIENTS

Original
sample
Sample
mean
Standard
deviation
T
statistics
P
values
EMV ->
GPA
0.241 0.237 0.088 2.747 0.006
FPV -> GPA 0.096 0.092 0.080 1.196 0.232
FQV -> GPA 0.174 0.177 0.076 2.294 0.022
GPA -> GPI 0.781 0.781 0.031 25.019 0.000
GPI -> GPB 0.726 0.726 0.031 23.125 0.000
PCE -> GPA -0.025 -0.028 0.050 0.498 0.618
ENC -> GPA 0.079 0.082 0.065 1.207 0.228
PEK -> GPA 0.177 0.176 0.078 2.262 0.024
SCV -> GPA 0.047 0.050 0.073 0.637 0.524

Fig. 2. Structural Model (Author)
Note: Numbers on paths represent standardized path coefficients (β). Values in grey adjacent to paths are p -values. Circles show latent constructs; rectangles
represent observed indicators. R² values are reported inside endogenous constructs (GPA, GPI, GPB) and indicate the proportion of variance explained
Overall, these findings offer partial empirical support for the
proposed model. While selected consumption values including
functional and emotional significantly shape green product
attitudes, from pro -environmental values, PEK demonstr ates
direct effects in this context. Additionally, GPA significantly
predicted GPI, which in turn significantly influenced GPB.
These findings support the value-attitude-behaviour framework,
highlighting the mediating role of attitude and intention in
translating values into sustainable behaviour.
Table IV presents the coefficients of determination (R2). The
model explains 44.7% of the variance in Green Product Attitude
(GPA), 61.0% in Green Purchase Intention (GPI), and 52.7% in
Green Purchase Behaviour (G PB). Adjusted R² values
confirmed model stability. The predictors explain a substantial
share of variance in the outcomes. In particular, the explanatory
power is highest for GPI (R² = 0.610), followed by GPB (R² =
0.527), supporting the mediating role of intention in the value-
attitude-behaviour sequence.
TABLE IV.  COEFFICIENT OF DETERMINATION (R²)
  R-square R-square adjusted
GPA 0.447 0.434
GPB 0.527 0.525
GPI 0.61 0.609

In addition to explanatory power, model fit was assessed
using the Standardized Root Mean Square Residual (SRMR).
The SRMR value for the saturated model was 0.059, which is
below the recommended threshold of 0.08, indicating an
adequate measurement model fit. The SRMR for the estimated
model was 0.110, indicating a slightly weaker structural fit, with
values between 0.08 and 0.10 generally considered to reflect a

Panwar et al. / Journal of Applied Science and Technology Trends Vol. 06, No. 02, pp. 408 –426 (2025)

416
mediocre fit [60]. However, as PLS-SEM prioritizes predictive
accuracy over absolute model fit, and given the satisfactory R²
values obtained, the model was retained due to its strong
theoretical foundation and empirical adequacy.
V. DISCUSSION
A. Interpretation of Significant Relationships
The results can be interpreted both behaviourally and as
signals for system design. Significant predictors can be treated
as high-priority modules within a digital pipeline. The analysis
revealed three statistically significant paths within the proposed
model: Functional Quality Value → Green Product Attitude,
Emotional Value →  Green Product Attitude, perceived
environmental knowledge → Green Product Attitude, and the
sequential mediation pathway of Green Product Attitude →
Green Purchase Intention → Green Purchase Behaviour. The
findings provide critical insights into s ustainable decision -
making in the e-commerce context.
The results suggest that FQV has a measurable effect on
GPA (β = 0.174, t = 2.294, p = 0.022). In other words, consumers
appear to weigh the perceived effectiveness of a product
alongside its environmental claims, though this emphasis is not
entirely surprising. For GPCPs in particular, attributes tied to
performance, safety, and reliability often emerge as decisive
factors in shaping evaluations [4, 61]. A moisturizer that feels
ineffective or a shampoo  that fails to deliver basic quality
expectations may undermine the appeal of its eco -friendly
positioning. Conversely, when products are framed as beneficial
for health or skin, consumer attitudes often lean more positively
[62].
At the same time, this does not mean that consumers
automatically privilege functionality over sustainability; rather,
many expect eco -friendly options to deliver both. There is an
implicit demand that environmental responsibility should not
come at the expense of efficacy. A tension that marketers must
navigate carefully. Credibility can be enhanced through signals
such as clinical validations, third-party certifications, or even the
seemingly mundane reassurance of user testimonials. Such
strategies may help consumers reconcile quality concerns with
sustainability commitments. In this sense, functional value
reinforces confidence not just in what the product does, but also
in whether its green claims can be believed.
Similarly, the analysis indicates that EMV exerted a notable
influence on GPA (β = 0.241, t = 2.747, p = 0.006). This finding
points to the increasingly recognized role of affective responses
in how consumers interpret and evaluate environmentally
friendly products, though the strength of this  relationship may
vary across contexts. In online settings where buyers cannot
physically inspect goods, emotional cues seem to take on added
weight. A feeling of personal satisfaction, or even the perception
of contributing to broader environmental goals,  can become a
powerful motivator. Prior work shows that green products
emphasizing natural ingredients, ethical sourcing, or cruelty -
free practices effectively elicit emotional responses [63, 64 ]. At
the same time, these responses are not purely about imm ediate
gratification; some consumers may also see environmentally
conscious purchasing as tied to identity, pride, or moral
consistency [37, 65] . Taken together, the results suggest that e-
retailers might benefit from foregrounding emotional appeals in
their messaging, for instance by highlighting alignment with
personal values or the “feel -good” dimension of sustainable
consumption..
PEK exerted a moderate effect on GPI (β = 0.177, t = 2.262,
p = 0.024). In practical terms, consumers who believe they
understand environmental issues are more inclined to view
GPCPs positively. This does not necessarily mean that objective
knowledge drives behaviour; rather, the perception of being
informed seems to matter as much, if not more. Prior studies
have pointed out that environmental knowledge often influences
consumer decision-making indirectly by shaping attitudes first,
which are then filtered into intentions and eventual behaviour
[66, 67].
Online marketplace complicates this dynamic. In contexts
where product claims cannot easily be verified, consumers often
lean on their own perceived expertise to judge whether labels
such as “organic,” “biodegradable,” or “cruelty-free” should be
trusted. Some may also be aware of broader concerns about
health and environmental impact, which, as Kaur et al. (2024)
suggest, can reinforce a preference for eco-friendly alternatives
[68].  This highlights the role of consumer education:
Certifications, impact facts, and ingredient details can bolster
credibility and attitudes.
The paths from attitude to intention and intention to
behaviour were strongly supported (β = 0.726, t = 23.125, p =
0.000). This corroborates the VAB hierarchy [69-71] . The
sequence confirms that positive evaluations of GPCPs translate
into stronger purchas e intentions, which in turn lead to actual
buying behaviour. The high explanatory power of intention (R²
= 0.615) and behaviour (R² = 0.593) further confirms the
importance of intention as a psychological mechanism that helps
translate green product attitudes into actual purchase behaviour,
particularly in digital contexts. This strong link between attitude,
intention and behaviour reflects classical behavioural theories
(e.g., the Theory of Reasoned Action and TPB). This assert that
intention is the most i mmediate predictor of behaviour [47]. In
the case of GPCPs, once a consumer forms a purchase intention
driven by positive attitudes, emotional value, and perceived
knowledge, they are likely to act on it, especially in an e -
commerce setting where friction to purchase is low (e.g., fast
checkout, product recommendations, promotions).
Overall, online green purchases are driven more by practical
factors like how useful the product is, how well it performs, and
consumer’s perceived knowledge, and emotions than by abstract
ideals. These factors appear to exert a greater influence on
behavioural outcomes than ideologically rooted values such as
environmental concern or ethical commitment. Thus, while
consumers may express pro-environmental attitudes, their actual
purchasing behaviour within digital environments is more
strongly shaped by functional value perceptions and emotions
than by abstract ecological ideals.
While this study deliberately focused on GPCPs because of
their unique intersection of safety, ingredient transparency, and
daily-use intimacy, some of the mechanisms identified are not
entirely confined to this sector. For example, the importance of

Panwar et al. / Journal of Applied Science and Technology Trends Vol. 06, No. 02, pp. 408 –426 (2025)

417
functional quality value reflects a broader expectation that green
products whether in personal care, house hold goods, or food
should not compromise on performance. Likewise, emotional
value and perceived environmental knowledge are likely to
influence sustainable choices across categories, even if the
strength of these drivers varies by context. Thus, although
GPCPs warrant independent study, our findings also suggest
potential points of convergence that future cross -category
research could explore to test external validity.
B. Non-Significant Effects and Possible Explanations
 Several hypothesized relationships w ere not supported by
the data. SCV, ENC, PCE, and FPV do not demonstrate
statistically significant effects on green product attitude.
 The hypothesized relationship between FPV and GPA
was not supported (β = 0.096, t = 1.196, p = 0.232). This
indicates that consumers’ perception of whether a GPCP offers
good value for its price does not significantly shape their attitude
toward purchasing it. While favourable price assessments were
expected to encourage positive purchase attitudes, the data
suggest otherwi se. Instead, consumer attitudes appear more
strongly influenced by perceived product quality. This diverges
from prior studies where price value emerged as a significant
predictor of sustainable consumption, particularly in categories
where cost differences are more salient [26,27]. One explanation
is that in online GPCP markets, prices are relatively transparent
and easily compared across sellers, reducing the role of
perceived price value as a differentiating factor. In the context
of GPCPs, consumers may  prioritize attributes such as social
support, safety, and environmental impact over affordability.
However, financial scarcity can shift priorities toward
affordability, thereby reducing the likelihood of choosing green
options [72]. Instead, higher prices may even be associated with
superior quality, ethical practices, or safer ingredients [ 73].
Consequently, brands in this space should avoid competing
primarily on price and instead focus on communicating product
quality, emotional benefits, and sustainability commitments
The hypothesized relationship between SCV and GPA is not
supported (β = 0.047, t = 0.637, p = 0.524). This indicates that,
in the online context, social approval or the opinions of others
do not significantly shape consumers’ attitudes toward GPCPs.
A likely explanation is that personal care routines are private and
individualized, making them less visible to others and therefore
less influenced by social recognition. As a result, their adoption
tends to be driven more by personal comfort and perceived
benefits [74]. Moreover, personal care needs, such as skin type,
hair texture, and sensitivity vary greatly between individuals,
further reinforcing the personalized nature of product choices
[75]. As a result, consumers may not rely heavily on peer
recommendations or influencer endorsements, perceiving them
as less relevant or trustworthy for their specific needs. This
weakens the impact of social proof, a key component of social
value. Prior studies in offline or more publicly visible produc t
categories have reported significant effects of social value on
sustainable consumption (e.g., [34]). Our result diverges from
this evidence, suggesting that the inherently private and
individualized nature of GPCPs, combined with the less
observable nature of online shopping, diminishes the signalling
power of social value. This finding implies that social value
cannot be assumed to drive green purchase attitudes unless
visibility is actively created, for example, through eco -badges,
community features, or public sharing options that make
sustainable choices more observable. Consequently, marketing
strategies for GPCPs should move beyond reliance on social
proof. Instead, brands should focus on transparent ingredient
communication, emphasizing safety, eff ectiveness, and
suitability for different skin and hair types. Clear, trustworthy
information empowers consumers to make informed choices
and builds confidence in the product’s value, especially when
personal relevance matters more than social validation.
The hypothesized relationship between ENC and GPA is not
supported (β = 0.079, t = 1.207, p = 0.228). This result diverges
from previous research showing a positive connection between
the variables [76, 77], but aligns with Chu’s (2020) findings in
similar context of skincare products [78]. A possible explanation
lies in the well -documented attitude –behaviour gap, where
expressed concern does not always lead to corresponding
actions. In the digital shopping environment, consumers may
prioritize immediate, t angible factors such as product
trustworthiness, or brand familiarity over broader environmental
ideals. Furthermore, uncertainty about the authenticity of green
claims can reduce the effectiveness of concern-based messaging
[79]. Consequently, marketers should link environmental issues
directly to product -level impacts and present information in a
way that feels credible, emotionally engaging, and directly
relevant to the consumer’s personal needs.  More broadly, this
divergence suggests that in online retail contexts, environmental
concern may function more as a background value than as a
direct predictor of green purchase attitudes. To activate it
effectively, platforms need to translate abstract concern into
verifiable product attributes such as certified  eco-labels,
transparent supply -chain disclosures, or quantified
environmental benefits, that make concern tangible at the point
of decision.
The hypothesized relationship between PCE and GPA is not
supported (β = -0.025, t = 0.498, p = 0.618). This sugges ts that
consumers’ belief in their ability to make a positive
environmental impact through their purchases does not
significantly influence their attitude toward buying GPCPs
online. This diverges from prior research that often identifies
PCE as a strong p redictor of pro -environmental attitudes in
offline settings [45]. A likely explanation is that such products
are typically associated with self -care, aesthetics, and health,
leading consumers to prioritize personal benefits over collective
environmental im pact. Their routine and low -involvement
nature may also reduce the perceived significance of individual
actions. In online shopping specifically, the influence may be
weakened as consumers may struggle to verify the credibility of
sustainability claims [80]. These findings suggest that in online
GPCP contexts, PCE is unlikely to shape attitudes unless
platforms make the impact of individual purchases transparent
and personally meaningful for example, by quantifying
outcomes (“this order saves X litres of wa ter”) or by linking
consumers to collective achievements (e.g., community carbon
offsets).
Collectively, these results suggest that cognitive and
ideological drivers alone may not be sufficient. More robust
informational strategies, supported by credible certification,

Panwar et al. / Journal of Applied Science and Technology Trends Vol. 06, No. 02, pp. 408 –426 (2025)

418
product transparency, emotional appeals and real -world
efficacy, may be needed. These can help turn environmental
values into positive attitudes and action.
VI. PIPELINE ARCHITECTURE FOR SUSTAINABLE ONLINE
CONSUMER BEHAVIOUR
The empirical analy sis in this study confirmed that FQV,
EMV, and PEK significantly shape GPA, which in turn predicts
GPI and, ultimately, GPB.  Non -significant predictors (FPV,
SCV, ENC, and PCE) were excluded from the pipeline
equations because of parsimony and computation al efficiency.
While these findings advance the theoretical understanding of
consumer decision-making, their practical application requires a
computational instantiation that can be embedded within digital
commerce platforms. To this end, we propose a mult i-stage
pipeline architecture that formalizes the Value –Attitude–
Behavior (VAB) framework and the SEM results into a modular
system design. The SEM findings were used to derive equations
(1–4), which then served as the basis for proposing the pipeline
architecture for sustainable online consumer behavior. In the
equations (1-4), u denotes the index for an individual consumer,
as each model operates at the consumer level. Parameter α
(alpha) represents the intercept or constant term, capturing the
baseline value of the dependent variable (such as GPA or GPI)
when predictors are absent. The coefficients β (beta) quantifies
the influence of predictor variables, indicating how much the
dependent variable changes with a one -unit increase in the
predictor, holding other factors constant.
Similarly, γ (gamma) represents the coefficient for control
variables (C ᵤ) in the GPI equation, reflecting the effect of
external or contextual factors such as incentives, trials, or
platform-specific interventions. The term ϵ (epsilon) denotes the
error component that accounts for unexplained variation or noise
in consumer responses. In the augmented model, κ (kappa) is
introduced as a reduced -form coefficient, which consolidates
constants and indirect effects when multiple equati ons are
combined. Collectively, these parameters provide a structured
way to quantify how consumer values, attitudes, and contextual
mechanisms shape intentions and sustainable purchasing
behaviors.
Each stage of the pipeline corresponds to a theoretical
construct validated in this study, operationalized as an
observable system component or intervention layer. This
architecture enables e-commerce systems to measure, influence,
and reinforce sustainable choices in a structured and transparent
manner. Fig. 3 illustrates the overall pipeline.
Stage 0: Data Instrumentation (Foundations)
To construct event streams, to capture proxies of GPA, GPI,
and GPB. GPA proxies include product detail page (PDP) dwell
time, ingredient-info expansions, and short surveys designed to
assess user attitudes and perceptions. GPI proxies include add -
to-cart, wishlist, and subscription trial actions. GPB proxies
include conversions and repeat purchases within a defined
window. These signals are stored in a fused clickstream + survey
dataset, enabling causal and path analyses aligned with the SEM
structure.
Stage 1: FQV Encoding Layer
Structured quality representations such as clinical claims,
dermatological test results, and verified certifications are
encoded as metadata objects lin ked to product entities.
Interactive UI affordances (e.g., badges, expandable quality
panels) expose these signals to consumers. In the pipeline
model, this relationship is captured by Equation (1), where FQV
serves as a positive predictor of Green Purchase Attitude (GPA).
GPA_u = α₁ + β₁ FQV_u + ϵ₁u, β₁ > 0             (1)

Stage 2: EMV Encoding Layer
Self-congruent narrative embeddings are generated within
the UI by combining personal benefits with environmental
alignment. Affective reinforcement mechanisms (e.g.,
encouraging messages post-add-to-cart) deliver feedback loops.
In Equation (2), EMV is modeled as a positive predictor of
GPA.”
GPA_u = α₂ + β₂ EMV_u + ϵ₂u, β₂ > 0            (2)

Stage 3: PEK Augmentation Layer
Micro-learning interventio ns such as hover -tooltips, label
decoders, or short explainers can be deployed to increase
knowledge accessibility. These modules can be coupled with
interactive tasks linked to loyalty rewards. In Equation (3), PEK
is modeled as a positive predictor of GPA.
GPA_u = α₃ + β₃ PEK_u + ϵ₃u, β₃ > 0              (3)

Stage 4: Intention Induction Layer
Green purchase attitudes (GPA) are translated into purchase
intentions (GPI) via low -friction commitment mechanisms,
including sample -size trials and one -click subs criptions with
deferred opt -out. This attitudinal influence is formalized in
Equation (4), where GPA positively predicts GPI, alongside
contextual control factors (C ᵤ) such as platform incentives or
trial offers.
GPI_u = α₄ + β₄ GPA_u + γ C_u + ϵ₄u, β₄, γ > 0         (4)
Notably, SEM results showed that these predictors
accounted for 44.7% of the variance in GPA, 61.0% in GPI, and
52.7% in GPB. These R² benchmarks provide evidence that the
reduced-form pipeline equations have substantial predictive
strength in explaining consumer behavior.
Stage 5: Behavior Reinforcement Layer
To close the gap between GPI and GPB, post -purchase
reinforcement mechanisms can be implemented. These include
onboarding prompts, product-use nudges, and structured review
solicitation. Review feedback loops feed directly into FQV
encoding by enriching product metadata with user -reported
efficacy.
Stage 6: A/B Testing and Path Modeling
An experimentation module evaluates the impact of
interventions on GPA, GPI, and GPB. Lightweight path models
replicate the SEM mediation structure in live settings, testing
whether system interventions improve explained variance (R²)
across behavioral outcomes.
Stage 7: Governance and Trust Enforcement

Panwar et al. / Journal of Applied Science and Technology Trends Vol. 06, No. 02, pp. 408 –426 (2025)

419
A centralized claim verification registry ensures th at all
quality and knowledge claims are supported by credible sources.
Review integrity filters mitigate noise, fraud, or manipulation
which could undermine trust in FQV signals.
A. Metrics & Evaluation
Construct-level proxies: FQV = interaction with proof
panels, review filters, certification hovers, EMV = completion
of narrative components, positive affect feedback taps, PEK =
micro-learning completion, label hover frequency.
Outcome metrics: GPA = micr o-survey scores, GPI =
commitment actions, GPB = conversion, repeat purchase.
Evaluation criterion: improvement in explained variance (R²)
across constructs, aligned with study benchmarks (GPA:
44.7%, GPI: 61.0%, GPB: 52.7%).

Fig. 3. Proposed pipeline architecture for sustainable online consumer behaviour (Author)
Overall, this pipeline operationalizes psychological
constructs into computational modules within an e-commerce
system. Each layer implements a causal intervention aligned
with significant SEM predictors (FQV, EMV, PEK) and is
validated through online experimentation and path modeling.
The design adheres to evidence -driven feature prioritization,
excluding non -significant determinants (FPV, SCV, ENC,
PCE), thus maximizing system efficiency in driving sustainable
online consumption.
Final Single (Augmented) Equation
After substituting GPA into GPI and grouping terms, the
augmented equation becomes as follows:
GPIᵤ = (γ + δα) + δβ₁·FQVᵤ + δβ₂·EMVᵤ
                         + δβ₃·PEKᵤ + (δεᵤ + ξᵤ)                               (5)
Here, δ is defined as β₄, the path coefficient from GPA to
GPI. This allows GPA predictors to be substituted directly into
the GPI equation.
We can define reduced -form coefficients and a composite
error term as follows:
κ₀ = γ + δα (absorbs constants + commitment effect)
κ₁ = δβ₁, κ₂ = δβ₂, κ₃ = δβ₃
η_u = δϵ_u + ξ_u (composite error term)
Thus, the final estimable regression model is:
GPIᵤ = κ₀ + κ₁·FQVᵤ + κ₂·EMVᵤ + κ₃·PEKᵤ + ηᵤ       (6)
B. Practical Application in E-commerce Systems
The proposed pipeline is technically implementable within
standard e -commerce infrastructures because it leverages
existing data flows and modular system components. At the data
layer, most platforms already capture the key behavioral proxies
required for the model: clickstream logs, product -detail-page
dwell time, ingredient information expansions, add -to-cart and
wish list events, subscription activations, and repeat purchases.
These events can be fused into a unified dataset (clickstream +
survey signals) that feeds into the pipeline as the foundation for
modeling attitudes, intentions, and behaviors.
The first operational stage functional quality value (F QV)
encoding can be realized by structuring product metadata such
as clinical claims, dermatological test results, and verified
ingredient lists as machine-readable attributes within the product
database. These metadata objects can be exposed at the interface
level through badges, expandable proof panels, or certification
icons, while also serving as features in recommender engines
and ranking algorithms. Similarly, emotional value (EMV)
encoding can be handled by embedding narrative-driven content
into the  user interface, supported by vectorized testimonial
corpora or natural language generation pipelines. Reinforcement
triggers can be added at interaction points (e.g., after an item is
added to cart, a pop -up confirmation communicates the
environmental or ethical value of the action).
The knowledge augmentation layer (PEK) can be
operationalized using micro -frontends that deliver eco -label
decoders, hover -tooltips, or interactive quizzes. Engagement
events such as tooltip hovers or quiz completions are logged and
ingested back into the system as features that approximate
perceived knowledge. Attitudinal states (GPA) are then
transitioned into intentions (GPI) through existing low -friction

Panwar et al. / Journal of Applied Science and Technology Trends Vol. 06, No. 02, pp. 408 –426 (2025)

420
mechanisms like wishlists, “subscribe and save” options, pre -
orders, o r free -sample trials. Each of these nodes can be
monitored by backend flags that track state transitions  in line
with the VAB sequence.
To close the loop, behavior reinforcement modules can be
integrated into customer relationship management (CRM)
systems, email automation, and push notification workflows.
These deliver personalized onboarding tips, replenishment
reminders, or structured review requests, with user -generated
reviews flowing back into the metadata layer to enrich quality
signals. A/B testing engines such as Optimizely, Google
Optimize, or in-house experimentation frameworks can be used
to validate the causal impact of each intervention, measuring
improvements in explained variance (R²) across attitudes,
intentions, and behaviors. Finally, gove rnance and trust
mechanisms can be built on claim-verification registries, either
centralized APIs or blockchain -based provenance systems,
while review fraud detection models ensure the integrity of
consumer feedback.
Taken together, this design can be dep loyed as a modular
middleware service that sits between the data layer,
application/UI layer, and experimentation layer of an e -
commerce platform. By treating psychological determinants as
programmable modules encoded as structured data, interface
elements, or backend processes, the pipeline provides a
practical, scalable, and evidence -driven approach that can be
layered into existing commerce architectures without requiring
disruptive system redesign.
C. Theoretical Implications
The findings add to theoretical understanding of green
consumer behaviour within the domain of GPCPs. First, the
study reinforces the VAB hierarchy by demonstrating that
functional quality, emotional value, and perceived
environmental knowledge significantly shape GPA, which in
turn influence purchase intentions and ultimately behaviour.
This sequential mediation underscores the attitudinal
mechanisms through which consumption values are translated
into action, supporting the relevance of behavioural theories
such as the Theory of Reasoned Action and Theory of Planned
Behaviour in digital consumption contexts. Importantly, the
study also extends the application of Consumption Value
Theory [81] to the sustainable e-commerce domain.
By extending Consumption Value Theory into a p ipeline
design framework, the study bridges behavioural science with
systems modelling. The significant influence of functional and
emotional values on consumer attitudes demonstrates that these
consumption values are central to green decision -making. The
effect remains important even without in -store interaction.
Second, the results highlight a shift in the salience of values,
where practical and affective considerations rather than
ideological or social factors emerge as primary drivers of green
purchase attitudes online. This diverges from earlier studies
emphasizing SCV and ENC, indicating that the digital nature of
the marketplace alters the cognitive weighting of influencing
variables. Third, the study challenges the presumed centrality of
constructs like PCE and FPV, suggesting that their impact may
be more context-dependent and less influential at the attitudinal
stage than previously theorized. These insights call for a
refinement of green consumer behaviour models, especially for
low-involvement pro duct categories in e -commerce settings.
For computer science, this provides evidence that system
architectures for sustainable commerce must prioritize encoding
verifiable quality, embedding affective reinforcement, and
augmenting knowledge rather than gen eric environmental
signalling.
D. Managerial Implications
From a practical standpoint, the results translate directly into
system requirements for pipeline -based e -commerce
architectures. From a practical standpoint, the strong impact of
FQV on consumer attitudes underscores the need for platforms
to encode structured product -quality metadata (e.g.,
dermatological testing, clinical claims) as machine -readable
objects, surfaced through trustworthy interface components.
Highlighting these signals strengthens trust and drives favorable
attitudes.
Second, the importance of EMV indicates that systems
should include affective encoding layers that deliver
emotionally resonant interactions. Platforms can implement
narrative embeddings, reinforcement messages, and testimonial-
driven storytelling to deepen engagement. These affective
modules transform psychological value into measurable digital
signals, increasing the likelihood of attitude formation and
intention activation.
Third, the effect of PEK underscores the nece ssity of
knowledge-augmentation layers within digital pipelines. Micro-
learning interventions, interactive eco -label decoders, and
credibility-enhancing educational content can be embedded as
dynamic UI features. Such modules reduce uncertainty and
increase product trust in ways consistent with the SEM findings.
Non-significant predictors such as SCV, FPV, ENC, and
PCE did not emerge as statistically significant in this study, but
they still carry practical relevance in specific contexts. For
example, SCV may become more salient in communities where
sustainable consumption is visible to peers; platforms could
experiment with eco -badges, public sharing features, or
influencer tie-ins to activate this value. FPV might matter more
in price -sensitive segments, where promotions, bundles, or
loyalty rewards can lower perceived financial barriers. ENC,
though not directly predictive, can still be mobilized by
translating abstract concerns into tangible product -level
attributes such as biodegradable packaging or cru elty-free
certifications. Similarly, PCE could be reinforced by linking
purchases to measurable outcomes (e.g., “this order prevents X
grams of plastic waste”), making individual contributions feel
concrete and personally meaningful. Taken together, these
insights suggest that managers should focus primarily on
quality, emotional engagement, and knowledge-building, while
selectively activating non-significant values in contexts where
they are likely to matter.
Beyond system-level design, the findings also hold broader
strategic implications for business managers seeking to
operationalize sustainability in e-commerce contexts. Managers
can leverage the validated determinants (functional quality,
emotional value, and perceived knowledge) in multiple ways.
These factors can serve as actionable levers for shaping brand

Panwar et al. / Journal of Applied Science and Technology Trends Vol. 06, No. 02, pp. 408 –426 (2025)

421
strategy, improving CRM, and guiding market segmentation.
For instance, integrating verified sustainability data into CRM
systems may enable more personalized engagement with green-
oriented consume rs, while AI -driven analytics could help
identify clusters of users more responsive to functional or
emotional cues. The pipeline’s measurable attitudinal and
behavioral stages offer a foundation for developing
sustainability-oriented key performance indic ators (KPIs),
allowing firms to monitor progress toward responsible
consumption goals. Moreover, leadership teams may consider
investing in training and incentive programs for vendors and
employees to ensure credible sustainability communication,
thereby strengthening brand trust, loyalty, and differentiation in
competitive online marketplaces.
E. Policy Implications
From a policy standpoint, the proposed computational
pipeline offers actionable insights for advancing Sustainable
Development Goal 12 (Responsib le Consumption and
Production). Policymakers can apply such frameworks to
monitor and evaluate sustainable consumption behaviors on
digital platforms through data-driven mechanisms. Encouraging
standardized eco -certification databases, interoperable
sustainability APIs, and transparent data governance structures
can enhance consumer trust and accountability in online
markets. Furthermore, regulations promoting explainable and
ethically aligned AI systems can help prevent algorithmic bias,
misinformation, an d greenwashing in e -commerce. Public –
private partnerships could also leverage these computational
insights to design educational initiatives that enhance digital
literacy and empower consumers to make informed sustainable
choices. Collectively, these measu res can align market
incentives with environmental policy objectives, fostering more
responsible consumption ecosystems in digital economies.
To further clarify how the proposed computational pipeline
differs from and extends previous research, Table V summarizes
the study’s positioning in relation to prior literature across key
dimensions of theory, modeling approach, and system design.
TABLE V.  POSITIONING THE PROPOSED COMPUTATIONAL PIPELINE IN
RELATION TO PRIOR LITERATURE
Aspect Literature Findings Current Study Findings
(Novelty / Differences)
Behavioural
constructs &
Theory Use
Many studies use Value–
Attitude–Behaviour
(VAB) or Theory of
Planned Behaviour
(TPB) to relate values →
attitudes → intention,
often via surveys/SEM
[82, 83].
This study embeds the
VAB chain into a
computational pipeline
architecture, mapping
values → attitudes →
intentions → behaviour as
operational
modules/signals rather
than abstract constructs.
Predictive /
System Design
vs Descriptive
Modelling
Literature is often
descriptive or pr edictive
(e.g., identifying which
values correlate with
green purchase, what
affects intention) but
rarely builds full system
pipelines [84].
This study builds a multi -
stage pipeline that
translates behavioural
determinants into
computational design
(signal inputs, modular
layers, output behaviours),
moving beyond
correlational analysis.
Category-
specific
Tailoring
Research on green
consumption often
focuses on broad
This study is specifically
tailored to green personal
care products, capturing
categories, but product -
specific contexts such as
personal care highlight
more specific
implications [3].
emotional and functional
quality drivers unique to
this category.
Parsimony/
Empirical
Feature
Selection
Several studies include
multiple predictors,
though onl y some
consistently emerge as
significant [4].
This study includes only
empirically significant
predictors (functional
quality value, emotional
value, perceived
environmental
knowledge), making the
pipeline leaner and more
implementable.
Bridging
Consumer
Psychology +
Computational
Implementation
Some works propose
tools (e.g.,
environmental-impact
ratings) or experiments
(nudges), but there are
limited examples of full
pipelines integrating
psychological theory into
system modules [85].
This study directly bridges
psychological constructs
with system design,
mapping theory into
computational modules as
programmable, testable
components for e -
commerce platforms.

F. Limitations and Future Research
The study offers meaningful insights into green consumer
behaviour within the e-commerce context. However, it has some
limitations. First, the data were collected using a cross-sectional
design. This restricts the ability to infer causality between
variables. Cross -sectional data provide only a snapshot at a
single point in time and therefore cannot capture how these
constructs evolve over time, nor can it confirm the temporal
ordering of the pathways. Second, the sample was
geographically limited, potentia lly constraining the
generalizability of the findings to broader or more diverse
populations. Third, the study relied on self-reported data, which
may have been affected by social desirability bias or gaps
between stated and actual behaviour. Additionally, the exclusive
focus on GPCPs limits the applicability of results to other
product categories with different involvement levels or purchase
motivations. Finally, although the survey was circulated
broadly, purposive sampling and the exclusion of respondent s
without prior online GPCP purchase experience resulted in a
sample skewed toward younger, urban, and more educated
consumers. While appropriate for ensuring data relevance, this
demographic concentration may restrict external validity. Future
studies should test the framework with more diverse populations
to enhance generalizability.
Future research could build on the current findings by
exploring value–behaviour relationships across multiple green
product categories, such as household goods, apparel, or food,
to identify whether predictors vary by product type or perceived
risk. Longitudinal studies may also offer a deeper understanding
of how values and attitudes evolve over time and in response to
repeated exposure or satisfaction with green products. I n
addition, qualitative investigations could enrich the quantitative
results by capturing nuanced consumer perceptions, emotional
drivers, and trust dynamics in online green shopping contexts.
Finally, future work could assess the influence of digital
marketing elements such as eco -label visibility, platform
credibility, and product presentation on consumer trust and
purchase behaviour in sustainability-driven segments.

Panwar et al. / Journal of Applied Science and Technology Trends Vol. 06, No. 02, pp. 408 –426 (2025)

422
VII. CONCLUSION
This study approached consumer behaviour not only as a
psychological process but also as a computational system design
problem, where values, attitudes, and behaviours can be
represented as data inputs, processing nodes, and measurable
outputs. Focusing on green personal care products (GPCPs) in
the e -commerce context, it validated  the Value –Attitude–
Behaviour (VAB) framework and confirmed that functional
quality value, emotional value, and perceived environmental
knowledge significantly shape attitudes, which in turn influence
purchase intentions and behaviours.
The originality of this work lies in translating these validated
behavioural determinants into a multi -stage computational
pipeline architecture. Unlike existing digital consumer models
that emphasize descriptive analytics, recommendation engines,
or predictive tools detache d from psychological theory, the
proposed framework operationalizes values, attitudes, and
intentions as programmable system components. It prioritizes
only empirically significant predictors, ensuring a parsimonious
and efficient design, and tailors the a rchitecture to the unique
drivers of GPCPs-a product category often overlooked in digital
sustainability research.
By bridging consumer psychology and computer science,
this study advances both theory and practice. This contribution
is distinct from prior work in two ways. Theoretically, unlike
existing green -consumption models, which are primarily
descriptive and offer little guidance for system implementation,
our pipeline extends the VAB framework into a computational
instantiation suitable for digital commerce. Practically, it offers
a blueprint for e -commerce platforms to implement evidence -
driven modules that encode product quality signals, embed
emotional reinforcement, and augment consumer knowledge.
This dual contribution distinguishes the study fro m prior
research, positioning the pipeline as both a theoretical
innovation and a practical pathway for fostering sustainable
online consumption.
Future research should extend this work by testing the
pipeline across other product categories, geographic co ntexts,
and digital environments. Longitudinal and experimental
designs could further refine the architecture and examine how
adaptive pipelines, powered by real-time data and reinforcement
learning, can optimize sustainability outcomes at scale. In doing
so, researchers and practitioners can continue to advance the
integration of behavioural science with system design for a more
sustainable digital marketplace.
REFERENCES
[1] B. Gajdzik, K. Bartuś, M. Jaciow, R. Wolniak, R. Wolny, and W. W.
Grebski, “Evolution of Polish E-Consumers’ Environmental Awareness
and Purchasing Behavior over Ten Years,” Sustainability, vol. 16, no. 11,
pp. 4686–4686, May 2024, doi: https://doi.org/10.3390/su16114686.
[2] A. Müller, z. Bács, v. Fenyves, s. Kovács, a. Lengyel, and é. B. Bác sné,
“Demographic Influences On Environmental Attitudes And Actions: An
Analysis Of The Attitude-Behavior Gap,” Geoj. Tour. Geosites, vol. 60,
no. 2 supplement, pp. 1028 –1040, Jun. 2025, doi:
https://doi.org/10.30892/gtg.602spl01-1477.
[3] C. Luthra, Pankaj De shwal, Shiksha Kushwah, and Samir Gokarn,
“‘Exploring barriers towards green personal care products purchase: an
integrated ISM-MICMAC approach,’” Int. J. Pharm. Healthc. Mark., Jan.
2025, doi: https://doi.org/10.1108/ijphm-05-2024-0045.
[4] R. Testa, F. Vella, G. Rizzo, G. Schifani, and G. Migliore, “What drives
and obstacles the intention to purchase green skincare products? A study
of the Italian market of green skincare products,” J. Clean. Prod., vol. 484,
no. 144358, p. 144358, Nov. 2024, doi:
https://doi.org/10.1016/j.jclepro.2024.144358.
[5] R. E. Dodson, B. Cardona, A. R. Zota, J. Robinson Flint, S. Navarro, and
B. Shamasunder, “Personal care product use among diverse women in
California: Taking Stock Study,” J. Expo. Sci. Environ. Epidemiol., vol.
31, no. 3, pp. 487 –502, May 2021, doi: https://doi.org/10.1038/s41370 -
021-00327-3.
[6] N. Singh, B. Rawat, D. S. Chaubey, A. P. Mani, and A. Singh,
“Understanding the Dynamics of consumer behaviour and purchase
intentions for Green Cosmetic Products in North India: A Gender-Neutral
Approach,” F1000Res., vol. 13, no. 611, pp. 611 –611, Jan. 2025, doi:
https://doi.org/10.12688/f1000research.151629.2.
[7] J. Oláh, J. Popp, M. A. Khan, and N. Kitukutha, “Sustainable e-commerce
and environmental impact on sustainability,” Econ. Sociol., vol. 16, no.
1, pp. 85 –105, 2023, doi: https://doi.org/10.14254/2071-789x.2023/16-
1/6.
[8] A. G. Cossatin, N. Mauro, and L. Ardissono, "Promoting green fashion
consumption through digital nudges in recommender systems," IEEE
Access, vol. 12, pp. 6812 –6829, 2024 , doi:  https://doi.org/
10.1109/ACCESS.2024.3349710
[9] G. Spillo, A. De Filippo, C. Musto, M. Milano, and G. Semeraro,
"Comparing data reduction strategies for energy -efficient green
recommender systems," Journal of Intelligent Information Systems, pp.
1–27, 2025, doi: https://doi.org/10.1007/s10844-025-00965-1
[10] Jing, H., & Xiaona, C. (2023). Research on the Construction of Trusted
Main-side Multi -chain Green Food Traceability Platform Bas ed on
Blockchain. Shipin gongye ke -ji, 44(14), 411 -418, doi:
https://doi.org/10.13386/j.issn1002-0306.2022070391
[11] N. Choudhury, R. Mukherjee, R. Yadav, Y. Liu, and W. Wang, “Can
machine learning approaches predict green purchase intention?—A study
from Indian consumer perspective,” Journal of Cleaner Production, vol.
456, p. 142218, 2024, doi: https://doi.org/10.1016/j.jclepro.2024.142218
[12] A. Munde and J. Kaur, “Predictive modelling of customer sustainable
jewelry purchases using machine learning algorithms,”  Procedia
Computer Science, vol. 235, pp. 683 –700, 2024 , doi:
https://doi.org/10.1016/j.procs.2024.04.066
[13] P. Huyn, A. Kumar, and S. Peng, “Personalizing consumer interventions
through leveraging behavioral economics,” Procedia Computer Science,
vol. 207, p p. 282 –291, 2022.  doi:
https://doi.org/10.1016/j.procs.2022.09.061
[14] M. R. Maarif, M. Syafrudin, and N. L. Fitriyani, “Uncovering
sustainability insights from Amazon’s eco -friendly product reviews for
design optimization,” Sustainability, vol. 16, no. 1, p. 172, 2024 , doi:
https://doi.org/10.3390/su16010172
[15] R. K. Behera, P. K. Bala, and N. P. Rana, “Creation of sustainable growth
with explainable artificial intelligence: An empirical insight from
consumer packaged goods retailers,” Journal of Cleaner Production, vol.
399, p. 136605, 2023, doi: https://doi.org/10.1016/j.jclepro.2023.136605
[16] C. Chen, D. Li, J. Qian, and Z. Li, “The Impact of Green Purchase
Intention on Compensatory Consumption: The Regulatory Role of Pro -
Environmental Behavior,” Sustainability, vol. 16, no. 18, pp. 8183–8183,
Sep. 2024, doi: https://doi.org/10.3390/su16188183.
[17] R. McLoughlin, M. McDonnell, and D. McEvoy, “The Impact of 3D and
AR Product Presentation on Mental Imagery, Product Uncertainty and
User Experience,” in Lecture notes in networks and systems, Springer
International Publishing, Jan. 2024, pp. 425 –443. doi:
https://doi.org/10.1007/978-3-031-73110-5_28.
[18] A. Shaban, Anastasiya Saraeva, S. Rose, and M. Clark, “The invisible
hand of touch: Testing a tactile sensation ‐choice satisfaction model in
online shopping, ”  J. Sens. Stud., vol. 39, no. 1, Jan. 2024, doi:
https://doi.org/10.1111/joss.12897.
[19] Z. Robichaud, B. M. Brand, and H. Yu, “Bridging the information
asymmetry in e -commerce: an intercultural perspective on sustainable
clothing,” Int. J. Retail Distrib. Manag., vol. 52(10/11), no. 1004 –1019,
Aug. 2024, doi: https://doi.org/10.1108/ijrdm-12-2023-0708.

Panwar et al. / Journal of Applied Science and Technology Trends Vol. 06, No. 02, pp. 408 –426 (2025)

423
[20] P. M. L. Ng et al., “The impact of social media exposure and online peer
networks on green purchase behavior,” Comput. Hum. Behav., vol. 165,
no. 108517, p. 108517, Nov. 2024, doi:
https://doi.org/10.1016/j.chb.2024.108517.
[21] P. M. Homer and L. R. Kahle, “A structural equation test of the value -
attitude-behavior hierarchy.,” J. Pers. Soc. Psychol., vol. 54, no. 4, pp.
638–646, 1988, doi: https://doi.org/10.1037/0022-3514.54.4.638.
[22] S. Sonkar, P. Singh, and R. Singh Dubey, “Examining the Consumer
Behavior and Preferences of Generation Y and Generation Z Toward
Green Cosmetics in the Indian Market,” J. Glob. Mark., pp. 1 –22, Jun.
2025, doi: https://doi.org/10.1080/08911762.2025.2518091.
[23] Y. Rossanty and M. D. T. P. Nasution, “Eco -Friendly Fashion and
Personal Values: Revealing the Hidden Forces behind Attitudes and
Purchase Intentions,” Int. Rev. Manag. Mark., vol. 15, no. 2, pp. 32 –44,
Feb. 2025, doi: https://doi.org/10.32479/irmm.17900.
[24] O. Essiz, S. Yurteri, C. Mandrik, and A. Senyuz, “Exploring the Value -
Action Gap in Green Consumption: Roles of Risk Aversion, Subjective
Knowledge, and Gender Differences,” J. Glob. Mark., vol. 36, no. 1, pp.
1–26, Aug. 2022, doi: https://doi.org/10.1080/08911762.2022.2116376.
[25] A. Renaldi, S. R. H. Hati, E. Ghazali, U. Sumarwan, and T. Ramayah,
“The determinants of customer loyalty in the sharing economy: a study of
the largest local food delivery apps in  Indonesia,” Cogent Bus. Manag.,
vol. 11, no. 1, Jun. 2024, doi:
https://doi.org/10.1080/23311975.2024.2364055.
[26] M. Pourvaziri, S. Mahmoudkelayeh, S. Kamranfar, A. M. Fathollahi -
Fard, M. Gheibi, and A. Kumar, “Barriers to green procurement of the
Iranian co nstruction industry: an interpretive structural modeling
approach,” Int. J. Environ. Sci. Technol., vol. 21, no. 4, pp. 3599 –3616,
Jan. 2024, doi: https://doi.org/10.1007/s13762-023-05346-1.
[27] A. Kumbargeri and S. Tripathi, “Price green inference: The role of green
= higher production cost lay belief,” J. Bus. Res., vol. 194, no. 115382, p.
115382, Apr. 2025, doi: https://doi.org/10.1016/j.jbusres.2025.115382.
[28] T. Hu, A. Al Mamun, M. N. H. Reza, M. Wu, and Q. Yang, “Examining
consumers’ willingness to pay premium price for organic food,” Humanit.
Soc. Sci. Commun., vol. 11, no. 1, Sep. 2024, doi:
https://doi.org/10.1057/s41599-024-03789-6.
[29] S. N. Khan and M. Mohsin, “The power of emotional value: Exploring
the effects of values on green product consumer choice b ehavior,” J.
Clean. Prod., vol. 150, no. 0959 -6526, pp. 65 –74, May 2017, doi:
https://doi.org/10.1016/j.jclepro.2017.02.187.
[30] Y. Wang, Y. Li, J. Zhang, and X. Su, “How impacting factors affect
Chinese green purchasing behavior based on Fuzzy Cognitive Maps, ” J.
Clean. Prod., vol. 240, no. 118199, p. 118199, Dec. 2019, doi:
https://doi.org/10.1016/j.jclepro.2019.118199.
[31] T. Handriana, M. Kurniawati, S. S. Sangadji, F. Wurjaningrum, and I. B.
Suryaningsih, “Antecedents and Consequences of Green Trust in
Environmentally Friendly Cosmetic Products,” Int. J. Environ. Impacts.,
vol. 7, no. 4, Dec. 2024, doi: https://doi.org/10.18280/ijei.070412.
[32] M. Chaudhary and N. S. Kola, “Consumers Behavior Towards Green
Marketing of Cosmetics,” Advances in marketing, customer relationship
management, and e -services book series, pp. 131 –158, Jan. 2025, doi:
https://doi.org/10.4018/979-8-3693-9959-0.ch006.
[33] S. N. Alsubari, S. N. Deshmukh, T. H. H. Aldhyani, A. Nefaie, and M.
Alrasheedi, “Rule-Based Classifiers for Identifying Fake R eviews in E -
commerce: A Deep Learning System,” Forum Interdiscip. Math., pp.
257–276, Jan. 2023, doi: https://doi.org/10.1007/978-981-19-8566-9_14.
[34] H. Zhao, F. Furuoka, R. A. Rasiah, and E. Shen, “Consumers’ Purchase
Intention toward Electric Vehicles from  the Perspective of Perceived
Green Value: An Empirical Survey from China,” World Electr. Veh. J.,
vol. 15, no. 6, p. 267, Jun. 2024, doi:
https://doi.org/10.3390/wevj15060267.
[35] J. Liu and S. Chelliah, “Personal Brand and Consumer Purchase Intention:
The Mediating Role of Perceived Emotional Value,” J. Ecohumanism.,
vol. 4, no. 1, Feb. 2025, doi: https://doi.org/10.62754/joe.v4i1.6253.
[36] I-Tung. Shih, A. D. K. Silalahi, K. Baljir, and S. Jargalsaikhan,
“Exploring the impact of perceived sustainability on customer satisfaction
and the mediating role of perceived value,” Cogent Bus. Manag., vol. 11,
no. 1, Nov. 2024, doi: https://doi.org/10.1080/23311975.2024.2431647.
[37] L.-S. Ling, S. Yi, K. Y. M. Lee, P. -S. Ling, and A. M. A. Edwin, “Do
Environmental-Related Facto rs Stimulate Consumers’ Green Cosmetic
Purchase Intention?,” Int. J. Sustain. Dev. Plan., vol. 19, no. 7, pp. 2605–
2614, Jul. 2024, doi: https://doi.org/10.18280/ijsdp.190717.
[38] L. Dessart and V. Pitardi, “How stories generate consumer engagement:
An exploratory study,” J. Bus. Res., vol. 104, no. 104, pp. 183–195, Nov.
2019, doi: https://doi.org/10.1016/j.jbusres.2019.06.045.
[39] N. Rasheed, R. I. Sabir, H. Mahmood, A. Rauf, A. M. Ibrahim, and W.
Naseem, “Impact of pro -environmental values on sustainable green
apparel buying behavior in Pakistan,” Clean. Responsible Consum., vol.
12, no. 100180, p. 100180, Feb. 2024, doi:
https://doi.org/10.1016/j.clrc.2024.100180.
[40] S. Stojanova, M. Zečević, and B. Culiberg, “From Words to Deeds: How
Do Knowledge, Effectiveness, a nd Personal Relevance Link
Environmental Concern and Buying Behavior?,” J. Nonprofit Public Sect.
Mark., vol. 35(4), no. 329 –353, pp. 1 –25, Jul. 2021, doi:
https://doi.org/10.1080/10495142.2021.1953671.
[41] S. Balaskas, A. Panagiotarou, and M. Rigou, “Impact o f Environmental
Concern, Emotional Appeals, and Attitude toward the Advertisement on
the Intention to Buy Green Products: The Case of Younger Consumer
Audiences,” Sustainability, vol. 15, no. 17, pp. 13204–13204, Sep. 2023,
doi: https://doi.org/10.3390/su151713204.
[42] D. Manika, S. Papagiannidis, M. Bourlakis, and R. M. Clarke, “Drawing
on Subjective Knowledge and Information Receptivity to Examine an
Environmental Sustainability Policy: Insights from the UK’s Bag Charge
Policy,” Eur. Manag. Rev., vol. 18, no.  3, pp. 249–262, Feb. 2021, doi:
https://doi.org/10.1111/emre.12453.
[43] G. Akandere and A. Gümrah, “The Green Purchase Behavior of Young
Consumers: The Role of Environmental Knowledge,” Folia Oecon.
Stetin., vol. 25, no. 1, pp. 1 –21, Jun. 2025, doi:
https://doi.org/10.2478/foli-2025-0001.
[44] I. Kovacs and E. R. Keresztes, “Perceived Consumer Effectiveness and
Willingness to Pay for Credence Product Attributes of Sustainable
Foods,” Sustainability, vol. 14, no. 7, p. 4338, Apr. 2022, doi:
https://doi.org/10.3390/su14074338.
[45] M. Mansoor, T. M. Awan, and O. S. Paracha, “Sustainable buying
behaviour: An interplay of consumers’ engagement in sustainable
consumption and social norms,” Int. Soc. Sci. J., vol. 72, no. 246, pp.
1053–1070, Sep. 2022, doi: https://doi.org/10.1111/issj.12372.
[46] G. Grunwald, A. Kara, and J. E. Spillan, “Involvement matters:
navigating the value –action gap in business students’ sustainability
transformation expectations—a cross-country Kano study,” Sustain. Sci.,
pp. 1–23, Apr. 2025, doi: https://doi.org/10.1007/s11625-025-01681-z.
[47] I. Ajzen, “The theory of planned behavior,” Organ. Behav. Hum. Decis.
Process., vol. 50, no. 2, pp. 179 –211, 1991, doi:
https://doi.org/10.1016/0749-5978(91)90020-T.
[48] J. F. Hair Jr, M. Sarstedt, L. Hopkins, and V.  G. Kuppelwieser, “Partial
Least Squares Structural Equation Modeling (PLS -SEM),” Eur. Bus.
Rev., vol. 26, no. 2, pp. 106 –121, Mar. 2014, doi:
https://doi.org/10.1108/EBR-10-2013-0128.
[49] A. Niedermeier, A. Emberger‐Klein, and K. Menrad, “Which factors
distinguish the different consumer segments of green fast ‐ moving
consumer goods in Germany?,” Bus. Strat. Environ., vol. 30, no. 4, pp.
1823–1838, Jan. 2021, doi: https://doi.org/10.1002/bse.2718.
[50] D. Jaiswal, V. Kaushal, P. K. Singh, and A. Biswas, “Green Market
Segmentation and Consumer profiling: a Cluster Approach to an
Emerging Consumer Market,” Benchmarking, vol. 28, no. 3, Nov. 2020,
doi: https://doi.org/10.1108/bij-05-2020-0247.
[51] L. Wang, Q. Zhang, and P. P. W. Wong, “Purchase Intention for Green
Cars Among Chinese Millennials: Merging the Value–Attitude–Behavior
Theory and Theory of Planned Behavior,” Front. Psychol., vol. 13, Feb.
2022, doi: https://doi.org/10.3389/fpsyg.2022.786292.
[52] S. Yu and J. Lee, “The Effects of Consumers’ Perceived Values on
Intention to Purchase Upcycled Products,” Sustainability, vol. 11, no. 4,
p. 1034, Feb. 2019, doi: https://doi.org/10.3390/su11041034.
[53] P. Kamalanon, J. -S. Chen, and T. -T.-Y. Le, “‘Why Do We Buy Green
Products?’ an Extended Theory of the Planned Behavior Model for Green
Product Purchase Behavior,” Sustainability, vol. 14, no. 2, p. 689, Jan.
2022, doi: https://doi.org/10.3390/su14020689.

Panwar et al. / Journal of Applied Science and Technology Trends Vol. 06, No. 02, pp. 408 –426 (2025)

424
[54] Md. Nekmahmud and M. Fekete -Farkas, “Why Not Green Marketing?
Determinates of Consumers’ Intention to Green Purchase Decision in a
New Developing Nation,” Sustainability, vol. 12, no. 19, p. 7880, Sep.
2020, Available: https://www.mdpi.com/2071-1050/12/19/7880
[55] P. Kumar and B. M. Ghodeswar, “Factors affecting consumers’ green
product purchase decisions,” Marketing Intelligence & Planning, vol. 33,
no. 3, pp. 330–347, 2015, doi: 10.1108/mip-03-2014-0068.
[56] N. Sreen, S. Purbey, and P. Sadarangani, “Impact of culture, behavior and
gender on green purchase intention,” Journal of Retailing and Consumer
Services, vol. 41, pp. 177 –189, 2018, doi:
10.1016/j.jretconser.2017.12.002.
[57] J. F. Hair, M. Page, and N. Brunsveld, Essentials of Business Research
Methods. Routledge, 2019. Available:
https://www.taylorfrancis.com/books/mono/10.4324/9780429203374
[58] C. Fornell and D. F. Larcker, “Evaluating structural equation models with
unobservable variables and measurement error,” J. Mark. Res., vol. 18,
no. 1, pp. 39 –50, Feb. 1981, doi:
https://doi.org/10.1177/002224378101800104.
[59] P. M. Podsakoff, S. B . MacKenzie, J. -Y. Lee, and N. P. Podsakoff,
“Common method biases in behavioral research: A critical review of the
literature and recommended remedies.,” J. Appl. Psychol., vol. 88, no. 5,
pp. 879–903, 2003, doi: https://doi.org/10.1037/0021-9010.88.5.879.
[60] L. Hu and P. M. Bentler, “Cutoff criteria for fit indexes in covariance
structure analysis: Conventional criteria versus new alternatives,”
Structural Equation Modeling: A Multidisciplinary Journal, vol. 6, no. 1,
pp. 1–55, 1999, doi: 10.1080/10705519909540118.
[61] S. A. V. Simão, S. F. Rohden, and D. C. Pinto, “Natural claims and
sustainability: The role of perceived efficacy and sensorial expectations,”
Sustain. Prod. Consum., vol. 34, no. 505 –517, pp. 505–517, Nov. 2022,
doi: https://doi.org/10.1016/j.spc.2022.09.026.
[62] A. A. Najm, S. A. Salih, S. Fazry, D. Law, and A. Azfaralariff,
“Moderated mediation approach to determine the effect of natural
packaging factors on intention to purchase natural skin care products
among the population of Klang Valley, Malaysia,” J. Sens. Stud., vol.
38(2), no. e12811, Jan. 2023, doi: https://doi.org/10.1111/joss.12811.
[63] T. Suphasomboon and S. Vassanadumrongdee, “Toward sustainable
consumption of green cosmetics and personal care products: The role of
perceived value and ethical concern,” Sustain. Prod. Consum., vol. 33, no.
2352–5509, pp. 230 –243, 2022, doi:
https://doi.org/10.1016/j.spc.2022.07.004.
[64] R. Ladhari and N. M. Tchetgna, “Values, socially conscious behaviour
and consumption emotions as predictors of Canadians’ intent to buy fair
trade products,” Int. J. Consum. Stud., vol. 41, no. 6, pp. 696 –705, Jul.
2017, doi: https://doi.org/10.1111/ijcs.12382.
[65] J. M. Hong, R. E. Lim, and L. Atkinson, “‘Doing Good’ versus ‘
Being Good ’: The interplay between pride appeals and regulatory ‐
focused messages in green advertising, ” J. Appl. Soc. Psychol., vol.
51(11), no. 1089 – 1108, Aug. 2021, doi:
https://doi.org/10.1111/jasp.12826.
[66] W. H. H. Cooray, S. S. J. Patabendige, and U. J. Mi rando, “Impact of
Environmental Knowledge on Green Purchase Intention: Examining the
Mediating Effect of Young Business Executives’ Attitudes Towards
Green Products in Developing Country Context,” Sri Lanka J. Mark., vol.
9, no. 3, pp. 261 –284, Feb. 2024, doi:
https://doi.org/10.4038/sljmuok.v9i3.159.
[67] A. Manopo, W. J. F. A. Tumbuan, and E. M. Gunawan, “The Influence
Of Product Knowledge On Green Purchase Intention, The Role Of
Attitude As Mediating Variable,” J. EMBA, vol. 9(4), no. 851–864, Oct.
2021, doi: https://doi.org/10.35794/emba.v9i4.36623.
[68] B. Kaur, V. P. Gangwar, G. Dash, N. Khan, and A. A. Alkhoraif, “‘Our
Planet, Our Health’ - Impact of Health Consciousness and Environmental
Concern on Green Purchase Behavior: Role of Reference Groups,” Pol. J.
Environ. Stud., vol. 33(2), no. 1191 –1202, Nov. 2023, doi:
https://doi.org/10.15244/pjoes/172037.
[69] I. U. Jan, S. Ji, and C. Yeo, “Values and Green Product Purchase
Behavior: The Moderating Effects of the Role of Government and Media
Exposure,” Sustainability,  vol. 11, no. 23, p. 6642, Nov. 2019, doi:
https://doi.org/10.3390/su11236642.
[70] D. Ghorbanzadeh, M. A. Khan, M. Lucia, K. Prasad, D. Abduvalieva, and
M. Alexandra, “From attitude to action: examining the factors affecting
sustainable purchasing behavior in Generation Z with an emphasis on
environmental responsibility,” Environ. Dev. Sustain., Apr. 2025, doi:
https://doi.org/10.1007/s10668-025-06141-3.
[71] M. R. Mayekar and K. G. Sankaranarayanan, “Values as predictors of
consumers’ green product purchase behaviour,” Int. J. Green Econ., vol.
13, no. 1, p. 1, 2019, doi: https://doi.org/10.1504/ijge.2019.101443.
[72] R. Zhang, Q. Ma, and D. Guan, “The impact of financial scarcity on
green consumption: Sequential mediating effects of anxiety and self ‐
efficacy,” Psychol. Mark., vol. 40(6), no. 1162 –1178, Mar. 2023, doi:
https://doi.org/10.1002/mar.21801.
[73] E. Kirchler, F. Fischer, and E. Hölzl, “Price and its Relation to Objective
and Subjective Product Quality: Evidence from the Austrian Market,” J.
Consum. Policy., vol. 33 , no. 3, pp. 275 –286, Jun. 2010, doi:
https://doi.org/10.1007/s10603-010-9138-1.
[74] S. Shukla and R. Sanjeev, “Exploring Feminine Hygiene Product
Adoption: a Gynecologists’ Perspective in India. Application of the
Theory of Planned Behavior (TPB) to Women’s Buying Behavior,” Soc.
Mark. Q., vol. 30, no. 1, Feb. 2024, doi:
https://doi.org/10.1177/15245004241233835.
[75] M. A. Farage, A. Katsarou, and H. I. Maibach, “Sensory, clinical and
physiological factors in sensitive skin: a review,” Contact Dermatitis, vol.
55, no. 1, pp. 1 –14, Jul. 2006, doi: https://doi.org/10.1111/j.0105 -
1873.2006.00886.x.
[76] K. Sanjay, S. Tewari, and A. N. Subbarao, “Bridging the Attitude –
Behavior Gap in Green Marketing: A Structural Equation Modeling
Approach to Psychological and Environmenta l Influences,” in In Green
Marketing Perspectives, Emerald Publishing Limited, 2025, p. (pp. 53 -
67), doi: https://doi.org/10.1108/978-1-83608-772-420251004
[77] D. Van Hoang and T. Le Thanh, “Relationship Between Environmental
Concern, Green Perceived Value and  Green Purchase Behaviour: The
Moderating Role of Price Consciousness,” Organ. Mark. Emerg. Econ.,
vol. 15, no. 2(31), pp. 248 –287, Dec. 2024, doi:
https://doi.org/10.15388/omee.2024.15.12.
[78] K. W. K. Chu, “The green gap of high-involvement purchasing decisions:
an exploratory study,” Asian J. Bus. Ethics., vol. 9, no. 2, pp. 371 –394,
Nov. 2020, doi: https://doi.org/10.1007/s13520-020-00115-6.
[79] N. B. Nguyen and T. D. Duong, “Examining the impact of greenwashing
on customer boycott intentions: the mediating rol e of green confusion,”
Discov. Sustain., vol. 6, no. 1, May 2025, doi:
https://doi.org/10.1007/s43621-025-01337-z.
[80] I. Rizomyliotis, “Consumer Trust and Online Purchase Intention for
Sustainable Products,” Am. Behav. Sci., Mar. 2024, doi:
https://doi.org/10.1177/00027642241236174.
[81] J. N. Sheth, B. I. Newman, and B. L. Gross, “Why we buy what we buy:
A theory of consumption values,” J. Bus. Res., vol. 22, no. 2, pp. 159 –
170, Mar. 1991, doi: https://doi.org/10.1016/0148-2963(91)90050-8.
[82] Chen, M. F. (2024). Integrating the value –belief–norm model and the
theory of planned behavior for explaining consumers’ purchase intention
of suboptimal food.  British Food Journal , 126(9), 3483 -3504, doi:
https://doi.org/10.1108/BFJ-05-2024-0426
[83] Wang, L., Gong, Y., Zhang, Q., Sun, R., Wong, P. P. W., & Zhou, W. W.
(2024). Merging the theory of planned behaviour and value -belief-norm
theory to predict green hotel visit intention among Chinese university
students: the case from Xuzhou, China. Acta Psychologica, 251, 104627,
doi: https://doi.org/10.1016/j.actpsy.2024.104627
[84] Nassanbekova, S., Yeshenkulova, G., Nurguzhina, A., & Ibadildin, N.
(2024). Green Product Purchase Intention of Young Customers from
Developing Country: Extended Theory of Planned
Behavior. International Journal of Sustainable Development &
Planning, 19(9), doi: https://doi.org/10.18280/ijsdp.190931
[85] Srivastava, S., Raniga, U. I., & Misra, S. (2021). A methodological
framework for life cycle s ustainability assessment of construction
projects incorporating TBL and decoupling
principles. Sustainability, 14(1), 197 , doi:
https://doi.org/10.3390/su14010197.

Panwar et al. / Journal of Applied Science and Technology Trends Vol. 06, No. 02, pp. 408 –426 (2025)

                        425
APPENDIX
TABLE VI.  MEASURES, ITEM LOADINGS, AND RELIABILITY
Variables/Items

Item Source
Factor
Loadings VIF
Cronbach
's alpha (rho_a) (rho_c) AVE
Function Quality value    0.827 0.844 0.896 0.743
“The green personal care product has an acceptable standard
of quality.”
[51]  0.851 1.848
“The green personal care product would perform
consistently.”
[52] 0.916 2.454
“The green personal care product is well made.” [52] 0.815 1.806
Function Price value    0.868 0.873 0.919 0.791
“The green personal care product is reasonably priced.” [51] 0.879 2.282
“The green personal care product offers value for money.” [52] 0.91 2.526
“The green personal care product is a good product for the
price.”
[52] 0.88 2.113
Emotional value    0.86 0.879 0.914 0.781
“Buying the green personal care product instead of
conventional products would feel like making a good personal
contribution to something better.”
[51]
0.906 2.613
“Buying the green personal care product instead of
conventional products would feel like the morally right thing.”
[51]
0.923 2.81
“Buying the green personal care product instead of
conventional products would make me feel like a better person.”
[51]
0.82
1.78

Social value    0.828 0.831 0.897 0.745
“I feel buying the green personal care products would give its
owner social approval.”
[51] 0.911 2.547
“Purchasing green personal care products helps me to feel
acceptable to others.”
[51] 0.85 2.008
“Purchasing green personal care products enable me to impress
others.”
[51] 0.826 1.709
Perceived consumer effectiveness    0.791 0.819 0.904 0.826
“It is worthless for an individual consumer to do anything
about environment”
[49] 0.929 1.647
“Whenever I buy products, I try to consider how my use of
them will affect the environment and other consumers.”
[49]

“Because a lone individual cannot have any effect on
environment or the over-exploitation of natural resources, it
does not make any difference what I do”
[49]
0.887
1.372

Environmental Concern    0.797 0.802 0.88 0.711
“I am worried about the worsening quality of the environment” [50] 0.828 1.63
“I often think about how the environmental quality can be
improved”
[50] 0.874 1.512
“Environment Protection is my major concern” [50] 0.826 1.229
Perceived Environmental Knowledge    0.752 0.758 0.858 0.668
“I feel I am quite knowledgeable about environmental issues” [50] 0.858 -
“I know how to select products and packages that reduce the
amount of landfill waste”.
[50] 0.796 1.628
“I understand the environmental labels and symbols on product
package (like- 100% organic, or vegan or cruelty free)”
[50] 0.796 1.352
Green Purchase attitude    0.943 0.944 0.957 0.815
“I think Buying eco-friendly personal care products from an
online platform is a good idea.”
[51] 0.899 3.469
“I have a favourable attitude towards the purchasing of eco-
friendly personal care products from an online platform.”
[51]
0.903 3.709
“I feel that online shopping for eco-friendly personal care
products is something I would like to do. [It’s desirable]”
[51] 0.911 3.93

Panwar et al. / Journal of Applied Science and Technology Trends Vol. 06, No. 02, pp. 408 –426 (2025)

426
“I think Buying eco-friendly personal care products from an
online platform is a smart decision.”
[51] 0.909 3.814
“I think Buying eco-friendly personal care products from an
online platform would be pleasant [enjoyable].”
[51] 0.892 3.182
Green Purchase Intention    0.916 0.921 0.938 0.75
“I intend to purchase green personal care products in the near
future from e-commerce platforms.”
[53] 0.88 2.199
“I will make an effort to buy green personal care products
from e-commerce platforms in the near future.”
[53] 0.911 2.486
“I intend to buy green personal care products instead of
conventional products in my future online shopping.”
[53] 0.879 2.286
“I would consider switching to green personal care products in
future.”
[53] 0.803 1
“I would consider buying green personal care products if I
happen to see them in an e-commerce platform.”
[56] 0.855 1.638
Green Purchase Behaviour    0.884 0.891 0.915 0.684
“When buying on e-commerce, I have green purchasing
behaviour for my daily needs’ products.”
[54]
0.851 2.334
“When buying on e-commerce, I have already switched to buy
green personal care products.”
[53,54] 0.862 2.773
“When buying on e-commerce, I often buy green personal care
products instead of conventional products if the quality is
comparable”
[53]
0.832 2.108
“When buying on e-commerce, I often buy green personal care
products even if they are more expensive than nongreen ones.”
[53]
0.84 2.378
“When buying on e-commerce, I pay attention that the
personal care products are sustainable”
[55] 0.744 1.774
