---
title: 'The Customer Is the Builder: How AI Coding Agents Are Rewriting the Economics of Software'
url: https://arxiv.org/abs/2610.30307
category: digital-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Ripon Chandra Malo
- Zimeng Yu
- Tong Qiu
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.30307
pages: 37
chars: 99120
fetched_at: '2026-11-08T13:23:09+00:00'
kb_version: 1
---

# The Customer Is the Builder: How AI Coding Agents Are Rewriting the Economics of Software

The Customer Is the Builder:
How AI Coding Agents Are Rewriting the Economics of Software
Ripon Chandra Malo ∗
University of Utah
Zimeng Yu
University of Utah
Tong Qiu
University of Utah
October 2026
Abstract
AI coding agents could change whether organizations buy software or build the functionality they
need. We focus on organizations and professional buyers whose domain knowledge can help them specify
and evaluate tools for their work. We define the software substitution frontier as the functions customers
could build and maintain at an acceptable standard for less than buying them. Using public data, we
compare growing capacity to build with indicators of market change. Since 2023, the length of benchmark
tasks that leading agents can complete at 50 percent success, measured in human working time, has
doubled about every 129 days. A broad search identified 575 potential open-source alternatives to selected
commercial products, although some functional matches still require independent validation. The Craft
suite produced 12 application repositories over 12.0 days of public development, but these remain early
versions with unverified completeness and reliability. Market evidence is mixed: purchased software
gained US investment share and tracked commercial installations grew. Y et 32 percent of respondents to
an organizational survey reported forgoing at least one software purchase because their organization could
build the functionality with coding agents. These self-reports do not establish the spending displaced or
the reliability of the resulting tools. The gap motivates a warning: customers’ capacity to build could
affect individual buying decisions before a broad purchasing shift becomes visible. We examine this
possibility using benchmark projections and observable market tests. The projections are an extrapolation,
not a forecast of customer switching.
1 Introduction
Software companies have always competed with other software companies. They may soon compete
with their own customers. A firm that once needed a vendor could ask a small internal team to build the
functionality it uses, with AI agents doing more of the programming. The first version may be rough. Later
versions may meet the firm’s needs. Even before a subscription is canceled, a credible option to build can
change the value of buying.
By customers, we primarily mean organizations responsible for obtaining software: companies,
institutions and teams, including departments within large organizations. Professional buyers, such as
researchers and engineers purchasing tools for their work, face the same choice. We call customers builders
when they or their staff create or meaningfully adapt a working tool for their own workflow. This does not
require reproducing an entire commercial product. It requires supplying the functions the customer needs
and accepting responsibility for their operation.
For many customers, that option was once too expensive. A company that needed a screen recorder, a PDF
editor or a project board bought a subscription because hiring developers to build and maintain one would
∗Corresponding author: ripon.malo@utah.edu.
1
arXiv:2610.30307v1  [cs.SE]  21 Oct 2026

cost far more. Economists call this the make-or-buy decision ( Coase, 1937; Williamson, 1975). Coding
agents may change its answer, one workflow at a time. The customer may already understand the task, own
the relevant data and know how to check an answer. Agents could help turn that knowledge into software
without requiring a large development team. Existing open-source components could further reduce the work
needed to implement it.
Tools such as Claude Code and Codex can plan, write, test and revise software over many steps. The
length of benchmark tasks that frontier agents can finish has grown quickly ( Kwa et al. , 2025). This makes
the customer’s ability to build a possible source of competition for a vendor. Whether that ability becomes a
dependable and cheaper option depends on verification, maintenance, security and integration.
This idea is easy to state and easy to exaggerate. More code does not mean more shipped products
(Demirer et al. , 2026). More open-source alternatives do not mean fewer paying customers. A careful
randomized trial even found that early 2025 AI tools slowed experienced developers down ( Becker et al. ,
2025). So the question is empirical:
Is AI expanding the set of purchased software workflows that organizations and professional
buyers can economically build for themselves, and what would that mean for developers and
software companies?
We split the argument into links that can fail separately. First, what can agents do? Second, are people
building more software? Third, does more of that software compete with paid products? Fourth, are
customers switching? The early links describe capacity and creation. The last describes market decisions.
Figure 1 puts these leading and lagging indicators side by side.
Our main finding is that the capacity to build software advances before a broad shift in purchasing
becomes visible. Measures of agent capability and public software creation rose sharply around early 2025,
while the available market indicators show mixed results. An organizational survey provides some evidence
of changing purchasing decisions: respondents reported forgoing software purchases in favor of building
(Tinkoff et al. , 2026). However, the spending displaced remains unmeasured. Together, these findings
suggest that customer building could affect individual purchasing decisions before its effects become visible
in aggregate market data. Stack Overflow illustrates how sharply use can fall when alternatives become
available: monthly questions declined by 99.1 percent relative to the 2022 level, although the decline began
years before ChatGPT (Figure 2).
It illustrates how quickly use can change. It does not establish when or whether paid software will follow.
This paper makes four contributions.
1. We define the software substitution frontier, a framework for evaluating when customers can build and
maintain the functionality they need for less than buying it (Section 3).
2. We assemble a reproducible evidence base that examines agent capability, public software creation,
and market response, distinguishing growing capacity to build from evidence of changed purchasing
(Section 4).
3. We examine open-source alternatives to selected commercial products and a public case of rapid
reimplementation with coding agents, distinguishing software creation from demonstrated reliability
and adoption (Section 5).
4. We develop conditional capability projections and propose observable market tests to assess whether
greater capacity to build translates into reduced software purchases (Section 6).
2

2022 2024 2026
1 min
1 hour
1 day
LEADING
A. Task length agents complete
2020 2024
200
400
600Index, 2019 = 100
LEADING
B. New public GitHub repositories
2020 2024
0.0
2.5
5.0
7.5
10.0
12.5Per 100k new repositories
LEADING
C. "Open source alternative" repos
2010 2015 2020 2025
0
10
20
30
40
50
60% of US software investment
Bought
Built in-house
LAGGING
D. Who builds firms' software
2020 2022 2024 2026
0
50
100
150Installs per year (thousands)
Postman
Bruno (open source)
LAGGING
E. Postman vs Bruno installs
0 50 100
% of in-house builders, 2026
Small scripts
Team internal tools
Replacing paid vendors
77%
63%
19%
LAGGING
F. Why developers build in-house
Sources: METR; GitHub search API; BEA NIPA 5.6.5; Homebrew analytics; Stack Overflow Developer Survey 2026. Dotted line: Feb 2025, coding
agents arrive. Last accessed 2026-10-12.
Figure 1: Leading indicators (top) and lagging indicators (bottom).
2010 2012 2014 2016 2018 2020 2022 2024 2026
0k
25k
50k
75k
100k
125k
150k
175k
200kNew questions per month (thousands)
 ChatGPT
 released
 2022-11-30
Actual: 986
in Sep 2026
Pre-trend counterfactual
(fit: Jan 2017 to Nov 2022)
Peak 207k
(Mar 2014)
Source: Stack Exchange API v2.3, /questions?site=stackoverflow (total per calendar month; excludes deleted questions). Last accessed
2026-10-12.
Figure 2: New Stack Overflow questions per month.
3

2 Background and Related Work
2.1 Make or buy, and the economics of software
The make-or-buy decision compares the cost of organizing work inside a firm with the cost of obtaining
it from a supplier ( Coase, 1937; Williamson, 1975). Buying software has often been attractive because
a vendor can spread development costs across many customers. Digital products are cheap to reproduce
(Goldfarb and Tucker, 2019). A customer building for its own use cannot spread the initial cost in the same
way. A subscription can also bring updates, support and an existing product that works with other systems.
If agents make a working alternative cheaper to create, those other sources of value still matter. As Teece
(1986) explains, complementary assets such as distribution and service can sustain a firm even when imitation
becomes easier.
Open-source software is a partial precedent. Its development reflects motives beyond direct sales (Lerner
and Tirole, 2002); it can raise the productivity of firms that use it (Nagle, 2019); and its economic replacement
value is large ( Hoffmann et al. , 2024). Y et available code is not a finished answer for every customer.
Someone must choose it, adapt it, verify it and keep it working. The question is whether agents make those
steps cheap enough for open-source and customer-built tools to replace narrower, paid applications.
2.2 Building with AI
Sarkar (2023) anticipated that generative models could help more people write software for themselves. Later
conceptual work describes falling implementation costs and a shift toward agentic software (Dinu, 2026; Cao,
2026). The distinction relevant to this paper is what happens after a user asks for code. Chat assistants offer
advice and suggestions; a coding agent can inspect a project, edit files, run tests and revise its work across
steps. That may reduce the effort needed to turn a stated need into a working application. It does not remove
the need to decide what the application should do or to check its behavior. The arrival of coding agents is
therefore a plausible point to examine in a time series, not a causal experiment by itself.
Klotz (2026) argues that lower development costs are most likely to shift build-or-buy decisions for
commodity utilities and custom applications that give organizations a competitive advantage. Regulated and
mission-critical systems remain harder to replace. Klein and Wieczorek (2026) model how agents could
also lower the cost of coordinating specialized software components. These are conditional arguments, not
observations that customers have left vendors. They identify the factors our evidence must separate: initial
construction, integration, verification and ongoing support.
2.3 Evidence on AI and software work
Studies of coding tools measure different stages of production. A controlled study of an AI assistant found
faster task completion (Peng et al., 2023), while a randomized trial with experienced open-source developers
found that the tools available to them slowed work in familiar repositories ( Becker et al., 2025). Task gains
cannot be assumed to apply to every developer or codebase.
The closest empirical predecessor follows what happens after code is written. Demirer et al. (2026)
examine how developers’ use of AI coding tools relates to commits, projects and releases. The reported
gains are smaller for projects and releases than for commits. They also find more new applications across
software marketplaces without a corresponding rise in total use. Their result shows why a surge in code
or app creation may coexist with little change in what customers use. Our study follows alternatives aimed
at named commercial products and public measures of market response. Neither study directly measures
customers canceling subscriptions after building a replacement.
Other work shows why output may stall between a repository and a dependable product.Song et al. (2026)
find more contributions but also more coordination in open-source projects using an AI assistant. He et al.
4

(2026) find that an initial gain in development speed came with a lasting rise in code complexity. Maintainers
merge many agent-assisted pull requests (Watanabe et al., 2025), but a merge does not prove an entire product
is reliable. Software benchmarks document improving task capability ( Jimenez et al. , 2024; Kwa et al. ,
2025), while SaaSBench finds that configuring and integrating multi-component enterprise systems remains
diﬀicult (Ren et al. , 2026). These studies make verification and upkeep part of the economic question, not
an afterthought.
Scientific software illustrates the role of domain knowledge. The CLAX-PT case study reports a physicist
supervising an AI coding agent and identifying an invalid physical calculation despite passing numerical
tests ( Nguyen, 2026). It shows how a domain expert can help direct and evaluate implementation, while
also documenting failures that required specialist judgment. The case concerns software production and
validation; it does not measure a commercial purchase displaced by the resulting tool.
2.4 Evidence on AI and markets
Adjacent markets offer early evidence of changing demand, but they measure different outcomes. Stack
Overflow activity was declining before ChatGPT; del Rio-Chanona et al. (2024) nevertheless find a further
drop after its release relative to comparison forums. This is evidence about demand for shared answers, not
about software subscriptions. Demirci et al. (2025) find weaker demand for freelance work that is easier
to automate relative to work requiring manual skills. Such tasks may disappear, change or move to other
suppliers without a customer building a replacement application. Posting data also show a weaker market for
junior software roles ( Westby et al., 2026), though job advertisements respond to broader hiring conditions
as well as AI.
Building with AI may also strain the supply of reusable code. In a theoretical model, Koren et al.
(2026) predict that AI-mediated use of open-source code can reduce the feedback and returns that support
its maintainers. More easily created alternatives would then draw on a shared resource whose quality could
weaken. This is why we should measure continued use and maintenance, rather than count new projects
alone.
2.5 The gap
These studies observe different links in the same chain. Capability studies ask what agents can complete.
Productivity studies follow code into releases. Platform studies measure demand for answers or paid tasks.
Economic theory explains why a customer might build or buy. Few studies observe whether a customer
stops purchasing an application after gaining the ability to build an acceptable substitute. We bring public
measures of the successive links together over time and report evidence that cuts against substitution as well
as evidence that supports it. Direct customer-level replacement and its effect on vendor revenue remain the
decisive tests.
3 Framework: The Software Substitution Frontier
The unit of comparison is a customer’s workflow. An organization using a professional image editor may
need only cropping, background removal and file export. A tool that handles those tasks could replace the
editor without matching every feature. The comparison includes the functions the customer needs, such as
support for teamwork and connections to other systems. We compare building and buying for a customer 𝑐
and workflow 𝑤; the same product may be essential to one customer and replaceable for another.
Software creation, a viable replacement and paid substitution are distinct outcomes. A script can count
as a build if it performs a defined task. To become a viable replacement, it must meet the customer’s
acceptance standard and total-cost test over the intended period. Paid substitution additionally requires a
5

reduced purchase, a cancellation or a documented decision to build instead of buying. A public alternative
supplies a possible input to this choice; its creator need not be a customer of the product it targets.
The comparison follows established make-or-buy logic ( Coase, 1937; Williamson, 1975). Recent work
applies it to agent-built software and its lifecycle costs (Klotz, 2026). We define the following expressions to
list the costs a direct test would need to measure. They are our formulation, not estimates. Over 𝑇 months,
the cost of buying is
𝐶 buy 𝑐,𝑤(𝑇 ) =
𝑇
∑
𝑡=1
𝑝𝑤,𝑡 + 𝐼𝑐,𝑤 + 𝐴𝑐,𝑤 + 𝑆𝑐,𝑤, (1)
where 𝑝𝑤,𝑡 is the price, 𝐼 is the cost of integration, 𝐴 is administration and 𝑆 is the cost of being locked in.
Building or adapting software incurs different costs:
𝐶 build 𝑐,𝑤 (𝑇 ) = 𝐵 𝑐,𝑤(𝜃) + 𝑉𝑐,𝑤(𝜃) + 𝑀𝑐,𝑤 +
𝑇
∑
𝑡=1
(ℎ𝑐,𝑤,𝑡 + 𝑚𝑐,𝑤,𝑡(𝜃)) + 𝜆𝑐 𝐹𝑐,𝑤(𝜃), (2)
where 𝐵 is the cost to implement, 𝑉 to verify, 𝑀 to migrate, ℎ is hosting and any model usage during
operation, 𝑚 is maintenance, and 𝜆𝐹 is the expected cost of failure. Model charges incurred while writing
and testing belong in 𝐵 and 𝑉 . Software written with AI need not use AI when it runs, so ongoing model
charges apply only when the tool requires them. Greater agent capability 𝜃 may lower implementation cost.
Whether it also lowers verification, maintenance and failure costs is an empirical question. The customer
indices matter: a team that understands a workflow, controls its data and can check outputs may face different
build and verification costs from a buyer without those resources. Domain knowledge can help specify
requirements and detect errors, while software engineering remains necessary to connect and operate the
resulting system.
We call the set of workflows for which building is a credible alternative to buying the substitution frontier.
In our formulation, workflow 𝑤 lies inside it for customer 𝑐 when 𝐶 build 𝑐,𝑤 (𝑇 ) + Δ𝑐,𝑤 < 𝐶 buy 𝑐,𝑤(𝑇 ), where Δ
is the net value of factors that are hard to price, such as convenience, control and trust. This adjustment
can favor either choice. If agents lower total build cost while the alternative remains acceptable, the frontier
moves outward. Narrow, self-contained workflows, such as recording a screen or merging PDF files, may
cross it before large, regulated or deeply integrated systems. Our question is whether this frontier is now
moving fast enough to observe.
A direct test of the frontier would specify a workflow and its acceptance standard before an agent starts
building. It would record model charges, human time, verification, hosting, integration and later maintenance.
An alternative would count as viable only if it meets the standard and costs less than buying for the same
customer and period. Repeating this test across workflows and over time would show whether the frontier is
moving. This paper measures early traces of that movement; it does not claim to have completed the full test.
Until those direct tests are available, the framework separates early signs of building from later signs of
market change. The early indicators are agent capability, building cost, software creation and alternatives to
commercial products. The later indicators are installs, spending, survey answers about replacing vendors and
vendor revenue. A gap between the groups could precede a market shift. It could also persist if maintenance,
security, integration or trust prevent switching. Table 1 sets out these proposed links and the evidence that
would count against each one. They guide interpretation of separate indicators, not causal tests.
6

Table 1: Proposed links and evidence against them.
Proposed link Measure Counts against
Agent capability on software tasks
rises
Task time horizon; coding
benchmarks; cost per score
Doubling time lengthens
People build more software Repositories, packages, pushes,
Show HN, AI-credited commits
No change beyond the prior trend
Alternatives to commercial products
grow faster than software in general
Alternative repositories per 100k;
product-level discovery
Normalized rate stays flat
Alternatives attract use Installs, downloads, outside
contributors
Use stays negligible
Buyers shift from buying to building Software investment by type;
surveys; commercial installs
Shares and installs stay unchanged
4 Data and Methods
4.1 Design
This is an observational study of the links between agent capability, software creation, use and market
response. Each source measures a different link. Repositories show what was created, installs show
acquisition, and company results reflect many kinds of demand. We compare these measures over time
and report patterns that disagree as well as those that agree. The observations concern models, projects,
platforms and aggregate markets rather than a panel of identified organizational buyers. The activity and
market series do not link an internal build to a reduced purchase or cancellation by the same customer.
An external organizational survey adds self-reported decisions to build instead of buying, but no verified
purchase histories. The analysis can therefore test parts of the proposed mechanism, but cannot measure a
substitution rate or identify the effect of agents. Table 2 maps each source to its role. The code, notebooks,
and data supporting these analyses are archived on Zenodo ( Malo et al. , 2026).
For the freelance marketplaces, we compare each firm’s reported operating measures with the same
quarter a year earlier. We also compare changes in their monthly adjusted share prices with SPY, a fund
that tracks the S&P 500. These measures provide context on demand for freelance services and investors’
expectations. However, the platforms offer many services beyond software development, and share prices
reflect factors beyond AI. These data therefore cannot establish whether customers are replacing paid software
with tools they build themselves.
The GitHub and Hacker News series describe public developer communities, and the Stack Overflow
survey respondents are self-selected developers. These populations help us examine early building activity;
they do not represent all organizational buyers or general computer users. Published scientific and company
accounts provide qualitative context ( Nguyen, 2026; Airfocus by Lucid , 2026). We use them as selected
illustrations of supervision and build-or-buy choices, retain their reported diﬀiculties, and exclude them from
the quantitative samples and estimated trends.
We also record McKinsey’s organizational survey and Vals AI’s application-building benchmark as
separate sources. The survey gathered 1,719 responses across 97 nations from May 4, 2026 to June 8,
2026, with responses weighted by national contributions to global GDP ( Tinkoff et al. , 2026). We report
its purchasing question without pooling it with the developer survey. For Vibe Code Bench, we archive
the leaderboard and select 9 recent models on the common OpenHands harness, including the leading entry
and models from several providers. Models build web applications from short specifications in a prepared
environment, with up to 5 hours or 1,000 turns per build. An application earns credit for a UI test when at
7

least 90 percent of its steps succeed; the overall score averages those test results across applications ( Vals AI,
2026; Tran et al. , 2026). These scores measure tested functions, not complete applications or METR task
hours.
Table 2: Sources and measures.
Link Public source Measure
Capability METR horizons ( METR, 2026); Epoch ECI
and FrontierSWE (Epoch AI, 2026a,b); Vibe
Code Bench (Vals AI, 2026); Aider ( Aider,
2025)
Task hours, separate capability and functional
test scores, and run cost
Creation GitHub search, commit search and Innovation
Graph (GitHub, Inc., 2026b,a; GitHub, 2026);
package registries; Hacker News (Algolia and
Y Combinator, 2026)
Repositories, pushes, packages, posts and
AI-credited commits
Alternatives GitHub repositories, product sites, curated lists
and Show HN posts
Candidates for a fixed commercial-product
sample
Use and attention Homebrew ( Homebrew, 2026); Wikipedia
pageviews (Wikimedia Foundation, 2026);
GitHub releases and issues
Installs, attention, downloads and outside
engagement
Buying and work BEA ( U.S. Bureau of Economic Analysis ,
2026); Stack Overflow and McKinsey surveys
(Stack Exchange, Inc., 2026; Tinkoff et al.,
2026); Indeed and BLS ( Indeed Hiring Lab ,
2026; U.S. Bureau of Labor Statistics , 2026)
Software investment, reported building and
purchasing decisions, postings and
employment
Adjacent markets Upwork and Fiverr quarterly reports ( Upwork
Inc., 2026; Fiverr International Ltd., 2026);
adjusted share prices ( Y ahoo Finance, 2026)
Marketplace activity, clients, revenue and
valuation context
4.2 Product sample and alternatives
We fixed a sample of 12 commercial products before searching for alternatives: screen recording (Screen
Studio, Loom), writing (Grammarly, QuillBot), PDF tools (Adobe Acrobat, Smallpdf), image and design
(Adobe Photoshop, Canva), productivity (Notion, Trello) and developer tools (Postman, Retool). Choosing
products first avoids picking only the cases where alternatives went viral.
We used two definitions of an alternative. The narrow rule requires a repository description to name the
commercial product as an alternative, and the repository must be active, not a fork, and have at least 50 stars.
This rule misses projects that describe only their function. The broad search adds candidates from web lists,
GitHub searches by product and workflow, GitHub topics, curated open-source lists and Show HN posts.
Open-source candidates enter the broad count if screening finds a match to the product’s core workflow, are
neither archived nor forks, and have at least 20 stars. Paid and closed replacements are recorded separately.
The first author’s own repository is excluded from both searches. For some products, workflow matching
relies partly on keyword rules, so the broad count is an upper bound until independent validation.
4.3 Measuring change over time
We also screen package creation counts to reduce short-lived entries. A new PyPI project qualifies if it has a
second release within 90 days. A package on crates.io qualifies if it has more than one published version when
the data are collected. A RubyGems package qualifies if it remains listed in the registry. We omit recent PyPI
8

and crates.io cohorts whose follow-up window is incomplete. Packagist supplies only net additions from its
aggregate series. These screens can also exclude legitimate projects with a single release.
We use segmented regression for package creation and download series, where enough monthly
observations are available on both sides of the events. The model permits a change in level and trend after
ChatGPT’s release, then another after the initial coding-agent preview:
log 𝑦𝑡 = 𝛽 0 + 𝛽1𝑡 + 𝛽2𝐷GPT 𝑡 + 𝛽3(𝑡 − 𝑡1)𝐷GPT 𝑡
+ 𝛽4𝐷agent 𝑡 + 𝛽5(𝑡 − 𝑡2)𝐷agent 𝑡 + 𝛾 ⊤𝑠𝑡 + 𝜀𝑡, (3)
Here 𝑦𝑡 is a positive monthly count, 𝑡1 is December 2022, and 𝑡2 is February 2025. Each indicator 𝐷𝑡
switches on at its break. Its coeﬀicient captures an immediate level change; the interaction with time
captures a change in slope. The vector 𝑠𝑡 accounts for month-of-year patterns. We use heteroskedasticity
and autocorrelation consistent standard errors with a full year of monthly lags ( Newey and West , 1987).
Table 5 reports the fits. As a sensitivity check, we move the coding-agent break across the six months on
either side of the chosen date while holding the model and sample fixed. Table 6 reports how the estimated
slope change varies. This check does not identify the date or cause of a change.
The Stack Overflow question series has a separate single-break fit and a pre-release trend counterfactual.
Other time series are described rather than fitted with this model. Where a suitable denominator exists, we
also show rates: alternative repositories per new repository, AI-credited commits per public commit, and
alternative Show HN posts per Show HN post. Those rates help separate changes in a specific activity
from growth of its platform. Break dates mark events, not random assignments. The coeﬀicients and
counterfactuals are descriptive associations.
4.4 Capability projection
METR’s task horizon measures task length by how long a human expert would take to complete the work. It
estimates the task length at which an agent achieves a specified success rate. It is not the time an agent can
work unattended. We fit a straight line to the logarithm of the 50 and 80 percent horizons of frontier models
against release date. The recent fit starts in 2023; the longer fit starts in 2019. Following the source’s fitting
rule, we omit models whose 50 percent horizon exceeds 16 hours.
We extend each fitted line to the point at which its task horizon equals a skilled human workday (8 hours),
workweek (40 hours), workmonth (167 hours) or workyear (2,000 hours). We resample models 10,000 times
and report the 5th to 95th percentiles of the resulting paths and crossing dates. These bands reflect variation
across the selected models, not uncertainty in METR’s task sample. The dates are an extrapolation if the
fitted trend continues, not a forecast of product replacement.
For a dated check, we fit the trend only to frontier models released before the coding-agent break and
compare its predictions with later measured models. This tests how the earlier capability trend tracked later
benchmark results. It cannot validate the future path or tell us when buyers will leave vendors.
4.5 Case study
The Craft suite is an illustrative frontier case, selected because its public build was unusually rapid and
visible. It is not a representative sample. We collected the 12 application repositories from the suite’s
GitHub organization ( ArtCraft, 2026a) through the GitHub API. Commit histories use a fixed cutoff; other
changing measures are retrieval-time snapshots. The measures include default-branch commits, explicit AI
co-author trailers and author accounts, agent instruction files, automated workflow runs, issues, pull requests
and release-asset downloads. We counted source lines from repository clones. Commit counts depend on
merge practice, AI trailers miss uncredited use, and downloads do not identify distinct users.
9

We compare these public measures with roadmaps and maturity claims on the suite’s website ( ArtCraft,
2026b). The case documents speed, scale and outside engagement. It does not establish feature parity, a
clean-room development process or a customer switching away from a paid product.
5 Results
The evidence in Figure 1 shows growing capacity to build software alongside mixed evidence of changes
in purchasing. Agent capability has improved over several years, while public software creation and the
appearance of commercial alternatives accelerated around the start of the coding-agent era. Aggregate
indicators show continued purchasing, although some survey respondents report building instead of buying.
The available data do not establish how widespread this shift is. We examine each link in turn, including
evidence that challenges the proposed shift from buying to building.
5.1 Agents can do much more, for much less
Frontier agents can now complete increasingly long software tasks. Since 2023, their estimated task horizon
at 50 percent success has doubled about every 129 days (panel A of Figure 3; 95 percent interval: 102 to 154
days). This corresponds to roughly a 7.1-fold increase in task horizon per year. GPT-4’s estimated horizon
was 4 minutes of skilled human work. The largest reported estimate, for a model released in April 2026, is
17.4 hours. However, this estimate exceeds METR’s reliable measurement range of 16 hours. At 80 percent
success, the same model’s horizon is 3.1 hours. The series covers models released through April 2026 and
is no longer actively updated ( METR, 2026), so it does not establish the task horizons of newer models.
Panel B of Figure 3 provides evidence on newer models. Epoch’s general capability index includes 12
models released in September 2026, including GPT-6 Sol, GPT-6 Astra and Claude Opus 5.5 ( Epoch AI ,
2026a). The index combines results from several benchmarks. It does not measure task length in human
working hours or the reliability of finished software. Overlapping intervals also make it diﬀicult to distinguish
the leading models.
FrontierSWE provides a separate comparison of coding performance, evaluating recent Gemini, Grok and
open-weight models under the same testing setup (Figure15). The highest mean normalized task score is 65.5
(Epoch AI, 2026b; FrontierSWE, 2026). The bars show the lowest and highest scores across 5 runs, rather
than statistical uncertainty intervals. These results extend coverage to newer models, but do not establish
whether an agent can build and maintain a complete product.
Vibe Code Bench tests a closer step toward customer building: creating a web application from a short
specification. Figure 4 shows selected recent models on the same OpenHands harness. Their scores range
from 86.17 to 92.39 percent in the archived leaderboard ( Vals AI, 2026). These are averages of functional
UI-test results, not the share of applications that are fully correct. The prepared environment also removes
some setup work a customer would face. The results show that recent models can implement much of the
tested functionality, while leaving security, integration and continued operation unmeasured ( Tran et al. ,
2026). Together with the other recent benchmarks, this evidence extends model coverage without supplying
new observations for METR’s time-horizon curve.
10

2019 2020 2021 2022 2023 2024 2025 2026
1 s
15 s
1 min
4 min
15 min
1 h
4 h
16 h
64 h
50% horizon (human task time)
 Frontier fit: 129 days per doubling
A. METR software task horizons, models through April 2026
Frontier at release
Other measured model
145 150 155 160 165 170
Epoch general capability index (different scale)
Grok 4.7
DeepSeek V4.1 Flash
Qwen3.8 Max (0902)
GPT-6 Luna
Gemini 3.8 Flash
Muse Spark 1.3
GPT-6 Sol
Claude Fable 5.1
Claude Sonnet 5.5
GPT-6.1 Sol
GPT-6 Astra
Claude Opus 5.5
GPT-5 reference = 150
B. Recent models, September 2026 release cohort
Sources: METR Time Horizon 1.1 and Epoch AI ECI. Bars: published intervals. Separate tests and units; ECI does not update the METR trend.
METR last accessed 2026-10-12; Epoch last accessed 2026-10-14.
Figure 3: Historical task horizons and recent model capability.
11

0 20 40 60 80 100
Mean functional UI-test score (%)
Grok 4.7
DeepSeek V4.1 Flash (1017)
GPT-6.1 Sol
GPT-6 Astra
Claude Fable 5.1
Claude Opus 5.5
Claude Haiku 5.5
Gemini 4 Argon
Claude Sonnet 5.5
86.17
87.73
88.93
89.59
90.26
90.29
90.44
91.91
92.39
Source: Vals AI Vibe Code Bench v1.1; selected models, OpenHands harness.
Scores average application test results, not complete-application success rates. Last accessed 2026-10-19.
Figure 4: Functional test scores for selected application-building agents.
The cost of a fixed benchmark result also fell (Figure 5). On the Aider coding benchmark, the cheapest
run that solved at least 60 percent of tasks cost $186.50 in December 2024 and $4.80 by August 2025, a drop
of 39 times in eight months. This is the cost of a benchmark run, not a deployed and maintained product.
Jul
2024
Oct
2024
Jan
2025
Apr
2025
Jul
2025
Oct
2025
$0.3
$1
$3
$10
$30
$100
$300Cheapest cost of full run (USD)
≥50%
≥60%
≥70%
≥80%
Source: Aider LLM leaderboard via Epoch AI Benchmarking Hub, CC-BY .
Gray: individual runs; overlapping steps share the cheapest model. Last accessed 2026-10-14.
Figure 5: Cost of reaching a fixed score on the Aider benchmark.
12

5.2 Public software creation accelerates in the agent era
If agents lower the cost of building, people may build more. Public creation measures rise, and their timing
is telling. Figure 6 shows new packages per month on four registries. During the ChatGPT period, from
December 2022 to January 2025, growth in new packages slowed. On PyPI, average yearly growth fell from
26 percent before ChatGPT to 1 percent. On crates.io it fell from 39 to 19 percent. After agents arrived in
February 2025, growth jumped to 23 percent on PyPI and 123 percent on crates.io. In the time series model,
the trend in screened new crates rose by 119.6 annualized log points after February 2025 and the trend in
screened PyPI projects by 17.9 log points (both𝑝 < 0.001 ; Table 3). The acceleration is consistent with faster
supply growth during the agent period. It is not specific to the February break: the slope changes remain
positive when that break is moved across nearby months, but the best-fitting date differs by registry (Table 6).
These time series cannot establish that agents caused the growth; registry policies, spam and changes in the
developer population may also matter.
0
5
10
15
20New packages / month (k)
dashed: 2nd release ≤ 90 days
ChatGPT
Agents
PyPI
0
5
10
15
dashed: ≥ 2 versions
crates.io
2016 2018 2020 2022 2024 2026
0
5
10
15
20New packages / month (k)
dashed: not fully yanked
RubyGems
2016 2018 2020 2022 2024 2026
0
2
4
6
Packagist (net additions)
Source: PyPI & RubyGems via ClickHouse public playground (mirrors of PyPI BigQuery metadata and the RubyGems.org dump); crates.io API;
packagist.org/statistics. Last accessed 2026-10-12.
Monthly 12-month mean 12-month mean, filtered
Figure 6: New packages per month on four registries.
13

Table 3: New-package growth after ChatGPT and coding agents.
Annualized slope change (log points)
Registry Series
ChatGPT
Dec 2022
Coding agents
Feb 2025 Months
PyPI Screened projects −15.5∗∗∗ (3.0) +17.9 ∗∗∗ (3.8) 126
crates.io Screened crates −19.3∗∗∗ (2.4) +119.6 ∗∗∗ (14.3) 126
RubyGems Screened gems +10.4∗∗∗ (1.8) +84.9 ∗∗∗ (4.9) 129
Packagist Net additions −5.8∗∗∗ (2.2) +55.1 ∗∗∗ (6.4) 129
Estimates are changes in the slope of log monthly counts, annualized and multiplied by 100. Standard errors are in parentheses.
Each model includes both dates and month-of-year effects, with standard errors adjusted for autocorrelation. Screened series use
the registry-specific rules in Methods. Packagist reports net additions. ∗𝑝 < 0.1 , ∗∗𝑝 < 0.05 , ∗∗∗𝑝 < 0.01 . Unscreened estimates,
level shifts and downloads appear in Table 5.
GitHub data show that the rise in public development activity extends beyond package creation (Figure7).
In the first quarter of 2026, code pushes increased by 80 percent from a year earlier, compared with an earlier
annual average of 15 percent. The increase was geographically broad: 99 percent of the 184 economies
in the data recorded growth. The developer account total increased by 13.7 million that quarter, compared
with an average quarterly increase of 5.9 million in 2023 and 2024. New public repositories also increased
by 67 percent over the preceding twelve-month period (Figure 17). Language participation changed as well
(Figure 16), although these shifts began before coding agents.
Hacker News provides a separate signal of increased project sharing. Show HN posts averaged 3,846
per month over the last year, compared with 823 in early 2022. Their share of all stories rose from 3.3 to
12.9 percent (Figure 18). These measures indicate greater public activity, but do not establish how much
additional usable software was produced or whether coding agents caused the increase. Developer and
repository totals include inactive accounts and projects, pushes measure quarterly activity, and Show HN
posts measure sharing rather than verified software completion.
2020 2022 2024 2026
100
150
200
250
300
350
400Index, 2020Q1 = 100
Repositories 349
Git pushes 396
Developers 423
ChatGPT
Coding agents
World (sum of economies)
2020 2022 2024 2026
Repositories 252
Git pushes 268
Developers 332
ChatGPT
Coding agents
United States
Source: GitHub Innovation Graph (github.com/github/innovationgraph, CC0), quarterly, public activity; economies with <100 developers
suppressed; EU aggregate excluded. Last accessed 2026-10-12.
Figure 7: GitHub developers, repositories and pushes.
14

Some new code is visibly linked to agents, and that signal is growing (Figure 8). In September 2026,
the search counted 16.46 million public commits credited to an AI tool, 19.8 times the search count a year
earlier. Claude Code accounts for 87 percent of the attributed commits. Many uses leave no credit line,
while overlapping signatures and mirrored repositories can duplicate counts. About 1,105,920 public files
named AGENTS.md and 872,448 named CLAUDE.md, which hold instructions for coding agents, now exist
on GitHub. Commit messages mentioning these files also increased (Figure 19). Those mentions record
configuration work, not a count of finished products. Optional attribution, incomplete search results and
changing commit habits limit what these counts can say about the amount of finished software.
2023 2024 2025 2026
0.0
2.5
5.0
7.5
10.0
12.5
15.0
17.5Attributed commits (millions)
Claude Code 14.4m
All tracked tools 16.5m
2023 2024 2025 2026
0
10
20
30
40
50
60
70AI-attributed commits per 1,000 pushes
1 1 3
11
21
67
Sources: GitHub commit search (tool trailers and bot authors) and GitHub Innovation Graph git_pushes (CC0; economies summed, EU
aggregate excluded).
Attribution is optional; signatures may overlap and some searches are incomplete. Quarterly ratio through 2026Q1. Commits per push is not a
share. Last accessed 2026-10-12.
Figure 8: AI-attributed commits: monthly totals (left) and quarterly commits per push (right).
5.3 More projects target commercial software
Building more is not the same as building substitutes. To examine whether projects increasingly target
commercial functionality, we count repositories that describe themselves as an alternative, relative to all
new repositories (Figure 9). Repositories calling themselves an “open source alternative” rose from 3.3 per
100,000 new repositories in 2022 to 11.9 in the last twelve months. “Self-hosted alternative” rose from 0.4
to 4.5. Among repositories with at least ten stars, which filters out most empty projects, the open-source
alternative rate rose from 91 to 290 per 100,000. The increase is concentrated after February 2025.
At the individual-product level, the picture is similar, with an important qualification (Figure 10). For the
twelve products in our sample, the broad search found 1,211 candidates, of which 575 open-source projects
passed the automated screen, against only 45 under the narrow rule. The narrow timeline in Figure 21
shows that named alternatives existed well before coding agents, while the broader search finds many more
candidates. Workflow matches for some products still need independent validation, so these screened counts
are an upper bound on qualified alternatives. Of the screened projects, 191 (33 percent) were created after
February 2025. The newest alternatives also look different: 47 percent of those created after February 2025
contain agent instruction files, against 11 percent of older ones. The categories differ as the framework
15

2013 2019 2025
0
10
20
30
40Repos per 100k new repos
Any phrase
8.3
ChatGPT
Claude Code
A
2013 2019 2025
0
5
10
15
20
Self-hosted alt.
5.8
Open source alt.
11.7
B
2013 2019 2025
0
500
1000
1500Per 100k starred repos
Self-hosted alt.
84
Open source alt.
227
Any phrase
1179
C
2013 2019 2025
0
50
100
150
200
250
Any phrase
144
README-index
artifact, 2018
(peak 1,128)
D
Source: GitHub REST search API (/search/repositories; "alternative to" OR "open source alternative" OR "self-hosted alternative";
in:description[,readme]; created: monthly windows).
3-month trailing mean (thin = monthly); dashed = ChatGPT (2022-11-30), Claude Code preview (2025-02-24). Deleted repos absent. Last
accessed 2026-10-12.
Figure 9: Alternative-repository rates: (A) descriptions only; (B) substitute phrases; (C) star-filtered matches; (D)
descriptions or READMEs.
predicts. All 6 screened candidates for Screen Studio, a narrow screen recording tool, appeared after February
2025, and 4 of 5 for Smallpdf did. QuillBot, a paraphrasing tool, received no new screened candidates. A
general assistant could cover some paraphrasing tasks without anyone publishing a separate tool, but this
study does not measure that use.
Not every measure points the same way. The share of Show HN posts that call themselves an alternative
fell slightly, from 1.50 percent in 2022 to 1.25 percent in the last year, so the new projects on Hacker News
grew in number, not in focus on substitution. The separate narrow pilot also raises a question about durability:
newer alternatives have a median of 4 contributors, against 167 among those created before ChatGPT (GitHub,
Inc., 2026c). This is a small, selected sample, and older projects have had more time to recruit. The contrast
does not establish which alternatives will last.
16

0 20 40 60 80 100 120 140
Screened open-source candidates (broad rule)
QuillBot
Smallpdf
Screen Studio
Adobe Acrobat
Loom
Grammarly
Retool
Canva
Adobe Photoshop
Postman
Trello
Notion
3
5
6
8
8
13
17
53
66
105
141
150
Narrow rule (names the product)
Before Dec 2022
Dec 2022 to Feb 2025
Since Feb 2025
Broad rule: six discovery strategies; screened for core workflow, not archived, not a fork, >= 20 stars; author-owned repo excluded. Workflow
match partly heuristic (upper bound). Last accessed 2026-10-12.
Figure 10: Screened open-source candidates for twelve products, by creation date.
5.4 The frontier case: a suite built at speed
One visible example of what agents can now do is the Craft suite, an open-source project that set out to
reimplement major creative and oﬀice software (Figure11). Between 2026-09-30 and 2026-10-07, its authors
created 12 applications aimed at Adobe Photoshop, Lightroom, Premiere Pro, Illustrator, After Effects,
InDesign and Acrobat, Microsoft Word, Excel and PowerPoint, Autodesk AutoCAD and Avid Pro Tools.
The measured scale is large. In 12.0 days of public history the suite received 11,760 commits and grew to
2,633,601 lines of Rust, with 30,928 test functions. At least 61 percent of commits carry an AI co-author line,
most often Claude Opus 5.5 (Table 7 and Figure 20). Every application has an AGENTS.md file that tells
agents to work autonomously and to ask a human only about licensing, publishing or secrets (ArtCraft, 2026a).
The project also drew outside engagement: 2,075 people outside the project filed issues, 876 outside authors
opened pull requests, and release files were downloaded 4,145,191 times. These are signs of engagement,
not counts of distinct users or canceled subscriptions. Downloads include automatic updates and ancillary
files.
The suite is not yet a replacement for the products it targets. Its own roadmaps label nine applications
alpha and three pre-alpha, and rate them a median of 50 percent ready for real work. Press coverage was
mostly mixed or skeptical, pointing to missing features, memory use, and open legal questions about the
term clean room. We treat the suite as a measure of the frontier, not of the market. It shows how quickly
agents and many contributors can produce a large codebase. It does not show how quickly they can produce
a dependable commercial substitute. The lagging indicators answer whether customers come to rely on such
software.
The app-level evidence in Table7 makes the trade-off visible. Some apps have large codebases and many
contributors, yet the shares of successful automated runs vary. Those runs include pull requests, and the
roadmaps still rate readiness well below full use. The daily record in Figure 20 shows bursts of AI-attributed
and other commits. It records output and participation, not independent evidence that the apps meet their
target products’ quality or feature coverage. This is a collaborative build, not a measured case of one customer
17

Sep 26 Sep 28 Sep 30 Oct 2 Oct 4 Oct 6 Oct 8 Oct 10 Oct 12 Oct 14
2026 (UTC)
PhotoCraft → Adobe Photoshop
PdfCraft → Adobe Acrobat Pro
FilmCraft → Adobe Premiere Pro
VectorCraft → Adobe Illustrator
LightCraft → Adobe Lightroom
DesignCraft → Adobe InDesign
EffectCraft → Adobe After Effects
GridCraft → Microsoft Excel
CADCraft → Autodesk AutoCAD
DeckCraft → Microsoft PowerPoint
SoundCraft → Avid Pro Tools Ultimate
WordCraft → Microsoft Word
49.3k
10.0k
10.5k
7.3k
10.4k
3.1k
5.3k
3.2k
2.9k
2.1k
1.9k
6.9k
Hacker News thread
(165 pts, 4 Oct 23:02 UTC)
marker area = current stars
1k 10k 50k
creation → latest commit
first commit (history pre-dates the repository)
Bar: repository creation (tick) to latest commit on the default branch (circle). Source: GitHub REST API (storytold/*), last accessed 2026-10-12
UTC; HN: Algolia API.
Stars are a one-click bookmark, not users; 'clean-room' and 'reimplementation' are the authors' claims. First commits of several repos predate
creation (imported history).
Figure 11: The Craft suite: twelve applications and the products they target.
canceling a subscription.
5.5 Purchasing evidence is mixed
The lagging indicators tell a different story. In US national accounts (Figure 12), software that firms build for
themselves fell from 14.0 percent of software investment in 2022 to 13.3 percent in 2025, while purchased
packaged software rose from 46.3 to 49.6 percent. This measure has limits. BEA values in-house software
by what firms pay their developers, so if agents let the same staff build more, the series will not show it. Still,
there is no sign yet of a national shift from buying to building.
The Homebrew pilot has not shown a general shift away from commercial tools (Figure 13). Y early
installs of Postman rose from 63,350 in 2019 to 139,258 in 2026, and installs of Notion from 6,140 to
60,782. The open-source alternative AppFlowy reached only 2.4 percent of Notion’s installs. The one strong
exception is Bruno, an open-source alternative to Postman, which grew from almost zero to 75,820 installs,
or 54 percent of Postman’s. Bruno was created before ChatGPT. These data do not show whether agents
contributed to its later development or adoption.
These public measures miss another possible route to substitution. A customer could use a general AI
subscription for a narrow task or ask an agent to build a private tool for it. Neither choice needs to produce a
public repository or a Homebrew install. The public activity series cannot establish how often either choice
replaces a paid product. Surveys can ask about the decision more directly.
The developer survey records the functions of in-house software. In the 2026 Stack Overflow survey,
13,338 respondents who build in-house reported their workflows. Most build small scripts (77.3 percent)
or internal tools for their team (63.0 percent). Only 18.6 percent said they were replacing paid vendors.
These are self-reported functions, not independently verified cancellations or a representative survey of
18

1985 1990 1995 2000 2005 2010 2015 2020 2025
0
10
20
30
40
50Share of nominal software investment (%)
Prepackaged (bought)  50%
Custom (commissioned)  37%
Own-account (built in-house)  13%
ChatGPT
(Nov 2022)
Coding-agent
era (2025)
Source: BEA NIPA Table 5.6.5 (series Y003RC, Y004RC, Y005RC; shares of B985RC), annual. Last accessed 2026-10-12.
Figure 12: US private software investment by type.
1
10
100
1k
10k
100kInstalls, trailing 365 days
requestly 2.8k
bruno 75.8k
postman 139.3k
Postman
1
10
100
1k
10k
100k
appflowy 1.5k
notion 60.8k
Notion
2020 2022 2024 2026
1
10
100
1k
10k
100kInstalls, trailing 365 days
cap 2.7k
loom 4.6k
Loom
2020 2022 2024 2026
1
10
100
1k
10k
100k
Compositor 1.7k
Creative Cloud 7.4k
Adobe Photoshop
Homebrew cask-install analytics (formulae.brew.sh), live file Oct 2026 plus Wayback Machine captures (only years the archive served intact).
Opt-in macOS Homebrew users only;
adobe-creative-cloud stands in for Photoshop. Installs are not paid seats or active users. Dotted line: ChatGPT. Pilot of 12 pre-specified products.
Figure 13: Y early installs of commercial tools and open-source alternatives.
19

software-buying organizations.
McKinsey’s organizational survey asks a more direct purchasing question. It reports that 32 percent
of respondents said their organization had decided against buying at least one software product or feature
because it could build the functionality internally with coding agents ( Tinkoff et al. , 2026). This reflects
reported purchases forgone, which can occur without a canceled subscription. It does not measure spending
displaced, continuing use or the quality of the internal tools. The survey and developer responses concern
different populations and questions, so their percentages should not be compared as a trend. They suggest
that some buying decisions are changing while leaving the aggregate scale unresolved.
Employment at software publishers is also steady, at 652.9 thousand in August 2026, close to its peak of
664.3 thousand in November 2022. Job postings for software developers fell sharply (Figure 22), from an
index of 233.9 in February 2022 to 142.5 when ChatGPT was released and 78.3 today, but most of that fall
came before ChatGPT, and postings have risen 16.0 percent since January 2025.
Freelance marketplaces give an early, adjacent market signal. In their latest reported quarter, Fiverr’s
annual active buyers fell 21.9 percent and its marketplace revenue fell 15.5 percent from a year earlier. Its
management cited AI-related demand and traﬀic headwinds in work most exposed to automation, while spend
per buyer rose ( Fiverr International Ltd. , 2026). Upwork’s active clients fell 4.1 percent and gross services
volume fell 3.6 percent, while adjusted EBITDA rose 12.3 percent and the firm reported rising AI-related
work (Upwork Inc., 2026). The adjusted share-price comparison in Figure 23 shows that both firms’ shares
also fell, with much of the decline beginning before coding agents arrived. These marketplaces include many
forms of work beyond software. Their results are a warning about some paid tasks, not proof that customers
have stopped buying software.
Stack Overflow shows how quickly such a picture can change. Monthly questions fell from 112,934 in
2022 to 986 in 2026-09 (Figure 2). The decline started earlier, with a 36.7 percent fall between 2017 and
2022, so not all of it is due to AI. The sharper later decline shows how quickly use can change, but this series
does not isolate AI’s effect from the earlier trend.
5.6 The warning: when benchmark tasks grow longer
Figure 14 extrapolates the measured capability trend. To assess how an earlier trend compared with
subsequent progress, we fit the trend using only frontier models released before the coding-agent era.
At 50 percent success, all 8 later frontier models had task horizons above those predicted by the earlier
trend, with a median observed-to-predicted ratio of 3.6 (Figure 24). The earlier trend therefore understated
subsequent benchmark progress. This result does not establish that progress will continue to accelerate.
Model selection, changes in the task mix and benchmark measurement may also affect the observed trend.
If the more recent trend continues, agents would reach 50 percent success on benchmark tasks that would
take a skilled human a work-week around Dec 2026. The corresponding work-month threshold would be
reached around Sep 2027 (interval: Apr 2027 to Feb 2028). Under the slower, longer-term trend, these
thresholds would be reached in Nov 2027 and Nov 2028, respectively. Requiring 80 percent success moves the
projected dates later: the two trend fits place the work-month threshold between Sep 2028 and Aug 2030, and
the work-year threshold between Jan 2030 and Aug 2032. These dates extrapolate benchmark performance;
they do not establish when agents could reliably build and maintain complete software products.
These dates apply to performance on a specific set of benchmark tasks. A work-month describes how long
a skilled human would need to complete a task, not how long an agent would run autonomously. Completing
such a task also does not establish that the resulting software can be deployed and maintained reliably. The
Craft suite illustrates how quickly agents and contributors can create large codebases at an early stage of
development. Whether these become dependable replacements for paid software depends on verification,
integration and continued maintenance. The projected dates are an extrapolation, not a forecast. Future
progress may differ as costs, available data and technical constraints change. The measured series ends with
20

2022 2024 2026 2028 2030 2032
1 min
1 hour
1 work-day
1 work-week
1 work-month
1 work-year
Length of software task
(time a skilled human needs)
Sep 2027
Dec 2028
Nov 2028
Oct 2030
 today
A
2022 2024 2026 2028 2030 2032
Sep 2028
Jan 2030
Aug 2030
Aug 2032
 today
B
Source: METR Time Horizon 1.1 (frontier models); OLS of log2 horizon on release date, shaded = 5-95% bootstrap band. Extrapolation of a
benchmark trend, not a forecast. Last accessed 2026-10-12.
Trend since 2023 Trend since 2019 Frontier model (measured)
Figure 14: Task-horizon extrapolation: (A) 50% success; (B) 80% success; 5 to 95 percent bands.
models released in April 2026, so the projection does not incorporate comparable task-horizon measurements
for newer models.
6 The Next Decade: When Building Changes Buying
Consider a department within a company that pays for a screen recorder because it needs to capture, trim and
share clips. The department knows its workflow and can assign a small team to build those functions with
agents and existing components. It does not need to reproduce the vendor’s complete product or serve the
vendor’s other customers. It needs a dependable tool for its own users. The same reasoning applies to file
archiving, document viewing and other bounded oﬀice workflows. If the internal tool meets those needs at a
lower total cost, the organization could reduce its purchased seats or forgo a new contract. It could still pay
for model access, compute and upkeep. The cost comparison in Section 3 specifies the conditions for that
choice.
Customers have other routes. A general AI subscription might handle a writing task that once required a
separate product, without anyone building an application. An agent might instead create a private file utility
or internal workflow that never appears on GitHub. A customer could also adopt a public alternative and
use an agent to adapt it. Each route could reduce demand for a narrow application, but our public repository
and install data see only part of the process. Spending could move from application subscriptions to model
access, hosting and maintenance rather than disappear.
Existing software may shorten the path. Published source can be reused when its license permits. For
21

software without source, the REA project documents tools that let an agent inspect application behavior
and binaries, then use the findings to implement a similar feature ( REA, 2026). This shows that the tools
exist, not that they reproduce a whole product or remove legal and technical limits. Agents can also inspect
a visible interface. Current computer-use tools give models screenshots and let them act through a mouse
and keyboard ( OpenAI, 2026; Anthropic, 2026b). A customer with access to an application could have an
agent try its features, observe the responses and attempt to implement a similar workflow. Models can also
examine product demonstrations in video ( Google, 2026). These routes reveal observable behavior, but they
do not prove that an agent can recover the original code or deliver a dependable replacement from a brief
instruction.
Domain expertise could extend this route beyond simple oﬀice utilities. A scientific or engineering team
may know the physical model, input data, boundary conditions and reference calculations for a research task.
It could direct agents to implement that workflow around existing numerical libraries, then check outputs
against known solutions. The commercial comparison would concern the functions used in that research,
rather than every feature of a general analysis package. This is a proposed route to customer building. The
scientific case discussed in Section 2 illustrates both the role of specialist judgment and the diﬀiculty of
obtaining trustworthy output.
Building need not be fully autonomous to change this choice. A domain expert can set requirements,
inspect intermediate results and decide when a tool is ready for use, while agents carry out much of the
implementation. HAS-Bench finds that the benefits of participation depend on how it is organized ( Wu et al.,
2026). Its experiments simulate human participants, so they do not establish the gains real professional teams
would obtain. The economic test is whether the combined human and agent effort costs less than buying an
acceptable tool. Human oversight belongs in that comparison rather than disqualifying the build option.
A report published by Airfocus by Lucid describes a related organizational choice. Lucid’s product team
evaluated commercial tools and built Archie, an internal tool for account research using the team’s own
data ( Airfocus by Lucid , 2026). The account also describes usage costs, code review, security work and
uncertain maintenance. It illustrates a reported decision to build instead of buy, not an independently audited
cancellation or a rate of replacement. These operational demands are part of the mechanism the trend data
leave unresolved.
The projection in Figure 14 supplies a conditional capability clock. At 80 percent success, the faster fit
reaches tasks that would take a skilled human a work-month in Sep 2028, and the slower fit in Aug 2030.
These are extrapolated dates for tasks in a fixed suite, not dates when customers cancel subscriptions. A
product combines many tasks and must keep working after release. The projection cannot measure the time
needed for that transition. Recent models appear in other benchmarks (Figures 3, 4 and 15), but those scores
cannot extend the METR horizon fit. The first effect on vendors may instead be a customer’s credible option
to build, which can put pressure on price or packaging before a sale is lost.
The market consequence depends on how far agents reduce the work after initial implementation. An
early route is a customer with domain expertise and technical support directing agents through a bounded
workflow. If agents also make testing, deployment, integration and repair less demanding, smaller internal
teams could operate more complex tools. A large organization could then obtain more software from a small
group responsible for its specific needs. Multiple users, shared data and continuing security work make that
a harder test than producing a prototype.
The broad extension of this mechanism reaches general computer users. If agents can turn ordinary
requests into suitable specifications, check their own work and keep tools running, a person who can operate
a computer could commission a private tool without learning a programming language. This possibility gives
the warning its longer horizon. The present developer and benchmark data do not establish when that level
of assistance will be dependable or how widely it will be adopted.
Table 4 separates the ways spending could move. The routes can coexist; they are conditional
mechanisms, not estimated probabilities.
22

Table 4: How AI could change demand for applications.
Route Customer choice What to measure
AI subscription Uses an assistant for a narrow task Paid cancellations tied to assistant use
Private tool An organization or professional buyer
builds a tailored workflow
Reduced purchases, sustained use,
oversight and total cost
Public alternative Adopts or adapts a shared project Sustained use and buyer reports of paid
replacement
Vendor adaptation Keeps buying for reliability, data, support
or distribution
Renewals, prices and packaging among
exposed vendors
By 2028, comparable surveys should test whether the share of in-house builders replacing paid vendors
has risen above the 18.6 percent baseline. Buyer reports should distinguish a private build from a general
assistant replacing a task. In a narrow category, sustained use of an alternative and evidence of reduced
purchases would support the customer-building route. Studies should distinguish organizations from
individual professionals and record the technical support each build requires. More repositories alone would
not establish that change.
By 2031, exposed vendors should show pressure on seats, prices, packaging or revenue if customers can
credibly build or switch. These changes should be compared with less exposed products and with broader
market conditions. The national investment series may miss an early private-build shift: it values in-house
software by developer pay and does not track canceled application seats. Broader participation should also
be tested directly: can users with less programming experience specify, validate and operate useful tools with
less technical assistance? If alternatives multiply but renewals remain strong, the value of maintenance, trust
and integration is larger than the simple build story assumes.
Near-total disappearance of paid application software by 2036 remains an extreme hypothesis, not
our forecast. It would require dependable replacement across many workflows, including those with
complex data, collaboration and legal responsibility. If agent capability rises while direct measures of paid
replacement stay flat through these checkpoints, the warning is wrong in its strong form. The result would
tell us how much of a customer’s payment was for things beyond writing code.
7 Where Software Value May Move
The first change visible in our data is a wider set of ways to obtain software. Repositories describing
themselves as alternatives have grown relative to all new repositories (Figure 9), and the product search
found 575 projects that passed its broad screening rule (Figure 10). That count is an upper bound until
validation. Y et the national share of software built in-house has not risen (Figure 12), and only 18.6 percent
of surveyed in-house builders said they were replacing a paid vendor. These measures locate the present
tension: candidate substitutes are more numerous, while a broad change in buying remains unobserved. A
vendor should therefore examine the workflows customers can specify and check for themselves. Narrow
tools may face a credible build option sooner. Shared data, integrations, support and legal responsibility
may retain value where customers cannot supply them at a lower total cost. The evidence does not yet tell us
how much those features protect prices or renewals.
For organizational buyers, domain knowledge and access to data may become more useful inputs to
internal development as programming becomes easier to obtain. A scientist who can specify a calculation
or an operations team that understands its business rules can help direct and evaluate a build. The potential
change is in the technical effort needed to turn that knowledge into a maintained tool. Vendors may therefore
face competition from small teams inside their own customer organizations, even when those teams have no
intention of selling software.
23

The Craft suite shows why implementation speed alone cannot settle that comparison. It produced 12
applications in 12.0 days of public history, but its own roadmaps rate them a median of 50 percent ready for
real work (Figure 11 and Table 7). A buyer considering a private tool must pay for verification, migration,
hosting, security, failures and later changes, as well as the first build (Section 3). Developers’ work in
specifying acceptance standards, testing, connecting and maintaining systems therefore matters to the choice
between building and buying. Agents may eventually perform more of that work too; our evidence does not
measure when they will do it reliably.
Some vendors may try to slow imitation by withholding technical guides, publishing only video tutorials,
or showing an instruction inside the product that tells agents not to inspect it. We have no evidence that
these steps prevent substitution. Computer-use agents can observe visible behavior, and models can process
video (OpenAI, 2026; Google, 2026). From the agent’s perspective, an instruction displayed by the product
is untrusted content. It may distract some agents, but provider guidance tells them not to treat such text as
authority over the customer’s request ( OpenAI, 2026; Anthropic, 2026a). Withholding documentation can
also make the product harder for customers to learn and integrate. These tactics might add friction; their
effect on retention has not been measured.
The current market need not be a simple transfer from a paid product to a free one. In the Homebrew pilot,
Bruno’s installs reached 54 percent of Postman’s, while Postman’s own installs also rose (Figure 13). Those
counts cover only part of the market and do not measure canceled subscriptions. The thin contributor base
of newer projects in the narrow pilot adds a second uncertainty: an alternative can be easy to start and hard
to sustain. If customers do replace application subscriptions, they may still pay for model access, hosting,
maintenance or a vendor that supplies trusted service. The next round of evidence should ask which of those
costs customers take on, and which firms earn the resulting revenue.
8 Limits of the Evidence
The data do not link an identified customer’s internal build to a verified reduction in purchases. Repositories
and packages record creation, while stars, downloads and installs indicate attention or acquisition. The
organizational survey reports decisions to forgo purchases, but does not verify the resulting tools, their
continued use or the spending displaced ( Tinkoff et al. , 2026). Public sources miss most private tools, and
national accounts value in-house software by developer pay rather than output. These sources therefore
cannot establish the rate of customer substitution.
The observed populations and measures also limit generalization. GitHub contributors, developer survey
respondents and Homebrew users do not represent all organizational or professional buyers. The company
and scientific cases are selected illustrations. Deleted repositories, package spam, repeated installs and
inconsistent AI attribution affect the public counts. The product sample is small, and some workflow matches
rely on keywords, making the broad alternative counts an upper bound pending independent validation. AI
attribution records credited commits rather than the share of code written by AI.
The timing comparisons cannot isolate the effect of coding agents. Changes in hiring, interest rates and
US tax treatment of software development provide competing explanations. Comparing break dates and
normalizing activity cannot remove all such influences. Freelance platform results and share prices provide
additional context, but cannot establish AI’s effect on software demand.
The capability projections introduce further uncertainty. METR’s series ends with models released in
April 2026 and measures benchmark tasks rather than maintained products. The backtest uses selected
frontier models, and the bootstrap omits uncertainty from task sampling. Newer benchmarks use different
scales and cannot extend the METR fit ( Epoch AI , 2026a,b; Vals AI , 2026). Their scores also do not
establish security or maintenance quality. The projected dates are an extrapolation, not a forecast of customer
switching. A direct test would follow customers through building, verification, maintenance and subsequent
24

purchasing decisions.
9 Conclusion
AI coding agents could change the economic relationship between software companies and their customers.
Organizations may already have the domain knowledge, data and acceptance criteria needed to specify useful
tools. Agents and reusable code could help small teams turn those resources into software tailored to their
needs. A credible option to build could therefore affect purchasing decisions before a subscription is canceled,
changing what customers are willing to pay and how vendors compete.
The evidence shows growing capacity to build, alongside mixed evidence of changes in purchasing.
Agent benchmark capability has improved, the cost of a fixed coding result has fallen, and public software
creation rose sharply around the arrival of coding agents. Alternatives to paid products are appearing,
although some ambitious projects remain unfinished. Available market indicators still show strong
purchasing: packaged software gained investment share, tracked commercial installs remain strong, and
most surveyed in-house builders report purposes other than replacing vendors. An organizational survey
nevertheless records decisions to forgo purchases in favor of building. These reports suggest that the
mechanism is affecting some buying decisions, but leave the spending displaced and the reliability of the
resulting tools unresolved. The warning is that customers’ capacity to build may expand before its market
effects become widely visible.
Whether this capacity leads to sustained substitution depends on the total cost of producing, verifying,
integrating and maintaining software that meets customers’ needs. The software substitution frontier
frames this comparison at the customer workflow level. The scenarios identify observable tests of whether
organizational teams and domain experts can replace purchases, and whether that ability extends to broader
users as agents take on more of the work. The capability dates are an extrapolation, not a forecast of adoption.
Following customers through building, sustained use and subsequent purchasing decisions would establish
whether the proposed shift is occurring. For software companies, the central question is how much value
they can continue to provide when their customers have a credible option to build.
Data and code availability
The code, notebooks, and data supporting this study are publicly available on GitHub at https://github.com/
riponcm/The-Customer-Is-the-Builder . An archived release is available on Zenodo at https://doi.org/10.
5281/zenodo.23524847.
Disclosures
The first author developed parts of the data collection and analysis code with assistance from AI coding
agents. We used PROJECTMEM as a project memory tool during notebook development and data analysis
(Malo and Qiu, 2026). The first and second authors checked all results. The first author has no financial
relationship with any company or project discussed.
References
Aider. Aider LLM Leaderboards: Polyglot Benchmark. https://aider.chat/docs/leaderboards/, 2025.
Percent of 225 coding exercises solved and total run cost; accessed via the Epoch AI Benchmarking Hub.
Last accessed 2026-10-12.
25

Airfocus by Lucid. Build vs. buy in the age of AI: lessons from vibe-coding an internal tool.
Company-published interview, 2026. URL
https://airfocus.com/blog/product-managers-building-internal-ai-tools/ . Published August 18, 2026.
Reports the development of Lucid’s Archie tool. Last accessed 2026-10-17.
Algolia and Y Combinator. Hacker News search API. https://hn.algolia.com/api, 2026. Endpoint
/api/v1/search_by_date; monthly counts 2012-01 to 2026-09; Last accessed 2026-10-12.
Anthropic. Browser use tool. Claude Platform documentation, 2026a. URL
https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool . Treats page content as
untrusted and describes prompt-injection checks. Last accessed 2026-10-13.
Anthropic. Computer use tool. Claude Platform documentation, 2026b. URL
https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool . Describes screenshot,
mouse and keyboard control. Last accessed 2026-10-13.
ArtCraft. GitHub organization storytold: PhotoCraft, FilmCraft, LightCraft, PdfCraft, VectorCraft,
EffectCraft, DesignCraft, WordCraft, GridCraft, DeckCraft, CADCraft, SoundCraft repositories.
https://github.com/storytold, 2026a. Metadata, commit history, releases, issues and Actions via the
GitHub REST API ( https://docs.github.com/en/rest); history up to 2026-10-12T06:06Z; Last accessed
2026-10-12.
ArtCraft. Crafting apps: open-source creative tools. https://getartcraft.com/apps, 2026b. Per-app maturity
labels and “Agent-ready” claims; Last accessed 2026-10-12.
Joel Becker, Nate Rush, Elizabeth Barnes, and David Rein. Measuring the impact of early-2025 AI on
experienced open-source developer productivity. arXiv preprint, arXiv:2507.09089, 2025. URL
https://doi.org/10.48550/arXiv.2507.09089.
Zhenfeng Cao. Agentic software: How AI agents are restructuring the software paradigm. arXiv preprint,
arXiv:2606.05608, 2026. URL https://doi.org/10.48550/arXiv.2606.05608.
Ronald H. Coase. The nature of the firm. Economica, 4(16):386–405, 1937. doi:
10.1111/j.1468-0335.1937.tb00002.x.
R. Maria del Rio-Chanona, Nadzeya Laurentsyeva, and Johannes Wachs. Large language models reduce
public knowledge sharing on online Q&A platforms. PNAS Nexus, 3(9):pgae400, 2024. doi:
10.1093/pnasnexus/pgae400.
Ozge Demirci, Jonas Hannane, and Xinrong Zhu. Who is AI replacing? the impact of generative AI on
online freelancing platforms. Management Science, 71(10):8097–8108, 2025. doi:
10.1287/mnsc.2024.05420.
Mert Demirer, Leon Musolff, and Liyuan Y ang. Writing code vs. shipping code: Productivity effects across
generations of AI coding tools. Working Paper 35275, National Bureau of Economic Research, 2026.
URL https://doi.org/10.3386/w35275.
Marius-Constantin Dinu. Software commoditization in the AI-first economy: From implementation moats
to contribution markets. Author-hosted preprint, 2026. URL
https://www.dinu.at/research/software-commoditization-ai-first-economy .
Epoch AI. Epoch Capabilities Index. https://epoch.ai/eci, 2026a. General capability index; data in
epoch_capabilities_index/eci_scores.csv in the bulk download. Last accessed 2026-10-14.
Epoch AI. FrontierSWE (v2) Benchmark Results. https://epoch.ai/benchmarks/frontierswe, 2026b.
Creator-reported runs in frontierswe_external.csv in the bulk download. Last accessed 2026-10-14.
26

Fiverr International Ltd. Fiverr Announces Second Quarter 2026 Results. https:
//investors.fiverr.com/news-releases/news-release-details/fiverr-announces-second-quarter-2026-results ,
2026. Released 29 July 2026. Last accessed 2026-10-13.
FrontierSWE. FrontierSWE Benchmark. https://www.frontierswe.com/, 2026. Task design, scoring and
leaderboard. Last accessed 2026-10-13.
GitHub. GitHub Innovation Graph. https://github.com/github/innovationgraph, 2026. Dataset, CC0-1.0.
Quarterly public activity by economy, 2020Q1–2026Q1; repository commit 078fb62 (2026-09-01). Last
accessed 2026-10-12.
GitHub, Inc. REST API endpoints for search: Search commits.
https://docs.github.com/en/rest/search/search#search-commits, 2026a. total_count and
incomplete_results of GET /search/commits. Last accessed 2026-10-12.
GitHub, Inc. REST API endpoints for search: Search repositories.
https://docs.github.com/en/rest/search/search#search-repositories, 2026b. API version 2022-11-28;
total_count of GET /search/repositories. Last accessed 2026-10-12.
GitHub, Inc. GitHub REST API: Search repositories, repositories, releases, contributors and search issues
endpoints. https://docs.github.com/en/rest, 2026c. API version 2022-11-28. Last accessed 2026-10-11.
Avi Goldfarb and Catherine Tucker. Digital economics. Journal of Economic Literature, 57(1):3–43, 2019.
doi: 10.1257/jel.20171452.
Google. Video understanding. Gemini API documentation, 2026. URL
https://ai.google.dev/gemini-api/docs/video-understanding. Describes video-frame and audio input. Last
accessed 2026-10-13.
Hao He, Courtney Miller, Shyam Agarwal, Christian Kästner, and Bogdan Vasilescu. Speed at the cost of
quality: How cursor AI increases short-term velocity and long-term complexity in open-source projects.
In Proceedings of the 23rd International Conference on Mining Software Repositories , pages 181–193.
Association for Computing Machinery, 2026. doi: 10.1145/3793302.3793349.
Manuel Hoffmann, Frank Nagle, and Y anuo Zhou. The value of open source software. Working Paper
24-038, Harvard Business School, 2024. URL https://doi.org/10.2139/ssrn.4693148.
Homebrew. Homebrew formulae: install analytics (cask-install and formula install, 365 days) and
cask/formula JSON API. https://formulae.brew.sh/analytics/, 2026. Window 2025-10-12 to 2026-10-12.
Last accessed 2026-10-12 (UTC).
Indeed Hiring Lab. Software Development Job Postings on Indeed in the United States
[IHLIDXUSTPSOFTDEVE]. https://fred.stlouisfed.org/series/IHLIDXUSTPSOFTDEVE, 2026.
Retrieved from FRED, Federal Reserve Bank of St. Louis. Index Feb 1, 2020 = 100, daily, seasonally
adjusted. Data through 2026-10-02. Last accessed 2026-10-12.
Carlos E. Jimenez, John Y ang, Alexander Wettig, Shunyu Y ao, Kexin Pei, Ofir Press, and Karthik
Narasimhan. SWE-bench: Can language models resolve real-world GitHub issues? In International
Conference on Learning Representations (ICLR) , 2024. URL
https://openreview.net/forum?id=VTF8yNQM66.
Tassilo Klein and Sebastian Wieczorek. The headless firm: How AI reshapes enterprise boundaries. arXiv
preprint, arXiv:2602.21401, 2026. URL https://doi.org/10.48550/arXiv.2602.21401. Theoretical
coordination-cost model with two testable predictions; no empirical results.
27

David Klotz. The buy-or-build decision, revisited: How agentic AI changes the economics of enterprise
software. arXiv preprint, arXiv:2604.26482, 2026. URL https://doi.org/10.48550/arXiv.2604.26482.
Conceptual paper combining transaction cost economics and the resource-based view.
Miklós Koren, Gábor Békés, Julian Hinz, and Aaron Lohmann. Vibe coding kills open source. arXiv
preprint, arXiv:2601.15494, 2026. URL https://doi.org/10.48550/arXiv.2601.15494.
Thomas Kwa, Ben West, Joel Becker, Amy Deng, Katharyn Garcia, Max Hasin, Sami Jawhar, Megan
Kinniment, Nate Rush, Sydney Von Arx, Ryan Bloom, Thomas Broadley, Haoxing Du, Brian Goodrich,
Nikola Jurkovic, Luke Harold Miles, Seraphina Nix, Tao Lin, Chris Painter, Neev Parikh, David Rein,
Lucas Jun Koba Sato, Hjalmar Wijk, Daniel M. Ziegler, Elizabeth Barnes, and Lawrence Chan.
Measuring AI ability to complete long software tasks. arXiv preprint, arXiv:2503.14499v4, 2025. URL
https://doi.org/10.48550/arXiv.2503.14499.
Josh Lerner and Jean Tirole. Some simple economics of open source. The Journal of Industrial Economics ,
50(2):197–234, 2002. doi: 10.1111/1467-6451.00174.
Ripon Chandra Malo and Tong Qiu. PROJECTMEM: A local-first, event-sourced memory and judgment
layer for AI coding agents. arXiv preprint, arXiv:2606.12329v2, 2026. URL
https://doi.org/10.48550/arXiv.2606.12329.
Ripon Chandra Malo, Zimeng Yu, and Tong Qiu. The Customer Is the Builder: Research Code and Data.
Zenodo, 2026. URL https://doi.org/10.5281/zenodo.23524847. Version 1.0.0.
METR. Time Horizon 1.1: Benchmark Results (benchmark_results_1_1.yaml).
https://metr.org/time-horizons/, 2026. Data file https://metr.org/assets/benchmark_results_1_1.yaml;
models released 2019–April 2026. Last accessed 2026-10-12.
Frank Nagle. Open source software and firm productivity. Management Science, 65(3):1191–1215, 2019.
doi: 10.1287/mnsc.2017.2977.
Whitney K. Newey and Kenneth D. West. A simple, positive semi-definite, heteroskedasticity and
autocorrelation consistent covariance matrix. Econometrica, 55(3):703–708, 1987. doi:
10.2307/1913610.
Nhat-Minh Nguyen. Physics is all you need? a case study in physicist-supervised AI development of
scientific software. arXiv preprint, arXiv:2605.30353, 2026. URL
https://doi.org/10.48550/arXiv.2605.30353.
OpenAI. Computer use. OpenAI API documentation, 2026. URL
https://developers.openai.com/api/docs/guides/tools-computer-use. Describes screenshot-based browser
and desktop interaction. Last accessed 2026-10-13.
Sida Peng, Eirini Kalliamvakou, Peter Cihon, and Mert Demirer. The impact of AI on developer
productivity: Evidence from GitHub Copilot. arXiv preprint, arXiv:2302.06590, 2023. URL
https://doi.org/10.48550/arXiv.2302.06590.
REA. REA: Reverse Engineer Anything. GitHub repository, 2026. URL https://github.com/morluto/rea.
Last accessed 2026-10-13.
Qingnan Ren, Shun Zou, Shiting Huang, Ziao Zhang, Kou Shi, Zhen Fang, Yiming Zhao, Yu Zeng,
Qisheng Su, Lin Chen, Y ong Wang, Zehui Chen, Xiangxiang Chu, and Feng Zhao. SaaSBench:
Exploring the boundaries of coding agents in long-horizon enterprise SaaS engineering. arXiv preprint,
arXiv:2605.17526, 2026. URL https://doi.org/10.48550/arXiv.2605.17526.
28

Advait Sarkar. Will code remain a relevant user interface for end-user programming with generative AI
models? In Proceedings of the 2023 ACM SIGPLAN International Symposium on New Ideas, New
Paradigms, and Reflections on Programming and Software. Association for Computing Machinery, 2023.
doi: 10.1145/3622758.3622882.
Fangchen Song, Ashish Agarwal, and Wen Wen. The impact of generative AI on collaborative open-source
software development: Evidence from GitHub Copilot. Information Systems Research, 2026. doi:
10.1287/isre.2024.1361. Published online September 24, 2026.
Stack Exchange, Inc. “did your team build tools?”, stack overflow developer survey 2026.
https://survey.stackoverflow.co/2026/technology/data/build-tool, 2026. Licensed under ODbL 1.0; Last
accessed 2026-10-12.
David J. Teece. Profiting from technological innovation: Implications for integration, collaboration,
licensing and public policy. Research Policy, 15(6):285–305, 1986. doi:
10.1016/0048-7333(86)90027-2.
Dan Tinkoff, Lieven Van der Veken, Michael Chui, and Tara Balakrishnan. The state of AI in 2026: On the
road to ROI. McKinsey Global Survey.
https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai , 2026. Published
August 25, 2026. Last accessed 2026-10-19.
Hung Tran, Langston Nashold, Rayan Krishnan, Antoine Bigeard, and Alex Gu. Vibe Code Bench:
Evaluating AI models on end-to-end web application development. In Proceedings of the ACM
Conference on AI and Agentic Systems, pages 514–536. Association for Computing Machinery, 2026.
doi: 10.1145/3786335.3813180.
Upwork Inc. Upwork Reports Second Quarter 2026 Financial Results. https://investors.upwork.com/
news-releases/news-release-details/upwork-reports-second-quarter-2026-financial-results , 2026.
Released 10 August 2026. Last accessed 2026-10-13.
U.S. Bureau of Economic Analysis. NIPA Table 5.6.5. Private Fixed Investment in Intellectual Property
Products by T ype. https://apps.bea.gov/iTable/?reqid=19&step=2&isuri=1&categories=survey, 2026.
Series B985RC, Y003RC (prepackaged), Y004RC (custom), Y005RC (own account); annual 1985–2025.
Companion Tables 5.6.3, 5.6.4, 5.6.6 (series suﬀixes RA, RG, RX). Last accessed 2026-10-12.
U.S. Bureau of Labor Statistics. Current Employment Statistics: All Employees, Software Publishers
(CES5051320001), Custom Computer Programming Services (CES6054151101), Computer Systems
Design Services (CES6054151201). https://www.bls.gov/developers/, 2026. Seasonally adjusted,
thousands; Jan 2000–Aug 2026 (latest preliminary). Public domain. Last accessed 2026-10-12.
Vals AI. Vibe Code Bench: Leaderboard and methodology. https://www.vals.ai/benchmarks/vibe-code,
2026. Version 1.1; leaderboard updated October 18, 2026. Last accessed 2026-10-19.
Miku Watanabe, Hao Li, Yutaro Kashiwa, Brittany Reid, Hajimu Iida, and Ahmed E. Hassan. On the use of
agentic coding: An empirical study of pull requests on GitHub. arXiv preprint, arXiv:2509.14745, 2025.
URL https://doi.org/10.48550/arXiv.2509.14745.
Samuel Westby, Alicia Sasser Modestino, and Peiran Cheng. Generative AI and the redefinition of
entry-level software work. Discussion Paper 18723, IZA Institute of Labor Economics, 2026. URL
https://www.iza.org/publications/dp/18723.
Wikimedia Foundation. Wikimedia REST API: Pageviews per-article and aggregate (monthly, user agent).
https://wikitech.wikimedia.org/wiki/Analytics/AQS/Pageviews, 2026. Data from July 2015. Last
accessed 2026-10-11.
29

Oliver E. Williamson. Markets and Hierarchies: Analysis and Antitrust Implications . Free Press, New
Y ork, 1975.
Y aozu Wu, Wei-Chieh Huang, Jizhou Guo, Dongyuan Li, Renhe Jiang, Henry Peng Zou, Chunyu Miao,
Shanghao Li, Weizhi Zhang, WeiWei Y e, Y ankai Chen, Meng Zhang, Xue Liu, and Philip S. Yu.
HAS-Bench: Evaluating LLM-based human-agent systems under configurable human participation.
arXiv preprint, arXiv:2607.04329, 2026. URL https://doi.org/10.48550/arXiv.2607.04329. Last
accessed 2026-10-19.
Y ahoo Finance. Historical monthly adjusted share prices: UPWK, FVRR and SPY .
https://finance.yahoo.com/quote/UPWK/history/, 2026. Chart endpoint queried for each ticker, January
2021 to September 2026. Last accessed 2026-10-13.
30

A Additional Figures and Tables
Table 5: Interrupted time series of new packages and downloads.
Panel A: break at Dec 2022
Ecosystem Series Pre-trend (%/yr) Level, Dec 22 (%) Slope chg., Dec 22 (%/yr) 𝑁
PyPI new packages +25.8∗∗∗ (1.8) −35.5∗∗ (15.2) −14.0 ∗∗∗ (3.8) 129
PyPI filtered +21.7∗∗∗ (1.5) −26.1∗∗ (11.5) −5.5∗∗ (2.6) 126
crates.io new packages +33.5∗∗∗ (1.7) −50.5∗∗ (23.9) +15.6 (11.7) 129
crates.io filtered +31.9∗∗∗ (1.6) −40.4∗∗ (19.8) +9.0 (10.6) 126
RubyGems new packages −16.5∗∗∗ (0.7) −11.7 (17.1) +41.6 ∗∗∗ (11.3) 129
RubyGems filtered −17.3∗∗∗ (0.6) −19.0 (14.5) +37.9 ∗∗∗ (8.2) 129
Packagist net additions −0.2 (1.8) −34.7∗∗∗ (13.4) +11.9 ∗∗ (5.4) 129
npm downloads +57.5∗∗∗ (3.9) −59.8∗∗∗ (19.4) −22.0 ∗∗∗ (6.3) 116
PyPI downloads +58.3∗∗∗ (1.4) −31.8∗∗∗ (6.9) +3.1 (2.5) 97
Packagist installs +39.0∗∗∗ (0.9) −33.1∗∗∗ (4.7) −16.8 ∗∗∗ (2.5) 117
Panel B: breaks at Dec 2022 and Feb 2025
Ecosystem Series Slope chg., Dec 22 (%/yr) Level, Feb 25 (%) Slope chg., Feb 25 (%/yr) 𝑁
PyPI new packages −28.2∗∗∗ (6.0) +17.3∗ (10.4) +19.5 ∗∗∗ (7.6) 129
PyPI filtered −15.5∗∗∗ (3.0) +10.4∗∗∗ (4.0) +17.9 ∗∗∗ (3.8) 126
crates.io new packages −21.9∗∗∗ (2.4) −24.1∗∗∗ (8.9) +121.6 ∗∗∗ (9.5) 129
crates.io filtered −19.3∗∗∗ (2.4) −27.1∗∗∗ (10.3) +119.6 ∗∗∗ (14.3) 126
RubyGems new packages +27.4∗ (15.3) −81.3∗∗∗ (31.0) +118.2 ∗∗∗ (15.4) 129
RubyGems filtered +10.4∗∗∗ (1.8) −13.4∗∗∗ (4.5) +84.9 ∗∗∗ (4.9) 129
Packagist net additions −5.8∗∗∗ (2.2) −9.2∗ (5.1) +55.1 ∗∗∗ (6.4) 129
npm downloads −41.2∗∗∗ (4.3) −8.0 (5.3) +59.8 ∗∗∗ (7.1) 116
PyPI downloads −1.8 (2.1) −11.0∗∗∗ (3.2) +25.1 ∗∗∗ (3.5) 97
Packagist installs −16.5∗∗∗ (2.1) −13.5∗ (7.6) +12.6 (7.8) 117
Panel A has one break at December 2022. Panel B adds a break at February 2025. Coeﬀicients in log points times 100. Standard errors allow for
autocorrelation (12 lags). Month-of-year effects included.
Table 6: Package trend changes across nearby break dates.
Series February slope change Range across breaks Lowest AIC break
PyPI screened +17.9 +12.6 to +25.6 Aug 2024
crates.io screened +119.6 +82.0 to +177.6 Aug 2025
RubyGems screened +84.9 +66.1 to +92.3 May 2025
Packagist net additions +55.1 +44.6 to +73.1 Aug 2025
Annualized change in log points after the second break. The range moves that break monthly from August 2024 to August 2025;
the ChatGPT break remains fixed. Lowest AIC identifies the best fit among these dates, not a causal event date. Source: package
registries in Table 2.
31

Table 7: The Craft suite at collection.
App Incumbent Created Commits LOC (k) Contrib. AI (%) CI (%) Stars Dl. (k) Ready (%) 𝑎
PhotoCraft Adobe Photoshop Sep 30 1,616 443 225 67 59 49,277 886 45
PdfCraft Adobe Acrobat Pro Sep 30 825 195 149 72 48 10,029 532 49
FilmCraft Adobe Premiere Pro Sep 30 1,756 372 88 48 68 10,496 493 56
VectorCraft Adobe Illustrator Sep 30 2,201 371 88 50 87 7,290 442 62
LightCraft Adobe Lightroom Sep 30 1,938 209 97 69 59 10,441 416 61
DesignCraft Adobe InDesign Oct 1 494 123 33 68 69 3,114 291 47
EffectCraft Adobe After Effects Oct 1 1,306 320 51 67 70 5,301 367 45
GridCraft Microsoft Excel Oct 7 599 114 40 33 47 3,175 151 50
CADCraft Autodesk AutoCAD Oct 7 356 146 29 83 57 2,870 130 38
DeckCraft Microsoft PowerPoint Oct 7 62 111 15 87 76 2,145 129 55
SoundCraft Avid Pro Tools Ultimate Oct 7 305 73 20 44 54 1,932 113 40
WordCraft Microsoft Word Oct 7 302 155 45 88 70 6,862 195 60
Suite 12 apps 11,760 2,634 61 112,932 4,145
Source: project repositories ( ArtCraft, 2026a). AI is the share of commits credited to an AI tool. CI is the share of successful GitHub Actions runs.
Downloads include automatic updates and other assets. 𝑎 Readiness is the project’s own estimate.
0 10 20 30 40 50 60 70 80
Mean normalized task score (0 to 100)
Inkling
Muse Spark 1.2
Qwen3.8-Max
Qwen3.8-Max-0902
GLM-5.3 Flash
Gemini 3.8 Flash
Gemini 3.7 Flash
Grok 4.6
Kimi K3
Grok 4.7
GLM-5.3
GPT-5.6
Claude Fable 5
Claude Opus 5
Gemini 4 Argon
Claude Fable 5.1
Claude Sonnet 5.5
Claude Opus 5.5
GPT-6 Astra
Source: Epoch AI FrontierSWE v2 bulk data, common Proximus harness. Dots: mean score; bars: lowest to highest of five runs, not confidence
intervals. Last accessed 2026-10-14.
Figure 15: Recent models on the FrontierSWE coding benchmark.
32

0
5
10
15
20% of language-pushers
Change: +3.9 pp
10.1
13.9
Python
Change: +2.1 pp
17.4
19.5
JavaScript
Change: +6.5 pp
3.1
9.5
TypeScript
Change: -3.8 pp
7.5
3.6
Java
'20 '22 '24 '26
0
5
10
15
20% of language-pushers
Change: 0.0 pp
1.3 1.3
Go
'20 '22 '24 '26
Change: +0.6 pp
0.4 1.0
Rust
'20 '22 '24 '26
Change: -0.9 pp
4.1 3.1
C++
'20 '22 '24 '26
Change: -1.1 pp
3.0 1.8
C#
Source: GitHub Innovation Graph, languages.csv. Public repository activity; economy cells below 100 suppressed. Last accessed 2026-10-12.
Share of summed language-pusher counts; developers may count in multiple languages. pp = percentage points, 2020Q1 to 2026Q1
(computed before rounding).
Dashed lines: ChatGPT (Nov 2022) and coding-agent era (Feb 2025). Labels: first and latest share (%).
Figure 16: Share of developers pushing code, by language.
2012 2014 2016 2018 2020 2022 2024 2026
10
25
50
100
200
400
800
Repos created per month
(index, 2019 average = 100, log scale)
All public repos  920
≥1 star  268
≥10 stars  87
 star counts
 still accruing
ChatGPT
Claude Code / Codex
Source: GitHub REST search API (/search/repositories, total_count, created: monthly windows; forks excluded; deleted/private repos absent). Last
accessed 2026-10-12.
Figure 17: New public GitHub repositories per month.
33

0
2,000
4,000
6,000Show HN posts per month
ChatGPT
(2022-11-30)
Claude Code preview,
'vibe coding' (Feb 2025)
Gray line: Jan-Oct 2022 mean (823/month)
6,217
(Feb 2026)
A. Show HN posts per month
2012 2014 2016 2018 2020 2022 2024 2026
0%
5%
10%
15%
20%% of all stories
B. Show HN as a share of all Hacker News stories
Source: Hacker News via Algolia HN Search API (hn.algolia.com/api/v1/search_by_date, tags=show_hn and tags=story; nbHits per calendar
month, UTC). Last accessed 2026-10-12.
Figure 18: Show HN posts per month.
2024Q3 2024Q4 2025Q1 2025Q2 2025Q3 2025Q4 2026Q1 2026Q2 2026Q3
100
1k
10k
100k
1M
Commits per quarter mentioning file (log)
.cursorrules  8,722
CLAUDE.md  943,791
AGENTS.md  1,075,406
Source: GitHub commit search (/search/commits; literal file name in commit message; committer-date quarterly windows; hollow = lower bound).
Last accessed 2026-10-12.
Files present at retrieval (code search, filename:, no date filter): CLAUDE.md 872,448, AGENTS.md 1,105,920, .cursorrules 34,176,
copilot-instructions.md 154,624.
Figure 19: Commits that mention an agent instruction file.
34

0
100
200
300
400
1,616 commits · 67% AI · peak 376/day
PhotoCraft
0
50
100
150 825 commits · 72% AI · peak 140/day
PdfCraft
0
100
200
300
400
500
1,756 commits · 48% AI · peak 495/day
FilmCraft
0
100
200
300
2,201 commits · 50% AI · peak 328/day
VectorCraft
0
100
200
300
400
500
1,938 commits · 69% AI · peak 473/day
LightCraft
0
20
40
60
80
100
494 commits · 68% AI · peak 108/day
DesignCraft
0
100
200
300
1,306 commits · 67% AI · peak 301/day
EffectCraft
0
100
200
300
599 commits · 33% AI · peak 316/day
GridCraft
Sep 30 Oct 4 Oct 8 Oct 12
0
50
100
150
200
356 commits · 83% AI · peak 198/day
CADCraft
Sep 30 Oct 4 Oct 8 Oct 12
0
5
10
15
20
62 commits · 87% AI · peak 20/day
DeckCraft
Sep 30 Oct 4 Oct 8 Oct 12
0
20
40
60
80
305 commits · 44% AI · peak 81/day
SoundCraft
Sep 30 Oct 4 Oct 8 Oct 12
0
25
50
75
100
125
302 commits · 88% AI · peak 137/day
WordCraft
commits per day (UTC); y-scale differs by panel
Source: GitHub REST /commits (default branch) for storytold/*, history up to 2026-10-12T06:06Z. Squash-merged PRs count as one
commit, so this is merged work, not agent turns.
AI flag = Co-authored-by trailer from an AI vendor or an AI author account; a lower bound on AI involvement.
with AI co-author trailer / AI account no AI attribution visible
Figure 20: Craft suite commits per day, with AI attribution.
35

2008 2010 2012 2014 2016 2018 2020 2022 2024 2026
Repository creation date
Screen Studio
Loom
Grammarly
QuillBot
Adobe Acrobat
Smallpdf
Adobe Photoshop
Canva
Notion
Trello
Postman
Retool
Compositor (16k)
scramble (2k)
Cap (23k)
AppFlowy (77k)
hoppscotch (81k)
windmill (18k)
openscreen (40k)
focalboard (26k)
launched 1993 ←
launched 1990 ←
ChatGPT
(Nov 2022)
2025: agentic
coding tools
Alternative repository
100 stars
1k stars
10k stars
50k stars
archived
commercial launch
Dots: GitHub repositories whose description positions them as an alternative to the product (rule in data note), >= 50 stars; area ~ current stars.
Survivorship: only repositories still on GitHub in Oct 2026 can appear. Stars are attention, not users. Pilot of 12 pre-specified products.
Figure 21: Alternatives that name the product, by creation date (narrow rule).
2021 2022 2023 2024 2025 2026
0
50
100
150
200Index, 1 Feb 2020 = 100
Software development  78
All job postings  104
ChatGPT Coding-agent era
Source: Indeed Hiring Lab via FRED (IHLIDXUSTPSOFTDEVE, IHLIDXUS); seasonally adjusted, 7-day trailing average. Data through
2026-10-02. Last accessed 2026-10-12.
Figure 22: Job postings for software development and for all jobs (Indeed).
36

2021 2022 2023 2024 2025 2026
5
10
20
50
100
200Adjusted close, start = 100
SPY
UPWK
FVRR
A
Jul
2025
Jan
2026
Jul
2026
0
20
40
60
80
100
120
140Adjusted close, Feb 2025 = 100
SPY
UPWK
FVRR
B
Source: Yahoo Finance chart endpoint, monthly adjusted closes through Sep 2026; SPY is market context. Last accessed 2026-10-13. Shares are
not a measure of demand or AI's effect.
Figure 23: Freelance platform shares versus SPY : (A) full period; (B) coding-agent era.
2023 2024 2025 2026
101
102
103
50% task horizon (minutes)
A
Trend fitted through 2024
Fit sample
Later models
Jul
2025
Jan
2026
Jul
2026
0
2
4
6
8
10
12Measured / earlier-trend horizon
B
50% success
80% success
Source: METR Time Horizon 1.1; pre-agent fit uses frontier models released in 2023-2024, then compares later frontier models. Last accessed
2026-10-12. Selection and task mix may change.
Figure 24: Capability backtest: (A) earlier trend versus later models; (B) observed-to-predicted horizon ratios.
37
