# Neo4j GraphRAG setup

This repo now uses a Neo4j-centric GraphRAG architecture.

## What it does

- scans the local corpus in `knowledge_base/`
- prepares stable chunk IDs and a deterministic `corpus_hash`
- builds a finished lexical + semantic graph in Neo4j
- exposes a read-only MCP server for graph retrieval

## Install

PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\python -m pip install --upgrade pip
.venv\Scripts\python -m pip install -e .
```

## Configure

Copy `.env.example` to `.env`, then set:

- `NEO4J_URI`
- `NEO4J_USERNAME`
- `NEO4J_PASSWORD`
- `NEO4J_DATABASE`
- `OPENAI_API_KEY` for creation/rebuild only
- `LLAMA_PARSE_API_KEY` only if you want managed PDF parsing

The default corpus is `knowledge_base/`.

## Build the graph

Dry run:

```powershell
.venv\Scripts\python -m llamacloud_rag.graph_bootstrap --dry-run
```

Build or rebuild:

```powershell
.venv\Scripts\python -m llamacloud_rag.graph_bootstrap --rebuild
```

The build writes local state to `.neo4j_graph_state.json` by default.

## Run the MCP server

```powershell
.venv\Scripts\python -m llamacloud_rag.mcp_server
```

## MCP tools

- `search_xponance_graph(query, top_k=5, path_depth=2)`
- `answer_xponance_graph(query, top_k=5, path_depth=2, citation_chunk_size=512)`
- `get_xponance_research_graph_status()`
- `get_xponance_research_index_status()`

`answer_xponance_graph` is retrieval-only. It returns graph paths plus supporting chunk references; MCP clients synthesize final prose.

## Production shape

- `Neo4j AuraDB` stores the finished graph
- `repo MCP` exposes read-only retrieval
- `Codex` and other MCP clients query the finished graph
