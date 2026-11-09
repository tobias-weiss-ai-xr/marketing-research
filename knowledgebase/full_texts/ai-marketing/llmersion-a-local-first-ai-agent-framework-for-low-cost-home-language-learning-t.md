---
title: 'LLMersion: A Local-First AI Agent Framework for Low-Cost Home Language Learning toward Educational
  Equity'
url: https://arxiv.org/abs/2609.29672
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Qiming Guo
- Jinwen Tang
- Xingran Huang
- Hung-Yu Lin
- Yafu Zhong
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.29672
pages: 24
chars: 99852
fetched_at: '2026-11-08T13:33:48+00:00'
kb_version: 1
---

# LLMersion: A Local-First AI Agent Framework for Low-Cost Home Language Learning toward Educational Equity

arXiv:2609.29672v2  [cs.CL]  2 Oct 2026
LLMersion: A Local-First AI Agent Framework for
Low-Cost Home Language Learning toward Educational Equity
Qiming Guo
Dept. of Computing Sciences
Texas A&M University–Corpus Christi
Corpus Christi, TX, USA
qguo2@islander.tamucc.edu
Jinwen Tang
Dept. of Electrical Engineering and Computer Science
University of Missouri
Columbia, MO, USA
jt4cc@umsystem.edu
Xingran Huang
Dept. of Computer Science and Engineering
University of California, Riverside
Riverside, CA, USA
xhuan230@ucr.edu
Hung-Yu Lin
Dept. of Computing Sciences
Texas A&M University–Corpus Christi
Corpus Christi, TX, USA
hlin5@islander.tamucc.edu
Yafu Zhong
Dept. of Mechanical and Aerospace Engineering
University of South Florida
Tampa, FL, USA
yafu@usf.edu
Xiatian Zhuang
Dept. of Civil and Environmental Engineering
University of Missouri
Columbia, MO, USA
xzrhb@umsystem.edu
Abstract
Artificial intelligence helps education most
where an essential provision has been rationed
by cost. For language learners that provi-
sion is a teacher’s voice, which binds listen-
ing, reading, speaking, and writing into one
act. Published evidence shows why most
learners lack it, from a global shortage of 44
million teachers to heavy household tutoring
bills, and why technology has not substituted
for it: computer-assisted language learning
proved effective but narrow, applications pre-
suppose connectivity 2.6 billion people lack,
and One Laptop per Child’s randomized eval-
uation found that hardware without capable
software teaches nothing. We distill eight dif-
ficulties and four binding constraints, and ar-
gue that small open-weight models dissolve
the last: a complete four-skill stack now fits
a $200-class laptop and, on community mea-
surements, generates at the pace speech is
consumed, for about one US cent of elec-
tricity per study hour. We therefore propose
LLMersion, a scheme for AI for education
that runs entirely at home, over the learner’s
own documents, with an AI-written, AI-
understood, AI-updated codebase anyone can
customize; present LLMersion-1, a released
open-source prototype (https://github.
com/QM378/LLMersion); and outline the
vision of a private learning agent.
Keywords:AI for education; educational equity;
second-language acquisition; computer-assisted
language learning; small language models; local-
first software.
1 Introduction
Where artificial intelligence helps education most
is not where instruction is already abundant, but
where an essential provision has been rationed by
cost. One-to-one guidance is the canonical exam-
ple: it is the most effective form of instruction we
can measure and, in Bloom’s words, “too costly
for most societies to bear on a large scale” (Bloom,
1984). This paper is about one sharply defined
piece of that rationed provision; about the tech-
nologies that have tried, for half a century, to sub-
stitute for it; and about a scheme, not merely a
system, for supplying it at the cost of electricity.
The piece in question is familiar to anyone who
learned English primarily through text. Many
learners read technical English fluently yet can-
not follow the same material by ear, and freeze
when asked to say its vocabulary aloud. The cause
is structural: solitary reading severs the sounds
of a language from its written form. A learner
alone with a book practices exactly one binding,
eyes to meaning, while the bindings that speech
requires, sound to text and articulation to sound,
are never exercised. In natural acquisition a person
supplies the missing link: a teacher reads the text

aloud, so the learner hears the words while seeing
them; models pronunciation, so new vocabulary
arrives with its spoken form; listens to the learner
speak, closing the loop from perception to produc-
tion; and corrects what the learner writes. Being
read to is itself a measurable engine of vocabu-
lary growth (Elley, 1989), and comprehensible in-
put drives acquisition generally (Krashen, 1985).
Learners with access to such a voice acquire listen-
ing, reading, speaking, and writing as one bound
skill; learners without it are left with text alone,
and their skill profile shows it.
That much has long been argued qualitatively.
The first half of this paper establishes its factual
scale from published evidence. The human provi-
sion is scarce at its source: the world needs 44
million additional teachers by 2030 (UNESCO,
2024), and in several major school systems the En-
glish teachers who do exist test below the profi-
ciency they are required to teach: more than half
of∼27,000 tested Indonesian teachers scored at
the lowest TOEIC band (Coleman, 2009). Where
a teacher is present, oral attention is diluted across
classes averaging 21 students in OECD primary
schools (OECD, 2025a) and larger elsewhere. The
consequence is stratification: fluent English car-
ries a 34% hourly wage premium for men in India
(Azam et al., 2013), and when China added a lis-
tening component to its college-entrance English
examination, the rural-urban gap in college ac-
cess widened by roughly 30%; the authors’ stated
mechanism is that listening and speaking skills re-
quire exactly the extracurricular resources disad-
vantaged students lack (Li et al., 2024). House-
holds answer by buying the provision privately:
private supplementary education reached 29.2 tril-
lion won in Korea in 2024 with English the lead-
ing subject (Statistics Korea and Ministry of Edu-
cation, Republic of Korea, 2025); tutoring house-
holds in China spent a mean of RMB 8,438 per
year in a nationally representative 2019 survey
(Wei, 2024); private coaching absorbs 11.8% of
Indian household education spending (National
Statistical Office, Ministry of Statistics and Pro-
gramme Implementation, Government of India,
2019); and 77% of Vietnamese upper-secondary
students attend private tutoring (Dang, 2007).
Prior technological approaches, examined next,
reveal an instructive contradiction. Computer-
assisted language learning is not ineffective; the
strongest meta-analysis finds it at least as effec-
tive as instruction without technology (Grgurovi ´c
et al., 2013). But it has been narrow: hand-
built tutoring systems shipped fixed lessons; au-
tomatic speech recognition, before deep learn-
ing, roughly doubled its error rate on non-native
speech, making oral feedback unreliable for pre-
cisely the learners who needed it (McCrocklin,
2026); commercial applications presuppose sub-
scriptions and connectivity that 2.6 billion peo-
ple do not have (International Telecommunica-
tion Union, 2024). The contradiction reaches its
clearest form in the One Laptop per Child pro-
gram: a randomized evaluation across 318 Pe-
ruvian schools raised computers per student ten-
fold and moved no mathematics or language score
(Cristia et al., 2017). Hardware was never the
missing ingredient; capable software running on
it was. Table 1 synthesizes the published evidence
into eight difficulties, the mechanism that sustains
each, the prior technological answer, and its limit.
What has changed, and what the second half
of this paper builds on, is that the missing soft-
ware has become small enough to own. Open-
weight language models of 1–3 billion parame-
ters occupy 0.8–2 GB quantized (hugging-quants
(Hugging Face), 2024), a complete synthesis–
recognition–translation stack adds under 2 GB
more (hexgrad, 2025), and community measure-
ments report generation at the pace speech and
text are consumed (Brysbaert, 2019) on hardware
as cheap as a $200-class laptop or an $80 single-
board computer (Raspberry Pi Ltd, 2023). At
the 2024 average US residential electricity price
(U.S. Energy Information Administration, 2025),
an hour of study on such a device costs on the
order of one US cent. The provision that Bloom
priced beyond societies’ reach can now, in this one
domain, be run at home.
We therefore propose LLMersion, ascheme
rather than only a system: (P1) a web interface
backed entirely by local, free, lowest-hardware-
cost models; (P2) the complete listening-reading-
speaking-writing loop, played in the teacher’s or-
der (read aloud to the learner, discuss what was
read, listen to the learner speak, correct what the
learner writes); (P3) the learner’s own documents
and self-built vocabulary as first-class input, not a
fixed curriculum; and (P4) a codebase that is AI-
written, AI-understood, and AI-updated, so that
customization does not require the professional
engineering that priced earlier tools out of reach.
We present LLMersion-1, a released open-source
reference instance implementing all four princi-

ples, together with a designed but not yet admin-
istered feedback instrument for future community
evaluation.
Our contributions: (1) an evidence-based anal-
ysis of learner needs, associated costs, and
prior technological approaches, distilled into a
reusable problem taxonomy (Table 1, Sections 2–
4); (2) an analysis identifying the four con-
straints that have bound low-cost, personalized,
equitable language education, and the evidence
that the last of them has newly dissolved (Sec-
tions 4–5); (3) a constraint-driven, local-first ed-
ucational agent architecture: four design princi-
ples, each answering one identified constraint, in-
cluding the AI-maintained-code principle (Sec-
tion 5); and (4) a released, continuously main-
tained reference instance (code:https://
github.com/QM378/LLMersion; compan-
ion narration tool:https://github.com/
QM378/llmersion-narrator, Section 6.6)
with a designed feedback instrument and pre-
stated expectations for future evaluation (Sec-
tion 6); the prototype remains under active devel-
opment, and as feedback data accumulates we will
continue to upgrade it and will report findings of
value.
Section 2 examines learner needs; Section 3 ex-
amines prior technological approaches and their
limitations; Section 4 distills the binding con-
straints; Section 5 states the scheme and its feasi-
bility; Section 6 describes the reference instance;
Section 7 discusses limitations and the outlook to-
ward a private learning agent; Section 8 concludes.
2 The Need: Second-Language
Acquisition under Resource Scarcity
This section establishes, from published evidence,
why the four-skill binding is out of reach for most
learners. We proceed from what the human pro-
vision does (Section 2.1), to the scarcity of that
provision at its source (Section 2.2), to the strati-
fication it produces (Section 2.3), to the skill pro-
file it leaves behind (Section 2.4), to what fami-
lies pay to compensate (Section 2.5), and finally to
why unassisted text study cannot substitute (Sec-
tion 2.6). Every quantitative claim below is traced
to a primary report or peer-reviewed study; where
only vendor or community figures exist, we say so
explicitly and attribute them.
2.1 What the Human Provision Does
One-to-one instruction remains the most effective
form of teaching we can measure: Bloom found
two-sigma gains under mastery tutoring (Bloom,
1984), and a meta-analysis of modern randomized
evaluations confirms tutoring among the most re-
liably effective educational interventions (Nickow
et al., 2020). For language in particular, the tutor’s
contribution is concrete and enumerable. First, the
voice: a teacher reads text aloud while the learner
sees it, and being read to is itself a measurable en-
gine of vocabulary growth (Elley, 1989), consis-
tent with the broader finding that comprehensible
input drives acquisition (Krashen, 1985). Read-
ing while listening, the self-administered form of
the same act, improves comprehension, reading
speed, and vocabulary retention across a sustained
line of classroom studies (Brown et al., 2008;
Chang, 2009, 2011; Chang and Millett, 2014,
2015), and a meta-analysis finds that glossing plus
aural support reliably aids incidental vocabulary
learning (Yanagisawa et al., 2020). Second, the
model: new vocabulary arrives with its spoken
form, so the learner’s phonological representation
is built at first contact rather than repaired later
(Nation, 2001). Third, the ear: the teacher listens
to the learner speak and corrects production, the
step shadowing research identifies as binding per-
ception to articulation (Kadota, 2019). Fourth, the
pen: the teacher corrects what the learner writes.
A learner with access to this provision exercises
all four bindings on the same material; a learner
without it exercises one.
2.2 Scarcity at the Source
The provision is scarce before any question of
quality arises. UNESCO’s 2024 global report
finds the world needs 44 million additional teach-
ers to reach universal primary and secondary edu-
cation by 2030, 15 million of them in sub-Saharan
Africa; closing the gap is costed at roughly $120
billion per year; and global primary-teacher attri-
tion nearly doubled between 2015 and 2022, from
4.62% to 9.06% (UNESCO, 2024). In the OECD’s
2024 teaching survey, the share of principals re-
porting that shortages of qualified teachers hinder
instruction rose again over 2018 levels (OECD,
2025b).
For English the shortage is compounded by a
second deficit: many of the teachers who do exist
cannot themselves model the language they must

Table 1: Eight difficulties of second-language acquisition under resource scarcity, the mechanism sustaining each,
technology’s prior answer, its documented limit, and this scheme’s response. Sections 2–4 develop each row with
sources.
Difficulty Why it persists Prior answer Its limit This scheme
Absolute teacher
scarcity
Demand outstrips trained
supply; attrition nearly
doubled 2015–2022 (UN-
ESCO, 2024)
Broadcast courses,
MOOCs, apps
Presuppose connectivity
2.6B people lack (Interna-
tional Telecommunication
Union, 2024)
The teacher’s four roles as
software on hardware al-
ready owned
Teachers’ own oral
proficiency
Teachers formed under
grammar/exam paradigms;
majorities test below
required levels (Coleman,
2009)
Broadcast native
audio
One-way; no feedback on
the learner
Synthesized model voice
over any chosen text
Individual speaking
time rationed
Classes of 21+ students;
teacher talk dominates
(OECD, 2025a)
ASR pronuncia-
tion drills
Pre-deep-learning ASR
∼doubled errors on L2
speech (McCrocklin,
2026)
Unlimited private spoken
turns with feedback
Method locked to
written exams
High-stakes tests reward
reading and grammar (Liu
and Ren, 2024)
Test-preparation
software
Reinforces the lock All four skills exercised
over the same document
Reading outruns
speech
Without oral input/output,
print decouples from
phonology (Costello et al.,
2021)
Audiobooks, sub-
titles
Fixed library; no interac-
tion with the learner’s ma-
terial
Read-aloud, then spo-
ken discussion, of the
learner’s own text
Proficiency tracks
wealth and geogra-
phy
Oral practice is bought
privately; +34% wage
premium in India (Azam
et al., 2013); listening
tests widened China’s
rural-urban gap (Li et al.,
2024)
Subscription appli-
cations
Recurring fees are a re-
gressive filter
One-time commodity
hardware; near-zero
marginal cost
Families pay heavily
for the gap
Shadow education: 29.2T
won in Korea (Statistics
Korea and Ministry of Ed-
ucation, Republic of Ko-
rea, 2025); RMB 8,438/yr
per tutoring household in
China (Wei, 2024)
Cheaper or
freemium apps
∼8% of monthly users
convert to paid (Duolingo,
Inc., 2025); content re-
mains fixed
Free, open weights; the
learner’s own materials
Cheap hardware
without capable
software
Distributing devices alone
moved no test score (ran-
domized evidence) (Cristia
et al., 2017)
Device-
distribution
programs
Hardware was never the
bottleneck
Small open models supply
the missing software lo-
cally
teach. In Indonesia, when roughly 27,000 teach-
ers in the country’s international-standard schools
took the TOEIC, more than half scored in the low-
est band of the 990-point scale and under one
percent reached professional working proficiency
(Coleman, 2009); a decade later, reviewers argu-
ing for a B2 minimum standard concluded the pic-
ture had not materially changed (Renandya et al.,
2018). Comparable below-benchmark proportions
have been reported for state English teachers else-
where in Southeast Asia (Renandya et al., 2018).
Even a proficient teacher cannot give what a
large class dissolves. Public primary classes aver-
age 21 students across the OECD (OECD, 2025a),
and are substantially larger in many of the sys-
tems where English carries the highest stakes. The
arithmetic is unforgiving and requires no study to
state: in a class of fifty, a full hour divided equally
into individual speaking turns yields barely a
minute per learner, before any teaching happens
in between. The one activity a tutor uniquely pro-
vides, listening to this learner speak and respond-
ing, is precisely the activity a classroom is least
able to ration out.
2.3 Stratification: Proficiency Tracks Wealth
and Geography
Because the oral provision must be bought where
schools cannot supply it, measured ability follows
money. In India, fluency in English carries a 34%
hourly wage premium for men relative to no En-
glish, and even partial English a 13% premium;

the return to fluency is comparable to that of com-
pleting secondary school (Azam et al., 2013). The
market prices exactly the skill the poor cannot
practice.
China offers an unusually clean identification
of the mechanism. A study in theJournal of
Development Economicsanalyzing administrative
records for 16 million college applicants exploits
the staggered introduction of a listening compo-
nent, worth 20% of the English subject score, into
the national college-entrance examination: rural
candidates’ English percentile ranks fell by about
two points, the rural-urban gap in college access
widened by roughly 30%, and the authors attribute
the effect to listening and speaking requiring ex-
tracurricular resources that disadvantaged students
lack (Li et al., 2024). A test of the bound skill,
added to an exam of the written one, converted a
resource gap directly into an admissions gap.
Cross-national proficiency indices tell a com-
patible story but must be handled with care: the
most-cited ranking, the EF English Proficiency In-
dex, is computed from millions of self-selected
online test takers and is explicitly not population-
representative (EF Education First, 2025); we
therefore use it for no quantitative claim in this pa-
per.
2.4 The Read-but-Cannot-Speak Profile
Where oral practice is scarce and examinations
are written, pedagogy adapts rationally, and the
adaptation leaves a signature. Studies of Chinese
university English teaching document the persis-
tence of grammar-translation and examination-
oriented practice and the difficulty of implement-
ing communicative and task-based approaches
against class sizes and test pressure (Liu and Ren,
2024). The equilibrium is self-reinforcing: high-
stakes written tests reward the skills that large
classes can drill, so reading and grammar advance
while listening and speaking wait; learners emerge
able to parse text they could never follow by ear.
The pattern is common enough across East Asian
systems to have earned vernacular names, and its
cause is structural rather than individual: it is the
expected output of instruction in which the sound
of the language is rarely heard and almost never
produced.
2.5 What Families Pay
Households do not accept the gap passively; they
buy the missing provision on a private market
whose scale is documented by official statistics
(Table 2). South Korea’s national survey puts
private supplementary education at 29.2 trillion
won in 2024, with 80% of students participating
and English the single largest subject at 248,000
won per month per participating student in 2023
(Statistics Korea and Ministry of Education, Re-
public of Korea, 2025). In China, a nationally rep-
resentative 2019 survey found tutoring households
spending a mean of RMB 8,438 per year (median
3,000), with participation at 31.4% in urban areas
against 14.1% in rural ones and 46.2% in first-
tier cities (Wei, 2024); the state judged the sec-
tor consequential enough to shut most of it down
by decree in 2021 (State Council of the People’s
Republic of China, 2021), closing over 90% of
private tutoring entities (Lyu and Lam, 2025), a
policy episode that confirms the scale of the de-
mand rather than eliminating it. In India, private
coaching absorbs 11.8% of household education
expenditure, and the national participation rate
rose to 27% by 2025 (National Statistical Office,
Ministry of Statistics and Programme Implemen-
tation, Government of India, 2019, 2025). In Viet-
nam, 31% of primary, 56% of lower-secondary,
and 77% of upper-secondary students attend pri-
vate tutoring (Dang, 2007). In Japan, the min-
istry of economy’s industry survey of English-
conversation schools, a top-firm sample covering
most of the market, annualizes to roughly ¥61 bil-
lion for 2024 (Ministry of Economy, Trade and
Industry, Japan, 2024). The pattern is global:
shadow education has been documented as a ma-
jor household expenditure across Asia, Africa, and
Europe (Bray, 2009; Bray and Lykins, 2012; Bray,
2021a,b). Whatever else these figures show, they
price the need: families worldwide pay substan-
tial, recurring, regressive sums for a provision that
is, at its core, a competent voice with time for one
learner.
2.6 Why Text-Only Self-Study Cannot
Compensate
The obvious zero-cost substitute, studying alone
from text, fails for a reason learning science
can state precisely. Language presented in
paired modalities is encoded through complemen-
tary verbal and imaginal channels (Paivio, 1986;
Mayer, 2009); the phonological loop of working
memory, rehearsing the sound of a new word, is
a core device of vocabulary learning (Baddeley
et al., 1998); and offering multiple, learner-chosen

Table 2: What families pay: one official or peer-reviewed anchor per country. Figures are for private supplementary
education; scope notes matter and are part of the claim.
Where Anchor (data year) Scope note
Korea 29.2T won total; English top subject at 248k
won/mo (2023–24) (Statistics Korea and Ministry
of Education, Republic of Korea, 2025)
Official national survey
China RMB 8,438/yr mean per tutoring household;
46.2% participation in first-tier cities (2019) (Wei,
2024)
Nationally representative survey; sector largely
closed by 2021 decree (State Council of the
People’s Republic of China, 2021; Lyu and
Lam, 2025)
India 11.8% of household education spending; participa-
tion 27% by 2025 (National Statistical Office, Min-
istry of Statistics and Programme Implementation,
Government of India, 2019, 2025)
Official NSS rounds; no per-subject breakdown
Vietnam 77% of upper-secondary students tutored (survey
era) (Dang, 2007)
Peer-reviewed household data
Japan≈¥61B/yr, conversation schools (2024) (Ministry
of Economy, Trade and Industry, Japan, 2024)
Ministry survey; top-firm sample, not full cen-
sus
modes of representation is a recognized principle
of accessible instructional design (CAST, 2018).
None of this rests on the contested claim that
learners should be matched to a fixed sensory
“style,” for which evidence is lacking (Pashler
et al., 2008); the point is that combined presen-
tation serves everyone, and a book supplies only
one mode.
Reading, moreover, does not smuggle the sound
in. Electrophysiological evidence shows that
skilled prelingually deaf readers recognize writ-
ten words without relying on phonological coding
at all (Costello et al., 2021): reading competence
can develop fully decoupled from sound. We cite
this as a mechanistic demonstration, not as a study
of hearing learners; but the implication for them
is direct. A learner who only ever reads English
can build a large orthographic and semantic vocab-
ulary while the phonological representations that
listening and speaking require are never formed,
or are formed privately and wrongly and then re-
hearsed. Text-only study does not merely progress
slowly toward the bound skill; it progresses con-
fidently away from it, which is why the profile of
Section 2.4 is stable. The missing ingredient is not
effort or material. It is a voice attached to the text,
and an ear attached to the learner.
3 Technology’s Compensations and
Their Contradictions
Technology has tried to substitute for the rationed
voice for half a century. The record is not one of
failure; it is one of narrowness, and the distinction
matters for what follows.
3.1 A Half-Century of Computer-Assisted
Language Learning
The standard periodization traces behavioristic
CALL (mainframe drill-and-practice), commu-
nicative CALL, and integrative CALL through
the 1960s to the 1990s (Warschauer and Healey,
1998), a framing later critiqued as chronologi-
cally loose but still the field’s reference map (Bax,
2003). Each generation moved closer to the tutor’s
role; none reached the voice-and-ear loop of Sec-
tion 2.1.
3.2 Effective, but Narrow
The honest starting point is a concession:
computer-assisted instruction worked. The
strongest meta-analysis of comparative studies
finds technology-supported language instruction
at least as effective as instruction without technol-
ogy, and superior in the most rigorously designed
studies (Grgurovi ´c et al., 2013). Any argument
that dismisses five decades of CALL as ineffec-
tive is contradicted by the evidence, and we do not
make it.
What the evidence does support is a claim about
the shape of that effectiveness. First, content was
fixed. Parser-based intelligent tutoring systems
required a hand-built lexicon, morphological an-
alyzer, parser, and error grammar per language;
the exemplary Japanese tutor ships one fixed se-
quence of twenty-four lessons for every user (Na-
gata, 2009), and porting the approach to a new
language was a multi-year research project in it-
self (Amaral and Meurers, 2011). No such system
could ingest the learner’s own documents. Second,

the speaking loop was unreliable exactly where
it was needed. Goodness-of-pronunciation scor-
ing (Witt and Young, 2000) depends on speech
recognition, and recognition degrades sharply on
the accented speech of learners: dictation sys-
tems transcribe native speakers at 90.25% accu-
racy but Chinese-L1 speakers at 72.45%, and their
accuracy does not correlate with human judgments
of intelligibility, so the tool cannot tell a learner
whether they would be understood (McCrocklin,
2026). Even a modern recognizer roughly triples
its word error rate between native and non-native
children’s read speech in benchmark comparisons
(Wills et al., 2023). A feedback channel that is
least accurate for its intended users cannot carry
the tutor’s ear.
3.3 The Application Era
Consumer applications scaled access dramatically
and inherited both limits. The flagship efficacy
study, commissioned by the vendor, estimated 34
hours of app study as equivalent in placement-
test gain to a first college semester, from a cohort
in which 156 participants began and 88 finished
(Vesselinov and Grego, 2012). Independent schol-
arship read the result narrowly: the study com-
pared the app to nothing (Krashen, 2014), an in-
dependent semester-long case study found high
attrition and gains concentrated among already-
committed learners (Loewen et al., 2019), and
the commercial-app efficacy literature as a whole
draws on a strikingly small circle of commissioned
authors (Jiang et al., 2021). None of this makes the
applications useless; it locates them. They deliver
fixed curricula well to learners who persist, and
the market leader’s own annual report shows how
the economics work: 116.7 million monthly users,
of whom 9.5 million, about 8%, pay (Duolingo,
Inc., 2025). The product that is free at the mar-
gin is not the tutor’s loop; the fuller product is a
subscription.
Language learning has now entered the LLM
era, and the early literature maps both the promise
and the boundary. Reviews of ChatGPT for lan-
guage teaching find genuine affordances for ex-
planation, text generation, and practice alongside
accuracy and pedagogy concerns (Kohnke et al.,
2023), classroom studies frame the model as a
complement to, not a substitute for, the teacher
(Jeon and Lee, 2023), and a systematic review of
speech-recognition chatbots argues that large lan-
guage models finally make open spoken practice
plausible, the very capability the pre-LLM assis-
tants of the previous generation delivered only in
constrained form (Jeon et al., 2023; Dizon, 2020).
What has not changed is the access model: ev-
ery deployed instantiation of this literature routes
through a metered cloud service, from ChatGPT
itself (OpenAI, 2023b) to the market leader’s pre-
mium tier built on a frontier model (Duolingo,
Inc., 2023). The pedagogy took the LLM turn;
the economics did not. Constraint C2 survives
the LLM era intact, which is precisely the gap the
scheme of Section 5 addresses by taking the LLM
turn local.
3.4 What Compensation Costs
Each compensation channel carries a recurring
price. Human oral practice online is sold by the
hour: major marketplaces list lessons from $4
and typically $4–40 per hour (italki, 2026; Preply,
2026), a real reduction on in-person tutoring that is
still a wage-indexed, per-hour cost. Frontier con-
versational AI, the first technology to offer some-
thing like open spoken interaction, is metered or
subscribed: the reference consumer tier costs $20
per month (OpenAI, 2023b), with inference served
from datacenters. For a learner in a high-income
country these are modest sums; against the income
distributions of Section 2.3 they reproduce exactly
the gradient the provision was supposed to flatten.
3.5 The Access Contradiction
All of the above presupposes connectivity, and the
presupposition excludes the population with the
most to gain. The ITU’s 2024 statistics count 2.6
billion people offline, a third of humanity, 1.8 bil-
lion of them rural; in low-income countries only
27% of people use the internet, and a fixed broad-
band subscription costs on the order of a third of
average monthly income (International Telecom-
munication Union, 2024). Even the device is a bar-
rier: an entry-level internet-capable handset costs
18% of average monthly income across low- and
middle-income countries, rising to 51% for the
poorest quintile (GSMA, 2024). “Free app” is a
description of a price, not of access.
3.6 The Contradiction’s Clearest Case: One
Laptop per Child
The era’s largest attempt to route around connec-
tivity and cost was to give out the hardware it-
self. The One Laptop per Child program dis-
tributed millions of purpose-built machines at

roughly $200 per unit; Peru alone deployed them
at national scale. The program received what ed-
ucational technology rarely gets, a large random-
ized evaluation: across 318 rural Peruvian schools,
the intervention raised computers per student from
0.12 to 1.18, and after fifteen months produced
no measurable effect on mathematics or language
test scores, alongside some positive but weaker ev-
idence on general cognitive skills (Cristia et al.,
2017); a companion randomized trial of home use
likewise found little academic impact (Beuermann
et al., 2015). The machines arrived; the outcomes
did not move.
We read this result carefully, because it is
the hinge of the paper. It does not show that
cheap hardware is useless; it shows that hardware
without capable software, software able to do a
teacher’s work rather than merely display content,
does not by itself teach. In 2012 no such soft-
ware could exist: nothing that fit in those machines
could read an arbitrary text aloud, converse about
it, hear the learner, or correct a sentence. The con-
straint was not the device. It was what the device
could run.
4 What Binds Low-Cost, Personalized,
Equitable Language Education
Sections 2 and 3 reduce to four constraints. Each
row of Table 1 is an instance of one of them.
C1: the human oral provision is intrinsically
expensive.It requires a proficient speaker’s ex-
clusive time, and both the proficiency and the time
are scarce: 44 million missing teachers, majorities
of tested teachers below the level they must teach,
and class arithmetic that dissolves individual at-
tention (rows 1–3). Every price in Section 2.5 is
this constraint expressed in currency.
C2: technological substitutes have presup-
posed connectivity and recurring payment.
Broadcast, apps, and cloud AI all meter access
through a subscription, a data plan, or both, re-
imposing the income gradient they were meant to
bypass (rows 6–7), and excluding the offline third
of humanity outright.
C3: substitute content has been fixed.Hand-
engineered lessons and app curricula cannot ingest
the learner’s own documents, vocabulary, or inter-
ests; the learner adapts to the material rather than
the material to the learner (rows 4–5, 7). This is
not a cosmetic limit: the need identified in Sec-
tion 2 is a voice attached tothe text the learner
must read, and a fixed library, however polished,
never contains it.
C4: capable software has never run on cheap
hardware.The one strategy that attacked cost and
connectivity directly, distributing devices, was de-
feated by this constraint alone: the machines could
not run anything that taught (Section 3.6, row 8).
The four constraints are not equally durable. C1
is a fact about humans and will not change. C2
and C3 are design choices, avoidable in principle
but economically stable as long as capable models
lived only in datacenters. C4 was, until recently,
a fact about software. The next section presents
the evidence that it no longer is, and a scheme
built on its dissolution: if a machine a family al-
ready owns can run software that performs the tu-
tor’s four roles over the learner’s own documents,
then C2 and C3 become unnecessary and C1 is by-
passed rather than solved.
5 The LLMersion Scheme: A Local AI
Agent for Home Language Acquisition
For readers outside artificial intelligence, we first
sketch, in three short stages, how the field arrived
at models a household machine can run; readers
who know this history can proceed to Section 5.4.
5.1 From Symbolic Rules to Statistical
Learning
Turing posed the founding question, whether ma-
chines can exhibit intelligent behavior, in 1950
(Turing, 1950). For the first decades the practical
answer was hand-written rules: experts encoded
knowledge as symbolic programs, and the parser-
based language tutors of Section 3 are exactly this
era’s classroom form, inheriting its economics, in
which every capability is authored by specialists.
Machine learning replaced authorship with train-
ing. Gradient-based learning of internal repre-
sentations (Rumelhart et al., 1986), convolutional
networks that read handwritten documents (Le-
Cun et al., 1998), support-vector machines (Cortes
and Vapnik, 1995), and random forests (Breiman,
2001) turned labeled data into behavior; but each
trained system still solved one narrow, fixed task.
5.2 Deep Learning Collapses Expert
Provisions
Deep networks scaled that recipe until breadth ap-
peared. The 2012 ImageNet result (Krizhevsky
et al., 2012) showed depth plus data beating

engineered features; residual connections made
very deep networks trainable (He et al., 2016);
recurrent memory handled sequences (Hochre-
iter and Schmidhuber, 1997); adversarial training
produced generative models (Goodfellow et al.,
2014). What followed was a series of cost col-
lapses in provisions once bound to scarce ex-
perts: champion-level Go (Silver et al., 2016),
dermatologist-level skin-cancer screening (Esteva
et al., 2017), protein-structure prediction (Jumper
et al., 2021), assistance in mathematical discovery
(Davies et al., 2021; Trinh et al., 2024), medium-
range weather forecasting (Lam et al., 2023),
materials design (Merchant et al., 2023), robust
speech recognition (Radford et al., 2023), and
applied systems from urban water-infrastructure
modeling (Guo and Wang, 2024) to small-object
detection in aerial imagery (Tang et al., 2025c).
Each collapse turned an expert service into soft-
ware; none of these systems yet conversed.
5.3 Large Language Models and Agents
The transformer architecture (Vaswani et al.,
2017) made language the next provision. Large-
scale pretraining (Devlin et al., 2019), few-shot
scaling (Brown et al., 2020), and instruction tun-
ing with human feedback (Ouyang et al., 2022)
produced systems that converse, explain, and cor-
rect. The frontier of this line is closed and me-
tered: GPT-4 (OpenAI, 2023a), Gemini (Gem-
ini Team, Google, 2023), and Claude (Anthropic,
2024) are reached by subscription over a net-
work, which is constraint C2 restated. What
matters for this paper is the parallel open line:
LLaMA (Touvron et al., 2023) began an open-
weight succession continued by Mistral (Jiang
et al., 2023), Qwen (Qwen Team, 2024), Gemma
(Gemma Team, 2024), Phi (Abdin et al., 2024), the
edge-sized Llama 3.2 family (Meta AI, 2024), and
the reasoning-focused DeepSeek-R1 (DeepSeek-
AI, 2025), models whose weights anyone may
download and run on their own machine. Cou-
pled with reasoning-and-acting and tool-use pat-
terns (Yao et al., 2023; Schick et al., 2023), such
models become agents: software that plans and
carries out multi-step work. Applications have
moved into expert services accordingly, including
clinical question answering (Singhal et al., 2023),
education (Kasneci et al., 2023), and spatio-
temporal signal prediction (Qin et al., 2025; Yan
et al., 2026); our own prior work follows the
same arc, with the SouLLMate systems for ac-
cessible, stigma-free mental-health support (Guo
et al., 2024a,b) and LLM-based mental-health pre-
screening (Tang and Shang, 2024), layered multi-
model reasoning for long-context mental-health
assessment (Tang et al., 2025a), a collaborative
MoE-LLM agent architecture for urban pipeline
monitoring (Guo et al., 2026a), conversational AI
tutoring with real-time knowledge tracing (RPKT)
(Tang et al., 2025b), and serving LLMs on low-
resource hardware, the deployment regime this pa-
per targets (Sun et al., 2025). The scheme below
spends this open, small, local tier of the technol-
ogy on the constraint analysis of Section 4.
5.4 Four Principles
P1: Web interface, fully local, lowest-cost mod-
els.The application is an ordinary browser inter-
face backed by a service on the same machine;
every model is free, open-weight, and chosen to
minimize hardware demand rather than maximize
benchmark scores. After a one-time download,
no network is required and nothing recurs. This
deletes C2: no subscription, no metering, no data
leaving the machine, and longevity independent
of any vendor. Keeping learner data on the de-
vice also avoids a problem that is costly to re-
pair afterwards: removing a person’s data from a
model after training, as privacy regulations such
as the GDPR and the CCPA may require, remains
an open research problem whose exact solutions
can approach the cost of full retraining (Guo et al.,
2026b,c); a design under which learner data never
reach a shared model avoids the problem rather
than solving it. Running the models on the device
is also what on-device machine learning is valued
for, keeping user data off the network; and be-
cause every model in the scheme is open-weight,
the model-extraction risk that a systematization of
on-device deployments documents for proprietary
models has nothing to take (Nayan et al., 2024).
P2: The complete four-skill loop, in the
teacher’s order.The software performs the enu-
merated roles of Section 2.1: it reads any text
aloud with the learner following (listening bound
to reading); discusses the text in spoken conver-
sation (listening bound to speaking); listens to
the learner and gives pronunciation and grammar
feedback (the ear); and corrects the learner’s writ-
ten retellings (the pen). The unit of study is the
same document throughout, so the four bindings
are exercised on shared material, which is what a
tutor does and what no fixed curriculum can.

P3: The learner’s own documents and vocab-
ulary are first-class.Input is whatever the learner
must actually read; the vocabulary store is built
from the learner’s own lookups and is deliberately
re-encountered across all four skills, in curated
reading, in conversation, and in writing feedback.
This deletes C3: the material adapts to the learner
because the materialisthe learner’s.
P4: AI-written, AI-understood, AI-updated.
The engineering cost that made intelligent CALL
expensive, per-language parsers and professional
maintenance (Section 3), is itself collapsing: the
same class of models that powers the tutor can
write and modify the software that hosts it. The
scheme therefore treats the codebase as an AI-
maintainable artifact: small legible modules, plug-
in registries with declarative capabilities, and be-
havior configured in editable prompt files rather
than compiled logic. Customization, adding a
voice, a language pair, a document format, or
a pedagogical behavior, becomes a conversation
with a model rather than a contract with a ven-
dor. Anyone able to describe a need can have the
system meet it; the reference instance of Section 6
was itself built and is maintained this way.
5.5 Feasibility on the Cheapest Hardware
The scheme stands or falls on a factual question:
can the machines that low-cost households and
schools actually have run these models? The ev-
idence, summarized in Table 3, is that they can,
with room to spare.
The stack fits.A 1B-parameter instruction-
following model occupies 808 MB at 4-bit quan-
tization and a 3B model 2.02 GB (hugging-quants
(Hugging Face), 2024); the 82M-parameter open
TTS voice weighs 327 MB (hexgrad, 2025); a
Whisper-class recognizer at the “small” size is un-
der half a gigabyte on disk, with community doc-
umentation reporting under 1 GB resident (Open-
Whispr, 2026; Radford et al., 2023); and compact
open translation models of the 77M class were
built precisely for real-time use on ordinary desk-
tops and small devices (Tiedemann and Thottin-
gal, 2020; Tiedemann et al., 2023; NLLB Team
et al., 2022). The complete four-skill stack totals
under 4 GB, inside the 8–16 GB of the cheapest
new laptops.
The models are capable enough.Current 1–
4B open models post solid instruction-following
and knowledge scores in their technical reports,
with the 3B class reporting MMLU in the low-to-
mid 60s and strong instruction-following bench-
marks (Meta AI, 2024; Gemma Team, 2024;
Qwen Team, 2024; Abdin et al., 2024); these are
not frontier systems, and the scheme does not need
them to be: the tutor’s roles here are reading, dis-
cussing a provided text, and correcting learner sen-
tences, tasks squarely within small-model range.
The models run at reading pace.No peer-
reviewed benchmark yet exists for LLM inference
on the cheapest CPUs, and we state throughput
only as attributed community measurement: re-
producible community tables report a 3B model at
roughly 4–9 tokens per second on an $80 single-
board computer and 5–15 tokens per second on
the entry laptop CPU class (Local AI Master,
2026; Shah, 2026; ggml-org/llama.cpp contribu-
tors, 2023). The yardstick is human reading itself:
silent reading averages 238 words per minute,
about four words per second (Brysbaert, 2019), so
even the measured floor delivers tutor text at the
pace a learner consumes it; synthesis, recognition,
and translation at the sizes above are lighter still.
The hardware floor is low and already
owned.New entry laptops with 16 GB of mem-
ory retail near $227 in current listings (a dated
snapshot, not a market average) (Walmart.com,
2026); the cheapest current Apple laptop launched
at $999, $899 for education, with 16 GB stan-
dard (Apple Inc., 2025); and an 8 GB single-board
computer lists at $80 (Raspberry Pi Ltd, 2023).
For households below even this floor, the relevant
comparison is Section 3: a device is a one-time
cost in a market where the alternative compensa-
tions recur monthly, and used business machines
circulate far below new prices.
The marginal cost is electricity.At the 2024
average US residential price of 16.5 cents per kWh
(U.S. Energy Information Administration, 2025),
a device drawing 15 W during study, the measured
envelope of entry CPUs under inference (Shah,
2026), costs about a quarter of one US cent per
study hour: one cent buys four hours. Taking a
generous 60 W full-laptop bound, the cost is still
about one cent per hour, and less wherever elec-
tricity is cheaper. After the device, the tutor’s
marginal price is the light bill.
This answers One Laptop per Child.The ran-
domized null result of Section 3.6 identified the
missing ingredient as capable software. That in-
gredient now exists, is free, is open-weight, and
fits the machines. Fitting the machines estab-
lishes feasibility, not efficacy: whether the soft-

Browser (local)listen·read·speak·write
V oice
TTS 82M
Ear
ASR small
Bilingual
MT 77M
Tutor
LLM 1–3B
Learner’s documents·self-built vocabulary·history
Figure 1: The scheme. Dashed nodes are replaceable open-weight models chosen for minimum hardware demand;
everything runs on the learner’s machine over the learner’s own material. An instance is described in Section 6.
Table 3: The complete four-skill stack against com-
modity memory. Sizes are published file or model-card
figures (hugging-quants (Hugging Face), 2024; hex-
grad, 2025; OpenWhispr, 2026; Tiedemann and Thot-
tingal, 2020; Walmart.com, 2026); the resident total
leaves headroom on an 8 GB device. Throughput on
the cheapest CPUs is community-measured (see text),
not peer-reviewed.
Component Params Size (Q4 / weights)
Tutor LLM 1B / 3B 0.81 / 2.02 GB
V oice (TTS) 82M 0.33 GB
Ear (ASR, “small”) 244M∼0.47 GB
Bilingual (MT) 77M∼0.30 GB
Whole stack (3B tutor)<4 GB
Cheapest new laptop memory 8–16 GB
ware teaches is a separate, measurable question,
and Section 6.10 equips the instance to ask it. The
scheme is the proposal to put the software there
and then measure.
6 A Reference Instance: LLMersion-1
LLMersion-1 is a released, open-source imple-
mentation of all four principles: a browser in-
terface backed by a local service that turns any
document into a synchronized listen-read-speak-
write session, plus an optional nightly curation
agent that keeps the reader supplied with person-
alized material. The two programs share only a
data folder; either runs without the other; both in-
stall with two commands on Windows, macOS, or
Linux, and touch the network only for one-time
model downloads and the curator’s public-source
fetches. This section describes the design; consis-
tent with the scope of this paper, we describe what
was built and how it embodies the scheme, and we
claim no learning outcomes.
6.1 Listening Bound to Reading
Documents (PDF, EPUB, HTML, Markdown,
text) pass through a loader registry that repairs lay-
out, recovers ligatures, and emits a typed para-
graph stream separating body prose from head-
ings, tables of contents, and formula debris. The
reader then plays the teacher’s first role: para-
graphs are synthesized as whole units, so the voice
carries the connected-speech phenomena, link-
ing, reduction, boundary intonation, that reading-
while- listening and shadowing practice depend
on (Brown et al., 2008; Kadota, 2019); sentence
boundaries are recovered from the synthesized
waveform so a highlighter tracks the spoken sen-
tence as the learner reads along. A translation
registry renders each paragraph into the learner’s
first language beneath the original, scheduled so
the sentences nearest the reading head arrive first.
Selecting any word snaps to word boundaries, re-
solves inflection to the dictionary head, shows IPA
and bilingual glosses, speaks the word, and files
it, dated and with its source sentence, into a self-
building vocabulary that feeds a flashcard mode;
each card can be spoken by the system or pro-
nounced by the learner for scoring.
Figure 2 shows a reading session in progress.
6.2 The Ear: Segmental Pronunciation
Feedback
Following the goodness-of-pronunciation tradi-
tion (Witt and Young, 2000), LLMersion-1 scores
a learner’s recording by transcribing it with a
phoneme-level CTC model (Baevski et al., 2020;
Xu et al., 2021) and aligning the result against a
reference phoneme sequence, reporting the spe-
cific substitutions, omissions, and insertions. The
reference sequence is obtained by transcribing
the synthesized reference audio with the same
model rather than from a pronunciation dictio-
nary, so both sequences share one symbol in-

Figure 2: The LLMersion-1 reader during a read-along session, as seen by a Chinese-speaking learner of English.
Interface labels are in the learner’s first language. From left to right the toolbar reads: open file; voice (here the
Kokoro voice “Heart”, General American); playback speed; reading mode (whole paragraph); Chinese translation
on or off; vocabulary book, with one saved word; writing practice; conversation; and a light or dark theme switch.
The English paragraph is the text being read aloud, and the yellow band marks the current reading position as the
voice proceeds. The grey text beneath it is a machine translation of the same paragraph into Simplified Chinese, so
the learner can check comprehension without leaving the page. The bar at the bottom holds the playback controls
and the position in the document.
ventory and one model bias and no grapheme-
to-phoneme component is required. Because the
reference voice is a synthetic American English,
the aligner folds a conservative set of allophone
classes (flap and stop realizations of /t/, central-
vowel variants, rhotic notation) before counting
errors, so accent-level differences are not scored
as mistakes. The feedback is deliberately segmen-
tal: it reports whether the sounds were produced,
not how native the prosody was, and the interface
says so.
6.3 Speaking: Conversation over What Was
Read
The conversation module closes the loop the needs
analysis identified as most rationed: someone to
talk to about the text. A session opens in one
of three grounding modes, free talk, a learner-
chosen topic, or the document currently open in
the reader, with document grounding following
the reading position. Interaction is push-to-talk:
the learner holds a key to speak and can inter-
rupt the tutor at any time, a deliberate choice over
voice-activity detection for robustness on cheap
microphones. Speech is recognized locally by a
Whisper-class model (Radford et al., 2023), with
an interim transcription refreshed while the learner
is still speaking so words appear as they are said.
After recognition, three independent jobs run in
parallel so a turn costs the slowest of them rather
than their sum: the tutor’s reply (generated by
the local LLM and spoken by the same voice
as the reader, with sentence-synchronized cap-
tions); a grammar-coach pass that returns a cor-
rection card, the learner’s sentence with changes
marked and a one-sentence explanation of the rule
in the learner’s first language, instructed to ig-
nore the repetitions and restarts that are normal
in speech; and the segmental pronunciation scorer
above. The tutor is prompted to deliberately reuse
words from the learner’s vocabulary store; a word
strip marks each stored word first when the tutor
uses it and again, fully, when the learner speaks
it, making the third re-encounter channel (heard,
then said) visible.
Two design honesty notes belong in the paper
rather than a footnote. First, in free conversa-
tion the pronunciation reference is derived from
the recognizer’s transcript of the learner’s own ut-
terance; this catches distorted sounds but cannot
catch a word so mispronounced that the recognizer

heard a different word, a limit the flashcard path
(where the target word is known) does not share.
Second, the grammar coach operates on the tran-
script, not the audio, so it corrects what was rec-
ognized, not what was said. Both limits are stated
in the interface.
Figure 3(a) shows the opening screen of a con-
versation session.
6.4 The Pen: Writing Practice
After studying a section, the learner retells it in
English in a writing panel; the local model re-
turns a corrected version with changes marked,
brief notes on the few most instructive errors,
and a vocabulary check: which of the learner’s
saved words appeared in the draft, and one more
that would fit, the productive counterpart of the
re-encounters above. A per-paragraph control
rewrites any hard paragraph at an easier register,
technical terms kept and glossed.
Figure 3(b) shows the writing panel.
6.5 Supply: The Night Curator
The remaining tutor cost, choosing what to study
next, is paid by an optional second program while
the machine is idle. One invocation is one night: it
fetches candidate texts from open sources on top-
ics the learner has rated well, ranks them partly
by how densely they re-encounter the learner’s
saved vocabulary, rewrites them for read-aloud de-
livery with the local model (verbalizing notation,
smoothing citation debris), and writes ordinary
Markdown files the reader picks up. Preference
signals are explicit ratings when given and implicit
read-completion otherwise, with explicit always
overriding implicit. The curator is strictly decou-
pled: it reads the reader’s store read-only, keeps its
own state, and deleting it removes a convenience,
never a capability.
6.6 A Companion Tool: LLMersion Narrator
The listening role is also released as a stan-
dalone companion program, LLMersion Nar-
rator (https://github.com/QM378/
llmersion-narrator), for learners who
want results they can keep and replay away from
the computer. It reuses the reader’s paragraph-
level synthesis and its waveform-derived sentence
timing: the learner pastes English text, opens a
file, or opens a whole folder, and receives for
each text a narrated MP3, a read-along MP4 in
which the spoken sentence is highlighted, and
a PDF of the text, optionally repeated back to
back up to 20 times. Like the reader it runs
locally, and a Windows build that requires no
Python installation is distributed with the release.
Figure 4 shows the input page and a frame of the
generated video.
6.7 AI-Built, AI-Maintained in Practice
Principle P4 is not aspirational in the instance; it
is how the system exists. The codebase was writ-
ten, debugged, and extended in AI-assisted ses-
sions, and its architecture is shaped for that work-
flow: every substitutable component, voices, rec-
ognizers, translators, dictionaries, document load-
ers, is a registry of small plug-in files sharing one
declared interface, so adding a capability is one
legible file that a model can write and a main-
tainer can read; pedagogical behavior, the tutor’s
persona, the coach’s correction policy, the cura-
tor’s rewriting style, lives in editable prompt files
rather than code. The practical consequence is the
one the scheme promises: a user who wants a new
voice, another language pair, or a stricter grammar
coach can describe the change to a model, in their
own language, and apply the resulting file, without
the professional engineering that priced the parser
era (Section 3) out of individual reach. We present
this as a design principle with an existence proof,
not as a quantified engineering result; measuring
its maintenance economics is future work.
Figure 5 shows the voice registry as the learner
sees it.
6.8 Positioning and Resource Profile
Table 4 places the instance among the tool cate-
gories available to an individual learner; Table 5
lists the default resident components, which sum
well inside the memory of the hardware floor of
Section 5.5, with an optional larger-LLM tier for
workstation users.
6.9 Deployment Arithmetic: Memory, Pace,
and Five-Year Cost
The scheme-level feasibility evidence of Sec-
tion 5.5 can be instantiated for LLMersion-1’s ac-
tual component set as three derivations. Every in-
put below is a cited figure; the arithmetic is ours
and is stated so a reader can recompute it.
Memory.Summing Table 5 for the worst case,
all components resident at once during a scored
conversation turn: voice (∼0.4 GB) + transla-
tion (∼0.3 GB) + recognizer at the “small” size

(a) Conversation (b) Writing practice
Figure 3: The speaking and writing modules (interface text in Chinese, the learner’s first language). (a) The
conversation module before a session. The heading reads “Before you speak, choose a starting point” and the
line below it, “Whichever you choose, the tutor will deliberately use words from your vocabulary book, and every
sentence you say will get pronunciation feedback and corrections along the way.” The three options are free talk,
a chosen topic, and talk about this document, followed by a start button. The strip labelled “your words” holds
endowed, the word the learner saved while reading the paragraph of Figure 2, now carried into conversation. At the
bottom are the push-to-talk button and a text box whose placeholder reads “If you can’t say it, type it; press Enter
to send.” (b) The writing panel. The header reads “Writing practice: after reading a section, retell or summarize it
in English; the local LLM corrects it and checks whether you used your vocabulary words.” The button below the
text box submits the draft for correction.
(a) Input page (b) A frame of the read-along MP4
Figure 4: LLMersion Narrator, the companion tool of Section 6.6; its interface is in English. (a) The input page:
the learner pastes text (or uses the “Open a file” and “Open a folder” tabs for batch work), chooses an accent, voice,
speed, and number of repetitions, selects the outputs (MP3 audio, MP4 read-along video, PDF of the text), and
presses “Read it aloud”. (b) A frame of the generated video in its light style: the sentence currently being spoken
is highlighted, and the title and paragraph counter run along the top.
Table 4: Feature comparison with the tool categories available to an individual learner. Entries are design properties
drawn from public product documentation, not measured outcomes; interactive spoken feedback from a human
tutor remains the quality benchmark.
Commercial Cloud LLM PDF LLMersion-1
lang. app chat reader (+curator)
Learner’s own documents rarely paste-in✓ ✓
Synchronized read-while-listen fixed library — —✓
Inline translation✓ ✓—✓
In-context vocabulary capture✓— limited✓
Spoken conversation on own documents scripted cloud tiers — local
Pronunciation feedback scripted drills text advice — segmental
Works offline — —✓ ✓
Open source, models replaceable — — varies✓
Recurring service cost subscription metered none none
(∼0.9 GB) + phoneme scorer (∼1.2 GB) + a 3B
tutor at 4-bit quantization (2.02 GB) + parsing, in-
terface, and cache (<0.2 GB)≈5.0 GB; Table 3’s
sub-4 GB figure is the scheme’s minimal four-skill
stack, and the instance’s optional phoneme scorer
accounts for the difference. With a 1B tutor the

Figure 5: The voice and model panel of LLMersion-1, an example of the plug-in registries of Section 6.7 (Chi-
nese labels translated here). The header reads “V oices and models”, followed by the number of speech engines
currently usable and the folder scanned for cloned voices; the buttons on the right rescan for engines and free GPU
memory. The text box holds a sentence from the open document, and the button beside it plays that sentence in
every checked voice for side-by-side comparison. On this machine only the Kokoro engine (tagged “local”) is
installed, with American and British voices. The greyed cards below are the other registered engines: Chatterbox
(tagged “clonable”, “local”, and “speed handled by the front end”), Piper (“local”), Edge neural (“online”), and
the operating system’s voice (“local”); each shows, in English, the one-line installation step that would enable it.
Table 5: Default resident components of the reference
instance (hexgrad, 2025; Tiedemann and Thottingal,
2020; Radford et al., 2023; Xu et al., 2021; hugging-
quants (Hugging Face), 2024).
Component Params Memory
TTS (Kokoro) 82M∼0.4 GB
MT (opus-mt-en-zh) 77M∼0.3 GB
ASR (Whisper base/small) 74–244M 0.3–0.9 GB
Phoneme CTC 0.3B∼1.2 GB
Tutor LLM (quantized) 1–4B 0.8–2.5 GB
Parsing, UI, cache —<0.2 GB
Optional: larger local LLM 4–27B 3–17 GB
same sum is≈3.8 GB. Against the 16 GB of the
current entry-laptop configuration (Walmart.com,
2026; Apple Inc., 2025) this leaves a majority of
memory to the operating system and the learner’s
other work; against an 8 GB device (Raspberry
Pi Ltd, 2023) the 1B configuration runs com-
fortably and the 3B configuration fits with the
phoneme scorer loaded on demand, which is how
LLMersion-1 already treats it. No configuration
requires hardware beyond the floor devices of Sec-
tion 5.5.
Pace.How fast must the tutor generate for ed-
ucation to work? The requirement can be derived
from measured human rates rather than asserted.
Adults read silently at 238 words per minute and
listen to oral delivery at 183 words per minute
(Brysbaert, 2019), that is, 3.97 and 3.05 words
per second; at the commonly documented ratio
of roughly 0.75 English words per model token
(OpenAI, 2024), these correspond to about 5.3 and
4.1 tokens per second. The binding constraint for
LLMersion-1 is the oral one: the tutor’s reply is
consumed as speech, so generation need only out-
run 4.1 tokens per second. Community measure-
ments report a 3B model at 4–9 tokens per sec-
ond on the $80 single-board floor and 5–15 on the
entry laptop class (Local AI Master, 2026; Shah,
2026): the floor meets the oral requirement and
the entry laptop clears the silent-reading one. The
same inputs bound the turn latency honestly: a
typical forty-word spoken reply is roughly 53 to-
kens, implying about 13 seconds of generation
at the floor rate before synthesis begins, halving
on the entry-laptop class; this is why the tutor is
prompted toward short conversational turns, and
why the three post-recognition jobs run in parallel
(Section 6.3) rather than in sequence.
Cost.Table 6 derives the five-year cost of
one hour of daily practice througheach chan-
nel examined in the cost analysis, native curren-
cies preserved so no exchange-rate assumption is
needed. The scheme’s recurring term is electric-
ity alone:1,825hours at a generous 60 W and
the 2024 average US residential rate of 16.5 cents
per kWh (U.S. Energy Information Administra-

Table 6: Five-year cost of one hour of daily prac-
tice, derived from cited prices (Walmart.com, 2026;
U.S. Energy Information Administration, 2025; Ope-
nAI, 2023b; italki, 2026; Statistics Korea and Ministry
of Education, Republic of Korea, 2025; Wei, 2024).
Native currencies preserved; the device row is a dated
retail snapshot, not a market average.
Channel 5 years Basis
LLMersion-1, new floor
laptop
≈$245 $227 device + $18
electricity
LLMersion-1, owned de-
vice
≈$18 electricity, 60 W
Cloud LLM subscription $1,200 $20/month
Tutoring, 1 h/week $2,600 $10/h floor
Korea, English tutoring 14.9M won 248k won/month
China, tutoring house-
hold
RMB 42,190 RMB 8,438/year
tion, 2025) is about $18; adding the dated $227
floor-laptop snapshot (Walmart.com, 2026) yields
roughly $245 all-in, and a household that already
owns any capable machine pays only the $18. Ev-
ery alternative channel costs more per year than
the scheme costs per five years, and the human
channels cost more per month: the average Ko-
rean per-student spend on English tutoring alone
(Statistics Korea and Ministry of Education, Re-
public of Korea, 2025) exceeds the scheme’s five-
year electricity total many times over in any recent
currency terms. The comparison is not that the al-
ternatives are bad; Section 3 concedes they work.
It is that their price re-imposes the gradient of Sec-
tion 2.3, and the scheme’s does not.
6.10 A Designed Feedback Instrument
The instance ships with the means of its own fu-
ture evaluation, and we state plainly that it is de-
signed, not yet administered: no learning out-
come is claimed in this paper. A 20-item self-
report instrument (Table 7, Appendix A) covers
reading fluency, listening, speaking and pronun-
ciation, vocabulary, and integrated workflow on
a uniform 0–4 scale, with an optional four-item
module for curator users; it is meant for longitu-
dinal self-comparison after the first session, one
week, one month, and one year. A conversa-
tional administration, in which a language model
adapts follow-up questions within the session, is
a natural later variant (Tang and Shang, 2025);
the fixed form is kept here so that responses re-
main comparable across timepoints. Alongside
self-report, the system logs objective traces lo-
cally, reading throughput, pronunciation-score tra-
jectories, vocabulary growth, curator completion
signals, which a respondent can attach voluntar-
ily. These traces are collected to operate the sys-
tem, not designed as comparative evidence, and
data gathered for operational monitoring are not
automatically valid evaluation data (Lin et al.,
2026b); they enter evaluation only as pre-declared
endpoints of a study designed for that purpose.
Collection is designed against pre-stated expec-
tations rather than mined afterwards: rising sub-
scale means across timepoints (H1); agreement
between the speaking subscale and logged pronun-
ciation trajectories (H2), between the vocabulary
subscale and logged list growth (H3), and between
curator ratings and implicit completion (H4); and
whether the re-encounter density of a curated pick
predicts its rating and completion (H5). Establish-
ing any of these, and any causal claim about learn-
ing, requires the controlled study we leave as fu-
ture work; the instrument and the logged measures
define its endpoints in advance.
7 Limitations and Outlook: Toward the
Private Learning Agent
The limits of this paper are the limits of a proposal.
We claim no learning outcomes: the published
evidence establishes the need and the feasibility
evidence establishes that the software runs, but
whether the scheme teaches is exactly the question
the designed instrument of Section 6.10 exists to
ask, and it has not yet been administered. Several
feasibility inputs are honest ranges rather than set-
tled facts: throughput on the cheapest CPUs rests
on attributed community measurement, not peer
review, and retail prices are dated snapshots. End-
to-end conversational latency, power draw, and
thermal behavior on floor hardware are likewise
unmeasured; the deployment arithmetic of Sec-
tion 6.9 bounds the first from cited inputs but mea-
sures none of them, and token throughput alone
does not equal usable tutoring latency. The in-
stance has its own stated edges: pronunciation
feedback is segmental only and, in free conver-
sation, references the recognizer’s transcript of
the learner’s own speech, so a wholly misrecog-
nized word escapes scoring; grammar correction
operates on transcripts, not audio; the resident tu-
tor is a small model, with a small model’s occa-
sional lapses in instruction following; the system
is single-user; and the dictionary is the last compo-

nent specific to the English-Chinese pair, though
the voice, recognition, translation, and scoring
registries are already language-agnostic.
The outlook is the scheme’s name taken liter-
ally: a private learning agent. The instance already
contains the parts of one, a curator that chooses
material overnight from the learner’s signals, a tu-
tor that discusses it by voice, a coach that cor-
rects production, and P4 makes the whole assem-
bly user-modifiable; what remains is their auton-
omy and reach. Concretely: difficulty modeling
beyond vocabulary overlap, so curation sequences
documents rather than merely selecting them; ad-
ditional language pairs, which in the current ar-
chitecture means principally a dictionary; richer
prosodic feedback for shadowing; pooling what
many learners’ installations learn without pooling
their data, the setting personalized federated learn-
ing addresses for heterogeneous and imbalanced
clients (Xu et al., 2022); and the controlled study,
pairing the instrument of Section 6.10 with the ob-
jective traces the system already logs, that would
convert this proposal’s pre-stated expectations into
evidence. The direction of travel is guided by the
identified constraints: every capability added must
continue to run on the machines people already
have, or it re-imposes the constraints this scheme
exists to delete.
A further horizon is embodiment. A decade of
research on social robots for education finds that
physical presence contributes what no screen does,
joint attention, gesture, and sustained engagement,
while noting that cost has kept such tutors out of
ordinary homes (Belpaeme et al., 2018); mean-
while embodied foundation models are folding
language, perception, and action into single sys-
tems (Driess et al., 2023). The scheme is built to
meet that line: LLMersion-1’s four-skill loop lives
behind a browser and a set of model registries, so
an embodied host would replace the screen, not
the stack, and the tutor that reads, converses, lis-
tens, and corrects could inhabit whatever low-cost
embodied platforms eventually reach households.
Experience with the most visible embodied de-
ployment of AI, automated driving, suggests that
the effect of such systems depends less on the sin-
gle machine than on how it is integrated with the
infrastructure around it (Lin et al., 2026a); for a
home tutor, that infrastructure is the household’s
existing devices. The low-power processors such
platforms rely on are themselves an active line
of open, reproducible design work (Huang et al.,
2026). The same affordability constraint applies
to embodiment: embodiment enters the scheme
when, and only when, it runs on hardware fami-
lies can own.
8 Conclusion
The binding of listening, reading, speaking, and
writing has always been available to learners with
someone to read to them, talk with them, and
correct them; the analysis in this paper docu-
mented what everyone else pays, in tutoring bills,
in widened admission gaps, in a skill profile that
reads but cannot speak. Technology’s earlier com-
pensations were real but narrow, and the one pro-
gram that put hardware directly into children’s
hands showed, under randomized evaluation, that
hardware alone teaches nothing: the missing in-
gredient was software able to do a teacher’s work.
That ingredient now fits in two gigabytes and gen-
erates at the pace speech is consumed, on ma-
chines sold for the price of a month of tutoring. We
have proposed a scheme for spending that fact on
educational equity, four principles: local and free,
the whole four-skill loop, the learner’s own mate-
rial, and a codebase its users can reshape through
AI, and released LLMersion-1 as a working in-
stance. The provision Bloom priced beyond soci-
eties’ reach is not beyond a household’s anymore;
what remains is to put it in homes, and to measure
what it does there.
References
Marah Abdin et al. 2024. Phi-3 technical re-
port: A highly capable language model locally
on your phone. Technical report, Microsoft.
ArXiv:2404.14219. Phi-3-mini 3.8B MMLU 68.8.
Accessed 2026-08-29.
Luiz A. Amaral and Detmar Meurers. 2011. On us-
ing intelligent computer-assisted language learning
in real-life foreign language teaching and learning.
ReCALL, 23(1):4–24.
Anthropic. 2024. The Claude 3 model family: Opus,
sonnet, haiku. Model card, Anthropic. Accessed
2026-08-29.
Apple Inc. 2025. Apple introduces the new MacBook
Air with the M4 chip and a sky blue color. Apple
Newsroom, 5 March 2025. $999 / $899 education;
16 GB starting unified memory. Accessed 2026-08-
29.
Mehtabul Azam, Aimee Chin, and Nishith Prakash.
2013. The returns to English-language skills in In-
dia.Economic Development and Cultural Change,

61(2):335–367. IHDS 2005; fluent English +34%
male hourly wages; a little +13%. Accessed 2026-
08-29.
Alan Baddeley, Susan Gathercole, and Costanza Pa-
pagno. 1998. The phonological loop as a language
learning device.Psychological Review, 105(1):158–
173.
Alexei Baevski, Yuhao Zhou, Abdelrahman Mohamed,
and Michael Auli. 2020. wav2vec 2.0: A frame-
work for self-supervised learning of speech repre-
sentations. InAdvances in Neural Information Pro-
cessing Systems (NeurIPS), volume 33.
Stephen Bax. 2003. CALL — past, present and future.
System, 31(1):13–28. Critique of the Warschauer–
Healey periodization; cite alongside it. Accessed
2026-08-29.
Tony Belpaeme, James Kennedy, Aditi Ramachan-
dran, Brian Scassellati, and Fumihide Tanaka. 2018.
Social robots for education: A review.Science
Robotics, 3(21):eaat5954.
Diether W. Beuermann, Julián Cristia, Santiago Cueto,
Ofer Malamud, and Yyannú Cruz-Aguayo. 2015.
One laptop per child at home: Short-term impacts
from a randomized experiment in Peru.American
Economic Journal: Applied Economics, 7(2):53–80.
Accessed 2026-08-29.
Benjamin S. Bloom. 1984. The 2 sigma problem: The
search for methods of group instruction as effec-
tive as one-to-one tutoring.Educational Researcher,
13(6):4–16.
Mark Bray. 2009.Confronting the Shadow Education
System: What Government Policies for What Private
Tutoring?UNESCO International Institute for Edu-
cational Planning, Paris, France.
Mark Bray. 2021a.Shadow Education in Africa: Pri-
vate Supplementary Tutoring and Its Policy Impli-
cations. Comparative Education Research Centre,
University of Hong Kong / UNESCO, Hong Kong.
Accessed 2026-08-29.
Mark Bray. 2021b. Shadow education in Europe:
Growing prevalence, underlying forces, and pol-
icy implications.ECNU Review of Education,
4(3):442–475. !! confirm volume/issue/pages
against the journal record. Accessed 2026-08-29.
Mark Bray and Chad Lykins. 2012.Shadow Educa-
tion: Private Supplementary Tutoring and Its Im-
plications for Policy Makers in Asia. Asian De-
velopment Bank and Comparative Education Re-
search Centre, University of Hong Kong, Mandaluy-
ong City. Accessed 2026-08-29.
Leo Breiman. 2001. Random forests.Machine Learn-
ing, 45(1):5–32.
Ronan Brown, Rob Waring, and Sangrawee Donkaew-
bua. 2008. Incidental vocabulary acquisition from
reading, reading-while-listening, and listening to
stories.Reading in a Foreign Language, 20(2):136–
163.
Tom B. Brown et al. 2020. Language models are few-
shot learners. InAdvances in Neural Information
Processing Systems (NeurIPS), volume 33.
Marc Brysbaert. 2019. How many words do we
read per minute? A review and meta-analysis of
reading rate.Journal of Memory and Language,
109:104047. Silent 238 wpm (non-fiction), 260 (fic-
tion), oral 183. Accessed 2026-08-29.
CAST. 2018. Universal design for learning guide-
lines, version 2.2.https://udlguidelines.
cast.org.
Anna C.-S. Chang. 2009. Gains to L2 listeners from
reading while listening vs. listening only in compre-
hending short stories.System, 37(4):652–663.
Anna C.-S. Chang. 2011. The effect of reading while
listening to audiobooks: Listening fluency and vo-
cabulary gain.Asian Journal of English Language
Teaching, 21:43–64.
Anna C.-S. Chang and Sonia Millett. 2014. The effect
of extensive listening on developing L2 listening flu-
ency: Some hard evidence.ELT Journal, 68(1):31–
40.
Anna C.-S. Chang and Sonia Millett. 2015. Im-
proving reading rates and comprehension through
audio-assisted extensive reading for beginner learn-
ers.System, 52:91–102.
Hywel Coleman. 2009. Indonesia’s ‘international stan-
dard schools’: What are they for? In8th Language
and Development Conference, Dhaka. 27,000 RSBI
teachers took TOEIC; >50% novice (10–250/990);
0.7% advanced+. Accessed 2026-08-29.
Corinna Cortes and Vladimir Vapnik. 1995. Support-
vector networks.Machine Learning, 20(3):273–
297.
Brendan Costello, Sendy Caffarra, Noemi Fariña,
Jon Andoni Duñabeitia, and Manuel Carreiras.
2021. Reading without phonology: ERP evidence
from skilled deaf readers of Spanish.Scientific
Reports, 11:5202. Verified against journal record
2026-08-29.
Julián Cristia, Pablo Ibarrarán, Santiago Cueto, Ana
Santiago, and Eugenio Severín. 2017. Technol-
ogy and child development: Evidence from the
one laptop per child program.American Eco-
nomic Journal: Applied Economics, 9(3):295–320.
RCT, 318 rural Peruvian schools; computers/student
0.12→1.18; no math/language test-score effect.
Load-bearing citation. Accessed 2026-08-29.

Hai-Anh Dang. 2007. The determinants and impact of
private tutoring classes in Vietnam.Economics of
Education Review, 26(6):683–698.
Alex Davies et al. 2021. Advancing mathematics by
guiding human intuition with AI.Nature, 600:70–
74.
DeepSeek-AI. 2025. DeepSeek-R1: Incentiviz-
ing reasoning capability in LLMs via reinforce-
ment learning. Technical report, DeepSeek.
ArXiv:2501.12948.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019. BERT: Pre-training of
deep bidirectional transformers for language under-
standing. InProc. NAACL-HLT, pages 4171–4186.
Gilbert Dizon. 2020. Evaluating intelligent personal
assistants for L2 listening and speaking develop-
ment.Language Learning & Technology, 24(1):16–
26.
Danny Driess, Fei Xia, Mehdi S. M. Sajjadi, et al. 2023.
PaLM-E: An embodied multimodal language model.
Technical report, Google. ArXiv:2303.03378;
ICML 2023.
Duolingo, Inc. 2023. Introducing Duolingo Max, a
learning experience powered by GPT-4. Duolingo
blog. Conversation features routed through a me-
tered frontier model. Accessed 2026-08-29.
Duolingo, Inc. 2025. Form 10-K for fiscal year ended
december 31, 2024. U.S. Securities and Exchange
Commission. 40.5M DAU, 116.7M MAU, 9.5M
paid subscribers (Q4 2024). Accessed 2026-08-29.
EF Education First. 2025. EF english proficiency index
2025: About / methodology. EF Education First.
2.2M self-selected online test-takers, 123 countries.
Cite ONLY with the self-selection caveat. Accessed
2026-08-29.
Warwick B. Elley. 1989. V ocabulary acquisition from
listening to stories.Reading Research Quarterly,
24(2):174–187.
Andre Esteva et al. 2017. Dermatologist-level classi-
fication of skin cancer with deep neural networks.
Nature, 542:115–118.
Gemini Team, Google. 2023. Gemini: A family of
highly capable multimodal models. Technical re-
port, Google. ArXiv:2312.11805.
Gemma Team. 2024. Gemma 2: Improving open lan-
guage models at a practical size. Technical report,
Google DeepMind. ArXiv:2408.00118. Accessed
2026-08-29.
ggml-org/llama.cpp contributors. 2023. Performance
of llama.cpp on Apple Silicon M-series. GitHub
Discussion #4167. (b) Maintainer benchmark ta-
bles, reproducible methodology. Accessed 2026-08-
29.
Ian Goodfellow, Jean Pouget-Abadie, Mehdi Mirza,
Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron
Courville, and Yoshua Bengio. 2014. Generative ad-
versarial nets. InAdvances in Neural Information
Processing Systems 27.
Maja Grgurovi´c, Carol A. Chapelle, and Mack C. Shel-
ley. 2013. A meta-analysis of effectiveness studies
on computer technology-supported language learn-
ing.ReCALL, 25(2):165–198. CALL at least as
effective as non-CALL; cite BEFORE critiquing
scope. Accessed 2026-08-29.
GSMA. 2024. The state of mobile internet connectiv-
ity 2024. Technical report, GSMA, London. Entry
handset = 18% of avg monthly income in LMICs;
51% for poorest quintile; up to 99% in Sub-Saharan
Africa. Accessed 2026-08-29.
Qiming Guo, Bishal Khatri, Wenbo Sun, Jinwen Tang,
Hua Zhang, and Wenlu Wang. 2026a. AquaSen-
tinel: Next-generation AI system integrating sen-
sor networks for urban underground water pipeline
anomaly detection via collaborative MoE-LLM
agent architecture. InProceedings of the AAAI Con-
ference on Artificial Intelligence, volume 40, pages
40265–40271.
Qiming Guo, Wenbo Sun, Chen Pan, Ye Wang, and
Wenlu Wang. 2026b. Unlearning on spatio-temporal
graphs through subgraph virtual edge reconstruc-
tion.arXiv preprint arXiv:2608.29369.
Qiming Guo, Wenbo Sun, Ye Wang, and Wenlu
Wang. 2026c. Spatial entropy based partitioning
for spatiotemporal graph unlearning.arXiv preprint
arXiv:2608.29360.
Qiming Guo, Jinwen Tang, Wenbo Sun, Haoteng
Tang, Yi Shang, and Wenlu Wang. 2024a. SouLL-
Mate: An adaptive LLM-driven system for ad-
vanced mental health support and assessment, based
on a systematic application survey.arXiv preprint
arXiv:2410.11859.
Qiming Guo, Jinwen Tang, Wenbo Sun, Haoteng Tang,
Yi Shang, and Wenlu Wang. 2024b. SouLLMate:
An application enhancing diverse mental health sup-
port with adaptive LLMs, prompt engineering, and
RAG techniques.arXiv preprint arXiv:2410.16322.
Qiming Guo and Wenlu Wang. 2024. HydroNet: A
spatio-temporal graph neural network for model-
ing hydraulic dependencies in urban wastewater sys-
tems. InProceedings of the 32nd ACM International
Conference on Advances in Geographic Information
Systems, pages 717–718.
Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian
Sun. 2016. Deep residual learning for image recog-
nition. InProc. IEEE Conference on Computer Vi-
sion and Pattern Recognition (CVPR), pages 770–
778.
hexgrad. 2025. Kokoro-82M model card. Hugging
Face. 82M params, Apache-2.0, weights 327 MB,
24 kHz. Accessed 2026-08-29.

Sepp Hochreiter and Jürgen Schmidhuber. 1997.
Long short-term memory.Neural Computation,
9(8):1735–1780.
Xingran Huang, Qiming Guo, Jinwen Tang, Wenqi Jia,
and Dongzheng Wang. 2026. Clock-gating inser-
tion strategies on an open-source MSP430 core: A
reproducible PPA study and a gate-level simulation
caveat.arXiv preprint arXiv:2608.30954.
hugging-quants (Hugging Face). 2024. Llama-3.2-
1B/3B-Instruct-Q4_K_M-GGUF model files. 1B
Q4 = 808 MB; 3B Q4 = 2.02 GB (file listings). Ac-
cessed 2026-08-29.
International Telecommunication Union. 2024. Mea-
suring digital development: Facts and figures 2024.
Technical report, ITU, Geneva. 2.6B offline (32%);
low-income countries 27% online; fixed broadband
≈1/3 of avg monthly income there. Accessed 2026-
08-29.
italki. 2026. How much does italki cost? pric-
ing guide.https://www.italki.com/en/
blog/italki-price. Lessons from $4; typical
$4–25 per session (marketplace self-reported range).
Accessed 2026-08-29.
Jaeho Jeon and Seongyong Lee. 2023. Large lan-
guage models in education: A focus on the comple-
mentary relationship between human teachers and
ChatGPT.Education and Information Technolo-
gies, 28(12):15873–15892.
Jaeho Jeon, Seongyong Lee, and Hansol Choe. 2023.
Beyond ChatGPT: A conceptual framework and
systematic review of speech-recognition chatbots
for language learning.Computers & Education,
206:104898.
Albert Q. Jiang, Alexandre Sablayrolles, Arthur Men-
sch, et al. 2023. Mistral 7B. Technical report, Mis-
tral AI. ArXiv:2310.06825.
Xiangying Jiang, Joseph Rollinson, Luke Plonsky, Erin
Gustafson, and Bozena Pajak. 2021. Evaluating
the reading and listening outcomes of beginning-
level Duolingo courses.Foreign Language Annals,
54(4):974–1002. !! Duolingo-affiliated authors;
cite as company-funded outcome study AND as ev-
idence of author concentration. Accessed 2026-08-
29.
John Jumper et al. 2021. Highly accurate protein struc-
ture prediction with AlphaFold.Nature, 596:583–
589.
Shuhei Kadota. 2019.Shadowing as a Practice in Sec-
ond Language Acquisition: Connecting Inputs and
Outputs. Routledge, London, U.K.
Enkelejda Kasneci et al. 2023. ChatGPT for good? On
opportunities and challenges of large language mod-
els for education.Learning and Individual Differ-
ences, 103:102274.
Lucas Kohnke, Benjamin Luke Moorhouse, and
Di Zou. 2023. ChatGPT for language teaching and
learning.RELC Journal, 54(2):537–550.
Stephen Krashen. 1985.The Input Hypothesis: Issues
and Implications. Longman, London, U.K.
Stephen Krashen. 2014. Does Duolingo “trump”
university-level language learning?The Inter-
national Journal of Foreign Language Teaching,
9(1):13–15.
Alex Krizhevsky, Ilya Sutskever, and Geoffrey E. Hin-
ton. 2012. ImageNet classification with deep con-
volutional neural networks. InAdvances in Neu-
ral Information Processing Systems (NeurIPS), vol-
ume 25.
Remi Lam et al. 2023. Learning skillful medium-range
global weather forecasting.Science, 382:1416–
1421.
Yann LeCun, Léon Bottou, Yoshua Bengio, and Patrick
Haffner. 1998. Gradient-based learning applied to
document recognition.Proceedings of the IEEE,
86(11):2278–2324.
Hongbin Li, Lingsheng Meng, Kai Mu, and Shaoda
Wang. 2024. English language requirement and ed-
ucational inequality: Evidence from 16 million col-
lege applicants in China.Journal of Development
Economics. Published version of NBER WP 32162.
!! confirm volume/article number against the journal
record before submission.
Hung-Yu Lin, Xingran Huang, Qiming Guo, and Jin-
wen Tang. 2026a. Connected autonomous mobility
in the United States: A narrative review of trans-
portation, urban, economic, environmental, and gov-
ernance implications.Engineering Archive.
Hung-Yu Lin, Xingran Huang, Qiming Guo, and
Jinwen Tang. 2026b. When compliance data
masquerades as evaluation: Measurement valid-
ity for deployed AI systems.arXiv preprint
arXiv:2609.13642.
Yuying Liu and Wei Ren. 2024. Task-based language
teaching in a local EFL context: Chinese university
teachers’ beliefs and practices.Language Teach-
ing Research. Grammar-translation legacy; weak
CLT implementation under exam pressure. Accessed
2026-08-29.
Local AI Master. 2026. Raspberry Pi 5 LLM bench-
marks: 12 models, real tokens/sec. (b) Community:
Llama 3.2 3B 8.8 tok/s on Pi 5. Accessed 2026-08-
29.
Shawn Loewen, Dustin Crowther, Daniel R. Isbell,
Kathy Minhye Kim, Jeffrey Maloney, Zachary F.
Miller, and Hima Rawal. 2019. Mobile-assisted lan-
guage learning: A Duolingo case study.ReCALL,
31(3):293–311.

Min Lyu and Ricky Lam. 2025. Private english tutors’
agency amid china’s ‘double reduction’ policy: A
bourdieusian perspective.Journal of Education Pol-
icy, 40(4):667–688. Reports over 90% of private tu-
toring entities shut down under the 2021 policy. Ver-
ified against publisher record 2026-08-29.
Richard E. Mayer. 2009.Multimedia Learning, 2nd
edition. Cambridge University Press, Cambridge,
U.K.
Shannon McCrocklin. 2026. ASR-dictation accu-
racy for second language speech: Programs, tasks,
and language backgrounds.Human Behavior and
Emerging Technologies. Native 90.25% vs Chinese-
L1 72.45%; accuracy uncorrelated with human intel-
ligibility judgments. !! confirm volume/pages when
assigned. Accessed 2026-08-29.
Amil Merchant et al. 2023. Scaling deep learning for
materials discovery.Nature, 624:80–85.
Meta AI. 2024. Llama 3.2: Revolutionizing edge AI
and vision with open, customizable models. 3B:
MMLU 63.4, IFEval 77.4. Accessed 2026-08-29.
Ministry of Economy, Trade and Industry, Japan. 2024.
Survey of selected service industries (dynamics):
Foreign-language conversation schools. Technical
report, METI. 2024 annualized≈¥61.1B, top-firm
sample (∼70% of market); survey discontinued after
Dec 2024. e-Stat dataset 00550050. Accessed 2026-
08-29.
Noriko Nagata. 2009. Robo-sensei’s NLP-based error
detection and feedback generation.CALICO Jour-
nal, 26(3):562–579.
I. S. P. Nation. 2001.Learning Vocabulary in An-
other Language. Cambridge University Press, Cam-
bridge, U.K.
National Statistical Office, Ministry of Statistics and
Programme Implementation, Government of India.
2019. Household social consumption on education
in india: NSS 75th round (july 2017–june 2018),
report no. 585. Technical report, MoSPI. Private
coaching = 11.8% of household education expendi-
ture. Accessed 2026-08-29.
National Statistical Office, Ministry of Statistics and
Programme Implementation, Government of India.
2025. Comprehensive modular survey: Education,
2025 (NSS 80th round). Technical report, MoSPI.
Private-coaching incidence 27.0% (rural 25.5%, ur-
ban 30.7%). Accessed 2026-08-29.
Tushar Nayan, Qiming Guo, Mohammed Al Duniawi,
Marcus Botacin, Selcuk Uluagac, and Ruimin Sun.
2024. SoK: All you need to know about On-Device
ML model extraction - the gap between research
and practice. In33rd USENIX Security Symposium
(USENIX Security 24), pages 5233–5250.
Andre Nickow, Philip Oreopoulos, and Vincent Quan.
2020. The impressive effects of tutoring on PreK–12
learning: A systematic review and meta-analysis of
the experimental evidence. Technical Report Work-
ing Paper 27476, National Bureau of Economic Re-
search.
NLLB Team et al. 2022. No language left behind:
Scaling human-centered machine translation.arXiv
preprint arXiv:2207.04672.
OECD. 2025a. Education at a glance 2025: OECD in-
dicators. Technical report, OECD Publishing, Paris.
Avg public-primary class 21; student-teacher 14:1
primary. Accessed 2026-08-29.
OECD. 2025b. Teaching for today’s world: Results
from TALIS 2024. Technical report, OECD Pub-
lishing, Paris. Principal-reported qualified-teacher
shortages rising vs 2018. Accessed 2026-08-29.
OpenAI. 2023a. GPT-4 technical report. Technical re-
port, OpenAI. ArXiv:2303.08774.
OpenAI. 2023b. Introducing ChatGPT Plus.https:
//openai.com/index/chatgpt-plus/.
US$20/month. Accessed 2026-08-29.
OpenAI. 2024. What are tokens and how to count
them? OpenAI Help Center. Vendor documen-
tation: roughly 0.75 English words per token. Ac-
cessed 2026-08-29.
OpenWhispr. 2026. Whisper model sizes explained.
(b) small: GGML 466 MiB,∼852 MB RAM. Ac-
cessed 2026-08-29.
Long Ouyang et al. 2022. Training language mod-
els to follow instructions with human feedback. In
Advances in Neural Information Processing Systems
(NeurIPS), volume 35.
Allan Paivio. 1986.Mental Representations: A Dual
Coding Approach. Oxford University Press, New
York, NY .
Harold Pashler, Mark McDaniel, Doug Rohrer, and
Robert Bjork. 2008. Learning styles: Concepts and
evidence.Psychological Science in the Public Inter-
est, 9(3):105–119.
Preply. 2026. Tutor pricing.https://preply.
com. Most tutors $10–40 per hour (marketplace
self-reported range). Accessed 2026-08-29.
Dayu Qin, Yi Yan, and Ercan Engin Kuruoglu. 2025.
LLM-based online prediction of time-varying graph
signals (student abstract). InProceedings of the
AAAI Conference on Artificial Intelligence, vol-
ume 39, pages 29472–29474.
Qwen Team. 2024. Qwen2.5 technical report. Tech-
nical report, Alibaba. ArXiv:2412.15115. Accessed
2026-08-29.

Alec Radford et al. 2023. Robust speech recognition
via large-scale weak supervision. InProc. Interna-
tional Conference on Machine Learning (ICML).
Raspberry Pi Ltd. 2023. Introducing: Raspberry Pi
5! raspberrypi.com news. $60 (4 GB) / $80 (8
GB) launch pricing. 2026 DRAM-driven rises doc-
umented as temporary in the 2026 news post. Ac-
cessed 2026-08-29.
Willy A. Renandya, Fuad A. Hamied, and Joko
Nurkamto. 2018. English language proficiency in
Indonesia: Issues and prospects.The Journal of
AsiaTEFL, 15(3):618–629. Review quoting Cole-
man (2009); B2 minimum-standard argument. Au-
thor names verified: Hamied & Nurkamto. Accessed
2026-08-29.
David E. Rumelhart, Geoffrey E. Hinton, and Ronald J.
Williams. 1986. Learning representations by back-
propagating errors.Nature, 323:533–536.
Timo Schick, Jane Dwivedi-Yu, Roberto Dessì,
Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer,
Nicola Cancedda, and Thomas Scialom. 2023. Tool-
former: Language models can teach themselves to
use tools. InAdvances in Neural Information Pro-
cessing Systems 36.
Bishal Kumar Shah. 2026. Running Ollama on Intel
N100 & N150 mini PC. (b) Community measure-
ment: Llama 3.2 3B Q4∼5–15 tok/s, 12–18 W. Ac-
cessed 2026-08-29.
David Silver et al. 2016. Mastering the game of Go
with deep neural networks and tree search.Nature,
529:484–489.
Karan Singhal et al. 2023. Large language models en-
code clinical knowledge.Nature, 620:172–180.
State Council of the People’s Republic of China. 2021.
Opinions on further reducing the homework bur-
den and off-campus training burden of students in
compulsory education. Policy document (“Dou-
ble Reduction”), 24 July 2021. Core-subject (incl.
English) tutoring to non-profit; capital barred. Ac-
cessed 2026-08-29.
Statistics Korea and Ministry of Education, Republic
of Korea. 2025. Private education expenditures sur-
vey of elementary, middle and high school students
in 2024. Statistics Korea press release. 29.2 tril-
lion won total (2024); participation 80.0%; English
top subject (2023: 248,000 won/month). Accessed
2026-08-29.
Wenbo Sun, Qiming Guo, Wenlu Wang, and Rihan Hai.
2025. TranSQL+: Serving large language models
with SQL on low-resource hardware.Proceedings
of the ACM on Management of Data, 3(6):1–27.
Jinwen Tang, Qiming Guo, Wenbo Sun, and Yi Shang.
2025a. A layered multi-expert framework for long-
context mental health assessments. In2025 IEEE
Conference on Artificial Intelligence (CAI), pages
435–440. IEEE.
Jinwen Tang, Qiming Guo, Zhicheng Tang, and
Yi Shang. 2025b. RPKT: Learning what you don’t
know–recursive prerequisite knowledge tracing in
conversational AI tutors for personalized learning.
In2025 IEEE International Conference on Fu-
ture Machine Learning and Data Science (FMLDS),
pages 133–138. IEEE.
Jinwen Tang and Yi Shang. 2024. Advancing mental
health pre-screening: A new custom GPT for psy-
chological distress assessment. In2024 IEEE 6th
international conference on cognitive machine intel-
ligence (CogMI), pages 162–171. IEEE.
Jinwen Tang and Yi Shang. 2025. AURA: A
reinforcement learning framework for AI-driven
adaptive conversational surveys.arXiv preprint
arXiv:2510.27126.
Zhicheng Tang, Jinwen Tang, and Yi Shang. 2025c. A
data-driven RetinaNet model for small object detec-
tion in aerial images. In2025 IEEE International
Conference on Future Machine Learning and Data
Science (FMLDS), pages 233–238. IEEE.
Jörg Tiedemann, Mikko Aulamo, Daria Bakshandaeva,
Michele Boggia, Stig-Arne Grönroos, Tommi Niem-
inen, Alessandro Raganato, Yves Scherrer, Raul
Vazquez, and Sami Virpioja. 2023. Democratizing
neural machine translation with OPUS-MT.Lan-
guage Resources and Evaluation, 58:713–755. !!
confirm volume/pages against the journal record.
Real-time compact MT on small devices. Accessed
2026-08-29.
Jörg Tiedemann and Santhosh Thottingal. 2020.
OPUS-MT: Building open translation services for
the world. InProc. 22nd Annual Conference of
the European Association for Machine Translation
(EAMT), pages 479–480.
Hugo Touvron, Thibaut Lavril, Gautier Izacard, et al.
2023. LLaMA: Open and efficient foundation
language models. Technical report, Meta AI.
ArXiv:2302.13971.
Trieu H. Trinh et al. 2024. Solving olympiad geometry
without human demonstrations.Nature, 625:476–
482.
Alan M. Turing. 1950. Computing machinery and in-
telligence.Mind, 59(236):433–460.
UNESCO. 2024. Global report on teachers: Address-
ing teacher shortages and transforming the profes-
sion. Technical report, UNESCO, Paris. 44M teach-
ers needed by 2030; SSA 15M; primary attrition
4.62% (2015) to 9.06% (2022). Accessed 2026-08-
29.
U.S. Energy Information Administration. 2025. Today
in energy: Residential electricity prices. US avg res-
idential 16.0 (2023)→16.5 cents/kWh (2024). Ac-
cessed 2026-08-29.

Ashish Vaswani et al. 2017. Attention is all you need.
InAdvances in Neural Information Processing Sys-
tems (NeurIPS), volume 30.
Roumen Vesselinov and John Grego. 2012. Duolingo
effectiveness study: Final report. Technical re-
port, City University of New York, Queens Col-
lege. Company-commissioned, not peer-reviewed;
34h (CI 26–49)≈one college semester; 156 started
/ 88 completed. Accessed 2026-08-29.
Walmart.com. 2026. 15.6-inch FHD laptop, Intel
N100, 16 gb RAM, 512 gb SSD (retail listing).
(b) Price snapshot $226.99, accessed 2026-08-29;
volatile, attribute with date.
Mark Warschauer and Deborah Healey. 1998. Comput-
ers and language learning: An overview.Language
Teaching, 31(2):57–71.
Yi Wei. 2024. Household expenditure on educa-
tion in China: Key findings from the China In-
stitute for Educational Finance Research-household
surveys (CIEFR-HS).ECNU Review of Educa-
tion, 7(3):738–761. 2019 wave, 34,643 households:
tutoring households mean RMB 8,438/yr (median
3,000); participation 24.4%, first-tier cities 46.2%.
Accessed 2026-08-29.
Simone Wills, Yu Bai, Cristian Tejedor-Garcia, Catia
Cucchiarini, and Helmer Strik. 2023. Automatic
speech recognition of non-native child speech for
language learning applications. InProc. 12th Sym-
posium on Languages, Applications and Technolo-
gies (SLATE), OASIcs, pages 11:1–11:8. Whisper
WER on read speech: native vs non-native Dutch
children, roughly threefold gap. arXiv:2306.16710.
Verified 2026-08-29.
Silke M. Witt and Steve J. Young. 2000. Phone-level
pronunciation scoring and assessment for interactive
language learning.Speech Communication, 30(2–
3):95–108.
Jian Xu, Yi Yan, and Shao-Lun Huang. 2022. Fed-
Per++: Toward improved personalized federated
learning on heterogeneous and imbalanced data. In
2022 International Joint Conference on Neural Net-
works (IJCNN), pages 01–08. IEEE.
Qiantong Xu, Alexei Baevski, and Michael Auli.
2021. Simple and effective zero-shot cross-
lingual phoneme recognition.arXiv preprint
arXiv:2109.11680.
Yi Yan, Dayu Qin, and Ercan E Kuruoglu. 2026. LLM
online spatial-temporal signal reconstruction under
noise.IEEE Journal of Selected Topics in Signal
Processing.
Akifumi Yanagisawa, Stuart Webb, and Takumi Uchi-
hara. 2020. How do different forms of glossing con-
tribute to L2 vocabulary learning from reading? A
meta-regression analysis.Studies in Second Lan-
guage Acquisition, 42(2):411–438.
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak
Shafran, Karthik Narasimhan, and Yuan Cao. 2023.
ReAct: Synergizing reasoning and acting in lan-
guage models. InProc. International Conference on
Learning Representations (ICLR).

A The Designed Self-Report Instrument
Table 7 reproduces the complete instrument of Section 6.10. It is designed and released with the system;
it has not been administered, and no response data exist at the time of writing.
Table 7: The LLMersion-1 preliminary longitudinal self-report instrument (designed; not yet administered or
validated). Mark one box per row: 0 = strongly disagree / never, 4 = strongly agree / always. Items 21–24 apply
only to learners who use the night curator.
Time using the system:□first session□1 week□1 month□1 year 0 1 2 3 4
Reading fluency
1 I can read English technical documents for longer sessions without fatigue.□ □ □ □ □
2 My reading speed on technical English has increased.□ □ □ □ □
3 I rarely need to re-read a sentence to work out its structure.□ □ □ □ □
4 I rely on the translation less than when I started.□ □ □ □ □
Listening
5 I can follow a spoken paragraph without looking at the text.□ □ □ □ □
6 I recognize word boundaries in fast connected speech.□ □ □ □ □
7 Listening at higher playback speeds is comfortable for me.□ □ □ □ □
8 English technical talks and videos are easier to follow than before.□ □ □ □ □
Speaking and pronunciation
9 I read aloud (shadow) along with the voice during my sessions.□ □ □ □ □
10 My pronunciation scores improve on words I practice repeatedly.□ □ □ □ □
11 I am confident pronouncing new technical terms aloud.□ □ □ □ □
12 Listeners understand my spoken English without my repeating myself.□ □ □ □ □
Vocabulary
13 I look up fewer words per page in documents from my field.□ □ □ □ □
14 Words I saved earlier reappear in my reading and I recognize them.□ □ □ □ □
15 Flashcard review helps me retain the words I saved.□ □ □ □ □
16 I can recall the pronunciation of saved words, not only their meaning.□ □ □ □ □
Integrated study workflow
17 Reading with synchronized audio keeps me more focused than silent reading.□ □ □ □ □
18 I complete more English documents per week than before.□ □ □ □ □
19 I use the system for documents I genuinely need, not only practice texts.□ □ □ □ □
20 Overall, this system has improved my English more than my previous routine.□ □ □ □ □
Material supply (optional module: answer only if you use the night curator)
21 The curator’s nightly picks match my interests.□ □ □ □ □
22 The difficulty of curated material is right for me.□ □ □ □ □
23 Curated material re-encounters words I have been looking up.□ □ □ □ □
24 I actually read the curated picks rather than letting them pile up.□ □ □ □ □
