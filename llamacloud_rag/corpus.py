from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

from pypdf import PdfReader

from .config import Settings


MARKDOWN_HEADING_PATTERN = re.compile(r"(?m)^#{1,6}\s+.+$")
WORD_PATTERN = re.compile(r"\S+")


@dataclass
class Document:
    text: str
    metadata: dict[str, Any] = field(default_factory=dict)
    id_: str | None = None

    def get_content(self, metadata_mode: str | None = None) -> str:
        del metadata_mode
        return self.text


def _is_excluded(path: Path, data_dir: Path, excluded_dirs: frozenset[str]) -> bool:
    relative_parts = path.relative_to(data_dir).parts[:-1]
    return any(part in excluded_dirs for part in relative_parts)


def _is_non_corpus_file(path: Path, data_dir: Path) -> bool:
    relative_path = path.relative_to(data_dir).as_posix()
    return relative_path == "README.md"


def iter_source_files(settings: Settings) -> list[Path]:
    files: list[Path] = []

    for path in settings.data_dir.rglob("*"):
        if not path.is_file():
            continue
        if _is_excluded(path, settings.data_dir, settings.excluded_dirs):
            continue
        if _is_non_corpus_file(path, settings.data_dir):
            continue
        if path.suffix.lower() not in settings.allowed_extensions:
            continue

        files.append(path)

    return sorted(files)


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _text_sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def build_source_metadata(path: Path, data_dir: Path) -> dict[str, Any]:
    relative_path = path.relative_to(data_dir).as_posix()
    relative_parts = Path(relative_path).parts
    collection = relative_parts[0] if len(relative_parts) > 1 else "root"

    return {
        "source_path": relative_path,
        "source_name": path.name,
        "source_extension": path.suffix.lower(),
        "collection": collection,
        "file_name": path.name,
        "source_document_id": f"source:{relative_path}",
    }


def build_source_manifest(settings: Settings) -> list[dict[str, Any]]:
    manifest: list[dict[str, Any]] = []

    for path in iter_source_files(settings):
        metadata = build_source_metadata(path, settings.data_dir)
        metadata["bytes"] = path.stat().st_size
        metadata["sha256"] = _sha256_file(path)
        manifest.append(metadata)

    return manifest


def compute_corpus_hash(manifest: Iterable[dict[str, Any]]) -> str:
    digest = hashlib.sha256()
    serialized = json.dumps(
        list(manifest),
        sort_keys=True,
        separators=(",", ":"),
    )
    digest.update(serialized.encode("utf-8"))
    return digest.hexdigest()


def _page_label(metadata: dict[str, Any]) -> str | None:
    value = metadata.get("page_label")
    if value not in (None, ""):
        return str(value)

    for key, candidate in metadata.items():
        if key.endswith("_page_label") and candidate not in (None, ""):
            return str(candidate)

    return None


def _document_text(document: Any) -> str:
    text = getattr(document, "text", None)
    if text:
        return str(text).strip()

    get_content = getattr(document, "get_content", None)
    if callable(get_content):
        try:
            return str(get_content()).strip()
        except TypeError:
            return str(get_content(metadata_mode="none")).strip()

    return ""


def _read_text_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _load_local_markdown_documents(path: Path, settings: Settings) -> list[Document]:
    return [
        Document(
            text=_read_text_file(path),
            metadata=build_source_metadata(path, settings.data_dir),
        )
    ]


def _load_local_pdf_documents(path: Path, settings: Settings) -> list[Document]:
    source_metadata = build_source_metadata(path, settings.data_dir)
    reader = PdfReader(str(path))
    documents: list[Document] = []

    for page_index, page in enumerate(reader.pages, start=1):
        text = (page.extract_text() or "").strip()
        if not text:
            continue
        documents.append(
            Document(
                text=text,
                metadata={
                    **source_metadata,
                    "page_label": str(page_index),
                },
            )
        )

    return documents


def _normalize_external_document(
    raw_document: Any,
    *,
    source_metadata: dict[str, Any],
) -> Document | None:
    metadata = {**source_metadata, **dict(getattr(raw_document, "metadata", {}) or {})}
    text = _document_text(raw_document)
    if not text:
        return None
    return Document(text=text, metadata=metadata)


def _load_pdf_documents(path: Path, settings: Settings) -> list[Document]:
    try:
        from llama_parse import LlamaParse
    except ImportError:
        return _load_local_pdf_documents(path, settings)

    api_key = settings.llama_parse_api_key
    if not api_key:
        return _load_local_pdf_documents(path, settings)

    parser = LlamaParse(
        api_key=api_key,
        result_type=settings.llama_parse_result_type,
    )
    parsed_documents = list(parser.load_data(str(path)))
    if not parsed_documents:
        return _load_local_pdf_documents(path, settings)

    source_metadata = build_source_metadata(path, settings.data_dir)
    normalized_documents: list[Document] = []
    for raw_document in parsed_documents:
        normalized = _normalize_external_document(
            raw_document,
            source_metadata=source_metadata,
        )
        if normalized is not None:
            normalized_documents.append(normalized)

    return normalized_documents or _load_local_pdf_documents(path, settings)


def _load_source_documents(path: Path, settings: Settings) -> list[Document]:
    if path.suffix.lower() == ".pdf":
        return _load_pdf_documents(path, settings)
    return _load_local_markdown_documents(path, settings)


def _heading_sections(text: str) -> list[str]:
    matches = list(MARKDOWN_HEADING_PATTERN.finditer(text))
    if not matches:
        stripped = text.strip()
        return [stripped] if stripped else []

    sections: list[str] = []
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        section = text[start:end].strip()
        if section:
            sections.append(section)

    prefix = text[: matches[0].start()].strip()
    if prefix:
        sections.insert(0, prefix)

    return sections


def _word_spans(text: str) -> list[tuple[int, int]]:
    return [match.span() for match in WORD_PATTERN.finditer(text)]


def _chunk_text(text: str, *, chunk_size: int, chunk_overlap: int) -> list[str]:
    stripped = text.strip()
    if not stripped:
        return []

    spans = _word_spans(stripped)
    if not spans:
        return []

    step = max(1, chunk_size - chunk_overlap)
    chunks: list[str] = []

    start_index = 0
    while start_index < len(spans):
        end_index = min(start_index + chunk_size, len(spans))
        char_start = spans[start_index][0]
        char_end = spans[end_index - 1][1]
        chunk = stripped[char_start:char_end].strip()
        if chunk:
            chunks.append(chunk)
        if end_index >= len(spans):
            break
        start_index += step

    return chunks


def _split_document_text(document: Document, settings: Settings) -> list[Document]:
    text = _document_text(document)
    if not text:
        return []

    source_extension = str(document.metadata.get("source_extension", "")).lower()
    if source_extension == ".md":
        sections = _heading_sections(text)
    else:
        sections = [text.strip()]

    chunked_documents: list[Document] = []
    for section in sections:
        for chunk in _chunk_text(
            section,
            chunk_size=settings.chunk_size,
            chunk_overlap=settings.chunk_overlap,
        ):
            chunked_documents.append(
                Document(
                    text=chunk,
                    metadata=dict(document.metadata),
                )
            )

    return chunked_documents


def load_documents(settings: Settings) -> list[Document]:
    files = iter_source_files(settings)
    if not files:
        return []

    chunked_documents: list[Document] = []

    for path in files:
        source_metadata = build_source_metadata(path, settings.data_dir)
        source_documents = _load_source_documents(path, settings)
        source_chunks: list[Document] = []

        for source_document in source_documents:
            metadata = {**source_metadata, **dict(source_document.metadata or {})}
            for parsed_chunk in _split_document_text(
                Document(text=source_document.text, metadata=metadata),
                settings,
            ):
                chunk_text = _document_text(parsed_chunk)
                if not chunk_text:
                    continue

                chunk_index = len(source_chunks) + 1
                chunk_metadata = {**metadata, **dict(parsed_chunk.metadata or {})}
                chunk_metadata["page_label"] = _page_label(chunk_metadata)
                chunk_metadata["chunk_index"] = chunk_index
                chunk_metadata["chunk_hash"] = _text_sha256(chunk_text)

                source_chunks.append(
                    Document(
                        text=chunk_text,
                        metadata=chunk_metadata,
                        id_=f"chunk:{source_metadata['source_path']}:{chunk_index:04d}",
                    )
                )

        for document in source_chunks:
            document.metadata["chunk_total"] = len(source_chunks)

        chunked_documents.extend(source_chunks)

    return chunked_documents
