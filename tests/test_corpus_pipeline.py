from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from llamacloud_rag.config import Settings
from llamacloud_rag.corpus import (
    build_source_manifest,
    compute_corpus_hash,
    load_documents,
)
from llamacloud_rag.corpus_gate import evaluate_corpus_gate
from llamacloud_rag.graph_schema import build_graph_schema


def make_settings(data_dir: Path) -> Settings:
    return Settings(
        repo_root=data_dir,
        data_dir=data_dir,
        graph_state_path=data_dir / ".neo4j_graph_state.json",
        openai_api_key=None,
        llama_parse_api_key=None,
        app_name="xponance-research",
        default_top_k=5,
        allowed_extensions=(".md", ".pdf"),
        excluded_dirs=frozenset(),
        chunk_size=512,
        chunk_overlap=32,
        llama_parse_result_type="markdown",
        graph_llm_model="gpt-4o",
        neo4j_uri=None,
        neo4j_username=None,
        neo4j_password=None,
        neo4j_database="neo4j",
    )


class CorpusPipelineTests(unittest.TestCase):
    def test_manifest_hash_changes_when_file_content_changes(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            data_dir = Path(tmpdir)
            (data_dir / "note.md").write_text("# Title\n\nhello world\n", encoding="utf-8")
            settings = make_settings(data_dir)

            original_manifest = build_source_manifest(settings)
            original_hash = compute_corpus_hash(original_manifest)

            (data_dir / "note.md").write_text("# Title\n\nhello again\n", encoding="utf-8")

            updated_manifest = build_source_manifest(settings)
            updated_hash = compute_corpus_hash(updated_manifest)

            self.assertNotEqual(original_hash, updated_hash)

    def test_load_documents_preserves_chunk_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            data_dir = Path(tmpdir)
            (data_dir / "guide.md").write_text(
                "# Heading\n\nParagraph one.\n\n## Subheading\n\nParagraph two.\n",
                encoding="utf-8",
            )
            settings = make_settings(data_dir)

            documents = load_documents(settings)

            self.assertTrue(documents)
            first_document = documents[0]
            self.assertEqual(first_document.metadata["source_path"], "guide.md")
            self.assertEqual(first_document.metadata["collection"], "root")
            self.assertGreaterEqual(first_document.metadata["chunk_index"], 1)
            self.assertGreaterEqual(first_document.metadata["chunk_total"], 1)
            self.assertTrue(first_document.id_.startswith("chunk:guide.md:"))

    def test_corpus_gate_detects_hash_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            data_dir = Path(tmpdir)
            (data_dir / "guide.md").write_text("# Heading\n\nBody.\n", encoding="utf-8")
            settings = make_settings(data_dir)
            manifest = build_source_manifest(settings)
            corpus_hash = compute_corpus_hash(manifest)

            matching_state = {
                "data_dir": str(data_dir),
                "corpus_hash": corpus_hash,
                "source_paths": ["guide.md"],
                "chunk_ids": ["chunk:guide.md:0001"],
            }

            matching_result = evaluate_corpus_gate(
                settings,
                graph_state=matching_state,
                require_graph=True,
            )
            self.assertTrue(matching_result.ok)

            mismatched_result = evaluate_corpus_gate(
                settings,
                graph_state={**matching_state, "corpus_hash": "bad-hash"},
                require_graph=True,
            )
            self.assertFalse(mismatched_result.ok)
            self.assertEqual(mismatched_result.error_type, "corpus_mismatch")

    def test_graph_schema_disallows_additional_types(self) -> None:
        schema = build_graph_schema()
        self.assertFalse(schema.additional_node_types)
        self.assertFalse(schema.additional_relationship_types)
        self.assertFalse(schema.additional_patterns)
        self.assertTrue(schema.patterns)


if __name__ == "__main__":
    unittest.main()
