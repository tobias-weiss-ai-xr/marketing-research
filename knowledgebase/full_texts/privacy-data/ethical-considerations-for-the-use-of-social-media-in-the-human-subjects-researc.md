---
title: Ethical Considerations for the Use of Social Media in the Human Subjects Research Setting
url: https://doi.org/10.2196/78183
category: privacy-data
subcategory: review
date: 2025-08
venue: Journal of Medical Internet Research
authors:
- Tara B. Coffin
source: openalex-oa
pdf_url: https://btlj.org/data/articles2020/35_2/01-Wachter_WEB_03-25-21.pdf
pages: 64
chars: 193768
fetched_at: '2026-11-08T17:16:31+00:00'
kb_version: 1
---

# Ethical Considerations for the Use of Social Media in the Human Subjects Research Setting

AFFINITY PROFILING AND DISCRIMINATION BY
ASSOCIATION IN ONLINE BEHAVIORAL ADVERTISING
Sandra Wachter
†
ABSTRACT
Affinity profiling—grouping people according to their assumed interests rather than solely
their personal traits —has become commonplace in the online advertising industry. Online
platform providers use online behavioral advertisement (OBA) and can infer very sensitive
information (e.g., ethnicity, gender, sexual orientation, religious beliefs, etc.) about individuals to
target or exclude certain groups from products and services, or to offer different prices.
OBA and affinity profiling challenge at least three distinct interests: privacy, non -
discrimination, and group-level protection. This Article first examines several shortfalls of the
General Data Protection Regulation (GDPR) concerning governance of sensitive inferences and
profiling. It then shows the gaps of E.U. non-discrimination law in relation to affinity profiling
in terms of its areas of application as well as the types of attributes and people it protects.
Ultimately, applying the concept of “discrimination by association” can help close some of
these gaps in legal protection against OBA. This concept challenges the idea of strictly
differentiating between assumed interests and personal traits when profiling people.
Discrimination by association occurs when a person is treated significantly worse than others
(e.g., not being shown an advertisement) based on their relationship or association (e.g., assumed
gender or affinity) with a protected group.
Crucially, the individual does not need to be a member of the protected group to receive
protection, which negates the need for people who are part of the protected group to “out”
themselves as members of the group (e.g., sexual orientation or religion) to receive protection, if
they prefer. Finally, individuals who have been discriminated against but are not actually
members of the protected group (e.g., people who have been misclassified as women) could also
bring a claim. It would also strengthen the relationship of allies and support of civil rights
movements (e.g., LGBTQ+, religious, or women’s).
However, the lack of transparent business models could pose a considerable barrier to
proving non-discrimination cases. Finally, inferential analytics and AI expand the circle of
potential victims by grouping people according to inferred or correlated similarities and
characteristics unaccounted for in data protection and non-discrimination law. This Article closes
with policy recommendations to address each of these legal challenges.

  DOI: https://doi.org/10.15779/Z38JS9H82M
  © 2020 Sandra Wachter.
 †  Corresponding author. Sandra Wachter, Associate Professor and Senior Research Fellow, E-
mail: sandra.wachter@oii.ox.ac.uk Oxford Internet Institute, University of Oxford, 1 St. Giles, Oxford,
OX1 3JS, UK; the Alan Turing Institute, British Library, 96 Euston Road, London, NW1 2DB, UK.
The author would like to thank Dr. Brent Mittelstadt, Dr. Chris Russell, Emmanouil Bougiakiotis, Prof.
Philipp Hacker, participants of the Harvard Law Faculty workshop, all participants of the PLSC
conference, and, in particular, Frederik Borgesius, Josephine Williams, Ignacio Cofone, Gloria González
Fuster, and Gabriela Zanfir-Fortuna for their incredibly helpful and constructive feedback that improved
the quality of the paper. Finally, the authors would like to thank the incredible Berkeley Technology Law
Journal’s editorial team for their fantastic work. This work was supported by the British Academy
Postdoctoral Fellowship grant nr PF2\180114, DeepMind Technologies Limited, The Alan Turing
Institute, EPSRC grant EP/N510129/1, the Miami Foundation, and the Luminate Group.

368 BERKELEY TECHNOLOGY LAW JOURNAL [Vol. 35:367

TABLE OF CONTENTS
I. THE TROUBLE WITH AFFINITY PROFILING  ........................ 369
II. AN OVERVIEW OF LEGAL CHALLENGES TO OBA AND
AFFINITY PROFILING .................................................................  375
A. PRIVACY AND OBA ................................ ................................ ................ 375
B. DISCRIMINATION AND OBA ................................ ................................  377
C. AFFINITY PROFILING, SPECIAL CATEGORY DATA, AND THE GDPR
 ................................ ................................ ................................ ........ 380
III. E.U. NON-DISCRIMINATION LAW AND AFFINITY PROFILING
 .......................................................................................................... 385
A. PRIMARY LAW ................................ ................................ .........................  387
B. SECONDARY LAW ................................ ................................ ................... 388
1. Race and Ethnicity  ................................ ................................ ........... 388
2. Gender ................................ ................................ .............................  389
3. Religion or Belief, Disability, Age, or Sexual Orientation  .................. 390
4. Sectoral Divergence in Protected Groups  ................................ ............. 390
C. CURRENT CHALLENGES AND FUTURE OPPORTUNITIES FOR E.U.
NON-DISCRIMINATION LAW AND AFFINITY PROFILING ..... 392
IV. DISCRIMINATION BY ASSOCIATION AND AFFINITY
PROFILING .................................................................................... 394
A. DIRECT DISCRIMINATION BY ASSOCIATION: THE COLEMAN CASE
 ................................ ................................ ................................ ........ 394
B. INDIRECT DISCRIMINATION BY ASSOCIATION: THE CHEZ CASE .. 398
1. Particular Disadvantage That Is Significantly More Negative in Its Effects
on a Protected Group  ................................ ................................ ........ 402
2. Disproportionately Affected in a Negative Way (A Comparator)  ....... 404
C. JUSTIFICATION OF DISCRIMINATION ................................ .................. 407
V. PROTECTION OF NON-TRADITIONAL GROUPS ................... 413
VI. SOLUTIONS FOR ACCOUNTABILITY IN OBA AND AFFINITY
PROFILING .................................................................................... 418
A. A RIGHT TO REASONABLE INFERENCES IN OBA .............................  418
B. CURRENT GOVERNANCE STRATEGIES ................................ ............... 420
C. OPEN PROBLEMS ................................ ................................ ....................  423
D. POLICY RECOMMENDATIONS ................................ ...............................  427

2020] AFFINITY PROFILING AND OBA 369

I. THE TROUBLE WITH AFFINITY PROFILING
Advertisement practices are nothing new; they date back to the late 1950s,
when their primary goal—as it is today—was to learn about customers in order
to offer them desired products and services.1 However, today’s advertisements
pose new challenges. Digital technologies are now devised to peer even further
into the needs, interests, and motivations of customers. Behavioral advertising,
online profiling, and behavioral targeting2 have become common tactics for
suppliers to more effectively 3 offer product s4 to customers in the digital
environment.5
Modern targeted and behavioral advertisements typically involve
advertising networks that connect advertisers and publishers  (i.e., any entity
that wishes to host advertisements such as newspapers)  using targeting

 1. Ryan Calo, Digital Market Manipulation, 82 GEO. WASH. L. REV. 995, 997 (2013); see
generally ROBERT B. CIALDINI, INFLUENCE: THE PSYCHOLOGY OF PERSUASION  (2007).
 2. For more background on online behavioral advertisement (OBA), see generally
Sophie C. Boerman, Sanne Kruikemeier & Frederik J. Zuiderveen Borgesius, Online Behavioral
Advertising: A Literature Review and Research Agenda, 46 J. ADVERT. 363 (2017) (explaining what
OBA is and what the privacy concerns are); Edith G. Smit, Guda Van Noort & Hilde A.M.
Voorveld, Understanding Online Behavioural Advertising: User Knowledge, Privacy Concerns and Online
Coping Behaviour in Europe, 32 COMPUTERS HUM. BEHAV. 15 (2014) (investigating a study on
user knowledge of OBA and cookies, concerns about their privacy, how they cope with OBA,
cookies, and the requested informed consent); Steven C. Bennett, Regulating Online Behavioral
Advertising, 44 J. MARSHALL L. REV 899 (2011) (examining the regulatory efforts surrounding
OBA and the issues that arise when balancing notions of privacy against the needs  of an
information-based economy); Aleecia M. McDonald & Lorrie Faith Cranor, Beliefs and
Behaviors: Internet Users’ Understanding of Behavioral Advertising , TPRC 2010 (2010), https://
ssrn.com/abstract=1989092 (presenting empirical data on American adult internet users’
perceptions and knowledge on internet advertising techniques); Chang Dae Ham & Michelle
R. Nelson, The Role of Persuasion Knowledge, Assessment of Benefit and Harm, and Third -Person
Perception in Coping with Online Behavioral Advertising , 62 COMPUT. HUM. BEHAV. 689 (2016)
(discussing a study on OBA and third-party perception).
 3. See generally S. C. Matz, M. Kosinski, G. Nave & D. J. Stillwell, Psychological Targeting as
an Effective Approach to digital mass persuasion , 114 PROC. NAT’L ACAD. SCI. 12714 (2017)
(analyzing studies that utilized psychological assessment from digital footprints to determine
how psychological persuasion influences behavior); JAMES WILLIAMS, STAND OUT OF OUR
LIGHT: FREEDOM AND RESISTANCE IN THE ATTENTION ECONOMY (2018) (discussing how
companies want to capture our attention to sell goods and services).
 4. See generally Shoshana Zuboff, Big Other: Surveillance Capitalism and the Prospec ts of an
Information Civilization, 30 J. INFO. TECH. 75 (2015) (describing “surveillance capitalism” and
its implications through analysis of Google’s practices); SHOSHANA ZUBOFF, THE AGE OF
SURVEILLANCE CAPITALISM: THE FIGHT FOR A HUMAN FUTURE AT THE NEW FRONTIER OF
POWER (2019) (explaining consequences of surveillance capitalism spreading to every
economic sector).
 5. Calo, supra note 1, at 1002–04; see generally RICHARD H. THALER & CASS R. SUNSTEIN,
NUDGE: IMPROVING DECISIONS ABOUT HEALTH , WEALTH, AND HAPPINESS  (2009)
(discussing the topic of nudging).

370 BERKELEY TECHNOLOGY LAW JOURNAL [Vol. 35:367

technologies to assemble individual users into target audiences.6 In addition to
explicit profiles created from data provided by the user, predictive profiles are
created by combining user data, background databases, and other information
collected by tracking technologies. 7 Advertisers use these profiles to target
groups with—and exclude other groups from —product offers or
differentiated prices. Then, as a targeted user browses a publisher’s website,
advertisers compete via real-time bidding to place their advertisement on that
website.
These modern advertising techniques pose three  distinct challenges :
advertising can (1) potentially violate privacy , (2) unlawfully discriminate
against traditionally marginalized groups, and (3) discriminate against  and
violate the privacy of  non-traditional groups who receive inadequate legal
protection. Each of these challenges is unpacked in the remainder of this
Article; the discussion below provides an overview.
First, the threat to privacy is that “affinity profiling” could sidestep the
protections of the E.U. General Data Protection Regulation (GDPR).
“Affinity profiling” is profiling which does not directly infer a user’s sensitive
data (“special category data”) , such as personal traits or membership in
protected groups, but rather uses other data to measure the user’s “affinity”
for groups. In other words, affinity profiling looks for a similarity between the
assumed interests of a user and the interests of a group. Although Article 9 of
the GDPR provides higher protections against processing sensitive  personal
data (compared to non-sensitive personal data), it may fail to acknowledge a
potential relationship between assumed interests and sensitive personal traits.
Such a failure would render these higher data protection standards inapplicable
to “affinity groups,” despite the users’ assumed interests having strong and
potentially invasive disclosive power.8

 6.  ARTICLE 29 DATA PROTECTION WORKING PARTY, 17/EN WP251REV.01,
GUIDELINES ON AUTOMATED INDIVIDUAL DECISION-MAKING AND PROFILING FOR THE
PURPOSES OF REGULATION 2016/679, (last revised and adopted Feb. 6, 2018) [hereinafter WP
Feb. Guidelines ]; Frederik J. Zuiderveen Borgesius, Personal Data Processing for Behavioural
Targeting: Which Legal Basis? , 5 INT’L DATA PRIV. L. 163, 164 (2015); Chris Jay Hoofnagle,
Ashkan Soltani, Nathaniel Good, Dietrich J. Wambach & Mika D. Ayenson, Behavioral
Advertising: The Offer You Can’t Refuse, 6 HARV. L & POL’Y REV. 273, 275 (2012).
 7. WP Feb. Guidelines, supra note 6, at 7.
 8. See generally Michal Kosinski, David Stillwell & Thore Graepel, Private Traits and
Attributes Are Predictable from Digit al Records of Human Behavior, 110 PROC. NAT’L. ACAD. SCI.
5802 (2013) (describing how Facebook “likes” can reveal intimate information); Christopher
Burr, Nello Cristianini & James Ladyman, An Analysis of the Interaction Between Intelligent Software
Agents and Human Users, 28 MINDS & MACHINES 735 (2018) (providing an overview on what
sensitive information can be disclosed using inferential analytics).

2020] AFFINITY PROFILING AND OBA 371

Moreover, even if the GDPR recognizes that assumed inte rests reveal
sensitive information, this does not automatically equate to higher legal
protection for individuals and groups. T he General Court of the European
Court of Justice (ECJ) 9 and legal scholars 10 believe that for these higher
protections to apply to inferential analytics, data controllers must both intend
to draw sensitive inferences and use source data which provides a reliable basis
to learn about sensitive data. If these prerequisites are not met, which may be
the case in affinity profiling , the inferences drawn will not be considered
special category data or be subject to the stricter protections enshrined in
Article 9.
To ensure that sensitive affinity profiling is classified as a type of sensitive
data processing within the scope of the GDPR, these artificial thresholds of
intent and reliability would need to be abandoned. For platform providers , it
is not important to learn sensitive details about one particular user ( intent) or
to accurately place users into groups or audiences (reliability). As advertising
has a high tolerance for classification errors, if a user seems to behave similarly
enough to an assumed group (e.g., women), that is sufficient to treat the user
as a member of that group (e.g., to show ads for women’s shoes).
Second, with regards to E.U. non-discrimination law, the legal status of
“affinity groups,” or groups based on inferred interests, remains unclear. The
key question that courts and scholars will face going forward is: do affinity
groups have equivalent legal st atus to protected groups? For example, would
the affinity group “interested in Muslim culture” have equivalent legal status
to the group “religion”? The legal status of affinity groups under non -
discrimination law remains unclear. Answering this question is critical: if users
are segregated into groups and offered or excluded different products, services,
or prices on the basis of affinity, it could raise discrimination issues.11 The legal
status of affinity groups thus determines which—if any —types of claims can
be made under non- discrimination law. Failing to acknowledge the potential

 9. See Case T-190/10, Egan v. Parliament, ECLI:EU:T:2012:165, ¶ 84, 101 (Mar. 28,
2012) [hereinafter Egan].
 10. See infra Section II.C.
 11. On how higher prices are offered to lower income populations, see Jennifer
Valentino-DeVries, Jeremy Singer-Vine & Ashkan Soltani, Websites Vary Prices, Deals Based on
Users’ Information , WALL ST. J. (Dec. 24, 2012), https:// www.wsj.com/articles
/SB10001424127887323777204578189391813881534; Jeff Larson, Surya Mattu & Julia
Angwin, Unintended Consequences of Geographic Targeting , TECH. SCI. (Aug. 31, 2015), https://
techscience.org/a/2015090103/ (discussing a study that “found that [ZIP Code Tabulation
Areas] with higher percentages of Asian residents were more likely to be quoted one of the
higher prices”).

372 BERKELEY TECHNOLOGY LAW JOURNAL [Vol. 35:367

relationship—be it direct or indirect—between assumed interests and personal
traits could render non-discrimination regulation ineffective.
E.U. law recognizes both direct discrimination and indirect discrimination.
If affinity groups are granted a legal status equivalent to that of protected
groups, individuals would be able to appeal to direct discrimination laws for
protection. For direct discrimination to occur, less favorable actions must be
explicitly based on protected grounds or attributes (e.g., ethnicity), or a known
proxy thereof. To receive relief, a claimant must be part of the protected group
(i.e., “direct discrimination”).12 Affinity groups could be seen as equivalent to
protected groups on the basis that the affinity group (e.g. , “interested in
Muslim culture”) is defined against an explicit protected attribute (e.g. ,
“religion”) or a strong proxy for that attribute (e.g., “headscarf wearer”).13
If, on the other hand, affinity groups are not granted this equivalent
protective legal status, individuals would only be able to appeal to indirect
discrimination for protection. Indirect discrimination occurs when different
effects for protected groups result from otherwise “apparently neutral
provision, criterion or practice  . . . .”14 In this case, advertisements shown
based on assumed affinities would be treated as a type of “neutral provision”
because affi nity groups are not seen as equivalent to protected groups. To
establish discrimination under these conditions, the claimant must prima facie
show that the neutral provision could disproportionately affect a protected
group when compared with others in a similar situation. In practice, this would
mean that the claimant would need to show that a sufficient percentage of the
members of the affinity group are likely to be members of a protected group
(which would receive disproportionately negative treatment)  when compared
with others in a similar situation. For instance, this could be achieved by
appealing to demographic statistics. To receive relief, the claimant would need
to be a member of the disadvantaged protected group.
While remedies are available via direct and indirect discrimination laws,
they alone may be insufficient to fully protect affected parties. Thus, the

 12. EVELYN ELLIS & PHILIPPA WATSON, EU ANTI-DISCRIMINATION LAW 142–43
(2012).
 13. See, e.g., Case C-188/15, Bougnaoui, Association de défense des droits de l’hom me
(ADDH) v. Micropole SA, ECLI:EU:C:2017:204, ¶¶ 31–32 (Mar. 14, 2017) (leaving open
whether the ban of headscarves at the workplace is direct or indirect discrimination).
 14. This term is used in all E.U. non-discrimination directives. See, e.g., Council Directive
2000/43/EC, art. 2(2)(b), 2000 O.J. (L 180) 22, 24 (EC) (Racial Equality Directive); Council
Directive 2006/54/EC, art. 2(1)(b), 2006 O.J. (L 204) 23, 26 (EU) (Gender Equality Directive
(recast)); Council Directive 2004/113/EC, art. 2(b), 2004 O.J. (L 373) 37, 40 (EU) (Gender
Access Directive); Council Directive 2000/78/EC, art. 2(2)(b), 2000 O.J. (L 303) 16, 18 (EC)
(Employment Directive).

2020] AFFINITY PROFILING AND OBA 373

concepts of direct 15 and indirect 16 “discrimination by association” can help
increase algorithmic accountability and fairness in OBA.
Applying the concept of “discrimination by association” to OBA is
unprecedented,17 but would be a powerful tool in the quest for more
algorithmic accountability. “Discrimination by association” occurs when a
person is treated significantly worse than others (e.g. , not being shown an
advertisement) based on their relationship or association (e.g., assumed gender
or affinity) with a protected group. Protection is granted on the basis of an
individual’s association with a group defined by legally protected attributes (or
an accepted proxy) which have led to differential treatment or results (e.g. ,
being shown advertisements for lower paying jobs).
This could have implications for OBA for three main reasons . First, it
would overcome the argument that inferring one’s “affinity for” and
“membership in” a protected group are strictly unrelated. If an interest group
is seen as equivalent to a protected group, it does not matter whether the
measure taken is based on a protected attribute that an individual possesses or
because they are somehow associated with the protected group (e.g., having an
interest in a specific culture). In such a case, claims under direct discrimination
by association are possible. Second, both direct and indirect discrimination
require the claimant to be a member of the protected group in order to receive
relief. As a result, to invoke either type of claim under non-discrimination law,
affected parties may need to “out” themselves (e.g., in relation to sexual
orientation or religion). This could be a problem, as there might be reasons an
individual may not wish to disclose potentiall y sensitive personal attributes.
Discrimination by association negates the need for people who are part of the
protected group to “out” themselves as members of the group in order to
receive protection. Finally, because claimants do not need to be members of
the protected group to receive protection, individuals who have received
discriminatory treatment but are not actually members of the protected group
(e.g., people who have been misclassified as women) could also bring a claim.
Both wrongly and accurately classified people who suffered adverse treatment
because of their assumed affinity and interests can claim relief via
discrimination by association. Widening the circle of potential claimants could

 15. See, e.g., Case C -303/06, Coleman v. Law, 2008 E.C.R. I -415 [hereinafter Coleman]
(providing an example of direct discrimination).
 16. See, e.g., Case C-83/14, CHEZ Razpredelenie Bulgaria AD v. Komisia za zashtita ot
diskriminatsi, ECLI:EU:C:2015:480 (July 16, 2015) [hereinafter CHEZ] (providing an example
of indirect discrimination).
 17. The notion of direct and indirect discrimination by association was established in
Coleman, supra note 15, and CHEZ, supra note 16.

374 BERKELEY TECHNOLOGY LAW JOURNAL [Vol. 35:367

also have the positive side effect of strengthening the  relationship of allies of
civil rights movements (e.g., LGBTQ+, religious, women’s). Moreover, not
granting protection to misclassified users could have an undesirable chilling
effect due to fear over potential negative consequences based on associating
with these groups.
Most interestingly, an ECJ judgment shows that certain seemingly neutral
actions can also constitute direct discrimination (by association). 18 If affinity
profiling is seen as direct discrimination, almost no legal justification will be
available to publishers or advertisers.19 Even if affinity profiling is only seen as
indirect discrimination, economic and business concerns alone are unlikely to
justify differential results.20 However, practical challenges remain, such as the
lack of algorithmic transparency and opaque business models , that will make
it difficult for affected parties to demonstrate prima facie discrimination.
Finally, the third challenge that OBA poses is to non- traditional groups.
Even with the most generous interpretation of data protection and non -
discrimination law , profiling and inferential analytics disrupt fundamental
tenets of data protection and non- discrimination law, and may render them
inapplicable. The scope of data protection law may fall short because profiling
can occur without identifying an individual and often without using any
personal data. 21 And the scope of non- discrimination law may fall short
because c onstructed groups do not necessarily  map onto legally protected
characteristics based on historical lessons .22 Both legal frameworks must be
revised to account for the privacy of “ad hoc groups” to overcome these
shortcomings.23
This Article examines in detail the three challenges that OBA and affinity
profiling pose in terms of privacy protection, non -discrimination, and group
privacy. It proceeds as follows. Part II explores the regulation around the
collection and legitimate uses of sensitive data and inferences. This Part reveals
current limitations and loopholes in the GDPR. Part III examines E.U. non-
discrimination law and sheds light on the lack of comprehensiveness in t he
types of decision-making and people it protects. Part IV focuses on direct and
indirect discrimination by association and explores its potential to close current
accountability gaps in relation to OBA and affinity profiling. Part V discusses

 18. CHEZ, supra note 16, at ¶ 129(3).
 19. ELLIS & WATSON, supra note 12, at 173.
 20. See infra Section IV.C.
 21. Sandra Wachter, Data Protection in the Age of Big Data, 2 NATURE ELEC. 6, 7 (2019).
 22. See Alessandro Mantelero, AI and Big Data: A Blueprint for a Human Rights,  Social and
Ethical Impact Assessment, 34 COMPUT. L. & SEC. REV. 754, 765 (2018).
 23. Brent Mittelstadt, From Individual to Group Privacy in Big Data Analytics , 30 PHIL. &
TECH. 475, 476, 485 (2017).

2020] AFFINITY PROFILING AND OBA 375

the concept  of group privacy  and the “right to reasonable inferences ” as
necessary tool s to close existing gaps in privacy and non- discrimination
protection. Finally, Part VI discusses current governance strategies and closes
with a set of recommendations on what kind of transparency tools should be
offered to users to increase algorithmic transparency and accountability in
OBA.24
II. AN OVERVIEW OF LEGAL CHALLENGES TO OBA AND
AFFINITY PROFILING
OBA and affinity profiling face several significant legal challenges in
Europe across privacy, data protection, and non-discrimination law.
A. PRIVACY AND OBA
The most evident concern with OBA is its potential to violate  individual
privacy.25 Internet technologies can be used to track users across the web over
time and gather information about their surfing behavior and interests.26 This
information is then used to build profiles which can be very invasive, often
revealing users’ explicit and subconscious intere sts, personality traits, and
behaviors.27 Among other things , tailored advertising can be based on those
profiles.28 To tailor advertising to specific users, ad networks use cookies29 that
record information about the users and remember if they return to specific

 24. It is worth noting that this Article does not examine consumer protection law, such
as Directive 2006/114/EC concerning misleading and comparative advertising and Directive
2005/29/EC concerning unfair commercial practices. While potentially relev ant, these
frameworks go beyond the scope of this Article.
 25. See Bennett, supra note 2, at 904–06; see also Tal Z. Zarsky, Privacy and Manipulation in
the Digital Age, 20 THEORETICAL INQUIRES L. 157, 158 (2019).
 26. See, e.g., Bin Bi, Milad Shokouhi, Michal Kosinski & Thore Graepel, Inferring the
Demographics of Search Users: Social Data Meets Search Queries , in PROC. 22ND INT ’L CONF . ON
WORLD WIDE WEB 131 (2013); Alvaro Ortigosa, Rosa M. Carro & José Ignacio Quiroga,
Predicting User Personality by Mining Social Interactions in Facebook , 80 J. COMPUT. SYS. SCI. 57
(2014); Zijian Wang, Scott A. Hale, David Adelani, Przemyslaw A. Grabowicz, Timo Hartman,
Fabian Flöck & David Jurgens, Demographic Inference and Representative Population Estimates from
Multilingual Social Media Data, in WORLD WIDE WEB CONF. 2056 (2019).
 27. See generally Matz et al., supra note 3.
 28. See Omer Tene & Jules Polenetsky, To Track or “Do Not Track”: Advancing Transparency
and Individual Control in Online Behavioral Advertising , 13 MINN. J.L. SCI. & TECH. 281, 282–83
(2012); WP Feb. Guidelines, supra note 6, at 7.
 29. Andrew McStay, I Consent: An Analysis of the Cookie Directive and Its Implications for UK
Behavioral Advertising, 15 NEW MEDIA & SOC’Y 596, 597–98 (2013). For more on the numerous
different tracking cookies, see Jonathan R. Mayer & John C. Mitchell, Third-Party Web Tracking:
Policy and Technology, 2012 IEEE SYMP. ON SECURITY & PRIVACY 413, 420–21 (2012).

376 BERKELEY TECHNOLOGY LAW JOURNAL [Vol. 35:367

websites or visit partner sites. 30 Sites sometimes also add additional
information, such as zip code, age , or gender, based on user activity such as
search queries. Each piece of information helps the ad network to serve
appropriate ads for the user.31 Sophie C. Boerman et al.32 provide an overview
of the methods (e.g., flash cookies and device fingerprints 33) as well as
characteristics and data tracked in behavioral advertising. According to them,
profiles are built from various types of data such as clicking and page-reading
behavior, geolocation, videos watched, and search queries,34 as well as app-use
data, purchases, posts on social media, and emails.35
The constant collection and evaluation of personal data enables companies
to gain very intimate insights into the lives of their customers. Using sensitive
tags to target users has become common practice. 36 Many scholars have long
been aware of these issues,37 with some believing that advertisers will continue
to increasingly rely on personalized and targeted advertising in the future. 38
Potentially sensitive information such as religious or political beliefs, sexual

 30. WP Feb. Guidelines, supra note 6, at 6.
 31. Bennett, supra note 2, at 900.
 32. Boerman et al., supra note 2, at 364 (finding evidence of widespread use of inferential
analytics).
 33. See Ibrahim Altaweel, Nathaniel Good & Chris Jay Hoofnagle, Web Privacy Census,
TECH. SCI. (2015), https://techscience.org/a/2015121502/.
 34. For an overview of existing methods of OBA, see Boerman et al., supra note 2, at
364.
 35. See Frederik J. Zuiderveen Borgesius, Improving Privacy Protection in the Area of
Behavioural Targeting (manuscript at 1) (Sept. 1, 2015), https:// papers.ssrn.com/sol3
/papers.cfm?abstract_id=2654213.
 36. Juan Miguel Carrascosa, Jakub Mikians, Ruben Cuevas, Vijay Erram illi & Nikolaos
Laoutaris, I Always Feel like Somebody’s Watching Me: Measuring Online Behavioural Advertising , in
PROC. 11TH ACM CONF. ON EMERGING NETWORKING EXPERIMENTS & TECH. 1, 1– 2
(2015).
 37. See, e.g. , VIKTOR MAYER-SCHÖNBERGER & THOMAS RAMGE, REINVENTING
CAPITALISM IN THE AGE OF BIG DATA (2018); Tene & Polenetsky, supra note 28; Bennett,
supra note 2; Frederik J. Zuiderveen Borgesius, Singling Out People Without Knowing Their Names–
Behavioural Targeting, Pseudonymous Data, and the New Data Protection Regulation, 32 COMPUT. L. &
SEC. REV. 256 (2016); Calo, supra note 1; VIKTOR MAYER-SCHÖNBERGER & KENNETH
CUKIER, BIG DATA : A REVOLUTION THAT WILL TRANSFORM HOW WE LIVE, WORK AND
THINK (2013); Tal Z. Zarsky, Mine Your Own Business: Making the Case for the Implications of the
Data Mining of Personal Information in the Forum of Public Opinion, 5 YALE J.L. & TECH. 1 (2002);
Danielle Keats Citron & Frank Pasquale, The Scored Society: Due Process for Automated Predictions,
89 WASH. L. REV. 1 (2014); FRANK PASQUALE, THE BLACK BOX SOCIETY: THE SECRET
ALGORITHMS THAT CONTROL MONEY AND INFORMATION (2015).
 38. See, e.g. , Boerman et al., supra note 2, a t 363; V. Kumar & Shaphali Gupta,
Conceptualizing the Evolution and Future of Advertising, 45 J. ADVERT. 302, 303 (2016); Don Schultz,
The Future of Advertising or Whatever We’re Going to Call It , 45 J. ADVERT. 276, 283–84 (2016);
Roland T. Rust, Comment: Is Advertising a Zombie?, 45 J. ADVERT. 346, 346–47 (2016).

2020] AFFINITY PROFILING AND OBA 377

orientation, race or ethnicity, physical or mental health status, or sex or gender
identity can be inferred from online behavior without users ever being aware.39
For example, researchers suggested that Facebook can infer sexual orientation
(and other sensitive characteristics) based on a user’s interactions with the
platform.40
B. DISCRIMINATION AND OBA
Discrimination is also a common concern with OBA among scholars.
According to Ariel Ezrachi and Maurice E. Stucke, from an economic
perspective, the “rise of behavioural discrimination” and price discrimination
can limit the autonomy of consumers in choosing products and their power
on the free market. 41 However, privacy, personalization, and price
discrimination are not the only concerns with OBA. A landmark study by
Latanya Sweeney revealed how OBA can reinforce racial stereotypes,
stigmatize users, and possibly illegally discriminate. 42 Her study showed that
names associated with Black people prompted more ads by
“instantcheckmate.com”—indicating an arrest—than was the case for names
associated with White people. 43 The causal root of this finding is not self-
evident; it may be roote d in the methods advertisers use to market their
product (e.g., search criteria, ad text, and bids), or it may reflect the clicking
behavior of users. The optimization of OBA algorithms towards higher
clickthrough rates can inadvertently reinforce stereotypes.44
Unfortunately, this is not the only example of discriminatory OBA. In
general, research suggests that algorithms can be inadvertently biased favoring
men over women for STEM jobs on platform s such as Facebook, Google,
Instagram, and Twitter. 45 This trend cannot be attributed entirely to
algorithmic reinforcement of stereotypes . ProPublica published a series of

 39. See Sandra Wachter & Brent Mittelstadt, A Right to Reasonable Inferences: Re -Thinking
Data Protection Law in the Age of Big Data and AI, 2 COLUM. BUS. L. REV. 494, 506–10 (2019).
 40. José González Cabañas, Ángel Cuevas & Rubén Cuevas, Facebook Use of Sensitive
Data for Advertising in Europe  (Feb. 14, 2018) (u npublished manuscript), https://
arxiv.org/pdf/1802.05030.pdf. For a discussion of the revealing power of Facebook “likes,”
see Kosinski, Stillwell & Graepel, supra note 8, at 5802–04.
 41. Ariel Ezrachi & Maurice E. Stucke, The Rise of Behavioural Discrimination , EUR.
COMPETITION L. REV. 485, 485–90 (2016); see also Frederik Zuiderveen Borgesius & Joost
Poort, Online Price Discrimination and EU Data Privacy Law, 40 J. CONSUMER POL’Y 347 (2017).
 42. See Latanya Sweeney, Discrimination in Online Ad Delivery , 11 ACM Queue 10, 19
(2013).
 43. Id. at 4.
 44. Id. at 14–15.
 45. L. Elisa Celis, Anay Mehrotra & Nisheeth K. Vishnoi, Toward Controlling
Discrimination in Online Ad Auctions  (May 22, 2019) (unpublished manuscript), https://
arxiv.org/pdf/1901.10450.pdf.

378 BERKELEY TECHNOLOGY LAW JOURNAL [Vol. 35:367

reports showing that Facebook allows advertisers to exclude certain groups
(e.g., from housing, employment, and credit offers),  based on ethnicity46 or
gender.47 Facebook has also used the “likes” of users to infer sexual orientation
and has allowed advertisers to serve young LGBTQ+ users “gay cure”
advertisements.48 Only recently has Facebook announced a change to their
policy: when placing ads in relation to housing, jobs, or credit, advertisers can
no longer use classes such as race, ethnicity, sexual orientation, and religion as
general targeting options.49
However, Facebook still allows advertisers to create custom audiences
based on personally identifiable information (PII), for instance by  matching
visitors of pages with Facebook users via Pixel. 50 Custom audiences can be
used by advertisers to target people based on gender, location, age, language,
“lookalike audiences,”51 source audiences52 (e.g., fans of a Facebook page), and

 46. Terry Parris Jr., Julia Angwin & Madeleine Varner, Facebook Lets Advertisers Exclude
Users by Race , PROPUBLICA (Oct. 28, 2016), https:// www.propublica.org/article/facebook
-lets-advertisers-exclude-users-by-race; Ariana Tobin & Julia Angwin, Facebook (Still) Letting
Housing Advertisers Exclude Users by Race , PROPUBLICA (Nov. 21, 2017), https://
www.propublica.org/article/facebook-advertising-discrimination-housing-race-sex-national
-origin; Ariana Tobin & Jeremy B. Merrill, Facebook Moves to Block Ad Transparency Tools —
Including Ours , PROPUBLICA (Jan. 28, 2019), https:// www.propublica.org/article/facebook
-blocks-ad-transparency-tools.
 47. Jeremy B. Merrill & Ariana Tobin, Facebook Is Letting Job Advertisers Target Only Men,
PROPUBLICA (Sept. 18, 2018), https:// www.propublica.org/article/facebook-is-letting-job
-advertisers-target-only-men.
 48. Helena Horton & James Cook, Facebook Accused of Targeting Y oung LGBT Users with
“Gay Cure” Adverts , TELEGRAPH (Aug. 25, 2018), https:// www.telegraph.co.uk/news/2018
/08/25/facebook-accused-targeting-young-lgbt-users-gay-cure-adverts/.
 49. Sheryl Sandberg, Doing More to Protect Against Discrimination in Housing, Employment and
Credit Advertising, FACEBOOK NEWSROOM, https://about.fb.com/news/2019/03/protecting
-against-discrimination-in-ads/ (last visited Mar 24, 2019). A promise to change this policy
was made in the past as well. See Ariana Tobin, Facebook Promises to Bar Advertisers From Targeting
Ads by Race or Ethnicity. Again. , PROPUBLICA (2018), https:// www.propublica.org/article
/facebook-promises-to-bar-advertisers-from-targeting-ads-by-race-or-ethnicity-again.
 50. About Reaching New Audiences , FACEBOOK FOR BUSINESS, https://
www.facebook.com/business/help/717368264947302?id=176276233019487 (last visited
April 20, 2020).
 51. About Lookalike Audiences , FACEBOOK FOR BUSINESS, https://www.facebook.com
/business/help/164749007013531?id=401668390442328 (last visited Mar 24, 2019) (“A
Lookalike Audience is a way to reach new people who are likely to be interested in your
business because they’re similar to your best existing customers.”). For more on the privacy
risks of this method, see generally Giridhari Venkatadri, Athanasios Andreou, Yabing Liu,
Alan Mislove, Drishna P. Gummadi, Patrick Loiseau & Oana Goga, Privacy Risks with Facebook’s
PII-Based Targeting: Auditing a Data Broker’s Advertising Interface , 2018 IEEE SYMP. ON SEC. &
PRIV. 89 (2018).
 52. Source Audience, FACEBOOK FOR BUSINESS, https:// en-gb.facebook.com/business
/help/475669712534537 (last visited Mar 24, 2019).

2020] AFFINITY PROFILING AND OBA 379

detailed targeting.53 Detailed targeting allows advertisers to target or exclude
people based on preferences, intents, or behaviors (e.g., travel, time spent on
a network, education, pages they engage with, relationship status, income,
children, or political affiliation) for users in certain locations.54 Till Speicher et
al. thus suggest that the concerns raised above remain because proxy data can
be used in lieu of explicit sensitive characteristics and platform data can be
linked to public (e.g., voter registration) and private datasets (e.g. , via data
brokers) to gain intimate insights about users. 55 According to Speicher et al.,
similar approaches seem to be taken by platforms such as Twitter, Pinterest,
LinkedIn, and YouTube.56
These examples demonstrate that affinity profiling and detecting bias are
more than a technological challenge. It is also a societal challenge 57 made
possible by implicit and explicit biases58 and stereotypical thinking. They reveal

 53. About Detailed Targeting , FACEBOOK FOR BUSINESS, https:// www.facebook.com
/business/help/182371508761821?id=176276233019487 (last visited May 11, 2019).
 54. See Mary Lister,  All of Facebook's Ad Targeting Options in 1 Epic Infographic ,
WORDSTREAM BLOG (Feb. 26, 2020) https:// www.wordstream.com/blog/ws/2016/06/27
/facebook-ad-targeting-options-infographic (last visited Mar 24, 2019). Some of these options
are available only in the United States.
 55. See Till Speicher, Muhammad Ali, Giridhari Venkatadri, Filipe Nune s Ribeiro,
George Arvanitakis, Fabrício Benevenuto, Drishna P. Gummadi, Patrick Loiseau & Alan
Mislove, Potential for Discrimination in Online Targeted Advertising Till Speicher MPI-SWS MPI-SWS
MPI-SWS, in 81 PROC. CONF. ON FAIRNESS, ACCOUNTABILITY, & TRANSPARENCY 1, 5
(2018).
 56. Id. at 2.
 57. See generally CATHY O’NEIL, WEAPONS OF MATH DESTRUCTION: HOW BIG DATA
INCREASES INEQUALITY AND THREATENS DEMOCRACY (2017); VIRGINIA EUBANKS,
AUTOMATING INEQUALITY: HOW HIGH-TECH TOOLS PROFILE, POLICE, AND PUNISH THE
POOR (2018); SAFIYA UMOJA NOBLE, ALGORITHMS OF OPPRESSION: HOW SEARCH ENGINES
REINFORCE RACISM (2018).
 58. See generally Matt Kusner, Joshua Loftus, Chris Russell & Ricardo Silva, Counterfactual
Fairness, in PROC. 31ST CONF. ON NEURAL INFO. PROCESSING SYS. 4069 (2017) (discussing the
challenges of detecting bias in data sets); Chris Russell, Matt J. Kusner, Joshua R. Loftus &
Ricardo Silva, When Worlds Collide: Integrating Different Counterfactual Assumptions in Fairness , in
PROC. 31ST CONF. ON NEURAL INFO. PROCESSING SYS. 6396 (2017); Cynthia Dwork, Moritz
Hardt, Toniann Pitassi, Omer Reingold & Richard Zemel, Fairness Through Awareness (Nov.
30, 2011) (unpublished manuscript), https://arxiv.org/pdf/1104.3913.pdf; Sorelle A. Friedler,
Carlos Scheidegger & Suresh Venkatasubramanian, On the (Im)Possibility of Fairness (Sept.
23, 2016) (unpublished manuscript), https:// arxiv.org/pdf/1609.07236.pdf; Nina Grgić -
Hlača, Muhammad Bilal Zafar, Krishna P. Gummadi & Adrian Weller, The Case for Process
Fairness in Learning: Feature Selection for Fair Decision Making , in NIPS SYMP. ON MACHINE
LEARNING & L. (2016); Celis, Mehrotra & Vishnoi, supra note 45; Speicher et al., supra note
55.

380 BERKELEY TECHNOLOGY LAW JOURNAL [Vol. 35:367

that discriminatory behavior can be profitable, which can incentivize
companies to allow advertisers to exclude specific groups.59
C. AFFINITY PROFILING, SPECIAL CATEGORY DATA, AND THE GDPR
When first confronted with the issues of affinity profiling, Facebook
explained that they do not infer ethnicity directly, but rather only infer affinity
with a specific culture based on a user’s interaction with the platform (e.g. ,
likes, friends, and groups).60 How does this argument fit within the context of
European data protection law?
Under Art icle 9 of the GDPR, the proces sing of sensitive data is only
allowed under certain circumstances. Article 9 provides an exclusive list of data
types that necessitate higher levels of protection, including ethnic origin,
political opinions, religious or philosophical beliefs, trade union membership,
and data concerning a natural person’s sex life or sexual orientation.61
This list does not cover all known types of data that can cause stigma and
discrimination. For example, sex and gender are not included in the list. The
Article 29 Working Party discussed this lack of comprehensiveness in an
advice paper and suggested expanding the definition of sensitive data in future
regulation to at least include information about financial status, minors,
geolocation, and profiles.62 This is a sensible approach because financial status
and geolocation are known to be strong proxies for gender or sex and ethnicity.
It is noteworthy, however, that the Working Party did not propose to include
gender or sex as a type of sensitive data, even though this t ype of data can
cause discrimination. 63 In the end, the Working Party’s proposal was not
adopted in the GDPR. This is a worrying result as all these types of data can
be the root of unfair or unjust treatment.

 59. See Muhammad Ali, Piotr Sapiezynski, Miranda Bogen, Aleksandra Korolova, Alan
Mislove & Aaron Rieke, Discrimination Through Optimization: How Facebook’s Ad Delivery Can Lead
to Skewed Outcomes, in 3 PROC. ACM ON HUM.-COMPUT. INTERACTION 1, 1 (2019).
 60. Alex Hern, Facebook’s “Ethnic Affinity” Advertising Sparks Concerns of Racial Profiling ,
GUARDIAN (Mar. 22, 2016), https:// www.theguardian.com/technology/2016/mar/22
/facebooks-ethnic-affinity-advertising-concerns-racial-profiling.
 61. Regulation (EU) 2016/ 679 of the European Parliament and of the Council of 27
April 2016 on the protection of natural persons with regard to the processing of personal data
and on the free movement of such data, and repealing Directive 95/ 46/EC (General Data
Protection Regulation), 2016 O.J. (L 119) 1 [hereinafter GDPR].
 62. Article 29 Data Prot. Working Party, Advice Paper on Special Categories of Data
(“Sensitive Data”), at 10, A res(2011)444105 - 20/04/2011 (2011), https://perma.cc/Q6PY
-9KAP (last visited Oct 1, 2017) [hereinafter Art. 29 WP Advice Paper].
 63. For an extensive discussion on several laws failing to guard against sensitive
inferences, see generally Wachter & Mittelstadt, supra note 39.

2020] AFFINITY PROFILING AND OBA 381

Following the advice paper of the Article 29 Working Party (“Working
Party”) on the definition of personal data and the phrasing in Art icle 9 of the
GDPR (specifically the usage of the word “revealing” in the definition),64 it is
safe to assume that “special category data” covers both sensitive data and data
that can be sensitive by inference. In other words, “special category data” is
not limited to data that directly reveals sensitive information such as “religion,”
but also includes data from which sensitive information can be concluded (e.g.,
a picture showing a person wearing religious attire).65
With regards to inference, academics disagree on the requirements for
personal data to be classified as sensitive data.66 For some, the intent to infer
sensitive attributes is required (an intention requirement). For example, if a
pizzeria delivers food to customers in a drug abuse center, their addresses are
not considered sensitive data because the pizzeria is presumably not interested
in inferring their health status.67 Similarly, it has been suggested that if sensitive
data is only captured coincidentally it should not be classified as sensitive,
unless the type of data is known to contain sensitive content. Following this
reasoning, it has been argued that images captured by CCTV camera of visitors
of “gay meeting spots” would not be considered sensitive data unless the
purpose of the camera was to record “gay meeting spots.”68 The same has been
argued for camera footage capturing people wearing religious attire. 69
However, the Working Party has argued that camera footage is inherently
problematic because it can reveal ethnic origin or health status.70
In addition to the intention requirement, some scholars argue that there is
a second requirement: the data collected must provide a reliable basis to infer

 64. See Art. 29 WP Advice Paper, supra note 62, at 6 (“The term ‘data revealing racial or
ethnic origin, political opinions, religious or philosophical beliefs, trade-union membership’ is
to be understood that not only data which by its nature contains sensitive information is
covered by this provision, but also data from which se nsitive information with regard to an
individual can be concluded.”).
 65. See Alexander Nguyen, Videoüberwachung insensitiven Bereichen , 35 DATENSCHUTZ
DATENSICHERHEIT 715, 715 (2011) (discussing CCTV and pictures allowing sensitive
inferences).
 66. For an overview on this academic debate, see Wachter & Mittelstadt, supra note 39,
at 560–68.
 67. Sebastian Schulz, Art. 9 Verarbeitung besonderer Kategorien personenbezogener Daten , in
DATENSCHUTZ-GRUNDVERORDNUNG VO (EU) 2016/679 295 xi–xiv (Peter Gola ed., 1st ed.
2017).
 68. Nguyen, supra note 65, at 517.
 69. Schulz, supra note 67, at xii–xiii.
 70. Art. 29 WP Advice Paper, supra note 62, at 8 (stating that a particular data type can
be problematic in terms of revealing sensitive attributes without regard to the intent or purpose
of the controller collecting the data, thereby logically suggesting that intention may be
irrelevant to the classification of personal data as sensitive data).

382 BERKELEY TECHNOLOGY LAW JOURNAL [Vol. 35:367

sensitive attributes. For example, pornographic browsing history is seen as
sufficient to infer sexual orientation, geolocation of cell phones at political
events can be used to infer political beliefs, and names, country of birth, and
addresses provide a reliable basis to infer ethnicity or religious beliefs.71 Some
scholars also argue that reliability does not need to be unambiguously proven
for the classification to apply; it is sufficient that a data controller can
realistically make these assumptions, taking into account the purpose of data
collection ( i.e., intent).72 In contrast, other scholars deny that the
aforementioned data types have sufficient sensitive disclosive power to qualify
as special category data.73
The General Court has previously affirmed that reliability is a necessary
precondition to transform personal data into sensitive data. In Egan v.
Parliament, the complainants requested access to the names of the personal
assistants of a member of the European Parliament. 74 The personal assistants
did not want this information to be disclosed, arguing that their working
relationship could be used to infer their political stances. The court ruled that
an employment relationship is not sufficiently reliable to draw inferences about
political beliefs.75
What does this mean for affinity profiling? In order for Art icle 9 of the
GDPR to apply, sensitive data or data that is sensitive by inference has to be
collected or processed. The argument that higher protection standards should
not apply if the data is used to infer an affinity with an ethnicity, rather than
ethnicity directly, is problematic because it too narrowly interprets the scope

 71. ALEXANDER SCHIFF, DS-GVO Art. 9 Besonderer Kategorien personenbezogener Daten , in
DATENSCHUTZ-GRUNDVERORDNUNG 334 xxvi –xxvii (Eugen Ehmann & Martin Selmayr
eds., 1st ed. 2017).
 72. Id. at xx–xxii.
 73. Schulz, supra note 67, at xii–xiii.
 74. Egan, supra note 9, at ¶ 101.
 75. The Court explains:
Furthermore, in response to the applicants’ argument that data concerning
former MEP assistants were previously accessible, the Parliament argued,
in its defence, that it cannot release such data, as they would reve al the
assistants’ political opinions and would therefore be sensitive data within
the meaning of Article 10 of Regulation No 45/ 2001 . . . . However, that
argument, which, moreover, is not in any way substantiated, cannot, in any
event, make up for the fact that the contested decision failed to show why
disclosure of those data would specifically and effectively undermine their
right to privacy within the meaning of Article 4(1)(b) of Regulation No
1049/2001.
Id. (internal citations omitted).

2020] AFFINITY PROFILING AND OBA 383

of “special category data.” 76 Such data has great inferential power because
personal interests allow inferences to be drawn about personal traits. In other
words, an interest in something sensitive (e.g., LGBTQ+ rights) is different
than collecting sensitive data about a user (e.g. , sexual orientation). Failing to
acknowledge the power of sensitive disclosures about a person’s life made
possible by assuming their interests will render the higher protection in the
GDPR inapplicable , meaning only the normal standards for personal data
would apply.
However, even if this disclosive power is acknowledged, intent and
reliability are problematic thresholds when applied to targeted advertising and,
especially, affinity profiling. The main reason is that sensitive attributes do not
need to be intentionally inferred to have an influence on advertisements. For
example, as mentioned above, Facebook explained that they have no intention
to infer sensitive traits, but only to assume an affinity. 77 Despite this lack of
intent, Facebook was accused of inferring very intimate details about their
users by proxy (e.g., ethnicity, sexual orientation, and political views).78 If proxy
data (e.g., assumed interests) can reveal sensitive traits without any intent to do
so, it shows that this artificial threshold to turn personal data into sensitive
data is misguided. If this view is continued, companies could learn sensitive
information about users without necessarily being bound to the higher
safeguards and standards in the GDPR that normally accompany such data. In
effect, they could be able to advertise to users based on sensitive
characteristics, or an affinity with such characteristics, without incurring the
higher legal safeguards in Article 9 that such advertising would normally incur.
The requirement of reliability for the GDPR to protect this type of data is
also a red herring and very problematic for advertisements. The question is not
only whether sensitive information can be reliably inferred, but also how these
inferences change the way advertisers and platform providers treat their users.
It is also problematic that sexual orientation, for instance, is inferred, be it

 76. GDPR, supra note 61, at 38 (art. 9). Special category data is defined as “personal data
revealing racial or ethnic origin, political opinions, religious or philosophical beliefs, or trade
union membership, and  the processing of genetic data, biometric data for the purpose of
uniquely identifying a natural person, data concerning health or data concerning a natural
person’s sex life or sexual orientation . . . .” Id. The phrase “personal data revealing” shows
that the definition is not intended to only capture explicit usage of protected attributes, but
rather data that when processed can reveal information about one of the listed categories. See
id. Data revealing an affinity with an ethnicity should thus be considered special category data.
 77. Hern, supra note 60.
 78. Parris Jr. et al., supra note 46; Horton & Cook, supra note 48; Alex Hern, Facebook Lets
Advertisers Target Users Based on Sensitive Interests , GUARDIAN (May 16, 2018), https://
www.theguardian.com/technology/2018/may/16/facebook-lets-advertisers-target-users
-based-on-sensitive-interests.

384 BERKELEY TECHNOLOGY LAW JOURNAL [Vol. 35:367

directly or by affinity, but the harm may continue after the inference is drawn.
Platform providers tailor content (e.g. , ads, news feeds, and search results)
based on these assumptions (e.g., based on assumed gender). Platforms do not
necessarily care whether they accurately place users into certain groups; rather,
what matters is whether the user behaves similarly enough to the assumed
group to be treated as a member of t he group. The opportunity cost of
showing ads intended for women to men that have been misclassified is very
low. The business model of OBA can tolerate  relatively high rates of
misclassification. This tolerance does not, however, benefit misclassified users
who are offered inaccurate or discriminatory content and may suffer as a result.
The focus on reliability is therefore misguided. People will be treated
differently based on their assumed affinity, regardless of whether this
assumption is correct.
If the reliability requirements advanced by the General Court and some
scholars are upheld, it could render Art icle 9 inapplicable to affinity profiling
and leave the data with only the normal standards of data protection. This is
problematic given that affinity profiling (which does not require an intention
to infer sensitive data) could cause the same privacy harms as direct collection
and inference of sensitive data.
The Working Party offers a more generous definition in their guidelines
on sensitive data. 79 This definition is operationalized in their guidelines on
OBA, where they argue , “if an ad network provider processes individual
behavior in order to ‘place him/her ’ in an interest category indicating a
particular sexual preference they would be process ing ‘sensitive data.’ ”80
According to the European Data Protection Board’s guidelines on the
targeting of social media users , this holds true regardless of whether  the
inferences are accurate (e.g., if the person is actually  politically right or left
wing).81 This view aligns with the European Data Protection Board’s opinion
on inferred political views. 82 Unfortunately, the European Data Protection
Board seems to insist on the intent requirement, and so personal data only

 79. Art. 29 WP Advice Paper, supra note 62, at 6.
 80. ARTITCLE 29 DATA PROTECTION WORKING PARTY, Opinion 2/2010 on online
behavioural advertising , 00909/10/EN WP 171 20 (2010), https://ec.europa. eu/justice
/article-29/documentation/opinion-recommendation/files/2010/wp171_en.pdf (last visited
Mar. 22, 2019) [hereinafter "Art. 29 Data Prot. Working Party, Opinion 2/2010"].
 81. Eur. Data Prot. Board, Guidelines 8/2020 on the targeting of social media users 30 (2020),
https://edpb.europa.eu/sites/edpb/files/consultation/edpb_guidelines_202008_onthetarge
tingofsocialmediausers_en.pdf.
 82. Eur. Data Prot. Board, Statement 2/2019 on the Use of Personal Data in the Course of
Political Cam paigns 1 (2019), https:// edpb.europa.eu/sites/edpb/files/files/file1/edpb-2019
-03-13-statement-on-elections_en.pdf.

2020] AFFINITY PROFILING AND OBA 385

turns into sensitive data if the data controller has the intent to do so. This is a
problem as algorithms will infer sensitive details regardless of intent.83
This view leads to higher data protection standards around the usage of
special category data. Article 9 only permits a limited range of cases for using
such data. One of these cases is explicit consent, which is a higher bar than
informed consent as described in Article 7. Legitimate interests (Article 6(2)(f))
or the necessity to fulfill a contract (Article 6(1)(b)) cannot be used to collect
special category data.84 Following this, the Working Party has explained in their
OBA guidelines that data controllers will need to seek explicit consent to
collect sensitive data and that “in no case would an opt -out consent
mechanism meet the requirement of the law.”85
These processing requirements, arbitrary thresholds, and conflicting views
of the General Court and the Working Party leave affinity profiling in a  legal
grey area. If the argument holds that affinity profiling does not predict or infer
sensitive information about the data subject, but only assumes an interest with
a protected group, data controllers might not need to comply with Art icle 9.
Only standard legal bases for processing personal data (either opt -in consent
via Article 7 of the GDPR or an objection to processing via Article 21 GDPR)
could apply to affinity profiling. Even if affinity profiling is classified as a type
of sensitive data processing, the intentionality and reliability thresholds to turn
personal data into sensitive data might prevent the higher protections of
Article 9 from applying, even though the privacy harms of sensitive data and
assumed affinity can be the same.
III. E.U. NON-DISCRIMINATION LAW AND AFFINITY
PROFILING
As the previous Section showed, Article 9 of the GDPR could prove
ineffective at protecting against privacy invasive inferential analytics. Privacy is
not, however, the only concern with affinity profiling. Concerns with
discrimination might also arise if only certain groups are shown an ad (possibly
even with different product prices) or excluded from the audience, and these
groups share protected characteristics (e.g. , gender, sexual orientation, or
religious beliefs). This Section will first shed light on the scope and limits of
E.U. non-discrimination law and then demonstrate how the concept of

 83. Art. 29 Data Prot. Working Party, Opinion 2/2010, supra note 80, at 31.
 84. Of course, Article 9 offers other legitimate bases to collect special category data, such
as employment, vital interests of the data subject, or research. These, however, are less likely
to form a legitimate basis for advertisement. In other words, if advertisers want to use special
category data, it is very likely that explicit consent will be the only legitimate grounds.
 85. Art. 29 Data Prot. Working Party, Opinion 2/2010, supra note 80, at 20.

386 BERKELEY TECHNOLOGY LAW JOURNAL [Vol. 35:367

discrimination by association could be used to close some of the current
loopholes in the law to offer greater protection against affinity profiling.
E.U. non-discrimination law has its roots in both primary86 and secondary
law.87 These two regulations have different scopes, have different ways of
enforcement, and apply to different actors. 88 Primary and secondary non-
discrimination law prohibits two types of discrimination: direct and indirect
discrimination.
Direct discrimination means that an individual or group is treated less
favorably in comparison to others in a similar situation, and the treatment is
based on a protected ground (e.g. , ethnicity) without any justification rooted
in the law.89 In the context of OBA, direct discrimination is rarer than indirect
discrimination because an advertiser or platform provider is not likely to
confess that a protected ground formed the basis for a decision.
Indirect discrimination refers to a seemingly “neutral provision, criterion
or practice”90 (e.g., the decision to show certain ads to people based on their
assumed interests) that affects prote cted groups in a significantly more
negative way than others in a comparable situation, and thus results in
differential results. 91 Indirect discrimination can be legally justified when a
legitimate aim is pursued and the means to achieve it are necessary and
proportionate.92 Statistics can play a significant role in establishing legitimacy
because the claimant must provide evidence to prove that differential effects
occurred (more on that below).

 86. ELLIS & WATSON, supra note 12, at 13. For a fantastic overview of the scope, history,
and effectiveness of E.U. non -discrimination law, see generally SANDRA FREDMAN,
DISCRIMINATION LAW (2011); MARK BELL, ANTI-DISCRIMINATION LAW AND THE
EUROPEAN UNION (2002).
 87. ELLIS & WATSON, supra note 12, at 19–21.
 88. Id. at 20.  Primary law refers to the “founding” treaties  of the European Union
(including the E.U. Charter of Fundamental Rights), whereas secondary law refers to all
legislative acts that are derived from these treaties such as regulations, directives, decisions,
opinions, and recommendations. EU Law, EUROPEAN JUSTICE, https://e-justice.europa.eu
/content_eu_law-3--maximize-en.do (last updated Mar. 1, 2019).
 89. See ELLIS & WATSON, supra note 12, at 142.
 90. This is stated in all E.U. Non -Discrimination Directives. See, e.g., Council Directive
2000/43/EC, supra note 14, at art. 2(2)(b); see also Christopher McCrudden, The New Architecture
of EU Equality Law After CHEZ: Did the Court of Justice Reconceptualise Direct and Indirect
Discrimination?, EUR. EQUAL. L. REV. 1, 3 (2016).
 91. ELLIS & WATSON, supra note 12, at 143.
 92. This is stated in the E.U. non-discrimination directives.

2020] AFFINITY PROFILING AND OBA 387

To the benefit of claimants, only prima facie discrimination must be
demonstrated to bring a direct or indirect discrimination case. 93 Once prima
facie discrimination is successfully raised, the burden of proof shifts to the
alleged offender to refute it.94
To prove prima facie direct discrimination, an identifiable victim does not
need to be found because the potential harm need not actually occur.95 In other
words, it is not necessary that the discriminatory practice (e.g., only showing
job ads to men) result in negative effects (e.g., less women applying for a job).
The burden of proof shifts if “the causation between the protected ground and
the harm is only probable or likely.”96
Finally, in both cases of discrimination, intent does not need to be
proven.97 Even good -faith and well- intentioned practices can amount to
discrimination if the adverse result of the treatment disproportionately affects
members of protected groups in comparison with others in a similar
situation.98 Even with the best intentions , platform providers can commit
direct or indirect discrimination.
A. PRIMARY LAW
The widest scope of non- discrimination exists in the primary law of the
European Union. Article 21 of the E.U. Charter of Fundamental Rights (“the
Charter”) states that “[a]ny discrimination based on any ground such as sex,
race, colour, ethnic or social origin, genetic features, language, religion or
belief, political or any other opinion, membership of a national minority,
property, birth, disability, age or sexual orientation shall be prohibited.”99 This

 93. LILLA FARKAS & DECLAIN O’DEMPSEY, HOW TO PRESENT A DISCRIMINATION
CLAIM: HANDBOOK ON SEEKING REMEDIES UNDER THE EU NON-DISCRIMINATION
DIRECTIVES 52 (2011).
 94. On prima facie discrimination and shifting the burden of proof, see Sandra Fredman,
The Reason Why: Unravelling Indirect Discrimination , 45 IND. L. J. 231, 235 (2016). On shifting
burden of proof, see, for example, Council Directive 2006/ 54/EC, supra note 14, art. 19
(gender discrimination cases); Council Directive 2000/ 78/EC, supra note 14, art. 10
(employment discrimination cases); Council Directive 2000/43/EC, supra note 14, art. 8 (race
discrimination cases); see also Council Directive 97/80/EC, 1997 O.J. (L 14) 6 (EC).
 95. For an example involving racist job ads, see Case C-54/07, Centrum voor gelijkheid
van kansen en voor racismebestrijding v. Firma Feryn NV, 2008 E.C.R. I-397, ¶ 25.
 96. LILLA FARKAS & ORLAGH O’FARRELL, EUROPEAN COMMISSION, REVERSING THE
BURDEN OF PROOF: PRACTICAL DILEMMAS AT THE EUROPEAN AND NATIONAL LEVEL 47
(2015).
 97. ELLIS & WATSON, supra note 12, at 167.
 98. EUR. UNION AGENCY FOR FUNDAMENTAL RIGHTS & COUNCIL OF EUR.,
HANDBOOK ON EUROPEAN NON-DISCRIMINATION LAW 239–42 (2018).
 99. Charter of Fundamental Rights of the European Union, art. 21, 2007 O.J. (C 303) 1,
7.

388 BERKELEY TECHNOLOGY LAW JOURNAL [Vol. 35:367

is a non- exclusive list that is sector- neutral. However, these provisions only
apply to E.U. institutions and institutions of the Member States if they
implement European Law.100 Thus, only public bodies of the European Union
and public bodies of the Member States in matters of E.U. law are bound by
these provisions.101
B. SECONDARY LAW
In contrast, secondary law applies to both private and public sectors.
Compared with primary law, the protections defined in secondary law are
limited both in terms of the types of people protected (exclusive list protecting
from discrimination based on race and ethnici ty, gender, religion and belief,
age, disability , and sexual orientation) and the sectors covered (only
employment, the welfare system, and access to goods and services, including
housing are covered).102 However, the directives must be in accordance with
the Charter.
1. Race and Ethnicity
The most far- reaching protection in secondary law can be found in the
Racial Equality Directive.103 Article 3 of the Racial Equality Directive prohibits
discrimination based on race or ethnicity in the context of employment, access
to the welfare system, social protection, education, as well as goods and
services. With regards to OBA, these protections extend to unjustified
discrimination based on ethnicity —be it directly or indirectly —in
advertisements offering jobs or (ads for) goods and services (e.g., products,

 100. However, the ECJ has opened  the possibility of letting the principle of non -
discrimination in the Charter apply to private entities as well. See generally Case C-144/04,
Werner Mangold v. Rüdiger Helm, 2005 E.C.R. I -9981; Case C-414/16, Vera Egenberger v.
Evangelisches Werk für Diakonie und Entwicklung eV, ECLI:EU:C:2018:257 (Apr. 17, 2018);
Case C-555/07, Seda Kücükdeveci v Swedex GmbH & Co. KG., 2010 E.C.R. I-365.
 101. See Charter of Fundamental Rights of the European Union, art. 51, 2000 O.J. (C 364)
1, 21.
 102. See ELLIS & WATSON, supra note 12, at 22 –42; FREDMAN, DISCRIMINATION LAW ,
supra note 86, at 109–53.
 103. Council Directive 2000/43/EC, supra note 14.

2020] AFFINITY PROFILING AND OBA 389

loans, insurance, or housing).104 Such discriminatory advertisements are illegal,
unless legally justified.105
2. Gender
Equality between men and women is guaranteed in two directives: the
Gender Equality Directive (recast)106 and the Gender Access Directive.107 Both
frameworks cover less ground than the Racial Equality Directive. 108 The
Gender Equality Directive guarantees equality in employment. However, equal
treatment is only guaranteed for social security and not in the broader welfare
system, including social protection and access to healthcare and education. 109
In most cases, showing or not showing job ads based on gender is illegal
(because the ads are within the realm of employment, a protected sector),
unless legally justified.
The Gender Access Directive, as opposed to the Racial Equality Directive,
excludes media content, advertisements, and education from its scope .110

 104. Similarly, E.U. consumer protection law requires that ethnicity or country of
residence within the European Union cannot be used as a basis for price discrimination. See
European Union, Pricing, payments and price discrimination in the EU, YOUR EUROPE - CITIZENS,
https://europa.eu/youreurope/citizens/consumers/shopping/pricing-payments/index
_en.htm (last visited Apr 20, 2020).  Further, the proposed Digital Services Act promises
stricter regulation on digital commerce. See Madhumita Murgia & Mehreen Khan, EU draws
up sweeping rules to curb illegal online content , FINANCIAL TIMES (July 24, 2019), https://
www.ft.com/content/e9aa1ed4-ad35-11e9-8030-530adfa879c2.
 105. See infra Section III.C.
 106. Council Directive 2006/ 54/EC, supra note 14; s ee also Case C -13/94, P v S and
Cornwall County Council 1996 E.C.R. I-02143 (protecting transsexual people against gender
and sex discrimination if they seek to undergo gender reassignment surgery).
 107. Council Directive 2004/ 113/EC, 2004 O.J. (L 373) 37 (EU) (Gender Access
Directive).
 108. On the hierarchy of protected groups and the political reasons, see Dagmar Schiek,
Broadening the Scope and the Norms of EU Gender Equality Law: Towards a Multidimensional Conception
of Equality Law, 12 MAASTRICHT J. EUR. & COMP. L. 427, 438 (2005).
 109. EUR. UNION AGENCY FOR FUNDAMENTAL RIGHTS & COUNCIL OF EUR., supra note
98, at 22.
 110. Council Directive 2004/113/EC, supra note. 107, at 40 (art. 3(3)) . Other legitimate
aims that limit the scope of the Directive are:
[d]ifferences in treatment may be accepted only if they are justified by a
legitimate aim. A legitimate aim may, for example, be the protection of
victims of sex-related violence (in cases such as the establishment of single
sex shelters), reasons of privacy and decency (in cases such as the provision
of accommodation by a person in a part of that person's home), the
promotion of gender equality or of the interests of men or women (for
example single-sex voluntary bodies), the freedom of association (in cases
of membership of single-sex private clubs), and the organisation of sporting
activities (for example single-sex sports events).

390 BERKELEY TECHNOLOGY LAW JOURNAL [Vol. 35:367

Originally it was planned to cover a vast range of sensitive areas such as social
assistance, education, media, advertising, and taxation, but these sectors were
ultimately not included.111 Samantha Besson argues that, in general, the Court
of Justice of the European Union’s (CJEU ) case law applies a higher level of
scrutiny on nationality and age than gender.112
3. Religion or Belief, Disability, Age, or Sexual Orientation
As demonstrated in Sections III.B.1–2, c ompared to other protected
classes, E.U. law offers the least protection against discrimination based on
religion or beliefs, disability, age, and sexual orientation. These attributes are
only protected in the context of employment ,113 but not in relation to the
welfare system or with respect to the purchase of goods and services. As it
currently stands, E.U. law allows advertisements offering goods and services
(including housing, financial services, and insurance) to discriminate based on
these traits.
Since 2008, the so-called Horizon Directive has been under discussion in
order to partially remedy this gap in non- discrimination law in the European
Union.114 The Horizon Directive aims to implement “the principle of equal
treatment between persons irrespective of religion or belief, disability, age or
sexual orientation” beyond the realm of employment. 115 Despite the debate
lasting over eleven years, the Horizon Directive remains in draft form, and the
current draft does not address the gaps in non-discrimination law based on sex
or gender.116
4. Sectoral Divergence in Protected Groups
Depending on the context in which ads are served, different groups will
be protected. Ads in the context of employment must adhere to the safeguards
against discrimination in relation to employment. Other types of ad s will

Id. at 38.
 111. EUR. PARLIAMENTARY RESEARCH SERV., GENDER EQUAL ACCESS TO GOODS AND
SERVICES DIRECTIVE 2004/113/EC: EUROPEAN IMPLEMENTATION ASSESSMENT I-7 (2017);
Schiek, supra note 108, at 429–30 (criticizing the limited scope of the Directive due to lobbying
efforts of the insurance industry).
 112. Samantha Besson, Gender Discrimination Under EU and ECHR Law: Never Shall the
Twain Meet?, 8 HUM. RIGHTS L. REV. 647, 665–67 (2008).
 113. Council Directive 2000/78/EC, supra note 14.
 114. See generally Proposal for a Council Directive on Implementing the Principle of Equal Treatment
between Persons Irrespective of Religion or Belief, Disability, Age or Sexual Orientation, COM (2008) 426
final (July 2, 2008) (Horizon Directive).
 115. Id. at 2.
 116. See id. For an overview of the regulatory history of anti -discrimination law and the
Horizon Directive, see generally Mark Bell, Advancing EU Anti-Discrimination Law: The European
Commission’s 2008 Proposal for a New Directive, 3 EQUAL RIGHTS REV. 7 (2009).

2020] AFFINITY PROFILING AND OBA 391

generally fall within the realm of protection of equal access to goods and
services.
Employment advertisements must adhere to the highest legal standards
because E.U. law offers protection to the broadest set of groups , specifically
those defined by ethnicity, gender, religion or belief, disability, age , or sexual
orientation. Given that companies 117 have been accused of favoring men or
even excluding women from seeing job ads despite such practices likely being
illegal under the Gender Equality Directive, this topic is of critical concern.118
When offering goods and services, the Directives do not allow gender and
ethnicity to be used to restrict access. In contrast, religion or belief, disability,
age, or sexual orientation can be used in this regard. However, the Gender
Access Directive allows gender (but not ethnicity) to be used as a factor to
discriminate in relation to media, advertising, and education content. It is
indeed problematic that media and advertising are excluded from the scope
because they can be the means used to inform potential customers about the
availability of goods and services.119
As mentioned above, it is safe to assume that employment ads fall within
employment non-discrimination protections and are thus a lex specialis to the
Gender Access Directive.120 Unlike other types of ads concerned with goods
and services, gender- based discrimination is therefore not allowed in
employment advertising, unless it constitutes a “genuine occupational
requirement.”121 At the same time, it is unclear how this would relate to ads
aimed to inform audiences about housing or credit, since this is also covered
in the Gender Access Directive, which allows gender discrimination in relation
to advertising. Evelyn Ellis and Philippa Watson believe that “[s]uppliers of
goods and services can therefore target their advertising to either men or

 117. Celis, Mehrotra & Vishnoi, supra note 45, at 3; Merrill & Tobin, supra note 47.
 118. For a general discussion on how and to what extent intermediaries for online ads are
liable, see Philipp Hacker, Teaching Fairness to Artificial Intelligence: Existing and Novel Strategies
Against Algorithmic Discrimination Under EU Law , 55 COMMON MKT. L. REV. 1143, 1162–64
(2018) (criticising the lack of transparency in financial and insurance decisions).
 119. Similar concerns have been raised by a Greek expert who explains that “the ‘vague’
exclusion of ‘the content of media an d advertising’ ‘cannot mean that offers of and
information on supply of goods and services in the media are excluded, the more so as the
directive concerns goods and services available to the public.’  ” SUSANNE BURRI & AILEEN
MCCOLGAN, SEX DISCRIMINATION I N THE ACCESS TO AND SUPPLY OF GOODS AND
SERVICES AND THE TRANSPOSITION OF DIRECTIVE 2004/113/EC 17 (2009).
 120. Lex specialis derogat legi generali means “special law repeals general laws.” See AARON X.
FELLMETH & MAURICE HORWITZ, GUIDE TO LATIN IN INTERNATIONAL LAW 177 (OXFORD
UNIV. PRESS 2009).
 121. “Genuine occupation requirement” is a common concept across the European
Union that features non-discrimination Directives in the realm of employment.

392 BERKELEY TECHNOLOGY LAW JOURNAL [Vol. 35:367

women but must supply the goods or services advertised to both sexes on the
same terms.” 122 However, Eugenia Caracciolo di Torella is concerned that
there is a “challenge of distinguishing ‘goods’ (included in the Directive) from
‘advertisement of goods’ (not included in the Directive).”123 In addition, these
gaps mean that the Gender Access Directive cannot entirely prevent
stereotypical, offensive, and sexist advertising.124
Lastly, E.U. law does not offer protection against discrimination based on
religion or belief, age, sexual orientation, or disability when offering goods and
services. Once again, Member State law can establish (and sometimes has)
higher levels of protection.125 For example, some Member States grant higher
protection for gender inequality in areas such as media, advertisement , and
education.126 The downside of this situation is that a harmonized standard for
non-discrimination does not exist at the European level.127
C. CURRENT CHALLENGES AND FUTURE OPPORTUNITIES FOR E.U.
NON-DISCRIMINATION LAW AND AFFINITY PROFILING
Thus far, this Article has analyzed privacy and discrimination problems
associated with affinity profiling. By claiming not to collect or infer sensitive
personal data, but rather to only assume an affinity or interests, companies
might not need to adhere to the higher protection afforded to sensitive data
processing in Article 9 of the GDPR. The lack of comprehensive non-
discrimination law in Europe furthe r erodes the protection available to data
subjects against affinity profiling. The law applies to a limited number of
protected grounds and contexts.128
The applicability of direct discrimination to affinity profiling leaves much
to be desired. If courts and regulators do not view affinity profiling as using

 122. ELLIS & WATSON, supra note 12, at 368.
 123. Eugenia Caracciolo di Torella, The Principle of Gender Equality, the Goods and Services
Directive and Insurance: A Conceptual Analysis, 13 MAASTRICHT J. EUR. COMP L. 339, 343 (2006).
 124. See BURRI & MCCOLGAN, supra note 119, at 6. For a strong criticism of these
exemptions, see Caracciolo di Torella, supra note 123, at 343 (“Although the unequal treatment
in these fields has been justified in light of its clash with the fundamental right to freedom of
expression, it is difficult to envisage how the exploitation of women in the media can be
regarded as a fundamental right.”).
 125. For an overview of this protection, as well as in relation to offensive, sexist
advertisements and Member State law, see generally BURRI & MCCOLGAN, supra note 119.
 126. EUR. PARLIAMENTARY RESEARCH SERV., supra note 111, at I-38. The handbook also
provides an overview of how the Member States have implemented the framework.
 127. For an overview of the fragmented standards across the E.U. Member States, see
generally ISABELLE CHOPIN, CARMINE CONTE & EDITH CHAMBRIER, EUROPEAN
COMMISSION, A COMPARATIVE ANALYSIS OF NON-DISCRIMINATION LAW IN EUROPE
(2018).
 128. See supra Sections III.B.1–III.B.4.

2020] AFFINITY PROFILING AND OBA 393

protected attributes or accepted proxies, people possessing these attributes
may not be able to raise direct discrimination claims. Even if affinity profiling
is interpreted as directly using protected traits, the  related argument that
inferring an affinity for a protected group (e.g., “affinity for African American
culture”) is completely different than inferring that the user has certain
protected attributes  (e.g., “African American”)  still creates problems for
potential claimants. If this argument is accepted, individuals subject to affinity
profiling would not be able to raise direct discrimination c laims because a
protected attribute has not been directly inferred; rather, only an affinity with
that attribute had been inferred. Even if these legal hurdles are overcome, the
claimant might not want to openly acknowledge that they possess a particular
protected trait (e.g., sexual orientation or religion) when bringing a
discrimination claim. And finally, people who are subjected to discriminatory
ads based on an inaccurate classification or grouping may not receive any
protection, as they do not possess  the trait protected by non-discrimination
law (e.g., men that are shown discriminatory ads intended for women).
Indirect discrimination provides a promising alternative route to raise
claims against advertisers. Targeting source or “look alike” audiences , while
not based on protected grounds, can still lead to differential results for
protected groups. For example, excluding people from seeing ads based on
their assumed interest in part-time work could lead to differential results, if it
can be shown that a large portion of part-time workers are women.
In these cases, members that share these attributes could bring a claim
provided that the other conditions have been established, such as the existence
of a comparison group, adverse and less favorable treatment, causality, and a
lack of justification. 129 Apart from the challenge of gathering the evidence
necessary to meet the conditions for a claim, two additional problems remain.
First, claimants might not want to openly and publicly discuss t heir sensitive
attributes. Second, as with direct discrimination, people that were served the
discriminatory ads but do not share the attributes of the target audience ( e.g.,
employment ads aimed at gay users that are unintentionally shown to a straight
user due to algorithmic misclassification of sexual orientation) may not be
eligible to make a claim because they are not a member of the protected group.
The next Section discusses how the concept of discrimination by association
can be used to address this gap in legal protections against affinity profiling.

 129. See infra Sections IV.B.1–IV.B.2, IV.C.

394 BERKELEY TECHNOLOGY LAW JOURNAL [Vol. 35:367

IV. DISCRIMINATION BY ASSOCIATION AND AFFINITY
PROFILING
The legal concept of discrimination by association may offer a way
forward. Discrimination by association is a type of discrimination which has
been recognized by the ECJ, the European Court of Human Rights (ECHR),
national courts ,130 and Member State laws. 131 Applying this concept to
advertising would solve many of the weaknesses of discrimination law in the
context of affinity profiling outlined above.  Two landmark judgments of the
ECJ have important implications for OBA by allowing claimants to appeal to
direct or indirect discrimination by association.
A. DIRECT DISCRIMINATION BY ASSOCIATION: THE COLEMAN CASE
Discrimination by association was first proposed by the ECJ in the 2008
case Coleman v. Law.132 According to the court , protections against direct
discrimination apply not only to people who possess the protected
characteristics in question, but also to people who experience discrimination
because of their association with the protected group.133
In Coleman, claimant, Ms. Coleman, sued her employer for not agreeing to
give her more flexible working hours to take care of her disabled child and for
eventually t erminating her. 134 She compared herself with a group of other
parents in the firm who had been granted such privileges for their non-disabled
children.135 She claimed to be discriminated against in the workplace because
of her child’s disability. 136 The court agreed, ruling that her treatment
constituted direct discrimination on the basis of her child’s disability. This type
of discrimination constitutes direct discrimination by association.137 According

 130. See, e.g., English v. Thomas Sanderson Ltd [2008] EWCA (Civ) 1421 (Eng.) (holding
that homophobic banters against a heterosexual man was discrimination protected by
antidiscrimination provisions); Szczegóły orzeczenia v. Ca 3611/ 14 - Portal Orzeczeń Sądu
Okręgowego w Warszawie (addressing discrimination in relation to sexual orientation in
Poland); EUR. UNION AGENCY FOR FUNDAMENTAL RIGHTS & COUNCIL OF EUR., supra note
98, at 51–52.
 131. For an overview and an example of the Member States laws on discrimination by
association or by assumption/perception, refer to Austria’s discrimination based on assumed
friendship with someone who possesses a protected attribute is illegal. See generally CHOPIN,
CONTE, & CHAMBRIER, supra note 127, at 44–46.
 132. Coleman, supra note 15.
 133. See id. at ¶ 63.
 134. Id. at ¶ 26.
 135. Id.
 136. Id. (citing to Articles 2(1)–(3) of the Directive 2000/78/EC).
 137. See id. at ¶ 56. Note that the Court never uses this term. See Bell, supra note 116, at 8.
For a view that the judgment created the concept of direct (but not indirect) discrimination by
association, see Andrea Eriksson, European Court of Justice: Broadening the S cope of European

2020] AFFINITY PROFILING AND OBA 395

to this concept, a claimant does not need to possess  a protected attribute
herself, but rather merely suffer the consequences of the discriminatory
behavior which is based on her relationship with her child, or the person(s)
possessing the protected attribute. 138 The court arguably did not limit
discrimination by association to disability because the rationale of the
Employment Directive is to combat all types of discrimination in the
workplace.139
Coleman marks a significant turning point for non- discrimination law. It
shows that, “[n]ot only does [non-discrimination law] protect the person with
a protected characteristic ( race, sex, disability), it also shields somebody who
does not but is associated with such a person.” 140 Claimants therefore do not
need to be part of a protected group but need only experience the adverse
effects directed at the group.141
What does discrimination by association mean for OBA? This will depend
on whether one deems the interest group in which users are placed to be close
enough to the classes protected in E.U. non-discrimination Directives. For
example, is “Hispanic affinity”142 close enough to “race” or “ethnicity” within
the meaning of the Racial Equality Directive? Is the interest category “Vogue
readers” close enough to “sex” in the sense of the Gender Equality Directive?

Nondiscrimination Law, 7 INT. J. CONST. L. 731, 751– 52 (2009); Gabriel von Toggenburg,
Discrimination by Association: A Notion Covered by EU Equality Law?, 3 EUR. L. REP. 82, 86 (2008).
 138. Coleman, supra note 15, at ¶ 61(1).
 139. Id. at ¶ 50 (“Although, in a situation such as that in the present case, the person who
is subject to dire ct discrimination on grounds of disability is not herself disabled, the fact
remains that it is the disability which, according to Ms Coleman, is the ground for the less
favourable treatment which she claims to have suffered. As is apparent from paragraph 38 of
this judgment, Directive 2000/ 78, which seeks to combat all forms of discrimination on
grounds of disability in the field of employment and occupation, applies not to a particular
category of person but by reference to the grounds mentioned in Artic le 1.”). For a similar
analysis of Coleman, see Marcus Pilgerstorfer & Simon Forshaw, Transferred Discrimination in
European Law: Case C-303/06, Coleman v Attridge Law; [2008] ICR 1128, [2008] IRLR 722 (ECJ),
37 INDUST. L.J. 384, 392–93 (2008); Bell, supra note 116, at 8. For an analysis in favor of the
Coleman approach, see Eriksson, supra note 137, at 751. For a view that only direct
discrimination by association exists (and not indirect), and only in areas such as disability, see
Catalina-Adriana Ivanus, Discrimination by Association in European Law, 2 PERSP. BUS. L.J. 116,
121 (2013).
 140. Catalina-Adriana Ivanus, supra note 139, at 117.
 141. It has been criticized that the Court did not define the required relationship/
closeness of the victim and the protected group to fall under this concept. See Eriksson, supra
note 137, at 751.
 142. Dexter Thomas, Facebook Tracks Your “Ethnic Affinity” — Unless You’re White, VICE
NEWS (2016), https:// www.vice.com/en_us/article/paqeez/facebook-tracks-your-ethnic
-affinity-unless-youre-white.

396 BERKELEY TECHNOLOGY LAW JOURNAL [Vol. 35:367

In relation to ethnicity, the ECJ ruled in a separate case that the “concept
of ethnicity . . . has its origin in the idea of societal groups marked in particular
by common nationality, religious faith, language, cultural and traditional
origins and backgrounds . . . .”143 Elsewhere, the ECJ stated that this will not
be the case if characteristics that do not link to any of these traits (e.g., country
of birth) are used.144 The court explained that it “cannot be presumed that each
sovereign State has one, and only one, ethnic origin,” 145 meaning the country
of birth is not a proxy for ethnicity.
The scope of the Racial Equality Directive has caused heated debates and
its interpretation and transportation also greatly differs across the Member
States.146 This is one of the reasons that Ellis and Watson have argued that
courts and regulators should classify less favorable treatment based on color
as direct discrimination based on ethnicity.147 Meanwhile, it is unclear whether
or not language could be seen as an attribute that leads to indirect
discrimination.148
If one wishes to argue that these interest groups do not map onto
protected groups in the law, direct discrimination cases will not be possible.
The avenue through indirect discrimination would, however, still be available
for plaintiffs targeted by affinity advertising.149
If, conversely, one wishes to argue that affinity profiling does correspond
to protected traits, direct discrimination claims are —in general—possible.
However, if it is argued that advertisers are not directly using or inferring
protected traits of an individual, but only assuming a person’s interests in the
protected group, direct discrimination claims would not likely be possible. In
other wor ds, the argument made is this: advertisements are shown to you
based not on your ethnicity, but rather on your interest in a given ethnicity.
Still, even if this argument is accepted, discrimination by association can
offer a solution. Individuals who experience an adverse action based on their
association with a protected group could receive protection based on assumed

 143. CHEZ, supra note 16, at ¶ 46.
 144. Case C-668/15, Jyske Finans A/ S v. Ligebehandlingsnævnet ex rel Huskic, ECLI:
EU:C:2017:278, ¶ 33 (Apr. 6, 2017).
 145. Id. at ¶ 21.
 146. See CHOPIN, CONTE & CHAMBRIER, supra note 127, at 15–16.
 147. ELLIS & WATSON, supra note 12, at 167.
 148. See Case C-391/09, Runevič-Vardyn v. Vilniaus miesto savivaldybės administracija
2011 E.C.R. I-03787, ¶ 94 (holding that refusing to use the claimant's national language falls
outside the Racial Equality Directive, as it does not constitute a service, without addressing
the issue of indirect discrimination).
 149. See supra Section III.B.

2020] AFFINITY PROFILING AND OBA 397

interests (or assumed association) with a protected group, without the need to
be a member of it.150
An important implication of discrimination by association is that it allows
associated individuals to raise a discrimination claim against actions based on
their assumed interests, rather than just actions based on their protected traits.
Moreover, claimants can do so regardless of whether they are actually a
member of the discriminated group. Arguably, individuals who are actually
members of the group could also take this path, meaning they would not need
to prove or publicly declare their membership in the group. 151 This approach
would be extremely valuable for claimants that might prefer not to publicly
disclose their sensitive traits (e.g., religion, disability, or sexual orientation).
Discrimination by association could increase algorithmic accountability in
advertising cases in several way s. First, if affinity profiling is seen as directly
using protected traits, it could constitute direct discrimination (or by
association). This means legal justification is only possible if the
aforementioned non- discrimination directives explicitly name a possible
exception.
Second, the concept of discrimination by association could widen the circle
of potential claimants which could help support legal battles against unlawful
discrimination. If direct discrimination occurred against, for example, a
religious group, then Christians who have been misclassified as Buddhists
could also make a claim as victims of direct discrimination (by association) if
they experienced adverse treatment. 152 It would also strengthen the
relationship of allies of civil rights movements (e.g., LGBTQ+, religious, and
women’s). Fearing potential negative consequences based on associating with
the groups could have an undesirable chilling effect.
Third, discrimination by association has practical advantages for claimants
who are in fact part of a protected group and feel unlawfully treated, but do
not want to “out” themselves in order to bring a claim. Since membership is
not a precondition to warrant protection, affected parties could bring a claim

 150. See Coleman, supra note 15.
 151. The Polish Court used a similar argument in relation to a gay worker who was
dismissed because he attended the Pride parade. See Szczegóły orzeczenia v. Ca 3611/ 14 -
Portal Orzeczeń Sądu Okręgowego w Warszawie.
 152. If one wishes to argue that affinity profiling is assuming that someone is, for example,
Christian (rather than thinking they are interested in this reli gion) when in fact they are not,
the concept of discrimination by perception could apply. The legal consequences are the same
for discrimination by association and perception. See, e.g., Erica Howard, EU Equality Law: three
recent developments, 17 EUR. L.J. 785, 800 (2011). (arguing that “discrimination by assumption”
can be read into the Directives based on the Coleman judgment).

398 BERKELEY TECHNOLOGY LAW JOURNAL [Vol. 35:367

under discrimination by association instead of appealing to normal direct
discrimination, which might require publicly disclosing sensitive attributes.
Finally, as is generally true of direct discrimination cases, an abstract victim
is sufficient to shift the burden of proof from the claimant to the accused ; an
actual victim does not need to be identified. This means that if a certain
practice is discriminatory, it does not matter whether the practice actually had
negative effects. 153 For example, prima facie  direct discrimination has been
seen in advertisements against recruiting immigrants 154 and in public
statements against recruiting gay football players. 155 In these cases, an
identifiable victim was not required to prove prima facie direct discrimination.
It was not necessary to demonstrate that fewer immigrants or fewer gay people
applied for the job for the claims of discrimination to be successful.
B. INDIRECT DISCRIMINATION BY ASSOCIATION: THE CHEZ CASE
Coleman established direct discrimination by association as a standard
concept in non-discrimination law.156 As mentioned before, it could be argued
that major companies do not use protected attributes to make decisions or
serve advertisements, but rather use affinity or assumed interests which are not
equivalent to protected traits in non-discrimination law.
However, it is problematic to see affinity profiling as completely different
from the usage of protected traits. This is because affinity or interests ( e.g.,
friends, likes,157 and groups) can potentially reveal or correlate with protected
attributes of a user. These interest groups could be proxies for a user’s sensitive
characteristics and personal life without the user being aware. For example,
research suggests that friends are a strong indication of identity and even sexual
orientation.158

 153. See Case C-54/07, Centrum voor gelijkheid van kansen en voor racismebestrijding v.
Firma Feryn NV, 2008 E.C.R. I-397, ¶ 40 (“[S]anctions . . . must be effective, proportionate
and dissuasive, even where there is no identifiable victim.”); see also Case C-81/12, Asociaţia
Accept v. Consiliul Na ţional pentru Combaterea Discrimin ării, ECLI:EU:C:2013:275, ¶ 62
(Apr. 25, 2013) (holding that “sanctions . . . must also be effective, proportionate and
dissuasive, regardless of whether there is an identifiable victim”).
 154. Case C-54/07, 2008 E.C.R. I-397, supra note 153, at ¶¶ 2, 18(4)(d), 41(3).
 155. C-81/12, Asociaţia Accept v. Consiliul Na ţional pentru Combaterea Discriminării,
Case 2013 E.C.R. I-275, ¶¶ 35(1), 62.
 156. See supra Section IV.A.
 157. Kosinski, Stillwell & Graepel, supra note 8, at 5802.
 158. On how friends of friends can be used to infer personality traits, see generally Kristen
M. Altenburger & Johan Ugander, Monophily in Social Networks Introduces Similarity Among Friends-
of-Friends, 2 NATURE HUM. BEHAV. 284 (2018); see also Carter Jernigan & Behram F. T. Mistree,
Gaydar: Facebook Friendships Expose Sexual Orientation , 14 FIRST MONDAY (2009), https://
doi.org/10.5210/fm.v14i10.2611.

2020] AFFINITY PROFILING AND OBA 399

Even if one sees affinity groups as distinct from groups with protected
traits, indirect discrimination as well as indirect discrimination by association
might still occur. Furthermore, it may be possible to treat discriminatory OBA
as direct discrimination (by association) where almost no legal justification
exists. This could potentially pose legal challenges for advertisers in the future.
Indirect discrimination by association was introduced in a case heard by
the ECJ in 2015, CHEZ Razpredelenie Bulgaria AD v. Komisia za zashtita ot
diskriminatsi.159 With this landmark judgment, the court established the notion
that a claimant can sue for indirect discrimination by association despite
neither being part of the protected group nor having a close relationship with
it. The case centered around Ms. Nikolova, a shop owner in Bulgaria. Her
establishment was situated in a primarily Roma populated area. Ms. Nikolova
herself was not of Roma descent.160 She felt discriminated against because her
electricity meters were situated at an unreachable height of six meters above
the ground. This made it impossible for her to monitor her electricity
consumption.161 The reason for installing the meters at this height was to
prevent tampering.162
Indirect discrimination occurs if a protected group is treated significantly
less favorably as a result of an “ ‘apparently neutral’ provision, criterion or
practice”163 (e.g., meter installation) which do not explicitly use  protected
attributes. Ms. Nikolova claimed that, in areas where the majority of the
population was not of Roma descent, the electricity meters were situated
significantly lower to the ground.164 The court found that there was differential
treatment in offering goods and services based on race or ethnicity,165 and that
although Ms. Nikolova was not of Roma descent, she had been discriminated
against.
Michael Malone has convincingly argued that this case has born the notion
of indirect discrimination by association.166 Similar to Coleman, Malone argues

 159. CHEZ, supra note 16.
 160. Id. at ¶ 49.
 161. Id. at ¶¶ 22–29.
 162. Id. at ¶ 113; Michael Malone, The Concept of Indirect Discrimination by Association: Too
Late for the UK?, 46 INDUS. L.J. 144, 145 (2017) (discussing the obvious stigma and implication
that tampering would otherwise occur).
 163.  CHEZ, supra note 16, at ¶ 109 (internal citations omitted).
 164. Id. at ¶¶ 22–23.
 165. For a better understanding of the law applied by the court in Coleman, see Council
Directive 2000/43/EC, supra note 14, at art. 3(1)(h).
 166. See Malone, supra note 162, at 150–51; see also Erica Howard, EU Anti-Discrimination
Law: Has the CJEU Stopped Moving Forward?, 18 INT’L. J. DISCRIMINATION & L. 60, 65 (2018)
(arguing that Chez and Coleman also prohibit “discrimination by perception,” which means

400 BERKELEY TECHNOLOGY LAW JOURNAL [Vol. 35:367

that the claimant  in CHEZ does not need to be part of the stigmatized
collective to suffer discrimination. Moreover, the claimant does not even need
to have a close relationship with the community. Rather, Malone explains that
any “third-party damage” suffered from indirect racial discrimination entitles
the victim(s) to protection. 167 Initially, as in Coleman, the Advocate General
(AG) in CHEZ referred to some sort of relationship with the stigmatized
community (i.e., “wholesale and collective character”), 168 but this restriction
did not appear in the final judgment. 169 It can therefore be assumed that no
personal relationship is needed to warrant protection.170
The significance of the judgment  in Chez goes further than establishing
indirect discrimination by association. The court left open the possibility that
the practice in question (meter installation) could be direct discrimination by
association. A decision on this classification was ultimately left to the national
court.171 Leaving this issue open is significant because the boundaries between
direct and indirect discrimination can easily blur, and offenders are not likely
to admit illegal reasons are behind their actions.172
What does this mean for affinity profiling? Advertisements based on the
correlation of interests could lead to undesired differential results for protected
groups. Platform providers may not actually be interested in inferring sensitive
attributes, but rather merely want to identify correlations in the interests of
their users. To use a stereotypical example, if a user visits jazz or blues websites,
they might also see ads for Caribbean food. The decision to show food
advertisements is not based on “race” or “ethnicity,” but rather on the
statistical correlation that suggests that people who have an interest in a certain
type of music also enjoy a certain type of food. The decision to show jazz
enthusiasts advertisements for Caribbean food can be see n as an “apparently

“discrimination because someone perceives a person to be, for example, of a particular ethnic
origin or sexual orientation, when they are not”).
 167. See Malone, supra note 162, at 151.
 168. Case C-83/14, Kokott, CHEZ Razpredelenie Bulgaria AD v. Komisia za zashtita ot
diskriminatsia, Advisory Opinion, ECLI:EU:C:2015:170, ¶¶ 58, 60 (Mar. 12, 2015).
 169. See Malone, supra note 162, at 151.
 170. See Rossen Grozev, A Landmark Judgment of the Court of Justice of the EU–New Conceptual
Contributions to the Legal Combat Against Ethnic Discrimination, 15 EQUAL RIGHTS REV. 168, 173
(2015).
 171. CHEZ, supra note 16, at ¶ 129(4); McCrudden, supra note 90.
 172. See, e.g., FARKAS & O’DEMPSEY, supra note 93, at 38 (“[T]he CJEU has identified as
direct discrimination cases in which a formally neutral rule (internal or legal) in fact affects one
group only. In Nikoloudi, the CJEU examined a rule that reserved established staff positions
to persons with full time jobs.”); see also id.  at 41 (addressing discrimination based on
pregnancy, which is now considered a form of direct discrimination).

2020] AFFINITY PROFILING AND OBA 401

neutral provision, criterion or practice .”173 Nonetheless, unlawful differential
results could still occur if statistical evidence shows that an interest in
Caribbean food and jazz music is more likely to occur among a particular
ethnic group and this group is treated less favorably than others without any
justification (more on that below).174
Such correlations are not unrealistic. As mentioned above, research
suggests that personal interests and friends are a strong indication of one’s
personality.175 These sources paint a very privacy-invasive picture and reveal or
correlate with sensitive traits such as sexual orientation.176
The ECJ’s judgments in Coleman and CHEZ have important
consequences for OBA. If affinity profiling is not seen as inferring or using
protected traits because the interest groups are seen as sufficiently distinct
from protected categories such as “race” and “ethnicity” as described in the
directives, no claims against direct discrimination could be brought. However,
claims under indirect discrimination are possible if it can be shown that actions
based on assumed affinity or interest groups lead to adverse and differential
results for a protected group (and anyone associated with this group) in
comparison with others in a similar situation.
Based on this reasoning, both claims under indirect discrimination as well
as indirect discrimination by association are then possible. This could have
interesting implications for OBA. First, as revealed in Coleman, it is not
necessary for the claimant to be part of the disadvantaged group (e.g., men
being shown advertisements for lower paying jobs because they have been
classified as women). Likewise, as revealed in CHEZ, the claimant also does
not need to have a close relationship with the protected group (e.g. , she does
not ne ed to be an active member of the women’s movement). However,

 173. This term is used in all E.U. non-discrimination directives. See, e.g., Council Directive
2000/43/EC, supra note 14, at art. 2(2)(b).
 174. It is important to note that is still unclear whether intermediaries such as Facebook
and Google will be liable for discriminatory advertisement and to what extent. However, some
scholars have argued that liability could extend to internet companies. See Philipp Hacker,
Teaching fairness to artificial intelligence: Existing and novel strategies against algorithmic discrimination under
EU law, 55 COMMON MARK. L. REV. 1143, 1164–65 (2018) (arguing that intermediaries can
be liable drawing similarities between the responsibilities of Uber as an internet service
provider); Jennifer Cobbe & Jatinder Singh, Regulating Recommending: Motivations, Considerations,
and Principles, 10 EUR. J.L. TECH. 1 (2019) (arguing that liability can be assumed when illegal
content is recommended); David Jacobus Dalenberg, Preventing discrimination in the automated
targeting of job advertisements, 34 COMPUT. L. SECUR. REV. 615, 626 (2018) (suggesting that ad
tech companies will be liable for discriminatory advertisement).
 175. See Kosinski, Stillwell & Graepel, supra note 8, at 5802; Altenburger & Ugander, supra
note 158, at 284.
 176. See Jernigan & Mistree, supra note 158.

402 BERKELEY TECHNOLOGY LAW JOURNAL [Vol. 35:367

widening the circle of potential claimants could also have the positive side
effect of strengthening the claimants’ relationship with stigmatized groups.
Moreover, not granting protection to third parties could have an undesirable
chilling effect due to fear over potential negative consequences from
associating with these groups (e.g., people moving away from Roma populated
areas).
Second, as argued above, the logical conclusion of not needing t o be a
member of the protected group to bring a successful claim is that a person
who is in fact a member of the protected group does not need to prove it or
“out” themselves.
Third, because the ECJ left open in CHEZ whether direct or indirect
discrimination by association occurred,177 it may also be possible to classify the
practice of placing ads based on affinity as direct discrimination (or by
association) with almost no justification as discussed in Section IV.C. This
could pose legal challenges for many advertising practices.
Of course, as discussed above, to bring a successful discrimination claim,
a claimant must still demonstrate that they have suffered a particular
disadvantage, identify a comparator that is treated more favorably , and
demonstrate a disproportionately negative effect on a protected group. An
indication of less favorable treatment in advertising could be seen in
differential pricing or exclusion from goods and services or jobs, which is
discussed in the next Section.
1. Particular Disadvantage That Is Significantly More Negative in Its Effects
on a Protected Group
To bring a successful claim, a particular disadvantage must occur for one
of the protected groups in comparison to a particular person or group in a
similar sit uation in a protected sector: employment, welfare, or goods and
services. Interestingly enough, the ECJ explained that “ ‘particular
disadvantage’ within the meaning of that provision does not refer to serious,
obvious or particularly significant cases of inequality, but denotes that it is
particularly persons of a given racial or ethnic origin who are at a disadvantage
because of the provision, criterion or practice at issue . . . .”178 The low bar for
the notion of “particular disadvantage ” is very relevant for cases of
discriminatory advertisements which might otherwise be seen as trivial.
Conversely, some Member State case law suggests that a certain threshold
of disadvantage must be met. The implementation assessment of the Gender

 177. See generally CHEZ, supra note 16.
 178. Id. at ¶ 109; see also Grozev, supra note 170, at 175 (explaining that “particular
disadvantage” and “less favourable treatment” should be seen as comparable in their severity).

2020] AFFINITY PROFILING AND OBA 403

Access Directive states that the issue of differential pricing is underexplored
because it is sometimes seen as “trivial.”179 For example, in Sweden, differential
prices for haircuts for men and women are seen as “trivial” issues. 180
Furthermore, despite the ECJ having struck dow n a provision in the Gender
Access Directive in 2012 that allowed insurance companies to have different
prices based on gender,181 some Member States such as Estonia, Hungary, and
(to a lesser degree) Finland still allow these practices . The European
Commission has expressed concern that such national provisions do not
comply with the ECJ’s ruling.182
Another potential standard for defining “particular disadvantage” can be
found under the GDPR. In the context of data protection law and the
safeguards around automated decision- making with legal and significant
effects (Article 22 of the GDPR), the Working Party explained that price
discrimination can be seen as a type of automated decision that impacts
individuals significantly.183 Data subjects receive additional protection under
data protection law on this basis. Potential parallels can be found between E.U.
non-discrimination law and the notion of “particular disadvantage,” and the
Working Party’s concept of legal and significant effects (e.g. , differential
pricing especially credit, health, or decisions relating to education or
employment) in the GDPR. 184 Thus, discriminatory advertisements as
described in the Working Party’s February Guidelines on automated decision-
making could be interpreted as a type of particular disadvantage.
Despite this, practical challenges remain. Individuals are often unaware
that they are discriminated against. In the offline world this might be a simpler
problem. Consumers, for example, have the ability to compare prices in
different stores. Similarly, consumers would know if a vendor refuses to sell
products to them. In the online world, discriminatory treatment can be much
harder to observe. Consumers may not know whether they or others have been

 179. EUR. PARLIAMENTARY RESEARCH SERV., supra note 111, at I-38.
 180. Id. at I-36.
 181. Case C-236/09, Association belge des Consommateurs Test-Achats ASBL v. Conseil
des ministres, ECLI:EU:C:2011:100, ¶¶ 30–34 (Mar. 1, 2011); see also Schiek, supra note 108, at
436 (criticizing this provision by stating: “One of the purposes of equality law is deeply
individualistic: no one shall be judged on the basis of assumptions in line with group
characteristics. Again, the insurance argument is a perfect test case”); Guidelines on the
Application of Council Directive 2004/113/EC to Insurance, in the Light of the Judgment of
the Court of Justice of the European Union in Case C-236/09 (Test-Achats), ¶ 14, 2012 O.J.
(C 11) 1, 3 (EU) (explaining that some gender-based differences in premiums are still possible).
 182. EUR. PARLIAMENTARY RESEARCH SERV., supra note 111, at I-23.
 183. Art. 29 WP Feb. Guidelines, supra note 6, at 22.
 184. Id. at 21–22.

404 BERKELEY TECHNOLOGY LAW JOURNAL [Vol. 35:367

offered a better price or (not) shown ads , or if they have been excluded from
the market.
Further, it is also not clear if online advertising constitutes “a particular
disadvantage” in the sense of the regulation. The court explained in Chez that
the threshold should not be situated too high: “ ‘[P]articular disadvantage’
within the meaning of [Article 2(2)(b) of Directive 2000/34] does not refer to
serious, obvious or particularly significant cases of inequality, but denotes that
it is particularly persons of a given racial or ethnic origin who are at a
disadvantage because of the provision, criterion or practice at issue  . . . .”185
Nonetheless, the ephemeral nature of online advertising may not be
comparable to a long -lasting systemic inequality. On the other hand, while a
particular ad might be ephemeral , the ad delivery system is not and could
exhibit systematic bias and is evidence of “persistent and relatively constant
disparity over a long period . . . .”186
Without algorithmic transparency and more transparent bu siness models,
it will be hard for claimants to prove prima facie discrimination and thus shift
the burden of proof to the alleged offender. 187 This could prove to be a great
challenge in the future as previous cases show that applicants are not
necessarily entitled to confidential information (in this case personal data of
another job applicant) in order to prove non-discrimination claims.188
2. Disproportionately Affected in a Negative Way (A Comparator)
In addition to demonstrating that a particular disadvantage occurred, the
claimant needs to find a group that is treated more favorably. This means that
the claimant must show that the disputed measure negatively affected “far

 185. CHEZ, supra note 16, at ¶ 109.
 186. See Case C-167/97, Regina v. Secretary of State for Employment, ex parte Seymour-
Smith, 1999 E.C.R. I-666, ¶ 61.
 187. See Philipp Hacker, Teaching Fairness to Artificial Intelligence: Existing and Novel Strategies
Against Algorithmic Discrimination Under EU Law, 55 COMMON MKT. L. REV. 1143, 1145, 1162–
64 (2018) (criticizing the lack of transparency in financial and insurance decisions).
 188. Case C-104/10, Kelly v. Nat’l Univ. of Ireland, 2011 E.C.R. I-06813, ¶ 39. This case
is interesting insofar as the court acknowledges that the lack of access is a problem. FARKAS
& O’DEMPSEY, supra note 93, at 28 –29; see also Case C-415/10, Meister v. Speech Design
Carrier Sys. GmbH, ECLI:EU:C:2012:217 (Apr. 19, 2012) (a similar case where the court
stated that while the applicant did not have a right of access to information on the person
hired for a job from which she was rejected, the refusal to share any information by the alleged
offender could have been interpreted as prima facie discrimination, causing the burden of proof
to shift: this issue was left for the national court in Germany to decide, and the court ultimately
rejected the claim).

2020] AFFINITY PROFILING AND OBA 405

more woman than men”189 or a protected group “far more”190 than others in a
similar situation.
Unfortunately, European case law varies noticeably in this regard. 191 For
example, in a Spanish case in relation to part-time work, the ECJ acknowledged
that if 80% of the affected group are women, the adve rse action constitutes
discrimination.192
The aforementioned study 193 also shows the importance of statistics to
prove differential results and refers to a summary of ECJ’s jurisprudence that
can be found in the AG Léger’s opinion in the Nolte  v.
Landesversicherungsanstalt Hannover case:194
[I]n order to be presumed discriminatory, the measure must affect
“a far greater number of women than men” or “a considerably lower
percentage of men than women” or “far more women than men”
. . . . Cases suggest that the  proportion of women affected by the
measure must be particularly marked. In Rinner-Kühn, the Court
inferred the existence of a  discriminatory situation where the
percentage of women was 89 %. In this instance, per se the figure of
60 % . . . would therefore probably be quite insufficient to infer the
existence of discrimination.195

 189. See Case C-1/95, Gerster v. Bayern, 1997 E.C.R I-5274, ¶ 30 (“According to settled
case-law, indirect discrimination a rises where a national measure, although formulated in
neutral terms, works to the disadvantage of far more women than men”); see also Case C-123/
10, Brachner v. Pensionsversicherungsanstalt, 2011 E.C.R. I -10044, ¶ 56; Case C -7/12,
Riežniece v. Zemkopības ministrija, ECLI: EU:C:2012:410, ¶ 39 (June 20, 2013) (addressing
indirect discrimination on the grounds of sex); Case C -363/12, Z. v. Gov. Dep’t,
ECLI:EU:C:2014:159, ¶ 53 (Mar. 18, 2014).
 190. Case C-123/10, Brachner v. Pensionsversicherungsanstalt, 2011 E.C.R. I-10044, ¶ 56
(“[a]ccording to the Court’s settled case -law, indirect discrimination arises where a national
measure, albeit formulated in neutral terms, works to the disadvantage of far more women
than men”); Case C-385/11, Isabel Elbal Moreno v. Instituto Nacional de la Seguridad Social,
ECLI:EU:C:2012:746, ¶ 29 (Nov. 22, 2012); Case C-527/13, Fernández v. Instituto Nacional
de la Seguridad Social, ECLI:EU:C:2015:215, ¶ 28 (Apr. 14, 2015).
 191. Sandra Wachter, Brent Mittelstadt & Chris Russell, Why Fairness Cannot Be Automated:
Bridging the Gap Between EU Non-Discrimination Law and AI (manuscript at 29–31) (Mar. 3, 2020),
https://papers.ssrn.com/abstract=3547922 (discussing  variability and imprecision in
thresholds for particular disadvantage across E.U. case law).
 192. Case C-385/11, ECLI:EU:C:2012:746, supra note 190, at ¶¶ 31–32 .
 193. EUR. UNION AGENCY FOR FUNDAMENTAL RIGHTS & COUNCIL OF EUR., supra note
98, at 242–48.
 194. Case C-137/93, Nolte v. Landesversicherungsanstalt Hannover, Advisory Opinion,
1995 E.C.R. I-4627, ¶¶ 56–58.
 195. EUR. UNION AGENCY FOR FUNDAMENTAL RIGHTS & COUNCIL OF EUR., supra note
98, at 242–43 (internal citations omitted).

406 BERKELEY TECHNOLOGY LAW JOURNAL [Vol. 35:367

In relation to different rights for part-time workers, courts have found that
potential discrimination was sufficiently proven in cases where 87.9% 196 or
87%197 of part- time employees were women. The abstract danger of a
protected group being affected at a large percentage was sufficient.
At the same time, the ECJ held in Regina v Secretary of State for
Employment, ex parte Nicole Seymour-Smith and Laura Perez that a measure
which only allow appeals against unfair dismissal after two years of continuous
employment, which affected 77.4% men and 68.9% women, did not amount
to indirect discrimination against women’s rights to appeal.198 It remains open
whether an 80 –90% threshold is normatively acceptable or desirable, or
whether this threshold should be lower.
Practically speaking, in OBA, finding a comparable group that is
significantly treated differently can be difficult due to a lack of transparency in
algorithmic decision- making and business practices. Not knowing the
optimization conditions or decision rules of algorithms make it difficult to
prove a case. If, for example, an employer was to decide that only people taller
than one meter and eighty centimeters should be hired, it would be easy to
establish prima facie discrimination.199 In this case, the rule is well known (via
hiring strategy) and thus it is easier to find statistical evidence to show that,
while the rule does not directly use gender as a discriminating factor, it would
nonetheless affect women disproportionately. In the online world, we often
do not know the rules and attributes on which we are profiled and whether
these attributes correlate with protected characteristics. We cannot be sure
how our interests (e.g., music) correlate with protected attributes (e.g., gender),
as we lack a full causal model of the world that would show us how this data
relates to each other.200
Further, potential claimants do not know the makeup and size of  their
profiling group, which other groups exist, and how they are treated in
comparison to those other groups. This makes it difficult to prove that a
protected group was disproportionally negatively affected. Trade secrets and
business secrecy have formed a strong barrier in the past to algorithmic

 196. Joined Cases C-4/02 & C-5/02, Schönheit v. Stadt Frankfurt am Main, 2003 E.C.R.
I-583, ¶¶ 35, 63–64.
 197.  Case C-1/95, 1997 E.C.R I-5274, supra note 189, at ¶ 33.
 198.  Case C-167/97, 1999 E.C.R. I-666, supra note 186, ¶¶ 63–65; see also Dalenberg, supra
note 174, at 623.
 199. Inspiration for this hypothetical was taken from a case heard by the Federal Labour
Court in Germany. Bundesarbeitsgericht [BAG] [Federal Labor Court] Feb. 18, 2016, 8 [AZR]
638/14 (discussing Lufthansa’s policy of only hiring pilots taller than 1.65 m).
 200. See Kusner et al., supra note 58; Russell et al., supra note 58, at 6397.

2020] AFFINITY PROFILING AND OBA 407

accountability and fairness. 201 To remedy this, more transparency is needed.
Specifically, information must be made available to individuals and groups
affected by OBA and affinity profiling concerning the composition of their
profiling group(s) and the distribution of outcomes across the affected
population. This information is essential for affected parties to define
legitimate disadvantaged and comparator groups.
On the positive side, if a comparable group can be found (and a particular
disadvantage occurred), the burden of proof is shifted from the claimant to
the accused. Only prima facie discrimination must be shown to shift  this
burden, at which point the accused must prove lawful behavior.
This can be done in two ways. First, by demonstrating that there was no
causal link between the prohibited ground and the differential treatment,
meaning that the same effect would have happened if the claimant had a
different age, gender, ethnicity, etc.202 Alternatively, the accused can show that
even though differential treatment occurred, it was justified because a
legitimate aim was pursued in a necessary and proportionate manner. 203 If
neither condition can be established, the alleged offender will be liable for
discrimination, regardless of their actual intent.204
C. JUSTIFICATION OF DISCRIMINATION
Both direct and indirect discrimination can be justified under certain
circumstances. Since differential treatments and results for protected groups
can be lawful under certain circumstances, it is necessary to take a closer look
at how discrimination can be justified. As discussed in Part III, direct
discrimination is only lawful if it is explicitly named in the non-discrimination
directives (e.g., genuine “occupational requirement ”205 or Recital 16 of the
Gender Goods and Service Directive 206) or in Member State law . Indirect

 201. Sandra Wachter, Brent Mittelstadt & Luc iano Floridi, Why a Right to Explanation of
Automated Decision-Making Does Not Exist in the General Data Protection Regulation, 7 INT’L. DATA
PRIVACY L. 76, 85–89 (2017); see also Merrill & Tobin, supra note 47 (discussing Facebook’s
efforts to prevent ad transparency tools from accessing information); but see ProPublica Data
Store, COMPAS Recidivism Risk Score Data and Analysis , PROPUBLICA DATA STORE (2016),
https://www.propublica.org/datastore/dataset/compas-recidivism-risk-score-data-and
-analysis (last visited May 7, 2019) (analyzing Northpointe’s COMPAS algorithm for bias or
unfairness).
 202. ELLIS & WATSON, supra note 12, at 167.
 203. This is mentioned in all E.U. non-discrimination directives. See, e.g., Council Directive
2000/43/EC, supra note 14, at art. 2(2)(b).
 204. Id.
 205. E.g., Council Directive 2000/78/EC, supra note 14, at art. 4.
 206. E.g., single-sex private clubs or single-sex sports events.

408 BERKELEY TECHNOLOGY LAW JOURNAL [Vol. 35:367

discrimination is only lawful if a legitimate aim is pursued and the measure is
necessary and proportionate.207
Unfortunately, European case law does not have a clear standard for what
constitutes a legitimate interest.208 At a minimum, some economic justifications
can be seen as legitimate. 209 Courts have found economic justifications to be
legitimate with respect  to less strict e mployment labor laws to alleviate the
burden for small businesses210 and to serve customer preferences,211 as well as
in relation to the exclusion from the pension scheme based on objectively
justified economic grounds. 212 At the same time , the ECJ, on various
occasions, has ruled that economic interests (e.g., cutting public expenditure213

 207. As stated in all the E.U. non-discrimination directives.
 208. For a strong critique of the broad possibilities of legitimizing indirect discrimination
through the frameworks themselves (Article 2(2) of the Employment Directive) as well as the
incoherence of the jurisprudence of the ECJ over the years, see ELLIS & WATSON, supra note
12, at 409–18. For a further overview of the Court’s accepted legitimate aims, see CHRISTA
TOBLER, LIMITS AND POTENTIAL OF THE CONCEPT OF INDIRECT DISCRIMINATION 33–35
(Christa Tobler & Europäische Kommission eds., 2008).
 209. See Case C -196/02, Nikoloudi v. Organ ismos Tilepikinonion Ellados AE, 2005
E.C.R. I-1812, ¶ 52 (“Even supposing that this last argument put forward by [defendant] seeks
to assert a legitimate aim falling within policy on economic development and job creation, it
nevertheless constitutes a mere generalisation insufficient to show that the aim of the measures
at issue is unrelated to any discrimination on grounds of sex . . . .”).
 210.  See Case C-189/91, Kirsammer-Hack v. Sidal, 1993 E.C.R. I-6215, ¶ 35 (“[W]here it
is not established that undertakings which are not subject to that system employ a considerably
greater number of women than men. Even if that were the case, such a measure might be
justified by objective reasons not related to the sex of the employees in so far as it is intended
to alleviate the constraints weighing on small businesses.”).
 211. This was a direct discrimination case (which also needs a legitimate aim to be lawful)
in relation to regulating the midwife profession. Case C -165/82, Comm’n of the Eur. Cmty.
v. United Kingdom of Great Britain and Northern Ireland, 1983 E.C.R 3432, ¶ 20 (stating that
provisions favoring women over man are justified because “[i]t must however be recognized
that at the present time personal sensitivities may play an important role in relations between
midwife and patient”).
 212. It was for the national court to decide if the measure corresponded to a real need is
necessary and appropriate. The sole fact that this measure affected more women than men
was not sufficient to claim indirect discrimination. See Case C-170/84, Bilka-Kaufhaus GmbH
v. von Hartz, 1986 E.C.R. I-1620, ¶ 36.
 213. For example, the aim of restricting public expenditure was not sufficient to justify
differential treatment between men and women. See Joined Cases C -4/02 & C -5/02, 2003
E.C.R. I -583, supra note 196, at ¶  84. In a different case, it was found that budgetary
considerations alone are not a legitimate interest. See Case C-196/02, 2005 E.C.R. I-1812, supra
note 209, at ¶ 53. For more details on economic justification, see Justyna Maliszewska-
Nienartowicz, Direct and Indirect Discrimination in Europe an Union Law –How to Draw a Dividing
Line?, 3 INT’L. J. SOC. SCI. STUD. 41, 44 (2014).

2020] AFFINITY PROFILING AND OBA 409

or increasing costs 214) cannot be the sole justification for discriminatory
measures in the public sector. The ECJ has ruled similarly, albeit with less
clarity, concerning the private industry, with respect to, for example, a policy
of neutrality via a company’s customers and customer satisfaction.215 Similarly,
the court has rejected the argument that that the costs associated with
rectifying inequality (i.e., a pay gap) can justify maintaining the status quo for
both the private and the public sectors.216 Similarly, the court ruled that “while
budgetary considerations may underpin the chosen social policy of a Member
State and influence the nature or extent of the measures that that Member
State wishes to adopt, such considerations cannot in themselves constitute a
legitimate aim within the meaning of Article 6(1) of Directive 2000/78 . . . .”217
Of course, it can be argued that different standards might apply to public
and private entities. However, it seems unlikely that the ECJ would allow a
completely different interpretation of the Directives for the private industry
compared to the public sector. 218 It seems more likely that a fair balance of
interests must be established that acknowledges that legitimate aims are

 214. See Case C-243/95, Hill v. Revenue Comm’r, 1998 E.C.R. I -3759, ¶ 40 (“So far as
the justification based on economic grounds is concerned, it should be noted that an employer
cannot justify discrimination arising from a job -sharing scheme solely on the ground that
avoidance of such discrimination would involve increased costs.”).
 215. In relation to customer complaints against employees providing IT services wearing
a headscarf, see Case C- 188/15, Bougnaoui, Association de défense des droits de l’homme
(ADDH) v. Micropole SA, ECLI:EU:C:2017:204, ¶ 40 (Mar. 14, 2017) (“It follows from the
information set out above that the concept of a ‘genuine and determining occupational
requirement’, within the meaning of that provision, refers to a requirement that is objectively
dictated by the nature of the occupational activities concerned or of the context in which they
are carried out. It cannot, however, cover subjective considerations, such as the willingness of
the employer to take account of the particular wishes of the customer.”). However, it was for
the national court to decide whether the action should be seen as indirect or direct
discrimination, which has implications on possible justifications. See id. ¶¶ 31–32. But see Case
C-157/15, Achbita v. G4S Secure Sol. NV, ECLI:EU:C:2017:203, ¶ 37 (Mar. 14, 2017) (“As
regards, in the first place, the condition relating to the existence of a legitimate aim, it should
be stated that the desire to display, in relations with both public and private sector customers,
a policy of political, philosophical or  religious neutrality must be considered legitimate.”).
However, it was for the referring court to decide if this measure is appropriate and necessary.
See id. at ¶ 44.
 216. See generally Case 43-75, Gabrielle Defrenne v. Société anonyme belge de navigation
aérienne Sabena, 1976 E.C.R. I-455.
 217. Case C-530/13, Schmitzer v. Bundesministerin für Inneres, ECLI:EU:C:2014:2359,
¶ 41 (Nov. 11, 2014); see also Joint Cases C-159/10 & C-160/10, Gerhard Fuchs v. Hessen,
ECLI:EU:C:2011:508, ¶ 74 (July 21, 2011).
 218. See TOBLER, supra note 208, at 6, 33 (claiming that budgetary reasons alone can never
constitute a legitimate aim).

410 BERKELEY TECHNOLOGY LAW JOURNAL [Vol. 35:367

different from budgetary reasons or competitiveness.219 In stark contrast, some
reports suggested that “[p]urely budgetary (financial) considerations can never
serve as objective justifications.”220
While the jurisprudence is inconsistent, the case law shows the court’s
preference for an overarching societal aim ( e.g., social and employment
policy221), rather than pure economic interests, when assessing what constitutes
a legitimate aim. For example, the court accepted legitimate aims such as public
safety in relation to the police force ,222 more job security for people over the
age of forty at the expense of younger people,223 integration of people without
a secondary degree into the job market and higher education, 224 forced
retirement to offer job opportunities for the youth,225 age limitations for safety
reasons,226 and compensation for career breaks to take care of children.227

 219. See ELLIS & WATSON, supra note 12, at 412 (“[L]egitimate aims are distinguishable
from purely individual reasons particular to the employer’s situation, such as cost reduction or
improving competitiveness, although it cannot be ruled out that a national rule may recognize,
in the pursuit of those legitimate aims, a certain degree of flexibility for employers.”).
 220. FARKAS & O’DEMPSEY, supra note 93, at 37.
 221. See Case C-173/13, Leone v. Garde des Sceaux, ECLI:EU:C:2014:2090, ¶ 53 (July
17, 2014) (holding that a legitimate social-policy objective is a legitimate aim).
 222. Access to posts and vocational training with firearms were restricted for women as
they are more often the victims of assassinations. It was left to the national court to decide if
the legitimate aim is pursued in a necessary and proportionate manner. See Case C-222/84
Johnston v. Chief Constable of the Royal Ulster Constabulary, 1986 E.C.R. I-206, ¶¶ 35, 62.
 223. Whilst the legitimate aim was lawful and shorter notice periods for people under the
age of twenty -five were seen as justified, the provision was still unlawful because “the
legislation is not appropriate for achieving that aim, since it applies to all employees who joined
the undertaking before the age of 25, whatever their age at the time of dismissal.” Case C-555/
07, Kücükdeveci v. Swedex GmbH & Co. KG., 2010 E.C.R. I-393, ¶¶ 34, 40.
 224. However, the provision was seen as not suitable to achieve this legitimate interest
and thus deemed unlawful. See Case C-88/08, Hütter v. Technische Universität Graz, 2009
E.C.R. I-5327, ¶¶ 46, 50.
 225. The case centered around dentists. Whether or not this measure was necessary and
appropriate was left for the national court to decide. See Case C -341/08, Petersen v.
Berufungsausschuss für Zahnärzte für den Bezirk Westfalen-Lippe, 2010 E.C.R. I-71, ¶¶ 68,
74.
 226. In relation to maximum age for recruitment of firefighters, see Case C-229/08, Wolf
v. Stadt Frankfurt am Main, 2010  E.C.R. I-1, ¶¶ 43–45, 48. However, this ruling is disputed
and seen as controversial. See ELLIS &WATSON, supra note 12, at 393. A different ruling stated
that a maximum age for pilots is a legitimate aim; however, in this case lowering of the
retirement age was seen as not necessary because public airlines had higher retirement ages
and have to deal with the same safety issues. See Case C-447/09, Prigge v. Deutsche Lufthansa
AG, 2011 E.C.R. I-8003, ¶¶ 68–69, 84 (2011). Note that both of these cases relate to direct
discrimination based on age, but lawful direct discrimination also requires a legitimate aim.
 227. In relation to better pension schemes (early retirement) for people that took  career
breaks, see Case C-173/13, ECLI:EU:C:2014:2090, supra note 221, at ¶ 104.

2020] AFFINITY PROFILING AND OBA 411

Other legitimate aims according to Justyna Maliszewska-Nienartowicz
include:
ensuring coherence of the tax system; the safety of navigation,
national transport policy and environmental protection in the
transport sector; protection of ethnic and cultural minorities living
in a particular region; ensuring sound management of public
expenditure on specialized medical care; encouragement of
employment and recruitment by the Member States; guaranteeing a
minimum replacement income; need to respond to the demand for
minor employment and to fight unlawful employment.228
The promotion of full- time work has also been acknowledged as a
legitimate interest of an employer, who used this interest to exclude part-time
workers from a pensions scheme. 229 Therefore, in these and similar cases ,
indirect discrimination can be justified if seen as both necessary and
proportionate.
Even though the ECJ views social and employment policy as a legitimate
aim, and grants Member States a higher margin of appreciation in this regard,230
it still requires that the measures enacting those policies be necessary and
proportionate:
[m]ere generalisations concerning the capacity of a specific measure
to encourage recruitment are not enough to show that the aim of the
disputed rule is unrelated to any discrimination based on sex nor to
provide evidence on the basis of which it could reasonably be
considered that the means chosen were suitable for achieving that
aim.231
In Bilka-Kaufhaus GmbH v. von Hartz, the court provided more detail on the
proportionality test. 232 The court explained that, in relation to sex
discrimination, the test has three steps. In order to justify indirect
discrimination, the measures must “correspond to a real need on the part of

 228. Maliszewska-Nienartowicz, supra note 213, at 44–45.
 229. Case C-170/84, 1986 E.C.R. I-1620, supra note 212, at ¶ 37. The argument was that
part-time workers often refuse to work in the afternoon and on weeke nds. Id. at ¶ 33.
Unfortunately the court did not discuss whether this measure was necessary or proportionate.
 230. Case C-317/93, Nolte v. Landesversicherungsanstalt Hannover, 1995 E.C.R. I-4650,
¶ 33.
 231.  Case C-167/97, 1999 E.C.R. I -666, supra note 186, at ¶ 76; see also TOBLER, supra
note 208, at 6, 35 (discussing the scope of legitimate aims in relation to justification of potential
discrimination).
 232. Case C-170/84, 1986 E.C.R. 1620, supra note 212, at ¶ 36.

412 BERKELEY TECHNOLOGY LAW JOURNAL [Vol. 35:367

the undertaking, are appropriate with a view to achieving the objectives
pursued and are necessary to that end . . . .”233
How does lawful justification apply to advertisements? The decision to
show ads to people could be based on a “neutral provision, criterion or
practice,”234 such as geolocation. Companies may not, for example, have an
explicit intention to use ethnicity as an excluding factor. Rather, discriminatory
advertisements could be based on the assumed interests of a certain
demographic, meaning the “neutral provision” was a business and
optimization decision. However, differential results can still occur (e.g., certain
ads (not) being shown) , which are only lawful with an objective justification,
and ideally not based on economic and business concerns (e.g. , customer
satisfaction, profit maximization) alone. Rather, as the court stated in Bilka-
Kaufhaus, the discriminatory measure must correspond to a “real need” in order
to be deemed a legitimate aim.235
Even if a legitimate aim is pursued, the measure taken must still be deemed
necessary and proportionate. As was demonstrated in CHEZ in relation to the
offensive nature of the meter installation in an unreachable height, if
advertisement practices closely overlap with, for example , stereotypical
grouping, they could be seen as offensive and stigmatizing.236 In such a case,
certain ads could potentially be unlawful even if a legitimate aim is pursued
and no less- infringing measures exist. 237 The stigmatizing nature of the
practice, specifically showing certain ads to certain groups , could make this
practice disproportionate and therefore potentially illegal. And as mentioned
above, if these ads are seen as illegal, they would not only violate directly or
indirectly the interests of people that share the protected attribute , but also
violate the interests of people that were associated with this group on the basis
of discrimination by association.
Of course, a claim will only be successful if the advertisements in question
fall under one of the protected areas (e.g., employment), affects legally
protected groups (e.g., religion or beliefs) , and a particular disadvantage
occurred. Moreover, finding a comparable group that is treated significantly
better can be difficult due to opaque algorithmic behavior and business
models, as well as the dispersed nature of advertisement provisioning, which
can increase the difficulty of locating other relevant individuals who were or
were not shown a particular advertisement.

 233. Id.
 234. See supra note 14.
 235. Case C-170/84, 1986 E.C.R. 1620, supra note 212, at ¶¶ 36–37.
 236. CHEZ, Advisory Opinion, supra note 168, at ¶¶ 60, 84, 87, 108, 128.
 237. Id. at ¶ 128.; Grozev, supra note 170, at 183.

2020] AFFINITY PROFILING AND OBA 413

V. PROTECTION OF NON-TRADITIONAL GROUPS
Even if these hurdles are overcome, and even with the most generous
interpretations of non- discrimination and data protection law, these
frameworks could still fail to guard against the novel risks of inferential
analytics. Discriminatory advertising practices can equally affect new types of
groups created through inferential analytics that do not map onto historically
protected attributes. Both types of law might fall short in providing adequate
protection to groups that fall outside the scope of legally protected groups.
Automated decision-making and profiling expand the range of potential
victims of discrimination and other potential harms (e.g. , privacy, financial,
and reputational) beyond traditionally protected groups. Profiling seeks to
identify unintuitive connections between people and to group or otherwise
stratify them according to attributes that do not count as special category data
or fall within the remit of non- discrimination law. In practic e, profiling
constructs ephemeral groups of potentially similar individuals. 238 This type of
classification can prove problematic in two ways: either by drawing invasive
inferences from a dataset, which is a problem of privacy and data protection,
or by taking unacceptable actions based on these inferences , which is a
problem of discrimination. 239 European data protection and non-
discrimination law may not sufficiently guard against these risks.
Data protection law only applies to drawing inferences if personal data is
processed and the data relates to an identifiable individual. 240 Inference-
drawing practices can thus avoid data protection law in a few ways. Group
profiling can be done by evaluating data about other people or data that does
not fall under data protection law (e.g. , non-personal data or anonymized
data).241 While individuals have no control or protections against insights
drawn from these types of data, the data can nonetheless reveal intimate details
of the individual’s life.
Profiling can also be performed without singling out data subjects. 242 But
identifying and singling out individuals is a precondition for data protection

 238. Brent Mittelstadt, From Individual to Group Privacy in Big Data Analytics , 30 PHIL. &
TECH. 475, 478 (2017).
 239. See supra Section II.C, Part III.
 240. See GDPR, supra note 61, at art. 4(1) (“  ‘[P]ersonal data’ means any information
relating to an identified or identifiable natural person (‘data subject’); an identifiable natural
person is one who can be identified,  directly or indirectly, in particular by reference to an
identifier such as a name, an identification number, location data, an online identifier or to one
or more factors specific to the physical, physiological, genetic, mental, economic, cultural or
social identity of that natural person . . . .”).
 241. See Wachter, supra note 21, at 7.
 242. See Mittelstadt, supra note 23, at 478.

414 BERKELEY TECHNOLOGY LAW JOURNAL [Vol. 35:367

law to apply. According to the Working Party , a person is singled- out or
“considered as ‘identified’ when, within a group of persons, he or she is
‘distinguished’ from all other members of the group. ”243 Successful affinity
profiling does not require identifying or singling out data subjects in this sense,
but nonetheless allows for sensitive information to be inferred which can drive
discriminatory actions. This observation suggests that, in order to sufficiently
protect against the novel risks and new types of groups creat ed by profiling
and inferential analytics, it would be sensible to abandon artificial data
categories and no longer focus solely on identifiability, and instead create new
protections based on holistic notions of data about people and group
conceptions of privacy.244
With regard to actions based on inferences made , similar problems arise
with European non- discrimination law, which is based on historical lessons.
Non-discrimination laws protect , for example , against religion and gender-
based direct and indire ct discrimination because such discrimination has
occurred in the past.245 However, inferential analytics can identify new patterns
and similarities between individuals,246 who can then be grouped for purposes
of ad provisioning. The difficulty is that these  new type of “ad hoc groups”247
are not guaranteed to align or correlate with the traditional social constructs or
attributes (e.g., religion, gender, or ethnicity) protected in non- discrimination
law, and yet  these groups  will experience discrimination wit h comparable
harmful effects via the same mechanisms as protected groups.248
Inferential analytics widens the range of victims of discriminatory actions.
These new types of victims do not map to or might not correlate with current
concepts in the law , as  new types of discrimination become possible. F or

 243. Even though knowing the name is not necessary to be singled out, other identifiers
(e.g., “socio -economic, psychological, philosophical or other criteria”) might suffice. See
ARTICLE 29 DATA PROT. WORKING PARTY, OPINION 4/2007 ON THE CONCEPT OF
PERSONAL DATA, 01248/07/EN WP 136, at 12–13 (adopted June 20, 2007) [hereinafter Art.
29 WP Op. 4/2007].
 244. Wachter, supra note 21, at 7; Tal Z. Zarsky, Incompatible: The GDPR in the Age of Big
Data, 47 SETON HALL L. REV. 995, 1013 (2017) (addressing the need to redefine artificial data
categories).
 245. Mantelero, supra note 22, at 765; see generally Alessandro Mantelero, Personal Data for
Decisional Purposes in the Age of Analytics: From an Individual to a Collective Dimension of Data Protection,
32 COMPUT. L. & SEC. REV. 238 (2016). For an analysis of discrimination under U.S. law, see
generally Solon Barocas & Andrew D. Selbst, Big Data’s Disparate Impact, 104 CALIF. L. REV.
671 (2016).
 246. Samuel Yeom, Irene Giacomelli, Matt Fredrikson & Somesh Jha, Privacy Risk in
Machine Learning: Analyzing the Connection to Overfitting , in 2018 IEEE 31ST COMPUT. SEC.
FOUND. SYMP. 268, 268–69 (2018).
 247. Mittelstadt, supra note 23, at 485.
 248. Mantelero, Personal Data, supra note 245, at 240.

2020] AFFINITY PROFILING AND OBA 415

example, less favorable treatment  can be given for people who own dogs,249
are born on a Tuesday, are identified as “sad teens ,”250 “Young Single
Parents,”251 or video gamers,252 or people who belong to groups that occupy
legal or ethical grey areas such as gamblers ,253 or drug addicts. Even more
opaque are groups that are created by neural nets where we have no concept
in our language to describe the characteristics of the group or the inferences
drawn about the group.254 In other words, groups of individuals perceived to
be similar to one another can be unfairly treated (e.g. , offered high-cost loans
and financially risky products), 255 without being singled out on the basis of
sensitive attributes.256
Put differently, groups such as “dog owners” are not protected under non-
discrimination law. As a result, no protection under direct discrimination is
possible. Of course, claims can be made under indirect discrimination if dog
ownership correlates with a prote cted attribute and all the other conditions
mentioned in Part IV are met. Apart from the technical difficulties257 to detect
the proxy power of dog ownership, it might be the case that this category does
not sufficiently correlate with a protected group , where disproportionately
affected means around 80–90% of the group are disadvantaged. 258 The ECJ

 249. For an overview of commonly used interest categories (i ncluding “Winter Activity
Enthusiast,” “dog owner,” and “Heavy Facebook User”), see generally FED. TRADE COMM’N,
DATA BROKERS: A CALL FOR TRANSPARENCY AND ACCOUNTABILITY B-2–B-6 (2014).
 250. Michael Reilly, Is Facebook Targeting Ads at Sad Teens? , MIT TECH. REV., https://
www.technologyreview.com/s/604307/is-facebook-targeting-ads-at-sad-teens/ (last visited
Apr. 19, 2019).
 251. Art. 29 WP Feb. Guidelines, supra note 6, at 10.
 252. Being labelled as a video gamer can cause the Chinese Social Credit Score to drop.
See Nicole Kobie, The Complicated Truth About China’s Social Credit System, WIRED UK (June 7,
2019, https://www.wired.co.uk/article/china-social-credit-system-explained.
 253. The Working Party warns about the possible exploitation of gamers via nudging and
online ads. See ARTICLE 29 DATA PROTECTION WORKING PARTY, Guidelines on Automated
individual decision-making and Profiling for the purposes of Regulation 2016/679, 17/EN WP 251  11
(2017), http://www.hldataprotection.com/files/2017/10/20171013_wp251_enpdf.pdf (last
visited Oct 22, 2017).
 254. Jason Yo sinski, Jeff Clune, Anh Nguyen, Thomas Fuchs & Hod Lipson,
Understanding Neural Networks Through Deep Visualization, (June 22, 2015) (unpublished
manuscript) https://arxiv.org/abs/1506.06579 (regarding visualizations of the intermediate
layers of neural networks to make the network’s computations more comprehensible).
 255. Art. 29 WP Feb. Guidelines, supra note 6, at 18.
 256. See Mittelstadt, supra note 23, at 478 (regarding how algorithmic groups are assembled
which are not reducible to individual data subjects or their privacy interests and the regulatory
gap for these groups caused by the focus in data protection law on identifiable individuals).
 257. On the challenge to detect proxy data, see Kusner et al., supra note 58 (discussing the
challenges of causal and counterfactual reasoning in detecting algorithmic bias).
 258. See supra Section IV.B.2.

416 BERKELEY TECHNOLOGY LAW JOURNAL [Vol. 35:367

ruled that it is not within its power to create new protected groups (e.g., “dog
owners”) as the list in the Directives is exclusive.259 Similarly, in relation to the
proportionality threshold, the court explained that a measure must , “taken in
isolation,”260 produce the disproportionate effect for one of the protected
grounds. It might be the case that the profile of “dog owners” is not
homogenous enough to meet this requirement. Nonetheless, it can still seem
unreasonable, counterintuitive, or unjust to use dog ownership as a deciding
factor for loan applications, despite it being lawful to use the characteristic as
a basis for decision-making.
These new types of groups also face new challenges in terms of
organization and collective action. Members of ad hoc groups often do not
know that they are part of the group. They are thus less able than historically
protected groups to protect themselves against new forms of discrimination
and other harms made possible by inferential analytics. 261 A clear collective
interest for new forms of group protection is evident, even if specific ad hoc
groups cannot themselves advocate for it.262 Reflecting this, scholars across law
and ethics are beginning to call for greater protection of group interests.263
Mireille Hildebrandt, for example, explains that “we have no access to the
group profiles that have been inferred from the mass of data that is being
aggregated and have not the faintest idea how these profiles impact our

 259. Coleman, supra note 15, at ¶ 46.
 260. The case was centered around a case of intersectionality where the claimant sued on
the basis of the combined factors “age” and “sexual orientation,” where one measure in
isolation did not produce a discriminatory effect. Case C -443/15, Parris v. Trinity College
Dublin, ECLI:EU:C:2016:897, ¶ 80 (Nov. 24, 2016). This shows that one protected group
needs to meet the threshold of disproportionality. For a strong critique, see Howard, supra
note 166, at 69. For an in-depth discussion of this case and on problems with intersectionality
in general, see generally Dagmar Schiek, On Uses, Mis-Uses and Non-Uses of Intersectionality Before
the European Court of Justice (ECJ), 7 CETLS ONLINE PAPER SERIES 1 (2018).
 261. Mittelstadt, supra note 23, at 485.
 262. Mantelero, Personal Data, supra note 245, at 245.
 263. See Mittelstadt, supra note 23; see generally GROUP PRIVACY: NEW CHALLENGES OF
DATA TECHNOLOGIES (Linnet Taylor, Luciano Floridi, & Bart van der Sloot eds., 1st ed.
2017); Mantelero, Personal Data, supra note 245; LEE A. BYGRAVE, DATA PROTECTION LAW:
APPROACHING ITS RATIONALE, LOGIC AND LIMITS (2002). On why big data is challenging
for privacy protection, see generally Solon Barocas & Helen Nissenbaum, Big Data’s End Run
Around Procedural Privacy Protections, 57 COMM. ACM 31 (2014).

2020] AFFINITY PROFILING AND OBA 417

chances in life.”264 In part this is due to group profiles often being protected
as trade secrets.265
Lee A. Bygrave (as one of the first) ,266 Linnet Taylor et al., 267 and
Alessandro Mantelero268 have made similar calls explaining that data protection
law is not equipped for this challenge . Mantelero, for example , calls for
collective privacy rights for affected parties.269 To enforce this, he suggests that
a third party could represent the interests of the group and an independent
party could conduct impact assessments prior to processing in order to prevent
large-scale discrimination and harms.270
The risks of automated decision-making and profiling for groups have also
been acknowledged by the Working Party. 271 Their guidelines on automated
decision-making state that “[p]rocessing that might have little impact on
individuals generally may in fact have a significant effect on certain groups of
society, such as minority groups or vulnerable adults.” 272 It remains open
whether “groups” in this context refers only to traditional vulnerable groups
(e.g., children) or also to groups assembled in a non- traditional sense. The
broader interpretation seems likely, as the guidelines also state that
“[i]ndividuals may wish to challenge  the accuracy of the data used and any
grouping or category that has been applied to them,”273 which is not explicitly
limited to traditionally protected groups or attributes.
It is not unrealistic to assume that ad hoc group privacy interests will be
enshrined in law in the future considering the Working Party’s stance. The

 264. Mireille Hildebrandt, Profiling and the Rule of Law , 1 IDENTITY INFO. SOC’Y 55, 64
(2009), https://papers.ssrn.com/abstract=1332076.
 265. MIREILLE HILDEBRANDT, SMART TECHNOLOGIES AND THE END(S) OF LAW:
NOVEL ENTANGLEMENTS OF LAW AND TECHNOLOGY 93, 103, 139, 222 (2015); see also
Hildebrandt, Profiling and the Rule of Law, supra note 264, at 63–65.
 266. See generally BYGRAVE, supra note 263; Lee A. Bygrave, Privacy Protection in a Global
Context - A Comparative Overview, 47 SCANDINAVIAN. STUD. L. 319 (2004).
 267. See generally GROUP PRIVACY: NEW CHALLENGES OF DATA TECHNOLOGIES, supra
note 263.
 268. See generally Mantelero, Personal Data , supra note 245 (regarding the absence of
collective dimensions in data protection law); Alessandro Mantelero, From Group Privacy to
Collective Privacy: Towards a New Dimension of Priv acy and Data Protection in the Big Data Era , in
GROUP PRIVACY 139 (2017) (regarding the recognition of group privacy in data protection
law); Alessandro Mantelero & Giuseppe Vaciago, Data Protection in a Big Data Society. Ideas for a
Future Regulation, 15 DIGITAL INVESTIGATION 104 (2015) (regarding the challenges for data
protection law introduced by Big Data).
 269. Mantelero, Personal Data, supra note 245, at 249–250.
 270. Id. at 250.
 271. See generally Art. 29 WP Feb. Guidelines, supra note 6.
 272. Id. at 11.
 273. Id. at 24.

418 BERKELEY TECHNOLOGY LAW JOURNAL [Vol. 35:367

Working Party takes issue with profiling which could deprive individuals of
“opportunities based on the actions of others ”274 by using “non-traditional
credit criteria, such as an analys is of other customers living in the same area
who shop at the same stores,”275 without having remedies against it. Following
this, the guidelines recommend that the data subject is “given information
about their profile, for example in which ‘segments’ or ‘categories’ they are
placed.”276 Further, the Working Party suggested that the “conclusive list of
data being regarded as sensitive per se – could be amended so as to react more
flexibly to possible new forms of sensitive data or new forms of data and data
processing which could lead to severe infringements of privacy.”277
VI. SOLUTIONS FOR ACCOUNTABILITY IN OBA AND
AFFINITY PROFILING
With the shortfalls in data protection and non- discrimination law now
clear, there are several potential solutions to address legal challenges facing
OBA and affinity profiling.
A. A RIGHT TO REASONABLE INFERENCES IN OBA
Inferential analytics expose accountability gaps in both privacy protection
and non- discrimination law. Data protection law does not offer sufficient
protection against sensitive inferences, inferences based on non- personal or
anonymized data, or profiling that does not single out individuals. Similarly,
non-discrimination law only offers protection for traditional groups in specific
sectors and only if the group is  disproportionately affected, and thus ignores
new types of algorithmic or profiling groups (e.g., “dog owners” or groups
defined by incomprehensible characteristics).
Recognizing these novel risks of big data, AI, and inferential analytics, a
“right to reasonable inferences” could close the current gaps in data protection
and non-discrimination law.278 Rather than playing catch- up and adding new
types of sensitive data or protected groups to existing laws, a holistic and
sectoral approach is more promising.

 274. Id. at 12; see also Kaveh Waddell, How Algorithms Can Bring Down Minorities’ Credit Scores,
ATLANTIC (Dec. 2, 2016), https:// www.theatlantic.com/technology/archive/2016/12/how
-algorithms-can-bring-down-minorities-credit-scores/509333/ [https://perma.cc/S5Z2
-MUZP].
 275. Art. 29 WP Feb. Guidelines, supra note 6, at 22.
 276. Id. at 23.
 277. Art. 29 WP Advice Paper, supra note 62, at 3.
 278. See generally Wachter & Mittelstadt, supra note 39.

2020] AFFINITY PROFILING AND OBA 419

A right to reasonable inferences would address  the harms of “high risk
inferences,” which (1) are privacy-invasive or damaging to reputation, or have
a high likelihood of being so in the future, or (2) have low verifiability in the
sense of being predictive or opinion- based and are used for important
decisions (e.g., loans and jobs).279 The first condition effectively sets a
proportionality test, according to which the privacy invasion or reputational
damage posed by using a particular data source to draw an inference must be
proportional to the predicted benefit or utility. This right would govern:
(1) why certain data form a normatively acceptable basis from which
to draw inferences; (2) why these inferences are relevant and
normatively acceptable for the chosen processing purpose or type of
automated decision; and (3) whether the data  and methods used to
draw the inferences are accurate and statistically reliable.280
In addition to these ex- ante mechanisms that provide context and
justification for inferences drawn, the right would require “ an additional ex-
post mechanism enabling unre asonable inferences to be challenged .”281 For
example, data controllers could enable data subject s to submit additional
information so they might reconsider or rectify decisions or assessments.
If such a right was granted, the new protections offered would extend
further than mere protection against discrimination, privacy invasion, and
opaque algorithmic measures. This would allow for more agility on a sectoral
basis. The right demands justification of new high- risk forms of inferential
analytics. It would, for example, protect individuals against being grouped
according to inferred “unethical” attributes (e.g., gambling addiction or mental
vulnerability) and guarantee that inferences drawn are accurate (e.g. , that
individuals have at a minimum been grouped accurately or with reliable
statistical measures). The right aims to protect against high-risk unreasonable
inferences and important or high- impact decisions based on them, which
could include discriminatory OBA and affinity profiling. This right could
potentially provide a remedy if designed to detect both individual and group
level harms or to notify individuals as groups are formed and used in profiling
or decision-making, which could facilitate contestation of group membership.

 279. Id. at 619.
 280. Id. at 495. The types of data used to draw inferences could include, for example,
browsing history, geolocation, or clicks and ‘likes’ on social media. Types of automated
decisions could include inferring sexual orientation or political views to display advertisements.
The accuracy and statistical reliability of data concerns could be improved through testing and
verification for bias in the data that underlies inferences and automated decisions.
 281. Id. at 588.

420 BERKELEY TECHNOLOGY LAW JOURNAL [Vol. 35:367

B. CURRENT GOVERNANCE STRATEGIES
Another key question to improve the accountability of OBA and affinity
profiling concerns whether current governance strategies used by
policymakers and companies are fit for the purpose of protecting against
discriminatory OBA and affinity profiling. Progress has been made in recent
years both by the public sector and the private sector, but it is still not enough.
The Working Party commented on the potential privacy implication of
tracking cookies and geolocation data for advertising. 282 Their guidelines
explain that “given the sensitivity of such information and the possible
awkward situations which may arise if individuals receive advertising that
reveals, for example, sexual preferences or political activity, offering/using
interest categories that would reveal sensitive data should be discouraged.”283
The Working Party also proposed greater transparency as a remedy to the
general privacy challenges of cookies and geolocation data . Specifically, they
argued that providing data subjects  and consumers with immediate
information about data processing in relation to OBA can help transform
informed and explicit consent into effective accountability mechanisms.284
While this is a good idea in theory, it overlooks the fact that it has been
long recognized that consent is not a suitable governance mechanism for data
protection.285 In the context of OBA, the ubiquity of advertisements and the
underlying data analytics used to create audiences and target advertisements
suggests well-informed consent is particularly difficult. Consent also fails to
address the justification of data uses286 (e.g., whether the proposed processing
is ethically acceptable independent of whether consent has been given) and
how data controllers handle a data subject’s refus al to give consent or object
to processing.287

 282. Art. 29 WP Feb. Guidelines, supra note 6.
 283. Art. 29 Data Prot. Working Party, Opinion 2/2010, supra note 80, at 19.
 284. Id. at 24–26.
 285. For strong critics of the functionality of informed consent, see, for example, Daniel
J. Solove, Privacy Self-Management and the Consent Dilemma, 126 HARV. L. REV. 1880 (2013); Paul
M. Schwartz, Internet Privacy and the State, 32 CONN. L. REV. 815 (1999); Zuiderveen Borgesius,
supra note 35, at 251–255; N. Van Eijk, N. Helberger, L. Kool, A. van der Plas & B. van der
Sloot, Online Tracking: Questioning the Power of Informed Consent , 14 INFO 57 (2012); Bert -Jaap
Koops, The Trouble with European Data Protection Law , 4 INT’L. DATA PRIVACY L. 250 (2014);
Smit, Van Noort & Voorveld, supra note 2, at 20 (regarding knowledge as a prerequisite for
informed consent which is often lacking in online interactions).
 286. Wachter & Mittelstadt, supra note 39, at 581–88.
 287. However, the situation might improve in the future as “forced consent” is no longer
possible under Article 7 of the GDPR; complaints against Google and Facebook in this vein
have already been launched. See Max Schrems, GDPR: noyb.eu Filed Four Complaints over “Forced
Consent” Against Google, Instagram, WhatsApp and Facebook (May 25, 2018), https://

2020] AFFINITY PROFILING AND OBA 421

To address the difficulty that the ubiquity of OBA creates for consent ,
insofar as individuals would experience information overload if given detailed
information about every advertisement encountered,  the Working Party
suggested using icons and explanations to help users understand why they have
been served with certain ads.288 Companies such as Google and Facebook are
currently offering explanations as to why certain ads have been shown to their
users.289
These explanations generally reveal the interest groups in which users have
been placed. Google informs with “Why you ’re seeing an ad” and “why this
ad” explanations.290 In their Ad Settings, Google also provides information
about the inferences on which ads are served, including , for example , age,
education, an interest in fitness, or an interest in video games.291 Facebook also
provides generic explanations in their “Why Am I Seeing This” feature, which
generally addresses the influence of age, geolocation, profile information, and
previously visited sites on displayed advertisements.292
While current industry standards are an encouraging first step, they remain
insufficient for at least two reasons. First, users often do not see or do not
understand the explanations provided. Boerman et al. assessed users’ attitudes
and perception towards OBA and transparency and found that users rarely
notice disclosures such as icons, logos, or other transparency banners, such as
the “Why did I get this ad?” or “AdChoices” features. Even when noticed,
users often do not understand the icons or the labels provided.293
Second, the explanations provided are often too generic or vague and
provide little detail specific to the individual. If explanations are intended to

www.stetson.edu/law/studyabroad/spain/media/Wk3.Stuart.Day3-2-Forced-Consent
-Complaints.pdf.
 288. Art. 29 WP Feb. Guidelines, supra note 6, at 18.
 289. AD SETTINGS, GOOGLE, https://perma.cc/8J6G-VYPD (last visited Apr. 20, 2020);
Why am I seeing ads from an advertiser on Facebook? , FACEBOOK, https://
www.facebook.com/help/794535777607370?helpref=popular_topics (last visited Apr. 20,
2020).
 290. AD SETTINGS, GOOGLE, supra note 289.
 291. Users can opt-out of personalized advertisements, but generic ads are still shown.
 292. Why am I seeing ads from an advertiser on Facebook? , supra note 289. On why this
transparency tool is not sufficient, see Athanasios Andreou, Giridhari Venkatadri, Oana Goga,
Krishna P. Gummadi, Patrick Loiseau & Alan Mislove, Investigating Ad Transparency Mechanisms
in Social Media: A Case Study of Facebook’s Explanations, in NETWORK & DISTRIBUTED SYS. SEC.
SYMP. 2018 1 (2018), https:// www.ndss-symposium.org/wp-content/uploads/2018/02
/ndss2018_10-1_Andreou_paper.pdf.
 293. Boerman, Kruikemeier & Zuiderveen Borgesius, supra note 2, at 367; Pedro Giovanni
Leon, Justin Cranshaw, Lorrie Faith Cranor, Jim Graves, Manoj Hastak, Blase Ur & Guzi Xu,
What Do Online Behavioral Advertising Privacy Disclosures Communicate to Users?, in PROC. 2012 ACM
WORKSHOP ON PRIV. ELEC. SOC’Y 19, 12 (2012).

422 BERKELEY TECHNOLOGY LAW JOURNAL [Vol. 35:367

increase transparency and accountability in OBA, they must provide
information necessary for users to assess whether their privacy has been
respected, as well as whether discrimination has occurred, for instance, due to
sensitive information being illegally used or inferred.
NGOs and activist groups routinely criticize current industry standards
and practices along these lines. Numerous complaints have recently been
submitted pushing for greater clarity on the legal and ethical acceptability of
inferential analytics in OBA.294
The path forward to prevent harmful and illegal OBA must cente r on
algorithmic accountability. A transparent business approach can also be
beneficial for the business interests of companies. Users value transparency295
and feel vulnerable if they see ads that are based on previous online activities.296
Following this, Guda Van Noort et al. suggest informing users immediately
that an ad has been shown because of their surfing behavior.297 Research shows
that users do not want to be tracked and find OBA to be privacy invasive.298
Prior research found that “highly personalized advertisements” decreased

 294. See, e.g., Privacy International Files Complaints Against Seven Companies for Wide -Scale and
Systematic Infringements of Data Protection Law , PRIV. INT’L, https:// privacyinternational.org
/press-release/2424/privacy-international-files-complaints-against-seven-companies-wide
-scale-and (last visited Mar. 4, 2019); Our Complaints Against Acxiom, Criteo, Equifax, Experian,
Oracle, Quantcast, Tapad , PRIV. INT’L, http s://privacyinternational.org/advocacy-briefing
/2426/our-complaints-against-acxiom-criteo-equifax-experian-oracle-quantcast-tapad (last
visited Mar. 4, 2019); Johnny Ryan, Regulatory Complaint Concerning Massive, Web-Wide Data Breach
by Google and Othe r “Ad Tech” Companies Under Europe’s GDPR , BRAVE BROWSER (2018),
https://www.brave.com/blog/adtech-data-breach-complaint/ (last visited Mar. 4, 2019); PI
Joins Open Letter to Facebook Regarding Ads Transparency, PRIV. INT’L, https://privacyinternational
.org/advocacy-briefing/2734/pi-joins-open-letter-facebook-regarding-ads-transparency (last
visited May 11, 2019); Why Am I Seeing This on Facebook? It’s Still Unclear , PRIV. INT’L,
https://web.archive.org/web/20190531171839/https://privacyinternational.org/news/277
2/why-am-i-seeing-facebook-its-still-unclear (last visited May 11, 2019); Update report into adtech
and real time bidding, 20 June 2019 , INFO. COMM’N’S OFF. 31, https:// ico.org.uk/media
/about-the-ico/documents/2615156/adtech-real-time-bidding-report-201906.pdf (last
visited Apr. 20, 2020) (stating that real time bidding is incompatible with the GDPR).
 295. Chris Jay Hoofnagle, Jennifer M. Urban & Su Li, Privacy and Modern Advertising: Most
US Internet Users Want “Do Not Track” to Stop Collection of Data About Their Online Activities , in
AMSTERDAM PRIV. CONF. 2012, 1, 11– 12 (2012); Boerman, Kruikemeier & Zuiderveen
Borgesius, supra note 2, at 367.
 296. Elizabeth Aguirre, Dominik Mahr, Dhruv Grewal, Ko de Ruyter & Martin Wetzels,
Unraveling the Personalization Paradox: The Effect of Information Collection and Trust-Building Strategies
on Online Advertisement Effectiveness, 91 J. RETAILING 34, 34 (2015).
 297. Guda Van Noort, Edith G. Smit & Hilde AM Voorveld, The Online Behavioural
Advertising Icon: Two User Studies, 4 ADVANCES ADVERT. RES. 365, 366 (2013).
 298. See Smit, Van Noort & Voorveld, supra note 2, at 16; Boerman, Kruikemeier &
Zuiderveen Borgesius, supra note 2, at 372.

2020] AFFINITY PROFILING AND OBA 423

clickthrough rates 299 while greater transparency had the opposite effect .300
More transparent business models in OBA can therefore benefit users,
platform providers, and advertisers, simultaneously.
C. OPEN PROBLEMS
As shown in this Article, OBA raises at least three areas of concern where
the law might be insufficient: privacy, non- discrimination, and group privacy
protection. Part II demonstrated how the concept of affinity profiling  is
deployed; grouping people according to their assumed interests rather than
solely on their personal traits (e.g. , ethnicity or sexual orientation) . It also
discussed the court’s and scholars’ views on the need to meet the threshold of
intentionality and reliability to turn personal data into sensitive data. Finally, it
also showed how this threshold might render Art icle 9 of the GDPR
inapplicable. Part III examined the scope of E.U. non-discrimination law and
discussed its problematic limitations in terms of the areas  to which it applies
(i.e., only employment, welfare, and goods and services including housing) and
the people it protects (i.e., lawful discrimination based on gender in media and
advertisements, and protection against discrimination based on religion,
disability, age and sexual orientation only in relation to employment).
Then, Part IV proposed the concept of discrimination by association to
challenge the idea that assumed interests and personal traits are strictly
unrelated, which potentially could render regulation inapplicable.
Discrimination by association establishes a basis for more effective protection
against discriminatory OBA by providing a possible path to close some of the
current accountability gaps in affinity profiling, regardless of whether the
practice is considered to use explicitly protected traits or accepted proxies.
In assessing the utility of discrimination by association as a legal concept,
the first question to address is whether affinity profiling should be seen as a
direct use of protected traits because of its close connection or strong
correlation between affinity profiles and those protected traits. If this question
is answered in the affirmative, affinity profiling may constitute direct
discrimination. However, arguing that only an affinity with the protected
category, for example ethnicity, is assumed but no actual ethnicity is inferred
could render regulation inapplicable.

 299. Aguirre et al., supra note 296, at 34–37; see also Boerman, Kruikemeier & Zuiderveen
Borgesius, supra note 2, at 365 ; see generally  Frederik J. Zuiderveen Borgesius, Sanne
Kruikemeier, Sophie C. Boerman & Natali Helberger, Tracking Walls, Take -It-Or-Leave-It
Choices, the GDPR, and the ePrivacy Regulation, 3 EUR. DATA PROT. L. REV. 353 (2017) (providing
empirical evidence that customers reject highly personalized advertisements).
 300. Boerman, Kruikemeier & Zuiderveen Borgesius, supra note 2, at 369.

424 BERKELEY TECHNOLOGY LAW JOURNAL [Vol. 35:367

This gap can be closed by using the conce pt of discrimination by
association. As illustrated in Coleman, discrimination by association allows
individuals to bring a claim if they suffer discriminatory negative effects from
a measure taken against a protected group, even if they are not a member of
that protected group. Discrimination by association grants protection if
someone is treated significantly worse based on their relationship or
association (e.g., affinity for African- American culture) with a group that
possesses a protected attribute. As a result, it would not matter whether the
person is part of the protected group or if the taken measure is based on a
protected attribute they actually possess. Due to the strong correlation and
disclosive power of one’s interests and one’s sensitive traits (e.g., affinity for
African-American culture and being African- American), this concept could
grant more protection against undesired and unlawful discrimination based on
interests or, by extension or proxy, on sensitive traits.
Discrimination by association is a powerful tool to close some of the
current accountability gaps in OBA. People who d o not possess protected
traits (e.g., misclassified users) can bring a claim, which can help combat
discrimination on a larger scale. Widening the circle of potential claimants
could also strengthen the relationship between allies of civil rights movements
(e.g., LGBTQ+, religious, women’s). Moreover, not granting protection to
misclassified users could have an undesirable chilling effect due to fear of
potential negative consequences based on associating with these groups.
Following this logic, members of the group also should not need to prove
that they are a member of this group. This can help combat potential public
stigmatization based on protected attributes. Intent does not need to be
proven on the side of the alleged offender and no concrete victim needs to be
identified, meaning the discriminatory practice does not need to be effective
to be considered discriminatory (e.g., preventing women from applying for
jobs) for prima facie discrimination. Of course, claims of discrimination will
only be successful if they can show that there was no justification for
differential treatment. However, only a very limited number of cases will be
justified because direct discrimination is only lawful if a legitimate basis exists
in a non-discrimination directive or Member State law.
If affinity profiling is ultimately seen as not involving direct usage of
protected traits because the interest groups are seen as sufficiently distinct
from protected categories such as “race” and “ethnicity” as described in the
Directives, claims based on direct discrimination could not be made. However,
under these conditions, affinity profiling could still constitute indirect
discrimination or indirect discrimination by association if this practice
disproportionately negatively  affects a protected group in comparison to

2020] AFFINITY PROFILING AND OBA 425

others in a similar situation. Thus, if this practice disproportionately adversely
affects a protected group, it could be  illegal ( e.g., differential pricing or
complete exclusion from certain ads), unless there is a justification for the
adverse action. Here, again, the concept of discrimination by association would
allow people who are not part of this group to bring a claim, while people who
are part of the group would not need to “out” themselves. And again, the
claimant does not need to establish the offender’s intent. The law might
therefore already have a solution to advertising based on correlations of user
interests that leads to discriminatory differential results.
In CHEZ, the ECJ also left open the question of whether or not the meter
installations in an unreachable height constitutes direct or indirect
discrimination by association. 301 This means that the boundaries between
actions and practices that constitute direct or indirect discrimination are fluid.
The decision to show certain ads based on assumed affinities could fall under
either category with almost no legal justification for the former.
Nonetheless, claimants may face difficulties proving that discrimination
occurred. To prove indirect discrimination, the claimant would need to find a
comparison group that is treated favorably, and then show that, in comparison
with others, a sufficiently large proportion of a protected group was subject to
a particular disadvantage (i.e., does the ephemeral nature of OBA make it less
harmful?). Unfortunately, as shown in Section IV.B.1, standards of what
constitutes a particular disadvantage are not coherent in E.U. case law ,
although the ECJ has clarified that the threshold should not be set too high
because the explicit goal of the directives is to combat illegal discrimination.302
This means an indication of less favorable treatment in advertising could be
seen in differential pricing or exclusion from goods and services for certain
groups. Finally, the claimant would need to show that the particular
disadvantage affected the protected group in a disproportionately negative way
when compared with others in a similar situation. Unfortu nately, the
jurisprudence, as shown in Section IV.B.2, is somewhat inconsistent and does
not provide a clear threshold of legally acceptable disparity (e.g., must affect a
“far greater number of women”303), usually 80–90%. It remains open whether
this threshold is socially acceptable.
Other practical and procedural challenges remain. More algorithmic
transparency is urgently needed. As mentioned above, to be successful, the
claimant will need to show that the “apparently neutral provision, criterion or

 301. CHEZ, supra note 16, at ¶ 129(4).
 302. See supra Section IV.B.1.
 303. EUR. UNION AGENCY FOR FUNDAMENTAL RIGHTS & COUNCIL OF EUR., supra note
98, at 242–43.

426 BERKELEY TECHNOLOGY LAW JOURNAL [Vol. 35:367

practice”304 caused a particular disadvantage and affected a protected group
disproportionately negatively when compared with others. The lack of
transparency in algorithmic decision- making and business practices in OBA
will make this a difficult task. In the same vein lies the difficulty of identifying
other members of a targeted audience, which is crucial because the claimant
will also need to prove that the differential results affected the protected group
disproportionately and identify a comparator that rec eived more favorable
treatment. Not knowing the rules, assumed interests, or attributes on which
one is profiled, and whether these assumed interests correlate with protected
attributes (i.e., not knowing if the interest group correlates with protected traits
and to what extent)305 adds further complexity to this task.
Thankfully, there is a vivid field of research dedicated to bias and fairness
in machine learning that helps to shed light on proxy data and the extent to
which it affects certain groups.306 The importance of this research field cannot
be overstated: it can help establish prima facie discrimination (e.g., post codes
and the subsequent regulation/ban of redlining),307 which is sufficient to shift
the burden of proof from claimants to the accused.
As shown in Section IV.C, alleged offenders can still show that indirect
discrimination was justified by establishing a legitimate aim, necessity , and
proportionality. Howeve r, purely economic reasons alone are unlikely to
qualify as a legitimate aim to justify a discriminatory (business) practice.
Moreover, even if a legitimate aim was pursued and the means were necessary,
the proportionality test could still fail if a practi ce is seen as “offensive or
stigmatising” and therefore deemed disproportionate.308

 304. Supra note 14.
 305. On the challenge to detect proxy data, see generally Kusner et al., supra note 58. On
legal and technical challenges, see generally Indrė Žliobaitė, Measuring Discrimination in
Algorithmic Decision Making, 31 DATA MINING & KNOWLEDGE DISCOVERY 1060 (2017). On
the need to collect sensitive data to avoid discrimination, see generally Ignacio N. Cofone,
Algorithmic Discrimination Is an Information Problem, 70 HASTINGS L.J. 1389 (2019).
 306. To name a few see Kusner et al., supra note 60; Russell et al., supra note 60; Dwork
et al., supra note 60; Friedler, Scheidegger, and Venkatasubramanian, supra note 60; Grgic -
Hlaca et al., supra note 60; Celis, Mehrotra, and Vishnoi, supra note 47; Speicher et al., supra
note 57.; Meike Zehlike, Philipp Hacker & Emil Wiedemann, Matching code and law: achieving
algorithmic fairness with optimal transport, 34 DATA MINING & KNOWLEDGE DISCOVERY 163
(2020).
 307. For examples in Germany see Wachter and Mittelstadt, supra note 25 at at 587.; for
examples from the United States, see generally Willy E. Rice, Race, Gender, Redlining, and the
Discriminatory Access to Loans, Credit, and Insurance: An Historical and Empirical Analysis of Consumers
Who Sued Lenders and Insurers in Federal and State Courts, 1950-1995, 33 SAN DIEGO L. REV. 583
(1996).
 308. CHEZ, supra note 16, at ¶ 128.

2020] AFFINITY PROFILING AND OBA 427

Moreover, Part V and Section VI.A showed that there is a clear need to
afford greater protection to the privacy interests of the groups formed by
modern inferential analytics and targeted by OBA. The challenge is that the
analytics behind many automated decision- making and profiling is not
concerned with singling out or identifying a unique individual, but rather with
drawing inferences from large datasets, calculating probabilities, and learning
about types or groups of people.309 Third-party, anonymized, or non-personal
data can be used for these purposes. Unfortunately, data protection law only
applies to the personal data of identifiable individuals. Therefore, new legal
mechanisms based on group or collective privacy interests may be necessary
to close the accountability gap created by data-driven OBA at scale.310 Profiling
and inferential analytics expand the circle of victims to include groups that may
not qualify for protection under non-discrimination because they do not map
on to traditional social concepts of protected traits (e.g., “sad teens”311 or video
gamers).312
Finally, current public and private sector governance tools discussed in
Sections VI.B and VI.C are welcome and encouraged, but leave much to be
desired. Platform providers currently offer generic and vague explanations of
why certain advertisements have been served. These types of explanations do
not alleviate the aforementioned concerns. Without g reater algorithmic and
business transparency in OBA, it will remain very difficult for individuals,
regulators, or NGOs to prove that one of privacy violations, differential
treatments, or differential results have occurred.
However, explanations of how ad vertisements are served based upon
assumed interests and sensitive characteristics can, if well formulated, provide
an effective tool to contest discriminatory advertisements, and thus increase
accountability in algorithmic profiling and decision-making.
D. POLICY RECOMMENDATIONS
The following types of information and explanations should be provided
to individuals by system or platform controllers when behavioral
advertisements are served:

 309. Mittelstadt, supra note 23, at 476–78.
 310. Leading thinkers on collective privacy interests include BYGRAVE, supra note 263;
Mittelstadt, supra note 23; Mantelero, Personal Data, supra note 245; GROUP PRIVACY: NEW
CHALLENGES OF DATA TECH., supra note 263.
 311. Reilly, supra note 250.
 312. Being labelled as a video gamer can cause the Chinese Social Credit Score to drop.
See Kobie, supra note 252.

428 BERKELEY TECHNOLOGY LAW JOURNAL [Vol. 35:367

1. Information that demonstrates that sensitive data and protected
attributes have not been unlawfully used. Giving data subjects direct
access (e.g., via Article 15 of the GDPR) to examine the data currently
processed about them, as well as easy mechanisms to opt -out or
withdraw consent for OBA, are similarly encouraged.
2. Information that provides individuals with a better understanding of
what assumptions, predictions, or inferences are currently drawn about
them. The current transparency efforts of tech companies, while an
encouraging first step, are not sufficient. To bette r align explanations
with the right to privacy and identity, users require better information
about how they are “seen” by platforms and advertisers.313
In addition, the following modifications to public policy and business
strategies should be made to improve the broader regulatory environment:
3. System or platform controllers should not use the argument that
affinity profiling does not use , collect, or infer sensitive or protected
attributes in order to avoid GDPR and non- discrimination law.
Regulators and the judiciary should likewise reject any such argument.
Even if affinity profiling is legally classified as involving sensitive
information, companies should also not solely rely on consent to
justify such processing. Companies should acknowledge that consent,
as proposed in GDPR, is not always a reliable method to gauge user
interests and preferences because most users do not read, and often do
not understand, the terms and conditions of digital services.
Companies should consider how to adopt ethical data analytics (e.g., a
right to reasonable inferences for users  (see Section A of this
Article)),314 sharing practices, and business relationships 315 (e.g.,

 313. On the need for governance of inferential analytics, see Wachter & Mittelstadt, supra
note 39, at 499.
 314. Id.
 315. Sandra Wachter, The GDPR and the Internet of Things: A Three -Step Transparency Model,
10 L., INNOVATION & TECH. 266, 278, 283–84, 292 (2018).

2020] AFFINITY PROFILING AND OBA 429

fiduciary duties316 or duty of care317), and make information regarding
these practices publicly available.
4. European regulators and policymakers should work t o close relevant
loopholes in current E.U. non-discrimination law. As shown in this
Article, non-discrimination law is not comprehensive. However, it is
clear that differential treatment and results , for example , based on
religion or belief, disability, ag e, sexual orientation, ethnicity, and
gender, should be avoided. Further, regulators, scholars, civil society
organizations, policymakers, and industries should create guidelines
for ethical business relations with partner companies to avoid
unethical, stigmatizing and offensive advertisements. A public
commitment to protect diversity (e.g., refraining from the use of
certain sensitive data groups) in a holistic way is encouraged.
5. System controllers should undertake s ystematic and periodical bias
testing to avoid unintentional discrimination. Bias testing is necessary
to ensure that ad targeting systems are fair. As affinity profiling is based
on the interests of user groups, it may be difficult to see that certain
interests correlate with protected attributes. For example, postcodes
can be strong proxies for religious belief or ethnicity. Therefore,
internal structures that audit and test for bias need to be implemented.
Collecting a list of known proxies and approaches to either avoid the
usage of or to mitigate the risks associated with them could be made
public.318 Post codes319 and redlining320 regulations are a good example.
6. System controllers, regulators, and funding agencies should provide
support for independent research or “white hat hacking” to determine

 316. TAP Staff Blogger, Jonathan Zittrain and Jack Balkin Propose Information Fiduciaries to
Protect Individual Privacy Rights , TECH. ACAD. POL’Y, https:// www.techpolicy.com/Blog
/September-2018/Jonathan-Zittrain-and-Jack-Balkin-Propose-Informat.aspx (last visited
Feb. 2, 2019) [https:// perma.cc/6AH6-EVG6]; see generally Jack M. Balkin, Information
Fiduciaries and the First Amendment, 49 U.C. DAVIS L. REV. 1183 (2015).
 317. Lorna Woods & William P errin, An Updated Proposal by Professor Lorna Woods and
William Perrin , CARNEGIEUK TRUST, https:// www.carnegieuktrust.org.uk/blog/internet
-harm-reduction-a-proposal/ (last visited May 11, 2019).
 318. Similarly, Dalenberg proposes blacklists. See Dalenberg, supra note 174, at 625.
 319. Wachter & Mittelstadt, supra note 39, at 587.
 320. On the history of redlining, see generally Willy E. Rice, Race, Gender, Redlining, and the
Discriminatory Access to Loans, Credit, and Insurance: An Historical and Empirical Analysis of Consumers
Who Sued Lenders and Insurers in Federal and State Courts, 1950-1995, 33 SAN DIEGO L. REV. 583
(1996).

430 BERKELEY TECHNOLOGY LAW JOURNAL [Vol. 35:367

when, how, and to what extent certain groups are affected by affinity
profiling. Due to the lack of algorithmic transparency, prima facie
discrimination might be hard to prove. The claimant needs to show
that they suffered a particular disadvantage and must demonstrate that
a protected group is treated significantly worse (i n comparison to
others in a similar situation) for the burden of proof to shift. Therefore,
more statistical evidence via independent research could help
businesses to demonstrate that they are not discriminatory. Future
policy discourse also needs to address whether the 80 –90%
threshold321 for legally acceptable disparity is normatively acceptable.
7. Regulators, policymakers, and system controllers should acknowledge
group-level privacy rights. Current profiling and inferential analytics
are not sufficiently addressed in data protection and non-
discrimination law. The former lacks teeth because profiling can also
occur without identifying an individual and sometimes even without
using personal data,322 while the latter fails because the created groups
do not map on to the protected groups in discrimination law. 323
Therefore, a holistic privacy protection approach, as well as safeguards
for people outside of these narrowly defined groups in non-
discrimination law (e.g., a right to reasonable inferences),324 should be
pursued.
OBA and affinity profiling pose novel privacy, non-discrimination, and
group privacy interests. Thankfully, it appears that E.U. non-discrimination
law provides a powerful tool in discrimination by association to mitigate some
of these risks. If the concept of discrimination by association is combined with
robust transparency standards to explain how advertisements are served based
on assumed interests and sensitive characteristics, the combination will greatly
improve protection against pervasive online advertising practices.

 321. See supra Section IV.B.2.
 322. Wachter, supra note 21, at 7.
 323. Mantelero, Personal Data, supra note 245, at 240.
 324. Wachter & Mittelstadt, supra note 39, at 500.
