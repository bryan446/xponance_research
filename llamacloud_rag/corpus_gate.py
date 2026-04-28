from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

from .config import Settings
from .corpus import build_source_manifest, compute_corpus_hash


@dataclass(frozen=True)
class CorpusGateResult:
    ok: bool
    error_type: str | None
    reason: str | None
    data_dir: str
    corpus_hash: str
    local_sources: int
    local_chunks: int | None
    graph_sources: int | None
    graph_chunks: int | None

    def to_payload(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["corpus_ready"] = self.ok
        return payload


def _source_count(state: dict[str, Any]) -> int | None:
    if "source_paths" in state:
        return len(state.get("source_paths", []))
    return None


def _chunk_count(state: dict[str, Any]) -> int | None:
    chunk_ids = state.get("chunk_ids")
    if chunk_ids is not None:
        return len(chunk_ids)
    doc_ids = state.get("doc_ids")
    if doc_ids is not None:
        return len(doc_ids)
    return None


def evaluate_corpus_gate(
    settings: Settings,
    *,
    graph_state: dict[str, Any] | None = None,
    require_graph: bool = False,
) -> CorpusGateResult:
    manifest = build_source_manifest(settings)
    corpus_hash = compute_corpus_hash(manifest)
    local_sources = len(manifest)

    if graph_state is None:
        graph_state = {}

    graph_sources = _source_count(graph_state)
    graph_chunks = _chunk_count(graph_state)

    checks: list[tuple[bool, str]] = []

    graph_data_dir = graph_state.get("data_dir")
    if graph_state and graph_data_dir and str(settings.data_dir) != str(graph_data_dir):
        checks.append(
            (
                False,
                "Configured corpus path does not match the active Neo4j graph state.",
            )
        )

    if require_graph and not graph_state:
        checks.append((False, "Neo4j graph has not been built for the active corpus."))
    elif require_graph and graph_sources is None:
        checks.append((False, "Neo4j graph state is missing source inventory."))
    elif require_graph and graph_sources != local_sources:
        checks.append(
            (
                False,
                "Local source count does not match the Neo4j graph state.",
            )
        )

    if require_graph and graph_state.get("corpus_hash") not in (None, corpus_hash):
        checks.append(
            (
                False,
                "Local corpus hash does not match the Neo4j graph state.",
            )
        )

    failure = next((reason for ok, reason in checks if not ok), None)
    return CorpusGateResult(
        ok=failure is None,
        error_type=None if failure is None else "corpus_mismatch",
        reason=failure,
        data_dir=str(settings.data_dir),
        corpus_hash=corpus_hash,
        local_sources=local_sources,
        local_chunks=None,
        graph_sources=graph_sources,
        graph_chunks=graph_chunks,
    )
