import math

import pytest

from backend.app.evaluation import mrr, ndcg_at_k, precision_at_k, recall_at_k
from backend.app.metrics import LatencyRecorder, percentiles


def test_ndcg_ideal_y_peor():
    rel = {"a": 3, "b": 1}
    assert ndcg_at_k(["a", "b"], rel) == pytest.approx(1.0)
    dcg = 1 / math.log2(2) + 7 / math.log2(3)
    assert ndcg_at_k(["b", "a"], rel) == pytest.approx((1 + 7 / math.log2(3)) / (7 + 1 / math.log2(3)))
    assert ndcg_at_k(["z"], rel) == 0 and dcg > 0


def test_mrr_recall_precision():
    rel = {"a": 1, "b": 2}
    assert mrr(["x", "a"], rel) == 0.5 and mrr(["x"], rel) == 0
    assert recall_at_k(["a", "x"], rel, 5) == 0.5
    assert precision_at_k(["a", "b", "x", "y", "z"], rel, 5) == 0.4


def test_percentiles():
    p = percentiles(list(range(1, 101)))
    assert p["p50"] == pytest.approx(50.5) and p["p95"] == pytest.approx(95.05)
    assert percentiles([])["p50"] is None


def test_recorder_ventana_y_reset():
    r = LatencyRecorder(window=3)
    for v in (1, 2, 3, 4):
        r.record("m", v)
    s = r.snapshot()["m"]
    assert s["count"] == 3 and s["max"] == 4
    r.reset()
    assert r.snapshot() == {}
