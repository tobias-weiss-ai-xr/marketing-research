---
title: 'THE ROLE OF ARTIFICIAL INTELLIGENCE IN TRANSFORMING TOURISM SERVICES: THE CASE OF DURRËS, ALBANIA'
url: https://doi.org/10.30892/gtg.61308-1518
category: ai-marketing
subcategory: case-study
date: 2025-07
venue: GeoJournal of Tourism and Geosites
authors:
- Anxhela Kosta
- Florina PAZARI
- Ilma Lili
source: openalex-oa
pdf_url: https://doi.org/10.30892/gtg.61308-1518
pages: 10
chars: 51329
fetched_at: '2026-11-08T17:44:28+00:00'
kb_version: 1
---

# THE ROLE OF ARTIFICIAL INTELLIGENCE IN TRANSFORMING TOURISM SERVICES: THE CASE OF DURRËS, ALBANIA

Geojournal of Tourism and Geosites Year XVIII, vol. 61, no. 3, 2025, p.1485-1494
ISSN 2065-0817, E-ISSN 2065-1198 DOI 10.30892/gtg.61308-1518

http://gtg.webhost.uoradea.ro/

THE ROLE OF ARTIFICIAL INTELLIGENCE IN TRANSFORMING
TOURISM SERVICES: THE CASE OF DURRËS, ALBANIA

Anxhela KOSTA 11* , Florina PAZARI 2 , Ilma LILI 1 , Silvana GRECA 1

1 University of Tirana, Faculty of Natural Science, Department of Computer Science, Tirana, Albania; anxhela.kosta@fshn.edu.al
(A.K.); ilma.lili@fshn.edu.al (I.L.); silvana.greca@fshn.edu.al (S.G.)
2Barleti University, Faculty of Social Science, Tourism and Sport, Department of Tourism, Hospitality and Recreation, Tirana,
Albania; floripazari@gmail.com (F.P.)

Citation: Kosta, A., Pazari, F., Lili, I., & Greca, S.  (2025). The role of artificial intelligence in transforming tourism services:
The case of Durrës, Albania. Geojournal of Tourism and Geosites, 61(3), 1485–1494. https://doi.org/10.30892/gtg.61308-1518

Abstract: In Albania, the tourism sector has increasingly been using technology to improve the travel experience and service
management. In t he past, websites and mobile applications served as promotional tools, but recent developments support more
sophisticated operations. This study explores the impact of Artificial Intelligence (AI) in tourism services in Durrës, Alban ia,
focusing on how AI -driven technologies improve service management, customer experience, decision making and hotel
recommendations. A mixed-methods approach was used, including a literature review, interviews, surveys, implementation, and
process improvement. An AI-based hotel recommendation system was developed using Natural Language Processing (NLP) and
machine learning to analyze customer reviews. Hotel reviews were collected from Google Reviews, and artificial intelligence
techniques were applied to identify and recommend hotels with similar ratings and sentiment profiles, thereby supporting more
personalized and data -driven recommendations. Through sentiment analysis, the reviews were classified as either negative or
positive. The study finds that AI technologies improve o perational efficiency, increase customer engagement, and support
strategic marketing efforts. It is recommended that tourism services in Durres adopt AI solutions as they positively impact
automated bookings, tour management, and personalized digital inter actions, thereby enhancing tourism to a greater extent. The
integration of AI -based recommendation systems further demonstrates how data analytics and sentiment analysis can optimize
hotel selection processes for tourists. On the other hand, the high cost and staffing required for this poses a challenge for the city.
This study provides a unique focus on AI's impact within Albania’s tourism sector, with Durrës as a case study. By integratin g
AI-driven analytics and hotel recommendation algorithms, the resea rch highlights the role of AI in improving service quality,
business efficiency, and the overall competitiveness of Albanian tourism. It offers practical insights into how AI can drive
sustainable growth and innovation, positioning Albania’s tourism industry for a more tech-driven future.

Keywords: Artificial Intelligence, Natural Language Processing (NLP) techniques, tourism, Selenium, Durrës, TF -IDF-based
text similarity, cosine similarity

*  *  *  *  *  *

INTRODUCTION
Albania is a country with a beautiful climate and natural beauty, which makes tourism a major sector in the Albanian
economy. Tourism offers a natural and cultural attraction that attracts domestic and international visitors. With the growth
of technology and the introduction of Artificial Intelligence everywhere, the question arises whether tourism needs the use
of technology? The answer is Yes, it has become indispensable in shaping travel experiences and improving tourism
management, everything in tourism is moving towards the digital part. Technology is involved in every phase of the tourist
journey, from simple websites and mobile applications to complex systems that personalize visitor interactions.
Over the past few years, the accessibility of digita l platforms has transformed the way tourists access, find
information, make reservations online without being physically present and interact with destinations. Tour operators
offer services more efficiently and tailor tourist packages according to individ ual preferences, because they have the
help of AI -powered applications such as chatbots, recommendation engines and data analytics platforms. Albania in
2024 had the highest number of visitors to the country, thus enabling a considerable potential for econ omic growth.
Certainly, for a better management of tourism, the integration of Artificial Intelligence can improve service quality and
operational effectiveness, helping the country compete in a digitally driven tourism landscape. The purpose of this paper
is to analyze, study, the impact of information technology on Tourism and what we can offer to improve it better.
The study  focuses on Durrës, one of Albania’s most popular coastal destinations, to examine the impact of
technology on tourism, and draws on face -to-face interviews with 6 major resorts in Durrës. Through interviews and
surveys conducted with local businesses including hotels and restaurants, this research investigates whether AI -driven
technology has begun to be used, and whether it is cont ributing positively to the tourism industry. The focus of the study
is also to examine the level of technological adoption, the challenges businesses face in using AI, and whether these

1* Corresponding author

Anxhela KOSTA, Florina PAZARI, Ilma LILI, Silvana GRECA

 1486
businesses are open to adopting AI tools. Based on the responses we re ceived from the study, and the perspectives of
tourism businesses, this paper also provides an implementation of a recommendation system using Artificial Intelligence
for tourists based on hotel reviews on Google and classifying them as positive or negative using semantic analysing.

LITERATURE REVIEW
Based on the research of academics and other scientists, in this section we are briefly summarizing the historical
development in tourism technology, the benefits of adapting these advances and future trends, and focusing more on
artificial intelligence and virtual reality VR. Of course, technology has also been introduced into the tourism sector,
reformulating the way of operating and serving tourists.
The way tourists receive recommendations, make online reservations, receive services without being present or without
having a traditional travel brochure, we can say that the revolution has been extraordinary.

a) Historical development of technology in tourism
Tourism has become more accessible and convenient since the 19th century with advancements in technology. The
development of steam engines and railways revolutionized mobility, allowing more people to move into new destinations
(Buhalis & Leung, 2018; Gretzel et al., 2015). The digital age further transformed the industry, as the internet opened up
online booking platforms, travel blogs, and social media -based promotion. Websites and apps soon emerged as favorite
platforms for providing real-time information about destinations, accommodations, and activities, setting new standards for
convenience and ease of access for travel planning (Huang et al., 2017).

b) The role of artificial intelligence and virtual reality
AI and VR have emerged as game changers fo r the tourism industry, increasing operational efficiency as well as
customer experiences. Artificial Intelligence used to be said to be in the future, but now we say we are in the future as it is
being used more and more every day in every sector, but esp ecially in the tourism sector. According to (Kieanwatana &
Vongvit, 2024) communication and response to a certain service against tourists has been difficult and slow before the
creation of AI. With the creation of AI, chatbots were also created which auto matically returned responses, enabling direct
communication with customers. Recommendation engines made it possible to create and offer tourist packages or services
based on user preferences and predictive analytics of user interests. On the other hand (Guttentag, 2010) stated that not only
chatbots, or recommendation systems helped in customer service in tourism, but also VR technologies began to be widely
used to offer visitors a different reality by seeing the destination virtually before touching it. Th rough VR, visitors were
able to make easier decisions about the selection of the destination (Kannan & Antony, 2024).

c) Advantages of technology in tourism
Giant platforms such as Booking.com and Airbnb have completely simplified the online booking part by  offering
tourists instant booking without any hassle and an open system to see and comment on the center or service they received.
Applications of Artificial Intelligence in tourism have helped a lot to improve various parts of the tourism sector, especially
chat bots that give direct answers without the need for human resources. Online advertisement has also risen in specificity
so that tourism businesses can access their target population through targeted ads  (Xiang & Fesenmaier, 2017; Neuhofer et
al., 2015). Data analytics tools help organizations analyze the behavior of customers, predict trends, and optimize service
offerings to enhance organizational efficiency and customer satisfaction (Mariani et al., 2018; Gretzel et al., 2015).

d) Future trends in tourism technology
In the coming years, AI, VR, and big data will play an even greater role in the future of tourism. AI solutions such as
real-time personalization marketing and dynamic pricing will help companies react to individual customers' needs in r eal
time. VR will provide tourists with pre -experiences of destinations, further influencing booking intentions (Tussyadiah
& Wang, 2016; Mariani et al., 2018). Moreover, analysis of big data will become increasingly important in evaluating
market trends t o allow companies to make decisions through information and aid improved service provision and
customer engagement (Slevitch et al., 2020). Analysis and recommendation systems based on AI are also expected to be
more advanced. Sentiment analysis techniques  will be enhanced by machine learning algorithms, improving how firms
interpret and act on customer feedback. Reinforcement learning may also improve recommendation engines to provide
real-time and dynamic personalized recommendations to tourists.

e) Challenges and considerations
While AI and other emerging technologies bring numerous advantages, their implementation is challenging. Issues
such as data privacy, cybersecurity, and adoption costs are still obstacles, particularly for small and medium -sized
enterprises. There is also a debate regarding AI -driven automation and its contribution to job displacement in the
tourism sector. The implementation of AI in Albania is also restrained by other issues like infrastructure and
technological expertise shortages . The majority of tourism businesses, especially the small and medium -sized ones, are
restricted by financial limitations that prevent them from investing in new and advanced technologies like AI and VR.
These must be addressed through strategic digital i nfrastructure investments, improved training programs, and
increased awareness among business owners about the benefits of AI adoption (Neuhofer et al., 2015; Tussyadiah &
Wang, 2016, Ivancsóné Horváth  et al., 2025).

The Role of Artificial Intelligence in Transforming Tourism Services: The Case of Durrës, Albania

 1487
METHODOLOGY
Understanding the reason wh y this topic is being addressed is a key element in identifying and carrying out the work.
The methodology followed for carrying out this work is: Collection and review of secondary data. Which were provided by
a simple internet search, by accessing online libraries, research reports related to the topic and a non-exhaustive list of other
secondary sources. From the secondary research, it is intended to understand the results of the academics, sciences they
have achieved, the difficulties and conclusions, r egarding how technology affects tourism. The study then follows with a
primary research/study, on the use of technology in tourism and the positive or negative effects it has on tourism in
Albania. Six big resorts in Durres were selected, to conduct direct  interviews with them. The goal was to understand how
AI-driven technologies affect tourism services in Durres, Albania. Implementing an AI recommendation system based on
Google reviews for these sectors enables increased customer satisfaction and operational efficiency. Using the Selenium for
web scraping, we have collected all the available user reviews placed on Google. To classify the ratings as positive,
negative or neural, we have used AI-based sentiment analysis and natural language processing (NLP) techniques.

Market study in Albania – Tourism and technology
In this study several resorts within the tourism sector were examined, including: restaurants, hotels, resorts and
guesthouses as part of their integrated service offering. These businesses repr esent a broad spectrum of the tourism
industry, each focusing on varied ways technology impacts their operations and growth. Table 1 below presents the names
and official Google Business links of the selected hospitality establishments that participated in  the survey. The primary
objective of this survey was to analyze the use of technology in the tourism sector from a business perspective.
Participating businesses provided valuable insights into how they utilize technology for management, online promotion,
and booking processes. Another aspect highlighted was the role of technology in offering personalized services to clients,
which contributes to increasing their tourism experience. The businesses indicated that they use a range of platforms and
technological tools to increase efficiency in daily operations. Some of the most commonly mentioned tools included:
a. Inventory Management Applications.
b. Online Booking Software
c. Customer Data Collection and Analysis Systems
In terms of digital marketing, businesses are increasingly oriented toward using platforms such as social media, online
advertisements, and search engines to promote their offerings. This approach facilitates real -time interaction with clients
and helps build long-lasting relationships with them. One of the main objectives of this study was to identify best practices
and challenges encountered in implementing technology in Albania's tourism industry. Businesses reported that one of the
greatest benefits of technology is the significant increase in operational efficiency and improved communication with
clients. Technology aids in establishing a stronger online presence, thereby increasing the visibility and promotion of local
tourist destinations. On the other hand, some businesses also faced challen ges when integrating technology into their
operations due to some barriers. Among these challenges are the high initial investment costs associated with technology
and a lack of qualified staff to manage these technological tools. We did physical interview s with the owners of the Hotels
that are shown in Table 1 and also we used Google Forms to collect the results.

Table 1. Tourism businesses in Durrës included in the survey and their Google Business profile links

Name of Resorts Google My Business link
 BRILLIANT HOTEL AND SPA Brilliant Hotel & Spa
KLAJDI RESORT Klajdi Resort
FAFA RESORT Grand Blue Fafa Resort
SUPREME HOTEL Supreme Hotel
PINEA HOTEL Pinea Hotel

STUDY RESULTS AND INTERPRETATION
From analyzing the collected responses, it is clear that the majority of surveyed entities are hotels and restaurants that
have integrated technology in several aspects of their management, as shown in Figure 1. What type of business do you
operate? Do you use technology to manage your business? Do you use technology to manage your business?

Figure 1. Distribution of business types participating in the tourism technology survey

Anxhela KOSTA, Florina PAZARI, Ilma LILI, Silvana GRECA

 1488

Figure 2. Business responses on the use of technology in tourism management

Figure 2 illustrates that respondents emphasized that they used technology more for managing online reservations and
storing data. They emphasized that this has facilitated customer servic e and improved resource management. Websites are
now, let's say, the formal part of every business. What stands out is that 95% of businesses reported having a website.
Through the website, they are present online, can be found and offer information to tou rists. Websites were stated to be
used more for the presentation and promotion of tourism businesses. The use of online reservation management systems is
also high, with 89% of businesses using platforms such as Booking.com and Airbnb to receive customer reservations.
These systems have significantly simplified the reservation process and have contributed to an increase in the number of
customers. At the end of the survey, 95% of businesses identified technology as a fundamental driver for the development
of tourism. They believe that technology not only promotes tourist destinations, but also plays a crucial role in increasing
tourists’ awareness of local attractions and offerings. In 2024, Artificial Intelligence spread rapidly almost all over the
world. So the respondents stated that if they incorporate artificial intelligence into some tourist services, it could
significantly increase productivity by automating routine tasks, allowing human resources to focus on more personalized
services. On the other h and, the tourist has an easier time getting the service he wants and also through AI he can get
suggested packages based on his reviews. The last question was: Give your opinion, what is expected to happen with
tourism in the coming years and what are the barriers that AI uses in Albanian tourism?

1. Barriers to the use of technology in Albanian tourism
Based on our survey of tourism businesses in Durres, some of the primary challenges which hinder full application of
technology and artificial intelligence  in tourism in Albania have been identified. The challenges range from structurally
diversified operations that hinder them from having the capacity to utilize and gain from AI -based solutions. These are the
most common of them, e.g., a lack of infrastruct ure for the internet, data security problems, the cost of implementation
being too high, and lacking the appropriate expertise in AI. All of them need to be handled so that technology can be
utilized to the maximum in enhancing the tourism industry of Albania.

1.1. Lack of internet infrastructure and digital accessibility
To use digital platforms, internet access and its reliability are essential. One of the biggest problems that Albania still faces
is the unstable access to the quality of the internet. Es pecially in coastal areas where internet coverage is low and in more
remote areas it almost does not reach at all. Bad internet access causes all sorts of issues for the tourism industry in Durr ës,
both for businesses and visitors. Nowadays, visitors are v ery much reliant upon online websites for restaurant and hotel
bookings and organizing places. In case of poor internet connectivity, the places are unable to utilize these facilities to t heir
full capacity and, hence, lose opportunities in greeting and ho sting guests efficiently. Technologies such as AI -powered
chatbots, smart check-in devices, and AR guides must be run on high -quality internet connectivity. Without access to such
tools, it is difficult for most Durrës businesses to compete with internatio nal tourist trends, tapping into their potential to
deliver tourists modern, technologically driven experiences. A second, more serious issue is that of remote working and online
management. Most of the hotels and tourist establishments are employing cloud -based management systems to handle
reservations, payments, and messages from guests. When there are interruptions in the internet, those systems turn unreliable,
leading to inefficiencies in day-to-day activities and spoiling the overall customer experience (Sousa et al., 2024).

2.2. Data security and privacy risks
With increasingly more tourism businesses in Albania going digital, data privacy and cybersecurity have become
pressing concerns. Most of the businesses in the sector have poor cybersecurity sy stems, which leave them open to
attacks such as data stealing, financial fraud, and identity theft. The greatest concern is the utilization of poor security
systems, where the majority of companies continue to utilize basic password protections and outdate d software, which
leave them vulnerable to simple cyberattacks. Cyber awareness among hotel and tourism staff is still limited, and they
are not at all or inadequately trained in identifying and preventing phishing attempts, malware infections, and other
online threats. Using and accessing the internet is not always positive if you are not sufficiently educated about
preventive measures. Businesses are still vulnerable to potential security breaches that could compromise customer data
and damage their image . We know that taking preventive measures against internet security requires budget and finance.
Financial constraints for the digital part in Albania also affect especially small businesses as they place more importance

The Role of Artificial Intelligence in Transforming Tourism Services: The Case of Durrës, Albania

 1489
on daily operating costs than cyber security. Without investment, exposed customer data goes unprotected, and the
vulnerability for data breaches and loss of money is increased. Even as of 2025 Albania is on the rise in terms of
cybersecurity Albania has progressed significantly in the ITU's  Global Cyber Security Index, moving up by 22 points
compared to the last report and ranked in Tier 2, among the countries that are developing rapidly in the field of cyber
security. It is a sign that the Albanian government is seriously working on makin g digital defenses more robust and
addressing growing cyber security threats effectively (National Authority for Cyber Security, 2025).

3.3. High costs of technology adoption
The incorporation of artificial intelligence -driven tools and intelligent tourist solutions poses a significant financial
burden to most of Albania's tourism sectors. It is within reach for large hotels to pay for computerized management
software, but smal l and medium enterprises (SMEs) cannot match the pace with the burden of digital change.
The investment is not only the one -time investment but also the ongoing expenses that present a challenge for small
businesses to implement technology. The greatest c hallenge is the significant amount of initial investment required to
deploy AI chatbots, automated booking systems, and data analysis software. The technologies, as beneficial as they are
for making business processes more efficient and customer experience  better, require a tremendous amount of financial
resources that many companies cannot put into them. One of the interviewees, the owner of Brilant Hotel, stated that a
key challenge is also the lack of access to finance from government funding. The govern ment has no subsidies to
support small businesses in implementing AI and the use of information technology in tourism.
Without any external help, most SMEs are not able to delay or forego digital transformation, which limits them from
competing with larg er, more tech -savvy players. Overcoming such economic barriers entails support from policies,
investment at hand, and individualized financing arrangement to facilitate companies of all sizes to avail digital
innovations towards continued development of th e tourism sector of Albania.

2.  Advantages of using AI and technology in tourism
The tourism industry is one of the sectors that has been most affected by technology and its role has become indispensable in
the management and performance of technical operations of companies operating in the tourism market. Technology has played
an important and very productive role in improving services and customer experience. The use of online platforms for managing
reservations, digital marketing, processing and analyzing customer information and facilities in electronic communication with
customers has created new and very effective opportunities for improving services and expanding into the global market
(Nongkhoo, 2025). Table 2 highlights the key reasons why AI and technologies are beneficial in the tourism industry.

Table 2. Advantage of using AI in Tourism

1
Improving customer
service and personalized
experience
Artificial intelligence, through virtual assistants and chatbots, helps customers find their most opti mal
solutions depending on their needs and expectations for the services requested. This is consist ent with
findings from (Czyz &  Javed 2025), who highlight that smart tourism technologies significantly
contribute to customer satisfaction and sustainable d estination image through personalization and
efficient service delivery. Virtual tools provide their most appropriate options and address customer
requests to managers, thus providing a convenient and quality experience for customers. The integration of
Geographic Information Systems (GIS) in tourism as demonstrated in the case of Ulytau National Park
contributes to a more personalized and enriched visitor experience (Amangeldi et al., 2025).
2 Increasing visibility and marketing Virtual tools, such as websites, social media and other mobile platforms, increased business visibility and market destinations in line with customer expectations.
3
Facilitation of
reservations, through
process automation
The selection and processing in  real time of customer requests for the services required, offers the
opportunity for businesses to offer personalized services according to the customer's preferences,
making the customer experience within his expectations. (Yang et al, 2024).
4 Personalized customer experiences The selection and processing in real time of customer requests for the services required, offers the opportunity for businesses to offer personalized services according to the customer's preferences, making the customer experience within his expectations. (Yang et al., 2024).
5 Effective customer relationship management The use of AI and other technological tools offers the possibility of good customer relationship management, providing them with the required security and reliability. (Huang et al., 2017).
6 Data collection and analysis Businesses have the convenience of collecting and analyzing data and customer behavior, which serve to improve the quality of service and assist in the decision -making process and long -term business strategies (Abdul-Azeez et al., 2024)
7 Cost reduction Automating administrative and operational processes through technology reduces the costs of human resources and manual data management.
8 Increased access to global markets Online platforms and digital promotional tools enable businesses to more easily reach customers from international markets.
9 Real-time communication Digital platforms offer the possibility of real -time communication with customers, ensuring fast and effective service
1
0 Security
AI systems detect suspicious behavior and alert security authorities, reducing the risk of crime within
the business or tourist destination. For example, (Dziurakh et al., 2024) present an intrusion detection
solution specifically designed for s mart tourism environments, using anomaly detection to identify and
report potentially harmful behavior in real time.

The use of online tools, such as mobile applications, websites, digital marketing platforms, have increased the visibility
of businesses and their attendance at the international level. With the use of technology, businesses can now collect and
analyze useful information about how their customers behave, allowing them to make well-informed decisions and improve
their products depending on market demands. As highlighted by (Nathan et al., 2020), platforms like Airbnb not only

Anxhela KOSTA, Florina PAZARI, Ilma LILI, Silvana GRECA

 1490
facilitate booking but also cont ribute to increasing destination visibility and enhancing tourist engagement through digital
interaction. Some of the advantages presented in table number 2 were identified through surveys conducted with selected
businesses. These businesses described the benefits they experienced from using technology, including improved operational
efficiency and management, increased business promotion and access to international markets, enhanced customer
communication, and expanded clientele—ultimately leading to increased financial income (Smart Tours Bird Albania).

3. Development of an AI-based hotel recommendation system
Durrës, one of the most popular seaside resorts in Albania, boasts a great selection of hotels to suit all tastes and
budgets. With new hotels open ing every year, visitors are typically faced with an overwhelming choice. Naturally, as a
matter of priority when selecting a hotel, most of the visitors would prefer comfort, cleanliness, location, and quality of
service to have a good time. The most effe ctive way of judging the quality of a hotel is by remarks, especially Google
reviewers, of former clients on their experience. They are an important component of tourists' decisions since they are
honest opinions about the strengths and weaknesses of each hotel. As customer reviews are an important factor in selecting
a hotel, our aim is to create an intelligent recommendation system that utilizes Google reviews to classify and rate hotels on
the basis of sentiment analysis and star ratings. This way, trave lers will have fact -based guidance to make in selecting the
most suitable hotel from an actual user perspective, instead of relying on advertisements only or personal assumptions.

Proposed Method / Approach
As the first step towards developing a useful re commendation system, our approach will involve fetching actual current
reviews for hotels from Google. We will do this through two likely means which we will utilize:
a. Option 1: Using Google places API: Google Places API allows us to web scrape information about hotels,
including name, address, ratings, and reviews. We will retrieve hotel reviews by making API requests, which we will then
put in a nicely formatted manner. The API allows us to get data quickly and reliably without any chance of getting blocked.
b. Option 2: Web Scraping with Selenium: In case API limits the amount of reviews scraped, Selenium can be used
to automate browsing and scrape reviews directly from Google. Selenium can mimic human activity (scrolling, clicks) to
compile all available rev iews. This is useful but will most certainly require additional caution for CAPTCHA and anti -
scraping protection. The specific Python script used for this purpose is shown in Algorithm 1.

Algorithm 1:  Selenium code for crawling the data from reviews of google
iimport pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

hotel_reviews_links = {
   "KLAJDI RESORT Durres":
"https://www.google.com/travel/search?q=KLAJDI%20RESORT%20Durres&ap=ugEHcmV2aWV3cw",
   "FAFA RESORT Durres":
"https://www.google.com/travel/search?q=FAFA%20RESORT%20Durres%22&ap=aAG6AQhvdmVydmlldw",
   "SUPREME HOTEL Durres":
"https://www.google.com/travel/search?q=supreme+hotel+durres&ap=ugEHcmV2aWV3cw",
   "PINEA HOTEL Durres":
"https://www.google.com/search?q=PINEA+HOTEL+Durres%22#lrd=0x134fdf0fa9b7ccb9:0x3943ecc0855608ca,1,,,,",
   "BRILLIANT HOTEL AND SPA Durres":
"https://www.google.com/travel/search?q=BRILLIANT%20HOTEL%20AND%20SPA%20Durres%22&ap=ugEHcmV2
aWV3cw"
}
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")
s)
     if not df_reviews.empty:
   df_reviews.to_excel("Durres_Hotel_Reviews.xlsx", index=False)
   print("File saved to 'Durres_Hotel_Reviews.xlsx'!")
else:
driver.quit()

After Selenium we got the excel file that has collected all the reviews we need containing the following key columns
(Review_ID: Unique identifier for each review., User_ID : User who posted the review., name_hotel: Name of the hotel.,
Hotel_ID: Unique hotel identifier., Review_Text: The actual review content., Rating: Numerical rating given to the hotel.)
These extracted reviews and their key attributes are illustrated in Figure 3.

The Role of Artificial Intelligence in Transforming Tourism Services: The Case of Durrës, Albania

 1491

Figure 3. Sample of extracted hotel reviews (comment) from Google using
Selenium automation for hotels in Durrës (Source: Reviews collected by google using Selenium)

Based on reviews to assess customer satisfaction levels, we applied Sentimen t Analysis using the TextBlob NLP
library. Each review was classified into one of three categories:
- Positive comments whose polarity value is greater than 0.1 (i.e., "The hotel was great, staff were very friendly").
- Neutral: Reviews with a polarity score between -0.1 and 0.1 (like "The hotel was okay, nothing special").
- Negative: Reviews with a polarity score less than -0.1 (e.g., "Rooms were dirty and the staff was rude"). The
sentiment categorization allowed us to rule out hotels with mostly negative rev iews and prefer those with positive
sentiment. The sentiment categorization allowed us to rule out hotels with mostly negative reviews and prefer those with
positive sentiment. The Python code used to perform this classification is presented in Algorithm 2.

Algorithm 2: Classification of the hotels based on reviews
iimport pandas as pd
from textblob import TextBlob
file_path = "Durres_Hotel_Reviews.xlsx"
df_reviews = pd.read_excel(file_path)
def analyze_sentiment(text):
   blob = TextBlob(str(text))
   polarity = blob.sentiment.polarity
   if polarity > 0.1:
       return "Positive"
   elif polarity < -0.1:
       return "Negative"
   else:
       return "Neutral"
df_reviews["Sentiment"] = df_reviews["Review_Text"].apply(analyze_sentiment)
output_file = "Durres_Hotel_Reviews_With_Sentiment.xlsx"
df_reviews.to_excel(output_file, index=False)
print(df_reviews[["name_hotel", "Review_Text", "Rating", "Sentiment"]].head())
print(f"\n Updated file saved as: {output_file}")

Figure 4 illustrates the output results of the sentiment analysis, where each review is categorized based on its polarity as
positive, neutral, or negative. To improve the efficiency of this process, we developed an AI -driven hotel recommendation
system that analyzes customer reviews and rec ommends hotels depending on review sentiment and text similarity. This
system merges Natural Language Processing (NLP) techniques to classify the reviews in terms of their quality and machine
learning algorithms to rank the top hotel options (Sancho Núñez et al., 2024).

Anxhela KOSTA, Florina PAZARI, Ilma LILI, Silvana GRECA

 1492

     Figure 4. Sentiment classification of hotel reviews using TextBlob analysis (Source: Generated by sentiment classification algorithm)

from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

We shifted our focus from sentiment analysis to translate text reviews to numeric format through Term Frequency -
Inverse Document Frequency (TF -IDF). TF-IDF approximates the significance of the word based on how often a word is
repeated in the dataset to al low the system to quickly identify patterns and cluster similar reviews. TF -IDF vectorization
allowed us to transform text data into numerically formatted numeric features such that we could measure proximity
between dissimilar reviews. Using cosine similarity, we proceeded to calculate the similarity of hotel reviews in a way that
we would be able to know how similar or different hotels were based on customer reviews (Wang et al., 2023). In order to
give personal recommendations, the system follows the fol lowing process: the user selects first a hotel of interest, the
algorithm searches for hotels with similar reviews based on TF-IDF similarity scores. The recommendations are then filtered
again by removing hotels that have the majority of negative reviews,  and only retaining those with the majority of positive
reviews. Finally, the AI system ranks and presents the top three most suitable hotels, offering personalized suggestions based
on real customer reviews and their semantic similarity as shown in Figure  5. By automating this process through artificial
intelligence techniques such as sentiment analysis and similarity scoring, the system significantly improves operational
efficiency, reduces manual workload, and supports faster, data-driven decision-making in the hotel selection process.

Figure 5. AI-based hotel recommendations using sentiment and review similarity

RESULTS AND INTERPRETATION
After executing the model on our data, we observed the following patterns:
● Hotels with a higher rating (4.0+) had a more positive sentiment.
● TF-IDF similarity scores helped us identify hotels with comparable guest experiences.

The Role of Artificial Intelligence in Transforming Tourism Services: The Case of Durrës, Albania

 1493
● The system effectively excluded hotels with an overabundance of negative reviews to maximize customer
satisfaction. Using AI -powered review analysis, we demonstrated that text -based hotel recommendations provide more
personalized and reliable suggestions compared to conventional rating -based filters. Figure 5 presents the final output of
the AI-driven recommendation system, which ranks hotels based on textual review similarity and sentiment analysis. By
combining TF -IDF vectorization with cosine similarity and filtering through sentiment scores, the system is able to
suggest the most relevant and positively  rated hotels.

DISCUSSION
This article proves that technology has indeed played a deep role in showing positive effects in the cause of developing
the tourism industry, in particular, in the hotel sector and the tourism sector in Albania. Based on the su rveys and
interviews conducted with the existing businesses in this field, including Brilliant Hotel and Spa, Klajdi Resort, Fafa
Resort, Supreme Hotel, and Pinea Hotel, market analysis points out that most of these entities have already employed
technological tools and platforms to enhance their service quality. Reservation management, online payment systems and
customer communication have all moved towards automating processes through digital platforms. The integration of
Artificial Intelligence (AI) in t ourism services has significant potential to improve operations by automating repetitive
tasks, allowing human resources to focus on delivering more personalized experiences. AI -enabled applications, such as
customer service chatbots and online booking sys tems, might be developed to enhance the productivity and efficiency of
services provided to a client. An extension of the above research suggests an AI-driven hotel recommendation system based
on the reviews by customers for better decision -making by a tou rist. The system applies Natural Language Processing
techniques, like sentiment analysis and TF -IDF-based text similarity to process the reviews from the guests to rank the
hotels. In that respect, the system can suggest a few hotels having equivalent posi tive experiences as perceived by their
guests with the help of Cosine Similarity, hence facilitating the traveling user in his choice. It does result in showing dat a-
based hospitality selections that build greater transparency over businesses' business, making attraction for more consumers
and bringing together a business from their customers more efficiently through presenting the positive features of the
respective services. Study data showed positive trends regarding reliance on technology toward greater business appearance
through website use and social networks to make places more accessible that attract tourists visiting such destinations along
with creating favorable experience for clientele. Many companies also showed improved operational efficiency and
increased competitiveness in the global arena. However, most of them pointed out difficulties involving high cost in
introducing newly advanced technologies and necessary training for specialized manpower. These are considered as
barriers to the adoption of technology, especially on the part of small businesses or firms with minimal finances.

CONCLUSION
Findings from this study indicate that technology is a salient factor for continuous development of tourism in Albania. It
is viewed as a necessary t ool by businesses not only to improve existing services but also to innovate new products and
offerings. Technology has redefined new pathways for growth and improvement, thereby providing avenues for
international interactions, thereby enhancing the overall quality of tourism offerings of the country. The example of an AI -
powered recommendation system also shows how machine learning and data -informative decision-making serve as forces
in pushing digitalization in the tourism sector. Summing up, this is a sure impact of technology on the tourism sector, while
businesses that seize these innovations and especially with AI implement automation of service, personal experience for
guests, and improve their marketing strategies greatly benefit in expansion and gr owth to contribute to the sustainable
development of tourism in Albania. This study is not without limitations. The research focused on a limited number of
resorts in Durrës, Albania, which may limit the generalizability of the findings to the broader tour ism sector or to other
regions. The data collected relied heavily on self -reported responses and publicly available ratings, which may carry
subjective biases. In addition, the proposed AI -powered hotel recommendation system was not deployed in a real -world
commercial environment, so its effectiveness was not validated in direct user conditions. The study also did not address
long-term implications, such as financial sustainability or return on investment of AI and smart tourism technologies.
Future research should expand the geographical scope, incorporate longitudinal methods, and aim to quantify the economic
impact of technology adoption in tourism, particularly in relation to artificial intelligence and service automation.

Recommendations
This paper is recommended to all businesses operating in the tourism sector, with the aim of helping them understand the
importance and benefits of adopting technology to further develop their services and attract a greater number of tourists. The
results of this study  can assist these businesses in improving their internal processes and increasing their presence in
international markets through digital platforms. Besides, businesses must consider adopting AI-based tools, such as automated
review analysis and recommenda tion systems, to enhance customer satisfaction, optimize service delivery, and increase
operational efficiency. Additionally, this paper is recommended to local and central institutions to value the positive impact
that technology has on the tourism indust ry. Governments and policymakers must promote digital innovation in tourism by
funding research and development of AI, subsidizing technology take -up for small and medium -sized enterprises, and
enhancing digital literacy training for tourism professionals.  Promoting the use of AI -driven recommendation systems by
companies can help ensure online hotel review transparency, build customer trust, and provide a more enjoyable experience
for tourists. By investing in AI -based solutions, businesses and institutions can make Albania more competitive as a tourist
destination, promoting sustainable development and long-term performance within the global tourism sector.

Anxhela KOSTA, Florina PAZARI, Ilma LILI, Silvana GRECA

 1494
Author Contributions: Conceptualization, A.K., F.P and I.L; methodology, A.K and F.P.; software, A.K, I.L  and S.G.;
validation, A.K. and F.P.; formal analysis, A.K, F.P. and S.G.; investigation, I.L. and S.G.; data curation, A.K  and F.P.;
writing - original draft preparation, A.K and F.P; writing - review and editing, A.K. and F.G.; visualization, I.L  and S.G.;
supervision, A.K.; project administration, A.K. All authors have read and agreed to the published version of the manuscript.

Funding: Not applicable.

Institutional Review Board Statement: Not applicable.

Informed Consent Statement: Not applicable.

Data Availability Statement: The data presented in this study may be obtained on request from the corresponding author.

Acknowledgements: We thank the Durr ës businesses that participated in this study. Their feedback and insights were
invaluable to us. We also acknowledge the application of AI tools in aiding data analysis, sentiment determination, and
content fine tuning, which significantly contributed to the precision and validity of our findings.

Conflicts of Interest: The authors declare no conflict of interest.

 REFERENCES
Buhalis, D., & Leung, D. (2018). Smart hospitality Interconnectivity and interoperability towards an ecosystem. International Journal of
Hospitality Management, 71, 41-50. http://dx.doi.org/10.1016/j.ijhm.2017.11.011
Gretzel, U., Sigala, M., Xiang, Z., & Koo, C. (2015). Smart tourism: Foundations and developments. Electronic Markets, 25 (3), 179–
188. https://doi.org/10.1007/s12525-015-0196-8
Neuhofer, B., Buhalis, D., & Ladkin, A. (2015). Technology as a catalyst of change: Enablers and barriers of the tourist experience and their
transformative power. Journal of Hospitality & Tourism Research, 39(4), 1053-1070. http://dx.doi.org/10.1007/978-3-319-14343-9_57
Huang, C. D., Goo, J., Nam, K., & Yoo, C. W. (2017). Smart tourism technologies in travel planning: The role of exploration and
exploitation. Information & Management, 54(6), 757–770. https://doi.org/10.1016/j.im.2016.11.010
Kieanwatana, K., & Vongvit, R. (2024). Virtual reality in tourism: The impact of virtual experiences and destination image on the travel
intention. https://doi.org/10.1016/j.rineng.2024.103650
Guttentag, D. A. (2010). Virtual reality: Applications and implications for tourism. http://dx.doi.org/10.1016/j.tourman.2009.07.003
Kannan, R., & Antony, P. J. (2024). Revolutionizing the tourism industry through artificial intelligence: A comprehensive review of AI
integration, impact on customer experience, operational efficiency, and future trends. https://www.researchgate.net/ publication/379412126
Xiang, Z., & Fesenmaier, D. R. (2017). Big data analytics, tourism design, and smart tourism. Springer International Publishing , 299-
307. http://dx.doi.org/10.1007/978-3-319-44263-1_17
Mariani, M., Baggio, R., Fuchs, M., & Höepken, W. (2018). Business intelligence and big data in hospitality and tourism: A sy stematic
literature review. International Journal of Information Management, 54, 401-421. http://dx.doi.org/10.1108/IJCHM-07-2017-0461
Tussyadiah, I. P., & Wang, D. (2016). Tourists attitudes toward proactive smartphone systems. Journal of Travel Research,  55(4), 493-
508. http://dx.doi.org/10.1177/0047287514563168
Slevitch, L., Chandrasekera, T., & Drew Sealy, M. (2020). Comparison of Virtual Reality Visualizations with Traditional Visua lizations
in Hotel Settings. Journal of 765 Hospitality & Tourism Research, 46(1). http://dx.doi.org/10.1177/1096348020957067
Ivancsóné Horváth, Z., Raffay, Z., & Happ, É. (2025). Digitalisation in angling tourism: Introducing new  technologies to a traditional
tourism product. Geojournal of Tourism and Geosites, 58(1), 42–51. https://doi.org/10.30892/gtg.58104-1389
Tussyadiah, I., & Park, S. (2017). Consumer Evaluation of Hotel Service Robots. Information and Communication Technologies in
Tourism. http://dx.doi.org/10.1007/978-3-319-72923-7_24
Czyz, M., & Javed, M. (2025). Revolutionizing travel: The role of  smart tourism technologies in enhancing tourist satisfaction and
shaping sustainable destination images: Insights from Istanbul. Geojournal of Tourism and Geosites, 58(1), 446– 455. https://doi.org/
10.30892/gtg.58141-1426
Amangeldi, A., Seidualin, D., Mukanov, A., Mukatova, R., Bilisbekov, T., & Sagatbayev, Y. (2025). Innovative technologies to improve
tourism experience in national parks: development of GIS maps and their value. Geojournal of Tourism and Geosites , 58(1), 210 –
224. https://doi.org/10.30892/gtg.58118-1403
Sousa, A. E., Cardoso, P., & Dias, F. (2024). The use of Artificial Intelligence systems in tourism and ho spitality. A Global Perspective
on the Hospitality and Tourism Industry. https://doi.org/10.3390/admsci14080165
Nongkhoo, A., Sitthiwarongchai, C., & Janmuangthai, W.  (2025). The Application of Ar tificial Intelligence technology innovation in
tourism. Ramkhamhaeng International Journal of Science and Technology, 8(1): 94-104.
Dziurakh, Y., et al. (2024). Intrusion Detection Systems for Smart Tourism Platforms: Safeguarding Food Safety and User Priv acy.
Journal of Internet Services and Information Security, 14(4), 484–498. https://doi.org/10.58346/JISIS.2024.I4.030
Nathan, R. J., Victor, V., Tan, M., & Fekete -Farkas, M. (2020). Tourists’ use of Airbnb app for visiting a historical city. Information
Technology & Tourism, 22(2), 217–242. https://doi.org/10.1007/s40558-020-00176-0
Yang, X., Zhang, L., & Feng, Z. (2024). Personaliz ed tourism recommendations and the e -tourism user experience. Journal of Travel
Research, 63(5), 1183–1200. https://doi.org/10.1177/00472875231187332
Abdul-Azeez, O., Ihechere, A. O., & Idemudia, C. (2024). Enhancing business performance: The role of data-driven analytics in strategic decision-
making. International Journal of Management & Entrepreneurship Research, 6(7), 2066–2081. https://doi.org/10.51594/ijmer.v6i7.1257
Sancho Núñez, J. C., Gómez -Pulido, J. A., & Robina Ramírez, R. (2024). Machine learning applied to tourism: A systematic review.
Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 14(5), Article e1549. https://doi.org/10.1002/widm.1549
Wang, E., Chen, Y., & Li, Y. (2023). Research on a hotel collaborative filtering recommendation algorithm based on the probab ilistic
language term set. Mathematics, 11(19), 4106. https://doi.org/10.3390/math11194106
National Authority for Cyber Security. (2025). Home. https://aksk.gov.al/en/home-2/
Smart Tours Bird Albania - https://smart-tour.bird.al/

Article history: Received: 17.03.2025 Revised: 18.06.2025 Accepted: 04.07.2025 Available online: 24.07.2025
