import fitz  # PyMuPDF


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


# -------------------------
# Testing
# -------------------------
#if __name__ == "__main__":

#    pdf_path = "resumes/sample_resume.pdf"

#    extracted_text = extract_text_from_pdf(pdf_path)

#    print("\n===== EXTRACTED RESUME TEXT =====\n")
#    print(extracted_text)
    
    
import re
import fitz

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

    return text

#-------------------------
# Testing
#------------------------

if __name__ == "__main__":

    pdf_path = "resumes/sample_resume.pdf"

    # Step 1: Extract text
    extracted_text = extract_text_from_pdf(pdf_path)

    # Step 2: Clean text
    cleaned_text = clean_resume_text(extracted_text)

    print("\n===== CLEANED RESUME TEXT =====\n")
    print(cleaned_text)