---
title: Where can AI be used? Insights from a deep ontology of work activities
url: https://arxiv.org/abs/2603.20619
category: digital-marketing
subcategory: empirical
date: 2026-03
venue: ''
authors:
- Alice Cai
- Iman YeckehZaare
- Shuo Sun
- Vasiliki Charisi
- Xinru Wang
source: arxiv
pdf_url: https://arxiv.org/pdf/2603.20619
pages: 120
chars: 579482
fetched_at: '2026-11-08T13:01:35+00:00'
kb_version: 1
---

# Where can AI be used? Insights from a deep ontology of work activities

Where can AI be used?
Insights from a deep ontology of work activities
Alice Cai1,2†, Iman YeckehZaare1,2†, Shuo Sun1,3†,
Vasiliki Charisi1,3†, Xinru Wang1,3, Aiman Imran1,2,
Robert Laubacher1,2, Alok Prakash1,3, Thomas W. Malone1,2*
1*Center for Collective Intelligence, Massachusetts Institute of
Technology, 100 Main Street, Cambridge, 02142, Massachusetts, USA.
2Sloan School of Management, Massachusetts Institute of Technology,
100 Main Street, Cambridge, 02142, Massachusetts, USA.
3*Mens, Manus, and Machina, Singapore-MIT Alliance for Research
and Technology, 1 CREATE Way, Singapore, 138602, Singapore.
*Corresponding author(s). E-mail(s): malone@mit.edu;
Contributing authors: cai@mit.edu; oneman@mit.edu;
shuo.sun@smart.mit.edu; vasiliki.charisi@smart.mit.edu;
xinru.wang@smart.mit.edu; aimanim@mit.edu; rjl@mit.edu;
alok.prakash@smart.mit.edu;
†These authors contributed equally to this work.
Abstract
Artificial intelligence (AI) is poised to profoundly reshape how work is executed
and organized, but we do not yet have deep frameworks for understanding where
AI can be used. Here we provide a comprehensive ontology of work activities
that can help systematically analyze and predict uses of AI. To do this, we dis-
aggregate and then substantially reorganize the approximately 20K activities in
the US Department of Labor’s widely used O*NET occupational database. Next,
we use this framework to classify descriptions of 13,275 AI software applications
and a worldwide tally of 20.8 million robotic systems. Finally, we use the data
about both these kinds of AI to generate graphical displays of how the estimated
units and market values of all worldwide AI systems used today are distributed
across the work activities that these systems help perform. We find a highly
uneven distribution of AI market value across activities, with the top 1.6% of
activities accounting for over 60% of AI market value. Most of the market value
is used in information-based activities (72%), especially creating information
1
arXiv:2603.20619v1  [cs.AI]  21 Mar 2026

(36%), and only 12% is used in physical activities. Interactive activities include
both information-based and physical activities and account for 48% of AI mar-
ket value, much of which (26%) involves transferring information. These results
can be viewed as rough predictions of theAI applicabilityfor all the different
work activities down to very low levels of detail. Thus, we believe this systematic
framework can help predict at a detailed level where today’s AI systems can and
cannot be used and how future AI capabilities may change this.
Keywords:ontology, work, task taxonomy, AI applications, robotics, O*NET,
knowledge graph
1 Introduction
Many people today believe that AI will lead to vast changes—either positive or nega-
tive—in the ways work is done. But to think systematically about these issues, one of
the most basic questions is:Where can AI be used?Where, for example, is it both tech-
nically and economically feasible to use AI for performing specific work tasks today?
And how might these answers change in the future?
A common way for researchers to answer questions like these is by systematically
identifying work activities and then considering which of these activities can be done
by AI (see [1–4] and Appendix A). For example, much of this research uses the work
activities identified in O*NET [5], the U.S. Department of Labor’s comprehensive
occupational database. This database contains detailed descriptions of approximately
20,000 activities from over 900 occupations in the U.S. economy.
Although O*NET is very comprehensive and has been widely used to help job
seekers find suitable jobs, it has limitations as a conceptual tool for analyzing where
AI can be used. For example, due to the compound nature of its basic tasks, it is
often difficult to determine which element of a compound task is relevant in a specific
situation.
To help address these problems, we created an early version of adeep ontology of
work activities. Bywork activities, we mean activities like those commonly performed
by human workers, and now, increasingly, also by computers, robots, and other types
of machines. Byontology, we mean a formal specification of the key types of entities in
a subject area and their properties and relationships (see [6–9] and Section 6.1). And
bydeep, we mean that the structure of the ontology includes multi-leveled “family
trees” of entities that have deep similarities with each other.
To create an ontology with these properties, we started with all the O*NET tasks,
disaggregated them into what we callatomic activities, and created more abstract
generic activitiesas needed to arrange the atomic activities into family trees of sim-
ilar activities. Our current version of this ontology contains 39,603 total activities,
including 1,113 generic activities, 15,989 atomic activities, and 20,950 original O*NET
tasks.
To use this ontology as a framework for understanding where AI can be used, we
acquired two large datasets about AI uses: (1) a database with descriptions of 13,275
2

AI software applications collected on a website called “There’s an AI for That ®”
(TAAFT) [10], and (2) data on 20.8 million robots of different types as reported by
the International Federation of Robotics (IFR) [11, 12].
We then classified all of these AI systems into the activities in our ontology that
they performed or helped perform. Next, we created graphical displays of the intensity
of AI usage in each activity. We interpreted this intensity of usage as an indicator of
theAI applicabilityfor each activity. And, finally, using the concept ofinheritance
that is common in ontologies, we assumed that the AI applicability of an activity was
often “inherited” by its more specialized descendants in the same branch of the family
tree, potentially all the way down to very detailed activities.
This, then, provides a systematic way of predicting—at a detailed level—where AI
can be used. The data we already have in the ontology can be used to help predict
uses that are possible today. And by hypothesizing future changes in AI applicability
for abstract activities, the ontology can also be used to predict possible AI uses in the
future.
2 Results
2.1 A deep ontology of work activities
Using the methods for automated classification and human editing described in
Sections 6.1 to 6.3, our first result was a comprehensive ontology of work activities
including approximately 40,000 total activities. These activities are arranged in a hier-
archy with a median depth of 9 levels, and Figure 1 shows a sample of how the different
types of activities are organized.
At the far left is the most general type of activity of all, “Act,” followed by a
collectionof more specialized (“child”) activities that are all answers to the question
“Act on what?” These three generic activities and their nicknames are: “Act on infor-
mation (‘Think’),” “Act on physical objects (‘Do’),” and “Act with other activities or
actors (‘Interact’).”
Indented beneath these three major categories of activities are further specializa-
tions (“children”) of each. For example, “Act on information” has children such as
“Create information,” “Modify information,” and “Transfer information.” To the right
is an expansion of one of these activities, “Create information,” showing further chil-
dren and collections. At the next to last level of the hierarchy are theatomic activities,
which include both verbs and objects in their names. Finally, at the far right are the
compound O*NET tasks in which these atomic activities are included. The O*NET
tasks, however, are notchildrenof the atomic activities; they are just the places in
O*NET where the atomic activities are used.
Inheritance of AI applicability
As noted above, our ontology takes advantage of the concept of inheritance. This
concept formalizes the common sense notion that if something is true of one kind of
object, it is usually true of more specialized types of that kind of object. For example,
the things that are true of mammals are true of dogs, and the things that are true of
dogs are true of Dalmatian puppies.
3

Fig. 1:Excerpt of the ontology structure.(a) The top 4 levels of the ontology, (b)
a sample of the next 5 levels beneath “Create information,” including generic activities,
such as “Decide” and “Select,” and leading all the way down to atomic activities,
such as “Select method.” At the last level are O*NET tasks, such as “Select banding
methods to permit identification of chromosome pairs.” Collections are groupings of
specializations that often differ on a dimension such as “Decide how?” or “Decide
what?”
In our case, we focus on inheriting the property ofAI applicability, that is, whether
an activity can be performed using AI. And we hypothesize that if an activity can
be performed using AI, then the more specialized types of that activity (its “descen-
dants”) can probably also be performed using AI. Figure 2 illustrates this principle
with a stylized example in which AI applicability is shown as high for the descendants
of “Act on information” and low for the descendants of “Act on physical objects.”
This means that if we discover that AI is applicable to a parent activity (e.g.,
“Write”), we have principled grounds for hypothesizing that it may be applicable to
the child activities (e.g., “Write report,” “Write email”) even before verifying this
empirically.
Of course, this is not always true, and the concept of inheritance also allows the
value of a property to beoverriddenat any point in the hierarchy. In this case, the
new value that overrides an inherited value is inherited by further descendants below
that point. For instance, even though most mammals reproduce by live birth, duck-
billed platypuses lay eggs. In the same way, even though AI is highly applicable to the
activity of writing, there are some types of writing (such as writing deeply personal
love letters) where it would be much less applicable.
The concept of inheritance also means that one way to estimate the AI applica-
bility of an abstract activity is to assume that if most of its descendants have high
AI applicability, then it probably does, too. In most of the results below, we take
4

Fig. 2:Demonstration ofinheritanceof the propertyAI Applicability.This
stylized example illustrates how different values of the property of “AI applicability”
can be inherited down different branches of the ontology from very abstract types of
activity like “Create information” to very specific activities like “Write grant applica-
tion for research projects.”
advantage of this assumption by estimating the AI applicability of an activity as the
sum of both (a) thedirectuses of AI systems in performing the activity, and (b) the
aggregateduses of AI in all the descendants of the activity.
2.2 AI software applications
To use this ontology in understanding where AI can be used, we first obtained a
database with descriptions of 13,275 AI software applications collected on a website
called “There’s an AI for That®” (TAAFT) [10]. These applications span a wide range
of tasks, from text generation and data analysis to image generation and workflows
(see Section 6.4.1). Then, using an automated classification pipeline (Section 6.5.1),
we classified each application into the most specific ontology activity that included
that application’s primary activity.
2.2.1 Where are AI software applications used today?
The resulting distribution of AI software applications is shown in the sunburst diagram
in Figure 3. Instead of the outline format shown in Figure 1, this diagram shows “Act,”
at the center, and successive outer rings correspond to increasingly specialized types
5

Act: 100%
Act on information
(“Think”): 92%
Act with other activities and actors (“Interact”): 32% Act on physical objects (“Do”): 0%
Create
information: 58%
Modify
information: 14%
Transfer
information: 22%
Storeinformation: 0.05%
Transfer between
actors: 30%
Act onactivities: 4%
Modify physicalobjects: 0%
Create physicalobjects: 0%
Store physical
objects: 0%
Transfer physical
objects: 0%
Plan: 4%
Analyze: 7%
Decide: 2% Calculate: 0.2% Express information: 24% Assemble information: 1% Reason: 0.8% Create information -- other: 18% Solve: 0.4%
Transform information: 13% Com bine inform
ation: 0.7%
Separate information: 0.9% Move information: 0.05%Exchange information: 5%
Get information: 7%Provide information: 8% Communicate (transfer information end-to-end): 2% Store information -- other: 0.05% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 0.5%
Buy: 0.4%
Distribute: 0.008%
Sell: 0.1%
Give: 0.02%
Take: 0%
Transfer information: 22%
Transfer service: 7%
Transfer physical objects: 0%
Interact: 0%
Open (make available): 0%
Receive: 0.008%
Return: 0%
Trade (Transfer both ways): 0.008%
Communicate (transfer information end-to-end): 2%
Earn: 0% Lend: 0% Pass (over): 0.06% Raise (funds): 0.03% W ithhold: 0%
Perform
 (action): 2%
Improve: 2%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0.1% Pass (achieve): 0% Undertake: 0% Transform physical objects: 0%
Separate physical objects: 0%
Combine physical objects: 0%
Move physical objects: 0%
Assemble: 0%
Fabricate: 0%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 0%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 1%
Outline: 0%
Plan -- other: 2%
Propose: 0.4%
 Schedule: 0.3%
Stage: 0%
 Analyze -- other: 4%
Characterize: 0%
 Correlate: 0%
 Determine: 0.9%
 Experiment: 0%
 Investigate: 1%
 Trace (analytically): 0%
 Accept: 0%
Decide -- other: 0.008%
 Estimate: 0.08%
 Reject: 0%
 Rule: 0.02%
 Select: 2%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0.1%
Count: 0.02%
 Estimate: 0.08%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0.3%
 Record: 24%
Assemble information -- other: 0.03%
Configure (information): 0.08%
 Construct (information): 1%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0.02%
Organize (analytically): 0.7%
 Reason -- other: 0.05%
 Create (Activity): 0.8%
 Create (Actor): 0%
Create (Information): 17%
 Address (solve): 0%
 Resolve: 0.08%
Solve -- other: 0.3%
Adjust (information): 1%
 Change Appearance: 0%
 Clean (inform
ation): 0.05%
 Decode: 0%
Encode: 0.008%
 Equalize: 0%
Fill (inform
ation): 0.1%
Finish (inform
ation): 0%
Im
prove: 2%
Organize (analytically): 0.7%
 Perm
ute: 0%
Prepare (inform
ation): 0.3%
Process (inform
ation): 1%
Renew (inform
ation): 0%
Revise: 5%
 Service (inform
ation): 0.4%
Switch: 0%
 Transform
 inform
ation -- other: 0.3%
Translate: 1%
 Use: 0.4%
 Add (inform
ation): 0.02%
Com
bine inform
ation -- other: 0.008%
Connect (inform
ation): 0.05%
Gather (inform
ation): 0.4%
Incorporate (inform
ation): 0.2%
Pack (together) (information): 0%
 Synthesize (information): 0.05%
 Break (into components): 0%
 Cut (information): 0.7%
 Disconnect (information): 0%
 Remove (information): 0.02%
Separate information -- other: 0.2%
 Move information -- other: 0%
 Put information: 0.05%
Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0.008%
 Converse: 1%
 Correspond: 0.008%
 Debate: 0.04%
 Exchange information -- other: 0.05%
 Interview: 0.2%
 Mediate: 0%
 Meet: 0.02%
 Negotiate: 0.02%
 Network: 0.02%
 Reach: 0.03%
 Teach: 3%
 Access: 0.2%
 Download: 0.008%
 Evaluate: 2%
 Gather (information): 0.4%
 Get information -- other: 0.07%
 Import: 0.008%
 Learn: 0.9%
 Perceive: 3%
 Understand: 0.09%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0.3%
 Provide decision: 0%
 Provide money: 0%
 Send information: 8%
 Communicate (transfer information end-to-end) -- other: 0.3%
 Store (Activity): 0%
 Store (Actor): 0.05%
Store (Information): 0.008%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 0.5%
Ticket: 0%
Buy -- other: 0.05%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0.3%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0.008%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0.08%
Sell Service: 0.008%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0.02%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 2%
Exchange information: 5%
Get information: 7%
Provide information: 8%
End service: 0%
Exchange service: 0.1%
Get service: 5%
Provide service: 2%
Exchange physical objects: 0%
Get physical objects: 0%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0.008%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0.3%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0.06%
 Raise (funds) -- other: 0.03%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 1%
 Conduct: 0.3%
 M
ake: 0%
Perform
 (action) -- other: 0.09%
Practice: 0.008%
 Rehearse: 0.2%
 Run (perform
): 0%
Im
prove -- other: 1.0%
Optim
ize: 0.9%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0.08%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0%
Clean (physical): 0%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0%
 Process (physical): 0%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
 Cut (physical): 0%
 Disassemble: 0%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0%
 Consolidate: 0%
 Cover: 0%
Enclose: 0%
Gather (physical): 0%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0%
Reorient physical objects: 0%
Transport physical objects: 0%
 Assemble -- other: 0%
Configure (physical): 0%
Construct (physical): 0%
 Copy (physical): 0%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 0%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0%
Fig. 3:Where are AI software applications used today?Sunburst diagram
illustrating the concentrations of AI software applications across activity types. Color
intensity represents the proportion of AI applications associated with each activity
(including its specializations in the outer rings) relative to the total number of AI
applications in the dataset. We view this as a rough indicator ofAI applicability.
(Percentages in a ring sum to more than 100% when activities are classified in multiple
places, but these double counts are removed at subsequent higher levels.)Note: For
this and all other sunburst diagrams in the paper, readers are encouraged to zoom in
to examine fine-grained specializations.
of activity. For legibility, only the first five levels of the ontology are shown here, but
Appendices F.3 and F.4 show all fourteen levels of the complete ontology.
For each ontology activity, the percentage value shown represents the percentage of
AI applications classified under that activity, including all of its specializations in the
outer rings. The color intensity of each segment reflects this percentage of AI usage,
and we interpret these AI concentrations as a rough indicator of theAI applicability
for each type of activity.
6

The diagram also highlights an important structural feature of the ontology: some
activities have multiple generalizations (or “parents,” see “multiple inheritance” in
Section 6.1.1). For example, the activity “Transfer information” is a child of both
“Think” and “Interact,” so it appears in two locations in the diagram. Both of these
instances are indicated in the diagram by gray dashed outlines (in the lower left and
upper left quadrants). In these cases, the percentage of AI applications in a given ring
may sum to more than 100%, but this double-counting is corrected at the higher levels
where the multiple branches come together. (See Appendix B.7 for more examples).
Is AI software used most for thinking, doing, or interacting?
At the second level of the ontology, all of the AI software applications fall under the
high-level categories “Act on information (‘Think’)” and “Act with other activities and
actors (‘Interact’)”. In contrast,noAI software applications are classified under “Act
on physical objects (‘Do’),” because the TAAFT dataset includes only digital appli-
cations. As we will see, in Sections 2.3 and 2.4, however, robotic systems complement
AI software in this dimension.
An examination of the darkest-shaded regions in Figure 3 indicates that the
vast majority of AI applications (approximately 92%) are concentrated within the
high-level category, “Think.” Within this category, activities related to “Create infor-
mation” constitute the largest share (58%), followed by “Transfer information” (22%,
multiply-inherited), and “Modify information” (14%). Together, these three activity
types dominate the current AI software application landscape, reflecting the central
role of information-related activities in contemporary AI software uses.
The “Interact” category accounts for 32% of AI applications. However, the majority
of this share is attributable to the multiply-inherited activity “Transfer informa-
tion” (22%), which is a specialized type of both “Think” and “Interact.” This
overlap suggests that many interactive AI software applications also heavily feature
information-related processes.
Overall, 92% of applications are mapped to only 6.8% of activities, all of which are
under “Think” in the ontology. This highly skewed distribution suggests that the use
of contemporary AI software tools is very concentrated in only a few types of activities.
This has at least two possible implications. First, it suggests specific places to look for
applications of today’s AI software tools. And, second, it suggests opportunities for
further development of new types of AI software for the activities thataren ’theavily
populated yet.
In what activities is AI software used most?
Figure 4 shows the individual activities into which the most AI software applications
were classified directly. Several clear patterns emerge in this figure. First, the highest-
ranked activities are overwhelmingly centered on content generation and information
manipulation, such as “Generate image using computer,” “Create content,” “Cre-
ate video,” “Write content,” “Develop application,” “Summarize (Information),” and
“Create recording.” These activities under “Think” account for a substantial fraction
of all AI applications, reflecting the dominant role of generative capabilities in the
current AI ecosystem.
7

7.18%
3.53%
2.69%
2.59%
1.88%
1.79%
1.54%
1.39%
1.19%
1.18%
1.15%
1.11%
1.11%
1.06%
1.01%
0.99%
0.96%
0.96%
0.88%
0.82%
0% 1% 2% 3% 4% 5% 6% 7% 8%
Generate image using computer
Create Content
Create video
Answer Question
Write Content
Develop Application
Summarize (Information)
Communicate (transfer information end-to-end)
Create Recording
Converse
Automate (Activity)
Write Code
Analyze Dataset
Teach Skill
Analyze (Information)
Generate Lead
Build Application
Write Text
Write Copy
Search (Information)
✓
✓
✓
✓✓
✓
✓
✓
✓✓
✓
✓✓
✓
✓
✓
✓✓
✓
✓
✓
✓
✓
✓✓
“Think”“Interact”“Do”
Fig. 4:The 20 activities with the most AI software applications.These 20
activities alone account for more than 35% of all AI software applications.
Beyond pure generation, activities such as “Answer question,” “Communicate,”
“Converse,” and “Teach skill,” also appear prominently. These activities are multi-
ply inherited from both “Think” and “Interact.” Their strong presence indicates that
many widely adopted AI software applications operate at the intersection of informa-
tion processing and interpersonal interaction, rather than within purely informational
or purely social domains. Meanwhile, activities such as “Automate (Activity),” that
are classified only as “Interact” tend to rank lower.
In general, the distribution of AI software applications across activities is highly
skewed. The top 20 activities, representing only about 0.1% of all activities in the
ontology, collectively account for more than 35.0% of all AI software applications.
This pronounced concentration confirms that current AI adoption is dominated by a
small subset of highly tractable and commercially valuable activities, while the vast
majority of potential activities in the ontology remain sparsely populated. As discussed
further in Section 3.1, this highlights substantial opportunities for future expansion
and diversification of AI use.
To investigate in more detail the activities with the highest concentration of AI
software applications, Figure 5 shows a zoomed-in sunburst view of the “Create
information” branch of the ontology, which includes 58% of all AI applications.
8

Create
information: 58%
Express
information: 24%
Decide: 2%
Plan: 4%
Analyze: 7%
Calculate: 0.2%
Assembleinformation: 1%
Reason: 0.8%
Solve: 0.4%
Create information
-- other: 18%
Record: 24%
Express Live: 0.3% Argue: 0%Conclude: 0%Emphasize: 0%
Select: 2%
Estimate: 0.08%
Accept: 0%
 Decide -- other: 0.008%
Reject: 0% Rule: 0.02% Sentence: 0% Design: 1%
Propose: 0.4% Schedule: 0.3% Anticipate: 0% Budget: 0% Conceptualize: 0% Outline: 0%
 Plan -- other: 2% Stage: 0%
Determine: 0.9%
 Analyze -- other: 4% Characterize: 0% Correlate: 0% Experiment: 0% Investigate: 1%
Trace (analytically): 0%
Estimate: 0.08% Account for: 0%
Balance (account): 0%
Calculate -- other: 0.1% Count: 0.02% Total: 0%
Configure (information): 0.08%
Construct (information): 1%
Assemble information -- other: 0.03%
Reassemble (information): 0%
Organize (analytically): 0.7%
Consider: 0%
Develop (idea): 0.02%
Reason -- other: 0.05%
Address (solve): 0%
Resolve: 0.08%
Solve -- other: 0.3%
W
rite: 1
1%
Create static image: 7%
Docum
ent: 1%
M
ark (inform
ation): 0.03%Copy (inform ation): 0.05% Create moving image (w/ or w/o sound): 3% Print: 0% Compose: 0.9% Enroll: 0%
 Record -- other: 0.4%
 Record Sound: 0.2% Talk: 0.1%Act (Perform, e.g. in a play): 0.02% Express using instruments: 0% Sign (signal): 0% Dance: 0%Introduce: 0%Read (out loud): 0.2% Sing: 0%
Argue -- other: 0%Defend (verbally): 0%
Conclude -- other: 0%
Emphasize -- other: 0%
Select holistically: 0%
Validate: 0.3%
Classify: 0.3%
Select by negotiation: 0%
Appoint: 0%
Categorize: 0%
Compare: 0.2%
Diagnose: 0.09%
Dial: 0%
Match (align): 0.2%
Select -- other: 0.6%
Select analytically: 0%
Select by explicit  formulas or rules (human-understandable): 0%
Select randomly: 0%
Select socially (based on what others do): 0%
Vote: 0.008%
Estimate -- other: 0.05%
Price: 0.02% Quote: 0.008%
Reject -- other: 0%
 Rule -- other: 0.02%
 Sentence -- other: 0% Choreograph: 0.008%
 Design -- other: 1% Detail: 0% Engineer: 0% Fram e (com positional): 0% Lay: 0% Lay out: 0% Redesign: 0% Specify: 0.008%Nom inate: 0%
 Propose -- other: 0.3% Book: 0%
 Schedule -- other: 0.2%
 Anticipate -- other: 0%
 Budget -- other: 0%
 Conceptualize -- other: 0%
 Outline -- other: 0%
 Stage -- other: 0%
Determine -- other: 0.09% Identify: 0.6% Predict: 0.2%
Characterize -- other: 0%
 Correlate -- other: 0%
 Experiment -- other: 0% Research: 1%
Trace (analytically) -- other: 0%
Estimate -- other: 0.05% Price: 0.02% Quote: 0.008%
Account for -- other: 0%
Balance (account) -- other: 0%
Count -- other: 0.008%
 Total -- other: 0% Collate: 0%
Configure (information) -- other: 0.08%
Construct (information) -- other: 1%
Reconstruct: 0%
Reassemble (information) -- other: 0%
Organize (analytically) -- other: 0.2%
Reorganize: 0%
Consider -- other: 0%
Develop (idea) -- other: 0.008%
Address (solve) -- other: 0%
Resolve -- other: 0.08%
Enter (information): 0.03%
 Complete (information): 0% Draft: 0.02% Program (computer): 1% Script: 0% Sign (signature): 0.008%
 Write -- other: 9% Draw (drawing): 0.03% Visualize: 0.02%
 Generate image using computer: 7% Paint (information): 0% Photograph: 0.03% Chart: 0%
 Document -- other: 0.4% Enum erate: 0% List: 0% M ap (out): 0% Transcribe (write): 1% Address: 0% Date: 0% Designate: 0%
M
ark (inform
ation) -- other: 0.02%
Stencil: 0%
 Copy (inform
ation) -- other: 0%
Model (represent) (information): 0.05%Trace (drawing) (inform
ation): 0%
Create video: 3% Film: 0% Videotape: 0%
 Print -- other: 0% Reprint: 0%
 Compose -- other: 0.9%
 Enroll -- other: 0%
Address (express): 0.03% Call (out): 0.06% Comment: 0.008% Praise: 0%
 Talk -- other: 0% Tell: 0.008%
 Act (Perform, e.g. in a play) -- other: 0% Impersonate: 0.02% Improvise: 0%
 Express using instruments -- other: 0% Sight-read: 0% Flag: 0%
Sign (signal) -- other: 0%
 Dance -- other: 0%
 Introduce -- other: 0%
 Read (out loud) -- other: 0.02%
 Sing -- other: 0%
Defend (verbally) -- other: 0%
Select based on emotion: 0%
Select based on intuition: 0%
Select by machine learning (or other opaque algorithms): 0%
Authenticate: 0.03%
Qualify: 0.008%
Validate -- other: 0.3%
Catalogue: 0%
Classify -- other: 0.3%
Select by negotiation in buying: 0%
Select by negotiation in selling: 0%
Appoint -- other: 0%
Compare -- other: 0.2%
Diagnose -- other: 0.09%
Dial -- other: 0%
Match (align) -- other: 0.1%
Vote -- other: 0%
Price -- other: 0.02%
Quote -- other: 0%
Choreograph -- other: 0%
Detail -- other: 0%
Engineer -- other: 0%
 Fram
e (com
positional) -- other: 0%
Lay -- other: 0%
 Lay out -- other: 0%
 Redesign -- other: 0%
 Specify -- other: 0.008%
Nom
inate -- other: 0%
Book -- other: 0%
Identify -- other: 0.6%
 Predict -- other: 0.07%
Research -- other: 0.4%
Price -- other: 0.02%
Quote -- other: 0%
Collate -- other: 0%
Reconstruct -- other: 0%
Reorganize -- other: 0%
Input into computer: 0.02%
Credit: 0%Debit: 0%
Enter (information) -- other: 0.008% Post (financial): 0% Re-enter: 0% Tabulate: 0%
Draft -- other: 0.02%
 Program (computer) -- other: 1%
 Script -- other: 0%
 Sign (signature) -- other: 0.008% Delineate: 0%
 Draw (drawing) -- other: 0.02% Shade: 0% Sketch: 0% Diagram: 0.02% Graph: 0%
 Visualize -- other: 0%
 Paint (information) -- other: 0%
 Photograph -- other: 0%
 Chart -- other: 0%
 Enum
erate -- other: 0%
List -- other: 0%
 M
ap (out) -- other: 0%
 Transcribe (write) -- other: 0.2%
 Address -- other: 0%
 Date -- other: 0%
 Designate -- other: 0%
Stencil -- other: 0%
 M
odel (represent) (inform
ation) -- other: 0.05%
Trace (drawing) (inform
ation) -- other: 0%
Film -- other: 0%
 Videotape -- other: 0%
 Reprint -- other: 0%
 Address (express) -- other: 0.03%
Call (out) -- other: 0%
 Comment -- other: 0.008%
 Praise -- other: 0%
 Tell -- other: 0.008%
 Impersonate -- other: 0.02%
 Improvise -- other: 0%
 Sight-read -- other: 0%
 Flag -- other: 0%
Authenticate -- other: 0%
Qualify -- other: 0%
Catalogue -- other: 0%
Input into computer -- other: 0%Type: 0.02%
Credit -- other: 0%
Debit -- other: 0%
Post (financial) -- other: 0%
 Re-enter -- other: 0%
 Tabulate -- other: 0%
Delineate -- other: 0%
 Shade -- other: 0%
 Sketch -- other: 0%
 Diagram -- other: 0%
 Graph -- other: 0%
Type -- other: 0.02%
Top-1
Generate image
using computer: 7.2%
Top-3
Create Video: 2.7%
Top-2
Create Content: 3.5%
(Under“Create information –other”)
Fig. 5:Distribution of AI applications across activities within the “Create
information” branch of the ontology. Consistent with the term “generative AI,”
most current AI applications (58%) involve various forms of creating information,
including images, videos, and other kinds of content.
The three activities with the most AI software applications, “Generate image using
computer,” “Create Content,” and “Create video,” are all present as specializations of
this branch. Note, by the way, that even though their AI software intensity is relatively
high, the angular width of these activities in the sunburst diagram is small because
they have relatively few specialized types of ontology activities classified under them.
At this finer level of granularity, AI applications targeting informational activities
are further concentrated in a small number of specialized subcategories. In particular,
“Express information” accounts for 24% of applications, “Create information – other”
(which includes more specialized activities that feature the verb “Create” and its
synonyms along with specific objects, such as “Create budget,” “Create content,” and
others) accounts for 18%, and “Analyze” accounts for 7%.
Figure 6 shows a further zoomed-in view of the “Create information – other” col-
lection, which comprises 222 atomic activities located at the outermost level of the
ontology. Among these activities, only 99 currently have AI software applications,
9

Create information
-- other: 18%Create
(Information): 17%
Create
(Activity): 0.8%
Create
(Actor): 0%
Create Agreement: 0%
Create Alternative: 0%
 Create Animation: 0.3%
 Create Approach: 0%
 Create Archive: 0%
 Create Arrangement: 0.008%
 Create Art: 0.2%
 Create Backup: 0%
 Create Blueprint: 0%
Create Budget (Generate Budget, Synonyms: Develop Budget): 0%
 Create Checklist: 0.05%
 Create Composition: 0%
 Create Concept: 0.03%
 Create Content: 4%
 Create Contract: 0.02%
 Create Criterion: 0%
 Create Database: 0.02%
 Create Datum: 0.04%
Create Design (Produce Design, Synonyms: Develop Design): 0.2%
 Create Diagram: 0.2%
Create Display (Produce Display, Synonyms: Develop Display): 0.008%
 Create Document (Produce Document, Synonyms: Develop Document): 0.6%
 Create Documentation (Produce Documentation, Synonyms: Develop Documentation): 0.2%
 Create Drawing (Produce Drawing, Synonyms: Develop Drawing): 0.03%
 Create Effect: 0.02%
 Create Element: 0%
 Create Estimate: 0%
 Create Feature: 0%
 Create File: 0%
 Create Form: 0.2%
 Create Formula: 0.1%
 Create Framework: 0%
 Create Goal: 0%
Create Graphic (Produce Graphic, Synonyms: Develop Graphic): 0.2%
 Create History: 0%
Create Illustration: 0.04%
Create Image (Generate Image, Make Image, Produce Image, Synonyms: Develop Image): 0.2%
 Create Indicator: 0%
Create Indice: 0%
Create Inform
ation: 0%
Create Instruction: 0.2%
 Create Invoice: 0.008%
 Create Label: 0.2%
 Create Layout: 0.02%
 Create Lettering: 0%
 Create Likeness: 0.1%
 Create Log: 0.02%
Create M
anual: 0.008%
Create M
ap (Produce M
ap, Synonym
s: Develop M
ap): 0.1%
Create M
arker: 0.008%
Create M
aterial (Produce M
aterial, Synonym
s: Develop M
aterial): 0.3%
Create M
edia: 0.1%
Create M
em
orandum
: 0%
Create M
odel (Produce M
odel, Synonym
s: Develop M
odel): 0.4%
Create Order: 0%
 Create Package: 0%
 Create Pattern: 0.09%
 Create Perform
ance: 0%
Create Plan (M
ake Plan, Synonym
s: Develop Plan): 0.2%
Create Playlist: 0.07%
 Create Policy: 0%
 Create Presentation (Produce Presentation, Synonyms: Develop Presentation): 0.6%
 Create Procedure: 0.02%
 Create Process: 0.05%
 Create Profile: 0.2%
 Create Program (Produce Program, Synonyms: Develop Program): 0.08%
 Create Recipe: 0.3%
 Create Record: 0.008%
 Create Recording: 1%
 Create Report (Generate Report, Produce Report, Synonyms: Develop Report): 0.2%
 Create Representation: 0.05%
 Create Scenario: 0.008%
 Create Schedule: 0.02%
 Create Schematic: 0%
 Create Score: 0%
 Create Script: 0.06%
 Create Sequence: 0.02%
 Create Simulation: 0.04%
 Create Site: 0.8%
 Create Sketch: 0%
 Create Specification: 0.02%
 Create Standard: 0%
 Create Strategy: 0.06%
 Create System: 0.02%
 Create Template: 0.07%
 Create Tool: 0.05%
 Create Visualization: 0.4%
 Create Worksheet: 0.04%
 Develop Account: 0%
 Develop Advertisement: 0.3%
 Develop Agenda: 0%
 Develop Aid: 0.008%
 Develop Algorithm: 0.008%
 Develop Application: 2%
 Develop Architecture: 0%
 Develop Artwork: 0%
Develop Aspect: 0%
Develop Assay: 0%
Develop Assessment: 0.05%
Develop Base: 0%
Develop Boundary: 0%
Develop Briefing: 0%
Develop Brochure: 0.008%
Develop Campaign: 0.05%
Develop Capability: 0%
Develop Case: 0%
Develop Channel: 0%
Develop Chart: 0.02%
Develop Circuit: 0%
Develop Code: 0.02%
Develop Configuration: 0%
Develop Controller: 0%
Develop Course: 0.2%
Develop Curricula: 0.008%
Develop Curriculum: 0.008%
Develop Curve: 0%
Develop Factor: 0%
Develop Flow: 0%
Develop Forecast: 0%
Develop Grid: 0%
Develop Guide: 0.008%
Develop Guideline: 0.008%
Develop Idea: 0.2%
Develop Iep: 0%
Develop Index: 0%
Develop Initiative: 0%
Develop Instrument: 0%
Develop Intervention: 0%
Develop Item: 0%
Develop Law: 0%
Develop Library: 0%
Develop List (Make List, Synonyms: Generate List): 0.07%
Develop Location: 0%
Develop Meal: 0%
Develop Measure: 0%
Develop Medication: 0.008%
Develop Menu: 0.008%
Develop Method: 0%
Develop Methodology: 0%
Develop Metric: 0%
 Develop Modification: 0%
 Develop Motion: 0%
 Develop Newsletter: 0.06%
 Develop Objective: 0%
 Develop Packet: 0%
 Develop Page: 0.008%
 Develop Parameter: 0%
 Develop Perspective: 0%
 Develop Philosophy: 0%
 Develop Portion: 0%
Develop Principle: 0%
 Develop Priority: 0%
 Develop Product: 0.03%
 Develop Program
m
ing: 0%
Develop Project: 0%
 Develop Prom
otion: 0%
Develop Proposal: 0%
 Develop Protocol: 0%
 Develop Query: 0.1%
 Develop Rate: 0%
Develop Recom
m
endation: 0%
Develop Regulation: 0%
Develop Requirem
ent: 0.02%
Develop Resource: 0%
 Develop Routine: 0%
 Develop Rule: 0%
 Develop Scale: 0%
 Develop Scope: 0%
Develop Software: 0.4%
 Develop Solution: 0.02%
 Develop Story: 0.05%
 Develop Structure: 0%
 Develop Study: 0%
 Develop Style: 0%
Develop Survey: 0.03%
 Develop Tactic: 0%
 Develop Target: 0%
Develop Technique: 0%
Develop Technology: 0%
 Develop Test: 0.4%
 Develop Text: 0%
Develop Theory: 0%
Develop Threshold: 0%
 Develop Topic: 0%
Develop Treatment: 0.008%
 Develop Way: 0%
Develop Workbook: 0.008%
 Generate Lead: 1.0%
 Generate Proof: 0%
 Generate Ratio: 0%
 Generate Tape: 0%
Make Dub: 0.008%
Produce Copy: 0%
Produce Correspondence: 0%
 Produce Film: 0.02%
 Produce Layer: 0%
Produce Measurement: 0%
 Produce Research: 0%
 Produce Result: 0%
 Produce Set: 0%
Produce Statistic: 0%
Produce Table: 0.008%
Create Landscape: 0.008%
 Create Tufting: 0%
Develop Action: 0%
Develop Activity: 0%
Develop Busines: 0.05%
 Develop Class: 0%
Develop Investigation: 0%
 Develop Liaison: 0%
Develop Network: 0.02%
Develop Partnership: 0%
Develop Practice: 0%
Develop Relationship: 0.02%
Develop Review: 0%
Develop Service: 0%
Develop Session: 0%
Develop Training: 0.008%
Make Presentation: 0%
Make Recording: 0%
Develop Clientele: 0%
Develop Contact: 0%
Fig. 6:Distribution of AI applications across activities within the “Create
Information – other” branch of the ontology. The diagram includes detailed
examples of activities both with and without AI applications, and as discussed in
Section 3.1, this provides a kind of checklist for different types of opportunities. (Read-
ers are encouraged to zoom in to see detailed activity names in the diagram.)
while the remaining 123 have no observed AI applications. The 18% of AI applica-
tions associated with this collection are thinly distributed across the covered activities,
with the majority of atomic activities receiving less than 0.1% of applications each.
Appendix F.5 provides illustrative examples of the five of these atomic activities
with the highest AI concentration, along with the O*NET tasks that include these
atomic activities. And Section 3.1 discusses how frameworks like those in Figure 6 and
Appendix F.5 can help systematically analyze and identify possible new opportunities
for using AI.
10

In what activities is AI software not being used?
While current AI software applications are densely clustered around a small set of
activities, a substantial number of activities remain sparsely represented or entirely
unpopulated by these applications. Excluding activities under the “Do” category that
exhibit zero counts (shown in gray), several “Think” and “Interact” activities show no
recorded AI applications. These include, among others, “Administer (treat),” “Collab-
orate (Actor),” “Comply,” “Attend (go to),” “Confer (Actor),” and “Analyze (Physical
Object),” each accounting for 0% of observed AI applications (as shown in the full
sunburst diagram in Appendix F.3).
Notably, some of these underrepresented activities correspond to forms of work
that are either highly context-dependent, socially embedded, or physically situated,
which may partially explain their limited AI adoption. In other words, these activities
may require high levels of the human capabilities included in the EPOCH framework
(Empathy, Presence, Opinion, Creativity, and Hope) [13].
In addition, several activities that involve authoritative, directive, or passive roles,
such as “Order (authoritative),” “Authorize,” “Assign,” and “Receive,” are also absent
from the current AI application landscape. These activities may be less amenable
to automation or may offer comparatively limited value when delegated to AI sys-
tems, given prevailing human preferences, accountability concerns, and organizational
norms. Taken together, the absence of AI applications in these areas highlights impor-
tant gaps and boundaries in current AI capabilities and adoption. These gaps point to
potential opportunities for future research, engineering, and entrepreneurial activity.
Viewed through the lens of our ontology, the distribution of AI applications reveals
a strong emphasis on information-centric and cognitively intensive activities, including
content generation, modification, and analysis. At the same time, this analysis high-
lights a pronounced imbalance in AI deployment, with certain regions of the activity
space appearing highly saturated while others remain comparatively underexplored.
Underrepresented activities are likely constrained either by current technical limi-
tations, limited availability of relevant data, or insufficient economic incentives for
development.
In many ways, thenegativeexamples of activities without much AI usage so far may
be as interesting as the positive ones, and we elaborate further on these possibilities
in Section 3.1.
2.2.2 How have uses of AI software applications evolved?
In addition to the cross-sectional analysis just described, we also conducted a longi-
tudinal study of how uses of AI software applications have evolved over time. Using
the launch dates of AI applications recorded in the dataset, we analyzed changes in
both the intensity and functional distribution of AI software applications over the past
decade.
Emergence of new specializations
Figure 7 reveals a clear and accelerating expansion of AI applications from 2016 to
2025, accompanied by increasing breadth of coverage within the ontology. In the early
11

Act: 0.08%
Act on information
(“Think”): 0.07%
Act with other activities and actors (“Interact”): 0.03% Act on physical objects (“Do”): 0%
Create
information: 0.05%
Modify
information: 0%
Transfer
information: 0.02%
Storeinformation: 0%
Transfer between
actors: 0.03%
Act onactivities: 0%
Modify physicalobjects: 0%
Create physicalobjects: 0%
Store physical
objects: 0%
Transfer physical
objects: 0%
Plan: 0%
Analyze: 0.008%Decide: 0.008% Calculate: 0% Express information: 0.02% Assemble information: 0% Reason: 0% Create information -- other: 0.02% Solve: 0%
Transform information: 0% Com bine inform
ation: 0%
Separate information: 0% Move information: 0%Exchange information: 0.008%
Get information: 0%Provide information: 0.008% Communicate (transfer information end-to-end): 0% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 0%
Buy: 0.008%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 0.02%
Transfer service: 0.008%
Transfer physical objects: 0%
Interact: 0%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0%
Communicate (transfer information end-to-end): 0%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0% W ithhold: 0%
Perform
 (action): 0%
Improve: 0%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0% Pass (achieve): 0% Undertake: 0% Transform physical objects: 0%
Separate physical objects: 0%
Combine physical objects: 0%
Move physical objects: 0%
Assemble: 0%
Fabricate: 0%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 0%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0%
Outline: 0%
Plan -- other: 0%
Propose: 0%
Schedule: 0%
Stage: 0%
Analyze -- other: 0.008%
 Characterize: 0%
 Correlate: 0%
 Determine: 0%
 Experiment: 0%
 Investigate: 0%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0%
 Reject: 0%
 Rule: 0%
 Select: 0.008%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0%
 Count: 0%
 Estimate: 0%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0%
 Record: 0.02%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0%
 Reason -- other: 0%
 Create (Activity): 0%
 Create (Actor): 0%
Create (Information): 0.02%
 Address (solve): 0%
 Resolve: 0%
Solve -- other: 0%
Adjust (information): 0%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 0%
Organize (analytically): 0%
 Perm
ute: 0%
Prepare (inform
ation): 0%
Process (inform
ation): 0%
Renew (inform
ation): 0%
Revise: 0%
 Service (inform
ation): 0%
Switch: 0%
 Transform
 inform
ation -- other: 0%
Translate: 0%
 Use: 0%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0%
Gather (inform
ation): 0%
Incorporate (inform
ation): 0%
Pack (together) (information): 0%
 Synthesize (information): 0%
 Break (into components): 0%
 Cut (information): 0%
 Disconnect (information): 0%
 Remove (information): 0%
 Separate information -- other: 0%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 0.008%
 Correspond: 0%
 Debate: 0%
 Exchange information -- other: 0%
 Interview: 0%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0%
 Network: 0%
 Reach: 0%
 Teach: 0%
 Access: 0%
 Download: 0%
 Evaluate: 0%
 Gather (information): 0%
 Get information -- other: 0%
 Import: 0%
 Learn: 0%
 Perceive: 0%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0%
 Provide decision: 0%
 Provide money: 0%
 Send information: 0.008%
 Communicate (transfer information end-to-end) -- other: 0%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 0%
Ticket: 0%
Buy -- other: 0%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0.008%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 0%
Exchange information: 0.008%
Get information: 0%
Provide information: 0.008%
End service: 0%
Exchange service: 0%
Get service: 0.008%
Provide service: 0%
Exchange physical objects: 0%
Get physical objects: 0%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 0%
 Conduct: 0%
 M
ake: 0%
Perform
 (action) -- other: 0%
Practice: 0%
 Rehearse: 0%
 Run (perform
): 0%
Im
prove -- other: 0%
Optim
ize: 0%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0%
Clean (physical): 0%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0%
 Process (physical): 0%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
 Cut (physical): 0%
 Disassemble: 0%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0%
 Consolidate: 0%
 Cover: 0%
Enclose: 0%
Gather (physical): 0%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0%
Reorient physical objects: 0%
Transport physical objects: 0%
 Assemble -- other: 0%
Configure (physical): 0%
Construct (physical): 0%
 Copy (physical): 0%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 0%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0%
2016
Act: 0.3%
Act on information
(“Think”): 0.3%
Act with other activities and actors (“Interact”): 0.08% Act on physical objects (“Do”): 0%
Create
information: 0.2%
Modify
information: 0.05%
Transfer
information: 0.05%
Storeinformation: 0%
Transfer between
actors: 0.08%
Act onactivities: 0.008%
Modify physicalobjects: 0%
Create physicalobjects: 0%
Store physical
objects: 0%
Transfer physical
objects: 0%
Plan: 0.008%
Analyze: 0.02%Decide: 0.02% Calculate: 0% Express information: 0.07% Assemble information: 0% Reason: 0% Create information -- other: 0.04% Solve: 0.008%
Transform information: 0.05% Com bine inform
ation: 0%
Separate information: 0% Move information: 0%Exchange information: 0.008%
Get information: 0.02%Provide information: 0.02%
Communicate (transfer information end-to-end): 0.008% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 0%
Buy: 0.02%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 0.05%
Transfer service: 0.02%
Transfer physical objects: 0%
Interact: 0%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0%
Communicate (transfer information end-to-end): 0.008%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0% W ithhold: 0%
Perform
 (action): 0%
Im
prove: 0.008%
Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0% Pass (achieve): 0% Undertake: 0% Transform physical objects: 0%
Separate physical objects: 0%
Combine physical objects: 0%
Move physical objects: 0%
Assemble: 0%
Fabricate: 0%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 0%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0%
Outline: 0%
 Plan -- other: 0.008%
Propose: 0%
Schedule: 0%
Stage: 0%
Analyze -- other: 0.02%
 Characterize: 0%
 Correlate: 0%
 Determine: 0%
 Experiment: 0%
 Investigate: 0%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0%
 Reject: 0%
 Rule: 0%
 Select: 0.02%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0%
 Count: 0%
 Estimate: 0%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0%
 Record: 0.07%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0%
 Reason -- other: 0%
 Create (Activity): 0%
 Create (Actor): 0%
Create (Information): 0.04%
 Address (solve): 0%
 Resolve: 0%
Solve -- other: 0.008%
Adjust (information): 0.02%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 0.008%
Organize (analytically): 0%
 Perm
ute: 0%
Prepare (inform
ation): 0.008%
Process (inform
ation): 0%
Renew (inform
ation): 0%
Revise: 0.008%
 Service (inform
ation): 0%
Switch: 0%
 Transform
 inform
ation -- other: 0%
Translate: 0.008%
 Use: 0%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0%
Gather (inform
ation): 0%
Incorporate (inform
ation): 0%
Pack (together) (information): 0%
 Synthesize (information): 0%
 Break (into components): 0%
 Cut (information): 0%
 Disconnect (information): 0%
 Remove (information): 0%
 Separate information -- other: 0%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 0.008%
 Correspond: 0%
 Debate: 0%
 Exchange information -- other: 0%
 Interview: 0%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0%
 Network: 0%
 Reach: 0%
 Teach: 0%
 Access: 0%
 Download: 0%
 Evaluate: 0.02%
 Gather (information): 0%
 Get information -- other: 0%
 Import: 0%
 Learn: 0%
 Perceive: 0.008%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0%
 Provide decision: 0%
 Provide money: 0%
 Send information: 0.02%
 Communicate (transfer information end-to-end) -- other: 0%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 0%
Ticket: 0%
Buy -- other: 0%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0.02%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 0.008%
Exchange information: 0.008%
Get information: 0.02%
Provide information: 0.02%
End service: 0%
Exchange service: 0%
Get service: 0.02%
Provide service: 0%
Exchange physical objects: 0%
Get physical objects: 0%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 0%
 Conduct: 0%
 M
ake: 0%
Perform
 (action) -- other: 0%
Practice: 0%
 Rehearse: 0%
 Run (perform
): 0%
Im
prove -- other: 0.008%
Optim
ize: 0%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0%
Clean (physical): 0%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0%
 Process (physical): 0%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
 Cut (physical): 0%
 Disassemble: 0%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0%
 Consolidate: 0%
 Cover: 0%
Enclose: 0%
Gather (physical): 0%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0%
Reorient physical objects: 0%
Transport physical objects: 0%
 Assemble -- other: 0%
Configure (physical): 0%
Construct (physical): 0%
 Copy (physical): 0%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 0%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0% 2017
Act: 0.5%
Act on information
(“Think”): 0.5%
Act with other activities and actors (“Interact”): 0.2% Act on physical objects (“Do”): 0%
Create
information: 0.3%
Modify
information: 0.08%
Transfer
information: 0.1%
Storeinformation: 0%
Transfer between
actors: 0.2%
Act onactivities: 0.03%
Modify physicalobjects: 0%
Create physicalobjects: 0%
Store physical
objects: 0%
Transfer physical
objects: 0%
Plan: 0.02%
Analyze: 0.06%Decide: 0.02% Calculate: 0% Express information: 0.1% Assemble information: 0% Reason: 0% Create information -- other: 0.06% Solve: 0.008%
Transform information: 0.08% Com bine inform
ation: 0%
Separate information: 0% Move information: 0%Exchange information: 0.008%
Get information: 0.05%Provide information: 0.02%
Communicate (transfer information end-to-end): 0.03% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 0.008%
Buy: 0.02%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 0.1%
Transfer service: 0.05%
Transfer physical objects: 0%
Interact: 0%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0%
Communicate (transfer information end-to-end): 0.03%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0% W ithhold: 0%
Perform
 (action): 0.008%
Im
prove: 0.02%
Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0.008% Pass (achieve): 0% Undertake: 0% Transform physical objects: 0%
Separate physical objects: 0%
Combine physical objects: 0%
Move physical objects: 0%
Assemble: 0%
Fabricate: 0%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 0%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0%
Outline: 0%
 Plan -- other: 0.02%
Propose: 0%
Schedule: 0%
Stage: 0%
Analyze -- other: 0.05%
 Characterize: 0%
 Correlate: 0%
 Determine: 0.008%
 Experiment: 0%
 Investigate: 0%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0%
 Reject: 0%
 Rule: 0%
 Select: 0.02%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0%
 Count: 0%
 Estimate: 0%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0%
 Record: 0.1%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0%
 Reason -- other: 0%
 Create (Activity): 0%
 Create (Actor): 0%
Create (Information): 0.06%
 Address (solve): 0%
 Resolve: 0%
Solve -- other: 0.008%
Adjust (information): 0.02%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 0.02%
Organize (analytically): 0%
 Perm
ute: 0%
Prepare (inform
ation): 0.008%
Process (inform
ation): 0.02%
Renew (inform
ation): 0%
Revise: 0.008%
 Service (inform
ation): 0%
Switch: 0%
 Transform
 inform
ation -- other: 0%
Translate: 0.008%
 Use: 0%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0%
Gather (inform
ation): 0%
Incorporate (inform
ation): 0%
Pack (together) (information): 0%
 Synthesize (information): 0%
 Break (into components): 0%
 Cut (information): 0%
 Disconnect (information): 0%
 Remove (information): 0%
 Separate information -- other: 0%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 0.008%
 Correspond: 0%
 Debate: 0%
 Exchange information -- other: 0%
 Interview: 0%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0%
 Network: 0%
 Reach: 0%
 Teach: 0%
 Access: 0%
 Download: 0%
 Evaluate: 0.02%
 Gather (information): 0%
 Get information -- other: 0%
 Import: 0%
 Learn: 0%
 Perceive: 0.03%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0%
 Provide decision: 0%
 Provide money: 0%
 Send information: 0.02%
 Communicate (transfer information end-to-end) -- other: 0%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 0.008%
Ticket: 0%
Buy -- other: 0%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0.02%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 0.03%
Exchange information: 0.008%
Get information: 0.05%
Provide information: 0.02%
End service: 0%
Exchange service: 0%
Get service: 0.04%
Provide service: 0.008%
Exchange physical objects: 0%
Get physical objects: 0%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 0.008%
 Conduct: 0%
 M
ake: 0%
Perform
 (action) -- other: 0%
Practice: 0%
 Rehearse: 0%
 Run (perform
): 0%
Improve -- other: 0.02%
Optim
ize: 0%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0.008%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0%
Clean (physical): 0%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0%
 Process (physical): 0%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
 Cut (physical): 0%
 Disassemble: 0%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0%
 Consolidate: 0%
 Cover: 0%
Enclose: 0%
Gather (physical): 0%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0%
Reorient physical objects: 0%
Transport physical objects: 0%
 Assemble -- other: 0%
Configure (physical): 0%
Construct (physical): 0%
 Copy (physical): 0%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 0%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0% 2018
Act: 0.9%
Act on information
(“Think”): 0.8%
Act with other activities and actors (“Interact”): 0.3% Act on physical objects (“Do”): 0%
Create
information: 0.5%
Modify
information: 0.2%
Transfer
information: 0.2%
Storeinformation: 0%
Transfer between
actors: 0.3%
Act onactivities: 0.07%
Modify physicalobjects: 0%
Create physicalobjects: 0%
Store physical
objects: 0%
Transfer physical
objects: 0%
Plan: 0.03%
Analyze: 0.08%Decide: 0.04% Calculate: 0% Express information: 0.2% Assemble information: 0% Reason: 0% Create information -- other: 0.1% Solve: 0.02%
Transform information: 0.1% Com bine inform
ation: 0%
Separate information: 0.02% Move information: 0%Exchange information: 0.02%
Get information: 0.08%Provide information: 0.05%
Communicate (transfer information end-to-end): 0.04% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 0.008%
Buy: 0.03%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 0.2%
Transfer service: 0.08%
Transfer physical objects: 0%
Interact: 0%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0%
Communicate (transfer information end-to-end): 0.04%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0% W ithhold: 0%
Perform
 (action): 0.03%
Im
prove: 0.03%
Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0.008% Pass (achieve): 0% Undertake: 0% Transform physical objects: 0%
Separate physical objects: 0%
Combine physical objects: 0%
Move physical objects: 0%
Assemble: 0%
Fabricate: 0%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 0%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0.008%
Outline: 0%
 Plan -- other: 0.02%
Propose: 0%
Schedule: 0%
Stage: 0%
Analyze -- other: 0.05%
 Characterize: 0%
 Correlate: 0%
 Determine: 0.008%
 Experiment: 0%
 Investigate: 0.02%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0%
 Reject: 0%
 Rule: 0%
 Select: 0.04%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0%
 Count: 0%
 Estimate: 0%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0%
 Record: 0.2%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0%
 Reason -- other: 0%
 Create (Activity): 0%
 Create (Actor): 0%
Create (Information): 0.1%
 Address (solve): 0%
 Resolve: 0%
Solve -- other: 0.02%
Adjust (information): 0.03%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 0.03%
Organize (analytically): 0%
 Perm
ute: 0%
Prepare (inform
ation): 0.02%
Process (inform
ation): 0.02%
Renew (inform
ation): 0%
Revise: 0.02%
 Service (inform
ation): 0%
Switch: 0%
 Transform
 inform
ation -- other: 0%
Translate: 0.008%
 Use: 0.008%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0%
Gather (inform
ation): 0%
Incorporate (inform
ation): 0%
Pack (together) (information): 0%
 Synthesize (information): 0%
 Break (into components): 0%
 Cut (information): 0.008%
 Disconnect (information): 0%
 Remove (information): 0%
 Separate information -- other: 0.02%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 0.008%
 Correspond: 0%
 Debate: 0%
 Exchange information -- other: 0%
 Interview: 0%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0%
 Network: 0%
 Reach: 0%
 Teach: 0.02%
 Access: 0%
 Download: 0%
 Evaluate: 0.03%
 Gather (information): 0%
 Get information -- other: 0%
 Import: 0%
 Learn: 0.02%
 Perceive: 0.04%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0%
 Provide decision: 0%
 Provide money: 0%
 Send information: 0.05%
 Communicate (transfer information end-to-end) -- other: 0%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 0.008%
Ticket: 0%
Buy -- other: 0.008%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0.02%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 0.04%
Exchange information: 0.02%
Get information: 0.08%
Provide information: 0.05%
End service: 0%
Exchange service: 0%
Get service: 0.06%
Provide service: 0.02%
Exchange physical objects: 0%
Get physical objects: 0%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 0.03%
 Conduct: 0%
 M
ake: 0%
Perform
 (action) -- other: 0%
Practice: 0%
 Rehearse: 0%
 Run (perform
): 0%
Improve -- other: 0.03%
Optim
ize: 0%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0.008%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0%
Clean (physical): 0%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0%
 Process (physical): 0%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
 Cut (physical): 0%
 Disassemble: 0%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0%
 Consolidate: 0%
 Cover: 0%
Enclose: 0%
Gather (physical): 0%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0%
Reorient physical objects: 0%
Transport physical objects: 0%
 Assemble -- other: 0%
Configure (physical): 0%
Construct (physical): 0%
 Copy (physical): 0%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 0%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0% 2019
Act: 2%
Act on information
(“Think”): 2%
Act with other activities and actors (“Interact”): 0.8% Act on physical objects (“Do”): 0%
Createinformation: 1%
Modify
information: 0.4%
Transfer
information: 0.5%
Storeinformation: 0%
Transfer between
actors: 0.8%
Act onactivities: 0.1%
Modify physicalobjects: 0%
Create physicalobjects: 0%
Store physical
objects: 0%
Transfer physical
objects: 0%
Plan: 0.06%
Analyze: 0.2%Decide: 0.08% Calculate: 0.008% Express information: 0.4% Assemble information: 0.02% Reason: 0% Create information -- other: 0.3% Solve: 0.02%
Transform information: 0.3% Com bine inform
ation: 0.03%
Separate information: 0.05% Move information: 0%Exchange information: 0.03%
Get information: 0.2%Provide information: 0.09%
Communicate (transfer information end-to-end): 0.1% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 0.02%
Buy: 0.05%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 0.5%
Transfer service: 0.2%
Transfer physical objects: 0%
Interact: 0%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0%
Communicate (transfer information end-to-end): 0.1%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0% W ithhold: 0%
Perform
 (action): 0.05%
Im
prove: 0.08%
Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Implement: 0.02%Pass (achieve): 0% Undertake: 0% Transform physical objects: 0%
Separate physical objects: 0%
Combine physical objects: 0%
Move physical objects: 0%
Assemble: 0%
Fabricate: 0%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 0%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0.02%
Outline: 0%
 Plan -- other: 0.05%
Propose: 0%
Schedule: 0%
Stage: 0%
 Analyze -- other: 0.1%
 Characterize: 0%
 Correlate: 0%
 Determine: 0.03%
 Experiment: 0%
 Investigate: 0.03%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0%
 Reject: 0%
 Rule: 0%
 Select: 0.08%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0.008%
 Count: 0%
 Estimate: 0%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0%
 Record: 0.4%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0.02%
Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0%
 Reason -- other: 0%
 Create (Activity): 0%
 Create (Actor): 0%
Create (Information): 0.3%
 Address (solve): 0%
 Resolve: 0%
Solve -- other: 0.02%
Adjust (information): 0.05%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 0.08%
Organize (analytically): 0%
 Perm
ute: 0%
Prepare (inform
ation): 0.02%
Process (inform
ation): 0.05%
Renew (inform
ation): 0%
Revise: 0.1%
 Service (inform
ation): 0%
Switch: 0%
 Transform
 inform
ation -- other: 0.008%
Translate: 0.02%
 Use: 0.008%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (information): 0.008%
Gather (inform
ation): 0.02%
Incorporate (inform
ation): 0%
Pack (together) (information): 0%
 Synthesize (information): 0%
 Break (into components): 0%
 Cut (information): 0.02%
 Disconnect (information): 0%
 Remove (information): 0%
 Separate information -- other: 0.04%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 0.008%
 Correspond: 0%
 Debate: 0%
 Exchange information -- other: 0%
 Interview: 0%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0%
 Network: 0%
 Reach: 0%
 Teach: 0.02%
 Access: 0%
 Download: 0%
 Evaluate: 0.08%
 Gather (information): 0.02%
 Get information -- other: 0%
 Import: 0%
 Learn: 0.02%
 Perceive: 0.1%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0%
 Provide decision: 0%
 Provide money: 0%
 Send information: 0.09%
 Communicate (transfer information end-to-end) -- other: 0.03%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 0.02%
Ticket: 0%
Buy -- other: 0.008%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0.04%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 0.1%
Exchange information: 0.03%
Get information: 0.2%
Provide information: 0.09%
End service: 0%
Exchange service: 0%
Get service: 0.2%
Provide service: 0.05%
Exchange physical objects: 0%
Get physical objects: 0%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0.03%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 0.04%
 Conduct: 0%
 M
ake: 0%
Perform
 (action) -- other: 0%
Practice: 0%
 Rehearse: 0.008%
 Run (perform
): 0%
Improve -- other: 0.06%
Optim
ize: 0%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0.02%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0%
Clean (physical): 0%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0%
 Process (physical): 0%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
 Cut (physical): 0%
 Disassemble: 0%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0%
 Consolidate: 0%
 Cover: 0%
Enclose: 0%
Gather (physical): 0%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0%
Reorient physical objects: 0%
Transport physical objects: 0%
 Assemble -- other: 0%
Configure (physical): 0%
Construct (physical): 0%
 Copy (physical): 0%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 0%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0% 2020
Act: 5%
Act on information
(“Think”): 4%
Act with other activities and actors (“Interact”): 2% Act on physical objects (“Do”): 0%
Createinformation: 3%
Modify
information: 1.0%
Transfer
information: 0.9%
Storeinformation: 0%
Transfer between
actors: 1%
Act onactivities: 0.4%
Modify physicalobjects: 0%
Create physicalobjects: 0%
Store physical
objects: 0%
Transfer physical
objects: 0%
Plan: 0.1%
Analyze: 0.5%Decide: 0.1% Calculate: 0.02% Express information: 0.9% Assemble information: 0.03% Reason: 0% Create information -- other: 0.8% Solve: 0.03%
Transform information: 0.8% Com bine inform
ation: 0.06%
Separate information: 0.1% Move information: 0%Exchange information: 0.1%
Get information: 0.3%Provide information: 0.2% Communicate (transfer information end-to-end): 0.2% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 0.03%
Buy: 0.05%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 0.9%
Transfer service: 0.6%
Transfer physical objects: 0%
Interact: 0%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0%
Communicate (transfer information end-to-end): 0.2%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0% W ithhold: 0%
Perform
 (action): 0.08%
Im
prove: 0.3%
Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Implement: 0.02%Pass (achieve): 0% Undertake: 0% Transform physical objects: 0%
Separate physical objects: 0%
Combine physical objects: 0%
Move physical objects: 0%
Assemble: 0%
Fabricate: 0%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 0%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0.03%
Outline: 0%
 Plan -- other: 0.08%
 Propose: 0.02%
 Schedule: 0.02%
Stage: 0%
 Analyze -- other: 0.2%
 Characterize: 0%
 Correlate: 0%
 Determine: 0.07%
 Experiment: 0%
 Investigate: 0.05%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0.008%
 Reject: 0%
 Rule: 0%
 Select: 0.1%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0.02%
 Count: 0%
Estimate: 0.008%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
Express Live: 0.008%
 Record: 0.9%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0.03%
Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0%
 Reason -- other: 0%
 Create (Activity): 0.02%
Create (Actor): 0%
Create (Information): 0.8%
 Address (solve): 0%
 Resolve: 0%
Solve -- other: 0.03%
Adjust (information): 0.08%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 0.3%
Organize (analytically): 0%
 Perm
ute: 0%
Prepare (inform
ation): 0.02%
Process (inform
ation): 0.1%
Renew (inform
ation): 0%
Revise: 0.2%
 Service (inform
ation): 0%
Switch: 0%
 Transform
 inform
ation -- other: 0.02%
Translate: 0.06%
 Use: 0.008%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (information): 0.008%
Gather (inform
ation): 0.04%
Incorporate (inform
ation): 0.008%
Pack (together) (information): 0%
 Synthesize (information): 0.008%
 Break (into components): 0%
 Cut (information): 0.02%
 Disconnect (information): 0%
 Remove (information): 0%
 Separate information -- other: 0.08%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 0.02%
 Correspond: 0%
 Debate: 0%
 Exchange information -- other: 0%
 Interview: 0%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0.008%
 Network: 0%
 Reach: 0%
 Teach: 0.09%
 Access: 0%
 Download: 0%
 Evaluate: 0.1%
 Gather (information): 0.04%
 Get information -- other: 0%
 Import: 0%
 Learn: 0.02%
 Perceive: 0.2%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0.008%
 Provide decision: 0%
 Provide money: 0%
 Send information: 0.2%
 Communicate (transfer information end-to-end) -- other: 0.04%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 0.03%
Ticket: 0%
Buy -- other: 0.008%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0.05%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 0.2%
Exchange information: 0.1%
Get information: 0.3%
Provide information: 0.2%
End service: 0%
Exchange service: 0%
Get service: 0.5%
Provide service: 0.1%
Exchange physical objects: 0%
Get physical objects: 0%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0.04%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 0.05%
 Conduct: 0.008%
 M
ake: 0%
Perform
 (action) -- other: 0%
Practice: 0%
 Rehearse: 0.02%
 Run (perform
): 0%
Im
prove -- other: 0.2%
Optim
ize: 0.08%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0.02%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0%
Clean (physical): 0%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0%
 Process (physical): 0%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
 Cut (physical): 0%
 Disassemble: 0%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0%
 Consolidate: 0%
 Cover: 0%
Enclose: 0%
Gather (physical): 0%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0%
Reorient physical objects: 0%
Transport physical objects: 0%
 Assemble -- other: 0%
Configure (physical): 0%
Construct (physical): 0%
 Copy (physical): 0%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 0%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0%
2021
Act: 13%
Act on information
(“Think”): 12%
Act with other activities and actors (“Interact”): 4% Act on physical objects (“Do”): 0%
Createinformation: 8%
Modify
information: 2%
Transfer
information: 2%
Storeinformation: 0%
Transfer between
actors: 3%
Act onactivities: 0.7%
Modify physicalobjects: 0%
Create physicalobjects: 0%
Store physical
objects: 0%
Transfer physical
objects: 0%
Plan: 0.4%
Analyze: 1%
Decide: 0.3% Calculate: 0.05% Express information: 4% Assemble information: 0.09% Reason: 0.08% Create information -- other: 2% Solve: 0.06%
Transform information: 2% Com bine inform
ation: 0.08%
Separate information: 0.2% Move information: 0%Exchange information: 0.4%
Get information: 0.8%Provide information: 0.7% Communicate (transfer information end-to-end): 0.3% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 0.04%
Buy: 0.09%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 2%
Transfer service: 1%
Transfer physical objects: 0%
Interact: 0%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0.008%
Communicate (transfer information end-to-end): 0.3%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0.008% W ithhold: 0%
Perform
 (action): 0.2%
Im
prove: 0.4%
Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Implement: 0.03%Pass (achieve): 0% Undertake: 0% Transform physical objects: 0%
Separate physical objects: 0%
Combine physical objects: 0%
Move physical objects: 0%
Assemble: 0%
Fabricate: 0%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 0%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0.1%
Outline: 0%
 Plan -- other: 0.2%
 Propose: 0.02%
 Schedule: 0.05%
Stage: 0%
 Analyze -- other: 0.7%
 Characterize: 0%
 Correlate: 0%
 Determine: 0.2%
 Experiment: 0%
 Investigate: 0.2%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0.02%
 Reject: 0%
 Rule: 0%
 Select: 0.2%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0.03%
 Count: 0%
Estimate: 0.02%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0.03%
 Record: 4%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0.09%
Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0.08%
 Reason -- other: 0%
 Create (Activity): 0.06%
Create (Actor): 0%
Create (Information): 2%
 Address (solve): 0%
 Resolve: 0.02%
Solve -- other: 0.05%
Adjust (information): 0.2%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 0.4%
Organize (analytically): 0.08%
 Perm
ute: 0%
Prepare (inform
ation): 0.05%
Process (inform
ation): 0.3%
Renew (inform
ation): 0%
Revise: 0.8%
 Service (inform
ation): 0.02%
Switch: 0%
 Transform
 inform
ation -- other: 0.04%
Translate: 0.2%
 Use: 0.02%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (information): 0.008%
Gather (inform
ation): 0.05%
Incorporate (inform
ation): 0.008%
Pack (together) (information): 0%
 Synthesize (information): 0.02%
 Break (into components): 0%
 Cut (information): 0.1%
 Disconnect (information): 0%
 Remove (information): 0.008%
Separate information -- other: 0.1%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 0.07%
 Correspond: 0%
 Debate: 0.008%
 Exchange information -- other: 0.008%
 Interview: 0.008%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0.008%
 Network: 0%
 Reach: 0.008%
 Teach: 0.3%
 Access: 0.008%
 Download: 0%
 Evaluate: 0.3%
 Gather (information): 0.05%
 Get information -- other: 0.008%
 Import: 0%
 Learn: 0.08%
 Perceive: 0.4%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0.03%
 Provide decision: 0%
 Provide money: 0%
 Send information: 0.7%
 Communicate (transfer information end-to-end) -- other: 0.06%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 0.04%
Ticket: 0%
Buy -- other: 0.02%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0.08%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 0.3%
Exchange information: 0.4%
Get information: 0.8%
Provide information: 0.7%
End service: 0%
Exchange service: 0%
Get service: 0.9%
Provide service: 0.2%
Exchange physical objects: 0%
Get physical objects: 0%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0.06%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0.008%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 0.1%
 Conduct: 0.03%
 M
ake: 0%
Perform
 (action) -- other: 0.02%
Practice: 0%
 Rehearse: 0.02%
 Run (perform
): 0%
Im
prove -- other: 0.3%
Optim
ize: 0.2%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0.02%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0%
Clean (physical): 0%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0%
 Process (physical): 0%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
 Cut (physical): 0%
 Disassemble: 0%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0%
 Consolidate: 0%
 Cover: 0%
Enclose: 0%
Gather (physical): 0%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0%
Reorient physical objects: 0%
Transport physical objects: 0%
 Assemble -- other: 0%
Configure (physical): 0%
Construct (physical): 0%
 Copy (physical): 0%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 0%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0% 2022
Act: 58%
Act on information
(“Think”): 53%
Act with other activities and actors (“Interact”): 18% Act on physical objects (“Do”): 0%
Create
information: 34%
Modify
information: 8%
Transfer
information: 12%
Storeinformation: 0.02%
Transfer between
actors: 17%
Act onactivities: 2%
Modify physicalobjects: 0%
Create physicalobjects: 0%
Store physical
objects: 0%
Transfer physical
objects: 0%
Plan: 2%
Analyze: 4%
Decide: 1% Calculate: 0.2% Express information: 14% Assemble information: 0.7% Reason: 0.4% Create information -- other: 10% Solve: 0.2%
Transform information: 7% Com bine inform
ation: 0.4%
Separate information: 0.6% Move information: 0.02%Exchange information: 2%
Get information: 4%Provide information: 5% Communicate (transfer information end-to-end): 1% Store information -- other: 0.02% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 0.3%
Buy: 0.2%
Distribute: 0.008%
Sell: 0.07%
Give: 0.02%
Take: 0%
Transfer information: 12%
Transfer service: 4%
Transfer physical objects: 0%
Interact: 0%
Open (make available): 0%
Receive: 0.008%
Return: 0%
Trade (Transfer both ways): 0.008%
Communicate (transfer information end-to-end): 1%
Earn: 0% Lend: 0% Pass (over): 0.02% Raise (funds): 0.02% W ithhold: 0%
Perform
 (action): 1.0%
Improve: 1%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Implement: 0.08%Pass (achieve): 0% Undertake: 0% Transform physical objects: 0%
Separate physical objects: 0%
Combine physical objects: 0%
Move physical objects: 0%
Assemble: 0%
Fabricate: 0%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 0%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0.7%
Outline: 0%
Plan -- other: 1%
Propose: 0.3%
 Schedule: 0.2%
Stage: 0%
 Analyze -- other: 2%
Characterize: 0%
 Correlate: 0%
 Determine: 0.5%
 Experiment: 0%
 Investigate: 0.6%
 Trace (analytically): 0%
 Accept: 0%
Decide -- other: 0.008%
 Estimate: 0.05%
 Reject: 0%
 Rule: 0.02%
 Select: 1%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0.08%
 Count: 0.02%
 Estimate: 0.05%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0.2%
 Record: 14%
Assemble information -- other: 0.02%
Configure (information): 0.05%
 Construct (information): 0.6%
Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0.02%
Organize (analytically): 0.3%
 Reason -- other: 0.03%
 Create (Activity): 0.4%
 Create (Actor): 0%
Create (Information): 10%
 Address (solve): 0%
 Resolve: 0.06%
Solve -- other: 0.1%
Adjust (information): 0.5%
 Change Appearance: 0%
 Clean (inform
ation): 0.02%
 Decode: 0%
Encode: 0.008%
 Equalize: 0%
Fill (inform
ation): 0.02%
Finish (inform
ation): 0%
Im
prove: 1%
Organize (analytically): 0.3%
 Perm
ute: 0%
Prepare (inform
ation): 0.2%
Process (inform
ation): 0.8%
Renew (inform
ation): 0%
Revise: 3%
 Service (inform
ation): 0.2%
Switch: 0%
 Transform
 inform
ation -- other: 0.2%
Translate: 0.6%
 Use: 0.2%
 Add (inform
ation): 0.02%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0.03%
Gather (inform
ation): 0.3%
Incorporate (inform
ation): 0.08%
Pack (together) (information): 0%
 Synthesize (information): 0.03%
 Break (into components): 0%
 Cut (information): 0.4%
 Disconnect (information): 0%
 Remove (information): 0.02%
Separate information -- other: 0.2%
 Move information -- other: 0%
 Put information: 0.02%
Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0.008%
 Converse: 0.7%
 Correspond: 0.008%
 Debate: 0.02%
 Exchange information -- other: 0.03%
 Interview: 0.05%
 Mediate: 0%
 Meet: 0.02%
 Negotiate: 0.008%
 Network: 0%
 Reach: 0.008%
 Teach: 1%
 Access: 0.1%
 Download: 0%
 Evaluate: 1%
 Gather (information): 0.3%
 Get information -- other: 0.04%
 Import: 0%
 Learn: 0.4%
 Perceive: 1%
 Understand: 0.05%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0.2%
 Provide decision: 0%
 Provide money: 0%
 Send information: 5%
 Communicate (transfer information end-to-end) -- other: 0.2%
 Store (Activity): 0%
 Store (Actor): 0.008%
 Store (Information): 0.008%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 0.3%
Ticket: 0%
Buy -- other: 0.02%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0.2%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0.008%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0.05%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0.02%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 1%
Exchange information: 2%
Get information: 4%
Provide information: 5%
End service: 0%
Exchange service: 0.06%
Get service: 3%
Provide service: 1%
Exchange physical objects: 0%
Get physical objects: 0%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0.008%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0.2%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0.02%
 Raise (funds) -- other: 0.02%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 0.7%
 Conduct: 0.2%
 M
ake: 0%
Perform
 (action) -- other: 0.05%
Practice: 0%
 Rehearse: 0.1%
 Run (perform
): 0%
Im
prove -- other: 0.6%
Optim
ize: 0.5%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0.08%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0%
Clean (physical): 0%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0%
 Process (physical): 0%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
 Cut (physical): 0%
 Disassemble: 0%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0%
 Consolidate: 0%
 Cover: 0%
Enclose: 0%
Gather (physical): 0%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0%
Reorient physical objects: 0%
Transport physical objects: 0%
 Assemble -- other: 0%
Configure (physical): 0%
Construct (physical): 0%
 Copy (physical): 0%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 0%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0% 2023
Act: 93%
Act on information
(“Think”): 86%
Act with other activities and actors (“Interact”): 30% Act on physical objects (“Do”): 0%
Create
information: 54%
Modify
information: 13%
Transfer
information: 20%
Storeinformation: 0.05%
Transfer between
actors: 28%
Act onactivities: 4%
Modify physicalobjects: 0%
Create physicalobjects: 0%
Store physical
objects: 0%
Transfer physical
objects: 0%
Plan: 4%
Analyze: 7%
Decide: 2% Calculate: 0.2% Express information: 22% Assemble information: 1% Reason: 0.7% Create information -- other: 17% Solve: 0.4%
Transform information: 12% Com bine inform
ation: 0.7%
Separate information: 0.8% Move information: 0.03%Exchange information: 4%
Get information: 6%Provide information: 8% Communicate (transfer information end-to-end): 2% Store information -- other: 0.05% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 0.5%
Buy: 0.4%
Distribute: 0.008%
Sell: 0.1%
Give: 0.02%
Take: 0%
Transfer information: 20%
Transfer service: 7%
Transfer physical objects: 0%
Interact: 0%
Open (make available): 0%
Receive: 0.008%
Return: 0%
Trade (Transfer both ways): 0.008%
Communicate (transfer information end-to-end): 2%
Earn: 0% Lend: 0% Pass (over): 0.05% Raise (funds): 0.03% W ithhold: 0%
Perform
 (action): 2%
Improve: 2%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0.1% Pass (achieve): 0% Undertake: 0% Transform physical objects: 0%
Separate physical objects: 0%
Combine physical objects: 0%
Move physical objects: 0%
Assemble: 0%
Fabricate: 0%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 0%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 1%
Outline: 0%
Plan -- other: 2%
Propose: 0.4%
 Schedule: 0.3%
Stage: 0%
 Analyze -- other: 4%
Characterize: 0%
 Correlate: 0%
 Determine: 0.8%
 Experiment: 0%
 Investigate: 0.9%
 Trace (analytically): 0%
 Accept: 0%
Decide -- other: 0.008%
 Estimate: 0.08%
 Reject: 0%
 Rule: 0.02%
 Select: 2%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0.1%
Count: 0.02%
 Estimate: 0.08%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0.3%
 Record: 22%
Assemble information -- other: 0.03%
Configure (information): 0.07%
 Construct (information): 1.0%
Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0.02%
Organize (analytically): 0.6%
 Reason -- other: 0.05%
 Create (Activity): 0.7%
 Create (Actor): 0%
Create (Information): 16%
 Address (solve): 0%
 Resolve: 0.08%
Solve -- other: 0.3%
Adjust (information): 0.9%
 Change Appearance: 0%
 Clean (inform
ation): 0.03%
 Decode: 0%
Encode: 0.008%
 Equalize: 0%
Fill (inform
ation): 0.1%
Finish (inform
ation): 0%
Im
prove: 2%
Organize (analytically): 0.6%
 Perm
ute: 0%
Prepare (inform
ation): 0.3%
Process (inform
ation): 1%
Renew (inform
ation): 0%
Revise: 4%
 Service (inform
ation): 0.3%
Switch: 0%
 Transform
 inform
ation -- other: 0.3%
Translate: 1%
 Use: 0.4%
 Add (inform
ation): 0.02%
Com
bine inform
ation -- other: 0.008%
Connect (inform
ation): 0.05%
Gather (inform
ation): 0.4%
Incorporate (inform
ation): 0.1%
Pack (together) (information): 0%
 Synthesize (information): 0.04%
 Break (into components): 0%
 Cut (information): 0.6%
 Disconnect (information): 0%
 Remove (information): 0.02%
Separate information -- other: 0.2%
 Move information -- other: 0%
 Put information: 0.03%
Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0.008%
 Converse: 1%
 Correspond: 0.008%
 Debate: 0.04%
 Exchange information -- other: 0.05%
 Interview: 0.1%
 Mediate: 0%
 Meet: 0.02%
 Negotiate: 0.02%
 Network: 0.02%
 Reach: 0.02%
 Teach: 3%
 Access: 0.2%
 Download: 0.008%
 Evaluate: 2%
 Gather (information): 0.4%
 Get information -- other: 0.07%
 Import: 0.008%
 Learn: 0.9%
 Perceive: 2%
 Understand: 0.08%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0.3%
 Provide decision: 0%
 Provide money: 0%
 Send information: 8%
 Communicate (transfer information end-to-end) -- other: 0.3%
 Store (Activity): 0%
 Store (Actor): 0.05%
Store (Information): 0.008%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 0.5%
Ticket: 0%
Buy -- other: 0.05%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0.3%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0.008%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0.08%
Sell Service: 0.008%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0.02%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 2%
Exchange information: 4%
Get information: 6%
Provide information: 8%
End service: 0%
Exchange service: 0.1%
Get service: 5%
Provide service: 2%
Exchange physical objects: 0%
Get physical objects: 0%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0.008%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0.3%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0.05%
 Raise (funds) -- other: 0.03%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 1%
 Conduct: 0.3%
 M
ake: 0%
Perform
 (action) -- other: 0.07%
Practice: 0.008%
 Rehearse: 0.2%
 Run (perform
): 0%
Im
prove -- other: 0.9%
Optim
ize: 0.8%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0.08%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0%
Clean (physical): 0%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0%
 Process (physical): 0%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
 Cut (physical): 0%
 Disassemble: 0%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0%
 Consolidate: 0%
 Cover: 0%
Enclose: 0%
Gather (physical): 0%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0%
Reorient physical objects: 0%
Transport physical objects: 0%
 Assemble -- other: 0%
Configure (physical): 0%
Construct (physical): 0%
 Copy (physical): 0%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 0%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0% 2024
Act: 100%
Act on information
(“Think”): 92%
Act with other activities and actors (“Interact”): 32% Act on physical objects (“Do”): 0%
Create
information: 58%
Modify
information: 14%
Transfer
information: 22%
Storeinformation: 0.05%
Transfer between
actors: 30%
Act onactivities: 4%
Modify physicalobjects: 0%
Create physicalobjects: 0%
Store physical
objects: 0%
Transfer physical
objects: 0%
Plan: 4%
Analyze: 7%
Decide: 2% Calculate: 0.2% Express information: 24% Assemble information: 1% Reason: 0.8% Create information -- other: 18% Solve: 0.4%
Transform information: 13% Com bine inform
ation: 0.7%
Separate information: 0.9% Move information: 0.05%Exchange information: 5%
Get information: 7%Provide information: 8% Communicate (transfer information end-to-end): 2% Store information -- other: 0.05% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 0.5%
Buy: 0.4%
Distribute: 0.008%
Sell: 0.1%
Give: 0.02%
Take: 0%
Transfer information: 22%
Transfer service: 7%
Transfer physical objects: 0%
Interact: 0%
Open (make available): 0%
Receive: 0.008%
Return: 0%
Trade (Transfer both ways): 0.008%
Communicate (transfer information end-to-end): 2%
Earn: 0% Lend: 0% Pass (over): 0.06% Raise (funds): 0.03% W ithhold: 0%
Perform
 (action): 2%
Improve: 2%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0.1% Pass (achieve): 0% Undertake: 0% Transform physical objects: 0%
Separate physical objects: 0%
Combine physical objects: 0%
Move physical objects: 0%
Assemble: 0%
Fabricate: 0%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 0%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 1%
Outline: 0%
Plan -- other: 2%
Propose: 0.4%
 Schedule: 0.3%
Stage: 0%
 Analyze -- other: 4%
Characterize: 0%
 Correlate: 0%
 Determine: 0.9%
 Experiment: 0%
 Investigate: 1%
 Trace (analytically): 0%
 Accept: 0%
Decide -- other: 0.008%
 Estimate: 0.08%
 Reject: 0%
 Rule: 0.02%
 Select: 2%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0.1%
Count: 0.02%
 Estimate: 0.08%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0.3%
 Record: 24%
Assemble information -- other: 0.03%
Configure (information): 0.08%
 Construct (information): 1%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0.02%
Organize (analytically): 0.7%
 Reason -- other: 0.05%
 Create (Activity): 0.8%
 Create (Actor): 0%
Create (Information): 17%
 Address (solve): 0%
 Resolve: 0.08%
Solve -- other: 0.3%
Adjust (information): 1%
 Change Appearance: 0%
 Clean (inform
ation): 0.05%
 Decode: 0%
Encode: 0.008%
 Equalize: 0%
Fill (inform
ation): 0.1%
Finish (inform
ation): 0%
Im
prove: 2%
Organize (analytically): 0.7%
 Perm
ute: 0%
Prepare (inform
ation): 0.3%
Process (inform
ation): 1%
Renew (inform
ation): 0%
Revise: 5%
 Service (inform
ation): 0.4%
Switch: 0%
 Transform
 inform
ation -- other: 0.3%
Translate: 1%
 Use: 0.4%
 Add (inform
ation): 0.02%
Com
bine inform
ation -- other: 0.008%
Connect (inform
ation): 0.05%
Gather (inform
ation): 0.4%
Incorporate (inform
ation): 0.2%
Pack (together) (information): 0%
 Synthesize (information): 0.05%
 Break (into components): 0%
 Cut (information): 0.7%
 Disconnect (information): 0%
 Remove (information): 0.02%
Separate information -- other: 0.2%
 Move information -- other: 0%
 Put information: 0.05%
Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0.008%
 Converse: 1%
 Correspond: 0.008%
 Debate: 0.04%
 Exchange information -- other: 0.05%
 Interview: 0.2%
 Mediate: 0%
 Meet: 0.02%
 Negotiate: 0.02%
 Network: 0.02%
 Reach: 0.03%
 Teach: 3%
 Access: 0.2%
 Download: 0.008%
 Evaluate: 2%
 Gather (information): 0.4%
 Get information -- other: 0.07%
 Import: 0.008%
 Learn: 0.9%
 Perceive: 3%
 Understand: 0.09%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0.3%
 Provide decision: 0%
 Provide money: 0%
 Send information: 8%
 Communicate (transfer information end-to-end) -- other: 0.3%
 Store (Activity): 0%
 Store (Actor): 0.05%
Store (Information): 0.008%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 0.5%
Ticket: 0%
Buy -- other: 0.05%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0.3%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0.008%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0.08%
Sell Service: 0.008%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0.02%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 2%
Exchange information: 5%
Get information: 7%
Provide information: 8%
End service: 0%
Exchange service: 0.1%
Get service: 5%
Provide service: 2%
Exchange physical objects: 0%
Get physical objects: 0%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0.008%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0.3%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0.06%
 Raise (funds) -- other: 0.03%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 1%
 Conduct: 0.3%
 M
ake: 0%
Perform
 (action) -- other: 0.09%
Practice: 0.008%
 Rehearse: 0.2%
 Run (perform
): 0%
Im
prove -- other: 1.0%
Optim
ize: 0.9%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0.08%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0%
Clean (physical): 0%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0%
 Process (physical): 0%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
 Cut (physical): 0%
 Disassemble: 0%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0%
 Consolidate: 0%
 Cover: 0%
Enclose: 0%
Gather (physical): 0%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0%
Reorient physical objects: 0%
Transport physical objects: 0%
 Assemble -- other: 0%
Configure (physical): 0%
Construct (physical): 0%
 Copy (physical): 0%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 0%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0% 2025
Fig. 7:Sunburst diagrams illustrating the changes in usage intensity of AI
software applications from 2016 to 2025. Each diagram represents the distri-
bution of AI applications across ontology activities for a given year. Color intensity
encodes the percentage of applications relative to the 2025 distribution. Color shading
is thus fixed and directly comparable across years, enabling longitudinal comparison
of category growth and concentration. This suggests substantial growth in the number
of applications over time but relatively little broadening in the types of activities for
which applications are available. (See larger diagrams for each year in Appendix F.6.)
period (2016–2022), AI applications are relatively sparse and distributed across a
limited number of activities, with shallow penetration into specialized branches.
A pronounced inflection point emerges after 2022, with the rise of generative AI,
when growth becomes substantially more rapid. This shift is reflected both in increased
color intensity and increased spread into deeper layers of the ontology. By 2023–2025,
the diagrams exhibit markedly broader and darker regions, indicating a sharp rise in
the number of AI applications across many branches. The use of consistent color scaling
across years further highlights that recent growth is driven primarily by intensification
within already dominant informational and cognitive activity categories, rather than
by uniform expansion into previously underrepresented functional areas (year-specific
visualizations with independent color scaling are provided in Appendix F.6.)
Growth in scale versus functional coverage
Figure 8 shows the temporal growth in the number of AI applications and the coverage
of work activities from 2016 to 2025. Coverage of work activities is defined as the
proportion of activities in the ontology for which there is at least one AI application,
relative to the total number of activities in the ontology.
In 2016, the ecosystem was still nascent, with only 11 recorded AI applications
covering 0.2% of activities. Growth during the early years (2017–2021) was gradual in
both scale and coverage, reaching 629 applications and 2.4% coverage by 2021. A clear
inflection point appears after 2022, with the number of applications rising sharply to
12

2016-12-312017-12-312018-12-312019-12-312020-12-312021-12-312022-12-312023-12-312024-12-312025-07-11
Time
0
2000
4000
6000
8000
10000
12000
14000
16000Number of AI applications
11 37 69 126 310 629
1,758
7,642
12,399
13,275
0
20
40
60
80
100
Coverage of work activities (%)
0.2% 0.6% 0.8% 1.2% 1.8% 2.4%
3.8% 7.2% 8.6% 8.7%
Fig. 8:Growth in AI software applications from 2016 to 2025.Significant
growth in the number of applications began in 2022 with the emergence of generative
AI, but it appeared to slow in 2024-25. The breadth of activities for which AI appli-
cations were available also increased over time, but at a much slower rate than the
number of applications.
7,642 in 2023 and surging further to 12,399 in 2024. Over this two-year period, the
number of AI applications increased by a factor of 6.0 times, while coverage expanded
by only a factor of 1.2 times.
Taken together, these trends suggest that despite the rapid growth in the number
of AI applications, the current AI ecosystem exhibits limited functional diversity and
generalizability. Development remains concentrated within a relatively narrow subset
of task categories, indicating that advances in AI capabilities have thus far translated
into depth in a few activities rather than breadth across the space of human activities.
2.3 Robotic systems
To understand the uses of robotic systems, we used the annualWorld Robotics
reports [11, 12] published by the International Federation of Robotics (IFR). These
reports comprise the world’s most comprehensive dataset on robotic systems, includ-
ing 2024 data on 20.8 million robots used for purposes such as cleaning, laser cutting,
welding, and preparing food. (See Section 6.4.2 for more details.)
2.3.1 Where are robotic systems used today?
Using the manual classification methods described in Section 6.5.2, we classified the
20.8 million robotic systems from the IFR dataset into the activities in our ontology.
Figure 9 shows these results in a sunburst diagram. As before, the percentage values
and color intensities indicate the share of robotic systems in that activity relative to
the total number of robotic systems, with each deployed unit weighted equally. Also,
13

Act: 100%
Act on information
(“Think”): 2%
Act with other activities and actors (“Interact”): 11% Act on physical objects (“Do”): 89%
Createinformation: 0%
Modify
information: 0%
Transfer
information: 2%
Storeinformation: 0%
Transfer between
actors: 1
1%
Act onactivities: 0.08%
Modify physicalobjects: 88%
Create physicalobjects: 0.5%
Store physical
objects: 0%
Transfer physical
objects: 0.2%
Plan: 0%
Analyze: 0%
Decide: 0%Calculate: 0% Express information: 0% Assemble information: 0% Reason: 0% Create information -- other: 0% Solve: 0%
Transform information: 0% Com bine inform
ation: 0%
Separate information: 0% Move information: 0%Exchange information: 2%
Get information: 0.2%Provide information: 0% Communicate (transfer information end-to-end): 0% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 0.9%
Buy: 0%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 2%
Transfer service: 7%
Transfer physical objects: 0.2%
Interact: 1%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0%
Communicate (transfer information end-to-end): 0%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0% W ithhold: 0%
Perform
 (action): 0.08%
Improve: 0%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0% Pass (achieve): 0% Undertake: 0% Transform physical objects: 87%
Separate physical objects: 0.02%
Combine physical objects: 1.0%
Move physical objects: 0.6%
Assemble: 0.3%
Fabricate: 0.2%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 0.2%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0%
Outline: 0%
Plan -- other: 0%
Propose: 0%
Schedule: 0%
Stage: 0%
 Analyze -- other: 0%
Characterize: 0%
 Correlate: 0%
 Determine: 0%
 Experiment: 0%
 Investigate: 0%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0%
 Reject: 0%
 Rule: 0%
 Select: 0%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0%
 Count: 0%
 Estimate: 0%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0%
 Record: 0%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0%
 Reason -- other: 0%
 Create (Activity): 0%
 Create (Actor): 0%
Create (Information): 0%
 Address (solve): 0%
 Resolve: 0%
Solve -- other: 0%
Adjust (information): 0%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 0%
Organize (analytically): 0%
 Perm
ute: 0%
Prepare (inform
ation): 0%
Process (inform
ation): 0%
Renew (inform
ation): 0%
Revise: 0%
 Service (inform
ation): 0%
Switch: 0%
 Transform
 inform
ation -- other: 0%
Translate: 0%
 Use: 0%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0%
Gather (inform
ation): 0%
Incorporate (inform
ation): 0%
Pack (together) (information): 0%
 Synthesize (information): 0%
 Break (into components): 0%
 Cut (information): 0%
 Disconnect (information): 0%
 Remove (information): 0%
 Separate information -- other: 0%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 0%
 Correspond: 0%
 Debate: 0%
 Exchange information -- other: 0%
 Interview: 0%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0%
 Network: 0%
 Reach: 0%
 Teach: 2%
 Access: 0%
 Download: 0%
 Evaluate: 0.1%
 Gather (information): 0%
 Get information -- other: 0%
 Import: 0%
 Learn: 0%
 Perceive: 0.07%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0%
 Provide decision: 0%
 Provide money: 0%
 Send information: 0%
 Communicate (transfer information end-to-end) -- other: 0%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 0.9%
Ticket: 0%
Buy -- other: 0%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 0%
Exchange information: 2%
Get information: 0.2%
Provide information: 0%
End service: 0%
Exchange service: 0%
Get service: 0.9%
Provide service: 6%
Exchange physical objects: 0%
Get physical objects: 0.2%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 1%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 0%
 Conduct: 0.03%
 M
ake: 0%
Perform
 (action) -- other: 0.04%
Practice: 0%
 Rehearse: 0%
 Run (perform
): 0%
Im
prove -- other: 0%
Optim
ize: 0%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0.02%
 Clean (physical): 87%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0%
Process (physical): 0.01%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0.05%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
Cut (physical): 0.004%
Disassemble: 0.0003%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0.01%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0.4%
 Consolidate: 0%
 Cover: 0.06%
Enclose: 0.2%
Gather (physical): 0.2%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0.1%
Reorient physical objects: 0%
Transport physical objects: 0.5%
Assemble -- other: 0.2%
Configure (physical): 0%
Construct (physical): 0.002%
 Copy (physical): 0.1%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0.2%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 0.2%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0%
Fig. 9:Where are robotic systems used today?Sunburst diagram showing
the distribution of robotic systems deployed in 2024. Percentages and color intensity
indicate the proportion of robotic systems associated with each activity relative to
the total number of robotic systems deployed in that year (Percentages in a ring sum
to more than 100% when activities are classified in multiple places, but these double
counts are removed at subsequent higher levels.).
as before, we interpret these measures of robotic system concentrations as a rough
indicator of theAI applicabilityfor each type of activity.
Are robotic systems used most for thinking, doing, or interacting?
Not surprisingly, the overwhelming majority of robot deployments (89%) fall under
the “Act on physical objects (‘Do’)” category. This finding is consistent with the
defining characteristic of robots: their embodiment and operation within the physical
environment. The most common activity in the “Do” branch by far is “Clean floor,”
due, in large part, to the fact that 76.7% of all 2024 robots deployments were low cost
floor-cleaning robots. 11% of robotic system deployments are classified under “Act
14

with other activities and actors (‘Interact’).” And 2% of these systems are classified
under both the “Think” and “Interact” ontology branches because they teach people
or provide navigational guidance to people in public places, activities that involved
both cognitive and interactive tasks.
Because the category “Clean floor” contains an exceptionally large number of
robots, it exerts a disproportionate influence on the aggregate results. To reduce
the influence of this factor, we re-examined the distribution of robotic activities
after excluding this category. Figure G14 shows that, once floor-cleaning robots are
removed, the activity distribution becomes nearly balanced between “Do” (55%) and
“Interact” (45%).
In what activities are robots used most?
Figure 10 shows the 20 most prevalent activities performed by robots, after “Clean
floor” is excluded. The most popular activities outside of “Clean floor” which accounts
for 76.7% of total installations are “Clean windows” (5.8%), “Care for lawn” (5.8%),
and “Clean yard” (5.3%). All of the top four activities are types of “Do,” and they
are all performed by service robots in less-structured environments potentially among
humans.
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓✓
“Think”“Interact”“Do”
Fig. 10:T op 20 robotic activities in 2024(excluding “Clean floor” robots, which
account for 76.7% of total installations).
15

Interestingly, the next most popular activities are “Interact client,” “Teach
(Actor),” and “Provide companionship.” These activities all fall under “Interact,”
and collectively, they account for almost 3% of robot installations. These activities
are physically situated and socially embedded and require advanced systems of social
intelligence. In other words, although some of those activities, such as “Teach,” are
commonly performed by AI software applications, social robots attempt to improve
the effectiveness of the AI systems with the use of additional modalities, physical
social presence, and affective engagement, which are important for activities such as
teaching.
Lastly, 12 out of the 14 remaining activities on the list are, again, classified under
“Do.” They include “Transport (Physical Object)”—primarily due to scale deployment
of robots in warehouses—“Weld metal,” and “Fabricate panel.” These activities are
all performed by robots in well-structured environments.
2.3.2 How have uses of robotic systems evolved?
As with AI software applications, we conducted a longitudinal study of how uses of
robotic systems have evolved over time. In this case, however, the IFR data available
aboutnumbersof robots deployed for each type of activity was not sampled in a
way to make it directly comparable across years [11]. Instead, only the cross-sectional
proportionsof robots in different activities were comparable across years.
Accordingly, Figure 11 shows the changes between 2015 and 2024 in the pro-
portionaldistributionsof robot installations across the different types of activities
defined in our ontology. Fortunately, the IFR uses a relatively consistent taxonomy
for different types of robots over time, and when necessary to ensure consistency, we
implemented small classification adjustments. For example, we consolidated the orig-
inally fine-grained agricultural subclasses (e.g., broad acre, greenhouse, fruit-growing,
vineyard) into a single category, “Cultivation.”
But perhaps the most surprising aspect of this figure is how little the distribution
across activities changed over the 10 year period shown. In the AI software applications
shown in Figures 7 and 8, the number of activities for which software applications are
used more than doubled in the two-year period from 2022 to 2024. But in the ten-
year period shown in Figure 11, there is relatively little change in which activities use
robots. Some of this is presumably because of stability in the IFR categories used to
classify the robots. But the IFR did change some categories during this period, and
if there had been substantial growth of robot uses in other activities, it seems likely
that IFR would have added some new categories.
In fact, even the distribution of robot use across these activities has had relatively
little change. Most of the activity types changed by only a few percentage points
over the ten-year period. And the largest exception to this was the activity “Modify
physical objects,” which is mainly affected by cleaning robots, and which increased
from approximately 66% in 2015 to approximately 76% in 2024.
So, while the IFR is currently the best source for studying robotic applicability
on work-related activities, our analysis raises the question of why the uses of robots
haven’t yet spread more widely across activities like software applications have and
indicates the need for more nuanced taxonomies of robotic systems.
16

Act: 100%
Act on information
(“Think”): 5%
Act with other activities and actors (“Interact”): 32% Act on physical objects (“Do”): 69%
Createinformation: 0%
Modify
information: 0%
Transfer
information: 5%
Storeinformation: 0%
Transfer between
actors: 32%
Act onactivities: 0.02%
Modify physicalobjects: 67%
Create physicalobjects: 1%
Store physical
objects: 0%
Transfer physical
objects: 0.3%
Plan: 0%
Analyze: 0%
Decide: 0%Calculate: 0% Express information: 0% Assemble information: 0% Reason: 0% Create information -- other: 0% Solve: 0%
Transform information: 0% Com bine inform
ation: 0%
Separate information: 0% Move information: 0%Exchange information: 5%
Get information: 0.08%Provide information: 0% Communicate (transfer information end-to-end): 0% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 23%
Buy: 0%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 5%
Transfer service: 3%
Transfer physical objects: 0.3%
Interact: 0.01%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0%
Communicate (transfer information end-to-end): 0%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0% W ithhold: 0%
Perform
 (action): 0.02%
Improve: 0%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0% Pass (achieve): 0% Undertake: 0% Transform physical objects: 65%
Separate physical objects: 0.05%
Combine physical objects: 2%
Move physical objects: 0.4%
Assemble: 0.8%
Fabricate: 0.2%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 0.3%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0%
Outline: 0%
Plan -- other: 0%
Propose: 0%
Schedule: 0%
Stage: 0%
 Analyze -- other: 0%
Characterize: 0%
 Correlate: 0%
 Determine: 0%
 Experiment: 0%
 Investigate: 0%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0%
 Reject: 0%
 Rule: 0%
 Select: 0%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0%
 Count: 0%
 Estimate: 0%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0%
 Record: 0%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0%
 Reason -- other: 0%
 Create (Activity): 0%
 Create (Actor): 0%
Create (Information): 0%
 Address (solve): 0%
 Resolve: 0%
Solve -- other: 0%
Adjust (information): 0%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 0%
Organize (analytically): 0%
 Perm
ute: 0%
Prepare (inform
ation): 0%
Process (inform
ation): 0%
Renew (inform
ation): 0%
Revise: 0%
 Service (inform
ation): 0%
Switch: 0%
 Transform
 inform
ation -- other: 0%
Translate: 0%
 Use: 0%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0%
Gather (inform
ation): 0%
Incorporate (inform
ation): 0%
Pack (together) (information): 0%
 Synthesize (information): 0%
 Break (into components): 0%
 Cut (information): 0%
 Disconnect (information): 0%
 Remove (information): 0%
 Separate information -- other: 0%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 0%
 Correspond: 0%
 Debate: 0%
 Exchange information -- other: 0%
 Interview: 0%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0%
 Network: 0%
 Reach: 0%
 Teach: 5%
 Access: 0%
 Download: 0%
 Evaluate: 0.06%
 Gather (information): 0%
 Get information -- other: 0%
 Import: 0%
 Learn: 0%
 Perceive: 0.01%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0%
 Provide decision: 0%
 Provide money: 0%
 Send information: 0%
 Communicate (transfer information end-to-end) -- other: 0%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 23%
Ticket: 0%
Buy -- other: 0%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 0%
Exchange information: 5%
Get information: 0.08%
Provide information: 0%
End service: 0%
Exchange service: 0%
Get service: 0.9%
Provide service: 2%
Exchange physical objects: 0%
Get physical objects: 0.3%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0.01%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 0%
 Conduct: 0%
 M
ake: 0%
Perform
 (action) -- other: 0.02%
Practice: 0%
 Rehearse: 0%
 Run (perform
): 0%
Im
prove -- other: 0%
Optim
ize: 0%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0.08%
 Clean (physical): 65%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0%
Process (physical): 0.01%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0.05%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
Cut (physical): 0.02%
 Disassemble: 0%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0.03%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 1%
 Consolidate: 0%
 Cover: 0.1%
Enclose: 0.5%
Gather (physical): 0.3%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0.2%
Reorient physical objects: 0%
Transport physical objects: 0.3%
Assemble -- other: 0.5%
Configure (physical): 0%
Construct (physical): 0.01%
 Copy (physical): 0.4%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0.2%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 0.3%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0%
2015
Act: 100%
Act on information
(“Think”): 6%
Act with other activities and actors (“Interact”): 34% Act on physical objects (“Do”): 67%
Createinformation: 0%
Modify
information: 0%
Transfer
information: 6%
Storeinformation: 0%
Transfer between
actors: 33%
Act onactivities: 0.02%
Modify physicalobjects: 66%
Create physicalobjects: 1%
Store physical
objects: 0%
Transfer physical
objects: 0.3%
Plan: 0%
Analyze: 0%
Decide: 0%Calculate: 0% Express information: 0% Assemble information: 0% Reason: 0% Create information -- other: 0% Solve: 0%
Transform information: 0% Com bine inform
ation: 0%
Separate information: 0% Move information: 0%Exchange information: 5%
Get information: 0.07%Provide information: 0% Communicate (transfer information end-to-end): 0% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 25%
Buy: 0%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 6%
Transfer service: 3%
Transfer physical objects: 0.3%
Interact: 0.007%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0%
Communicate (transfer information end-to-end): 0%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0% W ithhold: 0%
Perform
 (action): 0.02%
Improve: 0%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0% Pass (achieve): 0% Undertake: 0% Transform physical objects: 63%
Separate physical objects: 0.06%
Combine physical objects: 2%
Move physical objects: 0.5%
Assemble: 0.8%
Fabricate: 0.3%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 0.3%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0%
Outline: 0%
Plan -- other: 0%
Propose: 0%
Schedule: 0%
Stage: 0%
 Analyze -- other: 0%
Characterize: 0%
 Correlate: 0%
 Determine: 0%
 Experiment: 0%
 Investigate: 0%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0%
 Reject: 0%
 Rule: 0%
 Select: 0%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0%
 Count: 0%
 Estimate: 0%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0%
 Record: 0%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0%
 Reason -- other: 0%
 Create (Activity): 0%
 Create (Actor): 0%
Create (Information): 0%
 Address (solve): 0%
 Resolve: 0%
Solve -- other: 0%
Adjust (information): 0%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 0%
Organize (analytically): 0%
 Perm
ute: 0%
Prepare (inform
ation): 0%
Process (inform
ation): 0%
Renew (inform
ation): 0%
Revise: 0%
 Service (inform
ation): 0%
Switch: 0%
 Transform
 inform
ation -- other: 0%
Translate: 0%
 Use: 0%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0%
Gather (inform
ation): 0%
Incorporate (inform
ation): 0%
Pack (together) (information): 0%
 Synthesize (information): 0%
 Break (into components): 0%
 Cut (information): 0%
 Disconnect (information): 0%
 Remove (information): 0%
 Separate information -- other: 0%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 0%
 Correspond: 0%
 Debate: 0%
 Exchange information -- other: 0%
 Interview: 0%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0%
 Network: 0%
 Reach: 0%
 Teach: 5%
 Access: 0%
 Download: 0%
 Evaluate: 0.06%
 Gather (information): 0%
 Get information -- other: 0%
 Import: 0%
 Learn: 0%
 Perceive: 0.01%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0%
 Provide decision: 0%
 Provide money: 0%
 Send information: 0%
 Communicate (transfer information end-to-end) -- other: 0%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 25%
Ticket: 0%
Buy -- other: 0%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 0%
Exchange information: 5%
Get information: 0.07%
Provide information: 0%
End service: 0%
Exchange service: 0%
Get service: 0.9%
Provide service: 2%
Exchange physical objects: 0%
Get physical objects: 0.3%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0.007%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 0%
 Conduct: 0.002%
 M
ake: 0%
Perform
 (action) -- other: 0.02%
Practice: 0%
 Rehearse: 0%
 Run (perform
): 0%
Im
prove -- other: 0%
Optim
ize: 0%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0.07%
 Clean (physical): 63%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 6e-05%
 Process (physical): 0.01%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0.04%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
Cut (physical): 0.02%
Disassemble: 0.004%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0.04%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 1%
 Consolidate: 0%
 Cover: 0.1%
Enclose: 0.5%
Gather (physical): 0.3%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0.2%
Reorient physical objects: 0%
Transport physical objects: 0.3%
Assemble -- other: 0.4%
Configure (physical): 0%
Construct (physical): 0.01%
 Copy (physical): 0.4%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0.3%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 0.3%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0% 2016
Act: 100%
Act on information
(“Think”): 6%
Act with other activities and actors (“Interact”): 34% Act on physical objects (“Do”): 66%
Createinformation: 0%
Modify
information: 0%
Transfer
information: 6%
Storeinformation: 0%
Transfer between
actors: 34%
Act onactivities: 0.02%
Modify physicalobjects: 65%
Create physicalobjects: 1%
Store physical
objects: 0%
Transfer physical
objects: 0.3%
Plan: 0%
Analyze: 0%
Decide: 0%Calculate: 0% Express information: 0% Assemble information: 0% Reason: 0% Create information -- other: 0% Solve: 0%
Transform information: 0% Com bine inform
ation: 0%
Separate information: 0% Move information: 0%Exchange information: 6%
Get information: 0.07%Provide information: 0% Communicate (transfer information end-to-end): 0% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 25%
Buy: 0%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 6%
Transfer service: 3%
Transfer physical objects: 0.3%
Interact: 0.006%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0%
Communicate (transfer information end-to-end): 0%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0% W ithhold: 0%
Perform
 (action): 0.02%
Improve: 0%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0% Pass (achieve): 0% Undertake: 0% Transform physical objects: 62%
Separate physical objects: 0.05%
Combine physical objects: 2%
Move physical objects: 0.5%
Assemble: 0.8%
Fabricate: 0.3%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 0.3%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0%
Outline: 0%
Plan -- other: 0%
Propose: 0%
Schedule: 0%
Stage: 0%
 Analyze -- other: 0%
Characterize: 0%
 Correlate: 0%
 Determine: 0%
 Experiment: 0%
 Investigate: 0%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0%
 Reject: 0%
 Rule: 0%
 Select: 0%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0%
 Count: 0%
 Estimate: 0%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0%
 Record: 0%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0%
 Reason -- other: 0%
 Create (Activity): 0%
 Create (Actor): 0%
Create (Information): 0%
 Address (solve): 0%
 Resolve: 0%
Solve -- other: 0%
Adjust (information): 0%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 0%
Organize (analytically): 0%
 Perm
ute: 0%
Prepare (inform
ation): 0%
Process (inform
ation): 0%
Renew (inform
ation): 0%
Revise: 0%
 Service (inform
ation): 0%
Switch: 0%
 Transform
 inform
ation -- other: 0%
Translate: 0%
 Use: 0%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0%
Gather (inform
ation): 0%
Incorporate (inform
ation): 0%
Pack (together) (information): 0%
 Synthesize (information): 0%
 Break (into components): 0%
 Cut (information): 0%
 Disconnect (information): 0%
 Remove (information): 0%
 Separate information -- other: 0%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 0%
 Correspond: 0%
 Debate: 0%
 Exchange information -- other: 0%
 Interview: 0%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0%
 Network: 0%
 Reach: 0%
 Teach: 6%
 Access: 0%
 Download: 0%
 Evaluate: 0.05%
 Gather (information): 0%
 Get information -- other: 0%
 Import: 0%
 Learn: 0%
 Perceive: 0.01%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0%
 Provide decision: 0%
 Provide money: 0%
 Send information: 0%
 Communicate (transfer information end-to-end) -- other: 0%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 25%
Ticket: 0%
Buy -- other: 0%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 0%
Exchange information: 6%
Get information: 0.07%
Provide information: 0%
End service: 0%
Exchange service: 0%
Get service: 0.9%
Provide service: 2%
Exchange physical objects: 0%
Get physical objects: 0.3%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0.006%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 0%
 Conduct: 0.002%
 M
ake: 0%
Perform
 (action) -- other: 0.02%
Practice: 0%
 Rehearse: 0%
 Run (perform
): 0%
Im
prove -- other: 0%
Optim
ize: 0%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0.05%
 Clean (physical): 62%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0.0009%
 Process (physical): 0.01%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0.04%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
Cut (physical): 0.01%
Disassemble: 0.003%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0.03%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 1%
 Consolidate: 0%
 Cover: 0.1%
Enclose: 0.5%
Gather (physical): 0.3%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0.2%
Reorient physical objects: 0%
Transport physical objects: 0.3%
Assemble -- other: 0.5%
Configure (physical): 0%
Construct (physical): 0.01%
 Copy (physical): 0.3%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0.3%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 0.3%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0% 2017
Act: 100%
Act on information
(“Think”): 5%
Act with other activities and actors (“Interact”): 43% Act on physical objects (“Do”): 64%
Createinformation: 0%
Modify
information: 0%
Transfer
information: 5%
Storeinformation: 0%
Transfer between
actors: 37%
Act onactivities: 6%
Modify physicalobjects: 63%
Create physicalobjects: 1.0%
Store physical
objects: 0%
Transfer physical
objects: 8%
Plan: 0%
Analyze: 0%
Decide: 0%Calculate: 0% Express information: 0% Assemble information: 0% Reason: 0% Create information -- other: 0% Solve: 0%
Transform information: 0% Com bine inform
ation: 0%
Separate information: 0% Move information: 0%Exchange information: 5%
Get information: 0.8%Provide information: 0% Communicate (transfer information end-to-end): 0% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 22%
Buy: 0%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 5%
Transfer service: 3%
Transfer physical objects: 8%
Interact: 0.003%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0%
Communicate (transfer information end-to-end): 0%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0% W ithhold: 0%
Perform
 (action): 6%
Improve: 0%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0% Pass (achieve): 0% Undertake: 0% Transform physical objects: 48%
Separate physical objects: 0.03%
Combine physical objects: 9%
Move physical objects: 7%
Assemble: 0.7%
Fabricate: 0.2%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 8%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0%
Outline: 0%
Plan -- other: 0%
Propose: 0%
Schedule: 0%
Stage: 0%
 Analyze -- other: 0%
Characterize: 0%
 Correlate: 0%
 Determine: 0%
 Experiment: 0%
 Investigate: 0%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0%
 Reject: 0%
 Rule: 0%
 Select: 0%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0%
 Count: 0%
 Estimate: 0%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0%
 Record: 0%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0%
 Reason -- other: 0%
 Create (Activity): 0%
 Create (Actor): 0%
Create (Information): 0%
 Address (solve): 0%
 Resolve: 0%
Solve -- other: 0%
Adjust (information): 0%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 0%
Organize (analytically): 0%
 Perm
ute: 0%
Prepare (inform
ation): 0%
Process (inform
ation): 0%
Renew (inform
ation): 0%
Revise: 0%
 Service (inform
ation): 0%
Switch: 0%
 Transform
 inform
ation -- other: 0%
Translate: 0%
 Use: 0%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0%
Gather (inform
ation): 0%
Incorporate (inform
ation): 0%
Pack (together) (information): 0%
 Synthesize (information): 0%
 Break (into components): 0%
 Cut (information): 0%
 Disconnect (information): 0%
 Remove (information): 0%
 Separate information -- other: 0%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 0%
 Correspond: 0%
 Debate: 0%
 Exchange information -- other: 0%
 Interview: 0%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0%
 Network: 0%
 Reach: 0%
 Teach: 5%
 Access: 0%
 Download: 0%
 Evaluate: 0.05%
 Gather (information): 0%
 Get information -- other: 0%
 Import: 0%
 Learn: 0%
 Perceive: 0.7%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0%
 Provide decision: 0%
 Provide money: 0%
 Send information: 0%
 Communicate (transfer information end-to-end) -- other: 0%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 22%
Ticket: 0%
Buy -- other: 0%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 0%
Exchange information: 5%
Get information: 0.8%
Provide information: 0%
End service: 0%
Exchange service: 0%
Get service: 1%
Provide service: 1%
Exchange physical objects: 0%
Get physical objects: 8%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0.003%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 0%
 Conduct: 0.06%
 M
ake: 0%
Perform
 (action) -- other: 6%
Practice: 0%
 Rehearse: 0%
 Run (perform
): 0%
Im
prove -- other: 0%
Optim
ize: 0%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0.04%
 Clean (physical): 48%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0.009%
 Process (physical): 0.01%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0.03%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
Cut (physical): 0.009%
 Disassemble: 0.001%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0.02%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0.7%
 Consolidate: 0%
 Cover: 0.09%
Enclose: 0.3%
Gather (physical): 8%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0.1%
Reorient physical objects: 0%
Transport physical objects: 7%
Assemble -- other: 0.4%
Configure (physical): 0%
Construct (physical): 0.2%
 Copy (physical): 0.2%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0.2%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 8%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0% 2018
Act: 100%
Act on information
(“Think”): 5%
Act with other activities and actors (“Interact”): 39% Act on physical objects (“Do”): 66%
Createinformation: 0%
Modify
information: 0%
Transfer
information: 5%
Storeinformation: 0%
Transfer between
actors: 35%
Act onactivities: 4%
Modify physicalobjects: 65%
Create physicalobjects: 0.8%
Store physical
objects: 0%
Transfer physical
objects: 5%
Plan: 0%
Analyze: 0%
Decide: 0%Calculate: 0% Express information: 0% Assemble information: 0% Reason: 0% Create information -- other: 0% Solve: 0%
Transform information: 0% Com bine inform
ation: 0%
Separate information: 0% Move information: 0%Exchange information: 4%
Get information: 0.6%Provide information: 0% Communicate (transfer information end-to-end): 0% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 21%
Buy: 0%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 5%
Transfer service: 3%
Transfer physical objects: 5%
Interact: 0.003%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0%
Communicate (transfer information end-to-end): 0%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0% W ithhold: 0%
Perform
 (action): 4%
Improve: 0%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0% Pass (achieve): 0% Undertake: 0% Transform physical objects: 54%
Separate physical objects: 0.02%
Combine physical objects: 6%
Move physical objects: 5%
Assemble: 0.6%
Fabricate: 0.2%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 5%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0%
Outline: 0%
Plan -- other: 0%
Propose: 0%
Schedule: 0%
Stage: 0%
 Analyze -- other: 0%
Characterize: 0%
 Correlate: 0%
 Determine: 0%
 Experiment: 0%
 Investigate: 0%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0%
 Reject: 0%
 Rule: 0%
 Select: 0%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0%
 Count: 0%
 Estimate: 0%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0%
 Record: 0%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0%
 Reason -- other: 0%
 Create (Activity): 0%
 Create (Actor): 0%
Create (Information): 0%
 Address (solve): 0%
 Resolve: 0%
Solve -- other: 0%
Adjust (information): 0%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 0%
Organize (analytically): 0%
 Perm
ute: 0%
Prepare (inform
ation): 0%
Process (inform
ation): 0%
Renew (inform
ation): 0%
Revise: 0%
 Service (inform
ation): 0%
Switch: 0%
 Transform
 inform
ation -- other: 0%
Translate: 0%
 Use: 0%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0%
Gather (inform
ation): 0%
Incorporate (inform
ation): 0%
Pack (together) (information): 0%
 Synthesize (information): 0%
 Break (into components): 0%
 Cut (information): 0%
 Disconnect (information): 0%
 Remove (information): 0%
 Separate information -- other: 0%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 0%
 Correspond: 0%
 Debate: 0%
 Exchange information -- other: 0%
 Interview: 0%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0%
 Network: 0%
 Reach: 0%
 Teach: 4%
 Access: 0%
 Download: 0%
 Evaluate: 0.05%
 Gather (information): 0%
 Get information -- other: 0%
 Import: 0%
 Learn: 0%
 Perceive: 0.5%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0%
 Provide decision: 0%
 Provide money: 0%
 Send information: 0%
 Communicate (transfer information end-to-end) -- other: 0%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 21%
Ticket: 0%
Buy -- other: 0%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 0%
Exchange information: 4%
Get information: 0.6%
Provide information: 0%
End service: 0%
Exchange service: 0%
Get service: 0.9%
Provide service: 2%
Exchange physical objects: 0%
Get physical objects: 5%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0.003%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 0%
 Conduct: 0.04%
 M
ake: 0%
Perform
 (action) -- other: 4%
Practice: 0%
 Rehearse: 0%
 Run (perform
): 0%
Im
prove -- other: 0%
Optim
ize: 0%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0.03%
 Clean (physical): 54%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0.006%
 Process (physical): 0.01%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0.03%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
Cut (physical): 0.008%
 Disassemble: 0.002%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0.01%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0.6%
 Consolidate: 0%
 Cover: 0.08%
Enclose: 0.3%
Gather (physical): 5%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0.1%
Reorient physical objects: 0%
Transport physical objects: 5%
Assemble -- other: 0.3%
Configure (physical): 0%
Construct (physical): 0.1%
 Copy (physical): 0.2%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0.2%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 5%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0% 2019
Act: 100%
Act on information
(“Think”): 4%
Act with other activities and actors (“Interact”): 32% Act on physical objects (“Do”): 72%
Createinformation: 0%
Modify
information: 0%
Transfer
information: 4%
Storeinformation: 0%
Transfer between
actors: 29%
Act onactivities: 3%
Modify physicalobjects: 71%
Create physicalobjects: 0.7%
Store physical
objects: 0%
Transfer physical
objects: 4%
Plan: 0%
Analyze: 0%
Decide: 0%Calculate: 0% Express information: 0% Assemble information: 0% Reason: 0% Create information -- other: 0% Solve: 0%
Transform information: 0% Com bine inform
ation: 0%
Separate information: 0% Move information: 0%Exchange information: 4%
Get information: 0.4%Provide information: 0% Communicate (transfer information end-to-end): 0% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 17%
Buy: 0%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 4%
Transfer service: 4%
Transfer physical objects: 4%
Interact: 0.003%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0%
Communicate (transfer information end-to-end): 0%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0% W ithhold: 0%
Perform
 (action): 3%
Improve: 0%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0% Pass (achieve): 0% Undertake: 0% Transform physical objects: 63%
Separate physical objects: 0.02%
Combine physical objects: 5%
Move physical objects: 4%
Assemble: 0.5%
Fabricate: 0.2%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 4%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0%
Outline: 0%
Plan -- other: 0%
Propose: 0%
Schedule: 0%
Stage: 0%
 Analyze -- other: 0%
Characterize: 0%
 Correlate: 0%
 Determine: 0%
 Experiment: 0%
 Investigate: 0%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0%
 Reject: 0%
 Rule: 0%
 Select: 0%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0%
 Count: 0%
 Estimate: 0%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0%
 Record: 0%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0%
 Reason -- other: 0%
 Create (Activity): 0%
 Create (Actor): 0%
Create (Information): 0%
 Address (solve): 0%
 Resolve: 0%
Solve -- other: 0%
Adjust (information): 0%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 0%
Organize (analytically): 0%
 Perm
ute: 0%
Prepare (inform
ation): 0%
Process (inform
ation): 0%
Renew (inform
ation): 0%
Revise: 0%
 Service (inform
ation): 0%
Switch: 0%
 Transform
 inform
ation -- other: 0%
Translate: 0%
 Use: 0%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0%
Gather (inform
ation): 0%
Incorporate (inform
ation): 0%
Pack (together) (information): 0%
 Synthesize (information): 0%
 Break (into components): 0%
 Cut (information): 0%
 Disconnect (information): 0%
 Remove (information): 0%
 Separate information -- other: 0%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 0%
 Correspond: 0%
 Debate: 0%
 Exchange information -- other: 0%
 Interview: 0%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0%
 Network: 0%
 Reach: 0%
 Teach: 4%
 Access: 0%
 Download: 0%
 Evaluate: 0.04%
 Gather (information): 0%
 Get information -- other: 0%
 Import: 0%
 Learn: 0%
 Perceive: 0.4%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0%
 Provide decision: 0%
 Provide money: 0%
 Send information: 0%
 Communicate (transfer information end-to-end) -- other: 0%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 17%
Ticket: 0%
Buy -- other: 0%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 0%
Exchange information: 4%
Get information: 0.4%
Provide information: 0%
End service: 0%
Exchange service: 0%
Get service: 0.8%
Provide service: 3%
Exchange physical objects: 0%
Get physical objects: 4%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0.003%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 0%
 Conduct: 0.03%
 M
ake: 0%
Perform
 (action) -- other: 3%
Practice: 0%
 Rehearse: 0%
 Run (perform
): 0%
Im
prove -- other: 0%
Optim
ize: 0%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0.03%
 Clean (physical): 63%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0.006%
 Process (physical): 0.01%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0.02%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
Cut (physical): 0.007%
 Disassemble: 0.002%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0.01%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0.6%
 Consolidate: 0%
 Cover: 0.07%
Enclose: 0.2%
Gather (physical): 4%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0.1%
Reorient physical objects: 0%
Transport physical objects: 3%
Assemble -- other: 0.3%
Configure (physical): 0%
Construct (physical): 0.08%
 Copy (physical): 0.2%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0.2%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 4%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0%
2020
Act: 100%
Act on information
(“Think”): 4%
Act with other activities and actors (“Interact”): 28% Act on physical objects (“Do”): 75%
Createinformation: 0%
Modify
information: 0%
Transfer
information: 4%
Storeinformation: 0%
Transfer between
actors: 26%
Act onactivities: 2%
Modify physicalobjects: 74%
Create physicalobjects: 0.7%
Store physical
objects: 0%
Transfer physical
objects: 3%
Plan: 0%
Analyze: 0%
Decide: 0%Calculate: 0% Express information: 0% Assemble information: 0% Reason: 0% Create information -- other: 0% Solve: 0%
Transform information: 0% Com bine inform
ation: 0%
Separate information: 0% Move information: 0%Exchange information: 4%
Get information: 0.4%Provide information: 0% Communicate (transfer information end-to-end): 0% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 14%
Buy: 0%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 4%
Transfer service: 4%
Transfer physical objects: 3%
Interact: 0.002%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0%
Communicate (transfer information end-to-end): 0%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0% W ithhold: 0%
Perform
 (action): 2%
Improve: 0%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0% Pass (achieve): 0% Undertake: 0% Transform physical objects: 67%
Separate physical objects: 0.02%
Combine physical objects: 4%
Move physical objects: 3%
Assemble: 0.5%
Fabricate: 0.2%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 3%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0%
Outline: 0%
Plan -- other: 0%
Propose: 0%
Schedule: 0%
Stage: 0%
 Analyze -- other: 0%
Characterize: 0%
 Correlate: 0%
 Determine: 0%
 Experiment: 0%
 Investigate: 0%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0%
 Reject: 0%
 Rule: 0%
 Select: 0%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0%
 Count: 0%
 Estimate: 0%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0%
 Record: 0%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0%
 Reason -- other: 0%
 Create (Activity): 0%
 Create (Actor): 0%
Create (Information): 0%
 Address (solve): 0%
 Resolve: 0%
Solve -- other: 0%
Adjust (information): 0%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 0%
Organize (analytically): 0%
 Perm
ute: 0%
Prepare (inform
ation): 0%
Process (inform
ation): 0%
Renew (inform
ation): 0%
Revise: 0%
 Service (inform
ation): 0%
Switch: 0%
 Transform
 inform
ation -- other: 0%
Translate: 0%
 Use: 0%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0%
Gather (inform
ation): 0%
Incorporate (inform
ation): 0%
Pack (together) (information): 0%
 Synthesize (information): 0%
 Break (into components): 0%
 Cut (information): 0%
 Disconnect (information): 0%
 Remove (information): 0%
 Separate information -- other: 0%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 0%
 Correspond: 0%
 Debate: 0%
 Exchange information -- other: 0%
 Interview: 0%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0%
 Network: 0%
 Reach: 0%
 Teach: 4%
 Access: 0%
 Download: 0%
 Evaluate: 0.04%
 Gather (information): 0%
 Get information -- other: 0%
 Import: 0%
 Learn: 0%
 Perceive: 0.3%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0%
 Provide decision: 0%
 Provide money: 0%
 Send information: 0%
 Communicate (transfer information end-to-end) -- other: 0%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 14%
Ticket: 0%
Buy -- other: 0%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 0%
Exchange information: 4%
Get information: 0.4%
Provide information: 0%
End service: 0%
Exchange service: 0%
Get service: 0.8%
Provide service: 4%
Exchange physical objects: 0%
Get physical objects: 3%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0.002%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 0%
 Conduct: 0.03%
 M
ake: 0%
Perform
 (action) -- other: 2%
Practice: 0%
 Rehearse: 0%
 Run (perform
): 0%
Im
prove -- other: 0%
Optim
ize: 0%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0.02%
 Clean (physical): 67%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0.006%
 Process (physical): 0.009%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0.02%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
Cut (physical): 0.007%
 Disassemble: 0.002%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0.01%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0.5%
 Consolidate: 0%
 Cover: 0.07%
Enclose: 0.2%
Gather (physical): 3%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0.1%
Reorient physical objects: 0%
Transport physical objects: 3%
Assemble -- other: 0.3%
Configure (physical): 0%
Construct (physical): 0.07%
 Copy (physical): 0.2%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0.2%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 3%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0% 2021
Act: 100%
Act on information
(“Think”): 4%
Act with other activities and actors (“Interact”): 28% Act on physical objects (“Do”): 75%
Createinformation: 0%
Modify
information: 0%
Transfer
information: 4%
Storeinformation: 0%
Transfer between
actors: 26%
Act onactivities: 2%
Modify physicalobjects: 74%
Create physicalobjects: 0.8%
Store physical
objects: 0%
Transfer physical
objects: 3%
Plan: 0%
Analyze: 0%
Decide: 0%Calculate: 0% Express information: 0% Assemble information: 0% Reason: 0% Create information -- other: 0% Solve: 0%
Transform information: 0% Com bine inform
ation: 0%
Separate information: 0% Move information: 0%Exchange information: 4%
Get information: 0.4%Provide information: 0% Communicate (transfer information end-to-end): 0% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 13%
Buy: 0%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 4%
Transfer service: 5%
Transfer physical objects: 3%
Interact: 0.002%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0%
Communicate (transfer information end-to-end): 0%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0% W ithhold: 0%
Perform
 (action): 2%
Improve: 0%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0% Pass (achieve): 0% Undertake: 0% Transform physical objects: 67%
Separate physical objects: 0.02%
Combine physical objects: 4%
Move physical objects: 3%
Assemble: 0.5%
Fabricate: 0.2%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 3%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0%
Outline: 0%
Plan -- other: 0%
Propose: 0%
Schedule: 0%
Stage: 0%
 Analyze -- other: 0%
Characterize: 0%
 Correlate: 0%
 Determine: 0%
 Experiment: 0%
 Investigate: 0%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0%
 Reject: 0%
 Rule: 0%
 Select: 0%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0%
 Count: 0%
 Estimate: 0%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0%
 Record: 0%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0%
 Reason -- other: 0%
 Create (Activity): 0%
 Create (Actor): 0%
Create (Information): 0%
 Address (solve): 0%
 Resolve: 0%
Solve -- other: 0%
Adjust (information): 0%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 0%
Organize (analytically): 0%
 Perm
ute: 0%
Prepare (inform
ation): 0%
Process (inform
ation): 0%
Renew (inform
ation): 0%
Revise: 0%
 Service (inform
ation): 0%
Switch: 0%
 Transform
 inform
ation -- other: 0%
Translate: 0%
 Use: 0%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0%
Gather (inform
ation): 0%
Incorporate (inform
ation): 0%
Pack (together) (information): 0%
 Synthesize (information): 0%
 Break (into components): 0%
 Cut (information): 0%
 Disconnect (information): 0%
 Remove (information): 0%
 Separate information -- other: 0%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 0%
 Correspond: 0%
 Debate: 0%
 Exchange information -- other: 0%
 Interview: 0%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0%
 Network: 0%
 Reach: 0%
 Teach: 4%
 Access: 0%
 Download: 0%
 Evaluate: 0.06%
 Gather (information): 0%
 Get information -- other: 0%
 Import: 0%
 Learn: 0%
 Perceive: 0.3%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0%
 Provide decision: 0%
 Provide money: 0%
 Send information: 0%
 Communicate (transfer information end-to-end) -- other: 0%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 13%
Ticket: 0%
Buy -- other: 0%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 0%
Exchange information: 4%
Get information: 0.4%
Provide information: 0%
End service: 0%
Exchange service: 0%
Get service: 0.8%
Provide service: 5%
Exchange physical objects: 0%
Get physical objects: 3%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0.002%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 0%
 Conduct: 0.03%
 M
ake: 0%
Perform
 (action) -- other: 2%
Practice: 0%
 Rehearse: 0%
 Run (perform
): 0%
Im
prove -- other: 0%
Optim
ize: 0%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0.03%
 Clean (physical): 67%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0.01%
 Process (physical): 0.01%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0.03%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
Cut (physical): 0.008%
 Disassemble: 0.004%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0.01%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0.6%
 Consolidate: 0%
 Cover: 0.07%
Enclose: 0.3%
Gather (physical): 3%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0.1%
Reorient physical objects: 0%
Transport physical objects: 3%
Assemble -- other: 0.3%
Configure (physical): 0%
Construct (physical): 0.06%
 Copy (physical): 0.2%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0.2%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 3%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0% 2022
Act: 100%
Act on information
(“Think”): 4%
Act with other activities and actors (“Interact”): 28% Act on physical objects (“Do”): 75%
Createinformation: 0%
Modify
information: 0%
Transfer
information: 4%
Storeinformation: 0%
Transfer between
actors: 26%
Act onactivities: 2%
Modify physicalobjects: 74%
Create physicalobjects: 0.8%
Store physical
objects: 0%
Transfer physical
objects: 3%
Plan: 0%
Analyze: 0%
Decide: 0%Calculate: 0% Express information: 0% Assemble information: 0% Reason: 0% Create information -- other: 0% Solve: 0%
Transform information: 0% Com bine inform
ation: 0%
Separate information: 0% Move information: 0%Exchange information: 4%
Get information: 0.4%Provide information: 0% Communicate (transfer information end-to-end): 0% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 12%
Buy: 0%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 4%
Transfer service: 6%
Transfer physical objects: 3%
Interact: 0.01%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0%
Communicate (transfer information end-to-end): 0%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0% W ithhold: 0%
Perform
 (action): 2%
Improve: 0%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0% Pass (achieve): 0% Undertake: 0% Transform physical objects: 67%
Separate physical objects: 0.03%
Combine physical objects: 4%
Move physical objects: 3%
Assemble: 0.6%
Fabricate: 0.2%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 3%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0%
Outline: 0%
Plan -- other: 0%
Propose: 0%
Schedule: 0%
Stage: 0%
 Analyze -- other: 0%
Characterize: 0%
 Correlate: 0%
 Determine: 0%
 Experiment: 0%
 Investigate: 0%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0%
 Reject: 0%
 Rule: 0%
 Select: 0%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0%
 Count: 0%
 Estimate: 0%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0%
 Record: 0%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0%
 Reason -- other: 0%
 Create (Activity): 0%
 Create (Actor): 0%
Create (Information): 0%
 Address (solve): 0%
 Resolve: 0%
Solve -- other: 0%
Adjust (information): 0%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 0%
Organize (analytically): 0%
 Perm
ute: 0%
Prepare (inform
ation): 0%
Process (inform
ation): 0%
Renew (inform
ation): 0%
Revise: 0%
 Service (inform
ation): 0%
Switch: 0%
 Transform
 inform
ation -- other: 0%
Translate: 0%
 Use: 0%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0%
Gather (inform
ation): 0%
Incorporate (inform
ation): 0%
Pack (together) (information): 0%
 Synthesize (information): 0%
 Break (into components): 0%
 Cut (information): 0%
 Disconnect (information): 0%
 Remove (information): 0%
 Separate information -- other: 0%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 0%
 Correspond: 0%
 Debate: 0%
 Exchange information -- other: 0%
 Interview: 0%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0%
 Network: 0%
 Reach: 0%
 Teach: 4%
 Access: 0%
 Download: 0%
 Evaluate: 0.07%
 Gather (information): 0%
 Get information -- other: 0%
 Import: 0%
 Learn: 0%
 Perceive: 0.3%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0%
 Provide decision: 0%
 Provide money: 0%
 Send information: 0%
 Communicate (transfer information end-to-end) -- other: 0%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 12%
Ticket: 0%
Buy -- other: 0%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 0%
Exchange information: 4%
Get information: 0.4%
Provide information: 0%
End service: 0%
Exchange service: 0%
Get service: 0.9%
Provide service: 5%
Exchange physical objects: 0%
Get physical objects: 3%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0.01%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 0%
 Conduct: 0.03%
 M
ake: 0%
Perform
 (action) -- other: 2%
Practice: 0%
 Rehearse: 0%
 Run (perform
): 0%
Im
prove -- other: 0%
Optim
ize: 0%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0.03%
 Clean (physical): 67%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0.02%
 Process (physical): 0.01%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0.04%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
Cut (physical): 0.008%
 Disassemble: 0.007%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0.01%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0.6%
 Consolidate: 0%
 Cover: 0.08%
Enclose: 0.3%
Gather (physical): 3%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0.1%
Reorient physical objects: 0%
Transport physical objects: 3%
Assemble -- other: 0.4%
Configure (physical): 0%
Construct (physical): 0.06%
 Copy (physical): 0.2%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0.2%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 3%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0% 2023
Act: 100%
Act on information
(“Think”): 4%
Act with other activities and actors (“Interact”): 25% Act on physical objects (“Do”): 77%
Createinformation: 0%
Modify
information: 0%
Transfer
information: 4%
Storeinformation: 0%
Transfer between
actors: 23%
Act onactivities: 2%
Modify physicalobjects: 76%
Create physicalobjects: 0.8%
Store physical
objects: 0%
Transfer physical
objects: 2%
Plan: 0%
Analyze: 0%
Decide: 0%Calculate: 0% Express information: 0% Assemble information: 0% Reason: 0% Create information -- other: 0% Solve: 0%
Transform information: 0% Com bine inform
ation: 0%
Separate information: 0% Move information: 0%Exchange information: 3%
Get information: 0.3%Provide information: 0% Communicate (transfer information end-to-end): 0% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 11%
Buy: 0%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 4%
Transfer service: 6%
Transfer physical objects: 2%
Interact: 0.2%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0%
Communicate (transfer information end-to-end): 0%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0% W ithhold: 0%
Perform
 (action): 2%
Improve: 0%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0% Pass (achieve): 0% Undertake: 0% Transform physical objects: 70%
Separate physical objects: 0.03%
Combine physical objects: 3%
Move physical objects: 2%
Assemble: 0.6%
Fabricate: 0.2%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 2%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0%
Outline: 0%
Plan -- other: 0%
Propose: 0%
Schedule: 0%
Stage: 0%
 Analyze -- other: 0%
Characterize: 0%
 Correlate: 0%
 Determine: 0%
 Experiment: 0%
 Investigate: 0%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0%
 Reject: 0%
 Rule: 0%
 Select: 0%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0%
 Count: 0%
 Estimate: 0%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0%
 Record: 0%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0%
 Reason -- other: 0%
 Create (Activity): 0%
 Create (Actor): 0%
Create (Information): 0%
 Address (solve): 0%
 Resolve: 0%
Solve -- other: 0%
Adjust (information): 0%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 0%
Organize (analytically): 0%
 Perm
ute: 0%
Prepare (inform
ation): 0%
Process (inform
ation): 0%
Renew (inform
ation): 0%
Revise: 0%
 Service (inform
ation): 0%
Switch: 0%
 Transform
 inform
ation -- other: 0%
Translate: 0%
 Use: 0%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0%
Gather (inform
ation): 0%
Incorporate (inform
ation): 0%
Pack (together) (information): 0%
 Synthesize (information): 0%
 Break (into components): 0%
 Cut (information): 0%
 Disconnect (information): 0%
 Remove (information): 0%
 Separate information -- other: 0%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 0%
 Correspond: 0%
 Debate: 0%
 Exchange information -- other: 0%
 Interview: 0%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0%
 Network: 0%
 Reach: 0%
 Teach: 3%
 Access: 0%
 Download: 0%
 Evaluate: 0.08%
 Gather (information): 0%
 Get information -- other: 0%
 Import: 0%
 Learn: 0%
 Perceive: 0.3%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0%
 Provide decision: 0%
 Provide money: 0%
 Send information: 0%
 Communicate (transfer information end-to-end) -- other: 0%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 11%
Ticket: 0%
Buy -- other: 0%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 0%
Exchange information: 3%
Get information: 0.3%
Provide information: 0%
End service: 0%
Exchange service: 0%
Get service: 1.0%
Provide service: 5%
Exchange physical objects: 0%
Get physical objects: 2%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0.2%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 0%
 Conduct: 0.03%
 M
ake: 0%
Perform
 (action) -- other: 2%
Practice: 0%
 Rehearse: 0%
 Run (perform
): 0%
Im
prove -- other: 0%
Optim
ize: 0%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0.03%
 Clean (physical): 70%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0.02%
 Process (physical): 0.01%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0.04%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
Cut (physical): 0.007%
 Disassemble: 0.008%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0.01%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0.6%
 Consolidate: 0%
 Cover: 0.08%
Enclose: 0.3%
Gather (physical): 2%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0.1%
Reorient physical objects: 0%
Transport physical objects: 2%
Assemble -- other: 0.3%
Configure (physical): 0%
Construct (physical): 0.05%
 Copy (physical): 0.2%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0.2%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 2%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0% 2024
Act: 100%
Act on information
(“Think”): 4%
Act with other activities and actors (“Interact”): 23% Act on physical objects (“Do”): 79%
Createinformation: 0%
Modify
information: 0%
Transfer
information: 4%
Storeinformation: 0%
Transfer between
actors: 22%
Act onactivities: 2%
Modify physicalobjects: 78%
Create physicalobjects: 0.7%
Store physical
objects: 0%
Transfer physical
objects: 2%
Plan: 0%
Analyze: 0%
Decide: 0%Calculate: 0% Express information: 0% Assemble information: 0% Reason: 0% Create information -- other: 0% Solve: 0%
Transform information: 0% Com bine inform
ation: 0%
Separate information: 0% Move information: 0%Exchange information: 3%
Get information: 0.3%Provide information: 0% Communicate (transfer information end-to-end): 0% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 9%
Buy: 0%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 4%
Transfer service: 6%
Transfer physical objects: 2%
Interact: 0.3%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0%
Communicate (transfer information end-to-end): 0%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0% W ithhold: 0%
Perform
 (action): 2%
Improve: 0%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0% Pass (achieve): 0% Undertake: 0% Transform physical objects: 73%
Separate physical objects: 0.03%
Combine physical objects: 3%
Move physical objects: 2%
Assemble: 0.5%
Fabricate: 0.2%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 2%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0%
Outline: 0%
Plan -- other: 0%
Propose: 0%
Schedule: 0%
Stage: 0%
 Analyze -- other: 0%
Characterize: 0%
 Correlate: 0%
 Determine: 0%
 Experiment: 0%
 Investigate: 0%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0%
 Reject: 0%
 Rule: 0%
 Select: 0%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0%
 Count: 0%
 Estimate: 0%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0%
 Record: 0%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0%
 Reason -- other: 0%
 Create (Activity): 0%
 Create (Actor): 0%
Create (Information): 0%
 Address (solve): 0%
 Resolve: 0%
Solve -- other: 0%
Adjust (information): 0%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 0%
Organize (analytically): 0%
 Perm
ute: 0%
Prepare (inform
ation): 0%
Process (inform
ation): 0%
Renew (inform
ation): 0%
Revise: 0%
 Service (inform
ation): 0%
Switch: 0%
 Transform
 inform
ation -- other: 0%
Translate: 0%
 Use: 0%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0%
Gather (inform
ation): 0%
Incorporate (inform
ation): 0%
Pack (together) (information): 0%
 Synthesize (information): 0%
 Break (into components): 0%
 Cut (information): 0%
 Disconnect (information): 0%
 Remove (information): 0%
 Separate information -- other: 0%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 0%
 Correspond: 0%
 Debate: 0%
 Exchange information -- other: 0%
 Interview: 0%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0%
 Network: 0%
 Reach: 0%
 Teach: 3%
 Access: 0%
 Download: 0%
 Evaluate: 0.08%
 Gather (information): 0%
 Get information -- other: 0%
 Import: 0%
 Learn: 0%
 Perceive: 0.2%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0%
 Provide decision: 0%
 Provide money: 0%
 Send information: 0%
 Communicate (transfer information end-to-end) -- other: 0%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 9%
Ticket: 0%
Buy -- other: 0%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 0%
Exchange information: 3%
Get information: 0.3%
Provide information: 0%
End service: 0%
Exchange service: 0%
Get service: 0.9%
Provide service: 5%
Exchange physical objects: 0%
Get physical objects: 2%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0.3%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 0%
 Conduct: 0.03%
 M
ake: 0%
Perform
 (action) -- other: 2%
Practice: 0%
 Rehearse: 0%
 Run (perform
): 0%
Im
prove -- other: 0%
Optim
ize: 0%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0.03%
 Clean (physical): 72%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0.02%
 Process (physical): 0.01%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0.04%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
Cut (physical): 0.007%
 Disassemble: 0.009%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0.01%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0.6%
 Consolidate: 0%
 Cover: 0.07%
Enclose: 0.3%
Gather (physical): 2%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0.1%
Reorient physical objects: 0%
Transport physical objects: 2%
Assemble -- other: 0.3%
Configure (physical): 0%
Construct (physical): 0.04%
 Copy (physical): 0.2%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0.2%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 2%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0%
2025
Fig. 11:Sunburst diagrams illustrating the changes in distribution of
robotic systems across activities from 2015 to 2024. Each diagram shows how
installations of robotic systems are distributed across ontology activities for a given
year. Color intensity encodes the proportion of robotic systems deployed in an activ-
ity, relative to the total robotic systems deployed that year. In general, this figure
suggests that there may be less broadening over time of robot uses across different
types of activities than of AI software applications. (See larger diagrams for each year
in Appendix G.3.)
2.4 An integrated view of how AI software applications and
robotic systems are used today
Figure 12 provides a concise summary of the empirical results reported in this paper.
Using the methods described in Section 6.6, we combined the weighted market values
of both AI software applications and robotic systems and mapped them to the ontology
activities where they were classified. The figure shows an estimate of how the market
value of all AI systems used today is distributed across the work activities these
systems help perform.
Like previous figures in this paper, this one confirms the highly uneven uses of AI
across different activities. In this case, only 1.6% of activities account for over 60%
of AI market value. And many activities account for little or none of the AI market
value. As described in the Discussion section below, this suggests not only where to
find promising opportunities for deploying today’s AI systems; it also suggests many
possible places that new generations of AI could be used in the future—either for good
or for bad.
The figure also allows us to answer questions about the overall uses of AI systems
and how these uses are divided among AI software applications and robotic systems.
17

Act: 100%
Act on information
(“Think”): 72%
Act with other activities and actors (“Interact”): 48% Act on physical objects (“Do”): 12%
Create
information: 36%
Modify
information: 11%
Transfer
information: 26%
Storeinformation: 0.005%
Transfer between
actors: 41%
Act onactivities: 12%
Modify physicalobjects: 10%
Create physicalobjects: 2%
Store physical
objects: 0%
Transfer physical
objects: 2%
Plan: 3%
Analyze: 6%
Decide: 0.5% Calculate: 0.1% Express information: 9% Assemble information: 2% Reason: 0.3% Create information -- other: 15% Solve: 0.2%
Transform information: 9% Com bine inform
ation: 0.8%
Separate information: 1% Move information: 0.001%Exchange information: 6%
Get information: 6%Provide information: 11% Communicate (transfer information end-to-end): 3% Store information -- other: 0.005% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 1%
Buy: 0.1%
Distribute: 0%
Sell: 0.1%
Give: 0.002%
Take: 0%
Transfer information: 26%
Transfer service: 11%
Transfer physical objects: 2%
Interact: 0.5%
Open (make available): 0%
Receive: 0.0006%
Return: 0%
Trade (Transfer both ways): 0.02%
Communicate (transfer information end-to-end): 3%
Earn: 0% Lend: 0% Pass (over): 0.02% Raise (funds): 0.02% W ithhold: 0%
Perform
 (action): 8%
Improve: 5%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0.1% Pass (achieve): 0% Undertake: 0% Transform physical objects: 5%
Separate physical objects: 0.03%
Combine physical objects: 3%
Move physical objects: 1%
Assemble: 0.5%
Fabricate: 1%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 2%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0.8%
Outline: 0%
Plan -- other: 1%
Propose: 0.3%
 Schedule: 0.05%
Stage: 0%
 Analyze -- other: 3%
Characterize: 0%
 Correlate: 0%
 Determine: 1%
 Experiment: 0%
 Investigate: 1%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0.06%
 Reject: 0%
 Rule: 0%
 Select: 0.4%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0.05%
 Count: 0.0003%
 Estimate: 0.06%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0.1%
 Record: 9%
Assemble information -- other: 0.001%
 Configure (information): 0.1%
 Construct (information): 2%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0.002%
 Organize (analytically): 0.3%
 Reason -- other: 0.05%
 Create (Activity): 0.3%
 Create (Actor): 0%
Create (Information): 14%
 Address (solve): 0%
 Resolve: 0.09%
Solve -- other: 0.1%
Adjust (information): 0.4%
 Change Appearance: 0%
 Clean (inform
ation): 0.0009%
 Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0.009%
Finish (inform
ation): 0%
Im
prove: 5%
Organize (analytically): 0.3%
 Perm
ute: 0%
Prepare (inform
ation): 0.2%
Process (inform
ation): 1%
Renew (inform
ation): 0%
Revise: 2%
 Service (inform
ation): 0.1%
Switch: 0%
 Transform
 inform
ation -- other: 0.08%
Translate: 0.5%
 Use: 0.08%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0.01%
Gather (inform
ation): 0.8%
Incorporate (inform
ation): 0.04%
Pack (together) (information): 0%
 Synthesize (information): 0.02%
 Break (into components): 0%
 Cut (information): 1%
 Disconnect (information): 0%
 Remove (information): 0.0004%
 Separate information -- other: 0.03%
 Move information -- other: 0%
 Put information: 0.001%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 2e-05%
 Converse: 2%
 Correspond: 0%
 Debate: 0.003%
 Exchange information -- other: 0.004%
 Interview: 0.9%
 Mediate: 0%
 Meet: 0.001%
 Negotiate: 0.002%
 Network: 0.04%
 Reach: 0.02%
 Teach: 3%
 Access: 0.08%
 Download: 4e-05%
 Evaluate: 2%
 Gather (information): 0.8%
 Get information -- other: 0.01%
 Import: 0.001%
 Learn: 0.4%
 Perceive: 2%
 Understand: 0.02%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0.1%
 Provide decision: 0%
 Provide money: 0%
 Send information: 11%
 Communicate (transfer information end-to-end) -- other: 0.5%
 Store (Activity): 0%
 Store (Actor): 0.005%
 Store (Information): 3e-05%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 1%
Ticket: 0%
Buy -- other: 0.01%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0.1%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0.09%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0.002%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 3%
Exchange information: 6%
Get information: 6%
Provide information: 11%
End service: 0%
Exchange service: 0.01%
Get service: 8%
Provide service: 3%
Exchange physical objects: 0%
Get physical objects: 2%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0.5%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0.0006%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0.5%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0.02%
 Raise (funds) -- other: 0.02%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 1%
 Conduct: 0.6%
 M
ake: 0%
Perform
 (action) -- other: 6%
Practice: 0%
 Rehearse: 0.02%
 Run (perform
): 0%
Im
prove -- other: 1%
Optim
ize: 3%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0.1%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0.06%
 Clean (physical): 5%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0%
Process (physical): 0.02%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0.07%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
Cut (physical): 0.007%
Disassemble: 0.0004%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0.02%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0.9%
 Consolidate: 0%
 Cover: 0.1%
Enclose: 0.4%
Gather (physical): 2%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0.1%
Reorient physical objects: 0%
Transport physical objects: 1%
Assemble -- other: 0.4%
Configure (physical): 0%
Construct (physical): 0.02%
 Copy (physical): 0.2%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 1%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 2%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0%
Fig. 12:Overall view of how AI is used today .Both AI software applications
and robotic systems are included. Numbers and color intensity show the percent of
market value associated with each activity in the ontology. (Percentages in a ring sum
to more than 100% when activities are classified in multiple places, but these double
counts are removed at higher levels.)
Are AI systems overall used most for thinking, doing or interacting?
The figure shows that a large majority (72%) of the estimated AI market value involves
our category of “Act on information (‘Think’).” So “thinking” is the most important
way of using AI market value today. Two specialized types of thinking account for
most of this: “Create information” (36%) and “Transfer information” (26%).
Although some people may think of AI as being mostly about robots, the primary
type of activity robots perform is “Act on physical objects (‘Do’),” and this activity
uses only about 12% of the overall AI market value. So robots that perform purely
physical tasks today are a relatively small contributor to overall market value provided
by AI. In this segment, “Modify physical objects” uses the largest share (10%).
18

“Interact” activities account for 48% of combined AI market value, with “Transfer
between actors” accounting for 41%. But interactions generally involve either infor-
mation or physical objects, and in this case, much of the market value of “Interact”
is for “Transfer information” (26%) which is shared with “Think.”
Which type of AI systems (software or robotics) contribute more market
value to different activities?
As Figure I27 in Appendix I.3 shows, according to our estimates, AI software applica-
tions account for 75% of the total market value for AI systems, and robotic systems
account for 25%.
More specifically, AI software is almost completely responsible for the “Think”
activities, robotic systems are fully responsible for the “Do” activities, and the “Inter-
act” activities are supported by a combination of AI software (34%) and robotics
(14%).
3 Discussion
In order to analyze and predict where AI can be used, we created a deep ontology of
work activities that incorporates and substantially reorganizes the approximately 20K
activities in the US Department of Labor’s O*NET occupational database. But unlike
O*NET and similar task taxonomies, this ontology is structured to systematically
take advantage of the concept of inheritance as used in object-oriented programming
and many applied ontologies. This means that the work activities in the ontology
are structured into family trees of similar types of activity, and—importantly—that
properties of the abstract activities in these family trees are usually inherited by their
more specialized descendants.
The paper then shows how this ontology can help answer the question of where
AI can be used. To do this, we classified two large datasets about AI uses—in soft-
ware applications and robotic systems—into the activities in our ontology. And we
assumed that the activities with more current AI uses were those with moreAI appli-
cability. Crucially, we also assumed that if an abstract activity (like “Write”) had high
AI applicability, then many of its more specialized descendants (like “Write email to
schedule a meeting”) were also likely to have high AI applicability. Finally, we cre-
ated sunburst diagrams to graphically display the relative AI applicability of all the
activities in our ontology.
In future work, we expect to further formalize and empirically test the assumptions
made in doing these things. But, as described in the next two subsections, we believe
they are already useful in practice for systematically identifying opportunities and
risks from using AI.
3.1 Identifying AI opportunities
The results in Section 2 about which activities are widely supported by current
AI applications can serve as a systematic map of potential AI uses. For example,
Appendix F.5 shows a number of atomic activities (and their associated O*NET tasks)
19

for which AI applications are already commercially available. This is an obvious way
for managers, workers, and others to identify AI uses they can consider adopting now.
More interestingly, for any generic activity in the ontology that has a large number
of AI applications, it is likely that AI could be applicable to many of the specializations
of that activity, even those activities that do notyethave AI applications. For example,
Figure 6 shows the activity “Create information – other” which has almost one-fifth of
all the AI applications in our dataset. But many of the atomic activities on the outer
ring of this figure are gray, indicating that they do not yet have any AI applications
in our dataset. Similarly, Figure 9 highlights specific activity gaps—i.e., tasks that
cannot yet be completed using robots in the robotics dataset [11, 12].
Thus, these two figures (Figures 6 and 9) can serve as systematicchecklistsfor
considering possible uses of AI. To use them in this way, we can consider at least three
reasons why an activity (like “Create information – other”) with many AI applications
would have specializations thatdon ’t have many applications. Each of these reasons
provides a different kind of opportunity. For example:
1.Technical opportunities. For some of the activities, there may not yet be AI
techniques that are capable of supporting the activity. For instance, looking at
Figure 6 might suggest that for some specific activities involving text genera-
tion, the current technology may create too many inaccurate hallucinations. In
video creation activities, the current quality of AI-generated video may not be
suitable. Or in robotics, examining Figure 9 might help robotics experts identify
gaps that are not yet met by current systems—e.g., long-horizon task-and-motion
planning in unstructured settings; contact-rich manipulation with compliant con-
trol; or uncertainty-aware scene understanding and state estimation. In all these
cases, there are opportunities for researchers and developers to create new AI
capabilities.
2.Economic opportunities. In other cases, there may be activities for which current
AI capabilities could support the activity, but it just isn’t economically useful
to use AI in this way. This provides entrepreneurial opportunities, such as (a)
developing better ways of identifying customers willing to pay more for an AI-
enabled service, or (b) identifying less expensive ways to obtain the data needed
to train a suitable AI model.
3.Unrecognized opportunities. There may also be activities for which there are AI
uses that are both technically and economically feasible, but no one has recognized
and taken advantage of this yet. These may be some of the most promising
entrepreneurial opportunities of all.
3.2 Identifying AI risks
In addition to being a tool for identifying AI opportunities, this ontology can also
serve as a checklist for identifying potential AI risks. For instance, if we look at only
the first four levels in Figure 12, we see a number of activities for which there are
potential risks from the use of AI:
20

• Create information. Our societal experience with social media has already demon-
strated how the Internet can amplify thespreadof misinformation of various
sorts. Now, we see that AI systems can certainly amplify thecreationof such
information. It is not clear exactly how to deal with these risks, but it is certainly
an issue worth consideration.
• Provide information. Another kind of risk arises when AI systems provide infor-
mation that is correct but that enables people to do dangerous things like create
atomic or biological weapons. How should we deal with these risks?
• Sell. Another area in which AI systems could introduce potential risks is in
selling. For example, more and more people are now using AI chatbots to find
information about products they are considering buying. Should there be rules
requiring chatbots to disclose the sponsors who affect which products the chatbots
emphasize?
• Decide. More broadly than just purchase decisions, it seems likely that AI systems
will increasingly be used to help humans make decisions of all kinds. Are there
analogs of truth-in-advertising laws that such systems should comply with? When
AI systems are advising people about personal problems like a therapist would
do, are there equivalents of professional codes of conduct?
The issues just listed are only a tiny subset of the issues we, as a society, might
want to consider about AI, and there are many other more specialized activities in
the outer rings of our ontology (see Appendix F.3) that might suggest other more
specialized kinds of issues to consider.
The ontology presented here doesn’t provide answers for how to deal with these
risks, and these answers might take many forms, including governmental policies, self-
regulation, and changing community norms. But this ontology does help systematically
identify AI risks, and we hope future versions of the ontology will also help design
governance processes to deal with these risks.
In general, asNew York Timescolumnist Tom Friedman says, AI is being
“infused” [14] into many parts of our lives. We hope the frameworks in this paper pro-
vide a useful conceptual tool for thinking systematically about how this AI-infusion
is working and how we might want to influence it.
3.3 Adapting to changing AI capabilities
Even if we had perfect knowledge of all the detailed places where today’s AI systems
could be used, that does not mean that we would know where future generations of
AI systems would be useful. And, since AI capabilities are rapidly changing, it would
be very helpful to be able to predict in detail where new AI capabilities could be used.
Fortunately, the inheritance capability of our ontology can make it possible to do
this much more systematically than before. As a simple example, consider the ontology
activity of “Dress (clothes).” The AI intensity of this activity is currently shown as 0%,
meaning that no AI systems in our datasets are currently being used to put clothes
on a person. But imagine that someday soon, a future robot has the physical and
interpersonal skills to do this successfuly. Where could such a robot be used?
21

Of course, one could just try to imagine possibilities for this, with greater or lesser
degrees of success. But consulting the online platform of our ontology would imme-
diately show a range of examples. The current examples in the ontology include: (a)
dress patients who are unable to dress themselves, (b) dress children, and (c) dress
mannequins for store displays. And, more morbidly, it even shows an example that
many people probably wouldn’t have thought of: (d) dress cadavers.
If you worked for a company that was making such robots, a list like this of
potential customer types could be very useful. And if you were trying to assess risks
of such robots, such a list could also be very helpful.
Of course, this is a relatively simple example, but the more important implication
is that the structure of our ontology could help systematically consider scenarios of
many different kinds of AI capabilities and their potential uses down to a very detailed
level. And this could be helpful both for identifying new opportunities and for avoiding
potential risks.
3.4 Limitations
We view the work described here as an early progress report for a promising long-
term research agenda, not just about understanding where AI can be used, but also
about analyzing and designing work activities in many other ways. As such, there are
a number of limitations of the current work.
3.4.1 Ontology construction
We constructed our ontology using a combination of human and AI reasoning, includ-
ing heavy reliance on the structure of synonyms and hypernyms in the WordNet
linguistic database. We believe that this provided a durable, linguistically precise, and
human-understandable ontology structure. We also believe that this structure does a
good job of capturing the deep similarities in different types of activities, including
similarities on the dimension of whether AI is applicable to the activity.
But there may well be better approaches to constructing useful ontologies for work
activities, and we believe an important part of the research agenda in this domain
will include exploring various other such methods. This may, for example, include (a)
using different analytic techniques (such as semantic embedding and clustering) and
(b) involving larger communities of human contributors. And even with our current
ontology, we believe there are multiple ways to improve the naming, organization, and
related content (such as definitions and descriptions) of some of the activity categories.
3.4.2 Application classification pipeline
As noted above, our application classification pipeline classified applications into
appropriate categories in our ontology at least as well as humans did. But we expect
that there are multiple ways to improve the accuracy and reduce the cost of this pro-
cess. Possibilities include: (a) better LLM prompting, (b) more precise definitions of
the activities themselves, and (c) explicit consideration of more properties of activi-
ties (such as their sub-activities). Our classification pipeline also did not distinguish
22

between whether an application couldautomatethe activity oraugmentan actor
already performing the activity. In the future, we plan to introduce this distinction.
3.4.3 Estimating AI applicability
In the Results sections above, we estimate the AI applicability for different activities
from the number of units and the market values of AI software applications and
physical robots that are available for these activities. But these numbers are certainly
not perfect estimators of actual AI applicability. For example, many random factors
affect the decisions by software developers and customers about whether to produce
or buy an AI application or robot for a given activity, including personal interests and
biased perceptions.
And the method we used to combine the separate intensity estimates for software
applications and robots into a single diagram (Figure 12) is based on estimates of the
market value of the applications customers pay for in each area.
All these estimates are based on what we believe are plausible—but certainly not
perfectly accurate—assumptions. And we leave for future work attempts to empirically
validate the accuracy of these predictions.
4 Future research
In this paper, we have demonstrated one way of using a deep ontology to organize
knowledge about a very comprehensive set of approximately 40,000 work activities.
This early work resulted in graphically compelling displays of where AI is being used
today.
We believe there is now great potential for using this approach to analyze, design,
and improve work processes in many other ways. One way of thinking about the
potential of this approach is by analogy to another scientific framework: the periodic
table of the elements in chemistry [15]. While the analogy is certainly not perfect, it
provides an intriguing way of thinking about the potential benefits of ontologies of
work activities.
In chemistry, the periodic table identifies (a) different fundamentaltypesof
matter (called “elements”), (b) differentways of combiningthese elements (called
“molecules”), and (c) differentpropertiesof these elements and compounds (e.g., elec-
tronegativity and metallicity). For over 100 years, chemists, chemical engineers, and
others have been using this periodic table and the other knowledge it helps organize
to create many key elements of our modern industrial civilization.
By analogy to the periodic table, we observe that an ontology of activities can
identify (a) differenttypesof actions (“activities”), (b) differentways of combining
these activities (e.g., as “sub-activities” of a larger activity), and (c) differentproperties
of these activities (e.g., “AI applicability”). In this paper, we have described one way
of specifying and organizing such an ontology to represent and predict the activities
in which AI can be used.
But we believe this is just the beginning of a broad research agenda. Perhaps
the most urgent part of this agenda is developing richer representations of theparts
(or sub-activities) of various kinds of activities. And a further step is to represent
23

theprocessesfor performing an activity, including not only the sub-activities of the
activity but also the interdependencies (such as prerequisites and flows) among these
sub-activities.
With these elements, we believe there are many opportunities for using this
approach to:
1.Optimize existing processes. For example, with rich libraries of different varia-
tions for how a process can be done, automated systems can not just optimize
parameters in an existing set of equations for a given process, they can also opti-
mize across different processes for achieving the same goal, each with different
performance estimation equations.
2.Rapidly adapt processes to new situations. For example, when unusual situations
arise, this approach could be used to automatically construct new processes by
systematically examining alternative methods for accomplishing the parts of the
standard process that are not possible in the current situation.
3.Design innovative new processes. For example, in smaller-scale earlier work
upon which this paper builds, we successfully used distant analogies with other
processes to generate unexpected new process ideas [16].
4.Analyze and design societal processes. In addition to using this approach for
specific policies in individual organizations, the approach could also be used to
analyze and design large-scale societal processes, such as (a) identifying skill
changes needed for workers in the AI economy, or (b) identifying potential design
changes in widely used processes that would improve quality of life for workers. We
can even imagine that this approach could be used to design new forms of societal
decision-making, such as new forms of democratic decision-making enabled by
new kinds of AI.
5 Conclusion
In this paper, we have presented a broad framework that integrates detailed data
about the uses of both AI software applications and robotic systems. We have also
shown how organizing this information in a deep ontology provides a powerful basis for
systematically identifying both opportunities and risks in current and future AI uses.
Understanding how we humans can use the increasingly powerful technology of AI
may be one of the most important questions facing humanity today. And we hope this
work will help business people, technologists, policy makers, and many others address
these questions, not only more systematically, but also more wisely.
6 Methods
6.1 Representing knowledge using an ontology
The word “ontology” originated as a branch of philosophy involving the study of what
exists. In particular, the field of ontology seeks to ascertain the most important features
of entities found in the world and the relations between them [17]. “Applied ontology”
involves identifying the types of objects that exist in a given field of study along with
24

their properties and relationships [8]. For example, the discipline of biology has a set
of concepts to describe the types, properties, and relationships of living things.
Starting in the 1990s, computer science researchers began to use the word “ontol-
ogy,” to refer to formal, digital representations of these applied ontologies [8], and that
is the sense in which we will use the word here. More recently, the term “knowledge
graph” has also been widely used to describe a way of digitally representing ontolo-
gies and similar kinds of knowledge about objects and their relationships [18]. These
ontologies based on knowledge graphs have been developed and widely used in fields
such as biology [19], medicine [20], and finance [21], and our ontology is one of these.
Of particular importance as a foundation for our work here is an early ontology
of business activities called the MIT Process Handbook [16]. The Process Handbook
included over 5,000 business processes and activities, with an emphasis on simultane-
ously representing two kinds of hierarchies: (a) hierarchies of increasingly specialized
typesof activities (e.g., writing and its specialized types such as writing novels, writ-
ing news stories, and writing scientific articles), and (b) hierarchies of increasingly
fine-grainedpartsof activities (e.g., baking a cake and its parts such as assembling
ingredients, mixing, and heating).
A key feature of this kind of ontology is that the properties of a given type of
object areinheritedby the more specialized types of that object except when they
are explicitly overridden at the specialized level. For example, Figure 13 shows how
the five parts (or sub-activities) of the activity “Sell product” are inherited by two
specialized types (or “specializations”) of that activity. In this case, several of the sub-
activities are overridden in the two specializations, and the sub-activities are replaced
by their own specializations (e.g., “Identify potential customers” is overridden by
“Obtain email lists” in “Sell by email” and “Attract customers to store” in “Sell in
retail store”). For simplicity, we often refer to the specializations of an activity as its
“children” and the generalizations of an activity as its “parents.”
In future work on this ontology, we plan to add sub-activities like those shown
in Figure 13, and we expect this to be helpful, not just in identifying where AI can be
used, but also in answering broader questions such as how work processes are likely
to change to take advantage of AI capabilities. In the work described in this paper,
however, we focus only on the inheritance of the property ofAI applicability—whether
the activity can be performed using AI.
6.1.1 Multiple inheritance in ontologies
Many ontologies (including the one we use here) includemultiple inheritance, where
an activity can have multiple parents. For example, the activity “Talk” can be clas-
sified as a specialization (or child) of “Transfer information,” since it usually involves
transferring information to another person. But it can also be classified as a child
of “Create information” since it also involves creating information. If an activity has
multiple parents, and the parents have different properties, then the properties of at
least one of the parents must be overridden in the child activity.
And, as will happen multiple times in this paper, when characteristics like counts
of AI applications are aggregated from children up to their ancestors, theseaggregated
countsremove double counting at the levels where the ancestral lines come together.
25

Fig. 13:“Sell online” and “Sell in retail store” are specializations of the
generic sales process “Sell product.”Sub-activities that are different from those
in the generic process are shaded. Adapted from [16].
6.2 Creating a large-scale ontology of work activities
6.2.1 Design principles
To create an ontology of work activities, we began with the very comprehensive set
of activities in the O*NET database (version 29.1, released November 2024). But we
worked to reorganize these activities according to three desirable properties that are
not always present in O*NET:deep similarity,atomicity, andspecificity.
Deep similarity
The first and most important of these properties isdeep similarity. The biological tax-
onomy of species of living things (e.g., plants, animals, mammals, birds, etc.) provides
a good example of this property. Linnaeus and others who developed this taxonomy
did not primarily classify living things according to superficial characteristics such as
their color and size, but according to deep characteristics such as their structure (e.g.,
bones and organs) and function (e.g., warm-bloodedness and live birth) [22–24].
Similarly, in our ontology, we have classified activities in terms of deep similarities
in their structure and function [16]. For example, we group activities by their functional
outcomes (e.g., creating, modifying, storing, and transferring) and by the type of entity
they act upon (information, physical objects, or other actors), rather than on more
superficial characteristics such as the industry or geographical location of the work.
This matters because functionally similar activities are more likely to have similarAI
applicability.
In this proof-of-concept version of our ontology of work activities, we based
these classifications on the meanings of the words (especially the verbs) describing
the activities. To do this, we used the synonym and hypernym-hyponym relation-
ships represented in the commonly used WordNet lexical database [25, 26] combined
with our human editorial judgments to classify deeply similar activities together.
26

Hypernym-hyponym relationships are the semantic relations between a more generic
term (hypernym) and a more specific term (hyponym). For example, the verbs “walk”
and “run” arehyponymsof “move,” which is in turn considered theirhypernym. Using
this approach, for instance, the activity “Connect physical objects” includes as sub-
types (or what we callspecializations) activities with names that involve physical
objects and that start with “Connect” or its synonyms like “Link,” such as “Connect
cables” or “Link chains.” It also includes as specializations activities that involve phys-
ical objects and that start with hyponyms of “Connect,” such as “Adhere,” “Clamp,”
“Sew,” and more. In turn, “Connect physical objects” would be considered what we
call ageneralizationof these activities.
Atomicity
The second desirable property we designed our ontology to preserve isatomicity. This
is an important limitation in O*NET because the lowest level activities in O*NET,
called “tasks,” are mostly compound descriptions of multiple activities in a job role.
For example, one such activity is “Acquire, distribute, and store supplies.” In our
ontology, we decomposed this compound task into three atomic activities, represented
as verb-object pairs: “Acquire supplies,” “Distribute supplies,” and “Store supplies,”
and each of these atomic activities is classified in a different place in the ontology.
Thus, we use the word “atomic” here to mean a single activity that captures one
specific functional operation and that is usually represented as a verb-object pair. We
do not, however, mean that “atomic” activities are uniquely correct or irreducible
descriptions of work activities, since work activities can often be decomposed in many
different ways.
Specificity
The final desirable property isspecificity. By specificity, we mean that (a) a given
concept is represented by the same name everywhere it occurs, and (b) different con-
cepts have different names. This means that each node in the ontology corresponds
to a single, distinct activity, and our labels make those distinctions explicit. For
example, we distinguish “Perform (artistic)” from “Perform (action)” and “Load (dig-
ital)” from “Load (physical)” rather than using the same surface verb for multiple
meanings, whereas O*NET does not make this distinction. (For more examples, see
Appendix B.6)
6.2.2 Construction Process
To construct the ontology, we explored a number of different approaches—including
using LLMs only, using humans only, and using other knowledge sources for reference.
(We elaborate on these explorations in Appendix B.1). We then combined elements
from the approaches in our explorations to develop an initial version of the ontology.
Finally, we reviewed, edited, and expanded the initial ontology. Figure 14 provides a
full overview of the construction process.
27

Fig. 14:Flow chart demonstrating the ontology construction process,
including steps:(1) extracting verb-object pairs from O*NET items (to achieve
atomicity), (2) assigning appropriate definitions from WordNet for each verb in con-
text (to achievespecificity), (3) organizing activities into hierarchical structure using
WordNet’s “hypernym” (generalization) trees, and (4) significant human editing to
improve the structure (to achievedeep similarity).
Step 1: Semi-automated construction of initial ontology
After initial explorations, we formulated a hybrid approach using a combination of
top-down and bottom-up methods, as well as a combination of automated reasoning
and human judgment (see Figure 14).
28

In the bottom-up approach, we started with decomposing activities included in
the O*NET database, which contains approximately 18,000 tasks that get aggregated
successively into 2,082 Detailed Work Activities (DW As), 332 Intermediate Work
Activities (IW As), and 41 General Work Activities (GW As) [5]. These GW As are then
grouped into four major categories: Information Input, Interacting with Others, Men-
tal Processes, and Work Output. (See Figure 15 for an example of the relationships
between tasks, GW As, IW As, and DW As.)
Fig. 15:Overview of the O*NET hierarchy structure with an example of a
“woodworking” occupation and its associated GW As, IW As, DW As, and
tasks.The top-level activities in (a) can be found at https://www.onetonline.org/
find/descriptor/browse/4.A.
These DW As, IW As, GW As, and tasks are often compound descriptions, so we
used LLM reasoning to break them into atomic activities, the smallest units of work
described, which we represent as verb-object pairs. For instance, the task “Acquire,
distribute and store supplies,” was decomposed into three verb-object pairs: “acquire
supplies,” “distribute supplies,” and “store supplies.” This resulted in 40,825 verb-
object pairs, of which less than half (15,989) were unique, indicating many O*NET
tasks share atomic activities.
Then we used LLM reasoning to select the most appropriate definition for each
verb in the verb-object pairs from the available definitions in WordNet, a widely used
linguistic database that groups words by their meaning and maps the semantic rela-
tionships between them [27]. WordNet at times contains definitions with significant
similarity—for example, WordNet has both definitions “engage in drawing” and “rep-
resent by making a drawing of, as with a pencil, chalk, etc. on a surface” for the verb
“draw.” Due to the lack of clear distinction betewen the definitions, the LLM would
29

sometimes choose one and other times choose the other for the same context. Thus
to reduce the number of potential definitions, we presented the LLM with only the
definition with the most hyponyms for each “supersense” (a broad semantic category
in WordNet, such as verb.creation, verb.motion, verb.social, etc. [28]). We used the
number of hyponyms as a proxy for generality, preferring broader verb senses that are
more likely to anchor the hierarchy.
Sometimes, the chosen definition was incorrect, so we used another LLM that
checked whether the chosen definition matched the context given. We omitted
invalid definitions from the initial version of the hierarchy. We manually revised and
re-incorporated such instances in the Revision phase.
We used the selected meanings to merge the verb-object pairs into groups where
the verbs all have the same meaning and the objects are identical. We call these
groups “atomic activities.” To make it easier for LLM and human editing, we also
chose to first work only with meanings that had more than 10 occurrences in O*NET
tasks, excluding the so-called “long tail” of meanings. These we reincorporated in the
Revision phase. We then used the hypernym relationships (akin to generalizations)
in WordNet to organize the atomic activities into 60 hierarchical trees with the more
specialized verbs at the bottom of each tree and the more general verbs at the top of
each tree. (See Appendix B.2 for a full list of the 60 general verbs.)
Next, we used a top-down approach to create a top-level hierarchy into which
all these trees of atomic activities were classified. At the highest level, we adopted a
tripartite distinction between acting on information (which we nickname “Think”),
acting on physical objects (which we nickname “Do”), and interacting with other
actors (which we nickname “Interact”), commonly used in work studies [29]. Then, we
used LLM reasoning to classify the hypernym trees from the previous stage into this
top-level framework.
Step 2: Human and LLM editing to revise ontology
After the construction of the initial ontology, we refined it through a combination of
automated checks and human review. First, two authors of this paper acted as human
editors and revised the classifications, adding a second-level framework of Create,
Modify, Transfer, and Store underneath each branch within the Do/Think/Interact
framework. Our human editors also made other edits, such as renaming activities,
deleting unnecessary intermediary activities, merging activities with similar meanings,
and grouping activities to increase the intuitiveness of the framework. We opted to use
WordNet’s hierarchy as a linguistic starting point for our classifications, but we made
significant changes because our principle of deep similarity aims to capture functional
inheritance (inheritance of properties), which sometimes diverges from WordNet’s lex-
ical relationships. For instance, WordNet places “Type” (as in typing on a keyboard)
under “Write” based on lexical relationships, but functionally, typing is a physical
manipulation activity that may or may not involve writing; one can type numbers,
code, or random characters. We moved such activities to reflect functional rather than
lexical inheritance.
Next, we added explicit specifications to 215 activities using the same verb but
different meanings (e.g., Perform (artistic) vs. Perform (action), Load (physical) vs.
30

Load (digital)). (see Appendix B.6 for more detail). We then placed 644 previously
omitted meanings from both invalid definitions and the long tail of infrequently occur-
ring O*NET tasks. To do this, we used LLM-suggested placements reviewed by human
editors. (This method was developed iteratively, with details in Appendix B.3).
To address ambiguities in WordNet definitions—especially verbs spanning both
physical and informational uses—we iteratively developed a framework for classifying
direct objects into four categories: Physical Object, Information, Actor, and Activity
(e.g., “Improve activity”). Then we used this framework and a combination of LLM
reasoning and human judgment to resolve 615 inconsistencies between verb locations in
the ontology and object types. For example, if the activity “Cut video” is placed under
the “Act on physical objects>... Cut (physical)” branch, while “video” is labeled
as Information, this constitutes an inconsistency that can be resolved by placing it
under the mirror branch with the matching object, “Act on information>... Cut
(information)”. The principles we developed to define these categories are detailed in
Appendix B.4. The method to resolve inconsistencies is detailed in Appendix B.5.
Finally, we used these noun classifications to introduce object-based intermediate
activities between generic activities and atomic activities (e.g., adding the intermediate
activity “Observe Physical Object” between the generic activity “Observe” and the
atomic activity “Observe Equipment”), improving clarity and structural consistency.
In summary, using a combination of automated LLM reasoning, WordNet, and
editorial judgments by authors of this paper, we produced an ontology with atomicity,
specificity, and deep similarity that we hope can serve as a foundational analysis
framework for future studies.
This process produced an ontology of work activities with 1,113 generic activities
and 15,989 unique atomic activities covering all 20,950 O*NET tasks, DW As, IW As,
and GW As. Generic activities are usually verbs, like “Decide,” “Assemble,” “Clean,”
“Communicate,” sometimes with broad object categories, like “Create information”
or “Create physical objects.” Atomic activities are more specific verb-object pairs (like
“Collect fees”) extracted from O*NET tasks. The fact that there are fewer unique
atomic tasks in total than O*NET tasks also means that many atomic tasks are shared
across O*NET tasks, showing the compression power of our ontology.
Figure 1 shows a sample of the ontology contents. At the far left is the most
generic activity type of all, “Act,” followed by a “Collection” of related activities that
are all answers to the question “Act on what?” (e.g., “Act on information,” “Act
on physical objects,” “Act with other activities or actors”). Beneath those activities
are specializations of each (e.g. “Create information,” “Modify information,” etc., are
specializations of “Act on information”). To the right is an expansion of one of these
activities, “Create information,” which includes more specializations, collections, and
finally atomic activities and their associated O*NET tasks.
Table 1 shows more detailed statistics about the contents of the final ontology. The
first three levels are broad categories (e.g., “Act on information,” “Modify physical
objects”) into which all the more specialized activities can be classified. At these levels,
there may be relatively few characteristics that are inherited by their descendants.
Level 4, however, is the first level where we expect relatively detailed sets of properties
to characterize the “family trees” headed by the 69 activities at this level. There are
31

T able 1:Counts and examples across different levels of the ontology .Note
that the Total row is not the direct sum of the rows above, but rather counts only
once the activities that exist at multiple levels.
Type of activity Activity
level
Examples Number of
activities
Generic activities
1 Act 1
2 Act on information, Act on physical
objects, Act with other actors and activ-
ities
3
3 Create information, Modify information,
Transfer information, Store information,
Create physical objects, Modify physical
objects, . . .
10
4 Decide, Calculate, Plan, Fabricate, Buy,
Improve, . . .
69
Cumulative
1 - n-3
Select, Count, Budget, Cast, Rent, Opti-
mize, . . .
1,113
n−2 Select (Information), Select (Actor),
Budget (Activity), Cast (Physical
Object), Optimize (Information), . . .
1,551
Atomic activitiesn−1 Select method, Select personnel, Budget
work, Cast mold, Optimize cost, . . .
15,989
O*NET itemsn(16122) Select methods, techniques, or
criteria for data warehousing evaluative
procedures;
(4.A.3.a.2.I17.D01) Cast molds of patient
anatomies to create medical or dental
devices
20,950
T otal (excluding
collections)
— — 39,603
a total of 2,664 generic activities from level 1 to the last level before atomic activities.
Approximately 34.1% of generic activities fall under “Act on information,” 33.5%
under “Act on physical objects,” and 32.4% under “Act with other activities and
actors.”
In terms of the depth of the ontology, the median path length from the root activity
(“Act”) to leaf generic activities is 6. Below this, there are 3 more levels: noun-grouped
activities, atomic activities, and O*NET tasks, making the median total path length
9. The minimum path length to O*NET tasks is 6 and the maximum is 14.
We also track 22 activities that multiply inherit from more than one top-level
domain (“Think” vs. “Do” vs. “Interact”), indicating many activities (e.g., “Talk”,
32

“Greet”, “Gather”) cut across informational, physical, and interpersonal domains (see
Appendix B.7).
6.2.3 Rationale for Choice of Methods
While we do not claim our methods are optimized, we had several reasons for choosing
them over other potential methods. First, we chose not to create the hierarchy of
activities using semantic clustering, because we wanted the units of our ontology to
represent discrete wordsenses, not approximate similarities in a continuous embedding
space. Second, we chose not to use a purely LLM-generated taxonomy and instead
used a Human-in-the-Loop (HITL) approach. While recent work suggests LLMs can
sometimes outperform crowd workers for text annotation [30], our experience suggests
that the LLM’s tendency to hallucinate often results in taxonomies in which human
experts see many limitations. Based on this, we wanted to investigate the potential
benefits of using human experts to verify that the hierarchical relationships represent
actual functional inheritance rather than mere keyword association; in other words,
we distinguish “is a kind of” relationships from “often happens with” relationships.
We also utilized WordNet as the basis for our automated ontology creation, rather
than purely LLM-based classifications. This was primarily to ensure deterministic
results from the automated part of our classification process. While LLMs excel at
reasoning, their outputs can be non-deterministic and hallucinate novel categories.
Determinism matters for ontology construction because the ontology will serve as
a stable reference for classifying evolving datasets over time. If the ontology itself
were generated non-deterministically, different runs could produce different structures,
making longitudinal comparisons impossible. As a commonly used and well-respected
lexical database curated by human experts, WordNet provided us with a deterministic
and meaning-grounded starting point.
Methodologically, our effort brings the precision of the field of semantics to the
characterization of work activities. In contrast to existing task datasets, our ontology
is characterized by deep similarity, atomicity, and specificity. These features abstract
beyond task descriptions that vary over time, allowing our ontology to offer a durable
semantic framework that can anchor evolving datasets like O*NET.
6.2.4 Demonstration of Usefulness
To demonstrate the usefulness of our approach, this section provides concrete examples
of benefits from the three key features described above: atomicity, specificity, and deep
similarity.
First, theatomicityof our ontology enables analysis of tasks on their own, as
opposed to in compound forms like the instances found in O*NET. Figure 16 shows
a demonstration of this principle in practice by using an O*NET task that includes
4 distinct atomic activities. Previous AI impact analyses using O*NET tasks [31–
33] often clump together the atomic activities in an O*NET task. They also often
compensate for this by, for example, taking a measurement for an O*NET task and
arbitrarily dividing it equally among all the O*NET DW As the task includes [32].
As Figure 16 illustrates, the fine-grained focus provided by atomic activities can give
much more precision to many similar analyses.
33

Fig. 16:Example of how O*NET tasks break down into atomic tasks.
Demonstration of how this breakdown helps with the analysis of AI applicability,
because each atomic task requires different abilities.
Second, thespecificityof our ontology allows precise expression of activities with-
out being confused by synonyms or multiple meanings for a single word (polysemy).
Ultimately, ontologies should be grounded inmeaningsrather thanwords. Figure 17
shows an example of this. Consider the verbmake. In O*NET task 16513 (“Make
system device lists or event timing charts”), “make” is synonymous with verbs such
as produce and create used in other tasks describing the same activity (e.g., pro-
ducing graphics or creating diagrams). However,makeis also polysemous. In tasks
such as “Make customers feel welcome,” “make” expresses causation rather than cre-
ation. Without what linguists call “word sense disambiguation” (WSD), these distinct
meanings ofmakecould either be conflated (grouping causative actions with artifact
creation) or fragmented (treating synonymous expressions as separate activities). Our
ontology resolves these issues by mapping synonyms to a shared atomic activity while
separating the distinct senses of verbs that have multiple meanings, enabling precise
classification and downstream reasoning. For example, an AI tool capable of automat-
ically generating diagrams or system documentation can be correctly associated with
occupational tasks that includeproduce,create,makein the creative sense, but not
with causative uses ofmakethat involve directing or compelling human behavior.
Third, thedeep similarityof our ontology enables aggregating and propagating
insights. When analyzing tens of thousands of work activities, hierarchical frameworks
enable simplification of understanding and high-level insights. Many papers analyzing
34

Fig. 17:Demonstration of the importance ofspecificity,achieved using word
sense disambiguation, in the case of “Make”, with distinct senses meaning creation
and causation; “Produce” and “Create” also are synonyms of the Creation meaning.
work impact recognize the value of higher-level frameworks—for example, [32] devel-
ops a custom clustering-based hierarchy to classify the O*NET tasks associated with
prompts to the Claude LLM. O*NET itself has a hierarchical structure with tasks,
DW As, IW As, and GW As. However, we propose that such frameworks need deep sim-
ilarity—that is, child categories should share, or “inherit,” properties from parent
categories. Properties that can be inherited include, for example, the parts or steps
of an activity and the potential applicability of AI to the activity. Unlike clustering-
based hierarchies that group activities by statistical co-occurrence, our ontology groups
activities by functional inheritance.
To illustrate why deep similarity matters for AI analysis, consider the activity
family ofinspection—examining equipment, materials, or operations to assess their
condition or compliance. Most readers would expect these closely related tasks to
be grouped together: they share a common cognitive structure (perceive, compare
to standard, judge) and, crucially, similar AI applicability (computer vision systems
that can inspect equipment for defects can likely also inspect materials or operations
for defects). In our ontology, all inspection activities are descendants of the generic
activity “Inspect,” enabling this kind of cross-activity reasoning.
In O*NET’s Work Activities hierarchy, however, functionally similar inspection
tasks are scattered across three different top-level Generalized Work Activities (GW A)
branches. As shown in Table 2, “Inspect equipment to ensure proper functioning”
falls under GW A 4.A.1.b.2 (Inspecting Equipment, Structures, or Material), while
“Inspect operational processes” falls under GW A 4.A.1.a.2 (Monitor Processes, Mate-
rials, or Surroundings)—a different GW A branch entirely. Even more surprisingly,
“Disassemble equipment to inspect for deficiencies” is classified under GW A 4.A.3.a.2
(Handling and Moving Objects), grouping it with material handling rather than with
other inspection activities.
35

T able 2:O*NET scatters functionally similar inspection activities across
three separate GW A branches.All six DW As share the core cognitive operation
of inspection (perceive, compare, judge), yet O*NET’s hierarchy places them under
different top-level categories: two under “Inspecting Equipment,” three under
“Monitor Processes,” and one under “Handling and Moving Objects.” In our
ontology, all six activities inherit from a common “Inspect” ancestor, enabling AI
applicability to propagate across the entire inspection family.
GW A Branch GW A Title DW A ID DW A Title (Inspection
Activity)
Branch 1: Information Input→Inspecting Equipment, Structures, or Material
4.A.1.b.2 Inspecting Equipment,
Structures, or Material
4.A.1.b.2.I07.D18 Inspect equipment to ensure
proper functioning
4.A.1.b.2 Inspecting Equipment,
Structures, or Material
4.A.1.b.2.I10.D03 Inspect shipments to ensure
correct order fulfillment
Branch 2: Information Input→Monitor Processes, Materials, or Surroundings
4.A.1.a.2 Monitor Processes, Materi-
als, or Surroundings
4.A.1.a.2.I02.D09 Inspect operational pro-
cesses
4.A.1.a.2 Monitor Processes, Materi-
als, or Surroundings
4.A.1.a.2.I11.D02 Inspect products or oper-
ations to ensure standards
are met
4.A.1.a.2 Monitor Processes, Materi-
als, or Surroundings
4.A.1.a.2.I09.D06 Inspect condition of natural
environments
Branch 3: Work Output→Handling and Moving Objects
4.A.3.a.2 Handling and Moving
Objects
4.A.3.a.2.I19.D03 Disassemble equipment to
inspect for deficiencies
This scattering has practical consequences for AI impact analysis. A researcher
using O*NET’s hierarchy to assess whether AI can automate inspection tasks would
need to separately evaluate three GW A branches and somehow recognize that they
share an underlying capability. Our ontology resolves this by grouping all inspection
activities under a single “Inspect” ancestor, so that evidence of AI applicability to
any inspection task can propagate to related tasks through inheritance. When we find
that computer vision systems can “Inspect equipment,” we have principled grounds to
hypothesize they may also support “Inspect shipments” or “Inspect operational pro-
cesses”—a form of systematic capability transfer that O*NET’s fragmented structure
cannot support.
6.3 Software platform for creating an ontology
To create and maintain this ontology at the scale of tens of thousands of activities and
relationships, we developed a dedicated platform for collaborative ontology editing.
Figure 18 shows an example of the interface, which supports three core functionali-
ties: (i) structured browsing of the specialization hierarchy of activities, (ii) inspecting
and editing an activity’s title, definition, synonyms, and links (generalizations, spe-
cializations, and parts), and (iii) searching using a combination of keyword search and
semantic (meaning-based) retrieval (Appendix C).
The platform provides guardrails to support coherent, auditable editing at scale.
For example, it blocks edits that would disconnect (or “orphan”) an activity, flags
36

Fig. 18:User interface for ontology platform,including (a) an outline view of
the specialization hierarchy, starting with the most generic activity type called “Act,”
(b) an editable view of the chosen activity (“Select”), including properties such as
Title, Description, Generalizations, and Specializations, and (c) a search bar to find
activities by keywords or semantically similar phrases.
near-duplicate activities for review, and maintains node-level change histories with
attribution to the people who made changes. For downstream analyses and automated
classification, it exports versioned JSON snapshots so evaluations and scripts reference
a fixed ontology instance.
In addition to being essential for creating the ontology, this platform also served as
a primary instrument for the human evaluation of automated classifications described
in Section 6.5.1. A key feature of the platform for this purpose was the hybrid search
engine described above that combines keyword search with semantic retrieval. This
helps humans who are classifying activities (“human annotators”) locate candidate
activities based on either semantic meaning or exact wording.
6.4 Data sources about AI uses
For our analysis, we examine two representative datasets about AI usage. The first
dataset is a catalog of AI software applications from a website called “There’s an AI
for That ®” (TAAFT) [10]. These applications act on information, not on physical
37

objects. The second dataset, from the International Federation of Robotics (IFR)
World Roboticsreports [11, 12], describes robotic systems that act on physical objects.
Both types of systems can also act on or with other actors and activities. Together,
these two datasets provide a comprehensive overview of contemporary AI usage.
6.4.1 AI software applications
“There’s an AI for That ®” (TAAFT) [10] is a website that provides a comprehensive
catalog of AI software applications. The company provided us with a dataset that
included descriptions of 13,275 individual AI applications launched between November
2013 and July 2025. This dataset excluded applications listed on the site that (a)
were inactive or no longer maintained, (b) were platform-specific mini-tools developed
by TAAFT itself, or (c) involved only custom tools built using ChatGPT (“custom
GPTs”), which were considered largely obsolete.
The included applications span a wide range of tasks and use cases, including, but
not limited to, text generation, data analysis, automation, image-related tasks, and
domain-specific workflows. Although this is certainly not an exhaustive census of all
AI software applications, we believe it is broadly representative of the AI software
applications in use today. The dataset includes AI applications deployed on different
platforms, including websites, iOS, Android, and Chrome extensions. For each AI
application, the dataset includes descriptions, taglines, primary tasks, tags, pricing
information (including price, pricing model, and billing frequency), launch dates, and
indicators of community engagement such as the number of saves (see Appendix F.1
for example data).
6.4.2 Robotic systems
The International Federation of Robotics (IFR) publishes annualWorld Robotics
reports [11, 12]. These reports comprise the world’s most comprehensive dataset on
robotic systems.
IFR defines a robot as a “programmed actuated mechanism with a degree of auton-
omy, capable of performing locomotion, manipulation, or positioning” (adopted by the
International Standardization Organization (ISO) [34]. This definition excludes simple
factory machines that repeatedly perform the same movements without autonomous
decision-making. IFR classifies robots into two major categories, industrial and ser-
vice robots. Service robots include professional, medical and consumer robots (for
detailed definitions, see Appendix G.1). Note that the IFR reports specifically exclude
two types of robots: (i) military robots (robots for the defense sector), because they
are against the organization’s values for peaceful use of robotics; and (ii) autonomous
passenger transportation vehicles as part of the automotive industry.
In each major category, IFR segments robotic systems into classes and subclasses.
For example, industrial robots are divided into 6 classes (e.g., “Welding and solder-
ing”, “Assembly and disassembly,” etc.), and these classes are further divided into
35 subclasses (e.g., “Welding and soldering” includes the subclasses “Arc welding,”
“Spot welding,” and four others.) Service robots are similarly categorized into classes
and subclasses. In all, IFR recognizes 20 classes of robotic systems and 66 subclasses.
38

Table G8, Table G9, Table G10, and Table G11 in Appendix G.1 list all the classes
and subclasses defined by IFR.
We used IFR data on the global number of robot installations in each subclass
in 2024, the most recent year for which data is available. In that year, there were a
total of 20.8 million total installations of robotic systems, of which 20.1 million were
consumer robots, 542K industrial robots, 199K professional service robots, and 17K
medical robots.
6.5 Methods for classifying activities in an ontology
6.5.1 Automated classification
Since it was not feasible to manually classify the more than 13,000 AI software appli-
cations into a deep ontology, we developed an automated classification pipeline that
was validated by human annotators.
Philosophy of classification
We classified each application according to its primary activity: the essential verb-
object activity the application performs or helps perform. To do this, we determine the
most specific ontology activity whose scope fully covers the application ’s primary activ-
ity. Because many applications are multi-purpose and descriptions can be ambiguous,
classification is treated as a subjective judgment based on the rule in the previous
sentence.
We consider an automated classification pipeline satisfactory if its human-AI
inter-annotator agreement (IAA) is comparable to, or exceeds, the human-human
IAA achieved under equivalent instructions. This criterion evaluates consistency with
human judgment; it does not establish a single objective ground-truth label for each
application.
Automated classification pipeline
To automatically map the AI software dataset into our ontology, we investigated
a number of alternative methods and evaluated three final pipeline variants (see
Appendix D for details and prompt text):
• Single Prompt Partial Ontology (SPPO).We first use semantic embeddings
to retrieve a subset of ontology activities (k∈ {20,50,100}) that are semantically
similar to the application description and tagline. A single GPT-5.1 prompt then
(i) identifies a verb–object pair describing the application’s primary activity and
(ii) selects the best-matching ontology activity from the retrieved shortlist.
• Multi-Prompt Partial Ontology (MPPO).We first prompt GPT-5.1 to
extract a clean verb–object description of the application’s primary activity.
We then retrievek∈ {20,50,100}candidate ontology activities using seman-
tic similarity to this verb–object phrase. Finally, a second prompt selects the
best-matching ontology activity from the retrieved shortlist.
• Single Prompt F ull Ontology (SPFO).We cache the full ontology in the
model context and use a single GPT-5.1 prompt to identify the application’s
39

primary verb–object activity and select the most specific matching ontology node
from the full hierarchy, without retrieval.
Appendix D provides additional details about the evolution of these variants,
including the prompts and the main tradeoffs we observed across accuracy, specificity,
hallucinations, and cost.
Our final pipeline uses the SPFO approach with GPT-5.1 (high-reasoning-effort).
By caching the full ontology in the system prompt, this model can traverse the hierar-
chy rather than rely on a retrieved shortlist. As described in the next subsection, this
pipeline had the highest agreement with human annotators, though differences across
variants were not statistically significant.
Human evaluation of classifications
To evaluate the classification quality of the three candidate pipeline variants and
inform the final model selection, we conducted a small-scale human evaluation. We
randomly sampled 30 applications from the full TAAFT dataset. Seven authors of this
paper manually classified the primary activity for each of these 30 applications and
then compared their classifications with those produced by the three GPT-5.1 model
architectures described above.
Human classification.To make their classifications, each human annotator saw the
application name, tagline, and description for each application. The human annota-
tors were also given access to the ontology platform, which provided the full ontology
(including activity names, descriptions, and synonyms) as well as a search engine for
finding relevant ontology activities (see Appendix C). The human annotation instruc-
tions were intentionally aligned with the prompt for the AI models: both required
identifying the application’s primary verb-object pair and selecting the most appro-
priate (i.e., closest/most similar) ontology activity, operationalized as choosing the
most specific node whose scope fully covers that pair (see Appendix E.1 for the full
instructions provided to human annotators).
Human evaluation of model classifications.After completing their own classifica-
tions, human annotators were shown the classifications generated by the three AI
pipeline variants, each accompanied by the model-generated rationale. For each appli-
cation, participants were asked to consider their own classification and compare it
with each AI model’s output. They were also asked to review the model rationales
for additional context. Then the human annotators evaluated each model’s classifica-
tion using one of three options: “better than my own classification,” “equally good
as my own classification,” or “worse than my own classification.” To ensure fair com-
parison, model identities were anonymized as “LLM1,” “LLM2,” and “LLM3” during
evaluation.
Analysis Methods and Results.We report both human-human inter-annotator
agreement (IAA) and human-AI IAA following prior work [33, 35–37]. Because our task
involves classification within a hierarchically structured ontology rather than a flat cat-
egorical label space, general-purpose IAA measures are not directly applicable. Instead,
40

we adopt similarity-based IAA formulations with broader applicability for hierar-
chical structures [38]. Specifically, we use the Wu-Palmer (WuP) network similarity
metric [39] and weighted Cohen’sκ, as described in more detail in Appendix E.2.
As shown in Figure 19, all three pipeline variants achieve human-AI IAA levels
comparable to human-human IAA. Across both metrics, human-AI IAA is similar
to and slightly higher than human-human IAA, indicating that LLMs are capable
of closely approximating the subjective judgments made by human classifiers [40].
Within the human-AI conditions, the Single Prompt Full Ontology approach shows the
highest alignment with human classifications, although the differences across model
architectures are not significant. However, the AI-AI IAA is significantly higher than
any of these human-referenced agreements, indicating that the models are more self-
consistent than they are with human annotators, and than human annotators are
amongst themselves.
Fig. 19:Human-AI inter-annotator agreement for three GPT-5.1 (high-
reasoning-effort) classification pipeline variants:SPPO = Single Prompt
Partial Ontology, MPPO = Multi-Prompt Partial Ontology, SPFO = Single Prompt
Full Ontology. Left: Mean Wu-Palmer Similarity. Right: Weighted Cohen’sκ. Plots
show 95% confidence intervals computed via nonparametric bootstrap with 1,000
resamples.
For our purposes, the most important implication of these results is that the AI
classification pipelines agree as much with human raters as other humans do, and
this indicates that the automatic classifications are acceptable substitutes for human
classifications.
We also report the human evaluators’ comparisons of the three pipeline’s classifica-
tions against their own in a stacked bar chart (Figure 20). No statistically significant
differences were found across the three pipeline variants based on either the Friedman
test (p= 0.090) or a repeated-measures ANOV A (p= 0.383). However, the Single
Prompt Full Ontology approach appears to achieve the highest overall rating, receiv-
ing more “better” and “equally good” ratings and fewer “worse” ratings than the
other models.
Most importantly for our purposes, the human annotators said that∼81% of the
AI classifications are as good as or better than their own. And this provides another
41

Fig. 20:A diverging stacked bar chart showing human evaluation of model
classifications relative to their own.The skew toward the right (red) indicates
that in over 15% of cases, human annotators rated the AI’s classification and its rea-
soning as superior to their own initial judgment. The skew toward the left (blue)
indicates that in over 18% of cases, human annotators rated the AI’s classification
and its reasoning as inferior to their own initial judgment. Overall, human annotators
judged the AI classifications to be as good as their own in over 60% of cases, with
roughly comparable proportions rated as better than (over 15%) or worse than (over
18%). With the final model we used (SPFO), human annotators rated the AI classifi-
cations as equal to or better than their own in 81.4% of cases.
indication that our automated classification pipeline is at least as good as human
classifications, while also being much faster and cheaper.
These findings are also broadly consistent with prior human validation results
reported by Anthropic [32]. Their classification task was, in some sense, easier than
ours, since their human judges were judging binary acceptability over (a) a 3-level task
hierarchy (vs. a median depth of 9 levels in our ontology) and (b)∼100 categories (vs.
15,989 activities in our ontology). But they observed an 86% human-judged match
rate, which is roughly comparable to our finding that∼81% of AI classifications were as
good or better than human annotations. This comparability suggests that LLM-based
classification can scale to much deeper and more fine-grained taxonomies.
6.5.2 Manual classification
In the study of robotic systems, the research team did not rely on the automated
classification pipeline used for the TAAFT applications. Instead, the team manually
assigned the subclasses of robotic systems to activity nodes in the ontology. This was
possible because the IFR dataset includes only 66 subclasses.
Two authors with expertise in robotics independently mapped each IFR subclass to
a single activity in the ontology. In many cases, a subclass label corresponded directly
to a specific activity, without judgment being required. For example, the “Transporta-
tion and logistics” subclass was readily classified under “Transport physical object.”
In other instances, greater judgment was required. If disagreements arose, they were
resolved through discussion and review by the full author team.
Table G12 in the Appendix G.1 provides the final mapping of IFR subclasses to
ontology activities.
42

6.6 Combining usage measures of AI software applications and
robotic systems
In the results in Sections 2.2 and 2.3 below, we measured AI usage intensity in terms of
the number ofunitsof AI software applications and robotic systems, respectively. But
in Section 2.4, we wanted to see a holistic view that combines both kinds of systems.
To do this, we integrated the data from the TAAFT and IFR datasets. But because
AI software applications and robotic systems differ so substantially, merely comparing
the number of units deployed of each may not yield any meaningful insights. Therefore,
to assess the impact of both of these technologies simultaneously, we needed a common
metric for comparison. For this purpose, we converted the unit volume for each type
of system intomarket valuesexpressed in US dollars. This served as a measure of the
intensity of AI usage, which we take as a proxy for AI applicability.
For AI software applications in the TAAFT dataset, we first estimated relative
marketsharesusing the number of saves, prices, and billing frequency. Then, to obtain
marketvalueestimates, we multiplied the respective market shares for each appli-
cation by the global market value of non-robotic AI applications in 2024. To obtain
this number, we subtracted the global market value of robotic systems (USD$46.1
billion [41, p. 7]) from the overall AI market value (USD$186.4 billion [42, p. 20]).
This results in an estimate of USD$140.3 billion for the market value of all AI soft-
ware applications. Finally, we estimated the market value of AI applications in each
ontology activity by aggregating the market values of all the individual applications
classified into that activity. A detailed description of this method for calculating the
market value of AI applications is presented in Appendix H.2.
For activities linked to robotic systems, we estimated market value by starting with
the global robotics market size of USD 46.1 billion in 2024, as reported by Statista [41,
p. 7]. We then noted the share of the overall market accounted for by each key robotics
industry segment (e.g., industrial, medical, consumer, etc.), again using data from
Statista [41, p. 10]. We next estimated an average unit price for each of the 66 IFR
robot subclasses through a combination of research in industry and manufacturer
sources and calibration based on linking price ranges with the segment market shares
reported by Statista. Once assumptions about average system price were in place, 2024
revenues for each subclass were calculated by multiplying unit volume and average
system price. Revenues were then assigned to the activities into which each subclass
had been classified. Full methodological details, mappings, and calculation procedures
are provided in Appendix H.3.
7 Acknowledgments
This research has been supported: (a) by the National Research Foundation (NRF),
Prime Minister’s Office, Singapore, under its Campus for Research Excellence and
Technological Enterprise (CREATE) program, through the Mens, Manus and Machina
(M3S) interdisciplinary research group (IRG) of the Singapore–MIT Alliance for
Research and Technology (SMART) center, (b) by Google.org through the MIT
Pathways for AI Training and Hiring (PATH) program, (c) by the Toyota Research
Institute, and (d) by the MIT Quest for Intelligence. We are especially grateful to
43

Andrei Nedelcu and Tudor Iliescu, from There’s An AI For That, for providing the
data about AI software applications that we analyzed. We also especially thank Steven
Rick for early work that led to this project; Sam Ouhra and Soe Min Thant for their
software development support; Xinyue Chen, Zhexuan Ma, and Jiacheng Zhang for
their assistance in data analysis; and Emily Hu and Iyad Rahwan for helpful sugges-
tions on the writing of the paper itself. In addition, we are very grateful to the following
for their helpful advice at various stages of the project: Abdullah Almaatouq, Charles
Fine, Gianni Giacomelli, Isabella Loaiza, Armando Solar-Lezama, Nancy Taubenslag,
Dicle Uzunyayla, and Michelle Vaccaro.
44

Appendix A Related work
Assessing the potential future impact of AI requires detailed knowledge of work activi-
ties. The most important sources of information about work activities are occupational
databases assembled by national governments. The largest and most widely used is
the U.S. Dept of Labor’s Occupational Information Network (O*NET) [5] and its
predecessor, the Dictionary of Occupational Titles (DOT) [43].
In addition to collecting data on worker characteristics and work context for each
occupation, O*NET also gathers detailed information on work activities through sur-
veys. Survey respondents receive a questionnaire that lists tasks previously associated
with their occupation and are asked how important each task is in their current job.
Respondents can also add new tasks that have not been included in the standardized
list.
As noted above, O*NET covers over 900 occupations and lists more than 20,000
work tasks, DW As, IW As, and GW As.
Other governments have developed similar datasets, for example, Singapore’s
Skills Future [44] and the EU’s European Skills, Competences, Qualifications and
Occupations (ESCO) [45].
The primary purpose of occupational databases is to provide information to peo-
ple who are seeking work or planning careers. These databases are also valuable to
government entities responsible for education and workforce training.
In the early 2000s, these sources began to be used by researchers to gain insights
into the impact of new technologies on the workplace. One influential early study
[1] grouped occupations based on whether they primarily involved undertaking rou-
tine vs. non-routine tasks. The rationale was that ever more capable computers and
robots would increasingly be able to replace humans in performing repetitive tasks
that involved following explicit instructions. This study found that occupations with
many routine tasks had experienced job losses and wage reductions in the 1980s and
1990s.
This initial work spurred a plethora of subsequent studies that examined the impact
of new technologies on tasks and jobs. This stream of work came to be known as
employing the “task approach” or “task-based approach,” because of its focus on the
properties of tasks performed within an occupation, as opposed to other features of
the occupation like skills, work contexts, education levels, etc. [2].
Most studies undertaken before 2010 relied on grouping occupations listed in the
DOT, based on commonalities in their underlying tasks. The impact of new tech-
nologies on each occupational grouping was then assessed. After O*NET went online
in 2008, researchers began to take a finer-grained approach by examining the poten-
tial impact of emerging technologies not only on groups of occupations but also on
individual occupations and even individual tasks.
One influential study [3] examined the O*NET tasks associated with occupations
and projected the potential for information technology to drive job losses in each.
Another study [4] developed a 21-step rubric to identify tasks machine learning (ML)
could perform and then used it to assess ML’s potential impact on individual O*NET
tasks and, in turn, occupations where those tasks were important.
45

In the realm of physical work, recent studies have suggested that industrial robots
may affect workplace patterns in different ways than service robots [46, 47]. These find-
ings highlight the need for fine-grained, task-level analyses to delineate the potentially
variegated impacts of different types of robotic systems.
After the launch of ChatGPT in 2022, a number of researchers undertook studies
to examine the impact of generative AI systems. A group of controlled experiments
showed generative AI could increase output, speed, and/or quality in tasks as disparate
as writing [48], customer support [49], software development [50] and duties typically
undertaken by management consultants [51]. Notably, these studies all examined the
impact of generative AI on discrete tasks in particular organizational settings, but
none provided generalized findings across a broad range of tasks.
In the past year, several leading LLM developers—Anthropic [32, 52],
Microsoft [33], and OpenAI [36]—have used a task-based approach to examine the
impact of their systems on work practices. Anonymized data from prompt logs was
mapped against tasks in the O*NET database, and the results were then aggregated at
various levels to identify occupations and categories of tasks most likely to be affected
by the usage of LLMs in the future.
Not surprisingly, LLMs were primarily used for information-related tasks, such as
writing, software development, obtaining information, and conveying information to
others (for example, in response to customer inquiries). One additional interesting
finding was that over time, users increasingly asked LLMs to undertake larger and
more complex tasks, while also providing the tool with less guidance [52]. Table A1
summarizes the data sources used and the approach employed in these studies.
These studies have identified tasks for which users have most commonly asked
general-purpose LLMs to provide help. But they did not examine the potential impact
of AI across the full range of work tasks, nor did they identify tasks where other AI
tools with different functionality may have an impact.
In the approach described in this paper, we classify work activities using a prin-
cipled, systematically structured, and comprehensive ontology. By grouping similar
activities into “family trees” of specific, related categories, we avoid some of the confu-
sion caused by O*NET and previous classification systems. And we believe that this,
together with rich data sources like those we analyze here, can help us gain a more
precise understanding of the workplace changes occurring today and likely to occur in
the future.
46

T able A1:Summary of approaches used by Anthropic, Microsoft, and
OpenAI in studies of users’ conversations with their LLMs.
Study sponsor Anthropic Microsoft OpenAI
LLM employedClaude Copilot ChatGPT
Approximate num-
ber of conversations
with LLMs in dataset
1 million 200,000 1 million
Method to map user
conversations
Claude used to
position each con-
versation within
three-level hierar-
chical groupings
of O*NET tasks
developed by the
Anthropic research
team
GPT-4o used to map
each conversation to
best-fitting O*NET
Intermediate Work
Activity (IW A)
GPT-5 mini used
to map each con-
versation to the
best-fitting O*NET
Intermediate Work
Activity (IW A)
Level of aggregation
at which task classifi-
cation is reported
O*NET tasks and
associated occupa-
tions/skills
IW As, which are
linked to relevant
Generalized Work
Activities (GW As);
IW A data then used
to assess potential
future impact of
LLMs on occupations
IW A data aggre-
gated and reported
at GW A level; IW A
data also mapped to
24 categories created
by OpenAI to classify
features and capabil-
ities of current and
future GPTs
Source: Anthropic ([32, 52]), Microsoft ([33]), and OpenAI ([36])
47

Appendix B Ontology Construction Details
B.1 Details on Initial Explorations
Before we established the methodology described in the main paper, we explored
a number of different approaches, including using automated methods only, using
humans only, and using other knowledge sources for reference.
Using humans only, we attempted to organize O*NET tasks that contain frequently
occurring verbs, such as “Direct,” “Administer,” “Manage,” “Clean,” etc., into a hier-
archical structure. From this process, we gained several insights: 1) tasks needed to be
broken down into atomic units (focused on verb-object pairs), as compound tasks are
difficult to organize hierarchically, and 2), we needed to differentiate between different
meanings of the same word (e.g. “administer program” vs “administer drug”), and
different words with the same meaning (e.g. “administer drug” vs “dispense drug”).
These insights led to the design principles ofatomicityandspecificity.
Because human-only approaches would not be feasible with a dataset as large as
O*NET, we explored the use of LLMs as a scalable approach to process large amounts
of data. Working with LLMs only, we explored both using multiple steps to construct
the hierarchy (first having an LLM organize the most frequently occurring verbs in
O*NET, then using separate LLMs to organize subtrees beneath those verbs), as well
as a single step (giving all verbs in O*NET to an LLM along with a comprehensive
prompt specifying the desired properties of the hierarchy). We found that it was
difficult to achieve the elegance and logical consistency we desired using LLMs only,
even after many iterations of prompt engineering. Moreover, we found that multi-step
approaches made it easier for LLMs to maintain logical consistency, and for the output
to be more interpretable by our team. We also briefly explored using hierarchical
clustering of semantic embeddings. However, neither LLMs nor embedding clustering
could provide the specificity feature we needed.
Thus, we explored bringing in existing lexical and ontological databases to ground
the hierarchy construction. While we looked into FrameNet [53], SUMO [54], and other
ontologies, we ultimately decided to use WordNet for its extensive definitions, hyper-
nym relationships, and broad usage across existing research. By automating (using
LLMs) the definition-selection process for verbs in their task context, we could lever-
age WordNet’s existing hypernym structure as a starting point for our own hierarchy.
Ultimately, we ended up using mostly human editing of the WordNet-based hierar-
chy to produce our initial draft of the ontology. Once we had established a structure
that we thought met our principles, we used more LLM assistance in expanding this
structure to incorporate more activities.
B.2 Hierarchy Trees from WordNet
The following is a full list of the 60 top-level “synsets” (sets of synonyms that comprise
a single meaning) from the WordNet hierarchy trees that appear in O*NET tasks,
DW As, IW As, and GW As. Wordnet includes multiple definitions for many verbs, and
the definition we used is indicated by the suffix v.01, v.02, etc. The prefix [virtual]
48

indicates when the synset does not directly appear in an O*NET item, but rather is
the top-level parent of synset(s) that do directly appear.
[virtual] account.v.02
[virtual] act.v.01
[virtual] agree.v.01
[virtual] change.v.02
[virtual] create.v.02
[virtual] decide.v.01
[virtual] examine.v.02
[virtual] express.v.02
[virtual] forget.v.01
[virtual] get rid of.v.01
[virtual] guide.v.05
[virtual] have.v.01
[virtual] include.v.01
[virtual] induce.v.02
[virtual] kill.v.01
[virtual] mean.v.03
[virtual] perceive.v.01
[virtual] prevent.v.02
[virtual] show.v.04
[virtual] spread.v.01
[virtual] take.v.08
[virtual] think.v.03
[virtual] touch.v.01
[virtual] trade.v.01
[virtual] transfer.v.05
[virtual] understand.v.01
[virtual] unmake.v.01
[virtual] use.v.01
[virtual] watch.v.01
address.v.02
analyze.v.01
change.v.01
close.v.01
complete.v.05
confirm.v.01
connect.v.01
control.v.01
correspond.v.03
cover.v.01
cultivate.v.01
determine.v.01
enter.v.01
enter.v.02
exercise.v.04
gather.v.01
get.v.01
hire.v.01
make.v.01
meet.v.01
move.v.02
perform.v.01
remove.v.01
search.v.01
start.v.08
stop.v.01
support.v.01
take.v.04
travel.v.01
treat.v.03
work.v.01
B.3 Placement of previously omitted meanings
The construction of the initial hierarchy draft omitted 644 synsets from O*NET tasks,
for two types of reasons: first, synsets that were flagged by the LLM definition checker
to be invalidly assigned were omitted to allow manual definition assignment in the
Revision phase; second, synsets that infrequently occurred in O*NET were omitted
to reduce the number of hierarchical trees to make it more manageable for LLMs and
humans to organize into an overarching framework. To place these omitted definitions,
an LLM was used to make an initial check and placement recommendation for each
synset. Each prompt includes the full initial hierarchy and representative O*NET tasks
using that synset, as well as the verb’s definition, synonyms, and hypernym path from
WordNet.
The model’s returned output included a choice to either create a new node or
append the verb as a synonym to an existing one, the full recommended path to place
the synset, and a short explanation if the synset was deemed incorrect for the associ-
ated tasks. Each path was deterministically validated as a real path in the hierarchy,
and the LLM was re-prompted up to three times to replace invalid recommendations.
A subset of outputs was manually reviewed, leading to prompt adjustments empha-
sizing the importance of deeper node selection, clarifying the identification of incorrect
synsets, and creating a parallel run without the verb path to test whether better
recommendations would be made. This updated prompt was used over the missing
49

O*NET tasks and synsets a second time, and the resulting recommendations were
reviewed and edited by humans to finalize the placement.
B.4 Principles for direct-object classification system
To classify the direct objects of verb-object pairs into high-level categories (Physical
Object, Information, Actor, Activities), we developed definitions, examples, and dif-
ferentiation principles for the categories that were fed into an LLM classifier, detailed
below:
Physical Object
• Tangible, material things whose physical properties (shape, weight, size, location,
mechanical use) are important for the activity.
• Includes tools, artifacts, natural objects, substances, and places.
• Examples: lamp, hat, tree, house, city, glass of water.
Information
• Abstract entities whose meaning, content, or representation is important for the
activity.
• Includes knowledge, ideas, data, qualities, quantities, and symbolic representa-
tions.
• Examples: the contents of a book, a YouTube video, a teacher’s answer, the
concept of freedom, beauty, number.
Actor
• Entities that perform or can be treated as performing actions.
• Includes people, animals, organizations, groups, and roles.
• Examples: teacher, dog, government, team, leader, citizen.
Activity
• Happenings, occurrences, or activities.
• Includes both bounded events (specific occurrences) and activities (processes,
practices).
• Examples: wedding, earthquake, meeting, competition, concert, management,
research, inspection, negotiation, teaching, training, conversation, swimming,
celebration, investigation, design, maintenance, construction.
The distinction between categories depends on what aspects of the objects are
important for the task context. For example, for our purposes, we treat a book as
an information object if it is being used for what it “means” or “represents.” But if
the same book is used only as a doorstop, we would treat it as a physical object. In
general, we treat something as a physical object if its most important properties for the
50

activity are physical, and we treat it as information if its most important properties
are its meaning.
B.5 Verb-object inconsistency resolution system
Our way of choosing definitions for activities, relying on WordNet definitions, often
leaves room for ambiguity in verbs with meanings that apply to both physical objects
and information. For example, the definition chosen for “Cut” from WordNet is “sep-
arate with or as if with an instrument,” which can apply to both physical objects and
information. However, in our ontology activities acting on physical objects and activi-
ties acting on information are in separate branches. Therefore, we needed more specific
versions of “Cut” in both branches: “Cut physical objects” and “Cut information.”
We used our noun classification framework to identify 615 conflicts between verb
path and object classification (for example, if “Cut Music” was classified under the
path “Act on physical objects> . . . >Cut physical objects”, it should be moved to a
mirror branch under “Act on information> . . . >Cut information”). Some instances
of conflict, however, do not reflect a verb misclassification. For example, “Observe
equipment” should still be under “Act on information,” even though equipment is a
physical object, because the process of observation involves only processing informa-
tion. To deal with these complexities, we used a combination of LLM reasoning and
human judgment to decide what to do with each instance of conflict identified. In
each case, an LLM model made a recommendation with reasoning about whether to
move the task to the mirror category or not, and then a human reviewed. We first
tested the LLM on a subset of conflicts, then updated the prompt to improve it before
running the process on the full batch; then, two of our human editors reviewed each
recommendation and revised or accepted it.
B.6 Distinguished activities with the same name but
different meanings
We distinguished activities for which O*NET used the same verb for different mean-
ings. Two categories of such distinctions are made. First, activities using the same title
but linked to different WordNet meanings were distinguished through manual human
editing. Second, activities using the same title, linked to the same WordNet meaning,
but distinguished based on direct object in our classification (e.g. “Adapt (informa-
tion) (Adapt.v.01)” and “Adapt (physical) (Adapt.v.01)”) were identified through
automated checks for verb-object inconsistencies (see Appendix B.5) and validated by
human editors. The following is a full list of differentiations of 215 activities with the
same name but different meanings:
• Access (Access.v.01), Access (physical) (Access.v.02)
• Adapt (information) (Adapt.v.01), Adapt (physical) (Adapt.v.01)
• Add (information) (Add.v.01, Include.v.01), Add (physical) (Add.v.01,
Include.v.01)
• Address (Address.v.03), Address (express) (Address.v.02, Deliver.v.01), Address
(solve) (Address.v.05)
51

• Adjust (information) (Adjust.v.01), Adjust (physical) (Adjust.v.01)
• Administer (manage) (Administer.v.01), Administer (treat) (Administer.v.04)
• Admit (accept) (Admit.v.03), Admit (let in) (Admit.v.02)
• Align (information) (Align.v.01), Align (physical) (Align.v.01)
• Alter (information) (Alter.v.03), Alter (physical) (Alter.v.03)
• Apply (for) (Apply.v.03), Apply (physical) (Put on.v.07)
• Arrange (make arrangements for) (Arrange.v.02), Arrange (put in proper or
systematic order) (Arrange.v.01)
• Attend (care) (Attend.v.02), Attend (go to) (Attend.v.01)
• Balance (account) (Balance.v.02), Balance (equilibrate) (Balance.v.01)
• Blend (information) (Blend.v.01, Blend.v.03), Blend (physical) (Blend.v.01,
Blend.v.03)
• Blow (air) (Blow.v.14), Blow (shape by blowing) (Blow.v.06)
• Break (Break.v.02, Sever.v.01), Break (into components) (Break.v.02)
• Call (Call.v.05), Call (out) (Call.v.25)
• Capture (catch) (Capture.v.06), Capture (collect) (Trap.v.03)
• Charge (electrically) (Charge.v.24), Charge (money) (Charge.v.03)
• Clean (information) (Clean.v.01, Clean.v.02), Clean (physical) (Clean.v.01,
Clean.v.02)
• Clear (information) (Clear.v.05, Clear.v.22), Clear (physical) (Clear.v.05,
Clear.v.22)
• Collect (information) (Roll up.v.02), Collect (physical) (Roll up.v.02)
• Complete (activity) (Complete.v.01), Complete (information) (Complete.v.05)
• Configure (information) (Configure.v.01), Configure (physical) (Configure.v.01)
• Connect (information) (Affix.v.01, Attach.v.01, Connect.v.01, Join.v.02), Con-
nect (physical) (Affix.v.01, Attach.v.01, Connect.v.01, Join.v.02)
• Construct (information) (Construct.v.01, Raise.v.09), Construct (physical) (Con-
struct.v.01, Raise.v.09)
• Copy (information) (Copy.v.04, Duplicate.v.01, Reproduce.v.01, Twin.v.01),
Copy (physical) (Copy.v.04, Duplicate.v.01, Reproduce.v.01, Twin.v.01)
• Customize (information) (Customize.v.02), Customize (physical)
(Customize.v.02)
• Cut (information) (Cut.v.01), Cut (physical) (Cut.v.01)
• Defend (prevent) (Defend.v.02), Defend (verbally) (Defend.v.01)
• Deposit (money) (Deposit.v.02), Deposit (physical) (Situate.v.02)
• Develop (chemically) (Develop.v.15), Develop (idea) (Explicate.v.02)
• Disconnect (information) (Disconnect.v.02), Disconnect (physical) (Discon-
nect.v.02)
• Dock (Dock.v.05), Dock (cut) (Dock.v.04)
• Draw (drawing) (Draw.v.04, Draw.v.06), Draw (extract) (Draw.v.05)
• Dress (butchery) (Dress.v.06), Dress (clothes) (Dress.v.02), Dress (wound)
(Dress.v.14)
• Drive (force) (Force.v.06), Drive (operate) (Drive.v.01, Drive.v.03)
• Engage (people) (Involve.v.06), Engage (physical) (Engage.v.10)
• Enter (Enter.v.01), Enter (information) (Enter.v.01)
52

• Extend (information) (Expand.v.02, Extend.v.17, Widen.v.04), Extend (physical)
(Expand.v.02, Extend.v.17, Widen.v.04)
• File (formal) (File.v.01), File (information) (File.v.05), File (physical) (File.v.05),
File (surface) (File.v.02)
• Fill (information) (Fill.v.01, Inflate.v.02), Fill (physical) (Fill.v.01, Inflate.v.02)
• Finish (information) (Complete.v.02), Finish (physical) (Complete.v.02)
• Frame (compositional) (Frame.v.04), Frame (physical) (Frame.v.02)
• Gather (information) (Gather.v.01), Gather (physical) (Gather.v.01)
• Grade (Grade.v.03), Grade (shape) (Grade.v.02)
• Harmonize (information) (Harmonize.v.04, Harmonize.v.05), Harmonize (physi-
cal) (Harmonize.v.04, Harmonize.v.05)
• Incorporate (information) (Incorporate.v.02), Incorporate (physical) (Incorpo-
rate.v.02)
• Insert (information) (Feed.v.04, Insert.v.01), Insert (physical) (Feed.v.04,
Insert.v.01)
• Install (information) (Install.v.01), Install (physical) (Install.v.01)
• Lay (Lay.v.03), Lay (physical) (Lay.v.03, Lay out.v.05, Range.v.05)
• Load (digital) (Load.v.03), Load (physical) (Load.v.01)
• Maintain (information) (Conserve.v.02, Keep.v.01), Maintain (physical) (Con-
serve.v.02, Keep.v.01)
• Map (between) (Map.v.06), Map (out) (Map.v.01)
• Mark (information) (Code.v.01, Mark.v.02, Tag.v.01), Mark (physical)
(Mark.v.02)
• Match (align) (Match.v.01), Match (co-fund) (Match.v.02)
• Model (Model.v.03), Model (represent) (information) (Model.v.01, Model.v.05),
Model (represent) (physical) (Model.v.01, Model.v.05)
• Open (Open.v.01), Open (make available) (Open.v.06)
• Order (authoritative) (Order.v.01), Order (buy) (Order.v.02)
• Organize (analytically) (Organize.v.04, Structure.v.01), Organize (people or
events) (Hold.v.03, Organize.v.05)
• Orient (person) (Orient.v.02), Orient (physical) (Orient.v.03)
• Pack (compress) (Pack.v.02), Pack (into) (Pack.v.13), Pack (together) (informa-
tion) (Pack.v.01), Pack (together) (physical) (Pack.v.01)
• Paint (information) (Paint.v.02), Paint (physical) (Paint.v.02)
• Pass (achieve) (Pass.v.09), Pass (over) (Pass.v.05, Present.v.04)
• Patch (connect) (Patch.v.02), Patch (repair) (Patch.v.03)
• Perform (action) (Do.v.03, Perform.v.01, Prosecute.v.03, Take.v.01), Perform
(artistic) (Perform.v.03)
• Post (announcement) (Post.v.01), Post (financial) (Post.v.07)
• Prepare (information) (Fix.v.12), Prepare (physical) (Fix.v.12)
• Press (flatten) (Press.v.04), Press (touch) (Press.v.01)
• Process (information) (Process.v.01, Process.v.03), Process (physical) (Pro-
cess.v.01)
• Raise (funds) (Raise.v.04), Raise (physical) (Raise.v.02)
53

• Read (gauges, instruments, etc.) (Read.v.08), Read (out loud) (Read.v.03), Read
(something written or printed) (Read.v.01)
• Reassemble (information) (Reassemble.v.01), Reassemble (physical) (Reassem-
ble.v.01)
• Refine (information) (Refine.v.06), Refine (substance) (Refine.v.04)
• Regulate (authoritative) (Regulate.v.02), Regulate (modulate) (information)
(Regulate.v.01), Regulate (modulate) (physical) (Regulate.v.01)
• Remove (information) (Remove.v.01), Remove (physical) (Remove.v.01)
• Renew (information) (Regenerate.v.01), Renew (physical) (Regenerate.v.01)
• Repair (information) (Correct.v.01, Correct.v.08, Repair.v.01), Repair (physical)
(Correct.v.01, Correct.v.08, Repair.v.01)
• Replace (information) (Replace.v.01), Replace (physical) (Replace.v.01)
• Report (Report.v.01, Report.v.02), Report (to authorities) (Report.v.04)
• Roll (Roll.v.01), Roll (shape) (Roll.v.08, Roll Out.v.01)
• Run (movement) (Run.v.01), Run (perform) (Run.v.21), Run (placement)
(Run.v.03)
• Serve (deliver) (Serve.v.11), Serve (role) (Serve.v.02)
• Service (information) (Service.v.02), Service (physical) (Service.v.02)
• Shave (groom) (Shave.v.01), Shave (surface) (Shave.v.02)
• Sign (signal) (Sign.v.05), Sign (signature) (Sign.v.04)
• Snip (information) (Snip.v.02), Snip (physical) (Snip.v.02)
• Splice (information) (Splice.v.04), Splice (physical) (Splice.v.04)
• Strike (hit) (Strike.v.01), Strike (ignite) (Strike.v.11)
• Substitute (replace) (Substitute.v.01), Substitute (role) (Substitute.v.03)
• Synchronize (information) (Synchronize.v.01, Synchronize.v.03, Synchro-
nize.v.04), Synchronize (physical) (Synchronize.v.01, Synchronize.v.03,
Synchronize.v.04)
• Synthesize (information) (Synthesize.v.01), Synthesize (physical) (Synthe-
size.v.01)
• Tailor (information) (Tailor.v.01), Tailor (physical) (Tailor.v.01)
• Tap (draw from) (Tap.v.02), Tap (touch) (Tap.v.03)
• Touch Up (information) (Touch up.v.01), Touch Up (physical) (Touch up.v.01)
• Trace (analytically) (Trace.v.01), Trace (drawing) (information) (Trace.v.07),
Trace (drawing) (physical) (Trace.v.07)
• Transcribe (music) (Transcribe.v.03), Transcribe (write) (Transcribe.v.01)
• Travel (Transport self), Travel (Travel.v.01)
• Troubleshoot (information) (Trouble-shoot.v.01), Troubleshoot (physical)
(Trouble-shoot.v.01)
• Turn (on/off) (Turn.v.22), Turn (rotate) (Revolve.v.01, Turn.v.01, Turn.v.17)
• Upload (information) (Upload.v.01), Upload (physical) (Upload.v.01)
• Wrap (Envelop.v.01, Wrap.v.01), Wrap (gift) (Gift-Wrap.v.01)
54

B.7 Full list of activities with multiple inheritance
As described in Section 6.1.1, the ontology featuresmultiple inheritance, where activ-
ities have multiple parents. The full list of activities with multiple inheritance is
presented below1.
T able B2:Activities and their parent generalizations..
Activity Generalizations
Agree (Agree.v.01)Collaborate (Collaborate.v.01)
Exchange information (Change.v.06)
Brush (Brush.v.04)Reorient physical objects
Touch (Touch.v.01)
Casket (Casket.v.01)Cover (Cover.v.01)
Enclose (Enclose.v.03)
Communicate (transfer
information end-to-end)
Transfer information
End-to-end information transfer
Conduct (Conduct.v.01,
Conduct.v.02)
Manage (Manage.v.02, Treat.v.01)
Perform action (Do.v.03, Perform.v.01, Prosecute.v.03,
Take.v.01)
Draw (extract)
(Draw.v.05)
Extract (Draw.v.07, Extract.v.01)
Pull (Pull.v.01, Pull.v.17)
Estimate
(Estimate.v.01)
Calculate (Calculate.v.01, Calculate.v.02)
Decide
Express LiveExpress information
Provide information
Fly (Fly .v.03)Transport self as passenger
Operate
Gather (information)
(Gather.v.01)
Combine information (Combine.v.04)
Get information (Get.v.01, Obtain.v.01, Procure.v.01)
Gather (physical)
(Gather.v.01)
Combine physical objects (Create from raw
material.v.01)
Get physical objects (Get.v.01, Obtain.v.01,
Procure.v.01)
Continued on next page
1Suffixes such as “.v.01” correspond to WordNet sense identifiers and are included to differentiate distinct
meanings of the same word.
55

T able B2:Activities and their parent generalizations.(continued)
Activity Generalizations
Implement (Carry
through.v.01, F ollow
through.v.02)
Act on activities
Manage (Manage.v.02, Treat.v.01)
Improve (Better.v.02,
Enhance.v.02)
Act on activities
Manage (Manage.v.02, Treat.v.01)
Transform information (Change.v.01, Rework.v.01,
Transform.v.02, Work.v.05)
Organize (analytically)
(Organize.v.04,
Structure.v.01)
Reason (Reason.v.03, Think.v.03)
Transform information (Change.v.01, Rework.v.01,
Transform.v.02, Work.v.05)
Propose (Offer.v.04,
Project.v.08,
Propose.v.01)
Plan (Mastermind.v.01, Plan.v.02, Plan.v.03)
Send information (Send.v.02, Transmit.v.04)
Pull (Pull.v.01,
Pull.v.17)
Move physical objects
Remove (physical) (Remove.v.01)
Respond (React.v.01)Provide service
Send information (Send.v.02, Transmit.v.04)
Sign (signal) (Sign.v.05)Express Live
Inform (Advise.v.02, Inform.v.01)
T alk (T alk.v.02)Express Live
Send information (Send.v.02, Transmit.v.04)
Unwind (Unwind.v.01)Shape (Change shape.v.01, Shape.v.02, Shape.v.03)
Turn or rotate (Revolve.v.01, Turn.v.01, Turn.v.17)
Upload (information)
(Upload.v.01)
Send information (Send.v.02, Transmit.v.04)
Store information (Conserve.v.02, Store.v.01, Store.v.02)
Wire (Wire.v.01)Connect physical objects (Affix.v.01, Attach.v.01,
Connect.v.01, Join.v.02)
Equip (Equip.v.01)
56

Appendix C Ontology Platform Functionality
To develop this ontology of work activities, we built a curation platform that supports
synchronous multi-user editing, search, and structured browsing of a large activity
knowledge base. The platform is designed to support the complex, hierarchical rela-
tionships inherent in process taxonomies while providing the coordination mechanisms
necessary for coherent, auditable collaboration.
Our design builds on the MIT Process Handbook [55], which demonstrated the util-
ity of organizing knowledge about processes through generalization-specialization and
part-whole decomposition. While early ontology engineering relied heavily on manual
expert curation [6], prior work has shown that LLMs can accelerate ontology devel-
opment when used as assistants rather than sole authors [56]. Our platform adopts
a human-in-the-loop architecture [57], with hybrid search mechanisms that combine
semantic retrieval with keyword matching [58], so contributors can rapidly locate
candidate nodes while maintaining domain specificity and controlling hallucination
risks.
To preserve structural coherence, the platform requires each node to be linked
to at least one generalization, blocks edits that would orphan nodes, flags near-
duplicate nodes (based on lexical + embedding similarity) to discourage redundant
node creation, and maintains node-level change histories with attribution. The plat-
form also exports versioned ontology snapshots (in JSON format) so that analyses and
automated classification can reference a fixed ontology instance.
The platform is implemented with Firestore (data storage), Firebase Authen-
tication (user access), Google Cloud Run (deployment), Next.js (web framework),
Material UI (components), Jest (testing), Y.js (real-time collaboration), and D3.js
(visualization).
C.1 Data Structure and Inheritance
The platform represents the ontology as a directed graph where nodes represent simple
activities or broader processes. Following the approach in the Process Handbook, these
nodes are organized through two primary kinds of hierarchical relationships:typesand
parts.
• Types (specializations and generalizations): These relationships capture
the taxonomic structure. A specialized activity (specialization) inherits properties
(such as AI applicability and parts) from its generalization(s) but can also override
them to fit a specific context.
–Example: Consider the activity “Select.” It is categorized as a specialization
of “Decide.” We classify its further specializations (e.g., “Select job candi-
date”) based on the object being selected, the reason for selection, or the
selection process, narrowing down level-by-level until reaching atomic tasks.
• Parts (parts and is-part-of ): In addition to taxonomic structure, the platform
also captures the internal structure of activities. Each activity can be decomposed
into a set of sub-activities, referred to as “parts,” and each activity can also be
part of a larger activity.
57

–Example: The activity “Select” is decomposed into parts such as “Gather
information,” “Identify alternatives,” “Make selection,” and “Communicate
selection.” And some of these parts (e.g., “Gather information”) might also
be part of other larger activities.
–Inheritance of Parts: The platform supports sophisticated inheritance logic
for these parts. For instance, “Gather information” and “Identify alterna-
tives” are directly inherited from the parent activity “Decide,” while “Make
selection” is a specialization of the corresponding part in “Decide.”
C.2 Navigation and Visualization
To assist users in navigating this high-dimensional structure, the platform provides
three connected interfaces:
• Graph View: A Directed Acyclic Graph (DAG), visualizing the broader network
of specializations and generalizations.
• Outline View: A nested list view allowing users to rapidly expand or col-
lapse branches of the ontology. Contributors can restructure relationships (e.g.,
changing a node’s generalization) via drag-and-drop actions in this view.
• Node View: A detailed view displaying the node’s metadata, description, actors,
and inheritance paths. To prevent accidental modifications during navigation,
users can toggle a “Read-Only” mode.
C.3 Hybrid Semantic Search
To facilitate discovery within the ontology, we implemented a hybrid search engine
that includes both keyword search and semantic search. For the semantic search,
we embedded every node—including its title, description, synonyms, and the titles
of its parents and children—using OpenAI’s “text-embedding-3-large” model. These
embeddings are stored in a Chroma vector database. When a user queries the system,
we retrieve nodes with the highest cosine similarity to the embedding of the query,
and we display query results in a list that alternates between keyword search results
and semantic search results.
C.4 Synchronous Collaboration and Coordination
Given the scale of the ontology, coordination among contributors is critical. The
platform includes several socio-technical mechanisms to maintain coherence:
• Real-Time Synchronization: We implemented a synchronous editing archi-
tecture. When a user modifies a node, the changes are instantly propagated to
all other active clients—including users viewing linked nodes or those inheriting
from the modified node—ensuring a consistent state across the distributed team.
• Granular History and Attribution: Every node maintains an interactive
edit history, allowing users to visualize its evolution. Similarly, a global history
log tracks individual user contributions, providing transparency regarding how
different contributors shape the ontology.
58

• Contextual Communication: To resolve semantic ambiguity in real-time, the
platform features an integrated chatroom for high-level alignment. Additionally,
users can leave threaded comments directly on specific nodes and tag (@mention)
other contributors, anchoring discussions to the relevant data points.
C.5 Access and Extensibility
Write access is restricted to authorized accounts to maintain content quality. The
platform is architected for openness; it provides a documented API for programmatic
interaction and allows users to export the full ontology in JSON format. The archi-
tecture supports broader access for human and AI contributors, subject to access
controls.
59

Appendix D Evolution and evaluation of automated
classification architectures
This appendix provides implementation details for the automated classification
pipeline used to map AI software applications to ontology activities (Section 6.5.1).
We focus on the three pipeline variants evaluated in our human validation study: Sin-
gle Prompt Partial Ontology (SPPO), Multi-Prompt Partial Ontology (MPPO), and
Single Prompt Full Ontology (SPFO). We summarize the task and evaluation criteria,
present the model pipeline descriptions, and include the LLM prompts (with shared
text de-duplicated).
D.1 Task and evaluation setup
The core classification task is to map each AI application to themost specific ontology
activity whose scope fully covers the application ’s primary activity(the verb-object
action the application performs or helps perform).
All comparisons use a fixed ontology snapshot so that models are evaluated against
the same set of node titles and definitions. We define a node as aleafif it has no
specializations in the snapshot, and asnear-leafif all of its direct children are leaves.
We define ahallucinationas any output whose predicted node title does not exactly
match a node title in the snapshot. Unless otherwise noted, evaluations use a shared
pilot set of applications and the same base model (GPT-5.1 with high-reasoning-effort)
so that differences reflect pipeline design rather than underlying model choice.
In addition to the agreement metrics reported in the main text (Wu-Palmer simi-
larity and weighted Cohen’sκ; Appendix E.2), we tracked three practical criteria that
affect usefulness at scale:
• Leaf specificity: the fraction of predictions that are leaves or near-leaves.
• Hallucinations: the rate of outputs that are not valid ontology nodes under the
fixed snapshot.
• Cost and latency: prompt + completion tokens and wall-clock runtime per
application under a consistent batching and retry policy.
We also varied two controllable parameters:
• Retrieval depth (top-k): the number of candidate nodes returned by vector
search (e.g., 10, 25, 50, 100).
• Context window: how much node metadata (title, definition, synonyms,
parent/child links) is provided to the model when selecting a node.
D.2 Model architecture descriptions
Table D3 summarizes the three evaluated pipeline variants. For the human evalua-
tions, both the SPPO and MPPO models retrieved a shortlist of 100 candidate nodes
(k=100).
60

T able D3:Summary of automated classification pipeline variants
evaluated in the human validation study .All variants used the same base
model (GPT-5.1, high-reasoning-effort).
V ariant Ontology context Model calls Summary
SPPO (Single Prompt Partial Ontology) Retrieved shortlist
(top-k)
1 Retrieve candidate
nodes using appli-
cation text; one
prompt extracts
the verb-object
activity and selects
the best node from
the shortlist.
MPPO (Multi-Prompt Partial Ontology) Retrieved shortlist
(top-k)
2 First prompt
extracts a clean
verb-object activ-
ity; retrieval uses
this activity; sec-
ond prompt selects
the best node from
the shortlist.
SPFO (Selected) Full ontology
(cached)
1 Cache the full
ontology and use
one prompt to
extract the verb-
object activity and
select the best node
from the full hierar-
chy (no retrieval).
D.2.1 SPPO (Single Prompt Partial Ontology)
In SPPO, we retrieve a shortlist of candidate ontology nodes using semantic similarity
between the application description (title, tagline, and description) and pre-computed
node embeddings. We then prompt the model once to (i) identify a verb-object phrase
describing the application’s primary activity and (ii) select the most appropriate ontol-
ogy nodefrom the retrieved shortlist. This variant is efficient and works well when the
correct node appears in the shortlist, but it can fail when retrieval returns the wrong
sense for polysemous verbs or when the correct node is missing from the candidates.
D.2.2 MPPO (Multi-Prompt Partial Ontology)
MPPO decomposes the task into two LLM calls. The first call extracts a clean verb-
object description of the application’s primary activity. We then retrieve candidate
nodes using semantic similarity to this extracted activity (rather than to the full appli-
cation description), and the second call selects the most appropriate ontology node
from the retrieved shortlist. This decomposition reduced hallucinations and stabilized
outputs, but it tended to select higher-level nodes when the extracted activity was
generic, because the node-selection step only sees a limited slice of the ontology.
D.2.3 SPFO (Single Prompt F ull Ontology) (selected)
In SPFO, we remove retrieval entirely and instead cache the full ontology in the model
context. The model is prompted once to identify the application’s primary verb-object
61

activity and select the most specific matching ontology node from the full hierarchy. In
our evaluation, this variant achieved the best overall tradeoff between agreement with
human classifications, leaf specificity, hallucinations, and cost (with prompt caching
making full-context inference feasible at scale), so it is the variant used in the final
pipeline.
D.3 LLM prompts
SPPO and SPFO use the same base classification prompt; the main difference is
the content of theOntology Nodesfield (retrieved shortlist vs. full cached ontol-
ogy). MPPO adds an activity-extraction prompt as a first step, and its node-selection
step uses the same base prompt with a small modification to the input (it includes
the previously extracted activity) and output (it returns only the selected node and
rationale).
62

D.3.1 Base classification prompt (SPPO and SPFO)
/inf⌢-circle
## Role:
You are an analyst who classifies a software application according to: (a)
the main activity it performs or helps perform, represented as a ”verb
+ object” phrase, and (b) which of the nodes in the ontology (provided
as a JSON structure in the input) is the best classification for the main
activity. Work only with the supplied nodes and their fields; do not infer
or invent nodes or properties.
## Ontology Definition:
In our ontology, every node represents a work-related activity. The ontol-
ogy is represented as a long JSON structure, in which the title of each
node is a key and its value is a sub-ontology under that node.
If a node has many direct children, we group those children in collections.
These collection names are also represented as keys in the JSON structure,
but they are always in square brackets.
## Output:
Return a single JSON object only (no prose), with exactly these keys and
value types:
{
”main activity”: ”The single ’base-form verb + object’ describing the main
activity”,
”reasoning main activity”: ”Explain your reasoning for main activity. If
info is sparse or ambiguous, make the best-supported choice and note low
confidence in ”reasoning” fields.”,
”most appropriate node”: ”title of the ontology node”,
”most appropriate node rationale”: ”your reasoning for choosing this
ontology node”
}
## Constraints:
- Output must be valid JSON: double quotes around all strings, no trailing
commas, no extra keys or text.
- Always include one item in ”main activity”.
- Use base verb forms plus their direct object in ”main activity” (e.g.,
”write code”, ”conduct research”, ”summarize text”).
- To classify the main activity of the application: choose the most specific
node whose scope fully covers the main activity.
- These examples illustrate how to apply this principle:
1- For an app for automobile driving that plans a route to the user’s
destination:
The most specific node whose scope fully covers this app would be some-
thing like “plan route.” This node covers all the detailed navigational
decisions the app makes, but it is more specific than a node like “drive
car.”
63

/inf⌢-circle
2- For a “self-driving” car app that steers the car, accelerates, brakes, etc.,
but still requires a human to be behind the wheel and ready to take over
in unusual situations:
The most specific node whose scope fully covers this app would be some-
thing like “drive car.” There is no other simple description that fully covers
all the actions this app takes that is more specific than “drive car.”
3- For an image generation app that takes a verbal description of a
landscape and generates an image of a landscape based on this description:
A node like “generate landscape image” would fully cover the scope of this
activity even though in practice, a user might try many different verbal
descriptions before finding one that captured what the user wanted.
4- For a cleaning robot that can clean floors, dust furniture, and empty
trash cans:
The most specific node that covers all these kinds of cleaning might be
something like “clean rooms.” But if there isn’t any node like that in the
ontology, the best classification might be a node called “clean.” This node
is very general, but if there is no other node that covers all three activities
(clean floors, dust furniture, and empty trash cans) and is more specific
than “clean,” then “clean” might be the best classification.
Note that, in some cases, the above examples illustrate an app performing
an entire activity. In other cases, they illustrate an app helping a human
perform an activity. But in all cases, we try to choose the most specific
activity that fully covers the scope of what the app does.
## Procedure:
Internally follow this process:
1. From the provided application tagline and description, identify the main
activity the application performs or helps perform, represented as a ”verb
+ object” phrase.
2. Internally, analyze the ”verb + object” phrase and compare it to every
node in the ontology. For each node, consider all its information.
3. Select the node that best satisfies the classification principle and
examples above.
5. Produce the output JSON exactly as specified.
## Input:
### Ontology Nodes:
(THE NESTED ONTOLOGY GOES HERE.)
### Application Title:
(THE APP TITLE GOES HERE.)
### Application Tagline:
(THE APP TAGLINE GOES HERE.)
### Application Description:
(THE APP DESCRIPTION GOES HERE.)
64

D.3.2 MPPO step 1 prompt: activity extraction
/inf⌢-circle
## Role:
You are an analyst that describes a software application according to: (a)
what main substantive activity it performs or helps perform, represented
as a ”verb + object” phrase, and (b) whether it performs the whole activity
itself or helps a human perform the activity.
## Input:
- Application Title: (THE APP TITLE GOES HERE.)
- Application Tagline: (THE APP TAGLINE GOES HERE.)
- Application Description: (THE APP DESCRIPTION GOES HERE.)
## Output:
Return a single JSON object only (no prose), exactly with these keys and
value types:
{
”main activity”: ”The single ’base-form verb + object’ describing the main
activity”,
”reasoning main activity”: ”Explain your reasoning for main activity. If
info is sparse or ambiguous, make the best-supported choice and note low
confidence in ”reasoning” fields.”,
}
## Constraints:
- Output must be valid JSON: double quotes around all strings, no trailing
commas, no extra keys or text.
- Always include one item in ”main activity”.
- Use base verb forms plus their direct object in ”main activity” (e.g.,
”write code”, ”conduct research”, ”summarize text”).
## Procedure:
Internally follow this process:
1. From the provided application tagline and description, identify the main
activity it performs or helps perform, represented as a ”verb + object”
phrase.
2. Specify whether it performs the whole activity itself or helps a human
perform the activity.
D.3.3 MPPO step 2 prompt: node selection (differences from
base prompt)
MPPO’s node-selection step uses the base classification prompt above, with two
modifications:
• Theoutputis restricted to the selected node and rationale:
most appropriate nodeandmost appropriate node rationale.
65

• Theinputincludes the substantive activity extracted in step 1, and theOntology
Nodesfield contains a retrieved shortlist (top-k) rather than the full cached
ontology.
/inf⌢-circle
## Output (override):
Return a single JSON object only (no prose), with exactly these keys and
value types:
{
”most appropriate node”: ”title of the ontology node”,
”most appropriate node rationale”: ”your reasoning for choosing this
ontology node”
}
## Input (override):
In addition to the application fields, include the extracted activity:
- Substantive Activity: (SUBSTANTIVE ACTIVITY GOES HERE)
because (SUBSTANTIVE ACTIVITY REASONING GOES HERE)
And set ### Ontology Nodes to the retrieved shortlist (top-k) rather
than the full cached ontology.
All other instructions and constraints remain identical to the base
classification prompt.
D.4 Summary of lessons
Across these variants, retrieval was the dominant bottleneck: if the correct node was
missing or drowned in noisy candidates, downstream selection could not recover.
Adding richer node context helped when the model could reliably absorb it, and
decomposition improved stability at the expense of specificity. The full-context SPFO
variant provided the best overall tradeoff between agreement with human judgments,
specificity, hallucination rate, and cost, which is why it is used in the final pipeline.
66

Appendix E Additional details on human
classification process
E.1 Instructions to human annotators
We provided human annotators with detailed, structured instructions aligned with
the prompts used for the large language models (LLMs) performing the automated
annotations. This parallel design ensured conceptual consistency between human and
automated annotation procedures and facilitated comparability across annotations
from LLMs and humans.
• RoleYou are an analyst who classifies a software application according to: (a)
the main activity it performs or helps perform, represented as a “verb + object”
phrase, and (b) which of the nodes in the ontology is the best classification for
the main activity. Work only with the nodes included in the platform and their
fields; do not infer or invent nodes or properties.
• Ontology DefinitionIn our ontology, every node represents a work-related
activity. The ontology is organized as a hierarchical tree structure that represents
tasks across a wide range of occupations. It uses verbs and nouns to describe
these activities. It includes broad nodes (e.g., “Create information”), more specific
nodes (e.g., “Analyze”), and leaf nodes, the most specific level of the activities
(e.g. “Search literature”)
• InputYou receive a set of applications with the following information:
– Name of the application
– Application tagline
– Application Description
You have access to the platform of the ontology where you find the following
information:
– The ontology nodes
– A search engine to navigate the ontology
– A field with the description of each node and its generalizations and
specializations
• Output
– Main activity: The single base-form of [verb + object] describing the main
activity
– Reasoning of the main activity: Explain your reasoning for the main activity.
If info is sparse or ambiguous, make the best-supported choice and note low
confidence in “reasoning” fields.
– Most appropriate node: Choose the most appropriate node considering the
constraints and the procedure described below
– Most appropriate node rationale: Your reasoning for choosing this ontology
node
• Constraints
– Use base verb forms plus their direct object to describe the main activity
(e.g., “Write code,” “Conduct research,” “Summarize text”).
– To classify the main activity of the application, apply the following principle:
67

– Choose the most specific node whose scope fully covers the main activity.
• Examples (applying the classification principle)
1.Route-planning application for automobile driving.The most specific
node whose scope fully covers this app would be something like “Plan route.”
This node covers the detailed navigational decisions the application makes
and is more specific than a node such as “Drive car.”
2.“Self-driving” car application that steers, accelerates, and brakes,
but still requires a human to supervise and take over.The most
specific node whose scope fully covers this application would be something
like “Drive car.” There is no simpler description that fully covers all the
actions the application takes that is more specific than “Drive car.”
3.Image generation application that takes a verbal description and
generates a landscape image.A node such as “Generate landscape image”
would fully cover the scope of this activity, even if users iterate over multiple
prompts before achieving the desired output.
4.Cleaning robot that cleans floors, dusts furniture, and empties
trash cans.The most specific node covering all these actions might be
“Clean rooms.” If no such node exists in the ontology, the best available clas-
sification may be the more general node “Clean.” If no other node covers
all three activities (clean floors, dust furniture, and empty trash cans) while
being more specific than “Clean,” then “Clean” is the appropriate choice.
• NoteIn some cases, the above examples illustrate an application performing
an entire activity. In other cases, they illustrate an application helping a human
perform an activity. But in all cases, we try to choose the most specific activity
that fully covers the scope of what the application does.
• ProcedureFollow this process:
1.Identify the main activity .From the application tagline and descrip-
tion, determine the main activity the application performs or helps perform,
expressed as a “verb + object” phrase.
2.Search the ontology .Using the identified “verb + object” phrase, search or
browse the ontology to locate nodes that may be appropriate classifications.
3.Select the most appropriate node.Choose the node that best satisfies
the classification principle and aligns with the examples above.
E.2 Inter-annotator agreements details
Traditional inter-annotator agreement measures (like Cohen’sκ) treat all disagree-
ments equally; classifying an image generation application as “Write” versus “Create
image” counts the same as classifying it as “Write” versus “Clean floor”. But in a
hierarchical ontology, some disagreements are more severe than others. Wu-Palmer
similarity captures this by measuring how much of the path from the root two classifi-
cations share: siblings score higher than cousins, which score higher than activities in
entirely different branches. This measure is defined byS= 2N N1+N2 , whereSis the sim- ilarity between the two nodes,Nis the distance from the root node of the hierarchy to
the closest common ancestor of the two nodes, andN 1 andN 2 are the distances from
68

the root node to the two nodes being compared. In other words, it is the proportion
of links from the root node that the two nodes share.
We report (1) mean Wu-Palmer similarity over all pairs of ratings, and (2) weighted
Cohen’sκ, computed by incorporating Wu-Palmer similarity as the weighting function.
For human-human IAA, we calculated the mean pairwise Wu-Palmer similarity and
weighted Cohen’sκamong all human annotators. For human-AI IAA, we calculated
these metrics between each model and all human annotators. For AI-AI IAA, we
calculated the same pairwise measures across the three models.
We also invited three student interns from our research team to conduct the human
classification following the same procedure described in Section 6.5.1. These classifiers
can be regarded as “junior classifiers” who were entry-level on this annotation task and
less experienced than the seven authors, who are the core expert classifiers. Table E4
reports the human-AI, human-human, and AI-AI inter-annotator agreement results
for all three groups: junior annotators (interns), expert annotators, and all annotators
combined. Notably, there is a clear increase in both human-human and human-AI
agreement when comparing junior annotators with expert annotators. This suggests
that the ontology captures specialized organizational knowledge that requires domain
training to apply reliably.
T able E4:Inter-annotator agreement (IAA) across human annotation
groups,using Mean Wu-Palmer Similarity and Weighted Cohen’sκ(mean with
95% confidence intervals).
Mean Wu-Palmer Similarity Weighted Cohen’sκ
Interns Experts All Interns Experts All
Human-SPFO 0.591
[0.518,
0.666]
0.631
[0.561,
0.703]
0.619
[0.559,
0.680]
0.347
[0.233,
0.456]
0.411
[0.304,
0.509]
0.392
[0.296,
0.476]
Human-SPPO 0.583
[0.504,
0.660]
0.585
[0.511,
0.655]
0.584
[0.519,
0.645]
0.343
[0.225,
0.451]
0.349
[0.242,
0.444]
0.347
[0.254,
0.427]
Human-MPPO 0.554
[0.473,
0.635]
0.619
[0.543,
0.697]
0.600
[0.528,
0.670]
0.314
[0.195,
0.421]
0.412
[0.304,
0.514]
0.383
[0.282,
0.470]
Human-Human 0.525
[0.465,
0.586]
0.584
[0.525,
0.649]
0.557
[0.514,
0.609]
0.258
[0.161,
0.349]
0.348
[0.260,
0.433]
0.307
[0.234,
0.372]
AI-AI 0.812 [0.726, 0.895] 0.703 [0.566, 0.822]
E.3 Relation between human-AI classification similarity and
human evaluation of model classifications
We plot the distribution of human-AI annotation similarity for each manual rating cat-
egory. The pattern shown in Figure E1 reconfirms that manual evaluation labels align
69

with the hierarchy-aware similarity measure: perceived differences—whether favorable
or unfavorable—are associated with greater divergence in the ontology.
Fig. E1:Distribution of human-AI annotation similarity (mean W u-Palmer
similarity) across rating categories.When human evaluators rated the AI’s clas-
sification as equal to their own, the corresponding human-AI annotation pairs showed
higher similarity. In contrast, when the AI’s classification was rated as better or worse
than the human’s, annotation similarity was lower.
70

Appendix F Additional AI software application
results
F.1 Sample TAAFT data
T able F5:Sample AI application from the T AAFT dataset.
Name&facts
Linkhttps://www.andfacts.com/
TypeAI
Launch Date10-Jun-23
T askMarket analysis
T aglineAnalyze market signals for real-time consumer insights.
Description&facts is a market intelligence platform for consumer
brands that analyzes real-time market and product signals
to identify trends, opportunities, and risks. It supports
product development, marketing optimization, competitor
analysis, and international expansion by providing AI-
driven insights into consumer preferences and behavior
without the need for extensive manual research or consul-
tants.
Pricing ModelPaid-only
Starting Price$199
Billing F requencyOne-time
Number of Saves3
71

F.2 Sample TAAFT classification results
T able F6:Examples of AI applications and their classification results.
Name Launch Date T agline Description Classifi- cation
&AI 1-Jan-24
AI-
powered
patent
due dili-
gence in
seconds
&AI streamlines patent due diligence by rapidly generating
detailed claim charts, performing prior art searches, and ana-
lyzing claim robustness. The platform supports exporting
results to Word or Excel, semantic search across proprietary
and USPTO documents, and interactive querying through
a patent-aware chatbot. Its goal is to reduce the time and
cost associated with patent analysis while improving cover-
age and reliability.
Research
(Informa-
tion)
&facts 10-Jun-23
Analyze
market
signals for
real-time
consumer
insights.
&facts is a market intelligence platform for consumer brands
that analyzes real-time market and product signals to iden-
tify trends, opportunities, and risks. It supports product
development, marketing optimization, competitor analysis,
and international expansion by providing AI-driven insights
into consumer preferences and behavior without the need for
extensive manual research or consultants.
Analyze
Market
008 Agent 22-Nov- 23
AI-
powered
open-
source
softphone
revolu-
tionizing
VoIP.
008 Agent is an open-source, AI-powered softphone designed
for intelligent VoIP communication. It captures and pro-
cesses call events, transcribes conversations, performs sen-
timent analysis, and generates summaries. The system
integrates with CRM tools, supports programmable con-
versational agents, and provides transparent, customizable
workflows through a community-driven development model.
Commu-
nicate
(transfer
infor-
mation
end-to-
end)
04-x 1-Aug-23
Privacy-
first chat
with pow-
erful AI
models
04-x is a privacy-focused chat platform for interacting with
large language models. It supports multiple commercial and
open-source models, encrypts all user data end-to-end, and
allows tasks such as conversational interaction, summariza-
tion, and text generation. The system emphasizes data
ownership, security, and extensibility through continuous
model integration.
Converse
0gpt 9-Sep-24
Unmask
AI-
generated
text with
precision.
0gpt is an AI content detection tool that distinguishes
between human-written and AI-generated text using linguis-
tic and statistical analysis. It evaluates sentence structure,
vocabulary diversity, and contextual coherence, highlights
suspected AI-generated segments, supports multiple lan-
guages, and ensures privacy by not storing analyzed content.
The tool is free and designed for broad accessibility.
Classify
Content
72

F.3 Visualization of the complete ontology (aggregated
counts)
Fig. F2:Sunburst diagram of the complete ontology withaggregated counts
of AI software applications.Color intensities and percentage values represent the
proportion of AI applications classified directly in each activityand in all of its spe-
cializations, relative to the total number of AI applications in the dataset. Readers
are encouraged to zoom in to examine fine-grained specializations.
73

F.4 Visualization of the complete ontology (direct counts)
Fig. F3:Sunburst diagram of the complete ontology withdirect countsof
AI software applications.Color intensities and percentage values represent the
proportion of AI applications directly classifieddirectlyinto each activity, relative to
the total number of AI applications in the dataset. Readers are encouraged to zoom
in to examine fine-grained specializations.
74

F.5 Mapping atomic activities to associated O*NET tasks
T able F7:Selected atomic activities and associated O*NET tasks in the
“Create information – other” branch.
Atomic Activity O*NET T asks
Create content (3.53%)(O*NET) 16193 — Collaborate with Web, multimedia,
or art design staffs to create multimedia Web sites or
other internet content that conforms to brand and
company visual format.
(O*NET) 5219 — Plan and develop instructional
methods and content for educational, vocational, or
student activity programs.
Develop application
(1.79%)
(O*NET) 16184 — Develop transactional Web
applications using Web programming software and
programming languages such as HTML and XML.
(O*NET) 16786 — Develop new software applications
or customize existing applications to meet specific
scientific project needs.
(O*NET) 17706 — Develop or maintain applications
that process biologically based data into searchable
databases for analysis, calculation, or presentation.
(O*NET) 18093 — Develop, implement, or evaluate
health information technology applications, tools, or
processes to assist with data management.
(O*NET) 20193 — Develop software applications or
programming for statistical modeling and graphic
analysis.
(O*NET) 21734 — Develop specialized computer
software routines, internet-based GIS databases, or
business applications to customize geographic
information.
(O*NET) 3572 — Design, develop, and implement
computer applications for mining operations such as
mine design, modeling, mapping, or condition
monitoring.
(O*NET) 5351 — Plan or develop applications or
modifications for electronic properties used in
components, products, or systems to improve technical
performance.
Create recording (1.19%)(O*NET) 22277 — Create photographic recordings of
information using equipment.
(O*NET) 22572 — Produce recordings of music.
Generate lead (0.99%)(O*NET) 17654 — Generate solar energy customer
leads to develop new accounts.
Continued on next page
75

T able F7:Selected atomic activities and associated O*NET tasks in the
“Create Information – other” branch.(continued)
Atomic Activity O*NET T asks
Create site (0.81%)(O*NET) 16193 — Collaborate with Web, multimedia,
or art design staffs to create multimedia Web sites or
other internet content that conforms to brand and
company visual format.
(O*NET) 20058 — Develop and maintain course Web
sites.
(O*NET) 20288 — Develop or maintain internal or
external company Web sites.
(O*NET) 21049 — Develop Web sites.
(O*NET) 21109 — Develop and maintain Web sites for
online courses.
76

F.6 Distribution of AI applications (2016–2025)
Act: 100%
Act on information
(“Think”): 82%
Act with other activities and actors (“Interact”): 36% Act on physical objects (“Do”): 0%
Create
information: 64%
Modify
information: 0%
Transfer
information: 18%
Storeinformation: 0%
Transfer between
actors: 36%
Act onactivities: 0%
Modify physicalobjects: 0%
Create physicalobjects: 0%
Store physical
objects: 0%
Transfer physical
objects: 0%
Plan: 0%
Analyze: 9%
Decide: 9%Calculate: 0% Express information: 27% Assemble information: 0% Reason: 0% Create information -- other: 18% Solve: 0%
Transform information: 0% Com bine inform
ation: 0%
Separate information: 0% Move information: 0%Exchange information: 9%
Get information: 0%Provide information: 9% Communicate (transfer information end-to-end): 0% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 0%
Buy: 9%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 18%
Transfer service: 9%
Transfer physical objects: 0%
Interact: 0%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0%
Communicate (transfer information end-to-end): 0%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0% W ithhold: 0%
Perform
 (action): 0%
Improve: 0%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0% Pass (achieve): 0% Undertake: 0% Transform physical objects: 0%
Separate physical objects: 0%
Combine physical objects: 0%
Move physical objects: 0%
Assemble: 0%
Fabricate: 0%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 0%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0%
Outline: 0%
Plan -- other: 0%
Propose: 0%
Schedule: 0%
Stage: 0%
 Analyze -- other: 9%
Characterize: 0%
 Correlate: 0%
 Determine: 0%
 Experiment: 0%
 Investigate: 0%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0%
 Reject: 0%
 Rule: 0%
 Select: 9%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0%
 Count: 0%
 Estimate: 0%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0%
 Record: 27%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0%
 Reason -- other: 0%
 Create (Activity): 0%
 Create (Actor): 0%
Create (Information): 18%
 Address (solve): 0%
 Resolve: 0%
Solve -- other: 0%
Adjust (information): 0%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 0%
Organize (analytically): 0%
 Perm
ute: 0%
Prepare (inform
ation): 0%
Process (inform
ation): 0%
Renew (inform
ation): 0%
Revise: 0%
 Service (inform
ation): 0%
Switch: 0%
 Transform
 inform
ation -- other: 0%
Translate: 0%
 Use: 0%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0%
Gather (inform
ation): 0%
Incorporate (inform
ation): 0%
Pack (together) (information): 0%
 Synthesize (information): 0%
 Break (into components): 0%
 Cut (information): 0%
 Disconnect (information): 0%
 Remove (information): 0%
 Separate information -- other: 0%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 9%
 Correspond: 0%
 Debate: 0%
 Exchange information -- other: 0%
 Interview: 0%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0%
 Network: 0%
 Reach: 0%
 Teach: 0%
 Access: 0%
 Download: 0%
 Evaluate: 0%
 Gather (information): 0%
 Get information -- other: 0%
 Import: 0%
 Learn: 0%
 Perceive: 0%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0%
 Provide decision: 0%
 Provide money: 0%
 Send information: 9%
 Communicate (transfer information end-to-end) -- other: 0%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 0%
Ticket: 0%
Buy -- other: 0%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 9%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 0%
Exchange information: 9%
Get information: 0%
Provide information: 9%
End service: 0%
Exchange service: 0%
Get service: 9%
Provide service: 0%
Exchange physical objects: 0%
Get physical objects: 0%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 0%
 Conduct: 0%
 M
ake: 0%
Perform
 (action) -- other: 0%
Practice: 0%
 Rehearse: 0%
 Run (perform
): 0%
Im
prove -- other: 0%
Optim
ize: 0%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0%
Clean (physical): 0%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0%
 Process (physical): 0%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
 Cut (physical): 0%
 Disassemble: 0%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0%
 Consolidate: 0%
 Cover: 0%
Enclose: 0%
Gather (physical): 0%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0%
Reorient physical objects: 0%
Transport physical objects: 0%
 Assemble -- other: 0%
Configure (physical): 0%
Construct (physical): 0%
 Copy (physical): 0%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 0%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0%
Fig. F4: Distribution of AI applications in 2016.
77

Act: 100%
Act on information
(“Think”): 92%
Act with other activities and actors (“Interact”): 30% Act on physical objects (“Do”): 0%
Create
information: 57%
Modify
information: 16%
Transfer
information: 19%
Storeinformation: 0%
Transfer between
actors: 30%
Act onactivities: 3%
Modify physicalobjects: 0%
Create physicalobjects: 0%
Store physical
objects: 0%
Transfer physical
objects: 0%
Plan: 3%
Analyze: 8%
Decide: 5%Calculate: 0% Express information: 24% Assemble information: 0% Reason: 0% Create information -- other: 14% Solve: 3%
Transform information: 16% Com bine inform
ation: 0%
Separate information: 0% Move information: 0%Exchange information: 3%
Get information: 8%Provide information: 5% Communicate (transfer information end-to-end): 3% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 0%
Buy: 5%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 19%
Transfer service: 5%
Transfer physical objects: 0%
Interact: 0%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0%
Communicate (transfer information end-to-end): 3%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0% W ithhold: 0%
Perform
 (action): 0%
Improve: 3%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0% Pass (achieve): 0% Undertake: 0% Transform physical objects: 0%
Separate physical objects: 0%
Combine physical objects: 0%
Move physical objects: 0%
Assemble: 0%
Fabricate: 0%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 0%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0%
Outline: 0%
Plan -- other: 3%
Propose: 0%
Schedule: 0%
Stage: 0%
 Analyze -- other: 5%
Characterize: 0%
 Correlate: 0%
 Determine: 0%
 Experiment: 0%
 Investigate: 0%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0%
 Reject: 0%
 Rule: 0%
 Select: 5%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0%
 Count: 0%
 Estimate: 0%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0%
 Record: 24%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0%
 Reason -- other: 0%
 Create (Activity): 0%
 Create (Actor): 0%
Create (Information): 14%
 Address (solve): 0%
 Resolve: 0%
Solve -- other: 3%
Adjust (information): 5%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 3%
Organize (analytically): 0%
 Perm
ute: 0%
Prepare (inform
ation): 3%
Process (inform
ation): 0%
Renew (inform
ation): 0%
Revise: 3%
 Service (inform
ation): 0%
Switch: 0%
 Transform
 inform
ation -- other: 0%
Translate: 3%
 Use: 0%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0%
Gather (inform
ation): 0%
Incorporate (inform
ation): 0%
Pack (together) (information): 0%
 Synthesize (information): 0%
 Break (into components): 0%
 Cut (information): 0%
 Disconnect (information): 0%
 Remove (information): 0%
 Separate information -- other: 0%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 3%
 Correspond: 0%
 Debate: 0%
 Exchange information -- other: 0%
 Interview: 0%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0%
 Network: 0%
 Reach: 0%
 Teach: 0%
 Access: 0%
 Download: 0%
 Evaluate: 5%
 Gather (information): 0%
 Get information -- other: 0%
 Import: 0%
 Learn: 0%
 Perceive: 3%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0%
 Provide decision: 0%
 Provide money: 0%
 Send information: 5%
 Communicate (transfer information end-to-end) -- other: 0%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 0%
Ticket: 0%
Buy -- other: 0%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 5%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 3%
Exchange information: 3%
Get information: 8%
Provide information: 5%
End service: 0%
Exchange service: 0%
Get service: 5%
Provide service: 0%
Exchange physical objects: 0%
Get physical objects: 0%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 0%
 Conduct: 0%
 M
ake: 0%
Perform
 (action) -- other: 0%
Practice: 0%
 Rehearse: 0%
 Run (perform
): 0%
Im
prove -- other: 3%
Optim
ize: 0%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0%
Clean (physical): 0%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0%
 Process (physical): 0%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
 Cut (physical): 0%
 Disassemble: 0%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0%
 Consolidate: 0%
 Cover: 0%
Enclose: 0%
Gather (physical): 0%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0%
Reorient physical objects: 0%
Transport physical objects: 0%
 Assemble -- other: 0%
Configure (physical): 0%
Construct (physical): 0%
 Copy (physical): 0%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 0%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0%
Fig. F5: Distribution of AI applications in 2017.
78

Act: 100%
Act on information
(“Think”): 88%
Act with other activities and actors (“Interact”): 36% Act on physical objects (“Do”): 0%
Create
information: 52%
Modify
information: 14%
Transfer
information: 22%
Storeinformation: 0%
Transfer between
actors: 35%
Act onactivities: 6%
Modify physicalobjects: 0%
Create physicalobjects: 0%
Store physical
objects: 0%
Transfer physical
objects: 0%
Plan: 4%
Analyze: 12%Decide: 3%Calculate: 0% Express information: 20% Assemble information: 0% Reason: 0% Create information -- other: 12% Solve: 1%
Transform information: 14% Com bine inform
ation: 0%
Separate information: 0% Move information: 0%Exchange information: 1%
Get information: 10%Provide information: 4% Communicate (transfer information end-to-end): 6% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 1%
Buy: 3%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 22%
Transfer service: 9%
Transfer physical objects: 0%
Interact: 0%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0%
Communicate (transfer information end-to-end): 6%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0% W ithhold: 0%
Perform
 (action): 1%
Improve: 3%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 1% Pass (achieve): 0% Undertake: 0% Transform physical objects: 0%
Separate physical objects: 0%
Combine physical objects: 0%
Move physical objects: 0%
Assemble: 0%
Fabricate: 0%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 0%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0%
Outline: 0%
Plan -- other: 4%
Propose: 0%
Schedule: 0%
Stage: 0%
 Analyze -- other: 9%
Characterize: 0%
 Correlate: 0%
 Determine: 1%
 Experiment: 0%
 Investigate: 0%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0%
 Reject: 0%
 Rule: 0%
 Select: 3%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0%
 Count: 0%
 Estimate: 0%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0%
 Record: 20%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0%
 Reason -- other: 0%
 Create (Activity): 0%
 Create (Actor): 0%
Create (Information): 12%
 Address (solve): 0%
 Resolve: 0%
Solve -- other: 1%
Adjust (information): 4%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 3%
Organize (analytically): 0%
 Perm
ute: 0%
Prepare (inform
ation): 1%
Process (inform
ation): 3%
Renew (inform
ation): 0%
Revise: 1%
 Service (inform
ation): 0%
Switch: 0%
 Transform
 inform
ation -- other: 0%
Translate: 1%
 Use: 0%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0%
Gather (inform
ation): 0%
Incorporate (inform
ation): 0%
Pack (together) (information): 0%
 Synthesize (information): 0%
 Break (into components): 0%
 Cut (information): 0%
 Disconnect (information): 0%
 Remove (information): 0%
 Separate information -- other: 0%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 1%
 Correspond: 0%
 Debate: 0%
 Exchange information -- other: 0%
 Interview: 0%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0%
 Network: 0%
 Reach: 0%
 Teach: 0%
 Access: 0%
 Download: 0%
 Evaluate: 4%
 Gather (information): 0%
 Get information -- other: 0%
 Import: 0%
 Learn: 0%
 Perceive: 6%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0%
 Provide decision: 0%
 Provide money: 0%
 Send information: 4%
 Communicate (transfer information end-to-end) -- other: 0%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 1%
Ticket: 0%
Buy -- other: 0%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 3%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 6%
Exchange information: 1%
Get information: 10%
Provide information: 4%
End service: 0%
Exchange service: 0%
Get service: 7%
Provide service: 1%
Exchange physical objects: 0%
Get physical objects: 0%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 1%
 Conduct: 0%
 M
ake: 0%
Perform
 (action) -- other: 0%
Practice: 0%
 Rehearse: 0%
 Run (perform
): 0%
Im
prove -- other: 3%
Optim
ize: 0%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 1%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0%
Clean (physical): 0%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0%
 Process (physical): 0%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
 Cut (physical): 0%
 Disassemble: 0%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0%
 Consolidate: 0%
 Cover: 0%
Enclose: 0%
Gather (physical): 0%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0%
Reorient physical objects: 0%
Transport physical objects: 0%
 Assemble -- other: 0%
Configure (physical): 0%
Construct (physical): 0%
 Copy (physical): 0%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 0%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0%
Fig. F6: Distribution of AI applications in 2018.
79

Act: 100%
Act on information
(“Think”): 87%
Act with other activities and actors (“Interact”): 36% Act on physical objects (“Do”): 0%
Create
information: 51%
Modify
information: 17%
Transfer
information: 20%
Storeinformation: 0%
Transfer between
actors: 33%
Act onactivities: 7%
Modify physicalobjects: 0%
Create physicalobjects: 0%
Store physical
objects: 0%
Transfer physical
objects: 0%
Plan: 3%
Analyze: 9%
Decide: 4%Calculate: 0% Express information: 21% Assemble information: 0% Reason: 0% Create information -- other: 13% Solve: 2%
Transform information: 14% Com bine inform
ation: 0%
Separate information: 2% Move information: 0%Exchange information: 2%
Get information: 9%Provide information: 5% Communicate (transfer information end-to-end): 4% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 0.8%
Buy: 3%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 20%
Transfer service: 9%
Transfer physical objects: 0%
Interact: 0%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0%
Communicate (transfer information end-to-end): 4%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0% W ithhold: 0%
Perform
 (action): 3%
Improve: 3%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0.8% Pass (achieve): 0% Undertake: 0% Transform physical objects: 0%
Separate physical objects: 0%
Combine physical objects: 0%
Move physical objects: 0%
Assemble: 0%
Fabricate: 0%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 0%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0.8%
Outline: 0%
Plan -- other: 2%
Propose: 0%
Schedule: 0%
Stage: 0%
 Analyze -- other: 5%
Characterize: 0%
 Correlate: 0%
 Determine: 0.8%
 Experiment: 0%
 Investigate: 2%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0%
 Reject: 0%
 Rule: 0%
 Select: 4%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0%
 Count: 0%
 Estimate: 0%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0%
 Record: 21%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0%
 Reason -- other: 0%
 Create (Activity): 0%
 Create (Actor): 0%
Create (Information): 13%
 Address (solve): 0%
 Resolve: 0%
Solve -- other: 2%
Adjust (information): 3%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 3%
Organize (analytically): 0%
 Perm
ute: 0%
Prepare (inform
ation): 2%
Process (inform
ation): 2%
Renew (inform
ation): 0%
Revise: 2%
 Service (inform
ation): 0%
Switch: 0%
 Transform
 inform
ation -- other: 0%
Translate: 0.8%
 Use: 0.8%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0%
Gather (inform
ation): 0%
Incorporate (inform
ation): 0%
Pack (together) (information): 0%
 Synthesize (information): 0%
 Break (into components): 0%
 Cut (information): 0.8%
 Disconnect (information): 0%
 Remove (information): 0%
 Separate information -- other: 2%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 0.8%
 Correspond: 0%
 Debate: 0%
 Exchange information -- other: 0%
 Interview: 0%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0%
 Network: 0%
 Reach: 0%
 Teach: 2%
 Access: 0%
 Download: 0%
 Evaluate: 3%
 Gather (information): 0%
 Get information -- other: 0%
 Import: 0%
 Learn: 2%
 Perceive: 4%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0%
 Provide decision: 0%
 Provide money: 0%
 Send information: 5%
 Communicate (transfer information end-to-end) -- other: 0%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 0.8%
Ticket: 0%
Buy -- other: 0.8%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 2%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 4%
Exchange information: 2%
Get information: 9%
Provide information: 5%
End service: 0%
Exchange service: 0%
Get service: 6%
Provide service: 2%
Exchange physical objects: 0%
Get physical objects: 0%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 3%
 Conduct: 0%
 M
ake: 0%
Perform
 (action) -- other: 0%
Practice: 0%
 Rehearse: 0%
 Run (perform
): 0%
Im
prove -- other: 3%
Optim
ize: 0%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0.8%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0%
Clean (physical): 0%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0%
 Process (physical): 0%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
 Cut (physical): 0%
 Disassemble: 0%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0%
 Consolidate: 0%
 Cover: 0%
Enclose: 0%
Gather (physical): 0%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0%
Reorient physical objects: 0%
Transport physical objects: 0%
 Assemble -- other: 0%
Configure (physical): 0%
Construct (physical): 0%
 Copy (physical): 0%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 0%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0%
Fig. F7: Distribution of AI applications in 2019.
80

Act: 100%
Act on information
(“Think”): 88%
Act with other activities and actors (“Interact”): 35% Act on physical objects (“Do”): 0%
Create
information: 51%
Modify
information: 18%
Transfer
information: 20%
Storeinformation: 0%
Transfer between
actors: 33%
Act onactivities: 6%
Modify physicalobjects: 0%
Create physicalobjects: 0%
Store physical
objects: 0%
Transfer physical
objects: 0%
Plan: 3%
Analyze: 11%Decide: 3% Calculate: 0.3% Express information: 18% Assemble information: 0.6% Reason: 0% Create information -- other: 15% Solve: 0.6%
Transform information: 15% Com bine inform
ation: 1%
Separate information: 2% Move information: 0%Exchange information: 1%
Get information: 10%Provide information: 4% Communicate (transfer information end-to-end): 5% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 1.0%
Buy: 2%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 20%
Transfer service: 10%
Transfer physical objects: 0%
Interact: 0%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0%
Communicate (transfer information end-to-end): 5%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0% W ithhold: 0%
Perform
 (action): 2%
Improve: 3%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0.6% Pass (achieve): 0% Undertake: 0% Transform physical objects: 0%
Separate physical objects: 0%
Combine physical objects: 0%
Move physical objects: 0%
Assemble: 0%
Fabricate: 0%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 0%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0.6%
Outline: 0%
Plan -- other: 2%
Propose: 0%
Schedule: 0%
Stage: 0%
 Analyze -- other: 5%
Characterize: 0%
 Correlate: 0%
 Determine: 1%
 Experiment: 0%
 Investigate: 1%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0%
 Reject: 0%
 Rule: 0%
 Select: 3%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0.3%
Count: 0%
 Estimate: 0%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0%
 Record: 18%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0.6%
Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0%
 Reason -- other: 0%
 Create (Activity): 0%
 Create (Actor): 0%
Create (Information): 15%
 Address (solve): 0%
 Resolve: 0%
Solve -- other: 0.6%
Adjust (information): 2%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 3%
Organize (analytically): 0%
 Perm
ute: 0%
Prepare (inform
ation): 0.6%
Process (inform
ation): 2%
Renew (inform
ation): 0%
Revise: 5%
 Service (inform
ation): 0%
Switch: 0%
 Transform
 inform
ation -- other: 0.3%
Translate: 1.0%
 Use: 0.3%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0.3%
Gather (inform
ation): 1.0%
Incorporate (inform
ation): 0%
Pack (together) (information): 0%
 Synthesize (information): 0%
 Break (into components): 0%
 Cut (information): 0.6%
 Disconnect (information): 0%
 Remove (information): 0%
 Separate information -- other: 2%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 0.3%
 Correspond: 0%
 Debate: 0%
 Exchange information -- other: 0%
 Interview: 0%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0%
 Network: 0%
 Reach: 0%
 Teach: 1.0%
 Access: 0%
 Download: 0%
 Evaluate: 3%
 Gather (information): 1.0%
 Get information -- other: 0%
 Import: 0%
 Learn: 0.6%
 Perceive: 5%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0%
 Provide decision: 0%
 Provide money: 0%
 Send information: 4%
 Communicate (transfer information end-to-end) -- other: 1%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 1.0%
Ticket: 0%
Buy -- other: 0.3%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 2%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 5%
Exchange information: 1%
Get information: 10%
Provide information: 4%
End service: 0%
Exchange service: 0%
Get service: 8%
Provide service: 2%
Exchange physical objects: 0%
Get physical objects: 0%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 1%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 2%
 Conduct: 0%
 M
ake: 0%
Perform
 (action) -- other: 0%
Practice: 0%
 Rehearse: 0.3%
 Run (perform
): 0%
Im
prove -- other: 3%
Optim
ize: 0%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0.6%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0%
Clean (physical): 0%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0%
 Process (physical): 0%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
 Cut (physical): 0%
 Disassemble: 0%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0%
 Consolidate: 0%
 Cover: 0%
Enclose: 0%
Gather (physical): 0%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0%
Reorient physical objects: 0%
Transport physical objects: 0%
 Assemble -- other: 0%
Configure (physical): 0%
Construct (physical): 0%
 Copy (physical): 0%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 0%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0%
Fig. F8: Distribution of AI applications in 2020.
81

Act: 100%
Act on information
(“Think”): 91%
Act with other activities and actors (“Interact”): 33% Act on physical objects (“Do”): 0%
Create
information: 53%
Modify
information: 21%
Transfer
information: 18%
Storeinformation: 0%
Transfer between
actors: 32%
Act onactivities: 8%
Modify physicalobjects: 0%
Create physicalobjects: 0%
Store physical
objects: 0%
Transfer physical
objects: 0%
Plan: 3%
Analyze: 10%Decide: 3% Calculate: 0.5% Express information: 19% Assemble information: 0.6% Reason: 0% Create information -- other: 16% Solve: 0.6%
Transform information: 17% Com bine inform
ation: 1%
Separate information: 2% Move information: 0%Exchange information: 2%
Get information: 7%Provide information: 5% Communicate (transfer information end-to-end): 3% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 0.6%
Buy: 1%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 18%
Transfer service: 12%
Transfer physical objects: 0%
Interact: 0%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0%
Communicate (transfer information end-to-end): 3%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0% W ithhold: 0%
Perform
 (action): 2%
Improve: 6%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0.3% Pass (achieve): 0% Undertake: 0% Transform physical objects: 0%
Separate physical objects: 0%
Combine physical objects: 0%
Move physical objects: 0%
Assemble: 0%
Fabricate: 0%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 0%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0.6%
Outline: 0%
Plan -- other: 2%
Propose: 0.3%
 Schedule: 0.5%
Stage: 0%
 Analyze -- other: 5%
Characterize: 0%
 Correlate: 0%
 Determine: 1%
 Experiment: 0%
 Investigate: 1.0%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0.2%
 Reject: 0%
 Rule: 0%
 Select: 3%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0.3%
Count: 0%
 Estimate: 0.2%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0.2%
 Record: 19%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0.6%
Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0%
 Reason -- other: 0%
 Create (Activity): 0.3%
 Create (Actor): 0%
Create (Information): 16%
 Address (solve): 0%
 Resolve: 0%
Solve -- other: 0.6%
Adjust (information): 2%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 6%
Organize (analytically): 0%
 Perm
ute: 0%
Prepare (inform
ation): 0.5%
Process (inform
ation): 3%
Renew (inform
ation): 0%
Revise: 5%
 Service (inform
ation): 0%
Switch: 0%
 Transform
 inform
ation -- other: 0.3%
Translate: 1%
 Use: 0.2%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0.2%
Gather (inform
ation): 0.8%
Incorporate (inform
ation): 0.2%
Pack (together) (information): 0%
 Synthesize (information): 0.2%
 Break (into components): 0%
 Cut (information): 0.5%
 Disconnect (information): 0%
 Remove (information): 0%
 Separate information -- other: 2%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 0.3%
 Correspond: 0%
 Debate: 0%
 Exchange information -- other: 0%
 Interview: 0%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0.2%
 Network: 0%
 Reach: 0%
 Teach: 2%
 Access: 0%
 Download: 0%
 Evaluate: 2%
 Gather (information): 0.8%
 Get information -- other: 0%
 Import: 0%
 Learn: 0.3%
 Perceive: 4%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0.2%
 Provide decision: 0%
 Provide money: 0%
 Send information: 5%
 Communicate (transfer information end-to-end) -- other: 0.8%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 0.6%
Ticket: 0%
Buy -- other: 0.2%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 1.0%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 3%
Exchange information: 2%
Get information: 7%
Provide information: 5%
End service: 0%
Exchange service: 0%
Get service: 10%
Provide service: 2%
Exchange physical objects: 0%
Get physical objects: 0%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0.8%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 1%
 Conduct: 0.2%
 M
ake: 0%
Perform
 (action) -- other: 0%
Practice: 0%
 Rehearse: 0.3%
 Run (perform
): 0%
Im
prove -- other: 3%
Optim
ize: 2%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0.3%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0%
Clean (physical): 0%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0%
 Process (physical): 0%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
 Cut (physical): 0%
 Disassemble: 0%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0%
 Consolidate: 0%
 Cover: 0%
Enclose: 0%
Gather (physical): 0%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0%
Reorient physical objects: 0%
Transport physical objects: 0%
 Assemble -- other: 0%
Configure (physical): 0%
Construct (physical): 0%
 Copy (physical): 0%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 0%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0%
Fig. F9: Distribution of AI applications in 2021.
82

Act: 100%
Act on information
(“Think”): 93%
Act with other activities and actors (“Interact”): 27% Act on physical objects (“Do”): 0%
Create
information: 59%
Modify
information: 18%
Transfer
information: 17%
Storeinformation: 0%
Transfer between
actors: 26%
Act onactivities: 5%
Modify physicalobjects: 0%
Create physicalobjects: 0%
Store physical
objects: 0%
Transfer physical
objects: 0%
Plan: 3%
Analyze: 9%
Decide: 2% Calculate: 0.3% Express information: 28% Assemble information: 0.7% Reason: 0.6% Create information -- other: 16% Solve: 0.5%
Transform information: 15% Com bine inform
ation: 0.6%
Separate information: 2% Move information: 0%Exchange information: 3%
Get information: 6%Provide information: 5% Communicate (transfer information end-to-end): 2% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 0.3%
Buy: 0.7%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 17%
Transfer service: 8%
Transfer physical objects: 0%
Interact: 0%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0.06%
Communicate (transfer information end-to-end): 2%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0.06% W ithhold: 0%
Perform
 (action): 2%
Improve: 3%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0.2% Pass (achieve): 0% Undertake: 0% Transform physical objects: 0%
Separate physical objects: 0%
Combine physical objects: 0%
Move physical objects: 0%
Assemble: 0%
Fabricate: 0%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 0%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0.9%
Outline: 0%
Plan -- other: 1%
Propose: 0.2%
 Schedule: 0.3%
Stage: 0%
 Analyze -- other: 5%
Characterize: 0%
 Correlate: 0%
 Determine: 1%
 Experiment: 0%
 Investigate: 1%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0.1%
 Reject: 0%
 Rule: 0%
 Select: 2%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0.2%
Count: 0%
 Estimate: 0.1%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0.2%
 Record: 27%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0.7%
Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0.6%
 Reason -- other: 0%
 Create (Activity): 0.5%
 Create (Actor): 0%
Create (Information): 16%
 Address (solve): 0%
 Resolve: 0.1%
Solve -- other: 0.3%
Adjust (information): 1%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 3%
Organize (analytically): 0.6%
 Perm
ute: 0%
Prepare (inform
ation): 0.3%
Process (inform
ation): 2%
Renew (inform
ation): 0%
Revise: 6%
 Service (inform
ation): 0.2%
Switch: 0%
 Transform
 inform
ation -- other: 0.3%
Translate: 1%
 Use: 0.1%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0.06%
Gather (inform
ation): 0.4%
Incorporate (inform
ation): 0.06%
Pack (together) (information): 0%
 Synthesize (information): 0.1%
 Break (into components): 0%
 Cut (information): 1%
 Disconnect (information): 0%
 Remove (information): 0.06%
Separate information -- other: 0.7%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 0.5%
 Correspond: 0%
 Debate: 0.06%
 Exchange information -- other: 0.06%
 Interview: 0.06%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0.06%
 Network: 0%
 Reach: 0.06%
 Teach: 2%
 Access: 0.06%
 Download: 0%
 Evaluate: 2%
 Gather (information): 0.4%
 Get information -- other: 0.06%
 Import: 0%
 Learn: 0.6%
 Perceive: 3%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0.2%
 Provide decision: 0%
 Provide money: 0%
 Send information: 5%
 Communicate (transfer information end-to-end) -- other: 0.5%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 0.3%
Ticket: 0%
Buy -- other: 0.1%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0.6%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 2%
Exchange information: 3%
Get information: 6%
Provide information: 5%
End service: 0%
Exchange service: 0%
Get service: 7%
Provide service: 1%
Exchange physical objects: 0%
Get physical objects: 0%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0.5%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0.06%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 1%
 Conduct: 0.2%
 M
ake: 0%
Perform
 (action) -- other: 0.1%
Practice: 0%
 Rehearse: 0.2%
 Run (perform
): 0%
Im
prove -- other: 2%
Optim
ize: 1%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0.2%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0%
Clean (physical): 0%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0%
 Process (physical): 0%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
 Cut (physical): 0%
 Disassemble: 0%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0%
 Consolidate: 0%
 Cover: 0%
Enclose: 0%
Gather (physical): 0%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0%
Reorient physical objects: 0%
Transport physical objects: 0%
 Assemble -- other: 0%
Configure (physical): 0%
Construct (physical): 0%
 Copy (physical): 0%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 0%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0%
Fig. F10: Distribution of AI applications in 2022.
83

Act: 100%
Act on information
(“Think”): 92%
Act with other activities and actors (“Interact”): 30% Act on physical objects (“Do”): 0%
Create
information: 59%
Modify
information: 14%
Transfer
information: 21%
Storeinformation: 0.03%
Transfer between
actors: 29%
Act onactivities: 4%
Modify physicalobjects: 0%
Create physicalobjects: 0%
Store physical
objects: 0%
Transfer physical
objects: 0%
Plan: 4%
Analyze: 7%
Decide: 2% Calculate: 0.3% Express information: 25% Assemble information: 1% Reason: 0.7% Create information -- other: 18% Solve: 0.3%
Transform information: 13% Com bine inform
ation: 0.7%
Separate information: 1% Move information: 0.04%Exchange information: 4%
Get information: 6%Provide information: 8% Communicate (transfer information end-to-end): 2% Store information -- other: 0.03% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 0.5%
Buy: 0.4%
Distribute: 0.01%
Sell: 0.1%
Give: 0.03%
Take: 0%
Transfer information: 21%
Transfer service: 7%
Transfer physical objects: 0%
Interact: 0%
Open (make available): 0%
Receive: 0.01% Return: 0%
Trade (Transfer both ways): 0.01%
Communicate (transfer information end-to-end): 2%
Earn: 0% Lend: 0% Pass (over): 0.03% Raise (funds): 0.03% W ithhold: 0%
Perform
 (action): 2%
Improve: 2%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0.1% Pass (achieve): 0% Undertake: 0% Transform physical objects: 0%
Separate physical objects: 0%
Combine physical objects: 0%
Move physical objects: 0%
Assemble: 0%
Fabricate: 0%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 0%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 1%
Outline: 0%
Plan -- other: 2%
Propose: 0.4%
 Schedule: 0.3%
Stage: 0%
 Analyze -- other: 4%
Characterize: 0%
 Correlate: 0%
 Determine: 0.8%
 Experiment: 0%
 Investigate: 1.0%
 Trace (analytically): 0%
 Accept: 0%
Decide -- other: 0.01%
 Estimate: 0.09%
 Reject: 0%
 Rule: 0.03%
 Select: 2%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0.1%
Count: 0.03%
 Estimate: 0.09%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0.3%
 Record: 24%
Assemble information -- other: 0.03%
Configure (information): 0.09%
 Construct (information): 1%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0.03%
Organize (analytically): 0.6%
 Reason -- other: 0.05%
 Create (Activity): 0.7%
 Create (Actor): 0%
Create (Information): 17%
 Address (solve): 0%
 Resolve: 0.1%
Solve -- other: 0.2%
Adjust (information): 0.9%
 Change Appearance: 0%
 Clean (inform
ation): 0.04%
 Decode: 0%
Encode: 0.01%
 Equalize: 0%
Fill (inform
ation): 0.04%
Finish (inform
ation): 0%
Im
prove: 2%
Organize (analytically): 0.6%
 Perm
ute: 0%
Prepare (inform
ation): 0.3%
Process (inform
ation): 1%
Renew (inform
ation): 0%
Revise: 5%
 Service (inform
ation): 0.4%
Switch: 0%
 Transform
 inform
ation -- other: 0.4%
Translate: 1%
 Use: 0.3%
 Add (inform
ation): 0.03%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0.05%
Gather (inform
ation): 0.4%
Incorporate (inform
ation): 0.1%
Pack (together) (information): 0%
 Synthesize (information): 0.05%
 Break (into components): 0%
 Cut (information): 0.7%
 Disconnect (information): 0%
 Remove (information): 0.03%
Separate information -- other: 0.3%
 Move information -- other: 0%
 Put information: 0.04%
Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0.01%
 Converse: 1%
 Correspond: 0.01%
 Debate: 0.04%
 Exchange information -- other: 0.05%
 Interview: 0.08%
 Mediate: 0%
 Meet: 0.03%
 Negotiate: 0.01%
 Network: 0%
 Reach: 0.01%
 Teach: 3%
 Access: 0.2%
 Download: 0%
 Evaluate: 2%
 Gather (information): 0.4%
 Get information -- other: 0.07%
 Import: 0%
 Learn: 0.8%
 Perceive: 3%
 Understand: 0.09%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0.3%
 Provide decision: 0%
 Provide money: 0%
 Send information: 8%
 Communicate (transfer information end-to-end) -- other: 0.4%
 Store (Activity): 0%
 Store (Actor): 0.01%
Store (Information): 0.01%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 0.5%
Ticket: 0%
Buy -- other: 0.04%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0.3%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0.01%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0.09%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0.03%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 2%
Exchange information: 4%
Get information: 6%
Provide information: 8%
End service: 0%
Exchange service: 0.1%
Get service: 5%
Provide service: 2%
Exchange physical objects: 0%
Get physical objects: 0%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0.01%
Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0.4%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0.03%
 Raise (funds) -- other: 0.03%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 1%
 Conduct: 0.3%
 M
ake: 0%
Perform
 (action) -- other: 0.08%
Practice: 0%
 Rehearse: 0.2%
 Run (perform
): 0%
Im
prove -- other: 1%
Optim
ize: 0.9%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0.1%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0%
Clean (physical): 0%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0%
 Process (physical): 0%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
 Cut (physical): 0%
 Disassemble: 0%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0%
 Consolidate: 0%
 Cover: 0%
Enclose: 0%
Gather (physical): 0%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0%
Reorient physical objects: 0%
Transport physical objects: 0%
 Assemble -- other: 0%
Configure (physical): 0%
Construct (physical): 0%
 Copy (physical): 0%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 0%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0%
Fig. F11: Distribution of AI applications in 2023.
84

Act: 100%
Act on information
(“Think”): 92%
Act with other activities and actors (“Interact”): 32% Act on physical objects (“Do”): 0%
Create
information: 58%
Modify
information: 14%
Transfer
information: 22%
Storeinformation: 0.06%
Transfer between
actors: 30%
Act onactivities: 4%
Modify physicalobjects: 0%
Create physicalobjects: 0%
Store physical
objects: 0%
Transfer physical
objects: 0%
Plan: 4%
Analyze: 7%
Decide: 2% Calculate: 0.2% Express information: 24% Assemble information: 1% Reason: 0.7% Create information -- other: 18% Solve: 0.4%
Transform information: 13% Com bine inform
ation: 0.7%
Separate information: 0.9% Move information: 0.03%Exchange information: 5%
Get information: 7%Provide information: 9% Communicate (transfer information end-to-end): 2% Store information -- other: 0.06% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 0.5%
Buy: 0.4%
Distribute: 0.008%
Sell: 0.1%
Give: 0.02%
Take: 0%
Transfer information: 22%
Transfer service: 7%
Transfer physical objects: 0%
Interact: 0%
Open (make available): 0%
Receive: 0.008%
Return: 0%
Trade (Transfer both ways): 0.008%
Communicate (transfer information end-to-end): 2%
Earn: 0% Lend: 0% Pass (over): 0.05% Raise (funds): 0.03% W ithhold: 0%
Perform
 (action): 2%
Improve: 2%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0.1% Pass (achieve): 0% Undertake: 0% Transform physical objects: 0%
Separate physical objects: 0%
Combine physical objects: 0%
Move physical objects: 0%
Assemble: 0%
Fabricate: 0%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 0%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 1%
Outline: 0%
Plan -- other: 2%
Propose: 0.4%
 Schedule: 0.3%
Stage: 0%
 Analyze -- other: 4%
Characterize: 0%
 Correlate: 0%
 Determine: 0.8%
 Experiment: 0%
 Investigate: 1%
 Trace (analytically): 0%
 Accept: 0%
Decide -- other: 0.008%
 Estimate: 0.09%
 Reject: 0%
 Rule: 0.02%
 Select: 2%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0.1%
Count: 0.02%
 Estimate: 0.09%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0.3%
 Record: 24%
Assemble information -- other: 0.03%
Configure (information): 0.07%
 Construct (information): 1%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0.02%
Organize (analytically): 0.7%
 Reason -- other: 0.05%
 Create (Activity): 0.7%
 Create (Actor): 0%
Create (Information): 17%
 Address (solve): 0%
 Resolve: 0.08%
Solve -- other: 0.3%
Adjust (information): 1%
 Change Appearance: 0%
 Clean (inform
ation): 0.03%
 Decode: 0%
Encode: 0.008%
 Equalize: 0%
Fill (inform
ation): 0.1%
Finish (inform
ation): 0%
Im
prove: 2%
Organize (analytically): 0.7%
 Perm
ute: 0%
Prepare (inform
ation): 0.3%
Process (inform
ation): 1%
Renew (inform
ation): 0%
Revise: 5%
 Service (inform
ation): 0.4%
Switch: 0%
 Transform
 inform
ation -- other: 0.3%
Translate: 1%
 Use: 0.4%
 Add (inform
ation): 0.02%
Com
bine inform
ation -- other: 0.008%
Connect (inform
ation): 0.06%
Gather (inform
ation): 0.4%
Incorporate (inform
ation): 0.2%
Pack (together) (information): 0%
 Synthesize (information): 0.04%
 Break (into components): 0%
 Cut (information): 0.7%
 Disconnect (information): 0%
 Remove (information): 0.02%
Separate information -- other: 0.2%
 Move information -- other: 0%
 Put information: 0.03%
Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0.008%
 Converse: 1%
 Correspond: 0.008%
 Debate: 0.04%
 Exchange information -- other: 0.05%
 Interview: 0.2%
 Mediate: 0%
 Meet: 0.02%
 Negotiate: 0.02%
 Network: 0.02%
 Reach: 0.02%
 Teach: 3%
 Access: 0.2%
 Download: 0.008%
 Evaluate: 2%
 Gather (information): 0.4%
 Get information -- other: 0.07%
 Import: 0.008%
 Learn: 0.9%
 Perceive: 3%
 Understand: 0.09%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0.3%
 Provide decision: 0%
 Provide money: 0%
 Send information: 8%
 Communicate (transfer information end-to-end) -- other: 0.3%
 Store (Activity): 0%
 Store (Actor): 0.05%
Store (Information): 0.008%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 0.5%
Ticket: 0%
Buy -- other: 0.05%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0.3%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0.008%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0.09%
Sell Service: 0.008%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0.02%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 2%
Exchange information: 5%
Get information: 7%
Provide information: 9%
End service: 0%
Exchange service: 0.1%
Get service: 5%
Provide service: 2%
Exchange physical objects: 0%
Get physical objects: 0%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0.008%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0.3%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0.05%
 Raise (funds) -- other: 0.03%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 1%
 Conduct: 0.3%
 M
ake: 0%
Perform
 (action) -- other: 0.07%
Practice: 0.008%
 Rehearse: 0.2%
 Run (perform
): 0%
Im
prove -- other: 1.0%
Optim
ize: 0.8%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0.09%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0%
Clean (physical): 0%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0%
 Process (physical): 0%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
 Cut (physical): 0%
 Disassemble: 0%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0%
 Consolidate: 0%
 Cover: 0%
Enclose: 0%
Gather (physical): 0%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0%
Reorient physical objects: 0%
Transport physical objects: 0%
 Assemble -- other: 0%
Configure (physical): 0%
Construct (physical): 0%
 Copy (physical): 0%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 0%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0%
Fig. F12: Distribution of AI applications in 2024.
85

Act: 100%
Act on information
(“Think”): 92%
Act with other activities and actors (“Interact”): 32% Act on physical objects (“Do”): 0%
Create
information: 58%
Modify
information: 14%
Transfer
information: 22%
Storeinformation: 0.05%
Transfer between
actors: 30%
Act onactivities: 4%
Modify physicalobjects: 0%
Create physicalobjects: 0%
Store physical
objects: 0%
Transfer physical
objects: 0%
Plan: 4%
Analyze: 7%
Decide: 2% Calculate: 0.2% Express information: 24% Assemble information: 1% Reason: 0.8% Create information -- other: 18% Solve: 0.4%
Transform information: 13% Com bine inform
ation: 0.7%
Separate information: 0.9% Move information: 0.05%Exchange information: 5%
Get information: 7%Provide information: 8% Communicate (transfer information end-to-end): 2% Store information -- other: 0.05% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 0.5%
Buy: 0.4%
Distribute: 0.008%
Sell: 0.1%
Give: 0.02%
Take: 0%
Transfer information: 22%
Transfer service: 7%
Transfer physical objects: 0%
Interact: 0%
Open (make available): 0%
Receive: 0.008%
Return: 0%
Trade (Transfer both ways): 0.008%
Communicate (transfer information end-to-end): 2%
Earn: 0% Lend: 0% Pass (over): 0.06% Raise (funds): 0.03% W ithhold: 0%
Perform
 (action): 2%
Improve: 2%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0.1% Pass (achieve): 0% Undertake: 0% Transform physical objects: 0%
Separate physical objects: 0%
Combine physical objects: 0%
Move physical objects: 0%
Assemble: 0%
Fabricate: 0%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 0%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 1%
Outline: 0%
Plan -- other: 2%
Propose: 0.4%
 Schedule: 0.3%
Stage: 0%
 Analyze -- other: 4%
Characterize: 0%
 Correlate: 0%
 Determine: 0.9%
 Experiment: 0%
 Investigate: 1%
 Trace (analytically): 0%
 Accept: 0%
Decide -- other: 0.008%
 Estimate: 0.08%
 Reject: 0%
 Rule: 0.02%
 Select: 2%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0.1%
Count: 0.02%
 Estimate: 0.08%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0.3%
 Record: 24%
Assemble information -- other: 0.03%
Configure (information): 0.08%
 Construct (information): 1%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0.02%
Organize (analytically): 0.7%
 Reason -- other: 0.05%
 Create (Activity): 0.8%
 Create (Actor): 0%
Create (Information): 17%
 Address (solve): 0%
 Resolve: 0.08%
Solve -- other: 0.3%
Adjust (information): 1%
 Change Appearance: 0%
 Clean (inform
ation): 0.05%
 Decode: 0%
Encode: 0.008%
 Equalize: 0%
Fill (inform
ation): 0.1%
Finish (inform
ation): 0%
Im
prove: 2%
Organize (analytically): 0.7%
 Perm
ute: 0%
Prepare (inform
ation): 0.3%
Process (inform
ation): 1%
Renew (inform
ation): 0%
Revise: 5%
 Service (inform
ation): 0.4%
Switch: 0%
 Transform
 inform
ation -- other: 0.3%
Translate: 1%
 Use: 0.4%
 Add (inform
ation): 0.02%
Com
bine inform
ation -- other: 0.008%
Connect (inform
ation): 0.05%
Gather (inform
ation): 0.4%
Incorporate (inform
ation): 0.2%
Pack (together) (information): 0%
 Synthesize (information): 0.05%
 Break (into components): 0%
 Cut (information): 0.7%
 Disconnect (information): 0%
 Remove (information): 0.02%
Separate information -- other: 0.2%
 Move information -- other: 0%
 Put information: 0.05%
Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0.008%
 Converse: 1%
 Correspond: 0.008%
 Debate: 0.04%
 Exchange information -- other: 0.05%
 Interview: 0.2%
 Mediate: 0%
 Meet: 0.02%
 Negotiate: 0.02%
 Network: 0.02%
 Reach: 0.03%
 Teach: 3%
 Access: 0.2%
 Download: 0.008%
 Evaluate: 2%
 Gather (information): 0.4%
 Get information -- other: 0.07%
 Import: 0.008%
 Learn: 0.9%
 Perceive: 3%
 Understand: 0.09%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0.3%
 Provide decision: 0%
 Provide money: 0%
 Send information: 8%
 Communicate (transfer information end-to-end) -- other: 0.3%
 Store (Activity): 0%
 Store (Actor): 0.05%
Store (Information): 0.008%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 0.5%
Ticket: 0%
Buy -- other: 0.05%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0.3%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0.008%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0.08%
Sell Service: 0.008%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0.02%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 2%
Exchange information: 5%
Get information: 7%
Provide information: 8%
End service: 0%
Exchange service: 0.1%
Get service: 5%
Provide service: 2%
Exchange physical objects: 0%
Get physical objects: 0%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0.008%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0.3%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0.06%
 Raise (funds) -- other: 0.03%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 1%
 Conduct: 0.3%
 M
ake: 0%
Perform
 (action) -- other: 0.09%
Practice: 0.008%
 Rehearse: 0.2%
 Run (perform
): 0%
Im
prove -- other: 1.0%
Optim
ize: 0.9%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0.08%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0%
Clean (physical): 0%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0%
 Process (physical): 0%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
 Cut (physical): 0%
 Disassemble: 0%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0%
 Consolidate: 0%
 Cover: 0%
Enclose: 0%
Gather (physical): 0%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0%
Reorient physical objects: 0%
Transport physical objects: 0%
 Assemble -- other: 0%
Configure (physical): 0%
Construct (physical): 0%
 Copy (physical): 0%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 0%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0%
Fig. F13: Distribution of AI applications in 2025.
86

Appendix G Robotics dataset
G.1 IFR taxonomy of robotic systems
The International Federation of Robotics (IFR) classifies robotic systems into two
main categories: industrial and service robots, defined as follows:
• Industrial robotsdefined as “automatically controlled, reprogrammable, multi-
purpose manipulators, programmable in three or more axes, which can be either
fixed in place or mounted on a mobile platform for use in industrial automation
applications” [12] and
• Service robotsdefined as robots that “perform useful tasks for humans or
equipment” outside traditional industrial automation contexts [11].
Service robots are further classified as professional service robots, medical robots
and consumer robots. Table G8, Table G9, Table G10 and Table G11 present the
corresponding taxonomies of classes and subclasses for industrial, professional service,
medical and consumer robots, respectively. Table G12 presents our classification of
each subclass onto our ontology.
T able G8:IFR taxonomy of industrial robots.Column headings are classes
and items within each column are subclasses.
Handling
Operation
W elding Dispensing Cutting/
Process-
ing
Assembling Others
Metal casting Arc welding Painting,
enamelling
Laser
cutting
Assembling Cleanroom for
FPD
Plastic mold-
ing
Spot welding Sealing mate-
rial
Water jet
cutting
Assembling
unspecified
Cleanroom for
semiconduc-
tors
Stamping,
forging,
bending
Laser
welding
Other dis-
pensing,
spraying
Grinding Disassembling Cleanroom for
others
Handling
operation at
machine tools
Welding
other
Dispensing
unspecified
Processing
other
Service appli-
cations
Machine
tending
Soldering Processing
unspecified
Medical appli-
cations
Measurement,
inspection,
testing
Welding
unspecified
Others
Continued on next page
87

T able G8:IFR taxonomy of industrial robots.(continued)
Handling
Operation
W elding Dispensing Cutting/
Process-
ing
Assembling Others
Palletizing Unspecified
Packaging,
picking,
placing
Material han-
dling
Handling
operations
unspecified
T able G9:IFR taxonomy of service professional robots.
Agriculture Cleaning Inspection Construction/
Demolition
Cultivation Clean floor Inspect building Construction demoli-
tion
Milking Disinfect Inspect other
Farming other Cleaning other
T ransportation/
Logistics
Search/Rescue/
Security
Hospitality Other
Indoors without pub-
lic
Search, rescue ser-
vices
Prepare food Other
Indoors with public Security Mobile guidance,
telepresence
Outdoors without
public
Outdoors with pub-
lic; other transporta-
tion and logistics
88

T able G10:IFR taxonomy of
medical robots.
Medical robots
Diagnostics and medical analysis
Perform surgery
Rehabilitation and non-invasive therapy
Other medical robots
T able G11:IFR taxonomy of service consumer robots.
Domestic tasks Social interaction,
education
Care at home Consumer other
Cleaning floors
indoor
Social interaction,
companions
Mobility assistants,
assist eating
Other consumer
robots
Window cleaning,
gardening and other
domestic tasks
Education Manipulation aids
and other care robots
Cleaning outdoors
89

G.2 Classification of IFR subclasses onto the ontology
Table G12 shows the mapping of the IFR subclasses to the Ontology and Figure G14
shows the distribution of robotic systems deployed in 2024 excluding the node “Clean
floor”.
T able G12:Mapping of IFR subclasses to ontology work activities.
IFR Subclass Ontology W ork Activity
Industrial robots
Metal casting Pour Metal
Handling for plastic molding Mold Material
Handling for stamping/forging Shape Material
Handling operations at machine tools Operate Tool
Machine tending for other processes Tend Machine
Measurement, inspection, testing Measure (Physical Object)
Palletizing Stack (Physical Object)
Packaging, picking, placing Pack (together) (Physical Object)
Material handling Handling Object
Handling operations unspecified Handling Object
Arc welding Weld Metal
Spot welding Weld Connection
Laser welding Weld Connection
Other welding Weld (Physical Object)
Soldering Solder (Physical Object)
Welding unspecified Weld (Physical Object)
Painting and enamelling Coat (Physical Object)
Application of adhesive, sealing material Apply Sealer
Other dispensing/spraying Spray (Physical Object)
Dispensing unspecified Spray (Physical Object)
Laser cutting Cut Material
Water jet cutting Cut Material
Mechanical cutting/grinding/deburring Smooth (Physical Object)
Other processing Process (Physical Object)
Continued on next page
90

T able G12:Mapping of IFR Subclasses to Ontology W ork Activities.
(continued)
IFR Subclass Ontology W ork Activity
Processing unspecified Process (Physical Object)
Assembling Assemble (Physical Object)
Assembling unspecified Assemble (Physical Object)
Disassembling Disassemble (Physical Object)
Cleanroom for FPD Fabricate Panel
Cleanroom for semiconductors Fabricate Panel
Cleanroom for others Fabricate (Physical Object)
Service applications (other) Assist (Activity)
Medical applications (industrial) Treat (Actor)
Other (industrial) Act on Physical Objects (Do)
Unspecified (industrial) Act on Physical Objects (Do)
Professional service robots
Cultivation (harvest) Harvest Crop
Milking Collect Fluid
Other (farming/agriculture) Cultivate
Professional clean floor Clean Floor
Disinfect Disinfect (Physical Object)
Professional clean other Clean (Physical Object)
Inspect building / construction Inspect Building
Inspect other Inspect (Physical Object)
Construction / demolition Construct (Physical Object)
Transportation and logistics indoors without public Transport (Physical Object)
Transportation and logistics indoors with public Transport (Physical Object)
Transportation and logistics outdoors without public Transport (Physical Object)
Outdoor environments with public traffic Transport (Physical Object)
Rescue services / firefighting Rescue (Actor)
Security services Patrol Area
Continued on next page
91

T able G12:Mapping of IFR Subclasses to Ontology W ork Activities.
(continued)
IFR Subclass Ontology W ork Activity
Prepare food/drinks Prepare Product
Mobile guidance / information / telepresence Guide (Actor)
Other professional service robots Perform Service
Medical robots
Diagnostics and medical laboratory analysis Conduct Diagnostic
Perform surgery Perform Surgery
Rehabilitation and non-invasive therapy Provide Rehabilitation
Other medical robots Assist Patient
Consumer service robots
Cleaning floors indoor (domestic) Clean Floor
Window cleaning, other domestic tasks Clean Window
Gardening and other domestic tasks Care for Lawn
Cleaning outdoors (domestic) Clean Yard
Social interaction / companions Provide Companionship
Education Teach (Actor)
Mobility assistants / assist eating Assist Individual
Manipulation aids and other care robots Provide Care
Other consumer robots Interact Client
92

Act: 100%
Act on information
(“Think”): 9%
Act with other activities and actors (“Interact”): 46% Act on physical objects (“Do”): 55%
Createinformation: 0%
Modify
information: 0%
Transfer
information: 9%
Storeinformation: 0%
Transfer between
actors: 46%
Act onactivities: 0.3%
Modify physicalobjects: 52%
Create physicalobjects: 2%
Store physical
objects: 0%
Transfer physical
objects: 1%
Plan: 0%
Analyze: 0%
Decide: 0%Calculate: 0% Express information: 0% Assemble information: 0% Reason: 0% Create information -- other: 0% Solve: 0%
Transform information: 0% Com bine inform
ation: 0%
Separate information: 0% Move information: 0%Exchange information: 8%
Get information: 0.8%Provide information: 0% Communicate (transfer information end-to-end): 0% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 4%
Buy: 0%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 9%
Transfer service: 28%
Transfer physical objects: 1%
Interact: 5%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0%
Communicate (transfer information end-to-end): 0%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0% W ithhold: 0%
Perform
 (action): 0.3%
Improve: 0%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0% Pass (achieve): 0% Undertake: 0% Transform physical objects: 45%
Separate physical objects: 0.07%
Combine physical objects: 4%
Move physical objects: 3%
Assemble: 1%
Fabricate: 0.7%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 1%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0%
Outline: 0%
Plan -- other: 0%
Propose: 0%
Schedule: 0%
Stage: 0%
 Analyze -- other: 0%
Characterize: 0%
 Correlate: 0%
 Determine: 0%
 Experiment: 0%
 Investigate: 0%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0%
 Reject: 0%
 Rule: 0%
 Select: 0%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0%
 Count: 0%
 Estimate: 0%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0%
 Record: 0%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0%
 Reason -- other: 0%
 Create (Activity): 0%
 Create (Actor): 0%
Create (Information): 0%
 Address (solve): 0%
 Resolve: 0%
Solve -- other: 0%
Adjust (information): 0%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 0%
Organize (analytically): 0%
 Perm
ute: 0%
Prepare (inform
ation): 0%
Process (inform
ation): 0%
Renew (inform
ation): 0%
Revise: 0%
 Service (inform
ation): 0%
Switch: 0%
 Transform
 inform
ation -- other: 0%
Translate: 0%
 Use: 0%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0%
Gather (inform
ation): 0%
Incorporate (inform
ation): 0%
Pack (together) (information): 0%
 Synthesize (information): 0%
 Break (into components): 0%
 Cut (information): 0%
 Disconnect (information): 0%
 Remove (information): 0%
 Separate information -- other: 0%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 0%
 Correspond: 0%
 Debate: 0%
 Exchange information -- other: 0%
 Interview: 0%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0%
 Network: 0%
 Reach: 0%
 Teach: 8%
 Access: 0%
 Download: 0%
 Evaluate: 0.5%
 Gather (information): 0%
 Get information -- other: 0%
 Import: 0%
 Learn: 0%
 Perceive: 0.3%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0%
 Provide decision: 0%
 Provide money: 0%
 Send information: 0%
 Communicate (transfer information end-to-end) -- other: 0%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 4%
Ticket: 0%
Buy -- other: 0%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 0%
Exchange information: 8%
Get information: 0.8%
Provide information: 0%
End service: 0%
Exchange service: 0%
Get service: 4%
Provide service: 24%
Exchange physical objects: 0%
Get physical objects: 1%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 5%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 0%
 Conduct: 0.1%
 M
ake: 0%
Perform
 (action) -- other: 0.2%
Practice: 0%
 Rehearse: 0%
 Run (perform
): 0%
Im
prove -- other: 0%
Optim
ize: 0%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0.06%
 Clean (physical): 45%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0%
Process (physical): 0.05%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0.2%
Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
Cut (physical): 0.02%
Disassemble: 0.001%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0.05%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 2%
 Consolidate: 0%
 Cover: 0.3%
Enclose: 1.0%
Gather (physical): 1%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0.6%
Reorient physical objects: 0%
Transport physical objects: 2%
Assemble -- other: 1.0%
Configure (physical): 0%
Construct (physical): 0.007%
 Copy (physical): 0.5%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0.7%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 1%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0%
Fig. G14:Sunburst diagram showing the distribution of robotic systems
deployed in 2024 excluding the node “Clean floor”.
93

G.3 Robotics Sunburst diagrams (2015–2024)
Act: 100%
Act on information
(“Think”): 6%
Act with other activities and actors (“Interact”): 34% Act on physical objects (“Do”): 67%
Createinformation: 0%
Modify
information: 0%
Transfer
information: 6%
Storeinformation: 0%
Transfer between
actors: 33%
Act onactivities: 0.02%
Modify physicalobjects: 66%
Create physicalobjects: 1%
Store physical
objects: 0%
Transfer physical
objects: 0.3%
Plan: 0%
Analyze: 0%
Decide: 0%Calculate: 0% Express information: 0% Assemble information: 0% Reason: 0% Create information -- other: 0% Solve: 0%
Transform information: 0% Com bine inform
ation: 0%
Separate information: 0% Move information: 0%Exchange information: 5%
Get information: 0.07%Provide information: 0% Communicate (transfer information end-to-end): 0% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 25%
Buy: 0%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 6%
Transfer service: 3%
Transfer physical objects: 0.3%
Interact: 0.007%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0%
Communicate (transfer information end-to-end): 0%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0% W ithhold: 0%
Perform
 (action): 0.02%
Improve: 0%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0% Pass (achieve): 0% Undertake: 0% Transform physical objects: 63%
Separate physical objects: 0.06%
Combine physical objects: 2%
Move physical objects: 0.5%
Assemble: 0.8%
Fabricate: 0.3%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 0.3%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0%
Outline: 0%
Plan -- other: 0%
Propose: 0%
Schedule: 0%
Stage: 0%
 Analyze -- other: 0%
Characterize: 0%
 Correlate: 0%
 Determine: 0%
 Experiment: 0%
 Investigate: 0%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0%
 Reject: 0%
 Rule: 0%
 Select: 0%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0%
 Count: 0%
 Estimate: 0%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0%
 Record: 0%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0%
 Reason -- other: 0%
 Create (Activity): 0%
 Create (Actor): 0%
Create (Information): 0%
 Address (solve): 0%
 Resolve: 0%
Solve -- other: 0%
Adjust (information): 0%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 0%
Organize (analytically): 0%
 Perm
ute: 0%
Prepare (inform
ation): 0%
Process (inform
ation): 0%
Renew (inform
ation): 0%
Revise: 0%
 Service (inform
ation): 0%
Switch: 0%
 Transform
 inform
ation -- other: 0%
Translate: 0%
 Use: 0%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0%
Gather (inform
ation): 0%
Incorporate (inform
ation): 0%
Pack (together) (information): 0%
 Synthesize (information): 0%
 Break (into components): 0%
 Cut (information): 0%
 Disconnect (information): 0%
 Remove (information): 0%
 Separate information -- other: 0%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 0%
 Correspond: 0%
 Debate: 0%
 Exchange information -- other: 0%
 Interview: 0%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0%
 Network: 0%
 Reach: 0%
 Teach: 5%
 Access: 0%
 Download: 0%
 Evaluate: 0.06%
 Gather (information): 0%
 Get information -- other: 0%
 Import: 0%
 Learn: 0%
 Perceive: 0.01%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0%
 Provide decision: 0%
 Provide money: 0%
 Send information: 0%
 Communicate (transfer information end-to-end) -- other: 0%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 25%
Ticket: 0%
Buy -- other: 0%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 0%
Exchange information: 5%
Get information: 0.07%
Provide information: 0%
End service: 0%
Exchange service: 0%
Get service: 0.9%
Provide service: 2%
Exchange physical objects: 0%
Get physical objects: 0.3%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0.007%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 0%
 Conduct: 0.002%
 M
ake: 0%
Perform
 (action) -- other: 0.02%
Practice: 0%
 Rehearse: 0%
 Run (perform
): 0%
Im
prove -- other: 0%
Optim
ize: 0%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0.07%
 Clean (physical): 63%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 6e-05%
 Process (physical): 0.01%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0.04%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
Cut (physical): 0.02%
Disassemble: 0.004%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0.04%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 1%
 Consolidate: 0%
 Cover: 0.1%
Enclose: 0.5%
Gather (physical): 0.3%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0.2%
Reorient physical objects: 0%
Transport physical objects: 0.3%
Assemble -- other: 0.4%
Configure (physical): 0%
Construct (physical): 0.01%
 Copy (physical): 0.4%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0.3%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 0.3%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0%
Fig. G15: Distribution of robot units in 2015.
94

Act: 100%
Act on information
(“Think”): 6%
Act with other activities and actors (“Interact”): 34% Act on physical objects (“Do”): 66%
Createinformation: 0%
Modify
information: 0%
Transfer
information: 6%
Storeinformation: 0%
Transfer between
actors: 34%
Act onactivities: 0.02%
Modify physicalobjects: 65%
Create physicalobjects: 1%
Store physical
objects: 0%
Transfer physical
objects: 0.3%
Plan: 0%
Analyze: 0%
Decide: 0%Calculate: 0% Express information: 0% Assemble information: 0% Reason: 0% Create information -- other: 0% Solve: 0%
Transform information: 0% Com bine inform
ation: 0%
Separate information: 0% Move information: 0%Exchange information: 6%
Get information: 0.07%Provide information: 0% Communicate (transfer information end-to-end): 0% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 25%
Buy: 0%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 6%
Transfer service: 3%
Transfer physical objects: 0.3%
Interact: 0.006%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0%
Communicate (transfer information end-to-end): 0%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0% W ithhold: 0%
Perform
 (action): 0.02%
Improve: 0%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0% Pass (achieve): 0% Undertake: 0% Transform physical objects: 62%
Separate physical objects: 0.05%
Combine physical objects: 2%
Move physical objects: 0.5%
Assemble: 0.8%
Fabricate: 0.3%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 0.3%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0%
Outline: 0%
Plan -- other: 0%
Propose: 0%
Schedule: 0%
Stage: 0%
 Analyze -- other: 0%
Characterize: 0%
 Correlate: 0%
 Determine: 0%
 Experiment: 0%
 Investigate: 0%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0%
 Reject: 0%
 Rule: 0%
 Select: 0%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0%
 Count: 0%
 Estimate: 0%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0%
 Record: 0%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0%
 Reason -- other: 0%
 Create (Activity): 0%
 Create (Actor): 0%
Create (Information): 0%
 Address (solve): 0%
 Resolve: 0%
Solve -- other: 0%
Adjust (information): 0%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 0%
Organize (analytically): 0%
 Perm
ute: 0%
Prepare (inform
ation): 0%
Process (inform
ation): 0%
Renew (inform
ation): 0%
Revise: 0%
 Service (inform
ation): 0%
Switch: 0%
 Transform
 inform
ation -- other: 0%
Translate: 0%
 Use: 0%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0%
Gather (inform
ation): 0%
Incorporate (inform
ation): 0%
Pack (together) (information): 0%
 Synthesize (information): 0%
 Break (into components): 0%
 Cut (information): 0%
 Disconnect (information): 0%
 Remove (information): 0%
 Separate information -- other: 0%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 0%
 Correspond: 0%
 Debate: 0%
 Exchange information -- other: 0%
 Interview: 0%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0%
 Network: 0%
 Reach: 0%
 Teach: 6%
 Access: 0%
 Download: 0%
 Evaluate: 0.05%
 Gather (information): 0%
 Get information -- other: 0%
 Import: 0%
 Learn: 0%
 Perceive: 0.01%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0%
 Provide decision: 0%
 Provide money: 0%
 Send information: 0%
 Communicate (transfer information end-to-end) -- other: 0%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 25%
Ticket: 0%
Buy -- other: 0%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 0%
Exchange information: 6%
Get information: 0.07%
Provide information: 0%
End service: 0%
Exchange service: 0%
Get service: 0.9%
Provide service: 2%
Exchange physical objects: 0%
Get physical objects: 0.3%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0.006%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 0%
 Conduct: 0.002%
 M
ake: 0%
Perform
 (action) -- other: 0.02%
Practice: 0%
 Rehearse: 0%
 Run (perform
): 0%
Im
prove -- other: 0%
Optim
ize: 0%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0.05%
 Clean (physical): 62%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0.0009%
 Process (physical): 0.01%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0.04%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
Cut (physical): 0.01%
Disassemble: 0.003%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0.03%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 1%
 Consolidate: 0%
 Cover: 0.1%
Enclose: 0.5%
Gather (physical): 0.3%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0.2%
Reorient physical objects: 0%
Transport physical objects: 0.3%
Assemble -- other: 0.5%
Configure (physical): 0%
Construct (physical): 0.01%
 Copy (physical): 0.3%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0.3%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 0.3%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0%
Fig. G16: Distribution of robot units in 2016.
95

Act: 100%
Act on information
(“Think”): 5%
Act with other activities and actors (“Interact”): 43% Act on physical objects (“Do”): 64%
Createinformation: 0%
Modify
information: 0%
Transfer
information: 5%
Storeinformation: 0%
Transfer between
actors: 37%
Act onactivities: 6%
Modify physicalobjects: 63%
Create physicalobjects: 1.0%
Store physical
objects: 0%
Transfer physical
objects: 8%
Plan: 0%
Analyze: 0%
Decide: 0%Calculate: 0% Express information: 0% Assemble information: 0% Reason: 0% Create information -- other: 0% Solve: 0%
Transform information: 0% Com bine inform
ation: 0%
Separate information: 0% Move information: 0%Exchange information: 5%
Get information: 0.8%Provide information: 0% Communicate (transfer information end-to-end): 0% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 22%
Buy: 0%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 5%
Transfer service: 3%
Transfer physical objects: 8%
Interact: 0.003%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0%
Communicate (transfer information end-to-end): 0%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0% W ithhold: 0%
Perform
 (action): 6%
Improve: 0%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0% Pass (achieve): 0% Undertake: 0% Transform physical objects: 48%
Separate physical objects: 0.03%
Combine physical objects: 9%
Move physical objects: 7%
Assemble: 0.7%
Fabricate: 0.2%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 8%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0%
Outline: 0%
Plan -- other: 0%
Propose: 0%
Schedule: 0%
Stage: 0%
 Analyze -- other: 0%
Characterize: 0%
 Correlate: 0%
 Determine: 0%
 Experiment: 0%
 Investigate: 0%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0%
 Reject: 0%
 Rule: 0%
 Select: 0%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0%
 Count: 0%
 Estimate: 0%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0%
 Record: 0%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0%
 Reason -- other: 0%
 Create (Activity): 0%
 Create (Actor): 0%
Create (Information): 0%
 Address (solve): 0%
 Resolve: 0%
Solve -- other: 0%
Adjust (information): 0%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 0%
Organize (analytically): 0%
 Perm
ute: 0%
Prepare (inform
ation): 0%
Process (inform
ation): 0%
Renew (inform
ation): 0%
Revise: 0%
 Service (inform
ation): 0%
Switch: 0%
 Transform
 inform
ation -- other: 0%
Translate: 0%
 Use: 0%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0%
Gather (inform
ation): 0%
Incorporate (inform
ation): 0%
Pack (together) (information): 0%
 Synthesize (information): 0%
 Break (into components): 0%
 Cut (information): 0%
 Disconnect (information): 0%
 Remove (information): 0%
 Separate information -- other: 0%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 0%
 Correspond: 0%
 Debate: 0%
 Exchange information -- other: 0%
 Interview: 0%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0%
 Network: 0%
 Reach: 0%
 Teach: 5%
 Access: 0%
 Download: 0%
 Evaluate: 0.05%
 Gather (information): 0%
 Get information -- other: 0%
 Import: 0%
 Learn: 0%
 Perceive: 0.7%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0%
 Provide decision: 0%
 Provide money: 0%
 Send information: 0%
 Communicate (transfer information end-to-end) -- other: 0%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 22%
Ticket: 0%
Buy -- other: 0%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 0%
Exchange information: 5%
Get information: 0.8%
Provide information: 0%
End service: 0%
Exchange service: 0%
Get service: 1%
Provide service: 1%
Exchange physical objects: 0%
Get physical objects: 8%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0.003%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 0%
 Conduct: 0.06%
 M
ake: 0%
Perform
 (action) -- other: 6%
Practice: 0%
 Rehearse: 0%
 Run (perform
): 0%
Im
prove -- other: 0%
Optim
ize: 0%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0.04%
 Clean (physical): 48%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0.009%
 Process (physical): 0.01%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0.03%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
Cut (physical): 0.009%
 Disassemble: 0.001%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0.02%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0.7%
 Consolidate: 0%
 Cover: 0.09%
Enclose: 0.3%
Gather (physical): 8%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0.1%
Reorient physical objects: 0%
Transport physical objects: 7%
Assemble -- other: 0.4%
Configure (physical): 0%
Construct (physical): 0.2%
 Copy (physical): 0.2%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0.2%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 8%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0%
Fig. G17: Distribution of robot units in 2017.
96

Act: 100%
Act on information
(“Think”): 5%
Act with other activities and actors (“Interact”): 39% Act on physical objects (“Do”): 66%
Createinformation: 0%
Modify
information: 0%
Transfer
information: 5%
Storeinformation: 0%
Transfer between
actors: 35%
Act onactivities: 4%
Modify physicalobjects: 65%
Create physicalobjects: 0.8%
Store physical
objects: 0%
Transfer physical
objects: 5%
Plan: 0%
Analyze: 0%
Decide: 0%Calculate: 0% Express information: 0% Assemble information: 0% Reason: 0% Create information -- other: 0% Solve: 0%
Transform information: 0% Com bine inform
ation: 0%
Separate information: 0% Move information: 0%Exchange information: 4%
Get information: 0.6%Provide information: 0% Communicate (transfer information end-to-end): 0% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 21%
Buy: 0%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 5%
Transfer service: 3%
Transfer physical objects: 5%
Interact: 0.003%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0%
Communicate (transfer information end-to-end): 0%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0% W ithhold: 0%
Perform
 (action): 4%
Improve: 0%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0% Pass (achieve): 0% Undertake: 0% Transform physical objects: 54%
Separate physical objects: 0.02%
Combine physical objects: 6%
Move physical objects: 5%
Assemble: 0.6%
Fabricate: 0.2%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 5%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0%
Outline: 0%
Plan -- other: 0%
Propose: 0%
Schedule: 0%
Stage: 0%
 Analyze -- other: 0%
Characterize: 0%
 Correlate: 0%
 Determine: 0%
 Experiment: 0%
 Investigate: 0%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0%
 Reject: 0%
 Rule: 0%
 Select: 0%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0%
 Count: 0%
 Estimate: 0%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0%
 Record: 0%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0%
 Reason -- other: 0%
 Create (Activity): 0%
 Create (Actor): 0%
Create (Information): 0%
 Address (solve): 0%
 Resolve: 0%
Solve -- other: 0%
Adjust (information): 0%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 0%
Organize (analytically): 0%
 Perm
ute: 0%
Prepare (inform
ation): 0%
Process (inform
ation): 0%
Renew (inform
ation): 0%
Revise: 0%
 Service (inform
ation): 0%
Switch: 0%
 Transform
 inform
ation -- other: 0%
Translate: 0%
 Use: 0%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0%
Gather (inform
ation): 0%
Incorporate (inform
ation): 0%
Pack (together) (information): 0%
 Synthesize (information): 0%
 Break (into components): 0%
 Cut (information): 0%
 Disconnect (information): 0%
 Remove (information): 0%
 Separate information -- other: 0%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 0%
 Correspond: 0%
 Debate: 0%
 Exchange information -- other: 0%
 Interview: 0%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0%
 Network: 0%
 Reach: 0%
 Teach: 4%
 Access: 0%
 Download: 0%
 Evaluate: 0.05%
 Gather (information): 0%
 Get information -- other: 0%
 Import: 0%
 Learn: 0%
 Perceive: 0.5%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0%
 Provide decision: 0%
 Provide money: 0%
 Send information: 0%
 Communicate (transfer information end-to-end) -- other: 0%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 21%
Ticket: 0%
Buy -- other: 0%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 0%
Exchange information: 4%
Get information: 0.6%
Provide information: 0%
End service: 0%
Exchange service: 0%
Get service: 0.9%
Provide service: 2%
Exchange physical objects: 0%
Get physical objects: 5%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0.003%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 0%
 Conduct: 0.04%
 M
ake: 0%
Perform
 (action) -- other: 4%
Practice: 0%
 Rehearse: 0%
 Run (perform
): 0%
Im
prove -- other: 0%
Optim
ize: 0%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0.03%
 Clean (physical): 54%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0.006%
 Process (physical): 0.01%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0.03%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
Cut (physical): 0.008%
 Disassemble: 0.002%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0.01%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0.6%
 Consolidate: 0%
 Cover: 0.08%
Enclose: 0.3%
Gather (physical): 5%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0.1%
Reorient physical objects: 0%
Transport physical objects: 5%
Assemble -- other: 0.3%
Configure (physical): 0%
Construct (physical): 0.1%
 Copy (physical): 0.2%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0.2%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 5%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0%
Fig. G18: Distribution of robot units in 2018.
97

Act: 100%
Act on information
(“Think”): 4%
Act with other activities and actors (“Interact”): 32% Act on physical objects (“Do”): 72%
Createinformation: 0%
Modify
information: 0%
Transfer
information: 4%
Storeinformation: 0%
Transfer between
actors: 29%
Act onactivities: 3%
Modify physicalobjects: 71%
Create physicalobjects: 0.7%
Store physical
objects: 0%
Transfer physical
objects: 4%
Plan: 0%
Analyze: 0%
Decide: 0%Calculate: 0% Express information: 0% Assemble information: 0% Reason: 0% Create information -- other: 0% Solve: 0%
Transform information: 0% Com bine inform
ation: 0%
Separate information: 0% Move information: 0%Exchange information: 4%
Get information: 0.4%Provide information: 0% Communicate (transfer information end-to-end): 0% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 17%
Buy: 0%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 4%
Transfer service: 4%
Transfer physical objects: 4%
Interact: 0.003%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0%
Communicate (transfer information end-to-end): 0%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0% W ithhold: 0%
Perform
 (action): 3%
Improve: 0%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0% Pass (achieve): 0% Undertake: 0% Transform physical objects: 63%
Separate physical objects: 0.02%
Combine physical objects: 5%
Move physical objects: 4%
Assemble: 0.5%
Fabricate: 0.2%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 4%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0%
Outline: 0%
Plan -- other: 0%
Propose: 0%
Schedule: 0%
Stage: 0%
 Analyze -- other: 0%
Characterize: 0%
 Correlate: 0%
 Determine: 0%
 Experiment: 0%
 Investigate: 0%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0%
 Reject: 0%
 Rule: 0%
 Select: 0%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0%
 Count: 0%
 Estimate: 0%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0%
 Record: 0%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0%
 Reason -- other: 0%
 Create (Activity): 0%
 Create (Actor): 0%
Create (Information): 0%
 Address (solve): 0%
 Resolve: 0%
Solve -- other: 0%
Adjust (information): 0%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 0%
Organize (analytically): 0%
 Perm
ute: 0%
Prepare (inform
ation): 0%
Process (inform
ation): 0%
Renew (inform
ation): 0%
Revise: 0%
 Service (inform
ation): 0%
Switch: 0%
 Transform
 inform
ation -- other: 0%
Translate: 0%
 Use: 0%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0%
Gather (inform
ation): 0%
Incorporate (inform
ation): 0%
Pack (together) (information): 0%
 Synthesize (information): 0%
 Break (into components): 0%
 Cut (information): 0%
 Disconnect (information): 0%
 Remove (information): 0%
 Separate information -- other: 0%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 0%
 Correspond: 0%
 Debate: 0%
 Exchange information -- other: 0%
 Interview: 0%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0%
 Network: 0%
 Reach: 0%
 Teach: 4%
 Access: 0%
 Download: 0%
 Evaluate: 0.04%
 Gather (information): 0%
 Get information -- other: 0%
 Import: 0%
 Learn: 0%
 Perceive: 0.4%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0%
 Provide decision: 0%
 Provide money: 0%
 Send information: 0%
 Communicate (transfer information end-to-end) -- other: 0%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 17%
Ticket: 0%
Buy -- other: 0%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 0%
Exchange information: 4%
Get information: 0.4%
Provide information: 0%
End service: 0%
Exchange service: 0%
Get service: 0.8%
Provide service: 3%
Exchange physical objects: 0%
Get physical objects: 4%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0.003%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 0%
 Conduct: 0.03%
 M
ake: 0%
Perform
 (action) -- other: 3%
Practice: 0%
 Rehearse: 0%
 Run (perform
): 0%
Im
prove -- other: 0%
Optim
ize: 0%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0.03%
 Clean (physical): 63%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0.006%
 Process (physical): 0.01%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0.02%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
Cut (physical): 0.007%
 Disassemble: 0.002%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0.01%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0.6%
 Consolidate: 0%
 Cover: 0.07%
Enclose: 0.2%
Gather (physical): 4%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0.1%
Reorient physical objects: 0%
Transport physical objects: 3%
Assemble -- other: 0.3%
Configure (physical): 0%
Construct (physical): 0.08%
 Copy (physical): 0.2%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0.2%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 4%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0%
Fig. G19: Distribution of robot units in 2019.
98

Act: 100%
Act on information
(“Think”): 4%
Act with other activities and actors (“Interact”): 28% Act on physical objects (“Do”): 75%
Createinformation: 0%
Modify
information: 0%
Transfer
information: 4%
Storeinformation: 0%
Transfer between
actors: 26%
Act onactivities: 2%
Modify physicalobjects: 74%
Create physicalobjects: 0.7%
Store physical
objects: 0%
Transfer physical
objects: 3%
Plan: 0%
Analyze: 0%
Decide: 0%Calculate: 0% Express information: 0% Assemble information: 0% Reason: 0% Create information -- other: 0% Solve: 0%
Transform information: 0% Com bine inform
ation: 0%
Separate information: 0% Move information: 0%Exchange information: 4%
Get information: 0.4%Provide information: 0% Communicate (transfer information end-to-end): 0% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 14%
Buy: 0%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 4%
Transfer service: 4%
Transfer physical objects: 3%
Interact: 0.002%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0%
Communicate (transfer information end-to-end): 0%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0% W ithhold: 0%
Perform
 (action): 2%
Improve: 0%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0% Pass (achieve): 0% Undertake: 0% Transform physical objects: 67%
Separate physical objects: 0.02%
Combine physical objects: 4%
Move physical objects: 3%
Assemble: 0.5%
Fabricate: 0.2%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 3%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0%
Outline: 0%
Plan -- other: 0%
Propose: 0%
Schedule: 0%
Stage: 0%
 Analyze -- other: 0%
Characterize: 0%
 Correlate: 0%
 Determine: 0%
 Experiment: 0%
 Investigate: 0%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0%
 Reject: 0%
 Rule: 0%
 Select: 0%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0%
 Count: 0%
 Estimate: 0%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0%
 Record: 0%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0%
 Reason -- other: 0%
 Create (Activity): 0%
 Create (Actor): 0%
Create (Information): 0%
 Address (solve): 0%
 Resolve: 0%
Solve -- other: 0%
Adjust (information): 0%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 0%
Organize (analytically): 0%
 Perm
ute: 0%
Prepare (inform
ation): 0%
Process (inform
ation): 0%
Renew (inform
ation): 0%
Revise: 0%
 Service (inform
ation): 0%
Switch: 0%
 Transform
 inform
ation -- other: 0%
Translate: 0%
 Use: 0%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0%
Gather (inform
ation): 0%
Incorporate (inform
ation): 0%
Pack (together) (information): 0%
 Synthesize (information): 0%
 Break (into components): 0%
 Cut (information): 0%
 Disconnect (information): 0%
 Remove (information): 0%
 Separate information -- other: 0%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 0%
 Correspond: 0%
 Debate: 0%
 Exchange information -- other: 0%
 Interview: 0%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0%
 Network: 0%
 Reach: 0%
 Teach: 4%
 Access: 0%
 Download: 0%
 Evaluate: 0.04%
 Gather (information): 0%
 Get information -- other: 0%
 Import: 0%
 Learn: 0%
 Perceive: 0.3%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0%
 Provide decision: 0%
 Provide money: 0%
 Send information: 0%
 Communicate (transfer information end-to-end) -- other: 0%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 14%
Ticket: 0%
Buy -- other: 0%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 0%
Exchange information: 4%
Get information: 0.4%
Provide information: 0%
End service: 0%
Exchange service: 0%
Get service: 0.8%
Provide service: 4%
Exchange physical objects: 0%
Get physical objects: 3%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0.002%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 0%
 Conduct: 0.03%
 M
ake: 0%
Perform
 (action) -- other: 2%
Practice: 0%
 Rehearse: 0%
 Run (perform
): 0%
Im
prove -- other: 0%
Optim
ize: 0%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0.02%
 Clean (physical): 67%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0.006%
 Process (physical): 0.009%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0.02%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
Cut (physical): 0.007%
 Disassemble: 0.002%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0.01%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0.5%
 Consolidate: 0%
 Cover: 0.07%
Enclose: 0.2%
Gather (physical): 3%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0.1%
Reorient physical objects: 0%
Transport physical objects: 3%
Assemble -- other: 0.3%
Configure (physical): 0%
Construct (physical): 0.07%
 Copy (physical): 0.2%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0.2%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 3%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0%
Fig. G20: Distribution of robot units in 2020.
99

Act: 100%
Act on information
(“Think”): 4%
Act with other activities and actors (“Interact”): 28% Act on physical objects (“Do”): 75%
Createinformation: 0%
Modify
information: 0%
Transfer
information: 4%
Storeinformation: 0%
Transfer between
actors: 26%
Act onactivities: 2%
Modify physicalobjects: 74%
Create physicalobjects: 0.8%
Store physical
objects: 0%
Transfer physical
objects: 3%
Plan: 0%
Analyze: 0%
Decide: 0%Calculate: 0% Express information: 0% Assemble information: 0% Reason: 0% Create information -- other: 0% Solve: 0%
Transform information: 0% Com bine inform
ation: 0%
Separate information: 0% Move information: 0%Exchange information: 4%
Get information: 0.4%Provide information: 0% Communicate (transfer information end-to-end): 0% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 13%
Buy: 0%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 4%
Transfer service: 5%
Transfer physical objects: 3%
Interact: 0.002%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0%
Communicate (transfer information end-to-end): 0%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0% W ithhold: 0%
Perform
 (action): 2%
Improve: 0%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0% Pass (achieve): 0% Undertake: 0% Transform physical objects: 67%
Separate physical objects: 0.02%
Combine physical objects: 4%
Move physical objects: 3%
Assemble: 0.5%
Fabricate: 0.2%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 3%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0%
Outline: 0%
Plan -- other: 0%
Propose: 0%
Schedule: 0%
Stage: 0%
 Analyze -- other: 0%
Characterize: 0%
 Correlate: 0%
 Determine: 0%
 Experiment: 0%
 Investigate: 0%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0%
 Reject: 0%
 Rule: 0%
 Select: 0%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0%
 Count: 0%
 Estimate: 0%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0%
 Record: 0%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0%
 Reason -- other: 0%
 Create (Activity): 0%
 Create (Actor): 0%
Create (Information): 0%
 Address (solve): 0%
 Resolve: 0%
Solve -- other: 0%
Adjust (information): 0%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 0%
Organize (analytically): 0%
 Perm
ute: 0%
Prepare (inform
ation): 0%
Process (inform
ation): 0%
Renew (inform
ation): 0%
Revise: 0%
 Service (inform
ation): 0%
Switch: 0%
 Transform
 inform
ation -- other: 0%
Translate: 0%
 Use: 0%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0%
Gather (inform
ation): 0%
Incorporate (inform
ation): 0%
Pack (together) (information): 0%
 Synthesize (information): 0%
 Break (into components): 0%
 Cut (information): 0%
 Disconnect (information): 0%
 Remove (information): 0%
 Separate information -- other: 0%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 0%
 Correspond: 0%
 Debate: 0%
 Exchange information -- other: 0%
 Interview: 0%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0%
 Network: 0%
 Reach: 0%
 Teach: 4%
 Access: 0%
 Download: 0%
 Evaluate: 0.06%
 Gather (information): 0%
 Get information -- other: 0%
 Import: 0%
 Learn: 0%
 Perceive: 0.3%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0%
 Provide decision: 0%
 Provide money: 0%
 Send information: 0%
 Communicate (transfer information end-to-end) -- other: 0%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 13%
Ticket: 0%
Buy -- other: 0%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 0%
Exchange information: 4%
Get information: 0.4%
Provide information: 0%
End service: 0%
Exchange service: 0%
Get service: 0.8%
Provide service: 5%
Exchange physical objects: 0%
Get physical objects: 3%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0.002%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 0%
 Conduct: 0.03%
 M
ake: 0%
Perform
 (action) -- other: 2%
Practice: 0%
 Rehearse: 0%
 Run (perform
): 0%
Im
prove -- other: 0%
Optim
ize: 0%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0.03%
 Clean (physical): 67%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0.01%
 Process (physical): 0.01%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0.03%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
Cut (physical): 0.008%
 Disassemble: 0.004%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0.01%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0.6%
 Consolidate: 0%
 Cover: 0.07%
Enclose: 0.3%
Gather (physical): 3%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0.1%
Reorient physical objects: 0%
Transport physical objects: 3%
Assemble -- other: 0.3%
Configure (physical): 0%
Construct (physical): 0.06%
 Copy (physical): 0.2%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0.2%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 3%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0%
Fig. G21: Distribution of robot units in 2021.
100

Act: 100%
Act on information
(“Think”): 4%
Act with other activities and actors (“Interact”): 28% Act on physical objects (“Do”): 75%
Createinformation: 0%
Modify
information: 0%
Transfer
information: 4%
Storeinformation: 0%
Transfer between
actors: 26%
Act onactivities: 2%
Modify physicalobjects: 74%
Create physicalobjects: 0.8%
Store physical
objects: 0%
Transfer physical
objects: 3%
Plan: 0%
Analyze: 0%
Decide: 0%Calculate: 0% Express information: 0% Assemble information: 0% Reason: 0% Create information -- other: 0% Solve: 0%
Transform information: 0% Com bine inform
ation: 0%
Separate information: 0% Move information: 0%Exchange information: 4%
Get information: 0.4%Provide information: 0% Communicate (transfer information end-to-end): 0% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 12%
Buy: 0%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 4%
Transfer service: 6%
Transfer physical objects: 3%
Interact: 0.01%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0%
Communicate (transfer information end-to-end): 0%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0% W ithhold: 0%
Perform
 (action): 2%
Improve: 0%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0% Pass (achieve): 0% Undertake: 0% Transform physical objects: 67%
Separate physical objects: 0.03%
Combine physical objects: 4%
Move physical objects: 3%
Assemble: 0.6%
Fabricate: 0.2%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 3%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0%
Outline: 0%
Plan -- other: 0%
Propose: 0%
Schedule: 0%
Stage: 0%
 Analyze -- other: 0%
Characterize: 0%
 Correlate: 0%
 Determine: 0%
 Experiment: 0%
 Investigate: 0%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0%
 Reject: 0%
 Rule: 0%
 Select: 0%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0%
 Count: 0%
 Estimate: 0%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0%
 Record: 0%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0%
 Reason -- other: 0%
 Create (Activity): 0%
 Create (Actor): 0%
Create (Information): 0%
 Address (solve): 0%
 Resolve: 0%
Solve -- other: 0%
Adjust (information): 0%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 0%
Organize (analytically): 0%
 Perm
ute: 0%
Prepare (inform
ation): 0%
Process (inform
ation): 0%
Renew (inform
ation): 0%
Revise: 0%
 Service (inform
ation): 0%
Switch: 0%
 Transform
 inform
ation -- other: 0%
Translate: 0%
 Use: 0%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0%
Gather (inform
ation): 0%
Incorporate (inform
ation): 0%
Pack (together) (information): 0%
 Synthesize (information): 0%
 Break (into components): 0%
 Cut (information): 0%
 Disconnect (information): 0%
 Remove (information): 0%
 Separate information -- other: 0%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 0%
 Correspond: 0%
 Debate: 0%
 Exchange information -- other: 0%
 Interview: 0%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0%
 Network: 0%
 Reach: 0%
 Teach: 4%
 Access: 0%
 Download: 0%
 Evaluate: 0.07%
 Gather (information): 0%
 Get information -- other: 0%
 Import: 0%
 Learn: 0%
 Perceive: 0.3%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0%
 Provide decision: 0%
 Provide money: 0%
 Send information: 0%
 Communicate (transfer information end-to-end) -- other: 0%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 12%
Ticket: 0%
Buy -- other: 0%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 0%
Exchange information: 4%
Get information: 0.4%
Provide information: 0%
End service: 0%
Exchange service: 0%
Get service: 0.9%
Provide service: 5%
Exchange physical objects: 0%
Get physical objects: 3%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0.01%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 0%
 Conduct: 0.03%
 M
ake: 0%
Perform
 (action) -- other: 2%
Practice: 0%
 Rehearse: 0%
 Run (perform
): 0%
Im
prove -- other: 0%
Optim
ize: 0%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0.03%
 Clean (physical): 67%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0.02%
 Process (physical): 0.01%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0.04%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
Cut (physical): 0.008%
 Disassemble: 0.007%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0.01%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0.6%
 Consolidate: 0%
 Cover: 0.08%
Enclose: 0.3%
Gather (physical): 3%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0.1%
Reorient physical objects: 0%
Transport physical objects: 3%
Assemble -- other: 0.4%
Configure (physical): 0%
Construct (physical): 0.06%
 Copy (physical): 0.2%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0.2%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 3%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0%
Fig. G22: Distribution of robot units in 2022.
101

Act: 100%
Act on information
(“Think”): 4%
Act with other activities and actors (“Interact”): 25% Act on physical objects (“Do”): 77%
Createinformation: 0%
Modify
information: 0%
Transfer
information: 4%
Storeinformation: 0%
Transfer between
actors: 23%
Act onactivities: 2%
Modify physicalobjects: 76%
Create physicalobjects: 0.8%
Store physical
objects: 0%
Transfer physical
objects: 2%
Plan: 0%
Analyze: 0%
Decide: 0%Calculate: 0% Express information: 0% Assemble information: 0% Reason: 0% Create information -- other: 0% Solve: 0%
Transform information: 0% Com bine inform
ation: 0%
Separate information: 0% Move information: 0%Exchange information: 3%
Get information: 0.3%Provide information: 0% Communicate (transfer information end-to-end): 0% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 11%
Buy: 0%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 4%
Transfer service: 6%
Transfer physical objects: 2%
Interact: 0.2%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0%
Communicate (transfer information end-to-end): 0%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0% W ithhold: 0%
Perform
 (action): 2%
Improve: 0%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0% Pass (achieve): 0% Undertake: 0% Transform physical objects: 70%
Separate physical objects: 0.03%
Combine physical objects: 3%
Move physical objects: 2%
Assemble: 0.6%
Fabricate: 0.2%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 2%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0%
Outline: 0%
Plan -- other: 0%
Propose: 0%
Schedule: 0%
Stage: 0%
 Analyze -- other: 0%
Characterize: 0%
 Correlate: 0%
 Determine: 0%
 Experiment: 0%
 Investigate: 0%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0%
 Reject: 0%
 Rule: 0%
 Select: 0%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0%
 Count: 0%
 Estimate: 0%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0%
 Record: 0%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0%
 Reason -- other: 0%
 Create (Activity): 0%
 Create (Actor): 0%
Create (Information): 0%
 Address (solve): 0%
 Resolve: 0%
Solve -- other: 0%
Adjust (information): 0%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 0%
Organize (analytically): 0%
 Perm
ute: 0%
Prepare (inform
ation): 0%
Process (inform
ation): 0%
Renew (inform
ation): 0%
Revise: 0%
 Service (inform
ation): 0%
Switch: 0%
 Transform
 inform
ation -- other: 0%
Translate: 0%
 Use: 0%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0%
Gather (inform
ation): 0%
Incorporate (inform
ation): 0%
Pack (together) (information): 0%
 Synthesize (information): 0%
 Break (into components): 0%
 Cut (information): 0%
 Disconnect (information): 0%
 Remove (information): 0%
 Separate information -- other: 0%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 0%
 Correspond: 0%
 Debate: 0%
 Exchange information -- other: 0%
 Interview: 0%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0%
 Network: 0%
 Reach: 0%
 Teach: 3%
 Access: 0%
 Download: 0%
 Evaluate: 0.08%
 Gather (information): 0%
 Get information -- other: 0%
 Import: 0%
 Learn: 0%
 Perceive: 0.3%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0%
 Provide decision: 0%
 Provide money: 0%
 Send information: 0%
 Communicate (transfer information end-to-end) -- other: 0%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 11%
Ticket: 0%
Buy -- other: 0%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 0%
Exchange information: 3%
Get information: 0.3%
Provide information: 0%
End service: 0%
Exchange service: 0%
Get service: 1.0%
Provide service: 5%
Exchange physical objects: 0%
Get physical objects: 2%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0.2%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 0%
 Conduct: 0.03%
 M
ake: 0%
Perform
 (action) -- other: 2%
Practice: 0%
 Rehearse: 0%
 Run (perform
): 0%
Im
prove -- other: 0%
Optim
ize: 0%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0.03%
 Clean (physical): 70%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0.02%
 Process (physical): 0.01%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0.04%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
Cut (physical): 0.007%
 Disassemble: 0.008%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0.01%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0.6%
 Consolidate: 0%
 Cover: 0.08%
Enclose: 0.3%
Gather (physical): 2%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0.1%
Reorient physical objects: 0%
Transport physical objects: 2%
Assemble -- other: 0.3%
Configure (physical): 0%
Construct (physical): 0.05%
 Copy (physical): 0.2%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0.2%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 2%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0%
Fig. G23: Distribution of robot units in 2023.
102

Act: 100%
Act on information
(“Think”): 4%
Act with other activities and actors (“Interact”): 23% Act on physical objects (“Do”): 79%
Createinformation: 0%
Modify
information: 0%
Transfer
information: 4%
Storeinformation: 0%
Transfer between
actors: 22%
Act onactivities: 2%
Modify physicalobjects: 78%
Create physicalobjects: 0.7%
Store physical
objects: 0%
Transfer physical
objects: 2%
Plan: 0%
Analyze: 0%
Decide: 0%Calculate: 0% Express information: 0% Assemble information: 0% Reason: 0% Create information -- other: 0% Solve: 0%
Transform information: 0% Com bine inform
ation: 0%
Separate information: 0% Move information: 0%Exchange information: 3%
Get information: 0.3%Provide information: 0% Communicate (transfer information end-to-end): 0% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 9%
Buy: 0%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 4%
Transfer service: 6%
Transfer physical objects: 2%
Interact: 0.3%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0%
Communicate (transfer information end-to-end): 0%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0% W ithhold: 0%
Perform
 (action): 2%
Improve: 0%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0% Pass (achieve): 0% Undertake: 0% Transform physical objects: 73%
Separate physical objects: 0.03%
Combine physical objects: 3%
Move physical objects: 2%
Assemble: 0.5%
Fabricate: 0.2%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 2%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0%
Outline: 0%
Plan -- other: 0%
Propose: 0%
Schedule: 0%
Stage: 0%
 Analyze -- other: 0%
Characterize: 0%
 Correlate: 0%
 Determine: 0%
 Experiment: 0%
 Investigate: 0%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0%
 Reject: 0%
 Rule: 0%
 Select: 0%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0%
 Count: 0%
 Estimate: 0%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0%
 Record: 0%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0%
 Reason -- other: 0%
 Create (Activity): 0%
 Create (Actor): 0%
Create (Information): 0%
 Address (solve): 0%
 Resolve: 0%
Solve -- other: 0%
Adjust (information): 0%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 0%
Organize (analytically): 0%
 Perm
ute: 0%
Prepare (inform
ation): 0%
Process (inform
ation): 0%
Renew (inform
ation): 0%
Revise: 0%
 Service (inform
ation): 0%
Switch: 0%
 Transform
 inform
ation -- other: 0%
Translate: 0%
 Use: 0%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0%
Gather (inform
ation): 0%
Incorporate (inform
ation): 0%
Pack (together) (information): 0%
 Synthesize (information): 0%
 Break (into components): 0%
 Cut (information): 0%
 Disconnect (information): 0%
 Remove (information): 0%
 Separate information -- other: 0%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 0%
 Correspond: 0%
 Debate: 0%
 Exchange information -- other: 0%
 Interview: 0%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0%
 Network: 0%
 Reach: 0%
 Teach: 3%
 Access: 0%
 Download: 0%
 Evaluate: 0.08%
 Gather (information): 0%
 Get information -- other: 0%
 Import: 0%
 Learn: 0%
 Perceive: 0.2%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0%
 Provide decision: 0%
 Provide money: 0%
 Send information: 0%
 Communicate (transfer information end-to-end) -- other: 0%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 9%
Ticket: 0%
Buy -- other: 0%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 0%
Exchange information: 3%
Get information: 0.3%
Provide information: 0%
End service: 0%
Exchange service: 0%
Get service: 0.9%
Provide service: 5%
Exchange physical objects: 0%
Get physical objects: 2%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0.3%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 0%
 Conduct: 0.03%
 M
ake: 0%
Perform
 (action) -- other: 2%
Practice: 0%
 Rehearse: 0%
 Run (perform
): 0%
Im
prove -- other: 0%
Optim
ize: 0%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0.03%
 Clean (physical): 72%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0.02%
 Process (physical): 0.01%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0.04%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
Cut (physical): 0.007%
 Disassemble: 0.009%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0.01%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0.6%
 Consolidate: 0%
 Cover: 0.07%
Enclose: 0.3%
Gather (physical): 2%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0.1%
Reorient physical objects: 0%
Transport physical objects: 2%
Assemble -- other: 0.3%
Configure (physical): 0%
Construct (physical): 0.04%
 Copy (physical): 0.2%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0.2%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 2%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0%
Fig. G24: Distribution of robot units in 2024.
103

Appendix H Combining usage measures for AI
software applications and robotic
systems
H.1 Assumptions
To combine the measures of AI usage from AI software applications and robotic sys-
tems, we made the assumptions and completed the calculations listed below. We
believe that our approach is a plausible way to estimate the desired quantities. But it
is important to realize that all the results are only approximate, and we hope that we
and others can continue to develop better ways of estimating these numbers.
• Assumption 1:Thesize of the overall global AI marketin 2024 was USD 186.4
billion.
– Justification: [42, p. 20]
• Assumption 2:Thesize of the global market for robotic systemsin 2024 was USD
46.1 billion.
– Justification: [41, p. 7]
– Justification: Although there are other estimates available for the global
robotics market size, this source is closely aligned with the IFR report that
provided our primary data on robotics usage. There are close similarities
between the two sources in both:
∗market size estimates: USD 46.11 billion vs. USD 50.0 billion [12, p. 65]
∗definitions of robots and categories of robots.
• Assumption 3:Thesize of global market for AI software applicationsin 2024 was
USD 140.29 billion.
– Justification: The global AI market can be divided into two parts: (a) AI
software applications and (b) robotic systems. Therefore, subtracting the
robotics market size [Assumption 2] from the overall AI market size [Assump-
tion 1] should give a reasonable estimate for the size of the global market for
AI software.
• Assumption 4:Themapping of IFR subclasses to robotics industry segments
described in Step 2 of Section H.3 is a plausible basis for estimating market sizes
of the different IFR subclasses.
– Justification: This mapping was done by three knowledgeable experts in the
field of robotics who consulted a variety of reference materials in order to
make plausible inferences.
• Assumption 5:Themethod for estimating relative prices for IFR subclasses
described in Step 3 of Section H.3 is a plausible basis for estimating market sizes
of the different IFR subclasses.
– Justification: The estimation of relative prices was done by a knowledgeable
expert in the field of robotics who consulted publicly available price ranges for
representative robotic systems within each IFR subclass, drawing on industry
reports and manufacturer information.
104

• Assumption 6:Themathematical procedure for calculating market values of the
IFR subclasses based on their relative prices, as described in Steps 4 and 5 of
Section H.3, is a plausible method for estimating these numbers.
– Justification: The mathematical equations shown are self-evident logical con-
sequences of the meaning of the variables. But the method adjusts relative
prices separately for each industry segment, and that means the same robotic
subclass might receive different estimated prices in different industry seg-
ments. Even though these estimated prices are unlikely to be exactly correct,
the total market value attributed to subclasses that occur in multiple indus-
try segments is approximately 10%. So even ifallthese attributions of market
value were completely incorrect, the changes in results would be no more
than a total of 10% spread across all the activities in the ontology. Therefore,
we assume that the resulting market values will still be generally useful.
H.2 Estimating the market value of AI software applications
To calculate the market value of the AI applications in the TAAFT dataset, we first
estimated revenue for each application. Because direct revenue figures were not pub-
licly available for most applications in the dataset, we approximated revenue through
observable engagement and pricing signals. Using this, we estimated the relative
market share of each AI application within the TAAFT dataset using this formula:
Market shareapplication = Number of saves×Price×Billing frequencyP (Number of saves×Price×Billing frequency )
Then, using the ontology-based classification results described in Section 2.2.1,
we attributed each application’s estimated market share to the ontology activity in
which that application was classified. Aggregating across all applications produced an
estimated market share for each activity node in the ontology.
Next, to estimate the size of the global market for AI software applications, we
started with the estimated size of the overall AI market in 2024 (USD 186.4 billion)
[42, p. 20][Assumption 1], and then subtracted the size of the robotics market (USD
46.11 billion) [41, p. 7][Assumption 2]. This yielded a estimated market value of USD
140.29 billion for the global AI software applications market [Assumption 3]. In other
words, AI software applications account for 75% of the overall AI market value, and
robotic systems account for 25%.
Finally, to compute the market value of AI systems in each ontology activity, we
used the following formula:
Market valueactivity node = 140.29 B USD×Market share activity node
This procedure provides an approximate, ontology-informed view of how the global
market value of AI software applications is distributed across different categories of
activities.
105

H.3 Estimating the market value of robotic systems
To estimate the market value of each robot subclass, we performed the following steps:
Step 1: Estimate market sizes for different robotics industry segments
We began with the global robotics market estimate, which Statista reports as USD
46.1 billion [41, p. 7] in 2024[Assumption 2]. Statista also provides data on market
shares for 12 robotics industry segments (e.g. medical, logistics, domestic services, and
multiple industrial categories) [41, p. 10]. We calculated market values in each industry
segment by multiplying the shares by our market size estimate (USD 46.1 billion).
Table H13 presents the market share per segment as reported in Statista together
with the corresponding market values.
T able H13:Market share and corresponding market value by
robotic industry (2024).
Industry segment 2024 market share
(%)
2024 market value
(USD B)
Industrial
Automotive 7% 3.2
Electrical/Electronic 6% 2.8
Logistics 5% 2.3
Metal 2% 0.9
Chemical 2% 0.9
Food 1% 0.5
Other industrial 2% 0.9
Professional services
Medical 29% 13.2
Agriculture 3% 1.4
Other professional services* 9% 4.1
Consumer
Domestic 24% 11.2
Entertainment 10% 4.6
T otal 100% 46.0
*Other professional services robots include cleaning, inspection, construction, search &
rescue, and hospitality.
106

Step 2: Map IFR subclasses to robotics industry segments
In Table G12, we mapped the 66 IFR subclasses to activities in the ontology. Now, to
connect market sizes to ontology activities, we also needed to map the 66 IFR sub-
classes to the 11 industry segments. In some cases, IFR subclasses correspond directly
to industry segments (e.g., IFR’s four subclasses of medical robots all correspond to
the medical industry segment, and IFR’s subclasses in transportation and logistics
correspond to the logistics industry segment).
In other cases, however, there are no obvious correspondences between IFR sub-
classes and industry segments. In these cases, three of the authors of this paper,
with expertise in robotics, reviewed multiple external sources in order to make plau-
sible inferences about which IFR subclasses would be included in which industry
segments [Assumption 4]. For example, within the “automotive” industry segment,
we assigned the following IFR subclasses: arc welding, assembling, dispensing/spray-
ing, disassembling, machine tending, material handling, painting and enameling, spot
welding. Because published sources differ in how they categorize robot applications
within specific industries, we made subjective judgments about how best to reconcile
these differences. And these classifications should, therefore, be regarded as approx-
imations, not as definitive classification. In addition to the IFR report on industrial
robots [12], sources were consulted to help make these mappings for various industry
segments included: Electric/Electronic [59], Automotive [60], Metal [61], Food [62],
and Chemical [63] segments.
Step 3: Estimate the *relative* prices for each IFR subclass in each
industry
Since there is no obvious source of pricing information for different IFR subclasses,
we needed to use some form of expert estimates for these quantities. But, due to the
large variability in robotic systems, we believed it would be difficult or impossible,
even for experts, to directly estimate prices for each subclass in a way that would
also be mathematically consistent with both (a) the actual units sold in each subclass
and (b) the overall revenues in each industry segment. Therefore, we chose to start by
estimatingrelativeprices for each IFR subclass in an industry segment, and then, in
Step 4, to pick an adjustment factor to generate estimates of actual prices that were
simultaneously consistent with (a) the estimated relative prices, (b) the units sold per
subclass, and (c) the revenues in that industry segment.
To generate estimates of the relative prices, the same author of this paper who
served as an expert in Step 2, also created estimates ofrelativeaverage unit prices
in each industry segment[Assumption 5]. This was done by first compiling estimates
of high and low prices for each subclass, using publicly available sources, includ-
ing manufacturer disclosures, system integrator listings, and industry reports. When
sources reported differing price ranges, we adopted the widest reported range to avoid
understating potential price dispersion. For subclasses appearing in multiple industry
segments, we applied identical high and low price bounds across segments. Also, in
these cases, we divided the IFR-reported number of installations evenly between the
segments.
107

Then, for each subclass, we determined the midpoint between the estimated low
and high unit prices and treated this as an estimate of the average unit price. Finally,
for each industry segment, we rescaled the estimated prices to all berelativeto the
lowest price. In other words, the lowest price would now be 1, and the other prices
would be multiples of that lowest price. For example, if the lowest average price was
x, a subclass whose average price was twice as high (2x) received a relative price of 2.
This yielded a set of relative average unit prices for each subclass.
Step 4: Calculate an adjustment factor to make the estimated prices for
each IFR subclass mathematically consistent with the relative prices and
industry segment revenues
To calculate the adjustment factor, we first calculate the total segment revenue that
would be received if therelativeprices were used. Then we divide theactualsegment
revenue by that amount to get the adjustment factor[Assumption 6]. Mathematically,
this can be expressed as follows:
For a given industry segment, let
R= revenue in the segment
Ri = revenue in subclassiof the segment
n= number of subclasses in the segment
Ui = units sold in subclassiof the segment
Pi = average unit price in subclassiof the segment
P ′ i =relativeaverage unit price in subclassiof the segment
x= price adjustment factor for the segment,
where the relative prices are normalized such that the lowest relative price in the
segment satisfiesP ′ 1 = 1, and all otherP ′ i values are proportionally greater.
Then:
Pi =x∗P ′ i
Ri =P i ∗U i
=x∗P ′ i ∗U i
Total segment revenue is given by:
R=
nX
i=1
Ri
=
nX
i=1
(x∗P ′ i ∗U i)
108

=x∗
nX
i=1
(P ′ i ∗U i)
Solving for the price adjustment factor:
x= RPn
i=1 (P ′ i ∗U i)
Step 5: Calculate the estimated market value per subclass in each industry
Once the adjustment factor is known, the estimated market value for each subclass
can be calculated by multiplying the relative prices by the adjustment factor to get
actual prices and then multiplying the actual prices by units to get revenue (which is
equivalent to market value) in each subclass.
Using the mathematical notation from above, this is equivalent to calculating:
Ri =x∗P ′ i ∗U i
Table H14 shows an example of this estimation process for the medical robots
segment. This segment accounted for 29% of global robotics revenue in 2024, which
corresponded to approximately USD 13.2 billion. The medical segment has four sub-
classes: (i) diagnostics and laboratory analysis, (ii) surgical, (iii) rehabilitation and
non-invasive therapy, and (iv) other. After researching price ranges and completing
the calculations, our analysis showed that surgical robots accounted for nearly 12 bil-
lion USD, more than 90% of the 13.2 billion USD medical robots segment, while the
other three medical subclasses each account for less than 1 billion USD.
109

T able H14:Estimated Market V alue of Medical Robotics
Subclasses (2024).
The Medical Robotics industry represents 29% of the global robotics market
value (13.2bn USD). Average prices for each subclass are initially estimated
as the midpoint of the reported price ranges and then converted to relative
prices. The relative prices are multiplied by the price adjustment factor
(x= 110.1) to obtain adjusted price estimates. Then, the adjusted price
estimates are multiplied by the number of units to calculate the market
value of each subclass.
Subclass Units Price
range
(USD)
Initial
estimate
of avg
price
(USD)
Relative
avg
price
(ratio)
Adjusted
avg
price
(USD)
Market
value
(USD)
Diagnostics/
Lab analysis
3,293 100k–150k 125k 1.3 145k 0.5 bn
Surgical 6,612 600k–2,500k 1550k 16.4 1,800k 11.9 bn
Rehab/
non-invasive
therapy
5,759 69k–120k 94.5k 1.0 110k 0.6 bn
Other 995 100k–150k 125k 1.3 145k 0.2 bn
T otal
(USD)
13.2bn
110

Appendix I Results from market value analysis
I.1 Results on market value of AI applications
Figure I25 presents a sunburst visualization of the global AI application market value
projected onto our activity ontology. Among the three major categories of activities,
“Act on information (‘Think’)” accounts for the largest share of revenue, covering
approximately 92% of the total. This is roughly twice the share of “Act on activities or
actors (‘Interact’)”, which accounts for about 45%. Owing to the ontology’s multiple-
inheritance structure, these percentages are not mutually exclusive. In particular,
the activity “Transfer information”, which is shared by both categories, represents
approximately 32% of the total AI application revenue.
Act: 100%
Act on information
(“Think”): 92%
Act with other activities and actors (“Interact”): 45% Act on physical objects (“Do”): 0%
Create
information: 48%
Modify
information: 15%
Transfer
information: 32%
Storeinformation: 0.007%
Transfer between
actors: 43%
Act onactivities: 8%
Modify physicalobjects: 0%
Create physicalobjects: 0%
Store physical
objects: 0%
Transfer physical
objects: 0%
Plan: 3%
Analyze: 8%
Decide: 0.6% Calculate: 0.1% Express information: 13% Assemble information: 3% Reason: 0.5% Create information -- other: 19% Solve: 0.3%
Transform information: 12% Com bine inform
ation: 1%
Separate information: 1% Move information: 0.001%Exchange information: 6%
Get information: 6%Provide information: 15% Communicate (transfer information end-to-end): 4% Store information -- other: 0.007% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 0.3%
Buy: 0.2%
Distribute: 0%
Sell: 0.1%
Give: 0.003%
Take: 0%
Transfer information: 32%
Transfer service: 11%
Transfer physical objects: 0%
Interact: 0%
Open (make available): 0%
Receive: 0.0007%
Return: 0%
Trade (Transfer both ways): 0.03%
Communicate (transfer information end-to-end): 4%
Earn: 0% Lend: 0% Pass (over): 0.02% Raise (funds): 0.02% W ithhold: 0%
Perform
 (action): 2%
Improve: 6%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0.2% Pass (achieve): 0% Undertake: 0% Transform physical objects: 0%
Separate physical objects: 0%
Combine physical objects: 0%
Move physical objects: 0%
Assemble: 0%
Fabricate: 0%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 0%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 1%
Outline: 0%
Plan -- other: 2%
Propose: 0.4%
 Schedule: 0.07%
Stage: 0%
 Analyze -- other: 4%
Characterize: 0%
 Correlate: 0%
 Determine: 2%
 Experiment: 0%
 Investigate: 2%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0.08%
 Reject: 0%
 Rule: 0%
 Select: 0.5%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0.06%
 Count: 0.0004%
 Estimate: 0.08%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0.1%
 Record: 12%
Assemble information -- other: 0.001%
 Configure (information): 0.2%
 Construct (information): 3%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0.002%
 Organize (analytically): 0.4%
 Reason -- other: 0.06%
 Create (Activity): 0.5%
 Create (Actor): 0%
Create (Information): 19%
 Address (solve): 0%
 Resolve: 0.1%
Solve -- other: 0.2%
Adjust (information): 0.5%
 Change Appearance: 0%
 Clean (inform
ation): 0.001%
 Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0.01%
Finish (inform
ation): 0%
Im
prove: 6%
Organize (analytically): 0.4%
 Perm
ute: 0%
Prepare (inform
ation): 0.2%
Process (inform
ation): 2%
Renew (inform
ation): 0%
Revise: 2%
 Service (inform
ation): 0.2%
Switch: 0%
 Transform
 inform
ation -- other: 0.1%
Translate: 0.6%
 Use: 0.1%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0.02%
Gather (inform
ation): 1%
Incorporate (inform
ation): 0.05%
Pack (together) (information): 0%
 Synthesize (information): 0.02%
 Break (into components): 0%
 Cut (information): 1%
 Disconnect (information): 0%
 Remove (information): 0.0006%
 Separate information -- other: 0.04%
 Move information -- other: 0%
 Put information: 0.001%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 3e-05%
 Converse: 3%
 Correspond: 0%
 Debate: 0.004%
 Exchange information -- other: 0.005%
 Interview: 1%
 Mediate: 0%
 Meet: 0.001%
 Negotiate: 0.002%
 Network: 0.05%
 Reach: 0.02%
 Teach: 2%
 Access: 0.1%
 Download: 5e-05%
 Evaluate: 3%
 Gather (information): 1%
 Get information -- other: 0.02%
 Import: 0.002%
 Learn: 0.5%
 Perceive: 2%
 Understand: 0.03%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0.1%
 Provide decision: 0%
 Provide money: 0%
 Send information: 15%
Communicate (transfer information end-to-end) -- other: 0.6%
 Store (Activity): 0%
 Store (Actor): 0.007%
 Store (Information): 4e-05%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 0.3%
Ticket: 0%
Buy -- other: 0.01%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0.1%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0.1%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0.003%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 4%
Exchange information: 6%
Get information: 6%
Provide information: 15%
End service: 0%
Exchange service: 0.01%
Get service: 9%
Provide service: 2%
Exchange physical objects: 0%
Get physical objects: 0%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 0%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0.0007%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0.6%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0.02%
 Raise (funds) -- other: 0.02%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 2%
 Conduct: 0.2%
 M
ake: 0%
Perform
 (action) -- other: 0.3%
Practice: 0%
 Rehearse: 0.03%
 Run (perform
): 0%
Im
prove -- other: 2%
Optim
ize: 4%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0.1%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0%
Clean (physical): 0%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0%
 Process (physical): 0%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0%
 Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
 Cut (physical): 0%
 Disassemble: 0%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 0%
 Consolidate: 0%
 Cover: 0%
Enclose: 0%
Gather (physical): 0%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0%
Reorient physical objects: 0%
Transport physical objects: 0%
 Assemble -- other: 0%
Configure (physical): 0%
Construct (physical): 0%
 Copy (physical): 0%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 0%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 0%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0%
Fig. I25:The global market value distribution of AI software applications
in 2024.
111

Within “Act on information (‘Think’)”, the most dominant activity is “Create
information”, which alone accounts for 48% of total revenue. This concentration indi-
cates that nearly half of the AI application market is driven by systems designed to
generate new informational content, underscoring both the commercial success and rel-
ative maturity of generative AI technologies in current markets. Further decomposing
“Create information” reveals that “Create information – other” (19%), “Express infor-
mation” (13%), and “Transfer information” (12%) are the three largest contributing
activities.
An examination of representative applications associated with these activities sug-
gests that present-day AI revenue is primarily driven by products such as AI image
and video generation and editing tools, conversational AI systems, writing assistants,
and customer engagement platforms. These applications emphasize content creation,
expression, and communication, reflecting strong demand for AI systems that operate
directly on informational artifacts.
In contrast, activities that also inherit from “Create information”, including
“Decide”, “Plan”, and “Analyze”, account for comparatively little market value. This
imbalance suggests that, despite significant research progress in reasoning, planning,
and analytical capabilities, these functions have not yet translated into widespread,
monetized AI applications at scale. Possible explanations include higher integration
costs, greater domain specificity, or the need for tighter coupling with organizational
workflows and decision-making authority.
Overall, projecting AI application market value onto our ontology reveals a highly
uneven distribution across activity types. A small number of content-centric activities
account for the vast majority of market value, while many other activities account for
minimal market value despite their potential importance. This imbalance highlights
substantial untapped opportunities for AI deployment, particularly in activities that
involve deeper reasoning, decision support, and complex task orchestration, areas that
may represent the next frontier for economically impactful AI systems.
I.2 Results on market value for robotic systems
Figure I26 presents the estimated market value of robotic applications at the subclass
level. In contrast to the distribution ofcountsof robot installations, where activi-
ties classified under “Do” and “Interact” account for approximately 79% and 22% of
deployed units, respectively, the corresponding distribution of themarket valuesis sub-
stantially more balanced. Specifically, activities within the “Do” domain account for
approximately 50% of total market value, while activities within the “Interact” domain
contribute approximately 57%, rendering these two domains broadly comparable in
economic terms.
A closer examination of the disaggregated data reveals a pronounced divergence
between deployment volume and market value across activity subclasses. For instance,
the “Clean” activity includes a very large number of deployed consumer robots
(approximately 20 million units); however, due to the relatively low unit cost of these
systems, it contributes only moderately to the total market revenue. By contrast,
interactive robotic applications, particularly in the medical domain, are deployed in
comparatively small numbers but generate disproportionately high revenue. This effect
112

Act: 100%
Act on information
(“Think”): 9%
Act with other activities and actors (“Interact”): 57% Act on physical objects (“Do”): 50%
Createinformation: 0%
Modify
information: 0%
Transfer
information: 9%
Storeinformation: 0%
Transfer between
actors: 34%
Act onactivities: 25%
Modify physicalobjects: 38%
Create physicalobjects: 6%
Store physical
objects: 0%
Transfer physical
objects: 7%
Plan: 0%
Analyze: 0%
Decide: 0%Calculate: 0% Express information: 0% Assemble information: 0% Reason: 0% Create information -- other: 0% Solve: 0%
Transform information: 0% Com bine inform
ation: 0%
Separate information: 0% Move information: 0%Exchange information: 7%
Get information: 3%Provide information: 0% Communicate (transfer information end-to-end): 0% Store information -- other: 0% File (information): 0% Back up: 0%Upload (information): 0%
Supply: 5%
Buy: 0%
Distribute: 0%
Sell: 0%
Give: 0%
Take: 0%
Transfer information: 9%
Transfer service: 11%
Transfer physical objects: 7%
Interact: 2%
Open (make available): 0%
Receive: 0%Return: 0%
Trade (Transfer both ways): 0%
Communicate (transfer information end-to-end): 0%
Earn: 0% Lend: 0% Pass (over): 0% Raise (funds): 0% W ithhold: 0%
Perform
 (action): 25%
Improve: 0%Achieve: 0% Adopt: 0% Complete (activity): 0%Continue: 0% Im plem ent: 0% Pass (achieve): 0% Undertake: 0% Transform physical objects: 20%
Separate physical objects: 0.1%
Combine physical objects: 13%
Move physical objects: 5%
Assemble: 2%
Fabricate: 4%
Create physical objects -- other: 0% Remake: 0%
File (physical): 0%
Preserve: 0%
Store physical objects -- other: 0%
Stow: 0%
Upload (physical): 0%
Get physical objects: 7%
Exchange physical objects: 0%Provide physical objects: 0%
Anticipate: 0%
Budget: 0%
Conceptualize: 0%
Design: 0%
Outline: 0%
Plan -- other: 0%
Propose: 0%
Schedule: 0%
Stage: 0%
 Analyze -- other: 0%
Characterize: 0%
 Correlate: 0%
 Determine: 0%
 Experiment: 0%
 Investigate: 0%
 Trace (analytically): 0%
 Accept: 0%
 Decide -- other: 0%
 Estimate: 0%
 Reject: 0%
 Rule: 0%
 Select: 0%
 Sentence: 0%
 Account for: 0%
Balance (account): 0%
 Calculate -- other: 0%
 Count: 0%
 Estimate: 0%
 Total: 0%
 Argue: 0%
 Conclude: 0%
 Emphasize: 0%
 Express Live: 0%
 Record: 0%
Assemble information -- other: 0%
 Configure (information): 0%
 Construct (information): 0%
 Reassemble (information): 0%
 Consider: 0%
Develop (idea): 0%
Organize (analytically): 0%
 Reason -- other: 0%
 Create (Activity): 0%
 Create (Actor): 0%
Create (Information): 0%
 Address (solve): 0%
 Resolve: 0%
Solve -- other: 0%
Adjust (information): 0%
 Change Appearance: 0%
 Clean (information): 0%
Decode: 0%
 Encode: 0%
 Equalize: 0%
Fill (inform
ation): 0%
Finish (inform
ation): 0%
Im
prove: 0%
Organize (analytically): 0%
 Perm
ute: 0%
Prepare (inform
ation): 0%
Process (inform
ation): 0%
Renew (inform
ation): 0%
Revise: 0%
 Service (inform
ation): 0%
Switch: 0%
 Transform
 inform
ation -- other: 0%
Translate: 0%
 Use: 0%
 Add (inform
ation): 0%
Com
bine inform
ation -- other: 0%
Connect (inform
ation): 0%
Gather (inform
ation): 0%
Incorporate (inform
ation): 0%
Pack (together) (information): 0%
 Synthesize (information): 0%
 Break (into components): 0%
 Cut (information): 0%
 Disconnect (information): 0%
 Remove (information): 0%
 Separate information -- other: 0%
 Move information -- other: 0%
 Put information: 0%
 Redirect: 0%
 Transport information: 0%
 Agree: 0%
 Confer: 0%
 Converse: 0%
 Correspond: 0%
 Debate: 0%
 Exchange information -- other: 0%
 Interview: 0%
 Mediate: 0%
 Meet: 0%
 Negotiate: 0%
 Network: 0%
 Reach: 0%
 Teach: 7%
 Access: 0%
 Download: 0%
 Evaluate: 0.8%
 Gather (information): 0%
 Get information -- other: 0%
 Import: 0%
 Learn: 0%
 Perceive: 2%
 Understand: 0%
 Appear: 0%
 Charge (money): 0%
 Express Live: 0%
 Provide decision: 0%
 Provide money: 0%
 Send information: 0%
 Communicate (transfer information end-to-end) -- other: 0%
 Store (Activity): 0%
 Store (Actor): 0%
 Store (Information): 0%
 Archive: 0%
File (information) -- other: 0%
Back up -- other: 0%
 Upload (information) -- other: 0%
 Equip: 0%
Make available: 0%
Match (co-fund): 0%
Redeem: 0%
Retrofit: 0%
Stock: 0%
Supply -- other: 5%
Ticket: 0%
Buy -- other: 0%
Buy information: 0%
Buy physical object: 0%
Buy service: 0%
Order (buy): 0%
Rent (pay for time-limited use): 0%
Assign: 0%
Circulate: 0%
Deal: 0%
Deploy: 0%
Distribute -- other: 0%
Rotate (cycle): 0%
Lease out: 0%
Rent out: 0%
Sell -- other: 0%
Sell Service: 0%
Sell information: 0%
Sell physical objects: 0%
Contribute: 0%
Give -- other: 0%
Grant: 0%
Sponsor: 0%
Turn In: 0%
Capture (catch): 0%
Impound: 0%
Recover: 0%
Seize: 0%
Take -- other: 0%
Communicate (transfer information end-to-end): 0%
Exchange information: 7%
Get information: 3%
Provide information: 0%
End service: 0%
Exchange service: 0%
Get service: 6%
Provide service: 5%
Exchange physical objects: 0%
Get physical objects: 7%
Provide physical objects: 0%
Befriend: 0%
Interact -- other: 2%
Open (make available) -- other: 0%
Reopen: 0%
 Admit (accept): 0%
 Receive -- other: 0%
 Refund: 0%
 Return -- other: 0%
Trade (Transfer both ways) -- other: 0%
Transact: 0%
Communicate (transfer information end-to-end) -- other: 0%
Earn -- other: 0%
 Lend -- other: 0%
 Pass (over) -- other: 0%
 Raise (funds) -- other: 0%
 W
ithhold -- other: 0%
Activate: 0%
 Automate: 0%
 Conduct: 2%
 M
ake: 0%
Perform
 (action) -- other: 23%
Practice: 0%
 Rehearse: 0%
 Run (perform
): 0%
Im
prove -- other: 0%
Optim
ize: 0%
Achieve -- other: 0%
Adopt -- other: 0%
 Com
plete (activity) -- other: 0%
Continue -- other: 0%
 Im
plem
ent -- other: 0%
Pass (achieve) -- other: 0%
Undertake -- other: 0%
 Adjust (physical): 0%
 Apply M
akeup: 0%
Change surface: 0.2%
 Clean (physical): 20%
 Cool: 0%
Dem
agnetize: 0%
Develop (chem
ically): 0%
 Dilute: 0%
Dress (clothes): 0%
 Dry: 0%
Fill (physical): 0%
 Heat: 0%
Immobilize: 0%
 Kill: 0%
Machine: 0%
Neutralize: 0%
Prepare (physical): 0%
Process (physical): 0.06%
 Raze: 0%
Redevelop: 0%
Refine (substance): 0%
 Renew (physical): 0%
 Service (physical): 0%
 Shape: 0.3%
Style: 0%
Tenderize: 0%
Transform physical objects -- other: 0%
 Wet: 0%
Break: 0%
Capture (collect): 0%
Cut (physical): 0.03%
Disassemble: 0.002%
Disconnect (physical): 0%
 Isolate: 0%
 Plow: 0%
Ravel: 0%
Remove (physical): 0%
 Scatter: 0.09%
Segregate: 0%
Separate physical objects -- other: 0%
 Sift: 0%
Terminate: 0%
 Unpack: 0%
Add (physical): 0%
Connect (physical): 4%
 Consolidate: 0%
 Cover: 0.5%
Enclose: 2%
Gather (physical): 7%
Incorporate (physical): 0%
Synthesize (physical): 0%
Move physical objects -- other: 0%
Move physical objects in other ways: 0%
Put physical objects: 0.5%
Reorient physical objects: 0%
Transport physical objects: 4%
 Assemble -- other: 1%
Configure (physical): 0%
Construct (physical): 0.07%
 Copy (physical): 0.6%
Reassemble (physical): 0%
 Cast: 0%
Fabricate -- other: 4%
Create (Physical Object): 0%
Remake -- other: 0%
File (physical) -- other: 0%
Preserve -- other: 0%
Store (Physical Object): 0%
Stow -- other: 0%
Upload (physical) -- other: 0%
Gather (physical): 7%
Get physical objects -- other: 0%
Salvage: 0%
Exchange physical objects -- other: 0%
Provide food: 0%
Fig. I26:Sunburst diagram showing the global market value of robotic
systems (industrial and service robots) for the year 2024.
is driven by the high capital cost of such systems, with prices for advanced medical
robots frequently exceeding USD 2 million per unit. These findings underscore the
importance of distinguishing between deployment scale and economic impact when
assessing the structure and dynamics of the robotics market.
I.3 Results on allocation of total market value to AI software
applications and robotic systems
Figure I27 shows the market value contributions of AI software applications and
robotic systems for each activity in the ontology for the year 2024. Values are
calculated using the methods described in previous sections of Appendix H.
113

Act: 75% Software, 25% Robotics
Act on information
(“Think”): 70% Software, 2% Robotics
Act with other activities and actors(“Interact”): 34% Software, 14% Robotics
Act on physical objects
(“Do”): 0% Software, 12% Robotics
Create
information: 36% Software, 0% Robotics Modify information: 11% Software, 0% Robotics Transfer information: 24% Software, 2% Robotics Store information: 0.005% Software, 0% Robotics
Transfer between
actors: 33% Software, 8% Robotics
Act onactivities: 6% Software, 6% Robotics
Modify physical
objects: 0% Software, 10% Robotics
Create physicalobjects: 0% Software, 2% Robotics
Store physical
objects: 0% Software, 0% Robotics
Transfer physical
objects: 0% Software, 2% Robotics
Plan: 3% Software, 0% Robotics
Analyze: 6% Software, 0% RoboticsDecide: 0.5% Software, 0% Robotics Calculate: 0.1% Software, 0% Robotics Express information: 9% Software, 0% Robotics Assemble information: 2% Software, 0% Robotics Reason: 0.3% Software, 0% Robotics Create information -- other: 15%  Software, 0%  Robotics Solve: 0.2%  Software, 0%  Robotics
Transform information: 9% Software, 0% RoboticsCom
bine inform
ation: 0.8%
 Software, 0%
 Robotics
Separate information: 1%
 Software, 0%
 Robotics
Move information: 0.001% Software, 0% RoboticsExchange information: 4% Software, 2% Robotics
Get information: 5% Software, 0.7% RoboticsProvide information: 11% Software, 0% Robotics Communicate (transfer information end-to-end): 3% Software, 0% Robotics Store information -- other: 0.005% Software, 0% Robotics File (information): 0% Software, 0% Robotics Back up: 0% Software, 0% Robotics Upload (information): 0% Software, 0% Robotics
Supply: 0.3% Software, 1% Robotics
Buy: 0.1% Software, 0% Robotics
Distribute: 0% Software, 0% Robotics
Sell: 0.1% Software, 0% Robotics
Give: 0.002% Software, 0% Robotics
Take: 0% Software, 0% Robotics
Transfer information: 24% Software, 2% Robotics
Transfer service: 8% Software, 3% Robotics
Transfer physical objects: 0% Software, 2% Robotics
Interact: 0% Software, 0.5% Robotics
Open (make available): 0% Software, 0% Robotics
Receive: 0.0006% Software, 0% Robotics
Return: 0% Software, 0% Robotics
Trade (Transfer both ways): 0.02% Software, 0% Robotics
Communicate (transfer information end-to-end): 3% Software, 0% Robotics
Earn: 0% Software, 0% Robotics Lend: 0% Software, 0% RoboticsPass (over): 0.02%  Software, 0%  Robotics Raise (funds): 0.02%  Software, 0%  Robotics W ithhold: 0%  Software, 0%  Robotics
Perform (action): 2% Software, 6% Robotics
Im
prove: 5%
 Software, 0%
 Robotics
Achieve: 0%
 Software, 0%
 Robotics
Adopt: 0%
 Software, 0%
 Robotics
Com
plete (activity): 0%
 Software, 0%
 Robotics
Continue: 0%
 Software, 0%
 Robotics
Implement: 0.1% Software, 0% RoboticsPass (achieve): 0%
 Software, 0%
 RoboticsUndertake: 0%
 Software, 0%
 Robotics Transform physical objects: 0% Software, 5% Robotics Separate physical objects: 0% Software, 0.03% Robotics
Combine physical objects: 0% Software, 3% Robotics
Move physical objects: 0% Software, 1% Robotics
Assemble: 0% Software, 0.5% Robotics
Fabricate: 0% Software, 1% Robotics
Create physical objects -- other: 0% Software, 0% Robotics
Remake: 0% Software, 0% Robotics
File (physical): 0% Software, 0% Robotics
Preserve: 0% Software, 0% Robotics
Store physical objects -- other: 0% Software, 0% Robotics
Stow: 0% Software, 0% Robotics
Upload (physical): 0% Software, 0% Robotics
Get physical objects: 0% Software, 2% Robotics
Exchange physical objects: 0% Software, 0% Robotics Provide physical objects: 0% Software, 0% Robotics
Anticipate: 0% Software, 0% Robotics
 Budget: 0% Software, 0% Robotics
Conceptualize: 0% Software, 0% Robotics
 Design: 0.8% Software, 0% Robotics
 Outline: 0% Software, 0% Robotics
Plan -- other: 1% Software, 0% Robotics
 Propose: 0.3% Software, 0% Robotics
Schedule: 0.05% Software, 0% Robotics
 Stage: 0% Software, 0% Robotics
 Analyze -- other: 3% Software, 0% Robotics
 Characterize: 0% Software, 0% Robotics
 Correlate: 0% Software, 0% Robotics
Determine: 1% Software, 0% Robotics
 Experiment: 0% Software, 0% Robotics
 Investigate: 1% Software, 0% Robotics
 Trace (analytically): 0% Software, 0% Robotics
 Accept: 0% Software, 0% Robotics
 Decide -- other: 0% Software, 0% Robotics
 Estimate: 0.06% Software, 0% Robotics
 Reject: 0% Software, 0% Robotics
 Rule: 0% Software, 0% Robotics
 Select: 0.4% Software, 0% Robotics
 Sentence: 0% Software, 0% Robotics
 Account for: 0% Software, 0% Robotics
 Balance (account): 0% Software, 0% Robotics
 Calculate -- other: 0.05% Software, 0% Robotics
 Count: 0.0003% Software, 0% Robotics
 Estimate: 0.06% Software, 0% Robotics
 Total: 0% Software, 0% Robotics
 Argue: 0% Software, 0% Robotics
 Conclude: 0% Software, 0% Robotics
 Emphasize: 0% Software, 0% Robotics
 Express Live: 0.1% Software, 0% Robotics
 Record: 9% Software, 0% Robotics
 Assemble information -- other: 0.001% Software, 0% Robotics
 Configure (information): 0.1% Software, 0% Robotics
 Construct (information): 2% Software, 0% Robotics
 Reassemble (information): 0% Software, 0% Robotics
 Consider: 0% Software, 0% Robotics
 Develop (idea): 0.002% Software, 0% Robotics
 Organize (analytically): 0.3% Software, 0% Robotics
 Reason -- other: 0.05%
 Software, 0%
 Robotics
Create (Activity): 0.3%
 Software, 0%
 Robotics
Create (Actor): 0%
 Software, 0%
 Robotics
Create (Information): 14%
 Software, 0%
 Robotics
Address (solve): 0%
 Software, 0%
 Robotics
Resolve: 0.09%
 Software, 0%
 Robotics
Solve -- other: 0.1%
 Software, 0%
 Robotics
Adjust (information): 0.4%
 Software, 0%
 Robotics
Change Appearance: 0%
 Software, 0%
 Robotics
Clean (inform
ation): 0.0009%
 Software, 0%
 Robotics
Decode: 0%
 Software, 0%
 Robotics
Encode: 0%
 Software, 0%
 Robotics
Equalize: 0% Software, 0% Robotics
Fill (inform
ation): 0.009%
 Software, 0%
 Robotics
Finish (inform
ation): 0%
 Software, 0%
 Robotics
Im
prove: 5%
 Software, 0%
 Robotics
Organize (analytically): 0.3%
 Software, 0%
 Robotics
Perm
ute: 0%
 Software, 0%
 Robotics
Prepare (inform
ation): 0.2%
 Software, 0%
 Robotics
Process (inform
ation): 1%
 Software, 0%
 Robotics
Renew (inform
ation): 0%
 Software, 0%
 Robotics
Revise: 2%
 Software, 0%
 Robotics
Service (inform
ation): 0.1%
 Software, 0%
 Robotics
Switch: 0%
 Software, 0%
 Robotics
Transform
 inform
ation -- other: 0.08%
 Software, 0%
 Robotics
Translate: 0.5%
 Software, 0%
 Robotics
Use: 0.08% Software, 0% Robotics
Add (inform
ation): 0%
 Software, 0%
 Robotics
Com
bine inform
ation -- other: 0%
 Software, 0%
 Robotics
Connect (inform
ation): 0.01%
 Software, 0%
 Robotics
Gather (inform
ation): 0.8%
 Software, 0%
 Robotics
Incorporate (inform
ation): 0.04%
 Software, 0%
 Robotics
Pack (together) (information): 0%
 Software, 0%
 Robotics
Synthesize (information): 0.02%
 Software, 0%
 Robotics
Break (into components): 0%
 Software, 0%
 Robotics
Cut (information): 1%
 Software, 0%
 Robotics
Disconnect (information): 0%
 Software, 0%
 Robotics
Remove (information): 0.0004%
 Software, 0%
 Robotics
Separate information -- other: 0.03%
 Software, 0%
 Robotics
Move information -- other: 0%
 Software, 0%
 Robotics
Put information: 0.001% Software, 0% Robotics
 Redirect: 0% Software, 0% Robotics
 Transport information: 0% Software, 0% Robotics
 Agree: 0% Software, 0% Robotics
 Confer: 2e-05% Software, 0% Robotics
 Converse: 2% Software, 0% Robotics
 Correspond: 0% Software, 0% Robotics
 Debate: 0.003% Software, 0% Robotics
 Exchange information -- other: 0.004% Software, 0% Robotics
Interview: 0.9% Software, 0% Robotics
 Mediate: 0% Software, 0% Robotics
 Meet: 0.001% Software, 0% Robotics
 Negotiate: 0.002% Software, 0% Robotics
 Network: 0.04% Software, 0% Robotics
 Reach: 0.02% Software, 0% Robotics
 Teach: 1% Software, 2% Robotics
 Access: 0.08% Software, 0% Robotics
 Download: 4e-05% Software, 0% Robotics
 Evaluate: 2% Software, 0.2% Robotics
 Gather (information): 0.8% Software, 0% Robotics
 Get information -- other: 0.01% Software, 0% Robotics
 Import: 0.001% Software, 0% Robotics
 Learn: 0.4% Software, 0% Robotics
 Perceive: 2% Software, 0.5% Robotics
 Understand: 0.02% Software, 0% Robotics
 Appear: 0% Software, 0% Robotics
 Charge (money): 0% Software, 0% Robotics
 Express Live: 0.1% Software, 0% Robotics
 Provide decision: 0% Software, 0% Robotics
 Provide money: 0% Software, 0% Robotics
 Send information: 11% Software, 0% Robotics
 Communicate (transfer information end-to-end) -- other: 0.5% Software, 0% Robotics
 Store (Activity): 0% Software, 0% Robotics
 Store (Actor): 0.005% Software, 0% Robotics
 Store (Information): 3e-05% Software, 0% Robotics
 Archive: 0% Software, 0% Robotics
 File (information) -- other: 0% Software, 0% Robotics
 Back up -- other: 0% Software, 0% Robotics
 Upload (information) -- other: 0% Software, 0% Robotics
 Equip: 0% Software, 0% Robotics
Make available: 0% Software, 0% Robotics
 Match (co-fund): 0% Software, 0% Robotics
 Redeem: 0% Software, 0% Robotics
Retrofit: 0% Software, 0% Robotics
Stock: 0% Software, 0% Robotics
Supply -- other: 0.3% Software, 1% Robotics
Ticket: 0% Software, 0% Robotics
Buy -- other: 0.01% Software, 0% Robotics
Buy information: 0% Software, 0% Robotics
Buy physical object: 0% Software, 0% Robotics
Buy service: 0% Software, 0% Robotics
Order (buy): 0% Software, 0% Robotics
Rent (pay for time-limited use): 0.1% Software, 0% Robotics
Assign: 0% Software, 0% Robotics
Circulate: 0% Software, 0% Robotics
Deal: 0% Software, 0% Robotics
Deploy: 0% Software, 0% Robotics
Distribute -- other: 0% Software, 0% Robotics
Rotate (cycle): 0% Software, 0% Robotics
Lease out: 0% Software, 0% Robotics
Rent out: 0% Software, 0% Robotics
Sell -- other: 0.09% Software, 0% Robotics
Sell Service: 0% Software, 0% Robotics
Sell information: 0% Software, 0% Robotics
Sell physical objects: 0% Software, 0% Robotics
Contribute: 0% Software, 0% Robotics
Give -- other: 0.002% Software, 0% Robotics
Grant: 0% Software, 0% Robotics
Sponsor: 0% Software, 0% Robotics
Turn In: 0% Software, 0% Robotics
Capture (catch): 0% Software, 0% Robotics
Impound: 0% Software, 0% Robotics
Recover: 0% Software, 0% Robotics
Seize: 0% Software, 0% Robotics
Take -- other: 0% Software, 0% Robotics
Communicate (transfer information end-to-end): 3% Software, 0% Robotics
Exchange information: 4% Software, 2% Robotics
Get information: 5% Software, 0.7% Robotics
Provide information: 11% Software, 0% Robotics
End service: 0% Software, 0% Robotics
Exchange service: 0.01% Software, 0% Robotics
Get service: 7% Software, 1% Robotics
Provide service: 1% Software, 1% Robotics
Exchange physical objects: 0% Software, 0% Robotics
Get physical objects: 0% Software, 2% Robotics
Provide physical objects: 0% Software, 0% Robotics
Befriend: 0% Software, 0% Robotics
Interact -- other: 0% Software, 0.5% Robotics
Open (make available) -- other: 0% Software, 0% Robotics
Reopen: 0% Software, 0% Robotics
Admit (accept): 0% Software, 0% Robotics
Receive -- other: 0.0006% Software, 0% Robotics
Refund: 0% Software, 0% Robotics
Return -- other: 0% Software, 0% Robotics
Trade (Transfer both ways) -- other: 0% Software, 0% Robotics
Transact: 0% Software, 0% Robotics
Communicate (transfer information end-to-end) -- other: 0.5% Software, 0% Robotics
Earn -- other: 0% Software, 0% Robotics
Lend -- other: 0%
 Software, 0%
 Robotics
Pass (over) -- other: 0.02%
 Software, 0%
 Robotics
Raise (funds) -- other: 0.02%
 Software, 0%
 Robotics
W
ithhold -- other: 0%
 Software, 0%
 Robotics
Activate: 0%
 Software, 0%
 Robotics
Automate: 1%
 Software, 0%
 Robotics
Conduct: 0.2%
 Software, 0.5%
 Robotics
M
ake: 0%
 Software, 0%
 Robotics
Perform
 (action) -- other: 0.2%
 Software, 6%
 Robotics
Practice: 0%
 Software, 0%
 Robotics
Rehearse: 0.02%
 Software, 0%
 Robotics
Run (perform
): 0%
 Software, 0%
 Robotics
Im
prove -- other: 1%
 Software, 0%
 Robotics
Optim
ize: 3%
 Software, 0%
 Robotics
Achieve -- other: 0%
 Software, 0%
 Robotics
Adopt -- other: 0%
 Software, 0%
 Robotics
Com
plete (activity) -- other: 0%
 Software, 0%
 Robotics
Continue -- other: 0%
 Software, 0%
 Robotics
Im
plem
ent -- other: 0.1%
 Software, 0%
 Robotics
Pass (achieve) -- other: 0%
 Software, 0%
 Robotics
 Undertake -- other: 0%
 Software, 0%
 Robotics
Adjust (physical): 0%
 Software, 0%
 Robotics
Apply M
akeup: 0%
 Software, 0%
 Robotics
Change surface: 0%
 Software, 0.06%
 Robotics
Clean (physical): 0%
 Software, 5%
 Robotics
Cool: 0%
 Software, 0%
 Robotics
Dem
agnetize: 0%
 Software, 0%
 Robotics
Develop (chem
ically): 0%
 Software, 0%
 Robotics
Dilute: 0% Software, 0% Robotics
Dress (clothes): 0%
 Software, 0%
 Robotics
Dry: 0%
 Software, 0%
 Robotics
Fill (physical): 0%
 Software, 0%
 Robotics
Heat: 0%
 Software, 0%
 Robotics
Immobilize: 0%
 Software, 0%
 Robotics
Kill: 0%
 Software, 0%
 Robotics
Machine: 0%
 Software, 0%
 Robotics
Neutralize: 0%
 Software, 0%
 Robotics
Prepare (physical): 0%
 Software, 0%
 Robotics
Process (physical): 0%
 Software, 0.02%
 Robotics
Raze: 0% Software, 0% Robotics
 Redevelop: 0% Software, 0% Robotics
Refine (substance): 0% Software, 0% Robotics
Renew (physical): 0% Software, 0% Robotics
Service (physical): 0% Software, 0% Robotics
Shape: 0% Software, 0.07% Robotics
Style: 0% Software, 0% Robotics
Tenderize: 0% Software, 0% Robotics
Transform physical objects -- other: 0% Software, 0% Robotics
Wet: 0% Software, 0% Robotics
Break: 0% Software, 0% Robotics
Capture (collect): 0% Software, 0% Robotics
Cut (physical): 0% Software, 0.007% Robotics
Disassemble: 0% Software, 0.0004% Robotics
Disconnect (physical): 0% Software, 0% Robotics
Isolate: 0% Software, 0% Robotics
Plow: 0% Software, 0% Robotics
Ravel: 0% Software, 0% Robotics
Remove (physical): 0% Software, 0% Robotics
Scatter: 0% Software, 0.02% Robotics
Segregate: 0% Software, 0% Robotics
Separate physical objects -- other: 0% Software, 0% Robotics
Sift: 0% Software, 0% Robotics
Terminate: 0% Software, 0% Robotics
Unpack: 0% Software, 0% Robotics
Add (physical): 0% Software, 0% Robotics
Connect (physical): 0% Software, 0.9% Robotics
Consolidate: 0% Software, 0% Robotics
Cover: 0% Software, 0.1% Robotics
Enclose: 0% Software, 0.4% Robotics
Gather (physical): 0% Software, 2% Robotics
Incorporate (physical): 0% Software, 0% Robotics
Synthesize (physical): 0% Software, 0% Robotics
Move physical objects -- other: 0% Software, 0% Robotics
Move physical objects in other ways: 0% Software, 0% Robotics
Put physical objects: 0% Software, 0.1% Robotics
Reorient physical objects: 0% Software, 0% Robotics
Transport physical objects: 0% Software, 1% Robotics
Assemble -- other: 0% Software, 0.4% Robotics
Configure (physical): 0% Software, 0% Robotics
Construct (physical): 0% Software, 0.02% Robotics
Copy (physical): 0% Software, 0.2% Robotics
Reassemble (physical): 0% Software, 0% Robotics
Cast: 0% Software, 0% Robotics
Fabricate -- other: 0% Software, 1% Robotics
Create (Physical Object): 0% Software, 0% Robotics
Remake -- other: 0% Software, 0% Robotics
File (physical) -- other: 0% Software, 0% Robotics
Preserve -- other: 0% Software, 0% Robotics
Store (Physical Object): 0% Software, 0% Robotics
Stow -- other: 0% Software, 0% Robotics
Upload (physical) -- other: 0% Software, 0% Robotics
Gather (physical): 0% Software, 2% Robotics
Get physical objects -- other: 0% Software, 0% Robotics
Salvage: 0% Software, 0% Robotics
Exchange physical objects -- other: 0% Software, 0% Robotics
 Provide food: 0% Software, 0% Robotics
Fig. I27:Sunburst diagram showing the percentage contributions to market
value of AI software applications and robotic systems for each work activity
in 2024.Red shading indicates activities performed by AI software applications.
Blue shading indicates activities performed by robotic systems. And purple shading
indicates activities performed by a combination of both.
114

References
[1] Autor, D.H., Levy, F., Murnane, R.J.: The Skill Content of Recent Technological
Change: An Empirical Exploration. The Quarterly Journal of Economics118(4),
1279–1333 (2003) https://doi.org/10.1162/003355303322552801
[2] Autor, D.H.: The “task approach” to labor markets: an overview. Journal
for Labour Market Research46(3), 185–199 (2013) https://doi.org/10.1007/
s12651-013-0128-z
[3] Frey, C.B., Osborne, M.: The Future of Employment: How susceptible
are jobs to computerisation? https://www.oxfordmartin.ox.ac.uk/publications/
the-future-of-employment Accessed 2026-01-17
[4] Brynjolfsson, E., Mitchell, T., Rock, D.: What Can Machines Learn, and What
Does It Mean for Occupations and the Economy? AEA Papers and Proceedings
108, 43–47 (2018) https://doi.org/10.1257/pandp.20181019
[5] About O*NET at O*NET Resource Center. https://www.onetcenter.org/
overview.html Accessed 2026-01-17
[6] Gruber, T.R.: A translation approach to portable ontology specifications. Knowl-
edge Acquisition5(2), 199–220 (1993) https://doi.org/10.1006/knac.1993.1008
[7] Guarino, N.: Formal Ontology and Information Systems. In: Guarino, N. (ed.)
Formal Ontology in Information Systems: Proceedings of the 1st International
Conference on Formal Ontology in Information Systems (FOIS’98), pp. 3–15. IOS
Press, Trento, Italy (1998)
[8] Ontology (information science). Page Version ID: 1329509857 (2025).
https://en.wikipedia.org/w/index.php?title=Ontology (information science)
&oldid=1329509857#cite note-1 Accessed 2026-01-17
[9] Smith, B.: Ontology. In: Floridi, L. (ed.) Blackwell Guide to Philosophy of Com-
puting and Information. Blackwell Publishing, Oxford (2003). https://doi.org/
10.1111/b.9780631229193.2003.00014.x
[10] Nedelcu, A.: There’s An AI For That (2026). https://theresanaiforthat.com/
[11] M¨ uller, C., Jurkat, A., Kraus, W.G., Bregler, B., Kevin, B. (eds.): World Robotics
2025 – Service Robots. VDMA Services GmbH, Frankfurt am Main, Germany
(2025). Backup Publisher: IFR Statistical Department
[12] M¨ uller, C.: World Robotics 2025 – Industrial Robots. VDMA Services GmbH,
Frankfurt am Main, Germany (2025). Backup Publisher: IFR Statistical Depart-
ment
[13] Loaiza, I., Rigobon, R.: The EPOCH of AI: Human-Machine Complementarities
115

at Work. Social Science Research Network, Rochester, NY (2024). https://doi.
org/10.2139/ssrn.5028371 . https://papers.ssrn.com/abstract=5028371 Accessed
2026-03-19
[14] Friedman, T.L., Brink, B., Arthur, D.: Opinion|Tom Friedman’s A.I. Nightmare
and What the U.S. Can Do to Avoid It. The New York Times (2025). Chap.
Opinion. Accessed 2026-02-13
[15] Emsley, J.: The Periodic Table. In: Nature’s Building Blocks: An A–Z Guide To
the Elements, New edn., pp. 634–651. Oxford University Press, Oxford (2011)
[16] Malone, T.W., Crowston, K., Lee, J., Pentland, B., Dellarocas, C., Wyner, G.,
Quimby, J., Osborn, C.S., Bernstein, A., Herman, G., Klein, M., O’Donnell,
E.: Tools for Inventing Organizations: Toward a Handbook of Organizational
Processes. Management Science45(3), 425–443 (1999) https://doi.org/10.1287/
mnsc.45.3.425
[17] Hofweber, T.: Logic and Ontology. In: Zalta, E.N., Nodelman, U.
(eds.) The Stanford Encyclopedia of Philosophy, Summer 2023 edn.
Metaphysics Research Lab, Stanford University, Stanford, CA (2023).
https://plato.stanford.edu/archives/sum2023/entries/logic-ontology/
[18] Hogan, A., Blomqvist, E., Cochez, M., D’amato, C., Melo, G.D., Gutierrez, C.,
Kirrane, S., Gayo, J.E.L., Navigli, R., Neumaier, S., Ngomo, A.-C.N., Polleres, A.,
Rashid, S.M., Rula, A., Schmelzeisen, L., Sequeda, J., Staab, S., Zimmermann,
A.: Knowledge Graphs. ACM Comput. Surv.54(4) (2021) https://doi.org/10.
1145/3447772
[19] Gaudet, P., ˇSkunca, N., Hu, J.C., Dessimoz, C.: Primer on the Gene Ontology.
In: Dessimoz, C., ˇSkunca, N. (eds.) The Gene Ontology Handbook, pp. 25–37.
Springer, New York, NY (2017). https://doi.org/10.1007/978-1-4939-3743-1 3 .
https://doi.org/10.1007/978-1-4939-3743-1 3
[20] SNOMED CT|NCBO BioPortal. https://bioportal.bioontology.org/ontologies/
SNOMEDCT Accessed 2026-01-17
[21] Financial Industry Business Ontology (2023). https://www.3ds.com/products/
catia/no-magic/financial-industry-business-ontology Accessed 2026-01-17
[22] Mayr, E.: Principles of Systematic Zoology. McGraw-Hill, New York (1969)
[23] Wiley, E.O., Lieberman, B.S.: Phylogenetics: Theory and Practice of Phylo-
genetic Systematics. Wiley-Blackwell, Hoboken, NJ (2011). https://doi.org/10.
1002/9781118017883 .https://doi.org/10.1002/9781118017883
[24] Linnaeus, C.: Systema Naturae, 10 edn. Laurentii Salvii, Holmiae [Stockholm]
(1758)
116

[25] Miller, G.A.: WordNet: a lexical database for English. Commun. ACM38(11),
39–41 (1995) https://doi.org/10.1145/219717.219748
[26] Fellbaum, C.: WordNet: An Electronic Lexical Database. The MIT
Press, ??? (1998). https://doi.org/10.7551/mitpress/7287.001.0001 .
https://doi.org/10.7551/mitpress/7287.001.0001
[27] Princeton University: WordNet (2026). https://wordnet.princeton.edu/
[28] lexnames(5WN)|WordNet. https://wordnet.princeton.edu/documentation/
lexnames5wn Accessed 2026-03-16
[29] Fine, S.A., Wiley, W.W.: An Introduction to Functional Job Analysis. Tech-
nical Report Methods for Manpower Analysis No. 4, W. E. Upjohn Institute
for Employment Research, Kalamazoo, Michigan (September 1971). ERIC:
ED060221
[30] Gilardi, F., Alizadeh, M., Kubli, M.: ChatGPT outperforms crowd workers for
text-annotation tasks. Proceedings of the National Academy of Sciences120(30),
2305016120 (2023) https://doi.org/10.1073/pnas.2305016120
[31] Eloundou, T., Manning, S., Mishkin, P., Rock, D.: GPTs are GPTs: An
Early Look at the Labor Market Impact Potential of Large Language Mod-
els. arXiv. arXiv:2303.10130 [econ] (2023). https://doi.org/10.48550/arXiv.2303.
10130 . http://arxiv.org/abs/2303.10130
[32] Handa, K., Tamkin, A., McCain, M., Huang, S., Durmus, E., Heck, S., Mueller,
J., Hong, J., Ritchie, S., Belonax, T., Troy, K.K., Amodei, D., Kaplan, J., Clark,
J., Ganguli, D.: Which Economic Tasks are Performed with AI? Evidence from
Millions of Claude Conversations. eprint: 2503.04761 (2025). https://arxiv.org/
abs/2503.04761
[33] Tomlinson, K., Jaffe, S., Wang, W., Counts, S., Suri, S.: Working with AI: Mea-
suring the Applicability of Generative AI to Occupations. eprint: 2507.07935
(2025). https://arxiv.org/abs/2507.07935
[34] Robots and robotic devices — Vocabulary (2021). https://www.iso.org/standard/
75539.html
[35] McCain, M., Linthicum, R., Lubinski, C., Tamkin, A., Huang, S., Stern, M.,
Handa, K., Durmus, E., Neylon, T., Ritchie, S., Jagadish, K., Maheshwary,
P., Heck, S., Sanderford, A., Ganguli, D.: How People Use Claude for Sup-
port, Advice, and Companionship (2025). https://www.anthropic.com/news/
how-people-use-claude-for-support-advice-and-companionship
[36] Chatterji, A., Cunningham, T., Deming, D., Hitzig, Z., Ong, C., Shan, C.Y.,
Wadman, K.: How People Use ChatGPT. NBER Working Papers 34255, National
117

Bureau of Economic Research, Inc (2025). https://EconPapers.repec.org/RePEc:
nbr:nberwo:34255
[37] Patwardhan, T., Dias, R., Proehl, E., Kim, G., Wang, M., Watkins, O., Fishman,
S.P., Aljubeh, M., Thacker, P., Fauconnet, L., Kim, N.S., Chao, P., Miserendino,
S., Chabot, G., Li, D., Sharman, M., Barr, A., Glaese, A., Tworek, J.: GDPval:
Evaluating AI Model Performance on Real-World Economically Valuable Tasks.
arXiv. arXiv:2510.04374 [cs] version: 1 (2025). https://doi.org/10.48550/arXiv.
2510.04374 . http://arxiv.org/abs/2510.04374
[38] Braylan, A., Alonso, O., Lease, M.: Measuring Annotator Agreement Gen-
erally across Complex Structured, Multi-object, and Free-text Annotation
Tasks. In: Proceedings of the ACM Web Conference 2022, pp. 1720–
1730 (2022). https://doi.org/10.1145/3485447.3512242 . arXiv:2212.09503 [cs].
http://arxiv.org/abs/2212.09503
[39] Wu, Z., Palmer, M.: Verb Semantics and Lexical Selection. In: 32nd Annual
Meeting of the Association for Computational Linguistics, pp. 133–138. Asso-
ciation for Computational Linguistics, Las Cruces, New Mexico, USA (1994).
https://doi.org/10.3115/981732.981751 .https://aclanthology.org/P94-1019/
[40] He, J., Leng, Z., McKay, D., Spina, D., Trippas, J.R.: Can We Hide Machines
in the Crowd? Quantifying Equivalence in LLM-in-the-loop Annotation Tasks.
In: Proceedings of the 2025 Annual International ACM SIGIR Conference on
Research and Development in Information Retrieval in the Asia Pacific Region,
pp. 426–436 (2025). https://doi.org/10.1145/3767695.3769508 . arXiv:2510.06658
[cs].http://arxiv.org/abs/2510.06658
[41] Statista Market Insights: Robotics: Market Data & Analysis. Statista. Published:
Statista Market Insights (2024)
[42] Statista Market Insights: Artificial Intelligence: In-Depth Market Analysis.
Statista. Published: Statista Market Insights (2025)
[43] Dictionary of Occupational Titles - Fourth Edition, Revised 1991|U.S. Depart-
ment of Labor. https://www.dol.gov/agencies/oalj/topics/libraries/LIBDOT
Accessed 2026-01-17
[44] SkillsFuture Singapore|Homepage. https://www.skillsfuture.gov.sg/ Accessed
2026-01-17
[45] What is ESCO? https://esco.ec.europa.eu/en/about-esco/what-esco Accessed
2026-01-17
[46] Acemoglu, D., Restrepo, P.: Robots and Jobs: Evidence from US Labor Mar-
kets. Working Paper 23285, National Bureau of Economic Research (March
2017). https://doi.org/10.3386/w23285 . Series: Working Paper Series. http:
118

//www.nber.org/papers/w23285
[47] Lee, Y.S., Iizuka, T., Eggleston, K.: Robots and labor in nursing homes. Labour
Economics92, 102666 (2025) https://doi.org/10.1016/j.labeco.2024.102666
[48] Noy, S., Zhang, W.: Experimental evidence on the productivity effects of genera-
tive artificial intelligence. Science381(6654), 187–192 (2023) https://doi.org/10.
1126/science.adh2586
[49] Brynjolfsson, E., Li, D., Raymond, L.: Generative AI at Work. The Quar-
terly Journal of Economics140(2), 889–942 (2025) https://doi.org/10.1093/qje/
qjae044
[50] Cui, Z., Demirer, M., Jaffe, S., Musolff, L., Peng, S., Salz, T.: The Effects of
Generative AI on High-Skilled Work: Evidence from Three Field Experiments
with Software Developers. Working Paper 4945566, SSRN (2025). https://doi.
org/10.2139/ssrn.4945566 . https://ssrn.com/abstract=4945566
[51] Dell’Acqua, F., McFowland, E., Mollick, E.R., Lifshitz-Assaf, H., Kellogg, K.,
Rajendran, S., Krayer, L., Candelon, F., Lakhani, K.R.: Navigating the Jagged
Technological Frontier: Field Experimental Evidence of the Effects of AI on
Knowledge Worker Productivity and Quality. SSRN (2023) https://doi.org/10.
2139/ssrn.4573321
[52] Appel, R., McCrory, P., Tamkin, A., McCain, M., Neylon, T., Stern, M.:
Anthropic Economic Index report: Uneven geographic and enterprise AI adop-
tion. arXiv. arXiv:2511.15080 [econ] (2025). https://doi.org/10.48550/arXiv.
2511.15080 . http://arxiv.org/abs/2511.15080
[53] Baker, C.F., Fillmore, C.J., Lowe, J.B.: The Berkeley FrameNet Project. In: 36th
Annual Meeting of the Association for Computational Linguistics and 17th Inter-
national Conference on Computational Linguistics, Volume 1, pp. 86–90. Asso-
ciation for Computational Linguistics, Montreal, Quebec, Canada (1998). https:
//doi.org/10.3115/980845.980860 .https://aclanthology.org/P98-1013/Accessed
2026-03-16
[54] Niles, I., Pease, A.: Towards a standard upper ontology. In: Proceedings
of the International Conference on Formal Ontology in Information Sys-
tems - Volume 2001. FOIS ’01, pp. 2–9. Association for Computing Machin-
ery, New York, NY, USA (2001). https://doi.org/10.1145/505168.505170 .
https://doi.org/10.1145/505168.505170
[55] Malone, T.W., Crowston, K., Herman, G.A. (eds.): Organizing Business Knowl-
edge: The MIT Process Handbook. MIT Press, Cambridge, MA, USA (2003)
[56] Garc ´ ıa-Fern´ andez, J., Verhoosel, J., Ubacht, J., Bakker, R.: Ontology Engineering
119

with Large Language Models: Unveiling the potential of human-LLM collabo-
ration in the ontology extension process. CEUR Workshop Proceedings4020,
135–159 (2025)
[57] Schroeder, H., Roy, D., Kabbara, J.: Just Put a Human in the Loop? Investigat-
ing LLM-Assisted Annotation for Subjective Tasks. In: Che, W., Nabende, J.,
Shutova, E., Pilehvar, M.T. (eds.) Findings of the Association for Computational
Linguistics: ACL 2025, pp. 25771–25795. Association for Computational Linguis-
tics, Vienna, Austria (2025). https://doi.org/10.18653/v1/2025.findings-acl.1323
.https://aclanthology.org/2025.findings-acl.1323/
[58] Karpukhin, V., Oguz, B., Min, S., Lewis, P., Wu, L., Edunov, S., Chen, D., Yih,
W.-t.: Dense Passage Retrieval for Open-Domain Question Answering. In: Web-
ber, B., Cohn, T., He, Y., Liu, Y. (eds.) Proceedings of the 2020 Conference on
Empirical Methods in Natural Language Processing (EMNLP), pp. 6769–6781.
Association for Computational Linguistics, Online (2020). https://doi.org/10.
18653/v1/2020.emnlp-main.550 .https://aclanthology.org/2020.emnlp-main.550/
[59] Bogue, R.: The role of robots in the electronics industry. Industrial Robot: the
international journal of robotics research and application50, 717–721 (2023)
https://doi.org/10.1108/IR-04-2023-0082
[60] 6 Examples of Industrial Robots in the Automotive
Industry (2020). https://www.universal-robots.com/blog/
6-examples-of-industrial-robots-in-the-automotive-industry/ Accessed
2026-01-19
[61] Machinery & Metal Manufacturing|Industrial Robots by
Kawasaki Robotics. https://kawasakirobotics.com/uk/industries/
machinery-and-metal-manufacturing/ Accessed 2026-01-19
[62] Robots in the Food Industry - Robots Done Right. https://robotsdoneright.com/
Articles/robotics-in-the-food-industry.html Accessed 2026-02-20
[63] Chemistry|Plastics. https://www.yaskawa.co.uk/use-cases/industries/industry/
chemistry-plastics i183 Accessed 2026-01-19
120
