def generate_suggestions(ats_score, missing_skills):

    suggestions = []

    if ats_score < 90:
        suggestions.append(
            "Improve your ATS score by adding more relevant technical skills."
        )

    for skill in missing_skills:
        suggestions.append(
            f"Consider learning and adding {skill} to your resume."
        )

    if not suggestions:
        suggestions.append(
            "Excellent! Your resume is well optimized."
        )

    return suggestions