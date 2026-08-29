# Research Gaps in Contextual Intelligence for Marketing

**Analysis grounded in the marketing-research corpus (7,778 papers, `papers.yaml`),
the concept graph (`concept_graph.json` / `concepts.json`), the Bayesian trend data
(`docs/research/bayesian_trends.json`), and the landscape/trend/literature reports.**

## What "contextual intelligence" means here

Contextual intelligence = an AI/marketing system's ability to **sense, represent, and
act on the situation** in which a decision, message, or transaction occurs — going beyond
the *who* (identity/behavioral profile) to the *where, when, how, and why* of the moment.
In marketing this spans: contextual & semantic advertising, situation-aware
personalization, real-time omnichannel context, intent understanding, and (in the agentic
paradigm) the situational awareness that lets autonomous agents act appropriately.

## Hard gap signals from the corpus (evidence first)

| Signal | Corpus count | Implication |
|--------|-------------|-------------|
| "contextual intelligence" (as a concept) | **0** | The idea does not yet exist as a named research object |
| "situation awareness" | **0** | No cross-disciplinary borrowing of the concept from HCI/military/AI |
| "world model" | **1** | Context *representation* (models of the user+environment state) essentially absent |
| "agentic" | 41, burst **1.79×** | Agentic marketing is booming but never tied to situational awareness |
| "contextual" (as term) | 32 | Mostly confined to *contextual advertising* (a cookieless replacement playbook) |
| "context-aware" | 3–4 | Rarely appears as a general marketing capability |
| "semantic" | 18 | Semantic/contextual targeting present but thin and fragmented |
| "intent" | 622 | Rich intent literature exists, but is **not** connected to context/situational framing |

## The gap: three disconnects

1. **Contextual ≠ identity, but the corpus treats context only as a cookie substitute.**
   Almost every "contextual" paper sits in the cookieless/privacy-first playbook
   (replacing third-party cookies with contextual signals as a *fallback*), e.g.
   *AI-Driven Contextual Advertising* (2024), *Intent Graphs* (2026), *From Cookies to
   Context* (2025). Nobody treats contextual intelligence as a *superior* or *general*
   marketing capability in its own right.

2. **Agentic AI and situational awareness are two separate literatures.**
   The corpus's hottest burst (agentic, multi-agent, world model, simulation) is about
   AI *agents'* planning — but not about agents reading *marketing* context (audience
   situation, channel journey, moment-of-truth). The conceptual bridge of
   **situation-aware autonomous marketing agents** is unbuilt.

3. **No shared theory/construct.**
   "Context" appears 365 times but as a loose adjective, not an operationalized
   construct. There is no framework that defines *contextual intelligence* as a
   measurable marketing capability (dimensions, antecedents, outcomes, measurement
   instrument) — the field's **theory** and **measurement** cells around it are empty.

## Top research gaps answerable via contextual-intelligence research

### G1 — A conceptual framework / construct definition (theory gap)
Define and dimensionalize **contextual intelligence for marketing** (situational,
spatial/temporal, channel, social, and intent context) and how it differs from
traditional profile/identity-based targeting. This fills the `analytics/theory` and
`b2b/theory` thin cells (35 and 42 papers respectively) and gives the field a shared
vocabulary. Companion to Haas's conceptual-papers agenda.

### G2 — Measurement instrument (measurement gap)
Operationalize contextual intelligence as a **measurable capability** (a validated
scale / metric). The `analytics/measurement` cell is dense, but no instrument exists
for contextual intelligence. Directly supports the corpus's #1 durable trend —
**measurement, incrementality & MMM** — by adding context as a causal factor.

### G3 — Context-aware vs. identity-based targeting: effect study (empirical gap)
A controlled comparison of **contextual-intelligence-driven targeting vs. identity/
behavioral targeting** on outcomes (engagement, conversion, incrementality) —
especially relevant post-cookie. The corpus has the papers claiming contextual works
(_AI-Driven Contextual Advertising_) but no rigorous causal/field evidence. Fills both
`analytics/empirical` and the privacy-first narrative with hard numbers.

### G4 — Situational awareness for autonomous marketing agents (frontier gap)
How do **agentic marketing systems** acquire and act on context? A framework + prototype
tying the corpus's agentic/world-model burst to marketing situational awareness. This is
the single least-covered, highest-momentum gap — no paper in the corpus connects agents
with marketing context. Ideal for a **framework + benchmark** contribution.

### G5 — Omnichannel real-time context fusion (CX gap)
How to **fuse context across touchpoints in real time** (the `cx-retail` and
`omnichannel` space) into a single situational state, and evaluate when context fusion
improves the customer journey vs. adds noise/privacy cost. There's an `omnichannel`
cluster (200) but it treats channels as silos, not as a fused situational context.

### G6 — B2B contextual intelligence (B2B gap)
Contextual intelligence in **B2B/ABM** — firmographic + buying-situation + journey-stage
context for account engagement. The `b2b` cells are among the thinnest (measurement 7
papers, review 41, theory 42) yet B2B is the fastest-growing domain (share up 1.18×).
This pairs naturally with the Alexander Haas collaboration (value-based selling, B2B
sales management).

## Suggested positioning

**"Contextual intelligence" is a white-space concept** — a unifying umbrella over the
corpus's currently-fragmented contextual-advertising, intent, and agentic threads. The
most defensible, publishable series of contributions:

1. **Theory/framework paper** (G1) — define & dimensionalize the construct. 
2. **Measurement instrument** (G2) — the scale that makes it testable. 
3. **An agentic situational-awareness framework + benchmark** (G4) — the frontier, tied
   to the corpus's #1 trend (agentic, 1.79×) and its #1 durable trend (measurement).
4. **B2B application** (G6) — the fastest-growing domain, and the natural hook for the
   Haas collaboration (value-based selling in context-rich B2B situations).

These are gaps **this corpus can directly evidence and de-risk** — because a 7,700-paper
evidence base and the existing trend/landscape tooling can validate that the construct
is novel, growing, and under-served.

---

# External confirmation (lived literature, cross-checked 2026-08-28)

To verify the gaps are real in the wider academic record — not just absent from this
corpus — the following evidence was gathered from Crossref, (rate-limited)
Semantic Scholar/arXiv, and web search.

## 1. The term exists in INDUSTRY, not in marketing ACADEMIA
Web search shows "contextual intelligence" is an established **practitioner/adtech
term**: adtech vendors (zvelo, Adtech Juice, GumGum-style vendors) publish pieces
like "Contextual Intelligence 101: The Future of Smart Advertising", "What Is a
Contextual Intelligence Loop", "Contextual Intelligence Beyond Advertising". This is
marketing-vendor vocabulary with **no academic construct definition behind it** — a
classic theory-lag: practice uses the term; research has not yet defined/measured it.

## 2. Academic prior art is a DIFFERENT (older) meaning
Crossref shows "Contextual Intelligence" as a title in two lineages, neither of which
is modern AI-driven marketing:
- **Leadership/strategic management** — Matthew Kutz's *Contextual Intelligence* book
  (2016, rev. 2025 with chapters "What Is Contextual Intelligence?", "Learning
  Contextual Intelligence", "The Contextual Intelligence Behaviors", "Developing
  Contextual Intelligence", etc.). Meaning = an individual leader's situational
  adaptability across contexts. Well-served in management; not marketing, not AI.
- **Marketing-strategy (2007-2008)** — *Market-Driven Thinking: Achieving Contextual
  Intelligence* (J. Consumer Marketing, 2007); *Contextual intelligence and
  flexibility: understanding today's marketing environment* (Mark. Intell. & Plann.,
  2008). Meaning = strategic/market orientation flexibility. This predates
  generative AI entirely and has no data/AI/agentic dimension.

## 3. What marketing research does today — and what it's NOT
Recent marketing/advertising research (2022-2026) uses the word "contextual"
operationally, not as a construct:
- `AI-Driven Contextual Advertising` (J. Current Issues & Res. in Adv., 2024) —
  privacy-first contextual targeting as a *cookie replacement*.
- `Contextual Advertising Strategy Generation via Attention and Interaction Guidance`
  (IEEE DSAA, 2023, Benamara & Viennet) — algorithmic/adtech mechanics.
- `Marketing Strategies in the Era of Mobile Applications: Geolocation and Context`
  (2024) — context reduced to geolocation.
- `Intent Graphs` (2026), `From Cookies to Context` (2025) — cookieless-playbook papers.

None of these **defines "contextual intelligence" as a marketing capability** with a
construct, dimensions, or measurement. The CS side (IEEE) optimizes contextual ad
*algorithms*; the strategy side (2007-08, Kutz) means *managerial adaptability*; the
adtech side (industry) uses the term *without theory*.

## 4. Interest is rising (novelty + momentum)
**VERIFIED (2026-08-29 via BrowserMCP/DiVA):** A 2025 PhD thesis has claimed the
phrase: **Emil Häglund, *"Contextual intelligence: leveraging AI for targeted
marketing"*, Umeå University (Dept. of Computing Science), defended 2025-06-05**
(URN urn:nbn:se:umu:diva-238303; ISBN 978-91-8070-691-9; ORCID 0009-0005-2356-1286;
supervisors J. Björklund & A. Åbonde Garke; opponent B. Jansen). It is a
**computer-science / NLP program** (opinion-unit extraction, aspect-based sentiment,
media-context effects on ad perception, contextual-vs-personalized trade-offs),
with 6 published papers — its flagship *"AI-Driven Contextual Advertising: Toward
Relevant Messaging Without Personal Data"* (J. Current Issues & Res. in Adv., 2024)
is already in this corpus. It does **not** deliver a marketing *construct*
(no definition/dimensions as a firm capability, no nomological net, no scale, no
agentic/omnichannel/B2B). This confirms the construct is being claimed at the maths
frontier — but the *marketing* construct space remains open, and **first-mover
positioning is urgent**: a peer-reviewed marketing definition should move ahead to
set the terms.

## 5. Confirmation verdict per gap
| Gap | Confirmed? | Evidence |
|-----|-----------|----------|
| G1 (no modern AI-marketing construct) | ✅ | Prior art is 2007-08 strategy + Kutz leadership; no AI/adtech marketing construct |
| G2 (no measurement instrument) | ✅ | No scale/instrument anywhere for marketing CI; not in corpus, not in Crossref |
| G3 (no causal effect study vs identity targeting) | ✅ | Only privacy-playbook papers; no field/causal comparison |
| G4 (no agentic situational-awareness marketing) | ✅ | Corpus agentic burst (1.79×) never linked to marketing context; no external paper either |
| G5 (no omnichannel real-time context fusion) | ✅ | Omnichannel treated as siloed channels; no fused-situational-state work |
| G6 (no B2B contextual intelligence) | ✅ | B2B cells thinnest (measurement=7); no B2B CI construct anywhere |

## Refined positioning (from external evidence)
The defensible contribution is to **rescue the term from the 2007-08 strategic meaning
and the adtech/industry usage, and re-theorize it as a modern, AI-driven, measurable
marketing capability** — bridging the corpus's fragmented contextual-advertising,
intent, and agentic threads. Priority order remains:
1. **G1 Theory/framework** — define & dimensionalize modern marketing CI (explicitly
distinguished from Kutz's leadership CI and 2008 strategic CI).
2. **G2 Measurement** — the instrument that makes it testable.
3. **G4 Agentic situational awareness** — ties to the corpus's #1 burst (agentic) and
#1 durable trend (measurement); least-covered + highest momentum.
4. **G6 B2B** — fastest-growing domain; the Haas value-based-selling hook.

> Urgency note: with Häglund's 2025 Umeå PhD thesis (computer-science/NLP) already
> staking the phrase, timing matters — a peer-reviewed *marketing* framework/construct
> paper (ours) should move ahead to define the terms, explicitly cited as nearest
> prior art (see g1_contextual_intelligence_framework.md §4).

---
*Corpus + external cross-check. Not a pipeline output; safe to edit.*
