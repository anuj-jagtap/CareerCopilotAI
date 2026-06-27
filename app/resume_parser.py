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
if __name__ == "__main__":

    pdf_path = "resumes/sample_resume.pdf"

    extracted_text = extract_text_from_pdf(pdf_path)

    print("\n===== EXTRACTED RESUME TEXT =====\n")
    print(extracted_text)