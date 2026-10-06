#!/usr/bin/env python3
"""CAM-Sim ablations: 4 experiments (round-3 deferred + round-4 context-blind policy search).

1. Majority-action floor: always-EDUCATIONAL, flat bid.
2. Matched-family ablation: NCC on intent-only vs NCC on 3 signals.
3. Paired-difference bootstrap B=2000 (bootstraps paired diffs, not marginals).
4. Context-blind policy search: constant (action, channel, bid) policies (round-4 adversarial).

Usage: python paper/cam_sim_ablations.py
Self-contained: imports from paper/cam_sim.py only. Deterministic.
"""
import json, sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).parent))
from cam_sim import (Action, ActionType, AGENT_REGISTRY, Agent, CAMOracle, ChannelType,
    ENVIRONMENT_PRESETS, FullContext, IDEAL_ACTION, SITUATION_CHANNEL,
    SimulationEnvironment, SituationType, compute_statistics, run_env)

SEEDS = list(range(1, 51))
N_SCEN = 200
B_BOOT = 2000
SEED_BOOT = 123
OUT = Path(__file__).resolve().parent.parent / "results"

class MajorityActionAgent(Agent):
    """Always-EDUCATIONAL, flat bid. The true context-FREE floor (SEARCH channel)."""
    def __init__(self):
        super().__init__("majority_action")
        self._engine = CAMOracle("majority_action_engine")
    def decide(self, context):
        self.actions_taken += 1
        return Action(self.actions_taken, ActionType.EDUCATIONAL, ChannelType.SEARCH, 1.0)

class ContextBlindAgent(Agent):
    """Always picks a fixed (action_type, channel, bid). Context-FREE."""
    def __init__(self, action_type, channel, bid, name):
        super().__init__(name)
        self._action_type = action_type
        self._channel = channel
        self._bid = bid
    def decide(self, context):
        self.actions_taken += 1
        return Action(self.actions_taken, self._action_type, self._channel, self._bid)

def fit_ncc_intent_centroids(samples):
    sums, counts = {}, {}
    for intent, situation in samples:
        sums[situation] = sums.get(situation, 0.0) + intent
        counts[situation] = counts.get(situation, 0) + 1
    return {s: sums[s] / counts[s] for s in sums}

def fit_ncc_intent_from_env(config_overrides=None, calib_seed=999_999, n=2000):
    cfg = dict(ENVIRONMENT_PRESETS["default"])
    if config_overrides: cfg.update(config_overrides)
    env2 = SimulationEnvironment(seed=calib_seed, config=cfg)
    samples = []
    for _ in range(n):
        c = env2.generate_context()
        samples.append((c.audience_intent_strength, c.situation))
    return fit_ncc_intent_centroids(samples)

class NCCIntentAgent(Agent):
    """Nearest-centroid on intent-only. Same family as cam_multisignal, 1 signal."""
    def __init__(self, centroids, name="ncc_intent_only"):
        super().__init__(name)
        self.centroids = dict(centroids)
        self._engine = CAMOracle(name + "_engine")
    def classify(self, intent):
        best, best_dist = None, float("inf")
        for situation, centroid in self.centroids.items():
            d = abs(intent - centroid)
            if d < best_dist: best_dist, best = d, situation
        return best
    def decide(self, context):
        self.actions_taken += 1
        situation = self.classify(context.audience_intent_strength)
        action_type = IDEAL_ACTION[situation]
        channel = SITUATION_CHANNEL[situation]
        bid = self._engine._bid(situation, context)
        return Action(self.actions_taken, action_type, channel, round(bid, 2))

def paired_bootstrap_ci(diffs, n_resamples=B_BOOT, seed=SEED_BOOT):
    """Percentile bootstrap on paired differences (not marginal means)."""
    rng = np.random.default_rng(seed)
    d = np.asarray(diffs, dtype=float); n = len(d)
    boot_means = np.empty(n_resamples)
    for i in range(n_resamples):
        idx = rng.integers(0, n, n)
        boot_means[i] = d[idx].mean()
    lo, hi = np.percentile(boot_means, [2.5, 97.5])
    return float(d.mean()), float(lo), float(hi), float(boot_means.std(ddof=1))

CB_POLICIES = [
    ("cb_edu_email_030", ActionType.EDUCATIONAL, ChannelType.EMAIL, 0.30),
    ("cb_edu_email_050", ActionType.EDUCATIONAL, ChannelType.EMAIL, 0.50),
    ("cb_edu_email_100", ActionType.EDUCATIONAL, ChannelType.EMAIL, 1.00),
    ("cb_edu_search_100", ActionType.EDUCATIONAL, ChannelType.SEARCH, 1.00),
    ("cb_loy_email_030", ActionType.LOYALTY, ChannelType.EMAIL, 0.30),
]

def main():
    centroids = fit_ncc_intent_from_env()
    AGENT_REGISTRY["majority_action"] = MajorityActionAgent
    AGENT_REGISTRY["ncc_intent_only"] = (lambda c=centroids: NCCIntentAgent(c))
    for name, at, ch, bid in CB_POLICIES:
        AGENT_REGISTRY[name] = (lambda at=at, ch=ch, bid=bid, name=name: ContextBlindAgent(at, ch, bid, name))
    agents = ["baseline", "majority_action", "ncc_intent_only",
              "cam_inferred", "cam_learned", "cam_multisignal", "cam_multisignal_learned"]
    print(f"[1/3] Ablation ladder: {len(agents)} agents, {len(SEEDS)} seeds x {N_SCEN} ...")
    aggregate, _, per_seed, _, _ = run_env(None, seeds=SEEDS, scenarios=N_SCEN, agent_names=agents)
    results = {"n_seeds": len(SEEDS), "n_scenarios": N_SCEN,
               "bootstrap_B": B_BOOT, "bootstrap_seed": SEED_BOOT,
               "agents": aggregate, "paired_contrasts": {}, "matched_family": {}}
    for label, (a, b) in {
        "multisignal_vs_inferred": ("cam_inferred", "cam_multisignal"),
        "ms_learned_vs_learned": ("cam_learned", "cam_multisignal_learned"),
        "cam_multisignal_vs_ncc_intent": ("ncc_intent_only", "cam_multisignal"),
    }.items():
        profit = per_seed["total_profit"]
        da, db = np.asarray(profit[a], dtype=float), np.asarray(profit[b], dtype=float)
        diffs = db - da
        mean_diff, lo, hi, se_boot = paired_bootstrap_ci(diffs)
        n = len(diffs); sd = float(diffs.std(ddof=1))
        t_stat = mean_diff / (sd / np.sqrt(n)) if sd > 0 else None
        dz = mean_diff / sd if sd > 0 else None
        s = compute_statistics(list(da), list(db))
        results["paired_contrasts"][label] = {
            "a": a, "b": b, "mean_a": round(float(da.mean()), 2),
            "mean_b": round(float(db.mean()), 2), "mean_diff": round(mean_diff, 2),
            "sd_diff": round(sd, 2), "t": round(t_stat, 2) if t_stat else None,
            "p": s.get("p_value") if s else None,
            "d_z": round(dz, 3) if dz else None,
            "boot_ci95": [round(lo, 2), round(hi, 2)], "boot_se": round(se_boot, 2)}
    print("[2/3] Context-blind policy search (6 policies, default env) ...")
    cb_agents = [n for n, _, _, _ in CB_POLICIES] + ["cam_multisignal"]
    cb_agg, _, _, _, _ = run_env(None, seeds=SEEDS, scenarios=N_SCEN, agent_names=cb_agents)
    results["policy_search"] = {n: {"match_rate": cb_agg[n].get("context_match_rate_mean", 0),
                                     "profit": cb_agg[n].get("total_profit_mean", 0)} for n in cb_agents}
    print("[3/3] 9-environment comparison: cb_edu_email_030 vs cam_multisignal ...")
    env_results = {}
    for env_name, overrides in ENVIRONMENT_PRESETS.items():
        env_agg, _, _, _, _ = run_env(overrides, seeds=SEEDS, scenarios=N_SCEN,
                                      agent_names=["cam_multisignal", "cb_edu_email_030"])
        env_results[env_name] = {"cam_multisignal": env_agg["cam_multisignal"].get("total_profit_mean", 0),
                                 "cb_edu_email_030": env_agg["cb_edu_email_030"].get("total_profit_mean", 0)}
    wins = sum(1 for v in env_results.values() if v["cb_edu_email_030"] > v["cam_multisignal"])
    results["env_comparison"] = env_results
    results["env_wins"] = f"{wins} of {len(env_results)}"
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "cam_sim_ablations.json").write_text(json.dumps(results, indent=2, default=str) + "\n")
    lines = ["# CAM-Sim Ablations", "", f"- Seeds: {len(SEEDS)} x {N_SCEN} scenarios",
             f"- Bootstrap: B={B_BOOT}, paired differences, seed={SEED_BOOT}", "",
             "## Agents (ablation ladder)", "| Agent | Match rate | Profit |", "|---|---|---|"]
    for name in agents:
        if name in aggregate:
            a = aggregate[name]
            lines.append(f"| {name} | {a.get('context_match_rate_mean', 0):.1f} | {a.get('total_profit_mean', 0):+.2f} |")
    lines += ["", "## Paired contrasts (bootstrap on paired differences)",
              "| Contrast | mean diff | 95% CI | t | p | d_z |", "|---|---|---|---|---|---|"]
    for label, c in results["paired_contrasts"].items():
        p_str = f"{c['p']:.2e}" if c["p"] else "---"
        lines.append(f"| {label} | {c['mean_diff']:+.2f} | [{c['boot_ci95'][0]:+.2f}, {c['boot_ci95'][1]:+.2f}] | {c['t']} | {p_str} | {c['d_z']} |")
    lines += ["", "## Context-blind policy search (sec 8.7)",
              "| Policy | Match rate | Profit |", "|---|---|---|"]
    for n in cb_agents:
        ps = results["policy_search"][n]
        lines.append(f"| {n} | {ps['match_rate']:.1f} | {ps['profit']:+.2f} |")
    lines += ["", "## 9-environment comparison (cb_edu_email_030 vs cam_multisignal)",
              "| Environment | cb_edu_email_030 | cam_multisignal | Winner |", "|---|---|---|---|"]
    for env_name, v in env_results.items():
        w = "cb_email" if v["cb_edu_email_030"] > v["cam_multisignal"] else "cam_multisignal"
        lines.append(f"| {env_name} | {v['cb_edu_email_030']:+.2f} | {v['cam_multisignal']:+.2f} | {w} |")
    lines.append(f"| **Total** | | | **cb_email wins {wins} of {len(env_results)}** |")
    (OUT / "cam_sim_ablations.md").write_text("\n".join(lines) + "\n")
    print(f"Wrote {OUT / 'cam_sim_ablations.json'}")
    print(f"Wrote {OUT / 'cam_sim_ablations.md'}")
    for label, c in results["paired_contrasts"].items():
        p_str = f"p={c['p']:.2e}" if c["p"] else ""
        print(f"  {label}: {c['mean_diff']:+.2f} CI [{c['boot_ci95'][0]:+.2f}, {c['boot_ci95'][1]:+.2f}] {p_str}")
    ps = results["policy_search"]
    print(f"  cb_edu_email_030: {ps['cb_edu_email_030']['profit']:+.2f} vs cam_multisignal: {ps['cam_multisignal']['profit']:+.2f}")
    print(f"  9-env: cb_email wins {wins} of {len(env_results)}")

if __name__ == "__main__":
    main()
