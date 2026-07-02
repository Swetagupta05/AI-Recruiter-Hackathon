from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL_NAME

# Global model (loaded only once)
_model = None


def get_embedding_model():
    """
    Returns the SentenceTransformer model.
    Loads it only the first time.
    """
    global _model

    if _model is None:
        print("Loading embedding model...")
        _model = SentenceTransformer(EMBEDDING_MODEL_NAME)

    return _model


def create_embedding(text):
    """
    Convert text into a vector embedding.
    """
    model = get_embedding_model()
    return model.encode(text)