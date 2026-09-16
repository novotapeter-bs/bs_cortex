# bs_cortex
Asynchronous cognitive memory engine for AI agents. Sub-65ms Zero-LLM recall, anti-drift Living Specs, and nocturnal graph consolidation via MCP. (PostgreSQL + Neo4j)

<div align="center">

# Blue Synergy CORTEX
### Sovereign Cognitive Operating System for AI Agents

[![Version](https://img.shields.io/badge/version-v2.3%20Sovereign-0ea5e9.svg?style=flat-square)](https://cortex.bluesynergy.io)
[![Recall Latency](https://img.shields.io/badge/recall%20latency-%3C%2065ms%20(Zero--LLM)-10b981.svg?style=flat-square)](https://bluesynergy.io)
[![Protocol](https://img.shields.io/badge/protocol-FastMCP%20Native-6366f1.svg?style=flat-square)](https://modelcontextprotocol.io)
[![Compliance](https://img.shields.io/badge/compliance-EU%20AI%20Act%20%7C%20ISO%2042001-emerald.svg?style=flat-square)](https://bluesynergy.io/#compliance)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21445392-gray.svg?style=flat-square)](https://doi.org/10.5281/zenodo.21445392)

<p align="center">
  <strong>AI memory is not a note dumping ground.<br>
  It is an adaptive cognitive layer with multi-tier nocturnal synthesis.</strong>
</p>

[Quickstart](#quickstart) • [Tri-Stream Architecture](#tri-stream-architecture) • [Benchmarks](#telemetry--benchmarks) • [Compliance](#compliance--governance) • [Get Free Token](https://bluesynergy.io)

</div>

---

## Overview

Most long-term agent memory implementations act as passive vector garbage dumps. They flood model context windows with contradictory historical noise, suffer from multi-second retrieval latency, and degrade into echo chambers through unchecked sycophancy.

**Blue Synergy CORTEX v2.3** is an asynchronous, stateless, multi-tenant cognitive engine engineered for **Claude Desktop, Cursor IDE, Windsurf, and sovereign autonomous agents**. It decouples real-time dialogue from deep background consolidation, ensuring your agents maintain rigorous technical precision without semantic drift.


---

## Key Differentiators

| Capability | Conventional Vector Memory (Mem0, Naive RAG) | Blue Synergy CORTEX v2.3 |
| :--- | :--- | :--- |
| **Retrieval Latency** | 1.5 s – 4.0 s (Blocking LLM call on read) | **< 65 ms (Deterministic Zero-LLM Graph Recall)** |
| **Project Specs** | Lossy fluid text chunks; parameters drift | **Living Canonical Documents with Invariant Key Matrix** |
| **Drift & Sycophancy** | Agrees with user biases; persona drifts | **Deterministic Core Axioms & Actor-Critic Identity Audit** |
| **Memory Cleanup** | Unbounded accumulation or brute-force TTL | **Biological Ebbinghaus Phagocytosis & Nocturnal Consolidation** |
| **Protocol** | Custom proprietary SDKs | **Native FastMCP (Model Context Protocol) via SSE** |
| **Sovereignty** | Third-party sub-processors; external clouds | **100% Private Stack (PostgreSQL + Neo4j + Local GPU)** |

---

## Tri-Stream Architecture

Cortex enforces strict functional and biological boundaries across three memory flows:

1. **User Stream (`UserMemoryEngine`):** Biographical and relational history. Progressively synthesized into an evolving *Master Biography* without polluting technical parameters.
2. **Identity Stream (`AgentIdentityEngine`):** Self-reflection, communication style, and guardrails. Governed by a deterministic auditor at $T=0.0$ enforcing immutable *Core Axioms* (anti-sycophancy, physical realism).
3. **Knowledge Stream (`KnowledgeWorker` — V2.3):** Technical architectural specifications, database schemas, and mathematical invariants. Maintained via *Living Canonical Documents* protected against lossy compression and semantic drift.

---

## Quickstart

### 1. Connect via Claude Desktop (Zero-Install MCP)

Add the following block to your `claude_desktop_config.json`:

* **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
* **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "cortex": {
      "url": "https://api.bluesynergy.io/v1/mcp/sse",
      "headers": {
        "Authorization": "Bearer ctx_live_your_token_here"
      }
    }
  }
}


[ RETRIEVAL LATENCY ]  < 65 ms      (Topological edge traversal directly in Neo4j)
[ REANIMATION INDEX ]  33.2 %       (Ebbinghaus reactivation of dormant relevant edges)
[ IDENTITY DRIFT    ]  4.5 %        (Constrained within mathematical threshold <= 25.0%)
[ FAITHFULNESS      ]  98 %         (DeepEval evaluation vs grounded indexed context)
[ HALLUCINATION RATE]  2 %          (Significantly below industry regulatory thresholds)
