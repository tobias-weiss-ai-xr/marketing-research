---
title: 'SEO-Based Blog Content Pipeline Automation: Integrating Web Scraping and Generative AI for Digital
  Marketing Efficiency'
url: https://doi.org/10.31316/astro.v4i2.9454
category: ai-marketing
subcategory: empirical
date: 2026-05
venue: APPLIED SCIENCE AND TECHNOLOGY REASERCH JOURNAL
authors:
- Aris Wahyu Murdiyanto
- David Sulistiyantoro
- Mukasi Wahyu Kurniawati
source: openalex-oa
pdf_url: https://journal.upy.ac.id/index.php/ASTRO/article/download/9454/5317
pages: 11
chars: 29171
fetched_at: '2026-11-08T19:19:16+00:00'
kb_version: 1
---

# SEO-Based Blog Content Pipeline Automation: Integrating Web Scraping and Generative AI for Digital Marketing Efficiency

Applied Science and Technology Research Journal  Volume 5 Nomor 1, Mei 2026
e-ISSN : 2963-6698 https://journal.upy.ac.id/index.php/ASTRO/index
41
SEO-Based Blog Content Pipeline Automation:
Integrating Web Scraping and Generative AI for Digital
Marketing Efficiency
Aris Wahyu Murdiyanto*1, David Sulistiyantoro1, Mukasi Wahyu Kurniawati2
1Universitas Jenderal Achmad Yani Yogyakarta
2Universitas Akprind Indonesia
E-mail: *1ariswahyumurdiyanto@gmail.com,2david.unjaya@gmail.com,
3mukasi@akprind.ac.id
Abstract
The consistent production of Search Engine Optimization (SEO) content remains a
crucial challenge in digital marketing due to the inherent inefficiencies of manual workflows. This
study aims to design, develop, and evaluate the technical feasibility of an end-to-end hybrid
content automation pipeline architecture. The proposed system integrates deterministic web
scraping (Selenium and BeautifulSoup) for data acquisition, Generative AI (OpenAI GPT) for
text synthesis and On-Page SEO optimization, the Replicate API for visual asset generation, and
the WordPress REST API for autonomous publication. Employing a Proof of Concept (PoC)
method at Technology Readiness Level (TRL) 3, the system was tested across two scenarios
representing varying Document Object Model (DOM) structural complexities. Empirical results
demonstrate that on websites with standard HTML structures, the system successfully operated
autonomously, improving computational time efficiency by 98.8% (reducing the production cycle
from an estimated 195 minutes to 2.25 minutes per article). The generated content proved to
optimally meet On-Page SEO indicators. However, objective evaluation also revealed technical
vulnerabilities in dynamic websites utilizing Client -Side Rendering (CSR), where static s craper
scripts failed to extract the text payload. This study concludes that integrating generative AI into
the production pipeline offers massive SEO scalability, yet it necessitates a more adaptive data
extraction mechanism to achieve universal system reliability.

Keywords— Content Automation; On-Page SEO; Generative AI; Web Scraping; WordPress API
1. INTRODUCTION
In the contemporary digital era, a platform's visibility on search engines (Search Engine
Optimization/SEO) heavily relies on the continuous production and updating of high -quality
textual content [1]. However, the manual lifecycle of content production —encompassing topic
research, data aggregation, writing, editing, keyword insertion, and publication —is a highly
labor-intensive process prone to time inefficiencies. This scalability limitation remains a primary
hurdle for website owners and digital marketin g practitioners seeking to maintain  information
dominance. Figure 1 illustrates the bottleneck effect occurring in conventional content curation
methods due to high human intervention at every phase.

42

Figure 1. Conceptual Comparison between Conventional Content Curation Workflow
vs. Hybrid Automation Approach
The rapid development of Artificial Intelligence (AI), whose foundations were
comprehensively built through modern computational approaches [7] and classical machine
learning [8], now offers a new paradigm due to the integration of deep learning [10]. Specifically
in the sub-field of Natural Language Processing (NLP), before the current era of giant generative
models, the foundations of NLP evolved from neural modeling for basic text clas sification [22],
automated discourse evaluation [19], and visual-textual understanding [18], to multi-task learning
approaches [21]. This evolution reached its peak through the discovery of the Transformer
architecture [12] and bidirectional pre-training models such as BERT [11], XLNet [20], as well
as the initial iterations of Generative Pre-Training (GPT) [27]. Currently, the presence of cutting-
edge Large Language Models ( LLMs), such as those developed by OpenAI [5], has enabled
machine computation to mo ve toward synthesis and contextual summarization capabilities that
resemble human cognition [6]. Research by Chakraborty and Pagolu [2] proves that these
generative AI models can be effectively utilized to design and optimize SEO parameters in text.
Although the theoretical and functional foundations of each technology have been
validated, a review of the literature (state of the art) reveals a significant research gap. The
majority of previous studies tend to isolate their research focus on a single spatial domain—either
purely on data extraction algorithms or purely on AI -based content generation —without
attempting to integrate them. There is no published architectural model that explores holistic
integration (end-to-end pipeline) between web scraping, LLM processing, visual asset generation,
and automated data injection into Content Management Systems (CMS) like WordPress in a
single autonomous workflow. Additionally, evaluations of the robustness of these automation
scripts when faced with modern website s utilizing Client -Side Rendering (CSR) and dynamic
DOM structures are still rarely discussed. Table 1 summarizes the comparison of previous
research with the proposed framework, indicating that no published architecture has explored an
end-to-end pipeline integration.
Table 1. Matrix of State-of-the-Art Comparison and Research Position (Novelty)
Reference /
Principal
Researcher
Web
Scrapin
g
AI Text
Generatio
n (LLM)
AI Visual
Generatio
n
CMS
Auto-
Integratio
n
Limitations (Gap)
Kumar et al.
(2018) [3]
✓ X X X Focuses only on raw
data extraction
techniques without AI
synthesis.

Applied Science and Technology Research Journal  Volume 5 Nomor 1, Mei 2026
e-ISSN : 2963-6698 https://journal.upy.ac.id/index.php/ASTRO/index
43
Chakrabort
y & Pagolu
(2021) [2]
X ✓ X X No automated data
acquisition module or
autonomous
publication.
Moz (2022)
[1]
X ✓ X X The study is
conceptual/theoretical
, not a functional
system
implementation.
Weninger &
Glance
(2022) [4]
✓ X X X Focuses on web DOM
architecture without
integrating generative
AI processing.
This
Research
✓ ✓ ✓ ✓ Autonomous end-to-
end system (TRL 3)
integrating multiple
APIs up to the
publication stage.

Based on the literature gaps in Table 1, this study aims to design, develop, and evaluate
the technical feasibility of a hybrid content automation pipeline architecture. The proposed system
synergizes deterministic web scraping (Selenium and BeautifulSoup) , Generative AI (OpenAI
and Replicate APIs), and the WordPress REST API into a fully autonomous workflow.
Specifically, this research offers three main contributions to the scientific literature: First,
proposing a multi -API integration framework for On -Page SEO optimization that eliminates
manual intervention; Second, providing an empirical evaluation regarding the leap in
computational time efficiency compared to conventional methods; and Third, presenting a critical
analysis of the vulnerability of stati c scraping methods when dealing with the variability of
Document Object Model (DOM) structures in the modern web ecosystem. This research is also
expected to contribute to strengthening the local technology ecosystem, in line with the fighting
values of General Achmad Yani in building a strong and independent nation.
2. RESEARCH METHOD
2.1. Design and Type of Research
This study utilizes an applied experimental research approach with a prototyping system
development method. The research design focuses on testing a Proof of Concept (PoC) at
Technology Readiness Level (TRL) 3, where algorithm functionality and Application
Programming Interface (API) integration are validated within a laboratory simulation
environment.
2.2. Research Location and Time
Computational experiments, script code development, and system testing were conducted
at the Information Systems Study Program Laboratory, Universitas Jenderal Achmad Yani
Yogyakarta (Unjaya). The implementation of the research and the collection of testing log data
took place during the 2025 research funding period.
2.3. Research Subjects and Testing Scenarios
In the context of developing this automation system, the research subjects are not human
populations, but rather web data corpora and computational performance metric s. A purposive

44
sampling technique was used to determine the system input testing scenarios (keywords/topics).
Two topics were specifically selected to represent different levels of complexity in the Document
Object Model (DOM) of the source sites, namely:
1. Scenario A ("Chatbot AI"): Represents general topics with a probability of source
websites having standard (static) HTML structures.
2. Scenario B ("CX Network"): Represents specific topics with a probability of modern
source websites utilizing Client-Side Rendering (CSR) and dynamic class structures.
2.4. Research Instruments
The instruments used to conduct the experiments , as shown in Table 2 , and collect data
consist of hardware and software libraries:
1. Data Acquisition Module: Google Custom Search API, Selenium library (web browser
automation), and BeautifulSoup (HTML parser).
2. Artificial Intelligence Module: OpenAI API (Transformer -architected GPT model) for
text synthesis and Replicate API for image generation.
3. Distribution Platform & Measurement Tools: Content Management System (CMS)
WordPress, along with its REST API, and the industry-standard SEO plugin (Yoast SEO)
as the instrument for measuring article output quality.
Table 2. Software Instrument Specifications and System Testing Parameters
System
Component
Module / Service
Name
Main Function Key Specifications /
Parameters
Execution
Environment
Python 3.x Core program logic
and API orchestration
Libraries: requests, time,
re, os, io, base64, random
Browser
Automation
Selenium
WebDriver &
BeautifulSoup4
Dynamic web
navigation and HTML
DOM structure
parsing
Headless Chrome, CSS
Selector/XPath extraction
Search Engine Google Custom
Search API
Keyword-based source
URL acquisition
Programmable Search
Engine ID, Filter: (-
categories, -tags)
Language
Model (LLM)
OpenAI API
(Azure/OpenAI)
Data cleaning,
paraphrasing,
translation, and On-
Page SEO
optimization
Model: GPT-3.5-Turbo /
GPT-4, Temperature: 0.7
(optimal for creativity &
accuracy)
Visual
Generative
Model
Replicate API Featured Image
generation
Text-to-Image Model,
Aspect Ratio: 16:9,
Base64 Encoding
Distribution
Platform
WordPress REST
API
Article payload
reception and
autonomous
publication
Authentication:
Application Passwords,
Payload: Title, Content,
Tags, Media

2.5. Data Collection Procedures
System performance data collection was carried out through computational log recording
(time and error message logging) while the system was executed autonomously. The experimental
procedure runs according to the following architectural flow:
1. The system executes a search query via the Google API and compares the URLs with the
log database to prevent duplication (redundancy check).

Applied Science and Technology Research Journal  Volume 5 Nomor 1, Mei 2026
e-ISSN : 2963-6698 https://journal.upy.ac.id/index.php/ASTRO/index
45
2. The scraper script extracts raw text from target URLs and divides it (chunking) to av oid
LLM token limitations.
3. The raw data is sent to the OpenAI API for ad/navigation cleaning, translation,
paraphrasing, and SEO keyword injection. In parallel, the Replicate API processes the
visual prompt to generate a featured image.
4. The fully curated structured data is automatically uploaded to the WordPress CMS. The
system records the total cycle time (execution duration) and captures the SEO score
generated on the target platform.
The computational flow of the proposed automation system is represented through the
UML Activity Diagram in Figure 2. System execution begins with determining a keyword as a
trigger to acquire a list of potential URLs via the Google Custom Search API. The system then
performs a conditional validation (redundancy check) on each URL by matching it against an
internal log file; duplicate URLs will be ignored, while unique URLs will be processed using the
Selenium and BeautifulSoup libraries to extract raw text from the source site's Document Object
Model (DOM). Computational time efficiency in this architecture is achieved through the
implementation of asynchronous processing, where the raw text is sent to the OpenAI API for
cleaning, summarizing, translating, and SEO tag injection, while the title prompt is
simultaneously transmitted to the Replicate API for illustration image generation. After both
external processes are completed, the system synchronizes the optimized text and visual assets
into a unified data package (payload), which is then autonomously sent via the WordPress REST
API to complete the publication cycle.

Figure 2. UML Activity Diagram of the Multi-API-Based Blog Content Pipeline
Automation System

46
2.6. Data Analysis Techniques
Data analysis was pe rformed using quantitative descriptive methods and technical log
analysis.
1. Time Efficiency Analysis: The increase in computational time efficiency is analyzed by
comparing the estimated average manual production time ( Tmanual) with the automated
execution time (Tauto). The efficiency percentage (E) is calculated using the established
formula (1).
𝐸 =
𝑇𝑚𝑎𝑛𝑢𝑎𝑙−𝑇𝑎𝑢𝑡𝑜
𝑇𝑚𝑎𝑛𝑢𝑎𝑙
 x 100%       (1)
2. Quality and Robustness Analysis: Content quality is analyzed qualitatively based on On-
Page SEO parameter indicators (such as keyword density, heading structure, and slug
length) generated by the Yoast SEO plugin. Meanwhile, system robustness is evaluated
through the identification and classification of error messa ges in the failed testing
scenario (Scenario B) to analyze the parser's limitations against dynamic web
applications.
3. RESULTS AND DISCUSSION
3.1. Research Results
Description of Testing Data
The Proof-of-Concept testing was executed using two random keywor d input scenarios
to represent different complexities of data sources. Scenario A used the topic "Chatbot AI"
directed at technology sites with standard HTML structures, while Scenario B used the topic "CX
Network" directed at modern corporate sites. Testi ng was conducted autonomously without
human intervention, from the keyword trigger to the publication endpoint on the WordPress CMS.
Main Data Presentation and Performance Analysis
The main findings showed a significant disparity in results. In Scenario A, the system
successfully executed the entire pipeline perfectly. Empirical evidence of this success is shown
in Figure 3, which displays the WordPress CMS interface where the article draft has been
successfully injected, complete with an optimiz ed title, heading -structured content, and an AI -
generated featured image.

Figure 3. Screenshot of the WordPress Editor Interface Demonstrating the "Chatbot AI"
Article Successfully Generated Autonomously with Supporting Visual Assets
The comparative dat a in Table 3 confirm that the entire process above only takes an
average of 135 seconds, achieving a time efficiency of 98.8% compared to manual methods.
Table 3. Recapitulation of Content Production Time Efficiency Metrics

Applied Science and Technology Research Journal  Volume 5 Nomor 1, Mei 2026
e-ISSN : 2963-6698 https://journal.upy.ac.id/index.php/ASTRO/index
47
Computational Process Stage Estimated Manual Time System Execution Time Efficiency
Data Acquisition and
References
60 minutes 15 seconds 99.6%
Text Synthesis and
Optimization
90 minutes 90 seconds 98.3%
Visual Asset Generation 30 minutes 20 seconds 98.9%
CMS Integration and
Publication
15 minutes 10 seconds 98.9%
Total Cycle Time 195 minutes 135 seconds 98.8%

Regarding the output quality, the article published in Scenario A was recorded to have
optimal On-Page SEO indicators. Based on the Yoast SEO measurement instrument, the article
achieved "Green" (Good) status for parameters including Latent Semantic Indexi ng (LSI)
keyword distribution, hierarchical heading structure (H1-H3), and automated alt-text insertion for
the illustration images generated by the Replicate API.
On-Page SEO Quality Validation
The rapid production quantity is balanced with output quality that meets industry
standards. Analysis using the Yoast SEO instrument on the Scenario A article showed optimal
performance. As visualized in Figure 4, the article achieved a "Green" (Good) indi cator score.
The AI system proved capable of placing focus keywords naturally in the title, URL slug, and
sub-headings, as well as maintaining keyword density below the keyword stuffing threshold. In
terms of output quality, the article published in Scenario A was recorded to have optimal On-Page
SEO indicators. Based on the Yoast SEO measurement instrument, the article achieved a "Green"
(Good) status on the latent semantic indexing parameter, hierarchical heading structure (H1-H3),
and automated alt-text insertion on the illustration image generated by the Replicate API.

Figure 4. Results of On-Page SEO Indicator Analysis Using the Yoast SEO Instrument,
Demonstrating Optimal Scores (Green) for the System's Output Article.

Negative Findings (Objectivity)
Conversely, in Scenario B with the input keyword "CX Network", the system failed to
complete the computational flow. As shown in the execution log in Figure 5, the system
successfully went through the initiation phase and found target URLs via the Google API.
However, the process was terminated during the data acquisition phase.

48

Figure 5. Terminal Execution Log Demonstrating System Failure in Scenario B Due to
Empty Data Payload (NoneType) Resulting from Web Scraping
Analysis of the error message in Figure 5 confirms that the BeautifulSoup library returned
an empty data value (list or None type) when trying to extract target HTML tags (such as <div>
or <p>) from the source site. Consequently, the data payload variable became null and could not
be forwarded to the OpenAI processing module, forcing the system to abort execution to prevent
further errors.
3.2 Discussion
Result Interpretation and Relationship with Literature
The computational success in Scenario A confirms that the multi -API orchestration
(OpenAI, Replicate, and WordPress REST API) is highly feasible for cutting digital content
production bottlenecks. The 98.8% efficiency rate is inseparable from the capabilities of
transformer-architected Large Language Models (LLMs) that process lexical synth esis in
seconds—a cognitive task that takes human editors a long time. This finding empirically supports
and expands upon the research of Chakraborty & Pagolu (2021), which previously stated that AI
could optimize SEO parameters. This research proves that such optimization not only applies at
the text level but can be automated from upstream (search) to downstream (publication).
Conversely, the negative findings in Scenario B provide critical insights regarding the
weaknesses of this system's architecture. Text extraction failure occurred because the target sites
utilize Client -Side Rendering (CSR) and reactive JavaScript frameworks (such as React.js or
Vue.js). The deterministic scraping approach using static CSS Selectors is unable to identify
HTML class names that are obfuscated or dynamically generated when the browser loads. This
functional limitation aligns with the scraper scalability evaluation by Weninger & Glance (2022),
which emphasizes that Document Object Model (DOM) structural variability is an absolute hurdle
for traditional data extraction techniques.
Research Implications
Practically, the results of this study carry significant implications for the digital marketing
industry and information systems management. This hybrid approach allows websi te owners to
scale content production massively with operational costs (API token costs) that are far lower
than those of conventionally employing human resources. Theoretically, this research adds to the
literature regarding the integration of generative artificial intelligence into autonomous software
engineering architectures.
Research Limitations
This research is still at Technology Readiness Level (TRL) 3, so testing was limited to a
laboratory environment with a restricted query sample size. The main limitation lies in the design
of the web scraping module, which is still rigid, making it vulnerable to anomalies in source site
HTML structures. Furthermore, SEO evaluation still relies on On -Page indicators at the time of
publication, without measuring the impact of organic traffic increases longitudinally (time-series).
Recommendations and Follow-up Plans

Applied Science and Technology Research Journal  Volume 5 Nomor 1, Mei 2026
e-ISSN : 2963-6698 https://journal.upy.ac.id/index.php/ASTRO/index
49
Based on the limitations found, the recommendation for the subsequent research roadmap
(towards TRL 5) is to enhance the robustness of the data acquisition module. This can be achieved
by replacing the static HTML parser with a computer vision model (AI-based Computer Vision)
capable of extracting text based on visual layout (visual rendering), rather than merely relying on
the DOM code structure. Further research is also suggested to evaluate Off-Page SEO parameters
(such as click and impression metrics in Google Search Console) after the automated articles are
more than three months old in a real operational environment.
4. CONCLUSION
This study has successfully designed and validated the technical feasibility of a hybrid
content automation pipeline architecture based on Generative AI and web scraping at Technology
Readiness Level (TRL) 3. The proposed multi -API integration—encompassing data acquisition
via Google Search and Selenium, lexical processing via OpenAI, visual generation via Replicate,
and publication via the WordPress REST API —has proven capable of operating autonomously
(end-to-end). In terms of performance, this system off ers a massive leap in scalability, with
computational time efficiency reaching 98.8% compared to manual curation methods, reducing
production time from an estimated 195 minutes to an average of 2.25 minutes per article. The
resulting content output has pro ven to meet the feasibility of industry -standard On-Page SEO
metrics, confirming that generative AI is capable of maintaining the contextual and structural
quality of text. Nevertheless, an objective evaluation found system vulnerability when faced with
Document Object Model (DOM) variability. The deterministic scraper library proved to fail in
extracting data on modern websites that utilize Client-Side Rendering (CSR) with dynamic class
naming. Therefore, recommendations for the next research roadmap are to enhance the robustness
of the data extraction module by implementing visual rendering scraping techniques or Computer
Vision models, as well as conducting longitudinal testing in a real operational environment (TRL
5) to comprehensively measure the impact of Off-Page SEO traffic.
5. ACKNOWLEDGMENT
The authors express their deepest gratitude to Universitas Jenderal Achmad Yani
Yogyakarta for the full facility and funding support for this research through the Collaborative
Research/Fundamental Research scheme for the Fiscal Year 2025, based on the Contract
Agreement Letter Number: SPK/148/LPPMUNJAYA/III/2025.
6. AUTHOR CONTRIBUTIONS
Aris Wahyu Murdiyanto  acted as the principal investigator who conceptualized the
system architecture, developed the software coding, integrated the Application Programming
Interfaces (APIs), and wrote the initial draft of the manuscript. David Sulistiyantoro contributed
to formal analysis related to operational efficiency, conducted cost-benefit comparisons between
manual methods and automation, and validated the economic impact of improved SEO metrics.
Mukasi Wahyu Kurniawati contributed to process flow design (pipeline engine ering), system
robustness evaluation (robustness analysis), output quality control, and performed critical editing
and review of the final manuscript. All authors have read and approved the final version of this
manuscript.
7. SUGGESTIONS

50
Based on the analyti cal findings and identified limitations, suggestions for further
research development are focused on two main aspects. First, to overcome system vulnerability
to HTML class obfuscation on Client-Side Rendering (CSR) based websites, it is recommended
to int egrate an intelligent computer vision -based scraping agent or utilize the extraction
capabilities of multimodal language models (Vision -Language Models) capable of recognizing
content blocks based on visual layout rather than code structure. Second, in line with the research
roadmap towards Technology Readiness Level (TRL) 5, system testing needs to be expanded into
a real operational environment to evaluate SEO effectiveness longitudinally. Future researchers
are recommended to measure the impact of system  implementation on Off -Page SEO metrics,
such as search impression growth, Click -Through Rate (CTR), and verified organic backlink
acquisition through the Google Search Console instrument over a period of at least three to six
months post-publication.
REFERENCES
[1] Moz. SEO Best Practices for AI -Generated Content [Internet]. 2022 [cited 2026 Feb 22].
Available from: https://moz.com/research
[2] Chakraborty A, Pagolu VR. Automated Content Generation and SEO Optim ization Using
AI. J Web Eng. 2021;20(3):345-362.
[3] Kumar R, Singh MP, Kumar P. Web Scraping: A Review on Techniques and Tools. Int J
Adv Res Comput Sci. 2018;9(3):363-371.
[4] Weninger T, Glance N. Evaluating Web Scraping Methods for Large -Scale Content
Extraction. IEEE Trans Web Intell. 2022;18(4):555-70.
[5] OpenAI. GPT -4 Technical Report [Internet]. 2023 [cited 2026 Feb 22]. Available from:
https://arxiv.org/abs/2303.08774
[6] Liu P, Yuan W, Fu J, Jiang Z, H ayashi H, Neubig G. Pre -train, Prompt, and Predict: A
Systematic Survey of Prompting Methods in Natural Language Processing. ACM Comput
Surv. 2023;55(9):1-35.
[7] Russell S, Norvig P. Artificial Intelligence: A Modern Approach. 4th ed. Pearson, 2020.
[8] Mitchell TM. Machine Learning. McGraw-Hill; 1997.
[9] Gupta M, Gupta D. Web Scraping Techniques: A Beginner's Guide to Extracting Data from
the Web. Apress; 2022.
[10] Brownlee J. Deep Learning for Natural Language Processing. Machine Learning Mastery;
2019.
[11] Devlin J, Chang MW, Lee K, Toutanova K. BERT: Pre -training of Deep Bidirectional
Transformers for Language Understanding. Proceedings of NAACL -HLT 2019. Available
from: https://arxiv.org/abs/1810.04805
[12] Le QV. Advancements in Transformer Models for Text Generation and Optimization.
Proceedings of ICML 2020.
[13] Selenium Project. Selenium WebDriver API Guide [Internet]. 2023 [cited 2026 Feb 22].
Available from: https://www.selenium.dev/documentation
[14] Richardson L. BeautifulSoup 4 User Guide [Internet]. 2023 [cited 2026 Feb 22]. Available
from: https://www.crummy.com/software/BeautifulSoup/
[15] WordPress Developers. WordPress REST API Handbook [Internet]. 2023 [cited 2026 Feb
22]. Available from: https://developer.wordpress.org/rest-api/
[16] OpenAI API. Using GPT for Text Processing and Summarization [Internet]. 2023 [cited
2026 Feb 22]. Available from: https://beta.openai.com/docs/

Applied Science and Technology Research Journal  Volume 5 Nomor 1, Mei 2026
e-ISSN : 2963-6698 https://journal.upy.ac.id/index.php/ASTRO/index
51
[17] Google Developers. Custom Search JSON API Guide [Internet]. 2023 [cited 2026 Feb 22].
Available from: https://developers.google.com/custom-search
[18] Li Y, Chen C, Hovy E, Jurafsky D. Visualizing and Understanding Neural Mod els in NLP.
Proceedings of the 16th NAACL-HLT. 2018;1:681-691.
[19] Ren X, Cheng H, He J, Peng J, Sun M. Automated Essay Scoring with Discourse -Aware
Neural Models. Proceedings of the 27th COLING. 2018: 713-722.
[20] Yang Z, Dai Z, Yang Y, Carbonell J, Salakhutdin ov R, Le QV. XLNet: Generalized
Autoregressive Pretraining for Language Understanding. NeurIPS. 2019;32:5753-5763.
[21] Zhang Y, Yang Q. A Survey on Multi-Task Learning. IEEE Transactions on Knowledge and
Data Engineering. 2021;34(12):5586-5609.
[22] Howard J, Rud er S. Universal Language Model Fine -tuning for Text Classification.
Proceedings of the 56th ACL. 2018;1:328-339. [27] Radford A, Narasimhan K, Salimans T,
Sutskever I. Improving Language Understanding by Generative Pre -Training. OpenAI.
2018.
[23] Glez-Peña D,  Lourenço A, López -Fernández H, Reboiro -Jato M, Fdez -Riverola F. Web
scraping technologies in an API world. Briefings in Bioinformatics. 2014;15(5):788-797.
[24] Kumar A, Singh KK, Kumar A. A Survey on Web Scraping Techniques and Tools.
IJARCCE. 2019;8(2):76-81.
[25] Murdiyanto AW, Himawan A. Analysis of Web Scraping Techniques to Get Keywords
Suggestion and Allintitle Automatically from Google Search Engines. Telematika: Jurnal
Telematika dan Teknologi Informasi. 2022;19(1):77-90.
[26] Murdiyanto AW. Decision Support System of Keyword Selection Web Site Using Analytical
Hierarchy Process (AHP) and Simple Additive Weighting (SAW). Compiler. 2021;10(2):71-
78.
[27] Murdiyanto AW. Sistem Rekomendasi Evaluasi Awal Situs Web Secara Otomatis Terhadap
Mesin Pencari. Teknomatika. 2018;10(2):46-55.
