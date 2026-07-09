import re

def extract_name(text):
    """
    Extract candidate name from resume.

    Assumption:
    Name is usually the first meaningful line.
    """

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if len(line) == 0:
            continue

        # Skip lines containing common contact info
        if "@" in line:
            continue

        if "linkedin" in line.lower():
            continue

        if "github" in line.lower():
            continue

        if re.search(r"\d", line):
            continue

        return line

    return ""

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

if __name__ == "__main__":

    sample = """
    ANUJ JAGTAP

    Data Scientist

    jagtapanuj3@gmail.com

    +91 9309927273
    """

    print(extract_name(sample))