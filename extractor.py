import pdfplumber
import re

def extract_text_from_pdf(pdf_file):
    text = ""

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def extract_email(text):
    pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
    emails = re.findall(pattern, text)

    if emails:
        return emails[0]

    return "Not Found"


def extract_phone(text):
    pattern = r'\+?\d[\d\s-]{8,}\d'
    phones = re.findall(pattern, text)

    if phones:
        return phones[0]

    return "Not Found"