from __future__ import annotations

from neo4j_graphrag.experimental.components.schema import (
    GraphSchema,
    NodeType,
    Pattern,
    PropertyType,
    RelationshipType,
)
from neo4j_graphrag.experimental.components.types import LexicalGraphConfig


ENTITY_LABELS: tuple[str, ...] = (
    "PROVIDER",
    "PAPER",
    "STYLE",
    "BENCHMARK",
    "SIGNAL",
    "METHOD",
    "CONSTRAINT",
    "METRIC",
    "DATA_SOURCE",
    "IMPLEMENTATION_STEP",
)

RELATION_LABELS: tuple[str, ...] = (
    "DEFINES",
    "USES",
    "COMPARES",
    "CONSTRAINS",
    "MEASURES",
    "OVERLAYS_ON",
    "REQUIRES",
    "DOCUMENTS",
)

KG_VALIDATION_SCHEMA: tuple[tuple[str, str, str], ...] = (
    ("PROVIDER", "DEFINES", "STYLE"),
    ("PROVIDER", "DOCUMENTS", "METHOD"),
    ("PROVIDER", "DOCUMENTS", "CONSTRAINT"),
    ("PROVIDER", "DOCUMENTS", "BENCHMARK"),
    ("PAPER", "DOCUMENTS", "STYLE"),
    ("PAPER", "DOCUMENTS", "SIGNAL"),
    ("PAPER", "DOCUMENTS", "METHOD"),
    ("PAPER", "DOCUMENTS", "CONSTRAINT"),
    ("STYLE", "USES", "SIGNAL"),
    ("STYLE", "USES", "METHOD"),
    ("STYLE", "CONSTRAINS", "CONSTRAINT"),
    ("STYLE", "OVERLAYS_ON", "BENCHMARK"),
    ("STYLE", "REQUIRES", "DATA_SOURCE"),
    ("STYLE", "REQUIRES", "IMPLEMENTATION_STEP"),
    ("SIGNAL", "MEASURES", "METRIC"),
    ("METHOD", "USES", "SIGNAL"),
    ("METHOD", "COMPARES", "METHOD"),
    ("METHOD", "CONSTRAINS", "CONSTRAINT"),
    ("IMPLEMENTATION_STEP", "REQUIRES", "DATA_SOURCE"),
    ("IMPLEMENTATION_STEP", "REQUIRES", "METHOD"),
)

LEXICAL_GRAPH_CONFIG = LexicalGraphConfig(
    document_node_label="Document",
    chunk_node_label="Chunk",
    chunk_to_document_relationship_type="FROM_DOCUMENT",
    next_chunk_relationship_type="NEXT_CHUNK",
    node_to_chunk_relationship_type="FROM_CHUNK",
    chunk_id_property="id",
    chunk_index_property="chunk_index",
    chunk_text_property="text",
)

_NAME_PROPERTY = [PropertyType(name="name", type="STRING", required=True)]

NODE_DESCRIPTIONS: dict[str, str] = {
    "PROVIDER": "Index provider or benchmark publisher referenced in the research corpus.",
    "PAPER": "Research paper, white paper, or methodology note referenced in the corpus.",
    "STYLE": "Named investment style or factor sleeve described in the corpus.",
    "BENCHMARK": "Benchmark or parent universe used in methodology construction.",
    "SIGNAL": "Observable input signal or descriptor used in scoring or screening.",
    "METHOD": "Construction method, weighting method, ranking rule, or implementation procedure.",
    "CONSTRAINT": "Portfolio, turnover, liquidity, sector, or region constraint.",
    "METRIC": "Named metric, ratio, or formula used by a signal or method.",
    "DATA_SOURCE": "Named data source, vendor field, or required dataset.",
    "IMPLEMENTATION_STEP": "Operational step required to implement the methodology.",
}

RELATION_DESCRIPTIONS: dict[str, str] = {
    "DEFINES": "Defines or formally introduces a style, benchmark, or method.",
    "USES": "Uses a signal, metric, or method as an input or dependency.",
    "COMPARES": "Explicitly compares two methods or approaches.",
    "CONSTRAINS": "Applies a stated constraint or limit.",
    "MEASURES": "Measures a concept with a named metric or ratio.",
    "OVERLAYS_ON": "Applies on top of a benchmark or parent universe.",
    "REQUIRES": "Requires a data source or implementation dependency.",
    "DOCUMENTS": "Documents or describes a concept in source material.",
}


def build_graph_schema() -> GraphSchema:
    node_types = tuple(
        NodeType(
            label=label,
            description=NODE_DESCRIPTIONS[label],
            properties=list(_NAME_PROPERTY),
            additional_properties=True,
        )
        for label in ENTITY_LABELS
    )
    relationship_types = tuple(
        RelationshipType(
            label=label,
            description=RELATION_DESCRIPTIONS[label],
            additional_properties=False,
        )
        for label in RELATION_LABELS
    )
    patterns = tuple(
        Pattern(source=source, relationship=relationship, target=target)
        for source, relationship, target in KG_VALIDATION_SCHEMA
    )
    return GraphSchema(
        node_types=node_types,
        relationship_types=relationship_types,
        patterns=patterns,
        additional_node_types=False,
        additional_relationship_types=False,
        additional_patterns=False,
    )
