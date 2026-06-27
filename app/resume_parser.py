import re
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


def extract_email(text):
    """
    Extract email address from resume text.

    Args:
        text (str): Cleaned resume text.

    Returns:
        str: Email address if found, else None.
    """

    email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    match = re.search(email_pattern, text)

    if match:
        return match.group()

    return None


def extract_phone(text):
    """
    Extract phone number from resume text.

    Args:
        text (str): Cleaned resume text.

    Returns:
        str: Phone number if found, else None.
    """

    phone_pattern = r"(?:\+91[\s-]?)?[6-9]\d{9}"

    match = re.search(phone_pattern, text)

    if match:
        return match.group()

    return None


def extract_linkedin(text):
    """
    Extract LinkedIn profile URL from resume text.

    Args:
        text (str): Cleaned resume text.

    Returns:
        str: LinkedIn URL if found, else None.
    """

    linkedin_pattern = r"(?:https?://)?(?:www\.)?linkedin\.com/in/[A-Za-z0-9_-]+"

    match = re.search(linkedin_pattern, text, re.IGNORECASE)

    if match:
        return match.group()

    return None


def extract_github(text):
    """
    Extract GitHub profile URL from resume text.

    Args:
        text (str): Cleaned resume text.

    Returns:
        str: GitHub URL if found, else None.
    """

    github_pattern = r"(?:https?://)?(?:www\.)?github\.com/[A-Za-z0-9_-]+"

    match = re.search(github_pattern, text, re.IGNORECASE)

    if match:
        return match.group()

    return None


# -------------------------
# Testing
# -------------------------

if __name__ == "__main__":

    pdf_path = "resumes/sample_resume.pdf"

    # Step 1: Extract text from PDF
    extracted_text = extract_text_from_pdf(pdf_path)

    # Step 2: Clean extracted text
    cleaned_text = clean_resume_text(extracted_text)

    print("\n===== CLEANED TEXT =====\n")
    print(cleaned_text)
 
    # Step 3: Extract candidate information
    candidate = {
        "name": "",
        "email": extract_email(cleaned_text),
        "phone": extract_phone(cleaned_text),
        "linkedin": extract_linkedin(cleaned_text),
        "github": extract_github(cleaned_text),
        "skills": [],
        "education": [],
        "projects": []
    }

    print("\n========== CANDIDATE PROFILE ==========\n")

    for key, value in candidate.items():
        print(f"{key.capitalize():12}: {value}")