---
title: Assessing the Effectiveness of Selective Marketing to Broaden Participation in CS Education
url: https://arxiv.org/abs/2511.20554
category: digital-marketing
subcategory: empirical
date: 2025-11
venue: ''
authors:
- Aditya Shah
- Tyler Menezes
source: arxiv
pdf_url: https://arxiv.org/pdf/2511.20554
pages: 2
chars: 12016
fetched_at: '2026-11-08T13:15:28+00:00'
kb_version: 1
---

# Assessing the Effectiveness of Selective Marketing to Broaden Participation in CS Education

Assessing the Effectiveness of Selective Marketing to Broaden
Participation in CS Education
Aditya Shah
adshah@uw.edu
University of Washington
Seattle, Washington, USA
Tyler Menezes
tylermenezes@codeday.org
CodeDay
Seattle, Washington, USA
Abstract
Many studies have aimed to broaden participation in computing
(BPC) through extracurricular educational initiatives. When these
initiatives are structured as open-enrollment extracurricular pro-
grams, their success often depends on their marketing approach.
However, there is little in the computing education research litera-
ture about how to conduct effective marketing for these initiatives.
We describe the changes made to the marketing strategy of one
such program, an educational hackathon for middle school and high
school students in the Pacific Northwest. These included reducing
promotion to affluent families, using targeted school-based commu-
nication, and emphasizing cost supports during initial promotion.
We then compare attendance and self-reported demographics be-
fore and after the intervention. Results indicate a higher proportion
of students from marginalized and low-income communities and
no reduction in overall attendance.
1 Introduction
Extracurricular, open-enrollment computing education events are
often promoted through channels that disproportionately reach
students from affluent backgrounds and well-resourced communi-
ties, leading to participant pools that underrepresent marginalized
groups. This inequality limits access to the social, educational, and
career benefits these events provide and risks reinforcing existing
gaps in technology employment. CodeDay is one such program-
ming event that has been studied for its potential to improve diver-
sity. [2] The objective of this research is to test whether an improved
promotion strategy can help broaden participation in extracur-
ricular, in-person CS education programs and provide practical
guidance for inclusive recruitment in computer science education
contexts. Although the influence of marketing may seem intuitive,
BPC research rarely isolates it from program design, making it im-
portant to measure its independent impact. We test the hypothesis
that(H1)limited promotion in affluent neighborhoods, leveraged
teacher and community partner channels, and highlighted cost sup-
ports will improve the proportion of underrepresented students
participating in the program.
2 Prior Work
K-12 CS education programs use a range of marketing and recruit-
ment strategies. Among extracurricular and multi-school programs,
studies have discussed active recruitment practices such as letter-
writing campaigns and recruiting from introductory CS courses, [8]
alongside sustained partnerships between schools, districts, univer-
sities, and industry. [4] Several programs have addressed diversity
by offering professional development opportunities for strategically
selected schools, student recruitment efforts, volunteer training,
and curriculum design.[3, 7] Intra-school studies have found that
teacher support from counselors and administrators is essential,
with successful programs requiring holistic, schoolwide stakeholder
involvement rather than relying solely on CS teachers.[5, 8] Uni-
versal Design for Learning principles have also been implemented
to create accessible programming environments.[6]
These studies all describe thoughtful recruitment practices. How-
ever, there is limited literature examining the effect size of particular
marketing practices. It is difficult to determine how much of the
success of BPC programs in recruiting diverse participants is related
to appealing program design versus marketing tactics.
3 Methods
Prior to the intervention, program marketing comprised (1) technol-
ogy companies sharing event information with their employees and
their families; and (2) promotional flyers provided for distribution
to all local high schools. Events included a nominal registration fee
of $5-$10; while the fee was intended to offset costs, scholarships
were offered without restriction to any student who requested one,
with discounts being provided proactively to technology companies
and schools.
To study the effect size of the marketing strategy, we revised
these marketing tactics to reduce marketing to affluent areas, am-
plify communication channels that reach lower-income communi-
ties, and provide details about cost supports upfront in marketing
materials:
1.Reducing promotion to affluent families. To avoid skewed
attendance from affluent neighborhoods, the event was not ad-
vertised through channels disproportionately accessed by higher-
income families. We ceased flyer distribution to affluent schools and
promotion through corporate partners. Additionally, we did not
announce events on the CodeDay social media accounts, because
these followers were more affluent and familiar with the event.
2.Targeted school-based communication. A comprehensive
list of Title I high schools across the three nearest counties was
developed, and outreach messages were distributed to teachers
across a range of subject areas (including arts, humanities, and col-
lege/career readiness) rather than exclusively computer science de-
partments. This approach was designed to reach students who may
not already have identified with computer science as an academic
pathway. Promotional posts were also shared via school-affiliated
social media accounts and e-flyer services when available.
3.Emphasis on cost supports. Outreach materials explicitly
highlighted cost-reducing supports and attendance benefits, such as
free transportation options and a free laptop. Messaging was framed
to lower perceived financial and logistical barriers to attending the
events.
arXiv:2511.20554v1  [cs.CY]  25 Nov 2025

4 Results
Data were collected via registration forms at two events prior to the
implementation of the revised promotional strategy, in summer and
fall of 2023, and two events following implementation, in winter
and spring of 2024. (𝑁= 285; 𝑛𝑝𝑟𝑒 = 121, 𝑛𝑝𝑜𝑠𝑡 = 164). We analyzed
participant demographics according to gender, race/ethnicity, and
socioeconomic status. Each variable was dichotomized to reflect
participation by underrepresented groups, aligning with our focus
on barriers broadly rather than subgroup outcomes:
Gender identity.Coded asMale(he/him) orNonMale(others).
Race/ethnicity.Coded asUnderrepresented(non-White) orNot-
Underrepresented(White), reflecting the demographic composition
of software engineers in the studied region and time period.
Socioeconomic status.Average household income by residen-
tial postal code, as retrieved from American Community Survey
5-year estimates, was used as a proxy due to challenges in collect-
ing individual income data from minors. Participants were coded
asLowIncome(median household income < 150%of the Federal
poverty line) orNotLowIncome( ≥ 150%of the Federal poverty line).
We conducted Pearson’s chi-squared tests with Yates’ continuity
correction to examine associations between promotional strategy
and each demographic variable. To address the issue of multiple
comparisons, we applied the Holm–Bonferroni correction method
to adjust p-values. For associations reaching statistical significance,
we calculated Cramer’s V as a measure of effect size.
We found an association between the improved promotion strat-
egy and both ethnicity ( 𝜒 2 = 79.7, 𝑝< 0.0001) and income level
(𝜒 2 = 65.6, 𝑝< 0.0001) but not gender (𝜒 2 = 1.17, 𝑝= 0.28). In the
improved promotion strategy group, there were more students than
expected under the hypothesis of independence who are from under-
represented ethnic (𝑠𝑡𝑑𝑟𝑒𝑠= 9.04) and low-income (𝑠𝑡𝑑𝑟𝑒𝑠= 8.22)
backgrounds. According to our results, there is a large association
between the improved promotion strategy and ethnicity (Cramer’s
V =0.53) and a medium association with income level (V =0.49).
5 Discussion
Our findings demonstrate that targeted promotional strategies can
substantially improve participation from students of underrepre-
sented racial/ethnic backgrounds and low-income communities in
extracurricular K-12 computing education programs. These results
support H1 in emphasizing the importance of active, intentional
recruitment strategies. Teachers and other community partners
likely act as cultural brokers who communicate the value of CS pro-
grams to families who might otherwise see them as "not for them. "
Additionally, highlighting cost supports upfront may reduce uncer-
tainty about perceived hidden costs. The focus on inclusion and
barrier removal is critical in addressing the factors that contribute
to attrition from STEM fields, such as computer science, where
underrepresented students are more likely to leave the field due to
stereotype threat.[1] The lack of significant gender differences may
indicate that gender-based barriers to participation operate through
different mechanisms from those addressed by our intervention
and require further investigation.
6 Threats to Validity and Future Work
The pre–post design without a control group leaves open the possi-
bility of temporal or concurrent influences. Additionally, the find-
ings from a single geographic location may have limited general-
izability to programming events in regions with different demo-
graphic compositions or where the baseline levels of representation
of underrepresented groups in computing differ. Using ZIP code-
level income proxies and dichotomized demographic categories
may oversimplify participants’ lived experiences.
References
[1] Maya A. Beasley and Mary J. Fischer. 2012. Why they leave: the impact of stereo-
type threat on the attrition of women and minorities from science, math and
engineering majors.Social Psychology of Education15, 4 (Dec. 2012), 427–448.
https://doi.org/10.1007/s11218-012-9185-3
[2] Emilia Gan, Tyler Menezes, and Benjamin Mako Hill. 2022. How Gender, Ethnicity,
and Public Presentation Shape Coding Perseverance after Hackathons. InPro-
ceedings of the 22nd Koli Calling International Conference on Computing Education
Research (Koli Calling ’22). Association for Computing Machinery, New York, NY,
USA, 1–11. https://doi.org/10.1145/3564721.3564727
[3] Joanna Goode. 2007. If You Build Teachers, Will Students Come? The Role of
Teachers in Broadening Computer Science Learning for Urban Youth.Journal of
Educational Computing Research36, 1 (Jan. 2007), 65–88. https://doi.org/10.2190/
2102-5G77-QL77-5506
[4] Joanna Goode. 2008. Increasing diversity in k-12 computer science: strategies
from the field. InProceedings of the 39th SIGCSE technical symposium on Computer
science education. ACM, Portland OR USA, 362–366. https://doi.org/10.1145/
1352135.1352259
[5] Sarah Gretter, Aman Yadav, Phil Sands, and Susanne Hambrusch. 2019. Equi-
table Learning Environments in K-12 Computing: Teachers’ Views on Barriers
to Diversity.ACM Transactions on Computing Education19, 3 (Sept. 2019), 1–16.
https://doi.org/10.1145/3282939
[6] Alexandria K. Hansen, Eric R. Hansen, Hilary A. Dwyer, Danielle B. Harlow,
and Diana Franklin. 2016. Differentiating for Diversity: Using Universal Design
for Learning in Elementary Computer Science Education. InProceedings of the
47th ACM Technical Symposium on Computing Science Education. ACM, Memphis
Tennessee USA, 376–381. https://doi.org/10.1145/2839509.2844570
[7] Nwannediya Ada Ibe, Rebecca Howsmon, Lauren Penney, Nathaniel Granor,
Leigh Ann DeLyser, and Kevin Wang. 2018. Reflections of a Diversity, Equity, and
Inclusion Working Group based on Data from a National CS Education Program. In
Proceedings of the 49th ACM Technical Symposium on Computer Science Education.
ACM, Baltimore Maryland USA, 711–716. https://doi.org/10.1145/3159450.3159594
[8] Michael Karlin, Anne Ottenbreit-Leftwich, and Yin-Chan Liao. 2023. Build-
ing a gender-inclusive secondary computer science program: teacher led and
stakeholder supported.Computer Science Education33, 1 (Jan. 2023), 117–138.
https://doi.org/10.1080/08993408.2022.2131281
2
