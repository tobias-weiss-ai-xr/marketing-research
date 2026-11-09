---
title: 'AI in the Enterprise: How People Use M365 Copilot Chat'
url: https://arxiv.org/abs/2605.23958
category: digital-marketing
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Scott Counts
- Yan Chen
- Jing Dong
- Himanshu Sharma
- Andrey Zaikin
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.23958
pages: 37
chars: 92639
fetched_at: '2026-11-08T13:07:56+00:00'
kb_version: 1
---

# AI in the Enterprise: How People Use M365 Copilot Chat

AI in the Enterprise:
How People Use M365 Copilot Chat∗
Scott Counts, Yan Chen†, Jing Dong †, Himanshu Sharma †
Andrey Zaikin†, Rui Hu, Alperen Kok, Gorkem Ozer Yilmaz,
Siddharth Suri, Kiran Tomlinson, Sonia Jaffe, Will Wang
†Equal contribution, alphabetical by last name
Microsoft Corporation
One Microsoft Way, Redmond, W A 98052, USA
Abstract
M365 Copilot is used every week by millions of people across more than a million
companies around the world as part of their workflows. Uniquely positioned in the
AI landscape given its near-exclusive use for work purposes, M365 Copilot can offer a
clear picture of how people use AI for work and where that usage may expand next.
This paper characterizes that usage through direct classification of user interactions
with M365 Copilot Chat. Based on an anonymized and privacy-preserving analysis of a
sample of approximately 5.5 million sessions, we combine a learned classification of user
intent with a classification of O*NET work activities done with M365 Copilot Chat.
We find that M365 Copilot is emerging as an everyday assistant for knowledge work:
writing dominates, but users also rely on it for information retrieval, analysis, decision
making and strategizing, and evaluating and diagnosing programs and systems, among
others. Information seeking tasks remain common, but time trends suggest a relative
shift away from “chat as search” and toward content and communication-related work.
Comparisons across occupational groupings and to work done in the labor market
further show that usage is broad but uneven, where the relative share of work done
with M365 Copilot Chat cuts across jobs in some cases and is occupation-specific in
others. Areas of relative underrepresentation in the labor market suggest the next
frontier for enterprise AI adoption.
∗We thank David Tittsworth for classification pipeline engineering and Dhruv Joshi for language on data
privacy and general feedback.
arXiv:2605.23958v1  [cs.CY]  11 May 2026

1 Introduction
M365 Copilot is an AI platform used by people in over a million companies around the world
as part of their weekly workflows. As such, its usage offers a distinctive window into one of
the most important questions of our time: how is AI being incorporated into everyday work?
To answer that question, we need direct measurement of real-world enterprise AI usage to
assess what people are using AI for, how those uses cluster across kinds of work, and where
adoption remains thin relative to the work people do. Thus, our aims are two-fold: first, to
present an empirical characterization of M365 Copilot Chat 1 based on direct measurement
of user-Copilot conversations; and second, to use that characterization to identify where
enterprise AI is already becoming an everyday assistant for knowledge work and where
deeper adoption may still lie ahead.
These questions are important because the impact of AI on work may be profound. The
growth of M365 Copilot, along with other AI services, has pushed AI to the forefront can-
didate as the next general-purpose technology [Bresnahan and Trajtenberg, 1995, Eloundou
et al., 2024]. Estimates of the resulting economic impact range from small but non-trivial
[Acemoglu, 2024] to substantial [Collis and Brynjolfsson, 2025] to the possibility of econom-
ically transformative productivity growth at 3 – 5x historical averages [Brynjolfsson et al.,
2025a]. These estimates vary widely and are likely to shift as frontier capabilities emerge, as
cost for training and inference at scale decreases, and as the technology becomes embedded
in workflows. What remains especially important, then, is understanding not only what AI
may be capable of in principle, but how it is already being used in practice.
AI has already seen considerable adoption, both generally [Chatterji et al., 2025] and for
work specifically. Results from the Real-Time Population Survey show that 23% of workers
in the U.S. used AI weekly for work in 2024, with 9% using it daily [Bick et al., 2026].
Similarly, a Gallup poll found that the percent of U.S. employees that use AI at work a few
times per year or more has doubled since 2023 to 40% in 2025, with 19% using it weekly
and 8% daily [Pendell, 2025]. Further, emerging research shows this usage translates to
productivity gains and time savings [Dillon et al., 2025], both generally [Jaffe et al., 2024]
and in specific task areas like writing [Noy and Zhang, 2023] and domains such as software
development [Peng et al., 2023, Cui et al., 2026] and customer support [Brynjolfsson et al.,
2025b]. But usage data from broad consumer platforms can only partially answer how AI is
being used inside work itself. M365 Copilot is unusually informative in this regard because
its usage is overwhelmingly work-related and embedded in enterprise workflows.
Our analyses show that M365 Copilot is becoming an everyday assistant for knowledge
1Referred to throughout for simplicity as M365 Copilot.
1

work. Across user intents and O*NET work activities, the most common uses center on
writing and editing, information retrieval including company-specific information seeking,
analysis, decision making and strategizing, and communication. When we distinguish be-
tween the user side of the conversation (user goal) and the M365 Copilot side (Copilot
action), the activities that most strongly skew toward Copilot center on providing infor-
mation, advice, and other forms of assistance. Taken together, these patterns suggest that
enterprise AI is already being used not as a narrow capability for a small set of tasks, but
as a broadly useful layer in day-to-day knowledge work.
At the same time, our data show that usage is broad but uneven. Prior work already
suggests that AI use is concentrated in knowledge work and communication tasks and is far
less prevalent in physical-world work [Tomlinson et al., 2025, Handa et al., 2025, Eloundou
et al., 2024]. Our findings corroborate this skew, but they also sharpen it by showing where
enterprise AI appears underused relative to the work done in industries, occupations, and
the labor market more broadly. Comparing M365 Copilot activity with work distributions in
Banking, Consulting, and Manufacturing, and across occupational groupings, reveals both
work activities that are absent from current usage and activities that are present but un-
derrepresented. These underrepresented areas point to a next frontier for enterprise AI: not
adoption in general, but deeper adoption across underused work.
Most companies are comprised of many job roles regardless of industry. We thus comple-
ment our industry comparison by looking at usage across occupational aggregations. Here
we find usage patterns that both cut across and are uniquely indicative of different job fam-
ilies, again highlighting the broadandspecialized nature of M365 Copilot usage and also
suggesting areas for job-specific AI functionality. We compare the share of M365 Copilot
usage in different work activities to expectation based on the fraction of the labor force
that do those work activities. Some activities such as those related toGetting Information
are overrepresented, while others fall below expectation. Work activities underrepresented
compared to the size of the relevant workforce present a third view on areas for potential
growth of AI.
Our ability to answer these questions around the impact of AI on work is enabled by
direct measurement of the activities done with AI for work. We do this through two clas-
sification schemes, O*NET [National Center for O*NET Development, 2024] from the U.S.
Department of Labor and a bottom-up learned intent taxonomy to directly measure the
types of tasks done. The O*NET taxonomy allows us to compare the amount of different
types of work done with M365 Copilot to the amount of the same work in the labor market
as a whole (see Brynjolfsson and Mitchell [2017], Brynjolfsson et al. [2018] for early use of
this technique), and to use of other AI platforms characterized with the same classification
2

taxonomy [Chatterji et al., 2025, Handa et al., 2025, Appel et al., 2025, Massenkoff et al.,
2026, Appel et al., 2026, Tomlinson et al., 2025, Eloundou et al., 2024]. The intent taxonomy
provides a general characterization of the nature of usage—what are people doing and how
frequently—that supports a broad-based understanding in a taxonomy native to AI usage in
the unique productivity-centric context afforded by M365. Given the similarity between our
intent taxonomy and that of Chatterji et al. [2025], we are also able to compare user intent
in M365 Copilot to that in ChatGPT.
The bulk of this paper characterizes the degree and nature of use of M365 Copilot across
these intent and work activity classifications to support two theses: first, that enterprise
AI is becoming an everyday assistant for knowledge work; and second, that a possible next
frontier is deeper adoption across underused work. Key findings:
•M365 Copilot sees broad use across occupations and has areas for growth.While some
user intents such asContent Refinementare frequent regardless of occupation, there
is a long tail of usage types. Within that long tail, industry and occupational com-
parisons reveal work activities where the share of M365 Copilot is underrepresented
compared to expectation based on the labor market generally. Some examples: the
share ofEvaluate the quality or accuracy of datais lower than expected in the Banking
industry; almost half of work activities done by employees in consulting are absent
in M365 Copilot usage; the share of work activities involvingDocumenting/Recording
Informationis lower than expected given the size of workforce that do those activities.
Underrepresented usage indicates potential growth areas.
•M365 Copilot has unique usage compared to ChatGPT.Writing dominates both plat-
forms, but M365 Copilot sees more usage for decision making and problem solving,
analyzing and processing information, getting technical help, and obtaining informa-
tion, especially company-specific information. ChatGPT skews toward ideation in the
form of creative thinking and interpreting information.
•Users may be shifting away from “chat as search”.We see a 5% drop in theInformation
Inquiryshare of all user intent in our intent time series data. As shares of activity,
this may be due to an increase in other types of usage rather than a decrease in the
amount of information seeking done with M365 Copilot. Many occupations do more
Content RefinementthanInformation Inquirywith M365 Copilot.
•Use of M365 Copilot generally is assistive toward user goals.Work activities that skew
most toward the M365 Copilot side of user interactions center on advising and evalu-
ating products, services, or technologies, assisting with paperwork and other services,
3

and providing information for various purposes.
•M365 Copilot targets information work.This skew is expected. However, tracking the
relevance of M365 Copilot to the full range of work can quantify the disparity and
help identify emerging use cases. Our analyses of intent by occupational groups and
job family “AI applicability profiles” quantify the gap in the relevance of AI to some
classes of work over others, and provide views into potential growth of AI that may
cross industrial boundaries.
2 Data & Method
2.1 What is M365 Copilot
Microsoft 365 Copilot is an AI-powered assistant embedded in Microsoft 365 applications
that combines large language models with organizational data from Microsoft Graph, such as
files, emails, and meeting transcripts, and web-grounded information for productivity tasks.
Since its general availability for enterprises on November 1, 2023, Copilot has been available
worldwide in Microsoft’s public clouds and is now used by nearly 70% of the Fortune 500 2
and globally by more than a million companies. Based on direct classification of usage, we
estimate that between 82% - 89% of M365 Copilot Chat usage is for work purposes, with
about 10% for personal purposes, a stark difference from the 27% of ChatGPT usage for
work [Chatterji et al., 2025]. The user experience for M365 Copilot includes both stand-alone
chat, app-embedded chat (in the side pane of Word, for instance), and on-canvas interaction
(summarize an email thread in Outlook). All data used here were drawn only from M365
Copilot Chat, and thus does not include on-canvas in-application usage. Because M365
Copilot is embedded in the applications where enterprise knowledge work already happens,
usage logs offer a direct window into how AI is being woven into everyday work, rather than
how people experiment with a stand-alone chatbot.
2.2 Data
We used five datasets, each derived from a sample of conversations between a user and M365
Copilot, all of which were performed securely using an “eyes-off” environment, meaning
that no raw data was ever accessible directly for human review. Only anonymized and
aggregated quantities, such as the percentages of each intent class, were egressed from the
eyes-off data environment and only after thorough review and approval by Microsoft’s privacy
2Reported in Microsoft earnings on October 30, 2024.
4

and compliance processes. All aggregations were based on at least 5 users from 5 enterprise
customer tenants, though the vast majority were derived from much larger samples. Finally,
data subject to EU Data Boundary isolation was excluded from this analysis, as were data
from educational institutions. We also aggregate our user intent datasets by Occupational
Group, which consist of groups of users with job titles clustered using an LLM-based classifier.
(see Appendix Figure A2 for the full list of Occupational Groups). Occupation Group
aggregations followed the same privacy and compliance approved processes as other data
aggregations.
Intent dataset (primary): Our primary intent analyses were based on a sample of 175,274
M365 Copilot user prompts from the week of February 16 through February 22, 2026. The
intent dataset was sampled randomly from the entire M365 Copilot Chat prompt corpus,
aside from data subject to EU Data boundary isolation and educational institutions, includ-
ing both free and paid users.
Intent dataset (time series): Our time trend dataset for user intent was compiled from
a sample of approximately 310,000 conversations per week, sampled over a 114 day period
from June 1, 2025 to September 22, 2025, yielding a total sample of 5,342,156 prompts.
Work activity dataset (primary): Primary analyses of O*NET work activities were con-
ducted on a dataset of 105,000 randomly sampled M365 Copilot conversations from global
enterprise users, excluding data subject to EU Data Boundary restrictions and educational
institutions. Sampling occurred at a rate of 15,000 conversations per day between February
14 and February 21, 2026. Each work activity analysis dataset included the entire Copilot
conversation, encompassing both user prompts and Copilot responses.
Work Activity dataset (industry): To compare M365 usage across industries we sampled
conversations from a selected set of 5-11 companies demonstrating significant M365 Copilot
adoption with sustained user activity in each of three industries:Banking,Discrete Manu-
facturing(referred to throughout asManufacturing), andIT Services & Business Advisory
(referred to throughout asConsulting). Approximately 2,500 conversations per day were
sampled randomly from each industry over the week February 14 – February 21, 2025, for
a total of approximately 52,000 split evenly into 17,500 per industry. Sampling matched
amounts across Banking, Manufacturing, and Consulting lets us compare how the same AI
assistant is taken up in industries with different work mixes, which is central to identifying
where enterprise AI is already established and where adoption still has room to grow.
5

2.3 Intent Classification
2.3.1 Taxonomy Creation
The user intent taxonomy consisted of two hierarchical levels, a top-level intent and secondary
intents within each of the top-level intent classes. The intent classes were created by merging
two sets of candidate intents, one learned by running the TnT-LLM taxonomy generation
process [Wan et al., 2024] on the WildChat corpus of ChatGPT conversations [Zhao et al.,
2024], and the second drawn from categories curated from product managers. The learned
taxonomy from WildChat data provides bottom-up taxonomy creation, while the curated
intents ensures relevance to M365 Copilot. The final set of intents was used in a system
prompt for classification. The system prompt was created and refined through an iterative
process by continuing to provide correct and incorrect classification examples from WildChat
data while the LLM classifier continued to classify the validation set more accurately without
regressing on the test set.
2.3.2 Classification
The intent classification was based on one user prompt per M365 Copilot conversation. The
specific user prompt chosen from a given conversation was selected at random but the LLM-
based intent classification of that prompt included three other user prompts from the same
conversation as context. This strategy supports random selection of the user prompt for
classification rather than always using the initial user prompt, for example, while ensuring
sufficient context should the selected user prompt be ambiguous in isolation (e.g., “give me 10
more”). The chosen user prompt was classified using the system prompt in two passes, first
for top-level intents (e.g.,Information Inquiry,Content Generation,Ideation and Planning,
Programming Assistance, etc.) and then for secondary intents. GPT 4.1-mini was used for
all intent classification.
2.4 Work Activity Classification
Work activity classification used the procedure developed by Tomlinson et al. [2025], in which
work activities detected in Copilot conversations are based on the O*NET classification
maintained by the Department of Labor [National Center for O*NET Development, 2024].
O*NET is a hierarchical classification system that decomposes work done by occupations into
tasks (most granular), detailed work activities, intermediate work activities, and generalized
work activities (least granular). We classified M365 Copilot conversations based on the
intermediate work activities (IW As) they contain.
6

The IW A classification itself was performed in near identical fashion to Tomlinson et al.
[2025]. A prompt (GPT-4.1-mini) and embedding-based (text-embedding-3-small) classifi-
cation pipeline was used to identify all IW As present in each M365 Copilot conversation,
separately on the user (referred to as theuser goal) and Copilot (referred to as theCopilot
action) side of the conversation. In one minor departure from Tomlinson et al. [2025], for
performance reasons, when selecting the matched IW A from the set of potential candidates,
we used only the top 20 most likely candidate IW As. In accordance with Tomlinson et al.
[2025] we set a frequency threshold of 0.05% for IW A inclusion in all analyses to minimize
the possibility of including falsely detected IW As, where IW A frequency was determined by
afractional countof IW As detected in a given conversation. That is, for a conversation with
kmatching IW As, each matching IW A receives a fractional count of 1/k, so the sum of all
IW A fractional counts equals the number of conversations.
The O*NET taxonomy contains 332 IW As. Table 1 shows the count of fractional user
goal IW As and Copilot action IW As, as well as the number of unique IW As for each O*NET
dataset after removing IW As below the 0.05% activity share threshold. In terms of non-
fractional raw counts of IW As, most conversations had more than one IW A on both the user
goal and Copilot actions sides of the conversation. For our primary O*NET dataset, we see
176,803 absolute instances of user goal IW As and 342,471 Copilot action IW As. Thus in
terms of sheer number of work activities detected in the overall sample, the number of work
activities being performed by Copilot (3.26 per conversation) approaches double that of the
work activities in user goals (1.68 per conversation).
T able 1:Summary of M365 Copilot datasets for work activity analyses
Dataset User Goal, # IW As (fractional count) Copilot Action, # IW As (fractional count) Unique IW As
Primary 70,068 86,361 169
Industry 52,286 58,271 178
We also classified the scope of the IW A being done and whether it was completed. Scope
uses a 6-point Likert scale of none, minimal, limited, moderate, significant, and complete,
with all analyses based on the percentage of matched conversations in which an IW A’s scope
was ‘significant’ or higher, thescope score. Completion uses a 3-point Likert scale of not
complete, partially complete, and complete, with all analyses based on the percentage of
instances in which the per-IW A completion was equal to ‘complete,’ called thecompletion
rate. As our measures were identical to those in Tomlinson et al. [2025], we refer readers to
that work for validation, which was done with human raters or with explicit thumbs up/down
feedback from users.
7

We used two measures related to work activity. First, we used activity share, which was
the percent of total IW As accounted for by each IW A using fractional share as defined above.
If a dataset had a fractional count total of 100 IW As and a given IW A had a fractional count
total of 10, then its activity share would be 0.10. Second, we used the AI applicability score,
as defined in Tomlinson et al. [2025], which combines the activity share with the scope and
completion rate as defined above. In our work we aggregated AI applicability scores from
IW As to job families and to GW As as,
GW Auser i = X
j∈IW As(i)
1[f user j ≥0.0005]c user j suser j wij,(1)
where IW As(i) is the set of IW As mapping to GW Ai,f user j is the user goal activity share of
j,c user j is the task completion rate of conversations with IW Ajas a user goal, ands user j is
the fraction of conversations with user goaljin which the scope classification is moderate or
above. AI applicability for M365 Copilot actions is computed equivalently, and the overall
AI applicability for an IW A, GW A, or job family is the average of the user goal and M365
Copilot action AI applicability scores.
8

3 Results
3.1 User Intent
3.1.1 Top-level Intent
Figure 1 shows the distribution of user prompts in each top-level intent class.Information
InquiryandContent Refinementaccount for almost 60% of user prompts. Other forms of
content work including generation, as well as programming assistance and analytical reason-
ing account for about 20% of user prompts. Content summarization, ideation and planning,
and meeting-related activity account for about 7% of usage, and the bulk of the remaining
content (about 8%) are ambiguous/other. Confirming the use of M365 Copilot for work
purposes, only a little over 2% of user prompts are for informal exchange or entertainment.
Together, the concentration of usage in information inquiry and content work, and the near-
absence of recreational use, are consistent with M365 Copilot functioning as an everyday
assistant for enterprise knowledge work rather than as a general-purpose chatbot.
0.0 0.1 0.2 0.3
Leisure & Recreation
Contextual Update
Skill Acquisition
Ideation & Planning
Meeting Management
Informal Exchange
Analytical Reasoning
Content Summarization
Programming Assistance
Content Generation
Content Refinement
Information Inquiry
Fraction of User Prompts
Figure 1:Fraction of user prompts for top-level intent
3.1.2 Second-level Intent
For more detail, Figure 2 shows the second-level intents for the six most frequent top-level
intents. We observe that almost one quarter of all usage is for editing text for content
refinement, followed by about 10% of usage for asking general information questions. The
9

distributions of the second-level intents underscore the broad, general purpose utility of
M365 Copilot, spanning tasks from summarizing emails and files to specialized activities.
The set of second-level intents that account for two percent or more of user prompts includes
everything from asking for research and technical support to troubleshooting code to creating
reports and PowerPoints. Data analysis, including Excel data analysis, account for 1.5% and
image analysis account for about half of a percent of overall user prompts. In summary, while
content rewriting or editing and general information question asking dominate with about
one third of user prompts, the remaining two-thirds falls across a wide range of activities.
0.000 0.025 0.050 0.075
Chat Inquiry
App Inquiry
Personal Inquiry
Assistant Inquiry
Doc Inquiry
Email Inquiry
Profile Inquiry
T argeted Retrieval
Research Compare
T ech Support
Explain Concepts
How-T o Guidance
Enterprise Inquiry
Info Query
0.0000.0500.1000.1500.200
Proofread
Edit
0.0000.0050.0100.0150.020
Music Composition
Promo Content
Copywriting
Event Planning
Onboarding Docs
Media Communication
Multimedia
Presentation
Compose Email
Visual Content
Translation
T ext Composition
Report Generation
0.000 0.010 0.020
System Design
Explain Concepts
Debugging
Coding
0.000 0.005 0.010
Hybrid Data
User Visual Content
Public Data
Enterprise Data
Single Meeting
Multiple Meetings
Document
Email
User T ext Data
0.000 0.002 0.004 0.006
Workflow Optimize
Stat Analysis
Financial Planning
Hybrid Comparison
Legal Guidance
Doc Comparison
General Comparison
Financial Analysis
Image Analysis
Math Reasoning
Action Advice
Data Analysis
Excel Data Analysis
Fraction of User Prompts
Information
Inquiry (0.32)
Content
Refinement (0.26)
Content
Generation (0.09)
Programming
Assistance (0.07)
Content
Summarization (0.05)
Analytical
Reasoning (0.04)
Figure 2:Second-level intents for each of the top 6 most frequent top-level intents. See Appendix
Figure A1 for all second and first-level intent frequencies.
3.1.3 Intent Comparison to ChatGPT
For comparison and generalization, we compare user intent in M365 Copilot to user intent
in ChatGPT, as reported by Chatterji et al. [2025]. Because we do not use the same intent
taxonomy, we manually mapped our second-level intent classes to the topics from OpenAI.
For instance,Analyze Imagein ourAnalyzetop-level intent maps toMultimediain the
OpenAI taxonomy, whileAnalyze Excel Datamaps toTechnical Help.
Figure 3 shows the distribution of M365 intents mapped to the OpenAI topic taxonomy.
When compared to the subset of ChatGPT for work-related purposes, both services exhibit
10

a dominant share ofWritingas the most frequent user intent. Curiously, M365 Copilot and
ChatGPT for work appear nearly reversed with respect to seeking information and practical
guidance. This divergence may stem from M365 Copilot’s integration with organizational
data, where company-specific information-seeking accounts for roughly one third ofSeeking
Informationintents, an aspect that is presumably minimally present in ChatGPT if at all.
Furthermore, M365 Copilot has a higher proportion ofTechnical Help(14%) compared to
ChatGPT for work (10%). These differences with ChatGPT highlight usage of M365 Copilot
as a more work-dedicated AI assistant.
0.0 0.1 0.2 0.3 0.4
Self-Expression
Other/Unclear
Multimedia
T echnical Help
Seeking Information
Practical Guidance
Writing
Fraction of User Prompts
6HUYLFH
0&RSLORW
&KDW*37:RUN

&KDW*37$OO

Figure 3:M365 Copilot and ChatGPT intents, mapped to the OpenAI topic taxonomy.
3.1.4 Intent Over Time
Given the rapid pace of adoption of AI (e.g., Chatterji et al. [2025], Microsoft [2025], Misra
et al. [2025]), how is usage changing as more people use, learn to use, and develop usage
habits with AI? We look for changes in user intent over the 114 day period (June 1, 2025 -
September 22, 2025) in our intent time series dataset. Importantly, these changes are relative
to the overall sample of intent at each point in time and thus should be interpreted only
as a distribution that evolves over time to reflect a changing balance of usage.Information
Inquiry, while still the most frequent intent, declined from 38% of user intents to 33%, a
13% relative decline. In contrast,Content Refinementrose from less than 22% to 28.5%
11

for a relative increase of 32%. Together, these two big shifts suggest users moving away
from use of M365 Copilot for search and information lookup use and toward drafting and
polishing of content. The generation of content itself has remained constant. This shift
away from information lookup and toward content refinement is one of the clearest signals
in our data that the role of M365 Copilot is deepening over time: users are moving beyond
chat-as-search and toward using the assistant as a working collaborator in the production
of content. Movement of this kind, away from the most basic interaction mode and into
more substantive work, suggests that, as enterprise AI adoption progresses, the assistant
becomes more deeply embedded in day-to-day work. Finally, we highlight a drop in the
share of intent forProgramming Assistance, potentially attributable to increasing use of
Github Copilot and other IDE-embedded AI tools, though attributing this decrease to such
a shift requires confirmation.
0.0
0.1
0.2
0.3
Jun Jul Aug Sep
Date
Fraction of User Intent
Top−level Intent
Information Inquiry
Content Refinement
Content Generation
Programming Assistance
Analytical Reasoning
Ambiguous Intent
Content Summarization
Other
Informal Exchange
Ideation & Planning
Meeting Management
Skill Acquisition
Contextual Update
Leisure & Recreation
Figure 4:Fractional share of top-level intents over time. Data were sampled daily from June 1 -
September 22, 2025. Values are averaged over rolling past 28 days.
3.1.5 Intent by Industry and Occupation
We subset our intent data based on the originating company of each M365 Copilot prompt
and aggregate to the same three example industries as in our O*NET industry dataset:
Banking,ManufacturingandConsulting. Figure 5 shows thatInformation Inquirydomi-
nates, with more than 30% of intent in each industry, thoughBankingtrails the all-industry
mean, followed byContent Refinement.
12

Manufacturingsits notably above the all industry mean forInformation Inquiryand
below the all industry mean forContent Refinement.Programming Assistanceis one intent
where the industries are somewhat spaced out, especially relative to its share of all user intent.
HereManufacturing(9.39%) sees nearly double the share ofProgramming Assistanceas in
Consulting(5.25%). We remind readers that these are relative shares. One industry could
have both a larger absolute amount and smaller relative share of user intent in an intent
class compared to another industry.
Leisure & Recreation
Contextual Update
Skill Acquisition
Ideation & Planning
Meeting Management
Informal Exchange
Content Summarization
Other
Analytical Reasoning
Ambiguous Intent
Programming Assistance
Content Generation
Content Refinement
Information Inquiry
0.0 0.1 0.2 0.3
Fraction of Intent
Industry
All
Banking
Consulting
Manufacturing
Figure 5:Top-level intents for three example industries, with the average across all 37 industries
shown for reference. Data were sampled daily from Feb 16-22, 2026.
We turn now to our examination of top-level user intent across Occupational Groups
(Figure 6). We see that some intents account for a larger share of usage (e.g.,Content Re-
finement) across all Occupational Groups, while others a lower share (Content Summariza-
tion), highlighting functionality broadly applicable regardless of type of occupation. There
are, however, many user intents with elevated relevance to specific Occupational Groups.
Content Generationstands out forCreative Arts & Entertainment(16%), andMarketing
& Advertising(15%).Programminghas more than double the fraction of user intent in
Software Development and ITandResearch and Data Analysisthan the global average. A
range of Occupational Groups are high inContent Refinement, includingReal Estate and
Property Management,Customer Support and Service,Human Resources and Administra-
tion, andMarketing and Advertising. For all Occupation Groups crossed with all top-level
intents, see Appendix Figure A2.
13

0.02 0.11 0.31 0.04 0.34 0.04
0 0.16 0.26 0.04 0.33 0.05
0.03 0.1 0.32 0.04 0.29 0.02
0.05 0.08 0.19 0.03 0.39 0.1
0.04 0.12 0.31 0.04 0.28 0.05
0.04 0.15 0.35 0.04 0.26 0.02
0.03 0.11 0.38 0.02 0.3 0
0.05 0.08 0.21 0.03 0.34 0.16
0.04 0.07 0.17 0.03 0.37 0.2
Analytical
Reasoning
Content
Refinement
Information
Inquiry
Content
Generation
Content
Summarization
Programming
Assistance
Software Development & IT
Research & Data Analysis
Real Estate & Property Management
Marketing & Advertising
Human Resources & Administration
Engineering & Architecture
Customer Support & Service
Creative Arts & Entertainment
Content Creation & Journalism
Figure 6:Share of top-level user intent by Occupational Group. For the full intersection of all
Occupational Groups by all top-level user intents, see Appendix Figure A2.
We generalize the analysis of relationships in the share distributions of the intents over
Occupational Groups by clustering the intents. The resulting 4-cluster solution is shown
in Table 2. Cluster 1 encompasses information, skill, and technical usage, Cluster 2 is
about content work, Cluster 3 about meetings and staying current with communication and
coordination, and Cluster 4 about skill acquisition and non-work.
Together, these industry and occupational comparisons show the broad-but-uneven shape
of enterprise AI adoption. Some intents, most notablyContent Refinement, are used heavily
across nearly every occupation, suggesting that M365 Copilot is already serving as an every-
day assistant cutting across occupational boundaries. At the same time, the modest inverse
relationship betweenInformation InquiryandContent Refinement, and the sharp differences
in programming-related use across industries, show that occupations and industries put the
assistant to very different uses. Where an intent is common in some occupations or industries
and rare in others, the gap itself marks a plausible direction for deeper adoption.
T able 2:Top-level intent clustered based on distribution of intent share over Occupational Groups.
Analytical Content Meeting Social
Analytical Reasoning
Information Inquiry
Programming Assistance
Content Generation
Content Refinement
Informal Exchange
Content Summarization
Contextual Update
Meeting Management
Ideation & Planning
Skill Acquisition
Leisure & Recreation
14

3.2 Work Activities
3.2.1 Generalized Work Activities
Our analysis of work activities starts with characterizing work activities performed with
M365 Copilot through the aggregation of intermediate work activities (IW As) into gener-
alized work activities (GW As) using the mapping provided by O*NET. This provides a
comprehensive view of work done with and by M365 Copilot in a single set of the 35 (of
37 possible) GW As seen in our data (Figure 7). Recall that we separately classify the work
activities on the user side of the conversation (user goal) and the M365 Copilot side (Copilot
action). Top user goal GW As center on information work, notablyMaking Decisions and
Solving Problems, Communicating with Supervisors, Peers, or Subordinates, andDocument-
ing/Recording Information. Copilot actions show a similar skew toward information-centric
tasks, with a stronger emphasis on interpreting information, providing consultation and
supporting communication.
Performing General Physical Activities
Repairing and Maintaining Mechanical Equipment
Monitoring and Controlling Resources
Updating and Using Relevant Knowledge
Establishing and Maintaining Interpersonal Relationships
Identifying Objects, Actions, and Events
Staffing Organizational Units
Guiding, Directing, and Motivating Subordinates
Resolving Conflicts and Negotiating with Others
Selling or Influencing Others
Handling and Moving Objects
Scheduling Work and Activities
Training and Teaching Others
Inspecting Equipment, Structures, or Material
Coaching and Developing Others
Organizing, Planning, and Prioritizing Work
Monitor Processes, Materials, or Surroundings
Estimating Characteristics of Products, Events, or Information
Developing Objectives and Strategies
Performing for or Working Directly with the Public
Performing Administrative Activities
Evaluating Information to Determine Compliance with Standards
Judging the Qualities of Things, Services, or People
Assisting and Caring for Others
Processing Information
Interacting With Computers
Thinking Creatively
Analyzing Data or Information
Provide Consultation and Advice to Others
Communicating with Persons Outside Organization
Interpreting the Meaning of Information for Others
Communicating with Supervisors, Peers, or Subordinates
Getting Information
Documenting/Recording Information
Making Decisions and Solving Problems
0.0 0.1 0.2
Fraction of total activity
Copilot Action
User Goal
Figure 7:Fraction of each generalized work activity (GW A) for User Goal and Copilot Action
15

3.2.2 Intermediate Work Activities
We now examine intermediate work activities (IW As) performed by users with Copilot as-
sistance. Looking at the most frequent intermediate work activities (Figure 8) done by
users, writing and editing dominates, accounting for more than 20% of activity. Other fre-
quent IW As reflect information work activities such as examining and preparing materials,
communicating project details, gathering and analyzing data, diagnosing problems, and im-
plementing procedures. Copilot actions appear largely complementary, with many top IW As
reflecting assistance, advice, and explanation given about technical details, regulations, and
financial information.
Research healthcare issues
Document technical designs, procedures, or activities
Explain regulations, policies, or procedures
Provide information to guests, clients, or customers
Calculate financial data
Evaluate the characteristics of technologies
Explain financial information
Diagnose system or equipment problems
Write material for artistic or commercial purposes
Gather data about operational or development activities
Implement procedures or processes
Resolve computer problems
Process digital or online data
Explain technical details of products or services
Create visual designs or displays
Compile records, documentation, or other data
Examine materials for accuracy, compliance
Obtain information about goods or services
Gather information from physical or electronic sources
Prepare reports of operational activities
Communicate specifics, project details
Communicate operational plans, activities
Read materials to inform work processes
Prepare informational or instructional materials
Edit written materials or documents
0.00 0.05 0.10 0.15 0.20
Fraction of activity
(a) Top IW As: User Goal
Evaluate programs, practices, or processes
Issue documentation
Develop operational or technical procedures or standards
Write material for artistic or commercial purposes
Create visual designs or displays
Provide information or assistance to the public
Examine materials for accuracy, compliance
Advise others on business or operational matters
Explain financial information
Assist others to access services or resources
Explain regulations, policies, or procedures
Compile records, documentation, or other data
Respond to customer problems or inquiries
Present research or technical information
Prepare reports of operational activities
Communicate operational plans, activities
Advise others on products or services
Assist individuals with paperwork
Advise others on the design or use of technologies
Explain technical details of products or services
Communicate specifics, project details
Prepare informational or instructional materials
Read materials to inform work processes
Provide information to guests, clients, or customers
Edit written materials or documents
0.00 0.05 0.10 0.15
Fraction of activity (b) Top IW As: Copilot Action
Figure 8:Top 25 most frequent IW As for user goal (a) and Copilot action (b). Note different
x-axis scales.
The top 25 IW As reflect “head of curve” information work tasks more common across
occupations, but they don’t tell the whole story. In fact, these top 25 account for only two-
thirds of all user goal IW A instances and three-quarters of Copilot action IW A instances.
In other words, about 30% of all work activities fall into the “long tail” of activities done
with Copilot. Table 3 shows example IW As that are reasonably frequent but fall outside the
top 25. The breadth of this long tail shows that users are already bringing a wide range of
work activities to the assistant beyond the most frequent ones. It also points to where usage
might grow. See Appendix Table 5 for a full list of IW A frequencies.
16

3.2.3 User Goal and Copilot Action
In addition to the overall distribution of activities, we can also examine how the user side
and the Copilot side of each conversation differ in their activity mixes. Returning to the
question of the ways in which the goals of users deviate from the action taken by Copilot,
Figure 9 highlights the IW As that skew toward one or the other. User goals tend to emphasize
data and information gathering, financial work, and administrative tasks, whereas Copilot
actions predominantly focus on advising, assisting, and providing information. The shape of
this asymmetry — users bringing tasks and information needs, and Copilot responding with
advice, assistance, and explanation — reflects Copilot’s role as an assistant for knowledge
work.
Advise others on educational or vocational matters
Advise others on financial matters
Advise others on healthcare or wellness issues
Advise others on legal or regulatory matters
Advise others on products or services
Advise others on the design or use of technologies Assist individuals with paperwork
Assist others to access additional services or resources
Assist scientists, scholars, or technical specialists with projects or research
Execute financial transactions
Explain medical information to patients or family members
Gather data about operational or development activities
Maintain health or medical records
Manage budgets or finances
Manage human resources activities
Measure physical characteristics of materials, products, or equipment
Perform recruiting or hiring activities
Provide information or assistance to the public
Purchase goods or services
Resolve computer problems
Train others to use equipment or products
0
1
2
3
4
1 2 3 4
Log count of IWAs: User
Log count of IWAs: Copilot
Figure 9:Frequency of all IW As, split into user goal and Copilot action. Labeled IW As indicate
10x more likely to be a Copilot action or 2x more likely to be a user goal.
3.2.4 Comparison to ChatGPT
For broader context and to provide a sense of the uniqueness in usage of M365 Copilot as
an exclusively productivity focused AI platform, we compare usage to that of ChatGPT
[Chatterji et al., 2025]. We draw on published ChatGPT usage reports, which enable near
17

T able 3:Example IW As outside the top 25 most frequent IW As.
User Goal Copilot Action
IW A Fraction IW A Fraction
Assess regulations or policies 0.009 Evaluate programs, practices, or processes 0.008
Respond to customer problems or inquires 0.007 Develop marketing or promotional materials 0.006
Develop technical procedures or standards 0.006 Diagnose system or equipment problems 0.007
Analyze data to improve operations 0.005 Evaluate designs, specifications 0.006
Prepare financial documents 0.005 Analyze business or financial data 0.005
apples-to-apples comparisons of GW As through common alignment with the O*NET tax-
onomy, though we note that the classification procedures and prompt structures used to
classify ChatGPT data differ somewhat from those used for Copilot classifications.
Updating and Using Relevant Knowledge
Performing for or Working Directly with the Public
Coaching and Developing Others
Handling and Moving Objects
Assisting and Caring for Others
Developing Objectives and Strategies
Selling or Influencing Others
Evaluating Information to Determine Compliance with Standards
Performing Administrative Activities
Training and Teaching Others
Processing Information
Analyzing Data or Information
Thinking Creatively
Interpreting the Meaning of Information for Others
Documenting/Recording Information
Getting Information
Making Decisions and Solving Problems
0.0 0.1 0.2
Fraction of Activity
Service
Copilot Commercial
ChatGPT (work)
ChatGPT (all)
Figure 10:GW As: M365 Copilot commerical and ChatGPT. Percents do not sum to 100% due
to limitation of publicly available ChatGPT data.
In the higher-frequency GW As shown in Figure 10, M365 Copilot is used disproportion-
ately forMaking decisions and Solving Problems, as well as for getting, processing, and
evaluating information, analyzing data, and developing strategies. By contrast, ChatGPT
displays a relative emphasis on creative thinking and interpreting information. Both services
are used heavily for documenting and recording information.
18

This divergence at the work-activity level mirrors the intent-level comparison: M365
Copilot is shaped by the analytical and decision-oriented work of enterprises, while ChatGPT
skews more toward creative and interpretive uses.
3.2.5 Labor Market, Industry, and Job Family Comparisons
We turn now to the coverage of M365 Copilot usage compared to work done in the labor
market as a whole. Figure 11 shows the GW As ordered by fraction of work in each GW A by
the labor market overall. We can see that the top GW As,Handling and Moving Objectsand
Performing General Physical Activities, which account for 23% of all labor, see effectively
no coverage by M365 Copilot. Conversely, GW As such asGetting InformationandMaking
Decisions and Solving Problems, which account for more than a quarter of the user goal
GW As account for only 6% of labor done in the workforce at large.
0.03
0.06
0
0.03
0.04
0.03
0.01
0.07
0
0.01
0.01
0.03
0.04
0.12
0
0.03
0.01
0.02
0.02
0.03
0.05
0.03
0.01
0
0.05
0.11
0.02
0.02
0.02
0.01
0
0.01
0.01
0
0.04
0.03
0.01
Establishing and Maintaining Interpersonal Relationships
Staffing Organizational Units
Organizing, Planning, and Prioritizing Work
Resolving Conflicts and Negotiating with Others
Coaching and Developing Others
Identifying Objects, Actions, and Events
Developing Objectives and Strategies
Evaluating Information to Determine Compliance with Standards
Updating and Using Relevant Knowledge
Operating Vehicles, Mechanized Devices, or Equipment
Scheduling Work and Activities
Selling or Influencing Others
Repairing and Maintaining Mechanical Equipment
Interacting With Computers
Estimating the Quantifiable Characteristics of Products, Events, or Information
Performing for or Working Directly with the Public
Processing Information
Interpreting the Meaning of Information for Others
Judging the Qualities of Things, Services, or People
Provide Consultation and Advice to Others
Making Decisions and Solving Problems
Getting Information
Training and Teaching Others
Controlling Machines and Processes
Analyzing Data or Information
Inspecting Equipment, Structures, or Material
Communicating with Persons Outside Organization
Monitoring and Controlling Resources
Thinking Creatively
Communicating with Supervisors, Peers, or Subordinates
Guiding, Directing, and Motivating Subordinates
Monitor Processes, Materials, or Surroundings
Performing Administrative Activities
Assisting and Caring for Others
Documenting/Recording Information
Performing General Physical Activities
Handling and Moving Objects
0.0 0.1 0.2
Fraction of work activity
Source
Copilot Action
User Goal
Labor Market
Figure 11:Fraction of generalized work activities (GW As) in labor market. Fraction of user goal
and M365 Copilot action skew toward information work.
These differences naturally reflect the relevance and context of M365 Copilot as an infor-
mation work technology. Given this expected divergence, for more detail, we plot the subset
of IW As seen in M365 Copilot usage, contrasting their activity share to their share in the
labor market to highlight those that skew toward either the labor market or M365 Copilot
(see Appendix Figure A4a and Figure A4b).
19

Even when restricting analysis to work activities involving M365 Copilot, we observe
discrepancies between the activity shares in the data and those weighted by workforce size.
In other words, comparing observed usage to expected usage based on the size of workforce
that does each work activity reveals notable divergence (see Figure 12). Some work activities,
such asMaking Decisions and Solving Problemssee a slightly larger share than expected,
though many are relatively underrepresented. For instance, whileDocumenting/Recording
Informationis a common work activity conducted with M365 Copilot, we would expect
even greater usage given the size of the workforce that perform those activities.Thinking
Creativelyalso sees a lower share than expected. Assuming M365 Copilot usage tends toward
the amount of different types of work done, we would expect these underrepresented areas
to grow going forward.
−0.02
0
0.01
0
0
0.01
0.01
0
0.01
−0.04
0
−0.04
0
−0.02
0
0
0.07
0.01
0.01
−0.02
0.06
0
0
0
0
0
−0.06
0
0
0
0
0
0.02
0
0
Performing General Physical Activities
Repairing and Maintaining Mechanical Equipment
Monitoring and Controlling Resources
Updating and Using Relevant Knowledge
Establishing and Maintaining Interpersonal Relationships
Identifying Objects, Actions, and Events
Staffing Organizational Units
Guiding, Directing, and Motivating Subordinates
Resolving Conflicts and Negotiating with Others
Selling or Influencing Others
Handling and Moving Objects
Scheduling Work and Activities
Training and Teaching Others
Inspecting Equipment, Structures, or Material
Coaching and Developing Others
Organizing, Planning, and Prioritizing Work
Monitor Processes, Materials, or Surroundings
Estimating Characteristics of Products, Events, or Information
Developing Objectives and Strategies
Performing for or Working Directly with the Public
Performing Administrative Activities
Evaluating Information to Determine Compliance with Standards
Judging the Qualities of Things, Services, or People
Assisting and Caring for Others
Processing Information
Interacting With Computers
Thinking Creatively
Analyzing Data or Information
Provide Consultation and Advice to Others
Communicating with Persons Outside Organization
Interpreting the Meaning of Information for Others
Communicating with Supervisors, Peers, or Subordinates
Getting Information
Documenting/Recording Information
Making Decisions and Solving Problems
0.0 0.1 0.2
Fraction of Activity
Weighted
Copilot Action
User Goal
Unweighted
Copilot Action
User Goal
Figure 12:Weighted activity share for GW As. Bars show activity share as in Figure 7. Points
show activity share weighted by workforce size.
For a more detailed look at differences in M365 Copilot usage across the labor market, we
can compare usage across industries. We illustrate by comparing estimates of IW As done in
each of the three selected industries (Banking, Consulting, and Manufacturing) to the share
of corresponding IW As seen in M365 Copilot. The fraction of work done in each industry
was estimated using Occupational Employment and Wage Statistics data [U.S. Bureau of
20

Labor Statistics, 2024]. For each industry, the fraction of each IW A done was estimated as a
sum of the IW As performed by each occupation in the sector, weighted by occupation size.
Per occupation IW A frequency was itself estimated as a weighted sum of task frequency as
reported in O*NET. Noting that many IW As in each industry are not present in the M365
Copilot data (Table 4), Figure 13 shows the fraction of user goal for each industry in a subset
of IW As that vary notably across the industries or in relation to estimated work done by
employees in those industries.
Provide information to guests, clients, or customers
Evaluate the quality or accuracy of data
Calculate financial data
Explain technical details of products or services
Communicate operational plans, activities
Read materials to inform work processes
Edit written materials or documents
0.00 0.05 0.10 0.15 0.20
Fraction of User Goal
Labor Market
Banking
Consulting
Manufacturing
M365 Copilot
Banking
Consulting
Manufacturing
Figure 13:IW A comparison across three example industries. IW As shown differ in M365 Copilot
activity share by industry and/or from estimated share of work done in the industries based on
breakdown of per-occupation workforce share within each industry taken from Occupational Em-
ployment and Wage Statistics. See Appendix Figure A5 for comparison across a larger set of IW As.
T able 4:Industry IW As not present in M365 Copilot
Sector T otal IW As IW As not in M365 Copilot Estimated W ork in non-present IW As Example non-present IW A
Banking 238 140 36.6% Negotiate contracts or agreements
Consulting 315 217 46.9% Evaluate production inputs or outputs
Manufacturing 295 199 56.7% Assemble products or work aids
Several IW As stand out as divergent in M365 Copilot usage compared to the estimate
of work done in the industry, including in particularEdit Written Materials or Documents,
which captures a far larger fraction of activity in M365 Copilot than in the industries them-
selves. This discrepancy is due, presumably, to the general usage of M365 Copilot for editing
21

and writing in the course of many jobs, while each industry likely has few jobs, such as copy
editing, where editing and writing constitute “official” work activities in O*NET.
Some lower frequency work activities in M365 Copilot may undershoot potential usage,
particularly in Banking where activities likeEvaluate the quality or accuracy of dataare far
below their estimated overall share. These suggest areas where fine tuned AI agents may be
useful for assisting with work. Evaluating data in the banking industry, for instance, is a
work activity commonly done by claims adjusters and insurance underwriters who may have
specific workflows, tools, or data analysis needs that require more customized AI solutions.
Next we apply the AI applicability metric proposed by Tomlinson et al. [2025], aggregated
at the job family level as defined by O*NET. The AI applicability score, computed on IW As
and then aggregated to occupations, indicates the extent to which work activities seen in
M365 Copilot usage are relevant to an occupation. Figure 14 highlights the relevance of M365
Copilot to information work occupations, led by theComputer and Mathematicaljob family.
In broad strokes, two groups of job families can be seen in Figure 14, one for information
work occupations, where the AI applicability score is 40% or higher, and one for physical
world occupations where the AI applicability score is 25% or lower.
Building and Grounds Cleaning and Maintenance
Construction and Extraction
Farming, Fishing, and Forestry
Healthcare Support
Installation, Maintenance, and Repair
Food Preparation and Serving Related
Healthcare Practitioners and Technical
Production
Transportation and Material Moving
Protective Service
Personal Care and Service
Life, Physical, and Social Science
Community and Social Service
Educational Instruction and Library
Architecture and Engineering
Management
Office and Administrative Support
Arts, Design, Entertainment, Sports, and Media
Legal
Sales and Related
Business and Financial Operations
Computer and Mathematical
0% 20% 40% 60%
AI Applicability Score
Figure 14:AI applicability score by O*NET job family.
To understand the makeup of work done in each job family we decompose the AI Ap-
plicability score for each job family into constituent GW As. This allows us to understand
not just the overall degree of AI applicability to each job family, but a “profile” of the
ways in which AI is applicable based on usage. Although theAdministrative Supportand
22

Art, Design, and Mediajob families, for instance, share the same AI applicability score of
0.55, the composition of this metric by GW As differs substantially.Art, Design, and Media
has far moreThinking CreativelywhileAdministrative Supportsees much moreProcessing
Information,Administrative Tasks, andCommunicating with Externals.
We illustrate these job family profiles in Figure 15.Computer & Mathematicalhas
a somewhat higher overall AI applicability score (0.64) thanEducational Instruction and
Librarybut the differences in how that applicability is distributed stand out. Both see
considerableThinking Creatively, butEducational Instruction and Librarysees more appli-
cability inTraining & Teaching,Judging Qualities, andDocumenting/Recording Information.
Computer & Mathematicalsees more AI applicability inAnalyzing Data and Information,
Working with Computers, among other areas largely absent forEducational Instruction &
Library.
0
0.03
0.06
0.09
0.12
Administrative Tasks
Analyzing Data/Info
Assisting & Caring
Comm. w/ External
Comm: Supvs & Peers
Consulting & Advice
Decisions & Solving
Doc/Record Info       Getting Information
Interpret Meaning
Judging Qualities
Process Information
Thinking Creatively
Training & Teaching
Working w/ Computers
Computer & Math (0.64)
(a) Computer and Mathematical
0
0.03
0.06
0.09
0.12
Administrative Tasks
Analyzing Data/Info
Assisting & Caring
Comm. w/ External
Comm: Supvs & Peers
Consulting & Advice
Decisions & Solving
Doc/Record Info       Getting Information
Interpret Meaning
Judging Qualities
Process Information
Thinking Creatively
Training & Teaching
Working w/ Computers
Education & Library (0.45) (b) Educational Instruction and Library
Figure 15:AI applicability score and breakdown by GW A for the Computer and Mathematical
(a) and Educational Instruction and Library (b) job families. See Figure A6 for more job families.
Job families with lower AI applicability scores can also be differentiated.Life & Social
Sciencesis spiky, with considerable applicability inAnalyzing Data & Informationand
Documenting & Recording Information.Personal Servicesis only moderately lower in overall
AI applicability, but shows a more well-rounded usage pattern across work activities. See
Appendix Figure A6 for AI applicability profiles for more job families.
Taken together, these three views — labor market, industry, and job family — give the
most concrete picture in our data of one of enterprise AI’s next frontiers: extending into the
work activities, industries, and occupations where there is the most room for adoption to
grow.
23

4 Discussion
The findings above suggest two things about the state of enterprise AI today. First, M365
Copilot is functioning as an everyday assistant for knowledge work, used broadly across
occupations and industries for activities ranging from writing and information lookup to
analysis, decision support, and communication. Second, that adoption, while broad, is
uneven. Usage patterns vary substantially across industries, occupations, and work activities,
and there is substantial room for adoption to grow across the activities done in the labor
market. For example, the distribution of top-level user intent shows both intent-driven
effects in which some intents (Content Refinement) comprise a far larger share of user intent
than other intents (Meeting Management) across all occupational groups. Most occupational
groups do, however, have one if not several intents with uniquely higher share.Marketing
& Advertisingis relatively higher inIdeation & Planning,Science & Researchhigher in
Analytical Reasoning, andSoftware Development & IThigher inProgramming Assistance.
We see AI applicability scores for some information work job families (e.g.,Business and
Financial Operations) more than double job families comprised of occupations dominated by
physical world work (e.g.,Construction and Extraction). This skew away from physical labor
and toward information work is not surprising, but tracking the uptake of AI across the labor
market broadly is important for characterizing the evolving “jagged edge” of AI relevance.
Our analysis of work activities across job families, shows that each job family is unique in
the distribution of work done with M365 Copilot, even compared to job families with similar
overall levels of AI applicability.Business & Financelooks different fromLegal, which looks
different fromSales. Comparisons across three industries corroborated this pattern: broad
similarity in the work activities that comprise the most usage but with some uniqueness,
especially in relative terms within less frequent work activities.
What, then, does this uniqueness across industry and occupational comparisons suggest
about directions and work contexts in which AI usage may grow? We identify two types
of potential growth areas: 1) work done in the world and not present in M365 Copilot
data, and 2) work done in the world but relatively underrepresented in M365 Copilot data.
Our industry comparisons highlight the former case, as half or less of the work activities
done in our example industries were present in the M365 Copilot data. While some of
these, especially those oriented toward physical labor simply may not be a good fit for
current generative AI, the industries selected largely are information work industries and
thus comprised of work areas that are candidates for increased AI usage as AI capabilities
improve and become embedded in and tailored to an increasing number of professions.
The industry comparisons also highlight areas of relative underrepresentation of AI usage.
24

BankingandConsultingsee about the same share of M365 Copilot usage forEvaluate the
quality or accuracy of data, but the banking industry as a whole does far more of that
work activity, and thus we may see growth of that use case within that industry provided
sufficient AI functionality. The analyses of job families show a similar pattern. Contrasting
GW As with and without workforce weighting highlights types of usage that may grow given
the share of the labor market that does those activities. As examples,Thinking Creatively
andCommunicating with Supervisors, Peers, or Subordinates, while already common work
activities done with M365 Copilot would see even higher usage share if that share were more
aligned with the share of the workforce that does those activities.
Turning to the nature of usage, we see that high-frequency usage of M365 Copilot is con-
sistently assistive via general-purpose functionality applied by people across a wide range of
job types. The top user intent is still Information Inquiry and similarly Getting Information
accounts for the second largest share of work activity on the user goal side. Writing is a
dominant work activity, and both information seeking and writing are tasks done by people
in many jobs rather than only by those whose primary work functions involve them. Re-
turning to the industry comparisons, we see evidence of this: the share of people working in
those industries with core work functions that involve writing is tiny compared to the share
of writing done with M365 Copilot.
Notably, despite the large share of M365 Copilot activity involving some form of infor-
mation seeking, that was the area that saw the largest drop in usage over our six month
time frame. AI adoption and the underlying technology and implementations are changing
rapidly, but six months arguably is a short time frame to see the 5% absolute drop in infor-
mation seeking as a share of total usage. Such a shift may mark a turning point as people
move away from using AI largely as a search engine replacement toward a wider variety of
uses. We caution that we were only able to look at time trends for intent over a 114 day
period so we raise this as suggestive but important, and recommend continued study to track
this potential change.
What emerges across these analyses is a picture of enterprise AI past the novelty stage
and into something more substantive: M365 Copilot is being used as an everyday assistant
across the occupations and activities of day-to-day knowledge work. At the same time, the
pattern of where it is used, and where it is not, makes clear that today’s usage is not the
ceiling. Across industries, occupations, and the work the labor market actually does, sizable
areas remain where there is room for adoption to grow. The next phase of enterprise AI,
whatever else it brings in capability, will be defined in part by how broadly usage extends
into those areas — and continued direct measurement of usage in real workflows is what will
let us see whether and how that happens.
25

References
Daron Acemoglu. The simple macroeconomics of ai. Working Paper 32487, National Bureau
of Economic Research, May 2024. URLhttps://www.nber.org/papers/w32487.
Ruth Appel, Peter McCrory, Alex Tamkin, Miles McCain, Tyler Neylon, and Michael
Stern. Anthropic economic index report: Uneven geographic and enterprise AI adop-
tion. Technical report, Anthropic, 2025. URLhttps://www.anthropic.com/research/
anthropic-economic-index-september-2025-report. Accessed: 2025-10-05.
Ruth Appel, Maxim Massenkoff, Peter McCrory, Miles McCain, Ryan Heller,
Tyler Neylon, and Alex Tamkin. Anthropic economic index report: eco-
nomic primitives, 2026. URLhttps://www.anthropic.com/research/
anthropic-economic-index-january-2026-report.
Alexander Bick, Adam Blandin, and David J Deming. The rapid adoption of generative AI.
Management Science, 2026. doi: 10.1287/mnsc.2025.02523.
Timothy F Bresnahan and Manuel Trajtenberg. General purpose technologies: “engines of
growth”?Journal of Econometrics, 65(1):83–108, 1995.
Erik Brynjolfsson and Tom Mitchell. What can machine learning do? workforce implications.
Science, 358(6370):1530–1534, December 2017.
Erik Brynjolfsson, Tom Mitchell, and Daniel Rock. What can machines learn, and what
does it mean for occupations and the economy?AEA Papers and Proceedings, 108:43–47,
May 2018.
Erik Brynjolfsson, Anton Korinek, and Ajay Agrawal. A research agenda for the economics
of transformative AI. Working Paper 34256, National Bureau of Economic Research,
September 2025a. URLhttps://www.nber.org/papers/w34256.
Erik Brynjolfsson, Danielle Li, and Lindsey Raymond. Generative AI at work.The Quarterly
Journal of Economics, pages 889–942, 2025b.
Aaron Chatterji, Tom Cunningham, Christopher Ong, Carl Shan, David Deming, Z¨ oe Hitzig,
and Kevin Wadman. How people use ChatGPT, September 2025.
Avinash Collis and Erik Brynjolfsson. AI’s overlooked$97 billion contribution to the
economy.The Wall Street Journal, August 2025. URLhttps://www.wsj.com/opinion/
ais-overlooked-97-billion-contribution-to-the-economy-users-service-da6e8f55.
26

Accessed: 2025-10-12.
Kevin Zheyuan Cui, Mert Demirer, Sonia Jaffe, Leon Musolff, Sida Peng, and Tobias Salz.
The effects of generative AI on high-skilled work: Evidence from three field experiments
with software developers.Management Science, 2026.
Eleanor Wiske Dillon, Sonia Jaffe, Sida Peng, and Alexia Cambon. Early impacts of M365
Copilot.arXiv preprint arXiv:2504.11443, 2025.
Tyna Eloundou, Sam Manning, Pamela Mishkin, and Daniel Rock. GPTs are GPTs: Labor
market impact potential of LLMs.Science, 384(6702):1306–1308, 2024.
Kunal Handa, Alex Tamkin, Miles McCain, Saffron Huang, Esin Durmus, Sarah Heck, Jared
Mueller, Jerry Hong, Stuart Ritchie, Tim Belonax, Kevin K. Troy, Dario Amodei, Jared
Kaplan, Jack Clark, and Deep Ganguli. Which economic tasks are performed with AI?
evidence from millions of Claude conversations. arXiv:2503.04761 [cs.CY], 2025.
Sonia Jaffe, Neha Parikh Shah, Jenna Butler, Alex Farach, Alexia Cambon, Brent Hecht,
Michael Schwarz, and Jaime Teevan. Generative AI in real-world workplaces: The second
microsoft report on AI and productivity research. Technical report, Microsoft Corpora-
tion, 2024. URLhttps://www.microsoft.com/en-us/research/wp-content/uploads/
2024/07/Generative-AI-in-Real-World-Workplaces.pdf. Accessed: 2025-10-12.
Maxim Massenkoff, Eva Lyubich, Peter McCrory, Ruth Appel, and Ryan Heller. An-
thropic economic index report: Learning curves, 2026. URLhttps://www.anthropic.
com/research/economic-index-march-2026-report.
Microsoft. AI diffusion report: Where AI is most used, developed, and built. Techni-
cal report, Microsoft Corporation, 2025. URLhttps://www.microsoft.com/en-us/
research/wp-content/uploads/2025/10/Microsoft-AI-Diffusion-Report.pdf. Ac-
cessed: 2025-11-06.
Amit Misra, Jane Wang, Scott McCullers, Kevin White, and Juan Lavista Ferres. Measuring
AI diffusion: A population-normalized metric for tracking global AI usage, 2025. URL
https://arxiv.org/abs/2511.02781.
National Center for O*NET Development. O*NET Database Version 29.0, 2024. URL
https://www.onetcenter.org/db_releases.html. Accessed: 2025-05-29.
Shakked Noy and Whitney Zhang. Experimental evidence on the productivity effects of
generative artificial intelligence.Science, 381(6654):187–192, 2023.
27

Ryan Pendell. AI Use at Work has Nearly Doubled in Two Years, 2025. URLhttps:
//www.gallup.com/workplace/691643/work-nearly-doubled-two-years.aspx. Ac-
cessed: 2025-10-19.
Sida Peng, Eirini Kalliamvakou, Peter Cihon, and Mert Demirer. The impact of AI on
developer productivity: Evidence from GitHub copilot.arXiv preprint arXiv:2302.06590,
2023.
Kiran Tomlinson, Sonia Jaffe, Will Wang, Scott Counts, and Siddharth Suri. Working with
AI: Measuring the applicability of AI to occupations. arXiv:2507.07935 [cs.AI], 2025.
U.S. Bureau of Labor Statistics. Occupational Employment and Wage Statistics (OEWS),
May 2024, 2024. URLhttps://www.bls.gov/oes/tables.htm. Accessed: 2025-05-29.
Mengting Wan, Tara Safavi, Sujay Kumar Jauhar, Yujin Kim, Scott Counts, Jen-
nifer Neville, Siddharth Suri, Chirag Shah, Ryen W. White, Longqi Yang,
Reid Andersen, Georg Buscher, Dhruv Joshi, and Nagu Rangan. Tnt-
llm: Text mining at scale with large language models. InKDD, March
2024. URLhttps://www.microsoft.com/en-us/research/publication/
tnt-llm-text-mining-at-scale-with-large-language-models/.
Wenting Zhao, Xiang Ren, Jack Hessel, Claire Cardie, Yejin Choi, and Yuntian Deng. Wild-
Chat: 1M ChatGPT interaction logs in the wild. InThe Twelfth International Conference
on Learning Representations, 2024.
28

A Figures & Tables
0.0000.0250.0500.075
Chat Inquiry
App Inquiry
Personal Inquiry
Assistant Inquiry
Doc Inquiry
Email Inquiry
Profile Inquiry
T argeted Retrieval
Research Compare
T ech Support
Explain Concepts
How-T o Guidance
Enterprise Inquiry
Info Query
0.0000.0500.1000.1500.200
Proofread
Edit
0.0000.0050.0100.0150.020
Music Composition
Promo Content
Copywriting
Event Planning
Onboarding Docs
Media Communication
Multimedia
Presentation
Compose Email
Visual Content
Translation
T ext Composition
Report Generation
0.000 0.010 0.020
System Design
Explain Concepts
Debugging
Coding
0.000 0.005 0.010
Hybrid Data
User Visual Content
Public Data
Enterprise Data
Single Meeting
Multiple Meetings
Document
Email
User T ext Data
0.0000.0020.0040.006
Workflow Optimize
Stat Analysis
Financial Planning
Hybrid Comparison
Legal Guidance
Doc Comparison
General Comparison
Financial Analysis
Image Analysis
Math Reasoning
Action Advice
Data Analysis
Excel Data Analysis
0.0000.0020.0040.006
Collab Ideation
Retrospective
Workshop Session
1-on-1 Meeting
Project Planning
Customer Meeting
Leadership Meeting
0.0000.0010.0020.0030.004
Creative Non-Work
Strategic Plan
Problem-Solving
Creative Work
0.000 0.001 0.002 0.003
Community Connect
Soft Skills
Skill Development
Career Guidance
T echnical Skills
0.0000.0010.0010.002
Workplace Trend
T eams Catch-up
T ask Overview
Update from People
Email Catch-up
Cross-Channel Comm
Project Progress
0.0000.0000.0000.0010.001
Streaming Search
Music Composition
Fitness Guidance
Shopping Help
Travel Planning
Recreation
Fraction of User Prompts
Information
Inquiry (0.32)
Content
Refinement (0.26)
Content
Generation (0.09)
Programming
Assistance (0.07)
Content
Summarization (0.05)
Analytical
Reasoning (0.04)
Meeting
Management (0.01)
Ideation
& Planning (0.01)
Skill
Acquisition (0.01)
Contextual
Update (0.00)
Leisure
& Recreation (0.00)
Figure A1:Second-level intents for all top-level intents.
29

0.05 0.05 0.11 0.26 0.05 0.01 0.02 0.02 0.32 0 0.02 0.03 0.06 0
0.06 0.02 0.11 0.31 0.04 0 0.02 0.03 0.34 0 0 0.03 0.04 0
0.06 0 0.16 0.26 0.04 0 0.01 0.03 0.33 0 0.01 0.05 0.05 0
0.06 0.03 0.1 0.32 0.04 0 0.01 0.04 0.29 0 0.01 0.08 0.02 0.01
0.06 0.04 0.1 0.23 0.04 0 0.01 0.01 0.39 0 0.01 0.04 0.07 0.01
0.07 0.05 0.08 0.19 0.03 0 0.01 0.02 0.39 0 0.01 0.03 0.1 0.01
0.06 0.06 0.09 0.28 0.04 0 0.01 0.02 0.34 0 0.01 0.04 0.05 0.01
0.06 0.03 0.13 0.34 0.05 0 0.01 0.02 0.29 0 0.01 0.04 0.02 0
0.06 0.04 0.13 0.28 0.07 0 0.01 0.02 0.31 0 0.01 0.06 0.01 0
0.06 0.04 0.12 0.31 0.04 0 0.01 0.02 0.28 0 0.01 0.04 0.05 0.01
0.05 0.05 0.1 0.32 0.05 0 0.01 0.02 0.35 0 0.01 0.03 0.01 0
0.08 0.05 0.11 0.23 0.05 0 0.01 0.02 0.33 0 0.01 0.06 0.05 0
0.04 0.04 0.15 0.35 0.04 0.01 0.03 0.02 0.26 0 0.01 0.03 0.02 0
0.05 0.05 0.12 0.28 0.05 0.01 0.02 0.02 0.3 0 0.02 0.04 0.04 0.01
0.04 0.03 0.11 0.38 0.02 0 0 0.04 0.3 0 0 0.07 0 0
0.05 0.05 0.08 0.21 0.03 0 0.01 0.01 0.34 0 0.01 0.03 0.16 0.01
0.05 0.04 0.12 0.3 0.05 0 0.01 0.02 0.3 0 0.02 0.04 0.03 0
0.04 0.07 0.09 0.26 0.03 0 0 0.02 0.39 0 0.01 0.03 0.07 0
0.06 0.04 0.07 0.17 0.03 0 0.01 0.02 0.37 0 0.01 0.03 0.2 0.01
0.07 0.05 0.1 0.28 0.04 0 0.01 0.02 0.3 0 0.01 0.06 0.05 0
Ambiguous
Intent
Content
Generation
Content
Summarization
Ideation
& Planning
Information
Inquiry
Meeting
Management
Programming
Assistance
Analytical
Reasoning
Content
Refinement
Contextual
Update
Informal
Exchange
Leisure
& Recreation Other
Skill
Acquisition
Supply Chain & Logistics
Software Development & IT
Science & Research
Sales & Business Development
Research & Data Analysis
Real Estate & Property Management
Program & Product Management
Marketing & Advertising
Manufacturing & Quality Assurance
Legal & Compliance
Human Resources & Administration
Healthcare & Medical Services
Government & Public Administration
Financial Services & Analysis
Engineering & Architecture
Cybersecurity & Risk Management
Customer Support & Service
Creative Arts & Entertainment
Content Creation & Journalism
Consulting & Strategy
Figure A2:Top-level intent by Occupational Group.
30

Consulting & Strategy
Content Creation & Journalism
Creative Arts & Entertainment
Customer Support & Service
Cybersecurity & Risk Management
Engineering & Architecture
Financial Services & Analysis
Government & Public Administration
Healthcare & Medical Services
Human Resources & Administration
Legal & Compliance
Manufacturing & Quality Assurance
Marketing & Advertising
Program & Product Management
Real Estate & Property Management
Research & Data Analysis
Sales & Business Development
Science & Research
Software Development & IT
0.00
0.02
0.04
0.06
Supply Chain & Logistics
0.08
0.10
0.12
0.14
0.16
0.20
0.25
0.30
0.35
0.02
0.04
0.06
0.00
0.00
0.01
0.01
0.01
0.00
0.01
0.02
0.03
0.01
0.02
0.03
0.04
0.30
0.35
0.00
0.01
0.01
0.02
0.02
0.03
0.00
0.05
0.10
0.15
0.20
0.00
0.00
0.01
0.01
Intent share by Occupation Groups vs Intent Average
Share (Frac)
Analytical
Reasoning
Content
Generation
Content
Refinement
Content
Summarization
Contextual
Update
Ideation
& Planning
Informal
Exchange
Information
Inquiry
Meeting
Management
Programming
Assistance
Skill
Acquisition
Average Occupation Groups
Figure A3:Top-level intent by Occupational Group, showing different from overall mean.
31

Advise others on business or operational matters
Provide information or assistance to the public
Edit written materials or documents
Prepare informational or instructional materials
Communicate specifics, project details
Provide information to guests, clients, or customers
−4
−3
−2
−1
−4 −3 −2 −1
Log IWA Fraction: User Goal
Log IWA Fraction: Labor Market
IWA Skew

Copilot
Even
Labor Market
(a) IW A skew: User Goal v Labor Market
Set up computer systems
Respond to customer problems or inquiries
Communicate operational plans, activities
Edit written materials or documents
Provide information to guests, clients, or customers
Communicate specifics, project details
Maintain operational records
−4
−3
−2
−1
−4 −3 −2 −1
Log IWA Fraction: Copilot Action
Log IWA Fraction: Labor Market
IWA Skew

Copilot
Even
Labor Market
(b) IW A skew: Copilot Action v Labor Market
Figure A4:Share of IW As done in M365 Copilot vs. in the labor market as a whole, user goal (a;
r=−0.01) and Copilot action (b;r= 0.17). Example IW As shown skew toward Copilot, toward
the labor market, or are about even in share. Only IW As in Copilot data shown.
32

Banking Consulting Manufacturing
0.00 0.05 0.10 0.15 0.200.00 0.05 0.10 0.15 0.200.00 0.05 0.10 0.15 0.20
Evaluate the quality or accuracy of data
Evaluate programs, practices, or processes
Respond to customer problems or inquiries
Perform administrative or clerical activities
Create visual designs or displays
Analyze performance of systems or equipment
Document technical designs, procedures, or activities
Research healthcare issues
Prepare financial documents, reports, or budgets
Explain regulations, policies, or procedures
Provide information to guests, clients, or customers
Analyze business or financial data
Evaluate designs, specifications, or technical data
Implement procedures or processes
Process digital or online data
Prepare health or medical documents
Diagnose system or equipment problems
Gather data about operational or development activities
Evaluate the characteristics of technologies
Resolve computer problems
Compile records, documentation, or other data
Calculate financial data
Assess characteristics or impacts of regulations or policies
Gather information from physical or electronic sources
Obtain information about goods or services
Prepare reports of operational activities
Examine materials for accuracy, compliance
Explain technical details of products or services
Prepare informational or instructional materials
Communicate specifics, project details
Explain financial information
Edit written materials or documents
Fraction of User Goal
Figure A5:IW As for each of three example industries. IW As shown account for 0.9% or more
of activity. Dots shown estimate percent of IW A done within each sector based on Occupational
Employment and Wage Statistics data.
33

0
0.03
0.06
0.09
0.12
Administrative Tasks
Analyzing Data/Info
Assisting & Caring
Comm. w/ External
Comm: Supvs & Peers
Consulting & Advice
Decisions & Solving
Doc/Record Info       Getting Information
Interpret Meaning
Judging Qualities
Process Information
Thinking Creatively
Training & Teaching
Working w/ Computers
Administrative Support (0.55)
0
0.03
0.06
0.09
0.12
Administrative Tasks
Analyzing Data/Info
Assisting & Caring
Comm. w/ External
Comm: Supvs & Peers
Consulting & Advice
Decisions & Solving
Doc/Record Info       Getting Information
Interpret Meaning
Judging Qualities
Process Information
Thinking Creatively
Training & Teaching
Working w/ Computers
Architecture & Engineering (0.51)
0
0.03
0.06
0.09
0.12
Administrative Tasks
Analyzing Data/Info
Assisting & Caring
Comm. w/ External
Comm: Supvs & Peers
Consulting & Advice
Decisions & Solving
Doc/Record Info       Getting Information
Interpret Meaning
Judging Qualities
Process Information
Thinking Creatively
Training & Teaching
Working w/ Computers
Arts/Design/Media (0.55)
0
0.03
0.06
0.09
0.12
Administrative Tasks
Analyzing Data/Info
Assisting & Caring
Comm. w/ External
Comm: Supvs & Peers
Consulting & Advice
Decisions & Solving
Doc/Record Info       Getting Information
Interpret Meaning
Judging Qualities
Process Information
Thinking Creatively
Training & Teaching
Working w/ Computers
Business & Finance (0.61)
0
0.03
0.06
0.09
0.12
Administrative Tasks
Analyzing Data/Info
Assisting & Caring
Comm. w/ External
Comm: Supvs & Peers
Consulting & Advice
Decisions & Solving
Doc/Record Info       Getting Information
Interpret Meaning
Judging Qualities
Process Information
Thinking Creatively
Training & Teaching
Working w/ Computers
Community & Social Service (0.42)
0
0.03
0.06
0.09
0.12
Administrative Tasks
Analyzing Data/Info
Assisting & Caring
Comm. w/ External
Comm: Supvs & Peers
Consulting & Advice
Decisions & Solving
Doc/Record Info       Getting Information
Interpret Meaning
Judging Qualities
Process Information
Thinking Creatively
Training & Teaching
Working w/ Computers
Computer & Math (0.64)
0
0.03
0.06
0.09
0.12
Administrative Tasks
Analyzing Data/Info
Assisting & Caring
Comm. w/ External
Comm: Supvs & Peers
Consulting & Advice
Decisions & Solving
Doc/Record Info       Getting Information
Interpret Meaning
Judging Qualities
Process Information
Thinking Creatively
Training & Teaching
Working w/ Computers
Education & Library (0.45)
0
0.03
0.06
0.09
0.12
Administrative Tasks
Analyzing Data/Info
Assisting & Caring
Comm. w/ External
Comm: Supvs & Peers
Consulting & Advice
Decisions & Solving
Doc/Record Info       Getting Information
Interpret Meaning
Judging Qualities
Process Information
Thinking Creatively
Training & Teaching
Working w/ Computers
Legal (0.56)
0
0.03
0.06
0.09
0.12
Administrative Tasks
Analyzing Data/Info
Assisting & Caring
Comm. w/ External
Comm: Supvs & Peers
Consulting & Advice
Decisions & Solving
Doc/Record Info       Getting Information
Interpret Meaning
Judging Qualities
Process Information
Thinking Creatively
Training & Teaching
Working w/ Computers
Life & Social Science (0.41)
0
0.03
0.06
0.09
0.12
Administrative Tasks
Analyzing Data/Info
Assisting & Caring
Comm. w/ External
Comm: Supvs & Peers
Consulting & Advice
Decisions & Solving
Doc/Record Info       Getting Information
Interpret Meaning
Judging Qualities
Process Information
Thinking Creatively
Training & Teaching
Working w/ Computers
Management (0.51)
0
0.03
0.06
0.09
0.12
Administrative Tasks
Analyzing Data/Info
Assisting & Caring
Comm. w/ External
Comm: Supvs & Peers
Consulting & Advice
Decisions & Solving
Doc/Record Info       Getting Information
Interpret Meaning
Judging Qualities
Process Information
Thinking Creatively
Training & Teaching
Working w/ Computers
Personal Service (0.40)
0
0.03
0.06
0.09
0.12
Administrative Tasks
Analyzing Data/Info
Assisting & Caring
Comm. w/ External
Comm: Supvs & Peers
Consulting & Advice
Decisions & Solving
Doc/Record Info       Getting Information
Interpret Meaning
Judging Qualities
Process Information
Thinking Creatively
Training & Teaching
Working w/ Computers
Sales (0.59)
Figure A6:AI Applicability score by job family, broken out into GW As.
34

T able 5:Full list of IW As in primary work activity dataset.
IW A User Goal Copilot Action IW A User Goal Copilot Action
Adjust equipment to ensure adequate performance 0.00 0.00 Identify business or organizational opportunities 0.00 0.00
Advise others on business or operational matters 0.00 0.01 Implement procedures or processes 0.02 0.01
Advise others on educational or vocational matters 0.00 0.00 Implement security measures for computer systems 0.00 0.00
Advise others on financial matters 0.00 0.01 Inspect conditions of materials or products 0.00 0.00
Advise others on healthcare or wellness issues 0.00 0.00 Inspect completed work or finished products 0.00 0.00
Advise others on legal or regulatory matters 0.00 0.01 Inspect facilities or equipment 0.00 0.00
Advise others on products or services 0.00 0.02 Interpret language, cultural, or religious information 0.00 0.01
Advise others on the design or use of technologies 0.00 0.03 Interview people to obtain information 0.00 0.00
Advise others on workplace health or safety issues 0.00 0.00 Investigate incidents or accidents 0.00 0.00
Advise patients or clients on medical issues 0.00 0.00 Investigate individuals’ background or activities 0.00 0.00
Advocate for individual or community needs 0.00 0.00 Investigate organizational or operational problems 0.00 0.00
Analyze biological or chemical substances or data 0.00 0.00 Issue documentation 0.00 0.01
Analyze business or financial data 0.01 0.00 Maintain current knowledge in area of expertise 0.00 0.00
Analyze business or financial risks 0.00 0.00 Maintain computer, or technical equipment 0.00 0.00
Analyze data to improve operations 0.01 0.00 Maintain health or medical records 0.00 0.00
Analyze health or medical data 0.00 0.00 Maintain operational records 0.00 0.00
Analyze market or industry conditions 0.00 0.00 Maintain safety or security 0.00 0.00
Analyze performance of systems or equipment 0.01 0.00 Maintain sales or financial records 0.00 0.00
Analyze scientific or applied data 0.00 0.00 Manage budgets or finances 0.00 0.00
Arrange displays or decorations 0.00 0.00 Manage control systems or activities 0.00 0.00
Assess regulations or policies 0.01 0.00 Manage human resources activities 0.00 0.00
Assign work to others 0.00 0.00 Mark materials or objects for identification 0.00 0.00
Assist individuals with paperwork 0.00 0.03 Measure materials, products, or equipment 0.00 0.00
Assist others to access services or resources 0.00 0.02 Monitor equipment operation 0.00 0.00
Assist scientists, with projects or research 0.00 0.00 Monitor external affairs, trends, or events 0.00 0.00
Calculate financial data 0.01 0.01 Monitor financial data or activities 0.00 0.00
Coach others 0.00 0.00 Monitor individual behavior or performance 0.00 0.00
Collect data about consumer needs or opinions 0.00 0.00 Monitor operation of computer technologies 0.00 0.00
Collect information about patients or clients 0.00 0.00 Monitor operations to ensure adequate performance 0.00 0.00
Communicate sustainability information 0.00 0.00 Monitor operations for compliance with regulations 0.00 0.00
Communicate with others about business strategies 0.00 0.01 Monitor resources or inventories 0.00 0.00
Communicate operational plans, activities 0.03 0.02 Notify others of emergencies or problems 0.01 0.00
Communicate specifics, project details 0.03 0.05 Obtain formal documentation or authorization 0.01 0.00
Compile records, documentation, or other data 0.02 0.02 Obtain information about goods or services 0.02 0.00
Confer with clients to determine needs 0.00 0.01 Operate computer systems or equipment 0.00 0.00
Consult legal materials or public records 0.01 0.00 Perform administrative or clerical activities 0.01 0.00
Coordinate activities with clients or agencies 0.00 0.00 Perform human resources activities 0.00 0.00
Coordinate group, community , or public activities 0.00 0.00 Perform recruiting or hiring activities 0.00 0.00
Coordinate regulatory compliance activities 0.00 0.00 Plan events or programs 0.00 0.00
Coordinate with others to resolve problems 0.00 0.00 Plan work activities 0.01 0.00
Counsel others about personal matters 0.00 0.00 Prepare documentation for contracts or permits 0.00 0.00
Create artistic designs or performances 0.00 0.00 Prepare financial documents, reports, or budgets 0.00 0.00
Create visual designs or displays 0.02 0.01 Prepare health or medical documents 0.01 0.00
Design computer systems or applications 0.00 0.00 Prepare informational or instructional materials 0.03 0.05
Design materials or devices 0.00 0.00 Prepare legal or regulatory documents 0.00 0.00
Determine operational methods or procedures 0.01 0.01 Prepare proposals or grant applications 0.00 0.00
Determine resource needs of projects or operations 0.00 0.00 Prepare reports of operational activities 0.02 0.02
Determine values or prices of goods or services 0.00 0.00 Prepare schedules for services or facilities 0.00 0.00
Develop business or marketing plans 0.00 0.00 Present research or technical information 0.00 0.02
Develop educational programs, plans, or procedures 0.00 0.00 Process digital or online data 0.02 0.01
Develop financial or business plans 0.00 0.00 Program computer systems or production equipment 0.00 0.00
Develop marketing or promotional materials 0.01 0.01 Promote products, services, or programs 0.00 0.00
Develop models of systems, processes, or products 0.00 0.00 Provide general assistance to others 0.00 0.00
Develop news, entertainment, or artistic content 0.00 0.00 Provide information or assistance to the public 0.00 0.01
Develop operational procedures or standards 0.01 0.01 Provide information to guests, clients, or customers 0.01 0.09
Develop organizational goals or objectives 0.00 0.00 Provide support or encouragement to others 0.00 0.00
Develop organizational policies, systems, or processes 0.00 0.00 Purchase goods or services 0.00 0.00
Develop patient or client care or treatment plans 0.00 0.00 Read materials to inform work processes 0.03 0.05
Develop professional relationships or networks 0.00 0.00 Reconcile financial data 0.00 0.00
Develop recipes or menus 0.00 0.00 Research healthcare issues 0.01 0.00
Develop safety standards, policies, or procedures 0.00 0.00 Research historical or social issues 0.00 0.00
Develop technical specifications 0.00 0.00 Research laws, precedents, or other legal data 0.00 0.00
Diagnose system or equipment problems 0.01 0.01 Research organizational behavior or performance 0.00 0.00
Discuss legal matters 0.00 0.00 Research technology designs or applications 0.01 0.00
Document technical designs, procedures, or activities 0.01 0.01 Resolve computer problems 0.02 0.01
Edit written materials or documents 0.22 0.16 Resolve personnel or operational problems 0.00 0.00
Estimate project development or operational costs 0.00 0.00 Respond to customer problems or inquiries 0.01 0.02
Evaluate condition of financial assets, property 0.00 0.00 Schedule appointments 0.00 0.00
Evaluate designs, specifications, or technical data 0.01 0.01 Schedule operational activities 0.00 0.00
Evaluate patient condition or treatment options 0.00 0.00 Select materials for operations or projects 0.00 0.00
Evaluate personnel capabilities or performance 0.00 0.00 Set up computer systems 0.00 0.00
Evaluate production inputs or outputs 0.00 0.00 Set up equipment 0.00 0.00
Evaluate programs, practices, or processes 0.01 0.01 Signal others to coordinate work activities 0.00 0.00
Evaluate project feasibility 0.00 0.00 Study details of artistic productions 0.00 0.00
Evaluate the characteristics of technologies 0.01 0.00 T each academic or vocational subjects 0.00 0.00
Evaluate the quality or accuracy of data 0.01 0.01 T each life skills 0.00 0.00
Examine financial activities, operations, or systems 0.00 0.00 T each safety procedures or standards to others 0.00 0.00
Examine materials for accuracy , compliance 0.02 0.01 T est performance of computer or information systems 0.00 0.00
Execute financial transactions 0.00 0.00 T est performance of equipment or systems 0.00 0.00
Explain financial information 0.01 0.01 T rain others on health or medical topics 0.00 0.00
Explain medical information to patients or family 0.00 0.01 T rain others on operational or work procedures 0.00 0.00
Explain regulations, policies, or procedures 0.01 0.02 T rain others to use equipment or products 0.00 0.00
Explain technical details of products or services 0.02 0.04 V erify personal information 0.00 0.00
Gather data about operational activities 0.01 0.00 W rite material for artistic or commercial purposes 0.01 0.01
Gather information from physical or electronic source 0.02 0.00
35

B Classifiers
Work Classifier
You are an AI assistant tasked with classifying a sequence of users’ Conversations to AI
Chat(Copilot) as either **Personal** or **Work** related or **unclear**.
**Categories**:
- **Personal** – The user’s prompt is about personal or everyday matters (e.g. family, health,
home, hobbies, or general life).
- **Work** – The user’s prompt is about business, work, or professional matters (e.g. office
tasks, projects, corporate information, or job-related topics).
- **Unclear** – The user’s prompt is not about personal or Work, or it is not possible to
classify the prompts to any category
**Instructions**: Read the sequence of conversations (upto past 3 conversations if available is
given to you) and determine which category the last conversation (also labelled as ”conver-
sation to be classified”) falls into. **Respond with only the single word** “Personal” **or**
“Work” **or** “Unclear” accordingly, and nothing else. Do not add any explanations or extra
words.
**Examples**:
- **User Prompt:** Turn1: ”I need to buy groceries and pick up my kids from school.” Turn2:
”Recommend good restaurant on the way back?” *Your Response:* Personal
- **User Prompt:** Turn1: ”Prepare the slides for Monday’s sales meeting.” Turn2: ”Modify
the slide to include a summary slide for executives.” **Your Response:** Work
Now, classify the **Conversation**.
{{User Prompt}}
**Your Response:**
36
