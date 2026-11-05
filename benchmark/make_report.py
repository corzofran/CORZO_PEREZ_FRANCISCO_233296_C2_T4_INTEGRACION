"""Genera docs/RESULTADOS.md a partir de benchmark/results/*.json."""
import json
from pathlib import Path

R = Path(__file__).parent / "results"
OUT = Path(__file__).resolve().parents[1] / "docs" / "RESULTADOS.md"
cargar = lambda n: json.loads((R / n).read_text(encoding="utf-8")) if (R / n).exists() else None
L = ["# Resultados medidos", "", "Generado por `benchmark/make_report.py`. Cliente y servidor comparten la misma máquina.", ""]
q = cargar("quality.json")
if q:
    L += ["## Calidad (20 consultas)", "", "| Motor | nDCG@5 | MRR | R@5 | nDCG léxicas | nDCG semánticas | nDCG mixtas |", "|---|---|---|---|---|---|---|"]
    for n, r in q.items():
        g, t = r["global"], r["por_tipo"]
        L.append(f"| {n} | {g['ndcg']:.3f} | {g['mrr']:.3f} | {g['recall']:.3f} | {t['lexica']['ndcg']:.3f} | {t['semantica']['ndcg']:.3f} | {t['mixta']['ndcg']:.3f} |")
for tag, tit in (("think500", "Carga con pausa de ~500 ms"), ("stress", "Carga sin pausa (estrés)")):
    d = cargar(f"load_test_{tag}.json")
    if d:
        L += ["", f"## {tit}", "", "| Usuarios | Peticiones | Errores | req/s | p50 ms | p95 ms | p99 ms | p50 servidor | p95 servidor |", "|---|---|---|---|---|---|---|---|---|"]
        for r in d["resultados"]:
            e = r["e2e_ms"]
            sv = r["servidor_ms"]
            p50 = sum(v["p50"] for v in sv.values()) / len(sv)
            p95 = sum(v["p95"] for v in sv.values()) / len(sv)
            L.append(f"| {r['usuarios']} | {r['peticiones']} | {r['errores']} | {r['rps']} | {e['p50']:.2f} | {e['p95']:.2f} | {e['p99']:.2f} | {p50:.2f} | {p95:.2f} |")
s = cargar("scalability.json")
if s:
    L += ["", "## Escalabilidad (p50 / p95 en ms, k=5, en proceso)", "", "| Documentos | Indexado (s) | TF-IDF | BM25 | Embeddings | Híbrido |", "|---|---|---|---|---|---|"]
    for f in s:
        m = f["motores"]
        L.append(f"| {f['docs']} | {f['indexado_s']} | " + " | ".join(f"{m[k]['p50']:.2f} / {m[k]['p95']:.2f}" for k in ("tfidf", "bm25", "embeddings", "hybrid")) + " |")
st = cargar("startup.json")
if st:
    L += ["", f"## Arranque\n\nTiempo de carga de índices y modelo: {st['arranque_s']} s; memoria pico: {st['rss_mb']} MB."]
OUT.parent.mkdir(exist_ok=True)
OUT.write_text("\n".join(L) + "\n", encoding="utf-8")
print("escrito", OUT)
