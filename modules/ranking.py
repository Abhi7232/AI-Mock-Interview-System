import streamlit as st


def show():

    st.title("🏆 AI Candidate Ranking System")

    st.write(
        "Rank candidates based on Resume ATS Score and Interview Performance."
    )

    # -----------------------------
    # Session State
    # -----------------------------

    if "candidates" not in st.session_state:
        st.session_state.candidates = []

    # -----------------------------
    # Auto Add Candidate
    # -----------------------------

    if (
        "candidate_name" in st.session_state
        and "email" in st.session_state
        and "ats_score" in st.session_state
        and "overall_score" in st.session_state
    ):

        auto_candidate = {

            "Name": st.session_state["candidate_name"],

            "Email": st.session_state["email"],

            "ATS Score": st.session_state["ats_score"],

            "Interview Score": st.session_state["overall_score"],

            "Final Score": round(
                (st.session_state["ats_score"] * 0.6)
                +
                (st.session_state["overall_score"] * 10 * 0.4),
                2
            )
        }

        exists = False

        for candidate in st.session_state.candidates:

            if candidate["Email"] == auto_candidate["Email"]:

                candidate.update(auto_candidate)

                exists = True

                break

        if not exists:

            st.session_state.candidates.append(
                auto_candidate
            )

    st.divider()

    # -----------------------------
    # Manual Add Candidate
    # -----------------------------

    st.subheader("➕ Add Candidate")

    name = st.text_input(
        "Candidate Name"
    )

    email = st.text_input(
        "Candidate Email"
    )

    ats_score = st.number_input(
        "ATS Resume Score",
        min_value=0,
        max_value=100,
        value=0
    )

    interview_score = st.number_input(
        "Interview Score",
        min_value=0.0,
        max_value=10.0,
        value=0.0
    )

    if st.button("Add Candidate"):

        final_score = round(
            (ats_score * 0.6)
            +
            (interview_score * 10 * 0.4),
            2
        )

        candidate = {

            "Name": name,

            "Email": email,

            "ATS Score": ats_score,

            "Interview Score": interview_score,

            "Final Score": final_score

        }

        exists = False

        for c in st.session_state.candidates:

            if c["Email"] == email:

                c.update(candidate)

                exists = True

                break

        if not exists:

            st.session_state.candidates.append(
                candidate
            )

        st.success(
            "✅ Candidate Added Successfully!"
        )

    st.divider()

    # -----------------------------
    # Candidate Ranking
    # -----------------------------

    st.subheader("📊 Candidate Ranking")

    if st.session_state.candidates:

        ranked = sorted(
            st.session_state.candidates,
            key=lambda x: x["Final Score"],
            reverse=True
        )

        for index, candidate in enumerate(ranked):

            if index == 0:

                st.success(
                    f"🥇 Rank {index+1} - {candidate['Name']} | Score: {candidate['Final Score']}"
                )

            elif index == 1:

                st.info(
                    f"🥈 Rank {index+1} - {candidate['Name']} | Score: {candidate['Final Score']}"
                )

            elif index == 2:

                st.warning(
                    f"🥉 Rank {index+1} - {candidate['Name']} | Score: {candidate['Final Score']}"
                )

            else:

                st.write(
                    f"Rank {index+1} - {candidate['Name']} | Score: {candidate['Final Score']}"
                )

        st.divider()

        st.subheader("📋 Ranking Table")

        st.dataframe(
            ranked,
            use_container_width=True
        )

    else:

        st.warning(
            "No candidates added yet."
        )