---
title: AI Governance through Markets
url: https://arxiv.org/abs/2501.17755
category: ai-marketing
subcategory: empirical
date: 2025-01
venue: ''
authors:
- Philip Moreira Tomei
- Rupal Jain
- Matija Franklin
source: arxiv
pdf_url: https://arxiv.org/pdf/2501.17755
pages: 35
chars: 118439
fetched_at: '2026-11-08T13:18:18+00:00'
kb_version: 1
---

# AI Governance through Markets

AI Governance through Markets
PHILIP MOREIRA TOMEI 1,2, RUPAL JAIN 2,3, MATIJA FRANKLIN 1,2,4, AI Objectives Institute 1, USA, The ML
Alignment & Theory Scholars (MATS) Program2, USA, Mercatus Center, George Mason University3, USA, and University College
London4, UK
This paper argues that market governance mechanisms should be considered a key approach in the governance
of artificial intelligence (AI), alongside traditional regulatory frameworks. While current governance approaches
predominantly focus on regulation, we contend that market-based mechanisms offer effective incentives for responsible
AI development. We examine four emerging vectors of market governance: insurance, auditing, procurement, and
due diligence, demonstrating how these mechanisms can affirm the relationship between AI risk and financial risk
while addressing capital allocation inefficiencies. While we do not claim that market forces alone can adequately
protect societal interests, we maintain that standardised AI disclosures and market mechanisms can create powerful
incentives for safe and responsible AI development. This paper urges regulators, economists, and machine learning
researchers to investigate and implement market-based approaches to AI governance.
Contents
Abstract 1
Contents 1
1 Overview 3
1.1 Governance Through Markets 3
1.2 AI Risk as Market Failure 5
2 Risk Distribution: Insurance 8
2.1 Case Study: Commercial Real Estate 9
3 Assurance: Auditing and certification 9
3.1 Case Study: Zoom Video Communications 10
4 Protocolisaton: Procurement Standards 10
4.1 Case Study: NASA Apollo Mission 12
5 Investor behaviour: Due Diligence 12
5.1 Case Study: BP Oil Spill 13
6 Standardised Information as a Foundation for Market-Based AI Governance 13
6.1 Disclosure Mitigates Information Asymmetry 14
7 Disclosing AI’s development and deployment 15
7.1 AI Disclosures 16
8 Discussion 20
Corresponding Author’s Contact Information: philip.tomei@aiobjectives.org.
© 2025
1
arXiv:2501.17755v2  [econ.GN]  5 Mar 2025

8.1 Intellectual Property and Disclosure: A Tradeoff 20
8.2 Market incentives for risk mitigation can unlock funding for safety research 20
8.3 Scala Politica: Tailoring Intervention to Size without stifling innovation 21
9 Conclusion 22
Acknowledgments 22
References 22
A AI Risk Standardisation Targets 27
A.1 Data Acquisition and Privacy in AI Systems 27
A.2 Energy: Data Centre Efficiency and Algorithm Design 28
A.3 Compute Allocation 28
A.4 Intended Model Behaviour 28
A.5 Model Interpretability 29
A.6 Open-source practices 29
A.7 Adversarial Testing 29
B Existing Disclosure Frameworks 30

1 Overview
The field of Artificial Intelligence (AI) governance has predominantly emphasised regulatory frameworks [ 7, 136, 143] and
international cooperation [21, 58] to address AI risk. Meanwhile, uncertainty regarding AI risks is a major barrier to widespread
enterprise adoption [88] [5]. Despite the economic benefits, organisations recognise AI risk as a business risk and lack the tools to
confidently address it [36]. Market governance approaches, such as insurance, auditing, procurement, and due diligence, can serve
to both mitigate AI risk and enable AI growth - aligning market forces with prosocial behaviour [150].
Market governance mechanisms are processes that structure economic behaviour by aligning financial incentives with desired
outcomes. By directing capital flows, they possess the distinct advantage of embedding their own enforcement and incentive
structures [32]. Regulatory initiatives for AI, on the other hand, have faced increasing criticism for being perceived as anti-
competitive [110] and anti-growth [167]. We contend that rational and responsible approaches to AI governance can align with
economic objectives. Policy interventions may prove instrumental in creating a robust market governance ecosystem [84].
Analysis of the market governance of AI opens up distinct opportunities for both public and private involvement. Mechanisms
such as insurance, auditing, due diligence, and procurement offer opportunities for both startups and large enterprises to capitalise
on the growing need for AI de-risking which is projected to reach a value of $276 billion by 2030 [164]. These mechanisms also
afford policymakers and quasi-regulatory entities—including industry consortia, trade associations, and standards organisations —
strategic pathways for market shaping. Through the deployment of incentive structures, subsidisation programs, public-private
collaborations, and standardisation frameworks, policymakers can leverage markets to govern artificial intelligence development
while advancing critical economic, technological, and societal imperatives.
1.1 Governance Through Markets
By market governance mechanisms, we refer to tools and processes that align financial incentives with desired social or economic
outcomes by structuring economic behaviour [ 140]. These mechanisms include (but are not limited to) insurance, auditing,
procurement practices, and due diligence - which in turn serve risk distribution, information discovery, protocolisation and capital
allocation. In the context of AI governance, market governance mechanisms aim to decrease AI risk by pricing, measuring and
mitigating the risk incurred in AI deployment and development. These mechanisms further enable public and private stakeholders
to shape AI in ways that align with broader societal and economic goals, fostering a balance between innovation and risk mitigation.
As Hadfield and Clark argue [62] AI fundamentally disrupts traditional regulatory frameworks in ways that demand comprehensive
reconsideration of our approach. Their analysis suggests that the primary challenge is not simply creating new rules for AI-
specific risks, but developing dynamic regulatory approaches that can adapt to AI’s pervasive influence. Their proposal for
regulatory markets can be seen as one possible structure within which market governance mechanisms can operate. Their example
demonstrates the broad array of policy strategies available towards market governance of AI, which can range from complete
self-governance to government mandates with punitive enforcement.
Market governance mechanisms often function as private regulators, for-profit and non- profit organizations that develop and
supply regulatory services, which compete to sell to targets, this is the case for instance with the protocol organisations and
assurance providers [107] we describe later. This is not necessarily always the case, due diligence and insurance have similar
effects but would not fall under this label.

Fig. 1. 4 AI market governance mechanisms.
It is important to note that AI Risk and its associated uncertainty are a major barrier to AI adoption across the economy [6, 106].
This is exemplified by how AI service providers have resorted to providing unlimited indemnities to maintain their sales volume
[26]. Market governance mechanisms work to reduce asymmetry and risk, enhancing the stability and efficiency of markets and

enabling adoption [82]. For example, insurance functions as market governance by facilitating the distribution and management
of uncertainty across a broad pool of market participants [86], thereby mitigating individual exposure to risk while promoting
resource allocation through the collective absorption of losses [16].
We do not believe the aforementioned four mechanisms to be exhaustive but rather exemplary of the kind of intervention points
which are able to work alongside market forces to govern AI. We wish to highlight the way markets are already governing AI
and widen the possibility space for AI governance research beyond hard regulation. Each of these mechanisms represents an
opportunity for both public and private interventions into the governance of AI backed by the power of markets.
1.2 AI Risk as Market Failure
The uncertainty around AI risk is a major barrier to enterprise adoption of AI technologies [5, 88]. Large enterprise customers are
uncertain about how to measure, mitigate and govern the risks posed by AI integration into their organisations [36]. Notwith-
standing its potential economic advantages, this issue persists as a significant impediment to the dissemination of AI technologies.
Consequently, organisations have already recognised that AI-related risks are synonymous with business risks, and are responding
in a manner that reflects this understanding. The awareness of these risks and the inability of organisations to address them
prevents firms and society at large from benefiting from AI technologies.
In this vein, we may understand the uncertainty around AI Risk and its mitigation as market failure. The failure, that is, to
measure and mitigate the private costs of AI development and deployment and price its externalities. By AI risk, we imply a risk
from the development and deployment of AI systems. This risk to the firm is magnified in how closely AI is being integrated
to value-generating and infrastructural operations. We use the following formula to quantify this risk-adjusted value [10] of AI
investments:
RAV =𝐸(𝑋)− 𝜆·𝜎(𝑋)
• RA V (Risk-Adjusted Value): The value of an outcome adjusted for risk, reflecting the market actor’s risk tolerance. It
represents the certainty-equivalent value of the expected return after accounting for the investor’s aversion to risk.
• 𝐸(𝑋) (Expected Value): The average projected financial return, calculated as the probability-weighted mean of all potential
outcomes. Here,𝐸(𝑋) reflects the private expected returns for a market actor and does not inherently account for externalities
unless they are explicitly included in the calculation.
• 𝜆 (Risk Aversion Coefficient) : A factor representing a market actor’s sensitivity to risk, where higher values denote a
stronger preference for certainty and a greater aversion to risk. It scales the impact of risk (as measured by 𝜎(𝑋)) on the
risk-adjusted value, personalising the adjustment based on individual or organizational risk preferences.
• 𝜎(𝑋) (Standard Deviation) : A measure of outcome variability, indicating the level of uncertainty or risk in financial
performance. It quantifies the dispersion of possible returns around the expected value𝐸(𝑋), serving as a proxy for risk or
volatility. A higher standard deviation signifies greater uncertainty and potential variability in returns.
This formula calculates a risk-adjusted value (RAV) by subtracting a risk penalty (𝜆·𝜎(𝑋)) from the expected value. While𝐸(𝑋)
represents the average projected return,𝜎(𝑋) quantifies the uncertainty or variability in potential outcomes. This separation

allows for a more nuanced adjustment that reflects an actor’s specific risk tolerance, represented by the coefficient 𝜆. Without this
adjustment, the model would not adequately account for individual or institutional preferences regarding risk.
Imagine𝐸(𝑋) as the expected winnings from a lottery, averaged across all possible outcomes. While this gives a sense of the
potential reward, it doesn’t reflect the variability between a jackpot and losing the ticket price.𝜎(𝑋) measures this variability,
and𝜆 adjusts for how much the individual dislikes the uncertainty of not knowing whether they’ll win or lose.𝜆 captures the
market actor’s sensitivity to uncertainty, and𝜎(𝑋) quantifies the variability in potential financial outcomes due to AI deployment.
The contour plot of RAV in Figure 1 provides a visual representation of how𝐸(𝑋) and𝜎(𝑋) influence the attractiveness of AI
investment projects under varying𝜆. In AI hype-cycles,𝜆 is low, thus resulting in investment with higher𝜎(𝑋) [25].
Behavioural factors also play a crucial role in the accurate assessment of AI investment risks [2]. During hype cycles surrounding
AI technologies, cognitive biases may lead firms to underestimate their risk-aversion coefficient (𝜆) or the variability of outcomes
(𝜎(𝑋)). This is marked by the financial underperformance of many AI investments to date. Thus, investment decisions are not
aligned with the market actor’s true risk tolerance [13, 128].
Furthermore, the RAV formula primarily focuses on financial variability and may overlook regulatory and ethical risks [19]. These
include potential costs from regulatory fines, legal liabilities, or ethical breaches—such as violations of data privacy laws, biased
decision-making algorithms, or unintended harmful consequences of AI deployment. Such risks are not always fully captured
by𝜎(𝑋) but can have substantial financial and reputational repercussions. Incorporating these factors into the risk assessment
framework is necessary to obtain a comprehensive understanding of the risks involved in AI investments [146].
Integrating the RAV formula into AI investment evaluations provides a structured approach to quantifying and managing the risks
associated with AI deployment. This methodology reinforces the importance of acknowledging both private costs and externalities,
leading to more responsible investment decisions. By properly accounting for the risk of AI development and employment, firms
can better align their strategies with their actual risk tolerance levels. This alignment ensures benefits for shareholders through
optimised financial performance and for stakeholders by mitigating negative societal impacts associated with AI technologies.

Fig. 2. Figure 1. D Scatter Plot of RAV as a Function of 𝐸(𝑋),𝜎(𝑋), and𝜆. This visualisation illustrates how varying each parameter affects the
RAV, with warmer colours indicating higher risk-adjusted values.
As seen in Figure 2, at lower values of𝜆, the Risk-Adjusted Value (RAV) closely aligns with the expected return𝐸(𝑋), as the risk
penalty is relatively small. This reflects scenarios where risk aversion is minimal and the primary focus is on maximising returns,
regardless of the associated volatility. Conversely, at higher values of𝜆, the risk term𝜆·𝜎(𝑋) becomes more influential in the
RAV calculation, causing RAV to decrease even when𝐸(𝑋) is large. In risk-tolerant scenarios, where𝜆 is small, investments or
decisions with higher volatility (𝜎(𝑋)) may still yield favourable RAVs if𝐸(𝑋) is sufficiently high to offset the modest risk penalty.
This interplay highlights the importance of calibrating𝜆 to reflect the appropriate level of risk tolerance for a given context.

2 Risk Distribution: Insurance
Insurance serves as an enabler of transactions amid radical uncertainty by transferring and mitigating risks associated with
unforeseen events [86]. In the context of deploying AI systems in economic functions, there is an unavoidable material financial
risk due to the probabilistic nature of modern AI models [56], as model outputs are undetermined by their inputs. As AI systems
become more complex, agentic, and autonomous, the potential for unintended consequences increases and so do prospective
financial losses.
Insurance can serve as a powerful governance mechanism, shaping responsible AI development and deployment. This can be
achieved through risk-based pricing, underwriting standards, and carefully crafted policy exclusions. It also offers potential tools
to address thorny liability issues surrounding AI, such as joint causation scenarios or damages caused by hacked AI systems. While
traditional insurance domains may exhibit relative stability, AI systems present uniquely complex risk profiles characterised by both
substantial magnitude and high variance, which are characteristics that traditionally catalyse insurance market development [94].
The convergence of high-stakes outcomes and inherent unpredictability in AI agent behavior creates natural market conditions for
novel insurance products, reflecting the insurance sector’s historical role in facilitating technological adoption through systematic
risk distribution.
Insurance has the potential to create a more favourable incentive structure by making practices such as “safety-washing” or
underestimating AI-related risks less appealing [ 160]. The rigour of actuarial assessments may engender an anti-speculative
framework for pricing AI development, curtailing so called ’AI Hype’ - much like it has done in other sectors, such as real estate in
climate-vulnerable areas [115]. By pricing, mitigating, and transferring risk, insurance can encourage more accurate assessment
and analysis of AI risk profiles. In so doing, the development of a robust AI insurance market may enable both first- and third-party
stakeholders to more accurately understand the risk profile of AI development.
Cyberrisk provides a crucial precedent for AI risk. This has emerged as the most pressing form of business risk, mirroring the
indispensability of software in every major enterprise [52]. Accordingly, he financial toll of cyberattacks swells by 15% annually
up to $23tn by 2027 [44]. Among numerous potential solutions to this pervasive insecurity, insurance offers some respite. A robust
cyber incident insurance market incentivises organisations to strengthen their cyber defences, ultimately reducing societal cyber
risk [101]. While still in its infancy, cyberrisk insurance has promoted accurate analysis and pricing of the risk landscape. It further
incentivises the adoption of cybersecurity measures by making plain the financial consequences incurred and reducing premiums
or disqualifying policyholders with insufficient security measures.
As AI becomes integrated into the value creation of major industries, AI insurance will be in increasing demand. Lior et al[95]
have emphasised the value of building upon existing insurance infrastructure rather than creating entirely new AI-specific policies,
given uncertainties in the field. AI will affect multiple lines of existing insurance, including Technology Errors and Omissions
(E&O)/Cyber Liability, Professional Liability, Media Liability, and Employment Practices Liability, among others, depending on the
specific use case of the AI [8]. The manner in which AI risk is incorporated into insurance frameworks has significant implications
for both insurers and policyholders, shaping the management of AI-related risks throughout the private sector.
Societal-scale AI incidents may prompt the development of a CAT-bond market, in order to transfer liability from the insurance
sector to capital markets. As systemic AI risk increases with adoption this may provide a key backstop for societal resilience.
Catastrophe bonds decrease insurers’ contributions to systemic risk by offloading liability to global capital markets, thus lowering

default risks and enhancing stability[168]. CAT bonds support faster economic recovery after disasters by providing rapid liquidity
and mitigating financial strain on issuers, as strongly supported by empirical studies [61]. As the Crowdstrike incident shows,
misalignment between parametric triggers and actual losses remains a significant cause of basis risk [49].
Despite these potential benefits, and a number of commercial AI Insurance ventures already underway [129], numerous issues still
arise in AI risk distribution. The opacity of many AI systems ("black box" characteristics) presents severe technical challenges in
vulnerability assessment. Furthermore, the widespread integration of shared AI components, particularly foundational model APIs,
creates potential cascading failures across industries, complicating the evaluation of systemic risks, a concern that is particularly
acute in high-stakes sectors such as finance and healthcare. Privacy risk assessment faces trade-offs between model accuracy and
data protection, compounded by legal ambiguity around PII classification - while current fairness metrics often misalign with legal
standards, increasing discrimination liability [129]. Intellectual property risk is similarly constrained by varying technical and
legal interpretations, while tort law uncertainty complicates risk assessment. As such, a number of regulatory, legal and scientific
innovations are still necessary for a robust AI risk market to develop.
2.1 Case Study: Commercial Real Estate
Commercial real estate (CRE) owners have faced increasing insurance premiums in recent years, prompting behaviour changes to
manage these rising costs. Insurance companies have raised their prices to reflect the heightened risks associated with properties
in high-risk areas, such as those prone to natural disasters [ 57]. In response, property owners updated valuations to reflect
accurate replacement costs, made significant property improvements (e.g., installing new roofs), and opted for higher or aggregate
deductibles to negotiate better rates. These improvements reduced the overall risk of property damage, which in turn lowered
the likelihood of claims. This demonstrates how a market mechanism—higher insurance premiums—successfully incentivised
risk-reducing behaviours, ultimately benefiting both insurers and property owners through reduced risk [ 27]. Additionally,
alternative risk transfer strategies, such as structured programs, provide fixed premiums for budget certainty. These actions helped
CRE owners reduce premiums and ensure greater financial stability [27, 57]. A market actor—a company—changed their behaviour
to reduce risk and secure better insurance premiums.
3 Assurance: Auditing and certification
Third-party auditing is an independent examination of a company’s financial statements, operations, or compliance by an external
auditor to ensure accuracy and adherence to established standards and regulations [ 90]. Certification often follows auditing,
serving as formal recognition that a company meets specific industry benchmarks or quality standards. These processes are
usually made public, creating incentives for companies to maintain high levels of transparency and integrity to build trust with
stakeholders, including investors, customers, and regulators. The public nature of auditing and certification encourages companies
to improve their practices and reduce risks, as failing to meet standards can lead to reputational damage or financial penalties.
Consequently, companies may change their behaviour by implementing stronger internal controls [90]
Audits, when viewed as market governance mechanisms, serve as tools that help regulate market behaviour by enhancing
transparency, accountability, and trust between market participants [ 130]. They play a crucial role in reducing information
asymmetry, as the US Chamber of Commerce [ 41] notes, reinforcing market confidence through reliable audits is critical for
encouraging long-term investment.

There is significant literature on AI Auditing. The motivation for Audits for this varies; some [ 14, 45] argue that auditing is
necessary for public safety, while others [98] further point towards keeping AI firms accountable to their own commitments.
As Manheim et al. note, findings from audits, when disclosed, provide regulators and the scientific community with critical
insights into system behaviours and limitations. This transparency supports regulatory initiatives and scientific advancements
by deepening the comprehension of system operations. Additionally, Auditing aids due diligence and procurement processes by
providing third-party verification to first-party claims.
Further, audit mechanisms facilitate the resolution of public disclosure trade-offs, while system opacity maximises security
at the expense of external oversight, comprehensive disclosure enhances scrutiny but risks exposing proprietary technology.
Audits potentially offer an intermediary solution, enabling independent risk assessment while maintaining security protocols
[145]. Successful audit completion enhances investor confidence and stakeholder trust, aligning institutional credibility with
demonstrated accountability measures.
[91] identify significant methodological concerns regarding research practices, particularly within private sector institutions, where
incentive structures favor reporting superior performance on machine learning benchmarks. Their documentation of 43 distinct
"questionable research practices"—actions that, while not constituting explicit research misconduct, materially misrepresent AI
system capabilities—underscores the critical role of audit procedures in ensuring disclosure integrity and accuracy in AI system
evaluation.
3.1 Case Study: Zoom Video Communications
Following its initial public offering, Zoom Video Communications, Inc. encountered intensified examination regarding security
vulnerabilities within its telecommunications infrastructure, particularly during the unprecedented utilisation surge accompanying
the COVID-19 pandemic [ 112]. Suboptimal encryption protocols and potential unauthorised data access vectors presented
significant risks to stakeholder confidence and institutional reputation [66].
In response, Zoom implemented comprehensive third-party audit and risk management protocols, engaging cybersecurity
firms—notably Trail of Bits and NCC Group—to conduct thorough security assessments. These evaluations facilitated substantial
enhancement of security infrastructure, including the implementation of universal end-to-end encryption protocols, materially
improving service security parameters [89]. This case study exemplifies the efficacy of third-party audits as market governance
mechanisms for risk identification and mitigation.
4 Protocolisaton: Procurement Standards
Current procurement standards for AI systems are evolving to address challenges of safety, transparency, accountability, and
security. Governments often rely on private contractors for AI development, necessitating careful planning during procurement to
ensure transparency and compliance with norms [40]. Guidelines for AI procurement are being developed to support decision-
makers in identifying key elements for secure AI systems, considering technical and regulatory environments [85]. There is a
particularly urgent demand for AI-specific public procurement standards outside of the defence industry[72]. Private organisations
are further developing AI procurement standards, but concerns remain regarding liability and the need for internal governance
frameworks [106, 116].

The U.S. military, as the world’s largest single customer, has an annual budget of $916 billion [155], surpassing the total expenditures
of most nation-states. This substantial spending is governed by stringent procurement standards, which, in turn, influence the
behaviour of commercial suppliers seeking to secure highly lucrative government contracts [105]. Procurement standards, whether
set by governmental bodies or large private entities and consortia, play a crucial role in shaping customer demand and, by extension,
the development of products and technologies.
These guidelines and principles function as bottom-up market governance mechanisms that effectively regulate industries while
driving innovation [35]. In the defence sector, procurement standards such as the Defense Federal Acquisition Regulation Supple-
ment (DFARS) impose stringent requirements on suppliers, affecting not only contract eligibility but also driving technological
innovation and quality improvements [144]. The Department of Defense, governed by the Federal Acquisition Regulation (FAR)
and DFARS, enforces safety, performance, and reporting requirements [39]. They dictate the evolving technological and operational
standards for defence contractors, from the initial design phase through development, testing, and final delivery to meet the
evolving needs of the military, thereby indirectly promoting advancements in technology while imposing strict reliability thresholds
[54]. We must note however that the substantial resources required for regulatory compliance create barriers to entry, potentially
diminishing market competition [100]. Moreover, the transnational nature of these procurement standards manifests in their
influence on international suppliers, who must conform to these regulatory requirements to participate in the U.S. defense market,
effectively establishing global procurement paradigms [142].
In the commercial sector, multinational corporations such as Walmart and Apple implement procurement protocols that significantly
influence supplier practices across multiple domains, including labour conditions, environmental sustainability metrics, and product
quality specifications, thereby exercising considerable authority over global supply chain architectures [55]. This phenomenon
exemplifies how procurement standards transcend their conventional role as mere operational guidelines to function as instrumental
mechanisms in shaping industry practices, driving innovation trajectories, and establishing de-facto regulatory frameworks.
Pre-market testing standards, such as the FDA’s 510(k) Premarket Notification process, offer a compelling parallel for how large-scale
buyers can use their purchasing power to shape the trajectory of AI development. Just as the 510(k) process expedites regulatory
approval for medical devices that demonstrates substantial equivalence to another legally U.S. marketed device, procurement
standards for AI could require companies to meet predefined risk assessment benchmarks in order to reduce the friction of entering
into new lucrative markets and procurement contracts. This would incentivise a minimum level of efficacy and safety while also
fostering innovation within a controlled framework. In the downstream, this may harmonise high AI standards across borders as
well. In addition, pre-market testing standards typically come with public accountability measures, including the obligation to
report adverse events or safety concerns post-market. Such transparency creates a feedback loop, encouraging developers to be
proactive in mitigating risks while under the scrutiny of investors, regulators, and the public – as discussed further in the section
on “AI disclosures. ”
The U.S. The Department of Defense’s Cybersecurity Maturity Model Certification (CMMC) exemplifies existing technical safety
standards for AI, delineating three-tiered cybersecurity requirements—basic protection, Controlled Unclassified Information (CUI)
safeguards, and advanced threat mitigation—with mandatory compliance verification. This framework can inform the development
of comprehensive AI procurement standards. However, the establishment of universally applicable AI safety and reliability metrics
is imperative for practical implementation.

4.1 Case Study: NASA Apollo Mission
The National Aeronautics and Space Administration’s (NASA) Apollo Programme (1960s-1970s) exemplifies how rigorous procure-
ment protocols can facilitate the successful execution of complex, high-risk initiatives [48]. This program substantially enhanced
both private sector competition and aerospace technological reliability while maintaining safety parameters in mission-critical
contexts [152].
NASA’s procurement framework is structured upon the Federal Acquisition Regulation (FAR) and its organisational supplement,
the NASA FAR Supplement (NFS). These regulatory mechanisms are specifically designed to address the distinctive requirements
of space exploration, encompassing stringent reliability metrics, safety protocols, and performance criteria [104]. NASA’s uncom-
promising adherence to safety protocols, precision requirements, and performance criteria necessitates enhanced capabilities
among contractors [9].
These protocols catalysed technological innovations that would establish industry benchmarks for subsequent decades, encompass-
ing advancements in propulsion systems, microelectronic components, computational software, materials engineering, navigational
systems, and solar energy technology—innovations that were subsequently adapted for civilian applications [114]. Contemporary
commercial aviation and aerospace enterprises, including SpaceX and the Boeing Company, maintain comparably stringent safety
protocols per NFS procurement standards [3].
5 Investor behaviour: Due Diligence
Investor due diligence refers to a comprehensive appraisal conducted by investors to assess the potential risks and rewards
associated with an investment opportunity. This process involves a systematic evaluation of financial statements, management
competency, market conditions, and regulatory compliance [151]. For economists, due diligence plays a pivotal role in addressing
information asymmetry—the imbalance of information between corporate insiders and external investors—which can lead to
suboptimal investment decisions and market inefficiencies [113]. For investors, the ‘the goal of due diligence is to make the buyer
comfortable enough to go through with the deal’ [151].
Investor due diligence mitigates information asymmetry by enabling investors to obtain and analyse information that may not be
readily apparent from public disclosures [34]. This process encourages issuers to maintain accurate and comprehensive records,
knowing that sophisticated investors will scrutinise their disclosures. Thus, due diligence acts as a self-regulating mechanism that
complements formal regulatory frameworks [34].
Due diligence is not a monolithic process but rather a multifaceted approach which includes:
• Financial Due Diligence: This involves scrutinising financial statements, cash flow projections, debt obligations, and tax
liabilities. In the context of AI, this extends to evaluating the financial implications of AI investments and their potential
returns [74].
• Legal Due Diligence: Examining contracts, intellectual property rights, pending litigation, and regulatory compliance. With
AI, this includes assessing algorithmic bias, regulatory compliance, and potential liability issues arising from AI decision-making
[74].

• Operational Due Diligence: Evaluating business processes, supply chain efficiency, and operational risks. In AI-driven
companies, this includes assessing the robustness of risk management, development cycles and cybersecurity practices [65]
• Technical Due Diligence: For tech companies, this involves evaluating the underlying technology, its uniqueness, and its
potential for obsolescence. In the AI context, this becomes even more critical, requiring specialised expertise to assess AI
models, data quality, and algorithmic performance [65].
• Market Due Diligence: Analysing market size, growth potential, competitive landscape, and customer base. With AI,
this extends to evaluating the potential disruptive impact of AI technologies on existing markets, harnessing standardised
disclosures to compare AI integrations across competing firms [74].
The analysis that arises in due diligence helps in accurately pricing securities, reflecting all available information. Its governance
ability lies in being the determinant process by which investors allocate capital. In so doing, it incentivises management practices
and accountability within firms [141] and shapes competitive dynamics between firms. It is important to note that during the due
diligence process, buyers are not solely focused on identifying potential risks. Equally important to investors is the evaluation of
the enterprise’s strengths and opportunities. Thus, due diligence is both a carrot and a stick, rewarding those organisations that
present the least risk for investors while promising attractive returns [75].
Significant uncertainty exists regarding around the financial risk of firms with high levels of AI adoption [6]. Due diligence can
help scrutinise AI practices, in doing so investors help establish market norms for transparency in AI development. Companies are
further incentivised to maintain high standards in operational practices and regulatory compliance, knowing that investors pay
close attention to these aspects during the due diligence process [22].
5.1 Case Study: BP Oil Spill
The 2010 BP Deepwater Horizon incident, resulting in the discharge of approximately 4.9 million barrels of oil into the Gulf of
Mexico, represents the most extensive marine oil spill in recorded history [121]. Beythe catastrophic environmental and economic
implications, BP incurred $65 billion in remediation costs and legal settlements (United States Environmental Protection Agency,
2024). The financial impact was equally significant: BP’s market capitalisation decreased by $105 billion, representing a 55% decline
in equity value [64].
While operational safety deficiencies and insufficient corporate oversight precipitated the disaster, subsequent investor due
diligence proved instrumental in risk mitigation and catalysed substantial improvements in corporate governance and safety
protocols [69]. Investor pressure compelled comprehensive disclosure of financial liabilities and risk exposure, both immediate and
long-term. Consequently, BP allocated $5 billion annually toward transitioning from high-risk hydrocarbon operations to renewable
energy technologies, demonstrating how due diligence can facilitate strategic reorientation toward sustainable development [172].
This case study illustrates how investor-mandated audit reports and enhanced disclosure requirements, particularly regarding
high-risk applications, can fundamentally reshape corporate risk management strategies.
6 Standardised Information as a Foundation for Market-Based AI Governance
Asymmetry exists between the knowledge held by AI providers and rs and the broader market—including investors, insurers,
and procurers. Additionally, substantial uncertainty exists for all market participants regarding AI systems[6]. Without adequate

information, markets are unable to make informed decisions [68]. This information asymmetry and uncertainty, may be preventing
firms from effectively allocating resources to AI [6].
All the market governance mechanisms we examine—including insurance providers, procurement entities, and due diligence
evaluators—necessitate accurate and reliable data regarding artificial intelligence systems to effectively price AI assets, evaluate
associated risks, and facilitate implementation protocols. These stakeholders require comprehensive information to ensure
compliance with relevant standards, conduct thorough risk assessments, and optimise asset allocation decisions. We posit that the
convergence of these requirements would be optimally addressed through the implementation of standardised disclosure.
Standardisation of this kind in technology markets often reduces transaction costs, drives competition on value and reduces
externalities [? ]. Systematic disclosure could foster a robust epistemological foundation that enhances market participants’
decision-making capabilities, ultimately enabling more efficient capital allocation and minimising societal risks associated with AI
deployment [? ].
6.1 Disclosure Mitigates Information Asymmetry
Information asymmetry significantly impacts investors’ perceptions of novel technological implementation. It can result in both the
underestimation and overestimation of𝜆. In the former, market actors with less information on a technology might underestimate
their aversion, acting as if they are more willing to accept financial risk. The risk aversion coefficient𝜆 varies with the degree of
information asymmetry𝐼:
𝜆(𝐼) =𝜆0·𝑒𝑠𝜆·𝐼
• 𝜆0: The baseline risk aversion coefficient when information asymmetry is zero (𝐼 = 0). This represents investors’ standard
level of risk aversion under conditions of full transparency.
• 𝑠𝜆: The sensitivity parameter indicating how the risk aversion coefficient𝜆 responds to changes in information asymmetry
𝐼. The sign and magnitude of𝑠𝜆 determine the nature and extent of this response:
– If𝑠𝜆 > 0: The risk aversion coefficient 𝜆 increases exponentially with increasing 𝐼. This means that as information
asymmetry grows, investors perceive higher uncertainty and become more risk-averse. They may overestimate their
actual risk aversion, acting more cautiously than necessary due to the lack of information.
– If𝑠𝜆 < 0: The risk aversion coefficient 𝜆 decreases exponentially with increasing 𝐼. In this scenario, as information
asymmetry increases, investors perceive themselves as less risk-averse, potentially underestimating their true risk
aversion. This can lead them to take on excessive risk, possibly due to overconfidence or underappreciation of the unknown
risks.
By incorporating information asymmetry into the risk aversion coefficient, we can model how varying levels of transparency
affect investment decisions. The sensitivity parameter 𝑠𝜆 quantifies the impact of information asymmetry on investors’ risk
preferences. A positive𝑠𝜆 suggests that increased information asymmetry leads to higher perceived risk aversion, potentially
resulting in underinvestment due to overestimated risks. Conversely, a negative𝑠𝜆 indicates that higher information asymmetry
causes investors to act less risk-averse than they actually are, possibly leading to overinvestment in risky AI projects.

Fig. 3. Effect of Information Asymmetry on Risk Aversion Coefficient 𝜆(𝐼). The graph illustrates how𝜆(𝐼) varies with information asymmetry𝐼
for𝑠𝜆 =−0.5 (Underestimation of Risk Aversion) and𝑠𝜆 =+0.5 (Overestimation of Risk Aversion).
7 Disclosing AI’s development and deployment
Disclosure refers to the process of releasing all relevant information pertaining to a company. It is the foundation of the afore-
mentioned market governance mechanisms as disclosure powers auditing, insurance, due-diligence and procurement. Disclosure
can be financial or non-financial [ 111, 163]. Central to financial disclosures are financial statements—comprising the balance
sheet, income statement, and cash flow statement—which collectively provide insights into a firm’s financial position, operational
performance, and liquidity [67]. Non-financial reporting encompasses the disclosure of a company’s operations, business risks,
and corporate strategies that are not captured in traditional financial statements [161].
Most non-financial disclosures are not obligatory, yet 1,395 investors, who collectively manage $59 trillion—accounting for 60% of
global assets under management—have endorsed the UN Principles of Responsible Investment [12]. This endorsement signifies
a commitment to, among other considerations, take non-financial disclosures into account when making investment decisions.
Some funds will include or exclude potential investments on the basis of their non-financial information thus creating a strong
incentive [33, 38]. There is also large investor demand for non-financial disclosure [158]. For example, it is common for investors

to prefer funds that do not invest in companies providing services to the military [154]. Instances of widespread, non-financial
disclosures encompass research and development (R&D) information [87], sustainability reports [138], and organisational practices
[11]. Crucial for our purposes, nonfinancial disclosures provide market actors with information on potential risks that may not be
immediately apparent in financial statements [50, 126].
7.1 AI Disclosures
Standardisation serves to simplify complex risk areas, rendering them accessible to a broad range of market participants who
may lack expertise in AI. By adopting a common framework, AI risks can be articulated in a manner that facilitates more
informed decision-making across investment, insurance, and procurement activities. The absence of a standardised approach to
reporting AI-related risks introduces significant challenges for investors, insurers, and other stakeholders. Without uniform metrics,
assessing the financial and operational implications of AI risks becomes difficult, resulting in inefficiencies in capital allocation
and decision-making processes. A standardised risk framework is essential, as it provides consistent and comprehensible metrics
for communicating complex AI risks to non-specialists within the market. While such frameworks may not fully capture the
intricacies of each risk, they serve as a practical means of ensuring that AI-related concerns can be communicated and addressed
effectively.
We argue that the AI research communities can contribute to AI governance by standardising the disclosure of AI. This standardis-
ation requires the consistent description and quantification of key aspects of AI systems to enable firms, policymakers, and other
actors to make informed decisions.
Providers, such as developers of foundational general-purpose AI systems like GPT-4o, create the underlying models, while
distributors use these models to offer products, such as ChatGPT [60]. A growing community of researchers in academia, civil
society, government, and industry is actively studying the risks associated with AI. These risks are not always negative, but rather
descriptions of various features of the AI models and organisations that develop or distribute them that are currently uncertain.
These risks are increasingly communicated through various market governance mechanisms. For instance, organisations such
as METR, which function as safety auditors, evaluate the risk profiles of companies such as Anthropic or OpenAI [1]. Over this
decade, the standardisation of how AI-related information is transmitted through markets will likely solidify, much as we already
see with performance benchmarks such as GPQA [131], MATH [71], and MMLU [70] being widely adopted by companies like
OpenAI, DeepMind, and Anthropic.
In a competitive environment, the pressure to reduce risk becomes even more pronounced. AI companies that successfully minimise
risk can gain a competitive edge by attracting capital, securing better terms, and winning more procurement contracts. This
competitive advantage can create a virtuous cycle where reducing risk not only enhances a company’s market position but also
encourages industry-wide adoption of safer practices. As competitors observe the benefits of risk reduction, they too will be
motivated to improve their risk profiles, leading to a broader industry shift towards safer AI development and deployment.
By establishing clear guidelines for describing risks— such as the allocation of compute, incident reporting, and capabilities in
various areas—organisations can provide a comprehensive view of their AI models’ vulnerabilities and limitations. This would be
paired with specific metrics to quantify these risks, such as model error rates, data privacy breach incidents, or energy consumption
during model training and deployment. Such quantification enables stakeholders to make informed comparisons between different

AI systems and providers. With standardised reporting, market actors can assess AI risks more accurately, reducing uncertainty
and promoting better capital allocation.
The aforementioned market governance mechanisms require a framework for AI disclosure that identifies different sources of risk.
To disclose requires an understanding of the different areas that are present in the development and deployment of AI, as well as
in the organisations that develop and deploy. For example, OpenAI’s preparedness framework identifies categories such as: 1)
Individualised persuasion, 2) Cybersecurity, 3) Chemical, biological, radiological, and nuclear threats, and Autonomous replication
and adaptation [118]. Many other such frameworks exist, with the AI Risk Repository capturing 700+ risks extracted from 43
existing frameworks [149]. As such, this present paper will not be providing an exhaustive literature review of different AI Risks.
For the purpose of standardizing AI Risk disclosure, two critical aspects must be emphasized. First, Risk should not be construed as
inherently negative but rather as associated with uncertainty. A risk area is an area of uncertainty. Second, the way in which
different aspects of AI are disclosed needs to be standardised in order for them to be utilised by and communicated between
different market actors. This involves turning a complex nuanced area into a single metric or groups of metrics [ 157]. Some
standardised metrics have already emerged, such as the size of models expressed with floating-point operations per second (FLOPS)
[23], and the generalised capability of AI being regularly disclosed with famous benchmarks such as GPQA, MMLU and MATH
[70, 71, 131]. More metrics will be needed in order to fully describe the vast range of potential applications of AI.
Fig. 4. The 6 macro stages of the large AI model production line. This is a simplified overview. Other stages are described in the article text. This is
not a comprehensive overview of large AI model development.

Standardised metrics of AI risk will describe different aspects of AI development and deployment. The development of large
models—encompassing large language models, reasoning models, multimodal models, and other advanced AI systems—follows
a production pipeline with clearly delineated stages, each of which plays a critical role in shaping the model’s capabilities (See
Figure 4) [43]. The process initiates with data acquisition, where diverse datasets are curated and selected, which are subsequently
subjected to tokenisation and preprocessing [96]. Pre-training follows, where models are exposed to extensive datasets, learning
foundational patterns [42]. It is succeeded by mid-training, a phase that includes fine-tuning for specific tasks, domain adaptation,
and multi-task learning [122]. Post-training includes reinforcement learning from human feedback (RLHF) and other techniques,
as well as additional safety work such as audits, red-teaming, and capability enhancement like teaching tool use [102, 120, 166].
Upon completing these stages, models are prepared for productisation, where they are optimised for deployment environments,
such as through quantisation or distillation to reduce computational load [153, 165]. Deployment involves integrating models into
production systems, accompanied by continuous monitoring to track performance and detect issues like data drift [79].
Within this production pipeline, a number of aspects are of material significance to market participants, including investors,
regulators, and insurers. A detailed understanding of the risks, methodologies, and safeguards associated with each stage is essential
for accurately assessing the potential returns and liabilities inherent in the development of large models. Enhanced transparency
throughout these processes can facilitate improved risk assessment, inform capital allocation decisions, and ensure compliance
with regulatory frameworks, thereby supporting models that meet stringent safety, ethical, and performance benchmarks.
Table 1 outlines some standardisation targets that are anticipated to become prevalent across various stages of the large model
production process (See Appendix for a more detailed description of each standardisation target). Companies are already disclosing
some of these metrics. These projections are grounded in current regulatory requirements, industry best practices, and emergent
trends in AI governance. It is important to note that this is not an exhaustive inventory. Future research should extend this,
providing a more comprehensive perspective on the requisite standards for developing responsible and market-aligned models.

Risk Area Description Standardisation Target
Data Acquisition and Pri-
vacy in AI Systems
Diverse datasets are built by scraping,
buying, or making data. This involves
data curation (e.g., filtering out low-
quality or biased data) [96].
Data provenance, detailing the
sources and methods of data col-
lection—whether through scraping,
crowdsourcing, or third-party pur-
chases—and providing transparency on
labelling practices [20, 47, 53].
Energy: Data Centre Effi-
ciency and Algorithm De-
sign
Large AI models have large energy de-
mands, driving the need for energy-
efficient infrastructure and algorithms
[24, 83, 108, 109, 123, 171].
Energy consumption metrics like Power
Usage Effectiveness (PUE), the propor-
tion of energy derived from renewable
sources, the energy sources they use,
training methods reducing computa-
tional burden [80].
Compute Allocation Allocation of compute resources to the
training processes and the safety mea-
sures applied throughout AI model de-
velopment [43, 96].
Disclosing the quarterly compute spend
on pre-training, mid-training, post-
training, safety work, and inference.
Intended Model Behaviour Large model developers shape their
model’s behaviour through techniques
such as RLHF [120], Direct Preference
Optimisation (DPO) [127], fine-tuning
[122], red-teaming [102], and output fil-
ters [92].
Report the intended model behaviours,
and the methods and processes that
are being employed to achieve these in-
tended behaviours. The OpenAI Model
Spec provides a strong example of trans-
parency in this area [119].
Model Interpretability Model interpretability involves meth-
ods, such as Explainable AI [93] and
Mechanistic Interpretability [28], that en-
hance the transparency and understand-
ing of AI systems [59].
Interpretability techniques, model ar-
chitecture, identified biases, Foundation
Model Transparency Index [17].
Open-source practices Open-source practices in AI develop-
ment allow developers to share code,
datasets, and methodologies [148].
Documentation of open-source contri-
butions, including code, datasets, and
methodologies. Disclosing incidences
of potential dual-use cases, governance
structures for contributions and policies
for IP rights and licensing.
Adversarial Testing Adversarial testing assesses the re-
silience of AI systems by exposing them
to challenging inputs designed to ex-
ploit vulnerabilities [63, 137].
Detailing adversarial risks identified
during testing, reporting the scale, fre-
quency, and outcomes of these tests, as
well as the data sources.
Table 1. Risk Areas and Standardisation Targets

8 Discussion
8.1 Intellectual Property and Disclosure: A Tradeoff
Artificial intelligence enterprises maintain substantial opacity regarding their operational processes, a phenomenon particularly
pronounced in the semiconductor sector where competitive pressures and industrial espionage present significant concerns
[29]. However, empirical evidence suggests the possibility of achieving equilibrium between transparency and proprietary
protection. Patent systems exemplify such balanced disclosure mechanisms [78]. Standardised globally, patent legislation mandates
comprehensive technical documentation of innovations, ensuring replicability by qualified practitioners, as codified in Article
83 of the European Patent Convention. This reciprocal arrangement confers temporary market exclusivity in exchange for the
dissemination of public knowledge.
The pharmaceutical industry provides an instructive paradigm for managing the tension between disclosure requirements and
intellectual property protection. Global pharmaceutical research and development expenditure exceeded $300 billion in 2023,
representing significant growth from $5 billion in 1980 and $38 billion in 2000 [134]. Leading pharmaceutical corporations, including
Merck, Novartis, and Roche, maintain substantial R&D investment ratios, ranging from 27% to 50% of revenue [133]. Their disclosure
protocols prioritise methodological transparency over proprietary formulations [37], encompassing clinical trial methodologies,
regulatory milestones, development timelines, R&D intensity metrics, and scientific uncertainties, while maintaining competitive
advantages through strategic patent protection [117]. This disclosure framework enables investors to assess future profitability
while establishing realistic expectations. The model has facilitated substantial capital attraction despite inherent developmental
risks, supported by the potential for significant long-term revenue from successful therapeutic interventions.
The pharmaceutical sector’s approach offers valuable insights for AI disclosure frameworks [159]. Strategic transparency—encompassing
risk categorization, regulatory compliance milestones, and mitigation protocols—can be achieved without compromising pro-
prietary algorithms. This methodology, focusing on process disclosure rather than technical specifications, effectively balances
regulatory compliance, investment attraction, and stakeholder trust. Thus, AI disclosure requirements may be reconceptualised as
strategic opportunities rather than regulatory burdens.
8.2 Market incentives for risk mitigation can unlock funding for safety research
The scale of global asset management presents significant potential for influencing artificial intelligence development trajectories.
Current market data indicates substantial capital pools: hedge funds manage approximately $5 trillion, private equity firms control
$5 trillion, sovereign wealth funds oversee $11 trillion globally, while U.S. pension funds alone manage approximately $12 trillion
in assets [139, 169, 170]. If even 1% of assets under management incentivise responsible AI initiatives, this could could mobilise
approximately $330 billion—a sum that exceeds current philanthropic contributions to AI safety by several orders of magnitude, as
exemplified by Open Philanthropy’s $46 million allocation in 2023 [103]. Although not comparable, redeployment of this kind
could fundamentally transform the AI safety and security landscape, enabling expanded research initiatives, enhanced compliance
frameworks, and accelerated development in interpretability and model safety protocols.
This potential capital reallocation can be contextualised against ESG mandates, where projections indicate asset managers will
oversee $33.9 trillion in ESG-focused funds by 2026 [132]. This precedent demonstrates institutional investors’ capacity to integrate

non-traditional criteria into investment decisions, despite uncertainty regarding ESG’s correlation with financial returns. Crucially,
the primary critique of ESG funds lies in their inconsistent metrics and lack of standardisation, which undermines comparability
and transparency across firms and industries. This results in fostering superficial compliance practices, such as greenwashing,
rather than driving substantive improvements in sustainability or ethical governance. Our argument for a standardised disclosure
framework seeks to avoid an equivalent "safety washing". Further, the more direct financial implications of AI-related risks
may present even more compelling incentives for institutional investors. Thus, strategic influence on capital flows could create
substantial financial incentives for responsible AI development on a global scale.
8.3 Scala Politica: Tailoring Intervention to Size without stifling innovation
Disclosing information about AI Risk is a type of intervention, and to be effective every intervention must be tailored to the size
of the entity that it is being applied to. Interventions applied to a country, may not apply to a city, and vice versa. Unwanted
outcomes occur when an intervention designed for an entity of a certain scale, is applied to an entity of a different scale [156]. The
same can be said for the difference between the disclosure standards applied to startups and large organisations.
The interconnected nature of market actors can create cascading effects throughout the market ecosystem. Institutional investors,
particularly private equity firms managing pension fund portfolios, demonstrate how modifications in compliance expectations at
upper market echelons can fundamentally reshape capital allocation patterns throughout the investment hierarchy. The dramatic
473.5% increase in Fortune 500 companies identifying AI-related risks underscores this growing concern [ 51]. Conservative
projections suggest that AI-related incidents resulting in merely a 2% devaluation—whether through market capitalisation decline,
regulatory penalties, or customer attrition—could precipitate substantial financial implications, given the magnitude of capital
exposed.
However, startups have a starkly different landscape. The financial scale disparity between Fortune 500 corporations and venture
capital markets is substantial, with the former generating collective revenues exceeding $18 trillion in 2023, while venture
capital investments totalled approximately $394 billion in 2022, declining from a peak of $611 billion in 2021 [77]. Owing to the
complexities inherent in AI supply chains, there are financial interdependencies between emergent enterprises and established
corporations [18]. Major corporations, notably cloud service providers, often mitigate the risks that startups face through substantial
purchase commitments and preferential pricing strategies. While this arrangement currently maintains supply chain stability, its
sustainability remains contingent upon the continued risk-absorption practices of technology conglomerates.
Startups face severe financial constraints where compliance costs can drastically affect their operating margins, as evidenced by
research indicating that a 200% increase in compliance costs could shift a startup’s operating margin from 13% to -7% [147]. Growth
of small and emerging enterprises is important for a dynamic economy, vibrant markets, and the preservation of a competitive
spirit. Small businesses are underappreciated drivers of economic growth, contributing approximately 44% of U.S. economic activity
alone and creating 62% of new jobs between 1995 and 2020 [125].
The imposition of extensive disclosure requirements on early-stage enterprises may impede innovation trajectories. Resource
constraints can limit these organisations’ capacity to navigate these frameworks, resulting in increased operational costs that may
deter market entry and extend commercialisation timelines [162]. Excessive regulatory oversight can foster risk aversion, potentially
inhibiting experimental approaches essential for technological advancement [97]. Thus the appropriate level of disclosure must be
adjusted to an entity’s size.

9 Conclusion
Our analysis demonstrates how market governance can function as instruments for promoting beneficial artificial intelligence
development trajectories. These mechanisms represent critical intervention points through which both public and private entities
can cultivate incentive structures that favour positive AI outcomes. Tools such as insurance, auditing, procurement, and due
diligence, which have long played a role in managing risks and fostering transparency in sectors like finance and pharmaceuticals,
are now beginning to emerge in the AI industry. Standardised disclosures are playing a growing role in reducing information
asymmetry, enabling more informed decisions by investors, insurers, and regulators.
Our examination of market governance of AI reveals promising avenues for exploring AI risk reduction as a key to AI adoption.
We encourage further investigation into these approaches by policymakers, economists, and machine learning researchers, as
the intersection of their expertise may yield valuable insights for future AI governance interventions. Further research in this
vein could significantly enhance our understanding of how market governance mechanisms might be optimally designed and
implemented to ensure beneficial AI outcomes while maintaining innovation and economic efficiency.
Acknowledgments
We extend our deepest gratitude to Kristian Ronn, Ilan Strauss, Jamie Bernardi, Colleen McKenzie, Gabor Szorad and Alex
Krasdomski for their contributions and invaluable insights to this research.
We also thank Miles Brundage, Miguel Diaz, Nicolas Moes, Ema Provic, James Fox, Cyrus Hodes, Milan Griffes, Deric Cheng, Jacob
Goodwin, Gabriel Weil, Lucy Philippon, Risto Uuk, Ryan Kidd, Shakeel Hashim, Deger Turan, Edmund Zagorin, David Lawrence
and Oliver Klingfjord for their helpful support and feedback throughout this work.
References
[1] J. Achiam, S. Adler, S. Agarwal, L. Ahmad, I. Akkaya, F. L. Aleman, and B. McGrew. 2023. GPT-4 technical report. arXiv preprint arXiv:2303.08774 (2023).
[2] L. Ackert and R. Deaves. 2009. Behavioral finance: Psychology, decision-making, and markets . Cengage Learning.
[3] Federal Aviation Administration. 2017. FAA Evaluation of Commercial Human Space Flight Safety Frameworks and Key Industry Indicators . Technical Report.
Federal Aviation Administration. https://www.faa.gov/sites/faa.gov/files/2021-11/Sec.-111-Report-to-Congress-Evaluation-of-Commercial-Human-Space-
Flight-Safety-Frameworks-and-Key-Industry-Indicators.pdf Report to Congress.
[4] Copyright Alliance. 2023. AI and Copyright in 2023: In the Courts. https://copyrightalliance.org/ai-copyright-courts/
[5] Onur Altintas. 2024. Navigating uncertainty: enhancing decision-making in healthcare and interpretable AI adoption . Ph. D. Dissertation.
[6] Nicolas Ameye, Jacques Bughin, and Nicolas van Zeebroeck. 2023. How uncertainty shapes herding in the corporate use of artificial intelligence technology.
Technovation 127 (2023), 102846. https://doi.org/10.1016/j.technovation.2023.102846
[7] M. Anderljung et al. 2023. Frontier AI regulation: Managing emerging risks to public safety. arXiv preprint arXiv:2307.03718 (2023).
[8] AON. 2024. Generative AI: Emerging Risks and Insurance Market Trends. https://www.aon.com/en/insights/articles/how-is-the-insurance-market-responding-
to-generative-ai
[9] E. Arrilucea and European Commission. 2018. Apollo Project - Mission-oriented R&I Policies: In-depth Case Studies . Technical Report. https://research-and-
innovation.ec.europa.eu/document/download/3fb7597a-1680-4dff-86a3-1b82b02ad4b0_en?filename=mission_oriented_r_and_i_policies_case_study_report_
apollo_project-us.pdf&prefLang=it
[10] P. Artzner, F. Delbaen, J. M. Eber, D. Heath, and H. Ku. 2007. Coherent multiperiod risk adjusted values and Bellman’s principle. Annals of Operations Research
152 (2007), 5–22.
[11] S. Arvidsson. 2011. Disclosure of non-financial information in the annual report: A management-team perspective. Journal of intellectual capital 12, 2 (2011),
277–300.
[12] PRI Association. 2024. Annual report 2024. https://www.unpri.org/about-us/about-the-pri/annual-report.

[13] H Kent Baker and Victor Ricciardi. 2014. Investor behavior: The psychology of financial planning and investing . John Wiley & Sons.
[14] Jamie Bernardi, Gabriel Mukobi, Hilary Greaves, Lennart Heim, and Markus Anderljung. 2024. Societal Adaptation to Advanced AI.arXiv preprint arXiv:2405.10295
(2024).
[15] Runa Bhaumik, Vineet Srivastava, Arash Jalali, Shanta Ghosh, and Ranganathan Chandrasekharan. 2023. Mindwatch: A smart cloud-based ai solution for suicide
ideation detection leveraging large language models. medRxiv (2023), 2023–09.
[16] P. Boettke and R. Candela. 2021. The common sense of economics and divergent approaches in economic thought: A view from risk, uncertainty, and profit.
Journal of Institutional Economics 17, 6 (2021), 1033–1047. https://doi.org/10.1017/s1744137421000229
[17] Rishi Bommasani, Kevin Klyman, S. Longpre, Sayash Kapoor, Nestor Maslej, Betty Xiong, Daniel Zhang, and Percy Liang. 2023. The Foundation Model
Transparency Index. ArXiv abs/2310.12941 (2023). https://api.semanticscholar.org/CorpusID:264306385
[18] D. Cahn. 2024. The AI Supply Chain Tug of War. https://www.sequoiacap.com/article/the-ai-supply-chain-tug-of-war/
[19] R. Calo. 2017. Artificial intelligence policy: a primer and roadmap. UC Davis Law Review 51 (2017), 399.
[20] Nicholas Carlini, Daphne Ippolito, Matthew Jagielski, Katherine Lee, Florian Tramer, and Chiyuan Zhang. 2022. Quantifying memorization across neural
language models. arXiv preprint arXiv:2202.07646 (2022).
[21] S. Cha. 2024. Towards an international regulatory framework for AI safety: Lessons from the IAEA’s nuclear safety regulations. Humanities and Social Sciences
Communications 11, 1 (2024), 1–13.
[22] V. Charles, A. Emrouznejad, and T. Gherman. 2023. A critical analysis of the integration of blockchain and artificial intelligence for supply chain. Annals of
Operations Research 327, 1 (2023), 7–47.
[23] J. Chen, S. H. Kao, H. He, W. Zhuo, S. Wen, C. H. Lee, and S. H. G. Chan. 2023. Run, don’t walk: chasing higher FLOPS for faster neural networks. In Proceedings
of the IEEE/CVF Conference on Computer Vision and Pattern Recognition . 12021–12031.
[24] Frederic T Chong, Martijn JR Heck, Parthasarathy Ranganathan, Adel AM Saleh, and Hassan MG Wassel. 2013. Data center energy efficiency: Improving energy
efficiency in data centers beyond technology scaling. IEEE design & test 31, 1 (2013), 93–104.
[25] Y. Y. Chong. 2004. Investment risk management. John Wiley & Sons.
[26] Google Cloud. [n. d.]. https://cloud.google.com/terms/service-terms
[27] Bain & Company. 2024. The Future of Insurance: As Risks Mount, Insurers Aim to Augment Protection with Prevention. https://www.bain.com/insights/future-
of-insurance-as-risks-mount-insurers-aim-to-augment-protection-with-prevention/
[28] Arthur Conmy, Augustine N. Mavor-Parker, Aengus Lynch, Stefan Heimersheim, and Adrià Garriga-Alonso. 2023. Towards Automated Circuit Discovery for
Mechanistic Interpretability. ArXiv abs/2304.14997 (2023). https://api.semanticscholar.org/CorpusID:258418244
[29] Sarah Constantin. 2024. The Great Data Integration Schlep. https://www.lesswrong.com/posts/7L8ZwMJkhLXjSa7tD/the-great-data-integration-schlep
[30] Shane Coughlan. 2020. Standardizing Open Source License Compliance With OpenChain. Computer 53 (2020), 70–74. https://api.semanticscholar.org/CorpusID:
226248064
[31] Francesco Croce, Maksym Andriushchenko, Vikash Sehwag, Edoardo Debenedetti, Edoardo Debenedetti, Mung Chiang, Prateek Mittal, and Matthias Hein. 2020.
RobustBench: a standardized adversarial robustness benchmark. ArXiv abs/2010.09670 (2020). https://api.semanticscholar.org/CorpusID:224705419
[32] D. Cullenward and D. G. Victor. 2020. Making Climate Policy Work. John Wiley & Sons.
[33] Q. Curtis, J. Fisch, and A. Z. Robertson. 2021. Do ESG mutual funds deliver on their promises? Mich. L. Rev. 120 (2021), 393.
[34] B. Daley, T. Geelen, and B. Green. 2024. Due diligence. The Journal of Finance 79, 3 (2024), 2115–2161.
[35] F. Decarolis et al. 2021. Buyers’ role in innovation procurement: Evidence from US military R&D contracts. Journal of Economics & Management Strategy 30, 4
(2021), 697–720.
[36] Deloitte. 2024. Deloitte’s State of Generative AI in the Enterprise Quarter three report. https://www2.deloitte.com/content/dam/Deloitte/us/Documents/
consulting/us-state-of-gen-ai-q3.pdf#page=3.11
[37] Deloitte. 2024. Life Sciences Industry Accounting Guide. https://www2.deloitte.com/content/dam/Deloitte/us/Documents/audit/us-life-sciences-industry-
accounting-guide-2024.pdf
[38] S. S. Dikolli, M. M. Frank, Z. M. Guo, and L. J. Lynch. 2022. Walk the talk: ESG mutual fund voting on shareholder proposals. Review of Accounting Studies 27, 3
(2022), 864–896.
[39] Executive Services Directorate. 2014. Department of Defense Manual: Defense Standardization Program (DSP) Proce-
dures. https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodm/412024m.pdf?ver=2017-12-13-110538-837 Retrieved from
https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodm/412024m.pdf?ver=2017-12-13-110538-837.
[40] Lavi M. Ben Dor and Cary Coglianese. 2021. Procurement as AI Governance. IEEE Transactions on Technology and Society 2, 4 (Dec. 2021), 192–199.
[41] J. R. Doty. 2014. The Role of Audit in Economic Growth. U.S. Chamber of Commerce: The Future of Financial Reporting. https://www.uschamber.com/financial-
reporting
[42] Wenyu Du, Tongxu Luo, Zihan Qiu, Zeyu Huang, Yikang Shen, Reynold Cheng, Yike Guo, and Jie Fu. 2024. Stacking Your Transformers: A Closer Look at Model
Growth for Efficient LLM Pre-Training. arXiv preprint arXiv:2405.15319 (2024).
[43] Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Amy Yang, Angela Fan,
et al. 2024. The llama 3 herd of models. arXiv preprint arXiv:2407.21783 (2024).
[44] The Economist. 2024. Unexpectedly, the cost of big cyber-attacks is falling. https://www.economist.com/graphic-detail/2024/05/17/unexpectedly-the-cost-of-
big-cyber-attacks-is-falling
[45] S. Ee. 2023. Adapting Cybersecurity Frameworks to Manage Frontier AI Risks: a Defense-in-Depth Approach. Institute for AI Policy and Strategy (IAPS) (2023).

[46] Francisco Eiras, Aleksander Petrov, Bertie Vidgen, Christian Schroeder, Fabio Pizzati, Katherine Elkins, Supratik Mukhopadhyay, Adel Bibi, Aaron Purewal, Csaba
Botos, Fabro Steibel, Fazel Keshtkar, Fazl Barez, Genevieve Smith, Gianluca Guadagni, Jon Chun, Jordi Cabot, Joseph Marvin Imperial, Juan Arturo Nolazco, Lori
Landay, Matthew Jackson, Phillip H. S. Torr, Trevor Darrell, Yong Suk Lee, and Jakob Foerster. 2024. Risks and Opportunities of Open-Source Generative AI.
ArXiv abs/2405.08597 (2024). https://api.semanticscholar.org/CorpusID:269761311
[47] El-Mahdi El-Mhamdi, Sadegh Farhadkhani, Rachid Guerraoui, Nirupam Gupta, Lê-Nguyên Hoang, Rafael Pinot, Sébastien Rouault, and John Stephan. 2022. On
the impossible safety of large AI models. arXiv preprint arXiv:2209.15259 (2022).
[48] Ivan D. Ertel, Roland W. Newkirk, NATIONAL AERONAUTICS, and SPACE ADMINISTRATION. 1978.The Apollo Spacecraft. National Aeronautics and Space
Administration (NASA).
[49] Silke Finken and C. Laux. 2009. Catastrophe Bonds and Reinsurance: The Competitive Effect of Information-Insensitive Triggers. https://doi.org/10.1111/j.1539-
6975.2009.01317.x
[50] P. Flöstrand and N. Ström. 2006. The valuation relevance of non-financial information. Management Research News 29, 9 (2006), 580–587.
[51] Fortune. 2024. AI Risks in Fortune 500 Companies’ Annual Reports. (August 2024). https://fortune.com/2024/08/18/ai-risks-fortune-500-companies-generative-
artificial-intelligence-annual-reports/ Accessed: 2024-12-02.
[52] World Economic Forum. 2024. Global Risks Report 2021. https://www.weforum.org/publications/the-global-risks-report-2021/
[53] Daniel Ganji, Christos Kalloniatis, Haralambos Mouratidis, and Saeed Malekshahi Gheytassi. 2019. Approaches to develop and implement iso/iec 27001
standard-information security management systems: A systematic literature review. Int. J. Adv. Softw 12, 3 (2019).
[54] Government Accountability Office (GAO). 2020. Defense Acquisitions Annual Assessment . Technical Report. Government Accountability Office. https:
//www.gao.gov/ Retrieved from https://www.gao.gov/.
[55] Gary Gereffi and Joonkoo Lee. 2016. Economic and Social Upgrading in Global Value Chains and Industrial Clusters: Why Governance Matters. Journal of
Business Ethics 133, 1 (2016), 25–38.
[56] Zoubin Ghahramani. 2015. Probabilistic machine learning and artificial intelligence. Nature 521, 7553 (2015), 452–459.
[57] Greystone. 2024. Managing Risk and Rising Insurance Premiums in Commercial Real Estate. https://www.greystone.com/insights/managing-risk-and-rising-
insurance-premiums-in-commercial-real-estate/
[58] Ross Gruetzemacher, Alan Chan, Štěpán Los, Kevin Frazier, Siméon Campos, Matija Franklin, James Fox, Jose Hernandez-Orallo, Christin Manning, Philip Tomei,
et al. 2023. An International Consortium for AI Risk Evaluations. In Socially Responsible Language Modelling Research .
[59] David Gunning and David W. Aha. 2019. DARPA’s Explainable Artificial Intelligence (XAI) Program. AI Mag. 40 (2019), 44–58. https://api.semanticscholar.org/
CorpusID:67773377
[60] C. I. Gutierrez, A. Aguirre, R. Uuk, C. C. Boine, and M. Franklin. 2023. A proposal for a definition of general purpose artificial intelligence systems. Digital Society
2, 3 (2023), 36.
[61] T. Götze and Marc Gürtler. 2021. Risk transfer beyond reinsurance: the added value of CAT bonds. , 125-171 pages. https://doi.org/10.1057/S41288-021-00234-6
[62] Gillian K Hadfield and Jack Clark. 2023. Regulatory markets: The future of ai governance. arXiv preprint arXiv:2304.04914 (2023).
[63] B. Hannon, Y. Kumar, D. Gayle, J. J. Li, and P. Morreale. 2024. Robust Testing of AI Language Model Resiliency with Novel Adversarial Prompts. Electronics 13, 5
(2024), 842.
[64] S. Hargreaves. 2010. BP’s $70 Billion Whipping. CNN (2010). https://money.cnn.com/2010/06/01/news/companies/BP_analysts/index.htm
[65] M. G. Harvey and R. F. Lusch. 1995. Expanding the nature and scope of due diligence. Journal of Business Venturing 10, 1 (1995), 5–21.
[66] D. Harwell. 2020. Everybody seems to be using Zoom. But its security flaws could leave users at risk. https://www.washingtonpost.com/technology/2020/04/02/
everybody-seems-be-using-zoom-its-security-flaws-could-leave-people-risk/
[67] O. A. Hassan and C. Marston. 2019. Corporate financial disclosure measurement in the empirical accounting literature: A review article. The International Journal
of Accounting 54, 2 (2019), 1950006.
[68] P. M. Healy and K. G. Palepu. 2001. Information asymmetry, corporate disclosure, and the capital markets: A review of the empirical disclosure literature. Journal
of Accounting and Economics 31, 1-3 (2001), 405–440.
[69] B. Heineman. 2011. How the BP Commission Dropped the Ball. Harvard Business Review (2011). https://hbr.org/2011/01/dropped-ball-on-bp-governance
[70] D. Hendrycks, C. Burns, S. Basart, A. Zou, M. Mazeika, D. Song, and J. Steinhardt. 2020. Measuring massive multitask language understanding. arXiv preprint
arXiv:2009.03300 (2020).
[71] D. Hendrycks, C. Burns, S. Kadavath, A. Arora, S. Basart, E. Tang, and J. Steinhardt. 2021. Measuring mathematical problem solving with the math dataset. arXiv
preprint arXiv:2103.03874 (2021).
[72] Merve Hickok. 2022. Public procurement of artificial intelligence systems: new risks and future proofing. AI &amp; SOCIETY 39, 3 (Oct. 2022), 1213–1227.
[73] Janine S Hiller and Roberta S Russell. 2017. Privacy in crises: The NIST privacy framework. Journal of Contingencies and Crisis Management 25, 1 (2017), 31–38.
[74] P. Howson. 2017. Due diligence: The critical stage in mergers and acquisitions . Routledge.
[75] M. M. Hudson and P. Stavrand. 2007. Best Practice Guidance for Angel Groups - Post Investment Monitoring. Corporate Governance: Disclosure (2007).
https://api.semanticscholar.org/CorpusID:111152938
[76] Open Source Initiative. 2004. Open Source Initiative.
[77] Corporate Finance Institute. 2023. Fortune 500 - Top Companies, Methodology, and Key Stats. https://corporatefinanceinstitute.com/resources/equities/fortune-
global-500/
[78] Brookings Institution. 2011. Balancing Disclosure, Protection of Trade Secrets, and Patentability in Light of Patent Reform. https://www.brookings.edu/articles/
balancing-disclosure-protection-of-trade-secrets-and-patentability-in-light-of-patent-reform/

[79] Myeongjun Jang, Antonios Georgiadis, Yiyun Zhao, and Fran Silavong. 2024. DriftWatch: A Tool that Automatically Detects Data Drift and Extracts Representative
Examples Affected by Drift. In Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language
Technologies (Volume 6: Industry Track). 335–346.
[80] Enrique Jaureguialzo. 2011. PUE: The Green Grid metric for evaluating the energy efficiency in DC (Data Center). Measurement method using the power demand.
In 2011 IEEE 33rd International Telecommunications Energy Conference (INTELEC) . IEEE, 1–8.
[81] Jean Kaddour, J. Harris, Maximilian Mozes, Herbie Bradley, Roberta Raileanu, and Robert McHardy. 2023. Challenges and Applications of Large Language Models.
ArXiv abs/2307.10169 (2023). https://api.semanticscholar.org/CorpusID:259982665
[82] R. Kauffman and T. A. Weber. 2021. Improving New Digital Market Mechanisms. Journal of Management Information Systems 38 (2021), 574–578. https:
//doi.org/10.1080/07421222.2021.1958541
[83] Tahseen Khan, Wenhong Tian, Shashikant Ilager, and Rajkumar Buyya. 2022. Workload forecasting and energy state estimation in cloud data centres: ML-centric
approach. Future Generation Computer Systems 128 (2022), 320–332.
[84] Ray Kiely. 1998. Neoliberalism revised? A critical account of World Bank conceptions of good governance and market friendly intervention. International Journal
of Health Services 28, 4 (1998), 683–702.
[85] Peter Kieseberg, Christina Buttinger, Laura Kaltenbrunner, Marlies Temper, and Simon Tjoa. 2022. Security considerations for the procurement and acquisition of
Artificial Intelligence (AI) systems. In 2022 IEEE International Conference on Fuzzy Systems (FUZZ-IEEE) . IEEE, 1–7.
[86] F. H. Knight. 1921. Risk, Uncertainty, and Profit. Houghton Mifflin.
[87] P. Koh and D. Reeb. 2014. R&D disclosures. Working Paper, National University of Singapore.
[88] KPMG. [n. d.]. How risk and compliance can accelerate generative AI adoption. https://kpmg.com/us/en/articles/2023/risk-function-accelerate-generative-ai-
adoption.html
[89] N. Krenz. 2022. An Analysis of the 2020 Zoom Breach. https://cloudsecurityalliance.org/blog/2022/03/13/an-analysis-of-the-2020-zoom-breach
[90] R. J. Kueppers and K. B. Sullivan. 2010. How and why an independent audit matters. International Journal of Disclosure and Governance 7, 4 (2010), 286–293.
[91] Gavin Leech, Juan J Vazquez, Misha Yagudin, Niclas Kupper, and Laurence Aitchison. 2024. Questionable practices in machine learning. arXiv preprint
arXiv:2407.12220 (2024).
[92] Yucheng Li. 2023. Unlocking context constraints of llms: Enhancing context efficiency of llms with self-information-based content filtering. arXiv preprint
arXiv:2304.12102 (2023).
[93] Pantelis Linardatos, Vasilis Papastefanopoulos, and Sotiris B. Kotsiantis. 2020. Explainable AI: A Review of Machine Learning Interpretability Methods. Entropy
23 (2020). https://api.semanticscholar.org/CorpusID:229722844
[94] Anat Lior. 2020. AI entities as AI agents: Artificial intelligence liability and the AI Respondeat Superior Analogy. Mitchell Hamline Law Review 46, 5 (2020), 2.
[95] A. Lior. 2021. Insuring AI: The role of insurance in artificial intelligence regulation. Harvard Journal of Law & Technology 35 (2021), 467.
[96] Yiheng Liu, Hao He, Tianle Han, Xu Zhang, Mengyuan Liu, Jiaming Tian, Yutong Zhang, Jiaqi Wang, Xiaohui Gao, Tianyang Zhong, et al. 2024. Understanding
llms: A comprehensive overview from training to inference. arXiv preprint arXiv:2401.02038 (2024).
[97] DW Magazine. 2024. Over-Regulation: The Silent Killer of Innovation and Invention.
[98] David Manheim, Sammy Martin, Mark Bailey, Mikhail Samin, and Ross Greutzmacher. 2024. The Necessity of AI Audit Standards Boards. arXiv preprint
arXiv:2404.13060 (2024).
[99] Frederic Marimon and Martí Casadesús. 2017. Reasons to adopt ISO 50001 energy management system. Sustainability 9, 10 (2017), 1740.
[100] Stefan Markowski, Peter Hall, and Robert Wylie. 2010. Defense Procurement and Industry Policy: A Small Country Perspective . Routledge.
[101] Marsh. 2021. The Changing Face of Cyber Claims 2021.
[102] Mantas Mazeika, Long Phan, Xuwang Yin, Andy Zou, Zifan Wang, Norman Mu, Elham Sakhaee, Nathaniel Li, Steven Basart, Bo Li, et al. 2024. Harmbench: A
standardized evaluation framework for automated red teaming and robust refusal. arXiv preprint arXiv:2402.04249 (2024).
[103] S. McAleese. 2023. An Overview of the AI Safety Funding Situation. https://forum.effectivealtruism.org/posts/XdhwXppfqrpPL2YDX/an-overview-of-the-ai-
safety-funding-situation
[104] Jack R McCaffrey. 2021. NASA’S SPACE ACT AGREEMENTS: EFFICIENT AND EFFECTIVE ACQUISITION IN EXPLORING THE FINAL FRONTIER. Public
Contract Law Journal 51, 1 (2021), 111–130.
[105] J. J. McCullough and M. J. Anstett. 2024. Public Procurement Laws and Regulations USA 2024. International Comparative Legal Guides International Business
Reports (February 8 2024). https://iclg.com/practice-areas/public-procurement-laws-and-regulations/usa Accessed: 2024-12-02.
[106] McKinsey and Company. 2024. The state of AI in early 2024: Gen AI adoption spikes and starts to generate value. https://www.mckinsey.com/capabilities/
quantumblack/our-insights/the-state-of-ai
[107] Eva Micheler and Anna Whaley. 2020. Regulatory technology: replacing law with computer code. European Business Organization Law Review 21 (2020), 349–377.
[108] Sparsh Mittal. 2014. Power management techniques for data centers: A survey. arXiv preprint arXiv:1404.6681 (2014).
[109] Xiaopeng Mo and Jie Xu. 2021. Energy-efficient federated edge learning with joint communication and computation design. Journal of Communications and
Information Networks 6, 2 (2021), 110–124.
[110] M. Moutii and M. Moutii. 2024. EU AI Act: How stricter regulations could hamper Europe’s AI innovation. https://en.irefeurope.org/publications/online-
articles/article/eu-ai-act-how-stricter-regulations-could-hamper-europes-ai-innovation/
[111] F. Musweu. 2018. The disclosure of financial and non-financial information in the corporate world.
[112] BBC News. 2020. Coronavirus: Zoom under increased scrutiny as popularity soars. https://www.bbc.com/news/business-52115434

[113] O. Novikov, Maryna Dubinina, and Vitalii Kuzoma. 2018. DUE DILIGENCE: ESSENCE AND POSSIBLE PROSPECTS OF DEVELOPMENT. Baltic Journal of
Economic Studies 4 (2018), 141–146. https://api.semanticscholar.org/CorpusID:55143491
[114] NASA Technical Reports Server (NTRS). 1971. What Made Apollo A Success? Technical Report. https://ntrs.nasa.gov/citations/19720005243
[115] C. Nyce et al. 2015. The capitalization of insurance premiums in house prices. Journal of Risk and Insurance 82, 4 (2015), 891–919.
[116] Abiodun Finbarrs Oketunji, Muhammad Anas, and Deepthi Saina. 2023. Large Language Model (LLM) Bias Index - LLMBI. ArXiv abs/2312.14769 (2023).
https://api.semanticscholar.org/CorpusID:266521434
[117] Harvard Law School Forum on Corporate Governance. 2021. ESG & Long-Term Disclosures: The State of Play in Biopharma. https://corpgov.law.harvard.edu/
2021/07/01/esg-long-term-disclosures-the-state-of-play-in-biopharma/
[118] OpenAI. 2023. Preparedness framework: Understanding risks, evaluating systems, and improving our readiness (Beta). https://cdn.openai.com/openai-
preparedness-framework-beta.pdf
[119] OpenAI. 2024. Model Spec. https://cdn.openai.com/spec/model-spec-2024-05-08.html Accessed: 2024-12-02.
[120] Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. 2022.
Training language models to follow instructions with human feedback. Advances in neural information processing systems 35 (2022), 27730–27744.
[121] R. Pallardy. [n. d.]. Deepwater Horizon Oil Spill. https://www.britannica.com/event/Deepwater-Horizon-oil-spill/Cleanup-efforts
[122] Venkatesh Balavadhani Parthasarathy, Ahtsham Zafar, Aafaq Khan, and Arsalan Shahid. 2024. The ultimate guide to fine-tuning llms from basics to breakthroughs:
An exhaustive review of technologies, research, best practices, applied research challenges and opportunities. arXiv preprint arXiv:2408.13296 (2024).
[123] David Patterson, Joseph Gonzalez, Quoc Le, Chen Liang, Lluis-Miquel Munguia, Daniel Rothchild, David So, Maud Texier, and Jeff Dean. 2021. Carbon emissions
and large neural network training. arXiv preprint arXiv:2104.10350 (2021).
[124] Petr Petera and Jaroslav Wagner. 2015. Global reporting initiative (GRI) and its reflections in the literature. European Financial and Accounting Journal 10, 2
(2015), 13–32.
[125] Podium. 2024. Why Small Businesses are Essential to Our Economy.
[126] M. Pozzoli and M. Raffaele. 2022. Non-financial information and company market value. Management Control: special issue 2 2022 (2022), 167–187.
[127] Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and Chelsea Finn. 2024. Direct preference optimization: Your language
model is secretly a reward model. Advances in Neural Information Processing Systems 36 (2024).
[128] M. S. Rapp, T. Schmid, and D. Urban. 2014. The value of financial flexibility and corporate financial policy. Journal of Corporate Finance 29 (2014), 288–302.
[129] Munich Re. 2024. Insuring Generative AI: Risks and Mitigation Strategies. https://www.munichre.com/content/dam/munichre/contentlounge/website-
pieces/documents/MR_AI-Whitepaper-Insuring-Generative-AI.pdf
[130] R. Reider. 2007. Financial audits: Taking an operational view. Journal of Corporate Accounting & Finance 18, 4 (2007), 19–25.
[131] D. Rein, B. L. Hou, A. C. Stickland, J. Petty, R. Y. Pang, J. Dirani, and S. R. Bowman. 2023. Gpqa: A graduate-level google-proof Q&A benchmark. arXiv preprint
arXiv:2311.12022 (2023).
[132] ESR Trends Report. 2024. ESG at ESR: Space and Investment Solutions for a Sustainable Future. https://www.esr.com/white-paper/esg-at-esr-space-and-
investment-solutions-for-a-sustainable-future/
[133] Pharmaceutical Technology Report. 2024. The top pharmaceutical companies by R&D expenditure. https://www.pharmaceutical-technology.com/features/the-
top-pharmaceutical-companies-by-rd-expenditure/
[134] Statista Report. 2024. Total global spending on pharmaceutical research and development from 2014 to 2030. https://www.statista.com/statistics/309466/global-
r-and-d-expenditure-for-pharmaceuticals/
[135] Reuters. 2024. Authors sue Anthropic for copyright infringement over AI training. https://www.reuters.com/technology/artificial-intelligence/authors-sue-
anthropic-copyright-infringement-over-ai-training-2024-08-20/
[136] H. Roberts et al. 2021. The Chinese approach to artificial intelligence: An analysis of policy, ethics, and regulation . Springer International Publishing.
[137] N. Ruiz, A. Kortylewski, W. Qiu, C. Xie, S. A. Bargal, A. Yuille, and S. Sclaroff. 2022. Simulated adversarial testing of face recognition models. In Proceedings of the
IEEE/CVF Conference on Computer Vision and Pattern Recognition . 4145–4155.
[138] N. Saini, M. Singhania, M. Hasan, M. P. Yadav, and M. Z. Abedin. 2022. Non-financial disclosures and sustainable development: A scientometric analysis. Journal
of Cleaner Production 381 (2022), 135173.
[139] S. Sarwar. 2023. 20 Largest Hedge Hedge Funds in the World and Their Top Stock Picks. https://finance.yahoo.com/news/20-largest-hedge-hedge-funds-
193651548.html?guccounter=1
[140] Alberta M Sbragia. 2000. Governance, the state, and the market: what is going on? Governance 13, 2 (2000), 243–250.
[141] A. Schilling-Vacaflor and A. Lenschow. 2021. Hardening foreign corporate accountability through mandatory due diligence in the European Union? New trends
and persisting challenges. Regulation & Governance 17, 3 (2021), 677–693. https://doi.org/10.1111/rego.12402
[142] H. Schmidt and R. Bales. 2018. Globalization of Defense Procurement: International Perspectives. Journal of International Business Studies 49, 4 (2018), 465–482.
[143] J. Schuett. 2023. Defining the scope of AI regulations. Law, Innovation and Technology 15, 1 (2023), 60–82.
[144] Moshe Schwartz and Stephen Howard Chadwick. 2008. Defense Acquisitions: Overview, Issues, and Options for Congress . Technical Report. Congressional Research
Service, Library of Congress.
[145] L. Sharkey et al. 2024. A Causal Framework for AI Regulation and Auditing. https://arxiv.org/pdf/2405.10295
[146] W. F. Sharpe. 1964. Capital asset prices: A theory of market equilibrium under conditions of risk. The Journal of Finance 19, 3 (1964), 425–442.
[147] Politics Shorenstein Center on Media and Harvard Kennedy School Public Policy. 2024. Why Compliance Costs of AI Commercialization May Be Holding
Start-Ups Back. https://studentreview.hks.harvard.edu/why-compliance-costs-of-ai-commercialization-maybe-holding-start-ups-back/

[148] Yash Raj Shrestha, Georg von Krogh, and Stefan Feuerriegel. 2023. Building open-source AI. Nature Computational Science 3 (2023), 908 – 911. https:
//api.semanticscholar.org/CorpusID:264539067
[149] P. Slattery, A. K. Saeri, E. A. Grundy, J. Graham, M. Noetel, R. Uuk, and N. Thompson. 2024. The AI Risk Repository: A Comprehensive Meta-Review, Database,
and Taxonomy of Risks From Artificial Intelligence. arXiv preprint arXiv:2408.12622 (2024).
[150] Janet Bautista Smith. 2016. The art of integrating strategic planning, process metrics, risk mitigation, and auditing . Quality Press.
[151] B. Snow. 2023. Mergers & Acquisitions for Dummies . John Wiley & Sons.
[152] K. Sperber, NATIONAL AERONAUTICS, and SPACE ADMINISTRATION. 1973. Apollo Experience Report - Reliability and Quality Assurance . Technical Report.
National Aeronautics and Space Administration (NASA). https://ntrs.nasa.gov/api/citations/19730023037/downloads/19730023037.pdf Retrieved from NASA
Technical Reports Server (NTRS).
[153] Sharath Turuvekere Sreenivas, Saurav Muralidharan, Raviraj Joshi, Marcin Chochowski, Mostofa Patwary, Mohammad Shoeybi, Bryan Catanzaro, Jan Kautz, and
Pavlo Molchanov. 2024. Llm pruning and distillation in practice: The minitron approach. arXiv preprint arXiv:2408.11796 (2024).
[154] M. A. Starr. 2008. Socially responsible investment and pro-social change. Journal of Economic Issues 42, 1 (2008), 51–73.
[155] Statista. 2024. Countries with the highest military spending worldwide in 2022. https://www.statista.com/statistics/262742/countries-with-the-highest-military-
spending/#:~:text=The%20United%20States%20led%20the,to%202.4%20trillion%20U.S.%20dollars. Accessed: 2024-12-02.
[156] Nassim Nicholas Taleb. 2020. Principia Politica: Politics & Ethics under Scaling and Uncertainty .
[157] J. Tate and M. Panteghini. 2007. Standardisation–the theory and the practice. Clin Biochem Rev. 28, 4 (2007), 127–130. https://doi.org/10.18392125
[158] J. Thewissen, Ö. Arslan-Ayaydin, W. Westerman, and A. Dorsman. 2024. The ESG Framework and the Energy Industry: Demand and Supply, Market Policies, and
Value Creation. In The ESG Framework and the Energy Industry: Demand and Supply, Market Policies and Value Creation . Springer International Publishing, 1–5.
[159] Access to Medicine Foundation. 2020. Which information matters most? Transparency by Pharma that builds access to medicine plus trust and engage-
ment. https://accesstomedicinefoundation.org/news/which-information-matters-most-transparency-by-pharma-that-builds-access-to-medicine-plus-trust-
and-engagement
[160] P. Tomei. 2024. The Commodification of Risk. https://coilink.org/20.500.12592/4ktc57q
[161] T. Turzo, G. Marzi, C. Favino, and S. Terzani. 2022. Non-financial reporting research and practice: Lessons from the last decade. Journal of Cleaner Production 345
(2022), 131154.
[162] J. Van Reenen, P. Aghion, and A. Bergeaud. 2021. The Impact of Regulation on Innovation.
[163] A. Vanstraelen, M. T. Zarzeski, and S. W. Robb. 2003. Corporate nonfinancial disclosure practices and financial analyst forecast ability across three European
countries. Journal of International Financial Management & Accounting 14, 3 (2003), 249–278.
[164] Juniper Ventures. 2024. AI Assurance Technology. https://www.aiat.report/
[165] Yanshu Wang, Tong Yang, Xiyan Liang, Guoan Wang, Hanning Lu, Xu Zhe, Yaoming Li, and Li Weitao. 2024. Art and Science of Quantizing Large-Scale Models:
A Comprehensive Overview. arXiv preprint arXiv:2409.11650 (2024).
[166] Alexander Wei, Nika Haghtalab, and Jacob Steinhardt. 2024. Jailbroken: How does llm safety training fail? Advances in Neural Information Processing Systems 36
(2024).
[167] D. Weinstein. 2024. How AI can bring new opportunity in the UK. https://blog.google/around-the-globe/google-europe/united-kingdom/ai-potential-uk/
[168] Gregor N. F. Weiß, Denefa Bostandzic, and Felix Irresberger. 2013. Catastrophe Bonds and Systemic Risk. https://doi.org/10.2139/ssrn.2313160
[169] E. Whiteside. 2024. Where Do Pension Funds Typically Invest? https://www.investopedia.com/articles/credit-loans-mortgages/090116/what-do-pension-funds-
typically-invest.asp
[170] R. Wilson. 2024. Sovereign Wealth Funds: An Introduction. https://www.investopedia.com/articles/economics/08/sovereign-wealth-fund.asp
[171] Ziqing Zeng and Sachin S Sapatnekar. 2023. Energy-efficient hardware acceleration of shallow machine learning applications. In 2023 Design, Automation & Test
in Europe Conference & Exhibition (DATE) . IEEE, 1–6.
[172] H. Ziady. 2020. BP will Slash Oil Production by 40% and Pour Billions into Green Energy. CNN (2020). https://edition.cnn.com/2020/08/04/business/bp-oil-clean-
energy/index.html
A AI Risk Standardisation Targets
A.1 Data Acquisition and Privacy in AI Systems
Data acquisition is a foundational step in developing large models, as the quality and diversity of datasets directly influence
the performance and reliability of AI systems. This stage requires careful attention to privacy regulation especially given the
legal landscapes (e.g., GDPR). As such, standardised reporting in this domain might include metrics related to data provenance,
detailing the sources and methods of data collection—whether through scraping, crowd sourcing, or third-party purchases — and
providing transparency on labelling practices. Recent legal challenges, such as lawsuits against AI companies for using copyrighted

materials [4, 135] underscore the importance of curating datasets to exclude unauthorised content. A core issue in data privacy
relates to how personal information is managed and protected during and after collection. High-performance models often require
substantial data retention, which can inadvertently include sensitive information [47]. Private data, such as contact numbers and
email addresses, can remain within training datasets and be extracted from models [20].
Companies can provide standardised disclosures on their data practices. This could include descriptions of data minimisation
efforts, encryption standards, data anonymisation techniques, data storage practices, retention periods, and the purposes for
which data is used. Disclosures may also cover details on third-party access to data, as well as how companies handle data subject
requests, such as access, rectification, or erasure of personal information. Transparent reporting on data breaches—such as the
number of sensitive records exposed, their nature, and mitigation measures—could further aid market participants in assessing
a company’s risk management capabilities. Where appropriate, companies can employ existing standardisation metrics from
frameworks such as the ISO/IEC 27001 for information security [53], and the NIST Privacy Framework [73].
A.2 Energy: Data Centre Efficiency and Algorithm Design
Large AI models have large energy demands, driving the need for energy-efficient infrastructure and algorithms. Data centre
efficiency methods aim to optimise the energy use of computational resources to support model training. This includes strategies for
aligning workload demands, resource allocation, and energy balancing [24], alongside software-oriented approaches for workload
management [83], and integrated power management strategies [108]. Simultaneously, algorithm design plays a critical role in
improving the energy efficiency of machine learning processes, with techniques like federated edge learning [ 109], hardware
acceleration [171], and sparsely activated deep neural networks [123] offering significant reductions in energy consumption.
Standardised reporting on data centre efficiency might include energy consumption metrics like Power Usage Effectiveness (PUE)
and the proportion of energy derived from renewable sources [80]. Companies could also disclose which energy sources they use.
For algorithm design, companies could report on energy efficiency metrics related to training processes, detailing how different
techniques reduce the computational burden. Frameworks like the GRI [124], ISO 50001 [99], and The Green Grid [80] can already
provide some reporting guidelines.
A.3 Compute Allocation
Describing the allocation of compute resources would reveal information about the production processes and the safety measures
applied throughout AI model development. Market actors could understand a company’s strategic focus. For example, companies
could disclose the quarterly compute spend on pre-training, mid-training, post-training, safety work, and inference [43, 96]. This
macro overview could market participants, such as investors performing due diligence, evaluate where a company places its
resources and how it balances the goals of innovation, safety, and efficiency.
A.4 Intended Model Behaviour
Large model developers use a series of different method to shape their model’s behaviour. This involves shaping model outputs
to prioritise valuable behaviours while preventing unsafe, illegal, or unethical content. Techniques such as RLHF [120], Direct

Preference Optimisation (DPO) [127], fine-tuning [122], red-teaming [102], and output filters [92] are commonly employed to align
model outputs with desired outcomes to ensure models remain safe for public use. A great focus is placed on avoiding unwanted
behaviours, which result in reputational risks and legal liabilities. Key areas of concern include avoiding, harmful content, such as
suicide ideation [15], "hallucinations" [81], and bias in model outputs [116].
To standardise disclosures related to intended model behaviour, companies could report on their intended model behaviours, and
the methods and processes that they are employing to achieve these intended behaviours. The OpenAI Model Spec provides a
strong example of transparency in this area [119]. It details how it wants its models to behave, whilst trying to align with specific
ethical objectives, safety measures, and user needs, balancing user directives with broader considerations like legality and societal
impact.
A.5 Model Interpretability
Model interpretability involves methods that enhance the transparency and understanding of AI systems [59]. Often, AI models
function as "black boxes, " making it difficult to understand the reasoning behind their predictions. Explainable AI [93] and
Mechanistic Interpretability [28] offer techniques for clarifying the logic behind model outputs, helping stakeholders gain better
insights into the model’s decision-making process.
Companies could standardise the disclosure of interpretability techniques to provide insights into how specific decisions are made.
They might also disclose aspects of model architecture, any identified biases or limitations. There are technical breakthroughs that
need to be made for this to be fully possible, but setting standards also sets a research aim. Frameworks like the Foundation Model
Transparency Index [17] could guide some of these disclosures.
A.6 Open-source practices
Open-source practices in AI development allow developers to share code, datasets, and methodologies [148]. This openness can
accelerate progress and enable efficient peer review to identify and rectify errors. Open-sourcing advanced AI models can also come
with risks, such as model poisoning and dual-use concerns (e.g., repurposing models for harmful applications) [46]. Additionally,
transparency can challenge intellectual property (IP) management and compliance with data privacy laws.
To standardise open-source practices, companies might disclose detailed documentation of their open-source contributions,
including code, datasets, and methodologies. Disclosing incidences of potential dual-use cases can aid regulatory bodies in
understanding associated risks. Companies could also outline governance structures for contributions and establish clear policies
for IP rights (IPR) and licensing, particularly when integrating open-source elements into commercial products. Companies can
use aspects of existing frameworks like the Open Source Initiative [ 76] for licensing, or the Linux Foundation’s OpenChain
Specification [30] for open-source compliance.
A.7 Adversarial Testing
Adversarial testing assesses the resilience of AI systems by exposing them to challenging inputs designed to exploit vulnerabilities.
These methods are essential for evaluating how AI models withstand malicious attempts, especially in security-sensitive applications

[137]. They help identify risks such as data poisoning, evasion attacks, and extraction threats, which can compromise model
integrity [63].
Companies could standardise disclosures by detailing adversarial risks identified during testing. Reporting the scale, frequency,
and outcomes of these tests, as well as the data sources, can provide stakeholders with insights into a model’s robustness [31].
B Existing Disclosure Frameworks
Lack of corporate transparency coupled with inadequate risk assessment by investors creates a precarious foundation for potential
catastrophic outcomes. The 2008 collapse of Lehman Brothers serves as a reminder about the far-reaching consequences of
inadequate information transparency and (public, investors’, and regulatory) oversight in the markets. Leading up to its bankruptcy,
Lehman had amassed significant exposure to subprime mortgages, which were increasingly seen as high-risk investments. As
homebuyers defaulted on loans they couldn’t afford, it sent shockwaves to Wall Street. This led to a global financial crisis and
millions of job losses and home foreclosures. Despite warning signs, such as declining housing prices and rising mortgage
delinquencies, many investors continued to back Lehman’s stock. This disaster could have been uncovered at a nascent stage with
rigorous oversight and due diligence. Lehman also employed deceitful accounting practices known as "Repo 105, " temporarily
removing debt from its balance sheet - a clear information asymmetry and lack of transparency between Lehman’s management
and stakeholders.
Industries with high transformative potential and safety-critical environments—like defence, finance, biotechnology, semiconductor,
petrochemicals, pharmaceuticals—are primed to adopt a culture of AI safety due to their existing security mindsets. In these
sectors, AI integration has the potential to scale operations at an unprecedented rate, but this rapid expansion often occurs
without responsible oversight, magnifying risks and accelerating crises. The table below demonstrates how risks and opportunities
emerging from AI can be disclosed within the limits of already existing reporting frameworks/guidelines.

Existing Frame-
works
Existing Categories Integration of AI Risk and Opportunities into Disclo-
sures
ISO/TC 276, Biotech-
nology
Analytical Methods, Bio-
processing, Data Processing
and Integration, Biobank
and Bioresources, Predictive
Computational Models
Predictive Computational Models: Model overfitting, poor
generalisation, lack of ethical oversight, biased predictions.
Biobank and Bioresources: Privacy and security concerns,
genetic data leaks leading to discrimination, mismanagement
in biosample cataloguing/storage, and degradation from sys-
tem failures.
Analytical Methods: Issues in data integrity, validation er-
rors, algorithmic misclassification.
Bioprocessing: Risks from flawed algorithms, quality control
failures, bioproduction yield optimization destabilizing supply
chains, and privacy compromises.
Data Processing and Integration: Interoperability errors,
annotation biases impacting research.
Pharmaceutical Sup-
ply Chain Initiative
(PSCI)
Ethics, Human Rights, Health
and Safety, Sustainability,
Materials, Supply Chain
Resilience
Ethics: AI-driven medical decisions, bias in diagnostics, price
gouging, and automated fraud detection.
Human Rights: Surveillance in labor practices, job displace-
ment, discrimination.
Health and Safety: Automation of hazardous materials han-
dling, mental health implications, failure to predict emergen-
cies.
Sustainability: Efficient resource consumption offset by in-
creased emissions and waste.
Materials: Cyber risks in traceability of sourcing materials.
European Federation
of Pharmaceutical In-
dustries
Patient Safety and Clinical
Trials, Data Privacy, Supply
Chain Transparency, IP Pro-
tection, RnD Transparency,
Corporate Responsibility
Patient Safety and Clinical Trials: Bias in algorithms skew-
ing trial outcomes, misdiagnosis, privacy breaches, lack of
accountability.
RnD Transparency: Reporting AI in drug discovery, ensur-
ing diverse patient group applicability.
IP Protection: Risks in disclosing sensitive model details.
Supply Chain Transparency: Over-reliance on AI logistics
predictions creating vulnerabilities.
Data Privacy: GDPR compliance and patient data security
challenges.
Table 2. Biopharmaceuticals: Integration of AI Risks and Opportunities into Disclosures

Existing Frame-
works
Existing Categories Integration of AI Risk and Opportunities into Disclo-
sures
Securities and Ex-
change Commission
(SEC)
Risk Factors, Management’s
Discussion and Analysis
(MDandA), Financial State-
ments, Internal Control over
Financial Reporting, Executive
Compensation, Legal Proceed-
ings
Risk Factors: Market volatility from algorithmic trading, bi-
ased lending models, model failure, privacy violations, data
theft, market swings, dependency on market makers, lack of
transparency and interpretability in model outputs, informa-
tion asymmetry, losses due to inaccurate model predictions,
algorithmic collusion, market manipulation, unpredictability,
data quality risks.
MDandA: AI impact on financial performance, operational
efficiencies, and systemic vulnerabilities due to AI integration.
Financial Statements: AI-related assets, liabilities from AI
investments, impairment risks, potential liabilities from cyber
breaches, platform engagement statistics post-AI integration.
Executive Compensation: AI-driven metrics for perfor-
mance evaluation and biases.
Legal Proceedings: Regulatory scrutiny of AI practices, liti-
gation risks related to AI misuse, discrimination claims, failure
to comply with privacy laws (GDPR, etc.).
Solvency II Directive
(EU)
Quantitative Requirements,
Governance and Risk Manage-
ment, Solvency and Financial
Condition Report, Supervisory
Review Process
Quantitative Requirements: Capital requirements for
model risk, investment into AI safety, model performance
statistics.
Risk Management: Cybersecurity threats, data dependency
(inaccurate financial projections), AI oversight mechanisms,
transparency and accountability issues for AI-driven decisions,
biased lending models, risk prediction models, stress testing
with AI models.
Solvency: Market instability, algorithmic trading impacts,
spread of misinformation, manipulation of user behavior, in-
sufficient capital reserves due to unexpected AI-related losses.
Supervisory Review Process: Regulatory scrutiny over AI
practices, evaluation of AI risk management practices.
Financial Stability
Board (FSB) reports
Systemic Risk, Regulatory
Framework, Macroprudential
Policy, Financial Stability
Assessments, Data Quality
and Governance, Institutional
Resilience, Market Conduct
and Consumer Protection,
International Cooperation
Systemic Risk: AI-induced market volatility, algorithmic
trading risks, flash crashes, stress testing scenarios.
Macroprudential Policy: AI impact on financial cycles, AI’s
role in economic forecasting, policy responses.
Financial Stability Assessments: Risks in high-frequency
trading or algorithmic trading (e.g., flash crashes).
Data Governance: Data quality and privacy risks, algorith-
mic decision transparency, stock manipulation.
Institutional Resilience: Cyber threats and operational vul-
nerabilities, financial shock absorption capability.
Consumer Protection: Misleading information due to "AI-
washing, " biased lending models, data privacy concerns.
International Cooperation: Global coordination on AI gov-
ernance, cross-border data sharing.
Table 3. Finance: Integration of AI Risks and Opportunities into Disclosures

Existing Frame-
works
Existing Categories Integration of AI Risk and Opportunities into Disclo-
sures
Initiative for Responsi-
ble Mining Assurance
(IRMA) Standard
Environmental Stewardship,
Labor Rights, Mine Closure
and Rehabilitation, Planning
for Positive Legacies, Economic
Responsibility, Security Ar-
rangements, Cultural Heritage
(Indigenous Peoples’ Rights),
Supply Chain Management
Supply Chain Resilience: Cyber vulnerabilities, supplier
diversification, diminished traceability due to opaque AI.
Cultural Heritage: Over-exploitation and erosion of biodi-
versity and tribal culture, inadequate representation of Indige-
nous knowledge.
Environmental Stewardship: Algorithmic bias underesti-
mating biodiversity loss, improper waste disposal, and re-
source depletion due to poor automated predictions.
Labour Rights: Safety risks from AI-driven equipment, tribal
unemployment, inadequate resource allocation for emergen-
cies, job displacement due to mining automation.
Mine Closure and Rehabilitation: Automated detection of
environmental impacts post-closure.
Extractive Industries
Transparency Initia-
tive (EITI)
Revenue Reporting, Payments
to Governments (taxes, royal-
ties, fees), Licensing and Con-
tracts, Production Data, Owner-
ship Structures, Social and En-
vironmental Impact, Revenue
Management and Expenditure,
Sub-national Payments
Revenue Reporting: AI inaccuracies in revenue forecasting,
impacts on fiscal transparency, and mismanagement of public
funds.
Payments to Governments: Automation errors in tax com-
pliance.
Licensing and Contracts: Compliance risks, AI-driven data
theft, and legal reasoning issues.
Production Data: Provenance issues, poor resource alloca-
tion due to inaccurate predictions.
Social and Environmental Impact: Job displacement risks,
pollution (air, water, waste dumping), biodiversity loss, habitat
destruction for migratory animals.
International
Petroleum Indus-
try Environmental
Conservation Associ-
ation (IPIECA)
Governance, Health, Safety, En-
vironment, Social Responsibil-
ity
Governance: Lack of accountability in AI decision-making,
algorithmic decisions in supplier selection.
Climate/Energy/Environment: Energy consumption from
AI-driven operations, inefficiencies in climate risk modelling.
Biodiversity: Accelerated destruction from AI tools.
Safety, Health, and Security: Predictive systems for acci-
dent prevention, risks from autonomous systems (e.g., drones,
robotics).
Social Responsibility: Job displacement due to automation,
biased decision-making algorithms.
Table 4. Extractive Industries: Integration of AI Risks and Opportunities into Disclosures

Existing Frame-
works
Existing Categories Integration of AI Risk and Opportunities into Disclo-
sures
Carbon Disclosure
Project (CDP)
Governance, Strategy, Risks
and Opportunities, Targets,
Emissions, Energy, Environ-
mental Performance (Cli-
mate Change, Water Secu-
rity, Forests, Biodiversity),
Supply Chain, Engagement
Risks and Opportunities: Resource optimisation,
predictive maintenance, smart grid management, safety
monitoring, operational risks from AI decision-making
errors, cyber risk, grid dysfunction.
Targets: Using AI to achieve SDG, green energy, waste
management (e-waste generation from hardware upgrades),
scaling AI responsibly.
Emissions: Real-time data analytics, optimizing data
centres’ location based on energy sources.
Climate Change: AI’s role in climate adapta-
tion/mitigation, forecasting, carbon footprint of LLMs.
Water: AI’s use in water resource management, sustainable
practices.
Forests and Biodiversity: Ecological modelling, satellite
imagery analysis, biodiversity loss mitigation.
NIST Risk Manage-
ment Framework
Prepare, Categorize, Select,
Implement, Assess, Autho-
rise, Monitor
Prepare: Identify AI risks (bias, privacy, security), set ac-
ceptable residual risk levels, establish ethical guidelines.
Categorise: Classify risks by severity and sensitivity.
Select Security: Apply AI-specific controls for privacy, ro-
bustness.
Implement: Integrate controls, train workforce, mitigate
bias.
Assess: Test AI robustness, detect bias, validate models.
Authorise: Approve for use, verify compliance, document
risks.
Monitor: Continuously track AI risks, feedback into strate-
gies.
International Inte-
grated Reporting
Council (IIRC)
Organisational Overview,
Governance, Business
Model, Risks and Oppor-
tunities, Strategy and
Resource Allocation, Per-
formance, Future Outlook
Financial Capital: Metrics for costs, savings, risks, obso-
lescence.
Intellectual Capital: Proprietary technologies, over-
reliance risks.
Human Capital: Safeguard liberties, ensure equality and
safety.
Natural Capital: Efficiency, carbon footprint of data cen-
tres.
Social Capital: Mitigate misinformation, adhere to GDPR.
Future Outlook: AI lab partnerships, R&D revenue per-
centage, dual-use cases.
Table 5. Environment and Sustainability: Integration of AI Risks and Opportunities into Disclosures

Existing Frame-
works
Existing Categories Integration of AI Risk and Opportunities into Disclo-
sures
Nuclear Regulatory
Commission (NRC)
License Application and Re-
view Process, Operations,
Safety Culture Policy State-
ment, Cybersecurity Reg-
ulations, Emergency Pre-
paredness, Environmental
Review, Quality Assurance
Requirements
Cybersecurity Regulations: Cybersecurity threats ex-
ploiting nuclear controls, extortion risks, espionage, adver-
sarial attacks on safety-critical systems, incident response
plans.
Operations: Monitoring algorithm performance, address-
ing system failures, unauthorised access risks, decision-
making transparency issues.
Safety Culture Policy Statement: Use AI to enhance
safety systems, balance human oversight, train staff on AI
safety.
Emergency Preparedness: Reliance on AI for emergency
response, risk of misinformation, quality of training data
affecting predictions.
Quality Assurance Requirements: Model validation, test-
ing protocols, documentation.
International
Atomic Energy
Agency (IAEA)
Safety of Nuclear Instal-
lations, Nuclear Security,
Safety Assessment for Facil-
ities and Activities, Manage-
ment System, Emergency
Preparedness, Radiological
Safety, Radioactive Waste
Management, RnD
Safety of Nuclear Installations: Address AI-related con-
trol failures, accountability in opaque AI systems.
Nuclear Security: AI vulnerabilities in surveillance sys-
tems, bias in threat detection algorithms.
Management System: AI’s role in reactor monitoring,
training employees for AI integration, simulating emer-
gency responses.
Radiological Safety: AI errors in detecting radiation lev-
els, efficient waste transport and logistics systems.
Table 6. Integration of AI Risks and Opportunities into Nuclear Disclosures
