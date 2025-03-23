import sys
import os

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'src'))

sys.path.append(src_path)

from resume_parser.parser import parse_resume

if __name__ == "__main__":
    # Replace with your actual file name
    path = r"data/sample_resumes/NEERAJ KUMAR LOKIREDDY resume DS.pdf"

    result = parse_resume(path)
    print("Email Found:", result["email"])
    print("Skills Found:", result["skills"])
    print("Education Found:", result["education"])
    print("Experience Found:", result["experience"])
    print("\nResume Text Preview:\n", result["raw_text"])
