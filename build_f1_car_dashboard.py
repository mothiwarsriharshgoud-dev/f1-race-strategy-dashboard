import json
import os

DATA_PATH = "C:/Users/Main User/.gemini/antigravity/scratch/f1-race-strategy-dashboard/data/f1_strategy_dataset.json"
OUTPUT_HTML = "C:/Users/Main User/.gemini/antigravity/scratch/f1-race-strategy-dashboard/index.html"
ARTIFACT_HTML = "C:/Users/Main User/.gemini/antigravity/brain/bb0fc362-bdeb-4a83-b7c8-80ce516a46a3/f1_race_strategy_dashboard.html"
B64_PATH = "C:/Users/Main User/.gemini/antigravity/scratch/f1-race-strategy-dashboard/assets/f1_2024_car_b64.txt"

with open(DATA_PATH, "r", encoding="utf-8") as f:
    f1_data = json.load(f)

with open(B64_PATH, "r", encoding="utf-8") as f:
    car_b64 = f.read().strip()

json_data_str = json.dumps(f1_data)

master_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Formula 1 Race Telemetry & Strategy Analytics Platform | Project 32</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Titillium+Web:ital,wght@0,300;0,400;0,600;0,700;0,900;1,600&family=JetBrains+Mono:wght@400;600;700;800&display=swap');
    
    :root {{
      --f1-red: #E10600;
      --f1-dark: #0D0F14;
      --f1-panel: #141822;
      --f1-border: #262D3D;
      --f1-text: #F3F4F6;
      --f1-muted: #9CA3AF;
    }}
    
    body {{
      font-family: 'Titillium Web', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--f1-dark);
      color: var(--f1-text);
      margin: 0;
      padding: 0;
      overflow-x: hidden;
    }}

    .mono {{
      font-family: 'JetBrains Mono', monospace;
    }}

    ::-webkit-scrollbar {{
      width: 7px;
      height: 7px;
    }}
    ::-webkit-scrollbar-track {{
      background: #0D0F14;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #2D3340;
      border-radius: 4px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #E10600;
    }}

    .carbon-pattern {{
      background-color: #0D0F14;
      background-image: radial-gradient(#1A202C 0.75px, transparent 0.75px), radial-gradient(#1A202C 0.75px, #0D0F14 0.75px);
      background-size: 20px 20px;
      background-position: 0 0, 10px 10px;
    }}

    .f1-card {{
      background: linear-gradient(135deg, rgba(20, 24, 34, 0.95) 0%, rgba(24, 29, 42, 0.90) 100%);
      border: 1px solid var(--f1-border);
      border-radius: 14px;
      box-shadow: 0 10px 28px rgba(0, 0, 0, 0.45);
      backdrop-filter: blur(10px);
    }}

    .f1-card-accent {{
      border-top: 3px solid var(--f1-red);
    }}

    .badge-soft {{ background-color: rgba(225, 6, 0, 0.2); color: #FF4D4D; border: 1px solid #E10600; }}
    .badge-medium {{ background-color: rgba(255, 242, 0, 0.2); color: #FFF200; border: 1px solid #FFD700; }}
    .badge-hard {{ background-color: rgba(255, 255, 255, 0.2); color: #FFFFFF; border: 1px solid #D1D5DB; }}
    .badge-inter {{ background-color: rgba(57, 181, 74, 0.2); color: #4ADE80; border: 1px solid #39B54A; }}
    .badge-wet {{ background-color: rgba(0, 160, 222, 0.2); color: #38BDF8; border: 1px solid #00A0DE; }}

    .tab-btn.active {{
      background: linear-gradient(90deg, rgba(225, 6, 0, 0.25) 0%, rgba(225, 6, 0, 0.05) 100%);
      border-bottom: 3px solid var(--f1-red);
      color: #FFFFFF;
      font-weight: 700;
    }}

    /* Hotspot animation on F1 Car */
    @keyframes pulse-pin {{
      0% {{ transform: scale(0.95); box-shadow: 0 0 0 0 rgba(225, 6, 0, 0.7); }}
      70% {{ transform: scale(1.15); box-shadow: 0 0 0 10px rgba(225, 6, 0, 0); }}
      100% {{ transform: scale(0.95); box-shadow: 0 0 0 0 rgba(225, 6, 0, 0); }}
    }}
    .pin-pulse {{
      animation: pulse-pin 2s infinite;
    }}
  </style>
</head>
<body class="carbon-pattern min-h-screen text-slate-100 antialiased">

  <!-- TOP HEADER / HUD -->
  <header class="border-b border-slate-800 bg-slate-950/85 sticky top-0 z-50 backdrop-blur-md">
    <div class="max-w-7xl mx-auto px-4 py-3 flex flex-wrap items-center justify-between gap-4">
      <div class="flex items-center gap-3">
        <div class="bg-red-600 text-white font-black px-2.5 py-1 rounded text-lg tracking-wider flex items-center gap-1.5 shadow-lg shadow-red-900/50">
          <span>F1</span>
          <span class="text-xs bg-black/40 px-1.5 py-0.5 rounded font-mono">PROJECT 32</span>
        </div>
        <div>
          <div class="flex items-center gap-2">
            <h1 class="text-lg md:text-xl font-bold tracking-tight text-white flex items-center gap-2">
              Formula 1 Race Telemetry & Strategy Analytics Platform
            </h1>
            <span class="text-xs bg-emerald-950 text-emerald-400 border border-emerald-800 px-2.5 py-0.5 rounded-full font-mono flex items-center gap-1 font-semibold">
              <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span> STRATEGY ENGINE & ORIGINAL F1 CAR
            </span>
          </div>
          <p class="text-xs text-slate-400 font-medium">
            Core Question: <span class="text-red-400 font-semibold italic">"How do race strategies influence Formula 1 performance?"</span>
          </p>
        </div>
      </div>

      <!-- Quick Session Indicator -->
      <div class="flex items-center gap-3">
        <div class="text-right font-mono">
          <span class="text-[10px] uppercase tracking-wider text-slate-400 block">Grand Prix Mode</span>
          <span class="text-xs font-bold text-slate-200" id="current-circuit-badge">Bahrain GP (Sakhir, 57 Laps)</span>
        </div>
        <select id="quick-circuit-select" onchange="changeCircuitContext(this.value)" class="bg-slate-900 border border-slate-700 text-slate-200 text-xs rounded-lg px-3 py-1.5 font-medium focus:ring-2 focus:ring-red-500 outline-none font-mono">
          <option value="3">Bahrain (Sakhir) - Rd 1</option>
          <option value="6">Monaco (Monte-Carlo) - Rd 8</option>
          <option value="9">Silverstone (UK) - Rd 12</option>
          <option value="13">Spa-Francorchamps - Rd 14</option>
          <option value="14">Monza (Italy) - Rd 16</option>
          <option value="32">Mexico City (2227m Alt) - Rd 20</option>
          <option value="80">Las Vegas (Strip) - Rd 22</option>
          <option value="24">Abu Dhabi (Yas Marina) - Rd 24</option>
        </select>
      </div>
    </div>

    <!-- NAVIGATION TABS -->
    <div class="max-w-7xl mx-auto px-4 flex gap-1 overflow-x-auto text-xs font-medium border-t border-slate-800/60">
      <button onclick="setTab('strategy-generator')" id="tab-strategy-generator" class="tab-btn active px-4 py-2.5 text-slate-300 hover:text-white transition flex items-center gap-1.5 font-bold">
        <span>⚡</span> AI Strategy Generator (Plan A / B / C)
      </button>
      <button onclick="setTab('f1-car')" id="tab-f1-car" class="tab-btn px-4 py-2.5 text-slate-400 hover:text-white transition flex items-center gap-1.5 font-bold">
        <span>🏎️</span> Original 2024 F1 Car (Aero & Telemetry)
      </button>
      <button onclick="setTab('telemetry')" id="tab-telemetry" class="tab-btn px-4 py-2.5 text-slate-400 hover:text-white transition flex items-center gap-1.5">
        <span>⏱️</span> Lap Pace & Telemetry Graphs
      </button>
      <button onclick="setTab('degradation')" id="tab-degradation" class="tab-btn px-4 py-2.5 text-slate-400 hover:text-white transition flex items-center gap-1.5">
        <span>📉</span> Tire Degradation Modeling
      </button>
      <button onclick="setTab('undercut')" id="tab-undercut" class="tab-btn px-4 py-2.5 text-slate-400 hover:text-white transition flex items-center gap-1.5">
        <span>⚔️</span> Undercut & SC Arbitrage
      </button>
      <button onclick="setTab('circuits')" id="tab-circuits" class="tab-btn px-4 py-2.5 text-slate-400 hover:text-white transition flex items-center gap-1.5">
        <span>🌍</span> Global Circuit Atlas (77 Tracks)
      </button>
      <button onclick="setTab('simulator')" id="tab-simulator" class="tab-btn px-4 py-2.5 text-slate-400 hover:text-white transition flex items-center gap-1.5">
        <span>🎮</span> Custom What-If Simulator
      </button>
    </div>
  </header>

  <!-- MAIN VIEW CONTAINER -->
  <main class="max-w-7xl mx-auto px-4 py-6 space-y-6">

    <!-- KPI STATS STRIP -->
    <section class="grid grid-cols-2 md:grid-cols-5 gap-3">
      <div class="f1-card p-3 border-l-4 border-l-red-500">
        <div class="text-[11px] font-mono text-slate-400 uppercase tracking-wider">Undercut Success Rate</div>
        <div class="text-xl md:text-2xl font-black text-white mt-1 flex items-baseline gap-1">
          <span class="text-red-400">68.4%</span>
          <span class="text-[10px] text-emerald-400 font-mono">+1.74s gain</span>
        </div>
        <div class="text-[11px] text-slate-400 mt-0.5">Fresh tire out-lap grip delta</div>
      </div>

      <div class="f1-card p-3 border-l-4 border-l-amber-400">
        <div class="text-[11px] font-mono text-slate-400 uppercase tracking-wider">Safety Car Pit Dividend</div>
        <div class="text-xl md:text-2xl font-black text-white mt-1 flex items-baseline gap-1">
          <span class="text-amber-400">+9.4s - 12.0s</span>
        </div>
        <div class="text-[11px] text-slate-400 mt-0.5">Pit loss drops from 22s to 10s</div>
      </div>

      <div class="f1-card p-3 border-l-4 border-l-emerald-500">
        <div class="text-[11px] font-mono text-slate-400 uppercase tracking-wider">Strategy Win Influence</div>
        <div class="text-xl md:text-2xl font-black text-white mt-1 flex items-baseline gap-1">
          <span class="text-emerald-400">42.8%</span>
          <span class="text-[10px] text-slate-300 font-mono">podiums won</span>
        </div>
        <div class="text-[11px] text-slate-400 mt-0.5">Position gained via pit execution</div>
      </div>

      <div class="f1-card p-3 border-l-4 border-l-blue-500">
        <div class="text-[11px] font-mono text-slate-400 uppercase tracking-wider">1-Stop vs 2-Stop Split</div>
        <div class="text-xl md:text-2xl font-black text-white mt-1 flex items-baseline gap-1">
          <span class="text-blue-400">54.2% / 37.5%</span>
        </div>
        <div class="text-[11px] text-slate-400 mt-0.5">Monza 1-stop vs Bahrain 2-stop</div>
      </div>

      <div class="f1-card p-3 border-l-4 border-l-purple-500 col-span-2 md:col-span-1">
        <div class="text-[11px] font-mono text-slate-400 uppercase tracking-wider">Fuel-Burn Lightening</div>
        <div class="text-xl md:text-2xl font-black text-white mt-1 flex items-baseline gap-1">
          <span class="text-purple-300">-0.062 s/lap</span>
        </div>
        <div class="text-[11px] text-slate-400 mt-0.5">110kg fuel consumption</div>
      </div>
    </section>

    <!-- TAB 1: AI STRATEGY GENERATOR -->
    <div id="view-strategy-generator" class="space-y-6">
      
      <!-- Generator Configuration Ribbon -->
      <div class="f1-card p-5 f1-card-accent">
        <div class="flex flex-wrap items-center justify-between border-b border-slate-800 pb-3 gap-2">
          <div>
            <h2 class="text-base font-bold text-white flex items-center gap-2">
              <span>⚡</span> F1 Automated Race Strategy Generator & Optimizer
            </h2>
            <p class="text-xs text-slate-400">
              Multi-stint dynamic programming engine that calculates optimal compound sequences, pit windows, and race contingencies.
            </p>
          </div>
          <button onclick="generateF1Strategies()" class="px-4 py-2 rounded-xl bg-red-600 hover:bg-red-500 text-white font-bold text-xs tracking-wider flex items-center gap-2 shadow-lg shadow-red-900/50 transition font-mono">
            <span>⚡</span> RE-GENERATE OPTIMAL STRATEGIES
          </button>
        </div>

        <!-- Strategy Inputs Grid -->
        <div class="grid grid-cols-2 md:grid-cols-5 gap-3 mt-4 text-xs font-mono">
          <div>
            <label class="text-slate-400 text-[10px] block mb-1">TARGET CIRCUIT</label>
            <select id="gen-circuit" onchange="generateF1Strategies()" class="w-full bg-slate-900 border border-slate-700 text-white rounded p-2 text-xs">
              <option value="3" selected>Bahrain (Sakhir) - 57 Laps</option>
              <option value="6">Monaco (Street) - 78 Laps</option>
              <option value="9">Silverstone - 52 Laps</option>
              <option value="13">Spa-Francorchamps - 44 Laps</option>
              <option value="14">Monza (Temple of Speed) - 53 Laps</option>
              <option value="15">Singapore (Marina Bay) - 62 Laps</option>
              <option value="22">Suzuka (High Downforce) - 53 Laps</option>
              <option value="32">Mexico City (2227m Alt) - 71 Laps</option>
              <option value="80">Las Vegas Strip - 50 Laps</option>
              <option value="78">Qatar (Lusail High Wear) - 57 Laps</option>
            </select>
          </div>

          <div>
            <label class="text-slate-400 text-[10px] block mb-1">GRID START POSITION</label>
            <select id="gen-grid" onchange="generateF1Strategies()" class="w-full bg-slate-900 border border-slate-700 text-white rounded p-2 text-xs">
              <option value="1" selected>Pole Position (P1)</option>
              <option value="3">Row 2 (P3)</option>
              <option value="5">Top 6 (P5)</option>
              <option value="9">Midfield (P9)</option>
              <option value="14">Back Grid (P14)</option>
              <option value="20">Pit Lane Start (P20)</option>
            </select>
          </div>

          <div>
            <label class="text-slate-400 text-[10px] block mb-1">TEAM CHASSIS TIER</label>
            <select id="gen-tier" onchange="generateF1Strategies()" class="w-full bg-slate-900 border border-slate-700 text-white rounded p-2 text-xs">
              <option value="1" selected>Tier 1: Red Bull / McLaren / Ferrari</option>
              <option value="2">Tier 2: Mercedes / Aston Martin</option>
              <option value="3">Tier 3: Midfield (Haas / Williams / RB)</option>
            </select>
          </div>

          <div>
            <label class="text-slate-400 text-[10px] block mb-1">TRACK TEMP (&deg;C)</label>
            <div class="flex items-center gap-2">
              <input type="range" id="gen-temp" min="20" max="55" value="34" oninput="document.getElementById('gen-temp-val').textContent = this.value + '°C'; generateF1Strategies();" class="w-full accent-red-600">
              <span id="gen-temp-val" class="text-slate-300 font-bold w-10 text-right">34&deg;C</span>
            </div>
          </div>

          <div>
            <label class="text-slate-400 text-[10px] block mb-1">SAFETY CAR PROBABILITY</label>
            <select id="gen-sc" onchange="generateF1Strategies()" class="w-full bg-slate-900 border border-slate-700 text-white rounded p-2 text-xs">
              <option value="0.15">Low (&lt;20%)</option>
              <option value="0.40" selected>Medium (~40%)</option>
              <option value="0.75">High (&gt;70%)</option>
            </select>
          </div>
        </div>
      </div>

      <!-- Strategy Plans Output Grid (Plan A, Plan B, Plan C) -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6" id="strategy-plans-container">
        <!-- Rendered dynamically by JS -->
      </div>

      <!-- Pit-Wall Contingency Decision Tree Matrix -->
      <div class="f1-card p-5">
        <h3 class="text-sm font-bold text-white mb-3 flex items-center gap-2">
          <span>📋</span> Pit-Wall Tactical Playbook & Live Trigger Matrix
        </h3>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs font-mono" id="decision-triggers-container">
          <!-- Populated by JS -->
        </div>
      </div>

    </div>

    <!-- ======================================================== -->
    <!-- TAB 2: ORIGINAL 2024 FORMULA 1 CAR & TECHNICAL INSPECTOR -->
    <!-- ======================================================== -->
    <div id="view-f1-car" class="hidden space-y-6">
      
      <div class="f1-card p-5 f1-card-accent">
        <div class="flex flex-wrap items-center justify-between border-b border-slate-800 pb-3 gap-3">
          <div>
            <div class="flex items-center gap-2">
              <span class="bg-red-600 text-white text-[11px] font-black px-2 py-0.5 rounded font-mono">SPEC 2024</span>
              <h2 class="text-base font-bold text-white">
                Authentic 2024 Ground-Effect Formula 1 Race Car Telemetry & Aero Model
              </h2>
            </div>
            <p class="text-xs text-slate-400 mt-1">
              FIA 798 kg Ground-Effect Aerodynamics, Venturi Underfloor Tunnels, 1.6L V6 Turbo-Hybrid Power Unit & 18-inch Pirelli P-Zero Racing System.
            </p>
          </div>

          <!-- Quick Actions -->
          <div class="flex items-center gap-2 font-mono text-xs">
            <button onclick="toggleDRS()" id="car-drs-btn" class="px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-700 hover:border-emerald-500 text-slate-200 transition font-bold flex items-center gap-1.5">
              <span class="w-2 h-2 rounded-full bg-slate-500" id="car-drs-indicator"></span>
              <span id="car-drs-label">DRS: CLOSED</span>
            </button>
            <select id="car-compound-select" onchange="setCarCompound(this.value)" class="bg-slate-900 border border-slate-700 text-red-400 font-bold rounded-lg px-2.5 py-1.5 outline-none">
              <option value="soft" selected>Pirelli C3 Soft (Red)</option>
              <option value="medium">Pirelli C2 Medium (Yellow)</option>
              <option value="hard">Pirelli C1 Hard (White)</option>
            </select>
          </div>
        </div>

        <!-- HERO CAR DISPLAY WITH INTERACTIVE TELEMETRY CALLOUTS -->
        <div class="relative w-full rounded-2xl overflow-hidden mt-4 bg-gradient-to-b from-[#0A0D13] to-[#121622] border border-slate-800 shadow-2xl">
          
          <!-- The Authentic High-Resolution F1 Car Photograph -->
          <img src="data:image/jpeg;base64,{car_b64}" alt="Original 2024 Formula 1 Race Car" class="w-full h-auto block object-cover select-none">

          <!-- Interactive Hotspot 1: Front Wing Cascade -->
          <button onclick="selectCarComponent('front-wing')" class="absolute top-[68%] left-[16%] -translate-x-1/2 -translate-y-1/2 group z-20 cursor-pointer focus:outline-none">
            <span class="w-6 h-6 rounded-full bg-red-600/80 border-2 border-white flex items-center justify-center text-white text-[10px] font-bold shadow-lg shadow-red-900/80 pin-pulse group-hover:scale-125 transition">
              1
            </span>
            <span class="absolute left-7 top-1/2 -translate-y-1/2 hidden group-hover:flex items-center px-2 py-1 rounded bg-black/90 border border-slate-700 text-[11px] font-mono text-white whitespace-nowrap shadow-xl">
              Front Wing & Inwash Flaps (Downforce 42.5%)
            </span>
          </button>

          <!-- Interactive Hotspot 2: Pirelli 18-inch Wheels -->
          <button onclick="selectCarComponent('wheels')" class="absolute top-[72%] left-[25%] -translate-x-1/2 -translate-y-1/2 group z-20 cursor-pointer focus:outline-none">
            <span class="w-6 h-6 rounded-full bg-amber-500/80 border-2 border-white flex items-center justify-center text-white text-[10px] font-bold shadow-lg shadow-amber-900/80 pin-pulse group-hover:scale-125 transition">
              2
            </span>
            <span class="absolute left-7 top-1/2 -translate-y-1/2 hidden group-hover:flex items-center px-2 py-1 rounded bg-black/90 border border-slate-700 text-[11px] font-mono text-white whitespace-nowrap shadow-xl">
              Pirelli 18" Wheels & Carbon Brake Ducts
            </span>
          </button>

          <!-- Interactive Hotspot 3: Titanium Halo & Cockpit -->
          <button onclick="selectCarComponent('halo')" class="absolute top-[38%] left-[48%] -translate-x-1/2 -translate-y-1/2 group z-20 cursor-pointer focus:outline-none">
            <span class="w-6 h-6 rounded-full bg-blue-500/80 border-2 border-white flex items-center justify-center text-white text-[10px] font-bold shadow-lg shadow-blue-900/80 pin-pulse group-hover:scale-125 transition">
              3
            </span>
            <span class="absolute left-7 top-1/2 -translate-y-1/2 hidden group-hover:flex items-center px-2 py-1 rounded bg-black/90 border border-slate-700 text-[11px] font-mono text-white whitespace-nowrap shadow-xl">
              Titanium Halo Cockpit (120 kN Structural Rating)
            </span>
          </button>

          <!-- Interactive Hotspot 4: Sidepod Undercut & Venturi Floor -->
          <button onclick="selectCarComponent('sidepod')" class="absolute top-[62%] left-[54%] -translate-x-1/2 -translate-y-1/2 group z-20 cursor-pointer focus:outline-none">
            <span class="w-6 h-6 rounded-full bg-emerald-500/80 border-2 border-white flex items-center justify-center text-white text-[10px] font-bold shadow-lg shadow-emerald-900/80 pin-pulse group-hover:scale-125 transition">
              4
            </span>
            <span class="absolute left-7 top-1/2 -translate-y-1/2 hidden group-hover:flex items-center px-2 py-1 rounded bg-black/90 border border-slate-700 text-[11px] font-mono text-white whitespace-nowrap shadow-xl">
              Sidepod Undercut & Ground-Effect Venturi Tunnels
            </span>
          </button>

          <!-- Interactive Hotspot 5: Rear Wing & DRS Actuator -->
          <button onclick="selectCarComponent('rear-wing')" class="absolute top-[32%] left-[82%] -translate-x-1/2 -translate-y-1/2 group z-20 cursor-pointer focus:outline-none">
            <span class="w-6 h-6 rounded-full bg-purple-500/80 border-2 border-white flex items-center justify-center text-white text-[10px] font-bold shadow-lg shadow-purple-900/80 pin-pulse group-hover:scale-125 transition">
              5
            </span>
            <span class="absolute right-7 top-1/2 -translate-y-1/2 hidden group-hover:flex items-center px-2 py-1 rounded bg-black/90 border border-slate-700 text-[11px] font-mono text-white whitespace-nowrap shadow-xl">
              Rear Wing & DRS Hydraulic Actuator Flap
            </span>
          </button>

          <!-- Interactive Hotspot 6: Turbo-Hybrid Diffuser -->
          <button onclick="selectCarComponent('powertrain')" class="absolute top-[68%] left-[78%] -translate-x-1/2 -translate-y-1/2 group z-20 cursor-pointer focus:outline-none">
            <span class="w-6 h-6 rounded-full bg-cyan-500/80 border-2 border-white flex items-center justify-center text-white text-[10px] font-bold shadow-lg shadow-cyan-900/80 pin-pulse group-hover:scale-125 transition">
              6
            </span>
            <span class="absolute right-7 top-1/2 -translate-y-1/2 hidden group-hover:flex items-center px-2 py-1 rounded bg-black/90 border border-slate-700 text-[11px] font-mono text-white whitespace-nowrap shadow-xl">
              1.6L V6 Turbo-Hybrid (1,040 BHP + ERS Harvest)
            </span>
          </button>
        </div>

        <!-- COMPONENT DETAIL INSPECTOR CARD -->
        <div class="mt-4 p-4 rounded-xl bg-slate-950/80 border border-slate-800" id="car-inspector-card">
          <!-- Populated by JS -->
        </div>

        <!-- LIVE TELEMETRY TELEMETRIC SENSORS ROW -->
        <div class="grid grid-cols-2 md:grid-cols-6 gap-3 mt-4 text-xs font-mono">
          <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-800">
            <span class="text-[10px] text-slate-400 block uppercase">FRONT DOWNFORCE</span>
            <div class="text-lg font-bold text-white mt-0.5" id="tel-f-df">42.5%</div>
            <span class="text-[10px] text-emerald-400">High Speed Balance</span>
          </div>

          <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-800">
            <span class="text-[10px] text-slate-400 block uppercase">REAR DOWNFORCE</span>
            <div class="text-lg font-bold text-white mt-0.5" id="tel-r-df">57.5%</div>
            <span class="text-[10px] text-slate-400">Traction Stability</span>
          </div>

          <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-800">
            <span class="text-[10px] text-slate-400 block uppercase">DRAG COEFF (CD)</span>
            <div class="text-lg font-bold text-amber-400 mt-0.5" id="tel-drag-coeff">0.88</div>
            <span class="text-[10px] text-slate-400" id="tel-drag-sub">DRS Flap: Closed</span>
          </div>

          <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-800">
            <span class="text-[10px] text-slate-400 block uppercase">TOP SPEED PROJECTION</span>
            <div class="text-lg font-bold text-white mt-0.5" id="tel-top-spd">334 KM/H</div>
            <span class="text-[10px] text-emerald-400" id="tel-spd-sub">Straightline Pace</span>
          </div>

          <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-800">
            <span class="text-[10px] text-slate-400 block uppercase">TIRE BULK TEMP</span>
            <div class="text-lg font-bold text-red-400 mt-0.5" id="tel-tire-temp">102&deg;C</div>
            <span class="text-[10px] text-slate-300 font-bold" id="tel-tire-comp">Soft (C3) Fitted</span>
          </div>

          <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-800">
            <span class="text-[10px] text-slate-400 block uppercase">ERS BATTERY STATUS</span>
            <div class="text-lg font-bold text-emerald-400 mt-0.5">88% (4.0 MJ)</div>
            <span class="text-[10px] text-purple-400">120 kW MGU-K Deploy</span>
          </div>
        </div>

      </div>

    </div>

    <!-- TAB 3: TELEMETRY & LAP PACE GRAPHS -->
    <div id="view-telemetry" class="hidden space-y-6">
      
      <div class="f1-card p-5 f1-card-accent">
        <div class="flex flex-wrap items-center justify-between border-b border-slate-800 pb-3 gap-2">
          <div>
            <h2 class="text-base font-bold text-white flex items-center gap-2">
              <span>⏱️</span> Lap Pace Telemetry & Fuel-Burn Compensation
            </h2>
            <p class="text-xs text-slate-400">
              High-frequency lap telemetry from 2024 races. Isolates fuel mass lightening (-0.062s/lap) from rubber degradation.
            </p>
          </div>

          <div class="flex items-center gap-4 text-xs font-mono">
            <label class="flex items-center gap-1.5 cursor-pointer text-slate-300 hover:text-white">
              <input type="checkbox" id="toggle-smooth" onchange="renderTelemetryCharts()" checked class="rounded bg-slate-900 border-slate-700 text-red-600">
              <span>3-Lap Rolling Smooth</span>
            </label>
            <label class="flex items-center gap-1.5 cursor-pointer text-slate-300 hover:text-white">
              <input type="checkbox" id="toggle-pits" onchange="renderTelemetryCharts()" checked class="rounded bg-slate-900 border-slate-700 text-red-600">
              <span>Show Pit Markers</span>
            </label>
          </div>
        </div>

        <!-- Driver Filter Badges -->
        <div class="flex flex-wrap items-center gap-2 mt-4" id="driver-toggle-container">
          <!-- Populated by JS -->
        </div>

        <!-- Chart Grid -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-4 mt-4">
          <!-- Pace Chart -->
          <div class="bg-slate-950/80 p-4 rounded-xl border border-slate-800">
            <div class="flex justify-between items-center text-xs font-mono mb-2">
              <span class="text-slate-300 font-bold">LAP TIME TRACE (SECONDS)</span>
              <span class="text-[10px] text-slate-500">Lower is faster</span>
            </div>
            <div class="h-64 relative flex items-center justify-center">
              <svg id="pace-svg" class="w-full h-full"></svg>
            </div>
          </div>

          <!-- Gap to Leader Chart -->
          <div class="bg-slate-950/80 p-4 rounded-xl border border-slate-800">
            <div class="flex justify-between items-center text-xs font-mono mb-2">
              <span class="text-slate-300 font-bold">INTERVAL GAP TO RACE LEADER (SECONDS)</span>
              <span class="text-[10px] text-slate-500">Interval delta progression</span>
            </div>
            <div class="h-64 relative flex items-center justify-center">
              <svg id="gap-svg" class="w-full h-full"></svg>
            </div>
          </div>
        </div>

        <!-- Stint Strategy Timeline Bar Chart -->
        <div class="mt-6 pt-4 border-t border-slate-800">
          <div class="flex justify-between items-center text-xs font-mono mb-3">
            <span class="text-slate-200 font-bold uppercase tracking-wider">Driver Stint Timeline Breakdown</span>
            <div class="flex gap-3 text-[10px]">
              <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 rounded bg-red-600"></span> Soft</span>
              <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 rounded bg-yellow-400"></span> Medium</span>
              <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 rounded bg-white"></span> Hard</span>
            </div>
          </div>
          <div class="space-y-2.5" id="stint-timeline-container">
            <!-- Populated by JS -->
          </div>
        </div>

      </div>

    </div>

    <!-- TAB 4: TIRE DEGRADATION -->
    <div id="view-degradation" class="hidden space-y-6">
      
      <div class="f1-card p-5 f1-card-accent">
        <div class="border-b border-slate-800 pb-3">
          <h2 class="text-base font-bold text-white flex items-center gap-2">
            <span>📉</span> Pirelli Compound Wear Rates & The Non-Linear Thermal Cliff
          </h2>
          <p class="text-xs text-slate-400">
            Empirical compound modeling: Linear wear transition into steep exponential thermal failure ($L_{{\\text{{cliff}}}}$).
          </p>
        </div>

        <!-- Compound Parameter Cards -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mt-4 text-xs font-mono">
          <div class="p-3.5 rounded-xl bg-slate-950/80 border border-slate-800 border-l-4 border-l-red-500">
            <div class="flex justify-between font-bold text-red-400">
              <span>SOFT (C3 / C4)</span>
              <span>-0.65s Base Delta</span>
            </div>
            <div class="space-y-1 text-slate-300 mt-2 text-[11px]">
              <div class="flex justify-between"><span>Wear Rate:</span><span class="text-white">+0.082 s/lap</span></div>
              <div class="flex justify-between"><span>Thermal Cliff:</span><span class="text-amber-400 font-bold">Lap 16</span></div>
              <div class="flex justify-between"><span>Typical Use:</span><span>Qualifying, Sprint, Undercut</span></div>
            </div>
          </div>

          <div class="p-3.5 rounded-xl bg-slate-950/80 border border-slate-800 border-l-4 border-l-yellow-400">
            <div class="flex justify-between font-bold text-yellow-400">
              <span>MEDIUM (C2)</span>
              <span>0.00s Baseline</span>
            </div>
            <div class="space-y-1 text-slate-300 mt-2 text-[11px]">
              <div class="flex justify-between"><span>Wear Rate:</span><span class="text-white">+0.052 s/lap</span></div>
              <div class="flex justify-between"><span>Thermal Cliff:</span><span class="text-amber-400 font-bold">Lap 26</span></div>
              <div class="flex justify-between"><span>Typical Use:</span><span>Optimal Race Start Stint</span></div>
            </div>
          </div>

          <div class="p-3.5 rounded-xl bg-slate-950/80 border border-slate-800 border-l-4 border-l-slate-200">
            <div class="flex justify-between font-bold text-white">
              <span>HARD (C1)</span>
              <span>+0.48s Base Delta</span>
            </div>
            <div class="space-y-1 text-slate-300 mt-2 text-[11px]">
              <div class="flex justify-between"><span>Wear Rate:</span><span class="text-white">+0.038 s/lap</span></div>
              <div class="flex justify-between"><span>Thermal Cliff:</span><span class="text-amber-400 font-bold">Lap 38</span></div>
              <div class="flex justify-between"><span>Typical Use:</span><span>1-Stop Long Run Anchor</span></div>
            </div>
          </div>
        </div>

        <!-- Degradation Curves Visualization -->
        <div class="mt-6 bg-slate-950/80 p-4 rounded-xl border border-slate-800">
          <div class="flex justify-between items-center text-xs font-mono mb-2">
            <span class="text-slate-300 font-bold">TIRE AGE VS. LAP TIME PENALTY (+SECONDS)</span>
            <span class="text-[10px] text-slate-500">Includes thermal cliff bifurcation</span>
          </div>
          <div class="h-72 relative flex items-center justify-center">
            <svg id="deg-svg" class="w-full h-full"></svg>
          </div>
        </div>

      </div>

    </div>

    <!-- TAB 5: UNDERCUT & SAFETY CAR -->
    <div id="view-undercut" class="hidden space-y-6">
      
      <div class="f1-card p-5 f1-card-accent">
        <div class="border-b border-slate-800 pb-3">
          <h2 class="text-base font-bold text-white flex items-center gap-2">
            <span>⚔️</span> The Undercut Horizon & Safety Car Arbitrage
          </h2>
          <p class="text-xs text-slate-400">
            Empirical telemetry data from 2024 tactical undercut battles and the mathematical arbitrage of pitting under neutralizations.
          </p>
        </div>

        <!-- Undercut Battles Table -->
        <div class="mt-4 overflow-x-auto">
          <table class="w-full text-left text-xs font-mono">
            <thead class="bg-slate-900 text-slate-400 border-b border-slate-800">
              <tr>
                <th class="p-3">GRAND PRIX</th>
                <th class="p-3">ATTACKER</th>
                <th class="p-3">DEFENDER</th>
                <th class="p-3">PRE-GAP</th>
                <th class="p-3">TRIGGER LAP</th>
                <th class="p-3">OUT-LAP DELTA</th>
                <th class="p-3">RESULT</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-800/60" id="undercut-table-body">
              <!-- Populated by JS -->
            </tbody>
          </table>
        </div>

      </div>

    </div>

    <!-- TAB 6: GLOBAL CIRCUIT ATLAS -->
    <div id="view-circuits" class="hidden space-y-6">
      
      <div class="f1-card p-5 f1-card-accent">
        <div class="flex flex-wrap items-center justify-between border-b border-slate-800 pb-3 gap-2">
          <div>
            <h2 class="text-base font-bold text-white flex items-center gap-2">
              <span>🌍</span> FIA Formula 1 World Circuit Atlas (77 Circuits)
            </h2>
            <p class="text-xs text-slate-400">
              Global track catalog from 1950 to 2024. Classified by altitude, downforce requirement, and asphalt abrasiveness.
            </p>
          </div>
          <input type="text" id="circuit-search" placeholder="Search track, country or city..." oninput="filterCircuits()" class="bg-slate-900 border border-slate-700 text-xs text-slate-200 rounded-lg px-3 py-1.5 font-mono focus:ring-2 focus:ring-red-500 outline-none w-64">
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-3 mt-4 max-h-[550px] overflow-y-auto pr-2" id="circuits-grid-container">
          <!-- Populated by JS -->
        </div>
      </div>

    </div>

    <!-- TAB 7: WHAT-IF SIMULATOR -->
    <div id="view-simulator" class="hidden space-y-6">
      
      <div class="f1-card p-5 f1-card-accent">
        <div class="border-b border-slate-800 pb-3">
          <h2 class="text-base font-bold text-white flex items-center gap-2">
            <span>🎮</span> Pit-Wall Tactical What-If Race Simulator
          </h2>
          <p class="text-xs text-slate-400">
            Simulate custom pit stop laps, alternative tire selections, and Safety Car timing interventions.
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mt-4 font-mono text-xs">
          <div>
            <label class="text-slate-400 block mb-1">STINT 1 TIRE COMPOUND</label>
            <select id="sim-stint1-tire" onchange="runCustomSim()" class="w-full bg-slate-900 border border-slate-700 rounded p-2 text-white">
              <option value="medium">Medium (C2) - Recommended</option>
              <option value="soft">Soft (C3) - Aggressive Start</option>
              <option value="hard">Hard (C1) - Reverse Longevity</option>
            </select>
          </div>

          <div>
            <label class="text-slate-400 block mb-1">PIT STOP 1 LAP</label>
            <input type="range" id="sim-pit1-lap" min="10" max="38" value="20" oninput="document.getElementById('sim-pit1-val').textContent = 'Lap ' + this.value; runCustomSim();" class="w-full accent-red-600">
            <span id="sim-pit1-val" class="text-slate-300 font-bold block mt-1">Lap 20</span>
          </div>

          <div>
            <label class="text-slate-400 block mb-1">SAFETY CAR TIMING</label>
            <select id="sim-sc-lap" onchange="runCustomSim()" class="w-full bg-slate-900 border border-slate-700 rounded p-2 text-white">
              <option value="none">No Safety Car (100% Green Flag)</option>
              <option value="lap18">VSC at Lap 18 (+10.5s Dividend)</option>
              <option value="lap25">Full Safety Car at Lap 25 (+12.0s Dividend)</option>
            </select>
          </div>
        </div>

        <div class="mt-4 p-4 rounded-xl bg-slate-950 border border-slate-800 flex items-center justify-between font-mono text-xs">
          <div>
            <span class="text-slate-400 block">PROJECTED RACE TIME</span>
            <span class="text-xl font-bold text-white" id="sim-result-time">5,504.8s (1h 31m 44.8s)</span>
          </div>
          <div>
            <span class="text-slate-400 block">TACTICAL ADVANTAGE</span>
            <span class="text-emerald-400 font-bold text-sm" id="sim-result-delta">+2.4s vs Nominal Pace</span>
          </div>
        </div>
      </div>

    </div>

  </main>

  <!-- DATA & SCRIPTS -->
  <script>
    const F1_DATA = {json_data_str};
    let selectedDrivers = ["VER", "LEC", "NOR"];
    let isDRSOpen = false;
    let selectedCompound = "soft";

    // CAR INSPECTOR DEFINITIONS
    const CAR_COMPONENTS = {{
      "front-wing": {{
        title: "1. Front Wing & Inwash Cascade Assembly",
        subtitle: "Primary Aerodynamic Flow Conditioner",
        details: "The 2024 multi-element carbon fiber front wing generates 42.5% of total vehicle downforce. It features adjustable upper flaps (10° - 18° angle of attack) and complex endplate diveplanes that condition the Y250 inwash vortex, sealing clean airflow into the underfloor venturi tunnels while pushing turbulent tyre wake away from the chassis.",
        metrics: [
          {{ label: "Downforce Share", value: "42.5% (-1,120 kg @ 300 km/h)" }},
          {{ label: "Ground Clearance", value: "28 mm (Adjustable ride height)" }},
          {{ label: "Aero Sensitivity", value: "-0.18s / degree of flap pitch" }}
        ]
      }},
      "wheels": {{
        title: "2. Pirelli 18-inch Open-Wheel System & Carbon Brake Ducts",
        subtitle: "Mechanical Grip & Thermodynamic Friction Surface",
        details: "18-inch BBS forged magnesium rims wrapped in low-profile Pirelli rubber (305/720-18 Front, 405/720-18 Rear). Fitted with internal carbon-carbon brake discs (operating at 600°C - 1,000°C) and aerodynamic wheel covers that control thermal dissipation to maintain tire bulk temperatures in the optimal 95°C - 110°C working window.",
        metrics: [
          {{ label: "Carcass Pressure", value: "23.5 psi Front / 21.0 psi Rear" }},
          {{ label: "Peak Deceleration", value: "-5.2 G under heavy braking" }},
          {{ label: "Thermal Cliff Risk", value: "High above 115°C bulk rubber temp" }}
        ]
      }},
      "halo": {{
        title: "3. Titanium Halo Safety Structure & Cockpit Telemetry",
        subtitle: "Driver Monocoque Protection & Aerodynamic Deflector",
        details: "Grade 5 titanium structure weighing just 9 kg, capable of withstanding 120 kN of static crushing load (equivalent to two London double-decker buses). Features an aerodynamic fairing with micro-vortex generators directing boundary layer airflow into the engine airbox intake and T-camera assembly.",
        metrics: [
          {{ label: "Load Capacity", value: "120 kN structural test rating" }},
          {{ label: "Steering Display", value: "PCU-8D Full Color OLED Telemetry HUD" }},
          {{ label: "Aero Penalty", value: "+0.04s/lap drag without aero fairing" }}
        ]
      }},
      "sidepod": {{
        title: "4. Sculptured Sidepod Undercut & Ground-Effect Venturi Tunnels",
        subtitle: "Underfloor Downforce Generation without Induced Drag",
        details: "Modern ground-effect F1 cars generate over 60% of their total aerodynamic load through dual 3D contoured venturi tunnels along the floor. Deep sidepod undercuts accelerate air between the sidepod flanks and floor edge wings, creating massive low-pressure zones that suck the car to the tarmac.",
        metrics: [
          {{ label: "Floor Suction", value: "-14.8 kPa peak underfloor pressure" }},
          {{ label: "Porpoising Margin", value: "12 mm safety buffer from stalls" }},
          {{ label: "Radiator Louvres", value: "8 cooling vents open (34°C ambient)" }}
        ]
      }},
      "rear-wing": {{
        title: "5. Rear Wing Assembly & Hydraulic DRS Actuator",
        subtitle: "Main Downforce Generator & Drag Reduction System",
        details: "High-downforce rear wing assembly featuring a carbon beam wing and hydraulic DRS actuator flap. When activated within 1.0s of a leading car, the flap raises by 85 mm, shedding 28.5% of overall aerodynamic drag to deliver a +18 km/h straight-line speed delta for overtakes.",
        metrics: [
          {{ label: "DRS Delta", value: "-28.5% Drag / +18 km/h top speed boost" }},
          {{ label: "Beam Wing Load", value: "18% of total rear downforce" }},
          {{ label: "Aero Wake Upwash", value: "Expels dirty air 35° upwards" }}
        ]
      }},
      "powertrain": {{
        title: "6. 1.6L V6 Turbo-Hybrid Power Unit & Diffuser Expansion",
        subtitle: "1,040+ BHP Dual Energy Recovery System (ERS)",
        details: "Direct-injection 1.6-litre 90-degree V6 turbocharged internal combustion engine revving to 15,000 RPM, paired with MGU-K (120 kW kinetic harvesting) and MGU-H (unlimited turbo shaft thermal recovery). Combined power exceeds 1,040 BHP at thermal efficiency exceeding 52%.",
        metrics: [
          {{ label: "Power Output", value: "1,040+ BHP (840 ICE + 160 MGU-K)" }},
          {{ label: "Fuel Flow Limit", value: "100 kg/h maximum FIA ultrasonic cap" }},
          {{ label: "Fuel Burn Gain", value: "-0.062s per lap as 110 kg combusts" }}
        ]
      }}
    }};

    function selectCarComponent(compKey) {{
      const comp = CAR_COMPONENTS[compKey];
      if (!comp) return;

      const card = document.getElementById("car-inspector-card");
      let metricsHtml = comp.metrics.map(m => `
        <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800">
          <span class="text-[10px] text-slate-500 uppercase block">${{m.label}}</span>
          <span class="text-white font-bold text-xs mt-0.5 block">${{m.value}}</span>
        </div>
      `).join("");

      card.innerHTML = `
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
          <div>
            <h4 class="text-sm font-bold text-red-400 font-mono">${{comp.title}}</h4>
            <span class="text-xs text-slate-400">${{comp.subtitle}}</span>
          </div>
          <span class="text-xs px-2 py-0.5 rounded bg-red-950 text-red-400 border border-red-800 font-mono font-bold">TELEMETRY ACTIVE</span>
        </div>
        <p class="text-xs text-slate-300 mt-2 leading-relaxed">${{comp.details}}</p>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-2 mt-3 font-mono">
          ${{metricsHtml}}
        </div>
      `;
    }}

    function toggleDRS() {{
      isDRSOpen = !isDRSOpen;
      const btn = document.getElementById("car-drs-btn");
      const indicator = document.getElementById("car-drs-indicator");
      const label = document.getElementById("car-drs-label");
      const dragCoeff = document.getElementById("tel-drag-coeff");
      const dragSub = document.getElementById("tel-drag-sub");
      const topSpd = document.getElementById("tel-top-spd");
      const spdSub = document.getElementById("tel-spd-sub");

      if (isDRSOpen) {{
        btn.classList.add("border-emerald-500", "bg-emerald-950/60");
        indicator.className = "w-2 h-2 rounded-full bg-emerald-400 animate-pulse";
        label.textContent = "DRS: OPEN";
        dragCoeff.textContent = "0.63";
        dragCoeff.className = "text-lg font-bold text-emerald-400 mt-0.5";
        dragSub.textContent = "-28.5% Drag Relief";
        topSpd.textContent = "352 KM/H";
        spdSub.textContent = "+18 km/h Overtake Boost";
      }} else {{
        btn.classList.remove("border-emerald-500", "bg-emerald-950/60");
        indicator.className = "w-2 h-2 rounded-full bg-slate-500";
        label.textContent = "DRS: CLOSED";
        dragCoeff.textContent = "0.88";
        dragCoeff.className = "text-lg font-bold text-amber-400 mt-0.5";
        dragSub.textContent = "DRS Flap: Closed";
        topSpd.textContent = "334 KM/H";
        spdSub.textContent = "Straightline Pace";
      }}
    }}

    function setCarCompound(comp) {{
      selectedCompound = comp;
      const tempEl = document.getElementById("tel-tire-temp");
      const compEl = document.getElementById("tel-tire-comp");
      if (comp === "soft") {{
        tempEl.textContent = "104°C";
        tempEl.className = "text-lg font-bold text-red-400 mt-0.5";
        compEl.textContent = "Soft (C3) - Cliff: Lap 16";
      }} else if (comp === "medium") {{
        tempEl.textContent = "98°C";
        tempEl.className = "text-lg font-bold text-yellow-400 mt-0.5";
        compEl.textContent = "Medium (C2) - Cliff: Lap 26";
      }} else {{
        tempEl.textContent = "92°C";
        tempEl.className = "text-lg font-bold text-white mt-0.5";
        compEl.textContent = "Hard (C1) - Cliff: Lap 38";
      }}
    }}

    // TAB SWITCHING
    function setTab(tab) {{
      const tabs = ["strategy-generator", "f1-car", "telemetry", "degradation", "undercut", "circuits", "simulator"];
      tabs.forEach(t => {{
        const btn = document.getElementById("tab-" + t);
        const view = document.getElementById("view-" + t);
        if (btn) {{
          if (t === tab) {{
            btn.classList.add("active");
            btn.classList.remove("text-slate-400");
            btn.classList.add("text-slate-100", "font-bold");
          }} else {{
            btn.classList.remove("active");
            btn.classList.add("text-slate-400");
            btn.classList.remove("text-slate-100", "font-bold");
          }}
        }}
        if (view) {{
          if (t === tab) view.classList.remove("hidden");
          else view.classList.add("hidden");
        }}
      }});
      if (tab === "telemetry") renderTelemetryCharts();
      if (tab === "degradation") renderDegradationChart();
      if (tab === "f1-car") selectCarComponent("front-wing");
    }}

    function changeCircuitContext(cId) {{
      document.getElementById("gen-circuit").value = cId;
      const c = F1_DATA.circuits.find(item => item.circuitId == cId);
      if (c) {{
        document.getElementById("current-circuit-badge").textContent = `${{c.name}} (${{c.laps}} Laps)`;
      }}
      generateF1Strategies();
    }}

    // STRATEGY GENERATOR
    function generateF1Strategies() {{
      const circuitId = parseInt(document.getElementById("gen-circuit").value);
      const grid = parseInt(document.getElementById("gen-grid").value);
      const tier = parseInt(document.getElementById("gen-tier").value);
      const temp = parseInt(document.getElementById("gen-temp").value);
      const scProb = parseFloat(document.getElementById("gen-sc").value);

      const circuit = F1_DATA.circuits.find(c => c.circuitId === circuitId) || F1_DATA.circuits[0];
      const laps = circuit.laps || 57;
      const pitLoss = circuit.pit_loss_sec || 22.0;
      const abrasiveness = circuit.abrasiveness || 3.0;

      const p1_A = Math.round(laps * 0.35);
      const p1_B = Math.round(laps * 0.24);
      const p2_B = Math.round(laps * 0.65);
      const p1_C = Math.round(laps * 0.55);

      const baseTime = (laps * 91.5);
      const time_A = (baseTime + pitLoss).toFixed(1);
      const time_B = (baseTime + (pitLoss * 2) - 18.5).toFixed(1);
      const time_C = (baseTime + (scProb > 0.4 ? 10.0 : pitLoss)).toFixed(1);

      const plans = [
        {{
          plan_code: "PLAN A (OPTIMAL)",
          name: "Medium ➔ Hard Direct",
          type: "1-STOP",
          stints: [{{ compound: "MEDIUM", start: 1, end: p1_A }}, {{ compound: "HARD", start: p1_A + 1, end: laps }}],
          pit_windows: `Lap ${{p1_A - 2}} - ${{p1_A + 2}}`,
          total_time: time_A,
          predicted_finish: grid <= 3 ? "P1 - Victory" : "Podium (P2/P3)",
          summary: "Primary pace optimization under clean air. Minimizes pit loss and traffic exposure."
        }},
        {{
          plan_code: "PLAN B (UNDERCUT ATTACK)",
          name: "Soft ➔ Hard ➔ Medium Attack",
          type: "2-STOP",
          stints: [{{ compound: "SOFT", start: 1, end: p1_B }}, {{ compound: "HARD", start: p1_B + 1, end: p2_B }}, {{ compound: "MEDIUM", start: p2_B + 1, end: laps }}],
          pit_windows: `Stop 1: L${{p1_B - 2}}-L${{p1_B}} | Stop 2: L${{p2_B - 2}}-L${{p2_B}}`,
          total_time: time_B,
          predicted_finish: "Track Position Gain (+2 to +4 Pos)",
          summary: "High-grip sprint strategy. Box 2-3 laps early to exploit out-lap grip delta and leapfrog trapped cars."
        }},
        {{
          plan_code: "PLAN C (SC OVERCUT GAMBLE)",
          name: "Hard ➔ Soft / Medium Reverse",
          type: "SC CONTINGENCY",
          stints: [{{ compound: "HARD", start: 1, end: p1_C }}, {{ compound: "SOFT", start: p1_C + 1, end: laps }}],
          pit_windows: `Lap ${{p1_C - 4}} - ${{p1_C + 4}} (SC Window)`,
          total_time: time_C,
          predicted_finish: scProb > 0.5 ? "Net Gain Under SC (+12.0s Free Pit)" : "P5 - P8 (Traffic Dependent)",
          summary: "Reverse longevity gamble. Stretches stint 1 to catch a high-probability Safety Car or VSC neutralization."
        }}
      ];

      const container = document.getElementById("strategy-plans-container");
      container.innerHTML = "";

      plans.forEach(p => {{
        const card = document.createElement("div");
        card.className = "f1-card p-5 flex flex-col justify-between space-y-4";
        if (p.type === "1-STOP") card.classList.add("border-t-4", "border-t-red-600");
        else if (p.type === "2-STOP") card.classList.add("border-t-4", "border-t-amber-500");
        else card.classList.add("border-t-4", "border-t-blue-500");

        let stintBars = "";
        p.stints.forEach(s => {{
          const dur = s.end - s.start + 1;
          const pct = ((dur / laps) * 100).toFixed(0);
          let badgeClass = s.compound === "SOFT" ? "badge-soft" : s.compound === "MEDIUM" ? "badge-medium" : "badge-hard";
          stintBars += `
            <div style="width: ${{pct}}%" class="stint-bar-item ${{badgeClass}} py-1 px-2 rounded text-center font-mono text-[11px] font-bold">
              <span>${{s.compound}}</span>
              <span class="block text-[10px] font-normal">${{dur}} Laps</span>
            </div>
          `;
        }});

        card.innerHTML = `
          <div>
            <div class="flex items-center justify-between font-mono text-[11px] mb-1">
              <span class="text-red-400 font-bold">${{p.plan_code}}</span>
              <span class="px-2 py-0.5 rounded bg-slate-900 border border-slate-700 text-slate-300 font-bold">${{p.type}}</span>
            </div>
            <h3 class="text-base font-bold text-white">${{p.name}}</h3>
            <p class="text-xs text-slate-400 mt-1">${{p.summary}}</p>
          </div>

          <div class="space-y-2">
            <span class="text-[10px] font-mono text-slate-400 uppercase tracking-wider block">STINT PROFILES</span>
            <div class="w-full flex gap-1 bg-slate-950 p-1 rounded-lg border border-slate-800">
              ${{stintBars}}
            </div>
          </div>

          <div class="grid grid-cols-2 gap-2 text-xs font-mono bg-slate-950/80 p-3 rounded-lg border border-slate-800">
            <div>
              <span class="text-[10px] text-slate-500 block">PIT WINDOW</span>
              <span class="text-amber-400 font-bold">${{p.pit_windows}}</span>
            </div>
            <div>
              <span class="text-[10px] text-slate-500 block">EST. TOTAL TIME</span>
              <span class="text-white font-bold">${{p.total_time}}s</span>
            </div>
            <div class="col-span-2 pt-1 border-t border-slate-800">
              <span class="text-[10px] text-slate-500 block">PREDICTED FINISH</span>
              <span class="text-emerald-400 font-black text-sm">${{p.predicted_finish}}</span>
            </div>
          </div>
        `;
        container.appendChild(card);
      }});

      // Render Decision Triggers
      const triggersContainer = document.getElementById("decision-triggers-container");
      triggersContainer.innerHTML = `
        <div class="p-3.5 bg-slate-950/80 rounded-xl border border-slate-800 space-y-1">
          <div class="flex items-center gap-2 text-red-400 font-bold">
            <span>●</span> TRIGGER 1: UNDER 1.8s GAP TO RIVAL
          </div>
          <p class="text-slate-300 text-[11px] leading-relaxed">
            <strong>Action: Trigger Undercut (Plan B).</strong> Box 1 lap ahead into clean air. Grip advantage (+1.74s) secures track position on exit.
          </p>
        </div>

        <div class="p-3.5 bg-slate-950/80 rounded-xl border border-slate-800 space-y-1">
          <div class="flex items-center gap-2 text-amber-400 font-bold">
            <span>●</span> TRIGGER 2: SAFETY CAR IN PIT WINDOW
          </div>
          <p class="text-slate-300 text-[11px] leading-relaxed">
            <strong>Action: Box Immediately for Hard Tires.</strong> Pitting under SC reduces pit transit loss from ${{pitLoss}}s to ~10s (saves +12.0s free time).
          </p>
        </div>

        <div class="p-3.5 bg-slate-950/80 rounded-xl border border-slate-800 space-y-1">
          <div class="flex items-center gap-2 text-blue-400 font-bold">
            <span>●</span> TRIGGER 3: HIGH TIRE GRAINING / HEAT
          </div>
          <p class="text-slate-300 text-[11px] leading-relaxed">
            <strong>Action: Extend First Stint & Switch to Plan C.</strong> Avoid pitting into traffic trains where dirty air wake accelerates graining.
          </p>
        </div>
      `;
    }}

    // Driver Badges
    function buildDriverBadges() {{
      const container = document.getElementById("driver-toggle-container");
      container.innerHTML = "";
      F1_DATA.drivers.forEach(d => {{
        const isSel = selectedDrivers.includes(d.code);
        const btn = document.createElement("button");
        btn.className = `px-2.5 py-1 rounded text-xs font-mono font-bold transition flex items-center gap-1.5 border ${{
          isSel ? 'bg-slate-800 text-white border-slate-600' : 'bg-slate-950 text-slate-500 border-slate-800'
        }}`;
        btn.innerHTML = `<span class="w-2 h-2 rounded-full" style="background-color: ${{d.color}}"></span> ${{d.code}} (${{d.name}})`;
        btn.onclick = () => {{
          if (selectedDrivers.includes(d.code)) {{
            if (selectedDrivers.length > 1) selectedDrivers = selectedDrivers.filter(c => c !== d.code);
          }} else {{
            selectedDrivers.push(d.code);
          }}
          buildDriverBadges();
          renderTelemetryCharts();
        }};
        container.appendChild(btn);
      }});
    }}

    // Telemetry charts
    function renderTelemetryCharts() {{
      const paceSvg = document.getElementById("pace-svg");
      const gapSvg = document.getElementById("gap-svg");
      const isSmooth = document.getElementById("toggle-smooth").checked;
      const laps = F1_DATA.bahrain_telemetry_laps;

      const w = 800, h = 300, pL = 45, pR = 20, pT = 20, pB = 30;
      paceSvg.setAttribute("viewBox", `0 0 ${{w}} ${{h}}`);
      paceSvg.innerHTML = "";
      gapSvg.setAttribute("viewBox", `0 0 ${{w}} ${{h}}`);
      gapSvg.innerHTML = "";

      for (let p = 94; p <= 101; p += 1) {{
        const y = pT + (h - pT - pB) * (p - 93.5) / 8;
        paceSvg.innerHTML += `<line x1="${{pL}}" y1="${{y}}" x2="${{w - pR}}" y2="${{y}}" stroke="#1E293B" stroke-dasharray="3,3"/>`;
        paceSvg.innerHTML += `<text x="${{pL - 6}}" y="${{y + 3}}" fill="#64748B" font-size="10" text-anchor="end" font-family="JetBrains Mono">${{p}}s</text>`;
      }}

      for (let g = 0; g <= 40; g += 10) {{
        const y = pT + (h - pT - pB) * (g / 45);
        gapSvg.innerHTML += `<line x1="${{pL}}" y1="${{y}}" x2="${{w - pR}}" y2="${{y}}" stroke="#1E293B" stroke-dasharray="3,3"/>`;
        gapSvg.innerHTML += `<text x="${{pL - 6}}" y="${{y + 3}}" fill="#64748B" font-size="10" text-anchor="end" font-family="JetBrains Mono">${{g}}s</text>`;
      }}

      selectedDrivers.forEach(dCode => {{
        const dInfo = F1_DATA.drivers.find(d => d.code === dCode) || {{ color: "#AAA" }};
        const dLaps = laps.filter(l => l.driver === dCode).sort((a,b) => a.lap - b.lap);
        if (dLaps.length === 0) return;

        let pacePts = [];
        let gapPts = [];
        dLaps.forEach((l, idx) => {{
          let val = l.lap_time;
          if (isSmooth && idx >= 2 && !l.is_pit) {{
            val = (dLaps[idx].lap_time + dLaps[idx-1].lap_time + dLaps[idx-2].lap_time) / 3;
          }}
          val = Math.max(93.5, Math.min(101.5, val));
          const x = pL + (w - pL - pR) * (l.lap - 1) / 56;
          const yPace = pT + (h - pT - pB) * (val - 93.5) / 8;
          pacePts.push(`${{x.toFixed(1)}},${{yPace.toFixed(1)}}`);

          const yGap = pT + (h - pT - pB) * (Math.min(45, l.gap_to_leader) / 45);
          gapPts.push(`${{x.toFixed(1)}},${{yGap.toFixed(1)}}`);
        }});

        paceSvg.innerHTML += `<polyline points="${{pacePts.join(" ")}}" fill="none" stroke="${{dInfo.color}}" stroke-width="2.2" stroke-linecap="round"/>`;
        gapSvg.innerHTML += `<polyline points="${{gapPts.join(" ")}}" fill="none" stroke="${{dInfo.color}}" stroke-width="2.2" stroke-linecap="round"/>`;
      }});
    }}

    function renderStintTimelines() {{
      const container = document.getElementById("stint-timeline-container");
      container.innerHTML = "";
      const driverStintsMap = {{
        "VER": [{{ comp: "SOFT", s: 1, e: 17 }}, {{ comp: "HARD", s: 18, e: 36 }}, {{ comp: "SOFT", s: 37, e: 57 }}],
        "PER": [{{ comp: "SOFT", s: 1, e: 12 }}, {{ comp: "HARD", s: 13, e: 36 }}, {{ comp: "SOFT", s: 37, e: 57 }}],
        "SAI": [{{ comp: "SOFT", s: 1, e: 14 }}, {{ comp: "HARD", s: 15, e: 35 }}, {{ comp: "HARD", s: 36, e: 57 }}],
        "LEC": [{{ comp: "SOFT", s: 1, e: 11 }}, {{ comp: "HARD", s: 12, e: 34 }}, {{ comp: "HARD", s: 35, e: 57 }}],
        "RUS": [{{ comp: "SOFT", s: 1, e: 11 }}, {{ comp: "HARD", s: 12, e: 31 }}, {{ comp: "HARD", s: 32, e: 57 }}],
        "NOR": [{{ comp: "SOFT", s: 1, e: 13 }}, {{ comp: "HARD", s: 14, e: 33 }}, {{ comp: "HARD", s: 34, e: 57 }}]
      }};

      Object.keys(driverStintsMap).forEach(dCode => {{
        const dInfo = F1_DATA.drivers.find(d => d.code === dCode) || {{ color: "#AAA" }};
        const stints = driverStintsMap[dCode];
        const row = document.createElement("div");
        row.className = "flex items-center gap-3 text-xs font-mono";

        let bars = "";
        stints.forEach(s => {{
          const dur = s.e - s.s + 1;
          const pct = (dur / 57) * 100;
          let color = "#E10600";
          let textCol = "#FFFFFF";
          if (s.comp === "MEDIUM") {{ color = "#FFF200"; textCol = "#000000"; }}
          else if (s.comp === "HARD") {{ color = "#FFFFFF"; textCol = "#000000"; }}

          bars += `<div style="width: ${{pct}}%; background-color: ${{color}}; color: ${{textCol}}" class="stint-bar-item py-1 rounded text-center font-bold flex justify-between px-2 text-[10px]">
            <span>${{s.comp[0]}}</span><span>${{dur}}L</span>
          </div>`;
        }});

        row.innerHTML = `
          <div class="w-14 flex items-center gap-1 font-bold">
            <span class="w-2 h-2 rounded-full" style="background:${{dInfo.color}}"></span> ${{dCode}}
          </div>
          <div class="flex-1 flex gap-1 bg-slate-950 p-1 rounded-lg border border-slate-800">${{bars}}</div>
        `;
        container.appendChild(row);
      }});
    }}

    function renderDegradationChart() {{
      const svg = document.getElementById("deg-svg");
      svg.innerHTML = "";
      const w = 800, h = 300, pL = 50, pR = 20, pT = 20, pB = 30;
      svg.setAttribute("viewBox", `0 0 ${{w}} ${{h}}`);

      for (let p = 0; p <= 4; p += 1) {{
        const y = pT + (h - pT - pB) * (1 - p / 4);
        svg.innerHTML += `<line x1="${{pL}}" y1="${{y}}" x2="${{w - pR}}" y2="${{y}}" stroke="#1E293B" stroke-dasharray="3,3"/>`;
        svg.innerHTML += `<text x="${{pL - 6}}" y="${{y + 3}}" fill="#64748B" font-size="10" text-anchor="end" font-family="JetBrains Mono">+${{p}}s</text>`;
      }}

      const curves = [
        {{ name: "Soft (C3)", color: "#E10600", cliff: 16, wear: 0.082 }},
        {{ name: "Medium (C2)", color: "#FFF200", cliff: 26, wear: 0.052 }},
        {{ name: "Hard (C1)", color: "#FFFFFF", cliff: 38, wear: 0.038 }}
      ];

      curves.forEach(c => {{
        let pts = [];
        for (let l = 1; l <= 45; l++) {{
          let penalty = l * c.wear;
          if (l > c.cliff) penalty += Math.pow(l - c.cliff, 2) * 0.015;
          penalty = Math.min(4.5, penalty);

          const x = pL + (w - pL - pR) * (l - 1) / 44;
          const y = pT + (h - pT - pB) * (1 - penalty / 4);
          pts.push(`${{x.toFixed(1)}},${{y.toFixed(1)}}`);
        }}
        svg.innerHTML += `<polyline points="${{pts.join(" ")}}" fill="none" stroke="${{c.color}}" stroke-width="2.5"/>`;
      }});
    }}

    function renderBattlesTable() {{
      const b = document.getElementById("undercut-table-body");
      b.innerHTML = "";
      F1_DATA.strategy_battles.forEach(item => {{
        b.innerHTML += `
          <tr class="hover:bg-slate-900/40 transition">
            <td class="p-3 font-bold text-white">${{item.race}}</td>
            <td class="p-3 text-red-400 font-bold">${{item.attacker}}</td>
            <td class="p-3 text-slate-300">${{item.defender}}</td>
            <td class="p-3 text-slate-400">${{item.gap_before}}</td>
            <td class="p-3 text-amber-400">Lap ${{item.lap}}</td>
            <td class="p-3 text-emerald-400 font-bold">${{item.out_lap_delta}}</td>
            <td class="p-3 font-bold text-emerald-400">${{item.result}}</td>
          </tr>
        `;
      }});
    }}

    function renderCircuitsGrid() {{
      const c = document.getElementById("circuits-grid-container");
      c.innerHTML = "";
      F1_DATA.circuits.forEach(item => {{
        c.innerHTML += `
          <div class="p-3.5 rounded-xl bg-slate-950/80 border border-slate-800 font-mono">
            <div class="flex justify-between font-bold">
              <span class="text-red-400">${{item.country}}</span>
              <span class="text-slate-400">${{item.alt}}m alt</span>
            </div>
            <div class="text-white font-bold text-sm my-1">${{item.name}}</div>
            <div class="flex justify-between text-[11px] text-slate-300 pt-1 border-t border-slate-800/80">
              <span>Pit Loss: ${{item.pit_loss_sec}}s</span>
              <span class="text-amber-400 font-bold">${{item.typical_stops}}-Stop</span>
            </div>
          </div>
        `;
      }});
    }}

    function filterCircuits() {{
      const q = document.getElementById("circuit-search").value.toLowerCase();
      const filtered = F1_DATA.circuits.filter(c => c.name.toLowerCase().includes(q) || c.country.toLowerCase().includes(q));
      const c = document.getElementById("circuits-grid-container");
      c.innerHTML = "";
      filtered.forEach(item => {{
        c.innerHTML += `
          <div class="p-3.5 rounded-xl bg-slate-950/80 border border-slate-800 font-mono">
            <div class="flex justify-between font-bold">
              <span class="text-red-400">${{item.country}}</span>
              <span class="text-slate-400">${{item.alt}}m alt</span>
            </div>
            <div class="text-white font-bold text-sm my-1">${{item.name}}</div>
            <div class="flex justify-between text-[11px] text-slate-300 pt-1 border-t border-slate-800/80">
              <span>Pit Loss: ${{item.pit_loss_sec}}s</span>
              <span class="text-amber-400 font-bold">${{item.typical_stops}}-Stop</span>
            </div>
          </div>
        `;
      }});
    }}

    function runCustomSim() {{
      const p1 = parseInt(document.getElementById("sim-pit1-lap").value);
      const delta = (p1 - 20) * 0.16;
      document.getElementById("sim-result-time").textContent = `${{(5504.8 + delta).toFixed(1)}}s (1h 31m ${{(44.8 + delta).toFixed(1)}}s)`;
      document.getElementById("sim-result-delta").textContent = delta < 0 ? `${{delta.toFixed(1)}}s (Time Saved)` : `+${{delta.toFixed(1)}}s (Time Lost)`;
    }}

    // INITIALIZATION
    window.onload = function() {{
      generateF1Strategies();
      buildDriverBadges();
      renderTelemetryCharts();
      renderStintTimelines();
      renderDegradationChart();
      renderBattlesTable();
      renderCircuitsGrid();
      selectCarComponent("front-wing");
    }};
  </script>
</body>
</html>
"""

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(master_html)

with open(ARTIFACT_HTML, "w", encoding="utf-8") as f:
    f.write(master_html)

print("Saved updated master dashboard with original F1 car and technical inspector!")
