#!/usr/bin/env python3
"""CAM-Sim: Context-Aware Agentic Marketing Simulation Environment.

A synthetic marketing simulation for benchmarking Context-Aware Agentic Marketing
(CAM) frameworks. Enables reproducible evaluation of context-aware marketing
agents without requiring live ad spend or customer data.

Usage:
    python3 scripts/benchmarks/cam_sim.py --scenarios 1000 --agents baseline,cam --output results.json
    python3 scripts/benchmarks/cam_sim.py --evaluate --results results.json

Author: Tobias Weiss (2026)
"""

import argparse
import json
import random
import sys
from abc import ABC, abstractmethod
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from typing import List, Dict, Optional, Tuple, Type
from pathlib import Path

import numpy as np

# Type aliases
ContextID = str
ActionID = int


class SituationType(Enum):
    """Situational archetypes from CAM framework."""
    EXPLORATION = "exploration"
    CONSIDERATION = "consideration"
    DECISION = "decision"
    CRISIS = "crisis"
    OPPORTUNITY = "opportunity"
    RETENTION = "retention"


class ChannelType(Enum):
    """Marketing channel types."""
    SEARCH = "search"
    SOCIAL = "social"
    DISPLAY = "display"
    EMAIL = "email"
    VIDEO = "video"


class ActionType(Enum):
    """Marketing action types."""
    EDUCATIONAL = "educational"
    COMPARISON = "comparison"
    PROMOTIONAL = "promotional"
    CRISIS_RESPONSE = "crisis_response"
    URGENT = "urgent"
    LOYALTY = "loyalty"


@dataclass
class ContextSignal:
    """A single context signal."""
    category: str  # audience, channel, temporal, situational, social, market
    name: str
    value: float | str | int
    confidence: float = 1.0
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())


@dataclass
class FullContext:
    """Complete context state for a marketing moment."""
    context_id: ContextID
    timestamp: str
    signals: List[ContextSignal] = field(default_factory=list)
    situation: SituationType = SituationType.EXPLORATION
    audience_intent_strength: float = 0.5
    channel_quality: float = 0.7
    competitive_density: float = 0.3
    
    # Computed features for ML
    intent_vector: List[float] = field(default_factory=list)
    
    def to_dict(self) -> dict:
        return {
            'context_id': self.context_id,
            'timestamp': self.timestamp,
            'situation': self.situation.value,
            'audience_intent_strength': self.audience_intent_strength,
            'channel_quality': self.channel_quality,
            'competitive_density': self.competitive_density,
            'intent_vector': self.intent_vector,
            'signals': [{'category': s.category, 'name': s.name, 'value': s.value, 'confidence': s.confidence, 'timestamp': s.timestamp} for s in self.signals]
        }


@dataclass 
class Action:
    """A marketing action."""
    action_id: ActionID
    action_type: ActionType
    channel: ChannelType
    bid: float = 0.0
    content: str = ""
    
    def to_dict(self) -> dict:
        return {
            'action_id': self.action_id,
            'action_type': self.action_type.value,
            'channel': self.channel.value,
            'bid': self.bid,
            'content': self.content
        }

@dataclass
class ActionResult:
    """Result of taking an action in a context."""
    context_id: ContextID
    action_id: ActionID
    action_type: ActionType
    reward: float  # Immediate reward (clicks, conversions, revenue)
    cost: float  # Cost of action
    long_term_value: float = 0.0  # Lifetime value impact
    context_match: bool = False  # Whether action matched context
    latency_ms: float = 0.0  # Decision latency
    
    def to_dict(self) -> dict:
        return {
            'context_id': self.context_id,
            'action_id': self.action_id,
            'action_type': self.action_type.value,
            'reward': self.reward,
            'cost': self.cost,
            'long_term_value': self.long_term_value,
            'context_match': self.context_match,
            'latency_ms': self.latency_ms
        }
    
    @property
    def return_on_spend(self) -> float:
        """Return on ad spend (ROAS)."""
        if self.cost == 0:
            return float('inf')
        return (self.reward + self.long_term_value) / self.cost
    
    @property
    def profit(self) -> float:
        """Net profit from action."""
        return self.reward + self.long_term_value - self.cost


class Agent(ABC):
    """Abstract base class for marketing agents."""
    
    def __init__(self, name: str):
        self.name = name
        self.actions_taken: int = 0
    
    @abstractmethod
    def decide(self, context: FullContext) -> Action:
        """Make a decision given a context. Must be implemented by subclasses."""
        pass
    
    @abstractmethod 
    def reset(self):
        """Reset agent state."""
        self.actions_taken = 0
    
    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "type": self.__class__.__name__,
            "actions_taken": self.actions_taken
        }


class BaselineAgent(Agent):
    """Rule-based non-context-aware agent."""
    
    BASE_BIDS = {
        ChannelType.SEARCH: 1.50,
        ChannelType.SOCIAL: 1.00,
        ChannelType.DISPLAY: 0.80,
        ChannelType.EMAIL: 0.10,
        ChannelType.VIDEO: 2.00
    }
    
    DEFAULT_ACTIONS = {
        ChannelType.SEARCH: ActionType.EDUCATIONAL,
        ChannelType.SOCIAL: ActionType.EDUCATIONAL,
        ChannelType.DISPLAY: ActionType.PROMOTIONAL,
        ChannelType.EMAIL: ActionType.LOYALTY,
        ChannelType.VIDEO: ActionType.PROMOTIONAL
    }
    
    def __init__(self):
        super().__init__("baseline_rule_based")
        self.random_bid_variation = 0.2  # ±20% random variation
    
    def decide(self, context: FullContext) -> Action:
        self.actions_taken += 1
        
        # Simple rule-based decision - no context awareness
        channel = random.choice(list(ChannelType))
        base_bid = self.BASE_BIDS[channel]
        
        # Add random variation
        bid_variation = random.uniform(-self.random_bid_variation, self.random_bid_variation)
        bid = max(0.01, base_bid * (1 + bid_variation))
        
        action_type = self.DEFAULT_ACTIONS[channel]
        
        return Action(
            action_id=self.actions_taken,
            action_type=action_type,
            channel=channel,
            bid=round(bid, 2)
        )
    
    def reset(self):
        super().reset()


class CAMAgent(Agent):
    """Context-Aware Agentic Marketing agent (Level 3 implementation)."""
    
    # Situation-based bid multipliers
    SITUATION_MULTIPLIERS = {
        SituationType.EXPLORATION: 0.8,
        SituationType.CONSIDERATION: 1.2,
        SituationType.DECISION: 1.8,
        SituationType.CRISIS: 2.0,
        SituationType.OPPORTUNITY: 1.5,
        SituationType.RETENTION: 1.0
    }
    
    # Situation-based action recommendations
    SITUATION_ACTIONS = {
        SituationType.EXPLORATION: ActionType.EDUCATIONAL,
        SituationType.CONSIDERATION: ActionType.COMPARISON,
        SituationType.DECISION: ActionType.PROMOTIONAL,
        SituationType.CRISIS: ActionType.CRISIS_RESPONSE,
        SituationType.OPPORTUNITY: ActionType.URGENT,
        SituationType.RETENTION: ActionType.LOYALTY
    }
    
    # Channel quality adjustments
    CHANNEL_QUALITY_ADJUSTMENTS = {
        0.0: 0.5,   # Poor quality -> lower bid
        0.3: 0.8,
        0.5: 1.0,
        0.7: 1.2,
        0.9: 1.5,
        1.0: 2.0    # Excellent quality -> max bid
    }
    
    # Intent strength adjustments
    INTENT_ADJUSTMENTS = {
        0.0: 0.5,   # Low intent
        0.25: 0.8,
        0.5: 1.0,
        0.75: 1.3,
        1.0: 1.8    # High intent
    }
    
    def __init__(self):
        super().__init__("cam_context_aware")
    
    def _get_adjustment(self, value: float, mapping: dict) -> float:
        """Get linear interpolation from mapping."""
        keys = sorted(mapping.keys())
        for i in range(len(keys) - 1):
            if keys[i] <= value <= keys[i + 1]:
                # Linear interpolation
                ratio = (value - keys[i]) / (keys[i + 1] - keys[i])
                return mapping[keys[i]] + ratio * (mapping[keys[i + 1]] - mapping[keys[i]])
        return mapping.get(keys[-1], 1.0)
    
    def decide(self, context: FullContext) -> Action:
        self.actions_taken += 1
        
        # CAM: Make decision based on context
        base_bid = 1.0  # Base bid
        
        # Apply situation multiplier
        situation_multiplier = self.SITUATION_MULTIPLIERS[context.situation]
        
        # Apply channel quality adjustment
        channel_quality_adj = self._get_adjustment(context.channel_quality, self.CHANNEL_QUALITY_ADJUSTMENTS)
        
        # Apply intent strength adjustment
        intent_adj = self._get_adjustment(context.audience_intent_strength, self.INTENT_ADJUSTMENTS)
        
        # Calculate final bid
        bid = base_bid * situation_multiplier * channel_quality_adj * intent_adj
        
        # Determine action type from situation
        action_type = self.SITUATION_ACTIONS[context.situation]
        
        # For now, select channel based on situation (simplified)
        channel_map = {
            SituationType.EXPLORATION: ChannelType.SEARCH,
            SituationType.CONSIDERATION: ChannelType.SOCIAL,
            SituationType.DECISION: ChannelType.SEARCH,
            SituationType.CRISIS: ChannelType.SOCIAL,
            SituationType.OPPORTUNITY: ChannelType.DISPLAY,
            SituationType.RETENTION: ChannelType.EMAIL
        }
        channel = channel_map.get(context.situation, ChannelType.SEARCH)
        
        return Action(
            action_id=self.actions_taken,
            action_type=action_type,
            channel=channel,
            bid=round(bid, 2)
        )
    
    def reset(self):
        super().reset()


class SimulationEnvironment:
    """Synthetic marketing simulation environment."""
    
    ACTION_COSTS = {
        ChannelType.SEARCH: 1.20,
        ChannelType.SOCIAL: 0.80,
        ChannelType.DISPLAY: 0.60,
        ChannelType.EMAIL: 0.05,
        ChannelType.VIDEO: 2.50
    }
    
    def __init__(self, seed: Optional[int] = None, deterministic: bool = False):
        self.rng = np.random.RandomState(seed)
        self.deterministic = deterministic
        self.scenario_counter = 0
    
    def _random_situation(self) -> SituationType:
        """Generate random situation weighted by real-world distribution."""
        situations = list(SituationType)
        # Weights: exploration and consideration are most common
        weights = [0.35, 0.30, 0.15, 0.05, 0.05, 0.10]  # explore, consider, decide, crisis, opportunity, retention
        choice = self.rng.choice(len(situations), p=weights)
        return situations[choice]
    
    def _random_channel(self) -> ChannelType:
        """Generate random channel."""
        channels = list(ChannelType)
        return channels[self.rng.randint(0, len(channels))]
    
    def generate_context(self) -> FullContext:
        """Generate a synthetic marketing context."""
        self.scenario_counter += 1
        
        context_id = f"ctx_{self.scenario_counter}"
        timestamp = datetime.utcnow().isoformat()
        
        # Random situation
        situation = self._random_situation()
        
        # Generate signals based on situation
        signals = self._generate_signals(situation)
        
        # Generate context features
        audience_intent_strength = self._get_intent_strength(situation)
        channel_quality = self.rng.uniform(0.1, 1.0)
        competitive_density = self.rng.uniform(0.0, 1.0)
        
        # Simplified intent vector
        intent_vector = self._generate_intent_vector(situation)
        
        return FullContext(
            context_id=context_id,
            timestamp=timestamp,
            signals=signals,
            situation=situation,
            audience_intent_strength=audience_intent_strength,
            channel_quality=channel_quality,
            competitive_density=competitive_density,
            intent_vector=intent_vector
        )
    
    def _generate_signals(self, situation: SituationType) -> List[ContextSignal]:
        """Generate synthetic signals for a situation."""
        signals = []
        
        # Audience signals
        if situation in [SituationType.DECISION, SituationType.CRISIS]:
            signals.append(ContextSignal(
                category="audience",
                name="intent_strength",
                value=self._get_intent_strength(situation),
                confidence=0.9
            ))
        
        # Channel signals
        signals.append(ContextSignal(
            category="channel",
            name="quality_score",
            value=round(self.rng.uniform(0.5, 1.0), 2),
            confidence=0.8
        ))
        
        # Temporal signals
        signals.append(ContextSignal(
            category="temporal",
            name="time_of_day",
            value=self.rng.choice(["morning", "afternoon", "evening", "night"]),
            confidence=1.0
        ))
        
        # Situational signals
        signals.append(ContextSignal(
            category="situational",
            name="device_type",
            value=self.rng.choice(["desktop", "mobile", "tablet"]),
            confidence=0.95
        ))
        
        return signals
    
    def _get_intent_strength(self, situation: SituationType) -> float:
        """Get typical intent strength for a situation."""
        strengths = {
            SituationType.EXPLORATION: 0.2,
            SituationType.CONSIDERATION: 0.6,
            SituationType.DECISION: 0.9,
            SituationType.CRISIS: 0.8,
            SituationType.OPPORTUNITY: 0.7,
            SituationType.RETENTION: 0.3
        }
        # Add noise
        return max(0.0, min(1.0, strengths[situation] + self.rng.uniform(-0.1, 0.1)))
    
    def _generate_intent_vector(self, situation: SituationType) -> List[float]:
        """Generate a simplified intent embedding."""
        # Use 16-dimensional vectors for efficiency
        base_vectors = {
            SituationType.EXPLORATION: [0.8, 0.2, 0.1, 0.0, 0.0, 0.1, 0.3, 0.2, 0.1, 0.2, 0.1, 0.0, 0.1, 0.2, 0.1, 0.1],
            SituationType.CONSIDERATION: [0.2, 0.7, 0.3, 0.2, 0.1, 0.2, 0.1, 0.3, 0.2, 0.1, 0.1, 0.2, 0.2, 0.1, 0.2, 0.1],
            SituationType.DECISION: [0.1, 0.2, 0.8, 0.3, 0.4, 0.1, 0.1, 0.2, 0.1, 0.2, 0.3, 0.1, 0.2, 0.1, 0.1, 0.2],
            SituationType.CRISIS: [0.0, 0.1, 0.2, 0.8, 0.3, 0.2, 0.1, 0.1, 0.2, 0.3, 0.1, 0.2, 0.1, 0.1, 0.2, 0.3],
            SituationType.OPPORTUNITY: [0.3, 0.4, 0.2, 0.1, 0.1, 0.7, 0.2, 0.1, 0.3, 0.1, 0.2, 0.3, 0.1, 0.2, 0.1, 0.1],
            SituationType.RETENTION: [0.4, 0.2, 0.1, 0.0, 0.1, 0.3, 0.8, 0.1, 0.2, 0.1, 0.1, 0.1, 0.1, 0.2, 0.1, 0.3]
        }
        # Add noise
        vector = base_vectors[situation][:]
        noise = self.rng.uniform(-0.1, 0.1, len(vector))
        return [max(0.0, min(1.0, v + n)) for v, n in zip(vector, noise)]
    
    def evaluate_action(self, context: FullContext, action: Action) -> ActionResult:
        """Evaluate the result of taking an action in a context."""
        
        # Base rewards by action type and situation
        base_rewards = {
            (ActionType.EDUCATIONAL, SituationType.EXPLORATION): 2.0,
            (ActionType.EDUCATIONAL, SituationType.CONSIDERATION): 1.5,
            (ActionType.EDUCATIONAL, SituationType.DECISION): 0.5,
            (ActionType.EDUCATIONAL, SituationType.CRISIS): 0.3,
            (ActionType.EDUCATIONAL, SituationType.OPPORTUNITY): 1.0,
            (ActionType.EDUCATIONAL, SituationType.RETENTION): 1.2,
            
            (ActionType.COMPARISON, SituationType.EXPLORATION): 0.8,
            (ActionType.COMPARISON, SituationType.CONSIDERATION): 2.5,
            (ActionType.COMPARISON, SituationType.DECISION): 1.8,
            (ActionType.COMPARISON, SituationType.CRISIS): 0.5,
            (ActionType.COMPARISON, SituationType.OPPORTUNITY): 1.2,
            (ActionType.COMPARISON, SituationType.RETENTION): 0.8,
            
            (ActionType.PROMOTIONAL, SituationType.EXPLORATION): 0.5,
            (ActionType.PROMOTIONAL, SituationType.CONSIDERATION): 1.5,
            (ActionType.PROMOTIONAL, SituationType.DECISION): 3.0,
            (ActionType.PROMOTIONAL, SituationType.CRISIS): 0.3,
            (ActionType.PROMOTIONAL, SituationType.OPPORTUNITY): 2.5,
            (ActionType.PROMOTIONAL, SituationType.RETENTION): 0.5,
            
            (ActionType.CRISIS_RESPONSE, SituationType.EXPLORATION): 0.1,
            (ActionType.CRISIS_RESPONSE, SituationType.CONSIDERATION): 0.3,
            (ActionType.CRISIS_RESPONSE, SituationType.DECISION): 0.5,
            (ActionType.CRISIS_RESPONSE, SituationType.CRISIS): 2.5,
            (ActionType.CRISIS_RESPONSE, SituationType.OPPORTUNITY): 0.2,
            (ActionType.CRISIS_RESPONSE, SituationType.RETENTION): 0.8,
            
            (ActionType.URGENT, SituationType.EXPLORATION): 0.5,
            (ActionType.URGENT, SituationType.CONSIDERATION): 1.2,
            (ActionType.URGENT, SituationType.DECISION): 2.0,
            (ActionType.URGENT, SituationType.CRISIS): 0.8,
            (ActionType.URGENT, SituationType.OPPORTUNITY): 2.8,
            (ActionType.URGENT, SituationType.RETENTION): 0.3,
            
            (ActionType.LOYALTY, SituationType.EXPLORATION): 0.3,
            (ActionType.LOYALTY, SituationType.CONSIDERATION): 0.5,
            (ActionType.LOYALTY, SituationType.DECISION): 0.2,
            (ActionType.LOYALTY, SituationType.CRISIS): 0.5,
            (ActionType.LOYALTY, SituationType.OPPORTUNITY): 0.3,
            (ActionType.LOYALTY, SituationType.RETENTION): 2.0
        }
        
        # Get base reward
        base_reward = base_rewards.get((action.action_type, context.situation), 1.0)
        
        # Context match bonus: was this the right action for the situation?
        ideal_action = {
            SituationType.EXPLORATION: ActionType.EDUCATIONAL,
            SituationType.CONSIDERATION: ActionType.COMPARISON,
            SituationType.DECISION: ActionType.PROMOTIONAL,
            SituationType.CRISIS: ActionType.CRISIS_RESPONSE,
            SituationType.OPPORTUNITY: ActionType.URGENT,
            SituationType.RETENTION: ActionType.LOYALTY
        }[context.situation]
        
        context_match = (action.action_type == ideal_action)
        if context_match:
            context_bonus = 0.5  # Bonus for correct action type
        else:
            context_bonus = -0.3  # Penalty for wrong action type
        
        # Bid efficiency: how well did they bid relative to context?
        # Optimal bid is proportional to intent strength and channel quality
        optimal_bid = 1.0 * context.audience_intent_strength * context.channel_quality
        bid_ratio = action.bid / optimal_bid if optimal_bid > 0 else 0
        if 0.8 <= bid_ratio <= 1.2:
            bid_efficiency = 0.3  # Good bid
        elif 0.5 <= bid_ratio <= 1.5:
            bid_efficiency = 0.1  # Decent bid
        else:
            bid_efficiency = -0.2  # Bad bid
        
        # Competitive adjustment
        competitive_factor = 1.0 - context.competitive_density * 0.5
        
        # Total reward
        total_reward = base_reward + context_bonus + bid_efficiency
        total_reward *= competitive_factor
        
        # Cost
        cost = self.ACTION_COSTS[action.channel] * action.bid
        
        # Long-term value (simplified)
        long_term_value = total_reward * 0.2 * context.audience_intent_strength
        
        # Latency (simulated)
        latency_ms = self.rng.uniform(50, 500)  # 50-500ms
        
        return ActionResult(
            context_id=context.context_id,
            action_id=action.action_id,
            action_type=action.action_type,
            reward=round(total_reward, 2),
            cost=round(cost, 2),
            long_term_value=round(long_term_value, 2),
            context_match=context_match,
            latency_ms=round(latency_ms, 1)
        )


class BenchmarkRunner:
    """Run benchmarks comparing different agents."""
    
    def __init__(self, env: SimulationEnvironment):
        self.env = env
        self.results: Dict[str, List[ActionResult]] = defaultdict(list)
        self.contexts: List[FullContext] = []
    
    def run_agent(self, agent: Agent, num_scenarios: int) -> Dict[str, list]:
        """Run an agent through scenarios."""
        agent.reset()
        results = []
        
        for _ in range(num_scenarios):
            context = self.env.generate_context()
            self.contexts.append(context)
            
            action = agent.decide(context)
            result = self.env.evaluate_action(context, action)
            result.action_type = action.action_type
            results.append(result)
        
        return results
    
    def run_benchmark(self, agents: List[Agent], num_scenarios: int = 1000) -> dict:
        """Run all agents and collect results."""
        all_results = {}
        self.contexts = []  # Reset contexts
        
        for agent in agents:
            results = self.run_agent(agent, num_scenarios)
            all_results[agent.name] = results
        
        return all_results
    
    def get_metrics(self, results: Dict[str, List[ActionResult]]) -> Dict[str, dict]:
        """Calculate evaluation metrics."""
        metrics = {}
        
        for agent_name, agent_results in results.items():
            if not agent_results:
                continue
            
            # Basic counts
            total_actions = len(agent_results)
            total_cost = sum(r.cost for r in agent_results)
            total_reward = sum(r.reward for r in agent_results)
            total_long_term_value = sum(r.long_term_value for r in agent_results)
            total_profit = sum(r.profit for r in agent_results)
            
            # Rates
            context_match_rate = sum(1 for r in agent_results if r.context_match) / total_actions
            
            # Averages
            avg_cost = total_cost / total_actions if total_actions > 0 else 0
            avg_reward = total_reward / total_actions if total_actions > 0 else 0
            avg_roas = sum(r.return_on_spend for r in agent_results) / total_actions if total_actions > 0 else 0
            avg_latency = sum(r.latency_ms for r in agent_results) / total_actions if total_actions > 0 else 0
            
            # Efficiency
            profit_per_cost = total_profit / total_cost if total_cost > 0 else 0
            
            metrics[agent_name] = {
                'total_actions': total_actions,
                'total_cost': round(total_cost, 2),
                'total_reward': round(total_reward, 2),
                'total_profit': round(total_profit, 2),
                'total_long_term_value': round(total_long_term_value, 2),
                'context_match_rate': round(context_match_rate * 100, 1),
                'avg_cost': round(avg_cost, 2),
                'avg_reward': round(avg_reward, 2),
                'avg_roas': round(avg_roas, 2),
                'avg_latency_ms': round(avg_latency, 1),
                'profit_per_cost': round(profit_per_cost, 2)
            }
        
        return metrics


def create_default_agents() -> List[Agent]:
    """Create default agents for benchmarking."""
    return [
        BaselineAgent(),
        CAMAgent()
    ]


def main():
    parser = argparse.ArgumentParser(
        description="CAM-Sim: Context-Aware Agentic Marketing Simulation"
    )
    parser.add_argument(
        "--scenarios", "-n",
        type=int,
        default=1000,
        help="Number of scenarios to simulate (default: 1000)"
    )
    parser.add_argument(
        "--agents", "-a",
        type=str,
        default="baseline,cam",
        help="Comma-separated list of agents: baseline, cam (default: baseline,cam)"
    )
    parser.add_argument(
        "--seed", "-s",
        type=int,
        default=None,
        help="Random seed for reproducibility"
    )
    parser.add_argument(
        "--output", "-o",
        type=str,
        default="results/cam_sim_results.json",
        help="Output file path (default: results/cam_sim_results.json)"
    )
    parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="Minimal output"
    )
    
    args = parser.parse_args()
    
    # Create output directory
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Create environment and agents
    env = SimulationEnvironment(seed=args.seed)
    
    available_agents = {
        'baseline': BaselineAgent(),
        'cam': CAMAgent()
    }
    
    selected_agents = [
        available_agents[name.strip()] 
        for name in args.agents.split(',') 
        if name.strip() in available_agents
    ]
    
    if not selected_agents:
        print("No valid agents selected. Available: baseline, cam")
        sys.exit(1)
    
    # Run benchmark
    if not args.quiet:
        print(f"Running CAM-Sim with {args.scenarios} scenarios...")
        print(f"Agents: {[a.name for a in selected_agents]}")
        print()
    
    runner = BenchmarkRunner(env)
    results = runner.run_benchmark(selected_agents, args.scenarios)
    metrics = runner.get_metrics(results)
    
    # Print results
    if not args.quiet:
        print("=" * 70)
        print("CAM-Sim Benchmark Results")
        print("=" * 70)
        print()
        
        for agent_name, agent_metrics in metrics.items():
            print(f"🎯 {agent_name.upper()}")
            print("-" * 40)
            print(f"  Actions:           {agent_metrics['total_actions']:,}")
            print(f"  Total Cost:        ${agent_metrics['total_cost']:,.2f}")
            print(f"  Total Reward:      ${agent_metrics['total_reward']:,.2f}")
            print(f"  Total Profit:      ${agent_metrics['total_profit']:,.2f}")
            print(f"  Long-term Value:   ${agent_metrics['total_long_term_value']:,.2f}")
            print(f"  Context Match:     {agent_metrics['context_match_rate']}%")
            print(f"  Avg ROAS:           {agent_metrics['avg_roas']:.2f}x")
            print(f"  Avg Latency:       {agent_metrics['avg_latency_ms']}ms")
            print(f"  Profit/Cost:       ${agent_metrics['profit_per_cost']:.2f}")
            print()
        
        # Comparison
        if len(metrics) > 1:
            print("📈 COMPARISON")
            print("-" * 40)
            agent_names = list(metrics.keys())
            for metric_key in ['context_match_rate', 'total_profit', 'avg_roas', 'profit_per_cost']:
                values = [metrics[name][metric_key] for name in agent_names]
                if metric_key == 'context_match_rate':
                    print(f"  Context Match:  {values[0]}% vs {values[1]}% (+{values[1]-values[0]:.1f}%)")
                elif metric_key == 'total_profit':
                    profit_diff = values[1] - values[0]
                    profit_pct = (profit_diff / values[0] * 100) if values[0] != 0 else float('inf')
                    print(f"  Total Profit:   ${values[0]:,.2f} vs ${values[1]:,.2f} (+${profit_diff:,.2f}, +{profit_pct:.1f}%)")
                else:
                    diff = values[1] - values[0]
                    pct = (diff / values[0] * 100) if values[0] != 0 else float('inf')
                    print(f"  {metric_key.replace('_', ' ').title()}:  {values[0]:.2f} vs {values[1]:.2f} (+{diff:.2f}, +{pct:.1f}%)")
    
    # Save results
    output_data = {
        'timestamp': datetime.utcnow().isoformat(),
        'scenarios': args.scenarios,
        'seed': args.seed,
        'agents': [a.name for a in selected_agents],
        'metrics': metrics,
        'contexts': [c.to_dict() for c in runner.contexts[:10]]  # Save first 10 contexts as sample
    }
    
    with open(output_path, 'w') as f:
        json.dump(output_data, f, indent=2)
    
    if not args.quiet:
        print(f"\n✅ Results saved to: {output_path}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
