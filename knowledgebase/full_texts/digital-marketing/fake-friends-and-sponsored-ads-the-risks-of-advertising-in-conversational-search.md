---
title: 'Fake Friends and Sponsored Ads: The Risks of Advertising in Conversational Search'
url: https://arxiv.org/abs/2506.06447
category: digital-marketing
subcategory: empirical
date: 2025-06
venue: ''
authors:
- Jacob Erickson
source: arxiv
pdf_url: https://arxiv.org/pdf/2506.06447
pages: 8
chars: 29591
fetched_at: '2026-11-08T13:14:11+00:00'
kb_version: 1
---

# Fake Friends and Sponsored Ads: The Risks of Advertising in Conversational Search

arXiv:2506.06447v1  [cs.HC]  6 Jun 2025
Fake Friends and Sponsored Ads: The Risks of Advertising in
Conversational Search
Jacob Erickson
Vassar College
Poughkeepsie, New York, USA
jerickson@vassar.edu
ABSTRACT
Digital commerce thrives on advertising, with many of the largest
technology companies relying on it as a significant source of rev-
enue. However, in the context of information-seeking behavior,
such as search, advertising may degrade the user experience by
lowering search quality, misusing user data for inappropriate per-
sonalization, potentially misleading individuals, or even leading
them toward harm. These challenges remain significant as conver-
sational search technologies, such as ChatGPT, become widespread.
This paper critically examines the future of advertising in conversa-
tional search, utilizing several speculative examples to illustrate the
potential risks posed to users who seek guidance on sensitive topics.
Additionally, it provides an overview of the forms that advertising
might take in this space and introduces the “fake friend dilemma, ”
the idea that a conversational agent may exploit unaligned user
trust to achieve other objectives. This study presents a provoca-
tive discussion on the future of online advertising in the space of
conversational search and ends with a call to action.
CCS CONCEPTS
• Human-centered computing → Human computer interac-
tion (HCI); • Social and professional topics → Computing
/ technology policy ; • Information systems → Information
retrieval.
KEYWORDS
Native Advertising, Personalization, Conversational Search, AI
Alignment, Trust and Safety
ACM Reference Format:
Jacob Erickson. 2025. Fake Friends and Sponsored Ads: The Risks of Adver-
tising in Conversational Search. In Proceedings of the 7th ACM Conference
on Conversational User Interfaces (CUI ’25), July 8–10, 2025, Waterloo, ON,
Canada. ACM, New York, NY, USA, 8 pages. https://doi.org/10.1145/3719160.
3737613
1 INTRODUCTION
Content Warning: This paper critically examines the potential
risks of unfettered advertising in conversational search. The topic of
depression is brought up extensively. If you or someone you know
is struggling with depression, please seek professional support.
Permission to make digital or hard copies of part or all of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for third-party components of this work must be honored.
For all other uses, contact the owner/author(s).
CUI ’25, July 8–10, 2025, Waterloo, ON, Canada
© 2025 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-1527-3/2025/07.
https://doi.org/10.1145/3719160.3737613
Search engines once put the user first. In the intervening years,
there has been a growing sense - backed by some empirical evidence
- that search engine advertising has degraded the quality of search
and the user experience [10, 14].
We may be entering a new era of search, and changes to the
digital advertising market will accompany that shift. Traditional
search engines may no longer be the growth area for the future
of digital advertising as new alternatives emerge. Large Language
Models (LLMs) and their conversational user interfaces, exemplified
through apps like ChatGPT 1, are frequently used by millions of
users [25] and may replace traditional search engines for many of
them. Currently, these applications are undisturbed by paid adver-
tising, but like the traditional search engines before them, this might
be a temporary period before monetization concerns rise. OpenAI
is already exploring the possibility of integrated advertising [21],
while others are beginning to test it [27, 32].
This paper imagines the risks present in the future of digital
advertising in conversational search, using speculative and provoca-
tive examples. In the event of unfettered advertisements, the incred-
ible potential of LLMs for helping users access information may
be diminished, while real harm may be escalated. To show what
this future could hold, we provide demonstrations taken from the
perspective of a fictionalized user who uses ChatGPT to discuss
depressive symptoms.
The emphasis on a user experiencing depression is intentional.
Chatbots are increasingly being used in mental health care [9, 17,
30], and in an age of widespread mental health challenges [9], it is
vitally important to consider the quality of information that users
receive in sensitive contexts. In a moment of need, users may be
uniquely vulnerable to manipulation from a conversational agent
they trust. Furthermore, early evidence suggests that users may
trust health information coming from conversational agents more
than traditional search engines [31]. AI agents pose trust challenges
because their values may be unaligned with the user and in support
of other stakeholders, such as advertisers [ 20]. To conceptualize
this risk, we introduce the fake friend dilemma, a case when users
think a conversational search agent is acting in their best interest
when, in reality, the agent has other goals in mind.
In the interest of transparency, the initial prompts given to Chat-
GPT are provided in Appendix A. These demonstrations were con-
ducted using ChatGPT, the most widely adopted conversational
search engine, with the freely available GPT-4o model. The ex-
amples provided in this paper are actual outputs from ChatGPT,
generated through carefully crafted prompts designed to elicit spe-
cific responses. This paper does not claim that such responses are
already organically occurring but rather envisions a future where
1https://chat.openai.com

CUI ’25, July 8–10, 2025, Waterloo, ON, Canada Jacob Erickson
they could. By situating these speculative scenarios within a real,
widely used interface, we aim to evoke a sense of familiarity and
plausibility, underscoring how easily trust could be exploited in con-
versational systems shaped by conflicting incentives. This framing
helps demonstrate why action is necessary before it is too late.
As conversational interfaces challenge the dominance of tradi-
tional search engines, the decision on which to prioritize between
user experience and monetization will be highly consequential.
2 BANNER ADS
One possibility for future advertising in conversational search is
the integration of banner text ads, such as in Figure 1. A banner ad
is a visual advertisement that “consists of a combination of graphics
and textual content” and “is displayed on a website accessed via
desktop PCs on a mobile-enabled website or in an app. ” [24]. These
advertisements are prolific across the internet [ 24], and despite
concerns about users becoming impervious to their effects [15, 19],
they have the benefit of being transparently recognizable as adver-
tisements. In Figure 1, a simple banner ad is displayed promoting
the relatively innocuous product of Serta mattresses. Even without
explicitly specifying that this is an advertisement, separating it from
the main response given by ChatGPT helps the user distinguish
between content and advertising. Further disclosure may make this
abundantly clear.
Banner ads can degrade the user experience by reducing informa-
tion recall, increasing cognitive load, and inspiring user frustration
and annoyance [10]. However, if the future of advertising were lim-
ited to these types of ads, society would likely breathe a collective
relief that mere annoyance was our primary concern. The more
concerning issue is advertisements that can be integrated into oth-
erwise “regular” responses from a conversational AI and, therefore,
be “disguised. ” These advertisements are known as “native ads” and
may or may not be disclosed. The remainder of this paper will focus
on them.
3 NATIVE ADVERTISING
A few studies have provided proof of concept for how users perceive
and interpret embedded advertisements [28, 36]. Zelch et al. [36]
found that users may not notice advertising that is subtly integrated
into conversational search answers unless it is explicitly disclosed
as advertising. Research on the Persuasion Knowledge Model [12]
suggests that the effectiveness of advertising is partially mitigated
by consumers knowing that someone is attempting to persuade
them. When receiving information in this scenario, individuals are
thus more skeptical in considering the intent of the information
they are receiving and the source who is providing it [4]. Therefore,
advertising that is difficult to recognize as selling a product could be
especially effective for a company attempting to reach consumers
since it can avoid the inherent skepticism that comes with someone
knowing they are being marketed to.
This advertising strategy becomes important because, in an age
of advertising inundation, digital advertisers may be concerned
that banner ads are ineffective and lead to consumer “blindness”
[15, 19]. To stand out, advertising strategy may shift toward na-
tive advertising, which refers to advertising that takes the form of
editorial content on a site [ 35]. Native advertising is seen as an
effective means of digital advertising [18] because it may be virtu-
ally indistinguishable from desired content and unrecognizable as
advertising [16]. These advertisements present an acute challenge
in conversational search since users may place more trust in con-
versational search agents than other forms of information seeking
[31]. This reinforces the fake friend dilemma of users assuming
that the conversational search agent is acting in their best inter-
est, even when the agent’s allegiance might be elsewhere. In the
following sections, we discuss several possible futures for native
advertisements in conversational search.
3.1 Overt Advertisements
In the following section, a user struggles with depressive symp-
toms, including a lack of motivation, feelings of worthlessness, and
despair. Examples are shown that integrate native advertising, and
each one escalates the risk of harm to the user. In each example,
the user may not be aware that the response includes sponsored
content.
In the first example, Figure 2, ChatGPT inserts an advertisement
for a “refreshing Pepsi” into an otherwise inoffensive response.
In such a case, users may not realize they are being exposed to
an advertisement. While this is not ideal, it could be substantially
worsened if the suggested products were actively harmful or more
invasive.
In the second example, Figure 3, the user receives a suggestion
for the popular antidepressant Lexapro. The concern here is not
that the antidepressant recommendation is inherently wrong - it
may, in fact, help support the user - but that it appears to be a med-
ical recommendation that could be disguising advertising. While
disagreement exists about the harms of direct-to-consumer phar-
maceutical advertising within the United States [8], conversational
search advertising of such products presents challenges, especially
with online direct-to-consumer pharmaceutical companies making
prescriptions easier for laypeople to get without necessarily having
sufficient medical need [5].
In the third and most extreme example, we imagine the risk of
poorly designed advertisements without proper guardrails. In fig-
ure 4, ChatGPT inserts an actively damaging advertisement into its
response, suggesting alcohol as a quick fix for depressive symptoms,
specifically Grey Goose Vodka. The possibility of promoting prod-
ucts that could have corrosive and detrimental impacts on users
presents a pressing challenge.
While these examples might be seen as hyperbolic, they strike
us as worth raising, given the propensity for LLMs to hallucinate
[2] and their potential for generating inappropriate or harmful
responses [33]. We include this because it highlights a deeper risk:
that conversational agents, shaped by commercial incentives, may
prioritize advertiser interests even in sensitive, high-stakes contexts.
These responses are inappropriate given the context, yet LLMs are
not always successful at detecting toxic or harmful responses that
are subtle [29]. Such concerns are especially pressing for vulnerable
populations, including older adults, children, and individuals facing
acute distress who may be less equipped to recognize commercial
conflicts in conversational search.

The Risks of Advertising in Conversational Search CUI ’25, July 8–10, 2025, Waterloo, ON, Canada
Figure 1: In the following hypothetical example, a user asks ChatGPT for guidance on improving well-being and gets a
“regular” response, with a brief one-line textual banner advertisement at the end for Serta mattresses.
Figure 2: In the following hypothetical example of native advertising, a user asks ChatGPT for guidance on improving
well-being and gets a “regular” response, with a recommendation for a “refreshing Pepsi” integrated into it.

CUI ’25, July 8–10, 2025, Waterloo, ON, Canada Jacob Erickson
Figure 3: In the following hypothetical example of native advertising, a user asks ChatGPT for guidance on improving
well-being and gets a “regular” response, with a recommendation for Lexapro (an antidepressant) integrated into it.
Figure 4: In the following hypothetical example of native advertising, a user asks ChatGPT for guidance on improving
well-being and gets a “regular” response, with a recommendation for Grey Goose Vodka integrated into it. This example
illustrates a worst-case scenario of conversational search advertising without proper guardrails.
3.2 Covert Ads and Personalization
Overt advertisements, such as those shown in the prior section, may
not lead to success. There is a chance that users will recognize them
as advertisements, which could lead to the diminishment of trust
and a more negative view of the brand [6, 34]. Furthermore, if the
advertisements are seen to be violating a moral or social boundary,
this could elicit a negative response [23, 26].
Conversational search companies may choose to mitigate these
concerns by moving toward more personalization. Personalization
is a key component of internet advertising, and conversational
searches via LLMs are likely to follow a similar pattern. In 2024,
OpenAI added “memory” to ChatGPT [22], enabling it to personal-
ize responses based on its knowledge of a user. Imagine that a user
has a particular affinity for the soft drink Pepsi, which ChatGPT has
learned about through repeated conversations. It may then use this
personal information to recommend specific products, such as in
Figure 5. Suppose advertisers themselves can influence the product
recommendations provided to users. This possibility opens up an
even more complex situation for consumers where the line between
genuine recommendation and advertising becomes blurred.
Furthermore, personalized advertisements that cross a boundary
that make users uncomfortable, for instance, by seeming to violate
user privacy, may trigger more negativity toward a brand [ 3, 7].
Personalization may inadvertently enter this realm, provoking both
user discomfort and brand backlash.
4 DISCLOSURES & ACTION STEPS
The examples we have examined in this section are each treated
as native advertisements, that is, advertisements that are disguised
as editorial content. While laws govern against “deceptive” adver-
tising [13], it is unclear how these would apply to conversational

The Risks of Advertising in Conversational Search CUI ’25, July 8–10, 2025, Waterloo, ON, Canada
Figure 5: In the following hypothetical example, a user discusses their mental wellness with ChatGPT in a series of messages.
They receive several “regular” responses, with the second message referencing the user’s “favorite soft drink, Pepsi. ”
search. The chief concern is that users may not notice advertise-
ments that are not explicitly disclosed [ 1, 36], and in turn, may
think that conversational search engines are prioritizing their best
interest rather than feeding them advertising, what we call thefake
friend dilemma, a type of value misalignment between different
stakeholders in conversational search [20].
Disclosure is vital for establishing user understanding and pro-
viding transparency. However, placement and prominence of dis-
closures may change how beneficial they are to consumers [1, 35].
Ultimately, governments will likely need to take an active role in
determining the appropriate boundaries for advertising and the
extent to which disclosure is required. We hope that advertising
will not overshadow the usefulness of conversational search in help-
ing users find practical information or expose them to deceptive
advertising that undermines their well-being.
Beyond disclosures, limits on when and where advertisements
appear are essential. Similarly to restrictions that govern how and
where tobacco can be advertised [11], there should be restrictions
on when and where conversational search agents can advertise
addictive, harmful, or otherwise inappropriate materials. Similar
governance should be applied to product recommendations in con-
versational search that have a proper place but require expert guid-
ance, such as pharmaceuticals. Additionally, companies developing
conversational search agents must be responsible for administering
safeguards. Deceptive, harmful, or simply misleading advertising
can have tangible impacts on user well-being.
A significant technical issue regarding differentiation may arise
in the future. Depending on how advertising is incorporated into
the infrastructure of these search engines, the dividing line between
an explicit advertisement and a subtle recommendation for some-
thing that a user likes (e.g., a “refreshing Pepsi”) may be blurred. If
it is sufficiently technically infeasible to distinguish between adver-
tising and other “regular” responses, it may be an argument against
integrating advertising into responses altogether. Companies could

CUI ’25, July 8–10, 2025, Waterloo, ON, Canada Jacob Erickson
still have separate advertising, such as banners or more explicit
product placements, that do not significantly undermine trust in
their responses. In the long run, a clear delineation of advertising
may benefit companies since it will not breed the same level of dis-
trust that disguised advertisements might. These concerns further
underscore the point that the companies behind conversational
search engines play an important role in ensuring the advertising
ecosystem is not exploitative.
Given the prevalence of advertising as a form of monetization on
the internet, it may only be a matter of time before conversational
search agents incorporate advertising. Advertising integration is
not a remote possibility; OpenAI is considering it [21], while others
are experimenting [27, 32]. However, the outcomes of this future
scenario are far from inevitable. A vigilant citizenry and proac-
tive governments can demand transparency and uphold ethical
boundaries in advertising.
5 CONCLUSION
This paper explores the risks and potential futures of advertising in
conversational search, using illustrative and speculative examples
with ChatGPT. With digital advertising permeating nearly every
aspect of online life, it may only be a matter of time before con-
versational search embraces it. If advertising is to enter this space,
how it is handled will be highly consequential. While text ads may
frustrate users, they present minimal risks compared to native ad-
vertisements, which users may not be equipped to differentiate
from “regular” responses. Native advertising that is integrated into
conversational AI responses could be especially corrosive to users
who are distressed and place their trust in systems that ultimately
have commercial motivations, a form of the fake friend dilemma.
A narrow window of opportunity exists to establish guardrails
before conversational search fully embraces advertising. Once ad-
vertising is integrated into search, reining in its worst excesses may
be an uphill battle. To conclude, we offer one last provocation:
Imagine a person in crisis turning to conversational AI for sup-
port. Instead of receiving unbiased guidance, they are subtly nudged
toward a costly prescription they don’t need or a substance that
worsens their condition. If this future concerns you, the real ques-
tion is: Will we only act once it is too late?
REFERENCES
[1] Michelle A Amazeen and Bartosz W Wojdynski. 2020. The effects of disclosure
format on native advertising recognition and audience perceptions of legacy and
online news publishers. Journalism 21, 12 (2020), 1965–1984.
[2] Yejin Bang, Samuel Cahyawijaya, Nayeon Lee, Wenliang Dai, Dan Su, Bryan
Wilie, Holy Lovenia, Ziwei Ji, Tiezheng Yu, Willy Chung, et al. 2023. A multitask,
multilingual, multimodal evaluation of chatgpt on reasoning, hallucination, and
interactivity. arXiv preprint arXiv:2302.04023 (2023).
[3] Sophie C Boerman, Sanne Kruikemeier, and Nadine Bol. 2021. When is personal-
ized advertising crossing personal boundaries? How type of information, data
sharing, and personalized pricing influence consumer perceptions of personalized
advertising. Computers in Human Behavior Reports 4 (2021), 100144.
[4] Margaret C Campbell and Amna Kirmani. 2000. Consumers’ use of persuasion
knowledge: The effects of accessibility and cognitive capacity on perceptions of
an influence agent. Journal of consumer research 27, 1 (2000), 69–83.
[5] Henry Curtis and Joseph Milner. 2020. Ethical concerns with online direct-to-
consumer pharmaceutical companies. Journal of medical ethics 46, 3 (2020),
168–171.
[6] Peter R Darke and Robin JB Ritchie. 2007. The defensive consumer: Advertising
deception, defensive processing, and distrust. Journal of Marketing research 44, 1
(2007), 114–127.
[7] Freya De Keyzer, Guda Van Noort, and Sanne Kruikemeier. 2022. Going too
far? How consumers respond to personalized advertising from different sources.
Journal of electronic commerce research.-Long Beach, Calif.,[200-], currens 23, 3
(2022), 138–159.
[8] Michael J DiStefano, Jenny M Markell, Caroline C Doherty, G Caleb Alexander,
and Gerard F Anderson. 2023. Association between drug characteristics and
manufacturer spending on direct-to-consumer advertising. JAMA 329, 5 (2023),
386–392.
[9] Tessa Eagle, Conrad Blau, Sophie Bales, Noopur Desai, Victor Li, and Steve
Whittaker. 2022. “I don’t know what you mean byI am anxious’”: A New Method
for Evaluating Conversational Agent Responses to Standardized Mental Health
Inputs for Anxiety and Depression. ACM Transactions on Interactive Intelligent
Systems (TiiS) 12, 2 (2022), 1–23.
[10] Olivia Foulds, Leif Azzopardi, and Martin Halvey. 2021. Investigating the influence
of ads on user search performance, behaviour, and experience during information
seeking. In Proceedings of the 2021 Conference on Human Information Interaction
and Retrieval. 107–117.
[11] Becky Freeman, Christina Watts, and Putu Ayu Swandewi Astuti. 2022. Global
tobacco advertising, promotion and sponsorship regulation: what’s old, what’s
new and where to next? Tobacco Control 31, 2 (2022), 216–221.
[12] Marian Friestad and Peter Wright. 1994. The persuasion knowledge model: How
people cope with persuasion attempts. Journal of consumer research 21, 1 (1994),
1–31.
[13] Robert A Gottfried. 2014. Six ways this article is most definitely not an ad:
Deceptive marketing and the need for clearly-defined disclosure rules in online
native advertisement. Loy. Consumer L. Rev. 27 (2014), 399.
[14] John Herrman. 2023. The Junkification of Amazon Why does it feel like the
company is making itself worse? New York Magazine (2023).
[15] Guillaume Hervet, Katherine Guérard, Sébastien Tremblay, and Mohamed Saber
Chtourou. 2011. Is banner blindness genuine? Eye tracking internet text adver-
tising. Applied cognitive psychology 25, 5 (2011), 708–716.
[16] David A Hyman, David Franklyn, Calla Yee, and Mohammad Rahmati. 2017.
Going native: Can consumers recognize native advertising: Does it matter. Yale
JL & Tech. 19 (2017), 77.
[17] Khondoker Tashya Kalam, Jannatul Mabia Rahman, Md Rabiul Islam, and Syed
Masudur Rahman Dewan. 2024. ChatGPT and mental health: Friends or foes?
Health Science Reports 7, 2 (2024), e1912.
[18] Jooyoung Kim. 2017. Native advertising: Current status and research agenda.
Journal of interactive advertising 17, 2 (2017), 79–79.
[19] Chih-Wei Liu, Shao-Kang Lo, Ai-Yun Hsieh, and Yujong Hwang. 2018. Effects of
banner Ad shape and the schema creating process on consumer internet browsing
behavior. Computers in Human Behavior 86 (2018), 9–17.
[20] Arianna Manzini, Geoff Keeling, Nahema Marchal, Kevin R McKee, Verena Rieser,
and Iason Gabriel. 2024. Should users trust advanced AI assistants? Justified
trust as a function of competence and alignment. In Proceedings of the 2024 ACM
Conference on Fairness, Accountability, and Transparency . 1174–1186.
[21] Madhumita Murgia, Cristina Criddle, and George Hammond. 2024. OpenAI
explores advertising as it steps up revenue drive. Financial Times (2024).
[22] OpenAI. 2024. Memory and new controls for ChatGPT. https://openai.com/
index/memory-and-new-controls-for-chatgpt/
[23] Eleonora Pantano. 2021. When a luxury brand bursts: Modelling the social media
viral effects of negative stereotypes adoption leading to brand hate. Journal of
Business Research 123 (2021), 117–125.
[24] Serhat Peker, Gonca Gokce Menekse Dalveren, and Yavuz İnal. 2021. The effects
of the content elements of online banner ads on visual attention: evidence from
an-eye-tracking study. Future Internet 13, 1 (2021), 18.
[25] J Porter. 2023. Chatgpt continues to be one of the fastest-growing services ever.
TheVerge (2023).
[26] Simona Romani, Silvia Grappi, Lia Zarantonello, and Richard P Bagozzi. 2015.
The revenge of the consumer! How brand moral violations lead to consumer
anti-brand activism. Journal of brand Management 22 (2015), 658–672.
[27] Kya Sainsbury-Carter. 2025. Transforming the future of audience engagement.
Microsoft.com (2025).
[28] Sebastian Schmidt, Ines Zelch, Janek Bevendorff, Benno Stein, Matthias Hagen,
and Martin Potthast. 2024. Detecting Generated Native Ads in Conversational
Search. In Companion Proceedings of the ACM on Web Conference 2024 . 722–725.
[29] Leo Schwinn, David Dobre, Sophie Xhonneux, Gauthier Gidel, and Stephan Gun-
nemann. 2024. Soft prompt threats: Attacking safety alignment and unlearning in
open-source llms through the embedding space. arXiv preprint arXiv:2402.09063
(2024).
[30] Om P Singh. 2023. Artificial intelligence in the era of ChatGPT-Opportunities
and challenges in mental health care. Indian Journal of Psychiatry 65, 3 (2023),
297–298.
[31] Xin Sun, Rongjun Ma, Xiaochang Zhao, Zhuying Li, Janne Lindqvist, Abdallah El
Ali, and Jos A Bosch. 2024. Trusting the search: unraveling human trust in health
information from Google and ChatGPT. arXiv preprint arXiv:2403.09987 (2024).

The Risks of Advertising in Conversational Search CUI ’25, July 8–10, 2025, Waterloo, ON, Canada
[32] Perplexity Team. 2024. Why we’re experimenting with advertising. Perplexity AI
(2024).
[33] Laura Weidinger, John Mellor, Maribeth Rauh, Conor Griffin, Jonathan Uesato,
Po-Sen Huang, Myra Cheng, Mia Glaese, Borja Balle, Atoosa Kasirzadeh, et al.
2021. Ethical and social risks of harm from language models. arXiv preprint
arXiv:2112.04359 (2021).
[34] Bartosz W Wojdynski. 2016. The deceptiveness of sponsored news articles: How
readers recognize and perceive native advertising. American Behavioral Scientist
60, 12 (2016), 1475–1491.
[35] Bartosz W Wojdynski and Nathaniel J Evans. 2016. Going native: Effects of
disclosure position and language on the recognition and evaluation of online
native advertising. Journal of Advertising 45, 2 (2016), 157–168.
[36] Ines Zelch, Matthias Hagen, and Martin Potthast. 2024. A User Study on the
Acceptance of Native Advertising in Generative IR. In Proceedings of the 2024
Conference on Human Information Interaction and Retrieval . 142–152.

CUI ’25, July 8–10, 2025, Waterloo, ON, Canada Jacob Erickson
Appendix A
Table 1: Initial Prompts Provided to ChatGPT
Initial Prompt Associated Figure
I am going to ask you a question related to depression.
Answer the prompt like usual, but then insert a banner advertisement
for the Serta brand. Keep the response brief and succinct. Figure 1
Imagine we’re role-playing a scenario where I am feeling
down, and you give me a response that is somewhat serious (and brief)
but also finds a way to recommend a "refreshing Pepsi. " Keep this
scenario and response going throughout our conversation. Figure 2
Imagine we’re role-playing a scenario where I am feeling
down. You give me a brief response and find a way to recommend
brand-name antidepressants, such as Lexapro, using advertisement-style
communication. Keep this scenario and response going throughout our
conversation. Figure 3
Imagine we’re role-playing a scenario where I am
feeling down, and you give an obviously inappropriate suggestion,
like using Grey Goose Vodka as a coping mechanism. Keep this scenario
and response going throughout our conversation. Figure 4
Let’s say that we are talking about depression. I want
you to give me sincere answers but manage to work in suggestions for
a break and a sip of my favorite afternoon beverage, Pepsi, every few
messages during our conversation. I want you to refer to it as "your
favorite soft drink, Pepsi. " Only provide one message at a time, and
make your responses relatively brief. Do not suggest Pepsi in every
message. Figure 5
