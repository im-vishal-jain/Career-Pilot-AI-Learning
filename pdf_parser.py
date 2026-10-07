"""
PDF and DOCX parser — extracts raw text from uploaded resume files
"""

import io
import re


def extract_text_from_pdf(file_bytes: bytes) -> str:
    """Extract text from a PDF file using pdfplumber."""
    try:
        import pdfplumber
        with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
            pages = [p.extract_text() or "" for p in pdf.pages]
        return "\n".join(pages).strip()
    except Exception as e:
        return f"[PDF parse error: {e}]"


def extract_text_from_docx(file_bytes: bytes) -> str:
    """Extract text from a DOCX file using python-docx."""
    try:
        from docx import Document
        doc = Document(io.BytesIO(file_bytes))
        paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
        return "\n".join(paragraphs).strip()
    except Exception as e:
        return f"[DOCX parse error: {e}]"


def parse_uploaded_file(uploaded_file) -> str:
    """
    Accept a Streamlit UploadedFile and return extracted text.
    Supports .pdf and .docx.
    """
    if uploaded_file is None:
        return ""
    name = uploaded_file.name.lower()
    content = uploaded_file.read()
    if name.endswith(".pdf"):
        return extract_text_from_pdf(content)
    elif name.endswith(".docx"):
        return extract_text_from_docx(content)
    else:
        try:
            return content.decode("utf-8", errors="ignore")
        except Exception:
            return "[Unsupported file type]"


def clean_text(text: str) -> str:
    """Remove excessive whitespace and non-printable characters."""
    text = re.sub(r"\s{3,}", "\n\n", text)
    text = re.sub(r"[^\x20-\x7E\n]", " ", text)
    return text.strip()
