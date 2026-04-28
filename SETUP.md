# Setup Instructions

This repo runs a Neo4j-centric GraphRAG workflow over the local `knowledge_base/` corpus and exposes retrieval through a local MCP server.

## Requirements

- Python `3.12+`
- A Neo4j database
- An OpenAI API key for graph build and rebuild steps

Install dependencies with:

```powershell
python -m venv .venv
.venv\Scripts\python -m pip install --upgrade pip
.venv\Scripts\python -m pip install -r requirements.txt
```

If you want the package installed in editable mode for local development:

```powershell
.venv\Scripts\python -m pip install -e .
```

## Environment Setup

Create your local env file:

```powershell
Copy-Item .env.example .env
```

Populate `.env` with the required values:

- `OPENAI_API_KEY`
- `NEO4J_URI`
- `NEO4J_USERNAME`
- `NEO4J_PASSWORD`
- `NEO4J_DATABASE`

Optional:

- `LLAMA_PARSE_API_KEY`

## Build The Graph

Dry-run the corpus pipeline first:

```powershell
.venv\Scripts\python -m llamacloud_rag.graph_bootstrap --dry-run
```

Build or rebuild the Neo4j graph:

```powershell
.venv\Scripts\python -m llamacloud_rag.graph_bootstrap --rebuild
```

## Run The MCP Server

Start the local MCP server with:

```powershell
.venv\Scripts\python -m llamacloud_rag.mcp_server
```

## Notes

- The intended corpus is `knowledge_base/`.
- The default research evidence policy in this repo is `MCP-only`.
- Query-time retrieval is intended to run against the built Neo4j graph, not ad hoc local-file reasoning.
