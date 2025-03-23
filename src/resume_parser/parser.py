import fitz  # PyMuPDF
import re

def extract_experience(text):
    """Extract likely job titles from the resume text"""
    job_titles = [
        "data scientist", "data analyst", "machine learning engineer",
        "research assistant", "software engineer", "intern", "developer",
        "consultant", "product manager"
    ]
    text = text.lower()
    found = [title.title() for title in job_titles if title in text]
    return list(set(found))

def extract_education(text):
    """Extracts education degrees from the resume text"""
    education_keywords = [
        "bachelor", "b.tech", "b.sc", 
        "master", "m.s", "m.sc", 
        "mba", "phd", "doctorate", "bachelors", "masters"
    ]
    text = text.lower()
    found = [keyword.title() for keyword in education_keywords if keyword in text]
    return list(set(found))  # remove duplicates

def load_skills(skill_file="src/resume_parser/skills.txt"):
    """Load predefined skills from a text file"""
    with open(skill_file, "r", encoding="utf-8") as file:
        skills = [line.strip().lower() for line in file if line.strip()]
    return skills

def extract_skills(text, skill_file="src/resume_parser/skills.txt"):
    """Extract matching skills from resume text"""
    text = text.lower()
    words = set(text.split())
    skills = load_skills(skill_file)
    matched = [skill for skill in skills if skill in text]
    return matched

def extract_text_from_pdf(file_path):
    """Extract full text from a PDF file using PyMuPDF"""
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_email(text):
    """Use regex to find email in the text"""
    match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    return match.group() if match else None

def parse_resume(file_path):
    text = extract_text_from_pdf(file_path)
    email = extract_email(text)
    skills = extract_skills(text)
    education = extract_education(text)
    experience = extract_experience(text)

    return {
        "email": email,
        "skills": skills,
        "education": education,
        "experience": experience,
        "raw_text": text[:500]
    }


