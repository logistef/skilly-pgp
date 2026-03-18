# core/intent_detector.py

from dataclasses import dataclass
from typing import List, Dict
import numpy as np

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


@dataclass
class IntentResult:
    intent: str
    confidence: float
    actionable: bool


class Skilly:
    """
    Minimal implementation of the Parallel Guardian Pattern (PGP) intent detector.

    Uses embedding similarity to match user input against predefined intents.
    """

    def __init__(self, model_name: str = "BAAI/bge-small-en-v1.5"):
        self.model = SentenceTransformer(model_name)

        # Define a small, clean intent space
        self.intents: Dict[str, List[str]] = {
            "filesystem.list": [
                "list files",
                "show files",
                "what is in this folder",
                "list directory contents"
            ],
            "search.web": [
                "search the web",
                "look up information",
                "find online",
                "search for"
            ],
            "system.monitor": [
                "check cpu usage",
                "show system status",
                "monitor system",
                "check memory usage"
            ],
        }

        # Precompute embeddings for intent examples
        self.intent_embeddings = {
            intent: self.model.encode(phrases)
            for intent, phrases in self.intents.items()
        }

    def analyze(self, role: str, text: str) -> IntentResult:
        """
        Analyze user input and return best matching intent.
        """

        query_embedding = self.model.encode([text])[0]

        best_intent = None
        best_score = 0.0

        for intent, embeddings in self.intent_embeddings.items():
            similarities = cosine_similarity(
                [query_embedding],
                embeddings
            )[0]

            score = float(np.max(similarities))

            if score > best_score:
                best_score = score
                best_intent = intent

        actionable = best_score > 0.6

        return IntentResult(
            intent=best_intent if best_intent else "none",
            confidence=round(best_score, 3),
            actionable=actionable
        )