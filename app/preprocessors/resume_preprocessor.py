from pydoc import text
import re


class ResumePreprocessor:
    """
    Handles resume text preprocessing.
    """

    def __init__(self):
        pass

    def preprocess(self, text):
        """
        Clean and normalize resume text while preserving
        the resume structure.
        """
        
        # Convert Windows line endings
        text = text.replace("\r\n", "\n")
        text = text.replace("\r", "\n")

        # Replace tabs
        text = text.replace("\t", " ")

        # Remove invisible Unicode characters
        text = text.replace("\u200b", "")
        text = text.replace("\ufeff", "")
        text = text.replace("\u00a0", " ")

        # Convert to lowercase
        text = text.lower()

        # Fix email formatting
        text = re.sub(r"\s*@\s*", "@", text)
        text = re.sub(r"\s*\.\s*", ".", text)

        # Remove unwanted symbols
        text = re.sub(r"[^\w\s@#+./,\-]", " ", text)

        # Remove extra spaces but preserve newlines
        text = re.sub(r"[ ]{2,}", " ", text)

        # Trim spaces around newlines
        text = re.sub(r" *\n *", "\n", text)

        # Remove excessive blank lines
        text = re.sub(r"\n{3,}", "\n\n", text)

        return text.strip()
    
    