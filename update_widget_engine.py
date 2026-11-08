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
      background: rgba(225, 6, 0, 0.2);
      border-color: #E10600;
      color: #FFFFFF;
      font-weight: 700;
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
            Formula 1 AI Race Strategy Generator & Platform
            <span class="text-xs font-mono px-2 py-0.5 rounded-full bg-emerald-950 text-emerald-400 border border-emerald-800 font-semibold">
              ● Strategy Engine
            </span>
          </h2>
          <p class="text-xs text-[var(--muted-foreground)]">
            Resolving: <span class="text-red-400 italic font-semibold">"How do race strategies influence Formula 1 performance?"</span>
          </p>
        </div>
      </div>

      <div class="flex items-center gap-2 text-xs font-mono">
        <button onclick="runStrategyEngine()" class="px-3 py-1.5 rounded-lg bg-red-600 hover:bg-red-500 text-white font-bold flex items-center gap-1.5 shadow transition">
          <span>⚡</span> Re-Calculate Plans
        </button>
      </div>
    </div>

    <!-- STRATEGIC KPIS -->
    <div class="grid grid-cols-2 md:grid-cols-4 gap-2.5 text-xs">
      <div class="p-2.5 rounded-xl bg-slate-900/70 border border-[var(--border)] border-l-4 border-l-red-500">
        <span class="text-[10px] font-mono text-[var(--muted-foreground)] block uppercase">Undercut Win Rate</span>
        <div class="text-lg font-black text-white mt-0.5">68.4%</div>
        <span class="text-[10px] text-emerald-400 font-mono">+1.74s gap gain</span>
      </div>

      <div class="p-3 rounded-xl bg-slate-900/70 border border-[var(--border)] border-l-4 border-l-amber-500">
        <span class="text-[10px] font-mono text-[var(--muted-foreground)] block uppercase">SC Pit Dividend</span>
        <div class="text-lg font-black text-white mt-0.5">+12.0s Free Stop</div>
        <span class="text-[10px] text-amber-400 font-mono">Pit loss: 9.8s vs 22s</span>
      </div>

      <div class="p-3 rounded-xl bg-slate-900/70 border border-[var(--border)] border-l-4 border-l-emerald-500">
        <span class="text-[10px] font-mono text-[var(--muted-foreground)] block uppercase">Strategy Podiums</span>
        <div class="text-lg font-black text-white mt-0.5">42.8% Delta</div>
        <span class="text-[10px] text-slate-300 font-mono">Pit lane overtakes</span>
      </div>

      <div class="p-3 rounded-xl bg-slate-900/70 border border-[var(--border)] border-l-4 border-l-purple-500">
        <span class="text-[10px] font-mono text-[var(--muted-foreground)] block uppercase">Fuel Burn Rate</span>
        <div class="text-lg font-black text-white mt-0.5">-0.062 s/lap</div>
        <span class="text-[10px] text-purple-300 font-mono">110kg consumption</span>
      </div>
    </div>

    <!-- TABS -->
    <div class="flex gap-2 border-b border-[var(--border)] pb-2 text-xs font-mono">
      <button onclick="setWidgetTab('gen')" id="wtab-gen" class="tab-active px-3 py-1.5 rounded-lg border border-[var(--border)] transition">
        ⚡ Strategy Generator (Plan A/B/C)
      </button>
      <button onclick="setWidgetTab('telemetry')" id="wtab-telemetry" class="px-3 py-1.5 rounded-lg border border-[var(--border)] text-[var(--muted-foreground)] hover:text-white transition">
        ⏱️ Telemetry & Stints
      </button>
      <button onclick="setWidgetTab('degradation')" id="wtab-degradation" class="px-3 py-1.5 rounded-lg border border-[var(--border)] text-[var(--muted-foreground)] hover:text-white transition">
        📉 Tire Degradation
      </button>
      <button onclick="setWidgetTab('battles')" id="wtab-battles" class="px-3 py-1.5 rounded-lg border border-[var(--border)] text-[var(--muted-foreground)] hover:text-white transition">
        ⚔️ 2024 Battle Matrix
      </button>
    </div>

    <!-- VIEW 1: STRATEGY GENERATOR -->
    <div id="wview-gen" class="space-y-4">
      
      <!-- Interactive Inputs Bar -->
      <div class="p-3 bg-slate-950/80 rounded-xl border border-slate-800 grid grid-cols-2 md:grid-cols-4 gap-3 text-xs font-mono">
        <div>
          <span class="text-[10px] text-slate-400 block mb-1">CIRCUIT</span>
          <select id="wsel-circuit" onchange="runStrategyEngine()" class="w-full bg-slate-900 border border-slate-700 text-white rounded p-1.5 text-xs">
            <option value="3" selected>Bahrain (57 Laps)</option>
            <option value="6">Monaco (78 Laps)</option>
            <option value="9">Silverstone (52 Laps)</option>
            <option value="13">Spa (44 Laps)</option>
            <option value="14">Monza (53 Laps)</option>
            <option value="32">Mexico (71 Laps, 2227m)</option>
            <option value="80">Las Vegas (50 Laps)</option>
          </select>
        </div>

        <div>
          <span class="text-[10px] text-slate-400 block mb-1">GRID POSITION</span>
          <select id="wsel-grid" onchange="runStrategyEngine()" class="w-full bg-slate-900 border border-slate-700 text-white rounded p-1.5 text-xs">
            <option value="1" selected>Pole Position (P1)</option>
            <option value="3">Row 2 (P3)</option>
            <option value="6">Row 3 (P6)</option>
            <option value="10">Midfield (P10)</option>
            <option value="16">Back Grid (P16)</option>
          </select>
        </div>

        <div>
          <span class="text-[10px] text-slate-400 block mb-1">TRACK TEMP (&deg;C)</span>
          <div class="flex items-center gap-1.5">
            <input type="range" id="wsel-temp" min="20" max="55" value="34" oninput="document.getElementById('wtemp-num').textContent = this.value + '°C'; runStrategyEngine();" class="w-full accent-red-600">
            <span id="wtemp-num" class="w-10 text-right font-bold text-slate-200">34&deg;C</span>
          </div>
        </div>

        <div>
          <span class="text-[10px] text-slate-400 block mb-1">SAFETY CAR RISK</span>
          <select id="wsel-sc" onchange="runStrategyEngine()" class="w-full bg-slate-900 border border-slate-700 text-white rounded p-1.5 text-xs">
            <option value="LOW">Low (&lt;20%)</option>
            <option value="MED" selected>Medium (~40%)</option>
            <option value="HIGH">High (&gt;75%)</option>
          </select>
        </div>
      </div>

      <!-- Generated 3 Strategy Cards -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-3" id="wplans-cards-grid">
        <!-- Rendered dynamically -->
      </div>

      <!-- Live Contingency Triggers -->
      <div class="p-3 bg-slate-900/80 rounded-xl border border-slate-800 text-xs font-mono space-y-1.5">
        <span class="font-bold text-white flex items-center gap-1.5 text-xs">
          <span>📋</span> Pit-Wall Strategic Decision Trigger Checklist:
        </span>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-2 text-[11px] pt-1">
          <div class="p-2 bg-slate-950 rounded border border-slate-800 text-slate-300">
            <span class="text-red-400 font-bold block">1. Rival Undercut Alert</span>
            If car behind pits within 1.8s: <strong>Box on next lap</strong> to defend track position with fresh tire warmup.
          </div>
          <div class="p-2 bg-slate-950 rounded border border-slate-800 text-slate-300">
            <span class="text-amber-400 font-bold block">2. Safety Car Window</span>
            If SC occurs between L18-L36: <strong>Box immediately for Hard compound</strong>, harvesting a 12s free pit dividend.
          </div>
        </div>
      </div>

    </div>

    <!-- VIEW 2: TELEMETRY & STINTS -->
    <div id="wview-telemetry" class="space-y-4 hidden">
      <div class="flex flex-wrap items-center justify-between gap-3 text-xs">
        <div class="flex flex-wrap items-center gap-1.5" id="wdriver-toggles"></div>
        <label class="flex items-center gap-1.5 font-mono text-slate-300 cursor-pointer">
          <input type="checkbox" id="wtoggle-smooth" onchange="renderWidgetCharts()" checked class="rounded bg-slate-950 border-slate-700 text-red-600">
          <span>3-Lap Rolling Smooth</span>
        </label>
      </div>

      <div class="relative w-full h-60 bg-slate-950/80 rounded-xl p-2 border border-slate-800">
        <svg id="wpace-svg" class="w-full h-full" preserveAspectRatio="none"></svg>
      </div>

      <div class="space-y-1.5 bg-slate-950/60 p-3 rounded-xl border border-slate-800">
        <div class="flex items-center justify-between text-xs font-mono text-slate-400 mb-1">
          <span class="font-bold text-white">DRIVER STINT GANTT TIMELINE</span>
          <div class="flex items-center gap-2">
            <span class="inline-flex items-center gap-1 text-[11px]"><span class="w-2 h-2 rounded-full bg-red-600"></span> Soft</span>
            <span class="inline-flex items-center gap-1 text-[11px]"><span class="w-2 h-2 rounded-full bg-yellow-400"></span> Medium</span>
            <span class="inline-flex items-center gap-1 text-[11px]"><span class="w-2 h-2 rounded-full bg-white"></span> Hard</span>
          </div>
        </div>
        <div id="wstint-container" class="space-y-1.5"></div>
      </div>
    </div>

    <!-- VIEW 3: TIRE DEGRADATION -->
    <div id="wview-degradation" class="space-y-4 hidden">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs font-mono">
        <div class="p-3 rounded-xl bg-red-950/30 border border-red-900/60">
          <div class="flex justify-between items-center text-red-400 font-bold">
            <span>C3 SOFT</span>
            <span class="text-[10px] bg-red-900/60 px-1.5 py-0.5 rounded text-white">Cliff: L16</span>
          </div>
          <div class="text-xl font-black text-white mt-1">+0.082 s/lap</div>
          <span class="text-[11px] text-slate-400">High grip launch, rapid thermal wear</span>
        </div>

        <div class="p-3 rounded-xl bg-amber-950/30 border border-amber-900/60">
          <div class="flex justify-between items-center text-amber-400 font-bold">
            <span>C2 MEDIUM</span>
            <span class="text-[10px] bg-amber-900/60 px-1.5 py-0.5 rounded text-white">Cliff: L26</span>
          </div>
          <div class="text-xl font-black text-white mt-1">+0.052 s/lap</div>
          <span class="text-[11px] text-slate-400">Balanced stint flexibility</span>
        </div>

        <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700">
          <div class="flex justify-between items-center text-slate-200 font-bold">
            <span>C1 HARD</span>
            <span class="text-[10px] bg-slate-800 px-1.5 py-0.5 rounded text-white">Cliff: L38</span>
          </div>
          <div class="text-xl font-black text-white mt-1">+0.038 s/lap</div>
          <span class="text-[11px] text-slate-400">High durability, essential for 1-stops</span>
        </div>
      </div>

      <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs text-slate-300 leading-relaxed space-y-1.5">
        <span class="font-bold text-white flex items-center gap-1.5 text-xs">
          <span>⚠️</span> The Thermal Cliff Equation:
        </span>
        <p>
          Degradation accelerates non-linearly when rubber thickness thins past the heat dissipation threshold:
          <span class="font-mono text-red-400 font-semibold block mt-1">Penalty = ((Age - Cliff_Lap)^1.35) * 0.28s / lap</span>
        </p>
      </div>
    </div>

    <!-- VIEW 4: BATTLES MATRIX -->
    <div id="wview-battles" class="space-y-4 hidden">
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
          <tbody class="divide-y divide-slate-800 text-slate-300" id="wbattles-table"></tbody>
        </table>
      </div>
    </div>

  </div>

  <script>
    const F1_DATA = {json_data_str};
    let wSelected = ["VER", "PER", "SAI", "LEC", "NOR"];

    window.addEventListener("DOMContentLoaded", () => {{
      runStrategyEngine();
      renderWidgetToggles();
      renderWidgetCharts();
      renderWidgetStints();
      renderWidgetBattles();
    }});

    function setWidgetTab(tab) {{
      ["gen", "telemetry", "degradation", "battles"].forEach(t => {{
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

    function runStrategyEngine() {{
      const cId = parseInt(document.getElementById("wsel-circuit").value);
      const grid = parseInt(document.getElementById("wsel-grid").value);
      const temp = parseFloat(document.getElementById("wsel-temp").value);
      const sc = document.getElementById("wsel-sc").value;

      const circuit = F1_DATA.circuits.find(c => c.circuitId === cId) || F1_DATA.circuits[0];
      const totalLaps = (cId === 6) ? 78 : ((cId === 13) ? 44 : ((cId === 32) ? 71 : 57));

      const plans = [
        {{
          code: "PLAN A (PRIMARY OPTIMAL)",
          name: (circuit.typical_stops === 1) ? "1-Stop Medium → Hard" : "2-Stop Soft → Hard → Soft",
          color: "border-red-600",
          stints: (circuit.typical_stops === 1) 
            ? [{{c:"M", l: Math.floor(totalLaps*0.42), col:"#FFF200", tc:"#000"}}, {{c:"H", l: totalLaps - Math.floor(totalLaps*0.42), col:"#FFF", tc:"#000"}}]
            : [{{c:"S", l: Math.floor(totalLaps*0.28), col:"#E10600", tc:"#FFF"}}, {{c:"H", l: Math.floor(totalLaps*0.37), col:"#FFF", tc:"#000"}}, {{c:"S", l: totalLaps - Math.floor(totalLaps*0.65), col:"#E10600", tc:"#FFF"}}],
          pit_win: (circuit.typical_stops === 1) ? `Laps ${{Math.floor(totalLaps*0.40)}}-${{Math.floor(totalLaps*0.44)}}` : `L${{Math.floor(totalLaps*0.26)}}-${{Math.floor(totalLaps*0.29)}} & L${{Math.floor(totalLaps*0.63)}}-${{Math.floor(totalLaps*0.66)}}`,
          finish: (grid <= 2) ? "P1 - Victory" : ((grid <= 6) ? "P2 - Podium" : "P4 - Top 5"),
          conf: "95%"
        }},
        {{
          code: "PLAN B (UNDERCUT ATTACK)",
          name: "2-Stop Soft → Hard → Medium",
          color: "border-amber-500",
          stints: [
            {{c:"S", l: Math.floor(totalLaps*0.24), col:"#E10600", tc:"#FFF"}},
            {{c:"H", l: Math.floor(totalLaps*0.36), col:"#FFF", tc:"#000"}},
            {{c:"M", l: totalLaps - Math.floor(totalLaps*0.60), col:"#FFF200", tc:"#000"}}
          ],
          pit_win: `Laps ${{Math.floor(totalLaps*0.22)}}-${{Math.floor(totalLaps*0.25)}} & L${{Math.floor(totalLaps*0.58)}}-${{Math.floor(totalLaps*0.61)}}`,
          finish: (grid <= 5) ? "P1 - P2 (Undercut Jump)" : "P3 - P5",
          conf: "89%"
        }},
        {{
          code: "PLAN C (SC OVERCUT GAMBLE)",
          name: "1-Stop Hard → Medium (Long Stint)",
          color: "border-purple-500",
          stints: [
            {{c:"H", l: Math.floor(totalLaps*0.62), col:"#FFF", tc:"#000"}},
            {{c:"M", l: totalLaps - Math.floor(totalLaps*0.62), col:"#FFF200", tc:"#000"}}
          ],
          pit_win: `Laps ${{Math.floor(totalLaps*0.60)}}-${{Math.floor(totalLaps*0.65)}}`,
          finish: (sc === "HIGH") ? "P1 - P3 (Free SC Stop)" : "P6 - P8",
          conf: "82%"
        }}
      ];

      const c = document.getElementById("wplans-cards-grid");
      c.innerHTML = "";
      plans.forEach(p => {{
        let stintHtml = "";
        p.stints.forEach(s => {{
          const pct = (s.l / totalLaps) * 100;
          stintHtml += `<div style="width:${{pct}}%; background:${{s.col}}; color:${{s.tc}};" class="h-5 rounded flex items-center justify-center font-bold text-[9px] font-mono">
            ${{s.c}} ${{s.l}}L
          </div>`;
        }});

        c.innerHTML += `
          <div class="p-3.5 rounded-xl bg-slate-950/80 border-t-4 ${{p.color}} border border-slate-800 space-y-2.5">
            <div class="flex justify-between items-center text-[10px] font-mono">
              <span class="text-red-400 font-bold">${{p.code}}</span>
              <span class="text-emerald-400 font-bold">${{p.conf}} Conf</span>
            </div>
            <div class="font-bold text-white text-xs">${{p.name}}</div>
            <div class="flex gap-1 bg-slate-900 p-1 rounded">${{stintHtml}}</div>
            <div class="grid grid-cols-2 gap-1 text-[11px] font-mono pt-1 border-t border-slate-800">
              <div><span class="text-slate-500 block text-[9px]">PIT WINDOW</span><span class="text-amber-400 font-bold">${{p.pit_win}}</span></div>
              <div><span class="text-slate-500 block text-[9px]">PROJECTED</span><span class="text-emerald-400 font-black">${{p.finish}}</span></div>
            </div>
          </div>
        `;
      }});
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
          bars += `<div style="width:${{pct}}%; background:${{colMap[s.comp]}}; color:${{textMap[s.comp]}};" class="h-4 rounded flex items-center justify-center font-bold text-[9px] shadow-sm">
            ${{s.comp[0]}} ${{s.dur}}L
          </div>`;
        }});
        row.innerHTML = `<span class="w-8 font-bold text-slate-300">${{d}}</span><div class="flex-1 flex gap-0.5 bg-slate-900 p-0.5 rounded">${{bars}}</div>`;
        c.appendChild(row);
      }});
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
  </script>
</body>
</html>
"""

with open(WIDGET_PATH, "w", encoding="utf-8") as f:
    f.write(widget_html)

print("Updated widget with Strategy Generator successfully!")
