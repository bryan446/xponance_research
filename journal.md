# Journal

## 2026-04-02 - Finalized the implemented Neo4j-first runtime and removed the last primary-path drift

The repo is now internally aligned around one runtime:

- local corpus in `knowledge_base/`
- deterministic local chunk preparation
- Neo4j GraphRAG build path for creation
- Neo4j-first MCP retrieval for normal use

The main corrections in this final pass were:

- removed the remaining primary-path dependency on `llama_index` from the corpus loader
- replaced framework chunking with a local deterministic chunker in `llamacloud_rag/corpus.py`
- kept `LlamaParse` as optional only and `pypdf` as the local PDF fallback
- renamed the package docs metadata so the repo no longer advertises the retired LlamaCloud-first setup
- revalidated the MCP status surface against the current graph-only architecture

The most important implemented facts at the end of this pass are:

- the graph build path uses `neo4j-graphrag[openai,experimental]`
- the graph build path uses `gpt-4o` only during creation/rebuild
- the retrieval path does not require query-time OpenAI calls
- the MCP server is graph-only and retrieval-only by default
- the evidence contract is `Path + Chunk`

The local validation result at the end of this pass was:

- unit tests passed
- compile check passed
- graph dry-run passed
- the local corpus now resolves to:
  - `sources_found = 11`
  - `chunks_prepared = 427`
  - `corpus_hash = 83b3f98c76aa93bdda62723fb27aaf62bd7428d5e34da097cdd9537a69ac170f`

The current remaining blocker is purely operational:

- `OPENAI_API_KEY` is still missing for build-time extraction
- `NEO4J_PASSWORD` is still missing for the live Neo4j build

Because of that, the expected current state is:

- `get_xponance_research_index_status()` reports the local corpus correctly
- `get_xponance_research_graph_status()` correctly fails closed and reports that the graph is not built/configured yet

## 2026-04-02 - Replaced the hybrid path with a Neo4j-centric GraphRAG architecture

The repo no longer treats LlamaCloud as a primary retrieval dependency.

The main refactor completed in this pass was:

- replaced the LlamaIndex-first graph builder with Neo4j GraphRAG components
- simplified the configuration layer so Neo4j is the primary store and `OPENAI_API_KEY` is only required for graph creation
- removed the LlamaCloud-backed MCP tools from the primary runtime path
- rewrote the MCP server around graph-first, retrieval-only responses
- changed the default evidence contract to `Path + Chunk`
- updated docs and env templates so the repo now documents one finished-graph architecture instead of a hybrid vector + graph architecture

At the end of this refactor, the intended runtime is:

- `knowledge_base/` as the only source corpus
- Neo4j AuraDB as the durable lexical + semantic graph store
- one graph build command
- one MCP retrieval server
- no query-time model dependency after the graph has been built

## 2026-04-02 - Implemented the hybrid LlamaCloud + Neo4j architecture

The repo moved from a LlamaCloud-only retrieval scaffold to an actual hybrid retrieval architecture.

The main implementation work completed was:

- extended the configuration layer to support Neo4j, OpenAI, graph-state paths, chunk sizing, and LlamaParse settings
- refactored the corpus layer so it now builds chunk-preserving documents instead of flattening each source into one combined file-level document
- added deterministic file-hash manifests and a `corpus_hash` so the repo has a stable way to compare local corpus state against vector and graph state
- added a shared `corpus_mismatch` gate that now applies to vector retrieval, graph retrieval, and hybrid retrieval
- added a Neo4j graph backend with two graph layers:
  - lexical provenance graph
  - domain knowledge graph
- added a graph schema for the factor-research ontology:
  - `STYLE`
  - `BENCHMARK`
  - `PROVIDER`
  - `PAPER`
  - `SIGNAL`
  - `METHOD`
  - `CONSTRAINT`
  - `METRIC`
  - `DATA_SOURCE`
  - `IMPLEMENTATION_STEP`
- added a graph build entrypoint and wrapper scripts
- extended the MCP server with:
  - `search_xponance_graph`
  - `answer_xponance_hybrid_research`
  - `get_xponance_research_graph_status`

This was the point where the architecture stopped being theoretical. The repo now has actual code paths for:

- `local corpus -> chunked documents`
- `chunked documents -> LlamaCloud vector index`
- `chunked documents -> Neo4j lexical graph + domain KG`
- `vector + graph state -> one MCP tool surface`

## 2026-04-02 - Installed the graph dependencies and verified the local implementation

After the code changes were made, the repo environment was updated so the graph architecture could actually import and run.

The main dependency additions were:

- `llama-index-graph-stores-neo4j`
- `llama-index-llms-openai`
- `llama-index-embeddings-openai`
- `llama-parse`
- `neo4j`

The implementation was verified locally by:

- running the unit tests for the corpus hash and gate logic
- compiling the package after the graph code was added
- confirming that the new graph-specific imports resolve in the project virtual environment
- running a graph dry-run against a temporary local corpus

This matters because the repo is no longer at the "design only" stage. The local implementation is now coherent enough to run once the live credentials are in place.

This entry is now historical. The current runtime no longer uses these older LlamaIndex graph dependencies as the primary path.

## 2026-04-02 - Clarified the new real bottleneck: live service state

The biggest remaining blocker is no longer missing architecture. It is live service alignment.

The local code is in place, but the live system is still not ready for evidence-backed hybrid retrieval because:

- the graph has not yet been built against the live Neo4j Aura database
- `.env` still needs the full production credential set filled in

The important status fact at the end of implementation was:

- the MCP still correctly reports `corpus_mismatch`

That is actually the right outcome at this stage. It means the new hard gate is working. The system is refusing to pretend that live vector and graph evidence are ready before the real sync and graph build have been done.

The remaining operational sequence is now very concrete:

1. fill in `.env` with working:
   - `OPENAI_API_KEY`
   - `NEO4J_URI`
   - `NEO4J_USERNAME`
   - `NEO4J_PASSWORD`
   - `NEO4J_DATABASE`
   - optionally `LLAMA_PARSE_API_KEY`
2. run the real Neo4j graph build
3. start the MCP server
4. verify that:
   - index status is clean
   - graph status is clean
   - the graph state agrees with the local `data_dir` and `corpus_hash`

## 2026-04-02 - Updated the documentation to match the implementation

The architecture and setup documentation were updated so they no longer describe only the older LlamaCloud-only system.

The main documentation changes were:

- `architecture.md` was rewritten into one coherent current-state architecture document instead of mixed old and new sections
- the setup docs now explain the graph build path, graph env vars, and graph-only MCP tools
- the README now describes the repo as a Neo4j-centric finished-graph system rather than a hybrid retrieval system

This is important because the repo had reached the point where documentation drift would have become a real operating risk. The system now has enough moving parts that inaccurate docs would be almost as harmful as missing code.

## 2026-04-01 - Reframed the research system around a real project workflow

Today the project moved from a loose collection of notes and prompts into a more explicit research system for the Aapryl factor-index work. The manager email clarified that the real assignment is not just literature review. It is a full research, design, and implementation program for four factor families:

- `Deep Value`
- `Quality Value`
- `Quality Growth`
- `Aggressive Growth`

Each style ultimately needs to be expressed against four benchmark families:

- `Russell 1000`
- `Russell 2000`
- `MSCI EAFE`
- `MSCI EM`

The biggest conceptual shift was recognizing that the work has two layers:

1. `style archetype` design
2. `benchmark overlay` design

That matters because the factor logic should not be reinvented sixteen different times. The style should be defined once, then adapted to each benchmark universe with explicit rules around eligibility, weights, limits, and implementation.

The two unusual design questions from the manager email also became clearer:

- region and sector limits should reflect the observed behavior of active managers using these styles, not generic index-provider neutrality rules
- `weighted rank` versus `2-step screen-then-rank` is a real methodological decision that needs literature support plus empirical testing, not just intuition

## 2026-04-01 - Clarified what the MCP, the knowledge base, and LlamaCloud actually are

There was a lot of confusion initially about what was local, what was remote, and what exactly the MCP was doing. That is now much clearer.

This entry is historical and describes the pre-refactor understanding before the repo moved to the Neo4j-first runtime on `2026-04-02`.

The important distinction is:

- the actual research documents live locally in this repo
- `xponance_research` is the MCP server alias that Codex uses
- LlamaCloud is the remote indexing and retrieval backend

In other words, the current system does not pull from some hidden external LlamaCloud library. It indexes copies of local files and then serves search results from that remote index. The remote part is the chunking, embeddings, storage, and retrieval layer. The source material is still local.

This also changed how prompts should be written. If the goal is to force a knowledge-base-backed answer, the prompt needs to say:

- use only `xponance_research`
- do not use general knowledge
- include file/page references
- say `insufficient evidence` when unsupported

That became the foundation for the evidence policy in the project agent system.

## 2026-04-01 - Added citation-aware research behavior

The original MCP research flow was retrieval-only and returned trimmed search results, but it was not designed to produce a more structured answer with citation metadata. That gap mattered because the research workflow needs traceability.

The MCP server was extended so that:

- retrieval results include better citation fields
- a citation-aware answer mode exists for the research server
- the project can more easily support file/page-aware outputs

This did not mean that all answers magically became perfect citations. It meant the plumbing now supports a better evidence chain and can be used for citation-oriented research prompts.

## 2026-04-01 - Switched the intended knowledge base to `knowledge_base/`

The project originally pointed at the repo root as the effective research corpus. That was too loose because it mixed working notes, references, and setup files with the actual intended research documents.

The intended knowledge base was reset to:

- `C:\Users\bryan\OneDrive\Desktop\xponance_research\knowledge_base`

This required updating configuration and then checking whether the live MCP process actually respected the change. That turned into one of the most important lessons from the session: changing `.env` is not enough if the live MCP process is still running with stale state.

The difference between `configured corpus` and `active corpus` became central to the workflow.

## 2026-04-01 - Built a repo-local agent orchestration system

The project now has a more explicit Codex agent structure instead of vague persona prompts.

The system was redesigned around:

- a top-level orchestration contract in `AGENTS.md`
- specialist roles under `.agents/roles/`
- artifact contracts under `.agents/templates/`

The main improvement is that the system now thinks in terms of work products instead of personality labels.

The roles now cover:

- `coordinator`
- `corpus-auditor`
- `literature-reviewer`
- `manager-exposure-analyst`
- `portfolio-construction-analyst`
- `index-methodology-designer`
- `implementation-planner`
- `memo-writer`

The template layer now expects concrete outputs such as:

- `question map`
- `corpus gate report`
- `paper extraction sheet`
- `evidence appendix`
- `active-manager calibration plan`
- `rank-vs-two-step test plan`
- `index rulebook outline`
- `FactSet implementation spec`
- `manager memo`

This was a major step forward because it made the system operational. A role is no longer just a theme. It has required inputs, a procedure, required outputs, handoff expectations, and hard stop conditions.

## 2026-04-01 - Added a hard evidence gate

The strongest design choice in the new orchestration system is the hard corpus gate.

Under `MCP-only`, research must stop if:

- the active `data_dir` is wrong
- local source count does not match synced document count
- the requested source is not in the active corpus
- the MCP cannot expose enough state to verify the corpus

This matters because earlier research answers were able to reference files that were not actually in the intended `knowledge_base` folder. That behavior made it obvious that a soft policy was not enough. The system now requires a `corpus_mismatch` style stop instead of continuing with contaminated evidence.

This was the right design move. It is stricter, but it prevents false confidence.

## 2026-04-01 - Diagnosed the corpus mismatch in stages

The corpus mismatch problem turned out to have more than one layer.

First mismatch:

- the configured corpus was `knowledge_base`
- but the live MCP still appeared to be serving from the repo root

That indicated a stale process or stale sync state.

Second mismatch:

- once the dry-run was pointed at `knowledge_base`, the counts still did not line up
- `sources_found` was larger than `documents_prepared`

That meant the local scanner and the document loader did not agree about what was usable.

Third mismatch:

- the bad file was `quality_value/Piotroski.pdf` or `quality_value/Piotroski (1).pdf` depending on the rename state
- the file existed and opened as a PDF
- but it had zero extractable text across all pages

That was the real blocker. The loader logic drops documents whose extracted text is empty, so the file appeared in the source manifest but not in the prepared document set.

The important lesson is that `file exists` is not the same as `document is ingestible`.

## 2026-04-01 - Reached a clean dry-run state

After removing the bad Piotroski PDF from the usable corpus, the dry-run finally passed its local count check:

- `sources_found = 11`
- `documents_prepared = 11`

That means the local knowledge base is now internally consistent at the dry-run stage.

This does not fully finish the repair by itself. The remaining operational steps are still:

1. run the real sync
2. restart Codex
3. verify that live MCP status reports the same `knowledge_base` path and the same document count

Still, getting to `11 == 11` was the key breakthrough because it converted the issue from a fuzzy suspicion into a concrete operational checklist.

## 2026-04-01 - Improved how future research prompts should be written

Another outcome of this session was a clearer way to prompt the system.

The recommended pattern is to specify:

- the role to use
- the evidence policy
- the benchmark scope
- the style scope
- the deliverable type

For example, the system is now designed to handle prompts like:

- use the `corpus-auditor` role first
- use the `coordinator` role for the full Aapryl factor-index project
- use the `portfolio-construction-analyst` role for `Quality Value` in `Russell 1000`

This is better than free-form prompting because it produces bounded artifacts and makes handoffs between research stages more reliable.

## 2026-04-01 - Current state and open follow-ups

Current state:

- the intended KB path is `knowledge_base`
- the local dry-run corpus count now matches the prepared document count
- the repo has a stronger agent orchestration system
- the research workflow is now explicitly `MCP-only` by default
- the project has a hard stop for corpus mismatch

Open follow-ups:

1. run the real Neo4j graph build
2. verify live MCP graph status after the first successful build
3. obtain a text-searchable or OCR'd copy of the Piotroski paper if it is still needed in the knowledge base
4. begin using the new role-based orchestration flow for actual Aapryl research outputs

The overall result of the session is that the project is much less ambiguous than it was at the start. The main architecture, evidence policy, and operating workflow are now explicit. The next step is no longer figuring out what the system is supposed to be. The next step is running it cleanly and using it to produce actual research artifacts.
