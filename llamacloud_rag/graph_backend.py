from __future__ import annotations

import asyncio
from collections import defaultdict
from datetime import datetime, timezone
from importlib import import_module
from typing import Any

from .bootstrap import load_state, save_state
from .config import Settings, require_neo4j_settings, require_openai_api_key
from .corpus import build_source_manifest, compute_corpus_hash, load_documents
from .graph_schema import (
    ENTITY_LABELS,
    KG_VALIDATION_SCHEMA,
    LEXICAL_GRAPH_CONFIG,
    RELATION_LABELS,
    build_graph_schema,
)

INTERNAL_LABELS = {"__Entity__", "__KGBuilder__", "Document", "Chunk"}
ENTITY_SEARCH_INDEX = "xponance_entity_search"
CHUNK_SEARCH_INDEX = "xponance_chunk_search"


def _import_dependency(module_name: str, package_name: str) -> Any:
    try:
        return import_module(module_name)
    except ImportError as exc:  # pragma: no cover - environment specific
        raise ImportError(
            f"Install `{package_name}` to enable the Neo4j graph workflow."
        ) from exc


def graph_dependency_status() -> dict[str, Any]:
    retrieval_dependencies = {
        "neo4j": "neo4j",
    }
    build_dependencies = {
        "neo4j_graphrag": "neo4j-graphrag[openai,experimental]",
        "neo4j_graphrag.llm": "neo4j-graphrag[openai,experimental]",
    }
    optional_dependencies = {
        "llama_parse": "llama-parse",
    }

    retrieval_missing: list[str] = []
    build_missing: list[str] = []
    optional_missing: list[str] = []

    for module_name, package_name in retrieval_dependencies.items():
        try:
            import_module(module_name)
        except ImportError:
            retrieval_missing.append(package_name)

    for module_name, package_name in build_dependencies.items():
        try:
            import_module(module_name)
        except ImportError:
            build_missing.append(package_name)

    for module_name, package_name in optional_dependencies.items():
        try:
            import_module(module_name)
        except ImportError:
            optional_missing.append(package_name)

    return {
        "retrieval_ready": not retrieval_missing,
        "build_ready": not retrieval_missing and not build_missing,
        "missing": {
            "retrieval": retrieval_missing,
            "build": build_missing,
            "optional": optional_missing,
        },
    }


def connect_graph_driver(settings: Settings) -> Any:
    neo4j = _import_dependency("neo4j", "neo4j")
    uri, username, password, _database = require_neo4j_settings(settings)
    return neo4j.GraphDatabase.driver(uri, auth=(username, password))


def get_graph_llm(settings: Settings) -> Any:
    llm_module = _import_dependency("neo4j_graphrag.llm", "neo4j-graphrag[openai,experimental]")
    return llm_module.OpenAILLM(
        model_name=settings.graph_llm_model,
        model_params={"temperature": 0.0},
        api_key=require_openai_api_key(settings),
    )


def _sorted_source_documents(documents: list[Any]) -> dict[str, list[Any]]:
    grouped_documents: defaultdict[str, list[Any]] = defaultdict(list)
    for document in documents:
        source_path = document.metadata.get("source_path")
        if source_path:
            grouped_documents[str(source_path)].append(document)

    for source_documents in grouped_documents.values():
        source_documents.sort(key=lambda item: int(item.metadata.get("chunk_index", 0)))

    return dict(grouped_documents)


def _entity_primary_label(labels: list[str] | tuple[str, ...]) -> str | None:
    for label in labels:
        if label not in INTERNAL_LABELS:
            return label
    return None


def _truncate(text: str, *, limit: int) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 3].rstrip() + "..."


def _serialize_chunk_node(node: Any, *, text_limit: int) -> dict[str, Any]:
    properties = dict(node.items())
    source_path = properties.get("source_path") or properties.get("path")
    page_label = properties.get("page_label")
    citation = (
        f"{source_path} (page {page_label})"
        if page_label not in (None, "")
        else str(source_path)
    )
    return {
        "chunk_id": properties.get("id"),
        "source_path": source_path,
        "source_name": properties.get("source_name"),
        "collection": properties.get("collection"),
        "page_label": page_label,
        "chunk_index": properties.get("chunk_index"),
        "chunk_total": properties.get("chunk_total"),
        "citation": citation,
        "text": _truncate(str(properties.get("text", "")), limit=text_limit),
    }


def _serialize_entity_node(node: Any) -> dict[str, Any]:
    properties = dict(node.items())
    labels = sorted(label for label in node.labels if label not in {"__KGBuilder__"})
    return {
        "element_id": node.element_id,
        "labels": labels,
        "primary_label": _entity_primary_label(labels),
        "name": properties.get("name") or properties.get("path"),
        "properties": properties,
    }


def _chunk_evidence_for_entity(session: Any, entity_element_id: str, *, limit: int) -> list[dict[str, Any]]:
    records = session.run(
        """
        MATCH (entity:__Entity__)-[:FROM_CHUNK]->(chunk:Chunk)
        WHERE elementId(entity) = $entity_element_id
        RETURN DISTINCT chunk
        ORDER BY chunk.source_path ASC, chunk.chunk_index ASC
        LIMIT $limit
        """,
        entity_element_id=entity_element_id,
        limit=limit,
    )
    return [_serialize_chunk_node(record["chunk"], text_limit=900) for record in records]


def _chunk_support_for_edge(
    session: Any,
    start_element_id: str,
    end_element_id: str,
    *,
    limit: int,
    text_limit: int,
) -> list[dict[str, Any]]:
    records = session.run(
        """
        MATCH (start:__Entity__)-[:FROM_CHUNK]->(chunk:Chunk)<-[:FROM_CHUNK]-(end:__Entity__)
        WHERE elementId(start) = $start_element_id
          AND elementId(end) = $end_element_id
        RETURN DISTINCT chunk
        ORDER BY chunk.source_path ASC, chunk.chunk_index ASC
        LIMIT $limit
        """,
        start_element_id=start_element_id,
        end_element_id=end_element_id,
        limit=limit,
    )
    return [_serialize_chunk_node(record["chunk"], text_limit=text_limit) for record in records]


def _serialize_path(
    session: Any,
    path: Any,
    *,
    rank: int,
    score: float | None,
    text_limit: int,
) -> dict[str, Any]:
    nodes = [_serialize_entity_node(node) for node in path.nodes]
    relationships: list[dict[str, Any]] = []
    supporting_chunks: dict[tuple[str | None, str | None, str | None], dict[str, Any]] = {}

    for relationship in path.relationships:
        start_node = _serialize_entity_node(relationship.start_node)
        end_node = _serialize_entity_node(relationship.end_node)
        edge_chunks = _chunk_support_for_edge(
            session,
            relationship.start_node.element_id,
            relationship.end_node.element_id,
            limit=5,
            text_limit=text_limit,
        )
        for chunk in edge_chunks:
            key = (
                chunk.get("source_path"),
                str(chunk.get("page_label")),
                chunk.get("chunk_id"),
            )
            supporting_chunks[key] = chunk
        relationships.append(
            {
                "type": relationship.type,
                "start_node_id": relationship.start_node.element_id,
                "end_node_id": relationship.end_node.element_id,
                "start_name": start_node.get("name"),
                "end_name": end_node.get("name"),
                "chunks": edge_chunks,
            }
        )

    if not relationships and nodes:
        for chunk in _chunk_evidence_for_entity(session, nodes[0]["element_id"], limit=5):
            key = (
                chunk.get("source_path"),
                str(chunk.get("page_label")),
                chunk.get("chunk_id"),
            )
            supporting_chunks[key] = chunk

    return {
        "rank": rank,
        "score": score,
        "path": {
            "nodes": nodes,
            "relationships": relationships,
        },
        "supporting_chunks": list(supporting_chunks.values()),
    }


def _collect_references(path_results: list[dict[str, Any]]) -> list[dict[str, Any]]:
    ordered: dict[tuple[str | None, str | None, str | None], dict[str, Any]] = {}
    for result in path_results:
        for chunk in result.get("supporting_chunks", []):
            key = (
                chunk.get("source_path"),
                str(chunk.get("page_label")),
                chunk.get("chunk_id"),
            )
            if key in ordered:
                continue
            ordered[key] = {
                "source_path": chunk.get("source_path"),
                "source_name": chunk.get("source_name"),
                "page_label": chunk.get("page_label"),
                "chunk_id": chunk.get("chunk_id"),
                "citation": chunk.get("citation"),
            }
    return list(ordered.values())


def _semantic_path_query(path_depth: int) -> str:
    return f"""
    MATCH (seed:__Entity__)
    WHERE elementId(seed) = $seed_id
    OPTIONAL MATCH path = (seed)-[rels*1..{path_depth}]-(neighbor:__Entity__)
    WHERE ALL(rel IN rels WHERE type(rel) IN $semantic_relationship_types)
    RETURN path
    LIMIT $limit
    """


def _query_seed_entities(session: Any, query: str, *, top_k: int) -> list[dict[str, Any]]:
    records = session.run(
        """
        CALL {
            CALL db.index.fulltext.queryNodes($entity_index_name, $query) YIELD node, score
            WHERE node:__Entity__
            RETURN elementId(node) AS entity_id, score
            UNION
            CALL db.index.fulltext.queryNodes($chunk_index_name, $query) YIELD node, score
            MATCH (entity:__Entity__)-[:FROM_CHUNK]->(node)
            RETURN elementId(entity) AS entity_id, score * 0.7 AS score
        }
        MATCH (entity:__Entity__)
        WHERE elementId(entity) = entity_id
        RETURN entity, max(score) AS score
        ORDER BY score DESC, coalesce(entity.name, '') ASC
        LIMIT $top_k
        """,
        entity_index_name=ENTITY_SEARCH_INDEX,
        chunk_index_name=CHUNK_SEARCH_INDEX,
        query=query,
        top_k=top_k,
    )
    return [{"node": record["entity"], "score": float(record["score"])} for record in records]


def _query_matching_chunks(session: Any, query: str, *, top_k: int, text_limit: int) -> list[dict[str, Any]]:
    records = session.run(
        """
        CALL db.index.fulltext.queryNodes($chunk_index_name, $query) YIELD node, score
        RETURN node AS chunk, score
        ORDER BY score DESC, chunk.source_path ASC, chunk.chunk_index ASC
        LIMIT $top_k
        """,
        chunk_index_name=CHUNK_SEARCH_INDEX,
        query=query,
        top_k=top_k,
    )
    results: list[dict[str, Any]] = []
    for record in records:
        chunk_payload = _serialize_chunk_node(record["chunk"], text_limit=text_limit)
        chunk_payload["score"] = float(record["score"])
        results.append(chunk_payload)
    return results


def search_graph(
    settings: Settings,
    *,
    query: str,
    top_k: int,
    path_depth: int,
    text_limit: int = 900,
) -> dict[str, Any]:
    driver = connect_graph_driver(settings)
    try:
        with driver.session(database=settings.neo4j_database) as session:
            seed_entities = _query_seed_entities(session, query, top_k=top_k)
            matching_chunks = _query_matching_chunks(session, query, top_k=top_k, text_limit=text_limit)

            seen_signatures: set[tuple[str, ...]] = set()
            results: list[dict[str, Any]] = []

            for seed_rank, seed in enumerate(seed_entities, start=1):
                paths = session.run(
                    _semantic_path_query(path_depth),
                    seed_id=seed["node"].element_id,
                    semantic_relationship_types=list(RELATION_LABELS),
                    limit=max(1, top_k),
                )
                materialized_paths = [record["path"] for record in paths if record.get("path") is not None]

                if not materialized_paths:
                    singleton_result = {
                        "rank": len(results) + 1,
                        "score": seed["score"],
                        "path": {
                            "nodes": [_serialize_entity_node(seed["node"])],
                            "relationships": [],
                        },
                        "supporting_chunks": _chunk_evidence_for_entity(
                            session,
                            seed["node"].element_id,
                            limit=5,
                        ),
                    }
                    signature = tuple(node["element_id"] for node in singleton_result["path"]["nodes"])
                    if signature not in seen_signatures:
                        seen_signatures.add(signature)
                        results.append(singleton_result)
                    continue

                for path in materialized_paths:
                    signature = tuple(
                        [node.element_id for node in path.nodes]
                        + [relationship.type for relationship in path.relationships]
                    )
                    if signature in seen_signatures:
                        continue
                    seen_signatures.add(signature)
                    results.append(
                        _serialize_path(
                            session,
                            path,
                            rank=len(results) + 1,
                            score=seed["score"],
                            text_limit=text_limit,
                        )
                    )
                    if len(results) >= top_k:
                        break
                if len(results) >= top_k:
                    break

            return {
                "query": query,
                "results": results[:top_k],
                "references": _collect_references(results[:top_k])
                or [
                    {
                        "source_path": chunk.get("source_path"),
                        "source_name": chunk.get("source_name"),
                        "page_label": chunk.get("page_label"),
                        "chunk_id": chunk.get("chunk_id"),
                        "citation": chunk.get("citation"),
                    }
                    for chunk in matching_chunks
                ],
                "matching_chunks": matching_chunks,
            }
    finally:
        driver.close()


def query_graph_counts(settings: Settings) -> dict[str, int]:
    driver = connect_graph_driver(settings)
    try:
        with driver.session(database=settings.neo4j_database) as session:
            lexical_documents = session.run(
                "MATCH (n:Document) RETURN count(n) AS count"
            ).single()["count"]
            lexical_chunks = session.run(
                "MATCH (n:Chunk) RETURN count(n) AS count"
            ).single()["count"]
            ontology_nodes = session.run(
                "MATCH (n:__Entity__) RETURN count(n) AS count"
            ).single()["count"]
            semantic_relationships = session.run(
                """
                MATCH ()-[r]->()
                WHERE type(r) IN $relationship_types
                RETURN count(r) AS count
                """,
                relationship_types=list(RELATION_LABELS),
            ).single()["count"]
    finally:
        driver.close()

    return {
        "lexical_documents": lexical_documents,
        "lexical_chunks": lexical_chunks,
        "entity_count": ontology_nodes,
        "relationship_count": semantic_relationships,
    }


def get_graph_status(settings: Settings) -> dict[str, Any]:
    manifest = build_source_manifest(settings)
    corpus_hash = compute_corpus_hash(manifest)
    state = load_state(settings.graph_state_path)
    dependency_status = graph_dependency_status()
    status: dict[str, Any] = {
        "graph_state_file": str(settings.graph_state_path),
        "graph_ready": False,
        "data_dir": str(settings.data_dir),
        "local_sources": len(manifest),
        "local_corpus_hash": corpus_hash,
        "dependency_status": dependency_status,
        "neo4j_configured": bool(
            settings.neo4j_uri and settings.neo4j_username and settings.neo4j_password
        ),
        "openai_configured_for_build": bool(settings.openai_api_key),
        "last_graph_sync": state.get("updated_at"),
        "graph_source_count": len(state.get("source_paths", [])),
        "graph_chunk_count": len(state.get("chunk_ids", [])),
        "graph_corpus_hash": state.get("corpus_hash"),
    }

    if not dependency_status["retrieval_ready"]:
        status["graph_error"] = (
            "Graph retrieval packages are not installed. "
            f"Missing: {', '.join(dependency_status['missing']['retrieval'])}"
        )
        return status

    if not status["neo4j_configured"]:
        status["graph_error"] = "Neo4j credentials are not configured."
        return status

    try:
        status.update(query_graph_counts(settings))
        status["graph_ready"] = True
    except Exception as exc:  # pragma: no cover - external service behavior
        status["graph_error"] = str(exc)

    return status


def _reset_database(session: Any) -> None:
    session.run("MATCH (n) DETACH DELETE n")


def _ensure_indexes(session: Any) -> None:
    session.run(
        f"""
        CREATE FULLTEXT INDEX {ENTITY_SEARCH_INDEX} IF NOT EXISTS
        FOR (n:__Entity__) ON EACH [n.name, n.description]
        """
    )
    session.run(
        f"""
        CREATE FULLTEXT INDEX {CHUNK_SEARCH_INDEX} IF NOT EXISTS
        FOR (n:Chunk) ON EACH [n.text, n.source_path, n.source_name]
        """
    )
    session.run("CREATE INDEX document_path IF NOT EXISTS FOR (n:Document) ON (n.path)")
    session.run("CREATE INDEX chunk_source_path IF NOT EXISTS FOR (n:Chunk) ON (n.source_path)")
    session.run("CREATE INDEX chunk_page_label IF NOT EXISTS FOR (n:Chunk) ON (n.page_label)")


def _build_document_info(settings: Settings, source_documents: list[Any], corpus_hash: str) -> Any:
    types_module = _import_dependency(
        "neo4j_graphrag.experimental.components.types",
        "neo4j-graphrag[openai,experimental]",
    )
    source_metadata = dict(source_documents[0].metadata)
    document_metadata = {
        "source_path": source_metadata.get("source_path"),
        "source_name": source_metadata.get("source_name"),
        "source_extension": source_metadata.get("source_extension"),
        "collection": source_metadata.get("collection"),
        "app_name": settings.app_name,
        "corpus_hash": corpus_hash,
    }
    return types_module.DocumentInfo(
        path=str(source_metadata.get("source_path")),
        metadata=document_metadata,
        uid=str(source_metadata.get("source_document_id")),
    )


def _build_text_chunks(source_documents: list[Any], corpus_hash: str) -> Any:
    types_module = _import_dependency(
        "neo4j_graphrag.experimental.components.types",
        "neo4j-graphrag[openai,experimental]",
    )
    chunks: list[Any] = []
    for document in source_documents:
        metadata = dict(document.metadata)
        metadata["id"] = document.id_
        metadata["corpus_hash"] = corpus_hash
        chunks.append(
            types_module.TextChunk(
                text=str(document.text),
                index=int(metadata.get("chunk_index", 0)),
                metadata=metadata,
                uid=document.id_,
            )
        )
    return types_module.TextChunks(chunks=chunks)


async def _run_source_pipeline(
    extractor: Any,
    writer: Any,
    *,
    text_chunks: Any,
    document_info: Any,
    graph_schema: Any,
) -> dict[str, Any]:
    graph = await extractor.run(
        chunks=text_chunks,
        document_info=document_info,
        lexical_graph_config=LEXICAL_GRAPH_CONFIG,
        schema=graph_schema,
    )
    result = await writer.run(graph, lexical_graph_config=LEXICAL_GRAPH_CONFIG)
    return dict(result.metadata)


def _build_domain_graph(settings: Settings, documents: list[Any], corpus_hash: str) -> None:
    extractor_module = _import_dependency(
        "neo4j_graphrag.experimental.components.entity_relation_extractor",
        "neo4j-graphrag[openai,experimental]",
    )
    writer_module = _import_dependency(
        "neo4j_graphrag.experimental.components.kg_writer",
        "neo4j-graphrag[openai,experimental]",
    )

    graph_schema = build_graph_schema()
    extractor = extractor_module.LLMEntityRelationExtractor(
        llm=get_graph_llm(settings),
        create_lexical_graph=True,
        use_structured_output=False,
    )
    writer = writer_module.Neo4jWriter(
        driver=connect_graph_driver(settings),
        neo4j_database=settings.neo4j_database,
        clean_db=True,
    )

    try:
        for source_path, source_documents in _sorted_source_documents(documents).items():
            del source_path
            text_chunks = _build_text_chunks(source_documents, corpus_hash)
            document_info = _build_document_info(settings, source_documents, corpus_hash)
            asyncio.run(
                _run_source_pipeline(
                    extractor,
                    writer,
                    text_chunks=text_chunks,
                    document_info=document_info,
                    graph_schema=graph_schema,
                )
            )
    finally:
        writer.driver.close()


def _resolve_domain_entities(settings: Settings) -> str | None:
    resolver_module = _import_dependency(
        "neo4j_graphrag.experimental.components.resolver",
        "neo4j-graphrag[openai,experimental]",
    )
    driver = connect_graph_driver(settings)
    try:
        resolver = resolver_module.SinglePropertyExactMatchResolver(
            driver=driver,
            resolve_property="name",
            neo4j_database=settings.neo4j_database,
        )
        stats = asyncio.run(resolver.run())
        return (
            "Resolved duplicate semantic entities by exact name match. "
            f"Input nodes: {stats.number_of_nodes_to_resolve}, "
            f"result nodes: {stats.number_of_created_nodes}."
        )
    except Exception as exc:  # pragma: no cover - depends on Neo4j/APOC
        return f"Entity resolution skipped: {exc}"
    finally:
        driver.close()


def rebuild_graph(
    settings: Settings,
    *,
    dry_run: bool = False,
    rebuild: bool = False,
) -> dict[str, Any]:
    manifest = build_source_manifest(settings)
    corpus_hash = compute_corpus_hash(manifest)
    documents = load_documents(settings)
    current_chunk_ids = sorted(document.id_ for document in documents)
    current_source_paths = sorted(
        {
            document.metadata.get("source_path")
            for document in documents
            if document.metadata.get("source_path")
        }
    )
    previous_state = load_state(settings.graph_state_path)

    summary: dict[str, Any] = {
        "graph_state_file": str(settings.graph_state_path),
        "data_dir": str(settings.data_dir),
        "sources_found": len(manifest),
        "chunks_prepared": len(documents),
        "corpus_hash": corpus_hash,
        "source_manifest": manifest,
        "schema_patterns": list(KG_VALIDATION_SCHEMA),
    }

    if dry_run:
        return summary

    if not documents:
        raise ValueError("No chunked corpus documents were prepared for graph sync.")

    dependency_status = graph_dependency_status()
    if not dependency_status["build_ready"]:
        raise ImportError(
            "Graph build dependencies are missing: "
            f"{', '.join(dependency_status['missing']['build'])}"
        )

    require_openai_api_key(settings)

    if (
        not rebuild
        and previous_state.get("corpus_hash") == corpus_hash
        and previous_state.get("source_paths") == current_source_paths
    ):
        counts = query_graph_counts(settings)
        summary.update(
            {
                "skipped": True,
                "skip_reason": "Graph state already matches the active corpus hash.",
                **counts,
            }
        )
        return summary

    driver = connect_graph_driver(settings)
    try:
        with driver.session(database=settings.neo4j_database) as session:
            _reset_database(session)
    finally:
        driver.close()

    _build_domain_graph(settings, documents, corpus_hash)
    entity_resolution_note = _resolve_domain_entities(settings)

    driver = connect_graph_driver(settings)
    try:
        with driver.session(database=settings.neo4j_database) as session:
            _ensure_indexes(session)
    finally:
        driver.close()

    counts = query_graph_counts(settings)

    state_payload = {
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "data_dir": str(settings.data_dir),
        "corpus_hash": corpus_hash,
        "source_paths": current_source_paths,
        "chunk_ids": current_chunk_ids,
        "doc_ids": current_chunk_ids,
        "entity_count": counts["entity_count"],
        "relationship_count": counts["relationship_count"],
    }
    save_state(settings.graph_state_path, state_payload)

    summary.update(counts)
    summary["rebuild_performed"] = True
    if entity_resolution_note is not None:
        summary["entity_resolution_note"] = entity_resolution_note

    return summary
