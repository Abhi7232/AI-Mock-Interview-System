def calculate_ats_score(detected_skills, total_skills=25):

    score = int((len(detected_skills) / total_skills) * 100)

    if score > 100:
        score = 100

    return score