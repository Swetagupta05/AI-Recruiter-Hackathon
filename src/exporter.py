import pandas as pd

def export_submission(results, filename="submission.csv"):

    # Keep only top 100
    results = results[:100]

    rows = []

    for rank, candidate in enumerate(results, start=1):

        rows.append({
            "candidate_id": candidate["candidate_id"],
            "rank": rank,
            "score": round(candidate["score"], 4),
            "reasoning": candidate["reasoning"]
        })

    df = pd.DataFrame(rows)

    df.to_csv(filename, index=False)

    print(f"Saved {filename}")