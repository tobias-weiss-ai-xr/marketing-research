---
title: 'Upskilling with Generative AI: Practices and Challenges for Freelance Knowledge Workers'
url: https://arxiv.org/abs/2604.27231
category: ai-marketing
subcategory: empirical
date: 2026-04
venue: ''
authors:
- Kashif Imteyaz
- Isabel Lopez
- Nakul Rajpal
- Hunjun Shin
- Saiph Savage
source: arxiv
pdf_url: https://arxiv.org/pdf/2604.27231
pages: 19
chars: 123565
fetched_at: '2026-11-08T13:04:39+00:00'
kb_version: 1
---

# Upskilling with Generative AI: Practices and Challenges for Freelance Knowledge Workers

Upskilling with Generative AI: Practices and Challenges for
Freelance Knowledge Workers
Kashif Imteyaz
imteyaz.k@northeastern.edu
Civic AI Lab, Northeastern University
Boston, Massachusetts, USA
Isabel Lopez
isabellhur@gmail.com
CICESE
Ensenada, Baja California, Mexico
Nakul Rajpal
rajpal.n@northeastern.edu
Civic A.I. Lab, Northeastern
University
Boston, Massachusetts, USA
Hunjun Shin
shin.hu@northeastern.edu
Civic A.I. Lab, Northeastern
University
Boston, Massachusetts, USA
Saiph Savage
s.savage@northeastern.edu
Civic A.I. Lab, Northeastern
University
Boston, Massachusetts, USA
Universidad Nacional Autonoma de
Mexico (UNAM)
Mexico City, Mexico
Figure 1: Overview of our exploratory mixed method study
Abstract
Freelance workers must continually acquire new skills to remain
competitive in online labor markets, yet they lack the organizational
training, mentorship, and infrastructure available to traditional em-
ployees. Generative AI-powered tools like ChatGPT are reshaping
market skill demands while also offering new forms of on-demand
learning support to meet those demands. Despite growing interest
in AI-powered learning tools, little is known about how freelancers
actually use these tools to learn, the challenges they encounter, and
how generative AI for learning interacts with precarity and compe-
tition in platform-based work. We present a mixed-methods study
combining a survey and semi-structured interviews with freelance
knowledge workers. Grounded in self-directed learning theory, we
examine how freelancers integrate generative AI tools into their
learning practices. Our findings show that freelancers increasingly
rely on generative AI to structure learning and support exploratory
skill acquisition, but do not treat it as their primary learning re-
source due to inconsistency, lack of contextual relevance, and ver-
ification overhead. We identify a shift fromlearning as growth to
learning as survival, where upskilling is oriented toward immediate
This work is licensed under a Creative Commons Attribution 4.0 International License.
CHIWORK ’26, Linz, Austria
©2026 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2429-9/2026/06
https://doi.org/10.1145/3808045.3808068
market viability rather than long-term development. We also sur-
face a structural challenge we terminvisible competencies, in which
workers acquire skills through generative AI tools but lack credible
ways to signal or validate these skills in competitive freelance mar-
kets. Based on these insights, we offer design recommendations for
generative AI-powered learning tools for freelancers.
CCS Concepts
•Human-centered computing → Computer supported coop-
erative work.
Keywords
Generative AI, AI for Education, Personalized Learning
ACM Reference Format:
Kashif Imteyaz, Isabel Lopez, Nakul Rajpal, Hunjun Shin, and Saiph Savage.
2026. Upskilling with Generative AI: Practices and Challenges for Free-
lance Knowledge Workers. InProceedings of the 5th Annual Symposium on
Human-Computer Interaction for Work (CHIWORK ’26), June 22–25, 2026,
Linz, Austria.ACM, New York, NY, USA, 19 pages. https://doi.org/10.1145/
3808045.3808068
1 Introduction
Freelance knowledge workers face persistent challenges in main-
taining the ongoing skill development required to remain com-
petitive in online labor markets [ 13]. Unlike traditional corpo-
rate employees, who often benefit from institutional support such
as structured AI literacy workshops, supervised tool onboarding,
arXiv:2604.27231v1  [cs.HC]  29 Apr 2026

CHIWORK ’26, June 22–25, 2026, Linz, Austria Imteyaz et al.
peer learning cohorts, or mentorship aligned with organizational
goals [21, 125, 134], freelancers must independently identify, eval-
uate, and acquire new skills to sustain their livelihoods [ 12, 24].
Without access to organizational infrastructure or formal guidance
[100, 125], freelancers bear full responsibility for managing their
own learning trajectories [3, 13]. This burden is intensified by the
competitive nature of freelance platforms [58, 100], where sharing
knowledge about effective upskilling strategies may directly un-
dermine one’s own economic opportunities [90, 126]. As a result,
peer learning practices that are common in traditional workplaces
become difficult to sustain when workers are competing for the
same contracts [81].
These long-standing challenges have become more urgent with
the rapid advancement of Large Language Models (LLMs) such
as ChatGPT and other AI-powered learning tools. LLMs are re-
shaping knowledge work across domains [18, 88, 113], introducing
new forms of work while simultaneously redefining the skills re-
quired to perform existing tasks [42, 104, 134]. As these systems
become increasingly integrated in everyday knowledge-based la-
bor [44, 93], freelancers must not only learn how to use new AI
tools, but also develop novel competencies such as prompt design,
AI-assisted content production, and the integration of LLM out-
puts into client-facing deliverables [66, 92, 104]. These pressures
are further amplified by the continued expansion of the freelance
economy [19, 117]. By 2025, more than 1.56 billion people globally
engaged in freelance or independent work, reflecting a large-scale
shift toward contingent and flexible labor arrangements [108, 117].
In this context, the ability to learn and adapt quickly is no longer
optional but central to freelancers’ economic survival.
At the same time, LLMs present a paradox: while they increase
uncertainty by accelerating skill obsolescence and intensifying
competition [1, 7, 112], they also create new opportunities for per-
sonalized, on-demand learning support [59, 105]. However, most
existing generative AI learning systems are designed for traditional
organizational settings [79], assuming stable employment struc-
tures, managerial guidance, and collective learning environments
[15, 32]. As a result, little is known about how LLMs are reshaping
learning practices for freelance workers who operate outside these
institutional contexts. We lack empirical understanding of how
freelancers use LLMs to learn, what challenges they encounter, and
how AI-mediated learning intersects with precarity, competition,
or self-directed work. Understanding these dynamics matters, as
learning infrastructures that fail to account for freelance realities
risk widening inequalities in access to skills, income stability, and
long-term career mobility. Studying how LLMs are transforming
the learning landscape for freelance workers is therefore essential
for designing AI-assisted learning systems that genuinely support
independent workers rather than exclude them.
While freelancers have always faced challenges in self-directed
learning [12, 13], AI-mediated learning introduces new dynamics
that prior work has not examined [97]. First, the learning resource
itself is generative and opaque [132], producing content without
provenance or editorial review [97], which shifts the learner’s bur-
den from finding resources to verifying them [94, 122]. Second, skills
acquired through AI-mediated learning leave no social trace and
attribution [46, 91, 125], making them uniquely difficult to signal
in markets that rely on credentials and peer endorsement [31, 81].
Our contribution lies in identifying what changes when freelancers’
learning is mediated by generative AI systems with these charac-
teristics.
To address this knowledge gap, we conducted a mixed-methods
study combining survey data (n=71) and follow-up interviews
(n=20) with platform-based knowledge workers, professionals who
perform information-based tasks such as writing, data analysis,
design, and software development. We ground our analysis in self-
directed learning theory [ 38], which is particularly well-suited
for understanding how freelancers adapt to rapidly evolving land-
scapes. Self-directed learning theory conceptualizes learning as
a process where individuals take primary responsibility for plan-
ning, conducting, and evaluating their learning experiences [38].
Since freelancers typically lack access to formal training, men-
torship, and support systems available to traditional employees
[11], they must take full responsibility for their learning by setting
goals, identifying resources, and evaluating progress. Self-directed
learning’s emphasis on real-world problem-solving and practical
application provides a useful lens for examining how freelancers
navigate constant upskilling pressures in competitive and isolat-
ing environments. Fig. 1 presents an overview of our study. Our
research focuses on the following research questions:
(1) How do freelance knowledge workers approach skill de-
velopment in work environments increasingly shaped by
generative AI adoption?
(2) What barriers do freelancers encounter when trying to access
learning opportunities for skill development in AI-driven
work environments?
(3) How do freelancers envision future learning tools that can
support their skill development in the context of widespread
generative AI adoption?
In our mixed-methods study, we found that freelancers increas-
ingly use generative AI tools to support skill development. In partic-
ular, they rely on these tools to structure learning plans that break
skills into manageable steps and fit learning into demanding work
schedules. We also observed a shift towardlearning-as-survival,
where upskilling is oriented toward immediate market viability
rather than long-term professional growth.
At the same time, freelancers did not treat generative AI as their
primary or fully trusted learning source. A key limitation they felt
with generative AI tools was the lack of contextual personaliza-
tion. LLM-generated learning content often felt generic and did not
reflect freelancers’ specific, situated needs [45]. To fill this gap, free-
lancers turned to peer learning for more relevant, experience-based
knowledge. However, peer learning was constrained by the com-
petitive nature of freelance work, which made many freelancers
hesitant to share what they know [6]. Within this landscape, free-
lancers increasingly described generative AI as a lower-risk option
for exploratory learning, enabling them to learn and test skills pri-
vately while relying on peers for validation, access to opportunities,
and legitimacy-building.
We also found that AI-based learning introduced additional bur-
dens for freelancers. While prior work has noted that generative AI
can introduce new costs alongside productivity gains [106], we find
that these costs are amplified and reconfigured in freelance learning
contexts. Freelancers reported information overload, inconsistent

Upskilling with Generative AI: Practices and Challenges for Freelance Knowledge Workers CHIWORK ’26, June 22–25, 2026, Linz, Austria
guidance, and the need to verify AI-generated content, increasing
the effort required to learn effectively. Beyond these verification
demands, freelancers described a structural challenge that we call
invisible competencies. Although freelancers can acquire real skills
through AI-assisted learning, these capabilities are often difficult
to signal or validate in freelance labor markets. Concerns about
reputation, along with the risks of visible experimentation, further
discourage open learning [51, 57, 78].
In response, freelancers envisioned generative AI–based learning
tools that reduce verification burden, support strategic learning un-
der market pressure, and help translate AI-acquired skills into clear
and credible signals of competence for clients. Based on our find-
ings, we provide design recommendations for building generative
AI-based learning tools that better meet the needs of freelancers.
In this paper, we contribute:
• A mixed-methods study of freelancers’ upskilling practices,
examining how generative AI is used as a learning resource
in competitive, platform-mediated work contexts.
• A conceptual framing of freelancer upskilling that charac-
terizes a shift from learning-as-growth towardlearning-as-
survival, and identifyinvisible competenciesas a key conse-
quence of AI-assisted learning, where genuinely acquired
skills remain difficult to demonstrate or validate in freelance
labor markets.
• Design recommendations for future generative AI tools that
better support freelancers’ learning needs, grounded in free-
lancers’ own experiences and aspirations.
2 Related Work
Our research focuses on the algorithmic management of platform
labor, AI-driven job displacement, self-directed learning theory,
and the use of AI for upskilling. We review each area to situate our
study on how freelancers navigate upskilling.
2.1 Algorithmic Management and Platform
Labor
Platform-mediated freelance knowledge work is structured by al-
gorithmic systems that shape workers’ visibility, evaluation, and
access to economic opportunities [78, 126]. Research shows that
algorithmic management allows for managerial control through
ranking systems, automated task allocation, and data-driven over-
sight, which alters everyday decision making [72, 78]. Prior research
on platform-based work shows that workers experience workplace
surveillance, information asymmetries, and opaque algorithmic
processes under asymmetric power dynamics [ 30, 133]. Within
these systems, reputation metrics and client reviews function as
core mechanisms of algorithmic management [57, 126]. Freelancers
place substantial economic value on maintaining strong ratings
[26, 47], which can constrain upskilling by discouraging them from
taking on projects that require skills they are still developing. Plat-
form work is also marked by broader forms of precarity, including
emotional labor and the absence of institutional support [76, 82].
Recent work shows that freelance workers seek ways to reclaim
their agency within these systems [55, 135], from designing worker-
controlled data institutions to articulating principles for more trans-
parent and worker-centered algorithmic management [48, 109, 133],
and calling for institutional and policy-level reforms to address
algorithmic opacity and power asymmetries [ 83]. This body of
work positions platform labor as a sociotechnical environment that
directly shapes learning: algorithmic instability discourages long-
term skill investment, reputational risk makes freelancers reluctant
to experiment with unfamiliar skills in client-facing work, and lim-
ited structural support means they must navigate these decisions
alone [20, 62, 126, 127, 133].
2.2 AI Automation and Job Displacement
Understanding AI automation and job displacement has become
increasingly critical as Large Language Models (LLMs) and agen-
tic tools fundamentally transform knowledge work [5, 18, 44, 85].
Unlike previous automation waves that primarily affected manual
labor [7], current LLM-based tools such as ChatGPT and Claude
demonstrate unprecedented capabilities in automating entry-level
cognitive tasks and routine knowledge work [103], roles that tra-
ditionally served as gateways to professional careers [ 121, 129].
This shift introduces immediate competitive pressures, particularly
for vulnerable worker populations lacking institutional support
[30, 35, 54, 111, 127]. Platform-mediated labor markets show mea-
surable disruption within months of new LLM releases. On Upwork,
writing-related freelancers experienced a 2% drop in monthly jobs
and a 5.2% drop in monthly earnings following ChatGPT’s release,
with image-related freelancers seeing even steeper declines after
DALL-E 2 and Midjourney [52]. Recent HCI research highlights the
complex dynamics of augmentation, automation, and adaptation
beyond simplistic replacement narratives [54, 70, 129, 131].
However, existing studies largely focus on macroeconomic trends
and platform analytics [18, 29, 114], offering limited insight into
how individual freelance workers respond to these disruptions.
From an HCI perspective, this gap underscores the need to un-
derstand how freelancers engage in situated strategies to remain
viable in an AI-disrupted labor market [103, 131]. Specifically, little
is known about how freelancers adapt to AI-driven disruptions or
develop strategies to upskill and remain competitive.
2.3 Self-Directed Learning in Freelance Context
Self-directed learning (SDL) theory provides a framework for un-
derstanding how freelancers navigate skill development without
institutional support. Garrison [38] defines SDL as a process where
learners take primary responsibility for planning, conducting, and
evaluating their learning experiences. The framework comprises
three interrelated components:self-management(structuring and
organizing learning activities),self-monitoring(evaluating and re-
flecting on progress), andmotivation(sustaining effort and goal ori-
entation). This framework emphasizes learner autonomy in setting
goals, selecting resources, and monitoring progress, characteristics
that align with the independent nature of freelance work [100]. SDL
has been recognized as crucial for preventing skill obsolescence
and supporting upskilling in volatile economic conditions [80].
However, freelancers’ self-directed learning occurs under struc-
tural constraints [ 43]. Unlike traditional employees who access
skill development through formal training, peer learning cohorts,
curated resources, and protected experimentation time [ 71, 73],

CHIWORK ’26, June 22–25, 2026, Linz, Austria Imteyaz et al.
freelancers must independently identify skill gaps, fund their up-
skilling, and integrate learning into immediate income-generating
work [24]. Research identifies four key overheads that shape free-
lancer learning [13]:financial overheadfrom income volatility;emo-
tional overheadfrom self-management stress and isolation [ 30];
relational overheadfrom limited mentorship [ 12, 126]; andreputa-
tional overheadfrom continuous impression management, where
single negative reviews carry long-term consequences [126, 133].
Critically, freelancers lack thesocial validationthat organizational
contexts provide: the ability to observe peers, ask questions, and
develop shared norms about appropriate AI use [63, 125, 130].
In the absence of institutional support, peer learning becomes
a potentially valuable resource for freelancers [ 24]. Research on
peer learning typically assumes collaborative environments where
knowledge sharing is mutually beneficial [95, 116]. However, com-
petitive freelance markets complicate these assumptions. Platform
dynamics, including algorithmic visibility, public profiles, and bid-
ding systems, position freelancers as direct competitors, incentiviz-
ing knowledge hiding to preserve competitive advantage [6, 37, 78].
This makes visible experimentation costly and encourages selec-
tive reciprocity over open sharing [33]. Despite these barriers, peer
learning offers something that other learning resources may not:
situated knowledgegrounded in identifiable individuals with known
experience and professional trajectories [45, 50]. Situated knowl-
edge research emphasizes that knowledge claims are accountable
to the social and professional conditions under which they are
produced [45]. For freelancers navigating uncertain information
landscapes, knowingwhoproduced knowledge, and under what
conditions, may be as important as the knowledge itself. Yet sys-
tematic understanding of how freelancers balance peer learning
benefits against competitive risks [36, 43, 89], and how this inter-
sects with emerging AI learning tools, remains limited.
2.4 AI for Upskilling: Opportunities and
Tensions
While LLMs and AI agents introduce job displacement pressures
[106, 121], they simultaneously offer unprecedented opportunities
for personalized, accessible learning [105, 123]. In HCI and learning
sciences, researchers have long explored how intelligent systems
can support skill development through adaptive tutoring [4], intel-
ligent feedback [68], and personalized learning paths [17]. These
approaches build on scaffolding theory [120], temporary support
structures that enable learners to achieve beyond their independent
capabilities [96, 128]. Recent advances in LLMs have expanded these
possibilities, enabling on-demand explanations, code generation
for learning programming [ 60, 77], and conversational learning
partners [23, 75, 123]. However, applying scaffolding principles
to freelance learning reveals unique challenges. The concept of
"fading" support as competence develops becomes complex when
errors directly impact earnings and platform ratings [133]. LLMs
often fail to balance what Reiser [98] terms structure versus prob-
lematization: they either over-scaffold through complete task com-
pletion (reducing learning opportunities) or under-scaffold through
generic advice (failing to address specific skill gaps). Additionally,
freelancers face challenges in evaluating LLM generated content
quality, particularly when AI systems produce plausible-sounding
but incorrect information [28, 122]. This "verification burden" is
especially acute for freelancers who must spend time validating
learning materials [24, 115].
While LLMs can provide personalized instruction, it cannot repli-
cate the motivational and social benefits of human peer learning
[36, 99]. Despite growing research on LLM-based learning tools
[97], we lack an integrated understanding of how to design AI
learning systems that address the unique constraints and compet-
itive pressures that freelancers face while engaging in upskilling
practices.
2.5 Research Gap
While prior work offers valuable insights across these domains,
the literature remains largely separate. Research on platform labor
documents how algorithmic systems shape freelancer behavior but
rarely examines learning practices. Studies of AI-driven displace-
ment identify macroeconomic trends but offer little insight into how
individuals actually adapt. Self-Directed Learning theory offers a
useful framework for autonomous learning, though it has not been
applied to contexts where learners face simultaneous competitive
pressure, reputational risk, and rapidly evolving tools. HCI research
has produced promising AI-powered learning systems grounded in
scaffolding theory, but these have primarily targeted institutional
contexts with built-in social support. Our study examines what
happens in the gap between these literatures: how platform-based
freelancers who lack institutional infrastructure, compete directly
with peers, and face algorithmic reputation pressures, use genera-
tive AI tools for self-directed upskilling.
3 Method
Our IRB-approved study employed a sequential mixed-methods
design [2, 27, 56]. Initially, data were collected through an online
survey, which contained both open-ended and closed-ended re-
sponses. Following this, we conducted interviews with subset of
survey respondents. This approach allowed us to first identify broad
patterns in the freelancer’s upskilling approach, then explore the
underlying mechanisms and contexts through in-depth interviews.
3.1 Participants and Recruitment
A total of 71 individuals participated in the survey. The majority of
respondents were between the ages of 25–34 (55%), with an almost
equal distribution of gender: 52.1% identified as female and 46.5% as
male, while one participant chose not to disclose their gender. Most
participants held at least a bachelor’s degree, with 60.6% reporting
this as their highest level of education. The respondents varied
widely in terms of professional background, freelancing experience,
and hours dedicated to freelance work (see Table 2 in Appendix).
Freelance roles were diverse, with the most common areas being
content creation and writing (n = 16), followed by data analysis (n
= 13), consulting (n = 9), digital marketing (n = 6), Design/Creative
Work (n = 5), and software development (n = 5). Additional roles
included Virtual assistance/administrative support, customer sup-
port/AI automation scriptwriting, and product management. We
recruited participants for our study by creating a job posting on
Upwork, a prominent freelance platform [ 13]. Eligibility criteria

Upskilling with Generative AI: Practices and Challenges for Freelance Knowledge Workers CHIWORK ’26, June 22–25, 2026, Linz, Austria
required participants to: (1) have at least one year of active experi-
ence on a freelancing platform, (2) have used Generative AI tools
for upskilling, and (3) be proficient in English. Additionally, partici-
pants must have engaged in upskilling practices within the last six
months to advance their freelancing careers. We define upskilling
as deliberate efforts to acquire new skills or deepen existing ones
for professional purposes, such as taking online courses, using AI
tools to learn techniques, engaging in peer knowledge exchange,
obtaining certifications, or self-directed practice with new tools or
technologies [8]. These criteria ensured participants had both lon-
gitudinal platform experience and recent upskilling insights. Our
survey sample reflects the practical constraints of recruiting from
a freelance platform with specific eligibility requirements. Consis-
tent with our sequential mixed-methods design [ 27], the survey
was not intended to produce population-level generalizations but
to identify broad patterns in freelancers’ upskilling practices that
would inform the subsequent interview phase.
We invited 20 survey respondents to participate in interviews
using purposive sampling to better understand the reasons behind
the patterns observed in the survey data [14, 22]. Three findings
specifically shaped our interview focus and participant selection:
(1) the gap between high AI tool adoption and low preference for
AI-based learning, (2) the tension between frequent peer learning
practice and low preference ratings, and (3) participants’ open-
ended descriptions of AI-related challenges that needed deeper
exploration. We selected interview participants by first stratifying
the survey pool along three dimensions: freelance domain, years of
freelancing experience (1-2 years to 5+ years), and AI tool usage
intensity (low, moderate, high). We prioritized ensuring coverage
across all freelance domains represented in the survey, then within
each domain, selected participants who varied in experience level
and AI usage. When multiple candidates met the same criteria, we
prioritized those whose open-ended survey responses suggested
they could provide richer accounts of the tensions identified in the
survey data (see Table 3 in the appendix).
3.2 Data Collection
We developed and distributed an online survey using Google Forms.
The survey included a mix of question types: multiple-choice, Likert
scale, checkbox selection, and open-ended responses. Closed-ended
response options were developed through a two-step process. First,
we compiled survey items from prior research on freelancer skill
development [13, 24] and platform labor challenges [126]. For fea-
tures valued in AI learning tools, items were informed by both
prior work and established learning frameworks, including self-
directed learning [38], experiential learning [69], and principles of
adult learning [67]. For example, personalized learning paths re-
flect self-directed learning’s emphasis on learner autonomy, while
project-based practice exercises align with experiential learning
principles. We supplemented each item set with an "Other" option
and an open-text field, allowing participants to identify features or
barriers not captured in the predefined list.
The survey was divided into six sections: Demographics, Pro-
fessional Background, Current Upskilling Practices, Peer Learning
Challenges and Benefits, Learning Preferences and Needs, and Cur-
rent Use and Opportunities of AI. We conducted semi-structured
interviews guided by a protocol aligned with the survey items but
designed to elicit deeper insights. On average, each session lasted
approximately 60 minutes. All interviews were conducted online
via Zoom and recorded for analysis. Interviews both confirmed
survey-identified patterns and surfaced additional needs beyond
the predefined options.
3.3 Analysis
To analyze the quantitative data collected from the survey, we fol-
lowed standard statistical analysis techniques and reported the
frequency of responses in different categories [64]. Closed-ended
questions related to current upskilling practices, learning prefer-
ences, and patterns of use of AI tools were analyzed using descrip-
tive statistics in RStudio.
For our qualitative data, which included interviews and open-
ended responses, we followed the practices of reflexive thematic
analysis [16], conducting a bottom-up analysis of our interview
transcripts and open-ended survey responses. Two researchers in-
dependently open-coded separate halves of the transcripts, focusing
on our research questions regarding freelancers’ upskilling prac-
tices, meeting bi-weekly to discuss emerging patterns, refine the
codebook, and resolve disagreements through consensus. Consis-
tent with Braun and Clarke [16], we did not compute inter-rater
reliability, focusing instead on interpretive depth and reflexive en-
gagement. After open coding, we iteratively grouped codes into
higher-level themes through axial coding, examining relationships
between codes and their relevance to freelancers’ upskilling pro-
cesses. We continued analysis until thematic saturation was reached
[74], with no substantially new insights emerging in the final in-
terviews and themes well supported across the data. This process
produced 19 axial codes, which we synthesized into 6 core themes
that structure our findings. Throughout, we maintained reflexive
memos documenting analytical decisions. Participant quotes are
anonymized as P followed by participant ID. Our initial coding
was bottom-up and data-driven. SDL entered the process during
later stages of theme development, when we used Garrison’s three
components (self-management, self-monitoring, and motivation) as
interpretive lenses to contextualize emergent themes and structure
the discussion [38].
4 Survey Results
We present both closed-ended and open-ended survey results that
describe freelancers’ perceived impact of AI on their work, patterns
of upskilling, and AI-based learning preferences.
4.1 Impact of AI in Freelance Work
In our sample, all participants reported that AI was influencing
their day-to-day work. Figure 2 shows the distribution of these
ratings. Over half (57%) reported that AI had a significant impact
on their work in the past year (rating 5/5); the remaining 43% rated
the impact between 2 and 4 on a five-point scale (1 = no impact, 5
= significant). No respondent selected ‘no impact’.
To contextualize this impact, we also posed an open-ended ques-
tion inviting participants to describe their own perceptions of the
positive or negative impact of generative AI on their freelance work.
Through inductive thematic coding, we identified the main themes.

CHIWORK ’26, June 22–25, 2026, Linz, Austria Imteyaz et al.
Figure 2: Perceived impact of AI on freelance work over the
past year, rated from 5 (significant impact) to 1 (no impact).
Table 1 summarizes these findings, showing each type of impact, a
brief description, the number of freelancers who mentioned it, and
a sample quote from their responses.
The most frequently discussed positive impacts wereLearning
& Skill DevelopmentandIncreased Efficiency & Productivity, high-
lighting AI’s role in accelerating skill acquisition and helping free-
lancers complete tasks more efficiently. Other positives included
Improved Quality of Output, where freelancers noted AI’s ability to
enhance their products;Creative Support & Idea Generationwhere
they used AI as a brainstorming partner; andExpanded Opportu-
nities, where AI enabled them to offer new services. Across the
corpus of responses, positive mentions of AI’s impact (124) slightly
exceeded negative ones (110). Yet these benefits also came with
some concerns: the most prominent negative impacts, such asIn-
creased Market Competition, Over-reliance on Technology, and Skill
Degradation, indicate that freelancers see AI not only as a tool for
greater productivity and skill growth, but also as a potential desta-
bilizing force in their professional landscape. Additional concerns
includedQuality Concerns with AI Outputs,Job Security Concerns,
andCost Barriers.
After identifying their perceptions of the impact of AI, we exam-
ined how freelancers actually used AI in their daily work. Note that
Table 1 captures freelancers’ perceived impacts of AI (what they
believe AI does for them), while Figure 3 captures their reported
uses (what they actually do with AI). The gap between perceiving
AI as beneficial for learning (n=30, Table 1) and actively using it
for skill expansion (12%, Figure 3) became a focus of our interview
investigation. Figure 3 illustrates the different use cases and the
percentage of freelancers who selected each option from a select-all-
that-apply item. The options were drawn from prior research [44],
though participants could also select “other” and provide additional
examples. Nearly half (47%) reported using AI for creative support,
such as idea generation and brainstorming, followed by proposal
and pitch creation (20%). Individual freelancers also wrote in that
they used AI to summarize content, manage projects, clarify job
postings, communicate with clients, and cross-check their work.
The impact of a technology can also be measured by the time
people spend using it. Freelancers in our study reported dedicat-
ing more than one-fourth of their work time to AI. When asked
what percentage of their freelance work involved AI tools, most
participants (about 70%) said they used AI tools from one-quarter to
three-quarters of their time. A smaller group (18%) reported using
AI less than one-quarter of the time, and 11% mentioned using it
more than three-quarters of the time.
Figure 3: Self-reported purposes for using AI tools such as
ChatGPT and Claude in freelance work.
While freelancers use AI to support their work, they also face
barriers to its efficient use. When asked to select from a list of poten-
tial obstacles, the most frequently selected response was the rapid
pace of change (20.5%). This was followed by the cost of learning re-
sources (19.2%) and information overload (17.4%). Other frequently
mentioned obstacles included a lack of structured guidance (14. 7%),
time constraints (14. 3%), and difficulty in identifying relevant skills
(12. 1%). Individual representatives also mentioned issues such as a
lack of time, the release of new AI tools with varying capabilities,
difficulty in identifying the right tools, and the presence of too
many AI tools.
These diverse impacts create the context for our central focus,
understanding how freelancers approach learning when faced with
such disruption. We now turn to examining their upskilling pat-
terns.
4.2 Patterns of Upskilling and Preferences for
AI-Supported Learning
Freelance workers reported actively investing time in skill develop-
ment. In our study 29.6% reported participating in upskilling daily,
and another 29.6% weekly. Additionally, nearly half (48%) reported
spending between 2-5 hours per week learning new skills for their
freelancing careers, while 24% reported spending more than 6 hours
a week. These patterns align with the Upwork Research Institute’s
2025 Future Workforce Index. The report notes that 32% of skilled
workers (freelancers and Full Time Employees) say they are “learn-
ing new skills all the time, ” and that 87% of freelancers (vs. 82% of
FTEs) learned a new skill in the past six months [118].
Choosing which area to focus on for upskilling is not random.
When asked what skills they believed they needed to develop in
the next 1-2 years, around 39% of participants mentioned AI.
In terms of which methods they choose for upskilling, in a sin-
gle select-all-that-apply item, freelancers generally preferred self-
directed approaches, choosing video tutorials (85.9%; e.g., YouTube)
and AI learning tools (70.4%) over peer learning (64.7%) and other
community-learning methods. Nearly half of freelancers choose on-
line courses (49.3%), identifying specific programs such as Udemy,
Coursera, skool.com, and LinkedIn Learning, which encompass
both self-directed courses and community-learning programs. Fi-
nally, 42.3% selected Industry Blogs/Articles, which is lower than
the other categories but also shows value for learning from others,
potentially more experienced freelancers.

Upskilling with Generative AI: Practices and Challenges for Freelance Knowledge Workers CHIWORK ’26, June 22–25, 2026, Linz, Austria
Table 1: Positive and Negative Impacts of Generative AI on Freelance Knowledge Workers
# Theme Summary Count Representative Quote
POSITIVE IMPACTS OF AI
1 Increased Efficiency & Productivity Automation and speed for tasks like
writing, coding, proposals, etc.
29 “AI has made work faster and more effi-
cient. It helps me draft content, organize
tasks”
2 Learning & Skill Development Helps learn new tools, coding, and
improve professional skills
30 “Learning new skills using AI is easy and
time efficient”
3 Improved Quality of Output Polishes communication, improves
deliverables, boosts client satisfac-
tion
25 “It has saved me a lot of time. Has im-
proved my communication skills”
4 Creative Support & Idea Generation Supports brainstorming, breaks cre-
ative blocks, offers varied ideas
24 “It allows me to get going with brain-
storming rather than staring at a blank
page”
5 Expanded Opportunities Enables offering new services like
AI-content or automation
16 “AI has enabled me to offer specialized
services, like AI-powered solutions”
NEGATIVE IMPACTS OF AI
6 Increased Market Competition Beginners using AI create more
competition, potentially lowering
rates
33 “Beginners can now use AI to perform
tasks that once required deep expertise,
sometimes lowering gig rates”
7 Unrealistic Client Expectations Clients expect faster and cheaper
work assuming AI replaces human
expertise
13 “Sometimes it feels like clients expect ev-
erything to be done by AI, even the hu-
man touch”
8 Over-Reliance & Skill Degradation Heavy reliance on AI can lead to
reduced confidence and creativity
25 “Sometimes I catch myself depending on
AI for tasks I used to do confidently”
9 Quality Concerns with AI Outputs AI output hallucinates and requires
corrections
10 “I wasted time whenever the response had
many hallucinations”
10 Job Security Concerns Freelancers worry about being re-
placed or becoming obsolete
18 “I’m afraid of becoming obsolete, my
client might prefer using AI instead of
hiring me”
11 Cost Barriers Advanced AI tools are expensive for
some freelancers
11“It is expensive to use better Gen AI”
Professional certifications were also included in the response
options for this item, to capture freelancers’ interest in formal
recognition, consistent with prior studies exploring how and why
freelancers engage in professional development [13]. Although cer-
tification is not a direct method of upskilling, but rather a broader
category encompassing credential-based learning practices, it was
selected by 22 participants (31%). This suggests that for roughly
one-third of freelancers, obtaining certification is perceived as valu-
able. This emphasis on certification reflects an early indication of
a broader challenge that recurs throughout our findings. While
freelancers frequently described gaining practical skills through
self-directed and AI-supported learning, these skills were not al-
ways legible to clients or platforms without formal credentials. As
a result, participants often viewed certifications less as sites of
learning and more as mechanisms for making AI-acquired capa-
bilities visible and credible in the market. This tension indicates
what we later conceptualize as invisible competencies: skills that
freelancers genuinely develop, but struggle to signal or validate
within competitive freelance labor markets.
To compare actual practices with preferences, we asked free-
lancers to rate six learning methods on a 1–5 scale, where5indi-
cated a strong preference. We then calculated the percentage of
participants rating each method a4or5. As shown in Figure 4, the
most highly preferred approach was self-paced online courses, with
about 70% of respondents rating it positively, followed by project-
based learning (66%), underscoring a strong preference for flexible
and hands-on formats. One-on-one mentoring (58%) and AI-guided
adaptive learning (54%) were moderately favored. Although men-
toring received more top scores than AI-guided learning, the latter
showed broader acceptance overall, with higher mid-range ratings
(2s and3s) and no respondents rating it as1. Peer learning groups
received the lowest endorsement (44%). Overall, the distribution
of responses highlights substantial variation in individual learning
preferences across the sample.
Although AI-adaptive learning was not the most highly rated
method used by participants for upskilling, when asked how in-
terested they would be in using an AI-powered learning tool to
master skills 82% of participants responded very interested (13%
somewhat interested, 3% not very interested, and 3% neutral). A
follow-up question was included to explore further what features

CHIWORK ’26, June 22–25, 2026, Linz, Austria Imteyaz et al.
Figure 4: Preferred methods for learning new skills, rated
from 1 (lowest) to 5 (highest).
Figure 5: Features valued most in an AI-powered learning
tool. Respondents were asked to select their top three.
participants would most value in an AI-powered learning tool. The
most frequently selected features (Figure 5) included personalized
learning path (24. 1%), project-based practice exercises (19. 4%), and
progress tracking (14. 2%). Followed by real-time skill gap analysis
(12.9%), industry trend updates (11.2 %), certification preparation
(10.3%), and peer collaboration features (7.76%).
In sum, freelancers are active upskillers who increasingly view
AI as important for their learning needs. Yet, while 70.4% of free-
lancers currently use AI tools for upskilling, this method ranks
in the middle, compared to project-based learning and self-paced
online courses (see Fig. 4). However, more than 80% of freelancers
expressed a strong interest in an AI learning tool that would provide
personalized learning paths and project-based exercises. This sug-
gests that, despite their current use of AI tools for skill development,
existing options may not fully meet their needs for personalization
and practical experience.
5 Interview Results
We present the core themes that emerged from our qualitative
analysis, organized into five subsections:
5.1 Drivers for Learning New Skills in an
AI-Driven Labor Market
Despite the growing influence of AI in reshaping digital labor across
various fields [ 44], we found that freelancers’ upskilling efforts
were not primarily driven by AI as a technological frontier. Instead,
their learning remained anchored in client demands. However, AI
amplified and destabilized this client-driven dynamic in ways that
distinguish it from earlier cycles of tool adoption. For example,
P16 explained that they had to learn various project management
and collaboration tools because their clients expected them to use
those platforms:"The biggest challenge I face [in upskilling myself]
is sometimes it’s difficult to know what kind of tool is really relevant
[to learn] because client A can say, ’We are using Monday.com [a
project management tool], ’ and you learn Monday.com. Client B says,
’We are using Trello [another project management tool], ’ so you have
to learn again. Then client C comes with Basecamp [another project
management tool]. The client will not switch their subscription because
of you. So you just have to keep learning the different tools. "
Similarly, P5 explained that their learning was driven by mar-
ket demand, specifically the types of jobs clients were requesting.
Their motivation to upskill was not based on the release of new AI
technologies. Instead, they would analyze the kinds of jobs clients
wanted and then identify the skills they needed to complete those
jobs more effectively. This client-centered approach guided their
decisions about what to learn:"So this is a kind of a mix [my learn-
ing is driven by a kind of mix], a mix between market demand and
whatever new skills I stumble upon during my work that I feel like
if I learn them [learn the skills], it will make my work much easier.
So, for example, I talked about web scraping. This was my first skill
that I learned as a freelancer. And I learned it [learned the skill of web
scrapping] because it was, it has, it had the highest demand [many
clients were posting jobs related to web scrapping]. "
While client demand remained the primary driver of skill de-
velopment, AI reshaped the conditions under which freelancers
interpreted and responded to those demands. Freelancers described
AI as a background condition that intensified uncertainty about
what to learn and how long any given skill would remain valuable.
The pace of AI tool proliferation created a form of decision fatigue
distinct from earlier periods of technological change: freelancers
were contending with a rapid and unpredictable expansion of the
tool landscape itself, not just learning new tools as clients adopted
them. This stress came less from the tools themselves than from the
fear that clients would soon expect mastery of rapidly evolving AI
technologies. Consequently, freelancers often felt overwhelmed by
the constant pressure to stay current and worried that skills they
had invested time in learning might quickly become obsolete. As P4
emphasized:“I have felt very overwhelmed because...I may be trying
to master one skill on Google Ads. But, even before you can master
everything [on the AI-driven platform of Google Ads], TikTok Ads is
already there...Then there are X Ads, LinkedIn Ads. So it can be so
overwhelming because you’re trying to ask yourself, where should I
focus? And to have a competitive edge, you need to have one focus,
one niche. And sometimes the industry evolves so fast that some of
these skills end up becoming obsolete... "
This anxiety went beyond general concern about technologi-
cal change. Participants recognized that AI could create new skill
requirements and devalue existing expertise at the same time.

Upskilling with Generative AI: Practices and Challenges for Freelance Knowledge Workers CHIWORK ’26, June 22–25, 2026, Linz, Austria
5.2 Leveraging AI to Structure Learning Goals
and Integrate Them into Workflows
Our survey revealed that freelancers were beginning to use AI tools
to support their learning and skill development, the interviews
offered deeper insight into how freelancers actually did this. A
common approach was using AI to create personalized learning
roadmaps. Freelancers described asking AI to break down complex
learning goals into smaller, manageable steps tailored to their spe-
cific needs. They also used AI to help turn these small learning tasks
into actions they could incorporate into their daily work. Instead
of treating upskilling as a separate effort, freelancers used AI to
integrate learning into their regular workflows in a practical and
sustainable way. Participant P7 described this process:"So, the first
process is that I use AI to brainstorm what to learn...after using AI
to brainstorm, I tell the AI system I use, to give me a detailed and
organized checklist, breaking everything into a step by step section of
how I will go about learning each topic leading to a skill. That means
the AI is going to break everything down for me into segments that I
can take my time every day to learn. "
Part of the reason freelancers used AI to structure their learn-
ing process and find ways to integrate learning into their work
schedules was that they typically juggle multiple activities as part
of their freelancing responsibilities. AI thus became essential in
helping them organize their learning and seamlessly incorporate it
within their busy work schedules. P1 shared some of this reasoning:
"Sometimes it gets overwhelming when you have to juggle between
your timing, workload and learning. I leverage some AI tools to help
me to learn faster. I do, I use AI to structure my learning. I use them
to prioritize and structure my day for a particular period of time".
Given that freelancers valued AI tools that could help structure
learning into their daily workflow, participants also imagined future
AI systems that could track their progress in learning a skill and
then match them with jobs or projects to help them practice or
further develop that skill. For example, participant P5 described
the following:"For the more abstract topic, practical experience is
in my opinion, the only way to learn. Because an explanation video,
as I said before, makes you better understand what this topic is, but
not actually how to do so. So if an AI agent for example, generates a
problem for me, generates a project for me to do or finds a gig about
it, and then guide me through this project, if I am stuck on certain
parts, then this will certainly help".
This strategic approach of using AI to structure learning within
their everyday work schedules extended to using AI for targeted
skill acquisition and quick concept clarification. P2 described this
approach:"...I am actually using, using ChatGPT to just be like, hey,
I’m learning Go [a programming language]. Give me a rundown of
the syntax [structure of the programming language]. And then it does
that [gives them an overview of the programming language and its
syntax]".
Freelancers also described using AI to help them structure their
learning in ways that better matched their preferred learning styles,
even when these styles could be relatively complex. One participant
(P6) articulated their approach:"...and something that I do like with
ChatGPT and learning Spanish [a language they were learning to get
new gigs], [is that] I am very aware of how I learn best based off of
experimenting a lot... so, I know systems and structures that help me
focus well. And so with this, I’ve asked it [AI] to develop different, like,
to develop the optimal learning strategy for me for learning Spanish".
Overall, we found that freelancers primarily used AI to struc-
ture their learning process, making it easier to integrate into daily
workflows. This AI-driven structuring also enabled them to tailor
learning to their individual styles and focus on specific skills they
wanted to develop.
5.3 When AI-Acquired Learning Does Not
Translate to Recognition
Our survey revealed that while freelancers increasingly incorpo-
rated AI tools into their learning practices, these tools were not
their primary learning resources. Through interviews, freelancers
explained why AI remained secondary as it introduced additional
effort to interpret, evaluate, and verify learning content, increas-
ing freelancers’ learning burden. Participants described needing
to assess credibility, reconcile conflicting guidance, and translate
AI-generated content into practice, often under time pressure.
Freelancers frequently reported feeling overwhelmed by the
volume of AI-generated learning content. Although generative AI
tools offered extensive learning resources, this abundance often
produced decision fatigue, making it difficult for participants to
evaluate and select appropriate materials. P7 described this funda-
mental challenge:"I think it all comes down to, you know, it comes
down to resources...overwhelming number of resources when I’m try-
ing to learn. There are a lot of information out today and most of them
are not verified". Freelancers in our study highlighted another layer
of this overload, particularly the proliferation of AI learning tools.
P3 mentioned:"Some of the concerns I have with AI-powered learning
tools are that there are so many of them to learn from. Sometimes
I don’t know which one. There are so many of them. You wake up
each morning, and there’s one improvement over the previous one.
Sometimes it could be overwhelming. You don’t really know which
one to focus on. If you’re not careful, it could be distracting. "As a
result, learning using generative AI becomes less about engaging
with content and more about navigating an unstable ecosystem of
resources.
In addition to information overload, AI-generated learning con-
tent introduced a new challenge: inconsistency and unreliability.
Participants noted that AI tools often gave varying answers to simi-
lar questions, making it hard to know which learning path to follow.
As P4 noted,"..It’s [the AI is] never consistent. So let’s say today I’ve
asked it [the AI to] give me a roadmap on my digital marketing apps
skill journey. It will give me one [roadmap]. But tomorrow I ask it
the same question, it will give me a different response, and if I ask it
the next day, a different response. So you ask yourself, okay! Which
response should I focus on?". This inconsistency extended beyond
just varying responses as AI-generated content often failed to work
in practice, forcing freelancers to debug and troubleshoot rather
than learn. P5 described this frustrating experience:"It happened to
me a lot before when I was learning a new skill. For example, I have a
question that I can’t find an answer for. I will ask this gpt, for example,
or Google Gemini for an answer and he will give me an [unreliable]
piece of information, for example. I try to run it and I find half the
libraries are deprecated. ".

CHIWORK ’26, June 22–25, 2026, Linz, Austria Imteyaz et al.
Inconsistency and unreliability in AI-generated learning content
became a burden for freelancers, as it forced them to validate and
debug the information instead of focusing on learning. They had
to develop evaluation skills to distinguish useful content from un-
reliable advice, adding to their workload. As P6 noted, freelancers
not only had to learn new skills but also assess the quality of AI-
generated information:"I think that there is a sense of responsibility
of self fact checking [skills related to evaluating whether the AI sug-
gestions are useful] right now. Because, for example, when I am trying
to gather learning resources, it [the AI tool] provides great resources
like the titles of resources, but I need to go and fact check that these
resources actually exist and are credible".
Beyond these challenges, freelancers emphasized that AI-supported
learning rarely translated into legible signals of competence for
clients. While participants described acquiring valuable skills through
AI-mediated learning, they lacked credible mechanisms to demon-
strate or validate these capabilities within platform labor markets.
Clients often valued recognized credentials and prior experience as
indicators of expertise.
P4 emphasized the importance of certification from the client
perspective:’So one of the things they [Clients on freelance platform]
do value is experience. If I’m able to show a client my portfolio and
work I’ve done before, this is a bonus. And they also feel more confident
whenever I show them my certifications because once they see that,
ah, Google has certified you, clearly you can do my work. "
In contrast, AI-based learning frequently produced skills without
comparable forms of external recognition. This resulted in what
we term "invisible competencies", skills that freelancers genuinely
acquire through AI-mediated learning but cannot easily signal or
validate to clients. Rather than reflecting a simple absence of cer-
tification, participants described a structural mismatch between
learning and legibility, where learning pathways evolve faster than
the mechanisms platforms and clients use to evaluate competence.
As P3 articulated:"Sometimes you learn to learn and no certificate to
back it up. Some clients will want to see if you claim you have learned
this and so stuffs, where is a certificate to back it up? But, sometimes
the platforms [AI learning platforms] don’t have a certificate to back
it up [to show a certification that you gained the skill]... ".
This challenge was distinct from the difficulty of signaling infor-
mally acquired knowledge more broadly. When freelancers learned
from peers, they could reference who they learned from and draw
on that person’s professional credibility as indirect validation. AI-
acquired skills, by contrast, arrived without any attributable source.
Participants described having no equivalent way to explain to
clients how they developed a capability when the learning occurred
through private conversations with Generative AI.
Several freelancers described enrolling in formal courses primar-
ily to obtain recognizable credentials, even when those courses did
not substantially differ from what they could learn through AI tools.
P19 explained this strategy:’One of the things I sort of do is try to
get certified.... I take a lot of classes that are something that I’m really
interested in and then I just go through and take those classes as well. "
This behavior highlights how freelancers strategically pursue cre-
dentialed learning pathways not solely for skill acquisition, but to
obtain market-recognized signals that make their upskilling legible
to clients.
5.4 Learning with AI and Peers
Our survey uncovered that freelancers practiced peer learning and
AI tools to a similar degree. In our interviews, freelancers consis-
tently described turning to peer learning to address limitations of
current AI tools, particularly when learning required contextual
judgment, experiential grounding, or clarification amid uncertainty.
P7 emphasized the importance of peers in navigating confusing
or overwhelming AI-generated learning resources:"Most of the
time we are confused by our AI learning resources. We need someone
in that position [someone who is also a freelancer] to come in and
teach us. So having a community of learners and experts within our
same place [learners and experts who are also freelancers], they guide
you by the hand, taking you through whatever it is you’re finding
difficult, helping you to up-skill. Basically, we [freelancers] help one
another wherever we find difficulties. "Across interviews, freelancers
described using AI tools for structured, factual, or low-stakes ques-
tions, while relying on peers for guidance rooted in lived experience
and domain-specific context that AI could not provide.
Critically, freelancers emphasized that the value of peer learning
stemmed not only from personalization but from learning from
identifiable individuals whose experience, context, and professional
outcomes were known. This allowed freelancers to assess the rele-
vance and trustworthiness of shared knowledge without the exten-
sive verification that AI-generated content often required, directly
addressing the verification burden described in the previous sec-
tion. Because AI learning content arrived without provenance (no
indication of source, validity or basis for recommendations), peer
learning provided traceability: who shared the knowledge, under
what conditions, and with what results. P6 described this approach:
"If I only have basic level questions and I feel like that there’s enough
information online... then I am not going to ask these professionals
or people that have been there [those basic level questions]. Instead, I
can ask them something that’s actually deeper, something that has
some complexity [...] I’ll ask them a more complex question and that’s
something you can ask a human about based off of their experience. "
Such an approach addressed the verification burden described in
the previous section.
The value of learning from identifiable, experienced peers be-
came particularly evident when freelancers described gaining pro-
fessional benefits through peer learning, such as accessing special-
ized knowledge and securing new opportunities. P20 recounted
how collaborating with peers directly led to business success:"One
of my fellow freelancers that I am close with, he is in HR [he is a free-
lancer who work in human resources], but he is in like the HR business
partner space... he was able to kind of walk me through some like state
regulations pertaining to human resources, which was really nice of
him. And I ended up getting that gig [a gig related to HR and state
regulations] and was able to help that client". Here, the knowledge
was valuable precisely because P20 knew its source: a practicing
HR professional whose expertise could be verified through their
ongoing work. Similar regulatory information from a generative
AI tool would have required independent fact-checking due to the
absence of source attribution.
Peer learning created supportive environments that helped free-
lancers learn and progress in their gigs. P14 highlighted how this

Upskilling with Generative AI: Practices and Challenges for Freelance Knowledge Workers CHIWORK ’26, June 22–25, 2026, Linz, Austria
dynamic supported both learning and work advancement:"We ac-
tually grouped for a project [gig]. We are like 40 members. And the
reason why we went as far as we did was because we were all there.
We are like holding each other up as peers. We are actually called
peers in the community.... it actually helped us in the days where one
peer might not be feeling up to it [to finish work related to the gig].
Others would just encourage this person to, like, keep going. Or at
times, some people [freelancers] might not really understand what
is going on. The other peers will just take over, like, make you see a
better point of view or just teach you for you to understand. So peer
learning is actually great... ".
However, access to peer learning was uneven, creating barriers
for freelancers without strong networks and potentially pushing
them toward AI tools that, while accessible, lacked attribution bene-
fits. P8 noted that lack of access to experienced mentors particularly
disadvantaged newer freelancers:"I feel like if you have a mentor in
a particular field, you know, the mentor has gone ahead of you. The
mentor has seen some of these challenges and problems and difficul-
ties.. the mentor helps you navigate your way properly. So one of the
challenges that I feel like virtual assistants [a type of freelancer] face
is accessibility to mentorship, which will in turn impact on how much
resources they can get access to".
We observed that freelancers not only decided when to engage
in peer learning but also managed what to share and under what
conditions. Many took a strategic approach, balancing helpfulness
with protecting their competitive edge. P5 articulated this nuance:
"It is usually when both people stand to benefit from the exchange
[that we engage in peer learning]. I am usually willing to share my
knowledge, but at the same time I am a very competitive person. So,
if I know that this person [freelancer] in front of me is an actual
competitor and not just someone asking me about a question, then
usually, I will not be inclined to share [share knowledge], to give away
my advantages for free. But if they are willing to share some of their
specialized knowledge in exchange, in exchange for my own [my own
specialized knowledge], then this becomes a kind of trade and I am
willing to exchange to participate in these exchanges. "
Freelancers’ selectiveness in sharing knowledge often stemmed
from the competitive nature of freelancing, which posed challenges
to peer learning. As P20 observed:"The competitive nature of the gig
economy may deter freelancers from befriending others in the same
field due to direct competition for opportunities. "
Freelancers often drew clear boundaries between different types
of information. For example, many were willing to provide general
guidance but not share proprietary work products. As P5 further
explained:"So if someone just wants the final product from my previ-
ous projects, for example, I will usually tell them no. But I am willing
to give them a general outline of the process I went through and point
them in the right direction. "
The level of openness in peer learning also depended on the
context and audience. Freelancers were more inclined to share in
trusted, private settings than in public forums. P18 described this
distinction:"I prefer to share in private [private groups], because these
are the people that I know more of. I know... maybe I can say I know
every one of them [know the freelancers in the private group], or I
know most of them. I’m open to that, private groups [open to doing
peer learning in private groups]. But in the public [doing peer learning
in public online spaces], where your information can be accessed by
anyone, I’ll keep it brief and maybe more professional so that I don’t
spill more than I should. "
Taken together, these findings reveal a fundamental tension in
freelancers’ learning ecosystems. Peer learning offers contextual
grounding and credibility that AI tools often lack, helping free-
lancers manage information overload and reduce verification effort.
Yet competitive pressures and uneven access constrain when and
how freelancers engage in peer-based knowledge exchange. As a re-
sult, freelancers strategically navigate between AI tools for private,
exploratory, low-stakes learning and peer learning for contextual
validation, opportunity access, and legitimacy-building.
5.5 Envisioning Generative AI-powered
Self-Directed Learning System
Through our interviews, freelancers shared their visions for the
future of AI systems that could support their learning. They empha-
sized the need for AI systems that can actively manage cognitive
load by filtering learning-related information, adjusting content dif-
ficulty, and providing targeted feedback. For example, P3 described
such a system:"This adaptive learning [AI learning system] provides
me timely feedback, helps me adjust to difficulty levels, and it offers
me some personalized resources to learn from, like videos, articles,
and all that".
This emphasis on personalized resource curation reflects free-
lancers’ desire to take control of their learning environment, a core
component of self-directed learning [38]. Participants specifically
wanted AI systems that could reduce extraneous cognitive load
by eliminating irrelevant information and focusing attention on
essential learning elements. As P10 articulated,"if it [their proposed
AI learning tool] gives me personalized options, like, if I want to learn
a specific thing, and the AI tool gives me the exact specific things
and no other, like, no filler, but only the knowledge that I need for the
specific topic or skill, I would really want such a tool... ".
Similarly, another participant (P14) emphasized the importance
of giving learners control over personalization, enabling them to
better manage their cognitive load:"I would like to cut it off or shift
it [cut off or shift the information the AI learning tool provides to
them] and just move to what I need at that moment [move or control
the information the AI learning shows to whatever they need at the
moment]. So, I feel it would be really great if it [AI learning tool]
were personalized. The personalized view feature can be introduced
into any tool for gig workers to manage their mental energy!". This
vision reflects the understanding that effective scaffolding must be
responsive to learners’ immediate cognitive capacity and goals.
Freelancers envisioned AI learning tools that could support
self-monitoring through demonstration, providing examples, and
guided practice, allowing learners to observe professional proce-
dures and evaluate their own progress. This type of support could
help address the gap between theoretical knowledge and practi-
cal application that freelancers frequently encounter. Participants
wanted AI tools that could demonstrate professional practices
through concrete examples. P16 emphasized the importance of
demonstration:"It [AI learning tool] should try to give examples
because this is what helps. For example, if you are talking about how
to write a proposal or how to stand out, try to [the AI tool should try
to], like, show..., give relevant examples of profiles that are standing

CHIWORK ’26, June 22–25, 2026, Linz, Austria Imteyaz et al.
out. That way, when I take a look, I kind of know that, okay, this is
how to set my own up. "Participants also envisioned a Generative
AI tool that could learn each learner’s unique patterns and tailor
guidance accordingly. This would support the self-monitoring pro-
cess by helping freelancers track how they learn best. P9 explained:
"I would be willing to use an AI-powered adaptive learning tool if
it will definitely learn my learning pattern, the way I deal or the
way I, you know, search through things... and it would help me by
copying the pattern or copying the procedure for me and giving me
advice based on my learning pattern... "Others envisioned AI that
could temporarily complete steps for the learner, then gradually
reduce support as competence develops. As P10 said:"It [AI learn-
ing tool] should have the ability to make decisions for them [for the
learner] and complete tasks for them [for the learners] instead of
just making suggestions. This would be based on, like, [learners’]
previous experience and personalized adaptiveness... "These visions
reflect freelancers’ awareness of their learning challenges: informa-
tion overload from current AI tools, the gap between theoretical
knowledge and practical application, and the need for personalized
guidance that supports autonomous skill development.
6 Discussion
Our mixed-methods study reveals a set of tensions in how free-
lancers upskill using current generative AI tools. Freelancers in-
creasingly adopt these tools and express a strong interest in leverag-
ing generative AI for learning, but they often introduce additional
burdens, including information overload and the need to verify
outputs. Drawing on Garrison’s self-directed learning theory [38],
we argue that market pressures shift freelancer learning away from
growth-oriented goals toward what we calllearning-as-survival,
where upskilling is driven by the need to remain competitive and
secure income. We also identifyinvisible competencies: freelancers
acquire skills through generative AI use but struggle to demonstrate
or validate them in freelance labor markets.
6.1 Market-Driven Learning: From Growth to
Survival
Our survey found that 39% of participants consider learning AI-
related skills a top priority for upskilling over the next 1–2 years.
However, our qualitative data suggests that freelancers’ engage-
ment with AI for learning is primarily driven by client demands.
For many freelancers, upskilling in AI seems less about embracing
a new technological frontier and more about meeting explicit ex-
pectations for AI-augmented deliverables in a highly competitive
market.
This market-driven orientation reflects a reactive mode of pro-
fessional development. Freelancers often described adapting their
skill set not through strategic long-term planning but as a neces-
sary response to clients’ evolving demands. This highlights the
complex nature of productive client-freelancer relations, which has
an impact on freelancers’ professional development [13, 119]. As
such, freelancers framed their AI upskilling efforts as strategies for
economic survival, rather than as proactive career investments or
expressions of personal interest in the AI-enhanced technologies.
This pattern marks a shift from traditional adult learning mod-
els centered on self-directed growth [38], towards what we term
“economically constrained self-direction”, where market imperatives
appear to shape both the choice and perceived achievability of
learning goals.
Using Garrison’s self-directed learning framework [38], our find-
ings show that freelancers’ motivation to learn is shaped by context,
particularly economic precarity and client-driven expectations. In
this framework, self-directed learning involves taking responsi-
bility for one’s learning through three connected processes: self-
management (planning and organizing learning activities), self-
monitoring (evaluating progress and adjusting strategies), and mo-
tivation (sustaining effort and maintaining goal direction). Applied
to our results, the model suggests that motivation is not only an
individual disposition. It is also a response to external pressures.
Because freelancers contend with unstable income and must meet
client expectations, their learning priorities often emphasize imme-
diate market viability over longer-term professional growth.
In line with this, freelancers in our study demonstrated self-
management, often structuring learning around active client projects,
and self-monitoring, for example, by tracking market trends and
perceived skill gaps [49, 124]. However, their learning goals were
frequently constrained by how they interpreted shifting market
signals and client demands. These interpretations were shaped by
personal experience and local context, which could be incomplete,
short-lived, or only partially accurate. They also differed across
freelancers depending on access to stable work, professional net-
works, and prior exposure to market information. This raises equity
concerns about who can make well-informed learning decisions in a
rapidly changing environment. At a collective level, if the majority
of freelancers remain locked in survival-mode learning, the plat-
form labor market risks a narrowing of skill development toward
short-term client needs, with freelancers who lack financial stabil-
ity or strong professional networks disproportionately unable to
invest in the longer-term, exploratory learning that could broaden
their career trajectories.
These pressures were further intensified by platform dynamics.
Algorithmic reputation systems create reputational overhead that
influences how freelancers approach skill development [133]. Many
freelancers described avoiding experimentation with unfamiliar
skills in client-facing work because visible mistakes could harm
ratings and future opportunities. This produces a persistent tension
between the learning value of experimentation and the reputational
risks of platform-mediated labor [126], reinforcing reactive, client-
driven upskilling over exploratory learning.
This dynamic is further complicated by a tension specific to AI-
mediated learning: generative AI is both the source of the disruption
freelancers are responding to and the tool they use to respond.
Freelancers described feeling overwhelmed less by the tools than by
the expectation that clients would soon demand mastery of rapidly
evolving AI technologies, producing anxiety about whether current
learning investments would retain value. As a result, freelancers
found themselves dependent on the very technology that threatens
their market position, reinforcing the survival orientation rather
than enabling growth-oriented exploration.

Upskilling with Generative AI: Practices and Challenges for Freelance Knowledge Workers CHIWORK ’26, June 22–25, 2026, Linz, Austria
6.2 Generative AI Shifts Learning Effort and
Produces Invisible Competencies
Our findings reveal how freelancers navigate tensions between
learning, verification, and market legibility when using AI learning
tools. While 70.4% of participants actively used AI tools for up-
skilling and 82% expressed strong interest in AI-powered learning
systems, AI learning tools were not among their most preferred
methods for learning new skills. Although freelancers saw clear
opportunities in these tools, they also described persistent chal-
lenges, particularly inconsistency and unreliability. These issues
create what prior research characterizes as a verification burden
[97, 122]. Unlike traditional educational resources that typically
undergo editorial review [25, 110], AI-generated content often re-
quires continuous fact-checking by individual learners, which can
effectively increase their learning workload [115].
Freelancers also reported that AI-based learning can produce a
“credentialing gap, ” in which workers develop valuable skills but
lack formal recognition of those skills [ 71]. About one-third of
our participants identified this as a key limitation of AI-powered
learning tools, emphasizing the need to supplement AI learning
with formal courses to obtain recognized certifications. This gap
can be particularly consequential in platform-mediated freelance
markets, where credentials operate as trust signals that help clients
decide which workers to hire for specific tasks [86, 107]. Without
verifiable proof of AI-acquired skills, freelancers face what we term
“invisible competencies”,meaning real capabilities that are difficult
to communicate to potential clients.
This challenge differs from other forms of informal learning.
Skills acquired through peer exchange carry a social trace: the
learner can reference who taught them, and that person’s repu-
tation serves as indirect validation. AI-mediated learning leaves
no equivalent trace. It happens privately, produces no relationship
with a mentor or peer that others can verify, and is associated with a
technology that clients may distrust. The resulting skills are not just
uncredentialed but lack the social context through which informal
learning is usually recognized.
This finding extends prior work on verification burden by show-
ing that AI-mediated learning produces not only increased verifica-
tion effort, but also a distinct form of market invisibility. This invis-
ibility can undermine the motivation component of Self-Directed
Learning, as freelancers may question whether time invested in
AI-assisted learning will translate into market value. In this sense,
the credentialing gap is not simply a documentation issue. It can
be a structural barrier that shapes which learning paths freelancers
are willing and able to pursue.
6.3 Peer Learning as a Source of Traceability in
AI-Mediated Upskilling
A key insight from our study is that peer learning provides a form
of traceability that current AI learning tools often lack. Knowl-
edge shared by peers is grounded in identifiable individuals with
known experience, context, and professional trajectories. This al-
lows freelancers to assess credibility without extensive verification.
This finding aligns with theories of situated knowledge [45], which
emphasize that the trustworthiness of knowledge is inseparable
from the social and professional conditions under which it is pro-
duced. In this way, peer learning can reduce the verification burden
associated with AI-generated learning content.
At the same time, our findings reveal that freelancers operate
within a complex ecosystem of interconnected barriers that con-
strain effective peer learning. While prior work has documented
structural barriers such as time scarcity and competitive pressures
in freelance work [40], our study shows how these barriers become
particularly salient in learning contexts. Freelancers described com-
petitive environments in which knowledge sharing carries strategic
risks, which contrasts with peer-learning models that assume open
and reciprocal exchange for collective benefit [13, 95]. Although
64% of participants reported already engaging in peer learning
for upskilling, they rated it poorly as a preferred learning method.
This tension reflects freelancers’ awareness of the risks involved,
which our participants expressed include: oversharing, loss of com-
petitive advantage, and the need to carefully manage professional
boundaries.
Despite these concerns, freelancers also emphasized that peer
learning remains essential for developing specialized knowledge, ac-
cessing opportunities, and establishing professional legitimacy. This
tension points to a design challenge: enabling knowledge exchange
while protecting individual competitive advantage. In this context,
freelancers increasingly described generative AI as a lower-risk
complement to peer learning. AI tools allowed them to explore new
skills privately and iteratively, while reserving peer interactions
for validation, opportunity access, and signaling credibility.
Rather than viewing generative AI as a replacement for peer
learning, participants envisioned AI as a potential mediator of peer-
mediated learning that could help address the isolation of freelance
work [53, 87, 102]. Freelancers imagined AI systems that could
support matching with peers who have complementary, rather than
directly competing, expertise, enabling mutual learning benefits
while minimizing competitive risk.
These findings align with Self-Directed Learning theory, which
emphasizes that learning is not purely individual, but embedded
within social and contextual conditions [80, 84]. Garrison’s frame-
work highlights that while learners take responsibility for directing
their learning, social interaction plays a critical role in confirm-
ing, validating, and contextualizing newly acquired knowledge
[38]. This was evident in our qualitative data, where freelancers
consistently pointed to peers as crucial sources of opportunity,
specialization, and legitimacy. Designing safer peer-learning en-
vironments that balance knowledge exchange with protection of
competitive advantage can therefore strengthen trust and participa-
tion in peer learning, while complementing the role of generative
AI in freelance upskilling.
6.4 Design Implications
Building on our findings, we propose a set of design recommenda-
tions for generative AI–based upskilling tools that address learning
under market pressure, verification burden, invisible competencies,
and competitive peer learning dynamics.
Market-Informed Upskilling Tools.Our findings show that
freelancers are effective at tracking their learning activities, but
they often struggle to translate reactive, client-driven needs into

CHIWORK ’26, June 22–25, 2026, Linz, Austria Imteyaz et al.
long-term strategic growth. We propose tools that integrate real-
time signals of client and market demand directly into freelancers’
existing workflows and automatically cluster client-requested skills
into coherent skill domains over time. For example, a freelancer who
learns “Excel data analysis” for one client, “Tableau visualization”
for another, and “Python basics” for a third could see these skills
grouped as progress toward a “Data Analytics Consultant” position.
By surfacing these patterns, such tools would help freelancers turn
scattered, reactive learning into coherent upskilling trajectories,
strengthening the self-management component of Self-Directed
Learning [38].
Verification and Skill-to-Portfolio Translation.To address
both the verification burden imposed by AI-generated learning
content and the problem of invisible competencies, we propose
integrated systems that support both the validation of learning
materials and the translation of AI-acquired skills into market-
legible evidence. Such systems could cross-reference AI-generated
learning paths with verified sources, display confidence scores, and
flag inconsistencies across industry blogs, course platforms, and
job postings. Building on this verified learning trace, the system
could then document skills acquired through AI guidance using
timestamped evidence, generate portfolio artifacts that demonstrate
competency, and create “skill stories” that explain how skills were
developed and applied. By linking verification directly to portfolio
construction, these systems would reduce learning burden while
supporting the motivation component of Self-Directed Learning
[38], helping freelancers trust that their learning investments can
translate into recognized market value.
Such systems could extend the traceability that freelancers asso-
ciate with peer learning to AI-generated content. One approach is
linking learning path recommendations to outcome data from free-
lancers who followed similar trajectories, such as the proportion of
freelancers in a given domain who successfully applied a skill after
a particular sequence. Another is community annotation, where
freelancers who completed a learning path can flag what worked
and what did not in practice. This would give AI-generated guid-
ance the kind of experiential grounding that freelancers currently
find only through peer interactions.
AI-Mediated Peer Learning with Competitive Protection.
To address the tension between the benefits of peer learning and
the competitive risks it can create, we propose two complementary
features. First, Complementary Skills Matching would connect free-
lancers with peers whose expertise is complementary rather than
directly competing. By analyzing skill profiles, market positioning,
and learning goals, the system could form partnerships where both
parties benefit while minimizing the risk of losing client opportuni-
ties. Second, we propose AI-to-Peer Validation, a hybrid support
model that integrates AI-assisted learning with targeted human
feedback. In this model, a freelancer may use generative AI tools to
advance along a learning path, but when the system detects uncer-
tainty, contradictions, or context-sensitive decisions, it could route
the freelancer to relevant human peers who can validate, inter-
pret, or critique what the AI suggests. This is especially important
when assessing whether an AI recommendation is appropriate for
the freelancer’s specific work context, clients, and platform norms.
Such a system could be implemented through paid or volunteer-
based participation [34, 65], where freelancers build social capital
by supporting one another [41, 101]. This design direction could
align with prior approaches in friendsourcing and learnersourcing
[9, 10, 39, 61], leveraging structured peer contributions to provide
timely, contextualized assistance. Beyond validation, such systems
could support safer experimentation by creating simulated practice
environments that mirror real platform conditions: mock client
briefs, realistic project constraints, and peer review, without actual
reputational consequences. This would allow freelancers to apply
newly learned skills, receive feedback, and build confidence before
deploying them in client-facing work.
6.4.1 Limitation and Future Work.Our study has several limita-
tions. Participants were recruited exclusively from Upwork, which,
despite its size and global reach, has particular algorithmic man-
agement practices, incentive structures, and reputational systems
that may not generalize to other platforms. Our sample also skews
toward knowledge workers who already use AI tools for learning;
those who are reluctant to adopt generative AI may have different
adaptation strategies worth examining. At the same time, focus-
ing on early adopters remains valuable, as it provides some of the
first empirical insights into how knowledge workers on freelance
platforms are upskilling in the emerging landscape of generative
AI–mediated work. The survey analysis is descriptive, reflecting
both the sample size (n = 71) and its exploratory purpose. Larger
samples would allow for inferential analysis of relationships be-
tween freelancing experience, AI usage, and learning preferences.
Our findings also rely on self-reported practices, which may not
reflect actual skill acquisition or performance. Controlled compar-
isons measuring concrete outcomes, such as client acquisition or
earnings when using generative AI for upskilling, would strengthen
these claims. Finally, we focus on learning and upskilling without
attempting to characterize broader labor market shifts, power dy-
namics, or long-term career trajectories shaped by generative AI.
7 Conclusion
This paper examined how freelance knowledge workers use genera-
tive AI tools to support skill development in competitive, platform-
mediated labor markets. Freelancers increasingly turn to generative
AI to structure learning and adapt to shifting client demands, but
these tools introduce verification overhead, limited contextual rele-
vance, and a credentialing gap that produces what we call invisible
competencies. AI-acquired skills lack the social traces that make
peer-learned skills legible to clients, which shapes learning deci-
sions, discourages open experimentation, and reinforces existing
inequalities in access to opportunities. The value of AI-assisted
learning depends not only on content quality but on how well tools
support verification, credentialing, and integration with situated
peer knowledge. The design recommendations we offer focus on re-
ducing verification burden, supporting market-aware learning, and
helping workers translate AI-acquired skills into credible signals
for clients.
ACKNOWLEDGMENTS.Special thanks to the anonymous
reviewers for strengthening the paper and to the freelancers who
participated in the study. This work was partially supported by NSF
grants 2339443 and 2403252. We used Claude and Grammarly to
refine language and clarity under full author oversight; all study

Upskilling with Generative AI: Practices and Challenges for Freelance Knowledge Workers CHIWORK ’26, June 22–25, 2026, Linz, Austria
design, analysis, literature review, and writing were conducted and
verified by the authors.
References
[1] Daron Acemoglu, David Autor, Jonathon Hazell, and Pascual Restrepo. 2022. Ar-
tificial intelligence and jobs: Evidence from online vacancies.Journal of Labor
Economics40, S1 (2022), S293–S340.
[2] Rudaiba Adnin, Atharva Pandkar, Bingsheng Yao, Dakuo Wang, and Maitraye
Das. 2025. Examining Student and Teacher Perspectives on Undisclosed Use of
Generative AI in Academic Work. InProceedings of the 2025 CHI Conference on
Human Factors in Computing Systems. 1–17.
[3] Juan Carlos Alvarez de la Vega, Marta E Cecchinato, John Rooksby, and Joseph
Newbold. 2023. Understanding platform mediated work-life: a diary study with
gig economy freelancers.Proceedings of the ACM on Human-Computer Interaction
7, CSCW1 (2023), 1–32.
[4] John R Anderson, Albert T Corbett, Kenneth R Koedinger, and Ray Pelletier. 1995.
Cognitive tutors: Lessons learned.The journal of the learning sciences4, 2 (1995),
167–207.
[5] Anthropic. 2026.Getting Started with Cowork. Claude Help Center. https://
support.claude.com/en/articles/13345190-getting-started-with-cowork Accessed:
2026-02-02.
[6] John Asker, Chaim Fershtman, Jihye Jeon, and Ariel Pakes. 2016.The competitive
effects of information sharing. Technical Report. National Bureau of Economic
Research.
[7] David H Autor. 2015. Why are there still so many jobs? The history and future of
workplace automation.Journal of economic perspectives29, 3 (2015), 3–30.
[8] Margaret E. Beier, Mahima Saxena, Kurt Kraiger, David P. Costanza, Cort W.
Rudolph, David M. Cadiz, Gretchen A. Petery, and Gwenith G. Fisher. 2025. Work-
place learning and the future of work.Industrial and Organizational Psychology
18, 1 (2025), 84–109. doi:10.1017/iop.2024.57
[9] Michael S Bernstein. 2010. Crowd-powered interfaces. InAdjunct proceedings
of the 23nd annual ACM symposium on User interface software and technology.
347–350.
[10] Michael S Bernstein, Desney Tan, Greg Smith, Mary Czerwinski, and Eric Horvitz.
2008. Personalization via friendsourcing.ACM Transactions on Computer-Human
Interaction (TOCHI)17, 2 (2008), 1–28.
[11] Allie Blaising and Laura Dabbish. 2022. Managing the transition to online
freelance platforms: self-directed socialization.Proceedings of the ACM on Human-
Computer Interaction6, CSCW2 (2022), 1–26.
[12] Allie Blaising, Yasmine Kotturi, and Chinmay Kulkarni. 2019. Navigating Un-
certainty in the Future of Work: Information-Seeking and Critical Events Among
Online Freelancers. InExtended Abstracts of the 2019 CHI Conference on Human
Factors in Computing Systems(Glasgow, Scotland Uk)(CHI EA ’19). Association
for Computing Machinery, New York, NY, USA, 1–6. doi:10.1145/3290607.3312922
[13] Allie Blaising, Yasmine Kotturi, Chinmay Kulkarni, and Laura Dabbish. 2021.
Making it work, or not: A longitudinal study of career trajectories among online
freelancers.Proceedings of the ACM on Human-Computer Interaction4, CSCW3
(2021), 1–29.
[14] Ann Blandford, Dominic Furniss, and Stephann Makri. 2016.Qualitative HCI
research: Going behind the scenes. Morgan & Claypool Publishers.
[15] Gary Blau, Lynne Andersson, Kathleen Davis, Tom Daymont, Arthur Hochner,
Karen Koziara, Jim Portwood, and Blair Holladay. 2008. The relation between
employee organizational and professional development activities.Journal of
Vocational Behavior72, 1 (2008), 123–142.
[16] Virginia Braun and Victoria Clarke. 2019. Reflecting on reflexive thematic analysis.
Qualitative research in sport, exercise and health11, 4 (2019), 589–597.
[17] Peter Brusilovsky and Eva Millán. 2007. User models for adaptive hypermedia
and adaptive educational systems. InThe adaptive web: methods and strategies of
web personalization. Springer, 3–53.
[18] Erik Brynjolfsson, Danielle Li, and Lindsey Raymond. 2025. Generative AI at
work.The Quarterly Journal of Economics140, 2 (2025), 889–942.
[19] Andrew Burke and Marc Cowling. 2020. The relationship between freelance
workforce intensity, business performance and job creation.Small Business Eco-
nomics55, 2 (2020), 399–413.
[20] Dan Calacci. 2022. Organizing in the end of employment: information sharing,
data stewardship, and digital workerism. InProceedings of the 1st Annual Meeting
of the Symposium on Human-Computer Interaction for Work. 1–9.
[21] Joe Campana. 2014. Learning for work and professional development: The
significance of informal learning networks of digital media industry professionals.
International Journal of Training Research12, 3 (2014), 213–226. doi:10.1080/
14480220.2014.11082043
[22] Steve Campbell, Melanie Greenwood, Sarah Prior, Toniele Shearer, Kerrie Walkem,
Sarah Young, Danielle Bywaters, and Kim Walker. 2020. Purposive sampling:
complex or simple? Research case examples.Journal of research in Nursing25, 8
(2020), 652–661.
[23] John Chen, Xi Lu, Yuzhou Du, Michael Rejtig, Ruth Bagley, Mike Horn, and Uri
Wilensky. 2024. Learning Agent-based Modeling with LLM Companions: Expe-
riences of Novices and Experts Using ChatGPT & NetLogo Chat. InProceedings
of the 2024 CHI Conference on Human Factors in Computing Systems(Honolulu,
HI, USA)(CHI ’24). Association for Computing Machinery, New York, NY, USA,
Article 141, 18 pages. doi:10.1145/3613904.3642377
[24] Chun-Wei Chiang, Anna Kasunic, and Saiph Savage. 2018. Crowd coach: Peer
coaching for crowd workers’ skill growth.Proceedings of the ACM on Human-
Computer Interaction2, CSCW (2018), 1–17.
[25] Gráinne Conole and Karen Fill. 2005. A learning design toolkit to create peda-
gogically effective learning activities.Journal of Interactive Media in Education1
(2005).
[26] Kelley Cotter and Bianca C Reisdorf. 2020. Algorithmic knowledge gaps: A new
horizon of (digital) inequality.International Journal of Communication14 (2020),
21.
[27] John W Creswell and Vicki L Plano Clark. 2017.Designing and conducting mixed
methods research. Sage publications.
[28] Valdemar Danry, Pat Pataranutaporn, Matthew Groh, and Ziv Epstein. 2025.
Deceptive explanations by large language models lead people to change their
beliefs about misinformation more often than honest explanations. InProceedings
of the 2025 CHI Conference on Human Factors in Computing Systems. 1–31.
[29] Ozge Demirci, Jonas Hannane, and Xinrong Zhu. 2025. Who is AI replacing?
The impact of generative AI on online freelancing platforms.Management Science
71, 10 (2025), 8097–8108.
[30] Kimberly Do, Maya De Los Santos, Michael Muller, and Saiph Savage. 2024.
Designing gig worker sousveillance tools. InProceedings of the 2024 CHI Conference
on Human Factors in Computing Systems. 1–19.
[31] Mateusz Dolata, Norbert Lange, and Gerhard Schwabe. 2025. More Attention,
Transformation, Acceleration, and Exploration: Freelance Developers’ Take on
Hypes. InProceedings of the 2025 CHI Conference on Human Factors in Computing
Systems (CHI ’25). Association for Computing Machinery, New York, NY, USA,
Article 914, 21 pages. doi:10.1145/3706598.3713097
[32] Michael Eraut*. 2004. Informal learning in the workplace.Studies in continuing
education26, 2 (2004), 247–273.
[33] Shaoyang Fan, Ujwal Gadiraju, Alessandro Checco, and Gianluca Demartini. 2020.
Crowdco-op: Sharing risks and rewards in crowdsourcing.Proceedings of the ACM
on Human-Computer Interaction4, CSCW2 (2020), 1–24.
[34] Claudia Flores Saviaga, Ricardo Granados, Liliana Savage, Lizbeth Olivia Es-
cobedo Bravo, and Saiph Savage. 2020. Understanding the complementary nature
of paid and volunteer crowds for content creation. (2020).
[35] Claudia Flores-Saviaga, Benjamin V Hanrahan, Kashif Imteyaz, Steven Clarke,
and Saiph Savage. 2025. The Impact of Generative AI Coding Assistants on
Developers Who Are Visually Impaired. InProceedings of the 2025 CHI Conference
on Human Factors in Computing Systems. 1–17.
[36] Zachary Fulker and Christoph Riedl. 2024. Cooperation in the Gig Economy:
Insights from Upwork Freelancers.Proc. ACM Hum.-Comput. Interact.8, CSCW1,
Article 37 (April 2024), 20 pages. doi:10.1145/3637314
[37] Marylène Gagné, Sharon K Parker, Mark A Griffin, Patrick D Dunlop, Caroline
Knight, Florian E Klonek, and Xavier Parent-Rocheleau. 2022. Understanding
and shaping the future of work with self-determination theory.Nature Reviews
Psychology1, 7 (2022), 378–392.
[38] D Randy Garrison. 1997. Self-directed learning: Toward a comprehensive model.
Adult education quarterly48, 1 (1997), 18–33.
[39] Elena L Glassman, Christopher J Terman, and Robert C Miller. 2015. Learner-
sourcing in an engineering class at scale. InProceedings of the Second (2015) ACM
Conference on Learning@ Scale. 363–366.
[40] Mary L. Gray and Siddharth Suri. 2019.Ghost Work: How to Stop Silicon Valley
from Building a New Global Underclass. Houghton Mifflin Harcourt, New York,
NY. https://marylgray.org/bio/on-demand/
[41] Mary L Gray, Siddharth Suri, Syed Shoaib Ali, and Deepti Kulkarni. 2016. The
crowd is a collaborative network. InProceedings of the 19th ACM conference on
computer-supported cooperative work & social computing. 134–147.
[42] H. Gruenewald and M. Mueller. 2025. Challenges and Opportunities in Reskilling
and Upskilling. InReskilling and Upskilling in a Globalized Economy, Future of
Business and Finance. Springer Fachmedien Wiesbaden GmbH, part of Springer
Nature, 167–196. doi:10.1007/978-3-658-48384-5_7
[43] Fabian Gussek. 2024. Understanding the careers of freelancers on digital labor
platforms: The case of IT work.Information Systems Journal(2024). doi:10.1111/
isj.12509
[44] Kunal Handa, Alex Tamkin, Miles McCain, Saffron Huang, Esin Durmus, Sarah
Heck, Jared Mueller, Jerry Hong, Stuart Ritchie, Tim Belonax, et al. 2025. Which
economic tasks are performed with ai? evidence from millions of claude conversa-
tions.arXiv preprint arXiv:2503.04761(2025).
[45] Donna Haraway. 2013. Situated knowledges: The science question in feminism
and the privilege of partial perspective 1. InWomen, science, and technology.
Routledge, 455–472.
[46] Jessica He, Stephanie Houde, and Justin D Weisz. 2025. Which contributions
deserve credit? Perceptions of attribution in human-AI co-creation. InProceedings

CHIWORK ’26, June 22–25, 2026, Linz, Austria Imteyaz et al.
of the 2025 CHI conference on human factors in computing systems. 1–18.
[47] David M Holtz, Liane Scult, and Siddharth Suri. 2022. How Much Do Platform
Workers Value Reviews? An Experimental Method. InProceedings of the 2022
CHI Conference on Human Factors in Computing Systems(New Orleans, LA, USA)
(CHI ’22). Association for Computing Machinery, New York, NY, USA, Article 71,
11 pages. doi:10.1145/3491102.3501900
[48] Jane Hsieh, Miranda Karger, Lucas Zagal, and Haiyi Zhu. 2023. Co-designing
alternatives for the future of gig worker well-being: Navigating multi-stakeholder
incentives and preferences. InProceedings of the 2023 ACM Designing Interactive
Systems Conference. 664–687.
[49] Jane Hsieh, Angie Zhang, Sajel Surati, Sijia Xie, Yeshua Ayala, Nithila Sathiya,
Tzu-Sheng Kuo, Min Kyung Lee, and Haiyi Zhu. 2025. Gig2Gether: Datasharing to
Empower, Unify and Demystify Gig Work. InProceedings of the 2025 CHI Conference
on Human Factors in Computing Systems. 1–25.
[50] Jessica Huang, Ning F Ma, Veronica A Rivera, Tabreek Somani, Patrick Yung Kang
Lee, Joanna Mcgrenere, and Dongwook Yoon. 2024. Design Tensions in Online
Freelancing Platforms: Using Speculative Participatory Design to Support Free-
lancers’ Relationships with Clients.Proceedings of the ACM on Human-Computer
Interaction8, CSCW1 (2024), 1–28.
[51] Keman Huang, Jinhui Yao, and Ming Yin. 2019. Understanding the Skill Provision
in Gig Economy from A Network Perspective: A Case Study of Fiverr.Proceedings
of the ACM on Human-Computer Interaction3 (11 2019), 1–23. doi:10.1145/3359234
[52] Xiang Hui, Oren Reshef, and Luofeng Zhou. 2024. The Short-Term Effects of
Generative Artificial Intelligence on Employment: Evidence from an Online Labor
Market.Organization Science35, 6 (Nov. 2024), 1977–1989. doi:10.1287/orsc.2023.
18441
[53] Kashif Imteyaz, Claudia Flores-Saviaga, and Saiph Savage. 2024. GigSense:
An LLM-Infused Tool forWorkers’ Collective Intelligence.arXiv preprint
arXiv:2405.02528(2024).
[54] Kashif Imteyaz, Claudia Flores Saviaga, and Saiph Savage. 2024. Human Com-
putation, Equitable, and Innovative Future of Work AI Tools. InProceedings of
the Twelfth AAAI Conference on Human Computation and Crowdsourcing, Vol. 12.
AAAI Press, 155–156. doi:10.1609/hcomp.v12i1.31611
[55] Kashif Imteyaz, Michael Muller, Claudia Flores-Saviaga, and Saiph Savage. 2026.
Co-Designing Collaborative Generative AI Tools for Freelancers. InProceedings of
the 2026 CHI Conference on Human Factors in Computing Systems. 1–21.
[56] Nataliya V Ivankova, John W Creswell, and Sheldon L Stick. 2006. Using mixed-
methods sequential explanatory design: From theory to practice.Field methods18,
1 (2006), 3–20.
[57] Mohammad Hossein Jarrahi, Gemma Newlands, Min Kyung Lee, Christine T
Wolf, Eliscia Kinder, and Will Sutherland. 2021. Algorithmic management in a
work context.Big Data & Society8, 2 (2021), 20539517211020332.
[58] David W. Johnson and Roger T. Johnson. 1987.Learning Together and Alone:
Cooperative, Competitive, and Individualistic Learning(2nd ed.). Prentice-Hall, Inc.,
Englewood Cliffs, NJ.
[59] Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, Maria Bannert, Daryna
Dementieva, Frank Fischer, Urs Gasser, Georg Groh, Stephan Günnemann, Eyke
Hüllermeier, et al. 2023. ChatGPT for good? On opportunities and challenges
of large language models for education.Learning and individual differences103
(2023), 102274.
[60] Majeed Kazemitabaar, Justin Chow, Carl Ka To Ma, Barbara J Ericson, David
Weintrop, and Tovi Grossman. 2023. Studying the effect of AI code generators on
supporting novice learners in introductory programming. InProceedings of the
2023 CHI conference on human factors in computing systems. 1–23.
[61] Juho Kim et al. 2015.Learnersourcing: improving learning with collective learner
activity. Ph. D. Dissertation. Massachusetts Institute of Technology.
[62] Pyeonghwa Kim, Taylor Lewandowski, Michael Dunn, and Steve Sawyer. 2026.
Occupational Diversity and Stratification in Platform Work: A Longitudinal Study
of Online Freelancers.arXiv preprint arXiv:2604.03517(2026).
[63] Pyeonghwa Kim and Steve Sawyer. 2023. Many Futures of Work and Skill: Hetero-
geneity in Skill Building Experiences on Digital Labor Platforms. InProceedings of
the 2nd Annual Meeting of the Symposium on Human-Computer Interaction for Work
(Oldenburg, Germany)(CHIWORK ’23). Association for Computing Machinery,
New York, NY, USA, Article 11, 9 pages. doi:10.1145/3596671.3597655
[64] Barbara A Kitchenham and Shari L Pfleeger. 2008. Personal opinion surveys. In
Guide to advanced empirical software engineering. Springer, 63–92.
[65] Aniket Kittur, Jeffrey V. Nickerson, Michael Bernstein, Elizabeth Gerber, Aaron
Shaw, John Zimmerman, Matt Lease, and John Horton. 2013. The future of crowd
work. InProceedings of the 2013 Conference on Computer Supported Cooperative
Work(San Antonio, Texas, USA)(CSCW ’13). Association for Computing Machin-
ery, New York, NY, USA, 1301–1318. doi:10.1145/2441776.2441923
[66] Benjamin Knight, Dmitry Mitrofanov, and Serguei Netessine. 2024. The impact
of AI technology on the productivity of gig economy workers. InProceedings of
the 25th ACM Conference on Economics and Computation. 833–833.
[67] Malcolm Shepherd Knowles et al. 1980.The modern practice of adult education:
From pedagogy to andragogy. Vol. 2. Cambridge Adult Education Englewood Cliffs,
NJ.
[68] Ekaterina Kochmar, Dung Do Vu, Robert Belfer, Varun Gupta, Iulian Vlad Ser-
ban, and Joelle Pineau. 2022. Automated data-driven generation of personalized
pedagogical interventions in intelligent tutoring systems.International Journal of
Artificial Intelligence in Education32, 2 (2022), 323–349.
[69] David A Kolb. 2014.Experiential learning: Experience as the source of learning and
development. FT press.
[70] Lin Kyi, Amruta Mahuli, M Six Silberman, Reuben Binns, Jun Zhao, and Asia J
Biega. 2025. Governance of Generative AI in Creative Work: Consent, Credit,
Compensation, and Beyond. InProceedings of the 2025 CHI Conference on Human
Factors in Computing Systems. 1–16.
[71] Josephine Lang. 2023. Workforce upskilling: can universities meet the chal-
lenges of lifelong learning?The International Journal of Information and Learning
Technology40, 5 (2023), 388–400.
[72] Min Kyung Lee, Daniel Kusbit, Evan Metsky, and Laura Dabbish. 2015. Working
with Machines: The Impact of Algorithmic and Data-Driven Management on
Human Workers. InProceedings of the 33rd Annual ACM Conference on Human
Factors in Computing Systems(Seoul, Republic of Korea)(CHI ’15). Association
for Computing Machinery, New York, NY, USA, 1603–1612. doi:10.1145/2702123.
2702548
[73] Ling Li. 2024. Reskilling and upskilling the future-ready workforce for industry
4.0 and beyond.Information Systems Frontiers26, 5 (2024), 1697–1712.
[74] Andrew Lowe, Anthony C Norris, A Jane Farris, and Duncan R Babbage. 2018.
Quantifying thematic saturation in qualitative data analysis.Field methods30, 3
(2018), 191–207.
[75] Oleksandr Lytvyn. 2025. Human-AI Interaction in Language Acquisition: Eval-
uating LLM as a Language Partner. InProceedings of the MEi: CogSci Conference,
Vol. 19.
[76] Ning F. Ma, Veronica A. Rivera, Zheng Yao, and Dongwook Yoon. 2022. “Brush
it Off”: How Women Workers Manage and Cope with Bias and Harassment in
Gender-agnostic Gig Platforms. InProceedings of the 2022 CHI Conference on Human
Factors in Computing Systems(New Orleans, LA, USA)(CHI ’22). Association for
Computing Machinery, New York, NY, USA, Article 397, 13 pages. doi:10.1145/
3491102.3517524
[77] Shuai Ma, Junling Wang, Yuanhao Zhang, Xiaojuan Ma, and April Yi Wang. 2025.
DBox: Scaffolding Algorithmic Programming Learning through Learner-LLM Co-
Decomposition. InProceedings of the 2025 CHI Conference on Human Factors in
Computing Systems (CHI ’25). Association for Computing Machinery, New York,
NY, USA, Article 585, 20 pages. doi:10.1145/3706598.3713748
[78] Mareike Möhlmann, Lior Zalmanson, Ola Henfridsson, and Robert Wayne Gre-
gory. 2021. Algorithmic management of work on online labor platforms: When
matching meets control.MIS quarterly45, 4 (2021).
[79] Sofia Morandini, Federico Fraboni, Marco De Angelis, Gabriele Puzzo, Davide
Giusino, and Luca Pietrantoni. 2023. The Impact of Artificial Intelligence on
Workers’ Skills: Upskilling and Reskilling in Organisations.Informing Science: The
International Journal of an Emerging Transdiscipline26 (2023), 39–68. doi:10.28945/
5078
[80] Thomas Howard Morris. 2019. Self-directed learning: A fundamental competence
in a rapidly changing world.International Review of Education65, 4 (2019), 633–
653.
[81] Isabel Munoz, Michael Dunn, Steve Sawyer, and Emily Michaels. 2022. Platform-
mediated markets, online freelance workers and deconstructed identities.Proceed-
ings of the ACM on Human-Computer Interaction6, CSCW2 (2022), 1–24.
[82] Isabel Munoz, Steve Sawyer, and Michael Dunn. 2022. New futures of work or
continued marginalization? The rise of online freelance work and digital platforms.
InProceedings of the 1st Annual Meeting of the Symposium on Human-Computer
Interaction for Work. 1–7.
[83] Varun Nagaraj Rao, Samantha Dalal, Eesha Agarwal, Dana Calacci, and Andrés
Monroy-Hernández. 2025. Rideshare transparency: Translating gig worker insights
on ai platform design to policy.Proceedings of the ACM on Human-Computer
Interaction9, 2 (2025), 1–49.
[84] Katja Neureiter, Ulrike Bruckenberger, Alina Krischkowsky, and Manfred Tsche-
ligi. 2017. Exploring User Requirements for Online Cooperation through Social
Capital Theory.IxD&A34 (2017), 187–206.
[85] Amedeo Pachera, Andrea Mauri, Kashif Imteyaz, Jie Yang, Eric Umuhoza, Angela
Bonifati, Michal Lahav, and Nitesh Goyal. 2026. Co-Data: Cultivating Effective
Human-LLM Collaboration for Collaborative Data Processing. InProceedings of
the Extended Abstracts of the 2026 CHI Conference on Human Factors in Computing
Systems. 1–7.
[86] Amanda Pallais. 2014. Inefficient hiring in entry-level labor markets.American
Economic Review104, 11 (2014), 3565–3599.
[87] Roy D Pea. 2018. The social and technological dimensions of scaffolding and
related theoretical concepts for learning, education, and human activity. InScaf-
folding. Psychology Press, 423–451.
[88] Sida Peng, Eirini Kalliamvakou, Peter Cihon, and Mert Demirer. 2023. The
Impact of AI on Developer Productivity: Evidence from GitHub Copilot.
arXiv:2302.06590 [cs.SE] https://arxiv.org/abs/2302.06590
[89] Gustavo R Pilatti, Flavio L Pinheiro, and Alessandra A Montini. 2024. Systematic
literature review on gig economy: Power dynamics, worker autonomy, and the

Upskilling with Generative AI: Practices and Challenges for Freelance Knowledge Workers CHIWORK ’26, June 22–25, 2026, Linz, Austria
role of social networks.Administrative Sciences14, 10 (2024), 267.
[90] Timothy J Pleskac, Larissa Conradt, Christina Leuker, and Ralph Hertwig. 2021.
The ecology of competition: A theory of risk–reward environments in adaptive
decision making.Psychological Review128, 2 (2021), 315.
[91] Tejaswi Polimetla, Katy Ilonka Gero, and Elena L Glassman. 2026. A Paradigm for
Creative Ownership. InProceedings of the 2026 CHI Conference on Human Factors
in Computing Systems. 1–16.
[92] Pawel Popiel. 2017. “Boundaryless” in the creative economy: assessing freelancing
on Upwork.Critical Studies in Media Communication34, 3 (2017), 220–233.
[93] Kalyan Prasad Agrawal. 2024. Towards adoption of generative AI in organiza-
tional settings.Journal of Computer Information Systems64, 5 (2024), 636–651.
[94] Mirjana Prpa, Giovanni Maria Troiano, Matthew Wood, and Yvonne Coady. 2024.
Challenges and Opportunities of LLM-Based Synthetic Personae and Data in
HCI. InExtended Abstracts of the CHI Conference on Human Factors in Computing
Systems(Honolulu, HI, USA)(CHI EA ’24). Association for Computing Machinery,
New York, NY, USA, Article 461, 5 pages. doi:10.1145/3613905.3636293
[95] Ruo Ning Qiu, Annapurna Vadaparty, Suma Vintha, and Steven P Dow. 2025.
Self-Reflective Crowds: Surfacing Wisdom through Emergent Scaffolding. InPro-
ceedings of the ACM Collective Intelligence Conference. 169–187.
[96] Chris Quintana and Meilan Zhang. 2004. IdeaKeeper Notepads: Scaffolding digital
library information analysis in online inquiry. InCHI’04 Extended Abstracts on
Human Factors in Computing Systems. 1329–1332.
[97] Prerna Ravi, John Masla, Gisella Kakoti, Grace C. Lin, Emma Anderson, Matt
Taylor, Anastasia K. Ostrowski, Cynthia Breazeal, Eric Klopfer, and Hal Abelson.
2025. Co-designing Large Language Model Tools for Project-Based Learning with
K12 Educators. InProceedings of the 2025 CHI Conference on Human Factors in
Computing Systems (CHI ’25). Association for Computing Machinery, New York,
NY, USA, Article 138, 25 pages. doi:10.1145/3706598.3713971
[98] Brian J Reiser. 2018. Scaffolding complex learning: The mechanisms of structuring
and problematizing student work. InScaffolding. Psychology Press, 273–304.
[99] Christoph Riedl, David De Cremer, Gina Lucarelli, Erika Antoine-Souklaye, Seth
Bullock, Nirav Ajmeri, Mike Batty, Michaela Black, John Cartlidge, Robert Challen,
et al. 2025. The potential and challenges of AI for collective intelligence.Collective
Intelligence4, 1 (2025), 26339137241308821.
[100] Gobinda Roy and Avinash K Shrivastava. 2020. Future of gig economy: oppor-
tunities and challenges.Imi Konnect9, 1 (2020), 14–27.
[101] Jeffrey M Rzeszotarski and Meredith Ringel Morris. 2014. Estimating the social
costs of friendsourcing. InProceedings of the SIGCHI Conference on Human Factors
in Computing Systems. 2735–2744.
[102] Bhavani Seetharaman, Joyojeet Pal, and Julie Hui. 2021. Delivery work and
the experience of social isolation.Proceedings of the ACM on Human-Computer
Interaction5, CSCW1 (2021), 1–17.
[103] Yijia Shao, Humishka Zope, Yucheng Jiang, Jiaxin Pei, David Nguyen, Erik
Brynjolfsson, and Diyi Yang. 2025. Future of Work with AI Agents: Auditing
Automation and Augmentation Potential across the US Workforce.arXiv preprint
arXiv:2506.06576(2025).
[104] Judy Hanwen Shen and Alex Tamkin. 2026. How AI Impacts Skill Formation.
arXiv preprint arXiv:2601.20245(2026).
[105] Muhtasim Ibteda Shochcho, Mohammad Ashfaq Ur Rahman, Shadman Rohan,
Ashraful Islam, Hasnain Heickal, AKM Mahbubur Rahman, M. Ashraful Amin,
and Amin Ahsan Ali. 2025. Improving User Engagement and Learning Outcomes
in LLM-Based Python Tutor: A Study of PACE. InProceedings of the Extended
Abstracts of the CHI Conference on Human Factors in Computing Systems (CHI
EA ’25). Association for Computing Machinery, New York, NY, USA, Article 337,
12 pages. doi:10.1145/3706599.3720240
[106] Auste Simkute, Lev Tankelevitch, Viktor Kewenig, Ava Elizabeth Scott, Abi-
gail Sellen, and Sean Rintel. 2025. Ironies of generative AI: understanding and
mitigating productivity loss in Human-AI interaction.International Journal of
Human–Computer Interaction41, 5 (2025), 2898–2919.
[107] Michael Spence. 1978. Job market signaling. InUncertainty in economics. Elsevier,
281–306.
[108] Statista. 2023. Amount of people freelancing U.S. 2023. https://www.statista.
com/statistics/685468/amount-of-people-freelancing-us/ Accessed: 2025-04-01.
[109] Jake M L Stein, Vidminas Vizgirda, Max Van Kleek, Reuben Binns, Jun Zhao,
Rui Zhao, Naman Goel, George Chalhoub, Wael S Albayaydh, and Nigel Shadbolt.
2023. ‘You are you and the app. There’s nobody else. ’: Building Worker-Designed
Data Institutions within Platform Hegemony. InProceedings of the 2023 CHI Con-
ference on Human Factors in Computing Systems(Hamburg, Germany)(CHI ’23).
Association for Computing Machinery, New York, NY, USA, Article 281, 26 pages.
doi:10.1145/3544548.3581114
[110] Marcy Stein, Carol Stuen, Douglas Carnine, and Roger M Long. 2001. Textbook
evaluation and adoption.Reading & Writing Quarterly17, 1 (2001), 5–23.
[111] Muhammad Saleem Sumbal, Quratulain Amber, Adeel Tariq, Muham-
mad Mustafa Raziq, and Eric Tsui. 2024. Wind of change: how ChatGPT and
big data can reshape the knowledge management paradigm?Industrial Manage-
ment & Data Systems124, 9 (2024), 2736–2757.
[112] Daniel Susskind. 2020.A world without work: Technology, automation and how
we should respond. Penguin UK.
[113] Alex Tamkin, Miles Brundage, Jack Clark, and Deep Ganguli. 2021. Understand-
ing the capabilities, limitations, and societal impact of large language models.
arXiv preprint arXiv:2102.02503(2021).
[114] Ole Teutloff, Johanna Einsiedler, Otto Kässi, Fabian Braesemann, Pamela
Mishkin, and R Maria del Rio-Chanona. 2025. Winners and losers of genera-
tive AI: Early Evidence of Shifts in Freelancer Demand.Journal of Economic
Behavior & Organization(2025), 106845.
[115] Carlos Toxtli, Siddharth Suri, and Saiph Savage. 2021. Quantifying the invisible
labor in crowd work.Proceedings of the ACM on human-computer interaction5,
CSCW2 (2021), 1–26.
[116] T. Trust, D. G. Krutka, and J. P. Carpenter. 2016. “Together we are better”:
Professional learning networks for teachers.Computers & Education102 (2016),
15–34. doi:10.1016/j.compedu.2016.06.007
[117] Upwork. 2023. Upwork Study Finds 64 Million Americans Freelanced in 2023,
Adding $1.27 Trillion to U.S. Economy. https://investors.upwork.com/news-
releases/news-release-details/upwork-study-finds-64-million-americans-
freelanced-2023-adding Accessed: 2025-04-01.
[118] Upwork Research Institute. 2025. The Future Workforce Index: Evolving Talent
Trends in 2025 and Beyond. https://www.upwork.com/research/future-workforce-
index-2025 Accessed August 18, 2025.
[119] PSKP Venkatesh, V Selvakumar, M Ramu, M Manikandan, and CR Senthilnathan.
2023. Measure of well-being of freelancers in IT sector. In2023 Intelligent Comput-
ing and Control for Engineering and Business Systems (ICCEBS). IEEE, 1–4.
[120] Irina Verenikina. 2008. Scaffolding and learning: Its role in nurturing new
learners. (2008).
[121] Kelly B Wagman, Matthew T Dearing, and Marshini Chetty. 2025. Generative AI
Uses and Risks for Knowledge Workers in a Science Organization. InProceedings
of the 2025 CHI Conference on Human Factors in Computing Systems. 1–17.
[122] Xinru Wang, Hannah Kim, Sajjadur Rahman, Kushan Mitra, and Zhengjie Miao.
2024. Human-LLM Collaborative Annotation Through Effective Verification of
LLM Labels. InProceedings of the 2024 CHI Conference on Human Factors in Comput-
ing Systems(Honolulu, HI, USA)(CHI ’24). Association for Computing Machinery,
New York, NY, USA, Article 303, 21 pages. doi:10.1145/3613904.3641960
[123] Xinyu Jessica Wang, Christine P Lee, and Bilge Mutlu. 2025. LearnMate: En-
hancing Online Education with LLM-Powered Personalized Learning Plans and
Support. InProceedings of the Extended Abstracts of the CHI Conference on Human
Factors in Computing Systems. 1–10.
[124] Qi Wei, Lilith Whiley, and Caroline Boyd. 2024. Person-Career Fit: An Ex-
ploration of Self-Employed Freelancers. InAcademy of Management Proceedings,
Vol. 2024. Academy of Management Valhalla, NY 10595, 13093.
[125] Denise J Wilkins, Srihari Hulikal Muralidhar, Max Meijer, Laura Lascau, and
Siân Lindley. 2022. Gigified knowledge work: understanding knowledge gaps
when knowledge work and on-demand work intersect.Proceedings of the ACM on
human-computer interaction6, CSCW1 (2022), 1–27.
[126] Alex J Wood, Mark Graham, Vili Lehdonvirta, and Isis Hjorth. 2019. Good gig,
bad gig: autonomy and algorithmic control in the global gig economy.Work,
employment and society33, 1 (2019), 56–75.
[127] Alex J Wood, Vili Lehdonvirta, and Mark Graham. 2018. Workers of the Internet
unite? Online freelancer organisation among remote gig economy workers in six
Asian and African countries.New Technology, Work and Employment33, 2 (2018),
95–112.
[128] David Wood, Jerome S Bruner, and Gail Ross. 1976. The role of tutoring in
problem solving.Journal of child psychology and psychiatry17, 2 (1976), 89–100.
[129] Allison Woodruff, Renee Shelby, Patrick Gage Kelley, Steven Rousso-Schindler,
Jamila Smith-Loud, and Lauren Wilcox. 2024. How knowledge workers think
generative ai will (not) transform their industries. InProceedings of the 2024 CHI
Conference on Human Factors in Computing Systems. 1–26.
[130] Qing Xiao, Xinlan Emily Hu, Mark E Whiting, Arvind Karunakaran, Hong Shen,
and Hancheng Cao. 2025. AI Hasn’t Fixed Teamwork, But It Shifted Collabo-
rative Culture: A Longitudinal Study in a Project-Based Software Development
Organization (2023-2025).
[131] Bhada Yun, Dana Feng, Ace S Chen, Afshin Nikzad, and Niloufar Salehi. 2025.
Generative ai in knowledge work: Design implications for data navigation and
decision-making. InProceedings of the 2025 CHI Conference on Human Factors in
Computing Systems. 1–19.
[132] J Diego Zamfirescu-Pereira, Richmond Y Wong, Bjoern Hartmann, and Qian
Yang. 2023. Why Johnny can’t prompt: how non-AI experts try (and fail) to
design LLM prompts. InProceedings of the 2023 CHI conference on human factors
in computing systems. 1–21.
[133] Angie Zhang, Alexander Boltz, Chun Wei Wang, and Min Kyung Lee. 2022.
Algorithmic management reimagined for workers and by workers: Centering
worker well-being in gig work. InProceedings of the 2022 CHI conference on human
factors in computing systems. 1–20.
[134] Angie Zhang and Min Kyung Lee. 2025. Knowledge Workers’ Perspectives on
AI Training for Responsible AI Use. InProceedings of the 2025 CHI Conference on
Human Factors in Computing Systems. 1–18.
[135] Angie Zhang, Rocita Rana, Alexander Boltz, Veena Dubal, and Min Kyung Lee.
2024. Data probes as boundary objects for technology policy design: demystifying

CHIWORK ’26, June 22–25, 2026, Linz, Austria Imteyaz et al.
technology for policymakers and aligning stakeholder objectives in rideshare gig
work. InProceedings of the 2024 CHI Conference on Human Factors in Computing
Systems. 1–21.

Upskilling with Generative AI: Practices and Challenges for Freelance Knowledge Workers CHIWORK ’26, June 22–25, 2026, Linz, Austria
A Appendix
A.1 Survey Participant Table
Table 2: Participant Demographics: Survey Respondents
Variable n % Variable n %
Sex Hours per Week on Freelance/Gig Work
Female 37 52.1 0–10 hours 18 25.4
Male 33 46.5 11–20 hours 22 31.0
Not disclosed 1 1.4 21–30 hours 16 22.5
31–40 hours 15 21.1
Age Experience Working as a Freelancer
18–24 17 23.9 < 1 year 1 1.4
25–34 39 54.9 1–2 years 23 32.4
35–44 13 18.3 2–3 years 25 35.2
45–55 1 1.4 4–5 years 13 18.3
55+ 1 1.4 > 5 years 9 12.7
Highest Level of Education
High school 2 2.8
Some college 8 11.3
Bachelor’s 43 60.6
Master’s 17 23.9
Doctoral 1 1.4
A.2 Interview Participant Table
Table 3: Demographics and professional background of interview participants ( 𝑁= 20). All participants hold a Bachelor’s
degree unless otherwise noted.
ID Age Gender Degree Experience Platforms Area of Expertise
P1 27 F Doctorate 5+ yrs Upwork Strategy & Marketing
P2 29 M Bachelor’s 1–2 yrs Upwork Security Engineering
P3 31 M Bachelor’s 2–3 yrs Upwork Virtual Assistant
P4 28 F Bachelor’s 5+ yrs Upwork Content & Administration
P5 23 M Bachelor’s 1–2 yrs Upwork AI Engineering
P6 24 F Bachelor’s 2–3 yrs Upwork UI/UX Design
P7 25 F Bachelor’s 4–5 yrs MTurk, Upwork Graphic Design
P8 30 F Bachelor’s 4–5 yrs Upwork Virtual Assistant
P9 25 F Bachelor’s 4–5 yrs Upwork Digital Marketing
P10 22 M Bachelor’s 1–2 yrs Upwork Copywriting & Email Marketing
P11 21 M Bachelor’s 2–3 yrs Upwork Graphic Design
P12 22 F Bachelor’s 2–3 yrs Upwork Virtual Assistant
P13 29 M Bachelor’s 4–5 yrs Upwork Virtual Assistant
P14 23 F Bachelor’s 1–2 yrs Upwork, LinkedIn Virtual Assistant & Graphic Design
P15 32 M Bachelor’s 5+ yrs Freelancer.com, Upwork Software Engineering
P16 22 F Bachelor’s 1–2 yrs Upwork Virtual Assistant & Data Entry
P17 24 F Bachelor’s 5+ yrs Facebook Groups, Upwork Digital Marketing & Writing
P18 25 M Bachelor’s 1–2 yrs Upwork, Fiverr Cloud Solutions Architect
P19 27 F Bachelor’s 2–3 yrs Upwork Product Management
P20 28 F Bachelor’s 2–3 yrs Upwork Talent Acquisition & Recruiting
