import json
import os
import sys
from typing import Any

import httpx

CORTEX_API_URL = os.getenv("CORTEX_API_URL", "https://cortex.bluesynergy.io").rstrip("/")
CORTEX_API_KEY = os.getenv("CORTEX_API_KEY", "").strip()
CORTEX_USER_ID = os.getenv("CORTEX_USER_ID", "default_user")
CORTEX_AGENT_ID = os.getenv("CORTEX_AGENT_ID", "mcp_client")

TOOLS: list[dict[str, Any]] = [
    {
        "name": "cortex_recall",
        "description": "Sub-65ms Zero-LLM hierarchical recall combining Tri-Stream Master Identity, Hybrid Vector+FTS RAG, Smart Canonical Project Summaries, and Neo4j Exact Cosine graph edges.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Natural language search query or current user prompt."},
                "compact": {"type": "boolean", "description": "Optional token-saving mode for CLI/IDE agents.", "default": False},
            },
            "required": ["query"],
            "additionalProperties": False,
        },
    },
    {
        "name": "cortex_store_memory",
        "description": "Explicitly store exact technical specifications, architectural pillars, or facts into a dedicated project stream without biological forgetting.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "content": {"type": "string", "description": "Exact fact, rule, or specification to persist."},
                "project_id": {"type": "string", "description": "Target normalized project identifier (snake_case)."},
                "topic": {"type": "string", "description": "Optional topic or section tag."},
            },
            "required": ["content", "project_id"],
            "additionalProperties": False,
        },
    },
    {
        "name": "cortex_get_project_spec",
        "description": "Deterministically retrieve the latest Living Canonical Specification (Zone A + Zone B) of a given project, bypassing vector estimation.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "project_id": {"type": "string", "description": "Project identifier (e.g. 'general' or specific project slug)."},
            },
            "required": ["project_id"],
            "additionalProperties": False,
        },
    },
    {
        "name": "cortex_triage_general",
        "description": "Execute approved index-based migration or cleanup of orphaned facts from the 'general' incubator into dedicated projects.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "approved_projects": {
                    "type": "array",
                    "description": "List of migration or deletion instructions with assigned block indices.",
                    "items": {"type": "object"},
                },
            },
            "required": ["approved_projects"],
            "additionalProperties": False,
        },
    },
    {
        "name": "cortex_manage_draft",
        "description": "Approve, promote, merge, or discard quarantined draft projects created by the Memory Firewall.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "draft_id": {"type": "string", "description": "Quarantined draft project identifier."},
                "action": {"type": "string", "enum": ["approve", "merge", "discard"], "description": "Action to perform on the draft."},
                "target_project_id": {"type": "string", "description": "Optional target project ID when merging."},
            },
            "required": ["draft_id", "action"],
            "additionalProperties": False,
        },
    },
    {
        "name": "cortex_create_project",
        "description": "Explicitly initialize a new canonical project branch in the Cortex Knowledge Stream.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "project_id": {"type": "string", "description": "Unique project slug (snake_case)."},
                "project_name": {"type": "string", "description": "Human-readable project title."},
                "summary": {"type": "string", "description": "Initial project aim and architectural overview."},
            },
            "required": ["project_id"],
            "additionalProperties": False,
        },
    },
    {
        "name": "cortex_ingest_turn",
        "description": "Asynchronously push conversation turns into the high-speed Cortex ingest buffer (<10ms) for background Tri-Stream routing.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "messages": {"type": "array", "description": "List of conversation message objects (role, content).", "items": {"type": "object"}},
                "project_id": {"type": "string", "description": "Optional project_id for direct knowledge routing."},
            },
            "required": ["messages"],
            "additionalProperties": False,
        },
    },
    {
        "name": "cortex_consolidate_project",
        "description": "Enqueue asynchronous Order-II scientific ontology consolidation and differential Zone-B ledger synthesis for a project.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "project_id": {"type": "string", "description": "Project identifier to consolidate."},
            },
            "required": ["project_id"],
            "additionalProperties": False,
        },
    },
    {
        "name": "cortex_deprecate_memory",
        "description": "Explicitly deprecate an outdated or superseded rule/fact by memory ID while preserving historical auditability.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "memory_id": {"type": "integer", "description": "Numeric ID of the memory record to deprecate."},
                "reason": {"type": "string", "description": "Reason for deprecation (e.g. superseded by new revision)."},
            },
            "required": ["memory_id"],
            "additionalProperties": False,
        },
    },
]

ENDPOINT_MAP: dict[str, str] = {
    "cortex_recall": "/v1/recall",
    "cortex_store_memory": "/v1/memory/store",
    "cortex_get_project_spec": "/v1/specs/get",
    "cortex_triage_general": "/v1/specs/triage",
    "cortex_manage_draft": "/v1/drafts/manage",
    "cortex_create_project": "/v1/projects/create",
    "cortex_ingest_turn": "/v1/threads/ingest",
    "cortex_deprecate_memory": "/v1/memory/deprecate",
}


def _send(payload: dict[str, Any]) -> None:
    sys.stdout.write(json.dumps(payload, ensure_ascii=False) + "\n")
    sys.stdout.flush()


def _send_result(req_id: Any, result: dict[str, Any]) -> None:
    _send({"jsonrpc": "2.0", "id": req_id, "result": result})


def _send_error(req_id: Any, code: int, message: str) -> None:
    _send({"jsonrpc": "2.0", "id": req_id, "error": {"code": code, "message": message}})


def _call_cortex_api(name: str, arguments: dict[str, Any]) -> dict[str, Any]:
    if not CORTEX_API_KEY.startswith("ctx_"):
        return {
            "content": [
                {
                    "type": "text",
                    "text": (
                        "CORTEX_API_KEY is not configured or invalid. "
                        "Get your 21-day free trial key (ctx_live_...) at https://cortex.bluesynergy.io "
                        "and pass it via the CORTEX_API_KEY environment variable."
                    ),
                }
            ],
            "isError": False,
        }

    if name == "cortex_consolidate_project":
        project_id = arguments.get("project_id", "general")
        path = f"/v1/projects/{project_id}/consolidate"
    else:
        path = ENDPOINT_MAP.get(name)
        if not path:
            return {"content": [{"type": "text", "text": f"Unknown tool: {name}"}], "isError": True}

    body = {"user_id": CORTEX_USER_ID, "agent_id": CORTEX_AGENT_ID, **arguments}
    headers = {"Authorization": f"Bearer {CORTEX_API_KEY}", "Content-Type": "application/json"}

    try:
        with httpx.Client(timeout=30.0) as client:
            resp = client.post(f"{CORTEX_API_URL}{path}", json=body, headers=headers)
            resp.raise_for_status()
            return {"content": [{"type": "text", "text": resp.text}], "isError": False}
    except Exception as exc:
        return {"content": [{"type": "text", "text": f"Cortex API request failed: {exc}"}], "isError": True}


def main() -> None:
    sys.stdin.reconfigure(encoding="utf-8")
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)

    for raw_line in sys.stdin:
        line = raw_line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            continue

        if not isinstance(msg, dict) or "id" not in msg:
            continue

        req_id = msg["id"]
        method = msg.get("method", "")
        params = msg.get("params") or {}

        if method == "initialize":
            protocol_version = params.get("protocolVersion") or "2024-11-05"
            _send_result(
                req_id,
                {
                    "protocolVersion": protocol_version,
                    "capabilities": {
                        "tools": {"listChanged": False},
                        "resources": {"subscribe": False, "listChanged": False},
                        "prompts": {"listChanged": False},
                    },
                    "serverInfo": {"name": "bs-cortex", "version": "3.0.0"},
                },
            )
        elif method == "ping":
            _send_result(req_id, {})
        elif method == "tools/list":
            _send_result(req_id, {"tools": TOOLS})
        elif method == "resources/list":
            _send_result(req_id, {"resources": []})
        elif method == "resources/templates/list":
            _send_result(req_id, {"resourceTemplates": []})
        elif method == "prompts/list":
            _send_result(req_id, {"prompts": []})
        elif method == "tools/call":
            tool_name = params.get("name", "")
            tool_args = params.get("arguments") or {}
            _send_result(req_id, _call_cortex_api(tool_name, tool_args))
        else:
            _send_error(req_id, -32601, f"Method not found: {method}")


if __name__ == "__main__":
    main()
