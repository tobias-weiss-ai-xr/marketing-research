#!/usr/bin/env python3
"""CAM-Sim v1.4 extensions: online reward-feedback learning, mid-episode
distribution drift, flat-taxonomy confusion quantification.

19. Online learning (closes 10.3 #12 remainder / 9.2 #13): online eps-greedy
    Q-table and UCB1 agents over (estimated situation x action type) learn
    the situation->action mapping from OBSERVED PROFIT alone during the
    episode — no labeled action data. The v1.3 bandit baselines (8.12) were
    offline-trained; the Agent ABC had no reward-feedback loop. Here the
    classifier (hand-set 3-signal NCC, identical to cam_multisignal) provides
    the situation estimate; the Q/UCB layer learns the mapping online. Fair
    comparison: same classifier, same channel rule (SITUATION_CHANNEL[sit_est]),
    same bid rule (oracle-style heuristic bid) — the ONLY difference is
    fixed vs learned action mapping.
20. Mid-episode drift (partial 10.3 #7): contexts 1..n/2 drawn from the
    default distribution, contexts n/2+1..n from crisis_heavy. Extends the
    F5/F6 distribution-shift story from full-episode presets to within-episode
    non-stationarity, with per-half profit decomposition. "Recalibrated"
    agents are fit on the post-drift (crisis_heavy) distribution — the same
    labeled-sample assumption as F6 (8.4).
21. Flat-taxonomy confusion quantification (9.2 #18): confusion matrices of
    the intent-only interval classifier and the 3-signal NCC classifier on
    12,000 fresh default samples, plus per-confusion expected-profit cost
    (playing the predicted situation's full policy under the true situation).
    Quantifies the stage<->condition conflation the limitation predicts.

Also pre-registers (does NOT run — no LLM access in this environment) an
LLM zero-shot classifier baseline protocol; see paper Section 10.3 #24.

Usage: python paper/cam_sim_v14.py
Self-contained: imports from paper/cam_sim.py only. Deterministic (stdlib
random seeded per seed; agent order fixed; numpy env seeded per seed).
"""
import json
import math
import random
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from cam_sim import (Action, ActionType, AGENT_REGISTRY, Agent, CAMLearned,
                     CAMMultisignalLearned, CAMOracle, ENVIRONMENT_PRESETS,
                     IDEAL_ACTION, SITUATION_CHANNEL, SimulationEnvironment,
                     SituationType, compute_statistics, fit_intent_classifier,
                     fit_multisignal_classifier, infer_situation_multisignal)

SEEDS = list(range(1, 51))
N_SCEN = 200
OUT = Path(__file__).resolve().parent.parent / "results"


# ---------------------------------------------------------------------------
# [19] Online reward-feedback learning agents
# ---------------------------------------------------------------------------

class OnlineFeedbackAgent(Agent):
    """Base class: cam_multisignal's classifier/channel/bid + a LEARNED
    action-mapping layer updated from observed profit (no labeled data).

    Mirrors CAMMultisignal.decide exactly except action_type:
      sit_est  = infer_situation_multisignal(intent, comp, qual)   (same)
      channel  = SITUATION_CHANNEL[sit_est]                        (same)
      bid      = oracle-style heuristic bid for sit_est            (same)
      action   = argmax_situation-est Q[action]                    (learned)
    """

    def __init__(self, name, q0=2.5):
        super().__init__(name)
        self._engine = CAMOracle(name + "_e")
        self._q0 = q0
        self.reset()

    def reset(self):
        super().reset()
        self._Q = {s: {a: self._q0 for a in ActionType} for s in SituationType}
        self._n = {s: {a: 0 for a in ActionType} for s in SituationType}
        self._N = 0

    def _sit_est(self, context):
        return infer_situation_multisignal(
            context.audience_intent_strength,
            context.competitive_density,
            context.channel_quality)

    def _choose_action(self, sit_est):
        raise NotImplementedError

    def decide(self, context):
        self.actions_taken += 1
        self._N += 1
        s = self._sit_est(context)
        at = self._choose_action(s)
        return Action(self.actions_taken, at, SITUATION_CHANNEL[s],
                      round(self._engine._bid(s, context), 2))

    def observe(self, context, action, result):
        s = self._sit_est(context)
        a = action.action_type
        profit = result.reward + result.long_term_value - result.cost
        self._n[s][a] += 1
        # incremental sample mean
        self._Q[s][a] += (profit - self._Q[s][a]) / self._n[s][a]


class OnlineEpsQAgent(OnlineFeedbackAgent):
    """eps-greedy over (estimated situation x action type) Q-table with
    optimistic init (q0) and least-tried tie-breaking."""

    def __init__(self, eps=0.1, q0=2.5, name="online_eps_q010"):
        self._eps = eps
        super().__init__(name, q0=q0)

    def _choose_action(self, sit_est):
        if random.random() < self._eps:
            return random.choice(list(ActionType))
        return max(ActionType, key=lambda a: (self._Q[sit_est][a],
                                              -self._n[sit_est][a]))


class OnlineUCBAgent(OnlineFeedbackAgent):
    """UCB1 over (estimated situation x action type) cells."""

    def __init__(self, c=0.5, q0=2.5, name="online_ucb"):
        self._c = c
        super().__init__(name, q0=q0)

    def _choose_action(self, sit_est):
        q = self._Q[sit_est]
        n = self._n[sit_est]
        for a in ActionType:
            if n[a] == 0:
                return a  # play every arm once per sit_est first
        return max(ActionType, key=lambda a: q[a] + self._c * math.sqrt(
            math.log(self._N) / n[a]))


def run_online_env(env_config, seeds, scenarios, agents):
    """BenchmarkRunner.run_benchmark + observe() hook for online agents.

    Pairing is preserved: the context sequence is generated once per seed and
    shared by all agents. Stdlib random is seeded per seed (as in run_env) so
    the whole run is deterministic given the fixed agent order.
    Returns (aggregate, per_seed_profit, per_seed_match).
    """
    per_seed_profit = {a.name: [] for a in agents}
    per_seed_match = {a.name: [] for a in agents}
    for seed in seeds:
        random.seed(seed)
        env = SimulationEnvironment(seed=seed, config=env_config)
        contexts = [env.generate_context() for _ in range(scenarios)]
        for agent in agents:
            agent.reset()
            total_profit = 0.0
            matches = 0
            for context in contexts:
                action = agent.decide(context)
                result = env.evaluate_action(context, action)
                if hasattr(agent, "observe"):
                    agent.observe(context, action, result)
                total_profit += result.reward + result.long_term_value - result.cost
                matches += 1 if result.context_match else 0
            per_seed_profit[agent.name].append(total_profit)
            per_seed_match[agent.name].append(100.0 * matches / len(contexts))
    aggregate = {}
    for name, vals in per_seed_profit.items():
        v = np.asarray(vals)
        m = np.asarray(per_seed_match[name])
        aggregate[name] = {"profit_mean": round(float(v.mean()), 2),
                           "profit_std": round(float(v.std(ddof=1)), 2),
                           "match_mean": round(float(m.mean()), 1)}
    return aggregate, per_seed_profit, per_seed_match


# ---------------------------------------------------------------------------
# [20] Mid-episode distribution drift
# ---------------------------------------------------------------------------

def build_drift_sequence(seed, n_scen):
    """First half: default distribution (env seed = seed).
    Second half: crisis_heavy distribution (env seed = seed + 777001).
    Deterministic; every agent sees the identical sequence."""
    env_a = SimulationEnvironment(seed=seed, config=None)
    env_b = SimulationEnvironment(seed=seed + 777_001,
                                  config=ENVIRONMENT_PRESETS["crisis_heavy"])
    half = n_scen // 2
    return ([env_a.generate_context() for _ in range(half)]
            + [env_b.generate_context() for _ in range(n_scen - half)])


def fit_intent_for_config(cfg_overrides, calib_seed=999_999, n=2000):
    cfg = dict(ENVIRONMENT_PRESETS["default"])
    if cfg_overrides:
        cfg.update(cfg_overrides)
    env = SimulationEnvironment(seed=calib_seed, config=cfg)
    samples = []
    for _ in range(n):
        c = env.generate_context()
        samples.append((c.audience_intent_strength, c.situation))
    return fit_intent_classifier(samples)


def fit_ms_for_config(cfg_overrides, calib_seed=999_999, n=2000):
    cfg = dict(ENVIRONMENT_PRESETS["default"])
    if cfg_overrides:
        cfg.update(cfg_overrides)
    env = SimulationEnvironment(seed=calib_seed, config=cfg)
    samples = []
    for _ in range(n):
        c = env.generate_context()
        samples.append((c.audience_intent_strength, c.competitive_density,
                        c.channel_quality, c.situation))
    return fit_multisignal_classifier(samples)


def run_drift_env(agents, seeds, n_scen):
    """Run agents over the drift sequence; per-half and overall metrics.

    crisis_heavy differs from default ONLY in situation_weights, so a single
    default-config eval env evaluates both halves correctly (reward depends on
    the context's situation and cfg economics, not on the sampling weights)."""
    half = n_scen // 2
    per = {a.name: {"p1": [], "p2": [], "profit": [], "match": []} for a in agents}
    for seed in seeds:
        random.seed(seed)
        contexts = build_drift_sequence(seed, n_scen)
        eval_env = SimulationEnvironment(seed=seed + 888_002, config=None)
        for agent in agents:
            agent.reset()
            p1 = p2 = 0.0
            m1 = m2 = 0
            total_profit = 0.0
            matches = 0
            for i, context in enumerate(contexts):
                action = agent.decide(context)
                r = eval_env.evaluate_action(context, action)
                profit = r.reward + r.long_term_value - r.cost
                total_profit += profit
                if r.context_match:
                    matches += 1
                if i < half:
                    p1 += profit
                    m1 += 1 if r.context_match else 0
                else:
                    p2 += profit
                    m2 += 1 if r.context_match else 0
            per[agent.name]["p1"].append(p1)
            per[agent.name]["p2"].append(p2)
            per[agent.name]["profit"].append(total_profit)
            per[agent.name]["match"].append(100.0 * matches / n_scen)
    return per


# ---------------------------------------------------------------------------
# [21] Flat-taxonomy confusion quantification
# ---------------------------------------------------------------------------

def confusion_matrix(predict_fn, env_seed, n_samples):
    env = SimulationEnvironment(seed=env_seed)
    counts = {t: {p: 0 for p in SituationType} for t in SituationType}
    for _ in range(n_samples):
        c = env.generate_context()
        counts[c.situation][predict_fn(c)] += 1
    return counts


def policy_profit_matrix(n_per_cell=300, env_seed=424_242):
    """Mean profit of playing predicted-situation s_pred's FULL policy
    (IDEAL_ACTION, SITUATION_CHANNEL, oracle-style bid for s_pred) under
    true-situation s_true contexts."""
    engine = CAMOracle("profit_matrix_e")
    env = SimulationEnvironment(seed=env_seed)
    cache = {}
    out = {}
    for s_true in SituationType:
        ctxs = []
        w = [1.0 if s == s_true else 0.0 for s in SituationType]
        env_true = SimulationEnvironment(seed=env_seed,
                                         config={"situation_weights": w})
        for _ in range(n_per_cell):
            ctxs.append(env_true.generate_context())
        for s_pred in SituationType:
            tot = 0.0
            for c in ctxs:
                a = Action(0, IDEAL_ACTION[s_pred], SITUATION_CHANNEL[s_pred],
                           round(engine._bid(s_pred, c), 2))
                r = env.evaluate_action(c, a)
                tot += r.reward + r.long_term_value - r.cost
            out[(s_true, s_pred)] = round(tot / len(ctxs), 2)
    return out


# ---------------------------------------------------------------------------

def main():
    results = {}

    # [1/3] Online reward-feedback learning ---------------------------------
    print("[1/3] Online reward-feedback learning (eps-greedy Q, UCB1) ...")
    agents_online = [AGENT_REGISTRY["baseline"](),
                     AGENT_REGISTRY["cam_multisignal"](),
                     OnlineEpsQAgent(),
                     OnlineUCBAgent()]
    results["online"] = {}
    for env_name, cfg in [("default", None),
                          ("crisis_heavy", ENVIRONMENT_PRESETS["crisis_heavy"])]:
        agg, ps_p, ps_m = run_online_env(cfg, SEEDS, N_SCEN, agents_online)
        results["online"][env_name] = {"aggregate": agg}
        for ref in ("cam_multisignal",):
            for lbl, nm in [("online_eps_vs_ms", "online_eps_q010"),
                            ("online_ucb_vs_ms", "online_ucb")]:
                st = compute_statistics(ps_p[ref], ps_p[nm])
                results["online"][env_name][lbl] = {
                    "diff": round(st["diff_mean"], 2),
                    "p_value": st["p_value"],
                    "cohens_d": st["effect_size_cohens_d"]}

    # [2/3] Mid-episode drift ------------------------------------------------
    print("[2/3] Mid-episode distribution drift (default -> crisis_heavy) ...")
    th_def, lab_def = fit_intent_for_config(None)
    th_drift, lab_drift = fit_intent_for_config(
        ENVIRONMENT_PRESETS["crisis_heavy"])
    cent_drift = fit_ms_for_config(ENVIRONMENT_PRESETS["crisis_heavy"])
    drift_agents = [
        AGENT_REGISTRY["baseline"](),
        AGENT_REGISTRY["situation_only"](),
        AGENT_REGISTRY["cam_inferred"](),
        AGENT_REGISTRY["noisy50"](),
        CAMLearned(th_def, lab_def, name="cam_learned_def"),
        CAMLearned(th_drift, lab_drift, name="cam_learned_drift"),
        AGENT_REGISTRY["cam_multisignal"](),
        CAMMultisignalLearned(cent_drift, name="cam_ms_drift"),
        AGENT_REGISTRY["oracle"](),
    ]
    per = run_drift_env(drift_agents, SEEDS, N_SCEN)
    results["drift"] = {}
    for name, d in per.items():
        results["drift"][name] = {
            "profit": round(float(np.mean(d["profit"])), 2),
            "profit_h1": round(float(np.mean(d["p1"])), 2),
            "profit_h2": round(float(np.mean(d["p2"])), 2),
            "match": round(float(np.mean(d["match"])), 1)}
    st = compute_statistics(per["cam_learned_def"]["profit"],
                            per["cam_learned_drift"]["profit"])
    results["drift"]["contrast_recal_vs_default"] = {
        "diff": round(st["diff_mean"], 2), "p_value": st["p_value"],
        "cohens_d": st["effect_size_cohens_d"]}

    # [3/3] Flat-taxonomy confusion quantification ---------------------------
    print("[3/3] Flat-taxonomy confusion quantification ...")
    th_c, lab_c = fit_intent_for_config(None)
    intent_clf = CAMLearned(th_c, lab_c, name="intent_probe")
    pred_intent = lambda c: intent_clf.classify(c.audience_intent_strength)
    pred_ms = lambda c: infer_situation_multisignal(
        c.audience_intent_strength, c.competitive_density, c.channel_quality)
    cm_intent = confusion_matrix(pred_intent, env_seed=555_555, n_samples=12_000)
    cm_ms = confusion_matrix(pred_ms, env_seed=555_555, n_samples=12_000)
    ppm = policy_profit_matrix()
    results["confusion"] = {
        "intent_matrix": {t.value: {p.value: cm_intent[t][p] for p in SituationType}
                          for t in SituationType},
        "ms_matrix": {t.value: {p.value: cm_ms[t][p] for p in SituationType}
                      for t in SituationType},
        "profit_matrix": {f"{t.value}|{p.value}": v
                          for (t, p), v in ppm.items()}}

    # Aggregate conflation rates: fraction of true-stage situations
    # (exploration/consideration/decision) predicted as a non-stage situation
    # (crisis/opportunity/retention) and vice versa.
    STAGE = {SituationType.EXPLORATION, SituationType.CONSIDERATION,
             SituationType.DECISION}
    def cross_rate(cm):
        cross = stage_total = 0
        for t, row in cm.items():
            for p, n in row.items():
                stage_total += n
                if (t in STAGE) != (p in STAGE):
                    cross += n
        return round(100.0 * cross / stage_total, 1)
    results["confusion"]["cross_axis_rate_intent"] = cross_rate(cm_intent)
    results["confusion"]["cross_axis_rate_ms"] = cross_rate(cm_ms)

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "cam_sim_v14.json").write_text(
        json.dumps(results, indent=2, default=str) + "\n")

    # Markdown report --------------------------------------------------------
    md = ["# CAM-Sim v1.4 Extensions", "",
          f"{len(SEEDS)} seeds x {N_SCEN} scenarios. Generated by paper/cam_sim_v14.py.", ""]

    md += ["## 1. Online reward-feedback learning", ""]
    for env_name in ("default", "crisis_heavy"):
        md.append(f"### {env_name}")
        md += ["| Agent | Match % | Profit |", "|---|---|---|"]
        for n, v in results["online"][env_name]["aggregate"].items():
            md.append(f"| {n} | {v['match_mean']} | {v['profit_mean']:+.2f} |")
        for lbl in ("online_eps_vs_ms", "online_ucb_vs_ms"):
            c = results["online"][env_name][lbl]
            md.append(f"{lbl}: diff={c['diff']:+.2f}, p={c['p_value']:.2e}, d={c['cohens_d']}")
        md.append("")

    md += ["## 2. Mid-episode drift (default -> crisis_heavy at scenario 100)", "",
           "| Agent | Match % | Profit | H1 (default) | H2 (crisis_heavy) |", "|---|---|---|---|---|"]
    for n, v in results["drift"].items():
        if isinstance(v, dict) and "profit" in v:
            md.append(f"| {n} | {v['match']} | {v['profit']:+.2f} | {v['profit_h1']:+.2f} | {v['profit_h2']:+.2f} |")
    c = results["drift"]["contrast_recal_vs_default"]
    md.append(f"recal(default->drift) vs default-fit: diff={c['diff']:+.2f}, "
              f"p={c['p_value']:.2e}, d={c['cohens_d']}")

    md += ["", "## 3. Flat-taxonomy confusion (12,000 default samples)", "",
           f"Cross-axis confusion rate (stage <-> condition/lifecycle): "
           f"intent-only {results['confusion']['cross_axis_rate_intent']}%, "
           f"multi-signal {results['confusion']['cross_axis_rate_ms']}%", "",
           "### Intent-only confusion matrix (rows=true, cols=predicted)", ""]
    header = "| true \\ pred | " + " | ".join(s.value for s in SituationType) + " |"
    md += [header, "|" + "---|" * (len(list(SituationType)) + 1)]
    for t, row in results["confusion"]["intent_matrix"].items():
        md.append("| " + t + " | " + " | ".join(str(row[p.value]) for p in SituationType) + " |")
    md += ["", "### Multi-signal confusion matrix (rows=true, cols=predicted)", "",
           header, "|" + "---|" * (len(list(SituationType)) + 1)]
    for t, row in results["confusion"]["ms_matrix"].items():
        md.append("| " + t + " | " + " | ".join(str(row[p.value]) for p in SituationType) + " |")
    md += ["", "### Expected profit of playing predicted-policy under true situation", "",
           "| true \\ pred | " + " | ".join(s.value for s in SituationType) + " |",
           "|" + "---|" * (len(list(SituationType)) + 1)]
    pm = results["confusion"]["profit_matrix"]
    for t in SituationType:
        md.append("| " + t.value + " | "
                  + " | ".join(f"{pm[f'{t.value}|{p.value}']:+.2f}" for p in SituationType) + " |")

    (OUT / "cam_sim_v14.md").write_text("\n".join(md) + "\n")
    print("Wrote", OUT / "cam_sim_v14.json")
    print("Wrote", OUT / "cam_sim_v14.md")


if __name__ == "__main__":
    main()
