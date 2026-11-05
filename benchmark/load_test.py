"""Prueba de carga: N usuarios concurrentes (bucle cerrado) con httpx asíncrono.
Cada usuario elige consulta y motor al azar, espera la respuesta, hace una pausa (think time) y repite.
Uso: python benchmark/load_test.py --levels 1,10,25,50 --duration 15 --think-ms 500 --tag think500"""
import argparse
import asyncio
import json
import random
import sys
import time
from pathlib import Path

import httpx

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from backend.app.metrics import percentiles  # noqa: E402

QUERIES = [q["texto"] for q in json.loads((Path(__file__).resolve().parents[1] / "data" / "qrels.json").read_text(encoding="utf-8"))["consultas"]]
ENGINES = ["tfidf", "bm25", "embeddings", "hybrid"]


async def usuario(client, base, fin, think, lat, errores, rng, engine):
    while time.perf_counter() < fin:
        e = engine or rng.choice(ENGINES)
        t0 = time.perf_counter()
        try:
            r = await client.get(f"{base}/api/search", params={"q": rng.choice(QUERIES), "engine": e, "k": 5})
            ok = r.status_code == 200
        except Exception:
            ok = False
        ms = (time.perf_counter() - t0) * 1000
        if ok:
            lat.setdefault(e, []).append(ms)
        else:
            errores.append(1)
        if think:
            await asyncio.sleep(think / 1000 * rng.uniform(0.5, 1.5))


async def nivel(base, n, dur, think, engine=None, seed=1):
    lat, errores = {}, []
    rng = random.Random(seed)
    limits = httpx.Limits(max_connections=n + 5, max_keepalive_connections=n + 5)
    async with httpx.AsyncClient(limits=limits, timeout=30) as c:
        await c.post(f"{base}/api/stats/reset")
        for _ in range(10):  # calentamiento
            await c.get(f"{base}/api/search", params={"q": "agua", "engine": "bm25"})
        t0 = time.perf_counter()
        fin = t0 + dur
        await asyncio.gather(*[usuario(c, base, fin, think, lat, errores, random.Random(seed + i), engine) for i in range(n)])
        el = time.perf_counter() - t0
        srv = (await c.get(f"{base}/api/stats")).json()["latency_ms"]
    todas = [x for v in lat.values() for x in v]
    return {"usuarios": n, "duracion_s": round(el, 1), "peticiones": len(todas), "errores": len(errores),
            "rps": round(len(todas) / el, 1), "e2e_ms": percentiles(todas),
            "por_motor_e2e": {k: percentiles(v) for k, v in lat.items()},
            "servidor_ms": {k: {p: v[p] for p in ("p50", "p95", "p99")} for k, v in srv.items()}}


def md(res, think):
    L = [f"### Carga con pausa de ~{think} ms" if think else "### Carga sin pausa (estrés)", "",
         "| Usuarios | Peticiones | Errores | req/s | p50 (ms) | p95 (ms) | p99 (ms) |", "|---|---|---|---|---|---|---|"]
    for r in res:
        e = r["e2e_ms"]
        L.append(f"| {r['usuarios']} | {r['peticiones']} | {r['errores']} | {r['rps']} | {e['p50']:.2f} | {e['p95']:.2f} | {e['p99']:.2f} |")
    return "\n".join(L) + "\n"


async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="http://127.0.0.1:8000")
    ap.add_argument("--levels", default="1,10,25,50")
    ap.add_argument("--duration", type=float, default=15)
    ap.add_argument("--think-ms", type=float, default=500)
    ap.add_argument("--tag", default="")
    ap.add_argument("--engine", default=None)
    a = ap.parse_args()
    res = []
    for n in [int(x) for x in a.levels.split(",")]:
        r = await nivel(a.base, n, a.duration, a.think_ms, a.engine)
        print(f"{n:3d} usuarios: {r['peticiones']} peticiones, {r['errores']} errores, {r['rps']} rps, "
              f"p50 {r['e2e_ms']['p50']:.2f} ms, p95 {r['e2e_ms']['p95']:.2f} ms")
        res.append(r)
    d = Path(__file__).parent / "results"
    d.mkdir(exist_ok=True)
    suf = f"_{a.tag}" if a.tag else ""
    (d / f"load_test{suf}.json").write_text(json.dumps({"think_ms": a.think_ms, "resultados": res}, indent=1), encoding="utf-8")
    (d / f"load_test{suf}.md").write_text(md(res, a.think_ms), encoding="utf-8")

asyncio.run(main())
