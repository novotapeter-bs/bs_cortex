<div align="center">

# Blue Synergy Cortex (v3.0) 

> **Long-term, drift-free cognitive memory engine for AI Agents, Cursor IDE, and Claude Desktop via Model Context Protocol (MCP).**

[![MCP Compatible](https://img.shields.io/badge/MCP-FastMCP%20SSE-blue.svg)](https://modelcontextprotocol.io/)
[![Latency](https://img.shields.io/badge/Recall%20Latency-%3C65ms-green.svg)]()
[![Architecture](https://img.shields.io/badge/Tri--Stream-Stateless-orange.svg)]()
[![M8ven Score](https://m8ven.ai/badge/mcp/novotapeter-bs/bs_cortex)](https://m8ven.ai/mcp/novotapeter-bs/bs_cortex)

> **Deep Dive:** Want to understand our tri-stream model, autonomous rest cycles, and dynamic invariant guards?  
> Read the full [Engineering Whitepaper & Architecture Model (ARCHITECTURE.md)](./ARCHITECTURE.md).

---

### Stop AI Amnesia & Specification Drift
</div>
Most memory systems treat everything as fluid vector soup—causing agents to hallucinate, forget strict technical requirements, or confuse user preferences with code specs.

**Blue Synergy Cortex** implements an enterprise-grade **Tri-Stream Architecture** backed by transactional PostgreSQL and enterprise knowledge graph architecture:
1. **User Stream:** Generalizes conversational habits and user preferences over time.
2. **Identity Stream:** Deterministic guardrails and behavioral axioms that prevent sycophancy.
3. **Knowledge Stream (Living Specs):** Exact architecture specifications, hardware limits, and system parameters organized into an authoritative **Universal Domain Ontology**. This stream is **protected against lossy compression, semantic decay, and accidental drift**.


---

### Quickstart (1 Minute Setup)

**API Key Required:** Blue Synergy Cortex is a fully hosted, zero-maintenance cognitive cloud engine. You need an active API key to connect your client.
 
🔑 **[Get your 21-Day Free Trial Key here](https://cortex.bluesynergy.io)**  
*(Instant activation, no credit card required, includes 500 graph nodes & up to 3 agents).*

---

### Step 1: Get your API Key
1. Go to [cortex.bluesynergy.io](https://cortex.bluesynergy.io) and generate your trial key.
2. Your key will look like: `ctx_live_xxxxxxxxxxxxxxxxxxxxxx`.

---
### Step 2: Connect your AI agent

### A. Cursor IDE Integration

1. Open **Cursor Settings** (`Ctrl+Shift+J` or `Cmd+Shift+J`).
2. Navigate to **Features** -> **MCP Servers** -> **Add new MCP server**.
3. Configure as follows:
   * **Name:** `cortex-memory`
   * **Type:** `sse`
   * **URL:** `https://cortex.bluesynergy.io/v1/mcp/sse?api_key=YOUR_API_KEY`
4. Save. Your Cursor Composer and Agent now have permanent recall across restarts!

---

### B. Claude Desktop Integration

Edit your configuration file:
* **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
* **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

Add the Cortex remote configuration (Claude Desktop):

```json
{
  "mcpServers": {
    "cortex": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://cortex.bluesynergy.io/v1/mcp/sse",
        "--header",
        "Authorization: Bearer YOUR_API_KEY"
      ]
    }
  }
}
```
Restart Claude Desktop

---
### C. Other MCP Clients (Windsurf, VS Code Cline, Roo Code, Zed, Cursor)

Use the SSE endpoint directly in your tool's MCP configuration:

```json
{
  "mcpServers": {
    "cortex": {
      "url": "https://cortex.bluesynergy.io/v1/mcp/sse?api_key=ctx_live_..."
    }
  }
}
```

---
### D. Custom Agents & REST API (LangChain, CrewAI, AutoGen, OpenAI Custom GPTs, LlamaIndex, n8n)

Integrate Cortex directly into your custom pipelines via our sub-65ms REST endpoints:
* **Interactive API Documentation (Swagger UI):** [https://cortex.bluesynergy.io/docs](https://cortex.bluesynergy.io/docs)
* **OpenAPI Schema:** [https://cortex.bluesynergy.io/openapi.json](https://cortex.bluesynergy.io/openapi.json)

**Example: Querying Context (cURL)**
```bash
curl -X POST https://cortex.bluesynergy.io/v1/recall \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "System database requirements",
    "user_id": "developer",
    "agent_id": "backend_agent"
  }'
```

---

### Available MCP Tools & Lifecycle Architecture

Cortex is not a passive key-value store; it is an active cognitive operating system with strict governance boundaries. Understanding **when** and **why** to call each tool ensures high-fidelity memory consolidation.

---

#### The Standard Agent Turn Cycle
For every user turn, your agent should inherently follow this golden loop:
1. **At turn start:** Call `cortex_recall` to fetch ground-truth context (User Bio + Active Project Specs + Graph Relations).
2. **Generate response:** Formulate the answer grounded in the retrieved memory.
3. **At turn end:** Call `cortex_ingest_turn` to send the turn to the asynchronous ingestion buffer.

---

#### Detailed Tool Reference

| Tool Name | Type | When to Call | System Behavior |
| :--- | :--- | :--- | :--- |
| `cortex_recall` | Query | **Before answering** the user (mandatory for full context awareness). | Sub-65ms hybrid vector and topological graph search. Automatically injects verified user profile traits, active project specifications, and cross-entity relationships directly into the prompt context. |
| `cortex_ingest_turn` | Ingestion | **Immediately after answering** every conversational turn. | Asynchronously ingests the full conversational turn. The Memory Firewall filters dialogue noise, learns communication preferences, and stages technical facts for scheduled consolidation. |
| `cortex_store_memory` | Write | For **explicit system constraints, hard business rules, and technical decisions** that must be guaranteed. | Curated persistent write. **Safety Gate:** If `project_id` is not yet authorized by the user, facts are safely staged in the general memory pool (`general`) to prevent project pollution. |
| `cortex_get_project_spec` | Inspection | When you need the **complete Living Canonical Specification** of a project. | Deterministically retrieves the verified, unified specification (Living Document) of the project. **Note:** Returns only authorized and consolidated specifications—not unorganized scratchpad notes. |
| `cortex_manage_draft` | Governance | When a new product or domain is proposed and **awaits explicit user authorization**. | Approves quarantined project drafts (`draft_*`) into active production specifications, or permanently purges rejected concepts. Promotes staged facts from `general` into dedicated project scope. |
| `cortex_triage_general` | Maintenance | When the unstructured staging pool (`general`) accumulates multi-project notes. | Semantic clustering engine that organizes notes in `general`, pairs them with corresponding projects, and executes workspace compaction. |

---
### Project Governance & Lifecycle

To prevent memory fragmentation and unauthorized project sprawl, Cortex treats memory with strict governance boundaries:

```text
[Incoming Note / Message]
           │
           ▼
   Is Project Authorized?
        ├── NO  ──► Staged in General Pool ('general')
        │                 │
        │                 ▼
        │          Awaits Approval via `cortex_manage_draft`
        │                 │
        └── YES ◄─────────┘
           │
           ▼
[Asynchronous Consolidation Cycle]
           │
           ▼
[Active Living Specification & Knowledge Topology]
```
---
###  Why is my project_spec empty after storing notes?

Cortex enforces a Human-in-the-Loop policy. If a project_id has not yet been explicitly authorized by the user, incoming facts are safely staged in the general memory pool to prevent polluting active workspaces.
Once the project is approved (via cortex_manage_draft or explicit creation), the nocturnal consolidation engine automatically synthesizes these staged notes into the official Living Specification (cortex_get_project_spec).

---

### Core Architecture Highlights

* **Sub-65ms Zero-LLM Recall:** Direct high-performance vector and topological graph matching—completely bypassing slow, non-deterministic runtime LLM keyword extractors.
* **Dual-Zone Fast-Append:** Instant raw fact capture (< 20ms) into an inbox staging zone, followed by scheduled asynchronous consolidation into an immutable, unified Living Specification.
* **Semantic Invariant Guard:** Algorithmic verification gate that enforces factual density and continuity, mathematically preventing the truncation or loss of critical parameters during re-indexing.
* **Immunity Shield:** Operational errors, tool crashes, transient hallucinations, and conversational apologies are filtered out by design and never committed to long-term memory.

---

## Support & Feedback

Encountered an issue or have a feature suggestion?

* **Bug Reports & Issues:** [Open an Issue](https://github.com/novotapeter-bs/bs_cortex/issues)
* **Status & Portal:** [cortex.bluesynergy.io](https://cortex.bluesynergy.io)
* For a detailed theoretical and operational breakdown, see our [Engineering Whitepaper (ARCHITECTURE.md)](./ARCHITECTURE.md).
