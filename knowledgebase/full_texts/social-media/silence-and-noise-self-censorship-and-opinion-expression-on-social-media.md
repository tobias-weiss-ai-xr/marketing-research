---
title: 'Silence and Noise: Self-censorship and Opinion Expression on Social Media'
url: https://arxiv.org/abs/2604.09465
category: social-media
subcategory: empirical
date: 2026-04
venue: ''
authors:
- Xinyu Wang
- Emma Carpenetti
- Bruce Desmarais
- Sarah Rajtmajer
source: arxiv
pdf_url: https://arxiv.org/pdf/2604.09465
pages: 35
chars: 130570
fetched_at: '2026-11-08T12:57:26+00:00'
kb_version: 1
---

# Silence and Noise: Self-censorship and Opinion Expression on Social Media

Silence and Noise: Self-censorship and Opinion Expression on
Social Media
XINYU WANG,The Pennsylvania State University, USA
EMMA CARPENETTI,The Pennsylvania State University, USA
BRUCE DESMARAIS,The Pennsylvania State University, USA
SARAH RAJTMAJER,The Pennsylvania State University, USA
Unlike the more observable phenomenon of group opinion reinforcement, self-censorship online has received
comparatively less attention. Our goal in this work is to dissect the phenomena of self-censorship and to
examine the implications of restrained expression for participation in public discourse, particularly in polarized
contexts. We explore how social media users express their opinions online through analyses of 390 survey
responses and 20 semi-structured interviews using a mixed-methods approach. We ask social media users
about the differences between their publicly shared opinions and privately held beliefs, highlighting the
influence of contextual factors on self-expression. Our findings show that self-censorship is associated with
community context; social media users embedded within larger audiences, with lower posting frequency
and perceived support, are less likely to express their opinions, and those who do speak often adjust their
expressed views to align with perceived group norms. The study complements the rich literature on echo
chambers and opinion reinforcement on social media platforms, highlighting the silence within the noise and
its potential consequences for public discourse, which have become increasingly pertinent in an era where
online platforms are pivotal to social and political narratives.
CCS Concepts:•Social and professional topics → User characteristics;•Human-centered computing →
Empirical studies in HCI;•Information systems→Social networks.
Additional Key Words and Phrases: Self-censorship, Opinion Expression, Social Media Dynamics
ACM Reference Format:
Xinyu Wang, Emma Carpenetti, Bruce Desmarais, and Sarah Rajtmajer. 2026. Silence and Noise: Self-censorship
and Opinion Expression on Social Media.Proc. ACM Hum.-Comput. Interact.10, 6, Article CSCW152 (Octo-
ber 2026), 35 pages. https://doi.org/10.1145/3817000
1 Introduction
Social media encourages the establishment of communities which frame and reinforce a shared
narrative (see, e.g., [24]). In recent years, social media studies have explored opinion formation,
e.g., through the lens of echo chambers and filter bubbles [77, 92], and a variety of models have
been invoked to describe these phenomena [84]. One overarching concern is that the algorithms
behind content dissemination drive polarization and fail to mitigate the spread of misinformation.
The dynamics of misinformation and polarized content have been a topic of significant focus in
recent years [2, 30, 58, 61, 85, 93, 103].
Work in sociology, psychology, and communication has long emphasized the distinction be-
tween privately held opinions and publicly expressed views, particularly in social environments
characterized by conformity pressures [ 40, 49, 55]. This distinction underlies a rich theoretical
Authors’ Contact Information: Xinyu Wang, xzw5184@psu.edu, The Pennsylvania State University, USA; Emma Carpenetti,
The Pennsylvania State University, USA, erc5513@psu.edu; Bruce Desmarais, The Pennsylvania State University, USA,
bdesmarais@psu.edu; Sarah Rajtmajer, The Pennsylvania State University, USA, smr48@psu.edu.
This work is licensed under a Creative Commons Attribution 4.0 International License.
©2026 Copyright held by the owner/author(s).
ACM 2573-0142/2026/10-ARTCSCW152
https://doi.org/10.1145/3817000
Proc. ACM Hum.-Comput. Interact., Vol. 10, No. 6, Article CSCW152. Publication date: October 2026.
arXiv:2604.09465v2  [cs.SI]  22 Jun 2026

CSCW152:2 Wang et al.
tradition documenting how individuals remain silent or adjust their expressed opinions in response
to perceived social pressure and anticipated evaluation [5, 28, 41, 43]. For example, the Spiral of
Silence theory [72] posits that the fear of isolation drives individuals to monitor their environment;
if they perceive that their view is in the minority, they are less likely to voice it [43].
While these theories originated in the context of mass media, their application to the Computer-
Supported Cooperative Work (CSCW) domain introduces new complexities. Digital environments
introduce unique “affordances”, such as context collapse [68], that fundamentally alter how indi-
viduals navigate the tension between their private identity and their public persona [53]. Recent
empirical work has documented manifestations of self-censorship online. Hampton et al. [49] found
evidence of spiral-of-silence effects on social media; Gera et al. [ 42] showed that willingness to
express opinions online varies by topic, with hesitation commonly driven by anticipated audience
reactions; Warner and Wang [96] emphasized the role of privacy concerns and information control
in shaping self-censorship on social networking sites.
However, several gaps remain in our understanding of self-censorship in online contexts. (1)
There is a lack of research into the gradient of self-censorship, specifically the distinction between
complete silence and opinion conformity. Self-silencing theory suggests that these behaviors exist
on a continuum but prior work has not examined how contextual factors are associated with
different points along this continuum. (2) It remains unclear how contextual factors are associated
with users’ corresponding expression decisions. (3) We lack understanding of users’ own perceptions
of the consequences of restrained and reinforced expression and what interventions they believe
might support healthier discourse. This paper addresses these gaps by adopting a mixed-methods
approach to quantify the divergence between public and private opinions. We move beyond the
“observed post” as the unit of analysis to examine the deliberative process users undergo before
deciding to speak or remain silent. Methodologically, we integrate survey data (N=390) that captures
specific differences between private beliefs and public expression across six topical domains, with
semi-structured interviews (N=20) that explore the reasoning behind these patterns.
Our work is scaffolded by the following research questions:
RQ1: Is there a discrepancy between the opinions individuals share publicly through social media
(we will call thesepublic opinions) and their privately held beliefs (we will call theseprivate opinions)?
RQ2: How are contextual factors, e.g., topic, perceived community, and posting behavior, associated
with users’ willingness to share opinions and differences between private and public expression on
social media?
RQ3: What are users’ perceived consequences of opinion conformity and reinforcement, and what
interventions can be implemented to promote healthier social media ecosystems?
By way of these questions, our goal is to explore how self-censorship–literally “the act of preventing
oneself from speaking” [29]–contributes to online conversation dynamics. Our findings suggest
that self-censorship and milder versions of self-censorship, including posting subtle opinions and
engaging passively, can lead to reduced diversity of viewpoints and inadvertently encourage more
extreme views and misinformation to dominate public discourse.
We examine how users navigate these dynamics and identify design directions that can better
support expressive confidence online. These include: re-imagining fact-checking to support credible
expression; developing incentive structures that elevate respectful and inclusive interactions; and
strengthening accountability through both transparent internal moderation and external regulatory
oversight. By emphasizing collaborative responsibility across platforms, user communities, and
regulators, we aim to advance a vision for social media environments where individuals are not
only protected from harm, but also actively encouraged to participate in meaningful and open
public discourse.
Proc. ACM Hum.-Comput. Interact., Vol. 10, No. 6, Article CSCW152. Publication date: October 2026.

Silence and Noise: Self-censorship and Opinion Expression on Social Media CSCW152:3
2 Related Work
2.1 Theoretical Motivations
Our study is grounded in a set of socio-psychological theories that explain how individuals form,
suppress, and express opinions in social contexts, particularly within online environments. We
use them to frame concrete behaviors that can be observed through self-reported discrepancies
between private beliefs and public expression.
Self-silencing theory.Self-silencing theory provides a framework for understanding restrained
opinion expression as a set of related outcomes shaped by social pressure and anticipated evaluation.
Within this broader landscape of social influence, self-silencing refers to the inclination to restrain
self-expression and action in order to protect social ties or avert anticipated retaliation, for example,
by suppressing one’s true opinions to preserve a positive public image [55]. Prior research documents
a “spiral of silence” in online contexts, where individuals refrain from speaking publicly about
polarizing issues when they perceive their views as misaligned with prevailing opinions [22, 41, 49,
86]. In this paper, we use the termself-censorshipto refer to these forms of restrained expression,
encompassing both complete silence and opinion conformity. A common response is the decision
to remain silent, where individuals choose not to express their views at all in response to perceived
social risk. Importantly, theories of social influence also describe situations in which expression is
not withheld but adjusted. Individuals may continue to participate while modifying the intensity of
their expressed views, leading to discrepancies between private beliefs and public expression. On
the other hand, opinion reinforcement refers to behaviors in which publicly expressed opinions
differ in intensity from an individual’s original position, often becoming more positive or negative
in sentiment [66]. Reinforcement and self-censorship can be understood as alternative responses
that are discussed within the same theoretical landscape of social evaluation and visibility, rather
than as mutually exclusive outcomes.
Social identity theory.Opinion expression on social media is inherently shaped by audience
context. While self-silencing theory is used to define the forms of restrained expression we examine,
social identity theory provides a lens for understanding the contextual factors associated with
these outcomes. Social identity theory suggests that individuals tend to understand themselves
and others in relation to social groups, and that group membership provides a powerful lens
through which opinions are interpreted and evaluated [87–89]. When a group identity becomes
prominent, individuals develop their self-concept around paradigmatic ingroup characteristics
[17]. They are motivated to differentiate between their ingroup and relevant outgroups [65]. In
online social communities, these dynamics shape how users anticipate audience reactions and
evaluate the social costs of expression, influencing their willingness to share opinions [ 47, 90].
Classic experimental and contemporary work further shows that perceived social approval and
disapproval can distort expressed opinions even when private beliefs remain unchanged [1, 5, 28].
Related phenomena such as pluralistic ignorance [ 3] and the enforcement of unpopular norms
[21, 99] illustrate how misperceptions of group consensus can further constrain public expression.
This perspective motivates the inclusion of perceived support as a key variable, capturing the extent
to which individuals perceive alignment with their audience, as well as community size, which
reflects the scale and heterogeneity of the audience in which these identity-based evaluations take
place. Prior work has shown that anticipated acceptance or rejection within one’s social group is
associated with decisions to withhold or modify expression [9, 19], while evidence on the role of
audience size in shaping self-censorship remains mixed [15, 27, 29, 62].
Self-presentation theory.Self-presentation is the behavior of conveying information about
oneself, driven by the motivation to align one’s self-display with the expectations and preferences of
the audience [12]. In this study, we draw on self-presentation theory to guide the qualitative analysis
Proc. ACM Hum.-Comput. Interact., Vol. 10, No. 6, Article CSCW152. Publication date: October 2026.

CSCW152:4 Wang et al.
of how individuals manage expression in social media contexts. This perspective helps interpret
patterns of expression management in relation to anticipated social evaluation. Originally, theories
of self-presentation were centered on in-person interactions, exploring how individuals perform
and project their self-image in face-to-face settings [46, 83]. However, as digital media, particularly
social media, have become increasingly integral to daily life, these traditional theories have evolved
and now encompass the nuances of self-presentation in digital formats, adapting to the dynamics of
online communication and identity expression [53]. The anchoring of an individual’s online identity
in their offline identity and physical space constrains the extent of highly controlled and selective
self-presentation online, as the varying degrees of anonymity provided by certain social media
platforms influence these dynamics [53]. Within this framework, discrepancies between private
beliefs and public expression can be understood as strategic adjustments that allow individuals to
maintain a favorable public image while managing potential social costs. In addition to self-initiated
factors, the environment in which individuals interact plays a significant role in shaping their
online behavior. Platform affordances, such as anonymity and the differing interaction dynamics
across social media platforms, influence self-presentation and the willingness of self-expression
[74]. These contextual conditions also shape how individuals interpret topic sensitivity; prior work
shows that perceived topic polarity is associated with variation in willingness to express opinions,
with more controversial topics corresponding to higher levels of hesitation and self-censorship
[36, 102]. Finally, behavioral engagement provides an additional lens for understanding expression
dynamics. Posting frequency reflects how often individuals participate in opinion expression and
has been linked to audience-related factors such as community size [80].
Rather than taking these theories as competing explanations, we suggest that they offer com-
plementary lenses for interpreting observable patterns in participants’ reported willingness to
express opinions on social media. Self-silencing theory defines the forms of restrained expression
we examine (complete silence vs. adjusted expression). Social identity theory helps explain when
these behaviors occur by highlighting the role of group context and perceived alignment. Self-
presentation theory guides our qualitative understanding of how individuals reason about and
manage these tensions. Table 1 summarizes how these theoretical perspectives inform the selection
of key variables used in our subsequent analyses.
Variable Type Variable Theoretical Grounding
Dependent Decision to remain silent This variable captures complete self-censorship, defined as the choice not to express an opinion publicly.
Self-silencing theory and the spiral of silence framework suggest that individuals are less likely to voice
their views when they perceive their opinion to be in the minority or anticipate negative social evaluation
[22, 41, 49, 86]. This outcome represents one endpoint of the continuum of restrained expression examined
in this study.
Dependent Discrepancy between pri-
vate and public opinions
This variable captures partial self-censorship in the form of opinion adjustment, where publicly expressed
views differ from privately held beliefs. Self-silencing theory conceptualizes such adjustments as strategies to
manage social risk while maintaining participation [55]. In parallel, self-presentation theory suggests that
individuals selectively modify expressed opinions to align with perceived audience expectations and maintain
a favorable public image [12, 46].
Independent Perceived polarity Prior work shows that perceived topic polarity is associated with variation in opinion expression and restraint,
with more controversial topics eliciting higher levels of hesitation and self-censorship [36, 102]. Section 4.2.1
further documents topic-dependent patterns of expression in this study.
Independent Perceived support This variable captures perceived social alignment within one’s audience. Work on self-silencing emphasizes
that anticipated acceptance or rejection by others is associated with decisions to withhold or modify expression
[9, 19].
Independent Community size This variable captures the scale of the potential audience for expression and reflects structural aspects of
audience context discussed in group identity theory [ 87–89]. Prior research offers mixed evidence on its
relationship with self-censorship behaviors [15, 27, 29, 62].
Mediator Posting frequency Prior work suggests that audience scale is associated with how frequently individuals engage in posting
behaviors [80].
Table 1. Model variables and theoretical rationale.
Proc. ACM Hum.-Comput. Interact., Vol. 10, No. 6, Article CSCW152. Publication date: October 2026.

Silence and Noise: Self-censorship and Opinion Expression on Social Media CSCW152:5
2.2 Opinion Dynamics on Social Media
Prior literature has posited a divergence between individuals’ publicly expressed positions and
privately held beliefs [59, 82]. This divergence can manifest as either exaggeration or suppression
of true opinions, influenced by social and individual factors [60, 69]. Research on opinion dynamics
in social media has emphasized the reinforcement of views through mechanisms such as echo
chambers and filter bubbles [10, 18, 48, 81]. These phenomena describe how users are increasingly
exposed to homogeneous viewpoints that reinforce their existing beliefs, either due to network
structure [11, 24, 39] or algorithmic design [14, 70]. These dynamics have often been associated
with increased political polarization and the reinforcement of partisan attitudes [7, 44, 52]. However,
this body of literature centers almost exclusively on vocal participation—the conversations users
choose to publicly share, amplify, or engage with—and often takes these conversations at face
value through content analysis. Such approaches overlook the ways individuals withhold their true
opinions, which can take the form of complete silence or the expression of a distorted version of
their views. This self-censorship—what is not said or not explicitly said—also plays a critical role in
shaping online opinion dynamics.
Recent studies have examined hesitation and restraint in online opinion expression. For example,
Gera et al. [42] surveyed college students and found that posting willingness varies by topic, and
these concerns are strong in politically diverse audiences, where anticipated social sanctions increase
reluctance to post [98]. Gibson et al. [ 43] found that nearly half of Americans self-censor their
opinions online, often in response to political polarization and fear of social repercussions. Other
studies have explored distinct underlying motivations. Warner et al. [96] emphasized privacy-related
factors such as perceived vulnerability and information control as key drivers of self-censorship
on social networking sites. Dubois et al. [33] further showed that belief in the political relevance
of social media consistently predicts self-censorship across several countries, while impression
management and exposure to hostile interaction have also been shown to encourage restraint in
online political discussions [57, 79]. Howe et al. [54] demonstrated that self-censorship can also serve
as a strategy for limiting the spread of misinformation, showing that prompting users to share only
content they believe is true significantly improves discernment. Together, these studies suggest that
self-censorship is a common and multifaceted behavior, shaped by a range of socio-psychological
and contextual factors. Our work contributes to the understanding of self-censorship by examining
how users navigate the tension between private beliefs and public expression, focusing on how
perceived social context and group dynamics are associated with what individuals choose to share,
and exploring the relationship between echo chambers and self-censorship.
3 Research Methods
3.1 Survey Study
We conducted a structured survey using Qualtrics, a platform widely utilized in academic research
for survey design and deployment [35].
3.1.1 Survey design.The survey included Likert-scale items, slider-scale items, and open-ended
questions. The survey was structured to measure contextual factors which prior literature has
suggested may impact opinion-sharing on social media. Demographic and social media usage
questions used in the study were adapted from existing work and slightly modified to suit the
research objectives [64]. An outline of the survey follows here, and the full survey is provided in
Appendix 1.
Demographic information.We collected demographic data through multiple-choice questions
on gender, age, race/ethnicity, education, and political identification, with a follow-up question for
independents to specify a party leaning.
Proc. ACM Hum.-Comput. Interact., Vol. 10, No. 6, Article CSCW152. Publication date: October 2026.

CSCW152:6 Wang et al.
Social media usage.In addition to general social media usage questions, we asked participants to
share, for example, how often they post and the size of their audience. These items operationalize
behavioral engagement and community size, which are central contextual dimensions in our
theoretical framing and subsequent models.
Opinion expression.We explored discrepancies between users’ public and private opinions, preva-
lence of self-censorship, and habits around opinion sharing on social media. The statement-based
items were designed to directly capture participants’ self-reported experiences of opinion restraint
and adjustment. In addition, we specifically assessed participants’ opinion-sharing behaviors with
respect to six topics: politics, social justice, health, environment, technology, and religion. We
asked participants to rate the polarity of each topic. The research team discussed and shortlisted
six topical domains that are commonly encountered on social media and that differ in perceived
polarity and public visibility. This selection provides a shared reference frame for participants while
allowing examination of opinion expression across domains with varying levels of controversy.
Topic-specific responses.We asked participants to share their private opinions on specific issues
related to each of the six focal topics, e.g., climate change (see Appendix 1 for list of issues). For each
topic, the research team selected a single, widely recognizable issue through majority agreement
to serve as a shared reference point, anchoring responses in a concrete context and reducing
ambiguity in interpretation. We measured their stance, perceived polarization, community support,
and reported posting behaviors for each.
Open-ended questions.Participants reflected on discrepancies between their public posts and
private beliefs with respect to our focal topics. We asked participants to discuss the frequency
and impact of such discrepancies. We asked them to describe specific posts they have shared and
compare those to their privately held beliefs. These questions were included to capture context and
reasoning that may not be well represented by closed-ended items.
3.1.2 Target sample size.We calculated target sample size by setting the confidence level at 95%,
margin of error at 5%, and using the estimated number of social media users in the U.S. in 2023
(302.35 million)1 as the target population size. This calculation resulted in a required sample size of
385. Accordingly, we collected 390 responses through Prolific.
3.1.3 Recruitment and compensation.Survey recruitment was managed through the crowd-sourcing
platform Prolific, which supports fine-grained population sampling and has been shown to generate
high-quality response data [32]. For inclusion in the study, participants were required to be located
in the United States, at least 18 years of age, and report using English as their primary language
of communication on social media platforms. Participant demographics are provided in Table A1
(see Appendix 3). Each participant was paid $4 upon approval, which meets the minimum wage
standard at $12/hr. In total, $2133.33 was spent for survey participant compensation (including
service fees).
3.1.4 Quality checks.We undertook two-stage verification for survey data. Responses were re-
quired to pass both an attention check [73] and manual verification of Qualtrics-flagged potential
bots. All 390 responses were concluded to be valid (see Appendix 3 for details about quality check
procedure).
3.1.5 Pilot study.A pilot version of the survey was conducted with 10 participants from Prolific.
They were asked to provide feedback on the clarity of question phrasing and the comprehensibility
of question framing after completing each section. Based on their responses, questions were
refined to enhance clarity. There is no overlap between these 10 and the 390 participants in the
1https://www.demandsage.com/social-media-users/
Proc. ACM Hum.-Comput. Interact., Vol. 10, No. 6, Article CSCW152. Publication date: October 2026.

Silence and Noise: Self-censorship and Opinion Expression on Social Media CSCW152:7
reported survey study. The pilot study also informed the selection of the final statements used to
measure opinion difference, conformity, and reinforcement. For each construct, an initial pool of
five candidate statements was included in the pilot survey to capture slightly different formulations
of the same underlying concept. Responses from the pilot were reviewed to assess whether the
statements were interpreted consistently, whether they elicited similar response patterns, and
whether any statements caused confusion or redundancy. Based on this review, three statements
per construct were selected for the main survey. These selected statements showed consistent
interpretation across participants, aligned closely with the intended theoretical constructs.
3.1.6 Statistical analyses.We employed several statistical methods to analyze the survey data.
To assess which type of discrepancy between individuals’ public and private opinions was more
commonly observed, we used the Wilcoxon signed-rank test with Holm correction for multiple
comparisons as the data are paired and not normally distributed. For the analysis of topic-specific
differences in opinion expression, we utilized the Spearman’s rank correlation [ 101]. We used
logistic regression with standard errors clustered at the participant level to evaluate the probability
of a participant choosing to remain silent, given that the dependent variable in this scenario
is binary [ 71]. For analyses with an ordinal dependent variable, we employed ordered logistic
regression with standard errors clustered at the participant level to examine the factors correlated
with discrepancies between public and private opinions [37]. We then conducted mediation analyses
for both models to investigate potential indirect associations [67].
3.1.7 Thematic analyses.Open-ended survey questions were coded using thematic analysis [ 16].
Two authors served as the primary coders and were responsible for the initial coding and iterative
refinement of the codebook. Both primary coders independently familiarized themselves with
the data and conducted open coding on an initial subset of responses to identify salient concepts.
Using the resulting codebook, they iteratively coded the full datasets, refined code definitions, and
organized codes into higher-level thematic categories. Intercoder reliability was assessed using
Cohen’s kappa, treating each category as a binary label. Because each item could be assigned
multiple determinants, kappa was computed separately for each category. Kappa values ranged
from 0.76 to 1.00 across categories, reflecting relatively high agreement. A third author acted in a
review and adjudication role. After the coding and theme development were completed, the third
author reviewed the codebook and thematic structure to assess consistency and coherence. Any
remaining minor discrepancies were discussed among the authors and resolved through consensus.
3.2 Participant Interviews
We conducted 20 semi-structured interviews with volunteers amongst the survey participants. All
interviews were carried out via Zoom. Length of interviews ranged from 19 to 35 minutes; the
majority were completed within 25 minutes. Interview questions are provided in Appendix 2.
The survey results established systematic patterns in self-censorship and opinion discrepancy,
describing how participants reported behaving across different community contexts. The interviews
were conducted to complement these findings by examining how and why participants arrived at
these decisions. In particular, the interviews allowed us to probe the reasoning processes underlying
observed survey patterns, clarify how participants interpreted key survey constructs, and investigate
tensions in the survey responses that could not be resolved through quantitative analysis alone.
This mixed-method design enabled us to connect aggregate patterns to individual sense making
around opinion expression.
Proc. ACM Hum.-Comput. Interact., Vol. 10, No. 6, Article CSCW152. Publication date: October 2026.

CSCW152:8 Wang et al.
Participant Gender Age Race/Ethnicity Education Political Orientation
p1 Transgender Female 18 to 24 White/Caucasian High school degree or equivalent Democrat
p2 DemiMan 25 to 34 White/Caucasian High school degree or equivalent Independent
p3 Male 35 to 44 White/Caucasian High school degree or equivalent Independent
p4 Male 45 to 54 Asian Associate degree Independent
p5 Female 25 to 34 White/Caucasian Graduate degree Republican
p6 Female 35 to 44 White/Caucasian Bachelor degree Democrat
p7 Female 45 to 54 White/Caucasian Bachelor degree Independent
p8 Female 18 to 24 Black/African American High school degree or equivalent Independent
p9 Female 35 to 44 White/Caucasian Graduate degree Republican
p10 Male Above 55 White/Caucasian Bachelor degree Democrat
p11 Male 25 to 34 Asian Bachelor degree Democrat
p12 Male 25 to 34 White/Caucasian Graduate degree Democrat
p13 Female Above 55 White/Caucasian Bachelor degree Democrat
p14 Male 45 to 54 White/Caucasian Bachelor degree Independent
p15 Male 25 to 34 White/Caucasian High school degree or equivalent Democrat
p16 Female 25 to 34 White/Caucasian Bachelor degree Democrat
p17 Female Above 55 Black/African American Bachelor degree Independent
p18 Male 35 to 44 White/Caucasian High school degree or equivalent Republican
p19 Male 45 to 54 White/Caucasian Attending College Democrat
p20 Female Above 55 White/Caucasian Associate degree Democrat
Table 2. Interview participant demographics.
3.2.1 Interview design.The semi-structured interviews were organized around five thematic areas.
Each theme was selected to deepen understanding of specific patterns or open questions that
emerged from the survey results.
Reasons for discrepancies between public and private opinions.Survey responses indicated
that some participants reported substantial gaps between their privately held beliefs and their
public expressions, while others reported little or no discrepancy. This interview section was
designed to understand how participants interpreted these discrepancies, the situations in which
they arose, and the reasoning participants used to justify expressing or withholding certain views.
For participants who reported no discrepancy, questions focused on why they perceived alignment
between private and public opinions and how they assessed the risks of expression.
Determinants of opinion sharing.Responses to the open-ended survey questions suggested
that participants considered additional, more nuanced factors influencing opinion sharing that
were not fully captured by the closed-ended measures. Interview questions in this section therefore
explored how participants weighed these considerations in practice and surfaced other influences
on expression decisions that were not fully captured in the survey.
Crafting a public image.Survey findings suggested that concerns about audience perception
and self-presentation were linked to both silence and opinion adjustment. This interview section
examined how participants thought about managing their public image on social media and how
identity considerations influenced expression decisions.
Influence of social media community.While the survey captured community context (e.g.,
perceived audience size and support) at a high level, this section was designed to unpack how
participants understood their community, how they inferred norms or expectations, and how
community characteristics factored into their anticipation of feedback or judgment.
Consequences and influence of social media dynamics.Finally, the survey raised questions
about reinforcement, conformity, and the broader consequences of opinion expression over time.
This section invited participants to reflect on perceived positive and negative outcomes of opinion
reinforcement and conformity, as well as how platform features and social dynamics shaped their
longer-term expression strategies.
Proc. ACM Hum.-Comput. Interact., Vol. 10, No. 6, Article CSCW152. Publication date: October 2026.

Silence and Noise: Self-censorship and Opinion Expression on Social Media CSCW152:9
3.2.2 Recruitment and compensation.At the end of the survey, all participants were given the
opportunity to sign up for a follow-up interview. The decision to invite survey participants to these
interviews, rather than sourcing independent participants, was made because their responses to
the survey’s open-ended questions enabled us to tailor our semi-structured interview questions
to probe more deeply into the reasons behind their responses. A total of 42 survey respondents
indicated interest in participating in a follow-up interview. From this pool, we used purposeful
sampling [75, 76] to select participants who reflected diversity in opinion expression patterns,
including individuals who reported consistent opinion sharing, selective silence, and some level of
discrepancies between private beliefs and public expression. We aimed to maintain a balanced repre-
sentation across these three categories (target ratio 1:1:1), and the final sample closely approximated
this distribution (7:7:6). Selection also considered the clarity and substantive depth of participants’
open-ended survey responses to ensure that interviewees could articulate their reasoning and
experiences in detail. For example, we excluded responses that were extremely short or lacked
explanation (e.g., one-word or single-sentence answers without justification), as these provided
limited insight into participants’ underlying reasoning. In contrast, participants who provided
more elaborate responses with clear justification or examples were prioritized for inclusion. Each
interview participant was paid $15 upon completion, which is higher than the minimum wage
standard. In total, $300 was used for interview participant compensation. Demographic information
for interview participants is provided in Table 2.
3.2.3 Thematic analyses.After conducting a quality check on the transcriptions automatically
generated by Zoom, we analyzed interview transcripts using a thematic analysis approach via Nvivo-
14 [16, 31]. Two authors served as the primary coders, with a third author involved in reviewing
and adjudicating the coding process. This collaborative and iterative approach is commonly used
in Human-Computer Interaction research [ 4, 100]. The analysis proceeded in multiple stages,
including familiarization, open coding, iterative refinement of a shared codebook, and theme
synthesis. Initially, the first author familiarized themselves with the data through in-depth reading
of the transcriptions. During the open coding phase, initial codes were identified from participants’
answers to the seed questions. These codes were grouped into potential themes relevant to the RQs.
Following the initial coding, two authors collaboratively discussed the meaning, similarities, and
differences among identified themes. They decided collectively to retain, remove, or reorganize these
themes. These were then synthesized into broader themes that could represent patterns of opinion
expression more comprehensively. Using this preliminary codebook, subsequent transcripts were
coded iteratively. The research team held regular meetings to review coding decisions, clarify code
definitions, and group related codes into higher-level categories. Disagreements were discussed
among the coders until consensus was reached, and the codebook was refined throughout this
process. After the primary coding and theme development were completed, a third author reviewed
the existing codes, codebook, and thematic groupings to support the quality and coherence of
the analysis. Any remaining minor discrepancies were discussed among the authors and resolved
through consensus. The first and second authors served as the primary coders, while the third
author acted in a review and adjudication role, focusing on code consistency and thematic coherence
rather than independent recoding of all transcripts. All authors reviewed the resulting thematic
structure and supporting excerpts. This iterative process resulted in a set of thematic clusters that
form the basis of the qualitative findings reported in the paper.
3.2.4 Effective sample size.Thematic saturation refers to the point in qualitative analysis at which
additional data no longer yield substantively new themes [51]. In this study, interviews and analysis
proceeded iteratively, and a total of 20 interviews were conducted. At this point in the coding
process, no substantively new themes emerged.
Proc. ACM Hum.-Comput. Interact., Vol. 10, No. 6, Article CSCW152. Publication date: October 2026.

CSCW152:10 Wang et al.
3.3 Response Bias Control
To reduce the likelihood that Prolific participants could infer the study’s intent and adjust their
responses accordingly, we implemented several safeguards during recruitment and data collection.
The study description and materials were presented with neutral framing (e.g., the title and objec-
tives used “Understanding the patterns of opinion expression on social media platforms”), which
did not disclose the underlying hypotheses. In addition, interview questions were deliberately
structured to be asked in both directions (for example, addressing both potential positive and
negative consequences of different opinion expression patterns, as shown in the Appendix). This
approach reduced the likelihood that participants would modify their responses to align with
perceived expectations of the researchers.
4 Results
We present results in three parts, corresponding to our research questions. We first examine (R1)
whether there is a discrepancy between privately held beliefs and publicly expressed opinions on
social media. We then analyze (R2) how contextual factors, including topic, perceived community,
and posting behavior, are associated with users’ willingness to share opinions across different
topics. Finally, we report qualitative findings and design implications based on (R3) users’ perceived
consequences of self-censorship and reinforcement.
4.1 RQ1: Public vs. Private Opinions
This subsection addresses RQ1, examining whether and to what extent individuals exhibit discrep-
ancies between their privately held beliefs and publicly expressed opinions on social media. As
noted above, a series of survey questions were designed to measure: reported differences between
users’ public and private opinions on a variety of topics; users’ tendencies toward conformity and
self-censorship; and, users’ tendencies toward reinforcement. These questions employed a 7-point
Likert scale measuring participants’ agreement (ranging from “strongly disagree” to “strongly
agree”) with a series of statements. The calculated mean of the responses within each set yielded
an agreement score for each participant, with potential values extending from -3 to 3.
Response distributions and their corresponding Wilcoxon test p-values are shown in Figure 1.
Participants confirmed that there exists a discrepancy between their privately held beliefs and
publicly expressed opinions. They also agreed, on average, that they feel an inclination to conform
when expressing their public opinions. A minority of participants (29.23%) report amplifying their
true opinions on social media platforms.
4.2 RQ2: Contextual Influences on Opinion Expression
To address RQ2, we systematically explore context along multiple axes. Our analyses are structured
into three parts. The first explores relationships between topics of conversation and participants’
willingness to share their opinions on social media. Second, we model the effects of various indi-
vidual and community-level features on opinion expression, including users’ perceived community
support and community size. Finally, we extract additional contextual factors raised by partici-
pants during open-ended survey questions and interviews to construct a holistic understanding of
influences on opinion expression.
4.2.1 Categories and polarities of topics.We asked survey participants to rate the polarity of our
six focal topics on a 5-point Likert scale. Likewise, we asked them to rate their willingness to
post their true opinions about each topic on social media. As the data is discrete and ordered, we
performed Spearman rank-order correlation to quantify the relationship between topic polarity
and opinion expression (see Table 3). We observe that for less polarizing topics, such as technology,
Proc. ACM Hum.-Comput. Interact., Vol. 10, No. 6, Article CSCW152. Publication date: October 2026.

Silence and Noise: Self-censorship and Opinion Expression on Social Media CSCW152:11
Fig. 1. Participants’ agreement with statements intended to capture:discrepanciesbetween private and public
opinion; the extent to which participants experienceconformityor self-censorship; and,reinforcementof
their opinions within public social media discourse. An exemplar statement is provided for each of the three
categories. The reported statistics are an average of three similar statements within the survey (seeOpinion
Expressionin Appendix 1: Survey Instrument). (SD: Strongly Disagree, D: Disagree, SWD: Somewhat Disagree,
N: Neither Agree Nor Disagree, SWA: Somewhat Agree, A: Agree, SA: Strongly Agree, p-value: p-value from
Wilcoxon test.)
Topic𝜌P-value 95% CI
Politics 0.16<0.01 ∗∗ [0.06, 0.25]
Social Justice 0.16<0.01 ∗∗ [0.06, 0.25]
Health 0.18<0.001 ∗∗∗ [0.08, 0.28]
Environment 0.28<0.001 ∗∗∗ [0.19, 0.37]
Technology 0.25<0.001 ∗∗∗ [0.16, 0.34]
Religion 0.31<0.001 ∗∗∗ [0.22, 0.40]
Table 3. Topic-wise Spearman correlations between polarization and opinion expression, with p-values and
confidence intervals.
environment, health, and religion, the correlation between opinion expression and perceived
polarization is significantly positive. That is, people are more likely to engage in discussions that
are perceived as more controversial. This effect is diluted in discussions of politics and social justice
as many participants are less willing to express their true opinions due to the high level of perceived
topic polarity (see Figure 2). Specifically, we observe a greater concentration of high polarization
and low opinion expression scores, particularly evident in the bottom right corner, for topics related
to social justice and politics. When plotting average polarization vs. opinion expression across all
six topics (see Figure 2, right), a consistent pattern emerges: topics perceived as more polarizing
by the public demonstrate a lower overall opinion expression and higher levels of conformity.
The contrast between the within-topic and between-topic patterns suggests that the relationship
between perceived polarization and willingness of opinion expression is non-monotonic and
context-dependent: within less sensitive topics, perceived polarization may stimulate engagement;
however, for topics that are already highly divisive, a substantial portion of individuals choose to
suppress expression, potentially due to heightened conformity pressures.
Thematic analysis of the open-ended survey questions (see Table A3 in the Appendix) and
interviews supported these findings. Responses to the open-ended questions frequently referenced
topics and subtopics that aligned with the six topical categories used in our analysis, indicating
Proc. ACM Hum.-Comput. Interact., Vol. 10, No. 6, Article CSCW152. Publication date: October 2026.

CSCW152:12 Wang et al.
Fig. 2. Perceived polarization and willingness to express true opinion, by topic (Pol=Polarization, OE=Opinion
Expression).
that these categories capture a broad range of situations in which self-censorship and opinion
conformity arise. Several participants explicitly stated their reluctance to engage with polarizing
topics on social media.
I have been really hesitant to post at all about Palestine because it is so incredibly polarizing
and people seem angry on both sides if you post. I am afraid of being called antisemitic
for supporting Palestine. I have been posting more mild versions of my opinion instead of
calling for a ceasefire.–Survey participant
4.2.2 Variable operationalization.To examine how community context shapes self-censorship,
we constructed two regression models.Model 1examines the decision to remain silent (binary
outcome), whileModel 2examines opinion discrepancy among those who chose to post (ordinal
outcome). Both models use the same independent variables but capture different aspects of self-
censorship. The two dependent variables correspond to distinct stages of opinion expression:
the decision to speak and the degree of adjustment in expressed opinions. Table 4 summarizes
all variables and their operationalization 2. The selection of the target variables is theoretically
grounded and introduced in Section 2.1.
2Because our data are observational and cross-sectional, all estimated relationships, including those involving independent
variables, mediators, and interaction terms, are interpreted as associational patterns rather than as causal effects. References
to direct or indirect effects reflect statistical decomposition of associations rather than causal transmission.
Proc. ACM Hum.-Comput. Interact., Vol. 10, No. 6, Article CSCW152. Publication date: October 2026.

Silence and Noise: Self-censorship and Opinion Expression on Social Media CSCW152:13
Variable Type Variable Operationalization
Dependent Decision to remain silent Binary indicator of whether a participant reports willingness to share an opinion on a given topic (1 = silent,
0 = expresses opinion). This outcome is constructed from survey responses to topic-specific questions asking
about intention to post.
Dependent Opinion discrepancy Ordinal measure of the difference between privately held beliefs and publicly expressed opinions among
participants who report willingness to post. Both are measured on a 7-point Likert scale and recoded to the
range [-3, 3]. Discrepancy is computed as|True Opinion|−|Public Expression|.
Independent Perceived polarity Participant-rated topic controversy (5-point scale). Section 4.2.1 further documents topic-dependent patterns
of expression in this study.
Independent Perceived support Percentage of connections perceived to share the participant’s view.
Independent Community size Self-reported total number of connections on primary platform.
Mediator Posting frequency Self-reported posting frequency. Empirically, posting frequency shows a moderate correlation with community
size (0.35) (Tables A2 and A4), indicating that posting frequency is meaningfully related to audience scale.
Control Topic Six predefined topic categories are included to adjust for topic-specific differences in sensitivity and baseline
expression patterns that may confound associations between contextual variables and outcomes.
Control Political ideology Democrat / Republican / Neutral. Political ideology is included to adjust for observed imbalance in participant
distribution and to account for baseline differences in opinion expression associated with partisan orientation.
Interaction Topic×Polarity Interaction term capturing topic-dependent effects. This interaction captures topic-dependent variation in
the association between perceived polarity and opinion expression. As shown in Section 4.2.1, higher polarity
is associated with increased engagement for some topics and reduced expression for others.
Table 4. Model variables, operationalization, and theoretical rationale. The correlation matrices (see Table A2
and A4 in Appendix 3) show that all three independent variables have correlation coefficients lower than 0.1,
suggesting that the three dimensions capture non-redundant information. Variance Inflation Factor (VIF)
values were low (shown in Table A5 in Appendix 3, all <5), indicating no significant multicollinearity among
the independent variables.
Variable Coef. Std. Err. z P>|𝑧|95% CI Odds Ratio
Support -0.39 0.08 -5.19<0.001 ∗∗∗ [-0.53, -0.24] 0.68
Polarization -0.16 0.21 -0.78 0.43 [-0.57, 0.24] 0.85
Posting Frequency -0.54 0.23 -2.31 0.02* [-0.99, -0.08] 0.58
Community Size 0.19 0.09 2.04 0.04* [ 0.01, 0.37] 1.21
Topic: Health 0.18 0.20 0.87 0.39 [-0.22, 0.57] 1.19
Topic: Politics 0.00 0.25 0.01 0.99 [-0.49, 0.49] 1.00
Topic: Religion 0.10 0.19 0.54 0.59 [-0.27, 0.48] 1.11
Topic: Social Justice 0.11 0.20 0.54 0.59 [-0.28, 0.49] 1.11
Topic: Technology 0.06 0.17 0.34 0.73 [-0.27, 0.38] 1.06
Democrat (vs. Neutral) 0.37 0.35 1.05 0.29 [-0.32, 1.06] 1.45
Republican (vs. Neutral) 0.35 0.35 0.99 0.32 [-0.34, 1.04] 1.42
Polarization×Health 0.24 0.24 1.00 0.32 [-0.23, 0.71] 1.27
Polarization×Politics 0.56 0.30 1.88 0.06 [-0.02, 1.15] 1.76
Polarization×Religion 0.19 0.23 0.85 0.40 [-0.25, 0.63] 1.21
Polarization× Social Justice 0.16 0.24 0.66 0.51 [-0.31, 0.62] 1.17
Polarization×Technology 0.09 0.16 0.57 0.57 [-0.22, 0.40] 1.09
Table 5. Logistic regression results predicting self-censorship (Model 1; 𝑛= 2170). Odds ratios are reported to
indicate effect sizes, alongside coefficients, clustered standard errors, and 95% confidence intervals.
4.2.3 Model 1: Impacts of community factors on self-censorship.We employ logistic regression
on 2,170 out of 2,340 (6x390) valid survey responses to questions asking participants about their
intention to share an opinion on a variety of topics. The dependent variable is defined as a binary
indicator of whether a participant remains silent or expresses an opinion, as summarized in Table 4.
Our analysis reveals that both perceived community support and posting frequency are negatively
correlated with the decision to remain silent (Table 5). This suggests that social media users are
more inclined to remain silent if they perceive a lack of support within their community or if they
are infrequent users. Conversely, community size is positively associated with silence, indicating
Proc. ACM Hum.-Comput. Interact., Vol. 10, No. 6, Article CSCW152. Publication date: October 2026.

CSCW152:14 Wang et al.
that users who believe they are exposed to a larger audience are more likely to refrain from
expressing their opinion, possibly due to increased concerns about social judgment or backlash,
consistent with self-silencing theory. We also observe a marginally significant interaction between
perceived polarization and the topic of politics, indicating that polarization may have a stronger
effect on self-censorship when the topic is political. This suggests that the relationship between
perceived polarization and willingness to express opinions could potentially be context-dependent
and intensified in political discussions.
To further examine this relationship, we conducted a mediation analysis to test the indirect
pathway from community size to posting frequency, and subsequently to the decision to remain
silent (Table A6 in Appendix 3). We found that larger community size is positively associated with
more frequent posting (path coefficient = 0.33, 95% CI = [0.29, 0.45]), and that posting frequency
significantly reduces the likelihood of remaining silent (path coefficient = –0.53, 95% CI = [–0.98,
–0.07]). This results in a significant negative indirect effect (–0.18, 95% CI = [–0.22, –0.04]), indicating
that increased posting partially offsets the silencing effect of larger audiences. At the same time,
the direct effect of community size on self-censorship remains positive and significant (0.19, 95%
CI = [0.03, 0.38]), consistent with the main model. These findings indicate that community size is
associated with self-censorship both directly and through changes in posting frequency.
4.2.4 Model 2: Discrepancies amongst expressed opinions.Our second analysis examines associ-
ations between the set of factors listed in Table 4 and differences between privately held true
beliefs and publicly expressed opinions, focusing on expression outcomes among participants who
report willingness to share. The operationalization of this dependent variable is summarized in
Table 4. Disparity y is calculated as: Disparity(𝑦)= |True Opinion|−|Public Expression|, where
both quantities are measured on a 7-point Likert scale and recoded to the range [-3, 3]. The use of
absolute values ensures that any reduction in the strength of opinion—regardless of positive or
negative view—is treated as positive disparity. That is, whether a participant moderates a strong
view (e.g., True:-3; Public: -1) or reinforces a weak view (e.g., True:-1; Public: -3), the disparity
reflects the magnitude and direction of the change. Importantly, our design intentionally restricts
directional reversals between private and public opinions (cases where the private and public
opinions are completely opposed) to ensure that disparity reflects changes in intensity, not strategic
misrepresentation or deliberate opinion reversal, as these fall outside the conceptual scope of
opinion conformity and reinforcement.
We have 1,627 out of 2,340 (6x390) valid responses from participants reporting willingness to
share their opinion on a particular topic. We employed ordinal logistic regression with standard
errors clustered at the participant level and the result is shown in Table 6. We note that a larger
absolute value in the discrepancy signifies a greater divergence between private belief and public
expression.
We find a negative association between perceived support and the predicted probability of opinion
discrepancy, with lower perceived support corresponding to greater discrepancy. Mediation analysis
(Table A7, Appendix 3) provides further insight: while the direct effect of community size is not
statistically significant, the indirect effect through posting frequency is negative and significant
(–0.03, 95% CI = [–0.08, -0.00]). This indicate a weak indirect relationship in which posting frequency
links community size to differences between private beliefs and public expression.
Taken together, findings from Model 1 and Model 2 address two related aspects of opinion
expression. First, social media users in larger online communities, with lower perceived support
and lower posting frequency, are more likely to remain silent. Mediation analysis shows this
effect operates both directly and through posting frequency. Second, among users who do express
opinions, lower perceived support is associated with greater discrepancies between private beliefs
Proc. ACM Hum.-Comput. Interact., Vol. 10, No. 6, Article CSCW152. Publication date: October 2026.

Silence and Noise: Self-censorship and Opinion Expression on Social Media CSCW152:15
Variable Coef. Std. Err. z P>|𝑧|95% CI Odds Ratio
Support -0.13 0.06 -2.06 0.04* [-0.25, -0.01] 0.88
Polarization 0.01 0.13 0.08 0.93 [-0.24, 0.26] 1.01
Posting Frequency -0.02 0.06 -0.37 0.71 [-0.15, 0.10] 0.98
Community Size 0.09 0.05 1.70 0.09 [-0.01, 0.19] 1.09
Topic: Health 0.04 0.18 0.24 0.81 [-0.30, 0.39] 1.04
Topic: Politics 0.03 0.24 0.10 0.92 [-0.44, 0.50] 1.03
Topic: Religion -0.05 0.17 -0.27 0.79 [-0.39, 0.29] 0.96
Topic: Social Justice -0.07 0.22 -0.33 0.74 [-0.49, 0.35] 0.93
Topic: Technology -0.06 0.15 -0.41 0.68 [-0.36, 0.24] 0.94
Democrat (vs. Neutral) -0.01 0.20 -0.07 0.94 [-0.41, 0.38] 0.99
Republican (vs. Neutral) 0.05 0.20 0.26 0.80 [-0.34, 0.45] 1.05
Polarization×Health 0.07 0.18 0.36 0.72 [-0.29, 0.43] 1.07
Polarization×Politics 0.10 0.26 0.39 0.70 [-0.40, 0.60] 1.10
Polarization×Religion 0.01 0.19 0.04 0.97 [-0.37, 0.38] 1.01
Polarization× Social Justice -0.02 0.23 -0.10 0.92 [-0.47, 0.43] 0.98
Polarization×Technology -0.05 0.15 -0.32 0.75 [-0.34, 0.24] 0.95
Table 6. Ordered logistic regression results predicting the degree of opinion expression discrepancy (Model 2;
𝑛= 1627). Odds ratios are reported to indicate effect sizes, alongside coefficients, clustered standard errors,
and 95% confidence intervals.
Category Subcategory Count Percentage
Topic and Polarity — 27 6.9%
Self-presentation Desire for acceptance (59); Avoiding Conflict (27);
Career Constraint (9); Credibility (5)
100 25.6%
Evidence Support — 19 4.9%
Platform Affordance — 4 1.0%
Social Influence — 15 3.8%
None No Disparity or Posts (171); No Reason Given (64) 235 60.3%
Table 7. Determinants of opinion expression for survey respondents (from open-ended questions). Note: Total
percentage exceeds 100% as responses could reference multiple determinants.
and public expression, suggesting adjustment to align with perceived group norms or maintain
social cohesion.
4.2.5 Additional determinants of opinion expression.While our models captured structural predic-
tors that are quantifiable, participants also described additional factors influencing their willingness
to express opinions—many of which may function as latent confounders. We further qualitatively
identify and discuss key determinants of opinion expression from open-ended survey questions
(see Table 7) and interview responses.
Self-presentation.Social media users often engage in intentional and unintentional curation of
their online personas through their choices about what to post and what not to post. This curation is
driven by an awareness of how their self-image is perceived on social media, which acts as a barrier
to full disclosure of their real identities. Users are conscious of the balance between authenticity
Proc. ACM Hum.-Comput. Interact., Vol. 10, No. 6, Article CSCW152. Publication date: October 2026.

CSCW152:16 Wang et al.
and the need to maintain a certain image that aligns with their self-perception or the expectations
of their communities.
I was worried about how people who think they know me will perceive me based on certain
opinions.–P14
I just don’t want to be coming off as somebody that shoots out their mouth without thinking
about how it’s gonna affect other people.–P20
Self-presentation is influenced by many factors including: fear of judgment or isolation (11 out of
20 participants); desire for acceptance (P06, P07); inherent cultural identities (P11,P20); and potential
social repercussions that might follow from sharing true opinions (P04, P10, P12). Furthermore, the
decision by some social media users to amplify or authentically express their opinions, regardless
of external perceptions, can stem from a conscious awareness of their self-image. For instance,
these individuals may seek to present themselves as: challengers of superiority complexes (P18);
proponents of authenticity (P17); supporters of minority groups (P02, P14); and as advocates intent
on making their voices heard (P02).
We also observe that maintaining a coherent self-image can drive seemingly opposite actions. In
some instances, the act of expressing extreme views can be a form of conformity to community
norms. For instance, one participant shared that he posted strong stances on the Black Lives
Matter movement because his social circle expected it of him. To maintain a positive image within
the community, he felt compelled to present himself as a vocal supporter, despite not holding
strong personal opinions on the issue. Reflecting conformity through extremism arises from the
fundamental desire for social acceptance and identity management.
Evidence support.The accuracy and truthfulness of information significantly influence partici-
pants’ willingness to share opinions. For example,
If I say something has happened, I make sure it’s factual. I don’t like propaganda, lies or
misinformation.–P13
This reflects a broader concern about the integrity of information shared online and a personal
commitment to contribute positively by ensuring the authenticity of shared content. These attitudes
appear to be a deliberate effort to combat the spread of false information, emphasizing a possibly
proactive approach to fostering a healthier environment.
Platform norms and affordances.The nature of a platform fundamentally shapes users’ willing-
ness of opinion expression. We observe that social media users’ willingness to express opinions is
platform-dependent due to differences in audience composition, community norms, and platform-
specific cultures.
I’m not reluctant to express an opinion in general, just on social media. The platform is
the key variable.–Survey participant
For instance, platforms like LinkedIn were described as spaces where expressing personal beliefs
could risk professional consequences:
I use mainly Linkedin and I would not want anyone to see my personal beliefs or thoughts
because that could have a negative impact on my ability to be hired or how future employers
or current coworkers view me.–Survey participant
In contrast, platforms that are built upon weak identity ties, such as Reddit, were described as
more flexible spaces for expression.
If I were more anonymous I would probably engage more, at least on Reddit.–P01
Restrictions and moderation on social media platforms also shape user expression. Concerns
about being “punished” for saying certain words reflect growing user awareness and dissatisfaction
with the perceived overreach of platform moderation policies.
Proc. ACM Hum.-Comput. Interact., Vol. 10, No. 6, Article CSCW152. Publication date: October 2026.

Silence and Noise: Self-censorship and Opinion Expression on Social Media CSCW152:17
I noticed it on YouTube. People have shown that they can’t say certain words, or they get
punished for it. And to me, it seems like we’re going towards that type of society where
you can’t say what you feel.–P17
Affordances for anonymity can also encourage users to express themselves more freely, par-
ticularly about sensitive topics. However, they also raise questions about accountability in civil
discourse, as users may engage in behavior they would avoid using their real identities.
That’s why people like Reddit so much, you post anonymously...There are things that you
wouldn’t really be comfortable sharing, because, you have that level of anonymity on
there.–P15
Social influence.Participants report sharing their opinions when they believe it might make a
positive difference in some way. For example, the fear of misinformation spreading unchecked on
social media platforms motivates some users to speak out.
If I didn’t say that then I would be afraid that other people who come across this comment
might think that it’s true. Especially on the Internet, we’re so used to seeing false infor-
mation. So even if I had a polarizing point of view, I would say it simply for educational
purposes.–P08
I don’t exaggerate my ability to influence the world. But it’s like the famous Indian saying,
ripple in the pond starts with one rock in the middle, and it expands out so you don’t know
what that ripple might do.–P13
Conversely, some participants believe that not engaging is the best strategy when comments or
discussions are not likely to be constructive or change the situation.
Engaging in said conversation or behavior wouldn’t change anything at all, and it could
just keep the ball rolling. The easiest way to get it to stop is not even acknowledging it.
–P18
Cultural and societal identity.This connection between personal identity and online behavior
underscores the deeply personal nature of social media interactions, where users select and prioritize
issues that reflect and affect their own lives and those of their communities.
I think the more personal to me will make me more willing to share it. So something that
affects my identity and the identity of the people that I follow. So religion is a very personal
one, that’ll affect me nationality and my ethnic origin.–P11
4.3 RQ3: Consequences and Possible Interventions
Building on our examination of the determinants of opinion sharing, this section explores users’
perceptions of social media and its wide range of negative consequences. We discuss potential
actions to improve the design of social media systems, mitigate these negative effects, and promote
healthier digital environments.
4.3.1 Consequences of conformity.Although the majority of participants reported experiencing
conformity when sharing opinions on social media, they also noted the inherent challenge of
observing this behavior in others.
I see lots of extremism. If someone is moderating their opinion, I wouldn’t really know it,
because they’re posting something that I’ll take at face value.–P09
Nonetheless, participants acknowledged the negative effects of conformity. Through thematic
analysis, we categorized users’ reported consequences into user-level, community-level, and society-
level impacts. The corresponding summary of the consequences from survey open-ended questions
is shown in Table 8.
Proc. ACM Hum.-Comput. Interact., Vol. 10, No. 6, Article CSCW152. Publication date: October 2026.

CSCW152:18 Wang et al.
Category Count Percentage
No Negative Consequences 111 28.5%
Personal Discomfort 98 25.1%
Suppression of Rational Discourse 88 22.6%
Unintended Encouragement of Extremism 29 7.4%
Blank or N/A 44 11.3%
Depends/Maybe 26 6.7%
Table 8. Consequences of disparity for survey respondents (from open-ended questions). Note: Total percent-
age exceeds 100% as responses could reference multiple consequences.
Personal discomfort.One participant highlighted an often overlooked yet significant effect of
conformity on individual social media users. This effect is described by the psychological theory of
cognitive dissonance, which refers to the discomfort that arises when one’s actions conflict with
their beliefs [6].
...there might be some cognitive dissonance from pretending you’re going along with
something if you don’t. Again, this is online. It’s not like if someone knocked on your door
and said, ‘Here’s a gun. What do you think?’ where you might speak the truth.–P09
Suppression of rational discourse.Conformity in social media discussions can lead to the domi-
nance of one viewpoint, effectively silencing alternative perspectives. This suppression reduces
opportunities for back-and-forth discussions that are essential for generating reasoned arguments
and fostering rational debate on various topics. As a result, the overall quality of discourse dimin-
ishes.
The internet will have less reasonable people, because more reasonable people will feel like
’I can’t express myself’, and so they’ll slowly stop posting.–P08
It’s one less voice towards a cause that matters. That voice might have an impact or might
not have an impact, but you won’t know. And at the end of the day you will have to live
with the fact that you didn’t speak out for others when it was needed.–P11
Unintended encouragement of extremism.Many participants expressed concern that confor-
mity may unintentionally foster extremism by not actively opposing harmful content. This passive
acceptance creates an environment where extreme views can flourish unchecked and silence can
be interpreted as endorsement.
Silence is violence. If you’re not speaking up against something, you’re just as complicit as
the person committing the act.–P02
You’re not voicing your side, and it could cause them to believe whatever they want, or
even possibly causes them to do something more extreme to get more attention.–P18
4.3.2 Actions to reduce conformity.Participants identified several actions for content promotion and
moderation systems on social media platforms, aiming to address conformity and self-censorship
and support a more open and constructive online environment. These strategies aim to mitigate
the influence of pressures towards conformity and promote healthier engagement among users.
Fact-checking to support evidence-based expression.As observed, individuals prone to con-
formity are more likely to post when they have data or news to support their claims. While many
social media platforms have introduced fact-checking features—such as labeling disputed content,
linking to credible sources, or flagging misinformation—these practices have shown mixed results
[25, 94]. Nonetheless, participants highlighted the potential of well-implemented fact-checking
systems to reduce conflict and boost users’ confidence in posting truthful content.
Proc. ACM Hum.-Comput. Interact., Vol. 10, No. 6, Article CSCW152. Publication date: October 2026.

Silence and Noise: Self-censorship and Opinion Expression on Social Media CSCW152:19
At some point they started doing fact checking when people were posting stuff, and there
would be alerts like ‘no, you can’t post that because it’s not factual’... And if I can post
something in it and it’s proven to be factually based, I’m probably a lot more likely to post
it. –P16
These reflections suggest that enhancing the visibility, transparency, and responsiveness of
built-in or external fact-checking mechanisms could empower users to participate more actively
and reduce hesitation driven by fear of spreading misinformation or being challenged unfairly.
Providing incentives for healthy interactions.Efforts to design moderation systems often
focus on demoting extremism [26, 38, 63], but less attention is given to incentivizing users who
engage in reasonable and productive conversations. Participants highlighted the importance of
addressing the conformity effect by implementing targeted incentives.
I think they could offer more incentives, and they should have more specified rules and take
serious actions against people who do these type of things instead of promoting discussion
boards where people are attacking others and making it go viral... I think that would do
good for social media and make people more comfortable.–P08
Fair interventions to counteract extremism.Many participants indicated that a reason for
their self-censorship is the highly polarized environment and the need to protect themselves from
extremism. This situation is exacerbated by the lack of consequences for extreme behaviors online,
and such extremism often leads to greater monetization [8].
They’re refraining from talking about sensitive subjects because of the extreme thoughts.
They’re in the vileness of how people handle online interactions because there are no
consequences online. People can say whatever, they know they can walk away clean from
it.–P15
It draws attention...They get a lot of interaction in their post, and if they’re monetizing,
the more clicks they get, the more money they can make.–P13
Addressing this issue by counteracting the reinforcement of extreme opinions could, in turn, help
alleviate the need for self-censorship (P09).
I think accountability prevents hate speech. You can also have more of a conversation.
–P11
Moreover, the problem extends beyond platform self-regulation, as some platforms inherently
encourage extreme content due to monetization incentives. Participants explicitly pointed out the
need for external regulatory oversight:
I think there should be more regulation of big tech in general. Because the reality of it is
that I think it’s done a lot of things to our society that are not good, and quite honestly
begging them to be nice about it hasn’t really worked so at some point somebody else has
to step in and do it.–P10
These insights underscore that addressing online extremism effectively requires a balanced
approach combining robust internal moderation mechanisms with external regulatory frameworks
to ensure accountability and reduce incentives for polarizing content.
Promoting free speech with platform–community collaboration.To further encourage user
participation and mitigate the spiral of silence, platforms should reconsider their policies and
mission statements to explicitly advocate for open dialogue and inclusivity. Clearly articulated
commitments such as declarations emphasizing the welcome of diverse viewpoints can reassure
users about their freedom to communicate openly. Additionally, refining moderation practices
by providing greater transparency around user bans or topic restrictions could build trust and
encourage users to express their opinions more freely.
Proc. ACM Hum.-Comput. Interact., Vol. 10, No. 6, Article CSCW152. Publication date: October 2026.

CSCW152:20 Wang et al.
We allow everyone to talk, but maybe then loosening how they might ban people or ban
topics like on Reddit, or just being more upfront with saying, hey, we’re inclusive. Go ahead
and talk about whatever you want to talk about here. So then people can open up.–P12
However, promoting free speech effectively involves more than modifying platform-level policies;
community dynamics also play a significant role. Another participant emphasized:
I think it’s more about the community than the platform. And I don’t think everyone has
to have an opinion on every issue. But I feel like some issues are more pressing than others
and maybe if there was a way for a platform to make it easier for people to express their
opinions, then that’d be cool.–P11
This perspective underscores the necessity for platforms and communities to work together
to foster user engagement. Platforms could support this collaboration through targeted design
features, such as dedicated spaces or prompts that highlight critical societal topics.
4.3.3 Consequences of reinforcement.While conformity pressures limit users’ ability to express
genuine opinions openly, reinforcement further intensifies these dynamics by amplifying homoge-
neous perspectives and silencing opposite voices. Participants highlighted critical consequences
that arise from these reinforcement effects, including echo chambers and incitement to harm, that
indirectly promote conformity and intensify the negative impacts previously identified.
Echo chambers and polarized groups.The most frequently mentioned consequence of reinforce-
ment is the creation and maintenance of echo chambers. Such echo chambers isolate individuals
within homogeneous communities, significantly narrowing their exposure to diverse perspec-
tives and reinforcing polarized and often biased beliefs [24]. Participants noted that this not only
diminishes critical thinking but also amplifies societal division.
The bad thing is that people will get a false sense of reality. So if your entire school com-
munity, teachers, and family—if everybody thinks the same way, you have no connection
to reality because you’re living in an echo chamber. ... It is bad for objective reality because
it is harder to understand the points of view of people who disagree with you.–P09
Incitement to harm and violence.Reinforcement of extreme views can also lead to increased
potential for real-world harm, including misinformation and aggressive behaviors. Participants
stressed that continuous affirmation of extremist or harmful opinions on social media can normalize
aggressive attitudes, which might manifest in offline violence or harmful actions.
Because when you’re hiding behind a screen, you don’t know how something you said
is going to affect somebody else. You don’t know what’s going on in their life. What if
their comment is the thing that drove them over the edge, whether it’s suicide, or doing
something crazy like shooting up a school.–P06
Such harmful behaviors and attitudes reinforce conformity indirectly, by creating a hostile
environment where users fear backlash or aggressive responses if they disagree or challenge the
majority view, further limiting open expression and increasing users’ likelihood of self-censoring.
One of the rules I kind of made after those experiences was to refrain from commenting on
people that are less close to me unless I absolutely know them well.–P10
4.3.4 Actions to avoid reinforcement.Participants repeatedly acknowledged a significant interplay
between reinforcement and conformity: the stronger the reinforcement of dominant views, the
stronger the pressure to conform and the less space for rational, diverse discussions. In response to
the intertwined challenges of conformity and reinforcement, participants recommended several
actions to mitigate reinforcement effects that extend upon the efforts previously described for
reducing conformity.
Proc. ACM Hum.-Comput. Interact., Vol. 10, No. 6, Article CSCW152. Publication date: October 2026.

Silence and Noise: Self-censorship and Opinion Expression on Social Media CSCW152:21
Exposure to diverse opinions.A commonly suggested approach involves algorithmically ensuring
exposure to diverse viewpoints to help users step outside their echo chambers and engage with
broader perspectives.
Maybe some sort of algorithmic change so that they are still able to see things that are not
just in their circle.–P12
Current recommendation systems inadvertently reinforce echo chambers by primarily present-
ing content users already prefer, which is driven by monetization and engagement rather than
encouraging balanced discourse. To address this, recommendation algorithms should intentionally
introduce verified content representing alternative or opposing viewpoints. Such design would
actively disrupt echo chambers and provide users with broader perspectives, helping counteract
both reinforcement and conformity pressures.
Content creator training and education.Participants also suggested platforms could offer
training or education programs to enhance content creators’ abilities to produce responsible and
meaningful content.
It all depends on how the content creator carries themselves—whether they have done the
training and have the skills to create content to begin with. A lot of content creators are
coming in to create content, but they have no skills. They are throwing videos out there,
trying to get likes. The market is flooded with junk videos.–P19
Structured programs to guide content creators on best practices and ethical standards could signifi-
cantly enhance content quality, reduce the propagation of misinformation or extremist narratives,
and ultimately help maintain environments where conformity to uninformed or extreme views is
less appealing.
Interventions to prevent extremism.Participants discussed the importance of robust moderation
strategies to proactively identify and intervene against extremist behaviors. This approach aligns
closely with design implications discussed earlier for reducing conformity, such as clear guidelines,
proactive moderation, and accountability mechanisms. These overlapping strategies help tackle both
conformity and reinforcement by simultaneously promoting responsible discourse and discouraging
extremism.
I think they can maybe have more monitors or an admin—people who can interrupt it if it
is normal—but if they see that there is more violent talk, that the words they are using are
a little bit more targeted, then they should be able to come in and shut it down. If it is a
chat room, they should close the chat room, lock the discussion board, no more comments,
and then delete it. If there are certain members who are repeat offenders, they should be
banned or blocked, or have their account deleted.–P08
4.3.5 Conditional benefits of conformity and reinforcement.Although participants overwhelmingly
emphasized the negative consequences of conformity and reinforcement, they also described cir-
cumstances where these dynamics could serve protective or constructive purposes. These reflections
underscore that the effects of silence and reinforcement are not uniformly harmful; under specific
conditions, they may buffer against personal risks, preserve relationships, or amplify supportive
communities.
Benefits of conformity.At the individual level, silence was often described as a strategic or
protective choice. Withholding opinions helped some participants avoid harassment, doxxing, or
stalking.
Some part of it is security matter...You don’t want some weirdo doxxing you or stalking
you. You hear about stuff like that happening all the time.–P13
Proc. ACM Hum.-Comput. Interact., Vol. 10, No. 6, Article CSCW152. Publication date: October 2026.

CSCW152:22 Wang et al.
Silence was also framed as a way to maintain social harmony and personal relationships, allowing
individuals to navigate diverse viewpoints without unnecessary conflict.
You don’t piss anyone off, and you don’t ruin any real life connections.–P11
Benefits of reinforcement.At the community level, reinforcement within echo chambers was
sometimes experienced as supportive rather than isolating. For some participants, being surrounded
by like-minded voices provided a sense of belonging, validation, and confidence.
It may foster a sense of belonging even if somebody’s view is harmful or wrong in some
sense.–P03
You feel better about yourself because you think that you’re in the majority, and you think
that everybody would agree with you. When you’re living in that environment, it’s good
for you, or it makes your life more comfortable.–P09
Reinforcement was also seen as amplifying marginalized or contested voices, offering encourage-
ment to persist in speaking out despite opposition.
It allows you to express your views unfiltered, without caring about others, and usually
your voice is the strongest. You influence others to start speaking up because of how
unafraid you are.–P11
Taken together, these reflections show that conformity and reinforcement should not be understood
in absolute terms. The same behaviors that silence diverse viewpoints in some settings can, in others,
function as strategies of protection, relationship management, or community support. The critical
question is not only whether people conform or reinforce, but also what consequences follow. When
outcomes preserve safety, enable dialogue across differences, or empower marginalized voices, these
dynamics may be adaptive. When they entrench hostility, misinformation, or exclusion, intervention
becomes necessary. Recognizing this distinction shifts the discussion from simple value judgments
toward designing systems that can adapt to context—across individual and community levels, and
through both reactive and proactive strategies.
5 Design Implications
In survey and interview responses, participants highlighted critical barriers to open expression
and constructive discourse on social media, emphasizing conformity pressures, fear of extremism,
misinformation, and unclear moderation policies. While current platform efforts, such as fact-
checking mechanisms [97] and algorithmic advancements in moderation [45] demonstrate steps in
the right direction, participants clearly indicated that these strategies alone remain insufficient to
fundamentally alter user behavior or significantly reduce conformity pressures.
Participants’ reflections indicate a need for a shift from reactive, moderation-focused interven-
tions toward proactive, inclusive, and collaboration-oriented approaches. Fact-checking systems,
for instance, should not operate solely as post-hoc moderation. Instead, they could be embedded
into pre-posting nudges [56], for example, prompting users with counterevidence or prompting
reflection when posting on high-risk or polarizing topics. This type of intervention would build
on the accuracy nudges [20, 78] that have been studied extensively for promoting fact-checking
behavior among social media users [13]. By placing these nudges before posting, they may also
support users who are self-censoring by providing confidence and credible evidence to express their
views. Similarly, content moderation should not only penalize extreme behavior but proactively
incentivize and elevate healthy, respectful interactions under community-level efforts [23]. Plat-
forms have experimented with peer-sourced explanatory prompts, such as Community Notes on X3
3https://help.x.com/en/using-x/community_notes
Proc. ACM Hum.-Comput. Interact., Vol. 10, No. 6, Article CSCW152. Publication date: October 2026.

Silence and Noise: Self-censorship and Opinion Expression on Social Media CSCW152:23
(formerly known as Birdwatch on Twitter4), where trusted users provide contextual clarifications
rather than just binary flags. However, these efforts often rely on voluntary participation without
sustained engagement mechanisms. Our findings suggest that the effectiveness and quality of such
systems could be enhanced by implementing clear incentive mechanisms—such as credibility scores,
visibility boosts, or platform rewards—alongside social feedback loops like peer recognition, and by
embedding them seamlessly into users’ content engagement workflows.
Beyond individual-level nudges, our modeling results highlight the importance of community
context in self-censorship. We found that perceived support from the community is strongly
associated with whether users remain silent or adjust their expressed opinions. This suggests
opportunities for community-aware interventions. For example, platforms could enact a “small
group mode” that allows sensitive posts to be shared with narrower audiences, reducing the risks
associated with large, heterogeneous communities. Similarly, lightweight support signals, such
as indicators that others in the network share similar views, may encourage hesitant users to
participate more openly.
Importantly, study participants emphasized that relying solely on internal moderation creates a
structural conflict of interest, as platforms benefit from the engagement stimulated by divisive con-
tent. To address this, a combination of internal moderation with external oversight mechanisms is
essential for effectively tackling such issues [34]. One actionable approach is the implementation of
independent oversight bodies, such as Meta’s Oversight Board5, which reviews content moderation
decisions and provides accountability beyond the platform’s internal processes. In parallel, estab-
lishing publicly accessible databases that document moderation actions would enable retrospective
analysis and help restore users’ trust in actively participating in public interactions. Some platforms
have taken initial steps toward this vision—for example, Twitter (now X) previously launched
the Twitter Moderation Research Consortium to share moderation-related data with the public6.
However, these efforts have not been sustained, highlighting the need for regulatory mandates to
institutionalize transparency rather than relying on platform autonomy. Current regulatory efforts,
including the Digital Services Act (DSA) Transparency Database7, offer a promising step toward in-
dependent auditing, though recent findings reveal uneven adherence and reporting inconsistencies
across platforms [91]. These efforts underscore the importance of combining internal moderation
efforts with external regulatory frameworks to strengthen platform accountability and ensure more
consistent, transparent moderation practices.
Finally, we found that reinforcement and conformity coexist in a self-reinforcing loop: reinforce-
ment intensifies conformity pressures by repeatedly amplifying dominant views and marginalizing
opposite opinions, which in turn creates an environment where users feel compelled to conform
even more strongly. This cyclical relationship results in progressively narrower discourse spaces,
escalating polarization, and heightening the risk of online and offline harms. Effectively breaking
this cycle requires targeted design interventions that address both conformity and reinforcement
in tandem. These include:
• Algorithmic injection of minority perspectives: Implement calibrated exposure models in
feed recommendations to balance viewpoint diversity and mitigate echo chambers [50].
• Training for responsible content creation: Provide creator education and guidelines to en-
courage the production of respectful and inclusive content.
4https://blog.x.com/en_us/topics/product/2021/introducing-birdwatch-a-community-based-approach-to-misinformation
5https://www.oversightboard.com/
6https://blog.x.com/en_us/topics/company/2022/twitter-moderation-research-consortium-open-researchers
7https://transparency.dsa.ec.europa.eu/
Proc. ACM Hum.-Comput. Interact., Vol. 10, No. 6, Article CSCW152. Publication date: October 2026.

CSCW152:24 Wang et al.
• Proactive, context-aware moderation: Develop moderation systems that adapt to evolving
forms of interaction by considering the context of user behavior [95].
These interventions reflect a shift toward designing for expression as a reflection of social identity,
fostering community engagement and inclusivity in future platform designs.
6 Conclusions
Self-censorship manifests in multiple ways. Beyond complete silence, it can include posting subtle or
“toned down” opinions, engaging passively, communicating through private channels, referencing
external sources rather than commenting directly, and even adopting more extreme positions
to demonstrate agreement. These patterns provide empirical support for self-silencing theory
while extending it beyond complete withdrawal, showing that self-censorship often takes the
form of strategic adjustment rather than silence alone. Importantly, our findings further indicate
that such behaviors can reflect deliberate boundary setting or strategic restraint, rather than fear,
disengagement, or withdrawal from public discourse.
While conformity effects and reinforcement through group membership might appear contra-
dictory, they can coexist and are shaped by social context and how individuals relate to their
communities. Our results refine social identity theory by showing that individuals respond not only
to group membership but also to perceived community support and anticipated audience reactions.
These dynamics are closely related to processes of self-presentation or “exhibition identity”, where
individuals manage how they appear to others in social settings. In these scenarios, individuals
often align themselves with traits and norms deemed socially desirable. On social media, this entails
highlighting aspects of one’s life or opinions that are expected to attract positive feedback and
validation in their community. The extent to which a person conforms or expresses their true beliefs
can be influenced by their perceived community characteristics, whether they find themselves in
the minority or majority within a particular social context. These patterns are also consistent with
self-presentation theory and show how users actively manage the trade-off between authenticity
and social acceptability. Rather than simply projecting a favorable image, participants describe
ongoing negotiation between expressing true beliefs and maintaining social relationships under
conditions of uncertainty and visibility.
Building on these findings, we suggest that addressing opinion conformity and reinforcement
requires not only content-level interventions but also design considerations that reshape how
individuals engage with identity and audience. Design implications should therefore extend be-
yond algorithmic adjustments or moderation strategies. They must also support more flexible
self-expression and allow users to navigate complex social expectations. That is, elevating construc-
tive discourse through fact-checking mechanisms and offering visible incentives for thoughtful
engagement can help normalize meaningful conversations and reduce the pressure to conform or
provoke. In addition, sustained impact requires the combined efforts of communities, platforms,
and external regulatory oversight to facilitate meaningful identity presentation and enforce ac-
countability through fair moderation practices. This shift has the potential to create more authentic,
inclusive, and resilient digital environments.
7 Limitations and Future Work
Our findings from the survey and interviews are based on self-reported data regarding opinion
sharing, which introduce biases related to self-perception. The measures in this study capture
participants’ reported perceptions and intentions rather than directly observed behavior, and the
results should be interpreted accordingly. This is particularly relevant for studying self-censorship,
as behaviors of interest often involve non-action, such as choosing not to post, which cannot be
Proc. ACM Hum.-Comput. Interact., Vol. 10, No. 6, Article CSCW152. Publication date: October 2026.

Silence and Noise: Self-censorship and Opinion Expression on Social Media CSCW152:25
directly observed. At the same time, self-reported data introduce their own uncertainties, and future
work may benefit from combining self-reports with behavioral data where feasible.
Additionally, by limiting our participants to social media users in the United States, we excluded
international users from our sample. This restriction narrows our findings to US users. While
dataset statistics indicate a relatively balanced demographic distribution representing the social
media user population, we acknowledge potential sampling bias. While we made efforts to reduce
response bias by presenting the study materials with neutral framing and structuring interview
questions to cover both positive and negative aspects, we still recognize the possibility of such bias
in participants’ responses. Furthermore, while our models focused on community-level factors of
self-censorship, open-ended responses revealed additional determinants such as platform norms
and social influence not captured quantitatively. These factors might be studied in future work
examining the complexity of self-censorship from alternative perspectives.
8 Ethical Considerations
Both survey and interview components of the study were approved by the Institutional Review
Board (IRB) at the researchers’ institution. All participants have given their consent to participate
in the survey and interview studies. All identifiable information has been removed from the paper
and research artifacts to ensure privacy, and all video and audio recordings were deleted after
transcription quality checks. Given the relatively narrow nature of the data collected in this study,
we believe the risk of privacy violation and misuse to be minimal.
Acknowledgments
This work was supported by funding from the National Science Foundation award #2247723.
References
[1] Klaus Abbink, Lata Gangadharan, Toby Handfield, and John Thrasher. 2017. Peer punishment promotes enforcement
of bad social norms.Nature communications8, 1 (2017), 1–8.
[2] Hunt Allcott, Matthew Gentzkow, and Chuan Yu. 2019. Trends in the diffusion of misinformation on social media.
Research & Politics6, 2 (2019), 2053168019848554.
[3] Floyd Henry Allport. 1924.Social psychology. Boston, Houghton.
[4] Tawfiq Ammari and Sarita Schoenebeck. 2015. Understanding and supporting fathers and fatherhood on social media
sites. InProceedings of the 33rd annual ACM conference on human factors in computing systems. 1905–1914.
[5] Solomon E Asch. 1951. Effects of group pressure upon the modification and distortion of judgments.Organizational
influence processes58 (1951), 295–303.
[6] Jie Bai, Qingchao Kong, Linjing Li, Lei Wang, and Daniel Zeng. 2019. Exploring cognitive dissonance on social media.
In2019 IEEE International Conference on Intelligence and Security Informatics (ISI). IEEE, 143–145.
[7] Christopher A Bail, Lisa P Argyle, Taylor W Brown, John P Bumpus, Haohan Chen, MB Fallin Hunzaker, Jaemin Lee,
Marcus Mann, Friedolin Merhout, and Alexander Volfovsky. 2018. Exposure to opposing views on social media can
increase political polarization.Proceedings of the National Academy of Sciences115, 37 (2018), 9216–9221.
[8] Cameron Ballard, Ian Goldstein, Pulak Mehta, Genesis Smothers, Kejsi Take, Victoria Zhong, Rachel Greenstadt, Tobias
Lauinger, and Damon McCoy. 2022. Conspiracy brokers: Understanding the monetization of youtube conspiracy
theories. InProceedings of the ACM Web Conference 2022. 2707–2718.
[9] Daniel Bar-Tal. 2017. Self-censorship as a socio-political-psychological phenomenon: Conception and research.
Political Psychology38 (2017), 37–65.
[10] Pablo Barberá. 2020. Social media, echo chambers, and political polarization.Social media and democracy: The state of
the field, prospects for reform(2020), 34–55.
[11] Pablo Barberá, John T Jost, Jonathan Nagler, Joshua A Tucker, and Richard Bonneau. 2015. Tweeting from left to
right: Is online political communication more than an echo chamber?Psychological science26, 10 (2015), 1531–1542.
[12] Roy F Baumeister and Debra G Hutton. 1987. Self-presentation theory: Self-construction and audience pleasing. In
Theories of group behavior. Springer, 71–87.
[13] Md Momen Bhuiyan, Michael Horning, Sang Won Lee, and Tanushree Mitra. 2021. Nudgecred: Supporting news
credibility assessment on social media through nudges.Proceedings of the ACM on Human-Computer Interaction5,
Proc. ACM Hum.-Comput. Interact., Vol. 10, No. 6, Article CSCW152. Publication date: October 2026.

CSCW152:26 Wang et al.
CSCW2 (2021), 1–30.
[14] Engin Bozdag. 2013. Bias in algorithmic filtering and personalization.Ethics and information technology15 (2013),
209–227.
[15] Petter Bae Brandtzæg, Marika Lüders, and Jan Håvard Skjetne. 2010. Too many Facebook “friends”? Content sharing
and sociability versus the need for privacy in social network sites.Intl. Journal of Human–Computer Interaction26,
11-12 (2010), 1006–1030.
[16] Virginia Braun and Victoria Clarke. 2006. Using thematic analysis in psychology.Qualitative research in psychology3,
2 (2006), 77–101.
[17] Marilynn B Brewer et al. 1999. The psychology of prejudice: Ingroup love or outgroup hate?Journal of social issues
55 (1999), 429–444.
[18] Axel Bruns. 2017. Echo chamber? What echo chamber? Reviewing the evidence. In6th Biennial Future of Journalism
Conference (FOJ17).
[19] Alycia Burnett, Devin Knighton, and Christopher Wilson. 2022. The self-censoring majority: How political identity
and ideology impacts willingness to self-censor and fear of isolation in the United States.Social Media+ Society8, 3
(2022), 20563051221123031.
[20] Lucy H Butler, Toby Prike, and Ullrich KH Ecker. 2024. Nudge-based misinformation interventions are effective in
information environments with low misinformation prevalence.Scientific Reports14, 1 (2024), 11495.
[21] Damon Centola, Robb Willer, and Michael Macy. 2005. The emperor’s dilemma: A computational model of self-
enforcing norms.Amer. J. Sociology110, 4 (2005), 1009–1040.
[22] Irfan Chaudhry and Anatoliy Gruzd. 2020. Expressing and challenging racist discourse on Facebook: How social
media weaken the “spiral of silence” theory.Policy & Internet12, 1 (2020), 88–108.
[23] Chhaya Chouhan, Christy M LaPerriere, Zaina Aljallad, Jess Kropczynski, Heather Lipford, and Pamela J Wisniewski.
2019. Co-designing for community oversight: Helping people make privacy and security decisions together.Proceedings
of the ACM on Human-Computer Interaction3, CSCW (2019), 1–31.
[24] Matteo Cinelli, Gianmarco De Francisci Morales, Alessandro Galeazzi, Walter Quattrociocchi, and Michele Starnini.
2021. The echo chamber effect on social media.Proceedings of the National Academy of Sciences118, 9 (2021).
[25] Katherine Clayton, Spencer Blair, Jonathan A Busam, Samuel Forstner, John Glance, Guy Green, Anna Kawata, Akhila
Kovvuri, Jonathan Martin, Evan Morgan, et al. 2020. Real solutions for fake news? Measuring the effectiveness of
general warnings and fact-check tags in reducing belief in false stories on social media.Political behavior42 (2020),
1073–1095.
[26] Bennett Clifford. 2021. Moderating Extremism: The State of Online Terrorist Content Removal Policy in the United
States.Program on Extremism. Washington DC: George Washington University, December(2021).
[27] James S Coleman. 1988. Social capital in the creation of human capital.American journal of sociology94 (1988),
S95–S120.
[28] Richard S Crutchfield. 1955. Conformity and character.American psychologist10, 5 (1955), 191.
[29] Sauvik Das and Adam Kramer. 2013. Self-censorship on Facebook. InProceedings of the International AAAI Conference
on Web and Social Media, Vol. 7. 120–127.
[30] Michela Del Vicario, Alessandro Bessi, Fabiana Zollo, Fabio Petroni, Antonio Scala, Guido Caldarelli, H Eugene
Stanley, and Walter Quattrociocchi. 2016. The spreading of misinformation online.Proceedings of the National
Academy of Sciences113, 3 (2016), 554–559.
[31] Kerry Dhakal. 2022. NVivo.Journal of the Medical Library Association: JMLA110, 2 (2022), 270.
[32] Benjamin D Douglas, Patrick J Ewell, and Markus Brauer. 2023. Data quality in online human-subjects research:
Comparisons between MTurk, Prolific, CloudResearch, Qualtrics, and SONA.Plos one18, 3 (2023), e0279720.
[33] Elizabeth Dubois and Julia Szwarc. 2018. Self-Censorship, Polarization, and the—Spiral of Silence on Social Media. In
Policy & Politics Conference.
[34] Houda Elmimouni, Yarden Skop, Norah Abokhodair, Sarah Rüller, Konstantin Aal, Anne Weibert, Adel Al-Dawood,
Volker Wulf, and Peter Tolmie. 2024. Shielding or silencing?: An investigation into content moderation during the
sheikh jarrah crisis.Proceedings of the ACM on Human-Computer Interaction8, GROUP (2024), 1–21.
[35] Peer Eyal, Rothschild David, Gordon Andrew, Evernden Zak, and Damer Ekaterina. 2021. Data quality of platforms
and panels for online behavioral research.Behavior research methods(2021), 1–20.
[36] Vincent F Filak, Scott Reinardy, and Adam Maksl. 2009. Expanding and validating applications of the willingness to
self-censor scale: Self-censorship and media advisers’ comfort level with controversial topics.Journalism & Mass
Communication Quarterly86, 2 (2009), 368–382.
[37] Andrew S Fullerton. 2009. A conceptual framework for ordered logistic regression models.Sociological methods &
research38, 2 (2009), 306–347.
[38] Bharath Ganesh and Jonathan Bright. 2020. Countering extremists on social media: Challenges for strategic commu-
nication and content moderation. 6–19 pages.
Proc. ACM Hum.-Comput. Interact., Vol. 10, No. 6, Article CSCW152. Publication date: October 2026.

Silence and Noise: Self-censorship and Opinion Expression on Social Media CSCW152:27
[39] Kiran Garimella, Gianmarco De Francisci Morales, Aristides Gionis, and Michael Mathioudakis. 2018. Political
discourse on social media: Echo chambers, gatekeepers, and the price of bipartisanship. InProceedings of the 2018
world wide web conference. 913–922.
[40] Michael T Gastner, Beáta Oborny, and Máté Gulyás. 2018. Consensus time in a voter model with concealed and
publicly expressed opinions.Journal of Statistical Mechanics: Theory and Experiment2018, 6 (2018), 063401.
[41] Sherice Gearhart and Weiwu Zhang. 2015. “Was it something I said?”“No, it was something you posted!” A study of
the spiral of silence theory in social media contexts.Cyberpsychology, Behavior, and Social Networking18, 4 (2015),
208–213.
[42] Parush Gera, Nadia Thomas, and Tempestt Neal. 2020. Hesitation while posting: A cross-sectional survey of sensitive
topics and opinion sharing on social media. InInternational Conference on Social Media and Society. 134–140.
[43] James L Gibson and Joseph L Sutherland. 2023. Keeping your mouth shut: Spiraling self-censorship in the United
States.Political Science Quarterly138, 3 (2023), 361–376.
[44] Nabeel Gillani, Ann Yuan, Martin Saveski, Soroush Vosoughi, and Deb Roy. 2018. Me, my echo chamber, and I:
introspection on social media polarization. InProceedings of the 2018 World Wide Web Conference. 823–831.
[45] Tarleton Gillespie. 2020. Content moderation, AI, and the question of scale.Big Data & Society7, 2 (2020),
2053951720943234.
[46] Erving Goffman. 1949. Presentation of self in everyday life.Amer. J. Sociology55 (1949), 6–7.
[47] Steven Greene. 2004. Social identity theory and party identification.Social Science Quarterly85, 1 (2004), 136–153.
[48] Andrew Guess, Brendan Nyhan, Benjamin Lyons, and Jason Reifler. 2018. Avoiding the echo chamber about echo
chambers.Knight Foundation2, 1 (2018), 1–25.
[49] Keith N Hampton, Harrison Rainie, Weixu Lu, Maria Dwyer, Inyoung Shin, and Kristen Purcell. 2014.Social media
and the’spiral of silence’. PewResearchCenter Washington, DC, USA.
[50] Natali Helberger, Kari Karppinen, and Lucia D’acunto. 2018. Exposure diversity as a design principle for recommender
systems.Information, communication & society21, 2 (2018), 191–207.
[51] Monique Hennink and Bonnie N Kaiser. 2022. Sample sizes for saturation in qualitative research: A systematic review
of empirical tests.Social science & medicine292 (2022), 114523.
[52] Sara B Hobolt, Katharina Lawall, and James Tilley. 2024. The polarizing effect of partisan echo chambers.American
Political Science Review118, 3 (2024), 1464–1479.
[53] Erin E Hollenbaugh. 2021. Self-presentation in social media: Review and research opportunities.Review of communi-
cation research9 (2021), 80.
[54] Piers Howe, Andrew Perfors, Keith James Ransom, Bradley Walker, Nicolas Fay, Yoshihisa Kashima, and Morgan
Saletta. 2023. Self-censorship appears to be an effective way of reducing the spread of misinformation on social
media. InProceedings of the Annual Meeting of the Cognitive Science Society, Vol. 45.
[55] Dana Crowley Jack. 2011. Reflections on the silencing the self scale and its origins.Psychology of Women Quarterly
35, 3 (2011), 523–529.
[56] Farnaz Jahanbakhsh, Amy X Zhang, Adam J Berinsky, Gordon Pennycook, David G Rand, and David R Karger.
2021. Exploring lightweight interventions at posting time to reduce the sharing of misinformation on social media.
Proceedings of the ACM on human-computer interaction5, CSCW1 (2021), 1–42.
[57] Gabriela Juncosa, Taha Yasseri, Julia Koltai, and Gerardo Iniguez. 2024. Toxic behavior silences online political
conversations.arXiv preprint arXiv:2412.05741(2024).
[58] Natascha A Karlova and Karen E Fisher. 2013. A social diffusion model of misinformation and disinformation for
understanding human information behaviour. (2013).
[59] Stephen King. 1981. Conflicts between public and private opinion.Long Range Planning14, 4 (1981), 90–105.
[60] Elizaveta Konovalova, Gaël Le Mens, and Nikolas Schöll. 2023. Social media feedback and extreme opinion expression.
Plos one18, 11 (2023), e0293805.
[61] KP Krishna Kumar and G Geethakumari. 2014. Detecting misinformation in online social networks using cognitive
psychology.Human-centric Computing and Information Sciences4, 1 (2014), 1–22.
[62] K Hazel Kwon, Shin-Il Moon, and Michael A Stefanone. 2015. Unspeaking on Facebook? Testing network effects on
self-censorship of political expressions in social network sites.Quality & quantity49 (2015), 1417–1435.
[63] Miron Lakomy. 2023. Why do online countering violent extremism strategies not work? The case of digital jihad.
Terrorism and political violence35, 6 (2023), 1261–1298.
[64] Jooyoung Lee, Sarah Rajtmajer, Eesha Srivatsavaya, and Shomir Wilson. 2021. Digital inequality through the lens of
self-disclosure.Proceedings on Privacy Enhancing Technologies(2021).
[65] Jianing Li and Min-Hsin Su. 2020. Real talk about fake news: Identity language and disconnected networks of the US
public’s “fake news” discourse on Twitter.Social Media+ Society6, 2 (2020), 2056305120916841.
[66] Soo Ling Lim and Peter J Bentley. 2022. Opinion amplification causes extreme polarization in social networks.
Scientific Reports12, 1 (2022), 18131.
Proc. ACM Hum.-Comput. Interact., Vol. 10, No. 6, Article CSCW152. Publication date: October 2026.

CSCW152:28 Wang et al.
[67] David P MacKinnon, Amanda J Fairchild, and Matthew S Fritz. 2007. Mediation analysis.Annu. Rev. Psychol.58 (2007),
593–614.
[68] Alice E Marwick and Danah Boyd. 2011. I tweet honestly, I tweet passionately: Twitter users, context collapse, and
the imagined audience.New media & society13, 1 (2011), 114–133.
[69] Ariadne Neureiter, Marlis Stubenvoll, Ruta Kaskeleviciute, and Jörg Matthes. 2021. Trust in science, perceived media
exaggeration about COVID-19, and social distancing behavior.Frontiers in Public Health9 (2021), 670485.
[70] Tien T Nguyen, Pik-Mai Hui, F Maxwell Harper, Loren Terveen, and Joseph A Konstan. 2014. Exploring the filter
bubble: the effect of using recommender systems on content diversity. InProceedings of the 23rd international conference
on World wide web. 677–686.
[71] Todd G Nick and Kathleen M Campbell. 2007. Logistic regression.Topics in biostatistics(2007), 273–301.
[72] Elisabeth Noelle-Neumann. 1974. The spiral of silence a theory of public opinion.Journal of communication24, 2
(1974), 43–51.
[73] Daniel M Oppenheimer, Tom Meyvis, and Nicolas Davidenko. 2009. Instructional manipulation checks: Detecting
satisficing to increase statistical power.Journal of experimental social psychology45, 4 (2009), 867–872.
[74] Mustafa Oz, Saif Shahin, and Scott B Greeves. 2024. Platform affordances and spiral of silence: How perceived
differences between Facebook and Twitter influence opinion expression online.Technology in Society76 (2024),
102431.
[75] Lawrence A Palinkas, Sarah M Horwitz, Carla A Green, Jennifer P Wisdom, Naihua Duan, and Kimberly Hoagwood.
2015. Purposeful sampling for qualitative data collection and analysis in mixed method implementation research.
Administration and policy in mental health and mental health services research42, 5 (2015), 533–544.
[76] Michael Quinn Patton. 2014.Qualitative research & evaluation methods: Integrating theory and practice. Sage
publications.
[77] Gordon Pennycook, Tyrone D Cannon, and David G Rand. 2018. Prior exposure increases perceived accuracy of fake
news.Journal of experimental psychology: general147, 12 (2018), 1865.
[78] Ethan Porter, Thomas J Wood, David A Broniatowski, and Pedram Hosseini. 2024. Shoves, nudges and combating
misinformation: evidence on a new approach.Behavioural Public Policy(2024), 1–17.
[79] Elia Powers, Michael Koliska, and Pallavi Guha. 2019. “Shouting matches and echo chambers”: perceived identity
threats and political self-censorship on social media.International Journal of Communication13 (2019), 20.
[80] P Racca, Roberto Casarin, Pierpaolo Dondio, and F Squazzoni. 2018. Relating group size and posting activity of an
online community of financial investors: Regularities and seasonal patterns.Physica A: Statistical Mechanics and its
Applications493 (2018), 458–466.
[81] Samuel C Rhodes. 2022. Filter bubbles, echo chambers, and fake news: How social media conditions individuals to be
less critical of political misinformation.Political Communication39, 1 (2022), 1–22.
[82] Richard Rose. 2007. Going Public with Private Opinions: Are Post-Communist Citizens Afraid to Say What They
Think?Journal of Elections, Public Opinion and Parties17, 2 (2007), 123–142.
[83] Barry R Schlenker. 1985. Identity and self-identification.The self and social life65, 1 (1985), 99–106.
[84] Yilun Shang. 2019. Resilient consensus for expressed and private opinions.IEEE Transactions on Cybernetics51, 1
(2019), 318–331.
[85] Jieun Shin, Lian Jian, Kevin Driscoll, and François Bar. 2018. The diffusion of misinformation on social media:
Temporal pattern, message, and source.Computers in Human Behavior83 (2018), 278–287.
[86] Dongyoung Sohn. 2022. Spiral of silence in the social media era: A simulation approach to the interplay between
social networks and mass media.Communication Research49, 1 (2022), 139–166.
[87] Jan E Stets and Peter J Burke. 2000. Identity theory and social identity theory.Social psychology quarterly(2000),
224–237.
[88] Henri Tajfel and John C Turner. 2004. The social identity theory of intergroup behavior. (2004).
[89] Henri Tajfel, John C Turner, William G Austin, and Stephen Worchel. 1979. An integrative theory of intergroup
conflict.Organizational identity: A reader56, 65 (1979), 9780203505984–16.
[90] Sabine Trepte and Laura S Loy. 2017. Social identity theory and self-categorization theory.The international
encyclopedia of media effects(2017), 1–13.
[91] Amaury Trujillo, Tiziano Fagni, and Stefano Cresci. 2025. The DSA Transparency Database: Auditing self-reported
moderation actions by social media.Proceedings of the ACM on Human-Computer Interaction9, 2 (2025), 1–28.
[92] Christian Unkelbach and Felix Speckmann. 2021. Mere Repetition Increases Belief in Factually True COVID-19-Related
Information.Journal of Applied Research in Memory and Cognition(2021).
[93] Soroush Vosoughi, Deb Roy, and Sinan Aral. 2018. The spread of true and false news online.Science359, 6380 (2018),
1146–1151.
[94] Nathan Walter, Jonathan Cohen, R Lance Holbert, and Yasmin Morag. 2020. Fact-checking: A meta-analysis of what
works and for whom.Political communication37, 3 (2020), 350–375.
Proc. ACM Hum.-Comput. Interact., Vol. 10, No. 6, Article CSCW152. Publication date: October 2026.

Silence and Noise: Self-censorship and Opinion Expression on Social Media CSCW152:29
[95] Xinyu Wang, Sai Koneru, Pranav Narayanan Venkit, Brett Frischmann, and Sarah Rajtmajer. 2024. The unappreciated
role of intent in algorithmic moderation of social media content.arXiv preprint arXiv:2405.11030(2024).
[96] Mark Warner and Victoria Wang. 2019. Self-censorship in social networking sites (SNSs)–privacy concerns, privacy
awareness, perceived vulnerability and information management.Journal of Information, Communication and Ethics
in Society17, 4 (2019), 375–394.
[97] Ben Wasike. 2023. You’ve been fact-checked! Examining the effectiveness of social media fact-checking against the
spread of misinformation.Telematics and Informatics Reports11 (2023), 100090.
[98] Brian E Weeks, Audrey Halversen, and German Neubaum. 2024. Too scared to share? Fear of social sanctions for
political expression on social media.Journal of Computer-Mediated Communication29, 1 (2024), zmad041.
[99] Robb Willer, Ko Kuwabara, and Michael W Macy. 2009. The false enforcement of unpopular norms.Amer. J. Sociology
115, 2 (2009), 451–490.
[100] Chuhao Wu, Xinyu Wang, John Carroll, and Sarah Rajtmajer. 2024. Reacting to Generative AI: Insights from Student
and Faculty Discussions on Reddit. InProceedings of the 16th ACM Web Science Conference(, Stuttgart, Germany,)
(WEBSCI ’24). Association for Computing Machinery, New York, NY, USA, 103–113. doi:10.1145/3614419.3644014
[101] Jerrold H Zar. 2005. Spearman rank correlation.Encyclopedia of biostatistics7 (2005).
[102] Dora Zhao, Diyi Yang, and Michael S Bernstein. 2025. Mapping the Spiral of Silence: Surveying Unspoken Opinions
in Online Communities.arXiv preprint arXiv:2502.00952(2025).
[103] Melissa Zimdars and Kembrew McLeod. 2020.Fake news: understanding media and misinformation in the digital age.
MIT Press.
A Appendix 1: Survey Instrument
A.1 Introduction
Objectives: This survey aims to understand patterns of opinion expression on social media plat-
forms. Your responses are anonymous and will help understand the dynamics of online discourse.
Privacy and Ethics Statement: The survey data collected is used solely for research purposes
and all responses are kept strictly confidential. Respondents have the right to withdraw at any time
without penalty or retribution. By participating, respondents consent to the use of their anonymized
data for research purposes.
A.2 Consent
Please consent to the following statement: I agree to participate in the research study. I understand
the purpose and nature of this study and I am participating voluntarily. I understand that I can
withdraw from the study at any time, without any penalty or consequences. The IRB has reviewed
the study and determined that, as currently described, it is exempt from ongoing IRB review.
A.3 Demographic Information
1. What is your gender?
2. What category below includes your age?
3. Which race/ethnicity best describes you?
4. What is the highest degree you have completed?
5. In politics today, do you consider yourself a Republican, Democrat, an independent or something
else?
(If answer “Independent or other”: As of today, do you lean more to the Republican Party or more
to the Democratic Party?)
A.4 Social Media Usage
1. Which social media platforms do you use regularly and how many connections do you have on
the target platforms?
2. In a typical week, how many times do you share or post your opinions on social media platforms
related to one or more of the following topics: politics (e.g., US election), social justice issues (e.g.,
Proc. ACM Hum.-Comput. Interact., Vol. 10, No. 6, Article CSCW152. Publication date: October 2026.

CSCW152:30 Wang et al.
gender equality), environmental issues (e.g., climate change), religion (e.g., ritual practices), health
and healthcare (e.g., vaccinations), or technology and innovation (e.g., ChatGPT)?
A.5 Opinion Expression
1. Assess the typical/average level of polarization you observe in conversations online about each
of the following topics in your social networks.
2. Are you more or less willing to express your opinions about the following topics on social media?
3. Please indicate the extent to which you agree with each of the following statements:
I feel more authentic in expressing my beliefs in private conversations than on social media
platforms.
I feel the need to filter or adjust my personal beliefs before sharing them on social media.
Sometimes my social media persona is different from my real-life persona in terms of expressing
opinions.
4. Please indicate the extent to which you agree with each of the following statements:
I have censored or modified my opinion before posting due to fear of isolation or criticism.
I have refrained from expressing a minority view on a polarizing topic to avoid confrontation.
I feel that certain views are silenced on social media because they are unpopular.
5. Please indicate the extent to which you agree with each of the following statements:
I feel more inclined to express controversial opinions on social media because I anticipate support
from my social media connections.
I feel that my opinions are reinforced by my social media circle.
I believe that the backing of my in-group on social media leads me to amplify my expressed opinions.
A.6 Topic-specific Questions
1. Politics
Which side are you leaning towards in the upcoming U.S. election?
In your opinion, how polarizing is this topic of the upcoming U.S. election?
How many of your connections do you estimate share the same viewpoint as you on the upcoming
U.S. election? (expressed as a percentage)
Based on your current viewpoint, which one of the following posts would you be more inclined to
share?
2. Health
What is your opinion on COVID-19 vaccination?
In your opinion, how polarizing is the topic of COVID-19 vaccination?
How many of your connections do you estimate share the same viewpoint as you on COVID-19
vaccination? (expressed as a percentage)
Based on your current viewpoint, which one of the following posts would you be more inclined to
share?
3. Technology
What is your opinion on ChatGPT?
In your opinion, how polarizing is this topic of ChatGPT?
How many of your connections do you estimate share the same viewpoint as you on ChatGPT?
(expressed as a percentage)
Based on your current viewpoint, which one of the following posts would you be more inclined to
share?
4. Social Justice
What is your opinion on immigrants/immigration?
In your opinion, how polarizing is the topic of immigrants/immigration?
Proc. ACM Hum.-Comput. Interact., Vol. 10, No. 6, Article CSCW152. Publication date: October 2026.

Silence and Noise: Self-censorship and Opinion Expression on Social Media CSCW152:31
How many of your connections do you estimate share the same viewpoint as you on immi-
grants/immigration? (expressed as a percentage)
Based on your current viewpoint, which opinion would you be more inclined to share?
5. Religion
What is your opinion regarding the intersection of traditional religious beliefs and support for
LGBT rights?
In your opinion, how polarizing is this topic of the intersection of traditional religious beliefs and
support for LGBT rights?
How many of your connections do you estimate share the same viewpoint as you on the intersection
of traditional religious beliefs and support for LGBT rights? (expressed as a percentage)
Based on your current viewpoint, which one of the following posts would you be more inclined to
share?
6. Environment
What is your opinion regarding the trade-off between economic development and the urgency of
climate action?
In your opinion, how polarizing is this topic of the trade-off between economic development and
the urgency of climate action?
How many of your connections do you estimate share the same viewpoint as you on trade-off
between economic development and the urgency of climate action? (expressed as a percentage)
Based on your current viewpoint, which one of the following posts would you be more inclined to
share?
A.7 Open-ended Questions
1. Topics of Disparity: Please specify a topic on which you’ve noticed a disparity between your
own social media posts and your private beliefs.
2. Recent Social Media Post: Provide the content (or a summary) of one of your recent posts on this
topic.
3. Your Private Belief: Describe your actual belief or opinion on this topic. 4. Reason for Disparity:
If there’s a difference between your recent posts and your true belief, could you explain why?
5. Frequency of Disparity: How often do you find that your posts on social media differ from your
private beliefs across various topics?
6. Additional Topics: Are there any other topics or subjects where you’ve noticed a similar disparity
between your social media posts and your private beliefs? If so, please elaborate.
7. Potential Impact: Do you think reluctance to express true opinions could potentially lead to
negative consequences? If so, what could be the consequences? If not, why?
A.8 Invitation to Participate in the Interview
Thank you for participating!
If you would like to be considered for a paid post-survey study ($15 for 30-minute interview), please
reach out to us for more information.
B Appendix 2: Interview Questions
1. Discrepancy Between Public and Private Opinions
a. Instances of Discrepancy
•Have you ever expressed an opinion on social media that differed from your private opinion?
•Please specify the topic and outline what you said versus your actual opinion.
•What prompted you to present a different opinion publicly?
b. Observation of Others’ Discrepancies
Proc. ACM Hum.-Comput. Interact., Vol. 10, No. 6, Article CSCW152. Publication date: October 2026.

CSCW152:32 Wang et al.
•If you seldom post, have you noticed others displaying a discrepancy between their authentic and
public opinions on social media?
c. Consistency in Opinions
•If you always keep your public and private opinions the same, explain why.
2. Determinants of Opinion Sharing
•How do you determine which opinions to share or not share on social media?
•How does the topic of discussion influence your willingness to share certain opinions publicly?
•What features of a topic make you more willing or unwilling to share your opinion?
3. Self-presentation through Social Media
•Do you consciously curate a specific image on social media with the way you post (either post or
not post)?
•Do you feel any conflict between presenting an image of yourself on social media platforms and
being your true self?
4. Influence of Social Media Community
•How does the level of support from your connections affect your willingness to share opinions?
5. The Consequences and Influence of Social Media Dynamics
•Do you witness more opinion reinforcement/amplification or conformity on social media?
•If observe more reinforcement/amplification: What do you consider to be the potential positive
and negative outcomes of opinion reinforcement and amplification?
•If observe more conformity: What could be the potential positive and negative consequences of
opinion conformity and the spiral of silence?
•Do you think the social media community or platform should address these issues?
C Appendix 3
C.1 Quality Check Procedure
At the beginning of the survey we asked participants about their political orientation. Then, ap-
proximately midway through the survey (within a topic-specific section on Politics), we asked
participants a similar question once again. This attention check was seamlessly integrated into the
flow of the survey. We identified 1 out of 390 responses which exhibited a contradictory response
on the attention check. We contacted that participant for an explanation and re-evaluation. The par-
ticipant explained their reasoning, thus their survey was included in downstream analyses. Eleven
(11) out of 390 responses were flagged by Qualtrics as potential bots. We undertook meticulous
examination of those flagged answers including the completeness of the open-ended questions and
total time spent on the survey. We manually ruled out the possibility of those responses being bots.
Thus, we have 390 valid survey responses that are analyzed in the paper.
Received May 13, 2025; revised January 13, 2026; accepted April 9, 2026
Proc. ACM Hum.-Comput. Interact., Vol. 10, No. 6, Article CSCW152. Publication date: October 2026.

Silence and Noise: Self-censorship and Opinion Expression on Social Media CSCW152:33
Characteristic Values,𝑛(%)
Gender
Female 204, 52.31%
Male 172, 44.10%
Other or Prefer not to disclose 14, 3.59%
Age Group
18 to 24 53, 13.59%
25 to 34 128, 32.82%
35 to 44 92,23.59%
45 to 54 65, 16.67%
Above 55 52, 13.33%
Race/Ethnicity
White/Caucasian 218, 55.9%
Hispanic, Latino, or of Spanish origin 50, 12.82%
Black/African American 46, 11.79%
Asian 49, 12.56%
Native American 4, 1.03%
Multiple Ethnicity 23, 5.90%
Highest degree of education completed
Less than high school degree 6, 1.54%
High school degree or equivalent 98, 25.13%
Attending College 39, 10.00%
Associate degree 42, 10.77%
Bachelor degree 146, 37.44%
Graduate degree 51, 13.08%
Other 8, 2.05%
Political Self-identification
Republican 69, 17.69%
Democrat 195, 50.00%
Independent or others (Leaning Democrat) 77, 19.74%
Independent or others (Leaning Republican) 47, 12.05%
Independent or others (No Lean/Neutral) 2, 0.51%
Table A1. Survey respondent demographics (N=390).
Support Polarization Community Mediator
Support1.00 - - -
Polarization0.03 1.00 - -
Community-0.01 0.00 1.00 -
Mediator0.00 0.08 0.33 1.00
Table A2. Correlation Coefficients for Independent Variables and Mediator (Model 1).
Proc. ACM Hum.-Comput. Interact., Vol. 10, No. 6, Article CSCW152. Publication date: October 2026.

CSCW152:34 Wang et al.
Category Subcategory Count
Politics General (27); Military (27); Economics (18); Gun Control (7) 79
Social justice Immigration (27); LGBTQ+ (27); Abortion (21); Race (13); Diversity (5);
Gender (5)
98
Health COVID&Vaccination (9); Mental Health (3); Other (2) 14
Technology AI (9); Other (4) 13
Religion — 16
Environment — 14
Popular Culture Celebrities (8); Sports (2) 10
Personal or Local — 16
None No disparity in posts (137); No topics provided (12) 149
Table A3. Topics for which survey respondents report a disparity between their private beliefs and their social
media posts (from open-ended questions).
Support Polarization Community Mediator
Support1.00 - - -
Polarization0.09 1.00 - -
Community-0.02 0.03 1.00 -
Mediator0.01 0.10 0.33 1.00
Table A4. Correlation coefficients for independent variables and mediator (Model 2).
Variable Model 1 VIF Model 2 VIF
Support 1.00 1.01
Polarization 1.01 1.02
Community Size (maximum_total) 1.12 1.12
Frequency (frequency_numeric) 1.13 1.13
Table A5. Variance inflation factors (VIF) for independent variables and mediator in Model 1 and Model 2.
Path Coefficient Std. Err CI
Community Size to Frequency of Posting 0.33 0.06 [0.29, 0.45]
Frequency of Posting to Dependent Variable -0.53 0.23 [-0.98, -0.07]
Direct Effect of Community Size 0.19 0.10 [0.03, 0.38]
Indirect Effect -0.18 - [-0.22, -0.04]
Table A6. Mediation analysis results: Effect of community size on decision to remain silent mediated by
frequency of posting (The indirect effect coefficient is derived from the average of 1,000 bootstrap samples,
with the confidence interval calculated via bootstrapping.)
Proc. ACM Hum.-Comput. Interact., Vol. 10, No. 6, Article CSCW152. Publication date: October 2026.

Silence and Noise: Self-censorship and Opinion Expression on Social Media CSCW152:35
Path Coefficient Std. Err CI
Community Size to Frequency of Posting 0.33 0.09 [0.15,0.51]
Frequency of Posting to Dependent Variable -0.10 0.06 [-0.22, 0.03]
Direct Effect of Community Size 0.04 0.05 [-0.06,0.13]
Indirect Effect -0.03 - [-0.07, -0.00]
Table A7. Mediation analysis results: effect of community size on discrepancy between public and private
opinion mediated by frequency of posting (The indirect effect coefficient is derived from the average of 1000
bootstrap samples, with the confidence interval calculated via bootstrapping.)
Proc. ACM Hum.-Comput. Interact., Vol. 10, No. 6, Article CSCW152. Publication date: October 2026.
