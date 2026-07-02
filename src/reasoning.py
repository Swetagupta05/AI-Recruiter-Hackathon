AI_SKILLS = {
    "python",
    "machine learning",
    "deep learning",
    "llm",
    "llms",
    "langchain",
    "rag",
    "embeddings",
    "vector search",
    "pinecone",
    "milvus",
    "faiss",
    "transformers",
    "huggingface",
    "bert",
    "pytorch",
    "tensorflow",
    "mlflow",
    "airflow",
    "spark",
    "fine-tuning",
    "prompt engineering",
}


def generate_reasoning(candidate, final_score):
    """
    Generate recruiter-style reasoning for why this candidate
    was recommended.
    """

    profile = candidate["profile"]
    signals = candidate["redrob_signals"]

    candidate_skills = {
        s["name"].lower()
        for s in candidate.get("skills", [])
    }

    matched = AI_SKILLS.intersection(candidate_skills)

    reasoning = (
        f"{profile['current_title']} with "
        f"{profile['years_of_experience']} yrs experience; "
        f"{len(matched)} AI-related skills; "
        f"profile completeness "
        f"{signals['profile_completeness_score']:.0f}%; "
        f"GitHub activity "
        f"{signals['github_activity_score']:.1f}; "
        f"Final score {final_score:.3f}"
    )

    return reasoning