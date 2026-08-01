import streamlit as st
from utils.resume_parser import (
    extract_text_from_pdf,
    extract_name,
    extract_email,
    extract_phone
)
from utils.suggestions import generate_suggestions
from utils.skill_extractor import extract_skills
from utils.scoring import calculate_ats_score
from utils.matcher import calculate_match_score
from utils.skill_matcher import (
    extract_job_skills,
    compare_skills
)


def show():

    st.title("📄 Resume Analysis")

    st.write("Upload your resume in PDF format.")

    uploaded_file = st.file_uploader(
        "Choose a Resume (PDF)",
        type=["pdf"]
    )

    if uploaded_file is not None:

        st.success("✅ Resume uploaded successfully!")
        st.write("Filename:", uploaded_file.name)

        resume_text = extract_text_from_pdf(uploaded_file)

        name = extract_name(resume_text)
        email = extract_email(resume_text)
        phone = extract_phone(resume_text)

        skills = extract_skills(resume_text)
        ats_score = calculate_ats_score(skills)

        # Save for Reports Page
        st.session_state["candidate_name"] = name
        st.session_state["email"] = email
        st.session_state["skills"] = skills
        st.session_state["ats_score"] = ats_score

        st.subheader("👤 Candidate Information")

        col1, col2 = st.columns(2)

        with col1:
            st.write("**Name:**", name)
            st.write("**Email:**", email)

        with col2:
            st.write("**Phone:**", phone)

        st.subheader("🛠️ Detected Skills")

        if skills:
            for skill in skills:
                st.success(skill)
        else:
            st.warning("No skills detected")

        st.subheader("📊 ATS Resume Score")

        st.progress(ats_score / 100)

        st.metric(
            "ATS Score",
            f"{ats_score}/100"
        )

        if ats_score >= 70:
            st.success("Excellent Resume Match")
        elif ats_score >= 40:
            st.warning("Average Resume Match")
        else:
            st.error("Resume Needs Improvement")

        st.subheader("💼 Job Description")
        job_description = st.text_area(
            "Paste Job Description Here",
            height=200
        )

        if st.button("🔍 Analyze Resume Match"):

            if job_description.strip():

                match_score = calculate_match_score(
                    resume_text,
                    job_description
                )

                st.session_state["match_score"] = match_score

                job_skills = extract_job_skills(
                    job_description
                )

                matched_skills, missing_skills = compare_skills(
                    skills,
                    job_skills
                )

                suggestions = generate_suggestions(
                    ats_score,
                    missing_skills
                )

                st.subheader("🎯 Resume Match Score")

                st.progress(match_score / 100)

                st.metric(
                    "Match Percentage",
                    f"{match_score}%"
                )

                if match_score >= 80:
                    st.success("Excellent Match")
                elif match_score >= 60:
                    st.warning("Good Match")
                else:
                    st.error("Low Match")

                st.subheader("✅ Matched Skills")

                if matched_skills:
                    for skill in matched_skills:
                        st.success(skill)
                else:
                    st.warning("No matched skills found.")

                st.subheader("❌ Missing Skills")

                if missing_skills:
                    for skill in missing_skills:
                        st.error(skill)
                else:
                    st.success("No missing skills. Great!")

                st.subheader("💡 AI Resume Suggestions")

                for suggestion in suggestions:
                    st.info(suggestion)

            else:
                st.warning("Please paste a Job Description first.")

        st.subheader("📄 Extracted Resume Text")

        st.text_area(
            "Resume Content",
            resume_text,
            height=300
        )