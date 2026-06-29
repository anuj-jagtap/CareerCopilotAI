from app.parsers.pdf_parser import extract_text_from_pdf
from app.preprocessors.resume_preprocessor import ResumePreprocessor
from app.agents.skill_intelligence_agent import SkillIntelligenceAgent
from app.models.candidate_profile import CandidateProfile


class CareerPipeline:

    def __init__(self):

        self.preprocessor = ResumePreprocessor()

        self.skill_agent = SkillIntelligenceAgent(
            "data/knowledge_base/skills_knowledge_base.xlsx"
        )

        self.skill_agent.load_knowledge_base()

        self.profile = CandidateProfile()

    def run(self, pdf_path):
        """
        Execute complete pipeline.
        """

        # Step 1
        raw_text = extract_text_from_pdf(pdf_path)

        # Step 2
        clean_text = self.preprocessor.preprocess(raw_text)

        # Step 3
        matched_skills = self.skill_agent.extract_explicit_skills(clean_text)

        # Step 4
        skill_profile = self.skill_agent.build_skill_profile(
            matched_skills
        )

        # Step 5
        self.profile.add_skills(skill_profile)

        return self.profile