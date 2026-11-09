---
title: N8n Based Digital Marketing Workflow Automation for the Operational Efficiency of a Service Company
url: https://doi.org/10.59141/jist.v7i8.9240
category: digital-marketing
subcategory: framework
date: 2026-10
venue: Jurnal Indonesia Sosial Teknologi
authors:
- Rafi Farizki
source: openalex-oa
pdf_url: https://jist.publikasiindonesia.id/index.php/jist/article/download/9240/3059
pages: 15
chars: 39968
fetched_at: '2026-11-08T19:15:33+00:00'
kb_version: 1
---

# N8n Based Digital Marketing Workflow Automation for the Operational Efficiency of a Service Company

Available online a https://jist.publikasiindonesia.id/index.php/jist/index 433

E-ISSN: 2745-5254
Vol. 7, No. 8, August 2026, pp 433-447
https://doi.org/10.59141/jist.v7i8.9240

N8n Based Digital Marketing Workflow Automation for the
Operational Efficiency of a Service Company

Rafi Farizki
Politeknik Siber Cerdika Internasional, Indonesia
Coresponding Author: rafifarizki90@gmail.com
Keywords:  ABSTRACT
digital marketing, low code, n8n,
operational efficiency, workflow
automation

This is an open access article under the CC BY-
SA license.

Copyright © 2026 by Author. Published by
Publikasi Indonesia
 Digital marketing teams in service companies still spend much of their
day on manual operational work, from consolidating leads that arrive
through multiple channels and forwarding each one to the sales team,
to compiling periodic reports for management. This study aims to
design, implement, and evaluate digital marketing workflow
automation based on n8n, an open source low code workflow
automation platform, to improve the operational efficiency of a service
company. The research takes a qualitative, descriptive case study
approach in the digital marketing division of a multi brand service
company in West Java, Indonesia. Data were collected through
participant observation, workflow documentation, and interviews with
internal users, then analyzed through data condensation, data display,
and conclusion drawing. The study produces three findings. First, four
of the most burdensome manual workflows were identified: multi
channel lead consolidation, lead distribution to sales teams, weekly
performance reporting, and content monitoring. Second, all four were
automated through n8n workflows that connect web forms, social
media lead forms, a master spreadsheet, and instant messaging
channels under one trigger, normalization, storage, and notification
architecture. Third, automation cut the cycle time from lead arrival to
sales notification from hours to seconds, removed duplicate entries and
stray leads, and made weekly reporting consistent without manual
work. The findings show that a low code platform such as n8n lets a
mid sized service company build the kind of marketing automation
long associated with expensive commercial software, provided data
schema discipline and operational governance come with it.

INTRODUCTION
Digital transformation has fundamentally changed how service companies acquire
customers, manage marketing activities, and coordinate interactions between marketing
and sales departments. The increasing adoption of websites, social media platforms,
online advertising, and digital communication channels has created opportunities for

Rafi Farizki

Available online a https://jist.publikasiindonesia.id/index.php/jist/index 434

businesses to reach wider markets and improve customer engagement. However, the
expansion of digital marketing channels has also introduced operational challenges,
particularly in managing information generated across multiple platforms. Chaffey and
Ellis-Chadwick (2019) emphasize that effective digital marketing requires the integration
of digital technologies, customer information, and organizational processes to support
marketing objectives. Similarly, Kannan and Li (2017) explain that digital marketing
involves interconnected technologies, customer interactions, and organizational
capabilities that influence marketing effectiveness. These perspectives indicate that
successful digital marketing depends not only on promotional strategies but also on the
efficiency of the operational processes supporting them.
In service companies, digital marketing operations frequently involve repetitive
administrative activities, including collecting prospective customer information,
consolidating leads from different channels, distributing inquiries to sales teams,
monitoring content performance, and preparing management reports. These activities
become increasingly complex when companies manage multiple brands, each with
separate marketing channels, customer segments, and sales teams. Lead information
obtained through landing pages, social media forms, and other digital sources may require
manual processing before reaching the appropriate sales personnel. Consequently,
fragmented workflows can create delays, inconsistent data formats, duplicate records, and
additional administrative workloads. Such inefficiencies may reduce the responsiveness
of marketing operations and limit employees' capacity to focus on strategic activities,
including campaign optimization, content development, and customer relationship
management.
Marketing automation has emerged as an important approach to addressing these
operational challenges. Heimbach et al. (2015) describe marketing automation as a
technological approach that supports the systematic execution and coordination of
marketing activities. Järvinen and Taiminen (2016) examined marketing automation in
business-to-business content marketing and highlighted its relevance to lead management
and marketing processes. Furthermore, Mero et al. (2020) investigated effectual and
causal reasoning in marketing automation adoption, providing insights into how
organizations develop automation capabilities according to their available resources and
strategic objectives. These studies establish that marketing automation can support
organizational marketing activities, although the practical implementation of automation
depends on technological readiness, organizational resources, and process characteristics.
Beyond marketing-specific applications, the broader literature on robotic process
automation (RPA) provides a theoretical and practical foundation for understanding
workflow efficiency. Van der Aalst et al. (2018) discussed the potential of RPA to
automate repetitive, rule-based organizational tasks, while Hofmann et al. (2020)
examined its characteristics and implications for business processes. Syed et al. (2020)
further identified contemporary themes and challenges associated with RPA
implementation, including organizational integration, process suitability, and operational

Rafi Farizki

Available online a https://jist.publikasiindonesia.id/index.php/jist/index 435

management. Meanwhile, Aguirre and Rodriguez (2017)  presented a case study of
business process automation, demonstrating the relevance of automation technologies to
organizational workflows. Lacity and Willcocks (2016) also discussed service automation
as an approach to improving operational processes. Collectively, these studies indicate
that automation is particularly relevant to activities characterized by repetitive
procedures, structured data, and predictable decision rules.
Nevertheless, implementing automation through conventional commercial
software may present challenges for small and medium -sized service companies,
particularly when organizations must integrate multiple applications while maintaining
operational flexibility. Low-code and no-code development platforms offer an alternative
by enabling users to design and connect digital workflows through visual interfaces with
limited conventional programming requirements. Bock and Frank (2021) examined the
characteristics of low-code platforms, while Sahay et al. (2020) discussed approaches to
understanding and comparing low-code development environments. These studies
highlight the potential of low-code technologies to support application development and
system integration. Within this technological landscape, n8n provid es a workflow
automation environment through which organizations can connect applications, process
data, establish conditional operations, and automate information exchange across digital
systems.
Recent studies in Indonesia have begun examining the application of n8n across
different organizational settings. Pratama and Voutama (2026) investigated workflow
automation efficiency using n8n and reported improvements in the speed of data
transmission between integrated applications. Wali et al. (2025) examined the
implementation of n8n-based workflow automation in a sharia cooperative in Aceh,
highlighting its relevance to operational efficiency and organizational performance.
These investigations demonstrate the practical potential of n8n in automating routine
organizational processes. However, their research settings and operational objectives
differ from the requirements of multichannel digital marketing management in service
companies.
Other studies have explored n8n applications in specific business and information
management activities. Al Fajar et al. (2026) developed an automated service workflow
for a laundry business, while Sholihah et al. (2026) investigated a workshop registration
system integrating an artificial intelligence chatbot and multichannel notifications.
Pratama and Ahda (2025) examined an n8n-based AI agent for automated digital receipt
recording, whereas Ahmad et al. (2026) investigated workflow automation for a web-
based stock analysis agent. These studies contribute empirical examples of low -code
automation in consumer services, transaction documentation, registration systems, and
information processing. Nevertheless, their findings primarily concern individual service
processes or specific application functions rather than the integrated management of lead
acquisition, sales distribution, performance reporting, and content monitoring across
multiple brands.

Rafi Farizki

Available online a https://jist.publikasiindonesia.id/index.php/jist/index 436

Despite the growing literature on marketing automation, RPA, and low -code
platforms, several research gaps remain. First, previous marketing automation studies
have predominantly emphasized customer engagement, lead nurturing, and marketing
technology adoption, while the operational integration of repetitive digital marketing
workflows has received comparatively less attention in the literature reviewed. Second,
existing n8n studies have generally examined automation within individual services or
narrowly defined administrative processes, leaving limited empirical evidence
concerning integrated workflow automation across multiple marketing channels and
brands within a single service company. Third, previous investigations have not
sufficiently addressed how n8n -based workflow integration can be evaluated
simultaneously through lead-processing cycle time, data quality, and reporting
consistency in this particular organizational context. Fourth, although low-code platforms
reduce technical development barriers, further contextual evidence is needed regarding
the organizational governance, data standardization, and infrastructure requirements
necessary to sustain automated marketing operations.
These research gaps are particularly relevant to multibrand service companies,
where operational complexity increases as organizations expand their digital marketing
channels and customer acquisition activities. Without an integrated workflow
architecture, information generated from different platforms may remain fragmented,
requiring repeated manual processing and coordination between marketing and sales
personnel. The resulting inefficiencies create a practical need for automation solutions
that are adaptable to existing organizational systems and operational resources.
Consequently, investigating n8n-based automation within an actual multibrand service
company provides an opportunity to understand how low-code technology can support
operational integration while identifying the technical and organizational conditions
influencing its implementation.
The novelty of this study lies in its contextual and operational examination of n8n-
based digital marketing workflow automation within a multibrand service company in
West Java, Indonesia. Unlike previous studies focusing on individual administrative
functions, the present research integrates four interconnected digital marketing processes:
multichannel lead consolidation, automated lead distribution to sales teams, weekly
performance reporting, and content monitoring. These processes are organized through a
common four-layer architecture consisting of triggers, data normalization, centralized
storage, and automated notifications. Furthermore, the study evaluates automation
outcomes through three complementary dimensions of operational efficiency: processing
cycle time, data quality, and reporting consistency. This integrated perspective provides
a contextual contribution to understanding how low-code automation can be implemented
across interconnected marketing activities rather than isolated tasks.
An additional contribution of this study concerns the relationship between
technological automation and operational governance. Although low-code platforms
simplify workflow development, sustainable implementation requires consistent data

Rafi Farizki

Available online a https://jist.publikasiindonesia.id/index.php/jist/index 437

structures, reliable system infrastructure, secure application integration, and clearly
defined operational responsibilities. Accordingly, this research examines not only the
technical design of automated workflows but also the practical considerations associated
with their maintenance and reliability. This perspective extends the discussion of
workflow automation beyond technological functionality by emphasizing the
organizational arrangements required to maintain operational efficiency.
Based on these considerations, this study aims to design, implement, and evaluate
n8n-based digital marketing workflow automation to improve the operational efficiency
of a multibrand service company. Specifically, the research seeks to identify repetitive
manual workflows that contribute to operational inefficiency, develop an integrated
automation architecture connecting digital marketing channels with centralized data
management and sales notifications, and evaluate the observed changes in processing
cycle time, data quality, and reporting consistency following implementation. Through a
qualitative descriptive case study, the research examines these processes within their
actual organizational context to provide a detailed understanding of the automation
implementation and its operational outcomes.
Theoretically, this study contributes to the literature on digital marketing
automation, business process automation, and low-code technology adoption by
providing empirical insights into the integration of interconnected marketing workflows.
It also extends discussions of organizational automation by highlighting the relationship
between process standardization, technological integration, and operational governance.
Practically, the findings are expected to benefit digital marketing managers, sales teams,
automation developers, and service company decision-makers by providing a reference
for identifying automation priorities, designing integrated workflows, and establishing
operational controls. The proposed architecture may also serve as a contextual reference
for organizations seeking to reduce repetitive administrative work while improving the
consistency of information exchange across marketing and sales functions.
The managerial implications of this research emphasize the importance of
selecting repetitive and rule-based processes as initial automation priorities, establishing
standardized data structures before integrating multiple applications, and implementing
reliable monitoring mechanisms to maintain workflow continuity. For small and medium-
sized service companies, the findings may inform decisions concerning the adoption of
self-hosted, low-code automation as an alternative to more complex commercial
integration systems. However, the study does not establish that n8n is universally more
cost-effective than commercial alternatives, as a formal comparative cost analysis was
not conducted. Furthermore, because the investigation focuses on a single organizational
case, its findings are intended to provide analytical and practical insights rather than
statistically generalizable estimates of automation effectiveness. Ultimately, this research
seeks to demonstrate how integrated workflow automation can support more responsive,
consistent, and manageable digital marketing operations while identifying the governance
requirements necessary for sustainable implementation.

Rafi Farizki

Available online a https://jist.publikasiindonesia.id/index.php/jist/index 438

METHOD
Research Design
This study takes a qualitative approach in the form of a descriptive case study.
The case study design fits because the research examines a contemporary phenomenon,
digital marketing workflow automation, inside its real organizational context, where the
boundary between phenomenon and context cannot be drawn sharply  (Yin, 2018). The
research ran in four stages following a system design cycle: identifying the manual
workflows, designing the automation architecture, implementing the workflows on the
n8n platform, and evaluating operational efficiency qualitatively after implementation.
Figure 1 presents the stages.

Figure 1. Research Stages
Source: compiled by the researcher (2026)

Research Subject and Setting
The setting is the digital marketing division of a multi brand service company
headquartered in West Java that serves a national market. The division manages lead
acquisition for more than a dozen service brands through landing page forms, social
media lead forms, and organic blog traffic, with a separate sales team per brand. The
company's identity is anonymized at the organization's request. Research subjects include
the automation manager, digital marketing staff, and sales team representatives as
downstream users of the automated workflows.

Data Collection Techniques
Data were collected in three ways. First, participant observation, since the
researcher was directly involved in designing and operating the workflows and could
watch work before and after automation from the inside. Second, documentation,
covering n8n workflow diagrams, the master lead spreadsheet structure, workflow
execution logs, and archived weekly reports. Third, unstructured interviews with
marketing staff and the sales team about administrative workload before automation and
the changes felt afterwards. Together, the three allow cross checking between what was

Rafi Farizki

Available online a https://jist.publikasiindonesia.id/index.php/jist/index 439

designed, what actually ran in the system, and what users experienced. Table 1
summarizes the techniques, their data sources, and their outputs.

Table 1. Summary of Data Collection Techniques
Technique Data source Instrument Output
Participant
observation
Daily activities of the marketing
division before and after
automation
Field notes Map of manual
workflows and
bottlenecks
Documentation N8n workflow diagrams,
master spreadsheet,
execution logs, archived
weekly reports
Document review
sheet
Evidence of the
design and of the
running system
Unstructured
interviews
Digital marketing staff and sales
team representatives
Open question
guide
Perceived workload
and perceived
change
Source: compiled by the researcher (2026)

Data Analysis Technique
The analysis followed the three concurrent flows of qualitative analysis: data
condensation, data display, and conclusion drawing and verification (Miles et al., 2014) .
In condensation, observation notes and interview material were coded into workflow
categories, bottlenecks, and efficiency dimensions. In display, each workflow was
presented as a before and after pair alongside the architecture that replaced it. In
conclusion drawing, the changes on three efficiency dimensions, cycle time, data quality,
and reporting consistency, were read against the automation literature to establish the
contribution and its limits.

Trustworthiness
Trustworthiness rests on technique triangulation, comparing observations, system
documents, and user accounts before any efficiency claim is made; member checking,
confirming workflow descriptions with the staff who run them; and an audit trail in the
form of workflow execution logs that can be reinspected. The study's main limitation is
its position as a single case with qualitative evaluation, so the magnitudes of efficiency
gains are not meant to generalize statistically to the population of service companies.

Rafi Farizki

Available online a https://jist.publikasiindonesia.id/index.php/jist/index 440

RESULTS AND DISCUSSION
Identifying the Manual Workflows
Early observation and interviews identified the four manual workflows that
weighed most heavily on the digital marketing division. First, multi channel lead
consolidation. Leads arrive from each brand's landing page forms, from Meta and TikTok
lead forms, and from blog article tracking forms, and staff copy them one by one into a
master spreadsheet, each channel in a different format. Second, lead distribution to the
sales teams. Every new lead has to be forwarded by hand to the instant messaging group
of the relevant brand's sales team, so leads that arrive at night or on weekends wait until
the next day. Third, weekly performance reporting. Staff recap lead counts per brand and
per channel from several data sources and assemble them into a management report, work
that eats up to half a working day every week. Fourth, content monitoring, checking new
blog articles across brands and making sure each one is wired into the lead source tracking
mechanism.
The four workflows share the same profile: repetitive, governed by clear rules,
high in volume, built on moving data between applications, and rarely in need of human
judgment. That profile matches exactly the kind of task the robotic process automation
literature marks as most worth automating (Syed et al., 2020; van der Aalst et al., 2018),
so the four became the design targets.
The business cost of the manual flows is real and compounding. A lead that waits
goes cold, because prospective service customers typically contact several providers at
once and choose whoever responds first, so every hour of notification delay risks a lost
transaction. Manual copying also imposes cognitive load, since staff juggle multiple
channels while doing other work, a condition under which lapses are a consequence of
work design rather than of discipline. Automation priority was therefore set with three
plain considerations, event volume per day, repetition frequency, and clarity of the
decision rule; consolidation and distribution ranked highest because all three
considerations peak there.

Designing the Automation Architecture
The architecture was built on self hosted n8n so that lead data stays under the
company's control. Every workflow follows the same four layer pattern. The trigger layer
receives events, whether a webhook from a landing page form, periodic pulls of social
media lead form data, or a scheduler for recurring tasks. The normalization layer reshapes
data from each channel's format into one standard schema holding the lead's identity,
target brand, source channel, and source article where relevant. The storage layer appends
a row to the master lead spreadsheet that serves as the single source of truth across brands.
The notification layer sends a lead summary to the relevant brand's sales messaging group
in a uniform message format. The layered pattern means adding a new channel or brand
only takes copying a workflow and changing its trigger parameters, with no architectural
rework. Figure 2 visualizes the system.

Rafi Farizki

Available online a https://jist.publikasiindonesia.id/index.php/jist/index 441

Figure 2. N8n Based System Architecture
Source: compiled by the researcher (2026)

Several design decisions were made deliberately from the start. First, n8n was self
hosted on a company server instead of a per execution cloud plan, because high daily
execution volume makes per task pricing balloon quickly, and prospective customer
contact data was judged too sensitive to route through a third party. Second, every
workflow was designed to be idempotent, meaning a repeated execution of the same event
produces no duplicate row or notification, through a unique key check before any write.
Third, credentials for all services live in n8n's built in credential manager rather than
inside nodes, so password rotation never requires editing a workflow. Fourth, the master
spreadsheet was declared the single source of truth; other applications may read from it,
but only workflows may write to it, a rule that blocks the return of the very manual entry
the system was built to remove.

Implementing the Automation Workflows
Four workflows went live as designed. The first, lead consolidation, receives
webhook submissions from all landing page forms and pulls social media lead form data
on a schedule, normalizes them, and appends them to the master spreadsheet tagged with
brand and channel. Duplication is blocked by a contact number check before any new
row is written. The second, lead distribution, fires the moment a new row lands: the
system reads the target brand, composes a lead summary, and sends it to that brand's sales

Rafi Farizki

Available online a https://jist.publikasiindonesia.id/index.php/jist/index 442

messaging group, complete with the source article when the lead came from the blog, so
the sales team knows the prospect's context from the first message.
The third workflow, weekly reporting, runs on a schedule at the start of each week.
The system reads the master spreadsheet, computes lead recaps per brand and per channel
for the past week, compares them with the week before, and sends the summary to the
management group with no staff involvement. The fourth, content monitoring,
periodically checks new blog articles on each brand site, flags any article not yet wired
into lead source tracking, and reports it to the content manager. Every workflow writes
execution logs in n8n, and a failed execution fires its own alert to the automation manager,
so disruptions get handled the same day.
Implementation was not entirely smooth, and three technical lessons are worth
recording. First, the variety of data formats across channels made the normalization layer
the most revised part of the system; without a standard schema from day one, the master
spreadsheet dirties fast. Second, third party API quotas forced deliberate pacing and
scheduling so data pulls would not be rejected. Third, the reliability of the automation
rests on the reliability of the server n8n runs on, which makes server availabil ity
monitoring an operational precondition rather than an afterthought.
So that the automation would not depend on one person's memory, operational
governance was set up alongside implementation. Every workflow carries a uniform
name encoding brand, function, and version, which keeps dozens of workflows traceable
across brands. Changes to a live workflow are made by duplicating and testing a copy
first, never by editing production directly, and each workflow has a short note on its
trigger, its output, and who is affected if it stops. The automation manager role is explicit:
sole owner of the whole system, responsible for checking daily failure logs, reviewing
API quotas, and acting as first contact when field teams spot odd data. Such governance
sounds administrative, but it is what separates automation that lasts from experiments that
quietly die once their builder gets busy.

Evaluating Operational Efficiency
The evaluation covers three dimensions. The first is cycle time. Before
automation, the gap between a lead arriving and the sales team being notified depended
on when staff happened to check a channel, so it could stretch to hours, and leads outside
working hours waited until the next day [insert: average response time before automation
based on internal records]. After automation, notifications go out within seconds of arrival
on every connected channel, in line with M. I. Pratama and Voutama's (2026) finding that
n8n moves data between platforms in under two seconds. The second is data quality.
Duplicate entries and stray leads, once routine, practically disappeared because every
channel now drains into one master spreadsheet with duplicate checking, and every lead
carries the channel and source article tags that used to be forgotten. The third is reporting
consistency. The weekly report that once consumed up to half a working day and kept

Rafi Farizki

Available online a https://jist.publikasiindonesia.id/index.php/jist/index 443

changing shape now publishes automatically on the same schedule in a uniform structure,
which moved management discussion from verifying the numbers to acting on them.
Interviews with internal users reinforce the three changes. Marketing staff say the time
once lost to copying data has shifted to content production and channel experiments,
while the sales team values the source article context on notifications for openin g
conversations with prospects. This matches the classic automation argument that the
greatest value of machines is not replacing people but freeing them from repetition (van
der Aalst et al., 2018), and Wali et al.'s (2025) finding that n8n modules cut response
times and entry errors in a microfinance service organization.
Beyond the three main dimensions, the evaluation recorded two further
consequences. On scalability and cost, adding a new brand or channel now carries a
marginal cost close to zero, a workflow copy and a parameter change, whereas under
manual operations every new brand meant extra recap work that eventually demanded
extra people; self hosting also keeps platform cost from growing with execution volume.
On risk, automation creates a new fragility, dependence on server availability and on a
single automation manager; when the server goes down, the whole lead pipeline stops,
something that never happened when everything was manual because staff could always
copy by hand. The mitigations are automatic failure alerts, periodic workflow
configuration backups, and documentation that lets other staff take over; the efficiency
gained, in other words, is paid for with a new kind of operational discipline.

Discussion
Compared with the existing literature, this study contributes in three ways. First,
context. Earlier n8n studies each work on a single service, stock analysis (Ahmad et al.,
2026), a laundry business (Al Fajar et al., 2026), workshop registration (Sholihah et al.,
2026), digital receipt logging (W. Pratama & Ahda, 2025), or a cooperative (Wali et al.,
2025); this study shows the same four layer pattern scaling automation across more than
a dozen brands and many channels at once, the ordinary condition of a multi brand service
company. Second, the position of automation within the marketing function. The
marketing automation literature mostly discusses commercial tools for lead nurturing
(Heimbach et al., 2015; Järvinen & Taiminen, 2016); this study shows that the operational
layer beneath it, consolidation, distribution, and reporting, can be built in house on an
open source low code platform at marginal cost, which lowers the price barrier that has
kept mid sized companies away from marketing automation (Sahay et al., 2020) . Third,
the sociotechnical side. The automation does not run itself; its reliability depends on data
schema discipline, server monitoring, and one automation manager who understands both
the business process and the platform. Low code technology lowers the technical barrier,
but it relocates the critical point to process and data governance, a finding that matters to
any organization planning to copy this approach.
Theoretically, the findings enrich two conversations at once. For the marketing
automation literature, this case shows the effectual adoption path described by Mero et
al. (2020)  in its most concrete form: an organization builds automation capability step by

Rafi Farizki

Available online a https://jist.publikasiindonesia.id/index.php/jist/index 444

step from means it already owns, a spreadsheet, messaging channels, an internal server,
instead of waiting for the budget for commercial software. For the process automation
literature, n8n occupies an interesting position between robotic process automation that
mimics human clicks on interfaces and API based application integration; because it
works directly at the API layer, an n8n workflow is not brittle to interface changes, the
classic weakness of RPA (Syed et al., 2020) . Practically, the findings offer a replicable
path for other service companies in three steps: map the repetitive high volume
workflows, fix the data schema and the single source of truth before building the first
workflow, then grow the automation layer by layer along the trigger, normalization,
storage, and notification pattern.

CONCLUSION
This study shows that n8n based digital marketing workflow automation can raise
the operational efficiency of a multi brand service company on three dimensions at once:
lead handling cycle time falls from hours to seconds, data quality improves as duplicate
entries and stray leads are eliminated by a single source of truth, and weekly reporting
becomes consistent without manual work. The four automated workflows, multi channel
lead consolidation, lead distribution, performance reporting, and content monitor ing,
were all built on one four layer architecture of trigger, normalization, storage, and
notification, which proved easy to replicate across brands and channels. The findings
confirm that an open source low code platform lowers the cost barrier of market ing
automation for mid sized companies, with the caveat that its success rests on data schema
discipline, infrastructure monitoring, and the presence of an automation manager who
understands the business process.
For practitioners, the results suggest starting automation from workflows that are
repetitive, clearly rule bound, and high in volume, and fixing a standard data schema
before the first workflow is built. For future research, three directions stand open:
quantitative measurement of automation's effect on lead to customer conversion,
comparison across workflow automation platforms on the same workload, and study of
artificial intelligence agents on n8n for automatic lead qualification, a path recent studies
have begun to explore.

FUNDING
The author(s) declared that financial support was not received for this work and/or
its publication.

CONFLICT OF INTEREST
The author(s) declared that this work was conducted in the absence of any
commercial or financial relationships that could be construed as a potential conflict of
interest.

Rafi Farizki

Available online a https://jist.publikasiindonesia.id/index.php/jist/index 445

AUTHOR CONTRIBUTIONS
If applicable, the Author's Contribution Statement.

GENERATIVE AI STATEMENT
The author(s) declared that generative AI was used in the creation of this
manuscript. The author(s) wish to acknowledge the use of Generative AI for refining the
language clarity and grammatical structure of this manuscript. This application was
conducted in adherence to established ethical guidelines regarding the use and disclosure
of generative AI in scholarly research. Each author has provided substantial intellectual
contributions to the work, which has been rigorously vetted for accuracy, and the
author(s) assume full responsibility for the integrity and final contentofthemanuscript.
Any alternative text (alt text) provided alongside figures in this article has been
generated by Frontiers with the support of artificial intelligence and reasonable eﬀorts
have been made to ensureaccuracy, including review by thea uthors wherever possible. If
you identify any issues, please contact us.

Rafi Farizki

Available online a https://jist.publikasiindonesia.id/index.php/jist/index 446

REFERENCES
Aguirre, S., & Rodriguez, A. (2017). Automation of a business process using robotic
process automation (RPA): A case study. In Communications in Computer and
Information Science (Vol. 742, pp. 65–71). https://doi.org/10.1007/978-3-319-
66963-2_7
Ahmad, I. A. G., Hendriadi, A. A., & Ma’sum, A. (2026). Implementasi AI agent untuk
otomatisasi analisis saham berbasis web menggunakan workflow n8n. Jurnal
TIMES, 15(1). https://doi.org/10.51351/jtm.15.1.2026920
Al Fajar, M., Gunawan, & Wiradarma, A. (2026). Implementasi layanan otomasi usaha
laundri berbasis workflow automation menggunakan n8n. AnoaTIK: Jurnal
Teknologi Informasi Dan Komputer , 4(1), 29 –37.
https://doi.org/10.33772/anoatik.v4i1.136
Bock, A. C., & Frank, U. (2021). Low-code platform. Business & Information Systems
Engineering, 63(6), 733–740. https://doi.org/10.1007/s12599-021-00726-8
Chaffey, D., & Ellis-Chadwick, F. (2019). Digital marketing (7th ed.). Pearson.
Heimbach, I., Kostyra, D. S., & Hinz, O. (2015). Marketing automation. Business &
Information Systems Engineering, 57(2), 129–133. https://doi.org/10.1007/s12599-
015-0370-8
Hofmann, P., Samp, C., & Urbach, N. (2020). Robotic process automation. Electronic
Markets, 30(1), 99–106. https://doi.org/10.1007/s12525-019-00365-8
Järvinen, J., & Taiminen, H. (2016). Harnessing marketing automation for B2B content
marketing. Industrial Marketing Management , 54, 164 –175.
https://doi.org/10.1016/j.indmarman.2015.07.002
Kannan, P. K., & Li, H. (2017). Digital marketing: A framework, review and research
agenda. International Journal of Research in Marketing , 34(1), 22–45.
https://doi.org/10.1016/j.ijresmar.2016.11.006
Lacity, M. C., & Willcocks, L. P. (2016). A new approach to automating services. MIT
Sloan Management Review, 58(1), 41–49.
Mero, J., Tarkiainen, A., & Tobon, J. (2020). Effectual and causal reasoning in the
adoption of marketing automation. Industrial Marketing Management, 86, 212–222.
https://doi.org/10.1016/j.indmarman.2019.12.008
Miles, M. B., Huberman, A. M., & Saldaña, J. (2014). Qualitative data analysis: A
methods sourcebook (3rd ed.). SAGE Publications.
Pratama, M. I., & Voutama, A. (2026). Analisis performa efisiensi waktu pada workflow
otomasi menggunakan platform n8n. JATI (Jurnal Mahasiswa Teknik Informatika),
10(3), 4955–4960. https://doi.org/10.36040/jati.v10i3.18306
Pratama, W., & Ahda, F. A. (2025). Inovasi agen AI dalam sistem pencatatan struk digital
otomatis berbasis n8n. Jurnal FASILKOM , 15(3).
https://doi.org/10.37859/jf.v15i3.10366
Sahay, A., Indamutsa, A., Di Ruscio, D., & Pierantonio, A. (2020). Supporting the
understanding and comparison of low-code development platforms. Proceedings of

Rafi Farizki

Available online a https://jist.publikasiindonesia.id/index.php/jist/index 447

the 46th Euromicro Conference on Software  Engineering and Advanced
Applications (SEAA), 171–178. https://doi.org/10.1109/SEAA51224.2020.00036
Sholihah, F., Prashanda, P. D., & Purna, S. (2026). Rancang bangun sistem pendaftaran
workshop terintegrasi AI chatbot dan notifikasi multi-channel berbasis n8n. Jurnal
Kolaboratif Sains, 9(7), 1850–1861. https://doi.org/10.56338/jks.v9i7.11546
Syed, R., Suriadi, S., Adams, M., Bandara, W., Leemans, S. J. J., Ouyang, C., ter
Hofstede, A. H. M., van de Weerd, I., Wynn, M. T., & Reijers, H. A. (2020). Robotic
process automation: Contemporary themes and challenges. Computers in Industry,
115, 103162. https://doi.org/10.1016/j.compind.2019.103162
van der Aalst, W. M. P., Bichler, M., & Heinzl, A. (2018). Robotic process automation.
Business & Information Systems Engineering , 60(4), 269–272.
https://doi.org/10.1007/s12599-018-0542-4
Wali, M., Nasir, N., & Iqbal, T. (2025). Implementing workflow automation with N8N
to enhance operational efficiency and performance in the Sharia Cooperative of
Bank Indonesia, Aceh Province. Journal Digital Technology Trend, 4(1), 36–47.
https://doi.org/10.56347/jdtt.v4i1.341
Yin, R. K. (2018). Case study research and applications: Design and methods (6th ed.).
SAGE Publications.
