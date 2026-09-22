<div align="center">

# Blue Synergy CORTEX - coming soon...


# Blue Synergy Cortex (v3.0) 🧠⚡

> **Long-term, drift-free cognitive memory engine for AI Agents, Cursor IDE, and Claude Desktop via Model Context Protocol (MCP).**

[![MCP Compatible](https://img.shields.io/badge/MCP-FastMCP%20SSE-blue.svg)](https://modelcontextprotocol.io/)
[![Latency](https://img.shields.io/badge/Recall%20Latency-%3C30ms-green.svg)]()
[![Architecture](https://img.shields.io/badge/Tri--Stream-Stateless-orange.svg)]()

---

### Stop AI Amnesia & Specification Drift

Most memory systems treat everything as fluid vector soup—causing agents to hallucinate, forget strict technical requirements, or confuse user preferences with code specs.

**Blue Synergy Cortex** implements an enterprise-grade **Tri-Stream Architecture** backed by transactional PostgreSQL and Neo4j:
1. **User Stream:** Generalizes conversational habits and user preferences over time.
2. **Identity Stream:** Deterministic guardrails and behavioral axioms that prevent sycophancy.
3. **Knowledge Stream (Living Specs):** Exact architecture specifications, hardware limits, and system parameters organized into an immutable **Universal Scientific Ontology**. This stream is **protected against lossy compression, semantic decay, and accidental drift**.

</div>
---

## 🚀 Quickstart (1 Minute Setup)

To use Cortex, you need an API key. 
👉 **[Get your 21-day Free Trial API Key here](https://cortex.bluesynergy.io)**

---

### 1. Cursor IDE Integration

1. Open **Cursor Settings** (`Ctrl+Shift+J` or `Cmd+Shift+J`).
2. Navigate to **Features** -> **MCP Servers** -> **Add new MCP server**.
3. Configure as follows:
   * **Name:** `cortex-memory`
   * **Type:** `sse`
   * **URL:** `https://cortex.bluesynergy.io/v1/mcp/sse?api_key=YOUR_API_KEY`
4. Save. Your Cursor Composer and Agent now have permanent recall across restarts!

---

### 2. Claude Desktop Integration

Edit your configuration file:
* **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
* **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

Add the Cortex remote configuration:

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
5. Restart Claude Desktop
