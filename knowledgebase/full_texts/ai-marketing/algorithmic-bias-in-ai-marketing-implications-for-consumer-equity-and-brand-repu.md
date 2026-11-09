---
title: 'Algorithmic Bias in AI Marketing: Implications for Consumer Equity and Brand Reputation'
url: https://doi.org/10.22158/ibes.v8n4p1
category: ai-marketing
subcategory: review
date: 2026-10
venue: International Business & Economics Studies
authors:
- Mohammadali Shahbandi
source: openalex-oa
pdf_url: https://www.scholink.org/ojs/index.php/ibes/article/view/58140/21015
pages: 36
chars: 104859
fetched_at: '2026-11-08T20:00:58+00:00'
kb_version: 1
---

# Algorithmic Bias in AI Marketing: Implications for Consumer Equity and Brand Reputation

International Business & Economics Studies
ISSN 2640-9852 (Print) ISSN 2640-9860 (Online)
Vol. 8, No. 4, 2026
www.scholink.org/ojs/index.php/ibes
1
Original Paper
Algorithmic Bias in AI Marketing: Implications for Consumer
Equity and Brand Reputation
Mohammadali Shahbandi1
1 Keiser University, United States
Received: August 26, 2026 Accepted: September 19, 2026 Online Published: October 06, 2026
doi:10.22158/ibes.v8n4p1 URL: http://dx.doi.org/10.22158/ibes.v8n4p1
Abstract
Artificial intelligence (AI) is increasingly embedded in targeting, personalization, pricing,
recommendation, and content-generation systems, intensifying concerns about algorithmic bias and its
consequences for consumers and brands. This critical literature review synthesizes peer-reviewed and
applied research published primarily between 2017 and 2025 to examine how bias enters AI-enabled
marketing through data, model design, optimization objectives, and deployment contexts. The synthesis
identifies three recurring mechanisms data, model, and contextual bias and shows how they can
produce representational, measurement, and evaluation disparities. Across the reviewed literature,
these disparities are associated with discriminatory targeting, exclusion, opaque personalization,
perceived unfairness, and erosion of consumer trust, with downstream risks for brand legitimacy and
reputation. The review further integrates technical, organizational, and regulatory mitigation
approaches, including data audits, fairness-aware modeling, explainable AI, human oversight,
governance structures, impact assessment, and regulatory compliance. The article contributes an
integrated socio-technical perspective that connects the AI lifecycle to consumer-equity outcomes and
reputational consequences. It concludes that responsible AI marketing requires fairness and
accountability to be treated as design and governance objectives rather than post-hoc corrections.
Keywords
Algorithmic Bias, AI Marketing, Consumer Equity, Brand Reputation, Ethical Governance
1. Introduction
The integration of Artificial Intelligence (AI) has fundamentally reshaped the modern marketing
landscape, permeating virtually every function, from sophisticated customer segmentation and dynamic
pricing models to highly personalized content recommendations and automated campaign execution.
These advanced systems promise unparalleled efficiency, optimized decision-making, and the delivery

www.scholink.org/ojs/index.php/ibes International Business & Economics Studies Vol. 8, No. 4, 2026
Published by SCHOLINK INC.
2
of highly tailored consumer experiences, driving what many see as the future of brand engagement.
However, this transformative power comes with a critical caveat: AI marketing systems are not neutral
tools. As highlighted by Akter et al. (2022), algorithmic decisions possess the profound capacity to
reinforce and even exacerbate pre-existing societal inequalities inadvertently. This phenomenon,
known as algorithmic bias, stems from various points within the AI lifecycle, primarily originating
from historical prejudices embedded within the vast datasets used to train these systems, or from the
optimization goals that prioritize business performance metrics (like conversion rates or ROI) often at
the expense of broader ethical considerations such as fairness and transparency.
The increasing reliance on these data-driven models, frequently compounded by an inherent lack of
explainability and inadequate fairness protocols, has rapidly elevated algorithmic bias from a technical
flaw to a significant business and societal risk. In the context of marketing, this issue is particularly
problematic because it can lead to subtle yet pervasive discriminatory practices. For example, AI might
unintentionally exclude certain demographics from seeing job advertisements, limit access to credit
offers, or even deprioritize specific consumer groups from receiving advantageous personalized
discounts. As the marketing industry continues its relentless pursuit of hyper-personalized experiences,
the potential for reinforcing harmful stereotypes, alienating vulnerable consumers, and eroding public
trust grows exponentially.
This article undertakes a comprehensive review of scholarly and applied literature on algorithmic bias
in AI marketing. Our objective is twofold: first, to thoroughly examine how bias, stemming from data,
models, and deployment contexts, directly affects consumer equity—addressing issues of
discrimination, exclusion, and perceived fairness—and significantly impacts brand reputation through
public backlash and challenges to corporate social responsibility. Second, the article aims to synthesize
and present actionable recommendations and mitigation strategies across technical, organizational, and
regulatory dimensions. By tracing the lifecycle of bias and its far-reaching consequences, this review
advocates for an interdisciplinary response that centers consumer equity and ethical accountability,
asserting that in a digital economy increasingly shaped by algorithms, the legitimacy of marketing
practices—and the brands behind them—now critically hinges on how effectively they confront bias
and foster trust.
2. Review Method
This study uses a critical integrative literature review to examine algorithmic bias in AI-driven
marketing. The purpose is conceptual synthesis rather than meta-analysis or a PRISMA-style
systematic review. The review combines peer-reviewed research with selected applied and case-based
sources where they illuminate marketing practice, consumer consequences, or governance responses.
Because the original search records did not retain a complete reproducible screening log, this
manuscript does not report a fabricated flow count; a future systematic-review version should

www.scholink.org/ojs/index.php/ibes International Business & Economics Studies Vol. 8, No. 4, 2026
Published by SCHOLINK INC.
3
preregister the protocol and document database-specific search strings, search dates, deduplication,
screening decisions, and final study counts.
The literature search was conducted across major databases including Scopus, Web of Science, Google
Scholar, and SpringerLink, supplemented with targeted searches in marketing and information systems
journals. Keywords used included “algorithmic bias in marketing”, “AI fairness”, “consumer equity”,
“brand reputation”, “dynamic pricing discrimination”, and “ethical AI governance”. The inclusion
criteria were:
 Publication period: 2017-2025, to ensure coverage of the most recent advances in AI
marketing.
 Disciplinary scope: marketing, business ethics, information systems, and computer science.
 Content relevance: studies addressing bias in AI applications for marketing, including
segmentation, personalization, pricing, and advertising.
To ensure comprehensiveness, both conceptual and empirical works were included. Exclusion criteria
involved purely technical AI studies with no consumer or marketing context, as well as opinion pieces
lacking empirical or theoretical grounding.
The synthesis was structured around the lifecycle of algorithmic bias—from data, models, and
deployment contexts—to map how bias manifests at each stage. Findings were then categorized
according to their implications for consumer equity (e.g., discrimination, transparency, fairness
perceptions) and brand reputation (e.g., backlash, CSR alignment, ethical consumerism). This thematic
organization enables a holistic view of how algorithmic bias simultaneously functions as a
socio-technical challenge and a reputational risk.
3. Conceptual Foundations
3.1 What is Algorithmic Bias?
Algorithmic bias refers to systematic and repeatable errors in AI systems that lead to unfair,
discriminatory, or exclusionary outcomes, disproportionately affecting marginalized or minority groups.
In the context of AI-driven marketing, such biases not only distort business intelligence but also risk
alienating vulnerable consumer segments.

www.scholink.org/ojs/index.php/ibes International Business & Economics Studies Vol. 8, No. 4, 2026
Published by SCHOLINK INC.
4
Figure 1. Ethical issues of AI
As Akter et al. (2022) explain, these biases may originate from historical prejudices embedded in
training datasets or from implicit assumptions made by developers during the model design process.
For instance, if a marketing algorithm is trained on consumer behavior data that reflects historical
patterns of discrimination (e.g., underrepresentation of certain ethnicities in high-income segments), the
AI model will likely replicate those inequalities when recommending products or setting personalized
prices.
These biases are generally categorized as:
 Pre-existing bias: Rooted in real-world inequalities that are mirrored in the data used to train
AI systems. For example, historical underrepresentation of certain groups in marketing campaigns or
brand engagement data can skew predictions.
 Technical bias: Introduced during the modeling process—such as how features are selected,
how data is normalized, or which algorithmic parameters are prioritized. These biases often arise when
model designers make assumptions about what constitutes “normal” or “average” consumer behavior.
 Emergent bias: Develops after deployment as AI systems interact with users and environments
in real-time. These systems continuously learn from user data, which may itself be biased. Over time,
the AI may reinforce patterns that privilege dominant consumer behaviors while marginalizing others.
Algorithmic bias is not simply a flaw in computational logic—it reflects a complex interplay of social
structures, organizational priorities, and technological design choices. These systems are embedded in
broader marketing ecosystems where commercial incentives, performance metrics, and data collection
practices all influence how AI behaves in the real world (Reed et al., 2025).
Moreover, as Reed et al. (2025) emphasize, the consequences of algorithmic bias in marketing are not
just ethical but also commercial. Biased systems can erode consumer trust, trigger backlash on social
media, and harm brand reputation. For example, biased ad targeting that systematically excludes certain
racial or gender groups—whether intentionally or through automation—can lead to accusations of
discrimination, regulatory scrutiny, and customer attrition.
Akter et al. (2022) and Reed et al. (2025) stress that algorithmic bias is not static; it can intensify over
time through feedback loops, where biased outputs are treated as valid data in future model training.
This recursive cycle makes early detection and ongoing monitoring essential.

www.scholink.org/ojs/index.php/ibes International Business & Economics Studies Vol. 8, No. 4, 2026
Published by SCHOLINK INC.
5
In sum, algorithmic bias in AI marketing systems must be viewed as a socio-technical challenge,
requiring not only algorithmic scrutiny but also critical reflection on how business models, data
collection strategies, and team diversity influence AI behavior. Combating bias demands a
multi-pronged strategy that includes inclusive data practices, bias auditing tools, and cross-functional
ethical oversight.
3.2 AI Applications in Marketing
AI technologies enable firms to automate and optimize targeting, segmentation, personalization, pricing,
and campaign analysis. However, these same systems can also replicate discriminatory patterns unless
bias mitigation is embedded into the design (Akter et al., 2023).
Huang and Rust (2021) categorize AI's role in marketing across four evolutionary stages: mechanical
(automation), thinking (decision-making), feeling (empathy), and social (relationship management).
These dimensions illuminate how deeply AI now penetrates marketing operations—from personalized
content generation to customer engagement via chatbots and recommendation engines. However, they
caution that as AI evolves from rule-based systems to emotional and social engagement tools, the risk
of embedded bias grows more complex and harder to detect. For example, emotional AI applications
may unintentionally amplify stereotypical narratives or exclude minority emotional contexts.
3.3 Theoretical Lenses
Kordzadeh and Ghasemaghaei (2022) emphasize the importance of incorporating ethical
decision-making frameworks such as consequentialism and fairness-through-awareness in AI systems.
Their findings support a multi-level approach—technical, organizational, and regulatory—to address
ethical challenges.
Huang and Rust (2021) propose that AI systems be viewed through a strategic lens, where
organizations actively decide the level of AI autonomy and domain of deployment. The more autonomy
given to AI, the greater the need for embedded ethical constraints. This idea connects to bias: fully
autonomous systems that operate without human oversight are more likely to perpetuate bias silently.
Their strategic framework includes “value creation”, “customer journey touchpoints”, and “AI learning
feedback loops” as essential sites where fairness must be integrated.
The ethical deployment of AI in marketing requires moving beyond technical competence toward
organizational responsibility and consumer trust management. According to Naz and Kashif (2025),
ethical marketing AI must be guided by four foundational principles:
 Responsibility (Who is accountable for bias?)
 Transparency (Can consumers understand model outputs?)
 Fairness (Are outputs equitable across demographics?)
 Explainability (Are decisions justifiable?)
These ethical dimensions are not merely theoretical; they influence the strategic design of AI systems.
Naz and Kashif (2025), proposes a governance approach that integrates ethical values directly into the

www.scholink.org/ojs/index.php/ibes International Business & Economics Studies Vol. 8, No. 4, 2026
Published by SCHOLINK INC.
6
AI development pipeline, encouraging firms to embed consumer-centric safeguards at every
level—from data collection to output dissemination.
4. Algorithmic Bias in Marketing Systems
Algorithmic bias in marketing systems is deeply rooted in the full lifecycle of AI development and
deployment—emerging from the data used to train models, the objectives encoded into those models,
and the contexts in which they operate. Across the literature (Naz & Kashif, 2025; Reed et al., 2025),
three interrelated sources of bias consistently recur: data bias, model bias, and contextual (deployment)
bias. These sources not only affect AI’s technical accuracy but also significantly shape consumer
inclusion, visibility, and access.
4.1 Sources of Bias
4.1.1 Data Bias
Data bias arises when training datasets used to build AI models encode existing social, cultural, and
economic disparities. Marketing systems often rely on historical consumer data—such as purchase
histories, clickstreams, geolocation, and engagement metrics—which reflect prior patterns of
discrimination or exclusion (Naz & Kashif, 2025; Gonçalves et al., 2023; Hermann, 2022). For instance,
if certain groups—such as lower-income individuals, older adults, or rural populations—have
historically received fewer personalized offers or interacted less with digital platforms, their behaviors
will be underrepresented or mischaracterized in the training data (Eid et al., 2024; Deldjoo et al., 2024;
Mehrabi et al., 2021).
This leads to skewed learning, where models fail to accurately predict the preferences or needs of these
groups. In some cases, AI systems may even infer that these consumers are ‘less valuable,’ resulting in
their exclusion from premium offerings, loyalty programs, or targeted communications (Naz & Kashif,
2025; Mehrabi et al., 2021; Su et al., 2023). The problem is particularly acute in mobile commerce,
where data sparsity and behavioral variance among less digitally active users result in algorithms being
‘blind’ to certain demographic profiles (Reed et al., 2025).
Moreover, the use of web-scraped or large-scale digital corpora in training language models introduces
additional layers of bias. For example, AI-generated marketing slogans trained on biased language
datasets have shown disproportionate associations between certain demographics and stereotypical
messaging (Yilmaz & Ashqar, 2025).
4.1.2 Model Bias
Model bias refers to the internal logic and optimization strategies embedded in AI algorithms. In
marketing, models are frequently trained to maximize business-centric performance metrics such as
conversion rate, return on investment (ROI), click-through rate (CTR), or customer lifetime value (CLV)
(Gonçalves et al., 2023; Eid et al., 2024; Deldjoo et al., 2024). These goals, while commercially
justified, often conflict with principles of fairness and inclusion.
When algorithms are optimized purely for profitability, they inherently favor behavioral patterns

www.scholink.org/ojs/index.php/ibes International Business & Economics Studies Vol. 8, No. 4, 2026
Published by SCHOLINK INC.
7
exhibited by the most profitable or active segments—typically majority groups (Naz & Kashif, 2025;
Hermann, 2022; Mehrabi et al., 2021). For example, a recommender system that prioritizes users with
frequent engagement may ignore consumers who are less predictable or whose behavior deviates from
the norm. This leads to overfitting to dominant user profiles and underperformance for outliers or
minorities (Eid et al., 2024; Su et al., 2023).
In many cases, models rely on proxy variables such as device type, browser history, or location data to
infer user intent. These variables, while operationally efficient, often correlate with protected attributes
like race, gender, or socioeconomic status, embedding discrimination into outputs without explicit
intent (Gonçalves et al., 2023; Mehrabi et al., 2021).
Additionally, model bias is exacerbated by the lack of fairness-aware learning techniques. Few
marketing models incorporate fairness constraints, adversarial debiasing, or subgroup-specific
objectives—leading to systems that reinforce existing hierarchies under the guise of personalization
(Naz & Kashif, 2025; Deldjoo et al., 2024).
4.1.3 Contextual Bias
Contextual or deployment bias emerges once AI systems are operational and begin interacting with
dynamic user environments. Unlike static software, AI models evolve over time through consumer
interactions, which feed back into future model iterations. These feedback loops can reinforce and
amplify initial disparities (Naz & Kashif, 2025; Deldjoo et al., 2024; Mehrabi et al., 2021). For
example, a consumer who receives irrelevant content due to biased training data may engage less,
leading the algorithm to deprioritize them in subsequent rounds—a process known as self-reinforcing
exclusion (Eid et al., 2024; Mehrabi et al., 2021).
Marketing contexts—such as mobile interfaces, platform-specific constraints, and limited user
control—further entrench contextual bias (Reed et al., 2025). In mobile environments, personalization
is influenced by real-time responsiveness, UI/UX design, and fragmented consumer feedback, all of
which constrain the ability of consumers to contest or reshape algorithmic decisions. The opacity of
many AI systems means that users may not understand why they are receiving certain ads or prices,
reducing their ability to intervene or seek recourse (Reed et al., 2025; Hermann, 2022; Quach et al.,
2022).
Human oversight and organizational culture also play a role. Even technically fair models can behave
unfairly if deployed without accountability mechanisms, interpretive frameworks, or inclusive business
strategies (Deldjoo et al., 2024; Mehrabi et al., 2021; Su et al., 2023). In many marketing teams,
fairness is not embedded as a design priority—meaning biased outputs are often normalized,
rationalized, or left unchecked (Mehrabi et al., 2021; Reed et al., 2025).

www.scholink.org/ojs/index.php/ibes International Business & Economics Studies Vol. 8, No. 4, 2026
Published by SCHOLINK INC.
8
Figure 2. Sources of Bias
4.2 Types of Bias
Algorithmic bias in marketing systems is multifaceted, taking distinct yet interrelated forms. Scholars
have broadly categorized these into representation bias, measurement bias, and evaluation bias—each
affecting different phases of the AI lifecycle and often reinforcing the others (Naz & Kashif, 2025;
Gonçalves et al., 2023; Hermann, 2022). Understanding these bias types is essential for diagnosing and
mitigating the exclusionary tendencies of data-driven marketing technologies.
4.2.1 Representation Bias
Representation bias occurs when specific demographic groups or behavioral patterns are inadequately
captured—or disproportionately associated with negative outcomes—in the training data (Naz &
Kashif, 2025; Gonçalves et al., 2023; Mehrabi et al., 2021). In marketing systems, this often stems
from the use of CRM databases, web analytics, or digital engagement logs that overrepresent affluent,
urban, or majority users while marginalizing consumers from lower-income, rural, or minority
communities (Hermann, 2022; Mehrabi et al., 2021; Su et al., 2023).
For instance, if older consumers or individuals from the Global South engage less frequently with a
brand’s digital assets, they may be underrepresented in high-engagement segments. This absence
reduces the algorithm's exposure to these groups and subsequently its ability to make accurate or
relevant predictions for them (Gonçalves et al., 2023; Mehrabi et al., 2021). In turn, these consumers
are less likely to receive targeted offers, premium content, or personalized messaging, contributing to a
widening of digital inequality (Eid et al., 2024; Deldjoo et al., 2024).
Additionally, AI-generated marketing language has demonstrated representational bias by associating
certain demographic categories with narrow thematic domains. Yilmaz and Ashqar (2025) found that
slogans generated for women disproportionately included empowerment language, while men were
more often linked with financial terminology—reflecting gender-stereotyped messaging patterns
embedded in language models (Yilmaz & Ashqar, 2025).
4.2.2 Measurement Bias
Measurement bias emerges when the features used by an algorithm are correlated with protected
attributes like race, gender, or socioeconomic status—even if those attributes are not explicitly included
(Gonçalves et al., 2023; Hermann, 2022; Mehrabi et al., 2021). Marketing algorithms typically use

www.scholink.org/ojs/index.php/ibes International Business & Economics Studies Vol. 8, No. 4, 2026
Published by SCHOLINK INC.
9
proxy variables such as zip code, browser type, device usage, or purchase history to infer customer
profiles. However, these features can act as stand-ins for sensitive variables and inadvertently replicate
societal inequalities.
For example, a marketing model might assign lower value scores to users in certain zip codes
historically associated with lower spending—despite no intrinsic relationship between geographic
location and individual consumer worth (Naz & Kashif, 2025; Deldjoo et al., 2024). Similarly, models
may interpret less frequent engagement or smaller basket sizes as indicators of lower lifetime value,
disproportionately penalizing consumers with unconventional or economically constrained behaviors
(Reed et al., 2025; Su et al., 2023).
The problem is further complicated by the opacity of feature selection in many machine learning
models, especially deep learning systems. Without transparency into how features are weighted or
combined, biased correlations can persist undetected, undermining fairness (Eid et al., 2024; Mehrabi
et al., 2021).
4.2.3 Evaluation Bias
Evaluation bias occurs when models are validated using aggregate performance metrics such as overall
accuracy, ROI, or AUC (area under the curve), without assessing how performance varies across
demographic subgroups (Naz & Kashif, 2025; Eid et al., 2024; Hermann, 2022). A model that performs
well for the majority population may still perform poorly for minorities or underrepresented segments,
yet these discrepancies remain hidden in summary statistics (Deldjoo et al., 2024; Su et al., 2023).
This form of bias is particularly insidious because it fosters false confidence in the model’s
effectiveness. For instance, a recommender system might demonstrate high average engagement while
consistently excluding older women from receiving relevant content. Without disaggregated auditing
by gender, age, ethnicity, or income, such systematic underperformance is unlikely to be detected or
addressed (Gonçalves et al., 2023; Mehrabi et al., 2021).
Yilmaz and Ashqar (2025) introduced an empirical approach to uncover evaluation bias by using the
Kolmogorov–Smirnov (KS) test to measure distributional differences in AI-generated language across
demographic groups (Yilmaz & Ashqar, 2025). Their findings confirmed that marketing slogans vary
significantly depending on gender, income, and education level—demonstrating that evaluation must
go beyond surface-level metrics to consider qualitative and linguistic fairness.
These three types of bias—representation, measurement, and evaluation—rarely occur in isolation.
Instead, they interact across the AI pipeline to reinforce digital stratification. Poor representation in data
limits the diversity of behavioral signals available to models, which in turn encourages reliance on
flawed proxies (measurement bias), and these patterns remain obscured when performance is validated
at an aggregate level (evaluation bias) (Eid et al., 2024; Deldjoo et al., 2024; Su et al., 2023).

www.scholink.org/ojs/index.php/ibes International Business & Economics Studies Vol. 8, No. 4, 2026
Published by SCHOLINK INC.
10
Table 1. Summary of Different Types of AI Bias
Type of Bias Description Example from Marketing
Context
Cited Sources
Representation
Bias
Incomplete or
skewed data
coverage of user
groups
Older adults not represented in
engagement data; women
stereotyped in slogans
Gonçalves et al., 2023, Eid et
al., 2024, Mehrabi et al.,
2021, Quach et al., 2022
Measurement
Bias
Use of proxy features
that correlate with
sensitive attributes
Zip code or device type used as
proxy for income or race
Naz & Kashif, 2025,
Hermann, 2022, Mehrabi et
al., 2021
Evaluation
Bias
Performance
assessed only on
average, not by
subgroup
ROI looks good overall, but
minority users receive worse
recommendations
4.3 Real-World Manifestations of Algorithmic Bias in Marketing
The impacts of algorithmic bias in marketing are not merely theoretical—they manifest concretely in
various industry applications, influencing what consumers see, how they are categorized, and which
opportunities they receive. Studies across Naz & Kashif to Nzama-Sithole present a growing body of
empirical evidence and industry illustrations showing how biased marketing algorithms reproduce and
reinforce social inequalities, even when no discriminatory intent is present. These biases emerge across
domains including dynamic pricing, targeted advertising, recommender systems, and AI-generated
content.
4.3.1 Dynamic Pricing Discrimination
One of the most direct and tangible forms of bias is evident in personalized pricing algorithms, where
consumers from certain locations or using particular devices are offered less favorable prices. These
models often rely on behavioral data and technical features—such as device type, browser history, or
zip code—that correlate with socioeconomic status (Naz & Kashif, 2025; Mehrabi et al., 2021). For
example, users accessing e-commerce platforms from high-income zip codes may receive discounts or
loyalty benefits, while those from low-income areas are excluded, perpetuating a form of digital
redlining (Deldjoo et al., 2024; Su et al., 2023).
These pricing disparities are rarely the result of explicit programming but stem from the algorithm's
optimization for profit. When marketing models prioritize consumer segments associated with higher
conversion rates or larger basket sizes, they inadvertently marginalize consumers with less purchasing
power or different shopping behaviors (Gonçalves et al., 2023; Hermann, 2022).

www.scholink.org/ojs/index.php/ibes International Business & Economics Studies Vol. 8, No. 4, 2026
Published by SCHOLINK INC.
11
4.3.2 Discriminatory Ad Delivery and Targeting
Another critical domain is ad targeting and delivery, particularly in platforms such as Facebook or
Google Ads. Even when advertisers input neutral demographic preferences, AI-driven delivery systems
have shown a tendency to favor majority groups in distributing ads for housing, employment, or
financial services (Naz & Kashif, 2025; Deldjoo et al., 2024; Mehrabi et al., 2021). These outcomes are
driven by the algorithm’s learned assumptions about engagement likelihood based on historical
click-through behavior—a pattern shaped by existing inequalities (Eid et al., 2024).
In one high-profile case, Facebook’s ad delivery system disproportionately showed job advertisements
for high-paying positions to white men, even though the targeting parameters were gender- and
race-neutral (Mehrabi et al., 2021). This reflects how AI systems can encode and amplify bias without
human direction, due to the statistical inferences made during optimization.
4.3.3 Biased Content Personalization and Recommender Systems
Recommender systems, central to content marketing and user engagement strategies, frequently
reproduce inequality by prioritizing users who resemble historically profitable or active profiles (Naz &
Kashif, 2025; Eid et al., 2024; Mehrabi et al., 2021). These algorithms often learn to favor younger,
tech-savvy, urban consumers who engage frequently with digital platforms—leading to a feedback loop
where already-visible users gain more visibility, while underrepresented groups are further
marginalized.
For example, individuals with atypical or lower-frequency engagement patterns—such as older adults,
people with disabilities, or residents of the Global South—may be deprioritized by recommendation
engines (Hermann, 2022; Mehrabi et al., 2021). This has led to cases of recommendation blindness,
where certain consumers are never exposed to personalized offers or high-value content, creating
stratified experiences across user segments (Reed et al., 2025; Mehrabi et al., 2021).
Moreover, over-reliance on behavioral proxies exacerbates misclassification risks. Users from
underrepresented communities may be wrongly profiled and receive irrelevant or even offensive
content, undermining the credibility and inclusiveness of the marketing effort (Deldjoo et al., 2024;
Mehrabi et al., 2021).
4.3.4 Bias in AI-Generated Marketing Language
With the rise of large language models (LLMs) like ChatGPT in content creation, new forms of
algorithmic bias are surfacing in the language and narratives used in marketing campaigns. Yilmaz and
Ashqar (2025) conducted a controlled study generating 1,700 finance-related marketing slogans across
17 demographic subgroups, revealing systematic linguistic bias based on gender, income, age,
education, and marital status (Yilmaz & Ashqar, 2025).
Their findings show that:
 Women received slogans disproportionately focused on empowerment and emotion, implying
a stereotype of motivational need.

www.scholink.org/ojs/index.php/ibes International Business & Economics Studies Vol. 8, No. 4, 2026
Published by SCHOLINK INC.
12
 Men were more often presented with financially technical or goal-oriented language,
reinforcing assumptions of economic competence.
 Older consumers were offered less personalized or aspirational messaging compared to
younger audiences.
 Divorced individuals were repeatedly targeted with slogans emphasizing ‘rebuilding’ and
‘recovery,’ suggesting a narrative of fragility.
This linguistic differentiation—though subtle—shapes consumer perceptions, brand resonance, and
self-image. When language models reflect demographic stereotypes learned from training data, they
embed those norms into commercial discourse, often without detection (Yilmaz & Ashqar, 2025).
4.3.5 Structural and Reputational Consequences
These real-world manifestations of bias carry profound implications not only for consumer experience
but also for brand legitimacy and trust. Consumers increasingly recognize algorithmic discrimination,
particularly when it affects sensitive domains like pricing, employment, or financial inclusion (Naz &
Kashif, 2025; Eid et al., 2024). As awareness grows, so does the risk of reputational backlash and
regulatory scrutiny. If left unaddressed, algorithmic marketing systems risk reinforcing systemic
inequality under the guise of personalization and efficiency (Mehrabi et al., 2021; Reed et al., 2025).
Figure 3. Real-world Cases of Biased Marketing Algorithms
5. Implications for Consumer Equity
5.1 Discrimination and Exclusion
Algorithmic discrimination in marketing systems manifests not through overt exclusion, but through
subtle and systemic mechanisms that disproportionately disadvantage certain groups based on attributes
such as race, gender, age, income, education level, or geography. Across Naz & Kashif to
Nzama-Sithole, the literature demonstrates that the optimization goals, data inputs, and behavioral
proxies used in AI systems often reinforce pre-existing social and economic hierarchies—ultimately
resulting in a marketplace that privileges some consumers while marginalizing others (Naz & Kashif,
2025; Gonçalves et al., 2023; Hermann, 2022; Deldjoo et al., 2024).

www.scholink.org/ojs/index.php/ibes International Business & Economics Studies Vol. 8, No. 4, 2026
Published by SCHOLINK INC.
13
5.1.1 Structural Exclusion via Data and Model Design
At the core of this issue lies the design of AI systems, which are often trained on data that
overrepresents affluent, digitally active, and demographically dominant users. This results in
representational gaps, where minority and underrepresented groups are either invisible to the system or
treated as statistical anomalies (Gonçalves et al., 2023; Mehrabi et al., 2021). For example, when AI
models are trained predominantly on high-income user behavior, they learn to optimize for similar
profiles—thereby excluding or misclassifying lower-income consumers as low-engagement or
low-value (Naz & Kashif, 2025; Hermann, 2022; Su et al., 2023).
Such discrimination is rarely intentional; it stems from business goals like maximizing return on ad
spend (ROAS), engagement, or customer lifetime value (CLV)—metrics that inherently favor
profitable consumer segments. As Reed et al. (2025) argue, this leads to a self-reinforcing cycle:
consumers with limited engagement are deprioritized in targeting algorithms, receive fewer
personalized offers, and consequently engage less, further lowering their visibility in the system
(Deldjoo et al., 2024).
5.1.2 Dynamic Pricing and Digital Redlining
A particularly visible example of algorithmic exclusion is found in dynamic pricing systems. Reed et al.
(2025) report that AI-driven pricing algorithms have charged higher prices to users from lower-income
neighborhoods, not due to overt bias, but because the system associated certain zip codes or device
types with lower purchasing power or higher risk (Naz & Kashif, 2025; Reed et al., 2025). This
phenomenon—resembling digital redlining—mirrors historical practices in housing and lending, where
access and terms are stratified based on demographic and socioeconomic signals (Deldjoo et al., 2024;
Su et al., 2023).
Here, AI’s supposed neutrality conceals its role in reproducing unequal access to discounts, loyalty
programs, and competitive offers. Such price discrimination erodes the principle of equitable market
participation, especially when consumers lack insight into the data or logic influencing pricing
decisions (Hermann, 2022).
5.1.3 Recommendation and Segmentation Bias
Recommendation engines and customer segmentation tools further contribute to digital exclusion.
When personalization models overfit to high-engagement segments, they neglect diverse behavioral
patterns and atypical user profiles. This is particularly problematic in sectors like education,
employment, finance, and healthcare—domains where access to relevant information or services can
meaningfully impact quality of life (Gonçalves et al., 2023; Eid et al., 2024; Mehrabi et al., 2021).
Shrestha et al. (2019) caution that consumers who deviate from platform norms—such as those who
use alternative search behaviors or access services from low-end devices—are often excluded from
targeted promotions or personalized experiences, despite being equally interested or qualified (Mehrabi
et al., 2021). This reflects a deeper structural bias: systems equate data richness and predictability with

www.scholink.org/ojs/index.php/ibes International Business & Economics Studies Vol. 8, No. 4, 2026
Published by SCHOLINK INC.
14
value, rendering underrepresented consumers invisible (Reed et al., 2025; Hermann, 2022).
5.1.4 Bias in Language and Messaging
In the context of large language models (LLMs), discriminatory patterns also emerge through linguistic
segmentation. Yilmaz and Ashqar (2025) show that AI-generated slogans varied significantly across
demographic groups. Women received disproportionately more empowerment-oriented messages,
while individuals with only high school education were most frequently targeted with financial
coaching or motivational themes (Yilmaz & Ashqar, 2025). While such messages may appear
well-intentioned, they encode benevolent biases—assumptions about neediness or inferiority that may
alienate rather than engage consumers.
Meanwhile, older consumers were offered minimal personalization, suggesting an underlying
assumption that this group is disengaged or less worthy of tailored content. These differentiated
narratives reinforce perceptions of who belongs in the marketplace and who does not, shaping brand
perception and self-image alike (Yilmaz & Ashqar, 2025).
5.1.5 Algorithmic Exclusion as Ethical and Strategic Risk
The cumulative effect of these practices is the erosion of consumer agency and the entrenchment of
algorithmic hierarchies. Consumers from marginalized communities may find themselves routinely
excluded from opportunities, deals, or experiences that others take for granted—not due to their
preferences or behaviors, but because they do not conform to profitable or learnable patterns
(Gonçalves et al., 2023; Deldjoo et al., 2024; Mehrabi et al., 2021). Over time, this leads to a stratified
digital marketplace in which access is unevenly distributed and structural inequality is subtly
maintained by automated systems (Eid et al., 2024; Mehrabi et al., 2021).
The danger lies not only in ethical and reputational harm, but in the strategic misalignment that arises
when systems designed to broaden reach inadvertently shrink it. As ethical consumerism gains
momentum, brands must recognize that exclusion—however indirect—carries real costs, both socially
and commercially (Su et al., 2023; Reed et al., 2025).
5.2 Perceived Fairness and Transparency
Perceived fairness is not only about the outcomes AI systems produce but also about how transparent,
explainable, and accountable those systems appear to the people affected by them. Across the literature
from Naz & Kashif to Nzama-Sithole, scholars consistently underscore that consumers' subjective
experiences of justice and visibility within AI-driven marketing systems are critical determinants of
trust and engagement. When consumers feel excluded, stereotyped, or unable to understand why they
received certain offers—or were left out—they tend to view the system as unfair, even if no explicit
discrimination occurred (Gonçalves et al., 2023; Hermann, 2022; Deldjoo et al., 2024; Su et al., 2023).
5.2.1 The Problem of Algorithmic Opacity
A central challenge is the black-box nature of many AI systems, especially those using deep learning or
proprietary models in personalization and targeting. Most consumers lack insight into how algorithms

www.scholink.org/ojs/index.php/ibes International Business & Economics Studies Vol. 8, No. 4, 2026
Published by SCHOLINK INC.
15
make decisions, what data they use, and whether those decisions are replicable or accountable (Naz &
Kashif, 2025; Mehrabi et al., 2021). As Reed et al. (2025) argue, this opacity becomes particularly
problematic when outcomes appear arbitrary—such as being shown an inferior product, missing a
promotion, or receiving less relevant recommendations compared to peers (Naz & Kashif, 2025).
When the logic behind AI-driven marketing is concealed, consumers begin to speculate about hidden
biases, particularly those linked to sensitive attributes like race, gender, or income. These suspicions
are often intensified when consumers observe discrepancies between their own experiences and those
of others, either directly or through social media (Eid et al., 2024; Deldjoo et al., 2024; Su et al., 2023).
As Su et al. (2023) point out, the absence of explanation mechanisms undermines procedural
fairness—the perception that the process behind outcomes is legitimate and reasonable. Without
transparency, even technically accurate or profitable systems can be perceived as manipulative or
unjust (Su et al., 2023).
5.2.2 Personalization Without Explanation
The use of personalization technologies further complicates perceptions of fairness. AI systems that
tailor content, pricing, and product recommendations may do so based on behavioral patterns,
geolocation, or inferred preferences—none of which are made explicit to the consumer (Gonçalves et
al., 2023; Reed et al., 2025; Mehrabi et al., 2021). When users receive highly specific content without
understanding how it was generated, they may feel profiled or categorized in reductive ways. This is
especially true when personalization reflects stereotypical or oversimplified assumptions, such as
associating women with empowerment slogans or divorced users with themes of recovery (Yilmaz &
Ashqar, 2025).
Even when outputs seem well-intentioned, the lack of transparency can create discomfort. As Yilmaz
and Ashqar (2025) observe, LLM-generated slogans vary linguistically across demographics in ways
that reflect implicit assumptions about users’ emotional and financial needs (Yilmaz & Ashqar, 2025).
Such experiences raise critical concerns about invisible influence, as consumers may sense that the
system is making unjustified or intrusive judgments about them—without any opportunity to contest or
clarify (Hermann, 2022; Quach et al., 2022).
5.2.3 Inaccessibility of Redress and Control
Another dimension of perceived unfairness stems from consumers’ limited ability to challenge or
influence AI outcomes. Most marketing platforms lack accessible tools for users to modify, correct, or
even understand their algorithmic profiles. This lack of recourse reinforces a power asymmetry
between firms and consumers, in which decisions about visibility, pricing, and segmentation are made
unilaterally by opaque systems (Deldjoo et al., 2024; Mehrabi et al., 2021; Su et al., 2023).
Dwivedi et al. (2021) emphasize that consumers expect not just relevance, but responsiveness. When
personalization misfires, repetition occurs, or patterns feel biased, the inability to adjust these
experiences fosters alienation and dissatisfaction (Hermann, 2022). This disempowerment erodes the

www.scholink.org/ojs/index.php/ibes International Business & Economics Studies Vol. 8, No. 4, 2026
Published by SCHOLINK INC.
16
sense that consumers are active participants in their marketing experiences, replacing agency with
automated control.
Moreover, Ameen et al. (2021) note that transparency failures are especially harmful in mobile or
real-time environments, where consumers have little time or capacity to reflect on their interactions. In
these contexts, algorithmic decisions are experienced as ambient and unchangeable, further distancing
consumers from understanding or influencing their commercial experiences (Reed et al., 2025).
5.2.4 The Role of Perception in Trust Erosion
The consequences of perceived unfairness are not confined to individual frustration—they have
systemic and reputational implications. As multiple authors observe, consumer suspicion—even if not
grounded in provable discrimination—can severely damage brand trust (Eid et al., 2024; Deldjoo et al.,
2024; Su et al., 2023). In an age of algorithmic awareness and social media scrutiny, consumers are
quick to detect and share perceived injustices, regardless of technical justification.
Transparency, therefore, is not simply a matter of regulatory compliance or ethical aspiration—it is a
strategic imperative. Brands that cannot explain how their AI systems work, or that fail to acknowledge
the concerns of affected users, risk alienating ethically conscious consumers and triggering negative
word-of-mouth (Mehrabi et al., 2021; Reed et al., 2025).
Table 2. Perceived Fairness and Transparency in AI Marketing
Dimension Description Examples synthesized from the reviewed
literature
Algorithmic Opacity Lack of explainability in
decision-making logic
Exclusion from offers without explanation
(Naz & Kashif, 2025, Mehrabi et al., 2021)
Personalization
Without Clarity
Tailored content that feels
stereotypical or intrusive
Slogans for women stressing empowerment
(Yilmaz & Ashqar, 2025)
Absence of Redress
Mechanisms
Consumers cannot modify or appeal
algorithmic decisions
No tools to correct personalization
(Hermann, 2022, Deldjoo et al., 2024)
Mistrust from
Perceived Injustice
Suspicion of bias due to observed
inconsistencies or opaque outputs
Peer comparison leads to fairness concerns
(Eid et al., 2024, Su et al., 2023)
5.3 Ethical Consumerism
As artificial intelligence (AI) becomes increasingly central to marketing operations, consumer trust has
emerged as both a core value and a strategic asset. Across the reviewed literature (Naz & Kashif, 2025;
Reed et al., 2025), scholars emphasize that trust is no longer based solely on product quality, brand
familiarity, or price competitiveness—it is increasingly tied to algorithmic fairness, transparency, and
perceived ethical conduct. The presence of algorithmic bias in marketing systems threatens not only

www.scholink.org/ojs/index.php/ibes International Business & Economics Studies Vol. 8, No. 4, 2026
Published by SCHOLINK INC.
17
individual consumer relationships but also broader brand legitimacy in an era where ethical
consumerism is on the rise.
5.3.1 The Fragility of Trust in Algorithmic Environments
Trust in AI-powered marketing is inherently fragile. As Su et al. (2023) explain, even marginal or
unintentional bias can trigger disproportionate damage to consumer trust, particularly when users
perceive outcomes as unfair or discriminatory (Su et al., 2023). Unlike traditional brand interactions,
AI-mediated experiences often lack human accountability, making the system’s intentions opaque and
the errors impersonal but more difficult to forgive.
This fragility is exacerbated by the asymmetry in trust dynamics: while fair systems must consistently
perform well to earn gradual consumer confidence, a single incident of algorithmic discrimination or
perceived exclusion can unravel years of trust-building (Gonçalves et al., 2023; Eid et al., 2024; Reed
et al., 2025). Once broken, trust is difficult to restore, especially if consumers sense a lack of
commitment to accountability or redress mechanisms.
5.3.2 AI Bias and Brand Reputation
Marketing systems that systematically exclude or misrepresent consumer groups—whether through
targeting, pricing, or language—send implicit signals about whose identities, behaviors, and values
matter. When consumers detect patterns of exclusion, even indirectly, they may attribute these
outcomes to corporate negligence or ethical failure (Naz & Kashif, 2025; Deldjoo et al., 2024; Mehrabi
et al., 2021). The reputational costs are particularly high when consumers take to social media or public
forums to voice concerns, prompting viral backlash and long-term damage to brand image (Mehrabi et
al., 2021).
Reed et al. (2025) argue that trust erosion due to AI bias does not occur in isolation—it spills into
broader public discourse, influencing not only the affected individual but also prospective customers,
stakeholders, and regulators (Naz & Kashif, 2025). In this environment, trust becomes not just a
personal sentiment but a collective judgment about a brand’s moral character.
5.3.3 The Rise of Ethical Consumerism
The intersection between AI fairness and trust is especially pronounced in the context of ethical
consumerism—a growing trend in which purchasing decisions are influenced by a brand’s social
responsibility, transparency, and ethical governance. Consumers, particularly among younger and
digitally literate demographics, increasingly demand that brands not only deliver value but also uphold
values (Hermann, 2022; Quach et al., 2022).
As Reed et al. (2025) and Yilmaz and Ashqar (2025) demonstrate, consumers are becoming more
sensitive to how AI systems reflect or reinforce societal norms and biases. When marketing content
perpetuates stereotypes—for example, associating women with empowerment slogans or older adults
with disengagement—ethically conscious users are more likely to reject personalization that feels
manipulative, patronizing, or disrespectful (Deldjoo et al., 2024; Quach et al., 2022).

www.scholink.org/ojs/index.php/ibes International Business & Economics Studies Vol. 8, No. 4, 2026
Published by SCHOLINK INC.
18
Moreover, these consumers expect ethical alignment not only in what a company says, but in how its
systems behave. The perceived failure to align algorithmic actions with declared brand values
undermines trust, turning once-loyal customers into vocal critics (Eid et al., 2024; Su et al., 2023).
5.3.4 Trust as a Strategic and Ethical Imperative
From a strategic perspective, maintaining consumer trust through ethical AI governance is no longer
optional—it is imperative for long-term competitiveness and resilience. Brands that proactively
implement fairness audits, bias mitigation strategies, and transparent communication protocols are
more likely to retain trust even when errors occur (Mehrabi et al., 2021; Reed et al., 2025).
Shrestha et al. (2019) and Dwivedi et al. (2021) emphasize that trust is shaped not only by system
performance but by user experience of fairness, respect, and dignity (Mehrabi et al., 2021; Hermann,
2022). Consumers want to feel seen, valued, and understood—not merely segmented and optimized.
When personalization is delivered with fairness and responsiveness, it strengthens emotional loyalty
and brand advocacy. When it fails, it can provoke disengagement, protest, or abandonment.
Yilmaz and Ashqar (2025) also caution that even seemingly subtle forms of bias—such as skewed
linguistic framing in LLM-generated content—can signal to consumers that their identity is being
flattened or misinterpreted (Yilmaz & Ashqar, 2025). In such cases, trust is not lost because the system
made a technical mistake, but because it made consumers feel misrecognized.
Figure 4. Concentric Layers of Consumer Trust in AI Marketing Systems
The diagram illustrates four interdependent components required to sustain consumer trust in
algorithmically driven marketing: algorithmic fairness, ethical alignment, transparency and
explainability, and user respect and responsiveness. The innermost core—algorithmic fairness—serves
as the foundation upon which other layers build. Failure in inner layers leads to instability in the outer
layers. Synthesized from Naz and Kashif (2025) and Reed et al. (2025).

www.scholink.org/ojs/index.php/ibes International Business & Economics Studies Vol. 8, No. 4, 2026
Published by SCHOLINK INC.
19
6. Implications for Brand Reputation
6.1 Algorithmic Harm and Brand Backlash
As AI systems become the engine behind personalization, targeting, pricing, and content generation in
marketing, the risks of algorithmic harm—and their reputational consequences—have grown markedly.
Across the reviewed literature (Naz & Kashif, 2025; Reed et al., 2025), scholars emphasize that harms
stemming from biased, opaque, or exclusionary AI systems are not only technological failures, but are
increasingly perceived as ethical lapses and governance breakdowns. When AI marketing tools
generate discriminatory outputs, exclude marginalized users, or stereotype consumer groups, these
outcomes often trigger public backlash and brand damage—even if they are unintended.
6.1.1 From Technical Failure to Ethical Accountability
Historically, algorithmic errors may have been framed as isolated or fixable bugs. However, today’s
stakeholders—including consumers, regulators, and civil society—expect companies to anticipate and
mitigate bias, particularly in consumer-facing technologies (Naz & Kashif, 2025; Gonçalves et al.,
2023; Su et al., 2023). As a result, even unintentional harms—such as showing fewer job ads to women
or offering higher prices to users from minority zip codes—are no longer seen as benign mistakes.
Instead, they are interpreted as signs of negligence, poor oversight, or a lack of ethical design foresight
(Eid et al., 2024; Hermann, 2022; Reed et al., 2025).
Reed et al. (2025) refer to this shift as a transformation in public framing: when algorithmic systems
produce biased outcomes, the narrative quickly moves from ‘flawed code’ to ‘flawed company values’
(Naz & Kashif, 2025). Similarly, Reed et al. (2025) highlight how consumers increasingly view
algorithmic discrimination as a failure of brand responsibility, regardless of whether human intent was
involved (Gonçalves et al., 2023).
Su et al. (2023) describe a reputational paradox: AI systems may outperform human decision-making
in some respects (e.g., speed, efficiency), yet still generate disparate impact that offends ethical norms
and alienates consumers—producing backlash that outweighs performance benefits (Su et al., 2023).
6.1.2 Real-World Examples of Algorithmic Harm
The literature offers numerous real and illustrative examples where marketing AI systems caused harm:
 Dynamic pricing algorithms have charged higher prices to users from low-income or
minority-dense areas, reinforcing economic disparities and prompting accusations of digital redlining
(Naz & Kashif, 2025; Deldjoo et al., 2024).
 Ad targeting systems have disproportionately shown financial products or job opportunities to
certain racial or gender groups, echoing long-standing societal inequalities and leading to media
condemnation (Gonçalves et al., 2023; Mehrabi et al., 2021).
 Content recommendation engines have marginalized consumers who fall outside dominant
behavioral profiles, limiting their access to information or promotions and reinforcing invisibility (Eid
et al., 2024; Mehrabi et al., 2021).

www.scholink.org/ojs/index.php/ibes International Business & Economics Studies Vol. 8, No. 4, 2026
Published by SCHOLINK INC.
20
 LLM-generated marketing language has shown subtle but systematic patterns of bias—for
example, portraying divorced individuals as needing to ‘rebuild’ their lives, or tailoring empowerment
slogans only to women (Yilmaz & Ashqar, 2025).
These algorithmic decisions, though often produced without explicit intent, send cultural and ethical
signals that shape public interpretation. They influence not only individual consumer experiences but
also how the brand is perceived in terms of inclusivity, justice, and integrity.
6.1.3 Perceived Complicity and Moral Framing
One of the key themes is that brands are increasingly held morally accountable for algorithmic outputs.
As the literature suggests that consumers may attribute algorithmic harms to the organization
responsible for deploying the system (Eid et al., 2024). In this context, even subtle or unnoticed harms
can damage reputation when they resonate with broader public anxieties about surveillance, exclusion,
or digital manipulation.
Reed et al. (2025) note that the threshold for reputational backlash is lowering: consumers are not only
more aware of algorithmic bias but also more willing to mobilize against brands they perceive as
unethical (Deldjoo et al., 2024). This is particularly evident in highly visible sectors like finance,
healthcare, education, and employment, where biased AI systems can affect perceptions of equal
opportunity and access.
6.1.4 Stakeholder Fallout
The harm from biased algorithms is not limited to consumers. Brands also face scrutiny from:
 Media, which frame these failures as systemic ethical breakdowns rather than isolated
incidents (Naz & Kashif, 2025; Eid et al., 2024);
 Investors, who increasingly demand ESG-aligned risk mitigation and governance structures
(Su et al., 2023);
 Regulators, who may launch investigations or impose penalties if AI-driven harm violates
anti-discrimination or data ethics laws (Hermann, 2022; Mehrabi et al., 2021).
Yilmaz and Ashqar (2025) further warn that reputational harm extends into brand voice and narrative:
when AI-generated messages embody demographic stereotypes, they not only offend but reveal a lack
of ethical oversight in content strategy (Yilmaz & Ashqar, 2025).
6.2 The Amplification Effect
In the digital age, algorithmic bias does not remain hidden within internal systems—it often surfaces in
public, and spreads rapidly via social media. The literature highlights how even subtle or technical
forms of bias in AI-driven marketing can trigger intense public scrutiny and reputational crises,
particularly when exposed or interpreted in viral digital spaces. Platforms like Twitter, TikTok, and
Reddit serve as both amplifiers and adjudicators, transforming isolated algorithmic failures into widely
shared narratives of brand misconduct.

www.scholink.org/ojs/index.php/ibes International Business & Economics Studies Vol. 8, No. 4, 2026
Published by SCHOLINK INC.
21
6.2.1 The Speed and Virality of Algorithmic Backlash
One of the defining features of AI-related PR crises is the velocity of exposure. A single
screenshot—such as a discriminatory ad placement, a price discrepancy based on ZIP code, or a
stereotyped marketing slogan—can be captured and disseminated by a consumer in seconds (Eid et al.,
2024; Deldjoo et al., 2024). As Ameen et al. (2021) and Reed et al. (2025) note, these posts often carry
emotional weight, attracting high engagement, and invoking community outrage, especially when they
align with concerns around discrimination, surveillance, or fairness (Reed et al., 2025; Gonçalves et al.,
2023).
Importantly, consumers do not need to prove intentionality to generate backlash; the appearance of
harm is often sufficient. Su et al. (2023) describe this dynamic as a ‘reputational tinderbox,’ where
opacity, silence, or deflection on the part of the brand can accelerate mistrust and outrage (Su et al.,
2023).
6.2.2 From Personal Experience to Public Narrative
What begins as an individual’s negative experience often quickly evolves into a collective indictment
of the brand, especially when others report similar treatment or recognize broader patterns. As Dwivedi
et al. (2021) emphasize, consumers now expect brand transparency not only in product quality but also
in how algorithms govern their interactions (Hermann, 2022). When that transparency is lacking, social
media users fill in the blanks—often framing the brand as careless, untrustworthy, or exploitative
(Mehrabi et al., 2021).
Yilmaz and Ashqar (2025) provide a concrete example through their study of AI-generated slogans,
which revealed how marketing content varied by marital status, gender, and education. While the intent
may have been personalization, consumers perceived such differences as stereotyping and profiling,
especially when shared in side-by-side comparisons on social media (Yilmaz & Ashqar, 2025). These
interpretations gain traction not just because they are plausible, but because they resonate with broader
societal concerns about fairness and algorithmic manipulation (Naz & Kashif, 2025; Mehrabi et al.,
2021).
6.2.3 The Failure of Traditional PR Responses
Traditional public relations responses—such as issuing a formal statement, offering apologies, or
claiming the incident was unintentional—often fail in AI-related crises. This is partly because
algorithmic harm is framed not as a single bad act, but as evidence of systemic irresponsibility (Eid et
al., 2024; Deldjoo et al., 2024). When brands fail to disclose how algorithms work, or why certain
outcomes occurred, they reinforce the perception that they are hiding behind technology, rather than
taking accountability.
Moreover, as Reed et al. (2025) explain, a lack of technical literacy among corporate communication
teams often leads to vague, overly generalized responses that do little to rebuild trust (Gonçalves et al.,
2023). In contrast, brands that provide specific, technical explanations—and demonstrate willingness to

www.scholink.org/ojs/index.php/ibes International Business & Economics Studies Vol. 8, No. 4, 2026
Published by SCHOLINK INC.
22
audit, change, or suspend biased systems—are more likely to be perceived as trustworthy and
responsive (Mehrabi et al., 2021; Su et al., 2023).
6.2.4 Compounded Risk Through Influencer and Activist Amplification
Social media does not just expose bias—it magnifies it through influencer commentary, activist
framing, and journalistic inquiry. Influencers and watchdog groups often adopt an advocacy lens, using
algorithmic failures to highlight injustice or demand broader accountability (Eid et al., 2024; Deldjoo et
al., 2024). In some cases, this leads to trending hashtags, organized boycotts, or media coverage that
solidifies the crisis in the public imagination (Reed et al., 2025).
These actors also reshape the narrative structure of the crisis. Instead of viewing algorithmic bias as an
IT issue, they frame it as evidence of cultural negligence, systemic prejudice, or ethical
blindness—narratives that resonate far beyond the technical domain (Gonçalves et al., 2023; Quach et
al., 2022).
Figure 5. The Viral Outrage Chain in Algorithmic Marketing Crises
This infographic illustrates the typical escalation path of reputational damage following a biased AI
output in marketing. It begins with a discriminatory or unfair outcome and moves through consumer
exposure, social media amplification, influencer and activist engagement, media coverage, and
ultimately, brand response and long-term public perception. The figure highlights the speed and
interconnected nature of digital backlash. (Adapted from insights in Naz & Kashif, 2025;Reed et al.,
2025)
6.3 Corporate Social Responsibility (CSR)
In the context of AI-driven marketing, corporate social responsibility (CSR) is no longer a symbolic
gesture or peripheral function—it is now a strategic necessity for protecting long-term brand equity. As
marketing algorithms become more autonomous and impactful, consumers and stakeholders expect
companies to adopt proactive governance measures that ensure fairness, transparency, and
accountability. The literature (Naz & Kashif, 2025–Reed et al., 2025) affirms that ethical AI design and
responsible algorithm management are becoming essential components of both CSR frameworks and
brand value propositions.

www.scholink.org/ojs/index.php/ibes International Business & Economics Studies Vol. 8, No. 4, 2026
Published by SCHOLINK INC.
23
6.3.1 From Compliance to Proactive Governance
Traditionally, CSR was associated with philanthropic activities or environmental sustainability.
However, in the digital age, CSR has expanded to encompass algorithmic ethics, especially as AI tools
influence public perception, access to services, and consumer experiences (Gonçalves et al., 2023;
Deldjoo et al., 2024; Su et al., 2023). This shift requires companies to move beyond basic legal
compliance and instead embrace proactive, self-regulatory practices that align marketing technologies
with broader societal expectations.
As Su et al. (2023) emphasize, CSR in AI contexts must include bias audits, diverse training data, and
fairness-aware algorithmic design—not simply because these steps reduce harm, but because they
signal to consumers and stakeholders that the company takes ethical responsibility seriously (Su et al.,
2023). This is especially critical in sectors like finance, healthcare, education, and employment, where
the consequences of algorithmic bias can be particularly damaging to public trust and equity (Deldjoo
et al., 2024; Mehrabi et al., 2021).
6.3.2 Transparency and Explainability as CSR Pillars
Transparency and explainability have emerged as non-negotiable components of algorithmic CSR.
Brands that fail to explain how their AI systems operate or how consumer data is used risk being
viewed as evasive or unethical—even if the outputs themselves appear harmless (Eid et al., 2024;
Hermann, 2022; Mehrabi et al., 2021). Conversely, those that offer clear documentation, user-facing
disclosures, and meaningful channels for contesting algorithmic decisions are more likely to be trusted
and respected (Reed et al., 2025; Mehrabi et al., 2021).
Dwivedi et al. (2021) argue that modern CSR involves ‘techno-moral stewardship,’ where
organizations take public responsibility for both intentional and emergent outcomes of their AI systems
(Hermann, 2022). This includes anticipating potential biases, disclosing algorithmic limitations, and
involving external stakeholders—such as ethicists, regulators, and affected communities—in
governance discussions (Mehrabi et al., 2021; Reed et al., 2025).
6.3.3 The Branding Value of Ethical AI
Ethical AI practices are increasingly recognized not only as a risk management strategy but also as a
differentiator for brand positioning. As consumer expectations evolve, brands that can demonstrate
genuine commitment to fairness, inclusion, and responsible innovation are better positioned to cultivate
emotional loyalty, advocacy, and reputational resilience (Naz & Kashif, 2025; Deldjoo et al., 2024;
Quach et al., 2022).
Ameen et al. (2021) note that digital-native and younger consumers—particularly Gen Z and
Millennials—actively evaluate brands based on ethical alignment and digital responsibility (Reed et al.,
2025). These consumers are more likely to reward companies that engage in algorithmic transparency,
confront bias openly, and commit to inclusive design. Conversely, brands that ignore these
responsibilities risk being labeled as exploitative, outdated, or socially disengaged (Eid et al., 2024;

www.scholink.org/ojs/index.php/ibes International Business & Economics Studies Vol. 8, No. 4, 2026
Published by SCHOLINK INC.
24
Quach et al., 2022; Reed et al., 2025).
Moreover, algorithmic CSR has cross-stakeholder benefits. Investors concerned with ESG
(Environmental, Social, and Governance) metrics increasingly view AI governance as a marker of
long-term sustainability and reputational maturity (Mehrabi et al., 2021; Su et al., 2023). Regulatory
bodies are also placing greater emphasis on algorithmic accountability, making ethical readiness a
protective buffer against compliance failures (Hermann, 2022; Mehrabi et al., 2021).
6.3.4 Ethical Infrastructure as a Strategic Asset
Long-term brand equity depends not just on what a company builds, but how it builds it. The literature
calls for brands to create institutional infrastructure for AI ethics, such as:
 Internal ethics boards to review high-risk AI marketing strategies (Deldjoo et al., 2024;
Mehrabi et al., 2021);
 Bias testing protocols during model training and deployment (Gonçalves et al., 2023; Su et al.,
2023);
 Cross-functional teams that combine technical, legal, and social expertise (Reed et al., 2025;
Reed et al., 2025);
 Public transparency reports detailing system performance, fairness interventions, and user
complaints (Eid et al., 2024; Mehrabi et al., 2021).
Yilmaz and Ashqar (2025) suggest that such infrastructure sends a strong message: the brand views
algorithmic fairness not as a constraint, but as a core element of quality and integrity (Yilmaz & Ashqar,
2025). In this framing, CSR becomes not a reputational shield but a competitive advantage—enabling
companies to build trust, attract conscientious consumers, and withstand ethical scrutiny.
In a digital economy shaped by AI, ethical accountability is brand equity. Companies that
institutionalize fairness, respect, and transparency into their AI marketing practices not only prevent
reputational harm but actively cultivate credibility, distinctiveness, and long-term stakeholder loyalty.
As the boundary between algorithm and brand continues to blur, CSR must evolve into a discipline of
technological integrity.
7. Mitigation Strategies and Ethical Governance
7.1 Technical Interventions
The mitigation of algorithmic bias in marketing systems requires more than awareness—it demands
concrete, systematic technical interventions. Fairness must be integrated at multiple stages of the model
development pipeline, from data preprocessing to post-deployment evaluation. These interventions help
reduce disparities across demographic groups and ensure that AI-powered marketing systems align
with ethical expectations and consumer rights (Eid et al., 2024).

www.scholink.org/ojs/index.php/ibes International Business & Economics Studies Vol. 8, No. 4, 2026
Published by SCHOLINK INC.
25
7.1.1 Bias-Aware Data Engineering
Many biases in AI marketing systems originate from skewed, incomplete, or historically prejudiced
datasets. A common issue is the underrepresentation of marginalized consumer groups, which causes
models to generalize poorly for those populations (Naz & Kashif, 2025; Hermann, 2022; Deldjoo et al.,
2024). To address this, scholars advocate for rigorous dataset audits, including:
 Distributional checks across gender, race, geography, and socioeconomic status;
 Use of synthetic oversampling to correct underrepresented classes (Eid et al., 2024; Mehrabi et
al., 2021);
 Annotation protocols that incorporate fairness goals, not just accuracy (Mehrabi et al., 2021).
Reed et al. (2025) emphasize that addressing data bias upstream is essential, as no amount of post-hoc
fairness tweaking can fully resolve entrenched data inequities (Deldjoo et al., 2024).
7.1.2 Fairness-Constrained Machine Learning
Once the data is prepared, model selection and training offer opportunities for encoding fairness.
Several scholars propose embedding fairness constraints directly into model objectives, such as:
 Demographic parity: Ensuring equal positive prediction rates across groups;
 Equalized odds: Matching true positive and false positive rates between subgroups (Gonçalves
et al., 2023; Hermann, 2022);
 Minimized disparate impact: Reducing the likelihood that decisions disproportionately
disadvantage protected attributes (Eid et al., 2024; Su et al., 2023).
These fairness-aware algorithms often require multi-objective optimization where accuracy is balanced
against fairness thresholds. While this may reduce raw performance metrics slightly, the trade-off is
considered acceptable—particularly in high-stakes domains like pricing, credit, and hiring (Naz &
Kashif, 2025; Mehrabi et al., 2021; Mehrabi et al., 2021).
7.1.3 Explainable AI (XAI)
A recurrent concern in AI-driven marketing is the opacity of decision-making, especially in deep
learning systems. Explainable AI (XAI) frameworks—such as SHAP (SHapley Additive exPlanations)
and LIME (Local Interpretable Model-Agnostic Explanations)—are critical tools for:
 Tracing influential features in individual predictions;
 Identifying proxy variables that may serve as surrogates for protected attributes (e.g., ZIP code
for race);
 Democratizing model insights for non-technical stakeholders (Reed et al., 2025; Quach et al.,
2022).
XAI not only improves internal oversight but also enables external transparency, allowing companies
to explain personalization or pricing decisions to consumers and regulators (Deldjoo et al., 2024; Su et
al., 2023).

www.scholink.org/ojs/index.php/ibes International Business & Economics Studies Vol. 8, No. 4, 2026
Published by SCHOLINK INC.
26
7.1.4 Post-Hoc Bias Audits and Disaggregated Evaluation
Bias often emerges only after models are deployed in real-world settings. Therefore, post-hoc auditing
is necessary to detect unintended disparities. Authors recommend:
 Subgroup performance analysis, where accuracy, recall, and precision are compared across
demographic groups (Gonçalves et al., 2023; Mehrabi et al., 2021);
 Use of statistical tests such as the Kolmogorov–Smirnov distance to detect distributional
skews (Yilmaz & Ashqar, 2025);
 Deployment of bias dashboards to monitor real-time system outputs and disparities (Eid et al.,
2024; Mehrabi et al., 2021).
These evaluations should become part of the continuous deployment pipeline, allowing for rapid
intervention when bias metrics cross critical thresholds (Hermann, 2022; Reed et al., 2025).
7.1.5 Adaptive and Feedback-Driven Learning
Several sources stress the importance of building systems that learn from feedback and correct over
time. Static AI models can entrench bias if they fail to adapt to evolving consumer behavior and social
expectations (Reed et al., 2025; Deldjoo et al., 2024). Proposed mechanisms include:
 Online learning models that update based on new data;
 User flagging tools that allow consumers to contest outcomes (Mehrabi et al., 2021);
 Feedback loops that trigger re-weighting of training samples or realignment of model
priorities (Mehrabi et al., 2021; Reed et al., 2025).
This adaptability is especially crucial in domains like targeted advertising, where consumer values,
identities, and contexts are in constant flux.
7.2 Organizational Practices
While technical interventions are essential for mitigating algorithmic bias, they must be supported by
robust organizational practices that institutionalize fairness and accountability across the development
and deployment lifecycle. Effective bias mitigation in AI-driven marketing depends on the ability of
organizations to embed ethical governance into their internal structures, culture, and workflows.
Without this alignment, technical solutions risk becoming cosmetic, failing to address deeper power
imbalances, value conflicts, or systemic oversight gaps (Awan, 2023; Danks, 2017).
7.2.1 Building a Culture of Ethics-by-Design
A recurring theme across the literature is the need for an ethics-by-design approach, which integrates
fairness and transparency from the earliest stages of system conception (Gonçalves et al., 2023;
Deldjoo et al., 2024; Mehrabi et al., 2021). Rather than treating ethics as an afterthought or compliance
requirement, organizations must make it a foundational design principle, guiding decisions about data
collection, target metrics, and user segmentation.
This cultural shift requires top-down commitment from leadership and bottom-up participation from
employees across disciplines—including marketing strategists, data scientists, UX designers, and legal

www.scholink.org/ojs/index.php/ibes International Business & Economics Studies Vol. 8, No. 4, 2026
Published by SCHOLINK INC.
27
advisors (Hermann, 2022; Su et al., 2023). It also calls for a clear articulation of brand values in
relation to AI use, ensuring that every algorithmic decision reflects the organization's social
commitments (Reed et al., 2025; Mehrabi et al., 2021).
7.2.2 Multidisciplinary AI Ethics Committees
To support ethical decision-making, many scholars advocate the establishment of AI ethics committees
or review boards within firms. These bodies bring together cross-functional expertise—including
technical, legal, psychological, sociological, and commercial perspectives—to evaluate algorithmic risk
(Deldjoo et al., 2024; Mehrabi et al., 2021; Reed et al., 2025). Their responsibilities include:
 Reviewing high-risk AI projects before deployment;
 Assessing the social impact of personalization or segmentation algorithms;
 Recommending design revisions, fairness audits, or consumer transparency initiatives
(Gonçalves et al., 2023; Mehrabi et al., 2021).
Such committees also serve as internal accountability mechanisms, reducing reliance on ad hoc ethical
judgments by individual engineers or product managers.
7.2.3 Institutionalizing Fairness Protocols
To avoid inconsistent application of ethical principles, organizations should implement standardized
fairness protocols. These include:
 Bias testing procedures as part of model validation (Eid et al., 2024; Mehrabi et al., 2021);
 Inclusion of fairness KPIs in performance dashboards and OKRs (Hermann, 2022; Mehrabi et
al., 2021);
 Use of checklists and scorecards to document decisions about sensitive attributes, user groups,
and exclusions (Naz & Kashif, 2025; Quach et al., 2022).
Formalizing these procedures helps normalize fairness as a core concern, not an optional feature.
7.2.4 Training and Capacity Building
Organizational mitigation also requires sustained investment in training and education. Many
employees involved in marketing AI systems—especially in creative, managerial, or operational
roles—may lack the technical vocabulary or conceptual grounding to identify bias or respond
effectively (Eid et al., 2024; Deldjoo et al., 2024). Suggested practices include:
 Workshops on algorithmic bias and inclusive design;
 Scenario-based training modules that simulate real-world ethical dilemmas (Mehrabi et al.,
2021; Su et al., 2023);
 Integration of fairness-related learning objectives into onboarding and performance reviews
(Hermann, 2022; Mehrabi et al., 2021).
When staff across departments share a common language of fairness, organizational response to ethical
risks becomes more coherent and proactive.

www.scholink.org/ojs/index.php/ibes International Business & Economics Studies Vol. 8, No. 4, 2026
Published by SCHOLINK INC.
28
7.2.5 Co-Design and Participatory Governance
Another key strategy is involving external stakeholders and consumers in the design and monitoring of
AI systems. Dwivedi et al. (2021) and Yilmaz & Ashqar (2025) emphasize the importance of user
feedback loops, focus groups, and participatory evaluations, especially for systems that personalize
content or pricing (Hermann, 2022; Quach et al., 2022). This approach treats users not merely as data
points, but as co-constructors of algorithmic experience.
Such participation builds social legitimacy and reduces the likelihood of backlash or disengagement
due to opaque or exclusionary outcomes (Reed et al., 2025; Deldjoo et al., 2024).
7.2.6 Internal Communication and Accountability Channels
Lastly, fairness must be supported by internal transparency. Organizations should maintain
documentation systems that track:
 Model development decisions;
 Changes made in response to fairness reviews;
 Rationales for excluding or including sensitive attributes (Eid et al., 2024; Mehrabi et al.,
2021).
Additionally, internal whistleblower protections and anonymous reporting mechanisms can encourage
ethical concern without fear of reprisal (Gonçalves et al., 2023; Su et al., 2023).
7.3 Policy and Regulation
As algorithmic decision-making becomes embedded in marketing infrastructures, the role of regulation
in guiding fairness, transparency, and accountability has grown more urgent. While marketing
technologies have historically operated in lightly regulated environments, the widespread use of AI for
personalization, segmentation, and predictive profiling introduces new risks—particularly around
discrimination, privacy, and manipulation (Elliott, 2019). Scholars argue that a multi-layered
governance framework, combining public regulation, industry standards, and organizational
self-governance, is essential to mitigating algorithmic bias in marketing systems (Awan, 2023; Danks,
2017).
7.3.1 The European Union’s AI Act
The European Union’s Artificial Intelligence Act (AI Act) represents the most comprehensive
regulatory response to date. Although marketing systems are not explicitly categorized as ‘high-risk’
under the current draft, they may fall under ‘limited risk’ or ‘transparency obligations’—particularly
when they affect consumer autonomy or access to services (Gonçalves et al., 2023; Eid et al., 2024;
Deldjoo et al., 2024). The AI Act mandates:
 Transparency obligations for systems that interact with humans, such as chatbots and
recommender systems;
 Risk-based categorization, requiring greater scrutiny for applications with societal impact;
 Human-in-the-loop safeguards and documentation for traceability and accountability (Deldjoo

www.scholink.org/ojs/index.php/ibes International Business & Economics Studies Vol. 8, No. 4, 2026
Published by SCHOLINK INC.
29
et al., 2024; Mehrabi et al., 2021; Su et al., 2023).
Scholars argue that as AI marketing practices become more consequential—e.g., influencing credit
offers, job ads, or political messaging—regulators may expand the scope to include these systems as
‘systemic risks,’ requiring full impact assessments and third-party audits (Eid et al., 2024; Hermann,
2022).
7.3.2 U.S. Federal Trade Commission (FTC) Guidelines
In the United States, regulatory efforts are more fragmented but increasingly active. The Federal Trade
Commission (FTC) has issued guidance warning that algorithmic discrimination violates consumer
protection laws, especially when it affects pricing, targeting, or decision-making in areas such as
housing or credit (Naz & Kashif, 2025; Mehrabi et al., 2021). The FTC’s approach emphasizes:
 Truthful disclosures about how consumer data is used;
 Fairness in automated decision-making;
 Enforcement actions against companies that fail to mitigate known algorithmic harms (Eid et
al., 2024; Mehrabi et al., 2021; Reed et al., 2025).
While not as prescriptive as the EU model, FTC guidance reflects a broadening interpretation of unfair
and deceptive practices to include opaque or discriminatory algorithms (Deldjoo et al., 2024).
7.3.3 Self-Regulation and Ethical Certification
In the absence of binding global standards, many scholars advocate for voluntary self-regulatory
frameworks within the industry. These may include:
 Bias scorecards and algorithmic transparency reports published by firms (Reed et al., 2025;
Mehrabi et al., 2021);
 Ethical AI labels or certifications similar to nutrition labels, indicating whether systems meet
defined fairness benchmarks (Gonçalves et al., 2023; Deldjoo et al., 2024);
 Participation in industry consortia that establish codes of conduct for ethical personalization,
such as the Partnership on AI or IEEE initiatives (Hermann, 2022; Mehrabi et al., 2021).
Although voluntary, these mechanisms help fill regulatory gaps and offer consumers signals of
trustworthiness and compliance.
7.3.4 Preemptive Compliance and Legal Preparedness
Organizations are increasingly advised to engage in preemptive compliance, recognizing that
regulatory environments are evolving. This includes:
 Algorithmic impact assessments (AIAs) before deployment (Eid et al., 2024; Su et al., 2023);
 Documentation of model logic and fairness interventions;
 Establishing legal-technical collaboration teams to interpret and apply emerging policy
frameworks (Deldjoo et al., 2024; Reed et al., 2025).
Yilmaz and Ashqar (2025) highlight that brands investing in ethical foresight and compliance readiness
not only avoid regulatory penalties but also gain reputational advantages and investor confidence

www.scholink.org/ojs/index.php/ibes International Business & Economics Studies Vol. 8, No. 4, 2026
Published by SCHOLINK INC.
30
(Yilmaz & Ashqar, 2025).
7.3.5 Divergence and Convergence
Regulatory approaches differ widely across regions. The EU’s emphasis on prevention and systemic
governance contrasts with the U.S. model of enforcement and litigation. Meanwhile, countries like
Canada, Singapore, and Australia are developing hybrid models that blend risk-based assessments with
voluntary guidance (Hermann, 2022; Mehrabi et al., 2021). This divergence presents challenges for
global brands, who must navigate inconsistent expectations, enforcement mechanisms, and definitional
standards of fairness (Mehrabi et al., 2021; Reed et al., 2025).
Still, there is growing convergence on core principles: explainability, non-discrimination, human
oversight, and accountability. Scholars call for international cooperation and regulatory harmonization,
especially as marketing platforms operate across borders and impact transnational audiences (Eid et al.,
2024; Deldjoo et al., 2024).
8. Research Gaps and Future Directions
Despite a marked increase in scholarly and applied attention to algorithmic bias in AI-driven marketing
systems, significant gaps remain that hinder both theoretical advancement and practical implementation.
These gaps span methodological limitations, demographic and cultural blind spots, technological
complexities, and legal ambiguities. A more nuanced, interdisciplinary, and globally inclusive research
agenda is urgently needed.
8.1 Geographic and Cultural Limitations
Much of the existing literature is disproportionately centered on Western markets, particularly the
United States and Western Europe. As Deldjoo et al., 2024 highlights, algorithmic fairness and
consumer perceptions of bias vary significantly across cultures due to differences in societal values,
regulatory expectations, and moral frameworks. For instance, collectivist cultures prioritize social
harmony and may evaluate fairness based on group-level outcomes, while individualist societies are
more sensitive to violations of personal autonomy. Yet, few studies have systematically compared how
algorithmic bias is interpreted, tolerated, or resisted across these cultural lines (Deldjoo et al., 2024).
Future studies should conduct cross-cultural experiments to explore how demographic fairness,
procedural transparency, and trust are culturally constructed. The development of localized fairness
frameworks is critical for global brands aiming to deploy AI ethically and effectively across
jurisdictions.
8.2 Organizational Scope and Sector Diversity
The current literature also overrepresents large, tech-savvy corporations and omits small and medium
enterprises (SMEs) that increasingly adopt AI-driven marketing tools but lack robust governance
frameworks (Akter et al., 2023; Naz & Kashif, 2025). These firms may deploy third-party AI systems

www.scholink.org/ojs/index.php/ibes International Business & Economics Studies Vol. 8, No. 4, 2026
Published by SCHOLINK INC.
31
without sufficient understanding of embedded risks, raising questions about outsourced bias and
accountability dilution.
Research must explore how SMEs can operationalize fairness principles despite resource constraints.
Comparative studies are needed to assess how organizational size, sector, and digital maturity affect
bias detection and mitigation capabilities.
8.3 Temporal Gaps and Longitudinal Blind Spots
As Akter et al. (2023) point out, most studies evaluate fairness interventions at a single point in time,
without tracking how biases evolve or persist over extended periods. The lack of longitudinal data
makes it difficult to determine whether mitigation strategies—such as fairness-aware ML or algorithm
audits—produce durable changes in outcomes, trust, or brand perception.
Long-term studies are also needed to assess feedback loops where biased AI decisions influence
consumer behavior, which in turn reinforces training data disparities—creating self-reinforcing bias
cycles.
8.4 Data-Centric and Pipeline Bias Blindness
Hermann (2022) reveals a critical lack of research on bias embedded in data collection and labeling
pipelines, especially in commercial marketing datasets. While algorithmic outputs are increasingly
scrutinized, representational harm often begins upstream, when datasets fail to include marginalized
voices or encode biased feature engineering logic. Current audit tools and fairness metrics are often
post hoc and reactive, missing the structural roots of bias (Awan et al., 2023).
Future work must prioritize data governance protocols, particularly in third-party data acquisition,
annotation practices, and the reuse of legacy datasets that were never audited for fairness.
8.5 Legal and Regulatory Asymmetries
As discussed in Wang et al., (2023) the legal response to algorithmic bias remains fragmented across
jurisdictions, with the EU AI Act emphasizing ex ante risk categorization and the U.S. favoring post
hoc enforcement. This creates a patchwork regulatory environment that complicates global compliance
for brands operating in multiple regions (Benlian et al., 2022).
Research should examine the interoperability of fairness standards and the potential for unified
governance tools, such as standardized impact assessments and transparency benchmarks. The
intersection of soft law (e.g., OECD guidelines) and hard law (e.g., GDPR, FTC rules) deserves deeper
investigation (Brynjolfsson, Rock, & Syverson, 2018).
8.6 Explainability and Human-AI Collaboration
Reed et al., highlights the trade-off between model performance and explainability, a dilemma that has
not been adequately explored in consumer-facing applications. While explainable AI (XAI) techniques
like SHAP or LIME exist, there is limited research on how these explanations affect consumer
understanding, trust, and behavior in real-world marketing contexts.
Moreover, the literature lacks clarity on best practices for human-in-the-loop systems, which are often

www.scholink.org/ojs/index.php/ibes International Business & Economics Studies Vol. 8, No. 4, 2026
Published by SCHOLINK INC.
32
recommended but rarely studied in operational settings. How much human oversight is optimal? At
what stages should humans intervene? These are unresolved questions with direct implications for
accountability and bias governance (Belk, Belanche, & Flavian, 2023).
8.7 Behavioral and Moral Attribution Gaps
Findings from Gonçalves et al., and Mehrabi et al., indicate that consumers evaluate algorithmic
decisions differently from human ones, especially in terms of moral responsibility and blame
attribution. However, current models of consumer trust and satisfaction do not fully account for the
psychological dimensions of algorithmic interactions, such as perceived agency, intentionality, and
justice (Gonçalves et al., 2023; Eid et al., 2024; Deldjoo et al., 2024; Lee, 2020).
Further empirical research is needed to understand how algorithmic harms affect consumer loyalty,
forgiveness, and activism, and what types of redress (e.g., apologies, overrides, compensation) are most
effective post-harm.
8.8 Intersectionality and Demographic Complexity
Most fairness evaluations test bias across individual attributes like gender or income, but rarely
consider intersectional identities such as Black women, elderly immigrants, or disabled LGBTQ+
individuals. As Eid et al. notes, the lack of intersectional bias detection tools severely limits our ability
to diagnose and address complex inequities in AI systems.
There is a pressing need for fairness-aware models that accommodate multi-dimensional demographic
inputs, and for benchmarks that reflect real-world consumer diversity.
8.9 Toward an Interdisciplinary Research Agenda
In light of these gaps, Akter et al. (2023) and Su et al. (2023) advocate for a shift toward
socio-technical and interdisciplinary research that fuses AI engineering, marketing ethics, legal
scholarship, consumer psychology, and data governance. Only through such an integrated lens can the
field develop scalable, fair, and context-aware AI marketing systems.
9. Synthesis of Findings
The review of scholarly and industry literature highlights that algorithmic bias in marketing systems is
a multi-dimensional phenomenon rooted in the entire lifecycle of AI. First, evidence shows that bias
emerges from data, models, and deployment contexts, where historical inequalities, profit-driven
optimization, and self-reinforcing feedback loops converge to disadvantage certain consumer groups.
These mechanisms lead to specific patterns of representation bias, measurement bias, and evaluation
bias, each of which reduces visibility and access for marginalized users.
Second, the findings reveal significant implications for consumer equity. Biased algorithms not only
replicate but also intensify structural exclusion, dynamic pricing discrimination, and stereotyping in
personalized communication. Consumers are frequently left without transparency or meaningful
redress, which undermines perceptions of fairness and erodes trust. The review also underscores that

www.scholink.org/ojs/index.php/ibes International Business & Economics Studies Vol. 8, No. 4, 2026
Published by SCHOLINK INC.
33
consumer experiences of injustice are not limited to technical shortcomings but are shaped by opacity,
perceived arbitrariness, and the absence of control over algorithmic outcomes.
Third, the review shows that brand reputation is directly tied to algorithmic behavior. When AI-driven
systems exclude or misclassify users, or when generated content reflects stereotypes, such outcomes
are interpreted as failures of corporate responsibility rather than as isolated technological errors. Public
backlash is intensified by social media amplification, activist framing, and regulatory scrutiny,
transforming algorithmic flaws into reputational crises that affect consumer loyalty and stakeholder
confidence.
Finally, the literature identifies a range of mitigation strategies and governance mechanisms. Technical
interventions such as fairness-aware data engineering, explainable AI, and post-hoc audits are
increasingly combined with organizational practices including ethics-by-design, internal oversight
committees, and staff training. At the regulatory level, emerging frameworks like the EU AI Act and
FTC guidelines provide external accountability, while voluntary certifications and transparency reports
signal ethical alignment to consumers and investors. Collectively, these measures illustrate that
addressing algorithmic bias is no longer a peripheral task but a strategic imperative for sustaining
consumer equity and brand legitimacy in the digital economy.
10. Discussion
The findings of this review demonstrate that algorithmic bias in AI-driven marketing is not a purely
technical issue but a socio-technical challenge that lies at the intersection of data practices,
organizational priorities, and societal expectations. While AI is widely embraced for its capacity to
optimize targeting, personalization, and pricing, the evidence consistently reveals a tension between
profit maximization and fairness. Systems designed to optimize conversion rates or customer lifetime
value often privilege majority or high-income groups, leading to patterns of digital exclusion that
contradict the ethical commitments many brands publicly promote. This conflict illustrates the trade-off
between efficiency and equity that lies at the heart of AI marketing design.
The literature further shows consensus that personalization can easily slide into discrimination. Studies
agree that biased training data and proxy variables, such as ZIP codes or device types, embed structural
inequalities into model outputs. Yet there is some divergence in scholarly perspectives: while some
argue that technical interventions such as fairness-aware learning and explainable AI can substantially
mitigate these harms, others emphasize that without organizational culture change and regulatory
oversight, technical fixes alone risk becoming superficial. This divide underscores the importance of
integrating ethical governance alongside computational methods.
Another critical theme emerging from the review is the socio-technical nature of bias. Bias is not solely
the product of flawed algorithms but of the institutional contexts in which they are deployed. Marketing
teams frequently normalize or overlook biased outcomes because fairness is not embedded as a design

www.scholink.org/ojs/index.php/ibes International Business & Economics Studies Vol. 8, No. 4, 2026
Published by SCHOLINK INC.
34
priority, while consumers interpret these outputs as reflections of brand values. This duality—where
technical outputs are framed as ethical failures—highlights how deeply marketing AI systems are
entwined with social trust and organizational legitimacy.
Finally, the review points to significant gaps in current research. Much of the evidence is drawn from
Western contexts, leaving cultural and geographic blind spots in understanding how fairness is
interpreted across societies. Longitudinal studies remain scarce, limiting our knowledge of how biases
evolve over time or how mitigation strategies perform in practice. Moreover, there is limited
exploration of intersectionality, where overlapping identities such as age, gender, and ethnicity interact
to shape unique experiences of algorithmic exclusion. Addressing these gaps will require
interdisciplinary approaches that integrate marketing, computer science, law, and consumer
psychology.
In sum, the discussion highlights that algorithmic bias in marketing is both a technical and ethical
frontier. Reconciling business performance goals with fairness and accountability is not merely a
matter of fine-tuning models but of rethinking the values embedded in marketing practices. The
challenge for scholars and practitioners alike is to design AI systems that are not only efficient and
profitable but also inclusive, transparent, and aligned with the principles of consumer equity.
11. Limitations of the Review
This review has several limitations. First, it is a critical integrative review rather than a preregistered
systematic review, and the available source file does not contain a complete database-by-database
screening log or study-selection flow diagram. Accordingly, the synthesis should not be interpreted as
an exhaustive census of the literature. Second, the evidence base spans heterogeneous research designs
and application domains, limiting direct comparison of effect sizes or causal claims. Third, the
literature is concentrated in Western and technology-intensive contexts, which constrains cross-cultural
generalizability. Finally, the rapid development of generative and agentic AI means that regulatory
frameworks and empirical evidence can change quickly. Future reviews should use a preregistered
protocol, transparent screening records, formal quality appraisal, and periodic search updates.
12. Conclusion
Algorithmic bias in AI marketing is not merely a technical oversight—it is a socio-technical
phenomenon with profound ethical, commercial, and societal implications. As this review has shown,
bias can be encoded into marketing systems through historical data patterns, model optimization
choices, and real-world deployment contexts. These biases manifest in discriminatory pricing,
exclusionary targeting, and stereotyped content, undermining both consumer equity and brand
legitimacy. Trust, once anchored in product quality, now hinges on algorithmic fairness, explainability,
and responsiveness. Moreover, the impacts of bias are not evenly distributed—intersectional and

www.scholink.org/ojs/index.php/ibes International Business & Economics Studies Vol. 8, No. 4, 2026
Published by SCHOLINK INC.
35
underrepresented groups often face compounded harm, which remains undetected in aggregate metrics.
Addressing this challenge demands more than technical solutions; it requires a cultural shift in how
organizations design, govern, and evaluate their AI systems. Fairness must become a foundational
principle—integrated into the data pipeline, internal governance, and regulatory frameworks. In an era
of ethical consumerism and heightened digital scrutiny, brands that fail to engage with these challenges
risk losing not only market share, but moral credibility.
References
Akter, S., Dwivedi, Y. K., Sajib, S., Biswas, K., Bandara, R. J., & Michael, K. (2022). Algorithmic bias
in machine learning-based marketing models. Journal of Business Research, 144, 201-216.
Akter, S., Sultana, S., Mariani, M., Wamba, S. F., Spanaki, K., & Dwivedi, Y. K. (2023). Advancing
algorithmic bias management capabilities in AI-driven marketing analytics research. Industrial
Marketing Management, 114, 243-261.
Ameen, N., Tarhini, A., Reppel, A., & Anand, A. (2021). Customer experiences in the age of artificial
intelligence. Computers in Human Behavior, 114, 106548.
https://doi.org/10.1016/j.chb.2020.106548
Brynjolfsson, E., Rock, D., & Syverson, C. (2018). Artificial intelligence and the modern productivity
paradox: A clash of expectations and statistics. In A. Agrawal, J. Gans, & A. Goldfarb (Eds.), The
economics of artificial intelligence: An agenda (pp. 23-57). University of Chicago Press.
Danks, D., & London, A. J. (2017). Algorithmic bias in autonomous systems. In Proceedings of the
Twenty-Sixth International Joint Conference on Artificial Intelligence (pp. 4691-4697).
International Joint Conferences on Artificial Intelligence Organization.
Davenport, T., Guha, A., Grewal, D., & Bressgott, T. (2020). How artificial intelligence will change the
future of marketing. Journal of the Academy of Marketing Science, 48(1), 24-42.
De Bruyn, A., Viswanathan, V., Beh, Y. S., Brock, J. K. U., & von Wangenheim, F. (2020). Artificial
intelligence and marketing: Pitfalls and opportunities. Journal of Interactive Marketing, 51,
91-105.
Deldjoo, Y., Jannach, D., Bellogín, A., Difonzo, A., & Zanzonelli, D. (2024). Fairness in recommender
systems: Research landscape and future directions. User Modeling and User-Adapted Interaction,
34(1), 59-108.
Du, S., & Xie, C. (2021). Paradoxes of artificial intelligence in consumer markets: Ethical challenges
and opportunities. Journal of Business Research, 129, 961-974.
Dwivedi, Y. K., Hughes, L., Ismagilova, E., et al. (2021). Artificial intelligence (AI): Multidisciplinary
perspectives on emerging challenges, opportunities, and agenda for research, practice and policy.
International Journal of Information Management, 57, 101994.
https://doi.org/10.1016/j.ijinfomgt.2019.08.002

www.scholink.org/ojs/index.php/ibes International Business & Economics Studies Vol. 8, No. 4, 2026
Published by SCHOLINK INC.
36
Eid, M. A. H., Hashesh, M. A., Sharabati, A.-A. A., Khraiwish, A., Al-Haddad, S., & Abusaimeh, H.
(2024). Conceptualizing ethical AI-enabled marketing: Current state and agenda for future
research. International Journal of Data and Network Science, 8(4), 2291-2306.
https://doi.org/10.5267/j.ijdns.2024.6.002
Gonçalves, A. R., Pinto, D. C., Rita, P., & Pires, T. (2023). Artificial intelligence and its ethical
implications for marketing. Emerging Science Journal, 7(2), 313-327.
Hermann, E. (2022). Leveraging artificial intelligence in marketing for social good—An ethical
perspective. Journal of Business Ethics, 179(1), 43-61.
Huang, M.-H., & Rust, R. T. (2021). A strategic framework for artificial intelligence in marketing.
Journal of the Academy of Marketing Science, 49(1), 30-50.
https://doi.org/10.1007/s11747-020-00749-9
Kordzadeh, N., & Ghasemaghaei, M. (2022). Algorithmic bias: Review, synthesis, and future research
directions. European Journal of Information Systems, 31(3), 388-409.
Mehrabi, N., Morstatter, F., Saxena, N., Lerman, K., & Galstyan, A. (2021). A survey on bias and
fairness in machine learning. ACM Computing Surveys, 54(6), Article 115, 1-35.
https://doi.org/10.1145/3457607
Naz, H., & Kashif, M. (2025). Artificial intelligence and predictive marketing: An ethical framework
from managers’ perspective. Spanish Journal of Marketing-ESIC, 29(1), 22-45.
https://doi.org/10.1108/SJME-06-2023-0154
Reed, C., Wynn, M., & Bown, R. (2025). Artificial intelligence in digital marketing: Towards an
analytical framework for revealing and mitigating bias. Big Data and Cognitive Computing, 9(2),
40. https://doi.org/10.3390/bdcc9020040
Shrestha, Y. R., Ben-Menahem, S. M., & von Krogh, G. (2019). Organizational decision-making
structures in the age of artificial intelligence. California Management Review, 61(4), 66-83.
https://doi.org/10.1177/0008125619862257
Su, Y., Wang, J., & Berthon, P. (2023). Ethical marketing AI? A structured literature review of the
ethical challenges posed by artificial intelligence in the domains of marketing and consumer
behavior. In Proceedings of the 56th Hawaii International Conference on System Sciences (pp.
4933-4942). https://doi.org/10.24251/HICSS.2023.603
Yilmaz, B., & Ashqar, H. I. (2025). Towards equitable AI: Detecting bias in using large language
models for marketing. arXiv preprint.
