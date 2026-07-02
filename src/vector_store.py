import json
import numpy as np
import faiss
from tqdm import tqdm

from config import (
    EMBEDDINGS_FILE,
    IDS_FILE,
    FAISS_INDEX_FILE,
    BATCH_SIZE,
)

from data_loader import load_candidates
from preprocess import candidate_to_text
from embedding_model import get_embedding_model


def build_vector_store():
    """
    Generate embeddings for all candidates and build a FAISS index.
    """

    print("Loading candidates...")

    candidates = load_candidates()

    print(f"Loaded {len(candidates)} candidates")

    model = get_embedding_model()

    texts = []
    ids = []

    for candidate in candidates:
        texts.append(candidate_to_text(candidate))
        ids.append(candidate["candidate_id"])

    print("Generating embeddings...")

    embeddings = model.encode(
        texts,
        batch_size=BATCH_SIZE,
        show_progress_bar=True,
        convert_to_numpy=True,
    )

    embeddings = embeddings.astype("float32")

    print("Saving embeddings...")

    np.save(EMBEDDINGS_FILE, embeddings)

    with open(IDS_FILE, "w") as f:
        json.dump(ids, f)

    print("Building FAISS index...")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatIP(dimension)

    faiss.normalize_L2(embeddings)

    index.add(embeddings)

    faiss.write_index(index, str(FAISS_INDEX_FILE))

    print("Done!")

    print(f"Indexed {index.ntotal} candidates")