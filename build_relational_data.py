import os
import json
import pandas as pd
import numpy as np

DATA_DIR = "C:/Users/Main User/.gemini/antigravity/scratch/f1-race-strategy-dashboard/data"
JSON_PATH = os.path.join(DATA_DIR, "f1_strategy_dataset.json")

with open(JSON_PATH, "r", encoding="utf-8") as f:
    f1_data = json.load(f)

# 1. Dim_Circuits
circuits_df = pd.DataFrame(f1_data["circuits"])
circuits_csv = os.path.join(DATA_DIR, "Dim_Circuits.csv")
circuits_df.to_csv(circuits_csv, index=False)
print("Saved Dim_Circuits.csv:", len(circuits_df))

# 2. Dim_Races
races_df = pd.DataFrame(f1_data["races_2024"])
races_csv = os.path.join(DATA_DIR, "Dim_Races.csv")
races_df.to_csv(races_csv, index=False)
print("Saved Dim_Races.csv:", len(races_df))

# 3. Fact_LapTelemetry
laps_df = pd.DataFrame(f1_data["bahrain_telemetry_laps"])
laps_csv = os.path.join(DATA_DIR, "Fact_LapTelemetry.csv")
laps_df.to_csv(laps_csv, index=False)
print("Saved Fact_LapTelemetry.csv:", len(laps_df))

# 4. Fact_StrategyBattles
battles_df = pd.DataFrame(f1_data["pit_stop_battles"])
battles_csv = os.path.join(DATA_DIR, "Fact_StrategyBattles.csv")
battles_df.to_csv(battles_csv, index=False)
print("Saved Fact_StrategyBattles.csv:", len(battles_df))

# 5. Fact_RaceResults (2024 season finishing results & strategy impact)
results_records = [
    {"race": "Bahrain GP", "driver": "VER", "team": "Red Bull", "grid": 1, "finish": 1, "pos_change": 0, "points": 26, "stops": 2, "strategy": "Soft-Hard-Soft"},
    {"race": "Bahrain GP", "driver": "PER", "team": "Red Bull", "grid": 5, "finish": 2, "pos_change": 3, "points": 18, "stops": 2, "strategy": "Soft-Hard-Soft"},
    {"race": "Bahrain GP", "driver": "SAI", "team": "Ferrari", "grid": 4, "finish": 3, "pos_change": 1, "points": 15, "stops": 2, "strategy": "Soft-Hard-Hard"},
    {"race": "Bahrain GP", "driver": "LEC", "team": "Ferrari", "grid": 2, "finish": 4, "pos_change": -2, "points": 12, "stops": 2, "strategy": "Soft-Hard-Hard"},
    {"race": "Bahrain GP", "driver": "RUS", "team": "Mercedes", "grid": 3, "finish": 5, "pos_change": -2, "points": 10, "stops": 2, "strategy": "Soft-Hard-Hard"},
    {"race": "Bahrain GP", "driver": "NOR", "team": "McLaren", "grid": 7, "finish": 6, "pos_change": 1, "points": 8, "stops": 2, "strategy": "Soft-Hard-Hard"},
    {"race": "Bahrain GP", "driver": "HAM", "team": "Mercedes", "grid": 9, "finish": 7, "pos_change": 2, "points": 6, "stops": 2, "strategy": "Soft-Hard-Hard"},
    {"race": "Bahrain GP", "driver": "PIA", "team": "McLaren", "grid": 8, "finish": 8, "pos_change": 0, "points": 4, "stops": 2, "strategy": "Soft-Hard-Hard"},
    {"race": "Bahrain GP", "driver": "ALO", "team": "Aston Martin", "grid": 6, "finish": 9, "pos_change": -3, "points": 2, "stops": 2, "strategy": "Soft-Hard-Hard"},
    {"race": "Bahrain GP", "driver": "STR", "team": "Aston Martin", "grid": 12, "finish": 10, "pos_change": 2, "points": 1, "stops": 2, "strategy": "Soft-Hard-Hard"},
    {"race": "Miami GP", "driver": "NOR", "team": "McLaren", "grid": 5, "finish": 1, "pos_change": 4, "points": 25, "stops": 1, "strategy": "Medium-Hard (SC Overcut)"},
    {"race": "Miami GP", "driver": "VER", "team": "Red Bull", "grid": 1, "finish": 2, "pos_change": -1, "points": 18, "stops": 1, "strategy": "Medium-Hard"},
    {"race": "Miami GP", "driver": "LEC", "team": "Ferrari", "grid": 2, "finish": 3, "pos_change": -1, "points": 15, "stops": 1, "strategy": "Medium-Hard"},
    {"race": "Monza GP", "driver": "LEC", "team": "Ferrari", "grid": 4, "finish": 1, "pos_change": 3, "points": 25, "stops": 1, "strategy": "Medium-Hard (1-Stop Masterclass)"},
    {"race": "Monza GP", "driver": "PIA", "team": "McLaren", "grid": 2, "finish": 2, "pos_change": 0, "points": 18, "stops": 2, "strategy": "Medium-Hard-Hard (2-Stop Defeated)"},
    {"race": "Monza GP", "driver": "NOR", "team": "McLaren", "grid": 1, "finish": 3, "pos_change": -2, "points": 16, "stops": 2, "strategy": "Medium-Hard-Hard"},
]
results_df = pd.DataFrame(results_records)
results_csv = os.path.join(DATA_DIR, "Fact_RaceResults.csv")
results_df.to_csv(results_csv, index=False)
print("Saved Fact_RaceResults.csv:", len(results_df))

# 6. Build Multi-Tab Excel Workbook
excel_path = os.path.join(DATA_DIR, "F1_Project32_Strategy_Dataset.xlsx")
with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
    circuits_df.to_excel(writer, sheet_name="Dim_Circuits", index=False)
    races_df.to_excel(writer, sheet_name="Dim_Races", index=False)
    results_df.to_excel(writer, sheet_name="Fact_RaceResults", index=False)
    battles_df.to_excel(writer, sheet_name="Fact_StrategyBattles", index=False)
    laps_df.head(250).to_excel(writer, sheet_name="Sample_LapTelemetry", index=False)
print(f"Saved Excel workbook to: {excel_path}")
