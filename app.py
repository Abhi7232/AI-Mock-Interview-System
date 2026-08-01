import streamlit as st
from pages import home, resume_analysis, mock_interview, analytics, reports, ranking

st.set_page_config(
    page_title="AI Mock Interview System",
    page_icon="🎤",
    layout="wide"
)

st.sidebar.title("🎯 Navigation")

page = st.sidebar.radio(
    "Select a Module",
    [
        "🏠 Home",
        "📄 Resume Analysis",
        "🎤 Mock Interview",
        "📊 Dashboard",
        "📑 Reports",
        "🏆 Candidate Ranking",
        "ℹ️ About"
    ]
)

if page == "🏠 Home":
    home.show()

elif page == "📄 Resume Analysis":
    resume_analysis.show()

elif page == "🎤 Mock Interview":
    mock_interview.show()

elif page == "📊 Dashboard":
    analytics.show()

elif page == "📑 Reports":
    reports.show()
    
elif page == "🏆 Candidate Ranking":
    ranking.show()

elif page == "ℹ️ About":
    st.title("ℹ️ About")
    st.write("AI Mock Interview System - Version 1.0")