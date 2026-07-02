import json
from config import CANDIDATES_FILE


def load_candidates(limit=None):
    """
    Load candidate profiles from candidates.jsonl.

    Args:
        limit (int, optional): Number of candidates to load.
                               If None, loads all candidates.

    Returns:
        List of candidate dictionaries.
    """

    candidates = []

    with open(CANDIDATES_FILE, "r", encoding="utf-8") as file:

        for index, line in enumerate(file):

            candidates.append(json.loads(line))

            if limit and index + 1 >= limit:
                break

    return candidates