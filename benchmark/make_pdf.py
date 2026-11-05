"""Genera el reporte PDF de la Tarea 4 (reportlab) a partir de los resultados medidos."""
import json
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Image, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

RAIZ = Path(__file__).resolve().parents[1]
R, D = RAIZ / "benchmark" / "results", RAIZ / "docs"
F = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DV", F + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVB", F + "DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DVM", F + "DejaVuSansMono.ttf"))
pdfmetrics.registerFontFamily("DV", normal="DV", bold="DVB", italic="DV", boldItalic="DVB")
NAVY, CORAL = colors.HexColor("#1C3257"), colors.HexColor("#E08A6E")
ss = getSampleStyleSheet()
B = ParagraphStyle("B", parent=ss["BodyText"], fontName="DV", fontSize=9.2, leading=13.2, alignment=TA_JUSTIFY, spaceAfter=5)
H1 = ParagraphStyle("H1", fontName="DVB", fontSize=14, textColor=NAVY, spaceBefore=10, spaceAfter=6, keepWithNext=1)
H2 = ParagraphStyle("H2", fontName="DVB", fontSize=10.5, textColor=CORAL, spaceBefore=6, spaceAfter=3)
T = ParagraphStyle("T", parent=B, fontSize=8, leading=10.5, alignment=0, spaceAfter=0)
TB = ParagraphStyle("TB", parent=T, fontName="DVB")
CAP = ParagraphStyle("CAP", parent=B, fontSize=8, textColor=colors.grey, alignment=1)
J = lambda n: json.loads((R / n).read_text(encoding="utf-8"))
q, think, stress, esc, st = J("quality.json"), J("load_test_think500.json")["resultados"], J("load_test_stress.json")["resultados"], J("scalability.json"), J("startup.json")
NOM = {"tfidf": "TF-IDF", "bm25": "BM25", "embeddings": "Embeddings", "hybrid": "Híbrido RRF"}
p = lambda t, s=B: Paragraph(t, s)


def tabla(filas, anchos, cab=True):
    data = [[Paragraph(str(c), TB if (cab and i == 0) else T) for c in f] for i, f in enumerate(filas)]
    t = Table(data, colWidths=[a * cm for a in anchos], repeatRows=1)
    est = [("GRID", (0, 0), (-1, -1), .3, colors.HexColor("#C5CCDA")), ("VALIGN", (0, 0), (-1, -1), "TOP"),
           ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]
    if cab:
        est += [("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E6ECF6"))]
    t.setStyle(TableStyle(est))
    return t


def img(n, w):
    from PIL import Image as PI
    iw, ih = PI.open(D / n).size
    return Image(str(D / n), width=w * cm, height=w * cm * ih / iw)


S = []
S += [Spacer(1, 2 * cm), p("Universidad Politécnica de Chiapas · Minería de Datos · Corte 2", ParagraphStyle("c", parent=B, alignment=1, textColor=CORAL)),
      p("TAREA 4: INTEGRACIÓN DE MOTORES DE BÚSQUEDA", ParagraphStyle("t", fontName="DVB", fontSize=20, textColor=NAVY, alignment=1, leading=25, spaceBefore=14, spaceAfter=14)),
      p("Sistema fullstack con TF-IDF, BM25, Embeddings y búsqueda híbrida (RRF): comparación de calidad, latencia p50/p95 y prueba con hasta 50 usuarios concurrentes", ParagraphStyle("s", parent=B, alignment=1, fontSize=11, leading=15)),
      Spacer(1, 1.2 * cm), p("<b>Francisco Corzo Pérez</b> · Matrícula 233296", ParagraphStyle("a", parent=B, alignment=1, fontSize=11)),
      p("CORZO_PEREZ_FRANCISCO_233296_C2_T4_INTEGRACION", ParagraphStyle("n", parent=B, alignment=1, fontName="DVM", fontSize=9)), Spacer(1, 1 * cm), img("fig_arquitectura.png", 15)]
S += [Spacer(1, .8 * cm), p("<b>Resumen.</b> Se construyó un buscador fullstack (FastAPI + frontend web) que sirve los motores de las tareas anteriores sobre un corpus de 60 documentos de 106 a 121 palabras. "
      "El híbrido RRF obtuvo la mejor calidad (nDCG@5 0.908), BM25 fue el mejor motor léxico y los embeddings ganaron en consultas semánticas pero fallaron en términos literales. "
      "Con 50 usuarios concurrentes y una pausa de 500 ms entre consultas, la latencia de extremo a extremo fue p50 4.4 ms y p95 12.2 ms, sin errores; sin pausa (estrés) subió a p50 97 ms y p95 442 ms por saturación de la máquina de pruebas, no de los motores. "
      "<b>Aviso de honestidad:</b> el corpus es sintético (redactado para el proyecto) y los qrels se derivan de reglas; no se hizo web scraping contra el sitio real porque el entorno no tuvo acceso, así que no se reclaman los puntos extra.")]
S += [PageBreak(), p("1. Corpus y consultas de evaluación", H1),
      p("<b>Corpus.</b> 60 documentos tipo nota periodística sobre Chiapas, en 10 temas × 6 documentos (agua, café y cacao, turismo, salud, riesgos naturales, tecnología, infraestructura, medio ambiente, economía, cultura). "
        "Cada texto tiene entre 106 y 121 palabras (media 114.1; 6,844 en total), cumpliendo los mínimos del enunciado (≥50 documentos, ≥100 palabras). Los textos son originales, redactados para este proyecto: los lugares son reales (Cañón del Sumidero, Soconusco, Palenque…) pero los sucesos son ilustrativos y no deben leerse como noticias reales."),
      p("<b>Consultas y juicios de relevancia.</b> 20 consultas en tres tipos: 6 léxicas (expresión literal: «Cañón del Sumidero», «Soconusco», «Aedes aegypti», «marimba», «Lacandona», «pozol»), 8 semánticas (parafrasean sin repetir las palabras del documento: «temblor fuerte», «enfermedad transmitida por zancudos»…) y 6 mixtas («exportación de café orgánico», «cacao y chocolate»…). "
        "Relevancia graduada 1–3: en las léxicas es 3 si el documento contiene la expresión; en las demás se asigna por subtema. <b>Limitación:</b> como los qrels salen del mismo diseño del corpus, sirven para comparar motores entre sí, no como medida absoluta de calidad."),
      p("2. Desarrollo del sistema", H1),
      p("<b>Backend (FastAPI).</b> Carga el corpus y construye los 4 índices al arrancar (≈3.8 s, ≈1 GB de memoria por el modelo de vectores). Endpoints: <font name='DVM'>/api/search?q&amp;engine&amp;k</font>, <font name='DVM'>/api/compare</font> (los 4 motores y el solapamiento Jaccard), <font name='DVM'>/api/documents[/id]</font>, <font name='DVM'>/api/engines</font>, <font name='DVM'>/api/health</font> y <font name='DVM'>/api/stats</font> (p50/p95/p99 acumulados por motor). Cada búsqueda mide su tiempo con <font name='DVM'>perf_counter</font> y lo registra en un recolector con ventana de 20,000 muestras seguro entre hilos."),
      p("<b>Motores.</b> TF-IDF (tf=f/|d|, idf=ln(N/df), coseno) y BM25 (k1=1.5, b=0.75) con índice invertido en NumPy y pesos precalculados; Embeddings con el promedio de los vectores de palabras de spaCy <i>es_core_news_lg</i> (300 d) y coseno sobre una matriz normalizada; Híbrido con RRF (k=60) sobre BM25 y Embeddings. Usan dos preprocesamientos distintos: el léxico (sin acentos, stopwords salvo 13 palabras como «no» o «sin», stemming Snowball) y el de palabras completas con acentos y sin stemming para los vectores."),
      p("<b>Frontend.</b> Página web sin frameworks con tres pestañas: <i>Buscar</i> (selector de motor, resaltado de términos, vista del documento), <i>Comparar</i> (los 4 motores lado a lado con su latencia y Jaccard) y <i>Latencia</i> (p50/p95/p99 del servidor). Las funciones puras (resaltado, formato, Jaccard) se prueban con Node y el flujo completo con jsdom contra la API real."),
      p("<b>Pruebas.</b> 36 pruebas de pytest (los motores contra fórmulas ingenuas independientes, el cálculo exacto de RRF, las métricas, la API en modos <i>threadpool</i> e <i>inline</i>, los requisitos del corpus y el scraper con HTML de muestra, además de una prueba con los vectores reales) y 7 pruebas unitarias más 1 de DOM en el frontend. Todas pasan.")]
S += [PageBreak(), p("3. Comportamiento de los motores", H1),
      tabla([["Motor", "nDCG@5", "MRR", "R@5", "nDCG léxicas", "nDCG semánticas", "nDCG mixtas"]] +
            [[NOM[m], f"{q[m]['global']['ndcg']:.3f}", f"{q[m]['global']['mrr']:.3f}", f"{q[m]['global']['recall']:.3f}", f"{q[m]['por_tipo']['lexica']['ndcg']:.3f}", f"{q[m]['por_tipo']['semantica']['ndcg']:.3f}", f"{q[m]['por_tipo']['mixta']['ndcg']:.3f}"] for m in NOM],
            [3, 2, 2, 2, 2.4, 2.8, 2.4]), Spacer(1, 6), img("fig_calidad.png", 13), p("Figura 1. nDCG@5 por tipo de consulta (20 consultas).", CAP),
      p("<b>TF-IDF y BM25</b> son perfectos en consultas literales (nDCG 1.0): «Aedes aegypti» devuelve solo el documento del dengue. BM25 supera por poco a TF-IDF (0.868 vs 0.860) por la saturación de frecuencia y la normalización por longitud, que con documentos de longitud casi uniforme aportan poco. Su debilidad es el vocabulario: «enfermedad transmitida por zancudos» no comparte palabras con el texto del dengue (que no dice «zancudo»); el acierto del primer lugar se debe a que «enfermedad» sí aparece, y el resto del ranking es ruido léxico (roya del café, fiesta)."),
      p("<b>Embeddings</b> son los mejores en consultas semánticas (0.856), pero los peores en léxicas (0.649): promedian vectores y diluyen los nombres propios y términos raros. «Aedes aegypti» sí trae el documento correcto primero, pero rellena con documentos sin relación (jaguar, inundación); «cacao y chocolate» pone un documento de tamales antes que uno del cacao. Dan resultados siempre, aun cuando no hay nada relevante, y no distinguen bien lo que es una coincidencia exacta."),
      p("<b>Híbrido RRF</b> obtiene el mejor equilibrio (nDCG 0.908, MRR 1.000, R@5 0.790): mantiene el 1.0 en léxicas y sube las semánticas a 0.900, porque el documento que ambas listas coinciden en rankear alto gana sobre el que solo una propone. En consultas mixtas (0.826) no mejora a BM25 (0.830): ahí el aporte de los embeddings es neutro. «Temblor fuerte» ilustra la fusión: BM25 pone el simulacro primero, los embeddings el sismo, y RRF coloca ambos relevantes en el top 3.")]
S += [p("4. Latencia p50/p95 y 50 usuarios concurrentes", H1),
      p("<b>Método.</b> Generador de carga asíncrono (httpx) con N usuarios en <i>bucle cerrado</i>: cada uno elige consulta y motor al azar entre las 20 consultas y los 4 motores, espera la respuesta, hace una pausa aleatoria de 250–750 ms (tiempo de lectura de una persona) y repite durante 15 s. Se probaron 1, 10, 25 y 50 usuarios, más una variante de estrés sin pausa. Se reporta la latencia de extremo a extremo (cliente) y la del servidor (solo la búsqueda). <b>Entorno:</b> 2 vCPU, 8 GB de RAM, un solo proceso de uvicorn; <u>servidor y generador de carga comparten la misma máquina</u>, por lo que compiten por CPU y los números del estrés son pesimistas."),
      tabla([["Usuarios", "Peticiones", "Errores", "req/s", "p50 (ms)", "p95 (ms)", "p99 (ms)", "p50 / p95 búsqueda en servidor (ms)"]] +
            [[r["usuarios"], r["peticiones"], r["errores"], r["rps"], f"{r['e2e_ms']['p50']:.2f}", f"{r['e2e_ms']['p95']:.2f}", f"{r['e2e_ms']['p99']:.2f}",
              f"{sum(v['p50'] for v in r['servidor_ms'].values())/4:.2f} / {sum(v['p95'] for v in r['servidor_ms'].values())/4:.2f}"] for r in think], [1.9, 2.2, 1.6, 1.4, 1.8, 1.8, 1.8, 4.4]),
      p("Tabla 1. Carga con pausa de ~500 ms (comportamiento de usuarios reales).", CAP),
      tabla([["Usuarios", "Peticiones", "Errores", "req/s", "p50 (ms)", "p95 (ms)", "p99 (ms)"]] +
            [[r["usuarios"], r["peticiones"], r["errores"], r["rps"], f"{r['e2e_ms']['p50']:.2f}", f"{r['e2e_ms']['p95']:.2f}", f"{r['e2e_ms']['p99']:.2f}"] for r in stress], [2, 2.4, 2, 2, 2.4, 2.4, 2.4]),
      p("Tabla 2. Carga sin pausa (cada usuario dispara la siguiente consulta al recibir la respuesta).", CAP), img("fig_latencia.png", 14.5), p("Figura 2. Latencia de extremo a extremo vs. usuarios concurrentes.", CAP)]
mot = think[-1]["por_motor_e2e"]
S += [p("<b>Lectura.</b> Con 50 usuarios y pausa realista el sistema respondió <b>sin errores</b> con p50 de 4.41 ms y p95 de 12.20 ms (≈97 req/s); la búsqueda en sí toma 0.1–0.5 ms en el servidor, así que casi todo el tiempo es red local, FastAPI y serialización. Por motor, con 50 usuarios (extremo a extremo, p50/p95): " +
        "; ".join(f"{NOM[m]} {mot[m]['p50']:.2f}/{mot[m]['p95']:.2f} ms" for m in NOM) + ". Las diferencias entre motores (≈0.3 ms) son menores que el ruido de la red, por lo que <b>a esta escala la latencia no debe ser el criterio para escoger motor</b>. "
        "En estrés el sistema se satura en ≈350–560 req/s: la cola de peticiones, no el cálculo, hace crecer p95 (442 ms con 50 usuarios), un régimen mucho más duro que el uso humano. El modo <i>threadpool</i> vs. <i>inline</i> de FastAPI no mostró una diferencia concluyente en este tamaño de corpus.")]
S += [PageBreak(), p("5. Escalabilidad del corpus", H1),
      p("Como 60 documentos no distinguen los motores por costo, se replicó el corpus a 600, 6,000 y 30,000 documentos y se midió la búsqueda en proceso (150 consultas por motor)."),
      tabla([["Documentos", "Indexado (s)", "TF-IDF p50/p95", "BM25 p50/p95", "Embeddings p50/p95", "Híbrido p50/p95"]] +
            [[f["docs"], f["indexado_s"]] + [f"{f['motores'][m]['p50']:.2f} / {f['motores'][m]['p95']:.2f}" for m in NOM] for f in esc], [2.6, 2.6, 2.8, 2.8, 3.4, 2.8]),
      p("Tabla 3. Latencia de búsqueda en ms según el tamaño del corpus.", CAP), img("fig_escala.png", 11),
      p("Los motores léxicos crecen poco (el índice invertido solo toca los documentos que contienen los términos: 0.15 ms con 30,000), mientras que los embeddings y el híbrido crecen casi linealmente (3.8 y 5.4 ms) porque multiplican la consulta por toda la matriz N×300. Con corpus mucho mayores los embeddings requerirían un índice aproximado (ANN, p. ej. HNSW). Nota: esta réplica repite los textos, por lo que mide costo y no calidad.")]
S += [p("6. Criterio de decisión", H1),
      p("Se decidió con tres criterios, en este orden: (1) <b>calidad</b> (nDCG@5/MRR global y por tipo de consulta), (2) <b>robustez</b> (qué pasa cuando falla un componente o la consulta es rara) y (3) <b>costo</b> (latencia, memoria y complejidad de despliegue). Aplicados a los datos:"),
      tabla([["Criterio", "TF-IDF", "BM25", "Embeddings", "Híbrido RRF"],
             ["Calidad global (nDCG@5)", "0.860", "0.868", "0.762", "<b>0.908</b>"],
             ["Términos literales / nombres propios", "Excelente", "Excelente", "Débil", "Excelente"],
             ["Paráfrasis / sinónimos", "Débil", "Débil", "Buena", "Buena"],
             ["Latencia con 30,000 docs (p50)", "0.29 ms", "<b>0.15 ms</b>", "3.8 ms", "5.4 ms"],
             ["Memoria / arranque", "Mínima", "Mínima", "≈1 GB y ≈4 s (modelo)", "≈1 GB y ≈4 s"],
             ["Robustez", "Silencio si no hay palabras comunes", "Igual", "Siempre responde, aunque sea ruido", "Un componente mudo no lo rompe"]], [4.3, 3, 2.7, 3.7, 3.2]),
      Spacer(1, 6),
      p("<b>Decisión:</b> el híbrido RRF es la opción predeterminada del sistema, porque su ganancia en calidad (+0.04 sobre BM25, +0.15 sobre embeddings solos) cuesta milisegundos que ningún usuario percibe a esta escala. <b>BM25</b> es la alternativa cuando se necesita ligereza (sin modelo de vectores, 1 GB menos de memoria) o los usuarios buscan sobre todo nombres, siglas y códigos. TF-IDF queda como línea base: no ofrece ventaja sobre BM25 salvo simplicidad. Los embeddings solos no se recomiendan como único motor."),
      p("7. Cuándo usar cada corpus", H1),
      p("<b>Corpus sintético de este proyecto (60 documentos).</b> Sirve para desarrollar, probar y comparar motores de forma reproducible y controlada (sabemos exactamente qué documento es relevante); no para afirmar calidad en producción. Se usaría en pruebas automáticas, demostraciones y en la validación de que el sistema cumple el flujo completo."),
      p("<b>Corpus real o scrapeado (p. ej. Wikipedia o noticias reales).</b> Se usaría para evaluar con vocabulario, ruido y longitud reales, y para decidir de verdad el motor: el ruido (HTML, siglas, errores ortográficos) afecta distinto a cada motor. El scraper está en el repositorio (<font name='DVM'>scripts/scrape_corpus.py</font>) y la prueba de escalabilidad (30,000 documentos) indica que, con corpus grandes, convendría el híbrido con índice aproximado para la parte vectorial."),
      p("<b>Corpus de las tareas 1–3 (14 documentos).</b> Demasiado pequeño para medir latencia o estabilidad de las métricas; sirvió para entender las fórmulas, no para decidir.")]
S += [p("8. Ventajas y desventajas observadas", H1),
      tabla([["Motor", "Ventajas", "Desventajas"],
             ["TF-IDF", "Simple, explicable (cada peso se puede calcular a mano); muy rápido; sin modelos.", "No satura la frecuencia ni normaliza bien la longitud; ciego a sinónimos; sin resultados si no hay palabras comunes."],
             ["BM25", "Mejor motor léxico; el más rápido y el que mejor escala (0.15 ms con 30,000 docs); precisión perfecta en nombres propios.", "Mismos límites de vocabulario: «temblor» no encuentra «sismo»; depende del preprocesamiento (stemming, stopwords)."],
             ["Embeddings", "Capta paráfrasis y relaciones temáticas; mejor en consultas semánticas.", "Diluye nombres propios y términos raros; siempre devuelve algo (ruido); ≈1 GB de modelo; crece linealmente con el corpus; vector nulo para siglas fuera de vocabulario."],
             ["Híbrido RRF", "Mejor calidad global; combina las fortalezas sin ajustar pesos ni normalizar scores; tolera que un componente no responda.", "El costo es la suma de ambos; las mejoras son pequeñas en consultas mixtas; es más difícil de explicar y depurar."]], [2.4, 7, 7.5]),
      p("9. Alcance, limitaciones y web scraping", H1),
      p("<b>Web scraping (puntos extra): no se reclaman.</b> Se escribió un scraper (respeta robots.txt, User-Agent identificable, 1 s de pausa, extracción con BeautifulSoup, ≥100 palabras, genera la lista de fuentes con URL, fecha y licencia CC BY-SA 4.0) con 80 artículos semilla de Wikipedia en español, pero el entorno donde se desarrolló el proyecto no tuvo acceso a es.wikipedia.org, por lo que solo se probó con HTML de muestra y <u>nunca se ejecutó contra el sitio real</u>. El corpus entregado es sintético y no hay fuentes externas que citar. Para obtener los puntos extra se ejecuta <font name='DVM'>make scrape</font> con red y se adjunta <font name='DVM'>data/sources_scraped.md</font>."),
      p("<b>Otras limitaciones.</b> (a) Los qrels derivan de reglas, no de anotadores independientes, y con 20 consultas las diferencias pequeñas (p. ej. TF-IDF vs. BM25) no son estadísticamente concluyentes. (b) Las pruebas de carga corren con servidor y cliente en la misma máquina de 2 vCPU. (c) El backend SBERT está implementado pero no se probó. (d) Los números de latencia absolutos dependen del hardware; son útiles por comparación entre motores y niveles de carga."),
      p("10. Reproducción y repositorio", H1),
      p("<font name='DVM'>make install &amp;&amp; make model &amp;&amp; make test</font> (pruebas) · <font name='DVM'>make run</font> (servidor en el puerto 8000 con el frontend en «/») · <font name='DVM'>make eval</font> · <font name='DVM'>make loadtest</font> / <font name='DVM'>make loadtest-stress</font> · <font name='DVM'>make scalability</font> · <font name='DVM'>make report</font>. "
        "Repositorio: <b>CORZO_PEREZ_FRANCISCO_233296_C2_T4_INTEGRACION</b> (código, datos, pruebas, benchmarks y resultados crudos en <font name='DVM'>benchmark/results/</font>)."),
      p("<b>Fuentes.</b> Corpus: textos originales redactados para el proyecto (sin fuentes externas). Vectores: modelo <i>es_core_news_lg</i> de spaCy (fastText, Explosion). Repositorio de la materia: github.com/RamsesCamas/DataMining_Slices_and_Code.")]


def pie(c, d):
    c.saveState(); c.setFont("DV", 7.5); c.setFillColor(colors.grey)
    c.drawString(2 * cm, 1.2 * cm, "CORZO PÉREZ FRANCISCO · 233296 · C2 T4 Integración"); c.drawRightString(letter[0] - 2 * cm, 1.2 * cm, f"Página {d.page}"); c.restoreState()


out = RAIZ / "CORZO_PEREZ_FRANCISCO_233296_C2_T4_INTEGRACION.pdf"
SimpleDocTemplate(str(out), pagesize=letter, leftMargin=2 * cm, rightMargin=2 * cm, topMargin=1.8 * cm, bottomMargin=2 * cm,
                  title="Tarea 4 - Integración de motores de búsqueda", author="Francisco Corzo Pérez").build(S, onFirstPage=pie, onLaterPages=pie)
print("ok", out)
