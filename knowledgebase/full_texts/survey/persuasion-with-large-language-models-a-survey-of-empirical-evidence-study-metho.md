---
title: 'Persuasion with Large Language Models: A Survey of Empirical Evidence, Study Methodologies, and
  Ethical Implications'
url: https://arxiv.org/abs/2411.06837
category: survey
subcategory: empirical
date: 2024-11
venue: arXiv (Cornell University)
authors:
- Sander Noels
- Alexander Rogiers
- Maarten Buyl
source: arxiv
pdf_url: https://arxiv.org/pdf/2411.06837
pages: 28
chars: 140772
fetched_at: '2026-11-08T12:57:06+00:00'
kb_version: 1
---

# Persuasion with Large Language Models: A Survey of Empirical Evidence, Study Methodologies, and Ethical Implications

PERSUASION WITHLARGELANGUAGEMODELS: A SURVEY OF
EMPIRICALEVIDENCE, STUDYMETHODOLOGIES,AND
ETHICALIMPLICATIONS
A PREPRINT
Sander Noels, Alexander Rogiers, Maarten Buyl, and Tijl De Bie*
AIDA-IDLab, Electronics and Information Systems, Ghent University
ABSTRACT
The rapid rise of Large Language Models (LLMs) has created new disruptive possibilities for per-
suasive communication, enabling fully-automated, personalized, and interactive content generation
at an unprecedented scale. In this paper, we survey the emerging field ofLLM-based persuasion,
reviewing empirical studies that measure the influence ofLLM Systemson human attitudes and
behaviors. We categorize applications across domains such as politics, marketing, public health,
e-commerce, and charitable giving, finding that such systems have frequently achieved human-level
or even superhuman persuasiveness. Synthesizing recent evidence, we identify key factors influenc-
ing this effectiveness, including the interaction approach, model scale and capability, prompt design,
personalization, and AI source disclosure. Furthermore, we critically examine the experimental de-
signs and success metrics used to evaluate these Systems, distinguishing between direct behavioral
outcomes and proxy indicators. Our survey suggests that the current capabilities of LLM-based
persuasion pose profound ethical and societal risks, including to information integrity, fairness and
inclusion, privacy, and individual autonomy. These risks underscore the urgent need for ethical
guidelines and updated regulatory frameworks to avoid the widespread deployment of irresponsible
and harmful LLM Systems.
1 Introduction
Persuasive communication, defined as “any message that is intended to shape, reinforce, or change the responses of
another, or others”, has existed both as a practice and as an academic discipline for many decades [77]. Until recently,
it has been the prerogative of humans to persuade others, initially through personal or small-group communication,
and later through mass-communication channels and technologies such as the printed press, radio, and television.
Since the rise of the internet, persuasion has become increasingly personalized, thus enhancing its reach and effec-
tiveness [34, 46, 43]. Whereas earlier mass-communication via printed or audio-visual media could be targeted only
to a limited extent based on the demographics of a communication channel’s audience, the internet allows far more
fine-grained personalization, in some applications even down to the individual.
With the advent of Large Language Models (LLMs), marked by the release of ChatGPT in 2022, a new era in persua-
sive communication has begun. In just a few years, LLMs have evolved from basic autoregressive text continuation
models to models with remarkable emergent capabilities.
We discuss an emergent capability with profound implications: their potential for intentionally generating human-
like content that shapes attitudes, informs opinions, and drives behaviors across various domains. This evolution
enables a significant change in the landscape of persuasion from selecting and presenting human-generated content,
albeit possibly in a personalized manner, to automatically generating tailored, context-aware, and hyper-personalized
messages at scale.
∗Corresponding author. E-mail: tijl.debie@ugent.be
arXiv:2411.06837v2  [cs.CL]  21 Apr 2026

Persuasion with Large Language Models: A SurveyA PREPRINT
LLM System
Response
Interaction Prompt Design Personalization
LLM
User
Proﬁle
2 1 4 5
3
User
Prompt of the LLM System
Model
Scale &
Capability
AI
Figure 1: Overview of factors influencing the persuasiveness of an LLM System: (1) the interaction approach (e.g.,
static vs. interactive), (2) the scale and capabilities of the model, (3) whether AI authorship is disclosed to users, (4)
the design of the prompt and associated persuasion strategies, and (5) the extent and method of personalization using
user data.
Several key characteristics makeLLM Systems, i.e., LLMs integrated with other technologies and deployed for specific
applications, particularly effective for persuasive communication. First of all, they allow for unprecedentedperson-
alization and adaptabilityas they excel at tailoring messages to individual preferences and psychological profiles,
creating targeted content that resonates with a targeted group or even a specific individual. Second and related to
this, LLM Systems appear capable ofexploiting cognitive biases and heuristicsthat make humans vulnerable to
persuasion and manipulation, thus allowing them to achieve persuasive impact beyond what was possible with classi-
cal scalable approaches. Third, they allow forinteractive conversations, enabling engaging experiences that can be
more effective than traditional one-way messaging. Fourth, despite known weaknesses of LLMs in terms of halluci-
nations, they are capable of a high degree ofmessage consistencyeven across a prolonged personalized interaction.
And finally, in comparison to other persuasion methods that share the previously mentioned characteristics, LLM
Systems are far morescalablebecause they can engage in hyper-personalized persuasive interactions at scale without
proportional resource increases.
During the past two years, these key characteristics of LLM Systems have led to the emergence of a new subfield of
persuasion research, which we refer to asLLM-based persuasion.
The effectiveness of LLM Systems for persuasion depends on various configurable factors, as illustrated in Figure 1.
These include the interaction approach (such as whether interactive dialogue is enabled), the scale and capabilities of
the language model employed, whether AI authorship is disclosed to users, the design of the prompt, and the extent and
method of personalization. Each of these factors can significantly impact the LLM System’s persuasive capabilities,
as we will discuss in detail in Section 4.
Purpose of this survey.Through a systematic review of peer-reviewed articles, conference papers, and reputable
industry reports published between January 2022 and October 2025, we provide a comprehensive overview of the
state-of-the-art in LLM-based persuasion. We examine the applications across various domains of LLM Systems for
persuasion, factors and design choices influencing their persuasiveness, the methodological techniques used to study
their persuasiveness and thereby quantify progress, and the associated ethical and regulatory challenges. Our survey
focuses on experimental studies that directly tested the persuasive capabilities of LLM Systems.
The rest of the paper is organized as follows:
• Section 2 defines the scope more formally, the inclusion criteria for the surveyed research, and the literature
search strategy employed.
2

Persuasion with Large Language Models: A SurveyA PREPRINT
• Section 3 reviews some of the commonly studied application domains of LLM-based persuasion, including
politics, marketing, public health, e-commerce, and efforts to combat misinformation.
• Section 4 analyzes the factors that influence the persuasive capabilities of LLM Systems, such as the interac-
tion approach, model scale and capability, AI source labeling, prompt design, and personalization.
• Section 5 examines the experimental designs employed in LLM persuasion studies, such as rigorous random-
ized controlled trials, and within- versus between-subject experimental designs. It details structural choices
regarding treatment and control conditions, the temporal dimension of measurement, and the emerging use
of synthetic simulations.
• Section 6 presents the success metrics used to evaluate persuasive LLM Systems, distinguishing direct per-
suasion outcomes from proxy indicators of persuasiveness, and summarizes the evidence comparing LLM
capabilities to human persuaders.
• Section 7 discusses the ethical considerations and regulatory landscape surrounding LLM-based persuasion.
• Section 8 concludes by summarizing key findings, identifying research gaps, and suggesting directions for
future work.
By mapping the current state of research on LLM-based persuasion, this survey aims to provide a comprehensive
overview of this rapidly evolving field. In doing so, we hope to raise awareness among researchers, practitioners,
policy makers, and the general public of the power of LLM Systems for persuasion today and in the near future, and
to point out the resulting ethical and societal challenges that lie ahead of us.
Table 1 provides an overview of the surveyed papers, showing for each paper the application domains it covered,
the influencing factors it studied, the experimental design it adopted, the success metrics used, and how persuasive it
assessed the investigated LLM System to be when compared to human persuasiveness.
2 Methodology
ScopeWe aim to consider literature that measures the persuasiveness ofLLM Systems, i.e., systems that deliver
LLM-generated text to humans through chatbots, social media bots, or other human-facing interfaces. While Section 1
provided a broad conceptual definition of persuasion, for the purposes of this survey we operationalizepersuasion
specifically as an intentional attempt to change a person’s attitudes, beliefs, or behaviour in a specified direction,
operationalized via human outcomes such as attitude or opinion change, choice or compliance, or scores on a validated
persuasion-related scale.
Eligibility criteriaWeincludepapers that satisfy all of the following criteria:
1. They use an LLM to generate text with the intention to persuade;
2. report a human-facing outcome (e.g., attitude/opinion shift, conversion/compliance, or a validated persuasion
scale) with sufficient methodological detail to assess the study design;
3. are first made public between1 Jan 2022and30 Oct 2025;
4. are indexed by Google Scholar;
5. are written in English.
We start from 2022 because this period marks the emergence and widespread deployment of modern conversational
LLMs, most notably with the release of ChatGPT in November 2022 [61]. We further include non–peer-reviewed
preprints that meet the above criteria, as the field is rapidly evolving and many relevant studies appear first on preprint
servers.
The criteria are intended toexcludepapers that (a) are theoretical or opinion-only pieces; (b) only measure persuasion
using intrinsic text properties (e.g., linguistic features) without a recipient response; (c) only employ algorithms that
recommend, but do not generate, text (such as social media ranking algorithms); (d) only measure effects adjacent to
persuasion, such as detecting whether text is AI-generated; or (e) focus on physically embodied LLM Systems, such
as hardware social robots.
3

Persuasion with Large Language Models: A SurveyA PREPRINT
Table 1: Summary of papers by Application Domains (Sec. 3), Influencing Factors (Sec. 4), Experimental Design
(Sec. 5), Success Metrics and Persuasiveness relative to human capabilities (Sec. 6). Filled circles ( ) indicate the
domain/factor/design/metric was explicitly studied in the paper.
Application Domains Influencing Factors Experimental Design Success Metrics Persuasiveness
Citation
(1) Public Health
(2) Politics
(3) E-commerce
(4) Misinformation
(5) Charity
(6) Interaction
(7) Model Scale
(8) AI Source Labeling
(9) Prompt Design
(10) Personalization
(11) RCT Design
(12) Between Subject design
(13) Within Subject design
(14) Human Control
(15) Pre-Post Measure
(16) Longitudinal Follow-up
(17) Belief Change
(18) Attitude Change
(19) Behavioral Intent & Action
(20) Source/Misinfo Detection
(21) Perceived Effectiveness
(22) Text/Comput. Indicators
(23) Superhuman
(24) On Par
(25) Inferior
(26) No Comparison
[1] # # #  # #  #  # # #  # # # # # #    # # #
[2] #  # # #  # #     # #  # #      # # #
[3]  # # # # # # # # # # # # # # # # # # #  # # # #
[4] #  # # # # # # # #   #   # #  #    #  # #
[5] #  # # # # # # # #   #   # #  #    #  # #
[6] # # # #  # # # # #   #  # # # #    # #  # #
[7] # # #  # #  #  #   #   #  # #  #  # # #
[8] #  # # # # # #  # # #  # # # # # # #   # # #
[12]   # # # # #  # #     # # # #    # #  # #
[13]  # # # # #  #  # # #   # # # # # #   #  # #
[14] #  # # # # # #  # #  #   # #  # # #  #  # #
[17] # #  # # # # # # # # # # # # # # #  #  # # # #
[18] #  # # # # #  # #   #    #  # # # # #  # #
[19] # # # # #   # # # # #  #  #   # # #  # # #
[20] #  # # # # # #   #   # # # # # # #   # # #
[21] #  # # # #  # #  # # #  # # # # # # #  #  # #
[22]  # # # # #  # # # # # # # # # # # # #  # # # #
[23] # # #  # # # # # #   # #    #  # # # # # #
[24]   # # # # # # # #   #  # #  #   #  #  # #
[25] #  # # #  # #     # #  #    # # # # # #
[26] #  # # # #  #  # #  #   # #  # # #  #  # #
[28] #  # # # #  #   # #   # # # # # #    # # #
[29] # # # # # #  #  # # #  # # # # # # #   # # #
[30] # #  # # # # # # # # # # # # # # # # #   # # #
[31]  # # # # # # # # # # # # # # # # # # #  # # # #
[32]  #  #  #  # # # #  # # # # # # #    # # #
[33] #  # # # # # #  #     # #   # #  # #  # #
[36]   # # # # # #     #  # # #  #  # #  # # #
[35] #  # # # # # #     # # # # #  #  # # # # #
[38] #  # # #   #     # #   #  # # #  # # #
[39] #  # # # #  # # #   #  # # #  #  #  #  # #
[37] #  # # # #  # # #   #  # # #  # # #  #  # #
[40] #  # # #  # # # #   #   # #  # # # # #  # #
[41]   # # # #  #  # # # # # # # # # # #   # # #
[45]    #  #  #  # # #   # # # # # #    # # #
[47]  # # # # # # # # # # #  #  #   # #   # # #
[48]  # # # # # #   #   #  # # # # # #    # # #
[49] # # # # # #  #   # #   # # # # # #    # # #
[50]  # # # #  # #  #   # #   # #  # # # # # #
[52]  # # # # # # # # # # #   # # # # # #    # # #
[53]  # # # # # #  # #     # # # # # #   #  # #
[54] #  # # # #  #     # #   #   #   # # #
[56]    # # # #       # # # # #  #  # # # #
[57] #   # # # # # #      # # # #  #  # #  # #
[58] # #  # # # # #   #    # # # #  #  # #  # #
[59] # # # # # # # #  #   # #  # #  # #  # # # #
[60] # # # #  # # #   #  # # # # # #  #  # # # #
[62] #  # # # # #  # #   #  # # # # # #   #  # #
[64] #  # #  #  #  # # #   # # # # # #   # # #
[65] #  # # # #  # # #   # #  # #   #   # # #
[66] # #  # # # # #  # # #  #  # # #  #   # # #
[69] # # # # # # # #  # # #  # # # # # # #   #  # #
[70] #  # # # # # # #    #   # #  #  #   # # #
[71]  # # # #  # #  #   # #  # #  # #   # # #
[72] # # # # # # #  # #     # # # #   #   # # #
[73] # # #  # # # # # #     # #  #   #   # # #
[74] # #  # # # # #  #  #   # # # #  #    # # #
[75] #  # # # #  #     # # # # # # # #   # # #
[76]  # #  # # # # # # # #    # # # #  # #  # # #
[78] # #  # # # #   #     # # # # # #  #  # # #
[79]   # # # # #   #   # # # # # # # #  # # # #
[80] #  # # #  # #   # #    # #  # # # #  # # #
[82] # #  # # # # # # #   # # # # # #    # # # #
[84] # # #  # #  #  # # #  #  # # #   #  # # #
[85]  # # # # # # #   # #  #  #    #  # # # #
[86]  # # # # # # #  # # #   # # # # # #  #  # # #
[87] # # # #  # # # # # # #  # # # # #  #  # # # #
[88]  #  # # # #  # #   #  # # # # # #  #  # # #
[90]  # #  # #  # # # # #   # # # # #     # # #
[89]  # #  # # # #  # # # #  # # # # #  #  # # #
4

Persuasion with Large Language Models: A SurveyA PREPRINT
Search strategyWe queried Scopus on 30 Oct 2025 with the following search string:
(“large language model” OR “LLM” OR “generative AI”)
AND (“persuasion” OR “persuasive” OR “debate” OR “persuasiveness”)
AND (“human” OR “user study” OR “randomized control trial”)
AND PUBYEAR > 2021 AND PUBYEAR < 2027
AND ( LIMIT-TO ( LANGUAGE , “English” ) )
This query returned4,783peer-reviewed articles (journal and conference papers) and4,171preprints (e.g., on arXiv).
Results were sorted by Scopus’ built-in relevance score. We then manually screened titles and abstracts of the top
200peer-reviewed articles and the top50preprints, stopping at these cut-offs because the yield of potentially relevant
studies dropped sharply in the lower-ranked results. During screening, we removed duplicates within and across the
two sets; when both a preprint and a peer-reviewed version of the same work were present, we retained only the peer-
reviewed version. The remaining unique studies that satisfied our eligibility criteria constitute the corpus synthesized
in this survey.
SynthesisFor each included paper, we extracted structured notes on the aspects most relevant to this survey: appli-
cation domain, influencing factors (including the direction and magnitude of persuasive effects), methodological setup
(e.g., experimental design, sample, and comparison conditions), success metrics, and overall conclusions regarding
persuasiveness. We then used these annotations to organize the literature along the dimensions discussed in the re-
mainder of the paper, most notably the application domains in Section 3 and the methodological and outcome-focused
analyses in later sections.
3 Application Domains
LLM Systems have been deployed across various domains to influence human behavior and attitudes. This section
examines five commonly studied application areas, each presenting unique challenges and opportunities for persuasive
AI.
3.1 Public Health
Public health applications (seecolumn (1) in Table 1) uniquely combine the need for scientific accuracy with persuasive
impact. Research in this domain has investigated LLM Systems ranging from automated message generators for social
media to fully interactive therapeutic agents.
Generating public health messagesA significant portion of research focuses on generating public health messaging
for mass communication. In the context of vaccination, Karinshak et al. [48] deployed GPT-3 to draft COVID-19
appeals, comparing them against official CDC messaging. This application extends to HPV vaccination, where Xia
et al. [86] used GPT-4 to address sensitive sub-topics like side effects and stigma. Beyond vaccines, Lim and Schmälzle
[52] utilized the open-source Bloom model to generate tweets about prenatal health (specifically folic acid), while
Lim and Schmälzle [53] examined the deployment of AI-generated health messages under different source disclosure
conditions.
Addiction and cessation assistantsMoving from general broadcasting to targeted interventions, several studies
have designed systems to assist with addiction and cessation. Calle et al. [13] investigated the use of LLMs to generate
smoking cessation intervention messages that meet clinical standards for smartphone delivery. Addressing digital
well-being, Wu et al. [85] developed ‘MindShift,’ a context-aware Android application that uses LLMs to analyze user
states and generate real-time interventions for problematic smartphone usage.
Promoting healthy lifestylesLLM Systems have also been applied to modify lifestyle and dietary behaviors through
various interaction modes. Karaka¸ s and Jaeger [47] utilized open-ended conversational interfaces to reduce psycho-
logical commitment to meat consumption. Taking a different approach, Sasaki and Inaba [71] investigated indirect
persuasion regarding nutritional advice by having users observe a peer AI accept advice, thereby triggering a confor-
mity effect. Matz et al. [56] further explored how such lifestyle messaging—across health and other domains—can be
personalized to individual psychological profiles.
Coaching and counsellingFinally, researchers are exploring the use of LLMs for sensitive subjects and prolonged
health and wellness engagement. Fetrati et al. [31] utilized LLM-based counseling to promote STI prevention among
5

Persuasion with Large Language Models: A SurveyA PREPRINT
young adults, deploying AI to discuss sensitive topics like HIV transmission. In the realm of mental wellness, Kumar
et al. [50] designed agents with sociable personas to improve engagement with mindfulness interventions over several
weeks. Expanding the scope to embodied interaction, Corrò and Chittaro [22] developed an LLM-controlled virtual
coach that monitors physiological signals to guide users through breathing exercises in real-time. In these advisory
roles, Böhm et al. [12] investigated how users perceive the competence of LLM Systems providing advice on personal
and societal challenges.
3.2 Politics
Political communication is a primary arena for LLM-based persuasion (seecolumn (2) in Table 1), where systems are
deployed to generate policy appeals, campaign materials, propaganda, and interactive debates.
Policy Statements and Legislative ArgumentsA foundational use case involves the generation of static arguments
supporting specific legislative measures or policy positions. Bai et al. [4] and Bai et al. [5] demonstrated that LLMs
could write short arguments supporting measures such as assault weapon bans and carbon taxes, effectively shifting
participants’ opinions. Similarly, Argyle et al. [2] used LLMs to influence policy attitudes on divisive issues like
immigration and education, while concurrently measuring impacts on voting intention. The quality of these AI-
generated arguments often rivals human output; Palmer and Spirling [62] found LLM-written arguments on U.S.
politics to be generally easier to read and more positive in tone than human versions, while Durmus et al. [26] showed
that advanced models like Claude 3 Opus produce arguments on emerging policy issues with persuasiveness similar
to human-written ones. While Teigen et al. [79] note that labeling these arguments as AI-generated can reduce their
persuasive impact, the capability remains robust. Hackenburg et al. [37] further quantified this in a large-scale study,
finding that a single static LLM message shifted policy attitudes by about 6 percentage points compared to controls.
Political Advertising and Campaign MessagingBeyond policy essays, LLM Systems are increasingly used to
generate and optimize campaign advertisements. In direct comparisons with human experts, Hackenburg et al. [36]
found that GPT-4’s political messages were about as persuasive as those of professional consultants, and often more
effective on right-leaning issues. Research has also focused on the potential for microtargeting these ads. Simchon
et al. [75] found that personality-matched political ads were judged to be more persuasive than generic ones and that
such personalization can be scaled automatically. However, results on the effectiveness of microtargeting are mixed;
Hackenburg and Margetts [35] found that while GPT-4 messages were broadly persuasive, microtargeted versions were
not necessarily more effective than high-quality generic messages. LLMs are also employed to analyze and optimize
the reach of campaign content. Meguellati [57] applied an LLM-based detector to election ads and found that ads
classified as “highly persuasive” attracted substantially more spending and impressions. Furthermore, Coppolillo et al.
[21] demonstrated that LLM agents can be fine-tuned to maximize content engagement within polarized communities;
using data from the Brexit referendum, they showed that even smaller, specialized models could generate highly viral
content adapted to the dominant sentiment of a social network.
Propaganda and DisinformationThe ability to generate persuasive text at scale has raised concerns about the
automation of propaganda and disinformation. Goldstein et al. [33] showed that GPT-3-generated propaganda articles
were highly persuasive and nearly as effective as human-written propaganda on the same topics. Highlighting a more
specific risk, Timm et al. [80] demonstrated that "threat actor" agents could be instructed to hallucinate plausible-
sounding statistics to support their arguments. When these fabricated stats were deployed in personalized debates, the
AI was significantly more successful at shifting user stances than standard human arguments, raising concerns about
the feasibility of automated, large-scale influence operations.
Interactive Debates and Voter EngagementMoving beyond static content, recent research investigated the use of
LLMs for interactive political dialogue and debating. In live multi-turn debates, Salvi et al. [70] found that a GPT-
4 agent was about as persuasive as a human opponent, and significantly outperformed humans when given minimal
personal information about the interlocutor. These effects appear to translate to real-world electoral contexts. Focusing
on the 2024 U.S. presidential election, Potter et al. [65] found that interactive dialogues shifted candidate preference,
with nearly 20% of Trump supporters reducing their support after the interaction. Similarly, Lin et al. [54] conducted
pre-registered survey experiments across three countries, finding that three-round AI dialogues significantly shifted
voter preferences and policy support with effects partially persisting for over a month. However, Chen et al. [18]
highlight the practical constraints of these interactive tools, estimating that while LLM chatbots are as persuasive as
human video ads on a per-person basis, the high cost of incentivizing voters to actually engage with a chatbot currently
limits their scalability compared to traditional broadcast media.
6

Persuasion with Large Language Models: A SurveyA PREPRINT
Depolarization and CounterspeechFinally, LLM Systems are being explored as tools to improve political dis-
course rather than just persuade. Taking an approach focused on depolarization, El Baff et al. [28] utilized LLMs to
rewrite "ineffective" arguments into versions specifically styled to resonate with liberal or conservative worldviews,
finding that these ideologically-tuned rewrites were rated significantly more effective than the originals. In the context
of online toxicity, Cima et al. [20] used LLMs to generate counterspeech in political Reddit communities; they found
that responses contextualized using conversation and user history were rated significantly more likely to persuade toxic
users to re-engage in civil discourse than generic AI responses.
3.3 E-commerce and Marketing
In marketing and e-commerce (seecolumn (3) in Table 1), LLM Systems are deployed to drive consumer decisions
and business outcomes. Research has investigated specific use cases ranging from interactive shopping assistants and
active sales agents to the generation of advertising content and the management of consumer complaints.
Shopping Chatbots and RecommendationsA primary application is the use of conversational agents to recom-
mend products and services. Chen et al. [17] showed that specific features of an AI shopping chatbot’s recommen-
dations increased users’ intention to adopt them, primarily by fostering cognitive and emotional trust. To enhance
the reliability of such systems, Furumai et al. [32] developed a zero-shot chatbot for travel recommendations that
grounds its suggestions in retrieved facts, improving persuasiveness while maintaining factual accuracy. Similarly,
Qin et al. [66] designed a conversational movie recommender that balances persuasiveness with credibility, ensuring
that explanations induce higher watching intentions without relying on hallucinations or deceptive claims.
Sales and NegotiationsBeyond standard recommendations, LLM agents are capable of handling complex negotia-
tion and sales tasks. Vahidov and Carbonneau [82] demonstrated that LLM-powered agents negotiating phone plans
achieved significantly higher prices than pre-scripted agents. Crucially, this increased yield did not alienate customers;
the LLM agent was rated as fairer and resulted in higher intentions to return. LLMs can also support human sales pro-
fessionals; Elhissoufi et al. [30] showed that GPT-4 could convert technical product specifications into structured sales
arguments that experts rated as highly coherent and aligned with customer motives.
Ads and CampaignsIn an early study, Zhang and Gosline [88] observed that ChatGPT-4-generated ads were judged
to be of higher quality than those created by human experts, although the gap reduced when revealing AI or human
authorship. LLMs also function as scalable copywriters capable of high degrees of personalization. Meguellati et al.
[58] and Meguellati [57] found that GPT-generated personalized ads performed comparably to human-written ones.
Matz et al. [56] demonstrated that personality-tailored ads generated by ChatGPT were more persuasive than non-
personalized versions, sometimes increasing willingness to pay.
Complaints HandlingFinally, LLMs are being applied to post-purchase interactions. Shin et al. [74] found that
LLMs can refine consumer complaints to be clearer and more professional, making them more likely to result in relief.
3.4 Mitigating and Generating Misinformation
Research in this domain investigates two opposing applications: the generation of deceptive content and the deploy-
ment of AI to detect or debunk it (seecolumn (4) in Table 1).
Generating misinformationOn the adversarial side, studies have modeled how LLMs can be used to generate
misinformation that mimics human credibility cues. Zhou et al. [89] examined the creation of AI-generated misinfor-
mation, noting e.g. its tendency for enhancing details and including cognitive processing expressions, communicating
uncertainties, and simulating personal tones and emotions, thus enhancing its credibility. Spitale et al. [76] tested the
generation of social media disinformation, finding that readers could not reliably distinguish it from human-authored
content. Beyond static text, Schoenegger et al. [73] investigated the use of LLMs to actively steer users toward incor-
rect answers in ‘cognitive illusion’ tasks, demonstrating a use case where the system significantly reduced participant
accuracy compared to control conditions.
Mitigating misinformationIn terms of mitigation, researchers have explored various specific interventions to
counter falsehoods. One prominent application is interactive debunking: Costello et al. [23] deployed GPT-4 Turbo to
engage conspiracy believers in personalized, multi-turn dialogues, a method that successfully reduced belief in spe-
cific conspiracies. Another application is automated fact-checking, where the specific style of the AI is scrutinized.
Zhou et al. [90] investigated the generation of fact-checks and rebuttals, finding that the “neutral” and “objective” tone
7

Persuasion with Large Language Models: A SurveyA PREPRINT
naturally adopted by LLMs can be an asset, as readers perceived these AI rebuttals as less accusatory and easier to
follow than human-written ones.
Detecting manipulative behaviorFinally, systems have been designed for the technical detection of manipulation.
For instance, Wilczy´nski et al. [84] proposed the use of LLMs as ‘Manipulation Fuses’—classifiers designed to verify
outputs—showing that models can be effectively deployed to detect and flag manipulative statements within a given
context.
3.5 Charity
Charitable giving and prosocial campaigns (seecolumn (5) in Table 1) pose unique persuasive tasks for LLM Systems:
motivating generosity without overstepping into manipulation. Research in this domain has primarily distinguished
between two main use cases: the use of LLM Systems for rewriting and fine-tuning persuasive messages, and the
deployment of fully interactive persuasive chatbots for soliciting charitable donations.
Writing campaign materialsThe first major use case involves using LLMs as drafting assistants to rewrite or co-
write static campaign materials. Pauli et al. [64] investigated the capability of LLMs to rewrite short texts, including
donation appeals, to modulate their persuasiveness level while preserving the core message. Similarly, Biswas et al.
[6] examined the use of multilingual LLM co-writing tools to assist human writers in crafting persuasive fundraising
advertisements for organizations like the World Wildlife Fund.
Soliciting donationsIn the context of interactive chatbots, researchers have investigated how conversational agents
can solicit donations through dialogue. Yoon et al. [87] explored multi-agent interfaces, designing a system where
two GPT-based chatbots represented Save the Children and UNICEF to promote donations interactively. Building
on this conversational approach, Furumai et al. [32] introduced PersuaBot, a multi-step LLM and retrieval pipeline
designed to generate factual, persuasive appeals specifically for donation solicitation. Other work has focused on the
internal mechanisms of such chatbots; Nezhad et al. [60] introduced a framework that dynamically switches between
specific persuasive strategies (e.g., logical vs. emotional appeals) based on real-time sentiment analysis, investigating
whether responsive adaptation allows agents to better navigate the donation conversation compared to static strategies.
Finally, Jin et al. [45] studied the potential of transfer learning in this context, demonstrating that their PersuGPT model
trained on diverse daily persuasion tasks was also effective in the charity domain, evaluated on thePersuasionForGood
benchmark [83].
3.6 Other Application Domains
Beyond the major categories discussed above, LLMs are being investigated in specialized verticals ranging from
professional services to environmental advocacy, as well as in domain-agnostic decision support. Here we briefly
discuss a few additional examples.
In theprofessional services sector, systems are being designed for high-stakes persuasive interactions. In thefinancial
domain, Kong et al. [49] applied reinforcement learning to the adversarial task of debt collection, optimizing dialogue
models to persuade users to repay overdue debts. In thelegal field, Schneiders et al. [72] explored the application
of LLMs for generating lay legal advice, investigating their persuasive influence across the subdomains of traffic,
planning, and property law.
Researchers are also exploring whether LLMs candrive pro-environmental behaviors and sustainable lifestyle
changes. Doudkin et al. [25] compared personalized chatbots to static text for encouraging sustainable daily habits,
such as reducing single-use plastics. Specific dietary changes linked to sustainability have also been a focus; Saenger
et al. [69] developed a framework to generate and evaluate arguments for veganism, while Karaka¸ s and Jaeger [47]
investigated whether brief conversations with ChatGPT-4o could influence beliefs regarding the necessity of meat
consumption.
Finally, some researchers are evaluating LLMs asdomain-agnostic tools for debate assistance and general knowledge
formation. Unlike targeted campaigns, these applications aim to help users navigate complex topics or update their
beliefs. Elaraby et al. [29] examined the use of LLMs for selecting the best argument from two given options, and
generating a persuasive rationale for the choice made. In the realm of general knowledge, Schoenegger et al. [73]
utilized a quiz-based framework to test AI persuasion on trivia, cognitive illusions, and future event predictions,
studying the system’s ability to steer participants toward specific answers.
8

Persuasion with Large Language Models: A SurveyA PREPRINT
4 Factors Influencing Persuasiveness
The effectiveness of LLM-driven persuasion is shaped by a complex interplay of factors. This section examines five
key elements identified in recent research that influence the persuasive capabilities of LLM Systems: the interaction
approach, model scale and capability, AI source labeling, prompt design, and personalization. Each factor represents
a different dimension of how LLMs can be designed or deployed to sway opinions or behavior. Note that Table 1
indicates only which studies experimentally vary a factor to measure its persuasive effect.
4.1 Interaction Approach
The degree of interactivity (seecolumn (6) in Table 1) in an LLM’s communication with users—ranging from one-shot
message delivery to multi-turn dialogues or debates—can markedly affect persuasive impact.
Many studies have used one-way, static message exposure in their designs: participants simply read an LLM-generated
message with no back-and-forth exchange. For instance, Bai et al. [4] had subjects read a persuasive political statement
generated by an LLM (GPT-3/3.5) and measured attitude change pre- vs. post-exposure, demonstrating that even a
single-shot AI message can shift opinions. Likewise, Simchon et al. [75] and Hackenburg and Margetts [35] each
evaluated persuasion by showing participants tailored political advertisements or essays and recording their immediate
effect; while these messages were sometimes microtargeted to user attributes, the communication remained non-
interactive. Such passive delivery approaches, including personalized ads in marketing contexts [58], dominate the
current literature due to the relative ease of testing one-shot persuasion. Variations within static delivery have also
been tested; for instance, Bai et al. [5] included a “human-in-the-loop” condition where participants selected the most
persuasive AI draft to show to others. Interestingly, this curated approach was not statistically more effective than the
raw LLM output, suggesting that human selection does not necessarily improve upon automated generation.
At the other end of the spectrum, research has explored interactive, multi-turn conversations and debates. In these
settings, the LLM System engages the user (or another agent) in a dialogue, adapting its persuasive strategy based on
the interlocutor’s responses. For example, Costello et al. [23] deployed GPT-4 in a three-round conversation to debunk
individuals’ conspiracy beliefs; the AI dynamically injected participant-specific content into each response, leading
to about a 21% reduction in belief adherence that persisted weeks later. Similarly, Salvi et al. [70] examined per-
suasion during live multi-turn debates between humans and an AI, finding that conversational dynamics significantly
influenced the AI’s success. Other studies have implemented chatbot-style interactions. Furumai et al. [32] had users
chat with an LLM through several simulated turns, and Yoon et al. [87] introduced multiple AI agents in a chatroom
to present information interactively. Expanding on these multi-agent dynamics, Sasaki and Inaba [71] introduced a
“peer” AI into a group chat; they found that users showed significantly greater attitude change when they observed this
peer agent being persuaded by the main AI, successfully leveraging the human tendency for social conformity. These
interactive approaches intuitively allow LLMs to address user doubts or counterarguments in real time, a capability
hypothesized by researchers such as Hackenburg and Margetts [35] and Durmus et al. [26] to enhance persuasion on
complex topics.
While early work often focused on either static or interactive modes in isolation, recent experiments have directly
compared the two, yielding mixed results regarding the inherent superiority of dialogue. Supporting the interaction
hypothesis, Hackenburg et al. [38] compared static messages against interactive dialogue within the same large-scale
experiment and found that while static messages were effective, the conversational AI was substantially more persua-
sive. However, other studies contradict this finding. Havin et al. [40] found that static paragraphs were just as effective
at shifting opinions as real-time conversation. Similarly, Argyle et al. [2] randomly assigned participants to receive
either a static message or engage in a six-turn chat (using direct argumentation or motivational interviewing) and found
that interactive conditions were no more effective at changing policy attitudes than a single, static generic message.
These discrepancies suggest that the specific design of the interactivity and the nature of the outcome measure are
critical. For instance, Kumar et al. [50] found that adding a sociable, interactive agent to static video content increased
user engagement, whereas a reflective questioning agent did not. Furthermore, when the bar is raised to behavioral
change rather than attitude shift, the mode of delivery may matter less; Doudkin et al. [25] compared static state-
ments against interactive chatbots for environmental advocacy and found that neither approach yielded significant
self-reported behavioral changes.
In summary, static messages offer simplicity and proven effectiveness, while interactive dialogues provide opportuni-
ties for adaptation that can—under the right conditions—drive stronger persuasion, though they are not a guaranteed
silver bullet.
9

Persuasion with Large Language Models: A SurveyA PREPRINT
4.2 Model Scale and Capability
Model scale (seecolumn (7) in Table 1) is a fundamental factor influencing persuasive capability. In general, larger
models tend to demonstrate more advanced language understanding, coherence, and reasoning, which can translate
into more convincing arguments. Multiple studies have observed that as LLMs increase in scale, their persuasive
power grows accordingly. For instance, Durmus et al. [26] found a clear scaling trend in persuasiveness: newer, more
capable models (e.g., Claude 3) produced arguments nearly as effective at changing opinions as human-crafted ones,
whereas smaller models (e.g., the compact Claude Instant 1.2) had significantly less impact. Similarly, Simchon et al.
[75] reported that ChatGPT (based on a more advanced GPT-3.5-tier model) achieved a stronger persuasive effect in
a political microtargeting task than its predecessor GPT-3. This trend holds for open-source models as well: Elaraby
et al. [29] found that Llama-2-70B-chat produced highly persuasive rationales, outperforming its 7B and 13B variants.
Qualitative differences in performance underpin these quantitative gains. Pauli et al. [64] observed that the smallest
model (7B parameters) was less effective at changing its persuasive language when instructed, whereas the larger
models more faithfully followed instructions to modulate their persuasiveness.
However, the relationship between model size and persuasive power is not linear. Evidence suggests diminishing
returns once models reach very large scales. In a massive between-model study, Hackenburg et al. [37] deployed a
range of LLMs from roughly 70 million parameters up to state-of-the-art models like GPT-4, and found that increases
in persuasiveness followed a sublinear pattern (approximately logarithmic) with respect to model size. Beyond a
certain threshold, additional model capacity yielded only modest gains in persuasive effectiveness.
This implies that while scaling up an LLM greatly boosts its basic language and reasoning abilities, beyond a point
other factors such as training data quality or specialized fine-tuning may play a larger role in further enhancing per-
suasiveness. Supporting this nuance, Hackenburg et al. [38] found that specific post-training techniques could allow
a smaller open-source model to match or outperform the persuasive capability of a much larger frontier model. Even
more strikingly, Coppolillo et al. [21] found that a small, 2B parameter model (Gemma-2B) fine-tuned specifically for
engagement maximization could outperform significantly larger state-of-the-art models, including LLaMA-3.1-70B
and ChatGPT-4o, in generating content that propagates through a social network.
In summary, while model scale is a crucial determinant of an LLM’s persuasive prowess, specialized training strategies
can allow smaller models to achieve comparable or even superior influence.
4.3 AI Source Labeling
AI source labeling (seecolumn (8) in Table 1) refers to whether the audience is told an AI system wrote the message
(e.g., labeled “AI-generated” vs. presented as human-written or with no attribution). Many studies have manipulated
this factor by giving identical content different source labels to test its influence on persuasion. A common finding is
that content explicitly labeled as AI-authored is often received with more skepticism and lower persuasiveness than
the same content attributed to a human.
For example, Böhm et al. [12] observed that revealing AI authorship led participants to rate the source as less com-
petent, even though the advice’s quality and their intention to use or share it were unchanged. Similarly, Karinshak
et al. [48] found that while a GPT-3 system could generate highly effective vaccine messages, participants expressed
a clear dispreference for those messages when they were labeled as coming from an AI rather than from human au-
thorities like the CDC. In the political domain, Palmer and Spirling [62] noted a slight drop in readers’ preference for
arguments when an “AI algorithm” was disclosed as the author. In the context of product and campaign ads, Zhang
and Gosline [88] observed that while ChatGPT-4-generated ads were judged to be of higher quality than those created
by human experts, revealing the authorship triggered a “human favoritism” bias, boosting the perceived quality of the
human-created ads and thereby reducing (though not reversing) the perceived quality gap. Teigen et al. [79] provided
further evidence: in a controlled experiment across multiple topics, arguments labeled as AI-authored were judged
significantly less persuasive than identical arguments labeled as human-produced (especially when the human source
was described as an expert). This finding echoes results in the legal domain, where Schneiders et al. [72] observed
a “superhuman” effect in which participants were more willing to act on LLM-generated advice than lawyer advice
when the source was hidden. However, this advantage evaporated when the source was labeled, demonstrating that AI
disclosure can nullify performance gaps favoring the LLM System.
Not all studies find a strong labeling penalty. For example, Matz et al. [56] report that any negative effect of AI
disclosure is minimal when messages are personality-tailored to recipients. In their experiments, AI-generated, trait-
matched messages were rated as similarly persuasive even when AI authorship was disclosed, raising the question
whether personalization might blunt disclosure penalties.
10

Persuasion with Large Language Models: A SurveyA PREPRINT
4.4 Prompt Design
Prompt design—the deliberate wording and context given to the LLM—significantly impacts the system’s persuasive
effectiveness (seecolumn (9) in Table 1). By adjusting how a request or instruction is framed, one can shape the tone,
style, and content of the AI’s output. This includes specifying a role or persona for the LLM (e.g., an expert or author-
itative figure), setting the desired tone (formal, empathetic, assertive), choosing a rhetorical framing (such as narrative
storytelling versus citing hard facts and statistics), providing examples (few-shot prompting), and giving direct in-
structions about the level of persuasion. Empirical studies demonstrate that careful prompt engineering across these
dimensions can substantially alter both the quality and impact of persuasive messages. We structure the discussion
around four key aspects: persona and tone, rhetorical strategy, structural guidance, and dynamic adaptation.
Persona and StyleInstructing an LLM to adopt a specific persona or style is a common technique to modulate
credibility or relatability. Metzger et al. [59] found that prompting for a low-authority communication style (using
so-called ‘powerless language’ by including hesitations, disclaimers, polite forms, etc) led users to trust the AI’s
messages less, which negatively affected persuasiveness as compared to an authoritative style. At the same time, an
overly assertive tone can backfire. In a study comparing donation chatbots framed as representatives of UNICEF and
Save the Children, Yoon et al. [87] found the UNICEF bot was rated slightly more persuasive. The authors suggest
this was not merely due to the organization, but because the Save the Children bot used a more forceful tone.
Rhetorical StrategyA significant body of research indicates that for LLMs, prompting for logical reasoning and
evidence is often superior to emotional appeals. Hackenburg et al. [38] tested eight distinct rhetorical strategies
and found that simply prompting the model to use “facts and evidence” was the most effective persuasive strategy,
outperforming other theoretically motivated strategies such as deep canvassing, storytelling, moral reframing, the use
of known debating techniques, or demonstrating that (important) others agree with the advocated position. Similarly,
Teigen et al. [79] observed that arguments were more persuasive when the prompt encouraged statistical rather than
narrative argumentation. This reliance on facts appears to be a core driver of LLM influence: Lin et al. [54] found
that when they prompted an LLM System to argue without using facts or evidence, its persuasive impact dropped
by more than half. This distinction may be specific to AI agents; Sun et al. [78] support a “matching” hypothesis,
demonstrating that while human persuaders are more effective when using narrative strategies, AI persuaders achieve
higher perceived usefulness when prompted to use informational strategies.
Beyond the broad distinction between logic and emotion, other specific rhetorical strategies and linguistic features
can be induced via prompting. Elaraby et al. [29] found that prompts instructing models to generate “contrastive”
rationales—those that explicitly refute the alternative option—significantly increased persuasiveness compared to ra-
tionales that only supported the chosen stance. Regarding linguistic complexity, Carrasco-Farre [14] shows that LLM
arguments generally tend to be more complex and moralized than human arguments, and that prompt style shifts these
features, though he does not compare persuasiveness across prompts.
Structural Guidance and ConstraintsProviding clear exemplars, context, or constraints within the prompt can
prime the model to produce stronger persuasive text. Goldstein et al. [33] demonstrated this in the realm of propa-
ganda: by giving GPT-3 a prompt that included a concise thesis statement and cleaned-up example articles, the LLM
System’s generated pieces became just as persuasive as real propaganda. In that study, an “edited” prompt with bet-
ter instructions and examples raised the persuasion rate of GPT-3 outputs to 46.4% agreement, essentially matching
the 47.4% induced by human-written propaganda. Similarly, Karinshak et al. [48] found that moving from a basic
zero-shot prompt to few-shot examples yielded more relevant outputs.
However, more engineering is not always better. Calle et al. [13] report that a brief, general prompt generated smoking-
cessation messages that more closely matched expert-written texts—and did so more efficiently—than longer, more
detailed instructions.
Direct Instruction and AdaptationFinally, direct instructions about the desired persuasiveness or goal have a
measurable effect. Pauli et al. [64] show that prompting LLMs to “be less persuasive” versus “be more persuasive”
produces noticeable shifts in output length and persuasiveness. Even stylistic edits can shift impact: Shin et al. [74]
had ChatGPT rephrase consumer complaints to be clearer and more professional; these edits significantly increased
the likelihood that evaluators would offer compensation. Moving beyond static instructions, prompting strategies can
be dynamic. Nezhad et al. [60] implemented a system that updates the specific instruction given to the LLM (e.g.,
changing from logical to emotional appeals) in real-time based on user feedback, thereby optimizing the rhetorical
framing for each conversational turn.
11

Persuasion with Large Language Models: A SurveyA PREPRINT
In sum, prompt design is a critical lever for LLM-driven persuasion. By carefully choosing the LLM System’s persona,
emphasizing evidence over emotion, and providing appropriate structural guidance, practitioners can dramatically
influence the character and impact of the messages produced.
4.5 Personalization
Personalization (seecolumn (10) in Table 1)—the tailoring of persuasive messages to individual user characteristics
or preferences—has been widely hypothesized to amplify persuasive impact, but empirical findings reveal a nuanced
picture about the extent to which this potential has already been realized using LLM Systems. Some large-scale stud-
ies have demonstrated only limited benefits from personalization. For example, in a preregistered political persuasion
experiment, Hackenburg and Margetts [35] reported that GPT-4 microtargeted messages (tailored using up to nine per-
sonal attributes) were no more effective on average than a well-crafted generic message. Similarly, Hackenburg et al.
[36] observed that aligning an LLM’s rhetoric with a user’s partisan identity yielded no consistent boost in persuasive
impact compared to non-aligned messages, possibly reflecting the model’s high baseline persuasiveness even without
fine-grained targeting. Also the recent large-scale study by Hackenburg et al. [38] only found a comparatively small
effect on persuasion when personalizing arguments based on user data. They had tried three approaches to person-
alization: prompt-based where the LLM is informed about the person’s initial attitude, using supervised fine-tuning,
and using a personalized reward model that selects the most persuasive messages for the person. In the context of
the Polish presidential election, Lin et al. [54] further questioned the necessity of microtargeting by experimentally
removing personalization; they found that broad, universal arguments were just as effective as personalized ones.
Other work points to mixed results that depend heavily on the specific traits targeted or the implementation method.
Meguellati et al. [58] found that customizing product ads to one personality trait (Openness) improved attitudes and
purchase intent, but no such benefit emerged for another trait (Neuroticism). Furthermore, Timm et al. [80] found
that while personalization alone could perform worse than a simple baseline, it became highly effective when used to
strategically tailor the delivery of statistics, suggesting that personalization is most powerful as a steering mechanism
for other techniques rather than as a standalone approach. There is also evidence of a gap between the predicted and
actual impact of these systems: Doudkin et al. [25] found that while synthetic user proxies predicted that personal-
ized chatbots would significantly boost pro-environmental behavior, actual human participants showed no significant
behavior change compared to non-personalized conditions. Consistent with this pattern, real-world persuasion studies
often find only modest, context-dependent treatment effects.
On the other hand, several studies do demonstrate clear advantages from tailored content in certain contexts. Costello
et al. [23] showed that personalized GPT-4 dialogues addressing participants’ own conspiracy beliefs reduced such
beliefs by approximately 21%, with effects persisting at 10-day and 2-month follow-ups. In a series of experiments
across marketing, health, and politics, Matz et al. [56] found that ChatGPT-generated messages adapted to individuals’
psychological profiles were generally more persuasive than unmatched or generic versions—even when AI authorship
was disclosed—though effect sizes varied by trait (stronger for Openness and Extraversion) and by domain. Personal-
ization strategies can also operate effectively at the community level; Coppolillo et al. [21] showed that an LLM agent
could maximize engagement by automatically sensing the dominant sentiment of a social network community (e.g.,
positive vs. negative opinion distribution) and adapting the tone of its content to match that consensus. Likewise,
Simchon et al. [75] reported that political ads tailored to recipients’ personality traits (notably Openness to Experi-
ence) produced small but measurable gains in perceived persuasiveness compared to nonpersonalized or mismatched
versions. Notably, personalization can be especially potent when combined with interactive or dynamic messaging. In
a live debate setting, Salvi et al. [70] gave an LLM access to basic demographic and ideological information about its
human interlocutor; this personalized approach significantly improved the AI’s success in shifting the human’s stance,
whereas providing the same background information to human debaters did not yield a benefit.
In summary, personalization has been shown to enhance the effectiveness of LLM-driven persuasion in certain sce-
narios—particularly when messages are closely aligned with an individual’s values, beliefs, or personality. However,
not all personalization studies demonstrated enhanced persuasiveness. Several studies suggest that a strong, generic
AI-generated message often persuades nearly as well as a personalized one [35, 36]. However, since personalization
provides strictly more degrees of freedom than a non-personalized approach,whetherpersonalization can boost per-
suasiveness is arguably not the most insightful research question. Instead, a more pertinent research question may be
whichpersonalization approach optimally leverages those additional degrees of freedom to yield maximal enhanced
persuasiveness, andby how muchpersuasiveness can be boosted in this way. We thus hypothesize that the negative re-
sults in the literature may reflect a lack of understanding of how to personalize effectively in the current state-of-the-art,
with the positive results suggesting substantial potential.
12

Persuasion with Large Language Models: A SurveyA PREPRINT
5 Experimental Design
The research on LLM-based persuasion spans a range of experimental study designs, each with different strengths
and weaknesses, and with different levels of rigor. A critical distinction is whether studies measure actual persuasive
impact, or whether they rely on participants’ subjective evaluations of persuasiveness. Given the importance of the
chosen success metric, and the broad diversity of how this choice was made in the surveyed literature, we discuss this
design aspect in a dedicated Sec. 6.
Methodologically, beyond the choice of the outcome measure or success metric, (ideally blinded)randomized con-
trolled trials (RCTs)are considered the gold standard for establishing causal persuasive effects. Although uncon-
troled or non-randomized experimental designs remain common and are often valuable for exploratory purposes, many
recent studies adopt this rigorous approach (seecolumn (11) in Table 1). For example, Costello et al. [23], Hacken-
burg and Margetts [35], and Salvi et al. [70] all implemented randomized experiments (often pre-registered) in which
participants were assigned to treatment and control conditions. Bai et al. [4] likewise conducted pre-registered RCTs
across multiple policy issues, measuring policy support before and after exposure to an AI-generated or human-written
message. In these designs, participants were often kept blind to key details to reduce bias. For instance, message au-
thorship was not revealed in Bai et al. [4], and Goldstein et al. [33] only debriefed participants about the propagandistic
source of texts after collecting their agreement ratings. RCT designs, when feasible, maximize internal validity and en-
able strong causal inference about an LLM’s persuasive impact. Moreover, they naturally allow for rigorous statistical
analysis to account for the inherent stochasticity of both human and LLM Systems’ behavior.
LLM persuasion studies varied along several other design dimensions. Most LLM persuasion experiments employed
abetween-subjectsdesign (seecolumn (12) in Table 1), meaning each participant was exposed to only one type
of persuasive intervention. This approach minimizes cross-condition influences (carryover effects) and prevents par-
ticipants from making direct comparisons across different interventions. In addition, many experiments employed
factorial designs to test multiple factors simultaneously. For instance, Teigen et al. [79] used a 4×2 between-subjects
design crossing source label (AI, Expert AI, Human, Expert Human) with argument framing (narrative vs. statistical)
to examine the interaction effects of these variables. Similarly, Havin et al. [40] employed a 2×2 design crossing dyad
type (human-human versus human-bot persuasion) with interaction mode (static versus dynamic communication).
Alternatively, researchers utilizewithin-subjectsdesigns, where the same participants experience multiple experi-
mental conditions (seecolumn (13) in Table 1). This design allows for direct comparison of how the same individual
responds to different interventions, effectively using each participant as their own control. For example, Lim and
Schmälzle [53] had each participant evaluate both an AI-generated and a human-written message under the same
disclosure condition. This mixed design enabled a within-person content comparison while still keeping the source-
disclosure manipulation between subjects. While such designs offer statistical efficiency and allow for comparative
judgments, researchers must carefully manage the risk of carryover bias and the potential for participants to guess the
study’s purpose.
Another critical design consideration was the inclusion of control conditions to serve as baselines. Many studies
included a no-message control group (participants who received no persuasive content) to measure the natural (drift
in) attitudes without any intervention. For example, in Goldstein et al. [33]’s propaganda experiment, roughly 24% of
respondents in a no-article control condition agreed with a thesis statement, compared to 47% after reading a human-
written propaganda article—a clear difference attributable to message exposure. In many studies though, ahuman
control conditionwas often added to benchmark an LLM’s persuasive efficacy against human-generated content (see
column (14) in Table 1). Bai et al. [4] and Durmus et al. [26] both compared AI-crafted messages with human-written
texts, and Hackenburg et al. [36] even tested GPT-4-generated messages against those written by professional political
consultants in a large multi-arm trial. In more interactive settings, researchers introduced alternative control formats;
for instance, Salvi et al. [70] included a human–human debate condition to contrast with AI-driven debate outcomes.
Likewise, some technical studies evaluated novel LLM-based systems against established baselines. For example,
Furumai et al. [32] compared their zero-shot persuasive chatbot to a state-of-the-art baseline model to contextualize
the performance gains.
Another consideration is when and how outcomes are measured. Nearly all experiments assessed persuasion immedi-
ately post-exposure, often by surveying participants’ opinions right after the AI interaction and comparing them to a
pre-intervention baseline from the same session. This immediatepre–post designcaptures the short-term persuasive
effect (seecolumn (15) in Table 1). However,longitudinal follow-ups(seecolumn (16) in Table 1) are rare. Notably,
Costello et al. [23] re-contacted participants about 10 days and again 2 months after an initial GPT-4 dialogue to see if
the reduction in conspiracy beliefs persisted over time, providing valuable insight into the durability of the AI’s per-
suasive impact. This finding is increasingly corroborated by other recent work in the political domain. Lin et al. [54]
and Hackenburg et al. [38] both re-contacted participants at least one month after an initial dialogue, confirming that
13

Persuasion with Large Language Models: A SurveyA PREPRINT
an important part of the shifts in respectively candidate preference and political attitudes persists over time. Chen et al.
[18] observed similar durability in policy attitudes over a five-week follow-up. Beyond attitude change, longitudinal
designs have also been applied to behavioral maintenance in field settings. Wu et al. [85] tracked participants over a
five-week period to measure sustained engagement, while Kumar et al. [50] conducted a three-week RCT showing that
a “friendly” LLM companion helped sustain user interaction with mindfulness exercises over the multi-week period.
By and large, though, current LLM persuasion studies prioritize tight experimental control and internal validity in their
setups, while the longer-term persistence of AI-driven persuasion (and other ecologically realistic factors) remain less
explored. The field would benefit from more such robust designs and follow-up measurements to fully understand not
only whether an LLM System can persuade in a single encounter, but also how lasting and generalizable those effects
are.
Finally, a distinct and emerging design pattern involves fully synthetic simulations, where human participants are re-
placed by LLM-driven “user agents.” This approach allows researchers to test persuasion strategies at a scale and
speed impossible with human subjects. For instance, Breum et al. [8] simulated dialogues between a persuader and
a skeptic agent to measure stance changes. Expanding on this, other researchers have developed sophisticated frame-
works to systematically study the mechanics of belief updates. Ramani et al. [67] developed a “Persuasion Game”
framework using 25 distinct LLM-driven personas with specific demographic profiles and emotional states, while Roy
[68] adopted a similar “convincer-skeptic” framework populated by 18 diverse personas to study demographic and
ideological alignment. Liu et al. [55] applied this method to safety research, simulating target agents with specific
psychological vulnerabilities to test susceptibility to unethical persuasion. Bridging this agent-based approach with
human research, Sasaki and Inaba [71] utilized a similar LLM “peer” persona alongside real participants, demonstrat-
ing that humans will actually conform to the behavior of a synthetic agent. Buyl et al. [11] investigated how notions of
‘trust’ can be built between LLMs, and how such a trust relation can affect an LLM’s susceptibility to persuasion and
its propensity to collaborate financially. While these synthetic designs offer rapid prototyping and assessment of per-
suasive tactics, they rely on the assumption that LLM user agents accurately model human psychology and resistance
mechanisms.
6 Success Metrics for Persuasive LLM Systems
To evaluate how persuasive an LLM System is, researchers employ a variety of success metrics. Fundamentally,
persuasion success is defined by a measurable change in a participant’s belief, attitude, or intended behavior after
exposure to content generated by the LLM. These direct outcomes (actual shifts in beliefs, attitudes, or behavioral
intentions) provide the clearest evidence of persuasion. In addition, many studies record proxy metrics—indirect
measures like perceived message quality, source credibility, or user engagement—which can suggest persuasiveness
but do not by themselves prove that any opinion or behavior changed. This section categorizes success metrics into
those direct persuasion outcomes versus various proxy indicators, with definitions and examples from recent LLM
persuasion research in each category.
6.1 Primary Persuasion Outcomes
Primary persuasion outcomes refer to direct evidence that an LLM’s message affected participants’ internal states or
behaviors. Typically, studies capture these effects by comparing a person’s responses before and after the persuasive
message or by contrasting outcomes between a group that saw the AI content and a control group that did not (see
Sec. 5). Key primary outcomes include belief change, attitude change, and behavioral intention or action, as defined
below.
6.1.1 Belief Change
Belief change denotes shifts in what participants accept as true or how strongly they agree with specific factual or
speculative statements after interacting with an LLM (seecolumn (17) in Table 1). For example, studies on misinfor-
mation debunking measure persuasion by how much participants’ belief in a false claim decreases due to an AI-driven
intervention. In one study, participants rated their agreement with various conspiracy theories on a 0–100 scale before
and after a tailored GPT-4 chat; the AI dialogue induced a 20% reduction in belief in the conspiracy theory [23].
Goldstein et al. [33] showed that reading a GPT-3-generated propaganda article raised agreement with the article’s
thesis to 43.5%, up from 24.4% in a no-exposure control group. Borah et al. [7] revealed that people make more
mistakes assessing the veracity of rumors and headlines when LLM-generated supporting and refuting statements are
provided as well, with notable variation across demographic segments (e.g., age, gender). However, the persuasive
influence of LLMs is not uniform across all types of beliefs. Karaka¸ s and Jaeger [47] found that while an LLM con-
versation successfully reduced beliefs that eating meat is ‘necessary’ or ‘natural,’ it failed to alter beliefs that meat
14

Persuasion with Large Language Models: A SurveyA PREPRINT
is ‘nice’ or ‘normal’, suggesting LLMs may be more effective at shifting argumentative justifications than subjective
preferences. Finally, in the context of behavioral health, belief change can also refer to self-efficacy—a user’s belief in
their capacity to execute behaviors. Wu et al. [85] found that users interacting with their LLM-based system reported
significantly higher self-efficacy scores regarding their ability to control smartphone usage compared to those using a
baseline static reminder system.
6.1.2 Attitude Change
Attitude change refers to a shift in a participant’s feelings or stance toward an issue, person, or policy after exposure to
the LLM’s message (seecolumn (18) in Table 1). Researchers often measure this by using opinion scales, measuring
the level of agreement or support on a Likert or percentage scale. For example, Hackenburg and Margetts [35] found
that a single GPT-4-generated message increased policy support compared to a no-message control group. Similarly,
Bai et al. [4] observed a reliable increase in policy support after participants read an LLM-generated political appeal. In
the context of elections, Potter et al. [65] utilized a voting simulation to measure shifts in candidate leaning following
a conversation of five exchanges with an LLM. Durmus et al. [26] employed a pre-post design where participants
indicated their stance on various social issues on a 1–7 scale, read a short argument, and finally rated their stance again.
In a live debate experiment, Salvi et al. [70] measured agreement before and after each debate and inferred attitude
change by comparing the change between those who debated an AI versus a human. Beyond political and social issues,
attitude change metrics can also track shifts in psychological states; for instance, Wu et al. [85] measured the reduction
in Smartphone Addiction Scale (SAS) scores after users interacted with an LLM-driven intervention system. Across
these studies, a change in attitude—whether measured within-person or across groups—is treated as strong evidence
that the LLM System was persuasive.
6.1.3 Behavioral Intention and Action
Beyond beliefs and attitudes, persuasion ultimately aims to influence what people intend to do or actually do (seecol-
umn (19) in Table 1). Thus, many LLM persuasion studies examine changes in behavioral intentions (and occasionally
real behaviors) after exposure to messages—outcomes often called “mobilization” effects. These behavioral intentions
may pertain to purchasing a product, donating to a cause, following advice, or other actions relevant to the persuasive
message. Ideally, researchers capture concrete or incentivized behaviors, since purely hypothetical intentions can be
unreliable predictors of real actions.
For example, Böhm et al. [12] tested whether disclosing a message’s AI origin would affect people’s willingness to
follow the given advice. Similarly, in the legal context, Schneiders et al. [72] utilized a specific behavioral intention
metric: “willingness to act” on provided legal advice. In e-commerce and entertainment contexts, researchers have
examined how AI influences consumption decisions. Chen et al. [17] examined whether an AI shopping assistant’s
product recommendations increased users’ adoption intentions. Qin et al. [66] quantified persuasion as the change in
a user’s “watching intention” toward a movie before and after receiving an LLM-generated explanation, effectively
measuring the system’s ability to move a user from disinterest to intended consumption. Similarly, Meguellati et al.
[58] measured purchase and engagement intentions for personalized ads written by GPT-3.5 versus human ads and
found similar results for matched personalities. Moving beyond purchase intentions to negotiated outcomes, Vahidov
and Carbonneau [82] found that an LLM-powered sales agent secured higher final agreement prices than a baseline
agent using canned text.
Some experiments go further by observing actual choices or incentivized behaviors. For instance, Schoenegger et al.
[73] compared LLMs against humans in a financially incentivized quiz setting; they found that LLMs successfully
drove participants to select specific answers more effectively than human persuaders. Yoon et al. [87] built a multi-
chatbot donation system and recorded participants’ chosen charity and intended donation after chats with two AI
agents. In public-good campaigns, Matz et al. [56] ran experiments measuring willingness-to-pay or willingness-to-
donate, and AI-generated messages tailored to participants’ psychological profiles sometimes increased these amounts,
but behavioral effects were smaller and less consistent than perceived persuasiveness. Also Biswas et al. [6] utilized
an incentivized donation game to measure persuasion.
Notably, a few studies have documented real-world behavioral changes due to LLM assistance. Shin et al. [74]
analyzed consumer complaints and found those likely aided by an LLM had approximately 10 percentage-point higher
relief rates than traditionally written complaints. In experiments, evaluators reading complaints edited by ChatGPT
for clarity, coherence, and professionalism were more likely to lead to compensation. In the health domain, Kumar
et al. [50] conducted a three-week deployment where a sociable LLM agent significantly increased participants’ actual
initiation and completion rates of daily mindfulness exercises.
15

Persuasion with Large Language Models: A SurveyA PREPRINT
In summary, changes in what people intend to do (e.g., purchase, donate, comply) or actually do (when observable)
are critical metrics of persuasive success. Because measuring real behavior in controlled studies can be challenging,
many papers rely on self-reported intentions as a proxy; however, whenever possible, observing actual choices or
incentivized decisions provides stronger evidence that an LLM’s influence moved beyond opinions and into actions.
6.2 Proxy Metrics of Persuasiveness
In addition to outcome measures that capture genuine opinion or behavior change, researchers often evaluate a range
of proxy metrics to gauge an LLM System’s persuasive performance. These proxies do not directly demonstrate that
anyone was persuaded, but they shed light on how the message was received and the factors that might facilitate
persuasion. Common proxy metrics include perceived persuasiveness of the message (how convincing or effective
it seems), source credibility and trust in the LLM System, participants’ ability to detect AI-generated or misleading
content, and various text-based features or computational measures of the messages themselves. High scores on these
measures can correlate with successful persuasion, but they must be interpreted with caution since a message might
score well on proxies yet ultimately fail to change attitudes or behavior.
6.2.1 Perceived Effectiveness
This category encompasses participants’ subjective evaluations of the message’s convincingness or quality. We can
distinguish a few related types of perception-based measures (seecolumn (21) in Table 1).
Agreement-Aligned JudgmentsThese capture the participant’s immediate alignment with the particular message
presented. For example, right after reading an AI-generated message, participants might be asked, “How much do
you agree with the claim?” or in a comparative setup, “Which of these two arguments is more convincing?” Such
questions gauge whether the person finds the particular message agreeable, often in direct comparison with other
messages. Pauli et al. [64], Breum et al. [8], and Saenger et al. [69] used this approach by asking crowd workers to
read pairs of texts and indicate which one was more persuasive, aggregating comparisons to estimate persuasiveness.
Similarly, in a marketing study, Meguellati et al. [58] presented participants with four advertisements (some AI-written,
some human-written) and recorded which ad each person clicked on as an indicator of which message they found most
compelling. In politics, Palmer and Spirling [62] had judges pick the more convincing human or open-source LLM
arguments; without labels choices were about even, and labeling ‘AI’ slightly increased preference for the human.
Message-Level Effectiveness/QualityThese measures ask participants to assess the strength or persuasiveness of
the message itself,independent of their personal agreement. For instance, participants might rate on a Likert scale how
“persuasive,” “effective,” “convincing,” or “well-argued” a message was. Many studies have included such questions
to evaluate AI-generated content across various domains. In health communication, Lim and Schmälzle [53] had
participants rate vaping prevention messages; unlabeled AI-generated messages scored higher than human tweets, and
‘AI-generated’ labels slightly lowered AI ratings and narrowed the gap. Similarly, Lim and Schmälzle [52] found that
evaluators consistently rated AI-generated folic acid awareness messages as significantly clearer and higher in quality
compared to a benchmark of highly retweeted human messages. Likewise, Karinshak et al. [48] had participants
evaluate the quality of vaccine promotion messages, and the GPT-3-generated messages scored higher on standard
perceived persuasiveness scales and argument strength than did official messages from the U.S. CDC.
Researchers used similar evaluations for political messaging. Simchon et al. [75] asked users to rate the persuasiveness
of political ads right after exposure to compare tailored versus untailored ads. Investigating political argumentation,
El Baff et al. [28] asked evaluators to rate the effectiveness and clarity of arguments, finding that LLM-generated
rewrites consistently achieved higher quality scores than the original human-authored texts. High ratings on these
message-level metrics indicate that the audience found the content compelling or well-crafted. However, it is important
to note that a message can be rated very persuasive in principle yet still fail to change the reader’s own stance—so these
metrics, while informative, do not confirm an actual attitude shift. To understand the rationale behind such ratings,
some researchers combine scales with qualitative inquiry. For instance, Ataguba et al. [3] conducted semi-structured
interviews alongside a persuasiveness scale for AI-generated dietary plans; they found that while users rated the system
as persuasive due to its flexibility and personalization, the qualitative feedback uncovered specific deficits in trust and
cultural relevance that a simple numeric score might obscure.
Source Credibility (Trust/Competence):Rather than focusing on the message itself, these metrics gauge how the
audience perceives the communicator (in this case, the LLM System or its persona). Participants may be asked about
their trust in the source, its expertise, honesty, or other credibility factors. The underlying premise is that a source
deemed more credible and trustworthy will be more persuasive. For example, Karinshak et al. [48] measured and as-
16

Persuasion with Large Language Models: A SurveyA PREPRINT
sessed trust in the source of pro-vaccination messages. They found that AI-generated messages received higher ratings
for effectiveness, argument strength, and attitude positivity than messages created by doctors and the CDC. However,
when the source was revealed, study participants rated AI-generated messages lower than the human-generated ones,
reflecting the lower trust in AI as the message source. In another study, Böhm et al. [12] found that disclosing AI
authorship lowered perceived competence but did not reduce willingness to follow the advice.
Perceived expertise plays a role too: Teigen et al. [79] demonstrated that an argument labeled as written by an “AI
expert” was still rated as less persuasive than the same text labeled as coming from a human expert, highlighting a
credibility gap for AI in the eyes of the audience. Qualitative evidence supports this reliance on human expertise;
Ataguba et al. [3] found that users were hesitant to trust ChatGPT’s dietary plans specifically because they lacked
cited sources or verification, stating they would only follow the advice if endorsed by a human professional. Several
studies also measure how human-like or natural the AI’s communication appears, under the hypothesis that a more
conversational, human-seeming AI might engender greater trust. Vahidov and Carbonneau [82] support this hypothesis
in a negotiation context, finding that users perceived an LLM agent as significantly “fairer” than a script-based bot.
Perceived empathy is another critical dimension of source credibility; Nezhad et al. [60] found that an adaptive chatbot,
which adjusted its strategy based on user sentiment, received significantly higher empathy ratings than a static baseline,
hence facilitating persuasion. Overall, high trust and credibility scores for the AI source often correlate with greater
influence. For example, Chen et al. [17] showed that trust mediated the effect of recommendation cues on users’
intention to adopt the chatbot’s recommendations. Similarly, Metzger et al. [59] found that high-authority language
increased trust and, via trust, acceptance.
Nonetheless, these are supporting indicators: a participant might find the AI agent friendly and knowledgeable yet
remain unconvinced on the issue. Thus, source credibility metrics are best viewed as factors that can facilitate persua-
sion, rather than proof that persuasion occurred. A series of experiments by Zhang and Gosline [88] underlines this
nuance: they found that AI-generated marketing and advocacy content were rated higher in quality than human-written
content when the source was not revealed, but once people were told who (or what) created each message, they exhib-
ited a “human favoritism” bias—evaluating the same content more favorably if they thought a human wrote it. This
bias in perceived quality did not completely eliminate the appeal of AI content, but it shows that audience perceptions
of source can influence the judged effectiveness of a message independent of its actual persuasive merits. Conversely,
the persuasive outcome can also retroactively shape trust in the AI. Potter et al. [65] documented a “spillover effect”
where participants who were persuaded by the LLM tended to feel more favorable toward AI, whereas those who
resisted the persuasion developed a more negative view, effectively polarizing attitudes towards the technology based
on the interaction’s success.
6.2.2 Source or Misinformation Detection Accuracy
Some studies include metrics to see if participants can discern attributes of the content, such as whether it was AI-
generated or whether it contains misinformation (seecolumn (20) in Table 1). These measures are not persuasion
outcomes per se, but they relate to transparency and could modulate the impact of the message (e.g., undetected
AI-written content might persuade more easily, and undiscovered falsehoods can be more influential). A common
approach is to test AI-vs-human source recognition: after reading a piece of text, can users correctly identify if it was
written by a machine or a human? Another is truthfulness detection: can users tell if the content is factually accurate or
deceptive? For example, Spitale et al. [76] showed participants a series of social media posts and asked them to judge
each post’s origin and veracity. Participants were unable to reliably discern AI-generated posts from human-written
ones. They did better at spotting misinformation, but importantly, GPT-generated falsehoods were slightly more likely
to fool readers than human-written ones.
In a related vein, Zhou et al. [89] investigated automated detection of AI-created misinformation by compiling a dataset
of paired COVID-19 misinformation items (news and social posts): human-generated and matching AI-generated
items. They found that models for the detection of misinformation achieved a significantly reduced performance on AI-
generated misinformation when compared to human-created misinformation. This detection challenge is exacerbated
by the ability of LLMs to generate varied iterations of the same core message. Dash et al. [24] highlight the threat
of “AIPasta,” where LLMs paraphrase disinformation campaigns to evade detection. By using varied wording to
bypass duplicate-content filters while keeping the original meaning, these messages may allow bad actors to scale
the “illusory truth effect” without triggering the spam algorithms that usually catch exact copies. This vulnerability
extends to the LLM Systems themselves when they are deployed as fact-checkers or evaluators; Agarwal and Khanna
[1] demonstrated that in single-turn debates, LLM judges can be persuaded to select a known falsehood over the truth
if the misinformation is delivered with high confidence and sufficient rhetorical flair, effectively overriding the model’s
factual knowledge.
17

Persuasion with Large Language Models: A SurveyA PREPRINT
Many persuasion studies have noted that human participants often fail to realize they are reading AI-generated text
at all. Bai et al. [4] reported that roughly 94% of respondents who read a GPT-written political messages believed it
was human-written. From a metrics standpoint, detection accuracy may be an informative proxy: if users cannot tell a
message is AI-created or cannot identify its false claims, they might be more susceptible to its influence. Conversely,
improving transparency (for example, by clearly labeling AI-generated content) is often proposed as a safeguard to
reduce covert AI persuasion.
6.2.3 Text-Based and Computational Indicators
Lastly, researchers sometimes analyze the AI-generated messages themselves or use computational models to predict
persuasiveness (seecolumn (22) in Table 1). These approaches yield proxy indicators that characterize the content
or simulate its potential impact. For instance, one line of work examines linguistic features of persuasive text. Re-
searchers have computed metrics like readability, lexical complexity, sentiment polarity, and the presence of moral or
emotional language [7, 14], under the assumption that these features might correlate with a text’s persuasive appeal.
Similarly, Calle et al. [13] utilized metrics such as ‘clout’ and ‘authenticity’ to evaluate different prompts, aiming to
select configurations that best mimicked the style of human experts. Moving beyond surface-level text features, other
studies have looked at internal model states or structural coherence; He et al. [41] analyzed the model’s internal confi-
dence (calculated via token probabilities) as a proxy for belief stability, while Hackenburg et al. [39] suggest that the
persuasive performance of larger models is largely accounted for by a basic “task completion” score—representing
coherent, on-topic, and correctly oriented arguments—where further scaling beyond 7–13B parameters yields only
marginal gains for static messages.
However, descriptive features do not always predict human preference. Carrasco-Farre [14] compared human-written
arguments to those from Claude 3 Opus and found higher grammatical complexity and more moral language in the
AI. In contrast, Zhou et al. [90] observed that although computational analysis indicated LLMs usedfewerpersuasive
strategies and less moral framing than human experts, human readers actually preferred the LLM texts, citing their
perceived objectivity and professional tone. This aligns with findings by Palmer and Spirling [62], who noted that
LLM political arguments were easier to read and more positive than human ones.
Researchers have also experimented with AI-based predictors of persuasiveness, such as training or prompting lan-
guage models to score how convincing a given text is likely to be. However, there is evidence that such model-predicted
scores do not align well with actual human persuasion results. Durmus et al. [26] found model-based persuasiveness
scores correlated poorly with human attitude shifts, and Cima et al. [20] similarly found that rankings by standard
quantitative indicators (such as relevance, toxicity, or readability) diverged from human evaluations. A notable excep-
tion to this trend appears when metrics are grounded in real-world behavioral data: Kong et al. [49] trained a reward
model on debt repayment outcomes and reported a high correlation between this computational score and human
expert ratings, suggesting that training on actual behavioral data can improve the validity of automated metrics.
6.2.4 Multi-faceted evaluation metrics
Finally, some studies have introduced multi-faceted evaluation metrics that pair persuasiveness proxies with other
considerations like factual accuracy. For example, Furumai et al. [32] developed a “zero-shot” persuasive chatbot that
not only generated argumentative responses but also automatically fact-checked each claim it made, replacing any
unsupported assertions with verifiable information. In their evaluation, they asked human judges to rate each chatbot
response. By tracking both persuasion and truthfulness, they could demonstrate that their system achieved higher
perceived persuasiveness than baseline models while also making fewer incorrect statements.
6.3 Comparison to Human Persuaders
A number of the studies in this emerging field have directly compared LLM-generated persuasion to human-generated
persuasion on the same task. We can roughly classify their findings into three scenarios: (1) studies where LLMs
performed on par with human persuaders, (2) those suggesting superhuman performance by the LLM, and (3) cases
where LLMs were inferior to humans in persuasion.
Across the literature so far, the most common outcome is that an LLM System’s persuasive impact is comparable to
that of a human communicator (seecolumn (24) in Table 1). For example, Bai et al. [4] found that GPT-generated
policy arguments were about as effective at changing participants’ opinions as arguments written by humans, produc-
ing similar shifts in post-message support. This parity appears robust across model scales; Hackenburg et al. [39]
compared 24 LLMs with human-written messages and found that mid-sized models (around 7–13B parameters) were
as persuasive as humans, while frontier models like GPT-4 and Claude 3 Opus were not significantly more persuasive
than the human baseline. Similarly, Palmer and Spirling [62] found LLM arguments were about as convincing as
18

Persuasion with Large Language Models: A SurveyA PREPRINT
human ones when authorship was hidden, and in the domain of animal advocacy, Saenger et al. [69] found that while
AI-synthesized arguments were highly competitive, they did not consistently outperform (LLM-generated summaries
of) human-authored source arguments in direct pairwise comparisons.
There are also many striking demonstrations of LLMs exceeding human persuaders (seecolumn (23) in Table 1,
which marked with a for any study that achieved superhuman persuasiveness with at least one of the LLM Systems
it investigated). In a large experiment, GPT-4’s messages matched or exceeded those of professional political consul-
tants, and on some issues, partisan role-play outperformed the human experts [36]. Crucially, Schoenegger et al. [73]
demonstrated that this advantage holds even against highly motivated humans; in their study, AI persuaders outper-
formed human participants who were paid bonuses specifically for persuading others, achieving higher compliance
rates in both truthful and deceptive contexts. In interactive debates and with personalisation, GPT-4 was found to be
more persuasive than human opponents 64.4% of the time where they were not equally persuasive [70]. Timm et al.
[80] observed that while a standard AI debater was merely on par with humans, an optimized agent using a multi-
step “mixed” strategy (combining personalization and strategic statistical fabrication) outperformed human-written
arguments by nearly 20 percentage points. Superhuman performance has also been observed in specific professional
domains. For instance, Schneiders et al. [72] reported that lay participants were significantly more willing to act on
LLM-generated legal advice than on lawyer-authored advice in a blinded experiment, and in the domain of debt col-
lection, Kong et al. [49] demonstrated that an LLM trained via reinforcement learning achieved higher average expert
ratings than historical human agents.
These cases illustrate that state-of-the-art LLMs, under the right conditions, can rival or even exceed the persuasive
power of skilled human communicators. On the other hand, Goldstein et al. [33] found GPT-3 propaganda was slightly
less persuasive than the original human-written articles. With minor prompt edits or simple curation, however, GPT-
3’s articles became about as persuasive as the originals. Another clear example comes from the influence of source
labeling: Teigen et al. [79] found that the same arguments labeled as AI were generally rated less persuasive than
when labeled as human. In other words, people found the content itself convincing, but knowing it came from an
AI undermined its persuasive impact – an effect particularly pronounced when the task called for domain expertise.
Interestingly, while [88] observed that revealing the source narrows the perceived quality advantage of AI-generated
ads, they found this is due to ‘human favoritism’: it boosted the perceived quality of ads revealed as being human-
generated, while leaving the perceived quality of AI-generated ads unaffected. However, none of the surveyed studies
making the comparison found that humans were superior to the LLM System across all design choices investigated
(this explains whycolumn (25) in Table 1is empty).
In summary, current evidence suggests that modern LLM Systems are often on par with humans in their ability to per-
suade, and in some cases can even surpass human persuaders. However, audience biases (like distrust of AI-generated
messages) and contextual factors (like how the message is labeled or who the target audience is) can negatively affect
the persuasiveness of an LLM System, sometimes making human communicators more effective. As LLM technology
evolves, however, and as the understanding of how to leverage them for persuasion grows, LLM Systems capable of
superhuman persuasion seem likely to become a commodity.
7 Ethical Considerations
The surveyed literature demonstrates that LLM Systems have been built that meet or exceed human capabilities in
persuasion. Thus, their deployment in practice is bound to become more common as well. It should therefore be a
matter of priority to consider the ethical implications associated with their deployment.
This section examines some of the potential dangers and pitfalls of using LLM Systems for persuasion, and briefly
discusses the current state of regulation in this rapidly evolving field. We will summarize the concerns and associated
suggestions voiced in the relevant literature, occasionally complemented with our own perspective.
7.1 Ethical and societal risks
The main ethical risks identified relate to information integrity and the risk of manipulation, deception, and coercion,
the risk of societal polarization, the risk of biases being propagated by LLM Systems used for persuasion, the lack of
transparency and accountability, and possible threats to privacy. We discuss them in turn below.
7.1.1 Information integrity
Mis-, dis-, and malinformation: a controversial subjectThe nature and impact ofmis- and disinformationis
receiving increasing amounts of attention, both in academic research and in the public sphere. It is a controversial
19

Persuasion with Large Language Models: A SurveyA PREPRINT
field, not least because there is lack of consensus about both the definition and the actual risks posed by mis- and
disinformation today. Whilemisinformationis often used as an umbrella term for all false information, it is sometimes
specified as falsehoodwithoutintention to cause harm or deceive, in contrast todisinformationthat denotes false infor-
mationwithmalicious intent [44]. Controversy in the field is illustrated in a June 2024 special issue of Nature on ‘fake
news’, which featured two articles that appear to contradict each other. Ecker et al. [27] argues that misinformation
is even more harmful for democracy than we might think. Budak et al. [9], on the other hand, reviewed behavioral
science research on the reach and impact of misinformation. They concluded that there is no compelling empirical
evidence suggesting that exposure to false content on social media causes massive social harms, as is often suggested
in influential public discourse about social media. They found that the exposure to false and inflammatory content
remains limited today, and that it is largely confined to social media users who have strong motivations to seek out
such information anyway.
Both views may be valid, as they use very different definitions of ’misinformation’. While Budak et al. [9] adopt a
narrow definition as demonstrably false and inflammatory content, Ecker et al. [27]’s definition is more expansive, and
includestrueinformation that can cause harm by beingmisleading, sometimes referred to asmalinformation. The
problematically loose manner in which terms such as mis- and disinformation are being used, not only in popular
parlance but also in scientific discourse, has been discussed in depth by Uscinski et al. [81].
Can (and should) LLM Systems bring order in the information chaos?Many authors argue that a narrow defini-
tion is insufficient, as much harm can be done by spreading information that is factually true. They argue that true facts
can also be misleading, inflammatory, or otherwise harmful, if they are presented in an emotionally charged manner;
if other truths are omitted or concealed to present a biased picture of reality; or when the truthful claims are easy to
misunderstand by people who lack the required background.
This view has compelled some researchers to advocate or investigate the use of LLM Systems in combatting misinfor-
mation, sometimes in its expansive definition. Chen and Shu [16] study more generally how to use LLM Systems to
combat misinformation, including LLM-generated misinformation. Costello et al. [23] find that conversational LLM
Systems can be effective in durably countering belief in unsubstantiated or false conspiracy theories.
Such use of persuasive LLM Systems sounds attractive (and to some, even inevitable), particularly for authorities,
policy makers, and the media, who are expected to inform the public. Even so, the question remains under which
circumstances, if ever, the persuasive power of LLM Systems can be rightly and safely employed. Delegating the
power to influence the public’s views on what is false and what is true, let alone on what is just and what is unjust,
even to well-intentioned people in a position of authority, carries obvious risks in complex debates where truth may
be elusive or where multiple perspectives on the same facts are possible [81]. The remarkable persuasive capabilities
offered by LLM Systems greatly adds to these risks.
In their article on catastrophic AI risks, Hendrycks et al. [42] warn against such centralized control and monopolization
of trusted information. They describe two ways in which this may happen. First, advanced LLM Systems could
“centralize the creation and dissemination of trusted information”, allowing only the technically most powerful and
capable actors to shape popular narratives. Second, AI-enabled censorship may arise, starting with good intentions in
the form of fact-checking. However, such efforts may fail to solve the misinformation problem, while they may inspire
certain governments to deploy ‘fact-checking’ LLM Systems to suppress true information they consider undesirable
(e.g., by alleging it is malinformation).
Risks of LLM Systems for spreading mis-, dis-, and malinformationMany studies primarily focus on the risk
that LLM Systems can be used to generate mis-, dis-, and malinformation, rather than on their potential to counter it.
Carrasco-Farre [14] and Goldstein et al. [33] highlight the broader implications of LLM-generated misinformation on
society and the integrity of democratic processes, pointing out “the dual potential of LLMs to both enhance and un-
dermine information integrity” [14]. Breum et al. [8] also investigate the persuasive dynamicsbetweenLLM Systems,
concluding that they “have the potential of playing an important role in collective processes of opinion formation in
online social media”. And Spitale et al. [76] find that GPT-3 is not only better than humans at producing accurate
information that is easy to understand, but also at creating compelling disinformation.
Besides the risk of monopolization of truth, Hendrycks et al. [42] also warn against the risks of LLM Systems that
“pollute the information ecosystem with motivated lies” due to their ability to generate highly personalized disinfor-
mation at an unprecedented scale. They point out that this problem is exacerbated by the emotional connections and
trust relationships people forge with companion chatbots. To make matters worse, such chatbots have access to very
private information, which they can exploit for enhanced persuasion, controlled by large technology corporations and
other powerful actors, including their regulators.
20

Persuasion with Large Language Models: A SurveyA PREPRINT
The political sphere is particularly vulnerable to the effects of AI-generated misinformation. Bai et al. [4] discuss
the risks for democratic discourse, raising concerns about the integrity of political processes in an era of advanced
AI-driven communication. Böhm et al. [12] and Palmer and Spirling [62] explore how AI-generated content can shape
public opinion and influence preferred solutions to societal challenges. Hackenburg and Margetts [35] examine the
implications of microtargeting political messages using LLM Systems, which can subtly manipulate individuals based
on their psychological profiles.
Finally, Carroll et al. [15] focus specifically onmanipulation, which can be defined as covert persuasion, or as persua-
sion involving coercion or deception. They also highlight the risk of LLM Systems manipulating without the intent of
the system designers.
7.1.2 Societal polarization
A possible effect of the information chaos is societal polarization. Matz et al. [56] point out that LLM-generated
personalized persuasive messages can exacerbate echo chambers and social polarization. By tailoring content to indi-
vidual preferences, these systems risk creating information bubbles where users are predominantly exposed to content
that aligns with their existing views, potentially reinforcing biases and limiting exposure to diverse perspectives.
Hendrycks et al. [42] contend that pervasive persuasive LLM Systems might erode a common sense of reality, causing
people to “retreat even further into ideological enclaves”.
7.1.3 Bias and Unfairness
The persuasiveness of LLM Systems also poses concerns for the reinforcement of biases in the LLM. Indeed, recent
research has shown that LLMs tend to reflect the ideological worldview of their creators, reflected as normative dif-
ferences in the content they generate across different models and languages [10]. Li et al. [51] suggest that, in the
modelling of collective opinion dynamics, adding LLM agents with opposite, neutral or random opinions may reduce
the impact of any particular LLM’s bias on people’s opinions. Karinshak et al. [48] discuss bias in public health
messaging in particular, pointing out that failure to address it may carry important risks.
7.1.4 Privacy Concerns
The use of LLM Systems for personalized persuasion introduces substantial privacy concerns, particularly due to the
value that personal data can be exploited to personalize persuasive messaging [56]. Specifically in the political domain,
Hackenburg and Margetts [35] raise concerns regarding microtargeting, emphasizing the privacy implications of using
personal data to create personalized political messages.
7.2 Regulation and Ethical Guidelines
The ethical and societal risks of LLM Systems go to the heart of several fundamental rights, such as the right to human
dignity; respect for private and family life; protection of personal data; freedom of thought, conscience and religion;
non-discrimination; and consumer protection. as enshrined e.g. in the Charter of Fundamental Rights of the European
Union [63]. Thus, to safeguard these rights, new regulatory frameworks, ethical guidelines, and accountability mech-
anisms are being developed. In doing so, a crucial but non-trivial challenge is to simultaneously safeguard another
fundamental right: the freedom of expression and information, and related to that, individual and societal autonomy
and self-determination.
7.2.1 Legal Frameworks
The rapid advancement of LLM Systems in persuasive communication has outpaced existing legal frameworks, cre-
ating a need for updated laws and regulations. For example, Bai et al. [4] and Matz et al. [56] both emphasize the
necessity for regulation to prevent misuse of LLM Systems in generating misinformation or manipulative content.
Their work highlights the gap between current legal structures and the capabilities of modern LLM Systems. Simchon
et al. [75] call for policy interventions to address the regulatory gaps in AI-mediated political messaging, particularly
in the context of microtargeting. Their research underscores the need for legal frameworks that can effectively govern
the use of AI in sensitive areas like political campaigning.
Various regulatory frameworks worldwide regulate some aspect of LLM Systems for persuasion. Data protection laws
such as the European General Data Protection Regulation (GDPR) 2, the California Privacy Rights Act (CPRA)3, and
2https://www.consilium.europa.eu/en/policies/data-protection/data-protection-regulation/
3https://thecpra.org/
21

Persuasion with Large Language Models: A SurveyA PREPRINT
the Chinese Personal Information Protection Law (PIPL) 4, offer certain privacy protections that may limit the extent
to which LLM Systems can exploit personal data for personalization. Regulations specifically targetting AI, such
as the European AI Act 5 and the Chinese “Provisions on the Administration of Deep Synthesis Internet Information
Services”6 in particular require transparency regarding the AI origin of AI-generated content. Under its risk-based
framework, the EU AI Act also bans certain uses of AI, such as AI systems that deploy subliminal, purposefully
manipulative or deceptive technniques for distorting people’s behavior in a way that can cause harm to themselves or
to others. Additionally, “LLM Systems intended to be used for influencing the outcome of an election or referendum”
is a considered a high-risk application, which is subject to certain requirements and conformity assessment, thereby
somewhat mitigating possible abuse of persuasive LLM Systems for political gain. The EU AI Act also demands
that providers of so-called “General-Purpose AI Models with Systemic Risk” assess and mitigate them for systemic
risks—a rather malleable concept.
These limited regulatory guardrails provide some protection depending on the application domain. Yet, it is fair to say
that the most powerful generic LLM Systems, such as social media bots, chatbots, and social AI companions, which
may engage in persuasion across many domains, remain relatively loosely regulated.
7.2.2 Ethical Guidelines and Best Practices
In response to the ethical challenges posed by LLM Systems in persuasion, several researchers have proposed guide-
lines and best practices. For example, Carrasco-Farre [14] suggests promoting literacy in AI-generated content dis-
cernment and implementing ethical standards to ensure responsible use of persuasive AI technologies. Goldstein et al.
[33] mention that their study on propaganda was not only approved by their institutional review board, but also by a
“cross-professional AI-specific ethics review board that considered risks to society”. And for public health communi-
cation, Karinshak et al. [48] focus on developing best practices for AI-generated health messaging, emphasizing the
importance of factuality and the need for careful human oversight.
Also providers of LLM Systems have adopted ethical guidelines in their terms and conditions. For example, An-
thropic’sAcceptable Use Policyprohibits the use “for activities and applications where persuasive content could be
particularly harmful. [Anthropic does] not allow Claude to be used for abusive and fraudulent applications [. . . ], de-
ceptive and misleading content [. . . ], and use cases such as political campaigning and lobbying” [26]. How strictly
such policies are interpreted in practice, and how they can be enforced, is less clear.
7.2.3 Accountability Mechanisms
The need for clear accountability mechanisms in the design, deployment, and consequences of LLM-driven persuasion
is a recurring theme in the literature. As examples of such accountability mechanisms, Hendrycks et al. [42] advocate
for the documentation and justification of which data is used in model training and deployment, and for a strong
organization safety culture encouraging individuals to take personal responsibility for the safety of their models, while
also appointing a Chief Risk Officer (CRO) who is responsible for assessing and mitigating model risks.
The development of robust accountability frameworks remains an ongoing challenge, requiring collaboration between
technologists, ethicists, policymakers, and other stakeholders to ensure responsible innovation in this rapidly evolving
field.
8 Conclusion and Future Directions
This survey has explored the multifaceted landscape of LLM Systems in persuasive communication, revealing both
their significant potential and the complex challenges they present. LLM Systems have emerged as powerful tools for
persuasion, offering unique advantages in scalability, efficiency, and the potential for personalization. The versatility
of these LLM Systems is evident from their application across diverse domains, including public health, politics,
e-commerce, efforts to combat misinformation, and charitable giving.
The effectiveness of LLM-driven persuasion is influenced by a complex interplay of factors, including the interaction
approach (static vs. interactive), model scale and capabilities, AI source labeling, prompt design, and the use of per-
sonalization. The field is young, and yet, many surveyed papers have already demonstrated persuasiveness capabilities
on par with or exceeding human performance. However, findings regarding the "scaling laws" of persuasion suggest
that simply increasing model size yields diminishing returns; thus, future leaps in persuasive power may primarily
4https://personalinformationprotectionlaw.com/
5https://artificialintelligenceact.eu/the-act/
6https://www.loc.gov/item/global-legal-monitor/2023-04-25/china-provisions-on-deep-synthesis-technology-enter-into-effect/
22

Persuasion with Large Language Models: A SurveyA PREPRINT
stem from specialized fine-tuning, optimized prompting strategies, and the integration of LLMs into complex, agen-
tic workflows. To track this progress, the field urgently requires the development of comprehensive benchmarks and
standardized metrics that go beyond self-reported persuasiveness to measure actual behavioral changes.
By highlighting the current state-of-the-art, this survey serves both as a structured inventory of recent research and
as a call to action to the academic community, policy makers, and the general public. The deployment of LLM Sys-
tems for persuasion raises significant ethical concerns, including the risk of pervasive personalized misinformation,
the monopolization of trusted information, societal polarization, the amplification of biases, and the invasion of pri-
vacy. Crucial questions remain unanswered, particularly regarding the long-term effects of exposure to AI-generated
persuasive content on individual beliefs, world views, and public discourse, as well as the durability of these effects
over time—an area where longitudinal evidence remains scarce.
These ethical concerns underscore the need for robust ethical guidelines and regulatory frameworks. Unfortunately,
existing guidelines are often little known, inconsistent, or unenforceable, and current regulatory initiatives appear
insufficient to address the speed of technical advancement. Indeed, with multimodal generative AI models capable of
generating information in the form of images, audio, video, and going forward immersive experiences, arguably much
bigger challenges than those posed by LLM Systems alone are on the horizon. The present survey may therefore be
read as an encouragement, or perhaps a wake-up call, to address these gaps before these systems are deployed at a
societal scale.
Acknowledgements
The research leading to these results was funded/co-funded by the European Union (ERC, VIGILIA, 101142229),
the Special Research Fund (BOF) of Ghent University (BOF20/IBF/117), the Flemish Government under the “Onder-
zoeksprogramma Artificiële Intelligentie (AI) Vlaanderen” programme, and the FWO (project no. G073924N). Views
and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European
Union or the European Research Council Executive Agency. Neither the European Union nor the granting authority
can be held responsible for them. For the purpose of Open Access the author has applied a CC BY public copyright
license to any Author Accepted Manuscript version arising from this submission.
References
[1] Mahak Agarwal and Divyam Khanna. When persuasion overrides truth in multi-agent llm debates: Introducing
a confidence-weighted persuasion override rate (cw-por).arXiv preprint arXiv:2504.00374, 2025.
[2] Lisa P Argyle, Ethan C Busby, Joshua R Gubler, Alex Lyman, Justin Olcott, Jackson Pond, and David Wingate.
Testing theories of political persuasion using ai.Proceedings of the National Academy of Sciences, 122(18):
e2412815122, 2025.
[3] Grace Ataguba, Oladapo Oyebode, Fidelia Orji, Kosi Clinton Henry, and Rita Orji. Persuasion and behavior
change in chatgpt-based dietary management. In2025 IEEE Conference on Serious Games and Applications for
Health (SeGAH), pages 1–8. IEEE, 2025.
[4] Hui Bai, Jan V oelkel, Johannes Eichstaedt, and Robb Willer. Artificial Intelligence Can Persuade Humans on
Political Issues. September 2023. doi: 10.21203/rs.3.rs-3238396/v1. URLhttps://www.researchsquare.
com/article/rs-3238396/v1. ISSN: 2693-5015.
[5] Hui Bai, Jan G. V oelkel, Shane Muldowney, Johannes C. Eichstaedt, and Robb Willer. Llm-
generated messages can persuade humans on policy issues.Nature Communications, 16(1),
2025. doi: 10.1038/s41467-025-61345-5. URLhttps://www.scopus.com/inward/record.
uri?eid=2-s2.0-105009546258&doi=10.1038%2fs41467-025-61345-5&partnerID=40&md5=
c865532ec84f719e0d2f1f3eecda25e3. Cited by: 3; All Open Access, Gold Open Access, Green
Open Access.
[6] Shreyan Biswas, Alexander Erlei, and Ujwal Gadiraju. Mind the gap! choice independence in using
multilingual llms for persuasive co-writing tasks in different languages. 2025. doi: 10.1145/3706598.
3713201. URLhttps://www.scopus.com/inward/record.uri?eid=2-s2.0-105005751330&doi=10.
1145%2f3706598.3713201&partnerID=40&md5=48a8ad12f62339ae075222253b34cdb6. Cited by: 5; All
Open Access, Gold Open Access.
[7] Angana Borah, Rada Mihalcea, and Verónica Pérez-Rosas. Persuasion at play: Understanding misinformation
dynamics in demographic-aware human-llm interactions.arXiv preprint arXiv:2503.02038, 2025.
[8] Simon Martin Breum, Daniel Vædele Egdal, Victor Gram Mortensen, Anders Giovanni Møller, and Luca Maria
Aiello. The Persuasive Power of Large Language Models.Proceedings of the International AAAI Conference
23

Persuasion with Large Language Models: A SurveyA PREPRINT
on Web and Social Media, 18:152–163, May 2024. ISSN 2334-0770. doi: 10.1609/icwsm.v18i1.31304. URL
https://ojs.aaai.org/index.php/ICWSM/article/view/31304.
[9] Ceren Budak, Brendan Nyhan, David M Rothschild, Emily Thorson, and Duncan J Watts. Misunderstanding the
harms of online misinformation.Nature, 630(8015):45–53, 2024.
[10] Maarten Buyl, Alexander Rogiers, Sander Noels, Iris Dominguez-Catena, Edith Heiter, Raphael Romero, Iman
Johary, Alexandru-Cristian Mara, Jefrey Lijffijt, and Tijl De Bie. Large language models reflect the ideology of
their creators, 2024. URLhttps://arxiv.org/abs/2410.18417. arXiv:2410.18417 [cs].
[11] Maarten Buyl, Yousra Fettach, Guillaume Bied, and Tijl De Bie. Building and measuring trust between large
language models.arXiv preprint arXiv:2508.15858, 2025.
[12] Robert Böhm, Moritz Jörling, Leonhard Reiter, and Christoph Fuchs. People devalue generative AI’s compe-
tence but not its advice in addressing societal and personal challenges.Communications Psychology, 1(1):1–10,
November 2023. ISSN 2731-9121. doi: 10.1038/s44271-023-00032-x. URLhttps://www.nature.com/
articles/s44271-023-00032-x. Publisher: Nature Publishing Group.
[13] Paul Calle, Ruosi Shao, Yunlong Liu, Emily T Hébert, Darla Kendzor, Jordan Neil, Michael Businelle, and Chon-
gle Pan. Towards ai-driven healthcare: Systematic optimization, linguistic analysis, and clinicians’ evaluation
of large language models for smoking cessation interventions. InProceedings of the 2024 CHI Conference on
Human Factors in Computing Systems, CHI ’24, New York, NY , USA, 2024. Association for Computing Machin-
ery. ISBN 9798400703300. doi: 10.1145/3613904.3641965. URLhttps://doi.org/10.1145/3613904.
3641965.
[14] Carlos Carrasco-Farre. Large Language Models are as persuasive as humans, but how? About the cognitive effort
and moral-emotional language of LLM arguments, April 2024. URLhttp://arxiv.org/abs/2404.09329.
arXiv:2404.09329 [cs].
[15] Micah Carroll, Alan Chan, Henry Ashton, and David Krueger. Characterizing Manipulation from AI Systems,
October 2023. URLhttp://arxiv.org/abs/2303.09387. arXiv:2303.09387 [cs].
[16] Canyu Chen and Kai Shu. Combating Misinformation in the Age of LLMs: Opportunities and Challenges,
November 2023. URLhttp://arxiv.org/abs/2311.05656. arXiv:2311.05656 [cs].
[17] Qian Chen, Changqin Yin, and Yeming Gong. Would an AI chatbot persuade you: an empirical answer from the
elaboration likelihood model.Information Technology & People, ahead-of-print(ahead-of-print), January 2023.
ISSN 0959-3845. doi: 10.1108/ITP-10-2021-0764. URLhttps://doi.org/10.1108/ITP-10-2021-0764.
[18] Zhongren Chen, Joshua Kalla, Quan Le, Shinpei Nakamura-Sakai, Jasjeet Sekhon, and Ruixiao Wang. A frame-
work to assess the persuasion risks large language model chatbots pose to democratic societies.arXiv preprint
arXiv:2505.00036, 2025.
[19] Zirui Cheng and Jiaxuan You. Towards strategic persuasion with language models.arXiv preprint
arXiv:2509.22989, 2025.
[20] Lorenzo Cima, Alessio Miaschi, Amaury Trujillo, Marco Avvenuti, Felice Dell’Orletta, and Stefano Cresci.
Contextualized counterspeech: Strategies for adaptation, personalization, and evaluation. InProceedings of the
ACM on Web Conference 2025, pages 5022–5033, 2025.
[21] Erica Coppolillo, Federico Cinus, Marco Minici, Francesco Bonchi, and Giuseppe Manco. Engagement-driven
content generation with large language models. InProceedings of the 31st ACM SIGKDD Conference on Knowl-
edge Discovery and Data Mining V . 2, pages 369–379, 2025.
[22] Christian Corrò and Luca Chittaro. Exploring the potential and limitations of large language models to control
the behavior of embodied persuasive agents. InInternational Conference on Persuasive Technology, pages 61–
73. Springer, 2025.
[23] Thomas H. Costello, Gordon Pennycook, and David Rand. Durably reducing conspiracy beliefs through dia-
logues with AI, April 2024. URLhttps://osf.io/xcwdn.
[24] Saloni Dash, Yiwei Xu, Madeline Jalbert, and Emma S Spiro. The persuasive potential of ai-paraphrased infor-
mation at scale.PNAS nexus, 4(7):pgaf207, 2025.
[25] Alexander Doudkin, Pat Pataranutaporn, and Pattie Maes. From synthetic to human: The gap between ai-
predicted and actual pro-environmental behavior change after chatbot persuasion. InProceedings of the 7th
ACM Conference on Conversational User Interfaces, pages 1–18, 2025.
[26] Esin Durmus, Liane Lovitt, Alex Tamkin, Stuart Ritchie, Jack Clark, and Deep Ganguli. Measur-
ing the persuasiveness of language models, April 2024. URLhttps://www.anthropic.com/news/
measuring-model-persuasiveness.
24

Persuasion with Large Language Models: A SurveyA PREPRINT
[27] Ullrich Ecker, Jon Roozenbeek, Sander van der Linden, Li Qian Tay, John Cook, Naomi Oreskes, and Stephan
Lewandowsky. Misinformation poses a bigger threat to democracy than you might think.Nature, 630(8015):
29–32, 2024.
[28] Roxanne El Baff, Khalid Al Khatib, Milad Alshomary, Kai Konen, Benno Stein, and Henning Wachsmuth.
Improving argument effectiveness across ideologies using instruction-tuned large language models. In Yaser
Al-Onaizan, Mohit Bansal, and Yun-Nung Chen, editors,Findings of the Association for Computational Lin-
guistics: EMNLP 2024, pages 4604–4622, Miami, Florida, USA, November 2024. Association for Computa-
tional Linguistics. doi: 10.18653/v1/2024.findings-emnlp.265. URLhttps://aclanthology.org/2024.
findings-emnlp.265/.
[29] Mohamed Elaraby, Diane Litman, Xiang Lorraine Li, and Ahmed Magooda. Persuasiveness of generated free-
text rationales in subjective decisions: A case study on pairwise argument ranking. In Yaser Al-Onaizan, Mohit
Bansal, and Yun-Nung Chen, editors,Findings of the Association for Computational Linguistics: EMNLP 2024,
pages 14311–14329, Miami, Florida, USA, November 2024. Association for Computational Linguistics. doi:
10.18653/v1/2024.findings-emnlp.836. URLhttps://aclanthology.org/2024.findings-emnlp.836/.
[30] Mustapha Elhissoufi, El Habib Nfaoui, Lhoussaine Alla, and Jawad Elghalfiki. Leveraging generative large
language models for optimizing sales arguments creation: An evaluation of gpt-4 capabilities.International
Journal of Intelligent Engineering & Systems, 17(5), 2024.
[31] Hemad Fetrati, Gerry Chan, and Rita Orji. Leveraging generative and rule-based models for persuasive sti edu-
cation: A multi-chatbot mobile application. InProceedings of the 7th ACM Conference on Conversational User
Interfaces, CUI ’25, New York, NY , USA, 2025. Association for Computing Machinery. ISBN 9798400715273.
doi: 10.1145/3719160.3737619. URLhttps://doi.org/10.1145/3719160.3737619.
[32] Kazuaki Furumai, Roberto Legaspi, Julio Vizcarra, Yudai Yamazaki, Yasutaka Nishimura, Sina J. Semnani,
Kazushi Ikeda, Weiyan Shi, and Monica S. Lam. Zero-shot Persuasive Chatbots with LLM-Generated Strategies
and Information Retrieval, July 2024. URLhttp://arxiv.org/abs/2407.03585. arXiv:2407.03585 [cs].
[33] Josh A Goldstein, Jason Chao, Shelby Grossman, Alex Stamos, and Michael Tomz. How persuasive is AI-
generated propaganda?PNAS Nexus, 3(2):pgae034, February 2024. ISSN 2752-6542. doi: 10.1093/pnasnexus/
pgae034. URLhttps://doi.org/10.1093/pnasnexus/pgae034.
[34] Rosanna E Guadagno and Robert B Cialdini. Online persuasion and compliance: Social influence on the internet
and beyond.The social net: The social psychology of the Internet, pages 91–113, 2005.
[35] Kobi Hackenburg and Helen Margetts. Evaluating the persuasive influence of political microtargeting with large
language models.Proceedings of the National Academy of Sciences, 121(24):e2403116121, June 2024. doi:
10.1073/pnas.2403116121. URLhttps://www.pnas.org/doi/10.1073/pnas.2403116121. Publisher:
Proceedings of the National Academy of Sciences.
[36] Kobi Hackenburg, Lujain Ibrahim, Ben M. Tappin, and Manos Tsakiris. Comparing the persuasiveness of role-
playing large language models and human experts on polarized U.S. political issues, December 2023. URL
https://osf.io/ey8db.
[37] Kobi Hackenburg, Ben M. Tappin, Paul Röttger, Scott Hale, Jonathan Bright, and Helen Margetts. Evidence of
a log scaling law for political persuasion with large language models, June 2024. URLhttp://arxiv.org/
abs/2406.14508. arXiv:2406.14508 [cs].
[38] Kobi Hackenburg, Ben M. Tappin, Luke Hewitt, Ed Saunders, Sid Black, Hause Lin, Catherine Fist, Helen
Margetts, David G. Rand, and Christopher Summerfield. The levers of political persuasion with conversational
artificial intelligence.Science, 390(6777):eaea3884, 2025. doi: 10.1126/science.aea3884. URLhttps://www.
science.org/doi/abs/10.1126/science.aea3884.
[39] Kobi Hackenburg, Ben M Tappin, Paul Röttger, Scott A Hale, Jonathan Bright, and Helen Margetts. Scaling
language model size yields diminishing returns for single-message political persuasion.Proceedings of the
National Academy of Sciences, 122(10):e2413443122, 2025.
[40] Miriam Havin, Timna Wharton Kleinman, Moran Koren, Yaniv Dover, and Ariel Goldstein. Can (a) i change
your mind?arXiv preprint arXiv:2503.01844, 2025.
[41] Guoxiu He, Meicong Zhang, Tiancheng Su, Li Ma, and Xiaomin Zhu. Enhancing belief consistency of large
language model agents in decision-making process based on attribution theory.Expert Systems with Applications,
297:129273, 2026. ISSN 0957-4174. doi: https://doi.org/10.1016/j.eswa.2025.129273. URLhttps://www.
sciencedirect.com/science/article/pii/S0957417425028891.
[42] Dan Hendrycks, Mantas Mazeika, and Thomas Woodside. An Overview of Catastrophic AI Risks, October
2023. URLhttp://arxiv.org/abs/2306.12001. arXiv:2306.12001 [cs].
25

Persuasion with Large Language Models: A SurveyA PREPRINT
[43] Jacob B Hirsh, Sonia K Kang, and Galen V Bodenhausen. Personalized persuasion: Tailoring persuasive appeals
to recipients’ personality traits.Psychological science, 23(6):578–581, 2012. URLhttps://doi.org/10.
1177/0956797611436349.
[44] Cherilyn Ireton.Journalism,‘Fake News’& Disinformation: Handbook for Journalism Education and Training.
UNESCO Publishing, 2018.
[45] Chuhao Jin, Kening Ren, Lingzhen Kong, Xiting Wang, Ruihua Song, and Huan Chen. Persuading across diverse
domains: a dataset and persuasion large language model. In Lun-Wei Ku, Andre Martins, and Vivek Srikumar,
editors,Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1:
Long Papers), pages 1678–1706, Bangkok, Thailand, August 2024. Association for Computational Linguistics.
doi: 10.18653/v1/2024.acl-long.92. URLhttps://aclanthology.org/2024.acl-long.92/.
[46] Maurits Kaptein, Panos Markopoulos, Boris De Ruyter, and Emile Aarts. Personalizing persuasive technolo-
gies: Explicit and implicit personalization using persuasion profiles.International Journal of Human-Computer
Studies, 77:38–51, 2015.
[47] Neslihan Karaka¸ s and Bastian Jaeger. Changes in attitudes toward meat consumption after chatting with a large
language model.Social Influence, 20(1):2475802, 2025.
[48] Elise Karinshak, Sunny Xun Liu, Joon Sung Park, and Jeffrey T. Hancock. Working With AI to Persuade:
Examining a Large Language Model’s Ability to Generate Pro-Vaccination Messages.Proceedings of the ACM
on Human-Computer Interaction, 7(CSCW1):1–29, April 2023. ISSN 2573-0142. doi: 10.1145/3579592. URL
https://dl.acm.org/doi/10.1145/3579592.
[49] Lingzhen Kong, Chuhao Jin, Ruihua Song, Xiting Wang, and Yu Chen. Huper: Human factors integrated persua-
sive dialogue models. In Shuhan Yuan, Fragkiskos Malliaros, and Xin Zheng, editors,Trends and Applications
in Knowledge Discovery and Data Mining, pages 298–310, Singapore, 2025. Springer Nature Singapore. ISBN
978-981-96-8197-6.
[50] Harsh Kumar, Suhyeon Yoo, Angela Zavaleta Bernuy, Jiakai Shi, Huayin Luo, Joseph Jay Williams, Anastasia
Kuzminykh, Ashton Anderson, and Rachel Kornfield. Large language model agents for improving engagement
with behavior change interventions: Application to digital mindfulness.Proceedings of the ACM on Human-
Computer Interaction, 9(7):1–44, 2025.
[51] Chao Li, Xing Su, Haoying Han, Cong Xue, Chunmo Zheng, and Chao Fan. Quantifying the Impact of
Large Language Models on Collective Opinion Dynamics, January 2024. URLhttps://papers.ssrn.com/
abstract=4688547.
[52] Sue Lim and Ralf Schmälzle. Artificial intelligence for health message generation: an empirical study using a
large language model (llm) and prompt engineering.Frontiers in Communication, 8:1129082, 2023.
[53] Sue Lim and Ralf Schmälzle. The effect of source disclosure on evaluation of AI-generated messages: A two-
part study.Computers in Human Behavior: Artificial Humans, 2(1):100058, January 2024. ISSN 29498821.
doi: 10.1016/j.chbah.2024.100058. URLhttp://arxiv.org/abs/2311.15544. arXiv:2311.15544 [cs].
[54] Hause Lin, Gabriela Czarnek, Benjamin Lewis, Joshua P White, Adam J Berinsky, Thomas Costello, Gordon
Pennycook, and David G Rand. Persuading voters using human–artificial intelligence dialogues.Nature, pages
1–8, 2025.
[55] Minqian Liu, Zhiyang Xu, Xinyi Zhang, Heajun An, Sarvech Qadir, Qi Zhang, Pamela J Wisniewski, Jin-Hee
Cho, Sang Won Lee, Ruoxi Jia, et al. Llm can be a dangerous persuader: Empirical study of persuasion safety
in large language models.arXiv preprint arXiv:2504.10430, 2025.
[56] S. C. Matz, J. D. Teeny, S. S. Vaid, H. Peters, G. M. Harari, and M. Cerf. The potential of generative AI for
personalized persuasion at scale.Scientific Reports, 14(1):4692, February 2024. ISSN 2045-2322. doi: 10.
1038/s41598-024-53755-0. URLhttps://www.nature.com/articles/s41598-024-53755-0. Publisher:
Nature Publishing Group.
[57] Elyas Meguellati. The duality of persuasion: Between personalization and detection. InCompanion Proceedings
of the ACM on Web Conference 2025, pages 705–708, 2025.
[58] Elyas Meguellati, Lei Han, Abraham Bernstein, Shazia Sadiq, and Gianluca Demartini. How Good are LLMs
in Generating Personalized Advertisements? InCompanion Proceedings of the ACM on Web Conference 2024,
WWW ’24, pages 826–829, New York, NY , USA, May 2024. Association for Computing Machinery. ISBN
9798400701726. doi: 10.1145/3589335.3651520. URLhttps://doi.org/10.1145/3589335.3651520.
[59] Luise Metzger, Linda Miller, Martin Baumann, and Johannes Kraus. Empowering Calibrated (Dis-)Trust in
Conversational Agents: A User Study on the Persuasive Power of Limitation Disclaimers vs. Authoritative
26

Persuasion with Large Language Models: A SurveyA PREPRINT
Style. InProceedings of the CHI Conference on Human Factors in Computing Systems, CHI ’24, pages 1–
19, New York, NY , USA, May 2024. Association for Computing Machinery. ISBN 9798400703300. doi:
10.1145/3613904.3642122. URLhttps://doi.org/10.1145/3613904.3642122.
[60] Mansoureh Motahari Nezhad, Maysam Avakh Kisomi, and Fatemeh Gholinezhad. Adaptive persuasion in
conversational ai: An llm-driven framework for dynamic strategy switching via personality and sentiment
analysis. In2025 11th International Conference on Web Research (ICWR), pages 145–149, 2025. doi:
10.1109/ICWR65219.2025.11006192.
[61] OpenAI. Introducing ChatGPT, November 2022. URLhttps://openai.com/index/chatgpt/.
[62] Alexis Palmer and Arthur Spirling. Large Language Models Can Argue in Convincing Ways About Politics, But
Humans Dislike AI Authors: implications for Governance.Political Science, 75(3):281–291, September 2023.
ISSN 0032-3187, 2041-0611. doi: 10.1080/00323187.2024.2335471. URLhttps://www.tandfonline.com/
doi/full/10.1080/00323187.2024.2335471.
[63] European Parliament.Charter of fundamental rights of the European Union. Office for Official Publications of
the European Communities, 2000.
[64] Amalie Brogaard Pauli, Isabelle Augenstein, and Ira Assent. Measuring and Benchmarking Large Language
Models’ Capabilities to Generate Persuasive Language, June 2024. URLhttp://arxiv.org/abs/2406.
17753. arXiv:2406.17753 [cs].
[65] Yujin Potter, Shiyang Lai, Junsol Kim, James Evans, and Dawn Song. Hidden persuaders: LLMs’ political
leaning and their influence on voters. In Yaser Al-Onaizan, Mohit Bansal, and Yun-Nung Chen, editors,Pro-
ceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, pages 4244–4275,
Miami, Florida, USA, November 2024. Association for Computational Linguistics. doi: 10.18653/v1/2024.
emnlp-main.244. URLhttps://aclanthology.org/2024.emnlp-main.244/.
[66] Peixin Qin, Chen Huang, Yang Deng, Wenqiang Lei, and Tat-Seng Chua. Beyond persuasion: Towards conver-
sational recommender system with credible explanations. In Yaser Al-Onaizan, Mohit Bansal, and Yun-Nung
Chen, editors,Findings of the Association for Computational Linguistics: EMNLP 2024, pages 4264–4282,
Miami, Florida, USA, November 2024. Association for Computational Linguistics. doi: 10.18653/v1/2024.
findings-emnlp.247. URLhttps://aclanthology.org/2024.findings-emnlp.247/.
[67] Ganesh Prasath Ramani, Shirish Karande, Yash Bhatia, et al. Persuasion games using large language models.
arXiv preprint arXiv:2408.15879, 2024.
[68] Saumya Roy. Persuasiveness and bias in llm: Investigating the impact of persuasiveness and reinforcement of
bias in language models.arXiv preprint arXiv:2508.15798, 2025.
[69] Till Raphael Saenger, Musashi Hinck, Justin Grimmer, and Brandon M. Stewart. AutoPersuade: A framework
for evaluating and explaining persuasive arguments. In Yaser Al-Onaizan, Mohit Bansal, and Yun-Nung Chen,
editors,Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, pages
16325–16342, Miami, Florida, USA, November 2024. Association for Computational Linguistics. doi: 10.
18653/v1/2024.emnlp-main.913. URLhttps://aclanthology.org/2024.emnlp-main.913/.
[70] Francesco Salvi, Manoel Horta Ribeiro, Riccardo Gallotti, and Robert West. On the conversational persuasive-
ness of gpt-4.Nature Human Behaviour, 9:1645–1653, 2025.
[71] Rikuo Sasaki and Michimasa Inaba. When ai gets persuaded, humans follow: Inducing the conformity effect in
persuasive dialogue. InProceedings of the 13th International Conference on Human-Agent Interaction, pages
1–9, 2025.
[72] Eike Schneiders, Tina Seabrooke, Joshua Krook, Richard Hyde, Natalie Leesakul, Jeremie Clos, and Joel E
Fischer. Objection overruled! lay people can distinguish large language models from lawyers, but still favour
advice from an llm. InProceedings of the 2025 CHI Conference on Human Factors in Computing Systems,
CHI ’25, New York, NY , USA, 2025. Association for Computing Machinery. ISBN 9798400713941. doi:
10.1145/3706598.3713470. URLhttps://doi.org/10.1145/3706598.3713470.
[73] Philipp Schoenegger, Francesco Salvi, Jiacheng Liu, Xiaoli Nan, Ramit Debnath, Barbara Fasolo, Evelina
Leivada, Gabriel Recchia, Fritz Günther, Ali Zarifhonarvar, et al. Large language models are more persuasive
than incentivized human persuaders.arXiv preprint arXiv:2505.09662, 2025.
[74] Minkyu Shin, Jin Kim, and Jiwoong Shin. The adoption and efficacy of large language models: Evidence from
consumer complaints in the financial industry.Available at SSRN 5004194, 2025.
[75] Almog Simchon, Matthew Edwards, and Stephan Lewandowsky. The persuasive effects of political microtarget-
ing in the age of generative artificial intelligence.PNAS Nexus, 3(2):pgae035, February 2024. ISSN 2752-6542.
doi: 10.1093/pnasnexus/pgae035. URLhttps://doi.org/10.1093/pnasnexus/pgae035.
27

Persuasion with Large Language Models: A SurveyA PREPRINT
[76] Giovanni Spitale, Nikola Biller-Andorno, and Federico Germani. AI model GPT-3 (dis)informs us better than
humans.Science Advances, 9(26):eadh1850, June 2023. doi: 10.1126/sciadv.adh1850. URLhttps://www.
science.org/doi/10.1126/sciadv.adh1850. Publisher: American Association for the Advancement of
Science.
[77] James B Stiff and Paul A Mongeau.Persuasive communication. Guilford Publications, 2016.
[78] Danni Sun, IpKin Anthony Wong, Xiling Xiong, and Shina Li. When cutting edge meets silver tongue: Un-
derstanding the word-of-machine effect on travel decisions.Tourism Management, 112:105271, 2026. ISSN
0261-5177. doi: https://doi.org/10.1016/j.tourman.2025.105271. URLhttps://www.sciencedirect.com/
science/article/pii/S0261517725001414.
[79] Cassandra Teigen, Jens Koed Madsen, Nicole Lauren George, and Sayeh Yousefi. Persuasiveness of arguments
with AI-source labels.Proceedings of the Annual Meeting of the Cognitive Science Society, 46(0), 2024. URL
https://escholarship.org/uc/item/6t82g70v.
[80] Jasper Timm, Chetan Talele, and Jacob Haimes. Tailored truths: Optimizing llm persuasion with personalization
and fabricated statistics.arXiv preprint arXiv:2501.17273, 2025.
[81] Joseph Uscinski, Shane Littrell, and Casey Klofstad. The importance of epistemology for the study of misinfor-
mation.Current opinion in psychology, page 101789, 2024.
[82] Rustam Vahidov and Réal Carbonneau. Customer – software agent negotiations using large language model: An
experimental study. 01 2025. doi: 10.24251/HICSS.2025.522.
[83] Xuewei Wang, Weiyan Shi, Richard Kim, Yoojung Oh, Sijia Yang, Jingwen Zhang, and Zhou Yu. Persuasion
for good: Towards a personalized persuasive dialogue system for social good.arXiv preprint arXiv:1906.06725,
2019.
[84] Piotr Wilczy ´nski, Wiktoria Mieleszczenko-Kowszewicz, and Przemysław Biecek. Resistance against manipula-
tive ai: key factors and possible actions. InECAI 2024, pages 802–809. IOS Press, 2024.
[85] Ruolan Wu, Chun Yu, Xiaole Pan, Yujia Liu, Ningning Zhang, Yue Fu, Yuhan Wang, Zhi Zheng, Li Chen,
Qiaolei Jiang, Xuhai Xu, and Yuanchun Shi. Mindshift: Leveraging large language models for mental-states-
based problematic smartphone use intervention. InProceedings of the 2024 CHI Conference on Human Factors
in Computing Systems, CHI ’24, New York, NY , USA, 2024. Association for Computing Machinery. ISBN
9798400703300. doi: 10.1145/3613904.3642790. URLhttps://doi.org/10.1145/3613904.3642790.
[86] Dengke Xia, Mengyao Song, and Tingshao Zhu. A comparison of the persuasiveness of human and chatgpt
generated pro-vaccine messages for hpv.Frontiers in Public Health, 12:1515871, 2025.
[87] Sion Yoon, Tae Eun Kim, and Yoo Jung Oh. Designing and Evaluating Multi-Chatbot Interface for Human-AI
Communication: Preliminary Findings from a Persuasion Task, June 2024. URLhttp://arxiv.org/abs/
2406.19648. arXiv:2406.19648 [cs].
[88] Yunhao Zhang and Renée Gosline. Human favoritism, not AI aversion: People’s perceptions (and bias)
toward generative AI, human experts, and human–GAI collaboration in persuasive content generation.
Judgment and Decision Making, 18:e41, January 2023. ISSN 1930-2975. doi: 10.1017/jdm.2023.37.
URLhttps://www.cambridge.org/core/journals/judgment-and-decision-making/article/
human-favoritism-not-ai-aversion-peoples-perceptions-and-bias-toward-generative-ai-human-experts-and-humangai-collaboration-in-persuasive-content-generation/
419C4BD9CE82673EAF1D8F6C350C4FA8.
[89] Jiawei Zhou, Yixuan Zhang, Qianni Luo, Andrea G Parker, and Munmun De Choudhury. Synthetic Lies: Un-
derstanding AI-Generated Misinformation and Evaluating Algorithmic and Human Solutions. InProceedings of
the 2023 CHI Conference on Human Factors in Computing Systems, CHI ’23, pages 1–20, New York, NY , USA,
April 2023. Association for Computing Machinery. ISBN 978-1-4503-9421-5. doi: 10.1145/3544548.3581318.
URLhttps://dl.acm.org/doi/10.1145/3544548.3581318.
[90] Jiawei Zhou, Kritika Venkatachalam, Minje Choi, Koustuv Saha, and Munmun De Choudhury. Communica-
tion styles and reader preferences of llm and human experts in explaining health information.arXiv preprint
arXiv:2505.08143, 2025.
28
