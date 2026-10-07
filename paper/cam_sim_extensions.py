#!/usr/bin/env python3
"""CAM-Sim extensions: 8 experiments for the remaining simulatable referee items.

8. Channel-dependent reward (10.3 #20): channel_mismatch_penalty=0.5 kills the
   EMAIL arbitrage. 9. Adversarial mapping (10.3 #3): perfect classification +
   deranged action mapping separates classification value from mapping value.
10. Contextual bandits (10.3 #12): offline eps-greedy + LinUCB-style profit
    model. 11. Class-conditional label noise (10.3 #13): crisis<->decision,
    retention<->exploration confusion. 12. Convergence trend test (9.2 #17):
    Spearman + Geweke. 13. Perception-only dose-response (10.3 #4): flat bid,
    vary p. 14. Crisis bid policy (10.3 #17): pause/normal/counter(2x default).
15. Sensing fidelity (10.3 #18): real channel_quality in signals; results must
    be identical (classifiers read context scalars, not the signals list).

Usage: python paper/cam_sim_extensions.py
Self-contained: imports from paper/cam_sim.py only. Deterministic (except
eps-greedy / FixedBidNoisyCAM decision noise, seeded per seed by run_env).
"""
import json, random, sys
from pathlib import Path
import numpy as np
from scipy.stats import spearmanr
sys.path.insert(0, str(Path(__file__).parent))
from cam_sim import (Action, ActionType, AGENT_REGISTRY, Agent, CAMMultisignal,
    CAMMultisignalLearned, CAMOracle, ChannelType, ENVIRONMENT_PRESETS,
    IDEAL_ACTION, SITUATION_CHANNEL, SimulationEnvironment, SituationType,
    compute_statistics, fit_multisignal_classifier, run_env)

SEEDS = list(range(1, 51)); N_SCEN = 200
OUT = Path(__file__).resolve().parent.parent / "results"
IDEAL_ACTION_INV = {v: k for k, v in IDEAL_ACTION.items()}

class ContextBlindAgent(Agent):
    """Fixed (action, channel, bid) policy."""
    def __init__(self, action_type, channel, bid, name):
        super().__init__(name); self._at = action_type; self._ch = channel; self._bid = bid
    def decide(self, context):
        self.actions_taken += 1
        return Action(self.actions_taken, self._at, self._ch, self._bid)

ADVERSARIAL_ACTION = {
    SituationType.EXPLORATION: ActionType.PROMOTIONAL,
    SituationType.CONSIDERATION: ActionType.CRISIS_RESPONSE,
    SituationType.DECISION: ActionType.EDUCATIONAL,
    SituationType.CRISIS: ActionType.LOYALTY,
    SituationType.OPPORTUNITY: ActionType.COMPARISON,
    SituationType.RETENTION: ActionType.URGENT,
}

class AdversarialMappingAgent(Agent):
    """Perfect 3-signal classification but a deranged action mapping (9.2 #1)."""
    def __init__(self, name="adv_map_ms"):
        super().__init__(name); self._inner = CAMMultisignal()
    def decide(self, context):
        self.actions_taken += 1
        a = self._inner.decide(context)
        classified = IDEAL_ACTION_INV[a.action_type]
        return Action(self.actions_taken, ADVERSARIAL_ACTION[classified], a.channel, a.bid)

class CrisisPolicyAgent(Agent):
    """cam_multisignal with variant crisis bid multiplier (9.2 #23).
    mult: 0=pause, 1=normal (no 2x), 2=counter (current default)."""
    def __init__(self, mult, name):
        super().__init__(name); self._inner = CAMMultisignal(); self._mult = mult
    def decide(self, context):
        a = self._inner.decide(context); self.actions_taken += 1
        if context.situation == SituationType.CRISIS:
            return Action(self.actions_taken, a.action_type, a.channel,
                          round(a.bid * self._mult / 2.0, 2))
        return Action(self.actions_taken, a.action_type, a.channel, a.bid)

class FixedBidNoisyCAM(Agent):
    """NoisyCAM with flat bid=1.0: perception p isolated from bid policy (9.2 #4)."""
    def __init__(self, p_correct, name):
        super().__init__(name); self._p = p_correct
    def decide(self, context):
        self.actions_taken += 1
        if random.random() < self._p: sit = context.situation
        else: sit = random.choice(list(SituationType))
        return Action(self.actions_taken, IDEAL_ACTION[sit], SITUATION_CHANNEL[sit], 1.0)


CONFUSABLE = {
    SituationType.DECISION: SituationType.CRISIS, SituationType.CRISIS: SituationType.DECISION,
    SituationType.RETENTION: SituationType.EXPLORATION, SituationType.EXPLORATION: SituationType.RETENTION,
}

def fit_ms_classcond(eps, calib_seed=999_999, n=2000):
    """Multi-signal NCC fit under class-conditional noise (10.3 #13).
    Only crisis<->decision and retention<->exploration are corrupted; consideration
    and opportunity keep clean labels."""
    env2 = SimulationEnvironment(seed=calib_seed)
    rng = np.random.RandomState(calib_seed + 1); samples = []
    for _ in range(n):
        c = env2.generate_context(); sit = c.situation
        if eps > 0 and sit in CONFUSABLE and rng.random_sample() < eps:
            sit = CONFUSABLE[sit]
        samples.append((c.audience_intent_strength, c.competitive_density, c.channel_quality, sit))
    return fit_multisignal_classifier(samples)


class EpsilonGreedyAgent(Agent):
    """eps-greedy: classify via 3-signal NCC, then Q-argmax (== ideal action) with
    eps-random exploration. Q-argmax is the ideal action by construction (BASE_REWARDS
    maximized), so this measures the exploration tax vs cam_multisignal (10.3 #12)."""
    def __init__(self, eps=0.1, name="eps_greedy_010"):
        super().__init__(name); self._clf = CAMMultisignal(); self._engine = CAMOracle(name + "_e"); self._eps = eps
    def decide(self, context):
        self.actions_taken += 1
        ideal = self._clf.decide(context)
        if random.random() < self._eps:
            at = random.choice(list(ActionType))
        else:
            at = ideal.action_type
        sit = IDEAL_ACTION_INV[at]
        return Action(self.actions_taken, at, SITUATION_CHANNEL[sit], round(self._engine._bid(sit, context), 2))


class ProfitModelAgent(Agent):
    """LinUCB-style offline profit model: ridge regression per action-type arm on
    (1, intent, comp, qual) -> profit from calibration rollouts (10.3 #12).
    Picks argmax predicted profit; channel/bid from inverse-mapped situation."""
    def __init__(self, models, name="linucb_profit"):
        super().__init__(name); self._models = models; self._engine = CAMOracle(name + "_e")
    def decide(self, context):
        self.actions_taken += 1
        x = np.array([1.0, context.audience_intent_strength, context.competitive_density, context.channel_quality])
        preds = {at: float(self._models[at].predict(x.reshape(1, -1))[0]) for at in ActionType}
        at = max(preds, key=preds.get)
        sit = IDEAL_ACTION_INV[at]
        return Action(self.actions_taken, at, SITUATION_CHANNEL[sit], round(self._engine._bid(sit, context), 2))


def fit_profit_models(calib_seed=999_999, n=2000):
    """Evaluate all 6 action types on calibration contexts; fit ridge per arm."""
    from sklearn.linear_model import Ridge
    env2 = SimulationEnvironment(seed=calib_seed)
    X = {at: [] for at in ActionType}; y = {at: [] for at in ActionType}
    for _ in range(n):
        c = env2.generate_context()
        feats = [1.0, c.audience_intent_strength, c.competitive_density, c.channel_quality]
        ch = SITUATION_CHANNEL[c.situation]
        for at in ActionType:
            r = env2.evaluate_action(c, Action(0, at, ch, 1.0))
            X[at].append(feats); y[at].append(r.reward + r.long_term_value - r.cost)
    return {at: Ridge().fit(np.array(X[at]), np.array(y[at])) for at in ActionType}


def geweke_z(vals, first=0.2, last=0.5):
    a = np.asarray(vals[:int(len(vals) * first)], dtype=float)
    b = np.asarray(vals[-int(len(vals) * last):], dtype=float)
    return float((a.mean() - b.mean()) / np.sqrt(a.var(ddof=1) / len(a) + b.var(ddof=1) / len(b)))


def main():
    results = {}
    AGENT_REGISTRY["cb_edu_email_030"] = lambda: ContextBlindAgent(ActionType.EDUCATIONAL, ChannelType.EMAIL, 0.30, "cb_edu_email_030")
    AGENT_REGISTRY["adv_map_ms"] = AdversarialMappingAgent
    AGENT_REGISTRY["crisis_pause"] = lambda: CrisisPolicyAgent(0.0, "crisis_pause")
    AGENT_REGISTRY["crisis_normal"] = lambda: CrisisPolicyAgent(1.0, "crisis_normal")
    AGENT_REGISTRY["crisis_counter"] = lambda: CrisisPolicyAgent(2.0, "crisis_counter")
    for e in (0.1, 0.2, 0.3):
        c = fit_ms_classcond(e); tag = f"ms_cc{int(e*100)}"
        AGENT_REGISTRY[tag] = (lambda cc=c, nn=tag: CAMMultisignalLearned(cc, nn))
    AGENT_REGISTRY["eps_greedy_010"] = EpsilonGreedyAgent
    pm = fit_profit_models()
    AGENT_REGISTRY["linucb_profit"] = (lambda m=pm: ProfitModelAgent(m))
    fb_names = {}
    for p in (0.5, 0.6, 0.7, 0.8, 0.9, 1.0):
        n = f"fixedbid_p{int(p*100)}"; AGENT_REGISTRY[n] = (lambda pp=p, nn=n: FixedBidNoisyCAM(pp, nn)); fb_names[p] = n

    # [1/8] Channel-dependent reward
    print("[1/8] Channel-dependent reward (penalty=0.5) ...")
    ag8 = ["cb_edu_email_030", "cam_multisignal", "cam_learned", "situation_only", "oracle"]
    d_def, _, _, _, _ = run_env(None, seeds=SEEDS, scenarios=N_SCEN, agent_names=ag8)
    d_cd, _, _, _, _ = run_env({"channel_mismatch_penalty": 0.5}, seeds=SEEDS, scenarios=N_SCEN, agent_names=ag8)
    results["channel_dependent"] = {n: {"default_profit": round(d_def[n]["total_profit_mean"], 2),
        "channel_dep_profit": round(d_cd[n]["total_profit_mean"], 2),
        "default_match": round(d_def[n]["context_match_rate_mean"], 1),
        "channel_dep_match": round(d_cd[n]["context_match_rate_mean"], 1)} for n in ag8}

    # [2/8] Adversarial-mapping condition
    print("[2/8] Adversarial-mapping condition ...")
    ag9 = ["adv_map_ms", "cam_multisignal", "baseline"]
    a9, _, ps9, _, _ = run_env(None, seeds=SEEDS, scenarios=N_SCEN, agent_names=ag9)
    results["adversarial_mapping"] = {n: {"match": round(a9[n]["context_match_rate_mean"], 1),
        "profit": round(a9[n]["total_profit_mean"], 2)} for n in ag9}
    st = compute_statistics(list(ps9["total_profit"]["adv_map_ms"]), list(ps9["total_profit"]["cam_multisignal"]))
    results["adversarial_mapping"]["contrast_ms_vs_adv"] = {"diff": round(st["diff_mean"], 2),
        "p_value": st["p_value"], "cohens_d": st["effect_size_cohens_d"]}

    # [3/8] Contextual-bandit baselines
    print("[3/8] Contextual-bandit baselines (eps-greedy, LinUCB-style) ...")
    ag10 = ["eps_greedy_010", "linucb_profit", "cam_multisignal", "cam_learned"]
    a10, _, ps10, _, _ = run_env(None, seeds=SEEDS, scenarios=N_SCEN, agent_names=ag10)
    results["bandits"] = {n: {"match": round(a10[n]["context_match_rate_mean"], 1),
        "profit": round(a10[n]["total_profit_mean"], 2)} for n in ag10}
    for lbl, x, y in [("linucb_vs_ms", "cam_multisignal", "linucb_profit"),
                      ("eps_vs_ms", "cam_multisignal", "eps_greedy_010")]:
        st = compute_statistics(list(ps10["total_profit"][x]), list(ps10["total_profit"][y]))
        results["bandits"][lbl] = {"diff": round(st["diff_mean"], 2), "p_value": st["p_value"], "cohens_d": st["effect_size_cohens_d"]}

    # [4/8] Class-conditional label noise
    print("[4/8] Class-conditional label noise ...")
    ag11 = ["ms_cc10", "ms_cc20", "ms_cc30", "cam_multisignal_learned"]
    a11, _, ps11, _, _ = run_env(None, seeds=SEEDS, scenarios=N_SCEN, agent_names=ag11)
    results["class_cond_noise"] = {n: {"match": round(a11[n]["context_match_rate_mean"], 1),
        "profit": round(a11[n]["total_profit_mean"], 2)} for n in ag11}
    st = compute_statistics(list(ps11["total_profit"]["cam_multisignal_learned"]), list(ps11["total_profit"]["ms_cc30"]))
    results["class_cond_noise"]["cc30_vs_clean"] = {"diff": round(st["diff_mean"], 2), "p_value": st["p_value"], "cohens_d": st["effect_size_cohens_d"]}

    # [5/8] Convergence trend test (Spearman + Geweke)
    print("[5/8] Convergence trend test (Spearman + Geweke) ...")
    ag12 = ["cam_multisignal", "baseline", "cam_learned"]
    _, _, ps12, _, _ = run_env(None, seeds=SEEDS, scenarios=N_SCEN, agent_names=ag12)
    results["convergence_trend"] = {}
    for n in ag12:
        v = ps12["total_profit"][n]
        rho, pv = spearmanr(range(len(v)), v)
        results["convergence_trend"][n] = {"spearman_rho": round(float(rho), 3),
            "spearman_p": float(pv), "geweke_z": round(geweke_z(v), 2)}

    # [6/8] Perception-only dose-response (flat bid, vary p)
    print("[6/8] Perception-only dose-response (flat bid, vary p) ...")
    fb = [fb_names[p] for p in (0.5, 0.6, 0.7, 0.8, 0.9, 1.0)]
    a13, _, ps13, _, _ = run_env(None, seeds=SEEDS, scenarios=N_SCEN, agent_names=fb)
    results["perception_dose"] = {n: {"p": int(n.split("p")[1]) / 100,
        "match": round(a13[n]["context_match_rate_mean"], 1),
        "profit": round(a13[n]["total_profit_mean"], 2)} for n in fb}
    profits_by_p = {p: ps13["total_profit"][fb_names[p]] for p in sorted(fb_names)}
    per_seed_rho = [spearmanr(list(profits_by_p.keys()),
        [profits_by_p[p][s] for p in profits_by_p])[0] for s in range(len(SEEDS))]
    results["perception_dose"]["_meta"] = {"per_seed_rho_mean": round(float(np.mean(per_seed_rho)), 3),
        "per_seed_rho_min": round(float(np.min(per_seed_rho)), 3)}

    # [7/8] Crisis bid policy (pause/normal/counter) in default + crisis_heavy
    print("[7/8] Crisis bid policy (pause/normal/counter) ...")
    ag14 = ["crisis_pause", "crisis_normal", "crisis_counter"]
    results["crisis_policy"] = {}
    for env_name, cfg in [("default", None), ("crisis_heavy", ENVIRONMENT_PRESETS["crisis_heavy"])]:
        a14, _, _, _, _ = run_env(cfg, seeds=SEEDS, scenarios=N_SCEN, agent_names=ag14)
        results["crisis_policy"][env_name] = {n: round(a14[n]["total_profit_mean"], 2) for n in ag14}

    # [8/8] Sensing-layer fidelity (real channel_quality in signals)
    print("[8/8] Sensing-layer fidelity (real channel_quality in signals) ...")
    ag15 = ["cam_multisignal", "cam_multisignal_learned", "cam_learned", "cam_inferred"]
    a15d, _, _, _, _ = run_env(None, seeds=SEEDS, scenarios=N_SCEN, agent_names=ag15)
    a15f, _, _, _, _ = run_env({"sensing_fidelity": True}, seeds=SEEDS, scenarios=N_SCEN, agent_names=ag15)
    results["sensing_fidelity"] = {n: {"default_profit": round(a15d[n]["total_profit_mean"], 2),
        "fidelity_profit": round(a15f[n]["total_profit_mean"], 2)} for n in ag15}

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "cam_sim_extensions.json").write_text(json.dumps(results, indent=2, default=str) + "\n")

    md = ["# CAM-Sim Extensions (paper v1.3)", "",
          f"{len(SEEDS)} seeds x {N_SCEN} scenarios. Generated by paper/cam_sim_extensions.py.", ""]
    md += ["## 1. Channel-dependent reward (mismatch penalty 0.5)", "",
           "| Agent | default | channel-dep |", "|---|---|---|"]
    md += [f"| {n} | {v['default_profit']:+.2f} | {v['channel_dep_profit']:+.2f} |"
           for n, v in results["channel_dependent"].items()]
    md += ["", "## 2. Adversarial mapping", "", "| Agent | Match % | Profit |", "|---|---|---|"]
    md += [f"| {n} | {v['match']} | {v['profit']:+.2f} |"
           for n, v in results["adversarial_mapping"].items() if isinstance(v, dict) and "match" in v]
    c = results["adversarial_mapping"]["contrast_ms_vs_adv"]
    md.append(f"Contrast (ms - adv): +${c['diff']:.2f}, p={c['p_value']:.2e}, d={c['cohens_d']}")
    md += ["", "## 3. Bandit baselines", "", "| Agent | Match % | Profit |", "|---|---|---|"]
    md += [f"| {n} | {v['match']} | {v['profit']:+.2f} |"
           for n, v in results["bandits"].items() if isinstance(v, dict) and "match" in v]
    for lbl in ["linucb_vs_ms", "eps_vs_ms"]:
        c = results["bandits"][lbl]
        md.append(f"{lbl}: diff={c['diff']:+.2f}, p={c['p_value']:.2e}, d={c['cohens_d']}")
    md += ["", "## 4. Class-conditional noise", "", "| Agent | Match % | Profit |", "|---|---|---|"]
    md += [f"| {n} | {v['match']} | {v['profit']:+.2f} |"
           for n, v in results["class_cond_noise"].items() if isinstance(v, dict) and "match" in v]
    c = results["class_cond_noise"]["cc30_vs_clean"]
    md.append(f"cc30 vs clean: diff={c['diff']:+.2f}, p={c['p_value']:.2e}, d={c['cohens_d']}")
    md += ["", "## 5. Convergence trend", "", "| Agent | rho | p | Geweke z |", "|---|---|---|---|"]
    md += [f"| {n} | {v['spearman_rho']} | {v['spearman_p']:.3f} | {v['geweke_z']} |"
           for n, v in results["convergence_trend"].items()]
    md += ["", "## 6. Perception dose (flat bid)", "", "| p | Match % | Profit |", "|---|---|---|"]
    md += [f"| {v['p']} | {v['match']} | {v['profit']:+.2f} |"
           for n, v in results["perception_dose"].items() if isinstance(v, dict) and "p" in v]
    meta = results["perception_dose"]["_meta"]
    md.append(f"Per-seed rho(profit, p): mean {meta['per_seed_rho_mean']}, min {meta['per_seed_rho_min']}")
    md += ["", "## 7. Crisis bid policy", "", "| Env | pause | normal | counter |", "|---|---|---|---|"]
    md += [f"| {e} | {v['crisis_pause']:+.2f} | {v['crisis_normal']:+.2f} | {v['crisis_counter']:+.2f} |"
           for e, v in results["crisis_policy"].items()]
    md += ["", "## 8. Sensing fidelity", "", "| Agent | default | fidelity |", "|---|---|---|"]
    md += [f"| {n} | {v['default_profit']:+.2f} | {v['fidelity_profit']:+.2f} |"
           for n, v in results["sensing_fidelity"].items()]
    (OUT / "cam_sim_extensions.md").write_text("\n".join(md) + "\n")
    print("Wrote", OUT / "cam_sim_extensions.json")
    print("Wrote", OUT / "cam_sim_extensions.md")


if __name__ == "__main__":
    main()
