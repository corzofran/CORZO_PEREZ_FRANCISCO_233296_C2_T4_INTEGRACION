"""Interfaz común de los motores."""
from dataclasses import dataclass

import numpy as np


@dataclass
class Hit:
    doc_id: str
    score: float


class Engine:
    name = "base"
    label = "Base"
    description = ""

    def search(self, query: str, k: int = 10) -> list:
        raise NotImplementedError


def top_k(scores: np.ndarray, ids: list, k: int) -> list:
    """Top-k de documentos con score > 0, desempate estable por posición del documento."""
    k = min(k, len(ids))
    if k <= 0:
        return []
    idx = np.argpartition(-scores, k - 1)[:k] if k < len(scores) else np.arange(len(scores))
    idx = sorted(idx, key=lambda i: (-scores[i], i))
    return [Hit(ids[i], float(scores[i])) for i in idx if scores[i] > 0]
