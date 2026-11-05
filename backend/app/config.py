"""Configuración del sistema (variables de entorno con valores por defecto)."""
import os
from dataclasses import dataclass, field
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]


@dataclass
class Settings:
    corpus_path: Path = field(default_factory=lambda: Path(os.getenv("CORPUS_PATH", RAIZ / "data" / "corpus.json")))
    qrels_path: Path = field(default_factory=lambda: Path(os.getenv("QRELS_PATH", RAIZ / "data" / "qrels.json")))
    embeddings_backend: str = field(default_factory=lambda: os.getenv("EMBEDDINGS_BACKEND", "spacy"))
    spacy_model: str = field(default_factory=lambda: os.getenv("SPACY_MODEL", "es_core_news_lg"))
    sbert_model: str = field(default_factory=lambda: os.getenv(
        "SBERT_MODEL", "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"))
    frontend_dir: Path = field(default_factory=lambda: Path(os.getenv("FRONTEND_DIR", RAIZ / "frontend")))
    latency_window: int = field(default_factory=lambda: int(os.getenv("LATENCY_WINDOW", "20000")))
    # threadpool: endpoints síncronos en el pool de hilos de FastAPI; inline: se ejecutan en el event loop.
    execution: str = field(default_factory=lambda: os.getenv("EXECUTION_MODE", "threadpool"))
