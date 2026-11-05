"""TF-IDF con índice invertido: tf=f/|d|, idf=ln(N/df), similitud coseno."""
import math
from collections import Counter

import numpy as np

from ..preprocess import tokens_lexicos
from .base import Engine, top_k


class TfidfEngine(Engine):
    name, label = "tfidf", "TF-IDF"
    description = "Pesos tf·idf y similitud coseno sobre un índice invertido."

    def __init__(self, corpus):
        self.ids = [d.id for d in corpus.documentos]
        n = len(self.ids)
        docs = [Counter(tokens_lexicos(d.texto_indexable)) for d in corpus.documentos]
        df = Counter(t for c in docs for t in c)
        self.idf = {t: math.log(n / f) for t, f in df.items()}
        norms = np.zeros(n)
        post = {}
        for i, c in enumerate(docs):
            largo = sum(c.values()) or 1
            for t, f in c.items():
                w = (f / largo) * self.idf[t]
                norms[i] += w * w
                post.setdefault(t, ([], []))
                post[t][0].append(i)
                post[t][1].append(w)
        norms = np.sqrt(norms)
        norms[norms == 0] = 1.0
        self.index = {t: (np.array(ix), np.array(ws) / norms[ix]) for t, (ix, ws) in post.items()}
        self.n = n

    def search(self, query, k=10):
        toks = tokens_lexicos(query)
        if not toks:
            return []
        q = Counter(toks)
        largo = len(toks)
        qw = {t: (f / largo) * self.idf[t] for t, f in q.items() if t in self.idf}
        qn = math.sqrt(sum(w * w for w in qw.values()))
        if qn == 0:
            return []
        scores = np.zeros(self.n)
        for t, w in qw.items():
            ix, ws = self.index[t]
            scores[ix] += w * ws
        return top_k(scores / qn, self.ids, k)
