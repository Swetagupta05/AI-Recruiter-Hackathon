import json
from pathlib import Path

# Locate the data folder
project_root = Path(__file__).resolve().parent.parent
candidate_file = project_root / "data" / "candidates.jsonl"

# Read only the first candidate
with open(candidate_file, "r", encoding="utf-8") as file:
    first_line = file.readline()
    candidate = json.loads(first_line)

print("=" * 60)
print("FIRST CANDIDATE")
print("=" * 60)

print(json.dumps(candidate, indent=4))