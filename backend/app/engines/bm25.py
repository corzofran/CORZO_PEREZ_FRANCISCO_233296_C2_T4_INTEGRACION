"""BM25 (k1=1.5, b=0.75), idf=ln(1+(N-df+0.5)/(df+0.5)), índice invertido con pesos precalculados."""
import math
from collections import Counter

import numpy as np

from ..preprocess import tokens_lexicos
from .base import Engine, top_k


class BM25Engine(Engine):
    name, label = "bm25", "BM25"
    description = "Ranking probabilístico con saturación de frecuencia y normalización por longitud."

    def __init__(self, corpus, k1=1.5, b=0.75):
        self.ids = [d.id for d in corpus.documentos]
        self.n = len(self.ids)
        docs = [Counter(tokens_lexicos(d.texto_indexable)) for d in corpus.documentos]
        largos = np.array([sum(c.values()) for c in docs], dtype=float)
        avgdl = largos.mean() or 1.0
        df = Counter(t for c in docs for t in c)
        self.idf = {t: math.log(1 + (self.n - f + 0.5) / (f + 0.5)) for t, f in df.items()}
        post = {}
        for i, c in enumerate(docs):
            for t, f in c.items():
                w = self.idf[t] * f * (k1 + 1) / (f + k1 * (1 - b + b * largos[i] / avgdl))
                post.setdefault(t, ([], []))
                post[t][0].append(i)
                post[t][1].append(w)
        self.index = {t: (np.array(ix), np.array(ws)) for t, (ix, ws) in post.items()}

    def search(self, query, k=10):
        scores = np.zeros(self.n)
        hit = False
        for t in set(tokens_lexicos(query)):
            if t in self.index:
                ix, ws = self.index[t]
                scores[ix] += ws
                hit = True
        return top_k(scores, self.ids, k) if hit else []
