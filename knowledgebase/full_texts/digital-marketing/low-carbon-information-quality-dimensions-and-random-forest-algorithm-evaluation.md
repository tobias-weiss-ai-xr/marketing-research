---
title: Low-carbon information quality dimensions and random forest algorithm evaluation model in digital
  marketing
url: https://doi.org/10.1038/s41598-024-72910-1
category: digital-marketing
subcategory: theory
date: 2024-09
venue: Scientific Reports
authors:
- Weiji Gao
- Zhihua Ding
- Junyu Lu
source: openalex-oa
pdf_url: https://www.nature.com/articles/s41598-024-72910-1.pdf
pages: 16
chars: 75605
fetched_at: '2026-11-08T17:46:45+00:00'
kb_version: 1
---

# Low-carbon information quality dimensions and random forest algorithm evaluation model in digital marketing

Low-carbon information quality
dimensions and random forest
algorithm evaluation model in
digital marketing
Weiji Gao1,2, Zhihua Ding1, Junyu Lu3 & Yulong Wan2
The growing urgency for low-carbon lifestyles necessitates developing effective strategies to
promote sustainable consumer choices. This study investigates key dimensions of information quality
that shape consumer behavior within digital marketing to achieve this goal. Employing a mixed-
methods approach that integrates grounded theory and machine learning, this study identifies
three core dimensions of low-carbon information quality: matching quality, presentation quality,
and interpretability quality. These dimensions underscore the importance of aligning information
with consumer needs, ensuring clear and accurate presentation, and fostering transparency for
trustworthiness. A Random Forest algorithm-based evaluation model is constructed to assess low-
carbon information quality, demonstrating its effectiveness in identifying high-quality, sustainable
content. This research provides a practical tool for digital marketers to enhance their strategies, raise
consumer awareness of sustainable options, and ultimately contribute to the growth of the low-carbon
consumption market.
Keywords Digital marketing, Low-carbon, Information quality evaluation, Random forest
The escalating challenges of global climate change have led to a growing demand for low-carbon products
and services1. A 2023 World Economic Forum study revealed that over 65% of consumers actively seek low-
carbon offerings2. This trend is further corroborated by the significant sales growth observed in the low-carbon
product lines of companies like Unilever and Nike 3. However, converting this interest into actual low-carbon
consumption is challenging. Research indicates that consumer perceptions of information quality regarding
low-carbon products, particularly in terms of accuracy, credibility, and alignment with their needs, significantly
influence their purchasing decisions 4. Therefore, to effectively guide consumer behavior toward low-carbon
choices, businesses must prioritize the quality of low-carbon information disseminated through their digital
marketing strategies5.
Digital marketing, a crucial promotional strategy for businesses, plays a vital role in promoting low-
carbon consumption6. Companies are increasingly integrating low-carbon elements into these strategies 7. For
example, Patagonia successfully leverages its digital platform to promote environmental awareness and low-
carbon products, achieving positive market responses 8. However, despite growing attention to low-carbon
initiatives, the adoption of low-carbon consumption practices has not increased proportionally9. This disparity
highlights the need for businesses to effectively communicate low-carbon information through their digital
marketing strategies10, optimizing information quality to maximize consumer engagement with low-carbon
consumption11,12.
Previous research on low-carbon information has primarily focused on dissemination methods and consumer
attitudes4. However, limited attention has been given to specific dimensions of low-carbon information quality
and effective evaluation methods, particularly from a consumer-centric perspective 13. This study addresses
this gap by exploring: (1) key dimensions of low-carbon information quality influencing consumer behavior in
digital marketing recommendations; and (2) whether a Random Forest algorithm-based model can effectively
evaluate the quality of low-carbon information in these recommendations.
Drawing upon Information Quality Theory (IQT) 14, this study employs a mixed-methods approach,
integrating grounded theory and machine learning. While IQT provides a valuable framework for understanding
1School of Economics and Management, China University of Mining and Technology, Xuzhou 221116, China.
2Jiangsu Vocational College of Electronic and Information, School of Business, Huai’an 223001, China. 3Shanghai
National Accounting Institute, Shanghai 21000, China. email: runingao@hotmail.com
OPEN
Scientific Reports |        (2024) 14:22416 1| https://doi.org/10.1038/s41598-024-72910-1
www.nature.com/scientificreports

information quality, it requires further contextualization to address the nuances of low-carbon information
within digital marketing15. This research provides a nuanced understanding of low-carbon information quality,
recognizing its potential to motivate low-carbon choices and evoke positive emotions associated with low-
carbon lifestyles 16. Through grounded theory analysis, a low-carbon information quality evaluation model
incorporating multiple features is constructed, and a Random Forest algorithm is employed to train and validate
this model. This research aims to provide digital marketing professionals with a practical tool for identifying and
promoting high-quality low-carbon information, ultimately enhancing campaign effectiveness and maximizing
consumer engagement with low-carbon products and services.
This research contributes to the existing literature by: (1) developing a novel, consumer-centric, low-
carbon information quality evaluation model within the context of digital marketing, encompassing three core
dimensions: matching quality, presentation quality, and interpretability quality; and (2) combining grounded
theory and the Random Forest algorithm to construct a quantifiable model for assessing low-carbon information
quality, analyzing the impact of features on model predictions, and providing practical guidance for enhancing
information quality. This study equips digital marketers with an effective method for identifying and promoting
high-quality low-carbon information, ultimately driving low-carbon consumption and contributing to a low-
carbon economy.
Literature review
Digital marketing
The concept of digital marketing can be traced back to the rise of internet commercialization in the 1990s 17.
Since the mid-2010s, the use of digital technologies for marketing purposes, known as digital marketing,
has experienced rapid growth due to the widespread adoption of mobile internet and smart devices 18. This
growth has attracted significant attention across various industries 19. Digital marketing, emerging alongside
the rapid advancements in internet technology, has revolutionized industries practices by enhancing market
responsiveness and fostering innovation. It empowers industries to expand their market power by reshaping
firm boundaries and significantly improves customer engagement and brand loyalty, leading to increased
sales growth and market share expansion 20,21. These advancements offer companies a sustained competitive
advantage22.
Technological innovation plays a pivotal role in this transformation. Blockchain technology, integrated into
digital marketing management systems, has demonstrated significant improvements in sales efficiency and pre-
sale consultation rates 23. Artificial intelligence (AI), through automated recommendation systems and data
analytics, optimizes marketing strategies, enabling targeted marketing and personalized services24. For instance,
Netflix and Amazon leverage AI to recommend personalized movies and products to users, significantly
enhancing user satisfaction and loyalty 20. Big data analytics empowers businesses to understand customer
needs and market trends better, facilitating more effective marketing decisions 25. Furthermore, the integration
of mobile marketing and augmented reality technologies has significantly influenced consumer purchasing
decisions and shopping experiences26.
Despite these advancements, the adoption of digital marketing presents unique challenges and opportunities
for businesses. Traditional retailers are leveraging digital innovation to reshape customer experiences and
create new business models 27 However, small and medium-sized enterprises (SMEs) often face challenges in
their digital marketing transformation, primarily due to limited funding and skill gaps 28. Moreover, privacy
and transparency concerns within digital marketing are increasingly gaining attention, requiring businesses to
balance commercial interests with social responsibility29.
Consumer behavior occupies a central position within the realm of digital marketing 30. Research indicates
that digital marketing significantly influences consumer purchasing decisions and brand loyalty through
personalized recommendations, social media interactions, and other strategies 31,32. Furthermore, sustainable
and green marketing are emerging as crucial trends in the future of digital marketing. Companies are adopting
green marketing strategies to promote environmentally friendly consumption, enhance brand image, and
demonstrate social responsibility.
Information quality theory
In the digital age, information quality has become a critical factor for organizational decision-making and
operational efficiency across a wide range of businesses33. Information quality encompasses various dimensions,
such as accessibility, accuracy, timeliness, and relevance, which collectively determine whether information
effectively meets user needs34. High-quality information can significantly enhance marketing effectiveness and
strengthen consumer trust 35. A direct relationship exists between the accuracy and reliability of information
content and its overall quality, emphasizing the importance of reliable information in influencing consumer
decisions36. Effective information facilitates a deeper understanding of and response to information consumers’
needs, ultimately enhancing their consumption experience 37. Moreover, timeliness plays a crucial role in
influencing information quality38.
Assessing information quality requires establishing a multi-dimensional framework that comprehensively
considers dimensions such as accuracy, completeness, and timeliness 34. A combination of qualitative and
quantitative methods, including questionnaires, expert reviews, and data analysis, can be employed to
comprehensively evaluate information quality 39. For instance, a mixed-methods approach, involving the
definition of assessment objectives, identification of organization-specific needs, selection of relevant activities,
and configuration of these activities to create an evaluation framework aligned with organizational requirements,
can effectively assess information quality40.
The importance of information quality extends across various application domains, each presenting specific
needs and challenges. Brand awareness plays a complex role in online knowledge services, impacting consumer
Scientific Reports |        (2024) 14:22416 2| https://doi.org/10.1038/s41598-024-72910-1
www.nature.com/scientificreports/

repurchase intention and offering strategic insights for online service providers41. A model and methodological
framework have been proposed to ensure information quality in web-based information systems, emphasizing
its critical role in the accurate dissemination of web content42. Information quality strategies can effectively guide
organizations navigating digital transformation, as demonstrated in the context of military organizations 43.
The impact of tracking information quality on customer loyalty has been investigated within the B2B logistics
domain44.
High-quality information plays a crucial role in digital marketing, significantly enhancing the effectiveness
of digital marketing campaigns, including brand awareness, user engagement, and conversion rates 22,45. High-
quality information directly influences user trust and purchase decisions, underlining its significance in digital
marketing strategies. In the context of sustainable development, the quality of corporate carbon information
disclosure is paramount. Information quality can act as an effective technological intermediary, enabling
businesses to fully realize their social value and contribute to the low-carbon economy29,46.
Despite extensive research on information quality, exploring various dimensions, assessment methods,
influencing factors, and applications, most studies focus on general principles and dimensions 33. Limited
attention has been given to the specific characteristics of low-carbon information in digital marketing.
Information Quality Theory (IQT), while providing a valuable framework for understanding information
quality, lacks the granularity to address the nuanced needs of users seeking information related to sustainable
products and services 47. Moreover, existing research on low-carbon information predominantly focuses on
corporate disclosure practices and their impact on firm value, neglecting the crucial role of consumer-oriented
information in promoting low-carbon consumption46. This study seeks to bridge the gap by developing a novel
consumer-centric framework for evaluating the quality of low-carbon information specifically tailored to the
digital marketing context.
Methods and materials
Research method
This research employs a mixed-methods approach, integrating qualitative and quantitative research methods,
to comprehensively explore the dimensions of low-carbon information quality and develop a corresponding
evaluation model. This approach aims to provide both a theoretical foundation and practical tool for enhancing
the effectiveness of low-carbon information dissemination.
Firstly, this research employs the qualitative research method of Grounded Theory (GT) to construct
a dimensional model of low-carbon information quality within the context of digital marketing. Taking the
perspective of low-carbon consumers, Grounded Theory is particularly suitable as it allows for the development
of new theoretical concepts and models from raw data48. The research aims to gather subjective perspectives and
experiences from various stakeholders through in-depth interviews with digital marketing practitioners, low-
carbon experts, and general consumers, leading to a comprehensive understanding of the factors influencing
low-carbon information quality. The GT analysis will follow a three-stage coding procedure:
• Open Coding: The interview data will be analyzed line-by-line to identify and extract initial concepts and
categories related to low-carbon information quality.
• Axial Coding: Through methods such as cluster analysis, the concepts and categories derived from open cod-
ing will be integrated and categorized into higher-level themes and dimensions.
• Selective Coding: From the results of axial coding, the core categories will be selected to construct the low-car-
bon information quality dimension model, explaining the relationships between different dimensions.
Secondly, based on the findings of the GT analysis, the research will utilize the Random Forest algorithm to
construct a low-carbon information quality evaluation model and validate it using real-world data. The Random
Forest algorithm is chosen for its suitability in handling multi-dimensional data, preventing overfitting, and
identifying key features49. The application of the Random Forest algorithm will involve the following steps:
Feature Extraction: Based on the dimension model established through GT, relevant low-carbon information
data will be acquired for the experimental study. Textual and multimedia features describing content quality will
be extracted as input for the quantitative evaluation model.
• Training Data Labeling: Experts and experimental subjects will annotate the data to construct a low-carbon
information dataset with labeled samples. Dimensions from the theoretical model will be transformed into
target variables for supervised learning.
• Random Forest Model Training: The extracted features and labeled data will be used to train the Random
Forest regression model. Hyperparameter tuning will be employed to optimize model performance.
• Model Evaluation: The predictive performance of the trained Random Forest model will be assessed on a
test dataset using evaluation metrics such as accuracy, recall, and F1-score. The results will shed light on the
effectiveness of this model in evaluating low-carbon information quality.
By combining Grounded Theory and the Random Forest algorithm, this research aims to develop a low-carbon
information quality evaluation system that is both theoretically sound and practically applicable. This approach
provides a theoretical basis and technical support for enhancing the effectiveness of low-carbon information
dissemination, while offering a novel mixed-methods approach to the research field.
All methods were conducted in accordance with relevant guidelines and regulations.
Scientific Reports |        (2024) 14:22416 3| https://doi.org/10.1038/s41598-024-72910-1
www.nature.com/scientificreports/

Ethical approval
The research design and interview protocol were approved by the Institutional Review Board (IRB) of China
University of Mining and Technology. Participants were fully informed of the study procedures and provided
written informed consent.
Consent to participate
Informed consent was obtained from all individual participants included in the study.
Materials
This study utilizes both qualitative and quantitative data. The following section outlines the rigorous adherence
to relevant norms and standards throughout the data collection and handling processes, ensuring the reliability
and validity of the research findings.
Qualitative data collection
This study primarily uses semi-structured interviews to explore the connotations and dimensions of low-
carbon information quality50. To ensure participant cooperation and data reliability and representativeness, 30
individuals from three relevant groups were selected for interviews (Table 1):
• Digital marketing professionals ( n = 5): Individuals with practical experience and unique insights into
low-carbon information marketing.
• Experts and scholars in the low-carbon field ( n = 5): Specialists from environmental science, energy policy,
and sustainable development who can assess content quality from a professional perspective.
• General consumers ( n = 20): Randomly selected users engaged with low-carbon information, representing
end consumers and reflecting the impact of content quality on them.
Initially, five respondents were randomly selected for preliminary interviews using open-ended questions (e.g.,
“What do you consider high-quality low-carbon information?”) to inform the design of the semi-structured
interview guide. Based on feedback, the interview framework was refined, and in-depth interviews were
conducted with 25 participants.
This study employed both face-to-face and remote in-depth interviews. For face-to-face interviews, questions
were provided in advance, and specific times were scheduled to facilitate deeper understanding. Interviews were
conducted in informal settings (e.g., cafes, offices). Before the formal interviews, researchers outlined relevant
concepts of low-carbon information quality and types of digital marketing recommendations, using non-
technical language to facilitate understanding. Each interview was kept to about 20 min51.
Quantitative data collection
To construct a robust quality assessment model for low-carbon information within digital marketing
recommendations, we employed a comprehensive and systematic data collection approach, ensuring data
diversity, representativeness, and timeliness (Smith, 2022). The final dataset comprised over 16,000 entries,
encompassing text, images, and videos.
Data collection tools and sources  A custom web scraping tool was developed using Python’s Scrapy library
(version 2.5.1) along with platform-specific APIs to gather a multifaceted dataset (Jones et al., 2023). The follow-
ing data sources were utilized:
• Official Media (33%): Data was scraped from the Xinhua News Agency website (http://www.xinhuanet.com),
the People’s Daily Environmental Channel (http://env.people.com.cn), and specialized environmental news
Demographic variable Variable category Sample size Percentage (%)
Gender
Male 17 56.7%
Female 13 43.3%
Age
20–25 years 7 23.3%
26–35 years 10 33.3%
36–45 years 11 36.7%
46–55 years 2 6.7%
Education Level
Associate Degree or below 3 36.7%
Bachelor’s Degree 11 53.3%
Graduate Degree or above 16 10.0%
Occupation
Current Students 7 23.3%
Educational Researchers 6 20.0%
Government/Institution Employees 5 16.7%
Corporate Executives and Freelancers 12 40.0%
Table 1. Demographic characteristics of interviewees.

Scientific Reports |        (2024) 14:22416 4| https://doi.org/10.1038/s41598-024-72910-1
www.nature.com/scientificreports/

websites such as China Environmental News ( http://www.cenews.com.cn) and Environmental Protection
Magazine (http://www.epc.org.cn), using the Scrapy framework.
• Social Media (46%): Data was collected from Weibo and WeChat public platforms using their respective
APIs: Weibo API v2.0 and WeChat Public Platform API v3.0. This data included content from verified official
Weibo accounts and WeChat official accounts of environmental organizations (e.g., @WWFChina, @Green-
peace), personal Weibo accounts and WeChat official accounts of environmental experts and key opinion
leaders (KOLs), and user-generated content posted by environmental enthusiasts on both platforms.
• Government Sources (21%): Data was primarily acquired by scraping publicly available information from
official websites of government agencies, including the Ministry of Ecology and Environment of the People’s
Republic of China ( http://www.mee.gov.cn), the National Development and Reform Commission ( http://
www.ndrc.gov.cn), and local environmental protection bureaus at the provincial and municipal levels. The
web scraper was developed in Python using the Beautiful Soup library for parsing web content.
Data collection period and frequency Data collection spanned from January 1, 2023, to December 31, 2023,
covering a full year to account for potential seasonal variations in low-carbon content. The following strategies
were implemented to maintain data timeliness and comprehensiveness:
• Daily Scheduled Tasks: Automated scraping of the latest information from news websites and social media
platforms was performed daily at 2:00 AM using the Scrapy framework.
• Weekly Updates: Data from government websites and policy documents was updated every Sunday.
• Monthly Deep Dives: Archived pages were reviewed in depth on the 1st of each month to gather historical
data for the past year and conduct trend analysis.
Sampling strategy and bias mitigation  To address potential biases and ensure data quality, a stratified ran -
dom sampling technique was employed. Strata were defined based on source type (official media, social media,
government sources) and content type (text, image, video). Within each stratum, samples were randomly select-
ed to ensure representativeness52.
Specifically, we first obtained website traffic data for each source type using Alexa rankings ( https://www.
alexa.com/). Websites were then ranked based on traffic volume and user activity. Stratified random sampling
was performed proportionally to the website’s traffic share within its source type, ensuring that the collected
data reflected the overall information dissemination patterns across different source types. For example, if
Xinhua Net’s traffic accounted for 30% of the total traffic within official media websites, the data collected from
Xinhua Net also constituted 30% of the total official media data. To mitigate potential geographical bias, data was
weighted based on the population proportion of each province and municipality in China.
Technical challenges and solutions Data collection encountered technical challenges including anti-scraping
mechanisms, rate limiting, and dynamic content loading. These were addressed by implementing a random
proxy mechanism with 100 proxy IPs, adhering to robots.txt guidelines, utilizing an exponential backoff algo -
rithm for rate limiting, and employing Selenium WebDriver to handle dynamic content loading with a designat-
ed waiting time for complete page rendering53.
Ethical considerations and data privacy  Ethical considerations were prioritized throughout the data collec-
tion process. We strictly adhered to each platform’s terms of service and robots.txt guidelines. To protect user
privacy, collected personally identifiable information (PII), such as user IDs, was anonymized using a one-way
hashing algorithm, rendering it untraceable to individuals. For user-generated content, only publicly available
data was collected, excluding any content marked as private or restricted. When full-text content was required,
permission was obtained from the relevant platforms or users after collecting metadata and summary informa-
tion49.
Data validation and quality assurance A two-tier validation process was implemented to ensure the accuracy
and completeness of the collected data. Firstly, automated data cleaning was performed using Python scripts
to identify and address anomalies in data formatting and content. This included consistency checks for date
formats, data encoding, and data types; duplicate detection using Simhash and pHash algorithms for text and
images, respectively; and language detection using the langdetect library to ensure all content was in Simplified
Chinese54. Secondly, three researchers independently reviewed a random 5% sample of the data, focusing on ac-
curacy, relevance, and completeness. Detailed evaluation criteria and training were provided, and the research-
ers worked in pairs to cross-validate their assessments and reach a consensus55. Inter-rater reliability, calculated
using Cohen’s kappa coefficient, was 0.85, exceeding the acceptable threshold of 0.8.
Data storage and management The collected data was stored in a secure, encrypted MongoDB database (ver-
sion 5.0) hosted on a private cloud server. Regular backups were performed to prevent data loss, and access to
the database was restricted to authorized research team members only.
Limitations Despite our comprehensive approach, we acknowledge several limitations: The reliance on pub-
licly available data may not capture private discussions or sentiments about low-carbon topics. The one-year data
collection period may not reflect long-term trends in low-carbon information dissemination. While we strived
for representativeness, the online nature of our data sources may underrepresent segments of the population
with limited internet access.
Scientific Reports |        (2024) 14:22416 5| https://doi.org/10.1038/s41598-024-72910-1
www.nature.com/scientificreports/

Analysis of low-carbon information quality dimensions
Building on the Information Quality Theory framework, this study employed a grounded theory qualitative
research method to conduct three levels of coding on interview data. The aim is to establish a model of dimensions
of low-carbon information quality that influence consumer behavior.
Open coding
Open coding is primarily used to identify categories and concepts related to the research question by breaking
down, fragmenting, conceptualizing, and then recombining collected data to define categories and discover
themes. In the open coding phase, 25 interview materials were first imported into Nvivo11 software, key
information was extracted, irrelevant content was removed, and sentence-by-sentence coding was performed,
resulting in 118 initial statements. After aggregating similar or identical concepts and removing initial concepts
with a frequency of less than three, 19 initial concepts and eight low-carbon information quality categories were
identified, as shown in Table 2.
Axial coding
Open coding generated initial concepts and categories related to low-carbon information quality. However,
these concepts and categories remain isolated and lack clear interrelationships. Axial coding addresses this issue
by using cluster analysis to reveal the logical connections between these concepts. Through in-depth analysis
of the eight categories and their interrelationships, three main categories were identified: Matching Quality,
Presentation Quality, and Interpretability Quality. The specific meanings of these categories were elaborated to
prepare for the next step of theoretical construction, as shown in Table 3.
Main category Sub-category Description
Matching Quality (A1)
Behavioral Matching (B1) Recommendation information is highly related to the user’s low - carbon browsing history and behavioral habits, and can be adjusted based on the user’s needs and preferences.
Interest Matching (B2) Recommendation information aligns with the user’s environmental protection expectations and can stimulate the user’s purchasing desire.
Scenario Matching (B3) Recommendation information can provide what the user needs at the right time, and the information can meet the user’s current low-carbon needs.
Presentation Quality
(A2)
Content Quality (B4) The accuracy, completeness, and reliability of the recommendation low-carbon information.
Format Quality (B5) The dynamics, conciseness, and consistency of the recommendation low-carbon information.
Recommendation Quality (B6) The accessibility and ease of use of the recommendation low-carbon information.
Interpretability Quality
(A3)
Public Transparency (B7) The recommendation information is traceable, and the content of the information is publicly transparent.
Privacy Assurance (B8) During the use of recommendation information, the user’s personal information is protected and will not be leaked.
Table 3. Main categories and category descriptions.

Category Initial concept Original record
Behavior Match
Relevance P15: Recommendations align with my hobbies in low-carbon protection.
Correlation P17: Recommendations are highly correlated with previously viewed information.
Flexibility P10: Adjust content based on needs and preferences.
Interest Match
Preference P13: Recommendations match my environmental expectations without disappointing me.
Attraction P18: Low-carbon information is easy to understand and stimulates purchasing desire.
Scenario Match
Obtainability P03: Whether on the website or app, it is easy to obtain low-carbon product information.
Timeliness P06: When needed, timely access to the latest low-carbon information.
Effectiveness P19: Recommendations meet my current environmental needs.
Content Quality
Accuracy P05: Recommendations are accurate, clearly stating product low-carbon characteristics.
Completeness P09: Information is comprehensive, including certifications and data.
Reliability P11: Recommended products are trustworthy, from reliable sources.
Form Quality
Liveliness P07: Information is presented dynamically, making low-carbon features vivid.
Conciseness P12: Information is concise, not lengthy, emphasizing key points.
Consistency P08: Consistent recommendations across platforms, without contradiction.
Recommendation Quality
Low Disturbance P14: Even if I don’t understand, I can still find low-carbon products.
Usability P18: Quickly find appropriate low-carbon products based on recommendations.
Public Transparency
Reliability P02: User trusts recommendations due to platform verification.
Transparency P12: Information is transparent, with no hidden details, ensuring peace of mind.
Privacy Assurance Safety P04: Platform protects personal information, not disclosing privacy.
Table 2. The initial concepts and categories formed by open coding.

Scientific Reports |        (2024) 14:22416 6| https://doi.org/10.1038/s41598-024-72910-1
www.nature.com/scientificreports/

Selective coding
Selective Coding and Model Development: Selective coding involves systematically analyzing predefined
categories to identify the most representative and comprehensive core categories. This process aims to integrate
related concepts and categories into a theoretical framework, combining different levels of categories through
a coherent narrative. The analysis indicates that Matching Quality and Presentation Quality are explicit quality
requirements for low-carbon information in digital marketing recommendations, triggering low-carbon
responses. Interpretability Quality, on the other hand, is an implicit condition and safeguard for low-carbon
information quality. Based on these findings, a structural model was developed to examine the factors influencing
the quality of low-carbon information in digital marketing (Fig. 1).
Theoretical saturation testing
Theoretical saturation testing determines whether qualitative data has reached sufficient completeness. This is
achieved by re-analyzing newly acquired data using open, axial, and selective coding. The absence of new core
category relationships indicates that the grounded theory-derived categories and their hierarchical relationships
have reached saturation.This study initially conducted interviews with 30 participants. Following data coding,
no new concepts or relationships emerged. Employing the natural-occurring theoretical saturation testing
method, four additional participants were interviewed, and the three-level grounded theory coding procedure
was applied. The analysis revealed no new significant categories or concepts within the core categories, indicating
data saturation56.
Through a three-stage coding process using grounded theory and theoretical saturation testing, we
developed a model of low-carbon information quality in digital marketing, encompassing three core categories:
Matching Quality, Presentation Quality, and Interpretability Quality. Theoretical saturation testing confirmed
the distinctiveness of these categories, highlighting their representation of different aspects of low-carbon
information quality and their varying influence mechanisms on user behavior.
Matching quality This category emphasizes the alignment between low-carbon information and user needs,
directly influencing user interest and attention. If information fails to match user needs, users are likely to ignore
or reject it, even if the information itself is of high quality.
Presentation quality This category emphasizes the manner in which low-carbon information is presented, di-
rectly impacting user comprehension and acceptance. If information is unclear or presented in a dull or unin -
teresting way, users may find it difficult to understand or be unwilling to engage with it, even if the content is
valuable.
Interpretability quality This category emphasizes the transparency and credibility of low-carbon information,
directly influencing user trust and adoption. If the information source is unreliable or information disclosure
lacks transparency, users may doubt the authenticity and reliability of the information, even if the content aligns
with their needs.
Fig. 1. Model of factors influencing digital marketing-related low-carbon information quality.

Scientific Reports |        (2024) 14:22416 7| https://doi.org/10.1038/s41598-024-72910-1
www.nature.com/scientificreports/

By distinguishing these three core categories, we gain a deeper understanding of the various dimensions of
low-carbon information quality and their influence mechanisms on user behavior. This understanding provides
digital marketing platforms with more precise and effective guidance for developing low-carbon information
dissemination strategies.
Construction of a random forest evaluation model for low-carbon information
quality
Conceptual model design
A conceptual model linking low-carbon information quality dimensions to relevant influencing factors is
essential for effective assessment. Based on the three dimensions identified through qualitative research –
Matching Quality (A1), Presentation Quality (A2), and Interpretability Quality (A3) – we propose the following
model:
 Quality = f (M atching Quality, P resentation Quality, Interpretability Quality ) (1)
T o comprehensively evaluate low-carbon information quality, we identified and quantified measurable features
for each dimension (Table 3). The match dimension assesses the alignment between information and its target
audience. The beneficiality dimension evaluates the potential benefits for the audience, while interpretability
focuses on the clarity and ease of understanding. Based on these dimensions, we propose the following
conceptual model, where Features 1 to n represent the various influencing factors:
 Quality = f (F eature1, F eature 2, . . . , F eaturen) (2)
Algorithm model training
Random forest algorithm is an ensemble learning algorithm based on decision trees, commonly used for
classification and regression tasks. It operates by generating m subsets from the original dataset through bootstrap
aggregating (bagging). Each subset is used to train a decision tree with d randomly selected features, resulting in
m diverse trees. For a new sample, each tree generates a prediction, and the average of these predictions is taken
as the final output. The mathematical expression for a random forest is as follows:

P rediction = 1 N
n∑
i=1
T reei (X) (3)
where X represents the input sample, Treei represents the i-th decision tree, and N represents the total number of trees, the random forest algorithm offers several advantages for complex regression tasks like quality assessment.
These include resistance to overfitting, effective handling of high-dimensional data, and the ability to provide
feature importance scores. We formulated the low-carbon information quality assessment task as a machine
learning regression problem, using the extracted multidimensional features as inputs and the final quality score
as the output. A random forest algorithm was then employed to fit the proposed conceptual model57.
Evaluating the Conceptual Model involves feature engineering on raw low-carbon information data to extract
relevant features corresponding to the quality dimensions. These features are then standardized and compiled
into a feature matrix. This matrix, along with manually annotated content quality scores, forms the training set
for a random forest regression model. The resulting model serves as the final discriminant model. To assess the
quality of new low-carbon information, features are extracted and input into the trained model to predict its
quality score.
Data preprocessing
Constructing a robust quality assessment model for low-carbon information necessitates a substantial amount
of training data. The initial data, collected through web scraping and API calls, may contain quality issues such
as duplicates, irrelevant content, and formatting errors. To address these issues, a three-step data preprocessing
pipeline was implemented: data cleaning, feature engineering, and data encoding58.
Data cleaning
Automated data cleaning was performed using Python scripts to ensure data quality and consistency. This
process involved standardizing date formats, data encoding, and data types, with inconsistent entries being
either corrected or removed. Duplicate entries were identified and removed using the Simhash algorithm for
text data and the pHash algorithm for image data. Additionally, the langdetect library was employed to identify
and remove any content not in Simplified Chinese55.
Feature engineering
Based on the low-carbon information quality dimensions of Matching Quality, Presentation Quality, and
Interpretability Quality, we conducted comprehensive feature engineering, extracting multi-dimensional
features from the cleaned data. Open-source libraries such as Scikit-learn, NLTK, and Keras were employed
for feature extraction from text, images, and video data59. Specifically, we constructed features according to the
following sub-dimensions:
Scientific Reports |        (2024) 14:22416 8| https://doi.org/10.1038/s41598-024-72910-1
www.nature.com/scientificreports/

• Matching quality Behavioral Matching: We analyzed users’ low-carbon preferences based on their histori-
cal browsing data, likes, and favorites. We then calculated the correlation coefficients (e.g., cosine similarity)
between the keywords of the current information and the user’s interests.
• Scenario Matching: We assessed whether the information matched the user’s current needs based on the
information’s publication time, the user’s geographical location (if available), and the user’s potential current
context (e.g., work, leisure, travel). This involved using rule-based matching or machine learning models for
classification.
• Interest Matching: Combining “Behavioral Matching” and “Low-carbon Behavior Relevance, ” we analyzed
whether the information aligned with the user’s environmental values and beliefs and whether it could poten-
tially stimulate their purchasing desire.
• Presentation quality Content Quality: We evaluated the accuracy and completeness of the information
content. Accuracy was assessed by comparing the information with existing low-carbon knowledge bases or
through manual review, and a 0–1 variable was used to represent the outcome. Completeness was assessed by
checking whether the information contained essential low-carbon elements, such as the product’s raw mate-
rials, production process, usage methods, and recycling methods, using a checklist or information entropy.
• Format Quality: We used readability metrics, such as the Flesch-Kincaid readability ease score, to assess
the readability and ease of understanding of the text. Text length, image size, and video duration were also
used to evaluate conciseness. Furthermore, we assessed the vividness and appeal of the content based on text
sentiment scores, image attractiveness, and video engagement. For example, we employed image recognition
techniques to identify objects, scenes, and emotions in images and used speech recognition and natural lan -
guage processing techniques to analyze the sentiment and theme of video content.
• Interpretability quality Public Transparency: We assessed the reliability of the information source based
on the authority and credibility of the website, considering factors such as domain name, registration infor -
mation, and institutional background. We also evaluated the transparency of information based on whether
the information source, data source, and algorithms used were publicly disclosed and traceable. For example,
we checked whether the source of information was clearly labeled, whether the data processing procedure was
transparent, and whether interpretable machine learning models were used.
• Privacy Assurance: We evaluated the level of privacy protection based on whether the information contained
sensitive information and whether it complied with privacy regulations. This involved using regular expres -
sions or machine learning models to identify sensitive information.
Data encoding
After feature engineering, we encoded the extracted features to prepare the data for training the Random Forest
model60. This involved:
• Standardization: All features were scaled to a range between 0 and 1 to ensure that features with different
scales did not disproportionately influence the model.
• One-Hot Encoding: Categorical features, such as information source type (official media, social media, gov-
ernment) and content type (text, image, video), were converted into numerical representations using one-hot
encoding.
• Label Encoding: Ordinal features, such as the level of user engagement (e.g., low, medium, high), were con-
verted into numerical values using label encoding.
Model training
The feature matrix from feature engineering was combined with manually labeled quality scores to form
a supervised learning dataset. To prevent overfitting, k-fold cross-validation (k-fold CV) was employed to
divide the dataset into training and testing sets. Scikit-learn’s Random Forest Regressor was utilized for model
training61. Hyperparameter optimization using Randomized Search CV was performed to enhance performance
and generalization ability. Tuning the number of decision trees (n_estimators) with values below 100 (10, 30, 50,
80) revealed n_estimators = 30 as the optimal choice (Fig. 2).
After hyperparameter tuning, the final configuration for model evaluation was determined as follows:
n_estimators = 30, max_depth = 12, min_samples_split = 4, min_samples_leaf = 2, max_features =’log2’, and
bootstrap = True. This configuration yielded a random forest regression model with excellent performance on
the training set.
By using a tuned and trained random forest model, predictions are made on out-of-bag (OOB) data (i.e.,
samples not used during training). Then, each feature’s values are randomly shuffled, and predictions are made
again. The importance score for each feature is obtained by comparing the accuracy differences between the two
sets of predictions62. A higher score indicates a greater impact of that feature on the model’s prediction results,
playing a more critical role in evaluating low-carbon information quality. The heatmap of feature importance
scores after model training is shown in Fig. 3.
Model evaluation
To evaluate the performance of the random forest model, we applied it to a completely new set of low-carbon
information content data and compared its key performance metrics with those of several other commonly used
regression methods62. As shown in Table  4, the random forest model achieved the lowest Root Mean Squared
Error (RMSE) of 0.12 and the highest R-squared (R²) of 0.95, significantly outperforming the other methods.
Scientific Reports |        (2024) 14:22416 9| https://doi.org/10.1038/s41598-024-72910-1
www.nature.com/scientificreports/

Fig. 3. Model of factors influencing digital marketing-related low-carbon information quality.

Fig. 2. Performance analysis of the random forest algorithm with varying numbers of decision trees.

Scientific Reports |        (2024) 14:22416 10| https://doi.org/10.1038/s41598-024-72910-1
www.nature.com/scientificreports/

We cleaned 200 data points of low-carbon information recommended by digital marketing channels through
experiments and validated by experts. The data were then divided into training and test sets with a 7:3 ratio 63.
Analysis of the residual distribution of the trained random forest model on the test set revealed an approximate
normal distribution, with a mean near 0, kurtosis of 0.75, and skewness of -0.27 (Fig. 4). This suggests minimal
overall model bias. However, identified outliers in the residual distribution indicate that the model may struggle
with certain data points, leading to suboptimal prediction performance for some samples and highlighting areas
for further improvement.
To evaluate the predictive performance of the random forest model, we visualized its results using 20
independent datasets64. The model demonstrated a 93% prediction accuracy for samples with quality scores
ranging from 2 to 4 (The maximum score is 5). However, underfitting was observed for samples with scores
above 4 and below 2. Despite these limitations, the model achieved a 93% accuracy in identifying low-carbon
information content that aligns with established quality standards, demonstrating its ability to effectively
distinguish high-quality content (Fig. 5).
Discussion
This study aimed to identify the key dimensions of low-carbon information quality that influence consumer
behavior in digital marketing recommendations (RQ1) and to develop a Random Forest model for evaluating
and enhancing the quality of such information (RQ2).
Compared with existing research, this study contributes to a more nuanced understanding of low-carbon
information quality in several key ways. Firstly, this research introduces a novel consumer-centric framework
for evaluating low-carbon information quality, specifically tailored to the digital marketing context. Secondly,
this study identifies three core dimensions of low-carbon information quality: Matching Quality, Presentation
Quality, and Interpretability Quality, which extends the traditional Information Quality Theory (IQT) framework
by incorporating consumer-centric considerations. Finally, this research develops a quantifiable model, based
Fig. 4. Residual analysis of the random forest model.

Metric Random forest Linear regression Support vector regression Gradient boosting tree
RMSE 0.275 0.417 0.339 0.286
R2 0.871 0.725 0.803 0.854
Table 4. Comparison of key indicators of common regression methods.

Scientific Reports |        (2024) 14:22416 11| https://doi.org/10.1038/s41598-024-72910-1
www.nature.com/scientificreports/

on grounded theory and the Random Forest algorithm, for assessing low-carbon information quality, providing
practical guidance for digital marketers to enhance their strategies and promote sustainable consumption.
Regarding RQ1, our findings, derived from both qualitative and quantitative analyses, revealed three core
dimensions of low-carbon information quality: Matching Quality, Presentation Quality, and Interpretability
Quality.
Matching Quality: This dimension emphasizes the alignment between low-carbon information and user
needs, directly influencing user interest and attention. Our qualitative analysis revealed that users are more
receptive to information that aligns with their behavioral habits, interests, and usage scenarios. For example, P15
and P17 expressed preferences for information tailored to their individual low-carbon interests and past browsing
behavior. This observation is further supported by our Random Forest model, which identified “correlation with
low-carbon behavior” and “low-carbon interest alignment” as two of the most influential features in predicting
low-carbon information quality. This finding highlights the importance of leveraging user data to personalize
low-carbon information and ensure its relevance to individual consumers. By providing information that
resonates with users’ existing knowledge, values, and behavior patterns, digital marketers can capture attention,
stimulate interest, and ultimately increase the likelihood of engagement with low-carbon content.
Presentation Quality: This dimension highlights the importance of conveying low-carbon information in a
clear, engaging, and easily understandable manner. Our qualitative analysis indicated that users value accuracy
and completeness in information presentation. For instance, P05 emphasized the importance of accurate product
descriptions that clearly state low-carbon characteristics, while P09 highlighted the need for comprehensive
information, including certifications and data, to support low-carbon claims. Furthermore, users emphasized the
need for vivid and concise presentation styles. P07 expressed a preference for dynamic information that brings
low-carbon features to life, while P12 valued concise messaging that focuses on key points. These preferences
align with the findings from our Random Forest model, which identified “content accuracy, ” “information
completeness, ” and “content vividness” as significant predictors of low-carbon information quality. Therefore,
digital marketing platforms should prioritize both the factual accuracy of information and its presentation style
to ensure user comprehension and engagement.
Interpretability Quality: This dimension emphasizes the transparency and credibility of low-carbon
information, which directly influences user trust and adoption. Our qualitative analysis revealed that users are
more likely to trust information from reliable sources that are transparently presented and protect user privacy.
Fig. 5. Prediction performance of the random forest model.

Scientific Reports |        (2024) 14:22416 12| https://doi.org/10.1038/s41598-024-72910-1
www.nature.com/scientificreports/

For instance, P02 highlighted that platform endorsements enhance user trust in recommendations, while P04
emphasized the importance of privacy protection in building user confidence. While not directly incorporated
as features in our quantitative analysis, interpretability can be considered a foundational aspect of information
quality. Users are less likely to engage with information they perceive as untrustworthy or opaque, regardless of
its relevance or presentation. Therefore, platforms should prioritize building user trust by establishing robust
information review mechanisms, transparently disclosing information sources, and strictly adhering to data
security and privacy regulations.
Addressing RQ2, our findings indicate that the Random Forest model is an effective tool for evaluating low-
carbon information quality. The model achieved a 93% accuracy rate in identifying high-quality low-carbon
information, confirming the significant influence of the three identified dimensions. However, the model
exhibited limitations in identifying information with extremely high or low quality scores, indicating potential
underfitting in these cases. This suggests that while the model shows promise, there is room for improvement in
its ability to handle extreme cases. Future research can address this by collecting a larger, more diverse dataset
encompassing a wider range of quality levels and exploring alternative machine learning algorithms, such as
deep learning models, which may be better suited to capturing complex relationships and nuanced features in
the data.
The key dimensions of low-carbon information quality identified in this study, particularly Matching
Quality and Interpretability Quality, hold significant implications for broader sustainability initiatives.
Aligning information with consumer needs and preferences (Matching Quality) and ensuring transparency
and trustworthiness (Interpretability Quality) are crucial for promoting sustainable choices in various contexts.
For instance, in facilitating the adoption of renewable energy technologies, providing tailored information that
caters to consumers’ specific needs and knowledge levels, while ensuring the credibility of information sources,
can significantly enhance consumer confidence and encourage a transition towards cleaner energy sources.
Similarly, in the realm of green public procurement and government-led initiatives for low-carbon development,
ensuring the accuracy, relevance, and timeliness of low-carbon information, presented in a clear and accessible
manner, is paramount for guiding consumer and corporate decision-making towards sustainable practices65–67.
This study contributes to a more comprehensive understanding of low-carbon information quality by
combining empirical data with a consumer-centric perspective. Our proposed model provides a nuanced
framework for evaluating and enhancing the quality of low-carbon information disseminated through digital
marketing channels, ultimately contributing to the promotion of sustainable consumption.
Research conclusions, limitations, and prospects
Conclusion
This study aimed to explore the key dimensions of low-carbon information quality influencing digital marketing
recommendations and develop a Random Forest model to evaluate and enhance the quality of such information,
ultimately promoting sustainable consumer choices. By integrating information quality theory and digital
marketing theory, this study proposes a novel low-carbon information quality model encompassing three core
dimensions: Matching Quality, Presentation Quality, and Interpretability Quality. We employed grounded
theory and conducted in-depth interviews ( n = 30) with digital marketing practitioners, low-carbon experts,
and general consumers. The collected data was then used to construct and validate a Random Forest evaluation
model. Our findings confirmed that the three dimensions—Matching Quality, Presentation Quality, and
Interpretability Quality—significantly influenced the perceived quality of low-carbon information. Additionally,
the constructed model effectively identified high-quality low-carbon information.
Theoretical contributions
This study makes several significant theoretical contributions to the existing literature on information quality and
low-carbon consumption. Firstly, we extend the application of Information Quality Theory (IQT) to the domain
of digital marketing, demonstrating its relevance in this increasingly important context for promoting sustainable
consumption. However, traditional IQT frameworks primarily focus on general information quality criteria and
lack the granularity to address the unique characteristics of low-carbon information and the heterogeneity of user
needs in this domain. This research addresses this gap by introducing “Matching Quality” as a new dimension
of low-carbon information quality. This dimension, defined as the alignment between low-carbon information
and user’s low-carbon behaviors and preferences, is crucial for effectively influencing consumer choices toward
sustainability. Unlike previous studies that primarily focus on corporate information disclosure, we develop a
consumer-oriented low-carbon information quality evaluation framework. This framework adopts a consumer-
centric perspective and recognizes the importance of understanding and addressing the information needs of
individual consumers, which is vital for promoting sustainable consumption.
To enhance low-carbon information quality for effective digital marketing strategies, low-carbon product
enterprises should prioritize the development of accurate user profiles to enable personalized low-carbon
recommendations. Furthermore, clarity, conciseness, and engaging presentation styles are crucial for effective
information dissemination. Additionally, establishing robust information review mechanisms and transparently
disclosing information sources are essential for fostering user trust.
Limitations and future research directions
This study acknowledges limitations regarding potential model underfitting when identifying information
with extreme quality scores, possibly due to an imbalanced training dataset. Future research should prioritize
collecting larger, more diverse datasets encompassing various low-carbon information sources, content types,
and quality levels to enhance model robustness and generalizability. Additionally, refining evaluation metrics,
exploring alternative machine learning algorithms (e.g., deep learning), incorporating granular user behavior
Scientific Reports |        (2024) 14:22416 13| https://doi.org/10.1038/s41598-024-72910-1
www.nature.com/scientificreports/

data (e.g., clicks, shares, comments), and examining the influence mechanisms of high-quality low-carbon
information on consumer behavior are recommended avenues for further investigation.
Data availability
The datasets used and/or analyzed during the current study are available from the corresponding author upon
reasonable request.
Received: 3 May 2024; Accepted: 11 September 2024
References
 1. Agnew, M. D., Pettifor, H. & Wilson, C. Lifestyle, an integrative concept: Cross-disciplinary insights for low-carbon research. Wiley
Interdiscip. Rev. Energy Environ.12(6). https://doi.org/10.1002/wene.490 (2023).
 2. Díaz-Padilla, V . T., Travar, I., Acosta-Rubio, Z. & Parra-López, E. Tourism competitiveness versus sustainability: Impact on the
world economic forum model using the. Rasch Methodol. Sustain.15(18), 13700. https://doi.org/10.3390/su151813700 (2023).
 3. Jain, P ., Chou, M. C., Fan, F . & Santoso, M. P . Embedding sustainability in the consumer goods innovation cycle and enabling tools
to measure progress and capabilities. Sustainability13(12), 6662. https://doi.org/10.3390/su13126662 (2021).
 4. Wei, J., Zhang, L., Y ang, R. & Song, M. A new perspective to promote sustainable low-carbon consumption: The influence of
informational incentive and social influence. J. Environ. Manag. 327, 116848. https://doi.org/10.1016/j.jenvman.2022.116848
(2023).
 5. Zhang, J., Lyu, Y ., Li, Y . & Geng, Y . Digital economy: an innovation driving factor for low-carbon development. Environ. Impact
Assess. Rev.96, 106821. https://doi.org/10.1016/j.eiar.2022.106821 (2022).
 6. Denga, E. M., Vajjhala, N. R. & Rakshit, S. The role of digital marketing in achieving sustainable competitive advantage. Digit.
Transform. Int. Strateg. Organ. 44–60. https://doi.org/10.3390/su132413679 (2022).
 7. Lewis, J. I. & Nemet, G. F . Assessing learning in low carbon technologies: Toward a more comprehensive approach. Wiley
Interdiscip. Rev. Clim. Change12(5), e730. https://doi.org/10.1002/wcc.730 (2021).
 8. Miguel, A. & Miranda, S. The role of digital platforms in promoting pro-sustainable behavior and conscious consumption by
brands. Ecocycles9(2), 37–48. https://doi.org/10.19040/ecocycles.v9i2.298 (2023).
 9. Y ang, S., Jahanger, A. & Hossain, M. R. Does China’s low-carbon city pilot intervention limit electricity consumption? An analysis of
industrial energy efficiency using time-varying DID model. Energy Econ.121, 106636. https://doi.org/10.1016/j.eneco.2023.106636
(2023).
 10. Castro-Santa, J., Drews, S. & Bergh, J. Nudging low-carbon consumption through advertising and social norms. J. Behav. Exp.
Econ.102, 101956. https://doi.org/10.1016/j.socec.2022.101956 (2023).
 11. Wang, T., Shen, B., Springer, C. H. & Hou, J. What prevents us from taking low-carbon actions? A comprehensive review of
influencing factors affecting low-carbon behaviors. Energy Res. Social. Sci. 71, 101844. https://doi.org/10.1016/j.erss.2020.101844
(2021).
 12. Wu, Z., Duan, C., Cui, Y . & Qin, R. Consumers’ attitudes toward low-carbon consumption based on a computational model:
Evidence from China. Technol. Forecast. Soc. Chang.186, 122119. https://doi.org/10.1016/j.techfore.2022.122119 (2023).
 13. Zhang, L. et al. A data-driven approach to objective evaluation of urban low carbon development performance. J. Clean. Prod.368,
133238. https://doi.org/10.1016/j.jclepro.2022.133238 (2022).
 14. Wang, R. Y . & Strong, D. M. Beyond accuracy: What data quality means to data consumers. J. Manag. Inform. Syst.12(4), 5–33.
https://doi.org/10.1080/07421222.1996.11518099 (1996).
 15. Del Rio, D. D. F ., Sovacool, B. K. & Griffiths, S. Culture, energy and climate sustainability, and smart home technologies: A mixed
methods comparison of four countries. Energy Clim. Change2, 100035. https://doi.org/10.1016/j.egycc.2021.100035 (2021).
 16. Cheng, X., Wu, F ., Li, W ., Y ang, J. & Long, R. What maintains low-carbon consumption behaviors: Evidence from China. Renew.
Sustain. Energy Rev.189, 114050. https://doi.org/10.1016/j.rser.2023.114050 (2024).
 17. Peterson, R. A., Balasubramanian, S. & Bronnenberg, B. J. Exploring the implications of the internet for consumer marketing. J.
Acad. Mark. Sci.25, 329–346. https://doi.org/10.1177/0092070397254005 (1997).
 18. Sağkaya Güngör, A. & Ozansoy Çadırcı, T. Understanding digital consumer: A review, synthesis, and future research agenda. Int.
J. Consum. Stud.46(5), 1829–1858. https://doi.org/10.1111/ijcs.12809 (2022).
 19. Hofacker, C., Golgeci, I., Pillai, K. G. & Gligor, D. M. Digital marketing and business-to-business relationships: A close look at the
interface and a roadmap for the future. Eur. J. Market.54(6), 1161–1179. https://doi.org/10.1108/EJM-04-2020-0247 (2020).
 20. Xu, Y . & Li, C. M. Digital transformation, firm boundaries, and market power: Evidence from china’s listed companies. Systems11(9),
479. https://doi.org/10.3390/systems11090479 (2023).
 21. Sanbella, L., Van Versie, I. & Audiah, S. Online marketing strategy optimization to increase sales and e-commerce development:
An integrated approach in the digital age. Startupreneur Bus. Digit.3(1), 54–66. https://doi.org/10.33050/sabda.v3i1.492 (2024).
 22. Liu, Y ., Suo, X. K., Du, X. H., Wu, H. Q. & Lin, H. Corporate digital innovation and stock price crash risk. Finance Res. Lett.66,
Article 105690. https://doi.org/10.1016/j.frl.2024.105690 (2024).
 23. Y ang, R. Q. & Jiang, H. C. Digital marketing management control system based on blockchain under the internet background. Soft.
Comput.https://doi.org/10.1007/s00500-023-08352-0 (2023).
 24. Chintalapati, S. & Pandey, S. K. Artificial intelligence in marketing: A systematic literature review. Int. J. Market Res.64(1), 38–68.
https://doi.org/10.1177/14707853211018428 (2022).
 25. Varzaru, A. A. Assessing digital transformation acceptance in public organizations’ marketing. Sustainability15(1), Article 265.
https://doi.org/10.3390/su15010265 (2023).
 26. Sahli, A. & Lichy, J. The role of augmented reality in the customer shopping experience. Int. J. Organ. Anal.https://doi.org/10.1108/
IJOA-02-2024-4300 (2024).
 27. Jocevski, M. Blurring the lines between physical and digital spaces: Business model innovation in retailing. Calif. Manag. Rev.63(1),
99–117. https://doi.org/10.1177/000812562095 (2020).
 28. Bradač Hojnik, B. & Huđek, I. Small and medium-sized enterprises in the digital age: Understanding characteristics and essential
demands. Information14(11), 606. https://doi.org/10.3390/info14110606 (2023).
 29. Peng, H., Bumailikaimu, S. & Feng, T. The power of market: venture capital and enterprise digital transformation. North Am. J.
Econ. Finance74, Article 102218. https://doi.org/10.1016/j.najef.2024.102218 (2024).
 30. Dahiya, R. & Gayatri A research paper on digital marketing communication and consumer buying decision process: An empirical
study in the Indian passenger car market. J. Global Mark.31(2), 73–95. https://doi.org/10.1080/08911762.2017.1365991 (2018).
 31. Kim, J., Kang, S. & Lee, K. H. Evolution of digital marketing communication: Bibliometric analysis and network visualization from
key articles. J. Bus. Res.130, 552–563. https://doi.org/10.1016/j.jbusres.2019.09.043 (2021).
 32. Wang, H., Wu, D. L. & Zeng, Y . M. Digital economy, market segmentation and carbon emission performance. Environ. Dev.
Sustain.https://doi.org/10.1007/s10668-023-03465-w (2023).
Scientific Reports |        (2024) 14:22416 14| https://doi.org/10.1038/s41598-024-72910-1
www.nature.com/scientificreports/

 33. Surbakti, F . P . S., Wang, W ., Indulska, M. & Sadiq, S. Factors influencing effective use of big data: A research framework. Inf.
Manag.57(1), 103146. https://doi.org/10.1016/j.im.2019.02.001 (2020).
 34. Bovee, M., Srivastava, R. P . & Mak, B. A conceptual framework and belief-function approach to assessing overall information
quality. Int. J. Intell. Syst.18(1), 51–74. https://doi.org/10.1002/int.10074 (2003).
 35. Rane, N. L., Achari, A. & Choudhary, S. P . Enhancing customer loyalty through quality of service: Effective strategies to improve
customer satisfaction, experience, relationship, and engagement. Int. Res. J. Modernization Eng. Technol. Sci.5(5), 427–452. https://
doi.org/10.56726/IRJMETS38104 (2023).
 36. Lăzăroiu, G., Neguriţă, O., Grecu, I., Grecu, G. & Mitran, P . C. Consumers’ decision-making process on social commerce platforms:
Online trust, perceived risk, and purchase intentions. Front. Psychol.11, 890. https://doi.org/10.3389/fpsyg.2020.00890 (2020).
 37. Godoy, M. P ., Rusu, C., Hatibovic, F ., Granollers, T. & Ugalde, J. Addressing information consumer experience through a user-
centered information management system in a Chilean university. Sustainability15 (22), Article 15998. https://doi.org/10.3390/
su152215998 (2023).
 38. Kim, H. & Niehm, L. S. The impact of website quality on information quality, value, and loyalty intentions in apparel retailing. J.
Interact. Mark.23(3), 221–233 (2009). https://www.taylorfrancis.com/chapters/edit/10.4324/9780429293276-3
 39. Venkatesh, V ., Brown, S. A. & Bala, H. Bridging the qualitative-quantitative divide: Guidelines for conducting mixed methods
research in information systems. MIS Q. 21–54. https://doi.org/10.25300/MISQ/2013/37.1.02 (2013).
 40. Al-Fraihat, D., Joy, M. & Sinclair, J. Evaluating E-learning systems success: An empirical study. Comput. Hum. Behav.102, 67–86.
https://doi.org/10.1016/j.chb.2019.08.004 (2020).
 41. Du, H. L. S., Xu, J. H., Tang, H. & Jiang, R. X. Repurchase intention in online knowledge service: The brand awareness perspective.
J. Comput. Inform. Syst.62(1), 174–185. https://doi.org/10.1080/08874417.2020.1759159 (2022).
 42. Naim, A. & Alahmari, F . Reference model of e-learning and quality to establish interoperability in higher education systems. Int. J.
Emerg. Technol. Learn.15(2), 15–28. https://doi.org/10.3991/ijet.v15i02.11605 (2020).
 43. Struijk, M., Angelopoulos, S., Ou, C. X. & Davison, R. M. Navigating digital transformation through an information quality
strategy: Evidence from a military organization. Inform. Syst. J.33(4), 912–952. https://doi.org/10.1111/isj.12430 (2023).
 44. Rai, A., Tang, X., Yin, Z. & Du, S. Gaining customer loyalty with tracking information quality in B2B logistics. J. Manag. Inform.
Syst.39(2), 307–335. https://doi.org/10.1080/07421222.2022.2063552 (2022).
 45. Alterkait, M. A. & Alduaij, M. Y . Impact of information quality on satisfaction with e-learning platforms: Moderating role of
instructor and learner quality. SAGE OPEN 14(1), Article 21582440241233400. https://doi.org/10.1177/21582440241233400
(2024).
 46. Cao, Q., Zhou, Y ., Du, H., Ren, M. & Zhen, W . Carbon information disclosure quality, greenwashing behavior, and enterprise value.
Front. Psychol.13, 892415. https://doi.org/10.3389/fpsyg.2022.892415 (2022).
 47. Zha, D., Zhang, C., Jiang, P . & Wang, F . What makes energy consumption behavior visible? Conceptualization, scale development
and validation of customized information feedback. J. Bus. Res.182, 114761. https://doi.org/10.1016/j.jbusres.2024.114761 (2024).
 48. Mills, J., Bonner, A. & Francis, K. The development of constructivist grounded theory. Int. J. Qual. Methods5(1), 25–35. https://doi.
org/10.1177/160940690600500103 (2006).
 49. Lin, W ., Wu, Z., Lin, L., Wen, A. & Li, J. An ensemble random forest algorithm for insurance big data analysis. IEEE Access5,
16568–16575. https://doi.org/10.1109/ACCESS.2017.2738069 (2017).
 50. Gustavsson, E. & Elander, I. Behaving clean without having to think green? Local eco-technological and dialogue-based, low-
carbon projects in Sweden. J. Urban Technol.24(1), 93–116. https://doi.org/10.1080/10630732.2016.1175806 (2017).
 51. Sturges, J. E. & Hanrahan, K. J. Comparing telephone and face-to-face qualitative interviewing: A research note. Qualitative
Res.4(1), 107–118. https://doi.org/10.1177/1468794104041110 (2004).
 52. Hurwitz, L. B. et al. Content analysis across new media platforms: Methodological considerations for capturing media-rich data.
New. Media Soc.20(2), 532–548. https://doi.org/10.1177/1461444816663927 (2018).
 53. Roumeliotis, K. I. & Tselikas, N. D. A machine learning python-based search engine optimization audit software. In Informatics10(3),
68. https://doi.org/10.3390/informatics10030068 (2023).
 54. Pamulaparty, L., Rao, C. G. & Rao, M. S. Critical review of various near-duplicate detection methods in web crawl and their
prospective application in drug discovery. Int. J. BioMed. Eng. Technol.25(2–4), 212–226. https://doi.org/10.1504/IJBET.2017.087723
(2017).
 55. Sun, J. Improving Quality of Programming and Software Through Knowledge Graph Construction and Application. Doctoral dissertation
(The Australian National University, 2023). https://www.proquest.com/openview/5b5e3c1260a05ccb1313dace42759240
 56. Peters, H. C. A-methodological saturation: A grounded theory analysis. Couns. Psychol. 51(7), 933–969. https://doi.
org/10.1177/00110000231179706 (2023).
 57. Biau, G. & Scornet, E. A random forest guided tour. Test25, 197–227. https://doi.org/10.1007/s11749-016-0481-7 (2016).
 58. Gupta, S., Aga, D., Pruden, A., Zhang, L. & Vikesland, P . Data analytics for environmental science and engineering research.
Environ. Sci. Technol.55(16), 10895–10907. https://doi.org/10.1021/acs.est.1c01026 (2021).
 59. Jantunen, E., Campos, J., Sharma, P . & McKay, M. Open source analytics solutions for maintenance. In 5th International
Conference on Control, Decision and Information Technologies (CoDIT) , vol. 8, 688–693. (IEEE, 2018). https://doi.org/10.1109/
CoDIT.2018.8394819.
 60. Yin, Y ., Alqahtani, Y ., Feng, J. H., Chakraborty, J. & McGuire, M. P . Classification of eye tracking data in visual information
processing tasks using convolutional neural networks and feature engineering. SN Comput. Sci.2, 1–26. https://doi.org/10.1007/
s42979-020-00444-0 (2021).
 61. Kadiyala, A. & Kumar Applications of python to evaluate the performance of bagging methods. Environ. Prog. Sustain. Energy37(5),
1555–1559. https://doi.org/10.1002/ep.13018 (2018).
 62. Farnaaz, N. & Jabbar, M. A. Random forest modeling for network intrusion detection system. Procedia Comput. Sci.89, 213–217.
https://doi.org/10.1016/j.procs.2016.06.047 (2016).
 63. Yin, H. et al. A deep learning-based data-driven approach for predicting mining water inrush from coal seam floor using micro-
seismic monitoring data. IEEE Trans. Geosci. Remote Sens.https://doi.org/10.1109/TGRS.2023.3300012 (2023).
 64. Zermane, A., Tohir, M. Z. M., Zermane, H., Baharudin, M. R. & Yusoff, H. M. Predicting fatal fall from heights accidents using
random forest classification machine learning model. Saf. Sci.159, 106023. https://doi.org/10.1016/j.ssci.2022.106023 (2023).
 65. Yin, H. T., Wen, J. & Chang, C. P . Going green with artificial intelligence: The path of technological change towards the renewable
energy transition. Oecon. Copernic.14(4), 1059–1095. https://doi.org/10.24136/oc.2023.032 (2023).
 66. Lăzăroiu, G. et al. Environmentally responsible behavior and sustainability policy adoption in green public procurement.
Sustainability12(5), 2110. https://doi.org/10.3390/su12052110 (2020).
 67. Bai, T. et al. Paths to low-carbon development in China: The role of government environmental target constraints. Oecon.
Copernic.14(4), 1139–1173. https://doi.org/10.24136/oc.2023.034 (2023).
Author contributions
All authors contributed to the study meaningfully, providing feedback on the interpretation of the results and
on the writing of the paper.
Scientific Reports |        (2024) 14:22416 15| https://doi.org/10.1038/s41598-024-72910-1
www.nature.com/scientificreports/

Declarations
Competing interests
The authors declare no competing interests.
Additional information
Correspondence and requests for materials should be addressed to W .G.
Reprints and permissions information is available at www.nature.com/reprints.
Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and
institutional affiliations.
Open Access  This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives
4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in
any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide
a link to the Creative Commons licence, and indicate if you modified the licensed material. Y ou do not have
permission under this licence to share adapted material derived from this article or parts of it. The images or
other third party material in this article are included in the article’s Creative Commons licence, unless indicated
otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and
your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain
permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/
licenses/by-nc-nd/4.0/.
© The Author(s) 2024
Scientific Reports |        (2024) 14:22416 16| https://doi.org/10.1038/s41598-024-72910-1
www.nature.com/scientificreports/
