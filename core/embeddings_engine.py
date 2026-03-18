# core/embeddings_engine.py

from typing import List
import numpy as np

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class EmbeddingsEngine:
    """
    Lightweight wrapper around embedding model usage.

    Separates model loading and similarity logic from
    intent detection to keep components modular and reusable.
    """

    def __init__(self, model_name: str = "BAAI/bge-small-en-v1.5"):
        self.model_name = model_name
        self.model = SentenceTransformer(model_name)

    def encode(self, texts: List[str]) -> np.ndarray:
        """
        Convert a list of texts into embeddings.
        """
        return self.model.encode(texts)

    def similarity(self, query: np.ndarray, candidates: np.ndarray) -> float:
        """
        Compute max cosine similarity between query and candidate embeddings.
        """
        similarities = cosine_similarity([query], candidates)[0]
        return float(np.max(similarities))

    def best_match(self, query_text: str, candidates: List[str]):
        """
        Utility function to find the best matching candidate for a given query.
        """
        query_embedding = self.encode([query_text])[0]
        candidate_embeddings = self.encode(candidates)

        score = self.similarity(query_embedding, candidate_embeddings)

        best_index = int(np.argmax(
            cosine_similarity([query_embedding], candidate_embeddings)[0]
        ))

        return {
            "match": candidates[best_index],
            "confidence": round(score, 3)
        }