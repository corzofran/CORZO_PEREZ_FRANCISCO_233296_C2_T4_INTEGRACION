"""Construcción de los motores."""
from .bm25 import BM25Engine
from .embeddings import EmbeddingEngine, build_backend
from .hybrid import HybridEngine
from .tfidf import TfidfEngine

ORDEN = ["tfidf", "bm25", "embeddings", "hybrid"]


def build_engines(corpus, settings=None, backend=None) -> dict:
    if backend is None:
        backend = build_backend(settings)
    bm25, emb = BM25Engine(corpus), EmbeddingEngine(corpus, backend)
    motores = {"tfidf": TfidfEngine(corpus), "bm25": bm25, "embeddings": emb, "hybrid": HybridEngine(bm25, emb)}
    return {k: motores[k] for k in ORDEN}
