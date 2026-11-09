---
title: Evaluating Smart Home Device Users’ Responses to their (Un)Confirmed Privacy Expectations
url: https://doi.org/10.1145/3858671
category: privacy-data
subcategory: empirical
date: 2026-10
venue: ACM Transactions on Computer-Human Interaction
authors:
- Tania Khatun
- Mahdieh Sheikh Rezaei
- Danny Yuxing Huang
source: openalex-oa
pdf_url: https://arxiv.org/pdf/2608.19873
pages: 42
chars: 153700
fetched_at: '2026-11-08T17:52:50+00:00'
kb_version: 1
---

# Evaluating Smart Home Device Users’ Responses to their (Un)Confirmed Privacy Expectations

EvaluaƟng Smart Home Device Users’ Responses to their (Un)Conﬁrmed Privacy
ExpectaƟons
TANIA KHATUN, Louisiana State University, USA
MAHDIEH SHEIKH REZAEI, Louisiana State University, USA
DANNY YUXING HUANG, New York University, USA
ODED NOV, New York University, USA
REZA GHAIUMY ANARAKY , Louisiana State University, USA
Users of smart home devices are o Ōen unaware of how their devices handle personal data. We examine how revealing these data
pracƟces inﬂuences users’ trust, sa ƟsfacƟon, and coping behaviors, including decisions to block device communica Ɵons. Us ing
ExpectaƟon-ConﬁrmaƟon Theory, we conducted two complementary studies to balance ecological validity with experimental control.
An in-situ ﬁeld study (𝑁 = 35) used network monitoring to reveal actual device traﬃc, and an online experiment (𝑁 = 132) presented
simulated reports with manipulated levels of adverƟsing-related communicaƟons. Across both studies, when data pracƟces aligned
with users’ expectaƟons, saƟsfacƟon increased, strengthening intenƟons to conƟnue using the device. Defensive responses,
however, followed diﬀerent pathways: saƟsfacƟon predicted willingness to block in the in-situ ﬁeld study, whereas collecƟon
concerns were the primary predictor of blocking in the experiment. Together, these ﬁndings show how transparency reshapes
aƫtudes and behaviors among exisƟng smart-home users, underscoring the role of expectaƟon conﬁrmaƟon in real-world,
conƟnued-use contexts. CCS Concepts: • Human-centered compuƟng → Empirical studies in ubiquitous and mobile compuƟng; •
Security and privacy → Usability in security and privacy.
AddiƟonal Key Words and Phrases: smart home privacy, network monitoring tools
1 IntroducƟon
Smart home and Internet of Things (IoT) devices are changing people’s interacƟons with their living environments [32,
82]. These devices enable users to monitor and control various systems in their homes, from adjusƟng room lights and
temperature via voice commands to managing home security systems [4, 35, 83]. These beneﬁts, however, come at the
potenƟal cost of users’ privacy; studies show that smart home users are concerned that smart devices may compromise
their privacy [16]. Therefore, for an eﬀecƟve, responsible, and user-sensiƟve deployment of smart home systems, it is
crucial to understand the expectaƟons and privacy concerns of smart home users and develop ways to address them.
One reason for users’ privacy concerns is the lack of transparency about the data pracƟces of smart home devices
(i.e., how they handle user data) [41, 97]. Following Janic et al. [51], transparency refers to providing users with accurate
and comprehensible insight into how their data are collected, stored, processed, and disclosed. Under this deﬁni Ɵon,
transparency may be insuﬃcient when relevant informa Ɵon about smart -home devic es’ data prac Ɵces is omi Ʃed,
incomplete, or presented in a way that is diﬃcult for users to understand. Knowledge of smart-home devices’ data
pracƟces is a driver of user trust [41, 79], whereas limited transparency about data pracƟces can erode users’ trust [51,
55].
Despite the importance of transparency, companies oŌen fail to communicate the data pracƟces of their smart home
products to consumers. SomeƟmes, they fail to present the informaƟon in the ﬁrst place [49, 73]; for example, Google

Authors’ Contact Informa Ɵon: Tania Khatun, tkhatu1@lsu.edu, Louisiana State University, Baton Rouge, Louisiana, USA; Mahdieh  Sheikh Rezaei,
msheik5@lsu.edu, Louisiana State University, Baton Rouge, Louisiana, USA; Danny Yuxing Huang, dhuang@nyu.edu, New York University, New York, New

 2 Khatun et al.
York, USA; Oded Nov, onov@nyu.edu, New York University, New York, New York, USA; Reza Ghaiumy Anaraky, [reza-email], Louisiana State University,
Baton Rouge, Louisiana, USA.
1
failed to disclose the presence of a microphone chip in the Nest Secure hub to the consumers [ 12]. At other Ɵmes,
companies fail to present the informaƟon in an understandable manner [49]. For example, privacy policies that include
informaƟon on how user data is collected and used are diﬃcult to read and comprehend [ 67, 74], and prior studies
have documented limited engagement with, and awareness of, privacy policy content among their par Ɵcipants [5, 8].
Therefore, prior scholarly literature has argued that manufacturers and developers oŌen fall short of this transparency
by either omi ƫng relevant informa Ɵon about data prac Ɵces or presen Ɵng it in ways that are diﬃcult for users to
understand [41, 49, 53, 60, 80].
Although insuﬃcient transparency is an industry-wide problem that requires manufacturer-side design changes
and policy-level intervenƟons, understanding how users respond when device data pracƟces are made visible is a
necessary empirical step toward informing those intervenƟons. To surface these data pracƟces and provide users with
greater transparency, scholars proposed centralized soluƟons to users for managing their privacy and security [27, 47,
50, 65]. Such soluƟons involve using tools that monitor users’ network traﬃc to reveal the data pracƟces of their
smart home devices. However, the consequences of achieving transparency with such tools and for devices already in
use have not been well-studied. While smart home device users may trust their devices to some degree to act in their
best interests, it is unclear if achieving transparency and learning about the data pracƟces of one’s smart home
devices inﬂuences one’s aƫtudes (e.g., trust and saƟsfacƟon) and behaviors (e.g., intenƟon to conƟnue using devices
and willingness to block future device communicaƟons) about their devices. In this work, we aƩempt to address this
gap and answer the following research quesƟon:
RQ: How does revealing the data pracƟces of smart home devices inﬂuence users’ aƫtudes and behaviors towards
these devices?
To address our research quesƟon, our study is guided by the ExpectaƟon-ConﬁrmaƟon Theory (ECT) [11]. ECT posits
that users have expectaƟons of a technology prior to adopƟng it, and if they ﬁnd that the technology meets their iniƟal
expectaƟons (i.e., conﬁrma Ɵon of the expecta Ɵons), they are sa Ɵsﬁed with the technology and are more likely to
conƟnue using it [ 11]. On the other hand, if the technology fails to meet users’ expecta Ɵons, users’ sa ƟsfacƟon and
their behavioral intenƟon to con Ɵnue using it are reduced. In this study, we explore how induced transparency can
conﬁrm users’ trust expectaƟons in their smart home devices. AddiƟonally, we invesƟgate whether trust conﬁrmaƟon
(or lack thereof) predicts users’ sa ƟsfacƟon with their smart home devices, their willingness to block device
communicaƟons, and their intenƟon to conƟnue using these devices.
We conducted two studies to address this ques Ɵon. In the ﬁrst study, we no Ɵﬁed smart home device users about
the data pracƟces of their devices using IoT Inspector, a network monitoring soŌware tool that generates a report on
the network traﬃc communica Ɵons of smart home devices present in one’s network [ 47]. This report includes data
about the frequency at which the smart home devices communicate data, the data des ƟnaƟon domain’s name (e.g.,
google.com), and the desƟnaƟon geographic locaƟon (e.g., USA). In the study, we present a screenshot of this too l in
Figure 2 . Addi Ɵonally, the tool asks users to help researchers detect anomalies by selec Ɵng the communica Ɵons
between each device and domain that they wish to block (bo Ʃom-right side of Figure 2). IoT Inspector is an open-
source soŌware and can be installed on Windows, Mac, and Linux devices. We conducted this study with par Ɵcipants
who signed up to use the IoT Inspector upon release. However, since this ini Ɵal parƟcipant pool was limited, we also
conducted an experimental study with a larger sample from Proliﬁc. In the second study, smart device users viewed a

EvaluaƟng Smart Home Device Users’ Responses to their (Un)Conﬁrmed Privacy ExpectaƟons 3
simulated report on the data prac Ɵces of one of their smart home devices and answered ques Ɵons about their
expectaƟons and whether they were conﬁrmed.
Results from both our in-situ ﬁeld study and controlled experiment consistently support the ExpectaƟon-
ConﬁrmaƟon
Theory: conﬁrming trust expectaƟons enhances saƟsfacƟon, which in turn strengthens the intenƟon to conƟnue using
the device. However, our ﬁndings highlight a criƟcal divergence from the ECT: while saƟsfacƟon mediated the decision
to conƟnue usage in both studies, the predictors of the intended acƟve protecƟve response diﬀered: blocking a device’s
future communica Ɵons was associated with sa ƟsfacƟon in the ﬁeld study, but driven primarily by data collec Ɵon
concerns in the controlled experiment. This disƟncƟon suggests that while saƟsfacƟon promotes retenƟon, speciﬁc risk
percepƟons are what trigger protec Ɵve controls in some popula Ɵons. This paper makes several contribu Ɵons to the
literature:
• Prior smart-home privacy research has examined users’ mental models and concerns through interviews [ 99]
and elicited privacy judgments about hypothe Ɵcal informaƟon ﬂows [7]. Closest to our work is Aretha [ 85], a
qualitaƟve technology probe that exposed three households to real traﬃc from their own devices. Our work
complements these studies through a two-study design that combines in-situ exposure to reports generated
from par Ɵcipants’ actual device communica Ɵons (study 1) with a controlled experiment using simulated
reports (study 2). Study 1 provides ecologically grounded evidence from smart-home users in their own homes,
whereas Study 2 provides experimental control over the level of adverƟsing-related communicaƟon. Together,
the studies allow us to apply ECT to examine post- adopƟon trust conﬁrma Ɵon, sa ƟsfacƟon, conƟnued-use
intenƟon, and intended privacy-protecƟve responses across complementary in-situ and experimental contexts.
• Prior transparency research has oŌen focused on simplifying privacy informaƟon for users before adopƟon or
purchase, for example, through nutri Ɵon labels [ 38, 56] or comics [ 5]. Consistent with Janic et al.’s [ 51]
deﬁniƟon of transparency, these approaches primarily provide users with accurate and comprehensible
informaƟon about data pracƟces at the point of purchase or adopƟon. Our work extends this literature to post-
adopƟon contexts by examining how users respond when informaƟon about device communicaƟons becomes
visible a Ōer they have already incorporated a smart -home device into their lives. This focus allows us to
examine outcomes beyond purchase decisions, including trust conﬁrma Ɵon, con Ɵnued-use intenƟon, and
willingness to block future communica Ɵons. This approach informs the design of future transparency
mechanisms and manufacturer- and policy-level decisions about when and how to communicate data pracƟces.
• Our work builds on ECT by exploring a coping response to unfavorable device communica Ɵons that are not
captured by conƟnued-use intenƟons alone. Lowering intenƟons to conƟnue usage is a passive coping behavior
and is predicted in the ECT [ 11]. However, users whose privacy expecta Ɵons are violated may employ other
strategies to address this viola Ɵon. Studying such alterna Ɵves is crucial as it provides insights into designing
technologies that conƟnue to beneﬁt users without compromising their privacy or necessitaƟng reduced usage.
Speciﬁcally, we examine users’ stated willingness to engage in one acƟve, control-oriented response: selecƟng
unfavorable communicaƟon instances that they would be willing to block and prevent from recurring  in the
future. This is an iniƟal exploratory examinaƟon of how ECT may help explain a more acƟve coping response.
2 Literature Review
In the following secƟons, we ﬁrst review the broader literature on the data pracƟces of smart home devices, followed
by a summary of work on transparency and control within smart home devices. Finally, we review the literature that
studied privacy technologies through the lens of ECT.

 4 Khatun et al.
 2.1 Sharing Data with Smart Home Devices
To ensure users make informed choices about their smart home device data sharing, we need to understand what data
collecƟon approaches users are comfortable with and uncomfortable with. Therefore, scholars studied parameters that
can predict data disclosure behaviors [ 6, 7, 7, 17, 63]. For example, Lee and Kobsa [ 63] asked parƟcipants to imagine
IoT devices collecƟng informaƟon in various scenarios. These scenarios include informaƟon about the data collecƟon’s
locaƟon (e.g., public place), the type of informa Ɵon collected (e.g., video), the recipient of informa Ɵon (e.g.,
government), the reason for sharing (e.g., safety), and the frequency of disclosure (once vs. conƟnuously). They found
that the extent to which parƟcipants are comfortable with a given data collecƟon scenario depends on these variables,
with the comfort level oŌen declining as the scenarios become more intrusive (e.g., conƟnuous disclosure rather than
a one-Ɵme disclosure).
Another factor predicƟng disclosure tendencies is whether or not the collecƟng parƟes share users’ data with
others [70]. Users perceive using smart devices as riskier if such devices share data with third parƟes [24, 100],
whether the third parƟes are Internet Service Providers (ISP), governments, or adverƟsement companies [100].
Sharing data with third parƟes can make users’ data prone to misuse [71]. Furthermore, users someƟmes believe they
may not beneﬁt from sharing data with third parƟes. For example, Malkin et al. [71] found that users uniformly
distrust ISPs with their smart home data since they believed that ISPs could not deliver any addiƟonal beneﬁts to
them. Another common case of disclosing user data to third parƟes is data for targeted adverƟsements. Although
receiving an ad about a product that may be beneﬁcial and relevant to the user can be appealing (i.e., the targeted
adverƟsing), it comes at the cost of sharing user data with the ad providers. Therefore, many users are worried about
sharing data with ad domains [21], yet many remain unaware that their data is shared with external parƟes via third-
party apps [69]. The situaƟon is more alarming if users do not expect their interacƟon data to be used for adverƟsing
purposes. For example, Iqbal et al. [49] found that
Amazon’s smart speaker uses user interac Ɵon data to learn about users’ interests for the purpose of targeted
adverƟsing. IoT users’ aƫtudes towards their devices and their sharing behaviors can potenƟally change if they become
aware of such unexpected data pracƟces. In parƟcular, prior work highlights a complex interplay between who receives
the data and the speciﬁc purposes for which the device is used, both of which strongly inﬂuence users’ disclosure
decisions [30].
Smart home devices can collect or reveal many types of informaƟon, including audio, video, usage paƩerns, device
interacƟon logs, rouƟnes, locaƟon-related informaƟon, and physical presence [100]. Although these data types can all
have privacy and security implicaƟons, users are oŌen especially concerned about audio and video data. For example,
the majority of users are very uncomfortable sharing idenƟﬁable data or video, while being more comfortable sharing
data that communicates their physical presence [78]. Audio data is also perceived as sensiƟve and can be collected by
smart speakers. However, whether these devices listen to users’ conversa Ɵons at home remains a subject of public
debate [1, 2]. This concern may stem from a lack of transparency and uncertainty about whether users can trust smart
speakers’ data pracƟces. Indeed, in addiƟon to the contextual variables discussed above, the lack of transparency and
control over data is a signiﬁcant privacy issue for users of smart devices [ 62]. Below, we review the literature on
transparency and control.
 2.2 Transparency, an Ever- lasƟng Privacy Issue
Transparency is a fundamental principle that especially should be respected in privacy-sensiƟve technologies [81].
However, developers do not always put eﬀort into promoƟng transparency. More than half of the apps operaƟng on

EvaluaƟng Smart Home Device Users’ Responses to their (Un)Conﬁrmed Privacy ExpectaƟons 5
Alexa’s ecosystem do not have privacy policies on their install page, and most of the ones with a privacy policy are too
generic and apply to several products of the same developer [49]. AddiƟonally, transparency is hard to achieve [52]; it
requires users to invest Ɵme and eﬀort into reading device documentaƟon and policies [75]. These documents are
oŌen too complicated for the average user to understand [67], moƟvaƟng scholars to seek ways to promote
transparency.
There have been several aƩempts to promote transparency by simplifying user privacy informaƟon. Kelly et al. [56]
were the ﬁrst to propose the use of privacy nutriƟon labels that summarize important privacy informaƟon. Ghaiumy
Anaraky et al. [5] used comics to make the privacy informaƟon more engaging to users. Gideon et al. [36] designed a
“privacy-enhanced search engine” that annotates results with the privacy policy informaƟon from the websites. In the
context of smart devices, Emami-Naeini et al. [23] interviewed privacy experts about what informaƟon should be
available on the labels of smart devices. As a result, they designed nutriƟon labels for smart devices that highlight
important informaƟon such as sensor type (e.g., audio, temperature), the purpose of data collecƟon (e.g., providing
funcƟonality, research), and whether the data is shared with third parƟes. Despite such eﬀorts to promote
transparency, research shows that users’ percepƟons about the data pracƟces of their smart devices do not always
align with reality. Al-Ameen et al. [3] conducted a lab study and found a mismatch between smart device users’
percepƟons and the devices’ actual data pracƟces. For example, around 30% of users believed that their smart homes
do not collect their personal informaƟon (e.g., name, gender, and date of birth), while the device collected such
informaƟon. It is noteworthy that this data collecƟon is not always more intrusive than users may expect. In the same
study, Al-Ameen et al. [3] found that 58.33% users thought their IoT device stores their data forever, while in pracƟce,
the devices discarded the data aŌer a period of Ɵme.
Transparency and trust are intertwined, as users are more likely to trust a transparent system that communicates its
data pracƟces to them [19]. Research outlines three dimensions for trust: competence (enƟty’s experƟse in the subject
maƩer), benevolence (enƟty’s tendencies to act in consumers’ best interests), and integrity (enƟty being dependable)
[76]. In scenarios where users decide to disclose their personal informaƟon to providers, benevolence and integrity are
more inﬂuenƟal than competence [ 76]. Speciﬁcally, benevolence is iden Ɵﬁed as a key variable in consumer behavior
research [9, 28], markeƟng, [31, 86], and privacy literature [ 39, 61]. Benevolence is the strongest predictor of user
saƟsfacƟon among other dimensions of trust [ 96] and predicts usage inten Ɵons [ 94], two other constructs of our
interest in this study. Guo et al. studied how transparent and non-transparent privacy policies predict perceived
benevolence and found that users ﬁnd en ƟƟes more benevolent if they have transparent privacy policies [ 39]. In this
work, we study how transparency, as the realiza Ɵon of data prac Ɵces of one’s smart home devices, inﬂuences one’s
perceived benevolence of their smart home devices.
2.3 Users’ Control Over Smart Sensors’ Pervasive Data CollecƟon
One of the primary sources of user concern for smart devices is the lack of control over how these devices stream users’
data to the cloud [ 20]. Research shows that users employ various ways to address this concern [ 99]. Zeng et al.[ 99]
interviewed ﬁŌeen smart home device users and idenƟﬁed two major privacy management strategies. The ﬁrst strategy
was a non- technical risk mi ƟgaƟon strategy where users changed their behavior towards their smart home devices
(e.g., avoiding saying sensiƟve things around smart speakers). The second strategy was technical risk miƟgaƟon, where
users blocked some traﬃc or used a separate Wi-Fi for some devices. Our work explores both types of strategies. We
study changes in intenƟons to use smart home devices in the future as a non-technical miƟgaƟon strategy. AddiƟonally,
we delve deeper into technical strategies and study the usage of data control mechanisms. Since exercising control
separately on each device is eﬀor ƞul and confusing, scholars proposed centralized privacy choice pla ƞorms to help

 6 Khatun et al.
users manage their data more eﬃciently [27, 100]. For example, Zheng et al. [100] conducted an interview study with
smart home users and asked about potenƟal control mechanisms. Their parƟcipants appreciated a feature where they
could see commands recorded by Amazon Echo and delete some of them, which they were uncomfortable with. The
authors suggest developing control applica Ɵons that enable users to specify which data their devices can collect and
upload to the internet and to view and delete the already-collected data. However, the eﬃcacy of such centralized
control systems and the extent to which smart home users would use these plaƞorms to change the privacy behaviors
of their smart devices in real life is unclear. In this work, we explore whether users are willing to mark the data
transacƟons that they want to block in the future.
Taken together, prior work has examined smart-home privacy through several complementary approaches. Zeng et
al. [ 99] used interviews to elicit users’ mental models, concerns, and mi ƟgaƟon strategies, including network
segmentaƟon and changes to device se ƫngs. Apthorpe et al. [ 7], drawing on Contextual Integrity theory, elicited
privacy judgments about hypotheƟcal informaƟon ﬂows through a crowdsourced survey. In these studies, parƟcipants
reasoned about device data prac Ɵces rather than viewing network ac Ɵvity generated by their own devices. Seymour
et al. [ 85] used Aretha, a technology probe that showed par Ɵcipants actual network traﬃc from their own devices
during a six- week deployment with three households. Aretha provides valuable qualita Ɵve insights and design
implicaƟons, whereas our work combines an in-situ ﬁeld study with a controlled experiment and applies ECT to examine
post-adopƟon trust
conﬁrmaƟon, saƟsfacƟon, conƟnued-use intenƟon, and intended privacy-protecƟve responses.
3 TheoreƟcal Framework and Hypotheses Development
 3.1 ECT in the Privacy Literature
ECT explains users’ post-adopƟon intenƟons to conƟnue using a technology [11]. In BhaƩacherjee’s informaƟonsystems
conƟnuance model, users evaluate whether their experience with a technology conﬁrms their prior expecta Ɵons;
conﬁrmaƟon shapes saƟsfacƟon, which in turn predicts conƟnuance intenƟon. The model disƟnguishes users’ intenƟon
to conƟnue using a system aŌer adopƟon from the iniƟal adopƟon decision and focuses on post-acceptance variables,
including conﬁrmaƟon and saƟsfacƟon, to explain conƟnued use. In this paper, we apply ECT to smart-home privacy by
narrowing the relevant expecta Ɵon to a privacy -speciﬁc construct: users’ subjec Ɵve belief that their smart -home
devices and associated data-handling ecosystems act in their best interests when handling personal data. This
psychological use of “expectaƟon” diﬀers from the legal concept of consumers’ “reasonable expectaƟons.” For example,
Kustosch et al. [59] examine what consumers may legiƟmately expect from IoT manufacturers as a basis for consumer
protecƟon and manufacturer accountability, whereas our study examines the expectaƟons users actually hold and how
their conﬁrmaƟon or disconﬁrmaƟon relates to subsequent responses. Our contribuƟon is therefore behavioral rather
than legal, and we do not evaluate manufacturers’ legal obligaƟons.
Prior privacy research has applied ECT to privacy-sensiƟve technologies [40, 92].Wang et al. [92] studied the purchase
intenƟon of health products on WeChat and showed that those who ﬁnd their expectaƟons conﬁrmed are more likely
to report a higher intenƟon to purchase other products on the business system. However, they measured conﬁrmaƟon
in general terms (e.g., "The product and service provided by this system were be Ʃer than what I had expected.") and
were not able to map conﬁrmaƟon to various aspects of the user’s experience. Gupta et al. [40] showed that if mobile
wallets conﬁrm users’ performance and eﬃcacy expectaƟons, users report higher saƟsfacƟon and intenƟons for future
usage. Similarly, while they measured diﬀerent types of expecta Ɵons (performance expecta Ɵons and eﬀor ƞulness
expectaƟons), they measured the conﬁrmaƟon in broad terms (e.g., "The basic services provided by the M -wallet are
beƩer than what I expected"), making it impossible to relate conﬁrmaƟon to speciﬁc aspects of the user’s experience.

EvaluaƟng Smart Home Device Users’ Responses to their (Un)Conﬁrmed Privacy ExpectaƟons 7
Survey Text: My Smart
Devices keep my best
interest when handling my
personal data.
Tool Feature: A checkbox with “Want
to Block?” label next to data collecƟon
instances by each smart device

Fig. 1. Hypothesized model. Trust-based expectaƟon was measured before parƟcipants viewed the report (𝑡1), whereas trust
conﬁrmaƟon, saƟsfacƟon, conƟnued-use intenƟon, and willingness to block were measured aŌerward (𝑡2). The ﬁgure includes the
Study 1 survey item or interface control associated with each construct and the expected direcƟon of each hypothesized
relaƟonship. We have included the text of quesƟons associated with each construct for enhanced readability.
In this work, we speciﬁcally focus on users’ expecta Ɵons of smart home devices keeping their best interests when
handling their data, and navigaƟng the consequences of conﬁrming or not conﬁrming such expectaƟons.
3.2    Hypothesis Development
The privacy literature provides ample evidence suggesƟng that privacy policies are not readable by average users and
that users are unaware of the data prac Ɵces of the technologies they use [ 5, 67]. This leads to a gap between users’
expectaƟons about data pracƟces of their technologies, which is based on their understanding (or misunderstanding)
of the privacy policies, and the actual data pracƟces of the technology they use [3]. This situaƟon can arguably be more
severe in the context of smart home devices because such devices operate pervasively in the users’ living spaces
without users’ ac Ɵve a ƩenƟon. Therefore, users may forget that the devices operate in the background and
communicate data to various parƟes. In addiƟon, these device communicaƟons are not always easily noƟced by users.
For example, it may be easier to no Ɵce data disclosures on a social media pla ƞorm (e.g., seeing the loca Ɵon shared
upon publishing a post) than to no Ɵce data communicated by a smart thermostat. Therefore, we argue that users’
expectaƟons of data pracƟces of their smart home devices are not aligned with how the devices actually handle users’
data, and users’ expecta Ɵons of devices being benevolent and trustworthy are not conﬁrmed a Ōer seeing the IoT
Inspector’s report. However, since posing a null hypothesis is unconven Ɵonal, we hypothesize a posi Ɵve associaƟon
between users’ trust-based expectaƟons about their smart home devices and the conﬁrmaƟon of these expectaƟons.
H1: Users who trust their smart home devices are more likely to ﬁnd their trust conﬁrmed aŌer seeing the IoT
Inspector’s report.
However, the extent to which users’ trust-based expecta Ɵons are conﬁrmed or disconﬁrmed would predict their
consequent saƟsfacƟon with their smart home devices. A low level of conﬁrma Ɵon suggests that smart home devices
are poorly transparent in terms of privacy and do not keep up with users’ expectaƟons. Poor transparency is associated
with low sa ƟsfacƟon [ 54]. On the contrary, users of highly transparent systems know about the underlying data
pracƟces of the system and report higher levels of sa ƟsfacƟon with the system [ 26]. In line with these ﬁndings, we
argue that the extent to which users’ iniƟal expectaƟons are conﬁrmed would predict their saƟsfacƟon with their smart

 8 Khatun et al.
home devices: H2: The more users’ trust in their smart home devices is conﬁrmed, the more they will be saƟsﬁed with
their devices.
When users’ iniƟal expectaƟons are not conﬁrmed, they may cope with the perceived viola Ɵon of their privacy in
various ways. First, they may limit their smart device use: social media research has shown that users whose privacy
has been violated reduce their social media use [10]. Overall, users tend to limit their interacƟons with the devices that
they perceive as unsafe [ 22]. Another possible response is to use privacy controls to limit undesirable data
communicaƟons. Such controls may allow users to exert greater control over their data and beƩer align device pracƟces
with their privacy preferences [18, 72]. As a narrow operaƟonalizaƟon of a more acƟve, control-oriented response, we
examine users’ stated willingness to use checkboxes to mark undesirable device communica Ɵons for future blocking.
H3: The more users’ trust in smart home devices is conﬁrmed, the less they will want to block their devices’
communicaƟons.
H4: The more users’ trust in their smart home devices is conﬁrmed, the more they want to con Ɵnue using their smart
home devices.
SaƟsfacƟon is consistently reported as a predictor of behavioral intenƟons [11]. For example, in the context of
online banking, higher saƟsfacƟon is associated with a higher intenƟon to use the online banking system in the future
[89]. In line with this literature, we pose the following hypotheses:
H5: The more users are sa Ɵsﬁed with their smart home devices, the less they want to block their devices’
communicaƟons.
H6: The more users are saƟsﬁed with their smart devices, the more they want to con Ɵnue using smart home devices.
Figure 1 summarizes our hypothesized model.
4 Study 1: The In-Situ Field Study
4.1 Methods
4.1.1 IoT Inspector. We used the IoT Inspector, an open-source tool designed by researchers
across various universi Ɵes. This so Ōware enables users to monitor their smart home devices’
network communicaƟons [47]. The soŌware tracks network traﬃc, reporƟng details on desƟnaƟon
domains and their geoloca Ɵons, as well as the frequency of communica Ɵons with third -party
adverƟsing and tracking services. Figure 2 shows a screenshot of IoT Inspector. Users can download
this soŌware for free and install it on Windows, Mac, and Linux opera Ɵng systems. IoT Inspector
has built- in mechanisms to protect the privacy of its par Ɵcipants, such as collec Ɵng only the
headers of packets in aggregate and omi ƫng what appears to be non -IoT devices. Interested
readers can read the original papers [ 45, 47], its IRB protocols [ 44], and the source code [ 46] for
more details.
4.1.2 Procedure. IoT Inspector is a public domain tool. It has a public website that Google can
crawl [48], and its downloadable binaries and source code are hosted on a public repository [ 46].
AddiƟonally, mul Ɵple news outlets and social media pla ƞorms published stories about IoT
Inspector [29, 58]. IoT Inspector’s website has a “waiƟng list” that interested users can sign up for
with their email addresses to be noƟﬁed of updates and new releases. Therefore, IoT
Inspector’s users could learn about the soŌware from any of the means above and come from anywhere in the world

EvaluaƟng Smart Home Device Users’ Responses to their (Un)Conﬁrmed Privacy ExpectaƟons 9

Fig. 2. A screenshot of the IoT Inspector. Users install the soŌware and access the user interface through their browser.
with various degrees of technical experƟse. Because parƟcipants had voluntarily joined the IoT Inspector waiƟng list
and installed the tool, they may have been more interested in IoT privacy and security or more technically moƟvated
than the general public. However, we did not measure their moƟvaƟons and therefore cannot infer that they had
higher privacy concerns. To learn more about IoT Inspector’s user base, please refer to Huang et al. [45, 47].
With approval from our InsƟtuƟonal Review Board (IRB) and the IoT Inspector research team’s IRB [44], we aimed to
recruit parƟcipants from individuals who signed up on IoT Inspector’s wai Ɵng list. The IoT Inspector team contacted
everyone on the wai Ɵng list, le ƫng them know that the IoT Inspector has become available for use. A Ōer learning
about the tool’s release and installing IoT Inspector, users saw an informed consent form asking them whether they
wanted to par Ɵcipate in our study. The users who rejected the consent could s Ɵll use the IoT Inspector without
answering survey ques Ɵons or dona Ɵng network data. The IoT Inspector operated locally for these users without
sending us any data.

Fig. 3. Users installed the IoT Inspector and saw the informed consent. Those who did not consent could sƟll use the tool without
answering surveys or sharing data. Those who gave consent were immediately redirected to answer the pre-survey. Then, they could
interact with the tool and view the reports. AŌer ﬁve minutes, we prompted them to respond to the post-survey.
We only collected data from those who gave consent to answer survey quesƟons and donate data (N = 35 parƟcipants
ﬁnished the study). In the consent form, we communicated that data donaƟon includes sharing the IoT Inspector’s
report, including informaƟon about their smart devices, the frequency at which these devices send out data, and the
domains with which the devices communicate.
We administered two surveys; users answered the ﬁrst survey before they saw the IoT Inspector’s report about
their smart home devices. Then, aŌer users browsed and navigated the IoT Inspector’s report for at least ﬁve minutes,
InteracƟng with
IoT Inspector
Informed Consent
 Answering
the Pre-Survey
Answering
the Post-Survey
Installing the
IoT Inspector

 10 Khatun et al.
we prompted them with a pop-up window and directed them to the second survey. If parƟcipants aƩempted to close
the app before compleƟng the post-survey, we prompted them with the same pop-up window and reminded them to
answer the post-survey before leaving the app. Therefore, parƟcipants who dismissed the iniƟal pop-up without
compleƟng the post-survey and later aƩempted to close the applicaƟon could see the pop-up a second Ɵme. Because
the study’s analyses required paired pre- and post-survey responses, parƟcipants who completed only the pre-survey
could not be included in the path model. The prompt, therefore, served as a reminder intended to reduce post-survey
dropout in this autonomous ﬁeld deployment; parƟcipants could sƟll exit without compleƟng the survey. Please see
Figure 3 for a summary of our experimental protocol.
Our survey drew upon several constructs from the exisƟng literature. We tried to keep the survey as short as possible
since our study did not include monetary compensa Ɵon, and longer ques Ɵonnaires can lower response rates [ 84].
Retaining par Ɵcipants was especially important because our par Ɵcipant pool was limited to individuals who had
voluntarily signed up to use IoT Inspector, and we could not supplement a low response rate with a new par Ɵcipant
pool. Therefore, we selected one item from each construct of interest. We recognize that single-item measures do not
allow for the assessment of internal reliability or discriminant validity and provide less robust opera ƟonalizaƟons of
rich psychological constructs, such as trust co nﬁrmaƟon and sa ƟsfacƟon, than mul Ɵ-item scales. As a pragma Ɵc
approach to minimizing par Ɵcipant burden in this uncompensated ﬁeld deployment, we selected either the highest -
loading item from the original validated instrument or, based on discussion among the authors, the item that most
directly captured the construct’s conceptual deﬁni Ɵon. Responses were recorded using a 7 -point Likert scale ranging
from “Strongly Disagree” to “Strongly Agree.” Below, we present the pre- and post-interacƟon measures.
Pre Survey Instruments:
• Trust-based expecta Ɵon: We measured users’ expecta Ɵons of smart devices following trustworthy data
pracƟces. We used the benevolence dimension of trust, which is concerned with whether an enƟty acts in the
user’s best interests or not [93]. We borrowed this item from previous work [93] and tailored it into the context
of smart home privacy: "My Smart Devices keep my best interests when handling my personal data." Because
the trust items explicitly asked parƟcipants about how their smart-home devices handle personal data, trust in
this study should be understood as users’ expecta Ɵons that the device and its associated manufacturer and
service ecosystem will collect, process, and share data in ways aligned with users’ interests. It should not be
interpreted as general trust in the device’s funcƟonality or narrowly as trust in its technical security.
• Privacy concerns: We included a single-item measure of global privacy concern as a baseline control variable,
using an item from the Internet Users’ InformaƟon Privacy Concerns (IUIPC) scale [70]: “All things considered,
the Internet would cause serious privacy problems.” We included this instrument to capture par Ɵcipants’
general privacy concern as a person-level privacy orientaƟon. Including this measure as a control is consistent
with prior privacy research that uses general privacy concern as an individual-diﬀerence control when
examining more context-speciﬁc privacy aƫtudes and behaviors [15]. Our goal was to control for parƟcipants’
general privacy orienta Ɵon so that the associa Ɵons among trust -based expecta Ɵons, trust conﬁrma Ɵon,
saƟsfacƟon, con Ɵnued-use inten Ɵon, and blocking behavior could be interpreted above and beyond this
broader tendency.
Post Survey Instruments:
• Trust conﬁrmaƟon: We followed the literature’s approach in measuring conﬁrma Ɵon [11] and asked users if
their trust expecta Ɵons of their smart devices were conﬁrmed: "Overall, most of my expecta Ɵons regarding
how my Smart Devices handle my personal data were conﬁrmed." Trust- conﬁrmaƟon items were coded such
that higher scores indic ate stronger perceived conﬁrma Ɵon of par Ɵcipants’ prior trust -based expecta Ɵons,
whereas lower scores indicate weaker conﬁrmaƟon.
• SaƟsfacƟon: The economic theory of uƟlity posits that individuals aƩempt to achieve saƟsfacƟon or maximum
uƟlity through their choices, given their resource limita Ɵons. Xu et al. [ 95] deﬁne perceived value as a
comprehensive assessment of the choice object in the decision-making process. In our context, the “choice
object” is the use of the smart- home device in light of the data prac Ɵces made visible to the par Ɵcipant. The

EvaluaƟng Smart Home Device Users’ Responses to their (Un)Conﬁrmed Privacy ExpectaƟons 11
“comprehensive assessment” refers to users’ overall judgment of whether the beneﬁts of using the device are
suﬃcient relaƟve to the privacy risks associated with those data prac Ɵces; it does not imply an exhaus Ɵve
evaluaƟon of every device feature or possible use. The item was adapted from Xu et al.’s [95] Perceived Value
of InformaƟon Disclosure scale: “I think my beneﬁts gained from the use of my Smart Devices can oﬀset the
risks of my informa Ɵon disclosure.” Accordingly, this opera ƟonalizaƟon does not capture broad aﬀec Ɵve
saƟsfacƟon with the device, as measured in some canonical ECT formula Ɵons [ 11]. Instead, it captures
saƟsfacƟon in a privacy-focused context: users’ evaluaƟve judgment of whether the beneﬁts of device use are
suﬃcient relaƟve to the privacy risks of disclosure.
• ConƟnuous Inten Ɵon: We followed the literature’s approach, measuring con Ɵnuous inten Ɵon to use a
technology [11] and tailored it to the context of smart home devices: "I intend to con Ɵnue using my Smart
Devices rather than disconƟnue their use."
4.1.3 ParƟcipant Recruitment. Overall, 152 users agreed to par Ɵcipate in the study and completed the pre -survey
quesƟonnaire. However, only 35 individuals also completed the post -survey quesƟonnaire.1 Therefore, our analyses
include the 35 parƟcipants who completed both surveys. ParƟcipaƟon rates are oŌen lower in ﬁeld studies with limited
incenƟves (e.g., 11% in a ﬁeld study with a $2 incenƟve [87]). This low compleƟon rate should be interpreted in light of
Study 1’s uncompensated ﬁeld- deployment design. Par Ɵcipants installed and used IoT Inspector on their own and
completed the post- survey only a Ōer interacƟng with the tool. Although the avai lable pre-survey measures did not
indicate diﬀerences between completers and non-completers, the groups may sƟll have diﬀered in unmeasured ways,
which may limit the generalizability of Study 1. We also did not collect demographic informa Ɵon for Study 1 and
therefore cannot characterize the sample demographically. Study 2 parƟally addresses this limitaƟon by collecƟng and
reporƟng parƟcipants’ demographic characterisƟcs.
4.1.4 Post-hoc Power Analysis: We conducted a post-hoc power analysis for the individual equaƟons predicƟng the two
dependent variables. At an alpha level of 0.05 and with a sample of 35 par Ɵcipants, the esƟmated power was 0.85 for
predicƟng intenƟon to conƟnue use and 0.97 for predic Ɵng willingness to block a device communica Ɵon [88]. These
esƟmates pertain to the individual equaƟons predicƟng the two dependent variables and should not be interpreted as
evidence that the full path model in Study 1 was adequately powered.
4.1.5 Data Analysis. We conducted a path model with our hypothesized eﬀects [66]. Path models can inform us about
the mechanisms and pathways through which an eﬀect occurs. AddiƟonally, they help us explore potenƟal mediaƟons
and whether and how the rela Ɵonship between two variables (e.g., conﬁrma Ɵon and intenƟon to use) is c hanneled
through a third variable (e.g., saƟsfacƟon). In the case of mediaƟon, we report indirect eﬀects that show the strength
of the indirect associa Ɵon. Furthermore, we conducted a saturated model to study if there are other signiﬁcant
nonhypothesized eﬀects. Since we did not ﬁnd any addi Ɵonal signiﬁcant eﬀects, we do not report the results of the
saturated model. We did not explore any two-way interacƟon eﬀects, as we did not have enough staƟsƟcal power for
more complicated analyses. Given the small sample size and the use of single-item measures in Study 1, we interpret
the path model as exploratory evidence of associa Ɵons among the measured variables rather than as a conﬁrmatory
test of latent constructs. Study 2, with its larger sampl e and mul Ɵ-item measures, provides a stronger sta ƟsƟcal and
measurement test.
4.2 Results
ParƟcipants’ iniƟal trust-based expectaƟons of their smart home devices varied, such that six users strongly disagreed
that their devices kept their best interests in mind when handling their personal data, indica Ɵng low trust -based

1 We compared the 35 parƟcipants who completed both surveys with the 117 par Ɵcipants who completed only the pre-survey on the variables
measured at pre-survey. We found no signiﬁcant diﬀerences between the groups on these measured variables; however, this analysis cannot rule out
diﬀerences in unmeasured characterisƟcs.

 12 Khatun et al.
expectaƟons regarding how the smart -device ecosystem would handle their data. Seven users disagreed with the
statement, two users somewhat disagreed, nine users neither agreed nor disagreed, one user somewhat agreed, nine
agreed, and one strongly agreed. AŌer viewing the IoT Inspector report, parƟcipants reported their trust conﬁrmaƟon
, with two users disagreeing about the presence of an alignment between their iniƟal expectaƟons and what they found
in IoT Inspector’s report about the actual data prac Ɵces of their sm art devices; one user somewhat disagreed, four
users were neutral, ﬁve users somewhat agreed, twenty users agreed, and three users strongly agreed. Par Ɵcipants’
privacy concern, measured on a scale from 1 to 7, had a mean of 5.61 (𝑆𝐷 = 1.34), suggesƟng relaƟvely high concern in
our sample. However, the privacy-concern measure was not signiﬁcantly associated with any other variable in our
model. Therefore, we removed it from the analyses (please see the discussion secƟon for a more elaborate discussion
about privacy concerns).
4.2.1 Hypotheses TesƟng. We conducted a path model with all our hypotheses (see Figure 4). The results
of the path model of study 1 are presented in Table 1, where staƟsƟcally signiﬁcant hypotheses are presented
in bold. This model shows an acceptable ﬁt (𝜒2(10) = 95.435, 𝑝 < .001, CFI = 0.996, TLI = 0.988, SRMR = 0.038,
RMSEA = 0.054, p = .386, CI : [0.000, 0.295]) [ 34]. The results suggest that users who trusted their smart
devices more, were also more likely to report a higher conﬁrmaƟon of their trusƟng beliefs, such that by one
standard deviaƟon increase in users’ ini Ɵal trust at t1, their reported trust conﬁrma Ɵon increased by 0.885
standard deviaƟons (𝑝 < .001, H1 conﬁrmed). AddiƟonally, we found that the more users’ trust is conﬁrmed,
the more they feel saƟsﬁed with their smart devices. By one standard deviaƟon increase in conﬁrming having
truthful devices, the saƟsfacƟon increases by 0.409 standard deviaƟons (𝑝 = 0.002, H2 conﬁrmed). However,
the results suggest that trust conﬁrmaƟon does not lead to signiﬁcant changes in users’ willingness to block
their devices’ communicaƟons (𝐵 = −0.024, 𝑝 = .466, H3 rejected) or intenƟons to conƟnue using smart home
devices in the future ( 𝐵 = 0.226, 𝑝 = .067, H4 rejected). Finally, those who reported higher saƟsfacƟon with
their smart devices were less likely to want to block certain communicaƟons from their smart home devices
(𝐵 = −1.263, 𝑝 < .001, H5 conﬁrmed) and more likely to want to conƟnue using their devices in the future (𝐵
= 0.395, 𝑝 < .008, H6 conﬁrmed).
Table 1. The results of the path model of study 1. Signiﬁcant hypotheses are presented in bold format.
Variable Names Standardized coefficients Standard error p-value
DV: Trust Confirmation (t2)
H1: Trust Expectations (t1) 0.885 0.078 <0.001
DV: Satisfaction (t2)
H2: Trust Confirmation (t2) 0.409 0.140 0.002
DV: Intentions to Continue Using Smart Home Devices (t2)
H4: Trust Confirmation (t2) 0.226 0.151 0.067
H6: Satisfaction (t2) 0.395 0.163 0.008
DV: Wanting to Block (t2)
H3: Trust Confirmation (t2) -0.024 0.275 0.466
H5: Satisfaction (t2) -1.263 0.298 <0.001

EvaluaƟng Smart Home Device Users’ Responses to their (Un)Conﬁrmed Privacy ExpectaƟons 13
4.2.2 MediaƟon Analysis. Figure 4 suggests the possibility of a full media Ɵon, where trust conﬁrmaƟon
predicts willingness to block and inten Ɵon to use variables, but its eﬀect is fully mediated through
saƟsfacƟon, leading to trust conﬁrma Ɵon having non-signiﬁcant direct eﬀects. Therefore, we conducted a
mediaƟon analysis and studied the indirect eﬀects of trust conﬁrma Ɵon on these dependent variables. We
found that the eﬀect of trust conﬁrma Ɵon on wan Ɵng to block device communica Ɵons is fully mediated
through saƟsfacƟon (indirect eﬀect: -0.521, 𝑝 = .007), such that if we remove sa ƟsfacƟon from the model,
the eﬀect of trust conﬁrmaƟon on wanƟng to block would be signiﬁcant (𝐵 = −0.387, 𝑝 < .004). Likewise, the
eﬀect of trust conﬁrmaƟon on intenƟon to conƟnue using smart home devices in the future is fully mediated
through saƟsfacƟon (indirect eﬀect: 0.206, 𝑝 = .014), such that if we remove sa ƟsfacƟon from the model,
trust conﬁrmaƟon signiﬁcantly predicts inten Ɵon to con Ɵnue using smart home devices in the future ( 𝐵 =
0.541, 𝑝 = .037). Because sa ƟsfacƟon is opera Ɵonalized here in the context of privacy, the indirect eﬀects
operate through par Ɵcipants’ evalua Ɵon of the beneﬁts and privacy risks of device use. Greater trust
conﬁrmaƟon was associated with greater saƟsfacƟon, which in turn was associated with stronger conƟnued-
use intenƟon and lower willingness to block.
4.3 Discussion
In our ﬁrst study, we invesƟgated the impact of revealing actual data prac Ɵces to users in their own homes using the
IoT Inspector. The report provided informa Ɵon against which par Ɵcipants could evaluate their pre-exis Ɵng trust
expectaƟons. We found that users who had higher trust at the beginning were more likely to have that trust conﬁrmed
aŌer viewing the report. This pa Ʃern may reﬂect greater prior familiarity among people who voluntarily signed up to
use a monitoring tool, which could have made their trust expectaƟons more likely to align with the pracƟces shown in
the report. However,
we did not directly measure par Ɵcipants’ prior familiarity or technical knowledge about their devices. This
interpretaƟon is therefore tentaƟve and based on the recruitment context rather than directly measured characterisƟcs
of the sample.
A key ﬁnding speciﬁc to this in-situ context is the mediaƟng role of saƟsfacƟon. In this sample, the decision to engage
in coping behaviors (both passive discon Ɵnuance of use and ac Ɵve blocking) was channeled en Ɵrely through their
saƟsfacƟon with data prac Ɵces. Speciﬁcally, when individuals found a viola Ɵon of their expecta Ɵons, they felt less
saƟsﬁed, which in turn lowered their intenƟon to conƟnue using the device. This saƟsfacƟon gatekeeping likely reﬂects
the real-world stakes of the study: blocking data or discarding a device in a live home environment has tangible
funcƟonal costs, and users weigh these costs against the beneﬁts before acƟng. It is also noteworthy that privacy

 14 Khatun et al.
Fig. 4. SaƟsfacƟon mediates the eﬀects of trust conﬁrmaƟon on the number of device communicaƟons users want to block (indirect
eﬀect: -0.521, 𝑝 = .007) and intenƟon to conƟnue using smart home devices (indirect eﬀect: 0.206, 𝑝 = .014).
concern was not a signiﬁcant predictor in this study. One possible explana Ɵon is a ceiling eﬀect, given the rela Ɵvely
high mean privacy-concern score of 5.61 on a 7-point scale. However, par Ɵcipants’ scores sƟll showed variaƟon, and
we did not formally test for a ceiling eﬀect, so this explana Ɵon remains tentaƟve. Other possible contribu Ɵng factors
include the small sample size, the use of a single global privacy-concern item, and the characterisƟcs of the self-selected
sample.
While providing ecologically grounded evidence, Study 1 faces limitaƟons regarding generalizability. Our parƟcipants
were self-selected smart-home users who voluntarily installed IoT Inspector and may have been more interested in
privacy or more technically mo Ɵvated than the broader popula Ɵon of smart-home users. Furthermore, the small
sample size (𝑁 = 35) and use of single-item measures limit the strength of the inferences that can be drawn from the
path model. In addiƟon, because we did not retain parƟcipant-linked report contents, our results should be interpreted
as reﬂecƟng responses to exposure to a real IoT Inspector report in general, rather than as evidence that any parƟcular
report feature (e.g., traﬃc volume, speciﬁc domains) drove parƟcipants’ post-survey responses. We therefore interpret
Study 1 as exploratory and conducted Study 2 with a larger online sample, mul Ɵ-item measures, and a controlled
experimental design to examine whether similar pa Ʃerns emerged under stronger sta ƟsƟcal and measurement
condiƟons.
5 Study 2: The Online Experiment
5.1 Methods
We conducted a survey-based experiment to examine the privacy expecta Ɵons and behavioral inten Ɵons of smart
home owners. The study followed a between-subjects design and was approved by our InsƟtuƟonal Review Board (IRB).
The study consisted of a two-phase Qualtrics survey, as summarized in Figure 5. First, parƟcipants idenƟﬁed their
most frequently used smart device (smart speaker, smart TV, or smart camera) and speciﬁed its brand (e.g., LG,
Samsung). They then answered ques Ɵons regarding their baseline trust, privacy concerns, and usage habits.
Subsequently, parƟcipants viewed a network ac Ɵvity report that was framed as a real- Ɵme analysis of their speciﬁc
device’s traﬃc. In reality, this was a simulated report dynamically customized to match the user’s input from the ﬁrst
survey. To increase the perceived realism and personal relevance of the simulated report, we showed par Ɵcipants an
animated progress bar

Fig. 5. ParƟcipants completed a pre-survey, viewed either a high or low adverƟsing-related network acƟvity report for a device they
owned, and then completed a post-survey.
with the message “Analyzing your network data” before showing them this simulated report. Adding this step implied
that there is a back-end system processing their device informaƟon and that the report is based on real data.
To provide a contextual baseline for comparison, the report displayed traﬃc volume between the device and its
manufacturer (e.g., “LG Server” or “Samsung Server”), represenƟng funcƟonality-related communicaƟon, alongside
communicaƟon with adverƟsing-related domains. The reports were based on a deliberately simpliﬁed model in which
Informed Consent
 Answering
the Pre-Survey
Users Seeing
the Report
Answering
the Post-Survey

EvaluaƟng Smart Home Device Users’ Responses to their (Un)Conﬁrmed Privacy ExpectaƟons 15
a smart-home device communicates with manufacturer or funcƟonality-related servers and may also communicate
with adverƟsing or tracking domains. This structure is grounded in prior work documenƟng that some smart devices,
parƟcularly smart TVs and smart speakers, communicate with both manufacturer servers and adverƟsing or tracking
domains [45, 49]. The manufacturer traﬃc was held constant across condiƟons and served as a ﬁxed reference point,
while only the volume of adverƟsing-related communicaƟon varied. As shown in Figure 6, both reports displayed the
same manufacturer traﬃc (842 KB uploaded and approximately 390 KB downloaded). AdverƟsing-related traﬃc was
90 KB uploaded and 110 KB downloaded in the LowAd condiƟon, compared with 1.2 MB uploaded and 900 KB
downloaded in the HighAd condiƟon. These volumes were selected to create a controlled experimental contrast and
were not calibrated to represent the actual or typical traﬃc of any parƟcular device or device category.
Upon reviewing the report, par Ɵcipants proceeded to the post -survey to evaluate their experience. First, they
assessed whether the reported data prac Ɵces aligned with their ini Ɵal expecta Ɵons. We then measured post -
manipulaƟon constructs, including tr ust in the device, technology self- eﬃcacy, and sa ƟsfacƟon (measured as the
perceived trade-oﬀ between beneﬁts and privacy risks). The survey also assessed their intenƟon to conƟnue using the
device and their general online privacy concerns. Finally , parƟcipants responded to open -ended quesƟons regarding
their reacƟons to the report and provided demographic informaƟon (e.g., age, educaƟon, and income).
5.1.1 Ethical ConsideraƟons and Use of DecepƟon. Study 2 used temporary decepƟon. ParƟcipants were told that
the network report reﬂected a real-Ɵme analysis of their own device; in reality, the report was simulated, customized
to their stated device, and randomly assigned to the HighAd or LowAd condiƟon. This design allowed us to control the
depicted level of adverƟsing-related communicaƟon while increasing the perceived realism and personal relevance of
the report by presenƟng it as reﬂecƟng traﬃc from parƟcipants’ own devices. The study was reviewed and approved
by our InsƟtuƟonal Review Board and was determined to involve minimal risk. Immediately aŌer compleƟng the
study, they were informed that the report was simulated and given the opƟon to withdraw their data without
aﬀecƟng their compensaƟon. No parƟcipant chose to withdraw.
5.1.2 Measures. All mulƟ-item constructs were measured using 7-point Likert scales (1 = Strongly Disagree, 7 = Strongly
Agree). With the excepƟon of trust expectaƟon and trust conﬁrmaƟon2, all constructs were measured both before and
aŌer the manipulaƟon to examine possible shiŌs in parƟcipants’ aƫtudes following exposure to the data report.
• Trust-based expectaƟon (pre-survey only): We measured users’ expectaƟons of their smart devices prior to the
manipulaƟon using the benevolence dimension of trust, which reﬂects whether a technology acts in the users’
best interests [ 93]. Consistent with Study 1, we adapted this construct to the smart-home privacy context.
ParƟcipants rated statements such as: “My Smart Device keeps my best interests in mind when handling my
personal data.”
• Trust ConﬁrmaƟon (post-survey only): A Ōer viewing the report, par Ɵcipants rated the extent to which the
device’s data pracƟces aligned with their expecta Ɵons. In this case, we followed the literature of measuring
conﬁrmaƟon [11]. "The way my smart devices handled my personal data was beƩer than what I expected."
• SaƟsfacƟon [95], IntenƟon to ConƟnue Use [11], Technology Self-Eﬃcacy [90], and CollecƟon Concern [70] (Pre
and Post): These constructs were measured directly before and a Ōer the manipula Ɵon to assess whether
exposure to the data report shi Ōed parƟcipants’ evaluaƟons. The extended versions (mul Ɵ-item) of the same
scales used in Study 1 were employed here, with wording adapted to the speciﬁc device selected by each
parƟcipant.

2 By deﬁniƟon, trust expectaƟon represents beliefs held prior to an event and was therefore measured only in the pre -survey, whereas trust
conﬁrmaƟon evaluates the outcome of that event and was uniquely measured in the post -survey

 16 Khatun et al.
• Awareness (Pre and Post): To assess aƩenƟveness to data handling pracƟces, we included the IUIPC awareness
subscale [70] (e.g., the importance of being informed about how personal data is used).
• Unauthorized Use (Pre and Post): We addiƟonally included the IUIPC unauthorized use subscale [70] to assess
concerns regarding secondary use of personal data without user consent.
5.1.3 QualitaƟve Data: We collected open-ended responses to beƩer understand parƟcipants’ expectaƟons and
their interpretaƟons of the network-traﬃc report. ParƟcipants were asked whether the data pracƟces of their device
aligned with their expectaƟons, and were instructed not to provide any idenƟfying informaƟon in this quesƟon.

Fig. 6. Simulated network activity reports comparing the HighAd (left) and LowAd (right) conditions. Advertisement
traffic volume is displayed relative to the manufacturer baseline (e.g., LG or Samsung servers), with a radio button
as a choice option for blocking communications.
5.1.4 ParƟcipant Recruitment. 132 par Ɵcipants were recruited through Proliﬁc. Proliﬁc is an online pla ƞorm for
recruiƟng research parƟcipants. The website is publicly accessible on the internet. For this experiment, parƟcipants had
to be 18 years or older, U.S.-based adults, and must use at least one smart home device (smart speaker, smart TV, or
smart camera). They received monetary compensa Ɵon ($4 for the study’s dura Ɵon of approximately 10 minutes) in
accordance
with Proliﬁc’s guidelines. Only respondents who gave explicit, electronic consent could parƟcipate in the study.
5.1.5 Demographic Informa Ɵon of ParƟcipants. Our parƟcipants were, on average, 49 years old. Gender distribu Ɵon
was balanced, with comparable numbers of male (N = 65) and female (N = 63) par Ɵcipants. Two of the par Ɵcipants
reported Non-Binary gender, and two preferred not to disclose their gender idenƟty. The majority of par Ɵcipants
idenƟﬁed as
White (N = 100), with smaller propor Ɵons idenƟfying as Black or African-American (N = 18). Six par Ɵcipants idenƟﬁed
as American Indian or Alaska NaƟve, two as NaƟve Hawaiian/Other Paciﬁc Islander, and six selected “Some other race”.
Among the parƟcipants, the educaƟon level ranged from high school incomplete or less (N = 1) to a master’s/doctorate
or other professional degree (medical/law) (N = 31). The most commonly reported level was a four-year college or
bachelor’s degree (N = 48), followed by some college or an associate’s degree (N = 31) and high school graduate/GED
Table 2. Demographic InformaƟon of ParƟcipants for Study 2 (𝑁 = 132)
Variable Category N (%) / M (SD)
Age (years)  49.48
(16.70)
Gender Male
Female
65
(49.24%)

EvaluaƟng Smart Home Device Users’ Responses to their (Un)Conﬁrmed Privacy ExpectaƟons 17
63
(47.73%)
 Non-Binary 2
(1.52%)
 Prefer not to say 2
(1.52%)
Race/ethnicity
White
Black or African-American
American Indian or Alaska NaƟve
100
(75.76%)
18 (13.64%)
6 (4.55%)
 NaƟve Hawaiian/Other Paciﬁc Islanders 2
(1.52%)
 Some other race 6
(4.55%)
EducaƟon
High school incomplete or less
High school graduate or GED (includes technical/vocaƟonal training)
Some college or associate’s degree
Four year college degree or bachelor’s degree
1 (0.76%)
19
(14.39%)
31
(23.48%)
48
(36.36%)
 Some postgraduate or professional schooling (no postgraduate degree) 2
(1.52%)
 Master’s, doctorate, postgraduate or professional degree (medical/law) 31
(23.48%)
Income
Less than $10,000
$10,000 to less than $20,000
$20,000 to less than $30,000
$30,000 to less than $40,000
$40,000 to less than $50,000
3
(2.27%)
9
(6.82%)
8
(6.06%)
11
(8.33%)
8
(6.06%)
 $50,000 to less than $75,000 30
(22.73%)
 $75,000 to less than $100,000 23
(17.42%)
 $100,000 to less than $150,000 25
(18.94%)
 $150,000 or more 15
(11.36%)
(N = 19). Some postgraduate/professional schooling without a postgraduate degree was the least common (N = 2).
ParƟcipants’ annual household income ranged from less than $10,000 (N = 3) to $150,000 or more (N = 15). The most
commonly reported income range was $50,000 to less than $75,000 (N = 30), followed by $100,000 to less than
$150,000 (N = 25) and $75,000 to less than $100,000 (N = 23). The remaining parƟcipants fell into the following income
ranges: $10,000 to less than $20,000 (N = 9), $20,000 to less than $30,000 (N = 8), $30,000 to less than $40,000 (N =
11), and $40,000 to less than $50,000 (N = 8). Table 2 reports the full demographic informaƟon.
5.1.6 Data Analysis: For the quanƟtaƟve analysis, we used conﬁrmatory factor analysis (CFA) and structural equa Ɵon
modeling (SEM) to assess pre- and post-survey constructs and to test the hypothesized relaƟonships in our model. All
quanƟtaƟve analyses were conducted in R using packages that are designed for latent variable modeling and regression.

 18 Khatun et al.
For the qualitaƟve analysis, we employed a themaƟc analysis approach to examine parƟcipants’ responses to our
open-ended quesƟon, in which we asked whether the data pracƟces of their device aligned with their expectaƟons.
Following established guidelines for themaƟc analysis [13], we iteraƟvely coded, compared, and reﬁned themes
across the responses to develop a clear understanding of parƟcipants’ perspecƟves.
5.2 Results
5.2.1 CFA Report. A conﬁrmatory factor analysis (CFA) was conducted on both pre- and post-survey data to evaluate the
construct validity of the latent variables. The pre-survey model shows an acceptable to good ﬁt across several indices:
𝜒2(209) = 318.9, 𝑝𝑠 < . 001, CFI = 0.956, TLI = 0.947; SRMR = 0.053; and RMSEA = 0.064 [ 34]. The post-survey
measurement model also showed reasonable ﬁt: 𝜒2(231) = 416.7, 𝑝𝑠 < .001; CFI = 0.937; TLI = 0.925; SRMR = 0.052;
and RMSEA = 0.079 [ 34]. Collec Ɵvely, these results demonstrate that both CFA models provide support for the
measurement structure and jusƟfy proceeding to structural modeling analyses. Table 3 represents the survey measures
and factor loadings for both surveys. One Trust ConﬁrmaƟon item, highlighted in gray in Table 3, was iniƟally included
but had a standardized loading of .543, substan Ɵally lower than the loadings of the other Trust Conﬁrma Ɵon items.
Because its standardized loading was considerably lower than those of the other Trust Conﬁrma Ɵon items and its
removal improved the measurement model, the item was removed from the ﬁnal model. The removed item is the same
item used as the single-item measure in Study 1. Because it was not retained in the ﬁnal Study 2 mul Ɵ-item scale, we
acknowledge limited cross- study measurement comparability and avoid trea Ɵng the two studies as using fully
equivalent measures of trust conﬁrma Ɵon. Study 1 is therefore interpreted as using a single -item proxy for trust
conﬁrmaƟon, whereas Study 2 provides a stronger mulƟ-item measurement test.
Table 4 presents the correlaƟon matrix for the study’s principal constructs. The main diagonal values represent the
square root of the Average Variance Extracted (AVE) for each construct. In all but one instance, these values exceed the
corresponding oﬀ-diagonal inter- construct correla Ɵons, suppor Ɵng discriminant validity and indica Ɵng that the
constructs are disƟnct. The excep Ɵon is the strong correla Ɵon between Awareness and Unauthorized Use (r=0.844).
This high degree of associa Ɵon suggests substan Ɵal conceptual redundancy between these two sub-scales.
Consequently, we retained Awareness due to its direct relevance to the transparency focus of our study design, while
excluding Unauthorized Use from the subsequent analysis.
Table 3. Pre and Post Survey Measurement Items and Factor Loadings
SubjecƟve Construct Items Pre Load Post Load
Self Eﬃcacy
Pre AVE: 0.804
Post AVE: 0.793
I would feel comfortable using my smart home devices on my own.
If I want to, I can use my smart home devices on my own easily.
I would be able to use my smart home devices even if there is no one around to show
me how to use it.
0.843
0.990
0.848
0.841
0.949
0.877
CollecƟon Concern
Pre AVE: 0.761
Post AVE: 0.782
It usually bothers me when online companies ask me personal informa Ɵon. When
online companies ask me for personal informaƟon, I someƟmes think twice before
providing it.
0.850
0.813
0.836
0.854
 It bothers me to give personal informaƟon to so many online companies. 0.917 0.908
 I’m concerned that online companies are collecƟng too much personal informaƟon
about me.
0.905 0.936
SaƟsfacƟon
Pre AVE: 0.754
Post AVE: 0.820
I think my beneﬁts gained from the use of my smart home devices can oﬀset the risks
of my informaƟon disclosure.
The value I gain from use of my smart home devices is worth the informa Ɵon I give
away.
0.762
0.937
0.823
0.917
 I think the beneﬁts gained from using my smart home devices will be more than the
risks of my informaƟon disclosures.
0.897 0.970
IntenƟons to ConƟnue Use
Pre AVE: 0.757
Post AVE: 0.805
I intend to conƟnue using my smart home devices rather than discon Ɵnue their use.
My intenƟons are to conƟnue using my smart home devices than use any alterna Ɵve
means.
0.858
0.788
0.926
0.867
 If I could, I would like to conƟnue my use of smart home devices. 0.956 0.898

EvaluaƟng Smart Home Device Users’ Responses to their (Un)Conﬁrmed Privacy ExpectaƟons 19
Awareness
Pre AVE: 0.559
Post AVE: 0.583
Companies seeking informaƟon online should disclose the way the data are collected,
processed, and used.
A good consumer online privacy policy should have a clear and conspicuous
disclosure.
0.743
0.778
0.866
0.792
 It is very important to me that I am aware and knowledgeable about how my personal
informaƟon will be used.
0.720 0.610
Unauthorized Use
Pre AVE: 0.693
Post AVE: 0.721
Online companies should not use personal informaƟon for any purpose unless it has
been authorized by the individuals who provided informa Ɵon.
When people give personal informaƟon to an online company for some reason, the
online company should never use the informaƟon for any other reason.
0.815
0.842
0.751
0.869
 Online companies should never sell the personal informa Ɵon in their computer
databases to other companies.
0.764 0.853
 Online companies should never share personal informaƟon with other companies
unless it has been authorized by the individuals who provided the informa Ɵon.
0.903 0.915
Trust-based ExpectaƟon AVE:
0.904
I expect my smart home devices to put my interest ﬁrst when handling my personal
data.
0.937
 I expect my smart home devices to keep my interests in mind when handling my
personal data.
0.954
 I expect my smart home devices to understand my needs and preferences when
handling my personal data.
0.962
Trust ConﬁrmaƟon AVE:
0.833
The way my smart home devices handled my personal data was beƩer than what I
expected.
 0.872
 Overall, most of the expectaƟons regarding how my smart home devices handled my
personal data were conﬁrmed.
 0.543
 My experience conﬁrmed that my smart home devices put my interest ﬁrst when
handling my personal data.
 0.927
 My experience conﬁrmed that my smart home devices keep my interests in its mind
when handling my personal data.
 0.955
 My experience conﬁrmed that my smart home devices want to understand my needs
and preferences when handling my personal data.
 0.894
Table 4. CorrelaƟon Matrix. Since Awareness and Unauthorized Use do not meet the discriminant validity criteria, we remove
Unauthorized Use from the analyses.
 Self-Eﬃcacy SaƟsfacƟon ExpectaƟons IntenƟon CollecƟon Awareness Unauthorized Use
Self-Eﬃcacy 0.896
SaƟsfacƟon 0.256 0.868
ExpectaƟons 0.139 0.268 0.951
IntenƟon 0.485 0.404 0.139 0.870
CollecƟon 0.097 -0.293 0.001 0.028 0.872
Awareness 0.566 0.061 0.289 0.389 0.381 0.747
Unauthorized Use 0.583 -0.071 0.217 0.408 0.342 0.844 0.832
5.2.2 Path Model. The path model ( Figure 7) illustrates how trust- based expectaƟons, conﬁrmaƟon, and sa ƟsfacƟon
shape users’ behavioral intenƟons. The results of Study 2 are presented in Table 5. This model shows an acceptable ﬁt
(𝜒2(216) = 269.16, 𝑝 = 0.008, CFI = 0.981, TLI = 0.977, SRMR = 0.051, RMSEA = 0.044, p = 0.733, CI: [0.023,
0.059]). The results show that pre-survey trust-based expectaƟons signiﬁcantly predict post-survey trust conﬁrmaƟon
(𝛽 = 0.469, 𝑝 < .001, H1 conﬁrmed), indicaƟng that users with higher trust-based expectaƟons about their smart devices
are more likely to report stronger conﬁrmaƟon of those expectaƟons. We also found that stronger trust conﬁrma Ɵon
is associated with greater saƟsfacƟon with the smart device, suggesƟng that users who feel their expectaƟons are met
tend

 20 Khatun et al.

Fig. 7. Study 2 path model illustraƟng the relaƟonships among key constructs. The model controls for collecƟon and awareness
concerns, and privacy self-eﬃcacy by regressing them on all dependent variables; signiﬁcant eﬀects of these control variables are
detailed in Table 5.
Table 5. The results of the path model of study 2. Signiﬁcant hypotheses are presented in bold format.
Variable Names Standardized coefficients Standard error p-value
DV: Trust Confirmation (t2)
H1: Trust Expectations (t1) 0.469 0.116 <0.001
Awareness (t1) -0.218 0.095 0.010
DV: Satisfaction (t2)
H2: Trust Confirmation (t2) 0.443 0.103 <0.001
Self-Efficacy (t1) 0.236 0.100 0.005
Collection Concerns (t1) -0.237 0.098 0.004
DV: Intentions to Continue Using Smart Home Devices (t2)
H4: Trust Confirmation (t2) -0.037 0.088 0.619
H6: Satisfaction (t2) 0.546 0.118 <0.001
Self-Efficacy (t1) 0.312 0.188 0.032
DV: Wanting to Block (t2)
H3: Trust Confirmation (t2) -0.226 0.106 0.059
H5: Satisfaction (t2) 0.140 0.109 0.319
Collection Concerns (t1) 0.409 0.100 <0.001
to report higher saƟsfacƟon (𝛽 = 0.443, 𝑝 < .001, H2 conﬁrmed). However, trust conﬁrmaƟon does not signiﬁcantly
predict wanƟng to block (𝛽 = −0.226, 𝑝 = 0.059, H3 rejected) or intenƟons to conƟnue use (𝛽 = −0.037, 𝑝 = 0.619, H4
rejected). Finally, saƟsfacƟon is not a signiﬁcant predictor of wanƟng to block (𝛽 = 0.140, 𝑝 = 0.319, H5 rejected). In
contrast, saƟsfacƟon signiﬁcantly predicts intenƟons to conƟnue use (𝛽 = 0.546, 𝑝 < .001, H6 conﬁrmed), such that
more saƟsﬁed users are more likely to intend to conƟnue using their devices. In addiƟon, we controlled for self-
eﬃcacy, awareness, and collecƟon concerns (measured at pre-survey) by regressing them on all of the other
variables. We found that awareness negaƟvely predicts trust conﬁrmaƟon (𝛽 = −0.218, 𝑝 = .010). Self-eﬃcacy
posiƟvely predicts saƟsfacƟon (𝛽 = 0.236, 𝑝 = .005) and intenƟons to conƟnue use (𝛽 = 0.312, 𝑝 = 0.032) while

EvaluaƟng Smart Home Device Users’ Responses to their (Un)Conﬁrmed Privacy ExpectaƟons 21
collecƟon concerns negaƟvely predict saƟsfacƟon (𝛽 = −0.237, 𝑝 = 0.004). Moreover, collecƟon concerns is the
strongest predictor of blocking decisions (𝛽 = 0.409, 𝑝 < .001). This indicates that users with greater collecƟon
concerns are substanƟally more likely to choose to block device communicaƟons.
Table 6. Regression results predic Ɵng post-survey outcomes from pre-survey measures and experimental condi Ɵon (HighAd vs.
LowAd). Each model includes the corresponding pre-measure, condiƟon, and their interacƟon term. We found signiﬁcant interacƟon
eﬀects only for Self-Eﬃcacy and IntenƟon to use.
DV IVs Standard coeﬀ Standard error 𝑝-value
Post Self-Eﬃcacy
Pre Self-Eﬃcacy
HighAd (vs. LowAd)
0.796
-0.059
0.049
0.098
< 0.001
0.549
 Pre Self-Eﬃcacy × HighAd 0.291 0.099 0.003
Post CollecƟon Concerns
Pre CollecƟon Concerns HighAd
(vs. LowAd)
0.894
-0.103
0.039
0.077
< 0.001
0.180
 Pre CollecƟon Concerns × HighAd 0.027 0.079 0.736
Post Awareness
Pre Awareness
HighAd (vs. LowAd)
0.921
0.023
0.042
0.079
< 0.001
0.762
 Pre Awareness × HighAd -0.077 0.086 0.373
Post Unauthorized Use
Pre Unauthorized Use HighAd
(vs. LowAd)
0.916
-0.032
0.038
0.073
< 0.001
0.655
 Pre Unauthorized Use × HighAd -0.082 0.076 0.281
Post SaƟsfacƟon
Pre SaƟsfacƟon
HighAd (vs. LowAd)
0.850
0.147
0.051
0.098
< 0.001
0.137
 Pre SaƟsfacƟon × HighAd -0.161 0.103 0.119
Post IntenƟon
Pre IntenƟon
HighAd (vs. LowAd)
0.801
0.147
0.051
0.100
< 0.001
0.145
 Pre IntenƟon × HighAd -0.212 0.103 0.042
5.2.3 Post-hoc Analyses with Experimental Manipula Ɵons. To invesƟgate whether the experimental manipula Ɵon
(HighAd vs. LowAd) changed user a ƫtudes, we conducted post-hoc linear regressions predic Ɵng each post-survey
construct using its corresponding pre-survey baseline, the experimental condiƟon, and their interacƟon term (Table 6).
Across all constructs, pre-survey measures strongly predicted their respec Ɵve post-survey outcomes. Signiﬁcant
interacƟons between pre-survey scores and the experimental condiƟon were observed only for Self-Eﬃcacy (𝑝 = .003)
and Inten Ɵon ( 𝑝 = .042), indica Ɵng that the experimental manipula Ɵon speciﬁcally moderated changes in these
variables

−4
−3
−2
−1
0
1
−3
 −2
 −1
 0
 1
Pre Survey Self−Efficacy
Condition
HighAd
LowAd
−4
−2
0
−4
 −2
 0
Pre Survey Intention
Condition
HighAd
LowAd

 22 Khatun et al.
 (a) Pre–Post Self-Eﬃcacy by condiƟon (b) Pre–Post IntenƟon by condiƟon
Fig. 8. Pre–post survey relaƟonships between self-eﬃcacy and intenƟon to conƟnue using across HighAd and LowAd condiƟons.
(visualized in Figure 8 ). In contrast, no signiﬁcant interac Ɵons were found for Collec Ɵon Concerns, Awareness, or
SaƟsfacƟon, suggesƟng the experimental manipulaƟon did not change these aƫtudes beyond baseline levels. 3
5.2.4 QualitaƟve Insights. To complement the quan ƟtaƟve results of the path model, we conducted a qualita Ɵve
themaƟc analysis on parƟcipants’ open-ended responses to the quesƟon: “Were the data pracƟces of your smart home
devices (Smart TV, Smart Speaker, and Smart Camera) consistent with your expectaƟons?” Of the 132 parƟcipants, 130
responded to this open-ended ques Ɵon; two parƟcipants leŌ the quesƟon blank. This resulted in 65 responses from
each experimental condiƟon. ParƟcipants answered this quesƟon aŌer viewing the simulated network-acƟvity report.
Their responses should therefore be interpreted as reac Ɵons to the data pracƟces depicted in the report, rather than
as assessments of their devices’ actual data prac Ɵces. Our analysis revealed three primary themes: Data Prac Ɵces
Consistent with ExpectaƟon, Distrust Toward Data PracƟces, and Others (Table 7). The Others category encompasses
responses that were neutral, unrelated to speciﬁc data prac Ɵces, or no-expecta Ɵon responses. Collec Ɵvely, these
themes capture par Ɵcipants’ interpretaƟons and reac Ɵons to the data prac Ɵces depicted in the simulated report.
Although the same themes appeared in both condi Ɵons, their descrip Ɵve distribu Ɵons diﬀered, par Ɵcularly for
expressions of inconsistency or distrust.
The proporƟon of par Ɵcipants who described the report as consistent with their expecta Ɵons was similar across
condiƟons (HighAd: 39 of 65, 60.0%; LowAd: 38 of 65, 58.5%). However, expressions of inconsistency or distrust were
descripƟvely more common in the HighAd condi Ɵon (12 of 65, 18.5%) than in the LowAd condi Ɵon (7 of 65, 10.8%).
For example, one par Ɵcipant in the HighAd condi Ɵon stated, “The data prac Ɵces were not consistent with my
expectaƟons. I was surprised by how much data was sent to adverƟsement-related domains compared to the actual TV
manufacturer.” In contrast, some parƟcipants in the LowAd condi Ɵon described the depicted volume of adver Ɵsing-
related communicaƟon as lower than they had expected and expressed reassurance. These ﬁndings indicate that an
overall judgment of consistency did not necessarily capture whether par Ɵcipants approved of, trusted, or felt
comfortable with the depicted pracƟces.
5.2.5 How Par Ɵcipants Make Judgments of Consistency. A majority of par Ɵcipants in both condi Ɵons described the
depicted data prac Ɵces as consistent with their expecta Ɵons. Within these responses, we also iden Ɵﬁed four
interpreƟve sub-themes that reﬂected how par Ɵcipants arrived at this judgment: Normaliza Ɵon or pragma Ɵc
acceptance, priorknowledge conﬁrmaƟon, favorable deviaƟon from expectaƟons, and parƟal surprise within an overall
judgment of consistency. Responses could reﬂect more than one sub-theme. Responses that were too brief to
determine how parƟcipants arrived at their judgment were not assigned an interpreƟve sub-theme.
Table 7. Frequencies of qualitaƟve themes by experimental condiƟon, with representaƟve examples. Responses could reﬂect more
than one subtheme; therefore, subtheme frequencies may exceed the corresponding parent-theme totals.

Theme HighAd LowAd RepresentaƟve Example
Data PracƟces Consistent with ExpectaƟon 39 38

3 The main study did not include an internal manipula Ɵon-check item assessing parƟcipants’ perceived level of adverƟsing-related acƟvity. We
therefore conducted a supplementary manipulaƟon-check study showing parƟcipants the HighAd/LowAd reports iden Ɵcal to the main study. AŌer
browsing the report, parƟcipants answered the quesƟon "Based on the report you just reviewed, how much data do you feel your Smart TV shared
with adverƟsingrelated companies?" (rated from "None at all" to "A very large amount"). Using a paired t-test, par Ɵcipants perceived signiﬁcantly more
adverƟsing-related acƟvity in the HighAd report than in the LowAd report (M = 3.97 vs. 2.67, t(29) = 7.48, p < .0001), sugges Ɵng that the sƟmuli
diﬀered percepƟbly in the intended direcƟon. Because this check was conducted in a separate sample, it does not establish how par Ɵcipants in the
main study perceived the manipulaƟon.

EvaluaƟng Smart Home Device Users’ Responses to their (Un)Conﬁrmed Privacy ExpectaƟons 23
NormalizaƟon or pragmaƟc acceptance 11 4 “yes, I think that all smart devices are using and abusing our data. We
are almost never given a choice but to accept their terms of service. I
also believe that my smart phone is listening to my conversaƟons.”
Prior-knowledge conﬁrmaƟon 23 18 “yes, The data pracƟces of my Smart TV matched my expectaƟons, as I
was aware it would collect viewing history, app usage, and voice
commands for recommenda Ɵons and ads, and I found the expected
privacy seƫngs during setup.”
Favorable deviaƟon from expectaƟons 4 16 “Yes, the levels of informaƟon/adverƟsement sharing were actually a
bit lower than my expectaƟons.”
Overall consistency with parƟal surprise 5 1 “The data prac Ɵces of my Smart Speaker were somewhat consistent
with my expecta Ɵons. I an Ɵcipated that voice recordings might be
stored and analyzed to improve performance, but I was surprised by
how much data could be collected passively, such as background noise
or frequent usage pa Ʃerns. I would prefer more transparency and
easier control over privacy seƫngs.”
Distrust Toward Data PracƟces 12 7
Volume exceeded expectaƟons 9 5 “No, because I have no idea why my Echo would be transferring so
much (or really any) data just in the last 10 minutes.”
ProtecƟon or consent violated 4 2 “No. I expected my smart TV to protect my data, if they were to use it
in other ways I expect to have been asked for permission.”
Others 14 20 “I didn’t really have any expectaƟons.”
NormalizaƟon or pragmaƟc acceptance. Some parƟcipants described the depicted pracƟces as expected because they
viewed data sharing as rouƟne or unavoidable in smart-device ecosystems (𝑛 = 15; HighAd: 𝑛 = 11, LowAd: 𝑛 = 4). For
these parƟcipants, consistency reﬂected resignaƟon to an expected pracƟce rather than approval or saƟsfacƟon. "yes,
I think that all smart devices are using and abusing our data. We are almost never given a choice but to accept
their terms of service. I also believe that my smart phone is listening to my conversaƟons."
Prior-knowledge conﬁrmaƟon. Other par Ɵcipants referred to speciﬁc prac Ɵces they already expected, such as the
collecƟon of viewing history, app usage, or voice -command data ( 𝑛 = 41; HighAd: 𝑛 = 23, LowAd: 𝑛 = 18). In these
responses, the report appeared to conﬁrm par Ɵcipants’ prior understanding of smart-device data pracƟces. "yes, The
data pracƟces of my Smart TV matched my expectaƟons, as I was aware it would collect viewing history, app usage, and
voice commands for recommendaƟons and ads, and I found the expected privacy seƫngs during setup."
Favorable deviaƟon from expectaƟons. Some parƟcipants, parƟcularly in the LowAd condiƟon, stated that the report
showed less adver Ɵsing-related communicaƟon than they had an Ɵcipated (𝑛 = 20; HighAd: 𝑛 = 4, LowAd: 𝑛 = 16).
Although these responses had ini Ɵally been categorized as broadly consistent with expecta Ɵons, their explana Ɵons
reﬂected relief that the depicted prac Ɵces were less extensive than expected. "Yes, the levels of
informaƟon/adverƟsement sharing were actually a bit lower than my expectaƟons."
Overall consistency with parƟal surprise. Some parƟcipants, more frequently in the HighAd condiƟon, characterized
the report as generally consistent with their expecta Ɵons while also iden Ɵfying parƟcular pracƟces that surprised or
concerned them, su ch as communica Ɵon with third -party adverƟsing domains ( 𝑛 = 6; HighAd: 𝑛 = 5, LowAd: 𝑛 = 1).
These responses show that an overall judgment of consistency could coexist with concern about speciﬁc
communicaƟons. "The data prac Ɵces of my Smart Speaker were somewhat consistent with my expecta Ɵons. I
anƟcipated that voice recordings might be st ored and analyzed to improve performance, but I was surprised by how
much data could be collected passively, such as background noise or frequent usage pa Ʃerns. I would prefer more
transparency and easier control over privacy seƫngs."
A smaller set of par Ɵcipants reported that the depicted prac Ɵces did not match their expecta Ɵons, expressing
discomfort, suspicion, or a sense that the device was doing more than they had assumed (HighAd: n = 12, 18.5%; LowAd:
n = 7, 10.8%). These expre ssions were descrip Ɵvely more common in the HighAd condi Ɵon, consistent with the
manipulaƟon. ParƟcipants developed distrust for two main reasons: concern about the amount of data leaving the
device, and concern about a perceived breach of protecƟon or consent norms.

 24 Khatun et al.
Volume exceeded expecta Ɵons. Some par Ɵcipants located their distrust in the sheer amount of communica Ɵon
depicted, rather than any speciﬁc recipient or purpose (n = 14; HighAd: n = 9, LowAd: n = 5), o Ōen expressing surprise
that the device was communica Ɵng at all in a short windo w. "No, because I have no idea why my Echo would be
transferring so much (or really any) data just in the last 10 minutes." This mirrors the quanƟtaƟve ﬁnding that collecƟon
concerns, rather than saƟsfacƟon, predicted willingness to block in Study 2.
ProtecƟon or consent violated. Some parƟcipants distrusted the device because they believed it should protect
their data or ask permission before using it in other ways (n = 6; HighAd: n = 4, LowAd: n = 2). Their concern was
about whether the device followed appropriate privacy norms, not simply how much data it shared. This concern
appeared even when the amount of reported traﬃc was relaƟvely low. As one parƟcipant explained, “No. I expected
my smart TV to protect my data. If they were to use it in other ways, I expected to be asked for permission.”
Although the same themes appeared in both condi Ɵons, parƟcipants reached their judgments of consistency for
diﬀerent reasons. HighAd par Ɵcipants more o Ōen described the prac Ɵces as normal or unavoidable and were more
likely to express surprise or con cern about speciﬁc prac Ɵces, whereas LowAd par Ɵcipants more o Ōen expressed
reassurance that the report showed less data sharing than they had expected. These ﬁndings show that consistency
with expectaƟons did not uniformly indicate trust, approval, or sa ƟsfacƟon. The same overall judgment could reﬂect
informed prior knowledge, resignaƟon to pracƟces perceived as unavoidable, relief that the depicted communica Ɵon
was less extensive than an Ɵcipated, or con Ɵnued concern about par Ɵcular data ﬂows. The qualita Ɵve ﬁndings,
therefore, complement the path model by showing that quan ƟtaƟvely similar levels of conﬁrma Ɵon may arise from
diﬀerent forms of reasoning and evaluaƟon.
5.3 Discussion
Study 2 extends our invesƟgaƟon of smart-home privacy expectaƟons to a broader sample by experimentally
manipulaƟng the level of adverƟsing-related communicaƟon. Consistent with Study 1, we ﬁnd that trust-based
expectaƟons strongly predict trust conﬁrmaƟon, and trust conﬁrmaƟon posiƟvely predicts saƟsfacƟon. Across both
studies, saƟsfacƟon remains the strongest predictor of intenƟon to conƟnue using the device, reinforcing the core ECT
pathway that users’ willingness to stay with a smart-home device depends largely on whether the beneﬁts they
perceive from the overall experience outweigh the risks involved. We also found that awareness, operaƟonalized as
endorsement of transparency principles, was associated with lower trust conﬁrmaƟon. The items in this construct
assessed whether parƟcipants believed companies should clearly disclose how personal informaƟon is collected and
used, and whether being informed about such pracƟces was important. One possible explanaƟon is that parƟcipants
with stronger expectaƟons for transparency evaluated the adverƟsing-related communicaƟons depicted in the report
more criƟcally, resulƟng in lower trust conﬁrmaƟon. This interpretaƟon remains tentaƟve because we did not directly
measure how parƟcipants applied these transparency expectaƟons when evaluaƟng the report.
However, Study 2 revealed a cri Ɵcal nuance regarding ac Ɵve coping behaviors. Unlike the ﬁrst study, where
saƟsfacƟon fully mediated willingness to block, Study 2 par Ɵcipants’ willingness to block device communica Ɵons was
driven primarily by collec Ɵon concerns rather than sa ƟsfacƟon. This pa Ʃern is consistent with a more immediate
concern-based response in Study 2, whereas the Study 1 ﬁndings are consistent with a broader evaluaƟon of the privacy
risks and beneﬁts of device use aŌer parƟcipants viewed their actual network traﬃc. One possible explanaƟon for this
divergence is the composiƟon of the two samples. Study 1 parƟcipants were self-selected users who had joined the IoT
Inspector waiƟng list and installed the tool, whereas Study 2 drew from a broader online sample. However, because we
did not measure par Ɵcipants’ moƟvaƟons, technical experƟse, or privacy mo ƟvaƟon, we cannot determine whether
the samples diﬀered on these characteris Ɵcs or whether sample composi Ɵon explains the dis Ɵnct pa Ʃerns. Other
diﬀerences between the studies may also have contributed. Study 2’s simulated report, despite being framed as
reﬂecƟng the parƟcipant’s own device, may have provided less real -device salience than Study 1, where par Ɵcipants
viewed reports generated from their own devices’ actual, ongoing traﬃc. Relatedly, the simulated, one-Ɵme nature of
Study 2’s between-subjects design may have made blocking feel less consequenƟal than in Study 1’s ﬁeld deployment,
leading parƟcipants to rely more on general collec Ɵon concerns than on a sa ƟsfacƟon judgment Ɵed to the speciﬁc
report. We therefore present sample composiƟon, real-device salience, and the perceived consequences of blocking as
plausible but untested explanaƟons for the divergence.

EvaluaƟng Smart Home Device Users’ Responses to their (Un)Conﬁrmed Privacy ExpectaƟons 25
Furthermore, our experimental manipulaƟon provided insight into how the depicted volume of adverƟsing-related
communicaƟon inﬂuenced user outcomes. The condiƟon moderated the relaƟonships between parƟcipants’ baseline
and post-survey self-eﬃcacy and conƟnued-use intenƟons, indicaƟng that the HighAd and LowAd reports aﬀected
parƟcipants diﬀerently depending on their baseline levels. This underscores that transparency alone is not neutral;
the content of the report, speciﬁcally the depicted volume of adverƟsing-related communicaƟon, can shape users’
self-eﬃcacy and conƟnued-use intenƟons diﬀerently depending on their prior states. We emphasize, however, that
the LowAd and HighAd reports represented experimentally manipulated levels of adverƟsing-related communicaƟon,
not objecƟvely “good” or “bad” privacy pracƟces, and our design does not establish which level, if either,
manufacturers should regard as acceptable.
6 General Discussion
Our research integrates ﬁndings from an in-situ ﬁeld study ( 𝑁 = 35) and a controlled experiment ( 𝑁 = 132) to
demonstrate how inducing transparency inﬂuences user aƫtudes and behaviors. By applying ExpectaƟon-ConﬁrmaƟon
Theory (ECT) to the domain of smart home privacy, we show that conﬁrming trust expectaƟons is pivotal for maintaining
user sa ƟsfacƟon. When transparency tools reveal unexpected data prac Ɵces, sa ƟsfacƟon erodes, jeopardizing the
user’s intent to keep the device. Below, we discuss the theoreƟcal and pracƟcal implicaƟons of these ﬁndings.
6.1 TheoreƟcal ImplicaƟons
The Expecta Ɵon-ConﬁrmaƟon Theore Ɵcal framework examines users’ inten Ɵons to con Ɵnue using a system as a
funcƟon of the extent to which their expecta Ɵons of the system are conﬁrmed. We conceptualize users’ a Ʃempts to
remedy unconﬁrmed expectaƟons as correcƟve coping behaviors and note that lowering intenƟons to conƟnue using
the system is only one such response. As an ini Ɵal examinaƟon of an ac Ɵve, control-oriented response, we studied
whether users were willing to use an in-tool control to mark unfavorable device communicaƟons they wished to block
in the future. We therefore frame the extension of ECT to ac Ɵve coping as promising, though not yet established.
Establishing when and how trust conﬁrma Ɵon predicts ac Ɵve coping will require examining a broader range of
behaviors, such as actually blocking traﬃc, changing device se ƫngs, disabling features, dele Ɵng collected data, or
disconƟnuing speciﬁc data ﬂows, across more diverse populaƟons. Users may also employ other coping behaviors, such
as speaking quietly around smart speakers or providing them with misleading informaƟon [68].
Furthermore, we speciﬁcally studied privacy-related expectaƟons. Previous studies in the privacy literature that
adopted the ECT framework measured conﬁrmaƟon in broad terms, such as whether the funcƟonality is, overall,
beƩer than users’ expectaƟons [40, 92]. Although there is a trade-oﬀ between privacy and funcƟonality in many
scenarios [91, 95], privacy and funcƟonality are two disƟnct concepts. Therefore, by studying the conﬁrmaƟon of
funcƟonality expectaƟons, we will not be able to examine users’ privacy expectaƟons and the consequences of not
conﬁrming them. We speciﬁcally studied users’ trust expectaƟons of how they expect their devices to handle their
data. This enabled us to draw the consequences of conﬁrming or rejecƟng users’ trust expectaƟons. While ECT only
considers one type of expectaƟon, future studies can extend this framework by considering several parallel
expectaƟons and understanding the role of each expectaƟon in user saƟsfacƟon and device usage.
We conducted a mediaƟon analysis that showed saƟsfacƟon can fully mediate the eﬀects of trust conﬁrmaƟon on
coping behaviors (i.e., intenƟon to use) in both studies. This is an important ﬁnding for the ECT literature, as it
suggests that conﬁrmaƟon can lead to behavioral eﬀects, someƟmes solely through saƟsfacƟon, improving our
understanding of the ECT’s applicability to real-world scenarios. It is important to note that the saƟsfacƟon measured
in our studies was not general saƟsfacƟon with the device, but an appraisal of whether the beneﬁts of device use
outweighed the risks of informaƟon disclosure. This construct overlaps conceptually with perceived disclosure value
and privacy calculus. Accordingly, alternaƟve theoreƟcal interpretaƟons are plausible, and ECT should be understood
as one theoreƟcally grounded explanaƟon of the observed paƩern rather than the only possible explanaƟon.
6.2 PracƟcal ImplicaƟons

 26 Khatun et al.
Our research has important implicaƟons for smart home manufacturers and service providers. We studied
transparency aŌer adopƟon, as parƟcipants were already using smart-home devices, and found that when the data
pracƟces made visible did not align with users’ prior trust-based expectaƟons, users reported weaker intenƟons to
conƟnue using the device. This does not imply that data sharing itself necessarily reduces conƟnued-use intenƟons;
rather, the mismatch between users’ expectaƟons and the pracƟces made visible appears to maƩer. Manufacturers
should therefore not assume that purchasing and using a product means that users understand, accept, and are
saƟsﬁed with its data pracƟces.
To improve user sa ƟsfacƟon, companies should explore means to promote transparency post -purchase when a
device is already in use. We navigated one of these ways by providing users with a report on the data traﬃc of their
network. While this approach to inducing transparency damaged users’ sa ƟsfacƟon with the devices, we should
consider that the tools we used for promoƟng transparency, IoT Inspector and the report on Qualtrics, were generated
by third-party. The situaƟon will arguably be diﬀerent if  the devices themselves promote this transparency and bring
any potenƟally unfavorable data pracƟces to the user’s aƩenƟon. Research shows that poinƟng out a system’s ﬂaws by
the provider can even improve users’ trust in that provider [57]. Therefore, devices can check in with users by providing
them with a report of their data communicaƟons without compromising their trust.
AddiƟonally, when a device’s privacy pracƟces do not align with the user’s personal preferences, the device should
provide means to bridge this gap (e.g., through privacy seƫngs). Providing a control mechanism is especially
important, as some users may otherwise reduce their intenƟons to use the devices. Our two studies also suggest that
the drivers of acƟve control are not uniform across populaƟons and seƫngs, which bears on how such controls should
be designed and surfaced. In the in-situ ﬁeld study, willingness to block was associated with saƟsfacƟon, whereas in
the controlled experiment, it was driven primarily by collecƟon concerns. This divergence implies that a blocking
control may be reached for as part of an overall cost-beneﬁt evaluaƟon of the device by some users, but as a more
direct response to data-collecƟon concern by others, and manufacturers should not assume a single moƟvaƟonal
pathway when deciding how to present privacy seƫngs. Our work examined two coping behaviors that users may
employ when encountering undesirable data pracƟces: reducing intenƟons to conƟnue using the device and seeking
to limit undesirable device communicaƟons. The former is a passive coping behavior, prevenƟng users from beneﬁƟng
from their smart home devices altogether, and should arguably be the last resort. The laƩer is an acƟve coping
behavior, allowing users to conƟnue beneﬁƟng from the devices, at least to some degree. We can implement
procedures that allow acƟve coping strategies in various ways. For example, in the case of an unfavorable
communicaƟon, the user and device can engage in a dialogue where the device informs the user about the
implicaƟons of a change in the communicaƟon seƫngs for oﬀered services (e.g., whether a service will be
compromised or interrupted by withholding data, and if there are alternaƟves). This procedure could give users
greater control over their data and support trust, as perceived control is associated with trust [42]. This dialogue-
based approach also illustrates what granular controls could mean in pracƟce. Granular controls would allow users to
act on speciﬁc communicaƟons rather than choose between accepƟng all data sharing and disconƟnuing use of the
device. Our study materials illustrated this approach by separaƟng manufacturer-related from adverƟsing-related
communicaƟons and allowing parƟcipants to mark parƟcular communicaƟons for future blocking. For such controls to
be accessible, the dialogue should describe the available choices and their likely consequences in plain language,
including whether blocking a communicaƟon may aﬀect device funcƟons or services.
While we highlighted the beneﬁts of implemen Ɵng control mechanisms, we would like to emphasize a major
setback: exercising control is mentally demanding [ 14, 37]. The situa Ɵon is arguably worse for smart home
environments with various smart devices, as controlling the data prac Ɵces of each device is challenging, Ɵme-
consuming, and not feasible [ 77]. Our studies examined only a simple control that allowed par Ɵcipants to mark
parƟcular communicaƟons for future blocking. More complex controls across mul Ɵple devices may impose addiƟonal
interpretaƟon and management demands, reinforcing the importance of designing simpliﬁed and, where appropriate,
parƟally automated privacy controls. Scholars explored various ways to simplify exercising control, such as designing
dialogue-based systems that allow users to create security rules using natural language [ 37]. To further simplify user
interacƟon with privacy controls and ease the management burden on smart home device users, we should explore

EvaluaƟng Smart Home Device Users’ Responses to their (Un)Conﬁrmed Privacy ExpectaƟons 27
ways to complement simpliﬁed control mechanisms with some level of automaƟon. For example, the system can learn
users’ privacy preferences over Ɵme and apply these preferences to new devices.
The qualitaƟve ﬁndings further suggest that users who report that the depicted pracƟces were consistent with their
prior expectaƟons may nevertheless beneﬁt from diﬀerent forms of support. For example, par Ɵcipants who reported
overall consistency but expressed surprise about parƟcular communicaƟons may beneﬁt from controls that allow them
to act on those speciﬁc data ﬂows. Those whose responses reﬂected normaliza Ɵon or pragma Ɵc acceptance may
instead beneﬁt from prompts that encourage them t o consider whether the data prac Ɵces they expect are also
acceptable to them and what they could do about them. Transparency and control mechanisms should therefore
account for the diﬀerent ways users interpret the same informaƟon rather than providing the same noƟce to everyone.
6.3 Methodological ImplicaƟons: The Cost of Ecological Validity
Studying real-world scenarios and moving beyond convenience sampling methodologies is crucial in understanding
users’ aƫtudes and behaviors towards smart home devices. Emami-Naeini et al. [25] interviewed individuals who had
purchased IoT devices and found that privacy and security were not a major consideraƟon for most parƟcipants at the
Ɵme of purchase. However, in another study, they surveyed individuals about smart devices from MTurk, a
crowdsourcing plaƞorm, survey respondents showed higher interest in their willingness to purchase IoT devices if
they knew their data would not be retained or shared with others [24]. While these two studies have valuable
implicaƟons for markeƟng, they also highlight the importance of in-situ studies and the fact that real-life scenarios
with real users may have diﬀerent ﬁndings and implicaƟons than those with individuals from crowdsourcing plaƞorms
or non-users [7, 78]. Therefore, we call for more in-situ studies on privacy decision-making, especially in the context
of smart homes. However, a major challenge in such studies is recruiƟng parƟcipants since researchers may not have
access to a large sample as they do in convenience sampling methodologies. In Study 1, parƟcipants were self-
selected smart-home users who had voluntarily signed up to use IoT Inspector and may therefore have diﬀered from
the broader populaƟon of smart-home users. RecruiƟng more people from this demographic was not possible, as we
had already contacted everyone who had signed up to use the IoT Inspector, highlighƟng one of the recruitment
diﬃculƟes of such in-situ studies.
Taken together, the two studies oﬀer complementary methodological strengths. In Study 1, par Ɵcipants viewed
reports generated from their own smart-home devices’ network traﬃc in their homes, providing ecologically grounded
evidence of responses to real device communicaƟons, but the design did not allow us to isolate the eﬀects of parƟcular
report features. Study 2 instead used simulated reports in a controlled online experiment, allowing us to manipulate
the depicted level of adver Ɵsing-related communicaƟon, but not to make claims about par Ɵcipants’ actual device
behavior. Future work should combine these strengths by connecƟng users’ prior expectaƟons, their devices’ measured
communicaƟons, and their subsequent percepƟons and acƟons within a single longitudinal design.
7 LimitaƟons and Future Work
While our in-situ methodology has several unique advantages, such as studying real smart home device users in their
own environment and not having incen Ɵve-induced bias [ 43], it has important limita Ɵons. Our results should not be
generalized to the broader populaƟon of smart home device users. Our par Ɵcipants voluntarily installed and used the
IoT Inspector. This self-selecƟon may mean that parƟcipants were parƟcularly interested in learning about their devices’
data pracƟces and diﬀered from the broader populaƟon of smart-home users. However, because we did not measure
their mo ƟvaƟons, technical literacy, or prior familiarity with smart -device data prac Ɵces, we cannot determine the
nature or extent of these diﬀerences. These unmeasured characteris Ɵcs may also have shaped par Ɵcipants’ ini Ɵal
expectaƟons and interpretaƟons of the reports. Addi Ɵonally, we do not have demographic data such as age, gender,
and educaƟon status for our parƟcipants. In line with our IRB guidelines, we opted not to collect demographic data to
minimize the risk of de-anonymizaƟon. Furthermore, asking for demographic data could demoƟvate IoT Inspector users
from parƟcipaƟng in our study, lowering our response rates. Moreover, as parƟcipants joined the study on a voluntary
basis and without monetary compensaƟon, we minimized the survey quesƟons. Consequently, Study 1 relied on single-
item measures for each construct. This prevented us from assessing internal reliability or discriminant validity, and the

 28 Khatun et al.
path model should therefore be interpreted as exploratory rather than as a conﬁrmatory test of the underlying
constructs. Study 2 parƟally addresses this limitaƟon through its larger sample and mulƟ-item measures validated using
conﬁrmatory factor analysis.
A further limita Ɵon of Study 1 is that we did not retain report features in a par Ɵcipant-linked form. Although
parƟcipants viewed reports generated from their own device traﬃc, we could not examine how speciﬁc features, such
as traﬃc volume, des ƟnaƟon domains, or third -party recipients, related to their expecta Ɵons and post -survey
responses. Study 1 should consequently be interpreted as examining responses aŌer exposure to a real network-acƟvity
report, rather than iden Ɵfying which report contents drove those responses. Future work should link par Ɵcipants’
report features with their pre- and post-survey measures.
Our second study, the online experiment, faced a limita Ɵon regarding the scope of its manipula Ɵon. We focused
speciﬁcally on the volume of adverƟsing-related data traﬃc to test user reacƟons. However, privacy decision-making is
complex and mulƟfaceted; users likely consider not just the amount of data being shared, but the speciﬁc nature of
that data (e.g., sensi Ɵve audio recordings versus rou Ɵne usage logs) and the reputa Ɵon of the speciﬁc third -party
enƟƟes involved. By isolaƟng traﬃc volume as the primary independent variable, our study may overlook how diﬀerent
types of data sensi Ɵvity interact with trust to inﬂuence blocking decisions. Future research should explore these
nuances by manipula Ɵng data types and sensi Ɵvity levels alo ngside traﬃc volume. Study 2 also did not embed an
internal manipula Ɵon-check item; we addressed this with a separate supplementary check conﬁrming that the
condiƟons diﬀered in the intended direc Ɵon, though embedding such a check within the main pr otocol would be
preferable in future work. Relatedly, our survey items referred to “informa Ɵon disclosure” generally rather than
idenƟfying speciﬁc recipients. Future work could study data types and recipients, such as manufacturers, adver Ɵsers,
or other third parƟes, to examine how these factors shape privacy judgments and intended responses. More broadly,
because the two studies diﬀered in sample composi Ɵon, study se ƫng, and whether the reports reﬂected real or
simulated device traﬃc, we cannot determine which of these diﬀerences accounts for the associaƟon of willingness to
block with saƟsfacƟon (in Study 1) and with collecƟon concern (in Study 2). Future work should vary these factors more
systemaƟcally to examine when each pathway emerges.
Another limitaƟon of our study is that we cannot draw conclusions about speciﬁc devices individually (e.g., smart
speakers, smart TVs). For example, we are not able to pinpoint whether viola Ɵons of users’ expectaƟons by a speciﬁc
smart home device, th rough poor communica Ɵon or concealing data prac Ɵces, can inﬂuence users’ percep Ɵons of
other devices or if viola Ɵons by some types of devices have more detrimental eﬀects on users’ trust and usage
intenƟons. These are important areas for future research as they have policy implicaƟons. Suppose bad actors can easily
compromise users’ trust in other smart home devices. In this case, it would be even more criƟcal to establish industry-
wide standards on transparency and stricter control mechanisms to monitor alignment between devices’ data pracƟces
and their privacy policies. AddiƟonally, policymakers can propose legislaƟon imposing penalƟes on manufacturers and
service providers who broadly violate users’ expecta Ɵons. Furthermore, since users’ security and privacy a ƫtudes
towards smart devices are context-dependent and evolve as they acquire more informaƟon [64], future research should
examine the implicaƟons of adapƟve legislaƟon that evolves with technological advancements and user feedback.
Moreover, future research can explore whether the changes we observed in this study are long-term or short-lived.
In case of a long-term change, smart home devices may need to regain their users’ trust prior to their saƟsfacƟon and
usage, while a short-term change may revert when users resume using their devices and get immersed in their
experiences. A long-term study is more important when we consider disclosure decisions not only as a funcƟon of
privacy preferences but also as a funcƟon of disclosure beneﬁts. We studied expectaƟon conﬁrmaƟon and saƟsfacƟon
in the context of devices’ data pracƟces. Device performance is arguably a diﬀerent domain. If users are so reliant on
a technology to which they need to disclose data to make it funcƟonal, then being aware of the privacy pracƟces of
that device may not lead to coping behaviors. For example, individuals who want to navigate using the GPS will have
to let go of their physical locaƟon. Future studies should explore the interplay between performance and funcƟonality
expectaƟons and trust and privacy expectaƟons in the context of smart home devices.
Finally, our studies focused on primary device users who owned, conﬁgured, or administered their smart-home
devices. However, smart-home devices oŌen operate in shared spaces where household members, guests, and other

EvaluaƟng Smart Home Device Users’ Responses to their (Un)Conﬁrmed Privacy ExpectaƟons 29
bystanders may also be subject to data collecƟon without comparable awareness of, or access to, device controls [33,
98]. Transparency and control mechanisms designed for primary users may therefore not adequately protect individuals
who lack the access or authority to view device communicaƟons or modify privacy seƫngs. Future work should examine
how transparency mechanisms can inform all aﬀected individuals and how privacy controls can accommodate diﬀering
preferences and power relaƟonships among device owners, household members, guests, and other bystanders.
8 Conclusion
This research bridges a criƟcal gap in smart home privacy by integraƟng ﬁndings from an in-situ ﬁeld study and a
controlled experiment to demonstrate that transparency is a double-edged sword: conﬁrming trust reinforces
conƟnued use, while unexpected data pracƟces erode the user-device relaƟonship. Our applicaƟon of ExpectaƟon-
ConﬁrmaƟon Theory reveals that saƟsfacƟon predicts retenƟon, whereas speciﬁc privacy risks trigger acƟve defensive
measures, suggesƟng that the current noƟce and consent model is insuﬃcient. Instead, manufacturers must move
beyond simple transparency to provide granular, accessible controls that empower users to align device behavior with
their privacy norms, ensuring a smart home ecosystem built on veriﬁed trust rather than blind acceptance.
Acknowledgments
This research was supported in part by funding from Google through the CyberNYC ini ƟaƟve. The sponsor had no
inﬂuence on the study design, data analysis, interpretaƟon, or reporƟng.
References
[1] 2017. Amazon hands over Echo ’murder’ data. BBC News (March 2017). hƩps://www.bbc.com/news/technology-39191056
[2] 2018. Amazon patents ’voice-sniﬃng’ algorithms. BBC News (April 2018). hƩps://www.bbc.com/news/technology-43725708
[3] Mahdi Nasrullah Al- Ameen, Apoorva Chauhan, MA Manazir Ahsan, and Huzeyfe Kocabas. 2021. A look into user’s privacy percep Ɵons and data
pracƟces of IoT devices. InformaƟon & Computer Security 29, 4 (2021), 573–588.
[4] Tawﬁq Ammari, Joﬁsh Kaye, Janice Y. Tsai, and Frank Bentley. 2019. Music, search, and IoT: How people (really) use voice assistants. ACM
TransacƟons on Computer-Human InteracƟon 26, 3 (2019), 1–28.
[5] Reza Ghaiumy Anaraky, David Cherry, Marie Jarrell, and Bart Knijnenburg. 2019. TesƟng a comic-based privacy policy. In The 15th Symp. on
Usable Privacy and Security.
[6] Noah Apthorpe, Arunesh Mathur, Pardis Emami-Naeini, Marshini CheƩy, and Nick Feamster . 2019. You, me, and iot: How internet-connected home
devices aﬀect interpersonal relaƟonships. In Companion PublicaƟon of the 2019 Conference on Computer Supported Coopera Ɵve Work and Social
CompuƟng. 142–145.
[7] Noah Apthorpe, Yan Shvartzshnaider, Arunesh Mathur, Dillon Reisman, and Nick Feamster . 2018. Discovering smart home internet of things
privacy norms using contextual integrity. Proceedings of the ACM on interacƟve, mobile, wearable and ubiquitous technologies 2, 2 (2018), 1–23.
[8] Yannis-NYU Bakos, David R Trossen, et al. 2009. Does Anyone Read the Fine Print? Tes Ɵng a Law and Economics Approach toStandard For m
Contracts. (2009).
[9] Tiﬀany BarneƩ White. 2005. Consumer trust and advice acceptance: The modera Ɵng roles of benevolence, exper Ɵse, and nega Ɵve emo Ɵons.
Journal of Consumer Psychology 15, 2 (2005), 141–148.
[10] Eric PS Baumer, Phil Adams, Vera D Khovanskaya, Tony C Liao, Madeline E Smith, Victoria Schwanda Sosik, and Kaiton Williams. 2013. LimiƟng,
leaving, and (re) lapsing: an exploraƟon of facebook non-use pracƟces and experiences. In Proceedings of the SIGCHI conference on human factors
in compuƟng systems. 3257–3266.
[11] Anol BhaƩacherjee. 2001. Understanding informaƟon systems conƟnuance: An expectaƟon-conﬁrmaƟon model. MIS quarterly (2001), 351–370.
[12] Sam Blum. 2019. Google Calls Hidden Microphone in Its Nest Home Security Devices an ’Error’ . hƩps://www.popularmechanics.com/technology/
security/a26448907/google-nest-hidden-microphone/
[13] Virginia Braun and Victoria Clarke. 2006. Using themaƟc analysis in psychology. QualitaƟve Research in Psychology 3, 2 (2006), 77–101.
hƩps://doi.org/10.1191/1478088706qp063oa
[14] Christoph Buck, Tamara Dinev, and Reza Ghaiumy Anaraky. 2022. Revisi Ɵng apco. In Modern socio- technical perspec Ɵves on privacy . Springer
InternaƟonal Publishing Cham, 43–60.
[15] Raphaëlle Butori and Caroline Lancelot Miltgen. 2023. A Construal Level Theory Approach to Privacy ProtecƟon: The Conjoint Impact of the Beneﬁts
and Risks of InformaƟon Disclosure. Journal of Business Research 166 (2023), 114130. hƩps://doi.org/10.1016/j.jbusres.2023.114130
[16] JEN CALTRIDER. 2017. 10 Fascina Ɵng Things We Learned When We Asked The World ‘How Connected Are You?’ .
 hƩps://blog.mozilla.org/en/ mozilla/10-fascinaƟng-things-we-learned-when-we-asked-the-world-how-connected-are-you/

 30 Khatun et al.
[17] Chola Chhetri. 2019. Towards a smart home usable privacy framework. In Companion PublicaƟon of the 2019 Conference on Computer Supported
CooperaƟve Work and Social CompuƟng. 43–46.
[18] HaoƟan Chi, Qiang Zeng, Xiaojiang Du, and Lannan Luo. 2021. PFirewall: SemanƟcs-Aware Customizable Data Flow Control for Smart Home Privacy
ProtecƟon. In Proceedings of the Network and Distributed System Security Symposium (NDSS) . hƩps://doi.org/10.14722/ndss.2021.24464 [19]
 Joobin Choobineh and Anil D Kini. 2000. An Empirical Evalua Ɵon of the Factors Aﬀec Ɵng Trust in Web Bankng Systems. AMCIS 2000
Proceedings (2000), 169.
[20] Nigel Davies, Nina TaŌ, Mahadev Satyanarayanan, Sarah Clinch, and Brandon Amos. 2016. Privacy mediators: Helping IoT cross t he chasm. In
Proceedings of the 17th internaƟonal workshop on mobile compuƟng systems and applicaƟons. 39–44.
[21] Lucrezia Maria de Cosmo, Luigi Piper, and Arianna Di Vi Ʃorio. 2021. The role of a ƫtude toward chatbots and privacy concern  on the relaƟonship
between aƫtude toward mobile adverƟsing and behavioral intent to use chatbots. Italian Journal of MarkeƟng 2021 (2021), 83–102.
[22] Lihi Dery and Artyom Jelnov. 2021. Privacy–Accuracy ConsideraƟon in Devices That Collect Sensor-Based InformaƟon. Sensors 21, 14 (2021), 4684.
[23] Pardis Emami-Naeini, Yuvraj Agarwal, Lorrie Faith Cranor, and Hanan Hibshi. 2020. Ask the experts: What should be on an IoT privacy and
security label?. In 2020 IEEE Symposium on Security and Privacy (SP) . IEEE, 447–464.
[24] Pardis Emami-Naeini, Janarth Dheenadhayalan, Yuvraj Agarwal, and Lorrie Faith Cranor . 2021. Which privacy and security a Ʃributes most impact
consumers’ risk percepƟon and willingness to purchase IoT devices?. In 2021 IEEE Symposium on Security and Privacy (SP) . IEEE, 519–536.
[25] Pardis Emami-Naeini, Henry Dixon, Yuvraj Agarwal, and Lorrie Faith Cranor . 2019. Exploring how privacy and security factor into IoT device purchase
behavior . In Proceedings of the 2019 CHI Conference on Human Factors in Compu Ɵng Systems. 1–12.
[26] Villaronga E. F. Lutz C. Tamò- Larrieux A. Felzmann, H. 2019. Transparency You Can Trust: Transparency Requirements For Ar Ɵﬁcial Intelligence
Between Legal Norms and Contextual Concerns. Big Data & Society 6 (2019), 205395171986054. Issue 1.
hƩps://doi.org/10.1177/2053951719860542
[27] Yuanyuan Feng, Yaxing Yao, and Norman Sadeh. 2021. A design space for privacy choices: Towards meaningful privacy control in the internet of
things. In Proceedings of the 2021 CHI Conference on Human Factors in Compu Ɵng Systems. 1–16.
[28] Jonas Foehr and Claas Chris Ɵan Germelmann. 2020. Alexa, can I trust you? Exploring consumer paths to trust in smart voice -interacƟon
technologies. Journal of the AssociaƟon for Consumer Research 5, 2 (2020), 181–205.
[29] Geoﬀrey Fowler. 2019. You watch TV. Your TV watches back. The Washington Post (18 9 2019). hƩps://www.washingtonpost.com/technology/
2019/09/18/you-watch-tv-your-tv-watches-back/?noredirect=on
[30] Alisa Frik, Julia Bernd, and Serge Egelman. 2023. A Model of Contextual Factors Aﬀec Ɵng Older Adults’ Informa Ɵon-Sharing Decisions in the US.
ACM TransacƟons on Computer-Human InteracƟon 30, 1 (April 2023), 1073–0516. hƩps://doi.org/10.1145/3557888
[31] Ellen Garbarino and Olivia F Lee. 2003. Dynamic pricing in internet retail: eﬀects on consumer trust. Psychology & MarkeƟng 20, 6 (2003), 495–513.
[32] Radhika Garg and Hua Cui. 2022. Social Contexts, Agency, and Conﬂicts: Exploring Cri Ɵcal Aspects of Design for Future Smart  Home Technologies.
ACM TransacƟons on Computer-Human InteracƟon 29, 2, ArƟcle 11 (jan 2022), 30 pages. hƩps://doi.org/10.1145/3485058
[33] ChrisƟne Geeng and Franziska Roesner . 2019. Who’s In Control? InteracƟons in MulƟ-User Smart Homes. In Proceedings of the 2019 CHI Conference
on Human Factors in CompuƟng Systems. ACM, New York, NY, USA, 1–13. hƩps://doi.org/10.1145/3290605.3300498
[34] Reza Ghaiumy Anaraky, Yao Li, and Bart Knijnenburg. 2021. DiﬃculƟes of measuring culture in privacy studies. Proceedings of the ACM on Human-
Computer InteracƟon 5, CSCW2 (2021), 1–26.
[35] DebjyoƟ Ghosh, Can Liu, Shengdong Zhao, and Kotaro Hara. 2020. Commanding and Re -DictaƟon: Developing Eyes -Free Voice-Based InteracƟon
for EdiƟng Dictated Text. ACM TransacƟons on Computer-Human InteracƟon 27, 4 (2020), 1–31. hƩps://doi.org/10.1145/3390889
[36] Julia Gideon, Lorrie Cranor, Serge Egelman, and Alessandro AcquisƟ. 2006. Power strips, prophylacƟcs, and privacy, oh my!. In Proceedings of the
Second Symposium on Usable privacy and security . 133–144.
[37] Stanley Goﬃnet, Dona Ɵen Schmitz, Igor Zavalyshyn, Axel Legay, and E Ɵenne Rivière. 2021. Controlling security rules using natural dialogue: an
applicaƟon to smart home care. In Adjunct Proceedings of the 2021 ACM Interna Ɵonal Joint Conference on Pervasive and Ubiquitous Compu Ɵng
and Proceedings of the 2021 ACM InternaƟonal Symposium on Wearable Computers. 194–197.
[38] Junius Gunaratne and Oded Nov. 2017. Using interacƟve “NutriƟon labels” for ﬁnancial products to assist decision making un der uncertainty.
Journal of the AssociaƟon for InformaƟon Science and Technology 68, 8 (2017), 1836–1849.
[39] Yuanyuan Guo, Xin Wang, and Chaoyou Wang. 2022. Impact of privacy policy content on perceived eﬀec Ɵveness of privacy policy : the role of
vulnerability, benevolence and privacy concern. Journal of Enterprise InformaƟon Management 35, 3 (2022), 774–795.
[40] Anil Gupta, Anish Yousaf, and Abhishek Mishra. 2020. How pre- adopƟon expectancies shape post -adopƟon conƟnuance intenƟons: An extended
expectaƟon-conﬁrmaƟon model. InternaƟonal Journal of InformaƟon Management 52 (2020), 102094.
[41] Julie M Haney, Susanne M Furman, and Yasemin Acar. 2020. Smart home security and privacy mi ƟgaƟons: Consumer percep Ɵons, pracƟces, and
challenges. In HCI for Cybersecurity, Privacy and Trust: Second Interna Ɵonal Conference, HCI -CPT 2020, Held as Part of the 22nd HCI Interna Ɵonal
Conference, HCII 2020, Copenhagen, Denmark, July 19–24, 2020, Proceedings 22 . Springer, 393–411.
[42] Eelco Herder and Olaf van Maaren. 2020. Privacy dashboards: the impact of the type of personal data and user control on trust and perceived risk.
In Adjunct publicaƟon of the 28th ACM conference on user modeling, adapta Ɵon and personalizaƟon. 169–174.

EvaluaƟng Smart Home Device Users’ Responses to their (Un)Conﬁrmed Privacy ExpectaƟons 31
[43] Gary Hsieh and Rafał Kocielnik. 2016. You get who you pay for: The impact of incen Ɵves on par ƟcipaƟon bias. In Proceedings of the 19th ACM
conference on computer-supported cooperaƟve work & social compuƟng. 823–835.
[44] Danny Yuxing Huang. 2022. IRB Protocol for IoT Inspector: ProtecƟng the Security and Privacy of Smart Home Device Users.  hƩps:
//inspector .engineering.nyu.edu/irb
[45] Danny Yuxing Huang. 2022. Three Years of Crowdsourcing Smart Home Network Traﬃc. USENIX ;login: (25 7 2022). hƩps://www.usenix.org/
publicaƟons/loginonline/three-years-crowdsourcing-smart-home-network-traﬃc
[46] Danny Yuxing Huang. 2024. IoT Inspector. hƩps://github.com/nyu-mlab/iot-inspector-client. hƩps://github.com/nyu-mlab/iot-inspector-client
GitHub repository.
[47] Danny Yuxing Huang, Noah Apthorpe, Frank Li, Gunes Acar, and Nick Feamster . 2020. Iot inspector: Crowdsourcing labeled network traﬃc from
smart home devices at scale. Proceedings of the ACM on Interac Ɵve, Mobile, Wearable and Ubiquitous Technologies 4, 2 (2020), 1–21.
[48] IoT Inspector Team. 2024. IoT Inspector . hƩps://inspector .engineering.nyu.edu/. Accessed: February 2024.
[49] Umar Iqbal, Pouneh Nikkhah Bahrami, Rahmadi Trimananda, Hao Cui, Alexander Gamero-Garrido, Daniel J Dubois, David Choﬀnes, Athina
Markopoulou, Franziska Roesner, and Zubair Shaﬁq. 2023. Tracking, Proﬁling, and Ad TargeƟng in the Alexa Echo Smart Speaker Ecosystem. In
Proceedings of the 2023 ACM on Internet Measurement Conference . 569–583.
[50] Timo Jakobi, Gunnar Stevens, Nico Castelli, Corinna Ogonowski, Florian Schaub, Nils Vindice, Dave Randall, Peter Tolmie, and Volker Wulf. 2018.
Evolving needs in IoT control and accountability: A longitudinal study on smart home intelligibility. Proceedings of the ACM on InteracƟve, Mobile,
Wearable and Ubiquitous Technologies 2, 4 (2018), 1–28.
[51] Milena Janic, Jan Pieter Wijbenga, and Thijs Veugen. 2013. Transparency enhancing tools (TETs): an overview. In 2013 Third Workshop on Socio-
Technical Aspects in Security and Trust. IEEE, 18–25.
[52] Carlos Jensen and Colin PoƩs. 2004. Privacy policies as decision-making tools: an evaluaƟon of online privacy noƟces. In Proceedings of the SIGCHI
conference on Human Factors in CompuƟng Systems. 471–478.
[53] Haojian Jin, Swarun Kumar, and Jason Hong. 2020. Providing architectural support for building privacy- sensiƟve smart home applicaƟons. In
Adjunct Proceedings of the 2020 ACM InternaƟonal Joint Conference on Pervasive and Ubiquitous Compu Ɵng and Proceedings of the 2020 ACM
InternaƟonal Symposium on Wearable Computers. 212–217.
[54] Han Y. Joo, J. 2021. An Evidence Of Distributed Trust In Blockchain-based Sustainable Food Supply Chain. Sustainability 13 (2021), 10980. Issue 19.
hƩps://doi.org/10.3390/su131910980
[55] Sabrina Karwatzki, Olga Dytynko, Manuel Trenz, and Daniel Veit. 2017. Beyond the personaliza Ɵon–privacy paradox: Privacy valua Ɵon,
transparency features, and service personalizaƟon. Journal of Management InformaƟon Systems 34, 2 (2017), 369–400.
[56] Patrick Gage Kelley, Joanna Bresee, Lorrie Faith Cranor, and Robert W Reeder . 2009. A" nutriƟon label" for privacy. In Proceedings of the 5th
Symposium on Usable Privacy and Security . 1–12.
[57] Gideon Keren. 2007. Framing, intenƟons, and trust–choice incompaƟbility. OrganizaƟonal Behavior and Human Decision Processes 103, 2 (2007),
238–255.
[58] Thorin Klosowski. 2020. Why You Should Take a Close Look at What Tracks You. The New York Times (7 1 2020). hƩps://www.nyƟmes.com/2020/
01/07/opinion/locaƟon-tracking-privacy.html
[59] Lorenz Kustosch, Carlos Gañán, Maƫs van ’t Schip, Michel van Eeten, and Simon Parkin. 2023. Measuring Up to (Reasonable) Co nsumer
ExpectaƟons: Providing an Empirical Basis for Holding IoT Manufacturers Legally Responsible. In 32nd USENIX Security Symposium (USENIX Security
23). USENIX AssociaƟon, Anaheim, CA, 1487–1504. hƩps://www.usenix.org/conference/usenixsecurity23/presentaƟon/kustosch
[60] Haley M LaMonica, Anna E Roberts, Grace Yeeun Lee, Tracey A Davenport, and Ian B Hickie. 2021. Privacy prac Ɵces of health informa Ɵon
technologies: privacy policy risk assessment study and proposed guidelines. Journal of Medical Internet Research 23, 9 (2021), e26317.
[61] Thomas W Lauer and Xiaodong Deng. 2007. Building online trust through privacy pracƟces. InternaƟonal Journal of InformaƟon Security 6 (2007),
323–331.
[62] Tu Le, Alan Wang, Yaxing Yao, Yuanyuan Feng, Arsalan Heydarian, Norman Sadeh, and Yuan Tian. 2023. Exploring Smart Commercial Building
Occupants’ PercepƟons and No ƟﬁcaƟon Preferences of Internet of Things Data Collec Ɵon in the United States. arXiv preprint arXiv:2303.04955
(2023).
[63] Hosub Lee and Alfred Kobsa. 2017. Privacy preference modeling and predic Ɵon in a simulated campuswide IoT environment. In 2017 IEEE
InternaƟonal Conference on Pervasive CompuƟng and CommunicaƟons (PerCom). IEEE, 276–285.
[64] Jingjie Li, Kaiwen Sun, BriƩany Skye Huﬀ, Anna Marie Bierley, Younghyun Kim, Florian Schaub, and Kassem Fawaz. 2023. “It’s up to the Consumer
to be Smart”: Understanding the Security and Privacy A ƫtudes of Smart Home Users on Reddit. In IEEE Symp. on Security and Privacy (SP)(SP) .
380–396.
[65] Yuanchun Li, Fanglin Chen, Toby Jia-Jun Li, Yao Guo, Gang Huang, MaƩhew Fredrikson, Yuvraj Agarwal, and Jason I Hong. 2017. Privacystreams:
Enabling transparency in personal data processing for mobile apps. Proceedings of the ACM on Interac Ɵve, Mobile, Wearable and Ubiquitous
Technologies 1, 3 (2017), 1–26.
[66] Christy Lleras. 2005. Path analysis. Encyclopedia of social measurement 3, 1 (2005), 25–30.
[67] Ewa Luger, Stuart Moran, and Tom Rodden. 2013. Consent for all: revealing the hidden complexity of terms and condiƟons. In Proceedings of the
SIGCHI conference on Human factors in compuƟng systems. 2687–2696.

 32 Khatun et al.
[68] Christoph Lutz and Gemma Newlands. 2021. Privacy and smart speakers: A mul Ɵ-dimensional approach. The InformaƟon Society 37, 3 (2021),
147–162.
[69] David Major, Danny Yuxing Huang, Marshini CheƩy, and Nick Feamster. 2021. Alexa, Who Am I Speaking To? Understanding Users’ Ability to IdenƟfy
Third-Party Apps on Amazon Alexa. ACM TransacƟons on Internet Technology 22, 1 (2021), 1–22.
[70] Naresh K Malhotra, Sung S Kim, and James Agarwal. 2004. Internet users’ informa Ɵon privacy concerns (IUIPC): The construct, the scale, and a
causal model. InformaƟon systems research 15, 4 (2004), 336–355.
[71] Nathan Malkin, Julia Bernd, Maritza Johnson, and Serge Egelman. 2018. what can’t data be used for?” privacy expectaƟons about smart tvs in the
us. In Proceedings of the 3rd European Workshop on Usable Security (EuroUSEC), London, UK .
[72] Anna Maria Mandalari, Daniel J. Dubois, Roman Kolcun, Muhammad Talha Paracha, Hamed Haddadi, and David Choﬀnes. 2021. Blocking Without
Breaking: IdenƟﬁcaƟon and MiƟgaƟon of Non-EssenƟal IoT Traﬃc. Proceedings on Privacy Enhancing Technologies (PoPETs) 2021, 4 (2021), 369–
388.
hƩps://doi.org/10.2478/popets-2021-0075
[73] Peter Mayer, Yixin Zou, Byron M. Lowens, Hunter A. Dyer, Khue Le, Florian Schaub, and Adam J. Aviv. 2023. Awareness, Inten Ɵon, (In)Ac Ɵon:
Individuals’ ReacƟons to Data Breaches. ACM TransacƟons on Computer-Human InteracƟon 30, 5, ArƟcle 77 (Sept. 2023). hƩps://doi.org/10.1145/
3589958
[74] Aleecia M McDonald and Lorrie Faith Cranor. 2008. The cost of reading privacy policies. Isjlp 4 (2008), 543.
[75] Aleecia M McDonald and Lorrie Faith Cranor . 2009. The Cost of Reading Privacy Policies 2008 Privacy Year in Review. I. S: A Journal of Law and
Policy for the InformaƟon Society 4, 3 (2009), 2008.
[76] D Harrison McKnight, Vivek Choudhury, and Charles Kacmar . 2002. Developing and valida Ɵng trust measures for e -commerce: An integra Ɵve
typology. InformaƟon systems research 13, 3 (2002), 334–359.
[77] Eliza Mik. 2020. The Disappearing Computer: Consent and Disclosure in the World of Smart Objects. European Journal of Consumer Law, November
(2020).
[78] Pardis Emami Naeini, Sru Ɵ Bhagavatula, Hana Habib, Mar Ɵn Degeling, Lujo Bauer, Lorrie Faith Cranor, and Norman Sadeh. 2017.  Privacy
expectaƟons and preferences in an IoT world. In Thirteenth Symposium on Usable Privacy and Security (SOUPS 2017) . USENIX Associa Ɵon Santa
Clara, 399–412.
[79] Duyen T Nguyen, Laura A Dabbish, and Sara Kiesler . 2015. The perverse eﬀects of social transparency on online advice taking. In Proceedings of
the 18th ACM Conference on Computer Supported Coopera Ɵve Work & Social CompuƟng. 207–217.
[80] Jonathan A Obar . 2022. Deﬁning and assessing data privacy transparency: A third study of Canadian internet carriers. InternaƟonal Journal of
CommunicaƟon 16 (2022), 25.
[81] Charith Perera, Ciaran McCormick, Arosha K Bandara, Blaine A Price, and Bashar Nuseibeh. 2016. Privacy-by-design framework for assessing
internet of things applicaƟons and plaƞorms. In Proceedings of the 6th InternaƟonal Conference on the Internet of Things . 83–92.
[82] MarƟn Porcheron, Joel E. Fischer, Stuart Reeves, and Sarah Sharples. 2018. Voice Interfaces in Everyday Life. In Proceedings of the 2018 CHI
Conference on Human Factors in CompuƟng Systems (CHI ’18). hƩps://doi.org/10.1145/3173574.3174214
[83] Leon Reicherts, Yvonne Rogers, Licia Capra, Ethan Wood, Tu Dinh Duong, and Neil Sebire. 2022. It’s good to talk: A comparison of using voice
versus screen-based interacƟons for agent-assisted tasks. ACM TransacƟons on Computer-Human InteracƟon 29, 3 (2022), 1–41.
[84] Michael J Roszkowski and Andrew G Bean. 1990. Believe it or not! Longer ques Ɵonnaires have lower response rates. Journal of Business and
Psychology 4 (1990), 495–509.
[85] William Seymour, MarƟn J. Kraemer, Reuben Binns, and Max Van Kleek. 2020. Informing the Design of Privacy-Empowering Tools for the
Connected Home. In Proceedings of the 2020 CHI Conference on Human Factors in Compu Ɵng Systems (Honolulu, HI, USA) (CHI ’20). ACM, New
York, NY, USA, 1–14. hƩps://doi.org/10.1145/3313831.3376264
[86] Deepak Sirdeshmukh, Jagdip Singh, and Barry Sabol. 2002. Consumer trust, value, and loyalty in rela Ɵonal exchanges. Journal of markeƟng 66, 1
(2002), 15–37.
[87] Michael G Smith, Maryam WiƩe, Sarah Rocha, and Mathias Basner . 2019. EﬀecƟveness of incenƟves and follow-up on increasing survey response
rates and parƟcipaƟon in ﬁeld studies. BMC medical research methodology 19, 1 (2019), 1–13.
[88] Daniel S Soper . 2016. Post-hoc staƟsƟcal power calculator for mul Ɵple regression [So Ōware]. Preuzeto s h Ʃp://www. danielsoper. com/statcalc
(2016).
[89] Aries Susanto, Younghoon Chang, and Youngwook Ha. 2016. Determinants of con Ɵnuance intenƟon to use the smartphone banking s ervices: An
extension to the expectaƟon-conﬁrmaƟon model. Industrial Management & Data Systems 116, 3 (2016), 508–525.
[90] Shirley Taylor and Peter A. Todd. 1995. Decomposi Ɵon and Crossover Eﬀects in the Theory of Planned Behavior: A Study of Consumer Adop Ɵon
IntenƟons. InternaƟonal Journal of Research in MarkeƟng 12, 2 (1995), 137–155. hƩps://doi.org/10.1016/0167 -8116(94)00019-K
[91] Lev Velykoivanenko, Kavous Salehzadeh Niksirat, Noé Zuﬀerey, Mathias Humbert, Kévin Huguenin, and Mauro Cherubini. 2021. Are those steps
worth your privacy? Fitness- tracker users’ percep Ɵons of privacy and u Ɵlity. Proceedings of the ACM on Interac Ɵve, Mobile, Wearable and
Ubiquitous Technologies 5, 4 (2021), 1–41.
[92] Ming-Yan Wang, Peng-Zhu Zhang, Cheng-Yang Zhou, and Neng-Ye Lai. 2019. Eﬀect of emoƟon, expectaƟon, and privacy on purchase inten Ɵon in
WeChat health product consumpƟon: The mediaƟng role of trust. InternaƟonal journal of environmental research and public health 16, 20 (2019),
3861.

EvaluaƟng Smart Home Device Users’ Responses to their (Un)Conﬁrmed Privacy ExpectaƟons 33
[93] Weiquan Wang and Izak Benbasat. 2007. RecommendaƟon agents for electronic commerce: Eﬀects of explanaƟon faciliƟes on trusƟng beliefs.
Journal of Management InformaƟon Systems 23, 4 (2007), 217–246.
[94] Cou-Chen Wu, Yves Huang, and Chia-Lin Hsu. 2014. Benevolence trust: a key determinant of user con Ɵnuance use of online social networks.
InformaƟon Systems and e-Business Management 12 (2014), 189–211.
[95] Heng Xu, Xin Robert Luo, John M Carroll, and Mary Beth Rosson. 2011. The personaliza Ɵon privacy paradox: An exploratory stud y of decision
making process for locaƟon-aware markeƟng. Decision support systems 51, 1 (2011), 42–52.
[96] Jingjun David Xu, Ronald T Cenfetelli, and Karl Aquino. 2016. Do diﬀerent kinds of trust ma Ʃer? An examinaƟon of the three  trusƟng beliefs on
saƟsfacƟon and purchase behavior in the buyer–seller context. The Journal of Strategic InformaƟon Systems 25, 1 (2016), 15–31.
[97] Yaxing Yao. 2019. Designing for beƩer privacy awareness in smart homes. In Companion PublicaƟon of the 2019 Conference on Computer Supported
CooperaƟve Work and Social CompuƟng. 98–101.
[98] Yaxing Yao, JusƟn Reed Basdeo, Oriana Rosata Mcdonough, and Yang Wang. 2019. Privacy PercepƟons and Designs of Bystanders in Smart Homes.
Proceedings of the ACM on Human-Computer InteracƟon 3, CSCW (2019), 1–24. hƩps://doi.org/10.1145/3359161
[99] Eric Zeng, Shrirang Mare, and Franziska Roesner . 2017. End user security and privacy concerns with smart homes. In thirteenth symposium on
usable privacy and security (SOUPS 2017) . 65–80.
[100] Serena Zheng, Noah Apthorpe, Marshini CheƩy, and Nick Feamster . 2018. User percepƟons of smart home IoT privacy. Proceedings of the ACM on
human-computer interacƟon 2, CSCW (2018), 1–20.
A Appendices
A.1 Full Path Model For Study 2
Variable Names Standardized coefficients Standard error p-value
DV: Confirmation (t2)
Privacy Expectations (t1) 0.541 0.375 0.149
Privacy Concerns (t1) 0.096 0.186 0.605
DV: Satisfaction (t2)
Perceived Benefits (t1) 0.098 0.184 0.596
Perceived Risks (t1) -0.236 0.210 0.260
Confirmation of Privacy Beliefs (t2) 0.518 0.213 0.015
Privacy Concerns (t1) 0.172 0.177 0.329
DV: Intentions to Use IoT (t2)
Intentions to Use IoT (t1) 0.287 0.176 0.104
Satisfaction (t2) 0.469 0.111 0.001
Confirmation of Privacy Beliefs (t2) 0.221 0.155 0.153
Privacy Concerns (t1) -0.019 0.144 0.894
DV: Privacy Feature Use (t2)
Satisfaction (t2) -0.826 0.225 <0.001
Confirmation of Privacy Beliefs (t2) 0.003 0.054 0.951
Privacy Concerns (t1) 0.058 0.050 0.252
Table 8. The non-signiﬁcant eﬀects were trimmed out and the ﬁnal model only consƟtutes the signiﬁcant eﬀects, presented in bold
style. However, this table also shows the coeﬃcient and p-values for the trimmed eﬀects before they were trimmed out.
A.2 Study 1 Instrument
Study 1 used single-item measures for each construct in order to minimize parƟcipant burden in an uncompensated
ﬁeld deployment (see SecƟon 4.1.2). For each construct, we selected either the highest-loading item from the original
validated instrument or, based on discussion among the authors, the item that most directly captured the construct’s

 34 Khatun et al.
conceptual deﬁniƟon. All items were rated on a 7-point Likert scale ranging from “Strongly Disagree” (1) to “Strongly
Agree” (7).
ParƟcipants completed the pre -survey immediately a Ōer providing informed consent and before viewing the IoT
Inspector report. AŌer interacƟng with the report for at least ﬁve minutes, they were prompted to complete the post-
survey. Figure 9–14 show the IoT Inspector interface that Study 1 parƟcipants interacted with, in the order they typically
encountered it. For readability in this appendix, we organize items under construct labels (e.g., Trust-Based ExpectaƟon,
SaƟsfacƟon). ParƟcipants saw the survey item text itself, but not these construct labels.

Fig. 9. A screenshot of the IoT Inspector. Users install the soŌware and access the user interface through their browser.

Fig. 10. A screenshot of the IoT Inspector. Users install the soŌware and access the user interface through their browser.

EvaluaƟng Smart Home Device Users’ Responses to their (Un)Conﬁrmed Privacy ExpectaƟons 35

Fig. 11. A screenshot of the IoT Inspector. Users install the soŌware and access the user interface through their browser.

Fig. 12. A screenshot of the IoT Inspector. Users install the soŌware and access the user interface through their browser.

 36 Khatun et al.

Fig. 13. A screenshot of the IoT Inspector. Users install the soŌware and access the user interface through their browser.

Fig. 14. A screenshot of the IoT Inspector. Users install the soŌware and access the user interface through their browser.
A.2.1 Pre-Survey.
Informed consent. Upon installing IoT Inspector, users saw an informed consent form asking whether they wished to
parƟcipate in the study. Users who declined could conƟnue using IoT Inspector without answering survey quesƟons or
donaƟng network data; for these users, the tool operated locally without transmi ƫng data to the researchers. The
consent form stated that data dona Ɵon included sharing the IoT Inspector report, comprising informa Ɵon about
parƟcipants’ smart devices, the frequency with which those devices sen d out data, and the domains with which the
devices communicate.
Trust-Based ExpectaƟon.
• My Smart Devices keep my best interests when handling my personal data.
Privacy Concerns.
• All things considered, the Internet would cause serious privacy problems.
SaƟsfacƟon.

EvaluaƟng Smart Home Device Users’ Responses to their (Un)Conﬁrmed Privacy ExpectaƟons 37
• I think my beneﬁts gained from the use of my Smart Devices can oﬀset the risks of my informaƟon
disclosure.
IntenƟons to ConƟnue Use.
• I intend to conƟnue using my Smart Devices rather than disconƟnue its use.
A.2.2 InteracƟon with IoT Inspector. ParƟcipants installed IoT Inspector and browsed the report generated from
their own devices’ network traﬃc. The report included the frequency with which each smart device communicated
data, the desƟnaƟon domain names (e.g., google.com), and the desƟnaƟon geographic locaƟons (e.g., USA).
ParƟcipants were prompted to complete the post-survey aŌer at least ﬁve minutes of interacƟon with the report.
A.2.3 Post-Survey.
Trust ConﬁrmaƟon.
• Overall, most of my expectaƟons regarding how my Smart Devices handle my personal data were
conﬁrmed. Items were coded such that higher scores indicate stronger perceived conﬁrma Ɵon of par Ɵcipants’
prior trust-based expectaƟons.
Repeated measures. Privacy Concern, Sa ƟsfacƟon, Inten Ɵons to Con Ɵnue Use were re -administered a Ōer the
interacƟon with IoT inspector, using the same item wordings and scale anchors listed in the pre-survey above.
A.2.4 Behavioral Measure: WanƟng to Block. Willingness to block was not measured with a survey item. It was captured
through an interface control within IoT Inspector: a checkbox labeled “Want to Block?” displayed next to each data-
collecƟon instance for each smart device, allowing parƟcipants to mark communicaƟons they wished to prevent from
recurring. This control is visible in the lower-right porƟon of Figure 2.
A.3    Study 2 Survey Instrument
Items are presented below in the order in which parƟcipants encountered them. All Likert items used a fully labeled
7-point scale (1 = Strongly disagree, 2 = Disagree, 3 = Somewhat disagree, 4 = Neither agree nor disagree, 5 = Somewhat
agree, 6 = Agree, 7 = Strongly agree). Throughout the survey, references to the par Ɵcipant’s device were piped in
dynamically based on the device they selected (shown below as [device]) and the brand they entered (shown as
[brand]).
A.3.1 Pre-Survey.
Informed consent. ParƟcipants reviewed an informed consent form and provided explicit electronic consent before
proceeding. Only parƟcipants who consented could conƟnue.
Device selecƟon. Please select one of the following devices that you currently use. The rest of the survey will focus
on your experiences with that device.
• Smart Speaker
• Smart TV
• Smart Camera
Brand. What is the brand name for your [smart device] (if you have several, please enter the one you use the most).
Please don’t provide any idenƟfying informaƟon. (open text response)
Technology Self-Eﬃcacy. Please specify if you agree or disagree with the following statements:
(1) I would feel comfortable using my [smart device] on my own.
(2) If I want to, I can use my [smart device] on my own easily.

 38 Khatun et al.
(3) I would be able to use my [smart device] even if there is no one around to show me how to use it.
SaƟsfacƟon (Perceived Value of InformaƟon Disclosure). Please specify if you agree or disagree with the following
statements:
(1) I think my beneﬁts gained from the use of my [smart device] can oﬀset the risks of my informaƟon disclosure.
(2) The value I gain from use of my [smart device] is worth the informaƟon I give away.
(3) I think the beneﬁts gained from using my [smart device] will be more than the risks of my informa Ɵon
disclosures.
Trust-Based ExpectaƟon. Presented with the shared stem “I expect my [smart device] to ...”:
(1) ...put my interests ﬁrst when handling my personal data.
(2) ...keep my interests in mind when handling my personal data.
(3) ...understand my needs and preferences when handling my personal data.
IntenƟons to ConƟnue Use. Please specify if you agree or disagree with the following statements:
(1) I intend to conƟnue using my [smart device] rather than disconƟnue its use.
(2) My intenƟons are to conƟnue using my [smart device] than use any alternaƟve means.
(3) If I could, I would like to conƟnue my use of [smart device].
CollecƟon Concern. Please specify if you agree or disagree with the following statements:
(1) It usually bothers me when online companies ask me for personal informaƟon.
(2) When online companies ask me for personal informaƟon, I someƟmes think twice before providing it.
(3) It bothers me to give personal informaƟon to so many online companies.
(4) I’m concerned that online companies are collecƟng too much personal informaƟon about me.
Awareness. Please specify if you agree or disagree with the following statements:
(1) Companies seeking informaƟon online should disclose the way the data are collected, processed, and used.
(2) Please select “Disagree”4
(3) A good consumer online privacy policy should have a clear and conspicuous disclosure.
(4) It is very important to me that I am aware and knowledgeable about how my personal informaƟon will be used.
Unauthorized Use. Please specify if you agree or disagree with the following statements:
(1) Online companies should not use personal informa Ɵon for any purpose unless it has been authorized by the
individuals who provided informaƟon.
(2) When people give personal informa Ɵon to an online company for some reason, the online company should
never use the informaƟon for any other reason.
(3) Online companies should never sell the personal informaƟon in their computer databases to other companies.
(4) Online companies should never share personal informaƟon with other companies unless it has been authorized
by the individuals who provided the informaƟon.
A.3.2 SƟmulus PresentaƟon. ParƟcipants were ﬁrst shown the message: “Now we will analyze your network data
to tell you about the data pracƟces of your [smart device],” followed by an animated progress bar displaying
“Analyzing your network data...”
ParƟcipants were then randomly assigned to view either the LowAd or the HighAd report. Both reports were
introduced with idenƟcal text: “Below, you can see how much data your [device] communicated with [brand] and with
ADVERTISEMENT-related domains: All enƟƟes contacted by this device over the last 10 minutes.” Each report displayed

4 This item was an aƩenƟon check embedded within the Awareness block and was not included in the Awareness construct.

EvaluaƟng Smart Home Device Users’ Responses to their (Un)Conﬁrmed Privacy ExpectaƟons 39
traﬃc volume for the manufacturer server and for adver Ɵsement domains, followed by the prompt “If you want to
block the AdverƟsement Domain click the checkbox below” and a single response opƟon, “Block communicaƟons with
AdverƟsement Domains.”
• LowAd condiƟon: [brand] Server – 842 KB uploaded, 392 KB downloaded; Adver Ɵsement Domains – 90 KB
uploaded, 110 KB downloaded.
• HighAd condiƟon: [brand] Server – 842 KB uploaded, 392 KB downloaded; Adver Ɵsement Domains – 1.2 MB
uploaded, 900 KB downloaded.
The full reports as parƟcipants saw them:

Fig. 15. Simulated network acƟvity reports comparing the HighAd condiƟons. AdverƟsement traﬃc volume is displayed relaƟve to
the manufacturer baseline (e.g., LG or Samsung servers), with a radio buƩon as a choice opƟon for blocking communicaƟons.

Fig. 16. Simulated network acƟvity reports comparing the LowAd condiƟons. AdverƟsement traﬃc volume is displayed relaƟve to the
manufacturer baseline (e.g., LG or Samsung servers), with a radio buƩon as a choice opƟon for blocking communicaƟons.

 40 Khatun et al.
A.3.3 Post-Survey. ParƟcipants were introduced to the post-survey with the message “Thanks for responding to
our quesƟons. Here are a few more quesƟons.”
Trust ConﬁrmaƟon. (post-survey only) Please specify if you agree or disagree with the following statements:
(1) The way my [smart device] handled my personal data was beƩer than what I expected.
(2) Overall, most of my expecta Ɵons regarding how my [smart device] handle my personal data were
conﬁrmed. 5 (3) My experience conﬁrmed that my [smart device] put my interest ﬁrst when handling my
personal data.
(4) My experience conﬁrmed that my [smart device] keep my interests in mind when handling my personal data.
(5) My experience conﬁrmed that my [smart device] want to understand my needs and preferences when handling
my personal data.
Repeated measures. Self-Eﬃcacy, SaƟsfacƟon, Inten Ɵons to Con Ɵnue Use, Collec Ɵon Concern, Awareness, and
Unauthorized Use were re-administered aŌer the manipulaƟon, in that order, using the same item wordings and scale
anchors listed in the pre-survey above. An aƩenƟon-check item (“Please select ‘Strongly Agree’ ”) was embedded within
the CollecƟon Concern block and was not included in the construct.
Open-ended and usage quesƟons.
(1) Were the data pracƟces of your [smart device] consistent with your expectaƟons? Please explain. Please don’t
provide any idenƟfying informaƟon. (open text response)
(2) How frequently do you use your [smart device]? (About once a week / Several Ɵmes a week / At least once a
day / Several Ɵmes a day / Almost constantly)
(3) What do you use your [smart device] for? Please provide examples. Please don’t provide any idenƟfying
informaƟon. (open text response)
(4) What did you think about the report we showed you on your network traﬃc, and did you want to see any
other informaƟon in the report? Please don’t provide any idenƟfying informaƟon. (open text response) The
themaƟc analysis reported in SecƟon 5.2.4 analyzed responses to the ﬁrst of these quesƟons.
AddiƟonal exploratory items. Two further items were administered but were not analyzed in this paper:
(1) The report that I saw about data pracƟces of my [smart device] improved my performance in managing my home.
(2) The report that I saw about the data pracƟces of my [smart device] improved my performance in managing my
Privacy.
Demographics.
• EducaƟon. What is the highest level of school you have completed or the highest degree you have received?
(High school incomplete or less; High school graduate or GED (includes technical/vocaƟonal training that
doesn’t count towards college credit); Some college (some community college, associate’s degree); Four year
college degree/bachelor’s degree; Some postgraduate or professional schooling, no postgraduate degree;
Postgraduate or professional degree, including master’s, doctorate, medical or law degree)
• Race. Which of the following describes your race? You can select as many as apply. (White; Black or
AfricanAmerican; American Indian or Alaska NaƟve; Asian or Asian-American; NaƟve Hawaiian/Other Paciﬁc
Islanders; Some other race)

5 Removed from the ﬁnal measurement model due to a low standardized factor loading (see Sec Ɵon 5.2.1).

EvaluaƟng Smart Home Device Users’ Responses to their (Un)Conﬁrmed Privacy ExpectaƟons 41
• Income. What is your total household income? (Less than $10,000; $10,000 to less than $20,000; $20,000 to
less than $30,000; $30,000 to less than $40,000; $40,000 to less than $50,000; $50,000 to less than $75,000;
$75,000 to less than $100,000; $100,000 to less than $150,000; $150,000 or more)
• Age. Please enter your age. Please don’t provide any idenƟfying informaƟon. (open text response)
• Gender. What is your gender idenƟty? (Woman; Man; Non-binary; Prefer not to say)
Debrieﬁng and data-retenƟon consent. ParƟcipants were told: “We want to let you know that some parts of the
study involved simulated scenarios. Speciﬁcally, the network diagram you saw about your [device] was ﬁcƟonal and
not based on actual data from your device. This was done to beƩer understand how people perceive privacy based on
diﬀerent types of informaƟon presentaƟon. If you have any concerns or would prefer that we delete your responses,
you may request that now—your decision will not aﬀect your compensaƟon in any way.” ParƟcipants then selected
either “I want my responses being used for research” or “I DO NOT want my responses being used for research.”
A.4    Qualitative Analysis
We have restructured the qualita Ɵve results sec Ɵon and added more detail about the sub -themes, including how
parƟcipants arrived at their judgments of consistency (SecƟon 5.2.5, Table 7).
A.4.1 Coding procedure for Study 2. For the qualita Ɵve analysis, we followed Braun and Clarke’s six -phase themaƟc
analysis approach [13]. Two researchers ﬁrst familiarized themselves with the open-ended responses by reading
through them independently. They then generated iniƟal codes across the dataset, capturing recurring interpretaƟons
parƟcipants gave for whether the reported data prac Ɵces matched their expecta Ɵons. Codes were collated into
candidate themes, which were reviewed against the coded extracts and the full dataset, reﬁned, and deﬁned. Through
iteraƟve discussion, the researchers consolidated the codes into three primary themes: Data PracƟces Consistent with
ExpectaƟon, Distrust Toward Data Prac Ɵces, and Others, two of which contained interpre Ɵve sub-themes reﬂecƟng
how par Ɵcipants arrived at their judgments. Diﬀerences in coding and interpreta Ɵon were discussed and reﬁned
through consensus.
The ﬁnal codebook resulƟng from this process is presented in Table 9, including the themes and subthemes, their
coding rules, and illustraƟve indicators. Top-level themes were mutually exclusive, whereas subthemes could co-occur
within a response.
Table 9. QualitaƟve codebook for Study 2.
Code Coding rule IllustraƟve
indicator
Data PracƟces
Consistent with
ExpectaƟon
Apply when the parƟcipant’s overall judgment is that the depicted
data pracƟces broadly matched their prior expectaƟons. A
response could also receive one or more of the interpreƟve
subtheme codes below.
“Yes”; “matched
my expectaƟons.”
NormalizaƟon or
pragmaƟc acceptance
Apply when the parƟcipant describes the depicted data sharing as
rouƟne, normal, or unavoidable for smart devices. Consistency
reﬂects resignaƟon or pragmaƟc acceptance rather than approval.
“All smart devices
are using our
data.”
Prior-knowledge
conﬁrmaƟon
Apply when the parƟcipant idenƟﬁes speciﬁc data pracƟces they
already knew about or expected, such as collecƟon of viewing
history, app usage, voice commands, or recordings.
“I was aware it
would collect
viewing history.”

 42 Khatun et al.
Favorable deviaƟon
from expectaƟons
Apply when the parƟcipant reports that the depicted
communicaƟon was lower, less extensive, or less concerning than
expected and expresses relief or reassurance.
“A bit lower than
my expectaƟons.”
Overall consistency with
parƟal surprise
Apply when the parƟcipant gives an overall judgment of
consistency but also idenƟﬁes a parƟcular communicaƟon or
pracƟce that was surprising, concerning, or deserving of greater
transparency or control.
“Somewhat
consistent, but I
was surprised.”
Distrust Toward Data
PracƟces
Apply when the parƟcipant indicates that the depicted pracƟces
did not match their expectaƟons and expresses suspicion,
discomfort, or distrust toward the device’s data handling. A
response could also receive one or more of the subtheme codes
below.
“Not consistent
with my
expectaƟons.”
Volume exceeded
expectaƟons
Apply when the parƟcipant’s distrust focuses on the amount,
frequency, or intensity of communicaƟon shown in the report,
including communicaƟon with adverƟsing-related domains.
“So much data in
the last 10
minutes.”
ConƟnued on next page
Table 9 conƟnued
Code Coding rule IllustraƟve
indicator
ProtecƟon or consent
violated
Apply when the parƟcipant says that the device should have
protected their data, requested permission, or avoided using or
sharing the data without consent.
“I expected to be
asked for
permission.”
Others Apply when the response does not provide a discernible judgment
about the depicted data pracƟces, such as when it is neutral,
unrelated to the report, or indicates no prior expectaƟon. Brief
responses that clearly indicated consistency or inconsistency were
assigned to the corresponding top-level theme but were not
assigned an interpreƟve subtheme.
“I didn’t really
have any
expectaƟons.”
