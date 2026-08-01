import pdfplumber
import re

def extract_text_from_pdf(uploaded_file):
    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def extract_email(text):
    match = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    if match:
        return match.group()
    return "Not Found"


def extract_phone(text):
    match = re.search(r"(\+91[\s-]?)?[6-9]\d{9}", text)
    if match:
        return match.group()
    return "Not Found"


def extract_name(text):
    lines = text.split("\n")

    for line in lines:
        line = line.strip()

        if len(line) > 2 and len(line.split()) <= 4:
            return line

    return "Not Found"