"""Calidad de recuperación de los 4 motores (nDCG@5, MRR, R@5) global y por tipo de consulta."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from backend.app.config import Settings  # noqa: E402
from backend.app.corpus import load_corpus  # noqa: E402
from backend.app.engines.registry import build_engines  # noqa: E402
from backend.app.evaluation import evaluate, load_queries  # noqa: E402

s = Settings()
motores = build_engines(load_corpus(s.corpus_path), s)
Q = load_queries(s.qrels_path)
res = {n: evaluate(e, Q) for n, e in motores.items()}
out = Path(__file__).parent / "results" / "quality.json"
out.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"{'motor':11s} nDCG@5  MRR    R@5   | lex    sem    mix (nDCG)")
for n, r in res.items():
    g, t = r["global"], r["por_tipo"]
    print(f"{n:11s} {g['ndcg']:.3f}  {g['mrr']:.3f}  {g['recall']:.3f} | {t['lexica']['ndcg']:.3f}  {t['semantica']['ndcg']:.3f}  {t['mixta']['ndcg']:.3f}")
