#!/usr/bin/env python3
import os
import json

BASE_DIR = "/home/satya/Downloads/SATYA/satyabhan007.github.io/ai-devops-mastery"

from generate_site import SHARED_CSS, render_top_nav, render_footer

def make_page(filename, title, badge, content, prev_f, prev_l, next_f, next_l):
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | AI & DevOps Mastery Course</title>
  <style>{SHARED_CSS}</style>
</head>
<body>
  {render_top_nav(filename)}
  <main class="wrap">
    <div class="hero">
      <span class="badge">{badge}</span>
      <h1>{title}</h1>
    </div>
    {content}
    {render_footer(prev_f, prev_l, next_f, next_l)}
  </main>
</body>
</html>"""
    filepath = os.path.join(BASE_DIR, filename)
    with open(filepath, 'w') as f:
        f.write(full_html)
    print(f"[OK] Generated {filename}")

# ==============================================================================
# PAGE 1: INDEX.HTML
# ==============================================================================
p1_content = """
<div class="card">
  <h2>🎯 Curriculum Overview & Master Matrix</h2>
  <p>This 10-module masterclass translates <strong>45 real-world technical debriefs, failure war-stories, and architectural whiteboard challenges</strong> collected from senior AI candidates and leads at OpenAI, Google, NVIDIA, AWS, and Netflix into an interactive learning syllabus.</p>
</div>

<div class="play-box">
  <h3>🔍 Interactive Scenario Matrix Filter</h3>
  <p>Filter all 45 interview scenarios by domain or role track:</p>
  <div style="display:flex; gap:10px; margin-bottom:15px; flex-wrap:wrap;">
    <select id="roleFilter" onchange="filterMatrix()">
      <option value="ALL">All Roles</option>
      <option value="AI Engineer">AI Engineer</option>
      <option value="AI DevOps">AI DevOps / Platform</option>
      <option value="MLOps">MLOps</option>
      <option value="Architect">Architect / Lead</option>
    </select>
    <select id="diffFilter" onchange="filterMatrix()">
      <option value="ALL">All Difficulties</option>
      <option value="Hard">Hard / Whiteboard</option>
      <option value="Medium-Hard">Medium-Hard</option>
    </select>
    <input type="text" id="keywordSearch" placeholder="Search scenario, tech, or failure..." onkeyup="filterMatrix()" style="flex:1; min-width:200px;">
  </div>

  <div style="overflow-x:auto;">
    <table id="matrixTable" style="width:100%; border-collapse:collapse; font-size:14px; text-align:left;">
      <thead>
        <tr style="border-bottom:2px solid var(--line); color:var(--amber);">
          <th style="padding:10px;">ID</th>
          <th style="padding:10px;">Domain</th>
          <th style="padding:10px;">Role Track</th>
          <th style="padding:10px;">Core Scenario / Interview Question</th>
          <th style="padding:10px;">Difficulty</th>
          <th style="padding:10px;">Module Page</th>
        </tr>
      </thead>
      <tbody>
        <tr data-role="AI DevOps" data-diff="Hard"><td style="padding:8px;">QA-01</td><td>Production Failure</td><td>AI DevOps</td><td>The "Tell me about a 2 AM failure" in production AI</td><td>Hard</td><td><a href="cloud-devops-failures.html">09. SRE & Incidents</a></td></tr>
        <tr data-role="AI Engineer" data-diff="Hard"><td style="padding:8px;">QA-02</td><td>System Design</td><td>AI Engineer</td><td>Whiteboard: End-to-End Production RAG System</td><td>Hard</td><td><a href="rag-search.html">02. RAG & Search</a></td></tr>
        <tr data-role="AI Engineer" data-diff="Hard"><td style="padding:8px;">QA-03</td><td>Agentic Workflows</td><td>AI Engineer</td><td>LangGraph Checkpointer Crash & Duplicate Payment Bug</td><td>Hard</td><td><a href="agentic-ai.html">05. Agentic AI</a></td></tr>
        <tr data-role="AI DevOps" data-diff="Hard"><td style="padding:8px;">QA-04</td><td>GPU Architecture</td><td>AI DevOps</td><td>GPU Utilization vs Occupancy vs Memory Bandwidth</td><td>Hard</td><td><a href="gpu-memory-math.html">04. Memory Math</a></td></tr>
        <tr data-role="AI DevOps" data-diff="Hard"><td style="padding:8px;">QA-05</td><td>Inference Serving</td><td>AI DevOps</td><td>Continuous Batching & PagedAttention in vLLM</td><td>Hard</td><td><a href="llm-serving.html">03. Serving & Kernels</a></td></tr>
        <tr data-role="AI DevOps" data-diff="Hard"><td style="padding:8px;">QA-06</td><td>Memory Sizing</td><td>AI DevOps</td><td>Llama-3-70B VRAM & GQA KV-Cache Math (64 streams)</td><td>Hard</td><td><a href="gpu-memory-math.html">04. Memory Math</a></td></tr>
        <tr data-role="AI DevOps" data-diff="Medium-Hard"><td style="padding:8px;">QA-07</td><td>Autoscaling</td><td>AI DevOps</td><td>Why HPA CPU/GPU utilization fails for LLM serving</td><td>Medium-Hard</td><td><a href="k8s-gpu-infra.html">08. K8s & Autoscaling</a></td></tr>
        <tr data-role="Architect" data-diff="Hard"><td style="padding:8px;">QA-08</td><td>Cloud Resiliency</td><td>Architect</td><td>"What happens when an entire cloud region fails?"</td><td>Hard</td><td><a href="cloud-devops-failures.html">09. SRE & Incidents</a></td></tr>
        <tr data-role="AI DevOps" data-diff="Medium-Hard"><td style="padding:8px;">QA-09</td><td>Troubleshooting</td><td>AI DevOps</td><td>Intermittent 502 Bad Gateways under AI Inference load</td><td>Medium-Hard</td><td><a href="cloud-devops-failures.html">09. SRE & Incidents</a></td></tr>
        <tr data-role="AI DevOps" data-diff="Medium-Hard"><td style="padding:8px;">QA-10</td><td>High-Traffic Incident</td><td>AI DevOps</td><td>"Every morning at 10 AM, users see 'Something went wrong'"</td><td>Medium-Hard</td><td><a href="cloud-devops-failures.html">09. SRE & Incidents</a></td></tr>
        <tr data-role="AI Engineer" data-diff="Medium-Hard"><td style="padding:8px;">QA-11</td><td>Cost & Routing</td><td>AI Engineer</td><td>Intelligent Model Routing (SLMs -> LLMs)</td><td>Medium-Hard</td><td><a href="llm-serving.html">03. Serving & Kernels</a></td></tr>
        <tr data-role="AI DevOps" data-diff="Hard"><td style="padding:8px;">QA-12</td><td>Memory Exhaustion</td><td>AI DevOps</td><td>Cluster at 92% HBM; KV cache at 60%; cannot buy GPUs</td><td>Hard</td><td><a href="gpu-memory-math.html">04. Memory Math</a></td></tr>
        <tr data-role="AI DevOps" data-diff="Hard"><td style="padding:8px;">QA-13</td><td>K8s Networking</td><td>AI DevOps</td><td>5,000 Services & kube-proxy at 100% CPU in AI cluster</td><td>Hard</td><td><a href="k8s-gpu-infra.html">08. K8s & Autoscaling</a></td></tr>
        <tr data-role="AI DevOps" data-diff="Medium-Hard"><td style="padding:8px;">QA-14</td><td>AWS / CI/CD</td><td>AI DevOps</td><td>GitHub Actions OIDC to AWS failing with AccessDenied</td><td>Medium-Hard</td><td><a href="cloud-devops-failures.html">09. SRE & Incidents</a></td></tr>
        <tr data-role="AI Engineer" data-diff="Hard"><td style="padding:8px;">QA-15</td><td>RAG Failure Triage</td><td>AI Engineer</td><td>Model returns bad answer: Dissecting 5 root causes</td><td>Hard</td><td><a href="rag-search.html">02. RAG & Search</a></td></tr>
        <tr data-role="AI Engineer" data-diff="Medium-Hard"><td style="padding:8px;">QA-16</td><td>Agent Reliability</td><td>AI Engineer</td><td>Agent Infinite Tool Loops & Idempotent Retries</td><td>Medium-Hard</td><td><a href="agentic-ai.html">05. Agentic AI</a></td></tr>
        <tr data-role="AI Engineer" data-diff="Medium"><td style="padding:8px;">QA-17</td><td>Context Tradeoffs</td><td>AI Engineer</td><td>"If models have 1M+ tokens, why not pass all docs?"</td><td>Medium</td><td><a href="rag-search.html">02. RAG & Search</a></td></tr>
        <tr data-role="AI DevOps" data-diff="Hard"><td style="padding:8px;">QA-18</td><td>Security & Escapes</td><td>AI DevOps</td><td>Indirect Prompt Injection & Code Sandboxing</td><td>Hard</td><td><a href="eval-security-drills.html">10. Evals & Drills</a></td></tr>
        <tr data-role="MLOps" data-diff="Medium-Hard"><td style="padding:8px;">QA-19</td><td>Evaluation CI/CD</td><td>MLOps</td><td>Automated Quality Gates (Ragas, Faithfulness, Judges)</td><td>Medium-Hard</td><td><a href="eval-security-drills.html">10. Evals & Drills</a></td></tr>
        <tr data-role="AI DevOps" data-diff="Hard"><td style="padding:8px;">QA-20</td><td>HPC & Interconnect</td><td>AI DevOps</td><td>InfiniBand vs RoCE & NCCL Topology for Multi-Node</td><td>Hard</td><td><a href="distributed-parallelism.html">07. Distributed Scale</a></td></tr>
        <tr data-role="AI DevOps" data-diff="Medium-Hard"><td style="padding:8px;">QA-21</td><td>Cold Starts</td><td>AI DevOps</td><td>Reducing 70B model cold start from 8m to <45s</td><td>Medium-Hard</td><td><a href="k8s-gpu-infra.html">08. K8s & Autoscaling</a></td></tr>
        <tr data-role="AI DevOps" data-diff="Medium"><td style="padding:8px;">QA-22</td><td>IaC Drift</td><td>AI DevOps</td><td>Terraform plan wants to destroy un-touched state</td><td>Medium</td><td><a href="cloud-devops-failures.html">09. SRE & Incidents</a></td></tr>
        <tr data-role="MLOps" data-diff="Hard"><td style="padding:8px;">QA-23</td><td>Vector DB Scaling</td><td>MLOps</td><td>50M Vectors: HNSW vs IVF-PQ & Preventing OOM Kills</td><td>Hard</td><td><a href="rag-search.html">02. RAG & Search</a></td></tr>
        <tr data-role="AI Engineer" data-diff="Medium"><td style="padding:8px;">QA-24</td><td>Tokenomics</td><td>AI Engineer</td><td>Byte-Pair Encoding failure on numbers and code</td><td>Medium</td><td><a href="fine-tuning-lora.html">06. Fine-Tuning</a></td></tr>
        <tr data-role="AI DevOps" data-diff="Hard"><td style="padding:8px;">QA-25</td><td>Distributed Parallelism</td><td>AI DevOps</td><td>Tensor (TP) vs Pipeline (PP) vs Data Parallelism (DP)</td><td>Hard</td><td><a href="distributed-parallelism.html">07. Distributed Scale</a></td></tr>
        <tr data-role="AI Engineer" data-diff="Medium-Hard"><td style="padding:8px;">QA-26</td><td>Agent Protocols</td><td>AI Engineer</td><td>Model Context Protocol (MCP) vs Traditional REST APIs</td><td>Medium-Hard</td><td><a href="agentic-ai.html">05. Agentic AI</a></td></tr>
        <tr data-role="AI Engineer" data-diff="Hard"><td style="padding:8px;">QA-27</td><td>Kernel Optimization</td><td>AI Engineer</td><td>FlashAttention Tiling & Online Softmax Algorithm</td><td>Hard</td><td><a href="llm-serving.html">03. Serving & Kernels</a></td></tr>
        <tr data-role="AI Engineer" data-diff="Hard"><td style="padding:8px;">QA-28</td><td>Fine-Tuning vs PEFT</td><td>AI Engineer</td><td>LoRA vs QLoRA Mathematical Formulation & S-LoRA</td><td>Hard</td><td><a href="fine-tuning-lora.html">06. Fine-Tuning</a></td></tr>
        <tr data-role="AI Engineer" data-diff="Medium-Hard"><td style="padding:8px;">QA-29</td><td>Format Failure</td><td>AI Engineer</td><td>Prompting vs Fine-Tuning Decision Tree</td><td>Medium-Hard</td><td><a href="fine-tuning-lora.html">06. Fine-Tuning</a></td></tr>
        <tr data-role="AI DevOps" data-diff="Hard"><td style="padding:8px;">QA-30</td><td>Distributed Training</td><td>AI DevOps</td><td>DeepSpeed ZeRO-1/2/3 Memory Partitioning Math</td><td>Hard</td><td><a href="distributed-parallelism.html">07. Distributed Scale</a></td></tr>
        <tr data-role="AI Engineer" data-diff="Hard"><td style="padding:8px;">QA-31</td><td>Serving Asymmetry</td><td>AI Engineer</td><td>Speculative Decoding & The Core Transformer Asymmetry</td><td>Hard</td><td><a href="llm-serving.html">03. Serving & Kernels</a></td></tr>
        <tr data-role="Architect" data-diff="Hard"><td style="padding:8px;">QA-32</td><td>Scale Architecture</td><td>Architect</td><td>Prefill-Decode Disaggregation (PD Disaggregation)</td><td>Hard</td><td><a href="llm-serving.html">03. Serving & Kernels</a></td></tr>
        <tr data-role="AI DevOps" data-diff="Medium-Hard"><td style="padding:8px;">QA-33</td><td>Distributed Serving</td><td>AI DevOps</td><td>Ray Serve + vLLM High-Throughput Cluster Architecture</td><td>Medium-Hard</td><td><a href="distributed-parallelism.html">07. Distributed Scale</a></td></tr>
        <tr data-role="MLOps" data-diff="Hard"><td style="padding:8px;">QA-34</td><td>Quantization Showdown</td><td>MLOps</td><td>AWQ vs GPTQ vs SmoothQuant vs GGUF Tradeoffs</td><td>Hard</td><td><a href="fine-tuning-lora.html">06. Fine-Tuning</a></td></tr>
        <tr data-role="AI DevOps" data-diff="Hard"><td style="padding:8px;">QA-35</td><td>Runtime Security</td><td>AI DevOps</td><td>eBPF Runtime Threat Auditing & Zero-Downtime CVE Patch</td><td>Hard</td><td><a href="eval-security-drills.html">10. Evals & Drills</a></td></tr>
        <tr data-role="AI DevOps" data-diff="Hard"><td style="padding:8px;">QA-36</td><td>Serving Architecture</td><td>AI DevOps</td><td>Triton Inference Server Multi-Model Pipelines & SLAs</td><td>Hard</td><td><a href="llm-serving.html">03. Serving & Kernels</a></td></tr>
        <tr data-role="Architect" data-diff="Hard"><td style="padding:8px;">QA-37</td><td>Advanced Search</td><td>Architect</td><td>GraphRAG vs Vector RAG: Multi-Hop Macro Queries</td><td>Hard</td><td><a href="rag-search.html">02. RAG & Search</a></td></tr>
        <tr data-role="AI DevOps" data-diff="Hard"><td style="padding:8px;">QA-38</td><td>Agent Security</td><td>AI DevOps</td><td>Indirect Prompt Injection & Dual-LLM Privilege Isolation</td><td>Hard</td><td><a href="eval-security-drills.html">10. Evals & Drills</a></td></tr>
        <tr data-role="AI DevOps" data-diff="Hard"><td style="padding:8px;">QA-39</td><td>Interconnect</td><td>AI DevOps</td><td>InfiniBand vs RoCE v2 & NCCL Step-Time Jitter Triage</td><td>Hard</td><td><a href="distributed-parallelism.html">07. Distributed Scale</a></td></tr>
        <tr data-role="MLOps" data-diff="Hard"><td style="padding:8px;">QA-40</td><td>Distributed K8s</td><td>MLOps</td><td>Gang Scheduling with Volcano & Preventing Resource Deadlocks</td><td>Hard</td><td><a href="k8s-gpu-infra.html">08. K8s & Autoscaling</a></td></tr>
        <tr data-role="MLOps" data-diff="Medium-Hard"><td style="padding:8px;">QA-41</td><td>Quality & CI/CD</td><td>MLOps</td><td>Automated LLM Eval Quality Gates (Ragas/Promptfoo)</td><td>Medium-Hard</td><td><a href="eval-security-drills.html">10. Evals & Drills</a></td></tr>
        <tr data-role="AI Engineer" data-diff="Medium-Hard"><td style="padding:8px;">QA-42</td><td>Fine-Tuning Data</td><td>AI Engineer</td><td>Synthetic Data Distillation & Multi-Tier Execution Filter</td><td>Medium-Hard</td><td><a href="fine-tuning-lora.html">06. Fine-Tuning</a></td></tr>
        <tr data-role="Architect" data-diff="Medium-Hard"><td style="padding:8px;">QA-43</td><td>Cost Arbitrage</td><td>Architect</td><td>Intelligent Model Routing & Semantic Caching Gateway</td><td>Medium-Hard</td><td><a href="llm-serving.html">03. Serving & Kernels</a></td></tr>
        <tr data-role="AI DevOps" data-diff="Hard"><td style="padding:8px;">QA-44</td><td>Performance Profiling</td><td>AI DevOps</td><td>vLLM Chunked Prefill, PagedAttention & ITL Stutter Triage</td><td>Hard</td><td><a href="llm-serving.html">03. Serving & Kernels</a></td></tr>
        <tr data-role="Architect" data-diff="Hard"><td style="padding:8px;">QA-45</td><td>Fault Tolerance</td><td>Architect</td><td>Zero-Downtime Migration of Long-Running Agent Workflows</td><td>Hard</td><td><a href="agentic-ai.html">05. Agentic AI</a></td></tr>
      </tbody>
    </table>
  </div>
</div>

<script>
function filterMatrix() {
  const role = document.getElementById('roleFilter').value;
  const diff = document.getElementById('diffFilter').value;
  const q = document.getElementById('keywordSearch').value.toLowerCase();
  const rows = document.querySelectorAll('#matrixTable tbody tr');
  
  rows.forEach(r => {
    const rRole = r.getAttribute('data-role');
    const rDiff = r.getAttribute('data-diff');
    const text = r.innerText.toLowerCase();
    
    const roleMatch = (role === 'ALL' || rRole.includes(role));
    const diffMatch = (diff === 'ALL' || rDiff === diff);
    const textMatch = text.includes(q);
    
    if (roleMatch && diffMatch && textMatch) {
      r.style.display = '';
    } else {
      r.style.display = 'none';
    }
  });
}
</script>
"""
make_page("index.html", "Course Overview & 45 Scenario Matrix", "Module 01: Master Map", p1_content, None, None, "rag-search.html", "02. RAG & Search")

# ==============================================================================
# PAGE 2: RAG-SEARCH.HTML
# ==============================================================================
p2_content = """
<div class="card">
  <h2>Production Retrieval Augmented Generation & Search Architectures</h2>
  <p>Covers <strong>QA-02, QA-15, QA-17, QA-23, and QA-37</strong>. Master dense vector databases, graph-based global queries, reciprocal rank fusion, and mathematical memory sizing for 50 million embeddings.</p>
</div>

<!-- QA-02 -->
<div class="card">
  <span class="badge">QA-02 • System Design</span>
  <h3>Whiteboard: End-to-End Production RAG System</h3>
  <div class="q-box">
    <b>Scenario:</b> "Draw and defend an end-to-end production RAG system serving 10M enterprise documents. How do you handle ambiguous user queries, prevent stale knowledge retrieval, and keep latency under 800ms?"
  </div>
  
  <svg class="svg-diagram" viewBox="0 0 900 240">
    <rect x="20" y="90" width="120" height="60" rx="8" fill="#1E293B" stroke="#3B82F6"/>
    <text x="80" y="125" fill="#E2E8F0" font-size="12" text-anchor="middle">User Query</text>
    
    <path d="M 140 120 L 190 120" stroke="#8B9BB0" stroke-width="2" marker-end="url(#ar)"/>
    
    <rect x="190" y="90" width="140" height="60" rx="8" fill="#1E293B" stroke="#10B981"/>
    <text x="260" y="115" fill="#10B981" font-size="12" font-weight="bold" text-anchor="middle">Semantic Cache</text>
    <text x="260" y="135" fill="#94A3B8" font-size="10" text-anchor="middle">Cosine >= 0.96 (15ms)</text>
    
    <path d="M 330 120 L 380 70" stroke="#8B9BB0" stroke-width="2"/>
    <path d="M 330 120 L 380 170" stroke="#8B9BB0" stroke-width="2"/>
    
    <rect x="380" y="40" width="130" height="50" rx="8" fill="#1E293B" stroke="#F59E0B"/>
    <text x="445" y="70" fill="#F59E0B" font-size="11" text-anchor="middle">Dense (HNSW/Qdrant)</text>
    
    <rect x="380" y="150" width="130" height="50" rx="8" fill="#1E293B" stroke="#F59E0B"/>
    <text x="445" y="180" fill="#F59E0B" font-size="11" text-anchor="middle">Sparse (BM25)</text>
    
    <path d="M 510 65 L 560 100" stroke="#8B9BB0" stroke-width="2"/>
    <path d="M 510 175 L 560 140" stroke="#8B9BB0" stroke-width="2"/>
    
    <rect x="560" y="90" width="140" height="60" rx="8" fill="#1E293B" stroke="#8B5CF6"/>
    <text x="630" y="115" fill="#8B5CF6" font-size="12" font-weight="bold" text-anchor="middle">RRF Fusion + Rerank</text>
    <text x="630" y="135" fill="#94A3B8" font-size="10" text-anchor="middle">Cohere / BGE-Large</text>
    
    <path d="M 700 120 L 750 120" stroke="#8B9BB0" stroke-width="2"/>
    
    <rect x="750" y="90" width="120" height="60" rx="8" fill="#1E293B" stroke="#06B6D4"/>
    <text x="810" y="115" fill="#06B6D4" font-size="12" font-weight="bold" text-anchor="middle">vLLM Inference</text>
    <text x="810" y="135" fill="#94A3B8" font-size="10" text-anchor="middle">Stream Output</text>
  </svg>

  <div class="ans-box">
    <b>Whiteboard Architecture Breakdown:</b>
    <ul>
      <li><strong>Query Transformation:</strong> Run HyDE (Hypothetical Document Embeddings) and multi-query decomposition to resolve ambiguous slang.</li>
      <li><strong>Redis Semantic Cache:</strong> Check pre-computed vector embeddings. If similarity &ge; 0.96, return answer immediately (&lt;15ms latency, $0 token cost).</li>
      <li><strong>Hybrid Dual-Search:</strong> Run dense vector similarity (capturing semantic intent) alongside BM25 sparse keyword search (capturing exact product SKUs, error codes, and IDs).</li>
      <li><strong>RRF (Reciprocal Rank Fusion, k=60):</strong> Merge both ranked lists via score <code>sum(1 / (60 + rank))</code>.</li>
      <li><strong>Cross-Encoder Reranker:</strong> Joint attention across top-100 candidates pruned to top-5 high-signal chunks.</li>
    </ul>
  </div>
</div>

<!-- QA-23: CALCULATOR -->
<div class="play-box">
  <span class="badge">QA-23 • Interactive Calculator</span>
  <h3>Vector DB Memory & Index Sizing (HNSW vs IVF-PQ)</h3>
  <p>Test vector index sizing for millions of embeddings to prevent Linux OOM-killer crashes:</p>
  
  <div class="grid-2">
    <div>
      <label>Number of Vectors (Millions):</label><br>
      <input type="number" id="vCount" value="50" min="1" max="500" oninput="calcVectors()" style="width:100%; margin:8px 0;">
      
      <label>Vector Dimensions:</label><br>
      <input type="number" id="vDims" value="1536" step="128" oninput="calcVectors()" style="width:100%; margin:8px 0;">
    </div>
    <div style="background:#070B11; padding:15px; border-radius:10px; border:1px solid var(--line);">
      <div style="color:var(--mut); font-size:13px;">Raw Vector Size (FP32):</div>
      <div id="rawSize" style="font-size:22px; font-weight:bold; color:var(--txt);">307.2 GB</div>
      
      <div style="color:var(--rose); font-size:13px; margin-top:10px;">HNSW Index Footprint (2x Overhead):</div>
      <div id="hnswSize" style="font-size:22px; font-weight:bold; color:var(--rose);">614.4 GB (OOM Danger!)</div>
      
      <div style="color:var(--teal); font-size:13px; margin-top:10px;">IVF-PQ Compressed Footprint:</div>
      <div id="ivfSize" style="font-size:22px; font-weight:bold; color:var(--teal);">18.0 GB (Production Safe)</div>
    </div>
  </div>
</div>

<script>
function calcVectors() {
  const countM = parseFloat(document.getElementById('vCount').value) || 0;
  const dims = parseFloat(document.getElementById('vDims').value) || 0;
  
  const rawBytes = countM * 1e6 * dims * 4;
  const rawGB = (rawBytes / (1024**3)).toFixed(1);
  const hnswGB = (rawGB * 2.0).toFixed(1);
  const ivfGB = ((countM * 1e6 * 64 + countM * 1e6 * 8) / (1024**3) + 2).toFixed(1);
  
  document.getElementById('rawSize').innerText = rawGB + " GB";
  document.getElementById('hnswSize').innerText = hnswGB + " GB (OOM Danger!)";
  document.getElementById('ivfSize').innerText = ivfGB + " GB (Production Safe)";
}
</script>

<!-- QA-37 -->
<div class="card">
  <span class="badge">QA-37 • Advanced Architecture</span>
  <h3>GraphRAG vs Classic Vector RAG: Resolving Global Multi-Hop Queries</h3>
  <div class="q-box">
    <b>Interview Question:</b> "Why does vector search fail when asked: 'What are the top 3 themes across 50,000 customer feedback tickets?' How does GraphRAG solve this?"
  </div>
  <div class="ans-box">
    <b>The Core Asymmetry:</b> Vector distance captures <i>local semantic affinity</i> (finding paragraphs similar to a phrasing). It cannot synthesize global summaries across documents that share no common phrasing.<br><br>
    <b>GraphRAG Resolution:</b>
    <ol>
      <li><strong>Entity & Relation Ingestion:</strong> LLM parses documents into <code>(Subject, Relation, Object)</code> triples.</li>
      <li><strong>Leiden Community Detection:</strong> Graph is partitioned into hierarchical modular communities (C0, C1, C2).</li>
      <li><strong>Community Summaries:</strong> LLM pre-summarizes each cluster at ingest time.</li>
      <li><strong>Query Time:</strong> Global questions map to high-level community report vectors using map-reduce synthesis.</li>
    </ol>
  </div>
</div>

<!-- QA-15 -->
<div class="card">
  <span class="badge">QA-15 • Incident War Room</span>
  <h3>The 5-Point RAG Failure Triage Matrix</h3>
  <div class="pitfall">
    <b>Failure:</b> User queries: "What is our company's refund policy for damaged shipments?", but model hallucinates an incorrect standard 14-day policy.
  </div>
  <table style="width:100%; border-collapse:collapse; margin-top:10px; font-size:14px;">
    <tr style="border-bottom:1px solid var(--line);"><th style="padding:8px;">Failure Point</th><th>Diagnostic Check</th><th>Engineering Resolution</th></tr>
    <tr style="border-bottom:1px solid var(--line);"><td style="padding:8px; color:var(--rose);">1. Ingestion Missing</td><td>Does source document exist in vector DB?</td><td>Verify pipeline checksums & dead-letter queues.</td></tr>
    <tr style="border-bottom:1px solid var(--line);"><td style="padding:8px; color:var(--amber);">2. Chunk Splitting</td><td>Was answer fractured across chunk boundary?</td><td>Implement parent-child hierarchical chunking or semantic chunking.</td></tr>
    <tr style="border-bottom:1px solid var(--line);"><td style="padding:8px; color:var(--blue);">3. Embedding Mismatch</td><td>Cosine similarity score < 0.70?</td><td>Fine-tune embedding model with domain contrastive pairs.</td></tr>
    <tr style="border-bottom:1px solid var(--line);"><td style="padding:8px; color:var(--vio);">4. Lost-in-the-Middle</td><td>Is chunk placed in the middle of 20 docs?</td><td>Rerank chunks and place high-signal facts at beginning and end.</td></tr>
    <tr><td style="padding:8px; color:var(--teal);">5. Prompt Hallucination</td><td>Chunk is present, but model ignores it?</td><td>Lower temperature to 0.0; inject strict system prompt constraints.</td></tr>
  </table>
</div>
"""
make_page("rag-search.html", "Production RAG, Vector DBs & GraphRAG", "Module 02: Retrieval & Search", p2_content, "index.html", "01. Overview", "llm-serving.html", "03. Serving & Kernels")

# ==============================================================================
# PAGE 3: LLM-SERVING.HTML
# ==============================================================================
p3_content = """
<div class="card">
  <h2>Inference Serving: vLLM, PagedAttention, Kernels & Triton</h2>
  <p>Covers <strong>QA-05, QA-27, QA-31, QA-32, QA-36, and QA-44</strong>. Deep-dive into memory-efficient GPU serving, continuous batching, FlashAttention tiling, speculative decoding, and prefill-decode disaggregation.</p>
</div>

<!-- QA-05 & QA-27 -->
<div class="grid-2">
  <div class="card">
    <span class="badge">QA-05 • vLLM Core</span>
    <h3>Continuous Batching vs Static Batching</h3>
    <div class="q-box">
      <b>Question:</b> Why does static batching waste > 70% of GPU compute, and how does vLLM schedule at the iteration level?
    </div>
    <div class="ans-box">
      <ul>
        <li><strong>Static Batching:</strong> The entire batch waits for the slowest 2000-token sequence. Short 50-token queries output padding tokens, wasting compute.</li>
        <li><strong>Continuous Batching:</strong> As soon as a request generates an <code>&lt;EOS&gt;</code> token, it is evicted immediately. A new queued sequence joins on the very next token iteration.</li>
        <li><strong>PagedAttention:</strong> Physical memory is partitioned into 16-token blocks. Dynamic OS-style page tables eliminate external fragmentation.</li>
      </ul>
    </div>
  </div>

  <div class="card">
    <span class="badge">QA-27 • Google Round</span>
    <h3>FlashAttention & Online Softmax</h3>
    <div class="q-box">
      <b>Question:</b> Why does standard attention scale O(N&sup2;) in memory, and how does FlashAttention run in O(N)?
    </div>
    <div class="ans-box">
      <ul>
        <li><strong>Standard Attention:</strong> Materializes the intermediate N &times; N attention matrix <code>S = Q * K^T</code> directly in high-latency HBM (2 TB/s).</li>
        <li><strong>FlashAttention Tiling:</strong> Blocks of Q, K, and V are loaded into fast on-chip SRAM (20 TB/s).</li>
        <li><strong>Online Softmax Trick:</strong> Keeps a running maximum <code>m</code> and running normalization sum <code>l</code>, allowing exact softmax updates across tiles without writing N &times; N matrices to DRAM.</li>
      </ul>
    </div>
  </div>
</div>

<!-- QA-31: SPECULATIVE DECODING PLAYGROUND -->
<div class="play-box">
  <span class="badge">QA-31 • OpenAI Loop Simulation</span>
  <h3>Speculative Decoding Simulator: Breaking the Generation Bottleneck</h3>
  <p>Simulate how a small draft model (Llama-3-1B) speculates K tokens, which are verified in parallel by a target model (Llama-3-70B) in a single forward pass:</p>

  <div class="grid-2">
    <div>
      <label>Speculative Lookahead Tokens (K):</label><br>
      <input type="range" id="kTokens" min="1" max="8" value="4" oninput="simSpec()" style="width:100%;"><br>
      <span id="kVal" style="color:var(--amber); font-weight:bold;">K = 4 tokens</span><br><br>
      
      <label>Draft Model Acceptance Rate (%):</label><br>
      <input type="range" id="accRate" min="40" max="95" value="75" oninput="simSpec()" style="width:100%;"><br>
      <span id="accVal" style="color:var(--teal); font-weight:bold;">Alpha = 75%</span>
    </div>
    <div style="background:#070B11; padding:16px; border-radius:10px; border:1px solid var(--line);">
      <div style="color:var(--mut); font-size:13px;">Tokens Generated Per Verification Step:</div>
      <div id="effTokens" style="font-size:24px; font-weight:bold; color:var(--cyan);">3.25 tokens</div>
      
      <div style="color:var(--amber); font-size:13px; margin-top:10px;">Effective Speedup Factor:</div>
      <div id="speedupFactor" style="font-size:24px; font-weight:bold; color:var(--amber);">2.41x Faster</div>
      <div style="font-size:12px; color:var(--mut); margin-top:6px;">Target model executes only 1 compute-bound prefill pass instead of K sequential memory-bound decode passes.</div>
    </div>
  </div>
</div>

<script>
function simSpec() {
  const K = parseInt(document.getElementById('kTokens').value);
  const alpha = parseInt(document.getElementById('accRate').value) / 100.0;
  document.getElementById('kVal').innerText = "K = " + K + " tokens";
  document.getElementById('accVal').innerText = "Alpha = " + (alpha * 100).toFixed(0) + "%";
  
  // Expected accepted tokens = (1 - alpha^(K+1)) / (1 - alpha)
  let accepted = 0;
  for (let i = 0; i < K; i++) {
    accepted += Math.pow(alpha, i);
  }
  const speedup = (accepted / (1 + (K * 0.12))).toFixed(2);
  
  document.getElementById('effTokens').innerText = accepted.toFixed(2) + " tokens / step";
  document.getElementById('speedupFactor').innerText = speedup + "x Speedup";
}
</script>

<!-- QA-32 & QA-36 -->
<div class="card">
  <span class="badge">QA-32 • Enterprise Scale</span>
  <h3>Prefill-Decode Disaggregation (PD Disaggregation)</h3>
  <div class="ans-box">
    <b>Why colocation kills throughput:</b> Prefill is compute-bound ($O(N^2)$ GEMM), while Decode is memory-bandwidth bound ($O(1)$ GEMV). When an unexpected 4k prompt arrives, it preempts active streams, causing massive Inter-Token Latency (ITL) stutter.<br><br>
    <b>The Architecture:</b>
    <ul>
      <li><strong>Prefill Worker Pool:</strong> High-compute GPU nodes (e.g. H100 SXM5) run prompt processing at peak FLOPS.</li>
      <li><strong>High-Speed KV Transfer:</strong> Transfer computed KV cache over InfiniBand/RoCE via RDMA into the decode cluster.</li>
      <li><strong>Decode Worker Pool:</strong> Memory-optimized nodes focus purely on continuous iteration token streaming with zero latency jitter.</li>
    </ul>
  </div>
</div>

<div class="card">
  <span class="badge">QA-36 • Triton Inference Server</span>
  <h3>Triton BLS & Multi-Model Serving Under SLA</h3>
  <p>How to chain Embedding &rarr; Reranker &rarr; LLM on NVIDIA Triton Inference Server without serializing tensors to CPU memory:</p>
  <pre><code># Ensemble Model Configuration (CUDA IPC Direct Handoff)
dynamic_batching {
  max_queue_delay_microseconds: 2000
  preferred_batch_size: [ 8, 16, 32 ]
}
instance_group [
  {
    count: 2
    kind: KIND_GPU
    gpus: [ 0 ]
  }
]</code></pre>
</div>
"""
make_page("llm-serving.html", "LLM Serving: vLLM, PagedAttention & Kernels", "Module 03: Serving Engines", p3_content, "rag-search.html", "02. RAG & Search", "gpu-memory-math.html", "04. Memory Math")

# ==============================================================================
# PAGE 4: GPU-MEMORY-MATH.HTML
# ==============================================================================
p4_content = """
<div class="card">
  <h2>GPU Architecture, Hardware Sizing & Memory Mathematics</h2>
  <p>Covers <strong>QA-04, QA-06, and QA-12</strong>. Master the exact memory formulas expected on technical whiteboard rounds for Llama-3-70B, GQA KV-cache sizing, and the Roofline Model.</p>
</div>

<!-- QA-06 CALCULATOR -->
<div class="play-box">
  <span class="badge">QA-06 • Whiteboard Math Simulator</span>
  <h3>Interactive Llama-3-70B VRAM & GQA KV-Cache Sizing Calculator</h3>
  <p>Adjust concurrent active streams and context length to calculate exact GPU counts and tensor parallelism requirements:</p>

  <div class="grid-2">
    <div>
      <label>Concurrent Active Streams (Batch Size):</label><br>
      <input type="number" id="streamCount" value="64" min="1" max="512" oninput="calcVRAM()" style="width:100%; margin:8px 0;"><br>
      
      <label>Context Window Length (Tokens):</label><br>
      <input type="number" id="ctxLen" value="4096" step="512" oninput="calcVRAM()" style="width:100%; margin:8px 0;"><br>
      
      <label>Precision:</label><br>
      <select id="prec" onchange="calcVRAM()" style="width:100%; margin:8px 0;">
        <option value="2">FP16 / BF16 (2 bytes)</option>
        <option value="1">FP8 Quantized KV (1 byte)</option>
      </select>
    </div>
    
    <div style="background:#070B11; padding:18px; border-radius:10px; border:1px solid var(--line);">
      <div style="color:var(--mut); font-size:13px;">Static Model Weights (70B params):</div>
      <div style="font-size:20px; font-weight:bold; color:var(--txt);">140.0 GB</div>
      
      <div style="color:var(--amber); font-size:13px; margin-top:8px;">KV Cache Footprint:</div>
      <div id="kvFootprint" style="font-size:20px; font-weight:bold; color:var(--amber);">83.9 GB</div>
      
      <div style="color:var(--cyan); font-size:13px; margin-top:8px;">Total VRAM Required (Weights + KV + Act):</div>
      <div id="totalVRAM" style="font-size:24px; font-weight:bold; color:var(--cyan);">235.9 GB</div>
      
      <div style="color:var(--teal); font-size:13px; margin-top:8px;">Minimum 80GB GPUs Required:</div>
      <div id="gpusRequired" style="font-size:24px; font-weight:bold; color:var(--teal);">4x 80GB GPUs (TP=4)</div>
    </div>
  </div>
</div>

<script>
function calcVRAM() {
  const streams = parseInt(document.getElementById('streamCount').value) || 0;
  const ctx = parseInt(document.getElementById('ctxLen').value) || 0;
  const bytesPerVal = parseFloat(document.getElementById('prec').value) || 2;
  
  // Llama-3-70B: L=80, H_kv=8, d_h=128
  // KV bytes per token = 2 * L * H_kv * d_h * bytes
  const bytesPerToken = 2 * 80 * 8 * 128 * bytesPerVal;
  const totalKVBytes = streams * ctx * bytesPerToken;
  const kvGB = totalKVBytes / (1024**3);
  
  const weightsGB = 140.0;
  const actBufferGB = 12.0;
  const totalGB = weightsGB + kvGB + actBufferGB;
  
  const gpusNeeded = Math.ceil(totalGB / 80.0);
  // Nearest power of 2 for tensor parallelism
  let tp = 1;
  while (tp < gpusNeeded) tp *= 2;
  
  document.getElementById('kvFootprint').innerText = kvGB.toFixed(1) + " GB";
  document.getElementById('totalVRAM').innerText = totalGB.toFixed(1) + " GB";
  document.getElementById('gpusRequired').innerText = tp + "x 80GB GPUs (TP=" + tp + ")";
}
</script>

<!-- QA-04 -->
<div class="card">
  <span class="badge">QA-04 • Hardware Deep Dive</span>
  <h3>Why 100% GPU Utilization is Deceptive (The Roofline Model)</h3>
  <div class="q-box">
    <b>Scenario:</b> "Your nvidia-smi shows 100% GPU utilization while serving an LLM, but generation throughput is slow. Your lead asks if you need new GPUs. How do you respond?"
  </div>
  <div class="ans-box">
    <b>The Forensic Diagnostic:</b>
    <p><code>nvidia-smi</code>'s utilization counter reports 100% if <i>even a single CUDA thread</i> was executing over the sampling period. It tells you nothing about Streaming Multiprocessor (SM) occupancy or memory bandwidth saturation.</p>
    <ul>
      <li><strong>Prefill Phase:</strong> Compute-bound matrix multiplications (GEMM). High tensor core utilization.</li>
      <li><strong>Decode Phase:</strong> Memory bandwidth-bound matrix-vector products (GEMV). Each generated token must read every weight and KV cache token from DRAM to SRAM. The SMs spend 85% of cycles waiting on HBM latency.</li>
      <li><strong>Action Plan:</strong> Profile with <code>nsys</code> (Nsight Systems). If memory bandwidth is pegged at 95% while tensor cores sit at 15%, do not buy new GPUs—implement <strong>PagedAttention, FP8 quantization, or continuous batching</strong>.</li>
    </ul>
  </div>
</div>

<!-- QA-12 -->
<div class="card">
  <span class="badge">QA-12 • Capacity Crisis</span>
  <h3>Cluster at 92% HBM; KV Cache at 60%; Cannot Buy GPUs</h3>
  <div class="pitfall">
    <b>The Crisis:</b> Traffic is rising, HBM is near capacity, and hardware procurement has an 8-month lead time. How do you double throughput immediately?
  </div>
  <div class="ans-box">
    <b>Three Production Levers:</b>
    <ol>
      <li><strong>Automatic Prefix Caching (APC):</strong> Share KV blocks across identical system prompts and few-shot examples. Frees 30% to 50% of KV cache memory instantly.</li>
      <li><strong>FP8 KV Cache Quantization:</strong> Reduce KV cache footprint from 16-bit to 8-bit (<code>--kv-cache-dtype fp8</code>), doubling max concurrency with &lt;0.5% perplexity loss.</li>
      <li><strong>Chunked Prefill:</strong> Slice large input prompts into 512-token chunks to prevent memory allocation spikes from triggering OOM panics.</li>
    </ol>
  </div>
</div>
"""
make_page("gpu-memory-math.html", "GPU Architecture & VRAM Memory Math", "Module 04: Hardware & Math", p4_content, "llm-serving.html", "03. Serving & Kernels", "agentic-ai.html", "05. Agentic AI")

# ==============================================================================
# PAGE 5: AGENTIC-AI.HTML
# ==============================================================================
p5_content = """
<div class="card">
  <h2>Autonomous Agents, LangGraph Checkpointers & MCP Protocols</h2>
  <p>Covers <strong>QA-03, QA-16, QA-26, and QA-45</strong>. Master state persistence in cyclic agent graphs, preventing duplicate payments, Model Context Protocol vs REST APIs, and zero-downtime agent migration.</p>
</div>

<!-- QA-03 -->
<div class="card">
  <span class="badge">QA-03 • LangGraph Incident</span>
  <h3>LangGraph Checkpointer Crashes & The Duplicate Charge Bug</h3>
  <div class="q-box">
    <b>Scenario:</b> "An autonomous customer agent calls Stripe to charge $150. The network times out before receiving the 200 OK. When LangGraph resumes from its SQLite/Postgres checkpointer, the customer is billed twice. What happened and how do you fix it?"
  </div>
  
  <div class="ans-box">
    <b>The Core Checkpointer Mechanism:</b>
    <p>LangGraph checkpointers commit state <i>at node boundaries</i>. If a process dies or crashes mid-node, the checkpointer rolls back to the beginning of that node and replays line 1. If the node called an external API, that API call executes a second time!</p>
    <div class="pitfall">
      <b>Buggy Code:</b>
      <pre><code>def billing_node(state):
    # DANGER: Generates new key on replay!
    tx_id = uuid.uuid4()
    stripe.Charge.create(amount=state["amt"], idempotency_key=str(tx_id))
    return {"status": "paid"}</code></pre>
    </div>
    <div class="ans-box">
      <b>Resilient Solution:</b> Generate idempotency keys in a prior state node and store them in the graph state dictionary:
      <pre><code>def billing_node(state):
    # SAFE: Replay uses exact same idempotency token!
    key = state["idempotency_key"]
    stripe.Charge.create(amount=state["amt"], idempotency_key=key)
    return {"status": "paid"}</code></pre>
    </div>
  </div>
</div>

<!-- QA-26 -->
<div class="card">
  <span class="badge">QA-26 • Protocol Architecture</span>
  <h3>Model Context Protocol (MCP) vs Traditional REST APIs</h3>
  <div class="grid-2">
    <div class="card">
      <h4 style="color:var(--rose);">Traditional REST APIs</h4>
      <ul>
        <li>Fixed endpoints: Hardcoded OpenAPI/Swagger schemas in system prompts.</li>
        <li>Token Bloat: 50 REST tools consume 15,000 prompt tokens on every turn.</li>
        <li>Static Auth: Shared API tokens passed through frontend prompts.</li>
      </ul>
    </div>
    <div class="card">
      <h4 style="color:var(--teal);">Model Context Protocol (MCP)</h4>
      <ul>
        <li>Dynamic Discovery: Client queries tools, resources, and prompts dynamically via JSON-RPC.</li>
        <li>Zero Token Waste: Tool schemas loaded only when relevant context demands it.</li>
        <li>Transport Isolation: Runs over local <code>stdio</code> subprocesses or remote SSE (Server-Sent Events) with granular security boundaries.</li>
      </ul>
    </div>
  </div>
</div>

<!-- QA-16 & QA-45 -->
<div class="card">
  <span class="badge">QA-16 • Failure Mitigation</span>
  <h3>Agent Infinite Tool Loops & Fingerprinted Retries</h3>
  <div class="q-box">
    <b>Scenario:</b> "An autonomous agent encounters a transient database warning and calls the same query tool 200 times in an infinite loop, burning $80 of API credits in 4 minutes. How do you protect your systems?"
  </div>
  <div class="ans-box">
    <b>Three-Tier Protection Strategy:</b>
    <ol>
      <li><strong>Tool Call Fingerprinting:</strong> Hash tool name and arguments: <code>hash = sha256(tool_name + json_dumps(args))</code>. If identical hash appears &gt; 2 times, interrupt execution and inject a synthetic warning message.</li>
      <li><strong>Hard Max-Iteration Guards:</strong> Enforce strict <code>max_iterations = 6</code> in state graph definitions.</li>
      <li><strong>Human-in-the-Loop (HITL) Interruption:</strong> Use LangGraph's <code>interrupt()</code> to pause state and notify Slack/email when confidence drops below threshold.</li>
    </ol>
  </div>
</div>
"""
make_page("agentic-ai.html", "Agentic AI, LangGraph & MCP Protocols", "Module 05: Autonomous Systems", p5_content, "gpu-memory-math.html", "04. Memory Math", "fine-tuning-lora.html", "06. Fine-Tuning")

# ==============================================================================
# PAGE 6: FINE-TUNING-LORA.HTML
# ==============================================================================
p6_content = """
<div class="card">
  <h2>Fine-Tuning: LoRA, QLoRA, Quantization & Tokenomics</h2>
  <p>Covers <strong>QA-24, QA-28, QA-29, QA-34, and QA-42</strong>. Master parameter-efficient fine-tuning mathematics, NormalFloat4 double quantization, and formatting decision trees.</p>
</div>

<!-- QA-28 -->
<div class="card">
  <span class="badge">QA-28 • Mathematical Formulation</span>
  <h3>LoRA & QLoRA: Low-Rank Adaptation Mechanics</h3>
  <div class="ans-box">
    <b>The Core Mathematical Principle:</b>
    <p>Pre-trained weight matrix <code>W_0 &isin; R^{d &times; k}</code> is frozen. The update &Delta;W is factorized into two low-rank matrices <code>B &isin; R^{d &times; r}</code> and <code>A &isin; R^{r &times; k}</code> where rank <code>r &ll; min(d, k)</code>:</p>
    <pre><code>h = W_0 * x + (alpha / r) * (B * A) * x</code></pre>
    <ul>
      <li><strong>QLoRA Quantization:</strong> Base weights are compressed into <strong>NormalFloat4 (NF4)</strong>, an information-theoretically optimal quantile format for normally distributed weights.</li>
      <li><strong>Double Quantization:</strong> Quantizes the quantization constants themselves, saving 0.37 bits per parameter.</li>
      <li><strong>Paged Optimizers:</strong> Uses CUDA unified memory to page AdamW states to CPU RAM during activation memory spikes.</li>
    </ul>
  </div>
</div>

<!-- QA-29 -->
<div class="card">
  <span class="badge">QA-29 • Decision Tree</span>
  <h3>Prompting vs Fine-Tuning Decision Tree</h3>
  <div class="q-box">
    <b>Scenario:</b> "Our model outputs malformed JSON in 3% of responses. The team wants to fine-tune an 8B model to teach it valid JSON. Should we approve this project?"
  </div>
  <div class="ans-box">
    <b>The Rule of Thumb:</b>
    <ul>
      <li><strong>Fine-tuning is for Style, Syntax & Tone.</strong></li>
      <li><strong>RAG is for Knowledge, Facts & Verification.</strong></li>
      <li><strong>Constrained Decoding is for Schema & Structure.</strong></li>
    </ul>
    <div class="pitfall">
      <b>The Red Flag:</b> Never fine-tune a model purely to fix JSON formatting! Use <strong>Constrained Decoding (Grammar-guided sampling with Outlines / vLLM guided_json)</strong>. It masks invalid tokens from the logit vocabulary at runtime, guaranteeing 100% valid JSON with zero training cost.
    </div>
  </div>
</div>

<!-- QA-34 -->
<div class="card">
  <span class="badge">QA-34 • Quantization Showdown</span>
  <h3>AWQ vs GPTQ vs SmoothQuant vs GGUF</h3>
  <table style="width:100%; border-collapse:collapse; margin-top:10px; font-size:14px;">
    <tr style="border-bottom:1px solid var(--line);"><th style="padding:8px;">Format</th><th>Methodology</th><th>Primary Use Case</th><th>Pros / Cons</th></tr>
    <tr style="border-bottom:1px solid var(--line);"><td style="padding:8px; color:var(--amber);">AWQ (Activation-aware)</td><td>Protects top 1% salient weight channels based on activation magnitudes.</td><td>vLLM / Enterprise Serving</td><td>Highest accuracy retention; fast GEMM kernels.</td></tr>
    <tr style="border-bottom:1px solid var(--line);"><td style="padding:8px; color:var(--blue);">GPTQ</td><td>One-shot second-order Taylor error minimization (Hessian matrix).</td><td>Batch-1 Local Inference</td><td>Extremely fast offline conversion; slightly lower throughput in high batching.</td></tr>
    <tr style="border-bottom:1px solid var(--line);"><td style="padding:8px; color:var(--teal);">GGUF</td><td>Integer quantization (Q4_K_M, Q8) for llama.cpp.</td><td>CPU & Mac M-Series</td><td>Runs on consumer devices without dedicated GPU VRAM.</td></tr>
  </table>
</div>
"""
make_page("fine-tuning-lora.html", "Fine-Tuning: LoRA, QLoRA & Distillation", "Module 06: Alignment & PEFT", p6_content, "agentic-ai.html", "05. Agentic AI", "distributed-parallelism.html", "07. Distributed Scale")

# ==============================================================================
# PAGE 7: DISTRIBUTED-PARALLELISM.HTML
# ==============================================================================
p7_content = """
<div class="card">
  <h2>Distributed Training, 3D Parallelism & DeepSpeed ZeRO</h2>
  <p>Covers <strong>QA-20, QA-25, QA-30, QA-33, and QA-39</strong>. Prove the static memory math of ZeRO-1/2/3, map 3D Parallelism across NVLink and InfiniBand rails, and scale Ray Serve clusters.</p>
</div>

<!-- QA-30 -->
<div class="card">
  <span class="badge">QA-30 • Whiteboard Proof</span>
  <h3>DeepSpeed ZeRO-1/2/3 Static Memory Partitioning Proof</h3>
  <div class="ans-box">
    <b>Standard Mixed Precision Memory Math (For Model with P Parameters):</b>
    <ul>
      <li><strong>Model Weights (16-bit):</strong> 2P bytes</li>
      <li><strong>Gradients (16-bit):</strong> 2P bytes</li>
      <li><strong>AdamW Optimizer States (32-bit):</strong> Master weights (4P) + Momentum (4P) + Variance (4P) = 12P bytes</li>
      <li><strong>Total Static Memory:</strong> 2P + 2P + 12P = <strong>16P bytes</strong></li>
    </ul>
    <p><i>For a 70B parameter model: 16 &times; 70 = <strong>1,120 GB of memory</strong> before loading a single activation tensor!</i></p>
    
    <table style="width:100%; border-collapse:collapse; margin-top:10px; font-size:14px;">
      <tr style="border-bottom:1px solid var(--line);"><th style="padding:8px;">ZeRO Stage</th><th>What is Partitioned?</th><th>Memory Per GPU (N GPUs)</th><th>Communication Overhead</th></tr>
      <tr style="border-bottom:1px solid var(--line);"><td style="padding:8px; color:var(--amber);">ZeRO-Stage 1</td><td>Optimizer States only</td><td>2P + 2P + 12P/N</td><td>Zero extra communication overhead</td></tr>
      <tr style="border-bottom:1px solid var(--line);"><td style="padding:8px; color:var(--blue);">ZeRO-Stage 2</td><td>Optimizer States + Gradients</td><td>2P + 14P/N</td><td>Zero extra communication overhead</td></tr>
      <tr><td style="padding:8px; color:var(--teal);">ZeRO-Stage 3</td><td>Weights + Gradients + Optimizer States</td><td>16P / N</td><td>50% increase in inter-node communication</td></tr>
    </table>
  </div>
</div>

<!-- QA-25 -->
<div class="card">
  <span class="badge">QA-25 • Multi-Node Topology</span>
  <h3>3D Parallelism Grid Layout (256x H100 GPUs)</h3>
  <div class="ans-box">
    <table style="width:100%; border-collapse:collapse; font-size:14px;">
      <tr style="border-bottom:1px solid var(--line);"><th style="padding:8px;">Parallel Strategy</th><th>Physical Placement</th><th>Interconnect Requirement</th></tr>
      <tr style="border-bottom:1px solid var(--line);"><td style="padding:8px; color:var(--rose);">Tensor Parallelism (TP=8)</td><td>Within single 8-GPU node ONLY</td><td>900 GB/s NVLink / NVSwitch (Never put over Ethernet!)</td></tr>
      <tr style="border-bottom:1px solid var(--line);"><td style="padding:8px; color:var(--amber);">Pipeline Parallelism (PP=8)</td><td>Across distinct physical nodes</td><td>InfiniBand / RoCE (Point-to-point peer messaging)</td></tr>
      <tr><td style="padding:8px; color:var(--teal);">Data Parallelism (DP=4)</td><td>Across replicated 3D sub-grids</td><td>All-Reduce gradient synchronization</td></tr>
    </table>
  </div>
</div>
"""
make_page("distributed-parallelism.html", "Distributed AI: ZeRO, 3D Parallelism & Ray", "Module 07: Scale & Multi-Node", p7_content, "fine-tuning-lora.html", "06. Fine-Tuning", "k8s-gpu-infra.html", "08. K8s & Autoscaling")

# ==============================================================================
# PAGE 8: K8S-GPU-INFRA.HTML
# ==============================================================================
p8_content = """
<div class="card">
  <h2>Kubernetes GPU Infrastructure, Volcano & Fast Cold Starts</h2>
  <p>Covers <strong>QA-07, QA-13, QA-21, and QA-40</strong>. Master queue-depth autoscaling with KEDA, resolving 5,000 service kube-proxy CPU locks, and dropping 70B cold starts from 8m to under 45s.</p>
</div>

<!-- QA-07 -->
<div class="card">
  <span class="badge">QA-07 • KEDA Autoscaling</span>
  <h3>Why Standard HPA Fails for LLMs & How KEDA Fixes It</h3>
  <div class="pitfall">
    <b>The Trap:</b> Setting HPA to scale on 80% GPU memory causes instant scale-out to max replicas because vLLM pre-allocates 90% of VRAM for PagedAttention at boot time.
  </div>
  <div class="ans-box">
    <b>The Fix:</b> Configure KEDA to scale on <code>vllm:num_requests_waiting</code>:
    <pre><code>apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: vllm-queue-autoscaler
spec:
  scaleTargetRef:
    name: vllm-llama3-deployment
  minReplicaCount: 2
  maxReplicaCount: 16
  triggers:
  - type: prometheus
    metadata:
      serverAddress: http://prometheus.monitoring:9090
      metricName: vllm_num_requests_waiting
      query: sum(vllm:num_requests_waiting{model="llama3-70b"})
      threshold: '4'</code></pre>
  </div>
</div>

<!-- QA-21 -->
<div class="card">
  <span class="badge">QA-21 • Storage & Acceleration</span>
  <h3>Dropping 70B Cold Start from 8m to &lt; 45 Seconds</h3>
  <div class="ans-box">
    <b>Three-Step Optimization Pipeline:</b>
    <ol>
      <li><strong>Decouple Weights from Docker Images:</strong> Keep container images under 1.5GB. Mount weights from external object storage.</li>
      <li><strong>Distributed POSIX Cache (JuiceFS / Fluid):</strong> Pre-cache weights on local NVMe SSDs across the cluster.</li>
      <li><strong>GPUDirect Storage (GDS):</strong> Load safetensors files directly from NVMe into GPU HBM, skipping host CPU bounce-buffers. Throughput jumps from 800 MB/s to 12 GB/s!</li>
    </ol>
  </div>
</div>

<!-- QA-40 -->
<div class="card">
  <span class="badge">QA-40 • Scheduler Architecture</span>
  <h3>Volcano Gang Scheduling: Preventing Deadlocks in AI Clusters</h3>
  <div class="q-box">
    <b>The Deadlock:</b> 5 distributed Ray jobs each grab 4 out of their required 8 GPUs. All 40 GPUs are locked, but zero jobs can start.
  </div>
  <div class="ans-box">
    <b>Volcano All-or-Nothing Semantics:</b> Enforce <code>PodGroup</code> with <code>minMember: 8</code>. If only 6 GPUs are available, Volcano holds the entire job in queue, allowing smaller jobs to proceed instead of deadlocking the cluster.
  </div>
</div>
"""
make_page("k8s-gpu-infra.html", "Kubernetes GPU Infrastructure & Autoscaling", "Module 08: Orchestration", p8_content, "distributed-parallelism.html", "07. Distributed Scale", "cloud-devops-failures.html", "09. SRE & Incidents")

# ==============================================================================
# PAGE 9: CLOUD-DEVOPS-FAILURES.HTML
# ==============================================================================
p9_content = """
<div class="card">
  <h2>Cloud SRE, Networking & Production Incident War Stories</h2>
  <p>Covers <strong>QA-01, QA-08, QA-09, QA-10, QA-14, and QA-22</strong>. Master the STAR interview framework for production post-mortems, TCP keepalive 502 race conditions, and thundering herd mitigations.</p>
</div>

<!-- QA-01 -->
<div class="card">
  <span class="badge">QA-01 • The STAR Framework</span>
  <h3>The "Tell Me About a 2 AM Production Failure" Incident</h3>
  <div class="ans-box">
    <ul>
      <li><strong>Situation:</strong> At 2:15 AM, p99 latency on our customer service AI agent spiked from 800ms to 48 seconds, triggering PagerDuty alerts across the platform team.</li>
      <li><strong>Task:</strong> Identify the root cause, restore service without dropping customer chats, and eliminate the vulnerability permanently.</li>
      <li><strong>Action:</strong> Low-level tracing revealed a downstream CRM API was returning HTTP 429 HTML rate-limit error pages. The agent interpreted the HTML body as new instructions and entered an unbounded reflection loop. We applied emergency circuit breakers, capped <code>max_iterations = 4</code>, and enforced exponential backoff with full jitter.</li>
      <li><strong>Result:</strong> P99 latency recovered to 650ms. Incident post-mortem introduced automated CI/CD chaos tests, saving estimated $45k/month in runaway token loops.</li>
    </ul>
  </div>
</div>

<!-- QA-09 -->
<div class="card">
  <span class="badge">QA-09 • Network Race Condition</span>
  <h3>Intermittent 502 Bad Gateway Under Load</h3>
  <div class="q-box">
    <b>The Mystery:</b> 1.5% of requests fail with 502 Bad Gateway, but backend CPU is low and pods are not restarting.
  </div>
  <div class="ans-box">
    <b>The TCP Keepalive Mismatch:</b>
    <p>When the upstream reverse proxy (Nginx / ALB) has a keepalive timeout longer than the backend server (FastAPI/Uvicorn), the backend can send a <code>TCP FIN</code> at the exact moment the proxy forwards a new request, resulting in an immediate <code>TCP RST</code>.</p>
    <div class="play-box" style="margin:10px 0;">
      <b>Golden Rule:</b> Backend keepalive timeout must ALWAYS be strictly greater than proxy timeout:
      <pre><code># Nginx Ingress Proxy: keepalive_timeout 65s;
# Uvicorn Backend:     uvicorn.run(..., timeout_keep_alive=75)</code></pre>
    </div>
  </div>
</div>

<!-- QA-10 -->
<div class="card">
  <span class="badge">QA-10 • Thundering Herd</span>
  <h3>10 AM Traffic Spikes: Full Jitter Backoff Formula</h3>
  <div class="ans-box">
    <p>Break synchronous retry waves with AWS-style Full Jitter:</p>
    <pre><code>import random

def get_sleep_time(attempt, base_delay=1.0, max_delay=30.0):
    # Full Jitter decorrelates client retry storms
    temp = min(max_delay, base_delay * (2 ** attempt))
    return random.uniform(0, temp)</code></pre>
  </div>
</div>
"""
make_page("cloud-devops-failures.html", "Cloud SRE, Networking & Production Failures", "Module 09: Production War Stories", p9_content, "k8s-gpu-infra.html", "08. K8s & Autoscaling", "eval-security-drills.html", "10. Evals & Drills")

# ==============================================================================
# PAGE 10: EVAL-SECURITY-DRILLS.HTML
# ==============================================================================
p10_content = """
<div class="card">
  <h2>Automated Evaluations, Red Teaming & 30-Day Interview Drills</h2>
  <p>Covers <strong>QA-18, QA-19, QA-35, QA-38, QA-41</strong>, and the complete <strong>Section F 30-Day Mock Drill Framework</strong>. Master LLM-as-a-judge quality gates, eBPF runtime security, and candidate interview execution.</p>
</div>

<!-- QA-19 & QA-41 -->
<div class="card">
  <span class="badge">QA-19 / QA-41 • Quality Gates</span>
  <h3>Automated LLM Evaluation CI/CD Gate (The Ragas Triad)</h3>
  <div class="ans-box">
    <table style="width:100%; border-collapse:collapse; font-size:14px;">
      <tr style="border-bottom:1px solid var(--line);"><th style="padding:8px;">Metric</th><th>Formula / Definition</th><th>Pass Threshold</th></tr>
      <tr style="border-bottom:1px solid var(--line);"><td style="padding:8px; color:var(--teal);">Faithfulness</td><td>Verifiable claims in output &divide; claims in source context</td><td>&ge; 0.92 (Zero hallucinations)</td></tr>
      <tr style="border-bottom:1px solid var(--line);"><td style="padding:8px; color:var(--amber);">Answer Relevancy</td><td>Cosine similarity of answer vs user query</td><td>&ge; 0.88</td></tr>
      <tr><td style="padding:8px; color:var(--blue);">Context Recall</td><td>Ground truth facts retrieved &divide; total facts needed</td><td>&ge; 0.85</td></tr>
    </table>
    <p style="margin-top:12px;">Enforce in GitHub Actions: Block PR merge if Faithfulness drops by &gt; 2% against the baseline test suite.</p>
  </div>
</div>

<!-- QA-38 -->
<div class="card">
  <span class="badge">QA-38 • Security & Red Teaming</span>
  <h3>Indirect Prompt Injection: The Dual-LLM Defense Pattern</h3>
  <div class="ans-box">
    <ol>
      <li><strong>Untrusted Data Extractor (Zero Tools):</strong> Reads raw emails and PDFs. Outputs purely typed Pydantic JSON. Has zero access to network or file tools.</li>
      <li><strong>Privileged Agent:</strong> Reads validated JSON fields only. Never sees raw external prompt strings.</li>
      <li><strong>Execution Isolation:</strong> Tool executions (code scripts, bash commands) run in ephemeral AWS Firecracker microVMs with link-local IP <code>169.254.169.254</code> blocked.</li>
    </ol>
  </div>
</div>

<!-- 30-DAY DRILL CALENDAR -->
<div class="play-box">
  <span class="badge">Section F • Candidate Execution</span>
  <h3>30-Day Mock Interview Rehearsal Framework</h3>
  <div class="grid-2">
    <div>
      <h4 style="color:var(--amber);">Week 1: Serving & Memory Math</h4>
      <p style="font-size:13px;">Calculate Llama-3-70B KV cache on whiteboard cold. Explain FlashAttention online softmax and PagedAttention block tables without hesitation.</p>
      
      <h4 style="color:var(--teal);">Week 2: Kubernetes & Networking</h4>
      <p style="font-size:13px;">Write a KEDA queue-based ScaledObject manifest. Explain IPVS vs eBPF Cilium bypass for 5,000 services.</p>
    </div>
    <div>
      <h4 style="color:var(--blue);">Week 3: Agents & Protocols</h4>
      <p style="font-size:13px;">Build a LangGraph state graph with checkpointer and pre-generated idempotency tokens. Whiteboard Model Context Protocol (MCP) vs REST.</p>
      
      <h4 style="color:var(--rose);">Week 4: Failure War Stories & System Design</h4>
      <p style="font-size:13px;">Rehearse the "2 AM Production Incident" using the STAR framework. Execute full 45-minute timed whiteboard RAG designs.</p>
    </div>
  </div>
</div>
"""
make_page("eval-security-drills.html", "Evals, Red Teaming & 30-Day Interview Drills", "Module 10: Governance & Rehearsal", p10_content, "cloud-devops-failures.html", "09. SRE & Incidents", None, None)

print("ALL 10 PAGES GENERATED SUCCESSFULLY!")
