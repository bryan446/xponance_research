# Xponance Neo4j GraphRAG

This repo now uses a Neo4j-centric GraphRAG path:

1. Scan the local `.md` and `.pdf` research corpus.
2. Chunk the corpus with stable chunk IDs and a deterministic `corpus_hash`.
3. Build a finished Neo4j lexical + semantic knowledge graph.
4. Expose that graph through one local Python MCP server over `stdio`.

The full setup and operating guide lives in [docs/neo4j_graphrag_setup.md](/c:/Users/bryan/OneDrive/Desktop/xponance_research/docs/neo4j_graphrag_setup.md).

## Agent Infrastructure

This repo now includes a repo-local Codex research-agent pack for the Aapryl factor-index project:

- `AGENTS.md`: repo-wide guidance and evidence rules
- `.agents/roles/`: orchestration and specialist role contracts
- `.agents/templates/`: named artifact contracts for each stage of the workflow

### Default Flow

The default research flow is:

1. `corpus-auditor`
2. `coordinator`
3. specialist roles as needed
4. `memo-writer`

Under the default `MCP-only` evidence policy, the system hard-stops on corpus mismatch instead of continuing with contaminated evidence.

### Retrieval Layers

- `Neo4j AuraDB`: lexical provenance graph plus factor-research knowledge graph.
- `MCP`: one repo-owned tool surface that exposes graph-first retrieval.

### Example Invocations

Use prompts like these when you want Codex to lean on the repo-local agent briefs:

```text
Use the corpus auditor role in `.agents/roles/corpus-auditor.md` first. Enforce `MCP-only` research and return a corpus gate report.
```

```text
Use the coordinator role in `.agents/roles/coordinator.md`. Enforce `MCP-only` research. Turn the manager email into the full artifact package for the Aapryl factor-index project.
```

```text
Use the portfolio construction analyst role in `.agents/roles/portfolio-construction-analyst.md`. Compare `weighted rank` vs `2-step` for `Quality Value` in `Russell 1000` and return the benchmark-specific test plan.
```

```text
Use the manager exposure analyst role in `.agents/roles/manager-exposure-analyst.md`. Build the active-manager calibration plan and the `data-needed-from-FactSet` artifact for sector and region limits.
```

```text
Use the index methodology designer role in `.agents/roles/index-methodology-designer.md`. Draft the style archetype and benchmark overlay rulebook outline for `Quality Growth` in `Russell 1000` and `MSCI EAFE`.
```

```text
Use the implementation planner role in `.agents/roles/implementation-planner.md`. Convert the approved methodology into a `FactSet` and monthly refresh implementation spec.
```

## Quick Start

```powershell
python -m venv .venv
.venv\Scripts\python -m pip install --upgrade pip
.venv\Scripts\python -m pip install -e .
Copy-Item .env.example .env
```

Set `NEO4J_*` and `OPENAI_API_KEY` in `.env`, then dry-run the graph build:

```powershell
.venv\Scripts\python -m llamacloud_rag.graph_bootstrap --dry-run
.venv\Scripts\python -m llamacloud_rag.graph_bootstrap --rebuild
```

Run the MCP server:

```powershell
.venv\Scripts\python -m llamacloud_rag.mcp_server
```
