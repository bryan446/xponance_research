from __future__ import annotations

from functools import lru_cache

from mcp.server.fastmcp import FastMCP

from .bootstrap import load_state
from .config import Settings, get_settings
from .corpus import build_source_manifest, compute_corpus_hash, load_documents
from .corpus_gate import evaluate_corpus_gate
from .graph_backend import get_graph_status, search_graph


mcp = FastMCP("xponance-research")


@lru_cache(maxsize=1)
def _settings() -> Settings:
    return get_settings()


def _default_top_k(top_k: int) -> int:
    settings = _settings()
    if top_k <= 0:
        top_k = settings.default_top_k

    if top_k < 1 or top_k > 20:
        raise ValueError("top_k must be between 1 and 20.")

    return top_k


def _default_path_depth(path_depth: int) -> int:
    if path_depth <= 0:
        path_depth = 2
    if path_depth < 1 or path_depth > 4:
        raise ValueError("path_depth must be between 1 and 4.")
    return path_depth


def _corpus_gate(require_graph: bool = True) -> dict[str, object] | None:
    settings = _settings()
    graph_state = load_state(settings.graph_state_path)
    gate = evaluate_corpus_gate(
        settings,
        graph_state=graph_state,
        require_graph=require_graph,
    )
    if gate.ok:
        return None
    return gate.to_payload()


def _corpus_mismatch_payload(
    *,
    query: str | None,
    require_graph: bool,
    answer_mode: str | None = None,
) -> dict[str, object]:
    settings = _settings()
    gate_payload = _corpus_gate(require_graph=require_graph) or {}
    payload: dict[str, object] = {
        "query": query,
        "app_name": settings.app_name,
        "error_type": "corpus_mismatch",
        "reason": gate_payload.get("reason"),
        "corpus_gate": gate_payload,
        "results": [],
        "references": [],
    }
    if answer_mode is not None:
        payload["answer"] = None
        payload["answer_mode"] = answer_mode
        payload["evidence"] = []
    return payload


@mcp.tool()
def search_xponance_graph(
    query: str,
    top_k: int = 0,
    path_depth: int = 0,
) -> dict[str, object]:
    """Search the finished Neo4j knowledge graph and return path-plus-chunk evidence."""
    settings = _settings()
    top_k = _default_top_k(top_k)
    path_depth = _default_path_depth(path_depth)

    gate_payload = _corpus_gate(require_graph=True)
    if gate_payload is not None:
        return _corpus_mismatch_payload(query=query, require_graph=True)

    try:
        payload = search_graph(
            settings,
            query=query,
            top_k=top_k,
            path_depth=path_depth,
            text_limit=900,
        )
    except Exception as exc:  # pragma: no cover - depends on environment/services
        return {
            "query": query,
            "error_type": "graph_unavailable",
            "reason": str(exc),
            "results": [],
            "references": [],
            "graph_status": get_graph_status(settings),
        }

    payload.update(
        {
            "app_name": settings.app_name,
            "graph_status": get_graph_status(settings),
            "corpus_gate": {"corpus_ready": True},
        }
    )
    return payload


@mcp.tool()
def answer_xponance_graph(
    query: str,
    top_k: int = 0,
    path_depth: int = 0,
    citation_chunk_size: int = 512,
) -> dict[str, object]:
    """Return graph retrieval evidence only. MCP clients should synthesize final prose."""
    settings = _settings()
    top_k = _default_top_k(top_k)
    path_depth = _default_path_depth(path_depth)
    if citation_chunk_size < 128:
        raise ValueError("citation_chunk_size must be at least 128.")

    gate_payload = _corpus_gate(require_graph=True)
    if gate_payload is not None:
        return _corpus_mismatch_payload(
            query=query,
            require_graph=True,
            answer_mode="retrieval_only",
        )

    try:
        payload = search_graph(
            settings,
            query=query,
            top_k=top_k,
            path_depth=path_depth,
            text_limit=citation_chunk_size,
        )
    except Exception as exc:  # pragma: no cover - depends on environment/services
        return {
            "query": query,
            "app_name": settings.app_name,
            "answer": None,
            "answer_mode": "retrieval_only",
            "error_type": "graph_unavailable",
            "reason": str(exc),
            "results": [],
            "references": [],
            "evidence": [],
            "graph_status": get_graph_status(settings),
        }

    payload.update(
        {
            "app_name": settings.app_name,
            "answer": None,
            "answer_mode": "retrieval_only",
            "evidence": payload.get("results", []),
            "graph_status": get_graph_status(settings),
            "corpus_gate": {"corpus_ready": True},
        }
    )
    return payload


@mcp.tool()
def get_xponance_research_graph_status() -> dict[str, object]:
    """Inspect Neo4j graph readiness, freshness, and dependency status."""
    settings = _settings()
    payload = get_graph_status(settings)
    payload["corpus_gate"] = evaluate_corpus_gate(
        settings,
        graph_state=load_state(settings.graph_state_path),
        require_graph=True,
    ).to_payload()
    return payload


@mcp.tool()
def get_xponance_research_index_status() -> dict[str, object]:
    """Inspect the configured corpus, chunk inventory, and last graph build state."""
    settings = _settings()
    state = load_state(settings.graph_state_path)
    manifest = build_source_manifest(settings)
    corpus_hash = compute_corpus_hash(manifest)
    local_chunks = len(load_documents(settings))
    gate = evaluate_corpus_gate(
        settings,
        graph_state=state,
        require_graph=True,
    )

    return {
        "app_name": settings.app_name,
        "data_dir": str(settings.data_dir),
        "state_file": str(settings.graph_state_path),
        "primary_store": "neo4j",
        "sources_available_locally": len(manifest),
        "chunks_available_locally": local_chunks,
        "sources_sample": manifest[:10],
        "corpus_hash": corpus_hash,
        "last_sync": state.get("updated_at"),
        "last_synced_documents": len(state.get("source_paths", [])),
        "last_synced_chunks": len(state.get("chunk_ids", [])),
        "entity_count": state.get("entity_count"),
        "relationship_count": state.get("relationship_count"),
        "corpus_gate": gate.to_payload(),
    }


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
