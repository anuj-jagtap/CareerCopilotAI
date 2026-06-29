class CandidateProfile:
    """
    Central data model for CareerCopilot AI.
    Every agent reads from and updates this profile.
    """

    def __init__(self):

        self.personal_information = {
            "name": "",
            "email": "",
            "phone": "",
            "linkedin": "",
            "github": ""
        }

        self.skills = []

        self.education = []

        self.experience = []

        self.projects = []

        self.certifications = []

        self.job_preferences = {}

        self.profile_strength = {}

    def add_skills(self, skills):
        """Update candidate skills."""
        self.skills = skills

    def get_profile(self):
        """Return complete candidate profile."""

        return {
            "personal_information": self.personal_information,
            "skills": self.skills,
            "education": self.education,
            "experience": self.experience,
            "projects": self.projects,
            "certifications": self.certifications,
            "job_preferences": self.job_preferences,
            "profile_strength": self.profile_strength
        }
        
    
    def update_personal_information(
    self,
    name,
    email,
    phone,
    linkedin,
    github
    ):
        self.personal_information = {
            "name": name,
            "email": email,
            "phone": phone,
            "linkedin": linkedin,
            "github": github
            }