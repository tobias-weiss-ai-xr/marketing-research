#!/usr/bin/env python3
"""CAM-Sim ablations: 7 experiments.

1. Majority-action floor: always-EDUCATIONAL, flat bid.
2. Matched-family ablation: NCC on intent-only vs NCC on 3 signals.
3. Paired-difference bootstrap B=2000 (bootstraps paired diffs, not marginals).
4. Context-blind policy search: constant (action, channel, bid) policies (round-4 adversarial).
5. Standard classifier baselines: LR and RF on 1-signal and 3-signal (closes §9.2 #13).
6. Macro-F1: per-class F1 for all classifier agents (closes §9.2 #11).
7. CRN comparison: per-agent RNG vs shared RNG (closes §9.2 #10).

Usage: python paper/cam_sim_ablations.py
Self-contained: imports from paper/cam_sim.py only. Deterministic.
"""
import json, sys, random
from pathlib import Path
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
sys.path.insert(0, str(Path(__file__).parent))
from cam_sim import (Action, ActionType, AGENT_REGISTRY, Agent, CAMOracle, ChannelType,
    ENVIRONMENT_PRESETS, FullContext, IDEAL_ACTION, SITUATION_CHANNEL,
    SimulationEnvironment, SituationType, compute_statistics, run_env,
    BaselineAgent, NoisyCAM, BenchmarkRunner)

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

# --- Standard classifier baselines (LR, RF) — closes §9.2 #13, §10.3 #11 ---
SITUATIONS = list(SituationType)
SIT_TO_IDX = {s: i for i, s in enumerate(SITUATIONS)}
IDX_TO_SIT = {i: s for i, s in enumerate(SITUATIONS)}
IDEAL_ACTION_INV = {v: k for k, v in IDEAL_ACTION.items()}

class SKLearnAgent(Agent):
    """Classifier-based agent (LR or RF). Same action mapping as cam_multisignal."""
    def __init__(self, classifier, signal_count, name):
        super().__init__(name)
        self._clf = classifier
        self._n = signal_count
        self._engine = CAMOracle(name + "_engine")
    def classify(self, intent, comp, qual):
        X = [[intent] if self._n == 1 else [intent, comp, qual]]
        return IDX_TO_SIT[int(self._clf.predict(X)[0])]
    def decide(self, context):
        self.actions_taken += 1
        situation = self.classify(context.audience_intent_strength,
                                  context.competitive_density,
                                  context.channel_quality)
        action_type = IDEAL_ACTION[situation]
        channel = SITUATION_CHANNEL[situation]
        bid = self._engine._bid(situation, context)
        return Action(self.actions_taken, action_type, channel, round(bid, 2))

def fit_sklearn(clf_class, signal_count, calib_seed=999_999, n=2000):
    """Fit sklearn classifier on calibration sample (same 2000-sample protocol as NCC learners)."""
    cfg = dict(ENVIRONMENT_PRESETS["default"])
    env2 = SimulationEnvironment(seed=calib_seed, config=cfg)
    X, y = [], []
    for _ in range(n):
        c = env2.generate_context()
        if signal_count == 1:
            X.append([c.audience_intent_strength])
        else:
            X.append([c.audience_intent_strength, c.competitive_density, c.channel_quality])
        y.append(SIT_TO_IDX[c.situation])
    clf = clf_class(random_state=calib_seed)
    if clf_class is LogisticRegression:
        clf = clf_class(random_state=calib_seed, max_iter=2000)
    clf.fit(X, y)
    return clf

# --- CRN (Common Random Numbers) agents — closes §9.2 #10, §10.3 #5 ---
class CRNBaselineAgent(Agent):
    """BaselineAgent with per-agent RNG (CRN). Only BaselineAgent and NoisyCAM use random in decide()."""
    BASE_BIDS = {ChannelType.SEARCH: 1.50, ChannelType.SOCIAL: 1.00, ChannelType.DISPLAY: 0.80,
                 ChannelType.EMAIL: 0.10, ChannelType.VIDEO: 2.00}
    DEFAULT_ACTIONS = {ChannelType.SEARCH: ActionType.EDUCATIONAL, ChannelType.SOCIAL: ActionType.EDUCATIONAL,
                       ChannelType.DISPLAY: ActionType.PROMOTIONAL, ChannelType.EMAIL: ActionType.LOYALTY,
                       ChannelType.VIDEO: ActionType.PROMOTIONAL}
    def __init__(self, seed):
        super().__init__("crn_baseline")
        self._rng = random.Random(seed * 1000 + 99)
    def decide(self, context):
        self.actions_taken += 1
        channel = self._rng.choice(list(ChannelType))
        bid = max(0.01, self.BASE_BIDS[channel] * self._rng.uniform(0.8, 1.2))
        return Action(self.actions_taken, self.DEFAULT_ACTIONS[channel], channel, round(bid, 2))

class CRNNoisyCAM(Agent):
    """NoisyCAM with per-agent RNG (CRN)."""
    def __init__(self, p_correct, name, seed):
        super().__init__(name)
        self._p = p_correct
        self._rng = random.Random(seed * 1000 + 98)
        self._engine = CAMOracle(name + "_engine")
    def decide(self, context):
        self.actions_taken += 1
        if self._rng.random() < self._p:
            situation = context.situation
        else:
            situation = self._rng.choice(list(SituationType))
        action_type = IDEAL_ACTION[situation]
        channel = SITUATION_CHANNEL[situation]
        bid = self._engine._bid(situation, context)
        return Action(self.actions_taken, action_type, channel, round(bid, 2))

# --- Macro-F1 — closes §9.2 #11, §10.3 #6 ---
def compute_macro_f1(agent, contexts):
    """Compute macro-F1 for a classifier agent on a set of contexts."""
    y_true, y_pred = [], []
    agent.reset()
    for ctx in contexts:
        action = agent.decide(ctx)
        pred_sit = IDEAL_ACTION_INV[action.action_type]
        y_true.append(SIT_TO_IDX[ctx.situation])
        y_pred.append(SIT_TO_IDX[pred_sit])
    return f1_score(y_true, y_pred, average='macro', zero_division=0)

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
    print(f"[1/7] Ablation ladder: {len(agents)} agents, {len(SEEDS)} seeds x {N_SCEN} ...")
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
    print("[2/7] Context-blind policy search (6 policies, default env) ...")
    cb_agents = [n for n, _, _, _ in CB_POLICIES] + ["cam_multisignal"]
    cb_agg, _, _, _, _ = run_env(None, seeds=SEEDS, scenarios=N_SCEN, agent_names=cb_agents)
    results["policy_search"] = {n: {"match_rate": cb_agg[n].get("context_match_rate_mean", 0),
                                     "profit": cb_agg[n].get("total_profit_mean", 0)} for n in cb_agents}
    print("[3/7] 9-environment comparison: cb_edu_email_030 vs cam_multisignal ...")
    env_results = {}
    for env_name, overrides in ENVIRONMENT_PRESETS.items():
        env_agg, _, _, _, _ = run_env(overrides, seeds=SEEDS, scenarios=N_SCEN,
                                      agent_names=["cam_multisignal", "cb_edu_email_030"])
        env_results[env_name] = {"cam_multisignal": env_agg["cam_multisignal"].get("total_profit_mean", 0),
                                 "cb_edu_email_030": env_agg["cb_edu_email_030"].get("total_profit_mean", 0)}
    wins = sum(1 for v in env_results.values() if v["cb_edu_email_030"] > v["cam_multisignal"])
    results["env_comparison"] = env_results
    results["env_wins"] = f"{wins} of {len(env_results)}"

    # --- Experiment 5: Standard classifier baselines (LR, RF) ---
    print("[4/7] Standard classifier baselines (LR, RF on 1-signal and 3-signal) ...")
    lr1 = fit_sklearn(LogisticRegression, 1)
    lr3 = fit_sklearn(LogisticRegression, 3)
    rf1 = fit_sklearn(RandomForestClassifier, 1)
    rf3 = fit_sklearn(RandomForestClassifier, 3)
    AGENT_REGISTRY["lr_intent_only"] = (lambda clf=lr1: SKLearnAgent(clf, 1, "lr_intent_only"))
    AGENT_REGISTRY["lr_multisignal"] = (lambda clf=lr3: SKLearnAgent(clf, 3, "lr_multisignal"))
    AGENT_REGISTRY["rf_intent_only"] = (lambda clf=rf1: SKLearnAgent(clf, 1, "rf_intent_only"))
    AGENT_REGISTRY["rf_multisignal"] = (lambda clf=rf3: SKLearnAgent(clf, 3, "rf_multisignal"))
    sklearn_agents = ["lr_intent_only", "lr_multisignal", "rf_intent_only", "rf_multisignal",
                      "cam_learned", "cam_multisignal", "cam_multisignal_learned", "ncc_intent_only"]
    sk_agg, _, sk_per_seed, _, _ = run_env(None, seeds=SEEDS, scenarios=N_SCEN, agent_names=sklearn_agents)
    results["standard_baselines"] = {n: {"match_rate": sk_agg[n].get("context_match_rate_mean", 0),
                                          "profit": sk_agg[n].get("total_profit_mean", 0)} for n in sklearn_agents}
    for label, (a, b) in {
        "lr3_vs_ms": ("cam_multisignal", "lr_multisignal"),
        "lr1_vs_learned": ("cam_learned", "lr_intent_only"),
        "lr3_vs_lr1": ("lr_intent_only", "lr_multisignal"),
        "rf3_vs_rf1": ("rf_intent_only", "rf_multisignal"),
        "rf3_vs_ms": ("cam_multisignal", "rf_multisignal"),
    }.items():
        profit = sk_per_seed["total_profit"]
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

    # --- Experiment 6: Macro-F1 ---
    print("[5/7] Macro-F1 for all classifier agents ...")
    env1 = SimulationEnvironment(seed=1)
    contexts_f1 = [env1.generate_context() for _ in range(N_SCEN)]
    f1_agent_names = ["ncc_intent_only", "cam_inferred", "cam_learned", "cam_multisignal",
                      "cam_multisignal_learned", "lr_intent_only", "lr_multisignal",
                      "rf_intent_only", "rf_multisignal"]
    f1_results = {}
    for name in f1_agent_names:
        agent = AGENT_REGISTRY[name]()
        f1 = compute_macro_f1(agent, contexts_f1)
        f1_results[name] = round(f1, 4)
    results["macro_f1"] = f1_results

    # --- Experiment 7: CRN comparison ---
    print("[6/7] CRN comparison (per-agent RNG vs shared RNG) ...")
    crn_compare = ["baseline", "noisy50", "noisy80"]
    crn_seeds = list(range(1, 51))
    crn_per_seed = {n: [] for n in crn_compare + ["crn_baseline", "crn_noisy50", "crn_noisy80"]}
    for seed in crn_seeds:
        random.seed(seed)
        env = SimulationEnvironment(seed=seed)
        contexts = [env.generate_context() for _ in range(N_SCEN)]
        runner = BenchmarkRunner(env)
        agents = [("baseline", BaselineAgent()), ("crn_baseline", CRNBaselineAgent(seed)),
                  ("noisy50", NoisyCAM(0.5, "noisy50")), ("crn_noisy50", CRNNoisyCAM(0.5, "crn_noisy50", seed)),
                  ("noisy80", NoisyCAM(0.8, "noisy80")), ("crn_noisy80", CRNNoisyCAM(0.8, "crn_noisy80", seed))]
        results_run = runner.run_benchmark([a for _, a in agents], contexts, budget=None)
        metrics = runner.get_metrics(results_run)
        for name in crn_compare + ["crn_baseline", "crn_noisy50", "crn_noisy80"]:
            crn_per_seed[name].append(metrics[name]["total_profit"])
    results["crn_comparison"] = {n: {"shared_rng_profit": round(float(np.mean(crn_per_seed[n])), 2),
                                     "crn_profit": round(float(np.mean(crn_per_seed["crn_" + n])), 2),
                                     "diff": round(float(np.mean(crn_per_seed["crn_" + n]) - np.mean(crn_per_seed[n])), 2)}
                                  for n in crn_compare}

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
    # Standard baselines
    lines += ["", "## Standard classifier baselines (sec 8.8)",
              "| Agent | Match rate | Profit |", "|---|---|---|"]
    for n in sklearn_agents:
        sb = results["standard_baselines"][n]
        lines.append(f"| {n} | {sb['match_rate']:.1f} | {sb['profit']:+.2f} |")
    lines += ["", "## Standard-baseline paired contrasts",
              "| Contrast | mean diff | 95% CI | t | p | d_z |", "|---|---|---|---|---|---|"]
    for label in ["lr3_vs_ms", "lr1_vs_learned", "lr3_vs_lr1", "rf3_vs_rf1", "rf3_vs_ms"]:
        c = results["paired_contrasts"][label]
        p_str = f"{c['p']:.2e}" if c["p"] else "---"
        lines.append(f"| {label} | {c['mean_diff']:+.2f} | [{c['boot_ci95'][0]:+.2f}, {c['boot_ci95'][1]:+.2f}] | {c['t']} | {p_str} | {c['d_z']} |")
    # Macro-F1
    lines += ["", "## Macro-F1 (per-class F1, sec 9.2 #11)",
              "| Agent | Macro-F1 |", "|---|---|"]
    for n, f1 in sorted(f1_results.items(), key=lambda x: -x[1]):
        lines.append(f"| {n} | {f1:.4f} |")
    # CRN comparison
    lines += ["", "## CRN comparison (per-agent RNG vs shared RNG, sec 9.2 #10)",
              "| Agent | Shared RNG profit | CRN profit | Diff |", "|---|---|---|---|"]
    for n, v in results["crn_comparison"].items():
        lines.append(f"| {n} | {v['shared_rng_profit']:+.2f} | {v['crn_profit']:+.2f} | {v['diff']:+.2f} |")
    (OUT / "cam_sim_ablations.md").write_text("\n".join(lines) + "\n")
    print(f"Wrote {OUT / 'cam_sim_ablations.json'}")
    print(f"Wrote {OUT / 'cam_sim_ablations.md'}")
    for label, c in results["paired_contrasts"].items():
        p_str = f"p={c['p']:.2e}" if c["p"] else ""
        print(f"  {label}: {c['mean_diff']:+.2f} CI [{c['boot_ci95'][0]:+.2f}, {c['boot_ci95'][1]:+.2f}] {p_str}")
    ps = results["policy_search"]
    print(f"  cb_edu_email_030: {ps['cb_edu_email_030']['profit']:+.2f} vs cam_multisignal: {ps['cam_multisignal']['profit']:+.2f}")
    print(f"  9-env: cb_email wins {wins} of {len(env_results)}")
    sb = results["standard_baselines"]
    print(f"  LR-1: {sb['lr_intent_only']['match_rate']:.1f}% +${sb['lr_intent_only']['profit']:.2f}  LR-3: {sb['lr_multisignal']['match_rate']:.1f}% +${sb['lr_multisignal']['profit']:.2f}")
    print(f"  RF-1: {sb['rf_intent_only']['match_rate']:.1f}% +${sb['rf_intent_only']['profit']:.2f}  RF-3: {sb['rf_multisignal']['match_rate']:.1f}% +${sb['rf_multisignal']['profit']:.2f}")
    print(f"  Macro-F1: cam_multisignal={f1_results['cam_multisignal']:.4f}  lr_multisignal={f1_results['lr_multisignal']:.4f}  rf_multisignal={f1_results['rf_multisignal']:.4f}")
    crn = results["crn_comparison"]
    print(f"  CRN: baseline {crn['baseline']['diff']:+.2f}  noisy50 {crn['noisy50']['diff']:+.2f}  noisy80 {crn['noisy80']['diff']:+.2f}")

if __name__ == "__main__":
    main()
