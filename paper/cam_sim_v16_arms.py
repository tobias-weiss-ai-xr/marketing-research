#!/usr/bin/env python3
"""CAM-Sim v1.6 — Prompt-variant experiment harness with P1 diagnostics, P2 remediation arms, and P3 bootstrap statistics.

Extends the CAM-Sim LLM baseline (paper section 8.21) with eight experimental arms:
  ARM A: order-permutation (6 permutations of class-definition blocks)
  ARM B: minimal-labels (no definitions, just labels)
  ARM C: counterfactual-archetypes (42 probes at canonical centroids)
  ARM D: decoy-removal (omit quality_score from signals)
  ARM E: qualitative-hints (add two hint sentences)
  ARM F: few-shot (add six exemplar lines)
  ARM G: self-consistency (k=5 samples, majority vote)
  ARM H: end-to-end (LLM outputs full action line)

Usage:
    python3 paper/cam_sim_v16_arms.py --selftest
    python3 paper/cam_sim_v16_arms.py --arms A,B,E --models tud/mistral-medium-3.5-128b
    python3 paper/cam_sim_v16_arms.py --max-passes 4

Requires env: SAIA_API_KEY, ZAI_API_KEY, GROQ_API_KEY, TUD_API_KEY, LITELLM_API_KEY (for real runs).
"""
import argparse
import hashlib
import itertools
import json
import os
import random
import re
import sys
import time
import urllib.error
import urllib.request
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))

from cam_sim import (Action, ActionType, CAMOracle, ChannelType, IDEAL_ACTION,
                     SITUATION_CHANNEL, SimulationEnvironment, SituationType)
from cam_sim_v15_llm import (CACHE_DIR, PROVIDERS, SEEDS, build_reference_agents,
                             classify_with_retry, confusion, parse_label, paired,
                             paired_scenarios, textualize, walk_with_scenarios)

N_SCEN = 200
OUT = Path(__file__).resolve().parent.parent / "results"
ARMS_CACHE = OUT / "llm_cache" / "arms.jsonl"
LABELS = [s.value for s in SituationType]
LABEL_ORDER = {l: i for i, l in enumerate(LABELS)}

# Canonical centroids for ARM C (intent, competitive_density, channel_quality)
ARCHETYPES = {
    "exploration": (0.2, 0.5, 0.7),
    "consideration": (0.5, 0.5, 0.7),
    "decision": (0.9, 0.5, 0.7),
    "crisis": (0.8, 0.85, 0.2),
    "opportunity": (0.5, 0.85, 0.7),
    "retention": (0.3, 0.15, 0.8),
}

# Normative sentences for ARM H
NORMATIVE_SENTENCES = {
    "exploration": "exploration: educate browsers with broad-reach content on search.",
    "consideration": "consideration: help comparers evaluate options on social channels.",
    "decision": "decision: push promotional offers to ready buyers on search.",
    "crisis": "crisis: pause spending and respond defensively on social.",
    "opportunity": "opportunity: act urgently to capture the window on display.",
    "retention": "retention: nurture loyalty on cheap email channels.",
}

# Action/channel/bid menus for ARM H
ACTION_MENU = ["educational", "comparison", "promotional", "crisis_response", "urgent", "loyalty"]
CHANNEL_MENU = ["search", "social", "display", "email", "video"]
BID_MENU = [0.3, 0.5, 0.7, 1.0, 1.4]


def variant_tag(system_prompt: str, arm_name: str) -> str:
    """First 16 hex chars of sha256(system_prompt + '::' + arm_name)."""
    return hashlib.sha256((system_prompt + "::" + arm_name).encode()).hexdigest()[:16]


def cache_key(variant_tag_str: str, model_key: str, user_text: str) -> str:
    """sha256(variant_tag + '||' + model_key + '||' + user_text)."""
    return hashlib.sha256((variant_tag_str + "||" + model_key + "||" + user_text).encode()).hexdigest()


def load_cache() -> Dict[str, dict]:
    """Load JSONL cache; entries with null label are retried on reload."""
    cache = {}
    if ARMS_CACHE.exists():
        with open(ARMS_CACHE, encoding="utf-8") as f:
            for line in f:
                rec = json.loads(line.strip())
                if rec.get("label") is not None:
                    cache[rec["key"]] = rec
    return cache


def save_cache_entry(entry: dict):
    """Append one entry to JSONL cache and flush."""
    ARMS_CACHE.parent.mkdir(parents=True, exist_ok=True)
    with open(ARMS_CACHE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")
        f.flush()


def classify_variant(system_prompt: str, user_text: str, model_key: str, arm_name: str,
                     cache: Dict[str, dict], temperature: float = 0) -> Tuple[Optional[str], int, int, float]:
    """Classify with variant-aware cache. Returns (label, prompt_tokens, completion_tokens, latency)."""
    vt = variant_tag(system_prompt, arm_name)
    key = cache_key(vt, model_key, user_text)
    if key in cache:
        rec = cache[key]
        return rec["label"], rec.get("prompt_tokens", 0), rec.get("completion_tokens", 0), rec.get("latency_s", 0.0)
    prov = PROVIDERS.get(model_key)
    if not prov:
        raise ValueError(f"Unknown model: {model_key}")
    last_error = None
    for attempt in range(5):
        try:
            body = {"model": prov["model"], "temperature": temperature,
                    "max_tokens": prov.get("max_tokens", 16),
                    "messages": [{"role": "system", "content": system_prompt},
                                 {"role": "user", "content": user_text}]}
            body.update(prov.get("extra_params", {}))
            payload = json.dumps(body)
            if prov.get("transport") == "curl":
                import subprocess
                cmd = ["curl", "-s", "--max-time", str(prov.get("timeout", 30)),
                       "-X", "POST", prov["base"].rstrip("/") + "/chat/completions",
                       "-H", "Authorization: Bearer " + os.environ[prov["key_env"]],
                       "-H", "Content-Type: application/json",
                       "-H", "User-Agent: cam-sim-benchmark/1.6", "--data", "@-"]
                res = subprocess.run(cmd, input=payload.encode(), capture_output=True)
                if res.returncode == 28:
                    raise RuntimeError("curl timeout")
                if res.returncode != 0:
                    raise RuntimeError(f"curl exit {res.returncode}")
                out = json.loads(res.stdout.decode())
            else:
                req = urllib.request.Request(
                    prov["base"].rstrip("/") + "/chat/completions",
                    data=payload.encode(),
                    headers={"Authorization": "Bearer " + os.environ[prov["key_env"]],
                             "Content-Type": "application/json",
                             "User-Agent": "cam-sim-benchmark/1.6"})
                with urllib.request.urlopen(req, timeout=120) as r:
                    out = json.loads(r.read().decode())
            if "error" in out:
                err = out["error"]
                code = err.get("status") or (429 if "rate" in str(err).lower() else 500)
                raise urllib.error.HTTPError(prov["base"], code, json.dumps(err)[:200], None, None)
            msg = out.get("choices", [{}])[0].get("message", {})
            content = msg.get("content", "")
            label, invalid = parse_label(content)
            usage = out.get("usage", {}) or {}
            pt, ct = usage.get("prompt_tokens", 0), usage.get("completion_tokens", 0)
            if label is not None:
                entry = {"key": key, "label": label, "latency_s": 0.0,
                         "prompt_tokens": pt, "completion_tokens": ct, "error": None}
                save_cache_entry(entry)
                return label, pt, ct, 0.0
            last_error = "unparseable: " + repr(content)[:80]
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and attempt < 4:
                time.sleep([2, 4, 8, 16][attempt])
                continue
            last_error = f"http {e.code}"
            break
        except Exception as e:
            if attempt < 4:
                time.sleep(2 * (attempt + 1))
                continue
            last_error = type(e).__name__
            break
    entry = {"key": key, "label": None, "latency_s": 0.0, "prompt_tokens": 0, "completion_tokens": 0, "error": last_error}
    save_cache_entry(entry)
    return None, 0, 0, 0.0


def classify_batch_variant(system_prompt: str, contexts: List, model_key: str, arm_name: str,
                           max_passes: int = 8) -> Dict[str, Any]:
    """Classify all contexts with multi-pass loop until no missing or max_passes."""
    cache = load_cache()
    t0 = time.time()
    ptoks, ctoks, n_failed = 0, 0, 0
    for passage in range(max_passes):
        missing = [(c, textualize(c)) for c in contexts
                   if cache_key(variant_tag(system_prompt, arm_name), model_key, textualize(c)) not in cache]
        if not missing:
            break
        print(f"  Pass {passage + 1}: {len(missing)} missing", flush=True)
        for ctx, user in missing:
            label, pt, ct, _ = classify_variant(system_prompt, user, model_key, arm_name, cache)
            if label is not None:
                ptoks += pt
                ctoks += ct
            else:
                n_failed += 1
        cache = load_cache()
    labels = {}
    invalid = 0
    for c in contexts:
        key = cache_key(variant_tag(system_prompt, arm_name), model_key, textualize(c))
        lab = cache.get(key, {}).get("label")
        labels[key] = lab
        if lab is None:
            invalid += 1
    return {"labels": labels, "invalid": invalid, "failed_calls": n_failed,
            "n": len(contexts), "wall_s": round(time.time() - t0, 1),
            "prompt_tokens": ptoks, "completion_tokens": ctoks}


def bootstrap_ci(values: List[float], n_reps: int = 10000, seed: int = 20261103) -> Tuple[float, float, float]:
    """Seed-level cluster bootstrap: resample seeds with replacement, 95% CI."""
    rng = np.random.RandomState(seed)
    arr = np.array(values)
    n = len(arr)
    if n < 2:
        return float(np.mean(arr)), float(np.mean(arr)), float(np.mean(arr))
    means = []
    for _ in range(n_reps):
        idx = rng.randint(0, n, size=n)
        means.append(np.mean(arr[idx]))
    means = np.array(means)
    lo, hi = np.percentile(means, [2.5, 97.5])
    return float(np.mean(arr)), float(lo), float(hi)


def bootstrap_diff_ci(values_a: List[float], values_b: List[float], n_reps: int = 10000,
                      seed: int = 20261103) -> Tuple[float, float, float]:
    """Bootstrap CI for mean(b) - mean(a)."""
    rng = np.random.RandomState(seed)
    n = len(values_a)
    if n < 2:
        return float(np.mean(values_b) - np.mean(values_a)), 0.0, 0.0
    diffs = []
    for _ in range(n_reps):
        idx = rng.randint(0, n, size=n)
        diffs.append(np.mean(np.array(values_b)[idx]) - np.mean(np.array(values_a)[idx]))
    diffs = np.array(diffs)
    lo, hi = np.percentile(diffs, [2.5, 97.5])
    return float(np.mean(values_b) - np.mean(values_a)), float(lo), float(hi)


def majority_vote(labels_list: List[List[str]]) -> str:
    """Majority vote with ties broken by LABEL_ORDER."""
    counts = Counter(labels_list)
    max_count = max(counts.values())
    tied = [l for l, c in counts.items() if c == max_count]
    return min(tied, key=lambda x: LABEL_ORDER.get(x, 999))


def run_arm_a(max_passes: int) -> Dict[str, Any]:
    """ARM A: order-permutation — 6 permutations of class-definition blocks."""
    # Extract the six class-definition blocks from v15 SYSTEM_PROMPT
    base_blocks = [
        "- exploration: early-funnel discovery; consumers browse casually with little purchase intent.",
        "- consideration: mid-funnel evaluation; consumers actively compare options and features.",
        "- decision: bottom-funnel purchase readiness; consumers intend to buy imminently.",
        "- retention: existing-customer care; the goal is strengthening loyalty and reducing churn.",
        "- crisis: a reputation emergency; negative publicity threatens the brand and demands rapid response.",
        "- opportunity: a favorable window; conditions allow an unusually effective push for the brand.",
    ]
    model_key = "tud/mistral-medium-3.5-128b"
    seed = 1
    random.seed(seed)
    env = SimulationEnvironment(seed=seed, config=None)
    contexts = [env.generate_context() for _ in range(N_SCEN)]
    results = {"arm": "A", "name": "order-permutation", "permutations": []}
    for perm in itertools.permutations(range(6)):
        blocks = [base_blocks[i] for i in perm]
        system_prompt = """You classify a digital-marketing moment into exactly one of six marketing situations:

""" + "\n".join(blocks) + """

You will receive one observation with numeric scales (0 to 1). Respond with exactly one word — the situation label — and nothing else."""
        res = classify_batch_variant(system_prompt, contexts, model_key, "arm_a_perm_" + "".join(map(str, perm)), max_passes)
        preds = [res["labels"].get(cache_key(variant_tag(system_prompt, "arm_a_perm_" + "".join(map(str, perm))), model_key, textualize(c))) for c in contexts]
        acc = 100.0 * sum(1 for p, c in zip(preds, contexts) if p == c.situation.value) / N_SCEN
        conf = confusion(preds, [c.situation.value for c in contexts])
        results["permutations"].append({
            "order": list(perm), "accuracy": round(acc, 1), "confusion": conf,
            "invalid": res["invalid"], "failed_calls": res["failed_calls"]})
    return results


def run_arm_b(max_passes: int, models: List[str]) -> Dict[str, Any]:
    """ARM B: minimal-labels — system prompt reduced to labels only."""
    system_prompt = """You classify a digital-marketing moment into exactly one of six marketing situations. Respond with exactly one word — the situation label — and nothing else. The six situations are: exploration, consideration, decision, crisis, opportunity, retention."""
    seed = 1
    random.seed(seed)
    env = SimulationEnvironment(seed=seed, config=None)
    contexts = [env.generate_context() for _ in range(N_SCEN)]
    results = {"arm": "B", "name": "minimal-labels", "models": {}}
    for model_key in models:
        res = classify_batch_variant(system_prompt, contexts, model_key, "arm_b", max_passes)
        preds = [res["labels"].get(cache_key(variant_tag(system_prompt, "arm_b"), model_key, textualize(c))) for c in contexts]
        acc = 100.0 * sum(1 for p, c in zip(preds, contexts) if p == c.situation.value) / N_SCEN
        conf = confusion(preds, [c.situation.value for c in contexts])
        results["models"][model_key] = {
            "accuracy": round(acc, 1), "confusion": conf, "invalid": res["invalid"],
            "failed_calls": res["failed_calls"]}
    return results


def run_arm_c(max_passes: int, models: List[str]) -> Dict[str, Any]:
    """ARM C: counterfactual-archetypes — 42 probes at canonical centroids."""
    system_prompt = """You classify a digital-marketing moment into exactly one of six marketing situations:

- exploration: early-funnel discovery; consumers browse casually with little purchase intent.
- consideration: mid-funnel evaluation; consumers actively compare options and features.
- decision: bottom-funnel purchase readiness; consumers intend to buy imminently.
- retention: existing-customer care; the goal is strengthening loyalty and reducing churn.
- crisis: a reputation emergency; negative publicity threatens the brand and demands rapid response.
- opportunity: a favorable window; conditions allow an unusually effective push for the brand.

You will receive one observation with numeric scales (0 to 1). Respond with exactly one word — the situation label — and nothing else."""
    probes = []
    for arch, (intent, comp, qual) in ARCHETYPES.items():
        variants = [(intent, comp, qual)]
        for delta in [+0.15, -0.15]:
            variants.append((min(1.0, intent + delta), comp, qual))
            variants.append((intent, min(1.0, comp + delta), qual))
            variants.append((intent, comp, min(1.0, qual + delta)))
        for i, (i_, c_, q_) in enumerate(variants[:7]):
            probes.append((arch, i_, c_, q_))
    results = {"arm": "C", "name": "counterfactual-archetypes", "models": {}, "crisis_or_retention": False}
    for model_key in models:
        model_res = {"archetypes": {}}
        for arch, intent, comp, qual in probes:
            user = f"Observation:\n- audience_intent_strength: {intent:.3f}\n- competitive_density: {comp:.3f}\n- channel_quality: {qual:.3f}\n- signals: intent_strength={intent}; quality_score=0.72; time_of_day=morning; device_type=mobile"
            label, _, _, _ = classify_variant(system_prompt, user, model_key, f"arm_c_{arch}_{intent}_{comp}_{qual}", {}, max_passes=1)
            if label in ("crisis", "retention"):
                results["crisis_or_retention"] = True
            key = arch
            if key not in model_res["archetypes"]:
                model_res["archetypes"][key] = Counter()
            model_res["archetypes"][key][label] += 1
        results["models"][model_key] = model_res
    return results


def run_arm_d(max_passes: int) -> Dict[str, Any]:
    """ARM D: decoy-removal — omit quality_score from signals."""
    system_prompt = """You classify a digital-marketing moment into exactly one of six marketing situations:

- exploration: early-funnel discovery; consumers browse casually with little purchase intent.
- consideration: mid-funnel evaluation; consumers actively compare options and features.
- decision: bottom-funnel purchase readiness; consumers intend to buy imminently.
- retention: existing-customer care; the goal is strengthening loyalty and reducing churn.
- crisis: a reputation emergency; negative publicity threatens the brand and demands rapid response.
- opportunity: a favorable window; conditions allow an unusually effective push for the brand.

You will receive one observation with numeric scales (0 to 1). Respond with exactly one word — the situation label — and nothing else."""
    model_key = "tud/mistral-medium-3.5-128b"
    seed = 1
    random.seed(seed)
    env = SimulationEnvironment(seed=seed, config=None)
    contexts = [env.generate_context() for _ in range(N_SCEN)]
    # Custom textualize without quality_score
    def textualize_no_decoy(ctx):
        sigs = "; ".join(f"{s.name}={s.value}" for s in ctx.signals if s.name != "quality_score")
        return f"""Observation:
- audience_intent_strength: {ctx.audience_intent_strength:.3f} (0 = none, 1 = maximum purchase intent)
- competitive_density: {ctx.competitive_density:.3f} (0 = empty field, 1 = saturated with competitor activity)
- channel_quality: {ctx.channel_quality:.3f} (0 = unusable, 1 = excellent delivery conditions)
- signals: {sigs}

Situation label (one word):"""
    # Classify with modified user text
    cache = load_cache()
    for c in contexts:
        user = textualize_no_decoy(c)
        vt = variant_tag(system_prompt, "arm_d")
        key = cache_key(vt, model_key, user)
        if key not in cache:
            classify_variant(system_prompt, user, model_key, "arm_d", cache)
    cache = load_cache()
    res = {"invalid": 0, "failed_calls": 0, "n": N_SCEN}
    preds = []
    for c in contexts:
        user = textualize_no_decoy(c)
        key = cache_key(variant_tag(system_prompt, "arm_d"), model_key, user)
        lab = cache.get(key, {}).get("label")
        preds.append(lab)
        if lab is None:
            res["invalid"] += 1
    acc = 100.0 * sum(1 for p, c in zip(preds, contexts) if p == c.situation.value) / N_SCEN
    # Compare to v15 cache (with decoy)
    v15_cache_path = CACHE_DIR / "tud__mistral-medium-3-5-128b.jsonl"
    v15_acc = None
    if v15_cache_path.exists():
        v15_cache = {}
        with open(v15_cache_path, encoding="utf-8") as f:
            for line in f:
                rec = json.loads(line)
                if rec.get("label"):
                    v15_cache[rec["key"]] = rec["label"]
        # Re-key v15 cache by context
        from cam_sim_v15_llm import context_key as v15_context_key
        v15_preds = []
        for c in contexts:
            key = v15_context_key(model_key, c)
            v15_preds.append(v15_cache.get(key))
        v15_acc = 100.0 * sum(1 for p, c in zip(v15_preds, contexts) if p == c.situation.value) / N_SCEN
    results = {"arm": "D", "name": "decoy-removal", "accuracy": round(acc, 1),
               "v15_accuracy": round(v15_acc, 1) if v15_acc else None,
               "delta": round(acc - v15_acc, 1) if v15_acc else None,
               "invalid": res["invalid"], "failed_calls": res["failed_calls"]}
    return results


def run_arm_e(max_passes: int, models: List[str], seeds: List[int]) -> Dict[str, Any]:
    """ARM E: qualitative-hints — v15 prompt plus two hint sentences."""
    base_prompt = """You classify a digital-marketing moment into exactly one of six marketing situations:

- exploration: early-funnel discovery; consumers browse casually with little purchase intent.
- consideration: mid-funnel evaluation; consumers actively compare options and features.
- decision: bottom-funnel purchase readiness; consumers intend to buy imminently.
- retention: existing-customer care; the goal is strengthening loyalty and reducing churn.
- crisis: a reputation emergency; negative publicity threatens the brand and demands rapid response.
- opportunity: a favorable window; conditions allow an unusually effective push for the brand.

You will receive one observation with numeric scales (0 to 1). Respond with exactly one word — the situation label — and nothing else."""
    hints = """

Note: crisis combines high purchase intent with intense competitor activity and notably LOW channel quality.
Note: retention is an existing-customer moment with low intent and notably LOW competitive density."""
    system_prompt = base_prompt + hints
    results = {"arm": "E", "name": "qualitative-hints", "models": {}}
    # Get reference profits for contrasts
    refs = build_reference_agents()
    ref_per_seed, ref_per_scen = walk_with_scenarios(refs, seeds, N_SCEN)
    for model_key in models:
        all_preds, all_truths, per_seed_profit, per_seed_scen = [], [], [], {}
        for seed in seeds:
            random.seed(seed)
            env = SimulationEnvironment(seed=seed, config=None)
            contexts = [env.generate_context() for _ in range(N_SCEN)]
            res = classify_batch_variant(system_prompt, contexts, model_key, f"arm_e_{seed}", max_passes)
            for c in contexts:
                key = cache_key(variant_tag(system_prompt, f"arm_e_{seed}"), model_key, textualize(c))
                lab = res["labels"].get(key)
                all_preds.append(lab if lab else "consideration")
                all_truths.append(c.situation.value)
            # Evaluate profit
            eval_env = SimulationEnvironment(seed=seed, config=None)
            oracle = CAMOracle("oracle_ref")
            totals = []
            for c in contexts:
                key = cache_key(variant_tag(system_prompt, f"arm_e_{seed}"), model_key, textualize(c))
                lab = res["labels"].get(key)
                sit = SituationType(lab if lab else "consideration")
                action = Action(0, IDEAL_ACTION[sit], SITUATION_CHANNEL[sit], round(oracle._bid(sit, c), 2))
                r = eval_env.evaluate_action(c, action)
                totals.append(r.reward + r.long_term_value - r.cost)
            per_seed_profit.append(sum(totals))
            per_seed_scen[seed] = totals
        acc = 100.0 * sum(1 for p, t in zip(all_preds, all_truths) if p == t) / len(all_truths)
        # Per-class recalls
        class_preds = {l: [] for l in LABELS}
        class_truths = {l: [] for l in LABELS}
        for p, t in zip(all_preds, all_truths):
            class_truths[t].append(t)
            class_preds[t].append(p)
        recalls = {l: 100.0 * sum(1 for p, t in zip(class_preds[l], class_truths[l]) if p == t) / max(len(class_truths[l]), 1) for l in LABELS}
        macro_recall = np.mean(list(recalls.values()))
        crisis_recall = recalls.get("crisis", 0)
        retention_recall = recalls.get("retention", 0)
        # Bootstrap CIs
        profit_mean, profit_lo, profit_hi = bootstrap_ci(per_seed_profit)
        # Contrasts vs references
        contrasts = {}
        for ref in refs:
            if ref.name in ("cam_inferred", "cam_multisignal"):
                ref_profits = ref_per_seed[ref.name]
                diff, diff_lo, diff_hi = bootstrap_diff_ci(ref_profits, per_seed_profit)
                contrasts[ref.name] = {"diff": round(diff, 2), "ci95": [round(diff_lo, 2), round(diff_hi, 2)]}
        results["models"][model_key] = {
            "accuracy": round(acc, 1), "macro_recall": round(macro_recall, 1),
            "crisis_recall": round(crisis_recall, 1), "retention_recall": round(retention_recall, 1),
            "profit_mean": round(profit_mean, 2), "profit_ci95": [round(profit_lo, 2), round(profit_hi, 2)],
            "contrasts": contrasts, "per_seed_profit": [round(p, 2) for p in per_seed_profit]}
    return results


def run_arm_f(max_passes: int, models: List[str], seeds: List[int]) -> Dict[str, Any]:
    """ARM F: few-shot — v15 prompt plus six exemplar lines."""
    base_prompt = """You classify a digital-marketing moment into exactly one of six marketing situations:

- exploration: early-funnel discovery; consumers browse casually with little purchase intent.
- consideration: mid-funnel evaluation; consumers actively compare options and features.
- decision: bottom-funnel purchase readiness; consumers intend to buy imminently.
- retention: existing-customer care; the goal is strengthening loyalty and reducing churn.
- crisis: a reputation emergency; negative publicity threatens the brand and demands rapid response.
- opportunity: a favorable window; conditions allow an unusually effective push for the brand.

Examples:
Example exploration: intent 0.18, competition 0.55, quality 0.66.
Example consideration: intent 0.47, competition 0.50, quality 0.72.
Example decision: intent 0.86, competition 0.46, quality 0.75.
Example crisis: intent 0.78, competition 0.88, quality 0.24.
Example opportunity: intent 0.55, competition 0.82, quality 0.61.
Example retention: intent 0.27, competition 0.17, quality 0.79.

You will receive one observation with numeric scales (0 to 1). Respond with exactly one word — the situation label — and nothing else."""
    results = {"arm": "F", "name": "few-shot", "models": {}}
    refs = build_reference_agents()
    ref_per_seed, _ = walk_with_scenarios(refs, seeds, N_SCEN)
    for model_key in models:
        all_preds, all_truths, per_seed_profit = [], [], []
        for seed in seeds:
            random.seed(seed)
            env = SimulationEnvironment(seed=seed, config=None)
            contexts = [env.generate_context() for _ in range(N_SCEN)]
            res = classify_batch_variant(base_prompt, contexts, model_key, f"arm_f_{seed}", max_passes)
            for c in contexts:
                key = cache_key(variant_tag(base_prompt, f"arm_f_{seed}"), model_key, textualize(c))
                lab = res["labels"].get(key)
                all_preds.append(lab if lab else "consideration")
                all_truths.append(c.situation.value)
            eval_env = SimulationEnvironment(seed=seed, config=None)
            oracle = CAMOracle("oracle_ref")
            totals = []
            for c in contexts:
                key = cache_key(variant_tag(base_prompt, f"arm_f_{seed}"), model_key, textualize(c))
                lab = res["labels"].get(key)
                sit = SituationType(lab if lab else "consideration")
                action = Action(0, IDEAL_ACTION[sit], SITUATION_CHANNEL[sit], round(oracle._bid(sit, c), 2))
                r = eval_env.evaluate_action(c, action)
                totals.append(r.reward + r.long_term_value - r.cost)
            per_seed_profit.append(sum(totals))
        acc = 100.0 * sum(1 for p, t in zip(all_preds, all_truths) if p == t) / len(all_truths)
        class_preds = {l: [] for l in LABELS}
        class_truths = {l: [] for l in LABELS}
        for p, t in zip(all_preds, all_truths):
            class_truths[t].append(t)
            class_preds[t].append(p)
        recalls = {l: 100.0 * sum(1 for p, t in zip(class_preds[l], class_truths[l]) if p == t) / max(len(class_truths[l]), 1) for l in LABELS}
        macro_recall = np.mean(list(recalls.values()))
        profit_mean, profit_lo, profit_hi = bootstrap_ci(per_seed_profit)
        contrasts = {}
        for ref in refs:
            if ref.name in ("cam_inferred", "cam_multisignal"):
                ref_profits = ref_per_seed[ref.name]
                diff, diff_lo, diff_hi = bootstrap_diff_ci(ref_profits, per_seed_profit)
                contrasts[ref.name] = {"diff": round(diff, 2), "ci95": [round(diff_lo, 2), round(diff_hi, 2)]}
        results["models"][model_key] = {
            "accuracy": round(acc, 1), "macro_recall": round(macro_recall, 1),
            "profit_mean": round(profit_mean, 2), "profit_ci95": [round(profit_lo, 2), round(profit_hi, 2)],
            "contrasts": contrasts, "per_seed_profit": [round(p, 2) for p in per_seed_profit]}
    return results


def run_arm_g(max_passes: int, models: List[str], seeds: List[int]) -> Dict[str, Any]:
    """ARM G: self-consistency — k=5 samples at temperature 0.7, majority vote."""
    system_prompt = """You classify a digital-marketing moment into exactly one of six marketing situations:

- exploration: early-funnel discovery; consumers browse casually with little purchase intent.
- consideration: mid-funnel evaluation; consumers actively compare options and features.
- decision: bottom-funnel purchase readiness; consumers intend to buy imminently.
- retention: existing-customer care; the goal is strengthening loyalty and reducing churn.
- crisis: a reputation emergency; negative publicity threatens the brand and demands rapid response.
- opportunity: a favorable window; conditions allow an unusually effective push for the brand.

You will receive one observation with numeric scales (0 to 1). Respond with exactly one word — the situation label — and nothing else."""
    results = {"arm": "G", "name": "self-consistency", "models": {}}
    # Get zero-shot recalls from v15 cache for comparison
    v15_cache_path = CACHE_DIR / "tud__mistral-medium-3-5-128b.jsonl"
    v15_zai_cache = CACHE_DIR / "zai__glm-4-7.jsonl"
    for model_key in models:
        crisis_correct, crisis_total = 0, 0
        retention_correct, retention_total = 0, 0
        for seed in seeds:
            random.seed(seed)
            env = SimulationEnvironment(seed=seed, config=None)
            contexts = [env.generate_context() for _ in range(N_SCEN)]
            for c in contexts:
                if c.situation.value not in ("crisis", "retention"):
                    continue
                # k=5 samples
                samples = []
                for k in range(5):
                    user = textualize(c)
                    vt = variant_tag(system_prompt, f"arm_g_{seed}_{c.context_id}_{k}")
                    key = cache_key(vt, model_key, user)
                    # Load from cache or classify
                    cache = load_cache()
                    if key in cache:
                        lab = cache[key].get("label")
                    else:
                        lab, _, _, _ = classify_variant(system_prompt, user, model_key, f"arm_g_{seed}_{c.context_id}_{k}", {}, temperature=0.7)
                    if lab:
                        samples.append(lab)
                if len(samples) < 3:
                    continue
                vote = majority_vote(samples)
                if c.situation.value == "crisis":
                    crisis_total += 1
                    if vote == "crisis":
                        crisis_correct += 1
                elif c.situation.value == "retention":
                    retention_total += 1
                    if vote == "retention":
                        retention_correct += 1
        crisis_recall = 100.0 * crisis_correct / max(crisis_total, 1)
        retention_recall = 100.0 * retention_correct / max(retention_total, 1)
        # Zero-shot baseline from v15 cache
        v15_path = CACHE_DIR / (model_key.replace("/", "__") + ".jsonl")
        v15_crisis_correct, v15_crisis_total = 0, 0
        v15_retention_correct, v15_retention_total = 0, 0
        if v15_path.exists():
            v15_cache = {}
            with open(v15_path, encoding="utf-8") as f:
                for line in f:
                    rec = json.loads(line)
                    if rec.get("label"):
                        v15_cache[rec["key"]] = rec["label"]
            from cam_sim_v15_llm import context_key as v15_context_key
            for seed in seeds:
                random.seed(seed)
                env = SimulationEnvironment(seed=seed, config=None)
                contexts = [env.generate_context() for _ in range(N_SCEN)]
                for c in contexts:
                    if c.situation.value not in ("crisis", "retention"):
                        continue
                    key = v15_context_key(model_key, c)
                    lab = v15_cache.get(key)
                    if lab is None:
                        continue
                    if c.situation.value == "crisis":
                        v15_crisis_total += 1
                        if lab == "crisis":
                            v15_crisis_correct += 1
                    elif c.situation.value == "retention":
                        v15_retention_total += 1
                        if lab == "retention":
                            v15_retention_correct += 1
        results["models"][model_key] = {
            "crisis_recall_sc": round(crisis_recall, 1), "crisis_total": crisis_total,
            "retention_recall_sc": round(retention_recall, 1), "retention_total": retention_total,
            "crisis_recall_zeroshot": round(100.0 * v15_crisis_correct / max(v15_crisis_total, 1), 1) if v15_crisis_total else None,
            "retention_recall_zeroshot": round(100.0 * v15_retention_correct / max(v15_retention_total, 1), 1) if v15_retention_total else None}
    return results


def run_arm_h(max_passes: int, models: List[str], seeds: List[int]) -> Dict[str, Any]:
    """ARM H: end-to-end — LLM outputs full action line."""
    system_prompt = """You choose a marketing action given an observation. Respond with exactly one line in this format:
situation; action; channel; bid

Menus:
- situation: exploration, consideration, decision, crisis, opportunity, retention
- action: educational, comparison, promotional, crisis_response, urgent, loyalty
- channel: search, social, display, email, video
- bid: 0.3, 0.5, 0.7, 1.0, 1.4

Normative guidance:
exploration: educate browsers with broad-reach content on search.
consideration: help comparers evaluate options on social channels.
decision: push promotional offers to ready buyers on search.
crisis: pause spending and respond defensively on social.
opportunity: act urgently to capture the window on display.
retention: nurture loyalty on cheap email channels.

Respond with exactly one line: situation; action; channel; bid"""
    results = {"arm": "H", "name": "end-to-end", "models": {}}
    refs = build_reference_agents()
    ref_per_seed, ref_per_scen = walk_with_scenarios(refs, seeds, N_SCEN)
    for model_key in models:
        per_seed_profit, per_seed_match, invalid_counts = [], [], []
        action_dist, channel_dist, bid_dist = Counter(), Counter(), Counter()
        match_ideal = 0
        total_scenarios = 0
        for seed in seeds:
            random.seed(seed)
            env = SimulationEnvironment(seed=seed, config=None)
            contexts = [env.generate_context() for _ in range(N_SCEN)]
            seed_invalid = 0
            seed_profit, seed_match = 0.0, 0
            eval_env = SimulationEnvironment(seed=seed, config=None)
            for c in contexts:
                user = textualize(c)
                vt = variant_tag(system_prompt, f"arm_h_{seed}")
                key = cache_key(vt, model_key, user)
                cache = load_cache()
                if key in cache:
                    content = cache[key].get("content")
                else:
                    # Classify
                    prov = PROVIDERS.get(model_key)
                    if prov:
                        body = {"model": prov["model"], "temperature": 0,
                                "max_tokens": 64,
                                "messages": [{"role": "system", "content": system_prompt},
                                             {"role": "user", "content": user}]}
                        body.update(prov.get("extra_params", {}))
                        payload = json.dumps(body)
                        try:
                            if prov.get("transport") == "curl":
                                import subprocess
                                cmd = ["curl", "-s", "--max-time", str(prov.get("timeout", 30)),
                                       "-X", "POST", prov["base"].rstrip("/") + "/chat/completions",
                                       "-H", "Authorization: Bearer " + os.environ.get(prov["key_env"], ""),
                                       "-H", "Content-Type: application/json", "--data", "@-"]
                                res = subprocess.run(cmd, input=payload.encode(), capture_output=True)
                                if res.returncode == 0:
                                    out = json.loads(res.stdout.decode())
                                    content = out.get("choices", [{}])[0].get("message", {}).get("content", "")
                                else:
                                    content = None
                            else:
                                req = urllib.request.Request(
                                    prov["base"].rstrip("/") + "/chat/completions",
                                    data=payload.encode(),
                                    headers={"Authorization": "Bearer " + os.environ.get(prov["key_env"], ""),
                                             "Content-Type": "application/json"})
                                with urllib.request.urlopen(req, timeout=30) as r:
                                    out = json.loads(r.read().decode())
                                    content = out.get("choices", [{}])[0].get("message", {}).get("content", "")
                        except Exception:
                            content = None
                    else:
                        content = None
                    if content:
                        save_cache_entry({"key": key, "content": content, "label": None})
                # Parse response
                action = None
                if content:
                    parts = [p.strip() for p in (content or "").split(";")]
                    if len(parts) == 4:
                        sit_str, act_str, ch_str, bid_str = parts
                        try:
                            sit = SituationType(sit_str.lower())
                            act = ActionType(act_str.lower())
                            ch = ChannelType(ch_str.lower())
                            bid = float(bid_str)
                            if bid in BID_MENU:
                                action = Action(0, act, ch, bid)
                        except (ValueError, KeyError):
                            pass
                if action is None:
                    action = Action(0, ActionType.EDUCATIONAL, list(ChannelType)[0], 1.0)
                    seed_invalid += 1
                else:
                    action_dist[action.action_type.value] += 1
                    channel_dist[action.channel.value] += 1
                    bid_dist[action.bid] += 1
                    # Check match against IDEAL_ACTION
                    if action.action_type == IDEAL_ACTION[c.situation]:
                        match_ideal += 1
                r = eval_env.evaluate_action(c, action)
                seed_profit += r.reward + r.long_term_value - r.cost
                if r.context_match:
                    seed_match += 1
                total_scenarios += 1
            per_seed_profit.append(seed_profit)
            per_seed_match.append(100.0 * seed_match / N_SCEN)
            invalid_counts.append(seed_invalid)
        profit_mean = float(np.mean(per_seed_profit))
        profit_std = float(np.std(per_seed_profit, ddof=1))
        profit_mean_bs, profit_lo, profit_hi = bootstrap_ci(per_seed_profit)
        match_rate = 100.0 * match_ideal / max(total_scenarios, 1)
        contrasts = {}
        for ref in refs:
            if ref.name in ("cam_inferred", "cam_multisignal", "oracle"):
                ref_profits = ref_per_seed[ref.name]
                diff, diff_lo, diff_hi = bootstrap_diff_ci(ref_profits, per_seed_profit)
                contrasts[ref.name] = {"diff": round(diff, 2), "ci95": [round(diff_lo, 2), round(diff_hi, 2)]}
        results["models"][model_key] = {
            "profit_mean": round(profit_mean, 2), "profit_std": round(profit_std, 2),
            "profit_ci95": [round(profit_lo, 2), round(profit_hi, 2)],
            "match_rate_ideal": round(match_rate, 1),
            "invalid_total": sum(invalid_counts),
            "action_dist": dict(action_dist), "channel_dist": dict(channel_dist),
            "bid_dist": {str(k): v for k, v in bid_dist.items()},
            "contrasts": contrasts, "per_seed_profit": [round(p, 2) for p in per_seed_profit]}
    return results


def run_selftest():
    """Run fully offline selftest with deterministic stub."""
    print("Running selftest...", flush=True)
    # Monkeypatch classify_with_retry
    original_classify = None
    try:
        from cam_sim_v15_llm import classify_with_retry as original_classify
    except ImportError:
        pass

    def stub_classify(prov, system, user):
        label = hashlib.sha256(user.encode()).hexdigest()[:8]
        idx = int(label, 16) % len(LABELS)
        return LABELS[idx], 100, 10

    import cam_sim_v15_llm
    cam_sim_v15_llm.classify_with_retry = stub_classify

    # Test 1: variant-key stability
    vt1 = variant_tag("prompt1", "arm_a")
    vt2 = variant_tag("prompt1", "arm_a")
    vt3 = variant_tag("prompt1", "arm_b")
    assert vt1 == vt2, "variant_tag not stable"
    assert vt1 != vt3, "different arm name should give different key"
    k1 = cache_key(vt1, "model1", "user1")
    k2 = cache_key(vt1, "model1", "user1")
    k3 = cache_key(vt1, "model2", "user1")
    assert k1 == k2, "cache_key not stable"
    assert k1 != k3, "different model should give different key"
    print("  [OK] variant-key stability", flush=True)

    # Test 2: parse_label
    for label in LABELS:
        parsed, invalid = parse_label(label)
        assert parsed == label and not invalid, f"parse_label failed for {label}"
        parsed, invalid = parse_label(label.upper())
        assert parsed == label and not invalid, f"parse_label failed for {label.upper()}"
    parsed, invalid = parse_label("invalid_label")
    assert parsed is None and invalid, "parse_label should return None for invalid"
    print("  [OK] parse_label", flush=True)

    # Test 3: majority vote tie-breaking
    # LABELS order: exploration(0), consideration(1), decision(2), crisis(3), opportunity(4), retention(5)
    votes1 = ["crisis", "crisis", "decision", "decision", "exploration"]
    result1 = majority_vote(votes1)
    # crisis=2, decision=2 tied; decision has lower LABEL_ORDER (2 < 3)
    assert result1 == "decision", f"majority vote failed: {result1}"
    votes2 = ["crisis", "decision", "exploration", "consideration", "opportunity"]
    result2 = majority_vote(votes2)
    # All tied with count=1; exploration has lowest LABEL_ORDER (0)
    assert result2 == "exploration", f"majority vote tie-break failed: {result2}"
    print("  [OK] majority vote tie-breaking", flush=True)

    # Test 4: bootstrap CI width strictly positive
    values = [1.0, 2.0, 3.0, 4.0, 5.0]
    mean, lo, hi = bootstrap_ci(values, n_reps=1000)
    assert hi > lo, "bootstrap CI should have positive width"
    print("  [OK] bootstrap CI width > 0", flush=True)

    # Test 5: end-to-end Action construction and evaluation
    random.seed(42)
    env = SimulationEnvironment(seed=42, config=None)
    ctx = env.generate_context()
    action = Action(0, ActionType.PROMOTIONAL, ChannelType.SEARCH, 1.0)
    result = env.evaluate_action(ctx, action)
    assert hasattr(result, "profit"), "ActionResult should have profit"
    print("  [OK] Action construction and evaluation", flush=True)

    print("SELFTEST-OK", flush=True)
    return 0


def main():
    parser = argparse.ArgumentParser(description="CAM-Sim v1.6 — Prompt-variant experiment harness")
    parser.add_argument("--arms", type=str, default="A,B,C,D,E,F,G,H",
                        help="Comma-separated subset of arms (default: all)")
    parser.add_argument("--models", type=str, nargs="*", default=None,
                        help="Filter models")
    parser.add_argument("--max-passes", type=int, default=8,
                        help="Max passes for cache retry (default: 8)")
    parser.add_argument("--selftest", action="store_true",
                        help="Run offline selftest")
    parser.add_argument("--seeds", type=str, default="1,2,3,4,5",
                        help="Seeds for arms E,F,G,H (default: 1,2,3,4,5)")
    args = parser.parse_args()

    if args.selftest:
        return run_selftest()

    arms = [a.strip().upper() for a in args.arms.split(",")]
    models = args.models if args.models else list(PROVIDERS.keys())
    seeds = [int(s.strip()) for s in args.seeds.split(",")]

    results = {
        "meta": {
            "date": time.strftime("%Y-%m-%d"),
            "arms": arms,
            "models": models,
            "seeds": seeds,
            "max_passes": args.max_passes,
        }
    }

    for arm in arms:
        print(f"\n=== Running ARM {arm} ===", flush=True)
        if arm == "A":
            results["arm_A"] = run_arm_a(args.max_passes)
        elif arm == "B":
            results["arm_B"] = run_arm_b(args.max_passes, models)
        elif arm == "C":
            results["arm_C"] = run_arm_c(args.max_passes, models)
        elif arm == "D":
            results["arm_D"] = run_arm_d(args.max_passes)
        elif arm == "E":
            results["arm_E"] = run_arm_e(args.max_passes, models, seeds)
        elif arm == "F":
            results["arm_F"] = run_arm_f(args.max_passes, models, seeds)
        elif arm == "G":
            results["arm_G"] = run_arm_g(args.max_passes, models, seeds)
        elif arm == "H":
            results["arm_H"] = run_arm_h(args.max_passes, models, seeds)
        else:
            print(f"  Unknown arm: {arm}", flush=True)

    # Write results
    OUT.mkdir(parents=True, exist_ok=True)
    with open(OUT / "cam_sim_v16.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=1)
    print(f"\nWrote {OUT / 'cam_sim_v16.json'}", flush=True)

    # Print summary table
    print("\n=== Summary ===", flush=True)
    for arm_key in sorted(results.keys()):
        if arm_key.startswith("arm_"):
            arm_data = results[arm_key]
            print(f"{arm_key}: {arm_data.get('name', 'N/A')}", flush=True)
            if "models" in arm_data:
                for mk, md in arm_data["models"].items():
                    if "accuracy" in md:
                        print(f"  {mk}: acc={md['accuracy']}%", flush=True)
                    if "profit_mean" in md:
                        print(f"  {mk}: profit={md['profit_mean']}", flush=True)

    return 0


if __name__ == "__main__":
    sys.exit(main())
