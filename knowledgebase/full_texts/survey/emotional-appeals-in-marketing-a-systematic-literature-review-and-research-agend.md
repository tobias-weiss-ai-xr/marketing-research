---
title: 'Emotional appeals in marketing: a systematic literature review and research agenda'
url: https://doi.org/10.1007/s43039-026-00136-2
category: survey
subcategory: empirical
date: 2026-06
venue: Italian Journal of Marketing
authors:
- Seyed Mohammad Mirmahdi Komejani
- Ricardo Godinho Bilro
- Sandra María Correia Loureiro
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1007/s43039-026-00136-2.pdf
pages: 39
chars: 121459
fetched_at: '2026-11-08T18:41:01+00:00'
kb_version: 1
---

# Emotional appeals in marketing: a systematic literature review and research agenda

REVIEW ARTICLE
Italian Journal of Marketing         (2026) 2026:13
https://doi.org/10.1007/s43039-026-00136-2
  Ricardo Godinho Bilro
bilro.ricardo@gmail.com
1 Instituto Universitário de Lisboa (ISCTE-IUL), Business Research Unit (BRU-IUL),
Lisboa, Portugal
Received: 6 September 2025 / Accepted: 4 May 2026
© The Author(s) 2026
Emotional appeals in marketing: a systematic literature
review and research agenda
Seyed Mohammad Mirmahdi Komejani1 · Ricardo Godinho Bilro1  ·
Sandra Maria Correia Loureiro1
Abstract
This study presents a comprehensive synthesis of the literature on emotional ap -
peals in marketing, conducted through a systematic review of 136 peer-reviewed
articles retrieved from the Web of Science and Scopus. Using data mining and topic
modelling techniques in R, the analysis uncovers 14 latent thematic clusters that
reflect the evolving role of emotions across domains such as advertising, branding,
consumer engagement, and digital media. Beyond mapping existing contributions,
the study addresses conceptual fragmentation and terminological inconsistencies
by proposing an integrative framework that connects emotional constructs across
strategic and operational marketing contexts. A key outcome of this review is the
development of a structured research agenda that identifies underexplored areas,
such as collective emotional processing, real-time engagement on digital platforms,
and emotional branding in emerging sectors, and offers direction for future theoreti -
cal and empirical work. Additionally, this paper offers a framework structured using
the TCM (Theory–Characteristics–Methodology) model, which helps position the
identified gaps and suggests actionable pathways for advancing research in the field.
By consolidating scattered insights and systematising future research priorities, this
study contributes as a roadmap for scholars seeking to deepen their understanding
of how emotions influence the dynamics in the increasingly complex marketing
environment.
Keywords Emotional appeals · Emotional marketing · Systematic literature
review · Topic modelling · Consumer-brand relationships · Research agenda

1 3
   13  Page 2 of 39
Italian Journal of Marketing         (2026) 2026:13
1 Introduction
Emotions are affective responses triggered by stimuli and shaped by individuals’
appraisals of their environment, reflecting a form of cognitive readiness (Bagozzi
et al., 1999). They involve both positive sensations and disruptive feelings (Lee et
al., 2009). In marketing, interest in emotions has intensified as companies seek to
build durable bonds between brands and consumers (Shahid et al., 2022). Emotional
cues are known to capture attention, and consumer behaviour is often guided more
by emotional states than by rational evaluation (Hudson et al., 2015). For instance,
emotionally charged headline language can be subconsciously processed, attracting
attention even when consumers are distracted (Nielsen et al., 2010).
Prior marketing literature identifies a wide range of emotional responding in mar-
ket settings. Men, for instance, may exhibit heightened arousal when exposed to
advertisements featuring attractive women (Van Den Bergh et al., 2008). Emotional
cues can also shape product experiences, such as by enhancing perceived taste and
increasing the appeal of fast food (Effertz et al., 2019). Similarly, luxury-associated
coffee brands can evoke strong emotional engagement (Li et al., 2022). However,
emotional reactions are not uniform, and consumer characteristics, including age,
condition how individuals respond to stimuli (Williams & Drolet, 2005).
Despite extensive evidence supporting emotional appeals (Erevelles, 1998), their
effects remain a subject of debate. Emotional messaging does not always generate
positive outcomes and may instead cause resistance or alienation, resulting in brand
avoidance (Rahimah et al., 2023). When executed effectively, however, emotional
connections can strengthen long-term brand relationships. Emotionally connected
consumers are more willing to forgive corporate transgressions, whereas weaker
emotional ties are associated with more critical responses (Park & Nunes, 2025). At
the same time, emotionally charged advertising has been linked to stronger engage -
ment and memorability through the joint activation of affective and cognitive path -
ways, including heightened reward-related responses (Adalarasu et al., 2025).
Even with this growing body of research on emotional appeals in marketing, sev-
eral gaps persist. First, the literature offers limited precision in classifying emotional
appeals styles in business contexts. Many studies focus broadly on the distinction
between positive versus negative emotions, which may not capture the full com -
plexity of emotional dynamics. Second, while comparisons between emotional and
rational appeals are well established, there remains a need for more granular clas -
sifications of emotional appeals styles and their specific effects (Aeron & Rahman,
2025; Sharma et al., 2023). Third, although emotional appeals have been extensively
studied, a comprehensive synthesis of the marketing domains in which emotional
appeals have been most prominent is still missing. To address these gaps, this paper
offers a systematic review to clarifies how emotional appeals operate within market-
ing strategies and identifies where the literature is concentrated and where it remains
fragmented.
Whereas prior reviews have examined specific contexts, such as the service indus-
try (Arici et al., 2022) or sports sponsorship (Teal et al., 2020), this review adopts a
broader scope. It offers a comprehensive analysis of emotional dynamics in market -
ing, encompassing both short-term tactical applications and long-term strategic per -

1 3
Page 3 of 39    13
Italian Journal of Marketing         (2026) 2026:13
spectives. Unlike prior work that isolates individual emotions such as pride, shame,
or anger (Aeron & Rahman, 2025; Arici et al., 2022) or focuses narrowly on feelings
and moods (Kranzbühler et al., 2020), this study integrates these constructs into a
broader theoretical and practical marketing framework (see Table 1). Methodologi-
cally, we complement conventional review procedures with data-mining techniques
implemented in R software to enable systematic mapping and synthesis of academic
contributions. Moreover, by focusing on articles published in journals indexed in
Web of Science (WOS) and Scopus, we provide a rigorous evidence base that can
inform both theory development and future empirical work.
This study aims to bridge key gaps in the literature by synthesising and systematis-
ing the leading research on emotional appeals in marketing. Specifically, it identifies
core themes, evaluates conceptual progress, and proposes a structured roadmap for
future investigation. Its contribution unfolds across five dimensions: (1) offering a
holistic overview of existing literature, (2) employing data mining tools to extract
deeper insights, (3) identifying emerging trends and novel directions, (4) highlighting
critical research gaps and outlining a future agenda, and (5) developing an integra -
tive framework that consolidates foundational concepts from prior studies. Grounded
in the TCM framework (Theory, Characteristics, Methodology) (e.g., Aleem et al.,
2024; Bilro & Loureiro, 2020), we organise future research opportunities across
these three domains, offering a coherent map for advancing scholarship on emotional
appeals in marketing.
The remainder of this article is structured as follows. The next section outlines the
materials and methods. This is followed by a descriptive analysis of the literature and
a subsequent thematic analysis. The paper then presents the identified research gaps
and outlines a future research agenda. Finally, the conclusions and implications are
discussed.
2 Materials and methods
This study employs a systematic literature review (SLR) to examine the role of
emotional appeals in marketing. A SLR enables a rigorous and transparent synthesis
of prior academic research by following a predefined and replicable protocol. This
methodology is well suited for integrating fragmented evidence across domains and
for refining theoretical and methodological understanding (Christofi et al., 2017).
By consolidating diverse contributions, the review provides a comprehensive under-
standing of how emotional strategies are deployed within marketing contexts.
This review aims to clarify how emotional appeals are conceptualised and opera -
tionalised in the marketing literature, while identifying gaps and emerging trends
that can inform future research. To ensure rigour and relevance, we focus on peer
reviewed journal articles indexed in Web of Science (WoS) and Scopus, consistent
with established practice in recent reviews (Aleem et al., 2024). WoS and Scopus are
widely used bibliographic databases with selective coverage and established editorial
standards, supporting the identification of high-quality research (Clarivate, 2021).
Consistent with prior review protocols, we also treated journal outlets as a proxy for
quality when assessing the robustness and contribution of included studies (Bilro et

1 3
   13  Page 4 of 39
Italian Journal of Marketing         (2026) 2026:13
Authors Research
Method
Area Queries Criteria Databases Final
papers
(Kranzbüh-
ler et al.,
2020)
Meta
Analysis
Firm-customer
interactions
across various
business sectors
The search included broad emotion-related
terms such as “emotion*”, “feeling*”,
“affect*”, “mood*”, as well as specific
discrete emotions. Additionally, context-
specific keywords such as “customer*”,
“consumer*”, “service”, “shopping”, “re-
tail”, “store” were used to ensure relevance
to firm-customer interactions.
1. Studies should be related to firm-customer encoun-
ters (either real-life experiences, recalled experiences,
or experimental vignettes).
EBSCO
Business
Source
Premier, Web
of Science,
Google
Scholar
112
2. Articles should include attitudinal or behavioral
reactions to firm interactions, such as satisfaction,
purchase behavior, or word-of-mouth.
3. Only studies that manipulated or measured discrete
emotions were considered.
(Arici et al.,
2022)
Bibliomet-
ric Analysis
Service
Industry
‘anger’, ‘disgust’, ‘envy’, ‘jealousy’,
‘anxiety’, ‘fear’, ‘guilt’, ‘shame’, ‘relief’,
‘hope’, ‘sadness’, ‘depression’, ‘hap-
piness’, ‘pride’, ‘love’, ‘gratitude’,
‘compassion’.
1. Clear applicability to the service sector. Scopus 647
2. Studies on “emotions” published in 17 journals
specializing in service, tourism, and hospitality up
until December 31, 2021.
(Taqi et al.,
2025)
Systematic
Literature
Review
Different areas “Brand” + “Hate” 1. Articles published between 2009 and 2023
2. Only journal articles and conference papers were
considered
Web of Sci-
ence, Scopus,
Emerald
Insight,
EBSCO, Sci-
ence Direct,
and Wiley
86
Table 1 Reviews of literature focusing on emotion in business contexts

1 3
Page 5 of 39    13
Italian Journal of Marketing         (2026) 2026:13
Authors Research
Method
Area Queries Criteria Databases Final
papers
3. Inclusion of studies from all countries and
disciplines
4. Focus on articles explicitly discussing brand hate in
the marketing and consumer behavior context
(Teal et al.,
2020)
Literature
Review
Elite sports
sponsorships
Three levels were applied including
sponsorship (search terms: sponsorship,
event marketing, cause-related marketing,
advertising, marketing messages, social
marketing); sport/health (search terms:
sport, heath promotion, health campaign,
public service announcement, health mes-
sage, health communication, intention,
health behavior); emotions (search terms:
emotion, feel, affect, mood).
1. Studies published in peer-reviewed English journals
since 2000 until Oct 2018
2. Focus on sport sponsorship, health communication,
and emotions
PsychInfo,
ScienceDi-
rect, Web
of Science,
ProQuest,
Sport Discus,
Medline,
Communi-
cation and
Mass Media
Complete,
Emerald, and
EBSCO
39
For example (e.g. [sponsorship OR
market*mess* OR leverage* OR sport
brands] + [sport*ORevent*] + [emotion
ORaffectORfeel*])
3. Inclusion of studies where emotion was an inde-
pendent variable affecting behavioral intention or
health-related actions
4. Exclusion of review papers, conference papers, and
studies that did not analyze elite sports sponsorship
(Aeron &
Rahman,
2025)
Systematic
Literature
Review
Consumer
behavior and
marketing
Search Keywords: “emotion” OR “pride”
OR “proud”, OR “love” OR “shame” OR
“fear*” OR “anger*” OR “angry*” OR
“sad*” OR “happy*” OR “contentment*”.
1. Articles published between 1981 and 2023
2. Focused on business, management, and accounting
journals
3. Only English-language publications included
Scopus 453
Table 1 (continued)

1 3
   13  Page 6 of 39
Italian Journal of Marketing         (2026) 2026:13
Authors Research
Method
Area Queries Criteria Databases Final
papers
4. Journals ranked A or A* in the ABDC list and
ranked 4*,4 and 3 based on AJG
5. Studies had to directly refer to emotional states and
processes
6. Articles that only mentioned emotions superficially
or in unrelated contexts were excluded
Table 1 (continued)

1 3
Page 7 of 39    13
Italian Journal of Marketing         (2026) 2026:13
al., 2023). We searched WoS and Scopus for all eligible articles published up to 27
March 2025, without imposing an initial cut-off date. Consequently, the search was
constrained only by the timeline of the research process, allowing for the inclusion of
all relevant literature regardless of publication date. The review followed a five-phase
process comprising search strategy design, data collection, relevance screening, qual-
ity assessment, and synthesis.
The search was guided by three key expressions intended to capture various
dimensions of emotional marketing: “emotional marketing”, “emotional branding”,
and “emotional advertising”. These terms reflect different strategic and temporal ori-
entations within marketing, ranging from short-term advertising tactics to long-term
brand relationship strategies. In both databases, the search query was designed to
include the following terms with truncation: “emotion* marketing” OR “emotion*
advertis*” OR “emotion* brand*”. Only English-language articles published in peer-
reviewed academic journals with full-text availability were considered eligible for
inclusion. Additional inclusion criteria were applied to ensure disciplinary relevance,
with a focus on publications indexed under business, management, psychology, or
marketing-related fields.
The initial search returned 236 articles from Web of Science and 338 from Sco -
pus, resulting in a combined dataset of 574 records. These were then imported into a
master Excel file for organisation and validation. A case-by-case comparison of titles
and metadata was conducted to identify and remove duplicate entries. This process
eliminated 218 overlapping articles, reducing the dataset to 356 unique publications.
Each of these 356 articles underwent a detailed screening process. Titles and
abstracts were manually reviewed to determine whether the articles explicitly
addressed emotional appeals in consumer-focused marketing contexts. Studies
focusing exclusively on organisational behaviour, general psychological constructs,
or business-to-business interactions without a clear marketing application were
excluded. This screening led to the removal of 107 articles, resulting in a pool of 249
studies eligible for full-text assessment.
The remaining articles were then evaluated in detail according to pre-established
criteria, following guidance from Macpherson and Holt (2007), as outlined in Appen-
dix 1. This evaluation involved reading the full text of each article and assessing its
relevance, methodological soundness, and contribution to the field. Articles that did
not meet the necessary standards or that fell outside the thematic scope of the review
were excluded at this stage. This resulted in the removal of a further 113 papers, leav-
ing a final sample of 136 studies. These were then organised and segmented for the
subsequent phases of analysis, as detailed in Appendix 2.
Of the 136 included articles, a substantial majority (approximately 85%, or 116
papers) were published in journals listed in the Academic Journal Guide (AJG) 2024,
with quality ratings ranging from 1 to 4* (see Appendix 3). This distribution reflects
the academic credibility and relevance of the selected literature, which is primarily
situated within the fields of business and marketing. The overall selection and review
process is visually summarised in Fig. 1.
Following the selection process, the final set of papers was analysed using data
mining techniques, conducted through R software. This enabled the identification of
key themes, trends, and research patterns, which were subsequently structured into

1 3
   13  Page 8 of 39
Italian Journal of Marketing         (2026) 2026:13
Fig. 1 Flow diagram of the systematic literature review paper selection process

1 3
Page 9 of 39    13
Italian Journal of Marketing         (2026) 2026:13
an integrative analytical framework. The results of this analysis form the basis for the
conceptual and theoretical contributions discussed in the following sections.
3 Descriptive analyses of literature
An examination of publication trends reveals that scholarly interest in emotional
appeals in marketing began in 1995. Since then, the number of publications has var-
ied, showing alternating periods of stagnation and renewed academic attention. An
upward trajectory started in 2011, with a particularly sharp increase occurring in
2014, when the number of publications reached eight. The peak in publication output
was observed in 2020, which recorded eighteen studies, followed by another high
point in 2024, with sixteen publications. Although minor fluctuations persist, the gen-
eral trend indicates a growing scholarly interest in this field. This is particularly evi -
dent over the past five years, during which the topic has attracted sustained academic
attention. These trends are illustrated in Fig. 2.
In terms of publication outlets, four journals stand out for their consistent and
significant contributions to the field. A citation network visualised using VOSviewer
(Fig. 3) shows that the Journal of Product and Brand Management (N = 10), European
Journal of Marketing ( N = 8), Journal of Business Research ( N = 7), and Journal of
Brand Management ( N = 7) collectively account for 23.5% of all included studies.
Their prominence highlights their central role in shaping the academic dialogue on
emotional appeals in marketing.
The citation network of authors, also generated through VOSviewer (Fig. 4), iden-
tifies several influential scholars who have significantly contributed to the develop -
ment of this research area. Among the most frequently cited are Hoyer and Hudson,
both of whom appear as central nodes within the network. The dense interconnec -
Fig. 2 Evolution of publication trends

1 3
   13  Page 10 of 39
Italian Journal of Marketing         (2026) 2026:13
Fig. 3 Mapping citation networks based sources (sources not connected to others have been excluded)

1 3
Page 11 of 39    13
Italian Journal of Marketing         (2026) 2026:13
Fig. 4 Mapping citation networks and leading scholars (authors not connected to others have been excluded)

1 3
   13  Page 12 of 39
Italian Journal of Marketing         (2026) 2026:13
tions among these authors reflect a well-established pattern of academic collabora -
tion and knowledge dissemination, reinforcing the intellectual structure of the field.
4 Thematic analyses of literature
4.1 Topic analysis procedure
To uncover the latent thematic structures within the 136 selected articles, a rigorous
topic modelling procedure was employed. The full-text versions of all articles were
systematically processed and transformed into analysable textual data using R soft -
ware, following the guidance of established text-mining protocols (Breuer, 2017).
The initial phase of data preparation involved extracting the core content of each
document and refining it for analysis and interpretation. This process included con -
verting all text to lowercase, removing citations and bibliographic references, elimi -
nating stop words, numbers, punctuation marks, and redundant white spaces (Aleem
et al., 2024). Additionally, multi-word expressions that carried semantic significance
were consolidated to preserve meaningful conceptual patterns. To further enhance
coherence within the dataset, stemming techniques were applied to reduce words to
their root forms, preventing different variants of the same term from being treated as
distinct tokens (Wu et al., 2017).
Following this preprocessing stage, a document-term matrix was constructed to quan-
tify the frequency of word occurrences across the corpus. Latent Dirichlet Allocation
(LDA), a widely used unsupervised learning algorithm, was then applied to the matrix
to identify hidden thematic structures (Blei et al., 2003). As a probabilistic model, LDA
clusters words into a predefined number of topics, referred to as K, by estimating the co-
occurrence patterns of terms across documents. To address challenges posed by language
ambiguity, such as synonymy and polysemy, dimensionality reduction techniques were
also integrated into the analysis.
The optimal number of topic clusters was determined through an iterative evaluation
of model fit, using log-likelihood estimation based on Gaussian Mixture Models (Bishop,
2006). A range of values, from K = 2 to K = 40, was tested, and the optimal solution was
identified at K = 14, where a marked inflexion in the trend curve suggested the best bal-
ance between complexity and interpretability (Fig. 5).
A suite of R packages supported the text-mining workflow. The “tm” package provided
the foundation for core text processing tasks (Feinerer et al., 2008), while “tidytext” struc-
tured the data into a tidy format suitable for analysis. The packages “dplyr” and “tidyr”
facilitated efficient data manipulation (Grolemund & Wickham, 2017), “topicmodels”
enabled the implementation of the LDA algorithm (Grün & Hornik, 2011), and “ggplot2”
supported visual representation of the results (Wickham, 2016). Collectively, these tools
contributed to a robust and replicable analytical pipeline. In addition, Gibbs sampling, a
Monte Carlo-based iterative sampling method, was used within the LDA framework to
estimate the distribution of topics across the corpus (Griffiths & Steyvers, 2004).
Within the topic model, two probability measures were central to interpreting the
results: the Gamma and Beta distributions. The Gamma score indicates the prob -
ability of a given topic appearing within a specific document, reflecting the degree

1 3
Page 13 of 39    13
Italian Journal of Marketing         (2026) 2026:13
to which each document is associated with particular themes (higher frequencies of
topic-related terms within a document result in stronger Gamma values). Conversely,
the Beta score represents the probability of specific words belonging to each topic,
identifying the most characteristic terms within each cluster. Together, these mea -
sures provide a detailed thematic map of the corpus, revealing how concepts are
distributed, co-occur, and interrelate across the analysed literature (Blei et al., 2003).
At this stage, the identified articles undergo topic analysis to explore each thematic
category systematically. The classification process is guided by the most frequently
occurring terms and linguistic patterns shared among interconnected articles within
each topic. Given the algorithm’s nature, a single article can contribute to multiple
underlying themes (Bilro et al., 2023), though most documents predominantly align
with a primary suggested category. As a result, the articles selected to represent each
topic are those with the strongest correlation to the key terms (see Appendices 4 and
5). Each topic is discussed and analysed in the following sections.
4.2 Topics discussion
This section synthesises fourteen recurrent topics, organised into five macro-themes,
that structure contemporary research on emotional appeals in marketing. The analysis
begins with macro-theme 1, individual-level affective and cognitive mechanisms,
which encompass (T1) message processing, (T2) mood states, and (T3) consumer
interpretation. It then considers macro-theme 2, relational and symbolic constructs,
including (T4) brand relationships, (T5) self-identity, and (T6) symbolic consump -
tion. The topic discussion further extends to macro-theme 3, brand level phenomena,
covering (T7) brand identity, (T8) brand value, (T9) brand immersion, and (T10) con-
Fig. 5 Evaluation of K using log-likelihood and perplexity metrics after adjustments to the top (Griffiths
& Steyvers, 2004) and bottom charts (Cao et al., 2009)

1 3
   13  Page 14 of 39
Italian Journal of Marketing         (2026) 2026:13
sumer experience. Macro-theme 4 captures socially embedded dynamics, including
(T11) peer influence and (T12) social engagement. Finally, macro-theme 5 addresses
emotionally disruptive processes and contextual moderators, encompassing (T13)
emotional temperature and (T14) emotional disruption.
Macro-theme 1: Individual-level affective and cognitive mechanisms
4.2.1 Message processing
Message processing is conceptualised as a constructive interaction between message
senders and receivers. On the receiver’s side, it involves two main components: the
selection of appropriate channels for allocating resources to the received content, and
the manner in which allocated cognitive resources are utilised to interpret and engage
with the information (Buijzen et al., 2010). In the field of advertising, the interplay
between emotional and rational appeals plays a crucial role in shaping how consum-
ers process persuasive messages. However, emotional appeals have been shown to
exert a stronger impact than rational ones (Gong & Cummins, 2020). Whereas emo-
tional appeals tap into consumers’ feelings to stimulate desire and influence behav -
iour, rational appeals are rooted in cognitive persuasion, offering logical arguments
to support decision-making processes (Young et al., 2019). Both strategies compete
for resource allocation within the consumer’s cognitive system, especially under lim-
ited attention spans, and may trigger different types of processing strategies, such
as heuristic-systematic processing. Heuristic approaches rely on mental shortcuts
and surface cues, while systematic processing involves deeper scrutiny of the mes -
sage’s content (Garaus & Wolfsteiner, 2023). The decision of which route a consumer
adopts often depends on motivation, involvement, and available cognitive resources.
Properly calibrated messaging ensures that neither route overwhelms the other, lead-
ing to optimised processing and improved persuasion outcomes.
4.2.2 Mood states
Mood states, broadly understood as temporary, pervasive emotional conditions,
significantly affect consumer perception and decision-making (Gardner, 1985). In
advertising and branding, mood states encompass a range of affective dimensions,
including pleasure, satisfaction, arousal (Alshohaib, 2024; Lin, 2016), excitement
(Hancock et al., 2024), and even fear (Dunn & Hoegg, 2014). This perspective is vis-
ible in multiple empirical contexts. For instance, arousal, pleasure and consequently
satisfaction were identified as predictors of emotional responses to online shopping
experiences, especially in the context of post-pandemic consumption (Alshohaib,
2024). Recent evidence suggests that high-arousal emotional appeals, particularly
those that evoke intense excitement, can effectively foster positive attitudes, espe -
cially in the context of public services. Interestingly, the impact of such emotionally
charged appeals has been found to surpass even that of love-based stimuli (Hancock
et al., 2024). Conversely, fear, traditionally viewed as a negative valence emotion,
has also emerged as a mood state with the potential to deepen brand attachment, espe-
cially when appropriately framed (Dunn & Hoegg, 2014). These studies collectively

1 3
Page 15 of 39    13
Italian Journal of Marketing         (2026) 2026:13
demonstrate the significance of understanding mood states not only as emotional
reactions but also as strategic tools in consumer-brand interactions.
4.2.3 Consumer interpretation
Consumer interpretation refers to the subjective process through which individuals
respond to brand-related stimuli (Phillips, 1997). This interpretative mechanism is not
merely cognitive but deeply emotional, shaping brand attitude. A favourable brand
attitude often stems from how well the brand aligns with the consumer’s emotional
and psychological framework, particularly in terms of personal values and affective
needs (Mitchell & Olson, 1981). A key factor influencing this interpretative process
is emotional intelligence, which refers to a person’s ability to perceive, understand,
regulate, and express emotions in themselves and others (Salovey & Mayer, 1990).
High emotional intelligence enhances consumers’ ability to accurately appraise
marketing stimuli, modulate emotional responses, and develop deeper, more consis -
tent brand relationships (Kidwell et al., 2008). Importantly, emotions such as hap -
piness and boredom significantly influence consumer appraisal and interpretation.
While happiness is associated with increased satisfaction and positive evaluations
of brands (Bench & Lench, 2013), momentary feelings of boredom are typically
identified as unpleasant emotional states marked by reduced mental stimulation and
diminished physiological activation (Sung et al., 2020), which may even trigger
brand-switching behaviours.
Macro-theme 2: Relational and symbolic constructs
4.2.4 Brand relationships
Brand relationship is defined as a co-created emotional bond that emerges through
personal interactions between the consumer and the brand, an evolving process that
nurtures mutual connection and strengthens the depth of their engagement over time
(Garg et al., 2025).
Brand attachment is a crucial foundation for the development of brand love, a
stronger emotional attachment characterised by passion, affection, and positive senti-
ment toward the brand (Batra et al., 2012). Consumers who experience brand love not
only feel emotionally connected to the brand but are also willing to support it, further
enhancing their attachment and fostering brand loyalty (Ghorbanzadeh, 2021). The
role of brand satisfaction in sustaining a loyal relationship with the brand has been
well-documented in consumer behaviour literature, with studies showing that satis -
fied customers are more likely to develop a sense of attachment, ultimately contrib -
uting to brand loyalty (Oliver, 1999). However, brand relationships are not always
positive. Negative emotional reactions to a brand, recognised as brand hate (Bryson
et al., 2013), may arise either during consumption or even in its absence. Brand hate
is a phenomenon in which consumers experience a strong aversion toward a brand
due to negative experiences or perceived brand failures (Taqi et al., 2025). The con-
cept of brand hate shows the complexity of brand relationships, demonstrating that
emotional responses are not always uniformly positive.

1 3
   13  Page 16 of 39
Italian Journal of Marketing         (2026) 2026:13
4.2.5 Self-identity
Self-identity reflects how individuals define and experience themselves across situ -
ations and over time, comprising both the actual self and the ideal self they aspire
to become. From an emotional perspective, self-identity is central to consumption
because brands often function as symbolic resources through which consumers regu-
late feelings of self-worth, pride, and belonging (Huber et al., 2018). When brand
meanings align with consumers’ self-concept, emotional resonance emerges, foster -
ing self-congruence and strengthening affective responses toward the brand (Malär
et al., 2011; Sirgy, 1982).
Emotional attachment is particularly pronounced when brands resonate with con-
sumers’ ideal self, as aspirational alignment can intensify feelings of motivation and
personal fulfilment, especially among individuals with low public self-consciousness
(Malär et al., 2011). At the same time, the emotional relevance of self-congruence
varies by context, with ideal and actual self-alignment shaping affective responses
to hedonic and utilitarian brands in distinct ways (Huber et al., 2018). Importantly,
misalignments between the actual and ideal self may generate negative affect, such
as discomfort or frustration, prompting compensatory behaviours including compul-
sive consumption or outward brand denigration (Higgins, 1987; Japutra et al., 2018).
Within this emotional dynamic, cause related marketing offers a mechanism through
which brands can help consumers alleviate self-discrepancy by providing symbolic
and moral meaning, thereby supporting positive emotional regulation and deeper
emotional engagement (Bhattacharya & Sen, 2004).
4.2.6 Symbolic consumption
Symbolic consumption refers to the use of goods and services as tools to express
identity, signal social status, or affirm group membership. This form of consump -
tion relies on the shared symbolic value that society attributes to certain products
(Witt, 2010). Among the key psychological drivers of symbolic consumption is emo-
tional brand attachment, which reflects the emotional bond between a consumer and
a brand. Brands that evoke strong emotional connections often tap into consumer
nostalgia, triggering memories of past experiences, which strengthens both brand
attachment and symbolic value. Nostalgic branding strategies are particularly effec -
tive when targeting consumers seeking familiarity and emotional comfort in an ever-
changing market landscape (Muehling et al., 2014).
Furthermore, the concept of brand coolness is essential in contemporary symbolic
consumption, especially among younger demographics. Cool brands are perceived
as innovative, authentic, and socially admired, which makes them highly desirable
symbols for identity construction (Warren et al., 2019). The perception of coolness
enhances conspicuous consumption, whereby consumers engage in visible consump-
tion practices to showcase status and prestige. This behaviour is closely intertwined
with materialism, where individuals place a high value on possessions as a means of
achieving happiness and signalling success (Klabi, 2020).
Macro-theme 3: Brand level phenomena

1 3
Page 17 of 39    13
Italian Journal of Marketing         (2026) 2026:13
4.2.7 Brand identity
Brand identity captures the set of associations companies seek to establish about what
the brand stands for and aspires to be, including its purpose, values, and personal -
ity (Aaker, 1995). From an emotional appeals perspective, identity is consequential
because it provides the affective meaning system through which consumers interpret
brand cues and experience emotions such as warmth, pride, or reassurance during
brand encounters. Although brand image reflects how consumers perceive the brand,
brand identity is strategically articulated by the company and, when consistently
expressed, shapes the emotional tone of brand communications and relationship
vision (de Chernatony, 1999; Keller, 1993).
A key identity-related construct with direct emotional implications is brand
authenticity, defined as the extent to which a brand is perceived as genuine and faith-
ful to its supported values rather than purely commercially motivated (Napoli et al.,
2014). Authenticity signals can strengthen consumers’ affective trust and feelings of
psychological safety, thereby supporting emotional attachment and relational conti -
nuity. Conversely, misalignment between projected identity and experienced brand
encounters can elicit negative affective responses, such as disappointment, scepti -
cism, or irritation, which may undermine equity and weaken relationship strength
(Keller, 1993). Accordingly, effective brand management involves actively monitor-
ing consumer perceptions and ensuring that identity cues are translated coherently
across touchpoints, so that the brand’s intended emotional meaning is reliably rein -
forced rather than contradicted (da Silveira et al., 2013).
4.2.8 Brand value
Brand Value refers to the overall financial, emotional, and social worth that a brand
holds in the market, which is derived from its ability to create positive perceptions,
foster loyalty, and engage consumers effectively. It encompasses not only the brand’s
reputation but also its capacity to differentiate itself in the competitive landscape
(Keller & Swaminathan, 2020).
Emotional brand attachment plays a pivotal role in creating brand value, as it
reflects the deep, affective connection that consumers develop with a brand. This
attachment strengthens brand equity by enhancing consumer loyalty and advocacy
(Thomson et al., 2005; Vivek et al., 2012). The concept of value co-creation is inte -
gral to brand value, as it involves consumers actively participating in shaping and
enriching their experiences with the brand. By co-creating value, consumers feel
more deeply engaged and emotionally connected to the brand, leading to higher lev-
els of long-term brand satisfaction (Hussain et al., 2021). Brand trust is another key
driver of brand value, with consumers relying on brands to fulfil promises and deliver
consistent quality. Emotional branding, when leveraged effectively, fosters trust and
deepens emotional attachments, which ultimately enhance brand value (Abdul Aziz
et al., 2023). Brands that succeed in creating an emotional connection with consum -
ers through trust-building experiences and authentic messaging are better able to co-
create value with their audience (Hernandez-Fernandez & Lewis, 2019).

1 3
   13  Page 18 of 39
Italian Journal of Marketing         (2026) 2026:13
4.2.9 Brand immersion
Brand immersion refers to a deeply engaging experience where consumers are cog -
nitively, emotionally, and behaviourally absorbed into a brand’s environment. Unlike
surface-level interactions, immersive experiences aim to saturate the consumer’s per-
ceptual field, often through multisensory or interactive brand stimuli (Romero et al.,
2025; Schmitt, 1999).
Studies suggest that when consumers encounter emotionally salient or personally
relevant brand cues, the likelihood of accurate recall significantly increases (Kaya et
al., 2025).
Brand-integral stimuli, those seamlessly embedded in the storytelling or interac -
tive flow, trigger stronger associative links in memory, compared to peripheral cues
(Phillips & McQuarrie, 2004). Thus, immersion acts as a gateway for more durable
memory encoding and retrieval processes. At the core of this process lies consumer
attention, a limited cognitive resource that immersive experiences help capture and
sustain. Attention operates as a necessary precondition for both memory formation
and attitudinal shifts (Phillips & McQuarrie, 2004). Capturing and maintaining atten-
tion are prerequisites for message effectiveness. In a saturated landscape, brands must
rely on emotionally or contextually salient stimuli to engage consumers (Teixeira et
al., 2012).
4.2.10 Consumer experience
The consumer experience represents the totality of cognitive, emotional, sensory, and
behavioural responses that arise during the entire interaction between a consumer and
a brand (Lemon & Verhoef, 2016; Luo et al., 2024). It extends beyond mere product
utility, encompassing all touchpoints, physical (Lemon & Verhoef, 2016) or digital
(Luo et al., 2024), where consumers form impressions and meanings. As markets
become increasingly experience-driven, understanding and designing memorable
brand encounters has become a central focus in marketing strategy. A brand’s ability
to engage the senses is crucial in shaping brand experience, particularly in environ -
ments where physical presence is limited. Sensory branding leverages cues such as
sound, sight, colour, or even scent to trigger affective responses and more firmly
imprint brand identity in memory (Lindstrom, 2005).
One powerful indicator of sensory impact is facial expression, which can be both
observed in participants and symbolically used within advertisements to commu -
nicate emotions (Ekman & Friesen, 2003). In turn, these effects can significantly
influence purchase intention, especially when consumers feel emotionally aligned
with the sensory narrative being presented. Facial expressions act as powerful emo -
tional signifiers, and with the advent of cutting-edge technologies, machines are now
capable of decoding these non-verbal cues with remarkable precision and autonomy
(Höfling & Alpers, 2023).
Macro-theme 4: Socially embedded dynamics

1 3
Page 19 of 39    13
Italian Journal of Marketing         (2026) 2026:13
4.2.11 Peer influence
In the digital age, peer influence is often mediated through word-of-mouth (WOM)
and user-generated content, where consumers share brand-related experiences with
others (Ramirez et al., 2018). This informal form of communication serves as a pow-
erful source of information, especially when traditional advertising is perceived as
less trustworthy or overly commercialised. The cognitive valence of peer-shared
messages, whether positive, neutral, or negative, determines how recipients process
and internalise them. Unlike brand-driven narratives, peer messages often carry more
emotional and experiential weight, as they are shaped by the personal tone of the
sender. Furthermore, the generational divide plays a crucial role, as different age
groups interpret and react to online content in distinct ways, such as younger gen -
erations (Correia et al., 2025; Ramirez et al., 2018). In other words, the quality of
content created in the form of word of mouth has a greater impact than its volume.
Additionally, messages that evoke stronger emotional responses tend to have a more
significant influence on the audience’s mind. This emphasises that emotional content,
rather than just the amount of information shared, plays a key role in making the mes-
sage more impactful and memorable (Gopinath et al., 2014).
4.2.12 Social engagement
Social engagement in media refers to the level of interaction, participation, and emo-
tional connection users develop with brand-related content on social media platforms
(Brodie et al., 2013). In today’s media environment, social media operates not merely
as a promotional tool but as a dialogical space where users co-create value through
reactions, comments, shares, and emotional feedback. Insider content, which lever -
ages cultural codes and emotionally salient cues, garners significantly more reactions
and shares than generic promotional posts (Huertas & Marine-Roig, 2016). Further-
more, user reactions serve as real-time indicators of affective resonance. In emotion-
ally driven domains such as sports or tourism, user comments and shares often mirror
emotional investment. For instance, it is underlined that users interacting with sport-
related branded posts exhibit strong affective engagement due to emotional attach -
ment to teams or symbols (Ruihley & Pate, 2017). Finally, content strategies that
acknowledge user-centred values are significantly more likely to cultivate sustained
social engagement. Research suggests that content appealing to consumers’ personal
and emotional values enhances perceived relevance and increases the likelihood of
repeated interaction (Pang et al., 2009).
Macro-theme 5: Emotionally disruptive processes and contextual moderators
4.2.13 Emotional temperature
Emotional temperature is a dual-faceted emotional aspect that refers to the range of
human interactions, from warmth to coldness. The degree of social closeness cor -
relates with feelings of emotional warmth, whereas greater social distance is tied to
emotional coldness. In fact, emotional temperature usually interacts meaningfully
with physical temperature, conceptually experienced in proximity, where feelings

1 3
   13  Page 20 of 39
Italian Journal of Marketing         (2026) 2026:13
of love are associated with warmth, and discomfort is linked to coldness (Bruno et
al., 2022). Emotional match between feelings of happiness and sadness (Kwon et
al., 2022), alongside the assessment of environmental effects in advertising, holds
significant importance. For instance, ambient temperature can influence the extent to
which audiences are drawn to emotional stimuli (Bruno et al., 2017). A well-executed
emotional match can enhance message effectiveness by aligning external stimuli with
internal states. When this alignment supports the body’s drive toward homeostasis,
consumers may feel more comfortable and psychologically prepared to engage with a
message or brand (Bruno et al., 2017). Understanding emotional temperature enables
advertisers to craft more effective campaigns that align with emotional context.
4.2.14 Emotional disruption
Emotional disruption is defined as a sudden or sustained disturbance in affective
equilibrium (Schachter et al., 1961). It emerges when individuals are confronted
with emotionally charged, often contradictory, information such as fake news or
alarming content (Roozenbeek & van der Linden, 2019). When these inputs provoke
affect intensity, individuals may experience heightened emotional arousal, leading
to impulsive responses and decreased cognitive control. Research has shown that
affectively intense information, especially when false or misleading, can prompt
emotional volatility, making people more vulnerable to belief distortion and mis -
judgement (Forgas, 2011).
In the context of high-risk situations, emotional disruption can override the pre -
frontal cortex’s regulatory role, pushing individuals to make urgent decisions driven
more by emotion than analysis. High affect intensity leads people to overestimate
potential threats or consequences, intensifying the sense of urgency and reinforc -
ing risk-averse or extreme behaviours (Loewenstein et al., 2001). Decision-making
becomes compressed into a narrow emotional tunnel, where rapid judgments may
bring temporary relief but long-term negative consequences. Individuals under
emotionally unstable conditions are more susceptible to cognitive biases and heu -
ristics, which further impair their ability to assess information credibility (Lerner
et al., 2015). Managing emotional disruption requires more than just awareness; it
also requires effective coping strategies. Scholars have proposed affect regulation
frameworks and emotional inoculation strategies to reduce the psychological impact
of fake news and risky framing (van der Linden et al., 2020).
5 Future research agenda
While substantial progress has been made in examining emotional appeals in mar -
keting and their theoretical underpinnings, relevant gaps in the literature remain.
Addressing these gaps holds significant potential to advance the field by enriching
theoretical models, diversifying methodological approaches, and enhancing practi -
cal applications. Grounded in the TCM framework (Theory, Characteristics, Meth -
odology) (e.g., Aleem et al., 2024; Bilro & Loureiro, 2020), this study organises
future research opportunities across these three key domains. In doing so, it offers a

1 3
Page 21 of 39    13
Italian Journal of Marketing         (2026) 2026:13
structured guide to navigating and addressing underexplored frontiers in the study of
emotional appeals in marketing (see Table 2).
5.1 Future research directions - theory
As noted, the theoretical foundations of emotional appeals in marketing remain
disperse, with attachment, appraisal, and congruence theories featuring most prom -
inently in the literature. To advance theory development, this section outlines extend-
ing established theories, integrating multiple frameworks to capture the multi-faceted
nature of emotional processes, incorporating theories that reflect contemporary digi-
tal and platform mediated consumption and identifying previously unexplored con -
ceptual relationships.
One promising direction for theory development involves extending the applica -
tion of the Technology Acceptance Model (TAM). TAM is one of the most widely
used theoretical frameworks for understanding how users come to accept and use
technology. TAM suggests that the higher the usefulness and simplicity of technol -
ogy, the more likely individuals are to adopt and use it (Davis, 1989). Although the
influence of this model on purchase intention has been confirmed with the inclusion
of emotion factor in livestreaming environment (Zhou & Tong, 2022), it is recom -
mended that the upgraded model, known as TAM 3 (Venkatesh & Bala, 2008), which
offers more precise criteria, be explored in measuring emotions, particularly in tech-
nological contexts and beyond human relationships, given the continuous advance -
ments in technology.
With the increasing dominance of technology in human lives, new dimensions
of attachment theory can be explored. In fact, the introduction of novel attachment-
related concepts in the digital realm is worth discussing. For instance, digital attach-
ment, defined as the emotional relationships that a person develops with technological
environments (Hasan, 2022), could present a new direction for studies focusing on
the connection between humans in a digital platform (Zou et al., 2025), like social
media, or even between humans and artificial intelligence (AI) in a fresh phase.
While previous studies have examined attachment theory (Dwivedi et al., 2019;
Manohar et al., 2023; Mostafa & Kasamani, 2021), appraisal theory (Faseur &
Geuens, 2012; Li et al., 2023), and congruence theory (Gilal et al., 2023; Schne-
belen & Bruhn, 2018) individually or pairwise, a comprehensive integration of all
three repeatedly tested across both product and service industries could provide a
more holistic understanding. Such an approach would not only yield complemen -
tary insights but also significantly enhance the theoretical connectivity within this
research domain.
Building on the intersection of cognitive and behavioural economics, appraisal
theory, rooted in an individual’s subjective evaluation of experiences based on per -
sonal criteria (Faseur & Geuens, 2012), can be effectively integrated with prospect
theory as an economic behavioural topic, which explains consumer decision-making
under risky situations (Kahneman & Tversky, 1979). This fusion provides a more
nuanced and manipulable framework for analysing the cognitive processes of con -
sumers when exposed to emotional appeals, enabling a deeper understanding of their
decision-making mechanisms.

1 3
   13  Page 22 of 39
Italian Journal of Marketing         (2026) 2026:13
Research scopes Research topics Research questions
Theory Expanding established
theories
RQ1: How can new structure of technology acceptance
models (TAM), such as TAM3, provide a better explana-
tion of the effectiveness of emotional elements?
RQ2: How can attachment theory be redefined to encom-
pass the concept of digitalization?
Synthesizing
multiple theoretical
frameworks
RQ3: To what extent can appraisal theory illuminate
specific aspects of behavioral economics, such as prospect
theory, when emotional appeals are emphasized?
RQ4: What new insights might result from synthesizing
attachment theory, appraisal theory, and self-congruence
theory?
RQ5: Is there a conceptual linkage between social identity
theory and the technology acceptance model 3?
Adding theories and
uncovering novel
interconnections
RQ6: How can unexpected customer responses be pre-
dicted and managed through cognitive dissonance theory
and psychological reactance theory?
RQ7: How can embodiment theory, utilizing sensory and
motor experiences, contribute to deepening theoretical
knowledge?
RQ8: Does the conceptual sequence of emotions, as
explained by narrative transportation theory, reveal new
dimensions regarding consumer reactions?
Exploring new
connections
RQ9: What are the main positive and negative emotional
triggers, and how do they affect consumer responses?
RQ10: Which emotional cues play a fundamental role in
fostering deep brand attachment, and how do they drive
this connection?
RQ11: Does emotional brand attachment naturally trans-
late into sustained customer relationships?
RQ12: Is there a significant difference between human-
generated and AI-generated emotional content in terms of
impact and effectiveness?
Characteristics Sampling: Regional
Scope
RQ13: In which underexplored regional markets and areas
(e.g., African nations or Eastern European countries) can
emotionally appeals in marketing be investigated to evalu-
ate their market-specific impact?
RQ14: How do multi-country studies or intercontinental
analyses generate comparative perspectives, both within
culturally similar regions and across vastly different
cultural landscapes?
Sampling: Targeted
Segmentation
RQ15: How does sampling based on generational catego-
ries (e.g., Alpha and Z), through a focused approach on a
single generation or a comparative analysis across multiple
generations (e.g., differences between Z and X in expecta-
tions and reactions), enhance our understanding of social
media engagement and behavioral or emotional responses
to marketing?
RQ16: How does consumers segmentation based on
income levels or personality traits influence responses to
emotional attachment in marketing?
Table 2 Future research agenda

1 3
Page 23 of 39    13
Italian Journal of Marketing         (2026) 2026:13
Research scopes Research topics Research questions
RQ17: What outcomes can result from a strategically
targeted sample, such as celebrity followers or loyal
customers of a specific brand, when aligned with campaign
objectives in both the short-term and long-term for emo-
tional marketing strategies?
Study Procedure RQ18: How do different marketing techniques such as tex-
tual vs. visual content and static vs. dynamic formats affect
emotional cue perception across diverse personality traits?
RQ19: To what extent do findings from studies conducted
on real brands in real-world settings align with outcomes
observed for fictitious brands in controlled laboratory
experiments?
RQ20: Which emerging product or service industries pres-
ent promising opportunities for future research?
RQ21: How can advanced time-series analysis techniques
improve our understanding of consumer behavior patterns
in emotional attachment?
Statistical Techniques RQ22: What role can machine learning algorithms, like
unsupervised learning, play in uncovering hidden patterns
in emotional responses, which traditional methods might
overlook?
Innovative Emotional
Data Collection
RQ23: What impact could integrate eye-tracking technol-
ogy with virtual reality have on understanding emotional
content in digital marketing?
RQ24: How can wearable biometric devices, such as heart
rate monitors or skin conductance sensors, provide real-
time outputs and enhance the accuracy of data collection?
Data Analysis RQ25: How can advanced machine learning techniques,
implemented through platforms like TensorFlow or
PyTorch, transform statistical modeling into emotional
marketing studies by capturing deeper, non-observable
patterns in consumer behavior?
RQ26: How can emotion recognition software like “Emo-
tionAI” improve real-time analysis of consumer emotional
engagement with advertising stimuli in future studies?
RQ27: What benefits could the integration of Bayesian
analysis using software like JAGS or Stan bring to under-
standing non-linear relationships and uncertainty?
RQ28: How can emerging statistical software tools, such
as JASP or STATA, offer enhanced flexibility and transpar-
ency in analyzing complex datasets?
Methodology Expanding Research
Methods
RQ29: How can employ phenomenological methods
describe emotional cues for business goals?
RQ30: In what ways can longitudinally research method
be utilized to assess the long-term effects of advertising
cues that evoke emotions?
RQ31: How might action research be used to create itera-
tive feedback loops for testing in real-world environments?
RQ32: What methodological approaches are best suited for
managing and interpreting large-scale data in the context
of emotional marketing?
Table 2 (continued)

1 3
   13  Page 24 of 39
Italian Journal of Marketing         (2026) 2026:13
The outcomes of marketing strategies, particularly those employing emotional
appeals, do not always align with predetermined expectations and may, in some
instances, lead to unintended counterproductive effects (Poels & Dewitte, 2006). In
such cases, the significance of contrasting theoretical frameworks, namely cognitive
dissonance theory and psychological reactance theory, becomes increasingly evi -
dent. According to cognitive dissonance theory, individuals who encounter content
misaligned with their preexisting beliefs experience psychological discomfort and
a sense of cognitive inconsistency (Festinger, 1957). Likewise, psychological reac -
tance theory posits that perceived restrictions on one’s freedom of choice can elicit
oppositional responses (Brehm & Brehm, 2013), thereby undermining persuasive
intent. These theoretical perspectives provide critical insights into the potential draw-
backs of emotional advertising, highlighting the need for a more nuanced approach
to consumer engagement.
By embracing innovative theoretical perspectives, approaches such as narrative
transportation theory, which emphasises the immersive and emotionally engaging
nature of narrative-driven contents in information processing (Ried et al., 2025) and
embodiment theory, which demonstrates the deep interconnection between sensory
and tactile experiences and consumers’ emotional and cognitive responses (Gallese
& Lakoff, 2005), can unveil hidden dimensions of consumer attitudes in the busi -
ness landscape. These frameworks offer a more effective lens for decision-making
processes.
To uncover new connections, qualitative studies using the grounded theory
approach are necessary to identify emotional triggers (Talebzadeh et al., 2024) and
categorise them into positive and negative stimuli. This enables a more detailed
classification of triggers and facilitates more conceptual comparisons, for example,
between human-generated and AI-generated content (Kirk & Givi, 2025). Conse -
quently, the effects of positive and negative emotional signals can be assessed more
comprehensively.
Another important consideration is the examination of moderators and additional
mediators in the pathway leading to emotional brand attachment (Sudbury-Riley
& Edgar, 2016). Accordingly, brand-related attributes such as brand familiarity
(Sudbury-Riley & Edgar, 2016) and brand trust (Mostafa & Kasamani, 2021) may
function as potential mediators. Likewise, consumer-related attributes, including per-
sonality traits (Faseur & Geuens, 2012), emotional dissonance, emotional contagion,
and word-of-mouth, also hold potential for examination in moderating roles. It is sug-
gested that using different types of media, such as billboards (Nielsen et al., 2010),
TV and newspapers (Baumgartner & Laghi, 2012), and even going beyond physical
types (Long Yi, 2011), like social media (Ahmadi et al., 2023; Garaus & Wolfsteiner,
2023), be examined more thoroughly. However, immersive spaces like AR and VR
may also influence the intensity of consumer responses to environmental stimuli (Liu
Research scopes Research topics Research questions
RQ33: How can simulation-based approaches help refine
consumer segmentation in emotional marketing?
Table 2 (continued)

1 3
Page 25 of 39    13
Italian Journal of Marketing         (2026) 2026:13
& Lei, 2025; Yang et al., 2020). Similarly, sensory stimulation across all five senses
might produce distinct reactions (Tsujimoto et al., 2024).
Finally, although emotional brand attachment has been linked to brand love in
some studies (Choi et al., 2024; Ghorbanzadeh & Rahehagh, 2020), it remains open
to further exploration. It is essential to not only investigate this connection in greater
depth but also examine its impact on brand advocacy and the sustained relationship
between consumers and brands.
5.2 Future research directions - characteristics
Given the substantial geographical diversity observed in previous studies, future
research could benefit from expanding sample sizes (Mehmood et al., 2022; Wu
& Chen, 2024; Zhang et al., 2014) to focus on regions that remain underexplored
(Correia et al., 2025; Fernandes & Moreira, 2019) in terms of emotional responses
and behavioural evaluations such as Africa and Eastern Europe. These areas present
unique opportunities for uncovering cross-cultural variations in emotional engage -
ment. Moreover, considering the strong emphasis on cultural studies (Hudson et al.,
2015; Leung et al., 2014; Rathnayake, 2021), comparative analyses among countries
with similar cultural backgrounds could offer intriguing insights into shared emo -
tional patterns and consumer behaviours.
From a target population perspective, prior research has predominantly focused
on students (Alvarado-Karste & Guzmán, 2020; Huang, 1997; Lee & Davis Burns,
2014; Sharif & Sidi Lemine, 2024) and general consumers (Joo & Kim, 2021; Kim,
2019), with some generational studies particularly on Generation Y (Kurtoğlu et al.,
2022; Rathnayake, 2021). However, intergenerational studies, especially those exam-
ining Generations Z and Alpha, could provide a foundational understanding of how
younger generations interact with emotional appeals. Another promising direction
for sample selection involves studying fans of celebrities or teams (Kucharska et al.,
2020) and brand supporters (Chang, 2020). Examining the impact of fan-based bias
on emotional and brand attachment could reveal critical insights into how strong
affiliations influence consumer decision-making. From the study procedure perspec-
tive, different marketing strategies, including the use of textual versus visual content,
as well as static versus dynamic formats, may influence how consumers perceive
emotional cues. The impact of these techniques can vary depending on the individu-
al’s personality traits (Schmitt, 2012).
The generalizability of scientific findings to real-world settings has always been a
subject of debate. Given that some studies have focused on fictitious brands within
laboratory environments (Bruno et al., 2017; Ghasemi Siani et al., 2021; Long Yi,
2011), it is recommended that future research should consider the use of real brands
(Alvarado-Karste & Guzmán, 2020) in authentic, real-world contexts (Madadi et al.,
2024; Megías et al., 2011) to better assess the applicability of the results beyond
controlled settings. Emerging industries, particularly those driven by technology and
sustainability, present significant opportunities for future research into consumer
behaviour and emotional engagement. Sectors like electric vehicles (Domarchi et al.,
2024), sustainable fashion (Haines & Lee, 2022), and personalised healthcare (Zhou

1 3
   13  Page 26 of 39
Italian Journal of Marketing         (2026) 2026:13
et al., 2023) are rapidly evolving, with consumers’ emotional connections to these
products and services growing increasingly important.
From a statistical techniques’ perspective, machine learning algorithms, particu -
larly those involving unsupervised learning, can uncover hidden patterns in emo -
tional responses that traditional analytical methods may overlook. Unsupervised
learning techniques, such as clustering or dimensionality reduction, enable research-
ers to analyse vast datasets without predefined labels, revealing complex, nonlinear
relationships within the data (Dura & Wosiak, 2022), which can lead to the discov -
ery of new emotional clusters. While there is a notable diversity in data collection
methods used in past studies, it is recommended that future research adopt advanced
techniques such as eye-tracking technology combined with virtual reality (Liu et al.,
2024) and biometric devices (e.g., heart rate monitors or skin conductance sensors)
(De Keyser et al., 2021) to assess rapid emotional responses. These cutting-edge tools
could offer a more accurate and nuanced understanding of how consumers respond to
emotional stimuli in real-time.
The integration of advanced machine learning techniques, implemented through
platforms such as TensorFlow (Hribar et al., 2022) or PyTorch (Nie et al., 2025),
holds significant potential to transform statistical modelling. These methods can
uncover hidden, non-observable patterns in consumer behaviour, enabling research -
ers to explore deeper and more intricate aspects of emotional engagement. Similarly,
emotion recognition tools like EmotionAI could revolutionise real-time analy -
sis (Rhue, 2024) of consumer emotional responses to advertising stimuli, offering
insights that go beyond traditional methods. Additionally, the adoption of Bayes -
ian analysis through software such as JAGS or Stan offers considerable advantages
in handling nonlinear relationships and uncertainty in complex datasets (Plummer,
2023). This approach could enhance the accuracy of emotional marketing studies by
providing a more robust framework for handling complex data structures. Lastly, the
use of emerging statistical software tools, such as JASP or STATA, offers greater flex-
ibility and transparency in analysing complex datasets, thereby improving the overall
reliability and interpretability of findings.
5.3 Future research directions - methodology
Recent advancements in research methodologies have expanded the scope of emo -
tional marketing studies. The phenomenological approach offers deep insights into
consumer emotional signals by capturing subjective experiences, providing busi -
nesses with a nuanced understanding of affective responses. Meanwhile, as stated
in previous research, longitudinal studies can enhance the clarity of findings and
improve the generalizability of results by evaluating consumer responses to emo -
tional stimulation over time (He et al., 2016; Hudson et al., 2015; Vahdat et al., 2020)
and allow researchers to assess the enduring effects of emotionally charged advertis-
ing cues over time, revealing patterns of sustained influence on consumer behavior.
Additionally, action research fosters iterative feedback loops, enabling real-world
testing and continuous refinement of marketing strategies based on consumer interac-
tions (Basu et al., 2023).

1 3
Page 27 of 39    13
Italian Journal of Marketing         (2026) 2026:13
Given the increasing complexity of emotional marketing data, selecting robust
analytical frameworks is crucial for managing and interpreting large-scale datasets,
ensuring that output remains actionable and relevant in market environments. There-
fore, the implementation of big data analytics should be given precedence in upcom-
ing research endeavours (Wang et al., 2025). Simulation-driven methodologies
continue to offer a valuable framework for forecasting business strategy outcomes.
By enabling researchers and industry professionals to explore hypothetical scenarios
and assess potential consumer reactions (Monauni, 2017), these models contribute to
the optimisation of strategic decision-making for real-world implementation.
In this context, the proposed conceptual framework for future research is pre -
sented in Fig. 6.
The proposed framework offers a structured and integrative perspective to guide
future research in a field still characterised by conceptual dispersion and fragmented
empirical approaches. By explicitly linking ad-related attributes, consumer character-
istics, and brand-level dimensions through the mediating roles of affective response
and emotional brand attachment, the framework clarifies the mechanisms through
which emotional appeals translate into outcomes such as brand love and advocacy.
It encourages scholars to move beyond isolated examinations of emotions towards
a more systemic understanding that captures interactions across individual, contex -
tual, and technological factors, including the increasing role of AI-generated content
and digital environments. Furthermore, by incorporating moderating influences such
as emotional contagion, WOM dynamics, and individual differences, the framework
enables the investigation of collective and real-time emotional processes that remain
underexplored in prior literature. Overall, the proposed conceptual framework con -
solidates existing knowledge while outlining avenues for theoretical and method -
ological advancement, providing a foundation for more coherent, multi-level, and
context-sensitive research in emotional marketing.
Fig. 6 Conceptual framework for future research

1 3
   13  Page 28 of 39
Italian Journal of Marketing         (2026) 2026:13
6 Conclusions and implications
6.1 Theoretical implications
This study advances theoretical understanding in emotional marketing by offering
several contributions that address conceptual and methodological limitations in the
existing literature. In doing so, the review responds directly to prior calls for more
granular classifications of emotional styles and their effects (Aeron & Rahman, 2025;
Sharma et al., 2023) and provides a systematic foundation for theorising emotions as
appraised, situated, and strategically mobilised marketing phenomena (Bagozzi et
al., 1999).
First, the study develops a more holistic theoretical model that unifies emotional
advertising and emotional branding, two subfields that have often been examined
separately. Rather than treating emotional appeals as isolated executional tactics, the
model links message processing mechanisms to downstream outcomes. In particular,
it aligns work on how emotional and rational cues shape attention and processing
routes (Buijzen et al., 2010; Garaus & Wolfsteiner, 2023) with evidence that mood
states such as pleasure, arousal, excitement, and fear condition consumer receptivity
and evaluation (Gardner, 1985; Hancock et al., 2024). This integration helps explain
how emotional stimuli become embedded in the consumer experience across touch -
points (Lemon & Verhoef, 2016) and, over time, contribute to brand relationships,
including attachment, love, and also negative relational states (Batra et al., 2012;
Taqi et al., 2025). In doing so, the study provides a more comprehensive conceptual
foundation for examining emotions as both short-term persuasive triggers and long-
term relational assets.
Second, this paper introduces an innovative methodological approach to theory-
building by applying advanced data mining and topic modelling techniques to the
emotional marketing literature. This approach enables the identification of latent
structures and thematic relationships that are difficult to detect through narrative syn-
thesis alone. Importantly, the method also provides an empirical basis for responding
to recent calls for more granular classifications of emotional styles and their specific
effects (Aeron & Rahman, 2025; Sharma et al., 2023), by revealing how emotional
constructs cluster across substantive domains, such as consumer experience, brand
immersion, symbolic consumption, and social engagement (Brodie et al., 2013). In
this sense, the study contributes a theory-informed analytical method that can be rep-
licated in other marketing research areas where conceptual dispersion is prevalent.
Third, the paper contributes to theory by challenging the prevailing individual-
centric perspective found in much of the literature and by specifying when emotional
responses should be conceptualised as socially situated and temporally synchronised.
The topic structure shows that emotional influence is frequently mediated through
peer communication and platform interactions, where emotionally resonant word of
mouth and user engagement shape persuasion and diffusion (Ramirez et al., 2018).
By emphasising that emotional reactions unfold not only within individuals but
also across collective experiences in interactive digital environments, this research
extends the principles of Technology Acceptance Model 3 (Venkatesh & Bala, 2008)
to affective and socially mediated contexts. This extension complements the litera -

1 3
Page 29 of 39    13
Italian Journal of Marketing         (2026) 2026:13
ture on attention and immersion by theorising emotional engagement as a function of
both cognitive resource allocation and socially reinforced affective cues (Teixeira et
al., 2012; Schmitt, 1999).
Fourth, this study addresses a critical conceptual ambiguity in the literature: the
tendency to label broad affective categories, such as happiness, fear, or pleasure,
without clarifying their underlying triggers, appraisal mechanisms, or boundary con-
ditions. Through topic modelling, the study reveals that some constructs are used
as surface descriptors rather than theoretically specified affective processes, which
weakens accumulation and comparison across studies. Accordingly, we call for
greater theoretical precision by distinguishing between emotional labels and affective
mechanisms, and by grounding emotional effects in interpretation and appraisal pro-
cesses, including the role of emotional intelligence in shaping how consumers per -
ceive, regulate, and respond to marketing stimuli (Salovey & Mayer, 1990; Kidwell
et al., 2008; Phillips, 1997; Mitchell & Olson, 1981). This refinement is further sup-
ported by the prominence of themes such as emotional disruption, which highlights
how affect intensity and information conditions can alter judgment and increase sus-
ceptibility to heuristics (Loewenstein et al., 2001; Lerner et al., 2015; Roozenbeek &
van der Linden, 2019).
6.2 Managerial implications
This study provides valuable managerial insights by highlighting the strategic role of
emotional cues in fostering meaningful and enduring relationships between brands and
consumers. As demonstrated in prior research, emotional dimensions can shape con-
sumer attitudes and influence behavioural intentions across a wide range of products and
services (Geuens et al., 2011; Lee & Davis Burns, 2014). Building on this foundation, the
current study highlights the importance of brand managers adopting a more deliberate,
evidence-based approach to integrating emotional triggers into their marketing strategies.
Doing so can not only enhance campaign effectiveness but also strengthen brand equity
and long-term profitability.
A key contribution of this study lies in challenging the assumption that emotional
appeals consistently yield positive results. While much of the existing literature has
focused on favourable or negative consumer responses (e.g., Kurtoğlu et al., 2022; Leung
et al., 2014), the possibility of neutral or non-reactive outcomes has received limited
attention. This finding serves as a cautionary note for practitioners: emotional marketing
carries reputational and financial risks if not carefully designed and tested. It is therefore
essential that managers invest in robust pretesting mechanisms (such as A/B testing or
neuromarketing tools) before deploying emotionally charged content across large-scale
campaigns.
Another novel implication concerns the evolving role of digital platforms as a fertile
ground for emotional engagement. Social media provides real-time, high-volume interac-
tion that can be leveraged to create emotionally resonant brand experiences. Similarly,
immersive technologies (including augmented reality (AR), virtual reality (VR), and
the metaverse) offer new opportunities for simulating emotionally engaging encounters.
These platforms enable brands to foster deeper psychological engagement by provid-

1 3
   13  Page 30 of 39
Italian Journal of Marketing         (2026) 2026:13
ing consumers with multisensory, experiential interactions that transcend traditional
advertising.
This study also identifies specific sectors, such as mobile technology, fashion, tourism,
financial services, and aviation, as especially conducive to emotion-driven marketing.
These industries are characterised by high consumer involvement and competitive inten-
sity, which makes emotional differentiation a valuable strategic asset. However, a key
managerial insight emerging from this review is the need to extend emotional branding
strategies to less explored or emerging sectors. For example, contrasting contexts such as
sustainable versus unsustainable consumption (Kaur et al., 2023), public versus private
service provision (Larsson & Müller, 2019), and SMEs versus large corporations may
also benefit from emotional positioning to drive consumer loyalty and identity alignment.
By revealing both the opportunities and risks of emotional engagement in marketing,
this study provides brand managers with a deeper understanding of how emotional strate-
gies can be more effectively designed, targeted, and implemented across diverse contexts.
These findings encourage practitioners to move beyond simplistic emotional appeals
and towards a more nuanced, data-driven, and context-sensitive approach to emotional
branding.
6.3 Limitations
Despite the rigorous methodological approach adopted in this review, certain limitations
should be acknowledged. One key constraint lies in the exclusive reliance on two major
academic databases (Scopus and Web of Science). While both are globally recognised for
their extensive and peer-reviewed coverage, the omission of additional repositories may
introduce a degree of coverage bias. As a result, relevant studies published in non-indexed
or emerging journals may have been inadvertently excluded. To address this concern,
the review deliberately prioritised quality papers published in well-established journals
indexed in the WOS and Scopus databases to ensure the inclusion of influential and theo-
retically robust contributions.
A further limitation concerns the specificity of the search terminology. The search
strategy focused on key terms such as emotional marketing, emotional branding, and
emotional advertising, selected to align with the study’s research objectives. While this
targeted approach enhanced the relevance and conceptual precision of the included lit-
erature, it also introduced potential lexical bias. Studies employing alternative but related
expressions (such as affective marketing, emotion-driven communication, affective
branding, or sensory-emotional integration) may not have been captured within the search
results, despite the use of Boolean logic and wildcard operators to broaden coverage.
Although these limitations are inherent to the scope and focus of the review, they do
not detract from the validity of the insights generated. Instead, they highlight important
opportunities for future reviews to expand keyword strategies and database selection,
thereby capturing a broader spectrum of relevant literature.
Supplementary Information The online version contains supplementary material available at  h t t p s : / / d o i .
o r g / 1 0 . 1 0 0 7 / s 4 3 0 3 9 - 0 2 6 - 0 0 1 3 6 - 2     .
Acknowledgements This work was supported by Fundação para a Ciência e a Tecnologia, grant
UIDB/00315/2020.

1 3
Page 31 of 39    13
Italian Journal of Marketing         (2026) 2026:13
Funding Open access funding provided by FCT|FCCN (b-on).
Data availability Data is available from the authors upon reasonable request.
Declarations
Conflict of interests On behalf of all authors, the corresponding author states that there is no conflict of
interest.
Open Access  This article is licensed under a Creative Commons Attribution 4.0 International License,
which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long
as you give appropriate credit to the original author(s) and the source, provide a link to the Creative
Commons licence, and indicate if changes were made. The images or other third party material in this
article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line
to the material. If material is not included in the article’s Creative Commons licence and your intended use
is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission
directly from the copyright holder. To view a copy of this licence, visit  h t t p : / / c r e a t i v e c o m m o n s . o r g / l i c e n
s e s / b y / 4 . 0 /     .
References
Aaker, D. A. (1995). Building strong brands. Free Press
Abdul Aziz, N., Othman, N. A., Abdul Murad, S. M. Bin. (2023). The effects of social support and social
media influencers’ credibility on emotional brand attachment: The mediating roles of trust in mul -
tichannel. Social Sciences & Humanities Open , 8(1), 100727.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . s s a h o . 2 0 2 3 .
1 0 0 7 2 7
Adalarasu, K., Ghousiya Begum, K., Vishnu Priyan, M., Devendranath, C., & Sriram, G. V . (2025). Neuro-
signaling techniques in advertisement endorsements: Unveiling consumer responses and behavioral
trends. Journal of Retailing & Consumer Services , 84, 104175.  h t t p s  : / / d o i  . o r g /  1 0 . 1  0 1 6 / j . j r e t c o n s e r .
2 0 2 4 . 1 0 4 1 7 5
Aeron, S., & Rahman, Z. (2025). Emotion as cause, effect, Mediator, and moderator in marketing: An
integrative review and future Research directions. Journal of Consumer Behaviour, 24(1), 470–498.
https://doi.org/10.1002/cb.2430
Ahmadi, A., Taghipour, A., Fetscherin, M., & Ieamsom, S. (2023). Analyzing the influence of celebrities’
emotional and rational brand posts. Spanish Journal of Marketing - ESIC, 27(1), 117–136.  h t t p s : / / d o
i . o r g / 1 0 . 1 1 0 8 / S J M E - 1 2 - 2 0 2 1 - 0 2 3 8
Aleem, A., Loureiro, S. M. C., & Bilro, R. G. (2024). Luxury fashion consumption: A review, synthesis
and research agenda. Spanish Journal of Marketing - ESIC , 28(2), 144–164. Emerald Publishing.
https://doi.org/10.1108/SJME-06-2021-0105
Alshohaib, K. A. (2024). From screens to carts: The role of emotional advertising appeals in shaping
consumer intention to repurchase in the era of online shopping in post-pandemic. Frontiers in Com-
munication, 9, 1–14. https://doi.org/10.3389/fcomm.2024.1370545
Alvarado-Karste, D., & Guzmán, F. (2020). The effect of brand identity-cognitive style fit and social influ-
ence on consumer-based brand equity. Journal of Product and Brand Management, 29(7), 971–984.
https://doi.org/10.1108/JPBM-06-2019-2419
Arici, H. E., Köseoglu, M. A., & Cakmakoglu Arici, N. (2022). Emotions in service research: Evolutionary
analysis and empirical review. The Service Industries Journal, 42(11–12), 919–947.  h t t p s  : / / d o i  . o r g /
1 0 . 1  0 8 0 / 0 2 6 4 2 0 6 9 . 2 0 2 2 . 2 1 0 1 6 3 8
Bagozzi, R. P., Gopinath, M., & Nyer, P. U. (1999). The role of emotions in Marketing. Journal of the
Academy of Marketing Science, 27(2), 184–206. https://doi.org/10.1177/0092070399272005
Basu, R., Lim, W. M., Kumar, A., & Kumar, S. (2023). Marketing analytics: The bridge between customer
psychology and marketing decision-making. Psychology and Marketing , 40(12), 2588–2611. John
Wiley and Sons Inc. https://doi.org/10.1002/mar.21908
Batra, R., Ahuvia, A., & Bagozzi, R. P. (2012). Brand love. Journal of Marketing, 76(2), 1–16.  h t t p s : / / d o
i . o r g / 1 0 . 1 5 0 9 / j m . 0 9 . 0 3 3 9

1 3
   13  Page 32 of 39
Italian Journal of Marketing         (2026) 2026:13
Baumgartner, E., & Laghi, F. (2012). Affective responses to movie posters: Differences between adoles -
cents and young adults. International Journal of Psychology, 47(2), 154–160.  h t t p s : / / d o i . o r g / 1 0 . 1 0 8
0 / 0 0 2 0 7 5 9 4 . 2 0 1 1 . 5 9 7 3 9 8
Bench, S. W., & Lench, H. C. (2013). On the function of boredom. Behavioral Sciences, 3(3), 459–472.
MDPI Multidisciplinary Digital Publishing Institute. https://doi.org/10.3390/bs3030459
Bhattacharya, C. B., & Sen, S. (2004). Doing better at doing good: When, Why, and how consumers
respond to corporate social initiatives. California Management Review, 47(1), 9–24.  h t t p s : / / d o i . o r g
/ 1 0 . 2 3 0 7 / 4 1 1 6 6 2 8 4
Bilro, R. G., & Loureiro, S. M. C. (2020). A consumer engagement systematic review: Synthesis and
research agenda. Spanish Journal of Marketing - ESIC , 24(3), 283–307. Emerald Group Holdings
Ltd. https://doi.org/10.1108/SJME-01-2020-0021
Bilro, R. G., Loureiro, S. M. C., & Souto, P. (2023). A systematic review of customer behavior in business-
to-business markets and agenda for future research. Journal of Business and Industrial Marketing ,
38(13), 122–142. https://doi.org/10.1108/JBIM-07-2022-0313
Bishop, C. M. (2006). Pattern recognition and machine learning. Springer
Blei, D. M., Ng, A. Y ., & Jordan, M. I. (2003). Latent Dirichlet allocation. Journal of Machine Learning
Research, 3(Jan), 993–1022
Brehm, S. S., & Brehm, J. B. (2013). Psychological reactance: A theory of freedom and control. Elsevier
Science
Breuer, J. (2017). R (Software). In J. Matthes, C. S. Davis, & R. F. Potter (Eds.), The International Ency-
clopedia of Communication Research Methods. Thousand Oaks, CA: SAGE Publications
Brodie, R. J., Ilic, A., Juric, B., & Hollebeek, L. (2013). Consumer engagement in a virtual brand com -
munity: An exploratory analysis. Journal of Business Research, 66(1), 105–114.  h t t p s  : / / d o i  . o r g /  1 0 . 1
0 1 6 / j . j b u s r e s . 2 0 1 1 . 0 7 . 0 2 9
Bruno, P., Melnyk, V ., & Murray, K. B. (2022). The temperature dimension of emotions. European Journal
of Marketing, 56(8), 2172–2215. https://doi.org/10.1108/EJM-04-2020-0237
Bruno, P., Melnyk, V ., & Völckner, F. (2017). Temperature and emotions: Effects of physical tempera -
ture on responses to emotional advertising. International Journal of Research in Marketing , 34(1),
302–320. https://doi .org/10.101 6/j.ijresma r.2016.0 8.005
Bryson, D., Atwal, G., & Hultén, P. (2013). Towards the conceptualisation of the antecedents of extreme
negative affect towards luxury brands. Qualitative Market Research: An International Journal ,
16(4), 393–405. https://doi.org/10.1108/QMR-06-2013-0043
Buijzen, M., Van Reijmersdal, E. A., & Owen, L. H. (2010). Introducing the PCMC model: An investiga-
tive framework for young people’s processing of commercialized media content. Communication
Theory, 20(4), 427–450. https://doi .org/10.111 1/j.1468-28 85.2010. 01370.x
Cao, J., Xia, T., Li, J., Zhang, Y ., & Tang, S. (2009). A density-based method for adaptive LDA model
selection. Neurocomputing, 72(7), 1775–1781. https://doi.org/10.1016/j.neucom.2008.06.011.
Chang, W. J. (2020). Experiential marketing, brand image and brand loyalty: A case study of Starbucks.
British Food Journal, 123(1), 209–223. https://doi.org/10.1108/BFJ-01-2020-0014
Choi, C. J., Xu, J., & Min, D. G. (2024). Investigating of the influence process on consumers’ active
engagement through emotional brand attachment and brand love. Asia Pacific Journal of Marketing
and Logistics, 36(11), 3061–3080. https://doi.org/10.1108/APJML-10-2023-1028
Christofi, M., Leonidou, E., & Vrontis, D. (2017). Marketing research on mergers and acquisitions: A
systematic review and future directions. International Marketing Review, 34(5), 629–651.  h t t p s : / / d o
i . o r g / 1 0 . 1 1 0 8 / I M R - 0 3 - 2 0 1 5 - 0 1 0 0
Clarivate. (2021). Web of Science - Web of Science Group.  h t t p s  : / / c l a  r i v a t  e . c o  m / w e b o f s c i e n c e g r o u p / s o l u
t i o n s / w e b - o f - s c i e n c e /
Correia, R., Aksionova, E., Venciute, D., Sousa, J., & Fontes, R. (2025). User-generated content’s influ -
ence on tourist destination image: a generational perspective. Consumer Behavior in Tourism and
Hospitality, 20(2), 167–185. https://doi.org/10.1108/CBTH-11-2023-0208
da Silveira, C., Lages, C., & Simões, C. (2013). Reconceptualizing brand identity in a dynamic environ -
ment. Journal of Business Research, 66(1), 28–36. https://doi .org/10.101 6/j.jbusres .2011.07 .020
Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information tech-
nology. MIS Quarterly, 13(3), 319–340. https://doi.org/10.2307/249008
de Chernatony, L. (1999). Brand Management through narrowing the gap between brand identity and
brand reputation. Journal of Marketing Management , 15(1–3), 157–179.  h t t p s : / / d o i . o r g / 1 0 . 1 3 6 2 / 0 2
6 7 2 5 7 9 9 7 8 4 8 7 0 4 3 2

1 3
Page 33 of 39    13
Italian Journal of Marketing         (2026) 2026:13
De Keyser, A., Bart, Y ., Gu, X., Liu, S. Q., Robinson, S. G., & Kannan, P. K. (2021). Opportunities
and challenges of using biometrics for business: Developing a research agenda. Journal of Business
Research, 136, 52–62. https://doi .org/10.101 6/j.jbusres .2021.07 .028
Domarchi, C., Vuong, Q. C., & Cherchi, E. (2024). The role of emotional coherence in electric vehicle
purchasing decisions. Transportation Research Part F: Traffic Psychology and Behaviour, 107, 997–
1014. https://doi.org/10.1016/j.trf.2024.10.018
Dunn, L., & Hoegg, J. (2014). The impact of fear on emotional brand attachment. Journal of Consumer
Research, 41(1), 152–168. https://doi.org/10.1086/675377
Dura, A., & Wosiak, A. (2022). Unsupervised emotional state recognition based on clustering of EEG
features. Procedia Computer Science, 207, 3093–3102. https://doi.org/10.1016/j.procs.2022.09.367
Dwivedi, A., Johnson, L. W., Wilkie, D. C., & De Araujo-Gil, L. (2019). Consumer emotional brand
attachment with social media brands and social media brand equity. European Journal of Marketing,
53(6), 1176–1204. https://doi.org/10.1108/EJM-09-2016-0511
Effertz, T., Teichert, T., & Tsoy, M. (2019). Fast food, ads, and taste in a Russian child’s mind. Psychology
and Marketing, 36(3), 175–187. https://doi.org/10.1002/mar.21171
Ekman, P., & Friesen, W. V . (2003). Unmasking the face: A Guide to recognizing emotions from facial
expressions. Malor Books
Erevelles, S. (1998). The role of affect in Marketing. Journal of Business Research , 42(3), 199–215.
https://doi.org/10.1016/S0148-2963(97)00118-5
Faseur, T., & Geuens, M. (2012). On the effectiveness of ego- and other-focused ad-evoked emotions:
The moderating impact of product type and personality. International Journal of Advertising, 31(3),
529–546. https://doi.org/10.2501/IJA-31-3-529-546
Feinerer, I., Hornik, K., & Meyer, D. (2008). Text mining infrastructure in R. Journal of Statistical Soft-
ware, 25(5), 1–54. https://doi.org/10.18637/jss.v025.i05
Fernandes, T., & Moreira, M. (2019). Consumer brand engagement, satisfaction and brand loyalty: A com-
parative study between functional and emotional brand relationships. Journal of Product and Brand
Management, 28(2), 274–286. https://doi.org/10.1108/JPBM-08-2017-1545
Festinger, L. (1957). A theory of cognitive dissonance. Stanford University Press
Forgas, J. P. (2011). Affective influences on self-disclosure: Mood effects on the intimacy and reciprocity
of disclosing personal information. Journal of Personality & Social Psychology , 100(3), 449–461.
https://doi.org/10.1037/a0021129
Gallese, V ., & Lakoff, G. (2005). The Brain’s concepts: The role of the sensory-motor system in conceptual
knowledge. Cognitive Neuropsychology, 22(3–4), 455–479.  h t t p s : / / d o i . o r g / 1 0 . 1 0 8 0 / 0 2 6 4 3 2 9 0 4 4 2 0 0
0 3 1 0
Garaus, M., & Wolfsteiner, E. (2023). Media multitasking, advertising appeal, and gender effects. Review
of Managerial Science, 17(2), 539–567. https://doi.org/10.1007/s11846-022-00535-7
Gardner, M. P. (1985). Mood states and consumer behavior: A critical review. Journal of Consumer
Research, 12(3), 281. https://doi.org/10.1086/208516
Garg, P., Singh, S., Chamola, P., Kumar, A., & Paliwal, M. (2025). Elucidating the linkage between adver-
tisements embedded with emotional appeals and the brand relationship quality during the COVID
pandemic. Journal of Marketing Communications , 31(2), 126–150.  h t t p s  : / / d o i  . o r g /  1 0 . 1  0 8 0 / 1 3 5 2 7 2
6 6 . 2 0 2 3 . 2 2 2 0 3 3 8
Geuens, M., De Pelsmacker, P., & Faseur, T. (2011). Emotional advertising: Revisiting the role of product
category. Journal of Business Research , 64(4), 418–426.  h t t p s  : / / d o i  . o r g /  1 0 . 1  0 1 6 / j . j b u s r e s . 2 0 1 0 . 0 3 .
0 0 1
Ghasemi Siani, M., Mohammadi, S., Soltan Hosseini, M., & Dickson, G. (2021). Comparing young adult
responses to rational and emotional sports product advertisements: the moderating role of product
type and gender. International Journal of Sports Marketing & Sponsorship, 22(4), 798–815.  h t t p s : / /
d o i . o r g / 1 0 . 1 1 0 8 / I J S M S - 0 4 - 2 0 2 0 - 0 0 4 5
Ghorbanzadeh, D. (2021). From satisfaction to loyalty: The role of emotional structures in the process
of transition from satisfaction to loyalty. Asia-Pacific Journal of Business Administration , 13(3),
335–356. https://doi.org/10.1108/APJBA-07-2020-0225
Ghorbanzadeh, D., & Rahehagh, A. (2020). The role of emotional structures in the relationship between
satisfaction and brand loyalty.  Cogent Psychology, 7 (1), 1782098.  h t t p s  : / / d o i  . o r g /  1 0 . 1  0 8 0 / 2 3 3 1 1 9 0
8 . 2 0 2 0 . 1 7 8 2 0 9 8
Gilal, F. G., Gilal, N. G., Martinez, L. F., & Gilal, R. G. (2023). Do all brand CSR initiatives make consum-
ers happy? The role of CSR-brand (mis)fit and sense of relatedness. Journal of Product and Brand
Management, 32(6), 942–957. https://doi.org/10.1108/JPBM-01-2022-3849

1 3
   13  Page 34 of 39
Italian Journal of Marketing         (2026) 2026:13
Gong, Z., & Cummins, R. G. (2020). Redefining rational and emotional advertising appeals as available
Processing Resources: Toward an information processing perspective. Journal of Promotion Man -
agement, 26(2), 277–299. https://doi .org/10.108 0/10496491. 2019.169 9631
Gopinath, S., Thomas, J. S., & Krishnamurthi, L. (2014). Investigating the relationship between the con -
tent of online word of mouth, advertising, and brand performance. Marketing Science, 33(2), 241–
258. https://doi.org/10.1287/mksc.2013.0820
Griffiths, T. L., & Steyvers, M. (2004). Finding scientific topics. Proceedings of the National Academy of
Sciences, 101(suppl_1), 5228–5235. https://doi.org/10.1073/pnas.0307752101
Grün, B., & Hornik, K. (2011). Topicmodels: An R package for fitting topic models. Journal of Statistical
Software, 40(13), 1–30. https://doi.org/10.18637/jss.v040.i13
Grolemund, G., & Wickham, H. (2017). R for data Science: Import, tidy, transform, visualize, and Model
data. O’Reilly Media
Haines, S., & Lee, S. H. (. (2022). One size fits all? Segmenting consumers to predict sustainable fashion
behavior. Journal of Fashion Marketing and Management: An International Journal , 26(2), 383–
398. https://doi.org/10.1108/JFMM-08-2020-0161
Hancock, T., Pentina, I., & Lamendour, E. (2024). Effectiveness of future-focused sustainability appeals in
public service announcements: Roles of emotions and ‘forestalgia’ experiences. Journal of Market-
ing Communications, 1–23. https://doi .org/10.108 0/13527266. 2024.244 6808
Hasan, A. A.-T. (2022). Technology attachment, e-attitude, perceived value, and behavioral intentions
towards uber-ridesharing services: The role of hedonic, utilitarian, epistemic, and symbolic value.
Journal of Contemporary Marketing Science , 5(3), 239–265.  h t t p s : / / d o i . o r g / 1 0 . 1 1 0 8 / j c m a r s - 0 1 - 2 0
2 2 - 0 0 0 2
He, H., Zhu, W., Gouran, D., & Kolo, O. (2016). Moral identity centrality and cause-related marketing:
The moderating effects of brand social responsibility image and emotional brand attachment. Euro-
pean Journal of Marketing, 50(1/2), 236–259. https://doi.org/10.1108/EJM-10-2014-0613
Hernandez-Fernandez, A., & Lewis, M. C. (2019). Brand authenticity leads to perceived value and brand
trust. European Journal of Management and Business Economics , 28(3), 222–238.  h t t p s : / / d o i . o r g / 1
0 . 1 1 0 8 / E J M B E - 1 0 - 2 0 1 7 - 0 0 2 7
Höfling, T. T. A., & Alpers, G. W. (2023). Automatic facial coding predicts self-report of emotion, adver-
tisement and brand effects elicited by video commercials. Frontiers in Neuroscience, 17, 17.  h t t p s : / /
d o i . o r g / 1 0 . 3 3 8 9 / f n i n s . 2 0 2 3 . 1 1 2 5 9 8 3
Higgins, E. T. (1987). Self-discrepancy: A theory relating self and affect. Psychological Review, 94(3),
319–340. https://doi.org/10.1037/0033-295X.94.3.319
Hribar, R., Hrga, T., Papa, G., Petelin, G., Povh, J., Pržulj, N., & Vukašinović, V . (2022). Four algorithms
to solve symmetric multi-type non-negative matrix tri-factorization problem. Journal of Global Opti-
mization, 82(2), 283–312. https://doi.org/10.1007/s10898-021-01074-3
Huang, M. H. (1997). Exploring a new typology of emotional appeals: Basic, versus social, emotional
advertising. Journal of Current Issues and Research in Advertising, 19(2), 23–37.  h t t p s  : / / d o i  . o r g /  1 0
. 1  0 8 0 / 1 0 6 4 1 7 3 4 . 1 9 9 7 . 1 0 5 2 4 4 3 5
Huber, F., Eisele, A., & Meyer, F. (2018). The role of actual, ideal, and ought self-congruence in the con-
sumption of hedonic versus utilitarian brands. Psychology and Marketing, 35(1), 47–63.  h t t p s : / / d o i .
o r g / 1 0 . 1 0 0 2 / m a r . 2 1 0 7 0
Hudson, S., Roth, M. S., Madden, T. J., & Hudson, R. (2015). The effects of social media on emotions,
brand relationship quality, and word of mouth: An empirical study of music festival attendees. Tour-
ism Management, 47, 68–76. https://doi .org/10.101 6/j.tourman .2014.09 .001
Huertas, A., & Marine-Roig, E. (2016). User reactions to destination brand contents in social media. Infor-
mation Technology and Tourism, 15(4), 291–315. https://doi.org/10.1007/s40558-015-0045-9
Hussain, K., Jing, F., Junaid, M., Zaman, Q. U., & Shi, H. (2021). The role of co-creation experience in
engaging customers with service brands. Journal of Product and Brand Management, 30(1), 12–27.
https://doi.org/10.1108/JPBM-08-2019-2537
Japutra, A., Ekinci, Y ., Simkin, L., & Nguyen, B. (2018). The role of ideal self-congruence and brand
attachment in consumers’ negative behaviour: Compulsive buying and external trash-talking. Euro-
pean Journal of Marketing, 52(3/4), 683–701. https://doi.org/10.1108/EJM-06-2016-0318
Joo, B. R., & Kim, H. Y . (2021). Repositioning luxury fashion brands as intentional agents: The roles of
consumer envy and admiration. Journal of Fashion Marketing and Management: An International
Journal, 25(4), 606–624. https://doi.org/10.1108/JFMM-06-2019-0135
Kahneman, D., & Tversky, A. (1979). Prospect theory: An analysis of decision under risk. Econometrica,
47(2), 263–292. https://doi.org/10.2307/1914185

1 3
Page 35 of 39    13
Italian Journal of Marketing         (2026) 2026:13
Kaur, J., Gupta, S., & Singh, L. B. (2023). Role of justification of unethical behaviour in sustainable
fashion consumption among Indian consumers: A parallel mediation approach. Journal of Consumer
Marketing, 40(7), 842–853. https://doi.org/10.1108/JCM-12-2020-4305
Kaya, S. S., Munk, R., Prado, D., & Quoidbach, J. (2025). Emotions shape taste perception in a real res -
taurant environment. International Journal of Gastronomy and Food Science, 39, 39.  h t t p s : / / d o i . o r g
/ 1 0 . 1 0 1 6 / j . i j g f s . 2 0 2 4 . 1 0 1 0 8 0
Keller, K. L. (1993). Conceptualizing, measuring, and managing customer-based brand equity. Journal of
Marketing, 57(1), 1–22. https://doi.org/10.1177/002224299305700101
Keller, K. L., & Swaminathan, V . (2020). Strategic brand Management: Building, Measuring and Manag-
ing brand equity (Fifth ed.). Pearson
Kidwell, B., Hardesty, D. M., & Childers, T. L. (2008). Consumer emotional intelligence: Conceptualiza-
tion, measurement, and the prediction of consumer decision making. Journal of Consumer Research,
35(1), 154–166. https://doi.org/10.1086/524417
Kim, J. (2019). Luxury fashion goods ownership and collecting behavior in an omni-channel retail envi -
ronment: Empirical findings from affluent consumers in the US. Research Journal of Textile and
Apparel, 23(3), 212–231. https://doi.org/10.1108/RJTA-01-2019-0001
Kirk, C. P., & Givi, J. (2025). The AI-authorship effect: Understanding authenticity, moral disgust, and
consumer responses to AI-generated marketing communications. Journal of Business Research, 186,
114984. https://doi .org/10.101 6/j.jbusres .2024.11 4984
Klabi, F. (2020). To what extent do conspicuous consumption and status consumption reinforce the effect
of self-image congruence on emotional brand attachment? Evidence from the Kingdom of Saudi
Arabia. Journal of Marketing Analytics, 8(2), 99–117. https://doi.org/10.1057/s41270-020-00073-9
Kranzbühler, A. M., Zerres, A., Kleijnen, M. H. P., & Verlegh, P. W. J. (2020). Beyond valence: A meta-
analysis of discrete emotions in firm-customer encounters. Journal of the Academy of Marketing
Science, 48(3), 478–498. https://doi.org/10.1007/s11747-019-00707-0
Kucharska, W., Confente, I., & Brunetti, F. (2020). The power of personal brand authenticity and identifi-
cation: Top celebrity players’ contribution to loyalty toward football. Journal of Product and Brand
Management, 29(6), 815–830. https://doi.org/10.1108/JPBM-02-2019-2241
Kurtoğlu, R., Özbölük, T., & Hacıhasanoğlu, P. (2022). Revisiting the effects of inward negative emotions
on outward negative emotions, brand loyalty, and negative WOM. Journal of Brand Management ,
29(1), 72–84. https://doi.org/10.1057/s41262-021-00257-3
Kwon, J., Lin, H., Deng, L., Dellicompagni, T., & Kang, M. Y . (2022). Computerized emotional content
analysis: Empirical findings based on charity social media advertisements. International Journal of
Advertising, 41(7), 1314–1337. https://doi .org/10.108 0/02650487. 2021.201 2070
Larsson, L., & Müller, D. K. (2019). Coping with second home tourism: Responses and strategies of pri -
vate and public service providers in western Sweden. Current Issues in Tourism, 22(16), 1958–1974.
https://doi .org/10.108 0/13683500. 2017.141 1339
Lee, J. J., & Davis Burns, L. (2014). Deliver knowledge or touch the mind? The effect of informational and
emotional advertisement strategy on fashion sportswear brand attitude and recall. Journal of Global
Fashion Marketing, 5(2), 135–148. https://doi.org/10.1080/20932685.2013.878109
Lee, Y . K., Back, K. J., & Kim, J. Y . (2009). Family restaurant brand personality and its impact on Cus-
tomer’s eMotion, satisfaction, and brand loyalty. Journal of Hospitality and Tourism Research, 33(3),
305–328. https://doi.org/10.1177/1096348009338511
Lemon, K. N., & Verhoef, P. C. (2016). Understanding customer experience throughout the customer
journey. Journal of Marketing, 80(6), 69–96. https://doi.org/10.1509/jm.15.0420
Lerner, J. S., Li, Y ., Valdesolo, P., & Kassam, K. S. (2015). Emotion and decision making. Annual Review
of Psychology, 66(1), 799–823. https://doi .org/10.114 6/annurev-p sych-010 213-115043
Leung, L. C., Bougoure, U. S., & Miller, K. W. (2014). The effects of affective and utilitarian brand rela -
tionships on brand consideration. Journal of Brand Management , 21(6), 469–484.  h t t p s : / / d o i . o r g / 1
0 . 1 0 5 7 / b m . 2 0 1 4 . 1 5
Li, F., Su, Q., Guan, J., & Zhang, G. (2023). Communicate like humans? Anthropomorphism and hotel
consumers’ willingness to pay a premium price. Journal of Hospitality and Tourism Management, 56,
482–492. https://doi.org/10.1016/j.jhtm.2023.08.008
Lindstrom, M. (2005). Broad sensory branding. Journal of Product and Brand Management, 14(2), 84–87.
https://doi.org/10.1108/10610420510592554
Lin, I. Y . (2016). Effects of visual servicescape aesthetics comprehension and appreciation on consumer
experience. The Journal of Services Marketing , 30(7), 692–712.  h t t p s : / / d o i . o r g / 1 0 . 1 1 0 8 / J S M - 0 8 - 2 0
1 5 - 0 2 5 8

1 3
   13  Page 36 of 39
Italian Journal of Marketing         (2026) 2026:13
Li, R., Laroche, M., Richard, M. O., & Cui, X. (2022). More than a mere cup of coffee: When perceived
luxuriousness triggers Chinese customers’ perceptions of quality and self-congruity. Journal of
Retailing & Consumer Services, 64, 102759. https://doi .org/10.101 6/j.jretcon ser.2021 .102759
Liu, B., Moyle, B., Kralj, A., & Li, Y . (2024). Towards a typology of virtual tourists: Efficacy of visual
patterns and attentional cues. Tourism Management, 105, 104943.  h t t p s  : / / d o i  . o r g /  1 0 . 1  0 1 6 / j . t o u r m a n
. 2 0 2 4 . 1 0 4 9 4 3
Liu, Y ., & Lei, K. (2025). The impact of human and virtual endorsements on advertising effectiveness: A
comparative analysis based on different information appeals. Humanities and Social Sciences Com-
munications, 12(1). https://doi.org/10.1057/s41599-025-04509-4
Loewenstein, G. F., Weber, E. U., Hsee, C. K., & Welch, N. (2001). Risk as Feelings. Psychological Bul-
letin, 127(2), 267–286. https://doi.org/10.1037/0033-2909.127.2.267
Long Yi, L. (2011). The impact of advertising appeals and advertising spokespersons on advertising atti -
tudes and purchase intentions. African Journal of Business Management, 5(21), 8446–8457.  h t t p s : / /
d o i . o r g / 1 0 . 5 8 9 7 / a j b m 1 1 . 9 2 5
Luo, J. M., Hu, Z., & Law, R. (2024). Exploring online consumer experiences and experiential emotions
offered by travel websites that accept cryptocurrency payments. International Journal of Hospitality.
Management, 119, 119. https://doi.org/10.1016/j.ijhm.2024.103721
Macpherson, A., & Holt, R. (2007). Knowledge, learning and small firm growth: A systematic review of
the evidence. Research Policy, 36(2), 172–192. https://doi.org/10.1016/j.respol.2006.10.001
Madadi, R., Torres, I. M., & Zúñiga, M. Á. (2024). The semiotics of emojis in advertising: An integrated
quantitative and qualitative examination of emotional versus functional ad dynamics. Psychology
and Marketing, 41(6), 1223–1241. https://doi.org/10.1002/mar.21972
Malär, L., Krohmer, H., Hoyer, W. D., & Nyffenegger, B. (2011). Emotional brand attachment and brand
personality: The relative importance of the actual and the ideal self. Journal of Marketing , 75(4),
35–52. https://doi.org/10.1509/jmkg.75.4.35
Manohar, S., Kumar, R., Saha, R., & Mittal, A. (2023). Examining the effect of emotional branding in
building brand equity of social marketing campaigns: A case on Swachh Bharat, India. Society and
Business Review, 18(2), 197–218. https://doi.org/10.1108/SBR-09-2021-0159
Megías, A., Maldonado, A., Catena, A., Di Stasi, L. L., Serrano, J., & Cándido, A. (2011). Modulation
of attention and urgent decisions by affect-laden roadside advertisement in risky driving scenarios.
Safety Science, 49(10), 1388–1393. https://doi.org/10.1016/j.ssci.2011.06.001
Mehmood, S., Gulzar, A., Malik, I. A., Raza, M. A., & Mujtaba, B. G. (2022). Emotional and rational
advertising appeal on children’s wellbeing: Assessing the moderating role of parental support. SN
Social Sciences, 2(1). https://doi.org/10.1007/s43545-021-00306-3
Mitchell, A. A., & Olson, J. C. (1981). Are Product attribute beliefs the only Mediator of advertising effects
on brand attitude? Journal of Marketing Research , 18(3), 318–332.  h t t p s : / / d o i . o r g / 1 0 . 1 1 7 7 / 0 0 2 2 2 4
3 7 8 1 0 1 8 0 0 3 0 6
Monauni, M. (2017). Closing the strategy execution gap through business simulations. Development and
Learning in Organizations: An International Journal , 31(4), 9–12.  h t t p s : / / d o i . o r g / 1 0 . 1 1 0 8 / D L O - 0
8 - 2 0 1 6 - 0 0 6 9
Mostafa, R. B., & Kasamani, T. (2021). Brand experience and brand loyalty: Is it a matter of emotions?
Asia Pacific Journal of Marketing and Logistics , 33(4), 1033–1051.  h t t p s : / / d o i . o r g / 1 0 . 1 1 0 8 / A P J M
L - 1 1 - 2 0 1 9 - 0 6 6 9
Muehling, D. D., Sprott, D. E., & Sultan, A. J. (2014). Exploring the boundaries of nostalgic advertising
effects: A consideration of childhood brand exposure and attachment on consumers’ responses to
nostalgia-themed advertisements. Journal of Advertising , 43(1), 73–84.  h t t p s : / / d o i . o r g / 1 0 . 1 0 8 0 / 0 0
9 1 3 3 6 7 . 2 0 1 3 . 8 1 5 1 1 0
Napoli, J., Dickinson, S. J., Beverland, M. B., & Farrelly, F. (2014). Measuring consumer-based brand
authenticity. Journal of Business Research , 67(6), 1090–1098.  h t t p s  : / / d o i  . o r g /  1 0 . 1  0 1 6 / j . j b u s r e s . 2 0
1 3 . 0 6 . 0 0 1
Nielsen, J. H., Shapiro, S. A., & Mason, C. H. (2010). Emotionality and semantic onsets: Exploring orient-
ing attention responses in advertising. Journal of Marketing Research, 47(6), 1138–1150.  h t t p s : / / d o
i . o r g / 1 0 . 1 5 0 9 / j m k r . 4 7 . 6 . 1 1 3 8
Nie, T., He, J., Mei, Y ., Qin, G., Li, G., Sun, J., & Ma, W. (2025). Joint estimation and prediction of city-
wide delivery demand: A large language model empowered graph-based learning approach. Trans-
portation Research Part E: Logistics and Transportation Review, 197 , 104075.  h t t p s : / / d o i . o r g / 1 0 . 1
0 1 6 / j . t r e . 2 0 2 5 . 1 0 4 0 7 5

1 3
Page 37 of 39    13
Italian Journal of Marketing         (2026) 2026:13
Oliver, R. L. (1999). Whence consumer loyalty? Journal of Marketing, 63(4_suppl1), 33–44.  h t t p s : / / d o i . o
r g / 1 0 . 1 1 7 7 / 0 0 2 2 2 4 2 9 9 9 0 6 3 4 s 1 0 5
Pang, J., Keh, H. T., & Peng, S. (2009). Effects of advertising strategy on consumer-brand relationships:
A brand love perspective. Frontiers of Business Research in China, 3(4), 599–620.  h t t p s : / / d o i . o r g / 1
0 . 1 0 0 7 / s 1 1 7 8 2 - 0 0 9 - 0 0 2 9 - 8
Park, C. L., & Nunes, M. F. (2025). The use of (non)exotic leathers by (non)favourite luxury brands: An
attachment theory perspective. Journal of Retailing & Consumer Services, 84, 104249.  h t t p s  : / / d o i  . o
r g /  1 0 . 1  0 1 6 / j . j r e t c o n s e r . 2 0 2 5 . 1 0 4 2 4 9
Phillips, B. J. (1997). Thinking into it: Consumer interpretation of complex advertising images. Journal of
Advertising, 26(2), 77–87. https://doi .org/10.108 0/00913367. 1997.106 73524
Phillips, B. J., & McQuarrie, E. F. (2004). Beyond visual metaphor: A new typology of visual rhetoric in
advertising. Marketing Theory, 4(1–2), 113–136. https://doi.org/10.1177/1470593104044089
Plummer, M. (2023). Simulation-based Bayesian analysis. Annual Review of Statistics and Its Application,
10, 401–425. https://doi.org/10.1146/annurev-statistics-  122121 -040905
Poels, K., & Dewitte, S. (2006). How to capture the heart? Reviewing 20 years of emotion measurement
in advertising. Journal of Advertising Research , 46(1), 18–37.  h t t p s : / / d o i . o r g / 1 0 . 2 5 0 1 / S 0 0 2 1 8 4 9 9 0
6 0 6 0 0 4 1
Rahimah, A., Dang, H. P., Nguyen, T. T., Cheng, J. M. S., & Kusumawati, A. (2023). The subsequent
effects of negative emotions: From brand hate to anti-brand consumption behavior under moderating
mechanisms. Journal of Product and Brand Management , 32(4), 618–631.  h t t p s : / / d o i . o r g / 1 0 . 1 1 0 8 /
J P B M - 1 2 - 2 0 2 1 - 3 7 7 8
Ramirez, E., Gau, R., Hadjimarcou, J., & Xu, Z. (. (2018). User-generated content as word-of-mouth.
Journal of Marketing Theory and Practice , 26(1–2), 90–98). Routledge.  h t t p s  : / / d o i  . o r g /  1 0 . 1  0 8 0 / 1 0
6 9 6 6 7 9 . 2 0 1 7 . 1 3 8 9 2 3 9
Rathnayake, D. T. (2021). Gen Y consumers’ brand loyalty: A brand romance perspective. Marketing Intel-
ligence and Planning, 39(6), 761–776. https://doi.org/10.1108/MIP-09-2020-0421
Rhue, L. (2024). The anchoring effect, algorithmic fairness, and the limits of information transparency for
emotion artificial intelligence. Information Systems Research, 35(3), 1479–1496.  h t t p s : / / d o i . o r g / 1 0 .
1 2 8 7 / i s r e . 2 0 1 9 . 0 4 9 3
Ried, L., Kaufmann, L., & Schreiner, M. (2025). The surprisingly robust effects of narratives in supplier
negotiations. Journal of Supply Chain Management , 61(2), 33–52.  h t t p s : / / d o i . o r g / 1 0 . 1 1 1 1 / j s c m . 1 2
3 4 3
Romero, P. M., Lim, R. E., & Park, H. (2025). Branded virtual worlds in fashion gaming: Examining the
role of brand narratives and social presence in consumer engagement. Computers in Human Behav-
ior, 164, 164. https://doi.org/10.1016/j.chb.2024.108505
Roozenbeek, J., & van der Linden, S. (2019). The fake news game: Actively inoculating against the risk
of misinformation. Journal of Risk Research, 22(5), 570–580.  h t t p s  : / / d o i  . o r g /  1 0 . 1  0 8 0 / 1 3 6 6 9 8 7 7 . 2 0
1 8 . 1 4 4 3 4 9 1
Ruihley, B. J., & Pate, J. R. (2017). For the love of sport: Examining sport emotion through a Lovemarks
lens. Communication & Sport, 5(2), 135–159. https://doi.org/10.1177/2167479515607048
Salovey, P., & Mayer, J. D. (1990). Emotional intelligence. Imagination, Cognition and Personality, 9(3),
185–211. https://doi.org/10.2190/DUGG-P24E-52WK-6CDG
Schachter, S., Festinger, L., Willerman, B., & Hyman, R. (1961). Emotional disruption and industrial pro-
ductivity. Journal of Applied Psychology, 45(4), 201–213. https://doi.org/10.1037/h0042877
Schmitt, B. (1999). Experiential Marketing. Journal of Marketing Management, 15(1–3), 53–67.  h t t p s : / / d
o i . o r g / 1 0 . 1 3 6 2 / 0 2 6 7 2 5 7 9 9 7 8 4 8 7 0 4 9 6
Schmitt, B. (2012). The consumer psychology of brands. Journal of Consumer Psychology, 22(1), 7–17.
https://doi.org/10.1016/j.jcps.2011.09.005
Schnebelen, S., & Bruhn, M. (2018). An appraisal framework of the determinants and consequences of
brand happiness. Psychology and Marketing, 35(2), 101–119. https://doi.org/10.1002/mar.21073
Shahid, S., Paul, J., Gilal, F. G., & Ansari, S. (2022). The role of sensory marketing and brand experience
in building emotional attachment and brand loyalty in luxury retail stores. Psychology and Market-
ing, 39(7), 1398–1412. https://doi.org/10.1002/mar.21661
Sharif, K., & Sidi Lemine, M. (2024). Customer service quality, emotional brand attachment and customer
citizenship behaviors: Findings from an emerging higher education market. Journal of Marketing for
Higher Education, 34(1), 18–43. https://doi .org/10.108 0/08841241. 2021.194 9659

1 3
   13  Page 38 of 39
Italian Journal of Marketing         (2026) 2026:13
Sharma, K., Trott, S., Sahadev, S., & Singh, R. (2023). Emotions and consumer behaviour: A review and
research agenda. International Journal of Consumer Studies , 47(6), 2396–2416.  h t t p s : / / d o i . o r g / 1 0 .
1 1 1 1 / i j c s . 1 2 9 3 7
Sirgy, M. J. (1982). Self-concept in consumer behavior: A critical review. Journal of Consumer Research,
9(3), 287–300. https://doi.org/10.1086/208924
Sudbury-Riley, L., & Edgar, L. (2016). Why older adults show preference for rational over emotional
advertising appeals: A U.K. brand study challenges the applicability of socioemotional selectivity
theory to advertising. Journal of Advertising Research , 56(4), 441–455.  h t t p s : / / d o i . o r g / 1 0 . 2 5 0 1 / J A
R - 2 0 1 6 - 0 4 8
Sung, B., Yih, J., & Wilson, N. J. (2020). Individual differences in experience after a control task: Bore -
dom proneness, curiosity, and grit correlate with emotion. Australian Journal of Psychology, 72(2),
211–222. https://doi.org/10.1111/ajpy.12268
Talebzadeh, N., Yorganci, I., Nosrati, S., & Kilic, C. (2024). Residents’ emotional and behavioral responses
to visiting Maras (Varosha) as a dark tourism spot. Journal of Heritage Tourism , 19(4), 577–600.
https://doi .org/10.108 0/1743873X. 2024.230 2535
Taqi, M., Bagozzi, R. P., Tuğrul, T., & Yaprak, A. (2025). The phenomenon of brand hate: A systematic
literature review. Journal of Marketing Theory and Practice, 33(4), 649–676.  h t t p s  : / / d o i  . o r g /  1 0 . 1  0 8
0 / 1 0 6 9 6 6 7 9 . 2 0 2 4 . 2 3 7 6 0 2 1
Teal, R., Roberts, M., Harrigan, P., Clarkson, J., & Rosenberg, M. (2020). Leveraging spectator emotion: A
review and conceptual framework for marketing health behaviors in elite sports. Sport Management
Review, 23(2), 183–199. https://doi.org/10.1016/j.smr.2019.05.003
Teixeira, T., Wedel, M., & Pieters, R. (2012). Emotion-induced engagement in internet video advertise -
ments. Journal of Marketing Research, 49(2), 144–159. https://doi.org/10.1509/jmr.10.0207
Thomson, M., MacInnis, D. J., & Park, C. W. (2005). The ties that bind: Measuring the strength of con -
sumers’ emotional attachments to brands. Journal of Consumer Psychology, 15(1), 77–91.  h t t p s : / / d o
i . o r g / 1 0 . 1 2 0 7 / s 1 5 3 2 7 6 6 3 j c p 1 5 0 1 _ 1 0
Tsujimoto, M., Yoshida, T., Tanaka, S., Shitara, H., & Suzuki, K. (2024). Variable physical functions in
individuals in response to sensory stimuli. Sport Sciences for Health, 20(2), 577–584.  h t t p s : / / d o i . o r
g / 1 0 . 1 0 0 7 / s 1 1 3 3 2 - 0 2 3 - 0 1 1 4 2 - z
Vahdat, A., Hafezniya, H., Jabarzadeh, Y ., & Thaichon, P. (2020). Emotional brand attachment and attitude
toward brand extension. Services Marketing Quarterly, 41(3), 236–255.  h t t p s  : / / d o i  . o r g /  1 0 . 1  0 8 0 / 1 5 3
3 2 9 6 9 . 2 0 2 0 . 1 7 8 6 2 4 5
Van Den Bergh, B., Dewitte, S., & Warlop, L. (2008). Bikinis instigate generalized impatience in intertem-
poral choice. Journal of Consumer Research, 35(1), 85–97. https://doi.org/10.1086/525505
van der Linden, S., Panagopoulos, C., & Roozenbeek, J. (2020). You are fake news: Political bias in per -
ceptions of fake news. Media Culture & Society , 42(3), 460–470.  h t t p s : / / d o i . o r g / 1 0 . 1 1 7 7 / 0 1 6 3 4 4 3
7 2 0 9 0 6 9 9 2
Venkatesh, V ., & Bala, H. (2008). Technology acceptance model 3 and a research agenda on interventions.
Decision Sciences, 39(2), 273–315. https://doi .org/10.111 1/j.1540-59 15.2008. 00192.x
Vivek, S. D., Beatty, S. E., & Morgan, R. M. (2012). Customer engagement: Exploring customer relation-
ships beyond purchase. Journal of Marketing Theory and Practice , 20(2), 122–146.  h t t p s : / / d o i . o r g /
1 0 . 2 7 5 3 / M T P 1 0 6 9 - 6 6 7 9 2 0 0 2 0 1
Wang, F., Jiang, J., & Cosenz, F. (2025). Understanding data-driven business model innovation in com -
plexity: A system dynamics approach. Journal of Business Research, 186, 114967.  h t t p s  : / / d o i  . o r g /  1
0 . 1  0 1 6 / j . j b u s r e s . 2 0 2 4 . 1 1 4 9 6 7
Warren, C., Batra, R., Loureiro, S. M. C., & Bagozzi, R. P. (2019). Brand coolness. Journal of Marketing,
83(5), 36–56. https://doi.org/10.1177/0022242919857698
Wickham, H. (2016). ggplot2: Elegant graphics for data analysis (2nd ed.). Springer.  h t t p s : / / d o i . o r g / 1 0 . 1
0 0 7 / 9 7 8 - 3 - 3 1 9 - 2 4 2 7 7 - 4
Williams, P., & Drolet, A. (2005). Age-related differences in responses to emotional advertisements. Jour-
nal of Consumer Research, 32(3), 343–354. https://doi.org/10.1086/497545
Witt, U. (2010). Symbolic consumption and the social construction of product characteristics. Structural
Change and Economic Dynamics, 21(1), 17–25. https://doi.org/10.1016/j.strueco.2009. 11 . 008
Wu, Y . L., & Chen, P. C. (2024). Neurophysiology of sensory imagery: An effort to improve online adver-
tising effectiveness through science laboratory experimentation. Information & Management, 61(4),
103708. https://doi.org/10.1016/j.im.2022.103708

1 3
Page 39 of 39    13
Italian Journal of Marketing         (2026) 2026:13
Wu, Z., Lei, L., Li, G., Huang, H., Zheng, C., Chen, E., & Xu, G. (2017). A topic modeling based approach
to novel document automatic summarization. Expert Systems with Applications, 84, 12–23.  h t t p s : / / d
o i . o r g / 1 0 . 1 0 1 6 / j . e s w a . 2 0 1 7 . 0 4 . 0 5 4
Yang, K., Kim, H. M., & Zimmerman, J. (2020). Emotional branding on fashion brand websites: Harness-
ing the pleasure-arousal-dominance (P-A-D) model. Journal of Fashion Marketing and Manage -
ment: An International Journal, 24(4), 555–570. https://doi.org/10.1108/JFMM-03-2019-0055
Young, C., Gillespie, B., & Otto, C. (2019). The impact of rational, Emotional,And physiological advertis-
ing images on purchase intention. Journal of Advertising Research, 59(3), 329–341.  h t t p s : / / d o i . o r g /
1 0 . 2 5 0 1 / J A R - 2 0 1 9 - 0 1 0
Zhang, H., Sun, J., Liu, F., & Knight, J. G. (2014). Be rational or be emotional: Advertising appeals, ser -
vice types and consumer responses. European Journal of Marketing, 48(11/12), 2105–2126.  h t t p s : / /
d o i . o r g / 1 0 . 1 1 0 8 / E J M - 1 0 - 2 0 1 2 - 0 6 1 3
Zhou, R., & Tong, L. (2022). A study on the influencing factors of consumers’ purchase intention during
livestreaming e-commerce: The mediating effect of emotion. Frontiers in Psychology, 13.  h t t p s : / / d o
i . o r g / 1 0 . 3 3 8 9 / f p s y g . 2 0 2 2 . 9 0 3 0 2 3
Zhou, T., Wang, Y ., Yan, L.(Lucy), & Tan, Y . (2023). Spoiled for choice? Personalized recommenda-
tion for healthcare decisions: A multiarmed bandit approach. Information Systems Research, 34(4),
1493–1512. https://doi.org/10.1287/isre.2022.1191
Zou, Y ., Liao, J., & Jin, D. (2025). The effects of tourists’ digital attachment on behavioural intention in
live-streaming tourism. Current Issues in Tourism, 28(17), 2803–2824.  h t t    p  s :  /  / d  o i . o  r g  / 1  0 . 1 0 8 0 / 1 3 6
8 3 5 0 0 . 2 0 2 4 . 2 3 8 1 2 4 6
Publisher’s Note Springer Nature remains neutral with regard to jurisdictional claims in published maps
and institutional affiliations.
