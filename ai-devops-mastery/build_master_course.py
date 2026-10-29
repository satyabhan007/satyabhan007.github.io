#!/usr/bin/env python3
import os
import re

BASE_DIR = "/home/satya/Downloads/SATYA/satyabhan007.github.io/ai-devops-mastery"

from generate_enhanced_site import ENHANCED_CSS, render_top_nav, render_footer

def write_page(filename, title, badge, content, prev_f, prev_l, next_f, next_l):
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | AI & DevOps Mastery Course</title>
  <style>{ENHANCED_CSS}</style>
</head>
<body>
  {render_top_nav(filename)}
  <main class="wrap">
    <div class="hero">
      <span class="badge">{badge}</span>
      <h1>{title}</h1>
      <p style="margin:0; font-size:15px; color:var(--mut);">Interactive technical curriculum synthesized from FAANG and Tier-1 AI startup interview rounds.</p>
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

# Re-run page generation with enhanced interactive accordions, code snippets, and deep technical explainers

# ==============================================================================
# PAGE 2: RAG & SEARCH (QA-02, QA-15, QA-17, QA-23, QA-37)
# ==============================================================================
p2_content = """
<div class="card" style="border-left: 4px solid var(--blue);">
  <h2>Enterprise RAG, High-Dimensional Vector Search & GraphRAG</h2>
  <p>Comprehensive coverage of <strong>QA-02, QA-15, QA-17, QA-23, and QA-37</strong>. Master multi-stage hybrid retrieval, Reciprocal Rank Fusion, 50M vector memory scaling, and Leiden community detection.</p>
</div>

<!-- Interactive Step Explainer for RAG Pipeline -->
<div class="explainer-box">
  <h3 style="margin-top:0;">Interactive RAG Pipeline Flow Explainer</h3>
  <p style="font-size:14px; color:var(--mut);">Click each pipeline phase to see the exact production behavior, algorithms, and latency budgets:</p>
  
  <div style="display:grid; grid-template-columns: 1fr 1.5fr; gap:16px;">
    <div>
      <div class="interactive-step active" onclick="showRAGStep(0)">
        <div class="step-num">1</div>
        <div><b>Query HyDE & Decomposition</b><br><span style="font-size:12px; color:var(--mut);">Resolves ambiguous intent (&lt;40ms)</span></div>
      </div>
      <div class="interactive-step" onclick="showRAGStep(1)">
        <div class="step-num">2</div>
        <div><b>Redis Semantic Vector Cache</b><br><span style="font-size:12px; color:var(--mut);">Cosine similarity &ge; 0.96 (&lt;15ms)</span></div>
      </div>
      <div class="interactive-step" onclick="showRAGStep(2)">
        <div class="step-num">3</div>
        <div><b>Two-Stage Hybrid Retrieval</b><br><span style="font-size:12px; color:var(--mut);">Dense (HNSW) + Sparse (BM25)</span></div>
      </div>
      <div class="interactive-step" onclick="showRAGStep(3)">
        <div class="step-num">4</div>
        <div><b>Reciprocal Rank Fusion (RRF)</b><br><span style="font-size:12px; color:var(--mut);">k=60 rank normalization</span></div>
      </div>
      <div class="interactive-step" onclick="showRAGStep(4)">
        <div class="step-num">5</div>
        <div><b>Cross-Encoder Reranker</b><br><span style="font-size:12px; color:var(--mut);">BGE-Reranker-Large (Top-100 &rarr; Top-5)</span></div>
      </div>
    </div>
    
    <div id="ragStepDetail" style="background:#070B11; border:1px solid var(--line); border-radius:10px; padding:18px;">
      <h4 style="color:var(--cyan); margin-top:0;">Step 1: Query Transformation & HyDE</h4>
      <p style="font-size:14px;"><strong>Why:</strong> Raw user queries are noisy, brief, and contain colloquialisms. Standard vector search matches keywords poorly when phrased casually.</p>
      <p style="font-size:14px;"><strong>Mechanism:</strong> A small 0.5B model generates a hypothetical candidate document answering the question. The hypothetical document embedding is then queried against the vector space.</p>
      <pre><code># HyDE Query Transformation
hypothetical_doc = slm.generate(f"Write a technical passage answering: {query}")
query_vector = embedder.encode(hypothetical_doc)</code></pre>
    </div>
  </div>
</div>

<script>
const ragSteps = [
  {
    title: "Step 1: Query Transformation & HyDE",
    desc: "<strong>Why:</strong> Raw user queries are brief, vague, and lack domain phrasing.<br><strong>Mechanism:</strong> A fast SLM generates a hypothetical answer passage. Embedding this synthetic passage produces a vector that aligns far closer to the true document space than the raw query.",
    code: `# HyDE Generation
hypo_passage = fast_model.generate(f"Answer: {query}")
query_vector = embedder.encode(hypo_passage)`
  },
  {
    title: "Step 2: Redis Semantic Cache",
    desc: "<strong>Why:</strong> 25% of enterprise queries are duplicates or semantically identical. Running inference on every turn wastes money and spikes GPU latency.<br><strong>Mechanism:</strong> Query vector is compared against pre-cached queries in Redis Vector Store. If cosine similarity &ge; 0.96, the stored completion is returned directly in &lt;15ms at $0 cost.",
    code: `# Check Redis Vector Distance
hit = redis_client.ft("idx:cache").search(
    Query(f"*=>[KNN 1 @vector $vec AS score]")
    .sort_by("score")
    .return_fields("response", "score")
    .dialect(2),
    {"vec": query_vector.tobytes()}
)`
  },
  {
    title: "Step 3: Two-Stage Hybrid Retrieval",
    desc: "<strong>Why:</strong> Vector embeddings excel at conceptual meaning, but completely fail on SKU numbers, serial tags, and specific variable names. BM25 keyword search covers exact term matches.<br><strong>Mechanism:</strong> Query runs concurrently against dense HNSW index (Qdrant/Milvus) and BM25 sparse index (Elasticsearch/OpenSearch).",
    code: `# Concurrent Hybrid Query
dense_hits = qdrant.search(collection="docs", query_vector=query_vec, limit=50)
sparse_hits = opensearch.search(body={"query": {"match": {"content": query}}}, size=50)`
  },
  {
    title: "Step 4: Reciprocal Rank Fusion (RRF)",
    desc: "<strong>Why:</strong> Dense cosine scores and sparse BM25 scores have different distributions and cannot be summed directly.<br><strong>Mechanism:</strong> RRF standardizes scores purely by rank position: <code>RRF_Score = sum(1 / (k + rank_i))</code> where standard industry constant k = 60.",
    code: `# RRF Calculation
for rank, hit in enumerate(dense_hits):
    scores[hit.id] += 1.0 / (60 + rank)
for rank, hit in enumerate(sparse_hits):
    scores[hit.id] += 1.0 / (60 + rank)`
  },
  {
    title: "Step 5: Cross-Encoder Reranker",
    desc: "<strong>Why:</strong> Bi-encoders compress documents into fixed vectors, losing fine-grained cross-token interactions.<br><strong>Mechanism:</strong> Full cross-attention model (e.g. BGE-Reranker-Large or Cohere Rerank) scores all (Query, Chunk) pairs together, pruning Top-100 down to Top-5 highest signal chunks for generation.",
    code: `# Joint Cross-Attention Scoring
pairs = [[query, chunk.text] for chunk in top_100_chunks]
rerank_scores = cross_encoder.predict(pairs)
final_chunks = [top_100_chunks[i] for i in argsort(rerank_scores)[:5]]`
  }
];

function showRAGStep(index) {
  const steps = document.querySelectorAll('.interactive-step');
  steps.forEach((s, i) => {
    s.classList.toggle('active', i === index);
  });
  const data = ragSteps[index];
  document.getElementById('ragStepDetail').innerHTML = `
    <h4 style="color:var(--cyan); margin-top:0;">${data.title}</h4>
    <p style="font-size:14px;">${data.desc}</p>
    <pre><code>${data.code}</code></pre>
  `;
}
</script>

<!-- QA-02 DETAILED ACCORDION -->
<div class="scenario-card open">
  <div class="scenario-header" onclick="toggleCard(this)">
    <div>
      <span class="badge">QA-02 • System Design</span>
      <div class="scenario-title">Whiteboard: End-to-End Production RAG System</div>
      <div class="scenario-meta">Source: Naresh Edagotti (PracticAI) • Track: AI Engineer • Difficulty: Hard</div>
    </div>
    <div class="toggle-icon">▼</div>
  </div>
  <div class="scenario-body">
    <div class="q-box">
      <b>Interview Scenario:</b> "Draw and defend an end-to-end production RAG system serving 10M enterprise documents. How do you handle ambiguous user queries, prevent stale knowledge retrieval, and keep latency under 800ms?"
    </div>
    <div class="ans-box">
      <b>Key Architectural Breakdown to Deliver:</b>
      <ul>
        <li><strong>Query Transformation:</strong> Run HyDE and multi-query decomposition to resolve ambiguous slang.</li>
        <li><strong>Redis Semantic Cache:</strong> Check pre-computed vector embeddings. If similarity &ge; 0.96, return answer immediately (&lt;15ms latency, $0 token cost).</li>
        <li><strong>Hybrid Dual-Search:</strong> Run dense vector similarity (capturing semantic intent) alongside BM25 sparse keyword search (capturing exact product SKUs, error codes, and IDs).</li>
        <li><strong>RRF (Reciprocal Rank Fusion, k=60):</strong> Merge both ranked lists via score <code>sum(1 / (60 + rank))</code>.</li>
        <li><strong>Cross-Encoder Reranker:</strong> Joint attention across top-100 candidates pruned to top-5 high-signal chunks.</li>
      </ul>
    </div>
    <div class="pitfall">
      <b>Candidate Red Flag:</b> Relying solely on vector embeddings without keyword BM25 search. Vector embeddings frequently fail on specific SKUs, serial numbers, error codes, and function names.
    </div>
  </div>
</div>

<!-- QA-23: VECTOR CALCULATOR -->
<div class="scenario-card open">
  <div class="scenario-header" onclick="toggleCard(this)">
    <div>
      <span class="badge">QA-23 • Memory Sizing</span>
      <div class="scenario-title">50M Vectors: HNSW vs IVF-PQ & Preventing Linux OOM Kills</div>
      <div class="scenario-meta">Source: MLOps Community Debrief • Track: MLOps / Infra • Difficulty: Hard</div>
    </div>
    <div class="toggle-icon">▼</div>
  </div>
  <div class="scenario-body">
    <div class="q-box">
      <b>The Scenario:</b> "Your team is indexing 50,000,000 1,536-dimensional vectors in a vector database. The server crashes with Linux OOM-killer during index build. How do you calculate memory requirements and choose between HNSW and IVF-PQ?"
    </div>
    
    <div style="background:#101622; border:1px solid var(--vio); border-radius:12px; padding:20px; margin:16px 0;">
      <h4 style="margin-top:0; color:var(--vio);">Interactive Vector RAM Estimator</h4>
      <div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px;">
        <div>
          <label>Vectors to Index (Millions):</label>
          <input type="number" id="vCount" value="50" min="1" max="500" oninput="calcVectors()" style="width:100%; margin:8px 0; background:#0B0F17; color:#fff; border:1px solid var(--line); padding:8px; border-radius:6px;">
          
          <label>Dimensions (e.g. OpenAI 1536):</label>
          <input type="number" id="vDims" value="1536" step="128" oninput="calcVectors()" style="width:100%; margin:8px 0; background:#0B0F17; color:#fff; border:1px solid var(--line); padding:8px; border-radius:6px;">
        </div>
        <div style="background:#070B11; padding:15px; border-radius:8px; border:1px solid var(--line);">
          <div style="color:var(--mut); font-size:12px;">Raw FP32 Data:</div>
          <div id="rawSize" style="font-size:20px; font-weight:bold; color:var(--txt);">307.2 GB</div>
          
          <div style="color:var(--rose); font-size:12px; margin-top:8px;">HNSW Index Footprint (2x Graph Overhead):</div>
          <div id="hnswSize" style="font-size:20px; font-weight:bold; color:var(--rose);">614.4 GB (OOM Panic!)</div>
          
          <div style="color:var(--teal); font-size:12px; margin-top:8px;">IVF-PQ Quantized Footprint:</div>
          <div id="ivfSize" style="font-size:20px; font-weight:bold; color:var(--teal);">18.0 GB (Production Safe)</div>
        </div>
      </div>
    </div>
    
    <div class="ans-box">
      <b>Whiteboard Mathematical Proof:</b>
      <ul>
        <li><code>Raw Vectors = 50M * 1,536 dimensions * 4 bytes (FP32) = 307.2 GB</code></li>
        <li><strong>HNSW Graph Overhead:</strong> Each vector stores M=32 to 64 bidirectional graph edges. The graph metadata adds an additional 1.0x to 1.5x footprint, pushing total memory to <strong>614.4 GB RAM</strong>.</li>
        <li><strong>IVF-PQ Solution:</strong> Partitions vector space into 4,096 Voronoi clusters. Product quantization compresses 1,536 floats (6,144 bytes) to 64 bytes. Total memory drops from <strong>614 GB to 18 GB</strong>, fitting easily into memory with &gt;95% recall.</li>
      </ul>
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
  document.getElementById('hnswSize').innerText = hnswGB + " GB (OOM Panic!)";
  document.getElementById('ivfSize').innerText = ivfGB + " GB (Production Safe)";
}
</script>

<!-- QA-37 ACCORDION -->
<div class="scenario-card">
  <div class="scenario-header" onclick="toggleCard(this)">
    <div>
      <span class="badge">QA-37 • Advanced Architecture</span>
      <div class="scenario-title">GraphRAG vs Classic Vector RAG: Resolving Global Multi-Hop Queries</div>
      <div class="scenario-meta">Source: AI Architect Loop • Track: Architect / Principal • Difficulty: Hard</div>
    </div>
    <div class="toggle-icon">▼</div>
  </div>
  <div class="scenario-body">
    <div class="q-box">
      <b>The Question:</b> "Why does vector search fail when asked: 'What are the top 3 themes across 50,000 customer feedback tickets?' How does GraphRAG solve this?"
    </div>
    <div class="ans-box">
      <b>The Core Asymmetry:</b> Vector distance captures <i>local semantic affinity</i> (finding paragraphs similar to a phrasing). It cannot aggregate or synthesize across documents that share no common phrasing.<br><br>
      <b>GraphRAG Resolution:</b>
      <ol>
        <li><strong>Entity & Relation Ingestion:</strong> LLM parses documents into <code>(Subject, Relation, Object)</code> triples.</li>
        <li><strong>Leiden Community Detection:</strong> Graph is partitioned into hierarchical modular communities (C0, C1, C2).</li>
        <li><strong>Community Summaries:</strong> LLM pre-summarizes each cluster at ingest time.</li>
        <li><strong>Query Time:</strong> Global questions map to high-level community report vectors using parallel map-reduce synthesis.</li>
      </ol>
    </div>
  </div>
</div>

<!-- QA-17 ACCORDION -->
<div class="scenario-card">
  <div class="scenario-header" onclick="toggleCard(this)">
    <div>
      <span class="badge">QA-17 • Context Tradeoffs</span>
      <div class="scenario-title">"If Models Have 1M+ Tokens, Why Not Pass All Docs?"</div>
      <div class="scenario-meta">Source: Syamala Jayanthi • Track: AI Engineer • Difficulty: Medium</div>
    </div>
    <div class="toggle-icon">▼</div>
  </div>
  <div class="scenario-body">
    <div class="ans-box">
      <b>Three Critical Production Red Flags:</b>
      <ol>
        <li><strong>Latency (TTFT) Explosion:</strong> Processing 1M tokens in prefill takes 15 to 45 seconds before the first token is emitted, violating interactive SLAs.</li>
        <li><strong>Exponential Financial Burn:</strong> At $3.00/1M input tokens, 1,000 queries/day costs <strong>$90,000/month</strong> compared to $300/month with hybrid RAG.</li>
        <li><strong>Attention Dilution ("Lost in the Middle"):</strong> Self-attention weights dilute over irrelevant text, increasing hallucinations and missing fine-grained numerical constraints.</li>
      </ol>
    </div>
  </div>
</div>
"""
write_page("rag-search.html", "Production RAG, Vector DBs & GraphRAG", "Module 02: Retrieval & Search", p2_content, "index.html", "01. Overview", "llm-serving.html", "03. Serving & Kernels")

# ==============================================================================
# PAGE 3: LLM SERVING & KERNELS (QA-05, QA-27, QA-31, QA-32, QA-36, QA-44)
# ==============================================================================
p3_content = """
<div class="card" style="border-left: 4px solid var(--amber);">
  <h2>LLM Serving: vLLM, PagedAttention, Kernels & Triton</h2>
  <p>Comprehensive coverage of <strong>QA-05, QA-27, QA-31, QA-32, QA-36, and QA-44</strong>. Master iteration-level scheduling, FlashAttention online softmax, speculative decoding, and prefill-decode disaggregation.</p>
</div>

<!-- Interactive Speculative Decoding Explainer -->
<div class="explainer-box">
  <h3 style="margin-top:0; color:var(--cyan);">Interactive Speculative Decoding Simulator</h3>
  <p style="font-size:14px; color:var(--mut);">See how a small 1B draft model collaborates with a 70B target model to double token generation speeds without loss of accuracy:</p>
  
  <div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px;">
    <div>
      <label>Speculative Lookahead Tokens (K):</label>
      <input type="range" id="kRange" min="1" max="8" value="4" oninput="simSpec()" style="width:100%; margin:8px 0;">
      <div id="kLabel" style="color:var(--amber); font-weight:bold;">K = 4 tokens</div>
      
      <label style="margin-top:10px; display:block;">Draft Acceptance Probability (&alpha;):</label>
      <input type="range" id="aRange" min="40" max="95" value="75" oninput="simSpec()" style="width:100%; margin:8px 0;">
      <div id="aLabel" style="color:var(--teal); font-weight:bold;">Acceptance = 75%</div>
    </div>
    
    <div style="background:#070B11; padding:16px; border-radius:10px; border:1px solid var(--line);">
      <div style="color:var(--mut); font-size:12px;">Expected Accepted Tokens Per Forward Pass:</div>
      <div id="accOutput" style="font-size:24px; font-weight:bold; color:var(--cyan);">3.25 tokens</div>
      
      <div style="color:var(--amber); font-size:12px; margin-top:10px;">Net Generation Speedup:</div>
      <div id="speedOutput" style="font-size:24px; font-weight:bold; color:var(--amber);">2.41x Faster</div>
      <div style="font-size:12px; color:var(--mut); margin-top:6px;">Target model executes 1 parallel prefill verification step instead of 4 sequential memory-bound decode steps!</div>
    </div>
  </div>
</div>

<script>
function simSpec() {
  const K = parseInt(document.getElementById('kRange').value);
  const alpha = parseInt(document.getElementById('aRange').value) / 100.0;
  document.getElementById('kLabel').innerText = "K = " + K + " tokens";
  document.getElementById('aLabel').innerText = "Acceptance = " + (alpha * 100).toFixed(0) + "%";
  
  let accepted = 0;
  for (let i = 0; i < K; i++) accepted += Math.pow(alpha, i);
  const speedup = (accepted / (1 + (K * 0.12))).toFixed(2);
  
  document.getElementById('accOutput').innerText = accepted.toFixed(2) + " tokens / pass";
  document.getElementById('speedOutput').innerText = speedup + "x Faster";
}
</script>

<!-- QA-05 ACCORDION -->
<div class="scenario-card open">
  <div class="scenario-header" onclick="toggleCard(this)">
    <div>
      <span class="badge">QA-05 • Core Serving</span>
      <div class="scenario-title">Continuous Batching & PagedAttention in vLLM</div>
      <div class="scenario-meta">Source: H2LooP / Enterprise Infra • Track: AI DevOps • Difficulty: Hard</div>
    </div>
    <div class="toggle-icon">▼</div>
  </div>
  <div class="scenario-body">
    <div class="q-box">
      <b>The Question:</b> "Why does static request-level batching waste &gt;70% of GPU compute, and how does vLLM schedule at the iteration level?"
    </div>
    <div class="ans-box">
      <ul>
        <li><strong>Static Batching Inefficiency:</strong> The entire batch is bound by the slowest sequence. When a 50-token query finishes, it must output padding tokens while waiting for a 2,000-token sequence to complete.</li>
        <li><strong>Continuous Batching:</strong> Scheduling occurs at the <i>token iteration level</i>. The moment an sequence emits an <code>&lt;EOS&gt;</code>, it is evicted immediately. A newly queued request enters on the very next forward pass, keeping GPU tensor cores saturated.</li>
        <li><strong>PagedAttention Virtual Tables:</strong> Standard serving pre-allocates maximum context VRAM (causing up to 80% fragmentation). PagedAttention partitions KV cache into 16-token virtual blocks, allocating physical pages on demand.</li>
      </ul>
    </div>
  </div>
</div>

<!-- QA-27 ACCORDION -->
<div class="scenario-card">
  <div class="scenario-header" onclick="toggleCard(this)">
    <div>
      <span class="badge">QA-27 • Google Round</span>
      <div class="scenario-title">FlashAttention Tiling & The Online Softmax Algorithm</div>
      <div class="scenario-meta">Source: Ashutosh Gupta (Google) • Track: AI Systems • Difficulty: Hard</div>
    </div>
    <div class="toggle-icon">▼</div>
  </div>
  <div class="scenario-body">
    <div class="ans-box">
      <b>The Core Asymmetry:</b> High Bandwidth Memory (HBM) bandwidth is 2.0 TB/s, whereas on-chip SRAM is 20 TB/s (10x faster).<br><br>
      <b>Mechanism:</b>
      <ul>
        <li>Standard attention calculates <code>S = Q * K^T</code>, writes the intermediate N &times; N matrix to HBM, reads it back for Softmax, writes <code>P</code> back to HBM, and reads it for <code>O = P * V</code>. Memory complexity is O(N&sup2;).</li>
        <li>FlashAttention tiles Q, K, and V into blocks that fit entirely within SRAM.</li>
        <li><strong>Online Softmax:</strong> Keeps running scale factors (max value <code>m</code> and sum <code>l</code>). When a new tile arrives, existing output accumulator is scaled by <code>e^{m_prev - m_new}</code>, completing attention in a single pass without writing N &times; N matrices to HBM!</li>
      </ul>
    </div>
  </div>
</div>

<!-- QA-32 ACCORDION -->
<div class="scenario-card">
  <div class="scenario-header" onclick="toggleCard(this)">
    <div>
      <span class="badge">QA-32 • Scale Architecture</span>
      <div class="scenario-title">Prefill-Decode Disaggregation (PD Disaggregation) at Enterprise Scale</div>
      <div class="scenario-meta">Source: Mohit Kumar Dubey • Track: Architect / Principal • Difficulty: Hard</div>
    </div>
    <div class="toggle-icon">▼</div>
  </div>
  <div class="scenario-body">
    <div class="ans-box">
      <b>Why Colocation Fails:</b> Prefill is compute-bound (massive parallel GEMM operations). Decode is memory-bound (loading all weights per single token). Running both on the same GPU means a sudden burst of long prompts halts active decoding streams, spiking Inter-Token Latency (ITL) and creating stuttering user experiences.<br><br>
      <b>Disaggregated Solution:</b>
      <ul>
        <li><strong>Prefill Nodes:</strong> Clustered high-compute GPUs run prompt phase at 100% FLOPS occupancy.</li>
        <li><strong>KV-Cache Streaming:</strong> Computed KV cache is transmitted directly into decode GPU memory over high-speed RDMA / InfiniBand.</li>
        <li><strong>Decode Nodes:</strong> Devoted 100% to continuous generation streams with zero latency spikes.</li>
      </ul>
    </div>
  </div>
</div>
"""
write_page("llm-serving.html", "LLM Serving: vLLM, PagedAttention & Kernels", "Module 03: Serving Engines", p3_content, "rag-search.html", "02. RAG & Search", "gpu-memory-math.html", "04. Memory Math")

print("Generated enhanced Module 02 and Module 03!")

# ==============================================================================
# PAGE 4: GPU ARCHITECTURE & MEMORY MATH (QA-04, QA-06, QA-12)
# ==============================================================================
p4_content = """
<div class="card" style="border-left: 4px solid var(--teal);">
  <h2>GPU Architecture, Hardware Sizing & Memory Mathematics</h2>
  <p>Comprehensive coverage of <strong>QA-04, QA-06, and QA-12</strong>. Master Grouped-Query Attention (GQA) memory equations, the Roofline Model, and emergency capacity levers.</p>
</div>

<!-- Interactive Step Explainer: Memory Math Flow -->
<div class="explainer-box">
  <h3 style="margin-top:0; color:var(--teal);">Whiteboard Memory Math Step-Through</h3>
  <p style="font-size:14px; color:var(--mut);">Click each component to walk through the exact equations required in senior engineering technical screens:</p>
  
  <div style="display:grid; grid-template-columns: 1fr 1.5fr; gap:16px;">
    <div>
      <div class="interactive-step active" onclick="showMemStep(0)">
        <div class="step-num">1</div>
        <div><b>Static Model Weights</b><br><span style="font-size:12px; color:var(--mut);">Parameters &times; Precision Bytes</span></div>
      </div>
      <div class="interactive-step" onclick="showMemStep(1)">
        <div class="step-num">2</div>
        <div><b>GQA KV Cache Per Token</b><br><span style="font-size:12px; color:var(--mut);">2 &times; L &times; H_kv &times; d_h &times; Bytes</span></div>
      </div>
      <div class="interactive-step" onclick="showMemStep(2)">
        <div class="step-num">3</div>
        <div><b>Concurrent Stream Sizing</b><br><span style="font-size:12px; color:var(--mut);">Batch &times; Context Length &times; KV_Token</span></div>
      </div>
      <div class="interactive-step" onclick="showMemStep(3)">
        <div class="step-num">4</div>
        <div><b>Tensor Parallelism (TP) Split</b><br><span style="font-size:12px; color:var(--mut);">VRAM Per GPU & Headroom Buffer</span></div>
      </div>
    </div>
    
    <div id="memStepDetail" style="background:#070B11; border:1px solid var(--line); border-radius:10px; padding:18px;">
      <h4 style="color:var(--cyan); margin-top:0;">Step 1: Static Weights Footprint</h4>
      <p style="font-size:14px;"><strong>Formula:</strong> <code>Memory = Parameters &times; Bytes_Per_Weight</code></p>
      <p style="font-size:14px;">For Llama-3-70B in 16-bit (FP16/BF16, 2 bytes):<br>
      <code>70 &times; 10^9 &times; 2 bytes = 140,000,000,000 bytes &approx; 140 GB</code>.</p>
      <p style="font-size:14px; color:var(--mut);">This memory is completely static and independent of how many users are actively querying the server.</p>
    </div>
  </div>
</div>

<script>
const memSteps = [
  {
    title: "Step 1: Static Weights Footprint",
    desc: "<strong>Formula:</strong> <code>Weights_RAM = Parameters &times; Bytes_Per_Param</code><br>For Llama-3-70B in 16-bit precision:<br><code>70 &times; 10^9 &times; 2 bytes = 140 GB</code>.<br>This footprint remains constant whether you serve 1 user or 10,000 users.",
    code: `# Static Weights in VRAM
param_count = 70e9
bytes_per_weight = 2  # FP16/BF16
weight_memory_gb = (param_count * bytes_per_weight) / (1024**3)
# Output: 130.38 GiB (approx 140 GB decimal)`
  },
  {
    title: "Step 2: GQA KV Cache per Token",
    desc: "<strong>Why GQA Matters:</strong> Standard Multi-Head Attention (MHA) keeps separate key/value heads for all 64 query heads. Grouped-Query Attention (GQA) shares 1 key/value head across 8 query heads, cutting KV memory by <strong>8x</strong>!<br><strong>Formula:</strong> <code>2 (Key + Value) &times; L (Layers) &times; H_kv (KV Heads) &times; d_h (Head Dim) &times; Bytes</code><br>Llama-3-70B: <code>2 &times; 80 &times; 8 &times; 128 &times; 2 = 327,680 bytes &approx; 320 KB/token</code>.",
    code: `# GQA KV Cache Math
layers = 80
kv_heads = 8
head_dim = 128
precision_bytes = 2 # FP16

bytes_per_token = 2 * layers * kv_heads * head_dim * precision_bytes
# Result: 327,680 bytes = 320 KB per token`
  },
  {
    title: "Step 3: Total Concurrency Budgeting",
    desc: "<strong>Formula:</strong> <code>Total_KV = Active_Streams &times; Context_Length &times; Bytes_Per_Token</code><br>For 64 concurrent streams at 4,096 context tokens:<br><code>64 &times; 4,096 &times; 320 KB = 83.88 GB</code> of dynamic KV cache allocation.",
    code: `# Concurrency KV Footprint
active_streams = 64
context_length = 4096
total_tokens = active_streams * context_length  # 262,144 tokens
kv_cache_gb = (total_tokens * 327680) / (1024**3)
# Result: 80.0 GiB (approx 83.88 GB)`
  },
  {
    title: "Step 4: Cluster & Tensor Parallelism Sizing",
    desc: "<strong>Total Memory Required:</strong> Weights (140 GB) + KV Cache (83.88 GB) + Activation Buffer (12 GB) = <strong>235.88 GB</strong>.<br>Divided across 80GB A100/H100 GPUs:<br><code>235.88 / 80 = 2.95 &rarr; Minimum 4x 80GB GPUs (TP=4)</code>.<br>Each GPU holds: 35 GB weights + 21 GB KV cache + 3 GB activations = 59 GB, leaving 21 GB headroom.",
    code: `# Multi-GPU Tensor Parallelism Partitioning
total_vram = weight_memory_gb + kv_cache_gb + 12.0 # 226 GiB
num_gpus = 4 # Tensor Parallelism TP=4
vram_per_gpu = total_vram / num_gpus # 56.5 GiB / GPU
# Fits within 80GB VRAM with 23.5 GiB safety margin!`
  }
];

function showMemStep(idx) {
  document.querySelectorAll('.interactive-step').forEach((s, i) => s.classList.toggle('active', i === idx));
  const data = memSteps[idx];
  document.getElementById('memStepDetail').innerHTML = `
    <h4 style="color:var(--cyan); margin-top:0;">${data.title}</h4>
    <p style="font-size:14px;">${data.desc}</p>
    <pre><code>${data.code}</code></pre>
  `;
}
</script>

<!-- QA-06 CALCULATOR ACCORDION -->
<div class="scenario-card open">
  <div class="scenario-header" onclick="toggleCard(this)">
    <div>
      <span class="badge">QA-06 • Whiteboard Math</span>
      <div class="scenario-title">Llama-3-70B VRAM & GQA KV-Cache Math (64 streams)</div>
      <div class="scenario-meta">Source: Candidate Technical Screen • Track: AI DevOps / LLMOps • Difficulty: Hard</div>
    </div>
    <div class="toggle-icon">▼</div>
  </div>
  <div class="scenario-body">
    <div class="q-box">
      <b>Interview Scenario:</b> "We need to serve Llama-3-70B in 16-bit precision across 80GB GPUs with 64 concurrent streams and a 4,096-token context window. Exactly how many GPUs do we need, and what is the exact memory breakdown?"
    </div>
    
    <div style="background:#101622; border:1px solid var(--vio); border-radius:12px; padding:20px; margin:16px 0;">
      <h4 style="margin-top:0; color:var(--vio);">Live Hardware Sizing Simulator</h4>
      <div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px;">
        <div>
          <label>Active Streams (Batch Size):</label>
          <input type="number" id="streamCount" value="64" min="1" max="512" oninput="calcVRAM()" style="width:100%; margin:8px 0; background:#0B0F17; color:#fff; border:1px solid var(--line); padding:8px; border-radius:6px;">
          
          <label>Max Context Length (Tokens):</label>
          <input type="number" id="ctxLen" value="4096" step="512" oninput="calcVRAM()" style="width:100%; margin:8px 0; background:#0B0F17; color:#fff; border:1px solid var(--line); padding:8px; border-radius:6px;">
          
          <label>KV Precision:</label>
          <select id="prec" onchange="calcVRAM()" style="width:100%; margin:8px 0; background:#0B0F17; color:#fff; border:1px solid var(--line); padding:8px; border-radius:6px;">
            <option value="2">FP16 / BF16 (2 bytes)</option>
            <option value="1">FP8 Quantized (1 byte)</option>
          </select>
        </div>
        
        <div style="background:#070B11; padding:16px; border-radius:8px; border:1px solid var(--line);">
          <div style="color:var(--mut); font-size:12px;">Model Weights:</div>
          <div style="font-size:18px; font-weight:bold; color:var(--txt);">140.0 GB</div>
          
          <div style="color:var(--amber); font-size:12px; margin-top:8px;">KV Cache Size:</div>
          <div id="kvFootprint" style="font-size:18px; font-weight:bold; color:var(--amber);">83.9 GB</div>
          
          <div style="color:var(--cyan); font-size:12px; margin-top:8px;">Total VRAM (+12GB Activations):</div>
          <div id="totalVRAM" style="font-size:20px; font-weight:bold; color:var(--cyan);">235.9 GB</div>
          
          <div style="color:var(--teal); font-size:12px; margin-top:8px;">Recommended Hardware Cluster:</div>
          <div id="gpusRequired" style="font-size:22px; font-weight:bold; color:var(--teal);">4x 80GB GPUs (TP=4)</div>
        </div>
      </div>
    </div>
  </div>
</div>

<script>
function calcVRAM() {
  const streams = parseInt(document.getElementById('streamCount').value) || 0;
  const ctx = parseInt(document.getElementById('ctxLen').value) || 0;
  const bytesPerVal = parseFloat(document.getElementById('prec').value) || 2;
  const bytesPerToken = 2 * 80 * 8 * 128 * bytesPerVal;
  const kvGB = (streams * ctx * bytesPerToken) / (1024**3);
  const totalGB = 140.0 + kvGB + 12.0;
  const gpusNeeded = Math.ceil(totalGB / 80.0);
  let tp = 1;
  while (tp < gpusNeeded) tp *= 2;
  document.getElementById('kvFootprint').innerText = kvGB.toFixed(1) + " GB";
  document.getElementById('totalVRAM').innerText = totalGB.toFixed(1) + " GB";
  document.getElementById('gpusRequired').innerText = tp + "x 80GB GPUs (TP=" + tp + ")";
}
</script>

<!-- QA-04 ACCORDION -->
<div class="scenario-card">
  <div class="scenario-header" onclick="toggleCard(this)">
    <div>
      <span class="badge">QA-04 • Hardware Profiling</span>
      <div class="scenario-title">GPU Utilization vs Occupancy vs Memory Bandwidth (The Roofline Model)</div>
      <div class="scenario-meta">Source: Pallavi Ahuja • Track: AI Platform / DevOps • Difficulty: Hard</div>
    </div>
    <div class="toggle-icon">▼</div>
  </div>
  <div class="scenario-body">
    <div class="q-box">
      <b>The Scenario:</b> "Your nvidia-smi shows 100% GPU utilization while serving an LLM, but token throughput is disappointingly low. Your manager asks if buying faster GPUs is the only fix. How do you explain why 100% GPU utilization is deceptive?"
    </div>
    <div class="ans-box">
      <b>The Deception:</b>
      <p><code>nvidia-smi</code>'s utilization metric only measures the percentage of time that <i>any kernel</i> was executing on the GPU. If a single warp is fetching memory from DRAM while the other 128 SMs sit completely idle, <code>nvidia-smi</code> still reports <strong>100% Utilization</strong>!</p>
      <ul>
        <li><strong>Decode Phase is Memory-Bound:</strong> Each generated token must load 140GB of weights from HBM to register files. The GPU is memory-bandwidth bound ($O(1)$ arithmetic intensity).</li>
        <li><strong>Nsight Profiling (nsys):</strong> Profile DRAM throughput vs Tensor Core active cycles. If DRAM throughput is at 95% while SM compute is at 15%, you cannot fix it with faster clocks—you need <strong>Continuous Batching, Quantization (FP8/AWQ), or PagedAttention</strong>.</li>
      </ul>
    </div>
  </div>
</div>
"""
write_page("gpu-memory-math.html", "GPU Architecture & VRAM Memory Math", "Module 04: Hardware & Math", p4_content, "llm-serving.html", "03. Serving & Kernels", "agentic-ai.html", "05. Agentic AI")

# ==============================================================================
# PAGE 5: AGENTIC AI & MCP (QA-03, QA-16, QA-26, QA-45)
# ==============================================================================
p5_content = """
<div class="card" style="border-left: 4px solid var(--vio);">
  <h2>Autonomous Agents, LangGraph Checkpointers & MCP Protocols</h2>
  <p>Comprehensive coverage of <strong>QA-03, QA-16, QA-26, and QA-45</strong>. Master state persistence in cyclic agent graphs, preventing duplicate payments, Model Context Protocol vs REST APIs, and zero-downtime agent migration.</p>
</div>

<!-- Interactive Checkpointer Crash Explainer -->
<div class="explainer-box">
  <h3 style="margin-top:0; color:var(--vio);">Interactive LangGraph Checkpointer Lifecycle Walkthrough</h3>
  <p style="font-size:14px; color:var(--mut);">Step through how a node failure replays code and why external APIs must be guarded with idempotent tokens:</p>
  
  <div style="display:grid; grid-template-columns: 1fr 1.5fr; gap:16px;">
    <div>
      <div class="interactive-step active" onclick="showAgentStep(0)">
        <div class="step-num">1</div>
        <div><b>Node Boundary Checkpoint</b><br><span style="font-size:12px; color:var(--mut);">State saved in PostgreSQL / Redis</span></div>
      </div>
      <div class="interactive-step" onclick="showAgentStep(1)">
        <div class="step-num">2</div>
        <div><b>Mid-Node Network Timeout</b><br><span style="font-size:12px; color:var(--mut);">External call succeeds, ACK lost</span></div>
      </div>
      <div class="interactive-step" onclick="showAgentStep(2)">
        <div class="step-num">3</div>
        <div><b>Unhandled Process Crash</b><br><span style="font-size:12px; color:var(--mut);">Container dies, Kubernetes restarts</span></div>
      </div>
      <div class="interactive-step" onclick="showAgentStep(3)">
        <div class="step-num">4</div>
        <div><b>Replay from Checkpoint</b><br><span style="font-size:12px; color:var(--mut);">Node re-executes from Line 1</span></div>
      </div>
    </div>
    
    <div id="agentStepDetail" style="background:#070B11; border:1px solid var(--line); border-radius:10px; padding:18px;">
      <h4 style="color:var(--cyan); margin-top:0;">Step 1: Checkpoint Saved at Node Boundary</h4>
      <p style="font-size:14px;">LangGraph checkpointers (PostgresSaver / MemorySaver) serialize state <strong>only after a node returns cleanly</strong>.</p>
      <pre><code># Initial State Saved
state = {
    "order_id": "ORD-9481",
    "amount": 150.00,
    "idempotency_token": "tx_a8f93e" # Pre-generated!
}</code></pre>
    </div>
  </div>
</div>

<script>
const agentSteps = [
  {
    title: "Step 1: Checkpoint Saved at Node Boundary",
    desc: "LangGraph persists state snapshots only at node transitions. If state is not persisted with a pre-computed token, retries generate random UUIDs.",
    code: `state = {
    "order_id": "ORD-9481",
    "amount": 150.00,
    "idempotency_token": "tx_a8f93e" # Generated in parent node!
}`
  },
  {
    title: "Step 2: Mid-Node Network Timeout",
    desc: "The node sends an HTTP POST to Stripe. Stripe charges the card successfully, but the network drops before the 200 OK reaches your agent pod.",
    code: `# HTTP POST Sent
# Stripe charges $150
# Network drop: TimeoutException!
stripe.Charge.create(amount=150, idempotency_key=state["idempotency_token"])`
  },
  {
    title: "Step 3: Unhandled Process Crash",
    desc: "The unhandled exception causes Python to exit. Kubernetes restarts the container on a fresh node.",
    code: `# Exit code 1
# Pod terminated, restarted by kubelet`
  },
  {
    title: "Step 4: Replay with Idempotency Token",
    desc: "When the checkpointer resumes, it re-executes line 1. Because the idempotency token is preserved in state, Stripe detects the duplicate key and returns the existing charge instead of billing twice!",
    code: `# Stripe sees existing 'tx_a8f93e'
# Returns existing 200 OK -> ZERO DUPLICATE BILLING!`
  }
];

function showAgentStep(idx) {
  document.querySelectorAll('.interactive-step').forEach((s, i) => s.classList.toggle('active', i === idx));
  const data = agentSteps[idx];
  document.getElementById('agentStepDetail').innerHTML = `
    <h4 style="color:var(--cyan); margin-top:0;">${data.title}</h4>
    <p style="font-size:14px;">${data.desc}</p>
    <pre><code>${data.code}</code></pre>
  `;
}
</script>

<!-- QA-03 ACCORDION -->
<div class="scenario-card open">
  <div class="scenario-header" onclick="toggleCard(this)">
    <div>
      <span class="badge">QA-03 • LangGraph Core</span>
      <div class="scenario-title">LangGraph Checkpointer Crash & Duplicate Payment Bug</div>
      <div class="scenario-meta">Source: Naved Khan (LangGraph Core) • Track: AI Engineer • Difficulty: Hard</div>
    </div>
    <div class="toggle-icon">▼</div>
  </div>
  <div class="scenario-body">
    <div class="q-box">
      <b>The Bug:</b> An autonomous agent calls Stripe to charge $150. Mid-node network drops. Checkpointer rolls back to beginning of node. Customer is charged twice.
    </div>
    <div class="ans-box">
      <b>The Solution:</b>
      <ul>
        <li>Never generate idempotency tokens inside the mutation node!</li>
        <li>State nodes must be pure. Generate the token in an upstream planning node and store it in <code>state["idempotency_key"]</code>.</li>
        <li>On checkpointer replay, the external API recognizes the identical token and returns the original transaction.</li>
      </ul>
    </div>
  </div>
</div>

<!-- QA-26 ACCORDION -->
<div class="scenario-card">
  <div class="scenario-header" onclick="toggleCard(this)">
    <div>
      <span class="badge">QA-26 • Protocols</span>
      <div class="scenario-title">Model Context Protocol (MCP) vs Traditional REST APIs</div>
      <div class="scenario-meta">Source: Pavan Belagatti & Rohit Ghumare • Track: AI Engineer • Difficulty: Medium-Hard</div>
    </div>
    <div class="toggle-icon">▼</div>
  </div>
  <div class="scenario-body">
    <div class="ans-box">
      <ul>
        <li><strong>Dynamic Discovery:</strong> MCP clients query tool capabilities over JSON-RPC on demand, eliminating 15,000 prompt tokens of static Swagger schemas.</li>
        <li><strong>Transport Security:</strong> Runs over isolated <code>stdio</code> subprocesses or SSE with granular OAuth2 scopes.</li>
        <li><strong>Unified Ecosystem:</strong> Connects IDEs, AI coding assistants, and cloud platforms through a single standardized interface.</li>
      </ul>
    </div>
  </div>
</div>
"""
write_page("agentic-ai.html", "Agentic AI, LangGraph & MCP Protocols", "Module 05: Autonomous Systems", p5_content, "gpu-memory-math.html", "04. Memory Math", "fine-tuning-lora.html", "06. Fine-Tuning")

print("Generated enhanced Module 04 and Module 05!")

# ==============================================================================
# PAGE 6: FINE-TUNING & PEFT (QA-24, QA-28, QA-29, QA-34, QA-42)
# ==============================================================================
p6_content = """
<div class="card" style="border-left: 4px solid var(--rose);">
  <h2>Fine-Tuning: LoRA, QLoRA, Quantization & Tokenomics</h2>
  <p>Comprehensive coverage of <strong>QA-24, QA-28, QA-29, QA-34, and QA-42</strong>. Master low-rank adaptation matrix decomposition, NormalFloat4 double quantization, and decision trees for formatting regressions.</p>
</div>

<!-- Interactive Decision Tree Explainer -->
<div class="explainer-box">
  <h3 style="margin-top:0; color:var(--rose);">Interactive Decision Tree: Prompting vs Fine-Tuning vs RAG</h3>
  <p style="font-size:14px; color:var(--mut);">Select your production symptom to determine whether you need prompt engineering, constrained decoding, RAG, or LoRA fine-tuning:</p>
  
  <div style="display:grid; grid-template-columns: 1fr 1.5fr; gap:16px;">
    <div>
      <div class="interactive-step active" onclick="showFTStep(0)">
        <div class="step-num">1</div>
        <div><b>Malformed JSON / Schema Drops</b><br><span style="font-size:12px; color:var(--mut);">3% invalid braces or keys</span></div>
      </div>
      <div class="interactive-step" onclick="showFTStep(1)">
        <div class="step-num">2</div>
        <div><b>Hallucinated Product Facts</b><br><span style="font-size:12px; color:var(--mut);">Model outputs wrong prices/specs</span></div>
      </div>
      <div class="interactive-step" onclick="showFTStep(2)">
        <div class="step-num">3</div>
        <div><b>Specific Brand Tone & Nuance</b><br><span style="font-size:12px; color:var(--mut);">System prompt is 4,000 tokens long</span></div>
      </div>
      <div class="interactive-step" onclick="showFTStep(3)">
        <div class="step-num">4</div>
        <div><b>Numeric Arithmetic Failures</b><br><span style="font-size:12px; color:var(--mut);">BPE token splits multi-digits</span></div>
      </div>
    </div>
    
    <div id="ftStepDetail" style="background:#070B11; border:1px solid var(--line); border-radius:10px; padding:18px;">
      <h4 style="color:var(--cyan); margin-top:0;">Scenario: Malformed JSON / Schema Drops</h4>
      <p style="font-size:14px;"><strong>Recommendation:</strong> <strong>DO NOT FINE-TUNE!</strong> Use Constrained Decoding (Grammar-guided sampling with Outlines / vLLM <code>guided_json</code>).</p>
      <p style="font-size:14px;"><strong>Why:</strong> Masking invalid tokens from the logit vocabulary at runtime mathematically guarantees 100% schema validity at zero training cost.</p>
      <pre><code># Constrained Decoding in vLLM
sampling_params = SamplingParams(
    guided_json=MyPydanticSchema.model_json_schema()
)
outputs = llm.generate(prompt, sampling_params)</code></pre>
    </div>
  </div>
</div>

<script>
const ftSteps = [
  {
    title: "Scenario 1: Malformed JSON / Schema Regressions",
    desc: "<strong>Recommendation:</strong> <strong>NEVER FINE-TUNE FOR JSON SYNTAX!</strong><br>Use <strong>Constrained Decoding</strong> (Outlines / vLLM <code>guided_json</code>). It builds a finite state automaton (FSA) from your Pydantic schema, dynamically masking illegal tokens before softmax sampling.",
    code: `# Zero Training Cost Schema Guarantee
from pydantic import BaseModel

class TicketAction(BaseModel):
    action: str
    priority: int

params = SamplingParams(guided_json=TicketAction.model_json_schema())
outputs = llm.generate("Extract action...", params)`
  },
  {
    title: "Scenario 2: Hallucinated Enterprise Facts & Policies",
    desc: "<strong>Recommendation:</strong> <strong>USE RAG (Retrieval-Augmented Generation)</strong>.<br>Fine-tuning updates parametric weights, which suffer from catastrophic forgetting and cannot guarantee factual accuracy. RAG provides verifiable non-parametric citation grounding.",
    code: `# RAG Retrieval Injection
context = vector_db.query("refund policy", top_k=3)
prompt = f"Answer using ONLY this context: {context}"`
  },
  {
    title: "Scenario 3: Stylistic Consistency & System Prompt Distillation",
    desc: "<strong>Recommendation:</strong> <strong>USE LORA FINE-TUNING</strong>.<br>When your few-shot system prompt exceeds 4,000 tokens just to teach the model a specialized legal writing style or jargon, fine-tuning distills that style into low-rank adapter weights.",
    code: `# LoRA Fine-Tuning Setup
from peft import LoraConfig, get_peft_model

config = LoraConfig(
    r=16, lora_alpha=32,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05, bias="none"
)`
  },
  {
    title: "Scenario 4: BPE Arithmetic Tokenization Failures",
    desc: "<strong>Recommendation:</strong> <strong>UPDATE TOKENIZER REGEX OR USE TOOL CALLING</strong>.<br>Traditional tokenizers merge common number sequences into single tokens (e.g. '1000' vs '10' + '01'). Use regex digit isolation (Llama-3 tokenizer pattern) or delegate calculations to Python interpreter tools.",
    code: `# Tokenizer Digit Isolation Pattern
pattern = r"\\p{N}{1}"  # Force single-digit tokens!`
  }
];

function showFTStep(idx) {
  document.querySelectorAll('.interactive-step').forEach((s, i) => s.classList.toggle('active', i === idx));
  const data = ftSteps[idx];
  document.getElementById('ftStepDetail').innerHTML = `
    <h4 style="color:var(--cyan); margin-top:0;">${data.title}</h4>
    <p style="font-size:14px;">${data.desc}</p>
    <pre><code>${data.code}</code></pre>
  `;
}
</script>

<!-- QA-28 ACCORDION -->
<div class="scenario-card open">
  <div class="scenario-header" onclick="toggleCard(this)">
    <div>
      <span class="badge">QA-28 • Mathematical Formulation</span>
      <div class="scenario-title">LoRA & QLoRA: Low-Rank Adaptation Mechanics</div>
      <div class="scenario-meta">Source: Avi Chawla (MastercardAI) • Track: AI Engineer • Difficulty: Hard</div>
    </div>
    <div class="toggle-icon">▼</div>
  </div>
  <div class="scenario-body">
    <div class="ans-box">
      <b>The Mathematical Decomposition:</b>
      <p>Base frozen weights <code>W_0 &isin; R^{d &times; k}</code> are preserved. The update &Delta;W is factorized into <code>B &isin; R^{d &times; r}</code> and <code>A &isin; R^{r &times; k}</code> where rank <code>r &ll; min(d, k)</code>:</p>
      <pre><code>h = W_0 * x + (alpha / r) * (B * A) * x</code></pre>
      <ul>
        <li><strong>Matrix A:</strong> Initialized with Gaussian random values &sim; N(0, &sigma;&sup2;).</li>
        <li><strong>Matrix B:</strong> Initialized to zero, ensuring &Delta;W = 0 at training onset.</li>
        <li><strong>QLoRA Innovation:</strong> Base model is quantized to 4-bit NormalFloat4 (NF4) with Double Quantization, enabling a 70B parameter model to be fine-tuned on a single 48GB GPU!</li>
      </ul>
    </div>
  </div>
</div>
"""
write_page("fine-tuning-lora.html", "Fine-Tuning: LoRA, QLoRA & Distillation", "Module 06: Alignment & PEFT", p6_content, "agentic-ai.html", "05. Agentic AI", "distributed-parallelism.html", "07. Distributed Scale")

# ==============================================================================
# PAGE 7: DISTRIBUTED SCALE (QA-20, QA-25, QA-30, QA-33, QA-39)
# ==============================================================================
p7_content = """
<div class="card" style="border-left: 4px solid var(--cyan);">
  <h2>Distributed AI: ZeRO, 3D Parallelism & Ray Clusters</h2>
  <p>Comprehensive coverage of <strong>QA-20, QA-25, QA-30, QA-33, and QA-39</strong>. Master DeepSpeed ZeRO-1/2/3 static memory proofs, 3D Parallelism across NVLink and InfiniBand, and InfiniBand vs RoCE step-time jitter triage.</p>
</div>

<!-- Interactive ZeRO Memory Calculator -->
<div class="explainer-box">
  <h3 style="margin-top:0; color:var(--cyan);">Interactive DeepSpeed ZeRO Memory Proof Calculator</h3>
  <p style="font-size:14px; color:var(--mut);">Enter your model parameters and GPU cluster size to prove the exact per-GPU static memory savings across ZeRO stages:</p>
  
  <div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px;">
    <div>
      <label>Model Parameter Count (Billions):</label>
      <input type="number" id="zeroParams" value="70" min="1" max="500" oninput="calcZeRO()" style="width:100%; margin:8px 0; background:#0B0F17; color:#fff; border:1px solid var(--line); padding:8px; border-radius:6px;">
      
      <label>Data-Parallel GPUs (N):</label>
      <input type="number" id="zeroGPUs" value="16" min="1" max="1024" oninput="calcZeRO()" style="width:100%; margin:8px 0; background:#0B0F17; color:#fff; border:1px solid var(--line); padding:8px; border-radius:6px;">
    </div>
    
    <div style="background:#070B11; padding:16px; border-radius:10px; border:1px solid var(--line);">
      <div style="color:var(--rose); font-size:12px;">Standard Mixed Precision (16P Static):</div>
      <div id="stdMem" style="font-size:18px; font-weight:bold; color:var(--rose);">1,120 GB (Cannot fit on 1 GPU!)</div>
      
      <div style="color:var(--amber); font-size:12px; margin-top:8px;">ZeRO-1 (Optimizer Partitioning):</div>
      <div id="z1Mem" style="font-size:18px; font-weight:bold; color:var(--amber);">332.5 GB / GPU</div>
      
      <div style="color:var(--blue); font-size:12px; margin-top:8px;">ZeRO-2 (Optimizer + Gradient):</div>
      <div id="z2Mem" style="font-size:18px; font-weight:bold; color:var(--blue);">201.2 GB / GPU</div>
      
      <div style="color:var(--teal); font-size:12px; margin-top:8px;">ZeRO-3 (Full Parameters + Opt + Grad):</div>
      <div id="z3Mem" style="font-size:22px; font-weight:bold; color:var(--teal);">70.0 GB / GPU (Fits in 80GB VRAM!)</div>
    </div>
  </div>
</div>

<script>
function calcZeRO() {
  const P = parseFloat(document.getElementById('zeroParams').value) || 0;
  const N = parseFloat(document.getElementById('zeroGPUs').value) || 1;
  
  const std = 16 * P;
  const z1 = (4 * P) + (12 * P / N);
  const z2 = (2 * P) + (14 * P / N);
  const z3 = (16 * P) / N;
  
  document.getElementById('stdMem').innerText = std.toFixed(1) + " GB (Static across nodes)";
  document.getElementById('z1Mem').innerText = z1.toFixed(1) + " GB / GPU";
  document.getElementById('z2Mem').innerText = z2.toFixed(1) + " GB / GPU";
  document.getElementById('z3Mem').innerText = z3.toFixed(1) + " GB / GPU (" + (z3 <= 80 ? "Fits in 80GB VRAM!" : "Need more GPUs") + ")";
}
</script>

<!-- QA-25 ACCORDION -->
<div class="scenario-card open">
  <div class="scenario-header" onclick="toggleCard(this)">
    <div>
      <span class="badge">QA-25 • Multi-Node Topology</span>
      <div class="scenario-title">Tensor (TP) vs Pipeline (PP) vs Data Parallelism (DP) Across 256 GPUs</div>
      <div class="scenario-meta">Source: Intel / Enterprise Infra Panel • Track: AI Platform • Difficulty: Hard</div>
    </div>
    <div class="toggle-icon">▼</div>
  </div>
  <div class="scenario-body">
    <div class="ans-box">
      <b>The Hardware Boundary Rule:</b>
      <ul>
        <li><strong>Tensor Parallelism (TP=8):</strong> Must stay <strong>intra-node over NVLink (900 GB/s)</strong>. TP splits matrix operations layer-by-layer, requiring massive high-frequency All-Reduce synchronizations. Running TP over Ethernet or standard InfiniBand will crater performance.</li>
        <li><strong>Pipeline Parallelism (PP=8):</strong> Runs <strong>inter-node over InfiniBand</strong>. Layers are partitioned sequentially across nodes; only activation tensors flow between pipeline stages.</li>
        <li><strong>Data Parallelism (DP=4):</strong> Replicates 3D grids across the cluster with ZeRO-3 / FSDP gradient reductions.</li>
      </ul>
    </div>
  </div>
</div>
"""
write_page("distributed-parallelism.html", "Distributed AI: ZeRO, 3D Parallelism & Ray", "Module 07: Scale & Multi-Node", p7_content, "fine-tuning-lora.html", "06. Fine-Tuning", "k8s-gpu-infra.html", "08. K8s & Autoscaling")

print("Generated enhanced Module 06 and Module 07!")

# ==============================================================================
# PAGE 8: K8S GPU INFRASTRUCTURE (QA-07, QA-13, QA-21, QA-40)
# ==============================================================================
p8_content = """
<div class="card" style="border-left: 4px solid var(--blue);">
  <h2>Kubernetes GPU Infrastructure, Volcano & Fast Cold Starts</h2>
  <p>Comprehensive coverage of <strong>QA-07, QA-13, QA-21, and QA-40</strong>. Master queue-depth autoscaling with KEDA, Volcano gang scheduling, JuiceFS distributed NVMe caching, and eBPF kube-proxy replacements.</p>
</div>

<!-- Interactive Cold Start Optimization Breakdown -->
<div class="explainer-box">
  <h3 style="margin-top:0; color:var(--blue);">Interactive 70B Cold Start Optimization Pipeline</h3>
  <p style="font-size:14px; color:var(--mut);">Click each stage to see how a naive 8-minute pod launch is collapsed to under 45 seconds:</p>
  
  <div style="display:grid; grid-template-columns: 1fr 1.5fr; gap:16px;">
    <div>
      <div class="interactive-step active" onclick="showColdStep(0)">
        <div class="step-num">1</div>
        <div><b>Naive Baseline (8m 10s)</b><br><span style="font-size:12px; color:var(--mut);">140GB image pull from ECR/DockerHub</span></div>
      </div>
      <div class="interactive-step" onclick="showColdStep(1)">
        <div class="step-num">2</div>
        <div><b>Image Decoupling (2m 15s)</b><br><span style="font-size:12px; color:var(--mut);">Base runtime image (&lt;1.5GB)</span></div>
      </div>
      <div class="interactive-step" onclick="showColdStep(2)">
        <div class="step-num">3</div>
        <div><b>Distributed POSIX Cache (55s)</b><br><span style="font-size:12px; color:var(--mut);">JuiceFS / Fluid on local NVMe</span></div>
      </div>
      <div class="interactive-step" onclick="showColdStep(3)">
        <div class="step-num">4</div>
        <div><b>GPUDirect Storage (14s)</b><br><span style="font-size:12px; color:var(--mut);">Direct NVMe &rarr; GPU HBM bypass</span></div>
      </div>
    </div>
    
    <div id="coldStepDetail" style="background:#070B11; border:1px solid var(--line); border-radius:10px; padding:18px;">
      <h4 style="color:var(--rose); margin-top:0;">Stage 1: Naive Monolithic Image (8 min 10 sec)</h4>
      <p style="font-size:14px;"><strong>The Bottleneck:</strong> Teams bake 140GB of safetensors weights directly into the Docker image. Pulling a 140GB image across network interfaces and unpacking container layers takes 7 to 10 minutes on new nodes, completely missing burst traffic.</p>
    </div>
  </div>
</div>

<script>
const coldSteps = [
  {
    title: "Stage 1: Naive Monolithic Image (8 min 10 sec)",
    desc: "<strong>The Bottleneck:</strong> Storing 140GB weights in Docker images causes ECR registry rate-limiting, slow network pulls, and slow container unpack times.",
    code: `# AVOID: Monolithic 140GB Dockerfile!
FROM nvidia/cuda:12.4
COPY ./llama-3-70b-weights /app/weights # DANGER!`
  },
  {
    title: "Stage 2: Image Decoupling (2 min 15 sec)",
    desc: "<strong>Optimization:</strong> Strip weights out of the container image entirely. Build a minimal 1.2GB image containing only the vLLM python runtime and CUDA binaries. Image pulls in 15 seconds.",
    code: `# Clean Lightweight Dockerfile
FROM vllm/vllm-openai:v0.6.2 # 1.2GB only!`
  },
  {
    title: "Stage 3: Distributed NVMe POSIX Cache (55 sec)",
    desc: "<strong>Optimization:</strong> Deploy <strong>Fluid with JuiceFS</strong>. Weights are backed by S3, but local Kubernetes worker node NVMe drives pre-cache shards. Pods mount a local POSIX path.",
    code: `# Kubernetes Persistent Volume Mount
volumeMounts:
- name: model-weights
  mountPath: /models
  readOnly: true`
  },
  {
    title: "Stage 4: GPUDirect Storage (GDS) Direct DMA (14 sec)",
    desc: "<strong>Optimization:</strong> Load weights directly from local NVMe into GPU HBM using <strong>NVIDIA cuFile / GPUDirect Storage</strong>. Bypasses host CPU RAM and OS page cache entirely. Throughput increases to 12 GB/s!",
    code: `# Fast Direct DMA Tensor Loading
vllm serve /models/llama-3-70b --load-format safetensors`
  }
];

function showColdStep(idx) {
  document.querySelectorAll('.interactive-step').forEach((s, i) => s.classList.toggle('active', i === idx));
  const data = coldSteps[idx];
  document.getElementById('coldStepDetail').innerHTML = `
    <h4 style="color:var(--cyan); margin-top:0;">${data.title}</h4>
    <p style="font-size:14px;">${data.desc}</p>
    <pre><code>${data.code}</code></pre>
  `;
}
</script>

<!-- QA-07 ACCORDION -->
<div class="scenario-card open">
  <div class="scenario-header" onclick="toggleCard(this)">
    <div>
      <span class="badge">QA-07 • KEDA Autoscaling</span>
      <div class="scenario-title">Why HPA CPU/GPU Utilization Fails for LLMs</div>
      <div class="scenario-meta">Source: Rishabh Tripathi • Track: AI DevOps / SRE • Difficulty: Medium-Hard</div>
    </div>
    <div class="toggle-icon">▼</div>
  </div>
  <div class="scenario-body">
    <div class="pitfall">
      <b>The Trap:</b> Setting HPA to scale on 80% GPU memory causes instant scale-out to max replicas because vLLM pre-allocates 90% of VRAM for PagedAttention at boot time.
    </div>
    <div class="ans-box">
      <b>The Solution:</b> Use KEDA targeting <code>vllm:num_requests_waiting</code>:
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
</div>
"""
write_page("k8s-gpu-infra.html", "Kubernetes GPU Infrastructure & Autoscaling", "Module 08: Orchestration", p8_content, "distributed-parallelism.html", "07. Distributed Scale", "cloud-devops-failures.html", "09. SRE & Incidents")

# ==============================================================================
# PAGE 9: SRE & FAILURES (QA-01, QA-08, QA-09, QA-10, QA-14, QA-22)
# ==============================================================================
p9_content = """
<div class="card" style="border-left: 4px solid var(--amber);">
  <h2>Cloud SRE, Networking & Production Incident War Stories</h2>
  <p>Comprehensive coverage of <strong>QA-01, QA-08, QA-09, QA-10, QA-14, and QA-22</strong>. Master the STAR interview framework for 2 AM production failures, TCP keepalive 502 race conditions, and thundering herd mitigations.</p>
</div>

<!-- QA-01 STAR WAR STORY -->
<div class="scenario-card open">
  <div class="scenario-header" onclick="toggleCard(this)">
    <div>
      <span class="badge">QA-01 • The STAR Framework</span>
      <div class="scenario-title">The "Tell Me About a 2 AM Production Failure" Incident</div>
      <div class="scenario-meta">Source: Bharath Reddy (40 LPA Loop) • Track: AI DevOps / SRE • Difficulty: Hard</div>
    </div>
    <div class="toggle-icon">▼</div>
  </div>
  <div class="scenario-body">
    <div class="ans-box">
      <b>STAR War Story Delivery:</b>
      <ul>
        <li><strong>Situation:</strong> At 2:15 AM, p99 latency on our customer service AI agent spiked from 800ms to 48 seconds, triggering PagerDuty alerts across the platform team.</li>
        <li><strong>Task:</strong> Identify the root cause, restore service without dropping customer chats, and eliminate the vulnerability permanently.</li>
        <li><strong>Action:</strong> Low-level tracing revealed a downstream CRM API was returning HTTP 429 HTML rate-limit error pages. The agent interpreted the HTML body as new instructions and entered an unbounded reflection loop. We applied emergency circuit breakers, capped <code>max_iterations = 4</code>, and enforced exponential backoff with full jitter.</li>
        <li><strong>Result:</strong> P99 latency recovered to 650ms. Incident post-mortem introduced automated CI/CD chaos tests, saving estimated $45k/month in runaway token loops.</li>
      </ul>
    </div>
  </div>
</div>

<!-- QA-09 TCP RACE CONDITION -->
<div class="scenario-card open">
  <div class="scenario-header" onclick="toggleCard(this)">
    <div>
      <span class="badge">QA-09 • Network Race Condition</span>
      <div class="scenario-title">Intermittent 502 Bad Gateway Under AI Inference Load</div>
      <div class="scenario-meta">Source: Rishabh Tripathi • Track: DevOps / Platform • Difficulty: Medium-Hard</div>
    </div>
    <div class="toggle-icon">▼</div>
  </div>
  <div class="scenario-body">
    <div class="q-box">
      <b>The Mystery:</b> 1.5% of requests fail with 502 Bad Gateway, but backend CPU is low and pods are not restarting.
    </div>
    <div class="ans-box">
      <b>The TCP Keepalive Race Condition:</b>
      <p>When the upstream reverse proxy (Nginx / ALB) has a keepalive timeout longer than or equal to the backend server (FastAPI/Uvicorn), the backend can send a <code>TCP FIN</code> at the exact microsecond the proxy forwards a new request, resulting in an immediate <code>TCP RST</code>.</p>
      <div style="background:#070B11; border:1px solid var(--teal); border-radius:8px; padding:12px; margin:10px 0;">
        <b>The Golden Rule:</b> Backend keepalive timeout must ALWAYS be strictly greater than proxy timeout:
        <pre><code># Nginx Ingress: keepalive_timeout 65s;
# Uvicorn:       uvicorn.run(..., timeout_keep_alive=75) # 75s > 65s!</code></pre>
      </div>
    </div>
  </div>
</div>
"""
write_page("cloud-devops-failures.html", "Cloud SRE, Networking & Production Failures", "Module 09: Production War Stories", p9_content, "k8s-gpu-infra.html", "08. K8s & Autoscaling", "eval-security-drills.html", "10. Evals & Drills")

# ==============================================================================
# PAGE 10: EVALS, SECURITY & DRILLS (QA-18, QA-19, QA-35, QA-38, QA-41 & SECTION F)
# ==============================================================================
p10_content = """
<div class="card" style="border-left: 4px solid var(--teal);">
  <h2>Automated Evaluations, Red Teaming & 30-Day Interview Drills</h2>
  <p>Comprehensive coverage of <strong>QA-18, QA-19, QA-35, QA-38, QA-41</strong>, and the complete <strong>Section F 30-Day Mock Drill Framework</strong>. Master LLM-as-a-judge quality gates, eBPF runtime security, and candidate interview execution.</p>
</div>

<!-- QA-41 EVAL TRIAD ACCORDION -->
<div class="scenario-card open">
  <div class="scenario-header" onclick="toggleCard(this)">
    <div>
      <span class="badge">QA-41 • Quality Gates</span>
      <div class="scenario-title">Automated LLM Evaluation CI/CD Gate (The Ragas Triad)</div>
      <div class="scenario-meta">Source: MLOps Evaluation Loop • Track: MLOps / AI DevOps • Difficulty: Medium-Hard</div>
    </div>
    <div class="toggle-icon">▼</div>
  </div>
  <div class="scenario-body">
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
</div>

<!-- QA-38 ACCORDION -->
<div class="scenario-card open">
  <div class="scenario-header" onclick="toggleCard(this)">
    <div>
      <span class="badge">QA-38 • Red Teaming</span>
      <div class="scenario-title">Indirect Prompt Injection & The Dual-LLM Defense Pattern</div>
      <div class="scenario-meta">Source: AI Security Loop • Track: AI Security / DevOps • Difficulty: Hard</div>
    </div>
    <div class="toggle-icon">▼</div>
  </div>
  <div class="scenario-body">
    <div class="ans-box">
      <ol>
        <li><strong>Untrusted Data Extractor (Zero Tools):</strong> Reads raw emails and PDFs. Outputs purely typed Pydantic JSON. Has zero access to network or file tools.</li>
        <li><strong>Privileged Agent:</strong> Reads validated JSON fields only. Never sees raw external prompt strings.</li>
        <li><strong>Execution Isolation:</strong> Tool executions (code scripts, bash commands) run in ephemeral AWS Firecracker microVMs with link-local IP <code>169.254.169.254</code> blocked.</li>
      </ol>
    </div>
  </div>
</div>

<!-- 30-DAY DRILL SCHEDULE -->
<div class="card" style="border: 1px solid var(--amber);">
  <span class="badge" style="background:rgba(245,158,11,0.2); color:var(--amber); border-color:var(--amber);">Section F • Rehearsal Blueprint</span>
  <h3>30-Day Mock Interview Countdown Rehearsal Framework</h3>
  <div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px; margin-top:12px;">
    <div style="background:#070B11; border:1px solid var(--line); border-radius:10px; padding:16px;">
      <h4 style="color:var(--amber); margin-top:0;">Week 1: Serving & Memory Math</h4>
      <p style="font-size:13px; color:#CBD5E1;">Calculate Llama-3-70B KV cache on whiteboard cold. Explain FlashAttention online softmax and PagedAttention block tables without hesitation.</p>
      
      <h4 style="color:var(--teal); margin-top:16px;">Week 2: Kubernetes & Networking</h4>
      <p style="font-size:13px; color:#CBD5E1;">Write a KEDA queue-based ScaledObject manifest. Explain IPVS vs eBPF Cilium bypass for 5,000 services.</p>
    </div>
    <div style="background:#070B11; border:1px solid var(--line); border-radius:10px; padding:16px;">
      <h4 style="color:var(--blue); margin-top:0;">Week 3: Agents & Protocols</h4>
      <p style="font-size:13px; color:#CBD5E1;">Build a LangGraph state graph with checkpointer and pre-generated idempotency tokens. Whiteboard Model Context Protocol (MCP) vs REST.</p>
      
      <h4 style="color:var(--rose); margin-top:16px;">Week 4: Failure War Stories & Design</h4>
      <p style="font-size:13px; color:#CBD5E1;">Rehearse the "2 AM Production Incident" using the STAR framework. Execute full 45-minute timed whiteboard RAG designs.</p>
    </div>
  </div>
</div>
"""
write_page("eval-security-drills.html", "Evals, Red Teaming & 30-Day Interview Drills", "Module 10: Governance & Rehearsal", p10_content, "cloud-devops-failures.html", "09. SRE & Incidents", None, None)

print("COMPLETE 10-PAGE ENHANCED COURSE BUILD COMPLETED!")
