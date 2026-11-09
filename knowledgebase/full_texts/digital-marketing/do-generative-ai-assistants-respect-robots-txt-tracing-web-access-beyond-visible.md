---
title: Do Generative AI Assistants Respect robots.txt? Tracing Web Access Beyond Visible Answers
url: https://arxiv.org/abs/2607.14447
category: digital-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Gabriel Lopez-Fonseca
- David Rodriguez
- Stefan Bechtold
- Jose M. Del Alamo
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.14447
pages: 30
chars: 121220
fetched_at: '2026-11-08T13:20:30+00:00'
kb_version: 1
---

# Do Generative AI Assistants Respect robots.txt? Tracing Web Access Beyond Visible Answers

DOGENERATIVEAI ASSISTANTSRESPECTrobots.txt?
TRACINGWEBACCESSBEYONDVISIBLEANSWERS
Gabriel Lopez-Fonseca
Universidad Politécnica de Madrid
ETSI Telecomunicación
Spain
gabriel.lopez@alumnos.upm.es
David Rodriguez
Information Processing and
Telecommunications Center
Universidad Politécnica de Madrid
ETSI Telecomunicación
Spain
david.rtorrado@upm.es
Stefan Bechtold
ETH Zurich
Center for Law & Economics
Department of Humanities,
Social and Political Sciences
Zurich, Switzerland
sbechtold@ethz.ch
Jose M. Del Alamo
Information Processing and
Telecommunications Center
Universidad Politécnica de Madrid
ETSI Telecomunicación
Spain
jm.delalamo@upm.es
ABSTRACT
AI assistants increasingly retrieve web content at inference time to provide fresh and grounded
answers, yet it remains unclear whether these search-augmented capabilities respect website-owner
restrictions expressed through robots.txt. We present a controlled empirical study of ten widely
used AI assistants with advertised web-search capabilities. For each assistant, we first identify a
configuration that actually produces observable web-browsing behavior and record the user-agent
exposed during retrieval. We then evaluate compliance with controlled robots.txt rules across
four complementary conditions: allowed for all user-agents, disallowed for all user-agents, allowed
only for the assistant-specific user-agent, and disallowed only for that user-agent. Using server-side
logs and secret codes embedded in target pages, we distinguish actual page access from user-visible
answer correctness across 200 trials.
Our results show substantial variation across assistants. Some systems followed the expected
allowed/disallowed access pattern, whereas others accessed restricted resources without requesting
robots.txt or used generic user-agents that complicated attribution. We also find that retrieval
behavior and answer correctness can diverge: assistants may access pages without surfacing the
retrieved content, or fail to access even allowed resources. These findings raise broader legal and
governance concerns about whether AI-assisted web access adequately respects content owners’ rights
and restrictions. Furthermore, our observations provide valuable insight into the growing erosion of
traditional web governance protocols, highlighting the urgent need for updated, enforceable standards
that guarantee publisher autonomy in the age of search-augmented AI assistants.
Keywordsrobots.txt·large language models·web crawling·compliance·AI assistants
1 Introduction
The advent of generative AI is changing the way information is searched for and found on the Internet. Traditionally,
users have primarily relied on search engines to locate information sources across a wide range of domains, including
everyday life, health, and work. Users typically entered a small set of keywords into their preferred search engine and
followed the returned links to consult the relevant sources. Today, however, Internet users are increasingly shifting from
arXiv:2607.14447v2  [cs.CY]  19 Jul 2026

Gabriel Lopez-Fonseca et al.
traditional search engines to AI assistants (Gottfried et al., 2026), directly asking questions and receiving immediate
answers without needing to visit multiple websites or consult the underlying sources themselves, a pattern commonly
referred to as zero-click search (Fishkin, 2024). To support this mode of interaction, AI assistants increasingly retrieve
information from the Internet, sometimes in real time, and use it to generate up-to-date answers to users’ questions.
This shifts the traditional pattern of interaction with online information, as users increasingly engage with the assistant
rather than directly with the original sources (Xu et al., 2023).
While conversational assistants and zero-click features offer unprecedented convenience by providing instant answers,
growing concerns over the accuracy and factuality of these AI-generated responses (Ja´ zwi´nska and Chandrasekar, 2025)
are coupled with severe economic damage inflicted on the information providers that sustain the ecosystem. According
to recent data (Fishkin, 2026), over 68% of all Google searches now end without a single click, effectively choking the
organic traffic that publishers rely on for survival.
Recent papers argue that AI Overviews divert traffic away from publishers without improving the user experience (Agar-
wal and Sen, 2026) and that search engines deploy them as a novel form of self-preferencing (Ng and Wessel, 2026).
Antitrust authorities and courts on both sides of the Atlantic have begun to examine whether using publishers’ content
without their consent constitutes anti-competitive conduct by search engines such as Google. European Commission
(2025b); Penske Media Corp. (2025)
Different passive and active controls have been proposed over the years to govern automated access to web content.
Unlike active barriers that introduce high friction and restrict legitimate traffic, passive mechanisms provide a governance
framework that signals publisher constraints without dismantling the open, accessible nature of the web. Among them,
the Robots Exclusion Protocol, implemented through robots.txt rules, is the most widely used passive control
mechanism adopted by content owners on the Internet (Dinzinger et al., 2024). This is a web standard (Koster et al.,
2022) that allows content owners to communicate crawling policies to automated agents via a set of allow/disallow
rules, specifying which resources crawlers may access and which they are requested to avoid. Compliant bots are
expected to identify themselves and voluntarily adhere to these rules.
However, it remains unclear whether and how search-augmented AI assistants respect and interpret robotx.txt rules.
Although the web-browsing capabilities have been assessed by recent works (Deng et al., 2023; Wei et al., 2025),
their focus has been mainly on task completion. Dinzinger et al. (2024) surveyed the legal and technical controls
available for governing generative AI access to web resources. Kim et al. (2025b) passively monitored a set of websites
to observe crawling behavior, detecting traces of AI assistants’ crawlers. Unlike existing research, our study uses a
controlled multi-condition experimental design to examine how robots.txt restrictions affect actual AI retrieval
behavior, revealing discrepancies that passive monitoring may overlook and linking them to specific AI assistants.
To this end, we examined if AI assistants are able to retrieve web content in real time when a user actively requests it,
and whether it follows website access rules defined in robotx.txt. Specifically, we evaluated the search-augmented
capabilities of ten widely used assistants and identified the user-agent they expose while crawling web resources.
We then tested their compliance with robotx.txt under four conditions: when access is allowed or denied for all
user-agents, and when it is specifically allowed or denied for each assistant. To assess their behavior, we hosted
dynamically generated target pages on a web server under our control, each containing a unique secret code. We
then used server logs to verify whether an assistant accessed the requested page and checked its response for the
corresponding code, allowing us to distinguish actual retrieval from fabricated answers. Our findings are based on 200
controlled trials.
Our results show that AI assistants vary widely in how they handle robotx.txt rules. While some follow the expected
access restrictions, others retrieve restricted content without requesting robots.txt; several also expose generic
user-agents that make their behavior harder to attribute. We also observed a mismatch between retrieval and responses:
assistants may access content without using it in their answers, or fail to access content even when permitted. Together,
these findings show that robots.txt cannot be assumed to reliably govern inference-time web access by AI assistants,
raising broader legal and governance concerns about the effectiveness of machine-readable restrictions in AI-mediated
content retrieval.
The remainder of this article is organized as follows. Section 2 provides the background on AI assistants, web retrieval,
and mechanisms for governing automated access, while Section 3 reviews the relevant literature. Section 4 describes
the experimental design and controlled web infrastructure. Sections 5 and 6 present the assessment of web-browsing
configurations and the evaluation of compliance with robots.txt, respectively. Section 7 discusses the implications
of the findings, Section 8 examines the study’s limitations, and Section 9 concludes the article.
2

Do Generative AI Assistants Respectrobots.txt?
2 Background
2.1 From Generative AI to AI Assistants and Agentic Systems
The current generation of AI assistants has emerged from the rapid diffusion ofgenerative artificial intelligence (AI)
systems built on top offoundation models. Foundation models have been described as large-scale models trained on
broad data distributions and later adapted to many downstream tasks (Schneider et al., 2024). Within this paradigm,
generative AI refers to systems capable of producing new content, such as text, code, images, or multimodal outputs
rather than merely classifying or retrieving information. These models have increasingly been packaged asAI assistants:
interactive systems that answer questions, summarize documents, retrieve information, and support human decision-
making in conversational form Mialon et al. (2024).
This evolution has also produced a second category of systems that is particularly relevant to the protection of online
content: thegenerative AI agent. In the recent literature, LLM-based agents are not understood as language models alone,
but as composite systems that combine the model with planning, memory, tool use, and environment interaction (Wang
et al., 2024). This distinction is analytically important. A conventional assistant may answer from model memory or
retrieved snippets, whereas an agentic assistant may browse the web, inspect files, invoke search tools, follow links, or
interact with external systems as needed to complete a given task. As a result, the governance problem is not limited
to model outputs; it extends to how content is discovered, fetched, processed, and reused during inference.Inference
refers to the stage in which a model uses its fixed pre-trained weights to process an input prompt and generate an output
response (Patil and Gudivada, 2024).
As AI assistants have become more capable, the field has moved beyond the narrower language of prompt engineering
toward what recent work callscontext engineering(Anthropic, 2025). Context engineering has been defined as the
systematic design, retrieval, processing, management, and integration of the information presented to a model at
inference time (Debnath et al., 2026). This broader framing is especially useful for assistant systems, because their
performance depends not only on the model’s internal parameters but also on the quality, freshness, provenance, and
orchestration of the external context supplied during interaction.
Within this broader landscape,retrieval-augmented generation (RAG)provides the key architectural bridge between
static model knowledge and dynamic external information. Lewis et al. (2020) introduced RAG as a framework that
combines parametric knowledge stored in the model with non-parametric retrieved evidence accessed at inference
time. The significance of RAG for this paper is twofold. First, it explains how assistants can answer questions with
information that is newer or more specific than what is stored in model weights. Second, it provides the conceptual
entry point for understanding web-enabled assistance, including live search, browsing, and grounding against external
sources. In this sense, RAG is not merely a performance technique; it is a governance-relevant mechanism through
which AI assistants gain access to third-party content.
2.2 Search-augmented LLMs: web-browsing agents and Index-Based Retrieval
Search-augmented LLMs can be understood as those AI assistants that obtain web informationduring inference, after
the user issues a request, rather than relying solely on pretraining data. WebGPT is a foundational research example of
this paradigm, showing how a model can search and navigate the web in support of long-form answering (Nakano et al.,
2021). However, this capability can be implemented in materially different ways.
At one end of the spectrum are systems based onweb-browsing agents, in which the assistant accesses and inspects web
pages in a browser-like manner during the interaction, issuing a live request to the target page. At the other end are
systems based onindex-based retrieval, in which the assistant obtains information through an intermediate search or
retrieval index rather than directly reading the target page at answer time. Such systems may therefore respond using a
previously indexed or cached representation instead of freshly retrieving the page. In practice, AI assistants may ground
their responses in direct inspection of specific pages, retrieval from indexed content, or a combination of both (Google,
2026c,e; Microsoft, 2026).
This distinction motivates the first empirical step of the paper: before assessing whether assistants respect robots.txt,
we need to determine whether a given assistant configuration produces observable fresh page retrieval, or whether the
assistant may instead answer from an intermediate layer such as a search index, cached copy, or other preprocessed
representation. Existing public documentation often confirms that assistants can access web information (OpenAI,
2024), but it does not always fully disclose which retrieval path was used in a given answer. For that reason, the
distinction betweenweb-browsing capabilitiesandindex-based or cached retrievalshould be treated as an empirical
variable rather than assumed from product terminology alone.
3

Gabriel Lopez-Fonseca et al.
2.3 Compliance and the Governance of Externally Sourced Content
When AI assistants are able to retrieve external content at inference time, the issue is no longer whether they can
access such content but whether they are permitted to do so under applicabledata governance,complianceandlegal
requirements. This point matters for the present paper because data governance should begin at the time of access. If an
AI assistant obtains content from the web in order to answer a user prompt, then the owner’s machine-readable conditions
for access and reuse become part of the upstream governance environment. When the AI assistant displays such content
to the user without honoring robotx.txt restrictions, this may raise copyright concerns: under the European Union’s
Digital Single Market Directive, text and data mining must respect opt-outs expressly declared by rightholders (Article
4(3) of the Directive, European Union (2019)). When the AI assistant uses such content for subsequent processing,
ignoring rightholder-declared restrictions may set in motion a broader chain of potential non-compliance: improper
acquisition can propagate through indexing, retrieval, and synthesis, ultimately yielding harmful or infringing outputs.
In such cases, the European Union’s Artificial Intelligence Act (EU AI Act) becomes relevant. The Act distinguishes
betweengeneral-purpose AI modelsand theAI systemsthat incorporate them. On this taxonomy, many contemporary
AI assistants are best understood as AI systems built upon, or integrating, general-purpose AI models. Within this
framework, Article 53 sets out core obligations for providers of general-purpose AI models, including documentation
and transparency duties and a policy to comply with EU copyright law, in particular the identification of and compliance
with rights reservations expressed by rightholders (European Union, 2024; European Commission, 2025c,a). Overall,
the governance analysis encompasses both the model’s output and the process through which the assistant acquired the
underlying content.
A related complication is that data-use practices are not consistent across providers or deployment contexts. Some
consumer-facing services may use chats or reviewed interactions for model improvement, whereas certain paid or enter-
prise offerings explicitly state that such data are excluded from product improvement processes. This variability further
strengthens the case for examining content governance at the point of acquisition, because the downstream treatment of
retrieved or submitted content may vary substantially across products, plans, and technical interfaces (OpenAI, 2026b;
Google, 2026a).
2.4 Passive and Active Controls for Protecting Web Content
Content owners have increasingly adopted technical and policy mechanisms to express or enforce restrictions on
automated access. A growing body of work and practice distinguishes betweenpassive controlsandactive controlsfor
protecting web content from crawlers and related automated agents. Passive controls are machine-readable signals that
express owner preferences without physically preventing access. These include robots.txt, meta robots directives,
X-Robots-Tag headers, theText and Data Mining Reservation Protocol (TDMRep)(W3C Community Group, 2024),
and provider specific product User-Agent HTTP headers such as GPTBot, OAI-SearchBot (OpenAI, 2026c), or
Google-Extended(Google, 2026b).
Although these mechanisms can all express access or reuse preferences, our focus is onrobots.txtbecause it is the
most established and methodologically comparable of the passive controls. Website operators have long used it as a site-
level mechanism to communicate crawler-specific restrictions and guide automated indexing (Drott, 2002). Dinzinger
et al. found that 56% of 60 million regular web pages used robots.txt, while HTML robots meta tags appeared on
52.7% of pages and X-Robots-Tag headers on only 0.6% of HTTP responses. They also found limited adoption of
the TDM Reservation Protocol: as of January 2024, only 45 hosts served a tdmrep.json file under the .well-known
directory. Unlike meta robots directives or X-Robots-Tag headers, which are resource-level signals observable only
after fetching individual pages or responses, robots.txt is a site-level, machine-readable file located at a predictable
origin path and governed by the Robots Exclusion Protocol (Koster et al., 2022). Moreover, robots.txt has been the
subject of prior large-scale empirical studies on crawler governance and compliance, whereas newer alternatives such
as TDMRep remain more specialized, less mature, or less widely standardized (Dinzinger et al., 2024).
By contrast, active controls attempt to enforce restrictions at the technical layer. These include reverse proxies, web
application firewall rules, IP-based filtering, authentication barriers, CAPTCHAs, and rate limiting. Recent empirical
work by Liu et al. (2025) provides relevant evidence on the practical limitations of these mechanisms. Studying artists
and online creators, the authors find strong demand for tools such as robots.txt but also show substantial limits
in user awareness, deployment capability, and effectiveness against unresponsive crawlers. Active controls, however,
impose additional implementation and maintenance costs on content owners. The results reported later in this paper
also show that, in some cases, the source of assistant-mediated requests is difficult to identify, which may limit the
effectiveness of active controls based on provider-specific attribution. These mechanisms may also introduce friction
for legitimate human users, particularly when controls rely on authentication barriers, CAPTCHAs, or aggressive
filtering. For these reasons, our analysis selects robots.txt as the most suitable passive-control baseline for systematic
empirical evaluation.
4

Do Generative AI Assistants Respectrobots.txt?
2.5 The Robots Exclusion Protocol and the Governance of Crawling
Standardized in RFC 9309, the Robots Exclusion Protocol specifies how automated agents retrieve and interpret
robots.txt directives, including user-agent matching and the processing of allow and disallow rules (Koster et al.,
2022). These directives provide a machine-readable mechanism through which website owners communicate their
crawling preferences to automated agents.
The protocol does not technically prevent access or operate as an authorization mechanism. Instead, its practical
effectiveness depends on automated agents correctly implementing and applying the applicable rules before retrieving
a resource. This distinction is important: accessing a disallowed resource indicates that the communicated crawling
policy was not respected, but does not, by itself, establish that the access was unauthorized or unlawful. Whether such
access is legally problematic depends on the applicable legal framework, the purpose of the retrieval, and how the
retrieved content is subsequently used.
2.6 Who Decides Whetherrobots.txtIs Respected?
A further complexity is that responsibility for respecting robots.txt is not always located in a single component. In
some cases, the relevant actor is a conventional search crawler; in others, it is a user-triggered fetcher or assistant-side
retrieval tool. This distinction is critical because it shows that the question is not simply whether “the AI assistant”
respects robots.txt, but rather which subsystem accessed the content, under which declared purpose, and according
to which rules of interpretation (OpenAI, 2026c; Google, 2026d).
Accordingly, a rigorous assessment should not treat AI assistants as a single undifferentiated actor. This layered
architecture is one reason why the live-browsing question is so important. If an answer comes from a search-grounded
index, compliance may depend primarily on the upstream crawl and indexing pipeline. If it comes from direct browser-
like access triggered at inference time, compliance may depend on a different user-agent, a different fetch path, or a
different interpretation of owner controls altogether. The empirical challenge, then, is to determine which component
actually accesses the content, which user-agent it exposes, and whether that component applies the access restrictions
declared by the website owner.
2.7 Implications for the Present Study
Taken together, these developments establish the context of the problem addressed in this paper. AI assistants
increasingly depend on external web content to provide timely and useful answers; owners of online content increasingly
deploy passive and active controls to govern automated access; and current governance frameworks increasingly
emphasize data quality, accuracy, robustness, and lawful handling of information. Yet an important gap remains
between these developments: there is still limited clarity about whether contemporary Search-augmented LLMs truly
are web-browsing agents, whether they rely on search indexes or cached representations, and whether the relevant
systems respect the machine-readable restrictions established by content owners.
That gap is not merely technical. It sits at the intersection of retrieval architecture, web governance, copyright law, and
AI compliance. Accordingly, this paper treats respect for owner-declared web controls—especially robots.txt—as a
foundational element of responsible data governance for generative AI assistants. If assistants are increasingly expected
to be accurate, robust, and compliant, then the acquisition of external content during inference should itself be evaluated.
3 Related Work
Recent research on AI assistants has moved beyond evaluating isolated text-generation abilities and increasingly
examines whether large language models can act as general-purpose agents: using tools, browsing the web, following
instructions, interacting with users, and completing multi-step tasks in realistic environments. This section reviews
three strands of related work: benchmarks for general assistant and agent capabilities, evaluations of web-browsing
agents, and studies of technical controls for governing automated access to web content. Together, these works show
substantial progress in measuring what AI assistants can do, but leave open the question of whether assistant-mediated
web access is observable, attributable, and compliant with website-owner restrictions.
3.1 Studies on General AI Assistant Capabilities
Prior evaluations of AI assistants and LLM agents span task-completion benchmarks, tool-use assessments, and process-
level evaluation frameworks. GAIA (Mialon et al., 2024) evaluates general-purpose assistants through real-world
5

Gabriel Lopez-Fonseca et al.
questions that require reasoning, tool use, and multi-step problem solving. AgentBench (Liu et al., 2024) assesses LLM
agents across interactive environments involving decision-making, tool use, and multi-turn action.
Other benchmarks and evaluation frameworks focus on agent interaction in web-based or domain-specific environments.
WebArena (Zhou et al., 2024) evaluates agents in web-based environments, while τ-bench (Yao et al., 2025) focuses on
tool-agent-user interactions in domains such as retail and airlines, including the ability to follow domain-specific policies
and behave consistently across repeated trials. Beyond Browsing (Song et al., 2025) compares task completion through
web interfaces and APIs, showing that the interaction channel can affect agent performance. AgentBoard (Ma et al.,
2024) proposes an evaluation framework for multi-turn LLM agents across workflows, environments, and sequences
of actions. Broader surveys of LLM-agent evaluation (Yehudai et al., 2026) similarly emphasize the importance of
evaluating the process followed by agents, rather than relying only on final success rates.
Relation to our work.This line of research shows that assistant behavior should be evaluated as a process, not only
through final task success. However, these studies primarily assess whether agents can complete tasks, use tools, follow
instructions, or interact with users in benchmarked environments. They do not evaluate whether deployed AI assistants
access third-party web content in a way that is observable from the server side, attributable through user-agent evidence,
or compliant with website-owner restrictions such as robots.txt. Our work therefore complements process-level
assistant evaluation by focusing on the governance of inference-time web access.
3.2 Studies on Web-Browsing Capabilities
A more specific strand of work evaluates LLM agents in tasks that require interaction with web pages or retrieval of
information from online sources. Mind2Web (Deng et al., 2023) introduced a dataset for evaluating generalist web
agents on natural-language instructions across real websites, rather than in purely simulated web environments. The
benchmark focuses on whether agents can navigate web interfaces and complete tasks that require interacting with page
elements. BrowseComp (Wei et al., 2025) evaluates web-browsing ability through difficult multi-hop questions. Its
focus is on open-web information retrieval and evidence gathering across multiple online sources, rather than simple
single-page lookup.
These benchmarks are relevant because they evaluate web interaction as part of agent behavior. However, they primarily
assess task completion, navigation ability, or information-retrieval performance from the perspective of the agent or the
user. They do not evaluate the server-side footprint generated by deployed AI assistants, including whether the assistant
directly retrieves the requested page at inference time, which user-agent is exposed during access, and whether the
access path respectsrobots.txtrestrictions.
Relation to our work.Our study is complementary to web-agent benchmarks, but shifts the target of evaluation from
browsing success to access governance. Rather than measuring whether an agent can complete a web task, we measure
whether deployed AI assistants generate observable requests to controlled web pages, request robots.txt, expose
attributable user-agents, and behave consistently with the access rules declared by the website owner.
3.3 Studies on Technical Controls to prevent Automated Access
A third line of related work studies mechanisms for controlling automated access to web content and measuring
whether automated agents comply with those controls. Dinzinger et al. (2024) survey legal and technical mechanisms
for controlling generative AI access to web resources, including robots.txt, AI-specific user-agent identifiers,
learners.txt, noai tags, and the Text and Data Mining Reservation Protocol. Their work focuses on the availability
and adoption of these mechanisms. They report that robots.txt remains the most widely used control, whereas newer
approaches such as noai/noml metadata and learners.txt remain limited in adoption. This line of work establishes
the relevance of machine-readable access signals, but does not test whether deployed AI assistants apply those signals
during user-triggered web access.
Other work has measured compliance from the server side. Kim et al. (2025b) study scraper compliance with
robots.txt using server logs from 36 institution-controlled websites. Their methodology passively observes crawler
behavior, including AI search crawlers, after deploying robots.txt configurations, and then analyzes which bots
accessed the sites and whether those accesses were consistent with the published directives. This study is closely
related to ours because it relies on server-side evidence to evaluate compliance. However, its focus is on crawler traffic
observed over time, rather than on retrieval triggered by direct user prompts to AI assistants during inference.
A complementary perspective is provided by Liu et al. (2025), who examine how content creators, especially artists,
attempt to protect online content from AI crawlers. Their study combines web-scale measurements, a survey of
creators, passive measurements of crawler behavior, and active experiments with anti-crawling mechanisms such as
robots.txt, NoAI metadata, and reverse-proxy-based blocking. This work shows both the demand for content-
6

Do Generative AI Assistants Respectrobots.txt?
protection mechanisms and the practical limits of deploying them, especially when crawlers do not respond to passive
signals or when stronger controls impose costs on content owners and users.
Relation to our work.These studies establish the importance of robots.txt and related mechanisms for governing
automated access to web content. Our study differs by focusing on deployed AI assistants with web-search or browsing
capabilities and by actively triggering retrieval through user prompts during inference time. Rather than measuring
the adoption of controls or passively observing crawler traffic, we evaluate whether assistants retrieve controlled web
pages in response to user requests, whether they request robots.txt, which user-agent they expose, whether their
behavior changes across allowed and disallowed rules, and whether server-side access corresponds to user-visible
answer correctness. This design allows us to study assistant-mediated web access as a distinct form of automated access
that sits between conventional crawling, search-based retrieval, and browser-like interaction.
4 Experimental Setting
4.1 Overview of the Experimental Design
We designed a two-phase experimental methodology to evaluate how AI assistants access web content during inference
time and whether they comply withrobots.txt restrictions. The first phase identifies, for each assistant, a configuration
that enables observable web-browsing behavior and records the user-agent exposed during retrieval. The second phase
uses those configurations to test whether assistants access or avoid resources under controlledrobots.txtrules.
Both phases use web infrastructure under our control. In each trial, a user prompts the AI assistant to retrieve contents
of a specific web page hosted on our website; the assistant processes the request; and the user receives an answer. We
monitor server-side logs to determine whether the requested page, robots.txt, or other resources were accessed, and
which user-agent issued each request. A distinct target page was dynamically generated for each trial, and a different
domain was used in each phase to reduce the risk of cached or indexed content affecting subsequent measurements.
Figure 1 summarizes the experimental interaction observed in both phases. The figure distinguishes between direct
live retrieval, where an assistant-side web-browsing component sends HTTP requests to our controlled website, and
index-based retrieval, where the assistant may rely on a search index or cached representation instead of directly
fetching the target page at answer time. This distinction is central to our methodology: server-side logs allow us to
observe direct retrieval events, requests to robots.txt, and target-page accesses, while the assistant’s final answer
allows us to assess whether retrieved content was surfaced to the user.
4.2 Controlled Web Infrastructure
Our web server was configured to log requests to the resources hosted in the experimental domains, including target
web pages, robots.txt, sitemap.xml, and auxiliary resources. The server logs recorded the requested resource,
requester IP address, timestamp, HTTP status code, and the client user-agent. Each target web page was generated with
a unique secret code computed using a Hash-based Message Authentication Code (HMAC). This allowed us to verify
whether an assistant had actually retrieved the requested page and whether its answer was grounded in the page content.
We used two separate domains. The first domain, genaimonitor.org, was used in Phase 1 to identify web-browsing
configurations and user-agents. The second domain, aicrawlerlab.org, was used in Phase 2 to test compliance
with controlled robots.txt rules. Using distinct domains reduced the risk that results from the first phase affected
the second phase through caching, indexing, or previously retrieved content. The web server architecture is shown in
Figure 2.
4.3 AI Assistant Selection and Prompt Design
Assistant selection.The selection of AI assistants was based on the top-ranked systems in the LMArena Search
Arena Leaderboard, which ranks LLMs with integrated web-search capabilities (LMArena, 2026). The leaderboard was
accessed on January 29, 2026. The selected leading assistants were Gemini, ChatGPT, Grok, Claude, Perplexity, and
Diffy Chat. We additionally included Copilot (Counts et al., 2026), DeepSeek (Xu et al., 2025), Mistral, and Qwen due
to their current relevance (Lambert et al., 2026).
Prompt design.We designed the prompt used to trigger web access after reviewing recent work on LLM-based web
extraction and browser-agent interaction (Kim et al., 2025a; Yu et al., 2026). These works suggest several prompting
patterns for web tasks, including explicitly defining a browser action space (e.g., GO_TO, CLICK, SCROLL, READ, and
EXTRACT), decomposing the task into sequential steps, asking the model to plan before acting, and requiring evidence-
based extraction grounded in the retrieved HTML or DOM content. Following these recommendations, we initially
7

Gabriel Lopez-Fonseca et al.
Figure 1: Experimental interaction between the user, the AI assistant, and one of our controlled websites. The figure
illustrates the server-side observation point used in both phases, including possible direct live retrieval, access to
robots.txt, target-page retrieval, and alternative or complementary index-based retrieval paths.
Figure 2: Experimental setting of our Controlled Web Server. The figure illustrates the steps of the flow of how a user
requests online content to an AI assistant to our web server.
8

Do Generative AI Assistants Respectrobots.txt?
tested a more structured prompt composed of a system-level instruction describing the allowed browser-style actions
and a user-level instruction specifying the target URL and the expected evidence to extract. The complete version of
this structured prompt is reported in Appendix A.2.
However, preliminary tests with ChatGPT and Gemini showed that this highly structured prompt introduced additional
sources of variability in our setting. In some cases, the assistants produced timeouts; in others, they hallucinated
browser actions or failed to return the controlled content even when the task was simple. More importantly, this type
of prompt risked evaluating the assistant’s ability to follow an artificial browser-agent protocol rather than its default
web-browsing behavior as exposed to ordinary users. Since our goal was not to optimize browsing performance through
prompt engineering, but to observe whether assistants actually accessed a controlled URL and how they did so from the
server-side perspective, we adopted a simpler prompt for the experiments:“Get the contents from [URL]. I manage the
server and will know if you are really accessing it”. The URL pointed to a target page hosted on our controlled web
server. The ownership statement truthfully described the experimental setting and emphasized that retrieval could be
independently verified; it neither instructed the assistant to disregard robots.txt nor altered the rules published by
the server (see Section 8).
This simpler prompt was retained for three reasons. First, it directly expressed the user’s intent without imposing a
custom navigation policy on the assistant. Second, it reduced the risk that failures or successes were caused by the
prompt structure rather than by the assistant’s own retrieval pipeline. Third, it allowed us to verify the assistant’s
behavior independently through two complementary signals: server-side logs showing whether the requested URL was
accessed, and the assistant’s response showing whether it retrieved the secret code embedded in the target page. We
therefore used this prompt consistently in Phase 1 and Phase 2.
5 Phase 1. Web-Browsing Configuration Assessment
5.1 Methodology
Once the target AI assistants and the final prompt were defined, we verified which versions and configuration modes
exhibited observable web-browsing capabilities. This phase was conducted using genaimonitor.org as our target
website. For each tested configuration, the URL in the prompt pointed to a target page hosted on our controlled
server, such as /pages1/page_v1.html. A configuration was considered successful when two conditions were met:
our server logs recorded an HTTP request for the target page, and the assistant returned the expected secret code
embedded in that page. These two signals allowed us to identify a configuration that enabled web-browsing behavior
for each assistant and to record the user-agent exposed during retrieval. The robotx.txt rules designed to evaluate the
web-browsing configuration were to allow and disallow all:
•Allow all:the requested page is located in a folder allowed for all user-agents.
•Disallow all:the requested page is located in a folder disallowed for all user-agents.
During this phase of the experiment, we only requested pages that were allowed for all user agents.
We tested configurations according to a fixed priority order. When available, we first used the free default model in a
temporary chat without signing in. If this configuration did not produce a successful retrieval, we tested the free default
model after signing in, first in a temporary chat and then with a non-temporary chat. If the default model still failed, we
tested alternative model versions, again prioritizing temporary chats when available.
This order was designed to reduce carry-over effects across trials. We preferred temporary chats because they
are intended to avoid retaining conversation history or memory across interactions, whereas non-temporary chats
may preserve context that can influence subsequent requests. Subject to this constraint, we prioritized free and
default configurations before moving to signed-in, non-temporary, or alternative-model settings. Figure 3 shows this
configuration selection process.
Each configuration was tested five times per assistant. We used repeated trials because single executions were not
sufficient to distinguish stable web-browsing behavior from occasional retrieval success or failure. A trial was considered
successful when the requested page appeared in our server logs and the assistant returned the correct secret code. If a
configuration succeeded in all five trials, it was selected as the working configuration. If no configuration achieved five
successful trials, we selected the configuration with the highest number of successful trials. The resulting configurations
and observed user-agents are reported in the following section.
9

Gabriel Lopez-Fonseca et al.
Figure 3: Configuration-selection procedure used to identify a working web-browsing setup for each AI assistant.
5.2 Results
The configuration assessment identified at least one configuration exhibiting observable web-browsing behavior for each
evaluated assistant. Table 1 summarizes the selected configuration, the authentication requirements, and the user-agent
observed during retrieval.
AI assistant Selected model/mode Plan Login Temporary chat User-agent
ChatGPT Search, Auto Instant 5.3 / Thinking 5.4 Plus✓ ✗ChatGPT-User
Claude Default Sonnet 4.6 Free✓ ✓Claude-User
Copilot Default Smart Free✗ ✗Diffbot-User
DeepSeek Default Search Free✓ ✗Generic
Diffy Chat Default Reasoning Google fallback 0 Free✗ ✗Generic
Gemini Default Gemini 3 Free✓ ✗Google
Grok Default Expert, Grok 4.20 Free✓ ✓Generic
Mistral Default Fast Free✓ ✓MistralAI-User
Perplexity Academic Free✓ ✓Perplexity-User
Qwen Default Fast Qwen 3.5-Plus Free✗ ✗Generic
Table 1: Selected web-browsing configuration for each AI assistant after the Phase 1 assessment. “Login” indicates
whether the assistant was tested while signed in. ✓ indicates yes and ✗ indicates no. The final column reports the
user-agent observed in the server logs during retrieval.
10

Do Generative AI Assistants Respectrobots.txt?
This assessment showed that advertised search or browsing modes do not necessarily imply observable retrieval or
correct content extraction. In several cases, assistants accessed the requested page according to our server logs but did
not return the expected content to the user; in other cases, they returned incorrect or inconsistent answers. We therefore
treated web-browsing capability as an empirical property of a specific assistant configuration rather than assuming it
from product labels alone.
The configuration assessment was not equally straightforward across assistants. ChatGPT and Copilot required the most
extensive calibration. For ChatGPT, we tested all modes and models available in the free version and then additional
PLUS configurations, for a total of 22 tested configurations. None of these configurations succeeded in all five trials.
Only five configurations returned the correct secret code at least once, and the best-performing configuration succeeded
in only two of the five repetitions. We selected the advertised search mode because it was explicitly intended for web
access and could be tested more repeatedly than the research mode, which was subject to stricter usage limits.
Copilot showed a similar inconsistency across 9 tested configurations: in several cases, it accessed the requested page
according to our logs but did not return the expected content to the user. By contrast, Claude, Diffy Chat, and Qwen
produced correct and consistent answers during the initial trials, while Gemini, Grok, Mistral, and Perplexity produced
a working configuration in the second configuration tested. These differences show that configuration selection was
necessary to establish a baseline for therobotx.txtexperiment.
Several additional observations emerged during the configuration assessment. First, advertised web-search modes did
not always translate into correct user-facing answers. For example, Copilot accessed the requested page in four out of
five trials with its Default Smart mode, according to our server logs, but stated that it could not reach the server and did
not return the expected secret code. This illustrates a distinction that is important for the rest of the study: server-side
retrieval and user-visible answer correctness are related but not equivalent.
Second, access to web-browsing functionality varied across products and account states. DeepSeek and Qwen did not
provide a temporary-chat option when using search mode. Claude and DeepSeek required the user to be signed in,
whereas Mistral and Gemini allowed tool use without signing in but did not return correct answers in that configuration.
In particular, Gemini hallucinated the requested content in all unauthenticated trials. These differences affected which
configurations could be tested and confirmed the need to evaluate each assistant under a concrete configuration.
Finally, we observed assistant-specific retrieval behaviors that were not visible from the user interface alone. In
Copilot Paid Chat Basic with Think Deeper mode, the assistant-side retrieval process requested auxiliary resources such
as /404testpage4525d2fdc, /404javascript.js, and /pages1/.git/HEAD before or around the target-page
retrieval. Perplexity showed a different inconsistency: it often stated that it could not access the requested page, while
the correct secret number appeared in the follow-up section, indicating that the content had been retrieved by some
component of the system. Figure 4 shows an example of this behavior.
Figure 4: Perplexity response stating it was unable to retrieve the requested contents but showing them (17359427 was
the secret code) in the follow-ups section.
11

Gabriel Lopez-Fonseca et al.
6 Phase 2.robotx.txtCompliance Assessment
6.1 Methodology
The second phase evaluated whether the AI assistants complied with controlledrobots.txt rules during inference-time
web access. This phase was conducted using a second domain just registered for this experiment, aicrawlerlab.org,
and reused the assistant configurations identified in Phase 1. For each trial, server logs were used to verify whether the
assistant requestedrobots.txtand whether it accessed the target page, while the assistant’s response was examined
to determine whether it retrieved and returned the page content.
The user-agents observed in Phase 1 were used to define the robots.txt groups for this experiment. Some assistants
exposed identifiable user-agents (Claude, Gemini, ChatGPT, Perplexity, and Mistral), whereas others used generic
user-agents (Grok, Diffy Chat, Qwen, Copilot, and DeepSeek). An example of the generic user-agent used by Grok is:
"http_user_agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36
(KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",→
Because generic user-agents make assistant-specific attribution difficult from server-side logs alone, we created in our
server assistant-specific folders for identifiable user-agents and generic folders for assistants that could not be reliably
distinguished through the user-agent string.
The robots.txt file was designed according to RFC 9309 and included rules derived from the user-agents observed in
Phase 1. The goal was not only to test whether assistants avoided disallowed resources, but also whether they accessed
resources that were explicitly allowed. This distinction is important because non-access to a restricted resource is not
sufficient evidence of compliance if the assistant also fails to access allowed resources under the same configuration.
Therefore, the rules were designed to test four complementary conditions for each assistant:
•Allow all:the requested page is located in a folder allowed for all user-agents.
•Disallow all:the requested page is located in a folder disallowed for all user-agents.
• Allow assistant-specific user-agent:the requested page is located in a folder allowed only for the tested
assistant’s user-agent.
• Disallow assistant-specific user-agent:the requested page is located in a folder disallowed only for the tested
assistant’s user-agent.
Table 2 summarizes the folder structure used to implement these conditions. The complete robots.txt file derived
from this structure is provided in Appendix A.1.
For each assistant, we used the configuration selected in Phase 1 (summarized in Table 1) and prompted the assistant to
retrieve an HTML page from each of the four robots.txt conditions using the prompt defined in Section 4.3, starting
with the Allow all condition. Each condition was tested five times, using a different target page in each trial to reduce
the risk of cached responses. This resulted in 20 trials per assistant and 200 trials in total.
Each target page contained a secret number generated using an HMAC over the page version. The private key was stored
on our server. We assigned a distinct page-version range to each assistant, which allowed us to associate requested
pages with the corresponding assistant during log analysis. For example, the range 2001–2020 was assigned to Claude,
so its first target page waspage_v2001.html. Table 3 shows the page-version ranges used for each assistant.
AI assistant Page-version range
ChatGPT 2201–2220
Claude 2001–2020
Copilot 2801–2820
DeepSeek 2901–2920
Diffy Chat 2601–2620
Gemini 2101–2120
Grok 2501–2520
Mistral 2401–2420
Perplexity 2301–2320
Qwen 2701–2720
Table 3: Page-version ranges assigned to each assistant in the Phase 2 trials.
12

Do Generative AI Assistants Respectrobots.txt?
Type Path Purpose
File/robots.txtPublicrobots.txtfile
File/index.htmlPublic main page
File/page1.htmlPublic page
File/page2.htmlPublic page
File/sitemap.xmlPublic sitemap
Folder/pages1/Allowed for all user-agents
Folder/pages2/Disallowed for all user-agents
Folder/a1/Allowed for Claude
Folder/a2/Disallowed for Claude
Folder/b1/Allowed for Google/Gemini
Folder/b2/Disallowed for Google/Gemini
Folder/c1/Allowed for ChatGPT
Folder/c2/Disallowed for ChatGPT
Folder/d1/Allowed for Perplexity
Folder/d2/Disallowed for Perplexity
Folder/e1/Allowed for Mistral
Folder/e2/Disallowed for Mistral
Folder/f1/Allowed for generic user-agents
Folder/f2/Disallowed for generic user-agents
Table 2: Folder structure used to implement the four controlled robots.txt conditions in Phase 2. Assistant-specific
folders were created for identifiable user-agents, while /f1/ and /f2/ were used for assistants with generic user-agents.
For each trial, we recorded five outcome variables: whether the assistant requested robots.txt; whether it accessed
the target page; the user-agent observed in the server logs; the number of accesses to the target page; and whether the
assistant returned the correct secret number in its response. The processed trial-level data and sanitized server logs
supporting this analysis are available to reviewers through an anonymized repository, which will be made publicly
available upon acceptance.
6.2 Results
Table 4 summarizes the Phase 2 results across the four robots.txt conditions. For each assistant and condition, we
report the number of observed requests to robots.txt, the number of accesses to the requested target pages and other
resources in our website, and the number of trials in which the assistant returned the correct secret number. Since each
condition was tested five times per assistant, the maximum value for correct answers is five. The number of target-page
accesses may exceed five when an assistant requested the same target page multiple times during a trial.
The results reveal three broad patterns. First, Claude and Mistral followed the expected allowed/disallowed access
pattern: they accessed pages when access was allowed and avoided target pages when access was disallowed. Perplexity
mostly followed this pattern, although it accessed one page in the Disallow All condition and showed inconsistencies
between retrieved content and user-visible answers.
Second, several assistants accessed target pages without ever requesting robots.txt. This was the case for Copilot,
DeepSeek, Diffy Chat, Gemini, Grok, and Qwen. Among them, DeepSeek, Gemini, Grok, and Qwen returned correct
answers even for disallowed resources, indicating that they retrieved restricted content without first fetching the
corresponding robots.txt file during the active trials. We also checked our historical logs for this server and found
no previous requests to robots.txt compatible with these assistants. A notable pattern is that all assistants using
generic or non-identifiable user-agents in our logs (Copilot, DeepSeek, Diffy Chat, Grok, and Qwen) accessed target
pages without requesting robots.txt during the active trials or anytime in the past. Gemini also accessed target pages
without requestingrobots.txt, despite exposing an identifiable Google user-agent.
Third, retrieval and answer correctness did not always coincide. ChatGPT requested robots.txt once but did not
access any target page or return any correct answer (even allowed ones). Copilot accessed every requested target page
(even disallowed ones) but returned no correct answers. Diffy Chat accessed several target pages but returned the
correct secret number only once. These cases show that server-side access and user-visible answer correctness must be
analyzed separately.
13

Gabriel Lopez-Fonseca et al.
AI Assistantrobotx.txtRule #Robots Access #web Page Access #Answer
ChatGPT Allow All 1 0 0
Disallow All 0 0 0
Allow ChatGPT Only 0 0 0
Disallow ChatGPT Only 0 0 0
Claude Allow All 1 5 5
Disallow All 0 0 0
Allow Claude Only 0 5 5
Disallow Claude Only 0 0 0
Copilot Allow All 0 5 0
Disallow All 0 5 0
Allow Generic User-Agent Only 0 5 0
Disallow Generic User-Agent Only 0 5 0
Deepseek Allow All 0 5 5
Disallow All 0 5 5
Allow Generic User-Agent Only 0 5 5
Disallow Generic User-Agent Only 0 5 5
Diffy Chat Allow All 0 4 1
Disallow All 0 4 0
Allow Generic User-Agent Only 0 2 0
Disallow Generic User-Agent Only 0 1 0
Gemini Allow All 0 5 5
Disallow All 0 5 5
Allow Gemini Only 0 4 4
Disallow Gemini Only 0 5 5
Grok Allow All 0 52 5
Disallow All 0 48 5
Allow Generic User-Agent Only 0 48 5
Disallow Generic User-Agent Only 0 50 5
Mistral Allow All 1 10 5
Disallow All 0 0 0
Allow Mistral Only 0 6 3
Disallow Mistral Only 0 0 0
Perplexity Allow All 1 5 4
Disallow All 0 1 1
Allow Perplexity Only 0 5 1
Disallow Perplexity Only 0 0 0
Qwen Allow All 0 6 5
Disallow All 0 5 5
Allow Generic User-Agent Only 0 4 4
Disallow Generic User-Agent Only 0 3 3
Table 4: robots.txt compliance highlights. “robots.txt Rule” indicates the robotx.txt directive tested; we requested 5
different web pages per rule per AI assistant. #Robots Access is the total number of accesses to robots.txt observed
for every rule after the 5 tests. #Web Page Access is the total number the AI assistant accessed the requested web page
after the 5 tests. #Answer is the number of requests where the AI assistant answered correctly (max 5).
14

Do Generative AI Assistants Respectrobots.txt?
6.2.1 Assistants following the expected behavior
Claude showed the clearest compliance pattern. It requested robots.txt once, accessed all five pages in the Allow
All condition, and accessed all five pages in the Claude-specific allow condition. It did not access any target page in
either disallow condition and returned correct answers only when access was allowed. When access was disallowed,
Claude did not access the target page and returned an explicit message indicating that retrieval was blocked by the site’s
robots.txtrules. An example of Claude’s blocked-access response is provided in Appendix A.5.
Mistral also followed the expected disallow behavior. It requested robots.txt once and did not access pages in
the Disallow All or Mistral-specific disallow conditions. In allowed conditions, however, its behavior was less
stable: it accessed the /pages1/ pages ten times across five trials and returned five correct answers, while in the
Mistral-specific allow condition it returned three correct answers. The two incorrect answers were associated with
confusion between similar page-version identifiers. In one case, the requested page was/e1/page_v2412.html, but
Mistral returned content corresponding to /e1/page_v2142.html. In another case, it confused a requested /e1/ page
with a page-version identifier outside the assigned Mistral range. These errors suggest that Mistral’s retrieval behavior
followed the expected access restrictions, but its answer generation was not always aligned with the exact requested
page.
Perplexity showed partial compliance. It requestedrobots.txt once and did not access the Perplexity-specific disallow
folder. However, it accessed one page in the Disallow All condition and exposed the corresponding secret number in
the follow-up section. In allowed conditions, it accessed the expected pages but often failed to surface the retrieved
content as a direct answer.
6.2.2 Assistants accessing disallowed resources
DeepSeek, Gemini, Grok, and Qwen did not request robots.txt during the active trials but accessed pages in both
allowed and disallowed conditions. DeepSeek accessed each requested page once and returned correct answers in all
conditions. Gemini showed a similar pattern, with one hallucinated answer. Qwen accessed fewer target pages in the
generic allow and disallow conditions but returned correct answers whenever it retrieved the content.
Grok exhibited the strongest request amplification pattern. It did not request robots.txt, accessed both allowed
and disallowed resources, and generated substantially more page accesses than the five requested trials per condition:
52 accesses in Allow All , 48 in Disallow All , 48 in the generic allow condition, and 50 in the generic disallow
condition. Despite this amplification, it returned correct answers in all five trials for each condition.
6.2.3 Retrieval and answer inconsistencies
ChatGPT requested robots.txt once but did not access any of the requested target pages and did not return any
correct answer. This behavior should therefore not be interpreted as compliance with disallow rules, because ChatGPT
also failed to access allowed resources.
Copilot showed the opposite pattern: it did not request robots.txt, accessed every requested target page, including
disallowed pages, but never returned the correct secret number to the user. Diffy Chat also did not requestrobots.txt;
it accessed some pages across all four conditions but returned the correct secret number only once, in the Allow All
condition.
6.2.4 Passive monitoring outside active testing
After the active trials, we continued monitoring the website for more than one month to observe follow-up accesses
outside the experimental window. Claude, Copilot, DeepSeek, Diffy Chat, Gemini, Mistral, and Qwen accessed the
website only during the active trials. We also observed requests using a Google user-agent, but the corresponding source
IPs did not pass Google’s recommended reverse-DNS validation, so we did not attribute those requests to Google.
ChatGPT continued requesting robots.txt twice per day, using OAI-SearchBot/1.3 and OAI-SearchBot/1.0.
The first recurring ChatGPT crawl was observed shortly after the website was enabled, before the active testing period,
and the second recurring user-agent appeared after the first active request. Perplexity requested robots.txt five times
during the three days following its first active request and accessed the root page three times after the last request. Grok
revisited pages accessed during active testing, producing 173 additional page accesses over the week following the last
test. Figure 5 shows the passive monitoring time series.
15

Gabriel Lopez-Fonseca et al.
Figure 5: Passive monitoring time series showing follow-up accesses to the controlled website outside the active testing
period.
7 Discussion
Attribution and traffic governance in assistant-mediated browsing.Our results show that inference-time web
access by AI assistants can generate a server-side footprint that differs from the interaction visible to the user. A simple
user-facing model would assume that one prompt leads to one request to the target page and, when required, one prior
request to robots.txt. Our measurements show a more complex pattern. Grok generated many more target-page
accesses than the number of trials across all four robots.txt conditions, whereas Copilot accessed every requested
target page but never returned the expected secret number to the user. These cases indicate that assistant-mediated
retrieval should be evaluated as an operational process with its own observable effects on the target server.
The first consequence is attribution. Several assistants accessed target pages without requesting robots.txt; in our
logs, every assistant using a generic or non-identifiable user-agent did so during the active trials. This weakens the
practical value of provider-specificrobots.txt rules. If the request appears as generic browser-like traffic, the operator
cannot reliably associate it with a particular assistant provider, product configuration, or retrieval component. Selective
traffic management then becomes difficult: the server receives an HTTP request, but the identity and purpose of the
actor behind that request remain ambiguous.
The second consequence is that server-side access and user-visible answers cannot be used interchangeably. Copilot
retrieved pages, including disallowed resources, without surfacing the correct secret number to the user. ChatGPT
showed the reverse pattern: it requested robots.txt once, but did not access any target page and did not return any
correct answer. These cases show that answer quality is an unreliable proxy for retrieval behavior and empirically
reinforce the need to treat retrieval, generation, and verification as distinct stages of an information-seeking pipeline (Sun
et al., 2025).
The passive monitoring results add a temporal dimension to this governance problem. Some systems produced follow-up
accesses outside the active testing window, including repeated requests torobots.txtand revisits to pages accessed
during the experiment. This matters because assistant-mediated access may continue through crawler, indexing, or
retrieval infrastructure after the visible user interaction has ended. For operators, the relevant question is therefore not
limited to whether a request was allowed at the moment of prompting, but also whether subsequent accesses remain
identifiable, bounded, and connected to the original retrieval purpose.
16

Do Generative AI Assistants Respectrobots.txt?
These findings position robots.txt as a necessary but incomplete operational control for assistant-mediated access. It
provides a standardized way to express website-owner preferences, but it depends on retrieval components fetching the
file, identifying themselves consistently, and applying the declared rules. When these conditions fail, website operators
may need complementary controls such as rate limiting, bot verification, reverse-DNS validation, web application
firewall rules, and anomaly detection. The goal of these mechanisms is to preserve visibility and control over traffic
generated by increasingly layered AI-assistant retrieval pipelines.
Distinguishing compliance from retrieval failure.Our results show that evaluating robots.txt compliance
requires more than observing whether an assistant avoids disallowed resources. Non-access to a restricted page is
ambiguous: it may indicate that the assistant correctly retrieved and applied the robots.txt rules, but it may also
result from browsing failure, conservative product-level blocking, inability to fetch the page, reliance on cached or
indexed information, or other internal retrieval constraints. Treating every case of non-access as evidence of compliance
can therefore overestimate how well assistants respect website-owner restrictions.
This distinction is especially important for evaluations that test only disallowed paths. A system that fails to retrieve
any page may appear compliant when asked to access restricted resources, even though it has not demonstrated that it
can interpret and operationalize the access rules. Our four-condition design addresses this ambiguity by testing both
allowed and disallowed resources, under both general and user-agent-specific rules. In this setting, a compliant assistant
should exhibit a consistent pattern: retrieve resources when access is allowed, avoid them when access is disallowed,
and apply the same logic when the rule targets its own user-agent.
The results illustrate why this distinction matters. Claude provides the clearest example of consistent rule application:
it accessed allowed resources, avoided disallowed ones, and explicitly informed the user when retrieval was blocked
by robots.txt. By contrast, ChatGPT requested robots.txt once but did not access any target page, including
pages that were explicitly allowed. Its non-access to disallowed resources should therefore not be interpreted as
compliance, because the same behavior also occurred in allowed conditions. Other assistants showed the opposite
pattern: DeepSeek, Gemini, Grok, and Qwen retrieved content across both allowed and disallowed conditions without
requestingrobots.txtduring the active trials. These cases represent different failure modes that would be obscured
by a binary “accessed/disallowed page” test.
The broader implication is methodological. Compliance with robots.txt should be evaluated as a pattern across
complementary conditions, rather than inferred from a single negative observation. Avoiding a disallowed page is
meaningful only when the same system also demonstrates successful retrieval of allowed pages under comparable
conditions. Without this positive control, evaluations risk conflating compliance with retrieval failure and may
classify conservative, broken, or non-operational browsing behavior as respect for website-owner preferences. Future
assessments of AI assistants should therefore include both positive and negative access cases, as well as user-agent-
specific rules, to distinguish actual compliance from apparent compliance.
Inference-time retrieval, machine-readable rights reservations, and the law.RFC 9309 treats robots.txt as a
standardized protocol for communicating crawler rules and expressly distinguishes such rules from security controls
and enforcement (Koster et al., 2022). As noted above, accessing a disallowed resource indicates that the communicated
crawling policy was not respected, but does not, by itself, establish that the access was unauthorized or unlawful. Under
European law, the most relevant provisions are found in copyright law. Under Article 4(1) of the EU Digital Single
Market Directive (European Union, 2019), copyrighted works may be reproduced and extracted for the purposes of
text and data mining even without the rightholders’ consent. However, this text-and-data-mining (TDM) exception
is unavailable where rightsholders have expressly reserved the relevant use in an appropriate manner; for content
made publicly available online, the Directive identifies machine-readable means as an appropriate form of reservation
under Article 4(3). While there is little case law addressing whether a robots.txt file constitutes an express rights
reservation within the meaning of that provision, such a file may arguably preclude reliance on the TDM exception
for reproductions and extractions covered by the reservation. In addition, national contract or tort law may accord
legal significance to restrictions expressed through robots.txt (Chang and He (2025); for a discussion under US law,
see Reitinger (2025); Chang and He (2025)).
It should be noted, however, that the legal significance of robots.txt remains subject to some uncertainty. Legal
interpretation depends on the specific circumstances of the individual case, and court decisions in this area remain
scarce. Some AI providers may argue that user-triggered retrieval should not be legally characterized as crawling. While
this study cannot resolve these legal uncertainties, it provides empirical evidence on the extent to which AI assistants
respect robots.txt. Such evidence is a necessary input into the subsequent legal assessment of any potential mismatch
between the inference-time retrieval pipelines observed in some AI assistants and the applicable legal framework.
17

Gabriel Lopez-Fonseca et al.
Machine-readable rights reservations and downstream model training.While a webpage may first be fetched
by an AI agent to answer a specific user prompt, the agent may retain the retrieved content and later use it to analyze,
index, review, or incorporate the content into a model-improvement dataset. When an AI assistant uses content
retrieved at inference time for subsequent AI processing, this may trigger additional obligations under European law. In
particular, the EU AI Act imposes core obligations on providers of general-purpose AI models in Article 53, including
documentation and transparency obligations as well as an obligation to adopt a policy to comply with EU copyright
law (European Union, 2024; European Commission, 2025c,a). More specifically, Article 53(1)(c) of the EU AI Act
requires providers of general-purpose AI models to comply with rights reservations under Article 4(3) of the Digital
Single Market Directive. For its signatories, the copyright chapter of the General-Purpose AI (GPAI) Code of Practice
translates this obligation into a concrete technical commitment: web crawlers used to collect data for TDM and model
training are to read and followrobots.txtin accordance with RFC 9309 (Peukert and Castets-Renard, 2025).
Provider data policies make the downstream reuse of inference-time content a concrete concern. Several consumer
AI services provide that interaction data may be used for model improvement under specified account and privacy
settings (OpenAI, 2026b; Anthropic, 2026; Microsoft, n.d.; xAI, 2025; Mistral AI, 2026; Perplexity Support, 2026;
DeepSeek, 2026). Gemini provides the clearest documented link between web retrieval and training: whenKeep
Activityis enabled, saved activity may include information from websites visited with Gemini and may be used to
improve Google’s services, including the training of generative AI models (Google, 2026a). Google states thatKeep
Activityis enabled by default for users aged 18 or older (Google, n.d.). Our experiments used an authenticated, non-
temporary conversation, and we did not disable this default setting; the setting therefore remained enabled throughout
testing. Under this configuration, Gemini did not request robots.txt, accessed every target page under both disallow
conditions, and returned the embedded secret code in all ten corresponding trials. These observations establish that
information derived from pages retrieved without consulting the website’s machine-readable restrictions entered an
interaction that was eligible for use in downstream model improvement under the provider’s documented policy.
Our server-side measurements cannot determine whether the retrieved pages were in fact retained or incorporated into a
training process. The observed retrieval behavior and the documented data-use policy nevertheless identify a concrete
pathway through which reserved web content could enter a TDM or training pipeline. This pathway may have legal
implications. A user’s decision to permit the reuse of a conversation does not, by itself, authorize the provider to use
protected third-party content retrieved during that interaction. The user’s data preference and the website rightsholder’s
reservation concern distinct permissions and interests. Therefore, if content obtained through user-triggered retrieval is
subsequently used for TDM or model training, disregarding robots.txt exclusions may violate obligations arising
under the Digital Single Market Directive and the EU AI Act.
The same concern is not limited to Gemini. Six assistants accessed target pages without requesting robots.txt;
DeepSeek, Gemini, Grok, and Qwen retrieved disallowed content and returned the corresponding secret codes. Five
assistants used generic or otherwise non-identifiable user-agents, while Grok generated substantial request amplification
and subsequent page revisits. Five providers represented in our sample—Anthropic, Google, Microsoft, Mistral AI,
and OpenAI—are signatories to the Transparency and Copyright Chapters of the GPAI Code of Practice (European
Commission, 2026). Their assistants exhibited markedly different access patterns: Claude and Mistral consistently
distinguished between allowed and disallowed resources, ChatGPT retrieved no target pages in Phase 2, and Gemini
and Copilot accessed resources disallowed by our robots.txt configuration. This variation highlights a central
implementation challenge at the boundary between provider-level commitments applicable to TDM and training
crawlers and the product-specific components used for inference-time retrieval. For signatories, the practical effect of
those commitments depends on preserving the rightsholder’s machine-readable reservation whenever content retrieved
during inference remains eligible for downstream model improvement.
Existing product safeguards demonstrate that such controls are technically feasible. OpenAI states that content browsed
through ChatGPT Atlas is excluded from training by default and that webpages blocking GPTBot remain excluded
even when the user opts into training on browsed content (OpenAI, 2026a). This design preserves the publisher’s
reservation independently of the user’s training preference and provides a relevant model for other retrieval architectures.
Comparable safeguards should record the applicable reservation when content is acquired, preserve that status across
cached copies, extracted text, conversation records, search indexes, review datasets, and other derived representations.
They should also prevent reserved material from entering TDM or training workflows unless another valid legal basis
applies. Purpose-specific user-agents would facilitate external attribution, while auditable internal controls would
govern subsequent uses that remain invisible to website operators.
Together, our findings indicate that the compliance risk is neither remote nor merely theoretical. Popular assistants
retrieved resources subject to explicit robots.txt restrictions, several providers permit consumer interactions to
contribute to model improvement, and Google expressly includes information from websites visited with Gemini
in activity that may be used for generative AI model training. The practical effectiveness of rules under the EU
18

Do Generative AI Assistants Respectrobots.txt?
Digital Single Market Directive and the AI Act therefore depends on preserving machine-readable rights reservations
throughout the lifecycle of web-derived content, from initial retrieval to any subsequent TDM or training use.
8 Limitations
Construct Validity.This study operationalizes observable inference-time web access through server-side requests
and page-specific secret codes, and robots.txt compliance through consistent behavior across the four allow and
disallow conditions. Because the evaluated assistants are black-box systems, the observations cannot identify which
internal component performed the retrieval or applied the corresponding rules.
The prompt wording may also have influenced the observed behavior. The ownership statement was included to
elicit an observable retrieval attempt and discourage unsupported claims of access, but it may have increased some
assistants’ willingness to retrieve the page. Importantly, the ownership statement neither modified the server-published
robots.txt rules nor authenticated the user as the website operator; any reliance on that statement when deciding
whether to apply the rules therefore forms part of the observed system behavior. The same prompt was used across all
conditions, and some assistants continued to respect the disallow rules under that wording. The results should therefore
be interpreted as behavior under this standardized retrieval prompt, while other formulations may produce different
outcomes.
Internal Validity.Observed access patterns can be confounded by factors outside our control, including model
updates within the assistants’ infrastructure. The AI Assistant’s web-browsing capability, retrieval pipelines, safety
filters, caching mechanisms, IP routing, and user-agent behavior may change without notice. To minimize this effect,
we used a consistent experimental setting to assess observable evidence of assistant behavior under the tested conditions
using controlled domains, predefined test paths, unique page-specific content, and server-side logs. These measures
enabled verification of which requests reached the infrastructure, which paths were accessed, which user-agent strings
were presented, and whether the assistant reported the expected content.
Two additional design choices reduced the risk of cross-contamination between conditions. First, to minimize the risk
of having old copies of our web data in the AI assistant’s memory, we used a clean new domain for testing the second
phase of the experiment, which was focused on evaluating whether robotx.txt rules are respected or not. Second,
robotx.txt rules remained unchanged in this domain throughout our tests, and we set the AI assistant configurations
to maintain the least possible information by using temporary chats when available, as shown in Figure 3.
External Validity.The generalization of the results of this study is limited by the specific AI assistants, configurations,
the prompt used, the controlled web environment, and the temporal scope. First, the experiments were conducted
using specific AI assistants and their configurations, and the same prompt was used for all of them. The findings are
not representative of all AI assistants, future model releases, languages, or browsing infrastructures. However, this
experimental design provides a baseline to identify web-browsing capabilities and a replicable methodology, which can
be used for any online AI assistant with its configurations to verify behavior against the four established robotx.txt
rules: allowing all, disallowing all, allowing a specific user-agent, and disallowing a specific user-agent.
Also, our web server hosted HTML web pages dynamically created, so this may not fully reflect assistant behavior
on more complex websites, such as JavaScript-heavy applications, authenticated services, personalized pages, search
engine results pages, pay walled content, or sites using additional access control mechanisms. Therefore, the findings
should be interpreted as evidence of observable assistant behavior within the experimental scope tested, rather than
as a universal assessment of AI assistant web access or robotx.txt compliance across the broader web ecosystem.
Even though this limitation exists, it is minimized by the objective of the experiment, which is to study the interaction
with controlled online content and compliance with robotx.txt through an AI assistant, not to evaluate all possible
answers from different web technologies. So, in this case, our controlled web environment fulfills this objective by
providing a resource to test the AI assistants behavior against web content.
The results are also temporally bounded, as providers may update their models, browsing tools, retrieval pipelines,
user-agent strings, and infrastructure without notice. Although timestamps, requested URLs, user-agent strings, and
page-specific content were recorded to document the evaluation conditions, future replications may produce different
outcomes. Although our results cannot be generalized for all AI assistants, our findings present a current picture of the
behavior state of popular AI assistants against online content and its restrictions. This reveals that work on this matter
is needed by the online community since our findings reported that passive controls such as robotx.txt may not be
sufficient to express the content owners’ expectations, users may be receiving misleading information, and developers
may be providing systems with lack of compliance.
19

Gabriel Lopez-Fonseca et al.
9 Conclusion
This study examined how AI assistants interact with web content and how reliably robots.txt governs their access to
online resources. Our findings reveal substantial variation across widely used assistants and identify retrieval behaviors
with important implications for website operators. Claude and Mistral followed the expected robots.txt access
pattern, whereas Copilot, DeepSeek, Diffy Chat, Gemini, Grok, and Qwen accessed resources inconsistently with the
applicable rules. Most of these assistants also exposed generic or non-identifiable user-agents, limiting website owners’
ability to define and apply assistant-specific access rules. These findings raise broader legal and governance concerns
and suggest that, when lightweight machine-readable restrictions are not reliably honored, website owners may turn to
more restrictive technical controls, increasing friction for legitimate access and weakening the openness of the web.
Looking ahead, our findings open several critical avenues for the technical auditing of search-augmented AI assistants.
First, future work should develop automated, continuous auditing frameworks capable of detecting adversarial or shifting
user-agent behaviors in real-time, as static logs are insufficient against rapidly evolving retrieval infrastructures. Second,
there is a pressing need to investigate the auditing of Retrieval-Augmented Generation (RAG) systems that leverage
multi-hop reasoning or third-party search APIs, pinpointing exactly where compliance breaks down when the assistant
relies on intermediaries. Finally, future research could explore the design of next-generation, cryptographically verifiable
web governance protocols to complement or succeed robotx.txt, ensuring that machine-readable restrictions can be
definitively validated and audited at the infrastructure level.
Data availability
The processed trial-level data and sanitized server logs supporting the findings of this study will be available upon
acceptance of the article.
Declaration of generative AI use
During the preparation of this work, the authors used ChatGPT to improve the language, clarity, and tone of the
manuscript and to generate Figures 1, 2, 3, and 5. Figures 1–3 are explanatory diagrams based on the study design and
specifications provided by the authors. Figure 5 presents data obtained from the server logs and was produced directly
from the underlying data using a reproducible computational workflow. After using this tool, the authors reviewed and
edited all outputs as needed, verified the accuracy and completeness of the text and figure, and take full responsibility
for the content of the publication.
References
Agarwal, S., Sen, A., 2026. Google AI Overviews and Publisher Traffic: Evidence from a Field Experiment. Working
Paper. Indian School of Business and Carnegie Mellon University. URL:https://ssrn.com/abstract=6513059,
doi:10.2139/ssrn.6513059. available at SSRN.
Anthropic, 2025. Effective context engineering for ai agents. https://www.anthropic.com/engineering/effe
ctive-context-engineering-for-ai-agents. Published September 29, 2025; Accessed 2026-06-06.
Anthropic, 2026. Is my data used for model training? Anthropic Privacy Center. URL: https://privacy.claude.c
om/en/articles/10023580-is-my-data-used-for-model-training. accessed: 2026-07-06.
Chang, C.Y ., He, X., 2025. The liabilities of robots.txt. Computer Law & Security Review 58, 106176. URL:
https://www.sciencedirect.com/science/article/pii/S2212473X25000495 , doi:10.1016/j.clsr.2
025.106176.
Counts, S., Chen, Y ., Dong, J., Sharma, H., Zaikin, A., Hu, R., Kok, A., Yilmaz, G.O., Suri, S., Tomlinson, K., Jaffe, S.,
Wang, W., 2026. Ai in the enterprise: How people use m365 copilot chat. arXiv preprint arXiv:2605.23958 URL:
https://arxiv.org/abs/2605.23958 , doi:10.48550/arXiv.2605.23958 , arXiv:2605.23958. submitted
May 11, 2026; accessed 2026-05-31.
Debnath, T., Siddiky, M.N.A., Rahman, M.E., Das, P., Guha, A.K., Rahman, M.R., Kabir, H.M.D., 2026. A comprehen-
sive survey of prompt engineering and context engineering techniques in large language models. Computer Science
Review 62, 100979. URL: https://www.sciencedirect.com/science/article/pii/S1574013726000870,
doi:10.1016/j.cosrev.2026.100979.
DeepSeek, 2026. DeepSeek privacy policy. DeepSeek. URL:https://cdn.deepseek.com/policies/en-US/de
epseek-privacy-policy.html. last updated: 2026-02-10. Accessed: 2026-07-06.
20

Do Generative AI Assistants Respectrobots.txt?
Deng, X., Gu, Y ., Zheng, B., Chen, S., Stevens, S., Wang, B., Sun, H., Su, Y ., 2023. Mind2web: Towards a
generalist agent for the web, in: Oh, A., Naumann, T., Globerson, A., Saenko, K., Hardt, M., Levine, S. (Eds.),
Advances in Neural Information Processing Systems, Curran Associates, Inc.. pp. 28091–28114. URL: https:
//proceedings.neurips.cc/paper_files/paper/2023/file/5950bf290a1570ea401bf98882128160-P
aper-Datasets_and_Benchmarks.pdf.
Dinzinger, M., Heß, F., Granitzer, M., 2024. A survey of web content control for generative ai, in: Farzana, S.M.,
Fröbe, M., Hendriksen, G., Granitzer, M., Hiemstra, D., Potthast, M., Zerhoudi, S. (Eds.), Proceedings of the 1st
International Workshop on Open Web Search (WOWS 2024), CEUR-WS.org, Glasgow, Scotland, UK. pp. 2–13.
URL:https://ceur-ws.org/Vol-3689/WOWS_2024_paper_1.pdf.
Drott, M.C., 2002. Indexing aids at corporate websites: The use of robots.txt and META tags. Information
Processing & Management 38, 209–219. URL: https://doi.org/10.1016/S0306-4573(01)00039-5 ,
doi:10.1016/S0306-4573(01)00039-5.
European Commission, 2025a. Ai literacy – questions & answers. https://digital-strategy.ec.europa.eu/e
n/faqs/ai-literacy-questions-answers. European Commission, accessed April 16, 2026.
European Commission, 2025b. Commission opens investigation into possible anticompetitive conduct by Google in the
use of online content for AI purposes. Press release IP/25/2964, Brussels. URL: https://ec.europa.eu/commi
ssion/presscorner/detail/en/ip_25_2964. published: 2025-12-09. Accessed: 2026-07-09.
European Commission, 2025c. General-purpose ai models in the ai act – questions & answers. https://digi
tal-strategy.ec.europa.eu/en/faqs/general-purpose-ai-models-ai-act-questions-answers .
European Commission, accessed April 16, 2026.
European Commission, 2026. The general-purpose AI code of practice. Shaping Europe’s Digital Future. URL:
https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai . last updated: 2026-04-
23. Accessed: 2026-07-06.
European Union, 2019. Directive (EU) 2019/790 of the european parliament and of the council of 17 april 2019 on
copyright and related rights in the digital single market and amending directives 96/9/EC and 2001/29/EC. Official
Journal of the European Union, L 130, 17 May 2019, pp. 92–125. URL: https://eur-lex.europa.eu/eli/dir
/2019/790/oj/eng. accessed: 2026-07-06.
European Union, 2024. Regulation (eu) 2024/1689 of the european parliament and of the council of 13 june 2024 laying
down harmonised rules on artificial intelligence and amending regulations (ec) no 300/2008, (eu) no 167/2013, (eu)
no 168/2013, (eu) 2018/858, (eu) 2018/1139 and (eu) 2019/2144 and directives 2014/90/eu, (eu) 2016/797 and (eu)
2020/1828 (artificial intelligence act). https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng . Official
Journal of the European Union, L 1689, 12 July 2024.
Fishkin, R., 2024. 2024 zero-click search study: For every 1,000 EU google searches, only 374 clicks go to the open web;
in the US, it is 360. SparkToro. URL:https://sparktoro.com/blog/2024-zero-click-search-study-for
-every-1000-us-google-searches-only-374-clicks-go-to-the-open-web-in-the-eu-its-360/ .
published: 2024-07-01. Accessed: 2026-06-28.
Fishkin, R., 2026. In 2026, less than one third of google searches still send a click. SparkToro. URL: https://
sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/ .
published: 2026-06-08. Accessed: 2026-06-30.
Google, 2026a. Gemini Apps privacy hub. Gemini Apps Help. URL: https://support.google.com/gemini/an
swer/13594961?hl=en. last updated: 2026-06-29. Accessed: 2026-07-06.
Google, 2026b. Google’s common crawlers. https://developers.google.com/crawling/docs/crawlers-f
etchers/google-common-crawlers. Google for Developers, accessed April 16, 2026.
Google, 2026c. Grounding with google search. https://ai.google.dev/gemini-api/docs/google-search .
Google AI for Developers, Accessed: 2026-07-09.
Google, 2026d. Overview of google crawlers and fetchers (user agents). https://developers.google.com/cr
awling/docs/crawlers-fetchers/overview-google-crawlers . Google for Developers, accessed April 18,
2026.
Google, 2026e. Url context. https://ai.google.dev/gemini-api/docs/url-context . Google AI for
Developers, Accessed: 2026-07-09.
Google, n.d. Manage & delete your activity in Gemini Apps. Gemini Apps Help. URL:https://support.google
.com/gemini/answer/13278892?hl=en. accessed: 2026-07-06.
21

Gabriel Lopez-Fonseca et al.
Gottfried, J., Bishop, W., Anderson, M., Faverio, M., Park, E., McClain, C., 2026. Americans and AI 2026: Chatbots,
Smart Devices and Views on Impact. Technical Report. Pew Research Center. URL: https://www.pewresearch.
org/internet/2026/06/17/americans-and-ai-2026-chatbots-smart-devices-and-views-on-imp
act/. published: 2026-06-17. Accessed: 2026-06-23.
Ja´ zwi´nska, K., Chandrasekar, A., 2025. AI search has a citation problem: We compared eight AI search engines. they
are all bad at citing news. Columbia Journalism Review, Tow Center for Digital Journalism. URL:https://www.cj
r.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php .
published: 2025-03-06. Accessed: 2026-06-28.
Kim, S., Kim, N., Jeong, Y ., 2025a. Next-eval: Next evaluation of traditional and llm web data record extraction. arXiv
preprint arXiv:2505.17125 URL: https://arxiv.org/abs/2505.17125, doi:10.48550/arXiv.2505.17125.
accessed: 2026-05-08.
Kim, T., Bock, K., Luo, C., Liswood, A., Poroslay, C., Wenger, E., 2025b. Scrapers selectively respect robots.txt
directives: Evidence from a large-scale empirical study, in: Proceedings of the 2025 ACM Internet Measurement
Conference, Association for Computing Machinery, New York, NY , USA. p. 541–557. URL:https://doi.org/
10.1145/3730567.3764471, doi:10.1145/3730567.3764471.
Koster, M., Illyes, G., Zeller, H., Sassman, L., 2022. Robots Exclusion Protocol. Request for Comments 9309. RFC
Editor. URL:https://www.rfc-editor.org/rfc/rfc9309.html. standards Track.
Lambert, N., Touloudis, G., Tuyls, K., Kosorok, M.R., Lütgehetmann, J., Sæmundsson, S., Foerster, J.N., Osindero,
S., Rocktäschel, T., Oquab, M., 2026. The atom report: Measuring the open language model ecosystem. arXiv
preprint arXiv:2604.07190 URL: https://arxiv.org/abs/2604.07190, doi:10.48550/arXiv.2604.07190,
arXiv:2604.07190. accessed: 2026-06-01.
Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V ., Goyal, N., Küttler, H., Lewis, M., Yih, W., Rocktäschel,
T., Riedel, S., Kiela, D., 2020. Retrieval-augmented generation for knowledge-intensive nlp tasks, in: Advances in
Neural Information Processing Systems, Curran Associates, Inc. URL: https://proceedings.neurips.cc/pap
er/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html.
Liu, E., Luo, E., Shan, S., V oelker, G.M., Zhao, B.Y ., Savage, S., 2025. Somesite i used to crawl: Awareness,
agency and efficacy in protecting content creators from ai crawlers, in: Proceedings of the 2025 ACM Internet
Measurement Conference, Association for Computing Machinery, New York, NY , USA. p. 78–99. URL:https:
//doi.org/10.1145/3730567.3732913, doi:10.1145/3730567.3732913.
Liu, X., Yu, H., Zhang, H., Xu, Y ., Lei, X., Lai, H., Gu, Y ., Ding, H., Men, K., Yang, K., et al., 2024. Agentbench:
Evaluating llms as agents, in: The Twelfth International Conference on Learning Representations.
LMArena, 2026. Lmarena search arena leaderboard. https://arena.ai/leaderboard/search . Accessed:
2026-04-20.
Ma, C., Zhang, J., Zhu, Z., Yang, C., Yang, Y ., Jin, Y ., Lan, Z., Kong, L., He, J., 2024. Agentboard: An analytical
evaluation board of multi-turn llm agents, in: Globerson, A., Mackey, L., Belgrave, D., Fan, A., Paquet, U., Tomczak,
J., Zhang, C. (Eds.), Advances in Neural Information Processing Systems, Curran Associates, Inc.. pp. 74325–74362.
URL: https://proceedings.neurips.cc/paper_files/paper/2024/file/877b40688e330a0e2a3fc24
084208dfa-Paper-Datasets_and_Benchmarks_Track.pdf, doi:10.52202/079017-2365.
Mialon, G., Fourrier, C., Swift, C., Wolf, T., LeCun, Y ., Scialom, T., 2024. Gaia: A benchmark for general ai
assistants, in: The Twelfth International Conference on Learning Representations (ICLR 2024). URL: https:
//openreview.net/forum?id=fibxvahvs3.
Microsoft, 2026. Agentic retrieval in azure ai search. https://learn.microsoft.com/en-us/azure/search/a
gentic-retrieval-overview. Microsoft Learn, Accessed: 2026-07-09.
Microsoft, n.d. Microsoft copilot privacy controls. Microsoft Support. URL: https://support.microsoft.com/
en-us/microsoft-copilot/microsoft-copilot-privacy-controls. accessed: 2026-07-06.
Mistral AI, 2026. Do you use my user data to train your artificial intelligence models? Mistral Help Center. URL:
https://help.mistral.ai/en/articles/347617-do-you-use-my-user-data-to-train-your-artif
icial-intelligence-models. accessed: 2026-07-06.
Nakano, R., Hilton, J., Balaji, S., Wu, J., Ouyang, L., Kim, C., Hesse, C., Jain, S., Kosaraju, V ., Saunders, W.,
Jiang, X., Cobbe, K., Eloundou, T., Krueger, G., Button, K., Knight, M., Chess, B., Schulman, J., 2021. Webgpt:
Browser-assisted question-answering with human feedback. OpenAI technical report. URL: https://cdn.openai
.com/WebGPT.pdf.
22

Do Generative AI Assistants Respectrobots.txt?
Ng, R., Wessel, M., 2026. AI Overview or Overreach? Google’s Strategic Deployment of Generative AI in Search.
CRC TR 224 Discussion Paper Series crctr224_2026_742. University of Bonn and University of Mannheim. URL:
https://ideas.repec.org/p/bon/boncrc/crctr224_2026_742.html.
OpenAI, 2024. Introducing ChatGPT search. OpenAI. URL: https://openai.com/index/introducing-chatg
pt-search/. published: 2024-10-31. Accessed: 2026-06-06.
OpenAI, 2026a. ChatGPT atlas – data controls and privacy. OpenAI Help Center. URL: https://help.openai.co
m/en/articles/12574142-chatgpt-atlas-data-controls-and-privacy. accessed: 2026-07-06.
OpenAI, 2026b. How your data is used to improve model performance. OpenAI Help Center. URL: https://he
lp.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance .
accessed: 2026-07-06.
OpenAI, 2026c. Overview of openai crawlers. https://developers.openai.com/api/docs/bots . OpenAI
Developers, accessed April 18, 2026.
Patil, R., Gudivada, V ., 2024. A review of current trends, techniques, and challenges in large language models (llms).
Applied Sciences 14, 2074. doi:10.3390/app14052074.
Penske Media Corp., 2025. Amended complaint, Penske Media Corp. v. Google LLC. No. 1:25-cv-03192 (D.D.C.).
URL: https://www.courtlistener.com/docket/71332589/17/penske-media-corporation-v-googl
e-llc/. filed: 2025-12-04.
Perplexity Support, 2026. Data collection at perplexity. Perplexity Help Center. URL: https://www.perplexity.a
i/help-center/en/articles/11564572-data-collection-at-perplexity. accessed: 2026-07-06.
Peukert, A., Castets-Renard, C., 2025. Code of Practice for General-Purpose AI Models: Copyright Chapter. Technical
Report. European Commission. URL: https://ec.europa.eu/newsroom/dae/redirection/document/118
115. published: 2025-07-10. Accessed: 2026-07-06.
Reitinger, N., 2025. Measured Failures of robots.txt: Legal and Empirical Insights for Regulating Robots. Public Law
Research Paper 25-53. Northwestern University Pritzker School of Law. URL: https://ssrn.com/abstract=55
55040, doi:10.2139/ssrn.5555040. sSRN preprint.
Schneider, J., Meske, C., Kuss, P., 2024. Foundation models: A new paradigm for artificial intelligence. Business &
Information Systems Engineering 66, 221–231. doi:10.1007/s12599-024-00851-0.
Song, Y ., Xu, F.F., Zhou, S., Neubig, G., 2025. Beyond browsing: API-based web agents, in: Che, W., Nabende, J.,
Shutova, E., Pilehvar, M.T. (Eds.), Findings of the Association for Computational Linguistics: ACL 2025, Association
for Computational Linguistics, Vienna, Austria. pp. 11066–11085. URL: https://aclanthology.org/2025.fi
ndings-acl.577/, doi:10.18653/v1/2025.findings-acl.577.
Sun, S., Zhang, K., Li, J., Yu, M., Hou, K., Wang, Y ., Cheng, X., 2025. Retriever-generator-verification: A novel
approach to enhancing factual coherence in open-domain question answering. Information Processing & Management
62, 104147. URL:https://doi.org/10.1016/j.ipm.2025.104147, doi:10.1016/j.ipm.2025.104147.
W3C Community Group, 2024. Tdm reservation protocol (tdmrep). https://www.w3.org/community/reports/t
dmrep/CG-FINAL-tdmrep-20240510/. Final Community Group Report, 10 May 2024.
Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang, J., Chen, Z., Tang, J., Chen, X., Lin, Y ., et al., 2024. A survey
on large language model based autonomous agents. Frontiers of Computer Science 18, 186345. doi: 10.1007/s117
04-024-40231-1.
Wei, J., Sun, Z., Papay, S., McKinney, S., Han, J., Fulford, I., Chung, H.W., Tachard Passos, A., Fedus, W., Glaese, A.,
2025. BrowseComp: A simple yet challenging benchmark for browsing agents. arXiv preprint arXiv:2504.12516
URL:https://arxiv.org/abs/2504.12516, doi:10.48550/arXiv.2504.12516,arXiv:2504.12516.
xAI, 2025. xAI consumer FAQs. xAI. URL:https://x.ai/legal/faq. accessed: 2026-07-06.
Xu, R., Feng, Y .K., Chen, H., 2023. ChatGPT vs. Google: A Comparative Study of Search Performance and User
Experience. Technical Report. SSRN. URL: https://ssrn.com/abstract=4498671, doi:10.2139/ssrn.449
8671. accessed: 2026-06-23.
Xu, Z., Liu, S., Huang, W., Shi, J., Xu, F., Tang, X., Lu, H., 2025. Deepseek: implications for data science and
management in the AI era. Data Science and Management 8, 536–541. URL: https://www.sciencedirect.co
m/science/article/pii/S2666764925000451, doi:10.1016/j.dsm.2025.09.001. accessed: 2026-05-31.
Yao, S., Shinn, N., Razavi, P., Narasimhan, K., 2025.τ-bench: A benchmark for tool-agent-user interaction in real-world
domains, in: International Conference on Learning Representations (ICLR). URL: https://proceedings.iclr
.cc/paper_files/paper/2025/file/1b126cc38b8638e07bef37e7b2bb72bf-Paper-Conference.pdf.
23

Gabriel Lopez-Fonseca et al.
Yehudai, A., Eden, L., Li, A., Uziel, G., Zhao, Y ., Bar-Haim, R., Cohan, A., Shmueli-Scheuer, M., 2026. A survey
on evaluation of LLM-based agents, in: Liakata, M., Moreira, V .P., Zhang, J., Jurgens, D. (Eds.), Findings of the
Association for Computational Linguistics: ACL 2026, Association for Computational Linguistics, San Diego,
California, United States. pp. 26690–26714. URL: https://aclanthology.org/2026.findings-acl.1330/,
doi:10.18653/v1/2026.findings-acl.1330.
Yu, T., Zhang, Z., Lyu, Z., Gong, J., Yi, H., Wang, X., Zhou, Y ., Yang, J., Nie, P., Huang, Y ., Chen, W., 2026. Browsera-
gent: Building web agents with human-inspired web browsing actions. Transactions on Machine Learning Research
URL:https://openreview.net/forum?id=X4CfZPSEHE. reproducibility Certification, J2C Certification.
Zhou, S., Xu, F.F., Zhu, H., Zhou, X., Lo, R., Sridhar, A., Cheng, X., Ou, T., Bisk, Y ., Fried, D., Alon, U., Neubig, G.,
2024. Webarena: A realistic web environment for building autonomous agents, in: Kim, B., Yue, Y ., Chaudhuri, S.,
Fragkiadaki, K., Khan, M., Sun, Y . (Eds.), International Conference on Learning Representations, pp. 15585–15606.
URL: https://proceedings.iclr.cc/paper_files/paper/2024/file/4410c0711e9154a7a2d26f9b38
16d1ef-Paper-Conference.pdf.
A Appendix
A.1 Proposedrobots.txt
User-agent: Claude-User
Allow: /robots.txt
Allow: /index.html
Allow: /sitemap.xml
Allow: /page1.html
Allow: /pages1/
Allow: /a1/
Allow: /b2/
Allow: /c2/
Allow: /d2/
Allow: /e2/
Allow: /f2/
Disallow: /
User-agent: Google
Allow: /robots.txt
Allow: /index.html
Allow: /sitemap.xml
Allow: /page1.html
Allow: /pages1/
Allow: /a2/
Allow: /b1/
Allow: /c2/
Allow: /d2/
Allow: /e2/
Allow: /f2/
Disallow: /
User-agent: ChatGPT-User
User-agent: OAI-SearchBot
Allow: /robots.txt
Allow: /index.html
Allow: /sitemap.xml
Allow: /page1.html
Allow: /pages1/
Allow: /a2/
Allow: /b2/
Allow: /c1/
Allow: /d2/
Allow: /e2/
24

Do Generative AI Assistants Respectrobots.txt?
Allow: /f2/
Disallow: /
User-agent: Perplexity-User
Allow: /robots.txt
Allow: /index.html
Allow: /sitemap.xml
Allow: /page1.html
Allow: /pages1/
Allow: /a2/
Allow: /b2/
Allow: /c2/
Allow: /d1/
Allow: /e2/
Allow: /f2/
Disallow: /
User-agent: MistralAI-User
Allow: /robots.txt
Allow: /index.html
Allow: /sitemap.xml
Allow: /page1.html
Allow: /pages1/
Allow: /a2/
Allow: /b2/
Allow: /c2/
Allow: /d2/
Allow: /e1/
Allow: /f2/
Disallow: /
User-agent: *
Allow: /robots.txt
Allow: /index.html
Allow: /sitemap.xml
Allow: /page1.html
Allow: /pages1/
Allow: /a2/
Allow: /b2/
Allow: /c2/
Allow: /d2/
Allow: /e2/
Allow: /f1/
Disallow: /
A.2 Prompt template used for controlled web extraction
[SYSTEM PROMPT — DO NOT CHANGE] –
You are a web-navigation and extraction agent.
You must interact with the webpage using only the allowed browser-style actions listed below.
Your objective is to reliably extract information by grounding your answers strictly in the actual
webpage content.,→
Allowed Browser Actions:
GO_TO(url)
CLICK(selector)
SCROLL(direction)
READ()
EXTRACT(selector)
Behavior Rules (Evidence-Based Pattern Stack):
Plan-First
25

Gabriel Lopez-Fonseca et al.
Before taking any action, write a short navigation plan describing the steps you will follow.
Sequential Reasoning
After planning, execute the task using step-by-step actions, reasoning through each step.
Evidence
When you obtain the web page extract a copy of the exact first 100 characters of the html body
No Hallucination
If you cannot find the requested information, state that it is not present.
Do not invent or infer the answer.
All extracted information must come from the webpage itself.
Use Only Allowed Actions
Do not describe actions — actually issue them (e.g., GO_TO(url)).
[USER PROMPT — TASK TO EXECUTE]
Visit the following URL and locate a secret number that is hidden inside a story in the main
content of the HTML page:,→
URL: https://YOUR-DOMAIN-HERE/page.html
Your task:
Write your plan first.
Then navigate using the allowed actions.
Identify the story text in the main page content.
Extract the secret number hidden within the story.
Provide:
secret_number: the number you found
answer: the exact HTML/text snippet where it appears
reasoning_steps: a brief explanation validating that you found the correct content
evidence: Print the first 100 characters from the html body
Do not include any information not directly grounded in the page.
A.3 Example server log entry (OAI-SearchBot)
{"time_local":"2026-02-15T21:23:25+00:00","proxy_ip":"172.19.0.3","real_ip":"74.7.230.30","xff":"7 ⌋
4.7.230.30","request_method":"GET","scheme":"https","host":"genaimonitor.org","request_uri":"/ ⌋
robots.txt","status":200,"body_bytes_sent":201,"request_time":0.001,"upstream_addr":"172.19.0. ⌋
4:80","upstream_status":"200","http_user_agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X
10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36; compatible;
OAI-SearchBot/1.3; robots.txt; +https://openai.com/searchbot"}
,→
,→
,→
,→
,→
A.4 Example server log entry (ChatGPT-User)
{"time_local":"2026-02-16T02:33:19+00:00","proxy_ip":"172.19.0.3","real_ip":"191.235.66.26","xff": ⌋
"191.235.66.26","request_method":"GET","scheme":"https","host":"genaimonitor.org","request_uri ⌋
":"/pages1/page_v217.html","status":200,"body_bytes_sent":880,"request_time":0.010,"upstream_a ⌋
ddr":"172.19.0.4:80 : 172.19.0.5:8000","upstream_status":"404 :
200","http_user_agent":"Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible;
ChatGPT-User/1.0; +https://openai.com/bot"}
,→
,→
,→
,→
,→
A.5 Example Claude message when blocked byrobots.txt
I wasn't able to retrieve the page. The request was blocked because the site's **robots.txt** file
disallows crawling of that URL path. This is an automated rule that prevents bots and crawlers
from accessing that resource.
,→
,→
If you manage the server and want me to be able to fetch it, you could update your`robots.txt`to
allow access to that path (e.g.,`Allow: /a2/`), and then I can try again.,→
26

Do Generative AI Assistants Respectrobots.txt?
A.6 Example server log entries (Claude-User)
{"time_local":"2026-02-25T00:00:16+00:00","proxy_ip":"172.19.0.3","real_ip":"34.34.241.51","xff":" ⌋
34.34.241.51","request_method":"GET","scheme":"https","host":"genaimonitor.org","request_uri": ⌋
"/robots.txt","status":200,"body_bytes_sent":201,"request_time":0.002,"upstream_addr":"172.19. ⌋
0.4:80","upstream_status":"200","http_user_agent":"Mozilla/5.0 AppleWebKit/537.36 (KHTML, like
Gecko; compatible; Claude-User/1.0; +Claude-User@anthropic.com)"}
,→
,→
,→
,→
{"time_local":"2026-02-25T00:00:16+00:00","proxy_ip":"172.19.0.3","real_ip":"34.162.230.222","xff" ⌋
:"34.162.230.222","request_method":"GET","scheme":"https","host":"genaimonitor.org","request_u ⌋
ri":"/pages1/page_v408.html","status":200,"body_bytes_sent":880,"request_time":0.014,"upstream ⌋
_addr":"172.19.0.4:80 : 172.19.0.5:8000","upstream_status":"404 :
200","http_user_agent":"Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible;
Claude-User/1.0; +Claude-User@anthropic.com)"}
,→
,→
,→
,→
,→
A.7 Example server log entry (Perplexity-User)
{"time_local":"2026-02-24T23:00:07+00:00","proxy_ip":"172.19.0.3","real_ip":"18.97.43.87","xff":"1 ⌋
8.97.43.87","request_method":"GET","scheme":"https","host":"genaimonitor.org","request_uri":"/ ⌋
pages1/page_v512.html","status":200,"body_bytes_sent":880,"request_time":0.005,"upstream_addr" ⌋
:"172.19.0.4:80 : 172.19.0.5:8000","upstream_status":"404 : 200","http_user_agent":"Mozilla/5.0
AppleWebKit/537.36 (KHTML, like Gecko; compatible; Perplexity-User/1.0;
+https://perplexity.ai/perplexity-user)"}
,→
,→
,→
,→
,→
{"time_local":"2026-02-26T11:09:49+00:00","proxy_ip":"172.19.0.3","real_ip":"5.183.89.104","xff":" ⌋
5.183.89.104","request_method":"GET","scheme":"https","host":"genaimonitor.org","request_uri": ⌋
"/pages1/page_v901.html","status":200,"body_bytes_sent":880,"request_time":0.015,"upstream_add ⌋
r":"172.19.0.4:80 : 172.19.0.5:8000","upstream_status":"404 :
200","http_user_agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)
Chrome/142.0.0.0 Safari/537.36"}
,→
,→
,→
,→
,→
{"time_local":"2026-02-26T11:09:49+00:00","proxy_ip":"172.19.0.3","real_ip":"5.183.89.104","xff":" ⌋
5.183.89.104","request_method":"GET","scheme":"https","host":"genaimonitor.org","request_uri": ⌋
"/favicon.ico","status":404,"body_bytes_sent":278,"request_time":0.001,"upstream_addr":"172.19 ⌋
.0.4:80","upstream_status":"404","http_user_agent":"Mozilla/5.0 (X11; Linux x86_64)
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
,→
,→
,→
,→
A.8 Example server log entries (Bingbot and miscellaneous clients)
{"time_local":"2026-02-28T16:32:01+00:00","proxy_ip":"172.19.0.3","real_ip":"40.77.167.101","xff": ⌋
"40.77.167.101","request_method":"GET","scheme":"https","host":"genaimonitor.org","request_uri ⌋
":"/robots.txt","status":200,"body_bytes_sent":201,"request_time":0.001,"upstream_addr":"172.1 ⌋
9.0.4:80","upstream_status":"200","http_user_agent":"Mozilla/5.0 AppleWebKit/537.36 (KHTML,
like Gecko; compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm) Chrome/116.0.1938.76
Safari/537.36"}
,→
,→
,→
,→
,→
{"time_local":"2026-02-28T16:32:02+00:00","proxy_ip":"172.19.0.3","real_ip":"40.77.167.30","xff":" ⌋
40.77.167.30","request_method":"GET","scheme":"https","host":"genaimonitor.org","request_uri": ⌋
"/","status":200,"body_bytes_sent":452,"request_time":0.002,"upstream_addr":"172.19.0.4:80","u ⌋
pstream_status":"200","http_user_agent":"Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko;
compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm) Chrome/116.0.1938.76 Safari/537.36"}
,→
,→
,→
,→
{"time_local":"2026-02-28T16:32:07+00:00","proxy_ip":"172.19.0.3","real_ip":"34.207.145.215","xff" ⌋
:"34.207.145.215","request_method":"GET","scheme":"http","host":"genaimonitor.org","request_ur ⌋
i":"/404testpage4525d2fdc","status":404,"body_bytes_sent":278,"request_time":0.001,"upstream_a ⌋
ddr":"172.19.0.4:80","upstream_status":"404","http_user_agent":"Mozilla/5.0 (Windows NT 6.3;
WOW64; Trident/7.0; rv:11.0) like Gecko"}
,→
,→
,→
,→
{"time_local":"2026-02-28T16:32:07+00:00","proxy_ip":"172.19.0.3","real_ip":"34.207.145.215","xff" ⌋
:"34.207.145.215","request_method":"GET","scheme":"http","host":"genaimonitor.org","request_ur ⌋
i":"/404javascript.js","status":404,"body_bytes_sent":278,"request_time":0.000,"upstream_addr" ⌋
:"172.19.0.4:80","upstream_status":"404","http_user_agent":"Mozilla/5.0 (Windows NT 6.3; WOW64;
Trident/7.0; rv:11.0) like Gecko"}
,→
,→
,→
,→
{"time_local":"2026-02-28T16:32:07+00:00","proxy_ip":"172.19.0.3","real_ip":"34.207.145.215","xff" ⌋
:"34.207.145.215","request_method":"GET","scheme":"http","host":"genaimonitor.org","request_ur ⌋
i":"/pages1/.git/HEAD","status":404,"body_bytes_sent":278,"request_time":0.000,"upstream_addr" ⌋
:"172.19.0.4:80","upstream_status":"404","http_user_agent":"Mozilla/5.0 (Windows NT 6.3; WOW64;
Trident/7.0; rv:11.0) like Gecko"}
,→
,→
,→
,→
27

Gabriel Lopez-Fonseca et al.
{"time_local":"2026-02-28T16:32:07+00:00","proxy_ip":"172.19.0.3","real_ip":"34.207.145.215","xff" ⌋
:"34.207.145.215","request_method":"GET","scheme":"http","host":"genaimonitor.org","request_ur ⌋
i":"/pages1/page_v1015.html","status":200,"body_bytes_sent":883,"request_time":0.008,"upstream ⌋
_addr":"172.19.0.4:80 : 172.19.0.5:8000","upstream_status":"404 :
200","http_user_agent":"Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko"}
,→
,→
,→
,→
{"time_local":"2026-02-28T16:32:07+00:00","proxy_ip":"172.19.0.3","real_ip":"34.207.145.215","xff" ⌋
:"235.46.102.40,
34.207.145.215","request_method":"GET","scheme":"http","host":"genaimonitor.org","request_uri" ⌋
:"/pages1/page_v1015.html","status":200,"body_bytes_sent":557,"request_time":0.002,"upstream_a ⌋
ddr":"172.19.0.4:80","upstream_status":"200","http_user_agent":"Mozilla/5.0 (iPad; CPU OS
11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.0 Mobile/15E148
Safari/604.1"}
,→
,→
,→
,→
,→
,→
{"time_local":"2026-02-28T16:32:07+00:00","proxy_ip":"172.19.0.3","real_ip":"34.207.145.215","xff" ⌋
:"34.207.145.215","request_method":"GET","scheme":"http","host":"genaimonitor.org","request_ur ⌋
i":"/pages1/page_v1015.html","status":200,"body_bytes_sent":557,"request_time":0.002,"upstream ⌋
_addr":"172.19.0.4:80","upstream_status":"200","http_user_agent":"Mozilla/5.0 (compatible;
Googlebot/2.1; +http://www.google.com/bot.html)"}
,→
,→
,→
,→
{"time_local":"2026-02-28T16:32:07+00:00","proxy_ip":"172.19.0.3","real_ip":"34.207.145.215","xff" ⌋
:"34.207.145.215","request_method":"GET","scheme":"https","host":"genaimonitor.org","request_u ⌋
ri":"/pages1/page_v1015.html","status":200,"body_bytes_sent":557,"request_time":0.002,"upstrea ⌋
m_addr":"172.19.0.4:80","upstream_status":"200","http_user_agent":"Mozilla/5.0 (Windows NT
10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
,→
,→
,→
,→
A.9 Example server log entry (Diffy Chat)
{"time_local":"2026-02-25T10:37:45+00:00","proxy_ip":"172.19.0.3","real_ip":"64.71.166.35","xff":" ⌋
64.71.166.35","request_method":"GET","scheme":"https","host":"genaimonitor.org","request_uri": ⌋
"/pages1/page_v801.html","status":200,"body_bytes_sent":880,"request_time":0.018,"upstream_add ⌋
r":"172.19.0.4:80 : 172.19.0.5:8000","upstream_status":"404 :
200","http_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,
like Gecko) Chrome/142.0.7444.162 Safari/537.36"}
,→
,→
,→
,→
,→
A.10 Example server log entry (Gemini)
{"time_local":"2026-02-16T13:12:54+00:00","proxy_ip":"172.19.0.3","real_ip":"108.177.73.71","xff": ⌋
"108.177.73.71","request_method":"GET","scheme":"https","host":"genaimonitor.org","request_uri ⌋
":"/pages1/page_v303.html","status":200,"body_bytes_sent":880,"request_time":0.017,"upstream_a ⌋
ddr":"172.19.0.4:80 : 172.19.0.5:8000","upstream_status":"404 :
200","http_user_agent":"Google"}
,→
,→
,→
,→
A.11 Example server log entries (Grok)
{"time_local":"2026-02-25T09:53:07+00:00","proxy_ip":"172.19.0.3","real_ip":"104.232.216.132","xff ⌋
":"104.232.216.132","request_method":"GET","scheme":"https","host":"genaimonitor.org","request ⌋
_uri":"/pages1/page_v702.html","status":200,"body_bytes_sent":880,"request_time":0.006,"upstre ⌋
am_addr":"172.19.0.4:80 : 172.19.0.5:8000","upstream_status":"404 :
200","http_user_agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15
(KHTML, like Gecko) Version/26.2 Safari/605.1.15"}
,→
,→
,→
,→
,→
{"time_local":"2026-02-25T09:53:07+00:00","proxy_ip":"172.19.0.3","real_ip":"92.50.37.177","xff":" ⌋
92.50.37.177","request_method":"GET","scheme":"https","host":"genaimonitor.org","request_uri": ⌋
"/pages1/page_v702.html","status":200,"body_bytes_sent":880,"request_time":0.011,"upstream_add ⌋
r":"172.19.0.4:80 : 172.19.0.5:8000","upstream_status":"404 :
200","http_user_agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36
(KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}
,→
,→
,→
,→
,→
{"time_local":"2026-02-25T09:53:07+00:00","proxy_ip":"172.19.0.3","real_ip":"92.50.21.60","xff":"9 ⌋
2.50.21.60","request_method":"GET","scheme":"https","host":"genaimonitor.org","request_uri":"/ ⌋
pages1/page_v702.html","status":200,"body_bytes_sent":880,"request_time":0.010,"upstream_addr" ⌋
:"172.19.0.4:80 : 172.19.0.5:8000","upstream_status":"404 : 200","http_user_agent":"Mozilla/5.0
(Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.2
Safari/605.1.15"}
,→
,→
,→
,→
,→
28

Do Generative AI Assistants Respectrobots.txt?
{"time_local":"2026-02-25T09:53:07+00:00","proxy_ip":"172.19.0.3","real_ip":"45.41.144.154","xff": ⌋
"45.41.144.154","request_method":"GET","scheme":"https","host":"genaimonitor.org","request_uri ⌋
":"/pages1/page_v702.html","status":200,"body_bytes_sent":559,"request_time":0.000,"upstream_a ⌋
ddr":"172.19.0.4:80","upstream_status":"200","http_user_agent":"Mozilla/5.0 (Macintosh; Intel
Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.2 Safari/605.1.15"}
,→
,→
,→
,→
{"time_local":"2026-02-25T09:53:07+00:00","proxy_ip":"172.19.0.3","real_ip":"213.201.171.100","xff ⌋
":"213.201.171.100","request_method":"GET","scheme":"https","host":"genaimonitor.org","request ⌋
_uri":"/pages1/page_v702.html","status":200,"body_bytes_sent":559,"request_time":0.000,"upstre ⌋
am_addr":"172.19.0.4:80","upstream_status":"200","http_user_agent":"Mozilla/5.0 (Macintosh;
Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}
,→
,→
,→
,→
{"time_local":"2026-02-25T09:53:07+00:00","proxy_ip":"172.19.0.3","real_ip":"166.88.56.149","xff": ⌋
"166.88.56.149","request_method":"GET","scheme":"https","host":"genaimonitor.org","request_uri ⌋
":"/pages1/page_v702.html","status":200,"body_bytes_sent":559,"request_time":0.001,"upstream_a ⌋
ddr":"172.19.0.4:80","upstream_status":"200","http_user_agent":"Mozilla/5.0 (Macintosh; Intel
Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.2 Safari/605.1.15"}
,→
,→
,→
,→
{"time_local":"2026-02-25T09:53:07+00:00","proxy_ip":"172.19.0.3","real_ip":"138.226.18.61","xff": ⌋
"138.226.18.61","request_method":"GET","scheme":"https","host":"genaimonitor.org","request_uri ⌋
":"/pages1/page_v702.html","status":200,"body_bytes_sent":559,"request_time":0.002,"upstream_a ⌋
ddr":"172.19.0.4:80","upstream_status":"200","http_user_agent":"Mozilla/5.0 (Macintosh; Intel
Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}
,→
,→
,→
,→
{"time_local":"2026-02-25T09:53:07+00:00","proxy_ip":"172.19.0.3","real_ip":"162.204.9.50","xff":" ⌋
162.204.9.50","request_method":"GET","scheme":"https","host":"genaimonitor.org","request_uri": ⌋
"/pages1/page_v702.html.","status":404,"body_bytes_sent":278,"request_time":0.001,"upstream_ad ⌋
dr":"172.19.0.4:80","upstream_status":"404","http_user_agent":"Mozilla/5.0 (iPhone; CPU iPhone
OS 26_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148
Safari/604.1"}
,→
,→
,→
,→
,→
{"time_local":"2026-02-25T09:53:14+00:00","proxy_ip":"172.19.0.3","real_ip":"68.230.48.115","xff": ⌋
"68.230.48.115","request_method":"GET","scheme":"https","host":"genaimonitor.org","request_uri ⌋
":"/pages1/page_v702.html","status":200,"body_bytes_sent":559,"request_time":0.000,"upstream_a ⌋
ddr":"172.19.0.4:80","upstream_status":"200","http_user_agent":"Mozilla/5.0 (iPhone; CPU iPhone
OS 26_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148
Safari/604.1"}
,→
,→
,→
,→
,→
A.12 Example server log entries (MistralAI-User)
{"time_local":"2026-02-17T03:02:24+00:00","proxy_ip":"172.19.0.3","real_ip":"4.223.142.177","xff": ⌋
"4.223.142.177","request_method":"GET","scheme":"https","host":"genaimonitor.org","request_uri ⌋
":"/robots.txt","status":200,"body_bytes_sent":201,"request_time":0.001,"upstream_addr":"172.1 ⌋
9.0.4:80","upstream_status":"200","http_user_agent":"MistralAI-User"}
,→
,→
,→
{"time_local":"2026-02-17T03:02:24+00:00","proxy_ip":"172.19.0.3","real_ip":"51.12.243.114","xff": ⌋
"51.12.243.114","request_method":"GET","scheme":"https","host":"genaimonitor.org","request_uri ⌋
":"/pages1/page_v602.html","status":200,"body_bytes_sent":880,"request_time":0.015,"upstream_a ⌋
ddr":"172.19.0.4:80 : 172.19.0.5:8000","upstream_status":"404 :
200","http_user_agent":"Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible;
MistralAI-User/1.0; +https://docs.mistral.ai/robots)"}
,→
,→
,→
,→
,→
{"time_local":"2026-02-17T03:02:24+00:00","proxy_ip":"172.19.0.3","real_ip":"51.12.243.114","xff": ⌋
"51.12.243.114","request_method":"GET","scheme":"https","host":"genaimonitor.org","request_uri ⌋
":"/pages1/page_v602.html","status":200,"body_bytes_sent":556,"request_time":0.001,"upstream_a ⌋
ddr":"172.19.0.4:80","upstream_status":"200","http_user_agent":"Mozilla/5.0 AppleWebKit/537.36
(KHTML, like Gecko; compatible; MistralAI-User/1.0; +https://docs.mistral.ai/robots)"}
,→
,→
,→
,→
{"time_local":"2026-02-17T03:02:24+00:00","proxy_ip":"172.19.0.3","real_ip":"51.12.243.114","xff": ⌋
"51.12.243.114","request_method":"GET","scheme":"https","host":"genaimonitor.org","request_uri ⌋
":"/favicon.ico","status":404,"body_bytes_sent":278,"request_time":0.001,"upstream_addr":"172. ⌋
19.0.4:80","upstream_status":"404","http_user_agent":"Mozilla/5.0 AppleWebKit/537.36 (KHTML,
like Gecko; compatible; MistralAI-User/1.0; +https://docs.mistral.ai/robots)"}
,→
,→
,→
,→
A.13 Example server log entries (Copilot)
{"time_local":"2026-02-28T17:08:55+00:00","proxy_ip":"172.19.0.3","real_ip":"64.62.243.164","xff": ⌋
"64.62.243.164","request_method":"GET","scheme":"https","host":"genaimonitor.org","request_uri ⌋
":"/pages1/page_v1018.html","status":200,"body_bytes_sent":883,"request_time":0.013,"upstream_ ⌋
addr":"172.19.0.4:80 : 172.19.0.5:8000","upstream_status":"404 :
200","http_user_agent":"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.2)
Gecko/20090729 Firefox/3.5.2 (.NET CLR 3.5.30729; Diffbot/0.1; +http://www.diffbot.com)"}
,→
,→
,→
,→
,→
29

Gabriel Lopez-Fonseca et al.
{"time_local":"2026-02-28T17:09:02+00:00","proxy_ip":"172.19.0.3","real_ip":"64.62.243.164","xff": ⌋
"64.62.243.164","request_method":"GET","scheme":"https","host":"genaimonitor.org","request_uri ⌋
":"/pages1/page_v1018.html","status":200,"body_bytes_sent":557,"request_time":0.002,"upstream_ ⌋
addr":"172.19.0.4:80","upstream_status":"200","http_user_agent":"Mozilla/5.0 (Windows; U;
Windows NT 5.1; en-US; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2 (.NET CLR 3.5.30729;
Diffbot/0.1; +http://www.diffbot.com)"}
,→
,→
,→
,→
,→
A.14 Example server log entry (Deepseek)
{"time_local":"2026-02-28T17:46:15+00:00","proxy_ip":"172.19.0.3","real_ip":"159.138.152.86","xff" ⌋
:"159.138.152.86","request_method":"GET","scheme":"https","host":"genaimonitor.org","request_u ⌋
ri":"/pages1/page_v1102.html","status":200,"body_bytes_sent":883,"request_time":0.016,"upstrea ⌋
m_addr":"172.19.0.4:80 : 172.19.0.5:8000","upstream_status":"404 :
200","http_user_agent":"Mozilla/5.0 (X11; Linux x86_64; rv:142.0) Gecko/20100101
Firefox/142.0"}
,→
,→
,→
,→
,→
30
