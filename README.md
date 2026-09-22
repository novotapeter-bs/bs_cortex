<div align="center">

# Blue Synergy Cortex (v3.0) 

> **Long-term, drift-free cognitive memory engine for AI Agents, Cursor IDE, and Claude Desktop via Model Context Protocol (MCP).**

[![MCP Compatible](https://img.shields.io/badge/MCP-FastMCP%20SSE-blue.svg)](https://modelcontextprotocol.io/)
[![Latency](https://img.shields.io/badge/Recall%20Latency-%3C65ms-green.svg)]()
[![Architecture](https://img.shields.io/badge/Tri--Stream-Stateless-orange.svg)]()

---

### Stop AI Amnesia & Specification Drift
</div>
Most memory systems treat everything as fluid vector soup—causing agents to hallucinate, forget strict technical requirements, or confuse user preferences with code specs.

**Blue Synergy Cortex** implements an enterprise-grade **Tri-Stream Architecture** backed by transactional PostgreSQL and Neo4j:
1. **User Stream:** Generalizes conversational habits and user preferences over time.
2. **Identity Stream:** Deterministic guardrails and behavioral axioms that prevent sycophancy.
3. **Knowledge Stream (Living Specs):** Exact architecture specifications, hardware limits, and system parameters organized into an immutable **Universal Scientific Ontology**. This stream is **protected against lossy compression, semantic decay, and accidental drift**.


---

### Quickstart (1 Minute Setup)

[!IMPORTANT]
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

AAdd the Cortex remote configuration (Claude Desktop):

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

### Available MCP Tools

Once connected, your AI agent automatically acquires these native tools:

| Tool Name | Type | Description |
| :--- | :--- | :--- |
| `cortex_recall` | Query | Sub-65ms semantic & graph recall. Injects user bio, active project specs, and knowledge graph relations before generating a response. Always active (even in read-only mode). |
| `cortex_ingest_turn` | Ingestion | **Mandatory turn logger.** Automatically captures the conversational turn (`user_message` + `assistant_message`) into the async ingestion buffer for nocturnal consolidation. |
| `cortex_store_memory` | Write | Explicitly saves system constraints, architectural decisions, and project facts directly to a specific `project_id` and `topic`. |
| `cortex_get_project_spec` | Inspection | Deterministically retrieves the full canonical specification (Living Document) for any project, bypassing vector search limitations. |
| `cortex_triage_general` | Maintenance | Compaction and migration tool that moves unstructured notes from the `general` incubator into dedicated projects. |

---

### Core Architecture Highlights

* **Sub-65ms Zero-LLM Recall:** Direct exact-cosine edge matching in Neo4j and indexed PostgreSQL vectors—bypassing heavy runtime LLM keyword extractors.
* **Dual-Zone Fast-Append:** Instant raw fact capture (< 20ms) into an inbox zone, followed by asynchronous consolidation into a structured scientific schema (*Summary*, *Aim*, *Materials & Methods*, *Ideas*, *Attachments*).
* **Anti-Race Synthesis Guard:** Invariant guard enforcing `facts_volume_ratio >= 0.85`, preventing critical parameter deletions during re-indexing.
* **Immunity Shield:** Operational errors, tool crashes, and conversational apologies are filtered by design and never corrupted into permanent memory.

---

## Support & Feedback

Encountered an issue or have a feature suggestion?

* **Bug Reports & Issues:** [Open an Issue](#)
* **Status & Portal:** [cortex.bluesynergy.io](https://cortex.bluesynergy.io)
