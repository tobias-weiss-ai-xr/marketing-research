---
marp: true
theme: default
paginate: true
header: '![h:56](img/jlu-logo.png)'
footer: 'Professur Marketing & Verkaufsmanagement · Agentic AI for Lead Generation · github.com/tobias-weiss-ai-xr/marketing-research'
style: |
  /* JLU Gießen look: white background, JLU blue #165A97 */
  :root { --jlu-blue: #165A97; --jlu-light: #e8eff6; --jlu-green: #E5F0CF; --ink: #212529; --muted: #6c757d; }
  section {
    background-color: #ffffff;
    color: var(--ink);
    font-family: Verdana, 'Segoe UI', Helvetica, Arial, sans-serif;
    padding: 96px 64px 72px;
    border-top: 10px solid var(--jlu-blue);
  }
  section header { position: absolute; top: 18px; left: 64px; right: auto; }
  section header img { display: block; }
  section footer { color: var(--muted); font-size: 15px; left: 64px; right: 120px; }
  section::after { color: var(--jlu-blue); font-weight: 700; font-size: 18px; right: 64px; }
  section.smaller table { font-size: 18px; }
  section.smaller table th, section.smaller table td { padding: 4px 8px; }
  h1, h2, h3 { color: var(--jlu-blue); font-weight: 700; }
  h2 { border-bottom: 3px solid var(--jlu-green); padding-bottom: 6px; }
  strong { color: var(--jlu-blue); }
  table { margin: 0 auto; font-size: 20px; border-collapse: collapse; }
  table th, table td {
    background-color: #ffffff; padding: 5px 10px;
    border: 1px solid #dee2e6; color: var(--ink);
  }
  table thead th { background-color: var(--jlu-blue); color: #ffffff; border: 1px solid var(--jlu-blue); }
  table tbody tr:nth-child(even) td { background-color: #f4f7fa; }
  pre {
    background: #f8f9fa; border: 1px solid #dee2e6; border-left: 4px solid var(--jlu-blue);
    border-radius: 4px; color: var(--ink); font-size: 18px; padding: 12px;
  }
  code { background: #f1f3f5; color: var(--ink); }
  blockquote {
    background: var(--jlu-light); border-left: 5px solid var(--jlu-blue); color: var(--ink);
    font-style: normal; font-size: 22px; margin: 16px 0; padding: 6px 18px;
  }
  a { color: var(--jlu-blue); }
  ul { font-size: 24px; }
  li { margin: 6px 0; }
  li::marker { color: var(--jlu-blue); }
  section.lead { justify-content: center; border-top-width: 10px; }
  section.lead h1 { font-size: 54px; }
  section.lead h2 { border-bottom: none; color: var(--ink); font-weight: 400; }
---

<!-- _class: lead -->

# Agentic AI for Lead Generation

## Partner companies for the chair

Tobias Weiß · Guest Lecture · Professur Marketing & Verkaufsmanagement

Thursday, 22 October 2026 · 15:15–16:00
within "Advanced Issues in Marketing and Sales" (Prof. Haas)

45 minutes · BWL Master students · WS 2026/27 edition

![w:780](img/hero-agentic-leadgen.svg)

<!-- notes:
⏱ ~45 s · READ ALOUD

Good afternoon — thank you for having me. This session is about
agentic AI: what it is, and how to run it so its work is
trustworthy. Everything today maps onto one real task — helping
this chair find and qualify B2B partner companies. The shortlist
the agent produces is evidence for our Bachelor course Sales
Strategy and Execution next summer. Nothing here is an exercise.
It is the start of a deliverable. Let's begin.
-->

---

## Why this session exists

- The chair partners with companies: funding, data, cases
- Finding + qualifying partners is manual, slow, unscalable
- Agentic AI can research, score and rank prospects
- **Demo output = evidence for "Sales Strategy and Execution" (SS 2027)**

> Nobody wins from another lecture about chatbots.

<!-- notes:
⏱ ~45 s · READ ALOUD

[If preceding talker, bridge first:] You just heard about modern
marketing and sales in a digital world — agentic AI is the tooling
that puts exactly that into practice.

The chair partners with companies — for funding, for data, for
teaching cases. Finding and qualifying those partners is manual
work: slow, and it doesn't scale. Agentic AI can research
companies, score them, and rank them. And be clear: nobody needs
another lecture about chatbots. What you need is to recognise —
and judge — an agentic workflow, and to read the contract that
drives it. The demo produces a ranked list of partners, every claim
with a source. That list is the dataset the Bachelor course builds
on next year.
[jot: the "ranked list" is the handoff artefact — the
"output as input" promise. Protect it; it returns on slides 20/21.]
-->

---

## What you will be able to do

| By the end… | You can… |
|---|---|
| **Understand** | Explain what "agentic" means, and why it is not a chatbot |
| **Operate** | Read how a harness (pi) gives an AI tools, rules and a task |
| **Assess** | Judge an agentic output: checked? citable? repeatable? |
| **Apply** | Run the exercise yourself: ingest + rate leads for the chair (repo → rubric → validator) |
| **Context** | Say which context an agent can't know — and why that keeps you in charge |

> Model = brain. Harness = hands. Workflow = muscles. **Context = memory — the part only you can supply.**

<!-- notes:
⏱ ~30 s · READ ALOUD

Here's the promise of the next forty-five minutes, in four rows.
You'll be able to explain what agentic means — and why it is not
a clever chatbot. You'll be able to read how a harness gives an AI
tools, rules, and a task. You'll be able to judge an agentic output
— checked? citable? repeatable? And you'll run the loop yourself: repo, rubric, validator —
you'll ingest and rate leads for the chair before the course ends. One headline before we
start: model is the brain, harness is the hands, workflow is the
muscles — and context is the memory. That part is yours.
[Not read — colour:] Row 5 is the thread of the whole talk:
intelligence is distributed — generation (model), execution
(harness), context (you).
-->

---

<!-- _class: smaller -->

## Roadmap — 35 min + 10 min Q&A

| Block | Content | Time |
|---|---|---|
| 1 · Foundations | agentic ≠ chat · model · harness · loop · providers · corpus & rate limits · git & the repo | ~11 min |
| 2 · Method | contracts · the lead-gen loop · rating formulas · evidence | ~8 min |
| 3 · Walkthrough | live demo: repo → agent → validator | ~13 min |
| 4 · Reflection | take-aways · resources | ~4 min |
| 5 · Q&A | your questions · discussion | 10 min |

> The walkthrough is the heart — theory is fuel for it. **10 minutes are reserved for your questions.**

<!-- notes:
⏱ ~15 s · READ ALOUD

The map for the next thirty-five minutes: foundations first, then
the method, then the live walkthrough — the heart — and a short
reflection at the end. Ten minutes are reserved for your questions.
If one comes to you mid-talk, write it down — we'll get to it.
[Not read:] The notes sum to ~38 min — slightly over the 35 budget.
The flex is Step 2: its ~8 min estimate is padded; in the T1 run the
agent finished well inside it. If running behind: trim Define-the-
hunt (45 s), compress Providers and the corpus slide to the HRZ line, skip the DNS aside
unless it bites. Q&A is fixed at 10 min — bank questions with
"hold that for Q&A". The BrowserMCP intermezzo inside Step 2 (~45 s:
why a real browser — LinkedIn, consent walls, logins) folds into
the walkthrough buffer.
-->

---

## Agentic ≠ chat

![w:1200](img/chat-vs-agent.svg)

> "Agentic" is a working environment — not a better chat.

<!-- notes:
⏱ ~2.5 min · READ ALOUD

Let's clear up the most common confusion first. On the left: chat.
Question in, answer out. No tools, no files, no actions — a
conversation. On the right: an agent — a goal, a plan, tools,
verification, running inside a harness that grants it access to the
world: a browser, files, APIs. The amber loop in the middle is
where the work happens. The key point: agentic is not a smarter
ChatGPT. It is a difference in kind, not in size. The model can
touch the world, and it can check its own work. Keep this image —
it's the whole lecture in one picture.
-->

---

## The parts: model · harness · loop

![h:270](img/model-harness-loop.svg)

**Harnesses (2026):** pi, OpenCode, Claude Code — same model, different results. The harness decides.

<!-- notes:
⏱ ~2.5 min · READ ALOUD

Three parts. The model — the brain. The harness — the piece this
lecture adds: an executable environment, permissions, memory — the
hands and the workspace. And the loop — what makes it agentic: it
plans, acts, checks, corrects itself. Two asides. First: a fourth
ingredient is deliberately not on this diagram — context, the
criteria and judgement the loop cannot invent for itself. That's
yours, and it comes back in two slides. Second: pi is the harness
you see in the demo. I use it mainly for its small memory footprint.
OpenCode and Claude Code are solid alternatives. Same model,
different results — the harness decides.
[Not read:] If asked why pi — small memory footprint; OpenCode and
Claude Code are solid alternatives.
-->

---

<!-- _class: smaller -->

## Key AI providers — what you can use as a student

| Provider / offer | What you get | Where |
|---|---|---|
| **JLU HRZ API-Service** ⭐ | Free LLMs for JLU members: local Qwen (256K–1M ctx) + commercial | [uni-giessen.de → HRZ → KI](https://www.uni-giessen.de/de/fbz/svc/hrz/svc/services/ki/api-service) · **ki@uni-giessen.de** |
| **OpenCode Zen — free models** | **Big Pickle** (stealth) · **Beam Free** (Reflection 501B, 1M ctx, no training) | [opencode.ai/zen](https://opencode.ai/zen) — `/models` |
| **Google AI student plan** | 1 year Google AI **Plus** free · Gemini, 400 GB | [one.google.com/ai-student](https://one.google.com/ai-student?g1_landing_page=75) |
| **OpenRouter** | one key → many models (OpenAI, Anthropic, Google, open) | [openrouter.ai](https://openrouter.ai) |
| **Harnesses** | today's demo tools — **OpenCode**, pi | [opencode.ai](https://opencode.ai) · [pi.dev](https://pi.dev) |
| **Local models (Ollama)** | free, on your laptop, no account, private | [ollama.com](https://ollama.com) |

> ⚠️ **Privacy:** Big Pickle's provider **may train on your input**; Beam Free and HRZ local models **do not**. **Never paste private, customer, or unpublished data into a model that trains on user input** — for sensitive work use HRZ or Ollama. · Start with **HRZ API**.

<!-- notes:
⏱ ~1.25 min · READ ALOUD

What can you use as a student, starting tomorrow? Best option
first: the JLU HRZ API-Service. Free LLMs for every university
member — locally hosted Qwen models with up to a million tokens of
context, plus commercial models. Access by emailing
ki@uni-giessen.de; works with OpenCode out of the box. Second,
OpenCode Zen lists free models — Big Pickle (a stealth model, free
for now) and Beam Free (Reflection's open-weight 501-billion model,
also free, with a one-million-token context). One privacy caveat:
Big Pickle's provider may train on your input; Beam Free and the
HRZ local models do not. So never paste private, customer, or
unpublished research data into a model that trains on user input —
for sensitive work, use HRZ or run Ollama on your own laptop.
Google gives students a year of Google AI Plus free — verify with
your university email by the end of December. OpenRouter: one key,
many models, free tiers included. And the harnesses — OpenCode and
pi — are the tools behind today's live demo. If you take one thing
from this slide: start with HRZ.
One practical note on the network: if the campus Wi-Fi cannot
resolve opencode.ai, the fix — a public resolver or a hosts entry —
is in the HRZ one-pager. Thirty seconds of setup, then move on.
[Not read — DNS fix if opencode.ai does not resolve (hall Wi-Fi):]
Diagnose: `nslookup opencode.ai` fails while other pages load.
Fix A — resolver: set DNS on the Wi-Fi adapter to 1.1.1.1 +
8.8.8.8 (Windows: adapter → IPv4 → DNS; macOS: Network → Details →
DNS; Linux: NetworkManager → IPv4 → DNS); reconnect, retry.
Fix B — hosts entry (admin): resolve fresh via
`dig +short opencode.ai @1.1.1.1`, then append `<IP> opencode.ai`
to /etc/hosts (Linux/macOS) or C:\Windows\System32\drivers\etc\hosts
(Windows). Verified 19 Oct 2026: 172.65.90.20 (Cloudflare anycast,
.20–.23 all work) — re-verify at prep time, IPs can change.
Still failing → it is the firewall, not DNS → phone hotspot for
the demo machine; do not fight a deliberate campus block.
[Not read — for questions:] Google deal redeem by Dec 31 2026,
SheerID verification; OpenCode via LiteLLM provider block
(baseURL api.hrz.uni-giessen.de) or Claude Code via
ANTHROPIC_BASE_URL.
-->

---

<!-- _class: smaller -->

## The corpus and the rate limits — know your scale, know your ceiling

The agent searches a corpus of **>14,000 marketing papers** (title, authors, abstract, venue, URL for each) and calls the model in a loop — a lead-gen pass is dozens of calls. So the rate limit matters.

| Provider | Limit | Notes |
|---|---|---|
| **HRZ API-Service** ⭐ | free for JLU · no published cap | local Qwen, 256K–1M ctx |
| **OpenCode Zen** (free models) | ~15–20 req/min | silent 429 · models are temporary |
| **Google AI student plan** | ~90 prompts/day (Gemini 3 Flash) | AI Plus 2× standard · refreshes every 5h |
| **OpenRouter** | free tier limited | pay-as-you-go lifts the cap |
| **Ollama** (local) | no API limit | bounded by your hardware (VRAM, tokens/sec) |

> Free tiers are fine for learning. For a real run, start with **HRZ** — free, local, no training on your data.

<!-- notes:
⏱ ~1 min · READ ALOUD

Two things to know about your tools. First, the corpus: the agent
searches more than fourteen thousand marketing papers — title,
authors, abstract, venue, URL for each. A single lead-generation
pass is dozens of model calls, so the rate limit matters. Second,
the limits. HRZ is free for JLU members with no published cap —
start there. OpenCode Zen's free models run about fifteen to
twenty requests per minute, and the four-twenty-nine is silent —
no retry-after header, so the agent just waits and retries.
Google's student plan gives you roughly ninety prompts a day with
Gemini 3 Flash on the AI Plus tier, refreshing every five hours.
OpenRouter's free tier is limited; pay-as-you-go lifts the cap.
And Ollama running locally has no API limit — you are bounded by
your own hardware. For learning, any free tier is fine. For a real
run, start with HRZ.
[Not read — honesty note if probed:] Corpus numbers are lower
bounds (>14,000, >150 commits since Aug 2026, >90 last month);
exact snapshot 2 Nov 2026 in the workspace slide. Rate limits
verified 21 Oct 2026: OpenCode Zen ~15–20 RPM (GitHub
lidge-jun/opencodex#1145, freetokens.fyi); Google AI Plus ~90
prompts/day Gemini 3 Flash (9to5Google, Jan 2026); HRZ has no
published rate limit on the model hub page
(api.hrz.uni-giessen.de/ui/model_hub_table). Ollama is local —
bounded by VRAM and tokens/sec.
-->

---

<!-- _class: smaller -->

![bg right:22% fit](img/qr-repo.png)

## The workspace: git and the repo itself

**git** = a lab notebook that never forgets

| This repo — `marketing-research`, public | The numbers |
|---|---|
| The **corpus**: >14,000 papers in one `papers.yaml` — title · authors · abstract · venue · URL | **>150 commits** since Aug 2026 · 1 researcher + AI agents · >90 last month |
| The **machinery**: taxonomy · discovery scripts · **executable validators** | generated files are **never hand-edited** |
| **Your exercise**: `leads/` — same rules, same history | every lead a commit · every claim a URL |

<p style="text-align:center;margin:6px 0 0;font-size:15px;"><code>github.com/tobias-weiss-ai-xr/marketing-research</code></p>

> If it isn't in the repo, it didn't happen. If it is, you can check it — line by line, back to day one.

<!-- notes:
⏱ ~2 min · READ ALOUD

Before we go further: the workspace. Git is a lab notebook that
never forgets. Every change is a commit — who changed what, when,
down to the line. GitHub is the public copy; anyone can audit it —
including you. This lecture lives in one: the chair's
marketing-research repository. Inside: the corpus — more than
fourteen thousand marketing papers in a single file, over three
hundred thousand lines, each with title, authors, abstract, venue,
and a link. The history: more than one hundred fifty commits since
August — one researcher and the AI agents beside them, every commit
attributed — more than ninety in the last month alone. One rule
makes it trustworthy: generated files are never hand-edited, and a
validator runs before anything is committed. Your exercise lives in
the same repo, in the leads folder — same rules, same history. The
QR code on the right goes straight to the repository — scan it now
or after the session. One sentence to keep: if it isn't in the
repo, it didn't happen. If it is, you can check it.
[Not read:] BWL students may never have used git — the lab-notebook
framing is the point; hands-on comes in the leads exercise
(fork, commit, pull request). Numbers are thresholds, not snapshots:
on 2 Nov 2026 the true counts were 211 commits / 1,512 in the last
month / 15,769 papers / 356,729 lines. ">X" stays true as counts
grow; only the rolling "last month" figure can decay. If probed,
re-read exact counts from `git rev-list` and `wc -l papers.yaml`.
-->

---

<!-- _class: smaller -->

## Why now — the evidence inside the research corpus

The chair's open corpus, public on GitHub: **>14,000 marketing papers — >8,700 published in 2026 alone**

| Signal | Count |
|---|---|
| Papers mentioning **agentic AI** | >100 — >90 of them from 2026 |
| Papers on **lead generation** | >30 |
| **Both** — strict (agentic × lead-gen) | **≥ 2** |
| **Both** — broader (agent-aware × lead-ops) | **≥ 5** |
| Papers on **context-aware** marketing | >20 |

> Two rounds of OpenAlex ingestion took the strict intersection from **1** to **≥ 2**, the broader set from **3** to **≥ 5**. The field just opened — claim the gap while it's a gap.

<!-- notes:
⏱ ~1.5 min · READ ALOUD

Why now? The evidence — from this chair's own open corpus, public
on GitHub. More than fourteen thousand marketing papers — more
than eight thousand seven hundred published in 2026 alone. More
than a hundred papers mention agentic AI — more than ninety of
them from this year. More than thirty are about lead generation.
Now the intersection — papers that do both? Until a few weeks
ago: zero. Two rounds of targeted ingestion later, the strict
intersection is at least two — the Journal of Business Research,
then a second. Count the agent-aware field more broadly and it is
at least five. The field just opened, and the first position in it
is still free.
[Not read — honesty note if probed:] Slide shows lower bounds so
they stay true as the corpus grows. Exact snapshot 2 Nov 2026,
keyword search over title/abstract of our own corpus
(docs/papers.json, 15,769 papers, regenerated today): agentic 180
(168 in 2026), lead-gen 46, strict intersection 2, broader 6,
context-aware 26. Definitions: strict = substring 'agentic' AND
'lead generation'; broader = (agentic | ai agents | ai agent |
multi-agent | autonomous agents) AND (lead generation | lead
scoring | lead qualification | prospecting). Strict 2: the JBR
paper 'AI agents, agentic AI, and the future of sales' (2026) and
'The Augmented Rep' (IRJAEM, 2026). Broader adds GTM-Bench,
Governing Machines (SSRN), The Transformative Role of AI Agents in
Marketing (TechRxiv), Calibrating Professional Discretion in
AI-Supported B2B Selling (RaFT, 2026-09). Context-aware = 'context-aware' or
'contextual intelligence'. Corpus grew 15,495 → 15,769 this round
(+274 net: arXiv/DOI batch junk-screened, 52 off-topic entries removed —
hard sciences, medicine, SEO spam, hardware, datasets — 77 arXiv URLs
normalized). All URLs resolve; all DOIs verified;
lower-evidence candidates excluded rather than inflating the count;
validation passes.
-->

---

## How to talk to the machine: prompts vs contracts

![h:360](img/contract-vs-prompt.svg)

> Prompt = asks a chat · Contract = runs an agent · **Context = what the machine can't know**

<!-- notes:
⏱ ~2 min · READ ALOUD

This is the central mental model of the lecture. A prompt is how
you ask a chat: a question, in one go. A contract is how you run an
agent: it lives in the repository, it's versioned, it says what
'done' means. And the third piece: context. The contract is a
container for context — the chair's criteria, the sources we trust,
our judgement, the history of partnerships. Without it, the agent
is a brilliant generalist with no idea what 'good' means here. A
prompt turns an idea-generator into a conversation. A contract
turns it into a reproducible research pipeline. And in this
project the contract is not a document the agent might ignore — it
is the repository itself: schema, rubric, executable validator.
You'll see it in action in the walkthrough.
-->

---

## A lead-generation loop as an agentic workflow

![w:1200](img/leadgen-pipeline.svg)

> Six steps — the agent executes 2–5, you own definition and evaluation. **Those two boxes are where context lives.**

<!-- notes:
⏱ ~3 min · READ ALOUD

Let's make it concrete — a lead-generation loop as an agentic
workflow. Read it left to right. [point to each box as you say it]
DEFINE — you: the blue box. What does a good partner look like for
this chair? SOURCE — where do we hunt? QUALIFY — does this company
fit? RECORD — capture every claim with its source. VERIFY — check
those sources say what we think they say. OUTPUT — a ranked list,
judged by a human. The agent runs the middle four steps. You own
the first and the last — and you know why from the slide before:
those two boxes are where the context lives. The amber line along
the bottom: what you learn on a run feeds back to tighten the
contract for the next run. The agent stays inside the loop. The
human stays in charge.
[Not read:] DEFINE injects context (criteria, sector, guard rails);
EVALUATE judges with context (the three questions). Next slide makes
DEFINE concrete — the sector choice, still human work.
-->

---

<!-- _class: smaller -->

## Define the hunt: scoring the sector

Lead generation starts with a **human** decision: *which sector do we hunt?*

| Criterion (1–5) | Mech. & plant engineering | Optics / photonics | Grocery retail |
|---|---|---|---|
| Chair research fit — sales management | 5 | 5 | 2 |
| Course fit — "Sales Strategy and Execution" | 5 | 5 | 2 |
| Regional employers (Mittelhessen) | 5 | 5 | 3 |
| Lead-gen relevance — B2B, long cycles | 5 | 4 | 2 |
| Demo data availability | 4 | 4 | 5 |
| **Total** | **24** | **23** | **14** |

> Hard guard: sector is out if chair fit < 4 **or** lead-gen relevance < 4 — grocery retail (our first default) fails. **Decision: German mechanical & plant engineering.**

<!-- notes:
⏱ ~45 s · READ ALOUD

Before the agent does anything, a human decides where to hunt.
Look at the table: five criteria, scored one to five, plus one hard
guard. Our first default — grocery retail — fails the guard: lead
generation there is a consumer, demand-gen game, not a
sales-strategy one. Optics came close. Mechanical and plant
engineering wins on every axis. That's the sector you'll see in the
demo. And notice what just happened: the AI did not choose the
sector. We did. Choosing target segments is a core sales-strategy
decision — one we can teach in the Bachelor course.
[Not read:] This is the DEFINE box made concrete; guards the claim
the walkthrough is human-steered, not agent-chosen.
-->

---

<!-- _class: smaller -->

## Rate a lead: pick a formula — before the agent runs

| Formula | Rule | Trade-off |
|---|---|---|
| Weighted sum | `L = Σ wᵢ·sᵢ` · w: fit .35 · region .25 · size .15 · evidence .15 · timing .10 | transparent · **compensatory**: a 5 on fit can hide a 0 on evidence |
| Geometric mean | `L = Π sᵢ^wᵢ` | **non-compensatory**: one zero sinks the lead · harsh to defend |
| **Gated weighted sum** ✓ | gates first — B2B · region reachable · ≥ 1 verified source — then weighted sum | matches the chair's decision · thresholds = judgement calls |

Example (each criterion 0–5): fit 5 · region 3 · size 4 · evidence 4 · timing 2 → `L = 3.90`

> Weights live in the repo (`leads/leads.yaml`, `rubric:`) — **published context, not vibes**. Change them — in a PR, with reasons.

<!-- notes:
⏱ ~2 min · READ ALOUD

Before the agent scores anything, we decide how scoring works.
Five criteria, each nought to five: fit — chair research fit;
region — Mittelhessen reachability; size — at least a thousand
employees; evidence — independent sources; timing — live signals
like expansion or sales hiring. Three candidate formulas. The
weighted sum: transparent — but compensatory. A five on fit can
hide a zero on evidence. The geometric mean: one zero sinks the
whole lead — harsh, and hard to explain to a dean. Our choice:
gates first — B2B, region reachable, at least one verified source
— then the weighted sum on the survivors. Exactly like the sector
guard two slides ago. Worked example: three point nine. And the
weights are not vibes — they are published in the repository, in
the same file you will edit. Disagree? Change them — in a pull
request, with reasons. That is what published context means.
-->

---

## Now: a live walkthrough

Task: ingest **2 leads** into the chair's repo — `leads/leads.yaml` — with:

- scores per criterion + the weighted sum, gates applied, ranked
- named source URL per claim (citable, verifiable)
- `python3 leads/validate_leads.py` passing before anything counts

I run this live in a harness — in the same repo you will work in.
No fallback video: this exact exercise was **tested agentically**, end to end.

<!-- notes:
⏱ ~30 s · READ ALOUD

The live walkthrough. Task: ingest two leads into the chair's
repository — the same file, schema and validator you will use
yourself. Every claim with a source URL, scores per criterion,
gates first, then the weighted sum. And no fallback video: if
something breaks, I fix it live — that is the loop working. The
approach is trustworthy because it was tested agentically
beforehand — same task, same prompt, several timed runs. Let's go.
-->

---

<!-- _class: smaller -->

## Walkthrough · Step 1 — The repo is the contract

```text
marketing-research/               github.com/tobias-weiss-ai-xr/marketing-research
├─ papers.yaml                    >15,000 papers — single source of truth
├─ config/taxonomy.yaml           categories + discovery queries
├─ scripts/validate_papers.py     the contract, executable
├─ leads/leads.yaml              your starting point: schema + rubric
├─ leads/validate_leads.py       same pattern: validate before commit
└─ README.md · statistics.json    auto-generated — never hand-edited
```

> No prose rules file the agent can ignore: **structure + validators + one source of truth.**

<!-- notes:
⏱ ~2 min · READ ALOUD

Step one: the contract. Earlier I said contracts beat prompts —
here is what that means in practice. It is not a document the agent
reads at start and may ignore. It is the repository itself. One
source of truth: papers.yaml, fourteen thousand and sixty-seven
papers. Everything downstream is generated, never hand-edited.
Every change passes an executable validator before it is committed.
And your exercise lives in the same pattern: leads/leads.yaml —
schema, rubric, weights — and its own validator. Done does not mean
"looks finished". Done means the validator passes. One
critical-literacy point before we go on: every source in this repo
is self-reported by companies. A URL proves a claim exists; it does
not prove the claim is true. So the standing question today: whose
evidence is this?
[Not read:] The earlier approach — an AGENTS.md rules file — kept
getting ignored and drifting; structure plus executable validation
is what survived contact with real runs.
-->

---

<!-- _class: smaller -->

## Walkthrough · Step 2 — The agent at work

Watch the six-step loop run live:

- **only watch** — no magic, every tick is visible in the terminal
- agent reads the **repo** (schema + rubric), then **opens the browser** (MCP) — real company pages
- **why a browser:** LinkedIn, consent walls, logged-in portals block plain HTTP — the good context sits behind them
- writes leads into `leads/leads.yaml` → runs the **validator** → fixes what fails
- **iterates**: pause, correct, re-check — that is the loop

> Nothing happens off-screen — the loop is fully visible.

<!-- notes:
⏱ ~8 min live action — spoken play-by-play, in this order:

[agent starts] "I'm introducing the agent the way I'd introduce a
new colleague: here's the repo — schema, rubric, validator.
Here's the task. Show me your plan first."

[it plans] "Watch the plan — it maps one-to-one onto the six boxes
from the pipeline slide."

[it opens the browser] "There it is — it can touch the world; that's
what agentic means. It's reading the companies' own pages. Right
now it is absorbing our context — the criteria it could not invent
for itself."

[same beat — THE INTERMEZZO, pause & explain:] "Why a real browser
and not just an API call? Because the richest lead sources are
protected. LinkedIn hides contacts behind a login. Half the
companies gate their site behind a cookie banner or an anti-bot
wall, and vendor pages sit in logged-in portals. A plain HTTP
request or a search API gets a '403' — or a consent wall it can't
click through. So the agent drives a real browser — log in, accept
the consent, scroll the page — a tool purpose-built for exactly the
sites where the good context lives. That's the MCP part: a browser
as one more tool the model can pick up."

[quick show — one protected page it just logged into:] "Watch it
open that profile. It didn't scrape a summary; it read the real
page — the context behind the wall is what we're after."
[Not read — honesty if probed:] The agent is rate-limited and
touches only public or already-authenticated pages; we never paste
private or customer data. If the wall blocks it, we name it and
move on — a fixed failure is the lesson.

[it scores] "It scores each lead against the rubric — fit signal,
one sentence, source alongside."

[on a mistake — pause, then:] "Hold on. It over-claimed. Stop.
Which URL says that?" [let it correct itself] "That
pause-and-correct is the loop in action."

[it runs the validator] "It re-checks its own citations and the
score math — the validator checks both. That's step five: verify."

[final table] "There's the shortlist — ranked, cited, validated.
Let's judge it with the three questions."
[Not read:] Steps: (1) open browser via MCP, search prospects;
(2) read real pages, extract fit signals; (3) score vs rubric;
(4) write leads/leads.yaml entries with URLs; (5) run
validate_leads.py, fix failures; (6) ranked table. Speed beats
completeness — cut lead two if running long. Demo runs on real
public data via cloud API — never paste private/customer data.
Tested beforehand: ≥2 timed agentic runs of this exact exercise
(demo/test-protocol.md). If it breaks live: debug on screen and
name it — a fixed failure is the lesson. No recording, no
fallback video.
-->

---

## Walkthrough · Step 3 — The three questions

1. **Checked?** Did the agent verify its output, not just generate it?
2. **Citable?** Does every claim have a URL that resolves — and actually supports it?
3. **Repeatable?** Same repo, same rubric, same validator → a result you can re-run and audit?

*The 1–5 scores are a transparent heuristic — each criterion with evidence — not a measurement.*

> All three guard one thing: **context** — invented context (Checked) · untraceable context (Citable) · lost context (Repeatable).

> The final slide of the walkthrough: apply them to the live result.

<!-- notes:
⏱ ~2 min · READ ALOUD

The last step of the walkthrough: judge the output with three
questions. Checked — did the agent verify its output, or just
generate it? Citable — does every claim carry a URL that resolves
and supports the sentence? Repeatable — re-run the same repo, the
same rubric, the same validator: a result you can audit. All three
guard context.
Checked guards against invented context. Citable guards against
untraceable context. Repeatable guards against lost context. If the
output passes, it's a deliverable. If not, it's a draft. Same
discipline as verifying a prospect's claims before you sign.
Verify before you trust.
[Not read:] Repeatability is process-level, not byte-identical
output — models are stochastic, the method is re-runnable. Sales
connection: you verify a prospect's claims before signing.
-->

---

<!-- _class: smaller -->

## Your turn: clone the repo, ingest 2 leads

```bash
# Fork on GitHub, then clone your fork:
git clone https://github.com/YOUR-USERNAME/marketing-research.git
cd marketing-research
# … edit leads/leads.yaml, then validate …
python3 leads/validate_leads.py
git add leads/leads.yaml
git commit -m "Add 2 leads: CompanyA, CompanyB"
git push   # → open a pull request on GitHub
```

1. **Fork & clone** — the commands above (repo is public)
2. **Ingest 2 leads** — real B2B companies, every claim with a URL
3. **Score & rank** — gates first, then the published formula
4. **Validate & push** — validator passes → `git push` → pull request

> Best submissions join the chair's real shortlist — "Sales Strategy and Execution", SS 2027.

<!-- notes:
⏱ ~1.5 min · READ ALOUD

Now it's your turn. The repo is public — fork it on GitHub, clone
your fork, cd in. The commands are on the slide. The brief, the
schema, the rubric, the validator: all there. Your task: in your
own clone, ingest two leads — real companies that could partner
with this chair. Score them with the published formula: gates
first, then the weighted sum. Run the validator; if it passes,
add, commit, push, and open a pull request. The chair reviews
submissions like papers. And the best ones join the real shortlist
for the Bachelor course next summer. Everything you saw today,
you now run yourself.
[Not read:] YOUR-USERNAME is the student's GitHub fork; the
upstream repo is github.com/tobias-weiss-ai-xr/marketing-research.
Fork button is top-right on GitHub. After forking, the clone URL
has the student's own username. The commit message is a pattern —
replace CompanyA, CompanyB with the real company names.
-->

---

## What the chair gets out of it

- A reproducible partner-sourcing method (not a one-off search)
- A ranked, sourced shortlist — fed by the course's best submissions
- Students who can run agentic workflows (a real skill for the CV)
- Evidence base for the **Bachelor course "Sales Strategy and Execution"** (SS 2027)

> The lecture is not the output. The shortlist is.

<!-- notes:
⏱ ~1.5 min · READ ALOUD

What does the chair get out of this? Four things. A reproducible
partner-sourcing method — not a one-off search. A ranked, sourced
shortlist — and it grows with every student submission. Students who can run agentic
workflows — a real CV skill; that's what companies hire for now.
And an evidence base for the Bachelor course Sales Strategy and
Execution next summer. One note: everything here is open and
reusable — you can take this method into internships and theses.
The lecture is not the output. The shortlist is.
-->

---

## Take-aways

1. Agentic = working environment, not a chatbot
2. Harness = model + tools + rules = accountable AI work
3. The repo is the contract: schema, rubric, validator — "done" is executable
4. Verify, cite, repeat — the three questions
5. **Context beats compute — the right context contract beats a bigger model**

> Next summer semester, the chair decides what this feeds: the Bachelor course "Sales Strategy and Execution".

<!-- notes:
⏱ ~1 min · READ ALOUD

Five lines to take home. Agentic is a working environment, not a
chatbot. A harness is a model plus tools plus rules — that's what
makes AI work accountable. The repo is the contract — schema,
rubric, validator. Done is not 'looks finished'; done is the
validator passing. Verify, cite, repeat — the three questions. And the one
to remember: context beats compute. A small model with your
context beats a big model with none. Next summer, this shortlist
becomes the Bachelor course's input — the chair decides what it
feeds.
[Not read:] Take-away 5 is the portable one-liner; it reframes the
lecture beyond today's demo.
-->

---

## Resources

- **JLU HRZ API-Service** (free LLMs for JLU members) — [uni-giessen.de → HRZ → KI → API-Service](https://www.uni-giessen.de/de/fbz/svc/hrz/svc/services/ki/api-service) · [model overview](https://api.hrz.uni-giessen.de/ui/model_hub_table/)
- **HRZ access one-pager** (student quick start, 1 page) — [`hrz-access-one-pager.md`](hrz-access-one-pager.md)
- **pi** — [pi.dev](https://pi.dev) · docs: [pi.dev/docs](https://pi.dev/docs) · **OpenCode** — [opencode.ai](https://opencode.ai) · **OpenRouter** (one key, many models) — [openrouter.ai](https://openrouter.ai)
- **Google AI student plan** — [one.google.com/ai-student](https://one.google.com/ai-student?g1_landing_page=75) (1 year free for students)
- **marketing-research** (chair corpus, public) — [github.com/tobias-weiss-ai-xr/marketing-research](https://github.com/tobias-weiss-ai-xr/marketing-research) → start at **`leads/`** (exercise brief · rubric · validator)
- **skeleton-research** (forkable corpus skeleton) — [github.com/tobias-weiss-ai-xr/skeleton-research](https://github.com/tobias-weiss-ai-xr/skeleton-research)
- **This deck** — [`lecture/`](.) in this corpus repo (English, 45 min)

<!-- notes:
⏱ ~30 s · OPTIONAL read — the list stays up on screen either way.

"Everything on this slide is public and reusable — the links are in
the deck. Two are worth starting with: the HRZ API-Service, and the
research corpus that today's evidence came from. Fork it — it's a
skeleton you can grow into your own corpus."

[If you only say one sentence:] "All links are in the deck — the
corpus and the one-pager are where I'd start."
[Not read:] Lead with HRZ API-Service (free, university-provided).
Google link repeats the providers slide so it survives sharing.
marketing-research = evidence base of the "why now" slides;
skeleton-research = forkable starter for a student's own curated
corpus; hrz-access-one-pager.md = student quick start.
-->

---

<!-- _class: lead -->

# Thank you!

## Questions?

Tobias Weiß · guest lecture · Professur Marketing & Verkaufsmanagement

Agentic AI for Lead Generation · 22 Oct 2026 · 45 min

<!-- notes:
⏱ 10 min Q&A — closing words first, then moderation.

[Closing, ~15 s · READ ALOUD:] "Thank you for listening — and for
the questions you've banked. Let's hear them, one at a time."

[Each answer — keep it short, one idea, then ask the next person.]
Prepared answers you're likely to reach for:

- Model choice — the demo runs on **big pickle**; the harness is
  model-agnostic — pi switches model with Ctrl+L. Cost is why we
  pick cheap models with tight contracts, not size.
- "Is this just a fancy search engine?" — search returns matches;
  this returns judgements, because the contract carries the chair's
  context and every judgement is source-traceable. Context is the
difference — and it's yours, not the model's.
- "Is the output reproducible?" — same contract, same method:
  auditable, re-runnable; never promised byte-identical, models are
  stochastic.
- Data privacy — local models (Ollama, HRZ Qwen) if it matters;
  today's demo is public data only.
- "What is git?" — version control: every change is a commit with
  author, timestamp, exact diff; the repo's history is public — that
  is what makes the work auditable.
- "What does qualified mean?" — defined in the rubric
  (`leads/leads.yaml`): fit, region, size, evidence, timing, each
  0–5; gates first, then the published weighted sum.
- "What if the demo breaks?" — we debug it live; the approach was
  tested agentically beforehand (timed runs of the exact exercise).
- Trying it themselves — resources slide; start with HRZ API and the
  `leads/` folder in the repo.

[Hard stop at 16:00 — the course's Übung starts in this room right
after; the ten minutes belong to the students, never overrun.]
-->
