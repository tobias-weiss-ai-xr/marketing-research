# Demo script — Walkthrough (Block 3, ~13 min)

Live demo in the pi harness. The contract is [`AGENTS.md`](AGENTS.md) in this
folder; the target result looks like [`shortlist-template.md`](shortlist-template.md).

## Pre-flight (before the lecture, ~5 min)

- [ ] Network works **in the lecture hall** — test hall Wi-Fi, not office Wi-Fi
- [ ] `pi` starts, model selected (fast model is fine — speed beats depth)
- [ ] Browser tool (BrowserMCP/MCP) connects — open one company page once
- [ ] This folder open in the editor: `lecture/demo/`
- [ ] **Fallback:** run the demo at home beforehand and save the pi transcript to `fallback-session.md` next to this file (offline backup)

## Kickoff prompt (paste after showing AGENTS.md)

```text
Read AGENTS.md in this folder and follow it. Build the shortlist for
2 companies from the German grocery retail sector (e.g. a discounter
and a wholesaler). Show your plan first, then work step by step.
```

Small scope on purpose: 2 companies, one industry — the demo must finish.

## Narration beats

| Minute | What happens | What you say |
|---|---|---|
| 0–2 | Show `AGENTS.md` (slide 11) | "This is the contract — the agent reads this at every start. Done means: verified, cited, repeatable." |
| 2–3 | Paste kickoff prompt, agent plans | "Watch the plan — it maps to the six boxes from the pipeline slide." |
| 3–8 | Agent browses, extracts, scores | Narrate each tick: source → fit signal → score → URL. Point at the pipeline boxes. |
| ~6 | **Deliberate stumble** | If the agent invents or over-claims, stop it: "Which URL says that?" — let it correct itself. **This is the loop.** |
| 8–11 | Agent writes the table, re-checks URLs | "It verifies its own citations — that is step 5." |
| 11–13 | Final table → slide 13 (three questions) | "Now we judge it: checked? citable? repeatable?" |

## Timing guard

- Hard stop at minute 11 for the final table — if the demo runs long, cut the
  second company and show the table with one.
- Bank questions: "Hold that for Q&A — we have 10 minutes at the end."

## Fallback (no network in the hall)

1. Show `AGENTS.md` and walk through what *would* happen (slide 11–12).
2. Open the saved `fallback-session.md` transcript and walk the audience
   through it.
3. Still apply the three questions to the saved result — the method lands either way.
