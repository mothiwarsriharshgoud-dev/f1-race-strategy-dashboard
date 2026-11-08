import json
import os

DATA_PATH = "C:/Users/Main User/.gemini/antigravity/scratch/f1-race-strategy-dashboard/data/f1_strategy_dataset.json"
OUTPUT_HTML = "C:/Users/Main User/.gemini/antigravity/scratch/f1-race-strategy-dashboard/index.html"
ARTIFACT_HTML = "C:/Users/Main User/.gemini/antigravity/brain/bb0fc362-bdeb-4a83-b7c8-80ce516a46a3/f1_race_strategy_dashboard.html"
WIDGET_HTML = "C:/Users/Main User/.gemini/antigravity/brain/bb0fc362-bdeb-4a83-b7c8-80ce516a46a3/f1_race_strategy_widget.html"

with open(DATA_PATH, "r", encoding="utf-8") as f:
    f1_data = json.load(f)

json_data_str = json.dumps(f1_data)

# Let's write the complete master HTML
master_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Formula 1 Race Telemetry & Strategy Analytics Platform | Project 32</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Titillium+Web:ital,wght@0,300;0,400;0,600;0,700;0,900;1,600&family=JetBrains+Mono:wght@400;600;700;800&display=swap');
    
    :root {{
      --f1-red: #E10600;
      --f1-dark: #090B10;
      --f1-panel: #111520;
      --f1-card: #151A27;
      --f1-border: #242C3F;
      --f1-text: #F3F4F6;
      --f1-muted: #9CA3AF;
      --f1-yellow: #FFF200;
      --f1-drs: #00FF7F;
      --f1-cyan: #00E5FF;
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
      background: #090B10;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #2A3347;
      border-radius: 4px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #E10600;
    }}

    /* Carbon Fiber Weave Texture */
    .carbon-bg {{
      background-color: #090B10;
      background-image: 
        linear-gradient(45deg, #11141C 25%, transparent 25%), 
        linear-gradient(-45deg, #11141C 25%, transparent 25%), 
        linear-gradient(45deg, transparent 75%, #11141C 75%), 
        linear-gradient(-45deg, transparent 75%, #11141C 75%);
      background-size: 8px 8px;
      background-position: 0 0, 0 4px, 4px -4px, -4px 0px;
    }}

    .glass-card {{
      background: linear-gradient(135deg, rgba(20, 26, 40, 0.92) 0%, rgba(14, 18, 28, 0.96) 100%);
      border: 1px solid var(--f1-border);
      border-radius: 16px;
      box-shadow: 0 12px 32px rgba(0, 0, 0, 0.55);
      backdrop-filter: blur(14px);
    }}

    .glass-card-accent {{
      border-top: 3px solid var(--f1-red);
    }}

    .badge-soft {{ background-color: rgba(225, 6, 0, 0.25); color: #FF4D4D; border: 1px solid #E10600; }}
    .badge-medium {{ background-color: rgba(255, 242, 0, 0.25); color: #FFF200; border: 1px solid #FFD700; }}
    .badge-hard {{ background-color: rgba(255, 255, 255, 0.22); color: #FFFFFF; border: 1px solid #E5E7EB; }}
    .badge-inter {{ background-color: rgba(0, 210, 106, 0.25); color: #00D26A; border: 1px solid #00D26A; }}
    .badge-wet {{ background-color: rgba(0, 160, 222, 0.25); color: #38BDF8; border: 1px solid #00A0DE; }}

    .tab-btn.active {{
      background: linear-gradient(90deg, rgba(225, 6, 0, 0.3) 0%, rgba(225, 6, 0, 0.05) 100%);
      border-bottom: 3px solid var(--f1-red);
      color: #FFFFFF;
      font-weight: 700;
    }}

    /* Glow pulse for active telemetry */
    @keyframes pulse-red {{
      0%, 100% {{ box-shadow: 0 0 15px rgba(225, 6, 0, 0.6); }}
      50% {{ box-shadow: 0 0 5px rgba(225, 6, 0, 0.2); }}
    }}
    .glow-f1-red {{
      animation: pulse-red 2s infinite ease-in-out;
    }}

    @keyframes pulse-drs {{
      0%, 100% {{ box-shadow: 0 0 16px rgba(0, 255, 127, 0.8); }}
      50% {{ box-shadow: 0 0 6px rgba(0, 255, 127, 0.3); }}
    }}
    .glow-drs {{
      animation: pulse-drs 1s infinite ease-in-out;
    }}
  </style>
</head>
<body class="carbon-bg min-h-screen text-slate-100 antialiased selection:bg-red-600 selection:text-white">

  <!-- TOP HEADER / PIT-WALL HUD -->
  <header class="border-b border-slate-800 bg-slate-950/90 sticky top-0 z-50 backdrop-blur-md">
    <div class="max-w-7xl mx-auto px-4 py-3 flex flex-wrap items-center justify-between gap-4">
      <div class="flex items-center gap-3">
        <div class="bg-red-600 text-white font-black px-3 py-1 rounded text-xl tracking-wider flex items-center gap-1.5 shadow-lg shadow-red-900/60">
          <span>F1</span>
          <span class="text-xs bg-black/50 px-1.5 py-0.5 rounded font-mono">P32</span>
        </div>
        <div>
          <div class="flex items-center gap-2">
            <h1 class="text-lg md:text-xl font-black tracking-tight text-white flex items-center gap-2">
              Formula 1 Race Telemetry & Strategy Analytics Platform
            </h1>
            <span class="text-xs bg-emerald-950 text-emerald-400 border border-emerald-700 px-2.5 py-0.5 rounded-full font-mono flex items-center gap-1 font-semibold">
              <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span> LIVE MOTION HUD
            </span>
          </div>
          <p class="text-xs text-slate-400 font-medium">
            Core Question: <span class="text-red-400 font-semibold italic">"How do race strategies influence Formula 1 performance?"</span>
          </p>
        </div>
      </div>

      <!-- Quick Session Controls -->
      <div class="flex items-center gap-2.5">
        <button id="btn-sound-toggle" onclick="toggleEngineSound()" class="px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-700 hover:border-slate-500 text-xs font-mono text-slate-300 transition flex items-center gap-1.5">
          <span id="sound-icon">🔇</span>
          <span id="sound-text">Sound: OFF</span>
        </button>

        <select id="quick-circuit-select" onchange="switchCircuitFromSelect(this.value)" class="bg-slate-900 border border-slate-700 text-slate-200 text-xs rounded-lg px-3 py-1.5 font-medium focus:ring-2 focus:ring-red-500 outline-none font-mono">
          <option value="monza">Monza (Temple of Speed) - 🇮🇹</option>
          <option value="silverstone">Silverstone (Copse & Maggotts) - 🇬🇧</option>
          <option value="spa">Spa-Francorchamps (Eau Rouge) - 🇧🇪</option>
          <option value="bahrain">Bahrain (Sakhir Desert) - 🇧🇭</option>
          <option value="monaco">Monaco (Monte-Carlo Hairpin) - 🇲🇨</option>
        </select>
      </div>
    </div>

    <!-- NAVIGATION TABS -->
    <div class="max-w-7xl mx-auto px-4 flex gap-1 overflow-x-auto text-xs font-medium border-t border-slate-800/60">
      <button onclick="setTab('motion-arena')" id="tab-motion-arena" class="tab-btn active px-4 py-2.5 text-slate-300 hover:text-white transition flex items-center gap-1.5 font-bold">
        <span>🏎️</span> Live F1 Motion Arena & Cockpit HUD
      </button>
      <button onclick="setTab('strategy-generator')" id="tab-strategy-generator" class="tab-btn px-4 py-2.5 text-slate-400 hover:text-white transition flex items-center gap-1.5">
        <span>⚡</span> AI Strategy Optimizer (Plan A / B / C)
      </button>
      <button onclick="setTab('telemetry')" id="tab-telemetry" class="tab-btn px-4 py-2.5 text-slate-400 hover:text-white transition flex items-center gap-1.5">
        <span>⏱️</span> Lap Telemetry & Stints
      </button>
      <button onclick="setTab('degradation')" id="tab-degradation" class="tab-btn px-4 py-2.5 text-slate-400 hover:text-white transition flex items-center gap-1.5">
        <span>📉</span> Tire Degradation & Cliffs
      </button>
      <button onclick="setTab('undercut')" id="tab-undercut" class="tab-btn px-4 py-2.5 text-slate-400 hover:text-white transition flex items-center gap-1.5">
        <span>⚔️</span> Undercut Battles & SC Arbitrage
      </button>
      <button onclick="setTab('circuits')" id="tab-circuits" class="tab-btn px-4 py-2.5 text-slate-400 hover:text-white transition flex items-center gap-1.5">
        <span>🌍</span> Global Circuit Atlas (77 Tracks)
      </button>
      <button onclick="setTab('simulator')" id="tab-simulator" class="tab-btn px-4 py-2.5 text-slate-400 hover:text-white transition flex items-center gap-1.5">
        <span>🎮</span> Tactical What-If Simulator
      </button>
    </div>
  </header>

  <!-- MAIN VIEW CONTAINER -->
  <main class="max-w-7xl mx-auto px-4 py-5 space-y-5">

    <!-- KPI STATS STRIP -->
    <section class="grid grid-cols-2 md:grid-cols-5 gap-3">
      <div class="glass-card p-3 border-l-4 border-l-red-500">
        <div class="text-[11px] font-mono text-slate-400 uppercase tracking-wider">Undercut Win Rate</div>
        <div class="text-xl md:text-2xl font-black text-white mt-1 flex items-baseline gap-1">
          <span class="text-red-400">68.4%</span>
          <span class="text-[10px] text-emerald-400 font-mono">+1.74s gap gain</span>
        </div>
        <div class="text-[11px] text-slate-400 mt-0.5">Fresh tire out-lap grip delta</div>
      </div>

      <div class="glass-card p-3 border-l-4 border-l-amber-400">
        <div class="text-[11px] font-mono text-slate-400 uppercase tracking-wider">Safety Car Pit Dividend</div>
        <div class="text-xl md:text-2xl font-black text-white mt-1 flex items-baseline gap-1">
          <span class="text-amber-400">+9.4s - 12.0s</span>
        </div>
        <div class="text-[11px] text-slate-400 mt-0.5">Pit loss drops from 22s to 10s</div>
      </div>

      <div class="glass-card p-3 border-l-4 border-l-emerald-500">
        <div class="text-[11px] font-mono text-slate-400 uppercase tracking-wider">Strategy Win Influence</div>
        <div class="text-xl md:text-2xl font-black text-white mt-1 flex items-baseline gap-1">
          <span class="text-emerald-400">42.8%</span>
          <span class="text-[10px] text-slate-300 font-mono">podiums won</span>
        </div>
        <div class="text-[11px] text-slate-400 mt-0.5">Position gained via pit execution</div>
      </div>

      <div class="glass-card p-3 border-l-4 border-l-blue-500">
        <div class="text-[11px] font-mono text-slate-400 uppercase tracking-wider">1-Stop vs 2-Stop Split</div>
        <div class="text-xl md:text-2xl font-black text-white mt-1 flex items-baseline gap-1">
          <span class="text-blue-400">54.2% / 37.5%</span>
        </div>
        <div class="text-[11px] text-slate-400 mt-0.5">Monza 1-stop vs Bahrain 2-stop</div>
      </div>

      <div class="glass-card p-3 border-l-4 border-l-purple-500 col-span-2 md:col-span-1">
        <div class="text-[11px] font-mono text-slate-400 uppercase tracking-wider">Fuel-Burn Lightening</div>
        <div class="text-xl md:text-2xl font-black text-white mt-1 flex items-baseline gap-1">
          <span class="text-purple-300">-0.062 s/lap</span>
        </div>
        <div class="text-[11px] text-slate-400 mt-0.5">110kg fuel consumption</div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- TAB 1: LIVE F1 MOTION ARENA & COCKPIT HUD  -->
    <!-- ========================================== -->
    <div id="view-motion-arena" class="space-y-4">

      <!-- Interactive Arena Container -->
      <div class="glass-card glass-card-accent p-4 md:p-5 relative overflow-hidden">
        
        <!-- Controls & Livery Toolbar -->
        <div class="flex flex-wrap items-center justify-between gap-3 border-b border-slate-800 pb-3">
          
          <!-- Circuit Selection Buttons -->
          <div class="flex flex-wrap items-center gap-1.5">
            <span class="text-xs font-mono text-slate-400 uppercase tracking-wider mr-1">TRACK:</span>
            <button onclick="setTrack('monza')" id="btn-track-monza" class="px-2.5 py-1 rounded bg-red-600 text-white font-mono text-xs font-bold transition">
              🇮🇹 Monza
            </button>
            <button onclick="setTrack('silverstone')" id="btn-track-silverstone" class="px-2.5 py-1 rounded bg-slate-900 border border-slate-700 text-slate-300 hover:text-white font-mono text-xs transition">
              🇬🇧 Silverstone
            </button>
            <button onclick="setTrack('spa')" id="btn-track-spa" class="px-2.5 py-1 rounded bg-slate-900 border border-slate-700 text-slate-300 hover:text-white font-mono text-xs transition">
              🇧🇪 Spa
            </button>
            <button onclick="setTrack('bahrain')" id="btn-track-bahrain" class="px-2.5 py-1 rounded bg-slate-900 border border-slate-700 text-slate-300 hover:text-white font-mono text-xs transition">
              🇧🇭 Bahrain
            </button>
            <button onclick="setTrack('monaco')" id="btn-track-monaco" class="px-2.5 py-1 rounded bg-slate-900 border border-slate-700 text-slate-300 hover:text-white font-mono text-xs transition">
              🇲🇨 Monaco
            </button>
          </div>

          <!-- Team Livery Selector -->
          <div class="flex items-center gap-1.5">
            <span class="text-xs font-mono text-slate-400 uppercase tracking-wider mr-1">LIVERY:</span>
            <button onclick="setTeam('ferrari')" id="btn-team-ferrari" title="Scuderia Ferrari (Leclerc #16)" class="w-6 h-6 rounded-full bg-[#D40000] border-2 border-white transition transform hover:scale-110"></button>
            <button onclick="setTeam('redbull')" id="btn-team-redbull" title="Red Bull Racing (Verstappen #1)" class="w-6 h-6 rounded-full bg-[#061327] border-2 border-[#FFD700] transition transform hover:scale-110"></button>
            <button onclick="setTeam('mclaren')" id="btn-team-mclaren" title="McLaren (Norris #4)" class="w-6 h-6 rounded-full bg-[#FF8000] border-2 border-slate-600 transition transform hover:scale-110"></button>
            <button onclick="setTeam('mercedes')" id="btn-team-mercedes" title="Mercedes-AMG (Hamilton #44)" class="w-6 h-6 rounded-full bg-[#00A19B] border-2 border-slate-400 transition transform hover:scale-110"></button>
            <button onclick="setTeam('aston')" id="btn-team-aston" title="Aston Martin (Alonso #14)" class="w-6 h-6 rounded-full bg-[#00594F] border-2 border-[#CEDC00] transition transform hover:scale-110"></button>
          </div>

          <!-- Tactical Action Buttons -->
          <div class="flex items-center gap-2">
            <button onclick="triggerBoxBox()" id="btn-box-box" class="px-3.5 py-1.5 rounded-lg bg-amber-600 hover:bg-amber-500 text-white font-mono text-xs font-black tracking-wider flex items-center gap-1.5 shadow-lg shadow-amber-900/40 transition">
              <span>📻</span> BOX BOX (PIT STOP)
            </button>

            <button onclick="toggleMotionSim()" id="btn-sim-pause" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 font-mono text-xs font-bold transition">
              ⏸️ Pause
            </button>

            <div class="flex rounded-lg bg-slate-900 p-0.5 border border-slate-700 text-[11px] font-mono">
              <button onclick="setSpeedMultiplier(1)" id="spd-1" class="px-2 py-0.5 rounded bg-red-600 text-white font-bold">1x</button>
              <button onclick="setSpeedMultiplier(2)" id="spd-2" class="px-2 py-0.5 rounded text-slate-400 hover:text-white">2x</button>
              <button onclick="setSpeedMultiplier(4)" id="spd-4" class="px-2 py-0.5 rounded text-slate-400 hover:text-white">4x</button>
            </div>
          </div>
        </div>

        <!-- LIVE F1 RACING CANVAS VIEWPORT -->
        <div class="relative w-full mt-3 rounded-xl overflow-hidden border border-slate-800 bg-[#0B0E14] shadow-inner">
          
          <!-- Top Canvas Overlay: Track & Sector HUD -->
          <div class="absolute top-3 left-3 z-10 flex flex-wrap items-center gap-2 pointer-events-none">
            <div class="bg-black/75 backdrop-blur-md px-3 py-1.5 rounded-lg border border-slate-700 text-xs font-mono">
              <span class="text-slate-400">CIRCUIT: </span>
              <span id="hud-track-name" class="text-white font-bold">Autodromo Nazionale Monza</span>
            </div>
            <div class="bg-black/75 backdrop-blur-md px-3 py-1.5 rounded-lg border border-slate-700 text-xs font-mono">
              <span class="text-slate-400">LAP: </span>
              <span id="hud-lap-counter" class="text-red-400 font-bold">18 / 53</span>
            </div>
            <div class="bg-black/75 backdrop-blur-md px-3 py-1.5 rounded-lg border border-slate-700 text-xs font-mono flex items-center gap-1.5">
              <span class="text-slate-400">SECTOR: </span>
              <span id="hud-sector-badge" class="px-1.5 py-0.2 rounded bg-purple-950 text-purple-400 font-bold border border-purple-800">S2 PURPLE</span>
            </div>
          </div>

          <!-- Top-Right Canvas Overlay: DRS & Pit Limiter Status -->
          <div class="absolute top-3 right-3 z-10 flex flex-col items-end gap-1.5 pointer-events-none">
            <div id="hud-drs-badge" class="px-3 py-1 rounded-lg bg-slate-900/90 text-slate-400 border border-slate-700 text-xs font-mono font-bold flex items-center gap-1.5">
              <span class="w-2 h-2 rounded-full bg-slate-500"></span> DRS CLOSED
            </div>
            <div id="hud-limiter-badge" class="hidden px-3 py-1 rounded-lg bg-amber-950/90 text-amber-400 border border-amber-600 text-xs font-mono font-black animate-pulse flex items-center gap-1.5">
              <span>⚠️</span> PIT SPEED LIMITER (80 KM/H)
            </div>
          </div>

          <!-- Pit Stop Notification Banner (Triggered during Pit Stop) -->
          <div id="pit-stop-banner" class="hidden absolute inset-0 z-20 bg-black/60 backdrop-blur-sm flex flex-col items-center justify-center pointer-events-none transition">
            <div class="bg-slate-900 border-2 border-amber-500 rounded-2xl p-6 text-center shadow-2xl shadow-amber-900/50 max-w-md w-full mx-4 transform scale-100">
              <div class="text-xs font-mono text-amber-400 tracking-widest uppercase font-bold">● LIVE PIT-WALL EXECUTION</div>
              <div class="text-2xl font-black text-white mt-1">PIT CREW SERVICING CAR</div>
              <div class="text-4xl font-mono font-black text-amber-400 my-2" id="pit-stop-timer">0.00s</div>
              <div class="flex items-center justify-center gap-3 text-xs font-mono text-slate-300">
                <span>Tires: <span class="text-red-400 font-bold">SOFT (C3)</span> $\rightarrow$ <span class="text-white font-bold" id="pit-new-compound">HARD (C1)</span></span>
                <span>•</span>
                <span class="text-emerald-400 font-bold" id="pit-delta-gain">Undercut: +1.84s Target</span>
              </div>
              <div class="w-full bg-slate-800 rounded-full h-2 mt-4 overflow-hidden border border-slate-700">
                <div id="pit-progress-bar" class="bg-amber-500 h-2 rounded-full w-0 transition-all duration-100"></div>
              </div>
            </div>
          </div>

          <!-- The HTML5 Racing Canvas -->
          <canvas id="f1-canvas" class="w-full block" width="1100" height="500"></canvas>
        </div>

        <!-- COCKPIT TELEMETRY INSTRUMENT CLUSTER -->
        <div class="grid grid-cols-2 md:grid-cols-6 gap-3 mt-4">
          
          <!-- Speedometer & Rev Lights -->
          <div class="glass-card p-3 col-span-2 flex flex-col justify-between">
            <div class="flex items-center justify-between border-b border-slate-800 pb-1.5">
              <span class="text-[10px] font-mono text-slate-400 uppercase">F1 TELEMETRY SPEED</span>
              <span class="text-[10px] font-mono text-emerald-400 font-bold" id="tel-drs-status">DRS: CLOSED</span>
            </div>
            
            <!-- LED Rev Indicator Strip (15 LEDs) -->
            <div class="flex items-center justify-between gap-1 my-2 px-1" id="rev-led-bar">
              <!-- Rendered via JS: 5 green, 5 red, 5 purple -->
            </div>

            <div class="flex items-baseline justify-between mt-1">
              <div>
                <span class="text-3xl md:text-4xl font-black font-mono text-white tracking-tight" id="tel-speed">312</span>
                <span class="text-xs font-mono text-slate-400">KM/H</span>
              </div>
              <div class="text-right font-mono">
                <span class="text-xs text-slate-400 block text-[10px]">ENGINE SPEED</span>
                <span class="text-base font-bold text-red-400" id="tel-rpm">13,420 RPM</span>
              </div>
            </div>
          </div>

          <!-- Current Gear & Shift Indicator -->
          <div class="glass-card p-3 flex flex-col items-center justify-center text-center">
            <span class="text-[10px] font-mono text-slate-400 uppercase">TRANSMISSION</span>
            <div class="text-4xl font-black font-mono text-white my-1" id="tel-gear">7</div>
            <span class="text-[10px] font-mono text-slate-400" id="tel-gear-mode">8-SPEED SEAMLESS</span>
          </div>

          <!-- Throttle & Brake Pedals Pressure -->
          <div class="glass-card p-3 flex flex-col justify-between">
            <span class="text-[10px] font-mono text-slate-400 uppercase">PEDAL INPUTS</span>
            <div class="space-y-2 my-1">
              <div>
                <div class="flex justify-between text-[10px] font-mono mb-0.5">
                  <span class="text-emerald-400">THR</span>
                  <span class="text-slate-300 font-bold" id="tel-thr-val">96%</span>
                </div>
                <div class="w-full bg-slate-800 rounded-full h-1.5 overflow-hidden">
                  <div id="tel-thr-bar" class="bg-emerald-500 h-1.5 rounded-full" style="width: 96%"></div>
                </div>
              </div>
              <div>
                <div class="flex justify-between text-[10px] font-mono mb-0.5">
                  <span class="text-red-400">BRK</span>
                  <span class="text-slate-300 font-bold" id="tel-brk-val">0%</span>
                </div>
                <div class="w-full bg-slate-800 rounded-full h-1.5 overflow-hidden">
                  <div id="tel-brk-bar" class="bg-red-500 h-1.5 rounded-full" style="width: 0%"></div>
                </div>
              </div>
            </div>
            <span class="text-[9px] font-mono text-slate-400 text-center">DRIVE-BY-WIRE</span>
          </div>

          <!-- Lateral / Longitudinal G-Force Meter -->
          <div class="glass-card p-3 flex flex-col items-center justify-between">
            <span class="text-[10px] font-mono text-slate-400 uppercase">G-FORCE ACCEL</span>
            <div class="relative w-14 h-14 rounded-full border border-slate-700 bg-slate-950 flex items-center justify-center my-1">
              <div class="absolute w-full h-[1px] bg-slate-800"></div>
              <div class="absolute h-full w-[1px] bg-slate-800"></div>
              <div class="w-6 h-6 rounded-full border border-slate-800"></div>
              <!-- G-Force Dot -->
              <div id="tel-g-dot" class="w-2.5 h-2.5 rounded-full bg-red-500 shadow-md shadow-red-500/80 transition-all duration-75 transform translate-x-1 -translate-y-1"></div>
            </div>
            <div class="text-[10px] font-mono text-slate-300 font-bold" id="tel-g-val">+3.8 G LAT</div>
          </div>

          <!-- Pirelli Tire Heatmap (4 Corners) -->
          <div class="glass-card p-3 flex flex-col justify-between">
            <span class="text-[10px] font-mono text-slate-400 uppercase">TIRE BULK TEMPS</span>
            <div class="grid grid-cols-2 gap-1.5 my-1 text-center font-mono text-[10px]">
              <div class="p-1 rounded bg-slate-900 border border-slate-800" id="temp-fl-box">
                <span class="text-[9px] text-slate-400 block">FL</span>
                <span class="font-bold text-amber-400" id="temp-fl">102&deg;C</span>
              </div>
              <div class="p-1 rounded bg-slate-900 border border-slate-800" id="temp-fr-box">
                <span class="text-[9px] text-slate-400 block">FR</span>
                <span class="font-bold text-amber-400" id="temp-fr">104&deg;C</span>
              </div>
              <div class="p-1 rounded bg-slate-900 border border-slate-800" id="temp-rl-box">
                <span class="text-[9px] text-slate-400 block">RL</span>
                <span class="font-bold text-emerald-400" id="temp-rl">96&deg;C</span>
              </div>
              <div class="p-1 rounded bg-slate-900 border border-slate-800" id="temp-rr-box">
                <span class="text-[9px] text-slate-400 block">RR</span>
                <span class="font-bold text-emerald-400" id="temp-rr">97&deg;C</span>
              </div>
            </div>
            <div class="text-[9px] font-mono text-slate-400 flex justify-between">
              <span>COMPOUND:</span>
              <span id="tel-compound-name" class="text-red-400 font-bold">SOFT (C3)</span>
            </div>
          </div>

        </div>

      </div>

    </div>

    <!-- ========================================== -->
    <!-- TAB 2: AI STRATEGY OPTIMIZER (PLAN A/B/C)  -->
    <!-- ========================================== -->
    <div id="view-strategy-generator" class="hidden space-y-5">
      
      <!-- Generator Configuration Ribbon -->
      <div class="glass-card p-5 glass-card-accent">
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
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-5" id="strategy-plans-container">
        <!-- Rendered dynamically by JS -->
      </div>

      <!-- Pit-Wall Contingency Decision Tree Matrix -->
      <div class="glass-card p-5">
        <h3 class="text-sm font-bold text-white mb-3 flex items-center gap-2">
          <span>📋</span> Pit-Wall Live Tactical Decision Tree
        </h3>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs font-mono">
          <div class="p-3.5 rounded-xl bg-slate-900/90 border border-slate-800 border-l-4 border-l-red-500">
            <span class="text-red-400 font-bold block mb-1">SC / VSC IN PIT WINDOW (Laps 14-26)</span>
            <p class="text-slate-300 text-[11px] leading-relaxed">
              <strong>ACTION: BOX IMMEDIATELY.</strong> Pitting under VSC/SC saves ~10-12s in pit lane loss vs green flag conditions. Switch to C1 Hard tires to run to the checkered flag.
            </p>
          </div>

          <div class="p-3.5 rounded-xl bg-slate-900/90 border border-slate-800 border-l-4 border-l-amber-500">
            <span class="text-amber-400 font-bold block mb-1">GAP TO CAR AHEAD &lt; 1.8 SECONDS</span>
            <p class="text-slate-300 text-[11px] leading-relaxed">
              <strong>ACTION: TRIGGER UNDERCUT.</strong> Box 1-2 laps ahead of rival into clean air. High grip on out-lap (+1.74s) guarantees pit-lane overtake on exit.
            </p>
          </div>

          <div class="p-3.5 rounded-xl bg-slate-900/90 border border-slate-800 border-l-4 border-l-blue-500">
            <span class="text-blue-400 font-bold block mb-1">CAR TRAPPED IN MIDFIELD TRAFFIC TRAIN</span>
            <p class="text-slate-300 text-[11px] leading-relaxed">
              <strong>ACTION: SWITCH TO PLAN C (OVERCUT).</strong> Extend stint in clean air as midfield pits. Exploit aerodynamic wake penalty (-0.75s/lap) hurting rivals in traffic.
            </p>
          </div>
        </div>
      </div>

    </div>

    <!-- ========================================== -->
    <!-- TAB 3: TELEMETRY & LAP PACE EXPLORER       -->
    <!-- ========================================== -->
    <div id="view-telemetry" class="hidden space-y-5">
      <div class="glass-card p-5">
        <div class="flex flex-wrap items-center justify-between border-b border-slate-800 pb-3 gap-3">
          <div>
            <h2 class="text-base font-bold text-white flex items-center gap-2">
              <span>⏱️</span> Grand Prix Lap Telemetry & Stint Evolution
            </h2>
            <p class="text-xs text-slate-400">
              High-resolution lap times corrected for fuel burn lightening vs rubber thermal degradation.
            </p>
          </div>
          <div class="flex items-center gap-2 text-xs font-mono">
            <label class="text-slate-400">SELECT RACE:</label>
            <select id="telemetry-race-select" onchange="renderTelemetryChart(this.value)" class="bg-slate-900 border border-slate-700 text-slate-200 rounded px-2.5 py-1">
              <option value="1">Rd 1: Bahrain GP (Sakhir)</option>
              <option value="6">Rd 6: Miami GP (Miami)</option>
              <option value="8">Rd 8: Monaco GP (Monte Carlo)</option>
              <option value="12">Rd 12: British GP (Silverstone)</option>
              <option value="14">Rd 14: Belgian GP (Spa-Francorchamps)</option>
              <option value="16">Rd 16: Italian GP (Monza)</option>
              <option value="20">Rd 20: Mexico City GP (Hermanos Rodriguez)</option>
              <option value="24">Rd 24: Abu Dhabi GP (Yas Marina)</option>
            </select>
          </div>
        </div>

        <div class="h-80 w-full mt-4">
          <canvas id="telemetryChart"></canvas>
        </div>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- TAB 4: TIRE DEGRADATION MODELING           -->
    <!-- ========================================== -->
    <div id="view-degradation" class="hidden space-y-5">
      <div class="glass-card p-5">
        <h2 class="text-base font-bold text-white flex items-center gap-2 border-b border-slate-800 pb-3">
          <span>📉</span> Pirelli Compound Wear Rates & The Non-Linear Thermal Cliff
        </h2>
        <p class="text-xs text-slate-400 mt-2">
          Mathematical models of rubber wear: Soft (high grip, early cliff), Medium (balanced), and Hard (endurance compound).
        </p>

        <div class="h-80 w-full mt-4">
          <canvas id="degradationChart"></canvas>
        </div>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- TAB 5: UNDERCUT & SAFETY CAR ARBITRAGE     -->
    <!-- ========================================== -->
    <div id="view-undercut" class="hidden space-y-5">
      <div class="glass-card p-5">
        <h2 class="text-base font-bold text-white flex items-center gap-2 border-b border-slate-800 pb-3">
          <span>⚔️</span> Undercut Battles & Safety Car Pit Loss Dividend
        </h2>
        <div class="h-80 w-full mt-4">
          <canvas id="undercutChart"></canvas>
        </div>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- TAB 6: GLOBAL CIRCUIT ATLAS (77 TRACKS)    -->
    <!-- ========================================== -->
    <div id="view-circuits" class="hidden space-y-5">
      <div class="glass-card p-5">
        <div class="flex flex-wrap items-center justify-between border-b border-slate-800 pb-3 gap-3">
          <div>
            <h2 class="text-base font-bold text-white flex items-center gap-2">
              <span>🌍</span> FIA Formula 1 World Circuit Atlas (77 Circuits)
            </h2>
            <p class="text-xs text-slate-400">
              Classified by altitude, downforce requirement, and asphalt abrasiveness.
            </p>
          </div>
          <input type="text" id="circuit-search" placeholder="Search circuit or country..." oninput="filterCircuits()" class="bg-slate-900 border border-slate-700 text-xs text-slate-200 rounded-lg px-3 py-1.5 font-mono focus:ring-2 focus:ring-red-500 outline-none w-56">
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-3 mt-4 max-h-[500px] overflow-y-auto pr-2" id="circuits-grid-container">
          <!-- Dynamically populated -->
        </div>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- TAB 7: WHAT-IF RACE SIMULATOR              -->
    <!-- ========================================== -->
    <div id="view-simulator" class="hidden space-y-5">
      <div class="glass-card p-5">
        <h2 class="text-base font-bold text-white flex items-center gap-2 border-b border-slate-800 pb-3">
          <span>🎮</span> Tactical What-If Pit Lap Simulator
        </h2>
        <p class="text-xs text-slate-400 mt-2">
          Adjust pit stop laps and compound selections to compute projected finish time deltas.
        </p>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mt-4 font-mono text-xs">
          <div>
            <label class="text-slate-400 block mb-1">STINT 1 TIRE COMPOUND</label>
            <select id="sim-stint1-tire" onchange="runCustomSim()" class="w-full bg-slate-900 border border-slate-700 rounded p-2 text-white">
              <option value="medium">Medium (C2) - Recommended</option>
              <option value="soft">Soft (C3) - Aggressive Start</option>
              <option value="hard">Hard (C1) - Reverse Long Stint</option>
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
              <option value="none">No Safety Car (100% Green)</option>
              <option value="lap18">VSC at Lap 18 (+10.5s Dividend)</option>
              <option value="lap25">Full Safety Car at Lap 25 (+12.0s Dividend)</option>
            </select>
          </div>
        </div>

        <div class="mt-4 p-4 rounded-xl bg-slate-900/90 border border-slate-800 flex items-center justify-between font-mono text-xs">
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

    // ==========================================
    // 1. NAVIGATION & TAB SWITCHING
    // ==========================================
    function setTab(tabId) {{
      const tabs = ['motion-arena', 'strategy-generator', 'telemetry', 'degradation', 'undercut', 'circuits', 'simulator'];
      tabs.forEach(t => {{
        const btn = document.getElementById("tab-" + t);
        const view = document.getElementById("view-" + t);
        if (btn) {{
          if (t === tabId) {{
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
          if (t === tabId) view.classList.remove("hidden");
          else view.classList.add("hidden");
        }}
      }});

      if (tabId === 'telemetry') setTimeout(renderTelemetryChart, 100);
      if (tabId === 'degradation') setTimeout(renderDegradationChart, 100);
      if (tabId === 'undercut') setTimeout(renderUndercutChart, 100);
      if (tabId === 'circuits') setTimeout(renderCircuitsGrid, 100);
    }}

    // ==========================================
    // 2. LIVE F1 MOTION ARENA & MOVING F1 CAR
    // ==========================================
    
    // Circuit Layout Coordinates (High Resolution Waypoints)
    const CIRCUITS_PATH = {{
      monza: [
        [150, 420], [750, 420], // Main straight (Rettifilo) - 345 km/h
        [810, 420], [840, 390], [850, 350], [820, 330], [780, 350], // Prima Variante Chicane
        [830, 330], [890, 270], [930, 200], [910, 140], // Curva Grande (Biassono)
        [850, 140], [790, 140], [760, 160], // Variante della Roggia
        [720, 130], [670, 90], [610, 80],  // Lesmo 1 & 2
        [460, 120], [330, 160], // Serraglio curve & straight
        [270, 190], [220, 170], [250, 130], // Variante Ascari
        [210, 240], [150, 330], // Back straight to Parabolica
        [100, 380], [110, 420]  // Curva Alboreto (Parabolica)
      ],
      silverstone: [
        [160, 420], [450, 420], // Hamilton Straight
        [540, 420], [590, 380], // Abbey & Farm
        [640, 330], [600, 280], [520, 280], // Village & The Loop
        [460, 300], [360, 300], // Aintree & Wellington Straight
        [260, 260], [210, 210], // Brooklands & Luffield
        [210, 160], [270, 130], // Woodcote & National Pit Straight
        [370, 130], [480, 130], // Copse entry
        [560, 130], [650, 110], // Copse Corner
        [730, 110], [790, 140], [830, 180], // Maggotts & Becketts
        [850, 230], [810, 260], // Chapel
        [750, 340], [700, 380], // Hangar Straight & Stowe
        [580, 400], [500, 410], // Vale & Club
        [300, 420], [180, 420]
      ],
      spa: [
        [220, 400], [420, 400], // Pit straight
        [480, 400], [530, 370], [510, 330], [460, 340], // La Source Hairpin
        [480, 300], [550, 250], // Downhill to Eau Rouge
        [620, 200], [660, 140], // Raidillon crest
        [730, 120], [860, 120], // Kemmel Straight
        [900, 140], [880, 180], [830, 180], // Les Combes & Malmedy
        [810, 230], [750, 260], // Bruxelles 180 Hairpin
        [700, 280], [670, 320], // Speakers Corner
        [620, 340], [580, 360], // Double Gauche / Pouhon
        [500, 350], [430, 320], // Campus / Stavelot
        [360, 300], [290, 270], // Paul Frere
        [240, 240], [200, 210], // Blanchimont
        [150, 250], [140, 320], // Bus Stop Chicane
        [170, 380], [200, 400]
      ],
      bahrain: [
        [180, 410], [550, 410], // Main Straight
        [620, 410], [660, 370], [630, 330], // Turn 1 Hairpin & Turn 2
        [580, 310], [550, 270], [580, 220], // Turn 3 & 4 uphill
        [650, 200], [740, 180], // Turn 5, 6, 7 chicane
        [800, 200], [830, 250], // Turn 8 Hairpin
        [780, 290], [720, 310], // Turn 9-10 downhill lockup
        [680, 320], [650, 300], // Back straight to Turn 11
        [550, 260], [450, 220], // Turn 11, 12 fast sweeping right
        [380, 220], [320, 240], // Turn 13
        [260, 310], [200, 380], // Turn 14-15 onto main straight
        [160, 410]
      ],
      monaco: [
        [240, 420], [520, 420], // Boulevard Albert 1er
        [580, 420], [620, 380], // Sainte Devote
        [640, 330], [670, 270], // Beau Rivage climb
        [680, 220], [640, 180], // Massenet & Casino Square
        [580, 160], [530, 180], // Mirabeau Haute
        [480, 190], [450, 210], [470, 230], // Fairmont Hairpin
        [520, 240], [570, 250], // Mirabeau Bas & Portier
        [640, 270], [720, 300], // The Tunnel
        [760, 340], [730, 370], [680, 360], // Nouvelle Chicane
        [620, 350], [560, 340], // Tabac
        [500, 330], [450, 320], [420, 350], [390, 340], // Swimming Pool Chicane
        [340, 350], [290, 370], [260, 390], // La Rascasse & Anthony Noghes
        [220, 420]
      ]
    }};

    // Team Livery Definitions
    const TEAMS = {{
      ferrari: {{ name: 'Ferrari', color: '#D40000', accent: '#FFFFFF', rim: '#FFD700', driver: 'Charles Leclerc #16' }},
      redbull: {{ name: 'Red Bull', color: '#061327', accent: '#E10600', rim: '#FFD700', driver: 'Max Verstappen #1' }},
      mclaren: {{ name: 'McLaren', color: '#FF8000', accent: '#00D2BE', rim: '#1E2024', driver: 'Lando Norris #4' }},
      mercedes: {{ name: 'Mercedes', color: '#00A19B', accent: '#C0C0C0', rim: '#111111', driver: 'Lewis Hamilton #44' }},
      aston: {{ name: 'Aston Martin', color: '#00594F', accent: '#CEDC00', rim: '#111111', driver: 'Fernando Alonso #14' }}
    }};

    // Tire Compound Definitions
    const COMPOUNDS = {{
      soft: {{ name: 'SOFT (C3)', color: '#FF1801', wearRate: 1.8 }},
      medium: {{ name: 'MEDIUM (C2)', color: '#FFF200', wearRate: 1.0 }},
      hard: {{ name: 'HARD (C1)', color: '#FFFFFF', wearRate: 0.6 }}
    }};

    // Motion State
    let currentTrackKey = 'monza';
    let currentTeamKey = 'ferrari';
    let currentCompoundKey = 'soft';
    let simPaused = false;
    let simSpeedMultiplier = 1;
    let soundEnabled = false;

    // Simulation Coordinates & Telemetry
    let splinePoints = [];
    let carProgress = 0; // 0 to 1 along track
    let currentSpeed = 160; // km/h
    let currentRPM = 10500;
    let currentGear = 5;
    let currentThrottle = 80;
    let currentBrake = 0;
    let currentSteer = 0;
    let isDRSActive = false;
    let isPitLimiterActive = false;
    let pitStopInProgress = false;
    let inPitLane = false;
    let currentLap = 18;
    let maxLaps = 53;
    let sparks = [];

    // Catmull-Rom Spline Interpolator
    function buildSpline(pts, samplesPerSeg = 35) {{
      const n = pts.length;
      const result = [];
      for (let i = 0; i < n; i++) {{
        const p0 = pts[(i - 1 + n) % n];
        const p1 = pts[i];
        const p2 = pts[(i + 1) % n];
        const p3 = pts[(i + 2) % n];

        for (let s = 0; s < samplesPerSeg; s++) {{
          const t = s / samplesPerSeg;
          const t2 = t * t;
          const t3 = t2 * t;

          const x = 0.5 * ((2 * p1[0]) + (-p0[0] + p2[0]) * t + (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * t2 + (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * t3);
          const y = 0.5 * ((2 * p1[1]) + (-p0[1] + p2[1]) * t + (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * t2 + (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * t3);
          
          const dx = 0.5 * ((-p0[0] + p2[0]) + 2 * (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * t + 3 * (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * t2);
          const dy = 0.5 * ((-p0[1] + p2[1]) + 2 * (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * t + 3 * (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * t2);

          const heading = Math.atan2(dy, dx);
          const speedFactor = Math.hypot(dx, dy);

          result.push({{ x, y, dx, dy, heading, speedFactor }});
        }}
      }}

      // Calculate localized curvature
      const len = result.length;
      for (let i = 0; i < len; i++) {{
        const prev = result[(i - 1 + len) % len];
        const next = result[(i + 1) % len];
        let dHeading = next.heading - prev.heading;
        while (dHeading > Math.PI) dHeading -= 2 * Math.PI;
        while (dHeading < -Math.PI) dHeading += 2 * Math.PI;
        result[i].curvature = Math.abs(dHeading);
      }}

      return result;
    }}

    // Setup Track
    function setTrack(trackKey) {{
      currentTrackKey = trackKey;
      const rawPts = CIRCUITS_PATH[trackKey] || CIRCUITS_PATH.monza;
      splinePoints = buildSpline(rawPts);
      carProgress = 0;
      
      const trackNames = {{
        monza: 'Autodromo Nazionale Monza (53 Laps)',
        silverstone: 'Silverstone Circuit (52 Laps)',
        spa: 'Circuit de Spa-Francorchamps (44 Laps)',
        bahrain: 'Bahrain International Circuit (57 Laps)',
        monaco: 'Circuit de Monaco (78 Laps)'
      }};
      document.getElementById('hud-track-name').textContent = trackNames[trackKey] || trackKey;

      ['monza', 'silverstone', 'spa', 'bahrain', 'monaco'].forEach(k => {{
        const b = document.getElementById('btn-track-' + k);
        if (b) {{
          if (k === trackKey) {{
            b.classList.remove('bg-slate-900', 'text-slate-300');
            b.classList.add('bg-red-600', 'text-white', 'font-bold');
          }} else {{
            b.classList.remove('bg-red-600', 'text-white', 'font-bold');
            b.classList.add('bg-slate-900', 'text-slate-300');
          }}
        }}
      }});

      const select = document.getElementById('quick-circuit-select');
      if (select) select.value = trackKey;
    }}

    function switchCircuitFromSelect(val) {{
      setTrack(val);
    }}

    // Setup Team Livery
    function setTeam(teamKey) {{
      currentTeamKey = teamKey;
      ['ferrari', 'redbull', 'mclaren', 'mercedes', 'aston'].forEach(k => {{
        const b = document.getElementById('btn-team-' + k);
        if (b) {{
          if (k === teamKey) b.style.transform = 'scale(1.25)';
          else b.style.transform = 'scale(1.0)';
        }}
      }});
    }}

    // Controls
    function toggleMotionSim() {{
      simPaused = !simPaused;
      const b = document.getElementById('btn-sim-pause');
      if (b) b.textContent = simPaused ? '▶️ Resume' : '⏸️ Pause';
    }}

    function setSpeedMultiplier(mult) {{
      simSpeedMultiplier = mult;
      [1, 2, 4].forEach(m => {{
        const b = document.getElementById('spd-' + m);
        if (b) {{
          if (m === mult) {{
            b.classList.remove('text-slate-400');
            b.classList.add('bg-red-600', 'text-white', 'font-bold');
          }} else {{
            b.classList.remove('bg-red-600', 'text-white', 'font-bold');
            b.classList.add('text-slate-400');
          }}
        }}
      }});
    }}

    // Pit Stop Trigger & Execution
    function triggerBoxBox() {{
      if (pitStopInProgress) return;
      pitStopInProgress = true;
      inPitLane = true;
      isPitLimiterActive = true;

      const limiterBadge = document.getElementById('hud-limiter-badge');
      if (limiterBadge) limiterBadge.classList.remove('hidden');

      const banner = document.getElementById('pit-stop-banner');
      if (banner) banner.classList.remove('hidden');

      let timerVal = 0;
      const timerEl = document.getElementById('pit-stop-timer');
      const progressEl = document.getElementById('pit-progress-bar');
      
      const interval = setInterval(() => {{
        timerVal += 0.05;
        if (timerEl) timerEl.textContent = timerVal.toFixed(2) + 's';
        if (progressEl) progressEl.style.width = Math.min(100, (timerVal / 2.14) * 100) + '%';

        if (timerVal >= 2.14) {{
          clearInterval(interval);
          currentCompoundKey = (currentCompoundKey === 'soft') ? 'hard' : 'soft';
          document.getElementById('tel-compound-name').textContent = COMPOUNDS[currentCompoundKey].name;
          document.getElementById('tel-compound-name').style.color = COMPOUNDS[currentCompoundKey].color;

          setTimeout(() => {{
            if (banner) banner.classList.add('hidden');
            if (limiterBadge) limiterBadge.classList.add('hidden');
            isPitLimiterActive = false;
            inPitLane = false;
            pitStopInProgress = false;
            currentLap++;
            document.getElementById('hud-lap-counter').textContent = currentLap + ' / ' + maxLaps;
          }}, 500);
        }}
      }}, 50);
    }}

    // Audio Engine (Web Audio API Synthesizer)
    let audioCtx = null;
    let engineOsc = null;
    let engineGain = null;

    function toggleEngineSound() {{
      soundEnabled = !soundEnabled;
      const bText = document.getElementById('sound-text');
      const bIcon = document.getElementById('sound-icon');
      if (soundEnabled) {{
        initAudio();
        if (bText) bText.textContent = 'Engine: ON';
        if (bIcon) bIcon.textContent = '🔊';
      }} else {{
        if (engineGain) engineGain.gain.setValueAtTime(0, audioCtx.currentTime);
        if (bText) bText.textContent = 'Sound: OFF';
        if (bIcon) bIcon.textContent = '🔇';
      }}
    }}

    function initAudio() {{
      if (!audioCtx) {{
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        engineOsc = audioCtx.createOscillator();
        engineGain = audioCtx.createGain();

        engineOsc.type = 'sawtooth';
        engineOsc.frequency.setValueAtTime(110, audioCtx.currentTime);
        engineGain.gain.setValueAtTime(0.03, audioCtx.currentTime);

        const filter = audioCtx.createBiquadFilter();
        filter.type = 'lowpass';
        filter.frequency.setValueAtTime(1600, audioCtx.currentTime);

        engineOsc.connect(filter);
        filter.connect(engineGain);
        engineGain.connect(audioCtx.destination);
        engineOsc.start();
      }} else {{
        engineGain.gain.setValueAtTime(0.03, audioCtx.currentTime);
      }}
    }}

    function updateAudio(rpm, throttle) {{
      if (soundEnabled && audioCtx && engineOsc && engineGain) {{
        const targetFreq = 80 + (rpm / 15000) * 310;
        engineOsc.frequency.setTargetAtTime(targetFreq, audioCtx.currentTime, 0.05);
        const targetVol = 0.015 + (throttle / 100) * 0.04;
        engineGain.gain.setTargetAtTime(targetVol, audioCtx.currentTime, 0.05);
      }}
    }}

    // LED Rev Lights Generator
    function initRevLights() {{
      const bar = document.getElementById('rev-led-bar');
      if (!bar) return;
      bar.innerHTML = '';
      for (let i = 0; i < 15; i++) {{
        const led = document.createElement('div');
        led.id = 'led-' + i;
        led.className = 'w-2 h-2.5 rounded-sm bg-slate-800 transition-colors duration-75';
        bar.appendChild(led);
      }}
    }}

    function updateRevLights(rpm) {{
      const maxRpm = 14500;
      const minRpm = 6000;
      const ratio = Math.max(0, Math.min(1, (rpm - minRpm) / (maxRpm - minRpm)));
      const activeLeds = Math.floor(ratio * 15);

      for (let i = 0; i < 15; i++) {{
        const led = document.getElementById('led-' + i);
        if (!led) continue;
        if (i < activeLeds) {{
          if (i < 5) led.style.backgroundColor = '#00FF7F'; // Green
          else if (i < 10) led.style.backgroundColor = '#E10600'; // Red
          else led.style.backgroundColor = '#00E5FF'; // Blue/Purple rev limiter
        }} else {{
          led.style.backgroundColor = '#1E2433';
        }}
      }}
    }}

    // Main Canvas Render Loop
    function renderMotionLoop() {{
      const canvas = document.getElementById('f1-canvas');
      if (!canvas || splinePoints.length === 0) {{
        requestAnimationFrame(renderMotionLoop);
        return;
      }}
      const ctx = canvas.getContext('2d');
      const w = canvas.width;
      const h = canvas.height;

      ctx.clearRect(0, 0, w, h);

      // 1. Draw Asphalt Track Bed & Kerbs
      ctx.save();
      ctx.lineCap = 'round';
      ctx.lineJoin = 'round';

      // Outer gravel/run-off border
      ctx.lineWidth = 44;
      ctx.strokeStyle = '#161B26';
      ctx.beginPath();
      for (let i = 0; i < splinePoints.length; i++) {{
        const p = splinePoints[i];
        if (i === 0) ctx.moveTo(p.x, p.y);
        else ctx.lineTo(p.x, p.y);
      }}
      ctx.closePath();
      ctx.stroke();

      // Main Dark Asphalt Surface
      ctx.lineWidth = 36;
      ctx.strokeStyle = '#10141D';
      ctx.beginPath();
      for (let i = 0; i < splinePoints.length; i++) {{
        const p = splinePoints[i];
        if (i === 0) ctx.moveTo(p.x, p.y);
        else ctx.lineTo(p.x, p.y);
      }}
      ctx.closePath();
      ctx.stroke();

      // Racing Groove Wear (Dark rubber line)
      ctx.lineWidth = 14;
      ctx.strokeStyle = '#0B0D13';
      ctx.beginPath();
      for (let i = 0; i < splinePoints.length; i++) {{
        const p = splinePoints[i];
        if (i === 0) ctx.moveTo(p.x, p.y);
        else ctx.lineTo(p.x, p.y);
      }}
      ctx.closePath();
      ctx.stroke();

      // DRS Zone Highlighting (Main straight section)
      const drsStartIdx = Math.floor(splinePoints.length * 0.02);
      const drsEndIdx = Math.floor(splinePoints.length * 0.22);
      ctx.lineWidth = 4;
      ctx.setLineDash([8, 8]);
      ctx.strokeStyle = '#00FF7F';
      ctx.beginPath();
      for (let i = drsStartIdx; i < drsEndIdx; i++) {{
        const p = splinePoints[i];
        if (i === drsStartIdx) ctx.moveTo(p.x, p.y);
        else ctx.lineTo(p.x, p.y);
      }}
      ctx.stroke();
      ctx.setLineDash([]);

      // Start/Finish Line
      const pStart = splinePoints[0];
      const pNext = splinePoints[1];
      const normAng = pStart.heading + Math.PI / 2;
      const sfX1 = pStart.x + Math.cos(normAng) * 18;
      const sfY1 = pStart.y + Math.sin(normAng) * 18;
      const sfX2 = pStart.x - Math.cos(normAng) * 18;
      const sfY2 = pStart.y - Math.sin(normAng) * 18;
      ctx.lineWidth = 5;
      ctx.strokeStyle = '#FFFFFF';
      ctx.beginPath();
      ctx.moveTo(sfX1, sfY1);
      ctx.lineTo(sfX2, sfY2);
      ctx.stroke();

      ctx.restore();

      // 2. Physical Motion Update
      if (!simPaused) {{
        const ptIndex = Math.floor(carProgress * splinePoints.length);
        const curPt = splinePoints[ptIndex] || splinePoints[0];
        const curvature = curPt.curvature || 0.01;

        // Pit Lane or Normal Track Logic
        if (isPitLimiterActive) {{
          currentSpeed = 80;
          currentRPM = 5200;
          currentGear = 2;
          currentThrottle = 20;
          currentBrake = 0;
          isDRSActive = false;
        }} else {{
          // DRS Detection on Main Straight
          if (ptIndex >= drsStartIdx && ptIndex <= drsEndIdx) {{
            isDRSActive = true;
          }} else {{
            isDRSActive = false;
          }}

          // Cornering vs Straight physics
          if (curvature > 0.045) {{
            // Heavy Braking Zone & Sharp Chicane
            currentThrottle = 5;
            currentBrake = 95;
            currentSpeed = Math.max(90, currentSpeed - 8.5 * simSpeedMultiplier);
            currentGear = (currentSpeed < 120) ? 2 : 3;
            currentRPM = 7500 + (currentSpeed % 40) * 140;
            currentSteer = 0.35;
          }} else if (curvature > 0.02) {{
            // Medium Corner
            currentThrottle = 65;
            currentBrake = 10;
            currentSpeed = Math.max(160, Math.min(230, currentSpeed + 1.2 * simSpeedMultiplier));
            currentGear = (currentSpeed < 190) ? 4 : 5;
            currentRPM = 9800 + (currentSpeed % 40) * 110;
            currentSteer = 0.18;
          }} else {{
            // Full Throttle Straight (DRS Boost)
            currentThrottle = 100;
            currentBrake = 0;
            const topSpeedTarget = isDRSActive ? 352 : 335;
            currentSpeed = Math.min(topSpeedTarget, currentSpeed + 3.8 * simSpeedMultiplier);
            if (currentSpeed > 310) currentGear = 8;
            else if (currentSpeed > 270) currentGear = 7;
            else if (currentSpeed > 230) currentGear = 6;
            else currentGear = 5;
            currentRPM = 11200 + (currentSpeed % 40) * 85;
            currentSteer = 0;

            // Titanium skid sparks at high speeds (>300 km/h)
            if (currentSpeed > 295 && Math.random() < 0.6) {{
              sparks.push({{
                x: curPt.x - Math.cos(curPt.heading) * 18 + (Math.random() - 0.5) * 6,
                y: curPt.y - Math.sin(curPt.heading) * 18 + (Math.random() - 0.5) * 6,
                vx: -Math.cos(curPt.heading) * (2 + Math.random() * 4) + (Math.random() - 0.5) * 2,
                vy: -Math.sin(curPt.heading) * (2 + Math.random() * 4) + (Math.random() - 0.5) * 2,
                life: 1.0,
                color: '#FFD700'
              }});
            }}
          }}
        }}

        // Progress increment proportional to speed
        const progressIncrement = (currentSpeed / 340) * 0.0022 * simSpeedMultiplier;
        carProgress = (carProgress + progressIncrement) % 1;

        // Lap update on wrap
        if (carProgress < progressIncrement) {{
          if (!pitStopInProgress) {{
            currentLap = (currentLap % maxLaps) + 1;
            document.getElementById('hud-lap-counter').textContent = currentLap + ' / ' + maxLaps;
          }}
        }}

        // Audio update
        updateAudio(currentRPM, currentThrottle);
      }}

      // 3. Render Sparks Particle System
      for (let i = sparks.length - 1; i >= 0; i--) {{
        const sp = sparks[i];
        sp.x += sp.vx;
        sp.y += sp.vy;
        sp.life -= 0.045;
        if (sp.life <= 0) {{
          sparks.splice(i, 1);
        }} else {{
          ctx.save();
          ctx.fillStyle = sp.color;
          ctx.shadowColor = '#FF8000';
          ctx.shadowBlur = 8;
          ctx.beginPath();
          ctx.arc(sp.x, sp.y, 1.8 * sp.life, 0, Math.PI * 2);
          ctx.fill();
          ctx.restore();
        }}
      }}

      // 4. Render The High-Fidelity F1 Car
      const ptIndex = Math.floor(carProgress * splinePoints.length);
      const carPt = splinePoints[ptIndex] || splinePoints[0];
      const carX = carPt.x;
      const carY = carPt.y;
      const carHeading = carPt.heading;
      const team = TEAMS[currentTeamKey] || TEAMS.ferrari;
      const compound = COMPOUNDS[currentCompoundKey] || COMPOUNDS.soft;

      ctx.save();
      ctx.translate(carX, carY);
      ctx.rotate(carHeading);

      // DRS Flow Trail if active
      if (isDRSActive) {{
        ctx.save();
        ctx.strokeStyle = 'rgba(0, 255, 127, 0.4)';
        ctx.lineWidth = 14;
        ctx.shadowColor = '#00FF7F';
        ctx.shadowBlur = 15;
        ctx.beginPath();
        ctx.moveTo(-18, 0);
        ctx.lineTo(-45, 0);
        ctx.stroke();
        ctx.restore();
      }}

      // 4 Wheels (Open-Wheel Pirelli Tires)
      const wheelPositions = [
        {{ x: 13, y: -11 }}, // Front Left
        {{ x: 13, y: 11 }},  // Front Right
        {{ x: -14, y: -12 }},// Rear Left
        {{ x: -14, y: 12 }}  // Rear Right
      ];

      wheelPositions.forEach((wp, idx) => {{
        ctx.save();
        ctx.translate(wp.x, wp.y);
        if (idx < 2) ctx.rotate(currentSteer); // Front wheels turn!

        // Tire rubber
        ctx.fillStyle = '#080A0E';
        ctx.fillRect(-6, -3, 12, 6);

        // Glowing Pirelli Compound Sidewall Ring
        ctx.strokeStyle = compound.color;
        ctx.lineWidth = 1.6;
        ctx.beginPath();
        ctx.arc(0, 0, 2.6, 0, Math.PI * 2);
        ctx.stroke();

        // Brake Disc Glowing Red when braking
        if (currentBrake > 40) {{
          ctx.fillStyle = 'rgba(255, 60, 0, 0.85)';
          ctx.shadowColor = '#FF2200';
          ctx.shadowBlur = 6;
          ctx.beginPath();
          ctx.arc(0, 0, 2, 0, Math.PI * 2);
          ctx.fill();
        }}

        ctx.restore();
      }});

      // Aerodynamic Suspension Arms
      ctx.strokeStyle = '#4A5568';
      ctx.lineWidth = 1.2;
      ctx.beginPath();
      ctx.moveTo(8, -5); ctx.lineTo(13, -11);
      ctx.moveTo(8, 5); ctx.lineTo(13, 11);
      ctx.moveTo(-8, -5); ctx.lineTo(-14, -12);
      ctx.moveTo(-8, 5); ctx.lineTo(-14, 12);
      ctx.stroke();

      // Front Wing Assembly
      ctx.fillStyle = team.color;
      ctx.strokeStyle = team.accent;
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.rect(17, -13, 4, 26);
      ctx.fill();
      ctx.stroke();

      // Main F1 Monocoque / Chassis
      ctx.fillStyle = team.color;
      ctx.beginPath();
      ctx.moveTo(19, 0);
      ctx.lineTo(14, -4);
      ctx.lineTo(2, -7);
      ctx.lineTo(-14, -8);
      ctx.lineTo(-18, -4);
      ctx.lineTo(-18, 4);
      ctx.lineTo(-14, 8);
      ctx.lineTo(2, 7);
      ctx.lineTo(14, 4);
      ctx.closePath();
      ctx.fill();
      ctx.strokeStyle = team.accent;
      ctx.lineWidth = 1.2;
      ctx.stroke();

      // Cockpit Opening & Driver Helmet
      ctx.fillStyle = '#05070A';
      ctx.beginPath();
      ctx.ellipse(0, 0, 5, 3.2, 0, 0, Math.PI * 2);
      ctx.fill();

      // Helmet (Team Accent)
      ctx.fillStyle = team.rim;
      ctx.beginPath();
      ctx.arc(-1, 0, 2.2, 0, Math.PI * 2);
      ctx.fill();

      // Titanium Halo Structure
      ctx.strokeStyle = '#CBD5E1';
      ctx.lineWidth = 1.6;
      ctx.beginPath();
      ctx.moveTo(3, 0);
      ctx.lineTo(-2, -3.5);
      ctx.lineTo(-2, 3.5);
      ctx.closePath();
      ctx.stroke();

      // Rear Wing Assembly & DRS Flap
      ctx.fillStyle = team.color;
      ctx.fillRect(-22, -12, 4, 24);
      if (isDRSActive) {{
        // Flap open!
        ctx.strokeStyle = '#00FF7F';
        ctx.lineWidth = 2;
        ctx.strokeRect(-23, -12, 5, 24);
      }} else {{
        ctx.strokeStyle = team.accent;
        ctx.lineWidth = 1;
        ctx.strokeRect(-22, -12, 4, 24);
      }}

      // Rear Blinking Rain/Safety LED
      if (Math.floor(Date.now() / 200) % 2 === 0) {{
        ctx.fillStyle = '#FF0033';
        ctx.shadowColor = '#FF0033';
        ctx.shadowBlur = 8;
        ctx.beginPath();
        ctx.arc(-22, 0, 1.8, 0, Math.PI * 2);
        ctx.fill();
      }}

      ctx.restore();

      // 5. Update Telemetry HUD Elements
      const speedEl = document.getElementById('tel-speed');
      const rpmEl = document.getElementById('tel-rpm');
      const gearEl = document.getElementById('tel-gear');
      const thrVal = document.getElementById('tel-thr-val');
      const thrBar = document.getElementById('tel-thr-bar');
      const brkVal = document.getElementById('tel-brk-val');
      const brkBar = document.getElementById('tel-brk-bar');
      const drsBadge = document.getElementById('hud-drs-badge');
      const drsStatus = document.getElementById('tel-drs-status');
      const gDot = document.getElementById('tel-g-dot');
      const gVal = document.getElementById('tel-g-val');

      if (speedEl) speedEl.textContent = Math.round(currentSpeed);
      if (rpmEl) rpmEl.textContent = Math.round(currentRPM).toLocaleString() + ' RPM';
      if (gearEl) gearEl.textContent = isPitLimiterActive ? 'P' : currentGear;
      if (thrVal) thrVal.textContent = Math.round(currentThrottle) + '%';
      if (thrBar) thrBar.style.width = Math.round(currentThrottle) + '%';
      if (brkVal) brkVal.textContent = Math.round(currentBrake) + '%';
      if (brkBar) brkBar.style.width = Math.round(currentBrake) + '%';

      if (drsBadge) {{
        if (isDRSActive) {{
          drsBadge.className = 'px-3 py-1 rounded-lg bg-emerald-950/90 text-emerald-400 border border-emerald-600 text-xs font-mono font-bold flex items-center gap-1.5 glow-drs';
          drsBadge.innerHTML = '<span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span> DRS ACTIVE';
          if (drsStatus) {{
            drsStatus.textContent = 'DRS: ACTIVE';
            drsStatus.className = 'text-[10px] font-mono text-emerald-400 font-bold';
          }}
        }} else {{
          drsBadge.className = 'px-3 py-1 rounded-lg bg-slate-900/90 text-slate-400 border border-slate-700 text-xs font-mono font-bold flex items-center gap-1.5';
          drsBadge.innerHTML = '<span class="w-2 h-2 rounded-full bg-slate-500"></span> DRS CLOSED';
          if (drsStatus) {{
            drsStatus.textContent = 'DRS: CLOSED';
            drsStatus.className = 'text-[10px] font-mono text-slate-400';
          }}
        }}
      }}

      // G-Force Display
      const curPtCurv = carPt.curvature || 0.01;
      const latG = (curPtCurv * (currentSpeed / 60)).toFixed(1);
      if (gVal) gVal.textContent = `+${{latG}} G LAT`;
      if (gDot) {{
        const offset = Math.min(18, latG * 4);
        gDot.style.transform = `translate(${{offset}}px, ${{currentBrake > 0 ? 8 : -8}}px)`;
      }}

      // Tire Temperatures
      const flTemp = (94 + (currentSpeed / 20) + (currentBrake / 5)).toFixed(0);
      const frTemp = (96 + (currentSpeed / 19) + (currentBrake / 5)).toFixed(0);
      if (document.getElementById('temp-fl')) document.getElementById('temp-fl').innerHTML = flTemp + '&deg;C';
      if (document.getElementById('temp-fr')) document.getElementById('temp-fr').innerHTML = frTemp + '&deg;C';

      updateRevLights(currentRPM);

      requestAnimationFrame(renderMotionLoop);
    }}

    // ==========================================
    // 3. AI STRATEGY GENERATOR (PLAN A / B / C)
    // ==========================================
    function generateF1Strategies() {{
      const cId = parseInt(document.getElementById("gen-circuit").value);
      const grid = parseInt(document.getElementById("gen-grid").value);
      const temp = parseInt(document.getElementById("gen-temp").value);
      const scProb = parseFloat(document.getElementById("gen-sc").value);

      const circuit = F1_DATA.circuits.find(c => c.circuitId === cId) || F1_DATA.circuits[0];
      const laps = circuit.laps || 57;
      const pitLoss = circuit.pit_loss_sec || 22.0;

      const p1_A = Math.round(laps * 0.35);
      const p1_B = Math.round(laps * 0.24);
      const p2_B = Math.round(laps * 0.65);
      const p1_C = Math.round(laps * 0.55);

      const container = document.getElementById("strategy-plans-container");
      if (!container) return;

      container.innerHTML = `
        <!-- PLAN A -->
        <div class="glass-card p-5 border-t-4 border-t-red-600 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between">
              <span class="text-xs font-mono font-black text-red-400 uppercase tracking-widest">● PLAN A (OPTIMAL)</span>
              <span class="text-xs bg-red-950 text-red-400 border border-red-800 px-2 py-0.5 rounded font-mono font-bold">1-STOP</span>
            </div>
            <h3 class="text-lg font-bold text-white mt-1">Medium $\\rightarrow$ Hard Direct</h3>
            <p class="text-xs text-slate-400 mt-1">
              Pure pace optimization under green flag. Protects track position with zero traffic penalty.
            </p>

            <div class="space-y-3 mt-4 text-xs font-mono">
              <div class="p-3 rounded-xl bg-slate-900/90 border border-slate-800">
                <span class="text-slate-400 block text-[10px]">STINT SEQUENCE</span>
                <div class="flex items-center gap-2 mt-1">
                  <span class="badge-medium px-2 py-0.5 rounded font-bold">Medium: Laps 1 - ${{p1_A}}</span>
                  <span>$\\rightarrow$</span>
                  <span class="badge-hard px-2 py-0.5 rounded font-bold">Hard: Laps ${{p1_A+1}} - ${{laps}}</span>
                </div>
              </div>

              <div class="grid grid-cols-2 gap-2">
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800">
                  <span class="text-slate-400 block text-[10px]">PIT WINDOW</span>
                  <span class="text-white font-bold">Laps ${{p1_A-2}} - ${{p1_A+2}}</span>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800">
                  <span class="text-slate-400 block text-[10px]">TOTAL PIT LOSS</span>
                  <span class="text-red-400 font-bold">${{pitLoss.toFixed(1)}}s (1 Stop)</span>
                </div>
              </div>
            </div>
          </div>

          <div class="mt-4 pt-3 border-t border-slate-800 flex justify-between items-center text-xs font-mono">
            <span class="text-slate-400">WIN PROBABILITY:</span>
            <span class="text-emerald-400 font-black text-sm">62.4%</span>
          </div>
        </div>

        <!-- PLAN B -->
        <div class="glass-card p-5 border-t-4 border-t-amber-500 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between">
              <span class="text-xs font-mono font-black text-amber-400 uppercase tracking-widest">● PLAN B (UNDERCUT ATTACK)</span>
              <span class="text-xs bg-amber-950 text-amber-400 border border-amber-800 px-2 py-0.5 rounded font-mono font-bold">2-STOP</span>
            </div>
            <h3 class="text-lg font-bold text-white mt-1">Soft $\\rightarrow$ Hard $\\rightarrow$ Medium</h3>
            <p class="text-xs text-slate-400 mt-1">
              Aggressive high-grip sprint. Box early to trigger out-lap delta advantage against trapped rivals.
            </p>

            <div class="space-y-3 mt-4 text-xs font-mono">
              <div class="p-3 rounded-xl bg-slate-900/90 border border-slate-800">
                <span class="text-slate-400 block text-[10px]">STINT SEQUENCE</span>
                <div class="flex flex-wrap items-center gap-1.5 mt-1">
                  <span class="badge-soft px-1.5 py-0.5 rounded font-bold">Soft: 1-${{p1_B}}</span>
                  <span>$\\rightarrow$</span>
                  <span class="badge-hard px-1.5 py-0.5 rounded font-bold">Hard: ${{p1_B+1}}-${{p2_B}}</span>
                  <span>$\\rightarrow$</span>
                  <span class="badge-medium px-1.5 py-0.5 rounded font-bold">Med: ${{p2_B+1}}-${{laps}}</span>
                </div>
              </div>

              <div class="grid grid-cols-2 gap-2">
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800">
                  <span class="text-slate-400 block text-[10px]">TARGET PIT 1</span>
                  <span class="text-white font-bold">Lap ${{p1_B}} (Undercut)</span>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800">
                  <span class="text-slate-400 block text-[10px]">GAP DELTA</span>
                  <span class="text-amber-400 font-bold">+1.74s Out-Lap Gain</span>
                </div>
              </div>
            </div>
          </div>

          <div class="mt-4 pt-3 border-t border-slate-800 flex justify-between items-center text-xs font-mono">
            <span class="text-slate-400">WIN PROBABILITY:</span>
            <span class="text-amber-400 font-black text-sm">24.8%</span>
          </div>
        </div>

        <!-- PLAN C -->
        <div class="glass-card p-5 border-t-4 border-t-blue-500 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between">
              <span class="text-xs font-mono font-black text-blue-400 uppercase tracking-widest">● PLAN C (SC OVERCUT GAMBLE)</span>
              <span class="text-xs bg-blue-950 text-blue-400 border border-blue-800 px-2 py-0.5 rounded font-mono font-bold">SC CONTINGENCY</span>
            </div>
            <h3 class="text-lg font-bold text-white mt-1">Hard $\\rightarrow$ Soft / Medium</h3>
            <p class="text-xs text-slate-400 mt-1">
              Reverse longevity gamble. Stretches stint 1 to catch high-probability Virtual or full Safety Cars.
            </p>

            <div class="space-y-3 mt-4 text-xs font-mono">
              <div class="p-3 rounded-xl bg-slate-900/90 border border-slate-800">
                <span class="text-slate-400 block text-[10px]">STINT SEQUENCE</span>
                <div class="flex items-center gap-2 mt-1">
                  <span class="badge-hard px-2 py-0.5 rounded font-bold">Hard: Laps 1 - ${{p1_C}}</span>
                  <span>$\\rightarrow$</span>
                  <span class="badge-soft px-2 py-0.5 rounded font-bold">Soft: Laps ${{p1_C+1}} - ${{laps}}</span>
                </div>
              </div>

              <div class="grid grid-cols-2 gap-2">
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800">
                  <span class="text-slate-400 block text-[10px]">SC PIT DIVIDEND</span>
                  <span class="text-blue-400 font-bold">+12.0s Free Pit</span>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800">
                  <span class="text-slate-400 block text-[10px]">OVERCUT RISK</span>
                  <span class="text-slate-300 font-bold">Graining & Cliff Risk</span>
                </div>
              </div>
            </div>
          </div>

          <div class="mt-4 pt-3 border-t border-slate-800 flex justify-between items-center text-xs font-mono">
            <span class="text-slate-400">WIN PROBABILITY:</span>
            <span class="text-blue-400 font-black text-sm">12.8%</span>
          </div>
        </div>
      `;
    }}

    // ==========================================
    // 4. CHART.JS VISUALIZATIONS
    // ==========================================
    let telemetryChartInst = null;
    let degradationChartInst = null;
    let undercutChartInst = null;

    function renderTelemetryChart(raceId = "1") {{
      const ctx = document.getElementById("telemetryChart");
      if (!ctx) return;
      if (telemetryChartInst) telemetryChartInst.destroy();

      const raceTel = F1_DATA.telemetry.filter(t => t.race_id == raceId);
      const maxLaps = raceTel.length > 0 ? raceTel[0].total_laps : 57;
      const labels = Array.from({{ length: maxLaps }}, (_, i) => i + 1);

      // Synthesize pace curve with pit loss and degradation
      const paceData = labels.map(l => {{
        const base = 91.5 - (l * 0.058); // Fuel burn gain
        const tireWear = Math.pow((l % 24) * 0.12, 1.35);
        const pitSpike = (l === 18 || l === 38) ? 22.0 : 0;
        return (base + tireWear + pitSpike).toFixed(2);
      }});

      telemetryChartInst = new Chart(ctx, {{
        type: 'line',
        data: {{
          labels: labels,
          datasets: [{{
            label: 'Fuel-Corrected Lap Pace (Seconds)',
            data: paceData,
            borderColor: '#E10600',
            backgroundColor: 'rgba(225, 6, 0, 0.12)',
            fill: true,
            tension: 0.25,
            borderWidth: 2,
            pointRadius: 2,
            pointHoverRadius: 6
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ labels: {{ color: '#9CA3AF', font: {{ family: 'Titillium Web' }} }} }}
          }},
          scales: {{
            x: {{ grid: {{ color: '#1F2937' }}, ticks: {{ color: '#9CA3AF' }} }},
            y: {{ grid: {{ color: '#1F2937' }}, ticks: {{ color: '#9CA3AF' }} }}
          }}
        }}
      }});
    }}

    function renderDegradationChart() {{
      const ctx = document.getElementById("degradationChart");
      if (!ctx) return;
      if (degradationChartInst) degradationChartInst.destroy();

      const laps = Array.from({{ length: 40 }}, (_, i) => i + 1);
      const softPace = laps.map(l => (l < 16 ? 0.082 * l : 1.31 + Math.pow(l - 15, 1.8) * 0.15).toFixed(2));
      const medPace = laps.map(l => (l < 26 ? 0.052 * l : 1.35 + Math.pow(l - 25, 1.7) * 0.12).toFixed(2));
      const hardPace = laps.map(l => (l < 38 ? 0.038 * l : 1.44 + Math.pow(l - 37, 1.6) * 0.10).toFixed(2));

      degradationChartInst = new Chart(ctx, {{
        type: 'line',
        data: {{
          labels: laps,
          datasets: [
            {{ label: 'Soft (C3/C4) - Cliff @ Lap 16', data: softPace, borderColor: '#FF1801', borderWidth: 2.5, tension: 0.3 }},
            {{ label: 'Medium (C2) - Cliff @ Lap 26', data: medPace, borderColor: '#FFF200', borderWidth: 2.5, tension: 0.3 }},
            {{ label: 'Hard (C1) - Cliff @ Lap 38', data: hardPace, borderColor: '#FFFFFF', borderWidth: 2.5, tension: 0.3 }}
          ]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{ legend: {{ labels: {{ color: '#E5E7EB' }} }} }},
          scales: {{
            x: {{ title: {{ display: true, text: 'Tire Age (Laps)', color: '#9CA3AF' }}, grid: {{ color: '#1F2937' }}, ticks: {{ color: '#9CA3AF' }} }},
            y: {{ title: {{ display: true, text: 'Pace Loss vs New Tire (s)', color: '#9CA3AF' }}, grid: {{ color: '#1F2937' }}, ticks: {{ color: '#9CA3AF' }} }}
          }}
        }}
      }});
    }}

    function renderUndercutChart() {{
      const ctx = document.getElementById("undercutChart");
      if (!ctx) return;
      if (undercutChartInst) undercutChartInst.destroy();

      const races = ['Bahrain', 'Miami', 'Monaco', 'Silverstone', 'Spa', 'Monza', 'Singapore', 'Las Vegas'];
      const undercutGain = [1.84, 1.42, 0.45, 2.12, 1.95, 1.15, 1.68, 1.78];
      const scDividend = [11.8, 12.4, 8.5, 12.1, 13.5, 10.2, 11.0, 11.5];

      undercutChartInst = new Chart(ctx, {{
        type: 'bar',
        data: {{
          labels: races,
          datasets: [
            {{ label: 'Undercut Out-Lap Delta (+s)', data: undercutGain, backgroundColor: 'rgba(225, 6, 0, 0.7)', borderColor: '#E10600', borderWidth: 1 }},
            {{ label: 'Safety Car Free Pit Dividend (+s)', data: scDividend, backgroundColor: 'rgba(245, 158, 11, 0.7)', borderColor: '#F59E0B', borderWidth: 1 }}
          ]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{ legend: {{ labels: {{ color: '#E5E7EB' }} }} }},
          scales: {{
            x: {{ grid: {{ color: '#1F2937' }}, ticks: {{ color: '#9CA3AF' }} }},
            y: {{ grid: {{ color: '#1F2937' }}, ticks: {{ color: '#9CA3AF' }} }}
          }}
        }}
      }});
    }}

    // ==========================================
    // 5. GLOBAL CIRCUIT ATLAS
    // ==========================================
    function renderCircuitsGrid() {{
      const c = document.getElementById("circuits-grid-container");
      if (!c) return;
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
      if (!c) return;
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
      const sc = document.getElementById("sim-sc-lap").value;
      let scBonus = 0;
      if (sc === 'lap18') scBonus = 10.5;
      if (sc === 'lap25') scBonus = 12.0;

      const delta = (p1 - 20) * 0.14 - scBonus;
      const totalSec = (5504.8 + delta).toFixed(1);
      document.getElementById("sim-result-time").textContent = `${{totalSec}}s`;
      document.getElementById("sim-result-delta").textContent = delta < 0 ? `${{delta.toFixed(1)}}s (Pace Gained)` : `+${{delta.toFixed(1)}}s (Time Deficit)`;
    }}

    // Initialization
    window.addEventListener('DOMContentLoaded', () => {{
      initRevLights();
      setTrack('monza');
      setTeam('ferrari');
      generateF1Strategies();
      requestAnimationFrame(renderMotionLoop);
    }});
  </script>
</body>
</html>
"""

# Write to scratch index.html
with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(master_html)

# Write to artifact f1_race_strategy_dashboard.html
with open(ARTIFACT_HTML, "w", encoding="utf-8") as f:
    f.write(master_html)

print("Saved updated master dashboard & artifact successfully!")
