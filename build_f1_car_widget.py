import json

DATA_PATH = "C:/Users/Main User/.gemini/antigravity/scratch/f1-race-strategy-dashboard/data/f1_strategy_dataset.json"
WIDGET_PATH = "C:/Users/Main User/.gemini/antigravity/brain/bb0fc362-bdeb-4a83-b7c8-80ce516a46a3/f1_race_strategy_widget.html"
B64_PATH = "C:/Users/Main User/.gemini/antigravity/scratch/f1-race-strategy-dashboard/assets/f1_2024_car_b64.txt"

with open(DATA_PATH, "r", encoding="utf-8") as f:
    f1_data = json.load(f)

with open(B64_PATH, "r", encoding="utf-8") as f:
    car_b64 = f.read().strip()

json_data_str = json.dumps(f1_data)

widget_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Titillium+Web:wght@400;600;700;900&family=JetBrains+Mono:wght@400;600;700;800&display=swap');
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
    @keyframes pulse-pin {{
      0% {{ transform: scale(0.95); box-shadow: 0 0 0 0 rgba(225, 6, 0, 0.7); }}
      70% {{ transform: scale(1.15); box-shadow: 0 0 0 8px rgba(225, 6, 0, 0); }}
      100% {{ transform: scale(0.95); box-shadow: 0 0 0 0 rgba(225, 6, 0, 0); }}
    }}
    .pin-pulse {{
      animation: pulse-pin 2s infinite;
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
            Formula 1 Race Strategy & Original F1 Car Platform
            <span class="text-xs font-mono px-2 py-0.5 rounded-full bg-emerald-950 text-emerald-400 border border-emerald-800 font-semibold flex items-center gap-1">
              <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span> 2024 CAD MODEL
            </span>
          </h2>
          <p class="text-xs text-[var(--muted-foreground)]">
            Resolving: <span class="text-red-400 italic font-semibold">"How do race strategies influence Formula 1 performance?"</span>
          </p>
        </div>
      </div>

      <div class="flex items-center gap-2 text-xs font-mono">
        <button onclick="toggleWidgetDRS()" id="w-drs-btn" class="px-2.5 py-1 rounded-lg bg-slate-900 border border-[var(--border)] text-slate-300 font-bold hover:border-emerald-500 transition">
          <span id="w-drs-txt">DRS: CLOSED</span>
        </button>
        <button onclick="runWidgetStrategyEngine()" class="px-3 py-1.5 rounded-lg bg-red-600 hover:bg-red-500 text-white font-bold flex items-center gap-1 shadow transition">
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
      <button onclick="setWidgetTab('car')" id="wtab-car" class="tab-active px-3 py-1.5 rounded-lg border border-[var(--border)] transition flex items-center gap-1 font-bold">
        <span>🏎️</span> Original F1 Car (Aero & Hotspots)
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

    <!-- VIEW 1: ORIGINAL 2024 F1 CAR INSPECTOR -->
    <div id="wview-car" class="space-y-3">
      
      <!-- Interactive F1 Car Hero Container -->
      <div class="relative w-full rounded-xl overflow-hidden border border-[var(--border)] bg-[#0C0F17] shadow-2xl">
        <img src="data:image/jpeg;base64,{car_b64}" alt="Original 2024 Formula 1 Race Car" class="w-full h-auto block object-cover select-none">

        <!-- Hotspot 1: Front Wing -->
        <button onclick="selectWidgetHotspot('front-wing')" class="absolute top-[68%] left-[16%] -translate-x-1/2 -translate-y-1/2 group z-20 focus:outline-none">
          <span class="w-5 h-5 rounded-full bg-red-600/90 border border-white flex items-center justify-center text-white text-[9px] font-bold shadow-md pin-pulse">
            1
          </span>
        </button>

        <!-- Hotspot 2: Wheels -->
        <button onclick="selectWidgetHotspot('wheels')" class="absolute top-[72%] left-[25%] -translate-x-1/2 -translate-y-1/2 group z-20 focus:outline-none">
          <span class="w-5 h-5 rounded-full bg-amber-500/90 border border-white flex items-center justify-center text-white text-[9px] font-bold shadow-md pin-pulse">
            2
          </span>
        </button>

        <!-- Hotspot 3: Halo -->
        <button onclick="selectWidgetHotspot('halo')" class="absolute top-[38%] left-[48%] -translate-x-1/2 -translate-y-1/2 group z-20 focus:outline-none">
          <span class="w-5 h-5 rounded-full bg-blue-500/90 border border-white flex items-center justify-center text-white text-[9px] font-bold shadow-md pin-pulse">
            3
          </span>
        </button>

        <!-- Hotspot 4: Sidepod -->
        <button onclick="selectWidgetHotspot('sidepod')" class="absolute top-[62%] left-[54%] -translate-x-1/2 -translate-y-1/2 group z-20 focus:outline-none">
          <span class="w-5 h-5 rounded-full bg-emerald-500/90 border border-white flex items-center justify-center text-white text-[9px] font-bold shadow-md pin-pulse">
            4
          </span>
        </button>

        <!-- Hotspot 5: Rear Wing -->
        <button onclick="selectWidgetHotspot('rear-wing')" class="absolute top-[32%] left-[82%] -translate-x-1/2 -translate-y-1/2 group z-20 focus:outline-none">
          <span class="w-5 h-5 rounded-full bg-purple-500/90 border border-white flex items-center justify-center text-white text-[9px] font-bold shadow-md pin-pulse">
            5
          </span>
        </button>
      </div>

      <!-- Hotspot Details Card -->
      <div id="w-hotspot-card" class="p-3 rounded-xl bg-slate-900/90 border border-[var(--border)] text-xs font-mono space-y-1.5">
        <!-- Rendered by JS -->
      </div>

      <!-- Quick Telemetry Row -->
      <div class="grid grid-cols-4 gap-2 text-xs font-mono">
        <div class="p-2 rounded-lg bg-slate-900/80 border border-[var(--border)] text-center">
          <span class="text-[9px] text-[var(--muted-foreground)] block uppercase">DOWNFORCE</span>
          <div class="text-sm font-bold text-white mt-0.5">42.5% F / 57.5% R</div>
        </div>

        <div class="p-2 rounded-lg bg-slate-900/80 border border-[var(--border)] text-center">
          <span class="text-[9px] text-[var(--muted-foreground)] block uppercase">DRAG (CD)</span>
          <div class="text-sm font-bold text-amber-400 mt-0.5" id="w-cd-val">0.88</div>
        </div>

        <div class="p-2 rounded-lg bg-slate-900/80 border border-[var(--border)] text-center">
          <span class="text-[9px] text-[var(--muted-foreground)] block uppercase">TOP SPEED</span>
          <div class="text-sm font-bold text-emerald-400 mt-0.5" id="w-spd-val">334 KM/H</div>
        </div>

        <div class="p-2 rounded-lg bg-slate-900/80 border border-[var(--border)] text-center">
          <span class="text-[9px] text-[var(--muted-foreground)] block uppercase">TIRE BULK</span>
          <div class="text-sm font-bold text-red-400 mt-0.5">102&deg;C (Soft)</div>
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

    const W_HOTSPOTS = {{
      "front-wing": {{
        title: "1. Multi-Element Front Wing & Inwash Flaps",
        info: "Generates 42.5% front downforce (-1,120 kg @ 300 km/h) and conditions airflow into the underfloor venturi strakes.",
        spec: "Angle of Attack: 14.2° | Ride Height: 28 mm"
      }},
      "wheels": {{
        title: "2. Pirelli 18-inch Wheels & Carbon-Carbon Brakes",
        info: "Low-profile BBS forged rims. Operates in 95°C - 110°C thermal window. Brake discs withstand 1,000°C under deceleration.",
        spec: "Peak Decel: -5.2 G | 23.5 psi Front / 21.0 psi Rear"
      }},
      "halo": {{
        title: "3. Titanium Halo Structure & Cockpit Telemetry",
        info: "Grade 5 titanium structure withstanding 120 kN static crushing loads with aerodynamic fairing feeding the engine airbox.",
        spec: "Weight: 9 kg | Load Rating: 120 kN | OLED HUD"
      }},
      "sidepod": {{
        title: "4. Sculptured Sidepods & Ground-Effect Venturi Tunnels",
        info: "Dual underfloor venturi channels generate over 60% of total aerodynamic load through ground effect suction.",
        spec: "Underfloor Pressure: -14.8 kPa | Cooling Louvres: 8 Open"
      }},
      "rear-wing": {{
        title: "5. Rear Wing Assembly & Hydraulic DRS Actuator",
        info: "Generates 57.5% rear downforce. DRS opens flap to shed 28.5% drag, delivering +18 km/h overtake boost on straights.",
        spec: "DRS Gain: +18 km/h | Beam Wing Load: 18% of Rear"
      }}
    }};

    let wDRSOpen = false;

    function selectWidgetHotspot(key) {{
      const h = W_HOTSPOTS[key];
      if (!h) return;
      document.getElementById("w-hotspot-card").innerHTML = `
        <div class="flex justify-between font-bold border-b border-slate-800 pb-1">
          <span class="text-red-400">${{h.title}}</span>
          <span class="text-emerald-400 text-[10px]">AERO ACTIVE</span>
        </div>
        <p class="text-slate-300 text-[11px] leading-relaxed mt-1">${{h.info}}</p>
        <div class="text-[10px] text-slate-400 pt-1 border-t border-slate-800/80 font-bold">${{h.spec}}</div>
      `;
    }}

    function toggleWidgetDRS() {{
      wDRSOpen = !wDRSOpen;
      const btnTxt = document.getElementById("w-drs-txt");
      const cdVal = document.getElementById("w-cd-val");
      const spdVal = document.getElementById("w-spd-val");
      if (wDRSOpen) {{
        btnTxt.textContent = "DRS: OPEN";
        btnTxt.className = "text-emerald-400";
        cdVal.textContent = "0.63";
        spdVal.textContent = "352 KM/H";
      }} else {{
        btnTxt.textContent = "DRS: CLOSED";
        btnTxt.className = "text-slate-300";
        cdVal.textContent = "0.88";
        spdVal.textContent = "334 KM/H";
      }}
    }}

    function setWidgetTab(t) {{
      const tabs = ['car', 'gen', 'telemetry', 'degradation'];
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
      if (t === 'car') selectWidgetHotspot('front-wing');
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
          <div class="text-white font-bold my-1">Medium ➔ Hard</div>
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
          <div class="text-white font-bold my-1">Soft ➔ Hard ➔ Med</div>
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
          <div class="text-white font-bold my-1">Hard ➔ Soft</div>
          <div class="text-[11px] text-slate-300">Stint 1: L1-${{p1_C}} (SC Window)</div>
          <div class="flex justify-between text-[11px] text-slate-400 mt-2 pt-1 border-t border-slate-800">
            <span>Dividend: +12s Free</span>
            <span class="text-blue-400 font-bold">12.8% Win Prob</span>
          </div>
        </div>
      `;
    }}

    window.addEventListener('DOMContentLoaded', () => {{
      selectWidgetHotspot('front-wing');
      runWidgetStrategyEngine();
    }});
  </script>
</body>
</html>
"""

with open(WIDGET_PATH, "w", encoding="utf-8") as f:
    f.write(widget_html)

print("Saved updated widget with original F1 car successfully!")
