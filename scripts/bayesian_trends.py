#!/usr/bin/env python3
"""Bayesian trend analysis for the marketing corpus.

Two exact-conjugate analyses (no MCMC needed):

1) Category share-shift (Beta-Binomial): for each category, the share of the
   corpus it occupies in a 12-month prior window vs a 12-month recent window.
   Beta(1+y, 1+N-y) posteriors; ratio of shares sampled via Monte Carlo.
   Share-shift cancels the global fetch/relevance bias (which depresses ALL
   counts equally), so it measures *compositional* change: which areas are
   gaining ground in the recent literature.

2) Term ratio (Gamma-Poisson): mentions of a trend term in title+abstract,
   recent vs prior window, Gamma(1,1) prior -> exact Gamma posteriors.

Caveat (documented in the one-pager): the corpus is relevance-sorted OpenAlex
fetches, so within-window counts under-represent very recent work; share-shift
is robust to that, absolute rates are not.

Usage:
    python3 scripts/bayesian_trends.py [--prior-start 2024-08] [--recent-start 2025-08]
"""

import argparse
import json
from collections import Counter

import numpy as np
import yaml

REPO = __file__.rsplit("/", 2)[0]
RNG = np.random.default_rng(42)
A0, B0 = 1.0, 1.0  # Gamma prior for Poisson rates
N_SAMPLES = 400_000


def shift(start, months):
    y, m = int(start[:4]), int(start[5:7])
    m += months
    y += (m - 1) // 12
    m = (m - 1) % 12 + 1
    return f"{y:04d}-{m:02d}"


def in_window(date, start, months=12):
    return bool(date) and start <= date < shift(start, months)


def beta_ratio(y_cat, n, y_cat_p, n_p):
    """Posterior samples of share_recent / share_prior (Beta-Binomial)."""
    s_r = RNG.beta(1 + y_cat, 1 + (n - y_cat), size=N_SAMPLES)
    s_p = RNG.beta(1 + y_cat_p, 1 + (n_p - y_cat_p), size=N_SAMPLES)
    return s_r / s_p


def gamma_ratio(y_recent, y_prior, exp_recent=12, exp_prior=12):
    lam_r = RNG.gamma(A0 + y_recent, scale=1.0 / (B0 + exp_recent), size=N_SAMPLES)
    lam_p = RNG.gamma(A0 + y_prior, scale=1.0 / (B0 + exp_prior), size=N_SAMPLES)
    return lam_r / lam_p


def summarize(name, samples, y_recent, y_prior, extra=None):
    out = {
        "cell": name,
        "recent": int(y_recent),
        "prior": int(y_prior),
        "median": round(float(np.median(samples)), 2),
        "cr95_low": round(float(np.percentile(samples, 2.5)), 2),
        "cr95_high": round(float(np.percentile(samples, 97.5)), 2),
        "p_gt_1": round(float(np.mean(samples > 1.0)), 3),
    }
    if extra:
        out.update(extra)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prior-start", default="2024-08")
    ap.add_argument("--recent-start", default="2025-08")
    args = ap.parse_args()

    papers = yaml.safe_load(open(f"{REPO}/papers.yaml"))["papers"]
    cfg = yaml.safe_load(open(f"{REPO}/config/taxonomy.yaml"))
    cats = [c["id"] for c in cfg["taxonomy"]["categories"]]
    display = {c["id"]: c["display"] for c in cfg["taxonomy"]["categories"]}

    # Monthly counts per category + per-year totals
    by_cat_month = {c: Counter() for c in cats}
    for p in papers:
        c = p.get("category")
        if c in by_cat_month:
            by_cat_month[c][p.get("date", "")[:7]] += 1

    # ---- 1) Category share-shift (Beta-Binomial) ----
    counts = {c: {"r": 0, "p": 0} for c in cats}
    for c in cats:
        counts[c]["r"] = sum(v for k, v in by_cat_month[c].items() if in_window(k, args.recent_start))
        counts[c]["p"] = sum(v for k, v in by_cat_month[c].items() if in_window(k, args.prior_start))
    n_r = sum(v["r"] for v in counts.values())
    n_p = sum(v["p"] for v in counts.values())

    share_results = []
    for c in cats:
        y_r, y_p = counts[c]["r"], counts[c]["p"]
        ratio = beta_ratio(y_r, n_r, y_p, n_p)
        share_results.append(summarize(display[c], ratio, y_r, y_p,
                                       {"share_recent_pct": round(100 * y_r / n_r, 1),
                                        "share_prior_pct": round(100 * y_p / n_p, 1)}))

    # ---- 2) Term ratio (Gamma-Poisson) ----
    terms = [
        "agentic", "generative ai", "genai", "llm", "large language", "copilot",
        "influencer", "creator", "virtual influencer", "tiktok", "short-form",
        "cookieless", "first-party", "privacy", "consent",
        "retail media", "omnichannel", "customer journey",
        "social commerce", "ugc", "user-generated", "community",
        "sustainability", "purpose", "circular",
        "marketing mix", "mmm", "attribution", "incrementality", "experiment",
        "programmatic", "account-based", "abm", "b2b",
        "metaverse", "ar ", "storytelling", "personaliz", "recommend", "email",
    ]
    term_counts = {t: Counter() for t in terms}
    for p in papers:
        d = p.get("date", "")
        if in_window(d, args.recent_start):
            w = "r"
        elif in_window(d, args.prior_start):
            w = "p"
        else:
            continue
        text = (p.get("title", "") + " " + (p.get("abstract") or "")).lower()
        for t in terms:
            if t in text:
                term_counts[t][w] += 1

    term_results = []
    for t, cts in term_counts.items():
        r, p = cts["r"], cts["p"]
        if r + p >= 6:
            term_results.append(summarize(t, gamma_ratio(r, p), r, p))

    out = {
        "share_trends": sorted(share_results, key=lambda r: -r["median"]),
        "term_trends": sorted(term_results, key=lambda r: -r["median"]),
        "windows": {"prior": args.prior_start, "recent": args.recent_start},
        "corpus_totals": {"recent_window": n_r, "prior_window": n_p},
    }
    with open(f"{REPO}/docs/research/bayesian_trends.json", "w") as f:
        json.dump(out, f, indent=2)

    print(f"Corpus in windows: prior {n_p} | recent {n_r}")
    print(f"\n=== Category share-shift (recent/prior share ratio; Beta-Binomial) ===")
    print(f"{'category':<38}{'recent':>7}{'prior':>7}{'shr%→%':>12}{'median':>8}{'95% CrI':>16}{'P>1':>6}")
    for r in share_results:
        print(f"{r['cell']:<38}{r['recent']:>7}{r['prior']:>7}"
              f"{str(r['share_recent_pct'])+'→'+str(r['share_prior_pct']):>12}"
              f"{r['median']:>8.2f}[{r['cr95_low']:>6.2f},{r['cr95_high']:>6.2f}]"
              f"{r['p_gt_1']:>6.3f}")

    print(f"\n=== Term trends (Gamma-Poisson; min 6 mentions) ===")
    for r in term_results[:22]:
        print(f"{r['cell']:<18}{r['recent']:>5}/{r['prior']:<5}{r['median']:>7.2f}"
              f" [{r['cr95_low']:>5.2f},{r['cr95_high']:>5.2f}]  P={r['p_gt_1']:.2f}")


if __name__ == "__main__":
    main()
