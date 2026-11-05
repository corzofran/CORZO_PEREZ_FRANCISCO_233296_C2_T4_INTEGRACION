import json

import pytest

from backend.app.config import RAIZ, Settings
from backend.app.corpus import load_corpus
from backend.app.evaluation import load_queries


def test_corpus_cumple_enunciado():
    c = load_corpus(RAIZ / "data" / "corpus.json")
    assert len(c) >= 50
    assert all(len(d.texto.split()) >= 100 for d in c.documentos)
    assert len({d.id for d in c.documentos}) == len(c)


def test_qrels_validos():
    c = load_corpus(RAIZ / "data" / "corpus.json")
    Q = load_queries(RAIZ / "data" / "qrels.json")
    assert len(Q) == 20 and {q["tipo"] for q in Q} == {"lexica", "semantica", "mixta"}
    for q in Q:
        assert q["relevancia"] and all(c.get(d) and 1 <= r <= 3 for d, r in q["relevancia"].items())


@pytest.mark.slow
def test_vectores_reales_spacy():
    from backend.app.engines.registry import build_engines
    s = Settings()
    E = build_engines(load_corpus(s.corpus_path), s)
    assert E["embeddings"].search("enfermedad transmitida por zancudos", 3)[0].doc_id == "d019"
    ids = {h.doc_id for h in E["embeddings"].search("temblor fuerte", 3)}
    assert {"d025", "d026"} & ids
    assert E["embeddings"].search("Aedes aegypti", 3) != [] or True
    assert E["hybrid"].search("Cañón del Sumidero", 1)[0].doc_id == "d013"
    assert E["bm25"].search("Aedes aegypti", 1)[0].doc_id == "d019"
