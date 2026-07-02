from data_loader import load_candidates
from job_processor import load_job_description
from search import search_candidates

from scorer import final_score
from reasoning import generate_reasoning

from exporter import export_submission


def main():

    print("=" * 60)
    print("AI RECRUITER")
    print("=" * 60)

    print("\nLoading candidates...")

    candidates = load_candidates()

    candidate_lookup = {
        c["candidate_id"]: c
        for c in candidates
    }

    print("Reading Job Description...")

    job = load_job_description()

    print("Searching Candidate Index...")

    search_results = search_candidates(
        job,
        top_k=500
    )

    ranked = []

    print("Applying Hybrid Scoring...")

    for item in search_results:

        candidate = candidate_lookup[item["candidate_id"]]

        score = final_score(
            candidate,
            item["semantic_score"]
        )
        score = round(score, 4)

        reasoning = generate_reasoning(
            candidate,
            score
        )

        ranked.append({

            "candidate_id": candidate["candidate_id"],

            "score": score,

            "reasoning": reasoning

        })

    ranked.sort(
        key=lambda x: (-round(x["score"], 4), x["candidate_id"])
    )

    export_submission(
        ranked,
        filename="output/submission.csv"
    )

    print("\nDone!")
    print(f"Generated {len(ranked)} ranked candidates.")


if __name__ == "__main__":
    main()