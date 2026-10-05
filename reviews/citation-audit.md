# Citation Audit — paper/g4_academic_paper.md (CAM, DRAFT v0.4)

**Task ID:** citation-audit · **Corpus:** papers.yaml (9,994 entries verified by count) · **Paper NOT modified.**

## Summary

Every citation in `g4_academic_paper.md` was inventoried and cross-referenced against `papers.yaml` (full-text title/author search) and, for corpus-external works, against public bibliographic records. **Ten distinct citable works** appear (7 named scholarly references + 2 specific corpus papers + 1 bulk-corpus reference). The paper contains **zero fabricated citations**. A repo-wide `grep -i haas` on the paper returns **0 hits** — none of the four Haas citations that contaminated v0.1 of the related G6 paper survive here (Böhm et al. 2020 legitimately lists Haas as fifth co-author, but the G4 paper cites it correctly as "Böhm et al. 2020" with no Haas-specific claim). Likewise, the Haglund / Häglund (2025) thesis citation checks out as a real Umeå University dissertation (details below). Minor editorial defects exist (see Missing from References): two in-text citations absent from the References section, one orphan reference, and one suspect URN.

## Verified in Corpus (papers.yaml)

| Citation | Location | Evidence |
|---|---|---|
| "From Personalisation to Agentic Campaigns: Modern Marketing Techniques Using Artificial Intelligence in the Indian Context" (2026-07) | §5.3, References | Exact title + date match, papers.yaml ~line 66674 (corpus index ≈ #5232; DOI 10.55041/ijcope.v2i7.073). The paper's label "#5269" reflects an older corpus snapshot — cosmetic. |
| "I hope we don't do to trust what advertising has done to love" (2026-04, J. Alglave) | §5.3, References | Exact title + date match, papers.yaml ~line 95951 (corpus index ≈ #7484; arXiv 2604.28113). Same "#7535" snapshot caveat. |
| Bulk refs "All 61 agentic / 44 contextual papers from papers.yaml" | §5.1, §5.2, References | Aggregate pointer to the corpus, not individual claims; corpus total 9,994 matches the paper's stated corpus size. Naive regex counts (70/115) differ from 61/44 — methodology-dependent; the paper itself flags the breakdown for re-verification before submission. |

## Corpus-External (textbooks/standards — verified real, correctly outside papers.yaml)

| Citation | In-text | References | Status |
|---|---|---|---|
| Endsley, M. R. (1988). Situation Awareness in Dynamic Systems. Proc. Human Factors Society 32(1), 97–101 | §4.1, §6.1 | ✓ | Real; canonical SA reference. |
| Endsley, M. R. (1995). Toward a Theory of Situation Awareness in Dynamic Systems. Human Factors 37(1), 32–64 | §4.1, §6.1, §9.4, §10.2 | ✓ | Real; canonical SA reference. |
| Russell, S. J., & Norvig, P. (2020). AI: A Modern Approach (4th ed.). Pearson | §4.2 | ✓ | Real textbook. |
| Peppers, D., & Rogers, M. (1993). The One to One Future. Currency | §4.3 | ✓ | Real book. |
| Kotler, P., & Armstrong, G. (2021). Principles of Marketing (18th ed.). Pearson | **never cited in-text** | ✓ | Real textbook, but an **orphan reference** (see below). Kotler-authored corpus *papers* exist in papers.yaml but are unrelated. |
| Häglund, E. (2025). Contextual intelligence: leveraging AI for targeted marketing [PhD Thesis]. Umeå University | §2 (abstract), §3.2 ×2, §5.4 | ✓ | **Real thesis, externally verified**: Umeå University, Dept. of Computing Science, defended 2025 (DiVA record diva2:1955463; WASP-HS defense announcement 2025-06). Title, author, year, institution all match. Häglund also appears in papers.yaml as author of the related 2024 JCIRA paper. **Metadata flag:** the cited URN `urn:nbn:se:umu:diva-238303` does **not** match the public DiVA record (diva2:1955463 → `diva-1955463`); fix before submission. |
| Böhm, E., Eggert, A., Terho, H., Ulaga, W., & Haas, A. (2020). Drivers and outcomes of salespersons' value opportunity recognition competence in solution selling. JPSSM 40(3), 180–197 | §10.3 | **missing** | Real paper (full citation present in sibling `paper/g6_haas_integration.md`, consistent across the repo); not in papers.yaml → corpus-external. See below. |

## Unverified/Suspicious

**None.** No fabricated or unverifiable citations found. No Haas-specific citations remain (grep: 0 hits in this paper). The only suspicious-looking item — the Häglund URN suffix — is a metadata typo on a verified-real thesis, not a fabricated work.

## Missing from References

1. **Godin (1999), Permission Marketing** — cited in-text (§4.3, line 77) but absent from the References section.
2. **Böhm et al. (2020), JPSSM** — cited in-text (§10.3, line 514) but absent from the References section. (Full citation exists in `paper/g6_haas_integration.md`; add it here.)
3. **Orphan reference:** Kotler & Armstrong (2021) is listed in References but never cited in-text — either cite it or drop it.

## VERDICT

**PASS** — no fabricated or unverifiable citations remain; all ten citable works trace to verifiable sources (2 corpus entries, 7 real external works, 1 aggregate corpus pointer). The four fabricated Haas citations from v0.1 of the related paper have no trace in this document. Before journal submission, fix three editorial items: add Godin (1999) and Böhm et al. (2020) to References, resolve the Kotler & Armstrong (2021) orphan entry, and correct the Häglund URN to match DiVA (diva-1955463).
