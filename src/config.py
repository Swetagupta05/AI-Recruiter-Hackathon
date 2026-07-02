from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Data directory
DATA_DIR = PROJECT_ROOT / "data"

# Output directory
OUTPUT_DIR = PROJECT_ROOT / "output"

# Models directory
MODEL_DIR = PROJECT_ROOT / "models"

# Dataset files
CANDIDATES_FILE = DATA_DIR / "candidates.jsonl"
SAMPLE_CANDIDATES_FILE = DATA_DIR / "sample_candidates.json"
JOB_DESCRIPTION_FILE = DATA_DIR / "job_description.docx"

# Embedding model
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

# Cache files
EMBEDDINGS_FILE = MODEL_DIR / "candidate_embeddings.npy"
IDS_FILE = MODEL_DIR / "candidate_ids.json"
FAISS_INDEX_FILE = MODEL_DIR / "candidate_index.faiss"

# Batch size for embedding generation
BATCH_SIZE = 64