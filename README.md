# 🏎️ Formula 1 Race Telemetry & Strategy Analytics Platform (Project 32)
### Delivering the "Race Strategy Dashboard" — Resolving *"How do race strategies influence Formula 1 performance?"*

An interactive, high-performance Formula 1 race strategy and telemetry platform built using **FIA circuits data (77 global tracks)**, **historical race calendars (1950–2024)**, and **multi-driver lap telemetry modeling**.

---

## 👥 Project Team
* **Sri Harsh** &bull; `2503a52740`
* **Manohar** &bull; `2503a52766`
* **Jayavardhan** &bull; `2503a52747`

---

## 🌐 Live Web & Dashboard Link
* **GitHub Pages Web App**: [https://mothiwarsriharshgoud-dev.github.io/f1-race-strategy-dashboard/](https://mothiwarsriharshgoud-dev.github.io/f1-race-strategy-dashboard/)
* **GitHub Repository**: [https://github.com/mothiwarsriharshgoud-dev/f1-race-strategy-dashboard](https://github.com/mothiwarsriharshgoud-dev/f1-race-strategy-dashboard)

---

## 🌟 Core Features & Modules

### 1. Multi-Track & Multi-Dimensional Strategy Engine
- **Track Profiles (77 Circuits)**: Distinct degradation rates, pit transit deltas, and stop counts (Monaco 78 laps 1-stop vs. Bahrain 57 laps 2-stop vs. Lusail Qatar 57 laps mandatory 3-stop).
- **Grid Position Adaptation**: Strategies dynamically re-tailor for Front Row (P1-P2 clean air defense), Upper Hunters (P3-P6 early undercut strike), Midfield (P7-P12 traffic window split), and Back of Grid (P13-P20 radical reverse hard stint).
- **Live Safety Car / VSC Simulation Console**: Real-time +12.6s Free Pit Stop Dividend calculation, deployment lap scrubber, and automatic tactical plan re-optimization.

### 2. 2024 F1 Race Car CAD Platform
- High-fidelity 3D aerodynamic platform with 5 inspection hotspots (Front Wing, 18" BBS Wheels, Halo structure, Underfloor Venturi tunnels, and Rear Wing DRS Actuator).
- Interactive DRS flap control triggering live Drag ($C_d$) reduction from 0.88 to 0.63 and straight-line top speed boost to 352 km/h.

### 3. Lap Pace & Telemetry HUD
- Compare high-frequency lap times across Verstappen, Norris, Leclerc, Russell, Sainz, and Hamilton.
- Dynamic moving average smoothing to filter out traffic perturbations.
- Scaled Driver Stint Gantt timeline with caution intervention markers.

### 4. Tire Degradation & Exponential Thermal Cliff
- Empirical compound degradation rates ($+0.082\text{ s/lap}$ Soft vs. $+0.052\text{ s/lap}$ Medium vs. $+0.028\text{ s/lap}$ Hard).
- Fuel burn mass compensation toggle ($ -0.062\text{ s/lap}$ vehicle lightening).
- Non-linear thermal cliff curve visualization ($D(t) = D_{\text{base}} + \beta t + \gamma e^{t - L_{\text{cliff}}}$).

---

## 🚀 How to Run Locally

### In Any Web Browser:
Open `index.html` located at:
```powershell
Start-Process "C:\Users\Main User\.gemini\antigravity\scratch\f1-race-strategy-dashboard\index.html"
```
The application is self-contained with embedded telemetry data, ensuring instant offline rendering.
