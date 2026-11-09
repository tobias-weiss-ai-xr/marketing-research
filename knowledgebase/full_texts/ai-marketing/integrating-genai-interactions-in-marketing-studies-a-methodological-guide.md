---
title: 'Integrating GenAI interactions in marketing studies: A methodological guide'
url: https://doi.org/10.1016/j.ijresmar.2025.12.003
category: ai-marketing
subcategory: empirical
date: 2025-12
venue: International Journal of Research in Marketing
authors:
- Moritz Joerling
source: openalex-oa
pdf_url: https://hal.science/hal-05489669v1/document
pages: 21
chars: 107111
fetched_at: '2026-11-08T19:03:23+00:00'
kb_version: 1
---

# Integrating GenAI interactions in marketing studies: A methodological guide

HAL Id: hal-05489669
https://hal.science/hal-05489669v1
Submitted on 2 Feb 2026
HAL is a multi-disciplinary open access archive
for the deposit and dissemination of scientific re-
search documents, whether they are published or not.
The documents may come from teaching and research
institutions in France or abroad, or from public or pri-
vate research centers.
L’archive ouverte pluridisciplinaire HAL, est des-
tinée au dépôt et à la diffusion de documents scien-
tifiques de niveau recherche, publiés ou non, émanant
des établissements d’enseignement et de recherche
français ou étrangers, des laboratoires publics ou
privés.
Distributed under a Creative Commons CC BY 4.0 - Attribution - International License
Integrating GenAI interactions in marketing studies: A
methodological guide
Moritz Joerling
To cite this version:
Moritz Joerling. Integrating GenAI interactions in marketing studies: A methodological guide. International
Journal of Research in Marketing, 2026, 43 (1), pp.28-47. ⟨10.1016/j.ijresmar.2025.12.003⟩. ⟨hal-05489669⟩

Integrating GenAI interactions in marketing studies: A
methodological guide
Moritz Joerling *
EM Lyon Business School, 144 Av. Jean Jaur`es, 69007 Lyon, France
ARTICLE INFO
Keywords:
AI
generative AI
GenAI
Web applications
ABSTRACT
Reflecting the ubiquitous presence of generative AI (GenAI), marketing researchers have begun
integrating it as an interaction partner in research studies; however, technical barriers and
methodological gaps limit its broader adoption. This paper provides a comprehensive guide for
implementing GenAI interactions in marketing studies, particularly within the Qualtrics platform.
First, a literature review categorizes diverse GenAI applications—from scaling qualitative
methods to creating novel experimental paradigms—distinguishing between GenAI as research
method versus research object to help researchers identify untapped opportunities. Second, the
paper presents a decision framework for when GenAI offers value over traditional methods and
explains the principal architecture (frontend, API, backend) that enables researchers to connect
any GenAI model to their studies. Crucially, it demonstrates how AI coding assistants can
translate natural language instructions into functional code, eliminating programming barriers
for non-technical researchers. Third, step-by-step tutorials establish emerging best practices
through four implementations spanning text and image modalities: search assistants, automated
interviewers, co-creation tools, and hyper-personalized messaging. These implementations serve
as adaptable templates empowering researchers to create custom solutions for their unique
questions. By mastering AI coding assistants rather than copying specific code, researchers gain
methodological independence in a rapidly evolving landscape. This work democratizes GenAI
integration and enables previously impossible experimental paradigms.
1. Introduction
The rapid development of generative AI (GenAI) has opened new opportunities in marketing research. No longer confined to
traditional methods, researchers can now integrate GenAI interactions in their studies in a powerful dual capacity: as both a fascinating
subject of investigation and a revolutionary methodological instrument, deploying it to conduct scalable interviews, simulate complex
participant interactions, and create experimental interventions that would have been impossible before (Blanchard et al., 2025;
Chopra & Haaland, 2023; Pataranutaporn et al., 2024; Salvi et al., 2025). This convergence of studying AI and studying with AI marks a
paradigm shift in marketing research methodology.
Recent studies demonstrate GenAI’s versatility across diverse research contexts. In experimental settings, interactions with
ChatGPT have produced durable reductions in conspiracy theory beliefs (Costello et al., 2024) and enhanced creative performance in
ideation tasks (Lee & Chung, 2024). As a methodological tool, GenAI has proven capable of conducting qualitative interviews—even in
* Corresponding author.
E-mail address: joerling@em-lyon.com.
Contents lists available at ScienceDirect
International Journal of Research in Marketing
journal homepage: www.elsevier.com/locate/ijresmar
https://doi.org/10.1016/j.ijresmar.2025.12.003
Received 15 May 2025;
International Journal of Research in Marketing xxx (xxxx) xxx
Available online 10 December 2025
0167-8116/© 2025 The Author. Published by Elsevier B.V. This is an open access article under the CC BY license
( http://creativecommons.org/licenses/by/4.0/ ).
Please cite this article as: Moritz Joerling, International Journal of Research in Marketing,
https://doi.org/10.1016/j.ijresmar.2025.12.003

domains unrelated to AI, such as investigating stock market investment aversion (Chopra & Haaland, 2023). Researchers have also
explored how firsthand experience with GenAI shapes the evaluation of AI-generated content (Celiktutan et al., 2024) and whether
demographically-targeted LLM responses are more persuasive than generic messages (Hackenburg & Margetts, 2024) or whether
GenAI-based personalized video ads are more effective than generic nonpersonalized video ads (Kapoor et al., 2025).
While these applications are promising, significant barriers remain. The technical implementation can be daunting for researchers
without programming expertise, and a lack of standardized methodologies threatens to create inconsistent participant experiences and
compromise validity. Moreover, marketing researchers whose work is not inherently AI-focused may not recognize how GenAI could
support their research methods—from conducting hundreds of in-depth interviews simultaneously to creating new innovative para-
digms that would be impossible without GenAI interactions.
This paper bridges these gaps by providing marketing researchers with both the basic conceptual knowledge and practical tools to
harness the potential of GenAI interactions in research studies. Drawing on consultations with marketing researchers about their needs
and challenges, the paper makes three key contributions.
First, the paper synthesizes and categorizes existing GenAI applications in behavioral research, revealing patterns in how these
tools serve different research purposes. The analysis distinguishes between GenAI as a research method (e.g., automated interviewing
on stock market investments, participant simulation on social media) versus a research object (e.g., studying AI persuasion, human-AI
collaboration), helping researchers identify untapped opportunities in their own domains.
Second, the paper presents the principal architecture of GenAI integrations (frontend, GenAI service via API, backend) that enable
researchers to connect virtually any GenAI model to their studies. This approach transcends specific tools or platforms, ensuring
longevity despite GenAI’s rapid evolution. Crucially, the paper illustrates how AI coding assistants can translate natural language
instructions into functional code, democratizing GenAI implementation for researchers without programming skills. Researchers do
not need to write code themselves; they need sufficient understanding to articulate their requirements and guide the implementation
process—precisely the knowledge this paper provides.
Third, the paper showcases this practical approach with detailed walk-throughs for different marketing-relevant implementations
(one presented in the manuscript and three in the web appendix, pages 23–30): an AI-powered search assistant revealing how con-
sumers navigate information search with GenAI; an automated qualitative interviewer for scalable, in-depth consumer insights; a
multi-modal co-creation tool investigating human-AI collaboration across text and image generation; an application that allows testing
the persuasion power of GenAI by creating hyper-personalized output based on participant information. Each implementation includes
exact prompts for coding assistants and step-by-step instructions for a researcher’s own implementation.
The power of this approach extends beyond the provided examples as the same architectural principles and implementation steps
apply to any other GenAI integration. Hence, researchers can transfer this knowledge to create custom applications that are tailored to
their specific questions and needs. By mastering AI coding assistants rather than following specific code, researchers gain methodo-
logical independence as well as the agility to integrate emerging models and design novel paradigms in a landscape where new models
and GenAI capabilities evolve monthly. All code, and materials are publicly available at https://github.com/QualtriGen, enabling
immediate application and community-driven development. The following section presents results from group discussions with re-
searchers about their current understanding and perspectives on using GenAI interactions in research studies.
2. Understanding the researcher perspective
Five group discussions with sixteen marketing researchers from European and US institutions have been conducted to understand
the different implementation challenges.1 These discussions, involving researchers across all seniority levels from PhD students to full
professors, revealed both enthusiasm for GenAI’s potential and significant barriers to its integration in research studies (please see
pages 3–9 in the web appendix for a detailed coding table with direct quotes from the discussions; the full transcripts are available:
https://osf.io/53pgt/?view_only=bc7c976267274a90adc75ecd9c31bd74). The group discussions revealed the following key themes.
2.1. Current awareness and perceived opportunities
While researchers recognized GenAI’s transformative potential, actual implementation remains rare. The gap between recognition
and implementation emerged as a central theme across all discussions, with most participants having never implemented GenAI in
their own research despite seeing its value. When asked about specific applications, many researchers struggled to envision concrete
possibilities: “I have no idea how I would be able to use it […] to come up with ideas of how to use it, I have no idea what the ca-
pabilities of AI are.”
Through guided discussion, however, participants identified various potential applications, ranging from studying AI’s persuasive
characteristics to using it as a tool to make experiments more immersive and dynamic. They recognized immediate benefits of using
GenAI as a methodological tool, including the scalability of interviews and the anonymity of a non-human interviewer that may
encourage participants to be more forthcoming on sensitive topics. Participants also saw value in improved ecological validity and
increased engagement through more realistic and interactive experimental settings compared to standard questionnaires. Additional
use cases emerged, including using AI for participant priming and manipulation checks, facilitating idea generation in product
1 I thank an anonymous reviewer for suggesting the integration of group discussions.
M. Joerling
International Journal of Research in Marketing xxx (xxxx) xxx
2

development studies, and even preventing bot participation by serving as a quality control mechanism.
2.2. Key barriers to implementation and how this guide addresses them
Technical complexity and time investment. While researchers see enormous potential and compelling applications in the GenAI in-
tegrations, most of the group discussants have never tried it themselves, mainly because of technical barriers. Many researchers feel
they lack the necessary skills and are hesitant to invest the required time: “You need to study and dive into how it works and how such a
tool is created. It might be possible for many of us, but it takes some time”. To overcome the technical complexity barrier, particularly
the lack of coding skills that prevents implementation, this paper showcases how researchers without coding skills can translate natural
language into the required code with the support of coding assistants. This approach—using AI to implement AI—transforms learning
of sophisticated programming skills into minutes of describing research needs. The paper provides the essential technical knowledge
and prompts researchers need to direct these assistants effectively, along with best practices that eliminate the trial-and-error process,
making implementation accessible to researchers who, as one participant noted, are “very bad with technology… [and] just know how
to prompt.”.
Loss of experimental control. Researchers expressed deep concern about the unpredictability of AI responses. “When you’re running
experiments, it’s really important to keep things controlled and AI is a little bit uncontrolled,” one participant noted. Another worried
that AI might “blur the manipulations” by improvising beyond intended experimental conditions. This tension between ecological
validity and experimental control emerged as a fundamental challenge. To address this concern, the step-by-step guides demonstrate
how to capture complete interaction logs—every prompt and AI response—in Qualtrics’ embedded data fields for post-hoc analysis.
Additionally, the paper provides a decision framework (Table 2) helping researchers identify when GenAI’s dynamic interactions
enhance research value despite reduced control—such as when studying AI phenomena or improving ecological validity—versus when
absolute experimental control is essential and traditional methods should be preferred. Finally, the paper and web appendix (pages
20–22) also provide detailed information on API parameters that control AI behavior, such as temperature settings that affect output
randomness, along with error tracking instructions to monitor technical issues. However, perfect control remains elusive for the
moment as GenAI’s outputs are probabilistic (Blanchard et al., 2025).
Ethical and institutional uncertainties. Participants described uncertainty about ethical boundaries and IRB requirements, with one
noting their board requires “exact wording for all participant interactions,” making ad hoc AI responses problematic. Another attendee
stated that even AI developers admit they “don’t know themselves either” why AI responds certain ways, calling it a “black box.” To
navigate these uncertainties, the guide outlines differences between open and proprietary models. When using proprietary GenAI
models via APIs, providers can access and potentially store participant interactions—a crucial consideration for IRBs. For research
involving sensitive information or vulnerable populations, the paper recommends using open models on private infrastructure to
maintain full data control. While a complete discussion of all ethical concerns is beyond this manuscript’s scope, the web appendix
(pages 40–41) provides additional literature and guidance for navigating institutional review processes with these novel
methodologies.
Academic legitimacy concerns. Finally, researchers worried about peer review acceptance, anticipating that early adopters would
“bear a cost of reviewers who have no idea what you’re doing.” Beyond individual papers, participants identified this as requiring field-
wide acceptance of new methodological standards. This paper serves as a foundational resource to establish legitimacy, providing clear
documentation that researchers can cite and reviewers can reference to understand these emerging methodologies. The comprehensive
literature review demonstrates growing adoption across marketing research, helping normalize these approaches.
3. Previous research studies and existing GenAI implementations
With the rise of GenAI, researchers are increasingly using these tools for direct participant interaction in their research studies. This
section synthesizes these pioneering studies, summarized in Table 1, to identify their key applications and technical methodologies. As
a testament to the field’s rapid evolution, many of the works are currently only available as preprints. The synthesis of the literature
reveals that GenAI serves two fundamentally different purposes in behavioral research, each with distinct methodological implica-
tions. When used as a research method, GenAI transforms how researchers gather insights by leveraging AI’s unique capabilities to
scale qualitative methods or create entirely new research paradigms. When studied as a research object, GenAI becomes the phe-
nomenon under investigation, with researchers examining how AI influences human attitudes and behaviors, or how different AI
characteristics shape user interaction.
3.1. GenAI as a research method
Studies employing GenAI as a research method offer unprecedented scalability and enable entirely new research paradigms. For
example, a recent study deployed a large language model (LLM) to conduct 381 in-depth interviews exploring stock market investment
barriers (Chopra & Haaland, 2023). With this interview tool, the researchers uncovered psychological barriers that were subsequently
validated through traditional surveys (e.g., the belief that stock market participation is a demanding, high-maintenance activity
requiring constant monitoring and research). In another study, researchers have created controlled social media environments using
LLMs with assigned political personas, precisely manipulating partisan balance to test how being outnumbered affects user comfort
and platform perceptions—an experiment impossible with real platforms due to practical constraints (Allamong et al., 2024). Another
methodological innovation used personalized LLMs to generate users’ ’future selves’ at age 60, including AI-generated backstories and
M. Joerling
International Journal of Research in Marketing xxx (xxxx) xxx
3

Table 1
Studies using GenAI for participant interaction in behavioral research.
Research description GenAI integration
Reference Purpose of
GenAI
integration
Research
Topic
Research Question Key Findings Interface GenAI Service
[Modality]
API usage Description
Allamong et al.
(2024)
Research
method
Social
media
How does partisan
imbalance in feeds affect
user comfort & platform
perception?
Being outnumbered reduces
comfort and worsens
perceptions of the platform
and its users.
​ Custom social media
platform (https://www.
polarizationlab.com/
social-media-
accelerator)
GPT-3.5 [text] Probably but
not explicitly
mentioned
GPT-3.5-powered AI agents
with assigned political views to
simulate controlled partisan
environments.
Argyle et al.
(2025)
Research
object
Persuasion Are customized or
interactive AI messages
more persuasive than
generic ones?
AI messages were persuasive,
but customization and
interactivity offered no extra
benefit over a generic
message.
​ Custom chat integrated
in Qualtrics
GPT-4 [text] Yes GPT-4 was embedded in a
survey to test real-time
persuasive strategies, isolating
the effects of customization vs.
interaction.
Celiktutan et al.
(2024)
Research
object
Co-
Creation
How do people perceive
their contribution to a
human-AI co-production?
Individuals tend to overvalue
their own contributions to
tasks co-produced with GenAI
compared to the contributions
of others.
​ Public ChatGPT website ChatGPT
[text]
No Participants used the public
ChatGPT website for a task;
their perceptions were then
measured via a survey.
Chopra and
Haaland
(2023)
Research
method
Interview Can an AI fully automate
qualitative interviews to
generate high-quality
data?
An AI interviewer successfully
conducted 381 in-depth
interviews, maintained
engagement, and uncovered
deep insights.
​ Custom chat integrated
in Qualtrics
GPT-4 [text] Yes A multi-agent GPT-4 system
was built to act as an
autonomous interviewer,
handling probing, transitions,
and summarization.
Costello et al.
(2024)
Research
object
Persuasion Can conversational AI
durably reduce
conspiracy beliefs?
A single 5–10 min dialogue
durably reduced conspiracy
beliefs for at least 2 months.
​ Custom chat integrated
in Qualtrics
GPT-4 [text] Yes GPT-4 was prompted to use the
Socratic method, asking open-
ended questions to encourage
users to reflect reasoning.
De Freitas et al.
(2025)
Research
object
Support Can interacting with an
AI companion reduce
consumer loneliness?
Interacting with an AI
companion significantly
reduces momentary
loneliness, on par with human
interaction.
​ Custom chat app GPT-3 & GPT-
4 [text]
Yes A custom chat app (“Chatty”)
provided an AI companion
with a specific personality,
memory, and realistic typing
indicators.
Doshi & Hauser,
2024)
Research
object
Co-
Creation
How does GenAI access
affect the individual and
collective creativity of co-
created content?
GenAI increased individual
story creativity (novelty/
usefulness) but reduced
collective diversity, making
stories more similar to each
other.
​ Custom web interface GPT-4 [text] Yes Writers could request 3-sen-
tence story ideas from GPT-4 to
use as inspiration for their
short stories.
Flamino et al.
(2025)
Research
object
Persuasion How effective are LLM
agents as confederates
and surrogates in a
debate?
Agents were unpersuasive
confederates but improved
debate productivity. They are
not yet realistic surrogates for
human behavior.
​ Custom chat interface GPT-4 &
Llama 2 [text]
Yes LLM agents with unique
personas debated humans,
using a mix of GPT-4 and Llama
2 to generate conversational
responses.
Gaerth, Melumad,
and Meyer
(2025)
Research
method
Modality Do people disclose more
or less personal
information when
speaking or writing to
another agent?
Speaking feels more social,
which leads to higher social
desirability bias and people
disclosing less negative
personal information when
speaking.
​ ChatGPT mock-up in
Qualtrics
ChatGPT [text
& speech]
No Simulated ChatGPT interface
(continued on next page)
M. Joerling
International Journal of Research in Marketing xxx (xxxx) xxx
4

Table 1 (continued)
Research description  GenAI integration
Reference Purpose of
GenAI
integration
Research
Topic
Research Question Key Findings  Interface GenAI Service
[Modality]
API usage Description
Hackenburg and
Margetts
(2024)
Research
object
Persuasion Does LLM-based
microtargeting increase
persuasion compared to
generic messages?
GPT-4 messages were
persuasive, but
microtargeting showed no
significant persuasive
advantage over a well-crafted
generic message.
​ Custom chat interface GPT-4 [text] Yes A web app utilized participant
data to generate real-time,
personalized, persuasive
messages from GPT-4 for
comparison.
Hosanagar & Ahn
(2024)
Research
object
Co-
Creation
How do different human-
AI collaboration designs
affect creative writing
quality and diversity?
Human-led designs yielded
higher quality and satisfaction
than AI-led designs. AI
reduced content diversity, but
human-led designs mitigated
this.
​ Public ChatGPT website   GPT-3.5 [text] No Participants wrote stories using
ChatGPT 3.5 following specific
collaboration protocols (e.g.,
Human Confirmation, Copilot).
Hussein et al.
(2026)
Research
method
Mani-
pulation
Can an AI interaction
focused on “identity
reflection” increase
attitude extremity?
Reflecting on identity with an
AI agent significantly
increased attitude extremity
and preference for extreme
political candidates.
​ Custom chat integrated
in Qualtrics
GPT-4 [text] Yes An LLM agent was invisibly
prompted to guide the
conversation to “convince”
participants their opinion was
identity-relevant.
Kapoor, Kumar,
and Trulaske
(2025)
Research
object
Persuasion Can personalized GenAI
video ads increase
engagement over other ad
formats?
Personalized GenAI video ads
increased ad clicks by 6–9
percentage points over
personalized image and
generic video ads.
​ WhatsApp Proprietary
[video]
Yes A proprietary text-to-video
engine created a “digital
avatar” of a brand ambassador
to speak personalized ad
messages.
Karakas¸ and
Jaeger (2025)
Research
object
Persuasion Can a brief LLM
conversation change
attitudes about meat
consumption?
A short chat with GPT-4
significantly weakened
participants’ stated
commitment to eating meat.
​ Public ChatGPT website GPT-4 [text] No Participants had a 5–10 min
semi-structured conversation
with the public ChatGPT-4;
attitudes were measured pre-
and post-chat.
Lee and Chung
(2024)
Research
object
Co-
Creation
Does using ChatGPT
enhance human creativity
compared to Google or no
tools?
Using ChatGPT increased the
creativity of generated ideas
compared to both unassisted
ideation and using Google
Search.
​ Public ChatGPT website GPT-3.5 [text] No Participants generated ideas
using either ChatGPT, Google,
or no tools. Final ideas were
rated for creativity by human
judges.
Maier et al. (2025) Research
object
Co-
Creation
How do human-led vs.
model-led interaction
modes affect idea quality
and diversity?
“Question-mode” (human-
led) improved quality while
preserving diversity/
ownership, whereas “Model-
led” improved quality but
reduced diversity.
​ Custom web interface GPT-4 [text] Yes A custom chatbot used specific
strategies (asking questions,
giving suggestions, or
rewriting) to support users in
an ideation task.
Melumad and Yun
(2025)
Research
object
Search How does using an LLM
vs. a search engine affect
search behavior and
performance?
LLMs are more efficient for
search but lead to lower-
quality, less creative outputs
due to overreliance on AI
suggestions.
​ Custom chat integrated
in Qualtrics
GPT-3.5 [text] Yes An embedded ChatGPT
interface was compared against
an embedded Google interface
for a travel planning task.
Pataranutaporn
et al. (2024)
Research
method &
object
Support Can having a
conversation with an AI-
generated future self
reduce anxiety and
A brief interaction with an AI-
generated future self
significantly decreased
anxiety and increased future
​ Custom chat interface GPT-3.5 [text]
& StyleClip
[image]
Yes Personalized GPT-3.5 using
survey responses about users’
goals and qualities to create a
“future self” character at age
(continued on next page)
M. Joerling
International Journal of Research in Marketing xxx (xxxx) xxx
5

Table 1 (continued)
Research description  GenAI integration
Reference Purpose of
GenAI
integration
Research
Topic
Research Question Key Findings  Interface GenAI Service
[Modality]
API usage Description
increase future self-
continuity?
self-continuity compared to
control conditions.
60, and age-progressed photos
for a chat.
Potter et al.
(2024)
Research
object
Persuasion Do LLMs have political
biases, and can they
influence user attitudes?
LLMs show a clear liberal bias,
and brief exposure to
politically slanted AI
responses significantly shifts
user attitudes.
​ Custom chat integrated
in Qualtrics
GPT-4, GPT-
3.5, Llama 2
[text]
Yes A web app showed users 10
political responses from an
LLM prompted to be liberal or
conservative to measure
persuasive effects.
Sabour et al.
(2025)
Research
object
Persuasion Can an LLM agent
manipulate human
decision-making and risk-
taking?
An LLM agent successfully
manipulated participants,
significantly increasing their
risk-taking when prompted to
give risk-promoting advice.
​ Custom chat interface GPT-4 [text] Yes Participants played a financial
game while getting advice from
a GPT-4 agent secretly
prompted to be risk-promoting
or risk-averse.
Salvi et al. (2025) Research
object
Persuasion Is GPT-4 more persuasive
than humans in a
conversational debate?
GPT-4 was significantly more
persuasive than human
debaters (by 81.7 %), using
stronger arguments and more
formal language.
​ Custom chat interface GPT-4 [text] Yes Participants debated
controversial topics with either
another human or a GPT-4
agent in a randomized
controlled trial.
Schoenegger et al.
(2025)
Research
object
Persuasion Are LLMs more
persuasive than
incentivized human
persuaders?
GPT-4 was significantly more
persuasive than financially
motivated humans, causing a
23 percentage point greater
belief change.
​ Custom chat interface GPT-4 [text] Yes Participants read a persuasive
message generated by either an
incentivized human or a GPT-4
model prompted for max
persuasion.
Spatharioti et al.
2023)
Research
object
Search Do consumers prefer LLM
search for products, and
how does it affect their
choice?
Consumers find LLM search
more useful. It leads to a
narrower search process and a
final choice closer to the AI’s
first suggestion.
​ Custom chat interface Unspecified
LLM [text]
Yes A custom platform presented
users with either a
conversational AI or a
traditional search engine to
study product discovery
behavior.
Xu et al. (2023) Research
object
Search How does ChatGPT
compare to Google on
search efficiency?
ChatGPT is faster and more
satisfying, but Google users
demonstrate better
information retention.
​ Public ChatGPT website GPT-3.5 [text] No Participants used either the
public ChatGPT or Google
website to answer questions,
then were tested on efficiency,
satisfaction, and recall.
M. Joerling
International Journal of Research in Marketing xxx (xxxx) xxx
6

age-progressed images, enabling researchers to study interventions for psychological wellbeing (Pataranutaporn et al., 2024). Again
other research utilized LLM interactions to manipulate psychological constructs at the individual level (Hussein et al., 2026). By
instructing an LLM to engage participants in “identity reflection”, adaptively guiding them to see their opinions as self-defining, this
research demonstrates that increased identity relevance drives preferences for extreme political candidates. Despite these demon-
strations of GenAI transcending traditional methodological constraints, only a fraction of current studies leverage GenAI as a research
method, suggesting vast untapped opportunities for marketing researchers.
3.2. GenAI as a research object
More frequently, researchers integrate GenAI into their research studies to investigate the phenomenon of GenAI and its direct
effects on people’s attitudes and behaviors. Within this category, three dominant themes emerge. The most prominent theme in this
area is persuasion. While often explored in political or societal contexts—such as reducing conspiracy beliefs (Costello et al., 2024) or
influencing political opinions (Argyle et al., 2025; Hackenburg & Margetts, 2024; Potter et al., 2024)—these applications are directly
applicable to marketing. A common technique involves personalizing the AI’s arguments by incorporating the participant’s own at-
tributes (e.g., demographics, political opinion) into the instructions to the GenAI model. The model can then create hyper-personalized
or micro-targeted output that might be potentially more convincing than non-personalized messages. While the potential of this
method has been emphasized (Teeny & Matz, 2024), empirical evidence remains mixed. Initial studies found that text-based
personalized messages did not perform better than standard messages in persuasion tasks (Hackenburg & Margetts, 2024). Howev-
er, the same principle was used to generate hyper-personalized video ads, which showed a higher ad engagement than non-
personalized video ads (Kapoor et al., 2025).
A second major research stream examines how AI transforms online search, with studies revealing fundamental changes in con-
sumer behavior. Experiments comparing LLM-assisted search with traditional search engines demonstrate that while LLMs make
search more efficient, they lead to shallower knowledge acquisition (Melumad & Yun, 2025). Moreover, consumers perceive LLM
search as more useful than traditional search engines, but their eventual decisions may be less accurate due to overreliance when the
LLM erred (Spatharioti et al., 2023; Xu et al., 2023).
A third stream explores AI as a collaborative enhancer. Most remarkably, controlled experiments show that AI companions can
reduce loneliness—opening both opportunities and ethical questions for marketing applications, particularly in service industries
where human connection has traditionally been paramount (De Freitas et al., 2025). Moreover, studies of creative tasks demonstrate
that ChatGPT use increased creativity scores compared to both unassisted and Google-assisted ideation, suggesting AI’s potential as a
creative partner (Lee & Chung, 2024). However, other research warns that generative AI can homogenize content, reducing the
collective diversity of ideas (Doshi & Hauser, 2024). Crucially, though, this limitation is not inevitable; studies show it can be mitigated
when the interaction is designed for the human to lead the creative process (Hosanagar & Ahn, 2024; Maier et al., 2025). Finally,
research has uncovered that individuals systematically overvalue their own contributions in AI collaborations compared to how they
evaluate others’ contributions in identical situations (Celiktutan et al., 2024).
3.3. Technical implementation approaches
Turning to the technical implementation, the review shows that a majority of studies integrated GenAI interactions into Qualtrics
(e.g., Argyle et al., 2025; Chopra & Haaland, 2023; Costello et al., 2024). Exceptions typically arose when the research required
specialized functionality, such as a custom mobile app for a social companion (De Freitas et al., 2025), a simulated social media
interface (Allamong et al., 2024), or a field study conducted via WhatsApp (Kapoor et al., 2025). The choice of the integrated AI model
is remarkably consistent, with researchers almost exclusively using Large Language Models (LLMs) from OpenAI, despite the avail-
ability of potentially cheaper or better-performing alternatives. This monopolistic pattern raises concerns that research findings may
be model-specific to some extent rather than generalizable to AI broadly and that the field becomes vulnerable to changes in OpenAI’s
policies or practices. Remarkably, no study to date has systematically compared different models for research applications.
The technical implementation approaches also reveal a fundamental trade-off between simplicity and control. Some studies opted
for public website integration, directing participants to use ChatGPT’s public interface (Celiktutan et al., 2024; Lee & Chung, 2024).
This method is technically simple but comes with disadvantages. The researcher has no control over the model’s instructions (i.e., the
system prompt), cannot prevent the conversation from being potentially influenced by a participant’s prior chat history, and cannot
access the interaction data for analysis. The second, more sophisticated approach is the integration of a GenAI model into a researcher-
controlled user interface (e.g., Qualtrics) via an Application Programming Interface (API). This method provides the researcher with
full control over the interaction and complete data access. However, it introduces technical challenges and pitfalls that create a sig-
nificant barrier for those without coding expertise. Within this API approach, some studies call the model directly from the Qualtrics
platform (Costello et al., 2024), while others use a back-end server as an intermediary (Hackenburg & Margetts, 2024).
While these pioneering studies demonstrate the transformative potential of GenAI interactions in behavioral research, their
adoption in marketing research remains surprisingly limited. This gap between potential and practice may stem from several barriers
identified in the group discussions, the first being a lack of awareness about what is possible with GenAI interactions in research
studies. The literature review above addresses this by showcasing diverse applications and their potential. However, as the literature
review also reveals, there are different kinds of implementations ranging from simple public website integration to sophisticated API-
based systems, and many researchers mentioned the technical implementation as a main barrier to adopting GenAI interactions.
Hence, the following section addresses this technical barrier by first providing an overview of when GenAI tools provide value in
M. Joerling
International Journal of Research in Marketing xxx (xxxx) xxx
7

contrast to traditional methods, offering a decision framework for researchers, and then diving into practical explanations and step-by-
step walkthroughs for successful implementation.
4. The practical implementation of GenAI interactions into research studies
Drawing from the literature review, the technical nature of GenAI models—including their probabilistic behavior, data processing
requirements, and interaction capabilities—and insights from the discussions, the following table provides an overview of when GenAI
interactions provide value in research studies. This serves as a decision framework for researchers to determine when GenAI offers
legitimate methodological value versus when traditional methods remain more appropriate, before diving into technical imple-
mentation details (Table 2).
When researchers believe a GenAI integration would be beneficial in their research studies, they can draw upon existing valuable
resources for its implementation. One of them is the open-source template provided alongside the research on reducing conspiracy
beliefs (Costello et al., 2024). This resource is excellent for researchers seeking a practical, ready-to-use starting point. With this tool, a
researcher can download the provided Qualtrics template file, insert an API key, and run a text-based conversational study where a
participant chats with an AI inside the survey page. Another relevant approach involves the development of user-friendly, no-code
platforms, such as the LUCID solution (Garvey & Blanchard, 2025). This type of tool is very valuable for ensuring maximum acces-
sibility. With this solution, researchers can use a simple interface to set up text-based conversational studies with the GPT-4 model,
typically by entering their instructions and API key into web forms, without writing code.
While these resources excel at implementing established paradigms and might be a good point to start, the section below addresses
a different challenge: enabling researchers to create entirely novel GenAI integrations tailored to their specific research questions. The
approach presented here demonstrates how AI coding assistants can translate a researcher’s natural language description—whether for
voice-enabled interviews, GenAI online search, or image generation tasks—directly into functional code. This method combines the
accessibility of no-code solutions with the flexibility traditionally reserved for programmers. A researcher can describe their exact
needs (“I want participants to speak their responses to a GenAI driven interview bot in Qualtrics”) and receive working code minutes
later.
The following sections outline this approach, beginning with the foundational components to provide researchers with a con-
ceptual understanding of GenAI integrations, followed by introducing the practical method for using AI coding assistants to generate
the necessary code from natural language instructions. This is demonstrated through step-by-step walkthroughs of marketing-relevant
applications that showcase the breadth of possibilities this method enables.
4.1. Foundational architecture for integrating GenAI interactions in research studies
Building GenAI-driven applications fundamentally involves two core elements: a frontend and a GenAI service (please see page 3 in
the web appendix for a Glossary of technical terms). The frontend is the user-facing interface, such as a Qualtrics survey, where
participants input information. The GenAI service is the external AI model that processes this input and generates a response (e.g., text,
image, audio). The GenAI Service is often accessed via an Application Programming Interface (API). A key advantage of this API-
centric approach is its inherent flexibility, empowering researchers to connect their applications to virtually any GenAI service that
offers an API. This adaptability ensures that researchers remain independent of the rapidly evolving model landscape and can adapt or
extend their GenAI research applications as new and diverse GenAI models are published by various companies.
The fundamental technical task is to establish a communication channel between the GenAI service via the API and the user
frontend, which can be accomplished through different architectural patterns. The most direct architectural pattern connects the
frontend (i.e., Qualtrics) straight to the GenAI service. While this approach is straightforward and easier to implement, it also comes
with the risk of exposing the secret API key to survey participants, what could lead to unforeseen costs if they misuse it. However, the
cost risk can be significantly mitigated since most GenAI services use prepaid credit systems, allowing researchers to limit API key
funds to small amounts (please see pages 10–19 in the web appendix for API key setup). Nevertheless, to avoid the possibility of API
key access, an alternative pattern introduces a backend server as a secure intermediary that manages all communication with the
GenAI service on behalf of the frontend. The figure below shows the two principal architectures to establish the communication
channel between the GenAI service via the API and the user frontend. Subsequent chapters will provide the necessary background on
these elements (Fig. 1).
4.1.1. Frontend
A web frontend for GenAI interaction can be seen as any website that allows a user to make an input. While researchers can build
custom frontends from scratch (e.g., a mobile application; De Freitas et al., 2025), survey platforms such as Qualtrics offer a practical
and powerful option as it avoids the considerable effort of building and hosting a separate interface. The integration of a GenAI model
into Qualtrics is achieved by adding a small block of code to a survey question. This code combines three code elements that any
website is built with: Hypertext Markup Language (HTML), Cascading Style Sheets (CSS), and JavaScript (Simon, 2023). While HTML
defines the content and structure of a website (Berners-Lee & Connolly, 1993), CSS provides the design (Flanagan, 2011), and
JavaScript defines the frontend’s behavior and interactivity (Kalim, 2013).
For integrating a GenAI service into Qualtrics, JavaScript is the most important coding element as it establishes the communication
channel between the frontend and the GenAI service. It takes what a participant types, sends it to the GenAI service, and then displays
the AI’s output back to the participant. The other two, HTML and CSS, play supporting roles. HTML is used to create the basic structure
M. Joerling
International Journal of Research in Marketing xxx (xxxx) xxx
8

and text, such as the instructions a participant reads. CSS is then used to control the visual style, like the colors, layout, and fonts. In
practice, the code for all three elements is often bundled together in one script and inserted into a single survey question using
Qualtrics’s ’add JavaScript’ feature.
Another crucial feature of using Qualtrics as a frontend is its “Embedded Data” functionality, which allows custom variables to be
stored alongside standard survey responses. To implement this, a researcher first navigates to the ’Survey Flow’ section in Qualtrics.
There, they add an ’Embedded Data’ element and simply type the names for the new variables they wish to create, such as ‘user_-
prompt’ and ‘AI_response’. Once these fields are defined in the Survey Flow, the embedded JavaScript can be programmed to save
information directly into them. For example, after a participant types their prompt, the script would use a simple command to store
that text directly into the variable ‘user_prompt’. Similarly, after the script receives the response from the GenAI, it would save it to
‘AI_response’. The result is a complete, automatically logged transcript of the interaction. When the researcher downloads the study
data as usual from Qualtrics, the exported spreadsheet will contain new columns labeled ‘user_prompt’ and ‘AI_response’. For each
Table 2
Conditions for valuable GenAI interactions in research studies.
When GenAI interactions in research studies provide value
Studying AI as a Research Phenomenon - Investigating AI design, trust, adoption, and interaction patterns
- Examining human-AI collaboration effectiveness
- Understanding consumer responses to AI systems (e.g., chatbots, transparency preferences)
Enabling Novel Research Designs - Creating impossible interactions (e.g., conversations with simulated future selves)
- Establishing controlled collaborative settings with AI partners
- Simulating interactions difficult or unethical with humans
Enhancing Methodological Rigor - Replacing static stimuli with dynamic interactions
- Adding AI conditions to test robustness alongside traditional methods
- Adding AI conditions to traditional methods for balancing external validity and experimental control
Scaling Qualitative Methods - Conducting hundreds of interviews simultaneously
- Bridging qualitative depth with quantitative scale
- Enabling 24/7 data collection for global studies
- Using AI for initial exploration while humans focus on depth
Improving Data Quality & Participant Experience - Increasing engagement through interactive study experiences
- Reducing interviewer bias
- Enabling follow-up questions and clarifications in online studies
- Collecting multimodal data (text, voice, image)
- Serving as sophisticated attention checks
When GenAI interactions in research studies do not provide value
Population Constraints - Studying highly specific groups (e.g., domain experts, niche subcultures)
- Target participants unlikely to engage with AI
- Sample inherently limited by population characteristics
Human Expertise Essential - Trust and rapport critical to research topic
- Cultural context or specialized knowledge required
- Researcher’s interpretive skills central to data quality
Methodological Requirements - Absolute experimental control with zero variation needed
- Exact replication of previous methodologies required
- Observational or ethnographic methods necessary
- Non-verbal cues essential to research questions
Fig. 1. Principal architecture of a GenAI integration for participant interaction in research studies with and without backend solution (accessing
via API).
M. Joerling
International Journal of Research in Marketing xxx (xxxx) xxx
9

participant, these columns will hold the full text of their interaction, appearing directly alongside their answers to other questions that
the researcher added to the survey (e.g., demographics, behavioral intention, satisfaction measures). This creates a single, unified
dataset ready for analysis.
While this procedure works well for text-based output from the GenAI service, some modifications are needed to handle non-textual
outputs, such as images or audio files, which cannot be stored directly in Embedded Data fields. For this more specialized case, the
workflow involves uploading the generated media to an external cloud storage service. The persistent URL (i.e., Uniform Resource
Locator, the address of a specific webpage or file on the internet) for the stored file is then captured and saved into an Embedded Data
field, effectively linking the non-text output to the participant’s survey data (please see pages 34–36 in the web appendix for detailed
instructions on how to store non-textual data).
4.1.2. GenAI model
The GenAI model is the central component of a GenAI-driven web application, responsible for its core functionality. In contrast to
traditional AI models, which primarily analyze existing data for tasks like prediction and classification, GenAI constitutes a broad
category of systems capable of creating novel content (Toner, 2023). GenAI models are either offered directly by the individual
providers (e.g., OpenAI, Anthropic, Google), or there also exist “AI model Aggregators” like FireworksAI, AIMLAPI, or OpenRouter,
which provide a collection of the most relevant GenAI models on their web presence (much like booking a hotel directly on the hotel
webpage or booking it via a platform). In any case, selecting the appropriate GenAI model for a study requires the consideration of
some key characteristics.
The first and most fundamental characteristic to consider is modality—the format of the input the model receives from the study
participant and the output it generates. Although text-to-text interaction is the most common paradigm, the methods described in this
paper allow for the integration of a wide range of modalities within Qualtrics. The following table provides an overview of available
GenAI models, categorized by their input and output modalities, to illustrate the breadth of possibilities (Table 3).
Beyond modality, a second critical characteristic to consider is the model’s specialization and inherent capabilities. Many
contemporary GenAI models are augmented with built-in tools that extend their functionality beyond simple content generation. For
example, some models can perform real-time web searches to incorporate up-to-date information (OpenAI, 2025), a crucial feature for
studies involving current events or the investigation of people’s online search behavior (Melumad & Yun, 2025). Others include
moderation systems to ensure safe interactions by detecting harmful content (De Freitas et al., 2025) or are optimized for generating
computer code (MistralAI, 2025). A researcher should therefore select a model whose interaction modality and functionalities align the
best with the corresponding research question or task.
Moreover, the selection involves a practical evaluation of three often-competing factors: performance, speed (latency), and cost. A
model’s performance can be assessed using objective online resources and public leaderboards, which offer continuously updated
benchmarks that compare various models on standardized tests (e.g., https://artificialanalysis.ai/; https://lmarena.ai/).2 However,
higher performance often correlates with increased operational costs and higher latency—the time delay between a user’s input and
the model’s response. In a research context, high latency can negatively impact the participant experience, while high costs weigh on
the research budget. Consequently, the “best” model is context-dependent. The largest or most capable model is not always the optimal
choice. Researchers must balance these trade-offs to select a model that provides the necessary performance for their research question
while remaining within acceptable parameters for latency and budget.
Finally, GenAI models can be classified as either open-source (e.g., DeepSeek, LLaMA 3 by Meta or Gemma 2 by Google) or pro-
prietary (e.g., ChatGPT-4 by OpenAI or Gemini 2.5 by Google). Open-source models are models where aspects like the architecture,
training methods, or even the model weights themselves are made publicly available (Bi et al., 2024). However, to fully benefit from
open-source models, researchers must run them on their own computers or servers, which requires powerful hardware that most
researchers don’t have access to, especially if they want performance matching commercial models like ChatGPT. Given these practical
constraints, most researchers will find it more feasible to connect to proprietary GenAI models (e.g., ChatGPT, Gemini, Claude)
through their Application Programming Interface (API). However, for research projects requiring high control, transparency, or
customization, open-source models offer distinct advantages. These models can be modified or trained on specific datasets—for
example, teaching an AI to conduct specialized interviews using your field’s terminology and methods. Moreover, when running on a
private server, user-GenAI interactions are not shared with the model developer (please see pages 38–39 in the web appendix for an
additional discussion).
4.1.3. API
An API serves as the gateway through which a software program communicates with other programs, and—in the case of web
APIs—with the broader digital ecosystem across the internet (Jin et al., 2018). In our context, it is the crucial link that enables a
platform like Qualtrics to send a participant’s input to a GenAI model and receive a response. Each request sent via the API is a self-
contained package of information. This package includes several key components. First, it contains an API key for authentication—a
unique code that identifies the researcher’s account for access and billing, much like a credit card held on file at a restaurant. An API
key can be generated on the website of a GenAI model provider (please see pages 10–19 in the web appendix for API key setup). Most
providers (e.g., OpenAI, Anthropic) allow prepaid credits for their API usage (e.g., $20–100) with auto-recharge disabled, which
2 For more extensive discussions on measuring model performance and quality see for example Weidinger et al. (2025).
M. Joerling
International Journal of Research in Marketing xxx (xxxx) xxx
10

allows strict cost controls and ensures that the set budget will not be exceeded. However, not all providers offer these safeguards;
Google’s Gemini API currently lacks spending caps. In such cases, researchers who still want to use a specific model can turn to AI
model aggregators like OpenRouter or AIMLAPI. These services provide access to the same models through their own APIs while
offering prepaid credit systems for better cost control. Second, an API call includes a “body”, which specifies exactly what the
researcher wants the GenAI model to do. This includes defining which specific model to use (e.g., ChatGPT-4 or Gemini 2.5), and
providing an instruction on how the model should behave (e.g., “be a friendly collaborator and always provide constructive feed-
back”), which is called system prompt. Normal users of GenAI models never see the system prompt, which works behind the scenes, but
every model has specific instructions that are followed when a user types in their regular prompt. Moreover, the body eventually
includes the actual prompt from the study participant (e.g., “Write a slogan for a new eco-friendly sneaker”). This structured format
ensures the request is understood and processed correctly by the GenAI model.
From a methodological standpoint, the power of an API lies in its configurability. Critically, APIs address a key concern about
GenAI controllability in experimental settings by allowing researchers to adjust parameters like temperature, which governs output
determinism. Lower temperature values produce more consistent, predictable responses, while higher values introduce variability.
Beyond temperature control, researchers can configure numerous other parameters, such as defining specific brand personas through
system prompts or adjusting response length and style. Each model provider (e.g., OpenAI, Google, Anthropic) publishes compre-
hensive API documentations detailing these configurable options, which researchers can treat as independent variables in experi-
mental designs. This control enables researchers to standardize their methodology, enhance replicability, and test how specific AI
characteristics influence participant responses.
4.1.4. Backend
After selecting a GenAI model and understanding its API, the researcher must decide on the architectural pattern for connecting the
frontend survey to the GenAI service. They can either connect the frontend survey directly to the GenAI service or route requests
through a backend server, which is a private, researcher-controlled server that acts as an intermediary. While direct frontend con-
nections offer simplicity, using a backend is the professional standard for larger-scale studies. This architecture’s primary advantage is
security, as the API key remains stored on the private server, never exposed to participants’ browsers. Though the risk of survey
participants actively misusing an API key is minimal, backend routing prevents accidental key discovery or harvesting by automated
web scrapers—a particular concern for publicly available surveys.
The choice between direct frontend connection and backend architecture involves balancing simplicity against security re-
quirements. Direct frontend connections work well for rapid prototyping, pilot studies, and research with known participant pools.
Cost risks can be prevented by using pre-paid systems as described above. However, backend implementations provide the credential
security sometimes required by IRBs or university data policies but they come along with additional implementation complexity.
Researchers should select the architecture that aligns with their project’s specific context, participant pool, and institutional
requirements.
4.1.5. Operational and ethical aspects
Before showcasing the individual implementation steps for the described components, there are some operational and ethical
aspects to consider. First, researchers must obtain explicit informed consent from study participants before any AI interaction, clearly
stating that participant responses will be processed by an external service. Direct links to the provider’s data processing policies should
be included as participant inputs will be transmitted to third-party commercial entities (Weisz et al., 2024).
Instructions to the system’s behavior (i.e., system prompts) should be carefully designed to avoid soliciting personally identifiable
information from participants. When sensitive data is collected separately through the survey platform—researchers must ensure such
Table 3
Overview of GenAI models categorized by modality.
Input Modality
(s)
Output Modality
(s)
Description / Common Tasks Examplary Models
Text Text Generating human-like text, conversation, summarization, and
translation
GPT-4, Claude 3 Opus, Gemini 1.5 Pro, Llama 3
Text Code Generating computer code from natural language or code
prompts
GitHub Copilot, AlphaCode 2, Gemini,
CodeLlama
Text Image Creating images from textual descriptions Stable Diffusion 3, Midjourney v7, DALL-E 3,
Imagen 2
Text Video Creating video clips from textual descriptions Sora, Runway Gen-3, Make-A-Video
Text Audio (Speech) Synthesizing human-like speech from text (Text-to-Speech) ElevenLabs TTS, Bark, VALL-E X
Text Audio (Music/
Sound)
Generating music or sound effects based on text prompts MusicLM, Stable Audio 2.0, AudioCraft
Image Text Describing images in natural language (Captioning), Analysis Gemini Series, GPT-4 V, BLIP-2, Florence-2
Image (+ opt.
Text)
Image Modifying existing images based on prompts or styles Stable Diffusion (img2img, ControlNet),
Pix2PixHD
Video Text / Data Analyzing video content, generating descriptions or summaries Gemini Series, Video-LLaMA, various analysis
models
Audio Text Transcribing spoken language into text Whisper, Google Cloud Speech-to-Text
M. Joerling
International Journal of Research in Marketing xxx (xxxx) xxx
11

information is not transmitted to the GenAI service through embedded data fields or other mechanisms. Anticipating potential data
disclosure risks helps maintain participant privacy while collecting necessary interaction data.
Technical failures are inherent to systems dependent on external services and cannot be entirely eliminated. Network interruptions,
API outages, or rate limiting can all disrupt the participant experience. Researchers should establish rules for handling such disruptions
and check for incomplete or corrupted data in the final data set. Additionally, researchers can test whether participants can connect to
the AI service at the very start of the survey (please see page 33 in the web appendix for the technical instructions on such a con-
nectivity check). This simple check prevents participants from investing time in a study they cannot complete due to network re-
strictions, allowing researchers to redirect affected participants immediately rather than after they have begun responding to
questions.
Finally, documentation is essential for research validity and reproducibility. GenAI service providers may update their models
without notice, potentially altering behavior in ways that affect research outcomes. Researchers must record the specific model used
(including version numbers when available), all API configuration parameters such as temperature settings and system prompts
employed during data collection (Ganguly et al., 2025). This documentation ensures that results can be appropriately interpreted and
potentially replicated. Together, these considerations represent important methodological foundations for responsibly integrating
GenAI interactions into research studies.3
4.2. Coding assistants
A remarkable aspect of using GenAI is that the technology itself provides the most powerful means for its own implementation. This
empowers researchers, even those with little to no coding experience, to build the very GenAI-driven integrations they need for their
studies (Cui et al., 2025). This is made possible by a new category of specialized AI coding assistants. Unlike general-purpose chatbots
like ChatGPT, which only process isolated prompts, these specialized tools have a complete understanding of all the files in a research
project codebase. This “project awareness” is a crucial advantage. However, these assistants vary in user-friendliness. While some
operate through technical command-line interfaces, tools like Cursor or Windsurf provide familiar point-and-click interfaces similar to
standard word processors. Researchers can simply highlight code, click buttons, and chat with the AI assistant.
Cursor, for example, functions as a versatile workbench where code can be created. Its most transformative feature for researchers
with limited or no coding experience is the integrated AI chat. A researcher can simply type a request in plain English—such as, “Create
a JavaScript for Qualtrics to embed an interaction with ChatGPT”—and the AI translates this into a functional code snippet, which
could be integrated into Qualtrics. As seen in the screenshot below, the interface presents the chat on the right panel and generates the
corresponding code files in the main window. These files can be saved directly in a folder on the computer, ready for use. In the
example below, the coding assistant also automatically created a README file that helps with the further Qualtrics integration (Fig. 2).
For generating code, these tools offer different ways to manage their integrated AI assistant, which typically involves a trade-off
between automation and user control. The most common method is an “Ask” mode, which functions like a conversation. Here, the
researcher gives a command to the coding assistant, and the AI proposes the corresponding code. The researcher can then review and
approve the provided code, ensuring full control over the process. In contrast, an “Agent” mode offers a more hands-off approach. In
this mode, the researcher describes a goal in natural language, and the Agent works autonomously across multiple files to achieve it.
This is powerful but involves trusting the AI to complete the project independently.
To further refine the code generation in these coding assistants, researchers can use a feature called Rules (Cursor, 2025). Think of
rules as a permanent set of instructions or a style guide for the AI assistant, which prevents the need to repeat the same directions in
every prompt. For a Qualtrics study, a researcher could, for example, establish a general rule like the creation of README files to
provide implementation instructions or a project-related rule to ensure data quality and a good participant experience:
When creating new code snippets, always create an accompanying README file that explains their Qualtrics integration. Moreover, always
create code that saves the participant’s prompt to an embedded data field named ’user_prompt’ and the AI’s full response to ’ai_response’ after
every AI interaction. While the participant is waiting for the AI to reply, always display a “Loading…” message. If the connection to the AI fails,
display a simple error message to the participant and save the value ’API_ERROR’ in the ’ai_response’ field.
Once saved, the AI will automatically incorporate this logic into any future code it generates for the project. This ensures that
critical data is never lost and that the participant experience is consistent, without the researcher having to remember the coding
assistant. These coding assistants enable researchers—even without coding experience—to generate, test, and debug code connecting
Qualtrics with any GenAI model, as shown through step-by-step tutorials for marketing-relevant applications. Before presenting the
walk-throughs, understanding effective interaction with AI coding assistants will significantly improve success rates. The table below
presents practices that have proven essential (Table 4).
4.3. Implementation walk-throughs
This section provides one practical implementation walk-through for a GenAI-powered research tool within Qualtrics, using the
described coding assistant. Due to space constraints, three further walkthroughs are provided in the web appendix (pages 23–30),
following the same structure as the walkthrough in the manuscript. The examples address common marketing research needs related to
3 For a further discussion on responsible GenAI usage in marketing research see: Blanchard et al. (2025).
M. Joerling
International Journal of Research in Marketing xxx (xxxx) xxx
12

some of the themes identified in the literature review: understanding how consumers use GenAI to search for online information
(Melumad, 2023; Melumad & Yun, 2025; Spatharioti et al., 2023; Xu et al., 2023), conducting in-depth interviews at scale to un-
derstand consumer insights (Chopra & Haaland, 2023; Epp & Humphreys, 2025), the effective usage of GenAI as a co-creation tool
(Celiktutan et al., 2024; Lee & Chung, 2024), and GenAI’s power to persuade by creating hyper-individualized output (Hackenburg &
Fig. 2. Example of a coding assistant showing natural language prompt and created script.
Table 4
Best practices when working with coding assistants.
Setup and Implementation
​ • Use meta-prompting: Ask any LLM to help formulate detailed prompts for the coding assistant. Example: “Create a detailed prompt I can give to a coding
assistant to build […] in Qualtrics”
• Include API documentation: Always paste the provider’s API documentation (found on the provider’s website) with the prompt to the coding assistant
the coding assistant needs this exact syntax
• Follow code markers: Keep placeholder comments like “//Place your API Key here//” and follow embedded instructions
• Request documentation: Ask for a README file with implementation instructions, or set this as a rule to automatically generate documentation with every
code output
• Consolidate if needed: Request “Combine everything into a single JavaScript file for Qualtrics” if multiple files are generated
• Test properly: Use anonymous survey links, not preview mode (which may block features like audio recording) in Qualtrics for testing the provided code
Troubleshooting
​ • Use browser console to identify errors: Open it in your web browser by pressing F12 (or right-click anywhere on the page and select “Inspect”), then click
the “Console” tab. This shows what happens behind the scenes when the code runs. Red text indicates errors, yellow text shows warnings (usually not
critical), and white/gray text shows normal operations. Look for red error messages that often include line numbers and descriptions like “API key not
defined” or “Cannot read property of undefined”
• Share errors with assistant: Screenshot console errors and provide to coding assistant: “The code produces this error: [error text]. Please fix it”
• Be specific about issues: Describe unexpected behavior precisely (e.g., “The chat displays, but responses don’t save to embedded data”)
• Remember variability: AI-generated code is probabilistic  test thoroughly as the same prompt may produce different results
Table 5
Overview of basic implementation steps.
Step Action Description
1 Create Qualtrics Survey and
Question Container
Create a new project in Qualtrics and add a Text/Graphic question. This question will serve as the container for your
AI interface.
2 Get API Credentials Sign up with a provider (e.g., OpenAI, Anthropic). Generate an API Key in your account settings and copy the
provider’s API Documentation page.
3 Generate Code Open an AI Coding Assistant (e.g., Cursor). Paste the API documentation and a prompt: “Create a JavaScript for
Qualtrics that sends user input to this API and saves the reply to embedded data”.
4 Configure Script Save the code generated by the assistant. Insert your API Key into the code where the assistant indicated (e.g., const
API_KEY = ’your-key-here’).
5 Embed Script Return to your Qualtrics question (Step 1), open the JavaScript editor, and paste your fully configured code.
6 Define Data Fields In Qualtrics Survey Flow, add an Embedded Data element. Add the specific variable names used in your code (e.g.,
user_prompt, ai_response) so the data saves correctly.
7 Test Connection Test the survey. Interact with the AI to ensure it responds and check Data & Analysis to confirm all data is being
captured.
M. Joerling
International Journal of Research in Marketing xxx (xxxx) xxx
13

Margetts, 2024; Kapoor et al., 2025). All presented applications can be built using the straightforward approach of connecting
Qualtrics directly to AI services, making them accessible to researchers with a limited technical background. Subsequently, the po-
tential backend implementation is presented. The examples have been selected to demonstrate the breadth of possibilities, using GenAI
as a research method and as a research object. Moreover, different GenAI services are used, demonstrating that the approach can be
easily transferred to basically any GenAI service and model. Before the walk-throughs are described in detail, the following table gives
an overview of the basic steps that a researcher needs to go through for the implementation (Table 5).
4.3.1. Walk-through: The GenAI search assistant
The emergence of GenAI substantially impacted how people search for information, which represents one of the three main use
cases of ChatGPT (Chatterji et al., 2025). Moreover, about 58 % of consumers have already replaced search engines with GenAI tools
for product or service recommendations (Capgemini, 2025), and search patterns have shifted from shorter, more navigational search
queries to longer, more conversational prompts (Solis, 2025). Additionally, when AI provides synthesized answers, click-through rates
plummet to just 8 % as 26 % of users end their search entirely after reading AI responses (Kelly, 2025). For marketers, this creates new
challenges but also opportunities, prompting relevant questions about how to adapt. For example, how do consumers search for in-
formation, and how do they make decisions when search becomes conversation? What drives engagement in AI-generated search
results? How do marketers optimize for AI recommendations? The tool presented below enables researchers to systematically
investigate these questions.
Tool components. This application combines two parts: a Qualtrics survey as an interface and a GenAI service that can search the web
and provide answers. This example uses OpenAI’s GPT model with web search access. Researchers can identify suitable AI models for
their needs through simple web searches (e.g., “AI model with web search API” or “GenAI models with internet access”), consulting AI
comparison websites, directly asking any AI assistant about available options, or visiting the web pages of AI model aggregators (e.g.,
OpenRouter, AIMLAPI). To connect these pieces, instructions are needed for how Qualtrics should communicate with the selected
GenAI service through its API. These instructions, called API documentation, are freely available in the developer section of any GenAI
service provider’s website—OpenAI, Google, Anthropic, and others all provide this documentation in a similar format. While these
instructions might appear complex initially, they serve as a standardized recipe that the AI coding assistant will follow exactly when
generating the required code snippets. Researchers simply copy this documentation from the provider’s website (see Fig. 3 below) and
paste it into the coding assistant along with instructions describing what they want to build.
Building the tool. With the API documentation ready, researchers now need to tell the coding assistant what to build. These in-
structions should specify three elements: interface design (e.g., chat window, buttons), functionality (e.g., sending queries, displaying
responses), and data storage (which embedded data fields to populate). Rather than writing these from scratch, researchers can use any
GenAI model to help create this prompt (i.e., meta-prompting). Below is an example prompt that researchers can adapt or use directly:
“Create a JavaScript snippet for Qualtrics. It should power a chat interface with the HTML elements ’chat-container’, ’chat-box’, ’user-
input’, and ’send-btn’. When the user clicks the send button, take the text from ’user-input’ and send it to the web search of OpenAI (the
documentation is below). Display a ’loading…’ message while waiting. Show the AI’s response in the chat box. Before sending the API
request, store the user’s full prompt in the Qualtrics embedded data field named user_prompt. After receiving the response, store the entire
Fig. 3. OpenAI’s API documentation.
M. Joerling
International Journal of Research in Marketing xxx (xxxx) xxx
14

AI message in the ai_response field. Ensure you include error handling. Integrate the HTML and JavaScript into one script that I can add
as JavaScript to a Qualtrics question. Prioritize the robustness and functionality of input and output.”
After providing this prompt, paste the OpenAI API documentation for web search functionality directly below this prompt into the
coding assistant.
The coding assistant will create the corresponding code, and the following three straightforward steps are required for
implementation:
Configure the Code: Save the generated code as a file on your computer (e.g., web_search.js) and insert the API key from OpenAI
into the designated spot (marked as ‘your-openai-api-key-here’ in the code generated by the coding assistant) (Fig. 4).
Prepare Qualtrics: In the Survey Flow section, create two embedded data fields called user_prompt and ai_response. These must
appear before the question containing the chat tool. Leave the value of these fields empty.
Add to Survey: Create a Text/Graphic question, open its JavaScript editor following the platform’s standard procedure for adding
custom JavaScript (see: https://www.qualtrics.com/support/survey-platform/survey-module/question-options/add-javascript/),
and paste the entire code from the coding assistant, including the added API key.
Test the survey: When you reach the question where the JavaScript was added, you will see the Chat interface (Fig. 5).
Enhancing the tool. Once the basic tool is working its functionalities can be continuously expanded with simple additional in-
structions. In the coding assistant’s chat panel, describe the enhancement you want. The assistant will display the proposed changes
directly in your existing code in the main editor window, with visual indicators showing additions (typically in green) and deletions
(typically in red). Review these inline changes carefully before accepting to ensure core functionality remains intact.
For instance, to track which links participants click within AI responses: “Modify the script to save the URL of any link the participant
clicks on in an embedded data field named clicked_link.” This enhancement adds tracking functionality—when participants click any link
in the AI’s response, that URL is automatically captured and will appear in the downloaded data as a new column, enabling analysis of
which sources or suggestions participants found most relevant. Similarly, researchers can modify the chat interface or the AI’s behavior
by adjusting the system prompt—instructing it to be more descriptive, add emojis for emotional tone, adopt a specific brand voice, or
limit responses to certain word counts—allowing systematic testing of how different AI communication styles influence user
engagement and decision-making. Moreover, researchers can consider adding this rule to the coding assistant for developing search
applications in general: “For search applications, always parse and display the search results in a readable format with clear source attribution.
Store both the query and the complete response, including metadata.”.
Data collection. The tool captures complete interaction data: what participants asked (user_prompt), the full AI response (ai_r-
esponse), and any links clicked (clicked_link). This data appears in the standard Qualtrics data files and can be downloaded for
analysis. Researchers can analyze search patterns, identify which information participants found most useful, and understand decision-
making sequences through these recorded interactions (Fig. 6).
Experimental comparisons and benchmarking. To understand how AI-powered search transforms information seeking, researchers
should compare this conversational approach against traditional search engines (Google/Bing with standard result listings). This
comparison establishes whether AI synthesis fundamentally changes how users explore information versus self-directed searching.
The response presentation can be also systematically varied, comparing synthesized narratives versus structured bullet points,
inline citations versus separate reference lists, concise answers versus comprehensive explorations, and varying levels of confidence
indicators. Researchers could also test different AI personas (expert advisor versus neutral assistant), response timing (immediate
versus delayed), and visual enhancements (highlighting, relevance scores, source credibility badges).
Key measures should capture search efficiency (time to decision, query count), information quality (accuracy, decision confidence),
user experience (perceived helpfulness, trust), and behavioral outcomes (link clicks, final choices). Moreover, researchers could
examine whether GenAI surfaces similar or distinctly different results compared to traditional search engines, revealing the tech-
nology’s potential to expand discovery beyond conventional information pathways. This design reveals not only whether AI search
changes information seeking but also how specific presentation choices shape user trust, comprehension, and decision quality in this
new search paradigm.
4.3.2. Using a backend
The presented application will work when following the descriptions above. However, if a researcher wants to manage the
communication between the Qualtrics interface and the GenAI model through a backend to protect the API key, the following
description shows how researchers can make this transition using AI coding assistance.
Converting to Backend Architecture. The backend server is essentially a separate computer or cloud service. To build this
Fig. 4. Adding an API key to the generated JavaScript code.
M. Joerling
International Journal of Research in Marketing xxx (xxxx) xxx
15

intermediary system, researchers can use web frameworks, pre-built software tools that simplify server creation. Flask, which uses the
Python programming language, is particularly suitable for research applications because it requires minimal technical setup. The
server creates a specific receiving point (i.e., API endpoint, similar to a dedicated email address like /api/search) where survey input
arrives from Qualtrics. For security reasons, web browsers normally prevent different websites from communicating directly with each
other. Therefore, the server needs special permission settings (i.e., CORS—Cross-Origin Resource Sharing configuration) that explicitly
allow Qualtrics and the backend to exchange information. Additionally, the server stores API keys in a protected area separate from the
main code (i.e., environment variables). To create this backend system, researchers can use the following two prompts with a coding
assistant:
First, to request the server code: “Convert the existing web search tool to use a backend architecture. Create a Python Flask server that: 1)
Stores the OpenAI API key securely as an environment variable, 2) Receives search queries from Qualtrics through an /api/search endpoint, 3)
Handles the web search requests to the OpenAI server-side, 4) Returns search responses to Qualtrics with proper CORS configuration for
Qualtrics domains, 5) Includes error handling and query logging.“.
Second, update the Qualtrics code: “Modify the Qualtrics JavaScript to communicate with our backend server instead of OpenAI directly.
It should: 1) Send user queries to the backend, 2) Display appropriate loading messages, 3) Handle timeouts gracefully (30 s), 4) Save responses
to the same embedded data fields (user_prompt and ai_response), 5) Show user-friendly messages if the server is unreachable.”.
The coding assistant will generate both components, creating a secure architecture where participants never access the API key
directly.
Step-by-Step Implementation. Researchers can host their backend server at beginner-friendly platforms such as Render.com. The
deployment process involves several straightforward steps. First, researchers create a free account on the hosting platform and select
“New Web Service.” The Python code must then be stored in a GitHub repository (please see page 37 in the web appendix for a more
detailed explanation on GitHub). This repository is subsequently connected to the hosting service, a process guided by the platform’s
interface. The critical security configuration involves storing the API key as an environment variable (typically named OPEN-
AI_API_KEY, when using an OpenAI model) within the hosting platform’s settings interface, rather than embedding it directly in the
code where it would be visible. After deployment is initiated by a simple click in the hosting service, the platform generates a public
Fig. 5. The web search tool interface in Qualtrics showing user query and AI response.
Fig. 6. Data captured by the search tool in embedded data fields, showing user query, AI response, and clicked link.
M. Joerling
International Journal of Research in Marketing xxx (xxxx) xxx
16

URL (e.g., https://search-bot.onrender.com). This URL serves as the secure connection point that researchers enter in Qualtrics to
route survey requests through the backend to the AI service.
Once the server is running, the Qualtrics survey requires updating. The original JavaScript code is replaced with the backend-
enabled version generated by the coding assistant. Within this new code, researchers must locate the server URL reference (typi-
cally appearing as https://localhost:5000/api/search) and replace it with the actual deployed server URL (e.g., https://search-bot.
onrender.com).
Common deployment challenges. Several common issues may arise during backend implementation that the coding assistant can help
resolve. One frequent problem occurs when the server blocks requests from Qualtrics due to security settings. Essentially, the server
doesn’t recognize Qualtrics as a trusted source. The coding assistant can fix this configuration issue when given a prompt such as
“Update the Flask configuration to accept requests from Qualtrics domains.” Researchers can ensure proper configuration by providing the
coding assistant with the specific Qualtrics web address shown in their browser’s address bar, allowing automatic setup for that
particular survey platform.
Server overload represents a significant challenge when multiple participants access the study simultaneously. Free hosting tiers
have limited processing power and can become overwhelmed, leading to slow responses or crashes. This is particularly problematic
with resource-intensive services like image generation. The most practical solution for researchers is to control participant flow
through the study platform. On Prolific or MTurk, researchers should release the study in smaller batches (for example, 20–30 par-
ticipants at a time) rather than opening it to hundreds simultaneously. If the server still overloads, it is required to upgrade the service
(please see pages 31–32 in the web appendix for a discussion on hosting services).
If the server indicates the API key cannot be found, this typically means the environment variable wasn’t properly configured. The
coding assistant can provide platform-specific instructions with “Show me how to properly set environment variables on [platform name (e.
g, render.com)].”.
5. Research avenues for GenAI interactions in research studies
The implementation examples presented above and in the web appendix demonstrate the practical feasibility of integrating GenAI
interactions into research studies. The same methodological approach using AI coding assistants can be applied to create virtually any
GenAI-powered research instrument by describing it in natural language to coding assistants. Technical barriers that once limited such
implementations have largely been removed, opening new possibilities for innovative study designs. The following section discusses
some of these possibilities, starting with GenAI implementations for methodological purposes, followed by its integration to investigate
AI itself.
First, AI-powered interviews emerge as an exceptionally versatile tool that addresses multiple methodological challenges simul-
taneously. These interviews can uncover underlying motivations and process variables for subsequent quantitative testing, potentially
bridging the traditional divide between qualitative and quantitative research. Their scalability enables researchers to conduct large
numbers of interviews that may complement human-led sessions. AI interviews might follow human interviews to build on initial
insights, or run in parallel to uncover different patterns due to participants’ varying responses to AI versus human interviewers. Indeed,
initial research suggests hybrid human-AI approaches may be optimal, leveraging human interviewers for depth while using AI for
scale and pattern detection across large samples (Arora et al., 2025).
However, critical questions remain about optimizing AI interview design and performance. For example, whether participants
disclose more sensitive information to AI than human interviewers remains an open empirical question, with potential implications for
studying stigmatized behaviors. Additionally, the interaction modality (speaking versus writing) may affect disclosure differently
across topics, with spontaneous responses potentially benefiting from speech while complex reflections benefit from writing (Gaerth
et al., 2025). These design parameters await empirical validation to establish best practices for different research contexts.
Moreover, GenAI interviews may provide an elegant solution to encounter demand effects and social desirability bias. Rather than
administering scales that explicitly name constructs—thereby priming participants—researchers can conduct neutral conversational
interviews about general topics and then analyze transcripts post-hoc for construct presence. For instance, instead of measuring
materialism through direct scales, which may trigger socially desirable responding, an AI interviewer can discuss recent purchases,
gift-giving, or lifestyle aspirations. The resulting transcripts may reveal materialistic values that can be potentially quantified without
alerting participants to this focus. This approach shows whether constructs genuinely emerge in natural discourse or only appear when
explicitly prompted. If such an approach is feasible and how it needs to be designed can be element of future research.
Beyond exploratory interviews, GenAI enables entirely new research paradigms that were previously impossible or prohibitively
complex to implement. Considering the fundamental challenge of studying collaborative consumption or group decision-making,
researchers have traditionally faced enormous logistical hurdles in synchronizing multiple participants for real-time online in-
teractions. GenAI elegantly solves this by simulating collaborators with precise experimental control. For example, researchers can
now investigate how people reach a conclusion in group decisions (like group travel planning, household purchasing decisions, or
charity allocation of study bonuses). Each participant can engage with AI collaborators programmed with specific personalities,
expertise levels, or influence tactics, enabling clean experimental manipulations that would be impossibly messy with human
confederates.
Another compelling example of GenAI-enabled research paradigms is temporal manipulation. For example, an extensive psy-
chology study with over 60,000 participants demonstrated that conversations with an AI-simulated future self significantly reduce
anxiety (Pataranutaporn et al., 2024). This finding has profound implications for marketing, as temporal perspective fundamentally
shapes decision-making in general (Sagristano et al., 2002; Trope & Liberman, 2010), and consumer behavior in particular (Kyu Kim
M. Joerling
International Journal of Research in Marketing xxx (xxxx) xxx
17

et al., 2012). When participants can engage with a vivid, personalized representation of their future selves—one that can discuss the
consequences of today’s choices, share regrets about missed opportunities, or express gratitude for past decisions—it creates a psy-
chological bridge between present actions and future outcomes. This temporal manipulation paradigm could influence how marketers
approach long-term behavior change, from promoting retirement savings and insurance adoption to encouraging sustainable con-
sumption and health-conscious purchasing. The ability to make abstract future consequences feel immediate and personal through AI
conversation represents a methodological innovation that was simply impossible before GenAI. While the temporal manipulation
seems very powerful, researchers can explore countless alternative paradigms. Imagine participants conversing with versions of
themselves raised in different cultures to study how cultural context shapes consumer identity, or chatting with alternate selves who
made different career choices to understand professional identity’s role in consumption patterns. The implementation of such
experimental treatments is limited only by the researcher’s creativity, as GenAI can convincingly simulate any counterfactual version
of the self.
Turning to GenAI as a research object, the technology itself becomes the phenomenon under investigation. Consider, for example,
how GenAI transforms information search. Evidence of 80 million clickstream records shows that ChatGPT directs users differently
than traditional search (Kelly, 2025). This raises critical questions for marketers and content creators: How deeply do consumers
engage with AI-synthesized search results compared to traditional lists of links? Do they click through to original sources or accept AI
summaries at face value? In co-creation and collaboration contexts, AI becomes an active partner in generating content and ideas,
prompting different questions: Do individual co-created outcomes get better, but does the collectivity of co-created outcomes fall
victim to an average trap (Huang & Rust, 2025)? When sharing AI-co-created content (e.g., on platforms like etsy), do consumers
disclose AI involvement? Meanwhile, in consumer-company interactions, as AI increasingly mediates or replaces human touchpoints,
researchers must ask: When AI agents make purchasing decisions on behalf of consumers, how does this alter brand relationships and
loyalty? How does service recovery differ when the service failure involves an AI rather than a human employee? These examples
represent just a fraction of the contexts where GenAI influences marketing-relevant questions.
Finally, researchers can explore additional experimental variations. Response timing, for instance, carries psychological
weight—instant responses might suggest pre-formed databases while delays imply thoughtful consideration. Transparency levels offer
another avenue, with the recent introduction of “chain-of-thought” displays enabling studies of whether visible reasoning increases or
decreases trust (Piper, 2025). Autonomy and agency levels become critical as AI moves from assistant to actor, with researchers able to
vary decision-making authority from purely advisory to fully delegated across different product categories and purchase situations.
Together, these manipulable dimensions represent multifold research avenues for understanding how GenAI characteristics shape
consumer behavior and marketing outcomes.
6. Conclusion
This paper provides marketing researchers with a comprehensive guide for integrating GenAI interactions into research studies. It
demonstrates that technical barriers to integrating GenAI interactions into marketing research have effectively disappeared. By un-
derstanding the core architectural components (frontend, backend, GenAI service via API) and leveraging the provided templates and
resources, researchers without programming expertise can now oversee and implement sophisticated GenAI research tools—from
scalable AI interviews to controlled experiments with AI collaborators. The paper equips researchers with the conceptual knowledge to
guide implementations using AI coding assistants or to adapt the provided templates directly for their specific needs.
The rapid evolution of GenAI capabilities means that the specific models and implementations described here will inevitably be
superseded. However, the underlying approach—recognizing the potential value of GenAI integrations, understanding the core
architectural components, knowing how to articulate requirements clearly, and using AI to implement AI—provides a durable
foundation for continued advancement. As GenAI increasingly mediates marketplace interactions, from product discovery to customer
service to purchase decisions, marketing researchers need to develop the capabilities to study these new realities.
The practical walkthroughs and open-source resources (https://github.com/QualtriGen) provide immediate starting points, but
more importantly, they illustrate a fundamental shift: researchers can now create experimental paradigms that were previously
impossible, bridge qualitative depth with quantitative scale, and study AI-mediated consumer behavior as it actually occurs.
During the preparation of this work the author used Gemini 2.5, and Claude Opus 4.1 in order to copy edit content and generate
supporting materials. After using this tool/service, the author reviewed and edited the content as needed and takes full responsibility
for the content of the publication.
CRediT authorship contribution statement
Moritz Joerling: Writing – review & editing, Writing – original draft, Visualization, Validation, Software, Resources, Project
administration, Methodology, Investigation, Formal analysis, Data curation, Conceptualization.
Declaration of competing interest
The authors declare that they have no known competing financial interests or personal relationships that could have appeared to
influence the work reported in this paper.
M. Joerling
International Journal of Research in Marketing xxx (xxxx) xxx
18

Acknowledgements
I want to thank the anonymized researchers that have participated in the group discussions.
Appendix A. Supplementary data
Supplementary data to this article can be found online at https://doi.org/10.1016/j.ijresmar.2025.12.003.
Data availability
No data was used for the research described in the article.
References
Allamong, M., Trexler, A., Alqabandi, F., LaChapelle, T., Bail, C. A., Hillygus, D. S., & Volfovsky, A. (2024). Outnumbered Online: The Consequences of Partisan Imbalance
in Online Political Discussions. OSF. https://doi.org/10.31219/OSF.IO/TYGEC
Argyle, L. P., Busby, E. C., Gubler, J. R., Lyman, A., Olcott, J., Pond, J., & Wingate, D. (2025). Testing theories of political persuasion using AI. Proceedings of the
National Academy of Sciences of the United States of America, 122(18). DOI: 10.1073/pnas.2412815122.
Arora, N., Chakraborty, I., & Nishimura, Y. (2025). AI–Human Hybrids for Marketing Research: Leveraging Large Language Models (LLMs) as Collaborators. Journal of
Marketing, 89(2), 43–70. https://doi.org/10.1177/00222429241276529
Berners-Lee, T., & Connolly, D. (1993). Hypertext Markup Language (HTML) (Version 1.2; Internet Draft). https://www.w3.org/MarkUp/draft-ietf-iiir-html-01.txt.
Bi, X., Chen, D., Chen, G., Chen, S., Dai, D., Deng, C., Ding, H., Dong, K., Du, Q., Fu, Z., Gao, H., Gao, K., Gao, W., Ge, R., Guan, K., Guo, D., Guo, J., Hao, G., Hao, Z., …
Zou, Y. (2024). DeepSeek LLM: Scaling Open-Source Language Models with Longtermism. https://arxiv.org/abs/2401.02954v1.
Blanchard, S. J., Duani, N., Garvey, A. M., Netzer, O., & Oh, T. T. (2025). New Tools, New Rules: A Practical Guide to Effective and responsible GenAI Use for surveys
and Experiments Research. Journal of Marketing, 89(6), 119–139. https://doi.org/10.1177/00222429251349882
Capgemini. (2025). 71% of consumers want generative AI integrated into their shopping experiences. https://www.capgemini.com/news/press-releases/71-of-consumers-
want-generative-ai-integrated-into-their-shopping-experiences/.
Celiktutan, B., Klesse, A. K., & Tuk, M. A. (2024). Acceptability lies in the eye of the beholder: Self-other biases in GenAI collaborations. International Journal of
Research in Marketing, 41(3), 496–512. https://doi.org/10.1016/j.ijresmar.2024.05.006
Chatterji, A., Cunningham, T., Deming, D. J., Hitzig, Z., Ong, C., Shan, C. Y., & Wadman, K. (2025). How People Use ChatGPT.. https://doi.org/10.3386/W34255
Chopra, F., & Haaland, I. (2023). Conducting Qualitative Interviews with AI. In SSRN Electronic Journal. Elsevier BV. DOI: 10.2139/SSRN.4583756.
Costello, T. H., Pennycook, G., & Rand, D. G. (2024). Durably reducing conspiracy beliefs through dialogues with AI. Science. https://doi.org/10.1126/SCIENCE.
ADQ1814
Cui, Z. (Kevin), Demirer, M., Jaffe, S., Musolff, L., Peng, S., & Salz, T. (2025). The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments
with Software Developers. DOI: 10.2139/SSRN.4945566.
Cursor. (2025). Cursor – Rules. https://docs.cursor.com/en/context/rules#adding-a-new-setting-in-cursor.
De Freitas, J., O˘guz-U˘guralp, Z., U˘guralp, A. K., & Puntoni, S. (2025). AI Companions Reduce Loneliness. Journal of Consumer Research. https://doi.org/10.1093/JCR/
UCAF040
Doshi, A. R., & Hauser, O. P. (2024). Generative AI enhances individual creativity but reduces the collective diversity of novel content. Science Advances, 10(28), 5290.
https://doi.org/10.1126/SCIADV.ADN5290/SUPPL_FILE/SCIADV.ADN5290_SM.PDF
Epp, A. M., & Humphreys, A. (2025). Collaborating with Generative AI in Consumer Culture Research. Journal of Consumer Research, 52(1), 32–48. https://doi.org/
10.1093/JCR/UCAF014
Flamino, J., Modi, M. S., Szymanski, B. K., Cross, B., & Mikolajczyk, C. (2025). Testing the limits of large language models in debating humans. Scientific Reports, 15
(1), 1–13. https://doi.org/10.1038/s41598-025-98378-1
Flanagan, D. (2011). JavaScript : The definitive guide (6th ed.). O’Reilly.
Gaerth, M., Melumad, S., & Meyer, R. J. (2025). The Social Nature of Voice Technology. In SSRN Electronic Journal. Elsevier BV. DOI: 10.2139/SSRN.5296839.
Ganguly, A., Johri, A., Ali, A., & McDonald, N. (2025). Generative artificial intelligence for academic research: Evidence from guidance issued for researchers by
higher education institutions in the United States. AI and Ethics, 1–17. https://doi.org/10.1007/S43681-025-00688-7
Garvey, A., & Blanchard, S. J. (2025). Generative AI as a Research Confederate: The LUCID Methodological Framework and Toolkit for Human-AI Interactions Research..
https://doi.org/10.2139/SSRN.5256150
Hackenburg, K., & Margetts, H. (2024). Evaluating the persuasive influence of political microtargeting with large language models. Proceedings of the National
Academy of Sciences of the United States of America, 121(24), Article e2403116121. https://doi.org/10.1073/pnas.2403116121
Hosanagar, K., & Ahn, D. (2024). Designing Human and Generative AI Collaboration. https://arxiv.org/pdf/2412.14199.
Huang, M. H., & Rust, R. T. (2025). The GenAI Future of Consumer Research. Journal of Consumer Research, 52(1), 4–17. https://doi.org/10.1093/JCR/UCAF013
Hussein, M. A., Tormala, Z. L., & Wheeler, S. C. (2026). Why do people choose extreme candidates? the role of identity relevance. Journal of Experimental Social
Psychology, 122, Article 104821. https://doi.org/10.1016/J.JESP.2025.104821
Jin, B., Sahni, S., & Shevat, A. (2018). Designing Web APIs: Building APIs That Developers Love. O’Reilly Media, Inc. https://books.google.fr/books?
id=Dg1rDwAAQBAJ&redir_esc=y.
Kalim, M. (2013). Java Web Services:Up and Running. In O’Reilly.
Kapoor, A., Kumar, M., & Trulaske, R. J. (2025). Frontiers: Generative AI and Personalized Video Advertisements. Marketing Science, 44(4). https://doi.org/10.1287/
MKSC.2023.0494
Karakas¸, N., & Jaeger, B. (2025). Changes in attitudes toward meat consumption after chatting with a large language model. Social Influence, 20(1). https://doi.org/
10.1080/15534510.2025.2475802
Kelly, B. (2025, February 3). Investigating ChatGPT Search: Insights from 80 Million Clickstream Records. https://www.semrush.com/blog/chatgpt-search-insights/.
Kyu Kim, B., Zauberman, G., & Bettman, J. R. (2012). Space, time, and intertemporal preferences. Journal of Consumer Research, 39(4). https://doi.org/10.1086/
666464
Lee, B. C., & Chung, J. (2024). An empirical investigation of the impact of ChatGPT on creativity. Nature Human Behaviour 2024 8:10, 8(10), 1906–1914. DOI:
10.1038/s41562-024-01953-1.
Maier, S., Schneider, M., & Feuerriegel, S. (2025). Partnering with Generative AI: Experimental Evaluation of Human-Led and Model-Led Interaction in Human-AI Co-
Creation (Vol. 1). https://arxiv.org/pdf/2510.23324v1.
Melumad, S. (2023). Vocalizing Search: How Voice Technologies Alter Consumer Search Processes and Satisfaction. Journal of Consumer Research, 50(3), 533–553.
https://doi.org/10.1093/JCR/UCAD009
M. Joerling
International Journal of Research in Marketing xxx (xxxx) xxx
19

Melumad, S., & Yun, J. H. (2025). Experimental Evidence of the Effects of Large Language Models versus Web Search on Depth of Learning.. https://doi.org/10.2139/
SSRN.5104064
MistralAI. (2025). Coding. https://docs.mistral.ai/capabilities/code_generation/.
OpenAI. (2025). Web search - OpenAI API. https://platform.openai.com/docs/guides/tools-web-search?api-mode=chat.
Pataranutaporn, P., Winson, K., Yin, P., Lapapirojn, A., Ouppaphan, P., Lertsutthiwong, M., Maes, P., & Hershfield, H. E. (2024). Future you: A conversation with an
AI-Generated Future self Reduces anxiety, negative Emotions, and increases Future Self-Continuity. In In Proceedings - Frontiers in Education Conference, FIE.
Institute of Electrical and Electronics Engineers Inc. https://doi.org/10.1109/FIE61694.2024.10893443
Piper, K. (2025). January 31). Vox: You’re wrong about DeepSeek. https://www.vox.com/future-perfect/397539/deepseek-artificial-intelligence-chatgpt-openai-
china.
Potter, Y., Lai, S., Kim, J., Evans, J., & Song, D. (2024). Hidden Persuaders: LLMs’ Political Leaning and their Influence on voters. In In EMNLP 2024–2024 Conference
on Empirical Methods in Natural Language Processing, Proceedings of the Conference. Association for Computational Linguistics (ACL). https://doi.org/10.18653/v1/
2024.emnlp-main.244
Sabour, S., Liu, J. M., Liu, S., Yao, C. Z., Cui, S., Zhang, X., Zhang, W., Cao, Y., Bhat, A., Guan, J., Wu, W., Mihalcea, R., Wang, H., Althoff, T., Lee, T. M. C., & Huang,
M. (2025). Human Decision-making is Susceptible to AI-driven Manipulation. https://arxiv.org/pdf/2502.07663.
Sagristano, M. D., Trope, Y., & Liberman, N. (2002). Time-dependent gambling: Odds now, money later. Journal of Experimental Psychology: General, 131(3), 364–376.
https://doi.org/10.1037/0096-3445.131.3.364
Salvi, F., Horta Ribeiro, M., Gallotti, R., & West, R. (2025). On the conversational persuasiveness of GPT-4. Nature Human Behaviour, 1–9. https://doi.org/10.1038/
s41562-025-02194-6
Schoenegger, P., Salvi, F., Liu, J., Nan, X., Debnath, R., Fasolo, B., Leivada, E., Recchia, G., Günther, F., Zarifhonarvar, A., Kwon, J., Ul Islam, Z., Dehnert, M., H Lee, D.
Y., Reinecke, M. G., Kamper, D. G., Kobas¸, M., Sandford, A., Kgomo, J., … Karger, E. (2025). Large Language Models Are More Persuasive Than Incentivized Human
Persuaders. https://arxiv.org/pdf/2505.09662.
Simon, M. (2023). JavaScript for Web Developers. In JavaScript for Web Developers. Apress. DOI: 10.1007/978-1-4842-9774-2.
Solis, A. (2025, July 26). Key Traditional vs AI Search Differences - A Visual Comparison. https://www.aleydasolis.com/en/ai-search/key-traditional-search-ai-
comparison/.
Spatharioti, S. E., Rothschild, D. M., Goldstein, D. G., & Hofman, J. M. (2023). Comparing Traditional and LLM-based Search for Consumer Choice: A Randomized
Experiment. https://arxiv.org/pdf/2307.03744.
Teeny, J. D., & Matz, S. C. (2024). We need to understand “when” not “if” generative AI can enhance personalized persuasion. Proceedings of the National Academy of
Sciences of the United States of America, 121(43). DOI: 10.1073/PNAS.2418005121.
Toner, H. (2023, May 12). What Are Generative AI, Large Language Models, and Foundation Models? Center for Security and Emerging Technology. https://cset.
georgetown.edu/article/what-are-generative-ai-large-language-models-and-foundation-models/.
Trope, Y., & Liberman, N. (2010). Construal-Level Theory of Psychological Distance. Psychological Review, 117(2), 440–463. https://doi.org/10.1037/a0018963.
Construal-Level
Weidinger, L., Inioluwa, D. R., Wallach, H., Mitchell, M., Wang, A., Salaudeen, O., Bommasani, R., Ganguli, D., Koyejo, S., & Isaac, W. (2025). Toward an Evaluation
Science for Generative AI Systems. https://arxiv.org/abs/2503.05336v3.
Weisz, J. D., He, J., Muller, M., Hoefer, G., Miles, R., & Geyer, W. (2024). Design Principles for Generative AI Applications. Proceedings of the 2024 CHI Conference on
Human Factors in Computing Systems, 1–22. DOI: 10.1145/3613904.3642466.
Xu, R. R., Feng, Y. (Katherine), & Chen, H. (2023). ChatGPT vs. Google: A Comparative Study of Search Performance and User Experience. In SSRN Electronic Journal.
Elsevier BV. DOI: 10.2139/SSRN.4498671.
M. Joerling
International Journal of Research in Marketing xxx (xxxx) xxx
20
