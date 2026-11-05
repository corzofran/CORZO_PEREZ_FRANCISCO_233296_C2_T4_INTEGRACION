# Arquitectura y decisiones

```
Navegador (HTML/JS) ──HTTP──▶ FastAPI ──▶ motores en memoria
                                          ├─ TF-IDF   (índice invertido, NumPy)
                                          ├─ BM25     (índice invertido, pesos precalculados)
                                          ├─ Embeddings (promedio de vectores spaCy 300 d, matriz N×300 normalizada)
                                          └─ Híbrido  (RRF de BM25 + Embeddings)
                         LatencyRecorder (p50/p95/p99 por motor)
```

Decisiones:
1. **Dos preprocesamientos.** Léxico (sin acentos, stopwords menos 13 palabras, stemming) para TF-IDF/BM25; palabras completas con acentos y sin stemming para embeddings (los vectores se entrenaron con palabras completas).
2. **Índices invertidos con NumPy**, pesos precalculados al indexar: la búsqueda solo suma vectores por término de la consulta.
3. **RRF y no fusión lineal**: no requiere normalizar scores de escalas distintas y no tiene hiperparámetro α que ajustar.
4. **El híbrido tolera un componente mudo** (p. ej. una sigla sin vector): decide el otro.
5. **Ejecución `threadpool` vs `inline`** (`EXECUTION_MODE`): con búsquedas de ~0.2 ms el pool de hilos aporta poco; se dejó configurable y las diferencias medidas son marginales.
6. **Latencia en dos puntos**: en el servidor (solo búsqueda) y de extremo a extremo (cliente); la diferencia es red local + FastAPI + serialización.
7. **Backend de embeddings y corpus intercambiables** (`EMBEDDINGS_BACKEND`, `CORPUS_PATH`). El backend `sbert` está implementado pero no se probó.
