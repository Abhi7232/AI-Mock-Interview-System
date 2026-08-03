import streamlit as st
from modules import home, resume_analysis, mock_interview, analytics, reports, ranking

st.set_page_config(
    page_title="AI Mock Interview System",
    page_icon="🎤",
    layout="wide"
)

# ==========================
# Pages List
# ==========================
pages = [
    "🏠 Home",
    "📄 Resume Analysis",
    "🎤 Mock Interview",
    "📊 Dashboard",
    "📑 Reports",
    "🏆 Candidate Ranking",
    "ℹ️ About"
]

# ==========================
# Session State
# ==========================
if "page" not in st.session_state:
    st.session_state.page = pages[0]

# ==========================
# Sidebar Navigation
# ==========================
st.sidebar.title("🎯 Navigation")

page = st.sidebar.radio(
    "Select a Module",
    pages,
    index=pages.index(st.session_state.page)
)

st.session_state.page = page

# ==========================
# Navigation Buttons
# ==========================
def navigation_buttons(current_page):
    current_index = pages.index(current_page)

    st.markdown("---")

    col1, col2 = st.columns([1, 1])

    with col1:
        if current_index > 0:
            if st.button("⬅️ Previous"):
                st.session_state.page = pages[current_index - 1]
                st.rerun()

    with col2:
        if current_index < len(pages) - 1:
            if st.button("Next ➡️"):
                st.session_state.page = pages[current_index + 1]
                st.rerun()

# ==========================
# Page Routing
# ==========================
if page == "🏠 Home":
    home.show()
    navigation_buttons(page)

elif page == "📄 Resume Analysis":
    resume_analysis.show()
    navigation_buttons(page)

elif page == "🎤 Mock Interview":
    mock_interview.show()
    navigation_buttons(page)

elif page == "📊 Dashboard":
    analytics.show()
    navigation_buttons(page)

elif page == "📑 Reports":
    reports.show()
    navigation_buttons(page)

elif page == "🏆 Candidate Ranking":
    ranking.show()
    navigation_buttons(page)

elif page == "ℹ️ About":
    st.title("ℹ️ About")
    st.write("AI Mock Interview System - Version 1.0")
    navigation_buttons(page)