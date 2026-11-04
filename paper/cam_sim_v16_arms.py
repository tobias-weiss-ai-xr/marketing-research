#!/usr/bin/env python3
"""CAM-Sim v1.6 — Prompt-variant experiment harness (P1 diagnostics, P2 remediation arms, P3 bootstrap)."""
import argparse, hashlib, itertools, json, os, random, re, sys, time, urllib.error, urllib.request
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent))
from cam_sim import (Action, ActionType, CAMOracle, ChannelType, IDEAL_ACTION, SITUATION_CHANNEL,
                     SimulationEnvironment, SituationType)
from cam_sim_v15_llm import (CACHE_DIR, PROVIDERS, SEEDS, build_reference_agents, confusion,
                             parse_label, textualize, walk_with_scenarios)
N_SCEN, OUT = 200, Path(__file__).resolve().parent.parent / "results"
ARMS_CACHE = OUT / "llm_cache" / "arms.jsonl"
LABELS = [s.value for s in SituationType]
LABEL_ORDER = {l: i for i, l in enumerate(LABELS)}
ARCHETYPES = {"exploration": (0.2,0.5,0.7), "consideration": (0.5,0.5,0.7), "decision": (0.9,0.5,0.7),
              "crisis": (0.8,0.85,0.2), "opportunity": (0.5,0.85,0.7), "retention": (0.3,0.15,0.8)}
ACTION_MENU = ["educational","comparison","promotional","crisis_response","urgent","loyalty"]
CHANNEL_MENU = ["search","social","display","email","video"]
BID_MENU = [0.3,0.5,0.7,1.0,1.4]

def variant_tag(sp: str, arm: str) -> str: return hashlib.sha256((sp+"::"+arm).encode()).hexdigest()[:16]
def cache_key(vt: str, mk: str, ut: str) -> str: return hashlib.sha256((vt+"||"+mk+"||"+ut).encode()).hexdigest()

def load_cache() -> Dict[str, dict]:
    cache = {}
    if ARMS_CACHE.exists():
        with open(ARMS_CACHE, encoding="utf-8") as f:
            for line in f:
                rec = json.loads(line.strip())
                if rec.get("label") is not None: cache[rec["key"]] = rec
    return cache

def save_cache_entry(entry: dict):
    ARMS_CACHE.parent.mkdir(parents=True, exist_ok=True)
    with open(ARMS_CACHE, "a", encoding="utf-8") as f: f.write(json.dumps(entry)+"\n"); f.flush()

def _call_api(prov, system, user, temperature=0):
    body = {"model": prov["model"], "temperature": temperature, "max_tokens": prov.get("max_tokens",16),
            "messages": [{"role":"system","content":system},{"role":"user","content":user}]}
    body.update(prov.get("extra_params",{}))
    payload = json.dumps(body)
    if prov.get("transport") == "curl":
        import subprocess
        cmd = ["curl","-s","--max-time",str(prov.get("timeout",30)),"-X","POST",
               prov["base"].rstrip("/")+"/chat/completions","-H","Authorization: Bearer "+os.environ[prov["key_env"]],
               "-H","Content-Type: application/json","-H","User-Agent: cam-sim/1.6","--data","@-"]
        res = subprocess.run(cmd, input=payload.encode(), capture_output=True)
        if res.returncode != 0: raise RuntimeError(f"curl exit {res.returncode}")
        out = json.loads(res.stdout.decode())
    else:
        req = urllib.request.Request(prov["base"].rstrip("/")+"/chat/completions", data=payload.encode(),
            headers={"Authorization":"Bearer "+os.environ[prov["key_env"]],"Content-Type":"application/json"})
        with urllib.request.urlopen(req, timeout=120) as r: out = json.loads(r.read().decode())
    if "error" in out:
        err = out["error"]; code = err.get("status") or (429 if "rate" in str(err).lower() else 500)
        raise urllib.error.HTTPError(prov["base"], code, json.dumps(err)[:200], None, None)
    return out

def classify_variant(system_prompt, user_text, model_key, arm_name, cache, temperature=0):
    vt = variant_tag(system_prompt, arm_name); key = cache_key(vt, model_key, user_text)
    if key in cache:
        rec = cache[key]; return rec["label"], rec.get("prompt_tokens",0), rec.get("completion_tokens",0), rec.get("latency_s",0.0)
    prov = PROVIDERS.get(model_key)
    if not prov: raise ValueError(f"Unknown model: {model_key}")
    for attempt in range(5):
        try:
            out = _call_api(prov, system_prompt, user_text, temperature)
            msg = out.get("choices",[{}])[0].get("message",{}); content = msg.get("content","")
            label, invalid = parse_label(content)
            usage = out.get("usage",{}) or {}; pt, ct = usage.get("prompt_tokens",0), usage.get("completion_tokens",0)
            if label is not None:
                save_cache_entry({"key":key,"label":label,"latency_s":0.0,"prompt_tokens":pt,"completion_tokens":ct,"error":None})
                return label, pt, ct, 0.0
        except urllib.error.HTTPError as e:
            if e.code in (429,500,502,503,504) and attempt < 4: time.sleep([2,4,8,16][attempt]); continue
            break
        except Exception:
            if attempt < 4: time.sleep(2*(attempt+1)); continue; break
    save_cache_entry({"key":key,"label":None,"latency_s":0.0,"prompt_tokens":0,"completion_tokens":0,"error":"failed"})
    return None, 0, 0, 0.0

def classify_batch_variant(system_prompt, contexts, model_key, arm_name, max_passes=8):
    cache = load_cache(); t0 = time.time(); ptoks, ctoks, n_failed = 0, 0, 0
    for passage in range(max_passes):
        missing = [(c, textualize(c)) for c in contexts if cache_key(variant_tag(system_prompt,arm_name),model_key,textualize(c)) not in cache]
        if not missing: break
        def _work(item):
            ctx, user = item
            time.sleep(1.0)  # gentle pacing under provider TPM buckets
            return classify_variant(system_prompt, user, model_key, arm_name, cache)
        with ThreadPoolExecutor(max_workers=4) as pool:
            for label, pt, ct, _lat in pool.map(_work, missing):
                if label: ptoks += pt; ctoks += ct
                else: n_failed += 1
        cache = load_cache()
    labels, invalid = {}, 0
    for c in contexts:
        key = cache_key(variant_tag(system_prompt,arm_name), model_key, textualize(c))
        lab = cache.get(key,{}).get("label"); labels[key] = lab
        if lab is None: invalid += 1
    return {"labels":labels,"invalid":invalid,"failed_calls":n_failed,"n":len(contexts),
            "wall_s":round(time.time()-t0,1),"prompt_tokens":ptoks,"completion_tokens":ctoks}

def bootstrap_ci(values, n_reps=10000, seed=20261103):
    rng = np.random.RandomState(seed); arr = np.array(values); n = len(arr)
    if n < 2: return float(np.mean(arr)), float(np.mean(arr)), float(np.mean(arr))
    means = [np.mean(arr[rng.randint(0,n,size=n)]) for _ in range(n_reps)]
    return float(np.mean(arr)), *np.percentile(means, [2.5,97.5])

def bootstrap_diff_ci(values_a, values_b, n_reps=10000, seed=20261103):
    rng = np.random.RandomState(seed); n = len(values_a)
    if n < 2: return float(np.mean(values_b)-np.mean(values_a)), 0.0, 0.0
    diffs = [np.mean(np.array(values_b)[rng.randint(0,n,size=n)]) - np.mean(np.array(values_a)[rng.randint(0,n,size=n)]) for _ in range(n_reps)]
    return float(np.mean(values_b)-np.mean(values_a)), *np.percentile(diffs, [2.5,97.5])

def majority_vote(labels_list):
    counts = Counter(labels_list); max_count = max(counts.values())
    return min([l for l,c in counts.items() if c==max_count], key=lambda x: LABEL_ORDER.get(x,999))

def _eval_contexts(contexts, labels_by_key, system_prompt, model_key, arm_tag):
    oracle = CAMOracle("oracle_ref"); totals, matches = [], 0
    eval_env = SimulationEnvironment(seed=999, config=None)
    for c in contexts:
        key = cache_key(variant_tag(system_prompt,arm_tag), model_key, textualize(c))
        lab = labels_by_key.get(key); sit = SituationType(lab if lab else "consideration")
        action = Action(0, IDEAL_ACTION[sit], SITUATION_CHANNEL[sit], round(oracle._bid(sit,c), 2))
        r = eval_env.evaluate_action(c, action)
        totals.append(r.reward + r.long_term_value - r.cost)
        if r.context_match: matches += 1
    return totals, matches

def _per_class_recalls(preds, truths):
    class_data = {l: {"preds":[],"truths":[]} for l in LABELS}
    for p, t in zip(preds, truths): class_data[t]["preds"].append(p); class_data[t]["truths"].append(t)
    recalls = {l: 100.0*sum(1 for p,t in zip(class_data[l]["preds"],class_data[l]["truths"]) if p==t)/max(len(class_data[l]["truths"]),1) for l in LABELS}
    return recalls, np.mean(list(recalls.values()))

def run_arm_a(max_passes):
    blocks = ["- exploration: early-funnel discovery; consumers browse casually with little purchase intent.",
              "- consideration: mid-funnel evaluation; consumers actively compare options and features.",
              "- decision: bottom-funnel purchase readiness; consumers intend to buy imminently.",
              "- retention: existing-customer care; the goal is strengthening loyalty and reducing churn.",
              "- crisis: a reputation emergency; negative publicity threatens the brand and demands rapid response.",
              "- opportunity: a favorable window; conditions allow an unusually effective push for the brand."]
    model_key, seed = "tud/mistral-medium-3.5-128b", 1
    random.seed(seed); env = SimulationEnvironment(seed=seed, config=None)
    contexts = [env.generate_context() for _ in range(N_SCEN)]
    results = {"arm":"A","name":"order-permutation","permutations":[]}
    # 6 fixed permutations (identity + 5 non-trivial), NOT the full 720-permutation sweep
    perms = [(0,1,2,3,4,5), (1,2,3,4,5,0), (5,4,3,2,1,0), (1,0,3,2,5,4), (2,0,3,5,1,4), (0,2,1,4,3,5)]
    for perm in perms:
        blk = [blocks[i] for i in perm]
        sp = "You classify a digital-marketing moment into exactly one of six marketing situations:\n\n"+"\n".join(blk)+\
             "\n\nYou will receive one observation with numeric scales (0 to 1). Respond with exactly one word — the situation label — and nothing else."
        res = classify_batch_variant(sp, contexts, model_key, "arm_a_perm_"+" ".join(map(str,perm)), max_passes)
        preds = [res["labels"].get(cache_key(variant_tag(sp,"arm_a_perm_"+" ".join(map(str,perm))),model_key,textualize(c))) for c in contexts]
        acc = 100.0*sum(1 for p,c in zip(preds,contexts) if p==c.situation.value)/N_SCEN
        results["permutations"].append({"order":list(perm),"accuracy":round(acc,1),"confusion":confusion(preds,[c.situation.value for c in contexts]),
                                        "invalid":res["invalid"],"failed_calls":res["failed_calls"]})
    return results

def run_arm_b(max_passes, models):
    sp = "You classify a digital-marketing moment into exactly one of six marketing situations. Respond with exactly one word — the situation label — and nothing else. The six situations are: exploration, consideration, decision, crisis, opportunity, retention."
    seed = 1; random.seed(seed); env = SimulationEnvironment(seed=seed, config=None)
    contexts = [env.generate_context() for _ in range(N_SCEN)]
    results = {"arm":"B","name":"minimal-labels","models":{}}
    for mk in models:
        res = classify_batch_variant(sp, contexts, mk, "arm_b", max_passes)
        preds = [res["labels"].get(cache_key(variant_tag(sp,"arm_b"),mk,textualize(c))) for c in contexts]
        acc = 100.0*sum(1 for p,c in zip(preds,contexts) if p==c.situation.value)/N_SCEN
        results["models"][mk] = {"accuracy":round(acc,1),"confusion":confusion(preds,[c.situation.value for c in contexts]),
                                 "invalid":res["invalid"],"failed_calls":res["failed_calls"]}
    return results

def run_arm_c(max_passes, models):
    sp = """You classify a digital-marketing moment into exactly one of six marketing situations:
- exploration: early-funnel discovery; consumers browse casually with little purchase intent.
- consideration: mid-funnel evaluation; consumers actively compare options and features.
- decision: bottom-funnel purchase readiness; consumers intend to buy imminently.
- retention: existing-customer care; the goal is strengthening loyalty and reducing churn.
- crisis: a reputation emergency; negative publicity threatens the brand and demands rapid response.
- opportunity: a favorable window; conditions allow an unusually effective push for the brand.
You will receive one observation with numeric scales (0 to 1). Respond with exactly one word — the situation label — and nothing else."""
    probes = []
    for arch, (intent, comp, qual) in ARCHETYPES.items():
        variants = [(intent,comp,qual)]
        for delta in [+0.15,-0.15]:
            variants.append((min(1.0,intent+delta),comp,qual)); variants.append((intent,min(1.0,comp+delta),qual)); variants.append((intent,comp,min(1.0,qual+delta)))
        for i,(i_,c_,q_) in enumerate(variants[:7]): probes.append((arch,i_,c_,q_))
    results = {"arm":"C","name":"counterfactual-archetypes","models":{},"crisis_or_retention":False}
    cache = load_cache()
    for mk in models:
        model_res = {"archetypes":{}}
        for arch, intent, comp, qual in probes:
            user = f"Observation:\n- audience_intent_strength: {intent:.3f}\n- competitive_density: {comp:.3f}\n- channel_quality: {qual:.3f}\n- signals: intent_strength={intent}; quality_score=0.72; time_of_day=morning; device_type=mobile"
            label,_,_,_ = classify_variant(sp, user, mk, f"arm_c_{arch}_{intent}_{comp}_{qual}", cache)
            if label in ("crisis","retention"): results["crisis_or_retention"] = True
            if arch not in model_res["archetypes"]: model_res["archetypes"][arch] = Counter()
            model_res["archetypes"][arch][label] += 1
        results["models"][mk] = model_res
    return results

def run_arm_d(max_passes):
    sp = """You classify a digital-marketing moment into exactly one of six marketing situations:
- exploration: early-funnel discovery; consumers browse casually with little purchase intent.
- consideration: mid-funnel evaluation; consumers actively compare options and features.
- decision: bottom-funnel purchase readiness; consumers intend to buy imminently.
- retention: existing-customer care; the goal is strengthening loyalty and reducing churn.
- crisis: a reputation emergency; negative publicity threatens the brand and demands rapid response.
- opportunity: a favorable window; conditions allow an unusually effective push for the brand.
You will receive one observation with numeric scales (0 to 1). Respond with exactly one word — the situation label — and nothing else."""
    model_key, seed = "tud/mistral-medium-3.5-128b", 1
    random.seed(seed); env = SimulationEnvironment(seed=seed, config=None)
    contexts = [env.generate_context() for _ in range(N_SCEN)]
    def textualize_no_decoy(ctx):
        sigs = "; ".join(f"{s.name}={s.value}" for s in ctx.signals if s.name != "quality_score")
        return f"Observation:\n- audience_intent_strength: {ctx.audience_intent_strength:.3f}\n- competitive_density: {ctx.competitive_density:.3f}\n- channel_quality: {ctx.channel_quality:.3f}\n- signals: {sigs}\n\nSituation label (one word):"
    cache = load_cache()
    for c in contexts:
        user = textualize_no_decoy(c); vt = variant_tag(sp, "arm_d"); key = cache_key(vt, model_key, user)
        if key not in cache: classify_variant(sp, user, model_key, "arm_d", cache)
    cache = load_cache(); preds = []
    for c in contexts:
        user = textualize_no_decoy(c); key = cache_key(variant_tag(sp,"arm_d"), model_key, user)
        preds.append(cache.get(key,{}).get("label"))
    acc = 100.0*sum(1 for p,c in zip(preds,contexts) if p==c.situation.value)/N_SCEN
    v15_cache_path = CACHE_DIR / (model_key.replace("/", "__") + ".jsonl"); v15_acc = None
    if v15_cache_path.exists():
        v15_cache = {}
        with open(v15_cache_path, encoding="utf-8") as f:
            for line in f: rec = json.loads(line); v15_cache[rec["key"]] = rec.get("label")
        from cam_sim_v15_llm import context_key as v15_context_key, _legacy_context_key as v15_legacy_context_key
        v15_preds = [v15_cache.get(v15_context_key(model_key,c)) or v15_cache.get(v15_legacy_context_key(model_key,c)) for c in contexts]
        v15_acc = 100.0*sum(1 for p,c in zip(v15_preds,contexts) if p==c.situation.value)/N_SCEN
    return {"arm":"D","name":"decoy-removal","accuracy":round(acc,1),"v15_accuracy":round(v15_acc,1) if v15_acc else None,
            "delta":round(acc-v15_acc,1) if v15_acc else None,"invalid":sum(1 for p in preds if p is None)}

def _run_arm_ef(max_passes, models, seeds, arm_letter, extra_prompt=""):
    base = """You classify a digital-marketing moment into exactly one of six marketing situations:
- exploration: early-funnel discovery; consumers browse casually with little purchase intent.
- consideration: mid-funnel evaluation; consumers actively compare options and features.
- decision: bottom-funnel purchase readiness; consumers intend to buy imminently.
- retention: existing-customer care; the goal is strengthening loyalty and reducing churn.
- crisis: a reputation emergency; negative publicity threatens the brand and demands rapid response.
- opportunity: a favorable window; conditions allow an unusually effective push for the brand.
"""
    if arm_letter == "E":
        sp = base + "\nNote: crisis combines high purchase intent with intense competitor activity and notably LOW channel quality.\nNote: retention is an existing-customer moment with low intent and notably LOW competitive density.\n\nYou will receive one observation with numeric scales (0 to 1). Respond with exactly one word — the situation label — and nothing else."
    else:  # F
        sp = base + """Examples:
Example exploration: intent 0.18, competition 0.55, quality 0.66.
Example consideration: intent 0.47, competition 0.50, quality 0.72.
Example decision: intent 0.86, competition 0.46, quality 0.75.
Example crisis: intent 0.78, competition 0.88, quality 0.24.
Example opportunity: intent 0.55, competition 0.82, quality 0.61.
Example retention: intent 0.27, competition 0.17, quality 0.79.

You will receive one observation with numeric scales (0 to 1). Respond with exactly one word — the situation label — and nothing else."""
    results = {"arm":arm_letter,"name":"qualitative-hints" if arm_letter=="E" else "few-shot","models":{}}
    refs = build_reference_agents(); ref_per_seed, _ = walk_with_scenarios(refs, seeds, N_SCEN)
    for mk in models:
        all_preds, all_truths, per_seed_profit = [], [], []
        for seed in seeds:
            random.seed(seed); env = SimulationEnvironment(seed=seed, config=None)
            contexts = [env.generate_context() for _ in range(N_SCEN)]
            res = classify_batch_variant(sp, contexts, mk, f"arm_{arm_letter.lower()}_{seed}", max_passes)
            for c in contexts:
                key = cache_key(variant_tag(sp,f"arm_{arm_letter.lower()}_{seed}"), mk, textualize(c))
                lab = res["labels"].get(key); all_preds.append(lab if lab else "consideration"); all_truths.append(c.situation.value)
            oracle = CAMOracle("oracle_ref"); totals = []
            for c in contexts:
                key = cache_key(variant_tag(sp,f"arm_{arm_letter.lower()}_{seed}"), mk, textualize(c))
                lab = res["labels"].get(key); sit = SituationType(lab if lab else "consideration")
                action = Action(0, IDEAL_ACTION[sit], SITUATION_CHANNEL[sit], round(oracle._bid(sit,c), 2))
                r = env.evaluate_action(c, action); totals.append(r.reward + r.long_term_value - r.cost)
            per_seed_profit.append(sum(totals))
        acc = 100.0*sum(1 for p,t in zip(all_preds,all_truths) if p==t)/len(all_truths)
        recalls, macro_recall = _per_class_recalls(all_preds, all_truths)
        profit_mean, profit_lo, profit_hi = bootstrap_ci(per_seed_profit)
        contrasts = {}
        for ref in refs:
            if ref.name in ("cam_inferred","cam_multisignal"):
                diff, diff_lo, diff_hi = bootstrap_diff_ci(ref_per_seed[ref.name], per_seed_profit)
                contrasts[ref.name] = {"diff":round(diff,2),"ci95":[round(diff_lo,2),round(diff_hi,2)]}
        results["models"][mk] = {"accuracy":round(acc,1),"macro_recall":round(macro_recall,1),
            "crisis_recall":round(recalls.get("crisis",0),1),"retention_recall":round(recalls.get("retention",0),1),
            "profit_mean":round(profit_mean,2),"profit_ci95":[round(profit_lo,2),round(profit_hi,2)],
            "contrasts":contrasts,"per_seed_profit":[round(p,2) for p in per_seed_profit]}
    return results

def run_arm_g(max_passes, models, seeds):
    sp = """You classify a digital-marketing moment into exactly one of six marketing situations:
- exploration: early-funnel discovery; consumers browse casually with little purchase intent.
- consideration: mid-funnel evaluation; consumers actively compare options and features.
- decision: bottom-funnel purchase readiness; consumers intend to buy imminently.
- retention: existing-customer care; the goal is strengthening loyalty and reducing churn.
- crisis: a reputation emergency; negative publicity threatens the brand and demands rapid response.
- opportunity: a favorable window; conditions allow an unusually effective push for the brand.
You will receive one observation with numeric scales (0 to 1). Respond with exactly one word — the situation label — and nothing else."""
    results = {"arm":"G","name":"self-consistency","models":{}}
    for mk in models:
        crisis_correct, crisis_total, retention_correct, retention_total = 0, 0, 0, 0
        for seed in seeds:
            random.seed(seed); env = SimulationEnvironment(seed=seed, config=None)
            contexts = [env.generate_context() for _ in range(N_SCEN)]
            for c in contexts:
                if c.situation.value not in ("crisis","retention"): continue
                samples = []
                for k in range(5):
                    user = textualize(c); vt = variant_tag(sp, f"arm_g_{seed}_{c.context_id}_{k}")
                    key = cache_key(vt, mk, user); cache = load_cache()
                    if key in cache: lab = cache[key].get("label")
                    else: lab,_,_,_ = classify_variant(sp, user, mk, f"arm_g_{seed}_{c.context_id}_{k}", {}, temperature=0.7)
                    if lab: samples.append(lab)
                if len(samples) < 3: continue
                vote = majority_vote(samples)
                if c.situation.value == "crisis": crisis_total += 1; crisis_correct += (1 if vote == "crisis" else 0)
                elif c.situation.value == "retention": retention_total += 1; retention_correct += (1 if vote == "retention" else 0)
        v15_path = CACHE_DIR / (mk.replace("/","__")+".jsonl")
        v15_crisis_correct, v15_crisis_total, v15_retention_correct, v15_retention_total = 0, 0, 0, 0
        if v15_path.exists():
            v15_cache = {}
            with open(v15_path, encoding="utf-8") as f:
                for line in f: rec = json.loads(line); v15_cache[rec["key"]] = rec.get("label")
            from cam_sim_v15_llm import context_key as v15_context_key, _legacy_context_key as v15_legacy_context_key
            for seed in seeds:
                random.seed(seed); env = SimulationEnvironment(seed=seed, config=None)
                contexts = [env.generate_context() for _ in range(N_SCEN)]
                for c in contexts:
                    if c.situation.value not in ("crisis","retention"): continue
                    key = v15_context_key(mk, c); lab = v15_cache.get(key) or v15_cache.get(v15_legacy_context_key(mk, c))
                    if lab is None: continue
                    if c.situation.value == "crisis": v15_crisis_total += 1; v15_crisis_correct += (1 if lab == "crisis" else 0)
                    elif c.situation.value == "retention": v15_retention_total += 1; v15_retention_correct += (1 if lab == "retention" else 0)
        results["models"][mk] = {"crisis_recall_sc":round(100.0*crisis_correct/max(crisis_total,1),1),"crisis_total":crisis_total,
            "retention_recall_sc":round(100.0*retention_correct/max(retention_total,1),1),"retention_total":retention_total,
            "crisis_recall_zeroshot":round(100.0*v15_crisis_correct/max(v15_crisis_total,1),1) if v15_crisis_total else None,
            "retention_recall_zeroshot":round(100.0*v15_retention_correct/max(v15_retention_total,1),1) if v15_retention_total else None}
    return results

def run_arm_h(max_passes, models, seeds):
    sp = """You choose a marketing action given an observation. Respond with exactly one line in this format:
situation; action; channel; bid
Menus: situation: exploration, consideration, decision, crisis, opportunity, retention
       action: educational, comparison, promotional, crisis_response, urgent, loyalty
       channel: search, social, display, email, video
       bid: 0.3, 0.5, 0.7, 1.0, 1.4
Normative guidance:
exploration: educate browsers with broad-reach content on search.
consideration: help comparers evaluate options on social channels.
decision: push promotional offers to ready buyers on search.
crisis: pause spending and respond defensively on social.
opportunity: act urgently to capture the window on display.
retention: nurture loyalty on cheap email channels.
Respond with exactly one line: situation; action; channel; bid"""
    results = {"arm":"H","name":"end-to-end","models":{}}
    refs = build_reference_agents(); ref_per_seed, ref_per_scen = walk_with_scenarios(refs, seeds, N_SCEN)
    for mk in models:
        per_seed_profit, invalid_counts = [], []; action_dist, channel_dist, bid_dist = Counter(), Counter(), Counter()
        match_ideal, total_scenarios = 0, 0
        for seed in seeds:
            random.seed(seed); env = SimulationEnvironment(seed=seed, config=None)
            contexts = [env.generate_context() for _ in range(N_SCEN)]
            seed_invalid, seed_profit = 0, 0.0
            cache = load_cache()
            for c in contexts:
                user = textualize(c); vt = variant_tag(sp, f"arm_h_{seed}"); key = cache_key(vt, mk, user)
                rec = cache.get(key)
                content = rec.get("content") if rec else None
                if content is None and mk in PROVIDERS:
                    prov = PROVIDERS[mk]
                    try:
                        out = _call_api(prov, sp, user, temperature=0)
                        content = out.get("choices",[{}])[0].get("message",{}).get("content","")
                        lab = None
                        try: lab = SituationType(content.split(";")[0].strip().lower()).value
                        except (ValueError, KeyError): pass
                        rec = {"key":key,"content":content,"label":lab}
                        save_cache_entry(rec); cache[key] = rec
                    except Exception:
                        content = None; rec = None
                action = None
                if content:
                    parts = [p.strip() for p in (content or "").split(";")]
                    if len(parts) == 4:
                        try:
                            sit = SituationType(parts[0].lower()); act = ActionType(parts[1].lower())
                            ch = ChannelType(parts[2].lower()); bid = float(parts[3])
                            if bid in BID_MENU: action = Action(0, act, ch, bid)
                        except (ValueError, KeyError): pass
                if action is None: action = Action(0, ActionType.EDUCATIONAL, list(ChannelType)[0], 1.0); seed_invalid += 1
                else:
                    action_dist[action.action_type.value] += 1; channel_dist[action.channel.value] += 1; bid_dist[action.bid] += 1
                    if action.action_type == IDEAL_ACTION[c.situation]: match_ideal += 1
                r = env.evaluate_action(c, action); seed_profit += r.reward + r.long_term_value - r.cost
                total_scenarios += 1
            per_seed_profit.append(seed_profit); invalid_counts.append(seed_invalid)
        profit_mean, profit_std = float(np.mean(per_seed_profit)), float(np.std(per_seed_profit, ddof=1))
        profit_mean_bs, profit_lo, profit_hi = bootstrap_ci(per_seed_profit)
        contrasts = {}
        for ref in refs:
            if ref.name in ("cam_inferred","cam_multisignal","oracle"):
                diff, diff_lo, diff_hi = bootstrap_diff_ci(ref_per_seed[ref.name], per_seed_profit)
                contrasts[ref.name] = {"diff":round(diff,2),"ci95":[round(diff_lo,2),round(diff_hi,2)]}
        results["models"][mk] = {"profit_mean":round(profit_mean,2),"profit_std":round(profit_std,2),
            "profit_ci95":[round(profit_lo,2),round(profit_hi,2)],"match_rate_ideal":round(100.0*match_ideal/max(total_scenarios,1),1),
            "invalid_total":sum(invalid_counts),"action_dist":dict(action_dist),"channel_dist":dict(channel_dist),
            "bid_dist":{str(k):v for k,v in bid_dist.items()},"contrasts":contrasts,"per_seed_profit":[round(p,2) for p in per_seed_profit]}
    return results

def run_selftest():
    print("Running selftest...", flush=True)
    # Test 1: variant-key stability
    vt1, vt2, vt3 = variant_tag("prompt1","arm_a"), variant_tag("prompt1","arm_a"), variant_tag("prompt1","arm_b")
    assert vt1 == vt2 and vt1 != vt3, "variant_tag not stable"
    k1, k2, k3 = cache_key(vt1,"model1","user1"), cache_key(vt1,"model1","user1"), cache_key(vt1,"model2","user1")
    assert k1 == k2 and k1 != k3, "cache_key not stable"
    print("  [OK] variant-key stability", flush=True)
    # Test 2: parse_label
    for label in LABELS:
        parsed, invalid = parse_label(label); assert parsed == label and not invalid
        parsed, invalid = parse_label(label.upper()); assert parsed == label and not invalid
    parsed, invalid = parse_label("invalid_label"); assert parsed is None and invalid
    print("  [OK] parse_label", flush=True)
    # Test 3: majority vote tie-breaking (LABELS: exploration=0, consideration=1, decision=2, crisis=3, opportunity=4, retention=5)
    assert majority_vote(["crisis","crisis","decision","decision","exploration"]) == "decision"
    assert majority_vote(["crisis","decision","exploration","consideration","opportunity"]) == "exploration"
    print("  [OK] majority vote tie-breaking", flush=True)
    # Test 4: bootstrap CI width > 0
    mean, lo, hi = bootstrap_ci([1.0,2.0,3.0,4.0,5.0], n_reps=1000); assert hi > lo
    print("  [OK] bootstrap CI width > 0", flush=True)
    # Test 5: Action construction and evaluation
    random.seed(42); env = SimulationEnvironment(seed=42, config=None); ctx = env.generate_context()
    action = Action(0, ActionType.PROMOTIONAL, ChannelType.SEARCH, 1.0)
    result = env.evaluate_action(ctx, action); assert hasattr(result, "profit")
    print("  [OK] Action construction and evaluation", flush=True)
    print("SELFTEST-OK", flush=True); return 0

def main():
    parser = argparse.ArgumentParser(description="CAM-Sim v1.6 — Prompt-variant experiment harness")
    parser.add_argument("--arms", type=str, default="A,B,C,D,E,F,G,H")
    parser.add_argument("--models", type=str, nargs="*", default=None)
    parser.add_argument("--max-passes", type=int, default=8)
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--seeds", type=str, default="1,2,3,4,5")
    args = parser.parse_args()
    if args.selftest: return run_selftest()
    arms = [a.strip().upper() for a in args.arms.split(",")]
    # Fail fast on anything that is not a single-letter arm: a bare word
    # (e.g. --arms counterfactual) would otherwise silently dispatch nothing
    # and write a meta-only JSON with a zero-exit "success".
    VALID = set("ABCDEFGH")
    unknown = [a for a in arms if a not in VALID or len(a) != 1]
    if unknown:
        raise SystemExit(f"Unknown / non-single-letter arm(s): {unknown}. "
                         f"Expected one or more of {sorted(VALID)} (e.g. --arms C,E,F,H).")  # self-documenting safety guard
    models = args.models if args.models else list(PROVIDERS.keys())
    seeds = [int(s.strip()) for s in args.seeds.split(",")]
    results = {"meta":{"date":time.strftime("%Y-%m-%d"),"arms":arms,"models":models,"seeds":seeds,"max_passes":args.max_passes}}
    for arm in arms:
        print(f"\n=== Running ARM {arm} ===", flush=True)
        if arm == "A": results["arm_A"] = run_arm_a(args.max_passes)
        elif arm == "B": results["arm_B"] = run_arm_b(args.max_passes, models)
        elif arm == "C": results["arm_C"] = run_arm_c(args.max_passes, models)
        elif arm == "D": results["arm_D"] = run_arm_d(args.max_passes)
        elif arm == "E": results["arm_E"] = _run_arm_ef(args.max_passes, models, seeds, "E")
        elif arm == "F": results["arm_F"] = _run_arm_ef(args.max_passes, models, seeds, "F")
        elif arm == "G": results["arm_G"] = run_arm_g(args.max_passes, models, seeds)
        elif arm == "H": results["arm_H"] = run_arm_h(args.max_passes, models, seeds)
    OUT.mkdir(parents=True, exist_ok=True)
    with open(OUT / "cam_sim_v16.json", "w", encoding="utf-8") as f: json.dump(results, f, indent=1)
    print(f"\nWrote {OUT / 'cam_sim_v16.json'}", flush=True)
    print("\n=== Summary ===", flush=True)
    for arm_key in sorted(results.keys()):
        if arm_key.startswith("arm_"):
            arm_data = results[arm_key]
            print(f"{arm_key}: {arm_data.get('name','N/A')}", flush=True)
            if "models" in arm_data:
                for mk, md in arm_data["models"].items():
                    if "accuracy" in md: print(f"  {mk}: acc={md['accuracy']}%", flush=True)
                    if "profit_mean" in md: print(f"  {mk}: profit={md['profit_mean']}", flush=True)
    return 0

if __name__ == "__main__": sys.exit(main())
