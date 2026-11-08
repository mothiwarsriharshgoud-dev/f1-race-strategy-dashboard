import json
import os

DATA_PATH = "C:/Users/Main User/.gemini/antigravity/scratch/f1-race-strategy-dashboard/data/f1_strategy_dataset.json"
WIDGET_PATH = "C:/Users/Main User/.gemini/antigravity/brain/bb0fc362-bdeb-4a83-b7c8-80ce516a46a3/f1_race_strategy_widget.html"

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
    @import url('https://fonts.googleapis.com/css2?family=Titillium+Web:wght@400;600;700;900&family=JetBrains+Mono:wght@400;600;700&display=swap');
    
    body {{
      font-family: 'Titillium Web', -apple-system, BlinkMacSystemFont, sans-serif;
    }}
    .mono {{
      font-family: 'JetBrains Mono', monospace;
    }}
    .tab-active {{
      background: rgba(225, 6, 0, 0.15);
      border-color: #E10600;
      color: #FFFFFF;
      font-weight: 700;
    }}
    .stint-pill {{
      transition: all 0.2s ease;
    }}
    .stint-pill:hover {{
      filter: brightness(1.2);
      transform: translateY(-1px);
    }}
  </style>
</head>
<body class="bg-transparent text-[var(--foreground)] antialiased p-2 md:p-4">

  <!-- MAIN WRAPPER CARD -->
  <div class="bg-[var(--card)] text-[var(--foreground)] border border-[var(--border)] rounded-2xl p-4 md:p-6 shadow-2xl space-y-5">
    
    <!-- HEADER -->
    <div class="flex flex-wrap items-center justify-between gap-3 border-b border-[var(--border)] pb-4">
      <div class="flex items-center gap-3">
        <div class="bg-red-600 text-white font-black px-2.5 py-1 rounded text-base tracking-wider flex items-center gap-1 shadow-md shadow-red-900/40">
          <span>F1</span>
          <span class="text-xs bg-black/40 px-1 py-0.5 rounded font-mono">P32</span>
        </div>
        <div>
          <h2 class="text-base md:text-lg font-bold text-[var(--foreground)] flex items-center gap-2">
            Formula 1 Race Strategy Dashboard
            <span class="text-xs font-mono px-2 py-0.5 rounded-full bg-emerald-950 text-emerald-400 border border-emerald-800">
              Interactive Telemetry
            </span>
          </h2>
          <p class="text-xs text-[var(--muted-foreground)]">
            Resolving: <span class="text-red-400 italic font-semibold">"How do race strategies influence Formula 1 performance?"</span>
          </p>
        </div>
      </div>

      <!-- Quick Session Badge -->
      <div class="flex items-center gap-2 text-xs font-mono bg-slate-900/80 px-3 py-1.5 rounded-lg border border-[var(--border)]">
        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
        <span class="text-slate-200">2024 Sakhir Benchmark (57 Laps)</span>
      </div>
    </div>

    <!-- STRATEGIC KPIS -->
    <div class="grid grid-cols-2 md:grid-cols-4 gap-3 text-xs">
      <div class="p-3 rounded-xl bg-slate-900/60 border border-[var(--border)] border-l-4 border-l-red-500">
        <span class="text-[11px] font-mono text-[var(--muted-foreground)] block uppercase">Undercut Win Rate</span>
        <div class="text-xl font-black text-white mt-0.5">68.4%</div>
        <span class="text-[11px] text-emerald-400 font-mono">+1.74s gap overturn</span>
      </div>

      <div class="p-3 rounded-xl bg-slate-900/60 border border-[var(--border)] border-l-4 border-l-amber-500">
        <span class="text-[11px] font-mono text-[var(--muted-foreground)] block uppercase">SC / VSC Dividend</span>
        <div class="text-xl font-black text-white mt-0.5">+9.4s - 12.0s</div>
        <span class="text-[11px] text-amber-400 font-mono">Free stop window</span>
      </div>

      <div class="p-3 rounded-xl bg-slate-900/60 border border-[var(--border)] border-l-4 border-l-emerald-500">
        <span class="text-[11px] font-mono text-[var(--muted-foreground)] block uppercase">Strategy-Driven Podiums</span>
        <div class="text-xl font-black text-white mt-0.5">42.8%</div>
        <span class="text-[11px] text-slate-300 font-mono">Net delta vs grid pos</span>
      </div>

      <div class="p-3 rounded-xl bg-slate-900/60 border border-[var(--border)] border-l-4 border-l-purple-500">
        <span class="text-[11px] font-mono text-[var(--muted-foreground)] block uppercase">Fuel Burn Pace Gain</span>
        <div class="text-xl font-black text-white mt-0.5">-0.062 s/lap</div>
        <span class="text-[11px] text-purple-300 font-mono">110kg weight drop</span>
      </div>
    </div>

    <!-- TAB CONTROLS -->
    <div class="flex gap-2 overflow-x-auto border-b border-[var(--border)] pb-2 text-xs font-mono">
      <button onclick="setWidgetTab('telemetry')" id="wtab-telemetry" class="tab-active px-3 py-1.5 rounded-lg border border-[var(--border)] transition">
        ⏱️ Lap Pace & Stints
      </button>
      <button onclick="setWidgetTab('degradation')" id="wtab-degradation" class="px-3 py-1.5 rounded-lg border border-[var(--border)] text-[var(--muted-foreground)] hover:text-white transition">
        📉 Tire Degradation
      </button>
      <button onclick="setWidgetTab('undercut')" id="wtab-undercut" class="px-3 py-1.5 rounded-lg border border-[var(--border)] text-[var(--muted-foreground)] hover:text-white transition">
        ⚡ Undercut Battles
      </button>
      <button onclick="setWidgetTab('simulator')" id="wtab-simulator" class="px-3 py-1.5 rounded-lg border border-[var(--border)] text-[var(--muted-foreground)] hover:text-white transition">
        🎮 Strategy Simulator
      </button>
    </div>

    <!-- TAB 1: TELEMETRY & STINTS -->
    <div id="wview-telemetry" class="space-y-4">
      
      <!-- Driver Filter Pills & Smoothing Toggle -->
      <div class="flex flex-wrap items-center justify-between gap-3 text-xs">
        <div class="flex flex-wrap items-center gap-1.5" id="wdriver-toggles">
          <!-- populated dynamically -->
        </div>

        <label class="flex items-center gap-1.5 font-mono text-slate-300 cursor-pointer">
          <input type="checkbox" id="wtoggle-smooth" onchange="renderWidgetCharts()" checked class="rounded bg-slate-950 border-slate-700 text-red-600">
          <span>3-Lap Rolling Smooth</span>
        </label>
      </div>

      <!-- SVG Pace Chart -->
      <div class="relative w-full h-64 bg-slate-950/80 rounded-xl p-2 border border-slate-800">
        <svg id="wpace-svg" class="w-full h-full" preserveAspectRatio="none"></svg>
      </div>

      <!-- Stint Gantt Timeline -->
      <div class="space-y-1.5 bg-slate-950/60 p-3 rounded-xl border border-slate-800">
        <div class="flex items-center justify-between text-xs font-mono text-slate-400 mb-1">
          <span class="font-bold text-white">DRIVER STINT GANTT TIMELINE (57 LAPS)</span>
          <div class="flex items-center gap-2">
            <span class="inline-flex items-center gap-1 text-[11px]"><span class="w-2 h-2 rounded-full bg-red-600"></span> Soft</span>
            <span class="inline-flex items-center gap-1 text-[11px]"><span class="w-2 h-2 rounded-full bg-yellow-400"></span> Medium</span>
            <span class="inline-flex items-center gap-1 text-[11px]"><span class="w-2 h-2 rounded-full bg-white"></span> Hard</span>
          </div>
        </div>
        <div id="wstint-container" class="space-y-1.5">
          <!-- populated dynamically -->
        </div>
      </div>
    </div>

    <!-- TAB 2: TIRE DEGRADATION -->
    <div id="wview-degradation" class="space-y-4 hidden">
      <div class="flex flex-wrap items-center justify-between gap-2 text-xs">
        <div>
          <span class="font-bold text-white text-sm">Compound Degradation Slopes</span>
          <p class="text-xs text-[var(--muted-foreground)]">Measured lap time decay per lap on tire set.</p>
        </div>
        <button id="wfuel-btn" onclick="toggleWidgetFuel()" class="px-2.5 py-1 rounded bg-red-600 text-white font-mono font-bold text-xs">
          Fuel Adjustment: ON (-0.062s/lap)
        </button>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs font-mono">
        <div class="p-3 rounded-xl bg-red-950/30 border border-red-900/60">
          <div class="flex justify-between items-center text-red-400 font-bold">
            <span>C3 SOFT</span>
            <span class="text-[10px] bg-red-900/60 px-1.5 py-0.5 rounded text-white">Cliff: L16</span>
          </div>
          <div class="text-xl font-black text-white mt-1">+0.082 s/lap</div>
          <span class="text-[11px] text-slate-400">High launch grip, rapid thermal wear</span>
        </div>

        <div class="p-3 rounded-xl bg-amber-950/30 border border-amber-900/60">
          <div class="flex justify-between items-center text-amber-400 font-bold">
            <span>C2 MEDIUM</span>
            <span class="text-[10px] bg-amber-900/60 px-1.5 py-0.5 rounded text-white">Cliff: L26</span>
          </div>
          <div class="text-xl font-black text-white mt-1">+0.052 s/lap</div>
          <span class="text-[11px] text-slate-400">Versatile race start & stint flexibility</span>
        </div>

        <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700">
          <div class="flex justify-between items-center text-slate-200 font-bold">
            <span>C1 HARD</span>
            <span class="text-[10px] bg-slate-800 px-1.5 py-0.5 rounded text-white">Cliff: L38</span>
          </div>
          <div class="text-xl font-black text-white mt-1">+0.038 s/lap</div>
          <span class="text-[11px] text-slate-400">Essential for long stints & 1-stops</span>
        </div>
      </div>

      <!-- Thermal Cliff Box -->
      <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs text-slate-300 leading-relaxed space-y-1.5">
        <span class="font-bold text-white flex items-center gap-1.5 text-xs">
          <span>⚠️</span> The Strategic Decision Rule:
        </span>
        <p>
          A pit stop is strictly optimal when the cumulative lap time lost to tire degradation exceeds the pit transit delta:
          <span class="font-mono text-red-400 font-semibold block mt-1">Total_Degradation_Loss &gt; (Pit_Transit_Loss [~21.8s] - New_Tyre_Pace_Advantage)</span>
        </p>
      </div>
    </div>

    <!-- TAB 3: UNDERCUT BATTLES -->
    <div id="wview-undercut" class="space-y-4 hidden">
      <div class="overflow-x-auto">
        <table class="w-full text-left text-xs font-mono">
          <thead class="bg-slate-900 text-slate-400 border-b border-slate-800">
            <tr>
              <th class="p-2">Grand Prix</th>
              <th class="p-2">Attacker / Defender</th>
              <th class="p-2">Tactic</th>
              <th class="p-2">Pre-Gap</th>
              <th class="p-2">Out-Lap Delta</th>
              <th class="p-2">Outcome</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-800 text-slate-300" id="wbattles-table">
            <!-- populated dynamically -->
          </tbody>
        </table>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
        <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2">
          <span class="font-bold text-white block">Pit Transit Loss Arbitrage</span>
          <div class="space-y-1.5 font-mono text-[11px]">
            <div class="flex justify-between">
              <span>Green Flag Normal:</span>
              <span class="font-bold text-red-400">21.8s</span>
            </div>
            <div class="flex justify-between">
              <span>Virtual Safety Car:</span>
              <span class="font-bold text-amber-400">12.4s (+9.4s gain)</span>
            </div>
            <div class="flex justify-between">
              <span>Full Safety Car:</span>
              <span class="font-bold text-emerald-400">9.8s (+12.0s gain)</span>
            </div>
          </div>
        </div>

        <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-800 space-y-1">
          <span class="font-bold text-white block">Strategic Implication</span>
          <p class="text-slate-300 text-[11px] leading-relaxed">
            Leading teams must react to an undercut within 1 lap or surrender track position. In contrast, mid-field runners often extend stints hoping for a Safety Car to achieve a free pit stop.
          </p>
        </div>
      </div>
    </div>

    <!-- TAB 4: STRATEGY SIMULATOR -->
    <div id="wview-simulator" class="space-y-4 hidden">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        
        <!-- Controls -->
        <div class="space-y-3 bg-slate-950/80 p-3.5 rounded-xl border border-slate-800 text-xs">
          <span class="font-bold text-white block text-sm">Strategy Scenario Controls</span>
          
          <div>
            <div class="flex justify-between font-mono text-[11px] text-slate-300">
              <span>Stint 1 (Pit Stop Lap):</span>
              <span id="wsim-l1" class="text-red-400 font-bold">Lap 15</span>
            </div>
            <input type="range" id="wslider-p1" min="10" max="28" value="15" oninput="runWidgetSimulation()" class="w-full accent-red-600 mt-1">
          </div>

          <div class="grid grid-cols-2 gap-2 font-mono text-xs">
            <div>
              <span class="text-[10px] text-slate-400 block">START COMPOUND</span>
              <select id="wsel-c1" onchange="runWidgetSimulation()" class="w-full bg-slate-900 border border-slate-700 rounded p-1 text-white">
                <option value="SOFT" selected>Soft (C3)</option>
                <option value="MEDIUM">Medium (C2)</option>
                <option value="HARD">Hard (C1)</option>
              </select>
            </div>
            <div>
              <span class="text-[10px] text-slate-400 block">STINT 2 COMPOUND</span>
              <select id="wsel-c2" onchange="runWidgetSimulation()" class="w-full bg-slate-900 border border-slate-700 rounded p-1 text-white">
                <option value="HARD" selected>Hard (C1)</option>
                <option value="MEDIUM">Medium (C2)</option>
                <option value="SOFT">Soft (C3)</option>
              </select>
            </div>
          </div>

          <div class="flex items-center justify-between font-mono text-xs pt-1 border-t border-slate-800">
            <label class="flex items-center gap-1.5 cursor-pointer">
              <input type="checkbox" id="wcheck-sc" onchange="runWidgetSimulation()" class="rounded bg-slate-900 text-emerald-500">
              <span>Safety Car Pit Stop</span>
            </label>
            <label class="flex items-center gap-1.5 cursor-pointer">
              <input type="checkbox" id="wcheck-2stop" onchange="runWidgetSimulation()" checked class="rounded bg-slate-900 text-red-500">
              <span>2-Stop Strategy</span>
            </label>
          </div>
        </div>

        <!-- Projected Outcome -->
        <div class="bg-slate-950/80 p-3.5 rounded-xl border border-slate-800 flex flex-col justify-between space-y-3 text-xs">
          <div>
            <div class="flex items-center justify-between">
              <span class="font-bold text-white text-sm">Projected Race Outcome</span>
              <span id="wsim-badge" class="px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-emerald-950 text-emerald-300 border border-emerald-800">
                OPTIMAL
              </span>
            </div>

            <div class="grid grid-cols-2 gap-2 mt-3 font-mono">
              <div class="p-2 bg-slate-900 rounded border border-slate-800">
                <span class="text-[10px] text-slate-400 block">DELTA TO WINNER</span>
                <span id="wsim-delta" class="text-base font-black text-emerald-400">+0.2s</span>
              </div>
              <div class="p-2 bg-slate-900 rounded border border-slate-800">
                <span class="text-[10px] text-slate-400 block">EST. FINISH</span>
                <span id="wsim-finish" class="text-base font-black text-amber-400">P1 - P2</span>
              </div>
            </div>

            <p id="wsim-verdict" class="text-slate-300 text-xs mt-3 leading-relaxed">
              Soft-Hard-Soft configuration delivers peak pace, managing degradation without hitting the thermal cliff.
            </p>
          </div>

          <div class="w-full h-6 rounded flex overflow-hidden font-mono text-[10px] font-bold text-black" id="wsim-bar">
            <!-- populated dynamically -->
          </div>
        </div>

      </div>
    </div>

  </div>

  <script>
    const F1_DATA = {json_data_str};
    let wSelected = ["VER", "PER", "SAI", "LEC", "NOR"];
    let wFuelOn = true;

    window.addEventListener("DOMContentLoaded", () => {{
      renderWidgetToggles();
      renderWidgetCharts();
      renderWidgetStints();
      renderWidgetBattles();
      runWidgetSimulation();
    }});

    function setWidgetTab(tab) {{
      ["telemetry", "degradation", "undercut", "simulator"].forEach(t => {{
        const b = document.getElementById(`wtab-${{t}}`);
        const v = document.getElementById(`wview-${{t}}`);
        if (t === tab) {{
          b.className = "tab-active px-3 py-1.5 rounded-lg border border-[var(--border)] transition";
          v.classList.remove("hidden");
        }} else {{
          b.className = "px-3 py-1.5 rounded-lg border border-[var(--border)] text-[var(--muted-foreground)] hover:text-white transition";
          v.classList.add("hidden");
        }}
      }});
      if (tab === "telemetry") renderWidgetCharts();
    }}

    function renderWidgetToggles() {{
      const c = document.getElementById("wdriver-toggles");
      c.innerHTML = "";
      F1_DATA.drivers.slice(0, 7).forEach(d => {{
        const isSel = wSelected.includes(d.code);
        const b = document.createElement("button");
        b.className = `px-2 py-0.5 rounded text-xs font-mono font-bold border ${{
          isSel ? 'bg-slate-800 text-white border-slate-600' : 'bg-slate-950 text-slate-500 border-slate-800'
        }}`;
        b.innerHTML = `<span class="w-2 h-2 rounded-full inline-block" style="background:${{d.color}}"></span> ${{d.code}}`;
        b.onclick = () => {{
          if (wSelected.includes(d.code)) {{
            if (wSelected.length > 1) wSelected = wSelected.filter(x => x !== d.code);
          }} else {{
            wSelected.push(d.code);
          }}
          renderWidgetToggles();
          renderWidgetCharts();
        }};
        c.appendChild(b);
      }});
    }}

    function renderWidgetCharts() {{
      const svg = document.getElementById("wpace-svg");
      svg.innerHTML = "";
      const isSmooth = document.getElementById("wtoggle-smooth").checked;
      const laps = F1_DATA.bahrain_telemetry_laps;

      const w = 700, h = 240, pL = 40, pR = 15, pT = 15, pB = 25;
      svg.setAttribute("viewBox", `0 0 ${{w}} ${{h}}`);

      // Grid
      for (let p = 94; p <= 100; p += 2) {{
        const y = pT + (h - pT - pB) * (p - 93.5) / 7;
        svg.innerHTML += `<line x1="${{pL}}" y1="${{y}}" x2="${{w - pR}}" y2="${{y}}" stroke="#1E232F" stroke-dasharray="2,2"/>`;
        svg.innerHTML += `<text x="${{pL - 4}}" y="${{y + 3}}" fill="#64748B" font-size="9" font-family="monospace" text-anchor="end">${{p}}s</text>`;
      }}

      for (let l = 10; l <= 50; l += 10) {{
        const x = pL + (w - pL - pR) * (l - 1) / 56;
        svg.innerHTML += `<line x1="${{x}}" y1="${{pT}}" x2="${{x}}" y2="${{h - pB}}" stroke="#1E232F" stroke-dasharray="2,2"/>`;
        svg.innerHTML += `<text x="${{x}}" y="${{h - 8}}" fill="#64748B" font-size="9" font-family="monospace" text-anchor="middle">L${{l}}</text>`;
      }}

      wSelected.forEach(dCode => {{
        const dInfo = F1_DATA.drivers.find(d => d.code === dCode) || {{ color: "#AAA" }};
        const dLaps = laps.filter(l => l.driver === dCode).sort((a,b) => a.lap - b.lap);
        if (dLaps.length === 0) return;

        let pts = [];
        dLaps.forEach((l, idx) => {{
          let val = l.lap_time;
          if (isSmooth && idx >= 2 && !l.is_pit) {{
            val = (dLaps[idx].lap_time + dLaps[idx-1].lap_time + dLaps[idx-2].lap_time) / 3;
          }}
          val = Math.max(93.5, Math.min(100.5, val));
          const x = pL + (w - pL - pR) * (l.lap - 1) / 56;
          const y = pT + (h - pT - pB) * (val - 93.5) / 7;
          pts.push(`${{x.toFixed(1)}},${{y.toFixed(1)}}`);
        }});
        svg.innerHTML += `<polyline points="${{pts.join(" ")}}" fill="none" stroke="${{dInfo.color}}" stroke-width="2" opacity="0.9"/>`;
      }});
    }}

    function renderWidgetStints() {{
      const c = document.getElementById("wstint-container");
      c.innerHTML = "";
      const driverStints = {{
        "VER": [{{comp: "SOFT", dur: 17}}, {{comp: "HARD", dur: 19}}, {{comp: "SOFT", dur: 21}}],
        "PER": [{{comp: "SOFT", dur: 12}}, {{comp: "HARD", dur: 24}}, {{comp: "SOFT", dur: 21}}],
        "SAI": [{{comp: "SOFT", dur: 14}}, {{comp: "HARD", dur: 21}}, {{comp: "HARD", dur: 22}}],
        "LEC": [{{comp: "SOFT", dur: 11}}, {{comp: "HARD", dur: 23}}, {{comp: "HARD", dur: 23}}],
        "NOR": [{{comp: "SOFT", dur: 13}}, {{comp: "HARD", dur: 20}}, {{comp: "HARD", dur: 24}}],
      }};

      const colMap = {{ "SOFT": "#E10600", "MEDIUM": "#FFF200", "HARD": "#FFFFFF" }};
      const textMap = {{ "SOFT": "#FFF", "MEDIUM": "#000", "HARD": "#000" }};

      Object.keys(driverStints).forEach(d => {{
        const row = document.createElement("div");
        row.className = "flex items-center gap-2 font-mono text-[11px]";
        let bars = "";
        driverStints[d].forEach(s => {{
          const pct = (s.dur / 57) * 100;
          bars += `<div style="width:${{pct}}%; background:${{colMap[s.comp]}}; color:${{textMap[s.comp]}};" class="stint-pill h-4 rounded flex items-center justify-center font-bold text-[9px] shadow-sm">
            ${{s.comp[0]}} ${{s.dur}}L
          </div>`;
        }});
        row.innerHTML = `<span class="w-8 font-bold text-slate-300">${{d}}</span><div class="flex-1 flex gap-0.5 bg-slate-900 p-0.5 rounded">${{bars}}</div>`;
        c.appendChild(row);
      }});
    }}

    function toggleWidgetFuel() {{
      wFuelOn = !wFuelOn;
      const b = document.getElementById("wfuel-btn");
      b.textContent = wFuelOn ? "Fuel Adjustment: ON (-0.062s/lap)" : "Fuel Adjustment: OFF (Raw)";
      b.className = wFuelOn ? "px-2.5 py-1 rounded bg-red-600 text-white font-mono font-bold text-xs" : "px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-mono font-bold text-xs";
    }}

    function renderWidgetBattles() {{
      const tb = document.getElementById("wbattles-table");
      tb.innerHTML = "";
      F1_DATA.pit_stop_battles.slice(0, 4).forEach(b => {{
        tb.innerHTML += `
          <tr class="hover:bg-slate-900/40">
            <td class="p-1.5 font-bold text-white">${{b.race}}</td>
            <td class="p-1.5"><span class="text-emerald-400 font-bold">${{b.attacking_driver}}</span> vs ${{b.defending_driver}}</td>
            <td class="p-1.5 text-slate-400">${{b.tactic}}</td>
            <td class="p-1.5">${{b.pre_gap_sec}}s</td>
            <td class="p-1.5 font-bold text-emerald-400">${{b.outlap_delta_sec}}s</td>
            <td class="p-1.5 text-emerald-300 font-bold">${{b.outcome.split(' ')[0]}}</td>
          </tr>
        `;
      }});
    }}

    function runWidgetSimulation() {{
      const p1 = parseInt(document.getElementById("wslider-p1").value);
      const c1 = document.getElementById("wsel-c1").value;
      const c2 = document.getElementById("wsel-c2").value;
      const sc = document.getElementById("wcheck-sc").checked;
      const is2Stop = document.getElementById("wcheck-2stop").checked;

      document.getElementById("wsim-l1").textContent = `Lap ${{p1}}`;

      let delta = (p1 - 15) * 0.15;
      if (c1 === "HARD") delta += 3.2; // sluggish start
      if (sc) delta -= 11.8; // Safety car pit dividend
      if (!is2Stop) delta += 7.5; // High degradation penalty in closing laps

      const deltaTxt = (delta >= 0 ? "+" : "") + delta.toFixed(1) + "s";
      document.getElementById("wsim-delta").textContent = deltaTxt;

      const badge = document.getElementById("wsim-badge");
      const finish = document.getElementById("wsim-finish");
      const verdict = document.getElementById("wsim-verdict");

      if (delta <= 1.0) {{
        badge.textContent = "OPTIMAL";
        badge.className = "px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-emerald-950 text-emerald-300 border border-emerald-800";
        finish.textContent = "P1 - P2";
        finish.className = "text-base font-black text-amber-400";
        verdict.textContent = "Optimal strategy window. Fresh tire delta cleanly counteracts pit transit loss.";
      }} else if (delta <= 8.0) {{
        badge.textContent = "PODIUM CONTENDER";
        badge.className = "px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-amber-950 text-amber-300 border border-amber-800";
        finish.textContent = "P3 - P5";
        finish.className = "text-base font-black text-slate-200";
        verdict.textContent = "Solid points strategy, though late-stint degradation loses touch with the leader.";
      }} else {{
        badge.textContent = "SUB-OPTIMAL";
        badge.className = "px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-red-950 text-red-300 border border-red-800";
        finish.textContent = "P7 - P10";
        finish.className = "text-base font-black text-red-400";
        verdict.textContent = "Severe tire cliff penalty or poor compound alignment forfeiting track position.";
      }}

      // Sim bar
      const bar = document.getElementById("wsim-bar");
      const colMap = {{ "SOFT": "#E10600", "MEDIUM": "#FFF200", "HARD": "#FFFFFF" }};
      const textMap = {{ "SOFT": "#FFF", "MEDIUM": "#000", "HARD": "#000" }};
      const p1Pct = (p1 / 57) * 100;
      const p2Pct = is2Stop ? ((36 - p1) / 57) * 100 : ((57 - p1) / 57) * 100;
      const p3Pct = is2Stop ? (21 / 57) * 100 : 0;

      let bHtml = `<div style="width:${{p1Pct}}%; background:${{colMap[c1]}}; color:${{textMap[c1]}};" class="flex items-center justify-center">${{c1[0]}} ${{p1}}L</div>
                   <div style="width:${{p2Pct}}%; background:${{colMap[c2]}}; color:${{textMap[c2]}};" class="flex items-center justify-center">${{c2[0]}}</div>`;
      if (is2Stop) {{
        bHtml += `<div style="width:${{p3Pct}}%; background:#E10600; color:#FFF;" class="flex items-center justify-center">S 21L</div>`;
      }}
      bar.innerHTML = bHtml;
    }}
  </script>
</body>
</html>
"""

with open(WIDGET_PATH, "w", encoding="utf-8") as f:
    f.write(widget_html)

print(f"Successfully generated Generative UI Widget at: {WIDGET_PATH}")
