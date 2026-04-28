# Aapryl Research System Architecture

## Purpose

This repo now implements a **Neo4j-centric finished GraphRAG** architecture for the research corpus in `knowledge_base/`.

The system has two phases:

1. `Creation`
   Build a finished lexical + semantic knowledge graph in Neo4j.
2. `Retrieval`
   Query the finished graph through MCP in read-only mode.

## Implemented Status

As of `2026-04-02`, the local implementation reflects this design:

- the primary runtime no longer depends on `LlamaCloud`
- the primary graph builder no longer uses `LlamaIndex PropertyGraphIndex`
- query-time retrieval does not require OpenAI calls
- the graph build still requires:
  - `OPENAI_API_KEY`
  - `NEO4J_URI`
  - `NEO4J_USERNAME`
  - `NEO4J_PASSWORD`
  - `NEO4J_DATABASE`
- `LLAMA_PARSE_API_KEY` is optional and only improves PDF parsing

The current local dry-run state is:

- `sources_found = 11`
- `chunks_prepared = 427`
- `corpus_hash = 83b3f98c76aa93bdda62723fb27aaf62bd7428d5e34da097cdd9537a69ac170f`

The live Neo4j graph has not yet been built in the current environment because the required live credentials are still missing.

## Current Architecture

### 1. Local corpus

The source corpus lives in:

- `knowledge_base/`

The repo scans that directory, builds a deterministic source manifest, and computes a stable `corpus_hash`.

### 2. Shared chunk preparation

The local ingestion layer in `llamacloud_rag/corpus.py`:

- scans supported `.md` and `.pdf` files
- builds source metadata
- chunks the corpus into stable chunk documents with a local deterministic chunker
- preserves `source_path`, `page_label`, `chunk_index`, and `chunk_total`
- falls back to local PDF extraction with `pypdf`
- uses `LlamaParse` only when `LLAMA_PARSE_API_KEY` is present

This chunk-prep layer is the source of truth for graph creation.

### 3. Neo4j graph creation

The graph is built with the **Neo4j GraphRAG Python package**.

The creation pipeline writes:

- a lexical provenance graph:
  - `Document`
  - `Chunk`
  - `FROM_DOCUMENT`
  - `NEXT_CHUNK`
  - `FROM_CHUNK`
- a semantic graph with typed entities and relationships

The semantic ontology is:

- nodes:
  - `PROVIDER`
  - `PAPER`
  - `STYLE`
  - `BENCHMARK`
  - `SIGNAL`
  - `METHOD`
  - `CONSTRAINT`
  - `METRIC`
  - `DATA_SOURCE`
  - `IMPLEMENTATION_STEP`
- relationships:
  - `DEFINES`
  - `USES`
  - `COMPARES`
  - `CONSTRAINS`
  - `MEASURES`
  - `OVERLAYS_ON`
  - `REQUIRES`
  - `DOCUMENTS`

The graph creation path:

- uses `gpt-4o` only during creation/rebuild
- uses `LLMEntityRelationExtractor` as the semantic extractor
- runs exact-name entity resolution after extraction
- creates Neo4j full-text indexes for:
  - semantic entity lookup
  - chunk lookup
- stores build state in `.neo4j_graph_state.json`

### 4. MCP retrieval

The repo exposes one MCP server:

- `xponance_research`

It now serves graph-first read-only retrieval:

- `search_xponance_graph(...)`
- `answer_xponance_graph(...)`
- `get_xponance_research_graph_status()`
- `get_xponance_research_index_status()`

The default retrieval contract is:

- `Path + Chunk`

That means MCP answers return:

- graph path nodes and relationships
- exact supporting chunk references
- `source_path`
- `page_label`
- `chunk_id`

MCP does not create or mutate the graph during normal retrieval.
MCP also does not synthesize final prose by default; `answer_xponance_graph(...)` is retrieval-only and leaves final synthesis to the MCP client.

### 5. Retrieval method

The implemented retrieval path is Neo4j-first and deterministic:

- full-text search seeds the query against semantic entity names and chunk text
- graph traversal follows only the allowed semantic relationship types
- chunk evidence is attached from the lexical provenance layer

In v1, query-time retrieval does **not** depend on embeddings or query-time model calls. The current retrieval path is:

- full-text search
- graph traversal
- lexical chunk evidence

Graph-side vector retrieval can be added later, but it is not part of the current primary runtime.

## Evidence Flow

1. Documents are stored locally in `knowledge_base/`.
2. The corpus layer builds a manifest and chunk inventory.
3. The graph build command creates a finished Neo4j graph.
4. The graph state is recorded locally with `corpus_hash`.
5. MCP queries the finished graph and returns path-plus-chunk evidence.
6. Codex or other MCP clients synthesize final prose from the returned evidence.

## Corpus Integrity Gate

The repo still enforces a fail-closed corpus gate.

The gate checks:

- active `data_dir`
- local source inventory
- local `corpus_hash`
- Neo4j graph state

If the finished graph does not match the active corpus, MCP returns `corpus_mismatch` instead of partial graph evidence.

## Operational Model

This system is designed as a **durable artifact**:

- build once
- query many times
- rebuild only when the corpus or schema changes

The primary store is Neo4j. `LlamaCloud` is no longer part of the primary retrieval architecture.

## Current Operational Gap

The architecture is implemented locally, but the live graph is not yet ready in the current environment because:

- `NEO4J_PASSWORD` is not populated
- `OPENAI_API_KEY` is not populated
- `.neo4j_graph_state.json` has not been written from a live build yet

That means the expected current MCP status is:

- `get_xponance_research_index_status()` reports the local corpus correctly
- `get_xponance_research_graph_status()` reports `corpus_mismatch` / graph not built yet

That is the correct fail-closed behavior until the first live Neo4j rebuild succeeds.
