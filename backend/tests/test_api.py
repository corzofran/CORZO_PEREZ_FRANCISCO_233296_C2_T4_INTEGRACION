import pytest
from fastapi.testclient import TestClient

from backend.app.config import Settings
from backend.app.engines.registry import build_engines
from backend.app.main import create_app, snippet


def cliente(corpus, backend, modo="threadpool"):
    s = Settings(); s.execution = modo
    return TestClient(create_app(s, corpus, build_engines(corpus, s, backend)))


@pytest.fixture(scope="module", params=["threadpool", "inline"])
def c(request, corpus, backend):
    with cliente(corpus, backend, request.param) as cl:
        yield cl


def test_health_y_engines(c):
    assert c.get("/api/health").json()["documentos"] == 8
    assert [e["id"] for e in c.get("/api/engines").json()] == ["tfidf", "bm25", "embeddings", "hybrid"]


def test_search_formato(c):
    r = c.get("/api/search", params={"q": "marimba", "engine": "bm25"}).json()
    assert r["results"][0]["id"] == "t6" and r["took_ms"] >= 0 and "snippet" in r["results"][0]


def test_search_errores(c):
    assert c.get("/api/search", params={"q": "x", "engine": "nada"}).status_code == 404
    assert c.get("/api/search").status_code == 422
    assert c.get("/api/search", params={"q": "x", "k": 99}).status_code == 422


def test_compare_jaccard(c):
    r = c.get("/api/compare", params={"q": "café"}).json()
    assert set(r["engines"]) == {"tfidf", "bm25", "embeddings", "hybrid"}
    assert all(0 <= v <= 1 for v in r["jaccard"].values()) and len(r["jaccard"]) == 6


def test_documentos(c):
    assert len(c.get("/api/documents").json()) == 8
    assert c.get("/api/documents/t0").json()["titulo"].startswith("El agua")
    assert c.get("/api/documents/nope").status_code == 404


def test_stats_y_reset(c):
    c.post("/api/stats/reset")
    for _ in range(5):
        c.get("/api/search", params={"q": "agua", "engine": "tfidf"})
    s = c.get("/api/stats").json()["latency_ms"]["tfidf"]
    assert s["count"] == 5 and s["p95"] >= s["p50"]
    c.post("/api/stats/reset")
    assert c.get("/api/stats").json()["latency_ms"] == {}


def test_snippet():
    assert "mosquito" in snippet("a " * 100 + "el mosquito pica " + "b " * 100, "mosquitos")
