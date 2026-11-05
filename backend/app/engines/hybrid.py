"""Búsqueda híbrida con Reciprocal Rank Fusion: score(d)=Σ 1/(k_rrf+rank)."""
from .base import Engine, Hit


class HybridEngine(Engine):
    name, label = "hybrid", "Híbrido (RRF)"
    description = "Fusión RRF de las listas de BM25 y embeddings; si un componente no responde, decide el otro."

    def __init__(self, bm25, emb, k_rrf=60, min_depth=10):
        self.bm25, self.emb, self.k_rrf, self.min_depth = bm25, emb, k_rrf, min_depth

    def search(self, query, k=10):
        depth = max(k, self.min_depth)
        scores = {}
        for eng in (self.bm25, self.emb):
            for rank, h in enumerate(eng.search(query, k=depth), start=1):
                scores[h.doc_id] = scores.get(h.doc_id, 0.0) + 1.0 / (self.k_rrf + rank)
        ordenados = sorted(scores.items(), key=lambda x: (-x[1], x[0]))[:k]
        return [Hit(d, s) for d, s in ordenados]
