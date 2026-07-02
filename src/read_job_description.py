from pathlib import Path
from docx import Document

# Project root
project_root = Path(__file__).resolve().parent.parent

# Path to job description
job_file = project_root / "data" / "job_description.docx"

doc = Document(job_file)

print("=" * 60)
print("JOB DESCRIPTION")
print("=" * 60)

for para in doc.paragraphs:
    if para.text.strip():
        print(para.text)