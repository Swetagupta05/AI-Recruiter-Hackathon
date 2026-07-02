import json
from pathlib import Path
from sentence_transformers import SentenceTransformer

# Load embedding model
print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
CANDIDATE_FILE = PROJECT_ROOT / "data" / "candidates.jsonl"

def candidate_to_text(candidate):
    profile = candidate["profile"]

    text = f"""
    {profile.get('headline','')}
    {profile.get('summary','')}
    Experience: {profile.get('years_of_experience','')} years

    Skills:
    """

    for skill in candidate.get("skills", []):
        text += skill["name"] + ", "

    for job in candidate.get("career_history", []):
        text += f"""
        {job.get('title','')}
        {job.get('description','')}
        """

    return text


# Read first candidate
with open(CANDIDATE_FILE, "r", encoding="utf-8") as f:
    candidate = json.loads(f.readline())

candidate_text = candidate_to_text(candidate)

print("\nGenerating embedding...")

embedding = model.encode(candidate_text)

print("\nEmbedding Dimension:", len(embedding))

print("\nFirst 20 Numbers:\n")

print(embedding[:20])