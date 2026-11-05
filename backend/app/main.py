"""API FastAPI del buscador: 4 motores (TF-IDF, BM25, Embeddings, Híbrido RRF) sobre un mismo corpus."""
import functools
import re
import time
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .config import Settings
from .corpus import load_corpus
from .engines.registry import ORDEN, build_engines
from .evaluation import load_queries
from .metrics import LatencyRecorder
from .preprocess import quitar_diacriticos


def snippet(texto: str, query: str, largo=220) -> str:
    """Fragmento del texto centrado en la primera coincidencia con alguna palabra de la consulta."""
    plano = quitar_diacriticos(texto.lower())
    pos = -1
    for p in re.findall(r"\w{4,}", quitar_diacriticos(query.lower())):
        pos = plano.find(p[:5])
        if pos >= 0:
            break
    ini = max(0, pos - largo // 3) if pos >= 0 else 0
    frag = texto[ini:ini + largo].strip()
    return ("… " if ini > 0 else "") + frag + (" …" if ini + largo < len(texto) else "")


def create_app(settings=None, corpus=None, engines=None, backend=None) -> FastAPI:
    settings = settings or Settings()
    rec = LatencyRecorder(settings.latency_window)
    estado = {}

    @asynccontextmanager
    async def lifespan(app):
        estado["corpus"] = corpus or load_corpus(settings.corpus_path)
        estado["engines"] = engines or build_engines(estado["corpus"], settings, backend)
        yield

    app = FastAPI(title="Buscador T4", version="1.0", lifespan=lifespan)
    app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
    inline = settings.execution == "inline"

    def ruta(fn):
        if not inline:
            return fn

        @functools.wraps(fn)
        async def w(*a, **kw):
            return fn(*a, **kw)
        return w

    def get(path):
        return lambda fn: app.get(path)(ruta(fn))

    def post(path):
        return lambda fn: app.post(path)(ruta(fn))

    def motor(nombre):
        e = estado["engines"].get(nombre)
        if e is None:
            raise HTTPException(404, f"motor desconocido: {nombre}")
        return e

    def buscar(nombre, q, k):
        e = motor(nombre)
        t0 = time.perf_counter()
        hits = e.search(q, k=k)
        ms = (time.perf_counter() - t0) * 1000
        rec.record(nombre, ms)
        c = estado["corpus"]
        res = []
        for h in hits:
            d = c.get(h.doc_id)
            res.append({"id": d.id, "titulo": d.titulo, "tema": d.tema, "score": round(h.score, 5),
                        "snippet": snippet(d.texto, q)})
        return {"engine": nombre, "query": q, "took_ms": round(ms, 3), "total": len(res), "results": res}

    @get("/api/health")
    def health():
        return {"status": "ok", "documentos": len(estado["corpus"]), "motores": list(estado["engines"])}

    @get("/api/engines")
    def listar():
        return [{"id": k, "label": e.label, "description": e.description} for k, e in estado["engines"].items()]

    @get("/api/search")
    def search(q: str = Query(..., min_length=1), engine: str = "bm25", k: int = Query(5, ge=1, le=20)):
        return buscar(engine, q, k)

    @get("/api/compare")
    def compare(q: str = Query(..., min_length=1), k: int = Query(5, ge=1, le=20)):
        out = {n: buscar(n, q, k) for n in ORDEN if n in estado["engines"]}
        conj = {n: {r["id"] for r in v["results"]} for n, v in out.items()}
        nombres = list(conj)
        jac = {}
        for i, a in enumerate(nombres):
            for b in nombres[i + 1:]:
                u = conj[a] | conj[b]
                jac[f"{a}|{b}"] = round(len(conj[a] & conj[b]) / len(u), 3) if u else 0.0
        return {"query": q, "engines": out, "jaccard": jac}

    @get("/api/documents")
    def documentos():
        return [{"id": d.id, "titulo": d.titulo, "tema": d.tema} for d in estado["corpus"].documentos]

    @get("/api/documents/{doc_id}")
    def documento(doc_id: str):
        d = estado["corpus"].get(doc_id)
        if d is None:
            raise HTTPException(404, "documento no encontrado")
        return {"id": d.id, "titulo": d.titulo, "texto": d.texto, "tema": d.tema, "fuente": d.fuente}

    @get("/api/stats")
    def stats():
        return {"latency_ms": rec.snapshot(), "execution": settings.execution}

    @post("/api/stats/reset")
    def reset():
        rec.reset()
        return {"ok": True}

    if settings.frontend_dir and settings.frontend_dir.exists():
        app.mount("/", StaticFiles(directory=str(settings.frontend_dir), html=True), name="frontend")
    return app


app = create_app()
