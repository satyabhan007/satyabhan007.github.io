#!/usr/bin/env python3
"""
Enhanced Interactive Course Generator for AI Engineer & DevOps Mastery
Injects:
1. Interactive Q&A Accordions & Click-to-Reveal Deep Architectural Answers
2. Live Interactive Visual Explainers (Animated SVGs, Step-Through Walkthroughs)
3. Full end-to-end depth for all 45 scenarios
"""

import os
import re

BASE_DIR = "/home/satya/Downloads/SATYA/satyabhan007.github.io/ai-devops-mastery"

ENHANCED_CSS = """
:root {
  --bg: #0A0E17;
  --panel: #111827;
  --card: #162032;
  --card-hover: #1C293D;
  --line: #223249;
  --txt: #E2E8F0;
  --mut: #94A3B8;
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
  line-height: 1.7;
}
.wrap { max-width: 1360px; margin: auto; padding: 20px 24px 90px; }
.top-bar {
  position: sticky; top: 0; z-index: 100;
  background: rgba(10, 14, 23, 0.95);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--line);
  padding: 12px 24px;
}
.nav-scroll { display: flex; gap: 8px; overflow-x: auto; padding-bottom: 4px; }
.nav-btn {
  white-space: nowrap; font-size: 13px; font-weight: 600;
  text-decoration: none; color: var(--mut);
  background: #0F172A; border: 1px solid var(--line);
  padding: 7px 14px; border-radius: 999px; transition: all .2s;
}
.nav-btn:hover, .nav-btn.active {
  color: #fff; background: var(--card); border-color: var(--amber);
}
.hero {
  border: 1px solid var(--line); border-radius: 18px;
  padding: 32px; margin: 18px 0 26px;
  background: linear-gradient(180deg, #16243A 0%, #0D1422 100%);
  position: relative;
}
.badge {
  display: inline-block; padding: 4px 12px; border-radius: 999px;
  font-size: 12px; font-weight: 700; text-transform: uppercase;
  background: rgba(16, 185, 129, 0.15); color: var(--teal);
  border: 1px solid rgba(16, 185, 129, 0.3); margin-bottom: 12px;
}
h1 { font-size: 32px; margin: 0 0 10px; line-height: 1.25; color: #fff; }
h2 { font-size: 24px; margin: 34px 0 16px; border-bottom: 1px solid var(--line); padding-bottom: 8px; color: #fff; }
h3 { font-size: 19px; margin: 18px 0 8px; color: var(--amber); }
p, li { color: #CBD5E1; font-size: 15px; }

/* Interactive Scenario Card */
.scenario-card {
  background: var(--card); border: 1px solid var(--line);
  border-radius: 14px; margin: 18px 0; overflow: hidden;
  transition: border-color .2s;
}
.scenario-card:hover { border-color: #3B82F6; }
.scenario-header {
  padding: 18px 22px; cursor: pointer; display: flex;
  justify-content: space-between; align-items: center;
  background: #131D2D; user-select: none;
}
.scenario-title { font-size: 16px; font-weight: 700; color: #fff; }
.scenario-meta { font-size: 13px; color: var(--mut); margin-top: 4px; }
.toggle-icon { font-size: 18px; color: var(--amber); transition: transform .2s; }
.scenario-body {
  padding: 22px; display: none; border-top: 1px solid var(--line);
}
.scenario-card.open .scenario-body { display: block; }
.scenario-card.open .toggle-icon { transform: rotate(180deg); }

.q-box {
  background: #18150A; border: 1px solid var(--amber);
  border-left: 5px solid var(--amber); border-radius: 10px;
  padding: 16px; margin: 12px 0;
}
.ans-box {
  background: #0A1713; border: 1px solid var(--teal);
  border-left: 5px solid var(--teal); border-radius: 10px;
  padding: 18px; margin: 14px 0;
}
.pitfall {
  background: #1C0F12; border: 1px solid var(--rose);
  border-left: 5px solid var(--rose); border-radius: 10px;
  padding: 14px 16px; margin: 14px 0; font-size: 14px;
}
.explainer-box {
  background: #0E1626; border: 1px solid var(--blue);
  border-radius: 12px; padding: 18px; margin: 16px 0;
}
.interactive-step {
  display: flex; gap: 12px; align-items: flex-start;
  padding: 10px; border-radius: 8px; margin: 6px 0;
  background: #131E30; cursor: pointer; transition: background .2s;
}
.interactive-step:hover, .interactive-step.active {
  background: #1E2D48; border-left: 3px solid var(--cyan);
}
.step-num {
  background: var(--blue); color: #fff; font-weight: bold;
  border-radius: 50%; width: 26px; height: 26px; display: flex;
  align-items: center; justify-content: center; font-size: 13px; flex-shrink: 0;
}
pre {
  background: #070B11; border: 1px solid var(--line);
  border-radius: 10px; padding: 14px; overflow-x: auto;
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  font-size: 13px; line-height: 1.6; color: #E2E8F0;
}
code { font-family: inherit; color: var(--cyan); }
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
    <script>
      function toggleCard(header) {
        header.parentElement.classList.toggle('open');
      }
    </script>
    """
    return html

print("Enhanced CSS & Components configured.")
