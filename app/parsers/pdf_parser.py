import fitz
import re

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from all pages of a PDF file.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: Complete extracted text.
    """

    text = ""

    # Open the PDF
    document = fitz.open(pdf_path)

    # Loop through all pages
    for page in document:
        text += page.get_text()

    # Close the PDF
    document.close()

    return text

    
def clean_resume_text(text):
    """
    Cleans the extracted resume text.

    Args:
        text (str): Raw extracted text.

    Returns:
        str: Cleaned text.
    """

    # Replace tabs with spaces
    text = text.replace("\t", " ")

    # Remove extra spaces
    text = re.sub(r" +", " ", text)

    # Remove multiple blank lines
    text = re.sub(r"\n+", "\n", text)

    # Remove leading and trailing spaces
    text = text.strip()
    
    # Remove zero-width spaces and other invisible Unicode characters
    text = text.replace("\u200b", "")
    text = text.replace("\u200c", "")
    text = text.replace("\u200d", "")
    text = text.replace("\ufeff", "")

    return text
