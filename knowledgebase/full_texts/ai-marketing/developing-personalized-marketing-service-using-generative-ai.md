---
title: Developing Personalized Marketing Service Using Generative AI
url: https://doi.org/10.1109/access.2024.3361946
category: ai-marketing
subcategory: theory
date: 2024-01
venue: IEEE Access
authors:
- Gun Ho Lee
- Kyoung Jun Lee
- Baek Jeong
source: openalex-oa
pdf_url: https://ieeexplore.ieee.org/ielx7/6287639/6514899/10419357.pdf
pages: 8
chars: 44312
fetched_at: '2026-11-08T18:47:34+00:00'
kb_version: 1
---

# Developing Personalized Marketing Service Using Generative AI

VOLUME XX, 2017 1
Date of publication xxxx 00, 0000, date of current version xxxx 00, 0000.
Digital Object Identifier 10.1109/ACCESS.2022.Doi Number
Developing Personalized Marketing Service
Using Generative AI
GUN HO LEE, KYOUNG JUN LEE, BAEK JEONG, TAE KYOUNG KIM
Department of Big Data Analytics, Kyung Hee University, Seoul 02447, South Korea
Corresponding author: Kyoung Jun Lee (klee@khu.ac.kr)
This research was supported by the BK21 FOUR (Fostering Outstanding Universities for Resea rch) funded by the Ministry of Education(MOE, Korea) and
National Research Foundation of Korea(NRF).
ABSTRACT In today's world, the development of social network services (SNS) like Facebook and
Instagram has enabled consumers to acquire information about products through various channels. The
acquisition of diverse information has led to a diversification in consumer preferences and requirements. As
consumer preferences diversify and online channels expand, there is an increasing need for companies to
provide personalized marketing. Among the means of personalized marketing, personalized marketing
messages are a key tool that can enhance customer engagement. However, a limitation of personalized
marketing message services is the cost issue associated with manually writing individual marketing messages
for personalization. To solve this problem, when developing automated technology for personalized
marketing messages, there were concerns about the complexity of model development and the quality of
messages ge nerated automatically. In this study, we propose the Persuasive Message Intelligence (PMI)
service, which utilizes the recently prominent Large Language Model for automated individual personalized
marketing messages. PMI generates marketing messages through prompt engineering based on the theory of
persuasion in marketing and prior research on AI-generated messages, and validates the elements of prompts
through surveys. The trial and error of researchers presented in this study, along with the know-how and rules
of prompt engineering, will serve as guidelines for those who wish to develop services through prompts in
the future.
INDEX TERMS Generative AI, Personalized Marketing Message, Persuasion Theory, Prompt Engineering
I. INTRODUCTION
In contemporary society, consumers encounter product
information through various media channels, largely due to
the evolution of social networking services (SNS), leading
to heightened expectations regarding products and ser vices
[1]. In particular, the proliferation of SNS platforms such
as Facebook and Instagram has enabled access to product
information across diverse channels.  This abundance of
information has broadened consumers' tastes and
requirements. As a result, con sumers exhibit a greater
propensity to engage in purchasing behavior in response to
personalized or targeted advertisements rather than
traditional mass advertising [2]. Specifically, online
advertising, which is often more targeted, elicits a more
active intent to purchase [3].
Targeted advertisements are predominantly composed of
personalized marketing messages, which are increasingly
effective in the context of a society where online shopping
is becoming more prevalent.
This study acknowledges the nece ssity for personalized
services based on a deep understanding of consumer traits
and preferences. It seeks to establish personalized
marketing strategies using minimal customer data, aiming
to minimize costs and negative consumer perceptions. To
this end, the potential brought by advancements in
Generative AI, such as OpenAI's ChatGPT, is explored.
The research proposes a service that generates personalized
marketing messages by structuring prompts based on
persuasion theories and feeding them into Large La nguage
Models. It aims to experiment with the efficacy of message
components within these prompts. The study implements a
Persuasive Message Intelligence service, empirically
testing the impact of AI -generated messages on consumer
perception, the inclusion  of event dates, and the reflection
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3361946
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4.0/

VOLUME XX, 2017 7
of purchase history in the marketing message's
effectiveness.

II. Literature Review

A. Consumer Persuasion Research in AI-Generated
Messages

While research on the impact of AI -generated messages
on consumer persuasion has been ongoing, the advent of
Large Language Models has accelerated this field. A
notable study in this area defines AI -based persuasion as a
symbolic process, where messages created, augmented, or
modified by AI entities are delivered to huma n recipients
to shape, reinforce, or change their responses [ 4]. In the
context of donations, it was found that advertisements
generated by AI, particularly those featuring AI -generated
images of children, negatively impacted donation
intentions, mediated through empathy, anticipated guilt,
and emotional recognition [5].

B. Differences in Persuasiveness of AI Messages
Based on Construal Level

Research explaining how AI -driven persuasion attempts
differ from human -driven ones is based on the theory of
construal levels. Researchers assume that individuals
perceive AI at a lower construal level and understand
consumer responses to AI's persuasive actions in lieu of
humans. Messages generated by AI are more appropriate and
effective when they exhibit characteristics of a lower level of
construal [6]. This study was designed to construct prompts
that create messages at a lower level of construal based on
these findings.

C. AI-Generated Message Persuasion Process
through the Heuristic-Systematic Model

This research defines AI-based persuasion as a symbolic
process, where AI creates and modifies persuasive
messages to be delivered to human recipients. It concretizes
two ways in which AI complicates persuasion: the first
being Thin AI with minimal or no mechanical signals, and
the second being Thick AI, rich in both mechanical and
social signals. The study concludes that AI-generated
messages are perceived by humans through a heuristic
process, and for these messages to be persuasive, AI must
provide messages with high relevance, usability, and
accessibility [7]. This study was thus structured to generate
messages with high relevance, usability, and accessibility in
the prompts.

D. Comparing the Effectiveness of AI-Generated
Messages on Infectious Diseases           Based on
Perception of Origin

This study explores the effectiveness of the GPT -3 model
in generating public health messages, particularly focusing
on COVID -19 vaccination persuasion. It comprises three
distinct research phases: firstly, evaluating the quality of
vaccination messages generated by GPT -3; secondly,
observing how people perceive these AI-generated messages
compared to those written by humans; and thirdly, assessing
the impact of message source perception on perceived
quality.

The findings  indicate that messages generated by GPT -3
were perceived as more persuasive and effective than those
provided by the CDC. However, when marked as AI -
generated, participants showed a preference for public health
messages from human agencies. This suggests that while AI
can be a useful tool in generating public health messages,
human oversight and intervention are necessary. The study
proposes best practices for evaluating the generative output
of large language models and guidelines for public health
professionals on using AI systems [8].

E. Comparing the Effectiveness of Personalized AI-
Generated Messages

This research examines how Large Language Models
(LLMs) can enhance personalized persuasion. Through five
studies, it demonstrates that messages designed using LLMs,
tailored to various topics like consumer products, social
issues, and health advice, and aligned with individual
psychological profiles (personality traits, political ideologies,
moral foundations, etc.), have significantly greater imp act
compared to non-personalized messages.

To validate the effectiveness of personalized persuasion,
experiments were conducted targeting various types of
messages and psychological traits. These experiments tested
the ability of Large Language Models to generate persuasive
messages tailored to users' psychological characteristics. For
instance, the study involved using GPT-3 to create messages
like 'iPhone advertisements for extroverted and passionate
individuals', tailored to specific traits. The results  showed
that individual traits like openness, conscientiousness, and
extroversion predict their advertisement preferences,
indicating that GPT -3 generated personalized messages are
more persuasive.

This research demonstrates the potential of Large Language
Models to understand psychological traits and integrate them
into personalized message creation. Researchers found that
Large Language Models can 'think' and react to external
stimuli in a manner akin to humans when generating
psychologically tailored me ssages. These findings suggest
that Large Language Models could enable the automation
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3361946
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4.0/

VOLUME XX, 2017 7
and implementation of personalized persuasion.
Additionally, the study proves that AI -generated
personalized messages can enhance the effectiveness of
advertising messages [9].

III. Main Discussion

A. Persuasive Message Intelligence

The Persuasive Message Intelligence service proposed in this
study utilizes Generative AI to deliver personalized,
automated marketing messages that promote products
selected by merchants to consu mers. This service
incorporates the format of User Prompt and System Prompt,
akin to the GPT -4 model, and integrates theories of
persuasion in marketing along with prior research on the
persuasiveness of AI -generated messages. The prompts are
designed to r eflect age, gender, purchase history, and event
dates in the marketing messages. These prompts have been
crafted following the official prompt -engineering guides
provided by OpenAI.

Persuasive Message Intelligence employs the API of
OpenAI's GPT-4 model, which stands as the most advanced
among Large Language Models. OpenAI's GPT -4 model
demonstrates superior performance even when compared to
the latest Large Language Models like Google's Bard and
Meta's LLAMA2 models [10][11][12].

B. Design of Persuasive Message Intelligence
Structure

The Persuasive Message Intelligence (PMI) service is
designed to generate promotional messages for products set
by merchants, based on User Data. In this service,
merchants initially select the product to be promoted and
provide related information to the PMI system. The product
information provided by merchants includes the name and
description of the product to be advertised. Once the
merchant inputs the product information, the PMI system
retrieves the targeted User Data for marketing. This User
Data encompasses demographic details such as age, gender,
and phone number, along with purchase history and event
details (Day, Date, Time).

The PMI service generates User Prompts and System
Prompts, reflecting the information about the product to be
promoted by the merchant and the User Data. These
prompts are based on a pre-set structure informed by
persuasive theories. The User Prompt is tailored to reflect
individual information of the customers identified in the
System Prompt, thus creating distinct User Prompts for
each individual. The System Prompt, on the other hand,
establishes the basic structure, format, and rules for
generating the message [13][14][15].

These User and System Prompts are input into OpenAI's
GPT-4 API to generate personalized marketing messages
for each user. A function is then used to pair these
personalized messages with phone numbers. This pairing of
individualized messages and phone numbers is utilized to
call a text message transmission API, which then sends the
text messages to each respective user.
FIGURE 1. Persuasive Message Intelligence BPMN Structure

To clearly illustrate the service structure of Persuasive
Message Intelligence, the Business Process Model and
Notation (BPMN)  methodology, a standard for graphically
representing business processes, was employed as depicted
in <Figure 1>. BPMN serves as a pivotal tool in visualizing
the flow of processes in diagrammatic form, thereby
facilitating a clear understanding of the ope rational
workflow in businesses [16][17][18]. Based on this structure,
the process begins with the merchant performing a task of
inputting the name and description of the product to be
promoted, followed by retrieving User Data from a data
repository. This  data is then provided to the Persuasive
Message Intelligence system to generate messages.
Subsequently, a text message transmission API is called to
dispatch these messages to customers. The diagrammatic
representation of this process delineates the stages occurring
across three distinct layers: the store, the customer, and the
Persuasive Message Intelligence system, thereby indicating
at which layer each process step takes place.

C. Persuasive Message Intelligence Service Prompt
Engineering

In this study, the prompt engineering of the Persuasive
Message Intelligence service was planned based on prior
research on the persuasive power of advertising messages
and AI-generated messages in marketing. Furthermore, the
designed prompt structure utilizes Ope nAI's GPT-4 model,
the most advanced Large Language Model, and is based on
OpenAI's published prompt writing method, the
Cookbook[10][11][12]. The Cookbook's approach to prompt
writing begins by defining the role the Large Language
Model will perform at th e start of the prompt. It then
proceeds by numbering and writing the rules that must be
followed in the prompt[1 9]. For example, to write a prompt
for composing a novel on a given topic, one would start with
"Write Novel based on suggested Subject with fol lowing
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3361946
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4.0/

VOLUME XX, 2017 7
rules," commanding the creation of a novel on the given topic
and then listing the rules. These rules might be "1. Only write
in a polite tone. 2. Novel must be more than 300 words,"
ensuring that the novel is written politely and exceeds 300
words.

Based on prior research in marketing on the persuasive
power of advertising messages and AI -generated messages,
three elements were incorporated. The first element is to
ensure that the consumer receiving the advertising marketing
message does not percei ve it as AI -generated. The second
element is that the advertising marketing message should be
personalized without making the consumer feel overly
invaded in terms of information. The third element is that the
advertising marketing message should specifica lly explain
the reasons for recommending the product purchase. The
first element was based on studies showing that the
persuasiveness of a message decreases if the consumer
realizes it was AI -generated compared to when they do
not[30]. The second element was based on findings that AI -
generated messages are interpreted based on a Heuristic
process, and messages that are not strongly assertive but are
relevant, usable, and accessible are more persuasive[ 7].
Additionally, studies have shown that the persuasive ness of
AI-generated messages increases when personalized, such as
according to the BIG5 personality types[ 9]. The third
element was based on research findings that the more
specific the reasons for purchasing a product are in an
advertising marketing mess age, the more persuasive the
message becomes[6].

FIGURE 2. Persuasive Message Intelligence System Prompt

The prompt depicted in <Figure 5> was constructed
following the prompt-engineering guides method of OpenAI,
with roles and rules based on prior research on the persuasive
theories of advertising messages and the efficacy of AI -
generated messages in marketing. In the prompt, the role of
the Large Language Model, as described in the service
structure, was assigned to generate marketing messages
using the selected product and product description provided
by the Merchant, along with the customer's gender, age,
purchase history, and Event (Date). The rules reflected basic
characteristics of advertising marketing messages, such as
using emoticons and hashtags, and emp loying a polite tone.
To incorporate elements from the aforementioned research,
information was used as indirectly as possible to prevent
consumers from feeling that their personal information was
invaded or recognizing that the message was AI -generated.
Additionally, the reasons for recommending specific
products were detailed, and information perceived as less
invasive to personal privacy, such as age, gender, and
purchase history[ 18], was utilized to create personalized
messages. Through trial and error,  it was determined that
essential content should be denoted with adjectives like
'Must'. It was also observed that placing important sub -rules
earlier in the sequence reflected effectiveness more
accurately. Furthermore, rule 13 was developed to address
the issue of only citing 'experiencing a variety of tastes' as a
reason when the purchase history included diverse foods.

D. Technical Implementation of Persuasive Message
Intelligence Service

The code for implementing the automated service of
Persuasive Message Intelligence was developed on Google
Colab, utilizing a GPU of RTX3080Ti and a CPU of Intel i7
12700k. The code comprises functions for generating User
Prompts, calling the GPT-4 API and creating messages, and
a function for sending text messages.

Persuasive Message Intelligence employs a User Prompt
generation function to create distinct prompts for each user.
These prompts, along with a fixed System Prompt, are
inputted into the GPT-4 API to generate messages. Messages
created by the G PT-4 API are paired with phone numbers
and fed into a text message sending API, through which
personalized messages are dispatched as text messages.

The User Prompt generation function enables the Merchant
to input customer demographics such as gender, ag e,
purchase history, product name, and product description,
automatically creating User Prompts for input into GPT -4.
As previously described, these User Prompts contain
individual user information required by the System Prompt
set in the GPT -4 API, formin g the basis for generating
personalized messages.

The GPT-4 API calling function, utilizing libraries provided
by OpenAI, inputs the generated User Prompts and the fixed
System Prompt to create messages through the GPT -4 API.
The System Prompt is fixed, a llowing for the simultaneous
input of various User Prompts to generate multiple messages.
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3361946
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4.0/

VOLUME XX, 2017 7
FIGURE 3. Persuasive Message Intelligence Transmisson Code
Example
The text message format conversion function in Persuasive
Message Intelligence has been developed to transfo rm
customer phone numbers and personalized messages
generated by GPT -4 into the format required by Aligo's
automated text message transmission API, known as the
Aligo API, for transmission. An example of this conversion
process is illustrated in <Figure 6> , where the text message
conversion function adapts the phone numbers and messages
to the format of the Aligo API.

The text message transmission function within the
Persuasive Message Intelligence framework is designed to
utilize the Aligo API for dispatching messages. This function
operates by employing the text message format conversion
function, which adapts phone number and message pairs into
the Aligo API format. Once converted, these pairs are then
transmitted via the Aligo API. A significant featur e of this
API is its capability to simultaneously send distinct messages
to multiple recipients.

E. Survey on the Effectiveness of Message Elements
in Persuasive Message Intelligence
In this study, the elements of prompts used in Persuasive
Message Intelligence were validated through a series of three
surveys. The elements of the prompts verified through these
surveys included the perception of AI-generated content, the
reflection of Event (Date) in the message, and the indication
of purchase history in the m essage. The surveys aimed to
ascertain whether the effectiveness of messages varied
according to the prompt elements.

The hypotheses for the survey on prompts in this study are
as follows:
H1: When the AI generation of the message is not disclosed,
the effectiveness of the message will be higher.
H2: When Event (Date) is reflected in the creation of
marketing messages, the effectiveness of the message
will be higher.
H3: When the reflection of purchase history is not disclosed,
the effectiveness of the message will be higher.

The preceding research for hypothesis H1 suggests that when
consumers are aware that a message is AI -generated, they
tend to perceive it as less persuasive. An experiment showed
that even when the content of a health authority's message
about the risks of COVID -19 was identical, the
persuasiveness rated by respondents varied depending on
their awareness of the message being AI -generated [6]. For
hypothesis H2, the preceding research indicates that AI -
generated messages  are perceived by consumers through a
heuristic process. Messages recognized in this manner are
more effective when they contain information with high
relevance, utility, and accessibility. Additionally,
information such as dates can significantly influenc e
consumer purchasing decisions [ 7]. Regarding hypothesis
H3, the preceding research suggests that consumers feel a
sense of rejection when the information used in messages
leads to personal identification. For instance, the type of
information utilized in various messages, such as age, gender,
phone number, purchase history, and individual social media
posts, can elicit different levels of consumer aversion.
Messages that use personal social media posts in their
creation tend to provoke more negative emoti ons compared
to information that is less identifying, like age and gender
[19].

To validate the three prompt elements previously described,
a series of surveys were conducted in three phases, each
survey being conducted once. The first, second, and third
surveys were carried out through Embrain's Easy Survey
panel, targeting 300 adult men and women aged from their
20s to 60s in South Korea. Each phase of the survey involved
300 participants, and respondents who participated in one
phase were restricted fro m participating in subsequent
phases. In line with prior research, messages were generated
using minimal personal information, specifically age and
gender, to ensure personalization with minimal privacy
intrusion [19]. The product data used in the messages  were
based on the name and description of BBQ Chicken's Golden
Olive Chicken. The surveys were conducted online, and
different messages were displayed to each survey group to
evaluate the effectiveness of the messages. The sample size
of 300 respondents e xceeds the minimum sample size
required for statistical analysis in academic research, as
verified by the Gpower program [ 20]. The 300 participants,
both men and women aged from their 20s to 60s, sourced
from Embrain, were divided into 20 groups, each cons isting
of 15 individuals, based on gender (2 groups), generation (5
groups), and treatment (2 groups). This distribution ensured
a minimum number of participants for each variable,
securing the representativeness of the survey responses.

For the purpose of validating the effectiveness of the
proposed hypotheses based on the survey results, regression
analysis, a commonly used statistical method, was employed.
This analysis was conducted using the widely recognized
SPSS25 (Statistical Package for the Socia l Sciences 25)
software. The aim of the regression analysis was to
investigate the correlations between variables and to
understand the extent and direction of the impact of
independent variables on dependent variables [ 21].
Throughout this process, data collection and processing were
carried out in strict accordance with established statistical
standards and procedures.
To test H1 hypothesis, a primary survey was conducted.
Using Persuasive Message Intelligence, personalized
marketing messages were generated for different genders
and generations. For the group informed about AI creation,
the message displayed on the survey screen i ncluded the
phrase, “-This message was generated by AI-”.

The persuasiveness of the message and the increased
interest in the product were evaluated using a two -item, 11-
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3361946
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4.0/

VOLUME XX, 2017 7
point scale questionnaire. Considering the survey's nature,
where extreme responses are less common and middle values
are more frequently chosen, an 11 -point scale was used due
to the limited number of questions [ 22]. Messages were
generated for different genders and generations, varying in
AI creation awareness, age, and generation in the  prompts.
The results of the message generation revealed that the social
conventions associated with each generation and gender
were reflected in the messages.
FIGURE 4. Questionnaire Display Screen
<Figure 4> illustrates the screen as seen by respondents
during the survey. Initially, respondents enter demographic
information to categorize their generation. Subsequently,
they encounter a screen similar to <Figure 4> in the actual
survey response interface. The first paragraph displays
different messages to responden ts based on the group they
are assigned to. In <Figure 4>, one can observe the display
of a message indicating the AI creation status. Following this,
respondents answer two questions: one about the
persuasiveness of the advertisement message and another
regarding their level of interest in the product generated by
the advertisement message. The number and nature of the
survey questions were partially modified based on previous
studies [ 9]. As previously mentioned, the scoring was
conducted on an 11 -point scale, with 1 point indicating 'not
at all', 6 points 'moderate', and 11 points 'very much so', in
accordance with prior research [23].

Table 1. Regression Analysis Results for Hypothesis H1

For the regression analysis to adhere to its assumptions, it
is essential to satisfy the conditions of independence,
homoscedasticity, and normality. Regarding independence,
the item groups concerning AI creation awareness satisfy the
criterion of independence [ 24]. In terms of normality, a
Kolmogorov-Smirnov & Shapiro-Wilk test conducted using
SPSS25 revealed a P -value of <0.01, indicating that the
distribution conforms to normality, as this value is below the
significance level of 0.05. As for homoscedasticity, the
Levene's test for equality of variances conducted in SPSS25
yielded an F-value of 0.000 and a P-value of 0.946, satisfying
the condition of P>=0.5 and thus supporting the assumption
of homoscedasticity [25].

In the comparison of two regression analysis models, the first
model, which incorporated only control variables, exhibited
a modified R -squared value of 0.068, an R -squared change
of 0.084, an F -statistic of 5.032, and a p -value of the F -
statistic less than 0.001. These outcomes suggest that control
variables, specifically generat ion and gender, significantly
influence the effectiveness of the message.

The second model, an extension of the first with the inclusion
of the independent variable representing awareness of AI -
generated content, demonstrated an increase in the modified
R-squared value to 0.078, an R-squared change of 0.013, an
F-statistic of 4.064, and a p-value for the F-statistic of 0.045.
This indicates that the awareness of AI -generated content
additionally and significantly affects the effectiveness of the
message, affirming its statistical significance [24].

Synthesizing the results of the regression analysis conducted
for the verification of Hypothesis H1, it becomes evident that
the recognition of AI -generated phrases significantly
impacts the effectiveness of the  message. This implies that
the presence of AI -generated content phrases leads to a
statistically significant change in consumer satisfaction with
the message. However, the relatively minor change in the
modified coefficient of determination R -squared valu e
suggests that the explanatory power of AI-generated content
phrases is limited.

This finding indicates that while the awareness of AI -
generated content phrases does influence consumer
satisfaction, it might be a limited factor in determining the
overall effectiveness of the message. Consequently, these
results imply that while consumer perception of the
effectiveness of AI-generated advertisements is an important
aspect, enhancing overall message satisfaction requires
consideration of additional factors.

Therefore, considering the ethical implications and
consumer rights protection regarding AI -generated phrases,
future research should more thoroughly investigate the
impact of the inclusion of AI -generated content phrases on
message effectiveness. This a pproach could contribute to
stimulating societal discussions on the ethical challenges
posed by advancements in AI technology and aid in
developing marketing strategies that enhance the
transparency of AI-generated content.

Table 2. Regression Analysis Results for Hypothesis H2

According to <Table 2>, the inclusion of Event (Date), while
having low explanatory power, has a statistically significant
impact on message effectiveness.
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3361946
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4.0/

VOLUME XX, 2017 7

In the model including control variables such as generation
and gender, the regression analysis resulted in a modified R-
squared value of 0.088, an R-squared change of 0.095, an F-
statistic of 13.393, and a p -value for the F-statistic less than
0.001. This suggests that the control variables have a
considerable impact  on message effectiveness and are
statistically highly significant.

Moreover, in the independent variable model, when the
inclusion of Event (Date) was added to the control variable
model, the modified R-squared value increased to 0.100, the
R-squared change was 0.015, the F -statistic was 4.322, and
the p-value for the F -statistic was 0.039. This confirms that
the addition of Event (Date) information has an additional
significant impact on message effectiveness and is
statistically significant.

From these  analytical results, it is evident that specific
information elements within the message, namely the
inclusion of Event (Date), can be a crucial factor in altering
message effectiveness. However, the explanatory power of
such elements is relatively low, in dicating that other
variables influencing message effectiveness should also be
considered [24].

Table 3. Regression Analysis Results for Hypothesis H3
To test Hypothesis H3: "The effectiveness of the message
will be higher when the reflection of purchase history is not
disclosed," a regression analysis was conducted. The
independent variable was set as 'indication of purchase
history,' with 'gender' and 'generation' as control variables
and 'message effectiveness' as the dependent variable. The
assumptions of independence, homoscedasticity, and
normality for regression analysis were verified.

For the test of independence, independent groups were
confirmed to exist based on the reflection of purchase history,
and this was assumed. In the test of no rmality, the p -value
was less than 0.01, satisfying the significance level of below
0.05. The homoscedasticity test showed an F -value of 0.000
and a p -value of 0.998, assuming homoscedasticity.
However, as seen in <Table 7>, the regression analysis
results showed an F -value of 4.064 and a significance
probability of 0.778, not satisfying the significance level
p<0.05. This implies that the indication of purchase history
does not have a significant impact on message effectiveness.

Based on existing research, the impact of indicating purchase
history on consumer aversion is higher than that of age and
gender, but relatively lower compared to more sensitive
personal information like social media posts, phone numbers,
names, etc. [44]. The use of assumed purchase history in the
experimental design might also lead respondents to perceive
less invasion of privacy than in reality. However, positive
responses were observed in both cases regarding the
effectiveness of messages reflecting purchase history.

IV. Conclusion
Academically, this research conducted a theoretical study on
the prompt structure of personalized advertising message
services using the Large Language Model, based on studies
of marketing persuasion theory and the effectiveness  of AI
messages. It also proposed prompt engineering rules based
on the researcher's trial and error. The business implication
is the proposal of a persuasive, personalized marketing
message service using the Large Language Model,
suggesting an easy develo pment approach using only the
Large Language Model and SMS transmission API.
Additionally, it proposed providing cost -effective,
personalized marketing services using Generative AI.

The study has limitations due to practical constraints in
survey methodol ogy, as it could not experiment with
personalized messages generated using actual respondent
data. Future research needs to further experiment with
elements of prompts for generating personalized advertising
marketing messages and explore the correlation b etween
prompt elements and message effectiveness.

REFERENCES
[1] Kang, Y. & Yang, K. C. (2021). Will Social Media and Its
Consumption Converge or Diverge Global Consumer Culture?. In P.
Wamuyu (Ed.), Analyzing Global Social Media Consumption (pp. 68-
87). IGI Global
[2] Lina, L. F., & Setiyanto, A. (2021). Privacy concerns in personalized
advertising effectiveness on social media. SRIWIJAYA
INTERNATIONAL JOURNAL OF DYNAMIC ECONOMICS AND
BUSINESS, 5(2), 147-156.
[3] Aslam, H., Rashid, M., & Chaudhary, N. (20 21). Impact of
Personalized Social Media Advertising on Online Impulse Buying
Behavior. SEISENSE Business Review, 1(3), 12-25.
[4] Dehnert, M., & Mongeau, P. A. (2022). Persuasion in the age of
artificial intelligence (AI): Theories and complications of AI -based
persuasion. Human Communication Research, 48(3), 386-403.
[5] Arango, L., Singaraju, S. P., & Niininen, O. (2023). Consumer
Responses to AI -Generated Charitable Giving Ads. Journal of
Advertising, 1-18.
[6] Kim, T. W., & Duhachek, A. (2020). Artificial intellig ence and
persuasion: A construal -level account. Psychological science, 31(4),
363-380.
[7] Dehnert, M., & Mongeau, P. A. (2022). Persuasion in the age of
artificial intelligence (AI): Theories and complications of AI -based
persuasion. Human Communication Research, 48(3), 386-403
[8] Karinshak, E., Liu, S. X., Park, J. S., & Hancock, J. T. (2023).
Working With AI to Persuade: Examining a Large Language Model's
Ability to Generate Pro -Vaccination Messages. Proceedings of the
ACM on Human-Computer Interaction, 7(CSCW1), 1-29.
[9] Matz, S., Teeny, J., Vaid, S. S., Harari, G. M., & Cerf, M. (2023). The
Potential of Generative AI for Personalized Persuasion at Scale.
[10] li, R., Tang, O. Y., Connolly, I. D., Fridley, J. S., Shin, J. H., Sullivan,
P. L. Z., ... & Asaad, W. F. (2022). Performance of ChatGPT, GPT-4,
and Google bard on a neurosurgery oral boards preparation question
bank. Neurosurgery, 10-1227.
[11] Qian, M. (2023, September). Performance Evaluation on Human -
Machine Teaming Augmented Machine Translation Enabled by GPT-
4. In Proceedings of the First Workshop on NLP Tools and Resources
for Translation and Interpreting Applications (pp. 20-31).
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3361946
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4.0/

VOLUME XX, 2017 7
[12] Kortemeyer, G. (2023). Performance of the Pre -Trained Large
Language Model GPT-4 on Automated Short Answer Grading. arXiv
preprint arXiv:2309.09338.
[13] J. U. Duncom Cheng, J., Liu, X., Zheng, K., Ke, P., Wang, H., Dong,
Y., ... & Huang, M. (2023). Black-Box Prompt Optimization: Aligning
Large Language Models without Model Training. arXiv preprint
arXiv:2311.04155.be, “Infrared navigation—Part I: An assessment of
feasibility,” IEEE Trans. Electron Devices, vol. ED-11, no. 1, pp. 34–
39, Jan. 1959, 10.1109/TED.2016.2628402.
[14] Lim, S., & Schmälzle, R. (2023). Artificial intelligence for health
message generation: an empirical study using a large language model
(LLM) and prompt engineering. Frontiers in Communication, 8,
1129082.
[15] Wu, T., Terry, M., & Cai, C. J. (2022, April). Ai chains: Transparent
and controllable human -ai interaction by chaining large language
model prompts. In Proceedings of the 2022 CHI conference on human
factors in computing systems (pp. 1-22).
[16] Ballentine, B. (2016). Using Process Modeling Notation to Map the
Buying and Selling of Complex Software Solutions: A Qualitative
Study's Implications for Practice and Pedagogy. T echnical
Communication, 63(3), 212-230.
[17] Krishnan, R., Peters, J., Padman, R., & Kaplan, D. (2005). On data
reliability assessment in accounting information systems. Information
Systems Research, 16(3), 307-326.
[18] Szirtes, T. (2012). Managing knowledge sharin g–case study of a
consulting firm. Society and Economy. In Central and Eastern Europe
ǀ Journal of the Corvinus University of Budapest, 34(1), 139-160.
[19] OpenAI. (2023). prompt -engineering. OpenAI. Retrieved November
27, 2023, from https://platform.openai.co m/docs/guides/prompt-
engineering
[20] White, T. B., Zahay, D. L., Thorbjørnsen, H., & Shavitt, S. (2008).
Getting too personal: Reactance to highly personalized email
solicitations. Marketing Letters, 19, 39-50.
[21] Faul, F., Erdfelder, E., Lang, A. G., & Buchner, A. (2007). G* Power
3: A flexible statistical power analysis program for the social,
behavioral, and biomedical sciences. Behavior research methods,
39(2), 175-191.
[22] Olufemi, J., & Wasiu, O. (2015). THE EFFECTIVENESS OF
PARAMETRIC TECHNIQUES OF HYPOTHESIS T ESTING : AN
EMPIRICAL ANALYSIS OF DECISION MAKING IN THE
PUBLIC SECTOR.
[23] Zuell, C., & Scholz, E. (2016). 10 points versus 11 points? Effects of
Left-right Scale Design in a Cross-national Perspective.
[24] Dell-Kuster, S., Sanjuan, E., Todorov, A., Weber, H., Heberer, M., &
Rosenthal, R. (2014). Designing questionnaires: healthcare survey to
compare two different response scales. BMC medical research
methodology, 14, 1-13.
[25] Samsudin, S. N., Abdullah, B., & Yusoff, N. (2022, June). Customer
Satisfaction and Service  Experience in Big Data Analytics for
Automotive Service Advisor. In 2022 IEEE International Conference
on Automatic Control and Intelligent Systems (I2CACIS) (pp. 84-89).
IEEE.

GUN HO LEE  received the B.S. degree in
Business Administration  Studies from K ookmin
University, Seoul, South Korea. He is currently
pursuing the Master. degree in big data analytics at
the Kyung Hee university. His research interests
include natural language processing, generative AI,
and Business Idea with AI . He is working as a
Junior researcher in AIBM (Artificial Intelligence
and Business Models) Lab since 2022
KYOUNG JUN LEE is a professor of the
Business School and the department of Big Data
Analytics and the director of AIBM (Artificial
Intelligence and Business Models) Lab and Big
Data Research Center at Kyung Hee University
in Seoul, Korea. He won the IAAI Awards in
1995, 1997, and 2020 from AAAI and worked as
a visiting scientist/professor at CMU, MIT, and
UC Berkeley. He was the 2017 president of the
Korean Intelligent Information Systems Society.
He founded Benple Inc., an IoT & AI -based
company, and Allwin Inc., a patent -based e -
commerce company. He received the 2017 Presidential Award for his
contribution to Korea’s e-government system. He holds BS, MS, and PhD
degrees in Management Science from KAIST and completed graduate work
in Public Administration at Seoul National University

BAEK JEONG  received the B.S. and M.S.
degrees in Child and Family Studies from Kyung
Hee University, Seoul, South Korea. He is
currently pursuing the Ph.D. degree in big data
analytics at the same university. His research
interests include natural language processing ,
generative AI, and youth development. He is
working as a senior researcher in AIBM (Artificial
Intelligence and Business Models) Lab since 2020

Taekyung Kim is an Associate Professor in the
Department of Big Data Analytics at Kyung Hee
University. He earned his PhD from Seoul
National University, a testament to his deep
understanding and expertise in his field. Dr. Kim
has made significant contributions to the
academic community through his research, which
is evident in his numerous publications in
prestigious journals such as Information Systems
Research (ISR), Journal of Management
Information Systems (JMIS), International
Journal of Information Management (IJIM), Electronic Markets (EM), and
others. His primary research interests lie in big data analysis, machine
learning, di gital wellness, and smart tourism. These areas reflect his
commitment to leveraging data science and advanced analytical techniques
in addressing modern challenges and exploring innovative solutions. Dr.
Kim’s work not only advances theoretical understandi ng but also has
practical implications, especially in the evolving domains of digital
technology and smart applications.
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3361946
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4.0/
