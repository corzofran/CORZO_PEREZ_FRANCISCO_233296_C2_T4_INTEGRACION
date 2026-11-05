"""Percentiles y registro de latencias (seguro entre hilos)."""
import threading
from collections import defaultdict, deque

import numpy as np


def percentiles(valores, ps=(50, 95, 99)) -> dict:
    if len(valores) == 0:
        return {f"p{p}": None for p in ps}
    arr = np.asarray(valores, dtype=float)
    return {f"p{p}": float(np.percentile(arr, p)) for p in ps}


class LatencyRecorder:
    def __init__(self, window: int = 20000):
        self.window = window
        self._lock = threading.Lock()
        self._data = defaultdict(lambda: deque(maxlen=self.window))

    def record(self, nombre: str, ms: float):
        with self._lock:
            self._data[nombre].append(float(ms))

    def snapshot(self) -> dict:
        with self._lock:
            copia = {k: list(v) for k, v in self._data.items()}
        out = {}
        for k, v in copia.items():
            out[k] = {"count": len(v), **percentiles(v), "mean": float(np.mean(v)), "max": float(np.max(v))}
        return out

    def reset(self):
        with self._lock:
            self._data.clear()
