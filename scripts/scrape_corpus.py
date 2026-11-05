"""Scraper opcional (puntos extra): construye un corpus desde Wikipedia en español.

Respeta robots.txt, usa un User-Agent identificable y pausa 1 s entre peticiones. Genera:
  data/corpus_scraped.json, data/qrels_scraped.json (por tema), data/sources_scraped.md (URL, fecha, licencia).
Uso:  python scripts/scrape_corpus.py [--pause 1.0]
NOTA: en el entorno donde se desarrolló el proyecto no hubo acceso a es.wikipedia.org, por lo que este script NO se
ejecutó contra el sitio real (solo se probó con HTML de muestra). El corpus entregado es el sintético.
"""
import argparse
import json
import re
import sys
import time
import urllib.robotparser
from datetime import date
from pathlib import Path

import requests
from bs4 import BeautifulSoup

RAIZ = Path(__file__).resolve().parent.parent
UA = "UPCh-MineriaDeDatos-Tarea4/1.0 (proyecto academico; contacto: ver README del repositorio)"
MIN_PALABRAS = 100


def extraer(html: str, max_palabras=220):
    """(titulo, texto) con los primeros párrafos del artículo; None si no alcanza el mínimo de palabras."""
    soup = BeautifulSoup(html, "html.parser")
    h1 = soup.find("h1")
    titulo = h1.get_text(" ", strip=True) if h1 else ""
    cuerpo = soup.find(id="mw-content-text") or soup
    partes, n = [], 0
    for p in cuerpo.find_all("p"):
        for s in p.find_all(["sup", "style", "script"]):
            s.decompose()
        t = re.sub(r"\s+", " ", p.get_text(" ", strip=True))
        t = re.sub(r"\[\d+\]", "", t).strip()
        if len(t.split()) < 8:
            continue
        partes.append(t)
        n += len(t.split())
        if n >= max_palabras:
            break
    texto = " ".join(partes)
    return (titulo, texto) if len(texto.split()) >= MIN_PALABRAS and titulo else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pause", type=float, default=1.0)
    a = ap.parse_args()
    seeds = json.loads((RAIZ / "data" / "scrape_seeds.json").read_text(encoding="utf-8"))
    base = seeds["base_url"]
    rp = urllib.robotparser.RobotFileParser(base.split("/wiki/")[0] + "/robots.txt")
    rp.read()
    docs, fuentes = [], []
    for tema, titulos in seeds["temas"].items():
        for t in titulos:
            url = base + t
            if not rp.can_fetch(UA, url):
                print("robots.txt no permite", url)
                continue
            try:
                r = requests.get(url, headers={"User-Agent": UA}, timeout=20)
                r.raise_for_status()
            except Exception as e:
                print("fallo", url, e)
                continue
            ext = extraer(r.text)
            time.sleep(a.pause)
            if not ext:
                print("descartado (corto)", url)
                continue
            i = len(docs) + 1
            docs.append({"id": f"w{i:03d}", "titulo": ext[0], "texto": ext[1], "tema": tema, "subtema": tema,
                         "fuente": url, "n_palabras": len(ext[1].split())})
            fuentes.append((url, ext[0], tema))
    (RAIZ / "data" / "corpus_scraped.json").write_text(json.dumps(
        {"nombre": "Corpus Wikipedia (scraping)", "tipo": "scraping", "fecha_creacion": date.today().isoformat(),
         "licencia": seeds.get("license", ""), "documentos": docs}, ensure_ascii=False, indent=1), encoding="utf-8")
    qrels = [{"id": f"s{j+1:02d}", "texto": tema.replace("_", " "), "tipo": "semantica",
              "relevancia": {d["id"]: 3 for d in docs if d["tema"] == tema}} for j, tema in enumerate(seeds["temas"])
             if any(d["tema"] == tema for d in docs)]
    (RAIZ / "data" / "qrels_scraped.json").write_text(json.dumps({"consultas": qrels}, ensure_ascii=False, indent=1), encoding="utf-8")
    md = [f"# Fuentes del corpus scrapeado\n\nObtenido el {date.today().isoformat()}. Licencia: {seeds.get('license', '')}.\n"]
    md += [f"- [{t}]({u}) — tema: {tm}" for u, t, tm in fuentes]
    (RAIZ / "data" / "sources_scraped.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"{len(docs)} documentos guardados")
    return 0 if len(docs) >= 50 else 1


if __name__ == "__main__":
    sys.exit(main())
