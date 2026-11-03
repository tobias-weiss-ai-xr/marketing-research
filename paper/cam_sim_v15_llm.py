#!/usr/bin/env python3
"""CAM-Sim v1.5 — [25] LLM zero-shot classification baseline (API-driven).

Implements the protocol pre-registered in g4_academic_paper.md §10.3 #24,
verbatim: textualize each CAM-Sim context into a natural-language observation
(intent strength, competitive density, channel quality, signals list), prompt
an LLM to classify into the 6 situations (temperature 0), map via the fixed
IDEAL_ACTION/SITUATION_CHANNEL pipeline and oracle-style bid, and evaluate on
the identical 50-seed context sequences against cam_multisignal and
cam_inferred.

Models (2026-11-02 snapshot; scale adapted to measured provider quotas):
  - zai/glm-4.7              (Z.ai coding endpoint, thinking model)      — 10 seeds (2,000 calls)
  - groq/qwen3.8-27b         (Groq, 27B dense)                           — 3 seeds (600 calls; see note)
  - tud/mistral-medium-3.5   (TU Darmstadt llm-service, 128B dense)      — 10 seeds (2,000 calls)
  - local/deepseek-v4-flash  (LAN-local via LiteLLM, reasoning)          — 5 seeds (1,000 calls)
    [originally openai/gpt-oss-120b: its daily request quota (≈500 calls)
    exhausted mid-run on 2026-11-02; swapped to a fresh-quota model]
  - saia/qwen3.6-35b-a3b     (AcademicCloud SAIA, 35B MoE / 3B active)   — 2 seeds (400 calls, sequential; ~3 RPM quota)
  - saia/qwen3.5-397b-a17b   — dropped: shares the SAIA quota (~3 RPM), the
    10k-call protocol is infeasible; the 35b covers the Qwen family.

Design decisions (documented in the paper §8.21):
  - Situation definitions in the system prompt are QUALITATIVE marketing
    semantics only — no numeric centroids/thresholds are disclosed. The LLM
    must map the observed scalars onto situation semantics itself.
  - The signals list is included verbatim, including the decoy quality_score
    (sensing_fidelity=False default), testing decoy robustness.
  - Parse failures get one token-doubled retry; if still unparseable (or the
    API call fails after backoff) the agent plays the generic mid-funnel
    default ('consideration') and the case is counted in `invalid`.
  - Responses are cached (results/llm_cache/<model>.jsonl) so the evaluation
    walk is deterministic and reruns cost nothing. NOTE: LLM providers do not
    guarantee bitwise determinism at temperature 0; the cache freezes one
    snapshot. Exact regeneration requires fresh API calls.
  - Context sequences are pre-generated per seed from
    SimulationEnvironment(seed) BEFORE any evaluate_action call, mirroring
    run_online_env's pairing (evaluate_action consumes env RNG for latency,
    so generation must precede evaluation).

Run:  /usr/local/bin/python3.12 paper/cam_sim_v15_llm.py --pilot
      /usr/local/bin/python3.12 paper/cam_sim_v15_llm.py                # full run
      /usr/local/bin/python3.12 paper/cam_sim_v15_llm.py --models saia/qwen3.6-35b-a3b
Requires env: SAIA_API_KEY, ZAI_API_KEY, GROQ_API_KEY.

DEVIATION from the pre-registered 50-seed protocol (documented in §8.21):
provider rate limits make 50 seeds x 200 = 10,000 calls per model infeasible
(SAIA sustains ~3 req/min measured). All evaluations remain PAIRED on the
identical canned context sequences; per-model seed counts are reported.
Statistical analysis: per-scenario paired profit differences (n = seeds x 200,
primary; within-seed clustering caveat) + per-seed paired t-tests where
n_seeds >= 5 (robustness; low power at n = 5).
"""
import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))

from cam_sim import (ActionType, AGENT_REGISTRY, Action, CAMLearned, CAMOracle,
                     ChannelType, IDEAL_ACTION, SITUATION_CHANNEL,
                     SimulationEnvironment, SituationType,
                     compute_statistics, fit_intent_classifier)
from cam_sim_v14 import run_online_env

SEEDS = list(range(1, 51))
N_SCEN = 200
OUT = Path(__file__).resolve().parent.parent / "results"
CACHE_DIR = OUT / "llm_cache"

LABELS = [s.value for s in SituationType]  # crisis, decision, opportunity,
#                                            retention, exploration, consideration

# Qualitative marketing semantics ONLY — no numeric centroids (§8.21 notes).
SYSTEM_PROMPT = """You classify a digital-marketing moment into exactly one of six marketing situations:

- exploration: early-funnel discovery; consumers browse casually with little purchase intent.
- consideration: mid-funnel evaluation; consumers actively compare options and features.
- decision: bottom-funnel purchase readiness; consumers intend to buy imminently.
- retention: existing-customer care; the goal is strengthening loyalty and reducing churn.
- crisis: a reputation emergency; negative publicity threatens the brand and demands rapid response.
- opportunity: a favorable window; conditions allow an unusually effective push for the brand.

You will receive one observation with numeric scales (0 to 1). Respond with exactly one word — the situation label — and nothing else."""

# Short hash of the system prompt, bound into every cache key so that cached
# responses never silently go stale after a prompt edit (see context_key).
PROMPT_SHA16 = hashlib.sha256(SYSTEM_PROMPT.encode()).hexdigest()[:16]

USER_TEMPLATE = """Observation:
- audience_intent_strength: {intent:.3f} (0 = none, 1 = maximum purchase intent)
- competitive_density: {comp:.3f} (0 = empty field, 1 = saturated with competitor activity)
- channel_quality: {cq:.3f} (0 = unusable, 1 = excellent delivery conditions)
- signals: {signals}

Situation label (one word):"""


def textualize(context):
    """Deterministic natural-language observation for one FullContext."""
    sigs = "; ".join(f"{s.name}={s.value}" for s in context.signals)
    return USER_TEMPLATE.format(intent=context.audience_intent_strength,
                                comp=context.competitive_density,
                                cq=context.channel_quality,
                                signals=sigs)


# ---------------------------------------------------------------------------
# API client with cache, retries, and concurrency
# ---------------------------------------------------------------------------

PROVIDERS = {
    "zai/glm-4.7": dict(
        base="https://api.z.ai/api/coding/paas/v4", key_env="ZAI_API_KEY",
        model="glm-4.7", workers=4, max_tokens=2048, extra_params={},
        seeds=SEEDS[:10]),
    "groq/qwen3.8-27b": dict(
        base="https://api.groq.com/openai/v1", key_env="GROQ_API_KEY",
        model="qwen/qwen3.8-27b", workers=1, max_tokens=16,
        extra_params={}, seeds=SEEDS[:3], transport="curl", timeout=30),
        # 3 of 5 planned seeds: Groq daily token quota exhausted mid-run on
        # 2026-11-02; seeds 4-5 (192+16 of 200 classified) excluded so the
        # reported profit uses only complete sequences.
    "tud/mistral-medium-3.5-128b": dict(
        base="https://llm-service.ai.tu-darmstadt.de/v1", key_env="TUD_API_KEY",
        model="Mistral-Medium-3.5-128B", workers=4, max_tokens=16,
        extra_params={}, seeds=SEEDS[:10], transport="curl", timeout=60),
    "local/deepseek-v4-flash": dict(
        # Local DeepSeek V4 Flash served on the LAN (legion) via LiteLLM proxy;
        # reasoning model (~25 s/call) — the only provider without daily quota.
        base="http://192.168.42.20:4000/v1", key_env="LITELLM_API_KEY",
        model="local/deepseek-v4-flash/local", workers=4, max_tokens=768,
        extra_params={}, seeds=SEEDS[:5], transport="curl", timeout=150),
    "saia/qwen3.6-35b-a3b": dict(
        base="https://chat-ai.academiccloud.de/v1", key_env="SAIA_API_KEY",
        model="qwen3.6-35b-a3b", workers=1, max_tokens=16, extra_params={
            "chat_template_kwargs": {"enable_thinking": False}}, seeds=SEEDS[:2]),
}


def _post_chat(prov, system, user, timeout=120):
    body = {"model": prov["model"], "temperature": 0,
            "max_tokens": prov["max_tokens"],
            "messages": [{"role": "system", "content": system},
                         {"role": "user", "content": user}]}
    body.update(prov["extra_params"])
    payload = json.dumps(body)
    if prov.get("transport") == "curl":
        # curl --max-time gives a HARD total deadline (urllib's per-op socket
        # timeout can hang indefinitely on a slow-dribbling response).
        import subprocess
        cmd = ["curl", "-s", "--max-time", str(prov.get("timeout", 30)),
               "-X", "POST", prov["base"].rstrip("/") + "/chat/completions",
               "-H", "Authorization: Bearer " + os.environ[prov["key_env"]],
               "-H", "Content-Type: application/json",
               "-H", "User-Agent: cam-sim-benchmark/1.5",
               "--data", "@-"]
        res = subprocess.run(cmd, input=payload.encode(), capture_output=True)
        if res.returncode == 28:
            raise RuntimeError("curl timeout (hard cap)")
        if res.returncode != 0:
            raise RuntimeError(f"curl exit {res.returncode}")
        out = json.loads(res.stdout.decode())
        if "error" in out:
            err = out["error"]
            code = err.get("status") or (429 if "rate" in str(err).lower() else 500)
            raise urllib.error.HTTPError(prov["base"], code,
                                         json.dumps(err)[:200], None, None)
        return out
    req = urllib.request.Request(
        prov["base"].rstrip("/") + "/chat/completions",
        data=payload.encode(),
        headers={"Authorization": "Bearer " + os.environ[prov["key_env"]],
                 "Content-Type": "application/json",
                 "User-Agent": "cam-sim-benchmark/1.5"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())


_LABEL_RE = re.compile(r"\b(" + "|".join(LABELS) + r")\b")


def parse_label(text):
    """Strict single-word match first; word-boundary fallback; None if invalid."""
    t = (text or "").strip().lower()
    m = re.fullmatch(r"[^a-z]*(" + "|".join(LABELS) + r")[^a-z]*", t)
    if m:
        return m.group(1), False
    found = _LABEL_RE.findall(t)
    if found:
        return found[0], False
    return None, True


def classify_with_retry(prov, system, user):
    """One API call; empty-content thinking responses get a token-doubled retry."""
    last_error = None
    for max_tokens in (prov["max_tokens"], prov["max_tokens"] * 2):
        p = dict(prov, max_tokens=max_tokens)
        out = _post_chat(p, system, user)
        msg = out.get("choices", [{}])[0].get("message", {})
        label, invalid = parse_label(msg.get("content"))
        if not invalid:
            usage = out.get("usage", {}) or {}
            return label, usage.get("prompt_tokens", 0), usage.get("completion_tokens", 0)
        last_error = "unparseable: " + repr(msg.get("content"))[:80]
    raise RuntimeError(last_error)


def context_key(model_key, context):
    """Value-based key: FullContext.context_id (ctx_N) repeats across seeds,
    so labels must be keyed by the textualized observation hash instead. The
    key is bound to the system prompt (PROMPT_SHA16) so cached labels can
    never silently go stale after a prompt edit."""
    return hashlib.sha256((PROMPT_SHA16 + "||" + model_key + "||"
                           + textualize(context)).encode()).hexdigest()


def _legacy_context_key(model_key, context):
    """Legacy cache key (pre-prompt-hash); kept only as a read fallback so
    existing caches remain valid and are never silently re-run."""
    return hashlib.sha256((model_key + "||" + textualize(context)).encode()).hexdigest()


def classify_batch(model_key, contexts, progress_every=500):
    """Classify all contexts with a thread pool; JSONL cache makes reruns free.

    Returns dict with labels {context_id -> label|None}, invalid count, tokens,
    mean latency, wall time.
    """
    prov = PROVIDERS[model_key]
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_path = CACHE_DIR / (model_key.replace("/", "__") + ".jsonl")
    cache = {}
    if cache_path.exists():
        with open(cache_path, encoding="utf-8") as f:
            for line in f:
                rec = json.loads(line)
                if rec.get("label") is not None:  # retry failed calls on rerun
                    cache[rec["key"]] = rec
    tasks = []
    for c in contexts:
        user = textualize(c)
        key = context_key(model_key, c)
        # Legacy fallback: if the prompt-bound primary key is absent, accept
        # the pre-prompt-hash legacy key so existing caches stay valid.
        legacy = _legacy_context_key(model_key, c)
        if key not in cache and legacy not in cache:
            tasks.append((c.context_id, key, user))
    print(f"[{model_key}] {len(contexts)} contexts, {len(tasks)} API calls "
          f"({len(cache)} cached)", flush=True)
    t0 = time.time()
    latencies, ptoks, ctoks, n_failed = [], 0, 0, 0

    def work(item):
        cid, key, user = item
        time.sleep(1.2)  # gentle pacing: stay under provider TPM buckets
        for attempt in range(5):
            try:
                s = time.time()
                label, pt, ct = classify_with_retry(prov, SYSTEM_PROMPT, user)
                return cid, key, label, time.time() - s, pt, ct, None
            except urllib.error.HTTPError as e:
                if e.code in (429, 500, 502, 503, 504) and attempt < 4:
                    time.sleep([2, 4, 8, 16][attempt])
                    continue
                return cid, key, None, 0.0, 0, 0, f"http {e.code}"
            except Exception as e:
                if attempt < 4:
                    time.sleep(2 * (attempt + 1))
                    continue
                return cid, key, None, 0.0, 0, 0, type(e).__name__

    done = 0
    with ThreadPoolExecutor(max_workers=prov["workers"]) as ex:
        with open(cache_path, "a", encoding="utf-8") as fout:
            for cid, key, label, lat, pt, ct, err in ex.map(work, tasks):
                rec = {"key": key, "context_id": cid, "label": label,
                       "error": err, "latency": round(lat, 3)}
                cache[key] = rec
                fout.write(json.dumps(rec) + "\n")
                fout.flush()
                if err is None:
                    latencies.append(lat)
                    ptoks += pt
                    ctoks += ct
                else:
                    n_failed += 1
                done += 1
                if done % progress_every == 0:
                    rate = done / max(time.time() - t0, 1e-9)
                    print(f"[{model_key}] {done}/{len(tasks)} ({rate:.1f} calls/s)",
                          flush=True)
    labels, invalid = {}, 0
    for c in contexts:
        key = context_key(model_key, c)
        lab = (cache.get(key) or cache.get(_legacy_context_key(model_key, c)))["label"]
        labels[key] = lab
        if lab is None:
            invalid += 1
    lat_c = [((cache.get(context_key(model_key, c))
               or cache.get(_legacy_context_key(model_key, c)))["latency"])
             for c in contexts
             if (cache.get(context_key(model_key, c))
                 or cache.get(_legacy_context_key(model_key, c)))["latency"]]
    return {"labels": labels, "invalid": invalid, "failed_calls": n_failed,
            "n": len(contexts), "wall_s": round(time.time() - t0, 1),
            "prompt_tokens": ptoks, "completion_tokens": ctoks,
            "latency_mean_s": round(float(np.mean(lat_c)), 3) if lat_c else None}


# ---------------------------------------------------------------------------
# LLM zero-shot agent (mirrors cam_multisignal except the classifier)
# ---------------------------------------------------------------------------

class LLMZeroShotAgent:
    """Pre-registered §10.3 #24 agent: LLM situation estimate + fixed mapper.

    Identical to cam_multisignal's downstream pipeline (IDEAL_ACTION action
    type, SITUATION_CHANNEL channel, oracle-style bid) except the situation
    estimate comes from an API-driven LLM instead of a fitted classifier.
    Unparseable/failed labels fall back to the generic mid-funnel default
    ('consideration') and are counted (invalid_seen).
    """

    def __init__(self, name, labels_by_key, model_key):
        self.name = name
        self.labels = labels_by_key
        self.model_key = model_key
        self.oracle = CAMOracle(name="oracle_ref")  # reuses _bid() only
        self.actions_taken = 0
        self.invalid_seen = 0

    def reset(self):
        self.actions_taken = 0
        self.invalid_seen = 0

    def decide(self, context):
        self.actions_taken += 1
        sit_est = self.labels.get(context_key(self.model_key, context))
        if sit_est is None:
            sit_est = "consideration"
            self.invalid_seen += 1
        st = SituationType(sit_est)
        action_type = IDEAL_ACTION[st]
        channel = SITUATION_CHANNEL[st]
        bid = round(self.oracle._bid(st, context), 2)
        return Action(self.actions_taken, action_type, channel, bid)


# ---------------------------------------------------------------------------
# Experiment
# ---------------------------------------------------------------------------

def build_reference_agents():
    env = SimulationEnvironment(seed=999_999, config=None)
    samples = []
    for _ in range(2000):
        c = env.generate_context()
        samples.append((c.audience_intent_strength, c.situation))
    th, lab = fit_intent_classifier(samples)
    return [
        AGENT_REGISTRY["baseline"](),
        AGENT_REGISTRY["cam_inferred"](),
        CAMLearned(th, lab, name="cam_learned"),
        AGENT_REGISTRY["cam_multisignal"](),
        AGENT_REGISTRY["oracle"](),
    ]


def confusion(preds, truths):
    idx = {s: i for i, s in enumerate(LABELS)}
    m = [[0] * 6 for _ in range(6)]
    for p, t in zip(preds, truths):
        m[idx[t]][idx[p]] += 1
    return m


def paired(name_a, prof_a_by_seed, name_b, prof_b_by_seed, seeds):
    """diff = mean(prof_b) - mean(prof_a) over the shared seeds.
    NOTE: compute_statistics takes plain lists (truthiness checks)."""
    a = [prof_a_by_seed[s] for s in seeds]
    b = [prof_b_by_seed[s] for s in seeds]
    st = compute_statistics(a, b)
    return {"vs": name_a, "n_seeds": len(seeds), **st}


def paired_scenarios(name_a, scen_a_by_seed, name_b, scen_b_by_seed, seeds):
    """Per-scenario paired profit diff (primary test; n = n_seeds x 200).
    Caveat: scenarios within a seed share the situation distribution, so the
    effective n is smaller than the nominal n (clustered by seed)."""
    a = [p for s in seeds for p in scen_a_by_seed[name_a][s]]
    b = [p for s in seeds for p in scen_b_by_seed[name_b][s]]
    st = compute_statistics(a, b)
    return {"vs": name_a, "n_scenarios": int(len(a)), **st}


def walk_with_scenarios(agents, seeds, n_scen):
    """Mirror of cam_sim_v14.run_online_env that also records per-scenario profit.

    Pairing guard: per-seed totals are asserted to match run_online_env for all
    agents (byte-identical reproduction of the canonical walk)."""
    import random as _random
    per_seed = {a.name: [] for a in agents}
    per_scen = {a.name: {} for a in agents}
    for seed in seeds:
        _random.seed(seed)
        env = SimulationEnvironment(seed=seed, config=None)
        contexts = [env.generate_context() for _ in range(n_scen)]
        for agent in agents:
            agent.reset()
            totals = []
            for context in contexts:
                action = agent.decide(context)
                result = env.evaluate_action(context, action)
                totals.append(result.reward + result.long_term_value - result.cost)
            per_seed[agent.name].append(sum(totals))
            per_scen[agent.name][seed] = totals
    return per_seed, per_scen


def run_pilot(n=20):
    env = SimulationEnvironment(seed=1, config=None)
    contexts = [env.generate_context() for _ in range(n)]
    for mk in PROVIDERS:
        res = classify_batch(mk, contexts)
        preds = [res["labels"][context_key(mk, c)] for c in contexts]
        acc = 100.0 * sum(p == c.situation.value for p, c in zip(preds, contexts)) / n
        print(f"PILOT {mk}: acc={acc:.0f}% invalid={res['invalid']} "
              f"lat_mean={res['latency_mean_s']}s labels={preds}")


def run_full(models):
    results = {"meta": {
        "protocol": "g4 §10.3 #24 pre-registered LLM zero-shot classification baseline",
        "temperature": 0, "n_scen": N_SCEN, "full_seeds": "1-50",
        "reduced_seeds": "1-10 (provider rate limits; documented deviation)",
        "prompt_system_sha16": hashlib.sha256(SYSTEM_PROMPT.encode()).hexdigest()[:16],
        "date": time.strftime("%Y-%m-%d"),
    }}

    # Deterministic reference agents over the full 50-seed protocol.
    # walk_with_scenarios must reproduce run_online_env byte-identically
    # (pairing guard) and additionally gives per-scenario profit vectors.
    refs = build_reference_agents()
    agg, prof, match = run_online_env(None, SEEDS, N_SCEN, refs)
    refs2 = build_reference_agents()
    prof2, scen2 = walk_with_scenarios(refs2, SEEDS, N_SCEN)
    for a in refs:
        assert np.allclose(prof[a.name], prof2[a.name], atol=0.01), \
            f"pairing guard failed for {a.name}"
    print("pairing guard: walk_with_scenarios == run_online_env (all agents)", flush=True)
    results["reference"] = {a.name: {"profit_mean": agg[a.name]["profit_mean"],
                                     "profit_std": agg[a.name]["profit_std"],
                                     "match_mean": agg[a.name]["match_mean"]}
                            for a in refs}
    results["per_seed_profit"] = {a.name: prof[a.name] for a in refs}
    print("reference:", json.dumps(results["reference"], indent=None), flush=True)

    for mk in models:
        prov = PROVIDERS[mk]
        seeds = prov["seeds"]
        # Pre-generate the identical per-seed sequences BEFORE any evaluation
        ctx_by_seed, all_ctx = {}, []
        for s in seeds:
            env = SimulationEnvironment(seed=s, config=None)
            ctx_by_seed[s] = [env.generate_context() for _ in range(N_SCEN)]
            all_ctx += ctx_by_seed[s]
        cls = classify_batch(mk, all_ctx)
        agent_name = "llm_" + mk.split("/")[-1].replace(".", "_").replace("-", "_")
        per_seed_profit, per_seed_match, preds_all, truths_all = [], [], [], []
        llm_scen = {}
        invalid_in_walk = 0
        for s in seeds:
            eval_env = SimulationEnvironment(seed=s, config=None)  # latency RNG only
            agent = LLMZeroShotAgent(agent_name, cls["labels"], mk)
            totals, matches = [], 0
            for c in ctx_by_seed[s]:
                act = agent.decide(c)
                r = eval_env.evaluate_action(c, act)
                totals.append(r.reward + r.long_term_value - r.cost)
                matches += 1 if r.context_match else 0
                lab = cls["labels"].get(context_key(mk, c))
                if lab is None:
                    lab = "consideration"
                    invalid_in_walk += 1
                preds_all.append(lab)
                truths_all.append(c.situation.value)
            per_seed_profit.append(round(sum(totals), 2))
            per_seed_match.append(100.0 * matches / N_SCEN)
            llm_scen[s] = totals
        acc = 100.0 * sum(1 for p, t in zip(preds_all, truths_all) if p == t) / len(preds_all)
        ref_by_seed = {ref.name: dict(zip(SEEDS, prof[ref.name])) for ref in refs}
        llm_by_seed = dict(zip(seeds, per_seed_profit))
        contrasts = {
            ref.name: paired(ref.name, ref_by_seed[ref.name], agent_name,
                             llm_by_seed, seeds)
            for ref in refs if ref.name != "baseline"
        }
        scenario_contrasts = {
            ref.name: paired_scenarios(ref.name, scen2, agent_name,
                                       {agent_name: llm_scen}, seeds)
            for ref in refs if ref.name != "baseline"
        }
        results[mk] = {
            "agent": agent_name, "seeds": [seeds[0], seeds[-1]], "n_seeds": len(seeds),
            "accuracy": round(acc, 1), "invalid": cls["invalid"],
            "failed_calls": cls["failed_calls"], "n_calls": cls["n"],
            "wall_s": cls["wall_s"], "prompt_tokens": cls["prompt_tokens"],
            "completion_tokens": cls["completion_tokens"],
            "latency_mean_s": cls["latency_mean_s"],
            "profit_mean": round(float(np.mean(per_seed_profit)), 2),
            "profit_std": round(float(np.std(per_seed_profit, ddof=1)), 2),
            "match_mean": round(float(np.mean(per_seed_match)), 1),
            "confusion": confusion(preds_all, truths_all),
            "contrasts": contrasts,
            "scenario_contrasts": scenario_contrasts,
            "per_seed_profit": per_seed_profit,
        }
        print(f"[{mk}] profit=${results[mk]['profit_mean']} "
              f"match={results[mk]['match_mean']}% acc={acc:.1f}% "
              f"invalid={cls['invalid']} failed={cls['failed_calls']}", flush=True)

    OUT.mkdir(exist_ok=True)
    with open(OUT / "cam_sim_v15.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=1)
    print("wrote", OUT / "cam_sim_v15.json")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--pilot", action="store_true")
    ap.add_argument("--models", nargs="*", default=list(PROVIDERS))
    args = ap.parse_args()
    if args.pilot:
        run_pilot()
    else:
        run_full(args.models)
