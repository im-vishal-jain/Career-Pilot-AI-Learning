"""
Resume Analyzer — upload, parse, and AI-analyze resumes
"""

import streamlit as st
from utils.helpers import page_header, section_title, skill_tags
from utils.pdf_parser import parse_uploaded_file, clean_text
from utils.resume_parser import analyze_resume
from utils.database import save_session


def show():
    page_header("📄", "Resume Analyzer", "Upload your resume and get deep AI-powered insights")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        section_title("📁 Upload Resume")
        uploaded = st.file_uploader("Choose your resume file", type=["pdf", "docx", "txt"],
                                    label_visibility="collapsed")

        if uploaded:
            with st.spinner("Extracting text…"):
                raw = parse_uploaded_file(uploaded)
                text = clean_text(raw)
                st.session_state["resume_text"] = text

            st.success(f"✅ Extracted {len(text.split())} words from {uploaded.name}")

            with st.expander("Preview extracted text"):
                st.text_area("", text[:1500] + ("…" if len(text) > 1500 else ""),
                             height=200, disabled=True)

        elif st.session_state.get("resume_text"):
            st.info("Using previously uploaded resume")
            text = st.session_state["resume_text"]

        # Manual paste option
        st.markdown("---")
        section_title("✏️ Or Paste Resume Text")
        pasted = st.text_area("Paste your resume content here", height=160,
                              placeholder="Copy and paste your resume text…")
        if pasted.strip():
            text = pasted.strip()
            st.session_state["resume_text"] = text

        analyze_btn = st.button("🔍 Analyze Resume", type="primary",
                                use_container_width=True,
                                disabled=not st.session_state.get("resume_text"))
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        if st.session_state.get("resume_data"):
            _display_results(st.session_state["resume_data"])

    if analyze_btn and st.session_state.get("resume_text"):
        with st.spinner("🤖 Analyzing your resume with AI…"):
            data = analyze_resume(st.session_state["resume_text"])
            save_session(
                st.session_state.get("user_id", 1),
                st.session_state["resume_text"][:500],
                data.get("ats_score", 0),
                {},
            )
        st.rerun()


def _display_results(data: dict):
    ats = data.get("ats_score", 0)
    color = "#10B981" if ats >= 75 else "#F59E0B" if ats >= 50 else "#EF4444"
    label = "Excellent" if ats >= 75 else "Good" if ats >= 50 else "Needs Work"

    st.markdown(f"""
    <div class="glass-card" style="text-align:center;">
        <div style="font-size:56px; font-weight:800; color:{color};">{ats}</div>
        <div style="font-size:20px; color:{color}; margin-top:4px;">ATS Score · {label}</div>
        <div style="margin:16px 0;">
    """, unsafe_allow_html=True)
    st.progress(ats / 100)
    st.markdown("</div></div>", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["📊 Overview", "💡 Suggestions", "🛠️ Details"])

    with tab1:
        r1, r2 = st.columns(2)
        with r1:
            section_title("✅ Skills Detected")
            skill_tags(data.get("skills", []) or ["None detected"], "success")
            section_title("🎓 Education")
            for e in data.get("education", []) or ["—"]:
                st.markdown(f"- {e}")
            section_title("📜 Certifications")
            certs = data.get("certifications", [])
            skill_tags(certs if certs else ["None listed"], "default")
        with r2:
            section_title("💼 Experience")
            for e in data.get("experience", []) or ["—"]:
                st.markdown(f"- {e}")
            section_title("🚀 Projects")
            for p in data.get("projects", []) or ["—"]:
                st.markdown(f"- {p}")

    with tab2:
        r1, r2 = st.columns(2)
        with r1:
            section_title("💪 Strengths")
            for s in data.get("strengths", []) or ["—"]:
                st.markdown(f'<div style="color:#6EE7B7; font-size:14px; margin:4px 0;">✓ {s}</div>',
                            unsafe_allow_html=True)
            section_title("🚨 Missing Skills")
            skill_tags(data.get("missing_skills", []) or ["None detected"], "missing")
        with r2:
            section_title("⚠️ Weaknesses")
            for w in data.get("weaknesses", []) or ["—"]:
                st.markdown(f'<div style="color:#FCA5A5; font-size:14px; margin:4px 0;">✗ {w}</div>',
                            unsafe_allow_html=True)

        section_title("💡 AI Suggestions")
        for i, sug in enumerate(data.get("suggestions", []) or ["No suggestions available"], 1):
            st.markdown(f"""
            <div class="glass-card" style="padding:12px 16px; margin:6px 0;">
                <span style="color:#7C3AED; font-weight:600; margin-right:8px;">{i}.</span>
                <span style="color:#E2E8F0; font-size:14px;">{sug}</span>
            </div>""", unsafe_allow_html=True)

    with tab3:
        section_title("📋 Section Scores")
        sections = {
            "Skills": min(100, len(data.get("skills", [])) * 8),
            "Experience": min(100, len(data.get("experience", [])) * 20),
            "Projects": min(100, len(data.get("projects", [])) * 25),
            "Education": min(100, len(data.get("education", [])) * 30),
            "Certifications": min(100, len(data.get("certifications", [])) * 15 + 40),
        }
        for sec, score in sections.items():
            sc1, sc2 = st.columns([2, 3])
            with sc1:
                st.markdown(f'<div style="color:#94A3B8; font-size:14px;">{sec}</div>', unsafe_allow_html=True)
            with sc2:
                st.progress(score / 100)
