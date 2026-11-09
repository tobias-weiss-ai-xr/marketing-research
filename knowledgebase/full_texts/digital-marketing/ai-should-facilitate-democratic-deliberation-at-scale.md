---
title: AI Should Facilitate Democratic Deliberation at Scale
url: https://arxiv.org/abs/2609.20059
category: digital-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- José Ramón Enríquez
- Jiaxin Pei
- Alex Pentland
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.20059
pages: 15
chars: 74574
fetched_at: '2026-11-08T13:20:42+00:00'
kb_version: 1
---

# AI Should Facilitate Democratic Deliberation at Scale

Position: AI Should Facilitate Democratic Deliberation at Scale
José Ramón Enríquez 1 2 Jiaxin Pei 2 Alex Pentland 2 3
Abstract
AI systems can strengthen democracy by support-
ing deliberation at scale by addressing cognitive,
social, platform-design, and market-driven fric-
tions, while preserving human agency. Unlike
proposals such as liquid democracy that restruc-
ture representation through vote delegation, in
this position paper, we argue that AI-assisted de-
liberation offers a more promising path by low-
ering barriers to meaningful engagement without
substituting machine judgment for human choice.
Drawing on evidence from online deliberation
platforms and experimental research, we identify
four guiding principles: preserving agency and
autonomy, encouraging mutual respect, promot-
ing equality and inclusiveness, and augmenting
rather than substituting active citizenship. We also
address critical challenges, including alignment,
sycophancy, training bias, and over-reliance on AI
systems. We call on the machine learning commu-
nity to develop deliberation-focused AI systems
evaluated not on engagement metrics but on their
capacity to facilitate informed, representative, and
friction-robust discourse.
1. Introduction
Democratic societies face a representation crisis. Trust in
government has declined across established and develop-
ing democracies, with citizens perceiving widening gaps
between public preferences and policy outcomes (Citrin
and Stoker, 2018; Valgarðsson et al., 2025; Wike, 2025).
Affective polarization, the tendency to view political op-
ponents with contempt rather than mere disagreement, has
intensified (Reiljan et al., 2024; Boxell et al., 2024) and
populist discourse has deepened (Guriev and Papaioannou,
2022). Social media platforms, initially celebrated as de-
1Stanford Graduate School of Business, Stanford, CA, USA
2Stanford Institute for Human-Centered AI, Stanford, CA, USA
3MIT Media Lab, Cambridge, MA, USA. Correspondence to: José
Ramón Enríquez <jrenriquez@stanford.edu>.
Proceedings of the 43 rd International Conference on Machine
Learning, Seoul, South Korea. PMLR 306, 2026. Copyright 2026
by the author(s).
mocratizing forces that could amplify previously unheard
voices (Farrell, 2012; Tudoroiu, 2014; Jost et al., 2018),
have instead contributed to these problems: amplifying po-
larization, accelerating the spread of misinformation, and
systematically rewarding divisiveness over civic engage-
ment (Tucker et al., 2018; Bail et al., 2018; V osoughi et al.,
2018; Levy, 2021; Nyhan et al., 2023). However, at this
transformative moment for generative foundation models,
the question is not whether technological intervention is
needed, but what form it should take.
We argue that AI systems, when designed to complement
rather than substitute human judgment, offer an unprece-
dented opportunity to strengthen democracy by enabling de-
liberation at scale while addressing frictions that undermine
meaningful civic engagement. This position draws on a rich
tradition of democratic theory—from Habermas’s commu-
nicative action (1984) through Landemore’s open democ-
racy (2020) to Mansbridge’s systemic approach (2012)—
which holds that legitimate collective decisions emerge
through reasoned exchange among free and equal citizens.
Our position contrasts with alternative proposals, such as
liquid democracy, which enables transitive vote delegation
(Blum and Zuber, 2016), by emphasizing that AI should
augment human deliberative capacity rather than restructure
democratic representation itself.
The deployment of AI in democratic contexts presents both
promise and peril. On one hand, LLMs can summarize
complex policy debates (Li et al., 2024), translate across
languages (Lai et al., 2024), identify areas of emerging
consensus (Tessler et al., 2024; Braley et al., 2025b), and
help citizens articulate their views more clearly (Palmer and
Spirling, 2023; Bai et al., 2025a). On the other hand, LLMs
exhibit systematic biases toward Western cultural values
(Santurkar et al., 2023; Tao et al., 2024), display sycophantic
tendencies that amplify rather than moderate extreme views
(Sharma et al., 2023; Rathje et al., 2025), and risk creating
new forms of democratic exclusion. The challenge is to
harness AI’s capacity to reduce friction while preserving
the deliberative qualities—reflection, mutual justification,
and preference transformation—that distinguish democratic
deliberation from mere preference aggregation (Dryzek and
List, 2003).
Our argument proceeds as follows. We first articulate the
case for deliberation at scale and identify the behavioral
1
arXiv:2609.20059v1  [cs.HC]  17 Sep 2026

AI-Assisted Deliberation at Scale
frictions that limit its realization. We then present guid-
ing principles for pro-democratic AI design and show how
emerging platforms instantiate these principles through spe-
cific LLM-assisted interventions. We address critical chal-
lenges including sycophancy, training bias, and alignment,
engage with alternative perspectives, and conclude with a
call to action for the machine learning community.
2. The case for deliberation at scale
The democratic deficits like declining trust, rising affec-
tive polarization, and amplified misinformation are not in-
evitable features of mass democracy. A central insight from
deliberative democratic theory and practice is that the qual-
ity of collective decisions depends fundamentally on the
processes through which citizens form and express their
preferences (Gutmann and Thompson, 2009; Fishkin, 2009).
Deliberation works not by suppressing disagreement but
by transforming it: when citizens engage in structured dis-
cussion rather than simply broadcasting preferences, they
develop more informed positions, greater tolerance for op-
posing views, and increased willingness to accept outcomes
they did not initially prefer (Curato et al., 2017; Fishkin et
al., 2021). Empirical studies of deliberative forums consis-
tently show that participants update their views in response
to evidence, recognize legitimate concerns they had not pre-
viously considered, and report enhanced political efficacy
(Grönlund et al., eds, 2014; Luskin et al., 2002; Curato et al.,
2021). The challenge is therefore not whether deliberation
can address democratic dysfunction, but whether it can do
so at scale.
The benefits of deliberation operate at multiple levels. At
the individual level, participants in deliberative forums show
significant knowledge gains, with increase in factual under-
standing of policy issues (Fishkin et al., 2021; Luskin et al.,
2002). They also exhibit attitude change toward more mod-
erate, considered positions—not because they are pressured
to conform, but because exposure to diverse perspectives
and the requirement to justify one’s views produces genuine
reflection (Mercier and Sperber, 2011). At the community
level, deliberation reduces affective polarization with persis-
tent effects (Fishkin et al., 2024). Notably, in some cases,
deliberative processes generate positive spillover effects
within participants’ social networks (Paluck et al., 2016). At
the systemic level, deliberative processes produce decisions
that command broader legitimacy and trust and citizens are
more willing to accept outcomes (even unfavorable ones)
when they believe the process was fair and inclusive (Curato
et al., 2017). These empirical findings align with theoretical
arguments that democratic legitimacy requires not just pref-
erence aggregation but mutual justification among free and
equal citizens (Hauptmann, 1999; Cohen, 2007).
Yet traditional deliberation faces severe scalability con-
straints. Deliberative polling, for instance, requires trained
facilitators, careful sampling to ensure demographic repre-
sentation, physical venues, and participant compensation—
substantial resource requirements that limit even well-
funded implementations to a few hundred participants
(Fishkin et al., 2021). Citizens’ assemblies face similar
constraints: while they can produce high-quality recom-
mendations on contentious issues like electoral reform or
climate policy (Suiter et al., 2020), their typical size ranges
from 50 to 200 participants, representing only a tiny frac-
tion of affected populations. Open comment periods on
proposed regulations technically achieve mass participation
but produce little genuine exchange as participants broadcast
views without engaging alternatives, and agencies struggle
to extract meaningful signal from massive volumes of often-
duplicative input (Noveck, 2021). Town halls and public
hearings privilege those with time, confidence, and rhetor-
ical skill, systematically excluding working parents, shift
workers, non-native speakers, and others whose voices de-
liberation should amplify (Mansbridge et al., 2012). Online
forums, while potentially scalable, often devolve into echo
chambers or hostile exchanges without careful moderation
(Levy, 2021). The result is a persistent tradeoff: meaningful
deliberation for the few, or superficial participation for the
many.
Digital platforms offered promise to resolve this tradeoff.
Social media promised to democratize discourse by giving
everyone a voice and enabling exchange across geographic
and social boundaries. Instead, these platforms have largely
made deliberation harder. Platform architectures optimized
for engagement systematically favor content that provokes
emotional reactions (Brady et al., 2017; Epstein et al., 2022).
Algorithmic amplification creates “rich-get-richer” dynam-
ics in which a small number of highly active accounts domi-
nate discourse, often amplifying extreme or divisive voices
(Lera et al., 2020; Huszár et al., 2022). False information
spreads faster and reaches more people than corrections
(V osoughi et al., 2018; Pennycook et al., 2021). The at-
tention economy rewards outrage over understanding, with
moral-emotional language and partisan attacks generating
disproportionate engagement (Brady et al., 2020; Van Bavel
et al., 2021). In short, these platforms evolved to maximize
time-on-site and engagement for advertising revenue, not to
support collective reasoning.
A new generation of purpose-built deliberation platforms
demonstrates that digital technology can support civic dis-
course when designed with deliberative principles in mind.
Platforms such as Pol.is, Consider.it, deliberation.io, De-
cidim, and Asembl embody deliberative values through spe-
cific architectural choices: limiting comment frequency to
prevent domination by high-volume users, requiring partici-
pants to engage with others’ views before contributing their
own, visualizing opinion distributions to help participants
2

AI-Assisted Deliberation at Scale
identify both consensus and legitimate disagreement, and
focusing attention on arguments and reasoning rather than
individual identities or social status (Small et al., 2021; Tsai
et al., 2024).
AI systems in general and large language models in particu-
lar offer capabilities that could further extend deliberation’s
reach while addressing specific barriers to meaningful en-
gagement. LLMs can summarize thousands of contributions
into coherent overviews (Konya et al., 2023; Karanam et al.,
2024a;b); translate across languages in real-time, adjusting
language complexity to bridge differences in literacy levels
or technical expertise (Nguyen et al., 2024; Diack et al.,
2026); identify areas of agreement (Tessler et al., 2024); and
help participants articulate positions they struggle to express
(Argyle et al., 2023). Yet realizing this potential requires
understanding the specific frictions that limit online delib-
eration and designing AI interventions that address them
without introducing new problems.
The case forat scalerests on three concrete mechanisms
whose marginal cost per additional participant is small rel-
ative to the fixed costs of traditional deliberation. First,re-
flectioncan be elicited through one or a few LLM-mediated
rounds when participants first encounter contentious topics,
analogous to the lightweight two-step prompts that social
media platforms have used to discourage abusive posts (Kat-
saros et al., 2022). Second,synthesiscan summarize and
cluster opinions across thousands of contributions, replacing
the teams of trained facilitators who would otherwise read,
categorize, and distill them. Platforms such as Pol.is already
perform this clustering in real time (Small et al., 2021; 2023).
The challenge here is to perform this dimensionality reduc-
tion in a principled way that preserves minority perspectives
and aligns model outputs with the underlying distribution
of preferences, which is a non-trivial demand, since minor-
ity viewpoints are often underrepresented both in training
corpora and in LLM-generated summaries (Zhu et al., 2025;
Santurkar et al., 2023; Olabisi and Agrawal, 2024). Third,
moderationcan scaffold deliberative norms through civility
checks, comment recommendation, and equitable participa-
tion safeguards that would be prohibitively costly to staff
with human moderators at the scale of tens of thousands
of simultaneous participants. Transformer-based classifiers
materially outperform earlier rule-based and shallow-NLP
moderation tools on context-sensitive judgments such as
toxicity, harassment, and incivility, and production-grade
implementations such as Google’s Perspective API illus-
trate that this capability is already deployable at web scale
(Pavlopoulos et al., 2020; Lees et al., 2022; Koh et al., 2024).
In each case the marginal cost is computational rather than
human, and inference costs have fallen by roughly an or-
der of magnitude per year for tasks of equivalent quality
(Cottier et al., 2025; Xiao et al., 2025; Maslej et al., 2024).
Crucially, none of these mechanisms requires AI to render
judgments or generate conclusions on participants’ behalf:
each augments human reflection, exchange, and aggregation
rather than substituting for them.
3. Behavioral frictions in online deliberation
Four categories of behavioral frictions limit the quality and
scale of online deliberation. While some frictions reflect
inherent features of human cognition and social interaction,
others emerge from specific technological and economic
structures. Understanding these frictions is essential for
designing AI systems and interventions that address root
causes rather than symptoms.
3.1. Cognitive frictions
Cognitive frictions arise from information processing limi-
tations that constrain deliberative capacity.Cognitive over-
loadoccurs when the demands of processing complex policy
information exceed citizens’ limited attention and working
memory (Kahneman, 2011).Motivated reasoningleads
citizens to process information in ways that confirm prior
beliefs while discounting disconfirming evidence (Kahan,
2013; Epley and Gilovich, 2016).Confirmation biascom-
pounds this tendency by shaping which information citizens
seek in the first place (Nickerson, 1998).Correlation neglect
causes citizens to treat correlated information sources as in-
dependent, leading to overconfidence in positions supported
by redundant evidence (Ortoleva and Snowberg, 2015; Levy
and Razin, 2015; Enke and Zimmermann, 2019).
These frictions manifest predictably: citizens struggle to
articulate positions precisely, find it difficult to comprehend
technical arguments, and cannot track evolving discussions
involving numerous participants. Critically, cognitive fric-
tions might disproportionately disadvantage those with less
education, time, or cognitive resources, creating systematic
bias toward the views of the privileged and undermining
deliberation’s promise of democratic equality. When de-
liberative processing is overwhelmed, citizens default to
automatic responses—partisan heuristics, emotional reac-
tions, and group identities—that undermine deliberative
quality (Lodge and Taber, 2013; Bénabou and Tirole, 2011).
3.2. Social frictions
Social frictions emerge from affective polarization, peer
pressure, and ideological sorting that fragment the delibera-
tion space. This is manifested in increasing dislike distrust,
and even disgust (Iyengar et al., 2019). Partisans systemati-
cally overestimate the extremity of their opponents’ views
(Braley et al., 2025b; Mernyk et al., 2022). Mispercep-
tions lead to preemptive hostility that crowds out genuine
exchange.
Peer pressure within ideological communities rein-
3

AI-Assisted Deliberation at Scale
forces conformity and punishes heterodox views (Noelle-
Neumann, 1993; Mallinson and Hatemi, 2018). Geographic
sorting concentrates like-minded citizens in the same com-
munities, reducing exposure to diverse perspectives and
creating echo chambers that extend from neighborhoods to
online networks (Bishop and Cushing, 2008). The “sub-
version dilemma” (Braley et al., 2023) formalizes these
dynamics: fear of opponents exploiting democratic norms
creates incentives to abandon those norms preemptively,
even among citizens who value democracy. The crucial find-
ing is that correcting these misperceptions increases support
for democratic norms, suggesting that social frictions may
be tractable through appropriate intervention.
3.3. Platform-design and market-incentive frictions
Platform-design frictions result from architectural choices
that privilege certain voices over others independent of the
quality of their contributions. Unlimited commenting en-
ables a few voices to dominate discussions, crowding out the
broader population (Krämer et al., 2021). Reply functions
facilitate flame wars and ad hominem attacks that poison
the deliberative space (Cheng et al., 2017).“Rich-get-richer”
feedback loops become dominated by a small number of
accounts with extremely large followings (Lera et al., 2020),
rendering mass conversations neither inclusive nor rational.
These design choices reflect engineering decisions, not
democratic values. Most platforms were built to facili-
tate connection and content sharing, not deliberation (Gille-
spie, 2018). Features that maximize user engagement—
notifications, infinite scroll, algorithmic amplification of
reactions—actively work against the reflection and empa-
thy that meaningful discussion requires. The result is that
platform architecture systematically advantages the loud,
the persistent, and the provocative over the thoughtful, the
marginalized, and the constructive.
Market-incentive frictions arise from the business models
that govern digital platforms. Advertising-based revenue
models create incentives to maximize short-term engage-
ment rather than long-term deliberative quality (Ahmad,
2025). Platforms that profit from attention have incentives
to amplify divisive content that keeps users scrolling (Ep-
stein et al., 2022).These attention economies create a race
to the bottom in which deliberative quality is sacrificed to
competitive pressures.
3.4. Compounding effects
These frictions interact and compound in harmful ways.
Cognitive overload leaves citizens vulnerable to affective
shortcuts and partisan heuristics. Social mistrust discour-
ages the interpretation of ambiguous statements. Patform
design amplifies the voices least conducive to productive
exchange. Market incentives reward the exploitation of all
three preceding frictions. The result is not merely subopti-
mal deliberation but active degradation of civic capacity.
4. Guiding principles for pro-democratic AI
Drawing on deliberative democratic theory and recent work
on AI governance (Allen and Weyl, 2024; Lazar and Man-
uali, 2024; Tsai et al., 2024; Farrell, 2025; Burton et al.,
2024), we identify four principles that should govern the
integration of LLMs into deliberative platforms.
Preserving agency and autonomy.Pro-democratic AI
must preserve citizens’ capacity to reflect on their interests
and make choices without manipulation or undue influence
(Dahl, 2008). Technologies that distort information neces-
sary for informed judgment, limit available actions without
the user’s knowledge, or apply pressure toward particular
conclusions violate this principle. AI should inform and
enable choices, not make them.
Encouraging mutual respect.In an environment of polar-
ization and mistrust, platforms must help citizens engage
respectfully with those holding different views (Gutmann
and Thompson, 2009). This means flagging potentially of-
fensive language, providing alternative phrasings, and struc-
turing interactions to emphasize shared concerns rather than
divisions. AI moderation should maintain civility without
suppressing substantive disagreement.
Promoting equality and inclusiveness.Every participant
should have equal opportunity to contribute and be heard
(Young, 2002). This requires accessibility across languages,
literacy levels, and technical expertise. It also requires pre-
venting any individual, bot, or elite group from dominating
discourse. AI should amplify marginalized voices rather
than reinforce existing inequalities.
Augmenting rather than substituting active citizenship.
AI should provide tools for obtaining information, articu-
lating positions, and understanding others, not delegate to
machines the responsibilities that define citizenship. Delib-
eration’s benefits like preference transformation, increased
empathy, and mutual justification require human engage-
ment. Consequently, LLMs should be kept at arm’s length
from formal democratic decision-making but can strengthen
the informal public sphere where citizens seek information,
form civic publics, and hold leaders accountable (Lazar and
Manuali, 2024). Our focus on deliberation-supporting rather
than decision-making AI operationalizes this distinction.
4.1. Why these four principles?
Alternative frameworks for governing democratic AI empha-
size different organizing principles. The AI ethics guidelines
surveyed by Jobin et al. (2019) most frequently cite trans-
parency and accountability, while Gabriel et al. (2024) em-
4

AI-Assisted Deliberation at Scale
phasize safety, honesty, and harm avoidance. Engineering
discussions privilege efficiency and scalability; commercial
development centers on user satisfaction and engagement.
We argue that our four principles (agency, respect, equal-
ity, and augmentation) are both necessary and sufficient for
pro-democraticAI specifically, articulating positive require-
ments for systems that enhance collective self-governance
rather than merely negative constraints against harm. Trans-
parency supports agency by enabling informed choices and
equality by exposing discriminatory patterns, but a manip-
ulative system could be fully transparent about its mecha-
nisms while still undermining deliberation. Accountability
provides enforcement but does not specify normative com-
mitments. Safety prevents damage but does not distinguish
systems that actively strengthen democratic capacity from
those that merely avoid harm.
Efficiency and user satisfaction pose sharper tensions with
deliberative values. Deliberation is inherently slow: the cog-
nitive work of understanding diverse perspectives, updating
beliefs, and reaching reasoned accommodation cannot be
compressed without sacrificing the preference transforma-
tion that gives deliberation its democratic value (Fishkin et
al., 2021). Our augmentation principle thus constrains effi-
ciency: AI should reduce friction in accessing information,
not in deliberative processing itself. Moreover, user satis-
faction can directly conflict with deliberative quality: users
may prefer validation to challenge, simplification to nuance,
and agreement to productive disagreement. Our principles
privilege conditions for good deliberation over subjective
experience, forming a coherent framework in which agency
and equality establish who participates and on what terms,
respect governs how participants engage, and augmentation
constrains AI’s role. Other principles such as transparency,
accountability, safety, efficiency serve these core democratic
values but cannot replace them. Importantly, the four prin-
ciples are not in one-to-one correspondence with the four
friction categories of Section 3: each principle operates as a
cross-cutting constraint on every AI capability, regardless of
which friction the capability primarily addresses. Figure 1
depicts this structure, with principles shown as a band above
the friction–capability flow rather than as a column aligned
to particular frictions.
5. Promising directions: Evidence from
AI-assisted deliberation
A growing body of empirical research demonstrates that
AI interventions can address deliberative frictions while
preserving, and in some cases enhancing, the qualities that
make deliberation democratically valuable. We review evi-
dence organized by the friction categories identified above,
drawing on randomized experiments, field deployments,
and observational studies from platforms serving millions
of users. The studies surveyed below operationalize deliber-
ative quality through a range of quantitative measures, like
the Discourse Quality Index of Steenbergen et al. (2003),
the Deliberative Reason Index of Niemeyer et al. (2024),
and Fishkin’s measures of opinion change, knowledge gain,
and preference coherence (Fishkin et al., 2021; Luskin et al.,
2002), bridging scores that quantify cross-partisan agree-
ment, attitudinal scales of policy preferences, and emerging
text-analytic measures of perspective diversity. Together
these constitute candidate components of the deliberative-
quality benchmarks called for in Section 8.
Figure 2 makes the deliberation workflow into which AI
capabilities are inserted explicit. It maps four canonical
stages of online deliberation—input elicitation, reflection,
structured exchange, and synthesis—to the AI capabilities
reviewed in this section. We treat these stages as illustrative
rather than prescriptive: actual deployments commonly col-
lapse, reorder, or iterate over them, and the relevant claim is
that the same AI capabilities map onto whichever workflow
a given platform adopts. Throughout, AI provides scaf-
folding for human reasoning rather than substituting for it:
participants generate inputs, update their views, exchange
arguments, and determine the conclusions themselves.
5.1. Addressing cognitive frictions
AI interventions can reduce cognitive barriers without substi-
tuting for human reasoning. Real-time language assistance
improves conversation quality while preserving participant
autonomy: Argyle et al. (2023) shows that LLM-suggested
rephrasings enhanced democratic reciprocity and mutual
understanding in partisan discussions without shifting pol-
icy attitudes. This is, improvinghowcitizens communicate
without influencingwhatthey believe. Moreover, Behrendt
et al. (2025) tested AI modules on the adhocracy+ platform
and found that a Comment Recommendation Module in-
creased participation and improved users’ perceptions of
deliberative quality while not diminishing their sense of au-
tonomy. These findings suggest AI can reduce interpersonal
friction and help participants engage with relevant content,
preserving substantive disagreement while lowering barriers
to productive exchange.
Summarization and preference elicitation offer scalable ap-
proaches to synthesizing collective input without supplant-
ing human judgment. Konya et al. (2023) deployed LLM-
powered pipelines to identify consensus from large-scale
collective dialogues, translating bridging responses into pol-
icy guidelines that achieved strong cross-partisan support
across contentious issues. Karanam et al. (2024b) extend
this direction with Policy Dreamer, which elicits citizen
preferences through structured interactions and generates
diverse policy alternatives via simulation, enabling explo-
ration beyond positions participants explicitly articulate.
5

AI-Assisted Deliberation at Scale
Cross-cutting Principles (govern every AI capability below)
Agency Respect Equality Augmentation
Frictions AI Capabilities Goal
Cognitive
Social
Platform-Design
Market-Incentive
Summarization
Socratic Dialogue
Opinion Visualization
Consensus Mapping
AI Moderation
Equal V oice
Quality Metrics
Alignment
High-quality
Scaled
Deliberation
Figure 1.Conceptual framework for AI-assisted deliberation. The four guiding principles (agency, respect, equality, augmentation)
operate ascross-cutting constraints: they governhowevery AI capability is deployed rather than mapping one-to-one onto particular
frictions. The enclosing frame indicates that every element of the flow below, frictions, AI capabilities, and the deliberative goal, is subject
to the principles above. Within the flow, frictions (cognitive, social, platform-design, market-incentive) are addressed by AI capabilities
that together support high-quality scaled deliberation. Solid arrows denote primary friction–capability pairings. Faint dashed arrows
indicate secondary effects.
More broadly, Ovadya (2023) outlines how collective re-
sponse systems can leverage LLMs for real-time synthesis
while maintaining democratic legitimacy. Effective summa-
rization thus requires attention to what is excluded as much
as what is included.
A distinct line of research examines whether AI-guided self-
reflection can moderate extreme positions through epistemic
rather than persuasive mechanisms. Enríquez (2025) finds
that AI-Socratic dialogue, where an LLM prompts users to
articulate supporting arguments without introducing exter-
nal information, reduced extreme positioning and increased
cross-partisan behavioral outcomes. Crucially, moderation
occurred through enhanced perspective-taking rather than
improved argument quality, and perceived agency remained
equivalent across conditions. Related work confirms these
patterns: Socratic AI chatbots that prompt users to examine
the origins of contested claims stimulate critical thinking
without asserting conclusions (Duelen et al., 2024). These
findings suggest that fostering epistemic humility through
AI-guided self-reflection may prove more consequential
than providing superior arguments.
5.2. Addressing social frictions
Social frictions often stem from inaccurate beliefs about
what others think. Visualizing opinion distributions can
correct these misperceptions without the AI systems them-
selves advocating for positions. Braley et al. (2025b) finds
that exposure to accurate visualizations of opinion distribu-
tions significantly increased cross-partisan consensus and
willingness to take collective action. These findings align
with V oelkel et al. (2024), whose megastudy identified cor-
recting misperceptions about opposing partisans as among
the most effective interventions for reducing support for
undemocratic practices. The mechanism is informational
rather than persuasive: participants update beliefs when
shown evidence that their mental model of the out-group (or
own’s in-group) was inaccurate.
AI can help surface latent agreement without generating
the consensus itself. Konya et al. (2023) used bridging-
based ranking algorithms to identify responses with high
agreement across demographic divides, surfacing common
ground that participants had articulated but not recognized
as shared. Similarly, collective dialogue platforms can high-
light areas of emerging convergence, directing participant
attention toward promising avenues for agreement (Ovadya,
2023). The key distinction is between AI thatdiscovers
consensus among human-generated positions versus AI that
generatesconsensus statements. The former augments hu-
man deliberation while the latter risks substituting for it.
When AI tools surface what participants already believe but
did not realize others shared, they reduce social friction by
6

AI-Assisted Deliberation at Scale
1. Elicitation 2. Reflection 3. Exchange 4. Synthesis
Real-time language
assistance;
preference articulation
AI-Socratic dialogue;
perspective-taking
prompts
Comment recommendation;
civility moderation;
turn-taking
Bridging-based ranking;
opinion clustering;
summarization
Cross-cutting principles: Agency·Respect·Equality·Augmentation
Figure 2.Deliberation workflow with AI capabilities mapped to each stage. Participants move from input elicitation, through reflection on
their initial reactions, to structured exchange with others, and finally to synthesis of collective inputs. AI capabilities (in green) provide
scaffolding at each stage. The guiding principles (in amber) constrain how every capability is deployed. The four stages are illustrative
rather than prescriptive: actual platforms vary in their sequence and granularity, and individual stages may be collapsed, reordered, or
iterated. The cross-cutting principle is that, at no stage, the AI renders judgments or generates conclusions on participants’ behalf.
correcting coordination failures rather than by persuading
anyone to change positions.
More ambitious interventions use AI to support rather than
replace human facilitation. Dynamic question generation
represents a further extension: AI that identifies underex-
plored dimensions of a debate and proposes targeted dis-
cussion prompts can increase conversational breadth while
leaving substantive choices to participants (Braley et al.,
2025a). The common thread is AI as scaffolding for human
exchange, reducing the cognitive and social costs of deliber-
ation while preserving the human character of the reasoning
and compromise that emerge.
5.3. Addressing system frictions
Platform design choices shape the conditions for construc-
tive and inclusive deliberation. Pol.is and deliberation.io
limit contributions per user, require identity verification
while permitting pseudonymous participation, and disable
direct replies that facilitate adversarial exchanges (Small
et al., 2021; Pei et al., 2025). These constraints reflect the
principle that productive conversations depend on engaging
with arguments rather than personal characteristics. Syn-
chronous platforms such as the Stanford Online Deliberation
Platform and Frankly implement automated turn-taking and
timed agendas to ensure equitable speaking opportunities
regardless of participant assertiveness or status (Fishkin et
al., 2019; Roy et al., 2025). Such structural safeguards cre-
ate conditions for broader participation that AI assistance
can further enhance.
Field experiments reveal additional mechanisms for improv-
ing participation quality. Ahmad (2025) find that high-
quality conversations yield sustained engagement in on-
line forums, suggesting that deliberative norms and long-
term participation are complementary rather than competing
objectives. Chen et al. (2025) demonstrate that comment
presentation order affects perceived legitimacy: sequences
progressing from similar to different viewpoints increase
participants’ sense of representation and procedural fair-
ness. AI systems can dynamically optimize these structural
features, personalizing the deliberative experience while
maintaining consistent standards across participants.
AI can also reduce barriers to participation without directing
outcomes. Real-time translation, text-to-speech, and sim-
plified language options extend deliberative opportunities
to populations excluded from traditional forums (OECD,
2025). The key distinction is between AI thatenforces
norms and AI thatenablesparticipants to meet norms they
already endorse: the former risks paternalism while the
latter augments human capacity for inclusive exchange.
These components can be integrated into coherent, open-
source systems that preserve human agency and permit lo-
cal adaptation. Several platforms exemplify this approach.
Deliberation.io offers modular AI components that com-
munities can tailor to local contexts, audit for algorithmic
transparency, and govern democratically (Pei et al., 2025).
Decidim provides comprehensive participation infrastruc-
ture spanning ideation, deliberation, and decision-making,
with user-governance practices that allow implementing
organizations to shape platform evolution (Barandiaran et
al., 2019). Pol.is presents its opinion-clustering algorithms
as open source, enabling independent verification of how
consensus is identified and minority viewpoints surfaced
(Small et al., 2021). Across these platforms, open-source
release ensures that deliberative infrastructure remains a
public good rather than proprietary technology, which en-
ables communities to maintain control over the systems that
mediate their collective reasoning.
7

AI-Assisted Deliberation at Scale
6. Critical challenges and safeguards
The evidence reviewed in Section 5 establishes that com-
ponents of AI-assisted deliberation can work in carefully
designed settings, not that they already do so reliably across
deployments. Our position is normative: we argue that AI
systemsshouldbe designed to facilitate deliberation, and
we identify the specific challenges the machine learning
community must address before this potential is realized
at scale. The remainder of this section examines four such
challenges.
Generative foundation models simultaneously threaten and
offer tools to strengthen democracy (Allen and Weyl, 2024;
Lazar and Manuali, 2024; Tsai et al., 2024; Farrell, 2025).
On the risks side, AI enables deception and persuasion at
scale (Lin et al., 2025), can flatten preferences (Matz et
al., 2025; Sourati et al., 2026), and concentrates power in
those who control these systems (Kasy, 2025). On the op-
portunity side, the same technologies can reduce barriers
to participation and surface genuine consensus obscured
by partisan framing. Lazar and Manuali (2024) provide a
useful framework for navigating this tension: LLMs should
be kept at arm’s length from formal democratic processes
but can strengthen the informal public sphere where citizens
seek information, form civic publics, and hold leaders ac-
countable. Our focus on deliberation-supporting rather than
decision-making AI aligns with this prescription. With this
framing, we examine four challenges that require particular
attention.
6.1. Sycophancy and echo chambers
LLMs exhibit systematic tendencies toward sycophancy—
validating users’ existing beliefs rather than challenging
them constructively (Sharma et al., 2023; Rathje et al., 2025).
Experiments show that sycophantic chatbots increase atti-
tude extremity and certainty, with participants perceiving
validating AI as unbiased while viewing disagreeable AI
as biased—despite both being equally biased in opposite
directions. This “bias blind spot” is particularly insidious
for deliberative applications: users recognize bias in AI that
disagrees with them but not in AI that confirms their views.
AI systems designed to maximize user satisfaction will
undermine deliberative goals. Effective facilitation must
sometimes challenge rather than validate, present counter-
arguments alongside supporting evidence, and resist telling
users what they want to hear. This requires evaluation met-
rics based on deliberative quality rather than engagement or
satisfaction scores.
6.2. Training bias
LLM training introduces systematic biases along multiple
dimensions that threaten deliberative equality. Ideologically,
models can display slant across political topics (Motoki
et al., 2024; Westwood et al., 2025). Geographically and
culturally, models express values most aligned with English-
speaking and Protestant European countries, with reinforce-
ment learning from human feedback encoding the perspec-
tives of annotators disproportionately drawn from WEIRD
(Western, Educated, Industrialized, Rich, Democratic) popu-
lations (Tao et al., 2024; Kharchenko et al., 2024; Henrich et
al., 2010). Demographically, gender and racial bias appears
in substantial propotions, with even models containing im-
plicit stereotypes that translate to discriminatory outcomes
in applied settings like resume evaluation (Omar et al., 2025;
Bai et al., 2025b; An et al., 2025). Linguistically, English-
centric training degrades performance and amplifies biases
for non-English deliberation (Navigli et al., 2023).
For deliberative platforms operating across diverse contexts,
these intersecting biases risk systematically misrepresenting
participants from underrepresented ideologies, regions, cul-
tures, and demographic groups, which privileges dominant
viewpoints at the expense of universal reason. Address-
ing this requires ongoing evaluation against diverse bench-
marks, representative training and annotation populations,
and mechanisms for participants to flag misrepresentation.
6.3. Over-reliance and agency erosion
The convenience of AI assistance creates risks of over-
reliance that erode the very capacities deliberation should
cultivate. If citizens outsource opinion formation to LLMs,
they may develop less coherent preferences and reduced
capacity for independent reasoning (Gerlich, 2025; Benedek
and Sziklai, 2025). This “cognitive offloading” reduces
immediate cognitive load but comes at the cost of deep
engagement and critical reflection (Chirayath et al., 2025).
More troublingly, LLMs possess substantial persuasive ca-
pacity: Bai et al. (2025a) demonstrate that LLM-generated
messages shift policy attitudes as effectively as human-
authored messages, while Lin et al. (2025) show that AI-
human dialogues can change voter preferences on politically
contested issues. These capabilities create temptations to
deploy AI for persuasion rather than augmentation, vio-
lating the principle that AI should enhance how citizens
reason, not influence what they conclude. The deliberative
benefits accrue through human engagement, not efficient
outcomes. An AI system that produces consensus with-
out human deliberation—or worse, manufactures it through
persuasion—may achieve agreement without achieving the
civic learning that makes agreement valuable and, ultimately,
generates the conditions for agreement to be binding.
Safeguards include requiring human validation of AI-
generated content, providing multiple options rather than
single recommendations that create anchoring effects, mak-
ing AI assistance optional rather than default, and designing
8

AI-Assisted Deliberation at Scale
friction that encourages engagement rather than frictionless
paths to AI-generated conclusions.
6.4. Alignment
The alignment problem takes on distinctive urgency in de-
liberative contexts. Models must balance responsiveness to
user preferences against resistance to manipulation, facili-
tate constructive disagreement rather than premature con-
sensus, and represent minority viewpoints faithfully even
when aggregating toward majority positions (Gabriel et al.,
2024). Zhu et al. (2025) demonstrate that LLM-generated
summaries systematically underrepresent minority perspec-
tives and exhibit sensitivity to input ordering, raising fair-
ness concerns when synthesizing thousands of contributions
for policy use. Deliberative alignment requires normative
commitments to procedural values (equal voice, mutual re-
spect, reasoned justification) that may conflict with revealed
preferences for validation and conflict avoidance.
The alignment research agenda for deliberative AI should
prioritize: methods for detecting and resisting sycophantic
dynamics, techniques for representing diverse perspectives
without collapsing them into false consensus, evaluation
protocols assessing deliberative quality rather than user sat-
isfaction, and governance structures maintaining human
oversight over AI-mediated democratic processes.
7. Alternative views
Several alternative positions warrant consideration.
Liquid democracy offers a structural alternativeby en-
abling citizens to either vote directly or delegate their votes
to trusted proxies who can further delegate, creating transi-
tive chains of representation (Blum and Zuber, 2016). Propo-
nents argue this combines direct democracy’s inclusiveness
with representative democracy’s expertise. However, exper-
imental evidence suggests delegation underperforms both
universal majority voting and simple abstention (Mooers
et al., 2024). Participants struggle to assess the quality of
potential delegates, and delegation concentrates influence in
ways that may exacerbate rather than remedy representation
problems. Moreover, liquid democracy addresses who de-
cides but not how they deliberate. Our focus on AI-assisted
deliberation concerns the quality of reasoning that precedes
any voting mechanism.
In-person deliberation remains the gold standardfor de-
liberative quality, with evidence that face-to-face interaction
uniquely promotes empathy, trust-building, and preference
transformation. Critics might argue that online deliberation,
however AI-enhanced, cannot replicate these benefits. Yet
in-person deliberation cannot scale to democratic popula-
tions, and evidence suggests that online formats can achieve
comparable outcomes when properly designed (Siu et al.,
2025). The question is not whether online deliberation is
perfect but whether it extends deliberative benefits to par-
ticipants who would otherwise be excluded entirely. Fur-
thermore, AI-facilitated online deliberation offers distinct
advantages: discussions revolve around ideas rather than
the personal characteristics and social identities of speak-
ers, potentially reducing the status hierarchies that distort
face-to-face interaction.
Non-AI online deliberation platformsprovide a closer
point of comparison than either liquid democracy or in-
person formats. Forums such as early Pol.is deployments
without bridging-based ranking, comment-threaded civic
platforms, and human-moderated discussion tools demon-
strate that thoughtful structural design alone can support
productive exchange at modest scale (Small et al., 2021).
The relevant question is therefore not whether AI is neces-
sary for online deliberation, buthowwe envision AI to shape
the process. We see three complementary contributions: (i)
accessibility, through real-time translation, simplification,
and language assistance that extend participation to citi-
zens excluded by literacy, language, or technical barriers
(Argyle et al., 2023; Nguyen et al., 2024); (ii) reflection,
through Socratic prompts and perspective-taking scaffolds
that reduce extreme positioning without injecting external
arguments (Enríquez, 2025); and (iii) synthesis, through
bridging-based ranking and clustering that surface latent
agreement across volumes of contributions beyond what any
human facilitator could feasibly process (Konya et al., 2023;
Small et al., 2021). AI thus does not replace deliberation’s
structural safeguards but extends their reach.
Skeptics of AI in democratic contextsargue that algorith-
mic systems inevitably encode the values of their creators,
creating new forms of technocratic control incompatible
with democratic self-governance (see, for example Allen
and Weyl, 2024). Critics emphasize that democracy requires
not just individual expression but collective sense-making
through “identity validation”: the process by which com-
munities verify that communications genuinely represent
their members’ views. AI systems that can generate unlim-
ited synthetic content threaten this foundation by making it
impossible to distinguish authentic civic voice from manu-
factured discourse.
Our framework addresses these concerns seriously through
the principle of augmentation rather than substitution. The
identity validation challenge reinforces our emphasis on
platforms where AI facilitates rather than generates civic
expression, helping citizens articulate and understand one
another’s views rather than speaking on their behalf. The
alternative, leaving civic discourse to platforms designed
for engagement maximization, hardly represents democratic
self-governance either. The choice is not between AI and
no AI but between AI designed for deliberative quality and
9

AI-Assisted Deliberation at Scale
AI designed for engagement.
8. Call to action
We call on the machine learning community to prioritize
the development of deliberation-focused AI systems evalu-
ated on their capacity to facilitate informed, inclusive, and
consensus-building discourse rather than engagement met-
rics alone.
Researchersshould: (1) develop benchmarks for evalu-
ating AI systems on deliberative quality, building on the
measurement frameworks discussed in Section 5, including
measures of preference coherence, perspective-taking, and
consensus formation; (2) investigate mechanisms of syco-
phancy and methods for promoting constructive challenge;
(3) expand cultural alignment research to include deliber-
ative contexts across diverse populations; and (4) create
standardized protocols for assessing agency preservation in
AI-assisted deliberation.
Platform developersshould: (1) adopt the guiding prin-
ciples articulated here as design constraints; (2) make AI
assistance optional and transparent; (3) implement struc-
tural safeguards against domination by influential accounts;
and (4) subject platforms to independent evaluation against
deliberative standards.
Policymakersshould: (1) fund research on democratic
AI applications as public infrastructure; (2) require trans-
parency about AI use in civic platforms; and (3) consider
regulatory frameworks that distinguish deliberation-focused
platforms from engagement-maximizing social media.
The technology to scale deliberative democracy exists.
The question is whether we will design AI systems that
strengthen citizens’ capacity for collective self-governance
or systems that further erode it.
References
Ahmad, Wajeeha, “Managing Online Participation: Evi-
dence from a Field Experiment with AI Agents,”Working
Paper, 2025.
Allen, Danielle and E. Glen Weyl, “The Real Dangers
of Generative AI,”Journal of Democracy, 2024,35(1),
147–162.
An, Jiafu, Difang Huang, Chen Lin, and Mingzhu Tai,
“Measuring Gender and Racial Biases in Large Language
Models: Intersectional Evidence from Automated Re-
sume Evaluation,”PNAS Nexus, 2025,4(3), pgaf089.
Argyle, Lisa P., Christopher A. Bail, Ethan C. Busby,
Joshua R. Gubler, Thomas Howe, Christopher Ryt-
ting, Taylor Sorensen, and David Wingate, “Leverag-
ing AI for Democratic Discourse: Chat Interventions Can
Improve Online Political Conversations at Scale,”Pro-
ceedings of the National Academy of Sciences, 2023,120
(41), e2311627120.
Bai, Hui, Jan G Voelkel, Shane Muldowney, Johannes C
Eichstaedt, and Robb Willer, “LLM-Generated Mes-
sages Can Persuade Humans on Policy Issues,”Nature
Communications, 2025,16(1), 6037.
Bai, Xuechunzi, Angelina Wang, Ilia Sucholutsky, and
Thomas L Griffiths, “Explicitly Unbiased Large Lan-
guage Models Still Form Biased Associations,”Proceed-
ings of the National Academy of Sciences, 2025,122(8),
e2416228122.
Bail, Christopher A, Lisa P Argyle, Taylor W Brown,
John P Bumpus, Haohan Chen, MB Fallin Hunzaker,
Jaemin Lee, Marcus Mann, Friedolin Merhout, and
Alexander Volfovsky, “Exposure to opposing views on
social media can increase political polarization,”Proceed-
ings of the National Academy of Sciences, 2018,115(37),
9216–9221.
Barandiaran, Xabier E., Antonio Calleja-López, and
Arnau Monterde, “Decidim: Political and Technopoliti-
cal Networks for Participatory Democracy,” White Paper,
Ajuntament de Barcelona, Barcelona 2019.
Bavel, Jay J. Van, Steve Rathje, Elizabeth Harris, Claire
Robertson, and Anni Sternisko, “How Social Media
Shapes Polarization,”Trends in Cognitive Sciences, 2021,
25(11), 913–916.
Behrendt, Maike, Stefan Sylvius Wagner, Mira Warne,
Jana Leonie Peters, Marc Ziegele, and Stefan Harmel-
ing, “Supporting Online Discussions: Integrating AI Into
the adhocracy+ Participation Platform To Enhance De-
liberation,” in “Proceedings of the Fourth Workshop on
Bridging Human-Computer Interaction and Natural Lan-
guage Processing (HCI+ NLP)” 2025, pp. 7–16.
Bénabou, Roland and Jean Tirole, “Identity, Morals, and
Taboos: Beliefs as Assets,”The Quarterly Journal of
Economics, 2011,126(2), 805–855.
Benedek, Márton and Balázs R Sziklai, “Impact of AI
Tools on Learning Outcomes: Decreasing Knowledge
and Over-Reliance,”arXiv preprint arXiv:2510.16019,
2025.
Bishop, Bill and Robert G. Cushing,The Big Sort: Why
the Clustering of Like-Minded America Is Tearing Us
Apart, Boston: Houghton Mifflin Harcourt, 2008.
Blum, Christian and Christina Isabel Zuber, “Liquid
Democracy: Potentials, Problems, and Perspectives,”
Journal of Political Philosophy, 2016,24(2), 162–182.
10

AI-Assisted Deliberation at Scale
Boxell, Levi, Matthew Gentzkow, and Jesse M Shapiro,
“Cross-Country Trends in Affective Polarization,”Review
of Economics and Statistics, 2024,106(2), 557–565.
Brady, William J., Julian A. Wills, John T. Jost,
Joshua A. Tucker, and Jay J. Van Bavel, “Emotion
Shapes the Diffusion of Moralized Content in Social Net-
works,”Proceedings of the National Academy of Sciences,
2017,114(28), 7313–7318.
Brady, William J, Molly J Crockett, and Jay J Van Bavel,
“The MAD Model of Moral Contagion: The Role of Moti-
vation, Attention, and Design in the Spread of Moralized
Content Online,”Perspectives on Psychological Science,
2020,15(4), 978–1010.
Braley, Alia, Gabriel S Lenz, Dhaval Adjodah, Hossein
Rahnama, and Alex Pentland, “Why voters who value
democracy participate in democratic backsliding,”Nature
human behaviour, 2023,7(8), 1282–1293.
, Jiaxin Pei, Nuole Chen, José Ramón Enríquez, Umar
Patel, Lily Tsai, and Alex Pentland, “Beyond Moder-
ation: How AI Facilitation Can Enrich Online Political
Dialogue,”Working Paper, 2025.
, Lily Tsai, Nuole Chen, José Ramón Enríquez, Umar
Patel, Jiaxin Pei, and Alex Pentland, “The Face of
the Crowd: Generating Consensus and Collective Action
on Deliberative Democracy Platforms,”Working Paper,
2025.
Burton, Jason W, Ezequiel Lopez-Lopez, Shahar
Hechtlinger, Zoe Rahwan, Samuel Aeschbach,
Michiel A Bakker, Joshua A Becker, Aleks
Berditchevskaia, Julian Berger, Levin Brinkmann
et al., “How Large Language Models Can Reshape Col-
lective Intelligence,”Nature Human Behaviour, 2024,8
(9), 1643–1655.
Chen, Nuole, Alia Braley, José Ramón Enríquez, Jiaxin
Pei, Umar Patel, Alex Pentland, and Lily Tsai, “Com-
ment Ordering and Deliberation,”Working Paper, 2025.
Cheng, Justin, Michael Bernstein, Cristian Danescu-
Niculescu-Mizil, and Jure Leskovec, “Anyone can be-
come a troll: Causes of trolling behavior in online discus-
sions,” in “Proceedings of the 2017 ACM conference on
computer supported cooperative work and social comput-
ing” 2017, pp. 1217–1230.
Chirayath, Ginto, K Premamalini, and Jeena Joseph,
“Cognitive Offloading or Cognitive Overload? How AI
Alters the Mental Architecture of Coping,”Frontiers in
Psychology, 2025,16, 1699320.
Citrin, Jack and Laura Stoker, “Political Trust in a Cyn-
ical Age,”Annual Review of Political Science, 2018,21
(1), 49–70.
Cohen, Joshua, “Deliberative democracy,” in “Deliberation,
participation and democracy: Can the people govern?,”
Springer, 2007, pp. 219–236.
Cottier, Ben, Ben Snodin, David Owen, and Tom Adam-
czewski, “LLM Inference Prices Have Fallen Rapidly
but Unequally Across Tasks,”Epoch AI Data Insights,
2025. https://epoch.ai/data-insights/
llm-inference-price-trends.
Curato, Nicole, David Farrell, Brigitte Geissel, Kimmo
Grönlund, Patricia Mockler, Jean-Benoit Pilet, Alan
Renwick, Jonathan Rose, Maija Setälä, and Jane
Suiter,Deliberative Mini-Publics: Core Design Features,
Bristol University Press, 2021.
, John S. Dryzek, Selen A. Ercan, Carolyn M. Hen-
driks, and Simon Niemeyer, “Twelve Key Findings in
Deliberative Democracy Research,”Daedalus, 2017,146
(3), 28–38.
Dahl, Robert A,Democracy and its Critics, Yale University
Press, 2008.
Diack, Abdoulaye, Perry Nelson, Kwaku Agbesi et al.,
“W AXAL: A Large-Scale Multilingual African Language
Speech Corpus,”arXiv preprint arXiv:2602.02734, 2026.
Dryzek, John S and Christian List, “Social Choice Theory
and Deliberative Democracy: A Reconciliation,”British
Journal of Political Science, 2003,33(1), 1–28.
Duelen, Aline, Iris Jennes, and Wendy Van den Broeck,
“Socratic AI Against Disinformation: Improving Critical
Thinking to Recognize Disinformation Using Socratic
AI,” in “Proceedings of the 2024 ACM International Con-
ference on Interactive Media Experiences” 2024, pp. 375–
381.
Enke, Benjamin and Florian Zimmermann, “Correla-
tion Neglect in Belief Formation,”Review of Economic
Studies, 2019,86(1), 313–332.
Enríquez, José Ramón, “AI-Socratic dialogue and political
moderation,”Working Paper, 2025.
Epley, Nicholas and Thomas Gilovich, “The Mechanics of
Motivated Reasoning,”Journal of Economic Perspectives,
2016,30(3), 133–140.
Epstein, Ziv, Hause Lin, Gordon Pennycook, and David
Rand, “Quantifying attention via dwell time and engage-
ment in a social media browsing environment,”arXiv
preprint arXiv:2209.10464, 2022.
Farrell, Henry, “The Consequences of the Internet for
Politics,”Annual Review of Political Science, 2012,15
(1), 35–52.
11

AI-Assisted Deliberation at Scale
, “AI as Governance,”Annual Review of Political Science,
2025,28(1), 375–392.
Fishkin, James, Alice Siu, Larry Diamond, and Nor-
man Bradburn, “Is Deliberation an Antidote to Extreme
Partisan Polarization? Reflections on “America in One
Room”,”American Political Science Review, 2021,115
(4), 1464–1481.
, Nikhil Garg, Lodewijk Gelauff, Ashish Goel, Kamesh
Munagala, Sukolsak Sakshuwong, Alice Siu, and
Sravya Yandamuri, “Deliberative democracy with the
online deliberation platform,” in “The 7th AAAI Con-
ference on Human Computation and Crowdsourcing
(HCOMP 2019)” 2019, pp. 1–2.
Fishkin, James S,When the People Speak: Deliberative
Democracy and Public Consultation, Oxford: Oxford
University Press, 2009.
Fishkin, James, Valentin Bolotnyy, Joshua Lerner, Alice
Siu, and Norman Bradburn, “Can deliberation have last-
ing effects?,”American Political Science Review, 2024,
118(4), 2000–2020.
Gabriel, Iason, Arianna Manzini, Geoff Keeling,
Lisa Anne Hendricks, Verena Rieser, Hasan Iqbal,
Nenad Tomašev, Ira Ktena, Zachary Kenton, Mikel
Rodriguez et al., “The Ethics of Advanced AI Assistants,”
arXiv preprint arXiv:2404.16244, 2024.
Gerlich, Michael, “AI Tools in Society: Impacts on Cog-
nitive Offloading and the Future of Critical Thinking,”
Societies, 2025,15(1), 6.
Gillespie, Tarleton,Custodians of the Internet: Platforms,
Content Moderation, and the Hidden Decisions That
Shape Social Media, Yale University Press, 2018.
Grönlund, Kimmo, André Bächtiger, and Maija Setälä,
eds,Deliberative Mini-Publics: Involving Citizens in the
Democratic Process, ECPR Press, 2014.
Guriev, Sergei and Elias Papaioannou, “The Political
Economy of Populism,”Journal of Economic Literature,
2022,60(3), 753–832.
Gutmann, Amy and Dennis F Thompson,Democracy
and disagreement, Harvard University Press, 2009.
Habermas, Jürgen,The Theory of Communicative Action,
Vol. 1: Reason and the Rationalization of Society, Boston:
Beacon Press, 1984.
Hauptmann, Emily, “Deliberation = Legitimacy = Democ-
racy,”Political Theory, 1999,27(6), 857–872.
Henrich, Joseph, Steven J Heine, and Ara Norenzayan,
“The Weirdest People in the World?,”Behavioral and
Brain Sciences, 2010,33(2-3), 61–83.
Huszár, Ferenc, Sofia Ira Ktena, Conor O’Brien, Luca
Belli, Andrew Schlaikjer, and Moritz Hardt, “Algo-
rithmic Amplification of Politics on Twitter,”Proceed-
ings of the National Academy of Sciences, 2022,119(1),
e2025334119.
Iyengar, Shanto, Yphtach Lelkes, Matthew Levendusky,
Neil Malhotra, and Sean J Westwood, “The Origins
and Consequences of Affective Polarization in the United
States,”Annual Review of Political Science, 2019,22(1),
129–146.
Jobin, Anna, Marcello Ienca, and Effy Vayena, “The
Global Landscape of AI Ethics Guidelines,”Nature Ma-
chine Intelligence, 2019,1(9), 389–399.
Jost, John T, Pablo Barberá, Richard Bonneau, Melanie
Langer, Megan Metzger, Jonathan Nagler, Joanna
Sterling, and Joshua A Tucker, “How Social Media
Facilitates Political Protest: Information, Motivation, and
Social Networks,”Political Psychology, 2018,39, 85–
118.
Kahan, Dan M., “Ideology, Motivated Reasoning, and Cog-
nitive Reflection,”Judgment and Decision Making, 2013,
8(4), 407–424.
Kahneman, Daniel,Thinking, fast and slow, macmillan,
2011.
Karanam, Arjun, Farnaz Jahanbakhsh, and Sanmi
Koyejo, “Towards Deliberating Agents: Evaluating the
Ability of Large Language Models to Deliberate,” in
“NeurIPS 2024 Workshop on Behavioral Machine Learn-
ing” 2024.
, José Ramón Enríquez, Udari Madhushani Sehwag,
Michael Elabd, Kanishk Gandhi, Noah Goodman, and
Sanmi Koyejo, “Policy Dreamer: Diverse Public Pol-
icy Generation Via Elicitation and Simulation of Human
Preferences,” in “Workshop on Socially Responsible Lan-
guage Modelling Research” 2024.
Kasy, Maximilian,The Means of Prediction: How AI Re-
ally Works (and Who Benefits), University of Chicago
Press, 2025.
Katsaros, Matthew, Kathy Yang, and Lauren Fratam-
ico, “Reconsidering Tweets: Intervening During Tweet
Creation Decreases Offensive Content,” in “Proceedings
of the International AAAI Conference on Web and Social
Media,” V ol. 16 2022, pp. 477–487.
12

AI-Assisted Deliberation at Scale
Kharchenko, Julia, Tanya Roosta, Aman Chadha, and
Chirag Shah, “How Well Do LLMs Represent Values
Across Cultures? Empirical Analysis of LLM Responses
Based on Hofstede Cultural Dimensions,”arXiv preprint
arXiv:2406.14805, 2024.
Koh, Hyukhun, Dohyung Kim, Minwoo Lee, and Ky-
omin Jung, “Can LLMs Recognize Toxicity? A Struc-
tured Investigation Framework and Toxicity Metric,” in
“Findings of the Association for Computational Linguis-
tics: EMNLP 2024” Association for Computational Lin-
guistics 2024, pp. 6092–6114.
Konya, Andrew, Lisa Schirch, Colin Irwin, and Aviv
Ovadya, “Democratic Policy Development Using Collec-
tive Dialogues and AI,”arXiv preprint arXiv:2311.02242,
2023.
Krämer, Nicole C, German Neubaum, Stephan Winter,
Leonie Schaewitz, Sabrina Eimler, and Mary Beth
Oliver, “I Feel What They Say: The Effect of Social Me-
dia Comments on Viewers’ Affective Reactions Toward
Elevating Online Videos,”Media Psychology, 2021,24
(3), 332–358.
Lai, Wen, Mohsen Mesgar, and Alexander Fraser,
“LLMs Beyond English: Scaling the Multilingual Capabil-
ity of LLMs with Cross-Lingual Feedback,” in “Findings
of the Association for Computational Linguistics: ACL
2024” Association for Computational Linguistics 2024,
pp. 8186–8213.
Landemore, Hélène,Open Democracy: Reinventing Popu-
lar Rule for the Twenty-First Century, Princeton Univer-
sity Press, 2020.
Lazar, Seth and Lorenzo Manuali, “Can LLMs Advance
Democratic Values?,”arXiv preprint arXiv:2410.08418,
2024.
Lees, Alyssa, Vinh Q. Tran, Yi Tay, Jeffrey Sorensen,
Jai Gupta, Donald Metzler, and Lucy Vasserman, “A
New Generation of Perspective API: Efficient Multilin-
gual Character-Level Transformers,” in “Proceedings of
the 28th ACM SIGKDD Conference on Knowledge Dis-
covery and Data Mining” 2022, pp. 3197–3207.
Lera, Sandro, Alex Pentland, and Didier Sornette, “Pre-
diction and Prevention of Disproportionally Dominant
Agents in Complex Networks,”Proceedings of the Na-
tional Academy of Sciences, 2020,117(44), 27090–
27095.
Levy, Gilat and Ronny Razin, “Correlation Neglect, V ot-
ing Behavior, and Information Aggregation,”American
Economic Review, 2015,105(4), 1634–1645.
Levy, Ro’ee, “Social Media, News Consumption, and Po-
larization: Evidence from a Field Experiment,”American
Economic Review, 2021,111(3), 831–870.
Li, Lincan, Jiaqi Li, Catherine Chen, Fred Gui, Hongjia
Yang, Chenxiao Yu, Zhengguang Wang, Jianing Cai,
Junlong Aaron Zhou, Bolin Shen et al., “Political-LLM:
Large Language Models in Political Science,”arXiv
preprint arXiv:2412.06864, 2024.
Lin, Hause, Gabriela Czarnek, Benjamin Lewis,
Joshua P. White, Adam J. Berinsky, Thomas Costello,
Gordon Pennycook, and David G. Rand, “Persuading
V oters Using Human–Artificial Intelligence Dialogues,”
Nature, 2025,648(8093), 394–401.
Lodge, Milton and Charles S Taber,The rationalizing
voter, Cambridge University Press, 2013.
Luskin, Robert C, James S Fishkin, and Roger Jowell,
“Considered opinions: Deliberative polling in Britain,”
British Journal of Political Science, 2002,32(3), 455–
487.
Mallinson, Daniel J and Peter K Hatemi, “The Effects of
Information and Social Conformity on Opinion Change,”
PLoS ONE, 2018,13(5), e0196600.
Mansbridge, Jane, James Bohman, Simone Chambers,
Thomas Christiano, Archon Fung, John Parkinson,
Dennis F. Thompson, and Mark E. Warren, “A Sys-
temic Approach to Deliberative Democracy,” in John
Parkinson and Jane Mansbridge, eds.,Deliberative Sys-
tems: Deliberative Democracy at the Large Scale, Cam-
bridge: Cambridge University Press, 2012, pp. 1–26.
Maslej, Nestor, Loredana Fattorini, Raymond Perrault,
Vanessa Parli, Anka Reuel, Erik Brynjolfsson, John
Etchemendy, Katrina Ligett, Terah Lyons, James
Manyika, Juan Carlos Niebles, Yoav Shoham, Rus-
sell Wald, and Jack Clark, “The AI Index 2024 Annual
Report,” Technical Report, AI Index Steering Committee,
Institute for Human-Centered AI, Stanford University,
Stanford, CA 2024.
Matz, Sandra C, C Blaine Horton, and Sofie Goethals,
“The Basic B*** Effect: The Use of LLM-Based Agents
Reduces the Distinctiveness and Diversity of People’s
Choices,”arXiv preprint arXiv:2509.02910, 2025.
Mercier, Hugo and Dan Sperber, “Why Do Humans Rea-
son? Arguments for an Argumentative Theory,”Behav-
ioral and Brain Sciences, 2011,34(2), 57–74.
Mernyk, Joseph S, Sophia L Pink, James N Druckman,
and Robb Willer, “Correcting Inaccurate Metapercep-
tions Reduces Americans’ Support for Partisan Violence,”
Proceedings of the National Academy of Sciences, 2022,
119(16), e2116851119.
13

AI-Assisted Deliberation at Scale
Mooers, Victoria, Joseph Campbell, Alessandra Casella,
Lucas de Lara, and Dilip Ravindran, “Liquid Democ-
racy. Two Experiments on Delegation in V oting,”arXiv
preprint arXiv:2212.09715v2, 2024.
Motoki, Fabio, Valdemar Pinho Neto, and Victor Rangel,
“More Human Than Human: Measuring ChatGPT Politi-
cal Bias,”Public Choice, 2024,198(1), 3–23.
Navigli, Roberto, Simone Conia, and Björn Ross, “Biases
in Large Language Models: Origins, Inventory, and Dis-
cussion,”ACM Journal of Data and Information Quality,
2023,15(2), 1–21.
Nguyen, Xuan-Phi, Mahani Aljunied, Shafiq Joty, and
Lidong Bing, “Democratizing LLMs for Low-Resource
Languages by Leveraging their English Dominant Abili-
ties with Linguistically-Diverse Prompts,” in “Proceed-
ings of the 62nd Annual Meeting of the Association for
Computational Linguistics (V olume 1: Long Papers)”
2024, pp. 3501–3516.
Nickerson, Raymond S., “Confirmation Bias: A Ubiqui-
tous Phenomenon in Many Guises,”Review of General
Psychology, 1998,2(2), 175–220.
Niemeyer, Simon, Francesco Veri, John S. Dryzek, and
André Bächtiger, “How Deliberation Happens: Enabling
Deliberative Reason,”American Political Science Review,
2024,118(1), 345–362.
Noelle-Neumann, Elisabeth,The spiral of silence: Public
opinion–Our social skin, University of Chicago Press,
1993.
Noveck, Beth Simone,Solving public problems: A practi-
cal guide to fix our government and change our world,
Yale University Press, 2021.
Nyhan, Brendan, Jaime Settle, Emily Thorson, Mag-
dalena Wojcieszak, Pablo Barberá, Annie Y Chen,
Hunt Allcott, Taylor Brown, Adriana Crespo-Tenorio,
Drew Dimmery et al., “Like-minded sources on Face-
book are prevalent but not polarizing,”Nature, 2023,620
(7972), 137–144.
OECD, “Tackling Civic Participation Challenges with
Emerging Technologies: Beyond the Hype,” OECD Pub-
lic Governance Policy Papers 72, OECD Publishing, Paris
2025.
Olabisi, Olubusayo and Ameeta Agrawal, “Understand-
ing Position Bias Effects on Fairness in Social Multi-
Document Summarization,” in “Proceedings of the
Eleventh Workshop on NLP for Similar Languages, Va-
rieties, and Dialects (VarDial)” Association for Compu-
tational Linguistics Mexico City, Mexico 2024, pp. 117–
129.
Omar, Mahmud, Vera Sorin, Reem Agbareia, Don-
ald U Apakama, Ali Soroush, Ankit Sakhuja, Robert
Freeman, Carol R Horowitz, Lynne D Richardson,
Girish N Nadkarni et al., “Evaluating and Addressing
Demographic Disparities in Medical Large Language
Models: A Systematic Review,”International Journal for
Equity in Health, 2025,24(1), 57.
Ortoleva, Pietro and Erik Snowberg, “Overconfidence in
political behavior,”American Economic Review, 2015,
105(2), 504–535.
Ovadya, Aviv, “‘Generative CI’ through Collective Re-
sponse Systems,”arXiv preprint arXiv:2302.00672, 2023.
Palmer, Alexis and Arthur Spirling, “Large Language
Models Can Argue in Convincing Ways About Politics,
but Humans Dislike AI Authors: Implications for Gover-
nance,”Political Science, 2023,75(3), 281–291.
Paluck, Elizabeth Levy, Hana Shepherd, and Peter M
Aronow, “Changing Climates of Conflict: A Social Net-
work Experiment in 56 Schools,”Proceedings of the Na-
tional Academy of Sciences, 2016,113(3), 566–571.
Pavlopoulos, John, Jeffrey Sorensen, Lucas Dixon,
Nithum Thain, and Ion Androutsopoulos, “Toxicity
Detection: Does Context Really Matter?,” in “Proceed-
ings of the 58th Annual Meeting of the Association for
Computational Linguistics” Association for Computa-
tional Linguistics 2020, pp. 4296–4305.
Pei, Jiaxin, José Ramón Enríquez, Umar Patel, Alia Bra-
ley, Nuole Chen, Lily Tsai, and Alex Pentland, “Delib-
eration.io: Facilitating Democratic and Civil Engagement
at Scale with Open-Source and Open-Science,”Working
Paper, 2025.
Pennycook, Gordon, Ziv Epstein, Mohsen Mosleh, An-
tonio A Arechar, Dean Eckles, and David G Rand,
“Shifting attention to accuracy can reduce misinformation
online,”Nature, 2021,592(7855), 590–595.
Rathje, Steve, Meryl Ye, Laura K. Globig, Raunak M.
Pillai, Victoria Oldemburgo de Mello, and Jay J. Van
Bavel, “Sycophantic AI Increases Attitude Extremity and
Overconfidence,”Working Paper, 2025.
Reiljan, Andres, Diego Garzia, Frederico Ferreira Da
Silva, and Alexander H Trechsel, “Patterns of affective
polarization toward parties and leaders across the demo-
cratic world,”American Political Science Review, 2024,
118(2), 654–670.
Roy, Deb, Lawrence Lessig, and Audrey Tang, “Con-
versation Networks,”arXiv preprint arXiv:2503.11714,
2025.
14

AI-Assisted Deliberation at Scale
Santurkar, Shibani, Esin Durmus, Faisal Ladhak, Cinoo
Lee, Percy Liang, and Tatsunori Hashimoto, “Whose
Opinions Do Language Models Reflect?,” in “Interna-
tional Conference on Machine Learning” PMLR 2023,
pp. 29971–30004.
Sharma, Mrinank, Meg Tong, Tomasz Korbak, David
Duvenaud, Amanda Askell, Samuel R Bowman, New-
ton Cheng, Esin Durmus, Zac Hatfield-Dodds, Scott R
Johnston et al., “Towards Understanding Sycophancy
in Language Models,”arXiv preprint arXiv:2310.13548,
2023.
Siu, Alice, Estelle Ciesla, and Joshua Goodwin, “Delib-
erative Polling in Sub-Saharan Africa Paper,” in “Pro-
ceedings of the ACM Collective Intelligence Conference”
2025, pp. 44–57.
Small, Christopher, Michael Bjorkegren, Timo Erkkilä,
Lynette Shaw, and Colin Megill, “Polis: Scaling de-
liberation by mapping high dimensional opinion spaces,”
Recerca: revista de pensament i anàlisi, 2021,26(2).
Small, Christopher T., Ivan Vendrov, Esin Durmus, Had-
jar Homaei, Elizabeth Barry, Julien Cornebise, Ted
Suzman, Deep Ganguli, and Colin Megill, “Opportu-
nities and Risks of LLMs for Scalable Deliberation with
Polis,”arXiv preprint arXiv:2306.11932, 2023.
Sourati, Zhivar, Alireza S. Ziabari, and Morteza De-
hghani, “The Homogenizing Effect of Large Language
Models on Human Expression and Thought,”Trends in
Cognitive Sciences, 2026. Originally arXiv:2508.01491
(2025).
Steenbergen, Marco R., André Bächtiger, Markus
Spörndli, and Jürg Steiner, “Measuring Political De-
liberation: A Discourse Quality Index,”Comparative
European Politics, 2003,1(1), 21–48.
Suiter, Jane, Lala Muradova, John Gastil, and David M
Farrell, “Scaling up deliberation: Testing the potential
of mini-publics to enhance the deliberative capacity of
citizens,”Swiss Political Science Review, 2020,26(3),
253–272.
Tao, Yan, Olga Viberg, Ryan S. Baker, and René F. Kizil-
cec, “Cultural Bias and Cultural Alignment of Large Lan-
guage Models,”PNAS Nexus, 2024,3(9), pgae346.
Tessler, Michael Henry, Michiel A. Bakker, Daniel Jar-
rett, Hannah Sheahan, Martin J. Chadwick, Raphael
Koster, Georgina Evans, Lucy Campbell-Gillingham,
Tantum Collins, David C. Parkes, Matthew Botvinick,
and Christopher Summerfield, “AI Can Help Humans
Find Common Ground in Democratic Deliberation,”Sci-
ence, 2024,386(6719), eadq2852.
Tsai, Lily L., Alex Pentland, Alia Braley, Nuole Chen,
José Ramón Enríquez, and Anka Reuel, “Generative
AI for Pro-Democracy Platforms,”An MIT Exploration
of Generative AI, March 2024.
Tucker, Joshua A., Andrew Guess, Pablo Barberá, Cris-
tian Vaccari, Alexandra Siegel, Sergey Sanovich, De-
nis Stukal, and Brendan Nyhan, “Social Media, Politi-
cal Polarization, and Political Disinformation: A Review
of the Scientific Literature,” Technical Report, William
and Flora Hewlett Foundation, Menlo Park, CA March
2018.
Tudoroiu, Theodor, “Social Media and Revolutionary
Waves: The Case of the Arab Spring,”New Political
Science, 2014,36(3), 346–365.
Valgarðsson, Viktor, Will Jennings, Gerry Stoker, Han-
nah Bunting, Daniel Devine, Lawrence McKay, and
Andrew Klassen, “A Crisis of Political Trust? Global
Trends in Institutional Trust from 1958 to 2019,”British
Journal of Political Science, 2025,55, e15.
Voelkel, Jan G., Michael N. Stagnaro, James Y. Chu,
Sophia L. Pink, Joseph S. Mernyk, Chrystal Re-
dekopp, Isaias Ghezae, Matthew Cashman, Dhaval
Adjodah, Levi G. Allen et al., “Megastudy Testing 25
Treatments to Reduce Antidemocratic Attitudes and Par-
tisan Animosity,”Science, 2024,386(6719), eadh4764.
Vosoughi, Soroush, Deb Roy, and Sinan Aral, “The
Spread of True and False News Online,”Science, 2018,
359(6380), 1146–1151.
Westwood, Sean J., Justin Grimmer, and Andrew B.
Hall, “Measuring Perceived Slant in Large Language
Models Through User Evaluations,” Working Paper, Stan-
ford Graduate School of Business and Hoover Institution
2025.
Wike, Richard, “Why the World Is Down on Democracy,”
Journal of Democracy, 2025,36(1), 93–108.
Xiao, Chaojun, Jie Cai, Weilin Zhao, Guoyang Zeng,
Biyuan Lin, Jie Zhou, Zhi Zheng, Xu Han, Zhiyuan
Liu, and Maosong Sun, “Densing Law of LLMs,”Na-
ture Machine Intelligence, 2025,7(11), 1823–1833.
Young, Iris Marion,Inclusion and democracy, OUP Ox-
ford, 2002.
Zhu, Shenzhe, Shu Yang, Michiel A Bakker, Alex Pent-
land, and Jiaxin Pei, “Can AI Truly Represent Your
V oice in Deliberations? A Comprehensive Study of Large-
Scale Opinion Aggregation with LLMs,”arXiv preprint
arXiv:2510.05154, 2025.
15
