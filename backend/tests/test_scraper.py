import sys

from backend.app.config import RAIZ

sys.path.insert(0, str(RAIZ / "scripts"))
from scrape_corpus import extraer  # noqa: E402

HTML = "<h1>Café</h1><div id='mw-content-text'>" + "".join(
    f"<p>El café es una bebida que se prepara con granos tostados de cafeto{i} y se consume en todo el mundo cada día.<sup>[1]</sup></p>"
    for i in range(12)) + "</div>"


def test_extraer_ok():
    t, x = extraer(HTML)
    assert t == "Café" and len(x.split()) >= 100 and "[1]" not in x


def test_extraer_descarta_corto():
    assert extraer("<h1>X</h1><div id='mw-content-text'><p>muy corto</p></div>") is None
