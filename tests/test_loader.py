from data_loader import load_candidates

candidates = load_candidates(limit=2)

print(f"Loaded {len(candidates)} candidates\n")

for candidate in candidates:
    print(candidate["candidate_id"])
    print(candidate["profile"]["headline"])
    print("-" * 50)