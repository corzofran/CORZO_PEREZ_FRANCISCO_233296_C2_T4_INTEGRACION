"""Construye data/qrels.json: 20 consultas con juicios de relevancia graduada (3 = muy relevante ... 1 = marginal).

Como el corpus es sintético, cada documento se redactó con un SUBTEMA conocido, y los juicios se derivan de reglas
transparentes:
  - consultas LEXICAS: relevante (3) si el documento contiene literalmente la expresión (sin distinguir acentos);
  - consultas SEMANTICAS y MIXTAS: relevancia por subtema (la consulta usa palabras distintas a las del documento).
Advertencia: no es una anotación independiente; sirve para comparar motores, no para estimar calidad absoluta.

Uso:  python scripts/build_qrels.py
"""
import json
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent


def sin_acentos(s):
    return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn")


# (id, consulta, tipo, regla) -- regla: ("literal", expresion) o ("subtemas", {subtema: grado})
CONSULTAS = [
    ("q01", "Cañón del Sumidero", "lexica", ("literal", "Cañón del Sumidero")),
    ("q02", "Soconusco", "lexica", ("literal", "Soconusco")),
    ("q03", "Aedes aegypti", "lexica", ("literal", "Aedes aegypti")),
    ("q04", "marimba", "lexica", ("literal", "marimba")),
    ("q05", "Lacandona", "lexica", ("literal", "Lacandona")),
    ("q06", "pozol", "lexica", ("literal", "pozol")),
    ("q07", "falta de agua en las colonias", "semantica",
     ("subtemas", {"agua-colonias": 3, "agua-potable": 2, "agua-ahorro": 2, "agua-presa": 1, "agua-agro": 1, "agua-lluvias": 1})),
    ("q08", "temblor fuerte", "semantica", ("subtemas", {"riesgo-sismo": 3, "riesgo-simulacro": 3})),
    ("q09", "enfermedad transmitida por zancudos", "semantica", ("subtemas", {"salud-dengue": 3, "riesgo-inundacion": 1})),
    ("q10", "cultivos afectados por falta de lluvia", "semantica", ("subtemas", {"agua-agro": 3, "agua-lluvias": 1})),
    ("q11", "viajeros que visitan lugares históricos", "semantica",
     ("subtemas", {"turismo-palenque": 3, "turismo-sancristobal": 3, "turismo-sumidero": 1, "turismo-aguaazul": 1, "turismo-hoteles": 1})),
    ("q12", "aprendizaje automático para estudiantes", "semantica", ("subtemas", {"tec-ia": 3, "tec-bootcamp": 2, "tec-becas": 1})),
    ("q13", "animales en peligro de extinción", "semantica", ("subtemas", {"amb-jaguar": 3, "amb-lacandona": 2})),
    ("q14", "caminos y puentes en mal estado", "semantica",
     ("subtemas", {"infra-carretera": 3, "infra-puente": 3, "riesgo-deslave": 2})),
    ("q15", "exportación de café orgánico", "mixta",
     ("subtemas", {"cafe-exportacion": 3, "cafe-cooperativa": 2, "cafe-precios": 1, "cafe-roya": 1})),
    ("q16", "turismo y artesanías", "mixta",
     ("subtemas", {"turismo-sancristobal": 3, "cult-ambar": 2, "cult-textiles": 2, "eco-artesanas": 2, "turismo-hoteles": 1})),
    ("q17", "huracán y protección civil", "mixta",
     ("subtemas", {"riesgo-tormenta": 3, "riesgo-inundacion": 2, "riesgo-simulacro": 1, "riesgo-sismo": 1})),
    ("q18", "robótica en escuelas", "mixta", ("subtemas", {"tec-robotica": 3, "tec-bootcamp": 1, "tec-becas": 1})),
    ("q19", "cacao y chocolate", "mixta", ("subtemas", {"cacao-soconusco": 3, "cacao-chocolate": 3})),
    ("q20", "mercado de mango y fruta", "mixta", ("subtemas", {"eco-mango": 3, "eco-mercado": 2, "eco-frontera": 1})),
]


def construir(docs):
    consultas = []
    for qid, texto, tipo, (modo, regla) in CONSULTAS:
        if modo == "literal":
            clave = sin_acentos(regla)
            rel = {d["id"]: 3 for d in docs if clave in sin_acentos(d["titulo"] + " " + d["texto"])}
        else:
            rel = {d["id"]: regla[d["subtema"]] for d in docs if d["subtema"] in regla}
        if not rel:
            raise ValueError(f"{qid} '{texto}' no tiene documentos relevantes")
        consultas.append({"id": qid, "texto": texto, "tipo": tipo, "relevancia": rel})
    return consultas


if __name__ == "__main__":
    docs = json.loads((RAIZ / "data" / "corpus.json").read_text(encoding="utf-8"))["documentos"]
    consultas = construir(docs)
    for c in consultas:
        print(f'{c["id"]} [{c["tipo"]:9s}] {c["texto"]:42s} -> {len(c["relevancia"])} relevantes {sorted(c["relevancia"])[:6]}')
    (RAIZ / "data" / "qrels.json").write_text(json.dumps({"consultas": consultas}, ensure_ascii=False, indent=1), encoding="utf-8")
    print("\nescrito data/qrels.json")
