from job_processor import load_job_description
from search import search_candidates

job = load_job_description()

results = search_candidates(job, top_k=500)

print("\nTOP 10 CANDIDATES\n")

for i, r in enumerate(results, start=1):
    print(f"{i}. {r['candidate_id']}  Score: {r['score']:.4f}")