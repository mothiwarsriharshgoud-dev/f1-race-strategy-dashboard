# 🏎️ Formula 1 Race Telemetry & Strategy Analytics Platform (Project 32)
### Delivering the "Race Strategy Dashboard" — Resolving *"How do race strategies influence Formula 1 performance?"*

An interactive, high-performance Formula 1 race strategy and telemetry platform built using **FIA circuits data (77 global tracks)**, **historical race calendars (1950–2024)**, and **multi-driver lap telemetry modeling**.

---

## 📁 Project Structure

```
C:\Users\Main User\.gemini\antigravity\scratch\f1-race-strategy-dashboard/
├── data/
│   ├── circuits.csv                 # 77 Formula 1 circuits with lat, lng, altitude, location
│   ├── races.csv                    # Complete historical F1 races calendar
│   └── f1_strategy_dataset.json      # Structured telemetry, degradation slopes & strategic KPIs
├── index.html                       # Complete, self-contained interactive web dashboard
├── generate_f1_strategy_data.py      # Python data engineering & telemetry synthesis script
├── build_dashboard_html.py          # Dashboard builder script
└── README.md                        # Documentation & project guide
```

---

## 🌟 Core Features & Modules

### 1. Lap Pace & Telemetry HUD
- **Interactive Multi-Driver Telemetry**: Compare lap times for Verstappen, Norris, Leclerc, Russell, Sainz, Hamilton, and Piastri.
- **Dynamic 3-Lap Smoothing**: Toggle between raw telemetry noisy traces and moving averages to filter traffic perturbations.
- **Cumulative Gap-to-Leader**: Trace exact time deltas (s) relative to the race leader.
- **Driver Stint Gantt Timeline**: Horizontal color-coded compound stints (Soft `#E10600`, Medium `#FFF200`, Hard `#FFFFFF`) highlighting pit in/out laps.

### 2. Tire Degradation & Wear Modeling
- **Tyre Life vs. Lap Time Scatter & Linear Regression**: Empirical degradation rates ($\text{s/lap}$) per Pirelli compound.
- **Fuel-Burn Mass Correction Toggle**: Adjusts for the $-0.062\text{ s/lap}$ car lightening effect as fuel burns off to isolate genuine rubber degradation from vehicle weight dynamics.
- **The Thermal Cliff**: Explains and visualizes the critical crossover point where tire wear spikes and forces a pit stop.

### 3. Pit Stop & Undercut Dynamics
- **Undercut Success Rate (68.4%)**: Explores out-lap deltas and compound warmup advantages.
- **Virtual Safety Car & Safety Car Arbitrage**: Visualizes the $+9.4\text{s}$ to $+12.0\text{s}$ pit transit dividend under race neutralizations.
- **Real-World 2024 Case Studies**: Highlights key tactical battles (Hungarian GP, Miami GP, Monza 1-stop masterclass, Belgian GP, Spanish GP).

### 4. Global Circuit Strategy Atlas (77 Tracks)
- Complete database of all 77 historical and active circuits from the provided dataset.
- Filters for **High Altitude (>200m)** vs. **Sea Level (<50m)** circuits, analyzing how atmospheric density impacts aerodynamic sliding and tire graining.
- Strategic profiles: Pit lane time loss, tire stress index, and typical 1-stop vs. 2-stop allocations.

### 5. Live Race Strategy Simulator (What-If Calculator)
- Configure initial compound, stint lengths, pit stop laps, track temperature, and Safety Car deployment.
- Real-time simulation engine calculates total race time, pit loss penalties, and thermal cliff costs, predicting the final finishing position against the real winning benchmark.

---

## 🚀 How to Open and Use the Dashboard

### In Any Web Browser:
Simply double-click or open `index.html` located at:
```
C:\Users\Main User\.gemini\antigravity\scratch\f1-race-strategy-dashboard\index.html
```

Or open it via command line:
```powershell
Start-Process "C:\Users\Main User\.gemini\antigravity\scratch\f1-race-strategy-dashboard\index.html"
```

The application is completely self-contained with zero external CDN dependencies, ensuring instant, offline-capable rendering.
