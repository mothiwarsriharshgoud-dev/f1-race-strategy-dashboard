import json

DATA_PATH = "C:/Users/Main User/.gemini/antigravity/scratch/f1-race-strategy-dashboard/data/f1_strategy_dataset.json"
WIDGET_HTML = "C:/Users/Main User/.gemini/antigravity/brain/bb0fc362-bdeb-4a83-b7c8-80ce516a46a3/f1_race_strategy_widget.html"

with open(DATA_PATH, "r", encoding="utf-8") as f:
    f1_data = json.load(f)

json_data_str = json.dumps(f1_data)

widget_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Titillium+Web:ital,wght@0,400;0,600;0,700;0,900;1,600&family=JetBrains+Mono:wght@400;600;700;800&display=swap');
    body {{
      font-family: 'Titillium Web', -apple-system, BlinkMacSystemFont, sans-serif;
    }}
    .mono {{
      font-family: 'JetBrains Mono', monospace;
    }}
    .tab-active {{
      background: rgba(225, 6, 0, 0.25);
      border-color: #E10600;
      color: #FFFFFF;
      font-weight: 700;
    }}
    @keyframes pulse-drs {{
      0%, 100% {{ box-shadow: 0 0 12px rgba(0, 255, 127, 0.8); }}
      50% {{ box-shadow: 0 0 4px rgba(0, 255, 127, 0.2); }}
    }}
    .glow-drs {{
      animation: pulse-drs 1s infinite ease-in-out;
    }}
  </style>
</head>
<body class="bg-transparent text-[var(--foreground)] antialiased p-2 md:p-3">

  <div class="bg-[var(--card)] text-[var(--foreground)] border border-[var(--border)] rounded-2xl p-4 md:p-5 shadow-2xl space-y-4">
    
    <!-- HEADER -->
    <div class="flex flex-wrap items-center justify-between gap-3 border-b border-[var(--border)] pb-3">
      <div class="flex items-center gap-3">
        <div class="bg-red-600 text-white font-black px-2.5 py-1 rounded text-base tracking-wider flex items-center gap-1 shadow-md shadow-red-900/40">
          <span>F1</span>
          <span class="text-xs bg-black/40 px-1 py-0.5 rounded font-mono">P32</span>
        </div>
        <div>
          <h2 class="text-base font-bold text-[var(--foreground)] flex items-center gap-2">
            Formula 1 AI Race Strategy Platform & Live Motion Arena
            <span class="text-xs font-mono px-2 py-0.5 rounded-full bg-emerald-950 text-emerald-400 border border-emerald-800 font-semibold flex items-center gap-1">
              <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span> 60 FPS HUD
            </span>
          </h2>
          <p class="text-xs text-[var(--muted-foreground)]">
            Resolving: <span class="text-red-400 italic font-semibold">"How do race strategies influence Formula 1 performance?"</span>
          </p>
        </div>
      </div>

      <div class="flex items-center gap-2 text-xs font-mono">
        <button onclick="triggerWidgetBoxBox()" class="px-3 py-1.5 rounded-lg bg-amber-600 hover:bg-amber-500 text-white font-bold flex items-center gap-1.5 shadow transition">
          <span>📻</span> BOX BOX (PIT STOP)
        </button>
        <button onclick="runWidgetStrategyEngine()" class="px-3 py-1.5 rounded-lg bg-red-600 hover:bg-red-500 text-white font-bold flex items-center gap-1.5 shadow transition">
          <span>⚡</span> Re-Calculate
        </button>
      </div>
    </div>

    <!-- STRATEGIC KPIS -->
    <div class="grid grid-cols-2 md:grid-cols-4 gap-2.5 text-xs">
      <div class="p-2.5 rounded-xl bg-slate-900/80 border border-[var(--border)] border-l-4 border-l-red-500">
        <span class="text-[10px] font-mono text-[var(--muted-foreground)] block uppercase">Undercut Win Rate</span>
        <div class="text-lg font-black text-white mt-0.5">68.4%</div>
        <span class="text-[10px] text-emerald-400 font-mono">+1.74s gap gain</span>
      </div>

      <div class="p-2.5 rounded-xl bg-slate-900/80 border border-[var(--border)] border-l-4 border-l-amber-500">
        <span class="text-[10px] font-mono text-[var(--muted-foreground)] block uppercase">SC Pit Dividend</span>
        <div class="text-lg font-black text-white mt-0.5">+12.0s Free Stop</div>
        <span class="text-[10px] text-amber-400 font-mono">Pit loss: 9.8s vs 22s</span>
      </div>

      <div class="p-2.5 rounded-xl bg-slate-900/80 border border-[var(--border)] border-l-4 border-l-emerald-500">
        <span class="text-[10px] font-mono text-[var(--muted-foreground)] block uppercase">Strategy Podiums</span>
        <div class="text-lg font-black text-white mt-0.5">42.8% Delta</div>
        <span class="text-[10px] text-slate-300 font-mono">Pit lane overtakes</span>
      </div>

      <div class="p-2.5 rounded-xl bg-slate-900/80 border border-[var(--border)] border-l-4 border-l-purple-500">
        <span class="text-[10px] font-mono text-[var(--muted-foreground)] block uppercase">Fuel Burn Rate</span>
        <div class="text-lg font-black text-white mt-0.5">-0.062 s/lap</div>
        <span class="text-[10px] text-purple-300 font-mono">110kg consumption</span>
      </div>
    </div>

    <!-- TABS -->
    <div class="flex gap-2 border-b border-[var(--border)] pb-2 text-xs font-mono">
      <button onclick="setWidgetTab('motion')" id="wtab-motion" class="tab-active px-3 py-1.5 rounded-lg border border-[var(--border)] transition flex items-center gap-1">
        <span>🏎️</span> Live Motion Arena
      </button>
      <button onclick="setWidgetTab('gen')" id="wtab-gen" class="px-3 py-1.5 rounded-lg border border-[var(--border)] text-[var(--muted-foreground)] hover:text-white transition flex items-center gap-1">
        <span>⚡</span> Strategy Optimizer (Plan A/B/C)
      </button>
      <button onclick="setWidgetTab('telemetry')" id="wtab-telemetry" class="px-3 py-1.5 rounded-lg border border-[var(--border)] text-[var(--muted-foreground)] hover:text-white transition flex items-center gap-1">
        <span>⏱️</span> Telemetry & Stints
      </button>
      <button onclick="setWidgetTab('degradation')" id="wtab-degradation" class="px-3 py-1.5 rounded-lg border border-[var(--border)] text-[var(--muted-foreground)] hover:text-white transition flex items-center gap-1">
        <span>📉</span> Tire Degradation
      </button>
    </div>

    <!-- VIEW 1: LIVE MOTION ARENA -->
    <div id="wview-motion" class="space-y-3">
      
      <!-- Toolbar for Arena -->
      <div class="flex flex-wrap items-center justify-between gap-2 text-xs font-mono bg-slate-900/60 p-2.5 rounded-xl border border-[var(--border)]">
        <div class="flex items-center gap-1.5">
          <span class="text-[var(--muted-foreground)] text-[10px]">TRACK:</span>
          <button onclick="setWidgetTrack('monza')" id="wbtn-t-monza" class="px-2 py-0.5 rounded bg-red-600 text-white font-bold">Monza</button>
          <button onclick="setWidgetTrack('silverstone')" id="wbtn-t-silverstone" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300">Silverstone</button>
          <button onclick="setWidgetTrack('spa')" id="wbtn-t-spa" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300">Spa</button>
        </div>

        <div class="flex items-center gap-1.5">
          <span class="text-[var(--muted-foreground)] text-[10px]">CAR:</span>
          <button onclick="setWidgetTeam('ferrari')" id="wbtn-c-ferrari" title="Ferrari" class="w-5 h-5 rounded-full bg-[#D40000] border border-white"></button>
          <button onclick="setWidgetTeam('redbull')" id="wbtn-c-redbull" title="Red Bull" class="w-5 h-5 rounded-full bg-[#061327] border border-[#FFD700]"></button>
          <button onclick="setWidgetTeam('mclaren')" id="wbtn-c-mclaren" title="McLaren" class="w-5 h-5 rounded-full bg-[#FF8000] border border-slate-600"></button>
          <button onclick="setWidgetTeam('mercedes')" id="wbtn-c-mercedes" title="Mercedes" class="w-5 h-5 rounded-full bg-[#00A19B] border border-slate-400"></button>
        </div>

        <div class="flex items-center gap-2">
          <button onclick="toggleWidgetSim()" id="wbtn-pause" class="px-2.5 py-0.5 rounded bg-slate-800 text-slate-300">⏸️</button>
          <button onclick="setWidgetMultiplier(1)" id="wspd-1" class="px-2 py-0.5 rounded bg-red-600 text-white font-bold">1x</button>
          <button onclick="setWidgetMultiplier(2)" id="wspd-2" class="px-2 py-0.5 rounded text-slate-400">2x</button>
        </div>
      </div>

      <!-- Live Canvas & Moving F1 Car -->
      <div class="relative w-full rounded-xl overflow-hidden border border-slate-800 bg-[#0B0E14] shadow-inner">
        
        <!-- Live HUD Overlay -->
        <div class="absolute top-2.5 left-2.5 z-10 flex items-center gap-2 pointer-events-none text-[11px] font-mono">
          <div class="bg-black/75 px-2.5 py-1 rounded border border-slate-700 text-white">
            <span id="whud-track">Monza (53 Laps)</span> • Lap <span id="whud-lap" class="text-red-400 font-bold">18</span>
          </div>
          <div id="whud-drs" class="px-2.5 py-1 rounded bg-slate-900 border border-slate-700 text-slate-400 font-bold">
            DRS CLOSED
          </div>
        </div>

        <!-- Pit Stop Banner in Widget -->
        <div id="wpit-banner" class="hidden absolute inset-0 z-20 bg-black/60 backdrop-blur-sm flex flex-col items-center justify-center pointer-events-none">
          <div class="bg-slate-900 border border-amber-500 rounded-xl p-4 text-center max-w-xs w-full shadow-2xl">
            <span class="text-[10px] font-mono text-amber-400 font-bold uppercase tracking-wider">● BOX BOX EXECUTION</span>
            <div class="text-xl font-black text-white mt-0.5">PIT STOP IN PROGRESS</div>
            <div class="text-3xl font-mono font-black text-amber-400 my-1" id="wpit-timer">0.00s</div>
            <div class="text-[10px] font-mono text-slate-300">
              Fitted: <span id="wpit-compound" class="text-white font-bold">HARD (C1)</span> • <span class="text-emerald-400 font-bold">+1.84s Gap Gain</span>
            </div>
          </div>
        </div>

        <canvas id="w-f1-canvas" class="w-full block" width="800" height="380"></canvas>
      </div>

      <!-- Live Telemetry Bar -->
      <div class="grid grid-cols-4 gap-2 text-xs font-mono">
        <div class="p-2 rounded-lg bg-slate-900/90 border border-[var(--border)] text-center">
          <span class="text-[9px] text-slate-400 block">SPEED</span>
          <div class="text-lg font-black text-white"><span id="wtel-speed">315</span> <span class="text-[9px] text-slate-400">KM/H</span></div>
        </div>

        <div class="p-2 rounded-lg bg-slate-900/90 border border-[var(--border)] text-center">
          <span class="text-[9px] text-slate-400 block">GEAR</span>
          <div class="text-lg font-black text-red-400" id="wtel-gear">7</div>
        </div>

        <div class="p-2 rounded-lg bg-slate-900/90 border border-[var(--border)] text-center">
          <span class="text-[9px] text-slate-400 block">RPM</span>
          <div class="text-lg font-black text-slate-200" id="wtel-rpm">13,200</div>
        </div>

        <div class="p-2 rounded-lg bg-slate-900/90 border border-[var(--border)] text-center">
          <span class="text-[9px] text-slate-400 block">TIRE</span>
          <div class="text-sm font-bold text-red-400 mt-0.5" id="wtel-compound">SOFT (C3)</div>
        </div>
      </div>

    </div>

    <!-- VIEW 2: STRATEGY GENERATOR -->
    <div id="wview-gen" class="hidden space-y-3">
      <div class="grid grid-cols-2 md:grid-cols-4 gap-2 text-xs font-mono">
        <div>
          <label class="text-[10px] text-[var(--muted-foreground)] block">CIRCUIT</label>
          <select id="w-circuit" onchange="runWidgetStrategyEngine()" class="w-full bg-slate-900 border border-[var(--border)] rounded p-1.5 text-xs text-white">
            <option value="3" selected>Bahrain (57 Laps)</option>
            <option value="14">Monza (53 Laps)</option>
            <option value="9">Silverstone (52 Laps)</option>
            <option value="13">Spa (44 Laps)</option>
            <option value="6">Monaco (78 Laps)</option>
          </select>
        </div>

        <div>
          <label class="text-[10px] text-[var(--muted-foreground)] block">GRID POSITION</label>
          <select id="w-grid" onchange="runWidgetStrategyEngine()" class="w-full bg-slate-900 border border-[var(--border)] rounded p-1.5 text-xs text-white">
            <option value="1" selected>Pole (P1)</option>
            <option value="4">Row 2 (P4)</option>
            <option value="10">Midfield (P10)</option>
          </select>
        </div>

        <div>
          <label class="text-[10px] text-[var(--muted-foreground)] block">TRACK TEMP</label>
          <div class="flex items-center gap-1.5 mt-1">
            <input type="range" id="w-temp" min="22" max="50" value="34" oninput="document.getElementById('w-temp-val').textContent=this.value+'°C'; runWidgetStrategyEngine();" class="w-full accent-red-600">
            <span id="w-temp-val" class="font-bold text-slate-300 text-[11px] w-8">34&deg;C</span>
          </div>
        </div>

        <div>
          <label class="text-[10px] text-[var(--muted-foreground)] block">SAFETY CAR RISK</label>
          <select id="w-sc" onchange="runWidgetStrategyEngine()" class="w-full bg-slate-900 border border-[var(--border)] rounded p-1.5 text-xs text-white">
            <option value="0.2">Low (&lt;25%)</option>
            <option value="0.45" selected>Medium (~45%)</option>
            <option value="0.8">High (&gt;75%)</option>
          </select>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs" id="w-plans-container">
        <!-- Rendered by JS -->
      </div>
    </div>

    <!-- VIEW 3: TELEMETRY -->
    <div id="wview-telemetry" class="hidden space-y-2">
      <div class="p-3 rounded-xl bg-slate-900/80 border border-[var(--border)] text-xs font-mono space-y-2">
        <div class="flex justify-between font-bold border-b border-slate-800 pb-1.5">
          <span class="text-red-400">Grand Prix Telemetry Profiles</span>
          <span class="text-slate-400">Fuel Burn: -0.062s / Lap</span>
        </div>
        <p class="text-slate-300 leading-relaxed text-[11px]">
          Fuel burn lightening creates a steady pace improvement that offsets tire degradation during early laps. Once past the thermal cliff threshold, pace rapidly drops at +0.35s/lap.
        </p>
      </div>
    </div>

    <!-- VIEW 4: DEGRADATION -->
    <div id="wview-degradation" class="hidden space-y-2">
      <div class="p-3 rounded-xl bg-slate-900/80 border border-[var(--border)] text-xs font-mono space-y-2">
        <div class="flex justify-between font-bold border-b border-slate-800 pb-1.5">
          <span class="text-red-400">Pirelli Compound Wear Limits</span>
          <span class="text-amber-400">Non-Linear Thermal Cliffs</span>
        </div>
        <div class="grid grid-cols-3 gap-2 text-center text-[11px] pt-1">
          <div class="p-2 rounded bg-slate-950 border border-slate-800">
            <span class="text-red-400 font-bold block">SOFT (C3)</span>
            <span class="text-slate-300 block">Cliff: Lap 16</span>
            <span class="text-[10px] text-slate-400">+0.082 s/lap</span>
          </div>
          <div class="p-2 rounded bg-slate-950 border border-slate-800">
            <span class="text-yellow-400 font-bold block">MEDIUM (C2)</span>
            <span class="text-slate-300 block">Cliff: Lap 26</span>
            <span class="text-[10px] text-slate-400">+0.052 s/lap</span>
          </div>
          <div class="p-2 rounded bg-slate-950 border border-slate-800">
            <span class="text-white font-bold block">HARD (C1)</span>
            <span class="text-slate-300 block">Cliff: Lap 38</span>
            <span class="text-[10px] text-slate-400">+0.038 s/lap</span>
          </div>
        </div>
      </div>
    </div>

  </div>

  <script>
    const F1_DATA = {json_data_str};

    // Widget Tabs
    function setWidgetTab(t) {{
      const tabs = ['motion', 'gen', 'telemetry', 'degradation'];
      tabs.forEach(tab => {{
        const btn = document.getElementById('wtab-' + tab);
        const view = document.getElementById('wview-' + tab);
        if (btn) {{
          if (tab === t) btn.className = 'tab-active px-3 py-1.5 rounded-lg border border-[var(--border)] transition flex items-center gap-1 font-bold';
          else btn.className = 'px-3 py-1.5 rounded-lg border border-[var(--border)] text-[var(--muted-foreground)] hover:text-white transition flex items-center gap-1';
        }}
        if (view) {{
          if (tab === t) view.classList.remove('hidden');
          else view.classList.add('hidden');
        }}
      }});
      if (t === 'gen') runWidgetStrategyEngine();
    }}

    // Widget Motion State
    const W_CIRCUITS = {{
      monza: [
        [100, 310], [540, 310], [590, 290], [610, 260], [590, 240], [560, 250],
        [600, 230], [660, 190], [680, 140], [660, 100], [610, 100], [580, 110],
        [540, 90], [500, 60], [450, 60], [330, 90], [240, 120],
        [190, 140], [160, 120], [180, 90], [150, 170], [100, 240], [70, 280], [80, 310]
      ],
      silverstone: [
        [120, 310], [350, 310], [420, 290], [460, 250], [430, 210], [370, 210],
        [320, 220], [250, 220], [180, 190], [150, 150], [190, 120], [270, 90],
        [350, 90], [410, 80], [470, 90], [530, 110], [570, 140], [580, 180],
        [550, 200], [500, 260], [460, 290], [380, 300], [210, 310]
      ],
      spa: [
        [160, 300], [320, 300], [370, 300], [400, 270], [380, 240], [340, 250],
        [360, 220], [410, 180], [460, 140], [500, 90], [550, 80], [640, 80],
        [670, 100], [650, 130], [610, 130], [590, 170], [540, 190], [500, 210],
        [470, 240], [420, 250], [360, 230], [300, 200], [250, 180], [180, 160],
        [140, 170], [110, 190], [100, 240], [120, 280], [140, 300]
      ]
    }};

    const W_TEAMS = {{
      ferrari: {{ color: '#D40000', accent: '#FFFFFF', rim: '#FFD700' }},
      redbull: {{ color: '#061327', accent: '#E10600', rim: '#FFD700' }},
      mclaren: {{ color: '#FF8000', accent: '#00D2BE', rim: '#1E2024' }},
      mercedes: {{ color: '#00A19B', accent: '#C0C0C0', rim: '#111111' }}
    }};

    let wTrackKey = 'monza';
    let wTeamKey = 'ferrari';
    let wCompoundKey = 'soft';
    let wProgress = 0;
    let wSpeed = 160;
    let wRPM = 10500;
    let wGear = 5;
    let wSpeedMult = 1;
    let wPaused = false;
    let wDRS = false;
    let wPitLimiter = false;
    let wPitStop = false;
    let wLap = 18;
    let wSpline = [];
    let wSparks = [];

    function buildWidgetSpline(pts, samples = 30) {{
      const n = pts.length;
      const res = [];
      for (let i = 0; i < n; i++) {{
        const p0 = pts[(i - 1 + n) % n];
        const p1 = pts[i];
        const p2 = pts[(i + 1) % n];
        const p3 = pts[(i + 2) % n];
        for (let s = 0; s < samples; s++) {{
          const t = s / samples;
          const t2 = t * t;
          const t3 = t2 * t;
          const x = 0.5 * ((2 * p1[0]) + (-p0[0] + p2[0]) * t + (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * t2 + (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * t3);
          const y = 0.5 * ((2 * p1[1]) + (-p0[1] + p2[1]) * t + (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * t2 + (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * t3);
          const dx = 0.5 * ((-p0[0] + p2[0]) + 2 * (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * t + 3 * (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * t2);
          const dy = 0.5 * ((-p0[1] + p2[1]) + 2 * (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * t + 3 * (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * t2);
          res.push({{ x, y, heading: Math.atan2(dy, dx) }});
        }}
      }}
      const len = res.length;
      for (let i = 0; i < len; i++) {{
        let dh = res[(i + 1) % len].heading - res[(i - 1 + len) % len].heading;
        while (dh > Math.PI) dh -= 2 * Math.PI;
        while (dh < -Math.PI) dh += 2 * Math.PI;
        res[i].curv = Math.abs(dh);
      }}
      return res;
    }}

    function setWidgetTrack(k) {{
      wTrackKey = k;
      wSpline = buildWidgetSpline(W_CIRCUITS[k] || W_CIRCUITS.monza);
      wProgress = 0;
      ['monza', 'silverstone', 'spa'].forEach(t => {{
        const b = document.getElementById('wbtn-t-' + t);
        if (b) {{
          if (t === k) {{ b.className = 'px-2 py-0.5 rounded bg-red-600 text-white font-bold'; }}
          else {{ b.className = 'px-2 py-0.5 rounded bg-slate-800 text-slate-300'; }}
        }}
      }});
      const names = {{ monza: 'Monza (53 Laps)', silverstone: 'Silverstone (52 Laps)', spa: 'Spa (44 Laps)' }};
      document.getElementById('whud-track').textContent = names[k] || k;
    }}

    function setWidgetTeam(k) {{
      wTeamKey = k;
      ['ferrari', 'redbull', 'mclaren', 'mercedes'].forEach(t => {{
        const b = document.getElementById('wbtn-c-' + t);
        if (b) {{
          b.style.transform = (t === k) ? 'scale(1.25)' : 'scale(1.0)';
        }}
      }});
    }}

    function toggleWidgetSim() {{
      wPaused = !wPaused;
      const b = document.getElementById('wbtn-pause');
      if (b) b.textContent = wPaused ? '▶️' : '⏸️';
    }}

    function setWidgetMultiplier(m) {{
      wSpeedMult = m;
      [1, 2].forEach(val => {{
        const b = document.getElementById('wspd-' + val);
        if (b) {{
          if (val === m) b.className = 'px-2 py-0.5 rounded bg-red-600 text-white font-bold';
          else b.className = 'px-2 py-0.5 rounded text-slate-400';
        }}
      }});
    }}

    function triggerWidgetBoxBox() {{
      if (wPitStop) return;
      wPitStop = true;
      wPitLimiter = true;
      const banner = document.getElementById('wpit-banner');
      if (banner) banner.classList.remove('hidden');

      let timer = 0;
      const timerEl = document.getElementById('wpit-timer');
      const inv = setInterval(() => {{
        timer += 0.06;
        if (timerEl) timerEl.textContent = timer.toFixed(2) + 's';
        if (timer >= 2.14) {{
          clearInterval(inv);
          wCompoundKey = (wCompoundKey === 'soft') ? 'hard' : 'soft';
          document.getElementById('wtel-compound').textContent = wCompoundKey === 'soft' ? 'SOFT (C3)' : 'HARD (C1)';
          document.getElementById('wtel-compound').style.color = wCompoundKey === 'soft' ? '#FF1801' : '#FFFFFF';
          setTimeout(() => {{
            if (banner) banner.classList.add('hidden');
            wPitLimiter = false;
            wPitStop = false;
            wLap++;
            document.getElementById('whud-lap').textContent = wLap;
          }}, 400);
        }}
      }}, 50);
    }}

    function renderWidgetMotion() {{
      const cvs = document.getElementById('w-f1-canvas');
      if (!cvs || wSpline.length === 0) {{
        requestAnimationFrame(renderWidgetMotion);
        return;
      }}
      const ctx = cvs.getContext('2d');
      ctx.clearRect(0, 0, cvs.width, cvs.height);

      // Track surface
      ctx.save();
      ctx.lineCap = 'round';
      ctx.lineJoin = 'round';
      ctx.lineWidth = 34;
      ctx.strokeStyle = '#10141D';
      ctx.beginPath();
      for (let i = 0; i < wSpline.length; i++) {{
        if (i === 0) ctx.moveTo(wSpline[i].x, wSpline[i].y);
        else ctx.lineTo(wSpline[i].x, wSpline[i].y);
      }}
      ctx.closePath();
      ctx.stroke();

      // Rubber groove
      ctx.lineWidth = 12;
      ctx.strokeStyle = '#0B0D13';
      ctx.beginPath();
      for (let i = 0; i < wSpline.length; i++) {{
        if (i === 0) ctx.moveTo(wSpline[i].x, wSpline[i].y);
        else ctx.lineTo(wSpline[i].x, wSpline[i].y);
      }}
      ctx.closePath();
      ctx.stroke();

      // DRS Straight section
      const dStart = Math.floor(wSpline.length * 0.02);
      const dEnd = Math.floor(wSpline.length * 0.24);
      ctx.lineWidth = 3;
      ctx.setLineDash([6, 6]);
      ctx.strokeStyle = '#00FF7F';
      ctx.beginPath();
      for (let i = dStart; i < dEnd; i++) {{
        if (i === dStart) ctx.moveTo(wSpline[i].x, wSpline[i].y);
        else ctx.lineTo(wSpline[i].x, wSpline[i].y);
      }}
      ctx.stroke();
      ctx.setLineDash([]);
      ctx.restore();

      // Motion physics
      if (!wPaused) {{
        const ptIdx = Math.floor(wProgress * wSpline.length);
        const cur = wSpline[ptIdx] || wSpline[0];
        const curv = cur.curv || 0.01;

        if (wPitLimiter) {{
          wSpeed = 80;
          wRPM = 5200;
          wGear = 2;
          wDRS = false;
        }} else {{
          wDRS = (ptIdx >= dStart && ptIdx <= dEnd);
          if (curv > 0.045) {{
            wSpeed = Math.max(90, wSpeed - 8.0 * wSpeedMult);
            wGear = 2;
            wRPM = 8200;
          }} else if (curv > 0.02) {{
            wSpeed = Math.max(160, Math.min(220, wSpeed + 1.2 * wSpeedMult));
            wGear = 4;
            wRPM = 10400;
          }} else {{
            const topSpd = wDRS ? 348 : 332;
            wSpeed = Math.min(topSpd, wSpeed + 3.5 * wSpeedMult);
            wGear = (wSpeed > 300) ? 8 : (wSpeed > 260) ? 7 : (wSpeed > 220) ? 6 : 5;
            wRPM = 11400 + (wSpeed % 40) * 80;

            if (wSpeed > 295 && Math.random() < 0.5) {{
              wSparks.push({{
                x: cur.x - Math.cos(cur.heading) * 16,
                y: cur.y - Math.sin(cur.heading) * 16,
                vx: -Math.cos(cur.heading) * 3 + (Math.random() - 0.5) * 2,
                vy: -Math.sin(cur.heading) * 3 + (Math.random() - 0.5) * 2,
                life: 1.0
              }});
            }}
          }}
        }}

        const inc = (wSpeed / 340) * 0.0022 * wSpeedMult;
        wProgress = (wProgress + inc) % 1;
      }}

      // Sparks
      for (let i = wSparks.length - 1; i >= 0; i--) {{
        const sp = wSparks[i];
        sp.x += sp.vx;
        sp.y += sp.vy;
        sp.life -= 0.05;
        if (sp.life <= 0) wSparks.splice(i, 1);
        else {{
          ctx.fillStyle = '#FFD700';
          ctx.beginPath();
          ctx.arc(sp.x, sp.y, 1.6 * sp.life, 0, Math.PI * 2);
          ctx.fill();
        }}
      }}

      // Draw Car
      const ptIdx = Math.floor(wProgress * wSpline.length);
      const cp = wSpline[ptIdx] || wSpline[0];
      const tm = W_TEAMS[wTeamKey] || W_TEAMS.ferrari;

      ctx.save();
      ctx.translate(cp.x, cp.y);
      ctx.rotate(cp.heading);

      if (wDRS) {{
        ctx.strokeStyle = 'rgba(0, 255, 127, 0.4)';
        ctx.lineWidth = 10;
        ctx.beginPath();
        ctx.moveTo(-14, 0); ctx.lineTo(-35, 0);
        ctx.stroke();
      }}

      // 4 wheels
      const wCol = (wCompoundKey === 'soft') ? '#FF1801' : '#FFFFFF';
      [ [11, -9], [11, 9], [-12, -10], [-12, 10] ].forEach(([wx, wy]) => {{
        ctx.fillStyle = '#080A0E';
        ctx.fillRect(wx - 5, wy - 2.5, 10, 5);
        ctx.strokeStyle = wCol;
        ctx.lineWidth = 1.4;
        ctx.strokeRect(wx - 5, wy - 2.5, 10, 5);
      }});

      // Chassis
      ctx.fillStyle = tm.color;
      ctx.beginPath();
      ctx.moveTo(16, 0);
      ctx.lineTo(11, -3);
      ctx.lineTo(1, -6);
      ctx.lineTo(-12, -6);
      ctx.lineTo(-15, -3);
      ctx.lineTo(-15, 3);
      ctx.lineTo(-12, 6);
      ctx.lineTo(1, 6);
      ctx.lineTo(11, 3);
      ctx.closePath();
      ctx.fill();

      // Front & Rear wing
      ctx.fillRect(14, -10, 3, 20);
      ctx.fillRect(-17, -9, 3, 18);

      // Helmet
      ctx.fillStyle = tm.rim;
      ctx.beginPath();
      ctx.arc(-1, 0, 2, 0, Math.PI * 2);
      ctx.fill();

      ctx.restore();

      // HUD values
      const sEl = document.getElementById('wtel-speed');
      const rEl = document.getElementById('wtel-rpm');
      const gEl = document.getElementById('wtel-gear');
      const drsEl = document.getElementById('whud-drs');

      if (sEl) sEl.textContent = Math.round(wSpeed);
      if (rEl) rEl.textContent = Math.round(wRPM).toLocaleString();
      if (gEl) gEl.textContent = wPitLimiter ? 'P' : wGear;

      if (drsEl) {{
        if (wDRS) {{
          drsEl.className = 'px-2.5 py-1 rounded bg-emerald-950 border border-emerald-600 text-emerald-400 font-bold glow-drs';
          drsEl.textContent = 'DRS ACTIVE';
        }} else {{
          drsEl.className = 'px-2.5 py-1 rounded bg-slate-900 border border-slate-700 text-slate-400 font-bold';
          drsEl.textContent = 'DRS CLOSED';
        }}
      }}

      requestAnimationFrame(renderWidgetMotion);
    }}

    function runWidgetStrategyEngine() {{
      const cId = parseInt(document.getElementById("w-circuit").value);
      const circuit = F1_DATA.circuits.find(c => c.circuitId === cId) || F1_DATA.circuits[0];
      const laps = circuit.laps || 57;
      const pitLoss = circuit.pit_loss_sec || 22.0;

      const p1_A = Math.round(laps * 0.35);
      const p1_B = Math.round(laps * 0.24);
      const p2_B = Math.round(laps * 0.65);
      const p1_C = Math.round(laps * 0.55);

      const cont = document.getElementById("w-plans-container");
      if (!cont) return;

      cont.innerHTML = `
        <div class="p-3 rounded-xl bg-slate-900/90 border-t-2 border-t-red-600 font-mono">
          <div class="flex justify-between font-bold">
            <span class="text-red-400">PLAN A (OPTIMAL)</span>
            <span class="text-slate-400">1-STOP</span>
          </div>
          <div class="text-white font-bold my-1">Medium $\\rightarrow$ Hard</div>
          <div class="text-[11px] text-slate-300">Stint 1: L1-${{p1_A}} | Stint 2: L${{p1_A+1}}-${{laps}}</div>
          <div class="flex justify-between text-[11px] text-slate-400 mt-2 pt-1 border-t border-slate-800">
            <span>Pit Loss: ${{pitLoss}}s</span>
            <span class="text-emerald-400 font-bold">62.4% Win Prob</span>
          </div>
        </div>

        <div class="p-3 rounded-xl bg-slate-900/90 border-t-2 border-t-amber-500 font-mono">
          <div class="flex justify-between font-bold">
            <span class="text-amber-400">PLAN B (UNDERCUT)</span>
            <span class="text-slate-400">2-STOP</span>
          </div>
          <div class="text-white font-bold my-1">Soft $\\rightarrow$ Hard $\\rightarrow$ Med</div>
          <div class="text-[11px] text-slate-300">Box L${{p1_B}} & L${{p2_B}}</div>
          <div class="flex justify-between text-[11px] text-slate-400 mt-2 pt-1 border-t border-slate-800">
            <span>Delta: +1.74s Out-Lap</span>
            <span class="text-amber-400 font-bold">24.8% Win Prob</span>
          </div>
        </div>

        <div class="p-3 rounded-xl bg-slate-900/90 border-t-2 border-t-blue-500 font-mono">
          <div class="flex justify-between font-bold">
            <span class="text-blue-400">PLAN C (SC GAMBLE)</span>
            <span class="text-slate-400">REVERSE</span>
          </div>
          <div class="text-white font-bold my-1">Hard $\\rightarrow$ Soft</div>
          <div class="text-[11px] text-slate-300">Stint 1: L1-${{p1_C}} (SC Window)</div>
          <div class="flex justify-between text-[11px] text-slate-400 mt-2 pt-1 border-t border-slate-800">
            <span>Dividend: +12s Free</span>
            <span class="text-blue-400 font-bold">12.8% Win Prob</span>
          </div>
        </div>
      `;
    }}

    window.addEventListener('DOMContentLoaded', () => {{
      setWidgetTrack('monza');
      setWidgetTeam('ferrari');
      runWidgetStrategyEngine();
      requestAnimationFrame(renderWidgetMotion);
    }});
  </script>
</body>
</html>
"""

with open(WIDGET_HTML, "w", encoding="utf-8") as f:
    f.write(widget_html)

print("Saved updated motion widget successfully!")
