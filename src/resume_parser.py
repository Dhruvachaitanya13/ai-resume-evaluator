import PyPDF2
import spacy

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Predefined list of skills
SKILL_SET = {"python", "machine learning", "data science", "flask", "django", "sql", "pandas", "tensorflow", "keras"}

def extract_text(file):
    """Extracts text from a PDF resume."""
    pdf_reader = PyPDF2.PdfReader(file)
    text = "".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
    return text

def extract_skills(text):
    """Extracts relevant skills from resume text using NLP."""
    doc = nlp(text.lower())  # Convert text to lowercase
    skills_found = {token.text for token in doc if token.text in SKILL_SET}
    return list(skills_found)

