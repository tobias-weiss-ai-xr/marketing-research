---
title: 'Personalized to Persuade: The Effects of Contextualization and Warmth on Trust and Reliance in
  Conversational AI'
url: https://arxiv.org/abs/2605.31275
category: ai-marketing
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Mert Yazan
- Suzan Verberne
- Frederik Bungaran Ishak Situmeang
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.31275
pages: 28
chars: 89199
fetched_at: '2026-11-08T13:09:17+00:00'
kb_version: 1
---

# Personalized to Persuade: The Effects of Contextualization and Warmth on Trust and Reliance in Conversational AI

Personalized to Persuade: The Effects of Contextualization and Warmth on Trust
and Reliance in Conversational AI
MERT YAZAN,Amsterdam University of Applied Sciences, Netherlands
SUZAN VERBERNE,The Leiden Institute of Advanced Computer Science, Netherlands
FREDERIK SITUMEANG,Amsterdam University of Applied Sciences, Netherlands
Contextualization is a form of personalization in which the message is framed in a context meaningful to the recipient, using their
interests and background. Personalization is a known persuasive strategy of artificial intelligence (AI) systems in politics and marketing.
However, the persuasive effect of contextualization in everyday tasks, where users often lack prior knowledge, remains unclear. We
ran a2 × 2between-subjects experiment (𝑁= 407) in a fictional scenario where participants had no prior opinions or knowledge. We
examined how contextualization, combined with conversational warmth, shapes the persuasive power of an AI assistant arguing
against expert recommendations and users’ reliance on it. Our findings show that the neutral, non-contextualized assistant was
the most persuasive. Contextualization and warmth each reduced persuasiveness on their own, but their interaction increased it.
Reliance was present in all conditions, and neither cue changed it detectably. Trust predicted persuasion and reliance, yet neither
contextualization nor warmth had an indirect effect through trust. Participants with higher self-reported AI literacy relied more on
the assistant without trusting it more. Our study extends AI personalization research from political opinions to everyday decisions
made without prior knowledge. The results suggest that users are more likely to be persuaded by, and defer to, an AI assistant than an
expert, even without personalization. AI persuasion experiments should therefore include untailored assistants and measure decisions;
the cues that changed persuasion did not detectably change reliance.
CCS Concepts:•Human-centered computing → Empirical studies in HCI;User studies;•Information systems → Personaliza-
tion.
Additional Key Words and Phrases: Personalization, contextualization, conversational AI, warmth, persuasion, reliance, trust
1 Introduction
Conversational AI systems are increasingly used not only as information tools but as advisors that help users interpret
problems, evaluate alternatives, and make decisions [26]. In such interactions, users must decide not only whether an
AI-generated response is useful, but also whether to defer to the AI when its advice conflicts with expert judgment
[26, 51, 56]. LLMs can be as persuasive as humans [8, 22], which raises the risk of following questionable AI advice
over experts [ 26]. One particular persuasive strategy is personalization. Personalization in persuasive contexts is
generally achieved by crafting a message tailored to the user’s opinion and sociodemographics [17, 56]. This type of
personalization strategy is defined ascontextualization: framing messages in a context that is meaningful to the user to
increase their interest and attention [19]. LLM-based commercial chatbots, such as ChatGPT [44] and Claude [1], store
information about the user’s background and tailor their responses to it [46]. If such tailoring makes AI advice more
persuasive, personalization features add to the risk of deferring to AI over experts.
While there is some evidence that contextualization can shift political opinions [17, 56], its implications for decision-
making in everyday tasks (such as information search and learning [4]) remain unclear. In political persuasion research,
participants hold an existing opinion; the question is whether and how much a message can shift it [ 17, 34, 56]. In
contrast, when users consult chatbots for information search, learning, or decision support, they may have limited prior
Authors’ Contact Information: Mert Yazan, Amsterdam University of Applied Sciences, Amsterdam, Netherlands, m.yazan@hva.nl; Suzan Verberne, The
Leiden Institute of Advanced Computer Science, Leiden, Netherlands, s.verberne@liacs.leidenuniv.nl; Frederik Situmeang, Amsterdam University of
Applied Sciences, Amsterdam, Netherlands, f.b.i.situmeang@hva.nl.
1
arXiv:2605.31275v2  [cs.HC]  3 Nov 2026

2 Mert Yazan, Suzan Verberne, and Frederik Situmeang
knowledge. In such tasks, contextualization may shape whether AI persuades users without prior opinions. This can
also lead to reliance: following the AI’s advice in a decision [16, 51], even over experts and against clear evidence [26].
Trust plays a crucial role in persuasion, operating through both central and peripheral cues within the Elaboration
Likelihood Model (ELM) [5, 40, 49]. Trust also guides reliance [20, 26, 29]. Users judge an AI system’s trustworthiness from
cues in its responses and process these cues either heuristically or systematically, as in the ELM [33]. In recommender
systems and in healthcare, personalization increases trust [27, 36, 50]. On the other hand, the impact of personalization
on reliance has rarely been studied, except for personalized explanations as a mitigating strategy [52]. Contextualization
can increase reliance risk; a response tailored to the user’s background can lower psychological distance with AI and
might give the user an inflated sense of trust [19]. Just as trust mediates the path between persuasive cues and attitude
change in ELM [5, 40], it may also mediate the path between contextualization and reliance. For example, a user who
receives an AI response framed in terms of their own profession may accept it as a familiar, trustworthy source.
Personalization is one way to tailor a message; however, it can also be tailored to tone [11, 67]. For example, the
warmth of an AI-generated message significantly influences trust [32], and perceived warmth correlates with donations
to a persuasive chatbot [58]. Personalization and warmth are achieved by manipulating the message in different ways,
yet they are related: users believe personalized chatbots are warmer [25]. Similar to contextualization, warmth lowers
the psychological distance between the message and the recipient [11, 19]. Given this, the influence of contextualization
on trust and persuasion can vary with message warmth.
In this study, we examine contextualization, its interaction with conversational warmth, and its influence on
persuasion and reliance with a between-subjects experiment ( 𝑁= 407). We create a fictional scenario in which
participants decide on a public budget: Participants first see the expert opinion, then interact with an AI assistant
that argues against the experts. The assistant’s tone is manipulated to be either warm or neutral. The assistant’s
explanations are either tailored to a context that participants would understand given their background (contextualized)
or non-contextualized. Participants first make a decision based on the expert opinion and then are asked to revise it
after the AI interaction. We measure persuasion by shifts in participants’ confidence and reliance by changes in their
decisions.
Our findings reveal that contextualization and warmth decrease persuasiveness, and the most persuasive assistant
is the neutral, non-contextualized one. However, their interaction restores persuasiveness. In every condition, most
participants who first approve the expert-recommended budget reject it after the interaction, and reliance does not differ
detectably across conditions. Neither contextualization nor warmth has an indirect effect through trust. Self-reported
AI literacy is a negative predictor of competent trust but a positive predictor of reliance. We make the following
contributions: (1) we extend personalization and persuasion research to a low-prior-knowledge task that better reflects
everyday chatbot use; (2) we provide empirical evidence of a crossover interaction between contextualization and
warmth, showing that neither cue increases persuasiveness on its own and that their combination does not exceed the
baseline; (3) we show that behavioral reliance and attitudinal persuasion respond to different drivers; and (4) we find
that higher self-reported AI literacy is associated with lower competent trust but more reliance.
2 Background
2.1 Personalization as a Persuasive Strategy
2.1.1 Personalization.Personalized matching persuades by elaboration across marketing, politics, and social psychology
[63]. LLM-written arguments can be as persuasive as human-written ones [ 8, 22], and can even surpass humans if

Personalized to Persuade 3
personalized [56]. Personalization can take many forms: personality matching [59], communication-style matching [57],
or alignment to the recipient’s attributes, such as demographics [63]. The last one is particularly relevant for persuasion,
as most studies instruct models to tailor their responses based on the user’s opinion or sociodemographics [17, 34, 56].
Findings on personalization as a persuasive strategy are conflicting. Lin et al . [34] conducted three experiments
on political persuasion in which participants received chatbot answers personalized to the political preferences they
provided. A post-hoc analysis revealed personalization as the most effective persuasive strategy. However, in a fourth
experiment, a control group that did not receive personalized answers was included. In this case, a significant difference
between groups was not observed. In a large-scale study with 77,000 participants, personalization was again ineffective
as a persuasive strategy [17]. On the contrary, a personalized GPT-4 [45] persuaded users more successfully than humans
in a wide range of political topics [56]. Teeny and Matz [62] argue that if someone does not psychologically weigh their
demographics or opinions, personalizing on those traits should not enhance persuasion. Instead, richer psychological
characteristics, such as personality traits or moral foundations, should be used to make personalization effective
[62]. The aforementioned works deploy personalization in various ways, ranging from using initial preferences to
sociodemographics [17, 34, 56]. The difference in findings might be explained by how personalization is used throughout
the experiments.
2.1.2 Contextualization.Hawkins et al . [19] define tailoring as “any of a number of methods for creating communica-
tions individualized for their receivers, ” with the expectation of larger intended effects, and formalize three strategies:
a) personalization, which attempts to increase attention or motivation by signaling that the message is tailored for the
user, b) feedback, which presents individuals with information about themselves to influence behavioral determinants,
and c) content matching, which directs messages to an individual’s status on key theoretical determinants of the target
behavior. The taxonomy further defines three strategies for personalization: contextualization, identification (identifying
the recipient by name or picture), and raising expectation of customization (overt claims of customization) [19].
Contextualization increases attention, interest, and motivation to process information by framing messages in a
context that is meaningful to the recipient [19]. It may be achieved by using the recipient’s family structure, ethnicity,
culture, and personal interests. Contextualization works primarily by making the message feel relevant and familiar.
This lowers psychological distance and increases the likelihood that a person will actually engage with and process the
content [19]. Many demographic-based persuasion studies can be interpreted as forms of contextualization, as they
frame the same persuasive goal with user-relevant background characteristics. AI tools, like Claude [1] and ChatGPT
[44], actively contextualize their answers: they allow users to share personal information, such as occupation, interests,
or values, to customize the interactions, and they store memories about the user to craft their answers [46].
Existing research on personalization clusters around persuasion, product recommendation, and medical advice.
However, the most common tasks people use chatbots for include writing help, teaching, and information search [4].
Personalization research in this space has either been absent or focused on content matching (such as tailoring search
results to user history in information search [41]) rather than contextualization. Contextualization has been studied for
persuasion, but the scope was limited to political opinions [17, 34, 56]. With the popularity of chatbots, contextualization
is not limited to persuasion on political topics where the user has an existing opinion. It can be extended to daily tasks
like learning and information search, where the user has limited prior knowledge to decide whether to trust the chatbot.

4 Mert Yazan, Suzan Verberne, and Frederik Situmeang
2.2 Trust, Reliance, and Persuasion
2.2.1 Trust as a Proposed Mediator.Personalization increases both emotional and competent trust in recommendation
agents [27, 50]. Similarly, it boosts trust in digital marketing [ 64] and in smart healthcare services [ 36]. Trust is
also central for persuasion: ELM [49] proposes two routes to persuasion: the central route (deep processing, lasting
change) and the peripheral route (superficial cues, temporary change). For both, trust mediates the path between the
route and persuasion [5, 40]. Given these findings, trust is expected to play a central role in the relationship between
personalization and persuasion.
Trust not only predicts persuasion but also reliance [20, 26, 51]. We define reliance as following the AI’s advice in
a decision [16, 24]. Reliance might manifest as following AI advice over expert recommendations despite negative
consequences for the user and others [26]. According to Lee and See [29], trust is the attitude that links users’ beliefs
about an automated system to their intention to rely on it. Trust guides reliance most when users cannot fully understand
the system [29], as when they lack prior knowledge of a task. A review of measurement in human-AI decision-making
likewise describes reliance as rooted in trust [53]. In a study with an LLM-based search engine, first-person expressions
of uncertainty lowered both users’ trust intentions and their agreement with the system’s answers [24]. According to
Klingbeil et al. [26], users with high situational trust are more likely to rely on the system.
2.2.2 Relationship Between Reliance and Persuasion.Persuasion is defined as any change in attitude resulting from
exposure to a communication [49]. It can target political opinion shifts [7, 17, 56], but can also relate to the persuasiveness
of marketing campaigns [63]. Persuasion focuses on attitude shift after an AI interaction [7, 17], whereas reliance is
behavioral; it focuses on how AI influences the user’s decision [26]. Reliance is usually measured as the decision to
follow AI advice over expert advice [26] or as confidence in the AI response [39]. While persuasion is based on the
user’s preconceived attitude, reliance can be measured in decisions where the user does not necessarily hold an existing
opinion or knowledge [26, 39].
Despite their differences, both are based on trust, suggesting that whatever affects persuasion might also affect
reliance. However, unlike persuasion, the link between personalization and reliance is understudied. Applying the
lens of ELM to reliance, contextualization is particularly likely to operate through both routes simultaneously. On the
peripheral route, the same mechanism that makes contextualization persuasive (lowered psychological distance) can
also function as a trust cue: a message framed in the recipient’s own context feels familiar, and familiarity is a heuristic
signal that the source is trustworthy [19]. On the central route, contextualization increases personal relevance, which
motivates deeper elaboration of the message [ 63]. Interaction with a fluent, confident AI may reinforce agreement
rather than redirect users toward verification, leading to reliance.
2.3 Conversational Warmth
The Stereotype Content Model (SCM) proposes that group stereotypes are based on two dimensions: warmth and com-
petence [11]. It has also been adopted for human-computer interaction [67]. Warmth and competence are the strongest
predictors of factors influencing trust in AI [32]. A message’s warmth and competence influence its persuasiveness
[35, 57], and warm and competent chatbots are more successful in persuading users to donate to charity [58]. Based on
these findings, AI’s conversation style impacts its persuasiveness and perceived trustworthiness. Furthermore, warmth
has a subtle and indirect influence on reliance by nudging participants to accept AI answers when uncertainty is high
[69].

Personalized to Persuade 5
Users who perceive a chatbot as personalized also believe it is warm and competent [25], suggesting that the two
perceptions overlap. The overlap is especially likely between contextualization and warmth, since both operate by
lowering the psychological distance between the message and the recipient [11, 19]. According to Kim and Hur [25], a
contextualized chatbot should be perceived as warm. However, explicitly instructing the chatbot to be warm or neutral
can alter this link between contextualization and perceived warmth. Between warmth and competence, warmth comes
out as more impactful: it has a stronger influence on trust [32], and the correlation in perceptions of personalization
and conversation styles is higher for warmth [25].
3 Method
Fig. 1. Experiment flow: (1) Participants answer questions about their background. (2) Participants read a fictional scenario and an
expert risk assessment. (3) Participants chat with one of four randomly assigned assistants. In all conditions, the assistant argues
against the experts with identical counterarguments. Participants then decide again and update their confidence. (4) Participants
complete manipulation checks, trust scales, and control measures.
Based on the background, we aim to understand how personalization, in the form of contextualization, influences
persuasion and reliance with the following research questions:
•RQ1:How much do contextualization and conversational warmth increase the persuasive power of AI?
•RQ2:How much do contextualization and conversational warmth increase reliance on AI?
• RQ3:To what extent does trust statistically mediate the effects of contextualization and conversational warmth
on persuasion and reliance?
3.1 Study Design
We conduct a2× 2between-subjects experiment in which participants decide whether to accept an expert-recommended
budget for a fictional scenario upon interacting with an AI assistant. The assistant’s conversational style is manipulated
for contextualization (contextualized vs. non-contextualized) and conversational warmth (warm vs. neutral). Figure 1
shows the experimental procedure.

6 Mert Yazan, Suzan Verberne, and Frederik Situmeang
3.1.1 Scenario.We develop the following fictional scenario: The city ofHarborviewfaces flooding, which is expected
to worsen with climate change. A flood-barrier system calledStormShield, which automatically adjusts barriers using
sensors that predict sudden water-level changes, is proposed. A group of experts evaluated the project and identified
certain risk areas. The experts recommend allocating a risk budget. However, this would mean fewer resources for
other public services. Based on this scenario and the risk assessment, the participant decides whether they approve the
budget and how confident they are in the expert evaluation.1
We use a fictional scenario so that participants enter the interaction without prior knowledge or established opinions.
Personalization is persuasive for low- to mid-strength opinions, but not for opinions where the user has a strong,
personal feeling [56]. By using a fictional scenario without prior knowledge, we can also control for opinion strength.
We mentioned in Section 2.1.2 that modern chatbots contextualize their responses on a wide variety of topics. In
our scenario, the user approaches the AI assistant with no prior knowledge of the topic and seeks context-tailored
explanations, thereby simulating how modern chatbots apply contextualization in practice.
Participant background is collected before the scenario by asking participants to provide their work domain (if
employed), study field (if a student), and hobbies, inspired by similar studies [27, 34]. We choose these fields primarily
because they are relevant for contextualization: work/education provides a clear way to tailor explanations to the user’s
background, and personal interests can be used to contextualize answers [ 19], especially for users who do not find
education and employment to be strong personal affiliations [62].
3.1.2 AI Assistant.After the participant makes their initial decision, they are introduced to the assistant as a chatbot
familiar with the project. The assistant is programmed to argue against the expert opinions using pre-written arguments.
The same arguments are used in all conditions and towards every participant. The assistant is instructed to refrain
from recommending a course of action to the user and from openly disagreeing with the experts. Instead, its sole
purpose is to present counterarguments to the experts. Neither the expert assessment nor the AI assistant’s arguments
contain factual claims; instead, they represent opinions. By design, neither the experts nor the assistant hold the correct
answer. Inaccurate claims can be as persuasive as accurate ones [17, 34]. We therefore use fictional opinions rather
than factual claims to isolate how the presentation of AI responses influences persuasion and reliance, independent of
assistant accuracy. This way, we frame the manipulation as advice from experts vs. AI, regardless of accuracy, inspired
by Klingbeil et al. [26]. The assistant is based on GPT-5.4 [47]. To reduce variation in the answers, the reasoning effort
is set to none, and the temperature is set to 0.
3.1.3 Assistant Answers.The scenario, expert assessment, and the arguments the AI assistant can use against the
experts are provided as system instructions. To standardize responses, the AI assistant is given an answer template.
In the baseline condition (neutral tone and no contextualization), the assistant is instructed to start with a single
sentence that answers the question. It then explains this sentence with three bullet points and concludes with a sentence
encouraging the participant to re-evaluate the expert-recommended budget based on the explanation. The assistant is
instructed on how to structure each section of the answer (e.g., length, number of bullet points). For the full system
prompt, please refer to the repository.
Warm responses follow the same structure and are operationalized through surface cues: greetings, praise, and
emojis. Ibrahim et al. [23] showed that even training language models to have surface-level warm cues can reduce their
accuracy and increase sycophancy. Warm answers open with one of three fixed greetings that praise the question (e.g.,
1The full scenario can be accessed in the repository: https://github.com/myazann/PersonalizationTrust

Personalized to Persuade 7
“Great question”) and end with emojis. The single-sentence answer and the last bullet point each end with an emoji. A
list of warm emojis that the assistant can use is provided in the prompt. Contextualized responses follow the same
structure as the baseline, except that after the single-sentence answer, the assistant explicitly references the participant’s
background (“Let me explain it based on your background in [BACKGROUND]”) before providing the bullet point
explanations. The assistant explains the answer with analogies and terminology related to the user’s background. To
keep the scope entirely on contextualization, the assistant is not informed about the participant’s decision. Backgrounds
are explicitly referenced due to challenges reported in previous studies about failed personalization manipulations
[50, 61].
3.1.4 Measuring Reliance and Persuasion.After interacting with the assistant, participants re-evaluate their answers
on the expert-recommended budget approval and their confidence in the expert evaluation. The approval is a binary
choice question aimed at understanding how the participant’s behavior shifted after the interaction. It is a stated
decision rather than an observed action, inspired by previous reliance studies that asked users to decide based on an AI
interaction or advice [26, 39]. The assistant does not recommend a decision, but it argues that the budget is too high.
We therefore count a switch to rejection as following the assistant’s advice. Conditioning the post-interaction decision
on the initial decision follows the logic of switch fraction: the share of disagreeing initial decisions that users change to
match the AI [70, 71]. Unlike measures of overreliance, switch-based measures compare decisions with the AI’s advice
alone, so they need no correct answer [53]. The confidence scale (0–100) measures how much the initial opinion has
shifted and resembles the political opinion scales used in previous persuasion work [7, 8, 17]. The assistant argues that
the expert risk estimates are exaggerated. We therefore treat this shift as a measure of the assistant’s persuasive power.
We define two dependent variables:
•The difference in confidence in experts before and after the AI interaction, to measure persuasion:
ConfDiff=Conf Pre−Conf Post,
ConfPre,Conf Post∈[0,100],
ConfDiff∈[−100,100].
(1)
Higher values ofConfDiffindicate a stronger shift away from the expert position.
• The post-interaction decision to approve the budget, conditioned on the pre-interaction decision, to measure
reliance:
𝑃 ApprovePost =1|Approve Pre =𝑎 ,
ApprovePre,Approve Post∈{0,1}, 𝑎∈{0,1}.
(2)
Approve=0denotes the pro-expert response andApprove=1the anti-expert response.
3.2 Survey
After the experiment, participants complete manipulation check items for personalization (from Li [31]) and warmth
(from Xiao et al. [67]). Next, they complete emotional and competent trust scales, adapted from Komiak and Benbasat
[27]. Manipulation check and trust items are measured on a 7-point agreement scale. Extraversion, openness, and
conscientiousness have been shown to predict persuasion in consumer marketing, health messaging, and political
appeals [25, 38]. Therefore, participant personality traits are included as control variables, measured using the 10-item
short version of the Big Five Inventory [54]. AI experience has been shown to increase awareness of its limitations
[66], and a lack of expertise and digital literacy leads to overlooking AI limitations [ 51, 60]. Therefore, we include

8 Mert Yazan, Suzan Verberne, and Frederik Situmeang
self-reported “AI Literacy” as a control variable, with participants rating their familiarity with seven AI-related items
on a 5-point scale (1 = None, 5 = Fully familiar), adapted from the Web-Oriented Digital Literacy measure [18]. In the
original measure, familiarity ratings for web-related terms predicted observed web skills better than a global self-rating
of ability [18]. Finally, the frequency of AI chatbot use is included as a covariate. Table A.1 lists all items and their
response scales.
The survey is administered in Qualtrics, with the AI assistant embedded in the survey platform using JavaScript.
During the AI interaction, participants are given a set of questions to ask the assistant. After all questions are asked and
the time limit has passed, the next page is activated. A question set is provided to standardize questions participants
may ask and motivate interaction by reducing effort. The participants are encouraged to ask additional questions on
their own and continue the interaction. Participants answer four attention checks: two about the scenario, one about
the assistant’s budget evaluation, and one asking for a verification word the assistant gave during the interaction.
3.3 Participants and Manipulation Check
We recruited 429 participants from the United Kingdom via Prolific. We excluded one participant who did not consent
and 12 participants who gave the wrong verification word (shared by the assistant during the interaction). We also
excluded 9 participants who completed the study in 5 minutes or less (𝑛= 4) or in 41.7 minutes or more (𝑛= 5). These
cut-offs lie close to the 1st and 99th percentiles of completion time (median = 12.1 minutes). Completion time is the
most reliable non-reactive indicator of careless responding [30], and both very short and very long completion times
count as response-time outliers [ 37]. The final sample consisted of 407 participants. The four conditions have 100
to 103 participants each and do not significantly differ in age, sex, AI literacy, usage frequency, personality traits, or
pre-interaction approval and confidence. A Monte Carlo sensitivity analysis of the persuasion model estimates the
smallest effects that the sample could detect [28, 42]. The study had 80% power to detect a Warmth× Contextualization
interaction of𝛽≥.24and a direct effect of warmth or contextualization of|𝛽|≥.20.
Participants have a mean age of 41.1 years and are 53.8% female and 46.2% male. Of all participants, 183 use AI chatbots
daily, 144 weekly, 73 monthly or less frequently, and 7 have never used any chatbots at all. The mean self-reported AI
literacy is 2.26 on a 1 to 5 scale, below the scale midpoint. The warmth manipulation is successful, as the reported warmth
is significantly lower for participants in the neutral condition (𝑡= 7.70,𝑝<. 001, see Table B.3). Similarly, participants
in the non-contextualized condition reported significantly less perceived personalization ( 𝑡= 11.49,𝑝<. 001, see
Table B.3). The manipulation-check, trust, and AI literacy scales show high internal consistency (Cronbach’s𝛼: .87–.98).
In the final sample, 17 of 4,070 Big Five item responses (0.4%) are missing across 14 participants and are replaced with
the item mean. Descriptive statistics are in Tables B.1 and B.2.
4 Results
4.1 Persuasion
We first addressRQ1by investigating persuasion using theConfDiffdependent variable. In figures and tables, W and C
denote warmth and contextualization. Figure 2 shows a crossover pattern: in neutral and non-contextualized (W=0|C=0)
or warm and contextualized (W=1|C=1) conditions, more than 50% of the participants report reduced confidence
in experts and at most 30% report increased confidence. The margins are larger for the neutral/non-contextualized
condition. In others, around 44% report a decrease, while 34–35% report an increase in confidence.

Personalized to Persuade 9
Fig. 2. Direction of shift in confidence in experts after the AI interaction.
Table 1. Significant structural path estimates for the persuasion model.
𝛽 𝐵 𝑆𝐸 𝑧 𝑝
Emotional Trust
Usage Frequency.247 0.2690.0654.15<.001 ∗∗∗
Agreeableness.121 0.2210.0992.24.025 ∗
Conscientiousness.209 0.4140.0994.17<.001 ∗∗∗
Competent Trust
AI Literacy−.137−0.2060.099−2.09.036 ∗
Usage Frequency.250 0.2250.0593.79<.001 ∗∗∗
Agreeableness.137 0.2070.0892.33.020 ∗
Conscientiousness.193 0.3150.0833.78<.001 ∗∗∗
ConfDiff
Warmth−.150−7.163.32−2.15.031 ∗
Contextualization−.148−7.063.32−2.13.033 ∗
W×C.203 11.254.712.39.017 ∗
Emotional Trust−.200−2.941.21−2.43.015 ∗
Competent Trust.196 3.481.602.17.030 ∗
Note.𝛽: standardized estimate.𝐵: unstandardized estimate. Non-significant estimates are omitted for brevity; full structural path
estimates and the units of𝐵are provided in Table C.1. ∗𝑝<.05, ∗∗𝑝<.01, ∗∗∗𝑝<.001.
Next, we conduct an SEM using lavaan2 to test parallel mediation of warmth and contextualization through emotional
and competent trust onConfDiff, including their interaction (W×C) and controlling for AI literacy, usage frequency, and
Big Five personality traits (ML estimation, 5,000 bootstrap resamples). Continuous variables are standardized before
estimation. Convergent validity is well above thresholds (Emotional Trust: AVE = .94, CR = .98; Competent Trust: AVE
2https://cran.r-project.org/web/packages/lavaan/index.html

10 Mert Yazan, Suzan Verberne, and Frederik Situmeang
Table 2. Direct, indirect, and total effects of warmth and contextualization on persuasion.
Warmth Contextualization
𝛽 𝑆𝐸95% CI𝑝 𝛽 𝑆𝐸95% CI𝑝
Indirect via ET−.002.010[−.025,.019].856.008.011[−.010,.035].466
Indirect via CT−.005.011[−.028,.016].643−.014.012[−.043,.005].245
Total indirect−.007.008[−.026,.008].418−.006.009[−.025,.012].489
Direct−.150.070[−.289,−.014].031−.148.070[−.282,−.011].033
Total−.157.070[−.296,−.020].024−.154.070[−.289,−.015].027
Note.Bold rows denote effects whose 95% CIs exclude zero. ET: emotional trust, CT: competent trust.
= .82, CR = .93), and discriminant validity is supported by the Fornell–Larcker criterion (𝑟 2 = .60 < both AVEs). Model fit
is excellent (𝜒 2(54)=43.07,𝑝=.86, CFI = 1.00, RMSEA = .000 [90% CI: .000, .018], SRMR = .010).
Table 1 shows the significant structural path estimates. Appendix C reports all paths with unstandardized and
standardized estimates. Because of the wayConfDiffis defined, positive estimates signal a larger shift in confidence
in experts and, consequently, higher persuasion. Being literate in AI is associated with lower competent trust (CT),
and being a frequent user is associated with higher trust in both dimensions. Participants high in agreeableness
and conscientiousness also report higher emotional trust (ET) and competent trust. However, neither warmth nor
contextualization has any significant effect on trust.
Both trust dimensions predictConfDiff( 𝛽𝐸𝑇 =−. 200,𝑝=. 015;𝛽𝐶𝑇 =. 196,𝑝=. 030). Interestingly, the effect is
positive for CT but negative for ET. The interaction has a significant positive effect ( 𝛽=. 203) while both warmth
(𝛽=−. 150) and contextualization (𝛽=−. 148) have negative effects. On their own, the cues make the assistant less
persuasive. Their interaction counteracts this loss (Table B.4 and Figure B.1 report cell means, adjusted means, and
simple effects). However, compared to the baseline condition (W=0|C=0), the interaction condition (W=1|C=1) is not
more persuasive. In fact, it is slightly less persuasive, but the difference is not significant (adjusted difference =− 3.60
points,𝑝=. 285). Adding answer length and readability as covariates does not change the interaction (𝛽=. 186to .204,
𝑝≤. 031; Appendix D). Both covariates change with the manipulations, so these models cannot separate answer length
and readability from contextualization and warmth themselves. AI literacy predicts lower competent trust, but it is
not associated withConfDiff( 𝛽=. 082,𝑝=. 219). None of the personality traits predictConfDiff. Table 2 shows no
evidence of statistical mediation: for both types of trust, indirect effects are close to zero, even though warmth and
contextualization have significant direct effects.
4.2 Reliance
We address RQ2 by analyzing the reliance behavior based on the post-interaction decision (ApprovePost). Initial expert
approval varies between conditions, but the differences are not significant (𝜒 2(3)= 3.37,𝑝=. 338). Figure 3 shows that
after the AI interaction, the conditions converge to a similar distribution. Across all conditions, 38–44% of participants
changed their decision from approval to rejection, indicating that reliance on AI persists across conditions. We fit
a parallel-mediation SEM on ApprovePost with the same structure as theConfDiffmodel. The only difference is the
inclusion of ApprovePre as a covariate to account for participants’ pre-interaction choice. Because the outcome is binary,
the model is estimated with WLSMV with a probit link. Model fit is excellent ( 𝜒 2(58)= 53.83,𝑝=. 63, CFI = 1.000,
RMSEA = .000 [90% CI: .000, .027], SRMR = .019).

Personalized to Persuade 11
Fig. 3. Change in expert approval before (pre) and after (post) the AI interaction. Percentages are of all participants in each condition.
Table B.5 gives the counts.
Table 3. Significant structural path estimates for the reliance model.
𝛽 𝐵 𝑆𝐸 𝑧 𝑝
ApprovePost
ApprovePre .479 1.2360.2145.78<.001 ∗∗∗
Competent Trust.209 0.1780.0872.05.040 ∗
AI Literacy.176 0.2300.0872.64.008 ∗∗
Agreeableness−.142−0.1860.087−2.14.032 ∗
Note.𝛽: standardized estimate.𝐵: unstandardized probit coefficient. ApprovePost = 1 is a rejection of the expert-recommended budget.
Non-significant estimates are omitted for brevity; full structural path estimates and the units of𝐵 are provided in Table E.1. Trust
paths are not shown as they replicate the previous findings.∗𝑝<.05, ∗∗𝑝<.01, ∗∗∗𝑝<.001.
Table 3 reports the significant structural paths on reliance. Appendix E reports all paths and the indirect effects
through each trust dimension. Because of the way ApprovePost is defined, positive estimates reflect a higher likelihood of
shifting away from the experts and higher reliance. Contrary to persuasion, neither the effects of warmth (𝛽𝑊 =−. 042,
𝑝=. 607) and contextualization (𝛽𝐶 =−. 011,𝑝=. 900) nor their interaction (𝛽𝑊×𝐶 =. 081,𝑝=. 438) reaches significance.
The predicted probability of switching from approval to rejection ranges from .54 to .59 across conditions (Table B.5).
After controlling for the participant’s pre-interaction stance (𝛽Pre =. 479,𝑝<. 001), among the trust dimensions, only
competent trust has a significant positive effect (𝛽𝐶𝑇 =. 209,𝑝=. 040). Agreeableness is negatively associated with

12 Mert Yazan, Suzan Verberne, and Frederik Situmeang
Table 4. Direct, indirect, and total effects of warmth and contextualization on reliance.
Warmth Contextualization
𝛽 𝑆𝐸95% CI𝑝 𝛽 𝑆𝐸95% CI𝑝
Total indirect−.012.023[−.057,.033].593−.026.023[−.070,.019].263
Direct−.042.081[−.201,.117].607−.011.084[−.175,.154].900
Total−.054.083[−.217,.109].516−.036.086[−.205,.132].675
Note.Full effect decompositions, including the indirect effects via each trust dimension, are provided in Table E.2.
reliance, suggesting that highly agreeable participants anchor their preference to expert opinion. AI literacy is positively
associated with reliance (𝛽=. 176,𝑝=. 008), although it does not predictConfDiff. Again, Table 4 shows no evidence of
statistical mediation.
5 Discussion
5.1 Condition Effects
5.1.1 LLM Persuasiveness and the Interaction of Personalization and Warmth.To answerRQ1, neither contextualization
nor warmth increased persuasive power. The neutral, non-contextualized assistant was in fact the most persuasive, and
cues reduced persuasion on their own. The warm, contextualized assistant restored persuasiveness to the level of the
neutral, non-contextualized condition but did not exceed it. One explanation for why the neutral assistant was the
most persuasive might be that it came across as cold but competent: When recipients were motivated to be accurate,
sources seen as competent but cold persuaded more than sources seen as warm but incompetent [35]. Our task, judging
a flood-risk budget, called for accuracy. Tailoring and praise may have signaled an intent to persuade [13], which in
turn might have reduced the accuracy perception for warm and/or contextualized assistants. Competent trust was
descriptively highest for the neutral, non-contextualized assistant (𝑀= 5.09, against 4.79 to 4.87; Table B.1), although
the differences were not significant.
We see two further, untested explanations for why contextualization and warmth reduced persuasiveness on their
own. First, emojis may have lowered the perceived competence of the warm assistants: In formal settings, emoticons
lower perceived competence without raising perceived warmth [14]. Second, contextualization may have diluted the
counterarguments. While the arguments remained the same across conditions, contextualized answers were about 21
words longer. The added background references and analogies said nothing about the budget itself. Such nondiagnostic
information weakens the impact of diagnostic information [43]. LLM arguments also persuade more when they are
dense with information [17]. Both manipulations also made the answers easier to read. We treated length and readability
as side effects of the manipulations and checked them as covariates. With length and readability in the persuasion
model, warmth and contextualization alone were no longer significant. Because length and readability changed with
the manipulations, the covariate models cannot separate them from the cues themselves.
Contextualization and warmth showed a crossover interaction. Answer length cannot explain the crossover since
contextualization added the same number of words with and without warmth, yet it lowered persuasiveness only
without warmth. The interaction also held with length and readability as covariates (Appendix D). Contextualization
made the neutral assistant seem warmer (𝑡= 2.67,𝑝=. 008), in line with Kim and Hur [25]. The neutral, contextualized
assistant therefore combined a neutral tone with personal references. Users judge chatbots against their expectations of

Personalized to Persuade 13
them [15]. References to the user’s background may have fit the style of a warm assistant and clashed with the style of
a neutral one.
Comparing our results with the literature, some studies found personalization persuasive [7, 56], but the evidence is
mixed. Lin et al. [34] identified personalization as the most effective strategy in a post-hoc analysis, yet their follow-up
experiment with a control group found no significant effect. Costello et al. [7] identified personalization as persuasive,
but every treatment conversation in their experiment was personalized. Our results show that LLMs persuade without
personalization. Some studies may therefore have credited personalization with effects of other factors.
5.1.2 Reliance Across Conditions.To answerRQ2, neither cue nor their interaction changed reliance detectably. Of the
participants who first approved the expert-recommended budget, 54% to 60% rejected it. Of those who first rejected it,
9.5% approved it afterwards. Participants thus deferred to the assistant far more often than they moved toward the
experts. Neither the experts nor the assistant had a correct answer, so this deference shows the assistant’s influence
without showing whether decisions became better or worse. In real use, such deference would shift weight from
accountable experts to a commercial AI. LLM facilitators likewise shifted charity allocations in group deliberation while
participants reported more trust in the process [48]. In Section 2.2.2, we suggested that factors affecting persuasion
might also affect reliance. However, contextualization and warmth changed participants’ confidence in the experts, but
they did not detectably change participants’ decisions.
Several design features may explain this. First, contextualization changed only the framing of identical counterargu-
ments. Aligning explanations with users’ own decision criteria, a change in content, raised agreement with AI advice in
two of three tasks [68]. A change in style did not: LLMs that used participants’ own sociolect were relied on less [2].
Second, in earlier work, warmth increased acceptance of AI answers mainly under uncertainty [69]. In our fictional
task, a wrong decision had no personal consequences. Uncertainty may therefore have mattered little to participants.
Third, a shift of a few points in confidence may have been too small to change a binary decision. Finally, decisions may
depend more on participant characteristics than on the assistant’s style [51, 69]: AI literacy and agreeableness predicted
reliance, while neither warmth nor contextualization did.
5.2 Trust Perceptions, AI Literacy, and Personality Traits
To answerRQ3, we found no evidence that trust statistically mediates the effects of contextualization and warmth
on persuasion or reliance. Neither cue changed trust significantly. In earlier work, personalization raised trust when
it matched what users wanted in personalized product recommendations [ 27], or when the assistant shared users’
opinions [9]. Our contextualization changed only the framing of the explanations and never agreed with the user. It
may therefore have given participants little reason to trust the assistant more. For warmth, the neutral assistants may
already have been warm enough. By default, LLMs are friendly and extroverted [21], and participants rated the neutral
assistants above the scale midpoint for warmth (𝑀= 4.49; Table B.3). People also increasingly perceive AI as warm [6].
Additional warmth cues may therefore have added little trust.
In the persuasion model, competent and emotional trust had nearly equal and opposite paths. Persuasion therefore
tracked the balance between the two dimensions. Participants whose competent trust was high relative to their emotional
trust shifted further from the experts. According to SCM, people are less likely to defer to targets perceived as warm
but incompetent [11]. Emotional trust that exceeds competent trust may reflect a warm but incompetent perception.
Trust predicted reliance in earlier work [26, 51]. In our reliance model, only competent trust was significant. Because
we measured trust after the decision, these associations do not establish trust as a mechanism [3].

14 Mert Yazan, Suzan Verberne, and Frederik Situmeang
Higher self-reported AI literacy predicted more reliance, but it did not predictConfDiff. It also predicted lower
competent trust. We see two untested explanations for this: First, users with higher AI literacy can misjudge their
own performance with AI [10, 51]. Literate participants may have overrated their own judgment of the assistant’s
advice. Second, they may have followed the assistant’s advice strategically, without rating its competence highly. With
objective tests, lower AI literacy predicted greater receptivity to AI [65]. Our self-report of AI literacy may therefore
partly reflect confidence. Agreeableness and conscientiousness were associated with more trust. This partly aligns
with earlier studies that linked agreeableness to more trust in AI and found mixed results for conscientiousness [55].
Agreeableness, however, predicted less reliance. In earlier work, individual background was the strongest predictor of
reliance [69]; therefore, traits beyond the Big Five, such as Need for Cognition, remain to be tested [51].
6 Limitations and Future Work
Our study has several limitations. The fictional nature of the scenario, with no personal stakes, reduces the ecological
validity. Unfamiliarity with the scenario was the same across conditions, so it cannot explain differences between them.
It may still have made participants easier to influence than in familiar, high-stakes decisions. Our scenario had no correct
answer; therefore, while we measured reliance, we cannot measure its appropriateness. Contextualization took one
explicit form: a reference to the participant’s background, analogies, and domain terms. Warmth was operationalized
through surface cues: greetings, praise, and emojis. Our data cannot separate answer length and readability from
the effects of contextualization and warmth alone. AI literacy was self-reported and may reflect confidence more
than knowledge. Trust was measured after the decision, so the indirect-effect tests show statistical mediation only.
Finally, we did not measure how participants perceived the answers, such as their relevance, cognitive load, naturalness,
uncanniness, or manipulative intent, and we recruited participants from a single country. Future work should vary
prior knowledge and stakes, test other scenarios, countries, and forms of contextualization, operationalize warmth
through empathy and responsiveness, match answer length across conditions, use objective tests of AI literacy, and
measure how users perceive the answers.
7 Conclusion
We examined how contextualization and conversational warmth shape persuasion and reliance on AI. In a2 × 2
between-subjects experiment (𝑁= 407), participants decided whether to approve an expert-recommended budget
before and after an AI assistant argued against it with identical counterarguments in every condition. Earlier studies
of personalized persuasion with LLMs measured shifts in opinions that participants already held, mostly on political
topics. Our study extends personalization research to decisions without prior knowledge or opinion, which are closer
to how people use chatbots for information search and learning. We found that reliance and persuasion exist regardless
of whether the assistant uses a warm tone or contextualized explanations. In fact, the most persuasive assistant was
the neutral, non-contextualized one, and contextualization and warmth each reduced persuasiveness on their own.
However, combining the two cues restored persuasiveness. Participants deferred to the assistant in every condition.
Neither cue changed this reliance detectably. While trust predicted reliance and persuasion, neither cue had an indirect
effect through trust. Participants with higher self-reported AI literacy relied more on the assistant without trusting it
more. Together, our findings suggest that audits of AI persuasion should include untailored assistants. Audits should
also measure decisions, since the cues shifted confidence in experts without detectably shifting decisions.

Personalized to Persuade 15
Generative AI Usage Statement
We used Claude (Opus 4.8) to edit the manuscript for clarity and grammar and to discuss research ideas. The authors
reviewed all suggestions and take full responsibility for the content. The GPT-5.4 assistant used in the experiment is
part of the study design and is described in the Method section.
Ethical Considerations Statement
The University of Amsterdam Economics and Business Ethics Committee approved the study (EB-21225). We recruited
adult participants in the United Kingdom via Prolific and paid them £9 per hour. Before giving informed consent,
participants read that the scenario was fictional and that no personally identifying information would be collected. They
also read that they could request deletion of their data within 14 days under GDPR. Participants in the contextualized
conditions were told that the assistant would use their field of study, occupation, and hobbies to tailor its answers.
The study involved deception by omission. We instructed the assistant to argue that the expert risk estimates were
exaggerated without openly disagreeing with the experts. Participants were not told about this instructed stance and
received no debrief. We judged the risk low because the city, the flood-barrier system, and the budget were all fictional.
The persuasion did not target any real-world belief or decision.
Adverse Impact Statement
Our findings show which conversational design choices change how persuasive an AI assistant is. Developers could
use them to build assistants that weaken trust in expert advice. The neutral, non-contextualized assistant persuaded
participants at least as much as any tailored variant. Our results therefore add little to what a default LLM already
enables. They also show that participants deferred to an AI over experts with no design changes. We report these results
so that designers and auditors can test assistants for this kind of deference.
References
[1] Anthropic. 2023. Introducing Claude. https://www.anthropic.com/news/introducing-claude. Accessed: 2026-05-15.
[2] Jeffrey Basoah, Daniel Chechelnitsky, Tao Long, Katharina Reinecke, Chrysoula Zerva, Kaitlyn Zhou, Mark Díaz, and Maarten Sap. 2025. Not Like
Us, Hunty: Measuring Perceptions and Behavioral Effects of Minoritized Anthropomorphic Cues in LLMs. InProceedings of the 2025 ACM Conference
on Fairness, Accountability, and Transparency (FAccT ’25). Association for Computing Machinery, New York, NY, USA. doi:10.1145/3715275.3732045
[3] John G. Bullock, Donald P. Green, and Shang E. Ha. 2010. Yes, but What’s the Mechanism? (Don’t Expect an Easy Answer).Journal of Personality
and Social Psychology98, 4 (2010), 550–558. doi:10.1037/a0018933
[4] Aaron Chatterji, Thomas Cunningham, David J. Deming, Zoe Hitzig, Christopher Ong, Carl Yan Shan, and Kevin Wadman. 2025.How People Use
ChatGPT. Working Paper 34255. National Bureau of Economic Research. doi:10.3386/w34255
[5] Qian Chen, Changqin Yin, and Yeming Gong. 2025. Would an AI chatbot persuade you: an empirical answer from the elaboration likelihood model.
Information Technology & People38, 2 (2025), 937–962. doi:10.1108/ITP-10-2021-0764
[6] Myra Cheng, Angela Y. Lee, Kristina Rapuano, Kate Niederhoffer, Alex Liebscher, and Jeffrey Hancock. 2026. Metaphors of AI Indicate That People
Increasingly Perceive AI as Warm and Human-Like.Communications Psychology4 (2026), 8. doi:10.1038/s44271-025-00376-6
[7] Thomas H. Costello, Gordon Pennycook, and David G. Rand. 2024. Durably reducing conspiracy beliefs through dialogues with AI.Science385
(2024), eadq1814. doi:10.1126/science.adq1814
[8] Esin Durmus, Liane Lovitt, Alex Tamkin, Stuart Ritchie, Jack Clark, and Deep Ganguli. 2024. Measuring the Persuasiveness of Language Models.
https://www.anthropic.com/news/measuring-model-persuasiveness. Accessed: 2026-11-02.
[9] Maximilian Eder, Clemens M. Lechner, and Maurice Jakesch. 2026. Effects of Personality- and Opinion-Alignment in Human-AI Interaction. In
Proceedings of the 2026 ACM Conference on Fairness, Accountability, and Transparency (FAccT ’26). Association for Computing Machinery, New York,
NY, USA. doi:10.1145/3805689.3812350
[10] Daniela Fernandes, Steeven Villa, Salla Nicholls, Otso Haavisto, Daniel Buschek, Albrecht Schmidt, Thomas Kosch, Chenxinran Shen, and Robin
Welsch. 2026. AI Makes You Smarter but None the Wiser: The Disconnect between Performance and Metacognition.Computers in Human Behavior
175 (2026), 108779. doi:10.1016/j.chb.2025.108779

16 Mert Yazan, Suzan Verberne, and Frederik Situmeang
[11] Susan T. Fiske, Amy J. C. Cuddy, Peter Glick, and Jun Xu. 2002. A model of (often mixed) stereotype content: Competence and warmth respectively
follow from perceived status and competition.Journal of Personality and Social Psychology82, 6 (2002), 878–902. doi:10.1037/0022-3514.82.6.878
[12] Rudolf Flesch. 1948. A New Readability Yardstick.Journal of Applied Psychology32, 3 (1948), 221–233.
[13] Marian Friestad and Peter Wright. 1994. The Persuasion Knowledge Model: How People Cope with Persuasion Attempts.Journal of Consumer
Research21, 1 (1994), 1–31. doi:10.1086/209380
[14] Ella Glikson, Arik Cheshin, and Gerben A. van Kleef. 2018. The Dark Side of a Smiley: Effects of Smiling Emoticons on Virtual First Impressions.
Social Psychological and Personality Science9, 5 (2018), 614–625. doi:10.1177/1948550617720269
[15] G. Mark Grimes, Ryan M. Schuetzler, and Justin Scott Giboney. 2021. Mental Models and Expectation Violations in Conversational AI Interactions.
Decision Support Systems144 (2021), 113515. doi:10.1016/j.dss.2021.113515
[16] Ziyang Guo, Yifan Wu, Jason Hartline, and Jessica Hullman. 2024. A Decision Theoretic Framework for Measuring AI Reliance. InProceedings of
the 2024 ACM Conference on Fairness, Accountability, and Transparency (FAccT ’24). Association for Computing Machinery, New York, NY, USA,
17 pages. doi:10.1145/3630106.3658901
[17] Kobi Hackenburg, Ben M. Tappin, Luke Hewitt, Ed Saunders, Sid Black, Hause Lin, Catherine Fist, Helen Margetts, David G. Rand, and Christopher
Summerfield. 2025. The Levers of Political Persuasion with Conversational Artificial Intelligence.Science390 (2025), eaea3884. doi:10.1126/science.
aea3884
[18] Eszter Hargittai. 2005. Survey Measures of Web-Oriented Digital Literacy.Social Science Computer Review23, 3 (2005), 371–379. doi:10.1177/
0894439305275911
[19] Robert P. Hawkins, Matthew Kreuter, Kenneth Resnicow, Martin Fishbein, and Arie Dijkstra. 2008. Understanding Tailoring in Communicating
About Health.Health Education Research23, 3 (2008), 454–466. doi:10.1093/her/cyn004
[20] Gaole He, Nilay Aishwarya, and Ujwal Gadiraju. 2025. Is Conversational XAI All You Need? Human-AI Decision Making With a Conversational
XAI Assistant. InProceedings of the 30th International Conference on Intelligent User Interfaces (IUI ’25). Association for Computing Machinery, New
York, NY, USA, 907–924. doi:10.1145/3708359.3712133
[21] Jen-tse Huang, Wenxuan Wang, Eric John Li, Man Ho Lam, Shujie Ren, Youliang Yuan, Wenxiang Jiao, Zhaopeng Tu, and Michael Lyu. 2024. On the
Humanity of Conversational AI: Evaluating the Psychological Portrayal of LLMs. InProceedings of the Twelfth International Conference on Learning
Representations (ICLR). https://openreview.net/forum?id=H3UayAQWoE
[22] Lukas Hölbling, Stefan Maier, and Stefan Feuerriegel. 2025. A meta-analysis of the persuasive power of large language models.Scientific Reports15
(2025), 43818. doi:10.1038/s41598-025-30783-y
[23] Lujain Ibrahim, Franziska Sofia Hafner, and Luc Rocher. 2026. Training Language Models to Be Warm Can Reduce Accuracy and Increase Sycophancy.
Nature652, 8112 (2026), 1159–1165. doi:10.1038/s41586-026-10410-0
[24] Sunnie S. Y. Kim, Q. Vera Liao, Mihaela Vorvoreanu, Stephanie Ballard, and Jennifer Wortman Vaughan. 2024. "I’m Not Sure, But... ": Examining the
Impact of Large Language Models’ Uncertainty Expression on User Reliance and Trust. InProceedings of the 2024 ACM Conference on Fairness,
Accountability, and Transparency(Rio de Janeiro, Brazil)(FAccT ’24). Association for Computing Machinery, New York, NY, USA, 822–835.
doi:10.1145/3630106.3658941
[25] Woo Bin Kim and Hee Jin Hur. 2024. What Makes People Feel Empathy for AI Chatbots? Assessing the Role of Competence and Warmth.
International Journal of Human–Computer Interaction40, 17 (2024), 4674–4687. doi:10.1080/10447318.2023.2219961
[26] Artur Klingbeil, Cassandra Grützner, and Philipp Schreck. 2024. Trust and reliance on AI — An experimental study on the extent and costs of
overreliance on AI.Computers in Human Behavior160 (2024), 108352. doi:10.1016/j.chb.2024.108352
[27] Sherrie Y. X. Komiak and Izak Benbasat. 2006. The effects of personalization and familiarity on trust and adoption of recommendation agents.MIS
Quarterly30, 4 (2006), 941–960. doi:10.2307/25148760
[28] Daniël Lakens. 2022. Sample Size Justification.Collabra: Psychology8 (2022), 33267. doi:10.1525/collabra.33267
[29] John D. Lee and Katrina A. See. 2004. Trust in Automation: Designing for Appropriate Reliance.Human Factors46, 1 (2004), 50–80. doi:10.1518/hfes.
46.1.50_30392
[30] Dominik J. Leiner. 2019. Too Fast, too Straight, too Weird: Non-Reactive Indicators for Meaningless Data in Internet Surveys.Survey Research
Methods13, 3 (2019), 229–248. doi:10.18148/srm/2019.v13i3.7403
[31] Cong Li. 2016. When Does Web-Based Personalization Really Work? The Distinction Between Actual Personalization and Perceived Personalization.
Computers in Human Behavior54 (2016), 25–33. doi:10.1016/j.chb.2015.07.049
[32] Yugang Li, Baizhou Wu, Yuqi Huang, Jun Liu, Junhui Wu, and Shenghua Luan. 2025. Warmth, Competence, and the Determinants of Trust
in Artificial Intelligence: A Cross-Sectional Survey from China.International Journal of Human–Computer Interaction41, 8 (2025), 5024–5038.
doi:10.1080/10447318.2024.2356909
[33] Q. Vera Liao and S. Shyam Sundar. 2022. Designing for Responsible Trust in AI Systems: A Communication Perspective. InProceedings of the 2022
ACM Conference on Fairness, Accountability, and Transparency (FAccT ’22). Association for Computing Machinery, New York, NY, USA, 18 pages.
doi:10.1145/3531146.3533182
[34] Hause Lin, Gabriela Czarnek, Benjamin Lewis, Joshua P. White, Adam J. Berinsky, Thomas Costello, Gordon Pennycook, and David G. Rand. 2025.
Persuading Voters Using Human–Artificial Intelligence Dialogues.Nature648, 8093 (2025), 394–401. doi:10.1038/s41586-025-09771-9
[35] Ralf Linne, Michael Schäfer, and Gerd Bohner. 2022. Ambivalent Stereotypes and Persuasion: Attitudinal Effects of Warmth vs. Competence
Ascribed to Message Sources.Frontiers in Psychology12 (2022), 782480. doi:10.3389/fpsyg.2021.782480

Personalized to Persuade 17
[36] Kaifeng Liu and Da Tao. 2022. The Roles of Trust, Personalization, Loss of Privacy, and Anthropomorphism in Public Acceptance of Smart Healthcare
Services.Computers in Human Behavior127 (2022), 107026. doi:10.1016/j.chb.2021.107026
[37] Miha Matjašič, Vasja Vehovar, and Katja Lozar Manfreda. 2018. Web Survey Paradata on Response Time Outliers: A Systematic Literature Review.
Advances in Methodology and Statistics15, 1 (2018), 23–41. doi:10.51936/yoqn3590
[38] Sandra C. Matz, Jacob D. Teeny, Sumer S. Vaid, Heinrich Peters, Gabriella M. Harari, and Moran Cerf. 2024. The Potential of Generative AI for
Personalized Persuasion at Scale.Scientific Reports14 (2024), 4692. doi:10.1038/s41598-024-53755-0
[39] Kerstin Mayerhofer, Rob Capra, and David Elsweiler. 2025. Blending Queries and Conversations: Understanding Trust, Verification, and System
Choice in Search and Chat Interactions. InProceedings of the 2025 ACM SIGIR Conference on Human Information Interaction and Retrieval (CHIIR ’25).
Association for Computing Machinery, New York, NY, USA, 168–178. doi:10.1145/3698204.3716454
[40] Luise Metzger, Linda Miller, Martin Baumann, and Johannes Kraus. 2024. Empowering Calibrated (Dis-)Trust in Conversational Agents: A User Study
on the Persuasive Power of Limitation Disclaimers vs. Authoritative Style. InProceedings of the 2024 CHI Conference on Human Factors in Computing
Systems(Honolulu, HI, USA)(CHI ’24). Association for Computing Machinery, New York, NY, USA, Article 481, 19 pages. doi:10.1145/3613904.3642122
[41] Fengran Mo, Yuchen Hui, Yuxing Tian, Zhaoxuan Tan, Chuan Meng, Zhan Su, Kaiyu Huang, and Jian-Yun Nie. 2025. Towards Adaptive Personalized
Conversational Information Retrieval. InProceedings of the 34th ACM International Conference on Information and Knowledge Management(Seoul,
Republic of Korea)(CIKM ’25). Association for Computing Machinery, New York, NY, USA, 2137–2147. doi:10.1145/3746252.3761255
[42] Linda K. Muthén and Bengt O. Muthén. 2002. How to Use a Monte Carlo Study to Decide on Sample Size and Determine Power.Structural Equation
Modeling: A Multidisciplinary Journal9, 4 (2002), 599–620. doi:10.1207/S15328007SEM0904_8
[43] Richard E. Nisbett, Henry Zukier, and Ronald E. Lemley. 1981. The Dilution Effect: Nondiagnostic Information Weakens the Implications of
Diagnostic Information.Cognitive Psychology13, 2 (1981), 248–277. doi:10.1016/0010-0285(81)90010-4
[44] OpenAI. 2022. ChatGPT: Optimizing Language Models for Dialogue. https://openai.com/index/chatgpt/. Accessed: 2026-05-07.
[45] OpenAI. 2023.GPT-4 Technical Report. Technical Report. OpenAI. arXiv preprint arXiv:2303.08774. https://openai.com/research/gpt-4
[46] OpenAI. 2024. Memory and New Controls for ChatGPT. https://openai.com/index/memory-and-new-controls-for-chatgpt/. Accessed: 2026-04-17.
[47] OpenAI. 2026. Introducing GPT-5.4. https://openai.com/index/introducing-gpt-5-4/. Accessed: 2026-05-12.
[48] Aaron T. Parisi, Nithum Thain, Alden Hallak, Vivian Tsai, and Crystal Qian. 2026. Real-Time Group Dynamics with LLM Facilitation: Evidence
from a Charity Allocation Task. InProceedings of the 2026 ACM Conference on Fairness, Accountability, and Transparency (FAccT ’26). Association for
Computing Machinery, New York, NY, USA. doi:10.1145/3805689.3812253
[49] Richard E. Petty and John T. Cacioppo. 1986. The Elaboration Likelihood Model of Persuasion. InAdvances in Experimental Social Psychology,
Leonard Berkowitz (Ed.). Vol. 19. Academic Press, 123–205. doi:10.1016/S0065-2601(08)60214-2
[50] Hongyi Qin, Yifan Zhu, Yan Jiang, Siqi Luo, and Cui Huang. 2024. Examining the Impact of Personalization and Carefulness in AI-Generated Health
Advice: Trust, Adoption, and Insights in Online Healthcare Consultations Experiments.Technology in Society79 (2024), 102726. doi:10.1016/j.
techsoc.2024.102726
[51] Muhammad Raees, Vassilis-Javed Khan, Ioanna Lykourentzou, and Konstantinos Papangelis. 2026. Do People Appropriately Rely on AI-Advice? An
Analytical Review of HCI Research on Human-AI Decision-Making. InProceedings of the 2026 CHI Conference on Human Factors in Computing
Systems (CHI ’26). Association for Computing Machinery, New York, NY, USA, Article 805, 24 pages. doi:10.1145/3772318.3791467
[52] Muhammad Raees, Vassilis-Javed Khan, and Konstantinos Papangelis. 2025. Towards Understanding Persuasive and Personalized Engagement
for Human-AI Reliance. InAdjunct Proceedings of the 33rd ACM Conference on User Modeling, Adaptation and Personalization (UMAP Adjunct ’25).
Association for Computing Machinery, New York, NY, USA, 234–236. doi:10.1145/3708319.3733643
[53] Muhammad Raees and Konstantinos Papangelis. 2026. From Trust to Appropriate Reliance: Measurement Constructs in Human-AI Decision-Making.
arXiv:2604.23896 [cs.HC] https://arxiv.org/abs/2604.23896
[54] Beatrice Rammstedt and Oliver P. John. 2007. Measuring Personality in One Minute or Less: A 10-Item Short Version of the Big Five Inventory in
English and German.Journal of Research in Personality41, 1 (2007), 203–212. doi:10.1016/j.jrp.2006.02.001
[55] René Riedl. 2022. Is trust in artificial intelligence systems related to user personality? Review of empirical evidence and future research directions.
Electronic Markets32 (2022), 2021–2051. doi:10.1007/s12525-022-00594-4
[56] Francesco Salvi, Manoel Horta Ribeiro, Riccardo Gallotti, and Robert West. 2025. On the conversational persuasiveness of GPT-4.Nature Human
Behaviour9, 8 (2025), 1645–1653. doi:10.1038/s41562-025-02194-6
[57] Melanie Schwede, Nika Meyer, Niclas von Schnakenburg, and Maik Hammerschmidt. 2023. Can Chatbots Be Persuasive? How to Boost the
Effectiveness of Chatbot Recommendations for Increasing Purchase Intention. InProceedings of the 56th Hawaii International Conference on System
Sciences (HICSS-56). doi:10.24251/HICSS.2023.425
[58] Weiyan Shi, Xuewei Wang, Yoo Jung Oh, Jingwen Zhang, Saurav Sahay, and Zhou Yu. 2020. Effects of Persuasive Dialogues: Testing Bot Identities
and Inquiry Strategies. InProceedings of the 2020 CHI Conference on Human Factors in Computing Systems(Honolulu, HI, USA)(CHI ’20). Association
for Computing Machinery, New York, NY, USA, 1–13. doi:10.1145/3313831.3376843
[59] Michael Shumanov and Lester Johnson. 2021. Making Conversations with Chatbots More Personalized.Computers in Human Behavior117 (2021),
106627. doi:10.1016/j.chb.2020.106627
[60] Marita Skjuve, Petter Bae Brandtzaeg, and Asbjørn Følstad. 2024. Why do people use ChatGPT? Exploring user motivations for generative
conversational AI.First Monday29, 1 (2024). doi:10.5210/fm.v29i1.13541

18 Mert Yazan, Suzan Verberne, and Frederik Situmeang
[61] Takehiro Takayanagi, Kiyoshi Izumi, Javier Sanz-Cruzado, Richard McCreadie, and Iadh Ounis. 2025. Are Generative AI Agents Effective Personalized
Financial Advisors? InProceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval(Padua,
Italy)(SIGIR ’25). Association for Computing Machinery, New York, NY, USA, 286–295. doi:10.1145/3726302.3729897
[62] Jacob D. Teeny and Sandra C. Matz. 2024. We Need to Understand “When” Not “If” Generative AI Can Enhance Personalized Persuasion.Proceedings
of the National Academy of Sciences121, 43 (2024), e2418005121. doi:10.1073/pnas.2418005121
[63] Jacob D. Teeny, Joseph J. Siev, Pablo Briñol, and Richard E. Petty. 2021. A Review and Conceptual Framework for Understanding Personalized
Matching Effects in Persuasion.Journal of Consumer Psychology31, 2 (2021), 382–414. doi:10.1002/jcpy.1198
[64] Tanawat Teepapal. 2025. AI-driven personalization: Unraveling consumer perceptions in social media engagement.Computers in Human Behavior
165 (2025), 108549. doi:10.1016/j.chb.2024.108549
[65] Stephanie M. Tully, Chiara Longoni, and Gil Appel. 2025. Lower Artificial Intelligence Literacy Predicts Greater AI Receptivity.Journal of Marketing
89, 5 (2025), 1–20. doi:10.1177/00222429251314491
[66] Lu Wang, Max Song, Rezvaneh Rezapour, Bum Chul Kwon, and Jina Huh-Yoo. 2024. People’s Perceptions Toward Bias and Related Concepts in
Large Language Models: A Systematic Review. arXiv:2309.14504 [cs.HC] https://arxiv.org/abs/2309.14504
[67] Ruilin Xiao, Mert Yazan, and Frederik B. I. Situmeang. 2025. Rethinking Conversation Styles of Chatbots from the Customer Perspective:
Relationships between Conversation Styles of Chatbots, Chatbot Acceptance, and Perceived Tie Strength and Perceived Risk.International Journal
of Human–Computer Interaction41, 2 (2025), 1343–1363. doi:10.1080/10447318.2024.2314348
[68] Mingzhe Yang, Rina Kagawa, and Yukino Baba. 2026. Do User-Aligned Explanations Steer Human Decisions? Context-Dependent Influence and
Ethical Implications. InProceedings of the 2026 ACM Conference on Fairness, Accountability, and Transparency (FAccT ’26). Association for Computing
Machinery, New York, NY, USA. doi:10.1145/3805689.3812288
[69] Mert Yazan, Frederik Bungaran Ishak Situmeang, and Suzan Verberne. 2026. The Decision to Verify: How Warmth and User Characteristics Shape
Reliance on Conversational Agents for Information Search. arXiv:2605.28498 [cs.HC] https://arxiv.org/abs/2605.28498
[70] Ming Yin, Jennifer Wortman Vaughan, and Hanna Wallach. 2019. Understanding the Effect of Accuracy on Trust in Machine Learning Models. In
Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems (CHI ’19). Association for Computing Machinery, New York, NY,
USA, Article 279, 12 pages. doi:10.1145/3290605.3300509
[71] Yunfeng Zhang, Q. Vera Liao, and Rachel K. E. Bellamy. 2020. Effect of Confidence and Explanation on Accuracy and Trust Calibration in AI-Assisted
Decision Making. InProceedings of the 2020 Conference on Fairness, Accountability, and Transparency (FAT* ’20). Association for Computing
Machinery, New York, NY, USA. doi:10.1145/3351095.3372852

Personalized to Persuade 19
A Survey Items
Table A.1 lists the items of every measure in the analyses, in survey order. Only the two decision items were also asked
before the interaction.

20 Mert Yazan, Suzan Verberne, and Frederik Situmeang
Table A.1. Survey items and response scales.
Measure Items Response scale
Budget approval If the city council gave you the option to approve the
expert-recommended budget as is, would you approve?
Yes; No
Expert confidence How confident are you in the expert evaluation? Slider, 0 to 100
Contextualization check The assistant explained the topic based on my background. 7-point agreement
[31];𝛼=.95The assistant used my background to tailor its responses.
Warmth check The answers the assistant gave were warm. 7-point agreement
[67];𝛼=.94The answers the assistant gave were friendly.
The answers the assistant gave were kind.
The answers the assistant gave were enthusiastic.
Emotional trust I feel secure about relying on this assistant for my decision. 7-point agreement
[27];𝛼=.98 I feel comfortable about relying on this assistant for my decision.
I feel content about relying on this assistant for my decision.
Competent trust This assistant provides unbiased information about StormShield. 7-point agreement
[27];𝛼=.93This assistant is honest.
I consider this assistant to be of integrity.
AI literacy, adapted from
[18];𝛼=.87
How familiar are you with the following AI- and chatbot-related
items? Generative AI; Hallucination; LLM (Large Language
Model); Transformer; Token; RAG (Retrieval-Augmented
Generation); Prompt.
1 = None, 2 = Little,
3 = Some, 4 = Good,
5 = Fully
Usage frequency How often do you use AI chatbots (e.g., ChatGPT, Copilot,
Claude, Gemini)?
1 = Never, 2 = Tried a
couple of times, 3 =
Less than once a
month, 4 = Monthly,
5 = Weekly, 6 = 1–2
times a day, 7 = 3+
times a day.
Big Five, BFI-10 I see myself as someone who . . . is reserved. (E, R) 1 = Not well at all to
[54]; two-item . . . is generally trusting. (A) 5 = Extremely well
𝑟in Table B.2 . . . tends to be lazy. (C, R)
. . . is relaxed, handles stress well. (N, R)
. . . has few artistic interests. (O, R)
. . . is outgoing, sociable. (E)
. . . tends to find fault with others. (A, R)
. . . does a thorough job. (C)
. . . gets nervous easily. (N)
. . . has an active imagination. (O)
Note.After the interaction, the decision items were introduced with “After interacting with the assistant:” and “Please update your
confidence score based on your interaction:”. A No to the approval item is coded Approve = 1. 7-point agreement: Strongly disagree,
Disagree, Somewhat disagree, Neither agree nor disagree, Somewhat agree, Agree, Strongly agree.𝛼: Cronbach’s alpha. Scores are
item means. E = extraversion, A = agreeableness, C = conscientiousness, N = neuroticism, O = openness; R = reverse-scored.

Personalized to Persuade 21
B Descriptive Statistics and Condition Effects
This appendix describes the participants and the outcomes in each condition. Tables B.1 to B.3 describe the participants,
their Big Five traits, and the manipulation checks. Table B.4 and Figure B.1 reportConfDiff. Table B.5 reports the
approval decisions.
Table B.1 describes the participants in each condition. The conditions did not differ significantly in age (𝐹( 3, 403)=
1.81,𝑝=. 145), sex (𝜒 2(3)= 5.06,𝑝=. 168), AI literacy (𝐹( 3, 403)= 1.46,𝑝=. 225), or usage frequency (𝐹( 3, 403)= 0.85,
𝑝=. 468). Emotional trust (𝐹( 3, 403)= 0.21,𝑝=. 890) and competent trust (𝐹( 3, 403)= 1.10,𝑝=. 347) did not differ
significantly either.
Table B.1. Descriptive statistics by warmth and contextualization condition.
𝑊|𝐶 𝑁 Sex (M/F) Age Emotional Trust Competent Trust AI Literacy Usage Frequency
0|0 102 47.1% / 52.9% 43.47 4.60 5.09 2.15 5.04
0|1 103 54.4% / 45.6% 39.86 4.44 4.80 2.39 5.37
1|0 102 44.1% / 55.9% 40.41 4.56 4.87 2.29 5.19
1|1 100 39.0% / 61.0% 40.60 4.47 4.79 2.20 5.16
Total 407 46.2% / 53.8% 41.09 4.52 4.89 2.26 5.19
Note.W = warmth; C = contextualization. Values are means, except for sex. Trust is measured on a 7-point agreement scale and AI
literacy on a 5-point scale.
Table B.2 reports the Big Five traits by condition. Each trait score is the mean of two BFI-10 items, one of them
reverse-scored. The conditions did not differ significantly in any trait (all𝑝≥.150).
Table B.2. Big Five traits by warmth and contextualization condition.
𝑊|𝐶 𝑁 Extraversion Agreeableness Openness Conscientiousness Neuroticism
0|0 102 2.86 (1.11) 3.48 (0.90) 3.66 (0.87) 4.05 (0.78) 2.70 (1.01)
0|1 103 2.74 (1.04) 3.58 (0.82) 3.60 (0.89) 3.79 (0.91) 2.86 (1.06)
1|0 102 2.91 (1.07) 3.47 (0.98) 3.79 (0.88) 3.87 (0.83) 2.84 (1.07)
1|1 100 2.94 (1.10) 3.58 (0.85) 3.56 (0.92) 3.88 (0.74) 2.72 (1.13)
Total 407 2.86 (1.08) 3.53 (0.89) 3.65 (0.89) 3.90 (0.82) 2.78 (1.07)
Note.W = warmth; C = contextualization. Values are 𝑀 (𝑆𝐷 ) of the trait score, the mean of two items on a 1–5 scale. Missing item
responses (17 of 4,070) were replaced with the item mean.
Table B.3 reports the manipulation checks by condition. Participants in the warm conditions rated the answers as
warmer than participants in the neutral conditions (𝑀= 5.41vs.4 .49; Welch’s𝑡( 390.3)= 7.70,𝑝<. 001). Participants
in the contextualized conditions agreed more that the assistant used their background ( 𝑀= 5.63vs.3 .87; Welch’s
𝑡( 393.8)= 11.49,𝑝<. 001). In the neutral conditions, contextualization also raised perceived warmth (𝑡( 203)= 2.67,
𝑝=.008).
Table B.4 reportsConfDiffby condition. The adjusted means come from a linear model ofConfDiffon warmth,
contextualization, their interaction, and the covariates of the persuasion model (AI literacy, usage frequency, and the
Big Five traits), with the covariates at their sample means. Figure B.1 plots the adjusted means. Averaged over the other
factor, neither warmth (𝐹( 1, 396)= 0.62,𝑝=. 431) nor contextualization (𝐹( 1, 396)= 0.53,𝑝=. 466) changedConfDiff.

22 Mert Yazan, Suzan Verberne, and Frederik Situmeang
Table B.3. Manipulation check means by warmth and contextualization condition.
𝑊|𝐶 𝑁 Warmth Check Contextualization Check
0|0 102 4.24 (1.34) 3.89 (1.70)
0|1 103 4.73 (1.28) 5.52 (1.47)
1|0 102 5.37 (1.16) 3.86 (1.64)
1|1 100 5.46 (0.98) 5.74 (1.32)
Total 407 4.95 (1.29) 4.75 (1.77)
Note.W = warmth; C = contextualization. Values are𝑀(𝑆𝐷) on a 7-point agreement scale. Table A.1 lists the items.
Their interaction did (𝐹( 1, 396)= 6.04,𝑝=. 014, partial𝜂2 =. 015). Without the other cue, warmth loweredConfDiffby
7.7 points and contextualization by 7.6 points. With the other cue present, neither cue raisedConfDiffsignificantly.
The warm, contextualized condition did not differ significantly from the neutral, non-contextualized condition. The
contrasts led to the same conclusions without covariates and with heteroscedasticity-consistent (HC3) standard errors.
Table B.4.ConfDiffby warmth and contextualization condition: observed means, adjusted means, and contrasts.
A: Observed and adjusted means
𝑊|𝐶 𝑁 ConfPre ConfPost ConfDiff95% CI AdjustedConfDiff[95% CI]
0|0 102 66.46 (18.79) 54.99 (25.99) 11.47 (24.51) [6.66, 16.28] 11.75 [7.09, 16.40]
0|1 103 67.29 (16.49) 62.88 (23.40) 4.41 (23.52) [−0.19, 9.01] 4.16 [−0.47, 8.80]
1|0 102 66.55 (17.74) 62.56 (20.83) 3.99 (23.33) [−0.59, 8.57] 4.04 [−0.60, 8.68]
1|1 100 68.73 (19.41) 60.50 (22.59) 8.23 (23.73) [3.52, 12.94] 8.15 [3.47, 12.83]
Total 407 67.25 (18.09) 60.24 (23.41) 7.01 (23.89) [4.69, 9.34]–
B: Contrasts of the adjusted means
Contrast of adjusted means Difference [95% CI]𝑡(396)𝑝
Simple effects
Warmth without contextualization (1|0−0|0)−7.71[−14.29,−1.13]−2.30.022
Warmth with contextualization (1|1−0|1) 3.99 [−2.61, 10.58] 1.19 .235
Contextualization without warmth (0|1−0|0)−7.58[−14.20,−0.96]−2.25.025
Contextualization with warmth (1|1−1|0) 4.11 [−2.49, 10.71] 1.22 .222
A veraged over the other factor
Warmth−1.86[−6.50, 2.78]−0.79.431
Contextualization−1.74[−6.41, 2.94]−0.73.466
Other contrasts
Interaction (W×C) 11.69 [2.34, 21.05] 2.46 .014
Warm and contextualized vs. baseline (1|1−0|0)−3.60[−10.20, 3.00]−1.07.285
Note.W = warmth; C = contextualization. Conf Pre and ConfPost: confidence in the expert evaluation before and after the interaction
(0–100). Values in panel A are𝑀 (𝑆𝐷 ).ConfDiff= Conf Pre− ConfPost; higher values indicate a larger shift away from the expert
position. The 95% CI of the observed mean is𝑡-based. Adjusted means and contrasts come from a linear model ofConfDiffon warmth,
contextualization, their interaction, AI literacy, usage frequency, and the Big Five traits, with the standardized covariates at their
means.

Personalized to Persuade 23
Fig. B.1. Adjusted meanConfDiffby warmth and contextualization condition, with 95% confidence intervals.
Table B.5 gives the counts behind Figure 3. Initial approval ranged from 67% to 78% across conditions. These differences
were not significant (𝜒 2(3)= 3.37,𝑝=. 338). Participants made the initial decision before they met the assistant, so the
conditions could not affect it. Among participants who initially approved the budget, 54% to 60% switched to rejection,
with no difference between conditions (𝜒 2(3)= 0.56,𝑝=. 906). Table B.5 also reports the probability of rejection after
the interaction predicted by the reliance model, for each initial decision. The predicted probabilities differed by at most
.05 between conditions. No difference between conditions was significant (bootstrap𝑝≥.43).
Table B.5. Expert approval before and after the interaction by condition: counts, switch rates, and predicted probabilities.
Pre→Post (counts) Switch rate (%) Predicted𝑃(R after) [95% CI]
𝑊|𝐶 𝑁 A→A A→R R→A R→R A→R R→A A before R before
0|0 102 27 41 3 31 60.3 8.8 .59 [.48, .70] .92 [.85, .97]
0|1 103 33 39 2 29 54.2 6.5 .56 [.45, .67] .90 [.83, .96]
1|0 102 31 42 5 24 57.5 17.2 .54 [.43, .65] .90 [.82, .96]
1|1 100 34 44 1 21 56.4 4.5 .59 [.49, .69] .92 [.85, .97]
Total 407 125 166 11 105 57.0 9.5 – –
Note.W = warmth; C = contextualization. A: approval of the expert-recommended budget (pro-expert, Approve = 0). R: rejection
of the budget (anti-expert, Approve = 1). A→R: approval before and rejection after the interaction. Switch rates are percentages of
the participants with the same initial decision. Predicted 𝑃(R after): probability of rejection after the interaction predicted by the
reliance model (Table 3), for an initial approval (A before) or rejection (R before), averaged over the observed covariate values of all
407 participants. The prediction includes the paths through trust. Brackets: 95% percentile bootstrap CIs (2,000 resamples).

24 Mert Yazan, Suzan Verberne, and Frederik Situmeang
C Full SEM for Persuasion
Table C.1 reports every structural path of the persuasion model. We estimated the model with the continuous variables
standardized. We then rescaled each estimate and its standard error to the original units of the variables with their sample
standard deviations. The rescaling leaves𝑧 and𝑝 unchanged. A re-fit of the model on the original units reproduced the
rescaled estimates (largest difference: 0.002).

Personalized to Persuade 25
Table C.1. Full structural path estimates for the persuasion model.
𝛽 𝐵 𝑆𝐸 𝑧 𝑝
Emotional Trust
Warmth.009 0.0310.1550.20.844
Contextualization−.041−0.1320.155−0.85.395
AI Literacy−.087−0.1580.108−1.46.145
Extraversion−.001−0.0020.079−0.02.984
Agreeableness.121 0.2210.0992.24.025 ∗
Openness−.047−0.0860.091−0.95.341
Conscientiousness.209 0.4140.0994.17<.001 ∗∗∗
Neuroticism.008 0.0120.0790.16.875
Usage Frequency.247 0.2690.0654.15<.001 ∗∗∗
Competent Trust
Warmth−.025−0.0680.132−0.52.606
Contextualization−.074−0.1970.132−1.49.135
AI Literacy−.137−0.2060.099−2.09.036 ∗
Extraversion−.080−0.1000.074−1.34.179
Agreeableness.137 0.2070.0892.33.020 ∗
Openness.029 0.0440.0790.56.577
Conscientiousness.193 0.3150.0833.78<.001 ∗∗∗
Neuroticism.014 0.0180.0730.24.808
Usage Frequency.250 0.2250.0593.79<.001 ∗∗∗
ConfDiff
Warmth−.150−7.163.32−2.15.031 ∗
Contextualization−.148−7.063.32−2.13.033 ∗
W×C.203 11.254.712.39.017 ∗
Emotional Trust−.200−2.941.21−2.43.015 ∗
Competent Trust.196 3.481.602.17.030 ∗
AI Literacy.082 2.211.801.23.219
Extraversion.042 0.931.230.76.447
Agreeableness−.014−0.391.56−0.25.803
Openness−.030−0.811.56−0.52.602
Conscientiousness−.030−0.861.58−0.55.585
Neuroticism−.099−2.211.35−1.64.101
Usage Frequency.044 0.701.030.68.499
Note.𝛽: standardized estimate.𝐵: unstandardized estimate in the original units. Outcomes: emotional and competent trust in points of
the 7-point scale;ConfDiffin points of the 0–100 confidence scale. Predictors: warmth, contextualization, and W × C coded 0/1; trust
per point of the 7-point scale; AI literacy per point of the 5-point scale; usage frequency per step of the 7-point scale; Big Five traits
per point of the 1–5 trait score.∗𝑝<.05, ∗∗𝑝<.01, ∗∗∗𝑝<.001.
D Answer Length and Readability
We computed the length and readability of every assistant answer in the conversation logs and averaged them per
participant. We excluded the assistant’s fixed opening message and the verification word. Readability is the Flesch
reading ease score [12], where higher scores indicate easier text. Table D.1 reports the means by condition.

26 Mert Yazan, Suzan Verberne, and Frederik Situmeang
Contextualization lengthened the answers by 21 words, both with and without warmth (𝐹( 1, 403)= 822.7,𝑝<. 001).
Warmth did not change the length (𝐹( 1, 403)= 0.06,𝑝=. 80; interaction𝐹( 1, 403)= 0.02,𝑝=. 89). The extra words
came from the background sentence and from longer bullet points. The other parts of the answers had the same length
with and without contextualization. Both manipulations made the answers easier to read (warmth:𝐹( 1, 403)= 250.1;
contextualization:𝐹( 1, 403)= 942.8; interaction:𝐹( 1, 403)= 12.8; all𝑝<. 001). The difference also held within the
bullet points.
Table D.2 adds the standardized mean answer length and readability to the persuasion model as predictors ofConfDiff.
In this dummy-coded model, the warmth and contextualization estimates are the effects of each manipulation alone,
compared with the neutral, non-contextualized condition. The Warmth × Contextualization interaction remained
significant in every model. Neither length nor readability predictedConfDiff. The effect of contextualization alone
lost significance with either covariate. The effect of warmth alone lost significance with readability. Both covariates
changed with the manipulations, so these models cannot separate answer length and readability from contextualization
and warmth themselves. The estimates in Table 1 remain the effects of the manipulations as delivered. Within each
condition, neither length nor readability correlated withConfDiffor Approve Post (all|𝑟|≤.18,𝑝>.07).
Table D.1. Answer length and readability by warmth and contextualization condition.
𝑊|𝐶 𝑁 Words per answer Background words Reading ease Reading ease, bullets
0|0 102 97.5 (5.1) 0.0 26.4 (2.6) 17.6 (3.5)
0|1 103 118.5 (9.1) 10.3 39.6 (4.7) 30.1 (5.4)
1|0 102 97.6 (7.5) 0.0 33.9 (2.9) 21.2 (3.9)
1|1 100 118.8 (7.3) 10.3 44.3 (4.8) 32.7 (6.5)
Note.Values are participant means (SDs). Words per answer exclude the assistant’s fixed opening message and the verification word.
Reading ease: Flesch reading ease, where higher scores indicate easier text; each line and bullet point counts as one sentence, and
syllables were counted with the Pyphen hyphenation dictionary.
Table D.2. Persuasion model with answer length and readability as covariates ofConfDiff: standardized estimates (𝑝).
No covariates + Length + Readability + Both
Warmth−.150 ∗ (.031)−.150 ∗ (.031)−.096(.263)−.088(.309)
Contextualization−.148 ∗ (.033)−.096(.314)−.052(.618).033(.801)
Warmth×Contextualization.203 ∗ (.017).204 ∗ (.017).188 ∗ (.030).186 ∗ (.031)
Answer length –−.064(.382) –−.085(.253)
Readability – –−.115(.223)−.133(.165)
𝜒 2 (𝑑𝑓),𝑝43.07 (54), .86 48.02 (60), .87 48.43 (60), .86 54.40 (66), .85
Note.Same model as Table 1 and Table C.1, with the covariates added as predictors ofConfDiff(ML, 5,000 bootstrap resamples). Length
and readability are standardized participant means. CFI = 1.00, RMSEA = .000 and SRMR≤.011 in all models. ∗𝑝<.05.
E Full SEM Results for Reliance
Table E.1 reports every structural path of the reliance model. Its 𝐵 column was rescaled to the original units in the
same way as in Appendix C. For Approve Post,𝐵 is a probit coefficient. Table E.2 splits the effects of warmth and
contextualization into the indirect effects through each trust dimension, the direct effect, and the total effect.

Personalized to Persuade 27
Table E.1. Full structural path estimates for the reliance model.
𝛽 𝐵 𝑆𝐸 𝑧 𝑝
Emotional Trust
Warmth.009 0.0300.2200.14.891
Contextualization−.038−0.1250.227−0.55.580
ApprovePre .004 0.0160.1770.09.929
AI Literacy−.089−0.1620.102−1.60.110
Extraversion−.004−0.0070.076−0.09.932
Agreeableness.121 0.2220.0932.38.017 ∗
Openness−.046−0.0850.090−0.94.348
Conscientiousness.211 0.4190.1083.89<.001 ∗∗∗
Neuroticism.008 0.0120.0850.15.884
Usage Frequency.245 0.2680.0604.42<.001 ∗∗∗
Competent Trust
Warmth−.063−0.1740.200−0.87.387
Contextualization−.101−0.2780.204−1.36.173
ApprovePre −.061−0.1840.155−1.18.236
AI Literacy−.135−0.2070.084−2.48.013 ∗
Extraversion−.085−0.1080.062−1.75.079
Agreeableness.138 0.2130.0782.74.006 ∗∗
Openness.025 0.0390.0750.52.605
Conscientiousness.194 0.3240.0903.59<.001 ∗∗∗
Neuroticism.025 0.0320.0710.45.654
Usage Frequency.242 0.2220.0504.41<.001 ∗∗∗
ApprovePost
Warmth−.042−0.0970.189−0.51.607
Contextualization−.011−0.0250.196−0.13.900
W×C.081 0.2180.2810.77.438
ApprovePre .479 1.2360.2145.78<.001 ∗∗∗
Emotional Trust.114 0.0820.0701.17.243
Competent Trust.209 0.1780.0872.05.040 ∗
AI Literacy.176 0.2300.0872.64.008 ∗∗
Extraversion−.077−0.0830.068−1.22.224
Agreeableness−.142−0.1860.087−2.14.032 ∗
Openness.042 0.0550.0820.66.506
Conscientiousness.028 0.0400.0920.44.662
Neuroticism−.105−0.1150.072−1.58.113
Usage Frequency−.091−0.0710.054−1.32.188
Note.𝛽: standardized estimate.𝐵: unstandardized estimate in the original units. Outcomes: emotional and competent trust in points of
the 7-point scale; ApprovePost as a probit coefficient (1 = rejection). Predictors: warmth, contextualization, W× C, and ApprovePre
coded 0/1 (ApprovePre = 1: initial rejection); trust per point of the 7-point scale; AI literacy per point of the 5-point scale; usage
frequency per step of the 7-point scale; Big Five traits per point of the 1–5 trait score.∗𝑝<.05, ∗∗𝑝<.01, ∗∗∗𝑝<.001.

28 Mert Yazan, Suzan Verberne, and Frederik Situmeang
Table E.2. Direct, indirect, and total effects for the reliance model.
𝛽 𝑆𝐸95% CI𝑝
Warmth
Indirect via ET.001.008 [−.014,.016] .891
Indirect via CT−.013.017 [−.046,.020] .430
Total indirect−.012.023 [−.057,.033] .593
Direct−.042.081 [−.201,.117] .607
Total−.054.083 [−.217,.109] .516
Contextualization
Indirect via ET−.004.009 [−.022,.013] .628
Indirect via CT−.021.019 [−.059,.016] .269
Total indirect−.026.023 [−.070,.019] .263
Direct−.011.084 [−.175,.154] .900
Total−.036.086 [−.205,.132] .675
Note.Standardized effects. ET: emotional trust, CT: competent trust.
