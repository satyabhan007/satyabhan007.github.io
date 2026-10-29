#!/usr/bin/env python3
import os
import re

BASE_DIR = "/home/satya/Downloads/SATYA/satyabhan007.github.io/ai-devops-mastery"

PAGES = [
    ("index.html", "01. Overview"),
    ("rag-search.html", "02. RAG & Search"),
    ("llm-serving.html", "03. Serving & Kernels"),
    ("gpu-memory-math.html", "04. Memory Math"),
    ("agentic-ai.html", "05. Agentic AI"),
    ("fine-tuning-lora.html", "06. Fine-Tuning"),
    ("distributed-parallelism.html", "07. Distributed Scale"),
    ("k8s-gpu-infra.html", "08. K8s & Autoscaling"),
    ("cloud-devops-failures.html", "09. SRE & Incidents"),
    ("eval-security-drills.html", "10. Evals & Drills"),
    ("reasoning-kernels.html", "11. Reasoning & Triton")
]

def generate_nav(active_filename):
    items = []
    for href, title in PAGES:
        cls = "nav-btn active" if href == active_filename else "nav-btn"
        items.append(f'<a href="{href}" class="{cls}">{title}</a>')
    return f'<header class="top-bar"><nav class="nav-scroll">{"".join(items)}</nav></header>'

# 1. Update index.html
index_path = os.path.join(BASE_DIR, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    idx_content = f.read()

# Replace description
idx_content = re.sub(
    r"This (10|12)-module masterclass translates.*?into an interactive learning syllabus\.",
    r"This 11-module masterclass translates <strong>50 real-world technical debriefs, failure war-stories, and architectural whiteboard challenges</strong> collected from senior AI candidates and leads at OpenAI, Google, NVIDIA, AWS, and Netflix into an interactive learning syllabus.",
    idx_content
)

# Remove VAULT row if present
idx_content = re.sub(r'\s*<tr data-role="ALL" data-diff="ALL"><td style="padding:8px;">VAULT</td>.*?</tr>', '', idx_content)

# Ensure QA-46 to QA-50 exist
new_rows = """        <tr data-role="AI Engineer" data-diff="Hard"><td style="padding:8px;">QA-46</td><td>Frontier Modeling</td><td>AI Engineer</td><td>Test-Time Compute Scaling, o1/R1, PRM vs ORM Tree Search</td><td>Hard</td><td><a href="reasoning-kernels.html">11. Reasoning & Triton</a></td></tr>
        <tr data-role="AI Engineer" data-diff="Hard"><td style="padding:8px;">QA-47</td><td>Post-Training Alignment</td><td>AI Engineer</td><td>DPO vs PPO vs GRPO: Eliminating the Critic Network</td><td>Hard</td><td><a href="reasoning-kernels.html">11. Reasoning & Triton</a></td></tr>
        <tr data-role="AI DevOps" data-diff="Hard"><td style="padding:8px;">QA-48</td><td>Kernel Optimization</td><td>AI DevOps</td><td>Writing Custom Fused Kernels in OpenAI Triton (SRAM Tiling)</td><td>Hard</td><td><a href="reasoning-kernels.html">11. Reasoning & Triton</a></td></tr>
        <tr data-role="AI DevOps" data-diff="Hard"><td style="padding:8px;">QA-49</td><td>Quantization Formats</td><td>AI DevOps</td><td>FP8 (E4M3 vs E5M2) vs INT4 vs AWQ Tensor Core GEMM</td><td>Hard</td><td><a href="reasoning-kernels.html">11. Reasoning & Triton</a></td></tr>
        <tr data-role="Architect" data-diff="Hard"><td style="padding:8px;">QA-50</td><td>Frontier Inference</td><td>Architect</td><td>Speculative Decoding & Multi-Token Prediction (MTP) Engine</td><td>Hard</td><td><a href="reasoning-kernels.html">11. Reasoning & Triton</a></td></tr>"""

if "QA-46" not in idx_content:
    idx_content = idx_content.replace(
        '<tr data-role="Architect" data-diff="Hard"><td style="padding:8px;">QA-45</td><td>Fault Tolerance</td><td>Architect</td><td>Zero-Downtime Migration of Long-Running Agent Workflows</td><td>Hard</td><td><a href="agentic-ai.html">05. Agentic AI</a></td></tr>',
        '<tr data-role="Architect" data-diff="Hard"><td style="padding:8px;">QA-45</td><td>Fault Tolerance</td><td>Architect</td><td>Zero-Downtime Migration of Long-Running Agent Workflows</td><td>Hard</td><td><a href="agentic-ai.html">05. Agentic AI</a></td></tr>\n' + new_rows
    )

with open(index_path, "w", encoding="utf-8") as f:
    f.write(idx_content)
print("[OK] Cleaned index.html (removed Vault, updated 11-module syllabus).")

# 2. Update navigation bar across all 11 pages
for fname, title in PAGES:
    fpath = os.path.join(BASE_DIR, fname)
    if not os.path.exists(fpath):
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    new_nav = generate_nav(fname)
    html = re.sub(r'<header class="top-bar">.*?</header>', new_nav, html, flags=re.DOTALL)
    
    # Fix pager on eval-security-drills.html
    if fname == "eval-security-drills.html":
        html = re.sub(
            r'<div class="pager">.*?</div>',
            '<div class="pager"><a href="cloud-devops-failures.html">← Prev: 09. SRE & Incidents</a><a href="reasoning-kernels.html">Next: 11. Reasoning & Triton →</a></div>',
            html
        )
    
    # Fix pager on reasoning-kernels.html
    if fname == "reasoning-kernels.html":
        html = re.sub(
            r'<div class="pager">.*?</div>',
            '<div class="pager"><a href="eval-security-drills.html">← Prev: 10. Evals & Drills</a><a href="index.html">Next: 01. Overview →</a></div>',
            html
        )
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[OK] Harmonized nav for {fname}")

print("All course modules successfully synchronized!")
