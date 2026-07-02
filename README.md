# CareerCopilot AI

> An AI-powered Agentic Career Intelligence Platform that helps job seekers maximize their interview shortlisting chances through intelligent resume understanding, live job matching, resume optimization, and personalized interview preparation.

---

## Problem Statement

Finding relevant jobs is one of the biggest challenges faced by fresh graduates and early-career professionals.

Current job searching involves:

- Searching across multiple job portals
- Applying randomly to hundreds of jobs
- Receiving very few interview calls
- No understanding of why resumes get rejected
- Generic ATS checkers that only perform keyword matching
- No personalized career guidance

The problem is not just finding jobs.

The real problem is **finding jobs where the candidate has the highest probability of getting shortlisted.**

CareerCopilot AI aims to solve this problem using Agentic AI.

---

# Solution

CareerCopilot AI is an intelligent multi-agent system that understands a candidate's complete professional profile instead of simply matching resume keywords.

The platform:

- Parses resumes
- Builds an intelligent candidate profile
- Understands explicit and implicit skills
- Searches live jobs
- Ranks jobs by shortlist probability
- Suggests resume improvements for each job
- Generates interview questions specific to the selected role

Instead of acting like an ATS checker,

CareerCopilot AI behaves like an AI Career Advisor.

---

# Objectives

- Reduce random job applications
- Improve interview shortlisting probability
- Recommend only highly relevant jobs
- Personalize resume improvements
- Generate role-specific interview preparation
- Build an explainable AI-powered career guidance platform

---

# 🏗️ System Architecture

```
Resume Upload
        │
        ▼
Resume Parser
        │
        ▼
Resume Preprocessor
        │
        ▼
Candidate Intelligence Engine
        │
        ├──────────────┐
        ▼              ▼
Skill Agent      Contact Agent
        │              │
        └──────┬───────┘
               ▼
Candidate Profile
               │
               ▼
Job Discovery Agent
               │
               ▼
Job Matching Agent
               │
               ▼
Resume Review Agent
               │
               ▼
Interview Preparation Agent
               │
               ▼
Career Guidance Report
```

Future versions will use **LangGraph** for agent orchestration.

---

# 🤖 AI Agents

## Resume Parser Agent

Responsible for

- PDF parsing
- Text extraction
- Resume preprocessing

---

## Skill Intelligence Agent

Responsible for

- Explicit skill extraction
- Skill normalization
- Skill categorization
- AI-based implicit skill inference (planned)
- Skill confidence estimation
- Skill gap analysis

---

## Candidate Profile Agent

Builds a structured candidate profile containing

- Contact information
- Skills
- Education
- Experience
- Projects
- Certifications
- Career preferences

---

## Job Discovery Agent (Planned)

Searches live jobs from multiple platforms.

Examples:

- LinkedIn
- Naukri
- Indeed
- Foundit
- Wellfound

---

## Job Matching Agent (Planned)

Ranks jobs using

- Skill similarity
- Project relevance
- Education match
- Experience match
- Resume strength

Returns only high-confidence recommendations.

---

## Resume Review Agent (Planned)

Compares the resume against the selected job description.

Provides

- Missing skills
- Resume improvements
- Keyword suggestions
- Resume optimization tips

---

## Interview Preparation Agent (Planned)

Generates

- Technical interview questions
- HR interview questions
- Role-specific preparation roadmap
- Learning recommendations

---

# Tech Stack

### Programming

- Python

### AI / LLM

- Google Gemini API
- LangGraph (Planned)

### Machine Learning

- Scikit-Learn
- Sentence Transformers (Planned)

### NLP

- Regex
- SpaCy (Planned)

### Backend

- FastAPI (Planned)

### Frontend

- Streamlit (Planned)

### Database

- SQLite (Development)
- PostgreSQL (Future)

### Version Control

- Git
- GitHub

---

# Project Structure

```
CareerCopilotAI/

│

├── app/

│ ├── agents/

│ ├── models/

│ ├── parsers/

│ ├── preprocessors/

│ ├── pipeline.py

│ └── main.py

│

├── data/

│ ├── knowledge_base/

│ ├── outputs/

│ └── resumes/

│

├── tests/

│

├── requirements.txt

│

└── README.md
```

---

# Current Features

- Resume PDF parsing
- Resume text preprocessing
- Contact information extraction
- Skill knowledge base
- Explicit skill extraction
- Skill categorization
- Candidate Profile model
- Modular pipeline architecture
- Git version control

---

# Planned Features

### Version 2

- Gemini-powered Skill Intelligence
- Implicit skill inference
- Skill confidence estimation
- Candidate intelligence scoring

---

### Version 3

- Live Job Discovery
- Multi-platform job search
- Semantic job matching
- Match score explanation

---

### Version 4

- Resume optimization
- Resume improvement suggestions
- ATS optimization

---

### Version 5

- Interview preparation
- AI-generated interview questions
- Personalized career roadmap

---

# 🔬 Research Ideas

CareerCopilot AI explores several AI concepts:

- Agentic AI
- Multi-Agent Systems
- Resume Intelligence
- Career Intelligence
- Semantic Skill Matching
- LLM-based Reasoning
- AI Recommendation Systems
- Retrieval-Augmented Generation (Future)

---

# Development Status

| Module | Status |
|---------|--------|
| Resume Parser | ✅ |
| Resume Preprocessor | ✅ |
| Contact Parser | ✅ |
| Skill Intelligence Agent | ✅ |
| Candidate Profile | ✅ |
| Career Pipeline | ✅ |
| Gemini Skill Intelligence | 🚧 |
| Job Discovery Agent | 🚧 |
| Job Matching Agent | 🚧 |
| Resume Review Agent | 🚧 |
| Interview Preparation Agent | 🚧 |

---

# Key Highlights

✔ Modular Architecture

✔ Agent-Based Design

✔ Production-Oriented Folder Structure

✔ Extensible Pipeline

✔ AI-Powered Resume Intelligence

✔ Live Job Matching (Planned)

✔ Explainable Career Recommendations

✔ Built for Real-World Job Seekers

---

# Contributions

Contributions, ideas and feedback are always welcome.

Feel free to open an issue or submit a pull request.
