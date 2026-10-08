# Agentic AI for Lead Generation — Guest Lecture (45 min, EN)

English guest lecture for **BWL Master students** in the marketing seminar:
how **agentic AI** finds, qualifies and ranks partner companies for the chair —
delivered as a **live walkthrough** in an AI harness. The ranked partner
shortlist produced in the demo becomes the **input dataset for the Bachelor
seminar**.

## Files

| File | What |
|---|---|
| [`agentic-ai-for-lead-generation.md`](agentic-ai-for-lead-generation.md) | Deck source (Marp, 19 slides, JLU design: white background, JLU blue, speaker notes with timing) |
| [`agentic-ai-for-lead-generation.html`](agentic-ai-for-lead-generation.html) | Rendered deck (open in browser) |
| [`agentic-ai-for-lead-generation.pdf`](agentic-ai-for-lead-generation.pdf) | PDF for sharing / printing |
| [`agentic-ai-for-lead-generation.pptx`](agentic-ai-for-lead-generation.pptx) | PowerPoint export |
| [`img/`](img/) | Custom SVG diagrams (light, JLU colours) + JLU logo used by the slides |
| [`demo/`](demo/) | Demo kit for the live walkthrough: `AGENTS.md` contract, kickoff prompt + narration (`demo-script.md`), `shortlist-template.md` target format |

## Structure (35 min + 10 min Q&A)

| Block | Content | Time |
|---|---|---|
| 1 · Foundations | agentic ≠ chat · model · harness · loop | ~10 min |
| 2 · Method | contracts · the lead-gen loop · corpus evidence | ~7 min |
| 3 · Walkthrough | live demo: contract → agent at work → the three questions | ~13 min |
| 4 · Reflection | AI providers for students · take-aways · resources | ~5 min |
| 5 · Q&A | your questions · discussion | 10 min |

## Rebuild

Requires [Marp CLI](https://github.com/marp-team/marp-cli) (`npx @marp-team/marp-cli` works too):

```bash
# HTML (speaker notes included as HTML comments)
npx @marp-team/marp-cli --allow-local-files \
  lecture/agentic-ai-for-lead-generation.md -o lecture/agentic-ai-for-lead-generation.html

# PDF / PPTX
npx @marp-team/marp-cli --allow-local-files --pdf  lecture/agentic-ai-for-lead-generation.md -o lecture/agentic-ai-for-lead-generation.pdf
npx @marp-team/marp-cli --allow-local-files --pptx lecture/agentic-ai-for-lead-generation.md -o lecture/agentic-ai-for-lead-generation.pptx
```

## Student resources (from the deck)

- **JLU HRZ API-Service** — free LLM endpoints for JLU members ([uni-giessen.de → HRZ → KI → API-Service](https://www.uni-giessen.de/de/fbz/svc/hrz/svc/services/ki/api-service), access: ki@uni-giessen.de)
- **Google AI student plan** — 1 year free ([one.google.com/ai-student](https://one.google.com/ai-student?g1_landing_page=75))
- **OpenRouter** · **OpenCode** · **pi** · **Ollama** — see the providers slide
- This research corpus ([README](../README.md)) is the evidence base for the "why now" slide
