"""Construye data/corpus.json a partir de los textos redactados en corpus_source_a.py y corpus_source_b.py.

Uso:  python scripts/build_corpus.py
Valida los requisitos del enunciado: >= 50 documentos y >= 100 palabras por documento.
"""
import json
import statistics
import sys
from collections import Counter
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from corpus_source_a import DOCS_A  # noqa: E402
from corpus_source_b import DOCS_B  # noqa: E402

MIN_DOCS, MIN_PALABRAS = 50, 100
RAIZ = Path(__file__).resolve().parent.parent


def construir():
    docs = []
    for i, (tema, subtema, titulo, texto) in enumerate(DOCS_A + DOCS_B, start=1):
        docs.append({
            "id": f"d{i:03d}", "titulo": titulo, "texto": texto, "tema": tema, "subtema": subtema,
            "fuente": "Texto original redactado para este proyecto (corpus sintético); lugares reales, sucesos ilustrativos.",
            "n_palabras": len(texto.split()),
        })
    return docs


def validar(docs):
    errores = []
    if len(docs) < MIN_DOCS:
        errores.append(f"solo hay {len(docs)} documentos (mínimo {MIN_DOCS})")
    if len({d['id'] for d in docs}) != len(docs):
        errores.append("ids repetidos")
    for d in docs:
        if d["n_palabras"] < MIN_PALABRAS:
            errores.append(f"{d['id']} ({d['subtema']}) tiene {d['n_palabras']} palabras (< {MIN_PALABRAS})")
    return errores


if __name__ == "__main__":
    docs = construir()
    errores = validar(docs)
    palabras = [d["n_palabras"] for d in docs]
    print(f"{len(docs)} documentos | palabras: min {min(palabras)}, mediana {statistics.median(palabras):.0f}, "
          f"media {statistics.mean(palabras):.1f}, max {max(palabras)} | total {sum(palabras)}")
    print("por tema:", dict(Counter(d['tema'] for d in docs)))
    if errores:
        print("\nERRORES:")
        for e in errores:
            print(" -", e)
        sys.exit(1)
    salida = RAIZ / "data" / "corpus.json"
    salida.write_text(json.dumps({"nombre": "Corpus chiapaneco sintético", "fecha_creacion": date.today().isoformat(),
                                  "tipo": "sintetico", "documentos": docs}, ensure_ascii=False, indent=1), encoding="utf-8")
    print("escrito", salida.relative_to(RAIZ))
