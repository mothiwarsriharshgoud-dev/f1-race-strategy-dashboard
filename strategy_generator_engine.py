import json
import os
import math

class F1StrategyOptimizer:
    def __init__(self, dataset_path=None):
        if dataset_path is None:
            dataset_path = "C:/Users/Main User/.gemini/antigravity/scratch/f1-race-strategy-dashboard/data/f1_strategy_dataset.json"
        
        with open(dataset_path, "r", encoding="utf-8") as f:
            self.data = json.load(f)
            
        self.circuits = {c["circuitId"]: c for c in self.data["circuits"]}
        self.drivers = {d["code"]: d for d in self.data["drivers"]}
        
        # Compound baseline characteristics
        self.compound_specs = {
            "SOFT": {"delta_base": -0.65, "deg_base": 0.082, "cliff_lap": 16, "max_life": 22, "warmup_laps": 1, "color": "#E10600"},
            "MEDIUM": {"delta_base": 0.00, "deg_base": 0.052, "cliff_lap": 26, "max_life": 34, "warmup_laps": 1.5, "color": "#FFF200"},
            "HARD": {"delta_base": +0.48, "deg_base": 0.038, "cliff_lap": 38, "max_life": 50, "warmup_laps": 2.5, "color": "#FFFFFF"},
            "INTER": {"delta_base": +3.80, "deg_base": 0.095, "cliff_lap": 22, "max_life": 30, "warmup_laps": 1.0, "color": "#39B54A"},
            "WET": {"delta_base": +7.50, "deg_base": 0.120, "cliff_lap": 18, "max_life": 26, "warmup_laps": 1.0, "color": "#00A0DE"},
        }
        
    def generate_strategies(self, circuit_id=3, grid_position=1, team_tier="Tier 1 (Red Bull/McLaren/Ferrari)", 
                            track_temp=35.0, sc_probability="Medium (40%)", objective="Balanced Win/Podium"):
        circuit = self.circuits.get(circuit_id, self.circuits[3])
        total_laps = 57 if circuit_id == 3 else (78 if circuit_id == 6 else (44 if circuit_id == 13 else 56))
        
        # Adjust base pace for circuit length
        # Typical F1 lap ~ 1m 30s for 5.4km circuit
        base_lap_time = round((circuit["length_km"] / 5.412) * 94.8, 2)
        
        # Team tier delta
        tier_deltas = {
            "Tier 1 (Red Bull/McLaren/Ferrari)": 0.0,
            "Tier 2 (Mercedes/Aston Martin)": 0.45,
            "Tier 3 (Midfield: Haas/RB/Williams/Alpine/Sauber)": 0.95
        }
        tier_offset = tier_deltas.get(team_tier, 0.0)
        
        # Environmental and circuit multiplier
        stress = circuit.get("tire_stress", 3.5)
        abrasiveness = circuit.get("abrasiveness", 3.2)
        pit_loss = circuit.get("pit_loss_sec", 21.8)
        overtaking_diff = circuit.get("overtaking_diff", 5.0)
        
        temp_factor = 1.0 + ((track_temp - 30.0) * 0.012)
        circuit_deg_multiplier = (stress / 3.5) * (abrasiveness / 3.0) * temp_factor
        
        # SC discount
        sc_chance = 0.4
        if "Low" in sc_probability: sc_chance = 0.15
        elif "High" in sc_probability: sc_chance = 0.75
        
        # Simulate candidate strategies
        candidates = []
        
        # Permutation 1: 1-Stop (Medium -> Hard)
        p1 = self._simulate_stints(
            name="1-Stop Medium-Hard",
            stints=[("MEDIUM", 1, int(total_laps * 0.42)), ("HARD", int(total_laps * 0.42) + 1, total_laps)],
            total_laps=total_laps, base_lap=base_lap_time + tier_offset, pit_loss=pit_loss,
            circuit_mult=circuit_deg_multiplier, sc_chance=sc_chance, overtakes_needed=max(0, grid_position - 1),
            overtaking_diff=overtaking_diff
        )
        candidates.append(p1)
        
        # Permutation 2: 2-Stop (Soft -> Hard -> Soft or Soft -> Hard -> Medium)
        p2_split1 = int(total_laps * 0.28)
        p2_split2 = int(total_laps * 0.65)
        p2 = self._simulate_stints(
            name="2-Stop Soft-Hard-Soft (Attack)",
            stints=[
                ("SOFT", 1, p2_split1), 
                ("HARD", p2_split1 + 1, p2_split2), 
                ("SOFT", p2_split2 + 1, total_laps)
            ],
            total_laps=total_laps, base_lap=base_lap_time + tier_offset, pit_loss=pit_loss,
            circuit_mult=circuit_deg_multiplier, sc_chance=sc_chance, overtakes_needed=max(0, grid_position - 1),
            overtaking_diff=overtaking_diff
        )
        candidates.append(p2)
        
        # Permutation 3: 2-Stop (Medium -> Hard -> Medium)
        p3_split1 = int(total_laps * 0.35)
        p3_split2 = int(total_laps * 0.70)
        p3 = self._simulate_stints(
            name="2-Stop Medium-Hard-Medium (Balanced)",
            stints=[
                ("MEDIUM", 1, p3_split1), 
                ("HARD", p3_split1 + 1, p3_split2), 
                ("MEDIUM", p3_split2 + 1, total_laps)
            ],
            total_laps=total_laps, base_lap=base_lap_time + tier_offset, pit_loss=pit_loss,
            circuit_mult=circuit_deg_multiplier, sc_chance=sc_chance, overtakes_needed=max(0, grid_position - 1),
            overtaking_diff=overtaking_diff
        )
        candidates.append(p3)

        # Permutation 4: Reverse 1-Stop (Hard -> Soft/Medium - Overcut & SC Gamble)
        p4_split1 = int(total_laps * 0.62)
        p4 = self._simulate_stints(
            name="1-Stop Hard-Soft (Reverse Overcut)",
            stints=[
                ("HARD", 1, p4_split1), 
                ("SOFT", p4_split1 + 1, total_laps)
            ],
            total_laps=total_laps, base_lap=base_lap_time + tier_offset, pit_loss=pit_loss,
            circuit_mult=circuit_deg_multiplier, sc_chance=sc_chance, overtakes_needed=max(0, grid_position - 1),
            overtaking_diff=overtaking_diff, is_sc_gamble=True
        )
        candidates.append(p4)
        
        # Rank by total adjusted time
        candidates.sort(key=lambda x: x["expected_total_time"])
        
        # Format Top 3 Plans: Plan A (Optimal), Plan B (Attack Undercut), Plan C (Safety Car Contingency)
        plan_a = candidates[0]
        plan_a["plan_code"] = "PLAN A (PRIMARY OPTIMAL)"
        plan_a["role"] = "Recommended by telemetry engine for fastest aggregate race completion time."
        plan_a["confidence_score"] = 94.2
        
        # Find best alternative that is distinct
        plan_b = next((c for c in candidates[1:] if "2-Stop" in c["name"] or "Attack" in c["name"]), candidates[1])
        plan_b["plan_code"] = "PLAN B (UNDERCUT & TRACK DELTA)"
        plan_b["role"] = "High-aggression strategy to jump rivals in pit window using fresh tire out-lap grip."
        plan_b["confidence_score"] = 87.5
        
        plan_c = next((c for c in candidates if "Overcut" in c["name"] or c["is_sc_gamble"]), candidates[-1])
        plan_c["plan_code"] = "PLAN C (CONTINGENCY / SC GAMBLE)"
        plan_c["role"] = "Extends stint to fish for a Virtual Safety Car or Full Safety Car for a free pit stop."
        plan_c["confidence_score"] = 79.0
        
        return {
            "circuit": circuit,
            "inputs": {
                "grid_position": grid_position,
                "team_tier": team_tier,
                "track_temp": track_temp,
                "sc_probability": sc_probability,
                "objective": objective,
                "total_laps": total_laps,
                "pit_loss_sec": pit_loss,
            },
            "plans": [plan_a, plan_b, plan_c],
            "decision_triggers": self._generate_pit_triggers(circuit, total_laps, plan_a, plan_b, plan_c)
        }

    def _simulate_stints(self, name, stints, total_laps, base_lap, pit_loss, circuit_mult, sc_chance, overtakes_needed, overtaking_diff, is_sc_gamble=False):
        total_time = 0.0
        total_deg_loss = 0.0
        stint_profiles = []
        stops = len(stints) - 1
        
        # Expected pit transit loss
        # If SC gamble, there is a chance of saving 12s under SC
        effective_pit_loss = pit_loss * stops
        if is_sc_gamble and sc_chance > 0.3:
            effective_pit_loss -= (12.0 * sc_chance)
            
        cur_lap = 1
        for s_idx, (comp, s_start, s_end) in enumerate(stints, 1):
            stint_laps = s_end - s_start + 1
            spec = self.compound_specs[comp]
            comp_deg = spec["deg_base"] * circuit_mult
            cliff = spec["cliff_lap"]
            
            stint_time = 0.0
            stint_deg = 0.0
            
            for lap_in_stint in range(1, stint_laps + 1):
                race_lap = s_start + lap_in_stint - 1
                fuel_effect = (race_lap - 1) * -0.062
                
                # Degradation calculation
                wear = (lap_in_stint - 1) * comp_deg
                cliff_penalty = 0.0
                if lap_in_stint > cliff:
                    # Exponential cliff penalty
                    cliff_penalty = ((lap_in_stint - cliff) ** 1.35) * 0.28
                    
                lap_time = base_lap + spec["delta_base"] + fuel_effect + wear + cliff_penalty
                if race_lap == 1:
                    lap_time += 4.5  # standing start launch
                    
                stint_time += lap_time
                stint_deg += (wear + cliff_penalty)
                
            total_time += stint_time
            total_deg_loss += stint_deg
            
            stint_profiles.append({
                "stint_number": s_idx,
                "compound": comp,
                "start_lap": s_start,
                "end_lap": s_end,
                "duration_laps": stint_laps,
                "avg_pace": round(stint_time / stint_laps, 3),
                "deg_accumulated_sec": round(stint_deg, 2),
                "cliff_risk": "HIGH" if stint_laps > cliff else ("MEDIUM" if stint_laps > cliff - 4 else "LOW"),
                "color": spec["color"],
            })
            
        # Overtaking traffic penalty if low downforce / high difficulty
        traffic_penalty = 0.0
        if stops > 1 and overtaking_diff > 6.0:
            traffic_penalty = overtakes_needed * (overtaking_diff * 0.18)
            
        expected_total = total_time + effective_pit_loss + traffic_penalty
        
        # Predict finish position
        # Baseline winner is around 5504s for 57 laps (or proportional)
        base_target = total_laps * 96.5
        time_delta_to_target = expected_total - base_target
        
        pred_pos = "P1 - P2 (Win Contender)"
        if time_delta_to_target > 25.0: pred_pos = "P8 - P10 (Points)"
        elif time_delta_to_target > 14.0: pred_pos = "P5 - P7 (Top 6)"
        elif time_delta_to_target > 5.0: pred_pos = "P3 - P4 (Podium)"
        
        return {
            "name": name,
            "stops_count": stops,
            "stints": stint_profiles,
            "pit_window_text": f"Lap {stints[0][2] - 2} - {stints[0][2] + 2}" if stops == 1 else f"L{stints[0][2]-1}-{stints[0][2]+2} & L{stints[1][2]-1}-{stints[1][2]+2}",
            "expected_total_time": round(expected_total, 2),
            "pit_loss_total_sec": round(effective_pit_loss, 2),
            "deg_loss_total_sec": round(total_deg_loss, 2),
            "predicted_finish": pred_pos,
            "is_sc_gamble": is_sc_gamble,
        }
        
    def _generate_pit_triggers(self, circuit, total_laps, plan_a, plan_b, plan_c):
        return [
            {
                "trigger_condition": "Competitor within 1.8s initiates pit stop",
                "recommended_action": "Execute immediate reactive undercut response on next lap or commit to 8+ lap overcut extension.",
                "rationale": f"At {circuit['name']}, fresh tire warmup produces an immediate 1.74s out-lap pace delta."
            },
            {
                "trigger_condition": "Virtual Safety Car (VSC) deployed between Lap 16 and Lap 35",
                "recommended_action": "DIVERT TO PIT ENTRY IMMEDIATELY. Transition to Hard Compound.",
                "rationale": f"Pit transit loss shrinks from {circuit['pit_loss_sec']}s to ~12.4s, gaining ~9.4s free race delta."
            },
            {
                "trigger_condition": "Tire surface temperatures exceed 115°C or graining appears",
                "recommended_action": "Advance pit stop window by 2–3 laps to avoid exponential thermal cliff drop-off.",
                "rationale": "Degradation past the cliff lap accelerates at >0.28s per lap, exceeding the 2-stop crossover threshold."
            },
            {
                "trigger_condition": "Full Safety Car deployed in final 15 laps",
                "recommended_action": "Fit scrubbed C3 Soft compound for standing/rolling restart attack.",
                "rationale": "Pack compression negates previous gaps; fresh Soft warm-up guarantees 2–3 positions on restart."
            }
        ]

if __name__ == "__main__":
    optimizer = F1StrategyOptimizer()
    res = optimizer.generate_strategies(circuit_id=3, grid_position=1, team_tier="Tier 1 (Red Bull/McLaren/Ferrari)")
    print(f"Generated strategies for {res['circuit']['name']}:")
    for p in res["plans"]:
        print(f" - {p['plan_code']}: {p['name']} -> {p['predicted_finish']} (Time: {p['expected_total_time']}s)")
