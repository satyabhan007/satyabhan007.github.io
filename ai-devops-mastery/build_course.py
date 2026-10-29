#!/usr/bin/env python3
"""
Comprehensive 10-Page Interactive AI Engineer & DevOps Course Builder
Generates a responsive static site covering all 45 Q&A scenarios with:
- Connected interactive SVG diagrams
- Live memory math / calculator playgrounds
- STAR incident war story debriefs
- Interactive tabs, filters, and quizzes
"""

import os
import json

BASE_DIR = "/home/satya/Downloads/SATYA/satyabhan007.github.io/ai-devops-mastery"

pages = [
    {
        "file": "index.html",
        "num": "01",
        "title": "Course Overview & 45 Scenario Matrix",
        "badge": "Module 01: Master Map",
        "desc": "Executive orientation, curriculum roadmap, and interactive filtering matrix across all 45 interview scenarios from OpenAI, Google, NVIDIA, and Netflix loops.",
        "prev": None,
        "next": "rag-search.html"
    },
    {
        "file": "rag-search.html",
        "num": "02",
        "title": "Production RAG, Vector DBs & GraphRAG",
        "badge": "Module 02: Retrieval & Search",
        "desc": "Hybrid RRF retrieval, HNSW vs IVF-PQ 50M vector memory math, Cross-Encoders, GraphRAG with Leiden community detection, and the 5-point failure triage matrix.",
        "prev": "index.html",
        "next": "llm-serving.html"
    },
    {
        "file": "llm-serving.html",
        "num": "03",
        "title": "LLM Serving: vLLM, PagedAttention & Kernels",
        "badge": "Module 03: Serving Engines",
        "desc": "Continuous batching internals, FlashAttention Online Softmax tiling, Speculative Decoding asymmetric speeds, Prefill-Decode (PD) Disaggregation, and Triton BLS.",
        "prev": "rag-search.html",
        "next": "gpu-memory-math.html"
    },
    {
        "file": "gpu-memory-math.html",
        "num": "04",
        "title": "GPU Architecture & VRAM Memory Math",
        "badge": "Module 04: Hardware & Math",
        "desc": "Llama-3-70B GQA KV-Cache sizing formula, why 100% GPU utilization is deceptive (Roofline model), FP8 quantization, and cluster capacity budgeting.",
        "prev": "llm-serving.html",
        "next": "agentic-ai.html"
    },
    {
        "file": "agentic-ai.html",
        "num": "05",
        "title": "Agentic AI, LangGraph & MCP Protocols",
        "badge": "Module 05: Autonomous Systems",
        "desc": "LangGraph checkpointers & duplicate charge bugs, Model Context Protocol (MCP) vs REST, tool loop fingerprinting, and zero-downtime agent state migration.",
        "prev": "gpu-memory-math.html",
        "next": "fine-tuning-lora.html"
    },
    {
        "file": "fine-tuning-lora.html",
        "num": "06",
        "title": "Fine-Tuning: LoRA, QLoRA & Distillation",
        "badge": "Module 06: Alignment & PEFT",
        "desc": "Rank r << d LoRA math, NormalFloat4 (NF4) double quantization, synthetic data evolution loops, and the Prompting vs Fine-Tuning decision tree.",
        "prev": "agentic-ai.html",
        "next": "distributed-parallelism.html"
    },
    {
        "file": "distributed-parallelism.html",
        "num": "07",
        "title": "Distributed AI: ZeRO, 3D Parallelism & Ray",
        "badge": "Module 07: Scale & Multi-Node",
        "desc": "DeepSpeed ZeRO-1/2/3 static memory proofs, 3D Parallelism (TP on NVLink vs PP on InfiniBand vs DP), and Ray Serve high-throughput actor pools.",
        "prev": "fine-tuning-lora.html",
        "next": "k8s-gpu-infra.html"
    },
    {
        "file": "k8s-gpu-infra.html",
        "num": "08",
        "title": "Kubernetes GPU Infrastructure & Autoscaling",
        "badge": "Module 08: Orchestration",
        "desc": "Why HPA fails on LLMs, KEDA queue-based scaling, Volcano all-or-nothing gang scheduling, dropping 70B cold starts to <45s, and IPVS/eBPF kube-proxy fixes.",
        "prev": "distributed-parallelism.html",
        "next": "cloud-devops-failures.html"
    },
    {
        "file": "cloud-devops-failures.html",
        "num": "09",
        "title": "Cloud SRE, Networking & Production Failures",
        "badge": "Module 09: Production War Stories",
        "desc": "The 'Tell me about a 2 AM failure' STAR framework, TCP keepalive 502 race conditions, 10 AM thundering herds with full jitter, and AWS OIDC triage.",
        "prev": "k8s-gpu-infra.html",
        "next": "eval-security-drills.html"
    },
    {
        "file": "eval-security-drills.html",
        "num": "10",
        "title": "Evals, Red Teaming & 30-Day Interview Drills",
        "badge": "Module 10: Governance & Rehearsal",
        "desc": "Automated CI/CD PR evaluation gates (Ragas Triad), Indirect Prompt Injection dual-LLM defense, eBPF Falco security, and the 30-Day candidate mock drill.",
        "prev": "cloud-devops-failures.html",
        "next": None
    }
]

print(f"Plan initialized for {len(pages)} pages.")
