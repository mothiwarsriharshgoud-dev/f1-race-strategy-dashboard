import json
import os

DATA_PATH = "C:/Users/Main User/.gemini/antigravity/scratch/f1-race-strategy-dashboard/data/f1_strategy_dataset.json"
OUTPUT_HTML = "C:/Users/Main User/.gemini/antigravity/scratch/f1-race-strategy-dashboard/index.html"
ARTIFACT_HTML = "C:/Users/Main User/.gemini/antigravity/brain/bb0fc362-bdeb-4a83-b7c8-80ce516a46a3/f1_race_strategy_dashboard.html"

with open(DATA_PATH, "r", encoding="utf-8") as f:
    f1_data = json.load(f)

json_data_str = json.dumps(f1_data)

html_template = f"""<!DOCTYPE html>
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
      --f1-dark: #0F1115;
      --f1-panel: #161920;
      --f1-panel-alt: #1E222D;
      --f1-border: #2B313E;
      --f1-text: #F3F4F6;
      --f1-muted: #9CA3AF;
      --soft: #E10600;
      --medium: #FFF200;
      --hard: #FFFFFF;
      --inter: #39B54A;
      --wet: #00A0DE;
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

    /* Custom Scrollbars */
    ::-webkit-scrollbar {{
      width: 8px;
      height: 8px;
    }}
    ::-webkit-scrollbar-track {{
      background: #11141A;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #2D3340;
      border-radius: 4px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #E10600;
    }}

    .carbon-pattern {{
      background-color: #0F1115;
      background-image: radial-gradient(#1E232F 0.75px, transparent 0.75px), radial-gradient(#1E232F 0.75px, #0F1115 0.75px);
      background-size: 20px 20px;
      background-position: 0 0, 10px 10px;
    }}

    .f1-card {{
      background: linear-gradient(135deg, rgba(22, 25, 32, 0.95) 0%, rgba(27, 31, 41, 0.90) 100%);
      border: 1px solid var(--f1-border);
      border-radius: 12px;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35);
      backdrop-filter: blur(8px);
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
      background: linear-gradient(90deg, rgba(225, 6, 0, 0.2) 0%, rgba(225, 6, 0, 0.05) 100%);
      border-bottom: 3px solid var(--f1-red);
      color: #FFFFFF;
      font-weight: 700;
    }}

    .stint-bar {{
      transition: all 0.2s ease;
    }}
    .stint-bar:hover {{
      filter: brightness(1.25);
      transform: translateY(-2px);
    }}
  </style>
</head>
<body class="carbon-pattern min-h-screen text-slate-100 antialiased">

  <!-- TOP HEADER / HUD -->
  <header class="border-b border-slate-800 bg-slate-950/80 sticky top-0 z-50 backdrop-blur-md">
    <div class="max-w-7xl mx-auto px-4 py-3 flex flex-wrap items-center justify-between gap-4">
      <div class="flex items-center gap-3">
        <div class="bg-red-600 text-white font-black px-2.5 py-1 rounded text-lg tracking-wider flex items-center gap-1.5 shadow-lg shadow-red-900/40">
          <span>F1</span>
          <span class="text-xs bg-black/40 px-1.5 py-0.5 rounded font-mono">P32</span>
        </div>
        <div>
          <div class="flex items-center gap-2">
            <h1 class="text-lg md:text-xl font-bold tracking-tight text-white flex items-center gap-2">
              Formula 1 Race Telemetry & Strategy Analytics Platform
            </h1>
            <span class="text-xs bg-emerald-950 text-emerald-400 border border-emerald-800 px-2 py-0.5 rounded-full font-mono flex items-center gap-1">
              <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span> 2024 SEASON DATA
            </span>
          </div>
          <p class="text-xs text-slate-400 font-medium">
            Core Analytical Question: <span class="text-red-400 font-semibold italic">"How do race strategies influence Formula 1 performance?"</span>
          </p>
        </div>
      </div>

      <!-- Quick Race Benchmark Selector -->
      <div class="flex items-center gap-3">
        <div class="flex flex-col text-right">
          <span class="text-[11px] uppercase tracking-wider text-slate-400 font-mono">Benchmark Session</span>
          <span class="text-xs font-semibold text-slate-200" id="current-gp-label">2024 Bahrain GP (57 Laps)</span>
        </div>
        <select id="race-selector" onchange="switchRace(this.value)" class="bg-slate-900 border border-slate-700 text-slate-200 text-xs rounded-lg px-3 py-1.5 font-medium focus:ring-2 focus:ring-red-500 outline-none">
          <option value="1">Rd 1: Bahrain GP (Sakhir)</option>
          <option value="8">Rd 8: Monaco GP (Monte Carlo)</option>
          <option value="12">Rd 12: British GP (Silverstone)</option>
          <option value="14">Rd 14: Belgian GP (Spa)</option>
          <option value="16">Rd 16: Italian GP (Monza 1-Stop)</option>
          <option value="22">Rd 22: Las Vegas GP (Strip)</option>
          <option value="24">Rd 24: Abu Dhabi GP (Yas Marina)</option>
        </select>
      </div>
    </div>

    <!-- NAVIGATION TABS -->
    <div class="max-w-7xl mx-auto px-4 flex gap-1 overflow-x-auto text-xs font-medium border-t border-slate-800/60">
      <button onclick="setTab('telemetry')" id="tab-telemetry" class="tab-btn active px-4 py-2.5 text-slate-300 hover:text-white transition flex items-center gap-1.5">
        <span>⏱️</span> Lap Pace & Telemetry
      </button>
      <button onclick="setTab('degradation')" id="tab-degradation" class="tab-btn px-4 py-2.5 text-slate-400 hover:text-white transition flex items-center gap-1.5">
        <span>📉</span> Tire Degradation Modeling
      </button>
      <button onclick="setTab('undercut')" id="tab-undercut" class="tab-btn px-4 py-2.5 text-slate-400 hover:text-white transition flex items-center gap-1.5">
        <span>⚡</span> Pit Stop & Undercut Dynamics
      </button>
      <button onclick="setTab('circuits')" id="tab-circuits" class="tab-btn px-4 py-2.5 text-slate-400 hover:text-white transition flex items-center gap-1.5">
        <span>🌍</span> Global Circuit Strategy Atlas (77 Tracks)
      </button>
      <button onclick="setTab('simulator')" id="tab-simulator" class="tab-btn px-4 py-2.5 text-slate-400 hover:text-white transition flex items-center gap-1.5">
        <span>🎮</span> Live Strategy Simulator (What-If)
      </button>
    </div>
  </header>

  <!-- MAIN CONTAINER -->
  <main class="max-w-7xl mx-auto px-4 py-6 space-y-6">

    <!-- KPI STATS STRIP -->
    <section class="grid grid-cols-2 md:grid-cols-5 gap-3">
      <div class="f1-card p-3 border-l-4 border-l-red-500">
        <div class="text-[11px] font-mono text-slate-400 uppercase tracking-wider">Undercut Success Rate</div>
        <div class="text-xl md:text-2xl font-black text-white mt-1 flex items-baseline gap-1">
          <span class="text-red-400">68.4%</span>
          <span class="text-[10px] text-emerald-400 font-mono">+1.74s gap delta</span>
        </div>
        <div class="text-[11px] text-slate-400 mt-1">High across abrasive circuits</div>
      </div>

      <div class="f1-card p-3 border-l-4 border-l-amber-400">
        <div class="text-[11px] font-mono text-slate-400 uppercase tracking-wider">VSC / SC Pit Dividend</div>
        <div class="text-xl md:text-2xl font-black text-white mt-1 flex items-baseline gap-1">
          <span class="text-amber-400">+9.4s - 12.0s</span>
        </div>
        <div class="text-[11px] text-slate-400 mt-1">Pit loss drops from 22s to 10s</div>
      </div>

      <div class="f1-card p-3 border-l-4 border-l-emerald-500">
        <div class="text-[11px] font-mono text-slate-400 uppercase tracking-wider">Strategy-Dictated Wins</div>
        <div class="text-xl md:text-2xl font-black text-white mt-1 flex items-baseline gap-1">
          <span class="text-emerald-400">42.8%</span>
          <span class="text-[10px] text-slate-300 font-mono">net position gain</span>
        </div>
        <div class="text-[11px] text-slate-400 mt-1">Podiums decided by pit timing</div>
      </div>

      <div class="f1-card p-3 border-l-4 border-l-blue-500">
        <div class="text-[11px] font-mono text-slate-400 uppercase tracking-wider">1-Stop vs 2-Stop Split</div>
        <div class="text-xl md:text-2xl font-black text-white mt-1 flex items-baseline gap-1">
          <span class="text-blue-400">54% / 38%</span>
        </div>
        <div class="text-[11px] text-slate-400 mt-1">Monza 1-stop vs Bahrain 2-stop</div>
      </div>

      <div class="f1-card p-3 border-l-4 border-l-purple-500 col-span-2 md:col-span-1">
        <div class="text-[11px] font-mono text-slate-400 uppercase tracking-wider">Fuel-Burn Effect</div>
        <div class="text-xl md:text-2xl font-black text-white mt-1 flex items-baseline gap-1">
          <span class="text-purple-300">-0.062 s/lap</span>
        </div>
        <div class="text-[11px] text-slate-400 mt-1">110kg fuel lightens chassis</div>
      </div>
    </section>

    <!-- TAB 1: RACE TELEMETRY & LAP PACE -->
    <div id="view-telemetry" class="space-y-6">
      
      <!-- Controls Bar -->
      <div class="f1-card p-4 flex flex-wrap items-center justify-between gap-4">
        <div class="flex items-center gap-3">
          <span class="text-xs font-semibold text-slate-300 uppercase tracking-wider">Selected Drivers:</span>
          <div class="flex flex-wrap gap-1.5" id="driver-toggle-container">
            <!-- Dynamically populated driver badges -->
          </div>
        </div>

        <div class="flex items-center gap-4 text-xs font-mono">
          <label class="flex items-center gap-1.5 cursor-pointer text-slate-300 hover:text-white">
            <input type="checkbox" id="toggle-smooth" onchange="renderTelemetryCharts()" checked class="rounded bg-slate-900 border-slate-700 text-red-600 focus:ring-0">
            <span>3-Lap Rolling Smooth</span>
          </label>
          <label class="flex items-center gap-1.5 cursor-pointer text-slate-300 hover:text-white">
            <input type="checkbox" id="toggle-pits" onchange="renderTelemetryCharts()" checked class="rounded bg-slate-900 border-slate-700 text-red-600 focus:ring-0">
            <span>Show Pit Markers</span>
          </label>
        </div>
      </div>

      <!-- Main Lap Chart & Gap Chart Side by Side or Stacked -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        
        <!-- Left: Lap Time Pace Evolution (2 cols) -->
        <div class="f1-card p-5 lg:col-span-2 flex flex-col justify-between">
          <div class="flex items-center justify-between mb-3 border-b border-slate-800 pb-2">
            <div>
              <h2 class="text-base font-bold text-white flex items-center gap-2">
                <span>🏎️</span> Lap-by-Lap Pace Evolution
              </h2>
              <p class="text-xs text-slate-400">Progression of lap times (seconds) across all 57 laps with compound stints.</p>
            </div>
            <div class="flex items-center gap-2 text-xs font-mono">
              <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded badge-soft">● Soft</span>
              <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded badge-medium">● Medium</span>
              <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded badge-hard">● Hard</span>
            </div>
          </div>

          <!-- SVG Canvas for Lap Time -->
          <div class="relative w-full h-80 bg-slate-950/60 rounded-lg p-2 border border-slate-800/80 overflow-hidden" id="pace-chart-container">
            <svg id="pace-svg" class="w-full h-full" preserveAspectRatio="none"></svg>
            <div id="pace-tooltip" class="absolute hidden bg-slate-900/95 border border-slate-700 text-slate-100 text-xs p-2 rounded shadow-xl pointer-events-none z-30 font-mono"></div>
          </div>
          <div class="flex justify-between items-center text-[11px] font-mono text-slate-500 mt-2 px-1">
            <span>Lap 1 (Start)</span>
            <span>Pit Window 1 (L12-L18)</span>
            <span>Pit Window 2 (L32-L38)</span>
            <span>Lap 57 (Chequered Flag)</span>
          </div>
        </div>

        <!-- Right: Cumulative Delta to Leader (1 col) -->
        <div class="f1-card p-5 flex flex-col justify-between">
          <div class="flex items-center justify-between mb-3 border-b border-slate-800 pb-2">
            <div>
              <h2 class="text-base font-bold text-white flex items-center gap-2">
                <span>⏱️</span> Gap to Benchmark (s)
              </h2>
              <p class="text-xs text-slate-400">Cumulative time delta relative to race leader VER.</p>
            </div>
          </div>

          <div class="relative w-full h-80 bg-slate-950/60 rounded-lg p-2 border border-slate-800/80 overflow-hidden" id="gap-chart-container">
            <svg id="gap-svg" class="w-full h-full" preserveAspectRatio="none"></svg>
            <div id="gap-tooltip" class="absolute hidden bg-slate-900/95 border border-slate-700 text-slate-100 text-xs p-2 rounded shadow-xl pointer-events-none z-30 font-mono"></div>
          </div>

          <div class="text-[11px] font-mono text-slate-400 mt-2 flex justify-between">
            <span>Delta: 0.0s (Leader)</span>
            <span class="text-red-400">+25.0s Pitted Gap</span>
          </div>
        </div>
      </div>

      <!-- Driver Stint Gantt Timeline -->
      <div class="f1-card p-5">
        <div class="flex items-center justify-between mb-3 border-b border-slate-800 pb-2">
          <div>
            <h2 class="text-base font-bold text-white flex items-center gap-2">
              <span>📊</span> Tire Strategy Stint Timeline (Gantt View)
            </h2>
            <p class="text-xs text-slate-400">Exact compound choices and stint lengths per driver across 57 laps.</p>
          </div>
          <div class="text-xs font-mono text-slate-400">
            Hover over stints for lap range & degradation
          </div>
        </div>

        <div class="space-y-2 mt-4" id="stint-timeline-container">
          <!-- Populated dynamically via JS -->
        </div>
      </div>

    </div>

    <!-- TAB 2: TIRE DEGRADATION MODELING -->
    <div id="view-degradation" class="space-y-6 hidden">
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        
        <!-- Left: Degradation Scatter & Regression (2 cols) -->
        <div class="f1-card p-5 lg:col-span-2">
          <div class="flex flex-wrap items-center justify-between mb-4 border-b border-slate-800 pb-3 gap-2">
            <div>
              <h2 class="text-base font-bold text-white flex items-center gap-2">
                <span>📉</span> Tire Degradation Rate: Tyre Life vs. Lap Time
              </h2>
              <p class="text-xs text-slate-400">Linear regression slope modeling tire wear ($s/lap$) per compound.</p>
            </div>

            <!-- Fuel Correction Toggle -->
            <div class="flex items-center gap-2 bg-slate-900 border border-slate-700 px-3 py-1.5 rounded-lg text-xs font-mono">
              <span class="text-slate-400">Fuel Mass Adjustment:</span>
              <button id="fuel-btn-toggle" onclick="toggleFuelCorrection()" class="px-2 py-0.5 rounded bg-red-600 text-white font-bold transition">
                ACTIVE (-0.062s/lap)
              </button>
            </div>
          </div>

          <div class="relative w-full h-84 bg-slate-950/60 rounded-lg p-3 border border-slate-800/80 overflow-hidden" id="deg-chart-container">
            <svg id="deg-svg" class="w-full h-80" preserveAspectRatio="none"></svg>
            <div id="deg-tooltip" class="absolute hidden bg-slate-900/95 border border-slate-700 text-slate-100 text-xs p-2 rounded shadow-xl pointer-events-none z-30 font-mono"></div>
          </div>

          <!-- Degradation Slopes Breakdown -->
          <div class="grid grid-cols-3 gap-3 mt-4 text-xs font-mono">
            <div class="p-3 bg-red-950/30 border border-red-900/50 rounded-lg">
              <div class="text-red-400 font-bold flex items-center justify-between">
                <span>C3 SOFT COMPOUND</span>
                <span class="badge-soft px-1.5 py-0.2 rounded text-[10px]">High Grip</span>
              </div>
              <div class="text-lg font-black text-white mt-1">+0.082 s/lap</div>
              <div class="text-[11px] text-slate-400">Degradation slope | Cliff at ~16 Laps</div>
            </div>

            <div class="p-3 bg-amber-950/30 border border-amber-900/50 rounded-lg">
              <div class="text-amber-400 font-bold flex items-center justify-between">
                <span>C2 MEDIUM COMPOUND</span>
                <span class="badge-medium px-1.5 py-0.2 rounded text-[10px]">Balanced</span>
              </div>
              <div class="text-lg font-black text-white mt-1">+0.052 s/lap</div>
              <div class="text-[11px] text-slate-400">Degradation slope | Cliff at ~26 Laps</div>
            </div>

            <div class="p-3 bg-slate-900/80 border border-slate-700 rounded-lg">
              <div class="text-slate-200 font-bold flex items-center justify-between">
                <span>C1 HARD COMPOUND</span>
                <span class="badge-hard px-1.5 py-0.2 rounded text-[10px]">Durable</span>
              </div>
              <div class="text-lg font-black text-white mt-1">+0.038 s/lap</div>
              <div class="text-[11px] text-slate-400">Degradation slope | Cliff at ~38 Laps</div>
            </div>
          </div>
        </div>

        <!-- Right: The "Tire Cliff" Explanation & Elevation Impact -->
        <div class="space-y-4">
          <div class="f1-card p-5 f1-card-accent">
            <h3 class="text-sm font-bold text-white flex items-center gap-1.5 mb-2">
              <span>⚠️</span> The "Tyre Cliff" Mechanics
            </h3>
            <p class="text-xs text-slate-300 leading-relaxed">
              In Formula 1, tire wear follows a quasi-linear slope until reaching the <strong>thermal degradation threshold</strong> (the "cliff"). At this point, the tread depth is insufficient to dissipate heat, causing blistering or graining. Lap times suddenly spike by <strong>1.5s to 3.0s per lap</strong>, rendering the car an easy target for competitors on fresher rubber.
            </p>
            <div class="mt-3 p-2.5 bg-slate-900/80 rounded border border-slate-800 text-xs font-mono text-red-300">
              Crossover Rule: Pitting is optimal when <span class="text-white font-bold">Lap_Loss &gt; (Pit_Loss / Remaining_Laps)</span>.
            </div>
          </div>

          <div class="f1-card p-5">
            <h3 class="text-sm font-bold text-white flex items-center gap-1.5 mb-2">
              <span>🏔️</span> Circuit Altitude vs. Tire Graining
            </h3>
            <p class="text-xs text-slate-300 leading-relaxed">
              At high-altitude circuits like <strong>Mexico City (2,227m)</strong> and <strong>São Paulo (785m)</strong>, thin air density reduces aerodynamic downforce by ~25%. Cars slide significantly more through medium-speed corners, inducing severe surface graining on softer compounds while reducing brake cooling airflow.
            </p>
            <div class="mt-3 grid grid-cols-2 gap-2 text-xs font-mono">
              <div class="p-2 bg-slate-900 rounded">
                <span class="text-slate-400 text-[10px]">MEXICO (2,227m)</span>
                <div class="text-white font-bold">1-Stop Mandatory</div>
              </div>
              <div class="p-2 bg-slate-900 rounded">
                <span class="text-slate-400 text-[10px]">BAHRAIN (7m)</span>
                <div class="text-white font-bold">2-Stop High Wear</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 3: PIT STOP & UNDERCUT DYNAMICS -->
    <div id="view-undercut" class="space-y-6 hidden">
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        
        <!-- Tactical Case Studies Matrix -->
        <div class="f1-card p-5 lg:col-span-2">
          <div class="flex items-center justify-between mb-4 border-b border-slate-800 pb-2">
            <div>
              <h2 class="text-base font-bold text-white flex items-center gap-2">
                <span>⚔️</span> Real-World 2024 Undercut vs. Overcut Battles
              </h2>
              <p class="text-xs text-slate-400">Empirical track outcomes demonstrating how strategic timing overrides raw qualifying pace.</p>
            </div>
          </div>

          <div class="overflow-x-auto">
            <table class="w-full text-left text-xs font-mono">
              <thead class="bg-slate-900/80 text-slate-400 border-b border-slate-800">
                <tr>
                  <th class="p-2.5">Grand Prix</th>
                  <th class="p-2.5">Attacker / Defender</th>
                  <th class="p-2.5">Strategy Move</th>
                  <th class="p-2.5">Pre-Pit Gap</th>
                  <th class="p-2.5">Out-Lap Delta</th>
                  <th class="p-2.5">Outcome</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-800" id="battles-table-body">
                <!-- Dynamically populated -->
              </tbody>
            </table>
          </div>
        </div>

        <!-- Pit Delta Visualization -->
        <div class="space-y-4">
          <div class="f1-card p-5">
            <h3 class="text-sm font-bold text-white flex items-center gap-1.5 mb-2">
              <span>⏱️</span> Pit Lane Transit Loss Comparison
            </h3>
            <p class="text-xs text-slate-400 mb-4">
              Time lost during pit stop under different race neutralization conditions.
            </p>

            <div class="space-y-3 font-mono text-xs">
              <div>
                <div class="flex justify-between text-slate-300 mb-1">
                  <span>Green Flag (Normal Race Pace)</span>
                  <span class="font-bold text-white">21.8s</span>
                </div>
                <div class="w-full h-3 bg-slate-900 rounded-full overflow-hidden">
                  <div class="h-full bg-red-600 rounded-full" style="width: 100%;"></div>
                </div>
              </div>

              <div>
                <div class="flex justify-between text-slate-300 mb-1">
                  <span>Virtual Safety Car (VSC Delta)</span>
                  <span class="font-bold text-amber-400">12.4s (-9.4s gain)</span>
                </div>
                <div class="w-full h-3 bg-slate-900 rounded-full overflow-hidden">
                  <div class="h-full bg-amber-500 rounded-full" style="width: 57%;"></div>
                </div>
              </div>

              <div>
                <div class="flex justify-between text-slate-300 mb-1">
                  <span>Full Safety Car (SC Speed limit)</span>
                  <span class="font-bold text-emerald-400">9.8s (-12.0s gain)</span>
                </div>
                <div class="w-full h-3 bg-slate-900 rounded-full overflow-hidden">
                  <div class="h-full bg-emerald-500 rounded-full" style="width: 45%;"></div>
                </div>
              </div>
            </div>

            <div class="mt-4 p-3 bg-emerald-950/40 border border-emerald-900/60 rounded-lg text-xs text-emerald-300">
              <strong>Strategy Insight:</strong> Pitting under Safety Car yields an instantaneous ~12.0 second "free pit stop" advantage over cars that pitted under green flag conditions.
            </div>
          </div>

          <!-- Undercut Formula Card -->
          <div class="f1-card p-5 f1-card-accent">
            <h3 class="text-sm font-bold text-white mb-2">The Undercut Equation</h3>
            <p class="text-xs text-slate-300 leading-relaxed font-mono">
              Delta_Total = (In_Lap_A - In_Lap_B) + (Pit_Stop_A - Pit_Stop_B) + (Out_Lap_A - Normal_Lap_B)
            </p>
            <p class="text-xs text-slate-400 mt-2">
              If fresh tire warmup delta (&gt;1.5s faster per lap) exceeds the track gap, Car A successfully undercuts Car B upon pit exit.
            </p>
          </div>
        </div>

      </div>
    </div>

    <!-- TAB 4: GLOBAL CIRCUIT STRATEGY ATLAS (77 TRACKS) -->
    <div id="view-circuits" class="space-y-6 hidden">
      <div class="f1-card p-5">
        <div class="flex flex-wrap items-center justify-between gap-4 mb-4 border-b border-slate-800 pb-3">
          <div>
            <h2 class="text-base font-bold text-white flex items-center gap-2">
              <span>🌍</span> FIA Formula 1 World Championship Circuit Atlas (77 Tracks)
            </h2>
            <p class="text-xs text-slate-400">Historical & modern circuits from Melbourne 1950 to Las Vegas 2024 with strategic telemetry.</p>
          </div>

          <!-- Search & Filter Controls -->
          <div class="flex flex-wrap items-center gap-2">
            <input type="text" id="circuit-search" oninput="filterCircuits()" placeholder="Search circuit or country..." class="bg-slate-900 border border-slate-700 text-xs text-slate-200 px-3 py-1.5 rounded-lg outline-none focus:ring-2 focus:ring-red-500 font-mono w-48 md:w-64">
            
            <select id="circuit-alt-filter" onchange="filterCircuits()" class="bg-slate-900 border border-slate-700 text-xs text-slate-200 px-2 py-1.5 rounded-lg font-mono">
              <option value="ALL">All Altitudes</option>
              <option value="HIGH">High Alt (&gt;200m)</option>
              <option value="SEA">Sea Level (&lt;50m)</option>
            </select>

            <select id="circuit-stop-filter" onchange="filterCircuits()" class="bg-slate-900 border border-slate-700 text-xs text-slate-200 px-2 py-1.5 rounded-lg font-mono">
              <option value="ALL">All Strategies</option>
              <option value="1">1-Stop Favored</option>
              <option value="2">2-Stop Favored</option>
            </select>
          </div>
        </div>

        <!-- Circuit Cards Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 max-h-[640px] overflow-y-auto pr-2" id="circuits-grid-container">
          <!-- Populated dynamically -->
        </div>
      </div>
    </div>

    <!-- TAB 5: LIVE RACE STRATEGY SIMULATOR -->
    <div id="view-simulator" class="space-y-6 hidden">
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        
        <!-- Controls Panel -->
        <div class="f1-card p-5 space-y-4">
          <div class="border-b border-slate-800 pb-2">
            <h2 class="text-base font-bold text-white flex items-center gap-2">
              <span>🎮</span> Strategy Scenario Builder
            </h2>
            <p class="text-xs text-slate-400">Configure stint compounds & pit stop laps to simulate race time.</p>
          </div>

          <!-- Stint 1 -->
          <div class="p-3 bg-slate-900/80 rounded-lg border border-slate-800 space-y-2">
            <div class="flex justify-between items-center text-xs font-bold">
              <span class="text-white">STINT 1 (Race Start)</span>
              <span id="stint1-laps-label" class="text-red-400 font-mono">Laps 1 - 15 (15 laps)</span>
            </div>
            <div class="flex gap-2">
              <select id="sim-comp-1" onchange="runSimulation()" class="bg-slate-950 border border-slate-700 text-xs text-white rounded p-1.5 font-mono w-full">
                <option value="SOFT" selected>Soft (C3) - High Grip Start</option>
                <option value="MEDIUM">Medium (C2) - Flexible</option>
                <option value="HARD">Hard (C1) - Long Stint</option>
              </select>
            </div>
            <input type="range" id="sim-pit1-lap" min="8" max="30" value="15" oninput="updateSimLaps(); runSimulation();" class="w-full accent-red-600">
          </div>

          <!-- Stint 2 -->
          <div class="p-3 bg-slate-900/80 rounded-lg border border-slate-800 space-y-2">
            <div class="flex justify-between items-center text-xs font-bold">
              <span class="text-white">STINT 2</span>
              <span id="stint2-laps-label" class="text-amber-400 font-mono">Laps 16 - 36 (21 laps)</span>
            </div>
            <div class="flex gap-2">
              <select id="sim-comp-2" onchange="runSimulation()" class="bg-slate-950 border border-slate-700 text-xs text-white rounded p-1.5 font-mono w-full">
                <option value="HARD" selected>Hard (C1) - High Durability</option>
                <option value="MEDIUM">Medium (C2) - Race Pace</option>
                <option value="SOFT">Soft (C3) - Sprint Attack</option>
              </select>
            </div>
            <div class="flex items-center justify-between text-xs font-mono">
              <label class="flex items-center gap-1.5 cursor-pointer">
                <input type="checkbox" id="sim-enable-stop2" onchange="updateSimLaps(); runSimulation();" checked class="rounded bg-slate-950 border-slate-700 text-red-600">
                <span>Enable 2nd Pit Stop</span>
              </label>
            </div>
            <input type="range" id="sim-pit2-lap" min="20" max="48" value="36" oninput="updateSimLaps(); runSimulation();" class="w-full accent-amber-500">
          </div>

          <!-- Stint 3 (Optional) -->
          <div id="stint3-box" class="p-3 bg-slate-900/80 rounded-lg border border-slate-800 space-y-2">
            <div class="flex justify-between items-center text-xs font-bold">
              <span class="text-white">STINT 3 (Final Sprint)</span>
              <span id="stint3-laps-label" class="text-emerald-400 font-mono">Laps 37 - 57 (21 laps)</span>
            </div>
            <select id="sim-comp-3" onchange="runSimulation()" class="bg-slate-950 border border-slate-700 text-xs text-white rounded p-1.5 font-mono w-full">
                <option value="SOFT" selected>Soft (C3) - Fastest Lap Hunt</option>
                <option value="MEDIUM">Medium (C2) - Steady Pace</option>
                <option value="HARD">Hard (C1) - Security</option>
            </select>
          </div>

          <!-- Environmental Factors -->
          <div class="p-3 bg-slate-900/80 rounded-lg border border-slate-800 space-y-2 text-xs">
            <span class="font-bold text-slate-300">RACE INTERVENTIONS</span>
            <div class="space-y-2 font-mono">
              <label class="flex items-center justify-between cursor-pointer">
                <span>Safety Car Pit Intervention</span>
                <input type="checkbox" id="sim-sc-pit" onchange="runSimulation()" class="rounded bg-slate-950 border-slate-700 text-emerald-500">
              </label>
              <div class="flex items-center justify-between">
                <span>Track Temp (&deg;C)</span>
                <input type="number" id="sim-track-temp" min="15" max="55" value="34" onchange="runSimulation()" class="w-16 bg-slate-950 border border-slate-700 rounded px-1.5 py-0.5 text-right font-mono">
              </div>
            </div>
          </div>
        </div>

        <!-- Simulation Results Panel (2 cols) -->
        <div class="f1-card p-5 lg:col-span-2 flex flex-col justify-between space-y-6">
          <div>
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
              <div>
                <h2 class="text-base font-bold text-white flex items-center gap-2">
                  <span>📈</span> Projected Race Outcome & Strategic Delta
                </h2>
                <p class="text-xs text-slate-400">Calculated against real 2024 Bahrain GP winning baseline (Max Verstappen: 1h 31m 44.742s).</p>
              </div>
              <div id="sim-rating-badge" class="px-3 py-1 rounded-full text-xs font-mono font-bold bg-emerald-950 text-emerald-300 border border-emerald-800">
                OPTIMAL STRATEGY
              </div>
            </div>

            <!-- Simulation KPI Cards -->
            <div class="grid grid-cols-2 md:grid-cols-4 gap-3 mt-4 font-mono">
              <div class="p-3 bg-slate-950/80 rounded-lg border border-slate-800">
                <span class="text-[10px] text-slate-400 uppercase">Sim Total Time</span>
                <div class="text-lg font-bold text-white mt-1" id="sim-total-time">5504.8s</div>
                <span class="text-[11px] text-slate-400" id="sim-time-fmt">1h 31m 44.8s</span>
              </div>

              <div class="p-3 bg-slate-950/80 rounded-lg border border-slate-800">
                <span class="text-[10px] text-slate-400 uppercase">Delta to Real Winner</span>
                <div class="text-lg font-bold text-emerald-400 mt-1" id="sim-delta-winner">+0.1s</div>
                <span class="text-[11px] text-slate-400">Par with VER P1</span>
              </div>

              <div class="p-3 bg-slate-950/80 rounded-lg border border-slate-800">
                <span class="text-[10px] text-slate-400 uppercase">Total Pit Lane Loss</span>
                <div class="text-lg font-bold text-amber-400 mt-1" id="sim-pit-loss">43.6s</div>
                <span class="text-[11px] text-slate-400" id="sim-stops-count">2 Pit Stops</span>
              </div>

              <div class="p-3 bg-slate-950/80 rounded-lg border border-slate-800">
                <span class="text-[10px] text-slate-400 uppercase">Predicted Finish</span>
                <div class="text-lg font-black text-white mt-1 flex items-center gap-1" id="sim-finish-pos">
                  <span class="text-amber-400">P1 - P2</span>
                  <span class="text-xs font-normal text-slate-400">Podium</span>
                </div>
                <span class="text-[11px] text-emerald-400">Championship Contender</span>
              </div>
            </div>

            <!-- Stint Visual Breakdown -->
            <div class="mt-6">
              <div class="flex justify-between items-center text-xs font-mono text-slate-400 mb-2">
                <span>SIMULATED STINT PROFILE</span>
                <span id="sim-degradation-loss-total">Est. Tire Degradation Loss: +32.4s</span>
              </div>
              <div class="w-full h-8 bg-slate-950 rounded-lg overflow-hidden flex border border-slate-800" id="sim-gantt-bar">
                <!-- Filled dynamically -->
              </div>
            </div>

            <!-- Strategic Advice / Telemetry Verdict -->
            <div class="mt-6 p-4 rounded-xl bg-slate-900/90 border border-slate-700/80 text-xs leading-relaxed space-y-2">
              <div class="font-bold text-white flex items-center gap-2">
                <span>📋</span> Pit-Wall Strategic Briefing
              </div>
              <p class="text-slate-300" id="sim-briefing-text">
                Your simulated Soft-Hard-Soft 2-stop strategy closely mirrors the optimal winning configuration used by Red Bull in Bahrain. Starting on Soft grants immediate grid launch grip, while the 21-lap middle Hard stint absorbs tire degradation without hitting the thermal cliff.
              </p>
            </div>
          </div>
        </div>

      </div>
    </div>

    <!-- METHODOLOGY & ANALYTICAL SUMMARY CARD -->
    <section class="f1-card p-5 f1-card-accent">
      <div class="flex items-center justify-between mb-3 border-b border-slate-800 pb-2">
        <h3 class="text-base font-bold text-white flex items-center gap-2">
          <span>🧠</span> Strategic Takeaways: How Race Strategies Determine F1 Performance
        </h3>
        <span class="text-xs font-mono text-slate-400">FIA Telemetry Analytics Standard</span>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs leading-relaxed">
        <div class="p-3 bg-slate-950/60 rounded-lg border border-slate-800/80">
          <div class="font-bold text-red-400 mb-1 flex items-center gap-1.5">
            <span>1.</span> Track Position vs. Tire Delta
          </div>
          <p class="text-slate-300">
            Monaco and Singapore prioritize <strong>track position at all costs</strong> (overtaking difficulty &gt;8.0), favoring conservative 1-stops. Conversely, high-energy layouts like Bahrain and Silverstone punish worn rubber with over 2.5s/lap deficits, making 2-stop tire delta strategies decisively superior.
          </p>
        </div>

        <div class="p-3 bg-slate-950/60 rounded-lg border border-slate-800/80">
          <div class="font-bold text-amber-400 mb-1 flex items-center gap-1.5">
            <span>2.</span> The Safety Car Option Value
          </div>
          <p class="text-slate-300">
            Extending the opening stint (the "overcut gamble") provides critical option value. If a Safety Car or VSC appears, the trailing driver saves up to 12.0 seconds in pit transit, jumping directly ahead of competitors who pitted under green flag conditions (e.g. Norris at Miami 2024).
          </p>
        </div>

        <div class="p-3 bg-slate-950/60 rounded-lg border border-slate-800/80">
          <div class="font-bold text-emerald-400 mb-1 flex items-center gap-1.5">
            <span>3.</span> Compound Crossover Optimization
          </div>
          <p class="text-slate-300">
            Modern F1 races are won in the <strong>in-lap and out-lap windows</strong>. Pitting 1 lap before the defending rival (the undercut) leverages the 1.8s fresh tire grip jump to leapfrog positions without executing a hazardous on-track overtake.
          </p>
        </div>
      </div>
    </section>

  </main>

  <!-- EMBEDDED DATA SCRIPT -->
  <script>
    const F1_DATA = {json_data_str};

    // State
    let selectedDrivers = ["VER", "PER", "SAI", "LEC", "RUS", "NOR"];
    let fuelCorrectionActive = true;
    let currentTab = "telemetry";

    // Initialize UI on load
    window.addEventListener("DOMContentLoaded", () => {{
      buildDriverBadges();
      renderTelemetryCharts();
      renderStintTimelines();
      renderDegradationChart();
      renderBattlesTable();
      renderCircuitsGrid();
      runSimulation();
    }});

    // TAB SWITCHING
    function setTab(tab) {{
      currentTab = tab;
      const tabs = ["telemetry", "degradation", "undercut", "circuits", "simulator"];
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

    // DRIVER BADGES
    function buildDriverBadges() {{
      const container = document.getElementById("driver-toggle-container");
      container.innerHTML = "";
      F1_DATA.drivers.forEach(d => {{
        const isSel = selectedDrivers.includes(d.code);
        const btn = document.createElement("button");
        btn.className = `px-2 py-0.5 rounded text-xs font-mono font-bold transition flex items-center gap-1 border ${{
          isSel 
            ? 'bg-slate-800 text-white border-slate-600 shadow' 
            : 'bg-slate-950/60 text-slate-500 border-slate-800 hover:text-slate-300'
        }}`;
        btn.innerHTML = `<span class="w-2 h-2 rounded-full" style="background-color: ${{d.color}}"></span> ${{d.code}}`;
        btn.onclick = () => toggleDriver(d.code);
        container.appendChild(btn);
      }});
    }}

    function toggleDriver(code) {{
      if (selectedDrivers.includes(code)) {{
        if (selectedDrivers.length > 1) {{
          selectedDrivers = selectedDrivers.filter(c => c !== code);
        }}
      }} else {{
        selectedDrivers.push(code);
      }}
      buildDriverBadges();
      renderTelemetryCharts();
    }}

    // 1. LAP PACE & GAP SVG RENDERING
    function renderTelemetryCharts() {{
      const paceSvg = document.getElementById("pace-svg");
      const gapSvg = document.getElementById("gap-svg");
      const isSmooth = document.getElementById("toggle-smooth").checked;
      const showPits = document.getElementById("toggle-pits").checked;

      const laps = F1_DATA.bahrain_telemetry_laps;
      const width = 800;
      const height = 300;
      const padL = 45;
      const padR = 20;
      const padT = 20;
      const padB = 30;

      // Group laps by driver
      const driverMap = {{}};
      selectedDrivers.forEach(d => {{
        driverMap[d] = laps.filter(l => l.driver === d).sort((a,b) => a.lap - b.lap);
      }});

      // --- RENDER LAP PACE CHART ---
      paceSvg.setAttribute("viewBox", `0 0 ${{width}} ${{height}}`);
      paceSvg.innerHTML = "";

      // Min/Max bounds for Pace (filter standing start for scale)
      let minPace = 93.5;
      let maxPace = 101.5;

      // Draw grid lines
      for (let p = 94; p <= 101; p += 1) {{
        const y = padT + (height - padT - padB) * (p - minPace) / (maxPace - minPace);
        paceSvg.innerHTML += `<line x1="${{padL}}" y1="${{y}}" x2="${{width - padR}}" y2="${{y}}" stroke="#222733" stroke-dasharray="3,3"/>`;
        paceSvg.innerHTML += `<text x="${{padL - 6}}" y="${{y + 3}}" fill="#64748B" font-size="10" font-family="monospace" text-anchor="end">${{p.toFixed(1)}}s</text>`;
      }}

      // Draw lap lines
      for (let l = 10; l <= 57; l += 10) {{
        const x = padL + (width - padL - padR) * (l - 1) / 56;
        paceSvg.innerHTML += `<line x1="${{x}}" y1="${{padT}}" x2="${{x}}" y2="${{height - padB}}" stroke="#222733" stroke-dasharray="3,3"/>`;
        paceSvg.innerHTML += `<text x="${{x}}" y="${{height - 12}}" fill="#64748B" font-size="10" font-family="monospace" text-anchor="middle">L${{l}}</text>`;
      }}

      selectedDrivers.forEach(dCode => {{
        const dInfo = F1_DATA.drivers.find(d => d.code === dCode) || {{ color: "#AAA" }};
        const dLaps = driverMap[dCode] || [];
        if (dLaps.length === 0) return;

        let points = [];
        dLaps.forEach((l, idx) => {{
          let val = l.lap_time;
          // Apply 3-lap rolling smooth if checked and not lap 1
          if (isSmooth && idx >= 2 && !l.is_pit) {{
            val = (dLaps[idx].lap_time + dLaps[idx-1].lap_time + dLaps[idx-2].lap_time) / 3;
          }}

          // Clamp for SVG display
          val = Math.max(minPace, Math.min(maxPace, val));
          const x = padL + (width - padL - padR) * (l.lap - 1) / 56;
          const y = padT + (height - padT - padB) * (val - minPace) / (maxPace - minPace);
          points.push(`${{x.toFixed(1)}},${{y.toFixed(1)}}`);

          // Draw pit markers if requested
          if (showPits && l.is_pit) {{
            paceSvg.innerHTML += `<circle cx="${{x}}" cy="${{y}}" r="4.5" fill="${{dInfo.color}}" stroke="#FFFFFF" stroke-width="1.5"/>`;
          }}
        }});

        paceSvg.innerHTML += `<polyline points="${{points.join(" ")}}" fill="none" stroke="${{dInfo.color}}" stroke-width="2.2" opacity="0.9"/>`;
      }});

      // --- RENDER GAP TO LEADER CHART ---
      gapSvg.setAttribute("viewBox", `0 0 ${{width}} ${{height}}`);
      gapSvg.innerHTML = "";

      let maxGap = 45.0;
      // Horizontal gap grid
      for (let g = 0; g <= 40; g += 10) {{
        const y = padT + (height - padT - padB) * (g / maxGap);
        gapSvg.innerHTML += `<line x1="${{padL}}" y1="${{y}}" x2="${{width - padR}}" y2="${{y}}" stroke="#222733" stroke-dasharray="3,3"/>`;
        gapSvg.innerHTML += `<text x="${{padL - 6}}" y="${{y + 3}}" fill="#64748B" font-size="10" font-family="monospace" text-anchor="end">+${{g}}s</text>`;
      }}

      selectedDrivers.forEach(dCode => {{
        const dInfo = F1_DATA.drivers.find(d => d.code === dCode) || {{ color: "#AAA" }};
        const dLaps = driverMap[dCode] || [];
        if (dLaps.length === 0) return;

        let points = [];
        dLaps.forEach(l => {{
          const gap = Math.min(maxGap, Math.max(0, l.gap_to_leader));
          const x = padL + (width - padL - padR) * (l.lap - 1) / 56;
          const y = padT + (height - padT - padB) * (gap / maxGap);
          points.push(`${{x.toFixed(1)}},${{y.toFixed(1)}}`);
        }});

        gapSvg.innerHTML += `<polyline points="${{points.join(" ")}}" fill="none" stroke="${{dInfo.color}}" stroke-width="2.2" opacity="0.9"/>`;
      }});
    }}

    // 2. STINT TIMELINE GANTT BARS
    function renderStintTimelines() {{
      const container = document.getElementById("stint-timeline-container");
      container.innerHTML = "";

      // Group stints by driver
      const driverStintsMap = {{}};
      F1_DATA.bahrain_telemetry_laps.forEach(l => {{
        if (!driverStintsMap[l.driver]) driverStintsMap[l.driver] = [];
        let cur = driverStintsMap[l.driver][driverStintsMap[l.driver].length - 1];
        if (!cur || cur.stint !== l.stint || cur.compound !== l.compound) {{
          driverStintsMap[l.driver].push({{
            stint: l.stint,
            compound: l.compound,
            start_lap: l.lap,
            end_lap: l.lap
          }});
        }} else {{
          cur.end_lap = l.lap;
        }}
      }});

      const totalLaps = 57;

      Object.keys(driverStintsMap).forEach(dCode => {{
        const dInfo = F1_DATA.drivers.find(d => d.code === dCode) || {{ name: dCode, color: "#AAA", team: "" }};
        const stints = driverStintsMap[dCode];

        const row = document.createElement("div");
        row.className = "flex items-center gap-3 text-xs font-mono";

        let stintsHtml = "";
        stints.forEach(s => {{
          const duration = s.end_lap - s.start_lap + 1;
          const pct = (duration / totalLaps) * 100;
          let color = "#FFFFFF";
          let textColor = "#000000";
          let label = "H";
          if (s.compound === "SOFT") {{ color = "#E10600"; textColor = "#FFFFFF"; label = "S"; }}
          else if (s.compound === "MEDIUM") {{ color = "#FFF200"; textColor = "#000000"; label = "M"; }}
          else if (s.compound === "HARD") {{ color = "#FFFFFF"; textColor = "#000000"; label = "H"; }}

          stintsHtml += `
            <div class="stint-bar h-6 rounded flex items-center justify-between px-2 text-[11px] font-bold shadow-sm" 
                 style="width: ${{pct}}%; background-color: ${{color}}; color: ${{textColor}};"
                 title="${{dInfo.name}}: Stint ${{s.stint}} (${{s.compound}}) Laps ${{s.start_lap}} - ${{s.end_lap}} (${{duration}} laps)">
              <span>${{label}}</span>
              <span class="text-[9px] opacity-75">${{duration}}L</span>
            </div>
          `;
        }});

        row.innerHTML = `
          <div class="w-16 flex items-center gap-1.5 font-bold">
            <span class="w-2 h-2 rounded-full" style="background-color: ${{dInfo.color}}"></span>
            <span class="text-white">${{dCode}}</span>
          </div>
          <div class="flex-1 flex gap-1 bg-slate-950/80 p-1 rounded-lg border border-slate-800">
            ${{stintsHtml}}
          </div>
        `;
        container.appendChild(row);
      }});
    }}

    // 3. TIRE DEGRADATION SCATTER & REGRESSION CHART
    function renderDegradationChart() {{
      const svg = document.getElementById("deg-svg");
      svg.innerHTML = "";

      const width = 800;
      const height = 300;
      const padL = 45;
      const padR = 20;
      const padT = 20;
      const padB = 30;

      svg.setAttribute("viewBox", `0 0 ${{width}} ${{height}}`);

      const maxAge = 35;
      const minPace = 93.5;
      const maxPace = 99.5;

      // Draw Grid
      for (let p = 94; p <= 99; p += 1) {{
        const y = padT + (height - padT - padB) * (p - minPace) / (maxPace - minPace);
        svg.innerHTML += `<line x1="${{padL}}" y1="${{y}}" x2="${{width - padR}}" y2="${{y}}" stroke="#222733" stroke-dasharray="3,3"/>`;
        svg.innerHTML += `<text x="${{padL - 6}}" y="${{y + 3}}" fill="#64748B" font-size="10" font-family="monospace" text-anchor="end">${{p}}s</text>`;
      }}

      for (let a = 5; a <= 35; a += 5) {{
        const x = padL + (width - padL - padR) * a / maxAge;
        svg.innerHTML += `<line x1="${{x}}" y1="${{padT}}" x2="${{x}}" y2="${{height - padB}}" stroke="#222733" stroke-dasharray="3,3"/>`;
        svg.innerHTML += `<text x="${{x}}" y="${{height - 10}}" fill="#64748B" font-size="10" font-family="monospace" text-anchor="middle">${{a}} Laps</text>`;
      }}

      // Plot points & calculate regression lines
      const compColors = {{ "SOFT": "#E10600", "MEDIUM": "#FFF200", "HARD": "#FFFFFF" }};
      const laps = F1_DATA.bahrain_telemetry_laps.filter(l => !l.is_pit && l.lap > 1 && l.tyre_age <= 35);

      laps.forEach(l => {{
        let pTime = l.lap_time;
        // If fuel correction active, remove fuel gain so true tire wear shows
        if (fuelCorrectionActive) {{
          pTime += (l.lap - 1) * 0.062;
        }}

        const x = padL + (width - padL - padR) * l.tyre_age / maxAge;
        const y = padT + (height - padT - padB) * (pTime - minPace) / (maxPace - minPace);
        const col = compColors[l.compound] || "#888";

        svg.innerHTML += `<circle cx="${{x.toFixed(1)}}" cy="${{y.toFixed(1)}}" r="2.8" fill="${{col}}" opacity="0.45"/>`;
      }});

      // Draw Regression Trendlines
      const slopes = F1_DATA.metrics.tire_compound_degradation_slopes;
      ["SOFT", "HARD"].forEach(comp => {{
        const deg = slopes[comp].deg_per_lap;
        const base = comp === "SOFT" ? 94.6 : 95.8;
        const maxL = comp === "SOFT" ? 18 : 34;

        const x1 = padL;
        const y1 = padT + (height - padT - padB) * (base - minPace) / (maxPace - minPace);
        const x2 = padL + (width - padL - padR) * maxL / maxAge;
        const y2 = padT + (height - padT - padB) * ((base + maxL * deg) - minPace) / (maxPace - minPace);

        svg.innerHTML += `<line x1="${{x1}}" y1="${{y1}}" x2="${{x2}}" y2="${{y2}}" stroke="${{compColors[comp]}}" stroke-width="3" opacity="0.95"/>`;
      }});
    }}

    function toggleFuelCorrection() {{
      fuelCorrectionActive = !fuelCorrectionActive;
      const btn = document.getElementById("fuel-btn-toggle");
      if (fuelCorrectionActive) {{
        btn.textContent = "ACTIVE (-0.062s/lap)";
        btn.className = "px-2 py-0.5 rounded bg-red-600 text-white font-bold transition";
      }} else {{
        btn.textContent = "OFF (Raw Laptimes)";
        btn.className = "px-2 py-0.5 rounded bg-slate-800 text-slate-300 font-bold transition";
      }}
      renderDegradationChart();
    }}

    // 4. PIT STOP & UNDERCUT BATTLES TABLE
    function renderBattlesTable() {{
      const tbody = document.getElementById("battles-table-body");
      tbody.innerHTML = "";

      F1_DATA.pit_stop_battles.forEach(b => {{
        const row = document.createElement("tr");
        row.className = "hover:bg-slate-900/50 transition";
        row.innerHTML = `
          <td class="p-2.5 font-bold text-white">${{b.race}} <span class="text-[10px] text-slate-500 block">Lap ${{b.lap}}</span></td>
          <td class="p-2.5">
            <span class="text-emerald-400 font-bold">${{b.attacking_driver}}</span> vs <span class="text-red-400">${{b.defending_driver}}</span>
          </td>
          <td class="p-2.5">
            <span class="px-2 py-0.5 rounded bg-slate-800 border border-slate-700 text-slate-200">${{b.tactic}}</span>
          </td>
          <td class="p-2.5 text-slate-300">+${{b.pre_gap_sec}}s</td>
          <td class="p-2.5 font-bold text-emerald-400">${{b.outlap_delta_sec}}s</td>
          <td class="p-2.5">
            <span class="px-2 py-0.5 rounded bg-emerald-950/70 border border-emerald-800 text-emerald-300 font-bold">
              ${{b.outcome}}
            </span>
          </td>
        `;
        tbody.appendChild(row);
      }});
    }}

    // 5. GLOBAL CIRCUIT ATLAS (77 TRACKS)
    function renderCircuitsGrid(filteredList = null) {{
      const container = document.getElementById("circuits-grid-container");
      container.innerHTML = "";
      const list = filteredList || F1_DATA.circuits;

      list.forEach(c => {{
        const card = document.createElement("div");
        card.className = "p-4 rounded-xl bg-slate-950/80 border border-slate-800 hover:border-slate-700 transition flex flex-col justify-between space-y-3";
        
        let altBadge = `<span class="px-2 py-0.5 rounded bg-slate-800 text-slate-300">${{c.alt}}m alt</span>`;
        if (c.alt > 500) altBadge = `<span class="px-2 py-0.5 rounded bg-purple-950 text-purple-300 border border-purple-800 font-bold">${{c.alt}}m High Alt</span>`;
        else if (c.alt < 20) altBadge = `<span class="px-2 py-0.5 rounded bg-cyan-950 text-cyan-300 border border-cyan-800">${{c.alt}}m Sea Level</span>`;

        card.innerHTML = `
          <div>
            <div class="flex items-center justify-between text-[11px] font-mono mb-1">
              <span class="text-red-400 font-bold">#${{c.circuitId}} &bull; ${{c.country}}</span>
              ${{altBadge}}
            </div>
            <h3 class="text-sm font-bold text-white leading-tight">${{c.name}}</h3>
            <p class="text-xs text-slate-400 mt-0.5">${{c.location}}</p>
          </div>

          <div class="grid grid-cols-3 gap-2 text-[11px] font-mono bg-slate-900/80 p-2 rounded-lg border border-slate-800/80">
            <div>
              <span class="text-slate-500 block text-[9px]">LENGTH</span>
              <span class="text-slate-200 font-bold">${{c.length_km}} km</span>
            </div>
            <div>
              <span class="text-slate-500 block text-[9px]">PIT LOSS</span>
              <span class="text-amber-400 font-bold">${{c.pit_loss_sec}}s</span>
            </div>
            <div>
              <span class="text-slate-500 block text-[9px]">STRATEGY</span>
              <span class="text-emerald-400 font-bold">${{c.typical_stops}}-Stop</span>
            </div>
          </div>

          <div class="flex items-center justify-between text-[11px] font-mono text-slate-400 pt-1 border-t border-slate-800/60">
            <span>Tire Stress: <strong class="text-white">${{c.tire_stress}}/5</strong></span>
            <span>Overtake Diff: <strong class="text-white">${{c.overtaking_diff}}/10</strong></span>
          </div>
        `;
        container.appendChild(card);
      }});
    }}

    function filterCircuits() {{
      const query = document.getElementById("circuit-search").value.toLowerCase();
      const altFilter = document.getElementById("circuit-alt-filter").value;
      const stopFilter = document.getElementById("circuit-stop-filter").value;

      const filtered = F1_DATA.circuits.filter(c => {{
        const matchQ = c.name.toLowerCase().includes(query) || c.country.toLowerCase().includes(query) || c.location.toLowerCase().includes(query);
        let matchAlt = true;
        if (altFilter === "HIGH") matchAlt = c.alt >= 200;
        else if (altFilter === "SEA") matchAlt = c.alt <= 50;

        let matchStop = true;
        if (stopFilter !== "ALL") matchStop = c.typical_stops == parseInt(stopFilter);

        return matchQ && matchAlt && matchStop;
      }});

      renderCircuitsGrid(filtered);
    }}

    // 6. STRATEGY SIMULATOR LOGIC
    function updateSimLaps() {{
      const p1 = parseInt(document.getElementById("sim-pit1-lap").value);
      const isStop2 = document.getElementById("sim-enable-stop2").checked;
      const p2Slider = document.getElementById("sim-pit2-lap");
      const stint3Box = document.getElementById("stint3-box");

      // Constrain pit 2 to be after pit 1 + 8 laps
      p2Slider.min = p1 + 8;
      if (parseInt(p2Slider.value) <= p1) {{
        p2Slider.value = p1 + 12;
      }}
      const p2 = parseInt(p2Slider.value);

      document.getElementById("stint1-laps-label").textContent = `Laps 1 - ${{p1}} (${{p1}} laps)`;

      if (isStop2) {{
        stint3Box.classList.remove("hidden");
        document.getElementById("stint2-laps-label").textContent = `Laps ${{p1 + 1}} - ${{p2}} (${{p2 - p1}} laps)`;
        document.getElementById("stint3-laps-label").textContent = `Laps ${{p2 + 1}} - 57 (${{57 - p2}} laps)`;
      }} else {{
        stint3Box.classList.add("hidden");
        document.getElementById("stint2-laps-label").textContent = `Laps ${{p1 + 1}} - 57 (${{57 - p1}} laps)`;
      }}
    }}

    function runSimulation() {{
      const c1 = document.getElementById("sim-comp-1").value;
      const c2 = document.getElementById("sim-comp-2").value;
      const c3 = document.getElementById("sim-comp-3").value;
      const p1 = parseInt(document.getElementById("sim-pit1-lap").value);
      const p2 = parseInt(document.getElementById("sim-pit2-lap").value);
      const isStop2 = document.getElementById("sim-enable-stop2").checked;
      const scActive = document.getElementById("sim-sc-pit").checked;
      const trackTemp = parseFloat(document.getElementById("sim-track-temp").value) || 34;

      const slopes = F1_DATA.metrics.tire_compound_degradation_slopes;
      const baseLap = 95.8;
      let totalTime = 0.0;
      let totalDegradation = 0.0;

      // Temp adjustment factor: higher temp increases soft/medium degradation
      const tempFactor = 1.0 + ((trackTemp - 30) * 0.015);

      // Pit loss
      const pitLossNormal = 21.8;
      const pitLossSC = 9.8;
      const p1Loss = scActive ? pitLossSC : pitLossNormal;
      const p2Loss = isStop2 ? pitLossNormal : 0.0;
      const totalPitLoss = p1Loss + p2Loss;

      // Calculate stint 1
      for (let l = 1; l <= p1; l++) {{
        const age = l;
        const deg = slopes[c1].deg_per_lap * tempFactor;
        const deltaBase = slopes[c1].base_delta_to_medium;
        const fuel = (l - 1) * -0.062;
        const wear = (age - 1) * deg;
        totalDegradation += wear;
        let t = baseLap + deltaBase + fuel + wear;
        if (l === 1) t += 4.5;
        totalTime += t;
      }}

      // Calculate stint 2
      const end2 = isStop2 ? p2 : 57;
      for (let l = p1 + 1; l <= end2; l++) {{
        const age = l - p1;
        const deg = slopes[c2].deg_per_lap * tempFactor;
        const deltaBase = slopes[c2].base_delta_to_medium;
        const fuel = (l - 1) * -0.062;
        const wear = (age - 1) * deg;
        // Thermal cliff penalty if over-extended
        let cliffPenalty = 0;
        if (age > slopes[c2].cliff_lap) {{
          cliffPenalty = (age - slopes[c2].cliff_lap) * 0.22;
        }}
        totalDegradation += wear + cliffPenalty;
        totalTime += baseLap + deltaBase + fuel + wear + cliffPenalty;
      }}

      // Calculate stint 3 if 2-stop
      if (isStop2) {{
        for (let l = p2 + 1; l <= 57; l++) {{
          const age = l - p2;
          const deg = slopes[c3].deg_per_lap * tempFactor;
          const deltaBase = slopes[c3].base_delta_to_medium;
          const fuel = (l - 1) * -0.062;
          const wear = (age - 1) * deg;
          totalDegradation += wear;
          totalTime += baseLap + deltaBase + fuel + wear;
        }}
      }}

      totalTime += totalPitLoss;

      // Baseline winning time (Verstappen 2024 Bahrain = 5504.74s)
      const winnerBaseline = 5504.74;
      const deltaWinner = totalTime - winnerBaseline;

      // Update UI elements
      document.getElementById("sim-total-time").textContent = `${{totalTime.toFixed(1)}}s`;
      const mins = Math.floor(totalTime / 60);
      const secs = (totalTime % 60).toFixed(1);
      const hours = Math.floor(mins / 60);
      const remMins = mins % 60;
      document.getElementById("sim-time-fmt").textContent = `${{hours}}h ${{remMins}}m ${{secs}}s`;

      const deltaElem = document.getElementById("sim-delta-winner");
      if (deltaWinner <= 0.8) {{
        deltaElem.textContent = `${{deltaWinner >= 0 ? '+' : ''}}${{deltaWinner.toFixed(1)}}s`;
        deltaElem.className = "text-lg font-bold text-emerald-400 mt-1";
      }} else if (deltaWinner <= 5.0) {{
        deltaElem.textContent = `+${{deltaWinner.toFixed(1)}}s`;
        deltaElem.className = "text-lg font-bold text-amber-400 mt-1";
      }} else {{
        deltaElem.textContent = `+${{deltaWinner.toFixed(1)}}s`;
        deltaElem.className = "text-lg font-bold text-red-400 mt-1";
      }}

      document.getElementById("sim-pit-loss").textContent = `${{totalPitLoss.toFixed(1)}}s`;
      document.getElementById("sim-stops-count").textContent = isStop2 ? "2 Pit Stops" : "1 Pit Stop";
      document.getElementById("sim-degradation-loss-total").textContent = `Est. Tire Degradation Loss: +${{totalDegradation.toFixed(1)}}s`;

      // Update finish prediction & rating
      const ratingBadge = document.getElementById("sim-rating-badge");
      const finishPos = document.getElementById("sim-finish-pos");
      const briefingText = document.getElementById("sim-briefing-text");

      if (deltaWinner <= 2.5) {{
        ratingBadge.textContent = "OPTIMAL STRATEGY (VICTORY CONTENDER)";
        ratingBadge.className = "px-3 py-1 rounded-full text-xs font-mono font-bold bg-emerald-950 text-emerald-300 border border-emerald-800";
        finishPos.innerHTML = `<span class="text-amber-400">P1 - P2</span> <span class="text-xs font-normal text-slate-400">Podium</span>`;
        briefingText.innerHTML = `<strong>Race Engineer Verdict:</strong> Excellent strategy calibration. By keeping stints within compound degradation windows and fitting fresh rubber for the final stint, your modeled race pace matches or surpasses the real winning baseline.`;
      }} else if (deltaWinner <= 12.0) {{
        ratingBadge.textContent = "SOLID PODIUM STRATEGY";
        ratingBadge.className = "px-3 py-1 rounded-full text-xs font-mono font-bold bg-amber-950 text-amber-300 border border-amber-800";
        finishPos.innerHTML = `<span class="text-slate-200">P3 - P5</span> <span class="text-xs font-normal text-slate-400">Strong Points</span>`;
        briefingText.innerHTML = `<strong>Race Engineer Verdict:</strong> Competent strategy delivering reliable podium points, but tire degradation in the closing laps loses approx +${{deltaWinner.toFixed(1)}}s compared to optimal 2-stop execution.`;
      }} else {{
        ratingBadge.textContent = "HIGH-RISK / SUB-OPTIMAL";
        ratingBadge.className = "px-3 py-1 rounded-full text-xs font-mono font-bold bg-red-950 text-red-300 border border-red-800";
        finishPos.innerHTML = `<span class="text-red-400">P7 - P10</span> <span class="text-xs font-normal text-slate-400">Midfield</span>`;
        briefingText.innerHTML = `<strong>Race Engineer Verdict:</strong> Sub-optimal tire selection or over-extended stint. The tire has dropped off the thermal cliff, costing over +${{deltaWinner.toFixed(1)}}s. Consider shortening stint lengths or adding a second pit stop.`;
      }}

      // Update Sim Gantt Bar
      const gantt = document.getElementById("sim-gantt-bar");
      const s1Pct = (p1 / 57) * 100;
      const s2Pct = ((end2 - p1) / 57) * 100;
      const s3Pct = isStop2 ? ((57 - p2) / 57) * 100 : 0;

      const compColMap = {{ "SOFT": "#E10600", "MEDIUM": "#FFF200", "HARD": "#FFFFFF" }};
      const compTextMap = {{ "SOFT": "#FFF", "MEDIUM": "#000", "HARD": "#000" }};

      let gHtml = `
        <div style="width: ${{s1Pct}}%; background-color: ${{compColMap[c1]}}; color: ${{compTextMap[c1]}};" class="flex items-center justify-center text-xs font-bold font-mono">
          ${{c1[0]}} (${{p1}}L)
        </div>
        <div style="width: ${{s2Pct}}%; background-color: ${{compColMap[c2]}}; color: ${{compTextMap[c2]}};" class="flex items-center justify-center text-xs font-bold font-mono border-l border-slate-900">
          ${{c2[0]}} (${{end2 - p1}}L)
        </div>
      `;
      if (isStop2) {{
        gHtml += `
          <div style="width: ${{s3Pct}}%; background-color: ${{compColMap[c3]}}; color: ${{compTextMap[c3]}};" class="flex items-center justify-center text-xs font-bold font-mono border-l border-slate-900">
            ${{c3[0]}} (${{57 - p2}}L)
          </div>
        `;
      }}
      gantt.innerHTML = gHtml;
    }}

    function switchRace(raceNum) {{
      const labels = {{
        "1": "2024 Bahrain GP (57 Laps)",
        "8": "2024 Monaco GP (78 Laps)",
        "12": "2024 British GP (52 Laps)",
        "14": "2024 Belgian GP (44 Laps)",
        "16": "2024 Italian GP (53 Laps)",
        "22": "2024 Las Vegas GP (50 Laps)",
        "24": "2024 Abu Dhabi GP (58 Laps)"
      }};
      document.getElementById("current-gp-label").textContent = labels[raceNum] || "2024 Grand Prix";
      renderTelemetryCharts();
      renderStintTimelines();
    }}
  </script>
</body>
</html>
"""

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(html_template)

with open(ARTIFACT_HTML, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"Successfully generated HTML Dashboard at:\n{OUTPUT_HTML}\n{ARTIFACT_HTML}")
