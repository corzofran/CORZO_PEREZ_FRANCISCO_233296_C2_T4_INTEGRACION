# CORZO_PEREZ_FRANCISCO_233296_C2_T4_INTEGRACION

Tarea 4 (Corte 2, Minería de Datos): buscador fullstack que integra TF-IDF, BM25, Embeddings y búsqueda híbrida (RRF).
Autor: Francisco Corzo Pérez (233296). Reporte: `CORZO_PEREZ_FRANCISCO_233296_C2_T4_INTEGRACION.pdf`.

## Contenido
- `backend/app/`: FastAPI, motores (`engines/`), preprocesamiento, métricas y evaluación.
- `frontend/`: página web (Buscar · Comparar · Latencia) servida por el mismo backend en `/`.
- `data/`: `corpus.json` (60 documentos sintéticos, 106–121 palabras), `qrels.json` (20 consultas), `scrape_seeds.json`.
- `benchmark/`: calidad, prueba de carga (1–50 usuarios, p50/p95), escalabilidad, arranque; `results/` con los datos crudos.
- `scripts/`: construcción del corpus/qrels y scraper opcional de Wikipedia.
- `docs/`: `ARQUITECTURA.md`, `RESULTADOS.md` y figuras.

## Uso
```bash
make install && make model   # dependencias y modelo es_core_news_lg de spaCy
make test                    # pytest (36 pruebas)
make run                     # http://127.0.0.1:8000  (frontend + API)
make eval loadtest loadtest-stress scalability report
make test-frontend           # pruebas Node + jsdom contra la API real
```

## Honestidad sobre el alcance
- El corpus es **sintético** (textos originales redactados para el proyecto; lugares reales, sucesos ilustrativos) y los qrels se derivan de reglas: sirven para comparar motores, no como medida absoluta.
- El scraper (`make scrape`) **no se ejecutó contra el sitio real** (sin acceso a Wikipedia en el entorno de desarrollo); solo se probó con HTML de muestra.
- Las pruebas de carga corrieron con cliente y servidor en la misma máquina (2 vCPU, 8 GB).
- El backend de embeddings `sbert` está implementado pero no se probó.
