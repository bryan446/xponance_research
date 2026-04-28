from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


REPO_ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = REPO_ROOT / ".env"
load_dotenv(ENV_PATH, override=False)


def _read_optional(name: str) -> str | None:
    value = os.getenv(name)
    if value is None:
        return None
    value = value.strip()
    return value or None


def _resolve_path(raw_path: str | None, default: Path) -> Path:
    if not raw_path:
        return default.resolve()

    path = Path(raw_path).expanduser()
    if not path.is_absolute():
        path = REPO_ROOT / path

    return path.resolve()


def _split_csv(raw_value: str | None, *, default: tuple[str, ...]) -> tuple[str, ...]:
    if not raw_value:
        return default

    values = [item.strip() for item in raw_value.split(",")]
    return tuple(item for item in values if item)


def _read_int(name: str, default: int) -> int:
    raw_value = _read_optional(name)
    if raw_value is None:
        return default
    return int(raw_value)


@dataclass(frozen=True)
class Settings:
    repo_root: Path
    data_dir: Path
    graph_state_path: Path
    openai_api_key: str | None
    llama_parse_api_key: str | None
    app_name: str
    default_top_k: int
    allowed_extensions: tuple[str, ...]
    excluded_dirs: frozenset[str]
    chunk_size: int
    chunk_overlap: int
    llama_parse_result_type: str
    graph_llm_model: str
    neo4j_uri: str | None
    neo4j_username: str | None
    neo4j_password: str | None
    neo4j_database: str


def require_openai_api_key(settings: Settings) -> str:
    if settings.openai_api_key is None:
        raise ValueError(
            f"OPENAI_API_KEY is required. Add it to {ENV_PATH} or your shell environment."
        )
    return settings.openai_api_key


def require_neo4j_settings(settings: Settings) -> tuple[str, str, str, str]:
    if settings.neo4j_uri is None:
        raise ValueError(
            f"NEO4J_URI is required. Add it to {ENV_PATH} or your shell environment."
        )
    if settings.neo4j_username is None:
        raise ValueError(
            f"NEO4J_USERNAME is required. Add it to {ENV_PATH} or your shell environment."
        )
    if settings.neo4j_password is None:
        raise ValueError(
            f"NEO4J_PASSWORD is required. Add it to {ENV_PATH} or your shell environment."
        )

    return (
        settings.neo4j_uri,
        settings.neo4j_username,
        settings.neo4j_password,
        settings.neo4j_database,
    )


def get_settings() -> Settings:
    data_dir = _resolve_path(
        _read_optional("RAG_DATA_DIR"), REPO_ROOT / "knowledge_base"
    )
    graph_state_path = _resolve_path(
        _read_optional("RAG_GRAPH_STATE_FILE"), REPO_ROOT / ".neo4j_graph_state.json"
    )
    allowed_extensions = tuple(
        extension.lower()
        for extension in _split_csv(
            _read_optional("RAG_ALLOWED_EXTENSIONS"), default=(".md", ".pdf")
        )
    )
    excluded_dirs = frozenset(
        _split_csv(
            _read_optional("RAG_EXCLUDED_DIRS"),
            default=(
                ".git",
                ".venv",
                "__pycache__",
                ".mypy_cache",
                ".pytest_cache",
                "scripts",
                "llamacloud_rag",
                "codex",
                "docs",
                "node_modules",
                "plugins",
                ".agents",
            ),
        )
    )

    return Settings(
        repo_root=REPO_ROOT,
        data_dir=data_dir,
        graph_state_path=graph_state_path,
        openai_api_key=_read_optional("OPENAI_API_KEY"),
        llama_parse_api_key=_read_optional("LLAMA_PARSE_API_KEY"),
        app_name=_read_optional("RAG_APP_NAME") or "xponance-research",
        default_top_k=_read_int("RAG_DEFAULT_TOP_K", 5),
        allowed_extensions=allowed_extensions,
        excluded_dirs=excluded_dirs,
        chunk_size=_read_int("RAG_CHUNK_SIZE", 1024),
        chunk_overlap=_read_int("RAG_CHUNK_OVERLAP", 128),
        llama_parse_result_type=_read_optional("LLAMA_PARSE_RESULT_TYPE") or "markdown",
        graph_llm_model=_read_optional("GRAPH_LLM_MODEL") or "gpt-4o",
        neo4j_uri=_read_optional("NEO4J_URI"),
        neo4j_username=_read_optional("NEO4J_USERNAME"),
        neo4j_password=_read_optional("NEO4J_PASSWORD"),
        neo4j_database=_read_optional("NEO4J_DATABASE") or "neo4j",
    )
