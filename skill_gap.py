"""
Skill Gap Analysis — compare current vs required skills with visualizations
"""

import streamlit as st
import json, re
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from utils.helpers import page_header, section_title, skill_tags
from utils.groq_client import quick_analysis
from utils.prompts import SKILL_GAP_PROMPT

ROLES = [
    "Data Scientist", "AI Engineer", "ML Engineer", "Software Engineer",
    "Data Analyst", "Full Stack Developer", "Backend Developer",
    "DevOps Engineer", "Product Manager", "Cybersecurity Analyst",
]

PLOTLY_LAYOUT = dict(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                     font=dict(color="#94A3B8"), margin=dict(l=10, r=10, t=30, b=10))


def _parse(text: str) -> dict:
    text = re.sub(r"```(?:json)?", "", text).strip().rstrip("`").strip()
    try:
        return json.loads(text)
    except Exception:
        m = re.search(r"\{[\s\S]+\}", text)
        return json.loads(m.group()) if m else {}


def show():
    page_header("🧠", "Skill Gap Analysis", "Identify exactly what skills you need for your target role")

    resume_text = st.session_state.get("resume_text", "")
    if not resume_text:
        st.warning("⚠️ Please upload your resume first.")
        return

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        section_title("🎯 Target Role")
        role = st.selectbox("Role", ROLES, label_visibility="collapsed")
        custom = st.text_input("Custom role", placeholder="Optional…")
        if custom.strip():
            role = custom.strip()
        analyze_btn = st.button("🔍 Analyze Gap", type="primary", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    if analyze_btn:
        with st.spinner("🤖 Analyzing skill gap…"):
            prompt = SKILL_GAP_PROMPT.format(role=role, resume_text=resume_text[:3500])
            raw = quick_analysis(prompt, temperature=0.3, max_tokens=1500)
            data = _parse(raw)
            st.session_state["skill_gap_data"] = data
        st.rerun()

    with col2:
        data = st.session_state.get("skill_gap_data")
        if not data:
            st.markdown("""
            <div class="glass-card" style="text-align:center; padding:60px; color:#64748b;">
                <div style="font-size:48px;">🧠</div>
                <p style="margin-top:12px;">Run analysis to see your skill gap</p>
            </div>""", unsafe_allow_html=True)
            return

        overlap = data.get("overlap_percentage", 0)
        color = "#10B981" if overlap >= 70 else "#F59E0B" if overlap >= 40 else "#EF4444"

        st.markdown(f"""
        <div class="glass-card" style="display:flex; align-items:center; gap:20px;">
            <div style="font-size:48px; font-weight:800; color:{color};">{overlap}%</div>
            <div>
                <div style="color:#E2E8F0; font-weight:600;">Skills Overlap</div>
                <div style="color:#64748b; font-size:13px;">Top priority: {data.get('top_priority', '—')}</div>
            </div>
        </div>""", unsafe_allow_html=True)

    if not st.session_state.get("skill_gap_data"):
        return

    data = st.session_state["skill_gap_data"]
    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        section_title("✅ Skills You Have")
        skill_tags(data.get("current_skills", []) or ["—"], "success")

    with c2:
        section_title("📌 Required Skills")
        skill_tags(data.get("required_skills", []) or ["—"], "warning")

    # ── Missing skills table with bar chart ──────────────────────────────────
    missing = data.get("missing_skills", [])
    if missing:
        st.markdown("<br>", unsafe_allow_html=True)
        section_title("🚨 Skills to Learn")

        df = pd.DataFrame(missing)
        if "skill" in df.columns and "weeks_to_learn" in df.columns:
            priority_colors = {"High": "#EF4444", "Medium": "#F59E0B", "Low": "#10B981"}
            df["color"] = df["priority"].map(priority_colors).fillna("#94A3B8")

            fig = go.Figure(go.Bar(
                x=df["weeks_to_learn"],
                y=df["skill"],
                orientation="h",
                marker_color=df["color"],
                text=df["weeks_to_learn"].astype(str) + " wks",
                textposition="outside",
            ))
            fig.update_layout(
                xaxis_title="Weeks to Learn",
                height=max(200, len(df) * 40),
                **PLOTLY_LAYOUT,
            )
            st.plotly_chart(fig, use_container_width=True)

            # Table
            for _, row in df.iterrows():
                p_color = priority_colors.get(row.get("priority", ""), "#94A3B8")
                st.markdown(f"""
                <div class="glass-card" style="padding:12px 16px; display:flex; justify-content:space-between; align-items:center;">
                    <div>
                        <span style="color:#E2E8F0; font-weight:500; font-size:14px;">{row.get('skill','')}</span>
                        <span style="background:rgba(124,58,237,0.2); color:#C4B5FD; font-size:11px; padding:2px 8px; border-radius:10px; margin-left:8px;">{row.get('difficulty','')}</span>
                    </div>
                    <div style="display:flex; gap:12px; align-items:center;">
                        <span style="color:#64748b; font-size:13px;">~{row.get('weeks_to_learn','?')} weeks</span>
                        <span style="color:{p_color}; font-size:12px; font-weight:600;">{row.get('priority','')} Priority</span>
                    </div>
                </div>""", unsafe_allow_html=True)
