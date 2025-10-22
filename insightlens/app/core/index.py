from __future__ import annotations
from pathlib import Path
import json
import faiss
import numpy as np
import pandas as pd

class FaissIndex:
    def __init__(self, index_path: Path, meta_path: Path, dim: int):
        self.index_path = index_path
        self.meta_path = meta_path
        self.dim = dim
        self.meta = pd.DataFrame(columns=["id","text","source","ts","level","extra"])  # metadata
        self.index = faiss.IndexFlatIP(dim)
        self._loaded = False

    def load(self):
        if self.index_path.exists():
            self.index = faiss.read_index(str(self.index_path))
        if self.meta_path.exists():
            self.meta = pd.read_parquet(self.meta_path)
        self._loaded = True

    def save(self):
        self.index_path.parent.mkdir(parents=True, exist_ok=True)
        faiss.write_index(self.index, str(self.index_path))
        self.meta.to_parquet(self.meta_path, index=False)

    def add(self, vecs: np.ndarray, meta_rows: list[dict]):
        if not self._loaded:
            self.load()
        # Ensure normalized for cosine via inner product
        norms = np.linalg.norm(vecs, axis=1, keepdims=True) + 1e-9
        vecs = vecs / norms
        self.index.add(vecs.astype("float32"))
        self.meta = pd.concat([self.meta, pd.DataFrame(meta_rows)], ignore_index=True)

    def search(self, vecs: np.ndarray, k: int = 10):
        if not self._loaded:
            self.load()
        norms = np.linalg.norm(vecs, axis=1, keepdims=True) + 1e-9
        vecs = vecs / norms
        scores, idx = self.index.search(vecs.astype("float32"), k)
        out = []
        for row_scores, row_idx in zip(scores, idx):
            hits = []
            for s, i in zip(row_scores, row_idx):
                if i == -1 or i >= len(self.meta):
                    continue
                hits.append({"score": float(s), **self.meta.iloc[i].to_dict()})
            out.append(hits)
        return out
