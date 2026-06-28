import re

import pandas as pd


class SkillIntelligenceAgent:

    def __init__(self, knowledge_base_path):
        """
        Initialize the Skill Intelligence Agent.

        Args:
            knowledge_base_path (str): Path to skills knowledge base.
        """

        self.knowledge_base_path = knowledge_base_path
        self.skills_df = None
        self.skills_list = []

    def load_knowledge_base(self):
        """
        Load the skills knowledge base from Excel.
        """
        
        self.skills_df = pd.read_excel(self.knowledge_base_path)
        self.skills_list = (
            self.skills_df["skill"]
            .dropna()
            .astype(str)
            .str.strip()
            .tolist()
            )
        print(f"Knowledge Base Loaded Successfully.")
        print(f"Total Skills : {len(self.skills_list)}")


    def extract_explicit_skills(self, resume_text):
        """
        Extract explicitly mentioned skills using exact word matching.
        """

        matched_skills = []

        resume_text = resume_text.lower()

        for skill in self.skills_list:
            pattern = r"\b" + re.escape(skill.lower()) + r"\b"
            
            if re.search(pattern, resume_text):
                matched_skills.append(skill)

        matched_skills = sorted(set(matched_skills))

        return matched_skills
    
    
    
    
    def infer_skills(self):
        pass

    def build_skill_profile(self, matched_skills):
        """
        Build a structured skill profile.

        Args:
            matched_skills (list): List of extracted skills.

        Returns:
            list: Structured skill profile.
        """

        skill_profile = []

        for skill in matched_skills:
            row = self.skills_df[
                self.skills_df["skill"].str.lower() == skill.lower()
                ]
            
            if not row.empty:
                skill_profile.append({
                    "skill": skill,
                    "category": row.iloc[0]["category"],
                    "confidence": 1.0,
                    "source": "Explicit"
                    })

        return skill_profile


    
if __name__ == "__main__":

    agent = SkillIntelligenceAgent(
        "data/knowledge_base/skills_knowledge_base.xlsx"
    )

    agent.load_knowledge_base()

    print("\nFirst 10 Skills:\n")
    print(agent.skills_list[:10])

    sample_resume = """
    Python
    SQL
    Machine Learning
    Pandas
    NumPy
    Power BI
    """

    skills = agent.extract_explicit_skills(sample_resume)

    print("\nExtracted Skills:\n")
    print(skills)

    profile = agent.build_skill_profile(skills)

    print("\nSkill Profile:\n")

    for item in profile:
        print(item)