"""
Prompt templates for all Career Copilot AI features.
Centralised here for easy tuning and versioning.
"""

# ── Resume Analyzer ──────────────────────────────────────────────────────────
RESUME_ANALYSIS_PROMPT = """You are an expert ATS resume analyst and career coach.
Analyze the following resume and return a JSON object with EXACTLY this structure:
{{
  "ats_score": <integer 0-100>,
  "skills": ["skill1", "skill2", ...],
  "education": ["degree, institution, year", ...],
  "experience": ["job title at company (years)", ...],
  "certifications": ["cert1", ...],
  "projects": ["Project Name: brief description", ...],
  "strengths": ["strength1", ...],
  "weaknesses": ["weakness1", ...],
  "missing_skills": ["skill1", ...],
  "suggestions": ["suggestion1", ...]
}}

Return ONLY valid JSON. No markdown, no explanation.

RESUME:
{resume_text}
"""

# ── Job Matcher ──────────────────────────────────────────────────────────────
JOB_MATCH_PROMPT = """You are a technical recruiter and job market expert.
Given this resume and target role, return a JSON object:
{{
  "match_percentage": <integer 0-100>,
  "matched_skills": ["skill1", ...],
  "missing_skills": ["skill1", ...],
  "required_technologies": ["tech1", ...],
  "salary_range": "e.g. $90,000 – $130,000",
  "demand_level": "High|Medium|Low",
  "fit_summary": "2–3 sentence summary",
  "recommendations": ["rec1", ...]
}}

Return ONLY valid JSON.

TARGET ROLE: {role}
RESUME:
{resume_text}
"""

# ── Skill Gap ────────────────────────────────────────────────────────────────
SKILL_GAP_PROMPT = """You are a technical skills advisor.
Compare current skills to those required for the target role and return JSON:
{{
  "current_skills": ["skill1", ...],
  "required_skills": ["skill1", ...],
  "missing_skills": [
    {{"skill": "name", "priority": "High|Medium|Low", "difficulty": "Beginner|Intermediate|Advanced", "weeks_to_learn": <int>}}
  ],
  "overlap_percentage": <int 0-100>,
  "top_priority": "Most urgent skill to learn"
}}

Return ONLY valid JSON.

ROLE: {role}
RESUME / CURRENT SKILLS:
{resume_text}
"""

# ── Learning Roadmap ─────────────────────────────────────────────────────────
ROADMAP_PROMPT = """You are a learning path architect and career mentor.
Create a personalized learning roadmap for someone targeting the role of {role} with the following background:
{background}

Duration: {duration}

Structure your response as follows (use clear markdown headings and bullet points):

## 🎯 Goal Overview
Brief summary of the journey.

## 📅 Phase 1 — Foundations (First {phase1})
### Topics to Study
- ...
### Beginner Projects
- ...

## 📅 Phase 2 — Intermediate ({phase2})
### Topics to Study
- ...
### Projects
- ...

## 📅 Phase 3 — Advanced ({phase3})
### Topics
- ...
### Industry Projects
- ...

## 📚 Resources
### YouTube Channels
- ...
### Online Courses (free & paid)
- ...
### Books
- ...
### GitHub Repositories
- ...

## 💡 Pro Tips
- ...
"""

# ── Interview Coach ──────────────────────────────────────────────────────────
INTERVIEW_QUESTIONS_PROMPT = """You are an expert interview coach.
Generate interview questions for the role of {role} and return a JSON array:
[
  {{
    "question": "...",
    "type": "Technical|Behavioral|HR|Scenario",
    "difficulty": "Easy|Medium|Hard",
    "ideal_answer": "...",
    "tips": "..."
  }},
  ...
]
Generate exactly {count} questions with a mix of types.
Return ONLY valid JSON array.
"""

ANSWER_EVALUATION_PROMPT = """You are an expert interview coach evaluating a candidate's answer.
Role: {role}
Question: {question}
Candidate's Answer: {answer}

Evaluate and respond in JSON:
{{
  "score": <int 1-10>,
  "feedback": "detailed constructive feedback",
  "strengths": ["what they did well"],
  "improvements": ["what to improve"],
  "ideal_answer_points": ["key points they should have covered"]
}}
Return ONLY valid JSON.
"""

# ── Cover Letter ─────────────────────────────────────────────────────────────
COVER_LETTER_PROMPT = """You are a professional cover letter writer.
Write a compelling, personalized, ATS-friendly cover letter for:

Applicant Background (from resume):
{resume_text}

Target Company: {company}
Target Role: {role}
Tone: {tone}

Requirements:
- 3–4 paragraphs (opening, why them, why you, closing)
- Specific and confident, avoid clichés
- Reference actual skills/experience from the resume
- Include a call to action
- Professional but human tone
- 300–400 words

Write only the cover letter text, no instructions or meta-commentary.
"""

# ── Career Recommendation ─────────────────────────────────────────────────────
CAREER_RECOMMENDATION_PROMPT = """You are a career counselor and labor market expert.
Based on the user's profile, suggest career paths in JSON:
{{
  "recommended_paths": [
    {{
      "title": "Career Title",
      "match_score": <int 0-100>,
      "description": "2 sentence description",
      "salary_range": "e.g. $70k–$120k",
      "growth_trend": "Rapid/Steady/Declining",
      "key_technologies": ["tech1", ...],
      "time_to_ready": "e.g. 3–6 months"
    }}
  ],
  "top_pick": "Career Title",
  "reasoning": "Why this is the best match"
}}

Return 4–5 career paths. Return ONLY valid JSON.

USER PROFILE:
Interests: {interests}
Current Skills: {skills}
Goals: {goals}
Experience Level: {experience}
"""

# ── ATS Score Detailed ────────────────────────────────────────────────────────
ATS_DETAILED_PROMPT = """You are an ATS (Applicant Tracking System) expert.
Analyze this resume for ATS compatibility and return JSON:
{{
  "overall_score": <int 0-100>,
  "keyword_score": <int 0-100>,
  "format_score": <int 0-100>,
  "readability_score": <int 0-100>,
  "section_scores": {{
    "contact_info": <int>,
    "summary": <int>,
    "experience": <int>,
    "education": <int>,
    "skills": <int>
  }},
  "keywords_found": ["kw1", ...],
  "keywords_missing": ["kw1", ...],
  "format_issues": ["issue1", ...],
  "quick_wins": ["fix1", ...]
}}
Return ONLY valid JSON.

RESUME:
{resume_text}
"""
