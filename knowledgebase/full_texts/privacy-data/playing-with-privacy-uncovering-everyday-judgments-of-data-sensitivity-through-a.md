---
title: 'Playing with Privacy: Uncovering Everyday Judgments of Data Sensitivity Through an Arcade Machine
  Interface'
url: https://doi.org/10.1145/3742413.3789162
category: privacy-data
subcategory: framework
date: 2026-03
venue: ''
authors:
- Maksim Kalameyets
- Rebecca Owens
- Chi Hang Lam
source: openalex-oa
pdf_url: https://pure-oai.bham.ac.uk/ws/files/306816457/KalameyetsM2026Playing.pdf
pages: 16
chars: 81972
fetched_at: '2026-11-08T17:39:08+00:00'
kb_version: 1
---

# Playing with Privacy: Uncovering Everyday Judgments of Data Sensitivity Through an Arcade Machine Interface

University of Birmingham
Playing with Privacy
Kalameyets, Maksim; Owens, Rebecca; Lam, Chi Fai David; Olabode, Shola; Vlachokyriakos,
Vasilis; Farrand, Ben; Aidinlis, Stergios; Shi, Lei
DOI:
10.1145/3742413.3789162
License:
Creative Commons: Attribution (CC BY)
Document Version
Publisher's PDF, also known as Version of record
Citation for published version (Harvard):
Kalameyets, M, Owens, R, Lam, CFD, Olabode, S, Vlachokyriakos, V, Farrand, B, Aidinlis, S & Shi, L 2026,
Playing with Privacy: Uncovering Everyday Judgments of Data Sensitivity Through an Arcade Machine Interface.
in T Kuflik, S Kleanthous, L Chen, G Jaccuci & A Renner (eds), IUI '26: Proceedings of the 31st International
Conference on Intelligent User Interfaces. Association for Computing Machinery (ACM), pp. 1283-1297, The
31st Annual ACM Conference on Intelligent User Interfaces
, Paphos, Cyprus, 23/03/26. https://doi.org/10.1145/3742413.3789162
Link to publication on Research at Birmingham portal
General rights
Unless a licence is specified above, all rights (including copyright and moral rights) in this document are retained by the authors and/or the
copyright holders. The express permission of the copyright holder must be obtained for any use of this material other than for purposes
permitted by law.
•Users may freely distribute the URL that is used to identify this publication.
•Users may download and/or print one copy of the publication from the University of Birmingham research portal for the purpose of private
study or non-commercial research.
•User may use extracts from the document in line with the concept of ‘fair dealing’ under the Copyright, Designs and Patents Act 1988 (?)
•Users may not further distribute the material nor use it for the purposes of commercial gain.
Where a licence is displayed above, please note the terms and conditions of the licence govern your use of this document.
When citing, please reference the published version.
Take down policy
While the University of Birmingham exercises care and attention in making items available there are rare occasions when an item has been
uploaded in error or has been deemed to be commercially or otherwise sensitive.
If you believe that this is the case for this document, please contact UBIRA@lists.bham.ac.uk providing details and we will remove access to
the work immediately and investigate.
Download date: 08. Nov. 2026

Playing with Privacy: Uncovering Everyday Judgments of Data
Sensitivity Through an Arcade Machine Interface
Maksim Kalameyets
School of computing
Newcastle University
Newcastle upon Tyne, United
Kingdom
maksim.kalameyets@newcastle.ac.uk
Rebecca Owens
Law School
Durham University
Durham, United Kingdom
rebecca.owens@durham.ac.uk
Chi Fai David Lam
University of Birmingham
Birmingham, United Kingdom
c.f.d.lam@bham.ac.uk
Shola Olabode
Newcastle University
Newcastle Upon Tyne, United
Kingdom
shola.olabode@newcastle.ac.uk
Vasilis Vlachokyriakos
Open Lab
Newcastle University
Newcastle upon Tyne, United
Kingdom
vasilis.vlachokyriakos1@newcastle.ac.uk
Ben Farrand
Newcastle University
Newcastle upon Tyne, United
Kingdom
ben.farrand@newcastle.ac.uk
Stergios Aidinlis
Durham University
Durham, United Kingdom
stergios.aidinlis@durham.ac.uk
Lei Shi
School of Computing
Newcastle University
Newcastle upon Tyne, United
Kingdom
lei.shi@newcastle.ac.uk
Abstract
Current data protection legal frameworks, including the GDPR, clas-
sify “special” categories of personal data that are deemed deserving
of higher protection due to their impact on fundamental rights. Yet,
these legal abstractions fail to capture how individuals themselves
judge sensitivity in everyday digital contexts. This disconnect may
undermine intelligibility and erode trust in data protection as a
legal institution. Despite its centrality to privacy protection, limited
empirical work has systematically compared public sensitivity judg-
ments against the special categories of protected data under Article
9 GDPR. We address this gap through a mixed-methods design that
integrates nine semi-structured interviews with a game-like sur-
vey deployed on public arcade machines. This approach generated
2,935 responses from 224 participants enabling in-situ analysis of
everyday judgments. By operationalising an ontology capturing
who collects data, what data are collected, and for what purpose,
we systematically compared responses across demographic groups.
Contrary to literature assumptions that health and financial data are
primary markers of data sensitivity, our findings demonstrate that
expressive content, messages, photos, and social ties elicited the
strongest resistance to sharing by citizens. Acceptance was shaped
decisively by purpose. Citizens tolerated safety and functionality,
whilst advertising and vague claims of “research” were rejected.
Attitudes varied systematically, with women disproportionately
This work is licensed under a Creative Commons Attribution 4.0 International License.
IUI ’26, Paphos, Cyprus
© 2026 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-1984-4/26/03
https://doi.org/10.1145/3742413.3789162
resistant to sharing expressive content, and higher education and
digital literacy predicting greater caution. This study demonstrates
that data sensitivity cannot be reduced to fixed legal categories.
Rather, it is socially situated and purpose-dependent. Our find-
ings provide empirical foundations for reimagining consent flows,
privacy defaults, and transparency mechanisms that align with
everyday logics. This can enable the development of systems that
people can genuinely understand, trust, and consent to.
CCS Concepts
• Human-centered computing→ Empirical studies in HCI ; •
Security and privacy→ Social aspects of security and privacy;
• Applied computing→ Law, social and behavioral sciences ; •
Information systems→ Information systems applications.
Keywords
Privacy sensitivity, GDPR, mixed methods, arcade installations,
demographic differences
ACM Reference Format:
Maksim Kalameyets, Rebecca Owens, Chi Fai David Lam, Shola Olabode,
Vasilis Vlachokyriakos, Ben Farrand, Stergios Aidinlis, and Lei Shi. 2026.
Playing with Privacy: Uncovering Everyday Judgments of Data Sensitivity
Through an Arcade Machine Interface. In 31st International Conference on
Intelligent User Interfaces (IUI ’26), March 23–26, 2026, Paphos, Cyprus. ACM,
New York, NY, USA, 15 pages. https://doi.org/10.1145/3742413.3789162
1 Introduction
There is a growing mismatch between how the law defines sensitive
data and how citizens actually experience privacy and want their
1283

IUI ’26, March 23–26, 2026, Paphos, Cyprus Kalameyets et al.
data to be protected. Article 9 of the General Data Protection Regu-
lation (GDPR),1 an EU data protection law governing the collection
and processing of personal data, identifies special categories of
information, such as health, religion, and trade union membership,
that require heightened safeguards because of their potential im-
pact on fundamental rights. This legal definition of data sensitivity
is grounded in preventing structural risks of discrimination and
substantive harm [11, 29].
However, this risk-based legal logic, operates at a high level of
abstraction that differs from how individuals assess sensitivity in
everyday digital interactions. Individuals often perceive other forms
of data as equally, or even more, sensitive. These include personal
messages, financial information, and social media content. The
law’s categories thus only partly capture the lived sense of what it
means for data to feel private. Empirical research demonstrates that
sensitivity is not a fixed or universal attribute. Instead, it emerges
through age, gender, cultural context, and lived experience [ 30].
Younger people, for instance, may have fewer privacy concerns
than older adults [27]. Still, they often emphasise worries about
surveillance and tracking, whereas older adults are more attuned
to the financial harms of data collection [24]. Women frequently
highlight concerns about safety and harassment [ 7]. In the UK,
research has shown citizens often think of privacy on a local level,
focusing on immediate and tangible risks rather than global issues
of privacy [10]. These patterns reveal that what counts as “sensitive”
is dynamic, contingent, and deeply entangled with social life.
Despite this, influential legal frameworks, such as the GDPR,
continue to treat sensitivity as a stable legal category tied to a
closed list of issues affecting citizens’ fundamental rights. This mis-
alignment in understanding of sensitivity raises questions about
whether static legal categories can remain credible in a world where
the meaning of privacy is fluid, and citizens routinely make privacy
decisions through brief interactions with cookie banners and pri-
vacy policies. Building on calls across law and HCI to integrate lived
experiences into governance and system design, we examine how
people evaluate data sensitivity in everyday digital context [5, 15].
Our study advances understanding of how sensitivity is reasoned
about and experienced, and how these perceptions might inform
both regulatory frameworks and the design of systems that handle
personal data. Specifically, we ask:
• RQ1: How do individuals assess the sensitivity of different
types of personal data that companies collect about them?
• RQ2: How do perceptions of sensitivity vary across demo-
graphic groups, and how do these variations challenge or
extend the GDPR’s notion of “special categories”?
• RQ3: What implications do gaps between public expecta-
tions and regulatory frameworks have for the design of par-
ticipatory and context-sensitive privacy tools?
In this paper, we focus on empirical perceptions of sensitivity,
that is, how individuals feel about different forms of data collection
in everyday contexts. This stands in contrast to legal sensitivity,
which is a fixed construct tied to the risks of discrimination, exclu-
sion, or interference with fundamental rights, as codified in Article
1Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April
2016 on the protection of natural persons with regard to the processing of personal
data and on the free movement of such data (GDPR) [2016] OJ L119/1.
9 of the GDPR. Our contribution is not to propose a redefinition
of these legal categories, but rather to highlight how contextual
sensitivity, lived discomfort, and socially situated judgments can re-
veal blind spots where regulatory practice and public expectations
diverge. Such findings are increasingly important in light of the
EU’s recent Omnibus IV proposals to streamline data protection
laws [8].
To address these questions, we studied individuals’ opinions
using surveys (as a qualitative data source) and an interactive,
game-based tool housed in a physical arcade-style machine (as
a quantitative data source). Both surveys and arcade machines
present real-world data-collection scenarios and ask participants
to indicate how comfortable they feel. It then tells users whether
the data involved falls under the GDPR’s special categories. The
aim is twofold: to gather public judgments and to prompt regu-
latory reflection. This paper presents empirical evidence on how
people perceive data sensitivity beyond GDPR categories, a novel
participatory method for eliciting these judgments, and design im-
plications for context-sensitive privacy tools that better align with
lived practice.
This paper makes three contributions: (1) empirical evidence of
the alignment or divergence between everyday sensitivity judg-
ments and the classification of special and non-special categories
of personal data under Article 9 GDPR; (2) a novel participatory
method for eliciting judgments through interactive arcade ma-
chines; and (3) design implications for context-sensitive privacy
tools that better align with lived practice. Contrary to common
assumptions in the literature that health and financial data are
the chief indicators of sensitivity, our results show that expressive
material—messages, images, and social networks—provoked the
greatest reluctance to share among citizens. Purpose was the deci-
sive determinant of acceptability. While safety and functionality
were tolerated, advertising and ambiguous references to “research”
were rejected. Views varied systematically: women were dispro-
portionately unwilling to share expressive content, and individuals
with higher education and digital literacy were more cautious. This
study shows that data sensitivity cannot be confined to static legal
classifications; rather, it is socially situated and purpose-dependent.
The remainder of this paper is structured as follows. Back-
ground reviews prior work on context-sensitive privacy, legal
sensitivity categories, and participatory methods, motivating the
need to bridge legal definitions and lived experience. Methodol-
ogy describes our mixed-methods design: the “who-what-why”
ontology, interview protocol and analysis, the design and public
deployment of arcade machines, data handling, and our statistical
strategy for comparing demographic groups.Results reports partic-
ipant demographics and presents findings in two parts: qualitative
themes with illustrative quotes, and quantitative evidence from the
arcade data, including group comparisons and𝑝-values for trans-
parency. Discussion interprets these findings for HCI and policy,
outlines design implications, and notes limitations. Conclusion
summarises the paper’s contributions.
2 Background
Privacy is neither a static nor a universally defined concept. Instead,
it is contextually situated and shaped by social, demographic, and
1284

Playing with Privacy: Uncovering Everyday Judgments of Data Sensitivity Through an Arcade Machine Interface IUI ’26, March 23–26, 2026, Paphos, Cyprus
technological conditions [20]. Substantial scholarship has demon-
strated that individual privacy preferences are informed more by
subjective beliefs and contextual cues than by consistent normative
principles [2], [12], [20]. These preferences are also mediated by
identity, experience, and perceived risks, necessitating regulatory
frameworks that move beyond universalist models [30].
Early HCI and policy work documents that people differenti-
ate sharply between types of personal information and recipients
when deciding what to share. Olson et al. examined preferences
for sharing and privacy and showed that willingness to disclose
is strongly contingent on the information type and the social con-
text of disclosure [ 22]. Large-scale European evidence similarly
indicates heterogeneity in identity-data practices and regulatory
preferences across populations, highlighting that disclosure deci-
sions depend not only on perceived risk but also on institutional
trust and perceived benefits [17].
Privacy sensitivities differ markedly across demographic and
occupational groups. For example, journalists and activists prioritise
protection from surveillance and metadata tracking due to risks of
state targeting or professional exposure [13]. In contrast, corporate
employees may focus on employer oversight of communication
channels such as email and web browsing. Education level also
influences privacy awareness: individuals with higher education
are typically more aware of algorithmic profiling. At the same
time, those with limited digital literacy may emphasise concrete
harms such as identity theft and remain unaware of data brokerage
ecosystems [19].
Health status adds further nuance. Patients with chronic con-
ditions or disabilities often express heightened concern about the
handling of their medical and genetic data, fearing misuse by em-
ployers or insurers. Conversely, healthier individuals may be more
willing to share biometric or fitness data in exchange for person-
alised services [23]. Cultural and political contexts also influence at-
titudes: individuals in surveillance-oriented regimes may emphasise
anonymity and encryption, whereas those in liberal democracies
focus on corporate data collection and monetisation [17].
Gender and geography intersect with these trends. Women re-
port greater concern over online harassment, image-based abuse,
and doxxing, while men are more likely to emphasise financial or
reputational privacy risks[17]. Additionally, urban residents are
often more sensitive to surveillance infrastructures, such as CCTV
or smart city data systems. In contrast, rural populations express
concern about localised data flows, including land registries or
informal sharing within tight-knit communities [31].
Conventional regulatory models frequently rely on broad, pre-
defined categories of sensitive data. GDPR, for example, introduces
a risk-based framework under which health, religious, and political
data are granted “special category” protections [ 14], [9]. While
this approach provides necessary safeguards, it may diverge from
public perceptions of what constitutes sensitive or high-risk data
[28]. Recent work challenges the assumption that legally codified
sensitivity classifications align with user expectations, revealing a
potential disconnect between law and lived experience [26].
Other legal systems adopt alternative strategies. The United
States favours a sector-specific model: the Health Insurance Porta-
bility and Accountability Act governs health data. At the same time,
the Family Educational Rights and Privacy Act applies to educa-
tional records. These rules apply narrowly, reflecting institutional
domains rather than providing overarching data protection rights.
By contrast, countries such as Japan have developed hybrid systems
that blend GDPR-inspired protections with culturally and legally
localised mechanisms [18].Such jurisdictional divergences may sup-
port the case for adaptive privacy frameworks that accommodate
localised values and contextual norms, consistent with the theory
of contextual integrity [20]. According to this framework, privacy
depends on whether data is collected and shared in ways that fit
the setting. These expectations vary based on factors like who is
collecting the data, what information is gathered, why it is collected,
and how it is used, and can differ significantly across contexts such
as education, workplaces, social media, and the home.
There is an increasing recognition that public engagement is
essential for aligning data governance with the lived experiences
of privacy [22]. While surveys, interviews, and focus groups pro-
vide detailed insight into user attitudes, they often fail to capture
a representative cross-section of the population due to resource
constraints and access disparities.
Participatory design methodologies, such as co-design work-
shops and structured crowdsourcing, offer scalable alternatives.
However, these too risk excluding marginalised groups unless com-
bined with inclusive recruitment tactics, mobile accessibility, and
language localisation [19].
Speculative and scenario-based design techniques further enrich
engagement by encouraging participants to imagine and critique
future data governance regimes. Gamified methods, including in-
teractive challenges and role-playing games, can increase retention
and comprehension by embedding abstract regulatory trade-offs in
concrete, experiential formats [21, 25].
Beyond online platforms, physical installations have emerged as
a complementary tool for eliciting perspectives on privacy. Arcade-
style machines and interactive kiosks can be deployed in public
spaces to engage passersby in playful yet informative tasks, offering
a means of collecting data at scale while minimising participant
fatigue [3]. These systems offer three core advantages:
(1) Demographic Reach: Installations placed in community
centres, libraries, or universities can engage populations not
typically reached through digital methods, thereby capturing
sensitivity judgments that static legal frameworks such as
GDPR may overlook.
(2) Real-Time Education: Gamified feedback loops allow users
to learn about privacy risks and protections dynamically
through simulated scenarios.
(3) Efficient Data Collection: Tasks embedded within game
mechanics promote rapid, high-volume input without the
need for intensive researcher supervision.
Prior work shows that disclosure decisions vary by information
type, recipient, and context, and that privacy attitudes are not
captured by a single “concern” factor but are multidimensional
[13, 17, 22]. More recent research develops domain-specific accounts
of sensitivity and norms, including taxonomies for photo content
[16], decision-making around sensitive social media disclosures [4],
and privacy norms for smart-home assistants [1]. We build on these
insights but contribute a different comparison point: we explicitly
1285

IUI ’26, March 23–26, 2026, Paphos, Cyprus Kalameyets et al.
benchmark everyday sensitivity judgments against GDPR Article 9
special-category status using a structured who–what–why design.
We elicit these judgments in-the-wild via public arcade deployments
and explain the resulting patterns through follow-up qualitative
interviews.
Building on these insights, this study introduces a mixed-methods
approach that combines arcade-style participatory installations
with qualitative interviews. Our objective is to engage demographi-
cally diverse participants in reflecting on their privacy preferences
and the regulatory trade-offs associated with them. This approach
is designed to uncover latent privacy norms and support the de-
velopment of digital products and data models that are flexible,
inclusive, and grounded in everyday experiences.
3 Methodology
As mentioned previously, we study public privacy concerns using a
mixed-methods design that combines public arcade machines with
semi-structured interviews. The goal is to hear people’s reasons in
their own words and measure how common these views are across
different demographic groups.
First, we develop a privacy ontology that represents any data-
collection practice along three analytically distinct dimensions: the
data collector (who), the type of data collected (what), and the pur-
pose of collection (why). These dimensions are deliberately aligned
with GDPR constructs: the who corresponds to the controller (Arti-
cle 4(7)), the what to personal data under Article 4(1) and Article 9,
and the why to the lawful bases for processing in Article 6.
A central aim of this work is to compare everyday sensitivity
judgments to a concrete legal baseline. We therefore operationalise
legal sensitivity as membership in the GDPR’s “special categories
of personal data” (Article 9). During ontology construction, we an-
notated each data-type category with a binary indicator that marks
whether the attribute is an Article 9 special category (e.g., health-
related data and other Article 9 attributes when explicitly present)
versus ordinary personal data (Article 4(1)). Crucially, several data
types are treated as ordinary personal data under the GDPR and are
not classified as special categories under Article 9. These include
data that participants consistently regard as highly sensitive, most
notably financial information and expressive or social content. This
mapping allows us to report not only which data types participants
reject, but also whether these rejections fall inside or outside the
GDPR’s special-category boundary.
Second, we conducted semi-structured interviews focused on
the arcade machine game, asking participants to describe their feel-
ings and explain why. These conversations help us to contextualise
participants’ perceptions of privacy. Third, we deploy arcade-style
game machines in public places. The game shows the same kind of
“who-what-why” statements. For each one, the player chooses “I
hate that” or “I don’t care”, and then answers a short set of demo-
graphic questions. This approach enables us to receive numerous
quick responses from a diverse demographic of people.
This “who–what–why” structure also closely matches the core
idea of Contextual Integrity (CI): whether a data flow fits a situation
depends on who is involved, what data is shared, and under what
conditions [20]. Our ontology is a simplified CI-style template that
is suitable for short, readable arcade prompts. It captures (i) the
collector (who), (ii) the data type (what), and (iii) the purpose (why).
We do not model all CI parameters (e.g., the exact recipient or the
relationship between sender and recipient), because the interface
must stay brief for public use.
Our mixed-methods approach enables us to use interviews to
generate rich explanations and hypotheses, while quantitative data
from arcade machines demonstrates the strength of these effects
and identifies the populations for whom they are most pronounced.
3.1 Development of privacy ontology
We adopted a purposive sampling methodology to select privacy
policies, which we analysed to develop our ontology. Our selection
criteria revolved around three key aspects. The first was popular-
ity, determined by their ranking within the top 0.1% of the Tranco
popularity list2, a widely recognised benchmark for website traffic
and engagement. Secondly, we emphasised heterogeneity by choos-
ing policies from various industries, ensuring the legal ontology
accurately reflects the diverse data management practices across
different digital service domains. Lastly, we required the policies
to be publicly available online and in English for accessibility. We
reviewed 11 privacy policies from sectors including social media,
smart home IoT devices, and femtech applications. We accessed
these policies in September 2023, either as standalone documents
or as provisions within End-User License Agreements.
The team performed a manual qualitative content analysis of
the privacy policies to delineate the various categories inherent to
the privacy policy under investigation. To ensure the reliability of
our qualitative coding, at least two members of the research team
independently reviewed each policy and applied the pre-established
coding categories. Following initial coding, we held collaborative
sessions with team members from different disciplines to compare
interpretations. Where disagreements arose, these were discussed
until the team reached consensus. To further improve our reliability,
we implemented a deductive approach that entailed coding for pre-
established categories, including (a) data types (Figure 1), such as
special categories of data, (b) purposes of data collection (Figure 2), (c)
third-party sharing. These categories were chosen to be consistent
with the information that should be provided to users under GDPR.
Our goal was to shed light on the interrelationships between dif-
ferent entities of these categories, specifically exploring the purpose
of processing personal information, such as names and the ratio-
nale for sharing this information with third parties like Google or
Facebook. In doing so, we aimed to understand the routes through
which companies process and share user data.
3.2 Interviews
To examine participants’ perspectives on online behaviour, privacy,
and data regulation, we conducted semi-structured interviews in-
corporating both open-ended questions and a gamified exercise.
Our approach was designed to ensure consistency across partici-
pants while allowing space for individual elaboration. Below, we
describe our recruitment strategy and the procedures used in data
collection and analysis.
2https://tranco-list.eu/
1286

Playing with Privacy: Uncovering Everyday Judgments of Data Sensitivity Through an Arcade Machine Interface IUI ’26, March 23–26, 2026, Paphos, Cyprus
Figure 1: Ontology of data types that may be collected.
Figure 2: Ontology of collection purposes.
1287

IUI ’26, March 23–26, 2026, Paphos, Cyprus Kalameyets et al.
Participant Recruitment: Participants were recruited through
opportunity sampling at the physical locations of 2 arcade ma-
chine sites. On two separate visits, researchers approached citizens
present at the sites who had interacted with the machine and invited
them to participate in the study. Of 13 individuals approached, 9
consented and were interviewed; 4 declined. A £30 voucher was pro-
vided as an incentive. The study received full ethical approval from
University Ethical Board, and all participants provided informed
consent. This purposive, venue-based recruitment was to facilitate
relevance to the qualitative data collected. While this approach
allowed for efficient recruitment, it also has limitations in terms of
representativeness, as the sample was shaped by the availability of
those frequenting the selected sites.
Procedure and Analysis: The interviews were conducted using a
semi-structured guide that combined open-ended questions with a
gamified exercise designed to elicit participants’ perspectives. The
guide addressed four principal domains: (i) online behavior and
engagement, including frequency of internet use, types of online
activities, and adoption of smart home devices; (ii) awareness and
perceptions of data collection, probing participants’ knowledge,
assumptions, and affective responses regarding data usage; (iii)
privacy management and control, with particular attention to prac-
tices such as adjusting settings, responding to cookie banners, and
levels of institutional trust; and (iv) knowledge of GDPR. A central
feature of the interview was a short arcade game involving twenty
hypothetical “who-what-why” prompts. For each scenario, partici-
pants indicated whether they were indifferent to or disapproved of
the practice, and provided explanations for their judgments. Each
interview lasted approximately 25 minutes and was audio-recorded,
transcribed verbatim, and anonymised.
To analyse the data, we employed a qualitative research design
grounded in reflexive thematic analysis (RTA) [6]. RTA is a theo-
retically flexible analytic method suited to interrogating human
meaning-making and socially situated reasoning. It is particularly
well-suited to HCI research that involves interpretive engagement
with complex sociotechnical issues, as it positions the researcher’s
subjectivity as a valuable analytic resource. Our aim was not to
quantify opinion frequency, as was possible through arcade ma-
chine interactions, but rather to develop a nuanced understanding
of how participants construct meaning around privacy and their
lived experiences of being online.
We followed Braun and Clarke’s six-phase framework for reflex-
ive thematic analysis [6]. Consistent with the principles of reflexive
thematic analysis, we acknowledged the role of the researcher in
shaping the analysis. The research team brought interdisciplinary
expertise: computer science, law, and media and communications.
We relied on this diversity to inform our interpretive lens.
All transcripts were analysed by at least 2 researchers. Initial
open coding was used to identify patterns of meaning at the se-
mantic level, with attention paid to both explicit statements and
underlying assumptions. Codes were then generated inductively
and refined through collaborative discussion within the research
team to resolve any disagreements. Thematic development was iter-
ative and recursive, with multiple rounds of refinement undertaken
by a team of researchers from different disciplinary backgrounds
to ensure interpretive rigour and analytic depth.
3.3 Arcade Machines
In this section, we describe the design, implementation, and de-
ployment of our custom arcade machines, which gamify a privacy
survey. The goal of the platform is: (i) to quantify which ontology
components (who – collector type, what – data type, and why –
collection purpose) users deem more or less concerning, and (ii) to
explore how these concerns correlate with demographic variables.
No financial compensation was provided to participants for play-
ing the game. Only participants who provided consent for their
information to be used after gameplay were included in the study.
Each arcade unit consists of a standard bartop cabinet housing
a 10.1 inch capacitive touchscreen, two big colored push-buttons,
five small buttons, and a Raspberry-Pi 4 Model B micro-computer
(4 GB RAM) running Raspberry Pi OS. The Pi is configured in kiosk
mode, auto-launching a Chromium browser in fullscreen at system
boot. Figure 3 shows two assembled units.
During the study period, we placed the arcade machines in three
public locations in Newcastle upon Tyne (UK):
(1) Newcastle City Library (Unit A, 2 months). The first machine
stood on the ground floor of the central public library beside
the main entrance.
(2) Newcastle University (Unit B, 4 months). The second ma-
chine was installed in the ground-floor foyer of a teaching-
and-research complex that hosts daily lectures and multiple
laboratories.
(3) Newcastle upon Tyne Science Festival (Unit A, 1 day). For
one day the same unit was moved to the hands-on zone of
the city-wide science festival.
Table 1: Score interpretation based on GDPR alignment.
Score Range Interpretation
−100 to−67 You are a Privacy Rebel! GDPR is about as far
from your priorities as Earth is from Pluto.
−66 to−34 You and GDPR don’t quite agree! Sexual ori-
entation more critical than finances? Nah,
your wallet cries louder than your secrets!
−33 to+33 GDPR makes sense... sometimes... There are
moments when you think GDPR’s priorities
need a reality check.
+34 to+66 You stand with GDPR! You’re on board with
protecting what really matters.
+67 to+100 You perfectly vibe with GDPR. Like tea and
biscuits, you and GDPR are a match.
The game is implemented in vanilla JavaScript and HTML5. The
client executes entirely locally; no network connection is required
during play. Gameplay state exported in JSON format only when a
participant explicitly consents to data sharing.
We generated 1,000 “who-what-why” prompts of the form𝑐𝑜𝑙𝑙𝑒𝑐𝑡𝑜𝑟
collects𝑑𝑎𝑡𝑎 for 𝑝𝑢𝑟𝑝𝑜𝑠𝑒 , where 𝑐𝑜𝑙𝑙𝑒𝑐𝑡𝑜𝑟 ∈ {website, device,
application} (generic categories rather than named companies),
𝑑𝑎𝑡𝑎 is drawn from our ontology and annotated as special or or-
dinary per GDPR, and 𝑝𝑢𝑟𝑝𝑜𝑠𝑒 is a purpose from the ontology.
1288

Playing with Privacy: Uncovering Everyday Judgments of Data Sensitivity Through an Arcade Machine Interface IUI ’26, March 23–26, 2026, Paphos, Cyprus
Figure 3: Arcade machines (Unit A and B)
Table 2: Demographic questions presented at the end of the
game.
Question Options
What is your age range? 16–24, 25–34, 35–54, 55 or older,
Pass
What is your gender
identity?
Male, Female, Non-binary, Other,
Pass
Highest level of educa-
tion completed?
High School or equivalent, Bache-
lor’s degree, Master’s or Doctoral
degree, Other, Pass
Number of privacy pro-
tection tools used?
None, 1–2 tools occasionally, 3–4
tools regularly, 5+ tools actively,
Pass
The resulting strings were refined with GPT-4 to improve natural-
ness while preserving semantics and later manually checked by the
research team to avoid hallucinations and remove real company
names or replace them with fake ones (to avoid biases associated
with brand reputation).
Figure 4 illustrates the eight key screens of the game experience:
(1) Welcome — displays Press any button. On input, a brief rules
overlay appears; users may continue or exit.
(2) Round Screens (up to 20) — For random ontology state-
ment, players indicate I hate that or I don’t care. The GDPR
agreement meter starts at 0 and shifts 10 points left (green)
for an alignment choice or right (red) for a misalignment.
An 8-bit animation of Elon Musk reacts oppositely to GDPR:
anger for alignment, joy for misalignment.
(3) Termination — The game ends when the meter reaches -50
or +50 points or after 20 rounds.
(4) Results — A summary screen reports the final score and an
interpretation (Table 1).
(5) Demographics — Participants who provided consent to
share data complete a four -item demographic survey (Ta-
ble 2). Data from consenting participants is saved as a JSON
file, and the app resets to the Welcome screen.
For each consenting session, we store: (i) anonymised UUID, (ii)
timestamp, (iii) displayed ontology statements and player responses,
(iv) final meter score, and (v) demographic answers.
1289

IUI ’26, March 23–26, 2026, Paphos, Cyprus Kalameyets et al.
Figure 4: Arcade machine interface
1290

Playing with Privacy: Uncovering Everyday Judgments of Data Sensitivity Through an Arcade Machine Interface IUI ’26, March 23–26, 2026, Paphos, Cyprus
Table 3: Analysis factors and included levels.
Factor Included levels
Collector (who) Website (Web); Application (App); Smart-home de-
vice (IoT).
Data class (what) user_created_data, social_data, id,
device_information, usage_information,
financial,
health_information, Special Protected Data .
Purpose (why) advertisement, product_improvement,
functionality, safety_and_security, legal,
research, user_experience.
Demography Gender : M/F/N-B;
Age: 16–24, 25–34, 35–54, 55+;
Education: School, Bachelor, Master;
Digital literacy: Low/Med/High/Expert.
To quantify how various demographic groups evaluate specific
data-collection scenarios and to link these evaluations to the inter-
view themes, we used the following statistical analysis approach.
Unit of analysis: the user. Each arcade prompt yields a binary
response𝑠𝑢,𝑖 ∈{− 1,+1} for user𝑢 and item 𝑖 (−1=“I hate that” ,
+1=“I don’t care” ). Because users answer multiple prompts, the
statistical data point is the user. All inference is performed on per-
user summaries.
Define base conditions. A condition is a specific combination
of collector (who), data class (what), and purpose (why). For each
user𝑢 and condition𝐶 we compute the mean
¯𝑠𝑢,𝐶 = 1 𝑛𝑢,𝐶 ∑︁ 𝑖∈𝐶 𝑠𝑢,𝑖,
and use ¯𝑠𝑢,𝐶 in subsequent tests. Here,𝑢 indexes users,𝑖 indexes
individual prompts,𝐶 denotes the set of prompts whose (collector,
data class, purpose) equals that condition,𝑠𝑢,𝑖∈{− 1,+1} is user𝑢’s
coded response to prompt𝑖 (−1 = “I hate that”,+1 = “I don’t care”),
and𝑛𝑢,𝐶 =|{𝑖 :𝑖∈𝐶 and was seen by user𝑢}| is the number of
prompts in𝐶 that user𝑢 answered. We compute ¯𝑠𝑢,𝐶 only when
𝑛𝑢,𝐶≥ 1 (users who did not see any item in𝐶 do not contribute to
analyses involving𝐶). When comparing two conditions𝐴 and𝐵
within users, the contrast Δ𝑢 = ¯𝑠𝑢,𝐴− ¯𝑠𝑢,𝐵 is defined only for users
with𝑛𝑢,𝐴≥ 1 and𝑛𝑢,𝐵≥ 1. The four factors and their levels are
shown in Table 3. We focus inference on contrasts and subgroups
with adequate size (e.g.,𝑁≥ 20 users per subgroup).
Hypothesis-driven groupings. To test interview-informed
questions without fragmenting the sample, we (i) pooluser_created
_data and social_data into an expressive grouping (e.g., messages,
photos, posts), and (ii) attach simple attribute tags ( location, con-
tacts, voice/microphone) when the item text explicitly mentions the
keyword (case-insensitive) – this provides clearer and targeted com-
parisons (e.g., Expressive vs Baseline; penalties for location) that
align with the qualitative themes from interviews.
Estimate effects via contrasts. Wherever possible, we use
within-user contrasts to compare two conditions𝐴 and𝐵 for the
same person: Δ𝑢 = ¯𝑠𝑢,𝐴− ¯𝑠𝑢,𝐵, testing whether the average contrast
differs from zero (directional when pre-specified by interviews). To
examine demographic moderation (e.g., Female vs Male, literacy lev-
els, age groups) we compare user-level means across demographic
groups for the same condition.
Uncertainty estimation. Because multiple, related hypotheses
are evaluated, we control the false discovery rate within themat-
ically coherent families (contextualised sensitivity; data steward-
ship/trust; GDPR legitimacy/literacy) and report both raw𝑝-values
and adjusted𝑞-values. We present effect sizes as mean contrasts
with confidence intervals in figures and prioritise interpretation
where sample sizes are sufficient.
The full code and data are provided to accompany the paper,
ensuring reproducibility.
4 Results
We organise the Results around the main concerns raised in the
interviews. We conducted nine semi-structured interviews with
participants. Each interview took place around participants’ en-
gagement with the arcade machine and lasted approximately 25
minutes. For each concern, we first summarise what participants
said (qualitative quotes),and then we test whether the same pat-
tern appears in the arcade data by filtering to the relevant data or
purpose categories and comparing demographic groups. When a
test is significant (𝑝 <.05), we state which groups differ. When it is
not, we report the overall pattern and treat subgroup differences as
inconclusive. As context for the empirical results that follow, the
average playtime in pilot tests was 2.8min. Overall, we got 2935
responses from 224 participants (147 included into analysis, 77 ex-
cluded as they gave less then 5 answers). While Table 4 reports the
demographics of interview participants, Table 5 summarises the
demographic distribution of all participants who engaged with the
arcade machines.
Table 4: Demographic background of participants.
Participant
Number
Age
Bracket Gender Highest Level of Education
1 55+ Male
Diploma in Fine Arts
(degree-equivalent);
Postgraduate Certificate
in Education (PGCE)
2 25–34 Female High school
3 25–34 Male Pursuing bachelor’s degree
4 55+ Male Master’s degree (incomplete)
5 16–24 Male High school (in progress)
6 16–24 Female A Levels and GCSEs; pursuing undergraduate degree
7 16–24 Female Master’s degree (completed)
8 16–24 Male High school (completed)
9 16–24 Male Pursuing undergraduate de-
gree
Table 6 provides an aggregate benchmark contrasting GDPR
Article 9 status with observed dislike rates. The subsequent analyses
examine how sensitivity judgments vary by demographic group
and purpose.
1291

IUI ’26, March 23–26, 2026, Paphos, Cyprus Kalameyets et al.
Table 5: Demographic breakdown: answers and unique participants (by UserID). "Pass” means the participant chose not to
answer that question.
Age Gender
16-24 25-34 35-54 55+ PASS F M N-B Other Pass
Answers 1311 429 461 419 315 791 1552 249 114 229
Participants 102 32 35 30 25 57 123 21 7 16
Education Literacy
School Bachelor Master Other Pass Low Med High Expert Pass
Answers 807 794 725 320 289 608 966 597 453 311
Participants 59 58 58 25 24 47 76 44 33 24
Table 6: Legal status under Article 9 GDPR versus sensitivity in the arcade data. Demographic moderation is reported in Table 7
and in the subgroup analyses.
Data category (grouping) Covered in Art. 9 Dislike (answers) Illustrative demographic spread (key moderator)
Special Protected Data Yes 55.1% (N=490) –
Health information Yes 45.2% (N=648) Literacy: Low 38.9% vs High 55.9% ( 𝑝 =.007)
user_created + social No 47.7% (N=155) Gender: M 33.8% vs F 57.1% ( 𝑝 =.038)
Financial No 47.6% (N=82) (Broadly high; no reliable subgroup effects reported)
ID No 44.5% (N=344) Education: Bachelor 36.0% vs Master 54.9% ( 𝑝 =.005)
Telemetry (device + usage) No 34.8% (N=865) No reliable subgroup differences ( 𝑝≈.35–.79)
Below, we present identified concerns from interviews with
linked findings based on data from arcade machines. In the ar-
cade machines data, answers were coded as −1 (“I hate it”) and
+1 (“I don’t care”). For each concern, we filtered to the relevant
data_class or purposes_class, computed for each demographic
group (age, gender, education, digital literacy) the proportion of
−1 or+1, and compared groups with chi-square (𝜒2) tests. We re-
port𝑝-values to identify whether differences are likely to be real
(𝑝 <.05 taken as statistically significant).
1. Social and expressive privacy (messages, photos, social
ties). Participants worried most about socially exposed “expressive”
content, private chats, personal photos, and visible social ties, be-
cause it could be misread or turned against them. As Participant 5
described, it was “something someone could use against me, ” while
Participant 8 explained that, “I don’t walk around with a sign that
has my most recent messages or photos on it. ” These fears often
translated into active management of visibility as Participant 3 de-
scribed altering privacy settings on WhatsApp so "nobody knows
I’m online. ” Participants 2, 3, 5, 8 and 9 explained that concerns were
rooted less in abstract institutional surveillance than in everyday
risks to reputation, dignity, and control.
Quantitative test. We restricted touser_created_data and social
_data and calculated the share of −1 by demographic; groups
were compared with 𝜒2. Differences were significant by gen-
der (𝑝 = .038): women were most likely to reject sharing expres-
sive/social data (about 60% “do hate it”). Age, education, and literacy
differences were not significant (𝑝 >.05). The qualitative pattern
generalises, with a clearer emphasis among women.
2. Identification (ID) data sensitivity. Participants were di-
vided in their views on sharing basic identifiers such as names
and email addresses. Some regarded these details as trivial (Partici-
pants 4,7, and 9). This opinion was characterised by Participant 7,
who elaborated that providing her full name and date of birth “felt
normal. ” However, others expressed concern about how such in-
formation could be aggregated and misused (Participants 1,2,3 and
6). Participant 6 warned that “your name and your home address. . .
just stuff that could help people identify you more specifically”
required greater caution, particularly on untrusted websites, due
to the risk of crime. This was reflected by Participant 9, who de-
scribed enabling Snapchat’s “ghost mode” to prevent “people with
bad intentions” from accessing his location.
Quantitative test. We filtered data_class=id and compared−1
shares by demographic. The strongest and significant difference
appeared by education: Master’s-level respondents showed the
highest rejection (≈ 60%;𝑝 =.005). Age, gender, and literacy pat-
terns were not statistically reliable (𝑝≥ .06). Higher educational
attainment is associated with more cautious attitudes to ID data,
consistent with interview worries about downstream misuse.
3. Financial data sensitivity. Participants 1,2,6,7, and 8 consis-
tently framed financial details, especially bank account and credit
card information, as the most sensitive category, closely tied to
fraud risk. Participants 1 and 2 described strong mistrust of on-
line financial services, with Participant 1 explaining why he avoids
online banking: “I don’t like doing anything if there’s risk. . . All
the time, on the news, you hear of people. . . somebody has taken
thousands of pounds from them. . . I just mistrust. ” He also linked
this reluctance to difficulties with digital systems, such as forgetting
passwords, preferring in-person transactions over “convenience. ”
1292

Playing with Privacy: Uncovering Everyday Judgments of Data Sensitivity Through an Arcade Machine Interface IUI ’26, March 23–26, 2026, Paphos, Cyprus
Others explicitly identified financial details as their primary
concern. Participant 2 described bank details as “the most sensi-
tive” information, associating them with hackers and scams, and
explained that this perception directly discouraged her from shop-
ping online: “That’s why I don’t really order things online. . . when
you’ve got to put the long 16-digit number in, that’s what I don’t
like. ” Younger participants voiced similar anxieties. For instance,
Participant 8 worried that “credit card information” could be cap-
tured through online interactions and that leaks could put such
data “in the wrong hands. ”
Quantitative test. We filtered data_class=financial and com-
pared−1 shares across groups. Group differences were not statis-
tically reliable (𝑝 > .05)—occasional extreme percentages arose
in very small subgroups. Therefore, concern about financial data
is high and broadly shared rather than concentrated in particular
demographics.
4. Health data sensitivity. Participants consistently framed
health data as intimate and potentially harmful if leaked, often
treating it as a special category requiring heightened protection
(Participants 1,3,4,5,6,8.). As participant 4 explained, “medical data
should [be protected]. . . if somebody has a nasty disease, I can
see that they wouldn’t want that being spread around the office. ”
Pregnancy data was viewed as especially intrusive when collected
outside relevant contexts, with a Participant 6 questioning, “If it’s
not an app. . . specifically for stuff about your pregnancy. . . then
I don’t know why they would need that” By contrast, fitness and
physical data elicited more mixed responses, ranging from accep-
tance when linked to health promotion (Participant 7) to rejection
as unnecessary, with Participant 1 asking “Why would it want
to do that, to know how many steps?... I know how to keep fit, I
don’t need a machine to tell me. ” These findings suggest a clear
hierarchy of sensitivity: medical and pregnancy data were consis-
tently treated as highly personal, while fitness and physical data
were assessed more flexibly, depending on perceived utility and the
trustworthiness of the collector.
Quantitative test. We filtereddata_class=health_information
and compared−1 shares across groups. Differences were signif-
icant by education and digital literacy: Master’s-educated (∼
59.6% “do not like”; 𝑝 < .001) and high-literacy respondents (∼
56.2%;𝑝 = .007) were most cautious. Age and gender differences
were not significant. Greater familiarity with digital risks and higher
education aligns with a stronger reluctance to share health data.
5. Technical tracking (device/usage telemetry). Participants
drew a clear boundary between “always listening” devices and tech-
nical telemetry. Some were unsettled by microphones or cameras
they perceived as “spying. ” Participants 6 called sound-monitoring
apps “a bit creepy” and said, “Yeah, no, I hate that, ” comparing them
to being watched through a laptop camera. Others acknowledged
such surveillance as inevitable, with Participant 4 remarking, “I just
assume that anything smart is collecting data. ” In contrast, technical
traces such as device type, operating system, or error reports were
generally described as impersonal and even called “quite useful” by
Participant 5.
Quantitative test. We pooled device_information and usage
_information and compared−1 shares by demographic. No demo-
graphic differences were significant (all𝑝≈.35-.79). Attitudes to
technical telemetry are relatively even across groups—an ambient,
non-demographic concern.
6. Advertising aversion. Participants 1, 3, 6, 7, and 9 consis-
tently rejected the use of their data for advertising or resale, framing
such practices as intrusive, ineffective, and morally objectionable.
Participant 1 criticised the futility of targeted ads, noting he was
“bombarded with adverts” for items already purchased and dismiss-
ing them as a “nuisance. ” He linked this frustration to a broader
critique of consumerism: “It’s all to encourage that, so I’ll buy some
more. . . I think it’s wrong. ” Others focused on the surveillance un-
derpinning advertising, with participant 3 describing his upset at
targeted ads: “I feel like, obviously, somebody is checking what
I’m doing online. . . it’s an infringement into my privacy. ” Concerns
were particularly acute when sensitive information was implicated,
such as pregnancy status, which participant 6 judged inappropri-
ate unless collected in explicitly relevant contexts. Participants 1
and 7 articulated blanket opposition to adverts while Participant 9
rejected marketing based on political views or personality, citing
both privacy violations and the reinforcement of “confirmation
bias. ” Collectively, these responses highlight how advertising and
resale were viewed not merely as unwanted uses of data, but as
practices intertwined with surveillance.
Quantitative test. We filtered purposes_class=advertisement
and compared−1 shares across demographics. Differences were
significant by education (𝑝 = .008); a small “Other education”
group showed the highest rejection (∼ 83%). Other demograph-
ics did not differ reliably ( 𝑝 > .05). Objection to advertising is
widespread; some educational subgroups are especially critical (the
‘Other education’ group is small, percentages may be unstable).
7. Research scepticism. Participants expressed doubts regard-
ing the category of “research” as a justification for data collection,
particularly when the underlying purpose remained vague or when
individual benefits were not clearly articulated. For example, Partic-
ipant 9 emphasised the importance of transparency and reciprocity:
research uses could be acceptable “if it’s something where I can
clearly see why they’ll want it, or if they were to explain it well. ”
Absent such justification, however, participants 7 and 9 interpreted
the practice as exploitative, with the absence of clear benefits to data
subjects producing perceptions of unfairness and mistrust. This sug-
gests that participants were not rejecting research per se, but rather
research presented without adequate rationale or explanation of its
value to them.
Quantitative test. We filtered purposes_class=research and
compared−1 shares by demographic. Education differences were
significant: Master’s-educated respondents were most likely to
reject research uses (∼ 60.9%;𝑝 =.020). Other demographics did not
differ significantly. Higher education aligns with sharper scrutiny
of research rationales.
8. Legal scepticism and GDPR.. Participants’ knowledge of the
General Data Protection Regulation (GDPR) varied widely, ranging
from no awareness to a detailed understanding, and many described
it as abstract or difficult to use. Several had never heard of the term:
Participant 1 said simply, “No, I’m not familiar. ” Others showed
only vague awareness Participant 5 remarked, “Ish. Ish. Kind of. I
know that it’s about, sort of, like, protecting your data online, but
1293

IUI ’26, March 23–26, 2026, Paphos, Cyprus Kalameyets et al.
I’d say that’s about the extent of my knowledge, ” while Participant
7 noted, “I heard this name, but I don’t know what exactly and how
it works. ” In contrast, a minority articulated accurate definitions.
Participant described it as “an act that protects people’s private
or personal information or. . . restricts unauthorised access, ” and
Participant 9 connected it to data ethics frameworks, observing that
companies “aren’t allowed to collect more information than they
require. ” Despite these differences in knowledge, distrust in institu-
tional stewardship was common. Participant 1 linked regulatory
language to corporate reassurance rather than substantive protec-
tion: “They need to reassure the customer, don’t they, so they’re
not going to give me the full facts, necessarily. ” He explained GDPR
protections were likely disregarded in practice, underscoring a per-
ception that formal rights exist largely in theory rather than as
effective guarantees.
Quantitative test. We examined−1 shares forlegal and corporate
_governance purposes across demographics. Group differences
were not statistically reliable (𝑝≥ .05), though rejection for these
formal justifications was generally higher than for protective pur-
poses (e.g., safety). The qualitative scepticism toward legalistic
rationales appears diffuse, shared across groups rather than con-
centrated in specific demographics.
9. Resignation vs. general criticality. Participants framed pri-
vacy loss as structurally inevitable, positioning data collection as
an unavoidable condition of digital life. Participant 1 captured this
bluntly: “I can’t avoid it, can I?”; Participant 4 echoed, “It’s going
to happen anyway”; and Participant 9 concluded, “You can never
be fully comfortable with it, but there’s not a lot you can really do. ”
Such resignation was compounded by fatigue with privacy notices,
which were perceived as both unintelligible—“boring, long, long,
long sentences” (Participant 3)—and impractically time-consuming.
As a result, participants routinely disengaged, exemplified by Par-
ticipant 6’s admission: “I instantly accept cookies. . . just kind of
as a time thing. ” Collectively, these accounts suggest that consent
mechanisms not only fail to provide meaningful control but also ac-
tively normalise resignation, reinforcing a perception that privacy
cannot be protected.
Quantitative test. For each group we computed (a) general criti-
cality—the share of−1 over all data-purpose pairs; and (b) general
acceptance—the share of+1. General criticality was significantly
higher among age 35-54 (∼ 48.5%;𝑝 =.025), Master’s-educated
(∼ 51.3%;𝑝 < .001), and high-literacy (∼ 46.9%;𝑝 < .001). Con-
versely, general acceptance was higher for age 25-34 (∼ 62.2%;
𝑝 = .025), Bachelor’s (∼ 65.6%; 𝑝 < .001), and low literacy
(∼ 64.8%;𝑝 < .001). This mirrors the interviews: more mature
and/or more digitally confident groups tend to hold a principled,
critical stance; younger or less digitally confident groups more often
“let it pass” as routine.
10. Conditional acceptability for safety and functional-
ity. Participants consistently evaluated data collection through a
fairness lens, distinguishing between purposes they perceived as
protective or useful and those they saw as extractive. Protective
purposes were accepted when narrowly tailored and reciprocal,
such as safeguarding accounts or preventing spam. Participant 4,
for instance, justified password checks as “necessary for security, ”
while Participant 6 likened email collection for spam prevention to
familiar practices, such as Google login alerts. Participants also tol-
erated data used to improve functionality or personalisation when
benefits flowed back to them, with Participant 8 noting, “I want the
algorithm to suit me more. ”
By contrast, extractive uses, especially for marketing or resale,
were rejected as unfair. Participant 6 questioned why pregnancy
status should inform advertising: “If it’s not an app. . . specifically
for pregnancy, then I don’t know why they would need that. ” Par-
ticipant 9 drew the fairness line explicitly: “If there’s no apparent
reasoning and I’m not getting any clear benefit. . . then it just seems
wrong. ” Others were categorical, with Participant 7 stating sim-
ply, “I hate it. I don’t like advertised. ” Vagueness further eroded
legitimacy: Participant 1 distrusted the term “security” because it
“usually suggests the opposite, ” while Participant 9 dismissed IoT
data collection, such as that from a smart fridge, as “a bit weird. . .
unnecessary. ”
Quantitative test. We analysed+1 shares forsafety_and_security
and, separately, forfunctionality, user_experience, andproduct
_improvement. Safety acceptance was higher amongmen (∼ 67.2%;
𝑝 =.041) and a small “Other education” group (∼ 80%;𝑝 =.011). For
functionality/UX, acceptance was highest among low-literacy
respondents (∼ 73.1%;𝑝 = .003); age and education showed bor-
derline trends (𝑝≈.06-.07). Perceived user benefit and protection
increase tolerance of data collection, especially where immediate
usefulness is salient or resources to evaluate downstream risks are
lower.
Robustness notes. Where we report non-significant results (𝑝≥ .05),
differences should be read as patterns rather than firm effects. Some
extreme percentages reflect very small subgroups; we emphasise
effect direction with appropriate caution. Throughout, we used
simple, transparent comparisons (one concern at a time and direct
group contrasts) to keep the analysis accessible.
These concerns, as well as their quantitative interpretation, are
summarised in Table 7.
5 Discussion
Reflections on Findings. Our mixed-methods study points to a
clear pattern. People worry most about content that shows who
they are to others in everyday life. They are cautious about identity
and health information, and they treat financial details as strictly
off-limits. Why data are used matters a lot: safety and core functions
are easier to accept, while advertising and vague “research” uses are
not. Background device data (such as telemetry) worries people, but
it does not split the population into clear camps. Many people have
low awareness of the GDPR and feel tired of long notices, which
feeds a split between steady scepticism and “let it pass” acceptance.
Below we explain each point, supporting them with results from
Table 7.
Participants were most concerned about socially exposed, ex-
pressive content—private chats, personal photos, and visible so-
cial links—being misinterpreted or used against them (“something
someone could use against me, ” “I don’t walk around with a sign
that has my most recent messages or photos on it”). In the arcade
data, this shows up as higher rejection of expressive/social data
among women (about 60% “dislike”; difference by gender significant,
𝑝=.038). Differences by age, education, and digital literacy were not
1294

Playing with Privacy: Uncovering Everyday Judgments of Data Sensitivity Through an Arcade Machine Interface IUI ’26, March 23–26, 2026, Paphos, Cyprus
Table 7: Interview concerns and quantitative interpretation.
Concern from inter-
views
Interpretation from quantitative data
Social / expressive pri-
vacy (messages, photos,
ties)
Women show the highest rejection ( ∼
60% “dislike”; gender differences significant,
𝑝=.038); age, education, literacy not signifi-
cant.
Identification (ID) data
sensitivity
Highest rejection among Master’s-educated
(∼60%; education significant,𝑝=.005); other
demographics not reliably different.
Financial data sensitiv-
ity
Concern is broadly high across groups; dif-
ferences not statistically reliable (𝑝>.05); ex-
treme values stem from small subgroups.
Health data sensitivity Higher rejection among Master’s-educated
(∼ 59.6%,𝑝<.001) and high digital literacy
(∼56.2%,𝑝=.007); age and gender not signif-
icant.
Technical tracking (de-
vice / usage telemetry)
Moderate rejection overall; no significant de-
mographic differences (all𝑝≈.35-.79).
Advertising aversion
(purpose)
Education differences significant (𝑝=.008);
“Other education” subgroup shows the high-
est rejection (∼83%); other demographics not
significant.
Research scepticism
(purpose)
Master’s-educated most critical (∼60.9% “dis-
like”; education significant, 𝑝=.020); other
demographics not significant.
Legal / corporate gover-
nance scepticism (pur-
pose)
Rejection relatively elevated but not concen-
trated demographically; group differences
not significant (𝑝≥.05).
Safety acceptance (pur-
pose)
Higher “don’t care” among men (∼ 67.2%,
𝑝=.041) and “Other education” ( ∼ 80%,
𝑝=.011); other demographics not significant.
Functionality / UX ac-
ceptance (purposes)
Highest “don’t care” among low digital liter-
acy (∼73.1%; significant,𝑝=.003); age / edu-
cation show borderline trends (𝑝≈.06-.07).
General negativity (all
data-purpose pairs)
Higher overall “dislike” for age 35-54 ( ∼
48.5%,𝑝=.025), Master’s-educated (∼51.3%,
𝑝<.001), and high literacy (∼46.9%,𝑝<.001).
General acceptance (all
data-purpose pairs)
Higher overall “don’t care” for age 25-34 (∼
62.2%,𝑝=.025), Bachelor’s (∼65.6%,𝑝<.001),
and low literacy (∼64.8%,𝑝<.001).
substantial. In short, concerns here are mainly social: people fear
judgment and harm from other people, not only from institutions.
Sensitivity was tiered across data types. Some saw basic identi-
fiers (like name or email) as routine (“basic information we don’t
need to protect”), while others stressed how small bits, when com-
bined, can enable fraud (“if a hacker knows name, e-mail, date of
birth. . . he could hack”). Quantitatively, rejection of ID data was
highest among Master’s-educated respondents (about 60%;𝑝=.005).
Health data were often called intimate and risky (“even the NHS
had a data leak”), and rejection was higher for Master’s-educated
(∼59.6%;𝑝<.001) and high-literacy respondents (∼56.2%;𝑝=.007).
Financial details drew strong concern across the board; group differ-
ences were not significant (𝑝>.05). Together, these results show a
consistent ladder of concern: expressive/social, identity, and health
at the top; finance is universally sensitive. Importantly, health-
related data fall under Article 9, whereas expressive/social and
financial data do not. This ordering is broadly stable across gen-
der and age. Subgroup differences mainly change the strength of
rejection (e.g., women are more negative toward expressive/social
content) rather than reversing the cross-type ordering.
The purpose of data collection shaped acceptability. People drew
a clear line between uses that protect or help them and uses that
extract value for others. Interviewees were comfortable with safety
and core functions, but objected to advertising and sale to third
parties (“for safety and security. . . ok; for their marketing. . . no”;
“companies sell your data to third parties”). In the arcade data,
safety/security had higher acceptance among men (∼67.2%;𝑝=.041)
and a small “Other education” group (∼80%;𝑝=.011). Advertising
triggered broad rejection with significant differences by educa-
tion (𝑝=.008). Vague “research” uses faced scepticism unless clear
benefits were explained; rejection was highest among Master’s-
educated (∼60.9%;𝑝=.020). Functionality and user-experience were
more acceptable when usefulness was evident, especially among
low-literacy respondents (∼73.1% acceptance;𝑝=.003).
Always-on telemetry (device or usage traces) made some partic-
ipants uneasy, especially when microphones were mentioned. Yet
quantitatively this concern did not differ reliably by age, gender,
education, or literacy (all 𝑝≈ .35-.79), suggesting a background
worry that is broadly shared (Table 7).
In addition, long privacy policies and unclear options led people
to skip reading or to click through quickly. In the data, this maps
onto two general stances. Overall “dislike” was higher among those
aged 35-54 (∼48.5%;𝑝=.025), Master’s-educated (∼51.3%;𝑝<.001),
and high-literacy respondents (∼46.9%;𝑝<.001). Overall acceptance
was higher among ages 25-34 (∼62.2%;𝑝=.025), Bachelor’s-educated
(∼65.6%;𝑝<.001), and low-literacy respondents (∼64.8%;𝑝<.001).
Interviews describe this split as principled scepticism versus prag-
matic acceptance (“it’s going to happen anyway”) (Table 7).
Our demographic findings also highlight where public percep-
tions both align with and diverge from the GDPR’s current defini-
tion of “special categories” under Article 9. As an overall benchmark,
Table 6 shows that several non-Article 9 categories (notably social
and financial data) attract dislike rates comparable to Article 9 cat-
egories, while the detailed subgroup analyses reveal substantial
demographic moderation. Health data was consistently treated as
intimate and sensitive, confirming the rationale for its inclusion as
a legally protected category. However, participants also regarded
financial information and expressive/social content (such as private
messages, photos, and visible ties) as equally, if not more, sensi-
tive, yet these are not afforded comparable legal status under the
GDPR. Women, in particular, expressed heightened concerns about
expressive content, reflecting gendered vulnerabilities that remain
invisible in existing legal categories. Similarly, participants with
higher education and digital literacy demonstrated more caution
towards ID and health data, suggesting that awareness of down-
stream aggregation risks may shape broader notions of sensitivity.
Taken together, these findings demonstrate that everyday judg-
ments of data sensitivity do not align neatly with the GDPR’s static
sensitivity list. This misalignment exposes regulatory blind spots in
which the law underestimates risks encountered in routine digital
interactions.
Against this backdrop, our findings suggest that legal and design
interventions should be aligned more closely with how people
1295

IUI ’26, March 23–26, 2026, Paphos, Cyprus Kalameyets et al.
experience sensitivity in everyday contexts. To this end, we offer
the following complementary policy recommendations. First, make
social exposure clear at the moment data are captured. Tell people,
in plain language, who will see their expressive content, for what
reason, and for how long. Offer short retention by default and a
one-tap way to stop sharing. These measures give practical effect
to the purpose and storage limitation principles in Article 5(1)(b)
and (e) GDPR, and to the requirement in Article 25 GDPR to embed
data protection by design and by default.
Second, reduce extractive uses through interface-level trans-
parency. Standardise a short “data label” for each feature (type,
purpose, retention, recipients) so people can quickly spot adver-
tising or third-party sharing. This directly operationalises Articles
12-14 GDPR, which require information to be provided “in a concise,
transparent, intelligible and easily accessible form, using clear and
plain language. ”
Third, support understanding under time pressure. Place short
notices next to the feature that needs the data, keep a simple “map”
of active data flows, and include explanations for “why am I seeing
this?” This implements Recital 39 and Article 13(1)(c) GDPR, which
require controllers to inform users of the purposes of processing “at
the time when personal data are obtained. ” Embedding explanations
within the interaction flow ensures data use is legible at the point
of interaction and should be supported by reporting not just opt-ins
but also how often people review and revoke sharing.
Finally, public arcade deployments worked well for engaging
passersby, prompting quick choices, and collecting large numbers
of responses. However, such deployments may introduce context
effects such as the venue, time of day, or peer presence that shape
participants’ choices. To address this limitation, we paired arcade
data with follow-up interviews to explain why people make their
choices. We maintain analytical transparency by reporting sub-
group sizes, conducting straightforward statistical tests, and pro-
viding confidence intervals (see Results and Table 7).
Overall, our results reveal several key patterns. People place the
most weight on social legibility and trust in purpose. Expressive
content, identity markers, and health data require heightened safe-
guards. By contrast, safety concerns and core service functions
can justify limited, time-bound data use. Opaque or commercial
purposes face broad resistance.
Broader Societal Implications. At present, the GDPR’s strongest
safeguards are linked to Article 9 "special categories, " while the
data people experience as most risky, messages, photos, and visi-
ble social ties, rarely receive equivalent protection in practice. To
address this gap within the existing framework, the GDPR could
incorporate an "expressive data safeguard" through targeted ad-
justments to three key provisions. First, Article 25 (data protection
by design and by default) could be clarified to require heightened
defaults whenever controllers process expressive personal data.
These defaults would apply short retention periods and disable
third-party sharing unless explicitly authorised. Second, the DPIA
Data Protection Impact Assessment), which is an assessment used
to identify and mitigate risks to data subjects’ rights and freedoms
could be extended to explicitly evaluate the risks of large-scale
analysis of expressive content, ensuring that such practices are
subject to enhanced safeguards proportionate to their invasiveness.
Finally, Articles 12–14 could mandate in-flow, just-in-time "purpose
labels" that specify data type, purpose, retention, and recipients,
providing contextual transparency at the moment of data collection
rather than through static privacy policies. To take our recommen-
dations forward, policymakers and supervisory authorities such as
the ICO UK Information Commissioner’s Office), which is the UK’s
data protection regulator, should issue guidance encouraging data
controllers to adopt heightened defaults for vulnerable groups and
to examine the risk of such practices within the DPIA. Over time,
these practices could be codified, ensuring that the GDPR remains
responsive to mitigating the risk posed by the types of data citizens
are most concerned about.
6 Conclusion
Across interviews and arcade play, participants cared most about
content that showcases them to others in social settings, such as
messages, photos, and visible ties, followed by identity and health
information. Financial details were seen as risky by almost everyone.
Why data are collected mattered as much as what is collected: safety
and core functionality were easier to accept, while advertising and
vague “research" claims drew pushback. Device and usage telemetry
raised some concerns but did not strongly split groups. We also
observed uneven awareness and trust regarding the GDPR. Women
were more reluctant to share expressive content, and individuals
with higher education or digital literacy were more cautious about
sharing ID and health data. Our mixed approach linked what people
said to their choices in play, providing clear, testable insights.
We demonstrate that design and policy should centre on social
exposure and purpose. Platforms should clearly state who can view
expressive content, why, and for how long. They should set short
retention periods by default rather than rely on indefinite storage.
Simple “data labels” should be provided to indicate the type of data
collected, its purpose, its retention period, and the parties with
whom it is shared. Explanations should be brief and placed at the
point of decision-making, and third-party sharing should be audited
or limited. Critically, safeguards exceeding the GDPR’s minimum
requirements are necessary when handling expressive content, iden-
tity information, and health data. Looking ahead, future research
should deploy arcade interfaces more widely, test design changes
in real-world settings, and track how actual decisions shift when
users are given clearer and more granular control.
Ethics Board Approval and Anonymity
Prior to deploying the arcade machines and conducting interviews
with participants, this study received full approval from Newcastle
University institutional ethics review board. For the qualitative
elements of this study, to protect participant confidentiality, all
interviewees were anonymised through the removal of personal
identifiers from coded excerpts. Although audio recordings were
made during the interviews, only anonymised textual transcripts
were retained for analysis. All original audio files were permanently
deleted within six months after the study’s conclusion.
1296

Playing with Privacy: Uncovering Everyday Judgments of Data Sensitivity Through an Arcade Machine Interface IUI ’26, March 23–26, 2026, Paphos, Cyprus
Data Availability
The arcade-machine dataset analysed in this paper is publicly avail-
able on Kaggle via the link:
https://doi.org/10.34740/kaggle/dsv/14571715
A short demonstration video of the arcade machine and interac-
tion flow is available on YouTube:
https://youtube.com/shorts/-y8s17dDrdQ?feature=share
References
[1] Noura Abdi, Xiao Zhan, Marvin Ramokapane, and Jose M. Such. 2021. Privacy
Norms for Smart Home Personal Assistants. In CHI Conference on Human Factors
in Computing Systems (CHI ’21) . ACM. doi:10.1145/3411764.3445122
[2] Alessandro Acquisti, Laura Brandimarte, and George Loewenstein. 2015. Privacy
and human behavior in the age of information. Science 347, 6221 (2015), 509–514.
[3] Andy Alorwu, Niels van Berkel, Jorge Goncalves, Jonas Oppenlaender,
Miguel Bordallo López, Mahalakshmy Seetharaman, and Simo Hosio. 2022.
Crowdsourcing sensitive data using public displays—opportunities, challenges,
and considerations. Personal and Ubiquitous Computing 26, 3 (2022), 681–696.
[4] Nazanin Andalibi and Andrea Forte. 2018. Responding to Sensitive Disclosures
on Social Media: A Decision-Making Framework.ACM Transactions on Computer-
Human Interaction 25, 6 (2018). doi:10.1145/3241044
[5] Alex Bowyer, Jack Holt, Josephine Go Jefferies, Rob Wilson, David Kirk, and
Jan David Smeddinck. 2022. Human-GDPR interaction: practical experiences
of accessing personal data. In Proceedings of the 2022 CHI conference on human
factors in computing systems . 1–19.
[6] Virginia Braun and Victoria Clarke. 2019. Reflecting on reflexive thematic analysis.
Qualitative research in sport, exercise and health 11, 4 (2019), 589–597.
[7] Adéle da Veiga. 2022. A study on information privacy concerns and expectations
of demographic groups in South Africa. Computer Law & Security Review 47
(2022), 105769.
[8] European Commission. 2025. Omnibus IV. https://single-market-economy.ec.e
uropa.eu/publications/omnibus-iv_en. Accessed: 2025-09-28.
[9] Simon Gunst and Ferdi De Ville. 2021. The Brussels effect: how the GDPR
conquered Silicon Valley. European Foreign Affairs Review 26, 3 (2021).
[10] Information Commissioner’s Office. 2024. Data Lives: Year 2 — Final Report .
Technical Report. ICO. https://ico.org.uk/media2/migrated/4032384/ico-data-
lives-year-2-report.pdf Accessed: YYYY-MM-DD.
[11] Catherine Jasserand. 2023. Article 10: Processing of Special Categories of Personal
Data. LED Commentary, OUP (Fall 2023, Forthcoming), University of Groningen
Faculty of Law Research Paper 21 (2023).
[12] Leslie K John, Alessandro Acquisti, and George Loewenstein. 2011. Strangers on
a plane: Context-dependent willingness to divulge sensitive information. Journal
of consumer research 37, 5 (2011), 858–873.
[13] Bart P. Knijnenburg, Alfred Kobsa, and Hongxia Jin. 2013. Dimensionality of
Information Disclosure Behavior. International Journal of Human-Computer
Studies 71, 12 (2013), 1144–1162. doi:10.1016/j.ijhcs.2013.06.003
[14] He Li, Lu Yu, and Wu He. 2019. The impact of GDPR on global technology
development. 6 pages.
[15] Wenlong Li, Zihao Li, Wenkai Li, Yueming Zhang, and Aolan Li. 2025. Mapping
the empirical literature of the GDPR’s (In-) effectiveness: A systematic review.
Computer Law & Security Review 57 (2025), 106129.
[16] Yifang Li, Nishant Vishwamitra, Hongxin Hu, and Kelly Caine. 2020. Towards a
Taxonomy of Content Sensitivity and Sharing Preferences for Photos. In Proceed-
ings of the 2020 CHI Conference on Human Factors in Computing Systems . ACM.
doi:10.1145/3313831.3376498
[17] Wainer Lusoli, Margherita Bacigalupo, Francisco Lupiáñez-Villanueva, Norberto
Andrade, Shara Monteleone, and Ioannis Maghiros. 2012. Pan-European Survey
of Practices, Attitudes and Policy Preferences as Regards Personal Identity Data
Management. Technical Report. European Commission, Joint Research Centre.
Also available as SSRN working paper (Abstract ID: 2086579).
[18] Hiroshi Miyashita. 2021. Human-centric data protection laws and policies: A
lesson from Japan. Computer law & security review 40 (2021), 105487.
[19] Moritz Müller, Giovane C. M. Moura, Ricardo de O. Schmidt, and John Heide-
mann. 2017. Recursives in the wild: engineering authoritative DNS servers. In
Proceedings of the 2017 Internet Measurement Conference (London, United King-
dom) (IMC ’17). Association for Computing Machinery, New York, NY, USA,
489–495. doi:10.1145/3131365.3131366
[20] Helen Nissenbaum. 2004. Privacy as contextual integrity. Wash. L. Rev. 79 (2004),
119.
[21] Nina V Nygren, Ville Kankainen, and Lucas Brunet. 2022. Offsetting
game—framing environmental issues in the design of a serious game. Simu-
lation & Gaming 53, 6 (2022), 615–644.
[22] Judith S. Olson, Jonathan Grudin, and Eric Horvitz. 2005. A Study of Preferences
for Sharing and Privacy. In CHI ’05 Extended Abstracts on Human Factors in
Computing Systems. ACM, 1985–1988. doi:10.1145/1056808.1057073
[23] Carolyn Petersen, Jeffery Smith, Robert R Freimuth, Kenneth W Goodman,
Gretchen Purcell Jackson, Joseph Kannry, Hongfang Liu, Subha Madhavan, Dean F
Sittig, and Adam Wright. 2021. Recommendations for the safe, effective use of
adaptive CDS in the US healthcare system: an AMIA position paper. Journal of
the American Medical Informatics Association 28, 4 (2021), 677–684.
[24] Kathryn E. Ringland. 2019. A Place to Play: The (Dis)Abled Embodied Expe-
rience for Autistic Children in Online Spaces. In Proceedings of the 2019 CHI
Conference on Human Factors in Computing Systems (Glasgow, Scotland Uk)
(CHI ’19) . Association for Computing Machinery, New York, NY, USA, 1–14.
doi:10.1145/3290605.3300518
[25] Michael Sailer and Lisa Homner. 2020. The gamification of learning: A meta-
analysis. Educational psychology review 32, 1 (2020), 77–112.
[26] Eva-Maria Schomakers, Chantal Lidynia, Dirk Müllmann, Roman Matzutt, Klaus
Wehrle, Indra Spiecker genannt Döhmann, and Martina Ziefle. 2019. Putting
Privacy into Perspective - Comparing Technical, Legal, and Users’ View of Data
Sensitivity. CoRR abs/1911.06569 (2019). arXiv:1911.06569 http://arxiv.org/abs/
1911.06569
[27] Wouter MP Steijn and Anton Vedder. 2015. Privacy under construction: A de-
velopmental perspective on privacy perception. Science, Technology, & Human
Values 40, 4 (2015), 615–637.
[28] Omer Tene and Jules Polonetsky. 2012. Big data for all: Privacy and user control
in the age of analytics. Nw. J. Tech. & Intell. Prop. 11 (2012), 239.
[29] Marvin Van Bekkum and Frederik Zuiderveen Borgesius. 2023. Using sensitive
data to prevent discrimination by artificial intelligence: Does the GDPR need a
new exception? Computer Law & Security Review 48 (2023), 105770.
[30] Heng Xu, Tamara Dinev, Jeff Smith, and Paul Hart. 2011. Information privacy
concerns: Linking individual perceptions with institutional privacy assurances.
Journal of the Association for Information Systems 12, 12 (2011), 1.
[31] Toshihiro Yamauchi, Yohei Akao, Ryota Yoshitani, Yuichi Nakamura, and Masaki
Hashimoto. 2021. Additional kernel observer: privilege escalation attack preven-
tion mechanism focusing on system call privilege changes. International Journal
of Information Security 20, 4 (2021), 461–473.
1297
