import re


AI_KEYWORDS = {
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


AI_TITLES = [
    "ai",
    "ml",
    "machine learning",
    "data scientist",
    "data engineer",
    "backend engineer",
    "ai engineer",
    "research engineer",
]


def extract_skills(candidate):
    skills = set()

    for skill in candidate.get("skills", []):
        skills.add(skill["name"].lower())

    return skills


def title_score(candidate):

    title = candidate["profile"]["current_title"].lower()

    score = 0

    for keyword in AI_TITLES:

        if keyword in title:
            score += 1

    return min(score / 3, 1.0)


def experience_score(candidate):

    years = candidate["profile"]["years_of_experience"]

    if 5 <= years <= 9:
        return 1.0

    if 3 <= years < 5:
        return 0.7

    if 9 < years <= 12:
        return 0.7

    return 0.3


def skills_score(candidate):

    skills = {
        skill["name"].lower()
        for skill in candidate.get("skills", [])
    }

    score = 0

    for keyword in AI_KEYWORDS:

        for skill in skills:

            if keyword in skill or skill in keyword:
                score += 1
                break

    return score / len(AI_KEYWORDS)


def redrob_score(candidate):

    rr = candidate["redrob_signals"]

    score = 0

    score += rr["profile_completeness_score"] / 100
    score += min(rr["github_activity_score"] / 100, 1)
    score += rr["interview_completion_rate"]
    score += rr["offer_acceptance_rate"]

    return score / 4


def final_score(candidate, semantic_score):

    semantic_weight = 0.40
    skill_weight = 0.25
    title_weight = 0.15
    experience_weight = 0.10
    redrob_weight = 0.10

    return (
        semantic_weight * semantic_score
        + skill_weight * skills_score(candidate)
        + title_weight * title_score(candidate)
        + experience_weight * experience_score(candidate)
        + redrob_weight * redrob_score(candidate)
    )