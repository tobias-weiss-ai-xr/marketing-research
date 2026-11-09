---
title: 'Design and Implementation of Web-Based Company Profile Information System Using Laravel Framework
  with Lead Management Integration (Case Study: PT Sacha Inchi Sejahtera)'
url: https://doi.org/10.59141/jiss.v7i8.2458
category: b2b
subcategory: framework
date: 2026-08
venue: Jurnal Indonesia Sosial Sains
authors:
- Nurudina Awalia Paramita
- Moh Muthohir
- Bagus Sudirman
source: openalex-oa
pdf_url: https://jiss.publikasiindonesia.id/index.php/jiss/article/download/2458/2946
pages: 9
chars: 22102
fetched_at: '2026-11-08T17:35:15+00:00'
kb_version: 1
---

# Design and Implementation of Web-Based Company Profile Information System Using Laravel Framework with Lead Management Integration (Case Study: PT Sacha Inchi Sejahtera)

Vol. 7, No. 8, August 2026
                  E-ISSN:2723 – 6692 P-ISSN:2723– 6595
http://jiss.publikasiindonesia.id/

3651
Design and Implementation of Web-Based Company Profile Information
System Using Laravel Framework with Lead Management Integration (Case
Study: PT Sacha Inchi Sejahtera)

Nurudina Awalia Paramita*, Moh Muthohir, Bagus Sudirman
Universitas Sains dan Teknologi Komputer, Indonesia
Email: nurudinaawalia@gmail.com*, muthohir@stekom.ac.id, bagus@stekom.ac.id

Keywords:  Abstract
Company Profile; Laravel
Framework; Lead Management;
PT Sacha Inchi Sejahtera;
Research & Development;
Prototype Model
 The need for a digital presence in agro -herbal companies such as PT Sacha
Inchi Sejahtera is critical, particularly for establishing credibility and
facilitating B2B and B2C business communication. Currently, the company
relies heavily on conventional promotional channels, which limits market
reach and reduces client communication ef ficiency. This research aimed to
design and implement a web -based Company Profile Information System
using the Laravel framework, incorporating interactive Buyer Lead
Management integration, structured product specification cataloging, and
tailored Search Engine Optimization (SEO) strategies with a focus on User
Experience (UX). The system was developed using a Research and
Development (R&D) approach with a prototype model. Functional testing
through Black Box Testing achieved a 100% success rate across all primary
features. Furthermore, usability testing using the System Usability Scale
(SUS) resulted in an average score of 83.5, categorized as “Excellent”
(Grade A). The developed system effectively improved information
accessibility, accelerated lead conversion processes for the marketing team,
and enhanced the company’s overall digital branding performance.

INTRODUCTION
In the current era of digital transformation, the presence of web-based information platforms
has become a crucial instrument for modern business entities to establish professional credibility,
strengthen corporate image, and expand market reach. Internet penetration in Indonesia, which
exceeded 79.5% in 2024 and is projected to continue increasing, indicates that most stakeholders
and consumers rely on digital media as a primary source for obtaining business -related
information.
PT Sacha Inchi Sejahtera is a manufacturing and processing company engaged in the
processing of sacha inchi commodities and general-purpose machinery. In its business operations,
the company faces major challenges, including limited promotional reach and slow dissemination
of official company information to potential buyers, both in B2C markets (retail sales an d herbal
product education) and B2B markets (wholesale partnerships, distributor networks, and industrial
machinery procurement). Dependence on conventional promotional media, such as printed
brochures and banners, not only increases recurring operational costs but also restricts market

3652
expansion beyond local areas and makes it difficult for potential business partners to verify product
legality and technical specifications.
To address these challenges, a web -based Company Profile Information System was
developed using the Laravel framework  (Azizah & Tawadzu, 2026; Azran & Wahid, 2022;
Firosulhaq & Miftahuddin, 2026; Himmah & Laouar, 2025; Khaliq, Batubara, Syaula, & Sahrial,
2022; Khaliq, Batubara, Syaula, & Yudha, 2022; Surahmat & Darmawan, 2024; Wulandari &
Gunawan, 2024). Laravel was selected because it provides a structured and efficient Model–View–
Controller (MVC) architecture, built -in security mechanisms against cyber threats (including
Cross-Site Request Forgery [CSRF] protection, SQL injection prevention, and Cross -Site
Scripting [XSS] mitigation), as well as flexibility for future system scalability.
Several studies have examined the development of web -based company profile and
information systems across various contexts  (Emadi, 2023; Gledson et al., 2024; Li et al., 2023;
Lutfi et al., 2022; Sutisna & Rahman, 2025) . Nugraha et al. (2024) developed a school website
using the Laravel framework as an information and promotional medium for PKBM institutions.
The study successfully implemented a school profile information system with news features;
however, it did not include buy er lead classification or B2B Request for Quotation (RFQ)
integration. Meisak et al. (2022) developed a prototype -based application for equality education
institutions, focusing on institutional profiles with product catalogs and static galleries. However,
the system lacked structured Search Engine Optimization (SEO) implementation  and lead
management features. Al -Fraihat et al. (2023) evaluated information system success in public
organizations using the updated DeLone  and McLean model, emphasizing the importance of
system quality, information quality, and service quality in determining user satisfaction. Belanche
et al. (2022) examined website usability and its influence on consumer satisfaction and website
usage intention, highlighting the moderating role of perceived risk. Laudon and Laudon (2023)
discussed the strategic role of management information systems in digital organizations,
emphasizing the importance of information systems in supporting modern business operations.
Despite the growing body of research on web -based information systems, several gaps
remain. First, most existing studies have focused on educational institutions or general
organizational profiles, with limited attention to the specific requirements of agr o-herbal
manufacturing companies serving both B2B and B2C market segments. Second, although
numerous studies have developed company profile systems, few have integrated interactive lead
management features capable of classifying and routing potential buyer  inquiries in real time.
Third, previous research has generally overlooked the importance of structured product
specification catalogs with RFQ features specifically designed for the herbal industry, where
technical specifications, certifications, and prod uct documentation are essential for B2B
transactions. Fourth, limited studies have integrated SEO optimization, UX approaches, and lead
management within a single comprehensive information system (Ahmadi, 2022; Kolomiiets et al.,
2024; Nurrohman, 2025) . Fifth, research that simultaneously evaluates system functionality
through Black Box Testing and user experience through the System Usability Scale (SUS) within
the context of agro-herbal company profile systems remains limited.

3653
The primary novelty of this research lies in the integration of a Laravel -based Company
Profile Information System with the specific business process requirements of PT Sacha Inchi
Sejahtera. Unlike conventional company profile systems that primarily provide static information,
such as company profiles and basic galleries, this system introduces several distinguishing
features, including:
1. Interactive Lead Management System: Integration of potential buyer communication flow
forms that are able to classify applicant types (Retail B2C vs Wholesale/B2B Partners) and
auto-routing offer messages directly to the marketing team in real-time.
2. Structured Product Catalog & Education: Provision of sacha inchi product technical
specification modules (Omega 3 -6-9 content, certification, and quality standards) equipped
with the Request for Quotation (RFQ) feature.
3. On-Page SEO Optimization & UX Approach: Implementation of dynamic meta -data
structures, clean URLs, as well as responsive interface testing tailored to the search behavior
of potential buyers of the herbal industry.

Table 1. Comparison of Previous Research with the Novelty of This Research
Researcher /
Reference Research Focus Features/approach Limitations & Comparison
Nugraha et al. (2024) PKBM School Website School profile
information system &
news
There is no lead buyer
classification and B2B
RFQ integration yet.
Meisak et al. (2022) Institution Profile
Application
Product catalogue &
static gallery
It doesn't come with
structured SEO
optimization and lead
management.
This Research (2026) Company Profile PT
Sacha Inchi Sejahtera
Laravel, Interactive
Lead Capture, RFQ,
SEO & UX SUS
Testing
Specially designed to
answer the B2B/B2C
agro-business
communication flow.
 Source: Compiled from literature review, 2026

This research aimed to design and implement a web -based Company Profile Information
System for PT Sacha Inchi  Sejahtera using the Laravel framework with integrated lead
management features. Specifically, this research sought to develop a responsive and secure
company profile website that effectively presents company information, legal documents, and
product catalogs; implement an interactive lead management system capable of classifying B2B
and B2C inquiries and automatically routing them to the marketing team; evaluate system
functionality through Black Box Testing; and assess system usability using the System Us ability
Scale (SUS).
The benefits of this research are twofold. Theoretically, this study contributes to the body
of knowledge regarding web-based information system development in the agro -herbal industry,
expands the application of lead management integration within company profile systems, and
provides a comprehensive evaluation framework combining functional and usability testing.

3654
Practically, this research provides a digital solution for PT Sacha Inchi  Sejahtera to improve
information accessibility, accelerate lead conversion processes for marketing teams, strengthen
overall digital branding, and expand market reach across both B2B and B2C segments.
Furthermore, the developed system can serve as a reference model for other agro-herbal companies
facing similar challenges in establishing and managing their digital presence. This research also
provides practical guidance for web developers and system designers in integrating business
communication workflows with company profile platforms.

RESEARCH METHODS
This research employed the Research and Development (R&D) method combined with the
Prototype system development model. The Prototype approach was selected because it enabled
iterative design improvements based on direct feedback from stakeholders at PT Sacha Inchi
Sejahtera, resulting in a system that aligned with the company’s operational requirements.
R&D Research Stages
The development of the system is carried out through 10 systematic stages as follows:
(1) Potential and Problems: Identifying the limitations of print promotional media and the
absence of an official information platform at PT Sacha Inchi is prosperous.
(2) Data Collection: Conducting field observations and in -depth interviews with the
company's management and marketing team.
(3) Website Design: Designing system architecture, MySQL database structure, Entity
Relationship Diagram (ERD), Use Case Diagram, and UI/UX wireframe.
(4) Website Validation: Conduct an initial design evaluation with experts/skilled developers
to ensure the feasibility of the system architecture.
(5) Design Revision: Improved the database interface and flow based on expert validation
records.
(6) Website Testing (Alpha Testing): Conducting internal testing of system functionality
using the Black Box Testing method.
(7) Website Revision: Improving program code and exception handling after Black Box
Testing.
(8) Beta Testing: Testing direct use by end-users (company staff and potential buyers) using
the System Usability Scale (SUS) instrument.
(9) Post-Usability Revision: Minor adjustments to interface comfort and page response speed.
(10) System Production/Launch:  The system is uploaded to the official hosting server
(production environment) and is ready for full operation.
Data Collection Methods
Primary and secondary data collection is carried out through three main techniques: (1)
Direct observation of business processes and information request flows at PT Sacha Inchi
Sejahtera; (2) Structured interviews with marketing leaders and staff regarding the need for profile
data, legality certification, and product catalogs; and (3) Documentation Studies from scientific
literature, official Laravel documentation, and herbal industry regulatory standards.

3655
System Testing Instruments
To guarantee the reliability of the system, testing is carried out in two stages: First, Black
Box Testing is focused on verifying the functionality of the features (authentication, catalog
CRUD flow, lead management form delivery, and CSRF security). Second, the usability test uses
the System Usability Scale (SUS) questionnaire with 10 standard questions based on the Likert
scale of 1–5.

RESULTS AND DISCUSSION
Website Display Result

Figure 1. Home Page
The result of the User Interface display from the Computer Service Server company profile website are
equipped with the display of the system management content page below.

Figure 2. Admin Panel
Technical Specifications and System Architecture
Company Profile Information System PT Sacha Inchi Sejahtera was developed with
technical specifications based on the Laravel Framework (PHP 8.2), MySQL database, Blade

3656
Templating Engine, Tailwind CSS, and interactive JavaScri PT The system architecture separates
access rights between the General Visitor (Guest) and the Administrator (Admin Panel).

Table 2. Technical Specifications of System Development Environment
Development Components Technologies / Frameworks Used
Backend Framework Laravel 10.x / PHP 8.2 (MVC Architecture)
Database Management System MySQL Server 8.0 with Eloquent ORM
Frontend & UI Design HTML5, CSS3 (Tailwind CSS), Blade
Engine, JavaScript
Functional & UX Testing Black Box Testing & System Usability Scale
(SUS)
Source: Author's documentation, 2026
Key Features Implementation
The website interface is designed in a responsive manner to ensure convenient access through
mobile devices as well as desktop computers. Key features that have been implemented include:
1. Home: Displays interactive hero banners, company superior values, profile summaries, and
highlights of key products (Sacha Inchi Oil, Roasted Seeds, and Processing Machine).
2. Profile & Legal Page (About Us): Presents the vision -mission, organizational structure,
company history, and proof of official license/legality to provide legal certainty for potential
B2B buyers.
3. Interactive Product Catalog & RFQ: Displays product technical specifications, nutritional
content, high photo gallery, and special 'Request for Quotation' button.
4. Interactive Lead Management & Contact Module: An interactive form with a selection of
needs categories (Retail/Wholesale/Cooperation) that automatically maps incoming messages
to the Admin Dashboard and sends notifications to the marketing team's emails.
5. Administrator Dashboard: Authentication-protected pages to manage catalog content, read
and respond to lead messages, and autonomously update company news.
Functional Test Results (Black Box Testing)
Black Box testing is performed against all system functionality scenarios. The test results prove
that all of Laravel's built -in libraries such as Eloquent ORM, CSRF Protection, and Middleware
Authentication run as expected without any critical errors.

Table 3. Summary of Black Box Testing Results
Tested Features Testing Scenarios Expected Results Status
Admin Authentication Login with valid &
incorrect credentials
The system grants
access if it is valid and
rejects if it is wrong
Compliant (100%)
Kelola Catalog
(CRUD)
Add, edit, delete sacha
inchi product data
Data is successfully
updated in the MySQL
database
Compliant (100%)
Form Lead Capture Sending a B2B/B2C
quote form
Messages stored in DB
& email notifications
sent
Compliant (100%)

3657
SEO Optimization &
Dynamic Meta
Open a product page
with dynamic meta tags
Meta tags & clean
URLs appear according
to the structure
Compliant (100%)
CSRF Security & Input Submit a form without
a token / SQL injection
System blocks
unauthorized access
Compliant (100%)
 Source: Primary data from system testing, 2026

System Usability Scale (SUS) Test Results
The usage test was carried out by testing 15 respondents (consisting of 3 management staff
of PT Sacha Inchi Sejahtera and 12 prospective buyers/general visitors). The results of the SUS
score calculation resulted in an average score of 83.5. Based on the standard SUS assessment scale,
a score of 83.5 is included in the category of 'Acceptable' with Grade A ('Ex cellent'). This proves
that the system interface is very easy to operate, communicative, and according to the user's
preferences.

CONCLUSIONS
Based on the results of the design, implementation, and testing processes, this research
successfully developed a web -based Company Profile Information System for PT Sacha Inchi
Sejahtera using the Laravel framework that is informative, responsive, and secure. The integration
of Interactive Lead Management features and product technical specification catalogs effectively
facilitated the structured communication flow of potential buyers (B2B/B2C), addressing the
limitations of conventional company profile systems. Black Box Testing demonstrated a 100%
functional success rate, while System Usability Scale (SUS) testing achieved a score of 83.5,
categorized as Grade A (Excellent), co nfirming that the website was highly feasible as the
company’s official digital information and promotional platform. For future development, the
system is recommended to incorporate payment gateway integration and a complete e -commerce
module if the compa ny intends to support direct retail transactions through the website.
Additionally, the development of multilingual modules (Indonesian and English) is recommended
to expand the international market reach for sacha inchi products.

REFERENCES
Ahmadi, I. (2022). User experience-led redesign and SEO optimisation of a website. A case study
on a technologically augmented teaching system.
Al-Fraihat, D., Joy, M., Masa'deh, R., & Sinclair, J. (2023). Evaluating information system success
in public organizations: A theoretical model using DeLone and McKinley updated model.
Information Systems Frontiers, 25(2), 567-589.
Azizah, I., & Tawadzu, D. A. (2026). Designing a Web -Based Company Profile Information
System to Support Information Technology Governance in Event Organizers and Wedding
Organizers. Governance IT Adoption and Technology Advance, 1(2), 20–27.
Azran, N. Z. A. Z., & Wahid, N. (2022). Design and Development of a Web-Based System using
Laravel Framework: A Competition Management System. Applied Information Technology
And Computer Science, 3(2), 514–532.

3658
Belanche, D., Casaló, L. V., & Guinalíu, M. (2022). Website usability, consumer satisfaction and
the intention to use a website: The moderating effect of perceived risk. Journal of Retailing
and Consumer Services, 19(1), 124-132.
Emadi, J. (2023). The development of a design theory for web based information systems. Journal
of Robotics Spectrum, 1, 13–23.
Firosulhaq, M., & Miftahuddin, A. A. (2026). Web Based Sales Information System for Crackers
Products Using Laravel Framework. NEWTON: Networking and Information Technology ,
5(3), 104–107.
Gledson, B., Rogage, K., Thompson, A., & Ponton, H. (2024). Reporting on the development of a
web-based prototype dashboard for construction design managers, achieved through design
science research methodology (DSRM). Buildings, 14(2), 335.
Himmah, F., & Laouar, M. S. (2025). Development of a Web-Based Student Registration System
Using Laravel Framework. JOKI: Journal of Computing and Informatics, 2(2), 28–35.
Khaliq, A., Batubara, S., Syaula, M., & Sahrial, S. (2022). Designing a Web-Based Career System
Using the Laravel Framework using the waterfall method. International Conference on
Sciences Development and Technology, 2(1), 203–209.
Khaliq, A., Batubara, S., Syaula, M., & Yudha, S. W. (2022). Designing a Web -Based Career
System Using the Laravel Framework. International Journal Of Computer Sciences and
Mathematics Engineering, 1(2).
Kolomiiets, A., Miroshnychenko, I., Ziuziun, V., Kmytiuk, T., & Datsenko, N. (2024).
Development of Project Management Models for Information Systems to Improve Website
SEO Metrics. IT&I, 334–345.
Laudon, K. C., & Laudon, J. P. (2023). Management Information Systems: Managing the Digital
Firm (17th ed.). Pearson.
Li, P., Zhou, Y., & Huang, S. (2023). Role of information technology in the development of e -
tourism marketing: A contextual suggestion. Economic Analysis and Policy, 78, 307–318.
Lutfi, A., Al -Okaily, M., Alsyouf, A., & Alrawad, M. (2022). Evaluating the D&M IS success
model in the context of accounting information system and sustainable decision making.
Sustainability, 14(13), 8120.
Meisak, A., Pratiwi, S., & Nugroho, E. (2022). Development of prototype -based applications for
equality education institutions. Journal of Information Systems and Technology, 8(1), 23 -
34.
Nugraha, F. S., Sudirman, B., & Aqham, A. A. (2024). Development of school websites with
Laravel frame work as an information and promotional medium. Journal of Information and
Computer Systems (JISS), 2(1), 12-20.
Nurrohman, R. (2025). Optimizing Search Engine Optimization (SEO) and User Experience (UX)
on Local Online Business Training Websites: A Comparative Study of Young Entrepreneur
Community Platforms. Akubis: Jurnal Akuntansi Dan Bisnis, 10(1), 87–100.
Surahmat, A., & Darmawan, R. (2024). Application of the SDLC Method and Laravel Framework
in Developing a Web Draft Based Company Profile Information System. Scientific Journal
of Information System, 2(1), 20–25.
Sutisna, N., & Rahman, T. K. A. (2025). Web -Based E-Procurement Development in Regional -
Owned Enterprises (BUMD): An R&D Approach. International Journal of Advances in
Data and Information Systems, 6(1), 135–151.
Wulandari, H., & Gunawan, D. (2024). Design of a web -based project planning system using the
Laravel framework at PT Globalindo Lestari Utama. Journal of Information Technology,

3659
Computer Science and Electrical Engineering, 1(2), 181–190.
