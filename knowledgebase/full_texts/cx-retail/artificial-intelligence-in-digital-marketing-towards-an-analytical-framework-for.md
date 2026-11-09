---
title: 'Artificial Intelligence in Digital Marketing: Towards an Analytical Framework for Revealing and
  Mitigating Bias'
url: https://doi.org/10.3390/bdcc9020040
category: cx-retail
subcategory: framework
date: 2025-02
venue: Big Data and Cognitive Computing
authors:
- Catherine Reed
- Martín Wynn
- Robin Bown
source: openalex-oa
pdf_url: https://eprints.glos.ac.uk/14764/9/14764%20Reed%20et%20al.%20%282025%29%20Artificial%20Intelligence%20in%20Digital%20Marketing.pdf
pages: 25
chars: 95679
fetched_at: '2026-11-08T17:02:47+00:00'
kb_version: 1
---

# Artificial Intelligence in Digital Marketing: Towards an Analytical Framework for Revealing and Mitigating Bias

This is a peer-reviewed, final published version of the following document, ©2025 by the
authors. Licensee MDPI, Basel, Switzerland. and is licensed under Creative Commons:
Attribution 4.0 license:
Reed, Catherine, Wynn, Martin G ORCID logoORCID:
https://orcid.org/0000-0001-7619-6079 and Bown, G Robin
ORCID logoORCID: https://orcid.org/0000-0001-7793-108X
(2025) Artificial Intelligence in Digital Marketing: Towards an
Analytical Framework for Revealing and Mitigating Bias. Big
Data and Cognitive Computing, 9 (2). art 40.
doi:10.3390/bdcc9020040
Official URL: https://doi.org/10.3390/bdcc9020040
DOI: http://dx.doi.org/10.3390/bdcc9020040
EPrint URI: https://eprints.glos.ac.uk/id/eprint/14764
Disclaimer
The University of Gloucestershire has obtained warranties from all depositors as to their title in
the material deposited and as to their right to deposit such material.
The University of Gloucestershire makes no representation or warranties of commercial utility,
title, or fitness for a particular purpose or any other warranty, express or implied in respect of
any material deposited.
The University of Gloucestershire makes no representation that the use of the materials will not
infringe any patent, copyright, trademark or other property or proprietary rights.
The University of Gloucestershire accepts no liability for any infringement of intellectual
property rights in any material deposited but will remove such material from public view
pending investigation in the event of an allegation of any such infringement.
PLEASE SCROLL DOWN FOR TEXT.

This is a peer-reviewed, final published version of the following document:
Reed, Catherine, Wynn, Martin G ORCID logoORCID:
https://orcid.org/0000-0001-7619-6079 and Bown, G Robin
ORCID logoORCID: https://orcid.org/0000-0001-7793-108X
(2025) Artificial Intelligence in Digital Marketing: Towards an
Analytical Framework for Revealing and Mitigating Bias. Big
Data and Cognitive Computing, 9 (40). pp. 1-23.
doi:10.3390/bdcc9020040
Official URL: https://www.mdpi.com/journal/BDCC
DOI: https://doi.org/10.3390/bdcc9020040
EPrint URI: https://eprints.glos.ac.uk/id/eprint/14764
Disclaimer
The University of Gloucestershire has obtained warranties from all depositors as to their title in
the material deposited and as to their right to deposit such material.
The University of Gloucestershire makes no representation or warranties of commercial utility,
title, or fitness for a particular purpose or any other warranty, express or implied in respect of
any material deposited.
The University of Gloucestershire makes no representation that the use of the materials will not
infringe any patent, copyright, trademark or other property or proprietary rights.
The University of Gloucestershire accepts no liability for any infringement of intellectual
property rights in any material deposited but will remove such material from public view
pending investigation in the event of an allegation of any such infringement.
PLEASE SCROLL DOWN FOR TEXT.

Academic Editor: Domenico Ursino
Received: 31 December 2024
Revised: 28 January 2025
Accepted: 8 February 2025
Published: 12 February 2025
Citation: Reed, C.; Wynn, M.; Bown,
R. Artificial Intelligence in Digital
Marketing: Towards an Analytical
Framework for Revealing and
Mitigating Bias. Big Data Cogn.
Comput. 2025, 9, 40. https://doi.org/
10.3390/bdcc9020040
Copyright: © 2025 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license
(https://creativecommons.org/
licenses/by/4.0/).
Article
Artificial Intelligence in Digital Marketing: Towards an
Analytical Framework for Revealing and Mitigating Bias
Catherine Reed, Martin Wynn *
 and Robin Bown
School of Business, Computing and Social Sciences, University of Gloucestershire, Cheltenham GL50 2RH, UK;
catherinereed@connect.glos.ac.uk (C.R.); rbown@glos.ac.uk (R.B.)
* Correspondence: mwynn@glos.ac.uk
Abstract: Artificial intelligence (AI) affects many aspects of modern life, and most predic-
tions are that the impact of AI on business and society will only increase. In the marketing
function of today’s leading businesses, two main types of AI can be discerned. Traditional
AI centres on supervised learning algorithms to support and enable the application of
data rules, predictive functionality and other AI-based features. Generative AI, on the
other hand, uses large language model (LLM) data sets and user prompts to generate new
content. While AI-generated applications and content can boost efficiency, they also present
challenges regarding transparency and authenticity, and the question of bias is central to
these concerns. This article adopts a qualitative inductive approach to research this issue in
the context of the marketing function of a global software supplier. Based on a systematic
literature review and in-depth interviews with company marketeers, the perceived bias
issues in coding, prompting and deployment of AI in digital marketing are identified .
Then, based on a provisional conceptual framework derived from the extant literature, an
analytical framework for revealing and mitigating bias in digital marketing is put forward,
incorporating the perspectives of industry-based practitioners. The framework can be
used as a checklist of marketing activities in which bias may exist in either traditional or
generative AI across different stages of the customer journey. The article thus contributes to
the development of theory and practice regarding the management of bias in AI-generated
content and will be of interest to researchers and practitioners as an operational guide and
point of departure for subsequent studies.
Keywords: artificial intelligence; generative AI; marketing; digital marketing; bias; digital
transformation; martech stack; marketing customer journey
1. Introduction
Artificial Intelligence (AI) is conceptualised by some authors as the Intelligence Revo-
lution: “AI draws strength from the Internet, finally starting a major revolution comparable
to the previous technological revolutions” [ 1] (p. 12). The Intelligence Revolution will
completely change our society in many regards, but it is at risk, like any new technology, of
being misused if not correctly regulated. Within businesses, marketeers are being encour-
aged to use AI for marketing strategy execution and optimisation, from dynamic content
creation to data profiling, but with little implementation guidance [2].
Bias exists in everything we do, and bias propagation is already well documented
as being perpetuated in marketing through the marketeer [ 3]; however, AI usage can
compound already existent bias propagation. Currently, there is no global governance
to regulate AI usage in business, resulting in a lack of governance for employees using
Big Data Cogn. Comput. 2025, 9, 40 https://doi.org/10.3390/bdcc9020040

Big Data Cogn. Comput. 2025, 9, 40 2 of 23
it within their companies [4]. Nevertheless, a 2023 Gartner survey revealed that 63% of
marketing leaders planned to invest and adopt AI in their marketing practices within
the next 24 months [ 5] and that this adoption was estimated to produce an increase in
productivity of more than 40% in the next five years [6]. Whilst it is generally accepted that
bias is evident in most marketing-related activities, there is a dearth of research literature on
how to identify and mitigate bias in AI-driven marketing. Existing studies lack specificity
in this regard, and this article addresses this gap in the literature by providing a framework
from which a strategy and action plan can be developed to identify and manage bias in
marketing activities. In this context, this research aims to engender the implementation of
improved ethical marketing practices when using AI and, more specifically, addresses two
research questions (RQs):
RQ1. What are the current and perceived bias issues in coding, prompting and
deploying AI in digital marketing?
RQ2. What framework can be developed to provide guidance for practitioners to
reveal and mitigate bias in AI deployment in digital marketing?
Following this introduction, the article comprises five further sections. In Section 2,
the relevant literature is reviewed, and a provisional conceptual framework for the study is
developed as a basis for the primary research. In Section 3, the selection of the research
method is discussed. Section 4 then sets out the research results and addresses the research
questions. Section 5 is a discussion section that examines a number of emergent themes
that do not directly address the RQs but are still of relevance to the overall aim of the
research. The concluding Section 6 summarises the contribution of the research, outlines its
limitations and points out possible future areas for research in this field.
2. Literature Review
This systematic literature review uses a PRISMA (Preferred Reporting Items for Sys-
tematic Review or Meta-Analysis) flow to locate and determine the relevance of the liter-
ature to the overall research aim and research questions [7] (Figure 1). A comprehensive
search was used on various research databases between February and July 2024, using
the keywords “artificial intelligence”, “marketing”, “bias”, “marketing technology” and
“marketing customer journey”. The initial search delivered 1845 results, and after removing
duplication, 985 sources remained. To ensure relevance and applicability, these articles were
screened with two filters: the first to ensure relevance to the research area and the second
to restrict publication dates between January 2016 and July 2024. Broad search terms were
deliberately used to gain a holistic picture of the literature for AI, bias and digital marketing;
however, each piece of literature had to focus on at least two of these three core areas to
be eligible. Once the publication period had been applied and a meticulous screening of
relevant literature had been conducted, the final count of core sources for the research
project was 141. The analysis of these sources provided some initial findings as regards
RQ1, which are extended and developed in light of the primary research results reported in
Section 4. This literature synthesis allowed a categorisation of findings and development
of the provisional conceptual framework, which was then used for questionnaire and
interview design.

Big Data Cogn. Comput. 2025, 9, 40 3 of 23
Big Data Cogn. Comput. 2025, 9, x FOR PEER REVIEW 3 of 24

Figure 1. PRISMA ﬂow diagram for the systematic literature review.
2.1. Artiﬁcial Intelligence and Bias in Marketing
There are two main aspects of AI of relevance to digital marketing. First, supervised
learning algorithms (a category of machine learning) are used in combination with other
technologies within the marketing technology stack (Martech Stack), supporting and en-
abling the application of data rules, predicti ve functionality and other AI-based features
[2,8]. This is often seen as “Traditional AI” or “Weak AI”, and is limited to programmed
rules and inputs, making it more accurately described as “augmented intelligence” re-
quiring human oversight [9,10]. The second is  generative AI, which uses large learning
model data sets and user prompts to generate new content [1].
The Martech Stack is a collection of integr ated software made up of customer rela-
tionship management (CRM) systems, social media, analytics, and websites that may use
real-time AI algorithms to optimise usage [ 11]. AI improves these systems by modelling
predictive outcomes, algorithmic clusters and enabling personalisation at scale; however,
it risks introducing biases from incomplete or skewed datasets, potentially suppressing
genuine buyers and misrepresenting consumer behaviour. Continuous human oversight
is critical to maintain ethical marketing funnels and prevent automated biases from inﬂu-
encing decision-making [2,12,13].
Generative AI enhances eﬃciency by automating text, image, audio, and video con-
tent creation, which is crucial for reaching diverse audiences. For instance, AI-driven tools
streamline tasks like blog writing, social media updates, and email newsletters, allowing
marketers more time for strategic innovation [14,15]. Content production constitutes 26%
of marketing budgets, with 4% spent on localisation [16,17]. Generative AI can save mar-
keters 25–74% of their time [18]. However, marketing personas, based on job titles, de-
mographics, and industries, risk excluding or discriminating against outliers—continuing
to perpetuate biases in communication strategies. AI algorithms excel in recognising pat-
terns and sentiments, oﬀering cost-eﬀective, scalable visual content personalisation [19].
Despite time savings, unmoderated content can expose companies to reputational
risks. Tools like DALL-E source data from platforms like Google Images, and these plat-
Figure 1. PRISMA flow diagram for the systematic literature review.
2.1. Artificial Intelligence and Bias in Marketing
There are two main aspects of AI of relevance to digital marketing. First, super-
vised learning algorithms (a category of machine learning) are used in combination with
other technologies within the marketing technology stack (Martech Stack), supporting
and enabling the application of data rules, predictive functionality and other AI-based
features [2,8]. This is often seen as “Traditional AI” or “Weak AI”, and is limited to
programmed rules and inputs, making it more accurately described as “augmented intelli-
gence” requiring human oversight [9,10]. The second is generative AI, which uses large
learning model data sets and user prompts to generate new content [1].
The Martech Stack is a collection of integrated software made up of customer rela-
tionship management (CRM) systems, social media, analytics, and websites that may use
real-time AI algorithms to optimise usage [11]. AI improves these systems by modelling
predictive outcomes, algorithmic clusters and enabling personalisation at scale; however,
it risks introducing biases from incomplete or skewed datasets, potentially suppressing
genuine buyers and misrepresenting consumer behaviour. Continuous human oversight is
critical to maintain ethical marketing funnels and prevent automated biases from influenc-
ing decision-making [2,12,13].
Generative AI enhances efficiency by automating text, image, audio, and video content
creation, which is crucial for reaching diverse audiences. For instance, AI-driven tools
streamline tasks like blog writing, social media updates, and email newsletters, allowing
marketers more time for strategic innovation [14,15]. Content production constitutes 26% of
marketing budgets, with 4% spent on localisation [16,17]. Generative AI can save marketers
25–74% of their time [18]. However, marketing personas, based on job titles, demographics,
and industries, risk excluding or discriminating against outliers—continuing to perpetu-
ate biases in communication strategies. AI algorithms excel in recognising patterns and
sentiments, offering cost-effective, scalable visual content personalisation [19].
Despite time savings, unmoderated content can expose companies to reputational risks.
Tools like DALL-E source data from platforms like Google Images, and these platforms can
introduce biases. Research by Sun et al. [20] shows gender imbalances in occupational image

Big Data Cogn. Comput. 2025, 9, 40 4 of 23
searches, underrepresenting women in male-dominated fields and overrepresenting men
in female-dominated ones. Additionally, a Eurocentric aesthetic bias persists, excluding
diverse cultural representations [21]. These biases extend to AI-generated image captions,
crucial for accessibility but often prone to gender misclassification, requiring human review
until algorithms improve [22].
Audio and video AI systems also perpetuate biases. Tatman [ 23] found YouTube’s
voice recognition 13% less accurate for women, with linguistic minorities and regional
accents facing lower accuracy than standard American or Received Pronunciation accents.
Koenecke et al. [24] expanded on this, revealing that automatic speech recognition (ASR)
systems misidentified 35% of words from Black speakers compared to 19% from White
speakers, reflecting a systemic bias in speech technologies. Marketeers use these platforms
to create content or host their content to customers and not all will know the partiality
and bias that is already well researched and identified within them. Bias permeates all
marketing touchpoints due to human involvement. Marketing thrives on consumer biases,
predicting purchasing habits to engage prospects at optimal moments [25]. However, the
lack of a standardised framework for addressing bias in AI-driven marketing complicates
ethical considerations. Bias is often inherent and difficult to categorise, allowing it to
manifest in various forms when marketers use AI tools [26].
The influence of major tech companies on AI development introduces further com-
plications. These large international corporations may prioritise efficiency and profit over
data integrity, leading to biased outcomes [ 4,27]. Machine learning heuristics—quick,
approximate solutions—drive AI speed and scalability, but often at the expense of accu-
racy and fairness [28]. Transparency and accountability are limited due to the proprietary
nature of these algorithms, raising ethical concerns [ 29]. Martech stacks, built on big
tech platforms, inherit these biases, embedding flawed decision-making processes into
business software, including marketing software. By 2023, the U.S. led AI development
with 61 machine-learning models, followed by Europe (19) and China (7). However, rapid
innovation in Silicon Valley focuses more on boosting stock prices than ensuring ethical AI
development [30].
Gender disparity in AI development further exacerbates bias. Only 8–10% of software
developers are female, and this imbalance can encode biases into algorithms, often un-
intentionally [31,32]. Assumptions made by predominantly male developers can lead to
unfair outcomes, particularly in culturally sensitive applications where debiasing efforts
remain insufficient [20]. The European Union’s AI Act mandates debiasing, but loopholes
allow companies to circumvent regulations based on production location, perpetuating
inequalities and sustaining market dominance by former colonial powers [33].
Marketers themselves can unintentionally corrupt AI models through adversarial
attacks, altering input data, such as text or images, to mislead algorithms. These subtle
manipulations compromise machine-learning models for all users [ 34]. Consequently,
rigorous human oversight and ethical guidelines are essential to mitigate biases and ensure
the responsible use of AI in marketing.
2.2. Relevant Methods, Models, and Frameworks
To understand the rigour around ethical marketing usage of AI, relevant models
and frameworks were reviewed to identify current research gaps. Huang and Rust’s [35]
framework was one of the first research studies to investigate where AI can be used within
marketing. It structures strategic marketing planning across the broad AI landscape, cover-
ing marketing research, strategy (segmentation, targeting, and positioning), and operational
actions. This three-stage framework leverages AI to enhance strategic marketing, divided
into three types of AI: “mechanical AI” for automating repetitive marketing tasks, “thinking

Big Data Cogn. Comput. 2025, 9, 40 5 of 23
AI” for processing data to generate insights and support decision-making, and “feeling AI”
for analysing human emotions and social-economic interactions. However, this framework
is one dimensional, with general AI terminology mapped to the three areas and there is no
focus on application. Similarly, research from Buch and Thakkar [36] and Yu [37] scope the
possibilities of marketing use of AI, but do not define the use cases for it.
Nesterenko and Olefirenko [38] critique Huang and Rust’s [35] framework in that there
are no use cases in their research, which only focuses on the overall abilities of AI. However,
building on Huang and Rust’s [35] framework, Haleem et al. [14] built a comprehensive
table overview identifying 23 diverse ways marketeers can apply ChatGPT generative AI
in marketing activities. These include audience targeting, creating scripts for advertising,
and improving customer service. While both these models applied AI usage in marketing,
no investigation of bias propagation was undertaken by them.
The literature resources on how new technology, including AI, is successfully inte-
grated into companies were also reviewed. Any new deployment of technology within a
company requires organisational changes for its successful integration, usually referred to
as organisational complements [39]. Jarrahi et al. [40] argue the successful implementation
of AI for all operational requirements (not just marketing) lies in the infrastructure of its
adoption, not the technology itself. They propose three complements of people, infras-
tructure, and process to underpin successful integration of AI for all business applications.
This has some parallels with Huang and Rust’s [35] mechanical, thinking and feeling AI
framework. Other researchers [ 41] have examined the broader social and technological
responsibilities of companies using AI within the context of corporate digital responsibility.
More specifically, Buczek et al. [6] at Forrester Research suggest the “3Es” of AI in
marketing are (1) effectiveness, for improving business outcomes, (2) efficiency, for cost
savings and improved productivity, and (3) effort, for improving customer experiences.
A further output that corroborates this is Dwivedi et al.’s [ 42] research specifically on
generative AI bias. They proposed that three areas would help mitigate bias through AI
usage: (1) knowledge, transparency, and ethics; (2) digital transformation of organisations
and societies; and (3) teaching, learning, and scholarly research. Dwivedi et al.’s [ 42]
research, while focused on bias in generative AI, does not apply directly to marketing
use cases. While frameworks are available for using AI in marketing, no one provides a
framework for mitigating the propagation of bias by marketeers using AI.
Within the literature, the mitigation of bias in AI is often referenced in a cross-industry
context [43,44], but many of the available use cases apply to the healthcare industry [45].
The issues of diversity bias and gender bias are well documented within AI models that
are used for multiple industries [43–45]. A lack of diversity in both data, developers and
programmer bias is noted, aligning with the literature explored within the marketing
industry [43]. The focus is on instilling fairness within the data used from the beginning
and reducing bias within the algorithms themselves [44]. However, in common with the
literature available on AI in marketing, bias mitigation when prompting AI within other
industry functions and sectors is scarcely covered in the research literature. There are some
guidelines in the grey literature and online blogs, but these tend to be general in nature
and largely untested [46,47].
The marketing customer journey is a prominent focus in much of the relevant literature.
From 1960 onwards, the customer journey has often been viewed as comprising four
stages—need recognition; pre-purchase; purchase; and post-purchase—when marketing
began to focus on customer decision making when buying products [48]. It has been the
core of planning and executing a marketing campaign for decades. Due to the evolution
of digital marketing, there are now more marketing channels than a decade ago [49]. In
line with this, the customer journey lifecycle has now evolved into further stages, with

Big Data Cogn. Comput. 2025, 9, 40 6 of 23
companies using multiple-stage journey maps for their marketing efforts [50]. This research
uses the eight-stage marketing customer lifecycle map (Table 1). This eight-stage journey
shows content and marketing tactics mapped to granular decision-making stages, split
by pre-sale and post-sale and draws upon the evolved B2B marketing customer journey
proposed by Purmonen et al. [51].
Table 1. Business-to-business marketing customer lifecycle journey map.
Pre-Sale Stage
Sale
Post-Sale Stage
Stages Awareness Acquisition Consideration Select Adopt Usage Retain Expand
Content
Content with
messaging
for
awareness
Content with
messaging for
acquiring
Content with
messaging for
consideration
Content that
is used for
final
sale/selection
Content
with
messaging
on how to
adopt the
new
purchase
Content
with
messaging
on how to
use the
new
purchase
Content
that is used
for
customer
loyalty and
retention
Content to
expand
customers
into
purchasing
other
products
Channels
Channels that
grab
awareness:
Brand (TV ,
Billboards,
etc.)
Paid Media
Social Media
Organic
Search
Website
Pages
Events
Channels that
acquire:
Account-
based
marketing
Software
Reviews
Paid Media
Emails
Organic
Search
Website Pages
Events
Channels that
further
consideration:
Outbound
Tele-sales
Software
Reviews
Paid Media
Emails
Organic Search
Website Pages
Events
Channels that
encourage
selection:
Free Trials
Inbound
tele-sales
Marketplace
websites
Events
Partners
Channels
that
encourage
adoption:
Emails
Community
Websites
Learning
Modules
Channels
that
encourage
usage:
Emails
Community
Websites
Learning
Modules
Outbound
Tele-sales
Channels
that retain
customer:
Customer
Success
Events
Community
Websites
Channels
that
encourage
expansion:
Emails
Website
Outbound
Tele-sales
Source: Based upon Purmonen et al.’s [51] Customer Journey framework [51] and process mapping in the Case
Study Company (CSC).
Comparison of the “original” four-stage marketing customer journey [50] and Table 1
suggests a correlation between the two models: need recognition is equal to awareness;
pre-purchase is equal to acquisition and consideration; purchase is equal to select; and
post-purchase is equal to adopt, usage, retain and expand. The evolved customer journey
in Table 1 shows that there is content and channel differentiation when a customer is in the
two stages of acquisition and consideration that were not in the original customer journey.
The post-sale evolution also shows there is distinct differentiation to the stages a customer
goes through post-purchase. The customer journey is a pivotal go-to market for a company
and a vehicle for AI outputs to interact with customers.
The company studied in this research, given the alias “CSC”, sells B2B (business
to business), and a B2B buyer has a longer decision-making process with an average of
27 interactions with the company [52]. A B2B buyer’s preferred engagement is 67% digital
and 33% human-to-human interaction. These buyers are seeking interactive, immersive
and omnichannel engagement. Buczek et al. [6] state that by 2028, G200 firms (the largest
global companies) will utilise data and AI to automate 38% of actions in the buyer journey.
The Martech Stack also uses the evolved customer journey to optimise new technology
integrations and enhance audience interaction [11,53].
2.3. Provisional Conceptual Framework
The provisional conceptual framework (PCF) is drawn from the literature analysis and
represents an initial view of the key concepts that will underpin the development of the
analytical framework for revealing and mitigating bias, supporting the ethical usage of AI
in digital marketing. Jabareen [54] argues that a PCF is best placed to support theoretical
research in complex social phenomena, as “usually, these multidisciplinary phenomena

Big Data Cogn. Comput. 2025, 9, 40 7 of 23
do not even have a skeletal framework” (p. 50). While there are research frameworks that
map AI use in marketing [13,35], bias within the marketing customer journey [55] and bias
within AI [42], these are related to specific functions, activities or technologies with no
one framework bringing them together. Here, the PCF aims to achieve this as a basis for
subsequent development and validation within the primary research phase.
The PCF (Figure 2) sets out the relationships between the core concepts and related
elements that emerged from the literature review. For AI, two types are identified: gen-
erative AI and traditional AI [2]. The customer journey emerges as a central theme, and
here the eight-stage conceptualisation discussed above is included: awareness, acquisition,
consideration, selection, adoption, use, retention and expansion [6]. The core concept of the
Martech Stack has seven technologies: search engine optimisation, social media, website,
multi-channel nurture, DAM, CRM and analytics [ 11]. The routes to market within the
Martech Stack are SEO, social media, website and multi-channel nurture. DAM, CRM and
analytics are internal software used to measure ROI and structure content and customer
data. The PCF structure clearly details the cascade of bias within the types of AI and the
Martech Stack. This research, therefore, has 17 elements within its core concepts, giving
112 interactions to explore between them–2 AI types x 7 Martech Stack technologies x 8
Customer Journey stages.
Big Data Cogn. Comput. 2025, 9, x FOR PEER REVIEW 7 of 24

2.3. Provisional Conceptual Framework
The provisional conceptual framework (PCF ) is drawn from the literature analysis
and represents an initial view of the key co ncepts that will underpin the development of
the analytical framework for revealing and mitigating bias, supporting the ethical usage
of AI in digital marketing. Jabareen [54] argues that a PCF is best placed to support theo-
retical research in complex social phenomena, as “usually, these multidisciplinary phe-
nomena do not even have a skeletal framewor k” (p. 50). While there are research frame-
works that map AI use in marketing [13,35], bias within the marketing customer journey
[55] and bias within AI [42], these are related to speci ﬁc functions, activities or technolo-
gies with no one framework bringing them to gether. Here, the PCF aims to achieve this
as a basis for subsequent development and validation within the primary research phase.
The PCF (Figure 2) sets out the relationsh ips between the core concepts and related
elements that emerged from the literature review. For AI, two types are identiﬁed: gener-
ative AI and traditional AI [2]. The customer journey emerges as a central theme, and here
the eight-stage conceptualisat ion discussed above is included: awareness, acquisition,
consideration, selection, adoption, use, rete ntion and expansion [6]. The core concept of
the Martech Stack has seven technologies: search engine optimisation, social media, web-
site, multi-channel nurture, DAM, CRM and analytics [11]. The routes to market within
the Martech Stack are SEO, social media, website and multi-channel nurture. DAM, CRM
and analytics are internal software used to  measure ROI and structure content and cus-
tomer data. The PCF structure clearly details the cascade of bias within the types of AI
and the Martech Stack. This research, therefore, has 17 elements within its core concepts,
giving 112 interactions to explore between them–2 AI types x 7 Martech Stack technologies
x 8 Customer Journey stages.

Figure 2. Provisional conceptual framework.
People, processes, and infrastructure were also identiﬁed within the literature review
as appropriate categories for a top-line classi ﬁcation of the management of AI within a
Figure 2. Provisional conceptual framework.
People, processes, and infrastructure were also identified within the literature review
as appropriate categories for a top-line classification of the management of AI within
a company [40]. In this context, the Martech Stack can be viewed as the infrastructure
element, the marketing customer journey is the process element, and the exploration
of people (marketeers) is part of the analysis of the primary research. It requires the
appropriate combination and interaction of people, process and infrastructure elements
within companies to reveal and mitigate bias perpetuation.

Big Data Cogn. Comput. 2025, 9, 40 8 of 23
3. Research Method
This section consists of two main sections. First, the main elements of the research
methodology are briefly outlined and discussed in Section 3.1. Then, in Section 3.2, the
data analysis and validation techniques are discussed.
3.1. The Case Study Approach, Data Collection and Research Philosophy
The research reported here adopts an interpretivist philosophy, focusing on the com-
plex interplay between human subjectivity, interpretive frameworks, and a contextual
understanding of the social world [ 56]. The research is qualitative rather than quantita-
tive. Flick et al. [ 57] have pointed out that qualitative research allows the researchers to
be much closer to the subject under study compared with numerical and standardised
quantitative inquiries, which is central to the method adopted here. A study of bias in an
organisation involves a complex and highly contextual process, for which a qualitative
research approach is well suited [58]. The research design was aligned with the overall
interpretivist philosophical standpoint, and an inductive approach to concept development
was adopted. Thomas [ 59] (p. 238) notes that the inductive approach “is a systematic
procedure for analysing qualitative data in which the analysis is likely to be guided by
specific evaluation objectives”. Saunders et al. [60] classify the purpose of a research project
as exploratory, descriptive, explanatory, or evaluative, but a combination of research pur-
poses over time is possible. Here, the research is largely exploratory in that it explores
perspectives on bias in AI as evidenced in digital marketing activities and systems, but it is
also descriptive in that it aims to establish a model that sets out relationships between the
different concepts involved.
The analysis of pertinent literature, discussed above, provides a foundation for the pri-
mary research and can be viewed as a component of the research method. The primary data
were collected through a mono-method qualitative case study of an international software
vendor (referred to anonymously as CSC). Mono-method research ensures methodological
consistency by employing one approach throughout the research [61]. The data collection
method is one-to-one semi-structured interviews with 6 marketing professionals from CSC.
To qualify, interviewees had to meet certain criteria—they had to either use AI within their
job or have been on a project team that had implemented AI within CSC marketing. A
profile overview of each respondent is given in Table 2. These respondents represent a fair
cross section with a range of experience years and career levels (manager and lead). AI
adoption trends vary among professionals, making it essential to capture perspectives from
different stages of AI adoption at different career levels.
Prior to these interviews, respondents were sent (1) a Participant Information Sheet
that included the PCF for them to become familiar with it, (2) a consent form, and (3) a
preliminary questionnaire of 40 questions. These were analysed to ensure the interviews
were customized and focused accordingly to provide the maximum opportunities for
appropriate data capture [61]. The core concepts of the PCF were used as focus areas within
the questionnaires and interviews. This approach ensured an in-depth understanding of
how marketing professionals at CSC engage with AI and contribute to the development of
a robust, actionable framework for ethical usage.
Although there were only six interviewees drawn from the marketing department of
one company, the authors felt that the depth, variety and relevance of experience of these
senior marketing professionals would provide valuable insights that would address the
RQs and help progress the PCF into an analytical framework. As pointed out by Islam
and Aldaihani [ 62], qualitative research does not normally include a large sample of a
population because the collected data are not quantifiable. Another perspective is provided
by Guest et al. [63] (p. 59), who found that, in the context of qualitative interview-based

Big Data Cogn. Comput. 2025, 9, 40 9 of 23
research, “saturation occurred within the first twelve interviews”, but that “basic elements
for metathemes were present as early as six interviews”. This was “purposive sampling”,
albeit on a limited scale and from just one company. The interviewees were selected
because of their “particular features or characteristics which will enable detailed exploration
and understanding of the central themes and puzzles which the researcher wishes to
study” [64] (p. 78). The use of semi-structured interviews provided the opportunity
for interviewees to provide their own perspectives on bias, possibly uncovering the less
obvious aspects, giving them a “voice” in the study [65]. In an emotive field such as bias,
which is dependent on personal perceptions and attitudes amongst the participants, there
are unavoidable interpretive ambiguities in their engagement with the topic. This often
results from perceived power [8], and emotional communities [66]. The authors believe that
an initial small-scale sample is justified as a way of exploring these multiple interpretations.
Table 2. Interviewee profiles.
Respondent
Code Job Profile Years of Experience Knowledge of AI
R01 Strategic Marketing Project Manager 3 Years
• Led project that implemented AI
into a marketing function.
• Uses AI in daily role for
administration.
R02 Marketing Program Lead 13 Years • Uses AI in daily role for administration.
R03 Content Marketing Lead 12 Years
• Contributor to projects that
implemented AI into a marketing
function.
• Uses AI in daily role for
administration.
R04
Integrated
Marketing Program
Management
10 Years
• Contributor to projects that use AI
for content production.
• Uses AI in daily role for
administration.
R05
Marketing
Localization
Strategy Lead
15 Years
• Led project that implemented AI
into a marketing function and
content production/translation.
R06 Marketing Content Operations 16 Years • Uses AI in daily role for administration.
3.2. Data Analysis and Validation
Interview data were thematically analysed from the transcripts. The analysis proce-
dure was based on Terry et al.’s [67] six-phase thematic analysis framework: 1. familiarisa-
tion, 2. coding, 3. developing themes, 4. reviewing themes, 5. defining and naming themes
and 6. producing the report. This was done using spreadsheets with a degree of manual
sifting and reorganization of emergent themes. Indeed, Webb [ 68] recommends using a
manual data analysis when conducting small qualitative studies, as this allows a degree of
intuition that is not found in software analysis. This view is supported by Mason [69], who
argues that manual review of data is preferable as it enables the researcher to explore the
data to capture nuances and understand the tone of interviewees. Following the thematic
analysis of data to define the core themes, a cross-tabulation was created that was then
compared with the cross-tabulation created for the PCF.
This comparison uncovered gaps and suggested new elements that could be incor-
porated within the PCF, thereby providing a renewed basis for the analytical framework.
Using cross-tabulation as a framework analysis tool offers a clear process for conducting

Big Data Cogn. Comput. 2025, 9, 40 10 of 23
qualitative research [70]. The cross-tabulation mapping of literature, researcher experience
and interview data to the frameworks gives transparent and trustworthy insights into the
validation of the final analytical framework [71].
4. Results
This section addresses the two research questions, drawing on the literature review
presented in Section 3, the primary interview material and researcher observations. The
interviewees have been assigned interviewee codes for their direct quotes.
4.1. RQ1. What Are the Current and Perceived Bias Issues in Coding, Prompting and Deployment
of AI in Digital Marketing?
The bias issues for AI coding are reasonably well documented in the existing litera-
ture [2–4,14,22,23]. However, bias issues within the prompting and deployment of AI are
less researched, and these are a focus area within the primary research in this study (Table 3).
From the questionnaire returns, five out of six respondents agreed that marketeers bring
their own biases into marketing campaigns. This was explored further in the interviews
and generative AI was perceived to be riskier for bias propagation over traditional AI.
R01 stated: “I talk to ChatGPT on a daily basis, now it understands my preference and
current work. . .sometimes it works faster than my own brain”. R03 agreed and noted that
“every time you prompt (open AI) and the memory is updated you’re training the model
on something”. Traditional AI was perceived as less at risk for bias prompting as there are
review processes within IT at CSC for any traditional AI projects. There was an assumption
by respondents that IT will have followed due diligence in selecting the appropriate peo-
ple and process. R05 noted that when marketeers use traditional AI, “industry standard
tools take on the due diligence”. The only concern that emerged for traditional AI was
hyper-personalisation in the Martech Stack. R03 noted that “hyper-personalisation based
on anonymised customer IDs and behaviour patterns. . .we’re definitely missing a good
monitoring system”.
In exploring types of bias with respondents, cultural bias was especially noted and
the Eurocentricity of marketing was explored, which was also considered in the literature
review [21,33]. When localising centrally created content, R04 noted, “there’s so much,
not just languages, but you have to think about dialects. You have to think about the
culture”. Essentially, literarily translated content may not land well in a local language, and
reviewers should understand that culture, as well as being able to speak the language, to
ensure correct wording, known as transcreation. R02 noted the bias within buyer personas
as Eurocentric: “for research profiles, we survey 600ish people. But it still usually skews
heavily into one market, making up a lot of the responses for the survey. . .that adds a bias
into findings, even though we’re using the data as opposed to just opinion”. An example of
bias was given where social media banners were produced using generative AI to produce
the images. In a team review, it was noted that the imagery was not culturally diverse
or gender diverse—this was a manual review and edited before the content was used
externally—but a clear use case for the ease with which bias can propagate.
The literature gives insight into the lack of effective failsafes and laws regarding
AI [4,27], and all respondents noted that, to their knowledge, no failsafes are in place in
CSC for generative AI output. All participants stated that further training and education on
how to use AI were required and that current training was hard to apply to their day-to-day
jobs. R03 notes that “we’re trusting people to use their own critical thinking which isn’t
enough”. R02 stated that they are using their own “moral compass” to use AI ethically and
check their own bias when using it.

Big Data Cogn. Comput. 2025, 9, 40 11 of 23
Table 3. Bias issues for coding, prompting and deployment of AI in digital marketing.
Coding Prompting Deployment
C1. Machine learning heuristics—quick,
approximate solutions—drive AI speed
and scalability, but often at the expense of
accuracy and fairness [28]. Transparency
and accountability are limited due to the
proprietary nature of these algorithms,
raising ethical concerns [29].
C2. Only 8–10% of software developers
are female, and this imbalance can
encode biases into algorithms, often
unintentionally [31,32].
C3. Assumptions made by
predominantly male developers can lead
to unfair outcomes, particularly in
culturally sensitive applications where
debiasing efforts remain insufficient [20].
The European Union’s AI Act mandates
debiasing, but loopholes allow
companies to circumvent regulations
based on production location,
perpetuating inequalities and sustaining
market dominance by former colonial
powers [33].
C4. There are no global regulatory rules
for AI; different countries, continents and
political and economic unions are
employing different approaches [4,27].
P1. Generative AI learning from the users’
preferences. This can include any bias
from the prompter who does not
understand a culture but is generating
content for their market; or any bias from
the prompter who assumes their target
audience characteristics—gender, age,
location etc. [R01, R02, R04].
P2. Marketers themselves can
unintentionally corrupt AI models
through adversarial attacks, altering
input data, such as text or images, to
mislead algorithms. These subtle
manipulations compromise
machine-learning models for all users
[34].
P3. Lack of understanding and
knowledge for correctly prompting an AI.
“The art of prompting” is not something
currently taught and so marketeers are
having to use their own knowledge or
research to learn how to prompt. To be
aware of bias propagation they must
currently use their own “moral compass”
[R01, R02, R04, R05].
D1. No identified failsafe in generative
AI usage to flag biased prompts or inputs
[R01, R02 R03, R04, R05, R06].
D2. Further training is required that is
focused specifically on marketing use
cases and projects. This includes
prompting guidance or training and
should be a continuous learning
experience [R01, R02 R03, R04, R05, R06].
D3. Inconsistency of laws regarding AI
and its usage allows Eurocentric
marketing practices to occur. Those who
are not culturally or language fluent work
on localized projects [R04, R05].
Eurocentric marketing practices are
prevalent within large companies—where
decisions are made on behalf of other
markets by people who may not be aware
of cultural norms and differences [21,33].
D4. Further Eurocentric focus can result
from incomplete data integrity for
research profiles. Persona research may
just be done on one or two markets,
adding bias into findings [R02].
D5. Usage of historical data for current
data-driven decision making—such data
for software buyers can be skewed by
gender, age, demographics etc., and then
used for current marketing where
purchaser profiles are evolving to new
demographics [R01, R03].
Source: Extant literature and primary interviews (coded R01–R06).
The current literature suggests there is little difference between the pre- and post-sale
customer journey as regards the use of AI—content is produced in the same manner and
the channels to market are the same. However, interview feedback suggests an alternative
perspective. The AI capabilities using customer data are different before purchase and
after purchase. R03 noted that marketing has changed significantly in recent years and
all respondents agreed that the eight-stage customer journey (Table 1) was appropriate
for assessing AI and bias. R04 noted the customer journey was “crucial” to modern
marketing, stating: “traditionally, we’ve always used a single customer journey for a single
customer—that does not really work anymore. . . it has to be a slight customisation for each
customer journey”. R01 provided a more analytical observation, noting: “concern [is] for
the pre-sale, in terms of the output because if we use the AI for content generation. . .the AI
can only train itself based on the historical data”. The issue here is that personal historical
data could be inaccurate. R01 added that “if we let the AI create pre-sales content, it might
generate the content that’s more skewed towards men”. In this context, R03 observed: “the
white man in business is everywhere”. However, that view was not taken for post-sale
AI usage. R01, for example, asserted that “for the post sales, it’s not as skewed as the pre-
sales”. This is because AI is using more immediate real-life data from customers who have
just purchased—you have their age, gender, country they work in, and job title—giving
more control to outputs of AI and fewer instances for historical data assumptions or bias
to perpetuate.

Big Data Cogn. Comput. 2025, 9, 40 12 of 23
Respondents suggested that using AI for post-sale marketing could be easier than
within the pre-sale marketing stages, where there could be scalability challenges. R02
emphasised that the volume of content and advertising in pre-sale marketing activities
can be problematic, whereas “post purchase is where it [the customers journey] scatters
into very different directions, so there would be much less overlap [than pre-sale]”. R02
added that “AI would be really helpful in terms of creating efficiency and scale for what
that would look like after the purchase”. Similarly, R04 noted that “especially at post sales,
we don’t really have to spend more money or energy on creating awareness”, but also
observed that “if we use AI, we have so much more input to give to create perfect prompts
to create the perfect customer journey”.
4.2. RQ2. What Framework Can Be Developed to Provide Guidance for Practitioners, for Revealing
and Mitigating Bias in AI Deployment in Digital Marketing?
4.2.1. PCF Review
During the interviews, respondents were asked to review the PCF (Figure 2). The
pre-interview questionnaire structure and interview script was entirely consistent with
the PCF focus areas: AI, Customer Journey, MarTech Stack, People, Process, Infrastructure
and Bias. All respondents agreed that the customer journey was of particular value and
relevance within the framework—it was understandable to them and its placement within
the PCF was acceptable. People and process were also viewed as pertinent umbrella
concepts. R02 noted, for example, that “People” would align better to “Content Generation”
and “Process” aligned better to “Algorithmic Rules” in the PCF with people generating the
content, and tradition rule-based AI being aligned with an established process. R06 noted
that “[it’s required to have the] right processes and reviews and governance in place”. All
respondents agreed that multiple human reviews of AI output in marketing should take
place and that there should be a set process.
It was confirmed by all interviewees that the Martech Stack (Infrastructure) is of great
relevance when using AI in digital marketing—it is the conduit through which the AI is
used—and must be part of the final framework. R05 noted the Martech Stack “ensures
quality of marketing output”. However, there were some conflicting perceptions on how
the PCF structured it as a hierarchy. R04 observed that, “[when you] put it in a pyramid,
people immediately think of level of importance . . .this is a hierarchy”. R02 agreed and
stated: “a pyramid structure implies a foundation or a level of importance, or a volume
implication”. However, none of the other respondents viewed it as hierarchical. R02 also
noted their view of the bias cascade as follows: “[when you] start at the analytics and then
because there’s something that’s set up with a bias there, it cascades into the next level,
which would be then like the SEO and then further to the social media and then on to
the web itself”. The Martech Stack is a core component of the framework, but interview
feedback suggests the presentation of these technologies in a pyramid and the AI cascade
warrant review. The Martech Stack is not a hierarchy; multiple technologies within it
interact with each other, and any bias within it can be imputed at multiple stages. R04
stressed the importance of an “organised Martech Stack”, whereby companies using this
PCF should make sure their Martech Stack technologies interact with each other correctly,
and pass information coherently to each other to maintain data integrity.
Project management surfaced as a theme in several of the interviews and there were
differing respondent viewpoints on this. R01 was in favour of adding Project Management
within the Martech Stack, whereas R02, R03 and R04 saw Project Management sitting
under the Process umbrella within the PCF. As regards social media, R02 suggested “social
media” be renamed “organic and integrated social media”), to delineate a paid and non-
paid approach to social media, which was accepted for the research. Also, as regards the
Martech Stack in the PCF, Analytics was seen by R03 and R04 as too broad a term—the

Big Data Cogn. Comput. 2025, 9, 40 13 of 23
data just exist within CRM and then specific analytical activities are performed on that data.
R03 suggested labelling it as “algorithmic analytics and data modelling”. These proposals
were incorporated into the amended framework.
The interview feedback, along with relevant references from the literature, were then
mapped to the PCF core concepts (2 AI types x 7 Martech Stack technologies x 8 Customer
Journey stages, as outlined in Section 2.3). This was a form of framework analysis [54], in
which the two main types of AI were mapped against, first, the customer journey stages,
and then against the Martech technologies. These interactions are depicted in tabular
format in Appendix A as Tables A1 and A2. In addition, the cell data was classified as
people, process and/or infrastructure (PPI) themes via colour coding to provide a top-line
picture of their relative significance. The definition of people, process and infrastructure
follow Jarrahi et al.’s [ 38] classifications. For “people”, a human will have to be part of
the interaction (such as training, complex understanding or prompting); for “process” it
is workflows and cross-team collaboration; and “infrastructure” indicates the tools and
software used for data and interpretation. Within the tables, sections are merged where
there is no differentiation of the core concepts.
4.2.2. Towards an Analytical Framework for Revealing and Mitigating Bias
Based on the interviewee feedback discussed above, and the cross-tabulation of in-
terview data and literature perspectives (see Tables A1 and A2 in Appendix A), a new
framework for revealing and mitigating bias in AI deployment in marketing was developed
(Figure 3).
Big Data Cogn. Comput. 2025, 9, x FOR PEER REVIEW 14 of 24

Figure 3. A new framework for revealing and mitigating bias in marketing.
This framework is a progression from the PCF, incorporating the interview feedback.
It distinguishes between traditional and generative AI, and pinpoints the main marketing
activities in which AI may be deployed (within the blue arrows to the left and right of the
framework). These main marketing activities are directly linked to people and processes
that inﬂuence them. Bias is centred within the framework, and it accommodates the dif-
ferentiation between coding, prompting and deployment of AI, and the di ﬀerent nature
of issues relating to each activity (Table 3). The framework has the Martech technologies
underpinning the eight stages of the customer  journey at its core—this suggests that im-
pacts will vary signi ﬁcantly from stage to stage. It also emphasises the in ﬂuence of AI
across the Martech technologies, and acknowledges the two key management issues
emerging from the interviews—the value of  prompting education and the need for pro-
active management, which were highlighted as being of particular signiﬁcance for the de-
velopment and deployment of AI in today’s marketing technology environment.
The framework can act as a checklist and guide for the development of procedures
for identifying where bias may occur. A number of steps can be identi ﬁed. First, review
the marketing activities listed in the two blue arrow areas in the framework and highlight
those that are of particular importance in the organisation. Second, identify the stage or
stages of the customer journey where each of these identi ﬁed activities has the most im-
pact. Third, scrutinise the activity/process stage interaction and assess: (a) is AI involved
in supporting this activity and (b), if yes, explore its operation for possible evidence of
bias. This “seat of the pants” approach can be used even by small companies to develop
and then formalise and document procedures for revealing and mitigating bias. This con-
stitutes a pragmatic bo ttom-up approach to addressing an evolving concern, which is
likely to be increasingly encompassed in wider top-down governance-related legislation
in future years.
Figure 3. A new framework for revealing and mitigating bias in marketing.

Big Data Cogn. Comput. 2025, 9, 40 14 of 23
This framework is a progression from the PCF, incorporating the interview feedback.
It distinguishes between traditional and generative AI, and pinpoints the main marketing
activities in which AI may be deployed (within the blue arrows to the left and right of the
framework). These main marketing activities are directly linked to people and processes
that influence them. Bias is centred within the framework, and it accommodates the differ-
entiation between coding, prompting and deployment of AI, and the different nature of
issues relating to each activity (Table 3). The framework has the Martech technologies un-
derpinning the eight stages of the customer journey at its core—this suggests that impacts
will vary significantly from stage to stage. It also emphasises the influence of AI across
the Martech technologies, and acknowledges the two key management issues emerging
from the interviews—the value of prompting education and the need for proactive man-
agement, which were highlighted as being of particular significance for the development
and deployment of AI in today’s marketing technology environment.
The framework can act as a checklist and guide for the development of procedures for
identifying where bias may occur. A number of steps can be identified. First, review the
marketing activities listed in the two blue arrow areas in the framework and highlight those
that are of particular importance in the organisation. Second, identify the stage or stages of
the customer journey where each of these identified activities has the most impact. Third,
scrutinise the activity/process stage interaction and assess: (a) is AI involved in supporting
this activity and (b), if yes, explore its operation for possible evidence of bias. This “seat of
the pants” approach can be used even by small companies to develop and then formalise
and document procedures for revealing and mitigating bias. This constitutes a pragmatic
bottom-up approach to addressing an evolving concern, which is likely to be increasingly
encompassed in wider top-down governance-related legislation in future years.
5. Discussion
The above results and the interview feedback raised a number of other issues worthy
of further discussion. Firstly, all respondents noted the vital importance of correct prompt-
ing of generative AI. R06 called it “the art of prompting”. Individually, all respondents
discussed the value of learning how to prompt an AI. R04 noted that “one of the main
challenges is that we all use AI differently, so I could use a prompt in a different way [to
others]. . .because we all have different experiences, languages and so on”. The differing
cultural experiences of marketeers could lead to Eurocentric aesthetic biases in prompts
that exclude diverse cultural representations [21,22,33]. This is problematic because it can
alienate and marginalise non-European cultures, communities, and customers when they
are exposed to biased AI-generated content.
R04 pointed out that “in the end the outputs also change” but that for his/her company
“in terms of branding, in terms of messaging, we want to it to be more consistent. The risk
is that . . .. . .the AI output won’t be the same”. R06 agreed, stating: “I don’t think there
is a whole standard yet, everybody’s using it . . .but how do I even prompt AI to get out
what I need”. R02 noted that “[currently employees are] learning through errors of how to
appropriately craft a prompt”.
R02 noted their current unease with the lack of prompting education and training:
“I would feel a lot more confident about what I could and couldn’t put into a prompt
[with training]. R02 also observed that these concerns “holds them back from using AI
for anything other than administrative tasks”. R06 agreed, saying it was not a question of
“one-off training”, but rather “it’s really the art of how I do that [prompt]”, adding that “I
personally don’t feel comfortable yet”. Of note, all respondents strongly agreed that the
current training to use AI at CSC was inadequate, and all agreed that training is needed to
use AI responsibly. R05 stated that while marketeers are encouraged to use generative AI,

Big Data Cogn. Comput. 2025, 9, 40 15 of 23
“we get guidelines but no risk management”. This illustrates and emphasises the risk of
not having global regulatory rules for AI [4,27].
An educational program on how to prompt an AI for digital marketing uses was a
key issue for all respondents. R03 recommended that a training model could be used by
employees to test their prompting skills in a training scenario based on their job role and
interests. They noted that companies should define the bias parameters themselves and a
list of acceptable promptings for marketing use cases should be provided. R02 noted that
publishing prompting “guidelines on how to do so” would be beneficial. There was also
unease, as noted above, on the AI learning from marketeers and the risk of unintentionally
corrupted AI models through adversarial attacks [34]. This could be problematic in several
ways, as it might perpetuate biases, limit innovation, or result in ineffective campaigns.
R04 and R06 noted that companies should be limiting AI’s learning from employees
(especially in large companies that want to maintain the same brand integrity) and offer
generic prompts for marketeers to use—similar to Microsoft Co-Pilot that offers standard
prompts to all users. R05 explored the idea of “using an AI guidebook” where roles and
responsibilities were clearly defined and AI ambassadors from the general workforce are
on hand to offer guidance to peers. This will require initiatives across the people, process
and infrastructure field if it is to be successfully implemented.
Secondly, it was noted by R02 that companies usually are “reactive to new
technology”—rather than embracing a proactive approach to technology usage and im-
plementation. In this context, R03 drew a parallel with the evolution of the Internet: “if
you go back to the early days of the Internet—people didn’t really use the Internet very
much because the operating system was really, really terrible. It wasn’t until they fixed
the operating system that the adoption of it became really interesting”. The respondents’
viewpoints were consistent in that rather than allowing users to explore AI and allowing
something “bad” to happen, companies should provide proactive guidance, education
and adoption assistance in advance. R02 noted that more control around new technology
provides comfort for cautious users, and therefore, proactive management is in employees’
best interests to encourage more usage.
R01 suggested that those resistant to using AI and incorporating it into their work
are “legacy thinkers and laggard adopters” and noted “incremental adoption [of new
technology] requires support”. All respondents rated themselves as data-driven marketeers,
and all use AI in their jobs, marking themselves as “early adopters” within CSC (R01). The
average score of where they saw AI usage to be at CSC by their peers was 2 out of 5 (one
being not used and five being used prolifically). R04 noted that while this score is low, CSC
is, nevertheless, ahead of the current industry standard and rate of adoption.
Thirdly, some of the current literature [5,6] maintains that increased ROI and employee
output are to be expected from increased AI deployment. This was generally supported by
interview feedback. When asked to rank the perceived value of using AI against 10 criteria,
“work on higher value activities” and “increased output” were ranked first and second
overall (Table 4). This points to the value of supporting the workforce when the potential of
new technology in increasing productivity is understood, and staff are engaged in applying
new technology to enhance their own performance and output.
Indeed, empowering employees to use new technology fosters a culture of innovation
and efficiency, this being rather similar to when software developers are encouraged to
create AI at speed [28]. The encouraged speed comes at a cost, with the time to market
winning over the time to create fair and diversified datasets. This pressure for innovation
could be felt by marketeers using AI wantonly, before truly learning its limitations and
how to use it. When employees identify tools that enhance their productivity, it is often
based on a first-hand understanding of their tasks and pain points. Supporting such

Big Data Cogn. Comput. 2025, 9, 40 16 of 23
initiatives demonstrates trust, boosts morale, and encourages ownership of work outcomes.
It positions the company as adaptable, leveraging modern tools to maintain a competitive
edge. Ignoring these requests risks disengagement and inefficiencies, while embracing
them can drive better collaboration, streamlined workflows, and higher job satisfaction.
Ultimately, actively supporting employees in their use of new technologies creates a win-
win for workforce motivation and organisational performance. This underscores the value
of a proactive approach to supporting users through an adoption transition, in which the
analytical framework discussed above may act as a useful action checklist.
Table 4. Results from respondents’ pre-interview question on their perceived value of using AI in
Digital Marketing.
Respondent
Please Now Rank the Value of Using AI in Digital Marketing
1 = Highest Ranked, 10 = Lowest Ranked
1st 2nd 3rd 4th 5th 6th 7th 8th 9th 10th
R01
Increased
Conver-
sion Rates
Increased
Output
Work on
Higher
Value
Activities
Improved
Supplier
Perfor-
mance
Increased
Visibility of
Data
Higher
Quality
Output
Reduced
Workload
Reduced
Risk
Improved
Brand
Adherence
Increased
Control
R02
Work on
Higher
Value
Activities
Improved
Supplier
Perfor-
mance
Reduced
Workload
Increased
Output
Increased
Conver-
sion Rates
Higher
Quality
Output
Reduced
Risk
Increased
Control
Increased
Visibility of
Data
Improved
Brand
Adherence
R03 Increased Output
Work on
Higher
Value
Activities
Improved
Supplier
Perfor-
mance
Reduced
Workload
Higher
Quality
Output
Increased
Conver-
sion Rates
Increased
Visibility of
Data
Reduced
Risk
Increased
Control
Improved
Brand
Adherence
R04 Reduced Workload Increased Output Improved Brand Adherence Work on Higher Value Activities Improved Supplier Perfor- mance Increased Control Higher Quality Output Increased Visibility of Data Increased Conver- sion Rates Reduced Risk
R05 Increased Output Increased Conver- sion Rates Work on Higher Value Activities Reduced Workload Increased Visibility of Data Higher Quality Output Improved Supplier Perfor- mance Increased Control Reduced Risk Improved Brand Adherence
R06
Work on
Higher
Value
Activities
Increased
Visibility of
Data
Reduced
Workload
Increased
Conver-
sion Rates
Improved
Brand
Adherence
Increased
Control
Higher
Quality
Output
Increased
Output
Reduced
Risk
Improved
Supplier
Perfor-
mance
Overall ranking: 1 = Work on Higher Value Activities; 2 = Increased Output; 3 = Reduced Workload; 4 = Increased
Conversion Rates; 5 = Improved Supplier Performance; 6 = Increased Visibility of Data; 7 = Higher Quality Output;
8 = Improved Brand Adherence/Increased Control; 10 = Reduced Risk.
6. Conclusions
This article has explored the current and perceived bias issues in coding, prompting
and deployment of AI in digital marketing through a review of the current literature and
primary data from interviews with industry marketeers. It put forward a provisional
conceptual framework from which an outline analytical framework was developed to
provide guidance for practitioners for revealing and mitigating bias in AI deployment
in digital marketing. The core concepts are taken from leading marketing theories on
successful technology adoption [38] and the modern digital marketing landscape (Martech
Stack [11] and Customer Journey Map—Table 1).
The research clearly has its limitations. It is based on an analysis of secondary sources
and just six in-depth interviews in one major software vendor, which clearly limits the
scope for generalisation from these findings, as noted by Gray [72] and Yin [73]. However,
Flyvbjerg [74] (p. 223) has suggested that cases should focus on the generation of a deep
understanding of the complexity of the case, producing “concrete, context-dependent
knowledge”. The authors thus believe the PCF and analytical framework will be of interest
to researchers and businesses involved in the deployment of AI in marketing, and that this
research is best viewed as exploratory in a new and largely uncharted research field.

Big Data Cogn. Comput. 2025, 9, 40 17 of 23
The methodological approach of a pre-interview questionnaire with a follow-up
interview maximised the value of the data attained. All respondents used AI in their job
roles and claimed to be data-driven in their general approach. They covered four separate
marketing departments, five countries and five languages to get diverse data. The analytical
framework provides a baseline for future research in this field that could be tested and
adapted in other business environments. The current framework is designed for large and
medium-sized companies that want their marketing departments to use AI for marketing
activities. The framework could also be customised for use in small company projects, in
which redundant elements could be omitted or modified. It could also be evaluated and
developed through wider quantitative studies involving a survey of marketeers across
a range of companies. Such quantitative studies could, for example, be based on testing
hypotheses related to the core concepts of the operational framework, but also regarding the
relationships and causes of bias in coding, prompting and deployment. Such studies could
enhance the framework presented here and will be of most use to marketing leadership
and decision makers who plan and implement AI technologies and associated processes in
their organisations.
Future research will be conducted with other interviewees to validate and develop
this framework further, and other research teams could usefully extend this to different
business settings, in more countries and more languages, to broaden the applicability of
the framework. This would support subsequent generalisation, which, at this stage, must
be treated with caution. In addition, it will be essential to regularly review and update
the framework with the latest AI advances and digital marketing technologies. AI is a
nascent area, and those using it are early adopters. This framework will evolve as users
become more comfortable using AI in their jobs and as more AI models are created and
implemented for marketeers to use.
Author Contributions: Conceptualization, C.R., M.W. and R.B.; methodology , C.R., M.W. and R.B.;
software, C.R.; formal analysis, C.R. and M.W.; investigation, C.R.; data curation, C.R.;writing—original
draft preparation, C.R. and M.W.; writing—review and editing, C.R., M.W. and R.B.; visualization,
C.R., M.W. and R.B.; supervision, M.W. and R.B.; project administration, C.R., M.W. and R.B. All
authors have read and agreed to the published version of the manuscript.
Funding: This research received no external funding.
Institutional Review Board Statement: This study qualified for institution IRB waiver. Ethical issues
were reviewed in accordance with institutional rules, and it was determined that a mandatory referral
to an ethics committee was not necessary at the time of this research.
Informed Consent Statement: Informed consent was obtained from all subjects involved in the study.
Data Availability Statement: The data presented in the article are derived from confidential interview
transcripts and observation notes. Further inquiries can be directed to the corresponding author.
Conflicts of Interest: The authors declare no conflicts of interest.

Big Data Cogn. Comput. 2025, 9, 40 18 of 23
Appendix A
Table A1. Type of AI & customer journey interactions.
Awareness Acquisition Consideration Select Adopt Usage Retain Expand
Gen
AI
Content produced for
advertising: images,
videos, text and audio
[14,18,38]

R04 “internal CSC AI”.
R05 “Gen-AI CSC internal
tool”

R05 “Translation of copy
through AI, usage of AI
service to generate
voice-over in language for
video localization”

Content produced for
acquisition stage:
whitepapers, eBooks, etc.
[14,18,38]

Online events (i.e.,
webinars)—full content
production, tailoring
content [6]

R04 “internal CSC AI”.
R05 “Gen-AI CSC internal
tool”

Content produced for
consideration stage:
whitepapers, eBooks, etc.

AI Chatbots—text, audio
[14]

R04 “internal CSC AI”.
R05 “Gen-AI CSC internal
tool”

R05 “Translation of copy
through AI, usage of AI
service to generate
voice-over in language for
video localization”

Content produced for Select
stage: Guided experiences
and free trials [14,18,38]

Inbound qualification
services:
contact us and chatbots
[75,76]

Marketplace to buy
software [77]

R04 “internal CSC AI”.
R05 “Gen-AI CSC internal
tool”

Personalised generated content at scale. Content produced for
usage, retain and expand stage: emails, how-to guides,
webinars, etc. [14,18,38]

A/B testing on email and content wording and structure [15]

R04 “internal CSC AI”.
R05 “Gen-AI CSC internal tool”

R05 “Translation of copy through AI, usage of AI service to
generate voice-over in language for video localization”

Trd
AI
Using Target Account
Lists to target certain
companies and personas
[11,78,79]

R02 “Persona rules”.

R03
“hyper-personalization
tools, advanced A/B
testing methodologies,
customer journey
analysis”.

R01 “CSC leverages AI
and machine learning to
deliver personalized
customer experiences”
Using Target Account
Lists to target certain
companies [11,78,79]

Webinars—segmenting
event audiences,
geofencing [6]

AI Chatbots—routing
rules/suppression rules
[76]

Using Target Account Lists
to target certain companies
[11,78,79]

R05 “use industry-standard
tools” (embedded AI)

Contact us and inbound
qualification services [75]

R05 “use industry-standard
tools” (embedded AI)

R01 “CSC leverages AI and machine learning to deliver
personalized customer experiences”
Using Target Account Lists to target upselling and cross-selling
software to specific companies and personas
[11,78,79]

Nurture emails and webcast routing rules [2,80]

R02 “using Marketo for marketing nurture automation”.

R05 “use industry-standard tools” (embedded AI)

R03 “hyper-personalization tools, advanced A/B testing
methodologies, customer journey analysis”.

(indicating where the literature and primary data suggest AI is relevant to the customer journey).

Big Data Cogn. Comput. 2025, 9, 40 19 of 23
Table A2. Type of AI and Martech Stack interactions.
Search Engine
Optimisation Social Media Website Multi-Channel Nurture Tools Digital Asset Management (DAM) Customer Relationship Management (CRM) Analytics
Gen
AI
R03 “content
optimization for
SEO”

Content generation
with SEO keywords
(optimised organic
ranking) [14,18,38]

R04 “internal CSC
AI”.
R05 “Gen-AI CSC
internal tool”

R02 “Generative AI
creates a breadth of
banners to be used in
social channels”
R04 “Creating social
posts for customer
references for some
events”.

R03 “Social for
awareness and content
distribution”

Paid social personalised
generated content
[14,18,38]

Social media content
generated from social
listening [81]

R04 “internal CSC AI”.
R05 “Gen-AI CSC
internal tool”

R03 “website
management for lead
generation”

Personalised generated
content [14,18,38]

Software
reviews—automate
and analyse customer
feedback [82]

R05 “investment to use
Adobe Experience
Manager (embedded
AI)”

R04 “internal CSC AI”.
R05 “Gen-AI CSC
internal tool”

R03 “channel nurture
tools for email nurture
and omni channel
strategy”

Personalised generated
content [14,18,38]

A/B testing on email
and content wording
and structure [15]

R04 “internal CSC AI”.
R05 “Gen-AI CSC
internal tool”

Personalised generated
content [14,18,38]

R02 “Generative AI
supports the content
localization process.”
Localisation of content
[14]

Generating descriptions
for accessible content
[22]

R05 “investment to use
Opal (embedded AI)”

R03 “DAM for content
management”
R05 “Translation of copy
through AI, usage of AI
service to generate
voice-over in language
for video localization”

Generate predictive
analytics—customer
behaviour [83,84]

R03 “CRM for lead
management”

Generate forecasts
[85–87]

R03 “Analytics for
reporting”

Big Data Cogn. Comput. 2025, 9, 40 20 of 23
Table A2. Cont.
Search Engine
Optimisation Social Media Website Multi-Channel Nurture Tools Digital Asset Management (DAM) Customer Relationship Management (CRM) Analytics
Trd
AI
Targeting rules.
A/B testing on
keywords.
Metadata matching
rules.
[75]

R01 “CSC leverages
AI and machine
learning to deliver
personalized
customer
experiences”
Social listening targeting
rules [81].

R05 “use
industry-standard tools”
(embedded AI—Sprinklr
social media software)

Personalisation rules
and A/B testing on
website.
[11,78]

R02 “Persona rules”.

R03
“hyper-personalization
tools, advanced A/B
testing methodologies,
customer journey
analysis”

R01 “CSC leverages AI
and machine learning
to deliver personalized
customer experiences”

R02 “using Marketo for
marketing nurture
automation”.

Nurture & promotional
emails—data profiling,
segmentation, rules,
scoring. (i.e., by
product based on
interaction) [2,80]

R03 “channel nurture
tools for email nurture
and omni channel
strategy”

Automating tagging and
categorising content [14]

R06 “using AI as part of
content audits to identify
content gaps”.

R01 “our marketing
department leverages AI
to translate content and
deliver content to the
right personas”

R05 “internal CSC
Machine translation”
R01 “our marketing
department leverages
AI to identify target
accounts”

Contact suppression
rules.
Data modelling
algorithms.
Contact routing rules.
Contact scoring rules.
[2,80]

R05 “internal CSC
Machine translation”
R03 “CRM for lead
management”

R01 “CSC leverages AI
and machine learning to
optimize campaign
performance”

R02 “Persona rules”.

R03
“hyper-personalization
tools, advanced A/B
testing methodologies,
customer journey
analysis”.

Analysis of customer
data [78]
Dependent on data
maturity—large database
required [86]

First-party & third-party
data targeting [87]

R01 “our marketing
department leverages AI
to identify target
accounts and optimize
campaign programs
effectively”

R05 “internal CSC
Machine translation”
(indicating where the literature and primary data suggest AI is relevant to the Martech Stack). Colour Key: Purple = People, Blue = Process, Orange = Infrastructure.

Big Data Cogn. Comput. 2025, 9, 40 21 of 23
References
1. Li, R. Artificial Intelligence Revolution: How AI Will Change Our Society, Economy, and Culture; Skyhorse: New York, NY, USA, 2020.
2. Roetzer, P .; Kaput, M. Marketing Artificial Intelligence: AI, Marketing, and the Future of Business ; BenBella Books: Dallas, TX,
USA, 2022.
3. Gerhard, T. Bias: Considerations for research practice. Am. J. Health-Syst. Pharm. 2008, 65, 2159–2168. [CrossRef] [PubMed]
4. Schwartz, R.; Vassilev, A.; Greene, K.; Perine, L.; Burt, A.; Hall, P .Towards a Standard for Identifying and Managing Bias in Artificial
Intelligence; NIST Special Publication 1270; US Department of Commerce, National Institute of Standards and Technology:
Gaithersburg, MD, USA, 2022.
5. Stamford, C. Gartner Survey Finds 63% of Marketing Leaders Plan to Invest in Generative AI in the Next 24 Months. 2023.
Available online: https://www.gartner.com/en/newsroom/press-releases/2023-08-23-gartner-survey-finds-63-percent-of-
marketing-leaders-plan-to-invest-in-generative-ai-in-the-next-24-months (accessed on 23 March 2024).
6. Buczek, L.; Holder-Browne, A.; Maddox, M.; Kurtzman, W.; Jimenez, D.; Rajagopal, S.; Lall, R.; White, S.; Wallace, D. IDC
FutureScape: Worldwide Chief Marketing Officer 2024 Predictions. October 2023. IDC FutureScape. Available online: https:
//www.idc.com/getdoc.jsp?containerId=US50107023 (accessed on 12 October 2024).
7. Rethlefsen, M.L.; Page, M.J. PRISMA 2020 and PRISMA-S: Common questions on tracking records and the flow diagram. J. Med.
Libr. Assoc. 2022, 110, 253. [CrossRef]
8. Mousavi, Z.; Varahram, S.; Ettefagh, M.; Sadeghi, M.; Feng, W.; Bayat, M. A digital twin-based framework for damage detection
of a floating wind turbine structure under various loading conditions based on deep learning approach. Ocean Eng. 2024, 292,
116563. [CrossRef]
9. Crockett, L. “All AI’s Are Psychopaths”? Reckoning and Judgment in the Quest for Genuine AI; Augsburg University: Minneapolis,
MN, USA, 2020.
10. Heimo, O.I.; Kimppa, K.K. No Worries-the AI Is Dumb (for Now). Tethics 2019, 5, 1–8.
11. Earley, S. Using the customer journey to optimise the marketing technology stack. Appl. Mark. Anal. 2021, 6, 190–210. [CrossRef]
12. Buolamwini, J.; Gebru, T. Gender shades: Intersectional accuracy disparities in commercial gender classification. In Proceedings
of the Conference on Fairness, Accountability and Transparency, New York, NY, USA, 23–24 February 2018; pp. 77–91.
13. Ziakis, C.; Vlachopoulou, M. Artificial Intelligence in Digital Marketing: Insights from a Comprehensive Review. Information
2023, 14, 664. [CrossRef]
14. Haleem, A.; Javaid, M.; Qadri, M.A.; Singh, R.P .; Suman, R. Artificial intelligence (AI) applications for marketing: A literature-
based study. Int. J. Intell. Netw. 2022, 3, 119–132. [CrossRef]
15. Nair, K.; Gupta, R. Application of AI technology in modern digital marketing environment. World J. Entrep. Manag. Sustain. Dev.
2021, 17, 318–328. [CrossRef]
16. Brenner, M. The Ultimate Guide to a Content Marketing Strategy That Delivers ROI. Marketing Insider Group. 2023. Available
online: https://marketinginsidergroup.com/content-marketing/content-marketing-strategy-roi-ultimate-guide/ (accessed on 5
January 2024).
17. Kotzsch, R. Reduce Marketing Costs by Reducing Your Translation Costs. Smart Brief. 2023. Available online: https://www.
smartbrief.com/original/reduce-marketing-costs-by-reducing-your-translation-costs (accessed on 7 November 2023).
18. Rudan, N. 6 Ways Marketers Are Using Generative AI: Is It Really Saving Time? Databox. 2023. Available online: https:
//databox.com/how-are-marketers-using-gen-ai (accessed on 8 February 2024).
19. Scott, D.M. The New Rules of Marketing and PR: How to Use Content Marketing, Podcasting, Social Media, AI, Live Video, and Newsjacking
to Reach Buyers Directly; John Wiley & Sons: London, UK, 2022.
20. Sun, L.; Wei, M.; Sun, Y.; Suh, Y.J.; Shen, L.; Yang, S. Smiling women pitching down: Auditing representational and presentational
gender biases in image-generative AI. J. Comput.-Mediat. Commun. 2024, 29, 45–53. [CrossRef]
21. Henning, T.M. Don’t Just “Google It”: Argumentation and Racist Search Engines. Fem. Philos. Q. 2022, 8, 2. [CrossRef]
22. Tang, R.; Du, M.; Li, Y.; Liu, Z.; Zou, N.; Hu, X. Mitigating Gender Bias in Captioning Systems. In Proceedings of the IW3C2
Proceedings from International World Wide Web Conference Committee, New York, NY, USA, 3 June 2021.
23. Tatman, R. Gender and Dialect Bias in YouTube’s Automatic Captions. In Proceedings of the First ACL Workshop on Ethics in
Natural Language Processing. Association for Computational Linguistics, Valencia, Spain, 18 April 2017.
24. Koenecke, A.; Nam, A.; Lake, W.; Goel, S. Racial disparities in automated speech recognition. In Proceedings of the National
Academy of Sciences, Washington, DC, USA, 23 March 2020.
25. Conick, H. Read This Story to Learn How Behavioral Economics Can Improve Marketing. AMA. 2023. Available on-
line: https://www.ama.org/publications/MarketingNews/Pages/read-story-learn-how-behavioral-economics-can-improve-
marketing.aspx. (accessed on 6 November 2023).
26. Smith, M.; Conrad, S. Algorithmic Bias: A Threat to Digital Marketing Ethical Practices. J. Bus. Ethics 2020, 163, 623–634.
27. Diakopoulos, N. Accountability in algorithmic decision making. Commun. ACM 2016, 59, 56–62. [CrossRef]

Big Data Cogn. Comput. 2025, 9, 40 22 of 23
28. Karimi-Mamaghan, M.; Mohammadi, M.; Meyer, P .; Mohammad, A.; Karimi-Mamaghan, A.; Talbi, E. Machine learning at the
service of meta-heuristics for solving combinatorial optimization problems: A state-of-the-art. Eur. J. Oper. Res. 2022, 296, 393–422.
[CrossRef]
29. Lipton, Z. The mythos of model interpretability. Acmqueue 2016, 5, 1–27.
30. Metz, C.; Thompson, S. What to Know About Tech Companies Using A.I. to Teach Their Own A.I. 2024. Available online:
https://www.nytimes.com/2024/04/06/technology/ai-data-tech-companies.html (accessed on 10 February 2024).
31. Kaminski, N. Women in Tech: Why Are Only 10% of Software Developers Female? 2023. Available online: https://jetrockets.
com/blog/women-in-tech-why-are-only-10-of-software-developers-female (accessed on 6 February 2024).
32. Vailshery, L. Software Developers: Distribution by Gender 2022. 2022. Available online: https://www.statista.com/statistics/11
26823/worldwide-developer-gender/ (accessed on 2 March 2024).
33. Yalkin, C.; Özbilgin, M. Neo-colonial hierarchies of knowledge in marketing: Toxic field and illusion. Mark. Theory 2022, 22,
191–209. [CrossRef]
34. Palmer, L. Traditional AI vs GenAI: Amplified Risks and Challenges in Governance Explained. 2023. Available online:
https://www.drlisa.ai/post/traditional-ai-vs-genai-amplified-risks-and-challenges-in-ai-governance-explained (accessed on 10
November 2023).
35. Huang, M.H.; Rust, R.T. A strategic framework for artificial intelligence in marketing. J. Acad. Mark. Sci. 2021, 49, 30–50.
[CrossRef]
36. Buch, I.; Thakkar, M. AI in Advertising. 2023. Available online: https://www.researchgate.net/publication/357268694_AI_in_
Advertising (accessed on 8 February 2024).
37. Yu, Y. The Role and Influence of Artificial Intelligence on Advertising Industry. Adv. Soc. Sci. Educ. Humanit. Res. 2021, 631,
190–194.
38. Nesterenko, V .; Olefirenko, O. The impact of AI development on the development of marketing communications. Mark.
Menedžment Innovacij 2023, 14, 169–181. [CrossRef]
39. Brynjolfsson, E.; Rock, D.; Syverson, C. Artificial intelligence and the modern productivity paradox. Econ. Artif. Intell. Agenda
2019, 23, 23–57.
40. Jarrahi, M.; Askay, D.; Eshraghi, A.; Smith, P . Artificial intelligence and knowledge management: A partnership between human
and AI. Bus. Horiz. 2023, 66, 87–99. [CrossRef]
41. Jones, P .; Wynn, M. Artificial Intelligence and Corporate Digital Responsibility.J. Artif. Intell. Mach. Learn. Data Sci. 2023, 1, 50–58.
[CrossRef] [PubMed]
42. Dwivedi, Y.K.; Kshetri, N.; Hughes, L.; Slade, E.L.; Jeyaraj, A.; Kar, A.K.; Baabdullah, A.M.; Koohang, A.; Raghavan, V .; Ahuja, M.;
et al. “So what if ChatGPT wrote it?” Multidisciplinary perspectives on opportunities, challenges and implications of generative
conversational AI for research, practice and policy. Int. J. Inf. Manag. 2023, 71, 102642. [CrossRef]
43. Nadeem, A.; Abedin, B.; Marjanovic, O. Gender bias in AI: A review of contributing factors and mitigating strategies. In
Proceedings of the Australasian Conference on Information Systems, Wellington, New Zealand, 1 December 2020.
44. Varona, D.; Suárez, J.L. Discrimination, Bias, Fairness, and Trustworthy AI. Appl. Sci. 2022, 12, 5826. [CrossRef]
45. Shachar, C.; Gerke, S. Prevention of bias and discrimination in clinical practice algorithms. JAMA 2023, 4, 283–284. [CrossRef]
46. Dinesh, C. Mitigating AI Bias: Strategies for Ethical and Fair Algorithms. 21 November 2023. Linked-In. Available online: https:
//www.linkedin.com/pulse/mitigating-ai-bias-strategies-ethical-fair-algorithms-dinesh-c-qeg2c/ (accessed on 12 January 2024).
47. Kaur, A. Mitigating Bias in AI and Ensuring Responsible AI. No Date. Leena AI. Available online: https://leena.ai/blog/
mitigating-bias-in-ai/#:~:text=Strategies%20for%20Identifying%20and%20Addressing%20Bias%20in%20AI%20Systems&
text=One%20crucial%20approach%20is%20diverse,more%20equitable%20and%20unbiased%20decisions (accessed on 14
January 2025).
48. Lemon, K.N.; Verhoef, P .C. Understanding customer experience throughout the customer journey. J. Mark. 2016, 80, 69–96.
[CrossRef]
49. Moorman, C.; Soli, J.; Seals, M. How the Pandemic Changed Marketing Channels. Harvard Business Review. 2023. Available
online: https://hbr.org/2023/08/how-the-pandemic-changed-marketing-channels (accessed on 10 February 2024).
50. Micheaux, A.; Bosio, B. Customer Journey Mapping as a New Way to Teach Data-Driven Marketing as a Service.J. Mark. Educ.
2019, 41, 127–140. [CrossRef]
51. Purmonen, A.; Jaakkola, E.; Terho, H. B2B customer journeys: Conceptualization and an integrative framework.Ind. Mark. Manag.
2023, 113, 74–87. [CrossRef]
52. Strong, F. B2B Sales Cycles Require 27 Interactions both Digital and Human [Study]. 2022. Available online: https://www.
swordandthescript.com/2022/05/b2b-sales-interactions/ (accessed on 14 February 2024).
53. Santosh, M. Artificial Intelligence and Digital Marketing: An Overview. Int. J. Eng. Sci. Humanit. 2024, 14, 118–122. [CrossRef]
54. Jabareen, Y. Building a conceptual framework: Philosophy, definitions, and procedure. Int. J. Qual. Methods 2009, 8, 49–62.
[CrossRef]

Big Data Cogn. Comput. 2025, 9, 40 23 of 23
55. Dowling, K.; Guhl, D.; Klapper, D.; Spann, M.; Stich, L.; Yegoryan, N. Behavioral biases in marketing. J. Acad. Mark. Sci. 2020, 48,
449–477. [CrossRef]
56. Schwandt, T. Constructivist, interpretivist approaches to human inquiry. Handb. Qual. Res. 1994, 1, 118–137.
57. Flick, U.; von Kardorff, E.; Steinke, I. Qualitative Forschung. Ein Handbuch ; Qualitative Research. A Handbook; Rowohlt
Taschenbuch: Hamburg, Germany, 2013.
58. Holliday, A. Doing & Writing (3e)-Qualitative Research; SAGE Publications: London, UK, 2006.
59. Thomas, D.R. A General Inductive Approach for Analyzing Qualitative Evaluation Data.Am. J. Eval. 2006, 27, 237–246. [CrossRef]
60. Saunders, M.; Lewis, P .; Thornhill, A. Research Methods for Business Students, 3rd ed.; Pearson Education Limited: London, UK, 2023.
61. Creswell, J.W.; Creswell, J.D. Research Design: Qualitative, Quantitative, and Mixed Methods Approaches; Sage: London, UK, 2018.
62. Islam, M.; Aldaihani, F. Justification for Adopting Qualitative Research Method, Research Approaches, Sampling Strategy, Sample
Size, Interview Method, Saturation, and Data Analysis. J. Int. Bus. Manag. 2022, 5, 1–11.
63. Guest, G.; Bunce, A.; Johnson, L. How Many Interviews Are Enough? An Experiment with Data Saturation and Variability. Field
Methods 2006, 18, 59–82. [CrossRef]
64. Ritchie, J.; Lewis, J.; Elam, G. Designing and selecting samples. In Qualitative Research Practice: A Guide for Social Science Students
and Researchers; Ritchie, J., Lewis, J., Eds.; Sage Publications Ltd.: London, UK, 2003; pp. 77–108.
65. Lee, N.; Lings, I. Doing Business Research: A Guide to Theory and Practice; Sage Publications Ltd.: London, UK, 2008.
66. Cauteruccio, F. Investigating the emotional experiences in eSports spectatorship: The case of League of Legends. Inf. Process.
Manag. 2023, 60, 103516. [CrossRef]
67. Terry, G.; Hayfield, N.; Clarke, V .; Braun, V . Thematic analysis. SAGE Handb. Qual. Res. Psychol. 2017, 2, 17–37.
68. Webb, C. Analysing qualitative data: Computerized and other approaches. J. Adv. Nurs. 2001, 29, 323–330. [CrossRef]
69. Mason, J. ‘Re-using’ qualitative data: On the merits of an investigative epistemology.Sociol. Res. Online 2007, 12, 39–42. [CrossRef]
70. Smith, J.; Firth, J. Qualitative data analysis: The framework approach. Nurse Res. 2011, 18, 42–48. [CrossRef]
71. Onwuegbuzie, A.J.; Leech, N.L.; Collins, K.M. Qualitative analysis techniques for the review of the literature. Qual. Rep. 2012, 17,
17–28. [CrossRef]
72. Gray, D. Doing Research in the Business World; Sage Publications Ltd.: London, UK, 2019; pp. 1–896.
73. Yin, R.K. Case Study Research and Applications: Design and Methods, 6th ed.; Sage Publications Ltd.: London, UK, 2018.
74. Flyvbjerg, B. Five misunderstandings about case-study research. Qual. Inq. 2006, 12, 219–245. [CrossRef]
75. Arsenijevic, U.; Jovic, M. Artificial intelligence marketing: Chatbots. In Proceedings of the 2019 International Conference on
Artificial Intelligence: Applications and Innovations, Hersonissos, Greece, 24–26 May 2019; pp. 19–193.
76. Rakib, S.; Rabbi, S.N. Ai in Digital Marketing. Bachelor’s Thesis, Seinajoki University, Seinäjoki, Finland, 2024.
77. Permana, B. The Strategy for Developing a Marketplace Promotion Model Based on Artificial Intelligence (AI) to Improve Online
Marketing in Indonesia. Int. J. Soc. Sci. Bus. 2024, 8, 190–197.
78. Flavin, S.; Heller, J. A Technology Blueprint for Personalization at Scale; McKinsey: New York, NY, USA, 2019.
79. Meda, K. Biased Advertising: Identifying & Addressing the Problem. 2023. Available online: https://kortx.io/news/biased-
advertising/ (accessed on 7 February 2024).
80. Nygård, R. AI-Assisted Lead Scoring. Master’s Thesis, Åbo Akademi University, Turku, Finland, 2019.
81. Hayes, J.L.; Britt, B.C.; Evans, W.; Rush, S.W.; Towery, N.A.; Adamson, A.C. Can Social Media Listening Platforms’ Artificial
Intelligence Be Trusted? Examining the Accuracy of Crimson Hexagon’s AI-Driven Analyses.J. Advert. 2020, 50, 81–91. [CrossRef]
82. Limoa. What Is the Role of AI in Customer Feedback Analysis? 2024. Available online: https://www.lumoa.me/blog/artificial-
intelligence-customer-feedback-analysis/ (accessed on 6 March 2024).
83. Ghadage, A.; Yi, D.; Coghill, G.; Pang, W. Multi-stage bias mitigation for individual fairness in algorithmic decisions. InIAPR
Workshop on Artificial Neural Networks in Pattern Recognition; Springer International Publishing: New York, NY, USA, 2022.
84. Zhang, W.; Weiss, J.C. Fairness with censorship and group constraints. Knowl. Inf. Syst. 2023, 65, 2571–2594. [CrossRef]
85. Welsch, A. Humans and AI: Designing Collaboration for A Better Future. 2024. Available online: https://intelligencebriefing.
substack.com/p/human-ai-collaboration-for-adaptive-processes?utm_source=publication-search (accessed on 22 February 2024).
86. Lee, E. The Data Maturity Model: Master Your Data in 5 Easy Stages. 2024. Available online: https://kortxprod.wpenginepowered.
com/news/data-maturity-model/ (accessed on 6 February 2024).
87. Wilson, R. A Guide to Take Your Third-Party Data to the Next Level. 2024. Available online: https://kortxprod.wpenginepowered.
com/news/third-party-data/ (accessed on 6 February 2024).
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.
