"""Mide el tiempo de arranque y la memoria (RSS) del proceso con los 4 motores cargados."""
import json
import resource
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
t0 = time.perf_counter()
from backend.app.config import Settings  # noqa: E402
from backend.app.corpus import load_corpus  # noqa: E402
from backend.app.engines.registry import build_engines  # noqa: E402
s = Settings()
E = build_engines(load_corpus(s.corpus_path), s)
r = {"arranque_s": round(time.perf_counter() - t0, 2), "rss_mb": round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024)}
print(r)
(Path(__file__).parent / "results" / "startup.json").write_text(json.dumps(r), encoding="utf-8")
