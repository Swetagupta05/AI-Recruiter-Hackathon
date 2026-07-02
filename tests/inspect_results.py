from data_loader import load_candidates
from search import search_candidates
from job_processor import load_job_description

# Load everything
job = load_job_description()
results = search_candidates(job, top_k=500)

# Load all candidates once
candidates = load_candidates()

candidate_lookup = {
    c["candidate_id"]: c
    for c in candidates
}

print("=" * 80)
print("TOP 10 RESULTS")
print("=" * 80)

for i, result in enumerate(results, start=1):

    candidate = candidate_lookup[result["candidate_id"]]

    profile = candidate["profile"]

    print(f"\nRank {i}")
    print("=" * 40)

    print("ID:", result["candidate_id"])
    print("Score:", round(result["score"], 4))
    print("Headline:", profile["headline"])
    print("Experience:", profile["years_of_experience"])
    print("Current Title:", profile["current_title"])
    print("Company:", profile["current_company"])

    skills = [
        s["name"]
        for s in candidate["skills"][:10]
    ]

    print("Skills:", ", ".join(skills))