"""Gráficas del reporte (docs/fig_*.png) a partir de benchmark/results/*.json."""
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

R = Path(__file__).parent / "results"
D = Path(__file__).resolve().parents[1] / "docs"
C = {"tfidf": "#6B7FA3", "bm25": "#1C3257", "embeddings": "#E08A6E", "hybrid": "#2E8B7A"}
NOM = {"tfidf": "TF-IDF", "bm25": "BM25", "embeddings": "Embeddings", "hybrid": "Híbrido RRF"}
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False, "axes.grid": True, "grid.alpha": .25})
J = lambda n: json.loads((R / n).read_text(encoding="utf-8"))

q = J("quality.json")
fig, ax = plt.subplots(figsize=(7, 3.4))
grupos = [("lexica", "Léxicas"), ("semantica", "Semánticas"), ("mixta", "Mixtas")]
w = .2
for i, m in enumerate(C):
    ax.bar(np.arange(3) + (i - 1.5) * w, [q[m]["por_tipo"][g]["ndcg"] for g, _ in grupos], w, label=NOM[m], color=C[m])
ax.set_xticks(range(3)); ax.set_xticklabels([n for _, n in grupos]); ax.set_ylabel("nDCG@5"); ax.set_ylim(0, 1.1)
ax.legend(ncol=4, loc="upper center", bbox_to_anchor=(.5, 1.18), frameon=False); fig.tight_layout()
fig.savefig(D / "fig_calidad.png", dpi=200); plt.close(fig)

fig, axs = plt.subplots(1, 2, figsize=(7.4, 3.2))
for ax, tag, tit in ((axs[0], "think500", "Con pausa de ~500 ms"), (axs[1], "stress", "Sin pausa (estrés)")):
    r = J(f"load_test_{tag}.json")["resultados"]
    u = [x["usuarios"] for x in r]
    ax.plot(u, [x["e2e_ms"]["p50"] for x in r], "o-", color="#1C3257", label="p50")
    ax.plot(u, [x["e2e_ms"]["p95"] for x in r], "s--", color="#E08A6E", label="p95")
    ax.set_title(tit, fontsize=10); ax.set_xlabel("usuarios concurrentes"); ax.set_ylabel("ms (extremo a extremo)"); ax.set_xticks(u)
axs[0].legend(frameon=False); fig.tight_layout(); fig.savefig(D / "fig_latencia.png", dpi=200); plt.close(fig)

if (R / "scalability.json").exists():
    s = J("scalability.json")
    fig, ax = plt.subplots(figsize=(6.2, 3.2))
    for m in C:
        ax.plot([f["docs"] for f in s], [f["motores"][m]["p50"] for f in s], "o-", color=C[m], label=NOM[m])
    ax.set_xscale("log"); ax.set_yscale("log"); ax.set_xlabel("documentos en el índice"); ax.set_ylabel("p50 de búsqueda (ms)")
    ax.legend(frameon=False); fig.tight_layout(); fig.savefig(D / "fig_escala.png", dpi=200); plt.close(fig)

fig, ax = plt.subplots(figsize=(7.4, 2.4)); ax.axis("off")
cajas = [("Navegador\nHTML + JS", .02), ("FastAPI\n/api/search\n/api/compare", .27), ("Motores en memoria\nTF-IDF · BM25\nEmbeddings · RRF", .55), ("Corpus 60 docs\n+ qrels", .82)]
for t, x in cajas:
    ax.text(x + .07, .5, t, ha="center", va="center", fontsize=9, bbox=dict(boxstyle="round,pad=.6", fc="#EEF2F8", ec="#1C3257"))
for x in (.15, .40, .70):
    ax.annotate("", xy=(x + .06, .5), xytext=(x, .5), arrowprops=dict(arrowstyle="->", color="#E08A6E", lw=1.8))
ax.set_xlim(0, 1); fig.savefig(D / "fig_arquitectura.png", dpi=200, bbox_inches="tight"); plt.close(fig)
print("ok")
