import streamlit as st
from utils.pdf_report import generate_pdf
from utils.email_utils import send_report_email
import os


def show():

    st.title("📑 Interview & Resume Reports")

    st.write(
        "View your latest Resume Analysis and Mock Interview Report."
    )

    st.divider()

    # -------------------------
    # Resume Report
    # -------------------------

    st.subheader("📄 Resume Report")

    if "candidate_name" in st.session_state:

        candidate_name = st.session_state.get(
            "candidate_name",
            "N/A"
        )

        email = st.session_state.get(
            "email",
            "N/A"
        )

        ats_score = st.session_state.get(
            "ats_score",
            0
        )

        st.write("👤 Candidate Name:", candidate_name)
        st.write("📧 Email:", email)
        st.write("📊 ATS Score:", f"{ats_score}/100")

    else:

        st.warning(
            "No Resume Analysis data available."
        )

    st.divider()

    # -------------------------
    # Interview Report
    # -------------------------

    st.subheader("🎤 Interview Report")

    if (
        "overall_score" in st.session_state
        and st.session_state.overall_score > 0
    ):

        overall_score = st.session_state.get(
            "overall_score",
            0
        )

        question_scores = st.session_state.get(
            "question_scores",
            []
        )

        st.write(
            "🎯 Overall Interview Score:",
            f"{overall_score}/10"
        )

        st.subheader(
            "📈 Question Wise Performance"
        )

        for i, score in enumerate(question_scores):

            st.write(
                f"Question {i+1}: {score}/10"
            )
        # -------------------------
        # Recommendation
        # -------------------------

        if overall_score >= 8:

            recommendation = (
                "Recommended for Technical Interview Round"
            )

            st.success(
                "⭐⭐⭐⭐⭐ Excellent Performance"
            )

        elif overall_score >= 6:

            recommendation = (
                "Good candidate, continue improving skills"
            )

            st.info(
                "⭐⭐⭐⭐ Good Performance"
            )

        elif overall_score >= 4:

            recommendation = (
                "Needs more practice"
            )

            st.warning(
                "⭐⭐⭐ Average Performance"
            )

        else:

            recommendation = (
                "More preparation required"
            )

            st.error(
                "⭐⭐ Needs Improvement"
            )

        st.divider()

        st.subheader("📧 Download & Email Report")

        filename = "AI_Mock_Interview_Report.pdf"

        if st.button("📧 Download & Email Report"):

            generate_pdf(
                filename,
                st.session_state.get(
                    "candidate_name",
                    "N/A"
                ),
                st.session_state.get(
                    "email",
                    "N/A"
                ),
                st.session_state.get(
                    "ats_score",
                    0
                ),
                overall_score,
                question_scores,
                recommendation
            )

            try:

                receiver_email = st.session_state.get(
                    "email",
                    ""
                )

                if receiver_email:

                    send_report_email(
                        receiver_email,
                        filename
                    )

                    st.success(
                        f"✅ Report emailed successfully to {receiver_email}"
                    )

                else:

                    st.warning(
                        "⚠️ Candidate email not found."
                    )

            except Exception as e:

                st.error(
                    f"❌ Email sending failed: {e}"
                )
            # PDF Download

            with open(
                filename,
                "rb"
            ) as file:

                st.download_button(

                    label="⬇️ Download PDF Report",

                    data=file,

                    file_name=filename,

                    mime="application/pdf",

                    use_container_width=True

                )

    else:

        st.warning(
            "No Interview data available."
        )