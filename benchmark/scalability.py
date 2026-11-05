"""Escalabilidad en proceso: latencia p50/p95 de cada motor al replicar el corpus a 60/600/6000/30000 documentos."""
import json
import random
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from backend.app.config import Settings  # noqa: E402
from backend.app.corpus import Corpus, Document, load_corpus  # noqa: E402
from backend.app.engines.registry import build_engines  # noqa: E402
from backend.app.metrics import percentiles  # noqa: E402

s = Settings()
base = load_corpus(s.corpus_path)
Q = [q["texto"] for q in json.loads(s.qrels_path.read_text(encoding="utf-8"))["consultas"]]
rng = random.Random(7)
out = []
from backend.app.engines.embeddings import build_backend  # noqa: E402
backend = build_backend(s)
for n in (60, 600, 6000, 30000):
    docs = [Document(f"x{i}", d.titulo, d.texto + f" nota{i % 97}", d.tema, d.subtema) for i, d in
            ((i, base.documentos[i % len(base)]) for i in range(n))]
    t0 = time.perf_counter()
    E = build_engines(Corpus(docs), s, backend)
    build = time.perf_counter() - t0
    fila = {"docs": n, "indexado_s": round(build, 2), "motores": {}}
    for nombre, e in E.items():
        lat = []
        for _ in range(150):
            q = rng.choice(Q)
            t = time.perf_counter(); e.search(q, k=5); lat.append((time.perf_counter() - t) * 1000)
        fila["motores"][nombre] = percentiles(lat, (50, 95))
    print(n, fila["indexado_s"], {k: round(v["p50"], 3) for k, v in fila["motores"].items()}, flush=True)
    out.append(fila)
(Path(__file__).parent / "results" / "scalability.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
