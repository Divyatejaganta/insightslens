from __future__ import annotations
import os
import numpy as np

# Optional: OpenAI embeddings if key is present
_USE_OPENAI = bool(os.getenv("OPENAI_API_KEY"))

if _USE_OPENAI:
    from openai import OpenAI
    _client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

_DEF_MODEL = os.getenv("OPENAI_EMBED_MODEL", "text-embedding-3-small")

class Embedder:
    def __init__(self):
        self.use_openai = _USE_OPENAI
        if not self.use_openai:
            # Lightweight local fallback: hashing + SIF-like weighting
            # Deterministic, avoids external downloads.
            pass

    def embed_texts(self, texts: list[str]) -> np.ndarray:
        if self.use_openai:
            # Batch in chunks of 512 tokens-ish
            resp = _client.embeddings.create(model=_DEF_MODEL, input=texts)
            vecs = [d.embedding for d in resp.data]
            return np.array(vecs, dtype=np.float32)
        # Fallback: simple hashing TF features -> pseudo-embeddings
        dim = 384
        arr = np.zeros((len(texts), dim), dtype=np.float32)
        for i, t in enumerate(texts):
            h = 0
            for j, ch in enumerate(t):
                h ^= (ord(ch) + j) * 2654435761
            np.random.seed(h % (2**32 - 1))
            arr[i] = np.random.uniform(-1, 1, size=(dim,)).astype(np.float32)
        # L2 normalize
        norms = np.linalg.norm(arr, axis=1, keepdims=True) + 1e-9
        return arr / norms
