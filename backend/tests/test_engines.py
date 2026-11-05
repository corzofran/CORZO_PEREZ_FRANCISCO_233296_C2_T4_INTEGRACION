import math
from collections import Counter

import pytest

from backend.app.engines.base import Hit
from backend.app.engines.bm25 import BM25Engine
from backend.app.engines.embeddings import EmbeddingEngine
from backend.app.engines.hybrid import HybridEngine
from backend.app.engines.tfidf import TfidfEngine
from backend.app.preprocess import tokens_lexicos


def test_tfidf_referencia_ingenua(corpus):
    e = TfidfEngine(corpus)
    docs = [Counter(tokens_lexicos(d.texto_indexable)) for d in corpus.documentos]
    n = len(docs)
    df = Counter(t for c in docs for t in c)

    def vec(c):
        L = sum(c.values())
        return {t: f / L * math.log(n / df[t]) for t, f in c.items() if t in df}
    q = vec(Counter(tokens_lexicos("agua potable colonias")))
    esperado = {}
    for d, c in zip(corpus.documentos, docs):
        v = vec(c)
        num = sum(q[t] * v.get(t, 0) for t in q)
        den = math.sqrt(sum(x * x for x in q.values())) * math.sqrt(sum(x * x for x in v.values()))
        if den and num > 0:
            esperado[d.id] = num / den
    got = {h.doc_id: h.score for h in e.search("agua potable colonias", k=8)}
    assert got.keys() == esperado.keys()
    for k in got:
        assert got[k] == pytest.approx(esperado[k], rel=1e-9)


def test_bm25_referencia_ingenua(corpus):
    e = BM25Engine(corpus)
    docs = [Counter(tokens_lexicos(d.texto_indexable)) for d in corpus.documentos]
    n, avg = len(docs), sum(sum(c.values()) for c in docs) / len(docs)
    df = Counter(t for c in docs for t in c)
    esp = {}
    for d, c in zip(corpus.documentos, docs):
        s = 0.0
        for t in set(tokens_lexicos("café exportación")):
            if t in c:
                idf = math.log(1 + (n - df[t] + .5) / (df[t] + .5))
                s += idf * c[t] * 2.5 / (c[t] + 1.5 * (.25 + .75 * sum(c.values()) / avg))
        if s > 0:
            esp[d.id] = s
    got = {h.doc_id: h.score for h in e.search("café exportación", k=8)}
    assert got.keys() == esp.keys()
    for k in got:
        assert got[k] == pytest.approx(esp[k], rel=1e-9)


@pytest.mark.parametrize("cls", [TfidfEngine, BM25Engine])
def test_lexicos_encuentran_literal_y_vacio(corpus, cls):
    e = cls(corpus)
    assert e.search("marimba")[0].doc_id == "t6"
    assert e.search("xyzzy") == []
    assert e.search("de la") == []


def test_embeddings_orden_y_normalizacion(corpus, backend):
    e = EmbeddingEngine(corpus, backend)
    hits = e.search("café exportación sierra", k=3)
    assert hits[0].doc_id == "t1"
    assert [h.score for h in hits] == sorted([h.score for h in hits], reverse=True)


def test_embeddings_sin_vector_no_responde(corpus, backend):
    assert EmbeddingEngine(corpus, backend).search("1234 ???") == []


class Fijo:
    def __init__(self, ids): self.ids = ids
    def search(self, q, k=10): return [Hit(i, 1.0) for i in self.ids][:k]


def test_rrf_calculo_exacto():
    h = HybridEngine(Fijo(["a", "b", "c"]), Fijo(["b", "c", "d"]))
    r = {x.doc_id: x.score for x in h.search("q", k=4)}
    assert r["b"] == pytest.approx(1 / 62 + 1 / 61)
    assert r["a"] == pytest.approx(1 / 61) and r["d"] == pytest.approx(1 / 63)
    assert h.search("q", k=4)[0].doc_id == "b"


def test_hibrido_tolera_componente_vacio():
    h = HybridEngine(Fijo([]), Fijo(["x", "y"]))
    assert [x.doc_id for x in h.search("q")] == ["x", "y"]
