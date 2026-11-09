---
title: Online Bus Ticket Sales System
url: https://doi.org/10.68456/ujspr-2026-28
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: University Journal of Student Projects and Research
authors:
- Phone Myint Nyi Nyi
source: openalex-oa
pdf_url: http://ucsh.edu.mm/wp-content/uploads/2026/09/Online-Bus-Ticket-Sales-System.pdf
pages: 6
chars: 10229
fetched_at: '2026-11-08T20:02:47+00:00'
kb_version: 1
---

# Online Bus Ticket Sales System

University Journal of Student Projects and Research, Volume 3, 2026
Accepted Date: 15.9.2026
www.ucsh.edu.mm
1

Online Bus Ticket Sales System
Phone Myint Nyi Nyi
Student, 5th Year, B.C.Sc.
University of Computer Studies, Hinthada
Supervised By
Khin Theink Theink Soe
Faculty of Computer Science
University of Computer Studies, Hinthada
Abstract: The Online Bus Ticket Sales System is designed to modernize and simplify the
process of reserving and purchasing intercity bus tickets through a responsive web -based
platform. Traditional ticket booking re quires passengers to visit physical bus terminals or
contact agents directly, leading to long waiting times, lack of real -time seat availability, and
limited payment options. This system provides an integrated solution where travelers can
search bus schedules, select available seats dynamically, complete secure digital payments, and
download e-tickets instantly. Developed with modern web technologies, the system offers bus
operators an intuitive administrative portal to manage bus fleets, routes, seat layou ts, trip
schedules, bookings, and pricing. This platform optimizes operational efficiency for
transportation providers, reduces manual ticketing errors, and provides passengers with a
streamlined, transparent booking experience.
Keywords: Online bus ticket ing, bus reservation system, seat allocation, e -ticket,
transportation management
INTRODUCTION
Public road transportation serves as the backbone of intercity travel and passenger
transit across the region. However, conventional manual ticketing systems present numerous
hurdles for both passengers and transport operators. Commuters frequently face ch allenges
such as standing in long terminal queues, lack of real -time visibility over departure schedules
and seat availability, and paper -based ticket handling. To overcome these limitations, the
Online Bus Ticket Sales System provides a centralized digita l solution. Passengers can query
route availability, view visual seat maps, choose their preferred seats, and securely purchase
tickets from any device. The platform also enables transport administrators to manage bus
schedules, monitor occupancy rates, and handle finances seamlessly.
PROBLEM
Traditional bus ticketing requires passengers to visit physical counters, leading to long
queues, wasted time, and limited visibility over departure schedules and seat availability.
Meanwhile, manual record-keeping by operators often causes double-booking errors and slow
payment tracking. Therefore, an online bus ticket sales system is needed to provide real -time
schedule inquiries, dynamic seat selection, and streamlined digital payments for both
passengers and operators.
APPROACH
The Online Bus Ticket Sales System is designed with two main roles: User (Passenger)
and Administrator, as shown in Figure 1 and Figure 2. The User role allows passengers to search

 University Journal of Student Projects and Research, Volume 3, 2026
Accepted Date: 15.9.2026
www.ucsh.edu.mm
2

trips, reserve seats, and purchase tickets conveniently, while  the Administrator role manages
passengers, routes, trips, bookings, and overall system operations.
After accessing the system, users can:
 View home, help, FAQs, and about pages
 Search trips by selecting departure city (From), arrival city (To), and departure
date
 View available trip lists and select a preferred trip
 Check real-time seat availability and choose preferred seat(s)
 Enter traveler information and confirm the booking
 Select a payment agent, complete transfer via QR scan, and submit payment
 View, download, or print digital e-tickets
After logging in, the administrator can:
 View the dashboard and monitor ticketing activities
 Add, update, and delete bus routes, schedules, and trip details
 Manage passenger records and booking information
 Verify payment transactions and approve ticket issuances
 Generate sales reports and passenger manifests
 Logout from the system

Figure 1: System Flow Diagram for Admin

 University Journal of Student Projects and Research, Volume 3, 2026
Accepted Date: 15.9.2026
www.ucsh.edu.mm
3

Figure 2: System Flow Diagram for User

                                                     Figure 3: Database Architecture

 University Journal of Student Projects and Research, Volume 3, 2026
Accepted Date: 15.9.2026
www.ucsh.edu.mm
4

Figure 3 presents the Entity Relationship Diagram (ERD) for the Bus Booking System,
illustrating the database structure and relationships between key entities. The ERD serves as
the foundation for data modeling, ensuring referential integrity and efficient querying through
well-defined primary and foreign keys. In the Bus Booking System, the ER diagram consists
of nine main tables:
 buses - Stores fleet details, seating capacity, and operational status.
 routes - Manages travel paths, origins, destinations, and total distance.
 trips - Schedules specific bus journeys with departure/arrival times and fares.
 bookings - Records passenger reservations, selected seats, contact details, and
booking status
 payments - Tracks transaction records, payment methods, and verification statuses.
 seat_layouts - Defines the physical seat grid and aisle configurations for buses.
 seat_locks - Temporarily reserves seats during checkout to prevent duplicate
bookings.
Each table is interconnected using primary and foreign keys to ensure referential
integrity. The ERD defines cardinality (one-to-many, many-to-one) to reflect the real-world
structure of how buses, routes, trips, bookings, and passengers are related.
RESULTS
The Onli ne Bus Booking System streamlines route scheduling, passenger seat
reservations, and payment verification into a unified platform. Authorized administrators can
access a dedicated dashboard to manage bus fleets, configure route networks, schedule trips,
manage user accounts, and review submitted payment slips (such as KBZPay, CB Pay,
WavePay, and AYA Pay) before approving bookings. Passengers can easily search available
routes by origin, destination, and travel date without requiring prior registration, sel ect seats
via an interactive layout, and secure their seats through a temporary locking mechanism during
checkout. Upon payment confirmation, the system generates downloadable digital e -tickets
complete with scannable QR codes for seamless boarding verification.
Built with PHP, the Laravel framework, Blade templates, Vanilla JavaScript, and a
MySQL relational database, the platform follows an MVC pattern structured with a Service -
DAO architecture for high maintainability and testability. Eloquent ORM enforc es data
consistency across bookings, trips, seat allocations, and payments. Hosted on an Apache/Nginx
web server, the system eliminates manual booking overhead, prevents seat duplication, and
provides a responsive, reliable booking experience.

Figure 4: Admin Dashboard with Real-time Key Metrics and Today's Due Booking

 University Journal of Student Projects and Research, Volume 3, 2026
Accepted Date: 15.9.2026
www.ucsh.edu.mm
5

Figure 5: Sales Analytics and Revenue Line Chart Interface
CONCLUSION
The Online Bus Booking System was developed to streamline route scheduling, seat
reservations, and ticketing operations into a centralized platform. It addresses the inefficiencies
of manual ticketing and counter -based booking by providing an intuitive sys tem where
passengers can search routes, select seats in real time, and confirm bookings with digital
payments. This project reduces administrative workload, minimizes double -booking errors
through temporary seat -locking mechanisms, and accelerates verifica tion workflows with
scannable digital e-tickets. By leveraging modern technologies including PHP, Laravel, Blade
templates, and MySQL structured around a Service-DAO architecture, the application is built
to be scalable, maintainable, and reliable. In conc lusion, the system serves as an efficient
solution for transport operators and travelers alike, delivering transparent booking
management, robust transaction tracking, and an accessible ticketing experience.
REFERENCES
[1]. Matt Doyle, “Beginning PHP 5.3”, 1st Edition, Wiley Publishing , ISBN-10:
9780470413968x, 2009.
[2]. Tom Bulter and Kevin Yank, “PHP & MySQL Novice to Ninja”, 7th Edition, Site Point Pty,
Limited, Australia, 2024. http://classes.jgspectrum.com/classes/320_S24/LectureNotes/1-
13_PHP_and_MySQL_Novice_to_Ninja_ed7_with_highlights.pdf.
[3]. O’Reilly, “Head First PHP & MySQL”, 1st Edition, O'Reilly Media, Inc., 2008.
[4].  Janet Valade, “PHP 5 For Dummies”, Hoboken, NJ: Wiley Publishing. ISBN: 0764541668,
Indianapolis, Indiana, 2004.
[5]. Paul McFedries, “HTML, CSS, & JavaScript All-in-One for Dummies”, 1st Edition, Wiley
Publishing, ISBN: 978-1-394-16472-1, 2023.
[6]. Myat Thazin Soe, “PADDY PESTS INFORMATION SYSTEM”,  University Journal of
Student Projects and Research,  V olume 1, 2024 , Hinthada , Myanmar,
https://ucsh.edu.mm/wp-content/uploads/2024/10/PADDY-PESTS-INFORMATION-
SYSTEM.pdf
[7]. Nanda Kyaw, Saw Hla Nandar, “SmartGrade: Grading Certificate Information System
(Client-Server)”, University Journal of Student Projects and Research,  V olume 2, 2025,

 University Journal of Student Projects and Research, Volume 3, 2026
Accepted Date: 15.9.2026
www.ucsh.edu.mm
6

Hinthada, Myanmar, https://ucsh.edu.mm/wp-content/uploads/2025/10/SmartGrade-
Grading-Certificate-Information-System.pdf
[8]. Lin Lat Nay Chi, Nilar Kyaw , “Construction Materials Inventory Management System ”,
University Journal of Student Projects and Research, V olume 2, 2025, Hinthada, Myanmar,
https://ucsh.edu.mm/wp-content/uploads/2025/10/Construction-Materials-Inventory-
Management-System.pdf
[9].  Win Lei Lei Htun, Hnin Wutt Yee Zaw, “Dhamma Online Learning Platform”, University
Journal of Student Projects and Re search, V olume 2, 2025, Hinthada, Myanmar,
https://ucsh.edu.mm/wp-content/uploads/2025/10/Dhamma-Online-Learning-
Platform.pdf
[10]. Nan Hsu Wai, “The Fashion Shop Online Platform”, University Journal of Student Proj
ects and Research,  V olume 2, 2025, Hinthada, Myanmar, https://ucsh.edu.mm/wp -
content/uploads/2025/10/The-Fashion-Shop-Online-Platform-1.pdf
