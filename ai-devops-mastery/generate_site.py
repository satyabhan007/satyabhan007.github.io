#!/usr/bin/env python3
import os
import json

BASE_DIR = "/home/satya/Downloads/SATYA/satyabhan007.github.io/ai-devops-mastery"
os.makedirs(BASE_DIR, exist_ok=True)

SHARED_CSS = """
:root {
  --bg: #0B0F17;
  --panel: #131B26;
  --card: #182232;
  --line: #223247;
  --txt: #E6EDF5;
  --mut: #8B9BB0;
  --amber: #F59E0B;
  --teal: #10B981;
  --blue: #3B82F6;
  --vio: #8B5CF6;
  --rose: #F43F5E;
  --cyan: #06B6D4;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--txt);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  line-height: 1.65;
}
.wrap { max-width: 1360px; margin: auto; padding: 20px 24px 80px; }
.top-bar {
  position: sticky; top: 0; z-index: 100;
  background: rgba(11, 15, 23, 0.95);
  backdrop-filter: blur(8px);
  border-bottom: 1px solid var(--line);
  padding: 10px 24px;
}
.nav-scroll {
  display: flex; gap: 8px; overflow-x: auto; padding-bottom: 4px;
}
.nav-btn {
  white-space: nowrap; font-size: 13px; font-weight: 500;
  text-decoration: none; color: var(--mut);
  background: #111827; border: 1px solid var(--line);
  padding: 6px 14px; border-radius: 999px; transition: all .2s;
}
.nav-btn:hover, .nav-btn.active {
  color: #fff; background: var(--card); border-color: var(--amber);
}
.hero {
  border: 1px solid var(--line); border-radius: 18px;
  padding: 30px; margin: 18px 0 24px;
  background: linear-gradient(180deg, #162438 0%, #0F1724 100%);
  position: relative; overflow: hidden;
}
.badge {
  display: inline-block; padding: 4px 12px; border-radius: 999px;
  font-size: 12px; font-weight: 700; text-transform: uppercase;
  background: rgba(16, 185, 129, 0.15); color: var(--teal);
  border: 1px solid rgba(16, 185, 129, 0.3); margin-bottom: 12px;
}
h1 { font-size: 32px; margin: 0 0 10px; line-height: 1.25; }
h2 { font-size: 24px; margin: 34px 0 16px; border-bottom: 1px solid var(--line); padding-bottom: 8px; color: #fff; }
h3 { font-size: 18px; margin: 18px 0 8px; color: var(--amber); }
p, li { color: #CBD5E1; font-size: 15px; }
.card {
  background: var(--card); border: 1px solid var(--line);
  border-radius: 14px; padding: 22px; margin: 16px 0;
}
.grid-2 {
  display: grid; grid-template-columns: 1fr 1fr; gap: 20px;
}
@media (max-width: 900px) { .grid-2 { grid-template-columns: 1fr; } }
.q-box {
  background: #18150A; border: 1px solid var(--amber);
  border-left: 5px solid var(--amber); border-radius: 12px;
  padding: 16px; margin: 14px 0;
}
.ans-box {
  background: #0A1713; border: 1px solid var(--teal);
  border-left: 5px solid var(--teal); border-radius: 12px;
  padding: 16px; margin: 14px 0;
}
.pitfall {
  background: #1C0F12; border: 1px solid var(--rose);
  border-left: 5px solid var(--rose); border-radius: 12px;
  padding: 14px 16px; margin: 14px 0; font-size: 14px;
}
.play-box {
  background: #101622; border: 1px solid var(--vio);
  border-radius: 14px; padding: 20px; margin: 18px 0;
}
pre {
  background: #070B11; border: 1px solid var(--line);
  border-radius: 10px; padding: 14px; overflow-x: auto;
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  font-size: 13px; line-height: 1.6; color: #E2E8F0;
}
code { font-family: inherit; color: var(--cyan); }
.svg-diagram {
  width: 100%; height: auto; background: #070B11;
  border: 1px solid var(--line); border-radius: 12px; margin: 12px 0;
}
input, select {
  background: #0B0F17; border: 1px solid var(--line);
  color: #fff; padding: 8px 12px; border-radius: 8px; font-size: 14px;
}
.btn {
  background: var(--amber); color: #0B0F17; font-weight: 700;
  padding: 8px 16px; border-radius: 8px; border: 0; cursor: pointer;
  transition: opacity .2s;
}
.btn:hover { opacity: 0.9; }
.pager {
  display: flex; justify-content: space-between; align-items: center;
  margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line);
}
.pager a {
  text-decoration: none; color: var(--txt); background: var(--panel);
  border: 1px solid var(--line); padding: 10px 18px; border-radius: 10px;
  font-size: 14px; font-weight: 600;
}
.pager a:hover { border-color: var(--amber); color: #fff; }
"""

def render_top_nav(active_file):
    navs = [
        ("index.html", "01. Overview"),
        ("rag-search.html", "02. RAG & Search"),
        ("llm-serving.html", "03. Serving & Kernels"),
        ("gpu-memory-math.html", "04. Memory Math"),
        ("agentic-ai.html", "05. Agentic AI"),
        ("fine-tuning-lora.html", "06. Fine-Tuning"),
        ("distributed-parallelism.html", "07. Distributed Scale"),
        ("k8s-gpu-infra.html", "08. K8s & Autoscaling"),
        ("cloud-devops-failures.html", "09. SRE & Incidents"),
        ("eval-security-drills.html", "10. Evals & Drills")
    ]
    html = '<header class="top-bar"><nav class="nav-scroll">'
    for f, label in navs:
        act = " active" if f == active_file else ""
        html += f'<a href="{f}" class="nav-btn{act}">{label}</a>'
    html += '</nav></header>'
    return html

def render_footer(prev_file, prev_label, next_file, next_label):
    html = '<div class="pager">'
    if prev_file:
        html += f'<a href="{prev_file}">← Prev: {prev_label}</a>'
    else:
        html += '<span></span>'
    if next_file:
        html += f'<a href="{next_file}">Next: {next_label} →</a>'
    else:
        html += '<span></span>'
    html += '</div>'
    html += """
    <footer style="margin-top:30px; text-align:center; color:var(--mut); font-size:13px;">
      Satyabhan AI Engineering & DevOps Master Course • Synthesized from LinkedIn Production Debriefs & FAANG Engineering Loops
    </footer>
    """
    return html

print("Helper templates initialized.")
