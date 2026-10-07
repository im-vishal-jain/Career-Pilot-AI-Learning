"""
Resume parser — calls Groq to extract structured data from raw resume text
"""

import json
import re
import streamlit as st
from utils.groq_client import quick_analysis
from utils.prompts import RESUME_ANALYSIS_PROMPT


def parse_json_response(text: str) -> dict:
    """Robustly extract JSON from Groq response (strips markdown fences)."""
    text = re.sub(r"```(?:json)?", "", text).strip().rstrip("```").strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # Try to find JSON object in the text
        match = re.search(r"\{[\s\S]+\}", text)
        if match:
            try:
                return json.loads(match.group())
            except Exception:
                pass
    return {}


def analyze_resume(resume_text: str) -> dict:
    """
    Send resume text to Groq and return structured analysis dict.
    Results are cached in session state to avoid redundant API calls.
    """
    cache_key = f"resume_analysis_{hash(resume_text[:200])}"
    if cache_key in st.session_state:
        return st.session_state[cache_key]

    prompt = RESUME_ANALYSIS_PROMPT.format(resume_text=resume_text[:4000])
    raw = quick_analysis(prompt, temperature=0.3, max_tokens=2000)
    data = parse_json_response(raw)

    # Ensure all expected keys exist with defaults
    defaults = {
        "ats_score": 0,
        "skills": [],
        "education": [],
        "experience": [],
        "certifications": [],
        "projects": [],
        "strengths": [],
        "weaknesses": [],
        "missing_skills": [],
        "suggestions": [],
    }
    for k, v in defaults.items():
        data.setdefault(k, v)

    st.session_state[cache_key] = data
    st.session_state["resume_data"] = data
    st.session_state["ats_score"] = data.get("ats_score", 0)
    return data
