from ranker import rank_candidates

results = rank_candidates(limit=10)

print("\nTOP MATCHES\n")

for i, candidate in enumerate(results, start=1):

    print(
        f"{i}. {candidate['candidate_id']}"
    )

    print(
        candidate["headline"]
    )

    print(
        f"Similarity Score: {candidate['score']:.4f}"
    )

    print("-" * 50)
    