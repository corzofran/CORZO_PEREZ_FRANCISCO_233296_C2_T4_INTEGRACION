import hashlib
import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from backend.app.corpus import Corpus, Document  # noqa: E402
from backend.app.preprocess import tokens_palabras  # noqa: E402


class HashingBackend:
    """Doble de prueba: vector determinista por palabra (hash), sin descargar modelos."""
    name, dim = "hashing", 64

    def encode(self, textos):
        out = np.zeros((len(textos), self.dim), dtype=np.float32)
        for i, t in enumerate(textos):
            vs = [np.random.RandomState(int(hashlib.md5(p.encode()).hexdigest()[:8], 16)).randn(self.dim) for p in tokens_palabras(t)]
            if vs:
                out[i] = np.mean(vs, axis=0)
        return out


TEXTOS = [
    ("El agua potable llega a las colonias", "Las colonias reciben agua potable por tuberías. El agua escasea en verano."),
    ("Café de altura para exportación", "Los productores exportan café orgánico de la sierra a Europa con certificación."),
    ("Sismo de magnitud cinco", "Un sismo sacudió la costa y protección civil revisó las viviendas dañadas."),
    ("Dengue y mosquitos", "El dengue se transmite por el mosquito Aedes aegypti en agua estancada."),
    ("Cacao del Soconusco", "El cacao del Soconusco se fermenta y se convierte en chocolate artesanal."),
    ("Robótica escolar", "Estudiantes construyen robots con sensores y motores para un torneo."),
    ("Marimba en la plaza", "La marimba suena en la plaza durante la fiesta del pueblo."),
    ("Carretera nueva", "La carretera reduce el tiempo de traslado entre dos municipios de la sierra."),
]


@pytest.fixture(scope="session")
def corpus():
    return Corpus([Document(f"t{i}", t, x) for i, (t, x) in enumerate(TEXTOS)])


@pytest.fixture(scope="session")
def backend():
    return HashingBackend()
