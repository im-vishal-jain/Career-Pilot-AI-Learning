"""
Job Matcher — AI-powered job-role compatibility analysis
"""

import streamlit as st
import json, re
import plotly.graph_objects as go
from utils.helpers import page_header, section_title, skill_tags, metric_card
from utils.groq_client import quick_analysis
from utils.prompts import JOB_MATCH_PROMPT
from utils.database import save_session

ROLES = [
    "Data Scientist", "AI Engineer", "ML Engineer", "Software Engineer",
    "Data Analyst", "Full Stack Developer", "Backend Developer",
    "Frontend Developer", "DevOps Engineer", "Product Manager",
    "Cybersecurity Analyst", "Cloud Architect",
]

PLOTLY_LAYOUT = dict(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                     font=dict(color="#94A3B8"), margin=dict(l=10, r=10, t=30, b=10))


def _parse_json(text: str) -> dict:
    text = re.sub(r"```(?:json)?", "", text).strip().rstrip("`").strip()
    try:
        return json.loads(text)
    except Exception:
        m = re.search(r"\{[\s\S]+\}", text)
        return json.loads(m.group()) if m else {}


def show():
    page_header("🎯", "Job Matcher", "See how well your resume fits your target role")

    resume_text = st.session_state.get("resume_text", "")
    if not resume_text:
        st.warning("⚠️ Please upload and analyze your resume first in **Resume Analyzer**.")
        if st.button("Go to Resume Analyzer", type="primary"):
            st.session_state.current_page = "resume_analyzer"; st.rerun()
        return

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        section_title("🎯 Choose Target Role")
        role = st.selectbox("Target Role", ROLES, label_visibility="collapsed")
        custom_role = st.text_input("Or enter a custom role", placeholder="e.g. Quant Analyst")
        if custom_role.strip():
            role = custom_role.strip()

        match_btn = st.button("⚡ Calculate Match", type="primary", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        if st.session_state.get("job_match"):
            data = st.session_state["job_match"]
            st.markdown("<br>", unsafe_allow_html=True)
            metric_card(f"{data.get('match_percentage', 0)}%", "Match Score")
            st.markdown("<br>", unsafe_allow_html=True)
            metric_card(data.get("salary_range", "—"), "Salary Range")
            st.markdown("<br>", unsafe_allow_html=True)
            demand = data.get("demand_level", "—")
            color = {"High": "#10B981", "Medium": "#F59E0B", "Low": "#EF4444"}.get(demand, "#94A3B8")
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value" style="font-size:22px; color:{color};">{demand}</div>
                <div class="metric-label">Market Demand</div>
            </div>""", unsafe_allow_html=True)

    with col2:
        if match_btn:
            with st.spinner(f"🤖 Analyzing match for {role}…"):
                prompt = JOB_MATCH_PROMPT.format(role=role, resume_text=resume_text[:4000])
                raw = quick_analysis(prompt, temperature=0.3, max_tokens=1500)
                data = _parse_json(raw)
                st.session_state["job_match"] = data
                save_session(
                    st.session_state.get("user_id", 1),
                    resume_text[:200],
                    st.session_state.get("ats_score", 0),
                    data,
                )
            st.rerun()

        data = st.session_state.get("job_match")
        if not data:
            st.markdown("""
            <div class="glass-card" style="text-align:center; padding:60px 20px; color:#64748b;">
                <div style="font-size:56px;">🎯</div>
                <p style="margin-top:16px; font-size:16px;">Select a role and click <b>Calculate Match</b></p>
            </div>""", unsafe_allow_html=True)
            return

        match_pct = data.get("match_percentage", 0)
        color = "#10B981" if match_pct >= 70 else "#F59E0B" if match_pct >= 45 else "#EF4444"

        # Match gauge
        fig = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=match_pct,
            delta={"reference": 70, "increasing": {"color": "#10B981"}},
            gauge=dict(
                axis=dict(range=[0, 100], tickcolor="#475569"),
                bar=dict(color=color),
                bgcolor="rgba(30,41,59,0.5)",
                steps=[
                    dict(range=[0, 45], color="rgba(239,68,68,0.1)"),
                    dict(range=[45, 70], color="rgba(245,158,11,0.1)"),
                    dict(range=[70, 100], color="rgba(16,185,129,0.1)"),
                ],
            ),
            number=dict(suffix="%", font=dict(color=color, size=36)),
        ))
        fig.update_layout(height=220, **PLOTLY_LAYOUT)
        st.plotly_chart(fig, use_container_width=True)

        if data.get("fit_summary"):
            st.markdown(f"""
            <div class="glass-card" style="border-left:3px solid #7C3AED;">
                <p style="color:#E2E8F0; font-size:14px; line-height:1.7;">{data['fit_summary']}</p>
            </div>""", unsafe_allow_html=True)

        tab1, tab2, tab3 = st.tabs(["🛠️ Skills", "📋 Requirements", "💡 Recommendations"])

        with tab1:
            c1, c2 = st.columns(2)
            with c1:
                section_title("✅ Matched Skills")
                skill_tags(data.get("matched_skills", []) or ["None"], "success")
            with c2:
                section_title("🚨 Missing Skills")
                skill_tags(data.get("missing_skills", []) or ["None"], "missing")

        with tab2:
            section_title("🔧 Required Technologies")
            skill_tags(data.get("required_technologies", []) or ["—"], "warning")

        with tab3:
            section_title("💡 AI Recommendations")
            for i, rec in enumerate(data.get("recommendations", []) or ["—"], 1):
                st.markdown(f"""
                <div class="glass-card" style="padding:12px 16px; margin:6px 0;">
                    <span style="color:#3B82F6; font-weight:600;">{i}.</span>
                    <span style="color:#E2E8F0; font-size:14px; margin-left:8px;">{rec}</span>
                </div>""", unsafe_allow_html=True)
