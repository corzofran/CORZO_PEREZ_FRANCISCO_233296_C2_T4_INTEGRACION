# Resultados medidos

Generado por `benchmark/make_report.py`. Cliente y servidor comparten la misma máquina.

## Calidad (20 consultas)

| Motor | nDCG@5 | MRR | R@5 | nDCG léxicas | nDCG semánticas | nDCG mixtas |
|---|---|---|---|---|---|---|
| tfidf | 0.860 | 0.967 | 0.719 | 1.000 | 0.779 | 0.829 |
| bm25 | 0.868 | 0.967 | 0.729 | 1.000 | 0.797 | 0.830 |
| embeddings | 0.762 | 0.838 | 0.697 | 0.649 | 0.856 | 0.749 |
| hybrid | 0.908 | 1.000 | 0.790 | 1.000 | 0.900 | 0.826 |

## Carga con pausa de ~500 ms

| Usuarios | Peticiones | Errores | req/s | p50 ms | p95 ms | p99 ms | p50 servidor | p95 servidor |
|---|---|---|---|---|---|---|---|---|
| 1 | 29 | 0 | 1.9 | 3.84 | 5.20 | 7.11 | 0.30 | 0.63 |
| 10 | 302 | 0 | 19.4 | 4.00 | 6.88 | 22.03 | 0.30 | 0.42 |
| 25 | 761 | 0 | 48.8 | 4.45 | 8.50 | 52.95 | 0.31 | 0.43 |
| 50 | 1513 | 0 | 97.0 | 4.41 | 12.20 | 67.57 | 0.27 | 0.39 |

## Carga sin pausa (estrés)

| Usuarios | Peticiones | Errores | req/s | p50 ms | p95 ms | p99 ms | p50 servidor | p95 servidor |
|---|---|---|---|---|---|---|---|---|
| 1 | 3470 | 0 | 347.0 | 2.74 | 4.06 | 5.15 | 0.22 | 0.34 |
| 10 | 5595 | 0 | 558.5 | 15.29 | 36.69 | 58.33 | 0.20 | 2.09 |
| 25 | 4299 | 0 | 428.5 | 35.92 | 181.05 | 273.77 | 0.19 | 0.45 |
| 50 | 3512 | 0 | 348.0 | 96.82 | 442.20 | 738.95 | 0.20 | 0.50 |

## Escalabilidad (p50 / p95 en ms, k=5, en proceso)

| Documentos | Indexado (s) | TF-IDF | BM25 | Embeddings | Híbrido |
|---|---|---|---|---|---|
| 60 | 0.12 | 0.04 / 0.07 | 0.03 / 0.05 | 0.07 / 0.14 | 0.14 / 0.21 |
| 600 | 0.58 | 0.05 / 0.11 | 0.03 / 0.08 | 0.13 / 0.23 | 0.22 / 0.35 |
| 6000 | 5.71 | 0.07 / 0.14 | 0.05 / 0.09 | 0.48 / 0.59 | 0.62 / 0.76 |
| 30000 | 29.9 | 0.29 / 0.49 | 0.15 / 0.24 | 3.80 / 6.52 | 5.44 / 6.99 |

## Arranque

Tiempo de carga de índices y modelo: 3.79 s; memoria pico: 1026 MB.
