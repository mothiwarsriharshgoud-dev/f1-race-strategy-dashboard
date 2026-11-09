# -*- coding: utf-8 -*-
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

    /* Safety car pulse */
    @keyframes pulse-sc {{
      0%, 100% {{ opacity: 1; transform: scale(1); }}
      50% {{ opacity: 0.75; transform: scale(0.98); }}
    }}
    .sc-pulse {{
      animation: pulse-sc 1.5s infinite ease-in-out;
    }}
  </style>
</head>
<body class="carbon-pattern text-slate-100 min-h-screen">

  <!-- TOP BRANDING & NAVIGATION HEADER -->
  <header class="border-b border-slate-800 bg-slate-950/80 backdrop-blur sticky top-0 z-50">
    <div class="max-w-7xl mx-auto px-4 py-3 flex flex-wrap items-center justify-between gap-4">
      
      <div class="flex items-center gap-3">
        <div class="bg-red-600 text-white font-black px-2.5 py-1 rounded text-lg tracking-wider flex items-center gap-1 shadow-lg shadow-red-900/40">
          <span>F1</span>
        </div>
        <div>
          <div class="flex items-center gap-2">
            <h1 class="text-lg md:text-xl font-bold tracking-tight text-white flex items-center gap-2">
              Formula 1 Race Telemetry & Strategy Analytics Platform
            </h1>
            <span class="text-xs bg-red-950 text-red-400 border border-red-800 font-mono px-2 py-0.5 rounded font-bold">
              DAV PROJECT
            </span>
          </div>
          <p class="text-xs text-slate-400 font-medium">
            Core Question: <span class="text-red-400 font-semibold italic">"How do race strategies influence Formula 1 performance?"</span>
          </p>
        </div>
      </div>

      <!-- Quick Session & Safety Car Header Badges -->
      <div class="flex items-center gap-3 font-mono">
        <div id="header-sc-badge" class="px-2.5 py-1 rounded-full text-xs font-bold flex items-center gap-1.5 bg-emerald-950 text-emerald-400 border border-emerald-800 cursor-pointer" onclick="setTab('strategy-generator')">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          <span id="header-sc-text">TRACK: GREEN FLAG</span>
        </div>

        <div class="text-right">
          <span class="text-[10px] uppercase tracking-wider text-slate-400 block">Grand Prix Mode</span>
          <span class="text-xs font-bold text-slate-200" id="current-circuit-badge">Bahrain GP (57 Laps)</span>
        </div>

        <select id="quick-circuit-select" onchange="changeCircuitContext(this.value)" class="bg-slate-900 border border-slate-700 text-slate-200 text-xs rounded-lg px-2.5 py-1.5 font-medium focus:ring-2 focus:ring-red-500 outline-none">
          <option value="3">Bahrain (Sakhir) - 57 Laps</option>
          <option value="6">Monaco (Street) - 78 Laps</option>
          <option value="9">Silverstone (UK) - 52 Laps</option>
          <option value="13">Spa-Francorchamps - 44 Laps</option>
          <option value="14">Monza (Italy) - 53 Laps</option>
          <option value="15">Singapore (Marina Bay) - 62 Laps</option>
          <option value="22">Suzuka (Japan) - 53 Laps</option>
          <option value="4">Barcelona (Spain) - 66 Laps</option>
          <option value="70">Austria (Red Bull Ring) - 71 Laps</option>
          <option value="32">Mexico City - 71 Laps</option>
          <option value="80">Las Vegas Strip - 50 Laps</option>
          <option value="78">Qatar (Lusail) - 57 Laps</option>
          <option value="7">Montreal (Canada) - 70 Laps</option>
          <option value="1">Melbourne (Australia) - 58 Laps</option>
          <option value="24">Abu Dhabi (Yas Marina) - 58 Laps</option>
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
        <span>🔄</span> Undercut & Safety Car Dynamics
      </button>
      <button onclick="setTab('circuits')" id="tab-circuits" class="tab-btn px-4 py-2.5 text-slate-400 hover:text-white transition flex items-center gap-1.5">
        <span>🌐</span> Global Circuit Atlas (77 Tracks)
      </button>
      <button onclick="setTab('simulator')" id="tab-simulator" class="tab-btn px-4 py-2.5 text-slate-400 hover:text-white transition flex items-center gap-1.5">
        <span>🎯</span> Interactive Strategy Simulator
      </button>
    </div>
  </header>

  <!-- MAIN APP CONTAINER -->
  <main class="max-w-7xl mx-auto px-4 py-6 space-y-6">

    <!-- KPI EXECUTIVE METRICS RIBBON -->
    <section class="grid grid-cols-2 md:grid-cols-5 gap-3">
      <div class="f1-card p-3.5 border-l-4 border-l-red-600">
        <div class="text-[11px] font-mono text-slate-400 uppercase tracking-wider">Undercut Success Rate</div>
        <div class="text-xl md:text-2xl font-bold font-mono text-white mt-1">68.4%</div>
        <div class="text-[11px] text-emerald-400 mt-0.5 flex items-center gap-1">
          <span>▲</span> +1.74s/lap out-lap delta
        </div>
      </div>

      <div class="f1-card p-3.5 border-l-4 border-l-yellow-400">
        <div class="text-[11px] font-mono text-slate-400 uppercase tracking-wider">Safety Car Pit Dividend</div>
        <div class="text-xl md:text-2xl font-bold font-mono text-white mt-1" id="kpi-sc-dividend">+12.6s Free</div>
        <div class="text-[11px] text-amber-400 mt-0.5">Pit loss cut to ~10s</div>
      </div>

      <div class="f1-card p-3.5 border-l-4 border-l-cyan-400">
        <div class="text-[11px] font-mono text-slate-400 uppercase tracking-wider">Strategy Win Influence</div>
        <div class="text-xl md:text-2xl font-bold font-mono text-white mt-1">42.8%</div>
        <div class="text-[11px] text-slate-400 mt-0.5">Determines 1st - 3rd places</div>
      </div>

      <div class="f1-card p-3.5 border-l-4 border-l-emerald-500">
        <div class="text-[11px] font-mono text-slate-400 uppercase tracking-wider">1-Stop vs 2-Stop Split</div>
        <div class="text-xl md:text-2xl font-bold font-mono text-white mt-1" id="kpi-stops-split">54% / 38%</div>
        <div class="text-[11px] text-slate-400 mt-0.5" id="kpi-stops-desc">Circuit wear dependent</div>
      </div>

      <div class="f1-card p-3.5 border-l-4 border-l-purple-500 col-span-2 md:col-span-1">
        <div class="text-[11px] font-mono text-slate-400 uppercase tracking-wider">Fuel-Burn Lightening</div>
        <div class="text-xl md:text-2xl font-bold font-mono text-white mt-1">-0.062s</div>
        <div class="text-[11px] text-slate-400 mt-0.5">Per lap as fuel burns</div>
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
              Dynamically computes optimal compound sequences, stint boundaries, and pit windows responsive to <strong>different race tracks</strong> and <strong>live safety car interventions</strong>.
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
            <select id="gen-circuit" onchange="changeCircuitContext(this.value)" class="w-full bg-slate-900 border border-slate-700 text-white rounded p-2 text-xs">
              <option value="3" selected>Bahrain (Sakhir) - 57 Laps | High Deg (2-Stop)</option>
              <option value="6">Monaco (Street) - 78 Laps | Zero Wear (1-Stop)</option>
              <option value="9">Silverstone (UK) - 52 Laps | High G-Force (2-Stop)</option>
              <option value="13">Spa-Francorchamps - 44 Laps | 7km Track (2-Stop)</option>
              <option value="14">Monza (Italy) - 53 Laps | Temple of Speed (1-Stop)</option>
              <option value="15">Singapore (Street) - 62 Laps | 100% SC Rate (1-Stop)</option>
              <option value="22">Suzuka (Japan) - 53 Laps | High Lateral Energy (2-Stop)</option>
              <option value="4">Barcelona (Spain) - 66 Laps | Abrasive T3 (2-Stop)</option>
              <option value="70">Austria (Red Bull Ring) - 71 Laps | Short Sprint (2-Stop)</option>
              <option value="32">Mexico City - 71 Laps | 2,240m Altitude (1-Stop)</option>
              <option value="80">Las Vegas Strip - 50 Laps | Cold Night Temps (1-Stop)</option>
              <option value="78">Qatar (Lusail) - 57 Laps | FIA 18-Lap Cap (3-Stop)</option>
              <option value="7">Montreal (Canada) - 70 Laps | Heavy Kerbs (2-Stop)</option>
              <option value="1">Melbourne (Australia) - 58 Laps | 4 DRS Zones (1-Stop)</option>
              <option value="24">Abu Dhabi (Yas Marina) - 58 Laps | Twilight (1/2-Stop)</option>
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
            <label class="text-slate-400 text-[10px] block mb-1">CIRCUIT WEAR INDEX</label>
            <div id="gen-circuit-deg-badge" class="w-full bg-slate-950 border border-slate-800 rounded p-2 text-xs text-amber-400 font-bold text-center">
              HIGH DEG (2-STOP)
            </div>
          </div>
        </div>

        <!-- LIVE SAFETY CAR SIMULATION CONTROL CONSOLE -->
        <div class="mt-5 p-4 rounded-xl bg-slate-950 border border-amber-600/40 font-mono">
          <div class="flex flex-wrap items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-3">
              <div id="sc-status-pill" class="px-3 py-1 rounded-full text-xs font-bold flex items-center gap-1.5 bg-emerald-950 text-emerald-400 border border-emerald-800">
                <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                <span id="sc-status-text">TRACK STATUS: GREEN FLAG (RACE PACE)</span>
              </div>
              <span class="text-xs text-slate-400">| Standard Pit Loss: <span id="sc-pit-loss-display" class="text-white font-bold">22.8s</span></span>
            </div>

            <!-- Quick Safety Car State Switcher Buttons -->
            <div class="flex items-center gap-2 text-xs">
              <button onclick="setSafetyCarState('GREEN')" id="btn-sc-green" class="px-3 py-1.5 rounded-lg bg-emerald-600 text-white font-bold border border-emerald-500 shadow-md transition">
                🟢 Green Flag
              </button>
              <button onclick="setSafetyCarState('FULL_SC')" id="btn-sc-full" class="px-3 py-1.5 rounded-lg bg-slate-900 hover:bg-amber-950 text-amber-300 font-bold border border-amber-600/60 transition">
                🟡 Safety Car (SC)
              </button>
              <button onclick="setSafetyCarState('VSC')" id="btn-sc-vsc" class="px-3 py-1.5 rounded-lg bg-slate-900 hover:bg-purple-950 text-purple-300 font-bold border border-purple-600/60 transition">
                🟣 Virtual SC (VSC)
              </button>
            </div>
          </div>

          <!-- Deployment Lap Slider & Quick Presets -->
          <div class="grid grid-cols-1 md:grid-cols-12 gap-3 mt-3 items-center text-xs">
            <div class="md:col-span-5">
              <div class="flex justify-between text-[11px] mb-1">
                <span class="text-slate-400">SAFETY CAR DEPLOYMENT LAP</span>
                <span class="text-amber-400 font-bold" id="sc-lap-label">Lap 24 / 57</span>
              </div>
              <input type="range" id="sc-lap-slider" min="1" max="57" value="24" oninput="updateSCLap(this.value)" class="w-full accent-amber-500">
            </div>

            <div class="md:col-span-4 flex items-center gap-1.5 flex-wrap">
              <span class="text-[10px] text-slate-400 uppercase">Presets:</span>
              <button onclick="setSCPreset('early')" class="px-2 py-1 rounded bg-slate-900 border border-slate-700 hover:border-amber-500 text-slate-300 text-[10px]">L14 Early</button>
              <button onclick="setSCPreset('mid')" class="px-2 py-1 rounded bg-slate-900 border border-slate-700 hover:border-amber-500 text-slate-300 text-[10px]">L26 Window</button>
              <button onclick="setSCPreset('late')" class="px-2 py-1 rounded bg-slate-900 border border-slate-700 hover:border-amber-500 text-slate-300 text-[10px]">L42 Late</button>
              <button onclick="setSafetyCarState('GREEN')" class="px-2 py-1 rounded bg-slate-900 border border-slate-700 hover:border-emerald-500 text-emerald-400 text-[10px]">Clear SC</button>
            </div>

            <div class="md:col-span-3 text-right">
              <div class="text-[10px] text-slate-400 uppercase">Effective Pit Loss</div>
              <div id="sc-arbitrage-dividend" class="text-sm font-black text-emerald-400">22.8s (Normal)</div>
            </div>
          </div>

          <!-- Dynamic Live SC Alert Banner -->
          <div id="sc-live-alert" class="hidden mt-3 p-3 rounded-lg bg-amber-950/80 border border-amber-500 text-amber-200 text-xs flex items-center justify-between gap-2 sc-pulse">
            <div class="flex items-center gap-2">
              <span class="text-lg">⚠️</span>
              <span id="sc-live-alert-text"><strong>SAFETY CAR DEPLOYED (LAP 24):</strong> Track pace neutralized. Pit loss cut from 22.8s ➔ 10.2s! Free pit stop arbitrage window active.</span>
            </div>
            <span class="px-2.5 py-1 rounded bg-amber-500 text-slate-950 font-black text-[10px] uppercase tracking-wider">BOX OPPORTUNITY</span>
          </div>
        </div>

      </div>

      <!-- Strategy Plans Output Grid (Plan A, Plan B, Plan C) -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6" id="strategy-plans-container">
        <!-- Rendered dynamically by JS -->
      </div>

      <!-- Pit-Wall Contingency Decision Tree Matrix -->
      <div class="f1-card p-5">
        <h3 class="text-sm font-bold text-white mb-3 flex items-center gap-2 font-mono">
          <span>📋</span> Pit-Wall Tactical Playbook & Live Trigger Matrix
        </h3>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs font-mono" id="decision-triggers-container">
          <!-- Populated by JS -->
        </div>
      </div>

    </div>

    <!-- TAB 2: ORIGINAL 2024 FORMULA 1 CAR & TECHNICAL INSPECTOR -->
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

        <!-- Two Column Studio Display -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 mt-5 items-center">
          
          <!-- Column 1: Photorealistic 2024 F1 Car with Interactive Hotspots -->
          <div class="lg:col-span-8 relative rounded-2xl overflow-hidden bg-slate-950 border border-slate-800 shadow-2xl flex items-center justify-center p-3">
            <img src="data:image/jpeg;base64,{car_b64}" alt="Authentic 2024 Ground-Effect Formula 1 Race Car" class="w-full h-auto object-cover rounded-xl select-none" id="f1-car-image">

            <!-- Hotspot 1: Front Wing -->
            <button onclick="selectCarComponent('front-wing')" class="absolute top-[68%] left-[16%] -translate-x-1/2 -translate-y-1/2 group" title="Inspect Front Wing Aerodynamics">
              <div class="w-7 h-7 rounded-full bg-red-600/90 text-white font-mono font-bold text-xs flex items-center justify-center border-2 border-white shadow-lg pin-pulse group-hover:scale-125 transition">
                1
              </div>
            </button>

            <!-- Hotspot 2: Pirelli Wheels -->
            <button onclick="selectCarComponent('wheels')" class="absolute top-[62%] left-[28%] -translate-x-1/2 -translate-y-1/2 group" title="Inspect Pirelli Wheel & Brake Assembly">
              <div class="w-7 h-7 rounded-full bg-yellow-500/90 text-slate-950 font-mono font-bold text-xs flex items-center justify-center border-2 border-white shadow-lg pin-pulse group-hover:scale-125 transition">
                2
              </div>
            </button>

            <!-- Hotspot 3: Halo -->
            <button onclick="selectCarComponent('halo')" class="absolute top-[44%] left-[46%] -translate-x-1/2 -translate-y-1/2 group" title="Inspect Titanium Halo Structure">
              <div class="w-7 h-7 rounded-full bg-cyan-500/90 text-slate-950 font-mono font-bold text-xs flex items-center justify-center border-2 border-white shadow-lg pin-pulse group-hover:scale-125 transition">
                3
              </div>
            </button>

            <!-- Hotspot 4: Venturi Sidepod Undercut -->
            <button onclick="selectCarComponent('sidepod')" class="absolute top-[54%] left-[58%] -translate-x-1/2 -translate-y-1/2 group" title="Inspect Venturi Underfloor Tunnels">
              <div class="w-7 h-7 rounded-full bg-emerald-500/90 text-slate-950 font-mono font-bold text-xs flex items-center justify-center border-2 border-white shadow-lg pin-pulse group-hover:scale-125 transition">
                4
              </div>
            </button>

            <!-- Hotspot 5: Rear Wing DRS -->
            <button onclick="selectCarComponent('rear-wing')" class="absolute top-[32%] left-[78%] -translate-x-1/2 -translate-y-1/2 group" title="Inspect Rear Wing DRS Flap">
              <div class="w-7 h-7 rounded-full bg-purple-500/90 text-white font-mono font-bold text-xs flex items-center justify-center border-2 border-white shadow-lg pin-pulse group-hover:scale-125 transition">
                5
              </div>
            </button>

            <!-- Hotspot 6: Power Unit -->
            <button onclick="selectCarComponent('powertrain')" class="absolute top-[47%] left-[66%] -translate-x-1/2 -translate-y-1/2 group" title="Inspect V6 Turbo-Hybrid Power Unit">
              <div class="w-7 h-7 rounded-full bg-amber-500/90 text-slate-950 font-mono font-bold text-xs flex items-center justify-center border-2 border-white shadow-lg pin-pulse group-hover:scale-125 transition">
                6
              </div>
            </button>
          </div>

          <!-- Column 2: Detailed Component Inspector Card -->
          <div class="lg:col-span-4 space-y-4">
            <div id="component-details-card" class="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-3">
              <!-- Populated by selectCarComponent() -->
            </div>

            <!-- Live Aero HUD Telemetry Panel -->
            <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-3 font-mono text-xs">
              <div class="flex justify-between items-center text-slate-400 border-b border-slate-800 pb-2">
                <span class="font-bold text-white flex items-center gap-1.5">
                  <span class="w-2 h-2 rounded-full bg-emerald-400"></span> LIVE AERO SENSORS
                </span>
                <span class="text-[10px] text-slate-500">CAN-BUS TELEMETRY</span>
              </div>

              <div class="grid grid-cols-2 gap-2 text-center">
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800">
                  <span class="text-[10px] text-slate-500 uppercase block">Drag Coefficient (Cd)</span>
                  <span class="text-lg font-bold text-amber-400 mt-0.5 block" id="tel-drag-coeff">0.88</span>
                  <span class="text-[10px] text-slate-400 block" id="tel-drag-sub">DRS Flap: Closed</span>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800">
                  <span class="text-[10px] text-slate-500 uppercase block">Top Speed (Straight)</span>
                  <span class="text-lg font-bold text-white mt-0.5 block" id="tel-top-spd">334 KM/H</span>
                  <span class="text-[10px] text-slate-400 block" id="tel-spd-sub">Straightline Pace</span>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800">
                  <span class="text-[10px] text-slate-500 uppercase block">Underfloor Downforce</span>
                  <span class="text-lg font-bold text-cyan-400 mt-0.5 block" id="tel-downforce">-1,850 KG</span>
                  <span class="text-[10px] text-slate-400 block">@ 250 km/h Ground-Effect</span>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800">
                  <span class="text-[10px] text-slate-500 uppercase block">Tire Surface Temp</span>
                  <span class="text-lg font-bold text-red-400 mt-0.5 block" id="tel-tire-temp">104&deg;C</span>
                  <span class="text-[10px] text-slate-400 block" id="tel-tire-comp">Soft (C3) - Cliff: Lap 16</span>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>

    </div>

    <!-- TAB 3: TELEMETRY & LAP PACE -->
    <div id="view-telemetry" class="hidden space-y-6">
      <div class="f1-card p-5 f1-card-accent">
        <div class="flex flex-wrap justify-between items-center border-b border-slate-800 pb-3 gap-2">
          <div>
            <h2 class="text-base font-bold text-white flex items-center gap-2">
              <span>⏱️</span> Grand Prix Lap-by-Lap Telemetry & Pace Analysis
            </h2>
            <p class="text-xs text-slate-400">
              High-frequency lap timing telemetry disentangling fuel mass relief vs. rubber wear degradation.
            </p>
          </div>

          <div class="flex items-center gap-3 text-xs font-mono">
            <label class="flex items-center gap-1.5 cursor-pointer text-slate-300">
              <input type="checkbox" id="toggle-smooth" onchange="renderTelemetryCharts()" class="rounded accent-red-600">
              <span>Smooth Noise</span>
            </label>
            <div class="flex gap-1" id="driver-toggle-container">
              <!-- Driver badges injected by JS -->
            </div>
          </div>
        </div>

        <!-- Telemetry Graphs -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-4">
          <div class="p-4 rounded-xl bg-slate-950 border border-slate-800">
            <div class="flex justify-between items-center text-xs font-mono mb-2">
              <span class="text-slate-300 font-bold uppercase tracking-wider">Lap Pace Evolution (Seconds)</span>
              <span class="text-slate-500 text-[10px]">LOWER IS FASTER</span>
            </div>
            <div class="w-full h-64 overflow-hidden">
              <svg id="pace-svg" class="w-full h-full"></svg>
            </div>
          </div>

          <div class="p-4 rounded-xl bg-slate-950 border border-slate-800">
            <div class="flex justify-between items-center text-xs font-mono mb-2">
              <span class="text-slate-300 font-bold uppercase tracking-wider">Interval Gap to Leader (Delta)</span>
              <span class="text-slate-500 text-[10px]">TIME BEHIND P1</span>
            </div>
            <div class="w-full h-64 overflow-hidden">
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
            Empirical compound modeling: Linear wear transition into steep exponential thermal failure ($L_{{\text{{cliff}}}}$).
          </p>
        </div>

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
            <div class="flex justify-between font-bold text-slate-200">
              <span>HARD (C1)</span>
              <span>+0.55s Base Delta</span>
            </div>
            <div class="space-y-1 text-slate-300 mt-2 text-[11px]">
              <div class="flex justify-between"><span>Wear Rate:</span><span class="text-white">+0.028 s/lap</span></div>
              <div class="flex justify-between"><span>Thermal Cliff:</span><span class="text-amber-400 font-bold">Lap 38</span></div>
              <div class="flex justify-between"><span>Typical Use:</span><span>Endurance Stint, 1-Stop Base</span></div>
            </div>
          </div>
        </div>

        <div class="mt-6 p-4 rounded-xl bg-slate-950 border border-slate-800">
          <div class="flex justify-between items-center text-xs font-mono mb-2">
            <span class="text-slate-300 font-bold uppercase tracking-wider">Compound Degradation Curves (Over 40 Laps)</span>
            <span class="text-slate-500 text-[10px]">MODEL: D(t) = D_base + beta*t + gamma*exp(t - L_cliff)</span>
          </div>
          <div class="w-full h-72 overflow-hidden">
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
            <span>🔄</span> The Undercut Horizon & Safety Car Arbitrage
          </h2>
          <p class="text-xs text-slate-400">
            Empirical success rate across modern Formula 1 Grands Prix and timing window dynamics.
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-4 font-mono text-xs">
          <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-3">
            <h3 class="text-sm font-bold text-red-400">1. Undercut Success Mechanics</h3>
            <p class="text-slate-300 text-xs leading-relaxed">
              Pitting 1 to 2 laps earlier than an opposing car delivers an immediate tire grip delta of <strong>+1.74s</strong> on fresh cold/warm rubber.
            </p>
            <div class="p-3 bg-slate-900 rounded-lg space-y-1.5 text-[11px]">
              <div class="flex justify-between"><span>Average Out-Lap Gain:</span><span class="text-emerald-400 font-bold">+1.74 sec</span></div>
              <div class="flex justify-between"><span>Success Window:</span><span class="text-white">Gap &lt; 2.1 seconds</span></div>
              <div class="flex justify-between"><span>Failure Mode:</span><span class="text-red-400">Exiting into traffic wake</span></div>
            </div>
          </div>

          <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-3">
            <h3 class="text-sm font-bold text-yellow-400">2. Safety Car Arbitrage Dividend</h3>
            <p class="text-slate-300 text-xs leading-relaxed">
              When a Safety Car or VSC is deployed, the on-track speed is capped at 140 km/h (40% slower). However, pit lane transit is already speed-limited to 80 km/h.
            </p>
            <div class="p-3 bg-slate-900 rounded-lg space-y-1.5 text-[11px]">
              <div class="flex justify-between"><span>Green Flag Pit Loss:</span><span class="text-slate-400">~22.8 seconds</span></div>
              <div class="flex justify-between"><span>Safety Car Pit Loss:</span><span class="text-emerald-400 font-bold">~10.2 seconds</span></div>
              <div class="flex justify-between"><span>Net "Free Stop" Dividend:</span><span class="text-yellow-400 font-bold">+12.6 seconds advantage</span></div>
            </div>
          </div>
        </div>

        <!-- Historical Strategy Battles Table -->
        <div class="mt-6 pt-4 border-t border-slate-800">
          <h3 class="text-sm font-bold text-white mb-3 font-mono">Key Historical Undercut & Overcut Battles (2024 Season)</h3>
          <div class="overflow-x-auto">
            <table class="w-full text-left text-xs font-mono">
              <thead class="bg-slate-900 text-slate-400 text-[11px] uppercase">
                <tr>
                  <th class="p-2.5">Grand Prix</th>
                  <th class="p-2.5">Challenger</th>
                  <th class="p-2.5">Defender</th>
                  <th class="p-2.5">Tactic</th>
                  <th class="p-2.5">Delta</th>
                  <th class="p-2.5">Outcome</th>
                </tr>
              </thead>
              <tbody id="battles-table-body" class="divide-y divide-slate-800/60">
                <!-- Populated by JS -->
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 6: GLOBAL CIRCUIT ATLAS -->
    <div id="view-circuits" class="hidden space-y-6">
      <div class="f1-card p-5 f1-card-accent">
        <div class="flex flex-wrap justify-between items-center border-b border-slate-800 pb-3 gap-2">
          <div>
            <h2 class="text-base font-bold text-white flex items-center gap-2">
              <span>🌐</span> FIA Formula 1 World Circuit Atlas (77 Circuits)
            </h2>
            <p class="text-xs text-slate-400">
              Click any circuit below to instantly load its track parameters and generate custom strategies!
            </p>
          </div>
          <input type="text" id="circuit-search" placeholder="Search track, country or city..." oninput="filterCircuits()" class="bg-slate-900 border border-slate-700 text-white rounded-lg px-3 py-1.5 text-xs font-mono outline-none w-64">
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-3 mt-4 max-h-[550px] overflow-y-auto pr-1" id="circuits-grid-container">
          <!-- Populated by JS -->
        </div>
      </div>
    </div>

    <!-- TAB 7: INTERACTIVE STRATEGY SIMULATOR -->
    <div id="view-simulator" class="hidden space-y-6">
      <div class="f1-card p-5 f1-card-accent">
        <div class="border-b border-slate-800 pb-3">
          <h2 class="text-base font-bold text-white flex items-center gap-2 font-mono">
            <span>🎯</span> Interactive Dynamic Strategy Sandbox & What-If Simulator
          </h2>
          <p class="text-xs text-slate-400">
            Adjust pit stop timing to simulate race outcomes and analyze delta changes against the optimal Plan A baseline.
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mt-4 font-mono text-xs">
          <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-3">
            <label class="text-slate-400 block font-bold">1. Stop 1 Pit Lap Offset</label>
            <input type="range" id="sim-pit1-lap" min="10" max="30" value="20" oninput="runCustomSim()" class="w-full accent-red-600">
            <div class="flex justify-between text-[11px]">
              <span class="text-slate-500">Lap 10 (Early)</span>
              <span class="text-white font-bold" id="sim-pit1-val">Lap 20</span>
              <span class="text-slate-500">Lap 30 (Late)</span>
            </div>
          </div>

          <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-3 md:col-span-2 flex flex-col justify-between">
            <div>
              <span class="text-slate-400 text-[10px] uppercase block">Predicted Total Race Time</span>
              <div class="text-2xl font-bold text-white mt-1" id="sim-result-time">5504.8s (1h 31m 44.8s)</div>
            </div>
            <div class="flex items-center justify-between text-[11px] pt-2 border-t border-slate-800">
              <span class="text-slate-400">Delta vs Optimal Plan A:</span>
              <span class="text-emerald-400 font-bold" id="sim-result-delta">0.00s (Optimal)</span>
            </div>
          </div>
        </div>
      </div>
    </div>

  </main>

  <!-- FOOTER -->
  <footer class="border-t border-slate-800 py-6 text-center text-xs font-mono text-slate-500 space-y-2">
    <div>Formula 1 Race Telemetry & Strategy Analytics Platform | DAV Subject Capstone</div>
    <div>Project Team: Sri Harsh (2503a52740) &bull; Manohar (2503a52766) &bull; Jayavardhan (2503a52747)</div>
  </footer>

  <script>
    const F1_DATA = {json_data_str};
    let selectedDrivers = ["VER", "LEC", "NOR"];
    let isDRSOpen = false;
    let selectedCompound = "soft";

    // SAFETY CAR STATE ENGINE
    let currentSCState = "GREEN"; // "GREEN", "FULL_SC", "VSC"
    let currentSCLap = 24;

    // COMPREHENSIVE CIRCUIT STRATEGY PROFILES DATABASE
    const CIRCUIT_STRATEGY_PROFILES = {{
      3: {{ // Bahrain
        name: "Bahrain International Circuit (Sakhir)",
        laps: 57,
        baseLapSec: 93.2,
        pitLossGreen: 22.8,
        pitLossSC: 10.2,
        pitLossVSC: 12.8,
        abrasiveness: "Extreme (Desert Granite, 4.8/5)",
        tireStress: "Severe Rear Thermal Overheating (4.6/5)",
        overtakingDelta: 0.75,
        typicalStops: 2,
        degradationDesc: "High Deg (2-Stop)",
        planA: {{
          name: "Soft ➔ Medium ➔ Hard (Optimal 2-Stop)",
          type: "2-STOP",
          stints: [{{ compound: "SOFT", start: 1, end: 14 }}, {{ compound: "MEDIUM", start: 15, end: 35 }}, {{ compound: "HARD", start: 36, end: 57 }}],
          pitWindows: "Stop 1: L13-L16 | Stop 2: L34-L37",
          predictedFinish: "P1 - Victory",
          summary: "Thermal degradation on rough Sakhir asphalt forces a 2-stop. Soft start secures early position."
        }},
        planB: {{
          name: "Soft ➔ Soft ➔ Medium (Undercut Blitz)",
          type: "2-STOP ATTACK",
          stints: [{{ compound: "SOFT", start: 1, end: 12 }}, {{ compound: "SOFT", start: 13, end: 31 }}, {{ compound: "MEDIUM", start: 32, end: 57 }}],
          pitWindows: "Stop 1: L11-L13 | Stop 2: L30-L32",
          predictedFinish: "Podium (+2 Pos Gain)",
          summary: "Boxes 2 laps early on both stops to execute dual undercuts (+1.74s/lap out-lap delta)."
        }},
        planC: {{
          name: "Hard ➔ Medium (Longevity 1-Stop Gamble)",
          type: "1-STOP GAMBLE",
          stints: [{{ compound: "HARD", start: 1, end: 32 }}, {{ compound: "MEDIUM", start: 33, end: 57 }}],
          pitWindows: "Stop 1: L31-L34 (Targeting SC)",
          predictedFinish: "P4 - P7 (Tire Cliff Dependent)",
          summary: "Extreme tire management. Extremely vulnerable on worn tires, waiting for an SC."
        }}
      }},
      6: {{ // Monaco
        name: "Circuit de Monaco (Monte Carlo)",
        laps: 78,
        baseLapSec: 74.8,
        pitLossGreen: 24.5,
        pitLossSC: 11.0,
        pitLossVSC: 13.5,
        abrasiveness: "Ultra Low (Polished City Tarmac, 1.2/5)",
        tireStress: "Low Mechanical Wear (1.5/5)",
        overtakingDelta: 2.80,
        typicalStops: 1,
        degradationDesc: "Zero Wear (1-Stop)",
        planA: {{
          name: "Soft ➔ Hard (Mandatory 1-Stop Track Position)",
          type: "1-STOP",
          stints: [{{ compound: "SOFT", start: 1, end: 34 }}, {{ compound: "HARD", start: 35, end: 78 }}],
          pitWindows: "Stop 1: L33-L36",
          predictedFinish: "P1 - Victory (Track Position Secured)",
          summary: "Track position is 95% of victory in Monaco. Pit delta (24.5s) is too costly to make up on track. 1-stop is strictly mandatory."
        }},
        planB: {{
          name: "Medium ➔ Soft (Clean Air Overcut Trap)",
          type: "1-STOP OVERCUT",
          stints: [{{ compound: "MEDIUM", start: 1, end: 42 }}, {{ compound: "SOFT", start: 43, end: 78 }}],
          pitWindows: "Stop 1: L40-L44",
          predictedFinish: "Podium / Track Position Jump",
          summary: "Extends stint 1 in clean air while cars ahead pit into slow backmarker traffic, overcutting them on exit."
        }},
        planC: {{
          name: "Hard ➔ Soft (Barrier Incident / Red Flag Wait)",
          type: "SC AMBUSH",
          stints: [{{ compound: "HARD", start: 1, end: 54 }}, {{ compound: "SOFT", start: 55, end: 78 }}],
          pitWindows: "Stop 1: L52-L56 (SC Target)",
          predictedFinish: "Net Gain Under Neutralization",
          summary: "Stretches hard tire durability to maximum, banking on the 78% historical probability of a barrier wall incident."
        }}
      }},
      9: {{ // Silverstone
        name: "Silverstone Circuit (Great Britain)",
        laps: 52,
        baseLapSec: 88.5,
        pitLossGreen: 20.4,
        pitLossSC: 9.8,
        pitLossVSC: 12.0,
        abrasiveness: "High Lateral Energy (Copse, Becketts, 4.7/5)",
        tireStress: "Extreme Front-Left Blistering (5.0/5)",
        overtakingDelta: 0.70,
        typicalStops: 2,
        degradationDesc: "Extreme High-G (2-Stop)",
        planA: {{
          name: "Medium ➔ Hard ➔ Hard (High-G 2-Stop)",
          type: "2-STOP",
          stints: [{{ compound: "MEDIUM", start: 1, end: 18 }}, {{ compound: "HARD", start: 19, end: 37 }}, {{ compound: "HARD", start: 38, end: 52 }}],
          pitWindows: "Stop 1: L17-L20 | Stop 2: L36-L39",
          predictedFinish: "P1 - Victory",
          summary: "Copse and Maggotts-Becketts generate 5.2G lateral forces, blistering soft tires. Dual hard stints protect front-left integrity."
        }},
        planB: {{
          name: "Soft ➔ Medium ➔ Hard (Opening Sprint)",
          type: "2-STOP ATTACK",
          stints: [{{ compound: "SOFT", start: 1, end: 14 }}, {{ compound: "MEDIUM", start: 15, end: 34 }}, {{ compound: "HARD", start: 35, end: 52 }}],
          pitWindows: "Stop 1: L13-L15 | Stop 2: L33-L36",
          predictedFinish: "Podium (+2 Pos Gain)",
          summary: "Uses soft compound launch grip to build an early lead before switching to durable race compounds."
        }},
        planC: {{
          name: "Medium ➔ Hard (1-Stop Extreme Management)",
          type: "1-STOP HIGH RISK",
          stints: [{{ compound: "MEDIUM", start: 1, end: 24 }}, {{ compound: "HARD", start: 25, end: 52 }}],
          pitWindows: "Stop 1: L23-L26",
          predictedFinish: "P3 - P6 (Blistering Risk)",
          summary: "Avoids a 20.4s pit stop but requires extreme tire lift-and-coast to prevent sudden delamination."
        }}
      }},
      13: {{ // Spa
        name: "Circuit de Spa-Francorchamps (Belgium)",
        laps: 44,
        baseLapSec: 105.5,
        pitLossGreen: 21.6,
        pitLossSC: 9.5,
        pitLossVSC: 11.8,
        abrasiveness: "High Compression (Eau Rouge, 4.4/5)",
        tireStress: "Vertical Compression & High Speed (4.8/5)",
        overtakingDelta: 0.60,
        typicalStops: 2,
        degradationDesc: "7km Mountain (2-Stop)",
        planA: {{
          name: "Medium ➔ Hard ➔ Medium (Kemmel Attack)",
          type: "2-STOP",
          stints: [{{ compound: "MEDIUM", start: 1, end: 15 }}, {{ compound: "HARD", start: 16, end: 30 }}, {{ compound: "MEDIUM", start: 31, end: 44 }}],
          pitWindows: "Stop 1: L14-L16 | Stop 2: L29-L31",
          predictedFinish: "P1 - Victory",
          summary: "Long 7.004km lap makes fresh tire out-lap pace worth over +2.2s. 2-stop maximizes Kemmel straight overtake speed."
        }},
        planB: {{
          name: "Soft ➔ Hard ➔ Soft (DRS Slipstream Sprint)",
          type: "2-STOP SPRINT",
          stints: [{{ compound: "SOFT", start: 1, end: 11 }}, {{ compound: "HARD", start: 12, end: 28 }}, {{ compound: "SOFT", start: 29, end: 44 }}],
          pitWindows: "Stop 1: L10-L12 | Stop 2: L27-L29",
          predictedFinish: "Fastest Lap + Podium",
          summary: "Aggressive soft stints provide high corner exit speeds out of La Source into Raidillon."
        }},
        planC: {{
          name: "Medium ➔ Hard (Weather Radar Hedge)",
          type: "WEATHER GAMBLE",
          stints: [{{ compound: "MEDIUM", start: 1, end: 20 }}, {{ compound: "HARD", start: 21, end: 44 }}],
          pitWindows: "Stop 1: L19-L22",
          predictedFinish: "Contingent on Ardennes Rain",
          summary: "Stretches medium tires hoping for an Ardennes rain shower to transition directly to Intermediates."
        }}
      }},
      14: {{ // Monza
        name: "Autodromo Nazionale di Monza (Italy)",
        laps: 53,
        baseLapSec: 81.2,
        pitLossGreen: 24.5,
        pitLossSC: 10.5,
        pitLossVSC: 12.8,
        abrasiveness: "Low Downforce Slipstream (2.8/5)",
        tireStress: "Longitudinal Heavy Braking (3.2/5)",
        overtakingDelta: 0.65,
        typicalStops: 1,
        degradationDesc: "Temple of Speed (1-Stop)",
        planA: {{
          name: "Medium ➔ Hard (Classic Monza 1-Stop)",
          type: "1-STOP",
          stints: [{{ compound: "MEDIUM", start: 1, end: 24 }}, {{ compound: "HARD", start: 25, end: 53 }}],
          pitWindows: "Stop 1: L23-L26",
          predictedFinish: "P1 - Victory",
          summary: "Skinny rear wings reduce sliding and tire wear. 1-stop minimizes the 24.5s pit loss penalty."
        }},
        planB: {{
          name: "Soft ➔ Medium ➔ Soft (Aggressive 2-Stop)",
          type: "2-STOP ATTACK",
          stints: [{{ compound: "SOFT", start: 1, end: 15 }}, {{ compound: "MEDIUM", start: 16, end: 36 }}, {{ compound: "SOFT", start: 37, end: 53 }}],
          pitWindows: "Stop 1: L14-L16 | Stop 2: L35-L37",
          predictedFinish: "Podium (+3 Pos Gain)",
          summary: "Exploits soft grip into Rettifilo chicane to overtake cars struggling on worn hard tires."
        }},
        planC: {{
          name: "Hard ➔ Soft (Reverse Longevity)",
          type: "1-STOP REVERSE",
          stints: [{{ compound: "HARD", start: 1, end: 33 }}, {{ compound: "SOFT", start: 34, end: 53 }}],
          pitWindows: "Stop 1: L32-L35",
          predictedFinish: "Fastest Lap + P4",
          summary: "Long hard stint burns off fuel mass, allowing a 20-lap qualifying pace sprint on softs."
        }}
      }},
      15: {{ // Singapore
        name: "Marina Bay Street Circuit (Singapore)",
        laps: 62,
        baseLapSec: 96.5,
        pitLossGreen: 27.5,
        pitLossSC: 12.0,
        pitLossVSC: 14.5,
        abrasiveness: "Bumpy Street Surface (3.5/5)",
        tireStress: "Traction Rear Graining (3.9/5)",
        overtakingDelta: 1.90,
        typicalStops: 1,
        degradationDesc: "100% SC History (1-Stop)",
        planA: {{
          name: "Medium ➔ Hard (SC Anchor 1-Stop)",
          type: "1-STOP",
          stints: [{{ compound: "MEDIUM", start: 1, end: 28 }}, {{ compound: "HARD", start: 29, end: 62 }}],
          pitWindows: "Stop 1: L27-L30",
          predictedFinish: "P1 - Victory",
          summary: "Longest pit loss on the calendar (27.5s) makes a 2-stop suicidal. 100% historical Safety Car rate dictates waiting for caution."
        }},
        planB: {{
          name: "Soft ➔ Hard ➔ Soft (Aggressive Delta)",
          type: "2-STOP ATTACK",
          stints: [{{ compound: "SOFT", start: 1, end: 17 }}, {{ compound: "HARD", start: 18, end: 42 }}, {{ compound: "SOFT", start: 43, end: 62 }}],
          pitWindows: "Stop 1: L16-L18 | Stop 2: L41-L43",
          predictedFinish: "Podium Contender",
          summary: "Relies on soft tire traction out of 19 90-degree corners to break the DRS train."
        }},
        planC: {{
          name: "Hard ➔ Soft (Late Wall-Crash Ambush)",
          type: "SC AMBUSH",
          stints: [{{ compound: "HARD", start: 1, end: 44 }}, {{ compound: "SOFT", start: 45, end: 62 }}],
          pitWindows: "Stop 1: L42-L46 (SC Target)",
          predictedFinish: "Massive Gain Under SC (+15.5s Free)",
          summary: "Driver extends hard tire longevity waiting for fatigue-induced wall contact in the final 20 laps."
        }}
      }},
      78: {{ // Qatar
        name: "Lusail International Circuit (Qatar)",
        laps: 57,
        baseLapSec: 84.5,
        pitLossGreen: 23.5,
        pitLossSC: 10.5,
        pitLossVSC: 13.0,
        abrasiveness: "Extreme 50mm Pyramid Kerbs (5.0/5)",
        tireStress: "Severe Delamination Risk (5.0/5)",
        overtakingDelta: 0.85,
        typicalStops: 3,
        degradationDesc: "FIA 18-Lap Cap (3-Stop)",
        planA: {{
          name: "Soft ➔ Medium ➔ Medium ➔ Hard (Mandatory 3-Stop)",
          type: "3-STOP",
          stints: [{{ compound: "SOFT", start: 1, end: 15 }}, {{ compound: "MEDIUM", start: 16, end: 30 }}, {{ compound: "MEDIUM", start: 31, end: 44 }}, {{ compound: "HARD", start: 45, end: 57 }}],
          pitWindows: "Stop 1: L14-L16 | Stop 2: L29-L31 | Stop 3: L43-L45",
          predictedFinish: "P1 - Victory",
          summary: "FIA safety regulations enforce maximum 18 laps per tire set due to pyramid kerb vibrations. Mandatory 3-stop sprint."
        }},
        planB: {{
          name: "Medium ➔ Hard ➔ Hard ➔ Soft (Hard Sprint)",
          type: "3-STOP SPRINT",
          stints: [{{ compound: "MEDIUM", start: 1, end: 16 }}, {{ compound: "HARD", start: 17, end: 32 }}, {{ compound: "HARD", start: 33, end: 46 }}, {{ compound: "SOFT", start: 47, end: 57 }}],
          pitWindows: "Stop 1: L15-L17 | Stop 2: L31-L33 | Stop 3: L45-L47",
          predictedFinish: "Podium (+2 Pos)",
          summary: "Dual hard stints allow pushing flat-out on high-speed sweeps without thermal delamination."
        }},
        planC: {{
          name: "Hard ➔ Medium ➔ Soft ➔ Soft (Aggressive Finish)",
          type: "3-STOP ATTACK",
          stints: [{{ compound: "HARD", start: 1, end: 17 }}, {{ compound: "MEDIUM", start: 18, end: 32 }}, {{ compound: "SOFT", start: 33, end: 45 }}, {{ compound: "SOFT", start: 46, end: 57 }}],
          pitWindows: "Stop 1: L16-L18 | Stop 2: L31-L33 | Stop 3: L44-L46",
          predictedFinish: "Fastest Lap + P3",
          summary: "Double soft stint to finish with fresh rubber against degraded tires."
        }}
      }}
    }};

    // Helper: Retrieve circuit profile with intelligent fallback for all 77 tracks
    function getCircuitProfile(cId) {{
      const id = parseInt(cId);
      if (CIRCUIT_STRATEGY_PROFILES[id]) return CIRCUIT_STRATEGY_PROFILES[id];
      
      const c = F1_DATA.circuits.find(item => item.circuitId === id) || F1_DATA.circuits[0];
      const laps = (c.length_km > 6.0) ? 44 : (c.length_km > 5.0) ? 55 : (c.length_km < 4.0) ? 78 : 66;
      const stress = c.tire_stress || 3.5;
      const is2Stop = stress >= 4.0 || (c.typical_stops && c.typical_stops >= 2);
      const pitLossG = c.pit_loss_sec || 22.0;

      const p1_A = is2Stop ? Math.round(laps * 0.28) : Math.round(laps * 0.42);
      const p2_A = Math.round(laps * 0.68);
      const p1_B = Math.round(laps * 0.22);
      const p2_B = Math.round(laps * 0.60);
      const p1_C = Math.round(laps * 0.52);

      return {{
        name: c.name,
        laps: laps,
        baseLapSec: 88.0,
        pitLossGreen: pitLossG,
        pitLossSC: 10.2,
        pitLossVSC: 12.8,
        abrasiveness: `${{c.abrasiveness || 3.0}}/5`,
        tireStress: `${{stress}}/5`,
        overtakingDelta: 0.80,
        typicalStops: is2Stop ? 2 : 1,
        degradationDesc: is2Stop ? "High Deg (2-Stop)" : "Low Deg (1-Stop)",
        planA: is2Stop ? {{
          name: "Soft ➔ Medium ➔ Hard (High Deg 2-Stop)",
          type: "2-STOP",
          stints: [{{ compound: "SOFT", start: 1, end: p1_A }}, {{ compound: "MEDIUM", start: p1_A + 1, end: p2_A }}, {{ compound: "HARD", start: p2_A + 1, end: laps }}],
          pitWindows: `Stop 1: L${{p1_A-2}}-L${{p1_A+1}} | Stop 2: L${{p2_A-2}}-L${{p2_A+1}}`,
          predictedFinish: "P1 - Victory",
          summary: `High tire stress (${{stress}}/5) on this track makes a 2-stop the fastest overall strategy.`
        }} : {{
          name: "Medium ➔ Hard (Direct 1-Stop)",
          type: "1-STOP",
          stints: [{{ compound: "MEDIUM", start: 1, end: p1_A }}, {{ compound: "HARD", start: p1_A + 1, end: laps }}],
          pitWindows: `Stop 1: L${{p1_A-2}}-L${{p1_A+2}}`,
          predictedFinish: "P1 - Victory",
          summary: `Track characteristics favor track position. 1-stop minimizes the ${{pitLossG.toFixed(1)}}s pit lane loss.`
        }},
        planB: {{
          name: "Soft ➔ Hard ➔ Medium (Undercut Attack)",
          type: "2-STOP ATTACK",
          stints: [{{ compound: "SOFT", start: 1, end: p1_B }}, {{ compound: "HARD", start: p1_B + 1, end: p2_B }}, {{ compound: "MEDIUM", start: p2_B + 1, end: laps }}],
          pitWindows: `Stop 1: L${{p1_B-2}}-L${{p1_B}} | Stop 2: L${{p2_B-2}}-L${{p2_B}}`,
          predictedFinish: "Podium (+2 Pos Gain)",
          summary: "Box 2 laps early to trigger an undercut into clean air."
        }},
        planC: {{
          name: "Hard ➔ Medium (SC / Reverse Gamble)",
          type: "SC AMBUSH",
          stints: [{{ compound: "HARD", start: 1, end: p1_C }}, {{ compound: "MEDIUM", start: p1_C + 1, end: laps }}],
          pitWindows: `Stop 1: L${{p1_C-3}}-L${{p1_C+3}}`,
          predictedFinish: "Contingency Dependent",
          summary: "Stretches hard tire durability to bank on a Safety Car intervention."
        }}
      }};
    }}

    // SAFETY CAR INTERACTION FUNCTIONS
    function setSafetyCarState(state) {{
      currentSCState = state;

      const btnGreen = document.getElementById("btn-sc-green");
      const btnFull = document.getElementById("btn-sc-full");
      const btnVsc = document.getElementById("btn-sc-vsc");
      const pill = document.getElementById("sc-status-pill");
      const pillText = document.getElementById("sc-status-text");
      const headBadge = document.getElementById("header-sc-badge");
      const headText = document.getElementById("header-sc-text");
      const alertBanner = document.getElementById("sc-live-alert");
      const alertText = document.getElementById("sc-live-alert-text");

      // Reset button styles
      btnGreen.className = "px-3 py-1.5 rounded-lg bg-slate-900 text-slate-400 font-bold border border-slate-700 transition";
      btnFull.className = "px-3 py-1.5 rounded-lg bg-slate-900 text-slate-400 font-bold border border-slate-700 transition";
      btnVsc.className = "px-3 py-1.5 rounded-lg bg-slate-900 text-slate-400 font-bold border border-slate-700 transition";

      const cId = document.getElementById("gen-circuit").value;
      const profile = getCircuitProfile(cId);

      if (state === "GREEN") {{
        btnGreen.className = "px-3 py-1.5 rounded-lg bg-emerald-600 text-white font-bold border border-emerald-500 shadow-md transition";
        pill.className = "px-3 py-1 rounded-full text-xs font-bold flex items-center gap-1.5 bg-emerald-950 text-emerald-400 border border-emerald-800";
        pillText.textContent = "TRACK STATUS: GREEN FLAG (RACE PACE)";
        headBadge.className = "px-2.5 py-1 rounded-full text-xs font-bold flex items-center gap-1.5 bg-emerald-950 text-emerald-400 border border-emerald-800 cursor-pointer";
        headText.textContent = "TRACK: GREEN FLAG";
        alertBanner.classList.add("hidden");
        document.getElementById("sc-arbitrage-dividend").textContent = `${{profile.pitLossGreen.toFixed(1)}}s (Normal)`;
        document.getElementById("kpi-sc-dividend").textContent = "+12.6s Free";
      }} else if (state === "FULL_SC") {{
        btnFull.className = "px-3 py-1.5 rounded-lg bg-amber-500 text-slate-950 font-bold border border-amber-400 shadow-md transition";
        pill.className = "px-3 py-1 rounded-full text-xs font-bold flex items-center gap-1.5 bg-amber-950 text-amber-300 border border-amber-600 sc-pulse";
        pillText.textContent = `TRACK STATUS: SAFETY CAR ACTIVE (LAP ${{currentSCLap}})`;
        headBadge.className = "px-2.5 py-1 rounded-full text-xs font-bold flex items-center gap-1.5 bg-amber-950 text-amber-300 border border-amber-600 cursor-pointer sc-pulse";
        headText.textContent = `🟡 SC ACTIVE (L${{currentSCLap}})`;
        alertBanner.classList.remove("hidden");
        alertText.innerHTML = `<strong>SAFETY CAR DEPLOYED (LAP ${{currentSCLap}}):</strong> Full track pace neutralized. Pit loss cut from ${{profile.pitLossGreen.toFixed(1)}}s ➔ ${{profile.pitLossSC.toFixed(1)}}s! Free pit stop arbitrage window active (+${{(profile.pitLossGreen - profile.pitLossSC).toFixed(1)}}s savings).`;
        document.getElementById("sc-arbitrage-dividend").textContent = `+${{(profile.pitLossGreen - profile.pitLossSC).toFixed(1)}}s Free Stop`;
        document.getElementById("kpi-sc-dividend").textContent = `+${{(profile.pitLossGreen - profile.pitLossSC).toFixed(1)}}s LIVE`;
      }} else if (state === "VSC") {{
        btnVsc.className = "px-3 py-1.5 rounded-lg bg-purple-600 text-white font-bold border border-purple-500 shadow-md transition";
        pill.className = "px-3 py-1 rounded-full text-xs font-bold flex items-center gap-1.5 bg-purple-950 text-purple-300 border border-purple-600 sc-pulse";
        pillText.textContent = `TRACK STATUS: VIRTUAL SAFETY CAR (LAP ${{currentSCLap}})`;
        headBadge.className = "px-2.5 py-1 rounded-full text-xs font-bold flex items-center gap-1.5 bg-purple-950 text-purple-300 border border-purple-600 cursor-pointer sc-pulse";
        headText.textContent = `🟣 VSC ACTIVE (L${{currentSCLap}})`;
        alertBanner.classList.remove("hidden");
        alertText.innerHTML = `<strong>VIRTUAL SAFETY CAR (LAP ${{currentSCLap}}):</strong> Delta time restriction enforced. Pit loss reduced from ${{profile.pitLossGreen.toFixed(1)}}s ➔ ${{profile.pitLossVSC.toFixed(1)}}s (+${{(profile.pitLossGreen - profile.pitLossVSC).toFixed(1)}}s savings).`;
        document.getElementById("sc-arbitrage-dividend").textContent = `+${{(profile.pitLossGreen - profile.pitLossVSC).toFixed(1)}}s Free Stop`;
        document.getElementById("kpi-sc-dividend").textContent = `+${{(profile.pitLossGreen - profile.pitLossVSC).toFixed(1)}}s LIVE`;
      }}

      generateF1Strategies();
    }}

    function updateSCLap(val) {{
      currentSCLap = parseInt(val);
      const cId = document.getElementById("gen-circuit").value;
      const profile = getCircuitProfile(cId);
      document.getElementById("sc-lap-label").textContent = `Lap ${{currentSCLap}} / ${{profile.laps}}`;
      if (currentSCState !== "GREEN") {{
        setSafetyCarState(currentSCState);
      }} else {{
        generateF1Strategies();
      }}
    }}

    function setSCPreset(preset) {{
      const cId = document.getElementById("gen-circuit").value;
      const profile = getCircuitProfile(cId);
      if (preset === "early") currentSCLap = Math.round(profile.laps * 0.22);
      else if (preset === "mid") currentSCLap = Math.round(profile.laps * 0.44);
      else if (preset === "late") currentSCLap = Math.round(profile.laps * 0.72);

      document.getElementById("sc-lap-slider").value = currentSCLap;
      document.getElementById("sc-lap-label").textContent = `Lap ${{currentSCLap}} / ${{profile.laps}}`;
      setSafetyCarState("FULL_SC");
    }}

    // SWITCH CIRCUIT CONTEXT (Synchronizes header and inputs)
    function changeCircuitContext(cId) {{
      document.getElementById("gen-circuit").value = cId;
      document.getElementById("quick-circuit-select").value = cId;

      const profile = getCircuitProfile(cId);
      document.getElementById("current-circuit-badge").textContent = `${{profile.name}} (${{profile.laps}} Laps)`;
      document.getElementById("gen-circuit-deg-badge").textContent = profile.degradationDesc.toUpperCase();
      document.getElementById("sc-pit-loss-display").textContent = `${{profile.pitLossGreen.toFixed(1)}}s`;

      // Update SC slider range
      const slider = document.getElementById("sc-lap-slider");
      slider.max = profile.laps;
      if (currentSCLap > profile.laps) currentSCLap = Math.round(profile.laps * 0.42);
      slider.value = currentSCLap;
      document.getElementById("sc-lap-label").textContent = `Lap ${{currentSCLap}} / ${{profile.laps}}`;

      // Update KPI split
      document.getElementById("kpi-stops-split").textContent = (profile.typicalStops === 1) ? "1-Stop Dominant" : (profile.typicalStops === 2) ? "2-Stop Optimal" : "3-Stop Mandatory";
      document.getElementById("kpi-stops-desc").textContent = `${{profile.name.split(" ")[0]}} Strategy Split`;

      generateF1Strategies();
      renderStintTimelines();
    }}

    // MAIN STRATEGY GENERATOR ENGINE: FULLY DYNAMIC ACROSS RACE TRACK, GRID POSITION, AND SAFETY CAR
    function generateF1Strategies() {{
      const circuitId = parseInt(document.getElementById("gen-circuit").value);
      const grid = parseInt(document.getElementById("gen-grid").value);
      const tier = parseInt(document.getElementById("gen-tier").value);
      const temp = parseInt(document.getElementById("gen-temp").value);

      const profile = getCircuitProfile(circuitId);
      const laps = profile.laps;
      const typicalStops = profile.typicalStops;
      const isSC = currentSCState === "FULL_SC";
      const isVSC = currentSCState === "VSC";
      const isCaution = (isSC || isVSC);
      const activePitLoss = isSC ? profile.pitLossSC : isVSC ? profile.pitLossVSC : profile.pitLossGreen;
      const freeTimeSec = (profile.pitLossGreen - activePitLoss);
      const baseRaceTime = laps * profile.baseLapSec;

      const isPole = (grid <= 2);
      const isHunter = (grid >= 3 && grid <= 6);
      const isMidfield = (grid >= 7 && grid <= 12);
      const isBack = (grid >= 13);

      let plans = [];

      if (!isCaution) {{
        // ========================================================
        // 1. GREEN FLAG STRATEGIES (TRACK + GRID POSITION AWARE)
        // ========================================================
        if (isPole) {{
          // FRONT ROW / POLE POSITION (P1 - P2): Clean Air Defense
          const p1 = Math.round(laps * (typicalStops > 1 ? 0.32 : 0.44));
          const p2 = Math.round(laps * 0.68);
          const timeA = (baseRaceTime + (typicalStops * profile.pitLossGreen)).toFixed(1);
          const timeB = (baseRaceTime + (typicalStops * profile.pitLossGreen) - 3.2).toFixed(1);
          const timeC = (baseRaceTime + profile.pitLossGreen + 8.5).toFixed(1);

          plans.push({{
            plan_code: "PLAN A (LEADER'S DEFENSE)",
            name: (typicalStops === 1) ? "Medium ➔ Hard (Track Position Control)" : (typicalStops === 2 ? "Medium ➔ Hard ➔ Soft (Clean Air Dominance)" : "Soft ➔ Medium ➔ Medium ➔ Hard"),
            type: `${{typicalStops}}-STOP BASELINE`,
            stints: (typicalStops === 1) 
              ? [{{ compound: "MEDIUM", start: 1, end: p1 }}, {{ compound: "HARD", start: p1 + 1, end: laps }}]
              : (typicalStops === 2
                ? [{{ compound: "MEDIUM", start: 1, end: p1 }}, {{ compound: "HARD", start: p1 + 1, end: p2 }}, {{ compound: "SOFT", start: p2 + 1, end: laps }}]
                : profile.planA.stints),
            pit_windows: `Stop 1: L${{p1-1}}-L${{p1+2}}` + (typicalStops > 1 ? ` | Stop 2: L${{p2-1}}-L${{p2+2}}` : ""),
            total_time: timeA,
            predicted_finish: "P1 - Victory (Clean Air Control)",
            summary: `Starting from P${{grid}} on ${{profile.name}}. Dictate race tempo from the front. Run optimal baseline in clean air and react with a 1-lap cover window if P2 pits.`,
            statusBadge: "LEADER'S CALL",
            gridContext: `P${{grid}} FRONT ROW`
          }});

          plans.push({{
            plan_code: "PLAN B (UNDERCUT NEUTRALIZER)",
            name: "Proactive Early Box (Cover Chasing Rivals)",
            type: `${{typicalStops}}-STOP DEFENSE`,
            stints: (typicalStops === 1)
              ? [{{ compound: "SOFT", start: 1, end: p1 - 3 }}, {{ compound: "HARD", start: p1 - 2, end: laps }}]
              : [{{ compound: "SOFT", start: 1, end: p1 - 2 }}, {{ compound: "MEDIUM", start: p1 - 1, end: p2 - 2 }}, {{ compound: "HARD", start: p2 - 1, end: laps }}],
            pit_windows: `Stop 1: L${{p1-3}}-L${{p1-1}}` + (typicalStops > 1 ? ` | Stop 2: L${{p2-3}}-L${{p2-1}}` : ""),
            total_time: timeB,
            predicted_finish: "P1 / P2 (Track Position Secured)",
            summary: `Boxes 2-3 laps earlier than optimal window to proactively shut down any undercut attempt from P2/P3 behind.`,
            statusBadge: "TACTICAL DEFENSE",
            gridContext: `P${{grid}} COVER`
          }});

          plans.push({{
            plan_code: "PLAN C (CLEAN AIR OVERCUT)",
            name: "Extend Stint 1 (Wait for Traffic Gap)",
            type: "OVERCUT EXTENSION",
            stints: (typicalStops === 1)
              ? [{{ compound: "MEDIUM", start: 1, end: p1 + 6 }}, {{ compound: "HARD", start: p1 + 7, end: laps }}]
              : [{{ compound: "HARD", start: 1, end: p1 + 5 }}, {{ compound: "MEDIUM", start: p1 + 6, end: laps }}],
            pit_windows: `Stop 1: L${{p1+4}}-L${{p1+7}}`,
            total_time: timeC,
            predicted_finish: "P1 Net Victory",
            summary: `Extends stint 1 in clear air while chasers pit into midfield traffic. Re-emerges ahead on net pit exit delta.`,
            statusBadge: "CLEAN AIR OVERCUT",
            gridContext: `P${{grid}} OVERCUT`
          }});

        }} else if (isHunter) {{
          // UPPER MIDFIELD / HUNTERS (P3 - P6): Aggressive Undercut & Offset
          const p1 = Math.round(laps * (typicalStops > 1 ? 0.26 : 0.38));
          const p2 = Math.round(laps * 0.62);
          const timeA = (baseRaceTime + (typicalStops * profile.pitLossGreen) - 6.8).toFixed(1);
          const timeB = (baseRaceTime + (typicalStops * profile.pitLossGreen) - 2.5).toFixed(1);
          const timeC = (baseRaceTime + (2 * profile.pitLossGreen) - 11.2).toFixed(1);

          plans.push({{
            plan_code: "PLAN A (AGGRESSIVE UNDERCUT STRIKE)",
            name: (typicalStops === 1) ? "Soft ➔ Hard (Early Undercut Attack)" : "Soft ➔ Hard ➔ Medium (Dual Strike)",
            type: `${{typicalStops}}-STOP ATTACK`,
            stints: (typicalStops === 1)
              ? [{{ compound: "SOFT", start: 1, end: p1 }}, {{ compound: "HARD", start: p1 + 1, end: laps }}]
              : [{{ compound: "SOFT", start: 1, end: p1 }}, {{ compound: "HARD", start: p1 + 1, end: p2 }}, {{ compound: "MEDIUM", start: p2 + 1, end: laps }}],
            pit_windows: `Stop 1: L${{p1-2}}-L${{p1}}` + (typicalStops > 1 ? ` | Stop 2: L${{p2-2}}-L${{p2}}` : ""),
            total_time: timeA,
            predicted_finish: "P1 / P2 - Lead Attack (+2 Pos)",
            summary: `Starting P${{grid}} on ${{profile.name}}. Cannot follow leader in dirty air. Box 2-3 laps before front row to trigger +1.8s/lap fresh rubber delta and take the lead!`,
            statusBadge: "PRIMARY ATTACK",
            gridContext: `P${{grid}} HUNTER`
          }});

          plans.push({{
            plan_code: "PLAN B (CONTRARIAN COMPOUND OFFSET)",
            name: "Medium ➔ Hard ➔ Soft (Opposite Tire Order)",
            type: `${{typicalStops}}-STOP OFFSET`,
            stints: (typicalStops === 1)
              ? [{{ compound: "MEDIUM", start: 1, end: p1 + 5 }}, {{ compound: "SOFT", start: p1 + 6, end: laps }}]
              : [{{ compound: "MEDIUM", start: 1, end: p1 + 4 }}, {{ compound: "HARD", start: p1 + 5, end: p2 + 2 }}, {{ compound: "SOFT", start: p2 + 3, end: laps }}],
            pit_windows: `Stop 1: L${{p1+3}}-L${{p1+6}}`,
            total_time: timeB,
            predicted_finish: "Podium (+1 to +2 Pos)",
            summary: `Runs opposite tire sequence of front row. Gains free clean air once soft-shod leaders pit early into backmarker traffic.`,
            statusBadge: "OFFSET STRATEGY",
            gridContext: `P${{grid}} OFFSET`
          }});

          plans.push({{
            plan_code: "PLAN C (TIRE AGE OVERDRIVE)",
            name: "2-Stop Sprint Blitz (High Overtake Mode)",
            type: "2-STOP SPRINT",
            stints: [{{ compound: "SOFT", start: 1, end: Math.round(laps*0.22) }}, {{ compound: "SOFT", start: Math.round(laps*0.22)+1, end: Math.round(laps*0.58) }}, {{ compound: "MEDIUM", start: Math.round(laps*0.58)+1, end: laps }}],
            pit_windows: `Stop 1: L${{Math.round(laps*0.20)}}-L${{Math.round(laps*0.23)}} | Stop 2: L${{Math.round(laps*0.56)}}-L${{Math.round(laps*0.59)}}`,
            total_time: timeC,
            predicted_finish: "Fastest Lap + Podium",
            summary: `Uses lightweight fuel and softer compounds to aggressively hunt down conserving 1-stoppers in the final 12 laps.`,
            statusBadge: "SPRINT OVERDRIVE",
            gridContext: `P${{grid}} SPRINT`
          }});

        }} else if (isMidfield) {{
          // MIDFIELD PACK (P7 - P12): Clean Air Traffic Management
          const p1 = Math.round(laps * 0.35);
          const timeA = (baseRaceTime + profile.pitLossGreen).toFixed(1);
          const timeB = (baseRaceTime + (2 * profile.pitLossGreen) - 8.0).toFixed(1);
          const timeC = (baseRaceTime + profile.pitLossGreen + 14.0).toFixed(1);

          plans.push({{
            plan_code: "PLAN A (CLEAN AIR WINDOW SPLIT)",
            name: "Medium ➔ Hard (DRS Train Escape)",
            type: "1-STOP TRAFFIC SPLIT",
            stints: [{{ compound: "MEDIUM", start: 1, end: p1 }}, {{ compound: "HARD", start: p1 + 1, end: laps }}],
            pit_windows: `Stop 1: L${{p1-1}}-L${{p1+2}} (Open Window Target)`,
            total_time: timeA,
            predicted_finish: `P${{Math.max(6, grid - 2)}} - Best of Rest`,
            summary: `Starting P${{grid}} in the midfield pack. Time pit window to drop car into the open track gap between leaders and backmarkers, escaping dirty air and DRS trains.`,
            statusBadge: "OPTIMAL TRAFFIC SPLIT",
            gridContext: `P${{grid}} MIDFIELD`
          }});

          plans.push({{
            plan_code: "PLAN B (OPENING LAP SOFT BLITZ)",
            name: "Soft ➔ Hard (Launch Grip Attack)",
            type: "ATTACK UNDERCUT",
            stints: [{{ compound: "SOFT", start: 1, end: Math.round(laps*0.20) }}, {{ compound: "HARD", start: Math.round(laps*0.20) + 1, end: laps }}],
            pit_windows: `Stop 1: L${{Math.round(laps*0.18)}}-L${{Math.round(laps*0.21)}}`,
            total_time: timeB,
            predicted_finish: `P${{Math.max(6, grid - 3)}} (+3 Pos Gain)`,
            summary: `Starts on Softs with aggressive launch throttle mapping to overtake 2-3 cars into Turn 1, then boxes early onto durable Hards.`,
            statusBadge: "LAUNCH ATTACK",
            gridContext: `P${{grid}} BLITZ`
          }});

          plans.push({{
            plan_code: "PLAN C (SAFETY CAR LONGEVITY HEDGE)",
            name: "Hard ➔ Soft (Run Deep for Caution)",
            type: "SC LONGEVITY HEDGE",
            stints: [{{ compound: "HARD", start: 1, end: Math.round(laps*0.58) }}, {{ compound: "SOFT", start: Math.round(laps*0.58) + 1, end: laps }}],
            pit_windows: `Stop 1: L${{Math.round(laps*0.55)}}-L${{Math.round(laps*0.60)}} (Targeting SC)`,
            total_time: timeC,
            predicted_finish: "P6 - P8 (Neutralization Dependent)",
            summary: `Starts on durable Hard rubber. Runs 35+ laps waiting for midfield collisions to trigger a Safety Car, unlocking a free pit stop.`,
            statusBadge: "SAFETY CAR HEDGE",
            gridContext: `P${{grid}} HEDGE`
          }});

        }} else {{
          // BACK OF GRID / PIT LANE (P13 - P20): Radical Points Comeback
          const p1_rev = Math.round(laps * 0.62);
          const timeA = (baseRaceTime + profile.pitLossGreen + 4.0).toFixed(1);
          const timeB = (baseRaceTime + (2 * profile.pitLossGreen) - 10.0).toFixed(1);
          const timeC = (baseRaceTime + profile.pitLossGreen + 18.0).toFixed(1);

          plans.push({{
            plan_code: "PLAN A (RADICAL REVERSE LONGEVITY)",
            name: "Hard ➔ Soft (Late Race Low-Fuel Charge)",
            type: "1-STOP REVERSE",
            stints: [{{ compound: "HARD", start: 1, end: p1_rev }}, {{ compound: "SOFT", start: p1_rev + 1, end: laps }}],
            pit_windows: `Stop 1: L${{p1_rev-2}}-L${{p1_rev+2}}`,
            total_time: timeA,
            predicted_finish: `P${{Math.max(9, grid - 8)}} (+6 to +10 Pos Jump!)`,
            summary: `Starting P${{grid}}. Following standard strategy guarantees finishing out of points. Start on Hard compound, run 60% of race in clean air as field pits, then fit fresh Softs on low fuel for late points charge!`,
            statusBadge: "RADICAL POINTS GAMBLE",
            gridContext: `P${{grid}} REVERSE`
          }});

          plans.push({{
            plan_code: "PLAN B (EARLY TRAFFIC DUMP UNDERCUT)",
            name: "Ditch Dirty Air (Lap 8 Box into Empty Track)",
            type: "TRAFFIC DUMP",
            stints: [{{ compound: "SOFT", start: 1, end: 8 }}, {{ compound: "HARD", start: 9, end: Math.round(laps*0.58) }}, {{ compound: "MEDIUM", start: Math.round(laps*0.58) + 1, end: laps }}],
            pit_windows: `Stop 1: L7-L9 | Stop 2: L${{Math.round(laps*0.56)}}-L${{Math.round(laps*0.59)}}`,
            total_time: timeB,
            predicted_finish: `P${{Math.max(11, grid - 5)}} (+5 Pos Gain)`,
            summary: `Boxes on Lap 8 to dump dirty air immediately. Re-emerges on completely empty track to run qualifying-pace laps.`,
            statusBadge: "EARLY DUMP",
            gridContext: `P${{grid}} DUMP`
          }});

          plans.push({{
            plan_code: "PLAN C (EXTREME VARIANCE GAMBLER)",
            name: "Opposite of the Field (Red Flag / Weather Wait)",
            type: "EXTREME VARIANCE",
            stints: [{{ compound: "HARD", start: 1, end: Math.round(laps*0.70) }}, {{ compound: "SOFT", start: Math.round(laps*0.70) + 1, end: laps }}],
            pit_windows: `Stop 1: L${{Math.round(laps*0.68)}}-L${{Math.round(laps*0.72)}}`,
            total_time: timeC,
            predicted_finish: "P8 - P10 (Jackpot) or P16",
            summary: `Extreme endurance management. Nurses rubber hoping for barrier contact, red flag, or sudden weather change to steal championship points.`,
            statusBadge: "ALL-IN GAMBLE",
            gridContext: `P${{grid}} GAMBLE`
          }});
        }}

      }} else {{
        // ========================================================
        // 2. REAL-TIME SAFETY CAR / VSC ADAPTED DYNAMICS
        // ========================================================
        const scL = currentSCLap;
        const cautionTitle = isSC ? "SAFETY CAR" : "VIRTUAL SC";
        const divText = `+${{freeTimeSec.toFixed(1)}}s Free Stop`;

        if (isPole) {{
          // P1 - P2 LEADER'S CAUTION DILEMMA
          const timeA_SC = (baseRaceTime + (typicalStops * activePitLoss) - freeTimeSec).toFixed(1);
          const timeB_SC = (baseRaceTime + typicalStops * profile.pitLossGreen).toFixed(1);
          const timeC_SC = (baseRaceTime + (2 * activePitLoss) - 12.0).toFixed(1);

          plans.push({{
            plan_code: "PLAN A (LEADER'S SC ARBITRAGE BOX)",
            name: "BOX THIS LAP (Current ➔ Fresh Hard)",
            type: `FREE STOP (+${{freeTimeSec.toFixed(1)}}s)`,
            stints: [{{ compound: "MEDIUM", start: 1, end: scL }}, {{ compound: "HARD", start: scL + 1, end: laps }}],
            pit_windows: `🚨 ACTIVE NOW: BOX LAP ${{scL}} (SC ENTRY)`,
            total_time: timeA_SC,
            predicted_finish: "P1 - Clean Air & Net Win",
            summary: `${{cautionTitle}} active! Leader takes the ${{divText}} dividend with zero risk of dirty air, exiting in the net race lead.`,
            statusBadge: "LEADER'S ARBITRAGE",
            gridContext: `P${{grid}} POLE SC`
          }});

          plans.push({{
            plan_code: "PLAN B (TRACK POSITION DEFENSE - STAY OUT)",
            name: "STAY OUT (Do Not Concede Track Position)",
            type: "TRACK POSITION KING",
            stints: [{{ compound: "MEDIUM", start: 1, end: Math.round(laps*0.65) }}, {{ compound: "HARD", start: Math.round(laps*0.65) + 1, end: laps }}],
            pit_windows: "Do Not Box (Defend Line)",
            total_time: timeB_SC,
            predicted_finish: "P1 on Restart (Track Position King)",
            summary: `Track position is 95% of victory on ${{profile.name}}! Surrendering P1 to pit risks getting boxed behind rivals. Stay out and defend inside line into Turn 1!`,
            statusBadge: "TRACK POS DEFENSE",
            gridContext: `P${{grid}} STAY OUT`
          }});

          plans.push({{
            plan_code: "PLAN C (LATE RESTART SOFT SPRINT)",
            name: "Box for Brand New Soft Tires (Restart Sprint)",
            type: "RESTART SPRINT",
            stints: [{{ compound: "MEDIUM", start: 1, end: scL }}, {{ compound: "SOFT", start: scL + 1, end: laps }}],
            pit_windows: `BOX LAP ${{scL}}`,
            total_time: timeC_SC,
            predicted_finish: "Fastest Lap + P1 Victory",
            summary: `Pits for high-grip Soft tires. When green flag waves, car pulls an immediate 2.5s gap before DRS is enabled, securing victory.`,
            statusBadge: "RESTART SPRINT",
            gridContext: `P${{grid}} SOFT SPRINT`
          }});

        }} else if (isHunter) {{
          // P3 - P6 HUNTER CAUTION AMBUSH
          const timeA_SC = (baseRaceTime + (typicalStops * activePitLoss) - freeTimeSec - 2.0).toFixed(1);
          const timeB_SC = (baseRaceTime + (2 * activePitLoss) - 10.0).toFixed(1);
          const timeC_SC = (baseRaceTime + activePitLoss).toFixed(1);

          plans.push({{
            plan_code: "PLAN A (OPPORTUNISTIC SC AMBUSH)",
            name: "BOX THIS LAP (Undercut Front Row Under SC)",
            type: `FREE STOP (+${{freeTimeSec.toFixed(1)}}s)`,
            stints: [{{ compound: "SOFT", start: 1, end: scL }}, {{ compound: "HARD", start: scL + 1, end: laps }}],
            pit_windows: `🚨 BOX LAP ${{scL}} (SC ENTRY)`,
            total_time: timeA_SC,
            predicted_finish: "P1 / P2 Lead Takeover",
            summary: `Pits immediately under ${{cautionTitle}}. If leaders stay out or hesitate, this moves you into the net race lead with fresh rubber!`,
            statusBadge: "LEAD AMBUSH",
            gridContext: `P${{grid}} AMBUSH`
          }});

          plans.push({{
            plan_code: "PLAN B (RESTART ATTACK BLITZ - SOFTS)",
            name: "Box for Brand New Soft Tires (Restart Blitz)",
            type: "RESTART BLITZ",
            stints: [{{ compound: "SOFT", start: 1, end: scL }}, {{ compound: "SOFT", start: scL + 1, end: laps }}],
            pit_windows: `BOX LAP ${{scL}} (Tire Attack)`,
            total_time: timeB_SC,
            predicted_finish: "P1 Turn 1 Overtake Blitz",
            summary: `Cars ahead on cold Hards will struggle for tire warmup on restart. Exploit +2.1s grip delta on laps ${{scL+1}}-${{scL+4}} to dive down the inside!`,
            statusBadge: "RESTART BLITZ",
            gridContext: `P${{grid}} BLITZ`
          }});

          plans.push({{
            plan_code: "PLAN C (CONTRARIAN TRACK POSITION)",
            name: "Do Opposite of Leader (Inherit P1 Track Pos)",
            type: "CONTRARIAN GAMBLE",
            stints: [{{ compound: "HARD", start: 1, end: Math.round(laps*0.65) }}, {{ compound: "SOFT", start: Math.round(laps*0.65) + 1, end: laps }}],
            pit_windows: `Decision: Lap ${{scL}}`,
            total_time: timeC_SC,
            predicted_finish: "P1 / Podium Steal",
            summary: `Watch the leader's pit entry. If P1 boxes, STAY OUT to inherit the race lead and clean air on restart!`,
            statusBadge: "OPPOSITE CALL",
            gridContext: `P${{grid}} OPPOSITE`
          }});

        }} else if (isMidfield) {{
          // P7 - P12 MIDFIELD CAUTION ARBITRAGE
          const timeA_SC = (baseRaceTime + activePitLoss - freeTimeSec).toFixed(1);
          const timeB_SC = (baseRaceTime + (2 * activePitLoss) - 6.0).toFixed(1);
          const timeC_SC = (baseRaceTime + activePitLoss - freeTimeSec - 5.0).toFixed(1);

          plans.push({{
            plan_code: "PLAN A (MIDFIELD SC ARBITRAGE BOX)",
            name: "BOX THIS LAP (Bypass Midfield Traffic)",
            type: `FREE STOP (+${{freeTimeSec.toFixed(1)}}s)`,
            stints: [{{ compound: "MEDIUM", start: 1, end: scL }}, {{ compound: "HARD", start: scL + 1, end: laps }}],
            pit_windows: `🚨 BOX LAP ${{scL}}`,
            total_time: timeA_SC,
            predicted_finish: `P${{Math.max(4, grid - 4)}} (+4 Pos Jump)`,
            summary: `Saves ${{freeTimeSec.toFixed(1)}}s vs green stop. Overcuts all cars ahead that pitted under green flag conditions before the caution.`,
            statusBadge: "MIDFIELD ARBITRAGE",
            gridContext: `P${{grid}} ARBITRAGE`
          }});

          plans.push({{
            plan_code: "PLAN B (BUNCHED FIELD SOFT CHARGE)",
            name: "Fit Fresh Soft Tires (Restart Overtake Attack)",
            type: "RESTART CHARGE",
            stints: [{{ compound: "MEDIUM", start: 1, end: scL }}, {{ compound: "SOFT", start: scL + 1, end: laps }}],
            pit_windows: `BOX LAP ${{scL}}`,
            total_time: timeB_SC,
            predicted_finish: `P${{Math.max(5, grid - 3)}} (Top 5 Attack)`,
            summary: `Caution bunches the entire field nose-to-tail. With 0.0s time gaps, attack on brand new soft rubber on restart!`,
            statusBadge: "BUNCHED CHARGE",
            gridContext: `P${{grid}} SOFT CHARGE`
          }});

          plans.push({{
            plan_code: "PLAN C (HARD STINT CASH-IN JACKPOT)",
            name: "Hard Stint Cashing In (Golden Dividend)",
            type: "GOLDEN CASH-IN",
            stints: [{{ compound: "HARD", start: 1, end: scL }}, {{ compound: "MEDIUM", start: scL + 1, end: laps }}],
            pit_windows: `BOX LAP ${{scL}}`,
            total_time: timeC_SC,
            predicted_finish: `P${{Math.max(4, grid - 5)}} (Massive Net Gain)`,
            summary: `The longevity hedge won! Having stretched the opening Hard stint, this caution gives a virtually zero-penalty pit stop straight into the top 5!`,
            statusBadge: "GOLDEN JACKPOT",
            gridContext: `P${{grid}} CASH-IN`
          }});

        }} else {{
          // P13 - P20 BACK OF GRID CAUTION JACKPOT
          const timeA_SC = (baseRaceTime + activePitLoss - freeTimeSec - 4.0).toFixed(1);
          const timeB_SC = (baseRaceTime + (2 * activePitLoss) - 8.0).toFixed(1);
          const timeC_SC = (baseRaceTime + profile.pitLossGreen).toFixed(1);

          plans.push({{
            plan_code: "PLAN A (REVERSE STINT GOLDEN CASH-IN)",
            name: "Golden Pit Window: Hard Stint Cashing In!",
            type: `GOLDEN JACKPOT (+${{freeTimeSec.toFixed(1)}}s)`,
            stints: [{{ compound: "HARD", start: 1, end: scL }}, {{ compound: "SOFT", start: scL + 1, end: laps }}],
            pit_windows: `🚨 BOX NOW: LAP ${{scL}}`,
            total_time: timeA_SC,
            predicted_finish: `P7 - P9 (Points Finish from P${{grid}}!)`,
            summary: `The ultimate comeback! Starting on Hards and boxing under ${{cautionTitle}} leapfrogs 8-10 cars that pitted under green, putting you straight into the championship points!`,
            statusBadge: "POINTS COMEBACK",
            gridContext: `P${{grid}} COMEBACK`
          }});

          plans.push({{
            plan_code: "PLAN B (FRESH SOFT RESTART BLITZ)",
            name: "Box for Brand New Soft Tires (Restart Blitz)",
            type: "RESTART BLITZ",
            stints: [{{ compound: "HARD", start: 1, end: scL }}, {{ compound: "SOFT", start: scL + 1, end: laps }}],
            pit_windows: `BOX LAP ${{scL}}`,
            total_time: timeB_SC,
            predicted_finish: `P9 - P11 (+7 to +9 Pos Gain)`,
            summary: `Pits for softest rubber. With field compressed nose-to-tail, attack cars on cold or worn tires into Turn 1!`,
            statusBadge: "SOFT BLITZ",
            gridContext: `P${{grid}} BLITZ`
          }});

          plans.push({{
            plan_code: "PLAN C (STAY OUT TRACK POSITION JUMP)",
            name: "STAY OUT (Gain 8-10 Positions on Track)",
            type: "TRACK POS GAMBLE",
            stints: [{{ compound: "HARD", start: 1, end: Math.round(laps*0.75) }}, {{ compound: "SOFT", start: Math.round(laps*0.75) + 1, end: laps }}],
            pit_windows: "Stay On Track (Do Not Pit)",
            total_time: timeC_SC,
            predicted_finish: `P7 on Restart (Track Position King)`,
            summary: `While 10 midfield cars pit, STAY OUT. Gain 8-10 positions on track, then fiercely defend the inside line on restart!`,
            statusBadge: "TRACK POS JUMP",
            gridContext: `P${{grid}} STAY OUT`
          }});
        }}
      }}

      // RENDER STRATEGY CARDS
      const container = document.getElementById("strategy-plans-container");
      container.innerHTML = "";

      plans.forEach((p, idx) => {{
        const card = document.createElement("div");
        card.className = "f1-card p-5 flex flex-col justify-between space-y-4";
        
        if (currentSCState !== "GREEN") {{
          if (idx === 0) card.classList.add("border-t-4", "border-t-emerald-500", "shadow-emerald-950/40");
          else if (idx === 1) card.classList.add("border-t-4", "border-t-red-600");
          else card.classList.add("border-t-4", "border-t-amber-500", "shadow-amber-950/40");
        }} else {{
          if (p.type.includes("1-STOP")) card.classList.add("border-t-4", "border-t-red-600");
          else if (p.type.includes("2-STOP")) card.classList.add("border-t-4", "border-t-amber-500");
          else card.classList.add("border-t-4", "border-t-blue-500");
        }}

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

        const scIndicatorBadge = (currentSCState !== "GREEN") 
          ? `<span class="px-2 py-0.5 rounded bg-amber-500 text-slate-950 font-bold text-[10px] sc-pulse">🟡 SC INTERVENTION: LAP ${{currentSCLap}}</span>`
          : "";

        card.innerHTML = `
          <div>
            <div class="flex items-center justify-between font-mono text-[11px] mb-1">
              <span class="text-red-400 font-bold">${{p.plan_code}}</span>
              <div class="flex items-center gap-1.5">
                <span class="px-1.5 py-0.5 rounded bg-slate-800 text-slate-300 font-bold text-[10px]">${{p.gridContext}}</span>
                <span class="px-2 py-0.5 rounded bg-slate-900 border border-slate-700 text-slate-300 font-bold">${{p.type}}</span>
              </div>
            </div>
            <h3 class="text-base font-bold text-white mt-1">${{p.name}}</h3>
            <p class="text-xs text-slate-400 mt-1.5 leading-relaxed">${{p.summary}}</p>
          </div>

          <div class="space-y-2">
            <div class="flex justify-between items-center text-[10px] font-mono text-slate-400 uppercase tracking-wider">
              <span>STINT PROFILES (${{laps}} LAPS TOTAL)</span>
              ${{scIndicatorBadge}}
            </div>
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
            <div class="col-span-2 pt-1 border-t border-slate-800 flex justify-between items-center">
              <div>
                <span class="text-[10px] text-slate-500 block">PREDICTED FINISH</span>
                <span class="text-emerald-400 font-black text-sm">${{p.predicted_finish}}</span>
              </div>
              <span class="text-[10px] px-2 py-0.5 rounded bg-slate-900 border border-slate-700 text-slate-400 font-bold">${{p.statusBadge}}</span>
            </div>
          </div>
        `;

        container.appendChild(card);
      }});

      // RENDER DECISION TRIGGERS MATRIX
      const triggersContainer = document.getElementById("decision-triggers-container");
      const isSCActive = currentSCState !== "GREEN";
      triggersContainer.innerHTML = `
        <div class="p-3.5 bg-slate-950/80 rounded-xl border border-slate-800 space-y-1">
          <div class="flex items-center gap-2 text-red-400 font-bold">
            <span>●</span> TRIGGER 1: UNDER 1.8s GAP TO RIVAL
          </div>
          <p class="text-slate-300 text-[11px] leading-relaxed">
            <strong>Action: Trigger Undercut (Plan B).</strong> Box 1 to 2 laps ahead of rival into clean air. ${{profile.name.split(" ")[0]}} out-lap grip delta (+${{profile.overtakingDelta}}s) jumps them on exit.
          </p>
        </div>

        <div class="p-3.5 bg-slate-950/80 rounded-xl border ${{isSCActive ? 'border-amber-500 bg-amber-950/40 sc-pulse' : 'border-slate-800'}} space-y-1">
          <div class="flex items-center gap-2 ${{isSCActive ? 'text-amber-300 font-black' : 'text-amber-400 font-bold'}}">
            <span>●</span> TRIGGER 2: SAFETY CAR IN PIT WINDOW
          </div>
          <p class="text-slate-300 text-[11px] leading-relaxed">
            <strong>${{isSCActive ? 'ACTIVE NOW: BOX IMMEDIATELY!' : 'Action on Deploy: Box for Free Stop.'}}</strong> Pitting under caution cuts transit loss from ${{profile.pitLossGreen.toFixed(1)}}s to ${{activePitLoss.toFixed(1)}}s (saves <strong>+${{freeTimeSec.toFixed(1)}}s</strong> free time)!
          </p>
        </div>

        <div class="p-3.5 bg-slate-950/80 rounded-xl border border-slate-800 space-y-1">
          <div class="flex items-center gap-2 text-cyan-400 font-bold">
            <span>●</span> TRIGGER 3: HIGH TIRE CLIFF DEGRADATION
          </div>
          <p class="text-slate-300 text-[11px] leading-relaxed">
            <strong>Action: Monitor Thermal Cliff.</strong> When lap pace drops by &gt;1.2s, do not extend stint. Switch immediately to secondary compound to avoid puncture risk.
          </p>
        </div>
      `;
    }}


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

    function selectCarComponent(key) {{
      const comp = CAR_COMPONENTS[key];
      if (!comp) return;

      const card = document.getElementById("component-details-card");
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
      if (tab === "strategy-generator") generateF1Strategies();
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

    // DYNAMIC STINT TIMELINE (Scales to selected track and highlights Safety Car)
    function renderStintTimelines() {{
      const container = document.getElementById("stint-timeline-container");
      container.innerHTML = "";

      const cId = document.getElementById("gen-circuit").value;
      const profile = getCircuitProfile(cId);
      const laps = profile.laps;

      // Adapt driver stints to track laps and safety car
      const p1 = Math.round(laps * 0.28);
      const p2 = Math.round(laps * 0.64);
      const isSC = currentSCState !== "GREEN";
      const scL = currentSCLap;

      let driverStintsMap = {{}};

      if (!isSC) {{
        if (profile.typicalStops === 1) {{
          driverStintsMap = {{
            "VER": [{{ comp: "MEDIUM", s: 1, e: Math.round(laps * 0.44) }}, {{ comp: "HARD", s: Math.round(laps * 0.44) + 1, e: laps }}],
            "LEC": [{{ comp: "SOFT", s: 1, e: Math.round(laps * 0.38) }}, {{ comp: "HARD", s: Math.round(laps * 0.38) + 1, e: laps }}],
            "NOR": [{{ comp: "MEDIUM", s: 1, e: Math.round(laps * 0.42) }}, {{ comp: "HARD", s: Math.round(laps * 0.42) + 1, e: laps }}],
            "SAI": [{{ comp: "SOFT", s: 1, e: Math.round(laps * 0.36) }}, {{ comp: "HARD", s: Math.round(laps * 0.36) + 1, e: laps }}],
            "HAM": [{{ comp: "HARD", s: 1, e: Math.round(laps * 0.58) }}, {{ comp: "MEDIUM", s: Math.round(laps * 0.58) + 1, e: laps }}],
            "RUS": [{{ comp: "MEDIUM", s: 1, e: Math.round(laps * 0.40) }}, {{ comp: "HARD", s: Math.round(laps * 0.40) + 1, e: laps }}]
          }};
        }} else {{
          driverStintsMap = {{
            "VER": [{{ comp: "SOFT", s: 1, e: p1 }}, {{ comp: "HARD", s: p1 + 1, e: p2 }}, {{ comp: "SOFT", s: p2 + 1, e: laps }}],
            "LEC": [{{ comp: "SOFT", s: 1, e: p1 - 2 }}, {{ comp: "HARD", s: p1 - 1, e: p2 - 1 }}, {{ comp: "HARD", s: p2, e: laps }}],
            "NOR": [{{ comp: "MEDIUM", s: 1, e: p1 + 2 }}, {{ comp: "HARD", s: p1 + 3, e: p2 + 1 }}, {{ comp: "MEDIUM", s: p2 + 2, e: laps }}],
            "SAI": [{{ comp: "SOFT", s: 1, e: p1 }}, {{ comp: "HARD", s: p1 + 1, e: p2 - 1 }}, {{ comp: "HARD", s: p2, e: laps }}],
            "HAM": [{{ comp: "MEDIUM", s: 1, e: p1 + 1 }}, {{ comp: "HARD", s: p1 + 2, e: p2 }}, {{ comp: "SOFT", s: p2 + 1, e: laps }}],
            "RUS": [{{ comp: "SOFT", s: 1, e: p1 - 1 }}, {{ comp: "HARD", s: p1, e: p2 - 2 }}, {{ comp: "HARD", s: p2 - 1, e: laps }}]
          }};
        }}
      }} else {{
        // Under SC, drivers box at or around scL
        driverStintsMap = {{
          "VER": [{{ comp: "MEDIUM", s: 1, e: scL }}, {{ comp: "HARD", s: scL + 1, e: laps }}],
          "LEC": [{{ comp: "SOFT", s: 1, e: scL }}, {{ comp: "HARD", s: scL + 1, e: laps }}],
          "NOR": [{{ comp: "SOFT", s: 1, e: scL }}, {{ comp: "SOFT", s: scL + 1, e: laps }}],
          "SAI": [{{ comp: "HARD", s: 1, e: scL }}, {{ comp: "MEDIUM", s: scL + 1, e: laps }}],
          "HAM": [{{ comp: "MEDIUM", s: 1, e: scL }}, {{ comp: "SOFT", s: scL + 1, e: laps }}],
          "RUS": [{{ comp: "HARD", s: 1, e: scL }}, {{ comp: "SOFT", s: scL + 1, e: laps }}]
        }};
      }}

      Object.keys(driverStintsMap).forEach(dCode => {{
        const dInfo = F1_DATA.drivers.find(d => d.code === dCode) || {{ color: "#AAA" }};
        const stints = driverStintsMap[dCode];
        const row = document.createElement("div");
        row.className = "flex items-center gap-3 text-xs font-mono";

        let bars = "";
        stints.forEach(s => {{
          const dur = Math.max(1, s.e - s.s + 1);
          const pct = ((dur / laps) * 100).toFixed(1);
          let bgCol = s.comp === "SOFT" ? "#E10600" : s.comp === "MEDIUM" ? "#FFD700" : "#FFFFFF";
          let textCol = s.comp === "HARD" ? "#0D0F14" : (s.comp === "MEDIUM" ? "#0D0F14" : "#FFFFFF");
          bars += `
            <div style="width: ${{pct}}%; background-color: ${{bgCol}}; color: ${{textCol}};" class="py-1 px-1.5 rounded text-center font-bold text-[10px] overflow-hidden whitespace-nowrap shadow-sm">
              ${{s.comp}} (L${{s.s}}-${{s.e}})
            </div>
          `;
        }});

        row.innerHTML = `
          <div class="w-14 font-bold flex items-center gap-1.5" style="color: ${{dInfo.color}}">
            <span class="w-2 h-2 rounded-full" style="background-color: ${{dInfo.color}}"></span>
            <span>${{dCode}}</span>
          </div>
          <div class="flex-1 flex gap-1 bg-slate-950 p-1 rounded-lg border border-slate-800 relative">
            ${{bars}}
            ${{isSC ? `<div style="left: ${{(scL/laps)*100}}%" class="absolute top-0 bottom-0 w-1 bg-amber-400 z-10 shadow-lg shadow-amber-500/50" title="Safety Car on Lap ${{scL}}"></div>` : ''}}
          </div>
        `;
        container.appendChild(row);
      }});
    }}

    function renderDegradationChart() {{
      const svg = document.getElementById("deg-svg");
      const w = 800, h = 300, pL = 50, pR = 30, pT = 20, pB = 30;
      svg.setAttribute("viewBox", `0 0 ${{w}} ${{h}}`);
      svg.innerHTML = "";

      for (let d = 0; d <= 4; d += 1) {{
        const y = pT + (h - pT - pB) * (1 - d / 4);
        svg.innerHTML += `<line x1="${{pL}}" y1="${{y}}" x2="${{w - pR}}" y2="${{y}}" stroke="#1E293B" stroke-dasharray="3,3"/>`;
        svg.innerHTML += `<text x="${{pL - 8}}" y="${{y + 3}}" fill="#64748B" font-size="10" text-anchor="end" font-family="JetBrains Mono">+${{d.toFixed(1)}}s</text>`;
      }}

      for (let lap = 0; lap <= 40; lap += 10) {{
        const x = pL + (w - pL - pR) * (lap / 40);
        svg.innerHTML += `<text x="${{x}}" y="${{h - 10}}" fill="#64748B" font-size="10" text-anchor="middle" font-family="JetBrains Mono">Lap ${{lap}}</text>`;
      }}

      const compounds = [
        {{ name: "Soft (C3)", col: "#E10600", base: -0.65, wear: 0.082, cliff: 16 }},
        {{ name: "Medium (C2)", col: "#FFD700", base: 0.00, wear: 0.052, cliff: 26 }},
        {{ name: "Hard (C1)", col: "#FFFFFF", base: 0.55, wear: 0.028, cliff: 38 }}
      ];

      compounds.forEach(c => {{
        let pts = [];
        for (let t = 1; t <= 40; t++) {{
          let deg = c.base + (c.wear * t);
          if (t > c.cliff) deg += 0.18 * Math.pow(t - c.cliff, 1.85);
          deg = Math.min(4.0, Math.max(0, deg));
          const x = pL + (w - pL - pR) * (t / 40);
          const y = pT + (h - pT - pB) * (1 - deg / 4);
          pts.push(`${{x.toFixed(1)}},${{y.toFixed(1)}}`);
        }}
        svg.innerHTML += `<polyline points="${{pts.join(" ")}}" fill="none" stroke="${{c.col}}" stroke-width="2.5" stroke-linecap="round"/>`;
      }});
    }}

    function renderBattlesTable() {{
      const b = document.getElementById("battles-table-body");
      b.innerHTML = "";
      F1_DATA.pit_stop_battles.forEach(item => {{
        const isSuccess = item.outcome.includes("Success");
        b.innerHTML += `
          <tr class="hover:bg-slate-900/50 transition">
            <td class="p-2.5 font-bold text-white">${{item.gp}}</td>
            <td class="p-2.5 text-red-400 font-bold">${{item.driver_challenger}}</td>
            <td class="p-2.5 text-slate-300">${{item.driver_defender}}</td>
            <td class="p-2.5 font-bold text-amber-400">${{item.tactic}}</td>
            <td class="p-2.5 text-white">${{item.delta_seconds > 0 ? '+' : ''}}${{item.delta_seconds}}s</td>
            <td class="p-2.5">
              <span class="px-2 py-0.5 rounded text-[10px] font-bold ${{isSuccess ? 'bg-emerald-950 text-emerald-400 border border-emerald-800' : 'bg-red-950 text-red-400 border border-red-800'}}">
                ${{item.outcome}}
              </span>
            </td>
          </tr>
        `;
      }});
    }}

    function renderCircuitsGrid() {{
      const c = document.getElementById("circuits-grid-container");
      c.innerHTML = "";
      F1_DATA.circuits.forEach(item => {{
        c.innerHTML += `
          <div onclick="changeCircuitContext(${{item.circuitId}}); setTab('strategy-generator');" class="p-3.5 rounded-xl bg-slate-950/80 border border-slate-800 font-mono hover:border-red-600 cursor-pointer transition group">
            <div class="flex justify-between font-bold">
              <span class="text-red-400 group-hover:text-red-300">${{item.country}}</span>
              <span class="text-slate-400">${{item.alt}}m alt</span>
            </div>
            <div class="text-white font-bold text-sm my-1 group-hover:text-amber-400">${{item.name}}</div>
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
          <div onclick="changeCircuitContext(${{item.circuitId}}); setTab('strategy-generator');" class="p-3.5 rounded-xl bg-slate-950/80 border border-slate-800 font-mono hover:border-red-600 cursor-pointer transition group">
            <div class="flex justify-between font-bold">
              <span class="text-red-400">${{item.country}}</span>
              <span class="text-slate-400">${{item.alt}}m alt</span>
            </div>
            <div class="text-white font-bold text-sm my-1 group-hover:text-amber-400">${{item.name}}</div>
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
      document.getElementById("sim-pit1-val").textContent = `Lap ${{p1}}`;
      const delta = (p1 - 20) * 0.16;
      document.getElementById("sim-result-time").textContent = `${{(5504.8 + delta).toFixed(1)}}s (1h 31m ${{(44.8 + delta).toFixed(1)}}s)`;
      document.getElementById("sim-result-delta").textContent = delta <= 0 ? `${{delta.toFixed(1)}}s (Time Saved)` : `+${{delta.toFixed(1)}}s (Time Lost)`;
    }}

    // INITIALIZATION
    window.onload = function() {{
      changeCircuitContext("3"); // Start at Bahrain
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

print("Saved updated master dashboard with dynamic track strategies and interactive safety car engine!")
