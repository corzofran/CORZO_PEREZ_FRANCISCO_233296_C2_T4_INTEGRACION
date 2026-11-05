"""Dos preprocesamientos: léxico (TF-IDF/BM25) y de palabras completas (embeddings)."""
import re
import unicodedata
from functools import lru_cache

from nltk.stem.snowball import SpanishStemmer
from spacy.lang.es.stop_words import STOP_WORDS

# Palabras que spaCy marca como stopwords pero que cambian el sentido o son útiles para buscar.
CONSERVAR = {"no", "sin", "nunca", "tampoco", "nada", "ni", "mas", "menos", "poco", "mucho", "bajo", "alto", "contra"}

_HTML = re.compile(r"<[^>]+>")
_URL = re.compile(r"https?://\S+|www\.\S+")
_EMOJI = re.compile("[\U0001F000-\U0001FAFF\U00002600-\U000027BF\U0000FE0F]")
_PALABRA = re.compile(r"[^\W\d_]+", re.UNICODE)

_stemmer = SpanishStemmer()


def quitar_diacriticos(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def limpiar(texto: str) -> str:
    texto = _HTML.sub(" ", texto)
    texto = _URL.sub(" ", texto)
    return _EMOJI.sub(" ", texto)


STOP_SIN_ACENTO = {quitar_diacriticos(w) for w in STOP_WORDS} - CONSERVAR
STOP_CON_ACENTO = {w.lower() for w in STOP_WORDS if quitar_diacriticos(w) not in CONSERVAR}


@lru_cache(maxsize=200_000)
def _stem(palabra: str) -> str:
    return _stemmer.stem(palabra)


def tokens_lexicos(texto: str) -> list:
    """minúsculas, sin HTML/URL/emoji, sin acentos, sin stopwords (menos CONSERVAR), sin números, stemming."""
    t = quitar_diacriticos(limpiar(texto).lower())
    return [_stem(p) for p in _PALABRA.findall(t) if p not in STOP_SIN_ACENTO and len(p) > 1]


def tokens_palabras(texto: str) -> list:
    """palabras completas con acentos, sin stopwords ni números y sin stemming (para vectores de palabras)."""
    t = limpiar(texto).lower()
    return [p for p in _PALABRA.findall(t) if p not in STOP_CON_ACENTO and len(p) > 1]
