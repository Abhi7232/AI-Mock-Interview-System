import smtplib
from email.message import EmailMessage
import streamlit as st
import os


def send_report_email(receiver_email, pdf_path):

    sender_email = st.secrets["EMAIL_ADDRESS"]
    sender_password = st.secrets["EMAIL_APP_PASSWORD"]

    msg = EmailMessage()

    msg["Subject"] = "🎤 AI Mock Interview Report"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    msg.set_content(
        f"""
Dear Candidate,

Thank you for completing the AI Mock Interview.

Please find your Interview Report attached with this email.

Best Regards,
AI Mock Interview System
"""
    )

    with open(pdf_path, "rb") as f:

        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="pdf",
            filename=os.path.basename(pdf_path)
        )

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:

        smtp.starttls()

        smtp.login(
            sender_email,
            sender_password
        )

        smtp.send_message(msg)