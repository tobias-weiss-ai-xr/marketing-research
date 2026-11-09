---
title: Influence Operations in Social Networks
url: https://arxiv.org/abs/2502.11827
category: social-media
subcategory: empirical
date: 2025-02
venue: ''
authors:
- Javier Pastor-Galindo
- Pantaleone Nespoli
- José A. Ruipérez-Valiente
- David Camacho
source: arxiv
pdf_url: https://arxiv.org/pdf/2502.11827
pages: 11
chars: 40388
fetched_at: '2026-11-08T13:08:41+00:00'
kb_version: 1
---

# Influence Operations in Social Networks

Influence Operations in Social Networks
JA VIER PASTOR-GALINDO,Computer Systems Engineering Department, Universidad Politecnica de
Madrid, Spain
PANTALEONE NESPOLI and JOSÉ A. RUIPÉREZ-V ALIENTE,Department of Information and
Communications Engineering, University of Murcia, Spain
DA VID CAMACHO,Computer Systems Engineering Department, Universidad Politecnica de Madrid,
Spain
An important part of online activities are intended to control the public opinion and behavior, being considered
currently a global threat. This article identifies and conceptualizes seven online strategies employed in social
media influence operations. These procedures are quantified through the analysis of 80 incidents of foreign
information manipulation and interference (FIMI), estimating their real-world usage and combination. Finally,
we suggest future directions for research on influence operations.
CCS Concepts: • Security and privacy → Social network security and privacy .
Additional Key Words and Phrases: social networks, disinformation, misinformation
ACM Reference Format:
Javier Pastor-Galindo, Pantaleone Nespoli, José A. Ruipérez-Valiente, and David Camacho. 2025. Influence
Operations in Social Networks. 1, 1 (February 2025), 11 pages. https://doi.org/XXXXXXX.XXXXXXX
1 THE INFLUENCE CYBER BATTLEGROUND
The rise of social media and other online communication channels has provided unprecedented
reach and efficiency for intentional influence campaigns, having an important escalation from
Russia’s interference in the 2016 U.S. election. Governments are worried about these risks and
social platforms seriously fight against the so-called coordinated inauthentic behavior (CIB) [28].
In 2023, the landscape of influence operations saw a significant rise in detected Foreign In-
formation Manipulation and Interference (FIMI) incidents, with the European External Action
Service (EEAS) report [12] identifying 750 cases between December 1, 2022, and November 30,
2023, nearly doubling the previous year’s figures. FIMI attacks were globally distributed, targeting
53 countries, with Ukraine, the United States and several European nations being the most affected.
The content dissemination involved the coordinated use of websites and social media to create
illusions of authentic discourse and obscure origins, with cross-platform reach as a standard practice.
Unfortunately, this global threat is expected to be massively automated with generative artificial
intelligence, as stated by OpenAI [17], Microsoft [22] or Google [18].
Consequently, the study of online influence operations has grown in the last few years [ 16].
Existing case studies have focused on characterizing disinformation methods, inferring strategies
Authors’ Contact Information: Javier Pastor-Galindo, Computer Systems Engineering Department, Universidad Politecnica
de Madrid, Madrid, Spain; Pantaleone Nespoli; José A. Ruipérez-Valiente, Department of Information and Communications
Engineering, University of Murcia, Murcia, Spain; David Camacho, Computer Systems Engineering Department, Universidad
Politecnica de Madrid, Madrid, Spain.
Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee
provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the
full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored.
Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires
prior specific permission and/or a fee. Request permissions from permissions@acm.org.
© 2025 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM XXXX-XXXX/2025/2-ART
https://doi.org/XXXXXXX.XXXXXXX
, Vol. 1, No. 1, Article . Publication date: February 2025.
arXiv:2502.11827v1  [cs.SI]  17 Feb 2025

2 Javier Pastor-Galindo, Pantaleone Nespoli, José A. Ruipérez-Valiente, and David Camacho
from observed behaviors, assessing political impacts, analyzing interactions or identifying users
likely to spread deceptive content [28], among others. Particularly, there is a clear tendency towards
proposing unsupervised and supervised machine learning methods for detection and analysis.
However, the former are limited in scalability and timeliness, while the latter do not fully address
variability and detectability over time and across campaigns [ 1]. That is why the conclusions
reported in the literature usually have a partial, biased, or limited understanding of the problem [7].
In this context, apart from existing applied research and empirical studies, more analytical
research is needed to abstract the concept of an influence operation, set academic foundations and
homogenize the vision of this global challenge [29]. Particularly, the interpretation of influence
operations stands multidisciplinary, with several dimensions coming into play such as psychology,
sociology, political science, communication studies or computer science. That is why there is little
consensus on how to best describe and address influence operations [4]. In this line, and recognizing
that systematic modeling of influence operations is far from established, particularly on social
networks, we propose seven broader influence strategies that allow for a unified and structured
analysis of campaigns across social platforms.
2 INFLUENCE OPERATIONS: TOW ARDS A COMMON UNDERSTANDING
Influence operations are deliberate activities performed by threat actors to sway public opinion and
manipulate decision-making globally [7]. Their analysis is crucial for interpretation, standardized
knowledge, and shareable intelligence, often guided by models adopted by agencies, organizations,
and researchers [8].
Several frameworks can aid in structuring influence operation analysis. The ALERT taxon-
omy [11] categorizes political disruption tactics, while the ABCDE framework [25] assists EU
institutions and platforms in identifying key operational components. The Carnegie Mellon BEND
framework [9] details structural and narrative maneuvers, and the U.S. government’s SCOTCH
framework [4] integrates technological, organizational, and human factors for adversarial opera-
tions. One promising perspective is the consideration of them as cyber operations, calling for efforts
to understand the problem from the cybersecurity discipline. The Norwegian Defense Research
Establishment adapted the cyber kill chain for social media influence campaigns [3], mapping the
phases from reconnaissance to impact. Researchers at NYU [23] developed a similar framework
based on interviews with fact-checkers and analysts, characterizing threat actors, attack patterns,
channels, and targets. More rigorous proposals have been proposed by the Misinfosec Working
Group’s AMITT framework [31], later enhanced by MITRE and Florida International University into
SP!CE, extending MITRE ATT&CK to influence campaigns. In 2022, these merged into the DISARM
framework [36], now supported by the DISARM Foundation. While SP!CE remains used by the U.S.
Department of Defense, MITRE continues collaborating with DISARM to counter cyber-enabled
influence operations [34]. Finally, Meta researchers introduced theOnline Operations Kill Chain [24],
detailing ten steps used to analyze takedowns of influence campaigns on Facebook.
While the reviewed frameworks effectively characterize general online operations, they lack a
clear focus on understanding adversary campaigns on social media. Nevertheless, they provide
a foundation to propose key strategies of influence operations in social networks. In particular,
the DISARM framework [36] is one of the most comprehensive and up-to-date alternatives, being
currently employed in several projects (e.g., Attribution Data Analysis Countermeasures Inter-
operability [35], ATHENA [2] or the European Digital Media Observatory [27]). It has also been
adopted by important organizations (such as EU DisinfoLab [19], the European Center of Excellence
for Countering Hybrid Threats (Hybrid CoE) [37], the European Union Agency for Cybersecurity
, Vol. 1, No. 1, Article . Publication date: February 2025.

Influence Operations in Social Networks 3
Plan Prepare Execute Assess
Plan strategy Develop narratives Conduct pump priming Assess effectiveness
Plan objectives Develop content Deliver content
Target audience analysis Establish social assets Maximize exposure
Establish legitimacy Drive online harms
Microtarget Drive offline activity
Select channels and affordances Persist in the information environment
Table 1. DISARM phases and associated tactics in adversary influence operations.
(ENISA) [13], the European External Action Service (EEAS) [12] or the Alliance for Securing Democ-
racy [33]), demonstrating its practical utility and reliability. The DISARM framework1 follows the
philosophy of the MITRE ATT&CK matrix2 and considers that influence operations are structured
hierarchically into phases, tactics, and techniques. It defines the following four phases: 1) plan (set
clear goals and strategies), 2) prepare (assemble resources for readiness, including people, networks,
channels and content), 3) execute (deploy the operation from start to finish, maintaining presence
as needed), and 4) assess (review the outcome to improve future maneuvers). As detailed in Table 2,
each phase aggregates a set of tactics. Finally, each tactic can be achieved through specific fine-
grained actions, called techniques. There are more than one hundred predefined techniques under
the sixteen tactics, which can be explored in detail through the DISARM Framework Explorer3. For
instance, in the phase of execute, the tactic deliver content includes techniques like deliver ads, post
content, comment or reply on content , and attract traditional media.
The resulting matrix is a robust tool for modeling and evaluating various types of influence
operations in social networks. Among other benefits, this cybersecurity-inspered modeling facili-
tates the understanding of adversary strategies, analyzing indicators of compromise (IOC), building
tailored reactions to the precategorized techniques, increasing cooperative and collective resilience,
and countering complex problems such as hybrid threats, advanced persistent threats (APT), or the
last tailored term of advanced persistent manipulators (APM) [12, 22].
3 INFLUENCE OPERATIONS STRATEGIES IN SOCIAL NETWORKS
Strategy refers to high-level procedures aimed at achieving long-term objectives. In influence
operations on social networks, strategy represents a calculated approach to manipulate beliefs,
perceptions, and behaviors. To address the lack of clear definitions in the literature, we infer
influence strategies from the DISARM framework as follows:
(1) Identify execution-phase DISARM techniques specific to social networks . While the DISARM
phases of plan, prepare, and assess are medium-agnostic, execution techniques are tied to
communication channels. We select and focus on seven techniques exploiting social networks
as the primary attack vector, shown in the right part of Figure 1:(1) Post content, (2) Amplify
Narratives, (3) Incentivize Sharing , (4) Comment or reply on content , (5) Deliver ads , (6)
Harass, and (7) Flood the Information Space .
(2) Map execution techniques to their predecessor techniques from previous phase . This reverse map-
ping exposes the strategic decisions and resource allocation required for executing influence
strategies. By traversing the DISARM matrix, we form disjoint groups of techniques to define
decoupled strategies. Consequently, the planning and assessment phases are excluded due to
1https://disarmframework.herokuapp.com/
2https://attack.mitre.org/
3https://disarmframework.herokuapp.com/technique/
, Vol. 1, No. 1, Article . Publication date: February 2025.

4 Javier Pastor-Galindo, Pantaleone Nespoli, José A. Ruipérez-Valiente, and David Camacho
Narrative
Release
Narrative
Support
Narrative
Amplification
Counter-Narrative
Reaction
Narrative
Manipulation
Target
Degradation
Information
Pollution
ESTABLISH
SOCIAL ASSETS
DEVELOP
NARRATIVES
DEVELOP
CONTENT MICROTARGET
DELIVER
CONTENT
MAXIMIZE
EXPOSURE
DRIVE
ONLINE HARMS
Leverage Existing
Narratives
Develop Competing
Narratives
Develop
New Narratives
Leverage Conspiracy
Narratives
Integrate Target
Vulnerabilities
Develop Text,
Images, Videos
Reuse Content
Create Search
Artifacts
Distort Facts
Generate Info
pollution
Create Inaunthentic
Groups and Sites
Create Fake
Accounts
Create Localized
Content
Create Clickbait
Post Content
Amplify Narratives
Comment or Reply
on Content
Deliver Ads
Incentivize
Sharing
Flooding the
Information Space
Harrass
A D V E R S A R Y  I N F L U E N C E  S T R A T E G I E S
P  R  E  P  A  R  E E  X  E  C  U  T  E
TACTIC
TACTIC
TACTIC
TACTIC TACTIC
TACTIC TACTIC
PHASE PHASE
TECHNIQUES
Fig. 1. Seven strategies based on DISARM techniques for influence operations in social networks
their universal applicability, while certain preparation and execution tactics are omitted as
they do not serve as clear preconditions for the seven execution techniques.
(3) Define influence strategies from resulting pipelines . The sequential flow from preparation to
execution forms structured activity pipelines, outlining influence patterns of threat actors.
Each colored pipeline is inductively named and defined as a high-level influence strategy.
Narrative Release. This strategy introduces a narrative into the social network that aligns with
the intended influence objective. The fundamental technique is posting content, which involves
publishing original posts or multimedia directly on social platforms. These posts can be text
updates, images, videos, or links. To enable the execution of this technique, adversaries must first
develop narratives from scratch, develop the textual or multimedia content, and localize artifacts to
ensure that messaging is culturally and linguistically adapted. For instance, an actor might post
a publication on a Facebook group to shape public perception of a controversial issue. The goal
is to establish an anchor point for influence, making the narrative recognizable and available for
reinforcement, expansion, or manipulation [38].
Narrative Support. Once a narrative is introduced, this strategy strengthens its credibility and
makes it more widely accepted. Adversaries rely on amplifying narratives to make posts appear
more popular than they naturally would be by leveraging existing narratives and reusing content.
A common example is the forced posting or interaction with a narrative to increase reliability
and engagement. The goal is to solidify public acceptance, making the narrative more resistant to
scrutiny or opposing views [5].
Narrative Amplification. This strategy focuses on expanding the reach and virality of a narrative. By
increasing exposure, the narrative appears more widespread and influential for a broader audience.
Adversaries increase content spread by sharing and incentivizing sharing, creating search artifacts
that optimize content for visibility on search engines and social platforms while designing clickbait
, Vol. 1, No. 1, Article . Publication date: February 2025.

Influence Operations in Social Networks 5
that exploits cognitive biases. For example, a well-crafted Instagram reel with provocative imagery
and a catchy caption can encourage mass sharing. The goal is to raise its visibility, making it harder
to ignore [20].
Counter-Narrative Reaction. Deployed in response to competing narratives, this strategy works
to challenge, weaken, or redirect attention from opposing perspectives. Influence actors rely on
commenting or replying on content to shape discussions and control narratives. By strategically
posting comments on public threads, they can reinforce messages, attack opposition, or create
the illusion of widespread support. To execute this, adversaries develop competing narratives that
counter opposition and distort facts to undermine credibility. This strategy is frequently used in
YouTube comment sections, where adversaries flood replies with endorsements or criticism to sway
public perception. The goal is to protect the dominant narrative, ensuring it remains the primary
frame of reference [21].
Narrative Manipulation. Rather than simply reinforcing or amplifying a message, this strategy
modifies, distorts, or falsifies existing narratives to reshape public perception. Adversaries use links,
news articles, or social media promotions to redirect users to manipulated external content through
delivering ads. This strategy is supported by leveraging conspiracy narratives, creating inauthentic
groups, and developing fake news sites as reference points for misleading claims. A Facebook ad
campaign, for instance, might target users with deceptive links to fabricated news articles tailored
to their biases. The goal is to redefine reality, aligning public perception with a preferred version of
events [32].
Target Degradation. This strategy seeks to discredit, intimidate, or silence individuals or groups
that challenge an influence operation. It diminishes their credibility with harassment, weakening
their influence, and discourages engagement to remove opposition from public debate. To prepare
for such actions, adversaries integrate target vulnerabilities, gathering intelligence on their targets
to personalize attacks. A common example is a Twitter harassment campaign targeting journalists
or political figures to discredit or silence them. The goal is to reduce the ability of key figures to
contest the dominant narrative [29].
Information Pollution. By overwhelming the information environment with excessive or conflicting
content, this strategy creates confusion and distrust in the reliability of information sources.
Adversaries can flood the information space , not necessarily promoting a particular narrative but
diluting clarity and credibility, flooding social networks with excessive content and making it
difficult for users to discern credible information. This execution technique requires generating an
excess of low-quality or misleading content and creating fake accounts to emit and amplify it. A
typical example involves posting hundreds of tweets quickly to saturate a conversation and obscure
opposing viewpoints. The goal is to increase uncertainty, leaving audiences more susceptible to
influence [26].
Overall, these strategies provide a generalized framework for understanding complex influence
operations in the real world, being correlated with other studies [6].
4 INFLUENCE OPERATIONS IN THE REAL-WORLD
The literature on cross-analysis of influence operations using a standardized framework remains
limited. However, over the past year, a dataset comprising 81 FIMI campaigns targeting elections
and referendums from 2014 to 2024 has been manually tagged using DISARM techniques by the
SIPA Institute of Global Politics (IGP) [ 15], leveraging intelligence reports. By identifying the
execution techniques employed in each incident, we can infer the overarching influence strategies
conceptualized in this work.
, Vol. 1, No. 1, Article . Publication date: February 2025.

6 Javier Pastor-Galindo, Pantaleone Nespoli, José A. Ruipérez-Valiente, and David Camacho
0
10
20
30
40
50
60
70
80 USAGE IN REAL -WORLD INCIDENTS
97.5%
66.2% 63.7%
48.8%
42.5%
32.5% 30.0%
78
53 51
39
34
26 24
INFLUENCE STRATEGIES
Narrative
Release
Narrative
Support
Narrative
Amplification
Counter -Narrative
Reaction
Narrative
Manipulation
Target
Degradation
Information
Pollution
Fig. 2. Prevalence of influence strategies in past incidents from 2014 to 2024
4.1 Prevalence of strategies in real influence operations
Out of the 81 documented incidents, 80 could be mapped to the influence strategies proposed in
this study. Most of them integrating more than one strategy. This indicates that our methodology
effectively captures the critical techniques within the complex DISARM framework. Figure 2 reveals
the usage of strategies by adversaries to influence social networks audience.
Among the identified strategies, Narrative Release emerges as the most prevalent, present in
97.5% of cases. This finding underscores the importance of content seeding as the foundation of
influence campaigns, where adversaries introduce new narratives, fabricate stories, or selectively
leak information to set the stage for broader manipulation efforts. Following closely, Narrative
Manipulation (66.2%) and Information Pollution (63.7%) highlight the widespread use of content
distortion. These strategies involve reshaping existing narratives, amplifying conspiracy theories,
or overwhelming audiences with misleading or conflicting information. Their prevalence suggests
that influence operations are not solely about creating falsehoods but also about controlling the
information environment to erode trust and manipulate perceptions. Narrative Support, observed in
48.8% of cases, plays a crucial role in reinforcing and sustaining the visibility of manipulated content.
Techniques such as coordinated engagement, automated amplification, and deceptive endorsements
ensure that seeded narratives gain traction and appear credible. Similarly, Narrative Amplification
(42.5%) extends the reach of influence campaigns by leveraging social media algorithms, influencers,
and mass-sharing tactics to maximize exposure. Less common but equally significant, Counter-
Narrative Reaction (32.5%) and Target Degradation (30.0%) represent more aggressive forms of
influence operations.
These findings highlight two key takeaways. First, influence operations extend beyond narrative
manipulation (e.g., disinformation), encompassing a broader manipulation of the information
ecosystem. Second, real campaigns rarely rely on a single strategy but rather combine them to
reinforce and amplify their impact, as inspected next.
, Vol. 1, No. 1, Article . Publication date: February 2025.

Influence Operations in Social Networks 7
Raw Co-Occurence Network
Absolute frequencies of strategy combinations
Conditional Probability Network
Likelihood of a strategy appearing given another
Narrative
Release
Narrative
Release
Narrative
Amplification
Information
Pollution
Narrative
Amplification
Information
Pollution
Narrative
Manipulation
Narrative
Manipulation
Counter-Narrative
Reaction
Counter-Narrative
Reaction
Narrative
Support
Target
Degradation
Narrative
Support
Target
Degradation
Fig. 3. Combination of influence strategies in past incidents from 2014 to 2024
4.2 Dominance of multi-strategy influence operations
The majority of influence actors (92.5%, 74 out of 80 cases) rely on multi-strategy operations,
rarely deploying a single approach in isolation. The most common tactic (33%, 24 cases) involves
orchestrating four strategies, balancing complexity and efficiency. More sophisticated adversaries
execute five-strategy operations (20%), while three-strategy combinations (19%) remain a flexible
option. Simpler two-strategy operations (15%) are uncommon, and more intricate campaigns
employing six or seven strategies (8% and 5%) are rare, likely due to coordination challenges.
From a total of 120 potential strategy combinations, about 30 distinct patterns emerge from the
dataset, revealing preferred multi-strategy playbooks in Figure 3. On the left, the co-occurrence
network illustrates how influence actors interweave different strategies to enhance their impact.
A tendency is observed among those who rely on Narrative Release as a core strategy, frequently
coupling it with Information Pollution and Narrative Manipulation to both introduce and distort
narratives while overwhelming the information space. This structured approach appears in seven
incidents. Additionally, some adversaries intensify their manipulation efforts by combiningInforma-
tion Pollution and Narrative Manipulation, flooding feeds with deceptive content while embedding
misleading elements into ongoing discussions. Many further reinforce these efforts by deploying
Narrative Amplification for wide spread, as observed in 11 cases where all four strategies were used
together. Other influence actors rely on Narrative Support to strengthen their operations, aligning
it with Narrative Release, Narrative Amplification, Information Pollution, and Narrative Manipulation
to consolidate a coherent influence strategy, appearing together in six operations. While this graph
provides insights into dominant playbooks, frequent pairings do not necessarily imply a strong
interdependence between strategies.
On the right, the conditional probability network reveals how likely influence actors are to
deploy one strategy given the presence of another, uncovering tactical dependencies in influence
operations. Two primary trends emerge. First, adversaries who launch Narrative Release often
combine with Target Degradation, Narrative Support, and Counter-Narrative Reaction, reinforcing
their narratives by undermining opposing voices and injecting reactionary content. Second, those
, Vol. 1, No. 1, Article . Publication date: February 2025.

8 Javier Pastor-Galindo, Pantaleone Nespoli, José A. Ruipérez-Valiente, and David Camacho
relying onInformation Pollution, Narrative Manipulation, andNarrative Amplificationtend to saturate
the information ecosystem with deceptive content, reinforcing misleading narratives through
coordinated amplification. Notably, Narrative Manipulation appears as a linchpin, frequently used
regardless of the strategic combination.
5 CONFRONTING DIGITAL MANIPULATION: STRATEGIC RESPONSES AND FUTURE
DIRECTIONS
The increasing automation and sophistication of influence operations are transforming them into a
persistent digital threat, where adversaries (often APM) deploy coordinated tactics to manipulate
narratives, erode trust, and exploit vulnerabilities across social networks [ 14]. This study has
identified and categorized key influence strategies in social networks, grounded in the DISARM
framework. We revealed the prevalence of those strategies through an analysis of 80 FIMI incidents.
The co-occurrence and conditional probability perspectives provide complementary insights into
how adversaries coordinate multiple strategies, where key narratives are not only introduced and
manipulated but also strategically reinforced through amplification and support mechanisms. This
analytical and structured approach based on observable strategies in social networks set the stage
for a proactive response, integrating cybersecurity methodologies, intelligence-sharing, real-time
situational awareness, and mitigation strategies [31].
One of the most promising countermeasures is the integration of Cyber Threat Intelligence (CTI)
into influence operation monitoring, allowing analysts to track adversarial tactics and coordinate
rapid responses using established intelligence-sharing platforms such as MISP and OpenCTI [37].
This structured approach treats disinformation as a cybersecurity threat, fostering real-time collab-
oration between governments, platforms, and security researchers. However, detection alone is
insufficient, and achieving Cyber Situational Awareness (CSA) in social networks is vital to under-
standing the broader manipulation landscape [10]. By combining OSINT, SIGINT, and HUMINT,
and applying AI-driven behavioral analytics, CSA frameworks can anticipate influence campaigns
before they escalate, shifting from reactive defense to proactive intervention.
Beyond intelligence and monitoring, risk assessment and mitigation must evolve to counter
systemic vulnerabilities [31]. Influence operations thrive on media manipulation and institutional
weaknesses, making adaptive counter-narratives and targeted disruption strategies essential. The
development of AI-driven realistic simulations provides an effective means to evaluate adversary
influence, model adversarial behavior, and refine response tactics [ 30]. These controlled envi-
ronments enable preemptive stress-testing of emerging disinformation strategies, ensuring that
countermeasures are validated before real-world deployment.
Yet, technical solutions alone cannot neutralize influence operations. Education and cognitive re-
silience remain central to long-term defense. Initiatives like NATO’s InfoRange and Red Team–Blue
Team exercises offer practical training in recognizing and countering manipulation tactics [31].
Widespread digital literacy programs are needed to prepare both practitioners and the public to
critically assess online content [37].
As Generative AI accelerates the automation of information manipulation, the need for cross-
disciplinary collaboration becomes more pressing [ 4]. The DISARM framework, serving as a
foundation for structuring adversarial influence operations in this work, must continuously adapt
to new deception techniques, AI-powered strategies, and cross-platform operations. The future
of influence operation mitigation will not rely on a single solution but on a resilient, adaptive
ecosystem of intelligence, technology, and education. By embracing this holistic, multi-domain
approach, researchers, policymakers, and cybersecurity experts can build more effective defenses
against the next generation of digital manipulation threats.
, Vol. 1, No. 1, Article . Publication date: February 2025.

Influence Operations in Social Networks 9
Acknowledgments
This study was partially funded by: (a) the strategic project “Development of Professionals and
Researchers in Cybersecurity, Cyberdefense and Data Science (CDL-TALENTUM)" from i) the
Spanish National Institute of Cybersecurity (INCIBE) and ii) by the Recovery, Transformation and
Resilience Plan, Next Generation EU; (b) by a “Juan de la Cierva” Postdoctoral Fellowship (JDC2023-
051658-I) funded by the i) Spanish Ministry of Science, Innovation and Universities (MCIU), ii) by
the Spanish State Research Agency (AEI/10.13039/501100011033) and iii) by the European Social
Fund Plus (FSE+); (c) by H2020 TMA-MSCA-DN TUAI project "Towards an Understanding of
Artificial Intelligence via a transparent, open and explainable perspective" (HORIZON-MSCA-2023-
DN-01-01, Grant agreement n º: 101168344); (d) by project PCI2022-134990-2 (MARTINI) of the
CHISTERA IV Cofund 2021 program; (e) by EMIF managed by the Calouste Gulbenkian Foundation,
in the project MuseAI; and by (f) Comunidad Autonoma de Madrid, and by CIRMA-CAM Project
(TEC-2024/COM-404).
References
[1] Meysam Alizadeh, Jacob N. Shapiro, Cody Buntain, and Joshua A. Tucker. 2020. Content-based features predict social
media influence operations. Science Advances 6, 30 (2020), 1–13. https://doi.org/10.1126/sciadv.abb5824
[2] ATHENEA Project. 2024. Policy Brief Conclusions and Recommendations from the ATHENA Project on Foreign
Information Manipulation and Interference. https://project-athena.eu/wp-content/uploads/2024/12/Policy-Brief-
ATHENA.pdf
[3] Arild Bergh. 2020. Understanding influence operations in social media. Journal of information warfare 19, 4 (2020),
110–131. https://www.jstor.org/stable/27033648
[4] Sam Blazek. 2021. SCOTCH: A framework for rapidly assessing influence operations. Atlantic Council (2021). https:
//www.atlanticcouncil.org/blogs/geotech-cues/scotch-a-framework-for-rapidly-assessing-influence-operations
[5] Joshua E Blumenstock, Guanghua Chi, and Xu Tan. 2025. Migration and the value of social networks. Review of
Economic Studies 92, 1 (2025), 97–128. https://doi.org/10.1093/restud/rdad113
[6] Ben Buchanan, Andrew Lohn, Micah Musser, and Katerina Sedova. 2021. Truth, lies, and automation. Center for
Security and Emerging technology 1, 1 (2021), 2.
[7] Ceren Budak, Brendan Nyhan, David M. Rothschild, Emily Thorson, and Duncan J. Watts. 2024. Misunderstanding the
harms of online misinformation. Nature 630, 8015 (2024), 45–53. https://doi.org/10.1038/s41586-024-07417-w
[8] Gonzalo Cánovas López de Molina, Felipe Sánchez González, Pantaleone Nespoli, Javier Pastor Galindo, and José A
Ruipérez Valiente. 2024. Analyzing frameworks to model disinformation attacks in online social networks. InProceedings
of the 9th National Conference on Cybersecurity Research (JNIC2024) . 92–99.
[9] Kathleen M Carley. 2020. Social cybersecurity: an emerging science. Computational and mathematical organization
theory 26, 4 (2020), 365–381. https://doi.org/10.1007/s10588-020-09322-9
[10] Danilo Cavaliere, Giuseppe Fenza, Domenico Furno, and Vincenzo Loia. 2024. A semantic model bridging DISARM
framework and Situation Awareness for disinformation Attacks Attribution. In 2024 IEEE Conference on Cognitive
and Computational Aspects of Situation Management (CogSIMA) . 55–62. https://doi.org/10.1109/CogSIMA61085.2024.
10553682
[11] Kevin C. Desouza, Atif Ahmad, Humza Naseer, and Munish Sharma. 2020. Weaponizing information systems for
political disruption: The Actor, Lever, Effects, and Response Taxonomy (ALERT). Computers & Security 88 (2020),
101606. https://doi.org/10.1016/j.cose.2019.101606
[12] European Union External Action. 2024. 2nd EEAS Report on Foreign Information Manipulation and Interference Threats .
Technical Report January. https://www.eeas.europa.eu/eeas/2nd-eeas-report-foreign-information-manipulation-and-
interference-threats_en
[13] European Union Agency for Network and Information Security. 2014. ENISA Threat Landscape 2024. Issue December.
https://www.enisa.europa.eu/publications/enisa-threat-landscape-2024
[14] Rolf Fredheim and James Pamment. 2024. Assessing the risks and opportunities posed by AI-enhanced influence
operations on social media. Place Branding and Public Diplomacy (2024), 1–8. https://doi.org/10.1057/s41254-023-
00322-5
[15] Margot Fulde-Hardy. 2024. Foreign Information Manipulation and Interference (FIMI) Activities Targeting Elections
(2014-2024): Presenting a dataset, a methodology, and a codebook to guide future applications of structured frameworks
enabling threat assessment . Technical Report. Working Paper. https://igp.sipa.columbia.edu/sites/igp/files/2024-
06/2024_06_07_FIMIElections_Margot_Fulde-Hardy_paper.pdf
, Vol. 1, No. 1, Article . Publication date: February 2025.

10 Javier Pastor-Galindo, Pantaleone Nespoli, José A. Ruipérez-Valiente, and David Camacho
[16] Nicholas A Gabriel, David A Broniatowski, and Neil F Johnson. 2023. Inductive detection of influence operations via
graph learning. Scientific Reports 13, 1 (2023), 22571. https://doi.org/10.1038/s41598-023-49676-z
[17] Josh A. Goldstein, Girish Sastry, Micah Musser, Renee DiResta, Matthew Gentzel, and Katerina Sedova. 2023.Generative
Language Models and Automated Influence Operations: Emerging Threats and Potential Mitigations . Technical Report.
OpenAI.
[18] Google Threat Intelligence Group. 2025. Adversarial Misuse of Generative AI . Technical Report. Google.
[19] Nicolas Hénin. 2023. FIMI: Towards a European Redefinition of Foreign Interference. EU DISINFO Lab 13 (2023), 2023.
[20] Kristina Hristakieva, Stefano Cresci, Giovanni Da San Martino, Mauro Conti, and Preslav Nakov. 2022. The spread of
propaganda by coordinated communities on social media. In Proceedings of the 14th ACM Web Science Conference 2022 .
191–201. https://doi.org/10.1145/3501247.3531543
[21] Johannes Kaiser, Cristian Vaccari, and Andrew Chadwick. 2022. Partisan blocking: Biased responses to shared
misinformation contribute to network polarization on social media. Journal of Communication 72, 2 (2022), 214–240.
https://doi.org/10.1093/joc/jqac002
[22] Microsoft. 2024. Microsoft Digital Defense Report 2024: The Foundations and New Frontiers of Cybersecurity . Technical
Report. Microsoft.
[23] Muhammad Shujaat Mirza, Labeeba Begum, Liang Niu, Sarah Pardo, Azza Abouzied, Paolo Papotti, and Christina
Pöpper. 2023. Tactics, Threats & Targets: Modeling Disinformation and its Mitigation. In NDSS. https://doi.org/10.
14722/ndss.2023.23657
[24] Ben Nimmo and Eric Hutchins. 2023. Phase-based tactical analysis of online operations . Technical Report. Carnegie
Endowment for International Peace. https://www.jstor.org/stable/resrep48480.7
[25] James Pamment. 2020. The EU’s Role in Fighting Disinformation: Crafting A Disinformation Framework . Carnegie
Endowment for International Peace. https://www.jstor.org/stable/resrep26180.1
[26] Yikang Pan, Liangming Pan, Wenhu Chen, Preslav Nakov, Min-Yen Kan, and William Wang. 2023. On the Risk of
Misinformation Pollution with Large Language Models. In Findings of the Association for Computational Linguistics:
EMNLP 2023, Houda Bouamor, Juan Pino, and Kalika Bali (Eds.). Association for Computational Linguistics, Singapore,
1389–1403. https://doi.org/10.18653/v1/2023.findings-emnlp.97
[27] Enzo Panizio. 2023. Disinformation narratives during the 2023 elections in Europe . Technical Report. European Digital
Media Observatory (EDMO). Issue November 2023. https://edmo.eu/publications/disinformation-narratives-during-
the-2023-elections-in-europe
[28] Javier Pastor-Galindo, Félix Gómez Mármol, and Gregorio Martínez Pérez. 2022. Profiling users and bots in Twitter
through social media analysis. Information Sciences 613 (2022), 161–183. https://doi.org/10.1016/j.ins.2022.09.046
[29] Javier Pastor-Galindo, Félix Gómez Mármol, and Gregorio Martínez Pérez. 2021. Nothing to Hide? On the Security and
Privacy Threats Beyond Open Data. IEEE Internet Computing 25, 4 (2021), 58–66. https://doi.org/10.1109/MIC.2021.
3088335
[30] Javier Pastor-Galindo, Pantaleone Nespoli, and José A. Ruipérez-Valiente. 2024. Large-Language-Model-Powered
Agent-Based Framework for Misinformation and Disinformation Research: Opportunities and Open Challenges. IEEE
Security & Privacy 22, 3 (2024), 24–36. https://doi.org/10.1109/MSEC.2024.3380511
[31] Christopher R. Walker, Sara-Jayne Terp, Pablo C. Breuer, and Courtney L. Crooks, PhD. 2019. Misinfosec: Applying
Information Security Paradigms to Misinformation Campaigns. (2019), 1026–1032. https://doi.org/10.1145/3308560.
3316742
[32] Zhiying Bella Ren, Andrew M Carton, Eugen Dimant, and Maurice E Schweitzer. 2022. Authoritarian leaders share
conspiracy theories to attack opponents, galvanize followers, shift blame, and undermine democratic institutions.
Current Opinion in Psychology 46 (2022), 101388. https://doi.org/10.1016/j.copsyc.2022.101388
[33] Krystyna Sikora and Bret Schafer. 2025. The State(s) of Foreign Information Operations. A State-by-State Look at
Foreign Information Manipulation in the United States . Technical Report. Alliance for Securing Democracy. https:
//securingdemocracy.gmfus.org/wp-content/uploads/2025/02/The-States-of-Foreign-Information-Operations.pdf
[34] Daniel R Sixto and Paul S Kim. 2023. Structured Process for Information Campaign Enhancement (SP!CE) 2.1 An Analytic
Framework, Knowledge Base, and Scoring Rubric for Operations in the Information Environment McLean, V A . Technical
Report 0704. https://apps.dtic.mil/sti/trecms/pdf/AD1214088.pdf
[35] Victoria Smith, Stephen Campbell, and Adam Maunder. 2024. A Comprehensive Review of DISARM Framework
and its Compatibility with Related Frameworks Used to Model Foreign Information Manipulation and Interference.
https://adacio.eu/disarm-august2024
[36] Sara-Jayne Terp and Pablo Breuer. 2022. Disarm: a framework for analysis of disinformation campaigns. In 2022
IEEE Conference on Cognitive and Computational Aspects of Situation Management (CogSIMA) . IEEE, 1–8. https:
//doi.org/10.1109/CogSIMA54611.2022.9830669
[37] The European Centre of Excellence for Countering Hybrid Threats (Hybrid CoE). 2022.Foreign information manipulation
and interference defence standards: Test for rapid adoption of the common language and framework ’DISARM’ The European
, Vol. 1, No. 1, Article . Publication date: February 2025.

Influence Operations in Social Networks 11
Centre of Excellence for Countering Hybrid Threats . https://www.hybridcoe.fi/wp-content/uploads/2022/11/20221129_
Hybrid_CoE_Research_Report_7_Disarm_WEB.pdf
[38] Andriy Tyushka. 2022. Weaponizing narrative: Russia contesting EUrope’s liberal identity, power and hegemony.
Journal of Contemporary European Studies 30, 1 (2022), 115–135. https://doi.org/10.1080/14782804.2021.1883561
Received 20 February 2007; revised 12 March 2009; accepted 5 June 2009
, Vol. 1, No. 1, Article . Publication date: February 2025.
