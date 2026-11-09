---
title: Generative AI-Augmented Thematic Analysis
url: https://doi.org/10.1177/14707853251405043
category: ai-marketing
subcategory: empirical
date: 2025-12
venue: International Journal of Market Research
authors:
- Vimukthi Jayawardene
- Michael T. Ewing
source: openalex-oa
pdf_url: https://researchportal.scu.edu.au/view/delivery/61SCU_INST/12142308600002368/13145590310002368
pages: 33
chars: 82459
fetched_at: '2026-11-08T18:56:03+00:00'
kb_version: 1
---

# Generative AI-Augmented Thematic Analysis

Please do not remove this page
Generative AI-Augmented Thematic Analysis
Jayawardene, Vimukthi; Ewing, Michael T.
https://researchportal.scu.edu.au/esploro/outputs/journalArticle/Generative-AI-Augmented-Thematic-Analysis/991013337084902368/filesAndLinks?in
dex=0
Jayawardene, V., & Ewing, M. T. (2026). Generative AI-Augmented Thematic Analysis. International Journal
of Market Research, 68(2), 162–193. https://doi.org/10.1177/14707853251405043
Published Version: https://doi.org/10.1177/14707853251405043
Document Version: Published (Version of record)
Downloaded On 2026/11/09 05:56:05 +1100
© The Author(s) 2025.
Research:Open
CC BY V4.0
crossconnect@scu.edu.au
Southern Cross University Cross Connect: https://researchportal.scu.edu.au/esploro/
Please do not remove this page

Special Issue Article
International Journal of
Market Research
2026, Vol. 68(2) 162 –193
© The Author(s) 2025
Article reuse guidelines:
sagepub.com/journals-permissions
DOI: 10.1177/14707853251405043
journals.sagepub.com/home/mre
Generative AI-Augmented Thematic
Analysis
Vimukthi Jayawardene 1 and Michael T. Ewing 1*
Abstract
This study explores the use of generative AI tools in qualitative research, speci ﬁcally to enhance
thematic analysis (TA). Traditional TA, while widely adopted in marketing, is inherently labor-
intensive and prone to researcher biases. The method proposed here, generative AI-augmented
thematic analysis (GAATA), addresses these limitations by using gen AI tools to automate and
augment the data analysis process. GAATA comprises three phases: prompt designing, code
generation/validation, and theme generation/validation. The method leverages the capabilities of
multiple gen AI tools to generate initial codes and themes. These codes/themes are then validated
and reﬁned by human researchers, thereby increasing reliability and re ﬂexivity in the TA process. A
set of generic prompt templates are provided to enable researchers with less technical expertise to
use GAATA. An empirical comparison between GAATA and traditional thematic analysis (TA) is
then undertaken. The emergent themes are validated across four dimensions: conceptual mapping,
thematic speci ﬁcity, theoretical alignment, and time ef ﬁciency. GAATA, augmenting gen AI with
structured human oversight, offers a scalable, robust alternative that accelerates and enriches
thematic analysis in market research.
Keywords
gen AI, thematic analysis, prompt engineering, prompt templates, gen AI tool triangulation, gen AI
augmented thematic analysis, GAATA
Introduction
Qualitative research can provide deep insights into consumer behavior, preferences, and perceptions -
critical for developing effective marketing strategies ( Belk, 2013). Traditionally, this has involved
methods such as focus groups, interviews, and ethnographies, all of which demand rigor and
1Faculty of Business, Law & Arts, Southern Cross University, Bilinga, QLD, Australia
*Distinguished visiting professor, University of Johannesburg and senior research fellow, O.P. Jindal Global University.
Corresponding Author:
Michael T. Ewing, Faculty of Business, Law & Arts, Southern Cross University, Southern Cross Drive, Bilinga, 4225, QLD,
Australia.
Email: michael.ewing@scu.edu.au

researcher reﬂexivity throughout data analysis and interpretation. Thematic analysis (Braun & Clarke,
2006), is a widely adopted approach for analyzing qualitative data in marketing (Cooper et al., 2023).
This approach centers on the systematic identiﬁcation, analysis, and subsequent reporting of thematic
structures (patterns of meaning) embedded within qualitative data. The traditional (manual) execution
of TA is both labor-intensive and time-consuming (Nowell et al., 2017). However, the integration of
digital tools into TA allows researchers to handle larger qualitative datasets more efﬁciently, easing the
demands of manual approaches ( Bazeley, 2020; Hitch, 2024).
AI is reshaping the qualitative research domain ( Christou, 2023; Hitch, 2024; Morgan, 2023),
facilitating the systematic storage, retrieval and analysis of vast quantities of data. Thus, leading to
increased attention across severalﬁelds including healthcare (Briganti & Le Moine, 2020; Kanaparthi,
2022) and the application of AI technologies in various contexts including sentiment analysis and
keyword clustering (Chakriswaran et al., 2019). The advent of generative intelligence, however, is a
particularly important advancement for qualitative researchers, representing a departure from previous
applications of AI. Gen AI tools, equipped with capabilities to analyze and generate human-like text,
hold promise for automating and augmenting the data analysis process. With interpretive methods,
researcher bias is a longstanding issue. Although bracketing is a well-established practice for
demonstrating rigor (Creswell & Miller, 2000 ; Tufford & Newman, 2012 ), it has been criticized as
inherently dif ﬁcult and subject to the very biases which it seeks to control ( LeV asseur, 2003).
Qualitative researchers have therefore sought ways to minimize the inﬂuence of their own subjectivity
to preserve the integrity of the phenomenon under study. Others, however, argue that researcher biases
are inseparable from the interpretive process and play a central role within it ( Hirschman, 1986).
Indeed, the process of obtaining insight is embedded in a dynamic relationship between researcher and
data (Hitch, 2024). Thus, despite the technological advances, integration of gen AI into qualitative
market research remains nascent. Signi ﬁcant gaps persist in respect to methodological frameworks
capable of leveraging gen AI tools effectively without compromising the depth of consumer or
marketer insights (Gupta et al., 2024 ; Kshetri et al., 2023 ). Therefore, the purpose of this study is to
introduce and evaluate a structured framework - ‘Generative AI-Augmented Thematic Analysis ’
(GAA TA), which uses gen AI to augment the thematic analysis of qualitative data. It seeks to answer
the question: Can a carefully designed, prompt-based gen AI generate codes and themes that match the
quality of those produced by experienced human analysts?
Literature Review
Gen AI and Qualitative Research
Recent studies have begun to recognize the potential of gen AI in TA ( Katz et al., 2023 ; Yan,
Echeverria, et al., 2023 ; Zhang et al., 2023 ), signifying an opportunity to further explore it ’s ethical
and rigorous use in this context. Recent advancements in gen AI, particularly within the domain of
Natural Language Processing (NLP), offer novel avenues for language inferences such as answering
questions ( Devlin et al., 2019 ). Gen AI tools use large language models (LLMs), trained on vast
datasets (Sallam, 2023; Yan, Sha, et al., 2023), enabling them to produce original content that closely
mirrors human language patterns ( Brown et al., 2020 ; Meng et al., 2023 ). Beyond text generation,
these models are also capable of interpreting context, offering explanations, and assisting in TA
(Amarasinghe et al., 2023 ; Andres Felipe Zambrano, 2023b ). Andres Felipe Zambrano (2023a)
notes that gen AI tools are embedded with extensive pre-trained knowledge and thereby possess the
capacity to identify data patterns that may not be immediately apparent to human cognition; thereby
enhancing manual TA.
Jayawardene and Ewing 163

Gen AI and Thematic Analysis
Ongoing debate surrounds the application of gen AI tools in TA ( Morgan, 2023 ; V an Dis et al.,
2023). The arguments in favor are extensive ( Christou, 2023 ), while criticism broadly centers on
three fundamental themes:
(1) A central critique of using gen AI in TA is the tool ’s ability to comprehend complex human
experiences and social contexts ( Yan, Echeverria, et al., 2023 ; Yan, Sha, et al., 2023 ).
Researchers argue that while gen AI can identify textual patterns, meaning generation is
based on research questions and it lacks the capacity for nuanced insight which is critical for
in-depth TA ( Gebreegziabher et al., 2023 ; Yan, Echeverria, et al., 2023 ). Indeed, con-
textuality and ambiguity, both of which are inherent to human language, remain an ongoing
challenge ( Hitch, 2024 ). Particularly, because the fundamental advantage of qualitative
research methods are that they facilitate the discovery of nuance ( Fischer & Guzel, 2023 ;
Nowell & Albrecht, 2019 ).
(2) The potential for inherent biases in AI algorithms raises concerns about the representa-
tiveness and fairness of the identi ﬁed themes ( Mittermaier et al., 2023 ). These biases might
reﬂect in the themes generated by AI.
(3) In identifying themes, the lack of transparency in data processing potentially undermines
credibility. Transparency is critical to developing a trustworthy understanding of a particular
phenomenon ( Denzin & Lincoln, 2011 ; Patton, 2023 ).
In the following sub-sections, we investigate how humans can employ gen AI tools to augment
qualitative data analysis and thereby address the above limitations. More details on precise miti-
gation strategies are presented in the Approach section.
Prompts: Increasing Human Intervention in Gen AI Data Analysis
Prompts are used to instruct gen AI tools to perform tasks ( Bozkurt & Sharma, 2023). The quality of
prompts determines the response (output) generated by gen AI ( Poola, 2023). A well-crafted prompt
acts as a bridge between the user ’s intent and the tool ’s capabilities, guiding it towards generating
desired outputs that are accurate, relevant, and insightful ( Kan et al., 2023 ).
The following prompt types are described in the literature ( Bello, 2023 ; Ekin, 2023 ; OpenAI,
2024): (1) zero-shot prompting, where responses are entirely based on pre-trained knowledge on the
context of the task; (2) one-shot prompting, where the responses are based on an example provided
in the prompt and then gen AI models generate responses similar to the example; (3) few-shot
prompting, where responses are based on more than one example elaborating how the output should
be generated. Few-shot prompting is useful for tasks that require nuanced responses such as in TA.
Prompt Engineering
Recent studies note that effective use of gen AI varies across domains, and that domain-speciﬁc knowledge
used in prompts is essential for optimizing performance (Tian et al., 2024; Wang & Jin, 2023). Further,
Zhang et al. (2023)argue that prompt engineering should consider the speciﬁc application context to guide
the gen AI tool towards an effective response. The context may include a range of information that varies
from the research goal to the expected structure of the gen AI response. Hence, domain knowledge and
context are essential inputs required by gen AI tools in generating effective responses (output).
164 International Journal of Market Research 68(2)

Best Practices for Prompt Engineering. Gen AI tool developers hold that it is essential to apply speci ﬁc
best practices in prompt engineering. These practices are designed to enhance the clarity, speci ﬁcity,
and overall effectiveness of the prompts, thereby improving gen AI ’s responses ( Huit, 2024 ).
Appendix A synthesizes prompt engineering guidelines based on insights from OpenAI ’s resources
and related expert advice ( Zhang et al., 2023 ).
Reﬂexive Thematic Analysis (RTA)
While many researchers have contributed to developing TA,Liu (2023) argues that an over-emphasis
on structured methodologies has turned TA into a‘bucket ﬁlling’ deductive process, where it should be
a creative and inductive process.Braun and Clarke (2006)is the most frequently cited paper in theﬁeld
of TA1. The authors propose a six-step methodology which they revisit and subsequently update
(Clarke & Braun, 2013 , 2017). They lament how the research community has overlooked the un-
derlying assumptions of their original method, particularly with regard to identifying underdeveloped
themes using domain summaries ( Braun & Clarke, 2019 ). Domain summary themes focus on
summarizing diverse meanings expressed within a speciﬁc topic, where the themes often resemble data
collection questions. In order to to produce domain summaries as themes, Braun and Clarke (2019)
introduced Reﬂexive Thematic Analysis (RTA), that offers a tripartite typology for TA, updating their
earlier method as follows: (i) Coding reliability: Emphasis on replicability of codes - to control for
researcher subjectivity/biases and the reliability of measurement; (ii) Codebook: A codebook is a
ﬂexible, evolving guide used by researchers to document and reﬁne codes as they engage in the coding
process. Unlike structured orﬁxed codebooks used in other thematic approaches, the codebook in RTA
is dynamic and re ﬂects the researcher ’sr e ﬂexive engagement with the data; and (iii) Re ﬂexivity:
Emphasizes the researcher’s active role in identifying themes, acknowledging that coding is inﬂuenced
by the researcher ’s perspectives and insights.
RTA has been widely adopted across various ﬁelds of qualitative enquiry owing to its ﬂexibility
and rigor. The method allows researchers to engage deeply with their data, ensuring that themes are
developed through an iterative process of coding and thematic re ﬁnement. Additionally, RTA ’s
emphasis on re ﬂexivity and the active role of the researcher aligns well with contemporary
qualitative paradigms, making it a popular choice for studies exploring complex social phenomena
(Byrne, 2022 ; Kiger & V arpio, 2020 ).
Research Approach
This study develops a novel gen AI-enhanced RTA methodology using design science research
(DSR) principles. Following Hevner (2007) and V om Brocke et al. (2020), we consider three key
design principles: relevance, rigor and evaluation. Figure 1 illustrates the design rationale un-
derpinning the proposed gen AI-enhanced RTA methodology.
Relevance of the Problem
As highlighted in the introduction, timely decision-making requires rapid analysis of large qual-
itative datasets ( Kaplan & Haenlein, 2020 ). Traditional thematic analysis, involving manual data
immersion and iterative coding —is cognitively demanding, time-consuming, and inef ﬁcient for
large-scale studies (Nowell et al., 2017; Terry et al., 2017). These constraints limit its applicability in
fast-paced environments. Researchers are consequently exploring gen AI tools in pursuit of quicker,
more scalable insights ( Kaplan & Haenlein, 2020 ).
Jayawardene and Ewing 165

Rigor of the Proposed TA Methodology
Gen AI tools can automate coding and theme generation, signi ﬁcantly reducing the time and effort
required for data analysis (Brown et al., 2020). These tools can process large volumes of data swiftly,
maintaining consistency and objectivity in coding, which enhances the reliability of the analysis
(Bhatia et al., 2021 ). Moreover, gen AI-driven TA can uncover deeper patterns and insights that
might be overlooked in manual analysis, providing richer and more nuanced understandings of
qualitative data ( Smith & McGannon, 2018 ). However, it is important to address the limitations of
gen AI too and focus on how they enhance RTA process.
Addressing the Limitations of Gen AI in Qualitative Research
In our literature review, we noted three potential limitations in using gen AI tools in qualitative
research. We now outlined how these can be overcome.
(1) Human experiences and contextual understanding
Few-shot prompting (above) incorporating contextual information within prompts (Ahmed et al.,
2024), can enhance gen AI ’s grasp of complex human experiences. Few-shot prompts can pro-
gressively introduce details to overcome zero-shot prompts ’ lack of context. Human researcher
oversight is crucial, with rigorous review and validation ofall AI-generated codes/themes at each stage.
Figure 1. Design Science Approach for the Study
166 International Journal of Market Research 68(2)

(2) Biases in gen AI algorithms
Employing multiple gen AI tools for data analysis can mitigate bias, i.e., using one tool to generate
initial codes or themes, and a second to validate them. This approach leverages the different LLMs
employed by each gen AI tool, enabling comparative analysis and identi ﬁcation of inconsistencies.
Human review can then rectify any potential biases introduced by the various gen AI algorithms.
(3) Transparency in data processing
Incorporating clear instructions within prompts can enhance transparency. Prompts for code
generation can instruct the gen AI tool to list all excerpts or quotes to create each code, allowing
researchers to manually validate them. Additionally, prompts can specify an analytical framework
(guiding rules) and request evidence from the source data to justify the framework ’s use in gen-
erating results. This enhances transparency and enables researchers to maintain a clear audit trail
which is an established tenet of qualitative rigor.
Gen AI Augmentation to Facilitate Re ﬂexive Thematic Analysis
Gen AI can effectively augment the RTA process by facilitating the three RTA principles proposed
by Braun and Clarke (2019) as follows.
(1) Coding reliability
Few-shot prompts guided by domain concepts and research goals could be used to generate more
reliable and replicable codes using gen AI. Further, coding reliability can be improved by tool
triangulation (using two gen AI tools, as we do).
(2) Codebook development
Few-shot prompts designed with guiding rules for data analysis can serve as a framework to
generate codes/themes. Multiple iterations of the prompts can run until saturation is reached, and the
generated codes/themes can then be compiled into a single document that acts as a codebook.
(3) Re ﬂexive approach
Human involvement is crucial for validating and amending themes/codes generated by gen AI at
each step of the TA process. This ensures human oversight and control, acknowledging the re-
searcher’s critical role in interpreting and analysing the data. In summary, prompt engineering, gen
AI tool triangulation, and human review and validation are the criteria for addressing the limitations
of using gen AI tools in qualitative research.
Design and Evaluation of the Methodology
Gen AI can effectively augment the RTA process when its limitations are properly managed through
prompt engineering, tool triangulation and human validation. We propose GAATA —a gen AI-
augmented TA methodology that supports, rather than replaces, human interpretation while
maintaining reﬂexivity. To evaluate GAA TA, we systematically compared its codes and themes with
Jayawardene and Ewing 167

those from traditional RTA using a multi-criteria framework. Coding agreement was measured using
a ﬁve-step mapping protocol and Cohen ’s Kappa. Themes were compared based on conceptual
overlap, speci ﬁcity, and theoretical alignment. A broader conceptual comparison further assessed
GAA TA’s validity, reliability, and utility.
Gen AI Augmented Thematic Analysis (GAATA)
GAA TA consists of eight distinct step that integrate two gen AI tools to systematically generate,
validate, and re ﬁne eight analytical artefacts 2, thereby conducting Re ﬂexive Thematic Analysis
(RTA) under human oversight. Figure 2 provides an overview of this methodological ﬂow.
GAATA Prompt Templates
GAA TA uses four prompts (P1–P4) to guide the gen AI tools in generating and validating codes and
themes:
P1: Generate codes using gen AI-1.
P2: Rating and validating the codes using gen AI-2.
P3: Generate themes using gen AI-1.
P4: Rating and validating the themes in gen AI-2.
Researchers can tailor the GAA TA process to their study by customising the prompt templates
provided in Appendix A. These templates are intentionally designed to be easily adaptable, requiring
users to replace the blue-highlighted placeholders with research-speci ﬁc details. This design
supports not only expert users but also those with limited experience in generative AI prompting. By
following these structured templates, researchers can apply GAA TA con ﬁdently and rigorously,
without compromising the quality of their thematic analysis.
It is important to note that effective prompting with gen AI does not occur through a single one-
off instruction. Instead, users must engage in an iterative conversation with the AI, requesting
clariﬁcation or re ﬁnement as needed. As described by Ramlochan (2024) , this approach which is
referred to as conversational prompting, involves designing a prompt as a sequence of interrelated
prompts, executed step by step. This method has become increasingly common, as it enables AI
systems to produce more accurate and contextually aligned outputs through follow-up queries.
Accordingly, the prompt templates provided in Appendix A have been intentionally engineered
as conversational prompts. The development of these templates, and the prompt engineering
methodology, forms an integral part of this research and is detailed later under the section Ex-
perimental TA using GAATA.
Code Generation and Validation
GenAI-1 is used to generate initial codes from the source data using prompt P1. These codes are then
reviewed and re ﬁned by human researchers. GenAI-2 then rates the validated codes based on their
relevance to the research goal and their coverage of the dataset —helping to address potential biases
or omissions by GenAI-1. For this task we use Prompt P2. Finally, human researchers conduct
another round of review to produce a re ﬁned and comprehensive list of thematic codes.
168 International Journal of Market Research 68(2)

Figure 2. GAATA (Gen AI-Augmented Thematic Analysis)
Jayawardene and Ewing 169

Theme Generation and Validation
Using the ﬁnalized codes from above, GenAI-1 synthesizes themes using prompt P3. These are
reviewed and amended by researchers, after which GenAI-2 rates the themes based on their rel-
evance to the research goal using prompt P4. This process helps detect any algorithmic bias or gaps.
A ﬁnal human review is then conducted to consolidate and re ﬁne the themes, resulting in a
trustworthy set of ﬁnalized themes.Having described GAA TA in summary, next we explain each step
in detail, using an experimental TA performed using GAA TA. The research goal and dataset used for
the experimental TA is presented in Figure 3. More detail about this experimental TA is provide later
in the manuscript.
Step by Step Guide to GAATA with Illustrations
In TA, codes act as labels that assign meaning to data units, facilitating the identi ﬁcation of patterns
and themes aligned with the research goal (Braun & Clarke, 2019). We use ChatGPT-43as gen AI (1)
and Humata 4 as gen AI (2), however, researchers can select any gen AI tool.
Step 1: Initial Code Generation by Gen AI (1)
As shown in Figure 2, using the provided research data ﬁles, initial codes are generated by gen AI (1)
using the prompt P1. Every code should be relevant to the research goal and supported by data
excerpts (phrases, sentences, or paragraphs) from the input data. Due to the capacity limitations, gen
AI tools produce only a portion of codes at a time. Thus, we need to iteratively instruct gen AI to
Figure 3. Goals of the Experimental TA (4)
170 International Journal of Market Research 68(2)

continue the process of generating more codes until saturation is reached. Hence, in our experimental
TA, we designed P1 as a conversational prompt (see Supplemental Materials ).
P1.1: Instructs gen AI (1) to generate the ﬁrst set of codes
P1.2: Instructs gen AI (1) to generate more codes.
This prompt is used iteratively to generate more codes until gen AI exhibited prolonged inactivity (10 to
15 minutes) indicating a saturation of developing new codes.
P1.3: Instructs gen AI (1) to identify the tool saturation point formally to terminate step 1.
In our experimental TA, Step-1 generated 287 codes. An extract of A-1 is presented inFigure 4due to
space limitations and Full artefact is presented inSupplemental Materialsmaterials-GAA TA-Artefacts.
Step 2: Human Veri ﬁcation of Initial Codes
In step 2, researchers conduct a rigorous review of codes in A-1 and validate each code by conﬁrming
that it has valid excerpts from the source data. The codes lacking valid excerpts should be removed.
This validation removes any inaccurate codes, (1) by misinterpreting the excerpts by gen AI due to lack
of context and domain knowledge; (2) by inferring facts beyond the provided source data due to over-
reliance on general knowledge from training data used by the gen AI tool; or (3) Irrelevant codes to the
research goal generated due to gen AI limitations, errors or anomalies. In the example TA, we removed
Figure 4. Extracts From A-1
Jayawardene and Ewing 171

21 codes based on the above criteria. An extract of A-2 is given in Figure 5 below and the full artefact
with 266 coded is presented in Supplemental Materials-GAA TA-Artefacts.
Step 3: Code Rating and Expansion via Gen AI (2)
Step 3 aims to mitigate potential biases and limitations in gen AI algorithms, ensuring that all relevant
codes have been identi ﬁed from source data. Here, we follow the sub-steps below (see Figure 6).
Figure 5. Extracts From A-2
Figure 6. Four Steps of Step 3
172 International Journal of Market Research 68(2)

3.1: Measures the quality of gen AI (1) generated codes by using gen AI (2). P2 instructs gen AI (2) to rate
the codes, based on their relevance to the research goal assigning a rating from 0 to 10, based on each code ’s
relevance to the research goal, with 0 indicating the least relevance and 10 the most. P2 template is available
in Appendix A
3.2: Due to the limitations of gen AI (1), there is a possibility that it did not generate all the possible codes
available in source data in task-1. Hence, we use gen AI (2) to generate additional unique codes not included
in A-2. For this, prompt P1.2 is used with gen AI (2).
3.3: The additional unique codes generated in the above step using gen AI (2), are then rated using gen AI (1)
with P2 to ensure that they are relevant to the research goal.
3.4: The researchers combined the two sets of rated codes developed in sub-steps 3.1-3.3 to develop A-3.
When a study involves multiple research goals (sub-step 1), each goal is treated as a separate
rating dimension. In such cases, each code receives a distinct score for each objective.
In the experimental TA, we used Humata in sub-steps 1 and 2 and ChatGpt-4 in sub-step 3. The
adapted prompts used in every step is provided in the Supplemental Materials . Humata produced
16 additional codes, and they were in turn rated by ChatGPT-4. An extract of A-3 in the example TA
is provided in Figure 7, and the full artefact of 282 codes is presented in Supplemental Materials -
GAA TA-Artefacts.
Step 4: Human Re ﬁnement and Thematic Code Finalisation
In step 4, the rated list of codes in A-3 undergo a rigorous review by the researchers, such that codes
with zero rating are removed, and codes with ratings between 0-5 are examined by the researchers
and a decision made to exclude or improve them. As Boyatzis (1998) argues, considering both
semantics and pragmatics allows for the development of codes that are not only descriptive but also
explanatory, facilitating the identiﬁcation of complex patterns and themes that might be missed in a
more super ﬁcial analysis.
All relevant codes that remain are re ﬁned into comprehensive thematic codes with suitable
wording changes based on semantics and pragmatics. Step 4 enhances the analysis ’s validity and
Figure 7. Extract From A-3
Jayawardene and Ewing 173

reliability by fostering a more comprehensive interpretation of the codes ( Nowell et al., 2017 ). An
extract of A-4 produced in experimental TA is given in Figure 8 and the full artefact of 226 codes is
presented in Supplemental Materials. Both gen AI tools produced 303 codes - out of which 56 (18%)
were eliminated by human reviews. Changes were made to majority of the remaining codes to
convert them to comprehensive thematic codes.
Step 5: Initial Theme Synthesis via Gen AI (1)
This ﬁfth step used gen AI (1) to generate themes from the validated codes using the prompt P3 as a
single prompt to generate the themes. Constructi ng themes involves iterat ively interpreting and
synthesizing coded data into broader, meaningful patterns that addressed the research question
(Braun & Clarke, 2006 , 2019). Hence, we argue that the codes with high rating should be given
priority in generating meaningful patterns in synthesising more relevant themes to the research
goal. Themes should be internally coherent and clearly distinct from each other, ensuring that they
capture unique aspects of the data ( Patton, 2023 ). This principle helped to maintain the integrity of
each theme, avoiding redundancy. Themes should be linked to the original codes used to create
them, allowing researchers to trace them back to the original excerpts from the source data.
Themes can be grounded on existing theories, particularly in the case of deductive TA ( Sinclair-
Maragh & Simpson, 2021 ) where the codes are synthesized using domain speci ﬁc theoretical
frameworks, pre-existing classi ﬁcations available in the domain or classi ﬁcations based on re-
searchers’ expertise ( Tuckett, 2005 ). In the experimental TA, our goal was to identify the
pedagogical impacts of technology integration in marketing education. We grounded the ﬁndings
in TPACK ( Koehler et al., 2013 ), a well-established theoretical framework for technology-
integrated pedagogy. TPACK emphasizes the intersection of content knowledge (CK), peda-
gogical knowledge (PK), and technological knowle dge (TK) as essential for effective teaching.
T h eP 3t e m p l a t ei nAppendix A was developed based on these four core principles and is included
in the Supplemental Materials . In the experimental TA, 16 themes were developed, and an extract
of A-5 is given in Figure 9 . The full set of themes are provided in the Online Supplemental
Materials -GAA TA-Theme generation.
Figure 8. Extract From A-4
174 International Journal of Market Research 68(2)

Step 6: Human Veri ﬁcation of Initial Themes
Researchers review themes and check whether they adequately represent their underlying codes. If any
inconsistencies exist, they can be re ﬁned at this stage. In our TA example, researchers reviewed the
16 themes and concluded that each theme represents their underlying codes - in line with the research
goal. Thus, they did not have to amend the list. In the experimental TA the 16 themes were reviewed by
the researchers and conﬁrmed that they represent the underlying codes - hence no changes were required.
Step 7: Rating Themes in Gen AI (2)
This step aimed to mitigate potential biases in gen AI algorithms generating themes. The three sub-
steps reﬂect what we performed in step 3 for codes. Sub-step 7.1 instructs gen AI (2) to rate the themes
in A-6, indicating the relevance of the gen AI (1) generated themes compared with the research goal
and the theoretical frameworks integrated in theme generation in step 6. Themes are rated from 0 to 10,
based on relevance to the research goal: 0 being the least relevant and 10 the most relevant. This sub-
step uses the prompting template P4 to instructs gen AI (2) to rate the themes. Sub-step 7.2 is to instruct
gen AI (2) to generate additional unique themes not listed in A-6, ensuring the completeness of the gen
AI (1) generated themes. Template P3 is adapted and used to instructs gen AI (2) to generate additional
unique themes. The artefacts A-6 and A-4 (codes provided to gen AI (1) in step 5) are used as input
data in this step. In sub-step 7.3, if additional unique themes were generated by gen AI (2) in 7.2, gen
AI (1) rate them using the P4 with the same evaluation criteria as in 7.1. Finally, the researchers
Figure 9. Extract From A-5
Jayawardene and Ewing 175

compile a consolidated list of rated themes by combining outputs of sub-steps 7.1 and 7.3 above. In
7.1, when the study involves multiple research goals, each goal is treated as a separate rating di-
mension. In such cases, each theme receives a distinct score for each research objective.
In the experimental TA, in sub-step 7.1, Humata rated all 11 themes pertaining to the given rating
criteria. In sub-step 7.2, Humata generated ﬁve additional themes; and in sub-step 7.3, ChatGPT-4
rated the ﬁve new themes. Thus A-7 consisted of 16 themes. Ratings for each theme in A-7 had a
value of 7 or above, indicating a higher relevance to the research question. A-7 sample is given in
Figure 10 . More details in Online Supplemental Materials -GAATA-Theme generation.
Step 8: Human Validation of Themes
After the researchers thoroughly reviewed A-7, along with its underlying codes, themes with low ratings
(<5) are investigated along with their codes and removed or retained - depending on researchers ’
judgement. Overlapping themes were identiﬁed and necessary consolidations made based on researchers’
expertise– coupled with gen AI driven insights where appropriate. Theme deﬁnitions and descriptions are
improved and enriched by the researchers, using their expertise and gen AI-driven in sights where
necessary.Appendix A provides two simple prompts to support the above. In the experimental TA, the
researchers discussed theirﬁndings and concluded that all additionalﬁve themes generated by Humata
were in fact sub-themes of the original 11 themes generated by ChatGPT-4. More details of this con-
solidation are contained in the Online Supplemental Materials- GAA TA-Theme generation.
Finally, the researchers collaboratively enrichedthe themes by introducing more appropriate wording
and strengthening the themes with more speciﬁc domain concepts from the marketing discipline. For this
exercise, the researchers used the gen AI-driven insights in collaboration with their expertise. The prompts
used to enrich themes are listed inAppendix A. An extract of the enriched themes is provided inFigure 11.
Figure 10. Extract From A-7
176 International Journal of Market Research 68(2)

In this step, the researchers ’ expertise shaped the ﬁnal themes, ensuring they were duly informed
by researche rs ’ domain knowledge, their active role in the process, and their perspectives and
insights, as emphasized by RTA ( Braun & Clarke, 2019 ). Final themes are available under Online
Supplemental Materials -GAA TA-Final-themes.
Managing the Artefacts (A1-A8) in GAATA
To implement GAA TA, researchers must manage a sequence of evolving artefacts (A1 –A8)
throughout the process. Gen AI outputs are typically copied or exported into Word or Excel ﬁles,
which serve as working artefacts for validation and re ﬁnement. For instance, codes from step 1 are
reviewed in Word (A1) and re-used in step 2. When multiple or iterative ﬁles are created, researchers
consolidate them manually. For projects involving sensitive data, we recommend anonymizing
content and using local or secure AI platforms to ensure con ﬁdentiality.
Experimental TA Using GAATA
This section presents an experimental TA conducted using GAA TA. The experiment served two
purposes: (1) it informed the development of the prompt templates included in Appendix A, and (2)
it enabled a structured comparison between GAA TA-generated codes and themes and those pro-
duced through traditional RTA, allowing us to assess GAA TA ’s methodological reliability.
Figure 11. Extract From Finalized Themes
Jayawardene and Ewing 177

Engineering Prompt Templates for GAATA through an Experimental TA
As outlined above, GAA TA uses four tailored prompts to guide gen AI tools in data analysis. This
section introduces the development process of those prompt templates —a central methodological
contribution of this study.
In this experiment, we applied GAA TA to a data set of marketing journal papers published
between (2010-2024) with the aim of exploring the pedagogical impact of technology integration in
marketing education (see Figure 3 above). The two authors engineered the required prompts for each
step drawing on established prompt engineering best practices (see Appendix A). One author being
an expert in prompt engineering and the other, an expert in marketing domain, but with a good
understanding of gen AI prompts involved in this task. We identi ﬁed ﬁve key elements essential for
all few-shot prompts to align with GAA TA ’s analytical goals:
(1) Task: A concise explanation of the analytical objective, helping orient the AI tool ( OpenAI,
2024; Zhao et al., 2023 )
(2) Research goal : Researchers have emphasized that the data should be analyzed relative to
the research goal ( Boyatzis, 1998 ; Braun & Clarke, 2006 ; Nowell et al., 2017 ). Hence,
including the research goal within the prompt ensures that the AI aligns its output with the
analytical intent.
(3) Input data: All prompts must clearly identify the source data to be analyzed. This includes
providing access to the data either as a linked external ﬁle or appended text. Additionally, the
prompt should specify the structure or format of the data, as understood by the researchers,
so the AI can process it accordingly.
(4) Data analysis instructions: Detailed, step-by-step instructions should be included to guide
the AI ’s analytical approach ( White et al., 2023 ). These instructions include:
· Relevant theories, domain knowledge, or contextual cues;
· Requirements for transparency and traceability, e.g., instructing the AI to list and
categorize source excerpts under each generated code, along with justi ﬁcations.
(5) Expected Output : The format and structure of the desired output should be speci ﬁed,
including examples where appropriate, to help the AI produce results that are usable and
aligned with the research design ( OpenAI, 2024 ).
These ﬁve elements were then operationalized through a six-step structured prompt engineering
process ( Figure 12 ) as outlined below, ensuring prompts were systematically designed, iteratively
tested, and re ﬁned for quality.
(1) Initial prompt design: Each researcher independently drafts prompts incorporating the ﬁve
elements.
(2) Prompt review: They exchange drafts, independently critique them, and provide feedback.
(3) Consolidated prompt design : The researchers reconcile feedback to co-develop a single
reﬁned prompt.
(4) Testing the prompt in the gen AI tool : The consolidated prompt is trialed with actual data
to generate AI outputs (output).
(5) Response review: If the result meets quality criteria (e.g., clarity, accuracy), the prompt is
approved. If not, proceed to step 6.
(6) Prompt update : Researchers collaboratively re ﬁne the prompt using best practices
(Appendix A ) then return to step 4. This cycle continues until the response is satisfactory.
178 International Journal of Market Research 68(2)

This process was executed separately for each of prompts P1–P4, all of which were then successfully
deployed within GAA TA to generate and validate codes and themes. All outputs were manually re-
viewed for accuracy and theoretical integrity. Following validation, theﬁnal prompts were converted into
general-purpose templates to support novice resea rchers. These adaptable templates are provided in
Appendix A and recommended as a starting point for research-speciﬁc customization. Next, using the
outcomes (codes and themes) of experimental TA, we conducted an empirical evaluation of GAA TA.
Figure 12. Designing Prompt Templates for GAATA (5)
Jayawardene and Ewing 179

Empirical Evaluation: Traditional RTA vs GAATA
To robustly assess the reliability of GAA TA, we conducted a full manual thematic analysis on the
same dataset used in the experimental TA conducted using GAA TA. Two experienced qualitative
researchers5, H and L (neither being co-authors), independent of the GAA TA development process,
manually analyzed the entire dataset using re ﬂexive thematic analysis (RTA) principles ( Braun &
Clarke, 2019). They developed codes and themes through iterative reading, coding, and synthesis,
with discrepancies resolved through discussion. The manual TA results (codes and themes) were
considered as the benchmark and GAATA results were compared against the benchmark. Next, we
present the comparison of the manual TA codes with GAA TA codes ( Tables 1 and 2).
Validation of Codes Using Inter-rater Reliability
GAA TA produced 226 codes, and the manual TA produced 166 codes. Considering the manual TA
codes as the benchmark, we analytically compare the two sets of thematic codes. To ensure consistency
in comparison, we employed a rigorous ﬁve-step code mapping and reliability checking protocol
designed based on Cohen’sK a p p a(Cohen, 1960), calculated using a confusion matrix (Carletta, 1996).
1. Code normalization
All codes from both GAATA and manual TA were normalized to remove super ﬁcial linguistic
variations. This included converting codes to lowercase, eliminating stop words, and stan-
dardizing synonyms (e.g., “student satisfaction ” vs. “learner satisfaction ”).
2. Align the codes based on excerpts
We matched excerpts from manual TA and GAA TA, using either exact matches (same excerpt is used
by both codes), or fuzzy matching - when excerpts conveyed the same core meaning despite minor
linguistic or structural differences (e.g.,“AI for customer service” and “Customer support via artiﬁcial
intelligence”).This process developed a code mapping table which is available under Supplemental
Materials- Code-validation.xlsx. A sample of the table is presented below for illustration purposes
(Table 1).
In this analysis, we observed that every manual TA code matched with one or more GAA TA
codes. Also, there were 16 GAATA codes that did not match with any manual TA codes,
suggesting the potential for GAA TA to identify novel patterns.
Table 1. Excerpt Based Code Mapping Table
Excerpt Manual TA code GAATA code
Q1 Practice virtual merchandising Virtual merchandising using VR tools
Q2 AI based data analytics Marketing analytics using AI tools
Introducing AI for data analytics
Q3 Social media as a collaborative tool in classroom Using social media in collaborative learning
Q4 VR based practicals VR based experiential learning
Q5 No matching code Adaptive learning with online tools
180 International Journal of Market Research 68(2)

3. Assigning shared conceptual code categories (SCCC) for code pairs
For each matching code pair , the independent researchers (H & L) collaboratively assigned a
SCCC to represent both codes. Each SCCC represents an abstracted pedagogical concept that
captures the underlying meaning common to both the manual and GAA TA-generated codes. This
strategy aligns with established qualitative research practices that advocate grouping codes into
higher-order categories to facilitate pattern recognition and thematic development ( Ryan &
Bernard, 2003 ; Saldaña, 2021 ). In the case of one-to-many mapping, the same SCCC was
repeated across the rows. Also, for non-match codes we did the same using the code itself as the
conceptual category ( Supplemental Material - Code-validation.xlsx). A sample of the output is
presented below in Table 2.
4. Aligning the shared conceptual categories and constructing a confusion matrix
Next we constructed a confusion matrix - to evaluate the agreement between two coding
methods – useful in assessing the reliability of classi ﬁcation tasks in computational linguistics
(Carletta, 1996). This matrix serves as the foundation for calculating Cohen ’s Kappa, a measure
of inter-rater reliability ( Cohen, 1960 ). The confusion matrix displays the frequency of rater
reliability in a matrix of SCCC, with diagonal entries representing agreements and off-diagonal
entries indicating disagreements (see Table 3).
The application of confusion matrices in th ematic coding has been well-documented.
Garc ´ıa-Balboa et al. (2018) discuss the role of confusion matrices in evaluating thematic
accuracy in geographic data, highlighting their relevance in various domains. These studies
underscore the confusion matrix ’s critical role in ensuring the validity and reliability of
coding schemes across different research contexts. The full confusion matrix is available in
Supplemental Materials -Manual-VS-GAA TA-code-maping.xlsx and a sample is provided
in Table 4 for illustrative purposes.
5. Kappa Scoring.
Based on the ﬁnal confusion matrix, the total number of observations was 240, with 226 exact
matches along the diagonal ( Supplemental Material -Confusion Matrix-Cohens-Kappa). This
yielded a Cohen ’s Kappa score of 0.9417. According to accepted benchmarks ( Landis & Koch,
Table 2. Assigning Conceptual Code Categories
Manual TA code GAATA code
Shared conceptual code category
(SCCC)
Practice virtual merchandising Virtual merchandising using VR
tools
Virtual merchandising
AI based data analytics Marketing analytics using AI tools AI analytics
Introducing AI for data analytics AI analytics
Social media as a collaborative tool in
classroom
Using social media in collaborative
learning
Collaboration via social media
VR based practicals VR based experiential learning VR based experiential learning
No matching code Adaptive learning with online tools Tool based adaptive learning
Jayawardene and Ewing 181

Table 3. Confusion Matrix
GAATA: Virtual
merchandising
GAATA: AI
analytics
GAATA:
Collaboration via
social media
GAATA: VR-based
experiential learning
GAATA: Tool-
based adaptive
learning
GAATA:
Codes not
matching
More
categories
Manual TA: Virtual
merchandising
10 0 0 0 0
Manual TA: AI analytics 0 2 00 0 0
Manual TA:
Collaboration via
social media
00 1 0 0 0
Manual TA: VR-based
experiential learning
00 0 1 0 0
Manual TA: Tool-based
adaptive learning
00 0 0 0 1
Manual TA: Codes not
matching
00 0 0 0 0
More categories
182 International Journal of Market Research 68(2)

1977), this indicates an ‘almost perfect ’ level of agreement, validating the alignment between
GAA TA and manual TA codes. The Kappa calculation was implemented using a custom Python
script developed for this study. The script is available in Online Supplemental Materials -Python
script. This validation process strengthens the empirical support for GAA TA by demonstrating
high consistency with human interpretation.
Validation of Themes
To enable a systematic comparison of themes generated through the two different analytical
processes, four key dimensions were adopted from established literature in qualitative research.
These criteria provided a structured lens through which the thematic outputs could be examined for
clarity, depth, and theoretical alignment. The methodology consisted of four sequential steps,
drawing on established practices in qualitative research and educational theory. The same two
coders, H and L, involved in the manual TA conducted this analytical process.
Dimension 1: Conceptual Mapping via Shared Conceptual Code Categories (SCCC). Here we assessed the
degree of conceptual alignment between GAA TA and manual themes using shared conceptual
categories as an intermediary. A mediated mapping approach by two coders was used to identify
conceptual overlaps. First, each theme (manual and GAA TA) was associated with one or more
shared conceptual categories derived from prior code-level mappings (e.g., Reﬂective Learning ,
Gamiﬁcation, Data Analytics ). A theme-to-theme alignment matrix was then constructed, classi-
fying matches as:
· Exact Match – strong overlap in codes due to 3 or more exact matches of SCCC
· Partial – one or more SCCC overlapping but with differences in emphasis, scope, or focus
(e.g., a manual theme focusing broadly on “Technology Use ” and a GAA TA theme spe-
ciﬁcally on “Mobile Learning Tools” might be a partial match if both share an SCCC related to
“digital learning ”)
Table 4. Summary of Theme Validation
Manual
themes
GAATA
themes
Conceptual mapping between
manual and GAATA themes
Thematic speci ﬁcity and
focus
Manual
theme
TPACK
alignment
Manual
theme
GAATA
theme
GAATA
theme
M-Thm-1 G-Thm-5 Exact match Moderate High Strong Strong
M-Thm-2 G-Thm-7 Exact match Moderate High Strong Strong
M-Thm-3 G-Thm-11 Exact match High High Strong Strong
M-Thm-4 G-Thm-1 Exact match Moderate High Strong Strong
M-Thm-5 G-Thm-3 Exact match High High Moderate Strong
M-Thm-6 G-Thm-6 Exact match High High Strong Strong
M-Thm-7 G-Thm-9 Exact match High High Strong Strong
M-Thm-8 G-Thm-4 Exact match High High Strong Strong
M-Thm-9 G-Thm-10 Exact match High High Strong Strong
M-Thm-10 G-Thm-2 Exact match High High Strong Strong
G-Thm-8 No match N/a High N/a Strong
Jayawardene and Ewing 183

· None – no shared SCCC alignment
A theme comparison matrix indicating match type, shared categories, and alignment notes. This
method supports analytical triangulation and deeper cross-method validation ( Braun & Clarke,
2006; Jick, 1979 ; Nowell et al., 2017 ).
Dimension 2: Thematic Speciﬁcity and Focus. According to Braun and Clarke (2006) qualitative themes
should be clearly bound, conceptually coherent, and analytically useful. Each theme was assessed
based on its clarity of focus, internal consistency among supporting codes, and the absence of
conceptual sprawl. Themes were then categorized as having high, moderate, or low speci ﬁcity. The
independent coders (H & L) conducted this assessment and reached consensus on the rating for each
theme through discussion and comparison against pre-de ﬁned examples.
· High – distinct and well-bounded (e.g., AI-Enhanced Critical Thinking)
· Moderate – coherent but broad (e.g., Technology in Education)
· Low – vague or overly general (e.g., Student Engagement )
The above draws on Braun and Clarke’s (2019) recommendations for thematic rigor in qualitative
research.
Dimension 3: Theoretical and Pedagogical Alignment (TPACK Framework). This step assessed the
theoretical and pedagogical alignment of each theme using the TPACK framework ( Koehler et al.,
2013). Each theme (manual and GAA TA) was analyzed to determine the extent to which it in-
corporated all three dimensions. The rating levels assigned and agreed upon by the independent
researchers,
· Strong alignment – all TPACK domains present
· Moderate alignment – two domains evident
· Weak alignment – one or none explicitly addressed
This theoretical lens ensures that emerging themes reﬂect meaningful educational integration, not
merely technological adoption ( Koehler et al., 2013 ).
Dimension 4: Comparison of Time Utilization. To empirically assess GAA TA’se f ﬁciency, a critical
dimension for its practical application, the time dedicated to each phase of both the GAA TA-driven
experimental thematic analysis and the equivalent manual thematic analysis conducted by H and L
was meticulously recorded and analyzed.
Theme Validation Results
The full analytical validation is available under Supplemental Materials - GAA TA_vs_Ma-
nual_Theme_Comparison.xlsx and Table 5 provides a summary of the validation.
Conceptual mapping. Out of eleven GAA TA-generated themes, ten showed direct conceptual
alignment with their corresponding manual the mes, indicating strong t hematic convergence.
One theme (G-Thm-8), however, revealed a conceptual divergence, suggesting the emergence
of a novel construct not identi ﬁed through human-led analysis. (G-Thm-8: Challenges in
184 International Journal of Market Research 68(2)

Technology-Integrated Marketing Education: Navigating Negative Perceptions and Peda-
gogical Strain)
This discrepancy may stem from the differing epistemological orientations of manual and AI-
assisted approaches. Human coders, even in RTA, often unconsciously adhere to positivist
tendencies—favouring observable patterns —due to cognitive biases and a preference for empirical
certainty ( Guba & Lincoln, 1994 ; Tversky & Kahneman, 1974 ). These biases can limit the
identiﬁcation of more abstract or latent themes.
In contrast, GAA TA operates without such cognitive constraints, enabling it to detect nuanced
semantic patterns across large datasets. Its algorithmic processing can surface insights that might
elude human analysts due to data volume or the subtleties of pattern recognition ( Hwang & Wu,
2025). The unique theme produced by GAA TA demonstrates its potential to complement and extend
human interpretation by uncovering deeper layers of meaning and broadening the analytical horizon
(Jucker et al., 2013 ).
Thematic Speci ﬁcity. All eleven GAA TA themes were rated high in speci ﬁcity, indicating tightly
bound, well-articulated constructs. Seven (of ten) manual themes received a high rating, with others
assessed as moderate. This suggests that GAA TA produces themes with greater conceptual
sharpness and less thematic diffusion. The use of large language models in GAA TA likely con-
tributes to its ability to synthesize patterns across vast textual input, leading to more delineated
thematic structures ( Blei, 2012 ; Devlin et al., 2019 ).
Theoretical and Pedagogical Alignment. All GAA TA and manual themes were rated asstrong, showing
a high level of theoretical conformity, af ﬁrming its relevance for pedagogical inquiry. In this section
we presented conceptual and empirical evaluations of GAATA against traditional TA. The ﬁndings
collectively suggest that GAA TA is a viable alternative for manual TA and a potentially superior
method in thematic contexts within qualitative research.
GAATA vs Manual TA: Time Utilization
Here we present a comparison of the time taken to conduct each phases ( Braun & Clarke, 2006 ,
2019) in manual TA and equivalent GAA TA phases.
Aa above, GAA TA takes less than a third of the time of manual TA. It should be noted that this
timing is for analysis of 213 abstracts of journal articles. Manual TA could comparatively take more
time than GAATA when analysing large datasets due to the human fatigue, leaving GAA TA a
Table 5. Comparison of Time Utilization - Manual TA vs GAATA
Manual step Time GAATA step Time
Familiarisation 7 hrs Prompt design using templates 2 hrs
Initial coding 23 hrs AI code generation + rating (Phase 2) 2 hrs
Human review of codes (Phase 2) 9 hrs
Theme generation 19 hrs AI theme generation + rating (Phase 3) 1 hour
Reﬁnement and review 14 hrs Human review of themes (Phase 3) 7 hrs
Write-up of themes 8 hrs Write-up of themes with AI support 1 hr
Total time 71 hrs 22 hrs
Jayawardene and Ewing 185

preferred alternative in domains like marketing which has severe time constraints (online customer
feedback analysis etc).
Conceptual Evaluation: Traditional RTA, AI-Only TA, and GAATA
In addition to the empirical validation conducted against traditional RTA, we also performed a
conceptual comparison between GAA TA, traditional reﬂexive thematic analysis (RTA), and AI-only
TA where the latter representing fully automated approaches that depend exclusively on AI-
generated outputs with no human intervention.
Table 6 presents a comparative summary of the three approaches across key dimensions relevant
to qualitative research, namely time ef ﬁciency, thematic depth, reliability, transparency, scalability,
and re ﬂexivity.
Table 6. Comparative Features of Traditional TA, AI-Only TA, and GAATA
Dimension Traditional TA AI-only TA GAATA (Proposed)
Time ef ﬁciency Low – requires manual
coding, theme
development, and
iteration through multiple
data cycles
High – full automation
drastically reduces time
demands
High – prompt templates, tool
integration, and automation
signiﬁcantly reduce time
across coding and theme
development phases
Thematic depth High – inductive and
interpretive processes
allow for rich and
nuanced insights
Variable – may miss
contextual cues and
deeper meanings without
human interpretation
High – human validation and
reﬂexive synthesis ensure
depth while AI accelerates
data parsing and theme
abstraction
Reliability Moderate – inter-coder
reliability varies;
outcomes susceptible to
individual bias and
interpretive drift
Low to moderate – depends
on prompt quality; lacks
oversight to detect or
correct biased or
irrelevant outputs
High – multi-tool triangulation,
structured prompt
engineering, and iterative
human validation enhance
the rigour and
reproducibility of ﬁndings
Transparency/
Audit trail
Moderate – audit trails
depend on manual
documentation quality
and researcher diligence
Low – black-box nature of
LLMs and limited
traceability hinder
methodological
transparency
High – GAATA produces
artefact-based
documentation (A1 –A7),
enabling transparent, step-
by-step traceability and
veriﬁcation
Scalability Low – time and labour
constraints limit
applicability to large
datasets
High – can handle large
datasets instantly but may
lack meaningful synthesis
High – combines automation
for scale with human
oversight to maintain
analytical quality, enabling
both breadth and depth in
large qualitative datasets
Reﬂexivity High – researcher’s
interpretive stance and
contextual knowledge are
central to the process
None – AI operates
independently, without
introspection or
adaptation to research
context
High – human researchers
remain actively involved
throughout all phases,
ensuring critical reﬂexivity in
shaping and validating AI-
generated codes and themes
186 International Journal of Market Research 68(2)

This comparative framework illustrates GAA TA ’s distinct position as a hybrid methodology,
strategically integrating the strengths of both human-led and AI-driven approaches. Unlike AI-only
TA, GAA TA maintains methodological transparency, contextual sensitivity, and human reﬂexivity,
while offering signi ﬁcant ef ﬁciency and scalability gains beyond what is achievable through
traditional RTA.
By leveraging prompt engineering, dual-tool triangulation, and structured human vali-
dation, GAA TA delivers a scalable, ef ﬁcient, and rigorously controlled TA process, making it
particularly well suited for da ta-intensive and time-sensitiv e contexts such as marketing
research.
Additional Empirical Validation: Applying GAATA to Consumer Data
To validate GAA TA ’s methodological robustness beyond controlled academic contexts, the
framework was applied to an empirical corpus of airline customer feedback, comprising passenger
reviews sourced from commercial airline platforms (each containing detailed narratives of travel
experiences, complaints, and post- ﬂight re ﬂections). These authentic, emotionally charged, and
linguistically diverse narratives provided an ideal foundation for testing GAA TA’s capacity to extract
meaning from naturally occurring consumer data.
Research Goal: To Identify Key Drivers of Customer Dissatisfaction and Service Experience Gaps in the
Commercial Airline Industry. GAATA identiﬁed 110 codes and 13 themes aligning with the research
goal. Table 7 presents the summary of the themes, and the full analysis is provided under
Supplemental Materials due to space limitations of the manuscript.
Collectively, these thirteen themes form a multidimensional map of customer dissatisfaction,
spanning from macro-level systemic issues (e.g., operational inef ﬁciency, policy rigidity) to micro-
level service experiences (e.g., slow boarding, staff indifference). GAA TA demonstrated strong
alignment with human-coded validation, conﬁrming its capability to uncover semantically coherent,
theoretically grounded patterns of meaning.
Table 7. Themes Generated From Airline Customer Feedback
Themes
1 Service recovery failure and unresponsive complaint management
2 Operational inef ﬁciency and disrupted travel experience
3 Staff attitude, empathy, and passenger care de ﬁciencies
4 Poor physical environment and on-board comfort
5 Unmet service promises and downgraded value experience
6 In- ﬂight and ground-service quality de ﬁciencies
7 Accessibility and passenger support limitations
8 Unreliable booking, check-in, and digital service systems
9 Emotional disengagement and loss of trust
10 Systemic failures in baggage management
11 Policy and service rigidity in response to disruption
12 Health and medical care de ﬁciencies
13 Inef ﬁcient service execution and ﬂow
Jayawardene and Ewing 187

Discussion
The GAA TA methodology signiﬁcantly advances traditional TA by leveraging gen AI to augment
reﬂexive TA, ensuring the active involvement of human researchers in every step. GAA TA sig-
niﬁcantly reduces the time required for initial code and theme generation – freeing researchers ’
cognition for higher-level analysis and enabling them to analyze larger datasets more ef ﬁciently.
GAA TA addresses the limitations of using gen AI for qualitative data through three enablers: prompt
engineering, tool triangulation, and human validation.
GAA TA is a comprehensive process for designing high-quality and structured prompts which
deﬁnes ﬁve mandatory elements to account for the unique attributes of each research question,
thereby specifying data analysis instructions to gen AI tools. GAA TA actively integrates researchers’
expertise into the prompt design and validation phases, ensuring that AI-generated outputs are
grounded in domain-speci ﬁc knowledge. Prompt templates developed in this study ( Appendix A )
based on experimental TA, serve as adaptable templates for any TA, ensuring effective instructions
for gen AI tools for conducting a TA. Hence, researchers with limited experience in prompt en-
gineering can use these templates by customizing them to their own research goals.
Second, GAA TA employs a triangulation strategy to eliminate the bias in codes/themes generated
by one gen AI tool through a rating process using a second gen AI tool. Triangulation is also used to
mitigate the limitations of gen AI tools and to eliminate subjective human interpretations of data.
Third, human validation remains a cornerstone of GAA TA, ensuring the human element prevails by
keeping researchers in the loop iteratively. This fosters a reﬂexive TA approach in which researchers
critically examine their interpretations ( Braun & Clarke, 2006 ). Continuous human validation en-
hances the credibility of generated codes and themes by identifying potential inconsistencies.
The intermediate artefacts (A1 to A7) maintain detailed documentation of each step, like a
codebook in RTA, reﬂecting the transparency and validity of data analysis. The underlying LLMs in
gen AI tools have an extensive repository of knowledge that surpasses human cognitive capabilities.
GAA TA leverages this vast knowledge base to enhance the quality of results, particularly in the
development of ﬁnalized themes, achieving a level of insight unattainable by human efforts alone.
While gen AI has many strengths with regards to qualitative data analysis, it is important to
acknowledge that LLMs in AI tools are limited in their ability to access latent meanings. These
include symbolic references, emotional undertones, or context-speci ﬁc subtexts that are often
evident only through deep cultural familiarity or prolonged researcher immersion ( Franken &
Ve pˇrek, 2025). Further the extensive knowledge in LLMs can infer things beyond the given data and
include them in the analysis.
Moreover, there is a risk of over-reliance on AI-generated insights, particularly when researchers
adopt outputs without suf ﬁcient critical review. AI may reproduce dominant discourses encoded in
training data and may underrepresent marginalised perspectives or subtle divergences in meaning
(Passi & V orvoreanu, 2022 ).
GAA TA mitigates these concerns by integrating structured human validation at each phase,
ensuring that gen AI serves as an assistant not a substitute for interpretation. In the templates
provided with GAATA, we have provided instructions to mitigate these problems, giving users the
ﬂexibility to include further instructions to handle the above problems depending on the nature of the
domain. Researchers are encouraged to remain re ﬂexive, apply theoretical frameworks critically in
the templates, and triangulate AI outputs with domain expertise and contextual judgment.
Finally, our comprehensive evaluation demonstrates that GAA TA can generate high-quality
themes comparable to those produced through expert-led manual TA. Drawing on both theoretical
analysis and empirical validation, including high code alignment (Cohen ’s Kappa = 0.94), strong
188 International Journal of Market Research 68(2)

thematic convergence, and signi ﬁcant gains in ef ﬁciency—our ﬁndings suggest that GAATA is not
only a feasible alternative but, in many respects, a superior method for researchers working with
large qualitative datasets in time-sensitive and resource-constrained environments like marketing.
Theoretical and Practical Implications
The experimental TA presented here adopts a deductive approach, using the pre-existing TPACK
framework to guide the analysis, thus ensuring that the generated themes are contextually relevant
and theoretically sound ( Koehler et al., 2013 ). Traditionally, such moderation requires signi ﬁcant
cognitive effort. GAA TA leverages gen AI to automate this moderation within a deductive TA
framework, signi ﬁcantly reducing researchers ’ workload.
Conversely, GAA TA could also facilitate inductive TA, a data-driven approach in which themes
emerge organically from the data. By omitting theoretical frameworks from the data analysis in-
structions in prompts, researchers could allow gen AI to explore the data freely, aligning it with the
inductive approach ( Guest et al., 2011 ). This would foster a more exploratory and potentially
nuanced analysis.
The advent of gen AI has created new avenues for enhancing the ef ﬁciency and accuracy of
qualitative market research. Gen AI tools, equipped with capabilities to analyze and generate human-
like text, offer the potential to automate and augment the data analysis process, thus addressing the
traditional challenges of scale and subjectivity (Kaplan & Haenlein, 2020). Despite these technological
advances, the integration of gen AI into qualitative market research is still nascent. Signi ﬁcant gaps
exist in respect of methodological frameworks capable of leveraging gen AI effectively without
compromising the depth of consumer or marketer insights (Gupta et al., 2024; Kshetri et al., 2023). The
airline customer feedback analysis conducted in this study reveals that GAA TA has the capacity to
analyze emotionally charged, and linguistically diverse customer feedback to generate practically
useful themes. Integrating gen AI into market research can help mitigate the subjectivity inherent in
traditional methods while enabling scalable, time-ef ﬁcient analysis of large qualitative datasets.
ORCID iD
Michael T. Ewing  https://orcid.org/0000-0002-2260-2761
Funding
The authors received no ﬁnancial support for the research, authorship, and/or publication of this article.
Declaration of Con ﬂicting Interests
The authors declared no potential conﬂicts of interest with respect to the research, authorship, and/or publication
of this article.
Supplemental Material
Supplemental material for this article is available online.
Notes
1. >276,000 citations (as at Nov 21, 2025).
2. In GAA TA, an artefact refers to a tangible analytical output generated at each stage of the methodology —
such as a validated list of codes, a synthesized list of themes, with supporting analytical matrices where
necessary.
Jayawardene and Ewing 189

3. https://chatgpt.com/.
4. https://www.humata.ai/.
5. One an expert in marketing, the other an education expert.
References
Ahmed, T., Pai, K. S., Devanbu, P ., & Barr, E. (2024, April). Automatic semantic augmentation of language
model prompts (for code summarization). In Proceedings of the IEEE/ACM 46th international conference
on software engineering (pp. 1-13).
Amarasinghe, I., Marques, F., Ortiz-Beltr ´an, A., & Hern ´andez-Leo, D. (2023). August). Generative pre-trained
transformers for coding text data? An analysis with classroom orchestration data. In European Conference
on Technology Enhanced Learning (pp. 32 –43). ChamSwitzerland: Springer Nature.
Andres Felipe Zambrano, X. L., Barany, A., Baker, R. S., Kim, J., & Nasiar, N. (2023a). From nCoder to
ChatGPT: From automated coding to re ﬁning human coding. https://doi.org/10.35542/osf.io/grmzh
Andres Felipe Zambrano, X. L., Barany, A., Baker, R. S., Kim, J., & Nasiar, N. (2023b). From nCoder to
ChatGPT: From automated coding to re ﬁning human coding. https://doi.org/10.35542/osf.io/grmzh
Bazeley, P . (2020). Qualitative data analysis: Practical strategies. Qualitative Data Analysis ,1 –584.
Belk, R. W. (2013). Extended self in a digital world. Journal of Consumer Research , 40(3), 477–500. https://
doi.org/10.1086/671052
Bello, O. (2023). Prompt engineering for ChatGPT: A comprehensive guide. https://medium.com/@
seyibello31/prompt-engineering-for-chatgpt-a-comprehensive-guide-6650cdf0a047
Bhatia, A., Chandani, A., Atiq, R., Mehta, M., & Divekar, R. (2021). Artiﬁcial intelligence in ﬁnancial services:
A qualitative research to discover robo-advisory services. Qualitative Research in Financial Markets ,
13(5), 632 –654. https://doi.org/10.1108/qrfm-10-2020-0199
Blei, D. M. (2012). Probabilistic topic models. Communications of the ACM , 55(4), 77–84. https://doi.org/10.
1145/2133806.2133826
Boyatzis, R. E. (1998). Transforming qualitative information: Thematic analysis and code development . Sage.
Bozkurt, A., & Sharma, R. C. (2023). Generative AI and prompt engineering: The art of whispering to let the
genie out of the algorithmic world. Asian Journal of Distance Education , 18(2), i –vii.
Braun, V ., & Clarke, V . (2006). Using thematic analysis in psychology. Qualitative Research in Psychology ,
3(2), 77 –101. https://doi.org/10.1191/1478088706qp063oa
Braun, V ., & Clarke, V . (2019). Re ﬂecting on re ﬂexive thematic analysis. Qualitative Research in Sport,
Exercise and Health , 11(4), 589 –597. https://doi.org/10.1080/2159676x.2019.1628806
Briganti, G., & Le Moine, O. (2020). Arti ﬁcial intelligence in medicine: Today and tomorrow. Frontiers of
Medicine, 7, Article 509744. https://doi.org/10.3389/fmed.2020.00027
Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J. D., Dhariwal, P ., Neelakantan, A., Shyam, P ., Sastry,
G., & Askell, A. (2020). Language models are few-shot learners. Advances in Neural Information
Processing Systems , 33, 1877 –1901.
Byrne, D. (2022). A worked example of Braun and Clarke’s approach to reﬂexive thematic analysis. Quality and
Quantity, 56(3), 1391 –1412. https://doi.org/10.1007/s11135-021-01182-y
Carletta, J. (1996). Assessing agreement on classi ﬁcation tasks: The kappa statistic. arXiv preprint cmp-lg/
9602004.
Chakriswaran, P ., Vincent, D. R., Srinivasan, K., Sharma, V ., Chang, C.-Y ., & Reina, D. G. (2019). Emotion AI-
driven sentiment analysis: A survey, future research directions, and open issues. Applied Sciences, 9(24),
5462. https://doi.org/10.3390/app9245462
Christou, P . A. (2023). How to use artiﬁcial intelligence (AI) as a resource, methodological and analysis tool in
qualitative research? Qualitative Report , 28(7).
190 International Journal of Market Research 68(2)

Clarke, V ., & Braun, V . (2013). Teaching thematic analysis: Overcoming challenges and developing strategies
for effective learning. The Psychologist , 26(2), 120 –123.
Clarke, V ., & Braun, V . (2017). Thematic analysis. The Journal of Positive Psychology , 12(3), 297 –298.
Cohen, J. (1960). A coefﬁcient of agreement for nominal scales. Educational and Psychological Measurement,
20(1), 37 –46. https://doi.org/10.1177/001316446002000104
Cooper, H. B., Ewing, M. T., Campbell, C., & Treen, E. (2023). Hero brands, brand heroes: How RM Williams
inspired a cult following and created a shared sense of meaning. Business Horizons , 66(3), 405 –414.
https://doi.org/10.1016/j.bushor.2023.01.006
Creswell, J. W., & Miller, D. L. (2000). Determining validity in qualitative inquiry. Theory into Practice, 39(3),
124–130. https://doi.org/10.1207/s15430421tip3903_2
Denzin, N. K., & Lincoln, Y . S. (2011). The Sage handbook of qualitative research (4 ed.). Sage Publications.
Devlin, J., Chang, M. W., Lee, K., & Toutanova, K. (2019, Bert, June).: Pre-training of deep bidirectional
transformers for language understanding .I n Proceedings of the 2019 conference of the North American
chapter of the association for computational linguistics: human language technologies, 1 , 4171-4186.
Ekin, S. (2023). Prompt engineering for ChatGPT: A quick guide to techniques, tips, and best practices.
Authorea Preprints.
Fischer, E., & Guzel, G. T. (2023). The case for qualitative research. Journal of Consumer Psychology , 33(1),
259–272.
Franken, L., & V epˇrek, L. H. (2025). AI in and for qualitative research. In Handbuch Soziale Praktiken und
Digitale Alltagswelten (pp. 1 –9). Springer.
Garc´ıa-Balboa, J. L., Alba-Fern ´andez, M. V ., Ariza-López, F. J., & Rodr ´ıguez-Avi, J. (2018). Analysis of
thematic similarity using confusion matrices. ISPRS International Journal of Geo-Information , 7(6), 233.
Gebreegziabher, S. A., Zhang, Z., Tang, X., Meng, Y ., Glassman, E. L., & Li, T. J. J. (2023, April). Patat:
Human-ai collaborative qualitative coding with explainable interactive rule synthesis. In Proceedings of
the 2023 CHI Conference on Human Factors in Computing Systems (pp. 1-19).
Guba, E. G., & Lincoln, Y . S. (1994). Competing paradigms in qualitative research. Handbook of Qualitative
Research, 2(163-194), 105.
Guest, G., MacQueen, K., & Namey, E. (2011). Applied thematic analysis . Sage publications.
Gupta, R., Nair, K., Mishra, M., Ibrahim, B., & Bhardwaj, S. (2024). Adoption and impacts of generative
artiﬁcial intelligence: Theoretical underpinnings and research agenda. International Journal of Infor-
mation Management Data Insights , 4(1), Article 100232. https://doi.org/10.1016/j.jjimei.2024.100232
Hevner, A. R. (2007). A three cycle view of design science research. Scandinavian Journal of Information
Systems, 19(2), 4.
Hirschman, E. C. (1986). Humanistic inquiry in marketing research: Philosophy, method, and criteria. Journal
of Marketing Research , 23(3), 237 –249. https://doi.org/10.2307/3151482
Hitch, D. (2024). Arti ﬁcial intelligence augmented qualitative analysis: The way of the future? Qualitative
Health Research , 34(7), 595 –606. https://doi.org/10.1177/10497323231217392
Huit. (2024). Getting started with prompts for text-based generative AI tools. https://huit.harvard.edu/news/ai-
prompts
Hwang, Y ., & Wu, Y . (2025). The inﬂuence of generative arti ﬁcial intelligence on creative cognition of design
students: A chain mediation model of self-ef ﬁcacy and anxiety. Frontiers in Psychology , 15, Article
1455015. https://doi.org/10.3389/fpsyg.2024.1455015
Jick, T. D. (1979). Mixing qualitative and quantitative methods: Triangulation in action. Administrative Science
Quarterly, 24(4), 602 –611. https://doi.org/10.2307/2392366
Jucker, A. H., Landert, D., Seiler, A., & Studer-Joho, N. (2013). Uncovering layers of meaning in the history of
the English language. In A. Jucker, D. Landert, A. Seiler, & N. Studer-Joho (Eds.), Meaning in the history
Jayawardene and Ewing 191

of English: Words and texts in context (studies in language companion series 148) (pp. 1 –15). John
Benjamins.
Kan, B., Wang, T., Lu, W., Zhen, X., Guan, W., & Zheng, F. (2023). Knowledge-aware prompt tuning for
generalizable vision-language models. In Proceedings of the IEEE/CVF International Conference on
Computer Vision (pp. 15670-15680).
Kanaparthi, V . (2022). Examining natural language processing techniques in the education and healthcare
ﬁelds. International Journal of Engineering and Advanced Technology , 12(2), 8 –18. https://doi.org/10.
35940/ijeat.b3861.1212222
Kaplan, A., & Haenlein, M. (2020). Rulers of the world, unite! the challenges and opportunities of arti ﬁcial
intelligence. Business Horizons , 63(1), 37 –50. https://doi.org/10.1016/j.bushor.2019.09.003
Katz, A., Wei, S., Nanda, G., Brinton, C., & Ohland, M. (2023). Exploring the efﬁcacy of ChatGPT in analyzing
student teamwork feedback with an existing taxonomy. arXiv preprint arXiv:2305.11882.
Kiger, M. E., & V arpio, L. (2020). Thematic analysis of qualitative data: AMEE guide no. 131. Medical
Teacher, 42(8), 846 –854. https://doi.org/10.1080/0142159X.2020.1755030
Koehler, M. J., Mishra, P ., Kereluik, K., Shin, T. S., & Graham, C. R. (2013). The technological pedagogical
content knowledge framework. In Handbook of research on educational communications and technology
(pp. 101 –111). New York, NY: Springer.
Kshetri, N., Dwivedi, Y . K., Davenport, T. H., & Panteli, N. (2023). Generative arti ﬁcial intelligence in
marketing: Applications, opportunities, challenges, and research agenda . 102716. Elsevier.
Landis, J. R., & Koch, G. G. (1977). An application of hierarchical kappa-type statistics in the assessment of
majority agreement among multiple observers. Biometrics, 33(2), 363 –374.
LeV asseur, J. J. (2003). The problem of bracketing in phenomenology. Qualitative Health Research , 13(3),
408–420. https://doi.org/10.1177/1049732302250337
Liu, W. (2023). The cognitive basis of thematic analysis. International Journal of Research and Method in
Education, 47(3), 277 –287. https://journals.scholarsportal.info/details/1743727x/v47i0003/277_tcbota.
xml.
Meng, Y ., Michalski, M., Huang, J., Zhang, Y ., Abdelzaher, T., & Han, J. (2023, July). Tuning language models
as training data generators for augmentation-enhanced few-shot learning. In International Conference on
Machine Learning (pp. 24457 –24477). PMLR.
Mittermaier, M., Raza, M. M., & Kvedar, J. C. (2023). Bias in AI-based models for medical applications:
Challenges and mitigation strategies. Npj Digital Medicine , 6(1), 113. https://doi.org/10.1038/s41746-
023-00858-z
Morgan, D. L. (2023). Exploring the use of arti ﬁcial intelligence for qualitative data analysis: The case of
ChatGPT. International Journal of Qualitative Methods, 22, Article 16094069231211248. https://doi.org/
10.1177/16094069231211248
Nowell, B., & Albrecht, K. (2019). A reviewer ’s guide to qualitative rigor. Journal of Public Administration
Research and Theory , 29(2), 348 –363. https://doi.org/10.1093/jopart/muy052
Nowell, L. S., Norris, J. M., White, D. E., & Moules, N. J. (2017). Thematic analysis: Striving to meet the
trustworthiness criteria. International Journal of Qualitative Methods , 16(1), Article 1609406917733847.
OpenAI. (2024). GPT-4 is OpenAI’s most advanced system, producing safer and more useful responses. https://
openai.com/gpt-4
Passi, S., & V orvoreanu, M. (2022). Overreliance on AI literature review. Microsoft Research, 339, 340.
Patton, M. Q. (2023). Qualitative research & evaluation methods: Integrating theory and practice . Sage
publications.
Poola, I. (2023). Overcoming ChatGPTs inaccuracies with pre-trained AI prompt engineering sequencing
process. International Journal of Technology and Emerging Sciences (IJTES) , 3(3), 16 –19.
192 International Journal of Market Research 68(2)

Ramlochan, S. (2024). Role-playing in large language models like ChatGPT. https://promptengineering.org/
role-playing-in-large-language-models-like-chatgpt/
Ryan, G. W., & Bernard, H. R. (2003). Techniques to identify themes.Field Methods, 15(1), 85–109. https://doi.
org/10.1177/1525822x02239569
Saldaña, J. (2021). The coding manual for qualitative researchers. In The coding manual for qualitative re-
searchers (pp. 1 –440).
Sallam, M. (2023). ChatGPT utility in healthcare education, research, and practice: Systematic review on the
promising perspectives and valid concerns. Healthcare.
Sinclair-Maragh, G., & Simpson, S. B. (2021). Heritage tourism and ethnic identity: A deductive thematic
analysis of Jamaican Maroons. Journal of Tourism, Heritage & Services Marketing , 7(1), 64 –75.
Smith, B., & McGannon, K. R. (2018). Developing rigor in qualitative research: Problems and opportunities
within sport and exercise psychology. International Review of Sport and Exercise Psychology , 11(1),
101–121. https://doi.org/10.1080/1750984x.2017.1317357
Terry, G. H. , N., Clarke, V ., & Braun, V . (2017). Thematic analysis. In C. W. W. S. Rogers (Ed.), The SAGE
handbook of qualitative research in psychology (pp. 17 –37). Sage.
Tian, S., Jin, Q., Yeganova, L., Lai, P .-T., Zhu, Q., Chen, X., Yang, Y ., Chen, Q., Kim, W., Comeau, D. C.,
Islamaj, R., Kapoor, A., Gao, X., & Lu, Z. (2024). Opportunities and challenges for ChatGPT and large
language models in biomedicine and health. Brieﬁngs in Bioinformatics , 25(1), bbad493. https://doi.org/
10.1093/bib/bbad493
Tuckett, A. G. (2005). Applying thematic analysis theory to practice: A researcher ’s experience. Contemporary
Nurse, 19(1-2), 75 –87. https://doi.org/10.5172/conu.19.1-2.75
Tufford, L., & Newman, P . (2012). Bracketing in qualitative research. Qualitative Social Work, 11(1), 80–96.
https://doi.org/10.1177/1473325010368316
Tversky, A., & Kahneman, D. (1974). Judgment under uncertainty: Heuristics and Biases: Biases in judgments
reveal some heuristics of thinking under uncertainty. Science, 185(4157), 1124–1131. https://doi.org/10.
1126/science.185.4157.1124
V an Dis, E. A., Bollen, J., Zuidema, W., van Rooij, R., & Bockting, C. L. (2023). ChatGPT: Five priorities for
research. Nature, 614(7947), 224 –226. https://doi.org/10.1038/d41586-023-00288-7
V om Brocke, J., Hevner, A., & Maedche, A. (2020). Introduction to design science research. In Design science
research.I n Cases (pp. 1 –13). Cham: Springer International Publishing.
Wang, S., & Jin, P . (2023). A brief summary of prompting in using GPT models.
White, J., Fu, Q., Hays, S., Sandborn, M., Olea, C., Gilbert, H., Elnashar, A., Spencer-Smith, J., & Schmidt,
D. C. (2023). A prompt pattern catalog to enhance prompt engineering with chatgpt. arXiv preprint arXiv:
2302.11382.
Yan, L., Echeverria, V ., Nieto, G. F., Jin, Y ., Swiecki, Z., Zhao, L., Ga ˇsevi´c, D., & Martinez-Maldonado, R.
(2023a). Human-AI collaboration in thematic analysis using ChatGPT: A user study and design rec-
ommendations. arXiv preprint arXiv:2311.03999 .
Yan, L., Sha, L., Zhao, L., Li, Y ., Martinez-Maldonado, R., Chen, G., Li, X., Jin, Y ., & Ga ˇsevi´c, D. (2023b).
Practical and ethical challenges of large language models in education: A systematic literature review.
arXiv preprint arXiv:2303.13379 .
Zhang, H., Wu, C., Xie, J., Lyu, Y ., Cai, J., & Carroll, J. M. (2023). Redeﬁning qualitative analysis in the AI era:
Utilizing ChatGPT for ef ﬁcient thematic analysis. arXiv preprint arXiv:2309.10771 .
Zhao, W. X., Zhou, K., Li, J., Tang, T., Wang, X., Hou, Y ., Min, Y ., Zhang, B., Zhang, J., & Dong, Z. (2023). A
survey of large language models. arXiv preprint arXiv:2303.18223 .
Jayawardene and Ewing 193
