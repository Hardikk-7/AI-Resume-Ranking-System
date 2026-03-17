import re
import pdfplumber
from docx import Document

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


def extract_text_from_docx(file):
    doc = Document(file)
    return "\n".join([para.text for para in doc.paragraphs])


def extract_email(text):
    match = re.search(r'\S+@\S+', text)
    return match.group() if match else ""


def extract_phone(text):
    match = re.search(r'\+?\d[\d -]{8,12}\d', text)
    return match.group() if match else ""


def extract_name(text):
    lines = text.split("\n")
    for line in lines[:5]:
        if len(line.split()) <= 4 and line.strip():
            return line.strip()
    return "Unknown"


def extract_experience(text):
    text = text.lower()
    matches = re.findall(r'(\d+)\+?\s*(years|yrs)', text)
    if matches:
        return max([int(m[0]) for m in matches])
    return 0


def extract_education(text):
    text = text.lower()
    if "b.tech" in text or "bachelor" in text:
        return "Bachelor"
    elif "master" in text or "m.tech" in text:
        return "Master"
    return "Unknown"


def extract_location(text):
    lines = text.split("\n")
    for line in lines:
        if any(city in line.lower() for city in ["delhi", "mumbai", "bangalore", "hyderabad"]):
            return line.strip()
    return "Unknown"