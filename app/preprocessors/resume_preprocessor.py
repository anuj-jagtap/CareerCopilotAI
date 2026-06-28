import re


class ResumePreprocessor:
    """
    Handles resume text preprocessing.
    """

    def __init__(self):
        pass

    def preprocess(self, text):
        """
        Clean and normalize resume text.
        """

        # Lowercase
        text = text.lower()

        # Remove extra spaces
        text = re.sub(r"\s+", " ", text)

        # Remove unwanted symbols
        text = re.sub(r"[^\w\s#+./-]", " ", text)

        # Remove multiple spaces again
        text = re.sub(r"\s+", " ", text)

        return text.strip()
    
    
if __name__ == "__main__":

    sample = """
    Python, SQL,   Machine Learning
    Built dashboards in Power BI.
    """

    preprocessor = ResumePreprocessor()

    print(preprocessor.preprocess(sample))