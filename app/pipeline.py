from app.parsers.contact_parser import (
    extract_name,
    extract_email,
    extract_phone,
    extract_linkedin,
    extract_github
)


from app.parsers.pdf_parser import extract_text_from_pdf
from app.preprocessors.resume_preprocessor import ResumePreprocessor
from app.agents.skills_intelligence_agent import SkillIntelligenceAgent
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
        name = extract_name(clean_text)
        email = extract_email(clean_text)
        phone = extract_phone(clean_text)
        linkedin = extract_linkedin(clean_text)
        github = extract_github(clean_text)
        
        # Step 4: Update Candidate Profile
        self.profile.update_personal_information(
            name=name,
            email=email,
            phone=phone,
            linkedin=linkedin,
            github=github
            )


        # Step 5: Extract Skills
        matched_skills = self.skill_agent.extract_explicit_skills(clean_text)

        # Step 6: Build Structured skill profile
        skill_profile = self.skill_agent.build_skill_profile(
            matched_skills
        )

        # Step 7: Add skills to candidate profile
        self.profile.add_skills(skill_profile)
        
        # Step 8: Save profile
        self.profile.save_as_json(
            "data/outputs/candidate_profile.json"
            )


        return self.profile