def extract_skills(text):

    skills_list = [
        "Python",
        "SQL",
        "C++",
        "Artificial Intelligence",
        "Machine Learning",
        "Deep Learning",
        "NLP",
        "Natural Language Processing",
        "Generative AI",
        "Data Science",
        "Pandas",
        "NumPy",
        "Matplotlib",
        "Scikit-learn",
        "TensorFlow",
        "PyTorch",
        "Streamlit",
        "Flask",
        "Django",
        "Git",
        "GitHub",
        "Power BI",
        "Excel",
        "XGBoost"
    ]

    detected_skills = []

    text = text.lower()

    for skill in skills_list:
        if skill.lower() in text:
            detected_skills.append(skill)

    return detected_skills