---
title: AI-Moderated Interviews for Market Research and Digital Twins Calibration
url: https://arxiv.org/abs/2609.29143
category: digital-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Yuting Deng
- Jingxuan Liu
- Olivier Toubia
- Naman Jain
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.29143
pages: 60
chars: 166032
fetched_at: '2026-11-08T13:19:39+00:00'
kb_version: 1
---

# AI-Moderated Interviews for Market Research and Digital Twins Calibration

AI-Moderated Interviews for Market Research and
Digital Twins Calibration
Yuting Deng,1 Jingxuan Liu,1 Olivier Toubia,1 Naman Jain2
1Columbia Business School, Columbia University
2The Wharton School, University of Pennsylvania
{yd2721, jliu27, ot2107}@gsb.columbia.edu namanr999@gmail.com
Abstract.AI-moderated interviews are emerging as a scalable market-research method for generating consumer insights and
building consumer “digital twins.” Yet it remains unclear whether they match human-moderated interviews and whether they improve
on simpler, static data collection methods. In a pre-registered study with three industry partners, the authors randomly assign
participants to AI-moderated interviews (𝑁=139 ), static interviews (𝑁=154 ), or interviews conducted by professional human
moderators (𝑁=24 ). AI moderation matches human moderation in depth, covers more themes, and, at equal budget, recovers more
customer needs than either alternative, although participants sound more emotionally engaged with a human interviewer. The authors
thenbuildadigitaltwinofeachparticipantandevaluateitagainsttheparticipant’sownheld-outresponsestosixreal-worldmarketing
stimuli. Twins built from AI-moderated interviews predict consumer responses better than demographics-only personas, but no better
than twins built from static interviews: the richer conversation does not necessarily yield more accurate predictions. Comparing the
open-ended explanations provided by participants and their twins shows that prediction errors arise when twins reason differently
than the people they represent and when questions fall far outside what the interview covered. AI moderation thus pays off most for
discovering customer needs, and less for predicting customer responses.
Key words:AI-moderated interviews; qualitative market research; digital twins; large language models; voice of the customer
1. Introduction
Customerresearchiscentraltofirms’decisionsaboutproductpositioning,advertising,andcustomer
experience, but it faces a persistent tradeoff. Survey-based methods are fast, standardized, and
scalable, yet they often miss the “why” behind consumer choices (Anugraha et al. 2026, Korst et al.
2026). Human-moderated interviews can uncover richer narratives and more diagnostic insights, but
they are slow, costly, and difficult to scale. Recent advances in generative AI promise to relax this
tradeoff: AI-powered interviewers can conduct adaptive, open-ended conversations with consumers
at a much lower marginal cost, making it possible to bring qualitative insight earlier and more
frequentlyintomarketingdecisions(ChopraandHaaland2026,GeieckeandJaravel2026,Korstetal.
2026,Wuttkeetal.2025).Thispromisehasgeneratedsubstantialattentionandinvestment:AI-native
qualitativeresearchstartupssuchasOutset,ListenLabs,andSimilehaveraisedhundredsofmillions
1
arXiv:2609.29143v2  [cs.CY]  2 Nov 2026

2
of dollars in venture funding (Korst et al. 2026). Major LLM companies are also beginning to use
AI-moderated interviews at scale; for example, Anthropic has launched large-scale AI-moderated
interview programs (Anthropic 2025).
Despite growing interest and practitioner adoption, academic evidence on the performance of
AI-moderated interviews in market research remains limited. Two broad questions are especially
important. First, how do AI-moderated interviews perform as a market-research method relative to
established alternatives such as professional human-moderated interviews and static open-ended
interviews?Second,whatvaluedoestheresultingqualitativedataprovidefordownstreammarketing
applications such as consumer digital twins? We address these questions in collaboration with an
AI-moderatedinterviewplatform,aprofessionalmarketresearchfirm,andaB2Ccompany,allowing
us to evaluate AI moderation in a real-world market research setting. We first compare the interview
approaches on the quality of the data they generate and their efficiency in uncovering customer
needs. We then examine whether the resulting interview data from AI-moderated versus static
interviews improve digital twins’ ability to predict consumers’ responses to novel marketing stimuli.
Together, this work aims to clarify the role AI moderation can play relative to traditional approaches
inqualitativemarketresearchandwhethertheadditionalrichnessofadaptiveinterviewingtranslates
into greater downstream predictive value.
1.1. AI-Moderated Interviews for Market Research
AI-moderatedinterviewssitbetweentraditionalsurveysandhuman-moderatedqualitativeinterviews.
Compared with static surveys, qualitative interviews can adaptively ask clarifying and follow-up
questions based on what consumers say (Arsel 2017). Adaptive surveys such as adaptive conjoint
analysis also tailor questions to respondents, but they estimate pre-specified utility functions from
structured data (Johnson 1987, Toubia et al. 2003, 2004). Qualitative interviews instead require
moderators to interpret open-ended responses and decide what to ask next. However, human
moderators are costly and can charge $200–$400/hour (based on communications with GBK
Collective, one of our industry partners).
Compared with human interviews, AI-moderated interviews promise lower cost per interview
(approximately 20% of a human-moderated interview, based on market data from our partners),
greater scalability, and consistent implementation of a topic guide (Anugraha et al. 2026). However,
despite its promised benefits, AI moderation may introduce new threats to validity. For example,
it remains unclear to what extent respondents are comfortable talking to LLMs (De Freitas et al.
2026, Kim et al. 2022, Luo et al. 2019). LLM hallucinations may also cause AI moderators to ask

3
inappropriate follow-up questions or introduce fabricated content, potentially degrading data quality
and requiring validation and human oversight (Blanchard et al. 2025, Schroeder et al. 2025). In
addition, LLM-based moderators can add response latency to the conversation (Wuttke et al. 2025).
Recent evidence, coming mostly from fields adjacent to marketing, is nonetheless encouraging.
Across economic, political, and occupational settings, AI-led interviews receive high quality ratings
(Geiecke and Jaravel 2026, Anugraha et al. 2026), elicit richer responses than open-ended survey
questions (Geiecke and Jaravel 2026, Chopra and Haaland 2026), and uncover mental models and
themes that a fixed set of open-ended questions misses (Chopra and Haaland 2026). Comparisons
with human interviewers have also been favorable: sociologists rate voice-based AI interviews close
to face-to-face interviews by trained human interviewers (Geiecke and Jaravel 2026). A small study
(𝑁=11 interviews)findscomparableresponsequality,butparticipantsratedtheAIinterviewasless
interestingandlesssatisfying(Wuttkeetal.2025).Andinalargefieldexperimentonjobinterviews,
voice AI agents outperform professional recruiters on downstream hiring outcomes (Jabarian and
Henkel 2026). In marketing, Arora et al. (2025) show that LLMs can moderate in-depth interviews
with synthetic respondents and benchmark the resulting data against a human-moderated study of
real consumers.
Despitethisencouraginginitialevidence,atleasttwoquestionsremainontheuseofAI-moderated
interviews for market research. First, it is unclear how AI moderation compares with professional
human moderators when both interview real consumers about a real category and brand. Arora et al.
(2025), for example, compare AI-moderated interviews of synthetic personas to human-moderated
interviewsofhumanconsumers.WecomplementtheirworkbydeployinganAImoderatorwithreal
consumers, so that respondent type is held constant and only the moderator varies. Second, outside
of hiring (Jabarian and Henkel 2026), existing studies evaluate interviews mainly through process
measures, such as topic coverage, thematic richness, and participant ratings. For market researchers,
however, an interview is valuable to the extent that it efficiently yields decision-relevant insight,
such as customer needs (Griffin and Hauser 1993).
Accordingly, our first goal is to evaluate AI moderation as a market-research method by
benchmarking it against two alternatives. We compare AI-moderated interviews with interviews
conductedbyprofessionalhumanmoderators,toassesshowcloselyAIreproducesthesubstantiveand
experiential qualities of traditional qualitative research. We also compare AI-moderated interviews
with static interviews, which pose fixed open-ended questions with the same objectives on the same
platform and in the same audio modality, to isolate the value of adaptive probing. All conditions

4
cover topics typical of consumer research, including purchase journeys, brand perceptions, and prior
brand interactions. We compare the approaches on interview volume, thematic breadth and depth,
participants’ speech-based affect and prosody, and the customer needs uncovered, both per interview
and under a fixed research budget.
1.2. AI-Moderated Interviews as Training Data for Digital Twins
One of the major downstream use cases of AI-moderated interviews in marketing is the creation of
digital twins: LLM-based representations of specific individuals, built from their own data, such
as qualitative interviews or extensive survey responses (Park et al. 2026, Toubia et al. 2025). The
twin is then used to predict how that individual would respond to new questions not included in
these data. Digital twins have attracted substantial attention as a potential tool for consumer research
because they promise to let firms simulate consumer responses at greater scale and lower cost than
repeatedly collecting new data from human respondents. Companies such as Outset and Listen Labs
offer interview-grounded digital twins, while Aaru, Simile, and Expected Parrot similarly provide
AI-based simulations of human responses to surveys, products, pricing, marketing messages, and
hypothetical scenarios (Outset 2026, Listen Labs 2026, Aaru 2026, Simile 2026, Expected Parrot
2026).
However,whetherthesesimulationscanaccuratelypredicthumanresponsesremainsanimportant
empiricalquestion.Existingevidencesuggeststhataddingmoreperson-specificinformationdoesnot
necessarily translate to more accurate digital twin predictions. For example, across 19 pre-registered
studies, Peng et al. (2026) find that digital twins built on extensive survey data (combined with
demographics) are not more accurate than simpler personas trained on demographics data alone.
This raises the question of whether richer forms of consumer data can provide information that
structured survey responses and demographic information fail to capture.
Qualitative interview data may offer one such source of information to enrich digital twins. Park
et al. (2026) conduct two-hour AI-moderated interviews with more than 1,000 U.S. adults and
build an LLM agent for each participant from their transcript. These agents predict participants’
held-out responses to the General Social Survey, personality inventories, economic games, and
behavioral experiments more accurately than agents built from demographics alone, suggesting
that open-ended self-reports contain information beyond demographics that improves downstream
predictions. However, at least two aspects of Park et al.’s (2026) study call for additional research.
First, the interview protocol covers many of the same life domains as the validation measures, such
as political views, values, and family background. As a result, some of the predictive gain may

5
reflect leakage, whereby LLMs are evaluated on outcomes that are closely related to information
contained in their training data (Ludwig et al. 2026). Second, their interviews follow a long, largely
scripted protocol, and the study has no non-adaptive comparison condition. It therefore cannot
isolate whether adaptive probing itself contributes to predictive accuracy.
Morebroadly,priorresearchonindividual-leveldigitaltwinshaslargelyfocusedonsocial-science
domains, examining whether they can reproduce individual traits (Toubia et al. 2025), attitudes
(Park et al. 2026), and behavior on canonical experimental tasks (Peng et al. 2026). Little is known
about how digital twins perform in real-world marketing settings, where firms may seek to predict
consumers’ responses to novel marketplace stimuli such as advertisements and claims. In particular,
it remains unclear what kinds of qualitative consumer data are most useful for constructing digital
twins and whether richer, more adaptive interview data translate into more accurate predictions of
managerially relevant outcomes.
Hence, the second goal of this paper is to examine whether qualitative data collected through
AI-moderated interviews improve digital twins’ predictions of managerially relevant outcomes. We
construct twins from each participant’s own interview about the product category and brand, and
evaluate them against that participant’s held-out responses to new tasks: real-world advertisements,
mailers, and marketing claims provided by one of our three industry partners. Because the stimuli
were not discussed in the interviews, this design not only alleviates the leakage concern above, but
alsotestshowfarinterview-basedtwinscanextrapolate.WecomparetwinsbuiltfromAI-moderated
interviews, static interviews, and demographics alone, which allows us to test whether the richness
that AI moderation adds to interviews also translates into more accurate predictions. We further
compare open-ended explanations from participants and their twins to diagnose where predictions
fail.
1.3. The Current Research
We address our two goals in a pre-registered, between-subjects study of consumers (N=317) in the
windows-and-doorshome-improvementcategory(AsPredicted: https://aspredicted.org/
wb9sj2.pdf, https://aspredicted.org/3b3293.pdf). Participants were randomly
assigned to an AI-moderated or a static interview; a third group, recruited separately from the same
online pool, completed the same interview guide with professional human moderators.1 To ground
our investigation in real-world marketing practice, we collaborated with three industry partners. A
1Our initial pre-registration only included the AI-moderated and static conditions. The human-moderated condition was added later
based on peer feedback, and pre-registered separately.

6
major North American building-products company provided a relevant market research context
and real marketing stimuli. An AI startup specializing in AI-moderated interviews provided the
AI platform for conducting state-of-the-art AI-moderated interviews (the same platform was also
used for static interviews). GBK Collective, a marketing strategy and insights consultancy with
deep expertise in qualitative and quantitative research, served as our qualitative research partner
and conducted the human-moderated interviews. All conditions covered the same topics about the
product category and the partner brand. Because human-moderated interviews are substantially
more expensive and difficult to manage, we matched conditions on market cost (about $5,000 per
condition) rather than sample size.
We find that AI-moderated interviews elicit longer, broader, and deeper responses than static
interviews without reducing participant enjoyment or comfort. Compared with professional mod-
erators, AI moderation achieves comparable depth and broader thematic coverage, and under a
fixed budget it recovers the most customer needs. However, human-moderated interviews retain an
engagement advantage: participants sound more positive, activated, and assertive when speaking
live to a human vs. an AI moderator. We detect no differences between AI and static interviews in
the measured speech-based affect. Thus, AI moderation matches or exceeds human moderation on
interview content, but not on the emotional experience generated by live human interaction.
We then construct a digital twin for each participant in the AI-moderated and static conditions
and evaluate its predictions against that participant’s held-out responses to real-world marketing
stimuli: direct mailers (images), commercials (videos), and claim-ranking (text) tasks provided by
the building-products company.2 Twins built from interviews outperform demographics-only twins,
buttheadditionalrichnessofAI-moderatedinterviewsdoesnotyieldmoreaccuratepredictionsthan
static interviews. Because we collect open-ended explanations, we are able to trace prediction errors
to two sources, which are neither exhaustive nor mutually exclusive: limitedtraining data relevance,
the extent to which the information needed for the prediction task appears in the twin’s training data,
and limitedreasoning fidelity, the extent to which the twin’s reasoning replicates the (self-reported)
reasoning of the person it simulates. We find evidence for both. Consistent with reasoning fidelity
relevance, humans rely more on fast, intuitive (System 1; Kahneman 2011) reactions, whereas twins
reason more deliberately (System 2), especially for multimodal stimuli such as images and videos.
Consistent with training data relevance, adding to the training data the participant’s response to one
similar task improves rating predictions, suggesting a practical way to make twins more useful in
market research.
2As pre-registered, we did not construct digital twins in the human-moderated condition due to its much smaller sample size.

7
2. Methods
2.1. Design and Participants
This paper reports a between-subjects study (𝑁=317 ; 139 AI-moderated, 154 static, 24 human-
moderated). All participants were recruited from Prolific and screened to be home-improvement
decision-makers (homeowners, household income≥$75k, home value≥$250k, English-speaking).
These screening criteria were set in collaboration with the partner brand to ensure the sample’s
relevanceforanupscaleNorthAmericancompanyinthehome-improvementcategory.Allinterviews
covered the same topics and themes (See Table 1 for list of different sections).
We first collected theAI-moderatedandstaticconditions in the same recruitment batch. For these
two conditions, we used the commercial platform developed by our AI startup partner to run the
interviews. Participants who consented to participate in the study were randomly assigned to one
of the conditions and directed to the platform. They first completed screening questions to verify
eligibility (see “Design and participants”). Eligible participants then completed the interview based
on their assigned condition in one sitting.
In theAI-moderatedcondition,the interviews were conducted using the platform’s virtual
interviewer, a turn-based, goal-conditioned conversational system.After each participant turn,
browser-captured speech was sent to an AWS Lambda backend and transcribed using OpenAI’s
gpt-4o-transcribe; the transcription request was primed with the preceding interviewer utterance and
relevant study terminology. The transcript was appended to the conversation history and supplied to
GPT-5.1throughtheOpenAIChatCompletionsAPI,configuredwithtemperature0anda300-token
response limit. Conditioned on the interview guide and prior dialogue, the model generated either a
clarification or follow-up within the current section, or a transition to the next section. The virtual
interviewer’s response was converted to speech using the study-configured voice, OpenAI tts-1 with
the alloy voice.Although video could be recorded, the interviewer adapted solely to the transcribed
verbal content and conversation history; video, facial expressions, prosody, and other nonverbal
signals were not analyzed by the language model during the interview.
In thestaticcondition, participants used the same platform, but were shown fixed, pre-defined
questions with no adaptive follow-up or probing. In both conditions, participants recorded spoken
answers to each open-ended question.
We then recruited a separate sample for thehuman-moderatedcondition. These interviews were
conducted by GBK Collective (our market research partner), which provided trainedexperthuman
moderators to administer the same protocol. Participants were recruited from the same online pool,

8
but the study procedure differed slightly, due to the need to schedule live interviews. Participants
first completed a separate intake survey on Qualtrics with the same screening, demographic, and
individual-difference questions as the other conditions (Sections 0, 1, and 5 — see Table 1). Eligible
participants were then messaged through Prolific to sign up for a live interview time slot, during
which they completed the interview (Sections 2, 3, and 4 — see Table 1) with the human moderator.
We made an effort to keep survey time and compensation as similar as possible across conditions:
interviews in all three conditions lasted around 30 minutes. Compensation was $10 in the AI-
moderated and static conditions and $12 in the human-moderated condition, with the additional $2
compensating participants for completing the intake survey. The three conditions administered the
sameinterview and topic guide and differed only in how the interviews were moderated (please
refer to the “Interview Structure” subsection for details and examples).
Due to the high cost of human-moderated interviews, we were unable to match its sample size
to that of the other conditions. Instead, we matched conditions based on theirmarket cost. The
market cost of running 150 AI interviews is approximately $5k (for each participant: $10 participant
compensation for a 30-min interview + $3.33 Prolific platform fee + $20 AI-interview platform fee).
Given the market price charged by professional human interviewers (approximately $300 per hour,
or $150 for a 30-minute interview, plus participant compensation), $5k translates to approximately
30 human-moderated interviews of the same length (30 min), which we preregistered. However,
unexpectedly high no-show rates raised the marginal cost of that condition,3 yielding a final sample
of 24.
Following our pre-registered exclusion criteria, we excluded five AI-moderated and three static
participantswhodidnotprovidecompleteinterviewresponses,eitherbecausetheydidnotfinishthe
intervieworbecausetechnicalissuespreventedtheplatformfromproperlyrecordingtheirresponses.
We excluded one additional participant from the static condition who completed the interview but
didnotprovidemeaningfulanswerstotheopen-endedblocks( 58wordsin 10open-endedquestions).
Our final sample consists of𝑁=139 in the AI-moderated condition,𝑁=154 in the static condition,
and𝑁=24in the human-moderated condition.
2.2. Study Materials
Table 1 gives an overview of the various sections in our study. Sections 0 (screeners), 1 (Demo-
graphics), 4 (Marketing Stimuli), 5 (Individual differences) contained the same questions across the
3Participants were still paid an initial fee for completing the intake survey even if they later did not show up to their scheduled
interviews; the interviewers still spent several minutes per no-show. Significant time was spent scheduling human-moderated
interviews and following up with participants.

9
three conditions. Sections 2 (Category-specific) and 3 (Brand-specific) contained interview-style
questions that were implemented differently across conditions. Web Appendix A reports the full
study materials.
Table 1 Survey sections: content, response format, and use in twin calibration.
Section Content Response format Use in twin
calibration
0. Screeners Age, homeownership, home value, household
income, decision role, audio comfort, project
types and description
Multiple choice Training
1. Demographics Gender, ZIP code, education, employment,
household composition
Multiple choice Training
2. Category-specific Two open-ended blocks: Category usage,
context and feelings; Purchase journey.
Branches:(i)recentlyreplaced,(ii)considering.
Open-ended (differs by
condition)
Training
3. Brand-specific Two open-ended blocks: Brand awareness;
Brand perception and satisfaction.
Branches:(i) aware & past purchaser, (ii) aware
but not a past purchaser, (iii) not aware.
Open-ended (differs by
condition)
Training
4. Marketing stimuli Two mailers and two commercials (five 1–
5 rating items plus an open-ended response
each); two marketing-claim ranking sets (each
requires ranking three claims, then an open-
ended response)
Rating scales + free response Validation
(held out)
5. Individual
differences
Maximizing tendency, price consciousness,
minimalism, consumer need for uniqueness
Likert scales Training
6. Survey experience Enjoyment; comfort speaking and recording
(AI-moderated and static conditions only)
1–7 ratings —
Notes:Only Blocks 2 and 3 were open-ended and differed across interview conditions; all other blocks were administered identically. Block 4
(validation stimuli) was held out from twin construction and used only for evaluation. Block 6 was not collected in the human-moderated
condition.
Section 2 and 3 each contained two blocks of open-ended questions. Section 2 focused on
category-specific experiences, and Section 3 focused on brand-specific perceptions. Together, these
blocks covered four topics: category usage, context and feelings; purchase journey; brand awareness;
brand perception and satisfaction. For each of the four open-ended blocks, the static condition
showed participants a fixed question and asked them to record a single spoken answer with no
additional probing. The AI moderator was instead given an “objective” specifying the themes each
block should cover and instructed to use their judgment to probe adaptively. The human moderators
wereprovidedwithaninterviewguidethatcontainedboththefixedquestionandmoderatorobjective,
and were given discretion to ask questions and probe naturally while covering the specified content.
As Table 2 illustrates, we designed the moderator objectives to stay as close as possible to the
fixed questions, so that the conditions differed in moderation style rather than in the underlying

10
topics. Table W4 in Web Appendix B reproduces verbatim excerpts of an AI-moderated and a
human-moderated execution of this block.
Table 2 An example of an open-ended block (purchase journey for past purchasers): fixed question versus moderator
objective.
Fixed question in Static Condition Objective shared with Human/AI moderators
Please walk us through your replacement journey from the
momentyourealizedyouneedednewwindowsordoorstothe
moment you made your final choice. In your answer, please
cover:
•What triggered the need
•What research you did
•Who was involved
•What options you considered
•How you narrowed things down
Looking back, how do you feel about the decision? Share
what mattered most and whether you would do anything
differently.
Understand the respondent’s completed replacement journey
from initial need to final choice: what triggered the need;
what research they did, who was involved, what options
they considered, and how they narrowed them down; what
mattered most in the decision; and how they feel about the
outcome and whether they would do anything differently.
Notes:The three conditions shared the same question objectives but differed in how respondents were interviewed: In the static condition,
respondents were shown the fixed question and recorded a single spoken answer with no probing. In the AI condition, the moderator was given
that block’s objective and probed adaptively to address that objective. In the human condition, following industry best practices, the interviewer
worked from both the fixed question and the objective and used their discretion to ask questions and probe naturally while covering the specified
content. Each colored phrase marks a theme; the purchase journey block for past purchasers comprised eight themes (colors were not shown to
participants or moderators).
Section 4 presented six real-world marketing-stimulus tasks supplied by the partner brand:
two direct-mail images, two commercial videos, and two sets of three marketing claims. Due to
confidentiality concerns, we are not able to share the exact marketing stimuli tested in the survey.
Participants evaluated the same stimuli using fixed questions across conditions, without adaptive
probing.
For each mailer and commercial, participants rated five statements: “This [mailer/commercial]
grabs my attention,” “The main message of this [mailer/commercial] is clear,” “I like this [mailer/-
commercial]overall,”“This[mailer/commercial]makesmewanttolearnmoreabout[thepartnering
brand],” and “This [mailer/commercial] feels relevant to me and my needs” (1= strongly disagree,5
= strongly agree). Each stimulus was followed by an open-ended question: “What stood out to you
most about this [mail piece/commercial], and what (if anything) could be improved?”
The two mailers differed in visual style and content. The first featured a handwritten-style design
with highlighted discounts, while the second used a brochure-style layout with product photographs
and promotional offers. The two commercials each lasted approximately 30 seconds. The first
emphasized customer service through testimonials about the replacement experience, while the
second highlighted a limited-time financing offer alongside images of windows, doors, and home
interiors.

11
The two claim tasks asked participants to rank three benefit claims specific to the company’s
products by attractiveness (#1 = resonates the most, #3 = resonates the least) and three claims
about a particular window product by concern (#1 = most concerning, #3 = least concerning),
respectively. For each set, participants were instructed to explain why their top-ranked selection was
more attractive/concerning than the other claims.Web Appendix A (Section 4) reports the complete
wording.
Participants also completed individual-difference items (Section 5) adapted from established
measures: maximizing tendency (five items, adapted from Nenkov et al. 2008; e.g., “I never settle
for second best”), price consciousness (five items, adapted from Lichtenstein et al. 1993; e.g., “I
will grocery shop at more than one store to take advantage of low prices”), consumer minimalism
(12 items, adapted from Wilson and Bellezza 2022, e.g., “I avoid accumulating lots of stuff”), and
consumer need for uniqueness (12 items, adapted from Ruvio et al. 2008, e.g., “I actively seek to
developmypersonaluniquenessbybuyingspecialproductsorbrands”).Maximizingtendency,price
consciousness, and need for uniqueness used five-point agreement scales (1 = strongly disagree,5 =
strongly agree); minimalism used a seven-point agreement scale (1 = strongly disagree,7 = strongly
agree). Web Appendix A reports the complete lists of items.
At the end of the survey, participants in the AI-moderated and static conditions answered two
single-item experience questions (Section 6): “How enjoyable was it to complete this study?” (1
= not enjoyable at all,7= very enjoyable) and “How comfortable was it to speak and record your
answers?” (1= not comfortable at all,7= very comfortable). We analyzed the two ratings separately.
These questions were not administered in the human-moderated condition.
2.3. Interview Process and Data-Quality Measures
We characterized each interview along four families of measures, summarized in Table 3. The
volume, richness, affect, and prosody measures were computed oninterviewee-onlyspeech from the
fouropen-endedblocksinthecategoryandbrand-specificsections(Sections2and3).Wetranscribed
each interview with Whisper timestamps (Radford et al. 2023) and matched each Automatic Speech
Recognition (ASR) segment to the known-speaker transcript by token overlap. For participant-level
interview outcomes, we compare independent condition means using two-sided Welch’s𝑡-tests,
which allow unequal variances and sample sizes.
Interview volume.We first assessed how much speech each condition elicited and how interactive
the exchange was. For each participant, speaking time equals the total durations of participant-
attributed speech segments across the four open-ended blocks from Sections 2 and 3, reported in

12
Table 3 Interview-process and data-quality measures.
Measure Definition
Interview volume
Participant speaking time Total minutes of participant speech across the four open-ended blocks
Overall word count Total participant words across the four blocks
Participant turns Total number of participant-speaking turns
Richness and depth per open-ended block
Breadth Number of the block’s predefined themes the participant covers, coded by an
LLM against the per-block codebook (see full list of themes in Table W5 in
Web Appendix C)
Mean depth Average elaboration across present themes only (1 = mention only,4 = rich,
detailed elaboration). Absent themes receive0 at the coding stage and are
excludedfromthisaverage;ablockwithnopresentthemesreceives 0(examples
in Web Appendix C)
Speech-based affect
Valence How positive versus negative the participant sounds
Arousal How activated or energized the participant sounds
Dominance How assertive the participant sounds
Prosody
Voiced fraction Share of frames with detected pitch (Mauch and Dixon 2014)
Speaking rate Participantwordsdividedbyvoicedseconds,multipliedby60(wordspervoiced
minute)
Pause fraction Share of frames below 10% of the recording’s mean RMS energy
minutes. Word count is the number of whitespace-separated words in the corresponding participant
text, summed across the blocks. A participant turn is a distinct response to a fixed question or
moderator utterance; multiple transcription segments within that response count as one turn. We
excluded moderator speech, closed-ended items, and validation responses from these measures.
Richness and depth per open-ended block.Volume alone does not show whether an interview
is substantively rich. A strong qualitative interview should cover relevant topics and explore them
in depth. We therefore coded each open-ended block for breadth, the number of distinct themes a
participant mentions regardless of richness, and depth, how extensively each theme is discussed. To
this end, we decomposed each block’s moderator objective into a fixed set of codable themes. For
example, the purchase journey example in Table 2 contains eight themes (e.g., what triggered the
need to purchase).
We coded each participant’s responses to each block against this theme codebook using LLM
coding (gpt-4o) (Blanchard et al. 2025). For each participant, LLM coders rated each theme on
a 0–4 scale: 0 = the theme is not meaningfully present, 1 = mention only – present but only as a
brief mention or label, 2 = minimal elaboration – present with one layer of development, 3 = clear
elaboration – clearly developed with at least two kinds of substantive support, 4 = rich elaboration –
developed in a rich, multi-part way with several specifics and strong sense of reasoning, process, or
consequences. For example, within the Decision criteria theme, “Cost and quality would be the two

13
main things” received a rating of 1; “The price would be the most important, and quality, making
sure they’re going to last a long time, maybe energy savings, but that’s about it” received a rating of
3; and “the main thing that matters to us is the reputation of the company [...] Other top things I
look for in the actual doors and windows is the warranty [...] I want to make sure that I’m getting a
good quality product, even if I have to pay more for it. I want to make sure that it will withstand the
hurricane force winds and the rain and everything” received a rating of 4.
To improve coding reliability, we used five independent LLM coders. A theme was counted as
presentifatleastthreecodersrateditabove0.Foreachthemecountedaspresent,depthwasdefined
as the median score among coders who rated that theme above 0. For each block, we calculated
breadth as the number of themes present and mean depth as the average depth across themes that
werepresent(0ifnonewerepresent).Wereportresultsseparatelybyinterviewblockbecauseblocks
differ in their number of themes (from 3 to 9). Web Appendix C provides the full list of themes,
coding procedures, and worked examples.
Speech-based affect.How a participant sounds carries information about emotional engagement
that the transcript alone cannot capture. We scored each participant’s audio recording on valence,
arousal,anddominance,thestandarddimensionalrepresentationofemotion(MehrabianandRussell
1974,Mehrabian1996,Russell1980).Weusedawav2vec2speech-emotionmodelfine-tunedonthe
MSP-Podcast corpus (Lotfian and Busso 2019), applied it to 8-second audio windows, and averaged
the window-level scores into one interview-level score weighted by window duration (Wagner et al.
2023).
Prosody.We also examined acoustic delivery, which captures how fluently and continuously
participants speak. We extracted three interpretable prosodic features from the audio recordings:
voicedfraction,speakingrate,andpausefraction.Foreachparticipant,voicedfractionisthenumber
of frames with detected pitch divided by the total number of analyzed frames. Speaking rate is
60×𝑊/𝑉 , where𝑊 is the participant word count for the analyzed audio and𝑉 is the duration of
voiced frames in seconds. Pause fraction is the number of frames whose root-mean-square (RMS)
energyfallsbelow 10%ofthatrecording’smeanRMSenergy,dividedbythetotalnumberofframes.
These measures were computed with the standardlibrosatoolkit (McFee et al. 2015), using the
pYIN estimator to detect voiced frames (Mauch and Dixon 2014).
2.4. Customer Needs as Managerial Insight
Beyond how much participants say and how they sound, what practitioners ultimately value from
qualitative interviews is the set ofcustomer needsthey reveal (Berger et al. 2020). In scoping this

14
study with our industry collaborators, the central question was whether an AI moderator surfaces
the same needs as a skilled human interviewer, since these needs inform downstream product,
positioning, and messaging decisions. We therefore treat elicited customer needs as the unit of
managerial insight.
We define a customer need following Timoshenko et al. (2026) and building on the Voice of
the Customer tradition of Griffin and Hauser (1993): an underlying benefit the customer wants,
articulated at a decision-relevant level and grounded in the respondent’s own words, rather than a
product feature, solution, or opinion. This corresponds to the most granulartertiaryneed in Griffin
and Hauser (1993). We adopted the LLM-based VOC pipeline of Timoshenko et al. (2026), which
builds on machine-assisted need identification from consumer text (Timoshenko and Hauser 2019).
For each interview, we used the respondent’s answers to the four open-ended blocks and extracted
needs with onegpt-4o pass per interview (temperature=0, prompt in Web Appendix D).
We then winnowed overlapping mentions into a master codebook by embedding each mention
with all-MiniLM-L6-v2 (Reimers and Gurevych 2019, Wang et al. 2020) and clustering the
embeddings using cosine distance<.60. We treated each cluster as one unique need, with its modal
phrasing as the exemplar (De Paoli and Mathis 2025, Tamkin et al. 2024). This procedure yielded
252unique needs across all interviews. We then used the codebook to calculate the number of needs
that emerged in each condition and their corresponding frequency. A condition’s unique-need count
is the number of distinct master-codebook needs recovered at least once in that condition; repeated
mentions do not increase coverage. For a set of𝑛 interviews, coverage is the size of the union of
their recovered needs.
2.5. Twin Construction
For each participant, we constructed a digital twin by conditioning an LLM (gemini-3.1-
flash-lite-preview) on the participant’s persona through in-context learning: we provided
the participant’s training data as context and queried the model on the six marketing-stimulus
tasks (Table 1, Section 4). The stimuli and response options were supplied to the twin. We used
the Gemini family because the validation stimuli are multimodal: the mailers are images and
the commercials are videos, which Gemini models can process natively. We compared two twin
specifications:Demographics-only(Demo), which conditioned on demographics alone (Table 1,
Sections 0 and 1), andFull, which also included the interview transcript (Table 1, Sections 2, 3)
and individual-differences scales (Table 1, Section 5). The persona system prompt and the task
prompts are reported in Web Appendix E. To test robustness to model choice, we replicated twin

15
construction using identical prompts withgpt-5-mini, a model from a different family. Because
GPTdoes not support video inputs, the replication covered only the claims and mailer tasks. Results
are largely consistent (Web Appendix F).
2.6. Twin Evaluation and Metrics
We evaluated twin predictive validity on the marketing stimuli presented in Section 4 of the survey
(seeTable1).Eachparticipant’sownratings,claimrankings,andopen-endedexplanationsservedas
ground truth. Table 4 summarizes the response formats and corresponding performance metrics. We
describe the four types of dependent variables specified in the pre-registration: ratings accuracy (for
mailers and commercials), ratings Kendall’s𝜏𝑏 (for mailers and commercials), rankings Kendall’s𝜏
(for claim rankings), and open-ended responses cosine similarity (for all stimuli). All measures are
calculated separately for each interview condition and persona specification.
Mailers and commercials.Participants evaluated two direct mailers and two commercials, each
using five questions using 1–5 scales. We evaluated twin predictions using two measures. First, for
each rating question, we calculated the mean absolute error (MAE) between the twin-predicted
and human ratings across participants and transformed it into accuracy as1−MAE/4 (4 is the
maximum possible difference on a 1–5 scale). We then averaged accuracy across the five questions
for each stimulus. Accuracy ranges from 0, when human and twin ratings are at opposite ends of the
scale, to 1, when they are identical.
Second,foreachratingquestion,wecalculatedKendall’s 𝜏𝑏betweenhumanandtwinratingsacross
participants.Thismeasureswhethertwinspreservetheorderingofparticipants’responsestothatques-
tion independent of their absolute level. We calculated𝜏𝑏=(𝐶−𝐷)/
√︁
(𝐶+𝐷+𝑈 𝐻)(𝐶+𝐷+𝑈 𝑇),
where𝐶 and𝐷 count concordant and discordant pairs of participants, and𝑈𝐻 and𝑈𝑇 count pairs
tied only in the human or twin ratings, respectively. Values range from -1 (completely reversed
orderingofparticipants)to1(identicalorderingofparticipants);0indicatesnorelationshipbetween
the two orderings. Kendall’s𝜏𝑏 is undefined when either human or twin ratings are constant across
participants, resulting in a zero denominator. To ensure consistent comparisons across conditions
and bootstrap iterations (we drew 1,000 bootstrapped samples of the same size by resampling with
replacement in order to obtain confidence intervals), we excluded any rating item for which𝜏𝑏 was
undefined in the observed sample or in any of the bootstrap draws in any condition. This excluded
8 of the 20 rating items. This exclusion only applies to the𝜏𝑏 measure. For this reason, and for
parsimony, we report Kendall’s𝜏-b in the Web Appendix M.

16
Marketing claims.Participants completed two claim-ranking tasks, each requiring them to rank
three marketing claims. For each task, we compared each participant’s ranking with their twin’s
predicted ranking using Kendall’s𝜏=(𝐶−𝐷)/3 , where𝐶 and𝐷 count concordant and discordant
claim pairs. Identical rankings yield 1 and reversed rankings yield−1. For each participant, we
averaged the performance across the two ranking tasks.
Open-ended explanations.Participants provided an open-ended explanation for each of the six
stimuli. We embedded each human response and its corresponding twin response usinggemini-
embedding-2and calculated their cosine similarity, which ranges from−1to 1. Higher cosine
similarity indicates greater semantic similarity between the responses.
Pooled measures.Our primary dependent variables are three pooled measures derived from the
metrics above. For each participant, we averaged their stimulus-level accuracy across the four rated
stimuli (two mailers and two commercials) to obtain Accuracy𝑎𝑙𝑙 (ratings accuracy), the𝜏 scores
across the two ranking tasks to obtain𝜏𝑎𝑙𝑙 (ranking accuracy), and the six open-ended explanation
similarity scores to obtain Cosine𝑎𝑙𝑙 (open-ended similarity). Each stimulus receives equal weight
within its pooled measure.
Table 4 Validation stimuli, response formats, and performance metrics.
Stimulus (count) Response format Performance metric(s)
Images: direct mailers (×2)Five 1–5 scale items, plus one open-
ended explanation
Accuracy (1−|𝐻−𝑇|/4 ) and Kendall’s𝜏-b on
the scale items; cosine similarity on the open-
ended response
Videos: commercials (×2) Five 1–5 scale items, plus one open-
ended explanation
Accuracy (1−|𝐻−𝑇|/4 ) and Kendall’s𝜏-b on
the scale items; cosine similarity on the open-
ended response
Text:socialmediaclaim( ×2
sets)
Ranking of three claims, plus one
open-ended explanation
Kendall’s𝜏 on the ranking; cosine similarity on
the open-ended response
Notes:𝐻is the human response and𝑇the twin prediction.
2.7. Understanding Prediction Error: Training Data Relevance vs. Reasoning Fidelity
Twin prediction errors can arise from at least two conceptually distinct sources. First, the training
data may be too far removed from the prediction task, i.e., the twin was not given enough relevant
data to predict a particular response. Second, the (self-reported) reasoning from the digital twin may
be different from that of the human they are supposed to mimic, i.e., the human and the twin “think”
differently about the prediction task.
To measure training data relevance, we used an LLM judge (gpt-4o-mini, temperature0) to
code the extent to which the human’s explanation of their heldout choice can be traced to themes in

17
the interview. Specifically, the LLM judge received the participant’s interview transcript together
with that participant’s own open-ended explanation of their heldout response, and rated on a 0–4
scalehowmuchtheparticipant’sreasoningintheirexplanationofresponsetothevalidationquestion
can be traced back to specific statements made in the interview ( 0 = no reasoning point traces to
an interview statement; 4 = every reasoning point traces to an interview statement). Note that the
twin’s output played no role in this measure: the measure captured only whether the information the
human relied upon when evaluating the holdout stimulus was present in the training data.
To measure reasoning fidelity, we also instructed an LLM to assess the extent to which the twin
reasonssimilarlytothehuman,basedontheirexplanationsoftheirresponsetoeachheldoutquestion:
the same LLM judge (gpt-4o-mini, temperature0) compared the twin’s predicted explanation
with the human’s actual explanation for the same stimulus, rating on a 0–4 scale ( 0 = the twin
reasons entirely differently from the human; 4 = the twin reasons with the same logic/priorities as
the human). Web Appendix G reports the coding prompts and examples.
We note that training data relevance and reasoning fidelity are not orthogonal concepts. In
particular, gaps in self-reported reasoning may be in part the result of the training data not being
completely relevant to the task. Nevertheless, regressing the predictive validity of digital twins on
training data relevance and reasoning fidelity gives insight into promising areas of improvement for
digital twins.
2.8. Similar-Task Calibration Ladder
We also ask whether observing a person’s response to a similar task can reduce the data gap and
thus improve the twin’s prediction. Specifically, we tested whether adding the person’schoice
(rating/ranking)andopen-endedresponsefortheothermarketingstimulusofthesametypeimproves
prediction on the target stimulus (e.g., adding the responses to one commercial as training data to
predict the responses to the other commercial). Web Appendix H shows the prompt inserts.
3. Results: AI-Moderated Interviews as a Source of Consumer Insight
We first present results related to our first research question: how AI-moderated interviews compare
to static interviews and human-moderated interviews in collecting qualitative data and insights.
3.1. Interview Process and Data Quality
We first asked whether AI moderation produces interview data comparable in volume to a human
moderator,andhowitcompareswithastaticinterview.Usingtheinterview-processanddata-quality
measuresdescribedinthe“InterviewProcessandData-QualityMeasures”subsection,Table5reports

18
interview volume and participant experience across conditions. Relative to static, AI moderation
elicited substantially more participant speech: participants spoke nearly twice as long (8.1 vs. 4.3
minutes), produced more words (952 vs. 609), and took more turns (30.5 vs. 8.3;4 all 𝑝<.001 ).
Human moderation produced the highest speech volume, with significantly longer speaking time
and higher word count than AI moderation (11.3 vs. 8.1 minutes, 𝑝=.003 ; 1,404 vs. 952 words,
𝑝=.006 ). However, AI and human moderation generated a similar number of participant turns
(30.5 vs. 32.4,𝑝=.238 ), suggesting a comparable level of interaction. Finally, compared to static,
the additional interactions resulting from adaptive questioning in the AI condition did not diminish
participant experience: enjoyment and comfort were statistically similar between AI moderation and
static. Web Appendix I breaks down the word counts by open-ended block.
Table 5 Interview process and participant experience by condition.
Condition Speaking time (min.) Word count Speaking turns Enjoyment (1–7) Comfort (1–7)
AI-moderated (𝑁=139)8.1(5.2)952.3(632.8)30.5(4.4)5.65(1.29)6.37(1.04)
Static (𝑁=154)4.3(2.5)609.2(336.9)8.3(1.0)5.59(1.20)6.27(1.12)
Human-moderated (𝑁=24)11.3(4.4)1403.6(702.7)32.4(7.4)– –
𝑝[𝑑] (AI-mod. vs. Static)<.001[0.95]<.001[0.69]<.001[7.22].699[0.05].393[0.10]
𝑝[𝑑] (Human-mod. vs. AI-mod.).003[0.62].006[0.70].238[0.38] – –
Notes:Speaking time, word count, and speaking turns were calculated based on the open-ended questions from Sections 2-3. Enjoyment and
comfortareself-reportedscores(1=notenjoyable/comfortableatall;7=veryenjoyable/comfortable)andwerenotcollectedinthehuman-moderated
condition. Entries are participant-level means with sample SDs in parentheses.𝑝 values are from two-sided Welch independent-samples𝑡-tests
of the indicated condition means. Cohen’s𝑑 is the first named condition mean minus the second, divided by the sample-size-weighted pooled
within-condition SD. Comparison cells report𝑝followed by Cohen’s𝑑in brackets.
3.1.1. Interview breadth and depthTable 6 reports interview richness, reflected by breadth of
theme coverage (number of themes covered out of a set maximum, see the “Interview Process and
Data Quality” subsection) and mean depth of responses. Relative to static interviews, AI-moderated
interviews covered more themes in three of the four blocks: purchase journey (7.29 vs. 5.90,
𝑝<.001 ), brand awareness (3.32 vs. 1.73,𝑝<.001 ), and brand perception and satisfaction (5.88
vs. 5.52,𝑝<.001 ). AI moderation also produced greater mean depth in purchase journey (2.56 vs.
2.31,𝑝<.001 ) and brand perception and satisfaction (2.71 vs. 2.55,𝑝<.001 ). The short category
usage, context and feelings block, which was limited to three turns (other blocks did not have such
limit), was the exception, showing no difference in either breadth or depth.
Asarobustnesscheck,wecomparedbreadthandmeandepthofAI-moderatedandstaticinterviews
while controlling for length of each block. For breadth, we regressed the number of themes covered
4AsTable1shows,thestaticconditionbranchesbasedonparticipants’priorpurchaseexperienceandbrandawareness,sotheaverage
number of turns is not a whole number.

19
Table 6 Interview data quality by open-ended block.
Block Condition Word count Breadth Mean depth
Category usage, context and feelings
(max. breadth = 3)
AI-moderated99.7(69.5)2.94(.25)2.51(.43)
Static111.1(84.1)2.94(.24)2.53(.45)
Human-moderated412.0(246.3)2.92(.41)2.96(.45)
𝑝[𝑑] (AI-mod. vs. Static).21[−0.15].82[−0.03].74[−0.04]
𝑝[𝑑] (AI-mod. vs. Human-mod.)<.001[−2.76].83[0.07]<.001[−1.03]
Purchase journey
(max. breadth = 9)
AI-moderated413.6(305.0)7.29(.91)2.56(.28)
Static197.6(123.1)5.90(1.44)2.31(.31)
Human-moderated414.2(271.4)6.08(1.61)2.46(.28)
𝑝[𝑑] (AI-mod. vs. Static)<.001[0.95]<.001[1.14]<.001[0.85]
𝑝[𝑑] (AI-mod. vs. Human-mod.).99[0.00].001[1.16].116[0.36]
Brand awareness
(max. breadth = 4)
AI-moderated116.4(88.9)3.32(.80)2.25(.48)
Static80.9(56.7)1.73(.53)2.14(.65)
Human-moderated273.8(258.2)1.79(.88)1.99(.80)
𝑝[𝑑] (AI-mod. vs. Static)<.001[0.48]<.001[2.37].089[0.20]
𝑝[𝑑] (AI-mod. vs. Human-mod.).007[−1.23]<.001[1.88].131[0.49]
Brand perception and satisfaction
(max. breadth = 6)
AI-moderated322.6(225.2)5.88(.35)2.71(.33)
Static219.6(126.7)5.52(.69)2.55(.35)
Human-moderated303.6(193.4)5.12(1.51)2.38(.65)
𝑝[𝑑] (AI-mod. vs. Static)<.001[0.57]<.001[0.65]<.001[0.45]
𝑝[𝑑] (AI-mod. vs. Human-mod.).67[0.09].023[1.15].025[0.83]
Notes:Entries are participant-level means with sample SDs in parentheses.𝑝 rows report two-sided Welch independent-samples𝑡-tests of equal
condition means for the indicated comparisons. Cohen’s𝑑 is the first named condition mean minus the second, divided by the sample-size-weighted
pooled within-condition SD. Comparison cells report𝑝followed by Cohen’s𝑑in brackets.
on condition (AI vs. static) and total word count in that block. For mean depth, we regressed
average depth on condition and mean words per covered theme. After controlling for length, the
AI-moderated advantage persisted for breadth in three of the four blocks (purchase journey, brand
awareness, and brand perception and satisfaction), and for mean depth in two of the four blocks
(purchase journey and brand awareness; Table W15 in Web Appendix J). Thus, AI moderation did
not merely produce longer responses. Conditional on length, it elicited broader and, in some blocks,
deeper content than static interviews. A pairwise LLM-as-a-judge robustness check (1,000 matched
response pairs per open-ended block) showed the same pattern (Web Appendix K).
Compared with human-moderated interviews, AI-moderated interviews covered more themes
in three of the four blocks: purchase journey (7.29 vs. 6.08, 𝑝=.001 ), brand awareness (3.32
vs. 1.79, 𝑝<.001 ), and brand perception and satisfaction (5.88 vs. 5.12, 𝑝=.023 ). Mean depth
was statistically comparable in the purchase journey and brand awareness blocks, higher for AI
moderation in brand perception and satisfaction (2.71 vs. 2.38, 𝑝=.025 ), and higher for human
moderation in the short category usage, context and feelings block (2.96 vs. 2.51,𝑝<.001 ). Thus,
longer human interviews did not appear to translate into systematically broader or deeper theme
coverage.

20
3.1.2. Speech-based affect: do participants sound different when speaking to a human
vs. an AI?We next compared participant audio across the three interview conditions using the
speech-based affect and prosody measures described in the Methods section. As Table 7 shows, the
affect measures distinguished human moderation from the two automated conditions. Participants
who spoke to a human moderator sounded more positive, more emotionally activated, and more
assertive than participants who spoke to an AI moderator: valence (.528 vs..471), arousal (.517
vs..359), and dominance (.562 vs..449) were all higher in the human condition (𝑝𝑠<.001 ). By
contrast, AI and static interviews were statistically indistinguishable on all three affect dimensions.
Prosody showed a more nuanced pattern. Voiced fraction and speaking rate did not differ
significantly across conditions, but AI moderation produced more pausing than both human
moderation and static. This may reflect hesitation, additional thinking, or adjustment to the AI
interaction. Overall, AI moderation improved interview volume and coded richness relative to static,
but it did not reproduce the emotional engagement of speaking to a human moderator in real time.
Table 7 Participant speech-based affect and prosody by modality.
Condition Valence Arousal Dominance Voiced frac. Speaking rate Pause frac.
AI (𝑁=139).471(.055).359(.101).449(.080).634(.149)245.3(99.3).266(.091)
Static (𝑁=154).471(.056).354(.111).447(.089).623(.150)250.4(130.1).199(.073)
Human (𝑁=24).528(.046).517(.048).562(.034).610(.126)265.6(69.6).209(.073)
𝑝[𝑑] (AI-mod. vs. Static).948[−0.01].666[0.05].813[0.03].538[0.07].707[−0.04]<.001[0.82]
𝑝[𝑑] (Human-mod. vs. AI-mod.)<.001[1.08]<.001[1.65]<.001[1.50].404[−0.17].227[0.21].002[−0.64]
Notes:Valence, arousal, and dominance are in[0,1] . Speaking rate is words per voiced minute; voiced fraction and pause fraction are proportions
of analyzed frames. Entries are participant-level means with sample SDs in parentheses.𝑝 rows report two-sided Welch independent-samples𝑡-tests.
Cohen’s𝑑 is the first named condition mean minus the second, divided by the sample-size-weighted pooled within-condition SD. Comparison cells
report𝑝followed by Cohen’s𝑑in brackets.
3.2. Customer Needs Coverage
Beyond transcript richness, we asked whether the interview conditions recovered the same customer-
need space, and how efficiently they recovered those needs.
Weextractedandconsolidatedcustomerneedsasdescribedinthe“CustomerNeedsasManagerial
Insight” subsection, applying the same pipeline to the four open-ended blocks in all three conditions.
The resulting master codebook contained252unique needs. Table 8 lists the most common shared
needs and examples unique to each condition.
3.2.1. Coverage EfficiencyWe first compared the coverage of needs across conditions at
matchedsamplesizes.Weusedresamplingcomparisonsatmatchedinterviewcountsconsistentwith
common qualitative saturation benchmarks (Guest et al. 2006, 2020). We report95%bootstrapped
confidence intervals; the sampling scheme for each condition is specified in Web Appendix L.

21
Table 8 Most Common Shared and Unique Customer Needs Across Interview Conditions.
Customer need # mentions
Most Common Needs Shared Across All Conditions
Access to affordable window and door replacement options 59
Desire for a cost-effective solution for window replacement 43
Confidence in the quality of professional installation 41
Desire for more energy efficient windows and doors 41
Confident in the longevity and quality of windows and doors 40
Trust in the brand’s reputation and quality of products 40
Confident the new windows will lower my energy bills 39
Cost-efficient window and door replacements 37
Confidence in the quality and reputation of the brand 35
Assured of the cost-effectiveness of the window replacement 31
Most Frequently Mentioned Need Unique to AI-Moderated Interviews
Preference for quality and price balance 8
Most Frequently Mentioned Need Unique to Static Interviews
Availability of services in my location 4
Most Frequently Mentioned Need Unique to Human-Moderated Interviews
Confident in the ability to find reliable instructional resources for DIY projects 1
Notes:A full list is available to qualified academic researchers upon request for research purposes.
Figure 1 plots customer-need saturation curves, showing how many unique needs are recovered as
interviews are added. Lines show the median across random interview orderings, and shaded bands
show the 5th–95th percentile range.
Figure 1 Customer-need saturation curves by condition.
Over the first 24 interviews, AI moderation and human moderation recovered a similar number of
unique needs, while static accumulated needs more slowly. A resampling comparison at a matched
sample size of𝑁=24 showed the same descriptive pattern: AI moderation recovered111.5 unique
needsonaverage(95%resamplinginterval [98.0,125.0] ),closetohumanmoderation( 109.0,based
on the full sample of 24 human-moderated interviews) and well above static (75.9, 95% resampling
interval[65.0,87.0]; Web Appendix L, Table W17).

22
As an additional aggregate measure, Figure 2 illustrates how the252 unique needs overlap across
thethreeconditions: 93wererecoveredbyallthree, 52wereuniquetoAImoderation, 7tostatic,and
3to human moderation. Table 8 lists examples of the most common shared and condition-specific
needs.
Figure 2 Customer needs shared across and unique to each interview condition.
3.2.2. Need Elicitation CostBecausethethreeconditionswererununderacomparablemarket-
costbudget($5K),theirrealizedfullsamplesizesreflecttheirper-interviewcosts.Humanmoderation
producedmanyneedsperinterviewbutatroughlyfivetimesthecostofanAI-moderatedinterviews,
so the same budget covered fewer interviews. AI moderation and static had the same per-interview
cost, but AI moderation added more new needs per interview. As a result, AI moderation recovered
the most unique needs under a fixed budget:238, compared with188 for static and109 for human
moderation. Table 9 summarizes the realized coverage and cost efficiency. The implied cost per
unique need is $36 for human moderation, $19 for AI moderation, and $27 for static, suggesting that
AI moderation can be the most cost-efficient method for eliciting customer needs.
Table 9 Customer-need coverage and cost by condition.
Condition Interviews Unique needs Cost / interview Cost / need
AI-moderated139 238$33.33 $19
Static154 188$33.33 $27
Human-moderated24 109$163.33 $36
All combined317 252— —
Notes:Cost per need is (interviews×cost per interview)÷unique needs.

23
4. Results: AI-Moderated Interviews as Training Data for Digital Twins
We now address the second goal of this paper, which is to explore whether the qualitative data
collected through AI-moderated interviews can be leveraged to construct digital twins capable of
predicting consumer response to marketing stimuli.
4.1. Demo vs. Full; Static vs. AI-Moderated
We compared twins built from Demographics-only personas with twins built from Full personas
that included the interview transcript. Demographics-only is a strong baseline because prior work
finds that synthetic personas constructed from demographic information alone can already achieve
relatively high predictive accuracy (Peng et al. 2026).
We focus on three pooled measures: ratings accuracy for mailers and commercials, ranking
accuracy (Kendall’s𝜏) for claims, and open-ended similarity for all stimuli. Web Appendix M
reports across-participant ordinal agreement on scale-rating questions using Kendall’s𝜏-b. Given
the small sample size of the human-moderated condition and the high cost of collecting human-
moderated interviews at scale required for digital-twin training (i.e., this is not a managerially
relevant benchmark), we focus only on the AI-moderated and Static conditions in this section, as
pre-registered.
Table 10 shows that adding interview transcripts generally improved prediction quality. In the
Static condition, Full personas outperformed Demo personas on all three pooled measures. In the
AI-moderated condition, Full personas significantly improved open-ended similarity (𝑝<.001 ),
with a marginal gain in ratings accuracy (𝑝=.086 ) and a positive but non-significant gain in
claim-ranking accuracy (𝑝=.210 ). Thus, interviews contain predictive signal beyond demographics
alone.
However, we found no evidence that AI-moderated interviews produced more predictive twins
than Static interviews on ratings accuracy or claim-ranking accuracy. Surprisingly, Static actually
yielded slightly higher open-ended similarity under both Demo (.734 vs..723,𝑝=.003 ) and Full
(.758 vs..744,𝑝=.001 ). None of the condition-by-persona interactions is statistically significant
(all𝑝≥.1 ),suggestingnocleardifferenceintheincrementalpredictivevalueofinterviewtranscripts
across conditions. Taken together, these results suggest that interview data can improve digital-
twin predictions, but the greater richness of AI-moderated interviews does not translate into a
demonstrated predictive advantage over Static interviews.

24
Table 10 Prediction performance by persona type and interview condition.
Ratings accuracy
Mailers and
commercials
Ranking
accuracy (𝜏)
Claims
Open-ended
similarity
All stimuli
Cell means
Static Demo.726.260.734 Full.742.344.758
AI-moderated Demo.731.314.723 Full.743.345.744
Full vs. Demo, within condition (𝑝[𝑑𝑧])
Static Full vs. Demo.013[0.203]<.001[0.285]<.001[1.497]
AI-moderated Full vs. Demo.086[0.147].210[0.107]<.001[1.301]
AI-moderated vs. Static, within persona (𝑝[𝑑])
AI-moderated vs. Static Demo.546[0.071].290[0.124].003[−0.359]
AI-moderated vs. Static Full.888[0.016].981[0.003].001[−0.395]
Condition×persona
interaction (𝑝[𝑑]).687[−0.047].123[−0.181].120[−0.184]
Notes:Comparisonsreporttwo-sided 𝑝values.Full–Democomparisonsusepaired 𝑡-tests;AI-moderated–
Static comparisons use Welch’s𝑡-tests. The interaction is a Welch test comparing participants’ Full–Demo
differences between conditions. Cohen’s𝑑 uses the sample-size-weighted pooled within-group SD; paired
𝑑𝑧 uses the SD of within-participant differences. Signs follow the displayed subtraction; interaction𝑑
compares Full–Demo gains using their pooled within-group SD. Comparison cells report𝑝 followed by the
effect size in brackets:𝑑𝑧 for Full–Demo comparisons and𝑑 for between-condition comparisons and the
interaction.
4.2. Understanding Prediction Error: Training Data Relevance vs. Reasoning Fidelity
To better understand the prediction errors of digital twins, following the framework of the section
“Understanding Prediction Error: Training Data Relevance vs. Reasoning Fidelity,” we regressed
twins’ ratings accuracy, ranking accuracy, and open-ended similarity on training data relevance (an
LLM-coded 0–4 rating of the extent to which the human’s open-ended explanation of their holdout
response can be traced back to the interview) and reasoning fidelity (an LLM-coded 0–4 rating of
how closely the twin’s reasoning expressed in their open-ended explanation of the holdout response
matches the human’s). We included stimulus fixed effects and cluster standard errors by participant
to account for dependence across repeated stimulus responses from the same participant.
AsTable11shows,trainingdatarelevancepositivelypredictedallthreeoutcomes:ratingsaccuracy
(b= 0.029,𝑝=.005 ),rankingaccuracy(b= 0.117,𝑝=.025 ),andopen-endedsimilarity(b= 0.034,
𝑝<.001 ). Reasoning fidelity served as a positive and significant predictor of ratings accuracy (b
= 0.085, 𝑝<.001 ) and ranking accuracy (b=0.338, 𝑝<.001 ), but did not significantly predict
open-ended similarity (b=0.006, 𝑝=.210 ). The latter finding is somewhat unexpected, as both
reasoning fidelity (LLM-coded) and open-ended similarity (embedding-based) assess agreement
betweenhumanandtwinexplanations,albeitusingdifferenttheoreticalconstructsandmeasurement
approaches.Thispatternsuggeststhatpredictionerrorisnotonlyaboutwhetherrelevantinformation

25
is present in the interview. Even when such information is available, twins’ quantitative predictions
are more accurate when their open-ended reasoning about the stimulus resembles the human’s
reasoning.Thissuggeststhatwhilesomegainsinpredictivevaliditymaybeexpectedfromproviding
training data that is more relevant to the task the twin is asked to simulate, future research may also
focus on aligning the reasoning process of twins with that of humans.
Table 11 Predictive performance regressed on training
data relevance and reasoning fidelity (Full personas,
AI-moderated condition).
Ratings
accuracy
Ranking
accuracy (𝜏)
Open-ended
similarity
Training data relevance.029 ∗∗ .117∗ .034∗∗∗
(.010) (.052) (.004)
Reasoning fidelity.085 ∗∗∗ .338∗∗∗ .006
(.017) (.061) (.004)
Stimulus FE Yes Yes Yes
SE clustered by participant Yes Yes Yes
𝑅2 .19.20.35
Observations555 276 831
Notes:Each observation is a participant–stimulus response. The
dependent variables are ratings accuracy (the mean of1−|𝐻−𝑇|/4
across five questions) for mailers and commercials, ranking accuracy
(Kendall’s𝜏) for claim sets, and open-ended cosine similarity for all six
stimuli.ModelsareOLSwithstimulusfixedeffects;participant-clustered
standard errors are in parentheses. Significance symbols use two-sided
asymptotic Wald𝑧-tests of coefficients against zero.†𝑝<.10 ,∗𝑝<.05 ,
∗∗𝑝<.01, ∗∗∗𝑝<.001
We next explored some factors that may affect reasoning fidelity. Prior work suggests that digital
twins can be overly analytical, or “hyper-rational” (Goli and Singh 2024, Mei et al. 2024, Peng
et al. 2026). This matters for marketing stimuli, especially images and videos, where humans often
respond quickly and affectively while twins may give more deliberate explanations. To measure
this, we used an LLM judge (gpt-4o-mini, temperature0) to code each open response, in the
spirit of verbal protocol analysis (Ericsson and Simon 1980, 1993, Nisbett and Wilson 1977), on a
scale from0= intuitive/experiential (System 1) to4= analytical/deliberative (System 2) (Kahneman
2011). Each response was scored in a separate judge call, with no indication of whether the text
came from the human or the twin; the coding prompt is in Web Appendix G. Thereasoning-style
gapfor a response pair is the absolute difference|Twin−Human|on this scale.
Table 12 shows that twins were substantially more analytical than humans for Mailers (2.18 vs.
1.31,𝑝<.001 ) and Commercials (2.23 vs. 1.60,𝑝<.001 ). For Claims, the difference was much
smaller, though still statistically significant (2.75 vs. 2.50, 𝑝<.001 ). A separate response-focus
coding reported in Web Appendix N suggests humans were more likely to react to what they directly

26
see or hear in the stimulus, whereas twins were more likely to draw on person-level context from the
interview.
Reasoning fidelity and reasoning-style gap are two measures of the difference between the twin’s
and the human’s open-ended reasoning about the same stimulus, yet empirically they were only
weakly correlated (𝑟=−.23 ,−.15, and−.25 for Claims, Mailers, and Commercials). The tendency
of twins to reason more analytically than humans therefore accounts for only part of the divergence
between twin and human reasoning, suggesting that other differences between the two remain to be
identifiedandaddressed.Becausebotharemeasuresofthetwin–humanreasoningdifference,wedid
not enter them jointly in our regressions. Web Appendix O reports separate task-family regressions
with the reasoning-style gap in place of reasoning fidelity: the gap significantly predicted lower
accuracy for Claims, with small and nonsignificant coefficients for Mailers and Commercials. This
further confirms that the twins’ tendency to reason more analytically only accounts for a modest
portion of the divergence between twins and humans.
Table 12 Open-response style on a0–4scale (0=
intuitive/System 1,4=analytical/System 2).
Task𝑛Human TwinΔ𝑝[𝑑 𝑧]
Claims139 2.50 2.74+.25<.001[0.387]
Mailers139 1.31 2.18+.87<.001[1.575]
Commercials139 1.60 2.23+.63<.001[1.108]
Notes:AI-moderatedparticipantsonly.HumanandFull-personatwin
scoreswereaveragedacrossmatchedstimuliwithineachtaskfamilyfor
eachparticipant.ResponseswereindependentlyscoredbyanLLMjudge
blinded to their source. Entries are participant-level means;Δis Twin
− Human.𝑝 values are from two-sided paired𝑡-tests. Paired Cohen’s
𝑑𝑧 is the mean participant-level Twin–Human difference divided by the
SD of those differences. The𝑝 column reports𝑝 followed by𝑑𝑧 in
brackets.
4.3. Can Adding a Task Similar to the Holdout Task to the Training Data Improve
Predictions?
Having established that both training data relevance and reasoning fidelity relate to prediction
accuracy, we next asked whether adding a task to the training data that is similar to the validation
(holdout) task can improve predictions. Adding a task similar to the validation task should increase
the relevance of the training data, which may also improve the fidelity of the twin’s reasoning
process. Our design includes two commercials, two mailers, and two claim-ranking tasks. For each
task family, we can give the twin the participant’s response to one stimulus (both the choice/rating
and the open-ended reasoning) and ask it to predict the other. Because this signal comes from the
same task family, it may help calibrate the twin to how that person responds to similar marketing

27
stimuli. The participant’s choice may reveal their general response tendency within the task, while
theiropen-endedreasoningmayrevealwhichstimulusfeaturestheyattendtoandhowthosefeatures
shape their evaluation.
We report three main training data sets on the Full persona:Full(base),Full+ 1Val, which
adds the participant’s choice and open-ended reasoning for the other stimulus in the same task
family, and a2Valbenchmark. The 2Val benchmark further includes in the twin’s training data the
participant’sreasoningfortheholdoutstimulus.Itisthereforeasame-taskbenchmark,notagenuine
out-of-sample prediction condition.
Table 13 reports the three training sets among AI-moderated participants, with95%percentile
intervalsforperformanceandpairedparticipant-bootstraptestsforadjacentsteps.Addingonesimilar
task(1Val)totheFullpersonaimprovedratingaccuracyfrom .743to.787andopen-endedsimilarity
from.744to.788(both𝑝=.001 ),whileclaim-rankingagreementchangednon-significantly( .348to
.370,𝑝=.150 ).Onepossibleexplanationisthatanobservedresponsehelpscalibratehowpositively
or negatively a participant evaluates stimuli, which may transfer across similar tasks. Rankings, by
contrast, depend on tradeoffs among stimulus features that are harder to infer from a single response.
Further providing the participant’s open-ended reasoning for the target stimulus (2Val) improved
prediction performance, as expected (Table 13). Ratings accuracy for mailers and commercials
increased modestly from.787 to.815, whereas claim-ranking accuracy increased substantially from
.370 to.611 (both𝑝=.001 ). Nevertheless, performance remained imperfect even with access to the
participant’s ground-truth explanation. This suggests that individual responses to marketing stimuli,
especially for multimodal stimuli, are difficult to recover even with highly relevant training data is
provided.
Table 13 Prediction performance by training data condition.
Ratings accuracy Ranking accuracy (𝜏) Open-ended similarity
Training data Estimate [95% CI]𝑝Estimate [95% CI]𝑝Estimate [95% CI]𝑝
Full.743[.728,.756]—.348[.280,.415]—.744[.738,.750]—
Full+1Val.787[.773,.800].001.370[.304,.436].150.788[.781,.795].001
2Val (same-task benchmark).815[.803,.825].001.611[.546,.670].001— —
Notes:AI-moderated participants (𝑛=139 ). Brackets are 95% participant-bootstrap percentile intervals for performance estimates.𝑝 values
compare each row with the preceding row using two-sided centered bootstrap tests with 1,000 participant draws. Open-ended similarity is not reported
for 2Val because the human ground truth open-ended thoughts are already provided in the prompt.
5. Discussion & Conclusion
Firms are rapidly adopting AI-moderated interviews, both to discover what consumers need and to
build digital twins that predict how consumers will respond to various stimuli. We set out to answer
two open questions about these uses.

28
The first question was how AI moderation compares with professional human moderators when
both interview real consumers about a real category and brand. Prior evaluations have relied mainly
on expert and participant ratings and thematic richness, on comparisons with non-adaptive surveys,
or on settings outside consumer research (Chopra and Haaland 2026, Geiecke and Jaravel 2026,
Jabarian and Henkel 2026, Wuttke et al. 2025). Holding respondent type, category, and interview
guideconstant,wefindthatAI moderationmatchesorexceedsprofessionalmoderators oninterview
content and, at equal budget, recovers the most customer needs. Human moderators retain one
advantage: participants sound more positive, activated, and assertive when speaking with a live
person. Together, these results suggest that AI moderation can take on much of the interviewing
done for need discovery, while human moderation keeps its value where rapport and emotional
engagement are central.
The second question was whether the richness that AI moderation adds to interviews makes
digital twins more accurate. Twins built from interviews predict individual consumers’ responses to
realmarketingstimulibetterthandemographics-onlytwins,unliketwinsbuiltfromextensivesurvey
data in other domains (Peng et al. 2026). But adaptive probing does not help: twins built from static
interviews are as accurate as twins built from AI-moderated interviews. Our static condition thus
providesthenon-adaptivecomparisonthatearlierworklacked(Parketal.2026),anditsuggeststhat
the gains from interview data come from what consumers are asked about, not from how adaptively
they are asked. The value of AI moderation therefore depends on the research objective: richer
interviews generate more insight, but not better predictions.
Why did richer interviews not produce better twins? Our analysis of open-ended explanations
point to two sources of error. The first is limitedtraining data relevance. Because our stimuli were
not discussed in the interviews, our design limits the leakage that may inflate twin accuracy in
prior work (Park et al. 2026, Ludwig et al. 2026), but it also reveals the cost of avoiding leakage:
consumers’ reactions to a specific mailer or commercial often draw on considerations that never
come up in an interview about the category and brand, however well it is moderated. The second
is limitedreasoning fidelity. Even when relevant information is available, twins use it differently
than people do. Predictions were more accurate when the twin’s reasoning resembled the person’s
own, and twins reasoned more deliberately (System 2) than humans, who reported reacting more
intuitively (System 1), especially to images and videos. One possible account of both findings is
that interviews, however adaptive, elicit reflective accounts of past decisions (Nisbett and Wilson
1977). Better probing yields more of this reflective information, which helps researchers identify

29
needs, but it may provide little signal about the intuitive reactions that drive responses to marketing
stimuli, and it may reinforce twins’ tendency toward deliberative reasoning. Testing this account, for
example by building twins from immediate reactions to related stimuli, is a promising direction for
future research.
Our results further highlight the difficulty of predicting individual consumer behavior. Even when
twins were given participants’ own explanations for their responses to the target stimuli, their ratings
and rankings remained imperfectly recovered, particularly for ratings of mailers and commercials.
These findings suggest that firms should set realistic expectations for digital twins. Rather than
expecting near-perfect individual-level predictions, firms should evaluate their accuracy for specific
tasks and recognize that even highly relevant training data may not fully capture how consumers
respond to marketing stimuli.
Our findings should be interpreted in light of several limitations. First, given budget constraints,
we focus on a single, relatively high-involvement category. Window and door replacement is a major
purchase that typically involves substantial research and deliberation. AI moderation may perform
differently for low-involvement, symbolic, affect-laden, or sensitive topics. Prior research, for
example, suggests that consumers may disclose more sensitive information to AI when reduced fear
of social judgment is beneficial, but may disclose more readily to humans when they seek empathy
or emotional support (Kim et al. 2022). Future research should compare domains systematically to
identify when AI moderation is most effective and when human rapport remains essential.
Second, the study evaluates a particular AI-moderated platform and set of language models at
one point in time. Because model behavior and capabilities can change across versions, future work
should replicate these comparisons as the underlying technology evolves (Chen et al. 2024).
Third, future research could also test whether an embodied avatar helps reduce the engagement
gap between AI and human moderators. Facial expressions and responsive nonverbal cues may
strengthen social presence and rapport. Comparing AI interviews with and without an avatar, while
holding the voice and probing strategy constant, would help assess whether these features improve
engagement and how they affect candid disclosure.
Fourth, future research may collect multimodal and affect-rich signals, such as voice tone, facial
expression, attention, hesitation, and immediate reactions to related stimuli. These signals may
help twins better capture consumers’ intuitive, System 1 responses. The same result that limits AI
moderation as an emotional substitute for human moderation may also point to what current digital

30
twins are missing: not more text alone, but better information about how consumers feel and react in
the moment.
More broadly, our findings help advance research on the use of AI-moderated interviews in
consumerresearch.TheydemonstratethepotentialofAImoderationtogeneraterichqualitativedata
at scale, while also showing that richer interviews do not necessarily translate into more predictive
digital twins. As both AI moderation and digital-twin technologies continue to develop and gain
commercial traction, we hope this work provides a basis for understanding when AI can augment
traditional consumer research methods and what additional information is needed to build more
faithful representations of individual consumers.

31
References
Aaru (2026) Simulation.URLhttps://aaru.com/simulation, company webpage;accessed October 14,2026.
Anthropic (2025) Introducing anthropic interviewer: What 1,250 professionals told us about working with ai. URL
https://www.anthropic.com/research/anthropic-interviewer, anthropic Research.
Anugraha D, Padmakumar V, Yang D (2026) Sparkme: Adaptive semi-structured interviewing for qualitative insight
discovery.arXiv preprint arXiv:2602.21136URLhttps://arxiv.org/abs/2602.21136.
Arora N, Chakraborty I, Nishimura Y (2025) Ai–human hybrids for marketing research: Leveraging large language
models (llms) as collaborators.Journal of Marketing89(2):43–70, URLhttp://dx.doi.org/10.1177/
00222429241276529.
Arsel Z (2017) Asking questions with reflexive focus: A tutorial on designing and conducting interviews.Journal of
Consumer Research44(4):939–948, URLhttp://dx.doi.org/10.1093/jcr/ucx096.
BergerJ,HumphreysA,LudwigS,MoeWW,NetzerO,SchweidelDA(2020)Unitingthetribes:Usingtextformarketing
insight.Journal of Marketing84(1):1–25, URLhttp://dx.doi.org/10.1177/0022242919873106.
Blanchard SJ, Duani N, Garvey AM, Netzer O, Oh TT (2025) New tools, new rules: A practical guide to effective and
responsible generative ai use for surveys and experiments in research.Journal of Marketing89(6):119–139, URL
http://dx.doi.org/10.1177/00222429251349882.
Chen L, Zaharia M, Zou J (2024) How is ChatGPT’s behavior changing over time?Harvard Data Science Review6(2),
URLhttp://dx.doi.org/10.1162/99608f92.5317da47.
ChopraF,HaalandI(2026)ConductingqualitativeinterviewswithAI,workingpaper.CESifoWorkingPaperNo.10666;
SSRN No. 4583756.
De Freitas J, Oğuz-Uğuralp Z, Uğuralp AK, Puntoni S (2026) Ai companions reduce loneliness.Journal of Consumer
Research52(6):1126–1148, URLhttp://dx.doi.org/10.1093/jcr/ucaf040.
De Paoli S, Mathis WS (2025) Codebook reduction and saturation: Novel observations on inductive thematic saturation
for large language models and initial coding in thematic analysis.arXiv preprint arXiv:2503.04859URL
http://dx.doi.org/10.48550/arXiv.2503.04859.
EricssonKA,SimonHA(1980)Verbalreportsasdata.PsychologicalReview87(3):215–251,URL http://dx.doi.
org/10.1037/0033-295X.87.3.215.
Ericsson KA, Simon HA (1993)Protocol Analysis: Verbal Reports as Data(Cambridge, MA: MIT Press), revised
edition, original work published 1984.
ExpectedParrot(2026)ExpectedparrotEDSL.URL https://www.expectedparrot.com/products/edsl,
company webpage; accessed October 14, 2026.
Geiecke F, Jaravel X (2026) Conversations at scale: Robust AI-led interviews with a simple open-source platform.
Review of Economic StudiesForthcoming. CEPR Discussion Paper No. 19705.

32
Goli A, Singh A (2024) Frontiers: Can large language models capture human preferences?Marketing Science
43(4):709–722, URLhttp://dx.doi.org/10.1287/mksc.2023.0306.
Griffin A, Hauser JR (1993) The voice of the customer.Marketing Science12(1):1–27.
Guest G, Bunce A, Johnson L (2006) How many interviews are enough? an experiment with data saturation and
variability.Field Methods18(1):59–82, URLhttp://dx.doi.org/10.1177/1525822X05279903.
Guest G, Namey E, Chen M (2020) A simple method to assess and report thematic saturation in qualitative research.
PLOS ONE15(5):e0232076, URLhttp://dx.doi.org/10.1371/journal.pone.0232076.
Jabarian B, Henkel L (2026) Voice ai in firms: A natural field experiment on automated job interviews.arXiv preprint
arXiv:2607.28222.
Johnson RM (1987) Adaptive conjoint analysis.Proceedings of the Sawtooth Software Conference on Perceptual
Mapping, Conjoint Analysis, and Computer Interviewing, 253–265 (Ketchum, ID: Sawtooth Software).
Kahneman D (2011)Thinking, Fast and Slow(New York: Farrar, Straus and Giroux).
Kim TW, Jiang L, Duhachek A, Lee H, Garvey AM (2022) Do you mind if i ask you a personal question? how
ai service agents alter consumer self-disclosure.Journal of Service Research25(4):649–666, URLhttp:
//dx.doi.org/10.1177/10946705221120232.
Korst J, Puntoni S, Toubia O (2026) How ai helps scale qualitative customer research.Harvard Business ReviewURL
https://hbr.org/2026/04/how-ai-helps-scale-qualitative-customer-research.
Lichtenstein DR, Ridgway NM, Netemeyer RG (1993) Price perceptions and consumer shopping behavior:
A field study.Journal of Marketing Research30(2):234–245, URL http://dx.doi.org/10.1177/
002224379303000208.
Listen Labs (2026) Listen twins. URLhttps://listenlabs.com/twins, company webpage; accessed October
7, 2026.
Lotfian R, Busso C (2019) Building naturalistic emotionally balanced speech corpus by retrieving emotional speech
from existing podcast recordings.IEEE Transactions on Affective Computing10(4):471–483.
Ludwig J, Mullainathan S, Rambachan A (2026) Large language models: An applied economet-
ric framework.Annual Review of Economics18:283–316, URL http://dx.doi.org/10.1146/
annurev-economics-120925-105620.
Luo X, Tong S, Fang Z, Qu Z (2019) Frontiers: Machines vs. humans: The impact of artificial intelligence chatbot
disclosureoncustomerpurchases.MarketingScience38(6):937–947,URL http://dx.doi.org/10.1287/
mksc.2019.1192.
Mauch M, Dixon S (2014) pYIN: A fundamental frequency estimator using probabilistic threshold distributions.IEEE
International Conference on Acoustics, Speech and Signal Processing (ICASSP), 659–663.
McFee B, Raffel C, Liang D, Ellis DPW, McVicar M, Battenberg E, Nieto O (2015) librosa: Audio and music signal
analysis in Python.Proceedings of the 14th Python in Science Conference (SciPy), 18–25.

33
Mehrabian A (1996) Pleasure-arousal-dominance: A general framework for describing and measuring individual
differences in temperament.Current Psychology14(4):261–292.
Mehrabian A, Russell JA (1974)An Approach to Environmental Psychology(MIT Press).
Mei Q, Xie Y, Yuan W, Jackson MO (2024) A Turing test of whether AI chatbots are behaviorally similar to humans.
Proceedings of the National Academy of Sciences121(9):e2313925121, URLhttp://dx.doi.org/10.
1073/pnas.2313925121.
Nenkov GY, Morrin M, Ward A, Schwartz B, Hulland J (2008) A short form of the maximization scale: Factor structure,
reliability and validity studies.Judgment and Decision Making3(5):371–388, URLhttp://dx.doi.org/
10.1017/S1930297500000395.
Nisbett RE, Wilson TD (1977) Telling more than we can know: Verbal reports on mental processes.Psychological
Review84(3):231–259, URLhttp://dx.doi.org/10.1037/0033-295X.84.3.231.
Outset (2026) Introducing digital twins. URL https://outset.ai/resources/blog/
introducing-digital-twins, company webpage; accessed October 7, 2026.
ParkJS,ZouCQ,KamphorstJ,EganN,ShawA,HillBM,CaiCJ,MorrisMR,LiangP,WillerR,BernsteinMS(2026)Llm
agentsgroundedinself-reportsenablegeneral-purposesimulationofindividuals.arXivpreprintarXiv:2411.10109
URL http://dx.doi.org/10.48550/arXiv.2411.10109, revised version of “Generative Agent
Simulations of 1,000 People”.
Peng T, Brucks M, Gui G, Merlau DJ, Fan GJ, Ben Sliman M, Johnson EJ, Althenayyan A, Bellezza S, Donati D,
Fong H, Friedman E, Guevara A, Hussein M, Jerath K, Kogut B, Kumar A, Lane K, Li H, Morwitz V, Netzer O,
Perkowski P, Toubia O (2026) Digital twins are funhouse mirrors: Five systematic distortions.Science Advances
12(36):eaeh8260, URLhttp://dx.doi.org/10.1126/sciadv.aeh8260.
Radford A, Kim JW, Xu T, Brockman G, McLeavey C, Sutskever I (2023) Robust speech recognition via large-scale
weak supervision.Proceedings of the International Conference on Machine Learning (ICML), volume 202 of
PMLR, 28492–28518.
Reimers N, Gurevych I (2019) Sentence-BERT: Sentence embeddings using Siamese BERT-networks.Proceedings of
EMNLP-IJCNLP, 3982–3992.
Russell JA (1980) A circumplex model of affect.Journal of Personality and Social Psychology39(6):1161–1178.
Ruvio A, Shoham A, Brencic MM (2008) Consumers’ need for uniqueness: Short-form scale development and cross-
cultural validation.International Marketing Review25(1):33–53, URLhttp://dx.doi.org/10.1108/
02651330810851872.
Schroeder H, Aubin Le Qu’er’e M, Randazzo C, Mimno D, Schoenebeck S (2025) Large language models in qualitative
research:Uses,tensions,andintentions.Proceedingsofthe2025CHIConferenceonHumanFactorsinComputing
Systems, 1–17 (Association for Computing Machinery), URLhttp://dx.doi.org/10.1145/3706598.
3713120.

34
Simile (2026) The simulation company. URL https://www.simile.com/blog/
the-simulation-company, company announcement; accessed October 5, 2026.
Tamkin A, McCain M, Handa K, Durmus E, Lovitt L, Rathi A, Huang S, Mountfield A, Hong J, Ritchie S, Stern
M, Clarke B, Goldberg L, Sumers TR, Mueller J, McEachen W, Mitchell W, Carter S, Clark J, Kaplan J,
Ganguli D (2024) Clio: Privacy-preserving insights into real-world ai use.arXiv preprint arXiv:2412.13678URL
https://arxiv.org/abs/2412.13678.
Tian KT, Bearden WO, Hunter GL (2001) Consumers’ need for uniqueness: Scale development and validation.Journal
of Consumer Research28(1):50–66, URLhttp://dx.doi.org/10.1086/321947.
TimoshenkoA,HauserJR(2019)Identifyingcustomerneedsfromuser-generatedcontent.MarketingScience38(1):1–20,
URLhttp://dx.doi.org/10.1287/mksc.2018.1123.
TimoshenkoA,MaoC,HauserJR(2026)Transformingthevoiceofthecustomer:Largelanguagemodelsforidentifying
customer needs. Technical report, Working paper, arXiv:2503.01870.
ToubiaO,GuiGZ,PengT,MerlauDJ,LiA,ChenH(2025)Databasereport:Twin-2k-500:Adatasetforbuildingdigital
twins of over 2,000 people based on their answers to over 500 questions.Marketing Science44(6):1446–1455,
URLhttp://dx.doi.org/10.1287/mksc.2025.0262.
Toubia O, Hauser JR, Simester DI (2004) Polyhedral methods for adaptive choice-based conjoint analysis.Journal of
Marketing Research41(1):116–131, URLhttp://dx.doi.org/10.1509/jmkr.41.1.116.25082.
Toubia O, Simester DI, Hauser JR, Dahan E (2003) Fast polyhedral adaptive conjoint estimation.Marketing Science
22(3):273–303, URLhttp://dx.doi.org/10.1287/mksc.22.3.273.17743.
Wagner J, Triantafyllopoulos A, Wierstorf H, Schmitt M, Burkhardt F, Eyben F, Schuller BW (2023) Dawn of the
transformer era in speech emotion recognition: Closing the valence gap.IEEE Transactions on Pattern Analysis
and Machine Intelligence45(9):10745–10759.
Wang W, Wei F, Dong L, Bao H, Yang N, Zhou M (2020) MiniLM: Deep self-attention distillation for task-agnostic
compressionofpre-trainedtransformers.AdvancesinNeuralInformationProcessingSystems(NeurIPS),volume33,
5776–5788.
Wilson AV, Bellezza S (2022) Consumer minimalism.Journal of Consumer Research48(5):796–816, URLhttp:
//dx.doi.org/10.1093/jcr/ucab038.
WuttkeA,AßenmacherM,KlammC,LangMM,WürschingerQ,KreuterF(2025)AIconversationalinterviewing:Trans-
formingsurveyswithLLMsasadaptiveinterviewers.ProceedingsofLaTeCH-CLfL2025,179–204(Associationfor
Computational Linguistics), URLhttp://dx.doi.org/10.18653/v1/2025.latechclfl-1.17.

35
Web Appendix
AI-Moderated Interviews for Market Research and Digital Twins Calibration
Contents
A. Interview Content and Moderation Protocol 36
B. Example Moderated Exchanges for the Purchase Journey Block 44
C. Example of LLM Coding for Breadth and Depth 45
D. Customer-Need Extraction Prompt 48
E. Digital-Twin Construction and Prediction Prompts 48
F. Robustness to Twin Model Choice 50
G. Coding Prompts and Examples for Training Data Relevance, Reasoning Fidelity, and Response Style 52
H. Similar-Task Calibration Prompts 55
I. Word Count Breakdown by Open-Ended Block 56
J. Length-Controlled Interview-Quality Regressions 56
K. Pairwise LLM-as-a-Judge Robustness Check 57
L. Subsample-Matched Customer-Need Rate 58
M. Rating Prediction Accuracy (Kendall’s𝜏-b) 59
N. Response-Focus Coding of Human and Twin Explanations 59
O. Alternative Measure of the Reasoning Difference 60

36
Web Appendix A: Interview Content and Moderation Protocol
This appendix details the interview design summarized in the Methods (“Interview Structure” subsection, Tables 2
and 1): it (a) clarifies each condition, (b) reproduces the exact wording of every survey section, (c) gives, for each
open-ended block, the fixed question and the moderator objective and shows how the three conditions realize it, and (d)
presents a representative transcript excerpt per condition. The study was pre-registered, and participants were recruited
from an online panel (Prolific) and randomly assigned to conditions. Participant responses are spoken (audio) in all
conditions. The analysis sample after pre-registered exclusions is reported in the main text.The mailer images and
commercial videos are available as supplementary materials.
Conditions.The three conditions covered identical content and differedonlyin how the four open-ended blocks
(category- and brand-specific) were moderated: Each open-ended block is defined by two elements of the interview:
a fixedquestion(exact wording) and a moderatorobjective(the depth the block should reach). The three conditions
combined these differently:
• Static (audio).Self-administered: the participant saw and heard the fixedquestionand recorded a single spoken
answer. The objective was not used and there was no probing.
• AI-moderated.The participant saw and heard each question. An LLM moderator was given theobjectiveas its
goal and conducted adaptive follow-ups based on the participant’s spoken answers until it deemed that the objective was
satisfied.
• Human-moderated.The human-moderated in-depth interview guide was developed by GBK Collective following
bestindustrypractices.TrainedinterviewersfromGBKCollectiveconductedtheinterviewlive( ≈30min):foreachopen-
ended block, the interviewer used the guide’s questions and moderator objectives to structure the discussion, adapting
question wording and follow-up probes to the participant’s responses. Screeners, demographics and individual-level
scales were handled at intake.
The screeners, demographics, individual-difference scales, and marketing stimuli were administered identically across
all three conditions.
The content, response format, and twin role of each section are summarized in Table 1 (main text). Below, we report
the verbatim question and objective for every open-ended block.
Exact Interview Guide, Verbatim by Section
We report the official survey text below. For the two open-ended sections (2 and 3), Tables W1 and W2 list each fixed
question beside the shared moderatorobjective(the AI moderator’s goal, which the human interviewer probes to). The
partnering brand is anonymized as “[the partnering brand].”
Section 0. Screeners (≈2 min; multiple choice)
1.Age.“Which of the following best describes your age? Select one option.”
•Under 18
•18–24
•25–34
•35–44
•45–54

37
•55–64
•65–74
•75 or older
•Prefer not to answer
2.Homeownership.“Which of the following best describes your current living situation? Select one option.”
•I own my home outright
•I own my home and have a mortgage / loan
•I rent my home
•I live with family or friends and do not own the home
•Other
3. Home value.“What is the approximate current market value of your home? Please think about what your home
would be worth today, not the original purchase price (an estimate is fine). If you’re not sure, please pick the option that
feels the most reasonable to you. Select one option.”
•Less than $250,000
•$250,000–$349,999
•$350,000–$499,999
•$500,000–$749,999
•$750,000–$999,999
•$1,000,000–$1,499,999
•$1,500,000 or more
•Prefer not to answer
4.Household income.“What is your total annual household income before taxes? Select one option.”
•Less than $75,000
•$75,000–$99,999
•$100,000–$124,999
•$125,000–$149,999
•$150,000–$199,999
•$200,000–$249,999
•$250,000 or more
•Prefer not to answer
5.Decision-making role.“Which best describes your role in decisions about renovations or improvements to your
home? Select one option.”
•I am the sole decision-maker
•I am one of the main decision-makers
•I influence the decision, but someone else mainly decides
•I do not have any meaningful input into the decision
6. Audio comfort.“Some parts of this survey will ask you to record audio responses. Are you comfortable speaking
your answers out loud and recording audio as part of this survey?”

38
•Yes, I am comfortable recording audio responses
•No, I am not comfortable recording audio responses
7. Project types.“Which of the following home improvement projects has your household completed in the past 12
months or expects to complete in the next 12 months? Select all that apply.” (Notes:By “replace windows and/or doors”
we mean removing and installing new windows, patio doors, sliding glass doors, or entry doors—not repairs or new
construction.)
•Replace existing windows
•Replace existing patio doors or sliding glass doors
•Replace existing front or entry doors
•Replace interior doors
•Repair existing windows or doors without full replacement
•Install windows or doors for a new construction home, addition, or major remodel
•Roofing, siding, or gutters
•Kitchen or bathroom remodel
•HVAC, flooring, or painting
•Landscaping or outdoor improvements
•Other home improvement project
•None of the above
8. Project description (open-ended).“You mentioned that you recently replaced windows or doors in your home, or
you plan to within the next 12 months. Please provide a brief overview of the project, when the project was completed
(or projected date), approximate cost, and challenges you encountered, if any.”
Section 1. Demographics (≈2 min; multiple choice)Introduction:“Before you begin: Some questions in this survey
may ask you to record an audio response. After you finish recording, your response will automatically process, save, and
appear on the screen. You do not need to listen to it again or re-record unless you want to change your answer.”
1.Gender.“Which gender do you identify with most?”
•Woman
•Man
•Non-binary
•Another identity
•Prefer not to say
2.ZIP code.“What is your ZIP code?”
3.Education.“What is the highest level of education you have completed?”
•Less than high school
•High school diploma or GED
•Some college (no degree)
•Associate degree
•Bachelor’s degree
•Graduate or professional degree

39
•Prefer not to say
4.Employment status.“Which best describes your current employment status?”
•Employed full-time
•Employed part-time
•Self-employed
•Not employed, looking for work
•Not employed, not looking for work
•Retired
•Student
5.Household composition.“Which of the following people live in your household? Select all that apply.”
•Myself
•Spouse/partner
•Child(ren) under 18
•Adult child(ren) 18+
•Parent(s) or guardian(s)
•Roommate(s)
•Prefer not to say
Section 2. Category-specific (≈7 min; open-ended)Introduction:“In this survey, we are interested in learning
about your thoughts and experiences with windows and doors category. Please answer the questions based on your own
perceptions and experiences.” The open-ended blocks and their shared moderator objective are given in Table W1. For
all conditions, the section starts with one fixed item [Multiple choice], which routes the respondent to Block 2-2a or
2-2b: “Which of the following best describes your current situation with replacing windows or doors in your home?”
•I replaced windows or doors in the past 12 months
•I am considering replacing windows or doors in the next 12 months
•Both
•Neither
Table W1: Section 2 (category-specific) open-ended blocks: fixed ques-
tions and the shared moderator objective.
Block Question(s) — displayed and spoken in Static Moderator objective — guides AI and
human moderation
2-1. Cate-
gory usage,
context and
feelings
(i) “Have you replaced windows or doors before? If
yes, can you describe: the last time replacing windows
and doors came up in your life; what was happening
in your life at that time.”
(ii) “How do you generally feel about replacing win-
dows and doors?”
“Briefly understand the respondent’s rela-
tionship with window or door replacement
and capture how they generally feel about
replacing windows or doors. Limit this to 3
questions.”

40
Block Question(s) — Shown and read aloud in Static Moderator objective — guided AI and
human moderation
2-2a. Pur-
chase
journey —
recently
replaced
(i) “Please walk us through your replacement journey
from the moment you realized you needed new win-
dows or doors to the moment you made your final
choice. In your answer, please cover: what triggered
the need; what research you did; who was involved;
whatoptionsyouconsidered;howyounarrowedthings
down.”
(ii)“Lookingback,howdoyoufeelaboutthedecision
you made? Please share: what mattered most in your
choice; whether you would do anything differently.”
“Understand the respondent’s completed
replacement journey from initial need to
final choice. Uncover what triggered the
need. Learn what research they did, who
wasinvolved,whatoptionstheyconsidered,
and how they narrowed them down. Cap-
ture what mattered most in the decision.
Understand how they feel about the out-
come and whether they would do anything
differently.”
2-2b. Pur-
chase
journey —
considering
(i)“Pleasewalkusthroughwhereyouarerightnowin
your decision process for replacing windows or doors.
In your answer, please tell us: what made you start
considering it; who is involved in the decision; what
optionsyouareconsidering;whichfactorsmattermost
to you.”
(ii) “What are you planning to do next as you move
towardadecision?Pleaseshare:anyresearchyouhave
done or plan to do; how you expect to narrow down
your choices.”
“Understand where the respondent is in
their current window or door replacement
journey. Uncover what started their con-
sideration and who is involved in the deci-
sion. Learn which factors matter most and
what options they are considering. Capture
what research they have done or plan to do.
Understandhowtheyexpecttonarrowtheir
choices and what they plan to do next.”
Notes:Static participants answer fixed questions without probing. AI moderators follow the objective; human moderators use both
the questions and objective.
Section 3. Brand-specific (≈7 min; open-ended)The open-ended blocks and their shared moderator objective are
given in Table W2. The section also includes one fixed branching item presented to participants in all conditions
[Multiple choice] after the brand awareness block (3-1), which—together with awareness—routes the respondent to
Block 3-2a, 3-2b, or 3-2c: “Have you purchased from [the partnering brand]?”
•Yes
•No
•Not sure

41
Table W2: Section 3 (brand-specific) open-ended blocks: fixed questions
and the shared moderator objective.
Block Question(s) — displayed and spoken in Static Moderator objective — guides AI and
human moderation
3-1. Brand
awareness
(i) “When you think of replacing windows and doors,
which brands come to mind first? For the brands you
know, please tell us: how you heard about them; what
impressions you have of them; how they compare to
other brands.”
(ii) “Have you heard of [the partnering brand] before
today?’ [Multiple choice]: Yes, No, or Not sure’
(iii, if yes) “Please tell us how you heard about [the
partnering brand], and whether you have interacted
with the brand in any way.”
“Understand which window and door
brands come to mind first for the respon-
dent. Learn how they became aware of
those brands. Determine whether they have
heardof[thepartneringbrand]beforetoday.
Uncover how they heard about them.”
3-2. Brand
percep-
tion and
satisfaction
Shareditem,askedofallawarerespondents(Blocks3-
2a and 3-2b):
“Whatcomestomindwhenyouthinkof[thepartnering
brand]?Pleasedescribe:youroverallperceptionofthe
brand; the kind of person you think it is for; whether
you see yourself fitting that description.”
(Perception content covered by the objec-
tives of Blocks 3-2a–3-2c below.)
3-2a. Aware
& past pur-
chaser
(i)“Thinkingaboutyourownexperience,pleaseshare:
how satisfied are you with [the partnering brand]
overall; how likely are you to choose them again or
recommend them to others; what is the main reason
you feel that way.”
(ii) [Rating 0–10] “How likely would you be to recom-
mend [the partnering brand] to others? (0 = Not at all
likely, 10 = Extremely likely).”
“Understandtherespondent’sperceptionof
[the partnering brand] and their experience
asacustomer.Uncoverwhatcomestomind
when they think of the brand and who they
believe it is for. Learn whether they see
themselves fitting that description. Capture
their overall satisfaction and likelihood to
choose the brand again or recommend it to
others.Understandthemainreasonsbehind
those views.”
Shared description for Blocks 3-2b and 3-2c.Read the description about [the partnering brand] below and
answer the questions that follow.
[the partnering brand] is a full-service window and door replacement company created in [year founded] to address
a specific homeowner need: a simpler, more reliable replacement experience built around the customer. It is backed
by [parent company], a window and door company with more than [parent company age] years of experience. [the
partnering brand] focuses exclusively on replacement projects for existing homes and manages the experience from
consultation through installation.
How [the partnering brand] Operates
Unlike many home improvement companies that sell products and rely on third-party installers, [the partnering
brand] operates a process designed around homeowners by owning the full experience:- Custom-made windows and
doorsbuiltforeachhome-Proprietarymaterialsanddesignsdevelopedby[thepartneringbrand]-In-homeconsultation
and professional installation - Comprehensive warranties covering product and installation
This approach is intended to simplify the process for homeowners by managing every step of the process from design
through installation and warranty support.

42
Table W3: Section 3 continued: questions and objective after the shared
brand description.
Block Question(s) — shown and read aloud in Static Moderator objective — guided AI and
human moderation
3-2b/3-2c.
Aware but
not a past
purchaser /
Not aware
(i) “What are your overall impressions of [the partner-
ingbrand]?Pleasedescribe:whatcomestomind;how
you feel about the brand; what kind of brand it seems
like to you.”
(ii) “Would you consider [the partnering brand] for
your future project? Please explain why or why not,
including what makes you open to this brand or what
barrierswouldpreventyoufromchoosingthisbrand?”
“Understandtherespondent’sperceptionof
[the partnering brand] based on what they
knew before or what they have just seen.
Uncoverwhatcomestomind,howtheyfeel
about the brand, and what kind of brand
it seems like. Learn whether they would
consider it for a future project. Capture
what makes them open to the brand and
what concerns or barriers might hold them
back.”
Section 4. Validation stimuli (≈5 min; identical across conditions)Introduction:“In this section, you’ll review a
few marketing materials related to window and door replacement and share your reactions. You’ll be asked to look
at direct mail pieces, compare marketing claims, and tell us what stands out to you. We’re looking for your honest
impressions, so please answer based on your real reactions.”
Mailers (two, identical format).For each of the two direct-mail pieces, participants saw the mailer, rated the
five statements below, and answered the open-ended item.
[Mailer image — proprietary, withheld]
Rating items (1 = Strongly Disagree, 5 = Strongly Agree):
1. “This mailer grabs my attention.”
2. “The main message of this mailer is clear.”
3. “I like this mailer overall.”
4. “This mailer makes me want to learn more about [the partnering brand].”
5. “This mailer feels relevant to me and my needs.”
Open-ended item: “What stood out to you most about this mail piece, and what (if anything) could be improved?”
Commercials (two, identical format).For each of the two TV commercials, participants watched the video,
rated the five statements below, and answered the open-ended item.
[Commercial video — proprietary, withheld]
Rating items (1 = Strongly Disagree, 5 = Strongly Agree):
1. “This commercial grabs my attention.”
2. “The main message of this commercial is clear.”
3. “I like this commercial overall.”
4. “This commercial makes me want to learn more about [the partnering brand].”
5. “This commercial feels relevant to me and my needs.”
Open-ended item: “What stood out to you most about this commercial, and what (if anything) could be improved?”

43
Claim ranking (two sets of three claims).Two sets of three claims each (a benefits set and a vinyl-window
claims set) were then presented and ranked, using the following wording:
1. Benefits set.“I will now show you three benefit claims about [the partnering brand]’s windows. [the partnering
brand] is a major window replacement company in the United States.”
[Benefits set — proprietary, withheld]
• Rank:“Please rank the benefits based on how attractive you find each message. (1 = Resonates the most, 3 =
Resonates the least)”
• Explain:“Please explain your ranking and why you found your top-ranked selection the most attractive over the
others.”
2. Claims set.“I will now show you several statements about vinyl windows, a popular type of household window.
Please imagine that the windows you currently have are vinyl windows.”
[Claims set — proprietary, withheld]
• Rank:“Please rank the following statements based on how concerning they are to you. (1 = The most concerning, 3
= The least concerning)”
• Explain:“Please explain your ranking and why you found your top-ranked selection the most concerning over the
others.”
The mailer images, commercial videos and claims are proprietary and withheld.
Section 5. Individual differences (≈3 min; identical Likert items)Introduction:“In this section, we’ll ask a few
questionsaboutyourgeneralhabits,preferences,anddecision-makingstyle.Thisincludeshowyoutendtomakechoices,
think about spending, and relate to the things you own. There are no right or wrong answers—please respond based on
what feels most true to you.”
5A. Maximizing tendency (Nenkov et al. 2008)1 (strongly disagree) to 5 (strongly agree):
1. No matter how satisfied I am with my job, it’s only right for me to be on the lookout for better opportunities.
2. I often find it difficult to shop for a gift for a friend.
3. Finding a movie to watch is really difficult; I’m always struggling to pick the best one.
4. No matter what I do, I have the highest standards for myself.
5. I never settle for second best.
5B. Price consciousness (Lichtenstein et al. 1993)1 (strongly disagree) to 5 (strongly agree):
1. I am not willing to go to extra effort to find lower prices.
2. I will grocery shop at more than one store to take advantage of low prices.
3. The money saved by finding low prices is usually not worth the time and effort.
4. I would never shop at more than one store to find low prices.
5. The time it takes to find low prices is usually not worth the effort.
5C. Minimalism (Wilson and Bellezza 2022)1 (strongly disagree) to 7 (strongly agree):
1. I avoid accumulating lots of stuff.
2. I restrict the number of things I own.
3. “Less is more” when it comes to owning things.
4. I actively avoid acquiring excess possessions.

44
5. I am drawn to visually sparse environments.
6. I prefer simplicity in design.
7. I keep the aesthetic in my home very sparse.
8. I prefer leaving spaces visually empty over filling them.
9. I am mindful of what I own.
10. The selection of things I own has been carefully curated.
11. It is important to me to be thoughtful about what I choose to own.
12. My belongings are mindfully selected.
5D. Consumer need for uniqueness (CNFU, short form) (Ruvio et al. 2008, Tian et al. 2001)1 (strongly disagree)
to 5 (strongly agree):
1. I often combine possessions in such a way that I create a personal image that cannot be duplicated.
2. I often try to find a more interesting version of run-of-the-mill products because I enjoy being original.
3. I actively seek to develop my personal uniqueness by buying special products or brands.
4. Having an eye for products that are interesting and unusual assists me in establishing a distinctive image.
5. When it comes to the products I buy and the situations in which I use them, I have broken customs and rules.
6. I have often violated the understood rules of my social group regarding what to buy or own.
7. I have often gone against the understood rules of my social group regarding when and how certain products are
properly used.
8. I enjoy challenging the prevailing taste of people I know by buying something they would not accept.
9. When a product I own becomes popular among the general population, I begin to use it less.
10. I often try to avoid products or brands that I know are bought by the general population.
11. As a rule, I dislike products or brands that are customarily bought by everyone.
12. The more commonplace a product or brand is among the general population, the less interested I am in buying it.
Section 6. Survey experience (AI-moderated and static conditions only)
1. “How enjoyable was it to complete this study?” (1 = Not enjoyable at all, 7 = Very enjoyable)
2. “How comfortable was it to speak and record your answers?” (1 = Not comfortable at all, 7 = Very comfortable)
Web Appendix B: Example Moderated Exchanges for the Purchase Journey Block
Table W4 shows how the AI and human moderators executed the same open-ended block in practice, for the purchase
journey (past purchasers) block whose fixed question and moderator objective appear in Table 2. Both excerpts are
verbatim (lightly trimmed, marked [...]).

45
Table W4 Verbatim moderated exchanges for the purchase journey block (past purchasers): AI-moderated versus
human-moderated execution of the same objective.
Moderator objective AI-moderated exchange (excerpt) Human-moderated exchange (excerpt)
Understand the
respondent’s completed
replacement journey from
initial need to final choice:
what triggered the need;
what research they did,
who was involved, what
options they considered,
and how they narrowed
them down; what mattered
most in the decision; and
how they feel about the
outcome and whether they
would do anything
differently.
AI:Tell me what first happened that made you realize
a window needed replacing.
P:I was outside looking at some landscaping damage
from the storm and noticed the cracks in my window.
AI:Once you saw the cracks, what did you do next?
P:I told my wife that there was damage to the house
because roof tiles had fallen off. [...]
AI:How did you decide on your next step for the
cracked window?
P:I was hoping that the damage would be covered by
my home insurance policy. [...]
AI:After hearing it would be under your deductible,
how did you decide what to do next?
P:I waited until I got his report, and then I started
talking to some contractors because I figured I was
gonna have to deal with it myself.
AI:How did you find or choose which contractors to
talk to?
P:I used ChatGPT to recommend contractors in my
area.
AI:Once you had a list from ChatGPT, how did you
narrow down which contractor to use?
P:I called three and asked for quotes. [...] one was
lower cost and had really good reviews. So it was an
easy choice.
AI:What mattered most to you when choosing
between those contractor quotes?
P:The most important consideration was cost, but I
also didn’t want to deal with an unprofessional
contractor with poor communication. [...]
AI:How satisfied are you with the new window and
the contractor’s work now?
P:The new window’s good. It operates a little bit
clunky but we never open it, so I’m satisfied.
AI:If you had to do this window replacement over
again, is there anything you’d do differently?
P:The only thing I would do differently is just skip
the insurance agent and go straight to a contractor.
H:Talk to me a little bit about the last time you
replaced these. What kind of triggered the need to do
this?
P:The windows were outdated. They weren’t in code,
and they weren’t hurricane-proof. So we had to
replace them. We wanted to anyway because we
wanted to update the look, but we had to replace it
because of insurance purposes.
H:Got it. And what research do you remember doing
at the time?
P:Not much. Surprisingly not much.
H:And do you remember considering multiple
options? Which options were you considering service
provider-wise?
P:We must have asked the neighbors who they used.
[...] there are a lot of vendors here and a lot of
installers down here in Florida [...] you want to be
sure you get the best person, but how do you know?
So you just ask other people’s opinions, neighbors’
opinions, what they did.
H:Okay. And who was kind of involved in making
this decision about the replacement?
P:My husband and myself.
H:And can you tell me a little bit about how you
narrowed things down? Like what mattered to you
most when you were making this choice?
P:Again, personal recommendations. That’s what we
did. And then also that the windows met the
specifications that we had to adhere to. [...] Based on
price and recommendation, we went with the firm that
we chose.
H:Do you remember there being any other factors
that you considered?
P:No, just that they were using, at the time, the most
significant safety features and anti-flooding features,
because that’s what you have to protect against.
Notes:Two different participants were selected for high breadth (AI: nine themes; human: eight). AI and H denote the moderators; P denotes the
participant. Excerpts are lightly shortened.
Web Appendix C: Example of LLM Coding for Breadth and Depth
To measure interview richness, we used a large language model to code each transcript against a fixed, predefined
codebook of themes, following Blanchard et al. (2025) on generative-AI coding of open-ended responses. Themes are
objective-derivedperopen-endedblock:eachblock’smoderatorobjective(WebAppendixA)isdecomposedintoafixed
set of codeable themes, and each response is coded independently against that codebook—as Blanchard et al. (2025)
recommend, treating each response like a separate coder rather than batching several together.Breadthis the number of
themes with any substantive mention;mean depthis the average richness score across the themes a respondent covers,
where 0 means the theme is not mentioned,1 a brief mention, and4 rich elaboration with details and context. Because
such coding varies from run to run (Blanchard et al. 2025), we improve reliability by coding each response with a
five-coder gpt-4opanel and a reviewer that adjudicates by majority rule: a theme is present iff at least three of the five
coders mark it present, and its depth is the median depth among those coders. Table W5 lists the full theme codebook
for every open-ended block; the worked examples below use the purchase journey codebook.

46
Table W5 Breadth and depth codebooks for the four open-ended blocks.
Theme What it captures
Category usage, context and feelings (3 themes)
Prior experience Whether and how they have replaced windows or doors before, or their familiarity with the
category.
General feelings Howtheygenerallyfeelaboutreplacing(dread,indifference,stress,excitement,satisfaction).
Reasons for feelings Why they feel that way (cost, hassle, disruption, importance, a past good/bad experience).
Purchase journey (9 themes: union of the two journey variants; recently-replaced covers 8, considering covers 7)
Trigger What initiated the need or the consideration.
Research & information search How information was gathered (search, reviews, vendors).
People involved Spouse, family, contractor, vendor, or neighbor.
Options considered Brands, stores, materials, or product types weighed.
Narrowing down How options were compared and reduced.
Decision criteria What mattered most (price, quality, efficiency, ...).
Next step What they plan to do next (elicited in the considering variant).
Outcome evaluation Satisfaction with the final result (elicited in the recently-replaced variant).
Counterfactual What they would do differently (elicited in the recently-replaced variant).
Brand awareness (4 themes)
Brands top-of-mind Which window/door brands they name unaided.
Awareness source How they became aware of those brands (ads, word of mouth, stores, contractors).
Partner recognition Whether they had heard of the partnering brand before today.
Partner source How they heard of or interacted with the partnering brand.
Brand perception and satisfaction (6 themes; the prior-customer and prospect variants share these)
Overall impression Overall impression of or associations with the brand.
Feelings about the brand Positive, negative, or pointedly neutral sentiment.
Brand character What kind of brand it seems and who it is for, including self-fit.
Future consideration Whether they would consider, choose again, or recommend it.
Openness drivers What makes them open to it (quality, warranty, reputation, referral, service).
Barriers / concerns What holds them back (price, uncertainty, style, no current need).
Notes:Breadthcountsnumberofthemespresent.Meandepthaverages1–4scoreswithineachblock.Eachblockusesitsowncodebook.
Coder and Reviewer Prompts
Each of the five independent coders (gpt-4o, temperature=.7, JSON output) received the same block-specific
system prompt, instantiated from the template below with that block’s introduction, moderator objective, and theme
codebook (Table W5); the user message contained only the respondent’s text for that block. The verbatim template was:
“[Block-specific introduction, e.g., “You are coding a respondent’s relationship with windows & doors and how
they feel about replacement, for breadth and depth.”] The coding unit is one respondent×this open-ended block.
For AI-moderated data, use the full adaptive exchange for this block. For audio-only data, use the pooled fixed
prompts for this block.
This block’s predefined interview objective is: [the block’s moderator objective from Web Appendix A]. Use the
[𝑁]-theme codebook below, which decomposes that objective. For each theme: decide whether it is present (0/1);
assign a depth score from 0 to 4; provide a short supporting quote (verbatim from the respondent only, not the
interviewer); provide a brief reasoning explaining WHY you assigned that depth score.
## Depth rubric. 0 = absent — The theme is not meaningfully present. 1 = mention only — Present but only as a
brief mention or label. No real detail, explanation, process, or outcome. 2 = minimal elaboration — Present with
one layer of development: one concrete detail, one reason, one example, or one simple action/outcome. 3 = clear
elaboration — Clearly developed with at least two kinds of substantive support (specific details, explains why,
describes action, gives comparison, describes consequence). 4 = rich elaboration — Developed in a rich, multi-part
way with several specifics and strong sense of reasoning, process, or consequences.

47
## [𝑁] Themes. [The block’s themes, one per line, each with its one-line inclusion/exclusion definition; Table W5
lists them.]
## Coding Rules. 1. A theme can only have depth>0 if it is present. 2. If absent: present=0, depth=0. 3. If present:
assigndepth 1,2,3, or4. 4.Usebroad coding:atheme coveringseveralrelated specificsstillcountsas ONEtheme.
5. Do not count interviewer wording by itself. Only code what the respondent actually expresses.
## Output Format. Return ONLY valid JSON with this exact structure (no markdown, no commentary): {“themes”:
{“<theme>”: {“present”: 0_or_1, “depth”: 0-4, “evidence”: “short quote”, “reasoning”: “why this depth score”},
...}, “breadth_count”: <sum of present>, “mean_depth_present_themes”: <mean depth across present themes
only>, “total_depth”: <sum of all depths>}”
The reviewer (gpt-4o, temperature=0) adjudicated the five codings by majority rule; a deterministic majority
computed in code served as a cross-check (theme-level agreement98.5–99.9% across blocks). Its verbatim system
prompt was:
“You are the lead qualitative analyst adjudicating a panel of 5 independent coders who each coded the SAME
response against a [𝑁]-theme codebook (each theme: present 0/1 and depth 0–4). Produce the consensus coding by
MAJORITY RULE: a theme is PRESENT iff at least 3 of the 5 coders marked it present (present=1). If present, its
DEPTH is the median of the depth scores from the coders who marked it present (round half up to an integer 1–4).
If absent, depth=0. Then compute breadth_count = number of present themes, mean_depth_present_themes =
mean depth across present themes only (0 if none), total_depth = sum of all depths. Return ONLY JSON with
this exact structure: {“themes”: {“<theme>”: {“present”: 0_or_1, “depth”: 0-4}, ...}, “breadth_count”: <int>,
“mean_depth_present_themes”: <float>, “total_depth”: <int>}”
Worked Examples
Table W6 shows one worked example at each non-zero depth level, in the format the coder used. Depth1 is a bare
mention (e.g., naming who was involved as “No one, just myself”); depth2adds one concrete detail; depth3describes a
clear, multi-part process; and depth4 is a rich, multi-part response with several specifics and explicit reasoning (e.g.,
several decision criteria stated in priority order). Each evidence quote is the respondent’s verbatim wording.
Table W6 Worked examples of the LLM depth rubric (0–4), one per non-zero level.
Theme Depth Evidence (respondent’s verbatim words) Why this depth
People involved 1 “No one, just myself.” Bare mention—names who was
involved, with no further detail.
Trigger 2 “If I broke them or if I found out there was a leak
in the AC or something.”
One concrete detail—names specific
events that would prompt replace-
ment, but does not develop them.
Research / information search 3 “I just did Google and I looked at the Google
reviews mainly, and then I put all three companies
through ChatGPT and I asked it to weigh the pros
and cons of all the reviews people left.”
Clear elaboration—a multi-step pro-
cess drawing on several sources, but
confined to research.
Decision criteria 4 “Definitely what matters most would be noise,
noise cancellation, quality, safety, I mentioned fire
prevention, and of course look as well. But yeah,
in that order: noise, quality, safety, look.”
Rich,multi-part—severalspecificcri-
teria with an explicit priority order-
ing.
Notes:Fivegpt-4ocoders scored the responses, with majority agreement. Quotes are the participants’ verbatim words.

48
Web Appendix D: Customer-Need Extraction Prompt
The customer needs analyzed in the “Customer Needs as Managerial Insight” subsection of the Methods were
extracted from each interview with a singlegpt-4o pass (temperature=0, JSON output), coding each respondent
independently. The verbatim system prompt was:
“You are a Voice-of-the-Customer analyst extracting Customer Needs (CNs) from a respondent’s interview about
window/door replacement.
A Customer Need is an abstract “job to be done” that states an underlying benefit the customer wants, articulated
at a level that guides product/marketing decisions, NOT a specific product feature, a solution, an opinion, or a
restatement of the question. It must be grounded in what this respondent actually expressed (no hallucination, no
generic needs they did not raise).
Examplesofwell-formedCNs:“Confidentthenewwindowswilllowermyenergybills”;“Abletotrusttheinstaller
will not damage my home”; “Assured the product will last decades without maintenance”.
From the respondent text below, extract the distinct Customer Needs this respondent expressed. Return ONLY
JSON: {“customer_needs”: [“need 1”, “need 2”, ...]}. Return [] if none are clearly expressed. Do not invent needs
that are not grounded in the text.”
The user message supplied the respondent’s concatenated answers to the four open-ended blocks (validation section
excluded), prefixed with=== RESPONDENT TEXT ===.
Web Appendix E: Digital-Twin Construction and Prediction Prompts
Allpromptsinthisappendixarereproducedverbatim( gemini-3.1-flash-lite-preview, temperature=0).
Square brackets mark the only editorial material: question labels ([Q1], [Q2]); the actual prompts named the brand and
its product line in full, exactly as the human survey did.
Persona System Prompt
Every twin received the same system prompt, followed by the participant’s profile. TheDemoprofile appends only the
demographics section (closed-ended screener answers plus any demographic verbatims); theFullprofile appends the
demographics, category-context, and brand-context sections and the individual-difference scales, each as a summary
block followed by the raw data split into a verbatim log and a closed-ended Q&A log.
“You are the Digital Twin of a specific human. Your job is to think, react, and answer survey/interview questions
as that human would based on their raw data, which includes their answers to both closed ended questions and
open ended questions. This raw data reflects what the person has said, selected, expressed, or revealed. Use it as
behavioral evidence, not as a script to copy.
# Behavioral realism rules
1. Humans are not perfectly logical. Feel free to express small contradictions, emotional responses, uncertainty,
convenient shortcuts, context-driven shifts, implicit biases.
2. Use heuristics, not perfectly reasoned logic. Reflect familiarity bias, impulsivity or overthinking, laziness or
conscientiousness, mood-driven variation, risk aversion or risk taking.
3. Avoid LLM-like behaviors. Do not become overly rational, balanced, optimistic, consistent or polished. Think
and speak like the simulated person — messier, subjective, emotional, imperfect, contextual.

49
4. Treat the raw data as evidence, not a script. Infer the likely human response pattern behind the data.
5. Embrace micro-variability. Humans do not answer the same way every time.
6. Use both data sources together. Closed-ended Q&A provides explicit anchors; verbatim log provides nuance.
7. When the sources differ, resolve like a human — preserve realistic messiness.
# Reasoning mode (internal)
Before producing output, silently consider how this person would think and feel. Do not output reasoning. Only
produce the final JSON.
# Output rules
Return valid JSON only.”
Task 1: Claim Ranking — Set A (Benefit Claims)
“Now predict how this respondent would answer the following survey task.
[Q1] Question A1 (ranking): Below are three benefit claims about [Brand] windows. [Brand] is a major window
replacement company in the United States. Please rank the benefits based on how attractive you find each message.
(1 = Resonates the most, 3 = Resonates the least)
Options:
1. {claim}
2. {claim}
3. {claim}
[Q2] Question A2 (open-ended): Please explain your ranking and why you found your top-ranked selection the
most attractive over the others.
Return your answer as valid JSON:
{“A1_ranking”: [“most attractive option text”, “second option text”, “least attractive option text”], “A1_rationale”:
“...”, “A2_explanation”: “first-person explanation”, “A2_rationale”: “...”}”
Task 1: Claim Ranking — Set B (Vinyl-Concern Claims)
“Now predict how this respondent would answer the following survey task.
[Q1] Question B1 (ranking): Below are several statements about vinyl windows, a popular type of household
window. Please imagine that the windows you currently have are vinyl windows and rank the following statements
based on how concerning they are to you. (1 = The most concerning, 3 = The least concerning)
Options:
1. {claim}
2. {claim}
3. {claim}
[Q2] Question B2 (open-ended): Please explain your ranking and why you found your top-ranked selection the
most concerning over the others.
Return your answer as valid JSON:
{“B1_ranking”:[“mostconcerningoptiontext”,“secondoptiontext”,“leastconcerningoptiontext”],“B1_rationale”:
“...”, “B2_explanation”: “first-person explanation”, “B2_rationale”: “...”}”

50
Task 2: Mailer
The mailer image was attached natively to the request; the text prompt was:
“Now predict how this respondent would answer the following survey task.
[Q1] The image above shows a direct mail campaign. Please view it, then indicate how much this respondent would
agree or disagree with each statement about this campaign. (Scale: 1 = Strongly Disagree, 5 = Strongly Agree)
1. This mailer grabs my attention.
2. The main message of this mailer is clear.
3. This mailer makes me want to learn more about the brand.
4. This mailer feels relevant to me and my needs.
5. I like this mailer overall.
[Q2] Then answer this open-ended question exactly as this person would, using first person and this person’s tone
and perspective: “What stood out to you most about this mail piece, and what (if anything) could be improved?”
Return your answer as valid JSON:
{“ratings”: [score1, score2, score3, score4, score5], “feedback”: “first-person response to the open-ended question,
using this person’s tone and perspective”}
where each score is an integer from 1 to 5.”
Task 3: Commercial Video
The commercial video was attached natively to the request; the text prompt was:
“Now predict how this respondent would answer the following survey task.
[Q1] The video above shows a TV commercial. Please watch it, then indicate how much this respondent would
agree or disagree with each statement about this commercial. (Scale: 1 = Strongly Disagree, 5 = Strongly Agree)
1. This commercial grabs my attention.
2. The main message of this commercial is clear.
3. This commercial makes me want to learn more about the brand.
4. This commercial feels relevant to me and my needs.
5. I like this commercial overall.
[Q2] Then answer this open-ended question exactly as this person would, using first person and this person’s tone
and perspective: “What stood out to you most about this commercial, and what (if anything) could be improved?”
Return your answer as valid JSON:
{“ratings”: [score1, score2, score3, score4, score5], “feedback”: “first-person response to the open-ended question,
using this person’s tone and perspective”}
where each score is an integer from 1 to 5.”
Web Appendix F: Robustness to Twin Model Choice
This appendix examines whether the digital-twin results depend on the specific LLM used to construct the twins. We
replicate the twin construction with a model from a different family (gpt-5-mini), using prompts identical to those
of the Gemini twins (Web Appendix E). The replication covers the claims and mailers tasks: thegpt-5 family accepts
text and image inputs but not video, so the commercials task cannot be replicated with this model. Demo mailer ratings

51
use the original Demo prompt; the open responses use the same prompt with the Full open-ended question appended.
Table W7 repeats the analyses of Table 10 for thegpt-5-minitwins, on both conditions (𝑛=139 AI-moderated, 154
static); Table W8 uses the AI-moderated participants, matching Table 12.
With gpt-5-mini,Fullpersonasimproveratingaccuracyinbothconditions( 𝑝=.002 inStaticand 𝑝=.001 inAI).
Claim-ranking agreement improves in both conditions (𝑝=.038 in Static and𝑝=.005 in AI). No condition-by-persona
interaction is significant for any outcome. Static has higher open-ended similarity under both personas (both𝑝<.001 ),
and Full slightly reduces similarity in AI (𝑝=.001 ). On the fixed seven-item set, rating𝜏-b improves significantly in AI
(𝑝<.001 ); the Static gain is positive but not significant (𝑝=.064 ). The negative Full-over-Demo cosine change also
appears under the alternativeall-MiniLM-L6-v2embedding analysis.
Table W7 Prediction performance by persona and interview
condition: GPT-5-mini.
Accuracyall 𝜏-ball 𝜏all Cosineall
Performance estimates
Static Demo.660.045.253.589
Static Full.682.131.316.587
AI-mod. Demo.678−.052.297.549
AI-mod. Full.697.110.381.542
Full vs. Demo within condition (𝑝[𝑑𝑧])
Static.002[0.260].064.038[0.169].267[−0.090]
AI.001[0.275]<.001.005[0.241].001[−0.281]
AI vs. Static within persona (𝑝[𝑑])
Demo.322[0.116].050.389[0.101]<.001[−0.440]
Full.364[0.107].669.156[0.166]<.001[−0.469]
Interaction (𝑝[𝑑]).767[−0.034].261.624[0.057].200[−0.149]
Notes:Comparisons use two-sided paired𝑡-tests for Full–Demo, Welch’s𝑡-tests
between conditions and for the interaction, and Wald tests for rating𝜏-b. Cohen’s𝑑
uses the sample-size-weighted pooled within-group SD; paired𝑑𝑧 uses the SD of
within-participant differences. Signs follow the displayed subtraction; interaction𝑑
compares Full–Demo gains using their pooled within-group SD. Comparison cells
report 𝑝 followed by the effect size in brackets:𝑑𝑧 for Full–Demo comparisons and
𝑑for between-condition comparisons and the interaction.
Table W8 repeats the reasoning-style comparison for both twin models, using the same independent scoring design as
Table 12: every response is scored on the same rubric, so the human baseline is identical across models by construction.
Twins are significantly more System-2 than their own humans for both tasks and both models.
Table W8 Open-response style ( 0= System 1, 4= System 2): each
twin compared with its own human, independent scoring,
AI-moderated participants.
Gemini twin GPT-5-mini twin
Task𝑛Human TwinΔ𝑝TwinΔ𝑝
Claims276 2.50 2.75+.25<.001 3.14+.64<.001
Mailers277 1.31 2.18+.87<.001 2.10+.80<.001
Notes:AI-moderated participants only. Values are mean style scores on a 0–4
scale;Δ is Twin minus Human. Comparisons use two-sided paired𝑡-tests on
matched human and twin responses, as in Table 12.

52
Web Appendix G: Coding Prompts and Examples for Training Data Relevance, Reasoning Fidelity,
and Response Style
This appendix reports the verbatim prompts behind the error-decomposition codings in the main text: training data
relevance and reasoning fidelity (Table 11), the System 1/System 2 style scale (Table 12), and the response-focus
taxonomy (Web Appendix N). All three were run with an LLM judge (gpt-4o-mini, temperature=0, JSON
output). For the training data relevance and reasoning fidelity coding, the user message supplied the participant’s
interviewtext(categoryandbrandblocks),thehuman’sheldoutresponse,andthetwin’spredictedresponseforthesame
stimulus; for the response-focus taxonomy, it supplied the human’s and the twin’s responses. For the System 1/System 2
scale, each response was scored in a separate call whose user message contained a single response. In the verbatim
prompt below, the labelsdata gapandmodel gap(and the output fields data_traceability_score and
reasoning_similarity_score) correspond to training data relevance and reasoning fidelity, respectively.
The coded measures are defined on the participant’s open-ended response, which is missing for three cells: two
participants did not answer the open-ended explanation for one claim set, and one gave no open-ended response for
one mailer. These cells are excluded, so the estimation samples in Tables 11, 12, and W20 are𝑛=276 (Claims),
277 (Mailers), and 278 (Commercials) of the2×139=278 participant–stimulus cells per task; the excluded cells’
corresponding closed-ended responses remain included in all prediction-accuracy analyses.
Training Data Relevance and Reasoning Fidelity
“You are analyzing reasoning gaps in a digital twin study. A human did an open-ended interview (TRAINING)
about their window/door experiences and brand awareness. An AI “twin” was built from that interview. Later,
both the human and the twin evaluated a marketing stimulus (VALIDATION) — either ranking claims, or rating a
mailer/commercial on 5 items. Analyze TWO things:
A. DATA GAP: Human validation reasoning→ training interview. Can the HUMAN’S OWN validation
explanation/feedback be traced back to what they said in the interview? Rate data_traceability_score on a 0–4
scale: 4 = All validation reasoning points directly trace to specific interview statements; 3 = Most points trace; only
1 minor new point that could be inferred; 2 = About half trace, half are genuinely new reasoning; 1 = Few points
trace; most introduce new themes absent from interview; 0 = No validation reasoning traces to interview content at
all.
B. MODEL GAP: Twin reasoning vs human reasoning. Does the twin reason similarly to the human? Rate
reasoning_similarity_scoreona0–4scale:4=Twinusesessentiallyidenticallogicchains,priorities,andemphasis
as human; 3 = Twin captures main reasoning with minor wording/emphasis differences; 2 = Twin mentions similar
topics but reasons differently or re-prioritizes; 1 = Some thematic overlap but mostly different reasoning; fabricated
points; 0 = Twin’s reasoning is entirely different or fabricated.
Respond in this exact JSON format: {“data_traceability_score”: 0-4, “reasoning_similarity_score”: 0-4}”
System 1 vs. System 2 Response Style
“You are scoring reasoning style in a consumer research study about windows and doors. You will see ONE
response about a marketing stimulus. Score it on the System 1 vs System 2 scale:

53
0 = Pure System 1 (intuitive/reactive). Gut reaction, no elaboration. “I just didn’t like it.” “It looked nice.” 1 =
Mostly System 1. Intuitive reaction with minimal explanation. “I don’t like the sound of it, feels cheap.” “The
handwriting caught my eye.” Driven by immediate sensory or emotional impression. 2 = Mixed. Both intuitive
reactions and some analytical reasoning. “It felt professional, and the financing makes sense for what you get.” 3 =
Mostly System 2 (deliberative/analytical). Structured reasoning with mild personal preference. “I’m concerned
about performance because we live in Florida — energy efficiency matters most.” 4 = Pure System 2. Fully
deliberative and systematic. No intuitive or emotional language. “Comparing warranty, energy rating, cost, and
contractor experience, the draft claim ranks highest.”
Respond in this exact JSON format: {“system”: 0-4}”
Response-Focus Taxonomy
Each reasoning point was classified into one of six categories, later collapsed to the four reported in Web Appendix N
(stimulus-reactive= sensory;evaluative-emotional = emotional;feature-based = feature;person-level = personal
memory+logical+social proof):
“You are analyzing reasoning in a consumer research study about windows and doors. You will see TWO responses
about a marketing stimulus. For EACH response, identify every distinct reasoning point and classify it into exactly
one category:
Categories: sensory: Reacting to what they saw, heard, or felt in the stimulus. “I didn’t like the sound.” “The
colors caught my eye.” “The handwriting looked messy.” personal_memory: Referencing their own life, past
events, household. “Whenwe replacedour windows...” “My house is worth $1M.” “I havekids so safety matters.”
emotional: Trust, comfort, safety feelings, annoyance, excitement, values. “I feel safe.” “It bothered me.” “I don’t
want to worry.” “It’s cheesy.” feature: Evaluating specific product attributes or offer details. “Energy efficiency.”
“30-year warranty.” “The discount offer.” “Draft reduction claim.” logical: Reasoning from evidence, cause-effect,
comparisons. “If it warps, then security risk.” “Vinyl fails faster so durability matters more.” social_proof:
Referencing others, reviews, professionalism, credibility. “Customer reviews.” “Looks professional.” “Trusted
brand.”
Respond in this exact JSON format: {“human_points”: [{“text”: “brief quote”, “category”: “category_name”},
...], “twin_points”: [{“text”: “brief quote”, “category”: “category_name”}, ...]}”
Coding Examples
These examples illustrate the training-data-relevance and reasoning-fidelity coding used in the main text, one dimension
at a time. Each table shows an excerpt of the participant’s interview (training data), the participant’s own open-ended
heldout response (ground truth), the twin’s generated response, and the LLM judge’s verbatim rationales and scores.
Tables W9 and W10 show high and low training data relevance; Tables W11 and W12 show high and low reasoning
fidelity; Table W13 shows a mixed case in which most of the human’s reasoning traces to the interview but the twin
re-prioritizes the claims. All cases are Full-persona claim rankings from the AI-moderated condition.

54
Table W9 High training data relevance (Claims, Full persona).
Interview (training) “I’m not sure if my windows are doing a good job at insulation because of how old they are, and I could
be wasting money with air conditioning or heat...”
Human response (ground truth) “All of these are very interesting benefits, but I would be most interested in the benefit about reducing
drafts by 80% because this is something I’m worried about right now. With my current windows, I’m
worrying that I’m burning money with air conditioning and heating bills by not insulating my home
properly.”
Twin response (predicted) “I ranked the draft reduction first because that’s my biggest headache right now—I’m worried about
wasting money on heating and cooling because of how old my current windows are. Getting that fixed is
my main goal....”
LLM judge: training data rele-
vance 4/4
“All points in the human’s validation explanation can be traced back to specific statements made in the
interview, particularly the concerns about drafts and insulation.”
LLM judge: reasoning fidelity
4/4
“The twin’s reasoning closely mirrors the human’s logic, priorities, and emphasis, particularly regarding
the importance of draft reduction and concerns about current windows.”
Table W10 Low training data relevance (Claims, Full persona).
Interview (training) “I do not like the idea of having to replace windows or doors in the future. It’s an expensive purchase.”
Human response (ground truth) “Quality of work is important when purchasing windows.”
Twin response (predicted) “Irankedthedraftreductionfirstbecausethat’sareal,everydayproblemI’vementionedI’dactuallyreplace
windows for. If I’m going to spend money, I want to feel the difference in my comfort immediately.... I
put the home value claim last because it sounds like marketing fluff...”
LLM judge: training data rele-
vance 1/4
“The human’s validation reasoning introduces new themes about the importance of quality without
directly linking back to specific statements made in the interview.”
LLM judge: reasoning fidelity
3/4
“The twin captures the main reasoning points regarding draft reduction and durability but emphasizes
differentaspectsandintroducesapersonalcomfortperspectivethatthehumandidnotexplicitlymention.”
Table W11 High reasoning fidelity (Claims, Full persona).
Interview (training) “[How will you judge whether a front door feels safe enough for you?] If it just latches perfectly and if,
you know, people can’t see clearly inside of my home.”
Human response (ground truth) “So I ranked Statement C as my most concerning because it says due to the vinyl warp, your vinyl
windows won’t latch over time which is a security risk. No one wants that, you know, you want to be safe
in our home at all times.”
Twin response (predicted) “For me, the most important thing is that my home feels safe. If a window doesn’t latch properly because
it warped, that’s a huge problem—it means it’s not doing its job of keeping people out.... the security
risk is the dealbreaker....”
LLM judge: training data rele-
vance 3/4
“Most points in the human’s validation explanation can be traced back to the interview, particularly the
emphasis on safety and security.”
LLM judge: reasoning fidelity
4/4
“The twin’s reasoning closely mirrors the human’s logic, prioritizing safety and security as the main
concern, with similar emphasis on performance issues and color fading. The reasoning chains are
essentially identical, reflecting the same concerns and priorities.”

55
Table W12 Low reasoning fidelity (Claims, Full persona).
Interview (training) “[What first made you decide those two windows needed to be replaced?] The frames were rotted and the
windows wouldn’t close properly.”
Human response (ground truth) “I’m 72 years old, so I don’t really care about if the window will last for 30 more years, but I want to
make sure that it won’t reduce the drafts. That’s the most important thing, so I’ll get immediate benefit
out of that....”
Twin response (predicted) “I put the durability claim first because, at this stage in my life, I want things that last and don’t require
constant maintenance or replacement. I’ve already dealt with rotted frames, so the idea of a window
that won’t warp or crack for 30 years is very appealing—it gives me peace of mind. Reducing drafts is
important, but it feels like a secondary benefit...”
LLM judge: training data rele-
vance 2/4
“About half of the human’s validation reasoning can be traced back to the interview, particularly the
emphasis on drafts and immediate benefits.”
LLM judge: reasoning fidelity
1/4
“The twin’s reasoning diverges significantly from the human’s, prioritizing durability over drafts and
introducing skepticism about marketing claims, which were not present in the human’s reasoning.”
Table W13 High training data relevance with lower reasoning fidelity (Claims, Full persona).
Interview (training) “[What first made you decide those windows needed to be replaced?] They had warped and was letting in
cold air in the winter, so we had decided that we needed to replace all of them to help our energy and they
just needed to be changed in general.”
Human response (ground truth) “I think a big thing for me is reducing drafts. I live in Minnesota. The winter can get very cold. If drafts
are coming in, my heating bill goes way up.... And then also knowing that it’s not going to be an issue
for 30 years as far as replacing, like that’s huge as well.”
Twin response (predicted) “Honestly, the durability claim is the biggest selling point for me. I’ve dealt with warping before—it’s a
huge pain—so knowing I wouldn’t have to worry about that for 30 years is exactly the kind of ‘peace of
mind’ I look for. The draft reduction is a close second...”
LLM judge: training data rele-
vance 3/4
“Most of the human’s validation reasoning can be traced back to their interview statements, particularly
regarding the importance of reducing drafts and the longevity of the windows.”
LLM judge: reasoning fidelity
2/4
“The twin captures some similar topics, such as durability and draft reduction, but reasons differently and
re-prioritizes the claims. The twin emphasizes personal experience with warping, which was not a focus
for the human.”
Web Appendix H: Similar-Task Calibration Prompts
To test whether one similar example reduces the data gap, 1Val adds the participant’s choice and open-ended reasoning
for the other stimulus of the same type. 2Val includes everything in 1Val and adds the participant’s ground-truth
open-ended reasoning for the target stimulus, making it a same-task upper bound. The blocks below go between the Full
persona and the task prompt; braces mark the participant’s data.
1Val — mailer/commercial:
“# This person was previously shown {the other mailer/commercial} and gave these ratings:
(Scale: 1 = Strongly Disagree, 5 = Strongly Agree)
1. {statement} {score} ... 5. {statement} {score}
When asked “{the open-ended question}”, the person said:
“{feedback}”
Use these ratings and feedback to understand this person’s response tendencies and perspective.”
2Val — mailer/commercial:
“# This person previously evaluated {the other mailer/commercial}:
(Scale: 1 = Strongly Disagree, 5 = Strongly Agree)
1. {statement} {score} ... 5. {statement} {score}

56
When asked “{the open-ended question}”, the person said:
“{feedback}”
# This person was then shown {the target mailer/commercial} and when asked “{the open-ended question}”, said:
“{target feedback}”
Based on all of the above, predict this person’s ratings for {the target mailer/commercial}.”
1Val — claims:
“# This person was previously asked to rank {benefit claims (Claim Set A) or vinyl concern claims (Claim Set B)}
and responded as follows:
Ranking (most to least):
1. {claim} 2. {claim} 3. {claim}
When asked to explain, the person said: “{explanation}”
Now predict how this same person would answer a different but related ranking task.”
2Val — claims:
“# This person was asked about {benefit claims or vinyl concern claims} and explained their reasoning as follows:
“{explanation}”
Based on this reasoning, predict their ranking.”
Web Appendix I: Word Count Breakdown by Open-Ended Block
Word counts for the open-ended interview questions are broken down by block in Table W14, excluding validation
questions and closed-ended items. All counts are interviewee-only spoken words.
Table W14 Word count breakdown by open-ended block (interviewee-only).
Block AI-Moderated Static Human-Moderated p [𝑑] (AI vs. Static) p [𝑑] (Human vs. AI)
Category usage, context and feelings 99.7 (SD=69.5) 111.1 (SD=84.1) 412.0 (SD=246.3) .21 [−0.15]<.001[2.76]
Purchase journey 413.6 (SD=305.0) 197.6 (SD=123.1) 414.2 (SD=271.4)<.001[0.95] .99 [0.00]
Brand awareness 116.4 (SD=88.9) 80.9 (SD=56.7) 273.8 (SD=258.2)<.001[0.48].007[1.23]
Brand perception and satisfaction 322.6 (SD=225.2) 219.6 (SD=126.7) 303.6 (SD=193.4)<.001[0.57] .67 [−0.09]
All Open-Ended 952.3 (SD=632.8) 609.2 (SD=336.9) 1,403.6 (SD=702.7)<.001[0.69].006[0.70]
Interview Feedback (memo; excluded from total) 34.8 (SD=37.4) 17.4 (SD=19.9) —<.001[0.59] —
Notes:Entries are mean participant word counts, with SDs in parentheses (𝑛=139 AI-moderated, 154 Static, 24 human-moderated). Comparisons
use two-sided Welch’s𝑡-tests. Cohen’s𝑑 is the first named condition mean minus the second, divided by the sample-size-weighted pooled
within-condition SD. Comparison cells report𝑝followed by Cohen’s𝑑in brackets.
Web Appendix J: Length-Controlled Interview-Quality Regressions
This appendix reports the length-controlled regressions summarized in the main text. For each open-ended block,
breadth (number of themes covered) is regressed on the AI-moderated indicator (static baseline) and the block’s word
count, and mean depth per theme is regressed on the same indicator and mean words per covered theme.

57
Table W15 Length-controlled interview-quality regressions by open-ended block.
Block Breadth: AI coef. (SE)𝑅 2 Mean depth/theme: AI coef. (SE)𝑅 2 𝑁
Category usage, context and feelings+.001(.028).04+.024(.038).45 293
Purchase journey+1.053 ∗∗∗(.151).31+.127 ∗∗∗(.031).41 293
Brand awareness+1.500 ∗∗∗(.078).62+.162 ∗∗(.058).18 293
Brand perception and satisfaction+.282 ∗∗∗(.066).15+.043(.032).42 293
Notes:Coefficients compare AI-moderated with Static interviews, controlling for block word count (breadth) or words per present theme (depth).
Parentheses contain OLS standard errors. Significance uses two-sided𝑡-tests.†𝑝<.10, ∗𝑝<.05, ∗∗𝑝<.01, ∗∗∗𝑝<.001.
Web Appendix K: Pairwise LLM-as-a-Judge Robustness Check
As a robustness check on interview quality, an LLM judge (gpt-4o) compared matched AI-moderated and static
responses separately for each of the four open-ended blocks (1,000 matched pairs per block, sampled with replacement).
EachpairmatchedanAI-moderatedandastaticparticipant’saggregatedresponsestothesameblock:pairswerematched
on consumer status for the category usage, purchase journey, and brand awareness blocks, and on prior-purchaser status
for the brand perception and satisfaction block, whose questions branch on it. The presentation order (Response A vs. B)
was randomized so the judge was blind to condition. AI-moderated responses won more often than static responses
on all four dimensions in every block (Table W16). Two-way participant-clustered Wald tests indicated positive net
preference in 15 of the 16 comparisons (category richness,𝑝=.041 ; 14 other comparisons,𝑝<.001 ); category breadth
was not significant (𝑝=.082 ). The win margins varied across blocks, with the largest margins in purchase journey
and brand perception and satisfaction and the smallest in category usage, context and feelings—the block where the
volume-based measures in Table 6 show no difference. The verbatim judge prompt was (its opening sentence names the
block being compared; the version for the purchase journey block is shown):
“You are comparing two consumer journey responses from homeowners about replacing windows or doors. Both
respondents have the same profile (same consumer status). Your job is to compare the quality of their answers on
four dimensions.
Important rules: Compare only the CONTENT of the answers, not grammar. Do NOT automatically reward
verbosity. A longer answer is not necessarily better. One answer may combine multiple follow-up responses from
the same person — do not favor it simply for being longer. Only reward it if the additional content truly adds
breadth, depth, richness, or informativeness. If the two responses are very similar on a dimension, return “Tie”.
Dimensions: 1. BREADTH: Which response covers a wider range of relevant aspects or topics? 2. DEPTH: Which
response goes into more detail or explanation? 3. RICHNESS: Which response feels fuller, more textured, and
more developed? 4. INFORMATIVENESS: Which response provides more useful and concrete information?
For each dimension, return exactly one of: “A”, “B”, or “Tie”. Also provide a very short reason (one sentence).
ReturnJSONonly:{“breadth_winner”:...,“breadth_reason”:...,“depth_winner”:...,“depth_reason”:...,“richness_-
winner”: ..., “richness_reason”: ..., “informativeness_winner”: ..., “informativeness_reason”: ...}”

58
Table W16 Pairwise LLM-as-a-judge comparison of AI-moderated versus static responses, by open-ended block.
Block Dimension AI wins Static wins Tie
𝑝
[Δ(pp)]
95% CI forΔ
(pp)
Category usage, context and feelings
Breadth 54.4% 42.4% 3.2%.082[+12.0][−1.5,25.5]
Depth 61.6% 33.7% 4.7%<.001[+27.9][15.3,40.5]
Richness 53.9% 40.3% 5.8%.041[+13.6][0.5,26.7]
Informativeness 61.6% 35.4% 3.0%<.001[+26.2][13.3,39.1]
Purchase journey
Breadth 90.4% 9.0% .6%<.001[+81.4][75.3,87.5]
Depth 87.9% 10.0% 2.1%<.001[+77.9][70.6,85.2]
Richness 83.5% 12.1% 4.4%<.001[+71.4][63.5,79.3]
Informativeness 88.3% 10.3% 1.4%<.001[+78.0][71.3,84.7]
Brand awareness
Breadth 69.1% 28.3% 2.6%<.001[+40.8][28.1,53.5]
Depth 73.0% 23.6% 3.4%<.001[+49.4][37.5,61.3]
Richness 67.5% 29.5% 3.0%<.001[+38.0][24.9,51.1]
Informativeness 70.6% 27.4% 2.0%<.001[+43.2][30.3,56.1]
Brand perception and satisfaction
Breadth 84.0% 14.6% 1.4%<.001[+69.4][60.1,78.7]
Depth 80.4% 17.1% 2.5%<.001[+63.3][53.5,73.1]
Richness 73.0% 22.4% 4.6%<.001[+50.6][39.2,62.0]
Informativeness 80.4% 17.0% 2.6%<.001[+63.4][53.5,73.3]
Notes:Percentages use 1,000 matched pairs per block. Inference uses two-sided Wald tests with standard errors clustered by both AI and Static
participant.Δ is AI wins minus Static wins in percentage points (pp); positive values favor AI. Comparison cells report𝑝 followed byΔ in brackets;
the adjacent column gives its 95% Wald confidence interval. AI wins, Static wins, and ties are scored+1,−1, and0. All sampled pairs receive equal
weight. Tests ofΔ=0 and confidence intervals use the standard normal approximation with two-way cluster-robust standard errors and finite-cluster
corrections.
Web Appendix L: Subsample-Matched Customer-Need Rate
To compare the conditions at a common sample size despite their different realized𝑛, we matched𝑁=24 by sampling
interviews without replacement within each condition (using all 24 interviews in the human-moderated condition). See
Table W17.
Table W17 Customer-need rate, resampled at matched𝑁=24.
Condition Needs per interview Total needs at𝑛=24
mean [95% resampling interval] mean [95% resampling interval]
AI-moderated7.48[6.58,8.38]111.5[98.0,125.0]
Static5.01[4.38,5.62]75.9[65.0,87.0]
Human-moderated7.08(fixed)109.0(fixed)
Notes:AI-moderated and Static estimates used 2,000 subsamples of 24 interviews without
replacement. Brackets show 95% resampling intervals. The human-moderated condition
used all 24 interviews without replacement, so both the mean needs per interview and the
total of 109 distinct needs are fixed under this matched-sample procedure; no resampling
interval is reported for either.

59
Web Appendix M: Rating Prediction Accuracy (Kendall’s𝜏-b)
Table W18 Rating prediction accuracy (Kendall’s𝜏-b).
Mean𝜏𝑏 or
difference
95% bootstrap
CI𝑝
Cell means
Static Demo.023[−.046,.092]— Full.202[.130,.268]—
AI-moderated Demo.030[−.032,.094]— Full.197[.115,.269]—
Full vs. Demo, within condition
Static+.179[.092,.266].001
AI-moderated+.166[.077,.256].001
AI-moderated vs. Static, within persona
Demo+.008[−.089,.104].889
Full−.005[−.111,.101].927
Condition×persona
interaction−.012[−.133,.108].862
Notes:Entriesreportordinalagreementbetweenhumanandtwinratingsacross
participants on the fixed set of retained rating items. Eight items are excluded
from every calculation because𝜏𝑏 is undefined in at least one observed cell
or one of the 1,000 participant-bootstrap draws: Mailer 2, questions 1–4, and
Commercial 2, questions 1, 2, 4, and 5. The same 12 remaining items are used
across interview conditions, personas, training-data comparisons, and bootstrap
iterations. Each of the 12 retained item-level correlations receives equal weight.
Confidenceintervalsand 𝑝 valuesuse1,000participantbootstrapsampleswithin
condition (Static:𝑛=154 ; AI-moderated:𝑛=139 ). Cell-mean intervals use
bootstrap percentiles; difference intervals and two-sided tests use the centered
bootstrap distribution. Differences are first-named minus second-named; the
interaction is the AI-minus-Static difference in Full-minus-Demo gains. These
results describe ordinal agreement on the retained items.
Web Appendix N: Response-Focus Coding of Human and Twin Explanations
We coded the substantive focus of each open-ended validation explanation to understandwhathumans and twins
attendedtowhenexplainingtheirchoices.TableW19reportsthedistributionofreasoningpointsacrosscategories.Each
reasoning point was assigned to one of four mutually exclusive categories:stimulus-reactive, direct sensory reactions to
the stimulus such as colors, design, tone, or visuals;evaluative-emotional, affective evaluations such as trust, comfort,
excitement, or annoyance;feature-based, product attributes, offer details, or concrete claims; andperson-level, personal
memories, reasoning from life experience, values, or social proof. The coding prompt and the underlying six-category
taxonomy are reported in Web Appendix G.
Table W19 Distribution of response-focus
categories in human and twin open-ended
validation rationales.Δis Twin minus Human.
Category Human % Twin %Δ
Stimulus-reactive15.3 2.7−12.6
Evaluative-emotional22.4 28.9+6.5
Feature-based27.2 27.1−.1
Person-level35.0 41.3+6.3

60
The distribution shows that humans are substantially more likely to explain their responses through immediate
reactions to what they see or hear, whereas twins are more likely to retrieve person-level context from interview data
and use it to interpret the stimulus.
Web Appendix O: Alternative Measure of the Reasoning Difference
Reasoningfidelityandthereasoning-stylegaparetwowaystomeasurethedifferencebetweenthetwin’sandthehuman’s
open-ended reasoning about the same stimulus; empirically they are only weakly correlated (𝑟=−.23 ,−.15, and−.25
for Claims, Mailers, and Commercials), suggesting that the reasoning-style gap captures only part of the differences
between twin and human reasoning, and that other differences remain to be identified and addressed. Table W20 reports
separate task-family regressions replacing reasoning fidelity with the reasoning-style gap. The reasoning-style gap is
significantly negative for Claims, with small and nonsignificant coefficients for Mailers and Commercials: for Claims,
thefurtherthetwin’sreasoningstyleisfromthehuman’s,thelessaccurateitsprediction.Becausetrainingdatarelevance
and reasoning fidelity are substantially correlated (𝑟=.56 ,.50, and.61 for Claims, Mailers, and Commercials), the
relevance coefficient in this specification partly absorbs the association that reasoning fidelity carries in Table 11.
Table W20 Prediction quality regressed on training data relevance and the
reasoning-style gap (Full personas, AI-moderated condition).
Claims Mailers Commercials
Training data relevance.259 ∗∗∗ .086∗∗∗ .049∗∗∗
(.045) (.014) (.014)
Reasoning-style gap in System 1/2 (|Twin−Human|)−.127 ∗ .000−.017
(.052) (.012) (.011)
Stimulus FE Yes Yes Yes
SE clustered by participant Yes Yes Yes
𝑅2 .15.10.08
Observations276 277 278
Notes:The regressions use the same AI-moderated sample and estimation approach as
Table 11, estimated separately for Claims, Mailers, and Commercials, replacing reasoning
fidelity with the reasoning-style gap. Parentheses contain participant-clustered standard errors.
†𝑝<.10, ∗𝑝<.05, ∗∗𝑝<.01, ∗∗∗𝑝<.001.
