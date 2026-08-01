import re


def extract_job_skills(job_description):

    skill_list = [

        # Programming
        "Python",
        "SQL",
        "C++",

        # AI / ML
        "Artificial Intelligence",
        "Machine Learning",
        "Deep Learning",
        "Data Science",
        "Generative AI",
        "Natural Language Processing",
        "NLP",
        "Large Language Models",
        "LLM",

        # Libraries
        "Pandas",
        "NumPy",
        "Matplotlib",
        "Scikit-learn",
        "TensorFlow",
        "PyTorch",
        "XGBoost",

        # Deployment
        "Streamlit",
        "Flask",
        "Git",
        "GitHub",

        # Data Skills
        "Statistics",
        "Data Analysis",
        "Data Visualization",
        "Feature Engineering",
        "Model Deployment",

        # Soft Skills
        "Problem Solving",
        "Communication Skills",
        "Analytical Thinking",
        "Team Collaboration"
    ]

    found_skills = []

    text = job_description.lower()

    for skill in skill_list:

        if re.search(
            r"\b" + re.escape(skill.lower()) + r"\b",
            text
        ):
            found_skills.append(skill)

    return list(dict.fromkeys(found_skills))


def compare_skills(resume_skills, job_skills):

    matched = []
    missing = []

    # Case-insensitive comparison
    resume_lower = [skill.lower() for skill in resume_skills]

    for skill in job_skills:

        if skill.lower() in resume_lower:
            matched.append(skill)
        else:
            missing.append(skill)

    return matched, missing