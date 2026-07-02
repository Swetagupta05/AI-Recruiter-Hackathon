from docx import Document
from config import JOB_DESCRIPTION_FILE
from embedding_model import create_embedding


def load_job_description():
    """
    Read the job description from the DOCX file.
    Returns the complete text.
    """
    doc = Document(JOB_DESCRIPTION_FILE)

    paragraphs = []

    for para in doc.paragraphs:
        text = para.text.strip()
        if text:
            paragraphs.append(text)

    return "\n".join(paragraphs)


def create_job_embedding():
    """
    Generate an embedding for the job description.
    """
    job_text = load_job_description()
    embedding = create_embedding(job_text)

    return job_text, embedding