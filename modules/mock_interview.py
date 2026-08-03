import streamlit as st
from utils.questions import QUESTIONS
from utils.evaluator import evaluate_answer


def show():

    st.title("🎤 AI Mock Interview")
    st.write("Practice your interview with AI-generated questions.")

    role = st.selectbox(
        "Select Job Role",
        [
            "Data Scientist",
            "Machine Learning Engineer",
            "AI Engineer",
            "Python Developer"
        ]
    )

    # -------------------------
    # Session State
    # -------------------------

    if "interview_started" not in st.session_state:
        st.session_state.interview_started = False

    if "question_index" not in st.session_state:
        st.session_state.question_index = 0

    if "answers" not in st.session_state:
        st.session_state.answers = {}

    if "interview_completed" not in st.session_state:
        st.session_state.interview_completed = False

    if "overall_score" not in st.session_state:
        st.session_state.overall_score = 0

    if "question_scores" not in st.session_state:
        st.session_state.question_scores = []

    if "interview_id" not in st.session_state:
        st.session_state.interview_id = 0

    # -------------------------
    # Start Interview
    # -------------------------

    if st.button("🚀 Start Interview"):

        st.session_state.interview_started = True
        st.session_state.interview_completed = False
        st.session_state.question_index = 0
        st.session_state.answers = {}
        st.session_state.question_scores = []
        st.session_state.overall_score = 0
        st.session_state.interview_id += 1

        st.rerun()
    # -------------------------
    # Interview Questions
    # -------------------------

    if (
        st.session_state.interview_started
        and not st.session_state.interview_completed
    ):

        questions = QUESTIONS[role]
        current = st.session_state.question_index

        st.progress((current + 1) / len(questions))

        st.subheader(
            f"Question {current + 1} of {len(questions)}"
        )

        st.write(questions[current])

        answer = st.text_area(
            "Your Answer",
            value=st.session_state.answers.get(current, ""),
            height=200,
            key=f"answer_{st.session_state.interview_id}_{current}"
        )

        st.session_state.answers[current] = answer

        col1, col2 = st.columns(2)

        with col1:

            if st.button("⬅ Previous"):

                if current > 0:
                    st.session_state.question_index -= 1
                    st.rerun()

        with col2:

            if current < len(questions) - 1:

                if st.button("Next ➡"):

                    st.session_state.question_index += 1
                    st.rerun()

            else:

                if st.button("✅ Finish Interview"):

                    st.session_state.interview_completed = True
                    st.rerun()

    # -------------------------
    # Final Evaluation
    # -------------------------

    if st.session_state.interview_completed:

        st.divider()
        st.header("📊 Final Interview Evaluation")

        if st.button("🤖 Evaluate Interview"):

            total_score = 0
            question_scores = []

            questions = QUESTIONS[role]

            for i, question in enumerate(questions):

                answer = st.session_state.answers.get(i, "")

                result = evaluate_answer(answer)

                question_scores.append(result["score"])

                total_score += result["score"]

            overall = round(total_score / len(questions), 1)

            st.session_state.question_scores = question_scores
            st.session_state.overall_score = overall

            # Analytics ke liye
            st.session_state["analytics_scores"] = question_scores

            st.metric(
                "Overall Score",
                f"{overall}/10"
            )

            st.subheader("📈 Question-wise Scores")

            for i, score in enumerate(question_scores):
                st.write(f"Question {i+1}: {score}/10")

            if overall >= 8:
                st.success("⭐⭐⭐⭐⭐ Excellent Performance")

            elif overall >= 6:
                st.info("⭐⭐⭐⭐ Good Performance")

            elif overall >= 4:
                st.warning("⭐⭐⭐ Average Performance")

            else:
                st.error("⭐⭐ Needs Improvement")

        if st.button("🔄 Restart Interview"):

            # Clear everything
            st.session_state.interview_started = False
            st.session_state.interview_completed = False
            st.session_state.question_index = 0
            st.session_state.answers = {}
            st.session_state.question_scores = []
            st.session_state.overall_score = 0

            # Remove all answer text boxes
            for key in list(st.session_state.keys()):
                if key.startswith("answer_"):
                    del st.session_state[key]

            st.session_state.interview_id += 1

            st.rerun()