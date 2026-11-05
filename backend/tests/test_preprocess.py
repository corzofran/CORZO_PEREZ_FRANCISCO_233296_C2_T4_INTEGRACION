from backend.app.preprocess import CONSERVAR, limpiar, quitar_diacriticos, tokens_lexicos, tokens_palabras


def test_diacriticos():
    assert quitar_diacriticos("Cañón café") == "Canon cafe"


def test_limpiar_html_url_emoji():
    t = limpiar("<p>Hola</p> https://x.com/a 😀 mundo")
    assert "<" not in t and "http" not in t and "😀" not in t


def test_lexico_stem_y_sin_numeros():
    assert tokens_lexicos("Los cafetales 2024") == tokens_lexicos("cafetal")
    assert "2024" not in tokens_lexicos("año 2024")


def test_lexico_conserva_negacion():
    assert tokens_lexicos("sin agua") and "sin" in tokens_lexicos("sin agua")
    assert "sin" in CONSERVAR


def test_lexico_quita_stopwords():
    assert tokens_lexicos("de la en el") == []


def test_palabras_conserva_acentos_sin_stemming():
    assert tokens_palabras("El café de Chiapas") == ["café", "chiapas"]
