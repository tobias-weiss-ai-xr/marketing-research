---
title: I hope we don't do to trust what advertising has done to love
url: https://arxiv.org/abs/2604.28113
category: digital-marketing
subcategory: empirical
date: 2026-04
venue: ''
authors:
- Jade Alglave
source: arxiv
pdf_url: https://arxiv.org/pdf/2604.28113
pages: 7
chars: 22607
fetched_at: '2026-11-08T13:00:03+00:00'
kb_version: 1
---

# I hope we don't do to trust what advertising has done to love

I hope we don’t do to trust what advertising has done to love
JADE ALGLA VE,Arm and University College London, United Kingdom
Abstract:Advertising uses love to sell stuff, like nylons. It also uses the word “love” in trivialising ways—do you “love” your oven?
When I hear about trust in the context of AI, especially agentic, I hope we don’t do to trust what advertising has done to love.
But what is trust? Can we discuss it in actionable and measurable ways in the context of AI? Thus I suggest a number of “trust
pillars”, hoping to start a communal conversation, across computing and beyond, to civil society. I also suggest that agentic systems
may be a blessing in disguise, as we may be able to turn their explicit interfaces into “trust vectors”.
Keywords: Digital exclusion, agentic AI, architecture, trust, trustworthiness, user scenarios, love, grandparents
Draft:Jade Alglave. 2026. I hope we don’t do to trust what advertising has done to love. 1, 1 (May 2026), 7 pages.
My grandma is not tech-savvy: I worry about what technology looks like
and does to her; especially if AI, whether agentic or not, becomes a prevalent
way to interact with various services she depends on. How is she to trust
that it’s done what it was supposed to, and nothing else? Maybe you worry
about your folks in that way too. This column is for all of them.
1 AI is funny
AI applications may give absurd answers. These applications progress fast: the number of absurd answers may decrease.
But we still don’t really know why they behave how they do [23][10].
Yet the AI world marches forward, towards agentic systems: AI applications that don’t just chat back at you, but
can do stuff on your behalf. I hear a lot about this making the question of trust worse, so it got me thinking. What are
agentic systems? Might they be a blessing in disguise? What is “the question of trust”? What agentic systems are we
looking to trust? How can we architect such systems? Would this be enough for my grandma?
2 What are agentic systems?
In first approximation, a system is agentic if an LLM can influence what it does next. More concretely, I mean a system
as in Figure 1: there, the “Reasoning” box at least, and perhaps others, may often be an LLM. But you can see that we
are now examining not just a single black-box LLM but a whole system around it.
Back to my grandma, say she needs to renew her passport via an AI interface and part way through the doorbell
rings: Gateway interfaces through her phone, Routing chooses the next stage, Context Management gathers relevant
material, e.g. a snapshot of her old passport, Orchestrator coordinates, plans, delegates, Reasoning proposes next steps,
Perception notices the doorbell, Retrieval fetches external material e.g. guidance on what picture is acceptable, Memory
stores and recalls state, e.g. where she was before answering the door, Tools provide external capabilities e.g. her phone
camera, Executors carry out tasks e.g. filling in the form, and Actuation causes effects, finally filing her application.
Let’s distinguish model execution and surrounding system execution. The model produces e.g. a tool selection,
a ranking, a plan; the surrounding system uses the model, accesses memory, manages the context, calls the tool.
Components in the agentic architecture may not need to run sequentially, but a good understanding of what can run
Author’s Contact Information: Jade Alglave, Arm and University College London, United Kingdom, jade.alglave@arm.com, j.alglave@ucl.ac.uk.
2026.
Draft 1
arXiv:2604.28113v2  [cs.CY]  12 May 2026

2 Jade Alglave
Fig. 1. Basic agentic architecture and Examples of trust-related questions
concurrently is not apparent. Components don’t need to all be located in the same place, or be static: Executors may be
elsewhere than a local Orchestrator, some amount of Retrieval, Context Management, or Reasoning may be remote, etc.
3 Might agentic systems be a blessing in disguise?
Thus agentic systems may alter visibility, control flow, authority unduly. But the shift to an agentic architecture is an
opportunity; we can ask: what is visible? Is that intentional? What needs checking ahead of effects? What is relevant,
can or must be framed off or forgotten? Is someone accountable for the effects? Can they intervene? Can my grandma
request redress?... I give a few more questions in Figure 1.
If architected well, agentic systems may be more trustworthy than a black-box LLM, as they expose interfaces.
We could e.g.: intentionally restrict visibility before retrieval; soundly, e.g. programmatically or symbolically, reduce
context; carry sources and credentials throughout execution; delineate and enforce delegation limits; run checks before
taking action. Trust might then be less about the LLM alone and more about the architecture of the end-to-end system.
As an aside, and acknowledging Richard Sutton’s “Bitter Lesson” [19], I wonder: could we do more “on the cheap”?
Can we reproduce, or get close enough to [11], results obtained with LLMs, with maybe small, maybe domain-specific,
maybe open, models wrapped in carefully crafted agentic frameworks? See e.g. [4][8].
Might cheap, small, domain-specific or open models be easier both to check and keep in check? Frontier LLMs may
require Fort Knox, whilst other models might remain politely within a small hotel safe. Safety-critical systems may
prefer simpler and better understood architectures over maximal capability: historically, avionics has been cautious
about adopting complex systems such as multiprocessors and set up safety nets and checks around them.
Overall, we need to understand and document what LLMs can and cannot do with purposeful, ambitious, rigorous,
reproducible and open studies: how do they fare on termination [18]? Can they find concurrent invariants in Linux?...
And whilst for commercial reasons, implementation transparency may be unavailable, can we provide extensional
definitions? Arm has demonstrated the technical and commercial feasibility of devising, maintaining and publicly
distributing a behavioural envelope for systems as complex as multiprocessors, without revealing, or indeed prescribing,
any implementation insight [2]. Might this be achievable for LLMs?
Draft

I hope we don’t do to trust what advertising has done to love 3
What architecture is needed to sustain these “close enough” agentic frameworks reliably? What compute component
resides where, presumably in a concurrent, distributed, layered, dynamic fashion across e.g. personal devices and remote
locations? Where do verification components reside? Can we make sure they’re not neglected in favour of performance?
4 What is “the question of trust”?
I found this definition: “Trust is a willingness to open oneself to risk by engaging in a relationship with another
party” [9]. Trust is not in our control, but granted by the user: we must have user scenarios in any trust-related proposal.
My grandma needing to renew her passport is one, but we need more. A personal agent buys a plane ticket: will it
drain your savings? A decision procedure for recruitment, automatically ranking candidates: will it follow policies,
avoid bias [21]? An AI tutor for children, supporting homework: will it follow the curriculum? Facial recognition to
curb shoplifting: will it systematically flag the same demographics?. . .
We can at least try to offer users justification for relying on a system: a “trustworthy entity is one for which
sufficient evidence exists to support its claimed trustworthiness” [14]. This justification depends on context—country,
culture. . . [20]—e.g AI-aided farming can’t be one-size-fits-all when landscapes differ between Marfa and Osaka.
The trust “pillars” in Figure 2 attempt to make potential elements of justification explicit.
Fig. 2. Trust pillars
For my grandma’s passport, Suitability means e.g. that her application reaches the passport office when uploaded,
and nobody else; Provenance: she can demonstrate that she is the one who applied; Checkability: her application can
be checked w.r.t. official requirements; Relevance: only the necessary identity facts and images are in frame, nothing
more; Accountability: the passport office owns the process and intervention path; Delegation limits: no silent widening
into unrelated data collection or submission authority; Legibility: the renewal state, e.g. requirements and next steps,
are intelligible to users; Contestability: there exists a practically feasible route to challenge rejection or misprocessing;
Redress: there exists a practically feasible path to seek correction to processing error, or submission failure; Survivability:
under uncertainty or system failure, we fall back safely to manual handling.
There may be more pillars: I am not trying to argue that these are the only ones, but I have tried for them not to be
redundant. There may be fewer pillars; arguably, we could join some pillars into more abstract ones —see e.g. [13]. But I
felt we needed relatively concrete pillars, hoping for them to be actionable, perhaps even measurable, e.g. in engineering
Draft

4 Jade Alglave
and civil society: not all pillars can be addressed at a technical level, or not solely. Redress for example needs legal and
regulatory support, Accountability needs organisational support. Even within computing, this cannot be the prerogative
of certain groups, e.g. formal, safety or security folks, or be addressed by one single company’s solutions.
Tradeoffs between pillars may be envisageable in certain scenarios, and each pillar needs discussing. For example, the
Checkability pillar mentions “clearly designated sources”: if the system is deployed by, e.g. the NHS or the CDC, they
should clearly indicate what the reference sources are. For a personal agent, users need the freedom to designate sources.
I think it would be unwise, indeed likely at odds with trustworthiness, to impose
“sources of truth”. Rather the system needs to demonstrably preserve prove-
nance for reference material, and accept and demonstrate compliance with user
feedback w.r.t. more or less preferred sources. A source may or may not coincide
with fact; it may be poetry.
5 What agentic systems are we looking to trust?
How much freedom to expand their remit may these systems have? I found it useful to define two levels: bounded
agentic systems, and governable adaptive agentic systems. In practice, both levels may be distributed across device,
edge, cloud, and boundedness and governability must hold across execution landscapes.
Bounded agentic systemsmay plan, delegate, and act, but only inside fixed bounds, e.g. visibility scope, tools, actuation,
and stop conditions are bounded in advance. Delegation limits prevent silently widening permissions transitively, across
handoffs. Role adaptation is not allowed: executors remain bounded executors; they do not alter the visibility scope, call
new tools, become new orchestrators, or open new workflows outside the fixed bounds.
This is hard today as LLMs can disregard their instructions, and the distinction between actual content and instructions
does not seem apparent. So we may need, amongst other things, better prompt machinery (e.g. controlled English,
formal semantics, clear and enforceable separation of content vs instructions, Event-B, user-defined policies. . . ).
Governable adaptive agentic systemsgeneralise the bounded case: they may adapt beyond fixed bounds, to delegation
limits given by explicit governance rules (e.g. a declarative description of the envelope of legitimate behaviours, or
invariants): visibility scope, tools, actuation, and stop conditions are not bounded in advance. Role adaptation is allowed:
an executor may become a sub-orchestrator in a wider execution graph, but that adaptation must stay within the
envelope of behaviours given by the governance rules, with explicit delegation rather than silent widening.
The trust pillars must be preserved throughout adaptationand must remain effective and inspectable: suitability,
provenance, checkability, relevance, accountability, delegation limits, legibility, contestability, redress and survivability.
6 How can we architect such systems?
Suitability and Delegation limits may be helped by existing mechanisms e.g. iden-
tity and access management, sandboxing, attestations, protected storage, logging,
network controls, certification, computer architecture foundations [3]. . . C2PA’s
content credentials [7] may help with Provenance. Legibility may be helped
by using LLMs to turn complete, formal specifications into more palatable yet
sound documents, targetted at different audiences—e.g. implementers, users,
regulators, policy-makers—each level of documentation soundly abstracting the original one, nested like matriochkas. I
am certain there’s much more: a few suggestions appear in Figure 3.
Draft

I hope we don’t do to trust what advertising has done to love 5
Fig. 3. A few suggestions
I found inspiration for these whilst reflecting on what trust might mean for users like my grandma in the context of
agentic AI, imagining what mechanisms might help meet the trust pillars. To let us imagine further, here are a few
papers that have resonated with me:
• Adabara et al [1] review agentic AI across “architectural paradigms, threat taxonomies, and governance strategies”.
They emphasise the need for “interdisciplinary collaboration” and “cooperative innovation”.
• Chavali, Johnson and Denning [5] examine regulations across “the European Union, the United States, China,
India, and Canada”, and propose a “Geneva Convention for AI” to “co-create AI systems that adhere to ethical
principles like transparency, accountability, and professional oversight to promote societal well-being”.
• Engin and Hand [6] propose a governance framework for AI oversight, following three dimensions: authority,
autonomy, and accountability. The framework aims to support “the development of adaptive regulations that can
evolve alongside advancing AI capabilities without compromising safety or accountability. ”
• Osmond and Jego [ 12] survey “how public bodies, international organisations, national regulators, and the
private sector define agentic artificial intelligence”, suggesting “persistent definitional gaps”.
• Shapira et al [15] deployed agents over2weeks, and observed “unauthorized compliance with non-owners”,
“disclosure of sensitive information”, “uncontrolled resource consumption”, “identity spoofing”, “cross-agent
propagation of unsafe practices”, raising questions of e.g. accountability and delegated authority.
• Shavit et al [16] examine which parties are involved in an agentic AI system lifecycle, and suggest best practices
for each of these parties for keeping agents’ operations safe and accountable. They list open questions on how to
implement these practices, and categories of impact from agentic systems.
• Shen et al [17] assess two public sector procurement checklists to identify innovation directions for creating
“regulatable” AI systems. They indicate that “new methods are needed to connect data quality and objective
functions to outcomes, to identify what is possible with limited data and model access, to monitor continuously
learning agents, to balance transparency and privacy, and to enhance effective human+AI interaction. ”
• Wischnewski, Krämer and Müller [22] state that “to achieve appropriate reliance, users’ trust should be calibrated
to reflect a system’s capabilities. ”, and review the literature across “calibration” dimensions: “initial versus
dynamic”, “warranted versus unwarranted”, “static versus adaptive”, and “capabilities versus process-oriented”.
Draft

6 Jade Alglave
7 Would this be enough for my grandma?
Trust is granted by the user. Therefore all we can do is try to give the user justifications for relying on the system. These
justifications will depend on the user’s context, background, preferences, and beliefs, but I have tried to list a number of
justification elements, or trust pillars, which might be just about concrete enough to be actionable or measurable.
We need to understand our capability of control, or lack thereof, at various adaptiveness levels: controlling bounded
systems already seems hard with state-of-the-art technology, and governable adaptive systems seem harder still. Agentic
systems likely need to evolve from prompt-only control, towards additional enforceable architectural controls.
What may the system see or do? How much can it delegate, or adapt? What is checked before action? Who is
answerable? Can the user challenge, correct, or stop the system? If such questions remain implicit, my grandma should
not trust the system. If they are explicit, addressed by deliberate architecture, perhaps trust becomes possible.
Acknowledgements.The opinions expressed in this column are my own and not necessarily those of my employers.
Conversations with Eric Biscondi, Sylvan Clebsch, Hugo Ferreira, Hrutvik Kanabar, Yuxi Liu, Nikos Nikoleris, Peter
O’Hearn, Matthew Parkinson, Thomas Speier and Jules Villard helped me gather my thoughts. Patrick Cousot inspired
me to look at Event-B and reviewed various drafts. Richard Grisenthwaite too gave me helpful reviews, and suggested
the image of Fort Knox vs hotel safe. Rachel Coldicutt pointed me to the O’Neill reference, and discussed cultural
aspects of AI-assisted farming. Daryl Stewart drew the “Oma” and “Opa” love hearts, the “Abstraction Matriochkas”,
and the “Granny thinks of poetry” picture, whilst giving me meaningful feedback.
Finally, the East London Massive & Co. lost a dear friend and mentor earlier this year, Richard Bornat. I would have
loved (truly) to hear his thoughts on this column; but this was not to be.
References
[1] Ibrahim Adabara, Bashir Olaniyi Sadiq, Aliyu Nuhu Shuaibu, Yale Ibrahim Danjuma, and Venkateswarlu Maninti. Trustworthy agentic AI systems: a
cross-layer review. 2025. https://f1000research.com/articles/14-905.
[2] Arm. Arm Architecture Reference Manual for A-Profile Architecture. https://developer.arm.com/documentation/ddi0487/mb/?lang=en.
[3] Arm. Confidential Compute Architecture. 2026. https://www.arm.com/architecture/security-features/arm-confidential-compute-architecture.
[4] Peter Belcak, Greg Heinrich, Shizhe Diao, Yonggan Fu, Xin Dong, Saurav Muralidharan, Yingyan Celine Lin, and Pavlo Molchanov. Small Language
Models are the Future of Agentic AI. 2025. https://arxiv.org/abs/2506.02153.
[5] Durga P. Chavali, Jeffrey Johnson, and Peter Denning. Redefining Reality: Why the World Must Co-create for an Ethical AI Future. 2026.
https://dl.acm.org/doi/10.1145/3807969.
[6] Zeynep Engin and David Hand. Toward adaptive categories: dimensional governance for agentic AI. 2025. https://arxiv.org/abs/2505.11579.
[7] Coalition for Content Provenance and Authenticity. C2PA Specifications. 2026. https://spec.c2pa.org/specifications/specifications/2.2/index.html.
[8] Stanislav Fort. AI Cybersecurity After Mythos: The Jagged Frontier. 2026. https://aisle.com/blog/ai-cybersecurity-after-mythos-the-jagged-frontier.
[9] Linda Childers Hon and James E. Grunig. Guidelines for measuring relationships in public relations. 1999. https://instituteforpr.org/wp-
content/uploads/Guidelines_Measuring_Relationships.pdf.
[10] Ethan Mollick. On Working With Wizards. 2026. https://www.oneusefulthing.org/p/on-working-with-wizards.
[11] Andrew Odlyzko. Cybersecurity Is Not Very Important. 2019. https://dl.acm.org/doi/10.1145/3333611.
[12] Marcel Osmond and Thomas Jego. Mind The Gap: How The Technical Mechanism Of Agentic AI Outpace Global Legal Frameworks. 2026.
https://arxiv.org/abs/2603.27075.
[13] Onora O’Neill and James Bardrick. Trust, Trustworthiness And Transparency. 2017. https://www.thebritishacademy.ac.uk/documents/2563/Future-
of-the-corporation-Trust-trustworthiness-transparency.pdf.
[14] Ron Ross, Mark Winstead, and Michael McEvilley. Engineering Trustworthy Secure Systems. NIST SP 800-160. Volume 1 Revision 1. 2022.
https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-160v1r1.pdf.
[15] Natalie Shapira, Chris Wendler, Avery Yen, Gabriele Sarti, Koyena Pal, Olivia Floody, Adam Belfki, Alex Loftus, Aditya Ratan Jannali, Nikhil Prakash,
Jasmine Cui, Giordano Rogers, Jannik Brinkmann, Can Rager, Amir Zur, Michael Ripa, Aruna Sankaranarayanan, David Atkinson, Rohit Gandikota,
Jaden Fiotto-Kaufman, EunJeong Hwang, Hadas Orgad, P Sam Sahil, Negev Taglicht, Tomer Shabtay, Atai Ambus, Nitay Alon, Shiri Oron, Ayelet
Gordon-Tapiero, Yotam Kaplan, Vered Shwartz, Tamar Rott Shaham, Christoph Riedl, Reuth Mirsky, Maarten Sap, David Manheim, Tomer Ullman,
and David Bau. Agents of chaos. 2026. https://agentsofchaos.baulab.info/.
Draft

I hope we don’t do to trust what advertising has done to love 7
[16] Yonadav Shavit, Sandhini Agarwal, Miles Brundage, Steven Adler, Cullen O’Keefe, Rosie Campbell, Teddy Lee, Pamela Mishkin, Tyna Eloundou,
Alan Hickey, Katarina Slama, Lama Ahmad, Paul McMillan, Alex Beutel, Alexandre Passos, and David G. Robinson. Practices for governing agentic
AI systems. 2023. https://openai.com/index/practices-for-governing-agentic-ai-systems.
[17] Xudong Shen, Hannah Brown, Jiashu Tao, Martin Strobel, Yao Tong, Akshay Narayan, Harold Soh, and Finale Doshi-Velez. Directions of technical
innovation for regulatable AI systems. 2024. https://cacm.acm.org/research/directions-of-technical-innovation-for-regulatable-ai-systems/.
[18] Oren Sultan, Jordi Armengol-Estape, Pascal Kesseli, Julien Vanegue, Dafna Shahaf, Yossi Adi, and Peter O’Hearn. Large language models can solve
some instances of the halting problem. 2026. https://arxiv.org/abs/2601.18987.
[19] Richard Sutton. The Bitter Lesson. 2019. http://www.incompleteideas.net/IncIdeas/BitterLesson.html.
[20] University of Melbourne and KPMG International. Trust in AI: global study on sentiments and attitudes towards AI. 2025. https://mbs.edu/-
/media/PDF/Research/Trust_in_AI_Report.pdf?rev=0ee82285b2b0439bba524dbddc58214a.
[21] Caterina Urban, Maria Christakis, Valentin Wüstholz, and Fuyuan Zhang. Perfectly Parallel Fairness Certification of Neural Networks. 2020.
https://inria.hal.science/hal-03091870.
[22] Magdalena Wischnewski, Nicole Krämer, and Emmanuel Müller. Measuring and understanding trust calibrations for automated systems: A survey
of the state-of-the-art and future directions. 2023. https://dl.acm.org/doi/10.1145/3544548.3581197.
[23] Michael Wooldridge. This is not the AI we were promised. 2026. https://royalsociety.org/science-events-and-lectures/2026/02/faraday-prize-lecture/.
Draft
