---
title: 'Integrating customer relationship management with business intelligence platform design: a design
  science approach'
url: https://doi.org/10.1007/s44362-026-00024-x
category: cx-retail
subcategory: framework
date: 2026-09
venue: Journal of Digital Management
authors:
- Min; id_orcid 0000-0002-7955-1467 Zhang
- Byron Graham
- Julie McCandless
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1007/s44362-026-00024-x.pdf
pages: 20
chars: 102967
fetched_at: '2026-11-08T18:49:52+00:00'
kb_version: 1
---

# Integrating customer relationship management with business intelligence platform design: a design science approach

RESEARCH Open Access
Journal of Digital
Management
Zhang et al. Journal of Digital Management             (2026) 2:3
https://doi.org/10.1007/s44362-026-00024-x
Integrating customer relationship
management with business intelligence
platform design: a design science approach
Min Zhang1, Byron Graham1* , Julie McCandless1 and Louise Skeath2
  * C o r r e s p o n d e n c e :
Byron Graham
byron.graham@qub.ac.uk
1Queen’s University Belfast, Belfast, UK
2SDG, Armagh, UK
© The Author(s) 2026. Open Access  This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use,
sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and
the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this
article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included
in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will
need to obtain permission directly from the copyright holder. To view a copy of this licence, visit  h t t  p : / /  c r e  a t  i v e c o m m o n s . o r g / l i c e n s e s / b y / 4 . 0 /     .
Abstract
Situated within the broader business analytics paradigm, business intelligence (BI) is important in providing small
and medium-sized enterprises (SMEs) with the information needed to manage customer relationships successfully.
However, SMEs face specific challenges when integrating customer relationship management (CRM) with the
development of BI platforms. Drawing on the design science research methodology, this study combines CRM
and BI to design, develop, implement, and evaluate a CRM-BI platform alongside strategic and process artefacts
within an SME that supplies specialist construction materials. First, we design the customer strategy and the
approach to developing customer relationships. We then design a customer experience map and service blueprint,
which inform the customer engagement model. Drawing on these strategic and operational CRM artefacts, a BI
dashboard is developed to support a broader review of business practices and facilitate data-driven decision-
making. Successful implementation of the CRM-BI platform enabled the SME to transition from reactive decision-
making to proactive, data-driven strategic decision-making, identify new business opportunities, and improve
overall business performance. The platform also supported a programme of strategic change, restructuring,
improved accountability, and innovation. The study contributes to theory and practice through novel artefacts,
design principles and design knowledge.
Keywords Business intelligence platform, Data analytics, Customer relationship management, Knowledge transfer,
Small and medium-sized enterprise
  1 Introduction
Customer relationship management (CRM) focuses on
the use of market intelligence to develop and maintain
profitable customer relationships (Payne et al., 2005;
Zablah et al., 2004). It is recognised that technology is
an important part of CRM, alongside the business pro -
cesses and strategy needed to build successful customer
relationships (Zablah et al., 2004). Business analytics
has been identified as playing an important role in CRM
(Nam et al., 2019), with applications ranging from data
warehousing and storage solutions (Watson, 2002), busi-
ness intelligence and data mining (Phan & Vogel, 2010),
text analytics (Xu et al., 2017), through to advanced artifi-
cial intelligence (Ledro et al., 2023).
Firms can use business analytics to enhance perfor -
mance and operational efficiency (Gupta & George,
2016), improve decision-making effectiveness (Li et al.,
2022), increase innovation (Dubey et al., 2021; Mikalef et
al., 2019; Wang et al., 2025) and market share (Mikalef et
al., 2020). As an overarching concept, business analytics

Page 2 of 20
Zhang et al. Journal of Digital Management              (2026) 2:3
involves the use of data to carry out descriptive, pre -
dictive, and prescriptive analytics (Delen & Demirkan,
2013). Descriptive analytics focuses on using data to
describe current and historical trends, whereas predic -
tive analytics focuses on using historical data to make
predictions (Delen & Demirkan, 2013). Prescriptive ana -
lytics focuses on the use of data to decide what action to
take using techniques such as optimisation and simula -
tion (Delen & Demirkan, 2013; Delen & Ram, 2018).
Although substantial recent attention has been devoted
to the more advanced forms of predictive and prescrip -
tive analytics (Galetsi & Katsaliaki, 2020; Lepenioti et al.,
2020; Smyth et al., 2024), descriptive analytics remains
crucial in underpinning these higher levels of analytics
maturity, thereby forming a foundation for advanced ana-
lytics. Business intelligence (BI) is central to descriptive
analytics, providing interactive dashboards and reports
to display key performance indicators numerically and
visually (Delen & Ram, 2018). These solutions can now
also incorporate more advanced forms of analytics, such
as predictive analytics and generative artificial intelli -
gence (Ruoff et al., 2023). Despite the importance of BI
within the broader business analytics framework, it has
received less attention in recent literature than advanced
analytics.
Effective BI enables firms to gain a competitive advan -
tage and make informed decisions (Mikalef et al., 2020).
BI platforms focus on analysing and communicating data
through reporting and dashboards. They allow firms
to analyse current key performance indicators (KPIs)
alongside historical trends, providing insights to improve
decision-making and conveying these insights clearly and
effectively (Li et al., 2022). Despite the recent develop -
ment of advanced tools and techniques such as predictive
and prescriptive analytics and generative artificial intel -
ligence (AI), BI remains the most widely applied form
of analytics and is particularly important in small and
medium-sized enterprises (SMEs) (Ashrafi & Zarerava -
san, 2022) that may lack the more mature resources and
capabilities needed to collect and analyse data effectively,
or may not have the same strategic requirements as larger
firms to utilise more advanced analytics tools.
A wide range of technical and organisational resources
and capabilities have been identified as important in the
development of business analytics solutions (Table S1,
Supplementary Material 1) (Combita Niño et al., 2020;
Corallo et al., 2023; Hausladen & Schosser, 2020; Lismont
et al., 2017; Menukin et al., 2023). Specifically, data and
their governance and management have been viewed as
the core building blocks of analytics solutions (Corallo
et al., 2023). Researchers also highlight the availability
and quality of data as prerequisites for an analytics plat -
form (Corallo et al., 2023; Hausladen & Schosser, 2020).
Additionally, technical resources, including information
technology and analytics infrastructure, are required to
capture, store, manage and use data for knowledge cre -
ation and management (Comuzzi & Patel, 2016; Gökalp
et al., 2021). The effective development and implemen -
tation of business analytics solutions also rely on organ -
isational resources, including leadership, appropriate
organisational structures, and employee skills (Cosic
et al., 2015; Klievink et al., 2017). Although existing
research has noted that relational resources are critical
for successful development (Cosic et al., 2015; Menukin
et al., 2023), there is limited empirical evidence on how to
integrate CRM into the development of business analyt -
ics solutions (Phan & Vogel, 2010).
This study aims to integrate CRM in the development
and implementation of a BI platform for a construction
materials supplier in Northern Ireland (SDG 1) as part
of a university-industry knowledge transfer partnership
(KTP) project 2. KTPs are UK-wide programmes funded
by Innovate UK 3. They are public-private collaborative
initiatives, involving a three-way partnership between a
UK-registered company, a UK academic institution (the
knowledge base), and a qualified graduate (KTP associ -
ate) (Gledson et al., 2024). SDG operates as a supplier in
the construction industry, supplying building materials
and other construction-related tools and supplies. As a
business management KTP , the project aims to enhance
SDG’s performance by addressing a specific business
challenge and enabling the transfer of knowledge, tech -
nology, and expertise from the knowledge base to the
company.
The project addressed the business problem of enhanc -
ing customer relationship management through business
analytics and more effective strategic and operational
planning. The overarching business aim was to improve
customer engagement and retention, to drive sales and
business growth. KTPs operate within a structured
framework in which a KTP associate undertakes substan-
tial work for a company under the guidance of industrial
supervisors from the company and academic supervisors
from the knowledge base. The company benefits from
knowledge and expertise transfer, as well as access to new
technologies, specialist facilities, and technical expertise
(Ates et al., 2025). As practically orientated yet theory-
informed projects with clear artefacts as deliverables,
KTPs are an ideal setting for a design science study.
To guide the study, we propose the following research
questions: How can CRM principles inform the design of
BI platforms in SMEs? What design artefacts and design
1 https://wearesdg.com/.
2 https:/ /iuk-kt p.org.u k/ca se-stu dy/harn essing- the- power-of-data-and-auto-
mation.
3 https:   //w ww.u kri .org/c ou ncils/in novate-uk/.

Page 3 of 20
Zhang et al. Journal of Digital Management              (2026) 2:3
principles emerge from integrating CRM and BI in an
SME context?
To address the research questions, we follow the design
science research methodology, integrating CRM theory
and practice with the design and delivery of the BI plat -
form during the 24-month KTP project. Design science
is a research paradigm that aims to design and develop
practically useful, innovative artefacts, such as systems,
models, and processes, as solutions to real-world prob -
lems and to create and validate prescriptive knowledge
(Peffers et al., 2007; Tuunanen et al., 2024). With its focus
on artefact development, design science research empha -
sises the generation of explanatory insights grounded in
empirical evidence (Avdiji et al., 2020). This can lead to
the development of new design knowledge, which may
be useful across a broader context (Zolbanin & Aubert,
2025). The method has been applied to develop data ana -
lytics platforms and tools, such as visual inquiry tools
(Avdiji et al., 2020), supply chain energy and carbon man-
agement systems (Zampou et al., 2022), and tablet appli -
cations for financial education (Zaitsev & Mankinen,
2022). The design problem for the study was to design
and implement a solution to improve CRM through inte -
grated strategic, process and technical business intelli -
gence artefacts.
The study makes a practical contribution by demon -
strating how to integrate CRM theory and practice with
the development of a BI platform. The approach involves
developing a data-driven customer strategy, embedding
key account relationship development, and redesign -
ing the customer engagement model, resulting in the
formulation of strategic pillars across the organisation.
Data-driven decision-making is facilitated by designing,
developing, and implementing a BI platform that auto -
mates KPI analysis and dissemination through advanced
visual analytics and automated reporting. As a result,
the platform enables SDG to take a strategic, relational
approach to understanding, managing, and engaging
with customers and other key supply chain stakehold -
ers. Implementing the platform has enabled SDG to
move from reactive to proactive, data-driven decision-
making, helping the organisation achieve its strategic
objectives more effectively. The approach taken in this
design integrates strategic, process, and technical arte -
facts, demonstrating that, in practice, both technical and
organisational artefacts are necessary for CRM capability
development.
We contribute to the literature by providing an inno -
vative method and design principles for developing
CRM-based BI (Gregor & Hevner, 2013). Most existing
BI designs focus on technical artefacts, without consid -
ering the broader strategic and operational artefacts that
should accompany them. Grounded in CRM, we pro -
pose a method that integrates the design of technical and
organisational artefacts and the design principles that
inform and guide the development of the BI platform.
Hence, in this study, we improve on existing BI solutions
by providing more efficient and effective decision-mak -
ing support. The study demonstrates how BI can be used
to implement and promote CRM in an SME, thereby
improving understanding of the challenges SMEs face
when implementing business analytics (vom Brocke et
al., 2020). The findings also inform the development of a
CRM-guided design process. This study contextualises BI
development within an SME in the construction industry,
enhancing the fit of the design knowledge (vom Brocke et
al., 2020).
2 Literature review
The study is grounded in the literature on BI platform
design and CRM. We begin by reviewing related work on
BI platform design, followed by the relevant CRM litera -
ture. This is followed by the development of an integrated
CRM-BI framework, which guides the design of the over-
all solution.
2.1 Business intelligence
BI platforms encompass the processes, tools, and tech -
nologies used to transform data into information, and
information into knowledge and actionable plans that
drive effective business activities (Eckerson, 2012). BI
delivers relevant information to the right people at the
right time, enabling managers to act quickly and effi -
ciently. BI platforms typically include ‘back end’ compo -
nents to store and process data from underlying source
systems, such as data warehouses, as well as ‘front end’
analytics, dashboard and reporting tools which allow end
users to view and interact with the analytics (Duque et al.,
2022). Traditionally, information derived from data has
been disseminated across companies through standard
reporting, which presents a static view of KPIs. However,
more recent approaches centre on interactive self-service
dashboards, which allow an end user to view current and
historical data and to interrogate it using various filters
and selectors. The communication of data insights can be
efficiently managed through these dashboards—defined
as visual displays that consolidate and organise the most
important information required to achieve one or more
objectives on a single screen—thereby enabling effec -
tive monitoring (Recker, 2021; Ruoff et al., 2023). Using
charts, graphs, and numerical summaries, a BI platform
can transform large, complex datasets into meaningful
visual representations. An effective dashboard can also
accelerate organisational decision-making and sense -
making for respective audiences, monitor performance
outcomes, and enhance overall productivity (Eckerson,
2012).

Page 4 of 20
Zhang et al. Journal of Digital Management              (2026) 2:3
CRM, considering factors such as the degree of individu -
alisation and the information they need to collect about
customer requirements, leading to a range of specific
CRM approaches, including product-based selling, man -
aged services, customer-focused marketing, and individ -
ualised relationship management (Frow & Payne, 2009).
CRM can help businesses to better understand custom -
ers, build relationships, and target profitable customers,
thus increasing customer satisfaction and loyalty (Lee &
Park, 2005; Nguyen et al., 2007). Effective CRM is impor-
tant to retain and drive growth from existing customer
relationships, as it is often more expensive to acquire new
customers than to maintain existing customers (Phan &
Vogel, 2010).
2.3 Integrated CMR-BI framework
CRM has been conceptualised as focusing on multiple
business areas and functions. For example, Zablah et al.
(2004) posit that CRM has been conceptualised as focus -
ing on technologies, business processes, and/or strat -
egies. Similarly, Chen and Popovich ( 2003) posit that
CRM focuses on people, process, and technology. It has
also been recognised that CRM involves all business
functions, including sales and marketing, as well as other
functions such as operations, finance, R&D, and human
resources (Chen & Popovich, 2003). These conceptualisa-
tions of CRM highlight strategic, process, and technolog -
ical aspects of CRM across business functions.
Strategic CRM focuses on the allocation of resources
to develop customer relationships to maximise cus -
tomer lifetime value management (Zablah et al., 2004).
CRM processes place more emphasis on the changing
relationship with customers, and focus on the business
processes that convert CRM inputs to outputs (Chen
& Popovich, 2003; Zablah et al., 2004). CRM processes
include knowledge management and interaction manage-
ment (Zablah et al., 2004). The knowledge management
process takes data as input, transforms it into insights,
and disseminates them, which then feed into interaction
management processes (Zablah et al., 2004). Interaction
management processes can include customer evaluation,
for example, using customer lifetime value, as well as
interactions with customers (Zablah et al., 2004).
Technology has played a prominent role in CRM, and
includes the range of technologies needed to acquire,
process, store, and analyse data relating to customer
relationships. Despite most design science studies focus -
ing primarily on the technical artefact, the importance
of an integrated approach that incorporates strategy,
organisational processes, and technology has been rec -
ognised in the wider literature (Chen & Popovich, 2003;
Zablah et al., 2004). Focusing solely on technology when
implementing CRM is unlikely to improve business
performance (Chen & Popovich, 2003). Rather, CRM
Studies have applied design science to the develop -
ment of BI platforms across various fields. For example,
Kao et al. ( 2016) developed a BI platform for hospital
decision-making, identifying benefits for the organisation
and highlighting the importance of top management sup-
port. Recker ( 2021) analysed the in-situ implementation
of Germany’s RKI COVID-19 Dashboard to develop new
design principles to extend the state-tracking capabilities
of COVID-19 dashboards. Ruoff et al. ( 2023) designed
a crisis response dashboard by integrating natural lan -
guage interaction capabilities to improve transparent
user interaction and access to crisis-related information.
Vо and Plachkinovа ( 2023) built a data-driven dash -
board that helps judges make fairer, more objective
decisions by integrating diverse data points. Amirasari
and Andrias ( 2024) developed a BI dashboard artefact
for analysing Employee Engagement Survey data within
an organisation. Gledson et al. ( 2024) developed a digi -
tal, web-based dashboard prototype to enhance the effi -
ciency, productivity, and effectiveness of construction
design management. These studies confirm the useful -
ness of the interactive components in the BI platform and
provide empirical evidence that they generally enhance
user engagement with the dashboard and make it more
accessible to a broader audience. Organisations may face
challenges in creating effective, interactive, data-driven
dashboards due to inadequate stakeholder engagement
and relationship-building during the design stage. How -
ever, there is limited guidance on integrating CRM using
an interactive, relational approach in platform design and
development.
2.2 Customer relationship management
CRM focuses on the processes and systems for manag -
ing customer interactions, with the aim of increasing
customer retention and profitability by enhancing loy -
alty and satisfaction (Aziah et al., 2009; Khodakarami
& Chan, 2014; Nguyen et al., 2007). CRM approaches
enable firms to interact effectively with customers and to
collect, store, and analyse customer data, thereby gener -
ating useful knowledge about customers, which can be
used to enhance relationships (Khodakarami & Chan,
2014). CRM systems and processes store and manage
information on customer interactions, including cus -
tomer details, quotes, sales, complaints, tastes and pref -
erences, and other customer-related communications
(Nguyen et al., 2007).
Alongside these systems and processes, it is impor -
tant to ensure that CRM aligns with the wider business
strategy, considering factors such as current and poten -
tial customers, the desired relationships with these cus -
tomers, opportunities for growth, the firm’s internal and
external environments, and technology requirements
(Frow & Payne, 2009). Businesses can also implement

Page 5 of 20
Zhang et al. Journal of Digital Management              (2026) 2:3
technologies need to be combined with other organisa -
tional capabilities and processes to enhance performance
(Chang et al., 2010).
We draw on these conceptualisations and the wider
CRM and BI literature to develop an integrated CRM
framework which includes strategic, process, and tech -
nological components. This framework, presented in
Fig. 1, guides the design of our overall CRM-BI solution.
As shown in Fig. 1, the framework integrates SDG’s over-
arching strategic pillars, CRM strategy and processes,
and the BI platform. The framework demonstrates how
CRM guides the design, development, and use of the BI
platform, leading to more effective data-driven decision-
making. Additionally, SDG’s strategic pillars are informed
by CRM and, in turn, shape the development of the BI
platform. The following paragraphs explain how these
elements are interrelated.
Our framework includes strategic CRM artefacts, cen -
tring on the customer strategy and the organisation’s
strategic pillars. Alongside these strategic artefacts, the
framework also includes the technical BI platform and
process artefacts, including key account relationship
development and the customer engagement model. Key
account relationship development focuses on analysing
and mapping current customer relationships and setting
targets for each account. This process helps to identify
opportunities and risks. The key account relationship
development and customer strategy feed into the cus -
tomer engagement model. The customer engagement
model focuses on the collection and analysis of data
across the customer journey – identifying opportunities
for upselling, customer satisfaction, and improving rela -
tionships. In line with the literature indicating that imple-
menting CRM requires cross-functional change (Chen &
Popovich, 2003), a service blueprint is developed to out -
line CRM activities across business functions.
The framework also incorporates strategic CRM ele -
ments, focusing on the overall customer strategy, along -
side the wider business strategy. The customer strategy
includes customer segmentation and prioritisation to
enable the company to focus on customers with high
growth potential. CRM is also central to the overall busi -
ness strategy, which we formulate as ‘strategic pillars’
focusing on growth, innovation, customer centricity,
operational excellence, and working environment.
These CRM processes and strategy and overall business
strategy then inform the design of the BI platform, which
falls within the technology aspect of CRM conceptualisa -
tions, as well as supporting the knowledge management
CRM processes (Chen & Popovich, 2003; Zablah et al.,
2004). The BI platform includes data acquisition, process-
ing and storage, as well as the front-end BI dashboard and
reporting to disseminate insights to business users. The
main data storage aspect of the BI platform is the data
warehouse. The literature highlights that a wide range
of CRM-relevant data can be integrated into data ware -
houses, including order information, returns, customer
interactions, customer satisfaction, and data related to
Fig. 1 The CRM approach for BI platform development

Page 6 of 20
Zhang et al. Journal of Digital Management              (2026) 2:3
the customer’s business (Chen & Popovich, 2003). This
data can be obtained from a variety of sources, including
internal systems, surveys and feedback, social media and
other web sources. When integrated and presented effec -
tively in BI dashboards, this can improve understand -
ing of customers across the customer journey, resulting
in improved decision-making and better relationship
management.
The importance of BI in CRM has been recognised in
the literature (Chen & Popovich, 2003). BI can comple -
ment CRM systems and processes by providing the
analysis and information needed to enhance customer
satisfaction and drive business success (Phan & Vogel,
2010). The integration of BI and CRM can help seg -
ment and profile customers, identify profitable custom -
ers, and facilitate the measurement and monitoring of
CRM performance (Habul & Pilav-Velic, 2010). Although
the importance of BI in CRM has been recognised, less
is known about how CRM approaches can be combined
with the development of BI platforms to support firms’
growth. Whilst the CRM and BI platform design litera -
tures provide the theoretical underpinnings for the study,
they do not provide guidance on how to combine these
two areas to design and develop useful artefacts.
Ultimately, the aim of CRM is to build relationships
with customers, with the technology supporting this aim
by enhancing the understanding of customers (Chen &
Popovich, 2003). To meet this aim, BI dashboards must
provide the information needed to improve customer
understanding and relationship building. This means the
dashboard design should be driven by CRM needs. This
is likely to require close interaction between the design
of strategic and operational CRM artefacts and technical
CRM artefacts, rather than designing either in isolation.
CRM integrates data across customer touch points to
gain a better understanding of customers (Chen & Popo -
vich, 2003). More generally, a range of business analyt -
ics applications can be applied to data collected across
the stages of the customer journey to support CRM.
This can include applications such as segmentation, cus -
tomer profiling, churn prediction, dissatisfaction analy -
sis, and product recommendation (Zerbino et al., 2018).
These applications rely on data and can be applied across
stages of the customer journey from relationship initia -
tion, through to maintenance and termination (Zerbino
et al., 2018). This highlights the need for a close connec -
tion between information collected across the customer
journey and the technical BI platform. Sharing CRM data
across the organisation can also yield significant benefits,
such as identifying opportunities for upselling, improving
customer service, enhancing understanding of custom -
ers, and enabling segmentation and targeting (Chen &
Popovich, 2003). A CRM-informed BI solution can help
disseminate this information to realise these benefits.
To summarise, our CRM-BI framework highlights the
need to integrate strategic, process, and technological
artefacts in the development of CRM-BI solutions. The
CRM strategy and processes inform the data, informa -
tion, and insights that are needed to effectively imple -
ment CRM. CRM is a core aspect of the organisation’s
strategy and therefore also informs the information
required for the BI platform. The technical BI platform
presents this information to end users through dash -
boards, supporting more effective decision-making and
ultimately enhancing customer understanding and rela -
tionship management. Despite this, past design science
studies on BI have focused on technical artefacts, with -
out considering the wider strategic and process factors
that shape BI design. We therefore take a more integrated
approach than past literature when designing our CRM-
BI solution.
3 Method
We draw on the design science research methodology
(Peffers et al., 2007) to study how CRM can be combined
with the development of a BI platform to improve firm
performance. In contrast to studies focusing primarily on
theory development or testing, the design science meth -
odology focuses on gaining useful knowledge through
the design of practical artefacts intended to solve organ -
isational problems (Hevner et al., 2004; Holmström et
al., 2009). Rather than developing or testing new theo -
ries, design science artefacts draw on kernel theories,
which are bodies of existing knowledge, to explain why
an artefact should work (Hevner et al., 2004; Iivari, 2020).
Although the literature includes a range of approaches
regarding design science methodology, commonly
applied stages in the process include problem identifica -
tion, setting objectives, solution design and development,
demonstration, evaluation, and communication (Peffers
et al., 2007).
In implementing the design science method, we first
identified the issues faced by SDG and the aims and objec-
tives of the KTP project. The project aims and objectives
were identified and refined through initial discussions
between SDG and the academic team. A formal project
work plan was developed from these initial discussions,
which detailed the design requirements and activities to
be carried out over the two-year project. The activities in
the workplan were agreed by the business and academic
partners, with input from the KTP advisor and the Uni -
versity KTP office. This workplan was reviewed by the
funder, who subsequently funded the project. The ethics of
the project were also considered at this stage in line with
University ethics and integrity standards and guidelines.
Data analyses were carried out within the business by the
KTP associate, maintaining confidentiality and privacy.
Once funding was received, a recruitment process was

Page 7 of 20
Zhang et al. Journal of Digital Management              (2026) 2:3
conducted to hire the KTP associate. The KTP associate is
based at the company and undertook most of the artefact
design and development, with support from the academic
team and company personnel.
As presented in our overarching framework and
included in the project workplan, the project involved the
design and instantiation of strategic, process, and tech -
nological artefacts. These include the customer strategy,
key account relationship development, customer engage -
ment model, overarching strategic pillars, and the BI
platform. Together, these artefacts make up the overarch-
ing CRM-BI solution. The artefacts were designed in col -
laboration among the business, the academic team, and
the associate, with the associate primarily responsible for
their practical development and implementation. Evalua-
tion of design science artefacts is important to gain feed -
back, as well as to provide rigour to the research process
(Venable et al., 2016). Evaluation of the artefacts included
both formal and informal evaluation, and was both for -
mative and summative (Venable et al., 2016). This use
of multiple sources of formative and summative evalua -
tion evidence at different stages of the project is another
important aspect of design science research evaluation
(Venable et al., 2016), which we have incorporated in our
evaluation approach.
The artefacts were formally evaluated on an ongo -
ing basis during the project through a series of six local
management committee (LMC) meetings, each lasting
for around one hour. Each meeting included the follow -
ing people: the KTP associate, the company supervisor,
the Chief Executive of SDG, the two academics involved
in the project, a KTP advisor from the funder, and one
administrative staff member. This group provided expert
feedback on each artefact from differing perspectives.
Prior to each LMC meeting, the associate, academic
team, and company team were required to submit a writ -
ten report detailing progress to date. During the meeting,
these reports were presented to the committee. The focus
of each meeting was the associate’s presentation, which
detailed progress to date against the original workplan
and presented or demonstrated any artefacts produced
since the previous meeting. This included presenting the
strategic and process artefacts and demonstrating the
technical BI solution. The meeting committee provided
feedback on each artefact, leading to ongoing refinement
throughout the project. Detailed minutes were also taken
during the meeting.
As the associate was based in the company, more infor-
mal evaluation of the artefacts occurred on an ongo -
ing basis from company personnel and management.
Following completion of the project, an overall formal
evaluation took place. This consisted of a comprehen -
sive final evaluation report, with sections completed by
the academic team, the company, and the KTP associate.
The final reports contained a series of 50 questions that
required both qualitative and quantitative evidence of the
project’s performance. The associate’s sections contained
questions on the original project objectives; changes to
the original objectives; the main activities, milestones,
and outcomes; changes to the project plan and lessons
learned; project effectiveness and satisfaction with the
project; assessment of others’ satisfaction with the proj -
ect; additional post-project resources required to main -
tain the benefits; summary of documents logged with the
company at project closure; details of training provided
to the company; whether the project met expectations;
and suggested improvements to the KTP . The partners’
sections included a jointly completed summary of the
overall project, followed by questions to be completed
separately by the academic and industry partners. Ques -
tions for the company were both quantitative and quali -
tative, assessing the project’s outcomes and its impact on
company performance. Questions related to: business
changes arising from the project; contribution of the
project to the company strategy; external factors influ -
encing company strategy or the KTP project during the
project; the business opportunity addressed by the proj -
ect; new knowledge and skills acquired by the company’s
staff from the project; how these skills and knowledge
were embedded in the company; immediate and forecast
changes in sales, exports, and profit resulting from the
project; other enhancements to the company’s operations
from the project, social and cultural benefits; the nature
and significance of the impacts; investments to exploit
the results of the project; future impacts of the proj -
ect on company performance; and whether the project
matched up to expectations. Questions for the academic
team were also a mix of qualitative and quantitative, with
a greater focus on the project’s academic benefits. Ques -
tions for the academic team focused on academic staff
development, impact on teaching, postgraduate projects
from the project, research benefits, other institutional
benefits, and whether the project exceeded expectations.
In total, the completed report contained 23 pages of evi -
dence that was used to inform the formative ex-ante eval-
uation of the project artefacts.
The questions in these evaluation reports are designed
by the project funder and have been used extensively to
evaluate other KTP projects, indicating both their prac -
tical utility and their reliability as evidence for evalua -
tion. Following submission of the final project report, the
project was formally assessed by independent KTP advi -
sors who were not involved in carrying out the project.
Although the exact criteria for this final evaluation are
not made available, the project received the highest rat -
ing of ‘outstanding’ , further indicating the project’s overall
success. The use of formative and summative evaluations
from multiple sources during the design and evaluation

Page 8 of 20
Zhang et al. Journal of Digital Management              (2026) 2:3
of the project helps triangulate evaluation evidence,
thereby increasing rigour in the design science process.
4 Artefact description
The project involved designing five artefacts, with the key
results focusing on the artefact design and description,
and design principles. Strategic and process artefacts
include the customer strategy, key account relationship
management, customer engagement model, and the
organisation’s overall strategic pillars. The focal technical
artefact is the CRM-BI platform, central to which is the
CRM-BI dashboard. We first present the company back -
ground and project objectives, followed by the descrip -
tion and design of each artefact.
4.1 Company and project background
SDG is a family-owned SME and one of the main suppli -
ers of specialist construction materials to the building and
construction industry in Northern Ireland and the Repub-
lic of Ireland. SDG’s mix of product quality, rapid deliv -
ery, dependability, competitive pricing, and commitment
to customer service has enabled it to build a client base
ranging from SMEs to blue-chip construction companies,
public bodies, and government departments. Its vision
is to become a £50 million business, bringing innovation
and high-quality jobs to the local economy. The KTP team
comprises the KTP associate, who holds a master’s degree
in business analytics, two industrial supervisors (i.e., SDG’s
Chief Executive and Finance Manager), and two academic
supervisors. The KTP associate was based in SDG for the
duration of the twenty-four-month project, and the two
academic supervisors spent an average of half a day per
week on the project. The academic team's involvement
included meetings with the company management, the
associate, and the funder, as well as input into the solu -
tion’s development. Close interaction with the company
over this period provided the academic team with detailed
insights into the project and the organisation, thereby
facilitating the design science method used in this study.
4.2 Problem identification and project objectives
Before the project began, SDG had already established
routes to market through construction companies,
builders’ merchants, and distributors. SDG conducted
a strategic review that identified a need to shift from
product marketing to relational marketing. The review
highlighted the need to understand customer needs and
consistently deliver on them, alongside ongoing KPI
monitoring and measurement of CRM initiative impact.
Additionally, SDG had a limited understanding of how
to partner more effectively with customers and identify
their key issues and needs. SDG recognised that cus -
tomer engagement was ad hoc and intermittent, rather
than organised through an effective CRM process. This
created an opportunity to improve customer engage -
ment, enabling SDG to meet customer needs better and
drive sales. Hence, analysing gaps in relationship market -
ing and identifying where SDG might develop opportu -
nities was critical to achieving its growth objectives. The
review also highlighted a significant skills gap in data-
driven decision-making and a lack of internal expertise
to develop and implement advanced analytics solutions.
Operational inefficiencies were another pressing issue, as
manual processes consumed valuable time and resources,
thereby limiting productivity and overall performance.
Moreover, the existing business structure created bottle -
necks, preventing senior staff from dedicating time to
strategic initiatives. SDG lacked the knowledge and tools
to enable the senior management team to make data-
driven decisions.
The KTP project was motivated by the need to improve
customer relationships and by the recognition that data
and analytics could enhance the business. Given these
challenges and opportunities, the overarching aim of the
KTP project was to enhance business growth by leverag -
ing the latest thinking in CRM and business analytics.
This was paired with a more strategic, proactive approach
to understanding, managing, and engaging with custom -
ers, enabling SDG to shift from reactive measures to a
more proactive, data-driven strategy. Although SDG had
a good understanding of the underlying issues, it lacked
a clear vision for addressing them. The company also
understood that business analytics could help drive busi -
ness objectives, but lacked in-house expertise to use it
effectively and instead relied on basic spreadsheet analy -
ses and intuition-based decision-making. The academic
team, therefore, worked with SDG to develop a project
plan to integrate CRM with a data-driven BI solution.
Specifically, the project designed a CRM-based BI plat -
form that enables SDG to access real-time, on-demand
data and analytics, a comprehensive data governance
framework, and strategic and process artefacts. Devel -
opment of the CRM-BI platform involved developing
mechanisms for data delivery and presentation, including
designing the data flow and storage, modelling the data,
implementing security, monitoring and modification,
and creating a new interactive reporting and visualisation
interface.
4.3 Artefact design
The focal artefact for the study is the CRM-BI plat -
form. As presented in our framework, the design of BI
platforms occurs within a broader strategic and organ -
isational context. The CRM-BI platform is therefore
informed by the development and instantiation of stra -
tegic and process artefacts, including the customer strat -
egy, key account relationship development, customer
engagement model, and strategic pillars.

Page 9 of 20
Zhang et al. Journal of Digital Management              (2026) 2:3
4.3.1 Customer strategy
The first part of the CRM approach involved developing
a customer strategy by investigating current customer
interaction and purchase behaviour. We created a cus -
tomer strategy for existing customers by conducting a
detailed analysis alongside cluster analysis for customer
segmentation. This enabled us to identify customers
with significant growth opportunities based on current
engagement levels and customer financials, with the
overall aim of increasing SDG’s growth. We then selected
a sample of customers to conduct a detailed analysis
of their relationships, interaction types, and frequen -
cies. We also examined customer purchasing behaviour
to identify reasons for sales declines, which informed
improvements in account management and communica -
tion. Customer lifetime value was also calculated using
a historical approach based on sales revenue from 2017
to 2020 to identify where relationships were weakening
and could be strengthened. A product purchase trend
analysis helped investigate reasons behind significant
sales drops for certain products. An example of customer
analytics is provided in Fig. S1, Supplementary Material
1, offering insights into KPIs for customer relationship
management. The findings of this analysis were presented
in a workshop to gather employees’ views on the crite -
ria for customer segmentation and prioritisation and on
monitoring and measuring customer lifetime value.
Customer segmentation was undertaken using k-means
clustering. Data for the cluster analysis are from 302 cus -
tomers and include variables such as customer lifetime
value, order frequency, company turnover, sales in the
past 12 months, total years in business, and total years
with SDG. This resulted in four customer segments as
outlined in Fig. 2, with descriptive statistics for each clus-
ter presented in Table S2, Supplementary Material 1.
Detailed strategies were developed to manage rela -
tionships with each customer segment. Feedback from
the business indicated that it would be useful to further
subdivide customers based on relationship strength into
supporters, neutrals, and defectors. Supporters are loyal
customers who maintain a supportive, nurturing rela -
tionship with SDG and prefer to do business with SDG
over competitors. Neutral customers tend to be indiffer -
ent to whether they do business with SDG or its competi-
tors, and although they do work with SDG, they are more
likely to ‘shop around’ . Defectors are customers at high
risk of churning due to their weaker relationship with
SDG. Specific strategies were then developed for each
customer segment, broken down further by relationship
strength. A detailed overview of the specific strategies
developed during the project and used by the business is
presented in Table S3, Supplementary Material 1.
The first segment includes ‘True-blues’ . These are larger
customers who generate long-term repeat business and
account for around half of SDG’s total revenue. They are
highly engaged customers with significant power and
influence and should therefore be managed carefully.
SDG relies heavily on these customers and maintains
strong relationships that it aims to sustain and enhance.
To support these relationships, SDG plans to commu -
nicate regularly with these customers. For supporters,
this can include informal contacts to build relationships,
as well as providing training and information on prod -
uct updates. For neutrals, actions can focus on formal
updates, occasional informal communications, and train -
ing. For defectors, efforts focus on ensuring concerns are
recognised, gaining a better understanding of satisfac -
tion levels and current projects, and providing technical
advice.
The second segment comprises ‘safeguard strategic’
customers. These are customers who do not currently
generate as much revenue as true-blue customers but
have the potential to increase their revenue through
stronger relationship-building. These customers hold
significant influence, and careful relationship manage -
ment should be employed to ensure they remain with
the business. For example, additional relationship build -
ing may be required to boost sales and prevent churn.
For supporters, CRM actions can focus on providing
product updates and building relationships. For neutrals,
actions can again focus on keeping customers informed
and addressing any concerns. For defectors, actions can
focus on addressing concerns and on targeted efforts to
win customers back.
The third segment includes ‘attention seekers’ . This
group comprises a diverse range of smaller businesses
with limited influence, but together they generate a sig -
nificant portion of SDG’s revenue. These customers
require a high level of relationship management through
Fig. 2 Customer segmentation

Page 10 of 20
Zhang et al. Journal of Digital Management              (2026) 2:3
regular communication to sustain and grow sales. This
involves addressing any product queries they may have.
To maintain an effective relationship with this customer
group, SDG aims to ensure consistent contact. While
communication is important, it is carefully managed
to balance efficiency, relationship-building, and sales
growth. For supporters, actions can include maximising
opportunities for bulk orders to increase efficiency, as
well as effective account and time management. For neu -
trals, actions focus on improving customer satisfaction,
providing product-related education, and managing rela -
tionships by geographical area. For defectors, actions can
focus on addressing concerns, ensuring appropriate pric -
ing, and educating about SDG service and values.
The fourth segment includes ‘passive clients’ . These are
customers with low power and low interest. To main -
tain an efficient and effective relationship with this cus -
tomer group, SDG aims to monitor their needs and avoid
over-investing time. Marketing efforts for these clients
are more focused and targeted. For supporters, this can
include general marketing communication and respon -
sive account management, as well as specific market -
ing communications as necessary. For neutrals, this can
also include general communications and individual-
level interaction as required. For defectors, actions can
focus on allaying concerns through general channels and
responsive sales contact.
4.3.2 Key account relationship development
As shown in Fig.  1, the second element of the CRM
approach involved developing key account relationships.
We created two templates to collect quantitative (cus -
tomer data) and qualitative (relationship map) information
for analysing the development of key account relationships
(Fig. S2, Supplementary Material 1). First, we examined
the relationships within the account, mapping all custom-
ers and relevant stakeholders. This information helps SDG
identify which relationships to build and maintain, as well
as identify customers who could potentially disrupt plans.
Detailed data were gathered, including individual titles,
decision-making roles, the extent of current communica-
tion, and the level of friendliness. Second, after collecting
the data, we analysed the customer’s current business pro-
cesses, objectives, and financial health. This analysis adds
value to the account, helps identify mutually beneficial
opportunities, and allows SDG to gain a comprehensive
understanding of the client’s business, including current
goals and initiatives. Third, we set targets for the account,
including current account value, opportunities won and
lost, potential revenue growth, revenue forecasts, and
short-, medium-, and long-term goals.
We then collaborated with the senior management
team to develop a strategy for strengthening key account
relationships. The strategy aims to build long-term,
mutually beneficial partnerships with important custom -
ers. It helps account managers identify opportunities to
create value for their partners by diagnosing issues, pro -
posing innovative solutions, and leveraging partnerships
to guide the organisation toward its strategic objectives.
It seeks to foster customer loyalty, encourage growth, and
boost profitability, while driving innovative, scalable ser -
vice solutions, shortening sales cycles, reducing acquisi -
tion costs, and prioritising relationships.
4.3.3 Customer engagement model
As shown in Fig.  1, the customer strategy and key
account relationship development feed into a customer
engagement model, which was developed by analysing
the current customer experience and gathering data at
each stage of the customer journey, including customer
interactions and service levels. Specifically, we collected
data from external sales (order completion and fulfil -
ment), warehousing and delivery (stock, products, and
deliveries), and internal sales (follow-up). To refine the
customer journey and KPIs, we conducted a workshop
and individual meetings with employees across depart -
ments (marketing, sales, finance, and warehousing and
delivery), and observed employee-customer interactions
(with delivery drivers and the sales team).
We segmented the customer journey into five stages
(Awareness, Consideration, Decision/Service, Engage -
ment, and Loyalty) and outlined the main goals, the
data that can be collected, and the insights to be gained
at each stage (Table  1). We also created a framework to
gather customer insights throughout the journey (Fig.
S3 in Supplementary Material 1). This framework details
the points at which insights should be gathered across
the purchasing process, specifying the necessary level
and type of analysis. The customer insights are intended
to help SDG boost cross-selling and upselling and iden -
tify opportunities to improve customer satisfaction, ulti -
mately fostering greater customer loyalty.
We developed two methods to collect customer feed -
back. The first is the customer satisfaction survey (Fig. S4,
Supplementary Material 1). Surveys are used to identify
customers’ pain points and assess their satisfaction with
SDG’s products and services. Specifically, the first half of
the questionnaire focuses on customers’ perceptions of
SDG’s current offerings, while the second half explores
areas for improvement. We also included the Net Promoter
Score to measure overall customer satisfaction and loy -
alty. The second method involves ‘feedback and feed-for -
ward’ (Fig. S5, Supplementary Material 1), which involves
customer feedback received via phone, email, and meet -
ings. Negative feedback is acknowledged immediately and
assigned to the responsible individual for resolution within
48 h. A system to classify negative feedback has been devel-
oped (see Fig.  3), ensuring that SDG both acknowledges

Page 11 of 20
Zhang et al. Journal of Digital Management              (2026) 2:3
and promptly addresses any issues. We also established
methods to act swiftly on customer feedback through
automated processes and personal interactions. Specific
metrics are collected during feedback, including contact
details/role, date of feedback, channel used, reason for dis-
satisfaction, product details, responsible person, actions
taken, status, and date of resolution. The goal of collecting
feedback is to understand customer needs, improve and
develop better products, and foster customer loyalty by
serving their needs more effectively. Feedback also enables
SDG to innovate in response to customer needs and to
strengthen its overall brand and value proposition.
We created a service blueprint to outline the activities
of SDG’s departments (i.e., Marketing, Internal Sales,
Sales, Technical Department, Accounts, and Warehouse/
Delivery/Purchasing teams), covering both customer-
facing and ‘back office’ operations, as well as support
processes throughout the customer journey. We then
developed a customer engagement model for SDG based
on the customer journey and service blueprint (Fig.  4).
This engagement model summarises and highlights key
findings from the CRM approaches undertaken dur -
ing the project, including customer needs, major action
points, customer interactions and touchpoints, customer
actions, departmental activities, customer thoughts and
feelings, potential pain points, and opportunities for
improvement at each stage of the journey.
4.3.4 Strategic pillars
As shown in Fig.  1, the CRM artefacts inform the strate -
gic pillars and the design of the BI platform. These ele -
ments are closely interconnected in creating the overall
solution. To define the strategic pillars, the academic
team collaborated with SDG’s senior management team
to develop a company strategy structure (i.e., Strategic
pillars) that supports the implementation of the 5-year
strategic plan (Fig.  5). Among the five pillars, Pillars 1, 2,
and 3 are particularly relevant in highlighting the need
for a BI platform, with Pillars 1 and 3 both pointing to
the requirement for CRM business analytics, and Pillar 2
explicitly highlighting the better use of data as a core ele -
ment of the SDG’s innovation strategy. For example, the
strategic objective of smart growth in pillar 1 can be sup -
ported by segmenting target customers into clusters and
leveraging data to understand customer buying behav -
iour and product purchase patterns throughout their cus-
tomer journey. Focusing on customers with significant
growth potential will help SDG reach its overall growth
goals. A customer-centric approach prioritises improving
customer experiences. SDG can ensure quality of service
and enhance the customer experience by understanding
and delivering on customer motivations and continu -
ously tracking impact through engagement.
Table 1 The customer journey
Stage Goal Data Sources Insights gained
Awareness Contact
acquired
Customer contact and business information from web-
sites, brochures, social media, and direct inquiries.
Number of business development
opportunities.
Consideration Product signup Telephone enquiries, email inquiries, Construction Indus-
try Scheme tender notifications and quotes.
Potential leads information, interested prod-
ucts list.
Decision/Service Value delivered Point-of-sale transaction information (customer, products,
price). Order confirmation form. Invoice information.
Dispatch report. Proof of delivery document.
Product sales trends. Current and historical
purchases by customer. Order fulfilment times.
Engagement Fully engaged Follow-up logs, Satisfaction and engagement scores,
Sales information.
Level of engagement indicated by customer
feedback, customer satisfaction and engage-
ment, repeat transactions.
Loyalty Grow the life-
time value
Referrals, Testimonials and feedback, Net promoter score. Customer loyalty is indicated by business value
arising from referrals, positive testimonials and
feedback, and a high net promoter score.
Fig. 3 The classification of negative feedback

Page 12 of 20
Zhang et al. Journal of Digital Management              (2026) 2:3
4.3.5 Business intelligence platform
A workshop and meetings with the company’s senior
management team were organised to gather information
to inform the design of the BI platform. The KPIs to be
tracked were jointly decided with the senior manage -
ment team and used to shape the report and dashboard
layout. We reviewed SDG’s existing data architecture to
identify issues and risks and to implement role-based
Fig. 4 Customer engagement model

Page 13 of 20
Zhang et al. Journal of Digital Management              (2026) 2:3
security for reports. The BI platform aims to deliver and
present insights effectively. From a technical perspective,
this involved designing the data warehouse, modelling
the data, implementing security measures, monitoring
and adjusting data, and creating a new dashboarding
and reporting tool. This directly supported SDG’s over -
all business strategy. During development, we extracted
the necessary data from source systems, stored it in a
SQL Server data warehouse, and used Power BI to build
dashboards for employees and senior management (Fig.
S6, Supplementary Material 1). This enhanced data-
driven decision-making and automated time-consuming
reports.
The BI platform provides dashboards and a range of
reports, such as an overall scorecard (weekly and month-
to-date), top customer behaviour, account management
report, top customer purchasing trends, customer ana -
lytics, and gap analysis (product) for each customer
representative. The data and insights in each report are
based on data collection and analysis carried out dur -
ing CRM. Users can view information on all customer
representatives or on a specific one, filtered by year and
month. Within each dashboard, users can select the KPIs
of interest. For example, in the top customer purchasing
trend report, the KPIs include target sales versus actual
sales, total revenue by sector, and top customers by pur -
chasing amount (this year versus last year). In the score -
card report, KPIs include target versus actual sales and
revenue (% to target by month), monthly sales rank (top
customers), and the top 10 products sold (by sales value).
Following the design and development, the BI plat -
form was implemented within SDG. Senior managers
and employees received training on using the platform
for decision-making. We developed a ‘Guidebook’ to
help end users navigate the platform effectively. A video
tutorial to guide staff in navigating the platform was also
developed and made available to end users. We also ran
a series of workshops to promote the platform and pro -
vide training, including platform usage, data governance,
guidance on using the data through a new meeting for -
mat, an action-planning toolkit, and definitions and guid-
ance on KPIs. The CRM-BI dashboard also facilitated
weekly KPI scorecard meetings, which were attended
by the business’s senior management. These meetings
enhanced performance management within the business
and increased levels of accountability. They also provided
a forum for discussion and for ideas to improve KPI
performance.
The platform fundamentally informed SDG’s approach
to marketing, sales, and strategic planning, making the
Fig. 5 Strategic pillars

Page 14 of 20
Zhang et al. Journal of Digital Management              (2026) 2:3
business more data-driven and analytical, and increas -
ing visibility into performance and accountability within
the organisation. The BI platform also allows SDG to fully
capture the value of the data from its existing informa -
tion systems. All senior managers in SDG have adopted
the platform for data-driven planning and are increas -
ingly making decisions based on objective evaluation and
evidence.
5 Evaluation
The overall CRM-BI solution, incorporating the strategic,
operational, and technical artefacts, was evaluated using
a summative ex-post evaluation through the final project
evaluation reporting. This process involved completing a
final project evaluation report, with questions answered
separately by the associate, business, and academic
teams. This ex-post evaluation focused on a retrospective
assessment of the overall project and on predicting future
benefits. In this section, we draw primarily on this evi -
dence to evaluate the artefacts and the overall solution.
Although this provides a reliable summative evaluation
of the project, ongoing evaluation of artefacts through
LMC meetings, fortnightly supervision meetings with
the associate, and informal, ad hoc interactions between
the associate and the company also informed the design
of the artefacts and served as more informal formative
evaluations.
Overall, the final evaluation report indicates that the
project artefacts have been successfully embedded into
the organisation. Feedback included in the final evalu -
ation report from SDG’s chief executive indicates that
the KTP project has delivered substantial benefits across
multiple areas of the business. Based on the final project
evaluation, SDG identified substantial business changes
resulting from the project, including adopting strategic
planning aligned with the strategic pillars and moving
toward a data-driven culture in which all senior manag -
ers use data-driven approaches to planning, execution,
and evaluation. The latter cultural change was facilitated
by the BI platform, alongside training and workshops
provided by the associate to company staff, and, more
broadly, by the development of the organisation’s BI capa-
bility. In total, fifteen SDG staff were trained in the use of
management dashboards, KPI-setting, value proposition,
and account management. A permanent ‘Business Intel -
ligence Analytics Manager’ position was also created as
a direct result of the project. As a result of the project,
additional staff are also being recruited in account man -
agement and business development.
The final report highlights the benefits of the project’s
focal technical artefact, the CRM-BI platform, particu -
larly the CRM-BI dashboard, which provides informa -
tion to enhance decision-making. The CRM-BI platform
enabled SDG to use data from its internal systems more
effectively by providing staff with real-time analyt -
ics, advanced reporting, and market insights, thereby
streamlining decision-making and improving strategic
planning. Concrete examples of this include using the
CRM-BI dashboard during meetings to drive discussion
and decision-making, as well as a reported 25% reduction
in the time the senior management team requires to pre -
pare for meetings. This efficiency, coupled with time sav -
ings in automating reports, freed up time and resources,
enabling staff to focus on more value-added activities.
The CRM-BI platform also resulted in efficiency and time
saving in the preparation of reports. In the final report,
the business indicates that automating reports saved five
senior team days per month. The new CRM-BI solu -
tion also provided real-time information, rather than
the previous weekly and monthly reports. This provided
more up-to-date information for enhanced decision-
making. The associate also highlighted in the final report
that data-driven decision-making has become routine
in the business, with positive feedback and buy-in from
stakeholders.
The project also resulted in improved data quality,
which has positively impacted planning and tracking
capabilities, helping alleviate downward margin pres -
sures. For example, the war in Ukraine resulted in direct
and indirect increases of up to 35% in product costs.
Operating costs have also risen by up to 25%. With the
aid of the BI platform, SDG has improved margin verifi -
cation, sales planning, and pricing operations.
Improving relationship marketing also created signifi -
cant value for SDG. The customer engagement model
enabled SDG to prioritise key accounts, enhance cus -
tomer interactions, and identify growth opportunities.
The model provides enhanced visibility of performance
metrics across the business, ensuring decision-makers
have the insights required for effective decision-making.
The introduction of CRM further strengthened SDG’s
market position by prioritising key relationships and
delivering a more tailored customer experience.
The project also delivered measurable financial ben -
efits. During the project, annual sales turnover increased
by £100,000, with a three-year forecast projecting growth
to £1.5  million. Current export revenue has grown by
£250,000 as a result of the project, with a three-year pro -
jection of an additional £15  million in export revenue
resulting from the project. This is attributed to improved
business intelligence, market lead qualification and
improved price setting. Annual profit before tax also saw
a measurable increase, with current annual profit before
tax rising by £200,000, directly attributable to the proj -
ect. The predicted three-year increase in profit before tax
resulting from the project is £500,000. This includes both
new products and new markets, as well as operational
efficiency and improved quality. These performance gains

Page 15 of 20
Zhang et al. Journal of Digital Management              (2026) 2:3
are attributed to improved account management, margin
planning, optimising pricing, predictive stock planning
and sales, and improved key account reporting. SDG has
also strengthened its competitive position, delivering
enhanced customer value and building long-term resil -
ience. Ultimately, the project has transformed SDG into
a more innovative, customer-focused, and data-driven
organisation.
Although the overall evaluation of the solution was
largely positive, the associate also highlighted areas for
further work in the final report, including expanding the
business’s BI and analytics staff, formalising data gover -
nance and standard operating procedures, and continu -
ing to provide training and workshops to strengthen
data-driven decision-making across the organisation.
6 Design principles
Based on the design and implementation of the CRM-BI
platform and associated strategic and operational arte -
facts, we propose design principles to guide the devel -
opment of CRM-BI solutions in similar contexts. These
design principles emerged from the design process and
are embodied in the overall solution.
The first design principle focuses on the overall rela -
tionship and sequencing of the full suite of organisa -
tional and technical artefacts that make up the solution.
The overall solution highlights the need for the customer
strategy, key account relationship model, and service
blueprint to precede the development of the CRM-BI
technical solution. This is because these organisational
CRM artefacts are necessary to inform the design of the
CRM-BI platform. To successfully develop the customer
strategy also requires analysing data on current custom -
ers, including segmentation and value analysis. This ini -
tial analysis is necessary to develop the strategy, which
subsequently informs the CRM-BI platform. This analy -
sis can also help identify important KPIs and issues with
data access and quality, which are critical to the develop -
ment of the CRM-BI platform.
For example, these organisational artefacts should be
used to inform the data that is presented in the dash -
board KPIs. This is necessary to ensure that the dash -
board design aligns with the organisation’s strategic and
operational objectives. Organisations have access to a
vast array of data, making it necessary to focus on the
most important KPIs and metrics. Failure to incorpo -
rate key insights from strategic and operational artefacts
could result in a dashboard that presents irrelevant infor-
mation, making it difficult for decision-makers to focus
on what is most important to the organisation’s goals and
vision.
DP1 Strategic and organisational CRM arte -
facts, including customer strategy and relationship
management processes, should precede and inform
the overall strategy and the design of the technical BI
solution.
The business’s overarching strategy should also inform
the design of the CRM-BI dashboard. The broader organ-
isational strategy developed as part of the project is
embodied in the organisation’s strategic pillars. These
strategic pillars directly highlight the need for a business
intelligence solution, specifically a CRM-focused one.
The business’s core strategic objectives of smart growth,
innovation and customer centricity all require data and
insights, with smart growth and customer centricity
requiring CRM data and insights. The business’s inno -
vation objectives centre on making more effective use of
data to support other strategic objectives. To ensure the
project’s overall success, the technical BI platform arte -
fact was driven by these strategic objectives, rather than
pursuing analytics for its own sake without a clear busi -
ness objective. The strategic pillars also informed the
type of data and analytics required, which, in this proj -
ect, focused on CRM. The detailed KPIs presented in the
dashboard, therefore, centre on areas of strategic impor -
tance and are also informed by the CRM artefacts. Given
the need to ensure that BI is driven by strategic objec -
tives, we propose this as a core design principle.
DP2 CRM-BI design and instantiation should be driven
by the organisation’s strategic objectives.
Our overall solution design highlights the need to
combine both qualitative and quantitative information
to develop the CRM-BI solution. For example, to effec -
tively manage key accounts, quantitative data on orders
and financial performance were required, alongside more
qualitative information on key members of the customer
organisation, their priorities, and the quality and strength
of the relationship. Combining qualitative and quantita -
tive insights in the key account relationship artefact ulti -
mately yielded a more effective solution than relying on
either approach in isolation.
DP3 Combine quantitative customer analytics with
qualitative relationship mapping.
To develop the customer engagement model, it was
necessary to map the customer journey stages and cap -
ture data related to each stage. Much of the data required
at this stage was not held in internal information systems,
necessitating collection from a range of sources, includ -
ing websites, social media, emails, satisfaction scores,
and qualitative feedback. The specific data required
and its sources differed across the customer journey. To
effectively capture the required data, it was therefore
necessary to map stages of the customer journey to data
sources. The collection and analysis of this data pro -
vided crucial insights into business opportunities at each
stage of the customer journey, which informed the cus -
tomer engagement model. For example, business insights

Page 16 of 20
Zhang et al. Journal of Digital Management              (2026) 2:3
included development opportunities, potential leads, and
referrals.
DP4 Link customer journey stages to specific data-cap -
ture and insight-generation mechanisms.
To ensure the successful rollout and use of BI dash -
boards, they need to be embedded in wider organisa -
tional processes, including governance, training and
meeting routines. From a governance perspective, two
areas were particularly important to SDG. The first was
ensuring data security and privacy, achieved through
secure data storage, role-based access, and dashboard
views. This meant that end users could only view appro -
priate data. The second was to ensure appropriate pro -
cesses and policies for the collection, storage, and use of
data within the organisation. This helped formalise these
processes and improve data quality.
End users were also trained to use the dashboard’s
functionality and interpret the data. As analytics capa -
bility was new to SDG, upskilling staff was crucial to
ensure that analytics led to improved decision-making.
The dashboard also became a central part of meetings
within the organisation, becoming embedded in the typi -
cal meeting routine. This helped to ensure that decisions
within the organisation became more data-driven.
DP5 Embed dashboard deployment in governance,
training, and meeting routines.
Our final design principle focuses on the overall pro -
cess and the roles of the associate, business, and aca -
demic teams in the project. The associate developed the
project’s main artefacts, with support from the academic
team and the business. Crucial to this process was close
communication among the associate, business, and aca -
demic teams. The associate was embedded within the
business throughout the two-year project, facilitating
ongoing communication and refinement of artefacts and
incorporating qualitative business insights and knowl -
edge into artefact design. The associate also maintained
close communication with the academic team through
fortnightly supervision meetings, facilitating knowl -
edge transfer and further enhancing the design of the
artefacts. This interaction was crucial to the design of
the artefacts and represented a key process-level design
principle. This close interaction also helped ensure the
artefacts were grounded in business knowledge and met
the organisation’s requirements. Ultimately, the CRM-BI
solution designed in this project would have been more
challenging to design and implement through an arm’s-
length consultancy relationship.
DP6 The developer of CRM-BI solution artefacts
should be embedded within the organisation, with close
communication among stakeholders to ensure that
business and academic knowledge is embedded in the
artefacts.
7 Discussion
Following the design science methodology, we undertook
a collaborative university-industry project with an SME
supplier in the construction industry to design, develop
and implement a CRM-BI solution within the business.
The design and implementation of the CRM-BI solu -
tion have resulted in a range of benefits for the business.
The project enables employees and the senior manage -
ment team to take a more data-driven approach to CRM
decision-making. The CRM artefacts provide a frame -
work for guiding customer interactions and measur -
ing performance. The design and implementation of the
CRM-BI solution and the associated training also helped
drive cultural change within the business, leading to new
CRM processes, continuous improvement, and increased
accountability. Increased automation of data analysis has
resulted in time savings and greater efficiency. From a
practical perspective, the benefits of the project helped
the company achieve its overarching business aim of
improving CRM and ultimately business growth.
From a research perspective, we contribute new design
knowledge. Our main proposition from the study is that
integrating the design of CRM and BI artefacts is more
effective than designing these artefacts in isolation. This
proposition is captured in our overarching framework
and design principles. The guiding framework links the
key artefacts in developing the CRM-BI solution. This
framework builds on the CRM literature, which concep -
tualises CRM as comprising technologies, business pro -
cesses, and strategies (Zablah et al., 2004). We build on
these multidimensional and interrelated perspectives on
CRM, presenting an integrated framework that links stra-
tegic, process, and technical artefacts. Our framework
provides more depth than existing conceptualisations by
presenting the specific artefacts within these categories
as well as their interlinkages. Although there has been
debate in the design science literature about whether
organisational artefacts are appropriate in design science
research (Winter, 2008), we view these as crucial com -
ponents of our overall information system alongside the
focal technical artefact. This approach aligns with the
recognition in the broader information systems literature
that both technical and organisational components are
important (Winter, 2008).
The study resulted in design principles that can be con-
sidered when developing CRM-BI solutions in SMEs.
Our artefacts and design principles include the CRM-BI
platform as the central technical artefact, and demon -
strate how this is underpinned by strategic and business
process artefacts. These design principles support exist -
ing research highlighting the importance of data gover -
nance (Corallo et al., 2023), data quality (Corallo et al.,
2023; Hausladen & Schosser, 2020), training, skills and
leadership (Cosic et al., 2015; Klievink et al., 2017), and

Page 17 of 20
Zhang et al. Journal of Digital Management              (2026) 2:3
technical resources (Comuzzi & Patel, 2016; Gökalp et
al., 2021). However, we also extend this literature, high -
lighting the interrelationships between strategic, process,
and technical artefacts in developing solutions.
The design principles from our integrated CRM-BI
solution point to the need to draw on strategic and pro -
cess artefacts to inform the development of the techni -
cal solution. Studies have indicated that decision-makers
can typically only hold a small amount of information in
short-term memory, often posited as around 3–5 chunks
of information (Cowan, 2001). This means that it is nec -
essary to carefully design dashboards that present only
the most important information. Incorporating irrelevant
and unnecessary information can result in ‘paralysis by
analysis’ (Langley, 1995). Drawing on strategic and opera-
tional artefacts in dashboard design, alongside ongoing
engagement with end users, can help ensure that dash -
boards are effective tools for decision-making.
During the project, we encountered several challenges
in developing the CRM-BI platform. Here, we discuss our
approach to overcoming them, with the aim of provid -
ing further insights to guide the management of CRM-BI
projects. The first and most critical one is the availability
and ease of access to existing data and the lack of a clear,
concise data governance structure. The data is stored in
different units or functions across SDG and is also held
by external system suppliers. We had to develop a deep
understanding of the business processes and practices
to obtain relevant information. Usage of third-party
applications to collect and store customer/product data
made it challenging for SDG to access its own up-to-date
data. The second is the organisational challenge, which
underlines the lack of analytical competency in the exist -
ing workforce and the struggle to build a data culture
among employees. Because employees lack the knowl -
edge and capability to conduct in-depth data analysis,
securing their buy-in for data-driven strategy planning is
challenging. Third, scaling and automating data analysis
and reporting is another challenge, given the company’s
heavy reliance on external parties to generate data-driven
reports. The fourth challenge is change management. The
team invested substantial effort into building trust with
employees to promote the changes in the business. This
focused on gathering employee opinions to inform the
design and on creating a collective effort, ultimately lead-
ing to buy-in for the changes.
The final project evaluation highlighted two aspects
essential to further promote the adoption of business
analytics to drive growth beyond the project. The first is
maintaining momentum. Ownership and accountability
for data-driven decision-making are critical among staff.
The senior management team led by example during the
platform’s implementation. SDG has devised systems and
processes to implement the new practices, and the senior
management team have worked to integrate these into
employees’ daily routines alongside allocating respon -
sibility for KPIs. Focusing on BI development should be
viewed as an ongoing function within the company. The
second is employee upskilling. The project highlights the
importance of developing internal analytics human capi -
tal to enable the data analysis, interpretation of insights,
and implementation of findings. This capability develop -
ment requires ongoing training to develop initial capa -
bilities as well as developing capabilities in emerging
analytics technologies. Recruitment of external analytics
staff, alongside internal capability building, also helped to
strengthen the business’s overall CRM-BI capability.
In addition to its practical contributions, the study
advances the business analytics literature by integrating
CRM and BI. Existing design science literature focusing
on business analytics has drawn on kernel theory from
areas such as criminology (Vо & Plachkinovа, 2023),
socio-technical systems theory (Dremel et al., 2020), and
the theory of effective use (Ruoff et al., 2023). Our find -
ings contribute to this literature by incorporating CRM
alongside BI into the design, development, implementa -
tion, and evaluation of the CRM-BI platform artefact
and the supporting strategic and process artefacts. This
approach has revealed specific benefits, challenges, and
opportunities from CRM-BI solutions. Businesses can
draw on these insights to innovate with and enhance
their CRM-BI capabilities, with the aim of enhancing
firm performance.
8 Conclusions
Designing and implementing CRM-BI solutions is chal -
lenging for SMEs, involving the creation of strategic,
process, and technical artefacts. Drawing on the design
science method to address our initial research ques -
tions, this study provides a rich description of the design
of CRM-BI artefacts in an SME, as well as new design
knowledge in the form of design principles. The find -
ings highlight the interlinkages between artefacts and the
need for a holistic approach to developing CRM-BI capa -
bilities in SMEs.
8.1 Limitations and future research
As with other design science research, the main limi -
tation concerns the generalisability of the findings to
other contexts. Although we ground our design science
approach in CRM and BI theory and practice, it is impor-
tant to keep in mind that the study’s empirical com -
ponent is situated within a specific firm and industry,
focusing on a single case. For example, artefacts such as
the cluster analysis are based on firm-specific data. The
specific strategies and processes designed should also be
generalised with caution, considering differences in con -
text. Future studies could consider CRM-BI applications

Page 18 of 20
Zhang et al. Journal of Digital Management              (2026) 2:3
in other contexts to explore the generalisability of the
findings to other industries. Both CRM and BI are impor-
tant across all industries, creating the potential to apply
the design science methodology to address similar organ-
isational problems in diverse contexts. Future work could
also extend the framework to other functions of the busi -
ness, for example, a similar approach could be adopted in
areas such as finance or human resource management,
combining the strategic and organisational artefacts with
BI platform design. This could help to establish the gen -
eralisability of the findings to other business functions.
Although we ground the project in established theory, it
is difficult to establish causality. Future work could there-
fore draw on the framework presented in this study to
examine causality using other methods, such as experi -
mental approaches.
Our design and evaluation approach also has certain
limitations arising from the nature and design of the
overall project. Rather than proceeding through clearly
delineated design cycles, the project was carried out
based on a workplan. In the context of the SME, forma -
tive feedback was often ad hoc and informal, with issues
and updates to artefacts occurring in a less-structured
fashion. This may be partly due to the SME context of
the project, and partly due to following an existing KTP
workplan-based approach. Our overall artefact evalua -
tion approach also focuses on summative evidence doc -
umented in the final report, with questions completed
independently by the company, academic team, and asso-
ciate. Although this provides triangulation from mul -
tiple sources, other evidence would also be useful, such
as ongoing survey data from end users and, potentially,
experimental evidence demonstrating the impact of the
artefacts. The completion of the final report and evalua -
tion was carried out by project participants, introducing
potential bias into more qualitative assessments of the
project.
Although our project lasted for two years, future
work could consider extending the evaluation period to
account for longer-term benefits from the artefacts, as
well as identifying any longer-term risks and issues that
may arise. This longer-term evaluation may be particu -
larly useful in the context of rapidly evolving areas of
CRM and BI. In this context, it is likely that the original
design requirements are updated and change to meet the
evolving business needs, as well as to take advantage of
new technological developments.
Future work could also consider extending the techni -
cal BI solution. This could include incorporating predic -
tive and prescriptive analytics. Future solutions could
also draw on generative AI in dashboard design to enable
more interactive and conversational interfaces. This
could help make the BI platform more accessible to staff
who lack the technical skills to interact with the graphical
user interface. Generative AI could also be used in future
studies to assist in the design of strategic and organisa -
tional artefacts, such as planning, writing, and editing
strategic CRM documents.
Supplementary Information
The online version contains supplementary material available at  h t t  p s : /  / d o  i .  o r
g / 1 0 . 1 0 0 7 / s 4 4 3 6 2 - 0 2 6 - 0 0 0 2 4 - x     .
Supplementary Material 1
Author contributions
MZ: Conceptualization, Methodology, Writing – original draft, writing – review
and editing. BG: Methodology, Writing – original draft, writing – review
and editing. JMcC: Conceptualization, writing – review and editing. LS:
Conceptualization, writing – review and editing.
Funding
The research is funded by the Innovate UK Knowledge Transfer Partnership
(S2476MGT).
Data availability
No datasets were generated or analysed during the current study.
Declarations
Competing interests
Louise Skeath is CEO of the focal company in the study.
Received: 9 April 2026 / Revised: 7 May 2026 / Accepted: 15 June 2026
References
Amirasari, H., & Andrias, M. S. (2024). Implementation of Design Science for Devel-
oping BI Dashboard Employee Engagement Survey. Quantitative Economics
and Management Studies, 5(4), 793–804.  h t t  p s : /  / d o  i .  o r g / 1 0 . 3 5 8 7 7 / 4 5 4 r i . q e m
s 2 6 9 9
Ashrafi, A., & Zareravasan, A. (2022). An ambidextrous approach on the business
analytics-competitive advantage relationship: Exploring the moderating role
of business analytics strategy. Technological Forecasting and Social Change,
179(January), 121665. https:/ /doi.or g/10.10 16/j .techfore.2022.121665
Ates, A., Paton, S., Bititci, U., & Kemal Konyalıoğlu, A. (2025). From transfer to co-
creation: action research perspectives in knowledge transfer partnership
(KTP) projects. Production Planning and Control, 36(2), 236–249.  h t t  p s : /  / d o  i .  o r g
/ 1 0 . 1 0 8 0 / 0 9 5 3 7 2 8 7 . 2 0 2 4 . 2 3 3 5 4 7 5
Avdiji, H., Elikan, D., Missonier, S., & Pigneur, Y. (2020). A design theory for visual
inquiry tools. Journal of the Association for Information Systems, 21(3), 695–734.
https:/ /doi.or g/10.17 705/ 1jais.00617
Aziah, N., Kasim, A., & Minai, B. (2009). Linking CRM Strategy, Customer Perfor-
mance Measures and Performance in the Hotel Industry. International Journal
of Economics and Management, 3(2), 297–316.
Chang, W., Park, J. E., & Chaiy, S. (2010). How does CRM technology transform
into organizational performance? A mediating role of marketing capability.
Journal of Business Research, 63(8), 849–855.  h t t  p s : /  / d o  i .  o r g / 1 0 . 1 0 1 6 / j . j b u s r e s
. 2 0 0 9 . 0 7 . 0 0 3
Chen, I. J., & Popovich, K. (2003). Understanding customer relationship manage-
ment (CRM): People, process and technology. Business Process Management
Journal, 9(5), 672–688. https:/ /doi.or g/10.11 08/1 4637150310496758
Combita Niño, H. A., Cómbita Niño, J. P ., & Morales Ortega, R. (2020). Business intel-
ligence governance framework in a university: Universidad de la costa case
study. International Journal of Information Management, 50, 405–412.  h t t  p s : /  / d
o  i .  o r g / 1 0 . 1 0 1 6 / j . i j i n f o m g t . 2 0 1 8 . 1 1 . 0 1 2
Comuzzi, M., & Patel, A. (2016). How organisations leverage: Big Data: A maturity
model. Industrial Management and Data Systems, 116(8), 1468–1492.  h t t  p s : /  / d
o  i .  o r g / 1 0 . 1 1 0 8 / I M D S - 1 2 - 2 0 1 5 - 0 4 9 5

Page 19 of 20
Zhang et al. Journal of Digital Management              (2026) 2:3
Corallo, A., Crespino, A. M., Vecchio, D., Gervasi, V., Lazoi, M., M., & Marra, M. (2023).
Evaluating maturity level of big data management and analytics in industrial
companies. Technological Forecasting and Social Change, 196(August), 122826.
https:/ /doi.or g/10.10 16/j .techfore.2023.122826
Cosic, R., Shanks, G., & Maynard, S. (2015). A business analytics capability frame-
work. Australasian Journal of Information Systems, 19, S5–S19.  h t t  p s : /  / d o  i .  o r g /
1 0 . 3 1 2 7 / a j i s . v 1 9 i 0 . 1 1 5 0
Cowan, N. (2001). The magical number 4 in short-term memory: A reconsidera-
tion of mental storage capacity. Behavioral and Brain Sciences, 24(1), 87–114.
https:/ /doi.or g/10.10 17/S 0140525X01003922
Delen, D., & Demirkan, H. (2013). Data, information and analytics as services. Deci-
sion Support Systems, 55(1), 359–363. https:/ /doi.or g/10.10 16/j .dss.2012.05.044
Delen, D., & Ram, S. (2018). Research challenges and opportunities in business
analytics. Journal of Business Analytics, 1(1), 2–12.  h t t  p s : /  / d o  i .  o r g / 1 0 . 1 0 8 0 / 2 5 7
3 2 3 4 X . 2 0 1 8 . 1 5 0 7 3 2 4
Dremel, C., Stoeckli, E., & Wulf, J. (2020). Management of analytics-as-a-service -
results from an action design research project. Journal of Business Analytics,
3(1), 1–16. https:/ /doi.or g/10.10 80/2 573234X.2020.1740616
Dubey, R., Bryde, D. J., Graham, G., Foropon, C., Kumari, S., & Gupta, O. (2021). The
role of alliance management, big data analytics and information visibility on
new-product development capability. Annals of Operations Research.  h t t  p s : /  /
d o  i .  o r g / 1 0 . 1 0 0 7 / s 1 0 4 7 9 - 0 2 1 - 0 4 3 9 0 - 9
Duque, J., Godinho, A., & Vasconcelos, J. (2022). Knowledge data extraction for
business intelligence A design science research approach. Procedia Computer
Science, 204, 131–139. https:/ /doi.or g/10.10 16/j .procs.2022.08.016
Eckerson, W. W. (2012). Performance Dashboard Measuring, Monitoring, and Manag-
ing Your Business. John Wiley & Sons, Inc.
Frow, P . E., & Payne, A. F. (2009). Customer Relationship Management: A Strategic
Perspective. Journal of Business Market Management, 3(1), 7–27.  h t t  p s : /  / d o  i .  o r
g / 1 0 . 1 0 0 7 / s 1 2 0 8 7 - 0 0 8 - 0 0 3 5 - 8
Galetsi, P ., & Katsaliaki, K. (2020). A review of the literature on big data analytics in
healthcare. Journal of the Operational Research Society, 71(10), 1511–1529.
https:/ /doi.or g/10.10 80/0 1605682.2019.1630328
Gledson, B., Rogage, K., Thompson, A., & Ponton, H. (2024). Reporting on the
Development of a Web-Based Prototype Dashboard for Construction Design
Managers, Achieved through Design Science Research Methodology (DSRM).
Buildings, 14(2). https:/ /doi.or g/10.33 90/b uildings14020335
Gökalp, M. O., Gökalp, E., Kayabay, K., Koçyiğit, A., & Eren, P . E. (2021). Data-driven
manufacturing: An assessment model for data science maturity. Journal of
Manufacturing Systems, 60(July), 527–546.  h t t  p s : /  / d o  i .  o r g / 1 0 . 1 0 1 6 / j . j m s y . 2 0 2
1 . 0 7 . 0 1 1
Gregor, S., & Hevner, A. (2013). Positioning and presenting design science research
for maximum impact. MIS Quarterly, 37(2), 337-355.  h t t  p s : /  / w w  w .  j s t o r . o r g / s t a
b l e / 4 3 8 2 5 9 1 2
Gupta, M., & George, J. F. (2016). Toward the development of a big data analytics
capability. Information and Management, 53(8), 1049–1064.  h t t  p s : /  / d o  i .  o r g / 1 0
. 1 0 1 6 / j . i m . 2 0 1 6 . 0 7 . 0 0 4
Habul, A., & Pilav-Velic, A. (2010). Business intelligence and customer relation-
ship management. Proceedings of the ITI 2010 32nd Int. Conf. on Information
Technology Interfaces, 169–174.
Hausladen, I., & Schosser, M. (2020). Towards a maturity model for big data analyt-
ics in airline network planning. Journal of Air Transport Management, 82(Sep-
tember 2019), 101721. https:/ /doi.or g/10.10 16/j .jairtraman.2019.101721
Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design Science in Information
Systems Research. MIS Quarterly, 28(1), 75–105.  h t t  p s : /  / w w  w .  j s t o r . o r g / s t a b l e
/ 2 5 1 4 8 6 2 5
Holmström, J., Ketokivi, M., & Hameri, A. P . (2009). Bridging practice and theory: A
design science approach. Decision Sciences, 40(1), 65–87.  h t t  p s : /  / d o  i .  o r g / 1 0 . 1
1 1 1 / j . 1 5 4 0 - 5 9 1 5 . 2 0 0 8 . 0 0 2 2 1 . x
Iivari, J. (2020). Editorial: A critical look at theories in design science research.
Journal of the Association for Information Systems,21(3), 502–519. Association
for Information Systems. https:/ /doi.or g/10.17 705/ 1jais.00610
Kao, H. Y., Yu, M. C., Masud, M., Wu, W. H., Chen, L. J., & Wu, Y. C. J. (2016). Design and
evaluation of hospital-based business intelligence system (HBIS): A founda-
tion for design science research methodology. Computers in Human Behavior,
62, 495–505. https:/ /doi.or g/10.10 16/j .chb.2016.04.021
Khodakarami, F., & Chan, Y. E. (2014). Exploring the role of customer relationship
management (CRM) systems in customer knowledge creation. Information
and Management, 51(1), 27–42. https:/ /doi.or g/10.10 16/j .im.2013.09.001
Klievink, B., Romijn, B. J., Cunningham, S., & de Bruijn, H. (2017). Big data in the
public sector: Uncertainties and readiness. Information Systems Frontiers, 19(2),
267–283. https:/ /doi.or g/10.10 07/s 10796-016-9686-2
Langley, A. (1995). Between paralysis by analysis and extinction by instinct. Sloan
Management Review, 3(36), 63–77.
Ledro, C., Nosella, A., & Dalla Pozza, I. (2023). Integration of AI in CRM: Challenges
and guidelines. Journal of Open Innovation: Technology Market and Complexity,
9(4). https:/ /doi.or g/10.10 16/j .joitmc.2023.100151
Lee, J. H., & Park, S. C. (2005). Intelligent profitable customers segmentation system
based on business intelligence tools. Expert Systems with Applications, 29(1),
145–152. https:/ /doi.or g/10.10 16/j .eswa.2005.01.013
Lepenioti, K., Bousdekis, A., Apostolou, D., & Mentzas, G. (2020). Prescriptive
analytics: Literature review and research challenges. International Journal of
Information Management,50, 57–70. Elsevier Ltd.  h t t  p s : /  / d o  i .  o r g / 1 0 . 1 0 1 6 / j . i j i n
f o m g t . 2 0 1 9 . 0 4 . 0 0 3
Li, L., Lin, J., Ouyang, Y., Luo, X., & Robert. (2022). Evaluating the impact of big data
analytics usage on the decision-making quality of organizations. Technologi-
cal Forecasting and Social Change, 175.  h t t  p s : /  / d o  i .  o r g / 1 0 . 1 0 1 6 / j . t e c h f o r e . 2 0 2
1 . 1 2 1 3 5 5
Lismont, J., Vanthienen, J., Baesens, B., & Lemahieu, W. (2017). Defining analytics
maturity indicators: A survey approach. International Journal of Information
Management, 37(3), 114–124. https:/ /doi.or g/10.10 16/j .ijinfomgt.2016.12.003
Menukin, O., Mandungu, C., Shahgholian, A., & Mehandjiev, N. (2023). Guiding the
integration of analytics in business operations through a maturity framework.
Annals of Operations Research. https:/ /doi.or g/10.10 07/s 10479-023-05614-w
Mikalef, P ., Boura, M., Lekakos, G., & Krogstie, J. (2019). Big data analytics and firm
performance: Findings from a mixed-method approach. Journal of Business
Research, 98(January), 261–276. https:/ /doi.or g/10.10 16/j .jbusres.2019.01.044
Mikalef, P ., Krogstie, J., Pappas, I. O., & Pavlou, P . (2020). Exploring the relationship
between big data analytics capability and competitive performance: The
mediating roles of dynamic and operational capabilities. Information and
Management, 57(2). https:/ /doi.or g/10.10 16/j .im.2019.05.004
Nam, D., Lee, J., & Lee, H. (2019). Business analytics use in CRM: A nomological net
from IT competence to CRM performance. International Journal of Information
Management, 45, 233–245. https:/ /doi.or g/10.10 16/j .ijinfomgt.2018.01.005
Nguyen, T. U. H., Sherif, J. S., & Newby, M. (2007). Strategies for successful CRM
implementation. Information Management and Computer Security, 15(2),
102–115. https:/ /doi.or g/10.11 08/0 9685220710748001
Payne, A., Frow, P ., & Marketing, R. (2005). A Strategic Framework for Customer
Relationship Management. American Marketing Association, 69, 167–176.
Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design
science research methodology for information systems research. Journal of
Management Information Systems, 24(3), 45–77.  h t t  p s : /  / d o  i .  o r g / 1 0 . 2 7 5 3 / M I S 0
7 4 2 - 1 2 2 2 2 4 0 3 0 2
Phan, D. D., & Vogel, D. R. (2010). A model of customer relationship management
and business intelligence systems for catalogue and online retailers. Informa-
tion and Management, 47(2), 69–77. https:/ /doi.or g/10.10 16/j .im.2009.09.001
Recker, J. (2021). Improving the state-tracking ability of corona dashboards. Euro-
pean Journal of Information Systems, 30(5), 476–495.  h t t  p s : /  / d o  i .  o r g / 1 0 . 1 0 8 0 / 0
9 6 0 0 8 5 X . 2 0 2 1 . 1 9 0 7 2 3 5
Ruoff, M., Gnewuch, U., Maedche, A., & Scheibehenne, B. (2023). Designing
Conversational Dashboards for Effective Use in Crisis Response. Journal of the
Association for Information Systems, 24(6), 1500–1526.  h t t  p s : /  / d o  i .  o r g / 1 0 . 1 7 7
0 5 / 1 j a i s . 0 0 8 0 1
Smyth, C., Dennehy, D., Fosso Wamba, S., Scott, M., & Harfouche, A. (2024). Artificial
intelligence and prescriptive analytics for supply chain resilience: a systematic
literature review and research agenda. International Journal of Production
Research, 62(23), 8537–8561. Taylor and Francis Ltd.  h t t  p s : /  / d o  i .  o r g / 1 0 . 1 0 8 0 / 0
0 2 0 7 5 4 3 . 2 0 2 4 . 2 3 4 1 4 1 5
Tuunanen, T., Winter, R., & vom Brocke, J. (2024). Dealing with complexity in design
science research: A methodology using design echelons. MIS Quarterly:
Management Information Systems, 48(2), 427–458.  h t t  p s : /  / d o  i .  o r g / 1 0 . 2 5 3 0 0 /
M I S Q / 2 0 2 3 / 1 6 7 0 0
Venable, J., Pries-Heje, J., & Baskerville, R. (2016). FEDS: A framework for evaluation
in design science research. European Journal of Information Systems, 25(1),
77–89). Palgrave Macmillan Ltd. https:/ /doi.or g/10.10 57/e jis.2014.36
Vо, A., & Plachkinovа, M. (2023). Showcase: A Data-Driven Dashboard for Federal
Criminal Sentencing. Journal of the Association for Information Systems, 24(6),
1479–1499. https:/ /doi.or g/10.17 705/ 1jais.00796
vom Brocke, J., Hevner, A. R. & Maedche, A. (Eds.) (2020). Design Science Research.
Cases. Progress in IS. Springer, Cham.
Wang, X., Wang, Y., Li, N., & Zhao, Y. (2025). Low-code AI enabling marketing
innovation: The mediating role of marketing ambidexterity. Journal of Digital
Management, 1(1). https:/ /doi.or g/10.10 07/s 44362-025-00015-4

Page 20 of 20
Zhang et al. Journal of Digital Management              (2026) 2:3
Watson, H. J. (2002). Recent developments in data warehousing. Communications
of the Association for Information Systems, 8.  h t t  p s : /  / d o  i .  o r g / 1 0 . 1 7 7 0 5 / 1 c a i s . 0
0 8 0 1
Winter, R. (2008). Design science research in Europe. European Journal of Informa-
tion Systems,17(5), 470–475. Palgrave Macmillan Ltd.  h t t  p s : /  / d o  i .  o r g / 1 0 . 1 0 5 7
/ e j i s . 2 0 0 8 . 4 4
Xu, X., Wang, X., Li, Y., & Haghighi, M. (2017). Business intelligence in online cus-
tomer textual reviews: Understanding consumer perceptions and influential
factors. International Journal of Information Management, 37(6), 673–683.
https:/ /doi.or g/10.10 16/j .ijinfomgt.2017.06.004
Zablah, A. R., Bellenger, D. N., & Johnston, W. J. (2004). An evaluation of divergent
perspectives on customer relationship management: Towards a common
understanding of an emerging phenomenon. Industrial Marketing Manage-
ment, 33(6), 475–489. https:/ /doi.or g/10.10 16/j .indmarman.2004.01.006
Zaitsev, A., & Mankinen, S. (2022). Designing financial education applications for
development: applying action design research in Cambodian countryside.
European Journal of Information Systems, 31(1), 91–111.  h t t  p s : /  / d o  i .  o r g / 1 0 . 1 0 8
0 / 0 9 6 0 0 8 5 X . 2 0 2 1 . 1 9 7 8 3 4 1
Zampou, E., Mourtos, I., Pramatari, K., & Seidel, S. (2022). A Design Theory for
Energy and Carbon Management Systems in the Supply Chain. Journal of the
Association for Information Systems, 23(1), 329–371.  h t t  p s : /  / d o  i .  o r g / 1 0 . 1 7 7 0 5
/ 1 j a i s . 0 0 7 2 5
Zerbino, P ., Aloini, D., Dulmin, R., & Mininno, V. (2018). Big Data-enabled Customer
Relationship Management: A holistic approach. Information Processing and
Management, 54(5), 818–846. https:/ /doi.or g/10.10 16/j .ipm.2017.10.005
Zolbanin, H., & Aubert, B. (2025). A process model for design-oriented machine
learning research in information systems. Journal of Strategic Information
Systems, 34(1). Elsevier B.V. https:/ /doi.or g/10.10 16/j .jsis.2024.101868
Publisher’s note
Springer Nature remains neutral with regard to jurisdictional claims in
published maps and institutional affiliations.
