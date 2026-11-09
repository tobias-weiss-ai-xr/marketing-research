---
title: 'Voice to Calendar: An End-to-End Voice Reservation System for the Hospitality Industry'
url: https://doi.org/10.5281/zenodo.20807006
category: cx-retail
subcategory: framework
date: 2026-06
venue: Zenodo (CERN European Organization for Nuclear Research)
authors:
- Ali Kerem GÜLER
- Mehmet Göktürk
source: openalex-oa
pdf_url: https://e-arceng.com/index.php/arceng/article/download/79/61
pages: 9
chars: 29126
fetched_at: '2026-11-08T18:11:51+00:00'
kb_version: 1
---

# Voice to Calendar: An End-to-End Voice Reservation System for the Hospitality Industry

ARCENG
INTERNATIONAL JOURNAL OF ARCHITECTURE AND ENGINEERING
ISSN
2822-6895
Year 6 (2026) Vol:6   Issue: 1 Issued in June 2026 www.e-arceng.com

411 411
Article Arrival Date   Article Published Date
27.12.2025         23.06.2026

Voice to Calendar: An End-to-End Voice Reservation System for the Hospitality
Industry

Ali Kerem GÜLER 1, Mehmet GÖKTÜRK2
1 Machine Learning Team Lead, Machine Learning Department, Artificial Intelligence, Orcid:
0000-0003-3405-005X
2 Associate Professor, Department of Computer Engineering, Computer Engineering, Orcid:
0000-0002-8030-8923

Abstract
In the hospitality industry, where digital transformation is accelerating, there is a growing
demand for contactless and intelligent interaction methods that enhance user experience. This
study presents an end -to-end, voice -based, autonomous restaurant res ervation system
integrating the Turyid Loyalty mobile application and the Check and Place table management
platform under Protel A.Ş. The proposed architecture utilizes the OpenAI Whisper model and
the Speech Recognition library for speech recognition. For the semantic understanding process,
it employs a two-stage hybrid Natural Language Processing (NLP) pipeline. In the first stage,
structural irregularities and semantic inconsistencies within the transcribed text are normalized
using the Gemini-1.5-Flash model. In the second stage, the system precisely extracts date, time,
and person count entities using the Gemini -2.0-Flash-Exp model. One of the novel aspects of
this study is the management of temporal ambiguities in natural language. The system converts
relative expressions such as “this evening”, “next Tuesday”, or “New Year's Eve” into standard
ISO format. In cases where contextual cues are missing, it automatically assigns the most
appropriate reservation time using heuristics based on sectoral dynamic s. Designed with a
microservices architecture, this framework automates the reservation process by ensuring
seamless data flow between heterogeneous systems. An average task success rate of 94% and
an average completion time of 8.4 seconds, obtained in tests conducted under real -world
conditions, demonstrate the system's performance and commercial viability. Consequently, this
study demonstrates, through concrete data, the contribution of AI -powered voice assistants to
the omnichannel customer experience by eliminating friction in reservation processes.
Keywords: Voice-based reservation system, Machine Learning, Natural Language Processing,
Large Language Models, OpenAI Whisper, Google Gemini, Speech-to-intent

1. INTRODUCTION
In today's rapidly digitizing world, the proliferation of mobile devices and advancements in
voice assistant technologies (Poushneh, 2021), (Guha et al., 2023) are fundamentally changing
how users interact with services. Particularly in the fast -paced food and beverage sector, the
operational burden and time loss associated with traditional reservation methods such as phone
calls and manual form filling pose significant challenges for businesses and customers. In this

ARCENG
INTERNATIONAL JOURNAL OF ARCHITECTURE AND ENGINEERING
ISSN
2822-6895
Year 6 (2026) Vol:6   Issue: 1 Issued in June 2026 www.e-arceng.com

412 412
context, voice-based reservation infrastructures offer the potential to transform the customer
experience by enabling reservations through natural speech, without the need for complex text
inputs or long waiting times.
Voice-based systems significantly enhance operational efficiency by reducing the traditional
call center load, minimize erroneous data entry, and substantially improve customer satisfaction
through real-time personalization. Furthermore, advanced capabilities such as natural language
intent extraction expand the accessibility of businesses serving the global tourism market and
provide rich semantic content for data -driven decision -making processes. This innovative
technology layer sustainably strengthens th e competitive advantage of restaurant and
hospitality businesses.
The primary objective of this study is to simplify the restaurant reservation process by making
it entirely manageable through voice, thereby enhancing the user experience. To this end, a
scalable and robust infrastructure has been developed, integrating Protel A.Ş.'s Turyid Loyalty
mobile application with the Check and Place table-management platform. Leveraging machine
learning and natural language processing (NLP) techniques, the extraction of intent (date, time,
number of guests) from speech has been automated with high accuracy.
The system records the user's voice request and converts this audio into raw text via OpenAI
Whisper or SpeechRecognition modules. The obtained transcript is then processed by the
Gemini-1.5-Flash model to correct grammar, add punctuation, and complete mis sing words,
thereby enhancing semantic coherence. Subsequently, the revised text is analyzed by the
Gemini-2.0-Flash-Exp model, guided by an optimized prompt, to automatically extract the
necessary reservation parameters: date, time, and number of guests. During this process, natural
language date expressions (e.g., "this evening," "next Tuesday") are converted into the
DD/MM/YYYY format, and times are transformed into the 24 -hour clock, considering
contextual cues. Finally, these extracted parameters are combined with user information (name-
surname, phone number) retrieved from the Loyalty backend, transmitted to the Check and
Place API, and the reservation is saved in the restaurant's calendar.
This article is structured as follows: Section II provides a comprehensive literature review,
illustrating the study's position within relevant academic works. Section III details the system's
architecture, data processing steps, and the methodology employed. Section IV presents the
performance evaluation results. Finally, Section V summarizes the conclusions and outlines
future research directions.

2. LITERATURE REVIEW
Historically, chatbots began with the emergence of the term Chatterbot in 1991, with initial
attempts featuring digitized speech, such as Dr. Sbaitso in 1992. Subsequent developments like
ALICE (1995) and SmarterChild (2001) expanded conversational capabil ities and
demonstrated the potential for providing practical information. In recent years, AI -powered
chatbots have undergone a major transformation with advancements in natural language
processing, machine learning, and deep learning (DL). The emergence o f smart personal
assistants like Apple Siri and Amazon Alexa reflects this trend (Gupta et al., 2024).
In the hospitality sector, virtual assistants and chatbots are increasingly being utilized (Athikkal
and Jen q, 2022) . Examples include Amazon's Alexa for Hospitality (2018) and Google's
addition of hotel-specific features to its Nest Hub (2020). Solutions like HiJiffy's multilingual
virtual assistant and Nomadix's digital concierge Angie have also found their place in t he
industry. These technologies help hotels increase operational efficiency, enhance customer
services, and reduce costs (Britt, 2023). Chatbots specifically automate core operations such as

ARCENG
INTERNATIONAL JOURNAL OF ARCHITECTURE AND ENGINEERING
ISSN
2822-6895
Year 6 (2026) Vol:6   Issue: 1 Issued in June 2026 www.e-arceng.com

413 413
order processing, reservation management, and responses to frequently asked questions
(FAQs).
According to Media Richness Theory (MRT), the richness of communication channels is a
significant factor influencing consumers' perceptions and intentions. Voice assistants are
considered a rich communication channel due to their voice functionalities, nat ural language
processing capabilities, and instant feedback mechanisms. These features evoke a sense of
social presence in users, leading them to interact with devices as they would with humans. A
study by Flavián et al. (2023) demonstrated that voice assistant recommendations are more
effective in influencing consumer behavior compared to online consumer reviews. This effect
occurs through perceived credibility and usefulness. Voice recommendations are perceived as
more credible than text-based ones. Furthermore, this paper indicated that recommendations for
search products are perceived as more credible and effective than those for experience products.
However, voice assistant recommendations also have limitations. Factors such as difficulties in
memory retention (retaining voice information in short-term memory), challenges in comparing
multiple options leading to a higher tendency to accept the first recommendation, can indirectly
limit the amount of information voice assistants provide (Flavián et al., 2023). Additionally, for
some users, data privacy and security concerns remain a significant barrier to the adoption of
virtual assistants (Shafeeg et al., 2023), (Buhalis and Moldavska, 2022).
In areas such as restaurant and appointment scheduling, the foundation of voice-based systems
and chatbots lies in their ability to accurately understand user intent. The AI -powered chatbot
named Genie, developed by Gupta et al. (2024), classified customer queries for order processing
and reservations in the restaurant industry with 88.9% accuracy, using a combination of
Word2Vec and Artificial Neural Networks (ANN). Pathirage et a l. (2023), on the other hand,
developed a RASA NLU-based voice bot system for appointment scheduling and demonstrated
its efficiency in interpreting user intents and retrieving relevant data. These studies emphasize
the critical role of NLP techniques and machine l earning models in transforming complex
natural language requests into structured information.
Existing literature focuses on specific needs such as the role of voice assistants in conveying
sustainability messages (Jiang et al. , 2025), general chatbot applications (Gupta et al. , 2024),
appointment scheduling in specific domains (Pathirage et al. , 2023), and the impact of voice
recommendations on consumer behavior (Flavián et al. , 2023). Most of these studies either
address text-based chatbots or general applications of voice assistants, failing to provide an
integrated and holistic solution for entirely voice -based, end -to-end restaurant reservations.
Specifically, there is a lack of a n approach that automatically extracts necessary reservation
information (e.g., today, next Tuesday) from natural language expressions in a context -aware
manner, and then seamlessly integrates this information with existing hotel/restaurant
infrastructure.
This study aims to address the following shortcomings:
• Presenting a comprehensive architecture that unifies speech -to-text conversion,
text refinement, intent extraction, and reservation scheduling into a single automated
workflow.
• Integrating grammar correction, punctuation addition, and missing word
completion through a Whisper and Gemini LLM chain, thereby eliminating the need for
rule-based parsing. Furthermore, it contributes to semantic -time normalization by
introducing context -aware time mapping (e.g., seven this evening to 19:00) and
intelligent assumptions for ambiguous time expressions.
• Providing a production-ready module beyond conceptual prototypes by ensuring
real-world application integration with the Loyalty backend and Check and Place API

ARCENG
INTERNATIONAL JOURNAL OF ARCHITECTURE AND ENGINEERING
ISSN
2822-6895
Year 6 (2026) Vol:6   Issue: 1 Issued in June 2026 www.e-arceng.com

414 414
through a microservice architecture. The module enhances personalized, frictionless
experiences by automatically retrieving user data (name -surname, phone number) and
combining it with extracted reservation details, thereby simultaneously increasing both
customer satisfaction and operational efficiency.

3. METHODOLOGY
This study presents a voice -based restaurant reservation system that integrates Protel A.Ş.'s
Turyid Loyalty mobile application with the Check and Place table -management platform. The
system aims to automatically extract reservation information from user v oice commands and
save it to the relevant table management system. This section comprehensively explains the
system's end-to-end architecture, which consists of several distinct steps.
3.1. System Architecture and Data Flow
The system architecture comprises three main stages, as illustrated in Figure 1. After the user
logs into the Turyid Loyalty mobile application and selects a preferred restaurant, they submit
their voice request through the voice reservation option. The backend of the Loyalty application
then transmits this voice recording to the voice reservation backend, where reservation
information is extracted from the voice data.

Figure 1. A schematic view of voice reservation methodology concepts.

ARCENG
INTERNATIONAL JOURNAL OF ARCHITECTURE AND ENGINEERING
ISSN
2822-6895
Year 6 (2026) Vol:6   Issue: 1 Issued in June 2026 www.e-arceng.com

415 415
During the voice data processing stage, the .NET backend service transfers the user’s voice
recording (in hex format) and the mode parameter (which specifies the speech-to-text model to
be used) to the Python-based module responsible for extracting reservation information. At this
point, the audio file undergoes format validation. Only 16 -bit PCM WAV files are accepted.
Otherwise, an error is returned for other formats. This pre-check is performed by leveraging the
audio file's header information (WAV/MP4 distinction) and metadata (number of channels, bit
depth, sample rate). The system identifies the audio format by inspecting the signatures at the
beginning of the byte array, returning 'wav', 'mp4', or 'unknown', but only processes the 'wav'
format.
3.2. Speech-to-Text
For the speech-to-text (Bérard et al. 2016 ), (Wang et al., 2020) conversion stage, two distinct
model options are available: the SpeechRecognition API (Zhang, 2017) or the Faster-Whisper
model (Guillaumekln, 2023). The appropriate model is selected based on the mode parameter
specified by the user, and the transcription process is then executed.
When the mode parameter is set to 1, the Google Speech Recognition API is utilized for rapid
transcription. The audio data is converted into a speech_recognition.AudioFile object via an
io.BytesIO stream and then forwarded to the recognition engine. The recognition is performed
in Turkish (tr -TR) using the recognize_google method. SpeechRecognition offers a faster
operational time due to its direct API call mechanism.
When the mode parameter is set to 2, transcription is performed using the Faster -Whisper
model. The model is downloaded from AWS S3 only once and retained in the application's
memory. This approach ensures that the Docker image containing the voice reserva tion
application remains lightweight and reduces subsequent reloading costs. The audio data is
written to a temporary WAV stream, after which the Faster -Whisper model aggregates
transcriptions on a segment -by-segment basis. Post -transcription, expressions enclosed in
parentheses such as [.*] and (.*) are removed from the text. The Whisper model was preferred
in this study due to its offline operational capability.
3.3 Text Refinement and Semantic Analysis
The raw transcript obtained is subjected to a two -stage NLP process to accurately extract
reservation information. This process is carried out using large language models (Imran and N.
Almusharraf, 2024).
The initial transcript is sent to the Gemini -1.5-Flash large language model (Google, 2025). In
this step, the model performs grammar corrections, adds punctuation, and completes missing
words in accordance with Turkish writing, linguistic, and orthographic rules, thereby enhancing
the semantic coherence and readability of the text. The aim of this refinement is to increase the
reliability of information extraction in the subsequent stage.
The refined text is then presented to the Gemini -2.0-Flash-Exp model with a specially
optimized prompt to extract the key parameters required for a reservation (date, time, number
of guests). The model identifies date expressions (e.g., this evening, next Tuesday), context-
sensitive times (e.g., 8 PM), and the number of guests within the text. Specifically, time
expressions are converted into a 24 -hour format, taking into account contextual cues such as
morning or evening (e.g., 7 AM → 07:00, 8 PM → 20:00). If no contextual indicator is present,
times are, by default, assigned an evening (PM) reservation (e.g., 07:00 → 19:00, 10:00 →
22:00).
3.4. Normalization of Natural Dates
If the date information extracted during the intent extraction phase contains relative expressions

ARCENG
INTERNATIONAL JOURNAL OF ARCHITECTURE AND ENGINEERING
ISSN
2822-6895
Year 6 (2026) Vol:6   Issue: 1 Issued in June 2026 www.e-arceng.com

416 416
such as today, tomorrow, or next week, an additional process is applied to convert these
expressions into a precise calendar date. A second Gemini call, using the gemini-2.0-flash-exp
model, calculates and returns the exact date in dd -MM-yyyy format based on the current local
time in Turkey (UTC+03:00). If the date information, although provided to the gemini-2.0-flash
model in datetime format during intent extraction, does not yield a result from this model, a
higher version, the gemini -2.5-flash-preview-05-20 model, is invoked to perform the
calculation in dd-MM-yyyy format. This two-stage approach aims to convert date information
into a calendar date with higher accuracy during the intent extraction phase. The system
automatically updates the year of the converted date to the current year if it is earlier than the
current year, ensuring that the reservation points to a current date.
3.5. Integration and Reservation Management
The extracted date, time, and number of guests information is automatically combined with the
user's name-surname and telephone details retrieved from the Turyid Loyalty backend. All of
this reservation data is then transmitted to the Check and Place API. The Check and Place
system uses this data to automatically record the reservation in the restaurant's digital calendar.
This microservice -based workflow completes the speech -to-text-to-intent-to-calendar
conversion in a contactless and real-time manner, thereby simplifying the user experience and
optimizing business operations.
3.6. Error Management and System Robustness
To enhance the system's robustness and reliability, every critical processing block is enclosed
within try-except structures. Various error codes have been defined, ranging from speech format
validation to speech-to-text conversion, LLM model loading, and information extraction. These
specific error codes are designed to facilitate easy logging and user feedback at the .NET layer.

4. RESEARCH FINDINGS
This section presents the tests conducted and findings obtained to evaluate the performance of
the developed voice -based restaurant reservation system. The evaluation was carried out to
cover the accuracy rates and operational times of the system's different modules.
To analyze the system's performance under real -world conditions, 20 actual reservation voice
recordings, including various noise levels and different speakers' voices, were prepared.
Reservation information (date, time, number of guests) was manually extracted from each voice
recording to create a reference dataset.
Word Error Rate (WER) was calculated to evaluate the performance of the Speech -to-Text
models. For this calculation, manual transcripts of the voice recordings were generated and
compared with the transcripts produced by the models. Furthermore, the accuracy of matching
the date, time, and number of guests information within the model transcripts with the actual
reservation details in the voice recording was measured. The operational time for each model
was also recorded and included in the performance comparison. All obtained results, including
the accuracy rates and operational times of the models, were transferred to Table 1.

Table 1 Accuracy rates and operational times of models across various scenarios.
Model Flow WER
(%)
Date
Accuracy (%)
Time
Accuracy (%)
Guest Count
Accuracy (%)
𝚫 Time
(s)
SpeechRecognition 18.1 %90 %92 %98 1.96

ARCENG
INTERNATIONAL JOURNAL OF ARCHITECTURE AND ENGINEERING
ISSN
2822-6895
Year 6 (2026) Vol:6   Issue: 1 Issued in June 2026 www.e-arceng.com

417 417
Faster-Whisper 18.0 %90 %91 %98 3.75
Gemini-2.0-Flash - %90 %90 %96 0.95
Gemini-2.0-Flash and
Gemini-2.5-flash

-

%85

-

-

0.8
In Table 1, both Google SpeechRecognition and Faster-Whisper models exhibited similar Word
Error Rates (WER) in their speech -to-text conversion performance. The SpeechRecognition
model had a WER of 18.1%, while Faster -Whisper achieved a WER of 18.0%. This indicates
that both models had similar accuracy rates in transcribing reservation-related information from
speech. However, in terms of operational time, the SpeechRecognition model was faster at 1.96
seconds, compared to Faster -Whisper's 3.75 seconds. The main reas on for this is that
SpeechRecognition operates via an API call.
In the LLM layer, the Gemini -2.0-Flash-Exp model was observed to achieve high accuracy
rates in extracting reservation information from the transcript. This evaluation measured how
accurately reservation details were extracted from the transcript text. It was examined whether
the model successfully identified the date, time, and number of guests within the transcript.
This model extracted date information with 90% accuracy, time information with 90%
accuracy, and guest count with 96% accuracy. The informati on extraction time was
approximately 0.95 seconds.
Analysis revealed a 5  percentage point decrease in accuracy (to 85%) when the Gemini -2.0-
Flash and Gemini-2.5-Flash-Preview-05-20 models converted date information within the text
to the day, month, year format. For these intent extraction models, only date accuracy was
evaluated. This is  because at this stage, the model's success in accurately converting natural
language date expressions into calendar data is of paramount importance. This decrease can be
attributed to the varied interpretation of ambiguous expressions such as next week or  next
month in the test samples.
To measure the system's overall task success rate and completion time, a mobile application
was presented to 20 participants, each performing trials for three different scenarios (varying
dates, times, and guest counts). The average completion time and acc uracy of these trials are
presented in Table 1.

Table 2 System evaluation table.
Metric Average
Task success rate %94
Completion time 8.4s
According to Table 2, the system's overall task success rate was determined to be 94%. This
indicates that the system is largely capable of accurately processing users' voice -based
reservation requests. The average completion time for a reservation transaction was measured
at 8.4 seconds. This duration signifies a substantial time saving compared to reservations made
via manual form filling or through call centers. The Whisper and Gemini combination, chosen
as the default solution, demonstrated its potential for improving operational efficiency and user
experience with a total processing time of approximately 5 seconds.

ARCENG
INTERNATIONAL JOURNAL OF ARCHITECTURE AND ENGINEERING
ISSN
2822-6895
Year 6 (2026) Vol:6   Issue: 1 Issued in June 2026 www.e-arceng.com

418 418

5. CONCLUSION AND FUTURE WORKS
This study introduced a voice -based restaurant reservation system designed to transform
reservation processes within the hotel and restaurant sectors. The developed system integrates
Protel A.Ş.'s Turyid Loyalty mobile application with the Check and Place table-management
platform, thereby simplifying the user experience and enhancing operational efficiency. By
combining Speech -to-Text and Natural Language Processing technologies, the system can
automatically extract essential reservation details, such as date, time, and guest count, from user
voice requests with high accuracy.
The research findings demonstrated the practical applicability of the proposed voice -based
reservation system by meeting both accuracy and speed criteria for task completion, achieving
a 94% task success rate and an average completion time of 8.4 seconds with real -world data.
These results clearly indicate the system's potential for improving operational efficiency and
enhancing the user experience.
The developed microservice architecture offers a scalable, maintainable, and easily integrable
structure with existing hotel -restaurant infrastructures. The system provides robust speech -to-
intent conversion even in noisy real -world conditions, ensuring a multichannel and consistent
reservation experience. Its ability to automatically retrieve user data and combine it with
reservation details delivers a personalized and frictionless experience, simultaneously boosting
both customer satisfaction and operatio nal efficiency. This work has contributed a
comprehensive architecture to the literature by integrating fragmented approaches in voice -
based reservations, thereby automating the speech-to-text-to-intent-to-calendar chain from start
to finish.
Future iterations of the system will incorporate a verification loop to enhance data integrity.
After a voice command is processed, the transcribed text and extracted reservation details will
be shown to the user —both visually within the app and audibly vi a Text-to-Speech (TTS). A
multi-modal confirmation mechanism, allowing for either explicit voice approval (e.g.,
semantic confirmation commands) or direct UI interaction will be implemented to ensure
accuracy before finalization. Furthermore, the system wi ll include a feedback workflow that
allows users to correct specific parameters or re -initiate the recording process in case of
discrepancies, thereby establishing a fully interactive and error -resilient user experience.

ARCENG
INTERNATIONAL JOURNAL OF ARCHITECTURE AND ENGINEERING
ISSN
2822-6895
Year 6 (2026) Vol:6   Issue: 1 Issued in June 2026 www.e-arceng.com

419 419
5. REFERENCES
Athikkal, S., & Jenq, J. (2022). Voice chatbot for hospitality. arXiv preprint arXiv:2208.10926.
Bérard, A., Pietquin, O., Servan, C., & Besacier, L. (2016). Listen and translate: A proof of
concept for end-to-end speech-to-text translation. arXiv preprint arXiv:1612.01744.
Britt, P. (2023). Speech technology in travel and hospitality: Voice brings concierge service to
bookings and hotel stays. Speech Technology Magazine, 28(3), 30–32.
Buhalis, D., & Moldavska, I. (2022). Voice assistants in hospitality: Using artificial intelligence
for customer service. Journal of Hospitality and Tourism Technology, 13(3), 386–403.
Flavián, C., Akdim, K., & Casaló, L. V. (2023). Effects of voice assistant recommendations on
consumer behavior. Psychology & Marketing, 40(2), 328–346.
Google. (2024). Gemini. https://gemini.google.com
Guha, A., Bressgott, T., Grewal, D., Mahr, D., Wetzels, M., & Schweiger, E. (2023). How
artificiality and intelligence affect voice assistant evaluations. Journal of the Academy of
Marketing Science, 51(4), 843–866.
Guillaumekln. (2023). faster-whisper: Faster Whisper transcription with CTranslate2 [Software
repository]. GitHub. https://github.com/guillaumekln/faster-whisper
Gupta, M., Dheekonda, V., & Masum, M. (2024). Genie: Enhancing information management
in the restaurant industry through AI -powered chatbot. International Journal of Information
Management Data Insights, 4(2), 100255.
Imran, M., & Almusharraf, N. (2024). Google Gemini as a next generation AI educational tool:
A review of emerging educational technology. Smart Learning Environments, 11(1), Article
22.
Jiang, H. L., Lu, L. H., Yuen, T. W., & Liu, Y. L. (2025). Promoting sustainable hospitality:
Examining the impact of voice assistant recommendations on customer engagement in pre -
travel decision-making: Moderating effects of use purpose and cultural orien tation. Journal of
Hospitality Marketing & Management, 34(1), 1–25.
Pathirage, N. M., Madanayake, N. D., Gunasekara, D. W. W., Bandara, J. M. C. M., & Kumara,
A. P. (2023). Voice -bot for book an appointment. In 2023 International Conference on
Innovations in Info-business and Technology (ICIIT) (pp. 184–189). IEEE.
Poushneh, A. (2021). Humanizing voice assistant: The impact of voice assistant personality on
consumers’ attitudes and behaviors. Journal of Retailing and Consumer Services, 58, 102283.
Shafeeg, A., Shazhaev, I., Mikhaylov, D., Tularov, A., & Shazhaev, I. (2023). Voice assistant
integrated with chat GPT. The Indonesian Journal of Computer Science, 12(1), 189–199.
Wang, C., Tang, Y., Ma, X., Wu, A., Okhonko, D., & Pino, J. (2020). Fairseq S2T: Fast speech-
to-text modeling with fairseq. In Proceedings of the 1st Conference of the Asia-Pacific Chapter
of the Association for Computational Linguistics and the 10th Inter national Joint Conference
on Natural Language Processing: System Demonstrations (pp. 33–39).
Zhang, A. (2017). Speech Recognition (Version 3.11) [Computer software].
https://github.com/Uberi/speech_recognition#readme.
