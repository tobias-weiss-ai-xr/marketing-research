---
title: 'The Brand War: A Gamified AI-Feedback System for Time-Limited EFL Writing'
url: https://arxiv.org/abs/2608.28604
category: digital-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Jing-Yuan Huang
- Vivien Lin
- Yujong Park
- Yi Miao
- Yun-Hua Hsiao
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.28604
pages: 6
chars: 32689
fetched_at: '2026-11-08T13:21:54+00:00'
kb_version: 1
---

# The Brand War: A Gamified AI-Feedback System for Time-Limited EFL Writing

The Brand War: A Gamified AI-Feedback System
for Time-Limited EFL Writing
Jing-Yuan Huang∗, Vivien Lin †, Yujong Park ‡, Yi Miao §, Yun-Hua Hsiao †, Michael Pin-Chuan Lin ¶∗,
Daniel Chang ∥‡, Seong Min Park §, Marco Ho ∗∗, Michael S. Hsiao ††, and Jeeho Ryoo §
∗Simon Fraser University, Canada
†National Changhua University of Education, Taiwan
‡Sungkyunkwan University, Korea (South)
§Fairleigh Dickinson University, Canada
¶Mount Saint Vincent University, Canada
∥Athabasca University, Canada
∗∗British Columbia Institute of Technology, Canada
††Virginia Tech, USA
Abstract—Writing is a cognitively demanding and anxiety-
provoking skill for English as a Foreign Language (EFL) learners,
particularly under time-limited conditions. This paper presents
The Brand War, a web-based gamified writing application that
combines competitive game mechanics with iterative OpenAI
GPT-4.1-powered formative feedback for undergraduate EFL
learners in a timed narrative writing task. The application situates
students as marketing interns competing for a job offer, using
review passes to receive AI feedback, attack opponents, or shield
their own passes while drafting a 500-word brand story. We
conducted an exploratory single-session classroom study with
N= 29 university EFL students in Taiwan to examine how
students engaged with the system, whether iterative AI feedback
improved writing performance across revision attempts, and how
AI and human scores related to overall outcomes. Students wrote
their brand story within 60 minutes, using up to five AI feedback
passes before a final human-graded submission. Most students
(65.5%) used the AI feedback system, and within-student AI
scores improved modestly across revision attempts ( M= +3.7
points, SD= 7.4 ), with larger gains among students completing
more review cycles and scores significantly higher on the final
review than the first among those who completed multiple cycles
(p=.032 ). AI-assessed and human final scores showed strong
convergent validity (r= 0.722, p <0.001), and students who used
AI feedback scored descriptively, though not significantly, higher
than non-users. Students maintained a high mean focus ratio of
82.4%, and competitive mechanics were used sparingly, suggesting
most students prioritized writing over social interference even
when such options were available. Findings suggest that embedding
iterative AI scoring within a competitive game context is feasible
and may scaffold writing improvement, with implications for EFL
writing pedagogy and AI-mediated gamified learning design.
Index Terms—gamification, EFL writing, AI feedback, for-
mative assessment, game-based learning, self-regulated learning
I. INTRODUCTION
Writing in a second or foreign language is cognitively
demanding and anxiety-inducing [1] because writers juggle
meaning-making and language control simultaneously, and
the gap between what they intend to express and what they
can express in the second language produces both cognitive
strain and self-doubt. For EFL (English as a Foreign Language)
writers, the challenge is compounded when writing is time-
constrained, such as in course exams, proficiency assessments,
or professional workplace tasks. Despite the prevalence of
timed writing in real-world contexts, instructional approaches
that effectively support EFL writers under such conditions
remain underdeveloped.
Two independent lines of research offer complementary
solutions. First,gamification, the application of game design
elements in non-game contexts [2], has demonstrated positive
effects on learner motivation and engagement in EFL writing
tasks [3], [4]. Competitive game mechanics, narrative storylines,
and reward structures can transform writing from a solitary,
anxiety-laden exercise into an engaging, goal-directed activity.
Second, AI-generatedformative feedbackhas emerged as a
scalable tool for assessing student writing, with studies showing
that while human evaluators retain advantages in nuanced prior-
itization and affective tone, AI scoring demonstrates convergent
validity with expert raters on criteria-based dimensions [5]. The
provision of rapid, rubric-aligned feedback enables iterative
revision cycles that conventional classroom instruction rarely
affords.
Despite these parallel advances, few systems have attempted
to unify both approaches in a single learning environment.
Most gamified writing studies use non-adaptive mechanics
(e.g., leaderboards and badges) without coupling them to
substantive writing feedback [4]. Conversely, AI feedback
systems are typically deployed in standalone tools that lack
the motivational architecture of a game. The combination,
where game mechanics create urgency and investment while
AI feedback guides improvement within that game, represents
a largely unexplored design space.
This paper introducesThe Brand War, a web-based ap-
plication designed to address this gap. In The Brand War,
undergraduate EFL students assume the role of marketing
interns competing for a job offer, writing a 500-word brand
story under a 60-minute time limit. Students are allocated
five AI feedback passes, each enabling one cycle of OpenAI
GPT-4.1-powered scoring and evaluation of students’ current
arXiv:2608.28604v1  [cs.CY]  4 Jul 2026

draft. Competitive mechanics, including the ability to attack
opponents’ passes and deploy shields, add an optional layer of
social competition.
We conducted an exploratory single-session classroom study
with N= 29 university EFL students in Taiwan to investigate
three research questions.
• RQ1.How do students engage with a gamified AI-
feedback writing system during a time-limited writing
task?
• RQ2.Does iterative AI feedback improve students’ writing
performance across successive revision attempts?
• RQ3.How do convergent AI and human scores, and the
use of competitive mechanics, relate to overall writing
outcomes?
The remainder of this paper reviews relevant literature (Sec-
tion II), describes the system design (Section III), presents the
study methodology (Section IV), reports results (Section V),
and discusses implications and limitations (Sections VI–VII).
II. LITERATUREREVIEW
A. Gamification in EFL Writing
Deterding et al. [2] define gamification as “the use of
game design elements in non-game contexts,” distinguishing it
from full game-based learning by its application of individual
components, such as points, levels, and leaderboards, to existing
activities. Zhihao and Zhonggen [3] showed that gamified
elements improve learners’ engagement and writing quality
in time-limited tasks, though over-gamification can diminish
motivation once reward saturation is reached. A scoping review
by Guo et al. [4] synthesized 22 studies on game-related
writing methods, finding digital games the most common
format and competitive mechanics and storylines effective
for engagement, but noting a scarcity of designs that couple
mechanics to substantive feedback. Lin et al. [6] similarly found
that a tangible language game combining competition and
collaboration (“coopetition”) was accepted across proficiency
bands, with weaker students gaining the most, suggesting
competitive design is a tunable variable rather than a binary
choice.
B. Game-Based Learning and Narrative Writing
Beyond gamification, full game-based learning (GBL) en-
vironments that situate students within immersive storylines
have shown promising outcomes for writing motivation and
performance. Narrative framing transforms writing into purpose-
ful, audience-directed communication, reducing the abstraction
that often contributes to EFL writing anxiety [7], consistent
with frameworks that frame writing within professional or
scenario-driven narratives to reduce anxiety and L2 fatigue
[8]. Narrative-driven GBL also offsets disengagement during
extended writing practice, with enjoyment predicting sustained
motivation and skill gains across L1 and L2 cohorts [9]. Xiao
et al. [7] integrated ChatGPT-powered non-player characters
(NPCs) into storyline-driven GBL for argumentative EFL
writing, finding higher intrinsic motivation, situational interest,
and essay quality without increased cognitive load, an approach
that informed The Brand War’s professional narrative scenario,
with AI extended here from an interactional NPC role to a
formative scoring agent.
C. AI Feedback in EFL Writing
Theoretical models have proposed how GenAI can support
self-regulated learning and writing instruction [10], [11], and
the use of LLMs for writing assessment has accelerated rapidly.
Steiss et al. [5] compared ChatGPT-generated feedback with
human expert feedback, finding AI feedback approached human
quality on surface-level linguistic features, though human
raters retained an edge in nuanced, holistic judgment. AI-
based scoring is nonetheless cost-effective and immediate, well-
suited to time-constrained classrooms where human feedback
cycles are impractical. Huang and Chen [12] proposed the
Gamified Self-Regulated English Learning (G-SERL) system,
combining ChatGPT assistance with gamified reinforcement
and self-regulation nudges, reporting gains in post-test writing
performance relative to a ChatGPT-only control.
D. Theoretical Framework
Three complementary theories ground the design and in-
terpretation of The Brand War.Self-Determination Theory
(SDT) [13] posits that intrinsic motivation is sustained when
three basic psychological needs, autonomy, competence, and
relatedness, are met. The game’s competitive scenario supports
relatedness, the iterative AI scoring system supportscompe-
tencethrough immediate, specific feedback, and the choice
to use passes offensively or constructively supportsautonomy.
Self-Regulated Learning(SRL) theory [14] frames learning as a
cyclical process of planning, monitoring, and reflection, which
the AI feedback pass mechanic operationalizes as students
draft, receive evaluative information, set micro-goals, and revise.
Finally, Vygotsky’s [15]Zone of Proximal Development(ZPD)
offers a scaffold-oriented lens, in which the OpenAI GPT-
4.1 scoring model acts as a “more knowledgeable other” that
provides performance signals students cannot easily generate
for themselves.
E. Research Gap
Existing research has separately shown that gamification
supports EFL writing engagement, that narrative contexts
reduce writing anxiety, and that AI feedback can reliably assess
and improve student writing. However, no systemintegrates
competitive game mechanics, a storyline-driven writing task,
and iterative AI formative scoring within a single real-classroom
deployment. The present study addresses this gap with an
exploratory dataset from a live classroom implementation in
Taiwan.
III. SYSTEMDESIGN: THEBRANDWAR
A. Learning Context and Task
The Brand War writing app was designed for an under-
graduate mandatory EFL writing course at a university in
Taiwan. The target task was a 500-word narrative brand
story that students were required to write within 60 minutes.
The brand story writing task required the participants to

TABLE I
SUMMARY OFGAMEMECHANICS INTHEBRANDWAR
Mechanic Description
Review Pass Each student begins with 5 passes. Spending one
pass submits the current draft for OpenAI GPT-
4.1 scoring and feedback. Up to 5 revision cycles
are possible.
Attack A student may spend a pass to destroy one
of an opponent’s passes, reducing the target’s
remaining feedback opportunities.
Shield Each student holds one shield. Activating it
protects a pass from the next incoming attack.
Final Submit At any point before the time limit, a student
submits their current draft as the final essay for
human grading.
incorporate five narrative elements covered in the preceding
instructional unit, namelysetting,theme,mood,character, and
plot. This task design reflects authentic genre demands, since
brand storytelling is increasingly recognized as a professional
competency in marketing contexts, and provides a motivational
anchor aligned with the game scenario.
B. Game Scenario and Storyline
To frame the writing task within a competitive narrative,
The Brand War situates students as candidates competing for
a summer internship at “Global Marketing, Inc.,” a fictional
top-tier marketing firm at Taipei 101. The instructor introduces
the scenario in the following terms.
“This summer, you will be looking for summer
internships at Global Marketing, Inc. located in
Taipei 101 to experience the real world of marketing.
In the Brand War, you need to get to the top by
getting a job offer. You must finish writing a brand
story to bring to your interview. ”
This storyline grounds the abstract writing task in a concrete
professional situation, creates stakes through competition, and
aligns with students’ future career aspirations, all of which are
consistent with SDT’s emphasis onrelevanceas a driver of
autonomous motivation [13].
C. Game Mechanics
The application implements three distinct mechanic layers,
summarized in Table I. The pass economy creates a meaningful
trade-off. Using a pass for AI feedback improves the student’s
own draft, while using it to attack an opponent reduces a
competitor’s revision capacity. This trade-off is intended to
sustain competitive tension without making competition the
dominant strategy, because writing quality, after all, determines
the job offer. Additionally, the system includes an attack
validation rule requiring targets to retain at least one remaining
pass if no AI feedback passes have been used, guaranteeing all
participants at least one iterative AI feedback cycle regardless
of competitive interference. Importantly, the attack mechanic
only affects optional AI feedback opportunities and does not
influence human-assigned grades or assessment outcomes.
Fig. 1. The Brand War application interface.
D. AI Feedback and Scoring System
When a student submits a draft using a review pass,
the essay is evaluated by OpenAI GPT-4.1 using a rubric-
aligned prompt covering three dimensions, namelyContent
(relevance, narrative richness, use of the five narrative elements),
Mechanics(grammar, spelling, punctuation, sentence structure),
andStructure(organization, coherence, introduction–body–
conclusion flow). Each dimension is scored on a 0–100 scale,
and a composite average is computed and displayed to the
student alongside the dimensional breakdown. The rubric was
developed by the course instructor and was embedded directly
in the OpenAI GPT-4.1 prompt to ensure scoring alignment
with classroom expectations. Students receive their scores
immediately upon submission and may revise their essay before
using another pass.
It is important to note that this AI feedback is best
characterized asevaluative scaffoldingrather than full formative
feedback. Students receive scores and dimensional breakdowns
but not explicit revision suggestions. This design choice
preserves writing agency and prevents over-reliance on AI-
generated text, while still providing the diagnostic signal
students need to guide self-directed revision, consistent with
SRL theory’s emphasis on self-monitoring and self-evaluation
[14].
E. Engagement Tracking
The application logs all user interactions, including window
focus and blur events (via the browser Page Visibility API),
submission timestamps, and attack/shield activations. From
these logs, the platform computes student-level engagement
metrics includingfocus ratio(proportion of total task time
during which the essay input text box window was active),
number of focus sessions,total task duration, andpasses used
count. Fig. 1 shows the student-facing interface, with a resource
bar tracking remaining passes, attacks, and shields, a live word-
count essay editor targeting the 500-word limit, and a tabbed
review panel that returns dimensional AI feedback once a pass
is spent, keeping resource state, drafting progress, and feedback
visible together.

IV. METHODOLOGY
A. Participants
Participants were N= 29 university students enrolled in an
elective EFL writing course at a university in Taiwan. The class
represented a mix of majors. Two students did not submit a final
essay and are excluded from human-score analyses, yielding
n= 27 for those comparisons. One student had no focus-
event logs and is excluded from focus-ratio analyses ( n= 28).
Demographics were reported based on the 27 participants who
completed the final essay and post-survey (21 second-year, 2
fourth-year or above undergraduate students, and 2 graduate
students). Participants reported varied English proficiency based
on self-reported standardized test results. TOEIC was the
most common measure ( M= 824.31 , n= 16 ), and GEPT
respondents generally reported intermediate/high-intermediate
proficiency or above ( n= 12 ). Data were collected under
institutional research protocols during regular class hours as
part of the scheduled course activity.
B. Procedure
The session was conducted on March 17, 2026, and lasted
approximately 80 minutes, in five phases.
1) Game Introduction( ∼5 min). The instructor introduced
the scenario and rules (passes, attacks, shield, time limit).
2) Platform Onboarding( ∼5 min). Students logged in and
confirmed they understood the prompt and rubric.
3) Writing and Revision( ∼60 min). Students composed
their brand stories, optionally spending review passes for
OpenAI GPT-4.1 scoring and revising accordingly, or
using passes to attack opponents.
4) Final Submission. Students clicked “Submit Final Essay”
when satisfied or when time expired. Essays were graded
by the instructor using the same three-dimensional rubric
(Content, Mechanics, and Structure, each on a 0–100
scale) used by the AI system.
5) Debrief( ∼5 min). Brief class reflection on the writing
process and game experience.
C. Data Sources
Two datasets were extracted from the platform logs. The
review-level data( nreviews = 43submissions from 19 students)
record student ID, attempt number (1–5), and Content, Me-
chanics, and Structure scores plus the composite AI average.
Thestudent-level data( N= 29 ) record focus ratio, total task
duration, number of focus sessions, passes used, first and last
AI review scores, AI score gain, attack count, shield use, and
human final score.
D. Analysis
Analyses were conducted in Python using scipy.stats.
We report descriptive statistics for all key variables and the
trend in mean AI composite scores across attempts (1–5). We
use a Wilcoxon signed-rank test to compare first and final
reviewed submissions among students with at least two review
cycles, and a two-tailed Mann-Whitney U test to compare
human final scores between AI-feedback users ( n= 19) and
0 1 2 3 4 5
AI Feedback Passes Used
0
2
4
6
8
10
Number of Students
10
8
4 4
3
No AI feedback (0 passes)
Used AI feedback
Fig. 2. Distribution of AI feedback passes used per student.
non-users (n= 8). We also report Spearman correlations for
focus ratio versus human final score and for passes used versus
AI score gain, along with a Pearson correlation between AI last
review score and human final score as a convergent validity
check. Given the small sample ( N= 29 ) and single-session,
non-experimental design, all analyses are treated as exploratory,
with effect sizes emphasized alongsidep-values.
V. RESULTS
A. RQ1. Student Engagement Patterns
Of the 29 students, 19 (65.5%) used at least one AI review
pass, while 10 (34.5%) submitted without any AI feedback.
Fig. 2 shows pass usage was right-skewed. One pass was most
common (n= 8), usage tapered to n= 4 each at two and three
passes, and no student stopped at exactly four. The distribution
instead jumps directly to a smaller group that exhausted all
five ( n= 3 ). This gap suggests two usage patterns, a light-
touch majority sampling feedback once or twice, and a small
minority treating all five passes as an exhaustive revision loop.
Students were highly focused. Mean focus ratio was M=
0.824 (SD= 0.116 , range 0.56–1.00), and mean task duration
was M= 77.3 min ( SD= 5.0 ). Competitive mechanics were
used sparingly. Five students (17.2%) attacked an opponent’s
pass and none shielded, suggesting most students prioritized
writing over social interference even when the option was
available.
B. RQ2. Writing Performance Across AI Feedback Attempts
For students who used AI feedback ( n= 19), mean OpenAI
GPT-4.1 composite scores rose monotonically across attempts
(Fig. 3), climbing from M≈65.6 at Attempt 1 ( n= 19 ),
through ≈68 (Attempt 2, n= 11) and ≈75 (Attempt 3, n=
7), to ≈79 –81.3 by Attempts 4–5 ( n= 3 each). The steepest
gain falls between Attempts 2 and 3, and the shrinking error
bars at later attempts reflect both fewer remaining students and
less variable, higher-scoring drafts among those who persisted.
Mean AI score gain from first to last attempt was M= 3.7
(SD= 7.4 , range −5 to +22, n= 19 ). Among participants
completing at least two review cycles ( n= 11), scores were
significantly higher on the final than the first review, W= 8.5 ,
p=.032 (one-tailed), with a large effect size (rank-biserial
=.74 ). The three students who used all five cycles showed
the largest gains, while a few students saw minor decreases

1 2 3 4 5
Revision Attempt
0
25
50
75Mean AI Score
n = 19 n = 11 n = 7 n = 3 n = 3
Fig. 3. Mean AI composite scores (with standard deviation bars) by revision
attempt.
between consecutive attempts, likely reflecting natural variation
in AI scoring of near-equivalent drafts.
C. RQ3. AI Feedback, Human Scores, and Convergent Validity
Human final scores for AI-feedback users ( n= 19 , M=
76.9) were descriptively higher than for non-users ( n= 8 ,
M= 70.4 ), but the difference was not significant (Mann-
Whitney U= 102.5 , p=.167 , rank-biserial = 0.349), likely
reflecting the small sample and the lack of random assignment.
The Pearson correlation between students’ last AI review score
and their human final score was r= 0.722 (p < .001, n= 19),
a strong convergence between OpenAI GPT-4.1 rubric-based
scoring and the instructor’s holistic evaluation, and a key finding
supporting the validity of the AI feedback mechanism. Focus
ratio, meanwhile, showed no significant association with human
final score (Spearman ρ=−0.147 , p=.464 , n= 27), while
passes used showed a positive trend with AI score gain ( ρ=
0.428, p=.068 , n= 19) that did not reach α=.05 , likely due
to sample size. Students who attacked opponents ( Mhuman =
79.4) scored about the same as those who did not ( Mhuman =
74.1), suggesting attack behavior was not systematically tied
to writing quality.
Table II juxtaposes the four analytical results. The AI-
human correlation is far more reliable ( p < .001) than any
of the three engagement-related tests, none of which reach
α=.05 , showing that convergent validity, not engagement, is
this dataset’s strongest signal. Fig. 4 shows why. Focus ratio
and human score do not co-vary systematically. Top scores
(≥90 ) occur across the full focus range, including one student
at focus = 0.56, while several students above focus 0.9 scored
only in the low 60s. Non-users (grey) cluster at high focus
(0.85–1.0) but span nearly the entire score range ( 52–85), so
sustained on-screen attention alone did not guarantee a strong
final essay.
VI. DISCUSSION
A. AI Feedback as Evaluative Scaffolding
The monotonic increase in AI-assessed scores across revision
attempts, from M= 65.6 at Attempt 1 to M= 81.3 at At-
tempt 5 (Fig. 3), indicates that students responded productively
to the OpenAI GPT-4.1 scoring system. Viewed through a ZPD
lens [15], the AI functions as a “more knowledgeable other”
that externalizes performance standards, letting students close
the gap between their draft and the rubric’s expectations. This
operationalizes the monitor–evaluate–adjust loop central to SRL
TABLE II
SUMMARY OFKEYSTATISTICS
VariableM(SD) Range
Focus ratio0.824 (0.116) 0.56–1.00
Task duration (min)77.3 (5.0)–
Passes used –0–5
AI score gain3.7 (7.4)−5–+22
Human final score75.0 (13.1) 48–92
Analytical results
AIlast vs. Human (r)0.722***p < .001
Passes used vs. Gain (ρ)0.428†p=.068
Focus ratio vs. Human (ρ)−0.147p=.464
Users vs. Non-users (U)102.5p=.167
†p < .10, ***p < .001
0.6 0.7 0.8 0.9 1.0
Focus Ratio
40
50
60
70
80
90
100Human Final Score
 ρ = -0.147, p = 0.464
No AI feedback Used AI feedback
Fig. 4. Scatter plot of focus ratio vs. human final score.
theory [14] and aligns with multi-agent scaffolding frameworks
showing that constraints on AI access prompt metacognitive
monitoring and strategic resource allocation [16].
A key qualification is that the system providedevaluative
scaffolding, scores and dimensional breakdowns, rather than
fully elaborated formative feedback with explicit revision
suggestions. Students had to infer what to revise from scores
alone. This minimalist design helps prevent the technological
dependency observed when students use fully generative AI
tools [17], and the fact that scores nonetheless improved
suggests that even minimal feedback, embedded in a high-stakes
competitive frame, can motivate meaningful revision. Future
iterations could progressively fade from explicit feedback
toward scores-only as students approach their final revision,
consistent with fading scaffolding in ZPD-informed instruction.
The diminishing sample at higher attempts (n= 19 at Attempt 1
to n= 3 at Attempt 5, Fig. 3) also reflects self-selection, since
students who kept revising were likely more motivated or saw
more improvement potential, so this survivorship pattern should
temper how the later-attempt gains are interpreted.
B. Gamification, Engagement, and Self-Determination
The high mean focus ratio ( M= 0.824 ) indicates the game
context sustained behavioral engagement throughout the 60-
minute window, consistent with Zhihao and Zhonggen [3].
Under SDT [13], the competitive narrative likely satisfied

relatedness(social competition) andrelevance(career framing),
while the choice-based pass economy supportedautonomy.
A theoretically interesting finding is the asymmetry between
offensive mechanics (attack) and constructive mechanics (AI
feedback). Despite comparable cost, only 5 students (17.2%)
attacked and none shielded, whereas 19 (65.5%) used AI feed-
back (Fig. 2). SDT’scompetenceneed offers a parsimonious
explanation, since students appeared to favor mechanics that
improved their own ability over those that undermined others’,
consistent with Hajian et al.’s [18] argument that AI support
and scaffolding construct learner motivation. The competitive
frame appears to have generated motivational energy that
students channeled into writing rather than social interference,
a desirable outcome pedagogically. Future designs might tie
competitive mechanics directly to writing quality (e.g., attack
power scaling with AI score) so the two mechanics reinforce
rather than compete.
C. AI-Human Score Convergence
The strong correlation between AI last scores and human
final scores ( r= 0.722 , p < .001) evidences convergent
validity between OpenAI GPT-4.1-based scoring and the
instructor’s holistic evaluation (Table II). This does not indicate
perfect agreement, but supports AI scoring as a real-time
formative tool within the game while human scoring remains
appropriate for summative evaluation. The non-significant
group difference between AI-feedback users and non-users
(p=.167 ) should not be read as evidence of ineffectiveness.
The study was not powered to detect causal effects, and the
descriptive pattern (users M= 76.9 vs. non-users M= 70.4 )
is directionally consistent with a modest positive relationship.
VII. CONCLUSION
This paper introducedThe Brand War, a gamified web
application that embeds iterative OpenAI GPT-4.1-powered
writing feedback within a competitive narrative writing task
for undergraduate EFL learners. An exploratory single-session
study with N= 29 students in Taiwan found that nearly two-
thirds of students engaged with the AI feedback system, AI-
assessed scores rose monotonically across revision attempts, AI
and human scores converged strongly (r= 0.722), and students
maintained high task focus ( M= 82.4% ) while preferring
revision over competition even when competitive mechanics
were available. These findings suggest that integrating AI
evaluative scaffolding within a competitive game context is
pedagogically feasible and motivationally coherent for EFL
writing instruction, offering a practical deployment model that
requires no extensive instructor training or real-time feedback
provision. Limitations include the small, single-class sample
without a control condition, which limits generalizability and
precludes causal inference [19], the use of focus ratio as only
a behavioral proxy for engagement, and the evaluative rather
than fully formative nature of the AI feedback, whose inter-
rater reliability against a larger essay corpus remains to be
established. We would like to address these limitations in the
future work.
REFERENCES
[1] E. G ¨uvendir and K. Uzun, “L2 writing anxiety, working memory, and
task complexity in L2 written performance,”Journal of second language
writing, vol. 60, p. 101016, 2023.
[2] S. Deterdinget al., “From game design elements to gamefulness: defining
”gamification”,” inProceedings of the 15th international academic
MindTrek conference: Envisioning future media environments, 2011, pp.
9–15.
[3] Z. Zhihao and Y . Zhonggen, “The impact of gamification on the time-
limited writing performance of English majors,”Education Research
International, vol. 2022, no. 1, p. 4650166, 2022.
[4] K. Guoet al., “Applying game-related methods in the writing classroom:
A scoping review,”Education and Information Technologies, vol. 29,
no. 4, pp. 4481–4504, 2024.
[5] J. Steisset al., “Comparing the quality of human and ChatGPT feedback
of students’ writing,”Learning and Instruction, vol. 91, p. 101894, 2024.
[6] V . Linet al., “The effectiveness and learner acceptance of robot-facilitated
board games for enhancing content-based English vocabulary learning,”
Computer Assisted Language Learning, pp. 1–36, 2026.
[7] Y . Xiao, D. Li, and K. Guo, “Using ChatGPT to bring non-player
characters to life: Effects on students’ storyline-driven game-based writing
learning,”Computers & Education, p. 105414, 2025.
[8] C.-J. Linet al., “A flipped contextual game-based learning approach
to enhancing EFL students’ English business writing performance and
reflective behaviors,”Journal of Educational Technology & Society,
vol. 21, no. 3, pp. 117–131, 2018.
[9] L. K. Allenet al., “L2 writing practice: Game enjoyment as a key
to engagement,”Language, Learning and Technology, 2014. [Online].
Available: http://hdl.handle.net/10125/44373
[10] D. H. Changet al., “Educational design principles of using AI chatbot
that supports self-regulated learning in education: Goal setting, feedback,
and personalization,”Sustainability, vol. 15, no. 17, p. 12921, 2023.
[11] M. P.-C. Lin and D. Chang, “CHAT-ACTS: A pedagogical framework
for personalized chatbot to enhance active learning and self-regulated
learning,”Computers and Education: Artificial Intelligence, vol. 5, p.
100167, 2023.
[12] W. Huang and Y . Chen, “Design and evaluation of a gamified chat
generative pre-trained transformer-assisted English course learning system
with selfregulation support,” in2025 International Conference on
Intelligent Communication Networks and Computational Techniques
(ICICNCT). IEEE, 2025, pp. 1–6.
[13] E. L. Deci and R. M. Ryan, “The ”what” and ”why” of goal pursuits:
Human needs and the self-determination of behavior,”Psychological
inquiry, vol. 11, no. 4, pp. 227–268, 2000.
[14] B. J. Zimmerman, “Attaining self-regulation: A social cognitive perspec-
tive,” inHandbook of self-regulation. Elsevier, 2000, pp. 13–39.
[15] L. S. Vygotsky,Mind in society: Development of higher psychological
processes, M. Coleet al., Eds. Harvard university press, 1978.
[16] J. Ryooet al., “WIP: Multi-agent artificial intelligence model to enhance
self-regulated learning and conceptual understanding in computer science
education,” in2025 IEEE Frontiers in Education Conference (FIE).
IEEE, 2025, pp. 1–5.
[17] S. M. Parket al., “Evaluating the impact of assistive AI tools on learning
outcomes and ethical considerations in programming education,” in2025
IEEE Global Engineering Education Conference (EDUCON). IEEE,
2025, pp. 1–10.
[18] S. Hajianet al., “Motivational theories in action: A guide for teaching
artificial intelligence prompts to support student learning motivation,”
International Journal of Instruction, vol. 18, no. 4, pp. 601–626, 2025.
[19] V . Linet al., “The design and evaluation of a multimodal ubiquitous
learning application for EFL writers,”Digital Creativity, vol. 32, no. 2,
pp. 79–98, 2021.
