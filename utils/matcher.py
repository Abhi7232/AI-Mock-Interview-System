from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils.skill_matcher import extract_job_skills


def calculate_match_score(resume_text, job_description):

    # -----------------------------
    # Text Similarity (30%)
    # -----------------------------
    documents = [resume_text, job_description]

    tfidf = TfidfVectorizer()

    tfidf_matrix = tfidf.fit_transform(documents)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )[0][0]

    text_score = similarity * 100

    # -----------------------------
    # Skill Match (70%)
    # -----------------------------
    job_skills = extract_job_skills(job_description)

    resume_lower = resume_text.lower()

    matched = 0

    for skill in job_skills:

        if skill.lower() in resume_lower:
            matched += 1

    if len(job_skills) > 0:
        skill_score = (matched / len(job_skills)) * 100
    else:
        skill_score = 0

    # -----------------------------
    # Hybrid Score
    # -----------------------------
    final_score = round(
        (skill_score * 0.7) +
        (text_score * 0.3),
        2
    )

    return final_score