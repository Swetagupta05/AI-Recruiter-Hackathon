def candidate_to_text(candidate):
    """
    Convert one candidate dictionary into one text document.
    """

    profile = candidate.get("profile", {})

    parts = []

    # Basic Profile
    parts.append(profile.get("headline", ""))
    parts.append(profile.get("summary", ""))

    parts.append(
        f"{profile.get('years_of_experience',0)} years experience"
    )

    parts.append(profile.get("current_title", ""))
    parts.append(profile.get("current_company", ""))

    # Skills
    skills = candidate.get("skills", [])

    if skills:

        skill_names = [
            skill["name"]
            for skill in skills
        ]

        parts.append(
            "Skills: " + ", ".join(skill_names)
        )

    # Career

    for job in candidate.get("career_history", []):

        parts.append(
            f"{job.get('title','')} at {job.get('company','')}"
        )

        parts.append(
            job.get("description", "")
        )

    # Education

    for edu in candidate.get("education", []):

        parts.append(
            f"{edu.get('degree','')} "
            f"{edu.get('field_of_study','')} "
            f"{edu.get('institution','')}"
        )

    return "\n".join(parts)