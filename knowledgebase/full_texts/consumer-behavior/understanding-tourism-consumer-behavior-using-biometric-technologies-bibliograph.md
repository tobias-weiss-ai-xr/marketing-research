---
title: 'Understanding tourism consumer behavior using biometric technologies: bibliographic review and
  research agenda'
url: https://doi.org/10.18089/tms.2024si02
category: consumer-behavior
subcategory: review
date: 2024-04
venue: Tourism & Management Studies
authors:
- Universidad Rey Juan Carlos, Facultad de Ciencias de la Economía y de la Empresa, Economía de la Empresa,
  España
- Nuria Ruiz-Lacaci
source: openalex-oa
pdf_url: https://dialnet.unirioja.es/descarga/articulo/9532038.pdf
pages: 18
chars: 87715
fetched_at: '2026-11-08T17:32:27+00:00'
kb_version: 1
---

# Understanding tourism consumer behavior using biometric technologies: bibliographic review and research agenda

Tourism & Management Studies, 20(SI), 2024, 15-32.  https://doi.org/10.18089/tms.2024SI02
15

Understanding tourism consumer behavior using biometric technologies: bibliographic review
and research agenda

Comprensión del comportamiento del consumidor turístico mediante tecnologías biométricas: revisión bibliográfica
y agenda de investigación

Nuria Ruiz-Lacaci
Universidad Rey Juan Carlos, Facultad de Ciencias de la Economía y de la Empresa, Economía de la Empresa, España,
nuria.lacaci@urjc.es

Ana Reyes-Menéndez
Universidad Rey Juan Carlos, Facultad de Ciencias de la Economía y de la Empresa, Economía de la Empresa, España,
ana.reyes@urjc.es

Ana Vico Belmonte
Universidad Rey Juan Carlos, Facultad de Ciencias de la Economía y de la Empresa, Economía de la Empresa, España,
ana.vico@urjc.es

Received: 06.09.2023; Revisions required: 26.01.2024; Accepted: 09.04.2024
Abstract
Recent technological advances, particularly in biometrics, have
significantly impacted  the tourism industry. Amidst the COVID -19
pandemic, these technologies have grown rapidly, posing challenges
and opportunities in utilizing the resulting data. This study aims to
develop a research agenda concerning biometrics in tourism consumer
behavior, detailing what biometric data entails and outlining its diverse
applications. Through a bibliographic review of 422 recent papers,
employing machine learning and artificial intelligence techniques, we
extracted keywords, topics, and frequencies using the  methodological
approach of corpus linguistics and latent Dirichlet allocation algorithm.
The results identified 26 topics, including “KPIs”,” Techniques”,
“Personalization”, “Health”, and “Travel and transport”. Furthermore,
we observed that the COVID -19 pandemic has dramatically impacted
the tourism sector, with “Health” present in four categories. The
practical implications of our study suggest that companies can find the
issues that most concern the tourism consumer in the lines of research
presented in the research agenda, paying particular attention to the
lines developed in the research agenda involving “personalization”,
"travel and transport" and "health".
”Keywords: biometric analysis, corpus linguistics, consumer behavior,
tourism, research agenda.
Resumen
Los recientes avances tecnológicos, especialmente en el campo de la
biometría, han tenido un impacto significativo en la industria turística. En
medio de la pandemia de COVID -19, estas tecnologías han crecido
rápidamente, planteando retos y oportunidades en la utilización de los datos
resultantes. Este estudio pretende desarrollar una agenda de investigación
sobre la biometría en el comportamiento del consumidor turístico, detallando
lo que implican los datos biométricos y esbozando sus diversas aplicaciones.
Mediante una revisión bibliográfica de 422 artículos recientes, empleando
técnicas de aprendizaje automático e inteligencia artificial, extrajimos palabras
clave, temas y frecuencias utilizando el enfoque metodológico de la lingüística
de corpus y el algoritmo de Asignación Latente de Dirichlet. Los resultados
identificaron 26 temas, entre ellos "KPI", "Técnicas", "Personalización", "Salud"
y "Viajes y transporte". Además, observamos que la pandemia COVID-19 ha
tenido un impacto dramático en el sector turístico, con "Salud" presente en
cuatro categorías. Las implicaciones prácticas de nuestro estudio sugieren que
las empresas pueden encontrar los temas que más preocupan al consumidor
turístico en las líneas de inv estigación presentadas en la agenda de
investigación, prestando especial atención a las líneas desarrolladas en la
agenda de investigación que implican "personalización", "viajes y transporte"
y "salud"."
Palabras clave : análisis biométrico, lingüística de corpus,
comportamiento del consumidor, turismo, agenda de investigación.

1. Introduction
The competitiveness of the tourism sector has increased in the 21st century. A key factor that has driven this shift is the digital
revolution (Moutinho et al., 2011; Saura & Bennett, 2019). For instance, in 2019, the annual growth of the tourism sector reached
3.5% for the ninth consecutive year, exceeding the corresponding growth rate of the global economy (2.5%; WTTC, 2022). However,
this growth trend was dramatically disrupted in early 2020 by the COVID-19 pandemic, a worldwide emergency caused by the new
SARS-CoV-2 coronavirus (WHO, 2019). As a result of nationwide lockdowns and travel restrictions, the global touris m industry
declined by 50.4% in 2021. In 2022, the annual growth rate in the tourism industry exceeded 5.8%, and according to recent
estimates, a return to 2019 levels (i.e., 10.3%) can be expected by the end of 2023 (WTTC, 2022).
Despite the gradual globa l recovery, the COVID-19 pandemic has had several lasting effects on the tourism industry (Al-Ababneh
et al., 2022; Devkota et al., 2022) . On the one hand, border closures and restrictions on the movement of tourists have had
devastating economic and social effects on the industry (Unguren & Arslan, 2022;  Machová et al., 2021). On the other hand, the
global crisis caused by the COVID-19 pandemic has considerably accelerated the digitization that had already taken place in recent
years in the tourism sector (Reyes-Menendez et al., 2018).

Ruiz-Lacaci, N., Reyes-Menendéz, A., & Belmonte, A. V. (2024). Tourism & Management Studies, 20(SI), 15-32
16

The trend towards digitization forced com panies to accelerate the development of supporting technologies and to develop new
and innovative strategies to sustain the industry during this difficult period  (Krajčík et al, 2023) . Accordingly, in the wake of the
COVID-19 pandemic and in view of its consequences, digitization is increasingly seen as a transformational opportunity for many
actors in the sector (Sigala, 2020).
Currently, many different biometric analysis techniques are used in the tourism sector, such as: fingerprint analysis —a technique
that scans the surface of an individual's fingers with a scanner (Maltoni et al., 2009); eye tracking, a technique that allow s the
analysis to be performed on a fixation point (position of the user’s gaze); scan path (gaze trajectory); heat maps (areas of interest)
(Shokishalov, 2019).
The International Biometrics Identity Association (IBIA) defines biometric technology as “an automated method that allows the
identification and verification of the identity of a living individual based on physiological characteristics or behavioral types” (IBIA,
2018). More generally, biometric technologies can measure a user’s physical and behavioral characteristics through identifica tion
and authentication  and detect and draw inferences about a user’s personal ity and intentions, among other things (Crampton,
2019). Thus, the overarching goal of biometric analysis is to “mine” all available data about users and their behavior (Zuboff, 2019).
There is a growing interest in biometric technologies as the subject of this research. To highlight this interest, we have followed the
research of Reyes-Menendez et al. (2023) and created Figure 1. In this Figure, we can see the searches carried out worldwide in
the last 5 years with the corresponding search term “biometric technologies” in the category “companies and industries”. The
results of the searches in Google Trends highlight the interest of researchers in a specific topic (Reyes -Menendez et al., 2019).
Companies and professionals use Google Trends to understand search trends related to specific products, services, or topics (Liu et
al., 2021) as it provides a real -time view of the events, news, and topics of public interest that are generating the most search
interest (Jun et al., 2018).

Figure 1 - Evolution of searches for the keyword “biometrics” in Google Trends (accessed on 05 May 2021)

Source: own elaboration

During the COVID -19 pandemic, consumer behavior was investigated extensively using biometric analysis, which can be used to
obtain data unintentionally generated by individuals (Ariely & Berns, 2010; Cascio et al., 2015; Kim et al., 2021). In additi on to its
academic value, this information also has significant practical implications. Specifically, businesses can use an individual’ s data to
understand better  the factors affecting consumer behavior, which helps to understand consumer behavior and needs better .
However, the use of biometric scanning technologies in the tourism sector has yet to be evalua ted thoroughly (Loureiro et al.,
2020), suggesting the urgent need for a comprehensive investigation into the applicability of biometric analysis in researchi ng
tourist behavior. In this framework, this study is proposed as an indispensable tool to tackle the complexities of consumer behavior
in the tourism industry in a post-pandemic and digital transformation context by creating a research agenda, identifying key issues
related to tourism consumer behavior, and examining how biometric analytics technologies can be meaningfully applied to analyze
tourism consumer data.
The remainder of this paper is structured as follows: Section 2 presents the literature review; Section 3 presents the methodology
used to conduct this study; Section 4 presents the main res ults, followed by Section 5 where the discussion and conclusions are
presented.

Ruiz-Lacaci, N., Reyes-Menendéz, A., & Belmonte, A. V. (2024). Tourism & Management Studies, 20(SI), 15-32
17

2. Literature review
Tourism consumer behavior has been investigated extensively in a number of previous studies (e.g., Li et al., 2013; Hultman et al.,
2015; Han, 2021; Chiu & Cho, 2022; Lai et al., 2022). However, as technology advances, there is a need to adopt more sophisticated
methods to understand tourists' emotions and decisions better.
Among the tools we can find to measure the behavior of the tourist consumer are the psychophysiological techniques used to
measure the physiological responses of the human body concerning mental or emotional activity. This includes techniques such as
electroencephalogram (EEG), galvanic skin response (GSR), heart rate, and electrical skin conductance measurement, among
others. These tools are used to understand individuals' emotional and cognitive response s (Boz & Koç, 2022). In addition, we can
find neuromarketing tools, a subset of psychophysiological tools specifically applied in marketing and advertising. These tools help
to understand how the human brain responds to different marketing stimuli. Examples of neuromarketing tools include EEG, eye
tracking, and functional magnetic resonance imaging (fMRI). In tourism, thes e tools can be used to better understand how
consumers respond to tourism destinations, experiences, and promotions (Ali Gaafar & Al-Romeedy, 2022).
On the other hand, biometric tools are a broader range of techniques used to measure and analyze individuals' physical
characteristics or biological behavior s. This includes physiological responses as measured by psychophysiological and
neuromarketing tools and physical characteristics such as fingerprints, facial recognition, and voice recognition, among others. In
the context of tourism and hospitality, biometric tools can be used for customer identification, customer experience analysis, and
service personalization (Babaç & Yüncü, 2022; Neo & Teo, 2022).
Among the studies that explored the use of various biometric analysis techniques, González -Rodríguez et al. (2020) assesse d the
possibility of using facial expressions as an instrument to measure consumer satisfaction in the tourism sector. The research
develops a theoretical model that examines how emotions detected through facial expressions influence customer satisfaction and
uses structural equation modeling to test the hypotheses. The findings show that happiness is the most experienced emotion, and
that both positive and neutral emotions have a positive and significant effect on overall satisfaction, while negative emotions have
a negative and significant impact on overall satisfaction. It also highlights the moderating role of gender in these relationships. The
research concludes that the emotional responses detected by the facial expression recognition device are a good  indicator for
assessing the overall satisfaction derived from the service provided at a heritage tourism site. Similarly, in a study where facial
recognition was used to investigate the spontaneous emotions of tourism consumers, Li et al. (2018) examine the use of
psychophysiological measures in tourism, focusing on the usefulness of methods such as skin conductance (SC) and facial
electromyography (EMG) to track emotional responses to tourism destination advertisements. The results show that, compared to
self-report measures, ps ychophysiological measures can better distinguish between different destination advertisements and
between different dimensions of emotion, which suggests the effectiveness of these biometric techniques in measuring emotional
responses. Similarly, in a rec ent study by Boo and Chua (2022), tourists’ acceptance, attitude, and behavior during check -in at a
hotel were analyzed using facial recognition technology. This research aims to explain how hotel guests in Singapore form attitudes
towards facial recogniti on technology by integrating the Technology Acceptance Model (TAM), privacy calculus theory, and
personal innovativeness. The study considers institutional trust, risk perception, and personal innovativeness. It also seeks to
identify ways to improve the acceptance of this technology in the hospitality industry, especially among the growing population of
millennials and Generation Z, who are digital natives.
One of the most common and widely used biometric analyses in the tourism sector is the eye-tracking biometric analysis technique
(Scott et al., 2017). For example, in a study on different types of eye movements and their relationship with the underlying cognitive
processes in consumer decision -making, van der Lans and Wedel (2017) highlig ht the importance of distinguishing between
different types of eye movements. Furthermore, it points to the potential of eye tracking for understanding and improving
managerial decision -making in various contexts and suggests that eye -movement data can hel p infer the selection rules and
information used by consumers during decision -making, which ma y be crucial for improving the effectiveness of marketing
strategies and business decisions (Lustigova et al., 2021).
Taking a different research direction on eye -tracking biometric analysis technology, Morosan (2018) analyzed how positive and
negative emotions influence travelers’ perceptions of security through an analysis based on equity and emotion theories, and by
using data from 511 US air travelers, found that perceptions of safety and the benefits of disclosure had a major impact on
disclosure, while positive and negative emotions influenced travelers’ perceptions of safety. Zamorano et al. (2020) define t he
concept of a “smart airport” and analyze the acceptance of technologies at such airports, focusing on the ages of passengers and
their relationship with the use of technologies. They propose a model of technology acceptance based on perceived usefulness and
ease of use. The results show that using technology at airports increases passenger satisfaction, and that age is related to

Ruiz-Lacaci, N., Reyes-Menendéz, A., & Belmonte, A. V. (2024). Tourism & Management Studies, 20(SI), 15-32
18

technology acceptance. Higher satisfaction was found among technology users in various processes, supporting the hypothesis that
technology at airports improves passenger satisfaction. Similarly, Ding (2020) investigated the use of eye tracking to study the
effectiveness of emergency evacuation measures, concluding that analyzing the proportion of people following evacuation signals
under various conditions can help suggest improvements in safety design and support computer simulation modeling of crowd
evacuation in places such as airports or hotels.
Furthermore, in a study that combined eye tracking and electroencephalography (EEG), Coba et al. (2020) measured whether
tourists’ emotional and cognitive responses to their travel destinations would be indicative of their subsequent stated
destination preferences. The results of this study revealed that while hotel rating summary statistics initially had a positive
impact on tourists’ rating and choice, their rating and choice behavior was moderated by decision difficulty. Additionally, using
eye tracking, the experimental results confirmed that people spent more time weighing  the pros and cons of choice alternatives.
Similar to previous research on tourist destination preferences, Scott et al. (2020) used eye tracking to understand the mental
processes specific to tourist behavior. Using an innov ative eye -tracking method to measure the relative perceived beauty of
underwater images of the Great Barrier Reef, it was found that beautiful images that are pleasing to the eye attracted more
attention than ugly images. The result of their research prese nts eye tracking as a valuable tool for assessing the beauty of
tourist environments. In line with this research, Bastiaansen et al. (2018) also conducted a neuromarketing study that analyz ed
EEG as a valuable tool for evaluating the effectiveness of desti nation marketing through early emotional responses to images
of the cities of Bruges and Kyoto.
It is also important to note that several of the above -mentioned studies used neuromarketing techniques to investigate the
spontaneous emotions of tourism consu mers, which underlines the relevance of this approach in the analysis of emotional
responses in the tourism sector, as well as the study carried out by De -Frutos-Arranz & López (2022), where through a literature
review he provided an in -depth understanding of how neuromarketing contributes to revealing the implicit emotional responses
of tourists that affect subsequent decision -making. In the same way, Halkiopoulos et al. (2022) aim to demonstrate how
neuromarketing can provide new tools and insights into u nderstanding and improving tourism marketing and consumer behavior
in general. The research seeks to examine how the integration of cognitive and neurocognitive features can contribute to
forecasting consumer behavior and create a knowledge base covering a variety of holiday destinations.
In the pre-pandemic context, the study conducted by Negri et al. (2019) shows that the willingness of the Brazilian people to use
biometric analysis technologies in the airport check-in process is positive in more than 80% of those surveyed.
However, with the outbreak of the COVID-19 pandemic, practices related to biosecurity and the improvement of health and safety
conditions became the salient topic of investigation. Authors such as Amankwah-Amoah (2021) carried out a review in which they
linked airlines to the use of biometrics and proposed the accelerated implementation of biometrics for check -in. Meanwhile, by
using the Technology Acceptance Model (TAM), El Fkharany (2022) analyzed the views of travelers in Egyptian air ports on the use
of biometrics in the post-COVID-19 era and found that they had the highest percentage of positive acceptance.
Similarly, Kim et al. (2021) explored how the frequency of international travel during the COVID -19 pandemic affected
consumers’ biosecurity attitudes. The study proposes a conceptual model based on value -attitude-behavior theory to examine
whether the frequency of international travel affects the COVID -19-related biosecurity behavior of US travelers. Furthermore,
Ivanov et al. (202 0) presented new automation technologies as a key element in the reorganization of the tourism sector and
as an opportunity to mitigate biosecurity threats to customers. Their study reveals that the impact of biosecurity threats, s uch
as COVID -19, and gove rnment actions to curb the spread of viruses will be more severe for TTH (Travel, Tourism, Hospitality)
companies with less or no automation compared to companies with a high level of automation. The study by Ioannou et al.
(2021) develops a measurement sc ale called “Travelers Online Privacy Concerns” (TOPC) and examines its predictive validity in
relation to trust and the intention to disclose four types of personal data: biometric, identifiers, biographical, and behavi oral
data with online travel service providers.
Key papers included in the literature review, including the authors’ names, research titles, methodology, and framework are listed
in Table 1. The table also specifies the main theories and methods used in the reviewed studies.

Ruiz-Lacaci, N., Reyes-Menendéz, A., & Belmonte, A. V. (2024). Tourism & Management Studies, 20(SI), 15-32
19

Table 1 - Major papers included in the literature review

References Title Methodology Framework
Scott et al. (2017) A review of eye-tracking research
in tourism
Systematic quantitative
approach
-
Bastiaansen et al. (2018) My destination in your brain: A
novel neuromarketing approach for
evaluating the effectiveness of
destination marketing
EEG Destination image
Li et al. (2018) Using skin conductance and facial
electromyography to measure
emotional responses to tourism
advertising
Biometrics Emotional responses
Morosan (2018) Information Disclosure to Biometric
E-gates: The roles of Perceived
Security, Benefits, and Emotions
Systematic literature
review
-
Negri et al. (2019) Acceptance of biometric
technology in airport check-in.
Personal interviews -
Coba et al. (2020) Choosing between hotels: Impact of
bimodal rating summary statistics
and maximizing behavioral
tendency
Rank-based conjoint
method
-
Ding (2020) The effectiveness of evacuation
signs in buildings based on eye
tracking experiment
Wearable eye- tracking
devices
-
González-Rodríguez et
al. (2020)
Facial-expression recognition: An
emergent approach to the
measurement of tourist satisfaction
through emotions
Facial expression
recognition
Emotional responses
Ivanov et al. (2020) Biosecurity, automation
technologies and economic
resilience of travel, tourism and
hospitality companies
Literature review -
Scott et al. (2020) Measuring perceived beauty of the
Great Barrier Reef using eye-
tracking technology.
Wearable eye-tracking
devices
-
Zamorano et al. (2020) Smart Airports: Acceptance of
Technology by Passengers.
Personal interviews -
Amankwah-Amoah
(2021)
COVID‐19 pandemic and innovation
activities in the global airline
industry: A review
Literature review -
Ioannou et al. (2021) That’s private! Understanding
travelers’ privacy concerns and
online data disclosure.
Systematic literature
review
Travelers' online privacy
concerns (TOPC)
Kim et al. (2021) Does International Travel Frequency
Affect COVID-19 Biosecurity
Behavior in the United States?
Online survey Value–attitude–
behavior theory
Ali Gaafar & Al-Romeedy
(2022)
Neuromarketing as a Novel Method
to Tourism Destination Marketing:
Evidence from Egypt
Questionnaire -
Boo & Chua (2022) An integrative model of facial
recognition check-in technology
adoption intention: the perspective
of hotel guests in Singapore
Online questionnaire Technology acceptance
model (TAM) and
privacy calculus theory
Boz & Koç (2022) Using Neuromarketing Tools in
Hospitality and Tourism Research
Literature review -

Ruiz-Lacaci, N., Reyes-Menendéz, A., & Belmonte, A. V. (2024). Tourism & Management Studies, 20(SI), 15-32
20

De-Frutos-Arranz &
López (2022)
The State of the Art of Emotional
Advertising in Tourism: A
Neuromarketing Perspective
Bibliometric analysis -
El Fkharany (2022) Applying Biometric Technology for
Enhancing Airports’ Efficiency
during Covid-19 pandemic: A case
study of Egyptian Destination
Questionnaire Technology acceptance
model (TAM)
Halkiopoulos et al.
(2022)
Neuromarketing as an Indicator of
Cognitive Consumer Behavior in
Decision-Making Process of Tourism
destination—An Overview
Literature review -
Neo & Teo (2022) Biometrics in Tourism: Issues and
Challenges
Literature review -
Source: own elaboration
Considering the large number of recent studies published within a short period of time (Paul et al., 2021a; Barari et al., 2021; Knani
et al., 2022; Oliveira et al., 2022), as well as the abundance of previous research on different perspectives, such as the technology
used (Ding, 2020; Scott et al. 2020), the time of collection of tourist data (Li et al., 2018; Ioannou et al., 2021), or the link between
behavior and health (Kim et al., 2021; Kim et al., 2022), it is crucial to thoroughly investigate the use  of biometric analysis in the
research on tourist consumer behavior. To the best of our knowledge, none of the previous studies have attempted to review this
body of work extensively. Accordingly, this study seeks to bridge this gap in the literature with the aim of providing a solid basis for
future research and contributing to the development of more effective strategies for the tourism industry.
To remedy this shortfall, we relied on (Leonidou et al., 2010; Leonidou & Leonidou, 2011; Lim & Buntine, 2016;  Sigala et al., 2021;
Grazziotin et al., 2022; Huang et al., 2023; Mazov & Gureyev, 2023), who conducted a bibliographic review to carry out their
research. We also relied on the research of Paul & Benito (2018), Rosado-Serrano et al. (2018), Chen et al. (2021), and Hassan et al.
(2021), who agreed to identify trends, gaps, or areas for future research to provide a comprehensive and up -to-date overview of
the field of study, and in some cases, a future research agenda to stimulate academic research.
Furthermore, following the work of Al-Nakeeb et al. (2018), Mustak et al. (2021), and Reyes-Menendez et al. (2020), we carried out
a review supported by techniques from artificial intelligence and machine learning.
Using previous research that was based on the analysis of consumer-generated data (Mustak et al., 2021; Reyes- Menéndez et al.,
2020),this study aims to develop a research agenda (Rosado -Serrano et al., 2018) by statistically validating the results using log -
likelihood statistical measures (Minhas & Hussain, 2014; Iyengar, 2012) and mutual information (Wu & Su, 1993; Bouma, 2009).
The main research question addressed in this study is as follows:
RQ1: Is there an association of topics in the corpus of previous research on tourism consumer behavior and biometric analysis that
determines a research agenda for tourism?
3. Methodology
Two sets of analysis algorithms were used to conduct the review, analysis, and detection of connections between the topics in this
study. On the one hand, latent Dirichlet allocation (LDA) topic modeling, one of the most popular topic models first proposed  by
David Blei (2003), was used to detect the most prominent topics in the extracted data for each of the topics and thematic tre nds
by further analyzing co-occurrences between words (Jacobi et al., 2016; Nikolenko et al., 2017). Furthermore, a cluster analysis was
carried out on the corpus of documents to identify keywords and their frequency. In addition, the research agenda (Randha wa et
al., 2016) was validated with log-likelihood statistical measures (Minhas & Hussain, 2014; Iyengar, 2012) and mutual information.
3.1  Data collection
The search terms in this study were identified using the procedure proposed by Mustak et al. (2021); we also consulted the
keywords used in previous bibliographic reviews (Leonidou et al., 2010; Lim & Buntine, 2016). An initial search was performed  in
the entire Web of Science (WoS) database (Vanhala et al., 2020), which guarantees the quality of proceedings and publications by
applying Garfield's law and Bradford's discrete law (Borgman & Furner, 2002; Zhao et al., 2019; Paul et al., 2021a,b) using t he
following terms: “tourism”, “tourism consumer”, “tourism consumer behavior”, “online tourism buy ers”, “eye tracking, “eye -
movement behavior”, “biometric analysis”, “biometric technologies”, “digital technologies”, and “digital environments”. This
allowed us to arrive at the keywords.
In the first phase, a search was carried out that allowed us to ide ntify and download the 20 most cited articles and the 20 most
relevant of each search conducted. According to Vanhala et al. (2020), the number of citations contained in each article is not used

Ruiz-Lacaci, N., Reyes-Menendéz, A., & Belmonte, A. V. (2024). Tourism & Management Studies, 20(SI), 15-32
21

to compare the search results. To identify and determine the keywords for this study, the sets of words that were related to each
other were analyzed based on the search for "Tourism consumer behavior AND biometrics", as shown in Table
Table 2 - Database search details
 Search Terms
Field Tag: Title (TI) TI=(“tourism consumer” AND “biometric analysis” OR “eye tracking”)
TI=(“tourism consumer behavior” AND “digital
environments” OR “digital technologies”)
TI=(“tourism behavioral” AND “eye tracking”)
TI=(“tourism” AND “eye tracking” OR “eye-movement behavior”
OR “biometric analysis” )
TI=(“online tourism buyers” AND “consumer behavior”) TI=(“biometric
technologies” AND “tourism consumer behavior”)

 Source: own elaboration
In order to carry out a review of the literature through bibliographic analysis using automatic and semiautomatic analysis tools and
to determine an appropriate sample size, research works published to date in different subject areas with the same objective as
this research have been considered. The most relevant studies are shown in Table 3 below.
Table 3 - Main contributions and their sample sizes
Authors Method n
Putri et al. (2017) LDA model 100
Radhakrishnan et al. (2017) Text mining, Clusters 627
Huang et al. (2018) Topic modelling, LDA model, STLDA model 160
Mustak et al. (2020) Topic modelling, LDA model, VOSViewer 214
Talafidaryani (2020) Topic modeling, LDA model 191
Vanhala et al. (2020) Topic modeling, Text analysis, STM model 495

Source: own elaboration
As can be seen in Table 3, previous studies used different sample sizes (Putri et al., 2017; Huang et al., 2018; Mustak et al., 2020;
Talafidaryani, 2020). However, it is noteworthy that two of the previous studies employing data-mining techniques (Radhakrishnan
et al., 2017; Vanhala et al., 2020) used samples of 627 and 495 articles, respectively. Accordingly, in line with these two studies, we
collected a sample of 457 articles for our data-mining investigation.
We performed a systematic data filtering and selection process for a more precise data analysis based on several previous studies
(Mustak et al., 2021; Vanhala et al., 2020; Reyes -Menendez et al., 2020). For this purpose, after the initial search, which yielded a
total of 457 articles, a manual cleaning process was performed according to the procedure of Vanhala et al. (2020), where articles
that did not have an abstract (AB), year of publication (PY), and source of information (SO) were excluded, resulting in a total sample
of 422 articles with the metadata of authors, title, keywords, and abstract (Blasco-Arcas et al., 2022).
3.2  Corpus linguistics and latent Dirichlet allocation (LDA) model
The corpus linguistics (CL) methodology combines both quantitative (Jia et al., 2018; Saura et al., 2018) and qualitative approaches
(Baker et al., 2008). To conduct this study, a machine -based technique of the latent Dirichlet allocation (LDA) model was applied
(Reyes-Menéndez et al., 2020).
The goal of the LDA model is to detect how many times a document contains the same word . This model is based on probabilistic
analysis which allows the identification of keywords and topics associated with those keywords (Reyes-Menéndez et al., 2020).

Ruiz-Lacaci, N., Reyes-Menendéz, A., & Belmonte, A. V. (2024). Tourism & Management Studies, 20(SI), 15-32
22

The mathematical model developed in Python allows the establishment of a certain number of topics based on the identified word
clusters (Jia, 2018).
Following the standardized process presented by the LDA model, based on the number of words obtained, including repeated
words and their frequency, a name or label is assigned to each group to identify the topic.
 There are two phases to applying this model: (1) The registration of all the keywords in the document corpus and (2) the
identification of the topics associated with those keywords (Reyes -Menéndez et al., 2020). In the first step, the mathe matical
distribution is calculated to identify the topics objectively (see Equation (1)).

(1)

βi Distribution of word in topic i, K topics altogether
θd Proportion of topics in document d, D documents altogether
zd Topic assignment in document d
zd,n Topic assignment for the nth word in document d, N words altogether
wd Observed words for document d
wd,n The nth word for document d

Following this, the keywords associated with the topics are identified by using Gibbs sampling (see Equation (2); Jia, 2018) in the
MAC version of the Python software LDA 1.0.5.

(2)
4. Results
4.1  Keywords and frequency
A keyword analysis was carried out to identify the most prominent concepts in the corpus (Reyes -Menéndez et al., 2020). One of
the measures used in corpus linguistics is frequency, which establishes the number of times a word is repeated in a text (Bak er,
2006) and thus serves to highlight the importance of certain words according to the number of times they are repeated in a corpus
(McEnery & Hardie, 2013).
In descending order of their occurrence in the analyzed data, the most frequent terms in our data were “information” (404 times),
“tourism” (359 times), “research” (341 times), “online” (309 times), “use” (290 times), “data” (276 times), “biometric” (263 times),
and “technology” (261 times). These results suggest that the analyzed publications focused on the information generated by users
online or on the analysis of data and information provided through biometric technologies; therefore, “online” was the primar y
source of “data”.
4.2  Topics
After considering the most frequently used keywords in the analyzed corpus (see Section 4.1), we proceeded to the analysis of
topics or clusters linking these keywords in our corpus. The groups of words that create the corpus of a document form the topics,
which in turn are made up of their keywords (Reyes-Menéndez et al., 2020). To detect the relevant topics of our analysis, the LDA
model and its equation (1) were used (see Section 3.2).  To measure the thematic correlation and determine the coherence score
of the different topics detected through the measurement of word distances, we  used the topic coherence metric, which allowed
us to evaluate our LDA model. The value obtained for our analysis was 0.45, suggesting a strong correlation between topics (S yed
& Spruit, 2017; Rama-Maneiro et al., 2020).
The results with a coherence score of ~0.46 were considered, resulting in 26 topics that constitute the research agenda of the main
drivers in the field of tourism consumer behavior and biometric analysis technologies.

Ruiz-Lacaci, N., Reyes-Menendéz, A., & Belmonte, A. V. (2024). Tourism & Management Studies, 20(SI), 15-32
23

Of the 26 topics detected, the 7 topics with the highest contribution we re “Variables”, “Healthcare”, “Technology”, “Service”,
“Perception”, “Security”, and “Travel”.
Table 4 below shows the keywords that make up each of the 26 topics identified. To perform the selection of topic names, a
randomized controlled process was carried out by automatically sorting the words into topics and manually defining the topic name
based on these words (Jia, 2018). Following the work of Liu et al. (2017), Jia et al. (2018) and Büschken & Allenby (2020) wh o also
developed their research work based on topic identification using LDA, topics were identified manually as follows: from the list of
words, the first 10 words that could adequately describe the topic were selected from the top 10 words.
This manual definition of topics for identificat ion is a procedure used by authors such as Büschken & Allenby (2016) and Liu et al.
(2017) under the LDA model. The research agenda was then developed using the topics and keywords (see Section 4.3 for further
details).
Table 4 - Topic contribution and keywords of the topics
Topic num Topic tag Keywords Topic contrib.
16 Brand tourism,  app,  destination,  sport,  adoption,  sponsorship,  customer, restaurant, choice 0.74
17 Travel security, factor, participation, sport, passport, airline, error, satisfaction, intention 0.74
23 Preferences purchase, website, perceive, beauty, presence, tourism, product, risk 0.73
24 Credibility shopping, perceive, consumer, engagement, platform, work, relationship, expectation 0.72
18 Privacy security, traveler, travel, group, adoption, intention, avatar, improve, research 0.72
5 Service employee, menu, experience, agent, interaction 0.72
19 Servicescape workload, tourism, travel, saccade, marketing, discrimination, music, biometric 0.72
8 Experience destination, comment, internet, visit, map, device 0.71
3 Variables price, advertisement, review, theme 0.71
1 Information language, disclosure, valence, criterion 0.70
22 Profile viewer, label, dve, woman, scs, website, guide, millennial 0.70
13 Security group, consumer, passport, storytelling, rating, change, innovation, similarity 0.70
6 Analysis Fingerprint, map, fixation, accident 0.69
0 Experience image, brand, staffing, virtual agent 0.68
10 Consumer website, review, information, platform, process, usability, technology 0.66
2 Destination city, recall, preference, vehicle, plan 0.66
25 Lifestyle channel, telecare, landscape, travel, app, telephone, sport, eat 0.66
9 Healthcare telepresence, health, biometric, device 0.64
15 Insight guest, health, consumer, disclosure, group, care, perceive, willingness 0.64
14 Perception country, tourism, affordance, servicescape, customer, image, passport,
marketing
0.60
11 Technology fulfilment, model, trust, recovery 0.59
21 Personalization tourism, experience, satisfaction, customer, flow, patient, tourist, internet,
customize, consumer
0.57
4 Location space, contract, map, device, destination 0.49
7 Mood contradiction, recognition, authority, analyst 0.49
12 Attitude customer, satisfaction, tourism, implementation, task, participant 0.43
20 Measurement rating, testing, image, reputation, passenger, sponsorship, disturbance,
traveler, experience
0.43
Source: own elaboration
For a more visual understanding of the distances between different topics, the map in Figure 2 was created to show the topics and
the distances between them. Closer circles represent associated topics, while unrelated topics appear further apart. The size of the
circles represents the frequency of the topic in the document corpus. In our analysis, the most frequent topics in the corpus  were
17 “Travel”, 19 “Servicescape”, and 25 “Lifestyle”.

Ruiz-Lacaci, N., Reyes-Menendéz, A., & Belmonte, A. V. (2024). Tourism & Management Studies, 20(SI), 15-32
24

Figure 2 - Inter-topic distance map

Source: own elaboration
As can be seen in Figure 2, Topic 25 “Lifestyle” was somewhat isolated from the others in terms of inter -topic distance. The same
applies to Topic 1 “Information”, Topic 9 “Healthcare”, and Topic 12 “Attitude”. Interestingly, Topics 10 “Consumer”, 13 “Security”,
and 22 “Profile” created a single group. Similarly, there was a small distance between Topic 16 “Brand” and Topic 19 “Servicescape”.
While Topic 11 “Technology” was isolated, it was r elatively close to Topics 16 “Brand” and 6 “Analysis”, as well as to Topics 3
“Variables”, 5 “Services”, 14 “Perception”, 17 “Travel”, and 21 “Personalization”.
Based on the themes identified, five categories were created (1) KPIs; (2) Technical; (3) Personalization; (4) Health; (5) Travel and
Transport. Below, we explain which topic corresponds to which category as part of the research agenda.
4.3  Research agenda
Following two previous studies by Ivanov & Webster (2020) and Femenia -Serra et al. (2018), who developed agendas related to
the adoption of technology, namely artificial intelligence (AI) and robotics in (smart) tourism and tourism experiences respectively,
based on studies by Mustak et al. (2021), who developed a research agenda based o n AI in marketing, and in line with De Keyser
et al. (2021), who developed a research agenda related to the use of biometrics by businesses, we have developed an agenda fo r
tourism consumer behavior and biometric analysis in this study.
Based on the studies by De Keyser et al. (2021) and Blasco-Arcas et al. (2022), our agenda (see Table 5) was constructed using the
results obtained in the identification of themes extended by the identification of co-occurrences.
Accordingly, in the “Research direction” column, we list the above-mentioned categories related to the second column, i.e., “Topic
number”, which corresponds to the different numbers assigned to each topic identified with our analysis. Then, in the third column,
we present the “Topic tags” related to  the number. In addition, to facilitate the understanding of the research agenda and its
reading in the table, the “Description” column is included, which refers to this category and the topic tags it contains. Fin ally, and
following the work of De Keyser et al. (2021), the “Research avenues” column shows the research questions suggested for each of
the proposed categories.

Ruiz-Lacaci, N., Reyes-Menendéz, A., & Belmonte, A. V. (2024). Tourism & Management Studies, 20(SI), 15-32
25

Table 5  -  Research agenda

Research
direction
Topic
num.
Topic tag Description Research avenues
KPIs

12
17
20
21
24

Attitude
Travel
Measurement
Personalization
Credibility
Contributions
related to the
different metrics
that can be taken
into account to
measure
consumer
behavior
- What are the most KPIs for tourism industry
gathered with biometric technologies?
- How can biometrics KPIs be incorporated into
a managerial strategy?
- Which KPIs are more numerous: qualitative or
quantitative?
- What model and theoretical framework is it
possible to create based on these KPIs?
Techniques

0
4
6
7
19
Experience
Location
Analysis
Mood
Servicescape
Contributions
related to the
different
techniques that
can be applied to
analyze tourism
consumer
behavior through
biometric analysis
- Which techniques are widely used in biometric
research for tourism?
- Which new technologies can be implemented
in the future?
- How can customers' privacy concerns be
quantified in relation to data collected with
biometrics in tourism?
- Which biometric screening techniques are best
accepted by tourism consumers?
- What is the best way to use biometric data
collected in connection with COVID -19 for
managerial purposes?
- Which of the biometric screening techniques
used in tourism provide the most reliable
results?

Personalization  2
5
10
18
22
Destination
Service
Consumer
Privacy
Profile
Contributions
focused on
exploring
personalized
approaches using
biometric analysis
to tailor
experiences for
tourism
consumers
- How does destination personalization through
biometric analysis influence tourist satisfaction
and loyalty?
- What are the key factors influencing tourist
preferences for personalized services in the
context of biometric analysis?
- How do privacy concerns impact tourist
acceptance and the adoption of personalized
biometric services?
- What are the implications of tourist profile
customization using biometric data for
destination marketing and service delivery?
- How can chatbot -based personalized
interactions enhance tourist experiences and
engagement in biometric -enabled tourism
services?
Health  1
3
9
15
25
Information
Variables
Healthcare
Insight
Lifestyle
Implications and
impact of the
global social and
economic
situation on
tourism
- What biometric health measures for COVID -
19 persist after the pandemic?
- How can the tourist consumer experience be
improved in the context of a global pandemic?
- What are the best practices implemented by
governments to detect symptoms associated
with diseases through biomet ric analysis of
tourists?
- What is the level of tourist concern about
biometrics after the COVID-19 pandemic?
Travel and
transport
8
11
13
14
16
23
Experience
Technology
Security
Perception
Brand
Preferences
Contributions and
future lines of
research related to
travel and means
of transport
- How could the mass transit travel experience
be improved by using biometric technologies?
- What kind of biometric screening is present in
luxury transport?
- What are the constructs for successful
implementation of biometric technologies in
travel and transport?
- What differentiates travel and transport
biometrics from being a luxury or a commodity?
- What is the relationship between the use of tourist
transport and the security perceived by users?
Source: own elaboration

Ruiz-Lacaci, N., Reyes-Menendéz, A., & Belmonte, A. V. (2024). Tourism & Management Studies, 20(SI), 15-32
26

Of the five research directions presented in our research agenda, the first is that of “KPIs”; secondly, we propose research questions
around the research direction related to “Techniques”; the third research direction corresponds to “Personalization”; fourthly, we
formulate research questions related to the research direction of “Health”; finally, we present the research direction of “Travel and
transport”.
5. Discussion and conclusion
Despite the growth of scientific research on biometric analysis and tourism, theoretical studies highlighting the importance of
studying tourism consumer behavior through biometric analysis remain scarce. Therefore, further improving the algorithms and
methods applied to data analysis in this field of study is urgently needed.
To address this research gap and following previously used models such as that of Arbelaitz et al. (2013), where the use of LDA
allowed themes to be extracted from the content of a corpus of a travel website to analyze the interest of tourists, we condu cted
a bibliographic review with machine learning and artificial intelligence techniques.
Similarly, Shen et al. (2016) used this model to extract topics and topic probability distributions from Facebook user comments and
to identify the types of attractions tourists are most interested in. Furthermore, Jiang et al. (2015) analyzed themes in the content
of photos on social networks using an expanded LDA model and provided personalized recommendations to users. Hao et al. (2010)
also proposed a location topic model based on LDA to recommend travel desti nations based on travel intention; in the
aforementioned study, the authors also extracted the topics that characterized a certain location from a large collection of travel
logs.
The results presented in this study can serve as a reference for multidiscip linary companies, whether in the tourism sector or not,
that want to implement marketing strategies that take into account the current tourism landscape.
For example, taking as a reference the first research direction proposed in the research agenda, “KPIs ”, companies can use our
research avenues, such as “What are the most important KPIs for the tourism industry gathered with biometric technologies?”, to
measure the behavior of their consumers.
From a business perspective, the tourism sector experienced co nsiderable growth before the COVID -19 pandemic (WTTC, 2020),
placing it at the top of the list as a high -potential sector for investment, research, development, and innovation strategies. These
data lead us to focus on research directions 1 and 2 of our agenda, “KPIs” and “Techniques” respectively, which, along with t he
proposed research avenues, aim to identify the metrics for measuring co nsumer behavior and also the different techniques that
can be applied to analyze consumer behavior through biometric analysis.
In this sense, and as possible hypotheses derived from the results of this study and presented as research direction 1, “KPIs ”, we
formulate the following proposition:
1. The utilization of biometric analysis technologies in tourism consumer research enhances our understanding of key
performance indicators (KPIs) and informs strategic decision-making processes.
Analyzing ways to personalize offers to tourist consumers is presented as another possible research direction (“Personalization”),
which corresponds to research agenda number 3. Doing so will translate into better user adoption and less effort on the part of
users in the search process. In one relevant study, Lu (2015) developed a thematic Probit-Dirichlet hybrid allocation (PDHA) model
by including temporal features of documents to detect the cyclical dynamics of a topic, thus reflecting user habits with regard to a
particular topic; this information can be used meaningfully to formulate recommendations and personalize products and services
to users in specific contexts. Based on this evidence, and based on the third research direction of “Personalization”, our th ird
proposition can be formulated as follows:
2. Personalization strategies tailored to individual preferences and behaviors contribute to enhanced customer satisfaction and
loyalty in the tourism industry.
Considering that consumer behavior is prone to frequent changes  (Desai & Mahajan, 1998), tourists’ decisions are influenced by
numerous variables. Several authors argue that a tourism consumer is an agent with changing needs and preferences (Chen et al.,
2013; Strömberg et al., 2016). Accordingly, it is essential to identify in a timely manner those topics that are of current interest to
users or that affect them directly due to the current circumstances, such as the outbreak of a pandemic or a natural disaster. In this
sense, and in line with the research direction proposed in our research agenda corresponding to “Health” and Travel and transport”,
we formulate the following proposition:
3. Addressing health considerations, including biosecurity measures and health-related risks, is essential for promoting trust and
confidence among tourists in post-pandemic travel environments.

Ruiz-Lacaci, N., Reyes-Menendéz, A., & Belmonte, A. V. (2024). Tourism & Management Studies, 20(SI), 15-32
27

Furthermore, considering how the changes affect the type of transport used by tourists (Chen et al., 2021; Holmes et al., 2021) and
in line with research direction 5 “Travel and transport”, we formulate the following proposition:
4. Innovations in travel and transport technologies have the potential to transform the tourism landscape, offering new
opportunities to enhance the convenience, safety, and sustainability of travel experiences.
Concerning the research directions of “Travel and transport” and “Health”, including more specifically the issues of security,
technology, or healthcare, airports and directly related companies can benefit from our findings by identifying the issues that most
concern tourism consumers and thus adopt measures and resources in their facilities and services to best meet their clients’ needs
and expectations (Melis et al., 2018). In this domain, adopting new biometric or biosecurity technologies is a central issue (Trip &
Badulescu, 2022).
On the other hand, companies involved in development and innovation can use our results on security and health, privacy, or
personalization issues to develop new products or adapt existing ones. Similarly, tourism and market researchers can benefit from
our findings to start new lines of research or continue our investigation (Lee, 2021).
In summary, all stakeholders in the tourism sector need to be involved to overcome the current crisis and evolve towards a mo re
sustainable model where small businesses in the sector effectively coexist with large tour operators (Sharma et al., 2021).
However, relevant research in this area is limited. Among the few pertinent studies, Ivanov & Umbrello (2021) explored the use of
artificial intelligence and robotic systems in tourism by develo ping a research agenda on the subject. Along similar lines, Chi et al.
(2020) or Loureiro et al. (2020) conducted systematic reviews of the literature on artificial intelligence and proposed a fut ure
research agenda. However, none of the aforementioned studies focused specifically on the use of biometric analysis.
Several other studies, such as Trip & Badulescu (2020), focused on best practices in the use of digital technologies and tour ism
security during COVID -19, presenting biometrics as one of the most important resources employed in the tourism industry.
Acknowledging acceptance of biometric technologies, Norfolk & O'Regan (2020) conducted research on security, safety, and crowd
management at mass events. However, neither of the aforementioned previous studies developed a relevant research agenda.
In contrast to the research by Ioannides & Gyimóthy (2020), Khalid et al. (2021) and Sharma et al. (2021), which focused on tourism
consumer behavior, our research on biometric analysis has led us to obtain data on consumer behavior and consumer identification.
This was not considered in the initial research design stage and opens up future lines of research that could focus on biolog ical
rather than purely tourism behavior.
Future lines of research could be rel ated to automation and robotics, which are becoming increasingly functional in the tourism
sector and directly impact the behavior of the tourist consumer (Knani et al., 2022).
The development of a research agenda based on the identi fied themes further enriches our understanding of the key drivers
shaping future research directions. Drawing on previous studies and extending the identification of themes, our agenda
encompasses five overarching categories: KPIs, Technical, Personalizati on, Health, and Travel and Transport. These categories
provide a structured framework for tackling critical research questions and exploring emerging trends in tourism consumer
behavior and biometric analysis.
In this context, the significance and novelty of this study is that we develop a clear research agenda, combining research directions
that have not been previously analyzed in the field of tourism and biometric analysis.
Only one database, Web of Science (WoS), was considered for the study , and our sample did not include unpublished articles or
other scientific sources. In addition, the documents analyzed depended on the search keywords used. It is recommended that
future research consider additional databases and expand the number of keywords to increase the number of publications.
Nevertheless, the data presented and analyzed here constitute a representative sample that allows for further research on tourism
consumer behavior with a clear framework for future action.
Considering that the behavior of tourism consumers varies according to different contexts and the speed at which technology
evolves, it would be advisable to conduct research similar to ours in order to identify new lines of research in this direction.
In this study, we used machine learning and artificial intelligence techniques to thoroughly review and analyze a total of 42 2
academic papers that use biometric analysis in the tourism sector.
The results of our research allowed us to answer the research question (RQ1: Is there an association of topics in the corpus of
previous research on tourism consumer behavior and biometric analysis that determines a research agenda for tourism?) by finding
26 topics grouped into 5 categories, whic h we have called research directions, resulting in a research agenda (see Table 5).

Ruiz-Lacaci, N., Reyes-Menendéz, A., & Belmonte, A. V. (2024). Tourism & Management Studies, 20(SI), 15-32
28

Additionally, for each of the research directions, we have formulated research avenues for those companies and researchers in the
tourism sector willing to use biometric analysis technologies.
In the context of the recent growth of scientific publications on tourism consumer behavior and biometric analysis, our resul ts
provide compelling evidence that there is a research agenda for tourism consumer behavior that combines biometrics with tourism,
thereby facilitating the further work of researchers and practitioners in this area. Importantly, this study also reveals a s ignificant
connection between biometric screening in tourism and health and safety aspects, especially in the  context of COVID-19. In line
with Trip & Badulescu (2020), who focused their research on the use of digital technologies and tourism security during COVID -19
and presented biometrics as one of the important resources used in the tourism industry, or Norfo lk & O'Regan (2020), who
conducted research on safety, security, and crowd management and acknowledged the acceptance of biometric technologies for
such purposes, our research demonstrates and confirms the importance of the study of biometric technology applied to the tourism
consumer in terms of safety, security, and privacy.
In this respect, new research lines and  avenues are open and should be considered by future researchers and practitioners in
consumer behavior biometrics and tourism.
Similarly, based on the results of our bibliographic review, we developed a statistical measure of coherence, applying machin e
learning and artificial intelligence techniques supported by the statistical measure of coherence. This constitutes the originality and
novelty of this study. Our results revealed that the key categories in the data on tourism consumer behavior and biometric analysis
are “KPIs”, “Techniques”, “Personalization”, “Health”, and “Travel and transport”. Taking into account  the imminent recovery of
the tourism sector after the COVID -19 pandemic (Chang et al., 2020), we can expect considerable growth in the use of biometric
technology in this sector and its application to the behavioral domain in terms of safety, health, and travel and transport.
Credit author statement
Conceptualization, N.R.L, A.R.M and A.V.B.; methodology, N.R.L and A.R.M.; data collection N.R.L.; formal analysis, N.R.L.; writing—
original draft preparation, N.R.L, A.R.M. and A.V.B. ; writing—review and editing, N.R.L. All authors have read and agreed to the
published version of the manuscript.
Declaration of competing interest: None.
References
Al-Ababneh, M. M., Al-Shakhsheer, F. J., Habiballah, M. A., & Al-Badarneh, M. B. (2022). Assessing the ımpact of the COVID-19 pandemic on tourism
workers’ health and well-being in Jordan. Tourism & Management Studies, 18(2), 19-38. https://doi.org/10.18089/tms.2022.180202
Ali Gaafar, H., & Al -Romeedy, B. (2022). Neuromarketing as a novel method to tourism destination marketing: Evidence from Egypt. Journal of
Association of Arab Universities for Tourism and Hospitality, 22(1), 48-74. https://doi.org/10.21608/JAAUTH.2021.109864.1275
Al-Nakeeb, O. A. M. S., & Mufleh, B. A. H. (2018). Collocations and collocational networks of characters: a corpus -based feminist stylistic analysis.
Language in India, 18(9).
Amankwah-Amoah, J. (2021). COVID‐19 pandemic and innovation activities in the global airline industry: A review. Environment International, 156,
106719. https://doi.org/10.1016/j.envint.2021.106719
Arbelaitz, O., Gurrutxaga, I., Lojo, A., Muguerza, J., Pérez, J. M., & Perona, I. (2013). Web usage and content mining to extract knowledge for modelling
the users of the Bidasoa Turismo website and to adapt it. Expert Systems with Applications, 40(18), 7 478-7491.
https://doi.org/10.1016/j.eswa.2013.07.040
Ariely, D., & Berns, G. S. (010). Neuromarketing: the hope and hype of neuroimaging in business. Nature Reviews Neuroscience, 11(4), 284-292.
https://doi.org/doi:10.1038/nrn2795
Babaç, E., & Yüncü, H.R. (2022). Determination of user experience on foodbusiness websites using neuromarketing techniques. Tourism & Management
Studies, 18(3), 49-64. https://doi.org/10.18089/tms.2022.180304
Baker, P. (2006). Glossary of corpus linguistics. Edinburgh: Edinburgh University Press.
Baker, P. (2014). Corpus linguistics in sociolinguistics. Research Methods in Sociolinguistics: A Practical Guide. Hoboken, NJ: Wiley-Blackwell.
Baker, P., Gabrielatos, C., Khosravinik, M., Krzyżanowski, M., McEnery, T., & Wodak, R. (2008). A useful methodological synergy? Combining critical
discourse analysis and corpus linguistics to examine discourses of refugees and asylum seekers in the UK press. Discourse & Society, 19(3), 273-306.
https://doi.org/10.1177/0957926508088962
Barari, M., Ross, M., Thaichon, S., & Surachartkumtonkun, J. (2021). A meta‐analysis of customer engagement behavior. International Journal of
Consumer Studies, 45(4), 457-477. https://doi.org/10.1111/ijcs.12609
Bastiaansen, M., Straatman, S., Driessen, E., Mitas, O., Stekelenburg, J., & Wang, L. (2018). My destination in your brain: A no vel neuromarketing
approach for evaluating the effectiveness of destination marketing. Journal of destination marketing & managemen t, 7, 76 -88.
https://doi.org/10.1016/j.jdmm.2016.09.003
Blasco-Arcas, L., Lee, H. H. M., Kastanakis, M. N., Alcañiz, M., & Reyes-Menendez, A. (2022). The role of consumer data in marketing: A research agenda.
Journal of Business Research, 146, 436-452. https://doi.org/10.1016/j.jbusres.2022.03.054
Blei, D. M., Ng, A. Y., & Jordan, M. I. (2003). Latent dirichlet allocation. The Journal of Machine Learning Research, 3, 993-1022.
Boo, H. C., & Chua, B. L. (2022). An integrative model of facial recognition check-in technology adoption intention: the perspective of hotel guests in
Singapore. International Journal of Contemporary Hospitality Management, 34(11), 4052-4079. https://doi.org/10.1108/IJCHM-12-2021-1471

Ruiz-Lacaci, N., Reyes-Menendéz, A., & Belmonte, A. V. (2024). Tourism & Management Studies, 20(SI), 15-32
29

Borgman, C. L., & Furner, J. (2002). Scholarly communication and bibliometrics. Annual Review of İnformation Science and Technology, 36(1), 2-72.
https://doi.org/10.1002/aris.1440360102
Bouma, G. (2009). Normalized (pointwise) mutual information in collocation extraction. Proceedings of GSCL, Potsdam, Germany, pp. 31-40.
Boz, H., & Koç, E. (2022). Using neuromarketing tools in hospitality and tourism research. In Hakan Boz & Erdogan Koç (Eds.), Advanced research methods
in hospitality and tourism (pp. 87-109). Bingley, UK: Emerald Publishing Limited. https://doi.org/10.1108/978-1-80117-550-020221005
Büschken, J., & Allenby, G. M. (2016). Sentence -based text analysis for customer reviews. Marketing Science , 35(6), 953 -975.
https://doi.org/10.1287/mksc.2016.0993
Büschken, J., & Allenby, G. M. (2020). Imp roving text analysis using sentence conjunctions and punctuation. Marketing Science, 39(4), 727 -742.
https://doi.org/10.1287/mksc.2019.1214
Cascio, C., O'Donnell, M., Tinney, F., Lieberman, M., Taylor, S., Strecher, V., & Falk, E. (2015). Self-affirmation activates brain systems associated with
self-related processing and reward and is reinforced by future orientation . Social Cognitive and Affective Neuroscience , 11(4), 621-629.
https://doi.org/10.1093/scan/nsv136.
Chang, C. L., McAleer, M., & Ramos, V. (2020). A charter for sustainable tourism after COVID -19. Sustainability, 12(9), 3671.
https://doi.org/10.3390/su12093671
Chen, X., Duan, Y., Ali, L., Duan, Y., & Ryu, K. (2021). Understanding consumer travel behavior during covid -19. Sustainability, 13(23), 13330.
https://doi.org/10.3390/su132313330
Chen, Y. Y., Cheng, A. J., & Hsu, W. H. (2013). Travel recommendation by mining people attributes and travel group types from community-contributed
photos. IEEE Transactions on Multimedia, 15(6), 1283-1295. https://doi.org/10.1109/TMM.2013.2265077
Chen, Y., Mandler, T., & Meyer-Waarden, L. (2021). Three decades of research on loyalty programs: A literature review and future research agenda.
Journal of Business Research, 124, 179-197. https://doi.org/10.1016/j.jbusres.2020.11.057
Chi, O. H., Denton, G., & Gursoy, D. (2020). Artificially intelligent device use in service delivery: a systematic review, synthesis, and research agenda.
Journal of Hospitality Marketing & Management, 29(7), 757-786. https://doi.org/10.1080/19368623.2020.1721394
Chiu, W., & Cho, H. (2022). The model of goal-directed behavior in tourism and hospitality: A meta-analytic structural equation modeling approach.
Journal of Travel Research, 61(3), 637-655. https://doi.org/10.1177/0047287521991242
Coba, L., Rook, L., & Zanker, M. (2020). Choosing between hotels: impact of bimodal rating summary statistics and maximizing behavioral tendency.
Information Technology & Tourism, 22(1), 167-186. https://doi.org/10.1007/s40558-019-00156-z
Crampton, Jeremy. (2019). Platform Biometrics. Surveillance & Society, 17, 54-62. https://doi.org/10.24908/ss.v17i1/2.13111
De Keyser, A., Bart, Y., Gu, X., Liu, S. Q., Robinson, S. G., & Kannan, P. K. (2021). Opportunities and challenges of using biometrics for business: Developing
a research agenda. Journal of Business Research, 136, 52-62. https://doi.org/10.1016/j.jbusres.2021.07.028
De-Frutos-Arranz, S., & López, M. F. B. (2022). The state of the art of emotional advertising in tourism: A neuromarketing perspective. Tourism Review
International, 26(2), 139-162. https://doi.org/10.3727/154427221X16317419620246
Desai, K. K., & Mahajan, V. (1998). Strategic role of affect -based attitudes in the acquisition, development, and retention of customers. Journal of
Business Research, 42(3), 309-324. https://doi.org/10.1016/S0148-2963(97)00127-6
Devkota, N., Kmeco, L., Thapa, S., Houška, P., & Paudel, U.R. (2022). Tourists’ perception of travel risk and management in destination amid Covid-19
pandemic: empirical evidence from Nepal. Journal of Tourism and Services, 13(25), 90–119. https://doi.org/10.29036/jots.v13i25.388
Dimanche, F., & Havitz, M. E. (1995). Consumer behavior and tourism: Review and extension of four study areas. Journal of Travel & Tourism Marketing,
3(3), 37-57. https://doi.org/10.1300/J073v03n03_03
Ding, N. (2020). The effectiveness of evacuation signs in buildings based on eye tracking experiment. Natural Hazards , 103, 1201 -1218.
https://doi.org/10.1016/j.jnlssr.2022.11.001
El Fkharany, H. M. (2022). Applying biometric technology for enhancing airports efficiency during Covid-19 pandemic: A case study of Egyptian
destination. The International Journal of Tourism and Hospitality Studies, 3(2), 104-117.
Femenia-Serra, F., & Neuhofer, B. (2018). Smart tourism experiences: Conceptualisation, key dimensions and research agenda. Investigaciones
Regionales-Journal of Regional Research, (42), 129-150.
Gartner (2022). Hype cycle for emerging technologies, 2022. Retrieved online March, 2023 from https://www.gartner.com/en/documents/4016848
González-Rodríguez, M. R., Díaz-Fernández, M. C., & Gómez, C. P. (2020). Facial-expression recognition: an emergent approach to the measurement of
tourist satisfaction through emotions. Telematics and Informatics, 51, 101404. https://doi.org/10.1016/j.tele.2020.101404
Google Trends. 2021. Retrieved 05 May 2021 from www.google.com/trends
Grazziotin, L. S., Klaus, V., & Pereira, A. P. M. (2022). Documentary historical analysis and bibliographic research: study subjects and methodology. Pro-
Posições, 33, e20200141. http://dx.doi.org/10.1590/1980-6248-2020-0141EN
Halkiopoulos, C., Antonopoulou, H., Gkintoni, E., & Aroutzidis, A. (2022). Neuromarketing as an indicator of cognitive consumer behavior in decision-
making process of tourism destination—An overview. In Transcending Borders in Tourism Through Innovation and Cultural Heritage: 8th International
Conference, IACuDiT, Hydra, Greece, 2021 (pp. 679-697). Cham: Springer International Publishing.
Han, H. (2021). Consumer behavior and environmental sustainability in tourism and hospitality: A review of theories, concepts, and latest research.
Journal of Sustainable Tourism, 29(7), 1021-1042. https://doi.org/10.1080/09669582.2021.1903019
Hao, Q., Cai, R., Wang, C., Xiao, R., Yang, J. M., Pang, Y., & Zhang, L. (2010). Equip tourists with knowledge mined from travelogues. In Proceedings of the
19th international conference on World wide web (pp. 401-410). https://doi.org/10.1145/1772690.1772732
Hardaker, C., & McGlashan, M. (2016). “Real men don’t hate women”: Twitter  rape threats and group identity. Journal of Pragmatics, 91, 80 -93.
https://doi.org/10.1016/j.pragma.2015.11.005
Hassan, S. M., Rahman, Z., & Paul, J. (2021). Consumer ethics: A review and research agenda. Psychology & Marketing , 39, 111 -130.
https://doi.org/10.1002/mar.21580
Holmes, M. R., Dodds, R., & Frochot, I. (2021). At home or abroad, does our behavior change? Examining how everyday behavior influences sustainable
travel behavior and tourist clusters. Journal of Travel Research, 60(1), 102-116. https://doi.org/10.1177/0047287519894070

Ruiz-Lacaci, N., Reyes-Menendéz, A., & Belmonte, A. V. (2024). Tourism & Management Studies, 20(SI), 15-32
30

Huang, C., Wang, Q., Yang, D., & Xu, F. (2018). Topic mining of tourist attractions based on a seasonal context aware LDA model. Intelligent Data Analysis,
22(2), 383-405. https://doi.org/10.3233/IDA-173364
Huang, G. I., Karl, M., Wong, I. A., & Law, R. (2023). Tourism destination research from 2000 to 2020: A systematic narrative review in conjunction with
bibliographic mapping analysis. Tourism management, 95, 104686. https://doi.org/10.1016/j.tourman.2022.104686
Hultman, M., Skarmeas, D., Oghazi, P., & Beheshti, H. M. (2015). Achieving tourist loyalty through destination personality, satisfaction, and identification.
Journal of Business Research, 68(11), 2227-2231. https://doi.org/10.1016/j.jbusres.2015.06.002
IBIA (2018). Glossary: Biometrics. Retrieved 02 March 2023 from https://www.ibia.org/biometrics/glossary
Ioannides, D., & Gyimóthy, S. (2020). The COVID-19 crisis as an opportunity for escaping the unsustainable global tourism path. Tourism Geographies,
22(3), 624-632. https://doi.org/10.1080/14616688.2020.1763445
Ioannou, A., Tussyadiah, I., & Miller, G. (2021). That’s private! Understanding travelers’ privacy concerns and online data disclosure. Journal of Travel
Research, 60(7), 1510-1526. https://doi.org/10.1177/0047287520951642
Ivanov, S. H., & Umbrello, S. (2021). The ethics of artificial intelligence and robotisation in tourism and hospitality–a conceptual framework and research
agenda. Journal of Smart Tourism, 1(4), 9-18. https://doi.org/10.52255/smarttourism.2021.1.4.3
Ivanov, S., & Webster, C. (2020). Robots in tourism: A research agenda for tourism economics. Tourism Economics , 26(7), 1065 -1085.
https://doi.org/10.1177/1354816619879583
Ivanov, S., Webster, C., Stoilova, E., & Slobodskoy, D. (2020). Biosecurity, automation t echnologies and economic resilience of travel, tourism and
hospitality companies. Sorarxiv Pap, 1-34. https://doi.org/10.31235/osf.io/2hx6f
Iyengar, S., Sood, G., & Lelkes, Y. (2012). Affect, not ideologya social identity perspective on polarization. Public Opinion Quarterly, 76(3), 405-431.
Jacobi, C., Van Atteveldt, W., & Welbers, K. (2016). Quantitative analysis of large amounts of journalistic texts using topic modelling. Digital Journalism,
4(1), 89-106. https://doi.org/10.1080/21670811.2015.1093271
Jia, S. (S. (2018). Leisure motivation and satisfaction: A text mining of yoga centres, yoga consumers, and their interactions. Sustainability, 10(12), 4458.
https://doi.org/10.3390/su10124458
Jiang, S., Qian, X., Shen, J., Fu, Y., & Mei, T. (2015). Au thor topic model-based collaborative filtering for personalized POI recommendations. IEEE
Transactions on Multimedia, 17(6), 907-918. https://doi.org/10.1109/TMM.2015.2417506
Jun, S. P., Yoo, H. S., & Choi, S. (2018). Ten years of research change using Google Trends: From the perspective of big data utilizations and applications.
Technological Forecasting and Social Change, 130, 69-87. https://doi.org/10.1016/j.techfore.2017.11.009
Khalid, U., Okafor, L. E., & Burzynska, K. (2021). Does the size of the tourism sector influence the economic policy response to the COVID-19 pandemic?.
Current Issues in Tourism, 24(19), 2801-2820. https://doi.org/10.1080/13683500.2021.1874311
Kim, M. J., Bonn, M., & Hall, C. M. (2022). What influences COVID -19 biosecurity behaviour for tourism?. Current İssues in Tourism, 25(1), 21 -27.
https://doi.org/10.1080/13683500.2021.1883558
Kim, M. J., Hall, C. M., & Bonn, M. (2021). Does ınternational travel frequency affect Covid-19 biosecurity behavior in the United States?. International
Journal of Environmental Research and Public Health, 18(8), 4111. https://doi.org/10.3390/ijerph18084111
Knani, M., Echchakoui, S., & Ladhari, R. (2022). Artificial intelligence in tourism and hospitality: Bibliometric analysis and research agenda. International
Journal of Hospitality Management, 107, 103317. https://doi.org/10.1016/j.ijhm.2022.103317
Krajčík, V., Novotný, O., Civelek, M., & Zvolánková, S. S. (2023). Digital literacy and digital transformation activities of service and manufacturing SMEs.
Journal of Tourism and Services, 14(26), 242–262. https://doi.org/10.29036/jots.v14i26.551
Lai, T-C., Hsieh, C-L., & Ku, S.C.S. (2022). The gorgeous brand: understanding consumer’ conspicuous consumption for luxury tourism products. Journal
of Tourism and Services, 24(13), 108-127. https://doi.org/10.29036/jots.v13i24.308
Lee, M. (2021). Evolution of hospitality and tourism technology research from Journal of Hospitality and Tourism Technology: a computer-assisted
qualitative data analysis. Journal of Hospitality and Tourism Technology, 13(1), 62-84. https://doi.org/10.1108/JHTT-10-2020-0276
Leonidou, C. N., & Leonidou, L. C. (2011). Research into environmental marketing/management: a bibliographic analysis. European Journal of Marketing,
45(1/2), 68-103. https://doi.org/10.1108/03090561111095603
Leonidou, L. C., Katsikeas, C. S., & Coudounaris, D. N. (2010). Five decades of business research into exporting: A bibliogra phic analysis. Journal of
International Management, 16(1), 78-91. https://doi.org/10.1016/j.intman.2009.06.001
Li, S., Walters, G.,  Packer, J., & Scott, N. (2018). Using skin conductance and facial electromyography to measure emotional responses to tourism
advertising. Current Issues in Tourism, 21(15), 1761-1783. https://doi.org/10.1080/13683500.2016.1223023
Li, X., Li, X. R., & Huds on, S. (2013). The application of generational theory to tourism consumer behavior: An American perspective. Tourism
Management, 37, 147-164. https://doi.org/10.1016/j.tourman.2013.01.015
Lim, K. W., & Buntine, W. (2016). Bibliographic analysis on research publications using authors, categorical labels and the citation network. Machine
Learning, 103(2), 185-213. https://doi.org/10.1007/s10994-016-5554-z
Liu, Q., Chen, E., Xiong, H., Ge, Y., Li, Z., & Wu, X. (2012). A cocktail approach for travel package recommendation. IEEE Transactions on Knowledge and
Data Engineering, 26(2), 278-293. https://doi.org/10.1109/TKDE.2012.233
Liu, R., An, E., & Zhou, W. (2021). The effect of online search volume on financial performance: Marketing insight from Google trends data of the top
five US technology firms. Journal of Marketing Theory and Practice, 29(4), 423-434. https://doi.org/10.1080/10696679.2020.1867478
Liu, X., Burns, A. C., & Hou, Y. (2017). An investigation of brand -related user-generated content on Twitter. Journal of Advertising, 46(2), 236-247.
https://doi.org/10.1080/00913367.2017.1297273
Loureiro, S. M. C., Guerreiro, J., & Tussyadiah, I. (2020). Artificial intelligence in business: State of the art and future research agenda. Journal of Business
Research, 46(2), 236-247. https://doi.org/10.1080/00913367.2017.1297273
Lu, H. M. (2015). Detecting short -term cyclical topic dynamics in the user -generated content and news. Decision Support Systems , 70, 1 -14.
https://doi.org/10.1016/j.dss.2014.11.006
Lustigova, Z., Jarolímková, L., & Žufan, J. (2021). Evaluation of tourist decision-making process by eye-tracking method – focused on methodology gap
and cross-national comparison. Journal of Tourism and Services, 12(22), 89–104. https://doi.org/10.29036/jots.v12i22.258

Ruiz-Lacaci, N., Reyes-Menendéz, A., & Belmonte, A. V. (2024). Tourism & Management Studies, 20(SI), 15-32
31

Machová, R., Korcsmáros, E., Esseová, M., & Marča, R. (2021). Changing trends of shopping habits and tourism during the second wave of COVID-19 –
ınternational comparison. Journal of Tourism and Services, 12(22), 131–149. https://doi.org/10.29036/jots.v12i22.256
Maltoni, D., Maio, D., Jain, A. K., & Prabhakar, S. (2009). Handbook of fingerprint recognition. Berlin: Springer Science & Business Media.
Mazov, N. A., & Gureyev, V. N. (2023). Open access bibliographic resources for maintaining a bibliographic database of research organization. Scientific
and Technical Information Processing, 50(3), 211-223. https://doi.org/10.3103/S0147688223030115
McEnery, T., & Hardie, A. (2013). The history of corpus linguistics. In The Oxford handbook of the history of linguistics. Oxford: Oxford University Press.
https://doi.org/10.1093/oxfordhb/9780199585847.001.0001
Melis, D. J., Silva, J. M., & Yeun, R. C. (2018). Impact of biometric and anthropometric characteristics of passengers on aircraft safety and performance.
Transport Reviews, 38(5), 602-624. https://doi.org/10.1080/01441647.2017.1396264
Minhas, S., & Hussain, A. (2014). Linguistic correlates of deception in financial text a corpus linguistics based approach. Psychology Review, 19, 307-342.
Morosan, C. (2018). Information disclosure to biometric e-gates: The roles of perceived security, benefits, and emotions. Journal of Travel Research,
57(5), 644-657. https://doi.org/10.1177/0047287517711256
Moutinho, L., Ballantyne, R., & Rate, S. (2011). Consumer behavior in tourism. Strategic Management in Tourism , 2(2), 83-126.
https://doi.org/10.1079/9781845935887.0083
Mustak, M., Salminen, J., Plé, L., & Wirtz, J. (2021). Artificial intelligence in marketing: Topic modeling, scientometric analysis, and research agenda.
Journal of Business Research, 124, 389-404. https://doi.org/10.1016/j.jbusres.2020.10.044
Negri, N. A. R., Borille, G. M. R., & Falcão, V. A. (2019). Acceptance of biometric technology in airport check-in. Journal of Air Transport Management,
81, 101720. https://doi.org/10.1016/j.jairtraman.2019.101720
Neo, H. F., & Teo, C. C. (2022). Biometrics in Tourism: Issues and Challenges . In Handbook of e -Tourism (pp. 1835-1849). Berlin: Springer.
https://doi.org/10.1007/978-3-030-05324-6_137-1
Nikolenko, S. I., Koltcov, S., & Koltsova, O. (2017). Topic modelling for qualitative studies. Journal of Information Science , 43(1), 88 -102.
https://doi.org/10.1177/0165551515617393
Norfolk, L., & O’Regan, M. (2020). Biometric technologies at music festivals: An extended technology acceptance model. Journal of Convention & Event
Tourism, 22(1), 36-60. https://doi.org/10.1080/15470148.2020.1811184
Oliveira, P. M., Guerreiro, J., & Rita, P. (2022). Neuroscience research in consumer behavior: A review and future research agenda. International Journal
of Consumer Studies, 46(5), 2041-2067. https://doi.org/10.1111/ijcs.12800
Paul, J., & Benito, G. R. (2018). A review of research on outward foreign direct investment from emerging countries including China: What do we know?
How do we know? and Where should we be heading? Asia Pacific Business Review, 24(1), 90–115. https://doi.org/10.1080/13602381.2017.1357316
Paul, J., Lim, W. M., O'Cass, A., Hao, A. W., & Bresciani, S. (2021a). Scientific procedures and rationales for systematic literature reviews (SPAR‐4‐SLR).
International Journal of Consumer Studies, 45(4).  https://doi.org/10.1111/ijcs.12695
Paul, J., Merchant, A., Dwivedi, Y. K., & Rose, G. (2021b). Writing an impactful review article: What do we know and what do we need to know?. Journal
of Business Research, 133, 337-340. https://doi.org/10.1016/j.jbusres.2021.05.005
Putri, I. R., & Kusumaningrum, R. (2017). Latent Dirichlet allocation (LDA) for sentiment analysis toward tourism review in Indonesia. Journal of Physics:
Conference Series, Volume 801, International Conference on Computing and Applied Informatics 2016 14–15 December 2016, Medan, Indonesia. IOP
Publishing. https://doi.org/10.1088/1742-6596/801/1/012073
Radhakrishnan, S., Erbis, S., Isaacs, J. A., & Kamarthi, S. (2017). Novel keyword co-occurrence network-based methods to foster systematic reviews of
scientific literature. PloS one, 12(3), e0172778. https://doi.org/10.1371/journal.pone.0172778
Rama-Maneiro, E., Vidal, J. C., & Lama, M. (2020). Collective disambiguation in entity linking based on topic coherence in semantic graphs. Knowledge-
Based Systems, 199, 105967. https://doi.org/10.1016/j.knosys.2020.105967
Randhawa, K., Wilden, R., & Hohberger, J. (2016). A bibliometric review of open innovation: Setting a research agenda. Journal of Product Innovation
Management, 33(6), 750-772. https://doi.org/10.1111/jpim.12312
Reyes-Menendez, A., Palos-Sanchez, P. R., Saura, J. R., & Martin-Velicia, F. (2018). Understanding the influence of wireless communications and Wi-Fi
access on customer loyalty: a behavioral model system. Wireless Communications and Mobile Computing , 3487398.
https://doi.org/10.1155/2018/3487398
Reyes-Menendez, A., Saura, J. R., & Filipe, F. (2019). The importance of behavioral data to identify online fake reviews for touris m businesses: A
systematic review. Peer Journal of Computer Science, 5, e219. https://doi.org/10.7717/peerj-cs.219
Reyes-Menendez, A., Saura, J. R., & Thomas, S. B. (2020). Exploring key indicators of social identity in the #MeToo era: Using discourse analysis in UGC.
International Journal of Information Management, 54, 102129. https://doi.org/10.1016/j.ijinfomgt.2020.102129
Reyes-Menéndez, A., Žiaran, P., Antolín-Prieto, R., & Ruiz-Lacaci, N. (2023). How eye tracking can predict consumer behavior preferences on mobile
devices. Applied Marketing Analytics, 8(3), 239-254.
Rosado-Serrano, A., Paul, J., & Dikova, D. (2018). International franchising: A literature review and research agenda. Journal of Business Research, 85,
238-257. https://doi.org/10.1016/j.jbusres.2017.12.049
Saura, J. R., & Bennett, D. R. (2019). A three -stage method for data text mining: Using UGC in business intelligence analysis. Symmetry, 11(4), 519.
https://doi.org/10.3390/sym11040519
Saura, J. R., Reyes-Menendez, A., & Alvarez-Alonso, C. (2018). Do online comments affect environmental management? Identifying factors related to
environmental management and sustainability of hotels. Sustainability, 10(9), 3016. https://doi.org/10.3390/su10093016
Scott, N., Le, D., Becken, S., & Connolly, R. M. (2020). Measuring perceived beauty of the Great Barrier Reef using eye-tracking technology. Current Issues
in Tourism, 23(20), 2492-2502. https://doi.org/10.1080/13683500.2019.1626812
Scott, N. & Zhang, R . & Le, D . & Moyle, B . (2017). A review of eye -tracking research in tourism. Current Issues in Tourism , 22(10), 1244–1261.
https://doi.org/10.1080/13683500.2017.1367367.
Sharma, G. D., Thomas, A., & Paul, J. (2021). Reviving tourism industry post -COVID-19: A resilience -based framework. Tourism Management
Perspectives, 37, 100786. https://doi.org/10.1016/j.tmp.2020.100786

Ruiz-Lacaci, N., Reyes-Menendéz, A., & Belmonte, A. V. (2024). Tourism & Management Studies, 20(SI), 15-32
32

Shen, J., Deng, C., & Gao, X. (2016). Attraction recommendation: Towards personalized tourism via collective intelligence. Neurocomputing, 173, 789-
798. https://doi.org/10.1016/j.neucom.2015.08.030
Shokishalov, Z. H., & Wang, H. (2019). Applying eye tracking in information security. Procedia Computer Scienc e, 150, 347 -351.
https://doi.org/10.1016/j.procs.2019.02.062
Sigala, M. (2020). Tourism and COVID-19: Impacts and implications for advancing and resetting industry and research. Journal of Business Research, 117,
312-321. https://doi.org/10.1016/j.jbusres.2020.06.015
Sigala, M., Kumar, S., Donthu, N., Sureka, R., & Joshi, Y. (2021). A bibliometric overview of the Journal of Hospitality and Tourism Management: Research
contributions and influence. Journal of Hospitality and Tourism Management, 47, 273-288. https://doi.org/10.1016/j.jhtm.2021.04.005
Strömberg, H., Rexfelt, O., Karlsson, I. M., & Sochor, J. (2016). Trying on change–Trialability as a change moderator for sustainable travel behavior. Travel
Behavior and Society, 4, 60-68. https://doi.org/10.1016/j.tbs.2016.01.002
Syed, S., & Spruit, M. (2017, October). Full-text or abstract? examining topic coherence scores using latent dirichlet allocation. In 2017 IEEE International
conference on data science and advanced analytics (DSAA) (pp. 165-174), Tokyo, Japan. https://doi.org/10.1109/DSAA.2017.61
Talafidaryani, M. (2020). A text mining-based review of the literature on dynamic capabilities perspective in information systems research. Management
Research Review, 44(2), 236-267. https://doi.org/10.1108/MRR-03-2020-0139
Trip, D., & Badulescu, D. (2020). Touchless Tourism: How New Tourism Will Look like. In Griffiths School of Management and IT Annual Conference on
Business, Entrepreneurship and Ethics (pp. 85-100). Berlin: Springer. https://doi.org/10.1007/978-3-030-82755-7_6
Unguren, E., & Arslan, S. (2022). How does COVID-19 fear affect job insecurity and stress for hospitality employees? A moderated mediation model for
age and financial status. Tourism & Management Studies, 18(3), 2022, 7-20. https://doi.org/10.18089/tms.2022.180301
van der Lans, R., & Wedel, M. (2017). Eye movements during search and choice. In Wierenga, B., van der Lans, R. (Eds.), Handbook of Marketing Decision
Models. International Series in Operations Research & Management Science, vol 254. Berlin: Springer, Cham. https://doi.org/10.1007/978-3-319-56941-
3_11
Vanhala, M., Lu, C., Peltonen, J., Sundqvist, S., Nummenmaa, J., & Järvelin, K. (2020). The usage of large data sets in onlin e consumer behavior: A
bibliometric and computational text -mining–driven analysis of previous research. Journal of Business Research , 106, 46 -59.
https://doi.org/10.1016/j.jbusres.2019.09.009
Walters, G., Jiang, Y., & Li, S. (2023). Physiological measurements in hospitality and tourism research: a systematic review and new theoretical directions.
Journal of Hospitality & Tourism Research, 10963480231199990. https://doi.org/10.1177/10963480231199990
World Health Organization (WHO). Coronavirus disease (COVID -19) pandemic . Retrieved 12 March 2023 from
https://www.who.int/emergencies/diseases/novel-coronavirus-2019
World Travel and Tourism Council (2020). Biometrics Importance and Benefits . Retrieved 12 March 2023  from
https://wttc.org/Research/Insights/moduleId/1834/itemId/196/controller/DownloadRequest/action/QuickDownload
World Travel and Tourism Council (2022). Global economic impact trends. Retrieved 12 March 2023 from  https://wttc.org/research/economic-impact
Wu, M. W., & Su, K. Y. (1993, September). Corpus -based automatic compound extraction with mutual information and relative frequency count. In
Proceedings of Rocling VI Computational Linguistics Conference VI (pp. 207-216), Nantou, Taiwan.
Zamorano, M. M., Fernández-Laso, M. C., & de Esteban Curiel, J. (2020). Smart aırports: acceptance of technology by passengers. Cuadernos de Turismo,
(45), 567-570.
Zhao, J., Feng, Q., Wu, P., Warner, J. L., Denny, J. C., & Wei, W. Q. (2019). Using topic modeling via non -negative matrix factorization to identify
relationships between genetic variants and disease phenotypes: A case study of Lipoprotein (a)(LPA). PloS o ne, 14(2), e0212112.
https://doi.org/10.1371/journal.pone.0212112
Zuboff, S. (2019) The age of surveillance capitalism. The fight for a human future at the new frontier of power. New York: Public Affairs.
