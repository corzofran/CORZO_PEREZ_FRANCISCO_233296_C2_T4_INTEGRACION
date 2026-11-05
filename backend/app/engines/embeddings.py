"""Motor semántico: promedio de vectores de palabras (spaCy) o embeddings de oraciones (SBERT, opcional)."""
import numpy as np

from ..preprocess import tokens_palabras
from .base import Engine, top_k


class SpacyVectorBackend:
    name = "spacy"

    def __init__(self, model="es_core_news_lg"):
        import spacy
        self.nlp = spacy.load(model, disable=["tagger", "parser", "ner", "attribute_ruler", "lemmatizer", "morphologizer"])
        self.vocab = self.nlp.vocab
        self.dim = self.vocab.vectors_length

    def encode(self, textos):
        out = np.zeros((len(textos), self.dim), dtype=np.float32)
        for i, t in enumerate(textos):
            vs = [self.vocab[p].vector for p in tokens_palabras(t) if self.vocab[p].has_vector]
            if vs:
                out[i] = np.mean(vs, axis=0)
        return out


class SbertBackend:
    """Opcional (no probado en este proyecto): requiere `pip install sentence-transformers`."""
    name = "sbert"

    def __init__(self, model):
        from sentence_transformers import SentenceTransformer
        self.model = SentenceTransformer(model)
        self.dim = self.model.get_sentence_embedding_dimension()

    def encode(self, textos):
        return np.asarray(self.model.encode(list(textos), show_progress_bar=False), dtype=np.float32)


def build_backend(settings):
    if settings.embeddings_backend == "sbert":
        return SbertBackend(settings.sbert_model)
    return SpacyVectorBackend(settings.spacy_model)


class EmbeddingEngine(Engine):
    name, label = "embeddings", "Embeddings"
    description = "Promedio de vectores de palabras (300 d) y coseno sobre una matriz normalizada."

    def __init__(self, corpus, backend):
        self.backend = backend
        self.ids = [d.id for d in corpus.documentos]
        m = backend.encode([d.texto_indexable for d in corpus.documentos])
        self.matrix = self._normalizar(m)

    @staticmethod
    def _normalizar(m):
        n = np.linalg.norm(m, axis=1, keepdims=True)
        n[n == 0] = 1.0
        return m / n

    def search(self, query, k=10):
        q = self.backend.encode([query])
        if not np.any(q):  # sin vector (siglas/OOV): no hay resultados
            return []
        q = self._normalizar(q)[0]
        return top_k(self.matrix @ q, self.ids, k)
