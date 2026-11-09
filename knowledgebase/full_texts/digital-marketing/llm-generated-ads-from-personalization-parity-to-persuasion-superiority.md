---
title: 'LLM-Generated Ads: From Personalization Parity to Persuasion Superiority'
url: https://arxiv.org/abs/2512.03373
category: digital-marketing
subcategory: empirical
date: 2025-12
venue: ''
authors:
- Elyas Meguellati
- Stefano Civelli
- Lei Han
- Abraham Bernstein
- Shazia Sadiq
source: arxiv
pdf_url: https://arxiv.org/pdf/2512.03373
pages: 25
chars: 83563
fetched_at: '2026-11-08T13:17:54+00:00'
kb_version: 1
---

# LLM-Generated Ads: From Personalization Parity to Persuasion Superiority

LLM-Generated Ads:
From Personalization Parity to Persuasion Superiority
ELYAS MEGUELLATI,The University of Queensland, Australia
STEFANO CIVELLI,The University of Queensland, Australia
LEI HAN,The University of Queensland, Australia
ABRAHAM BERNSTEIN,The University of Zurich, Switzerland
SHAZIA SADIQ,The University of Queensland, Australia
GIANLUCA DEMARTINI,The University of Queensland, Australia
As large language models (LLMs) become increasingly capable of generating persuasive content, understanding
their effectiveness across different advertising strategies becomes critical. This paper presents a two-part
investigation examining LLM-generated advertising through complementary lenses: (1) personality-based and
(2) psychological persuasion principles. In our first study (n=400), we tested whether LLMs could generate
personalized advertisements tailored to specific personality traits (openness and neuroticism) and how their
performance compared to human experts. Results showed that LLM-generated ads achieved statistical parity
with human-written ads (51.1% vs. 48.9%,𝑝> 0.05), with no significant performance differences for matched
personalities. Building on these insights, our second study (n=800) shifted focus from individual personalization
to universal persuasion, testing LLM performance across four foundational psychological principles: authority,
consensus, cognition, and scarcity. AI-generated ads significantly outperformed human-created content,
achieving a 59.1% preference rate (vs. 40.9%, p<0.001), with the strongest performance in authority (63.0%) and
consensus (62.5%) appeals. Qualitative analysis revealed AI’s advantage stems from crafting more sophisticated,
aspirational messages and achieving superior visual-narrative coherence. Critically, this quality advantage
proved robust: even after applying a 21.2 percentage point detection penalty when participants correctly
identified AI-origin, AI ads still outperformed human ads, and 29.4% of participants chose AI content despite
knowing its origin. These findings demonstrate LLMs’ evolution from parity in personalization to superiority in
persuasive storytelling, with significant implications for advertising practice given LLMs’ near-zero marginal
cost and time requirements compared to human experts.
ACM Reference Format:
Elyas Meguellati, Stefano Civelli, Lei Han, Abraham Bernstein, Shazia Sadiq, and Gianluca Demartini. 2025.
LLM-Generated Ads: From Personalization Parity to Persuasion Superiority. 1, 1 (December 2025), 25 pages.
https://doi.org/10.1145/nnnnnnn.nnnnnnn
1 INTRODUCTION
The rapid emergence of Generative AI (GenAI) is reshaping how marketing content is produced and
deployed, with early evidence that such systems can materially affect creative tasks and workflows
in practice [22]. In advertising, this shift intersects with a longstanding, resource-intensive creative
process that relies on expert iteration and collaboration within agencies [53]. A central question
Authors’ Contact Information: Elyas Meguellati, The University of Queensland, Brisbane, Australia, m.meguellati@uq.edu.au;
Stefano Civelli, The University of Queensland, Brisbane, Australia; Lei Han, The University of Queensland, Brisbane,
Australia; Abraham Bernstein, The University of Zurich, Zurich, Switzerland; Shazia Sadiq, The University of Queensland,
Brisbane, Australia; Gianluca Demartini, The University of Queensland, Brisbane, Australia.
Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee
provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the
full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored.
Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires
prior specific permission and/or a fee. Request permissions from permissions@acm.org.
©2025 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM XXXX-XXXX/2025/12-ART
https://doi.org/10.1145/nnnnnnn.nnnnnnn
, Vol. 1, No. 1, Article . Publication date: December 2025.
arXiv:2512.03373v1  [cs.CY]  3 Dec 2025

2 Meguellati et al.
follows:Can large language models (LLMs) achieve parity with or surpass human experts in the
generation of persuasive communications that effectively engage consumers?
Understanding LLM effectiveness in advertising requires engaging with two pillars of persuasive
communication. First ispersonalization: tailoring messages to individual differences, for which the
Big Five framework provides a widely used lens [19]. Personality-targeted advertising has shown
that aligning message framing with traits can increase effectiveness at scale [ 36, 57]. Second is
persuasion: leveraging broadly applicable influence mechanisms that shape judgments independent
of narrow targeting. Decades of work document the roles of source credibility (authority) [ 43],
social norms and consensus [13], processing fluency and cognition [1], and scarcity signals [35] in
driving compliance and choice.
A further consideration is whether theoriginof content (human vs. AI) changes consumer
response. Behavioral research shows both “algorithm aversion, ” where people discount algorithmic
outputs after observing errors [15], and “algorithm appreciation, ” where people sometimes prefer
algorithmic to human advice [34]. These mixed priors make advertising a particularly revealing
domain for testing whether high-quality execution by LLMs can overcome origin-based biases.
This paper presents a two-part investigation that evaluates LLM-generated advertising across
both the personalization and persuasion paradigms. In Study 1, we test whether LLMs can implement
trait-based personalization (openness, neuroticism) with effectiveness on par with human experts
when audiences are trait-matched. Study 2 shifts to universal persuasion, comparing LLM- and
human-crafted ads built around authority, consensus, cognition, and scarcity principles. Across
both studies, we combine quantitative preference data with qualitative analysis to examine which
ads participants prefer, why they prefer them, and whether origin (human vs. AI) matters.
Our findings reveal a progression. In Study 1, LLM-generated ads achieve statistical parity
with human experts for matched personalities. In Study 2, when applying universal persuasion
principles, LLM-generated ads significantly outperform human-created content (59.1% vs. 40.9%,
𝑝<. 001), and this superiority remains robust even when participants correctly identify content
as AI-generated. Qualitative analyses suggest that LLMs deliver more aspirational messaging and
stronger visual–narrative coherence, indicating a shift in which execution quality—rather than
human authorship—may increasingly determine advertising effectiveness.
Contributions
This paper makes two primary contributions:
(1) Empirical evidence of LLM advertising effectiveness across paradigms:We provide the
first systematic comparison of LLM-generated versus human-created advertising across both
personalization and persuasion strategies, revealing conditions under which LLMs achieve
parity versus superiority.1
(2) Evidence of quality transcending origin:Through mixed-methods analysis, we show that
high-quality execution can overcome bias against AI-identified content. Specifically, we find
that even after applying a 21.2 percentage point detection penalty, AI ads still outperform
human ads, and 29.4% of participants chose AI content despite knowing its origin—challenging
assumptions about the necessity of human authenticity in persuasive communication.
1This article is an extended version of our short paper published in the Companion Proceedings of the ACM Web Conference
2024 [39]. Compared to the preliminary version which focused solely on personality-based text generation (Study 1), this
work introduces a completely new experiment evaluating multimodal persuasion principles (Study 2), adds a detailed
qualitative analysis of user preference drivers (Appendix A), and provides new demographic insights regarding AI Preference
and bias.
, Vol. 1, No. 1, Article . Publication date: December 2025.

LLM-Generated Ads:
From Personalization Parity to Persuasion Superiority 3
2 RELATED WORK
2.1 Personalization in Advertising
Personalizing ads based on users’ personality traits has gained significant attention in recent years
due to its potential to enhance engagement and effectiveness. Youyou et al . [60] demonstrated
the potential of computer-based models in achieving more accurate personality judgments using
Facebook Likes, offering insights into the future of social-cognitive activities in various domains.
Kosinski et al. [31] highlighted that personal traits and attributes can be predicted from digital
records of human behavior, such as Facebook Likes, with a high degree of accuracy, raising both
opportunities and concerns about privacy.
Matz et al. [37] discussed the effectiveness of psychological targeting for digital mass persuasion
and found that substantial changes in behavior were observed when tailoring persuasive appeals
to the person’s psychological traits. Similarly, Zarouali et al. [62] investigated the effectiveness of
political microtargeting (PMT) by tailoring political ads to citizens’ personality traits and found
that customizing political ads to match citizens’ personality traits results in greater persuasion.
Chen et al . [10] explored the relationship between personality traits and ad engagement in
social media advertising and demonstrated the effectiveness of using derived personality traits
for social media ad targeting. Winter et al . [56] investigated the effects of microtargeting on
consumer persuasion in the context of social media advertising and found that ads tailored to
specific persuasive strategies and personality traits showed higher engagement intentions.
Shumanov et al . [48] their approach involves utilizing contextual information to determine
consumer personality traits, they demonstrated that aligning consumer personality with corre-
sponding advertising messages can result in more successful persuasion. Ning et al. [40] proposed a
Friend Recommendation System (FRS) that leverages the five traits and hybrid filtering, taking into
account both traits and harmony ratings for friend suggestions, showing potential for enhancing
personalized user experiences on social media platforms.
Lee et al. [32] examined the impact of social media advertising content on customer engagement,
specifically focusing on emotional, humorous, and informative content. They found that brand
personality, particularly philanthropic gestures, increases customer engagement, while informative
content does not perform well. Ribeiro et al. [45] provided insights on the abuse and exploitation
of Facebook’s targeted advertising infrastructure for political gain and suggested ways to redesign
the infrastructure to prevent such abuse, which can have implications for ad personalization and
targeting strategies.
In addition to the previously mentioned studies, Hirsh et al. [25] investigated the effectiveness
of tailoring ads based on individuals’ personality traits and found that ads designed to match the
recipient’s psychological profile were more effective in changing consumer attitudes . Moreover,
Winter et al. [56] demonstrated that personality-targeted ads can increase user engagement in social
media advertising compared to non-targeted ads, indicating the potential for personality-based
targeting to improve the overall effectiveness of advertising campaigns.
The literature on personalizing ads based on users’ personality traits has demonstrated the
potential of leveraging digital records of human behavior and computer-based models for more
accurate personality judgments and targeting. However, it also raises concerns about privacy
and the potential for abuse. These studies highlight the importance of responsible ad targeting,
transparency, and control over users’ information, as well as the need to carefully consider the
ethical implications of ad personalization [31, 45]. Furthermore, the findings suggest that trait-based
personalization can enhance the persuasiveness of advertising messages by increasing the relevance
and resonance of the content with the target audience [10, 48, 56].
, Vol. 1, No. 1, Article . Publication date: December 2025.

4 Meguellati et al.
In addition to what has been stated, studies have been conducted to investigate the interactions
between personality traits and factors such as emotional, humorous, and informative content,
to optimize ad performance and engagement [32]. These studies have provided insights into the
complex interplay between personality traits and advertising content, including the impact of
different types of content on customer engagement and the role of brand personality in influencing
consumer behavior.
However, the ethical implications of using personal data for targeting purposes have also been a
concern in the field of personalized advertising. Researchers have examined the need to protect
users’ privacy and prevent the abuse of targeted advertising infrastructure, particularly in sensitive
domains like political advertising [45, 62]. These studies have emphasized on the importance of
responsible ad targeting and the challenges of balancing effective personalization with ethical
considerations.
Having explored the related work on personalization in advertising, the next subsection will
discuss the use of large language models (LLMs) and their capabilities, further expanding the scope
of the literature review and providing a comprehensive foundation for the study of personalized
ads creation using LLMs.
2.2 The Emergence of LLMs
Significant progress has been made in LLMs, with increased scale and data volume contributing to
enhanced performance in a variety of tasks, in accordance with the established scaling law [28].
Models such as GPT-3 (175B parameters) and PaLM (540B parameters) demonstrate capabilities and
behaviors distinct from smaller models like BERT (330M parameters) and GPT-2 (1.5B parameters),
thanks to their emergent abilities [54]. LLMs’ capacity to handle complex tasks, including few-shot
learning via in-context understanding, is exemplified by GPT-3 [26, 47, 52, 55].
The advent of innovative LLMs, such as ChatGPT, and the anticipation surrounding GPT-4 have
led to debates within the AI community about the possibility of artificial general intelligence (AGI),
with some arguing that GPT-4 could be the first iteration of an AGI system [8].
LLMs’ impact extends beyond Natural Language Processing (NLP) and encompasses fields such as
Information Retrieval (IR) and Computer Vision (CV). In NLP, LLMs serve as all-purpose language
task solvers. In IR, AI chatbots like ChatGPT challenge conventional search engines, while platforms
like New Bing employ LLMs to improve search results [9, 16, 27, 58]. In CV, vision-language models
such as GPT-4 are being developed to enable multimodal dialogues [64].
However, while the progress and implications of LLMs are remarkable, there are still challenges in
understanding the underlying principles that contribute to their superior abilities [18, 54]. Questions
persist regarding the emergence of these capabilities and the factors that drive this phenomenon.
Additionally, the practical aspects of training proficient LLMs, including computational resource
requirements and ensuring alignment with human values and preferences, necessitate further
research and development2. As the field continues to advance, continued exploration of LLMs
and addressing these challenges will pave the way for unlocking their full potential in various
domains. Our study on utilizing LLMs for generating personalized ads complements existing work
by enabling automated targeting at scale, leveraging their power to revolutionize the delivery of
tailored advertisements.
2.3 LLMs for Personalized Persuasion
LLMs have rapidly advanced the study and practice of personalized persuasion across various
application areas such as public policy, health, advertising, and dialogic settings. Empirically, several
2https://cdn.openai.com/papers/gpt-4.pdf
, Vol. 1, No. 1, Article . Publication date: December 2025.

LLM-Generated Ads:
From Personalization Parity to Persuasion Superiority 5
studies demonstrate that LLMs can generate messages that are at least as persuasive as typical
human baselines, and sometimes more so, especially when tailored to audience characteristics.
For instance, Matz et al . [38] show across four studies that ChatGPT-crafted messages aligned
to recipients’ psychological profiles outperform non-personalized alternatives, underscoring the
scalability of microtargeted generation. In the political domain, Bai et al . [6] report that LLM-
authored messages can meaningfully shift attitudes on policy issues at magnitudes comparable to
human-written texts, albeit via distinct stylistic pathways (e.g., perceived factuality and logical tone
for AI vs. originality for humans). Moving to interactive debate, Salvi et al. [46] find that GPT-4,
when given access to demographic cues for personalization, “outpersuades” a human interlocutor
in roughly two-thirds of trials, highlighting the potency of personalization in dialogue.
At the same time, evidence is mixed on the incremental value of fine-grained microtargeting
relative to strong generic messaging. Using GPT-3 to instantiate multiple persuasive strategies
(including microtargeting and interactive elaboration), Argyle et al. [3] find significant attitude
change overall from AI-generated content but only modest gains from personalization beyond a
well-crafted generic message. In health communication, Karinshak et al. [29] show that GPT-3 can
produce pro-vaccination messages rated more effective than official guidance, while also revealing
that source labeling (AI vs. human) shapes reception—pointing to the importance of disclosure and
perceived agency in persuasive outcomes.
Alongside efficacy, emerging work flags ethical and safety risks when LLMs are tasked with
influence. Liu et al. [33] introduce a framework showing that many popular models inconsistently
refuse unethical persuasion requests and may exhibit manipulative tactics under certain prompts,
motivating stronger alignment and policy controls for persuasion-capable systems. Complementing
this, benchmark- and platform-oriented efforts such as Singh et al. [49] proposePersuasionBenchand
PersuasionArenato systematically evaluate persuasion (including the “transsuasion” transformation
task), documenting both model strengths in generation and notable weaknesses in simulating
persuasion dynamics.
Methodologically, the personalization toolkit around LLMs is expanding. Data- and optimization-
efficient approaches include modular parameter sharing as in Tan et al . [50] (PER-PCS), which
composes user-specific “pieces” for efficient adaptation; prompt-then-edit pipelines as in Zhang
et al. [63], which synthesize self-preference data and modify internal representations for rapid on-
the-fly personalization; and preference induction from user writing samples, as in Aroca-Ouellette
et al. [4] (PROSE), which yields substantial improvements in stylistic alignment. Benchmarking
frameworks such as Zollo et al. [65] (PersonalLLM) further standardize evaluation of user-tailored
outputs under sparse feedback, enabling controlled comparisons across algorithms and data regimes.
Broader surveys synthesize these directions: Chen et al. [11] outline opportunities and challenges
for LLM-centric personalized computing (e.g., long-term user modeling, privacy, tool use), while
Xu et al. [59] systematize personalized generation across modalities and tasks, identifying open
problems in data scarcity, privacy-preserving modeling, and cross-modal alignment.
Applications span beyond persuasion per se to personalized assistance and narrative engagement.
In information seeking, Baek et al. [5] show that knowledge-augmented LLMs can produce more
contextually relevant, user-tailored query suggestions; Prahlad et al. [44] similarly demonstrate
GraphRAG-style personalization by integrating user knowledge graphs for dialogue. In narrative
domains, Yunusov et al. [61] find that personalized “mirror” stories generated by GPT-4 are rated
more engaging than generic AI or human baselines, suggesting benefits for education and inclusion.
Within synthetic social reasoning, Breum et al. [7] observe that arguments emphasizing factual
evidence, trust, and status cues tend to be most persuasive, offering design signals for LLM-mediated
influence.
, Vol. 1, No. 1, Article . Publication date: December 2025.

6 Meguellati et al.
Advertising is a focal use case and a locus of concern. Meguellati et al. [39] show that GPT-based
models can match human-crafted, persona-tailored ad copy in relevance and appeal, indicating
near-term viability of scalable customized creative. Yet user research reveals pitfalls: Tang et al. [51]
find that embedded, personalized ads in chatbot responses are often unnoticed without disclosure
but reduce trust and increase perceived intrusiveness when disclosed, raising UX, transparency, and
autonomy questions. Finally, head-to-head tests against experts suggest that state-of-the-art LLMs
are already competitive persuaders: Hackenburg et al . [23] report GPT-4 performs on par with
political campaign professionals overall (and better on some topics), while persona-alignment yields
limited average gains—again tempering expectations about microtargeting’s marginal returns.
3 METHODOLOGY
We employ a generation pipeline that leverages Knowledge Graphs (KGs) to LLMs outputs, as
illustrated in Figure 1. Specifically, the KG functions as a structured grounding layer, effectively
mapping the semantic relationships between abstract user traits and concrete product attributes to
ensure that the prompt context is data-driven rather than generic. In this architecture, the LLM
serves as the central engine, transforming structured constraints—from user attributes to psycho-
logical principles—into targeted advertising copy. To strictly evaluate the quality and efficacy of
these AI-generated narratives without the confounding variables of a live deployment environment,
we isolate the generative module in our experiments. This allows us to systematically benchmark
the LLM’s performance against human experts across both personality-based and persuasion-based
tasks.
Fig. 1. The proposed generation pipeline. Stage 1 utilizes a KG to map user-product relationships, providing
structured context for prompt construction. In Stage 2, the LLM transforms these constraints into persuasive
narratives (Generative Storytelling), which are then delivered to matched audiences in Stage 3.
3.1 Study 1: Personalizing with LLMs
This study aims to explore how effective LLM-generated ads are compared to ads created by humans.
We are interested in how this effectiveness is tied to personality traits, especially in individuals
, Vol. 1, No. 1, Article . Publication date: December 2025.

LLM-Generated Ads:
From Personalization Parity to Persuasion Superiority 7
with high levels of openness or neuroticism. To this end, we focus on: (i) studying how well LLMs
can personalize ads for specific personality traits, (ii) finding out which personality trait works best
for LLM-based ad personalization, and (iii) comparing how LLM-generated ads and human-written
ads perform in terms of personalization and user engagement.
To study the individual preferences of the participants with respect to their ad engagement, we
designed two tasks followed by the Big5 questionnaire [14].
After showing them an ad,Task 1is designed to capture participants’ responses on a 5-point
Likert scale for three aspects: (i) the product attitude, where we ask them to provide a rating to
indicate how they like this advertisement, (ii) the purchase intention, where we ask them the
likelihood of their intent to purchase the advertised product after viewing the advertisement, and
(iii) the engagement intention, assessing their interest in seeking further information about the
product featured in the advertisement.Task 2seeks to assess the effectiveness of LLM-generated
ads compared to human-written ads when presented side by side. It aims to examine participant
preferences in selecting the best ads. By displaying both types of ads simultaneously, we can
evaluate their relative performance and determine how generated ads comparatively appeal to
human-written ads.The Big5is a 20-item questionnaire that allows us to calculate participants’
personality scores and it is administered after subjects complete the previous tasks.
3.1.1Dataset.The human-written ads used in our study were sourced from the research by
Winter et al. [56]. For the generation of ad messages targeting openness and neuroticism traits, we
employed two LLM prompts. The prompts are as follows:
• “write a 1 line ad for a phone called Xphone targeting people with the openness trait without
mentioning the trait explicitly"
• “write a 1 line ad for a phone called Xphone targeting people with the neuroticism trait
without mentioning the trait explicitly"
In our experiments, we maintained the ‘temperature’ – a setting of that controls the randomness
of the model’s response - at its default setting of 0.7. This value offers a balance between randomness
and determinism which provides the model with enough flexibility to generate inventive outputs,
while still ensuring it stays relevant to the given prompts.
As the LLM, we utilized GPT 3.5, despite the availability of newer models such as GPT 3.5-Turbo
(also known as ChatGPT) and GPT-4. Our decision was motivated by the desire for reproducibility
and consistency as during our study both GPT 3.5-Turbo and GPT-4 were undergoing frequent
updates.
3.1.2Task Design.
Task 1.Four surveys were created as shown in Figure 2. The study included multiple versions
of the same ad image with varying messages customized for individuals with high openness or
neuroticism traits, and created either by a human, or the LLM.
Participants were presented with the same image in all surveys along with one of the four
message variations, where the survey type is associated with the ad message shown as follows:
•OH:Openness, written by aHuman
•OG:Openness,Generated by an LLM
•NH:Neuroticism, written by aHuman
•NG:Neuroticism,Generated by an LLM
Participants were then asked to rate their perception of the product, purchase intention, and
engagement intention on a 5-point Likert scale ranging from “very unlikely" to “very likely".
, Vol. 1, No. 1, Article . Publication date: December 2025.

8 Meguellati et al.
Fig. 2. Procedure of the experiment: (i) Task 1, including three questions presented on a 5-point Likert scale;
(ii) Task 2, prompting participants to select one ad message from the four messages displayed side-by-side;
followed by (iii) the Big5 questionnaire to gather their personality information. Note that there are four
variants of Task 1: OH, OG, NH, and NG
Task 2.Once they completed Task 1, participants were shown all four messages simultaneously
and asked to select their preferred message. It is important to consider the potential bias that may
arise from participants having seen one of the four ads in Task 1. However, this bias is balanced
out across the four surveys since an equal number of participants were exposed to each ad before
proceeding to Task 2. By ensuring that the same number of participants viewed each of the four
ads before the preference selection task, the influence of any individual ad exposure in Task 1 is
mitigated. Thus, when examining the data in an aggregate fashion, the bias resulting from the
initial exposure to a specific ad is minimized, ensuring a fair assessment of participants’ preferences
in Task 2.
Big5 questionnaire.After having completed the tasks, participants answered a Big Five personality
questionnaire (20 items) focusing on openness and neuroticism [ 14]. The analysis explored the
relationship between these traits and task responses. Participants were categorized based on their
openness and neuroticism scores. The questionnaire was strategically placed at the study’s end to
minimize bias from prior exposure to the questionnaire, though it leads to reduced control over
personality and demographic distributions.
3.1.3Measurements.
Task 1.The Mann-Whitney test was utilized to assess statistical significance because the data is
not equally distributed, and the Benjamini-Hochberg correction was applied to account for multiple
comparisons.
Task 2.We employed the chi-square test to examine variable independence and assess the
relationship between the different ad messages.
Personality Traits.To systematically compare the effectiveness of generated ads with matched
and non-matched personality traits, this study measures the Big Five personality traits used to
tailor messages. These traits are measured with The Big Five personality questionnaire [14, 20] on
, Vol. 1, No. 1, Article . Publication date: December 2025.

LLM-Generated Ads:
From Personalization Parity to Persuasion Superiority 9
Fig. 3. Example of advertisements used in Study 2 for the scarcity persuasion principle condition. Left: Human-
created advertisement. Right: AI-generated advertisement (text generated using LLMs, image generated using
a diffusion model - Midjourney). Both ads emphasize time-limited availability and urgency, core elements of
the scarcity principle. Participants viewed both advertisements side-by-side without knowledge of which was
AI-generated.
a 6-point Likert scale, including openness (e.g., “Am able to come up with new and different ideas")
and neuroticism (e.g., “Get overwhelmed by emotions"), as they are the focus of the study.
3.1.4Participants.The study recruited 400 participants from Amazon Mechanical Turk (MTurk),
with an equal distribution of 100 participants assigned to each survey variation. The participants’
demographics are: 297 males (74.2%) and 103 females (25.8%), with an average age of 32. The tasks
took approximately 5 minutes to complete, and participants were rewarded $1 for their time. To
ensure English proficiency, participants must be 18 or older and reside in the United States.
3.2 Study 2: Persuasion Principles with LLMs
This study investigates the effectiveness of AI-generated advertisements compared to human-
created advertisements across different persuasion principles [ 12]. While Study 1 focused on
personality-based personalization with varying text messages, Study 2 examines complete adver-
tisements (both image and text) designed around established persuasion principles. Our objectives
are to: (i) assess participant preferences between AI-generated and human-created ads within
different persuasion contexts, (ii) understand the qualitative factors influencing these preferences,
and (iii) evaluate participants’ ability to distinguish AI-generated content from human-created
content.
3.2.1Dataset.For each persuasion condition, we generated outputs from three LLMs (GPT-5,
Sonnet 4, LLama 4). To rigorously test the democratization potential of GenAI, we adopted anon-
expert selection protocol. A single author (with a Computer Science background and no professional
advertising training) manually selected the final variant based on subjective appeal and perceived
, Vol. 1, No. 1, Article . Publication date: December 2025.

10 Meguellati et al.
quality, acting as a proxy for a general end-user. This methodological choice ensures our results
represent aconservative lower boundof AI performance: if a non-expert selector relying on intuition
can achieve parity or superiority, professional curation would likely yield even higher efficacy.
All advertisements featured the same product (Xphone) used throughout Study 1, ensuring
consistency across both studies. The advertisements were designed around four distinct persuasion
principles [12]:
•Consensus: Emphasizing social proof and the popularity of the product among users
•Authority: Highlighting expert endorsements and professional credibility
•Scarcity: Focusing on limited availability and time-sensitive offers
•Cognition: Appealing to rational thinking and logical product features
3.2.2Task Design.We employed a between-subjects design with four experimental conditions
corresponding to the four persuasion principles. A total of 800 participants were recruited, with
200 participants randomly assigned to each condition. Unlike Study 1, where participants evaluated
advertisements with identical images but varying text messages, Study 2 presented participants
with complete advertisements featuring both unique images and text tailored to each persuasion
principle. Figure 3 illustrates an example of the advertisements used in the scarcity condition,
showing both the human-created and AI-generated versions presented to participants.
In each condition, participants were shown two advertisements side-by-side: one human-created
and one AI-generated. Both advertisements targeted the same persuasion principle and featured
the Xphone product. The presentation order of the human-created and AI-generated ads was
randomized to control for position bias.
Participants completed four sequential tasks:
Question 1: Preference Selection.Participants were asked to select which of the two advertisements
they preferred. This forced-choice format allowed us to measure direct preference between AI-
generated and human-created content within each persuasion context.
Question 2: Preference Reasoning.Following their selection, participants provided an open-ended
explanation for their preference. This qualitative data enabled us to identify the underlying reasons
driving participant choices and to understand which advertisement characteristics resonated most
strongly with viewers.
Question 3: Influencing Factors.Participants were then asked to describe, in an open-ended
format, the specific factors that influenced their decision. This question aimed to elicit more
detailed insights into the design elements, messaging strategies, or other attributes that contributed
to their preference formation.
Question 4: AI Detection.Finally, participants were asked to identify which of the two adver-
tisements they believed was generated by AI. It is important to note that participants were not
informed about the AI-generated nature of any advertisement during Questions 1-3, ensuring their
preference selection and reasoning were unbiased by knowledge of the ad’s origin. This design
allows for subsequent analysis examining potential bias towards or against AI-generated content by
comparing participants’ actual preferences (Question 1) with their perceptions of which ad was AI-
generated (Question 4). Such analysis can reveal whether participants exhibit systematic preference
patterns based on perceived AI involvement, independent of actual ad quality or effectiveness.
3.2.3Measurements.
Advertisement Preference.The chi-square test ( 𝜒 2) was utilized to assess the relationship between
advertisement type (AI vs. Human) and participant preference, as well as to test independence
, Vol. 1, No. 1, Article . Publication date: December 2025.

LLM-Generated Ads:
From Personalization Parity to Persuasion Superiority 11
across conditions. Bonferroni correction was applied to account for multiple comparisons across
the four persuasion conditions (adjusted significance threshold:𝛼=0.0125, calculated as 0.05/4).
Effect Sizes.Cohen’s h was calculated for overall proportional differences between AI and human
preference rates. Cohen’s d was computed for condition-specific effect sizes (Authority, Consensus,
Cognition, Scarcity). Risk Ratios (RR) with 95% confidence intervals were used to quantify the
relative likelihood of preferring AI versus human advertisements.
Detection Accuracy.The Kappa statistic (𝜅) was employed to measure agreement between partic-
ipants’ AI identification and actual advertisement origin beyond chance. Odds Ratios (OR) with
95% confidence intervals were calculated to assess the impact of AI detection on preference rates.
Qualitative Analysis.To analyze the open-ended justifications (Questions 2 and 3), we employed
an inductive thematic analysis approach. Responses were coded to identify recurrent drivers of
preference, such as message sophistication and visual coherence. A detailed breakdown of the
thematic definitions, coding methodology, and supplementary participant quotes is provided in
Appendix A.
3.2.4Participants.The study recruited 800 participants from Prolific, with an equal distribution of
200 participants assigned to each of the four persuasion principle conditions (Authority, Consensus,
Cognition, Scarcity). The participant demographics were: 362 females (45.3%) and 432 males (54.0%),
with ages ranging from 18 to 65+. The tasks took approximately 2 minutes to complete, and
participants were compensated £0.50 for their time (equivalent to £15/hour). To ensure data quality,
participants were required to be 18 or older, have English as their first language, and reside in the
United States.
Ethical considerations.Both studies were conducted anonymously, and participant data is
kept confidential. The studies have been approved by the first author’s institution IRB. Participants
provided informed consent to collect and analyze their data. Compensation rates for both studies
exceeded recommended minimum wages.
4 RESULTS
Our evaluation strategy mirrors the paper’s progression from investigating data-driven personal-
ization to exploring universal persuasion.
InStudy 1, the objective is to determine if GenAI can effectively tailor content based on explicit
user data (Big Five traits). We utilize psychometric Likert scales (Product Rating, Purchase Intention)
to measure thedepth of resonance—verifying that the model is not just producing generic text, but
successfully aligning with the specific psychological profile of the user.
InStudy 2, the focus shifts to investigating the model’s capacity to apply universal persuasion
principles and generate multimodal assets (text and visuals)withoutprior knowledge of the user.
Here, we transition to a forced-choice metric (Preference Rate) to evaluate thecomparative efficacy
of AI against human experts in a competitive setting.
While this difference in measurement precludes a direct statistical comparison of effect sizes
between the two studies, it allows us to evaluate each capability within its appropriate context:
validating theinternal fitof trait-based text in the former, and assessing theexternal impactof
multimodal persuasion in the latter.
4.1 Study 1: Personalizing with LLMs
4.1.1 Task 1: Effectiveness of Personality-Tailored Ads.In the first task, we evaluated the efficacy of
advertisement messages generated by LLMs compared to those written by humans, specifically
, Vol. 1, No. 1, Article . Publication date: December 2025.

12 Meguellati et al.
examining the impact of personality congruence. We measured three key dimensions of user
engagement:Product Rating,Purchase Intention, andEngagement Intention.
To ensure robust statistical analysis, we employed the Mann-Whitney U test to assess differences
between groups, given the non-normal distribution of the Likert-scale data. To control for the False
Discovery Rate (FDR) accumulation due to multiple hypothesis testing, we applied the Benjamini-
Hochberg correction to all reported𝑝-values.
Table 1. Comparative analysis of ad effectiveness (Means) and statistical significance (P-values) for Matched
vs. Unmatched personality traits. Significant values (𝑝≤0.05) are highlighted in bold.
Condition Measurement Matched Unmatchedp
Generated Ads (LLM)
Openness
(OG)
Product Rating 4.14 3.710.02
Purchase Intention 4.14 3.690.02
Engagement Intention 4.33 3.730.01
Neuroticism
(NG)
Product Rating 3.84 4.00 0.33
Purchase Intention 3.77 4.15 0.27
Engagement Intention 3.97 4.29 0.27
Human-Written Ads (Baseline)
Openness
(OH)
Product Rating 4.13 3.96 0.50
Purchase Intention 4.33 3.680.05
Engagement Intention 4.30 3.88 0.15
Neuroticism
(NH)
Product Rating 3.61 3.76 0.54
Purchase Intention 3.74 4.00 0.54
Engagement Intention 3.71 4.15 0.47
Impact of Personality Congruence (Matched vs. Unmatched)
Table 1 presents a consolidated view of the mean scores and statistical significance for both LLM-
generated and human-written advertisements.
For theOpennesstrait, we observed a strong positive effect of personalization. In the LLM-
generated condition (OG), participants with matching personality traits reported significantly
higher scores across all three metrics compared to unmatched participants. Specifically, Product
Rating (𝑝= 0.02), Purchase Intention (𝑝= 0.02), and Engagement Intention (𝑝= 0.01) all showed
statistically significant improvements when the ad content was congruent with the user’s Openness
level. A similar trend was observed in the human-written control condition (OH), where Purchase
Intention was significantly higher for matched participants (𝑝= 0.05), reinforcing that the Openness
trait is highly receptive to personalized messaging regardless of the authoring source.
Conversely, the results for theNeuroticismtrait revealed a more complex dynamic. As detailed
in Table 1, matching ad content to high-neuroticism users did not yield a positive increase in
engagement. In several instances, such as the Generated Neuroticism (NG) condition, matched
participants actually reported lower Purchase Intentions ( 𝑀= 3.77) compared to unmatched
participants (𝑀= 4.15), though these differences did not reach statistical significance after cor-
rection (𝑝> 0.05). This finding aligns with prior literature suggesting that individuals with high
, Vol. 1, No. 1, Article . Publication date: December 2025.

LLM-Generated Ads:
From Personalization Parity to Persuasion Superiority 13
neuroticism scores may exhibit avoidance behaviors or heightened caution when targeted with
stimuli that resonate with their trait-specific anxieties. Consequently, while LLMs successfully
generated content that aligned with the trait theoretically, thereceptivenessof the target audience
to neuroticism-based appeals remains low.
Comparative Efficacy: AI vs. Human
A critical objective of this study was to determine if LLM-generated content could rival human
creativity. We conducted a direct comparison between the LLM-generated ads (OG/NG) and human-
written ads (OH/NH) specifically for the matched personality groups. The statistical analysis
revealed no significant differences across any of the three measured dimensions (𝑝> 0.05for all
comparisons). For example, in the Openness condition, the Product Rating for LLM ads (𝑀= 4.14)
was statistically indistinguishable from human ads (𝑀= 4.13). This lack of significant divergence
suggests that basic LLM prompting strategies (zero-shot) are sufficient to produce advertising copy
that is perceptually equivalent to content crafted by human experts in terms of user engagement
and purchase intent.
4.1.2 Task 2: Preference and Competitive Performance.In the second task, participants evaluated
the four ad variations simultaneously in a simulated competitive shopping environment. This
forced-choice design allowed us to assess relative preference and potential click-through behavior.
The distribution of user clicks is visualized in Figure 4. The human-written ad tailored to Openness
emerged as the most preferred option, garnering 31.82% of total clicks. However, the LLM-generated
ad for Openness followed closely with 26.21%. Notably, the LLM-generated ad for Neuroticism
(24.93%) significantly outperformed its human-written counterpart (17.04%), suggesting that the
LLM may have captured a nuance in the neuroticism prompt that resonated more effectively—or
was less aversive—than the human attempt in a comparative setting.
A Chi-Squared test for independence confirmed a significant association between ad type and user
preference (𝜒 2,𝑝< 0.05). When aggregating the data by source, LLM-generated ads secured a total
of 51.14% of clicks, marginally surpassing human-written ads at 48.86%. These results indicate that
LLM-generated content is not only comparable in isolation (Task 1) but remains competitive when
presented alongside human-authored alternatives, demonstrating high stability across different
trait targets.
Human-Open LLM-Open LLM-Neuro Human-Neuro
0
10
20
30
31.82
26.21 24.93
17.04
Preference Share (%)
Fig. 4. Distribution of participant preferences (clicks) when ads were presented side-by-side in Task 2. LLM-
generated ads collectively received 51.14% of clicks compared to 48.86% for human-written ads.
, Vol. 1, No. 1, Article . Publication date: December 2025.

14 Meguellati et al.
4.2 Study 2: Persuasion Principles with LLMs
4.2.1 Advertisement Preference and Effectiveness.In the second study, we evaluated the comparative
effectiveness of AI-generated versus human-created advertisements across four distinct persuasion
principles.
Overall Performance.AI-generated advertisements achieved a dominant 59.1% preference rate
compared to 40.9% for human-created advertisements (𝜒 2 = 26.65,𝑝< 0.001). The effect size was
medium (Cohen’sℎ= 0.37), representing a substantial 18.2 percentage point advantage for the
AI-generated content.
Performance by Persuasion Principle.As detailed in Table 2, performance varied significantly
depending on the persuasion strategy employed. After applying the Bonferroni correction for mul-
tiple comparisons (𝛼= 0.0125), AI advertisements maintained a statistically significant advantage
in three of the four conditions. The strongest performance was observed in theAuthority( 𝑑= 0.52)
andConsensus( 𝑑= 0.50) conditions, suggesting that LLMs are particularly adept at generating
content that leverages credibility and social proof. Conversely, theScarcitycondition showed
no meaningful difference (𝑝= 0.671), with qualitative feedback indicating a general consumer
skepticism toward urgency tactics regardless of the source.
Table 2. AI advertisement performance across persuasion principles. Effect sizes (Cohen’sd) and Risk Ratios
(RR) are reported. Significant values after Bonferroni correction (𝑝≤0.0125) are bolded.
Principle Human AI Gapp-value Cohen’sdRR [95% CI]
Authority 37.0% 63.0% +26.0%<0.0010.52 1.70 [1.32–2.19]
Consensus 37.5% 62.5% +25.0%<0.0010.50 1.67 [1.30–2.14]
Cognition 40.5% 59.5% +19.0%0.0070.38 1.47 [1.15–1.87]
Scarcity 48.5% 51.5% +3.0% 0.671 0.06 1.06 [0.86–1.31]
Demographic Homogeneity in Preference.Table 3 presents the demographic breakdown of adver-
tisement preferences. Statistical analysis revealed no significant effects of age (𝑝= 0.363) or gender
(𝑝= 0.827) on advertisement choice. This indicates that the preference for AI-generated aesthetics
and messaging was consistent across demographic cohorts, suggesting a broad appeal rather than
a niche trend among specific user groups.
Qualitative Drivers of Preference.Analysis of open-ended responses identified three primary
drivers behind the success of AI advertisements:
• Message Sophistication:AI advertisements frequently employed aspirational language.
Participants described these messages as “inspiring” (36 mentions) and “professional” (44
mentions).
• Visual Coherence:32% of qualitative responses noted superior color palettes and image-text
unity in the AI ads. One participant notably described an AI ad’s aesthetic as evoking “a
professor’s lecture room, ” reinforcing the Authority principle.
• Psychological Precision:AI demonstrated a superior application of persuasion principles,
particularly in Authority and Consensus conditions, where participants valued clear markers
of “credentials” and “diverse group representation. ”
, Vol. 1, No. 1, Article . Publication date: December 2025.

LLM-Generated Ads:
From Personalization Parity to Persuasion Superiority 15
Table 3. Demographic distribution of advertisement preferences. AI preference rates (“AI Choosers”) remained
stable across age groups and gender categories.
DemographicNChose AI Chose Human AI Preference %
Age Group
18–24 32 20 12 62.5%
25–34 168 102 66 60.7%
35–44 198 117 81 59.1%
45–54 190 109 81 57.4%
55–64 136 77 59 56.6%
65+ 76 48 28 63.2%
Gender
Female 362 218 144 60.2%
Male 432 251 181 58.1%
Total Sample 800 473 327 59.1%
4.2.2 AI Detection Capabilities.We assessed participants’ ability to distinguish between human
and AI-generated content (“AI Spotters”). Overall, 58.4% of participants correctly identified the
AI-generated advertisement (Kappa = 0.17), indicating only a moderate detection ability beyond
random chance.
However, as shown in Table 4, detection accuracy was heavily stratified by age. Younger partic-
ipants (18–24) demonstrated significantly higher detection rates (72.5%) compared to the oldest
cohort (65+), who performed near chance levels (49.2%). The odds of correctly identifying AI were
2.78 times higher for the youngest group compared to the oldest (OR = 2.78, 95% CI: [1.23, 6.28],
𝑝<0.01).
4.2.3 The Perception-Choice Interaction.To understand whether identifying an advertisement
as AI-generated influenced user preference, we analyzed the interaction between perception and
choice. Table 5 presents a matrix of these behaviors.
The Bias Penalty vs. Quality Resilience.To quantify the bias, we calculated theDetection Penalty
(Δ𝑏𝑖𝑎𝑠 ) as the difference in AI preference rates between participants who were deceived and those
who correctly identified the source:
Δ𝑏𝑖𝑎𝑠 =𝑃(Choose AI|Believed Human)−𝑃(Choose AI|Detected AI)(1)
Substituting the observed rates yields a significant penalty:
Δ𝑏𝑖𝑎𝑠 21.2%=71.5%−50.3%
This calculation confirms a significant bias against known AI content (𝑂𝑅= 0.40,𝑝< 0.001).
However, critically, even after this penalty is applied, the AI preference rate (50 .3%) remains
above the actual human advertisement performance (40.9%), demonstrating that execution quality
effectively overrides the negative origin bias.
Synthesizing Quantitative and Qualitative Insights.Critically, 41.3% of participants (330 people)
made origin-independent choices: either selecting AI while correctly identifying it (29.4%) or
, Vol. 1, No. 1, Article . Publication date: December 2025.

16 Meguellati et al.
Table 4. AI detection accuracy (“AI Spotters”) broken down by persuasion principle and age group.
CategoryNCorrect ID Incorrect ID Accuracy %
By Persuasion Principle
Consensus 200 151 49 75.5%
Cognition 200 129 71 64.5%
Authority 200 125 75 62.5%
Scarcity 200 62 138 31.0%
By Age Group
18–24 32 23 9 72.5%
25–34 168 113 55 67.3%
35–44 198 124 74 62.8%
45–54 190 113 77 59.3%
55–64 136 74 62 54.6%
65+ 76 37 39 49.2%
Overall 800 467 333 58.4%
Table 5. Choice-Perception Matrix: The relationship between advertisement preference and origin identifica-
tion. Percentages indicate the proportion of that choice group (e.g., 49.7% of AI Choosers knew it was AI).
Choice Group Perception StateN% of Total % of Choice
AI Choosers Correctly identified as AI 235 29.4% 49.7%
Thought it was human 238 29.8% 50.3%
Subtotal 473 59.1% 100.0%
Human Choosers Correctly identified as human 232 29.0% 71.0%
Thought it was AI 95 11.9% 29.0%
Subtotal 327 40.9% 100.0%
selecting human content while believing it was AI (11.9%). In both cases, the participant willingly
chose an advertisement theyperceivedto be AI-generated. This suggests that for a substantial
segment of users, execution quality transcends origin concerns.
Qualitative analysis clarified the demographic divergence observed in the quantitative detection
data (Table 4). Younger participants, who were more accurate at spotting AI, tended to use language
emphasizing “vibe” and “aesthetic” with less concern for authenticity. In contrast, older participants
placed higher emphasis on “authenticity” and “natural qualities. ” Paradoxically, this search for
authenticity often led older participants to misidentify high-quality AI content as human (the
"Thought it was human" group), assuming that the sophisticated execution must have been human-
made.
, Vol. 1, No. 1, Article . Publication date: December 2025.

LLM-Generated Ads:
From Personalization Parity to Persuasion Superiority 17
5 DISCUSSION
Our investigation across two studies provides a comprehensive view of Generative AI’s role in
digital advertising. From text-based personalization (Study 1) to multimodal persuasion (Study
2), the results challenge the traditional assumption that human creativity is the gold standard for
marketing communication. Below, we discuss the implications of these findings through five key
questions.
5.1 Can LLMs Effectively Personalize at Scale?
The results from Study 1 suggest that the answer is a nuanced “yes, ” but it depends heavily on the
target trait. We observed that LLMs excelled at targeting theOpennesstrait. Participants high in
openness—who are naturally more receptive to novelty and innovation—responded significantly
better to AI-generated messages than generic ones. In this context, the LLM successfully mimicked
the creative flexibility required to engage this audience. However, the failure to generate effective
ads for theNeuroticismtrait highlights a fundamental psychological barrier rather than just a
model limitation. Despite the LLM technically following the prompt, the resulting ads did not
increase engagement for high-neuroticism individuals. This aligns withRegulatory Focus Theory
[24], which distinguishes between “promotion” and “prevention” orientations. While Openness is
apromotion-focusedtrait (seeking gain), Neuroticism is aprevention-focusedtrait (avoiding risk).
Consequently, simply mirroring the trait in ad copy—without explicitly signaling safety—likely
triggers defensive avoidance behaviors regardless of whether the author is human or machine.
Thus, while AI enables personalization at scale, it is not yet a universal key for all psychological
profiles.
Fig. 5. Qualitative drivers of preference. Participants preferring
AI (red) overwhelmingly citedColor/ToneandModel Quality,
whereas those preferring humans (blue) prioritizedAuthenticity
andClarity.
Fig. 6. Performance by principle. AI holds
a strong lead inAuthorityandConsen-
sus, but ties onScarcitydue to tactical
skepticism.
5.2 Is AI-Generated Content Superior to Human Creativity?
In the domain of persuasion principles (Study 2), AI did not merely compete with humans; it
significantly outperformed them. With an 18.2 percentage point advantage overall, and dominant
performance inAuthority(+26%) andConsensus(+25%), the data suggests that AI models have
internalized the structural rules of persuasion better than the average human creator. As shown in
Figure 5, qualitative analysis reveals that this superiority stems fromMessage Sophistication
andVisual Coherence. Participants frequently described AI ads as “inspiring, ” “elevating, ” and
“professional”. This supports the theory ofNarrative Transportation[ 21]—the AI was better at telling
a transformative story about the product rather than just describing it. Furthermore, the AI’s ability
, Vol. 1, No. 1, Article . Publication date: December 2025.

18 Meguellati et al.
to generate images that perfectly matched the textual “vibe” indicates that GenAI reduces the
friction between copy and art direction. This creates a high degree ofProcessing Fluency[ 2],
where the visual-textual alignment reduces cognitive load and acts as a heuristic cue for credibility.
However, this advantage was non-existent in theScarcitycondition, where AI and human ads
performed equally (Figure 6). This exception can be explained by thePersuasion Knowledge
Model (PKM)[ 17]. Scarcity tactics—such as “Act Now!” or “Limited Time Only”—are distinctively
overt attempts to curtail the consumer’s freedom to choose. Unlike the subtle cues of Authority,
Scarcity acts as apersuasion trigger: it alerts the user that they are being marketed to, causing
them to raise a “psychological shield” of skepticism. Once this resistance is activated, the execution
quality of the ad becomes irrelevant; the user resists thetacticitself, not the creator. Thus, while
AI can polish the aesthetics of urgency, it cannot bypass the structural resistance consumers have
developed toward high-pressure sales techniques.
(a) The Perception Paradox
 (b) Choice-Perception Flow
Fig. 7. Interaction between detection and preference. (a) AI preference drops when detected (21.2 pp penalty)
but remains above the human baseline (40.9%). (b) Attribution flow showing that AI preference is driven by
both those who were deceived and those who accepted the AI origin.
5.3 Does the “AI Perception” hinder User Trust?
A central concern in HCI is whether the revelation of non-human authorship breaks the social
contract of communication. Our data confirms the existence of aDetection Penalty; correctly
identifying an ad as AI-generated reduced preference by 21.2% as shown in Figure 7. This vali-
dates the “authenticity requirement” often discussed in marketing literature. However, a paradox
emerged: despite this penalty, the AI advertisementsstillwon. Even when participants knew they
were looking at AI, 50.3% preferred it over the human alternative. This phenomenon, which we
termQuality Resilience, suggests that the functional superiority of the content overrides the
negative bias associated with its origin. This hierarchy of effects can be mapped to theElabora-
tion Likelihood Model (ELM)[ 42], while the “source origin” (AI) acts as a negativeperipheral
cue, the superior “argument quality” (aesthetic appeal, aspirational messaging) serves as a dom-
inantcentral cuethat drives the final decision. For nearly half of the participants, the decision
was origin-independent; they prioritized the “what” over the “who, ” signaling a shift toward a
“Post-Authenticity” consumption model.
, Vol. 1, No. 1, Article . Publication date: December 2025.

LLM-Generated Ads:
From Personalization Parity to Persuasion Superiority 19
Fig. 8. Generational divergence in detection. Accuracy declines sharply with age, with digital natives (18-24)
achieving 73.0% accuracy while the 65+ cohort performs at chance level (48.3%).
5.4 Is Authenticity Still a Human Trait?
Perhaps the most surprising finding is the generational divergence in how authenticity is perceived
and detected (Figure 8).
Boomers (The Deceived):Older participants (65+), who placed the highest value on “genuine”
and “natural” qualities, frequently misidentified AI ads as human (Figure 8). Qualitative analysis
suggests they engaged in a heuristicHalo Effect[ 41]: they conflated high production quality with
human effort. They attributed the AI’s high-quality polish to “human thoughtfulness, ” effectively
using quality as a proxy for humanity and failing to spot the machine because it was “too good” to
look fake.
Gen Z (The Pragmatists):Conversely, younger participants (18-24) were significantly more
adept at spotting AI (73.0% accuracy) but judged ads based on “vibe” rather than authenticity. This
behavior aligns withUses and Gratifications Theory[ 30]: these users prioritize the immediate
gratification of the aesthetic experience over the provenance of the source. The “uncanny valley”
appears to be closing for this cohort, not because they are deceived, but because they have learned
to detach the artifact’s utility from its creator.
5.5 Limitations and Future Work
Our studies have some limitations that open directions for future research. Both samples were drawn
from online platforms in the United States, which limits cultural and regional generalizability. Real-
world advertising effects depend on repeated exposure, competing products, and actual purchasing
behavior, while our measures focused on single exposure preferences and self-reported intentions.
Methodologically, Study 1 examined only two personality traits and a single product category
with short textual messages and a fixed image. Other traits or product types may interact differently
with LLM-generated personalization. Study 2 explored four persuasion principles, but persuasion
theory includes many additional mechanisms that may show distinct patterns when instantiated by
AI. Our prompts and model choices were also conservative. We did not fine-tune models, optimize
prompts iteratively, or dynamically adapt content based on user feedback, which suggests that our
results are likely a lower bound on what such systems could achieve.
, Vol. 1, No. 1, Article . Publication date: December 2025.

20 Meguellati et al.
Future work can extend this line of research by testing multi-trait personalization, richer interac-
tion histories, and longitudinal outcomes such as trust, brand attitude, and perceived manipulation.
It will also be important to explore normative questions, such as when personality-based and
principle-based personalization crosses the line from beneficial tailoring to exploitative targeting.
Our findings indicate that, at least in controlled settings, AI-generated persuasion can already
compete with human creativity. The central question is no longer whether AI can persuade, but
how we choose to constrain and govern that capability.
6 CONCLUSION
This research investigated the capability of Large Language Models and diffusion models to generate
effective advertising content, comparing AI-generated assets directly against human-authored
counterparts across personality-based and principle-based frameworks. Our findings demonstrate
that these models have reached a threshold of creative utility where they can effectively rival, and
in specific contexts surpass, human expertise in ad creation.
In the domain of trait-based personalization, we observed that LLMs successfully generated
engaging content for individuals high in openness, yielding performance metrics statistically
equivalent to human writers. However, the efficacy of this matching is not universal; targeting
neuroticism proved ineffective for both AI and human creators. This highlights the inherent
challenge of engagingprevention-focusedtraits, where tailored stimuli are more likely to trigger
avoidance behaviors than engagement, regardless of the author’s origin.
When expanding the scope to multimodal advertisements based on persuasion principles, AI-
generated content demonstrated a clear performance advantage, achieving a 59.1% preference
over human-created advertisements. This superiority was most pronounced in advertisements
leveraging Authority and Consensus principles, suggesting that GenAI excels at synthesizing
markers of credibility and social proof to establish highprocessing fluency. However, this advantage
was non-existent in the Scarcity condition, indicating that AI cannot inherently overcome consumer
skepticism toward specific high-pressure tactics.
With reference to consumer perception, our results reveal a complex relationship between
detectionandpreference. While participants possessed only a moderate ability to identify AI-
generated content (58.4% accuracy), successful detection resulted in a significant penalty, reducing
the likelihood of preference by 21.2 percentage points. Yet, a critical paradox emerged: even when
correctly identified as artificial, AI advertisements maintained a majority preference share (50.3%)
against human benchmarks. This suggests that the execution quality of the content—its visual
coherence and message sophistication—possesses aQuality Resiliencethat can override the
negative bias associated with non-human authorship.
These findings signal a shift toward a “post-authenticity” advertising era, characterized by a
distinct generational divergence. Our demographic analysis revealed that while younger participants
acted aspragmatists, identifying AI but prioritizing aesthetic appeal over origin, older participants
frequently conflated high production quality with human authorship. As the younger cohort defines
the future market, the distinction between human and machine authorship is becoming secondary to
the quality of the experience, now that AI has demonstrated it can rival human creative proficiency.
The evidence suggests that GenAI has evolved beyond a simple productivity aid, establishing itself
as a sophisticated engine for production capable of delivering superior engagement outcomes.
Ultimately, this work documents a pivotal moment in the evolution of persuasive communi-
cation. The question is no longer whether artificial intelligence can match human creativity in
advertising—it can, and in measurable ways, it already exceeds it. The questions that remain are
societal: how do we ensure that these powerful capabilities serve consumer interests rather than
exploit psychological vulnerabilities? How do we balance personalization benefits against privacy
, Vol. 1, No. 1, Article . Publication date: December 2025.

LLM-Generated Ads:
From Personalization Parity to Persuasion Superiority 21
concerns and manipulation risks? And as the line between human and machine-generated content
continues to blur, what new frameworks for authenticity, trust, and creative attribution must we
construct? These are the challenges that will define the next chapter of AI-driven persuasion.
References
[1] Adam L. Alter and Daniel M. Oppenheimer. 2009. Uniting the Tribes of Fluency to Form a Metacognitive Nation.
Personality and Social Psychology Review13, 3 (2009), 219–235. doi:10.1177/1088868309341564
[2] Adam L Alter and Daniel M Oppenheimer. 2009. Uniting the tribes of fluency to form a metacognitive nation.Personality
and social psychology review13, 3 (2009), 219–235.
[3] Lisa P Argyle, Ethan C Busby, Joshua R Gubler, Alex Lyman, Justin Olcott, Jackson Pond, and David Wingate. 2025.
Testing theories of political persuasion using AI.Proceedings of the National Academy of Sciences122, 18 (2025),
e2412815122.
[4] Stéphane Aroca-Ouellette, Natalie Mackraz, Barry-John Theobald, and Katherine Metcalf. 2025. Aligning LLMs by
Predicting Preferences from User Writing Samples.arXiv preprint arXiv:2505.23815(2025).
[5] Jinheon Baek, Nirupama Chandrasekaran, Silviu Cucerzan, Allen Herring, and Sujay Kumar Jauhar. 2024. Knowledge-
augmented large language models for personalized contextual query suggestion. InProceedings of the ACM Web
Conference 2024. 3355–3366.
[6] Hui Bai, Jan G Voelkel, Shane Muldowney, Johannes C Eichstaedt, and Robb Willer. 2025. LLM-generated messages
can persuade humans on policy issues.Nature Communications16, 1 (2025), 6037.
[7] Simon Martin Breum, Daniel Vædele Egdal, Victor Gram Mortensen, Anders Giovanni Møller, and Luca Maria Aiello.
2024. The persuasive power of large language models. InProceedings of the International AAAI Conference on Web and
Social Media, Vol. 18. 152–163.
[8] Sébastien Bubeck, Varun Chandrasekaran, Ronen Eldan, Johannes Gehrke, Eric Horvitz, Ece Kamar, Peter Lee, Yin Tat
Lee, Yuanzhi Li, Scott Lundberg, et al. 2023. Sparks of artificial general intelligence: Early experiments with gpt-4.
arXiv preprint arXiv:2303.12712(2023).
[9] Yihan Cao, Siyu Li, Yixin Liu, Zhiling Yan, Yutong Dai, Philip S Yu, and Lichao Sun. 2023. A comprehensive survey of
ai-generated content (aigc): A history of generative ai from gan to chatgpt.arXiv preprint arXiv:2303.04226(2023).
[10] Jilin Chen, Eben Haber, Ruogu Kang, Gary Hsieh, and Jalal Mahmud. 2015. Making use of derived personality: The
case of social media ad targeting. InProceedings of the International AAAI Conference on Web and Social Media, Vol. 9.
51–60.
[11] Jin Chen, Zheng Liu, Xu Huang, Chenwang Wu, Qi Liu, Gangwei Jiang, Yuanhao Pu, Yuxuan Lei, Xiaolong Chen,
Xingmei Wang, et al . 2024. When large language models meet personalization: Perspectives of challenges and
opportunities.World Wide Web27, 4 (2024), 42.
[12] Robert B. Cialdini and Noah J. Goldstein. 2004. Social influence: Compliance and conformity.Annual Review of
Psychology55 (2004), 591–621. doi:10.1146/annurev.psych.55.090902.142015
[13] Robert B. Cialdini, Raymond R. Reno, and Carl A. Kallgren. 1990. A Focus Theory of Normative Conduct: Recycling
the Concept of Norms to Reduce Littering in Public Places.Journal of Personality and Social Psychology58, 6 (1990),
1015–1026. doi:10.1037/0022-3514.58.6.1015
[14] David M Condon. 2022. The SAPA Personality Inventory: An empirically-derived, hierarchically-organized self-report
personality assessment model. (2022).
[15] Berkeley J. Dietvorst, Joseph P. Simmons, and Cade Massey. 2015. Algorithm Aversion: People Erroneously Avoid
Algorithms After Seeing Them Err.Journal of Experimental Psychology: General144, 1 (2015), 114–126. doi:10.1037/
xge0000033
[16] Danny Driess, Fei Xia, Mehdi SM Sajjadi, Corey Lynch, Aakanksha Chowdhery, Brian Ichter, Ayzaan Wahid, Jonathan
Tompson, Quan Vuong, Tianhe Yu, et al. 2023. Palm-e: An embodied multimodal language model.arXiv preprint
arXiv:2303.03378(2023).
[17] Marian Friestad and Peter Wright. 1994. The persuasion knowledge model: How people cope with persuasion attempts.
Journal of consumer research21, 1 (1994), 1–31.
[18] Yao Fu, Hao Peng, and Tushar Khot. 2022. How does gpt obtain its ability? tracing emergent abilities of language
models to their sources.Yao Fu’s Notion(2022).
[19] Lewis R. Goldberg. 1993. The Structure of Phenotypic Personality Traits.American Psychologist48, 1 (1993), 26–34.
doi:10.1037/0003-066X.48.1.26
[20] Lewis R Goldberg et al. 1999. A broad-bandwidth, public domain, personality inventory measuring the lower-level
facets of several five-factor models.Personality psychology in Europe7, 1 (1999), 7–28.
[21] Melanie C Green and Timothy C Brock. 2000. Transportation into narrative worlds: The role of narrative transportation
in public policy.Journal of personality and social psychology79, 5 (2000), 701.
, Vol. 1, No. 1, Article . Publication date: December 2025.

22 Meguellati et al.
[22] Dhruv Grewal, Cinthia B. Satornino, Thomas Davenport, and Abhijit Guha. 2025. How generative AI is shaping the
future of marketing.Journal of the Academy of Marketing Science53 (2025), 702–722. doi:10.1007/s11747-024-01064-3
[23] Kobi Hackenburg, Lujain Ibrahim, Ben M Tappin, and Manos Tsakiris. 2025. Comparing the persuasiveness of
role-playing large language models and human experts on polarized US political issues.AI & SOCIETY(2025), 1–11.
[24] E Tory Higgins. 1997. Beyond pleasure and pain.American psychologist52, 12 (1997), 1280.
[25] Jacob B Hirsh, Sonia K Kang, and Galen V Bodenhausen. 2012. Personalized persuasion: Tailoring persuasive appeals
to recipients’ personality traits.Psychological Science23, 6 (2012), 578–581.
[26] Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las
Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, et al . 2022. Training compute-optimal large language
models.arXiv preprint arXiv:2203.15556(2022).
[27] Shaohan Huang, Li Dong, Wenhui Wang, Yaru Hao, Saksham Singhal, Shuming Ma, Tengchao Lv, Lei Cui, Owais Khan
Mohammed, Qiang Liu, et al. 2023. Language is not all you need: Aligning perception with language models.arXiv
preprint arXiv:2302.14045(2023).
[28] Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford,
Jeffrey Wu, and Dario Amodei. 2020. Scaling laws for neural language models.arXiv preprint arXiv:2001.08361(2020).
[29] Elise Karinshak, Sunny Xun Liu, Joon Sung Park, and Jeffrey T Hancock. 2023. Working with AI to persuade: Examining
a large language model’s ability to generate pro-vaccination messages.Proceedings of the ACM on Human-Computer
Interaction7, CSCW1 (2023), 1–29.
[30] Elihu Katz, Jay G Blumler, and Michael Gurevitch. 1973. Uses and gratifications research.The public opinion quarterly
37, 4 (1973), 509–523.
[31] Michal Kosinski, David Stillwell, and Thore Graepel. 2013. Private traits and attributes are predictable from digital
records of human behavior.Proceedings of the national academy of sciences110, 15 (2013), 5802–5805.
[32] Dokyun Lee, Kartik Hosanagar, and Harikesh S Nair. 2018. Advertising content and consumer engagement on social
media: Evidence from Facebook.Management Science64, 11 (2018), 5105–5131.
[33] Minqian Liu, Zhiyang Xu, Xinyi Zhang, Heajun An, Sarvech Qadir, Qi Zhang, Pamela J Wisniewski, Jin-Hee Cho,
Sang Won Lee, Ruoxi Jia, et al. 2025. LLM can be a dangerous persuader: Empirical study of persuasion safety in large
language models.arXiv preprint arXiv:2504.10430(2025).
[34] Jennifer M. Logg, Julia A. Minson, and Don A. Moore. 2019. Algorithm appreciation: People prefer algorithmic to human
judgment.Organizational Behavior and Human Decision Processes151 (2019), 90–103. doi:10.1016/j.obhdp.2018.12.005
[35] Michael Lynn. 1991. Scarcity effects on value: A quantitative review of the commodity theory literature.Psychology &
Marketing8, 1 (1991), 43–57. doi:10.1002/mar.4220080105
[36] Sandra C. Matz, Michal Kosinski, Gideon Nave, and David Stillwell. 2017. Psychological targeting as an effective
approach to digital mass persuasion.Proceedings of the National Academy of Sciences114, 48 (2017), 12714–12719.
doi:10.1073/pnas.1710966114
[37] Sandra C Matz, Michal Kosinski, Gideon Nave, and David J Stillwell. 2017. Psychological targeting as an effective
approach to digital mass persuasion.Proceedings of the National Academy of Sciences114, 48 (2017), 12714–12719.
[38] Sandra C Matz, Jacob D Teeny, Sumer S Vaid, Heinrich Peters, Gabriella M Harari, and Moran Cerf. 2024. The potential
of generative AI for personalized persuasion at scale.Scientific Reports14, 1 (2024), 4692.
[39] Elyas Meguellati, Lei Han, Abraham Bernstein, Shazia Sadiq, and Gianluca Demartini. 2024. How good are llms in
generating personalized advertisements?. InCompanion Proceedings of the ACM Web Conference 2024. 826–829.
[40] Huansheng Ning, Sahraoui Dhelim, and Nyothiri Aung. 2019. PersoNet: Friend recommendation system based on
big-five personality traits and hybrid filtering.IEEE Transactions on Computational Social Systems6, 3 (2019), 394–402.
[41] Richard E Nisbett and Timothy D Wilson. 1977. Telling more than we can know: Verbal reports on mental processes.
Psychological review84, 3 (1977), 231.
[42] Richard E Petty and John T Cacioppo. 1986. The elaboration likelihood model of persuasion.Advances in experimental
social psychology19 (1986), 123–205.
[43] Chanthika Pornpitakpan. 2004. The Persuasiveness of Source Credibility: A Critical Review of Five Decades’ Evidence.
Journal of Applied Social Psychology34, 2 (2004), 243–281. doi:10.1111/j.1559-1816.2004.tb02547.x
[44] Deeksha Prahlad, Chanhee Lee, Dongha Kim, and Hokeun Kim. 2025. Personalizing Large Language Models using
Retrieval Augmented Generation and Knowledge Graph. InCompanion Proceedings of the ACM on Web Conference
2025. 1259–1263.
[45] Filipe N Ribeiro, Koustuv Saha, Mahmoudreza Babaei, Lucas Henrique, Johnnatan Messias, Fabricio Benevenuto, Oana
Goga, Krishna P Gummadi, and Elissa M Redmiles. 2019. On microtargeting socially divisive ads: A case study of
russia-linked ad campaigns on facebook. InProceedings of the conference on fairness, accountability, and transparency.
140–149.
[46] Francesco Salvi, Manoel Horta Ribeiro, Riccardo Gallotti, and Robert West. 2025. On the conversational persuasiveness
of GPT-4.Nature Human Behaviour(2025), 1–9.
, Vol. 1, No. 1, Article . Publication date: December 2025.

LLM-Generated Ads:
From Personalization Parity to Persuasion Superiority 23
[47] Murray Shanahan. 2022. Talking About Large Language Models.arXiv preprint arXiv:2212.03551(2022).
[48] Michael Shumanov, Holly Cooper, and Mike Ewing. 2022. Using AI predicted personality to enhance advertising
effectiveness.European Journal of Marketing56, 6 (2022), 1590–1609.
[49] Somesh Singh, Yaman K Singla, Harini SI, and Balaji Krishnamurthy. 2024. Measuring and improving persuasiveness
of large language models.arXiv preprint arXiv:2410.02653(2024).
[50] Zhaoxuan Tan, Zheyuan Liu, and Meng Jiang. 2024. Personalized pieces: Efficient personalized large language models
through collaborative efforts.arXiv preprint arXiv:2406.10471(2024).
[51] Brian Jay Tang, Kaiwen Sun, Noah T Curran, Florian Schaub, and Kang G Shin. 2024. GenAI Advertising: Risks of
Personalizing Ads with LLMs.arXiv preprint arXiv:2409.15436(2024).
[52] Ross Taylor, Marcin Kardas, Guillem Cucurull, Thomas Scialom, Anthony Hartshorn, Elvis Saravia, Andrew Poulton,
Viktor Kerkez, and Robert Stojnic. 2022. Galactica: A large language model for science.arXiv preprint arXiv:2211.09085
(2022).
[53] Sarah Turnbull and Colin Wheeler. 2017. The advertising creative process: A study of UK agencies.Journal of Marketing
Communications23, 2 (2017), 176–194. doi:10.1080/13527266.2014.1000361
[54] Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma,
Denny Zhou, Donald Metzler, et al. 2022. Emergent abilities of large language models.arXiv preprint arXiv:2206.07682
(2022).
[55] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Ed Chi, Quoc Le, and Denny Zhou. 2022. Chain of
thought prompting elicits reasoning in large language models.arXiv preprint arXiv:2201.11903(2022).
[56] Stephan Winter, Ewa Maslowska, and Anne L Vos. 2021. The effects of trait-based personalization in social media
advertising.Computers in Human Behavior114 (2021), 106525.
[57] Stefanie Winter, Ewa Maslowska, and Anita L. T. Vos. 2021. Do you like what I like? Similarity in product rec-
ommendations increases conversions and improves attitudes.Computers in Human Behavior114 (2021), 106525.
doi:10.1016/j.chb.2020.106525
[58] Chenfei Wu, Shengming Yin, Weizhen Qi, Xiaodong Wang, Zecheng Tang, and Nan Duan. 2023. Visual chatgpt:
Talking, drawing and editing with visual foundation models.arXiv preprint arXiv:2303.04671(2023).
[59] Yiyan Xu, Jinghao Zhang, Alireza Salemi, Xinting Hu, Wenjie Wang, Fuli Feng, Hamed Zamani, Xiangnan He, and
Tat-Seng Chua. 2025. Personalized generation in large model era: A survey.arXiv preprint arXiv:2503.02614(2025).
[60] Wu Youyou, Michal Kosinski, and David Stillwell. 2015. Computer-based personality judgments are more accurate
than those made by humans.Proceedings of the National Academy of Sciences112, 4 (2015), 1036–1040.
[61] Sarfaroz Yunusov, Hamza Sidat, and Ali Emami. 2024. MirrorStories: Reflecting Diversity through Personalized
Narrative Generation with Large Language Models.arXiv preprint arXiv:2409.13935(2024).
[62] Brahim Zarouali, Tom Dobber, Guy De Pauw, and Claes de Vreese. 2022. Using a personality-profiling algorithm
to investigate political microtargeting: assessing the persuasion effects of personality-tailored ads on social media.
Communication Research49, 8 (2022), 1066–1091.
[63] Yijing Zhang, Dyah Adila, Changho Shin, and Frederic Sala. 2025. Personalize Your LLM: Fake it then Align it.arXiv
preprint arXiv:2503.01048(2025).
[64] Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang, Yupeng Hou, Yingqian Min, Beichen Zhang, Junjie
Zhang, Zican Dong, et al. 2023. A survey of large language models.arXiv preprint arXiv:2303.18223(2023).
[65] Thomas P Zollo, Andrew Wei Tung Siah, Naimeng Ye, Ang Li, and Hongseok Namkoong. 2024. Personalllm: Tailoring
llms to individual preferences.arXiv preprint arXiv:2409.20296(2024).
, Vol. 1, No. 1, Article . Publication date: December 2025.

24 Meguellati et al.
A Appendix: Qualitative Analysis of Participant Preferences
A.1 Thematic Analysis Methodology
To understand the underlying drivers of advertisement preference, we analyzed open-ended re-
sponses from participants across all four persuasion conditions. Responses were categorized using
an inductive thematic analysis approach, focusing on three primary dimensions: message content,
visual aesthetics, and perceived authenticity. This process yielded three dominant drivers of AI
success: Message Sophistication (mentioned in 38% of responses), Visual Coherence (32%), and
Psychological Precision.
A.2 Drivers of AI Superiority
The most significant differentiator for AI-generated content was the use ofaspirational messaging.
While human-authored advertisements were frequently described as “relatable, ” “simple, ” and
“direct, ” AI-generated narratives were characterized by participants as “inspiring” (36 mentions),
“elevating” (15 mentions), and “professional” (44 mentions). This suggests that the LLM success-
fully employednarrative transportation, moving beyond functional product descriptions to offer
transformative storylines that resonated with users seeking improvement or status.
In terms ofvisual coherence, participants consistently noted that AI-generated imagery achieved
superior integration with the textual message. Comments highlighted that AI advertisements
possessed better “color palettes” and “contrasts, ” with one participant noting the imagery set the
mood of a “professor’s lecture room, ” thereby reinforcing the Authority principle. Conversely,
human-created visuals were often criticized for lacking this cohesion, though they were praised for
appearing more “natural” and “pensive. ”
Table 6. Comparative Qualitative Feedback: Representative participant quotes contrasting AI and Human
advertisements.
Participants who Chose AI Participants who Chose Human
On Message Sophistication
“It speaks to how the product will improve
your life, not just who it’s made for. ”
“Felt more relatable and approachable. The
tagline is simple, direct. ”
“The captivating tagline and the imagery is
splendid and precise. ”
“More of a marketing slogan than a personal
message. ”
“More influencing than A which looks like
demanding. ”
“Too abstract and formal. ”
On Visual Presentation
“The color palette. The colors contrast bet-
ter. ”
“The thoughtful pose felt natural and invit-
ing. ”
“The image is more fitting with the text... the
overall darker colors give it the mood of a
professor’s lecture room. ”
“I like the contrast of colors. The image on
the right has too much brown. ”
“It is so clear and realistic. ” “Looks more pensive. ”
A.3 The Perception Paradox
Our analysis revealed a complex interaction between detection and preference. As detailed in Table
7, the largest sub-group of AI choosers (50.3%) believed the content was human-created, attributing
“genuine thoughtfulness” and “real human creativity” to the AI output. However, a substantial
, Vol. 1, No. 1, Article . Publication date: December 2025.

LLM-Generated Ads:
From Personalization Parity to Persuasion Superiority 25
group (49.7% of AI choosers) selected the AI advertisement despite correctly identifying its origin.
This indicates a shift towardQuality Resilience, where the sophisticated execution of the AI content
overrides the “authenticity penalty” usually associated with automated media.
Table 7. Perception Groups: Interaction between Origin Identification and Advertisement Choice.
Group Count % of Total Key Insight
Chose AI, Detected AI 235 29.4% Quality Resilience:Em-
braced sophistication
despite knowing origin.
Chose AI, Believed Human 238 29.8% The Deceived:Attributed
“genuine thoughtfulness” to
AI work.
Chose Human, Detected Human 232 29.0% Authenticity Seekers:Val-
ued “natural” qualities.
Chose Human, Believed AI 95 11.9% Avoidance:Selected per-
ceived lower-quality content
to avoid AI.
, Vol. 1, No. 1, Article . Publication date: December 2025.
