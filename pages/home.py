import streamlit as st


def show():

    st.title("🎤 AI Mock Interview System")

    st.markdown(
        """
        ## 🚀 Welcome to AI Mock Interview System

        Practice technical interviews, analyze resumes, and evaluate candidates using Artificial Intelligence.

        ---
        """
    )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📄 Resume Analysis")

        st.write("""
        ✔ Resume Parsing

        ✔ Candidate Information Extraction

        ✔ Skill Detection

        ✔ ATS Resume Score

        ✔ Job Description Matching
        """)

        st.subheader("🎤 AI Mock Interview")

        st.write("""
        ✔ Role-Based Interview Questions

        ✔ AI Answer Evaluation

        ✔ Question-wise Scoring

        ✔ Overall Interview Score
        """)

    with col2:

        st.subheader("📊 Analytics")

        st.write("""
        ✔ Performance Dashboard

        ✔ Question-wise Charts

        ✔ Interview Summary
        """)

        st.subheader("🏆 Candidate Ranking")

        st.write("""
        ✔ Automatic Candidate Ranking

        ✔ Final Score Calculation

        ✔ Resume + Interview Evaluation
        """)

    st.divider()

    st.subheader("⚙️ Technologies Used")

    st.write("""
    • Python

    • Streamlit

    • Machine Learning

    • Natural Language Processing (NLP)

    • Scikit-learn

    • Pandas

    • NumPy

    • Matplotlib

    • Git & GitHub
    """)

    st.divider()

    st.success(
        "💡 AI Mock Interview System helps candidates prepare for technical interviews with AI-powered resume analysis, interview evaluation, analytics, and candidate ranking."
    )