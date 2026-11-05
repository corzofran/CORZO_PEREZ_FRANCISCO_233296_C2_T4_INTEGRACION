"""Métricas de recuperación: nDCG@k, MRR, Recall@k, Precision@k."""
import json
import math
from pathlib import Path


def ndcg_at_k(ranking, relevancia: dict, k=5) -> float:
    dcg = sum((2 ** relevancia.get(d, 0) - 1) / math.log2(i + 2) for i, d in enumerate(ranking[:k]))
    ideal = sorted(relevancia.values(), reverse=True)[:k]
    idcg = sum((2 ** r - 1) / math.log2(i + 2) for i, r in enumerate(ideal))
    return dcg / idcg if idcg > 0 else 0.0


def mrr(ranking, relevancia: dict) -> float:
    for i, d in enumerate(ranking):
        if relevancia.get(d, 0) > 0:
            return 1.0 / (i + 1)
    return 0.0


def recall_at_k(ranking, relevancia: dict, k=5) -> float:
    rel = {d for d, r in relevancia.items() if r > 0}
    return len(rel & set(ranking[:k])) / len(rel) if rel else 0.0


def precision_at_k(ranking, relevancia: dict, k=5) -> float:
    return sum(1 for d in ranking[:k] if relevancia.get(d, 0) > 0) / k


def load_queries(path) -> list:
    return json.loads(Path(path).read_text(encoding="utf-8"))["consultas"]


def evaluate(engine, queries, k=5) -> dict:
    """Devuelve métricas globales y por tipo de consulta para un motor."""
    filas = []
    for q in queries:
        ranking = [h.doc_id for h in engine.search(q["texto"], k=10)]
        rel = q["relevancia"]
        filas.append({"id": q["id"], "tipo": q["tipo"], "ndcg": ndcg_at_k(ranking, rel, k),
                      "mrr": mrr(ranking, rel), "recall": recall_at_k(ranking, rel, k)})

    def prom(rows):
        n = len(rows) or 1
        return {"ndcg": sum(r["ndcg"] for r in rows) / n, "mrr": sum(r["mrr"] for r in rows) / n,
                "recall": sum(r["recall"] for r in rows) / n, "n": len(rows)}
    tipos = sorted({f["tipo"] for f in filas})
    return {"global": prom(filas), "por_tipo": {t: prom([f for f in filas if f["tipo"] == t]) for t in tipos},
            "por_consulta": filas}
