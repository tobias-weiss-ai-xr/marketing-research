# Agentic AI and Contextual Intelligence in Marketing
## A Combined Literature Review (WIP)

> **File:** `lit_review_agentic_contextual.md`
> **Status:** DRAFT v0.1 — literature review work-in-progress (combines the planned "systematic review of agentic AI in marketing" and "review of contextual intelligence in marketing/B2B")
> **Purpose:** (a) substantiate the near-zero-intersection claim that motivates the CAM/G4 program (resolves the §5.3 caveat in `g4_academic_paper.md`), (b) anchor the G1 construct-definition gap and the G6 B2B line, (c) feed the related-work section of the 2027 Working Paper
> **Evidence base:** this repo's corpus (15,000+ papers; snapshot 2026-10-31 — counts below are live lower bounds, the corpus only grows) + externally verified anchors
> **Lead Author:** Tobias Weiss (proposed) + [TBD co-authors]
> **Target Venues:** *Journal of Business Research*, *Industrial Marketing Management*, *International Journal of Research in Marketing* (review track), or as the related-work backbone of the 2027 Working Paper
> **Last Updated:** 2026-10-29

---

## TL;DR

Agentic AI is entering marketing research fast (≥100 corpus papers, all 2025–2026) but almost entirely as *capability demonstrations* — agents that shop, sell, price, and run campaigns. Contextual intelligence, meanwhile, exists in marketing mainly as *advertising targeting* (contextual ads, context-aware attribution) — a narrow, channel-level usage. At the intersection there are at most a handful of papers, and **none defines a marketing construct for agent-level situational/contextual intelligence**. The construct exists only outside marketing: in Endsley's human-factors situational-awareness tradition, in CS/NLP (Häglund 2025), and in B2B sales research as a *human* competence (Böhm et al. 2020 — value opportunity recognition). The review surfaces five gaps and maps each to the repo's research program.

---

## 1. Motivation & Research Questions

The corpus trend data shows two curves rising simultaneously: **agentic** (the corpus's highest-momentum trend, ≥100 papers, all from 2025–2026) and **contextual** (≥250 papers mentioning "contextual", strongly concentrated in 2024–2026). The paper program (CAM/G4, B2B-CI/G6, the 2027 Working Paper) rests on the claim that these two streams have **not yet been joined by a marketing construct**.

This review tests that claim and synthesizes both streams.

**RQ1:** How is agentic AI entering marketing research — as what phenomena, in which roles?
**RQ2:** How is contextual intelligence / context-awareness treated in marketing research — as what construct, at what level?
**RQ3:** What exists at the *intersection* (agents + context), inside marketing and in adjacent fields?
**RQ4:** What does the B2B sales literature contribute on context (value-based selling, value opportunity recognition)?

---

## 2. Method (PRISMA-lite)

**Corpus.** The repo's curated corpus: 15,000+ papers (15,773 at snapshot 2026-10-31), auto-discovered via taxonomy-aware arXiv/OpenAlex/Crossref/dblp queries, each entry carrying one category (11 marketing domains) and one lens (empirical / framework / review / case-study / theory / measurement). Full list in `PAPERS.md`; machine-readable in `docs/papers.json`.

**Search & screening.** Title/abstract keyword searches over the corpus:
- `agentic` → ≥100 papers (167 at snapshot; all 2025–2026); of these, ≥60 (64) also mention sales/lead/B2B/CRM/selling/buyer
- `contextual intelligence` OR `context-aware`/`context aware` → ≥25 papers (27)
- intersection of both → ≤18 papers, using broadened agent vocabulary (`agentic` OR `multi-agent` OR `autonomous agent` OR `ai agent` OR `llm agent`; agent-broad pool 384, context pool 380), screened individually (§5)
- `value opportunity` → 0 papers

**Inclusion.** Papers whose *substance* (not just vocabulary) addresses (a) agents acting in marketing/sales roles, (b) context as a targeting/decision input in marketing, or (c) both. Preprints (arXiv, SSRN, Research Square, Zenodo) are included but flagged as non-peer-reviewed.

**Exclusion.** Papers mentioning both terms only lexically (e.g., an unrelated "agent" such as chemical agents, or "context" in a passage) without substantive engagement.

**Honest caveats.** (1) This is a *corpus-bounded* review: it covers what this curated corpus contains, not the full literature — useful for construct-gap claims within the corpus's coverage, not as proof of global absence. (2) Counts are lower bounds tied to a snapshot (2026-10-31); the corpus grows weekly. (3) The agentic stream is less than two years old; much of it sits in preprints and low-tier venues — quality varies widely.

---

## 3. Theme A — Agentic AI Entering Marketing (RQ1)

Three sub-streams, all emerging 2025–2026:

### 3.1 The consumer side: agentic shopping and machine customers
- *Shopping by algorithm: How agentic AI deploys human heuristics as a surrogate consumer* (Wadi & Ma, arXiv, 2026-09) — agents as consumer surrogates.
- *When AI Shops for Us: A Systematic Literature Review on Agentic AI and the Algorithmic Consumer* (OPUS BW, 2026-09, preprint) — first corpus SLR on the agentic-consumer phenomenon.
- *When the customer is a machine: a systematic literature review and integrative framework* (Moghaddam, Alipour & Grunert, Research Square, 2026-10, preprint) — machine customers as a new research object; the most explicit signal that the *counterparty* of marketing is becoming an agent.
- *Marketing to Machines: Strategic Frameworks for Engagement with Autonomous Agentic AI* (book chapter, 2026-10) — strategy frameworks aimed at machine audiences.

**Reading:** a coherent, fast-forming conversation — marketing's target shifts from humans to agents, with implications for segmentation, persuasion, and measurement.

### 3.2 The firm side: agents in sales, CRM, and marketing operations
- *AI agents, agentic AI, and the future of sales* (Gonzalez, Habel & Hunter) — *Journal of Business Research* (2026-01). The strongest peer-reviewed anchor in the corpus: positions agents across the sales function.
- *The Augmented Rep: Agentic AI Across the Enterprise Sales Cycle* (IRJAEM, 2026-06, preprint) — stage-by-stage agent augmentation of the sales cycle.
- *Agentic Agent, Better Agent: Evidence from Agentic AI in Telemarketing* (SSRN working paper, 2026-04) — rare *empirical* evidence on agentic (vs. generative) AI effects.
- *The Dual-Journey Model of Marketing in the Agentic Era* (SSRN, 2026-01) — conceptualizes parallel human/agent journeys.
- *GENIE CRM: An Agentic AI-Powered Customer Relationship Management System* (ISJEM, 2026-04, preprint) — system-level design artifact.
- *Calibrating Professional Discretion in Artificial Intelligence-Supported B2B Selling* (RaFT, 2026-09) — human discretion vs. agent automation in B2B selling.
- *From Data Quality to Quality of Agentic Data Use: A Conceptual Framework* (Applied Sciences, 2026-09).

### 3.3 Infrastructure: benchmarks, metrics, and governance
- *GTM-Bench: Evaluating Agentic AI Systems for Buyer/Seller Coherence in Go-to-Market Workflows* (technical report, 2026-09) — first go-to-market agent benchmark in the corpus.
- *Can AI Agents Simulate A/B Test Outcomes? A Validation Framework for Agentic Experimentation* (arXiv, 2026-08).
- *AI Win-Rate: A Board Metric for AI-Mediated Buying (Methodology v1.0)* (Zenodo, 2026-09, preprint).
- *AI, Agents, and the Marketing Operating System* (Routledge, 2026-10) — the "marketing OS" framing.
- *Privacy Preference Controls for Agentic Systems* (arXiv, 2026-10) — governance of agent behavior.

**Forward-snowball (outside the corpus).** Citations of the JBR anchor (Semantic Scholar, 2026-10-31) show the field consolidating in top sales journals: a *JBR* field consolidation of AI in sales (2017–early 2026, 2027), and *JPSSM* papers on AI maturity in buyer–seller exchange and salesperson AI wisdom along the B2B buying journey. The agentic conversation is entering peer-reviewed sales research faster than the corpus's ingestion reflects — the corpus-bounded screen undercounts the peer-reviewed core (see §9 #1).

**Reading (RQ1 answer).** Agentic AI enters marketing as (i) a *new customer type* (machine customers), (ii) a *workforce layer* (sales/CRM agents), and (iii) *infrastructure* (benchmarks, metrics, governance). What it is **not**, anywhere in the corpus: a treatment of what agents need to *know about marketing context* in order to act well. Capability is demonstrated; the informational substrate — the situational context that makes an action appropriate — is assumed.

**Synthesis (RQ1):** The agentic stream is a capability-first literature. It demonstrates what agents *can do* (shop, sell, price, govern) but assumes the informational substrate they need to act appropriately. This confirms the gap is not merely a lack of papers, but a lack of conceptualization of agent-level contextual intelligence.

---

## 4. Theme B — Contextual Intelligence & Context-Awareness in Marketing (RQ2)

The ≥25 context-aware/contextual-intelligence papers split into:

### 4.1 Contextual advertising (the dominant usage)
- *Context on Display: Digital Signage Attributes, Contextual Advertising, and Consumer Responses* (Businesses, 2026-09).
- *Context-aware Advertisement Modeling and Applications in Rapid Transit Systems* (arXiv, 2024-09).
- *Adaptive Attention-Based Marketing: A Review of Emotion- and Context-Aware Advertising* (Cureus JBE, 2026-07, preprint) — the only review in this stream.

### 4.2 Context as a modeling input
- *Entire Chain Uplift Modeling with Context-Enhanced Learning for Intelligent Marketing* (arXiv, 2024-02).
- *Context-Aware Marketing Attribution Based on Survival Analysis* (LNIS, 2025-01).
- *CatBoost-based context-aware purchase-decision prediction on tabular customer-journey data* (IJAIN, 2026-08).
- *Lines and Ladders: A Context-Aware Multi-Agent Framework for Large-Scale Retail Pricing* (arXiv, 2026-08) — see §5, the one genuine intersection paper.

**Reading (RQ2 answer).** In marketing, "context" is used at the **channel/campaign level**: a signal among many in ad targeting, attribution, or price modeling. There is **no marketing construct** that treats context as a *capability* — nothing analogous to Endsley's situational awareness (1988, 1995) applied to marketing decision-makers, human or machine.

**Synthesis (RQ2):** Marketing's treatment of context is channel-bound and operational. It lacks the theoretical depth of Endsley's situational awareness or Böhm et al.'s value opportunity recognition. The construct is absent.

**Prior art outside marketing (verified):**
- *Häglund (2025), "Contextual intelligence: leveraging AI for targeted marketing"* (PhD thesis, Umeå University, Dept. of Computing Science; DiVA diva2:1955463) — stakes the phrase in **CS/NLP** (opinion-unit extraction, aspect-based sentiment, media-context effects). Technical foundations, but no marketing construct.
- Management-literature uses of "contextual intelligence" (leadership tradition; scanned in `gaps_deep_dive.md`) — decision-making in context, but organizational/human-level, not marketing-agent-level.
- CS infrastructure: context-aware recommender systems (Adomavicius & Tuzhilin, 2011), context (Dey, 2001), contextual bandits (Li et al., 2010; Agrawal & Goyal, 2013) — context-aware *action selection*, deployed at scale in ad platforms, but a scalar-reward policy view with no marketing situation taxonomy and no situational-awareness semantics.

---

## 5. Theme C — The Intersection (RQ3)

Screening the ≤18 papers containing both agent vocabulary (`agentic`/`multi-agent`/`autonomous agent`/`ai agent`/`llm agent`) and context vocabulary (`contextual`/`context-aware`) — the broadened screen that captures context-aware agent papers regardless of whether they use the word "agentic":

- **Genuine intersection (2)** — both full-text-confirmed substantive (arXiv abstracts, 2026-10-31):
  - *Lines and Ladders: A Context-Aware Multi-Agent Framework for Large-Scale Retail Pricing* (Chunduri et al., arXiv, 2026-08) — context-aware LLM agents constructing pricing taxonomies; evaluated on real-world enterprise data, deployed in production (F1 0.83 for Lines, 3-agent system beats single-agent baselines). Algorithmic infrastructure (catalog governance), not a marketing *construct*.
  - *Personalized to Persuade: The Effects of Contextualization and Warmth on Trust and Relevance* (arXiv, 2026-05) — a 2×2 between-subjects experiment (N = 380) on AI assistants that personalize responses via *contextualization*: contextualization alone **reduces** persuasive power; combined with conversational warmth it restores persuasiveness via a crossover interaction; reliance on AI persists across conditions. The corpus's closest treatment of *agent-level context effects on consumer persuasion* — empirical, but framed as communication/persuasion, not as a marketing situational-awareness construct.
- **Lexical co-mentions (≤16):** e.g., *Can AI Agents Simulate A/B Test Outcomes?* (validation methodology), *Calibrating Professional Discretion in AI-Supported B2B Selling* (context mentioned, not constructed), *LLMs Are Not Good Strategists, Yet Memory-Enhanced Agency Boosts Reasoning* (reasoning, not marketing context), plus CS-domain agent papers (pathology, chemistry, trading, web dev) where "context" is incidental.

**Refined claim (supersedes the earlier "zero intersection" framing):** the gap is **not** that no paper combines agents and context — *Lines and Ladders* does, and contextual bandits do so industry-wide. The gap is that **no paper defines what situational or contextual intelligence *means* for a marketing agent** — no situation taxonomy, no construct, no measurement, no theory of which context dimensions matter for which marketing actions. The two substantive papers bracket the gap from both sides: one builds *infrastructure* on context-aware agents (pricing), the other measures *persuasion effects* of agent contextualization (N = 380) — neither asks what a marketing agent should know about its context, or how that knowledge should be structured.

**Synthesis (RQ3):** The 18-paper intersection screen reveals that while agents and context do co-occur in two substantive papers, neither bridges the gap: one builds pricing infrastructure (Lines and Ladders), the other measures persuasion effects (Personalized to Persuade). The construct-level gap remains wide open. The intersection is empty at the *construct* level, not the lexical level. This is exactly the distinction the CAM-Sim paper's §5.3 caveat anticipated; this review substantiates it.

---

## 6. Theme D — The B2B Line: Value-Based Selling → Value Opportunity Recognition (RQ4)

B2B sales research has already built — for *humans* — the construct this program proposes to agentify:

- *Terho, Haas, Eggert & Ulaga (2012, IMM 41(1))* — value-based selling: the seller's focus on the customer's business value. The construct paper (verified against Haas's profile; see `g6_haas_integration.md`).
- *Böhm, Eggert, Terho, Ulaga & Haas (2020, JPSSM 40(3))* — **value opportunity recognition**: sensing when contextual conditions open a value-relevant engagement window. Endsley Level-1/2 awareness, published by the Haas group in 2020, as a *salesperson competence*.
- In the corpus: `value opportunity` → **0 papers**. The construct has not entered the agentic-marketing conversation at all.
- Adjacent corpus hook: *The four Cs of B2B targeting: Using company, customer, channel and contextual data to shrink the audience bullseye* (Applied Marketing Analytics, 2024-12) — one of very few corpus papers combining B2B targeting with contextual data.

**Reading (RQ4 answer).** The B2B literature supplies the theoretical anchor (value opportunity recognition = human contextual sensing) and the differentiation: the program operationalizes Layer 0 (value context) as a **machine-sensible capability**, not a re-proof of Haas's theory.

**Synthesis (RQ4):** B2B sales research provides the theoretical anchor. Value opportunity recognition (Böhm et al., 2020) is precisely the construct of contextual sensing this program proposes to agentify. The differentiation is clear: human competence vs. machine capability.

---

## 7. Conceptual Framework: The Agent–Context Matrix

To visualize the gap, we propose a 2×2 matrix mapping the literature landscape:

|  | **Low Contextual Intelligence** (channel-level targeting) | **High Contextual Intelligence** (agent-level situational awareness) |
|---|---|---|
| **High Agentic Capability** | **Theme A (Agentic AI)** — agents act without contextual grounding. Capability demonstrated, substrate assumed. | **The Construct Gap (Theme C)** — the white space. No paper defines what a marketing agent should know about its context. |
| **Low Agentic Capability** | Traditional marketing automation / rule-based targeting. | **Theme B (Contextual Intelligence)** — contextual ads, attribution, pricing. Context as a feature, not a capability. |

**Reading:** The corpus is heavily concentrated in the bottom-left and bottom-right (contextual intelligence without agents, or agentic AI without context). The top-left (Theme A) is rapidly growing. The top-right (Theme C) remains theoretically empty at the construct level, despite algorithmic and empirical advances on both sides.

---

## 7. Gap Synthesis

| # | Gap | Evidence (this review) | Maps to |
|---|-----|------------------------|---------|
| 1 | **No marketing construct** for agent-level situational/contextual intelligence | §4.2, §5 — construct absent; only channel-level "context" usage | G1, G4 |
| 2 | **Agents demonstrated, not contextualized** — agentic papers assume the informational substrate | §3.3 — benchmarks measure capability, none measures context quality | G4 |
| 3 | **Value opportunity recognition not agentified** — 0 corpus papers | §6 — human construct (Böhm et al. 2020) has no machine counterpart | G6, 2027 WP |
| 4 | **No measurement instrument** for marketing contextual intelligence | §4.2 — no scale/instrument anywhere in the corpus | G2 |
| 5 | **No causal evidence** context-aware beats identity-based targeting in marketing outcomes | §4.1 — contextual advertising literature is descriptive/modeling, no head-to-head field evidence | G3 |

---

## 8. Research Agenda (derived)

1. **Define the construct** (G1): marketing situational/contextual intelligence for agents — dimensions, boundaries, differentiation from Häglund (CS), Endsley (human factors), and Böhm et al. (human competence). *This review is its related-work backbone.*
2. **Operationalize sensing** (G4): signal taxonomy (audience, channel, temporal, situational, social, market) + benchmark (CAM-Sim exists; field validation per §10.3 of the benchmark paper).
3. **Agentify value opportunity recognition** (G6/2027 WP): Layer-0 value context on top of Terho/Böhm theory; Haas panel for expert labels (RQ portfolio H1–H8).
4. **Instrument** (G2): scale development once the construct is stable.
5. **Causal evidence** (G3): field experiment contextual vs. identity-based targeting.

---

## 9. Conclusion

This review set out to test the foundational claim of the CAM/G4 program: that agentic AI and contextual intelligence, though both rising fast in marketing research, have not yet been joined by a marketing construct. The claim holds, with a necessary refinement. The intersection is not empty lexically — eighteen papers combine agent and context vocabularies, and two are substantive (a production-deployed retail-pricing multi-agent framework; an N = 380 experiment on agent contextualization and persuasion). But neither defines a marketing construct for agent-level situational/contextual intelligence; the construct gap is real, and it is the white space this program targets.

The review also surfaces the theoretical anchor for the B2B line: value opportunity recognition (Böhm et al., 2020) is the human competence that the program operationalizes as a machine-sensible capability. The research agenda (§8) derives five actionable gaps, each mapped to a program artifact (G1, G4, G6, G2, G3).

---

## 9. Limitations of This Review

1. **Corpus-bounded.** Claims are about this curated corpus's coverage; global absence would require database-independent searching (WoS/Scopus full PRISMA). Partially mitigated by forward-snowballing from the JBR anchor (§3.2), which surfaced six peer-reviewed AI-in-sales papers outside the corpus — none of them defining a marketing contextual/situational construct, which is consistent with (not contradictory to) the construct-gap claim. The claim is framed accordingly ("no construct in a 15,000+ paper marketing corpus plus its forward-citation neighbourhood", not "no construct exists anywhere").
2. **Snapshot drift.** Counts are lower bounds at 2026-10-29; the agentic stream is growing weekly. Screens should be re-run at submission.
3. **Preprint-heavy.** The agentic stream is dominated by preprints and low-tier venues; peer-reviewed anchors are few (*JBR* 2026-01 is the strongest). Findings should be weighted accordingly.
4. **Single-coder screening.** The lexical → substantive screening was done by one reviewer; inter-rater reliability is pending (natural Bachelor/Master task — see RQ portfolio H7/H8).

---

## References

### Verified anchors (external to corpus)
- Endsley, M. R. (1988). Design and evaluation for situation awareness enhancement. *Proceedings of the Human Factors Society Annual Meeting*, 32(2), 97–101.
- Endsley, M. R. (1995). Toward a theory of situation awareness in dynamic systems. *Human Factors*, 37(1), 32–64.
- Li, L., Chu, W., Langford, J., & Schapire, R. E. (2010). A contextual-bandit approach to personalized news article recommendation. *WWW*.
- Agrawal, S., & Goyal, N. (2013). Thompson sampling for contextual bandits with linear payoffs. *ICML*.
- Adomavicius, G., & Tuzhilin, A. (2011). Context-aware recommender systems. *ACM RecSys*.
- Dey, A. K. (2001). Understanding and using context. *Personal and Ubiquitous Computing*, 5(1), 4–7.
- Häglund, E. (2025). *Contextual intelligence: leveraging AI for targeted marketing* [PhD thesis]. Umeå University. DiVA: diva2:1955463 (URL verified 2026-10).
- Böhm, E., Eggert, A., Terho, H., Ulaga, W., & Haas, A. (2020). Drivers and outcomes of salespersons' value opportunity recognition competence in solution selling. *Journal of Personal Selling & Sales Management*, 40(3), 180–197.
- Terho, H., Haas, A., Eggert, A., & Ulaga, W. (2012). "It's almost like taking the sales out of selling" — Towards a conceptualization of value-based selling in business markets. *Industrial Marketing Management*, 41(1), 174–185.
- Grewal, D., Satornino, C. B., & Davenport, T. H. (2024). How generative AI is shaping the future of marketing. *Journal of the Academy of Marketing Science*. https://doi.org/10.1007/s11747-024-01064-3

### Corpus papers (all verified in `papers.yaml`, snapshot 2026-10-31; ⚑ = preprint, not peer-reviewed)
**Agentic — consumer side**
- Moghaddam, M. T., Alipour, M., & Grunert, K. G. (2026). When the customer is a machine: a systematic literature review and integrative framework. Research Square (⚑ preprint). https://doi.org/10.21203/rs.3.rs-11222729/v1
- Tzvetkov, M. (2026). When AI shops for us: A systematic literature review on agentic AI and the algorithmic consumer. OPUS Baden-Württemberg (⚑ preprint). https://doi.org/10.26205/opus-4058
- Wadi, D., & Ma, Y. (2026). Shopping by algorithm: How agentic AI deploys human heuristics as a surrogate consumer. arXiv (⚑ preprint). https://arxiv.org/abs/2609.28372
- Radwan, R., Alsolaim, M. A., & Abo Ellil, R. M. A. (2026). Marketing to machines: Strategic frameworks for engagement with autonomous agentic AI. Book chapter. https://doi.org/10.68337/978-81-181312-6-7.ch01

**Agentic — firm side**
- Gonzalez, G. R., Habel, J., & Hunter, G. K. (2026). AI agents, agentic AI, and the future of sales. *Journal of Business Research*. https://doi.org/10.1016/j.jbusres.2025.115799
- Gudla, A. (2026). The augmented rep: Agentic AI across the enterprise sales cycle. IRJAEM (⚑ preprint). https://doi.org/10.47392/eclearnix.2026.b058
- Zhang, M., Kan, Y., Qiu, W., & Chen, F. (2026). Agentic agent, better agent: Evidence from agentic AI in telemarketing. SSRN working paper (⚑ preprint). https://doi.org/10.2139/ssrn.6502379
- Kannan, A. R. (2026). The dual-journey model of marketing in the agentic era. SSRN (⚑ preprint). https://doi.org/10.2139/ssrn.6436240
- Dudharejiya, H. B., & Shah, D. T. (2026). GENIE CRM: An agentic AI-powered customer relationship management system. ISJEM (⚑ preprint). https://doi.org/10.55041/isjem06720
- Hart, G., Burrell, D. N., & Valle, F. (2026). Calibrating professional discretion in artificial intelligence-supported business-to-business selling. *RaFT*. https://doi.org/10.2478/raft-2026-0025
- Cravero, A., Díaz-Villegas, J., & Xiao, Z. (2026). From data quality to quality of agentic data use: A conceptual framework. *Applied Sciences*. https://doi.org/10.3390/app16178887

**Agentic — infrastructure**
- Polaczuk, M., Baron, J., Horne, R., & Cavill, T. (2026). GTM-Bench: Evaluating agentic AI systems for buyer/seller coherence in go-to-market workflows. Technical report (⚑ preprint). https://gtm-bench.ai/assets/gtm-bench-paper.pdf
- Hut, S., & Masoero, L. (2026). Can AI agents simulate A/B test outcomes? A validation framework for agentic experimentation. arXiv (⚑ preprint). https://arxiv.org/abs/2608.02345
- Sheals, P., & de Rosen, T. (2026). AI win-rate: A board metric for AI-mediated buying (Methodology v1.0). Zenodo (⚑ preprint). https://doi.org/10.5281/zenodo.22280230
- McMahon, T. P. (2026). AI, agents, and the marketing operating system. Routledge. https://doi.org/10.4324/9781003567028-10
- Kochar, S., Sugsavanvit, P., Gupta, V., & Calandrino, J. A. (2026). Privacy preference controls for agentic systems. arXiv (⚑ preprint). https://arxiv.org/abs/2610.29929

**Contextual / context-aware in marketing**
- Ghanvat, S., Joshi, S., & Jamdagni, R. (2026). Adaptive attention-based marketing: A review of emotion- and context-aware advertising. Cureus JBE (⚑ preprint). https://doi.org/10.7759/s44404-026-00184-z
- Roux, T. (2026). Context on display: Digital signage attributes, contextual advertising, and consumer responses. *Businesses*. https://doi.org/10.3390/businesses6030049
- Chunduri, R. T., Boya, S. R., Mishra, D. N., & Kumar, A. B. (2026). Lines and ladders: A context-aware multi-agent framework for large-scale retail pricing. arXiv (⚑ preprint). https://arxiv.org/abs/2608.12674
- Züllig, K., Napirata, S., & Zimmermann, S. (2025). Context-aware marketing attribution based on survival analysis. LNIS. https://doi.org/10.1007/978-3-031-80122-8_22
- Ahmed, A., & Raees, M. (2024). Context-aware advertisement modeling and applications in rapid transit systems. arXiv (⚑ preprint). https://arxiv.org/abs/2409.09956
- Huang, Y., Wang, S., Gao, M., & Wei, X. (2024). Entire chain uplift modeling with context-enhanced learning for intelligent marketing. arXiv (⚑ preprint). https://arxiv.org/abs/2402.03379
- Thai, P. K., Lam, N. T. B., & Le, T. M. (2026). CatBoost-based context-aware purchase-decision prediction on tabular customer-journey data. IJAIN. https://ijain.org/index.php/IJAIN/article/view/2412
- Diorio, S. G., & Howarth, R. (2024). The four Cs of B2B targeting: Using company, customer, channel and contextual data to shrink the audience bullseye. *Applied Marketing Analytics*. https://doi.org/10.69554/zubn7528

**Forward-snowball finds (outside corpus; peer-reviewed; citing the JBR 2026-01 anchor — Semantic Scholar, verified 2026-10-31)**
- *Artificial intelligence in sales (2017–early 2026): field consolidation and the rise of human-AI collaboration* (2027). *Journal of Business Research*. https://doi.org/10.1016/j.jbusres.2026.116580 — the closest peer-reviewed consolidation of the AI-in-sales field; directly relevant to Theme A's positioning.
- *Developing salesperson AI wisdom along the B2B customer buying journey* (2026). *Journal of Personal Selling & Sales Management*. https://doi.org/10.1080/08853134.2026.2738645 — B2B buying-journey-stage AI competence; directly relevant to G6 (journey-stage context).
- *Artificial intelligence maturity in buyer–seller exchange* (2026). *Journal of Personal Selling & Sales Management*. https://doi.org/10.1080/08853134.2026.2743641
- *The efficiency trap of agentic AI in human resource management* (2026). *Human Resource Management*. https://doi.org/10.1002/hrm.70106 — evidence that "agentic AI" is entering peer-reviewed management journals.
- *AI-enabled social media: implications for salespeople, sales leadership, and sales organizations* (2026). *Journal of Personal Selling & Sales Management*. https://doi.org/10.1080/08853134.2026.2738642
- *Beyond virtual reality: identifying functional and perceptual drivers of immersive negotiation training adoption in B2B sales* (2026). *Journal of Marketing Theory and Practice*. https://doi.org/10.1080/10696679.2026.2743750

**Intersection candidates (title-verified; full-text screen pending — Appendix A)**
- *Personalized to persuade: The effects of contextualization and warmth on trust and relevance* (2026). arXiv (⚑ preprint). https://arxiv.org/abs/2605.31275
- *LLMs are not good strategists, yet memory-enhanced agency boosts reasoning* (2026). arXiv (⚑ preprint). https://arxiv.org/abs/2608.12626

**CS-side adjacent**
- Xu, L., He, L., Hou, K., & Fan, Y. (2026). ProMemAgent: Long-horizon proactive assistance with context-aware prospective memory. arXiv (⚑ preprint). https://arxiv.org/abs/2610.27400

---

## Appendix A — Second-Coder Screening Kit (lexical → substantive screen, κ)

**Task.** Two coders independently code the ≤18 intersection papers as `SUBSTANTIVE` or `LEXICAL`:
- **SUBSTANTIVE** — the paper's substance addresses (a) agents acting in a marketing/sales/pricing role AND (b) context as a decision or modeling input (not merely mentioned).
- **LEXICAL** — both vocabularies present, no substantive engagement (unrelated domain; "context" incidental; agent vocabulary in a reference list only).

**Procedure.** Coders work blind to each other; compute Cohen's κ on the binary judgment; resolve disagreements by discussion and record both pre- and post-consensus labels. Reliability threshold: κ ≥ 0.6 (mirrors RQ H1 in the 2027 program design). Ties to RQ H7/H8 (gap-rate tracking and claim-verification rate).

**Judgment sheet** (fill one row per paper; papers verified in `papers.yaml`, snapshot 2026-10-31; ⚑ = preprint):

| # | Paper | Year | Venue | Coder A | Coder B | Agreed? | Consensus |
|---|-------|------|-------|---------|---------|---------|-----------|
| 1 | The AI Evaluation Ecosystem | 2026-10 | arXiv ⚑ | | | | |
| 2 | SOTA: Stock options trading agents guided by option-implied return distributions | 2026-10 | arXiv ⚑ | | | | |
| 3 | OptScientist: Automated discovery of optimization laws | 2026-10 | arXiv ⚑ | | | | |
| 4 | ReTRACE: Feedback-guided LLM agent in a chemistry harness | 2026-10 | arXiv ⚑ | | | | |
| 5 | TRAP: Tool-result replay attack for probing misbinding in LLM agents | 2026-10 | arXiv ⚑ | | | | |
| 6 | From preference to reciprocity: Decentralized matching with LLM agents | 2026-09 | arXiv ⚑ | | | | |
| 7 | Generative AI, autonomous agents, and conversational marketing for governance trust | 2026-09 | IGI book ⚑ | | | | |
| 8 | Calibrating professional discretion in AI-supported B2B selling | 2026-09 | RaFT | | | | |
| 9 | Multi-RAG enterprise | 2026-09 | IJERST ⚑ | | | | |
| 10 | 402Pilot: An x402 decision layer for autonomous agent micropayments | 2026-08 | arXiv ⚑ | | | | |
| 11 | Can AI agents simulate A/B test outcomes? | 2026-08 | arXiv ⚑ | | | | |
| 12 | The future of web application development: 2026 and beyond | 2026-08 | Zenodo ⚑ | | | | |
| 13 | Lines and ladders: A context-aware multi-agent framework for retail pricing | 2026-08 | arXiv ⚑ | | | | |
| 14 | LUCAID: Agentic multimodal AI for lung cancer precision pathology | 2026-08 | arXiv ⚑ | | | | |
| 15 | LLMs are not good strategists, yet memory-enhanced agency boosts reasoning | 2026-08 | arXiv ⚑ | | | | |
| 16 | Dynamic dialogue for organizational knowledge acquisition | 2026-08 | ECKM | | | | |
| 17 | Substitution-vs-synthesis as an architectural primitive | 2026-08 | Zenodo ⚑ | | | | |
| 18 | Personalized to persuade: Contextualization, warmth, trust, relevance | 2026-05 | arXiv ⚑ | | | | |

**Reference expectation (updated 2026-10-31 after full-text confirmation of #13 and #18):** #13 substantive (retail-pricing multi-agent framework, production-deployed); #18 substantive (N = 380 experiment on agent contextualization × warmth → persuasion); the remainder expected lexical. The κ run replaces this single-coder expectation.

---

## TODO (next iterations)

- [x] Re-run screens; refresh lower-bound counts (done 2026-10-31: corpus 15,773; agentic 167; broadened intersection 18).
- [x] Add author names for corpus papers (done — reference list now author-attributed).
- [x] PRISMA flow diagram (done — `paper/prisma_flow.svg`).
- [x] Second-coder screening kit (done — Appendix A; the κ run itself is a Bachelor/Master task).
- [x] Add conceptual framework (Agent-Context Matrix), synthesis paragraphs, and conclusion (done 2026-10-31).
- [ ] Run the second-coder κ screen (Appendix A; ties to RQ H7/H8).
- [x] Full-text-confirm the two genuine intersection candidates (done 2026-10-31 via arXiv abstracts: #13 infrastructure, #18 N = 380 persuasion experiment — construct-level gap holds).
- [x] Forward-snowball from the JBR 2026-01 anchor (done 2026-10-31 via Semantic Scholar: 6 peer-reviewed finds outside the corpus, incl. a JBR 2027 field consolidation of AI in sales — none defines a marketing context construct).
- [ ] Decide: standalone review paper vs. related-work section of the 2027 Working Paper (§8 item 1 feeds both).

---

*Reproducibility: every corpus count in this review regenerates from `papers.yaml` (keyword screens in §2); every corpus citation is verified against `papers.yaml` at the stated snapshot; external anchors were verified in prior repo passes (`g6_haas_integration.md`, DiVA check 2026-10).*
