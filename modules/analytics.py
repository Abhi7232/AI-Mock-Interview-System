import streamlit as st


def show():

    st.title("📊 Analytics Dashboard")

    st.write("Interview Performance Summary")

    scores = st.session_state.get("analytics_scores", [])

    if not scores:
        st.warning("No interview data available.")
        return

    average_score = sum(scores) / len(scores)
    highest_score = max(scores)
    lowest_score = min(scores)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Average Score",
            f"{average_score:.1f}/10"
        )

    with col2:
        st.metric(
            "Highest Score",
            f"{highest_score}/10"
        )

    with col3:
        st.metric(
            "Lowest Score",
            f"{lowest_score}/10"
        )

    st.subheader("📈 Question-wise Scores")

    chart_data = {
        "Question": [
            f"Q{i+1}" for i in range(len(scores))
        ],
        "Score": scores
    }

    st.bar_chart(
        chart_data,
        x="Question",
        y="Score"
    )

    st.subheader("📋 Interview Summary")

    if average_score >= 8:
        st.success("Excellent Interview Performance ⭐⭐⭐⭐⭐")
    elif average_score >= 6:
        st.info("Good Interview Performance ⭐⭐⭐⭐")
    elif average_score >= 4:
        st.warning("Average Interview Performance ⭐⭐⭐")
    else:
        st.error("Needs Improvement ⭐⭐")