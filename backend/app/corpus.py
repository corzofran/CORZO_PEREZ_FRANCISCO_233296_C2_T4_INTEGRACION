"""Carga del corpus."""
import json
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Document:
    id: str
    titulo: str
    texto: str
    tema: str = ""
    subtema: str = ""
    fuente: str = ""

    @property
    def texto_indexable(self) -> str:
        return f"{self.titulo}. {self.texto}"


@dataclass
class Corpus:
    documentos: list
    nombre: str = ""
    tipo: str = ""
    _por_id: dict = field(default_factory=dict, repr=False)

    def __post_init__(self):
        self._por_id = {d.id: d for d in self.documentos}

    def __len__(self):
        return len(self.documentos)

    def get(self, doc_id):
        return self._por_id.get(doc_id)


def load_corpus(path) -> Corpus:
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    items = raw["documentos"] if isinstance(raw, dict) else raw
    docs = [Document(id=d["id"], titulo=d["titulo"], texto=d["texto"], tema=d.get("tema", ""),
                     subtema=d.get("subtema", ""), fuente=d.get("fuente", "")) for d in items]
    meta = raw if isinstance(raw, dict) else {}
    return Corpus(docs, nombre=meta.get("nombre", ""), tipo=meta.get("tipo", ""))
