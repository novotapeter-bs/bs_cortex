import asyncio
import os
from typing import Any

import mcp.types as types
from mcp.client.session import ClientSession
from mcp.client.sse import sse_client
from mcp.server import Server
from mcp.server.stdio import stdio_server

CORTEX_SSE_URL = os.getenv("CORTEX_SSE_URL", "https://cortex.bluesynergy.io/v1/mcp/sse")
CORTEX_API_KEY = os.getenv("CORTEX_API_KEY", "").strip()

app = Server("bs-cortex")

# Statická definice 9 nástrojů Cortex v3.0 pro offline introspekci (Glama.ai / sandbox bez klíče)
OFFLINE_TOOLS: list[types.Tool] = [
    types.Tool(
        name="cortex_recall",
        description="Sub-65ms Zero-LLM hierarchical recall combining Tri-Stream Master Identity, Hybrid Vector+FTS RAG, Smart Canonical Project Summaries, and Neo4j Exact Cosine graph edges.",
        inputSchema={
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Natural language search query or current user prompt."},
                "compact": {"type": "boolean", "description": "Optional token-saving mode for CLI/IDE agents.", "default": False},
            },
            "required": ["query"],
        },
    ),
    types.Tool(
        name="cortex_store_memory",
        description="Explicitly store exact technical specifications, architectural pillars, or facts into a dedicated project stream without biological forgetting.",
        inputSchema={
            "type": "object",
            "properties": {
                "content": {"type": "string", "description": "Exact fact, rule, or specification to persist."},
                "project_id": {"type": "string", "description": "Target normalized project identifier (snake_case)."},
                "topic": {"type": "string", "description": "Optional topic or section tag."},
            },
            "required": ["content", "project_id"],
        },
    ),
    types.Tool(
        name="cortex_get_project_spec",
        description="Deterministically retrieve the latest Living Canonical Specification (Zone A + Zone B) of a given project, bypassing vector estimation.",
        inputSchema={
            "type": "object",
            "properties": {
                "project_id": {"type": "string", "description": "Project identifier (e.g. 'general' or specific project slug)."},
            },
            "required": ["project_id"],
        },
    ),
    types.Tool(
        name="cortex_triage_general",
        description="Execute approved index-based migration or cleanup of orphaned facts from the 'general' incubator into dedicated projects.",
        inputSchema={
            "type": "object",
            "properties": {
                "approved_projects": {
                    "type": "array",
                    "description": "List of migration or deletion instructions with assigned block indices.",
                    "items": {"type": "object"},
                },
            },
            "required": ["approved_projects"],
        },
    ),
    types.Tool(
        name="cortex_manage_draft",
        description="Approve, promote, merge, or discard quarantined draft projects created by the Memory Firewall.",
        inputSchema={
            "type": "object",
            "properties": {
                "draft_id": {"type": "string", "description": "Quarantined draft project identifier."},
                "action": {"type": "string", "enum": ["approve", "merge", "discard"], "description": "Action to perform on the draft."},
                "target_project_id": {"type": "string", "description": "Optional target project ID when merging."},
            },
            "required": ["draft_id", "action"],
        },
    ),
    types.Tool(
        name="cortex_create_project",
        description="Explicitly initialize a new canonical project branch in the Cortex Knowledge Stream.",
        inputSchema={
            "type": "object",
            "properties": {
                "project_id": {"type": "string", "description": "Unique project slug (snake_case)."},
                "project_name": {"type": "string", "description": "Human-readable project title."},
                "summary": {"type": "string", "description": "Initial project aim and architectural overview."},
            },
            "required": ["project_id"],
        },
    ),
    types.Tool(
        name="cortex_ingest_turn",
        description="Asynchronously push conversation turns into the high-speed Cortex ingest buffer (<10ms) for background Tri-Stream routing.",
        inputSchema={
            "type": "object",
            "properties": {
                "messages": {"type": "array", "description": "List of conversation message objects (role, content).", "items": {"type": "object"}},
                "project_id": {"type": "string", "description": "Optional project_id for direct knowledge routing."},
            },
            "required": ["messages"],
        },
    ),
    types.Tool(
        name="cortex_consolidate_project",
        description="Enqueue asynchronous Order-II scientific ontology consolidation and differential Zone-B ledger synthesis for a project.",
        inputSchema={
            "type": "object",
            "properties": {
                "project_id": {"type": "string", "description": "Project identifier to consolidate."},
            },
            "required": ["project_id"],
        },
    ),
    types.Tool(
        name="cortex_deprecate_memory",
        description="Explicitly deprecate an outdated or superseded rule/fact by memory ID while preserving historical auditability.",
        inputSchema={
            "type": "object",
            "properties": {
                "memory_id": {"type": "integer", "description": "Numeric ID of the memory record to deprecate."},
                "reason": {"type": "string", "description": "Reason for deprecation (e.g. superseded by new revision)."},
            },
            "required": ["memory_id"],
        },
    ),
]


def _auth_headers() -> dict[str, str]:
    return {"Authorization": f"Bearer {CORTEX_API_KEY}"}


@app.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    if CORTEX_API_KEY.startswith("ctx_"):
        try:
            async with sse_client(url=CORTEX_SSE_URL, headers=_auth_headers()) as (read, write):
                async with ClientSession(read, write) as session:
                    await session.initialize()
                    res = await session.list_tools()
                    return res.tools
        except Exception:
            return OFFLINE_TOOLS
    return OFFLINE_TOOLS


@app.list_resources()
async def handle_list_resources() -> list[types.Resource]:
    return []


@app.list_prompts()
async def handle_list_prompts() -> list[types.Prompt]:
    return []


@app.call_tool()
async def handle_call_tool(name: str, arguments: dict[str, Any] | None) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    if not CORTEX_API_KEY:
        return [
            types.TextContent(
                type="text",
                text=(
                    "CORTEX_API_KEY is not configured. "
                    "Blue Synergy Cortex runs on a stateless cloud cognitive engine. "
                    "Get your 21-day free trial API key (ctx_live_...) at https://cortex.bluesynergy.io "
                    "and set CORTEX_API_KEY in your MCP environment."
                ),
            )
        ]

    async with sse_client(url=CORTEX_SSE_URL, headers=_auth_headers()) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.call_tool(name, arguments or {})
            return list(result.content)


async def main() -> None:
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options(),
        )


if __name__ == "__main__":
    asyncio.run(main())
