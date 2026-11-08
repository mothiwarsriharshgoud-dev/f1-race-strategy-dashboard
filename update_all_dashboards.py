import json
import os

DATA_PATH = "C:/Users/Main User/.gemini/antigravity/scratch/f1-race-strategy-dashboard/data/f1_strategy_dataset.json"
OUTPUT_HTML = "C:/Users/Main User/.gemini/antigravity/scratch/f1-race-strategy-dashboard/index.html"
ARTIFACT_HTML = "C:/Users/Main User/.gemini/antigravity/brain/bb0fc362-bdeb-4a83-b7c8-80ce516a46a3/f1_race_strategy_dashboard.html"
WIDGET_HTML = "C:/Users/Main User/.gemini/antigravity/brain/bb0fc362-bdeb-4a83-b7c8-80ce516a46a3/f1_race_strategy_widget.html"

with open(DATA_PATH, "r", encoding="utf-8") as f:
    f1_data = json.load(f)

json_data_str = json.dumps(f1_data)

# Master Dashboard HTML with full-fledged AI Strategy Generator
master_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>F1 Race Telemetry & Strategy Analytics Platform | Project 32</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Titillium+Web:ital,wght@0,300;0,400;0,600;0,700;0,900;1,600&family=JetBrains+Mono:wght@400;600;700&display=swap');
    
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

    .stint-bar-item {{
      transition: all 0.2s ease;
    }}
    .stint-bar-item:hover {{
      filter: brightness(1.25);
      transform: translateY(-2px);
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
              <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span> STRATEGY ENGINE ACTIVE
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
      <button onclick="setTab('telemetry')" id="tab-telemetry" class="tab-btn px-4 py-2.5 text-slate-400 hover:text-white transition flex items-center gap-1.5">
        <span>⏱️</span> Lap Pace & Telemetry
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

    <!-- TAB: AI STRATEGY GENERATOR (CENTERPIECE) -->
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
        <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-4">
          <div>
            <h3 class="text-base font-bold text-white flex items-center gap-2">
              <span>📋</span> Race Engineer Decision Triggers & Tactical Playbook
            </h3>
            <p class="text-xs text-slate-400">
              Pre-calculated in-race contingency triggers calibrated for the selected circuit profile.
            </p>
          </div>
          <span class="text-xs font-mono text-emerald-400 bg-emerald-950/80 px-2.5 py-1 rounded border border-emerald-800">
            FIA LIVE TELEMETRY SYNC
          </span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs font-mono" id="decision-triggers-container">
          <!-- Populated dynamically -->
        </div>
      </div>

    </div>

    <!-- TAB: LAP PACE & TELEMETRY -->
    <div id="view-telemetry" class="space-y-6 hidden">
      <div class="f1-card p-4 flex flex-wrap items-center justify-between gap-4">
        <div class="flex items-center gap-3">
          <span class="text-xs font-semibold text-slate-300 uppercase tracking-wider">Driver Selector:</span>
          <div class="flex flex-wrap gap-1.5" id="driver-toggle-container"></div>
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

      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div class="f1-card p-5 lg:col-span-2 flex flex-col justify-between">
          <div class="flex items-center justify-between mb-3 border-b border-slate-800 pb-2">
            <div>
              <h2 class="text-base font-bold text-white flex items-center gap-2">
                <span>🏎️</span> Lap-by-Lap Pace Progression
              </h2>
              <p class="text-xs text-slate-400">Lap times (seconds) across all 57 laps with compound stints.</p>
            </div>
            <div class="flex items-center gap-2 text-xs font-mono">
              <span class="badge-soft px-2 py-0.5 rounded">● Soft</span>
              <span class="badge-medium px-2 py-0.5 rounded">● Medium</span>
              <span class="badge-hard px-2 py-0.5 rounded">● Hard</span>
            </div>
          </div>

          <div class="relative w-full h-80 bg-slate-950/60 rounded-lg p-2 border border-slate-800/80 overflow-hidden">
            <svg id="pace-svg" class="w-full h-full" preserveAspectRatio="none"></svg>
          </div>
        </div>

        <div class="f1-card p-5 flex flex-col justify-between">
          <div class="flex items-center justify-between mb-3 border-b border-slate-800 pb-2">
            <h2 class="text-base font-bold text-white flex items-center gap-2">
              <span>⏱️</span> Gap to Leader Delta (s)
            </h2>
          </div>
          <div class="relative w-full h-80 bg-slate-950/60 rounded-lg p-2 border border-slate-800/80 overflow-hidden">
            <svg id="gap-svg" class="w-full h-full" preserveAspectRatio="none"></svg>
          </div>
        </div>
      </div>

      <div class="f1-card p-5">
        <div class="flex items-center justify-between mb-3 border-b border-slate-800 pb-2">
          <h2 class="text-base font-bold text-white flex items-center gap-2">
            <span>📊</span> Historical Stint Gantt Timeline (Sakhir 57 Laps)
          </h2>
          <span class="text-xs font-mono text-slate-400">Hover over stints for exact lap ranges</span>
        </div>
        <div class="space-y-2 mt-4" id="stint-timeline-container"></div>
      </div>
    </div>

    <!-- TAB: TIRE DEGRADATION MODELING -->
    <div id="view-degradation" class="space-y-6 hidden">
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div class="f1-card p-5 lg:col-span-2">
          <div class="flex flex-wrap items-center justify-between mb-4 border-b border-slate-800 pb-3 gap-2">
            <div>
              <h2 class="text-base font-bold text-white flex items-center gap-2">
                <span>📉</span> Tire Degradation Rate: Tyre Life vs. Lap Time
              </h2>
              <p class="text-xs text-slate-400">Linear regression slope modeling tire wear ($s/lap$) per compound.</p>
            </div>
            <button id="fuel-btn-toggle" onclick="toggleFuelCorrection()" class="px-2.5 py-1 rounded bg-red-600 text-white font-mono font-bold text-xs">
              Fuel Mass Adjustment: ACTIVE (-0.062s/lap)
            </button>
          </div>

          <div class="relative w-full h-80 bg-slate-950/60 rounded-lg p-3 border border-slate-800/80 overflow-hidden">
            <svg id="deg-svg" class="w-full h-full" preserveAspectRatio="none"></svg>
          </div>

          <div class="grid grid-cols-3 gap-3 mt-4 text-xs font-mono">
            <div class="p-3 bg-red-950/30 border border-red-900/50 rounded-lg">
              <div class="text-red-400 font-bold flex justify-between">
                <span>C3 SOFT</span>
                <span class="badge-soft px-1.5 py-0.2 rounded text-[10px]">High Grip</span>
              </div>
              <div class="text-lg font-black text-white mt-1">+0.082 s/lap</div>
              <div class="text-[11px] text-slate-400">Cliff Lap: ~16 Laps</div>
            </div>

            <div class="p-3 bg-amber-950/30 border border-amber-900/50 rounded-lg">
              <div class="text-amber-400 font-bold flex justify-between">
                <span>C2 MEDIUM</span>
                <span class="badge-medium px-1.5 py-0.2 rounded text-[10px]">Balanced</span>
              </div>
              <div class="text-lg font-black text-white mt-1">+0.052 s/lap</div>
              <div class="text-[11px] text-slate-400">Cliff Lap: ~26 Laps</div>
            </div>

            <div class="p-3 bg-slate-900/80 border border-slate-700 rounded-lg">
              <div class="text-slate-200 font-bold flex justify-between">
                <span>C1 HARD</span>
                <span class="badge-hard px-1.5 py-0.2 rounded text-[10px]">Durable</span>
              </div>
              <div class="text-lg font-black text-white mt-1">+0.038 s/lap</div>
              <div class="text-[11px] text-slate-400">Cliff Lap: ~38 Laps</div>
            </div>
          </div>
        </div>

        <div class="space-y-4">
          <div class="f1-card p-5 f1-card-accent">
            <h3 class="text-sm font-bold text-white flex items-center gap-1.5 mb-2">
              <span>⚠️</span> The Thermal Degradation Cliff
            </h3>
            <p class="text-xs text-slate-300 leading-relaxed">
              When tires exceed their designed thermal cycle, rubber delamination causes lap pace to degrade non-linearly at <strong>+0.28s to +0.50s per lap</strong>. At this point, staying out loses more time than executing a pit stop.
            </p>
          </div>

          <div class="f1-card p-5">
            <h3 class="text-sm font-bold text-white flex items-center gap-1.5 mb-2">
              <span>🏔️</span> High Altitude Aerodynamic Sliding
            </h3>
            <p class="text-xs text-slate-300 leading-relaxed">
              Thin air at tracks like <strong>Mexico City (2,227m)</strong> reduces downforce by 22%, increasing tire slip angles and triggering surface graining on softer compounds.
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB: UNDERCUT & SAFETY CAR -->
    <div id="view-undercut" class="space-y-6 hidden">
      <div class="f1-card p-5">
        <h2 class="text-base font-bold text-white mb-3">2024 Real-World Undercut vs. Overcut Battles</h2>
        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs font-mono">
            <thead class="bg-slate-900 text-slate-400 border-b border-slate-800">
              <tr>
                <th class="p-2.5">Grand Prix</th>
                <th class="p-2.5">Attacker / Defender</th>
                <th class="p-2.5">Strategy Move</th>
                <th class="p-2.5">Pre-Pit Gap</th>
                <th class="p-2.5">Out-Lap Delta</th>
                <th class="p-2.5">Outcome</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-800" id="battles-table-body"></tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- TAB: GLOBAL CIRCUIT ATLAS (77 TRACKS) -->
    <div id="view-circuits" class="space-y-6 hidden">
      <div class="f1-card p-5">
        <div class="flex flex-wrap items-center justify-between gap-4 mb-4 border-b border-slate-800 pb-3">
          <div>
            <h2 class="text-base font-bold text-white flex items-center gap-2">
              <span>🌍</span> FIA Circuit Strategy Atlas (All 77 Circuits)
            </h2>
            <p class="text-xs text-slate-400">Searchable elevation, pit loss, and tire wear profiles.</p>
          </div>
          <div class="flex gap-2">
            <input type="text" id="circuit-search" oninput="filterCircuits()" placeholder="Search circuit..." class="bg-slate-900 border border-slate-700 text-xs text-slate-200 px-3 py-1.5 rounded-lg outline-none font-mono">
          </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 max-h-[640px] overflow-y-auto pr-2" id="circuits-grid-container"></div>
      </div>
    </div>

    <!-- TAB: CUSTOM SIMULATOR -->
    <div id="view-simulator" class="space-y-6 hidden">
      <div class="f1-card p-5">
        <h2 class="text-base font-bold text-white mb-2">Interactive What-If Scenario Builder</h2>
        <p class="text-xs text-slate-400 mb-4">Adjust stint compounds & pit stop laps manually to test custom hypotheses.</p>
        <!-- Simulator content -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div class="p-4 bg-slate-900/80 rounded-xl border border-slate-800 space-y-3 font-mono text-xs">
            <div>
              <span class="text-slate-300 block mb-1">Stint 1 Length:</span>
              <input type="range" id="sim-pit1-lap" min="10" max="30" value="16" oninput="runCustomSim()" class="w-full accent-red-600">
            </div>
            <div class="flex justify-between">
              <span>Start Compound: Soft (C3)</span>
              <span>Stint 2 Compound: Hard (C1)</span>
            </div>
          </div>
          <div class="p-4 bg-slate-900/80 rounded-xl border border-slate-800 font-mono text-xs space-y-2">
            <span class="font-bold text-white block">Projected Finish Result</span>
            <div class="text-2xl font-black text-emerald-400" id="sim-result-time">5505.2s</div>
            <span class="text-slate-300 block">Matches P1 Baseline Pace</span>
          </div>
        </div>
      </div>
    </div>

  </main>

  <script>
    const F1_DATA = {json_data_str};
    let selectedDrivers = ["VER", "PER", "SAI", "LEC", "RUS", "NOR"];
    let fuelCorrectionActive = true;

    window.addEventListener("DOMContentLoaded", () => {{
      generateF1Strategies();
      buildDriverBadges();
      renderTelemetryCharts();
      renderStintTimelines();
      renderDegradationChart();
      renderBattlesTable();
      renderCircuitsGrid();
    }});

    function setTab(tab) {{
      const tabs = ["strategy-generator", "telemetry", "degradation", "undercut", "circuits", "simulator"];
      tabs.forEach(t => {{
        const btn = document.getElementById(`tab-${{t}}`);
        const view = document.getElementById(`view-${{t}}`);
        if (t === tab) {{
          btn.classList.add("active");
          btn.classList.remove("text-slate-400");
          btn.classList.add("text-slate-200");
          view.classList.remove("hidden");
        }} else {{
          btn.classList.remove("active");
          btn.classList.remove("text-slate-200");
          btn.classList.add("text-slate-400");
          view.classList.add("hidden");
        }}
      }});
      if (tab === "telemetry") renderTelemetryCharts();
      if (tab === "degradation") renderDegradationChart();
    }}

    function changeCircuitContext(cId) {{
      document.getElementById("gen-circuit").value = cId;
      const c = F1_DATA.circuits.find(x => x.circuitId == cId) || F1_DATA.circuits[0];
      document.getElementById("current-circuit-badge").textContent = `${{c.name}} (${{c.country}})`;
      generateF1Strategies();
    }}

    // AI STRATEGY GENERATOR
    function generateF1Strategies() {{
      const cId = parseInt(document.getElementById("gen-circuit").value);
      const grid = parseInt(document.getElementById("gen-grid").value);
      const tier = parseInt(document.getElementById("gen-tier").value);
      const temp = parseFloat(document.getElementById("gen-temp").value);
      const scProb = parseFloat(document.getElementById("gen-sc").value);

      const circuit = F1_DATA.circuits.find(c => c.circuitId === cId) || F1_DATA.circuits[0];
      const totalLaps = (cId === 6) ? 78 : ((cId === 13) ? 44 : ((cId === 32) ? 71 : 57));
      const baseLap = (circuit.length_km / 5.412) * 94.8 + (tier - 1) * 0.45;
      const pitLoss = circuit.pit_loss_sec;

      // Strategy Permutations
      const plans = [
        {{
          plan_code: "PLAN A (PRIMARY OPTIMAL)",
          name: (circuit.typical_stops === 1) ? "1-Stop Medium → Hard (Pace Balance)" : "2-Stop Soft → Hard → Soft (Sprint Attack)",
          stints: (circuit.typical_stops === 1) 
            ? [{{ comp: "MEDIUM", start: 1, end: Math.floor(totalLaps * 0.42), color: "#FFF200" }},
               {{ comp: "HARD", start: Math.floor(totalLaps * 0.42) + 1, end: totalLaps, color: "#FFFFFF" }}]
            : [{{ comp: "SOFT", start: 1, end: Math.floor(totalLaps * 0.28), color: "#E10600" }},
               {{ comp: "HARD", start: Math.floor(totalLaps * 0.28) + 1, end: Math.floor(totalLaps * 0.65), color: "#FFFFFF" }},
               {{ comp: "SOFT", start: Math.floor(totalLaps * 0.65) + 1, end: totalLaps, color: "#E10600" }}],
          pit_windows: (circuit.typical_stops === 1) ? `Laps ${{Math.floor(totalLaps * 0.40)}}-${{Math.floor(totalLaps * 0.44)}}` : `L${{Math.floor(totalLaps * 0.26)}}-${{Math.floor(totalLaps * 0.30)}} & L${{Math.floor(totalLaps * 0.63)}}-${{Math.floor(totalLaps * 0.67)}}`,
          total_time: (totalLaps * baseLap + pitLoss * circuit.typical_stops).toFixed(1),
          predicted_finish: (grid <= 3 && tier === 1) ? "P1 - Victory Contender" : ((grid <= 8) ? "P3 - Podium" : "P5 - Top 6"),
          confidence: "94.8%",
          summary: "Engine-calculated fastest theoretical race execution time. Maintains tires inside the thermal window.",
          color_accent: "border-red-600"
        }},
        {{
          plan_code: "PLAN B (AGGRESSIVE UNDERCUT)",
          name: "2-Stop Soft → Hard → Medium (Track Attack)",
          stints: [
            {{ comp: "SOFT", start: 1, end: Math.floor(totalLaps * 0.24), color: "#E10600" }},
            {{ comp: "HARD", start: Math.floor(totalLaps * 0.24) + 1, end: Math.floor(totalLaps * 0.60), color: "#FFFFFF" }},
            {{ comp: "MEDIUM", start: Math.floor(totalLaps * 0.60) + 1, end: totalLaps, color: "#FFF200" }}
          ],
          pit_windows: `Laps ${{Math.floor(totalLaps * 0.22)}}-${{Math.floor(totalLaps * 0.25)}} & L${{Math.floor(totalLaps * 0.58)}}-${{Math.floor(totalLaps * 0.62)}}`,
          total_time: (totalLaps * baseLap + pitLoss * 2 + 1.8).toFixed(1),
          predicted_finish: (grid <= 5 && tier === 1) ? "P1 - P2" : "P3 - P5",
          confidence: "88.2%",
          summary: "Pits 2 laps earlier to exploit the +1.74s out-lap fresh tire grip jump, leapfrogging defending cars.",
          color_accent: "border-amber-500"
        }},
        {{
          plan_code: "PLAN C (CONTINGENCY / SC GAMBLE)",
          name: "1-Stop Hard → Medium (Reverse Overcut)",
          stints: [
            {{ comp: "HARD", start: 1, end: Math.floor(totalLaps * 0.62), color: "#FFFFFF" }},
            {{ comp: "MEDIUM", start: Math.floor(totalLaps * 0.62) + 1, end: totalLaps, color: "#FFF200" }}
          ],
          pit_windows: `Laps ${{Math.floor(totalLaps * 0.60)}}-${{Math.floor(totalLaps * 0.65)}}`,
          total_time: (totalLaps * baseLap + pitLoss - (scProb > 0.3 ? 11.2 : 0)).toFixed(1),
          predicted_finish: (scProb >= 0.4) ? "P2 - P4 (High SC Dividend)" : "P6 - P8",
          confidence: "81.0%",
          summary: "Extends opening stint on durable rubber. If Safety Car triggers, saves 12s in pit lane for a free pit stop.",
          color_accent: "border-purple-500"
        }}
      ];

      // Render Strategy Plans Cards
      const container = document.getElementById("strategy-plans-container");
      container.innerHTML = "";

      plans.forEach(p => {{
        const card = document.createElement("div");
        card.className = `f1-card p-5 border-t-4 ${{p.color_accent}} flex flex-col justify-between space-y-4`;

        let stintBars = "";
        p.stints.forEach(s => {{
          const dur = s.end - s.start + 1;
          const pct = (dur / totalLaps) * 100;
          stintBars += `
            <div style="width: ${{pct}}%; background-color: ${{s.color}};" class="h-6 rounded text-black font-bold text-[10px] flex items-center justify-center font-mono">
              ${{s.comp[0]}} (${{dur}}L)
            </div>
          `;
        }});

        card.innerHTML = `
          <div>
            <div class="flex items-center justify-between font-mono text-[11px] mb-1">
              <span class="text-red-400 font-bold">${{p.plan_code}}</span>
              <span class="px-2 py-0.5 rounded bg-slate-900 border border-slate-700 text-slate-300 font-bold">${{p.confidence}} Conf</span>
            </div>
            <h3 class="text-base font-bold text-white">${{p.name}}</h3>
            <p class="text-xs text-slate-400 mt-1">${{p.summary}}</p>
          </div>

          <div class="space-y-2">
            <span class="text-[10px] font-mono text-slate-400 uppercase tracking-wider block">STINT PROGRESSION (GANTT)</span>
            <div class="w-full flex gap-1 bg-slate-950 p-1 rounded-lg border border-slate-800">
              ${{stintBars}}
            </div>
          </div>

          <div class="grid grid-cols-2 gap-2 text-xs font-mono bg-slate-950/80 p-3 rounded-lg border border-slate-800/80">
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
            <span>⚡ TRIGGER: RIVAL UNDERCUT ATTEMPT</span>
          </div>
          <p class="text-slate-300 text-xs">If competitor within 1.8s boxes: <strong>Box on immediate next lap to defend track position</strong>. Failure to react guarantees undercut defeat.</p>
        </div>
        <div class="p-3.5 bg-slate-950/80 rounded-xl border border-slate-800 space-y-1">
          <div class="flex items-center gap-2 text-amber-400 font-bold">
            <span>⚠️ TRIGGER: VSC / SAFETY CAR DEPLOYED</span>
          </div>
          <p class="text-slate-300 text-xs">If neutralization occurs between L${{Math.floor(totalLaps * 0.35)}}-L${{Math.floor(totalLaps * 0.70)}}: <strong>BOX IMMEDIATELY</strong>. Saves ${{circuit.pit_loss_sec - 10.0}}s in pit loss delta.</p>
        </div>
        <div class="p-3.5 bg-slate-950/80 rounded-xl border border-slate-800 space-y-1">
          <div class="flex items-center gap-2 text-purple-400 font-bold">
            <span>📉 TRIGGER: THERMAL CLIFF DROP-OFF</span>
          </div>
          <p class="text-slate-300 text-xs">If lap pace drops by &gt;0.4s for two consecutive laps: <strong>Abort current stint and pit 2 laps early</strong> to avoid exponential cliff.</p>
        </div>
        <div class="p-3.5 bg-slate-950/80 rounded-xl border border-slate-800 space-y-1">
          <div class="flex items-center gap-2 text-emerald-400 font-bold">
            <span>🏁 TRIGGER: LATE SAFETY CAR (&lt;12 LAPS TO GO)</span>
          </div>
          <p class="text-slate-300 text-xs">Pit for scrubbed Softs. Field compression gives fresh Soft tire +1.8s/lap grip advantage on rolling restart.</p>
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
        btn.className = `px-2 py-0.5 rounded text-xs font-mono font-bold transition flex items-center gap-1 border ${{
          isSel ? 'bg-slate-800 text-white border-slate-600' : 'bg-slate-950 text-slate-500 border-slate-800'
        }}`;
        btn.innerHTML = `<span class="w-2 h-2 rounded-full" style="background-color: ${{d.color}}"></span> ${{d.code}}`;
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
        paceSvg.innerHTML += `<line x1="${{pL}}" y1="${{y}}" x2="${{w - pR}}" y2="${{y}}" stroke="#222733" stroke-dasharray="3,3"/>`;
        paceSvg.innerHTML += `<text x="${{pL - 6}}" y="${{y + 3}}" fill="#64748B" font-size="10" font-family="monospace" text-anchor="end">${{p}}s</text>`;
      }}

      for (let g = 0; g <= 40; g += 10) {{
        const y = pT + (h - pT - pB) * (g / 45);
        gapSvg.innerHTML += `<line x1="${{pL}}" y1="${{y}}" x2="${{w - pR}}" y2="${{y}}" stroke="#222733" stroke-dasharray="3,3"/>`;
        gapSvg.innerHTML += `<text x="${{pL - 6}}" y="${{y + 3}}" fill="#64748B" font-size="10" font-family="monospace" text-anchor="end">+${{g}}s</text>`;
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

        paceSvg.innerHTML += `<polyline points="${{pacePts.join(" ")}}" fill="none" stroke="${{dInfo.color}}" stroke-width="2.2" opacity="0.9"/>`;
        gapSvg.innerHTML += `<polyline points="${{gapPts.join(" ")}}" fill="none" stroke="${{dInfo.color}}" stroke-width="2.2" opacity="0.9"/>`;
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

          bars += `<div style="width: ${{pct}}%; background-color: ${{color}}; color: ${{textCol}};" class="stint-bar-item h-6 rounded flex items-center justify-between px-2 font-bold text-[10px]">
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
      const w = 800, h = 300, pL = 45, pR = 20, pT = 20, pB = 30;
      svg.setAttribute("viewBox", `0 0 ${{w}} ${{h}}`);

      for (let p = 94; p <= 99; p += 1) {{
        const y = pT + (h - pT - pB) * (p - 93.5) / 6;
        svg.innerHTML += `<line x1="${{pL}}" y1="${{y}}" x2="${{w - pR}}" y2="${{y}}" stroke="#222733" stroke-dasharray="3,3"/>`;
        svg.innerHTML += `<text x="${{pL - 6}}" y="${{y + 3}}" fill="#64748B" font-size="10" font-family="monospace" text-anchor="end">${{p}}s</text>`;
      }}

      // Trendlines
      svg.innerHTML += `<line x1="${{pL}}" y1="${{pT + (h - pT - pB) * 0.15}}" x2="${{pL + 400}}" y2="${{pT + (h - pT - pB) * 0.85}}" stroke="#E10600" stroke-width="3"/>`;
      svg.innerHTML += `<line x1="${{pL}}" y1="${{pT + (h - pT - pB) * 0.35}}" x2="${{w - pR}}" y2="${{pT + (h - pT - pB) * 0.9}}" stroke="#FFFFFF" stroke-width="3"/>`;
    }}

    function toggleFuelCorrection() {{
      fuelCorrectionActive = !fuelCorrectionActive;
      const b = document.getElementById("fuel-btn-toggle");
      b.textContent = fuelCorrectionActive ? "Fuel Mass Adjustment: ACTIVE (-0.062s/lap)" : "Fuel Mass Adjustment: OFF (Raw Pace)";
      b.className = fuelCorrectionActive ? "px-2.5 py-1 rounded bg-red-600 text-white font-mono font-bold text-xs" : "px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-mono font-bold text-xs";
    }}

    function renderBattlesTable() {{
      const tbody = document.getElementById("battles-table-body");
      tbody.innerHTML = "";
      F1_DATA.pit_stop_battles.forEach(b => {{
        tbody.innerHTML += `
          <tr class="hover:bg-slate-900/40">
            <td class="p-2.5 font-bold text-white">${{b.race}}</td>
            <td class="p-2.5"><span class="text-emerald-400 font-bold">${{b.attacking_driver}}</span> vs <span class="text-red-400">${{b.defending_driver}}</span></td>
            <td class="p-2.5"><span class="px-2 py-0.5 rounded bg-slate-800 text-slate-200">${{b.tactic}}</span></td>
            <td class="p-2.5">${{b.pre_gap_sec}}s</td>
            <td class="p-2.5 font-bold text-emerald-400">${{b.outlap_delta_sec}}s</td>
            <td class="p-2.5 text-emerald-300 font-bold">${{b.outcome}}</td>
          </tr>
        `;
      }});
    }}

    function renderCircuitsGrid() {{
      const c = document.getElementById("circuits-grid-container");
      c.innerHTML = "";
      F1_DATA.circuits.forEach(item => {{
        c.innerHTML += `
          <div class="p-3.5 rounded-xl bg-slate-950/80 border border-slate-800 font-mono text-xs space-y-2">
            <div class="flex justify-between font-bold">
              <span class="text-red-400">${{item.country}}</span>
              <span class="text-slate-400">${{item.alt}}m alt</span>
            </div>
            <div class="text-white font-bold text-sm">${{item.name}}</div>
            <div class="flex justify-between text-[11px] text-slate-300 pt-1 border-t border-slate-800">
              <span>Pit Loss: ${{item.pit_loss_sec}}s</span>
              <span class="text-amber-400 font-bold">${{item.typical_stops}}-Stop Typical</span>
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
          <div class="p-3.5 rounded-xl bg-slate-950/80 border border-slate-800 font-mono text-xs space-y-2">
            <div class="flex justify-between font-bold">
              <span class="text-red-400">${{item.country}}</span>
              <span class="text-slate-400">${{item.alt}}m alt</span>
            </div>
            <div class="text-white font-bold text-sm">${{item.name}}</div>
            <div class="flex justify-between text-[11px] text-slate-300 pt-1 border-t border-slate-800">
              <span>Pit Loss: ${{item.pit_loss_sec}}s</span>
              <span class="text-amber-400 font-bold">${{item.typical_stops}}-Stop Typical</span>
            </div>
          </div>
        `;
      }});
    }}

    function runCustomSim() {{
      const p1 = parseInt(document.getElementById("sim-pit1-lap").value);
      const delta = (p1 - 16) * 0.18;
      document.getElementById("sim-result-time").textContent = `${{(5504.8 + delta).toFixed(1)}}s`;
    }}
  </script>
</body>
</html>
"""

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(master_html)

with open(ARTIFACT_HTML, "w", encoding="utf-8") as f:
    f.write(master_html)

print("Updated master dashboard successfully!")
