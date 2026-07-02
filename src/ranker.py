from sklearn.metrics.pairwise import cosine_similarity
from data_loader import load_candidates
from preprocess import candidate_to_text
from embedding_model import create_embedding
from job_processor import create_job_embedding


def rank_candidates(limit=10):
    """
    Rank candidates using semantic similarity.
    """

    # Job embedding
    job_text, job_embedding = create_job_embedding()

    candidates = load_candidates(limit=limit)

    ranked = []

    for candidate in candidates:

        text = candidate_to_text(candidate)

        embedding = create_embedding(text)

        score = cosine_similarity(
            [job_embedding],
            [embedding]
        )[0][0]

        ranked.append({
            "candidate_id": candidate["candidate_id"],
            "headline": candidate["profile"]["headline"],
            "score": float(score)
        })

    ranked.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return ranked