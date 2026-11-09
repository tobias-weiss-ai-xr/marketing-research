---
title: 'Generative AI and Customer Engagement in Digital Marketing: A Systematic Review and Evidence Map
  of Affective vs. Behavioral Outcomes, Disclosure Effects, and Human-in-the-Loop Moderation'
url: https://doi.org/10.1177/27523543261461786
category: ai-marketing
subcategory: empirical
date: 2026-06
venue: Emerging Media
authors:
- Sangita Pokhrel
- Nalinda Somasiri
source: openalex-oa
pdf_url: https://ray.yorksj.ac.uk/id/eprint/15340/1/pokhrel-somasiri-2026-generative-ai-and-customer-engagement-in-digital-marketing-a-systematic-review-and-evidence-map.pdf
pages: 21
chars: 54361
fetched_at: '2026-11-08T18:14:42+00:00'
kb_version: 1
---

# Generative AI and Customer Engagement in Digital Marketing: A Systematic Review and Evidence Map of Affective vs. Behavioral Outcomes, Disclosure Effects, and Human-in-the-Loop Moderation

RaY
Research at the University of York St John
For more information please contact RaY at
ray@yorksj.ac.uk
Pokhrel, Sangita and Somasiri, Nalinda (2026) Generative AI and
Customer Engagement in Digital Marketing: A Systematic Review
and Evidence Map of Affective vs. Behavioral Outcomes, Disclosure
Effects, and Human-in-the-Loop Moderation. Emerging Media.
Downloaded from: https://ray.yorksj.ac.uk/id/eprint/15340/
The version presented here may differ from the published version or version of record. If
you intend to cite from the work you are advised to consult the publisher's version:
https://doi.org/10.1177/27523543261461786
Research at York St John (RaY) is an institutional repository. It supports the principles of
open access by making the research outputs of the University available in digital form.
Copyright of the items stored in RaY reside with the authors and/or other copyright
owners. Users may access full text items free of charge, and may download a copy for
private study or non-commercial research. For further reuse terms, see licence terms
governing individual outputs.  Institutional Repositories Policy Statement

Generative AI and Customer
Engagement in Digital
Marketing: A Systematic Review
and Evidence Map of Affective
vs. Behavioral Outcomes,
Disclosure Effects, and Human-
in-the-Loop Moderation
Sangita Pokhrel 1 and Nalinda Somasiri 1
Abstract
The rapid advancement of generative arti ﬁcial intelligence (AI) has transformed digital marketing,
redeﬁning how brands create, personalize, and deliver content to engage consumers. As organiza-
tions increasingly rely on AI-driven systems for customer interaction, understanding how these tech-
nologies in ﬂuence customer engagement has become a critical area of inquiry. This study
systematically reviews research published between 2022 and 2025 to evaluate the impact of genera-
tive AI on customer engagement, distinguishing between affective outcomes (e.g., satisfaction, trust,
and commitment) and behavioral outcomes (e.g., click-throughs, shares, purchases, and retention).
Following PRISMA guidelines, a comprehensive search across major databases (Scopus, Web of
Science, and Google Scholar) identiﬁed 528 records, of which 64 articles were assessed for eligibility,
and 33 studies met theﬁnal inclusion criteria for qualitative synthesis. Findings indicate that generative
AI tools, particularly large language models (LLMs) for conversational marketing and generative
adversarial or diffusion models for visual content, generally associated with positive behavioral
engagement outcomes, such as improved attention, interactivity, and conversion rates, although
these effects vary depending on context, platform, and implementation. However, affective engage-
ment outcomes remain mixed; while personalization and novelty foster satisfaction and delight,
authenticity concerns often hinder trust and emotional connection. Two moderating factors, AI con-
tent disclosure and human-in-the-loop (HITL) oversight, emerged as critical inﬂuences. Transparent
disclosure can enhance credibility in some contexts but evoke skepticism in others, while human
1Department of Computer Science and Data Science, York St John University, London, UK
Corresponding Author:
Sangita Pokhrel, Department of Computer Science and Data Science, York St John Universityy, London, UK.
Email: s.pokhrel@yorksj.ac.uk
Creative Commons CC BY: This article is distributed under the terms of the Creative Commons
Attribution 4.0 License (https:/ /creativecommons.org/licenses/by/4.0/) which permits any use,
reproduction and distribution of the work without further permission provided the original work is attributed as speci ﬁed
on the SAGE and Open Access page (https:/ /us.sagepub.com/en-us/nam/open-access-at-sage).
Original Research Article
Emerging Media
1–20
© The Author(s) 2026
Article reuse guidelines:
sagepub.com/journals-permissions
DOI: 10.1177/27523543261461786
journals.sagepub.com/home/emm

oversight consistently reinforces brand authenticity, ethical quality, and consumer con ﬁdence.
Practical implications include guidance on effective AI disclosure strategies, when and how to be
transparent about AI generation and the importance of maintaining a human touch in AI-augmented
marketing. The review also identiﬁes key research gaps, including long-term effects on brand loyalty,
cross-cultural differences, and ethical and legal implications, and proposes a future research agenda to
advance knowledge in this rapidly evolving ﬁeld.
Keywords
generative AI, digital marketing, customer engagement, affective outcomes, behavioral outcomes,
AI disclosure, human-in-the-loop, systematic review, PRISMA
Received: December 19, 2025; revised: May 4, 2026; accepted: May 4, 2026
Introduction
Recent advances in generative arti ﬁcial intelligence (AI), from large language models (LLMs) like
GPT-4/5 to image generators like generative adversarial networks (GANs) and diffusion models are
transforming digital marketing. Brands now deploy AI to autonomously create content, personalize
communications, and even interact with customers via chatbots (Sundari et al., 2025). The rapid
adoption of these technologies re ﬂects a broader organizational shift toward AI-driven operations,
according to Mckinsey & Company ’s State of AI Report (2025), 78% of organizations now use AI
in at least one business function, with marketing and sales among the most common areas of appli-
cation (Sundari et al., 2025). This widespread adoption underscores the growing strategic import-
ance of AI in shaping customer experiences. Yet this paradigm shift raises critical questions about
customer engagement: How does AI-generated content affect consumers ’ feelings and behaviors?
Does knowing that an advertisement or message was produced by AI change how customers
respond? And what role do human marketers play when AI is “in the loop ” of content creation?
These questions are increasingly salient as generative AI (GenAI) moves from a novel experiment
to a mainstream marketing tool.
Customer engagement is a multidimensional construct encompassing both effective and behav-
ioral dimensions. The effective dimension re ﬂects consumers’ emotional and attitudinal responses
such as interest, enjoyment, trust, satisfaction, and commitment while the behavioral dimension
captures observable actions such as clicks, shares, comments, purchases, and repeat visits. In digital
marketing, these two dimensions are closely interlinked, that is, emotionally positive experiences
strengthen brand loyalty and word-of-mouth, while behavioral engagement directly drives sales
and visibility (Lai Cheung et al., 2024). GenAI has the potential to shape both aspects simultan-
eously. For instance, AI-driven personalization may delight customers (affective) and trigger imme-
diate purchases (behavioral), whereas AI-generated content that appears inauthentic could erode
trust (affective) and reduce engagement (behavioral). Empirical research offers a mixed picture
of this transformation. On the one hand, GenAI enables large-scale hyper-personalization and
creative optimization, often producing “superhuman” marketing content that rivals or exceeds
human-created materials in quality (Lim et al., 2022). Several studies report signi ﬁcantly higher
engagement metrics, such as up to 50% higher click-through and conversion rates for
AI-generated advertisements demonstrating clear behavioral bene ﬁts (Singla et al., 2025). On the
other hand, the emotional side of engagement remains fragile. The absence of human authenticity
2 Emerging Media

and ethical sensitivity can weaken perceived credibility and trust, particularly when customers real-
ize that content or communication is AI-generated. This transparency dilemma whether to disclose
or conceal AI involvement poses strategic and ethical challenges for marketers (Li et al., 2024).
While disclosure aligns with responsible AI principles, it may also in ﬂuence how consumers inter-
pret the persuasive intent behind the message. Drawing on persuasion knowledge theory (Rahmani,
2023), consumers may become more critical when they recognize that content is designed to per-
suade them. Compared to traditional human-created advertising, AI-generated content may be per-
ceived as algorithmically optimized for persuasion and lacking visible human effort, which can
heighten skepticism in certain contexts and potentially diminish engagement. Moreover, fully auto-
mated content generation without human oversight risks producing off-brand, culturally insensitive,
or factually incorrect outputs, thereby undermining both emotional and behavioral engagement
(Sundari et al., 2025).
Given the rapid adoption of GenAI in marketing and the fragmented nature of existing evidence,
there is a need for a structured synthesis that clearly distinguishes between different dimensions of
engagement and the contextual factors shaping these outcomes. To address this gap and guide the
scope and structure of the review, the following research questions are proposed:
RQ1: How does generative AI in ﬂuence behavioral engagement outcomes in digital marketing contexts?
RQ2: How does generative AI affect affective engagement outcomes, including trust, satisfaction, and emo-
tional response?
RQ3: What moderating factors, particularly AI disclosure and human-in-the-loop (HITL) oversight, in ﬂu-
ence the relationship between generative AI and customer engagement?
RQ4: What theoretical and practical insights emerge from the current literature regarding the effective and
responsible use of generative AI in marketing?
This study addresses these research questions through a PRISMA-based systematic review of
literature published between 2022 and 2025, providing an integrated and evidence-based under-
standing of how GenAI shapes both the emotional and behavioral dimensions of engagement.
The review categorizes outcomes into affective and behavioral engagement, while analyzing two
key moderating factors: AI content disclosure and human-in-the-loop (HITL) oversight. Both fac-
tors frequently appear as critical determinants of AI effectiveness in marketing contexts. The article
proceeds by outlining the review methodology, presenting results across these dimensions, and
integrating ﬁndings into an evidence map that illustrates how GenAI in ﬂuences both the emotions
and actions of customers. The discussion then synthesizes theoretical implications (e.g., authenti-
city and persuasion knowledge in AI marketing), offers practical guidance for AI disclosure and
hybrid human –AI strategies, and identi ﬁes future research directions concerning long-term brand
loyalty, AI aversion, and governance in marketing practice (Cillo & Rubera, 2025). Through this
comprehensive review, we aim to provide scholars and practitioners a state-of-the-art understanding
of GenAI’s dual impact on the emotions and behaviors of customers and how thoughtful strategy
(around disclosure and human collaboration) can maximize the bene ﬁts while mitigating the risks.
Theoretical foundations of generative AI and customer engagement
To provide a conceptual basis for this review, it is important to explain how GenAI in ﬂuences cus-
tomer engagement. Rather than functioning solely as a technological tool, GenAI acts as a socio-
technical agent that shapes how consumers perceive and respond to marketing stimuli (Singla et al.,
2025; Sun et al., 2025).
Pokhrel and Somasiri 3

A primary theoretical lens is the Stimulus –Organism–Response (S –O–R) model (Nian et al.,
2023), which explains how external stimuli in ﬂuence internal cognitive and emotional states, sub-
sequently driving behavioral responses. In digital marketing, AI-generated content such as perso-
nalized messages, chatbot interactions, and visual outputs serves as stimuli that shape consumer
perceptions (e.g., trust and relevance), leading to both affective and behavioral engagement out-
comes (Lim et al., 2022; Sun et al., 2025). This framework supports the distinction between affect-
ive and behavioral engagement as core dimensions of this review. Consumer responses to
AI-generated content are further shaped by perceptions of authenticity. The authenticity and effort
heuristic suggests that perceived human involvement in ﬂuences judgments of credibility and sin-
cerity. Accordingly, fully automated or explicitly disclosed AI-generated content may reduce per-
ceived authenticity and trust (Feng & Sun, 2025; Wen et al., 2025), whereas human –AI co-creation
can enhance emotional engagement and brand connection (Yang, 2025).
From a design perspective, human-centered AI (HCAI) (Floridi et al., 2018) emphasizes that AI
should augment rather than replace human creativity and judgment. This perspective underpins the
importance of HITL approaches, which improve contextual relevance, ethical alignment, and
engagement quality in AI-driven marketing (Yang, 2025; Sun et al., 2025). In addition,
Persuasion Knowledge Theory (Friestad & Wright, 1994) explains how consumers interpret
AI-generated persuasive content. When consumers recognize algorithmic intent, they may activate
persuasion knowledge, leading to more critical evaluation, and potential skepticism. This mechan-
ism highlights the role of AI disclosure as a key moderating factor in ﬂuencing engagement out-
comes (Sundari et al., 2025; Cillo & Rubera, 2025).
Collectively, these frameworks provide a theoretical foundation for this review. The S –O–R
model explains the distinction between affective and behavioral engagement, while authenticity
perceptions and persuasion knowledge account for variations in consumer responses. HCAI further
justiﬁes the role of HITL as a critical moderating factor. Together, these perspectives guide the
selection of focal variables and inform the interpretation of ﬁndings in subsequent sections of
the review. Building on this foundation, the following section outlines the systematic review
methodology.
Methodology
We conducted a systematic literature review following the PRISMA 2020 guidelines (Page et al.,
2021). The review focused on studies published between 2022 and October 2025, re ﬂecting the per-
iod during which GenAI technologies, such as LLMs, GANs, and diffusion models, gained sub-
stantial traction in digital marketing research and practice. Only peer-reviewed academic
sources, including journal articles and conference proceedings, were included to ensure the schol-
arly rigor of the evidence base. Searches were performed across major databases including Scopus,
Web of Science, ACM Digital Library, ScienceDirect, and Google Scholar. Additional full-text
access was obtained through ResearchGate and publisher websites where necessary.
The search strategy was designed to systematically capture relevant studies on GenAI in digital
marketing and its impact on customer engagement. A structured Boolean search approach was
employed, in which related terms within each concept were combined using the OR operator, while
different conceptual categories were linked using the AND operator.
The search string was structured as follows:
(“generative AI” OR “generative artiﬁcial intelligence” OR “ChatGPT” OR “large language model* ” OR
“AI-generated content”)
4 Emerging Media

AND
(“digital marketing ” OR “advertising” OR “social media marketing ” OR “online marketing ”)
AND
(“customer engagement ” OR “consumer engagement” OR “user engagement ”)
Searches were conducted across title, abstract, and keyword ﬁelds where supported by the
respective databases. Given the broad scope of results across databases, additional screening pro-
cedures, including duplicate removal, relevance screening, and full-text eligibility assessment, were
applied to ensure that only studies meeting the inclusion criteria were retained. This structured
approach ensured both comprehensiveness and reproducibility of the search process.
Table 1 summarizes the inclusion and exclusion criteria used to identify relevant studies for this
review. Only peer-reviewed, English-language publications from 2022 to October 2025 focusing
on GenAI in marketing and its impact on customer engagement were included. Both empirical
and conceptual works were considered. Studies on non-GenAI, purely technical model papers,
opinion articles, and inaccessible or non-English texts were excluded. Conceptual papers linking
GenAI with engagement moderators, such as AI disclosure or HITL were retained, while unrelated
or off-topic studies were removed.
Figure 1 summarizes the screening and selection process following the PRISMA 2020 protocol.
A total of 957 records were identiﬁed, with 142 removed as duplicates or out of scope. After screen-
ing and eligibility assessment, 33 studies met all inclusion criteria and were included in the ﬁnal
qualitative synthesis. This process ensures methodological rigor and transparency in study selec-
tion. Appendix 1 provides a comprehensive overview of these studies, outlining their focus, meth-
odological approach, marketing domain, and primary contribution to understanding how GenAI
inﬂuences customer engagement.
Results and discussion
The systematic review synthesized 33 peer-reviewed studies published between 2022 and October
2025, focusing exclusively on the application of GenAI in digital marketing contexts. Collectively,
Table 1. Inclusion and Exclusion Criteria.
Primary Data
Inclusion Exclusion
1. Studies on Gen AI in marketing or consumer
contexts
2. Address customer engagement outcomes
3. Empirical, conceptual, or review of studies
4. Peer-reviewed journals or conference papers
5. Published 2022 –2025
6. English language, full text available
1. Focus on non-GenAI (e.g., predictive analytics,
recommendation systems)
2. Technical model papers with no marketing or
consumer focus
3. Opinion of pieces, reports, or nonreviewed articles
4. Studies before 2022
5. Non-English or inaccessible full text
Secondary data
Inclusion Exclusion
1. Discuss generative AI and customer
engagement conceptually
2. Offer theoretical or integrative insights (e.g.,
disclosure, HITL)
1. No relevance to customer engagement
2. Not related to marketing/consumer context
Note. AI=artiﬁcial intelligence; HITL human-in-the-loop.
Pokhrel and Somasiri 5

these studies spanned advertising (33%), customer relationship management (21%), social media
and inﬂuencer marketing (18%), personalized content creation (15%), and digital branding and cus-
tomer experience (13%).
Empirical research dominated the corpus, with 43% employing quantitative designs, 31% using
qualitative or case-based approaches, and 26% offering conceptual or theoretical frameworks. In
terms of publication outlets, the reviewed studies were primarily published in peer-reviewed jour-
nals across marketing, information systems, and business disciplines, reﬂecting the interdisciplinary
nature of the ﬁeld.
With respect to temporal distribution, the reviewed studies exhibit a pronounced upward trajec-
tory over time. Of the 33 included studies, only 1 study (3%) was published in 2022, followed by a
modest increase to two studies (6%) in 2023. This growth accelerated in 2024 with six studies
(18%), culminating in a substantial concentration in 2025, which alone accounts for 24 studies
(73%) of the sample. This sharp rise re ﬂects the rapid advancement and widespread adoption of
GenAI technologies, particularly following the emergence and diffusion of large-scale GenAI tools
and platforms, which have signiﬁcantly intensiﬁed both academic inquiry and practical applications
in digital marketing contexts.
Geographically, the studies were concentrated in North America (39%) and Asia (34%), re ﬂect-
ing regions with early adoption of GenAI in marketing practice. A smaller proportion of studies
Figure 1. PRISMA literature screening and selection process.
6 Emerging Media

originated from Europe and other regions, indicating a broader international presence of research. In
terms of outcomes, Figure 2 shows that 61% examined behavioral engagement (e.g., click-
throughs, conversions, and purchases), 26% focused on affective outcomes (e.g., satisfaction, trust,
and authenticity), and 13% explored moderating factors such as AI disclosure and HITL collabor-
ation. Beyond these descriptive characteristics, a synthesis of the direction of ﬁndings across the
reviewed studies provides insight into the relative magnitude and consistency of reported effects.
The majority of studies examining behavioral engagement report positive outcomes, particularly
in terms of increases click-through rates, interaction levels, and conversation performance. In con-
trast, ﬁndings related to affective engagement are more heterogenous. While several studies report
improvements in satisfaction, enjoyment, and perceived innovation, others highlight reductions in
trust and authenticity, especially in contexts involving explicit AI disclosure or fully automated
content generation. Overall, this pattern indicates that behavioral engagement outcomes are gener-
ally positive across studies, whereas affective engagement outcomes are more context-dependent
and sensitive to consumer perceptions of authenticity and human involvement.
Figure 2 visually maps across two analytical dimensions: the type of engagement outcome
(affective vs. behavioral) and the presence of moderating factors (AI disclosure and HITL over-
sight). The evidence distribution shows a strong concentration of studies in the behavioral domain,
indicating that most research focuses on measurable actions such as clicks, shares, and purchase
intentions. Fewer studies address affective outcomes like trust, satisfaction, and emotional attach-
ment, while an even smaller cluster explicitly examines moderation effects, underscoring the need
for future research on how transparency and human collaboration shape engagement dynamics.
Thematic ﬁndings
Generative AI in content creation and brand communication. A prominent theme across literature is the
creative transformation of marketing communication through GenAI. LLMs like GPT 4/5, Llama,
Claude and image diffusion models such as DALL-E, MidJourney, Nano Banana from Google
Gemini enable the automation of ideation and content production at an unprecedented scale.
Studies (Sun et al., 2025; Wang, 2025) show that AI-generated advertisements perform comparably
to human-generated ones in engagement metrics, especially in low to mid-involvement product cat-
egories. AI-driven tools enhance message precision, stylistic adaptability, and real-time responsive-
ness to consumer feedback. However, authenticity of tension emerges as a limiting factor. In luxury
Figure 2. Generative AI in digital marketing studies.
Pokhrel and Somasiri 7

and creative domains, To et al. (2025) found that AI-generated messaging triggered skepticism and
reduced perceived brand sincerity when disclosed to audiences. Consumers associate exclusivity
with human craftsmanship and creativity, thus penalizing automation.
This underscores the dual nature of GenAI in brand communication, a source of scale and speed,
but one requiring strategic curation to sustain human warmth and narrative integrity.
The framework in Figure 3 illustrates how GenAI inputs such as LLMs, GANs, and diffusion
systems shape customer engagement outcomes through various mechanisms like personalization,
creativity, and interactivity. These mechanisms in ﬂuence both effective (trust, satisfaction, and
emotional connection) and behavioral (clicks, shares, and purchases) engagement. The framework
also highlights two moderate factors. AI disclosure, which affects customer perceptions of authen-
ticity and transparency, and human oversight, which ensures ethical, brand-aligned, and emotion-
ally resonant communication. Together, these elements explain how human –AI collaboration and
strategic transparency can maximize engagement effectiveness in digital marketing.
(A) Personalization and Adaptive Marketing
Personalization emerged as the most consistent engagement driver. Through LLMs and multi-
modal generation, GenAI enables microsegmentation and hyper-personalized messaging at an indi-
vidual level. Empirical studies (Qi et al., 2025; Lou & Copeland, 2025) demonstrate that AI-driven
Figure 3. Conceptual framework on Generative AI in ﬂuence on customer engagement.
8 Emerging Media

personalization increases consumer satisfaction, attention, and loyalty by aligning message tone
and imagery with consumer ’s emotional and situational contexts.
For instance, in social commerce, GenAI-powered recommendation engines dynamically gener-
ate tailored visuals or captions that mirror user sentiment, signi ﬁcantly increasing conversion rates
and click-through performance. Nevertheless, over-personalization introduces privacy and ethical
risks. Bijalwan et al. (2025) observed that users expressed discomfort when AI-generated messages
felt overly intrusive or when the logic behind personalization was opaque. This calls for transparent
explainability (XAI) and consent-based personalization protocols, ensuring ethical and sustained
engagement.
The reviewed studies conceptualized engagement along two axes, affective (emotional) and
behavioral (action-based), each revealing distinct effects of GenAI.
1. Affective engagement
Generative systems stimulate positive emotions such as curiosity, delight, and enjoyment when
they deliver novelty or humor (Kim et al., 2025). However, repeated exposure to AI-created content
may evoke “synthetic fatigue, ” where consumers feel emotionally detached due to over-
automation. AI chatbots eliciting empathy and human-like interaction, as shown by Qi et al.
(2025), outperform transactional bots in eliciting emotional attachment and satisfaction.
2. Behavioral engagement
GenAI-driven campaigns are often associated with improvements in behavioral engagement
indicators, including higher click-through rates, shares, and conversion outcomes (Sun et al.,
2025; Feng & Sun, 2025). Co-creative platforms, where users help design or re ﬁne AI-generated
visuals, further amplify engagement through a sense of ownership and participation. Overall, affect-
ive engagement remains more context-dependent, while behavioral outcomes show universal uplift
across sectors, particularly when personalization depth and esthetic novelty are optimized.
Figure 4 illustrates how collaboration, creation, and communication interact in a human-guided
process to optimize AI-driven marketing. It highlights the balance between human oversight and AI
capability where collaboration ensures strategic alignment, creation drives data-informed personal-
ization, and communication sustains emotional and contextual engagement across channels.
(B) Moderating Factors: AI Disclosure, Human-in-the-Loop, and Ethics
1. AI disclosure
Findings converge on the paradox of transparency. Disclosure enhances perceived honesty and
ethical responsibility (Li et al., 2024) but can also diminish perceived authenticity and trust if con-
sumers interpret automation as low effort. Context matters in technology and service brands, dis-
closure boosts credibility; in experience-based or luxury contexts, it erodes it (To et al., 2025).
Marketers should therefore employ framed transparency, such as emphasizing AI ’s supportive
rather than substitutive role (e.g., “AI-assisted creativity ” instead of “AI-generated”).
Pokhrel and Somasiri 9

2. Human-in-the-loop
Studies (Stanikzai & Mittal, 2025; Sun et al., 2025) unanimously report that hybrid human –AI
workﬂows outperform fully automated systems in both engagement quality and ethical perception.
Human moderation ensures emotional resonance, contextual accuracy, and brand tone alignment,
dimensions often missing in unsupervised outputs.
3. Ethical considerations
Ethical governance of GenAI is critical for sustainable engagement. Liao (2025b) highlights
issues such as bias in training data, misinformation, and consent ambiguity. Ethical lapses can pro-
duce not just disengagement but active backlash, damaging brand credibility. Thus, human
Figure 4. The human guided 3C framework for Generative AI enhanced marketing.
10 Emerging Media

oversight is not just an operational control but an ethical imperative. Figure 5 demonstrates how
optimal customer engagement emerges from the synergy between the AI layer, which enables auto-
mated, data-driven personalization, and the human layer, which provides empathy, ethical judg-
ment, and creative curation. The integration of both layers fosters greater trust, satisfaction, and
long-term loyalty in digital marketing interactions.
(C) Organizational and Strategic Transformation
Beyond customer outcomes, GenAI reshapes the internal logic of marketing organizations.
Rodriguez and Trainor (2025) and Sundari et al. (2025) found that GenAI integration rede ﬁnes mar-
keting as a data-creativity symbiosis, enhancing productivity while transforming job roles from exe-
cution to orchestration. Marketers increasingly function as prompt engineers and AI curators,
blending human creativity with algorithmic intelligence. This recon ﬁguration enhances strategic
agility and campaign ef ﬁciency by up to 50% (Singla et al., 2025) allowing teams to allocate
more time to analytics, ideation, and experimentation.
However, these organizational bene ﬁts depend on governance frameworks that address cultural
sensitivity, bias mitigation, and AI explainability. Firms investing in ethical infrastructure and AI
literacy report stronger brand resilience and higher consumer trust.
Building on the theoretical foundations outlined in the second section, the reviewed studies
reﬂect several key theoretical perspectives that underpin GenAI-driven customer engagement.
Rather than introducing new frameworks, this section synthesizes how existing theories are
reﬂected in the empirical ﬁndings. Tables 2 and 3 summarize these theoretical perspectives guided
both the interpretation of ﬁndings and the synthesis of engagement outcomes across the reviewed
studies.
Together, these theories establish a multidimensional foundation for understanding AI-enabled
engagement. The S –O–R model clari ﬁes the psychological pathway through which AI content
inﬂuences emotions and behaviors. The Authenticity and Effort Heuristic introduce a perceptual
lens, highlighting how human –AI collaboration shapes authenticity. Finally, HCAI adds an ethical
dimension, emphasizing the need for human oversight, empathy, and creativity in technology-
Figure 5. The power of human –AI synergy in customer engagement.
Pokhrel and Somasiri 11

mediated engagement. Collectively, they provide a conceptual bridge between technological medi-
ation, emotional cognition, and ethical co-creation in marketing.
Building on these theoretical foundations, the following managerial strategies translate concep-
tual insights into actionable practices for marketers seeking to implement GenAI responsibly and
effectively.
These strategies reposition marketing practice from AI-driven automation toward human –AI
symbiosis. They ensure that GenAI operates as an extension of human creativity and moral intel-
ligence rather than a replacement. By embedding ethical oversight, strategic transparency, and
Table 2. Theoretical Lenses Underpinning Generative AI-Driven Engagement.
Theoretical Lens Core Principle Application Within Generative AI Context
Stimulus Organism
Response (S–O–R)
Model
External stimuli in ﬂuence internal
emotional and cognitive states,
which in turn drive behavioral
responses
Generative AI outputs, such as
personalized ads, chatbot dialogue, and
AI-generated imagery serve as stimuli
that trigger affective and cognitive
engagement, leading to actions like
purchases, shares, or recommendations
Authenticity and effort
heuristic
Consumers evaluate sincerity and
authenticity based on perceived
human effort and involvement
Visible human editing or co-creation in AI
content signals authenticity, whereas
fully automated messages may seem
artiﬁcial or low-effort
Human-centered AI
(HCAI)
AI should augment human creativity
and moral reasoning rather than
replace them
When AI is designed to enhance human
intuition and empathy, it fosters ethically
grounded, emotionally resonant
engagement experiences
Table 3. Managerial Strategies Derived From Theoretical Foundations.
Strategic Focus
Managerial Action/Implementation
Approach Intended Organizational Outcome
Hybrid creativity
models
Combine AI-generated content with human
reﬁnement and emotional editing to
ensure expressiveness and brand
consistency
Achieve operational ef ﬁciency while
preserving emotional authenticity
and creative quality
Strategic disclosure
of AI use
Communicate AI involvement transparently
but positively, position AI as a co-creator
rather than a substitute for human
creativity
Enhance consumer trust and
acceptance of AI-driven marketing
AI literacy and
prompt
competence
Provide continuous training for marketers in
prompt engineering, model evaluation, and
ethical AI use
Strengthen creative control, reduce
bias, and improve campaign
outcomes
Ethical governance
frameworks
Institutionalize AI ethics policies, bias audits,
and data accountability systems
Maintain fairness, compliance, and
long-term consumer con ﬁdence in
AI-mediated engagement
12 Emerging Media

creative collaboration, organizations can harness AI ’se f ﬁciency while sustaining authenticity,
empathy, and trust, the cornerstones of lasting consumer engagement.
Conclusion
This systematic review offers a consolidated understanding of how GenAI is transforming digital
marketing and customer engagement across both affective (emotional) and behavioral dimensions.
By synthesizing insights from 33 peer-reviewed studies (2022 –2025), the review demonstrates that
GenAI facilitates scalable personalization, creative automation, and interactive communication,
collectively enhancing the quality, relevance, and immediacy of marketing engagement.
However, the analysis also uncovers critical contextual and ethical complexities. While behav-
ioral engagement manifested through increased clicks, shares, and conversions, is consistently
strengthened, affective outcomes such as trust, satisfaction, and authenticity remain conditional
and fragile. These emotional responses depend heavily on the perceived transparency of AI use
and the degree of human oversight in creative processes. The moderating role of AI disclosure
and HITL integration emerges as central: disclosure requires contextual nuance to avoid reactance,
whereas human collaboration ensures moral integrity and emotional resonance.
From a theoretical perspective, this study extends the S –O–R) model, the Authenticity –Effort
Heuristic, and HCAI paradigms, positioning GenAI not merely as a technological tool but as a socio-
cognitive actor that mediates emotion, meaning, and ethics in marketing ecosystems. From a man-
agerial standpoint, the ﬁndings urge organizations to adopt strategic transparency, hybrid creativity
models, and ethical governance mechanisms. Marketers must evolve from users of AI technologies
to architects of human–AI co-creative systems, capable of delivering personalization without eroding
authenticity or trust. Cultivating AI literacy, prompt-craft competence, and bias-aware governance is
essential to sustain ethical and emotionally intelligent engagement at scale.
Future research directions
Despite its contributions, this review highlights several avenues for future inquiry:
 Longitudinal impact of GenAI engagement: Future studies should examine how sustained
exposure to AI-mediated interactions in ﬂuences brand loyalty, emotional attachment, and
consumer fatigue over time.
 Cross-cultural and demographic variations: Understanding how cultural norms, values, and
technological trust shape consumer responses to GenAI can re ﬁne global marketing
strategies.
 Ethical and psychological implications of synthetic media: As AI-generated images, voices,
and personas become ubiquitous, research should explore their effects on authenticity, per-
ception, identity, and persuasion ethics.
 Multimodal AI and immersive marketing: Emerging GenAI systems that blend text, image,
and video (e.g., multimodal agents) warrant examination for their potential to create emo-
tionally immersive yet ethically complex engagement environments.
Ultimately, GenAI does not replace human creativity, it rede ﬁnes it. When guided by empathy,
ethics, and imagination, GenAI can transform marketing into a shared human –machine narrative,
one that is ef ﬁcient yet authentic, data-driven yet emotionally intelligent, and technologically
advanced yet profoundly human.
Pokhrel and Somasiri 13

Acknowledgments
For the purpose of open access, the authors have applied a Creative Commons Attribution (CC BY) licence to
any Author Accepted Manuscript version arising from this submission. For improved ﬂow, grammar, and clar-
ity of this report, we have utilized generative AI tools, including GPT-5 and Claude Sonnet 4. However, the
conception of ideas, research design, critical analysis, and in-depth review are entirely our own.
ORCID iD
Sangita Pokhrel https:/ /orcid.org/0009-0008-2092-7029
Ethical considerations
This study is a systematic literature review based solely on previously published and publicly available
sources. It does not involve human participants or primary data collection; therefore, institutional ethical
approval and informed consent were not required. Ethical standards were maintained through accurate citation,
transparency, and responsible synthesis of the reviewed literature.
Funding
The authors disclosed receipt of the following ﬁnancial support for the research, authorship, and/or publication
of this article: This work was supported by the York St John Unive.
Declaration of con ﬂicting interests
The authors declared no potential con ﬂicts of interest with respect to the research, authorship, and/or publica-
tion of this article.
References
Ali, L., Ali, F., Abdalla, M. J., & Alotaibi, S. (2025). Beyond the hype: Evaluating the impact of generative AI
on brand authenticity, image, and consumer behavior in the restaurant industry. International Journal of
Hospitality Management, 131, Article 104318 https:/ /doi.org/10.1016/j.ijhm.2025.104318
Bijalwan, P., Gupta, A., Johri, A., Wasiq, M., & Wani, S. K. (2025). Unveiling Sora OpenAI ’s impact: A
review of transformative shifts in marketing and advertising employment. Cogent Business &
Management, 12(1), Article 2440640 https:/ /doi.org/10.1080/23311975.2024.2440640
Chung, K. C. (2025). The evolution of creativity: How generative AI is reshaping the hospitality landscape.
Enterprise Information Systems , 19(3–4), Article 2427024 https:/ /doi.org/10.1080/17517575.2024.
2427024
Cillo, P., & Rubera, G. (2025). Generative AI in innovation and marketing processes: A roadmap of research
opportunities. Journal of the Academy of Marketing Science , 53(3), 684 –701 https:/ /doi.org/10.1007/
s11747-024-01044-7
Dang, S., Quach, S., & Roberts, R. E. (2025). Human-generative AI interaction: Assessing futureprooﬁng attri-
butes from time perspectives and temporal distances. International Journal of Human –Computer
Interaction, 42(10), 7112–7141 https:/ /doi.org/10.1080/10447318.2025.2556233
Feng, Y., & Sun, Y. (2025). Consumer empowerment through generative arti ﬁcial intelligence: Enhancing
brand narrative with collaboration, creation, and communication. International Journal of Advertising ,
45(1), 229–261 https:/ /doi.org/10.1080/02650487.2025.2547545
Floridi, L., Cowls, J., Beltrametti, M., Chatila, R., Chazerand, P., Dignum, V., Luetge, C., Madelin, R.,
Pagallo, U., Rossi, F., Schafer, B., Valcke, P., & Vayena, E. (2018). AI4People —an ethical framework
for a good AI society: Opportunities, risks, principles, and recommendations. Minds and Machines ,
28(4), 689–707 https:/ /doi.org/10.1007/s11023-018-9482-5
14 Emerging Media

Friestad, M., & Wright, P. (1994). The persuasion knowledge model: How people cope with persuasion
attempts. Journal of Consumer Research , 21(1), 1 –31 https:/ /doi.org/10.1086/209380
Gołąb-Andrzejak, E. (2023). The impact of generative AI and ChatGPT on creating digital advertising cam-
paigns. Cybernetics and Systems , 56(8), 1130–1144 https:/ /doi.org/10.1080/01969722.2023.2296253
Hussain, K., Khan, M. L., & Malik, A. (2024). Exploring audience engagement with ChatGPT-related content
on YouTube: Implications for content creators and AI tool developers. Digital Business , 4(1), Article
100071 https:/ /doi.org/10.1016/j.digbus.2023.100071
Joshi, S., Bhattacharya, S., Pathak, P., Natraj, N. A., Saini, J., & Goswami, S. (2025). Harnessing the potential
of generative AI in digital marketing using the behavioral reasoning theory approach. International Journal
of Information Management Data Insights , 5(1), Article 100317 https:/ /doi.org/10.1016/j.jjimei.2024.
100317
Kim, J. S., Kim, M., & Baek, T. H. (2025). Enhancing user experience with a generative AI chatbot.
International Journal of Human –Computer Interaction , 41(1), 651 –663 https:/ /doi.org/10.1080/
10447318.2024.2311971
Krowinska, A., & Dineva, D. (2025). The role and forms of social media branded content driving active cus-
tomer engagement behaviours. Journal of Marketing Management , 41(9–10), 1030 –1060 https:/ /doi.org/
10.1080/0267257X.2025.2544808
Kshetri, N., Dwivedi, Y. K., Davenport, T. H., & Panteli, N. (2024). Generative arti ﬁcial intelligence in mar-
keting: Applications, opportunities, challenges, and research agenda. International Journal of Information
Management, 75, Article 102716 https:/ /doi.org/10.1016/j.ijinfomgt.2023.102716
Lai Cheung, M., Pires, G. D., Rosenberger, P. J., Leung, W. K. S., & Attia, S. (2024). Exploring the theory of
consumer-engagement marketing: Antecedents and consequences of consumers ’ participative and engage-
ment behaviours. Journal of Strategic Marketing , 32(8), 1444 –1459 https:/ /doi.org/10.1080/0965254X.
2024.2404841
Li, T. G., Zhang, C. B., Chang, Y., & Zheng, W. (2024). The impact of AI identity disclosure on consumer
unethical behavior: A social judgment perspective. Journal of Retailing and Consumer Services , 76,
Article 103606, https:/ /doi.org/10.1016/j.jretconser.2023.103606
Liao, T. H. (2025a). Relationships between motivated consumer innovativeness, consumer AI usage experi-
ence, and consumer commitment: A comparative analysis across four arti ﬁcial intelligence devices.
International Journal of Human –Computer Interaction , 42(3), 1597 –1614 https:/ /doi.org/10.1080/
10447318.2025.2526567
Liao, T. H. (2025b). The importance of human interactivity in arti ﬁcial intelligence use in advertising:
Development of a new scale. International Journal of Advertising , 45(1), 193 –228 https:/ /doi.org/10.
1080/02650487.2025.2541505
Lim, R. E., Kim, S., Abernathy, A., Shin, S., & Avance, R. (2025). Excited or anxious about adopting gen-
erative AI? Investigating the drivers of generative AI adoption among advertising creatives. Journal of
Marketing Communications ,1 –24. https:/ /doi.org/10.1080/13527266.2025.2497259
Lim, W. M., Rasul, T., Kumar, S., & Ala, M. (2022). Past, present, and future of customer engagement.
Journal of Business Research , 140, 439–458 https:/ /doi.org/10.1016/j.jbusres.2021.11.014
Lou, X., & Copeland, L. (2025). Gen Z and AI-generated fashion ads: A qualitative study to understanding
female consumer perceptions and reactions. Journal of Internet Commerce , 24(3), 131 –152 https:/ /doi.
org/10.1080/15332861.2025.2520194
Nian, S., Li, D., Zhang, J., Lu, S., & Zhang, X. (2023). Stimulus-organism-response framework: Is the per-
ceived Outstanding Universal Value attractiveness of tourists bene ﬁcial to World Heritage Site conserva-
tion? International Journal of Environmental Research and Public Health , 20(2), Article 1189 https:/ /doi.
org/10.3390/ijerph20021189
Pokhrel and Somasiri 15

Page, M. J., Moher, D., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., Shamseer, L., Tetzlaff,
J. M., Akl, E. A., Brennan, S. E., Chou, R., Glanville, J., Grimshaw, J. M., Hróbjartsson, A., Lalu, M. M.,
Li, T., Loder, E. W., Mayo-Wilson, E., McDonald, S., & McKenzie, J. E. (2021). PRISMA 2020 explan-
ation and elaboration: Updated guidance and exemplars for reporting systematic reviews. BMJ, 372, Article
n160 https:/ /doi.org/10.1136/bmj.n160
Prasanna, A., & Kushwaha, B. P. (2025). Transforming marketing landscapes: A systematic literature review
of generative AI using the TCCM model framework. Management Review Quarterly , 76, 421–455 https:/ /
doi.org/10.1007/s11301-025-00486-9
Qi, L., Cho, M., & Ko, E. (2025). Emotional and functional values of generative AI in fashion: Effects on user
satisfaction and continued use. International Journal of Human–Computer Interaction, 42(10), 7591–7608
https:/ /doi.org/10.1080/10447318.2025.2560517
Rahmani, V. (2023). Persuasion knowledge framework: Toward a comprehensive model of consumers ’ per-
suasion knowledge. AMS Review , 13(1–2), 12–33 https:/ /doi.org/10.1007/s13162-023-00254-6
Rezazadeh, A., Kohns, M., Bohnsack, R., António, N., & Rita, P. (2025). Generative AI for growth hacking:
How startups use generative AI in their growth strategies. Journal of Business Research , 192, Article
115320 https:/ /doi.org/10.1016/j.jbusres.2025.115320
Rodriguez, M., & Trainor, K. J. (2025). Integrating generative arti ﬁcial intelligence (GenAI) in a professional
selling course: Application of prompt engineering. Marketing Education Review ,1 –12. https:/ /doi.org/10.
1080/10528008.2025.2507682
Singla, A., Sukharevsky, A., Yee, L., Chui, M., & Hall, B. (2025, March 12). The state of AI: How organiza-
tions are rewiring to capture value . QuantumBlack, AI by McKinsey. https:/ /www.mckinsey.com/
capabilities/quantumblack/our-insights/the-state-of-ai-how-organizations-are-rewiring-to-capture-value
Stanikzai, M. E., & Mittal, E. (2025). Leveraging AI-generated and human-generated content for maximized
user engagement in contentpreneurs ’ innovation and creativity. Journal of Innovation and
Entrepreneurship, 14(1), Article 91 https:/ /doi.org/10.1186/s13731-025-00529-1
Sun, L., An, Y., Song, X., & Liu, J. (2025). Human vs. AI in creative contests: A study on the effectiveness of
advertisement copy generated by Chinese large language models. Electronic Commerce Research . https:/ /
doi.org/10.1007/s10660-025-09990-2
Sundari, M. H., Parhana, R., Santhanalakshmi, K., & Haridharan, K. N. (2025) Arti ﬁcial intelligence in digital
marketing: A systematic review and strategic framework for AI-augmented marketing. International
Research Journal on Advanced Engineering and Management 3 (8): 2595 –2611. https://doi.org/10.
47392/IRJAEM.2025.0410.
To, R. N., Wu, Y. C., Kianian, P., & Zhang, Z. (2025). When AI doesn ’t sell Prada: Why using AI-generated
advertisements back ﬁres for luxury brands. Journal of Advertising Research , 65(2), 202 –236 https:/ /doi.
org/10.1080/00218499.2025.2454120
van Berlo, Z. M. C., Campbell, C., & Voorveld, H. A. M. (2024). The MADE framework: Best practices for
creating effective experimental stimuli using generative AI. Journal of Advertising, 53(5), 732–753 https:/ /
doi.org/10.1080/00913367.2024.2397777
Wang, Z. (2025). Human vs. ChatGPT: Language of advertising in beauty products advertisements [Review
of the book Human vs. ChatGPT: Language of advertising in beauty products advertisements , by I. Skubis
&D .K ołodziejczyk]. Asia Paciﬁc Business Review,1 –4. https:/ /doi.org/10.1080/13602381.2025.2471364
Wen, X., Niu, Y., & Liao, C. (2025). U-shaped effect of color in short-form video: Combination of text, audio,
image ML, and generative AI. Journal of Business Research, 192, Article 115278 https:/ /doi.org/10.1016/j.
jbusres.2025.115278
Yang, J. (2025). Exploring the productivity of generative AI-powered ad campaigns: A consumer response
perspective. Journal of Interactive Advertising , 25(3), 222 –239 https:/ /doi.org/10.1080/15252019.2025.
2551598
16 Emerging Media

Appendix 1
Source Theme/Focus Area
Methodology/
Sample
Engagement
Outcome(s)
Key Insights/
Contribution
Sundari et al., 2025;
Lai Cheung et al.,
2024; Lim et al.,
2022; Singla et al.,
2025; Li et al.,
2024; Cillo &
Rubera, 2025; Nian
et al., 2023
Foundational and
integrative
studies on
generative AI in
marketing and
customer
engagement
Conceptual/
review
Affective &
behavioral
These studies provide
insights into
generative AI in
marketing,
supporting
engagement,
adoption, and
moderating factors
To et al., 2025 Luxury brand
marketing and AI
disclosure
Experimental (2 ×
2 design; AI vs.
human ads)
Affective &
behavioral
AI ads lower
perceived luxury
and authenticity;
partial AI disclosure
moderates trust
and purchase intent
Feng & Sun, 2025 Co-creation &
empowerment
through GenAI
Conceptual
model based
on value
co-creation
frameworks
Affective &
behavioral
Proposes
collaborative
AI-consumer model
linking creation and
engagement;
enhances brand
narratives
van Berlo et al., 2024 Experimental
design using
GenAI stimuli
Methodological
paper using
multiple ad
prototypes
(n ≈ 400)
Not directly
measured—
enables valid
future
research
Introduces MADE
framework for valid
AI stimuli creation
in advertising
experiments
Joshi et al., 2025 Drivers and
barriers to
GenAI adoption
by marketers
Quantitative
survey (n = 312
marketing
professionals)
Behavioral
(usage
intention)
Behavioral Reasoning
Theory links
motives and
barriers to GenAI
adoption in
marketing contexts
Ali et al., 2025 Brand authenticity
& AI use in
hospitality
marketing
Empirical survey
(n = 512
consumers)
Affective &
behavioral
AI content enhances
innovation
perception but
reduces
authenticity for
experience-driven
brands
Wen et al., 2025 Visual design &
attention in
AI-generated ads
Experimental
(multi-modal
stimuli test)
Behavioral
(attention,
CTR)
Finds U-shaped
relationship
between
AI-assisted color
use and attention
levels
(continued)
Pokhrel and Somasiri 17

Continued.
Source Theme/Focus Area
Methodology/
Sample
Engagement
Outcome(s)
Key Insights/
Contribution
Hussain et al., 2024 Audience reactions
to AI content on
social media
Content analysis
of YouTube
videos
(n ≈ 500)
Behavioral
(views,
comments,
shares)
Viewers show high
behavioral
engagement driven
by curiosity and
learning motives
Chung, 2025 Creativity and AI in
hospitality
branding
Case studies of 5
hospitality
brands
Affective
(satisfaction,
trust)
GenAI drives creative
innovation but
needs human
oversight for
authenticity and
trust
Rezazadeh et al., 2025 Startup marketing
& AI growth
strategies
Survey +
interviews (n =
250 startups)
Behavioral
(engagement
metrics,
conversion)
Startups use GenAI
for content
automation and
personalization to
boost conversion
and retention
Liao, 2025b Human interactivity
and AI ads
Scale
development
survey
(n = 420)
Affective &
behavioral
Introduces validated
scale linking human
touch in AI ads to
greater trust and
positive affect
Yang, 2025 Productivity &
effectiveness of
AI ads
Experimental
survey (n = 310
respondents)
Behavioral
(CTR,
purchase
intent)
AI ads increase
attention and clicks
but can reduce
authenticity
perception in some
segments
Dang et al., 2025 Perceptions of
future AI
systems in
marketing
Experimental
design
(3 scenarios)
Affective (trust)
& behavioral
(intent)
Perceived
future-orientation
of AI tools boosts
trust and
engagement intent
when time distance
is short
Krowinska & Dineva,
2025
Branded content
and AI-assisted
social media
marketing
Mixed methods
survey +
content
analysis
Behavioral
(clicks, shares,
comments)
AI-aided content
planning and timing
enhance interactive
and participatory
engagement
Prasanna &
Kushwaha, 2025
Meta-analysis of
GenAI research
themes
Systematic
literature
review
(2018–2025)
Synthesized
affective &
behavioral
Identiﬁes three
dominant themes:
personalization,
automation, and
ethics; calls for
HITL models
(continued)
18 Emerging Media

Continued.
Source Theme/Focus Area
Methodology/
Sample
Engagement
Outcome(s)
Key Insights/
Contribution
Gołąb-Andrzejak,
2023
Digital advertising
creation using
ChatGPT and
GenAI
Conceptual
analysis +
industry
examples
Behavioral
(creative
output,
engagement)
Explains how
ChatGPT-driven
ads enhance
efﬁciency and
creative
experimentation in
campaign design
Lim et al., 2025 Adoption drivers
among
advertising
professionals
Quantitative
survey ( n = 260
creatives)
Affective
(adoption
attitude) &
behavioral
(intention)
Finds that creative
self-efﬁcacy and
usefulness increase
AI adoption; anxiety
reduces
engagement
readiness
Liao, 2025a Consumer
innovativeness
and AI usage
behavior
Comparative
survey (n = 480
AI users)
across four AI
platforms
Affective
(commitment,
trust) &
behavioral
(usage
intensity)
Demonstrates that
motivated
innovation and
positive AI usage
experience increase
consumer
commitment and
continued
engagement with AI
tools
Kshetri et al., 2024 Comprehensive
overview of
GenAI
applications in
marketing
Conceptual
review +
industry
examples
Synthesized
(affective &
behavioral)
Identiﬁes practical
applications of
LLMs, GANs, and
diffusion models in
marketing; calls for
ethics-aligned
engagement
frameworks and
HITL oversight
Sun et al., 2025; Qi
et al., 2025; Wang,
2025; Lou &
Copeland, 2025;
Bijalwan et al.,
2025
AI-generated
advertising,
personalization,
and consumer
perception
Mixed
(experimental,
survey,
qualitative)
Affective &
behavioral
These studies show
that AI-generated
content can match
or outperform
human-created
content in
engagement, while
highlighting the role
of personalization
and concerns
around perceived
authenticity and
intrusiveness
Kim et al., 2025;
Stanikzai & Mittal,
AI-driven user
experience,
Empirical/
conceptual
Affective &
behavioral
These studies
emphasize
(continued)
Pokhrel and Somasiri 19

Continued.
Source Theme/Focus Area
Methodology/
Sample
Engagement
Outcome(s)
Key Insights/
Contribution
2025; Rodriguez &
Trainor, 2025
chatbot
interaction, and
ethical
considerations
emotional
engagement, ethical
AI use, and the
importance of
human oversight in
sustaining trust and
long-term
engagement
Note.A I=artiﬁcial intelligence; CTR=click-through rate; GAN= generative adversarial networks; HITL= human-in-the-loop;
LLM=large language model; MADE=mapping, assembling, demonstrating, executing.
20 Emerging Media
