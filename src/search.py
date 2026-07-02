import json
import faiss
import numpy as np

from config import (
    FAISS_INDEX_FILE,
    IDS_FILE,
)

from embedding_model import create_embedding


import json
import faiss
import numpy as np

from config import (
    FAISS_INDEX_FILE,
    IDS_FILE,
)

from embedding_model import create_embedding


def search_candidates(job_text, top_k=500):

    index = faiss.read_index(str(FAISS_INDEX_FILE))

    with open(IDS_FILE, "r") as f:
        ids = json.load(f)

    query = create_embedding(job_text)

    query = np.array([query]).astype("float32")

    faiss.normalize_L2(query)

    scores, indices = index.search(query, top_k)

    results = []

    for score, idx in zip(scores[0], indices[0]):

        results.append({
            "candidate_id": ids[idx],
            "semantic_score": float(score)
        })

    return results