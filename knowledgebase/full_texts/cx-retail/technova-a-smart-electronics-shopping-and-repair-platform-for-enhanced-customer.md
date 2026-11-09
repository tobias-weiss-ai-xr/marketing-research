---
title: 'TechNova: A Smart Electronics Shopping and Repair Platform for Enhanced Customer Experience'
url: https://doi.org/10.52098/airdj.20266378
category: cx-retail
subcategory: review
date: 2026-08
venue: Artificial Intelligence & Robotics Development Journal
authors:
- Aaisha S. AlShibli
- Asaad Al-Roshdi
- Ali Al-Bahrani
source: openalex-oa
pdf_url: https://testojs.acaa-p.com/index.php/AIRDJ/article/download/78/33
pages: 16
chars: 38879
fetched_at: '2026-11-08T18:44:25+00:00'
kb_version: 1
---

# TechNova: A Smart Electronics Shopping and Repair Platform for Enhanced Customer Experience

Artificial Intelligence & Robotics Development Journal
Volume 6, Issue 3, pp 450-465, July 2026, https://doi.org/10.52098/airdj.20266378
ISSN: 2788-9696  Received: 2/5/2026  Revised: 20/7/2026  Accepted: 22/8/2026

TechNova: A Smart Electronics Shopping and Repair
Platform for Enhanced Customer Experience
Aaisha S. AlShibli 1*, Asaad Al-Roshdi 2, Ali Al-Bahrani 3, Hamed Al-Orimi4, Salem Al-Hinai 5
1, 2,3,4,5 University of Technology and Applied Science-Suhar Branch, DCIS
*Corresponding author: Aaisha S. AlShibli 1, Aaisha.AlShibli@utas.edu.om.

Abstract
 This paper aims to provide a Smart Electronics Shopping and Repair Platform, an integrated online system
designed to enhance the efficiency and reliability of purchasing and maintaining electronic devices. This study
addresses the critical challenge of insufficient and unreliable product information on existing e -commerce platforms,
which often leads to ineffective user decision -making. The proposed platform provides comprehensive and accurate
details, including technical specifications, pricing, warranty i nformation, and verified customer reviews for products
such as smartphones, smartwatches, and laptops. The system was designed and implemented using a structured
development methodology, employing HTML for the front -end interface, PHP for server -side processing, and SQL
for database management. Emphasis was placed on usability, system performance, and data accuracy through
systematic testing and validation processes. In addition, a dedicated repair module was incorporated to enable users
to submit maintenance requests, thereby extending the platform’s functionality beyond conventional online shopping
systems. The results indicate that TechNova significantly improves user experience by delivering reliable product
information, simplifying the decision -making p rocess, and increasing overall user satisfaction. Furthermore,
integrating repair services enhances platform effectiveness and promotes customer retention. The findings
demonstrate that TechNova provides a robust, user-centered solution that effectively bridges the gap between product
selection and after-sales support in the electronics domain.

Keywords: Smart Shopping, web-based systems, e-commerce systems, user-centered solutions.

451

1. Introduction
T Smart shopping has revolutionized how consumers buy electronic devices in terms of ease, clarity, and
information. Consumers have the ability to compare products, study their specifications and make informed decisions
on purchases, and be sure of receiving  good after-sales services, thus making shopping a smooth process for the
consumer (AbdulMalik & Yousif, 2021). echNova: Smart Electronics Shopping and Repair Platform is a web -based
system designed to improve the process of purchasing electronic devices while integrating post -purchase repair
services within a single platform. The system provides users with access t o a wide range of electronic products,
including smartphones, smartwatches, and laptops, along with detailed and reliable information to support informed
decision-making.
In the current digital marketplace, users often encounter challenges when selecting appropriate electronic products
due to incomplete, inconsistent, or unreliable information available on many e-commerce platforms (Vyas et al., 2023).
This lack of transparency can lead to poor purchasing decisions and reduced user satisfaction. Additionally, most
existing platforms do not offer integrated repair services, forcing users to rely on external providers for maintenance
and support, which can be inefficient and inconvenient. To address these issues, TechNova proposes a comprehensive
solution that combines an online shopping system with a dedicated repair service module. The platform delivers
accurate product specifications, pricing details, warranty information, and customer r eviews in a user -friendly
interface. The system is developed using HTML for front -end design, PHP for backend processing, and SQL for
database management, ensuring efficient data handling and system performance. The main objectives of this study are
to develop a user -centered platform that enhances the online shopping experience, provide reliable and complete
product information, integrate repair and maintenance services, and improve overall user satisfaction through efficient
and accessible system design.

2. Literature Review

The rapid evolution of e -commerce has fundamentally reshaped the way consumers search for, evaluate, and
purchase electronic devices. Modern e -commerce systems have evolved beyond simple online stores into integrated
digital business platforms that combine  product information, customer interaction, secure payment systems, and
logistics management (Turban et al., 2018). With the increasing reliance on digital platforms, users now expect not
only a wide variety of products but also accurate information, compe titive pricing, and seamless user experiences.
Major platforms such as Amazon and Noon have set high standards by offering extensive product catalogs,
personalized recommendations, and efficient logistics systems. Similarly, regional retailers like Jumbo E lectronics
have adopted omnichannel strategies to enhance customer engagement. However, despite these advancements,
significant challenges remain, particularly in ensuring the reliability of product information and providing
comprehensive after-sales services. Many existing platforms primarily focus on facilitating transactions rather than
supporting the full product lifecycle, especially in terms of repair and maintenance. This gap highlights the need for
more integrated and user -centered solutions. Theref ore, this study explores existing e -commerce platforms and
identifies their limitations as a foundation for proposing TechNova, a system designed to combine product purchasing
with repair service management in a unified platform.  The rapid growth of e -commerce platforms has significantly

                                                                        452

transformed how consumers purchase electronic devices. Large platforms such as Amazon and eBay provide extensive
product catalogs, competitive pricing, and user -generated reviews. However, despite their popularity, several studies
indicate that users still face challenges related to inconsistent product information and difficulty in evaluating product
reliability (Laudon & Traver, 2022; Wells et al., 2011). Amazon is one of the world’s leading e-commerce platforms,
offering a vast selection of electronic devices such as smartphones, laptops, tablets, and smartwatches  (Combe, C.,
2002; Hamill, J, 1998; Cui, T. H., 2022; Sawan, A. S.,  2024). The platform provides detailed product descriptions,
technical specifications, competitive pricing, and customer reviews, which support users in making informed
purchasing decisions ( Laudon & Traver, 2022 ; Wells et al., 2011). Additionally, Amazon utilizes advanced
recommendation systems and personalized features to enhance the user experience and increase customer engagement
(Verhoef et al., 2015 ; Egodawele et al., 2022). Its efficient logistics network and customer -centric approach have
significantly influenced the evolution of modern retail and online shopping practices (Grewal et al., 2017).  Despite
these advantages, Amazon primarily focuses on product sales and distribution rather than comprehensive after -sales
services. While return policies, refunds, and limited warranty support are available, repair services are typically
handled by manufa cturers or third -party providers rather than the platform itself ( Almtiri, 202 1). This limitation
highlights a gap in integrated e -commerce solutions, particularly for users seeking convenient and centralized repair
services alongside purchasing options (Stone, 2013).  Noon is a prominent e-commerce platform operating across the
Middle East, offering a wide range of electronic products such as smartphones, laptops, tablets, and smartwatches.
The platform provides detailed product descriptions, specifications, competitive  pricing, and frequent promotional
discounts, enabling customers to make informed purchasing decisions. In addition, Noon supports localized services
including multiple payment options —such as cash on delivery —and efficient regional delivery systems, which
enhance accessibility and convenience for users in the Gulf region (Combe, C , 2002; Laudon & Traver, 2022) .
Furthermore, Noon leverages user reviews and ratings to improve transparency and trust, while its digital interface is
designed to offer a seamless and user-friendly shopping experience. The platform also contributes to the growth of e-
commerce in the regi on by addressing local consumer preferences and logistics challenges (Grewal et al., 2017;
Verhoef et al., 2015). However, despite its strong retail capabilities, Noon primarily concentrates on product sales and
marketplace operations rather than comprehensive after -sales services. While customers may benefit from return
policies or limited warranty support, the platf orm does not typically provide integrated or free repair services for
damaged electronic devices. This limitation highlights an opportunity for more holistic platforms that combine both
purchasing and maintenance services within a single ecosystem (Stone, 2013). Noon has rapidly emerged as a leading
e-commerce platform in the Middle East, offering a wide range of products and localized services tailored to regional
consumers (Momani, 2026; Traoret, 2024). The platform was launched in 2017 with strong regional backing and a
focus on building an Arabic -first digital marketplace ( Momani, 2026). Furthermore, Noon’s investment in logistics
infrastructure and fulfillment systems has contributed significantly to its growth and competitiveness in the regional
market (Traoret et al., 2024; Elamin et al., 2025). Jumbo Electronics is a well-established consumer electronics retailer
in the United Arab Emirates, operating within one of the region's most dynamic retail markets. The continued
expansion of the UAE retail sector has been driven by economic diversification, digital transformation, and increasing
consumer demand for omnichannel shopping experiences (Nandwa & Al Ameemi, 2016). Jumbo Electronics offers a

                                                                        453

wide range of products including smartphones, laptops, tablets, home appliances, and accessories through both
physical stores and its online platform. The company provides detailed product information, technical specifications,
competitive pricing, and after -sales support such as manufacturer warranties and customer service assistance, which
help consumers make informed purchasing decisions (Khan et al., 2026; Laudon & Traver, 2022). In addition, Jumbo
Electronics has developed a strong reputation in the regional retail market by integrating in -store experiences with
digital shopping channels, reflecting the growing trend toward omni -channel retailing (Verhoef et al., 2015).
Furthermore, the company offers repair and maintenance services for electronic devices; however, these services are
typically fee-based and depend on the product type and warranty conditions. While such services ensure professional
maintenance and support, they may not always be cost-effective or easily accessible for all customers (Grewal et al.,
2017). In contrast, the proposed TechNova platform introduces a more customer-centric approach by integrating both
e-commerce and after -sales support into a single system. Unlike traditional retailers such as Jumbo Electronics,
TechNova aims to provide free repair services for damaged devices, thereby addressing a significant gap in the market
and enhancing customer convenience and satisfaction. This approach highlights the shift toward more comprehensive
and service-oriented digital platforms in the electronics retail sector (Stone, 2013).  Electronics retailers in the UAE,
such as Jumbo Electronics, operate within a rapidly evolving market characterized by strong digital transformation
and increasing consumer demand for integrated shopping experiences ( Khan et al. , 202 6; Barbado, 202 0). The
adoption of omnichannel strategies and enhanced customer service models has become essential for maintaining
competitiveness in the sector (Brynjolfsson et al., 2013; Pantano & Timmermans, 2014).
Research in e-commerce systems highlights that user trust is strongly influenced by transparency, completeness
of product information, perceived value, and the availability of verified customer reviews, all of which contribute to
customer satisfaction and purchasing decisions (Kotler & Keller, 2020; Koufaris, 2002).  Inaccurate or incomplete
information often leads to poor purchasing decisions and increased return rates (Koufaris, 2002). Additionally, most
existing platforms focus primarily on sales transactions, with limited integration of after -sales services such as repair
and maintenance support. From a design perspective, studies in Human-Computer Interaction emphasize that usability
and interface simplicity significantly enhance user satisfaction and system effectiveness (Brooke,1996; Lewis, 2018).
A well-structured interface allows users to navigate easily, compare products efficiently, and complete tasks with
minimal cognitive effort.
In conclusion, while leading e -commerce platforms such as Amazon and Noon, along with established retailers
like Jumbo Electronics, have significantly advanced online shopping experience through improved accessibility,
product variety, and user engagement, they still exhibit notable limitations. These systems largely emphasize sales
and distribution, with limited integration of after -sales services such as repair and m aintenance. Additionally, issues
related to inconsistent product information and user trust continue to affect consumer decision -making. The analysis
of existing literature reveals a clear gap in the development of comprehensive e-commerce solutions that address both
pre-purchase and post -purchase needs. In response to this gap, the proposed TechNova platform aims to deliver a
more holistic approach by integrating reliable product information, user-friendly design, and free repair services within
a single system. This approach not only enhances user satisfaction but also reflects the future direction of e-commerce
toward more service-oriented and customer-centric platforms.

                                                                        454

3. Methodology

The development of TechNova: Smart Electronics Shopping and Repair Platform follows a structured system
design approach to ensure efficiency, reliability, and usability. The methodology consists of several key phases,
including data collection and analysis, system design, implementation, and testing.

3.1 Data Collection and Analysis

Data for this study were collected using a structured online questionnaire developed through Google Forms. The
survey link was distributed electronically to participants and remained accessible for a period of one week. A total of
40 respondents completed the questionnaire. The instrument consisted of multiple -choice and Likert-scale questions
designed to examine consumers’ purchasing behavior toward electronic devices, as well as the key factors influencing
their decision-making processes. The data collected were systematically analyzed, and responses for each question
were summarized using descriptive statistics (Yousif et al., 2021). The results were then presented through graphs and
charts to provide clear and visually accessible insights into participant responses. These visual representations
facilitated the identification of dominant trends, patterns, and user preferences.   Figure shows the  Frequency of
Purchasing Electronic Devices. The findings indicate that half of the respondents (50%) purchase electronic devices
once a year or less, while 25% purchase devices two to three times annually, and another 25% purchase more than
three times per year. Overall, the results demonstrate that many consumers make electronic device purchases relatively
infrequently.

Figure 1: Purchasing Electronic Devices

Figure 2  presents types of Electronic Devices Purchased  results that show the Smartphones emerged as the most
purchased devices, selected by 57.5% of respondents (23 participants). This was followed by other electronic devices
(42.5%), accessories (40%), and laptops (37.5%). Smartwatches were the least purchased category, with only 15% of
respondents. These findings highlight the dominant demand for smartphones compared to other device categories.

                                                                        455

Figure 2: Types of Electronic Devices Purchased

Figure 3 present Factors Influencing Purchase Decisions  such as Price that identified as the most influential factor,
reported by 62.5% of respondents, closely followed by brand preference (60%). Technical specifications were
important for 45% of participants, while design and appearance influenced 35%. User reviews affected 27. 5% of
respondents, whereas warranty and after -sales services were considered the least important factor (17.5%). This
suggests that economic and brand-related considerations outweigh service-related aspects in purchase decisions.

Figure 3: Factors Influencing Purchase Decisions

Figure 4 shows that most respondents (67.5%) indicated that finding accurate product specifications online is either
easy (47.5%) or very easy (20%). However, a notable proportion (32.5%) reported difficulties, indicating that
challenges in accessing reliable information persist for a significant segment of users.

                                                                        456

Figure 4: Ease of Finding Accurate Product Information

Figure 5 presents the trust in online reviews appears to be limited. More than half of the respondents (52.5%) stated
that they trust reviews only occasionally depending on the platform, while 25% rarely trust them. Only 12.5%
expressed consistent trust, and 10% reported no trust at all. These findings reflect a general skepticism toward online
review systems.

Figure 5: Trust in Online Reviews

Figure 6 exposes that the most prominent issue identified was the lack of trust in reviews (50%), followed by unclear
or inconsistent product specifications (40%). Price inconsistencies and insufficient warranty information were
reported by 35% of respondents. Additional concerns included general usability issues (30%) and difficulties in
comparing products (22.5%). These challenges highlight critical limitations in current e -commerce platforms.

                                                                        457

Figure 6: Challenges Faced in Online Shopping

Figure 7 shows that respondents emphasized the need for enhanced platform features, with filtering and sorting options
ranking highest (45%). Accurate product specifications, clear price comparisons, and verified reviews were each
selected by 42.5% of participants. Product com parison tools and warranty details were requested by 32.5%, while
22.5% highlighted the need for a repair request feature. These results indicate strong demand for improved
transparency and usability.

Figure 7: Desired Features in E-Commerce Platforms

Figure 8 indicates that most respondents expressed willingness to use a repair request feature, with 47.5% indicating
they are likely to use it and 15% very likely. Conversely, 27.5% were unlikely, and 10% were very unlikely. Overall,
the findings suggest a generally positive attitude toward integrating repair services within e-commerce platforms.

                                                                        458

Figure 8: Interest in Repair Request Feature

Figure 9  presents the  Most Important Platform Features  such as Price transparency and comparison tools were
identified as the top priority (35%), followed by trustworthy and verified reviews (27.5%). Accurate specifications
and warranty information were equally valued by 15% of respondents, while the repair request feature was considered
the primary priority by 7.5%. These results emphasize the importance of clarity and reliability in user decision-making.

Figure 9: Most Important Platform Features

Figure 10 presents the Willingness rate to Purchase from Platforms Offering Repair Services. A strong majority (65%)
indicated a willingness to purchase from platforms that provide repair services, while 30% expressed conditional
interest (“maybe”), and only 5% rejected the idea. This demonstrates a clear market preference for integrated service

                                                                        459

solutions.

Figure 10: Willingness to Purchase from Platforms Offering Repair Services

Figure 11 shows that the Preferred Customer Support Communication Channels is Chat-based with rate of (32.5%),
closely followed by phone support (30%). Email was preferred by 20% of respondents, while 17.5% reported no
specific preference. This suggests a growing inclination toward instant and interactive support methods.

Figure 11: Preferred Customer Support Channels

In the design phase, the system architecture was defined to support both the e -commerce and repair service
functionalities. The platform was structured into two main modules: the product management module and the repair
service module. The user interface was designed using HTML to ensure a clear, responsive, and user-friendly layout.
Figure 12 illustrates a data flow diagram (DFD) for an integrated e-commerce and repair management system, showing
the interaction between users, system processes, and data storage components. On the left side, the Customer interacts
with the system through a sequence of core processes. The workflow begins with (1) Browse Products, where users
can view available electronic items stored in the Products database (D1). After selecting an item, the user proceeds to
(2) Place Order, where order details are generated and stored in the Orders database (D2). Following purchase, the

                                                                        460

customer can (3) Submit Review, which contributes feedback linked to product and order information, improving
system transparency and supporting future customer decisions.  The system then transitions to administrative and
management functions. In (4) Manage Products, the admin updates product information and ensures that the product
database remains current with updated listings and availability. The system also processes and confirms order-related
information through the New Order Info module, which interacts with both Products (D1) and Users (D2) data stores.
A key feature of the system is the (5) Request Repair process, where customers can submit repair requests directly
through the platform. This request is forwarded to the admin, who manages repair operations and updates the Repair
Order database (D1). In ad dition, User information (D2) and Order records (D3) are used to track repair status and
maintain service history.  Overall, the diagram presents a unified system that integrates product browsing, ordering,
review submission, product management, and repair services within a single platform. This structure highlights the
proposed system’s goal of combining traditional e-commerce functions with after-sales repair management to enhance
user convenience and service efficiency.

Figure 12: Data flow diagram (DFD)

4. Implementation and Validation

HTML was used as the server -side scripting language to handle user requests, process data, and manage
interactions between the front-end and the database. SQL was utilized for database design and management, enabling
efficient storage and retrieval of product details, user information, reviews, and repair requests.

4.1 Functional Requirements
The system is designed to deliver comprehensive, efficient, and user -friendly electronic shopping and repair
experience. It must be capable of performing the following core functions:
a. User Registration and Secure Login : The system enables users to create personal accounts through a simple
registration process. It provide s a secure authentication mechanism that allows users to log in safely using
encrypted credentials. The system ensures privacy and protects user accounts from unauthorized access.

                                                                        461

b. Product Browsing and Display : The platform present s a well -organized and categorized product catalog,
including smartphones, smartwatches, laptops, and other electronic devices. Each product include s detailed
information such as technical specifications, pricing, availability status, and warranty coverage. The interface
provides a visually clear and structured product presentation to enhance user experience and decision -making.
c.  Advanced Search and Smart Filtering : The system supports a powerful search engine that allows users to
quickly locate products by brand, category, price range, and key features. Filtering options are intuitive and
flexible, enabling users to refine results efficiently and reduce search time.  The goal is to ensure users can find
relevant products with minimal effort.
d. Customer Reviews and Rating System : Users view authentic customer reviews and ratings for each product.
The system allows registered users to submit feedback based on their purchase experience. This feature enhances
transparency, builds trust, and supports informed purchasing decisions.
e. Shopping Cart and Secure Checkout : The platform provides a shopping cart feature where users can add,
update, or remove selected products. A secure and seamless checkout process is implemented, supporting safe
payment processing and order confirmation. The system ensures accuracy and reliability during transactions.
f. Repair Request Submission System: Users submit repair or service requests for purchased electronic items. The
system captures essential details such as issue description, product information, and service status tracking. This
feature integrates after-sales support directly into the platform.
g. Administrative Control Panel : An advanced admin dashboard provided for system administrators.
Administrators manage product listings, monitor and respond to repair requests, and moderate user -generated
content such as reviews. This ensures full control over platform operations and cont ent quality.
h. Database Integration and Data Management : The system utilizes a structured SQL database to store and
manage all critical data, including user profiles, product information, transactions, and reviews. It ensures data
consistency, integrity, and efficient retrieval across all system modules.

4.2 Non-Functional Requirements
The system meet s average-quality performance standards that ensure efficiency, usability, and reliability under
some conditions such as:
a. Performance and Speed: The website delivers fast loading times, with all pages loading within 2 seconds under
normal conditions.  Product search results in a smooth user experience. The system maintains consistent
responsiveness even during peak usage.
b. Usability and User Experience: The platform is intuitive, user-friendly, and easy to navigate, even for first-time
users. A clean and modern interface guides users effortlessly through browsing, purchasing, and service requests.
The system responds and is optimized for mobile phones, tablets, and desktop devices.
c.  Security and Data Protection : Strong security mechanisms are implemented to protect sensitive user
information such as passwords and personal data. All credentials are encrypted and securely stored in the database.
The system is protected against cyber threats, unauthorized access, and potential data breaches. Backup
mechanisms and recovery procedures in place to prevent data loss and ensure system continuity in case of failure.

                                                                        462

4.3 System Testing and Validation
To ensure the reliability, functionality, and usability of the TechNova platform, a comprehensive testing process
was conducted. The testing phase included functional testing, usability testing, and performance testing, supported by
real user data collected from 20 participants selected from the original survey group.

4.3.1 Functional Testing
Functional testing was performed to verify that all system features operate according to the specified requirements.
Each module of the system was tested using predefined test cases.  Table 1 presents a sample of functional testing
results.
Table 1: Functional Testing Results
Test Case Description Expected Result Actual Result Status
TC1 User Registration User account created successfully Successful Pass
TC2 User Login Valid credentials allow access Successful Pass
TC3 Product Search Relevant products displayed Accurate results shown Pass
TC4 Add to Cart Product added to cart Successful Pass
TC5 Submit Review Review stored in database Successful Pass
TC6 Repair Request Request submitted and recorded Successful Pass
TC7 Admin Product Update Product updated in database Successful Pass

The results indicate that 100% of the tested functionalities were successfully executed, confirming that the system
meets its functional requirements.

4.3.2 Usability Testing
Usability testing was conducted to evaluate user interaction, ease of navigation, and overall satisfaction. A group
of 20 users was asked to perform key tasks such as searching for a product, making a purchase, and submitting a repair
request. The following metrics were collected:
                                         Table 2: Usability Testing Results
STANDARD(Metric) Result
Task Completion Rate 95%
Average Task Time 2.1 minutes
User Satisfaction 4.4 / 5
Navigation Ease 90% positive feedback
Interface Clarity 92% positive feedback

These results demonstrate that the platform provides a highly user -friendly interface, with most users completing
tasks efficiently and expressing strong satisfaction with the system design.

4.3.3 Performance Testing
Performance testing was carried out to evaluate system responsiveness and stability under different conditions.
The system was tested using simulated concurrent users.

                                                                        463

                     Table 3: Performance Testing Results
Metric Result
Average Page Load Time 1.8 seconds
Maximum Load Time 2.5 seconds
Concurrent Users Tested 50 users
System Response Time < 2 seconds
Error Rate 2%

The results indicate that the system performs efficiently under normal and moderate load conditions, maintaining
acceptable response times and low error rates.

4.3.4 Discussion of Testing Results
The overall testing results confirm that the TechNova platform is functionally reliable, user -friendly, and
performance-efficient. Functional testing validated that all core features operate correctly without system failures.
Usability testing highlighted strong user acceptance, with high satisfaction scores and minimal task completion time.
Performance testing further demonstrated that the system could handle multiple users while maintaining stable
response times.  These findings support the effectiveness of the system design and validate its ability to deliver
seamless, integrated e-commerce and repair service experience.

5. Conclusion

This study presented the design and implementation of TechNova: Smart Electronics Shopping and Repair
Platform, a comprehensive system that integrates electronic product shopping with repair and maintenance services.
The platform was developed to address key challenges in existing e-commerce systems, particularly the lack of reliable
product information and the absence of integrated post -purchase support. The results demonstrate that the proposed
system successfully enhances online shopping experience by providing accurate, detailed, and user -friendly product
information. Additionally, the inclusion of a repair service module significantly improves convenience and user
satisfaction by offering a complete solution within a single pla tform. In conclusion, TechNova represents a practical
and efficient approach to modern e-commerce by bridging the gap between product selection and after-sales services.
The system not only improves user decision-making but also promotes trust and long-term engagement.

Acknowledgment: The research leading to these results has received no Research Grant Funding .
Author contribution: All authors have contributed, read, and agreed to the published version of the manuscript
results.
Conflict of interest: The authors declare no conflict of interest.

References
[1] AbdulMalik, A. H. H., & Yousif, M. J. (2021). Smart Online Grocery Shopping App Development. Artificial
Intelligence & Robotics Development Journal, 93-102.
[2] AlGhamdi, R., Nguyen, J., Nguyen, A., & Drew, S. (2012). Factors influencing e-commerce adoption by retailers
in Saudi Arabia: A quantitative analysis. International Journal of Electronic Commerce Studies, 3(1), 83–100.

                                                                        464

[3] Almtiri, Z. H. A., Miah, S. J., & Noman, N. (2022). Application of e-commerce technologies in accelerating the
success of SME operation. Education and Information Technologies, 27 (5), 6873 –6894.
https://doi.org/10.1007/s10639-021-10845-4
[4] Barbado, R., Araque, O., & Iglesias, C. A. (2020). A framework for fake review detection in online consumer
electronics retailers. Information Processing & Management, 57 (5), Article 102272.
https://doi.org/10.1016/j.ipm.2020.102272
[5] Combe, C. (2002). The management of e-commerce strategies for gaining and sustaining competitive advantage
in the online bookselling industry: The case of Amazon.com. Management Decision, 40 (9), 919 –925.
https://doi.org/10.1108/00251740210441185
[6] Hamill, J. (1998). Competing on the Internet: The case of Amazon.com. European Management Journal, 16(2),
212–222. https://doi.org/10.1016/S0263-2373(97)00089-3
[7] Cui, T. H., Liu, H., Xiao, W., & Zhao, X. (2022). Fulfilled by Amazon: A strategic perspective of competition
at the e -commerce platform. Manufacturing & Service Operations Management .
https://doi.org/10.1287/msom.2022.1078
[8] Sawan, A. S., Al -Otaibi, T. I., Al -Yahya, H. M., Soliman, W., & Abdul Hamid, A. -F. (2024). The role of e -
commerce in influencing corporate social responsibility: A case study on Noon Company. The International
Journal for Scientific Research, 3(4). https://doi.org/10.59992/IJSR.2024.v3n4p11
[9] Brooke, J. (1996). SUS: A quick and dirty usability scale. In P. W. Jordan, B. Thomas, B. A. Weerdmeester, &
I. L. McClelland (Eds.), Usability evaluation in industry (pp. 189–194). Taylor & Francis.
[10] Brynjolfsson, E., Hu, Y. J., & Rahman, M. S. (2013). Competing in the age of omnichannel retailing. MIT
Sloan Management Review, 54(4), 23–29.
[11] Egodawele, et al., Sedera, D., & Bui, V. (2022). A systematic review of digital transformation literature (2013–
2021) and the development of an overarching a priori model to guide future research. Journal of Strategic
Information Systems.
[12] Elamin, A. M., Ali, L., Ahmed, A. Z. E., & Aldabbas, H. (2025). Factors affecting attitudes toward e-shopping
in the United Arab Emirates. Cogent Business & Management, 12 (1), Article 2442542.
https://doi.org/10.1080/23311975.2024.2442542
[13] Grewal, D., Roggeveen, A. L., & Nordfält, J. (2017). The future of retailing. Journal of Retailing, 93(1), 1–6.
https://doi.org/10.1016/j.jretai.2016.12.008
[14] Khan, S., Ahmed, R. R., Hussain, M., & Khan, M. A. (2026). Knowledge transformation and omnichannel
adoption in retail internationalization: Comparative insights from the United Arab Emirates and Pakistan.
Journal of Open Innovation: Technology, Market, and Complexity.
[15] Kotler, P., & Keller, K. L. (2020). Marketing management (16th ed.). Pearson.
[16] Koufaris, M. (2002). Applying the technology acceptance model and flow theory to online consumer behavior.
Information Systems Research, 13(2), 205–223. https://doi.org/10.1287/isre.13.2.205.83
[17] Laudon, K. C., & Traver, C. G. (2022). E-commerce: Business, technology, and society  (17th ed.). Pearson.
ISBN 0137922205
[18] Lewis, J. R. (2018). The System Usability Scale: Past, present, and future. International Journal of Human –
Computer Interaction, 34(7), 577–590. https://doi.org/10.1080/10447318.2018.1455307
[19] Momani, A. M. (2026). Noon.com: A case study on technology adoption driving e -commerce success .
International Journal of Multidisciplinary and Current Research, 14 (2), 193–203.
[20] Nandwa, B., & Al Ameemi, H. (2016). The retail sector: Prospects and potential. In A. Al Faris & R. Soto
(Eds.), The economy of Dubai (pp. 189–212). Oxford University Press.
[21] Pantano, E., & Timmermans, H. (2014). What is smart for retailing? Procedia Environmental Sciences, 22 ,
101–107. https://doi.org/10.1016/j.proenv.2014.11.010
[22] Statista Research Department. (2024). E-commerce and consumer electronics market in the UAE. Statista.
[23] Stone, B. (2013). The everything store: Jeff Bezos and the age of Amazon. Little, Brown and Company.
[24] Traoret, R. I., AlDhaheri, S., AlAmeemi, F., & Ertek, G. (2024). Insights into domain names and product
categories of e-commerce websites: A case study of the UAE. In Lecture Notes in Operations Research  (pp.
229–241). Springer.
[25] Turban, E., Outland, J., King, D., Lee, J. K., Liang, T.-P., & Turban, D. C. (2018). Electronic commerce 2018:
A managerial and social networks perspective. Springer.
[26] Verhoef, P. C., Kannan, P. K., & Inman, J. J. (2015). From multi -channel retailing to omni-channel retailing.
Journal of Retailing, 91(2), 174–181. https://doi.org/10.1016/j.jretai.2015.02.005

                                                                        465

[27] Vyas, S. K., Vyas, L., Singh, S., & Joshi, M. (2023). Future of E -commerce: A robust review. In Intelligent
Sustainable Systems: Selected Papers of WorldS4 2022, Volume 2 (pp. 697 -710). Singapore: Springer Nature
Singapore.
[28] Yousif, J. H., Khan, F. R., Zia, K., & Saadi, N. A. (2021). Analytical data review to determine the factors
impacting risk of diabetes in North Al-Batinah Region, Oman. International Journal of Environmental Research
and Public Health, 18(10), 5323.
[29] Wells, J. D., Valacich, J. S., & Hess, T. J. (2011). What signal are you sending? How website quality influences
perceptions of product quality and purchase intentions. MIS Quarterly, 35 (2), 373 –396.
https://doi.org/10.2307/23044048
